Configuration in the Mattermost Database
=========================================
A new configuration option was added in `5.10 release <https://docs.mattermost.com/administration/changelog.html#configuration-in-database>`_ to use the database as the single source of truth for the active configuration of your Mattermost installation. This will change the Mattermost binary from reading the default config.json file to reading the configuration settings stored within a configuration table in the database. 

Mattermost has been running our `community server <https://community.mattermost.com>`_ on this option since the feature was released, and recommends its use for those on :doc:`High Availability deployments <cluster>`.

Benefits to using this option:

  - Conveniently manage configuration changes directly from the System Console, even in High Availability deployments and read-only containerized environments.
  - Ensure all servers in a High Availability deployment have the same configuration, even when new servers are added to the cluster.
  - Automatically deploy SAML certificates and keys to all servers in the cluster.

To start using configuration in database, pass the database connection string via the ``--config`` flag or ``MM_CONFIG`` environment variable. For example:

  .. code-block:: 
  
    ./mattermost --config="postgres://mmuser:mostest@dockerhost:5432/mattermost_test?sslmode=disable\u0026connect_timeout=10"

To migrate an existing config.json into the database, use the ``config migrate`` `command <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-config-migrate>`_. For example:

  .. code-block:: 

    ./mattermost config migrate  path/to/config.json "postgres://mmuser:mostest@dockerhost:5432/mattermost_test?sslmode=disable&connect_timeout=10"

Any existing SAML certificates and private keys will also be migrated to the database.

Addtitionally, to disable automatically watching the default config.json and affecting changes, set the ``--disableconfigwatch`` `flag <https://docs.mattermost.com/administration/command-line-tools.html#mattermost>`_ to true.

With configuration in the database enabled, any changes to the configuration are recorded to the ``Configurations`` and ``ConfigurationFiles`` tables. Furthermore, ``ClusterSettings.ReadOnlyConfig`` is ignored, enabling full use of the System Console.

Note that environment variable overrides remain fully supported using the configuration in the database. They will no longer be written back to the configuration when a change is saved, but will be written to the database instead.


Troubleshooting
-----------------

Server fails to start 
~~~~~~~~~~~~~~~~~~~~~
Providing the --disableconfigwatch flag while not actually pointing at a file will fail to start the server with an appropriate error message.
