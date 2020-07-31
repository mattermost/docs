Configuration in the Mattermost Database
=========================================

A new configuration option was added in `5.10 release <https://docs.mattermost.com/administration/changelog.html#configuration-in-database>`_ to use the database as the single source of truth for the active configuration of your Mattermost installation. This will change the Mattermost binary from reading the default ``config.json`` file to reading the configuration settings stored within a configuration table in the database.

Mattermost has been running our `community server <https://community.mattermost.com>`_ on this option since the feature was released, and recommends its use for those on :doc:`High Availability deployments <cluster>`.

Benefits to using this option:

  - Conveniently manage configuration changes directly from the System Console, even in High Availability deployments and read-only containerized environments.
  - Ensure all servers in a High Availability deployment have the same configuration, even when new servers are added to the cluster.
  - Automatically deploy SAML certificates and keys to all servers in the cluster.

How to Migrate Configuration to the Database
--------------------------------------------

These instructions cover migrating the Mattermost configuration to the database and updating your ``systemd`` configuration to load it from the database.

.. note::
  These instructions assume you have Mattermost server installed at ``/opt/mattermost`` If you are running Mattermost in a different directory you will have to modify the paths to match your environment.

1. Get your Database Connection String
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first step is to get your master database connection string. There are several ways to do this, but the easiest is to use ``mattermost config get`` command like this:

.. code-block:: bash

   sudo su mattermost
   cd /opt/mattermost
   bin/mattermost config get SqlSettings.DataSource

Example Output:

.. code-block:: text

   SqlSettings.DataSource: "mmuser:really_secure_password@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8\u0026readTimeout=30s\u0026writeTimeout=30s"

**NOTE:** Be sure to run this command as the ``mattermost`` user and *not* root. Running the Mattermost binary as root will cause permissions errors.

Another way is to view your ``config.json`` file and get the value in ``SqlSettings.DataSource``. 

If ``SqlSettings.DataSource`` does not start with ``postgres://`` then you have to add ``mysql://`` to the beginning. Also, if you see ``\u0026`` replace it with ``&``.

Here are two example connection strings:

*MySQL*

.. code-block:: text

   mysql://mmuser:really_secure_password@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8&readTimeout=30s&writeTimeout=30s

*PostgreSQL*

.. code-block:: text

   postgres://mmuser:really_secure_password@localhost:5432/mattermost?sslmode=disable&connect_timeout=10

2. Create Environment File:
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
  If you are running Mattermost in an HA cluster this step must be done on **all** servers in the cluster. 

Create the file  ``/opt/mattermost/config/mattermost.environment``  to set the ``MM_CONFIG`` environment variable to the database connection string. For example:

*MySQL*

.. code-block:: text

   MM_CONFIG='mysql://mmuser:mostest@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8&readTimeout=30s&writeTimeout=30s'

*PostgreSQL*

.. code-block:: text

   MM_CONFIG='postgres://mmuser:mostest@localhost:5432/mattermost_test?sslmode=disable&connect_timeout=10'

.. note::
  Be sure to escape any single quotes in the database connection string by placing a ``\`` in front of them like this ``\'``. For example: ``MM_CONFIG='mysql://mmuser:it\'s-a-password!@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8&readTimeout=30s&writeTimeout=30s'``

.. code-block:: text

   MM_CONFIG='mysql://mmuser:it\'s-a-password!@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8&readTimeout=30s&writeTimeout=30s'

Finally, run this command to verify the permissions on your Mattermost directory:

.. code-block:: bash

   sudo chown -R mattermost:mattermost /opt/mattermost

3. Modify Mattermost systemd file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, find the ``mattermost.service`` file by first running this command:

.. code-block:: bash

   sudo systemctl status mattermost.service

The second line of output will have the location of the running ``mattermost.service``

.. code-block:: text

      Loaded: loaded (/lib/systemd/system/mattermost.service; enabled; vendor preset: enabled)

Edit this file as *root* to add this line just before the line that beings with ``ExecStart``\ :

.. code-block:: text

   EnvironmentFile=/opt/mattermost/config/mm.environment

Here is a complete ``mattermost.service`` file with the ``EnvironmentFile`` line added:

.. code-block:: text

   [Unit]
   Description=Mattermost
   After=network.target
   After=mysql.service
   Requires=mysql.service

   [Service]
   Type=notify
   EnvironmentFile=/opt/mattermost/config/mm.environment
   ExecStart=/opt/mattermost/bin/mattermost
   TimeoutStartSec=3600
   Restart=always
   RestartSec=10
   WorkingDirectory=/opt/mattermost
   User=mattermost
   Group=mattermost
   LimitNOFILE=49152

   [Install]
   WantedBy=mysql.service

.. note::
  If you are using PostgreSQL as your database the ``mysql.service`` must be replaced with ``postgresql.service``. The easiest way to avoid making a mistake is to just add the ``EnvironmentFile`` line and not copy the entire example.

4. Migrate configuration from ``config.json``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
  If you are using an HA cluster you only need to run this on a single server in the cluster.

Like before, the command to migrate the config to the database should always be run as the *mattermost* user.

.. code-block:: bash

   sudo su mattermost
   cd /opt/mattermost
   bin/mattermost config migrate ./config/config.json 'mysql://mmuser:mostest@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8&readTimeout=30s&writeTimeout=30s'

As with the environment file you will have to escape any single quotes in the database connection string. Also, any existing SAML certificates will be migrated into the database as well so they are available for all servers in the cluster. 

With configuration in the database enabled, any changes to the configuration are recorded to the ``Configurations`` and ``ConfigurationFiles`` tables. Furthermore, ``ClusterSettings.ReadOnlyConfig`` is ignored, enabling full use of the System Console.

If you have configuration settings that must be set on a per-server basis you should add them as environment variables to the ``mm.environment`` file. These must be on their own line, and you must escape them properly.

5. Verify that the configuration was migrated correctly.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configurations are stored in the ``Configurations`` table in the database. To verify that you have migrated the configuration successfully run this query:

.. code-block:: sql

   SELECT * FROM Configurations WHERE Active = 1;

There should be exactly one line returned, and the ``Value`` field for that line should match your ``config.json`` file.

6. Reload ``systemd`` files and restart Mattermost
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
  If you are running Mattermost in HA this step must be run on all servers in the cluster.

Finally, run these commands to reload the daemon and restart Mattermost using the new ``MM_CONFIG`` environment variable.

.. code-block:: text

   sudo systemctl daemon-reload
   sudo systemctl restart mattermost

Rolling Back
^^^^^^^^^^^^

If you run into issues with your configuration in the database you can roll back to the ``config.json`` file by commenting out the ``MM_CONFIG`` line in ``/opt/mattermost/config/mm.environment`` and restarting Mattermost with ``systemctl restart mattermost``

Troubleshooting
-----------------

Server fails to start 
~~~~~~~~~~~~~~~~~~~~~
Providing the ``--disableconfigwatch`` flag while not actually pointing at a file will fail to start the server with an appropriate error message.
