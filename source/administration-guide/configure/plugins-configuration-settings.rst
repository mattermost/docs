Plugins configuration settings
==============================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Review and manage the following plugin configuration options in the System Console by selecting the **Product** |product-list| menu, selecting **System Console**, and then selecting **Plugins**:

- `Plugin management <#plugin-management>`__
- `Calls <#calls>`__
- `AI Agents <#ai-agents>`__
- `GitLab <#gitlab>`__
- `GitHub <#github>`__
- `Jira <#jira>`__
- `Legal Hold <#legal-hold>`__
- `Microsoft Calendar Integration <#microsoft-calendar>`__
- `MS Teams <#ms-teams>`__
- `Performance metrics <#performance-metrics>`__
- `Collaborative playbooks <#collaborative-playbooks>`__
- `User satisfaction surveys <#user-satisfaction-surveys>`__
- `ServiceNow <#servicenow>`__
- `Zoom <#zoom>`__
- `config.json-only settings <#config-json-only-settings>`__

.. tip::

  System admins managing a self-hosted Mattermost deployment can edit the ``config.json`` file as described in the following tables. Each configuration value below includes a JSON path to access the value programmatically in the ``config.json`` file using a JSON-aware tool. For example, the ``Enable`` value is under ``PluginSettings``.

  - If using a tool such as `jq <https://stedolan.github.io/jq/>`__, you'd enter: ``cat config/config.json | jq '.PluginSettings.Enable'``
  - When working with the ``config.json`` file manually, look for an object such as ``PluginSettings``, then within that object, find the key ``Enable``.

----

Plugin management
-----------------

Access the following configuration settings in the System Console by going to **Plugins > Plugin Management**.

