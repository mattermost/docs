Plugins configuration settings
==============================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Self-hosted can manage the following configuration settings in **System Console > Plugins** or by editing the ``config.json`` file as described in the following tables. 

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

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| - **true**: **(Default)** Enables plugin signature validation for managed and unmanaged plugins.                                                                                      | - System Config path: **Plugins > Plugin Management**                        |
| - **false**: Disables plugin signature validation for managed and unmanaged plugins.                                                                                                  | -  ``config.json`` setting: ``.PluginSettings.RequirePluginSignature: true`` |
|                                                                                                                                                                                       | - Environment variable: ``MM_PLUGINSETTINGS_REQUIREPLUGINSIGNATURE``         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| **Notes**:                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                      |
| - Pre-packaged plugins are not subject to signature validation. Plugins installed through the Marketplace are always subject to signature validation at the time of download.                                                                                        |
| - Enabling this configuration will result in `plugin file uploads <#upload-plugin>`__ being disabled in the System Console.                                                                                                                                          |
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

.. config:setting:: plugins-upload
  :displayname: Upload Plugin (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: EnableUploads
  :environment: MM_PLUGINSETTINGS_ENABLEUPLOADS

  - **true**: Enables system admins to upload plugins from the local computer to the Mattermost server.
  - **false**: **(Default)** Disables uploading of plugins from the local computer to the Mattermost server.

Upload Plugin
~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| - **true**:  Enables you to upload plugins from the local computer to the Mattermost server.                                       | - System Config path: **Plugins > Plugin Management**                  |
| - **false**: **(Default)** Disables uploading of plugins from the local computer to the Mattermost server.                         | - ``config.json`` setting: ``.PluginSettings.EnableUploads: false``    |
|                                                                                                                                    | - Environment variable: ``MM_PLUGINSETTINGS_ENABLEUPLOADS``            |
+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| **Notes**:                                                                                                                                                                                                  |
|                                                                                                                                                                                                             |
| - When plugin uploads are enabled, the error ``Received invlaid response from the server`` when uploading a plugin file typically indicates that the                                                        |
|   :ref:`MaxFileSize <configure/environment-configuration-settings:maximum file size>` configuration setting isn't large enough to support the plugin file upload. Additional proxy setting updateds         |
|   may also be required.                                                                                                                                                                                     |
| - The ability to upload plugin files is disabled when the `Require plugin signature <#require-plugin-signature>`__ configuration setting is enabled.                                                        |
+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. config:setting:: plugins-enablemarketplace
  :displayname: Enable marketplace (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: .PluginSettings.EnableMarketplace
  :environment: MM_PLUGINSETTINGS_ENABLEMARKETPLACE

  - **true**: **(Default)** Enables the plugin Marketplace on your Mattermost server for all system admins.
  - **false**: Disables the plugin Marketplace on your Mattermost server for all system admins.

Enable Marketplace
~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| - **true**: **(Default)** Enables the plugin Marketplace on your Mattermost server for all system admins. | - System Config path: **Plugins > Plugin Management**                  |
| - **false**: Disables the plugin Marketplace on your Mattermost server for all system admins.             | - ``config.json`` setting: ``.PluginSettings.EnableMarketplace: true`` |
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

  - **true**: **(Default)** Enables the calls plugin on your Mattermost workspace.
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
| - **false**: Only system admins can enable or disable calls on specific channels.                                                      | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.allowenablecalls``                |
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

*This setting was called Enable on all channels until Mattermost v7.7. It was renamed to defaultenabled in code and Test Mode in-product.*

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| - **false**: Test mode is enabled and only system admins can start calls in channels.                           | - System Config path: **Plugins > Calls**                                                   |
| - **true**: Live mode is enabled and all team members can start calls in channels.                              | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.defaultenabled``   |
|                                                                                                                 | - Environment variable: N/A                                                                 |
+-----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+

.. note::
  Use this setting as a system admin to confirm calls work as expected. When **false**, users attempting to start calls are prompted to contact a system admin, and system admins are prompted to confirm that calls are working as expected before switching to live mode.

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

.. |ice_host_override_link| replace:: :ref:`ICE Host Override <configure/plugins-configuration-settings:ice host override>`

.. config:setting:: plugins-callsicehostportoverride
  :displayname: ICE host port override (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.icehostportoverride
  :environment: N/A
  :description: An optional port number to be used as an override for host candidates in place of the one used to listen on.

ICE host port override
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| This setting can be used to override the port used in the ICE host candidates that get advertised to clients when connecting to calls.                              | - System Config path: **Plugins > Calls**                                                              |
|                                                                                                                                                                     | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.icehostportoverride``         |
|                                                                                                                                                                     | - Environment variable: N/A                                                                            |
| This can be useful in case there are additional network components (e.g. NLBs) in front of the RTC server that may route the calls traffic through a different port.|                                                                                                        |
| Changing this setting requires a plugin restart to take effect.                                                                                                     |                                                                                                        |
|                                                                                                                                                                     |                                                                                                        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| **Note**: this value will apply to both UDP and TCP host candidates.                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsrtcdserviceurl
  :displayname: RTCD service URL (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.rtcdserviceurl
  :environment: MM_CALLS_RTCD_URL
  :description: The URL to a running rtcd service instance that will host the calls. When set (non empty) all the calls will be handled by this external service.

RTCD service URL
~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| The URL to a running `rtcd <https://github.com/mattermost/rtcd>`__ service instance that will host the calls. | - System Config path: **Plugins > Calls**                                                                                                                 |
|                                                                                                               | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.rtcdserviceurl``                                                                 |
|                                                                                                               | - Environment variable: ``MM_CALLS_RTCD_URL``                                                                                                             |
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
  :environment: MM_CALLS_MAX_PARTICIPANTS
  :description: The maximum number of participants that can join a single call. Default value is **0** (unlimited). The maximum recommended setting is 50.

Max call participants
~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| This setting limits the number of participants that can join a single call. | - System Config path: **Plugins > Calls**                                                                     |
|                                                                             | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.maxcallparticipants``                |
|                                                                             | - Environment variable: ``MM_CALLS_MAX_PARTICIPANTS``                                                         |
| Default is **0** (no limit).                                                |                                                                                                               |
+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| **Note**: This setting is optional, but the recommended maximum number of participants is **50**. Call participant limits greatly depends on instance resources.                            | 
| See the :doc:`Calls self-hosted deployment </configure/calls-deployment>` documentation for details.                                                                                        |
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

.. |rtcd_service| replace:: :ref:`rtcd service <configure/calls-deployment:the rtcd service>`

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

+---------------------------------------------------------------------------------------------------------------------------------------+
| **Note**: To get TURN generated credentials to work you must provide a secret through the *TURN static auth secret* setting below.    |
+---------------------------------------------------------------------------------------------------------------------------------------+

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
| This is an optional field.                                                 | - Environment variable: N/A                                                                                    |
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
  :displayname: (Experimental) Enable simulcast for screen sharing (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enablesimulcast
  :environment: N/A
  
  - **true**: Enables simulcast for screen sharing. This can help to improve screen sharing quality.
  - **false**: (Default) Disables simulcast for screen sharing.

Enable simulcast for screen sharing (Experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| - **true**: Enables simulcast for screen sharing. This can help to improve screen sharing quality.                     | - System Config path: **Plugins > Calls**                                                                |
| - **false**: Disables simulcast for screen sharing.                                                                    | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.enablesimulcast``               |
|                                                                                                                        | - Environment variable: N/A                                                                              |
+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **Note**: This functionality has the following requirements:                                                                                                                                                                      |
| - Calls plugin version >= v0.16.0                                                                                                                                                                                                 |
| - ``rtcd`` version >= v0.10.0 (if in use)                                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-enablecallrecordings
  :displayname: Enable call recordings (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enablerecordings
  :environment: N/A

  - **true**: Allows call hosts to record meeting video and audio.
  - **false**: (Default) Call recording functionality is not available to hosts.

Enable call recordings
~~~~~~~~~~~~~~~~~~~~~~

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
  :environment: MM_CALLS_JOB_SERVICE_URL
  :description: The URL to a running job service where all the processing related to recordings happens. This is a required field. Changing this setting requires a plugin restart to take effect.
  
Job service URL
~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| The URL to a running job service where all the processing related to recordings happens. The recorded files produced are stored in Mattermost. | - System Config path: **Plugins > Calls**                                                            |
|                                                                                                                                                | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.jobserviceurl``             |
| This is a required field. Changing this setting requires a plugin restart to take effect.                                                      | - Environment variable: ``MM_CALLS_JOB_SERVICE_URL``                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| **Note**:                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                       |
| - The client will self-register the first time it connects to the service and store the authentication key in the database. If no client ID is explicitly provided, the diagnostic ID of the Mattermost installation will be used.                    |
| - The service URL supports credentials in the form ``http://clientID:authKey@hostname``. Alternatively these can be passed through environment overrides to the Mattermost server, namely ``MM_CALLS_JOB_SERVICE_CLIENT_ID``                          |
|   and ``MM_CALLS_JOB_SERVICE_AUTH_KEY``.                                                                                                                                                                                                              |
| - As of Calls v0.25 it's possible to override the site URL used by jobs to connect by setting the ``MM_CALLS_RECORDER_SITE_URL`` or ``MM_CALLS_TRANSCRIBER_SITE_URL`` environment variables respectively. This can be helpful to avoid the jobs       |
|   from connecting through the public Site URL configured in Mattermost and thus potentially bypass the public network.                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

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
| **Note**: The quality setting will affect the performance of the job service and the file size of recordings. Refer to the :ref:`deployment section <configure/calls-deployment:configure recording, transcriptions, and live captions>` for more information.                               |
+-----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-enablecalltranscriptions
  :displayname: Enable call transcriptions (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enabletranscriptions
  :environment: N/A
  
  - **true**: Enables automatic transcriptions of calls.
  - **false**: (Default) Call transcriptions functionality is disabled.

Enable call transcriptions (Beta)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| - **true**: Enables automatic transcriptions of calls.                                                                                                                                                                                                             | - System Config path: **Plugins > Calls**                                                                  |
| - **false**: **(Default)** Call transcriptions functionality is disabled.                                                                                                                                                                                          | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.enabletranscriptions``            |
|                                                                                                                                                                                                                                                                    |                                                                                                            |
| Transcriptions are generated from the call participants' audio tracks and the resulting files are attached to the call thread when the recording ends. Captions will be optionally rendered on top of the recording file video player.                             |                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| **Note**: Call transcriptions require :ref:`call recordings <configure/plugins-configuration-settings:enable call recordings>` to be enabled. This setting is available starting in plugin version 0.22.                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-transcribermodelsize
  :displayname: Call transcriber model size (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.transcribermodelsize
  :environment: N/A
  :description: The speech-to-text model size to use. Heavier models will produce more accurate results at the expense of processing time and resources usage.

Transcriber model size
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| The speech-to-text model size to use. Heavier models will produce more accurate results at the expense of processing time and resources usage. Available options are: *Tiny*, *Base* and *Small*.                                                                                  | - System Config path: **Plugins > Calls**                                                           |
|                                                                                                                                                                                                                                                                                    | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.transcribermodelsize``     |
| The default is **Base**. This is a required value.                                                                                                                                                                                                                                 |                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| **Note**: The model size setting will affect the performance of the job service. Refer to the :ref:`configure call recordings, transcriptions, and live captions <configure/calls-deployment:configure recording, transcriptions, and live captions>` documentation for more information.                                                                                                |
| This setting is available starting in plugin version 0.22.                                                                                                                                                                                                                                                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-transcribernumthreads
  :displayname: Call transcriber threads (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.transcribernumthreads
  :environment: N/A
  :description: The number of threads used by the post-call transcriber. Default is 2. This is a required value that must be in the range [1, numCPUs].

Call transcriber threads
~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| The number of threads used by the post-call transcriber. This must be in the range [1, numCPUs].                                                                                                                                                                                                                                     | - System Config path: **Plugins > Calls**                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                      | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.transcribernumthread``                                                                |
| The default is 2. This is a required value.                                                                                                                                                                                                                                                                                          |                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Note**: The call transcriber threads setting will affect the performance of the job service. Refer to the :ref:`configure call recordings, transcriptions, and live captions <configure/calls-deployment:configure recording, transcriptions, and live captions>` documentation for more information. This setting is available starting in plugin version 0.26.2.                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-enablelivecaptions
  :displayname: (Experimental) Enable live captions (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enablelivecaptions
  :environment: N/A
  :description: Enables live captioning of calls.

  - **true**: Enables live captioning of calls.
  - **false**: **(Default)** Live captions functionality is disabled.

Enable live captions (Beta)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| - **true**: Enables live captioning of calls.                             | - System Config path: **Plugins > Calls**                                                      |
| - **false**: **(Default)** Live captions functionality is disabled.       | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.enablelivecaptions``  |
|                                                                           |                                                                                                |
| Live captions are generated from the call participants' audio tracks      |                                                                                                |
| and the resulting captions can be optionally displayed on the call        |                                                                                                |
| clients by clicking the `[cc]` button.                                    |                                                                                                |
+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| **Note**: Live captions require :ref:`call recordings <configure/plugins-configuration-settings:enable call recordings>` and                                               |
| :ref:`call transcriptions <configure/plugins-configuration-settings:enable call transcriptions (beta)>` to be enabled.                                                     |
| This setting is available starting in plugin version 0.26.2.                                                                                                               |
+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-livecaptionsmodelsize
  :displayname: Live captions: Model size (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.livecaptionsmodelsize
  :environment: N/A
  :description: The speech-to-text model size to use for live captions. Heavier models will produce more accurate results at the expense of processing time and resources usage. Default is **Tiny**. This is a required value. 

Live captions: Model size
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| The speech-to-text model size to use for live captions. While heavier models can produce more accurate results, live captioning requires the transcriber to process up to ten seconds of audio within two seconds. Therefore a maximum of size `base` is recommended. Available options are: *Tiny*, *Base* and *Small*. | - System Config path: **Plugins > Calls**                                                         |
|                                                                                                                                                                                                                                                                                                                          | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.livecaptionsmodelsize``  |
| The default is **Tiny**. This is a required value.                                                                                                                                                                                                                                                                       |                                                                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| **Note**: The model size setting will affect the performance of the job service. Refer to the `performance and scalability recommendations <https://github.com/mattermost/calls-offloader/blob/master/docs/performance.md>`_ documentation for more information. This setting is available starting in plugin version 0.26.2.                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-livecaptionsnumtranscribers
  :displayname: Live captions: Number of transcribers used per call (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.livecaptionsnumtranscribers
  :environment: N/A
  :description: The number of separate live captions transcribers for each call. Each transcribes one audio stream at a time. Default is 1. This is a required value. The product of LiveCaptionsNumTranscribers * LiveCaptionsNumThreadsPerTranscriber must be in the range [1, numCPUs].

Live captions: Number of transcribers used per call
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| The number of separate live captions transcribers for each call. Each transcribes one audio stream at a time. The product of LiveCaptionsNumTranscribers * LiveCaptionsNumThreadsPerTranscriber must be in the range [1, numCPUs].                                                                                       | - System Config path: **Plugins > Calls**                                                              |
|                                                                                                                                                                                                                                                                                                                          | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.livecaptionsnumtranscribers`` |
| The default is 1. This is a required value.                                                                                                                                                                                                                                                                              |                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| **Note**: The live captions number of transcribers setting will affect the performance of the job service. Refer to the `performance and scalability recommendations <https://github.com/mattermost/calls-offloader/blob/master/docs/performance.md>`_ documentation for more information. This setting is available starting in plugin version 0.26.2.                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-livecaptionsnumthreadspertranscriber
  :displayname: Live captions: Number of threads per transcriber (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.livecaptionsnumthreadspertranscriber
  :environment: N/A
  :description: The number of threads per live captions transcriber. Default is 2. This is a required value. The product of LiveCaptionsNumTranscribers * LiveCaptionsNumThreadsPerTranscriber must be in the range [1, numCPUs].

Live captions: Number of threads per transcriber
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| The number of threads per live-captions transcriber. The product of ``LiveCaptionsNumTranscribers`` * ``LiveCaptionsNumThreadsPerTranscriber`` must be in the range [1, numCPUs].                                                                                                                                        | - System Config path: **Plugins > Calls**                                                                       |
|                                                                                                                                                                                                                                                                                                                          | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.livecaptionsnumthreadspertranscriber`` |
| The default is 2. This is a required value.                                                                                                                                                                                                                                                                              |                                                                                                                 |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **Note**: The live captions number of threads per transcriber setting will affect the performance of the job service. Refer to the `performance and scalability recommendations <https://github.com/mattermost/calls-offloader/blob/master/docs/performance.md>`_ documentation for more information. This setting is available starting in plugin version 0.26.2.                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-livecaptionslanguage
  :displayname: Live captions language (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.livecaptionslanguage
  :environment: N/A
  :description: The language passed to the live captions transcriber. Should be a 2-letter ISO 639 Set 1 language code, e.g. 'en'. If blank, the lange will be set to 'en' (English) as default. 

Live captions language
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| The language passed to the live captions transcriber. Should be a 2-letter ISO 639 Set 1 language code, e.g. 'en'.  | - System Config path: **Plugins > Calls**                                                                       |
|                                                                                                                     | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.livecaptionslanguage``                 |
| If blank, the lange will be set to 'en' (English) as default.                                                       |                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsenableipv6
  :displayname: (Experimental) Enable IPv6 (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enableipv6
  :environment: N/A

  - **true**: The RTC service will work in dual-stack mode, listening for IPv6 connections and generating candidates in addition to IPv4 ones.
  - **false**: (False) The RTC service will only listen for IPv4 connections.

(Experimental) Enable IPv6
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| - **true**: The RTC service will work in dual-stack mode, listening for IPv6 connections and generating candidates in addition to IPv4 ones. | - System Config path: **Plugins > Calls**                                                                |
| - **false**: **(Default)** The RTC service will only listen for IPv4 connections.                                                            | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.enableipv6``                    |
|                                                                                                                                              | - Environment variable: N/A                                                                              |
| Changing this setting requires a plugin restart to take effect.                                                                              |                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| **Note**:                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                         |
| - This setting is only applicable when not running calls through the standalone ``rtcd`` service.                                                                                                                                                       |
| - This setting is available starting in plugin version 0.17.                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-enablecallringing
  :displayname: Enable call ringing (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enableringing
  :environment: N/A

  - **true**: Ringing functionality is enabled. Direct and group message participants receive a desktop app alert and a ringing notification when a call starts.
  - **false**: **(False)** Ringing functionality is disabled.

Enable call ringing
~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| - **true**: Ringing functionality is enabled. Direct and group message   | - System Config path: **Plugins > Calls**                                                   |
|   participants receive a desktop app alert and a ringing notification    | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls. enableringing``   |
|   when a call starts.                                                    | - Environment variable: N/A                                                                 |
| - **false**: **(Default**) Ringing functionality is disabled.            |                                                                                             |
+--------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+

.. config:setting:: plugins-enableav1
  :displayname: Enable AV1 codec for screen sharing (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enableav1
  :environment: N/A

  - **true**: Enables the ability to use the AV1 codec to encode screen sharing tracks. This can result in improved screen sharing quality for clients that support it.
  - **false**: **(False)** AV1 codec is disabled for screen sharing tracks.

Enable AV1 (Experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| - **true**: Enables the ability to use the AV1 codec to encode screen    | - System Config path: **Plugins > Calls**                                                   |
|   sharing tracks. Can result in improved screen sharing quality via      | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.enableav1``        |
|   clients that support AV1 encoding.                                     | - Environment variable: N/A                                                                 |
| - **false**: **(Default**) AV1 codec is disabled for screen sharing      |                                                                                             |
|   tracks.                                                                |                                                                                             |
+--------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| **Note**:  This setting is ignored when                                                                                                                                |
| :ref:`simulcast is enabled for screen sharing <configure/plugins-configuration-settings:enable simulcast for screen sharing (experimental)>`.                          |
+--------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+

.. config:setting:: plugins-enabledcsignaling
  :displayname: Use data channels for signaling media tracks (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enabledcsignaling
  :environment: N/A

  - **true**: Clients will use WebRTC data channels for signaling of media tracks (i.e., voice, screen). This can result in a more efficient and less race-prone process, especially in case of poor network connections.
  - **false**: **(False)** Clients will use WebSockets for signaling media tracks.

Enable DC signaling (Experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| - **true**: Clients will use WebRTC data channels for signaling of media   | - System Config path: **Plugins > Calls**                                                        |
|   tracks (i.e., voice, screen). This can result in a more efficient and    | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.enabledcsignaling``     |
|   less race-prone process, especially in case of poor network connections. | - Environment variable: N/A                                                                      |
| - **false**: **(Default**) Clients will use WebSockets for signaling       |                                                                                                  |
|   media tracks.                                                            |                                                                                                  |
+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| **Note**: Version v0.18.0 or higher of the |rtcd_service| is required for this functionality to work when hosting calls through the dedicated WebRTC service.                 |
+----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+

----

.. config:setting:: integrations-gitlab
  :displayname: GitLab interoperability (Plugins)
  :systemconsole: Plugins > GitHub
  :configjson: gitlab
  :environment: N/A
  :description: Connect your GitLab instance to your Mattermost instance.

GitLab
------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

See the :doc:`Connect GitLab to Mattermost </integrate/gitlab-interoperability>` product documentation for available :ref:`Mattermost configuration options <integrate/gitlab-interoperability:mattermost configuration>`.

----

.. config:setting:: integrations-github
  :displayname: GitHub interoperability (Plugins > GitHub)
  :systemconsole: Plugins > GitHub
  :configjson: github
  :environment: N/A
  :description: Connect your GitHub instance to your Mattermost instance.

GitHub
------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

See the :doc:`Connect GitHub to Mattermost </integrate/github-interoperability>` product documentation for available :ref:`Mattermost configuration options <integrate/github-interoperability:mattermost configuration>`.

----

.. config:setting:: integrations-jira
  :displayname: Jira interoperability (Plugins > Jira)
  :systemconsole: Plugins > Jira
  :configjson: jira
  :environment: N/A
  :description: Connect your Jira instance to your Mattermost instance.

Jira
----

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

See the :doc:`Connect Jira to Mattermost </integrate/jira-interoperability>` product documentation for available :ref:`Mattermost configuration options <integrate/jira-interoperability:mattermost configuration>`.

----

.. config:setting:: integrations-legalhold
  :displayname: Perform legal holds (Plugins > Legal Hold)
  :systemconsole: Plugins > Legal Hold
  :configjson: legal-hold
  :environment: N/A
  :description: Perform legal holds in Mattermost.

Legal hold
----------

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

See the :doc:`Legal holds </comply/legal-hold>` product documentation for details.

----

MS Teams
---------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Mattermost for Microsoft Teams enables you to break through siloes in a mixed Mattermost and Teams environment by forwarding real-time chat notifications from Teams to Mattermost.

Access the following configuration settings in the System Console by going to **Plugins > MS Teams**.

.. include:: ../_static/badges/academy-msteams.rst
  :start-after: :nosearch:

.. config:setting:: plugins-msteamsenable
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
| **Note**: Use the `Enabled Teams <#enabled-teams>`__ configuration option to specify which Mattermost teams synchronize     |
| direct and group messages with Microsoft Teams chats.                                                                       |
+------------------------------------------------------------------------+----------------------------------------------------+

.. config:setting:: plugins-msteamstenantid
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

.. config:setting:: plugins-msteamsclientid
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

.. config:setting:: plugins-msteamsclientsecret
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

.. config:setting:: plugins-msteamsgenerateatrestencryptionkey
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
| **Note**: Select **Regenerate** to generate a new key.                                                                     |
+------------------------------------------------------------------------+---------------------------------------------------+

.. config:setting:: plugins-msteamsgeneratewebhooksecret
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
| **Note**: Select **Regenerate** to generate a new key.                                                                     |
+------------------------------------------------------------------------+---------------------------------------------------+

.. config:setting:: plugins-msteamsuseevaluationapipaymodel
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

.. config:setting:: plugins-msteamssyncnotifications
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

.. config:setting:: plugins-msteamsmaxsizeattachments
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

.. config:setting:: plugins-msteamsbuffer
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

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

See the :doc:`Monitor performance metrics </scale/collect-performance-metrics>` product documentation for available :ref:`Mattermost configuration options <scale/collect-performance-metrics:mattermost configuration>`.

----

Collaborative playbooks
------------------------

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Use collaborative playbooks in Mattermost to provide structure, monitoring and automation for repeatable, team-based processes integrated with the Mattermost platform.

Access the following configuration settings in the System Console by going to **Plugins > Collaborative playbooks**.

.. config:setting:: plugins-playbooksenable
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

.. config:setting:: plugins-playbooksenabledteams
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

.. config:setting:: plugins-playbooksexperimentalfeatures
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

.. config:setting:: integrations-servicenow
  :displayname: ServiceNow interoperability (Plugins)
  :systemconsole: Plugins > ServiceNow
  :configjson: servicenow
  :environment: N/A
  :description: Connect your ServiceNow instance to your Mattermost instance.

ServiceNow
----------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

See the :doc:`Connect ServiceNow to Mattermost </integrate/servicenow-interoperability>` product documentation for available :ref:`Mattermost configuration options <integrate/servicenow-interoperability:mattermost configuration>`.


----

.. config:setting:: integrations-zoom
  :displayname: Zoom interoperability (Plugins)
  :systemconsole: Plugins > Zoom
  :configjson: zoom
  :environment: N/A
  :description: Connect your Zoom instance to your Mattermost instance.

Zoom
----

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

See the :doc:`Connect Zoom to Mattermost </integrate/zoom-interoperability>` product documentation for available :ref:`Mattermost configuration options <integrate/zoom-interoperability:mattermost configuration>`.

----

config.json-only settings
--------------------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. config:setting:: plugins-sigpublickeyfile
  :displayname: Signature public key file (Plugins)
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

.. config:setting:: plugins-chimeraoauthproxyurl
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
