Configuration in the Mattermost Database
=========================================
A new configuration option was added in `5.10 <https://docs.mattermost.com/administration/changelog.html#configuration-in-database>`_ to use the database for the single source of truth of the active configuration of your Mattermost installation. This will change the Mattermost binary from reading the default config.json file to reading the configuration settings stored within a configuration table in the database. Mattermost has been running our high availability community server on this option since the feature was released.  

Benefits to using this option include: 

  - Conveniently manage configuration changes directly from the System Console, even in High Availability deployments and read-only containerized environments.
  - Ensure all servers in a High Availability deployment have the same configuration, even when new servers are added to the cluster.
  - Automatically deploy SAML certificates and keys to all servers in the cluster.

To change your server from reading the config.json file to using the configuration in database: 

1. Use the ``--config`` `command <https://docs.mattermost.com/administration/command-line-tools.html#mattermost>`_ to change the binary from reading from the default config.json file and location to the config database store by specifying a supported provider uri. Alternatively, the you may specify the ``MM_CONFIG`` variable to configure the same flag. 
  
  a. The provider uri specifies the driver name and data source name used to resolve the database. For example: ``postgres://mmuser:mostest@dockerhost:5432/mattermost_test?sslmode=disable\u0026connect_timeout=10``
  b. Alternatively, you can  use the ``--migrate config`` `command <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-config-migrate>`_ for installs that are already using the ``config.json`` default file. 
  
2. Set the ``--disableconfigwatch`` `flag <https://docs.mattermost.com/administration/command-line-tools.html#mattermost>`_ to true to disable automatically watching this default config.json and effecting changes.

With configuration in the database enabled, any changes to the configuration will recorded the new, full configuration as a new row in the `Configurations` table. Note that `ClusterSettings.ReadOnlyConfig` is ignored when using configuration in the database, enabling full use of the system console.

Note that environment variable overrides remain fully supported, and will no longer be written back to the configuration when a different change is saved.

.. note::
    If using SAML, ensure the SAML certificates and keys are accessible to also migrate into the database.

Troubleshooting
-----------------

Server fails to start 
~~~~~~~~~~~~~~~~~~~~~
Providing the --disableconfigwatch flag while not actually pointing at a file will fail to start the server with an appropriate error message.
