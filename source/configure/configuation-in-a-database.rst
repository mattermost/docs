Configuration in a database
============================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

A new configuration option was added in the `5.10 release </install/self-managed-changelog.html>`_ to use the database as the single source of truth for the active configuration of your Mattermost installation. This changes the Mattermost binary from reading the default ``config.json`` file to reading the configuration settings stored within a configuration table in the database.

Mattermost has been running our `community server <https://community.mattermost.com>`__ on this option since the feature was released, and recommends its use for those on :doc:`High Availability deployments <../scale/high-availability-cluster>`.

Benefits to using this option:

* Conveniently manage configuration changes directly from the System Console, even in High Availability deployments and read-only containerized environments.
* Ensure all servers in a High Availability deployment have the same configuration, even when new servers are added to the cluster.
* Automatically deploy SAML certificates and keys to all servers in the cluster.

Note that once you start using configuration in the database, you shouldn't manually edit the active configuration row. You should edit or update the configuration in one of the following ways:

* Use the System Console to make changes to the configuration.
* Use ``mmctl`` to make changes to the configuration.
* Stop any of the running mattermost-server instances and edit the active configuration row directly in the ``Configurations`` table.

The Mattermost server keeps active configuration in memory and writes new ones to the database only when there is a change. This way we avoid polling the database to process changes to the configuration. Publishing the changes to the cluster are handled by the application itself.

How to migrate configuration to the database
--------------------------------------------

These instructions cover migrating the Mattermost configuration to the database and updating your ``systemd`` configuration to load it from the database.

.. note::
  These instructions assume you have Mattermost server installed at ``/opt/mattermost``. If you're running Mattermost in a different directory you'll have to modify the paths to match your environment.

Get your database connection string
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first step is to get your master database connection string. We recommend using the `mmctl config get command </manage/mmctl-command-line-tool.html#mmctl-config-get>`__, or using the CLI's ``mattermost config get`` command to do this.  

To use the ``mattermost config get`` command:

.. code-block:: bash

   sudo su mattermost
   cd /opt/mattermost
   mmctl config get SqlSettings.DataSource

Example output:

.. code-block:: text

   "mmuser:really_secure_password@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8\u0026writeTimeout=30s"

Another way to get your database connection string is to view your ``config.json`` file and get the value in ``SqlSettings.DataSource``.

If ``SqlSettings.DataSource`` does not start with ``postgres://`` or ``mysql://``, then you have to add this line to the beginning based on the database in use. Also, if you see ``\u0026`` replace it with ``&``.

Here are two example connection strings:

**MySQL**

.. code-block:: text

   mysql://mmuser:really_secure_password@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8&writeTimeout=30s

**PostgreSQL**

.. code-block:: text

   postgres://mmuser:really_secure_password@localhost:5432/mattermost?sslmode=disable&connect_timeout=10

Create an environment file
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
   
   If you're running Mattermost in a High Availability cluster, this step must be done on all servers in the cluster.

Create the file ``/opt/mattermost/config/mattermost.environment`` to set the ``MM_CONFIG`` environment variable to the database connection string. For example:

**MySQL**

.. code-block:: text

   MM_CONFIG='mysql://mmuser:mostest@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8&writeTimeout=30s'

**PostgreSQL**

.. code-block:: text

   MM_CONFIG='postgres://mmuser:mostest@localhost:5432/mattermost_test?sslmode=disable&connect_timeout=10'

.. note::
  Be sure to escape any single quotes in the database connection string by placing a ``\`` in front of them like this ``\'``. For example: ``MM_CONFIG='mysql://mmuser:it\'s-a-password!@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8&writeTimeout=30s'``

.. code-block:: text

   MM_CONFIG='mysql://mmuser:it\'s-a-password!@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8&writeTimeout=30s'

Finally, run this command to verify the permissions on your Mattermost directory:

.. code-block:: bash

   sudo chown -R mattermost:mattermost /opt/mattermost

