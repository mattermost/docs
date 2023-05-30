Environment variables
=====================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

You can use environment variables to manage the configuration. Environment variables override settings in ``config.json``. If a change to a setting in ``config.json`` requires a restart for it to take effect, then changes to the corresponding environment variable also require a server restart.

The name of the environment variable for any setting can be derived from the name of that setting in ``config.json``. For example, to derive the name of the Site URL setting:

1. Find the setting in ``config.json``. In this case, *ServiceSettings.SiteURL*.
2. Add ``MM_`` to the beginning and convert all characters to uppercase and replace the ``.`` with ``_``. For example, *MM_SERVICESETTINGS_SITEURL*.
3. The setting becomes ``export MM_SERVICESETTINGS_SITEURL="http://example.com"``.

.. note::

  - If Mattermost is run from an initialization file, environment variables can be set via ``Environment=<>``, or ``EnvironmentFile=<path/to/file>``. In the second case, the file specified contains the list of environment variables to set.
  - From Mattermost v7.5, environment configuration parsing supports JSON for ``MM_PLUGINSETTINGS_PLUGINS`` and ``MM_PLUGINSETTINGS_PLUGINSTATES``. This is especially helpful for Helm configuration files, provided all plugins are configured at the same time. For example, ``MM_PLUGINSETTINGS_PLUGINSTATES="{\"com.mattermost.calls\":{\"Enable\":true},\"com.mattermost.nps\":{\"Enable\":true}}"``.
  - When settings are configured through an environment variable, System Admins can't modify them in the System Console. If a setting is configured through an environment variable, and any other changes are made in the System Console, the value stored of the environment variable will be written back to the ``config.json`` as that setting's value.
  - For any setting that's not set in ``config.json`` or in environment variables, the Mattermost server uses the setting's default value as documented in the sections below on this page.

.. warning::
   
   - Environment variables for Mattermost settings that are set within the active shell will take effect when migrating configuration. For more information, see the `configuration in a database </configure/configuation-in-a-database.html>`__ documentation.
   - Database connection strings for the database read and search replicas need to be formatted using `URL encoding <https://www.w3schools.com/tags/ref_urlencode.asp>`__. Incorrectly formatted strings may cause some characters to terminate the string early, resulting in issues when the connection string is parsed.
   
Override Mattermost license file
--------------------------------

You can use an environment variable to override any license in the database or file configuration without replacing those licenses. When starting the server, specify the license key as ``MM_LICENSE`` with the contents of a license file.

.. note::
   If ``MM_LICENSE`` is set to a non-empty string, but the license specified is not valid, the Mattermost server will be started without a license.
   
   In a High Availability deployment, using an environment variable to override a server license only affects the individual app server and doesn't propagate to other servers in the cluster.

Load custom configuration defaults
----------------------------------

This custom configuration applies only if the values are not already present in the current server configuration.

1. Create a JSON file that contains the custom configuration defaults. For example, ``custom.json``.
2. When starting the server, point the custom defaults environment variable to the defaults file: ``MM_CUSTOM_DEFAULTS_PATH=custom.json``.
