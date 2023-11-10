Plugins configuration settings
==============================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Both self-hosted and Cloud admins can access the following configuration settings in **System Console > Plugins**. Self-hosted admins can also edit the ``config.json`` file as described in the following tables. 

- `Plugin Management <#plugin-management>`__
- `Apps <#apps>`__
- `Calls <#calls>`__
- `Google Calendar <#google-calendar>`__
- `MS Teams Sync <#ms-teams-sync>`__
- `Playbooks <#playbooks>`__
- `User Satisfaction surveys <#user-satisfaction-surveys>`__
- `Zoom <#zoom>`__

----

Plugin management
-----------------

Access the following configuration settings in the System Console by going to **Plugins > Plugin Management**.

.. config:setting:: plugins-enable
  :displayname: Enable plugins (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: .PluginSettings.Enable
  :environment: MM_PLUGINSETTINGS_ENABLE

  - **true**: **(Default)** Enables plugins on your Mattermost server.
  - **false**: Disables plugins on your Mattermost server.

Enable plugins
~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+
| - **true**: **(Default)** Enables plugins on your Mattermost server. See the `Use plugins with Mattermost <https://developers.mattermost.com/integrate/plugins/using-and-managing-plugins/>`__ documentation for details. | - System Config path: **Plugins > Plugin Management**       |
| - **false**: Disables plugins on your Mattermost server.                                                                                                                                                                  | - ``config.json`` setting: ``.PluginSettings.Enable: true`` |
|                                                                                                                                                                                                                           | - Environment variable: ``MM_PLUGINSETTINGS_ENABLE``        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+

.. config:setting:: plugins-requiresignature
  :displayname: Require plugin signature (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: .PluginSettings.RequirePluginSignature
  :environment: MM_PLUGINSETTINGS_REQUIREPLUGINSIGNATURE

  - **true**: **(Default)** Enables plugin signature validation for managed and unmanaged plugins.
  - **false**: Disables plugin signature validation for managed and unmanaged plugins.

Require plugin signature
~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| - **true**: **(Default)** Enables plugin signature validation for managed and unmanaged plugins.                                                                                      | - System Config path: **Plugins > Plugin Management**                        |
| - **false**: Disables plugin signature validation for managed and unmanaged plugins.                                                                                                  | -  ``config.json`` setting: ``.PluginSettings.RequirePluginSignature: true`` |
|                                                                                                                                                                                       | - Environment variable: ``MM_PLUGINSETTINGS_REQUIREPLUGINSIGNATURE``         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| **Note**: Pre-packaged plugins are not subject to signature validation. Plugins installed through the Marketplace are always subject to signature validation at the time of download.                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+

.. config:setting:: plugins-automaticprepackagedplugins
  :displayname: Automatic prepackaged plugins (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: .PluginSettings.AutomaticPrepackagedPlugins
  :environment: MM_PLUGINSETTINGS_AUTOMATICPREPACKAGEDPLUGINS

  - **true**: **(Default)** Mattermost automatically installs and upgrades any enabled pre-packaged plugins.
  - **false**: Mattermost does not automatically install or upgrade pre-packaged plugins.

Automatic prepackaged plugins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| - **true**: **(Default)** Mattermost automatically installs and upgrades any enabled pre-packaged plugins. If a newer version is installed, no changes are made.                | - System Config path: **Plugins > Plugin Management**                            |
| - **false**: Mattermost does not automatically install or upgrade pre-packaged plugins. Pre-packaged plugins may be installed manually from the Marketplace, even when offline. | - ``config.json`` setting: ``.PluginSettings.AutomaticPrepackagedPlugins: true`` |
|                                                                                                                                                                                 | - Environment variable: ``MM_PLUGINSETTINGS_AUTOMATICPREPACKAGEDPLUGINS``        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: plugins-enableuploads
  :displayname: Upload Plugin (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: EnableUploads
  :environment: MM_PLUGINSETTINGS_ENABLEUPLOADS

Upload Plugin
~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| - **true**:  Enables uploading of plugins from your local computer to your Mattermost server for all system admins.                | - System Config path: **Plugins > Plugin Management**                  |
| - **false**: **(Default)** Disables uploading of plugins from your local computer to your Mattermost server for all system admins. | - ``config.json`` setting: ``.PluginSettings.EnableUploads: false``    |
|                                                                                                                                    | - Environment variable: ``MM_PLUGINSETTINGS_ENABLEUPLOADS``            |
+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+


.. config:setting:: plugins-enablemarketplace
  :displayname: Enable marketplace (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: .PluginSettings.EnableMarketplace
  :environment: MM_PLUGINSETTINGS_ENABLEMARKETPLACE

  - **true**: **(Default)** Enables the plugin Marketplace on your Mattermost server for all System Admins.
  - **false**: Disables the plugin Marketplace on your Mattermost server for all System Admins.

Enable Marketplace
~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| - **true**: **(Default)** Enables the plugin Marketplace on your Mattermost server for all System Admins. | - System Config path: **Plugins > Plugin Management**                  |
| - **false**: Disables the plugin Marketplace on your Mattermost server for all System Admins.             | - ``config.json`` setting: ``.PluginSettings.EnableMarketplace: true`` |
|                                                                                                           | - Environment variable: ``MM_PLUGINSETTINGS_ENABLEMARKETPLACE``        |
+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. config:setting:: plugins-enableremotemarketplace
  :displayname: Enable remote marketplace (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: .PluginSettings.EnableRemoteMarketplace
  :environment: MM_PLUGINSETTINGS_ENABLEREMOTEMARKETPLACE

  - **true**: **(Default)** Mattermost attempts to connect to the endpoint set in MarketplaceURL.
  - **false**: Mattermost doesn't attempt to connect to a remote Marketplace, and shows only pre-packaged and installed plugins.

Enable remote Marketplace
~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| - **true**: **(Default)** Mattermost attempts to connect to the endpoint set in **Marketplace URL**.                                            | - System Config path: **Plugins > Plugin Management**                           |
|   If the connection fails, an error is displayed, and the Marketplace only shows pre-packaged and installed plugins.                            | - ``config.json`` setting: ``.PluginSettings.EnableRemoteMarketplace: true``    |
| - **false**:  Mattermost does not attempt to connect to a remote Marketplace.                                                                   | - Environment variable: ``MM_PLUGINSETTINGS_ENABLEREMOTEMARKETPLACE``           |
|   The Marketplace shows only pre-packaged and installed plugins. Use this setting if your Mattermost server cannot connect to the Internet.     |                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| **Notes**:                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                   |
| - From Mattermost v9.1, set this configuration setting value to ``true`` to access a configured remote marketplace URL.                                                                                                           |
| - For Mattermost v9.0, the ``MM_FEATUREFLAGS_STREAMLINEDMARKETPLACE`` feature flag must be set to ``false``, and this configuration setting must be set to ``true`` to access a configured remote marketplace URL.                |
| - Each Mattermost host must have network access to the endpoint set in MarketplaceURL.                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+

.. config:setting:: plugins-marketplaceurl
  :displayname: Marketplace URL (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: .PluginSettings.MarketplaceURL
  :environment: MM_PLUGINSETTINGS_MARKETPLACEURL
  :description: This setting stores the URL for the remote Marketplace. Default is **https://api.integrations.mattermost.com**.

Marketplace URL
~~~~~~~~~~~~~~~

+----------------------------------------------------------------------+---------------------------------------------------------------+
| This setting stores the URL for the remote Markeplace.               | - System Config path: **Plugins > Plugin Management**         |
|                                                                      | - ``config.json`` setting: ``.PluginSettings.MarketplaceURL`` |
| String input. Default is **https://api.integrations.mattermost.com** | - Environment variable: ``MM_PLUGINSETTINGS_MARKETPLACEURL``  |
+----------------------------------------------------------------------+---------------------------------------------------------------+

.. config:setting:: plugins-installedpluginstates
  :displayname: Installed plugin state (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: .PluginSettings.PluginStates
  :environment: MM_PLUGINSETTINGS_PLUGINSTATES
  :description: This setting is a list of installed plugins and their status as enabled or disabled.

Installed plugin state
~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+
| This setting is a list of installed plugins and their status as enabled or disabled.                                                                                                                         | - System Config path: **Plugins > Plugin Management**       |
|                                                                                                                                                                                                              | - ``config.json`` setting: ``.PluginSettings.PluginStates`` |
| The ``config.json`` setting is an object. The object keys are plugin IDs, e.g. ``com.mattermost.apps``. Each key maps to an object that contains an ``Enable`` key that can be set as ``true`` or ``false``. | - Environment variable: ``MM_PLUGINSETTINGS_PLUGINSTATES``  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+

.. config:setting:: plugins-pluginsettings
  :displayname: Plugin settings (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: .PluginSettings.Plugins
  :environment: MM_PLUGINSETTINGS_PLUGINS
  :description: This setting contains plugin-specific data.

Plugin settings
~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------+
| This setting contains plugin-specific data.                                                                                                                            | - System Config path: **Plugins > Plugin Management**  |
|                                                                                                                                                                        | - ``config.json`` setting: ``.PluginSettings.Plugins`` |
| The ``config.json`` setting is an object. The object keys are plugin IDs, e.g. ``com.mattermost.apps``. Each key maps to an object that contains plugin-specific data. | - Environment variable: ``MM_PLUGINSETTINGS_PLUGINS``  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------+

----

Apps
----

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. note::
  
  From Mattermost v8.1, this third-party plugin is managed by the Mattermost Community.

Access the following configuration settings in the System Console by going to **Plugins > Apps**.

To create your own Mattermost App, see the `Mattermost Apps <https://developers.mattermost.com/integrate/apps/>`__ developer documentation.

.. config:setting:: plugins-appsenable
  :displayname: Enable plugin (Plugins - Apps)
  :systemconsole: Plugins > Apps
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the Apps plugin on your Mattermost server.
  - **false**: (Default) Disables the Apps plugin on your Mattermost server.

Enable plugin
~~~~~~~~~~~~~

+----------------------------------------------------------------------------+-------------------------------------------------------------+
| - **true**: Enables the Apps plugin on your Mattermost server.             | - System Config path: **Plugins > Apps**                    |
| - **false**: (Default) Disables the Apps plugin on your Mattermost server. |                                                             |
|                                                                            |                                                             |
+----------------------------------------------------------------------------+-------------------------------------------------------------+

----

Calls
-----

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Plugins > Calls**.

.. config:setting:: plugins-callsenable
  :displayname: Enable plugin (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.PluginStates.com.mattermost.calls.Enable
  :environment: MM_PLUGINSETTINGS_PLUGINSTATES_COM_MATTERMOST_CALLS

  - **true**: (Default) Enables the calls plugin on your Mattermost workspace.
  - **false**: Disables the calls plugin on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| - **true**: (Default) Enables the Calls plugin on your Mattermost workspace.   | - System Config path: **Plugins > Calls**                                              |
| - **false**: Disables the Calls plugin on your Mattermost workspace.           | - ``config.json`` setting: ``PluginSettings.PluginStates.com.mattermost.calls.Enable`` |
|                                                                                | - Environment variable: ``MM_PLUGINSETTINGS_PLUGINSTATES_COM_MATTERMOST_CALLS``        |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsrtcserveraddress
  :displayname: RTC server port (UDP) (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.udpserveraddress
  :environment: N/A
  :description: The IP address used by the RTC server to listen for UDP connections. By default the service listens on all the available interfaces.

RTC server address (UDP)
~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| This setting controls the IP address the RTC server listens for UDP connections. All calls UDP traffic will be served through this IP.     | - System Config path: **Plugins > Calls**                                                                 |
|                                                                                                                                            | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.udpserveraddress``               |
| Changing this setting requires a plugin restart to take effect.                                                                            | - Environment variable: N/A                                                                               |
| If left unset (default value) the service will listen on all the available interfaces.                                                     |                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| **Note**: This setting is only applicable when not running calls through the standalone ``rtcd`` service.                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsrtcserveraddress
  :displayname: RTC server port (TCP) (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.tcpserveraddress
  :environment: N/A
  :description: The IP address used by the RTC server to listen for TCP connections. By default the service listens on all the available interfaces.

RTC server address (TCP)
~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| This setting controls the IP address the RTC server listens for TCP connections. All calls TCP traffic will be served through this IP.     | - System Config path: **Plugins > Calls**                                                                 |
|                                                                                                                                            | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.tcpserveraddress``               |
| Changing this setting requires a plugin restart to take effect.                                                                            | - Environment variable: N/A                                                                               |
| If left unset (default value) the service will listen on all the available interfaces.                                                     |                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| **Note**:                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                        |
| - This setting is only applicable when not running calls through the standalone ``rtcd`` service.                                                                                                                                                      |
|                                                                                                                                                                                                                                                        |
| - This setting is available starting in plugin version 0.17.                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsrtcserverportudp
  :displayname: RTC server port (UDP) (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.udpserverport
  :environment: N/A
  :description: The UDP port the RTC server will listen on. All calls UDP traffic will be served through this port. Default port is **8443**.

RTC server port (UDP)
~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| This setting controls the UDP port listened on by the RTC server. All calls UDP traffic will be served through this port.     | - System Config path: **Plugins > Calls**                                                              |
|                                                                                                                               | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.udpserverport``               |
|                                                                                                                               | - Environment variable: N/A                                                                            |
| Changing this setting requires a plugin restart to take effect.                                                               |                                                                                                        |
|                                                                                                                               |                                                                                                        |
| Default is **8443**.                                                                                                          |                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| **Note**: This setting is only applicable when not running calls through the standalone ``rtcd`` service.                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsrtcserverporttcp
  :displayname: RTC server port (TCP) (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.tcpserverport
  :environment: N/A
  :description: The TCP port the RTC server will listen on. All calls TCP traffic will be served through this port. Default port is **8443**.

RTC server port (TCP)
~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| This setting controls the TCP port listened on by the RTC server. All calls TCP traffic will be served through this port.     | - System Config path: **Plugins > Calls**                                                              |
|                                                                                                                               | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.tcpserverport``               |
|                                                                                                                               | - Environment variable: N/A                                                                            |
| Changing this setting requires a plugin restart to take effect.                                                               |                                                                                                        |
|                                                                                                                               |                                                                                                        |
| Default is **8443**.                                                                                                          |                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| **Note**:                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                        |
| - This setting is only applicable when not running calls through the standalone ``rtcd`` service.                                                                                                                                      |
|                                                                                                                                                                                                                                        |
| - This setting is available starting in plugin version 0.17.                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+


.. config:setting:: plugins-enableonspecificchannels
  :displayname: Enable on specific channels (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.allowenablecalls
  :environment: N/A
  :description: Manage who can enable or disable calls on specific channels (deprecated from Mattermost v7.7)

Enable on specific channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Admins can't configure this setting from Mattermost v7.7; it's hidden and always enabled*

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+----------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| - **true**: Channel admins can enable or disable calls on specific channels. Participants in DMs/GMs can also enable or disable calls. | - System Config path: **Plugins > Calls**                                                                  |
| - **false**: Only System Admins can enable or disable calls on specific channels.                                                      | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.allowenablecalls``                |
|                                                                                                                                        | - Environment variable: N/A                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-testmode
  :displayname: Test mode (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.defaultenabled
  :environment: N/A
  :description: A setting to allow system admins to test calls before making them available across the deployment. This setting was called **Enable on all channels** up until Mattermost v7.7.

Test mode
~~~~~~~~~

*This setting was called Enable on all channels up until Mattermost v7.7*

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| - **true**: Only System Admins can start calls in channels.                                                                                | - System Config path: **Plugins > Calls**                                                                                                          |
| - **false**: All team members can start calls in channels.                                                                                 | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.defaultenabled``                                                          |
|                                                                                                                                            | - Environment variable: N/A                                                                                                                        |
+--------------------------------------------------------------+-----------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **Note**: Use this setting to confirm calls work as expected. When **true**, users attempting to start calls are prompted to contact System Admins. System Admins are prompted to confirm that calls are working as expected before switching to live mode.                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsicehost
  :displayname: ICE host override (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.icehostoverride
  :environment: N/A
  :description: An optional override to the host that gets advertised to clients when connecting to calls. When empty or unset, the RTC service will attempt to automatically find the instance's public IP through STUN.

ICE host override
~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This setting can be used to override the host addresses that get advertised to clients when connecting to calls. The accepted formats are the following:                                                                                                                                 | - System Config path: **Plugins > Calls**                                                                                                                                      |
|                                                                                                                                                                                                                                                                                          | - ``config.json`` setting:  ``PluginSettings.Plugins.com.mattermost.calls.icehostoverride``                                                                                    |
|                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                |
| - A single IP address (e.g. ``10.0.0.1``).                                                                                                                                                                                                                                               |                                                                                                                                                                                |
| - A single hostname or FQDN (e.g. ``calls.myserver.tld``).                                                                                                                                                                                                                               |                                                                                                                                                                                |
| - (starting in v0.17.0) A comma separated list of externalAddr/internalAddr mappings (e.g. ``10.0.0.1/172.0.0.1,10.0.0.2/172.0.0.2``).                                                                                                                                                   |                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                |
| This is an optional field. Changing this setting requires a plugin restart to take effect.                                                                                                                                                                                               |                                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Note**:                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|   - This setting is only applicable when not running calls through the standalone ``rtcd`` service.                                                                                                                                                                                                                                                                                                                                                                       |
|   - Depending on the network infrastructure (e.g. instance behind a NAT device) it may be necessary to set this field to the client facing external IP for clients to connect. When empty or unset, the RTC service will attempt to find the instance's public IP through STUN.                                                                                                                                                                                           |
|   - A hostname (e.g. domain name) can be specified in this setting, but an IP address will be passed to clients. This means that a DNS resolution happens on the Mattermost instance which could result in a different IP address from the one the clients would see, causing connectivity to fail. When in doubt, we recommend using an IP address directly or confirming that the resolution on the host side reflects the one on the client.                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |ice_host_override_link| replace:: `ICE Host Override <plugins-configuration-settings.html#ice-host-override>`__

.. config:setting:: plugins-callsrtcdserviceurl
  :displayname: RTCD service URL (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.rtcdserviceurl
  :environment: N/A
  :description: The URL to a running `rtcd <https://github.com/mattermost/rtcd>`__ service instance that will host the calls. When set (non empty) all the calls will be handled by this external service.

RTCD service URL
~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| The URL to a running `rtcd <https://github.com/mattermost/rtcd>`__ service instance that will host the calls. | - System Config path: **Plugins > Calls**                                                                                                                 |
|                                                                                                               | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.rtcdserviceurl``                                                                 |
|                                                                                                               | - Environment variable: N/A                                                                                                                               |
| When set (non empty) all the calls will be handled by this external service.                                  |                                                                                                                                                           |
|                                                                                                               |                                                                                                                                                           |
| This is an optional field. Changing this setting requires a plugin restart to take effect.                    |                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Note**:                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                           |
| - The client will self-register the first time it connects to the service and store the authentication key in the database. If no client ID is explicitly provided, the diagnostic ID of the Mattermost installation will be used.                                        |
| - The service URL supports credentials in the form ``http://clientID:authKey@hostname``. Alternatively these can be passed through environment overrides to the Mattermost server, namely ``MM_CALLS_RTCD_CLIENT_ID`` and ``MM_CALLS_RTCD_AUTH_KEY``                      |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsmaxcallparticipants
  :displayname: Max call participants (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.maxcallparticipants
  :environment: N/A
  :description: The maximum number of participants that can join a single call. Default value is **0** (unlimited). The maximum recommended setting is 200.

Max call participants
~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| This setting limits the number of participants that can join a single call. | - System Config path: **Plugins > Calls**                                                                     |
|                                                                             | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.maxcallparticipants``                |
|                                                                             | - Environment variable: N/A                                                                                   |
| Default is **0** (no limit).                                                |                                                                                                               |
+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Note**: This setting is optional, but the recommended maximum number of participants is **200**.                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsiceservers
  :displayname: ICE server configurations (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.iceserversconfigs
  :environment: N/A
  :description: A list of ICE servers (STUN/TURN) to be used by the service. Value should be valid JSON. Default value is **[{"urls": ["stun:stun.global.calls.mattermost.com:3478"]}]**.

ICE servers configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| This setting stores a list of ICE servers (STUN/TURN) in JSON format to be used by the service.                                                                                                                           | - System Config path: **Plugins > Calls**                                                        |
|                                                                                                                                                                                                                           | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.iceserversconfigs``     |
|                                                                                                                                                                                                                           | - Environment variable: N/A                                                                      |
| This is an optional field. Changing this setting may require a plugin restart to take effect.                                                                                                                             |                                                                                                  |
|                                                                                                                                                                                                                           |                                                                                                  |
| Default is ``[{"urls": ["stun:stun.global.calls.mattermost.com:3478"]}]``                                                                                                                                                 |                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| **Note**:                                                                                                                                                                                                                 |                                                                                                  |
|                                                                                                                                                                                                                           |                                                                                                  |
| - The configurations above, containing STUN and TURN servers, are sent to the clients and used to generate local candidates.                                                                                              |                                                                                                  |
|                                                                                                                                                                                                                           |                                                                                                  |
| - If hosting calls through the plugin (i.e. not using the |rtcd_service|) any configured STUN server may also be used to find the instance's public IP when none is provided through the |ice_host_override_link| option. |                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+

.. |rtcd_service| replace:: `rtcd service <calls-deployment.html#the-rtcd-service>`__

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

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Note**:                                                                                                                                                                     |
| - To get TURN generated credentials to work you must provide a secret through the *TURN static auth secret* setting below.                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsturnauthsecret
  :displayname: TURN static auth secret (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.turnstaticauthsecret
  :environment: N/A
  :description: A static secret used to generate short-lived credentials for TURN servers.

TURN static auth secret
~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+----------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| A static secret used to generate short-lived credentials for TURN servers. | - System Config path: **Plugins > Calls**                                                                      |
|                                                                            | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.turnstaticauthsecret``                |
|                                                                            | - Environment variable: N/A                                                                                    |
| This is an optional field.                                                 |                                                                                                                |
+----------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsturncredentialsexpiration
  :displayname: TURN credentials expiration (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.turncredentialsexpirationminutes
  :environment: N/A
  :description: The expiration, in minutes, of the short-lived credentials generated for TURN servers.

TURN credentials expiration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| The expiration, in minutes, of the short-lived credentials generated for TURN servers. | - System Config path: **Plugins > Calls**                                                                                  |
|                                                                                        | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.turncredentialsexpirationminutes``                |
|                                                                                        | - Environment variable: N/A                                                                                                |
| Default is **1440** (one day).                                                         |                                                                                                                            |
+----------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsserversideturn
  :displayname: Server side TURN (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.serversideturn
  :environment: N/A

  - **true**: The RTC server will use the configured TURN candidates for server-initiated connections.
  - **false**: TURN will be used only on the client-side.

Server side TURN
~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| - **true**: The RTC server will use the configured TURN candidates for server-initiated connections. | - System Config path: **Plugins > Calls**                                                                |
| - **false**: TURN will be used only on the client-side.                                              | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.serversideturn``                |
|                                                                                                      | - Environment variable: N/A                                                                              |
| Changing this setting requires a plugin restart to take effect.                                      |                                                                                                          |
+------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsallowscreensharing
  :displayname: Allow screen sharing (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.allowscreensharing
  :environment: N/A

  - **true**: Call participants will be allowed to share their screen.
  - **false**: Call participants won't be allowed to share their screen.

Allow screen sharing
~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| - **true**: Call participants will be allowed to share their screen.   | - System Config path: **Plugins > Calls**                                                                    |
| - **false**: Call participants won't be allowed to share their screen. | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.allowscreensharing``                |
|                                                                        | - Environment variable: N/A                                                                                  |
| Changing this setting requires a plugin restart to take effect.        |                                                                                                              |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsenablesimulcast
  :displayname: Enable simulcast for screen sharing (Experimental) (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enablesimulcast
  :environment: N/A
  :description: When set to true it enables simulcast for screen sharing. This can help to improve screen sharing quality.

Enable simulcast for screen sharing (Experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| - **true**: Enables simulcast for screen sharing. This can help to improve screen sharing quality.                     | - System Config path: **Plugins > Calls**                                                                |
| - **false**: Disables simulcast for screen sharing.                                                                    | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.enablesimulcast``               |
|                                                                                                                        | - Environment variable N/A                                                                               |
+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **Note**: This functionality has the following requirements:                                                                                                                                                                      |
|                                                                                                                                                                                                                                   |
| - Calls plugin version >= v0.16.0                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                   |
| - ``rtcd`` version >= v0.10.0 (if in use)                                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-enablecallrecordings
  :displayname: Enable call recordings (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enablerecordings
  :environment: N/A
  :description: Allow call hosts to record meeting video and audio. 

Enable call recordings (Beta)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| - **true**: Allows call hosts to record meeting video and audio.                                                                                      | - System Config path: **Plugins > Calls**                                                                  |
| - **false**: **(Default)** Call recording functionality is not available to hosts.                                                                    | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.enablerecordings``                |
|                                                                                                                                                       |                                                                                                            |
| Recordings include the entire call window view along with participants' audio track and any shared screen video. Recordings are stored in Mattermost. |                                                                                                            |
|                                                                                                                                                       |                                                                                                            |
| Changing this setting requires a plugin restart to take effect.                                                                                       |                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-jobserviceurl
  :displayname: Job service URL (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.jobserviceurl
  :environment: N/A
  :description: The URL to a running job service where all the processing related to recordings happens.
  
Job service URL
~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| The URL to a running job service where all the processing related to recordings happens. The recorded files produced are stored in Mattermost. | - System Config path: **Plugins > Calls**                                                                                        |
|                                                                                                                                                | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.jobserviceurl``                                         |
| This is a required field. Changing this setting requires a plugin restart to take effect.                                                      |                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| **Note**:                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                   |
| - The client will self-register the first time it connects to the service and store the authentication key in the database. If no client ID is explicitly provided, the diagnostic ID of the Mattermost installation will be used.                                                |
| - The service URL supports credentials in the form ``http://clientID:authKey@hostname``. Alternatively these can be passed through environment overrides to the Mattermost server, namely ``MM_CALLS_JOB_SERVICE_CLIENT_ID`` and ``MM_CALLS_JOB_SERVICE_AUTH_KEY``.               |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-maximumcallrecordingduration
  :displayname: Maximum call recording duration (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.maxrecordingduration
  :environment: N/A
  :description: The maximum duration of a call recording in minutes.
  
Maximum call recording duration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| The maximum duration of a call recording in minutes.                                                                        | - System Config path: **Plugins > Calls**                                                                      |
|                                                                                                                             | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.maxrecordingduration``                |
|                                                                                                                             | - Environment variable: N/A                                                                                    |
| The default is **60**. The maximum is **180**. This is a required value.                                                    |                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-recordingquality
  :displayname: Call recording quality (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.recordingquality
  :environment: N/A
  :description: The audio and video quality of call recordings.

Call recording quality
~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| The audio and video quality of call recordings. Available options are: *Low*, *Medium* and *High*.                          | - System Config path: **Plugins > Calls**                                                                                                                      |
|                                                                                                                             | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.recordingquality``                                                                    |
| The default is **Medium**. This is a required value.                                                                        |                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Note**: The quality setting will affect the performance of the recording service and the file size of recordings. Refer to the `deployment section <configure/calls-deployment.html#configure-recording>`__ for more information.                                                          |
+-----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsenableipv6
  :displayname: (Experimental) Enable IPv6 (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enableipv6
  :environment: N/A

  - **true**: The RTC service will work in dual-stack mode, listening for IPv6 connections and generating candidates in addition to IPv4 ones.
  - **false**: The RTC service will only listen for IPv4 connections.

(Experimental) Enable IPv6
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| - **true**: The RTC service will work in dual-stack mode, listening for IPv6 connections and generating candidates in addition to IPv4 ones. | - System Config path: **Plugins > Calls**                                                                |
| - **false**: The RTC service will only listen for IPv4 connections.                                                                          | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.enableipv6``                    |
|                                                                                                                                              | - Environment variable: N/A                                                                              |
| Default value is **false**.                                                                                                                  |                                                                                                          |
|                                                                                                                                              |                                                                                                          |
| Changing this setting requires a plugin restart to take effect.                                                                              |                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **Note**:                                                                                                                                                                                                                                               |
| - This setting is only applicable when not running calls through the standalone ``rtcd`` service.                                                                                                                                                       |
| - This setting is available starting in plugin version 0.17.                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

.. |note| replace:: .

Enable call ringing (Beta)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. config:setting:: plugins-enablecallringing
  :displayname: Enable call ringing (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls. enableringing
  :environment: N/A
  :description: Enable or disable incoming call desktop alerts and ringing notifications

+--------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| - **true**: Ringing functionality is enabled. Direct and group message   | - System Config path: **Plugins > Calls**                                                   |
|   participants receive a desktop app alert and a ringing notification    | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls. enableringing``   |
|   when a call starts.                                                    | - Environment variable: N/A                                                                 |
| - **false**: **(Default**) Ringing functionality is disabled.            |                                                                                             |
+--------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+

----

Google Calendar
----------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

The Mattermost Google Calendar plugin enables a two-way integration between Mattermost and Google Calendar.

Access the following configuration settings in the System Console by going to **Plugins > Google Calendar**.

.. config:setting:: plugins-googlecalendarenable
  :displayname: Enable plugin (Plugins - Google Calendar)
  :systemconsole: Plugins > Google Calendar
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the Google Calendar plugin on your Mattermost workspace.
  - **false**: Disables the Google Calendar plugin on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

+--------------------------------------------------------------------------+------------------------------------------------------+
| Enable the Mattermost Google Calendar plugin for all Mattermost teams.   | - System Config path: **Plugins > Google Calendar**  |
|                                                                          | - ``config.json`` setting: N/A                       |
| - **true**: Enables Google Calendar plugin on your Mattermost workspace. | - Environment variable: N/A                          |
| - **false**: **(Default)** Disables the Google Calendar plugin.          |                                                      |
+--------------------------------------------------------------------------+------------------------------------------------------+

.. config:setting:: plugins-googlecalendaradminuserids
  :displayname: Enable plugin (Plugins - Google Calendar)
  :systemconsole: Plugins > Google Calendar
  :configjson: N/A
  :environment: N/A

Admin user IDs
~~~~~~~~~~~~~~

+--------------------------------------------------------------------------+------------------------------------------------------+
| A comma-separated list of users authorized to manage the plugin.         | - System Config path: **Plugins > Google Calendar**  |
|                                                                          | - ``config.json`` setting: N/A                       |
| Go to **System Console > User Management > Users** to access user IDs.   | - Environment variable: N/A                          |
+--------------------------------------------------------------------------+------------------------------------------------------+

.. config:setting:: plugins-googlecalendarcopypluginlogs
  :displayname: Enable plugin (Plugins - Google Calendar)
  :systemconsole: Plugins > Google Calendar
  :configjson: N/A
  :environment: N/A

Copy plugin logs to admins, as bot messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------+------------------------------------------------------+
| The level of detail in log events for the plugin.                        | - System Config path: **Plugins > Google Calendar**  |
|                                                                          | - ``config.json`` setting: N/A                       |
| Can be one of: **None**, **Debug**, **Info**, **Warning**, or **Error**. | - Environment variable: N/A                          |
+--------------------------------------------------------------------------+------------------------------------------------------+

.. config:setting:: plugins-googlecalendardisplayfullcontext
  :displayname: Enable plugin (Plugins - Google Calendar)
  :systemconsole: Plugins > Google Calendar
  :configjson: N/A
  :environment: N/A

  - **true**: Displays full context for each admin log entry.
  - **false**: Full context isn't displayed for each admin log entry.

Display full context for each admin log message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------+------------------------------------------------------+
| Specify whether full context is displayed for log messages.              | - System Config path: **Plugins > Google Calendar**  |
|                                                                          | - ``config.json`` setting: N/A                       |
| - **true**: Displays full context for each admin log entry.              | - Environment variable: N/A                          |
| - **false**: Full context isn't displayed for each admin log entry.      |                                                      |
+--------------------------------------------------------------------------+------------------------------------------------------+

.. config:setting:: plugins-googlecalendarencryptionkey
  :displayname: Enable plugin (Plugins - Google Calendar)
  :systemconsole: Plugins > Google Calendar
  :configjson: N/A
  :environment: N/A

Encryption key
~~~~~~~~~~~~~~

+--------------------------------------------------------------------------+------------------------------------------------------+
| The encryption key used to store data in the database.                   | - System Config path: **Plugins > Google Calendar**  |
|                                                                          | - ``config.json`` setting: N/A                       |
|                                                                          | - Environment variable: N/A                          |
+--------------------------------------------------------------------------+------------------------------------------------------+
| **Note**: Select **Regenerate** to generate a new encryption key. When you regenerate this value, all users will need to        |
| `reconnect their Google Calendar with Mattermost </collaborate/use-mattermost-google-calendar-plugin.html#connect-your          |
| google-calendar-account-to-mattermost>`__.                                                                                      |
+--------------------------------------------------------------------------+------------------------------------------------------+

.. config:setting:: plugins-googlecalendarappclientid
  :displayname: Enable plugin (Plugins - Google Calendar)
  :systemconsole: Plugins > Google Calendar
  :configjson: N/A
  :environment: N/A

Google application client ID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------+------------------------------------------------------+
| The Google App Authentication Client ID.                                 | - System Config path: **Plugins > Google Calendar**  |
|                                                                          | - ``config.json`` setting: N/A                       |
|                                                                          | - Environment variable: N/A                          |
+--------------------------------------------------------------------------+------------------------------------------------------+

.. config:setting:: plugins-googlecalendarclientsecret
  :displayname: Enable plugin (Plugins - Google Calendar)
  :systemconsole: Plugins > Google Calendar
  :configjson: N/A
  :environment: N/A

Google client secret
~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------+------------------------------------------------------+
| The Google App Authentication Client Secret.                             | - System Config path: **Plugins > Google Calendar**  |
|                                                                          | - ``config.json`` setting: N/A                       |
|                                                                          | - Environment variable: N/A                          |
+--------------------------------------------------------------------------+------------------------------------------------------+

----

MS Teams Sync
-------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Mattermost for Microsoft Teams enables you to collaborate with technical & operations teams seamlessly through the Mattermost app, without leaving Microsoft Teams.

Access the following configuration settings in the System Console by going to **Plugins > MS Teams Sync**.

.. include:: ../_static/badges/academy-msteams.rst
  :start-after: :nosearch:

.. config:setting:: plugins-msteamssyncenable
  :displayname: Enable plugin (Plugins - MS Teams Sync)
  :systemconsole: Plugins > MS Teams Sync
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the MS Teams Sync plugin on your Mattermost workspace.
  - **false**: Disables the MS Teams Sync plugin on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

+------------------------------------------------------------------------+----------------------------------------------------+
| Enable the Mattermost for Microsoft Teams plugin for all Mattermost    | - System Config path: **Plugins > MS Teams Sync**  |
| teams.                                                                 | - ``config.json`` setting: N/A                     |
|                                                                        | - Environment variable: N/A                        |
| - **true**: Enables MS Teams Sync plugin on your Mattermost workspace. |                                                    |
| - **false**: **(Default)** Disables the MS Teams Sync plugin.          |                                                    |
+------------------------------------------------------------------------+----------------------------------------------------+
| **Note**: Use the `Enabled Teams <#enabled-teams>`__ configuration option to specify which Mattermost teams synchronize     |
| direct and group messages with Microsoft Teams chats.                                                                       |
+------------------------------------------------------------------------+----------------------------------------------------+

.. config:setting:: plugins-msteamssynctenantid
  :displayname: Tenant ID (Plugins - MS Teams Sync)
  :systemconsole: Plugins > MS Teams Sync
  :configjson: N/A
  :environment: N/A
  :description: Specify the Microsoft Teams Tenant ID.

Tenant ID
~~~~~~~~~~

+------------------------------------------------------------------------+---------------------------------------------------+
| Specify the Microsoft Teams Tenant ID.                                 | - System Config path: **Plugins > MS Teams Sync** |
|                                                                        | - ``config.json`` setting: N/A                    |
|                                                                        | - Environment variable: N/A                       |
+------------------------------------------------------------------------+---------------------------------------------------+

.. config:setting:: plugins-msteamssyncclientid
  :displayname: Client ID (Plugins - MS Teams Sync)
  :systemconsole: Plugins > MS Teams Sync
  :configjson: N/A
  :environment: N/A
  :description: Specify the Microsoft Teams Client ID.

Client ID
~~~~~~~~~

+------------------------------------------------------------------------+---------------------------------------------------+
| Specify the Microsoft Teams Client ID.                                 | - System Config path: **Plugins > MS Teams Sync** |
|                                                                        | - ``config.json`` setting: N/A                    |
|                                                                        | - Environment variable: N/A                       |
+------------------------------------------------------------------------+---------------------------------------------------+

.. config:setting:: plugins-msteamssyncclientsecret
  :displayname: Client secret (Plugins - MS Teams Sync)
  :systemconsole: Plugins > MS Teams Sync
  :configjson: N/A
  :environment: N/A
  :description: Specify the Microsoft Teams Client Secret.

Client secret
~~~~~~~~~~~~~~

+------------------------------------------------------------------------+---------------------------------------------------+
| Specify the Microsoft Teams Client Secret.                             | - System Config path: **Plugins > MS Teams Sync** |
|                                                                        | - ``config.json`` setting: N/A                    |
| Alpha-numeric value.                                                   | - Environment variable: N/A                       |
+------------------------------------------------------------------------+---------------------------------------------------+

.. config:setting:: plugins-msteamssyncgenerateatrestencryptionkey
  :displayname: At rest encryption key (Plugins - MS Teams Sync)
  :systemconsole: Plugins > MS Teams Sync
  :configjson: N/A
  :environment: N/A
  :description: Generate the AES encryption key used to encrypt sotred access tokens.

At rest encryption key
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+---------------------------------------------------+
| Generate the AES encryption key used to encrypt sotred access tokens.  | - System Config path: **Plugins > MS Teams Sync** |
|                                                                        | - ``config.json`` setting: N/A                    |
| Alpha-numeric value.                                                   | - Environment variable: N/A                       |
+------------------------------------------------------------------------+---------------------------------------------------+
| **Note**: Select **Regenerate** to generate a new key.                                                                     |
+------------------------------------------------------------------------+---------------------------------------------------+

.. config:setting:: plugins-msteamssyncgeneratewebhooksecret
  :displayname: Webhook secret (Plugins - MS Teams Sync)
  :systemconsole: Plugins > MS Teams Sync
  :configjson: N/A
  :environment: N/A
  :description: Generate the webhook secret that Microsoft Teams will use to send messages to Mattermost.

Webhook secret
~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+---------------------------------------------------+
| Generate the webhook secret that Microsoft Teams will use to send      | - System Config path: **Plugins > MS Teams Sync** |
| messages to Mattermost.                                                | - ``config.json`` setting: N/A                    |
|                                                                        | - Environment variable: N/A                       |
+------------------------------------------------------------------------+---------------------------------------------------+
| **Note**: Select **Regenerate** to generate a new key.                                                                     |
+------------------------------------------------------------------------+---------------------------------------------------+

.. config:setting:: plugins-msteamssyncuseevaluationapipaymodel
  :displayname: Use the evaluation API pay model (Plugins - MS Teams Sync)
  :systemconsole: Plugins > MS Teams Sync
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the evaluation API pay model.
  - **false**: Disables the evaluation API pay model.

Use the evaluation API pay model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+---------------------------------------------------+
| Enable the evaluation API pay model to receive a limited number of     | - System Config path: **Plugins > MS Teams Sync** |
| change notifications. Ensure you keep the number of notifications low. | - ``config.json`` setting: N/A                    |
|                                                                        | - Environment variable: N/A                       |
| - **true**: Enables the evaluation API pay model.                      |                                                   |
| - **false**: **(Default)** Disables the evaluation API pay model.      |                                                   |
+------------------------------------------------------------------------+---------------------------------------------------+

.. config:setting:: plugins-msteamssyncenforceconnectedaccounts
  :displayname: Enforce connected accounts (Plugins - MS Teams Sync)
  :systemconsole: Plugins > MS Teams Sync
  :configjson: N/A
  :environment: N/A

  - **true**: Users are required to connect their Mattermost and Microsoft Teams accounts.
  - **false**: Users aren't required to connect their Mattermost and Microsoft Teams accounts.

Enforce connected accounts
~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+---------------------------------------------------+
| Requires all users to connect their Mattermost account to their        | - System Config path: **Plugins > MS Teams Sync** |
| Microsoft Teams account, if the accounts aren't already connected.     | - ``config.json`` setting: N/A                    |
|                                                                        | - Environment variable: N/A                       |
| - **true**: Users are required to connect their Mattermost and         |                                                   |
|   Microsoft Teams accounts each time they refresh the Mattermost       |                                                   |
|   browser, refresh the desktop app, or log in to Mattermost.           |                                                   |
| - **false**: **(Default)** Users aren't required to connect their      |                                                   |
|   Mattermost and Microsoft Teams accounts.                             |                                                   |
+------------------------------------------------------------------------+---------------------------------------------------+

.. config:setting:: plugins-msteamssyncallowtempskipconnectuser
  :displayname: Allow to temporarily skip connect user (Plugins - MS Teams Sync)
  :systemconsole: Plugins > MS Teams Sync
  :configjson: N/A
  :environment: N/A

  - **true**: Enables users to skip the current prompt to connect their Mattermost and Microsoft Teams user accounts.
  - **false**: Prevents users from skipping the prompt to connect their Mattermost and Microsoft Teams user accounts.

Allow to temporarily skip connect user
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+---------------------------------------------------+
| Allow users to temporarily dismiss the prompt to connect their         | - System Config path: **Plugins > MS Teams Sync** |
| Mattermost account to their Microsoft Teams account. Users will        | - ``config.json`` setting: N/A                    |
| continue to be prompted when they refresh the browser, refresh the     | - Environment variable: N/A                       |
| desktop app, or log in to Mattermost.                                  |                                                   |
|                                                                        |                                                   |
| - **true**: Enables users to skip the current prompt to connect their  |                                                   |
|   Mattermost and Microsoft Teams user accounts.                        |                                                   |
| - **false**: **(Default)** Prevents users from skipping the prompt to  |                                                   |
|   connect their Mattermost and Microsoft Teams accounts.               |                                                   |
+------------------------------------------------------------------------+---------------------------------------------------+

.. config:setting:: plugins-msteamssyncsyncusers
  :displayname: Sync users (Plugins - MS Teams Sync)
  :systemconsole: Plugins > MS Teams Sync
  :configjson: N/A
  :environment: N/A
  :description: Specify how often, in minutes, to synchronize direct messages, group messages, and chats, between Mattermost and Microsoft Teams users. Leave blank to disable user synchronization.

Sync users
~~~~~~~~~~

+------------------------------------------------------------------------+---------------------------------------------------+
| Specify how often, in minutes, to synchronize direct messages,         | - System Config path: **Plugins > MS Teams Sync** |
| group messages, and chats, between Mattermost and Microsoft Teams      | - ``config.json`` setting: N/A                    |
| users.                                                                 | - Environment variable: N/A                       |
|                                                                        |                                                   |
| Leave this value blank to disble user synchronization.                 |                                                   |
| Numerical value.                                                       |                                                   |
+------------------------------------------------------------------------+---------------------------------------------------+

.. config:setting:: plugins-msteamssyncguestusers
  :displayname: Sync guest users (Plugins - MS Teams Connect)
  :systemconsole: Plugins > MS Teams Connect
  :configjson: N/A
  :environment: N/A

  - **true**: Mattermost includes Microsoft Teams guest users when synchronizing.
  - **false**: Mattermost doesn't include Microsoft Teams guest users when synchronizing.

Sync guest users
~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+------------------------------------------------------+
| Synchronize Microsoft Teams guest users and Mattermost users.          | - System Config path: **Plugins > MS Teams Connect** |
|                                                                        | - ``config.json`` setting: N/A                       |
| - **true**: Mattermost includes Microsoft Teams guest users when       | - Environment variable: N/A                          |
|   synchronizing.                                                       |                                                      |
| - **false**: **(Default)** Mattermost doesn't include Microsoft Teams  |                                                      |
|   guest users when synchronizing.                                      |                                                      |
+------------------------------------------------------------------------+------------------------------------------------------+

Sync direct and group messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+----------------------------------------------------+
| Synchronize direct messages, group messages, and chats between         | - System Config path: **Plugins > MS Teams Sync**  |
| Mattermost and Microsoft Teams users.                                  | - ``config.json`` setting: N/A                     |
|                                                                        | - Environment variable: N/A                        |
| - **true**: **(Default)** Mattermost synchronizes direct messages,     |                                                    |
|   group messages, and chats between Mattermost and Microsoft Teams.    |                                                    |
| - **false**: Mattermost doesn't synchronize messages and chats.        |                                                    |
+------------------------------------------------------------------------+----------------------------------------------------+

.. config:setting:: plugins-msteamssyncenabledteams
  :displayname: Enabled teams (Plugins - MS Teams Sync)
  :systemconsole: Plugins > MS Teams Sync
  :configjson: N/A
  :environment: N/A
  :description: Specify which Mattermost teams synchronize direct messages, group messages, and chats with Microsoft Teams.

Enabled teams
~~~~~~~~~~~~~

+------------------------------------------------------------------------+----------------------------------------------------+
| Specify which Mattermost teams synchronize direct messages, group      | - System Config path: **Plugins > MS Teams Sync**  |
| messages, and chats with Microsoft Teams.                              | - ``config.json`` setting: N/A                     |
|                                                                        | - Environment variable: N/A                        |
| Separate multiple team names with commas. Leave this value blank to    |                                                    |
| synchronize all Mattermost teams.                                      |                                                    |
+------------------------------------------------------------------------+----------------------------------------------------+

.. config:setting:: plugins-msteamssyncpromptinterval
  :displayname: Sync users (Plugins - MS Teams Connect)
  :systemconsole: Plugins > MS Teams Connect
  :configjson: N/A
  :environment: N/A
  :description: Specify how often, in hours, to prompt users to connect their Microsoft Teams user account to their Mattermost user account.

Prompt interval for DMs and GMs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+------------------------------------------------------+
| Specify how often, in hours, to prompt users to connect their          | - System Config path: **Plugins > MS Teams Connect** |
| Microsoft Teams user account to their Mattermost user account.         | - ``config.json`` setting: N/A                       |
|                                                                        | - Environment variable: N/A                          |
| Leave this value blank to disble the prompt.                           |                                                      |
| Numerical value.                                                       |                                                      |
+------------------------------------------------------------------------+------------------------------------------------------+

.. config:setting:: plugins-msteamssyncmaxsizeattachments
  :displayname: Maximum size of attachments to support complete one time download (Plugins - MS Teams Connect)
  :systemconsole: Plugins > MS Teams Connect
  :configjson: N/A
  :environment: N/A
  :description: Specify the maximum file size, in megabytes (MB), of attachments that can be loaded into memory. Attachment files larger than this value will be streamed from Microsoft Teams to Mattermost.

Maximum size of attachments to support complete one time download
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+----------------------------------------------------------+
| Specify the maximum file size, in megabytes (MB), of attachments   | - System Config path: **Plugins > MS Teams Connect**     |
| that can be loaded into memory. Attachment files larger than       | - ``config.json`` setting: N/A                           |
| this value will be streamed from Microsoft Teams to Mattermost.    | - Environment variable: N/A                              |
|                                                                    |                                                          |
| Numerical value. Default is **20** MB.                             |                                                          |
+--------------------------------------------------------------------+----------------------------------------------------------+

.. config:setting:: plugins-msteamssyncbuffer
  :displayname: Buffer size for streaming files (Plugins - MS Teams Connect)
  :systemconsole: Plugins > MS Teams Connect
  :configjson: N/A
  :environment: N/A
  :description: Specify the buffer size, in megabytes (MB), for streaming attachment files from Microsoft Teams to Mattermost.

Buffer size for streaming files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+----------------------------------------------------------+
| Specify the buffer size, in megabytes (MB), for streaming          | - System Config path: **Plugins > MS Teams Connect**     |
| attachment files from Microsoft Teams to Mattermost.               | - ``config.json`` setting: N/A                           |
|                                                                    | - Environment variable: N/A                              |
| Numerical value. Default is **20** MB.                             |                                                          |
+--------------------------------------------------------------------+----------------------------------------------------------+

----

Playbooks
----------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Mattermost Playbooks is an open source, self-hosted collaboration tool for teams. Each playbook represents a recurring outcome or specific goal that your teams collaborate on to achieve, such as service outage recovery or customer onboarding. Teams run a playbook every time they want to orchestrate people, tools, and data to achieve that outcome as quickly as possible while providing visibility to stakeholders. Playbooks also allow teams to incorporate learnings from the retrospective to tweak and improve the playbook with every iteration. See the `Mattermost Playbooks plugin </guides/repeatable-processes.html>`__ documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Playbooks**.

.. config:setting:: plugins-playbooksenable
  :displayname: Enable plugin (Plugins - Playbooks)
  :systemconsole: Plugins > Playbooks
  :configjson: 
  :environment: 

  - **true**: **(Default)** Enables Mattermost Playbooks on your Mattermost workspace.
  - **false**: Disables Mattermost Playbooks on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------+-----------------------------------------------+
| - **true**: **(Default)** Enables Mattermost Playbooks on your Mattermost workspace.              | - System Config path: **Plugins > Playbooks** |
| - **false**: Disables Mattermost Playbooks on your Mattermost workspace.                          | - ``config.json`` setting:                    |
|                                                                                                   | - Environment variable:                       |
+---------------------------------------------------------------------------------------------------+-----------------------------------------------+

.. config:setting:: plugins-playbooksenabledteams
  :displayname: Enabled teams (Plugins - Playbooks)
  :systemconsole: Plugins > Playbooks
  :configjson: 
  :environment: 
  :description: Enable Playbooks for all Mattermost teams, or for only selected teams.

Enabled teams
~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------+-----------------------------------------------+
| Enable Playbooks for all Mattermost teams, or for only selected teams.            | - System Config path: **Plugins > Playbooks** |
|                                                                                   | - ``config.json`` setting:                    |
|                                                                                   | - Environment variable:                       |
+-----------------------------------------------------------------------------------+-----------------------------------------------+

.. config:setting:: plugins-playbooksexperimentalfeatures
  :displayname: Enable experimental features (Plugins - Playbooks)
  :systemconsole: Plugins > Playbooks
  :configjson: 
  :environment: 

  - **true**: Enables experimental Playbooks features on your Mattermost workspace.
  - **false**: Disables experimental Playbooks features on your Mattermost workspace.

Enable experimental features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------+-----------------------------------------------+
| - **true**: Enables experimental Playbooks features on your Mattermost workspace.          | - System Config path: **Plugins > Playbooks** |
| - **false**: Disables experimental Playbooks features on your Mattermost workspace.        | - ``config.json`` setting:                    |
|                                                                                            | - Environment variable:                       |
+--------------------------------------------------------------------------------------------+-----------------------------------------------+

User satisfaction surveys
-------------------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

This plugin enables Mattermost to send user satisfaction surveys to gather feedback and improve product quality directly from your Mattermost users. Please refer to the `Mattermost Privacy Policy <https://mattermost.com/privacy-policy/>`__ for more information on the collection and use of information received through Mattermost services.

Access the following configuration settings in the System Console by going to **Plugins > User Satisfaction Surveys**.

.. config:setting:: plugins-surveysenable
  :displayname: Enable plugin (Plugins - User Satisfaction Surveys)
  :systemconsole: Plugins > User Satisfaction Surveys
  :configjson: N/A
  :environment: N/A

  - **true**: (Default) Enables the Mattermost User Satisfaction Surveys plugin on your Mattermost workspace.
  - **false**: Disables the Mattermost User Satisfaction Surveys plugin on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| - **true**: (Default) Enables the Mattermost User Satisfaction Surveys plugin on your Mattermost workspace.   | - System Config path: **Plugins > User Satisfaction Surveys** |
| - **false**: Disables the Mattermost User Satisfaction Surveys plugin on your Mattermost workspace.           |                                                               |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

.. config:setting:: plugins-surveysenablesend
  :displayname: Enable user satisfaction survey (Plugins - User Satisfaction Surveys)
  :systemconsole: Plugins > User Satisfaction Surveys
  :configjson: N/A
  :environment: N/A

  - **true**: A user satisfaction survey is sent to all users every quarter.
  - **false**: (Default) User satisfaction surveys are disabled.

Enable user satisfaction survey
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| - **true**: A survey is sent to all users every quarter. Results are used by Mattermost, Inc. to improve the product.       | - System Config path: **Plugins > User Satisfaction Surveys** |
| - **false**: (Default) User satisfaction surveys are disabled.                                                              |                                                               |
+-----------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| **Note**: See the `Mattermost Privacy Policy <https://mattermost.com/privacy-policy/>`__ for more information on the collection and use of information by Mattermost.                       |
+-----------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

----

Zoom
----

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This plugin allows team members to initiate a Zoom meeting with a single click. All participants in a channel can easily join the Zoom meeting and the shared link is updated when the meeting is over. See the `Zoom Plugin <https://github.com/mattermost/mattermost-plugin-zoom/blob/master/README.md#installation>`__ documentation for details.

.. note::

  To set up this plugin, you need to create a Zoom App using a Zoom Administrator account. See the `Zoom plugin <https://github.com/mattermost/mattermost-plugin-zoom/blob/master/README.md>`__ documentation for details. 

Access the following configuration settings in the System Console by going to **Plugins > Zoom**.

.. config:setting:: plugins-zoomenable
  :displayname: Enable plugin (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A

  - **true**: (Default) Enables the Zoom plugin on your Mattermost server.
  - **false**: Disables the Zoom plugin on your Mattermost server.

Enable plugin
~~~~~~~~~~~~~

+----------------------------------------------------------------------------+------------------------------------------+
| - **true**: (Default) Enables the Zoom plugin on your Mattermost server.   | - System Config path: **Plugins > Zoom** |
| - **false**: Disables the Zoom plugin on your Mattermost server.           |                                          |
+----------------------------------------------------------------------------+------------------------------------------+

.. config:setting:: plugins-zoomurl
  :displayname: Zoom URL (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A
  :description: Specify the URL for a self-hosted private cloud or on-premise Zoom server. Leave blank if you're using Zoom's vendor-hosted SaaS service.

Zoom URL
~~~~~~~~

+----------------------------------------------------------------------------+------------------------------------------+
| Specify the URL for a self-hosted private cloud or on-premise Zoom server. | - System Config path: **Plugins > Zoom** |
| For example, **https://yourzoom.com**.                                     |                                          |
| Leave blank if you're using Zoom's vendor-hosted SaaS service.             |                                          |
+----------------------------------------------------------------------------+------------------------------------------+

.. config:setting:: plugins-zoomapiurl
  :displayname: Zoom API URL (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A
  :description: Specify the API URL for a self-hosted private cloud or on-premise Zoom server. Leave blank if you're using Zoom's vendor-hosted SaaS service.

Zoom API URL
~~~~~~~~~~~~

+---------------------------------------------------------------------------------+------------------------------------------+
| Specify the API URL for a self-hosted private cloud or on-premises Zoom server. | - System Config path: **Plugins > Zoom** |
| For example, **https://api.yourzoom.com/v2**.                                   |                                          |
| Leave blank if you're using Zoom's vendor-hosted SaaS service.                  |                                          |
+---------------------------------------------------------------------------------+------------------------------------------+

.. config:setting:: plugins-zoomoauth
  :displayname: Enable OAuth (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A

  - **true**: OAuth will be used as the authentication means with Zoom.
  - **false**: (Default) JWT will be used as the authentication means with Zoom.

Enable OAuth
~~~~~~~~~~~~

+---------------------------------------------------------------------------------+------------------------------------------+
| - **true**: OAuth will be used as the authentication means with Zoom.           | - System Config path: **Plugins > Zoom** |
| - **false**: (Default) JWT will be used as the authentication means with Zoom.  |                                          |
+---------------------------------------------------------------------------------+------------------------------------------+

.. note::

  If you are currently using a JWT Zoom application and switch to OAuth, all users will need to connect their Zoom account using OAuth the next time they try to start a meeting. See the `Zoom plugin <https://github.com/mattermost/mattermost-plugin-zoom#readme>`__ documentation for details.

.. config:setting:: plugins-zoomoauthbyaccountlevel
  :displayname: OAuth by account level app (Beta) (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: 
  :environment:

  - **true**: Only an account administrator must log in. The rest of the users will use their e-mail to log in.
  - **false**: (Default) All users must use their e-mail to log in.

OAuth by account level app (Beta)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------+------------------------------------------+
| - **true**: Only an account administrator must log in. The rest of the users will use their e-mail to log in. | - System Config path: **Plugins > Zoom** |
| - **false**: (Default) All users must use their e-mail to log in.                                             |                                          |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------+

.. config:setting:: plugins-zoomoauthclientid
  :displayname: Zoom OAuth client ID (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A
  :description: Specify the Client ID for the OAuth app registered with Zoom. Leave blank if not using OAuth.

Zoom OAuth client ID
~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------+------------------------------------------+
| Specify the Client ID for the OAuth app registered with Zoom. Leave blank if not using OAuth. | - System Config path: **Plugins > Zoom** |
|                                                                                               |                                          |
|                                                                                               |                                          |
+-----------------------------------------------------------------------------------------------+------------------------------------------+

.. config:setting:: plugins-zoomoauthclientsecret
  :displayname: Zoom OAuth client secret (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A
  :description: Specify the Client Secret for the OAuth app registered with Zoom. Leave blank if not using OAuth.

Zoom OAuth client secret
~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------+------------------------------------------+
| Specify the Client Secret for the OAuth app registered with Zoom. Leave blank if not using OAuth. | - System Config path: **Plugins > Zoom** |
+---------------------------------------------------------------------------------------------------+------------------------------------------+

.. config:setting:: plugins-zoomatresttokenencryptionkey 
  :displayname: At rest token encryption key (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A
  :description: Generate an AES encryption key for the Zoom OAuth Token used to encrypt stored access tokens by selecting **Regenerate**. 

At rest token encryption key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------+
| Generate an AES encryption key for the Zoom OAuth Token used to encrypt stored access tokens by selecting **Regenerate**. | - System Config path: **Plugins > Zoom** |
| Regenerating the key invalidates your existing Zoom OAuth.                                                                |                                          |
+---------------------------------------------------------------------------------------------------------------------------+------------------------------------------+

.. config:setting:: plugins-zoomapikey
  :displayname: API key (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: 
  :environment:
  :description: Specify the API Key generated by Zoom used to create meetings and pull user data.

API key
~~~~~~~

+-----------------------------------------------------------------------------------+------------------------------------------+
| Specify the API Key generated by Zoom used to create meetings and pull user data. | - System Config path: **Plugins > Zoom** |
+-----------------------------------------------------------------------------------+------------------------------------------+

.. config:setting:: plugins-zoomapisecret
  :displayname: API secret (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A
  :description: Specify the API Secret generated by Zoom for your API key.

API secret
~~~~~~~~~~

+------------------------------------------------------------+------------------------------------------+
| Specify the API Secret generated by Zoom for your API key. | - System Config path: **Plugins > Zoom** |
+------------------------------------------------------------+------------------------------------------+

.. config:setting:: plugins-zoomwebhooksecret
  :displayname: API secret (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A
  :description: Generate a secret for the webhook URL endpoint used to authenticate the webhook to Mattermost.

Webhook secret
~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------+------------------------------------------+
| Generate a secret for the webhook URL endpoint used to authenticate the webhook to Mattermost. | - System Config path: **Plugins > Zoom** |
| Regenerating the secret invalidates your existing Zoom plugin.                                 |                                          |
+------------------------------------------------------------------------------------------------+------------------------------------------+

.. config:setting:: plugins-zoomsigpublickeyfile
  :displayname: Signature public key file (Plugins - Zoom)
  :systemconsole: N/A
  :configjson: SignaturePublicKeyFiles
  :environment: N/A
  :description: In addition to the Mattermost plugin signing key built into the server, each public key specified is trusted to validate plugin signatures.

Signature public key files
~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

In addition to the Mattermost plugin signing key built into the server, each public key specified here is trusted to validate plugin signatures.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SignaturePublicKeyFiles": {}`` with string array input consisting of contents that are relative or absolute paths to signature files.              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-zoomchimeraoauthproxyurl
  :displayname: Chimera OAuth proxy URL (Plugins - Zoom)
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