Modify the Mattermost ``systemd`` file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, find the ``mattermost.service`` file using:

.. code-block:: bash

   sudo systemctl status mattermost.service

The second line of output will have the location of the running ``mattermost.service``.

.. code-block:: text

      Loaded: loaded (/lib/systemd/system/mattermost.service; enabled; vendor preset: enabled)

Edit this file as *root* to add the below text just above the line that begins with ``ExecStart``\ :

.. code-block:: text

   EnvironmentFile=/opt/mattermost/config/mattermost.environment

Here's a complete ``mattermost.service`` file with the ``EnvironmentFile`` line added:

.. code-block:: text

   [Unit]
   Description=Mattermost
   After=network.target
   After=mysql.service
   Requires=mysql.service

   [Service]
   Type=notify
   EnvironmentFile=/opt/mattermost/config/mattermost.environment
   ExecStart=/opt/mattermost/bin/mattermost
   TimeoutStartSec=3600
   KillMode=mixed
   Restart=always
   RestartSec=10
   WorkingDirectory=/opt/mattermost
   User=mattermost
   Group=mattermost
   LimitNOFILE=49152

   [Install]
   WantedBy=mysql.service

.. note::
  If you're using PostgreSQL as your database, the ``mysql.service`` must be replaced with ``postgresql.service``. The easiest way to avoid making a mistake is to add only the ``EnvironmentFile`` line and not copy the entire example.

Migrate configuration from ``config.json``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the `mmctl config migrate </manage/mmctl-command-line-tool.html#mmctl-config-migrate>`__ command, or you can use the CLI mattermost config migrate command for this step, as described below.

.. note::
 
   If you're using a High Availability cluster, you only need to run this on a single server in the cluster.

The CLI command to migrate the config to the database should always be run as the *mattermost* user.

.. code-block:: bash

   sudo su mattermost
   cd /opt/mattermost
   mmctl config migrate ./config/config.json 'mysql://mmuser:mostest@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8&writeTimeout=30s'

.. warning::
   When migrating config, Mattermost will incorporate configuration from any existing ``MM_*`` environment variables set in the current shell. See `Environment Variables  </configure/configuration-settings.html>`_
   
As with the environment file, you'll have to escape any single quotes in the database connection string. Also, any existing SAML certificates will be migrated into the database as well so they are available for all servers in the cluster.

When configuration in the database is enabled, any changes to the configuration are recorded to the ``Configurations`` and ``ConfigurationFiles`` tables. Furthermore, ``ClusterSettings.ReadOnlyConfig`` is ignored, enabling full use of the System Console.

If you have configuration settings that must be set on a per-server basis you should add them as environment variables to the ``mattermost.environment`` file. These must be on their own line, and you must escape them properly.

Verify that the configuration was migrated correctly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configurations are stored in the ``Configurations`` table in the database. To verify that you've migrated the configuration successfully run this query:

.. code-block:: sql

   SELECT * FROM Configurations WHERE Active = 1;

There should be exactly one line returned, and the ``Value`` field for that line should match your ``config.json`` file.

Reload ``systemd`` files and restart Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
  If you're running Mattermost in High Availability this step must be run on all servers in the cluster.

Finally, run these commands to reload the daemon and restart Mattermost using the new ``MM_CONFIG`` environment variable.

.. code-block:: text

   sudo systemctl daemon-reload
   sudo systemctl restart mattermost

Rolling back
~~~~~~~~~~~~

If you run into issues with your configuration in the database you can roll back to the ``config.json`` file by commenting out the ``MM_CONFIG`` line in ``/opt/mattermost/config/mattermost.environment`` and restarting Mattermost with ``systemctl restart mattermost``.

Troubleshooting
-----------------

Server fails to start 
~~~~~~~~~~~~~~~~~~~~~

Providing the ``--disableconfigwatch`` flag while not actually pointing at a file will fail to start the server with an appropriate error message.