.. config:setting:: enable-plugins
  :displayname: Enable plugins (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: .PluginSettings.Enable
  :environment: MM_PLUGINSETTINGS_ENABLE

  - **true**: **(Default)** Enables plugins on your Mattermost server.
  - **false**: Disables plugins on your Mattermost server.

Enable plugins
~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| - **true**: **(Default)** Enables plugins on your Mattermost server. See the `Use plugins with Mattermost <https://developers.mattermost.com/integrate/plugins/using-and-managing-plugins/>`__ documentation for details. | - System Config path: **Plugins > Plugin Management**                 |
| - **false**: Disables plugins on your Mattermost server.                                                                                                                                                                  | - ``config.json`` setting: ``PluginSettings`` > ``Enable`` > ``true`` |
|                                                                                                                                                                                                                           | - Environment variable: ``MM_PLUGINSETTINGS_ENABLE``                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+

.. note::

  Disabling this configuration setting in larger deployments may improve server performance in the following areas:

  - Resource Consumption: Plugins consume system resources such as CPU, memory, and disk. Disabling them frees up these resources, allowing the core Mattermost application to run more efficiently.
  - Reduced Complexity: Each plugin can add additional logic and processing requirements. By reducing the number of active plugins, you lower the complexity and potential points of failure in the system.
  - Faster Load Times: Disabling plugins can lead to faster server startup and lower latency during user interactions, as there are fewer components for the system to initialize and manage.
  - Stability: Some plugins may have bugs or performance issues that can affect the overall performance and stability of the Mattermost instance. Disabling problematic or under-utilized plugins can enhance the stability of the system.
  - Maintenance and Updates: Managing fewer plugins reduces the overhead associated with maintaining and updating them, which can contribute to smoother operation and less downtime
  - However, plugins are often essential for integrating Mattermost with other services and workflows. It's important to balance performance improvements with the needs of your organization and users.


.. config:setting:: require-plugin-signature
  :displayname: Require plugin signature (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: .PluginSettings.RequirePluginSignature
  :environment: MM_PLUGINSETTINGS_REQUIREPLUGINSIGNATURE

  - **true**: **(Default)** Enables plugin signature validation for managed and unmanaged plugins.
  - **false**: Disables plugin signature validation for managed and unmanaged plugins.

Require plugin signature
~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| - **true**: **(Default)** Enables plugin signature validation for managed and unmanaged plugins.                                                                                      | - System Config path: **Plugins > Plugin Management**                                  |
| - **false**: Disables plugin signature validation for managed and unmanaged plugins.                                                                                                  | -  ``config.json`` setting: ``PluginSettings`` > ``RequirePluginSignature`` > ``true`` |
|                                                                                                                                                                                       | - Environment variable: ``MM_PLUGINSETTINGS_REQUIREPLUGINSIGNATURE``                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+

.. note::
  - This setting is applicable to self-hosted deployments only.
  - From Mattermost server v10.11, pre-packaged plugins require signature validation on startup. Distributions that bundle custom pre-packaged plugins must configure custom public keys via ``PluginSettings.SignaturePublicKeyFiles`` to validate their signatures.
  - **Mattermost server v10.10 and earlier**: Pre-packaged plugins are not subject to signature validation.
  - Plugins installed through the Marketplace are always subject to signature validation at the time of download.
  - Enabling this configuration will result in `plugin file uploads <#upload-plugin>`__ being disabled in the System Console.

.. config:setting:: automatic-prepackaged-plugins
  :displayname: Automatic prepackaged plugins (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: .PluginSettings.AutomaticPrepackagedPlugins
  :environment: MM_PLUGINSETTINGS_AUTOMATICPREPACKAGEDPLUGINS

  - **true**: **(Default)** Mattermost automatically installs and upgrades any enabled pre-packaged plugins.
  - **false**: Mattermost does not automatically install or upgrade pre-packaged plugins.

Automatic prepackaged plugins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| - **true**: **(Default)** Mattermost automatically installs and upgrades any enabled pre-packaged plugins. If a newer version is installed, no changes are made.                | - System Config path: **Plugins > Plugin Management**                                      |
| - **false**: Mattermost does not automatically install or upgrade pre-packaged plugins. Pre-packaged plugins may be installed manually from the Marketplace, even when offline. | - ``config.json`` setting: ``PluginSettings`` > ``AutomaticPrepackagedPlugins`` > ``true`` |
|                                                                                                                                                                                 | - Environment variable: ``MM_PLUGINSETTINGS_AUTOMATICPREPACKAGEDPLUGINS``                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+

.. note::
  **Prepackaged Plugin Installation Behavior**: When system administrators drop plugin files (with their ``.sig`` signature files) into the ``prepackaged_plugins`` directory, the plugins won't install automatically. Prepackaging makes the plugin available for "offline" installation. The plugin will automatically install only when a system admin pre-configures the ``config.json`` with that plugin enabled.

.. config:setting:: upload-plugin
  :displayname: Upload Plugin (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: EnableUploads
  :environment: MM_PLUGINSETTINGS_ENABLEUPLOADS

  - **true**: Enables system admins to upload plugins from the local computer to the Mattermost server.
  - **false**: **(Default)** Disables uploading of plugins from the local computer to the Mattermost server.

Upload Plugin
~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| - **true**:  Enables you to upload plugins from the local computer to the Mattermost server.                                       | - System Config path: **Plugins > Plugin Management**                            |
| - **false**: **(Default)** Disables uploading of plugins from the local computer to the Mattermost server.                         | - ``config.json`` setting: ``PluginSettings`` > ``EnableUploads`` > ``false``    |
|                                                                                                                                    | - Environment variable: ``MM_PLUGINSETTINGS_ENABLEUPLOADS``                      |
+------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

.. note::
  - This setting is applicable to self-hosted deployments only.
  - When plugin uploads are enabled, the error ``Received invlaid response from the server`` when uploading a plugin file typically indicates that the
    :ref:`MaxFileSize <administration-guide/configure/environment-configuration-settings:maximum file size>` configuration setting isn't large enough to support the plugin file upload. Additional proxy setting updateds
    may also be required.
  - The ability to upload plugin files is disabled when the `Require plugin signature <#require-plugin-signature>`__ configuration setting is enabled.

.. config:setting:: enable-pluginsmarketplace
  :displayname: Enable marketplace (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: .PluginSettings.EnableMarketplace
  :environment: MM_PLUGINSETTINGS_ENABLEMARKETPLACE

  - **true**: **(Default)** Enables the plugin Marketplace on your Mattermost server for all system admins.
  - **false**: Disables the plugin Marketplace on your Mattermost server for all system admins.

Enable Marketplace
~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| - **true**: **(Default)** Enables the plugin Marketplace on your Mattermost server for all system admins. | - System Config path: **Plugins > Plugin Management**                            |
| - **false**: Disables the plugin Marketplace on your Mattermost server for all system admins.             | - ``config.json`` setting: ``PluginSettings`` > ``EnableMarketplace`` > ``true`` |
|                                                                                                           | - Environment variable: ``MM_PLUGINSETTINGS_ENABLEMARKETPLACE``                  |
+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: enable-pluginsremotemarketplace
  :displayname: Enable remote marketplace (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: .PluginSettings.EnableRemoteMarketplace
  :environment: MM_PLUGINSETTINGS_ENABLEREMOTEMARKETPLACE

  - **true**: **(Default)** Mattermost attempts to connect to the endpoint set in MarketplaceURL.
  - **false**: Mattermost doesn't attempt to connect to a remote Marketplace, and shows only pre-packaged and installed plugins.

Enable remote Marketplace
~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| - **true**: **(Default)** Mattermost attempts to connect to the endpoint set in **Marketplace URL**.                                            | - System Config path: **Plugins > Plugin Management**                                     |
|   If the connection fails, an error is displayed, and the Marketplace only shows pre-packaged and installed plugins.                            | - ``config.json`` setting: ``PluginSettings`` > ``EnableRemoteMarketplace`` > ``true``    |
| - **false**:  Mattermost does not attempt to connect to a remote Marketplace.                                                                   | - Environment variable: ``MM_PLUGINSETTINGS_ENABLEREMOTEMARKETPLACE``                     |
|   The Marketplace shows only pre-packaged and installed plugins. Use this setting if your Mattermost server cannot connect to the Internet.     |                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+

.. note::
  - From Mattermost v9.1, set this configuration setting value to ``true`` to access a configured remote marketplace URL.
  - For Mattermost v9.0, the ``MM_FEATUREFLAGS_STREAMLINEDMARKETPLACE`` feature flag must be set to ``false``, and this configuration setting must be set to ``true`` to access a configured remote marketplace URL.
  - Each Mattermost host must have network access to the endpoint set in MarketplaceURL.

.. config:setting:: marketplace-url
  :displayname: Marketplace URL (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: .PluginSettings.MarketplaceURL
  :environment: MM_PLUGINSETTINGS_MARKETPLACEURL
  :description: This setting stores the URL for the remote Marketplace. Default is **https://api.integrations.mattermost.com**.

Marketplace URL
~~~~~~~~~~~~~~~

+----------------------------------------------------------------------+--------------------------------------------------------------------+
| This setting stores the URL for the remote Markeplace.               | - System Config path: **Plugins > Plugin Management**              |
|                                                                      | - ``config.json`` setting: ``PluginSettings`` > ``MarketplaceURL`` |
|                                                                      | - Environment variable: ``MM_PLUGINSETTINGS_MARKETPLACEURL``       |
| String input. Default is **https://api.integrations.mattermost.com** |                                                                    |
+----------------------------------------------------------------------+--------------------------------------------------------------------+

.. config:setting:: installed-plugin-state
  :displayname: Installed plugin state (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: .PluginSettings.PluginStates
  :environment: MM_PLUGINSETTINGS_PLUGINSTATES
  :description: This setting is a list of installed plugins and their status as enabled or disabled.

Installed plugin state
~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| This setting is a list of installed plugins and their status as enabled or disabled.                                                                                                                         | - System Config path: **Plugins > Plugin Management**            |
|                                                                                                                                                                                                              | - ``config.json`` setting: ``PluginSettings`` > ``PluginStates`` |
|                                                                                                                                                                                                              | - Environment variable: ``MM_PLUGINSETTINGS_PLUGINSTATES``       |
| The ``config.json`` setting is an object. The object keys are plugin IDs, e.g. ``com.mattermost.apps``. Each key maps to an object that contains an ``Enable`` key that can be set as ``true`` or ``false``. |                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+

.. config:setting:: plugin-settings
  :displayname: Plugin settings (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: .PluginSettings.Plugins
  :environment: MM_PLUGINSETTINGS_PLUGINS
  :description: This setting contains plugin-specific data.

Plugin settings
~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+
| This setting contains plugin-specific data.                                                                                                                            | - System Config path: **Plugins > Plugin Management**       |
|                                                                                                                                                                        | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` |
|                                                                                                                                                                        | - Environment variable: ``MM_PLUGINSETTINGS_PLUGINS``       |
| The ``config.json`` setting is an object. The object keys are plugin IDs, e.g. ``com.mattermost.apps``. Each key maps to an object that contains plugin-specific data. |                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+

----

Calls
-----

Access the following configuration settings in the System Console by going to **Plugins > Calls**.

.. config:setting:: enable-plugin
  :displayname: Enable plugin (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.PluginStates.com.mattermost.calls.Enable
  :environment: MM_PLUGINSETTINGS_PLUGINSTATES_COM_MATTERMOST_CALLS

  - **true**: **(Default)** Enables the calls plugin on your Mattermost workspace.
  - **false**: Disables the calls plugin on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| - **true**: (Default) Enables the Calls plugin on your Mattermost workspace.   | - System Config path: **Plugins > Calls**                                                                |
| - **false**: Disables the Calls plugin on your Mattermost workspace.           | - ``config.json`` setting: ``PluginSettings`` > ``PluginStates`` > ``com.mattermost.calls`` > ``Enable`` |
|                                                                                | - Environment variable: ``MM_PLUGINSETTINGS_PLUGINSTATES_COM_MATTERMOST_CALLS``                          |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

.. config:setting:: rtc-server-address-udp
  :displayname: RTC server port (UDP) (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.udpserveraddress
  :environment: MM_CALLS_UDP_SERVER_ADDRESS
  :description: The IP address used by the RTC server to listen for UDP connections. By default the service listens on all the available interfaces.

RTC server address (UDP)
~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| This setting controls the IP address the RTC server listens for UDP connections. All calls UDP traffic will be served through this IP.     | - System Config path: **Plugins > Calls**                                                                                 |
|                                                                                                                                            | - ``config.json`` setting: ``PluginSettings`` ``Plugins`` > ``com.mattermost.calls`` > ``udpserveraddress``               |
| Changing this setting requires a plugin restart to take effect.                                                                            | - Environment variable: ``MM_CALLS_UDP_SERVER_ADDRESS``                                                                   |
| If left unset (default value) the service will listen on all the available interfaces.                                                     |                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

.. note::
  This setting is applicable to self-hosted deployments only, and only when not running calls through the standalone ``rtcd`` service.

.. config:setting:: rtc-server-address-tcp
  :displayname: RTC server port (TCP) (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.tcpserveraddress
  :environment: MM_CALLS_TCP_SERVER_ADDRESS
  :description: The IP address used by the RTC server to listen for TCP connections. By default the service listens on all the available interfaces.

RTC server address (TCP)
~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| This setting controls the IP address the RTC server listens for TCP connections. All calls TCP traffic will be served through this IP.     | - System Config path: **Plugins > Calls**                                                                                   |
|                                                                                                                                            | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``tcpserveraddress``               |
| Changing this setting requires a plugin restart to take effect.                                                                            | - Environment variable: ``MM_CALLS_TCP_SERVER_ADDRESS``                                                                     |
| If left unset (default value) the service will listen on all the available interfaces.                                                     |                                                                                                                             |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+

.. note::
  This setting is available starting in plugin version 0.17, and is only applicable for self-hosted deployments when not running calls through the standalone ``rtcd`` service.

.. config:setting:: rtc-server-port-udp
  :displayname: RTC server port (UDP) (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.udpserverport
  :environment: MM_CALLS_UDP_SERVER_PORT
  :description: The UDP port the RTC server will listen on. All calls UDP traffic will be served through this port. Default port is **8443**.

RTC server port (UDP)
~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| This setting controls the UDP port listened on by the RTC server. All calls UDP traffic will be served through this port.     | - System Config path: **Plugins > Calls**                                                                                |
|                                                                                                                               | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``udpserverport``               |
|                                                                                                                               | - Environment variable: ``MM_CALLS_UDP_SERVER_PORT``                                                                     |
| Changing this setting requires a plugin restart to take effect.                                                               |                                                                                                                          |
|                                                                                                                               |                                                                                                                          |
| Default is **8443**.                                                                                                          |                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+

.. note::
  This setting is only applicable for self-hosted deployments when not running calls through the standalone ``rtcd`` service.

.. config:setting:: rtc-server-port-tcp
  :displayname: RTC server port (TCP) (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.tcpserverport
  :environment: MM_CALLS_TCP_SERVER_PORT
  :description: The TCP port the RTC server will listen on. All calls TCP traffic will be served through this port. Default port is **8443**.

RTC server port (TCP)
~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| This setting controls the TCP port listened on by the RTC server. All calls TCP traffic will be served through this port.     | - System Config path: **Plugins > Calls**                                                                   |
|                                                                                                                               | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``tcpserverport``  |
|                                                                                                                               | - Environment variable: ``MM_CALLS_TCP_SERVER_PORT``                                                        |
| Changing this setting requires a plugin restart to take effect.                                                               |                                                                                                             |
|                                                                                                                               |                                                                                                             |
| Default is **8443**.                                                                                                          |                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+

.. note::
  This setting is available starting in plugin version 0.17, and is only applicable for self-hosted deplyoments when not running calls through the standalone ``rtcd`` service.

.. config:setting:: enable-pluginsonspecificchannels
  :displayname: Enable on specific channels (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.allowenablecalls
  :environment: MM_CALLS_ALLOW_ENABLE_CALLS
  :description: Manage who can enable or disable calls on specific channels (deprecated from Mattermost v7.7)

Enable on specific channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Admins can't configure this setting from Mattermost v7.7; it's hidden and always enabled for self-hosted deployments*

+----------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| - **true**: Channel admins can enable or disable calls on specific channels. Participants in DMs/GMs can also enable or disable calls. | - System Config path: **Plugins > Calls**                                                                       |
| - **false**: Only system admins can enable or disable calls on specific channels.                                                      | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``allowenablecalls``   |
|                                                                                                                                        | - Environment variable: ``MM_CALLS_ALLOW_ENABLE_CALLS``                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+

.. config:setting:: test-mode
  :displayname: Test mode (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.defaultenabled
  :environment: MM_CALLS_DEFAULT_ENABLED
  :description: A setting to allow system admins to test calls before making them available across the deployment. This setting was called **Enable on all channels** up until Mattermost v7.7.

Test mode
~~~~~~~~~

*This setting was called Enable on all channels until Mattermost v7.7. It was renamed to defaultenabled in code and Test Mode in-product and is only applicable to self-hosted deployments.*

+-----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| - **false**: Test mode is enabled and only system admins can start calls in channels.                           | - System Config path: **Plugins > Calls**                                                                     |
| - **true**: Live mode is enabled and all team members can start calls in channels.                              | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``defaultenabled``   |
|                                                                                                                 | - Environment variable: ``MM_CALLS_DEFAULT_ENABLED``                                                          |
+-----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+

.. note::
  Use this setting as a system admin to confirm calls work as expected. When **false**, users attempting to start calls are prompted to contact a system admin, and system admins are prompted to confirm that calls are working as expected before switching to live mode.

.. config:setting:: ice-host-override
  :displayname: ICE host override (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.icehostoverride
  :environment: MM_CALLS_ICE_HOST_OVERRIDE
  :description: An optional override to the host that gets advertised to clients when connecting to calls. When empty or unset, the RTC service will attempt to automatically find the instance's public IP through STUN.

ICE host override
~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| This setting can be used to override the host addresses that get advertised to clients when connecting to calls. The accepted formats are the following:         | - System Config path: **Plugins > Calls**                                                                      |
|                                                                                                                                                                  | - ``config.json`` setting:  ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``icehostoverride``  |
|                                                                                                                                                                  | - Environment variable: ``MM_CALLS_ICE_HOST_OVERRIDE``                                                         |
|                                                                                                                                                                  |                                                                                                                |
| - A single IP address (e.g. ``10.0.0.1``).                                                                                                                       |                                                                                                                |
| - A single hostname or FQDN (e.g. ``calls.myserver.tld``).                                                                                                       |                                                                                                                |
| - (starting in v0.17.0) A comma separated list of externalAddr/internalAddr mappings (e.g. ``10.0.0.1/172.0.0.1,10.0.0.2/172.0.0.2``).                           |                                                                                                                |
|                                                                                                                                                                  |                                                                                                                |
| This is an optional field. Changing this setting requires a plugin restart to take effect.                                                                       |                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+

.. note::
  - This setting is only applicable for self-hosted deployments when not running calls through the standalone ``rtcd`` service.
  - Depending on the network infrastructure (e.g. instance behind a NAT device) it may be necessary to set this field to the client facing external IP for clients to connect. When empty or unset, the RTC service will attempt to find the instance's public IP through STUN.
  - A hostname (e.g. domain name) can be specified in this setting, but an IP address will be passed to clients. This means that a DNS resolution happens on the Mattermost instance which could result in a different IP address from the one the clients would see, causing connectivity to fail. When in doubt, we recommend using an IP address directly or confirming that the resolution on the host side reflects the one on the client.

.. |ice_host_override_link| replace:: :ref:`ICE Host Override <administration-guide/configure/plugins-configuration-settings:ice host override>`

.. config:setting:: ice-host-overrideportoverride
  :displayname: ICE host port override (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.icehostportoverride
  :environment: MM_CALLS_ICE_HOST_PORT_OVERRIDE
  :description: An optional port number to be used as an override for host candidates in place of the one used to listen on.

ICE host port override
~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| This setting can be used to override the port used in the ICE host candidates that get advertised to clients when connecting to calls.                              | - System Config path: **Plugins > Calls**                                                                                |
|                                                                                                                                                                     | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``icehostportoverride``         |
|                                                                                                                                                                     | - Environment variable: ``MM_CALLS_ICE_HOST_PORT_OVERRIDE``                                                              |
|                                                                                                                                                                     |                                                                                                                          |
| This can be useful in case there are additional network components (e.g. NLBs) in front of the RTC server that may route the calls traffic through a different port.|                                                                                                                          |
| Changing this setting requires a plugin restart to take effect.                                                                                                     |                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+

.. note::
  - This setting is applicable only to self-hosted deployments.
  - This value will apply to both UDP and TCP host candidates.

.. config:setting:: rtcd-service-url
  :displayname: RTCD service URL (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.rtcdserviceurl
  :environment: MM_CALLS_RTCD_SERVICE_URL
  :description: The URL to a running rtcd service instance that will host the calls. When set (non empty) all the calls will be handled by this external service.

RTCD service URL
~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| The URL to a running `rtcd <https://github.com/mattermost/rtcd>`__ service instance that will host the calls. | - System Config path: **Plugins > Calls**                                                                                                                 |
|                                                                                                               | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``rtcdserviceurl``                                               |
|                                                                                                               | - Environment variable: ``MM_CALLS_RTCD_SERVICE_URL``                                                                                                     |
|                                                                                                               |                                                                                                                                                           |
| When set (non empty) all the calls will be handled by this external service.                                  |                                                                                                                                                           |
|                                                                                                               |                                                                                                                                                           |
| This is an optional field. Changing this setting requires a plugin restart to take effect.                    |                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::
  - This setting is applicable only to self-hosted deployments.
  - The environment variable ``MM_CALLS_RTCD_URL`` is deprecated in favor of ``MM_CALLS_RTCD_SERVICE_URL``.
  - The client will self-register the first time it connects to the service and store the authentication key in the database. If no client ID is explicitly provided, the diagnostic ID of the Mattermost installation will be used.
  - The service URL supports credentials in the form ``http://clientID:authKey@hostname``. Alternatively these can be passed through environment overrides to the Mattermost server, namely ``MM_CALLS_RTCD_CLIENT_ID`` and ``MM_CALLS_RTCD_AUTH_KEY``
  - The client will self-register the first time it connects to the service and store the authentication key in the database. If no client ID is explicitly provided, the diagnostic ID of the Mattermost installation will be used.
  - The service URL supports credentials in the form ``http://clientID:authKey@hostname``. Alternatively these can be passed through environment overrides to the Mattermost server, namely ``MM_CALLS_RTCD_CLIENT_ID`` and ``MM_CALLS_RTCD_AUTH_KEY``

.. config:setting:: max-call-participants
  :displayname: Max call participants (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.maxcallparticipants
  :environment: MM_CALLS_MAX_CALL_PARTICIPANTS
  :description: The maximum number of participants that can join a single call. Default value is **0** (unlimited). The maximum recommended setting is 50.

Max call participants
~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| This setting limits the number of participants that can join a single call. | - System Config path: **Plugins > Calls**                                                                       |
|                                                                             | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``maxcallparticipants``|
|                                                                             | - Environment variable: ``MM_CALLS_MAX_CALL_PARTICIPANTS``                                                      |
|                                                                             |                                                                                                                 |
| Default is **0** (no limit).                                                |                                                                                                                 |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+

.. note::
  - This setting is applicable only to self-hosted deployments.
  - The environment variable ``MM_CALLS_MAX_PARTICIPANTS`` is deprecated in favor of ``MM_CALLS_MAX_CALL_PARTICIPANTS``.
  - This setting is optional, but the recommended maximum number of participants is **50**. Call participant limits greatly depends on instance resources. See the :doc:`Calls self-hosted deployment </administration-guide/configure/calls-deployment>` documentation for details.


.. config:setting:: ice-servers-configurations
  :displayname: ICE server configurations (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.iceserversconfigs
  :environment: MM_CALLS_ICE_SERVERS_CONFIGS
  :description: A list of ICE servers (STUN/TURN) to be used by the service. Value should be valid JSON. Default value is **[{"urls": ["stun:stun.global.calls.mattermost.com:3478"]}]**.

ICE servers configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| This setting stores a list of ICE servers (STUN/TURN) in JSON format to be used by the service.                                                                                                                           | - System Config path: **Plugins > Calls**                                                                          |
|                                                                                                                                                                                                                           | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``iceserversconfigs``     |
|                                                                                                                                                                                                                           | - Environment variable: ``MM_CALLS_ICE_SERVERS_CONFIGS``                                                           |
|                                                                                                                                                                                                                           |                                                                                                                    |
| This is an optional field. Changing this setting may require a plugin restart to take effect.                                                                                                                             |                                                                                                                    |
|                                                                                                                                                                                                                           |                                                                                                                    |
| Default is ``[{"urls": ["stun:stun.global.calls.mattermost.com:3478"]}]``                                                                                                                                                 |                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

.. note::
  - This setting is applicable only to self-hosted deployments.
  - The configurations above, containing STUN and TURN servers, are sent to the clients and used to generate local candidates.
  - If hosting calls through the plugin (i.e. not using the |rtcd_service|) any configured STUN server may also be used to find the instance's public IP when none is provided through the |ice_host_override_link| option.

.. |rtcd_service| replace:: :ref:`rtcd service <administration-guide/configure/calls-deployment:the rtcd service>`

**Example**

 .. code-block:: json

   [
    {
       "urls":[
          "stun:stun.global.calls.mattermost.com:3478"
       ]
    },
    {
       "urls":[
          "turn:turn.example.com:3478"
       ],
       "username":"webrtc",
       "credentials":"turnpassword"
    }
   ]

**Example (Using generated TURN credentials)**

  .. code-block:: json

    [{
	    "urls": ["turn:turn.example.com:443"]
    }]

.. note::
  To get TURN generated credentials to work you must provide a secret through the *TURN static auth secret* setting below.

.. config:setting:: turn-static-auth-secret
  :displayname: TURN static auth secret (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.turnstaticauthsecret
  :environment: MM_CALLS_TURN_STATIC_AUTH_SECRET
  :description: A static secret used to generate short-lived credentials for TURN servers.

TURN static auth secret
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| A static secret used to generate short-lived credentials for TURN servers. | - System Config path: **Plugins > Calls**                                                                                        |
|                                                                            | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``turnstaticauthsecret``                |
|                                                                            | - Environment variable: ``MM_CALLS_TURN_STATIC_AUTH_SECRET``                                                                     |
| This is an optional field.                                                 |                                                                                                                                  |
+----------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

.. note::

  This setting is applicable only to self-hosted deployments.

.. config:setting:: turn-credentials-expiration
  :displayname: TURN credentials expiration (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.turncredentialsexpirationminutes
  :environment: MM_CALLS_TURN_CREDENTIALS_EXPIRATION_MINUTES
  :description: The expiration, in minutes, of the short-lived credentials generated for TURN servers.

TURN credentials expiration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| The expiration, in minutes, of the short-lived credentials generated for TURN servers. | - System Config path: **Plugins > Calls**                                                                                                    |
|                                                                                        | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``turncredentialsexpirationminutes``                |
|                                                                                        | - Environment variable: ``MM_CALLS_TURN_CREDENTIALS_EXPIRATION_MINUTES``                                                                     |
|                                                                                        |                                                                                                                                              |
| Default is **1440** (one day).                                                         |                                                                                                                                              |
+----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

  This setting is applicable only to self-hosted deployments.

.. config:setting:: server-side-turn
  :displayname: Server side TURN (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.serversideturn
  :environment: MM_CALLS_SERVER_SIDE_TURN

  - **true**: The RTC server will use the configured TURN candidates for server-initiated connections.
  - **false**: TURN will be used only on the client-side.

Server side TURN
~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| - **true**: The RTC server will use the configured TURN candidates for server-initiated connections. | - System Config path: **Plugins > Calls**                                                                                  |
| - **false**: TURN will be used only on the client-side.                                              | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``serversideturn``                |
|                                                                                                      | - Environment variable: ``MM_CALLS_SERVER_SIDE_TURN``                                                                      |
|                                                                                                      |                                                                                                                            |
| Changing this setting requires a plugin restart to take effect.                                      |                                                                                                                            |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+

.. note::

  This setting is applicable only to self-hosted deployments.

.. config:setting:: allow-screen-sharing
  :displayname: Allow screen sharing (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.allowscreensharing
  :environment: MM_CALLS_ALLOW_SCREEN_SHARING

  - **true**: Call participants will be allowed to share their screen.
  - **false**: Call participants won't be allowed to share their screen.

Allow screen sharing
~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| - **true**: Call participants will be allowed to share their screen.   | - System Config path: **Plugins > Calls**                                                                                      |
| - **false**: Call participants won't be allowed to share their screen. | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``allowscreensharing``                |
|                                                                        | - Environment variable: ``MM_CALLS_ALLOW_SCREEN_SHARING``                                                                      |
| Changing this setting requires a plugin restart to take effect.        |                                                                                                                                |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+

.. note::

  This setting is applicable only to self-hosted deployments.

.. config:setting:: enable-pluginsimulcast
  :displayname: (Experimental) Enable simulcast for screen sharing (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enablesimulcast
  :environment: MM_CALLS_ENABLE_SIMULCAST
  
  - **true**: Enables simulcast for screen sharing. This can help to improve screen sharing quality.
  - **false**: (Default) Disables simulcast for screen sharing.

Enable simulcast for screen sharing (Experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| - **true**: Enables simulcast for screen sharing. This can help to improve screen sharing quality.                     | - System Config path: **Plugins > Calls**                                                                                  |
| - **false**: Disables simulcast for screen sharing.                                                                    | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``enablesimulcast``               |
|                                                                                                                        | - Environment variable: ``MM_CALLS_ENABLE_SIMULCAST``                                                                      |
+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+

.. note::

  - This experimental setting is applicable only to self-hosted deployments.
  - This functionality requires Calls plugin version >= v0.16.0 and ``rtcd`` version >= v0.10.0 (when in use).
  - Avoid enabling both this experimental configuration setting and the `Enable AV1 <#enable-av1-experimental>`__ experimental configuration setting at the same time. 

.. config:setting:: enable-pluginscallrecordings
  :displayname: Enable call recordings (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enablerecordings
  :environment: MM_CALLS_ENABLE_RECORDINGS

  - **true**: Allows call hosts to record meeting video and audio.
  - **false**: (Default) Call recording functionality is not available to hosts.

Enable call recordings
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| - **true**: Allows call hosts to record meeting video and audio.                                                                                      | - System Config path: **Plugins > Calls**                                                                                    |
| - **false**: **(Default)** Call recording functionality is not available to hosts.                                                                    | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``enablerecordings``                |
|                                                                                                                                                       | - Environment variable: ``MM_CALLS_ENABLE_RECORDINGS``                                                                       |
| Recordings include the entire call window view along with participants' audio track and any shared screen video. Recordings are stored in Mattermost. |                                                                                                                              |
|                                                                                                                                                       |                                                                                                                              |
| Changing this setting requires a plugin restart to take effect.                                                                                       |                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+

.. note::

  This setting is applicable only to self-hosted deployments.

.. config:setting:: job-service-url
  :displayname: Job service URL (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.jobserviceurl
  :environment: MM_CALLS_JOB_SERVICE_URL
  :description: The URL to a running job service where all the processing related to recordings happens. This is a required field. Changing this setting requires a plugin restart to take effect.
  
Job service URL
~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| The URL to a running job service where all the processing related to recordings happens. The recorded files produced are stored in Mattermost. | - System Config path: **Plugins > Calls**                                                                              |
|                                                                                                                                                | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``jobserviceurl``             |
| This is a required field. Changing this setting requires a plugin restart to take effect.                                                      | - Environment variable: ``MM_CALLS_JOB_SERVICE_URL``                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+

.. note::

  - This setting is applicable only to self-hosted deployments.
  - The client will self-register the first time it connects to the service and store the authentication key in the database. If no client ID is explicitly provided, the diagnostic ID of the Mattermost installation will be used.
  - The service URL supports credentials in the form ``http://clientID:authKey@hostname``. Alternatively these can be passed through environment overrides to the Mattermost server, namely ``MM_CALLS_JOB_SERVICE_CLIENT_ID``
    and ``MM_CALLS_JOB_SERVICE_AUTH_KEY``.
  - As of Calls v0.25 it's possible to override the site URL used by jobs to connect by setting the ``MM_CALLS_RECORDER_SITE_URL`` or ``MM_CALLS_TRANSCRIBER_SITE_URL`` environment variables respectively. This can be helpful to avoid the jobs
    from connecting through the public Site URL configured in Mattermost and thus potentially bypass the public network.

.. config:setting:: maximum-call-recording-duration
  :displayname: Maximum call recording duration (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.maxrecordingduration
  :environment: MM_CALLS_MAX_RECORDING_DURATION
  :description: The maximum duration of a call recording in minutes.
  
Maximum call recording duration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| The maximum duration of a call recording in minutes.                                                                        | - System Config path: **Plugins > Calls**                                                                        |
|                                                                                                                             | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``maxrecordingduration``|
|                                                                                                                             | - Environment variable: ``MM_CALLS_MAX_RECORDING_DURATION``                                                      |
| The default is **60**. The maximum is **180**. This is a required value.                                                    |                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+

.. note::

  This setting is applicable only to self-hosted deployments.

.. config:setting:: call-recording-quality
  :displayname: Call recording quality (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.recordingquality
  :environment: MM_CALLS_RECORDING_QUALITY
  :description: The audio and video quality of call recordings.

Call recording quality
~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| The audio and video quality of call recordings. Available options are: *Low*, *Medium* and *High*.                          | - System Config path: **Plugins > Calls**                                                                                                                      |
|                                                                                                                             | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``recordingquality``                                                  |
|                                                                                                                             | - Environment variable: ``MM_CALLS_RECORDING_QUALITY``                                                                                                         |
| The default is **Medium**. This is a required value.                                                                        |                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::
  - This setting is applicable only to self-hosted deployments.
  - The quality setting will affect the performance of the job service and the file size of recordings. Refer to the :ref:`deployment section <administration-guide/configure/calls-deployment:configure recording, transcriptions, and live captions>` for more information.

.. config:setting:: enable-pluginscalltranscriptions
  :displayname: Enable call transcriptions (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enabletranscriptions
  :environment: MM_CALLS_ENABLE_TRANSCRIPTIONS
  
  - **true**: Enables automatic transcriptions of calls.
  - **false**: (Default) Call transcriptions functionality is disabled.

Enable call transcriptions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| - **true**: Enables automatic transcriptions of calls.                                                                                                                                                                                                             | - System Config path: **Plugins > Calls**                                                                                    |
| - **false**: **(Default)** Call transcriptions functionality is disabled.                                                                                                                                                                                          | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``enabletranscriptions``            |
|                                                                                                                                                                                                                                                                    | - Environment variable: ``MM_CALLS_ENABLE_TRANSCRIPTIONS``                                                                   |
| Transcriptions are generated from the call participants' audio tracks and the resulting files are attached to the call thread when the recording ends. Captions will be optionally rendered on top of the recording file video player.                             |                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+

.. note::
  - This setting is applicable only to self-hosted deployments.
  - The ability to enable call transcriptions in Mattermost calls is currently in :ref:`Beta <administration-guide/manage/feature-labels:beta>`. 
  - This server-side configuration setting is available from plugin version 0.22. 
  - Call transcriptions require :ref:`call recordings <administration-guide/configure/plugins-configuration-settings:enable call recordings>` to be enabled. 

.. config:setting:: transcriber-model-size
  :displayname: Call transcriber model size (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.transcribermodelsize
  :environment: MM_CALLS_TRANSCRIBER_MODEL_SIZE
  :description: The speech-to-text model size to use. Heavier models will produce more accurate results at the expense of processing time and resources usage.

Transcriber model size
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| The speech-to-text model size to use. Heavier models will produce more accurate results at the expense of processing time and resources usage. Available options are: *Tiny*, *Base* and *Small*.                                                                                  | - System Config path: **Plugins > Calls**                                                                             |
|                                                                                                                                                                                                                                                                                    | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``transcribermodelsize``     |
|                                                                                                                                                                                                                                                                                    | - Environment variable: ``MM_CALLS_TRANSCRIBER_MODEL_SIZE``                                                           |
| The default is **Base**. This is a required value.                                                                                                                                                                                                                                 |                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+

.. note::
  - This setting is applicable only to self-hosted deployments.
  - This setting is available starting in plugin version 0.22. The model size setting will affect the performance of the job service. Refer to the :ref:`configure call recordings, transcriptions, and live captions <administration-guide/configure/calls-deployment:configure recording, transcriptions, and live captions>` documentation for more information.

.. config:setting:: call-transcriber-threads
  :displayname: Call transcriber threads (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.transcribernumthreads
  :environment: MM_CALLS_TRANSCRIBER_NUM_THREADS
  :description: The number of threads used by the post-call transcriber. Default is 2. This is a required value that must be in the range [1, numCPUs].

Call transcriber threads
~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| The number of threads used by the post-call transcriber. This must be in the range [1, numCPUs].                                                                                                                                                                                                                                     | - System Config path: **Plugins > Calls**                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                      | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``transcribernumthread``                                              |
|                                                                                                                                                                                                                                                                                                                                      | - Environment variable: ``MM_CALLS_TRANSCRIBER_NUM_THREADS``                                                                                                   |
| The default is 2. This is a required value.                                                                                                                                                                                                                                                                                          |                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::
  - This setting is applicable only to self-hosted deployments.
  - The call transcriber threads setting will affect the performance of the job service. Refer to the :ref:`configure call recordings, transcriptions, and live captions <administration-guide/configure/calls-deployment:configure recording, transcriptions, and live captions>` documentation for more information. This setting is available starting in plugin version 0.26.2.

.. config:setting:: enable-pluginslivecaptions
  :displayname: (Experimental) Enable live captions (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enablelivecaptions
  :environment: MM_CALLS_ENABLE_LIVE_CAPTIONS
  :description: Enables live captioning of calls.

  - **true**: Enables live captioning of calls.
  - **false**: **(Default)** Live captions functionality is disabled.

Enable live captions
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| - **true**: Enables live captioning of calls.                             | - System Config path: **Plugins > Calls**                                                                        |
| - **false**: **(Default)** Live captions functionality is disabled.       | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``enablelivecaptions``  |
|                                                                           | - Environment variable: ``MM_CALLS_ENABLE_LIVE_CAPTIONS``                                                        |
| Live captions are generated from the call participants' audio tracks      |                                                                                                                  |
| and the resulting captions can be optionally displayed on the call        |                                                                                                                  |
| clients by selecting the **[cc]** option.                                 |                                                                                                                  |
+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+

.. note::
  - The ability to enable live call captions in Mattermost calls is currently in :ref:`Beta <administration-guide/manage/feature-labels:beta>`. 
  - This server-side configuration setting is available starting in plugin version 0.26.2. 
  - Live captions require :ref:`call recordings <administration-guide/configure/plugins-configuration-settings:enable call recordings>` and :ref:`call transcriptions <administration-guide/configure/plugins-configuration-settings:enable call transcriptions>` to be enabled.

.. config:setting:: live-captions-model-size
  :displayname: Live captions: Model size (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.livecaptionsmodelsize
  :environment: MM_CALLS_LIVE_CAPTIONS_MODEL_SIZE
  :description: The speech-to-text model size to use for live captions. Heavier models will produce more accurate results at the expense of processing time and resources usage. Default is **Tiny**. This is a required value. 

Live captions: Model size
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| The speech-to-text model size to use for live captions. While heavier models can produce more accurate results, live captioning requires the transcriber to process up to ten seconds of audio within two seconds. Therefore a maximum of size `base` is recommended. Available options are: *Tiny*, *Base* and *Small*. | - System Config path: **Plugins > Calls**                                                                           |
|                                                                                                                                                                                                                                                                                                                          | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``livecaptionsmodelsize``  |
|                                                                                                                                                                                                                                                                                                                          | - Environment variable: ``MM_CALLS_LIVE_CAPTIONS_MODEL_SIZE``                                                       |
| The default is **Tiny**. This is a required value.                                                                                                                                                                                                                                                                       |                                                                                                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. note::
  - This setting is applicable only to self-hosted deployments.
  - This setting is available starting in plugin version 0.26.2. The model size setting will affect the performance of the job service. Refer to the `performance and scalability recommendations <https://github.com/mattermost/calls-offloader/blob/master/docs/performance.md>`_ documentation for more information.

.. config:setting:: live-captions-number-of-transcribers-used-per-call
  :displayname: Live captions: Number of transcribers used per call (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.livecaptionsnumtranscribers
  :environment: MM_CALLS_LIVE_CAPTIONS_NUM_TRANSCRIBERS
  :description: The number of separate live captions transcribers for each call. Each transcribes one audio stream at a time. Default is 1. This is a required value. The product of LiveCaptionsNumTranscribers * LiveCaptionsNumThreadsPerTranscriber must be in the range [1, numCPUs].

Live captions: Number of transcribers used per call
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| The number of separate live captions transcribers for each call. Each transcribes one audio stream at a time. The product of LiveCaptionsNumTranscribers * LiveCaptionsNumThreadsPerTranscriber must be in the range [1, numCPUs].                                                                                       | - System Config path: **Plugins > Calls**                                                                                |
|                                                                                                                                                                                                                                                                                                                          | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``livecaptionsnumtranscribers`` |
|                                                                                                                                                                                                                                                                                                                          | - Environment variable: ``MM_CALLS_LIVE_CAPTIONS_NUM_TRANSCRIBERS``                                                      |
| The default is 1. This is a required value.                                                                                                                                                                                                                                                                              |                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+

.. note::
  - This setting is applicable only to self-hosted deployments.
  - This setting is available starting in plugin version 0.26.2. The live captions number of transcribers setting will affect the performance of the job service. Refer to the `performance and scalability recommendations <https://github.com/mattermost/calls-offloader/blob/master/docs/performance.md>`_ documentation for more information.

.. config:setting:: live-captions-number-of-threads-per-transcriber
  :displayname: Live captions: Number of threads per transcriber (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.livecaptionsnumthreadspertranscriber
  :environment: MM_CALLS_LIVE_CAPTIONS_NUM_THREADS_PER_TRANSCRIBER
  :description: The number of threads per live captions transcriber. Default is 2. This is a required value. The product of LiveCaptionsNumTranscribers * LiveCaptionsNumThreadsPerTranscriber must be in the range [1, numCPUs].

Live captions: Number of threads per transcriber
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| The number of threads per live-captions transcriber. The product of ``LiveCaptionsNumTranscribers`` * ``LiveCaptionsNumThreadsPerTranscriber`` must be in the range [1, numCPUs].                                                                                                                                        | - System Config path: **Plugins > Calls**                                                                                         |
|                                                                                                                                                                                                                                                                                                                          | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``livecaptionsnumthreadspertranscriber`` |
|                                                                                                                                                                                                                                                                                                                          | - Environment variable: ``MM_CALLS_LIVE_CAPTIONS_NUM_THREADS_PER_TRANSCRIBER``                                                    |
| The default is 2. This is a required value.                                                                                                                                                                                                                                                                              |                                                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

.. note::
  - This setting is applicable only to self-hosted deployments.
  - This setting is available starting in plugin version 0.26.2. The live captions number of threads per transcriber setting will affect the performance of the job service. Refer to the `performance and scalability recommendations <https://github.com/mattermost/calls-offloader/blob/master/docs/performance.md>`_ documentation for more information

.. config:setting:: live-captions-language
  :displayname: Live captions language (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.livecaptionslanguage
  :environment: MM_CALLS_LIVE_CAPTIONS_LANGUAGE
  :description: The language passed to the live captions transcriber. Should be a 2-letter ISO 639 Set 1 language code, e.g. 'en'. If blank, the lange will be set to 'en' (English) as default. 

Live captions language
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| The language passed to the live captions transcriber. Should be a 2-letter ISO 639 Set 1 language code, e.g. 'en'.  | - System Config path: **Plugins > Calls**                                                                        |
|                                                                                                                     | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``livecaptionslanguage``|
|                                                                                                                     | - Environment variable: ``MM_CALLS_LIVE_CAPTIONS_LANGUAGE``                                                      |
| If blank, the lange will be set to 'en' (English) as default.                                                       |                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+

.. note::
  This setting is applicable only to self-hosted deployments.

.. config:setting:: enable-pluginipv6
  :displayname: (Experimental) Enable IPv6 (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enableipv6
  :environment: MM_CALLS_ENABLE_IPV6

  - **true**: The RTC service will work in dual-stack mode, listening for IPv6 connections and generating candidates in addition to IPv4 ones.
  - **false**: (False) The RTC service will only listen for IPv4 connections.

(Experimental) Enable IPv6
~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| - **true**: The RTC service will work in dual-stack mode, listening for IPv6 connections and generating candidates in addition to IPv4 ones. | - System Config path: **Plugins > Calls**                                                                |
| - **false**: **(Default)** The RTC service will only listen for IPv4 connections.                                                            | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``enableipv6``  |
|                                                                                                                                              | - Environment variable: ``MM_CALLS_ENABLE_IPV6``                                                         |
| Changing this setting requires a plugin restart to take effect.                                                                              |                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

.. note::
  - This setting is applicable only to self-hosted deployments.
  - This setting is available starting in plugin version 0.17, and is only applicable when not running calls through the standalone ``rtcd`` service.

.. config:setting:: enable-pluginscallringing
  :displayname: Enable call ringing (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enableringing
  :environment: MM_CALLS_ENABLE_RINGING

  - **true**: Ringing functionality is enabled. Direct and group message participants receive a desktop app alert and a ringing notification when a call starts.
  - **false**: **(False)** Ringing functionality is disabled.

Enable call ringing
~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| - **true**: Ringing functionality is enabled. Direct and group message   | - System Config path: **Plugins > Calls**                                                                    |
|   participants receive a desktop app alert and a ringing notification    | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``enableringing``   |
|   when a call starts.                                                    | - Environment variable: ``MM_CALLS_ENABLE_RINGING``                                                          |
| - **false**: **(Default**) Ringing functionality is disabled.            |                                                                                                              |
+--------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+

.. note::

  The ability to enable call ringing in Mattermost calls is in :ref:`Beta <administration-guide/manage/feature-labels:beta>`.

.. config:setting:: enable-pluginsav1
  :displayname: Enable AV1 codec for screen sharing (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enableav1
  :environment: MM_CALLS_ENABLE_AV1

  - **true**: Enables the ability to use the AV1 codec to encode screen sharing tracks. This can result in improved screen sharing quality for clients that support it.
  - **false**: **(False)** AV1 codec is disabled for screen sharing tracks.


Enable AV1 (Experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~
+--------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| - **true**: Enables the ability to use the AV1 codec to encode screen    | - System Config path: **Plugins > Calls**                                                                     |
|   sharing tracks. Can result in improved screen sharing quality via      | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``enableAV1``        |
|   clients that support AV1 encoding.                                     | - Environment variable: ``MM_CALLS_ENABLE_AV1``                                                               |
| - **false**: **(Default**) AV1 codec is disabled for screen sharing      |                                                                                                               |
|   tracks.                                                                |                                                                                                               |
+--------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+

.. note::

  Avoid enabling both this experimental configuration setting and the `Enable simulcast for screen sharing <#enable-simulcast-for-screen-sharing-experimental>`__ experimental configuration setting at the same time. 

.. config:setting:: enable-pluginsdcsignaling
  :displayname: Use data channels for signaling media tracks (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enabledcsignaling
  :environment: MM_CALLS_ENABLE_DC_SIGNALING

  - **true**: Clients will use WebRTC data channels for signaling of media tracks (i.e., voice, screen). This can result in a more efficient and less race-prone process, especially in case of poor network connections.
  - **false**: **(False)** Clients will use WebSockets for signaling media tracks.

Enable DC signaling (Experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| - **true**: Clients will use WebRTC data channels for signaling of media   | - System Config path: **Plugins > Calls**                                                                          |
|   tracks (i.e., voice, screen). This can result in a more efficient and    | - ``config.json`` setting: ``PluginSettings`` > ``Plugins`` > ``com.mattermost.calls`` > ``enabledcsignaling``     |
|   less race-prone process, especially in case of poor network connections. | - Environment variable: ``MM_CALLS_ENABLE_DC_SIGNALING``                                                           |
| - **false**: **(Default**) Clients will use WebSockets for signaling       |                                                                                                                    |
|   media tracks.                                                            |                                                                                                                    |
+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

.. note::

  - Version v0.18.0 or higher of the |rtcd_service| is required for this functionality to work when hosting calls through the dedicated WebRTC service.
  - Use caution when enabling this experimental configuration setting since it determines how the system handles part of the setup for WebRTC-based calls. Enabling this configuration setting may make the call setup a bit faster or more reliable in certain situations.

----

AI Agents
----------

.. note::

  Mattermost Agents is formerly known as Mattermost Copilot.

Access the following Mattermost Agents configuration settings in the System Console by going to **Plugins > Agents**.

.. config:setting:: enable-agents-plugin
  :displayname: Enable plugin (Plugins - Agents)
  :systemconsole: Plugins > Agents
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the Agents plugin on your Mattermost workspace.
  - **false**: **(Default)** Disables the Agents plugin on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| - **true**: Enables the Agents plugin on your Mattermost workspace.    | - System Config path: **Plugins > Agents**                                                             |
| - **false**: **(Default)** Disables the Agents plugin.                 | - ``config.json`` setting: N/A                                                                         |
|                                                                        | - Environment variable: N/A                                                                            |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-bot-display-name
  :displayname: Display name (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A
  :description: The bot's display name in Mattermost used to distinguish it from other bots in the system.

Display name
~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The bot's display name in Mattermost used to distinguish the bot       | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
| from other bots in the system.                                         | - ``config.json`` setting: N/A                                                                         |
|                                                                        | - Environment variable: N/A                                                                            |
| String input.                                                          |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-bot-username
  :displayname: Bot username (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A
  :description: The agent's username that can be used to @mention the AI bot in a channel.

Agent username
~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The bot's username that can be used to @mention the bot in a channel.  | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
|                                                                        | - ``config.json`` setting: N/A                                                                         |
|                                                                        | - Environment variable: N/A                                                                            |
| String input.                                                          |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-bot-avatar
  :displayname: Bot avatar (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A
  :description: Upload an image to use as the AI agent's avatar in Mattermost.

Agent avatar
~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Upload an image to use as the agent's avatar in Mattermost.            | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
|                                                                        | - ``config.json`` setting: N/A                                                                         |
|                                                                        | - Environment variable: N/A                                                                            |
| Image upload interface.                                                |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-service-type
  :displayname: Service (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A
  :description: Select the LLM service provider to use for AI assistance.

Service
~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Select the LLM service provider to use for AI assistance.              | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
|                                                                        | - ``config.json`` setting: N/A                                                                         |
|                                                                        | - Environment variable: N/A                                                                            |
| Available options: **OpenAI**, **OpenAI Compatible**, **Azure**,       |                                                                                                        |
| **Anthropic**, and **Ask Sage**.                                       |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-username
  :displayname: Username (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A
  :description: The username used to authenticate with the Ask Sage LLM service.

Username
~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The username used to authenticate with the **Ask Sage** LLM service.   | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
|                                                                        | - ``config.json`` setting: N/A                                                                         |
|                                                                        | - Environment variable: N/A                                                                            |
| String input required.                                                 |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-password
  :displayname: Password (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A
  :description: The password used to authenticate with the Ask Sage LLM service.

Password
~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The password used to authenticate with the **Ask Sage** LLM service.   | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
|                                                                        | - ``config.json`` setting: N/A                                                                         |
|                                                                        | - Environment variable: N/A                                                                            |
| String input required. This value is encrypted when stored.            |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-api-url
  :displayname: API URL (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A
  :description: The endpoint that Mattermost will use to communicate with the LLM's API.

API URL
~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The endpoint that Mattermost will use to communicate with the LLM's    | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
| API. Required for **OpenAI Compatible** and **Azure** LLM services.    | - ``config.json`` setting: N/A                                                                         |
|                                                                        | - Environment variable: N/A                                                                            |
|                                                                        |                                                                                                        |
| String input (URL format).                                             |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-api-key
  :displayname: API Key (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A
  :description: The key used to authenticate requests to the LLM's API.

API key
~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The key used to authenticate requests to the LLM's API. Required for   | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
| **OpenAI**, **OpenAI Compatible**, and **Anthropic** LLM services.     | - ``config.json`` setting: N/A                                                                         |
|                                                                        | - Environment variable: N/A                                                                            |
|                                                                        |                                                                                                        |
| String input. This value is encrypted when stored.                     |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-organization-id
  :displayname: Organization ID (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A
  :description: Ensures that requests are billed and processed under the correct organization, where applicable.

Organization ID
~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Ensures that requests are billed and processed under the correct       | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
| organization, where applicable. Supported for **OpenAI**,              | - ``config.json`` setting: N/A                                                                         |
| **OpenAI Compatible**, and **Azure** LLM services.                     | - Environment variable: N/A                                                                            |
|                                                                        |                                                                                                        |
| String input.                                                          |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-send-user-id
  :displayname: Send User ID (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A

  - **true**: Includes unique user identifiers in API requests to the LLM.
  - **false**: **(Default)** Does not include user identifiers in API requests.

Send user ID
~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| - **true**: Includes unique user identifiers in API requests to the    | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
|   LLM for analytics, personalization, and auditing purposes.           | - ``config.json`` setting: N/A                                                                         |
| - **false**: **(Default)** Does not include user identifiers.          | - Environment variable: N/A                                                                            |
|                                                                        |                                                                                                        |
| Review LLM data privacy policies before enabling this setting.         |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. note::
  We recommend reviewing LLM data privacy policies to confirm whether transmitting user information is acceptable and secure within your organization's regulatory framework. Do not enable when you need to conform to strict privacy regulations (e.g., GDPR) that limit sharing user-identifiable data with external services.

.. config:setting:: agent-default-model
  :displayname: Default Model (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A
  :description: The specific LLM that will be used to process queries if no other model is explicitly selected.

Default model
~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The specific LLM that will be used to process queries if no other      | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
| model is explicitly selected. Supported for all LLM services.          | - ``config.json`` setting: N/A                                                                         |
|                                                                        | - Environment variable: N/A                                                                            |
|                                                                        |                                                                                                        |
| String input (model name).                                             |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-input-token-limit
  :displayname: Input token limit (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A
  :description: The maximum number of tokens that the selected LLM can process in a single prompt or request.

Input token limit
~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The maximum number of tokens (chunks of text, including words,         | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
| punctuation, or special characters) that the selected LLM can          | - ``config.json`` setting: N/A                                                                         |
| process in a single prompt or request.                                 | - Environment variable: N/A                                                                            |
|                                                                        |                                                                                                        |
| Numerical value. Directly impacts the size of user queries that        |                                                                                                        |
| can be handled.                                                        |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-output-token-limit
  :displayname: Output token limit (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A
  :description: The maximum number of tokens that the LLM can generate in its response to a query.

Output token limit
~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The maximum number of tokens (chunks of text, including words,          | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
| punctuation, or special characters) that the LLM can generate in        | - ``config.json`` setting: N/A                                                                         |
| its response to a query.                                                | - Environment variable: N/A                                                                            |
|                                                                         |                                                                                                        |
| Numerical value. Must be greater than 0 for **Anthropic** LLM services. |                                                                                                        |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-streaming-timeout
  :displayname: Streaming Timeout Seconds (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A
  :description: Determines how long the system will wait for a response from the LLM when using streaming output mode.

Streaming timeout
~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Determines how long the system will wait for a response from the LLM   | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
| when using streaming (real-time) output mode. Supported for            | - ``config.json`` setting: N/A                                                                         |
| **OpenAI**, **OpenAI Compatible**, and **Azure** LLM services.         | - Environment variable: N/A                                                                            |
|                                                                        |                                                                                                        |
| Numerical value (in seconds). If the LLM takes longer than the         |                                                                                                        |
| configured timeout, the connection is terminated.                      |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. note::
  Streaming allows LLMs to display the response gradually as it's being generated, creating a smoother and more interactive experience for users.

.. config:setting:: agent-custom-instructions
  :displayname: Custom instructions (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A
  :description: Preset specific contextual or behavioral guidance for the LLM to tailor responses to your organization's needs.

Custom instructions
~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Preset specific contextual or behavioral guidance for the LLM.         | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
| Helps tailor the model's responses to align with your organization's   | - ``config.json`` setting: N/A                                                                         |
| needs, tone, or expectations. Supported for all LLM services.          | - Environment variable: N/A                                                                            |
|                                                                        |                                                                                                        |
| Text input. Instructions that the model will implicitly follow for     |                                                                                                        |
| every interaction, providing consistency and adaptability.             |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. note::
  Custom instructions can include behavioral guidance, tone preferences, contextual functions, and organizational preferences. This ensures responses adhere to your organization's language and tone guidelines and aligns the model's behavior with specific roles or purposes.

.. config:setting:: agent-enable-vision
  :displayname: Enable Vision (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the LLM to process and generate responses that incorporate image-related input or output.
  - **false**: **(Default)** Disables vision capabilities.

Enable vision
~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| - **true**: Enables the LLM to process and generate responses that     | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
|   incorporate image-related input or output. Supported for **OpenAI**, | - ``config.json`` setting: N/A                                                                         |
|   **OpenAI Compatible**, **Azure**, and **Anthropic** LLM services.    | - Environment variable: N/A                                                                            |
| - **false**: **(Default)** Disables vision capabilities.               |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. note::
  This feature is in :ref:`Beta <administration-guide/manage/feature-labels:beta>`. When enabled, the LLM can interact with prompts that include image-related input, such as image analysis, visual-related assistance, and visual outputs, where supported.

.. config:setting:: agent-enable-tools
  :displayname: Enable Tools (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the LLM to leverage additional tools or plugins to enhance its capabilities.
  - **false**: **(Default)** Disables tool capabilities.

Enable tools
~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| - **true**: Enables the LLM to leverage additional tools or plugins    | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
|   to enhance its capabilities. Supported for **OpenAI**,               | - ``config.json`` setting: N/A                                                                         |
|   **OpenAI Compatible**, **Azure**, and **Anthropic** LLM services.    | - Environment variable: N/A                                                                            |
| - **false**: **(Default)** Disables tool capabilities.                 |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. note::
  When enabled, advanced features beyond basic query processing allow the LLM to perform specialized tasks like retrieving data, integrating with external APIs, or performing computations, where supported.

.. config:setting:: agent-channel-access
  :displayname: Channel access (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A
  :description: Determines whether the bot can consume the contents of a given channel and provide answers only from content available in the channel.

Channel access
~~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Determines whether the bot can consume the contents of a given         | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
| channel and provide answers only from content available in the         | - ``config.json`` setting: N/A                                                                         |
| channel. Supported for all LLM services.                               | - Environment variable: N/A                                                                            |
|                                                                        |                                                                                                        |
| Available options: **Allow for all channels**, **Allow for selected    |                                                                                                        |
| channels**, **Block selected channels**, and **Block all channels**.   |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-user-access
  :displayname: User access (Plugins - Agents)
  :systemconsole: Plugins > Agents > Add an AI Bot
  :configjson: N/A
  :environment: N/A
  :description: Determines whether users who chat with this bot can get private assistance about content across all channels the user has access to.

User access
~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Determines whether users who chat with this bot can get private        | - System Config path: **Plugins > Agents > Add an AI Bot**                                             |
| assistance about content across all channels the user has access to.   | - ``config.json`` setting: N/A                                                                         |
| Supported for all LLM services.                                        | - Environment variable: N/A                                                                            |
|                                                                        |                                                                                                        |
| Available options: **Allow for all users**, **Allow for selected       |                                                                                                        |
| users**, and **Block selected users**.                                 |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-default-bot
  :displayname: Default bot (Plugins - Agents - AI Functions)
  :systemconsole: Plugins > Agents > AI Functions
  :configjson: N/A
  :environment: N/A
  :description: Select the default bot to use for AI functions when multiple agents are configured.

Default agent
~~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Select the default bot to use for AI functions when multiple agents    | - System Config path: **Plugins > Agents > AI Functions**                                              |
| are configured. Based on defined agents.                               | - ``config.json`` setting: N/A                                                                         |
|                                                                        | - Environment variable: N/A                                                                            |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-allowed-hostnames
  :displayname: Allowed Upstream Hostnames (Plugins - Agents - AI Functions)
  :systemconsole: Plugins > Agents > AI Functions
  :configjson: N/A
  :environment: N/A
  :description: Comma separated list of hostnames that LLMs are allowed to contact when using tools.

Allowed upstream hostnames
~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Comma-separated list of hostnames that LLMs are allowed to contact     | - System Config path: **Plugins > Agents > AI Functions**                                              |
| when using tools. Supports wildcards like ``*.mydomain.com``.          | - ``config.json`` setting: N/A                                                                         |
|                                                                        | - Environment variable: N/A                                                                            |
| Example: ``mattermost.atlassian.net`` to allow JIRA tool use.          |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-enable-llm-trace
  :displayname: Enable LLM Trace (Plugins - Agents - Debug)
  :systemconsole: Plugins > Agents > Debug
  :configjson: N/A
  :environment: N/A

  - **true**: Enables tracing of LLM requests and outputs full conversation data to the logs.
  - **false**: **(Default)** Disables LLM request tracing.

Enable LLM trace
~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| - **true**: Enables tracing of LLM requests and outputs full           | - System Config path: **Plugins > Agents > Debug**                                                     |
|   conversation data to the logs. Supported for all LLM services.       | - ``config.json`` setting: N/A                                                                         |
| - **false**: **(Default)** Disables LLM request tracing.               | - Environment variable: N/A                                                                            |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. note::
  Use this setting for debugging purposes only. When enabled, it may log sensitive conversation data.

.. config:setting:: agent-enable-embedding-search
  :displayname: Enable Embedding Search (Plugins - Agents - Embedding Search)
  :systemconsole: Plugins > Agents > Embedding Search
  :configjson: N/A
  :environment: N/A

  - **Composite**: Enables experimental embedding search capabilities for semantic search across Mattermost content.
  - **Disabled**: **(Default)** Disables embedding search capabilities.

Enable embedding search
~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| - **Composite**: Enables experimental embedding search capabilities for     | - System Config path: **Plugins > Agents > Embedding Search**                                          |
|   semantic search across Mattermost content using pgvector and              | - ``config.json`` setting: N/A                                                                         |
|   OpenAI-compatible endpoints.                                              | - Environment variable: N/A                                                                            |
| - **Disabled**: **(Default)** Disables embedding search capabilities.       |                                                                                                        |
+-----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. note::
  Embedding search requires an Enterprise license and is available as an :ref:`experimental <administration-guide/manage/feature-labels:experimental>` feature. You must also enable the ``pgvector`` extension in your PostgreSQL database. Performance may vary with large datasets.

.. config:setting:: agent-embedding-provider
  :displayname: Embedding Provider (Plugins - Agents - Embedding Search)
  :systemconsole: Plugins > Agents > Embedding Search
  :configjson: N/A
  :environment: N/A
  :description: Select the provider for generating embeddings for semantic search.

Embedding provider type
~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Select the provider for generating embeddings for semantic search.     | - System Config path: **Plugins > Agents > Embedding Search**                                          |
| Available options: **OpenAI** and **OpenAI Compatible**.               | - ``config.json`` setting: N/A                                                                         |
|                                                                        | - Environment variable: N/A                                                                            |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-embedding-api-key
  :displayname: Embedding API Key (Plugins - Agents - Embedding Search)
  :systemconsole: Plugins > Agents > Embedding Search
  :configjson: N/A
  :environment: N/A
  :description: The API key used to authenticate requests to the embedding provider's API.

API Key
~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The API key used to authenticate requests to the embedding provider's  | - System Config path: **Plugins > Agents > Embedding Search**                                          |
| API. Required for **OpenAI Compatible** embedding providers.           | - ``config.json`` setting: N/A                                                                         |
|                                                                        | - Environment variable: N/A                                                                            |
| String input. This value is encrypted when stored.                     |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-embedding-model
  :displayname: Embedding Model (Plugins - Agents - Embedding Search)
  :systemconsole: Plugins > Agents > Embedding Search
  :configjson: N/A
  :environment: N/A
  :description: The specific embedding model to use for generating vector representations of content.

Model
~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The specific embedding model to use for generating vector              | - System Config path: **Plugins > Agents > Embedding Search**                                          |
| representations of content. Must be compatible with the selected       | - ``config.json`` setting: N/A                                                                         |
| embedding provider.                                                    | - Environment variable: N/A                                                                            |
|                                                                        |                                                                                                        |
| String input (model name).                                             |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-embedding-api-url
  :displayname: Embedding API URL (Plugins - Agents - Embedding Search)
  :systemconsole: Plugins > Agents > Embedding Search
  :configjson: N/A
  :environment: N/A
  :description: The endpoint URL for the OpenAI-compatible embedding API.

API URL
~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The endpoint URL for the **OpenAI-compatible** embedding API.          | - System Config path: **Plugins > Agents > Embedding Search**                                          |
|                                                                        | - ``config.json`` setting: N/A                                                                         |
| Required string input (URL format).                                    | - Environment variable: N/A                                                                            |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-embedding-dimensions
  :displayname: Embedding Dimensions (Plugins - Agents - Embedding Search)
  :systemconsole: Plugins > Agents > Embedding Search
  :configjson: N/A
  :environment: N/A
  :description: The dimensionality of the embedding vectors, which must match the chosen embedding model.

Dimensions
~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The dimensionality of the embedding vectors, which must match the      | - System Config path: **Plugins > Agents > Embedding Search**                                          |
| chosen embedding model. Common values include 1536 for OpenAI          | - ``config.json`` setting: N/A                                                                         |
| text-embedding-ada-002 and 3072 for text-embedding-3-large.            | - Environment variable: N/A                                                                            |
|                                                                        |                                                                                                        |
| Numerical input. Common values are 768, 1024, or 1536,                 |                                                                                                        |
| depending on the model.                                                |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-chunking-strategy
  :displayname: Chunking Strategy (Plugins - Agents - Embedding Search)
  :systemconsole: Plugins > Agents > Embedding Search
  :configjson: N/A
  :environment: N/A
  :description: The method used to split content into smaller chunks for embedding generation.

Chunking strategy
~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The method used to split content into smaller chunks for embedding     | - System Config path: **Plugins > Agents > Embedding Search**                                          |
| generation. Available options: **Sentences**, **Paragraphs**,          | - ``config.json`` setting: N/A                                                                         |
| **Fixed Size**.                                                        | - Environment variable: N/A                                                                            |
|                                                                        |                                                                                                        |
| Choose based on your content type and search requirements.             |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-chunk-size
  :displayname: Chunk Size (Plugins - Agents - Embedding Search)
  :systemconsole: Plugins > Agents > Embedding Search
  :configjson: N/A
  :environment: N/A
  :description: The maximum size of each content chunk in tokens.

Chunk size
~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The maximum size of each content chunk in characters. Recommended      | - System Config path: **Plugins > Agents > Embedding Search**                                          |
| range is 512-1024 characters. The optimal value varies by chunking     | - ``config.json`` setting: N/A                                                                         |
| strategy.                                                              | - Environment variable: N/A                                                                            |
|                                                                        |                                                                                                        |
| Numerical input.                                                       |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-chunk-overlap
  :displayname: Chunk Overlap (Plugins - Agents - Embedding Search)
  :systemconsole: Plugins > Agents > Embedding Search
  :configjson: N/A
  :environment: N/A
  :description: The number of tokens that consecutive chunks share for better context continuity.

Chunk overlap
~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The number of tokens that consecutive chunks share for better          | - System Config path: **Plugins > Agents > Embedding Search**                                          |
| context continuity. Recommended range is 20-50 characters for          | - ``config.json`` setting: N/A                                                                         |
| **Fixed Size** chunking.                                               | - Environment variable: N/A                                                                            |
|                                                                        |                                                                                                        |
| Numerical input.                                                       |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-minimum-size-ratio
  :displayname: Minimum Size Ratio (Plugins - Agents - Embedding Search)
  :systemconsole: Plugins > Agents > Embedding Search
  :configjson: N/A
  :environment: N/A
  :description: The minimum ratio for chunk size validation to ensure chunks meet size requirements.

Minimum chunk size ratio
~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The minimum ratio for chunk size validation to ensure sentence         | - System Config path: **Plugins > Agents > Embedding Search**                                          |
| and paragraph chunks meet size requirements. Used to filter out        | - ``config.json`` setting: N/A                                                                         |
| chunks that are too small releative to the configured chunk size.      | - Environment variable: N/A                                                                            |
|                                                                        |                                                                                                        |
| Numerical input (decimal ratio).                                       |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: agent-reindex-all-posts
  :displayname: Reindex All Posts (Plugins - Agents - Embedding Search)
  :systemconsole: Plugins > Agents > Embedding Search
  :configjson: N/A
  :environment: N/A
  :description: Trigger a complete reindexing of all posts for embedding search.

Reindex all posts
~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Select **Reindex Posts** to trigger a complete reindexing of all       | - System Config path: **Plugins > Agents > Embedding Search**                                          |
| posts for embedding search. Use this control to rebuild the search     | - ``config.json`` setting: N/A                                                                         |
| index when changing embeddingproviders, models, or                     | - Environment variable: N/A                                                                            |
| chunking configurations.                                               |                                                                                                        |  
|                                                                        |                                                                                                        |
| Monitor indexing progress during the reindexing process.               |                                                                                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

----

.. config:setting:: gitlab
  :displayname: GitLab interoperability (Plugins)
  :systemconsole: Plugins > GitHub
  :configjson: gitlab
  :environment: N/A
  :description: Connect your GitLab instance to your Mattermost instance.

GitLab
------

See the :doc:`Connect GitLab to Mattermost </integrations-guide/gitlab>` product documentation for details.

----

.. config:setting:: github
  :displayname: GitHub interoperability (Plugins > GitHub)
  :systemconsole: Plugins > GitHub
  :configjson: github
  :environment: N/A
  :description: Connect your GitHub instance to your Mattermost instance.

GitHub
------

See the :doc:`Connect GitHub to Mattermost </integrations-guide/github>` product documentation for details.

----

.. config:setting:: jira
  :displayname: Jira interoperability (Plugins > Jira)
  :systemconsole: Plugins > Jira
  :configjson: jira
  :environment: N/A
  :description: Connect your Jira instance to your Mattermost instance.

Jira
----

See the :doc:`Connect Jira to Mattermost </integrations-guide/jira>` product documentation for available :ref:`Mattermost configuration options <integrations-guide/jira:mattermost configuration>`.

----

.. config:setting:: legal-hold
  :displayname: Perform legal holds (Plugins > Legal Hold)
  :systemconsole: Plugins > Legal Hold
  :configjson: legal-hold
  :environment: N/A
  :description: Perform legal holds in Mattermost.

Legal hold
----------

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

See the :doc:`Legal holds </administration-guide/comply/legal-hold>` product documentation for details.

----

.. config:setting:: microsoft-calendar
  :displayname: Microsoft Calendar Integration (Plugins > Microsoft Calendar)
  :systemconsole: Plugins > Microsoft Calendar
  :configjson: N/A
  :environment: N/A
  :description: Connect your Microsoft Calendar to your Mattermost instance.

Microsoft Calendar Integration
-------------------------------

See the :doc:`Connect Microsoft Calendar Integration to Mattermost </integrations-guide/microsoft-calendar>` product documentation for available :ref:`Mattermost configuration options <integrations-guide/microsoft-calendar:enable and configure the microsoft calendar integration in mattermost>`.

----

.. config:setting:: microsoft-teams-meetings
  :displayname: Microsoft Teams Meetings interoperability (Plugins > MS Teams Meetings)
  :systemconsole: Plugins >  MS Teams Meetings
  :configjson: N/A
  :environment: N/A
  :description: Connect your Microsoft Teams Meetings to your Mattermost instance.

Microsoft Teams Meetings
------------------------

See the :doc:`Connect Microsoft Teams Meetings to Mattermost </integrations-guide/microsoft-teams-meetings>` product documentation for available :ref:`Mattermost configuration options <integrations-guide/microsoft-teams-meetings:enable and configure the microsoft teams meetings integration in mattermost>`.


----


MS Teams
---------

Mattermost for Microsoft Teams enables you to break through siloes in a mixed Mattermost and Teams environment by forwarding real-time chat notifications from Teams to Mattermost.

.. tip::

  Download our `Mattermost for Microsoft Teams datasheet <https://mattermost.com/mattermost-for-microsoft-teams-datasheet/>`_ to learn how Mattermost helps your organization get more from your Microsoft tools.

Access the following configuration settings in the System Console by going to **Plugins > MS Teams**.

.. config:setting:: enable-plugin
  :displayname: Enable plugin (Plugins - MS Teams)
  :systemconsole: Plugins > MS Teams
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the MS Teams plugin on your Mattermost workspace.
  - **false**: Disables the MS Teams plugin on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

+------------------------------------------------------------------------+----------------------------------------------------+
| Enable the Mattermost for Microsoft Teams plugin for all Mattermost    | - System Config path: **Plugins > MS Teams**       |
| teams.                                                                 | - ``config.json`` setting: N/A                     |
|                                                                        | - Environment variable: N/A                        |
| - **true**: Enables MS Teams plugin on your Mattermost workspace.      |                                                    |
| - **false**: **(Default)** Disables the MS Teams plugin.               |                                                    |
+------------------------------------------------------------------------+----------------------------------------------------+

.. note::
  Use the `Enabled Teams <#enabled-teams>`__ configuration option to specify which Mattermost teams synchronize
  direct and group messages with Microsoft Teams chats.

.. config:setting:: tenant-id
  :displayname: Tenant ID (Plugins - MS Teams)
  :systemconsole: Plugins > MS Teams
  :configjson: N/A
  :environment: N/A
  :description: Specify the Microsoft Teams Tenant ID from the Azure portal.

Tenant ID
~~~~~~~~~~

+------------------------------------------------------------------------+---------------------------------------------------+
| Specify the Microsoft Teams Tenant ID from the Azure portal.           | - System Config path: **Plugins > MS Teams**      |
|                                                                        | - ``config.json`` setting: N/A                    |
|                                                                        | - Environment variable: N/A                       |
+------------------------------------------------------------------------+---------------------------------------------------+

.. config:setting:: client-id
  :displayname: Client ID (Plugins - MS Teams)
  :systemconsole: Plugins > MS Teams
  :configjson: N/A
  :environment: N/A
  :description: Specify the Microsoft Teams Client ID of your registered OAuth app in the Azure portal.

Client ID
~~~~~~~~~

+------------------------------------------------------------------------+---------------------------------------------------+
| Specify the Microsoft Teams Client ID of your registered OAuth         | - System Config path: **Plugins > MS Teams**      |
| app in the Azure portal.                                               | - ``config.json`` setting: N/A                    |
|                                                                        | - Environment variable: N/A                       |
+------------------------------------------------------------------------+---------------------------------------------------+

.. config:setting:: client-secret
  :displayname: Client secret (Plugins - MS Teams)
  :systemconsole: Plugins > MS Teams
  :configjson: N/A
  :environment: N/A
  :description: Specify the client secret of your registered OAuth app in Azure portal.

Client secret
~~~~~~~~~~~~~~

+-------------------------------------------------------------------------+---------------------------------------------------+
| Specify the client secret of your registered OAuth app in Azure portal. | - System Config path: **Plugins > MS Teams**      |
|                                                                         | - ``config.json`` setting: N/A                    |
| Alpha-numeric value.                                                    | - Environment variable: N/A                       |
+-------------------------------------------------------------------------+---------------------------------------------------+

.. config:setting:: at-rest-encryption-key
  :displayname: At rest encryption key (Plugins - MS Teams)
  :systemconsole: Plugins > MS Teams
  :configjson: N/A
  :environment: N/A
  :description: Regenerate a new encryption secret. This encryption secret will be used to encrypt and decrypt the OAuth token.

At rest encryption key
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+---------------------------------------------------+
| Regenerate a new encryption secret. This encryption secret will be     | - System Config path: **Plugins > MS Teams**      |
| used to encrypt and decrypt the OAuth token.                           | - ``config.json`` setting: N/A                    |
|                                                                        | - Environment variable: N/A                       |
| Alpha-numeric value.                                                   |                                                   |
+------------------------------------------------------------------------+---------------------------------------------------+

.. note::
  Select **Regenerate** to generate a new key. 

.. config:setting:: webhook-secret
  :displayname: Webhook secret (Plugins - MS Teams)
  :systemconsole: Plugins > MS Teams
  :configjson: N/A
  :environment: N/A
  :description: Generate the webhook secret that Microsoft Teams will use to send messages to Mattermost.

Webhook secret
~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+---------------------------------------------------+
| Generate the webhook secret that Microsoft Teams will use to send      | - System Config path: **Plugins > MS Teams**      |
| messages to Mattermost.                                                | - ``config.json`` setting: N/A                    |
|                                                                        | - Environment variable: N/A                       |
+------------------------------------------------------------------------+---------------------------------------------------+

.. note::
  Select **Regenerate** to generate a new key.

.. config:setting:: use-the-evaluation-api-pay-model
  :displayname: Use the evaluation API pay model (Plugins - MS Teams)
  :systemconsole: Plugins > MS Teams
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the evaluation API pay model. Enable this only for testing purposes. You need the pay model to be able to support enough message notifications to work in a real world scenario.
  - **false**: Disables the evaluation API pay model.

Use the evaluation API pay model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+---------------------------------------------------+
| Enable this only for testing purposes. You need the pay model to be    | - System Config path: **Plugins > MS Teams**      |
| able to support enough message notifications to work in a real         | - ``config.json`` setting: N/A                    |
| world scenario.                                                        | - Environment variable: N/A                       |
|                                                                        |                                                   |
| - **true**: Enables the evaluation API pay model.                      |                                                   |
| - **false**: **(Default)** Disables the evaluation API pay model.      |                                                   |
+------------------------------------------------------------------------+---------------------------------------------------+

.. config:setting:: sync-notifications
  :displayname: Sync Notifications
  :systemconsole: Plugins > MS Teams (Plugins - MS Teams)
  :configjson: N/A
  :environment: N/A
  :description: Notify connected users in Mattermost on receipt of a chat or group chat from Microsoft Teams.

  - **true**: Users are required to connect their Mattermost and Microsoft Teams accounts.
  - **false**: Users aren't required to connect their Mattermost and Microsoft Teams accounts.

Sync notifications
~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+----------------------------------------------------+
| Notify connected users in Mattermost on receipt of a chat or group     | - System Config path: **Plugins > MS Teams**       |
| chat from Microsoft Teams.                                             | - ``config.json`` setting: N/A                     |
|                                                                        | - Environment variable: N/A                        |
| - **true**: **(Default)** Sync notifications of chat messages for any  |                                                    |
|   connected user that enables the feature.                             |                                                    |
| - **false**: Do not sync notifications.                                |                                                    |
+------------------------------------------------------------------------+----------------------------------------------------+

.. config:setting:: maximum-size-of-attachments-to-support-complete-one-time-download
  :displayname: Maximum size of attachments to support complete one time download (Plugins - MS Teams)
  :systemconsole: Plugins > MS Teams
  :configjson: N/A
  :environment: N/A
  :description: Specify the maximum file size, in mebibytes (MiB), of attachments that can be loaded into memory. Attachment files larger than this value will be streamed from Microsoft Teams to Mattermost.

Maximum size of attachments to support complete one time download
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------+----------------------------------------------------------+
| Specify the maximum file size, in mebibytes (MiB), of attachments   | - System Config path: **Plugins > MS Teams**             |
| that can be loaded into memory. Attachment files larger than        | - ``config.json`` setting: N/A                           |
| this value will be streamed from Microsoft Teams to Mattermost.     | - Environment variable: N/A                              |
|                                                                     |                                                          |
| Numerical value. Default is **20** MiB.                             |                                                          |
+---------------------------------------------------------------------+----------------------------------------------------------+

.. config:setting:: buffer-size-for-streaming-files
  :displayname: Buffer size for streaming files (Plugins - MS Teams)
  :systemconsole: Plugins > MS Teams
  :configjson: N/A
  :environment: N/A
  :description: Specify the buffer size, in mebibytes (MiB), for streaming attachment files from Microsoft Teams to Mattermost.

Buffer size for streaming files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------+----------------------------------------------------------+
| Specify the buffer size, in mebibytes (MiB), for streaming          | - System Config path: **Plugins > MS Teams**             |
| attachment files from Microsoft Teams to Mattermost.                | - ``config.json`` setting: N/A                           |
|                                                                     | - Environment variable: N/A                              |
| Numerical value. Default is **20** MiB.                             |                                                          |
+---------------------------------------------------------------------+----------------------------------------------------------+

----

Performance metrics
-------------------

.. include:: ../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

See the :doc:`Monitor performance metrics </administration-guide/scale/collect-performance-metrics>` product documentation for available :ref:`Mattermost configuration options <administration-guide/scale/collect-performance-metrics:mattermost configuration>`.

----

Collaborative playbooks
------------------------

Use collaborative playbooks in Mattermost to provide structure, monitoring and automation for repeatable, team-based processes integrated with the Mattermost platform.

Access the following configuration settings in the System Console by going to **Plugins > Collaborative playbooks**.

.. config:setting:: enable-plugin
  :displayname: Enable plugin (Plugins - Collaborative playbooks)
  :systemconsole: Plugins > Collaborative playbooks
  :configjson: 
  :environment: 

  - **true**: **(Default)** Enables collaborative playbooks on your Mattermost workspace.
  - **false**: Disables collaborative playbooks on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------+
| - **true**: **(Default)** Enables collaborative Playbooks on your Mattermost workspace.           | - System Config path: **Plugins > Collaborative playbooks** |
| - **false**: Disables collaborative Playbooks on your Mattermost workspace.                       | - ``config.json`` setting:                                  |
|                                                                                                   | - Environment variable:                                     |
+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------+

.. config:setting:: enable-plugindteams
  :displayname: Enabled teams (Plugins - Collaborative playbooks)
  :systemconsole: Plugins > Collaborative playbooks
  :configjson: 
  :environment: 
  :description: Enable collaborative playbooks for all Mattermost teams, or for only selected teams.

Enabled teams
~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------+-------------------------------------------------------------+
| Enable collaborative playbooks for all Mattermost teams, or for only selected teams.       | - System Config path: **Plugins > Collaborative playbooks** |
|                                                                                            | - ``config.json`` setting:                                  |
|                                                                                            | - Environment variable:                                     |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------+

.. config:setting:: enable-experimental-features
  :displayname: Enable experimental features (Plugins - Collaborative playbooks)
  :systemconsole: Plugins > Collaborative playbooks
  :configjson: 
  :environment: 

  - **true**: Enables experimental playbooks features on your Mattermost workspace.
  - **false**: Disables experimental playbooks features on your Mattermost workspace.

Enable experimental features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------+-------------------------------------------------------------+
| - **true**: Enables experimental playbooks features on your Mattermost workspace.          | - System Config path: **Plugins > Collaborative playbooks** |
| - **false**: Disables experimental playbooks features on your Mattermost workspace.        | - ``config.json`` setting:                                  |
|                                                                                            | - Environment variable:                                     |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------+

----

.. config:setting:: servicenow
  :displayname: ServiceNow interoperability (Plugins)
  :systemconsole: Plugins > ServiceNow
  :configjson: servicenow
  :environment: N/A
  :description: Connect your ServiceNow instance to your Mattermost instance.

ServiceNow
----------

See the :doc:`Connect ServiceNow to Mattermost </integrations-guide/servicenow>` product documentation for available :ref:`Mattermost configuration options <integrations-guide/servicenow:mattermost configuration>`.


----

.. config:setting:: zoom
  :displayname: Zoom interoperability (Plugins)
  :systemconsole: Plugins > Zoom
  :configjson: zoom
  :environment: N/A
  :description: Connect your Zoom instance to your Mattermost instance.

Zoom
----

See the :doc:`Connect Zoom to Mattermost </integrations-guide/zoom>` product documentation for available :ref:`Mattermost configuration options <integrations-guide/zoom:mattermost configuration>`.

----

config.json-only settings
--------------------------

The following self-hosted deployment settings are only configurable in the ``config.json`` file and are not available in the System Console.

.. config:setting:: signature-public-key-files
  :displayname: Signature public key file (Plugins)
  :systemconsole: N/A
  :configjson: SignaturePublicKeyFiles
  :environment: N/A
  :description: In addition to the Mattermost plugin signing key built into the server, each public key specified is trusted to validate plugin signatures.

Signature public key files
~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

In addition to the Mattermost plugin signing key built into the server, each public key specified here is trusted to validate plugin signatures.

.. important::
  From Mattermost v10.11, pre-packaged plugins require signature validation on startup. Distributions that bundle custom pre-packaged plugins **must** configure this setting with their custom public keys to ensure proper validation of their signed plugins. Use ``PluginSettings.SignaturePublicKeyFiles`` to define custom plugin signing keys.

  When bundling custom plugins:
  
  - Drop both the plugin files and their corresponding ``.sig`` signature files into the ``prepackaged_plugins`` directory.
  - Add your custom public key using this configuration setting to validate the signatures.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SignaturePublicKeyFiles": {}`` with string array input consisting of contents that are relative or absolute paths to signature files.              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: chimera-oauth-proxy-url
  :displayname: Chimera OAuth proxy URL (Plugins)
  :systemconsole: N/A
  :configjson: ChimeraOAuthProxyUrl
  :environment: N/A
  :description: Specify the `Chimera <https://github.com/mattermost/chimera>`__ URL used by Mattermost plugins to connect with pre-created OAuth applications.

Chimera OAuth proxy URL
~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Specify the `Chimera <https://github.com/mattermost/chimera>`__ URL used by Mattermost plugins to connect with pre-created OAuth applications.

+-------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ChimeraOAuthProxyUrl": {}`` with string input.                             |
+-------------------------------------------------------------------------------------------------------------------------+
