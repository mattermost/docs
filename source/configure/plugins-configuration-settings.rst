Plugins configuration settings
==============================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Both self-hosted and Cloud admins can access the following configuration settings in **System Console > Plugins**. Self-hosted admins can also edit the ``config.json`` file as described in the following tables. 

- `Plugin Management <#plugin-management>`__
- `Agenda <#agenda>`__
- `Antivirus <#antivirus>`__
- `Apps <#apps>`__
- `Autolink <#autolink>`__
- `AWS SNS <#aws-sns>`__
- `Calls <#calls>`__
- `Channel Export <#channel-export>`__
- `Demo Plugin <#demo-plugin>`__
- `GIF commands <#gif-commands>`__
- `Mattermost Boards <#mattermost-boards>`__
- `Mattermost Playbooks <#mattermost-playbooks>`__
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
  - **false**: Mattermost does not attempt to connect to a remote Marketplace, and will show only pre-packaged and installed plugins.

Enable remote Marketplace
~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| - **true**: **(Default)** Mattermost attempts to connect to the endpoint set in **Marketplace URL**. If the connection fails, an error is displayed, and the Marketplace only shows pre-packaged and installed plugins.    | - System Config path: **Plugins > Plugin Management**                        |
| - **false**: Mattermost does not attempt to connect to a remote Marketplace. The Marketplace will only show pre-packaged and installed plugins. Use this setting if your Mattermost server cannot connect to the Internet. | - ``config.json`` setting: ``.PluginSettings.EnableRemoteMarketplace: true`` |
|                                                                                                                                                                                                                            | - Environment variable: ``MM_PLUGINSETTINGS_ENABLEREMOTEMARKETPLACE``        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| **Note**: To connect to a remote Marketplace, **Enable Marketplace** must be **true** and each Mattermost host must have network access to the endpoint set in **Marketplace URL**.                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

Agenda
------

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Plugins > Agenda**.

.. config:setting:: plugins-agendaenable
  :displayname: Enable plugin (Plugins - Agenda)
  :systemconsole: Plugins > Agenda
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the Agenda plugin on your Mattermost server.
  - **false**: (Default) Disables the Agenda plugin on your Mattermost server.

Enable plugin
~~~~~~~~~~~~~

+------------------------------------------------------------------------------+--------------------------------------------+
| - **true**: Enables the Agenda plugin on your Mattermost server.             | - System Config path: **Plugins > Agenda** |
| - **false**: (Default) Disables the Agenda plugin on your Mattermost server. |                                            |
+------------------------------------------------------------------------------+--------------------------------------------+

----

Antivirus
---------

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

This plugin allows the forwarding of uploaded files to an antivirus scanning application, `ClamAV anti-virus software <https://www.clamav.net/>`__, and prevents the upload from completing if there is a virus detected in the file.

Use this plugin to prevent users from inadvertently spreading malware or viruses via your Mattermost server. See the `Mattermost Antivirus Plugin <https://github.com/mattermost/mattermost-plugin-antivirus>`__ documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Antivirus**.

.. config:setting:: plugins-antivirusenable
  :displayname: Enable plugin (Plugins - Antivirus)
  :systemconsole: Plugins > Antivirus
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the Antivirus plugin on your Mattermost server.
  - **false**: (Default) Disables the Antivirus plugin on your Mattermost server.

Enable plugin
~~~~~~~~~~~~~

+---------------------------------------------------------------------------------+-----------------------------------------------+
| - **true**: Enables the Antivirus plugin on your Mattermost server.             | - System Config path: **Plugins > Antivirus** |
| - **false**: (Default) Disables the Antivirus plugin on your Mattermost server. |                                               |
|                                                                                 |                                               |
+---------------------------------------------------------------------------------+-----------------------------------------------+

.. config:setting:: plugins-antivirusclamavhostport
  :displayname: ClamAV - host and port (Plugins - Antivirus)
  :systemconsole: Plugins > Antivirus
  :configjson: N/A
  :environment: N/A
  :description: Specify the hostname and port to connect to the ClamAV server.

ClamAV - host and port
~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------+-----------------------------------------------+
| Sets the **hostname** and **port** to connect to the ClamAV server  | - System Config path: **Plugins > Antivirus** |
| when the Antivirus plugin is enabled.                               |                                               |
+---------------------------------------------------------------------+-----------------------------------------------+

.. config:setting:: plugins-antivirusscantimeout
  :displayname: Scan timeout (Plugins - Antivirus)
  :systemconsole: Plugins > Antivirus
  :configjson: N/A
  :environment: N/A
  :description: Specifies the length of time, in seconds, before the virus scan times out.

Scan timeout (seconds)
~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------+-----------------------------------------------+
| Sets the length of time, in seconds, before the virus scan times out  | - System Config path: **Plugins > Antivirus** |
| when the Antivirus plugin is enabled.                                 |                                               |
+-----------------------------------------------------------------------+-----------------------------------------------+

----

Apps
----

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

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

Autolink
--------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This plugin creates regular expression patterns that are reformatted into a Markdown link before the message is saved into the database. This plugin can be configured through the System Console, ``config.json`` file, or ``/autolink`` slash command. See the `Autolink Plugin <https://github.com/mattermost/mattermost-plugin-autolink/blob/master/README.md>`__ documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Autolink**.

.. config:setting:: plugins-autolinkenable
  :displayname: Enable plugin (Plugins - Autolink)
  :systemconsole: Plugins > Autolink
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the Autolink plugin on your Mattermost server.
  - **false**: (Default) Disables the Autolink plugin on your Mattermost server.

Enable plugin
~~~~~~~~~~~~~

+--------------------------------------------------------------------------------+----------------------------------------------+
| - **true**: Enables the Autolink plugin on your Mattermost server.             | - System Config path: **Plugins > Autolink** |
| - **false**: (Default) Disables the Autolink plugin on your Mattermost server. |                                              |
|                                                                                |                                              |
+--------------------------------------------------------------------------------+----------------------------------------------+

.. config:setting:: plugins-autolinkenableadmin
  :displayname: Enable administration with /autolink command (Plugins - Autolink)
  :systemconsole: Plugins > Autolink
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the ability to configure the Apps plugin using the ``/autolink`` slash command.
  - **false**: (Default) Disables the ability to use the slash command to configure the plugin.

Enable administration with /autolink command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------+----------------------------------------------+
| - **true**: Enables administration of the Autolinks plugin using the ``/autolink`` slash command.             | - System Config path: **Plugins > Autolink** |
| - **false**: (Default) Disables administration of the Autolinks plugin using the ``/autolink`` slash command. |                                              |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------------+

.. config:setting:: plugins-autolinkapplytoupdatedposts
  :displayname: Apply plugin to updated posts as well as new posts (Plugins - Autolink)
  :systemconsole: Plugins > Autolink
  :configjson: N/A
  :environment: N/A

  - **true**: Applies the plugin to updated posts as well as new posts.
  - **false**: (Default) Applies the plugin to new posts only.

Apply plugin to updated posts as well as new posts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------+----------------------------------------------+
| - **true**: Applies the plugin to updated posts as well as new posts. | - System Config path: **Plugins > Autolink** |
| - **false**: (Default) Applies the plugin to new posts only.          |                                              |
|                                                                       |                                              |
+-----------------------------------------------------------------------+----------------------------------------------+

.. config:setting:: plugins-autolinkadminuserids
  :displayname: Admin user IDs (Plugins - Autolink)
  :systemconsole: Plugins > Autolink
  :configjson: N/A
  :environment: N/A
  :description: Specify users authorized to administer the plugin in addition to System Admins. Separate multiple user IDs with commas.

Admin user IDs
~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------+----------------------------------------------+
| Use this setting to authorize non-System Admin users to administer the Autolink plugin  | - System Config path: **Plugins > Autolink** |
| when the Autolink plugin is enabled. Separate multiple user IDs with commas.            |                                              |
+-----------------------------------------------------------------------------------------+----------------------------------------------+

.. tip::

  Find user IDs by going to **System Console > User Management > Users**.

----

AWS SNS
-------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This plugin is used to receive alert notifications from `Amazon AWS CloudWatch <https://aws.amazon.com/cloudwatch/>`__ to Mattermost channels via `AWS Simple Notification Server (SNS) <https://docs.aws.amazon.com/sns/latest/dg/welcome.html>`__.

Access the following configuration settings in the System Console by going to **Plugins > AWS SNS**.

.. config:setting:: plugins-awssnsenable
  :displayname: Enable plugin (Plugins - AWS SNS)
  :systemconsole: Plugins > AWS SNS
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the AWS SNS plugin on your Mattermost server.
  - **false**: (Default) Disables the AWS SNS plugin on your Mattermost server.

Enable plugin
~~~~~~~~~~~~~

+-------------------------------------------------------------------------------+---------------------------------------------+
| - **true**: Enables the AWS SNS plugin on your Mattermost server.             | - System Config path: **Plugins > AWS SNS** |
| - **false**: (Default) Disables the AWS SNS plugin on your Mattermost server. |                                             |
|                                                                               |                                             |
+-------------------------------------------------------------------------------+---------------------------------------------+

.. config:setting:: plugins-awssnsnotificationchannel
  :displayname: Channel to send notifications to (Plugins - AWS SNS)
  :systemconsole: Plugins > AWS SNS
  :configjson: N/A
  :environment: N/A
  :description: Use this setting to specify the channel that will receive AWS SNS notifications in the format, **teamname,channelname**. 

Channel to send notifications to
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+
| Use this setting to specify the channel that will receive AWS SNS notifications by entering the team name and channel name as: **teamname,channelname**. | - System Config path: **Plugins > AWS SNS** |
|                                                                                                                                                          |                                             |
| For example, if the channel URL is https://example.com/**myteam**/channels/**mychannel**, enter: **myteam,mychannel**.                                   |                                             |
|                                                                                                                                                          |                                             |
| If the channel does not exist, the plugin creates the channel for you.                                                                                   |                                             |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------+

.. config:setting:: plugins-awssnsauthorizeduserids
  :displayname: Authorized user IDs (Plugins - AWS SNS)
  :systemconsole: Plugins > AWS SNS
  :configjson: N/A
  :environment: N/A
  :description: Specify users authorized to accept AWS SNS subscriptions to a Mattermost channel. Separate multiple user IDs with commas.

Authorized user IDs
~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------+---------------------------------------------+
| Use this setting to authorize users to accept AWS SNS subscriptions to a Mattermost channel  | - System Config path: **Plugins > AWS SNS** |
| when the AWS SNS plugin is enabled. Separate multiple user IDs with commas.                  |                                             |
+----------------------------------------------------------------------------------------------+---------------------------------------------+

.. tip::

  Find user IDs by going to **System Console > User Management > Users**.

.. config:setting:: plugins-awssnstoken
  :displayname: Token (Plugins - AWS SNS)
  :systemconsole: Plugins > AWS SNS
  :configjson: N/A
  :environment: N/A
  :description: Generate a token to validate incoming requests from AWS SNS by selecting **Regenerate**.

Token
~~~~~

+------------------------------------------------------------------------------------------+---------------------------------------------+
| Generate a token to validate incoming requests from AWS SNS by selecting **Regenerate**  | - System Config path: **Plugins > AWS SNS** |
| when the AWS SNS plugin is enabled.                                                      |                                             |
+------------------------------------------------------------------------------------------+---------------------------------------------+

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
  :displayname: RTC server port (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.udpserveraddress
  :environment: N/A
  :description: The IP address used by the RTC server to listen on. By default the service listens on all the available interfaces.

RTC server address
~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| This setting controls the IP address the RTC server listens to. All Calls traffic will be served through this IP.     | - System Config path: **Plugins > Calls**                                                                 |
|                                                                                                                       | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.udpserveraddress``               |
| Changing this setting requires a plugin restart to take effect.                                                       | - Environment variable: N/A                                                                               |
| If left unset (default value) the service will listen on all the available interfaces.                                |                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| **Note**: This setting is only applicable when not running calls through the standalone ``rtcd`` service.             |                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsrtcserverport
  :displayname: RTC server port (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.udpserverport
  :environment: N/A
  :description: The UDP port the RTC server will listen on. All calls traffic will be served through this port. Default port is **8443**.

RTC server port
~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| This setting controls the UDP port listened on by the RTC server. All Calls traffic will be served through this port. | - System Config path: **Plugins > Calls**                                                              |
|                                                                                                                       | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.udpserverport``               |
|                                                                                                                       | - Environment variable: N/A                                                                            |
| Changing this setting requires a plugin restart to take effect.                                                       |                                                                                                        |
|                                                                                                                       |                                                                                                        |
| Default is **8443**.                                                                                                  |                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| **Note**: This setting is only applicable when not running calls through the standalone ``rtcd`` service.             |                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

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

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This setting overrides the host advertised to clients when connecting to calls.                                                                                          | - System Config path: **Plugins > Calls**                                                                                                                                                                                                                                                      |
|                                                                                                                                                                          | - ``config.json`` setting:  ``PluginSettings.Plugins.com.mattermost.calls.icehostoverride``                                                                                                                                                                                                    |
| This is an optional field. Changing this setting requires a plugin restart to take effect.                                                                               |                                                                                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
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

+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| The URL to a running `rtcd <https://github.com/mattermost/rtcd>`__ service instance that will host the calls. | - System Config path: **Plugins > Calls**                                                               |
|                                                                                                               | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.rtcdserviceurl``               |
|                                                                                                               | - Environment variable: N/A                                                                             |
| When set (non empty) all the calls will be handled by this external service.                                  |                                                                                                         |
|                                                                                                               |                                                                                                         |
| This is an optional field. Changing this setting requires a plugin restart to take effect.                    |                                                                                                         |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+

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
| **Note**: This functionality has the following requirements:                                                           |                                                                                                          |
|                                                                                                                        |                                                                                                          |
| - Calls plugin version >= v0.16.0                                                                                      |                                                                                                          |
|                                                                                                                        |                                                                                                          |
| - ``rtcd`` version >= v0.10.0 (if in use)                                                                              |                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-enablecallrecordings
  :displayname: Enable call recordings (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: PluginSettings.Plugins.com.mattermost.calls.enablerecordings
  :environment: N/A
  :description: Allow call hosts to record meeting video and audio. 

Enable call recordings (beta)
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

+------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| The URL to a running job service where all the processing related to recordings happens. The recorded files produced are stored in Mattermost. | - System Config path: **Plugins > Calls**                                                               |
|                                                                                                                                                | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.jobserviceurl``                |
| This is a required field. Changing this setting requires a plugin restart to take effect.                                                      |                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| The audio and video quality of call recordings. Available options are: *Low*, *Medium* and *High*.                          | - System Config path: **Plugins > Calls**                                                                                                                      |
|                                                                                                                             | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.calls.recordingquality``                                                                    |
| The default is **Medium**. This is a required value.                                                                        |                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Note**: The quality setting will affect the performance of the recording service and the file size of recordings. Refer to the `deployment section <configure/calls-deployment.html#configure-recording>`__ for more information.                                                          |
+-----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |note| replace:: .

----

Channel export
--------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Plugins > Channel Export**.

.. config:setting:: plugins-channelexportenable
  :displayname: Enable plugin (Plugins - Channel Export)
  :systemconsole: Plugins > Channel Export
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the Channel Export plugin on your Mattermost workspace.
  - **false**: (Default) Disables the Channel Export plugin on your Mattermost workspace.

Enable Plugin
~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------+----------------------------------------------------+
| - **true**: Enables the Channel Export plugin on your Mattermost workspace.             | - System Config path: **Plugins > Channel Export** |
| - **false**: (Default) Disables the Channel Export plugin on your Mattermost workspace. |                                                    |
|                                                                                         |                                                    |
+-----------------------------------------------------------------------------------------+----------------------------------------------------+

----

Demo plugin
-----------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Plugins > Demo Plugin**.

.. config:setting:: plugins-demoenable
  :displayname: Enable plugin (Plugins - Demo)
  :systemconsole: Plugins > Demo Plugin
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the Demo plugin on your Mattermost workspace.
  - **false**: (Default) Disables the Demo plugin on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

+-------------------------------------------------------------------------------+-------------------------------------------------+
| - **true**: Enables the Demo plugin on your Mattermost workspace.             | - System Config path: **Plugins > Demo Plugin** |
| - **false**: (Default) Disables the Demo plugin on your Mattermost workspace. |                                                 |
+-------------------------------------------------------------------------------+-------------------------------------------------+

.. config:setting:: plugins-demochannelname
  :displayname: Channel name (Plugins - Demo)
  :systemconsole: Plugins > Demo Plugin
  :configjson: N/A
  :environment: N/A
  :description: Specify the channel to use as part of the demo plugin. If the specified channel does not exist, the plugin creates the channel for you.

Channel name
~~~~~~~~~~~~

+----------------------------------------------------------------------------------+-------------------------------------------------+
| Specify the channel to use as part of the demo plugin, when enabled.             | - System Config path: **Plugins > Demo Plugin** |
|                                                                                  |                                                 |
| If the specified channel does not exist, the plugin creates the channel for you. |                                                 |
+----------------------------------------------------------------------------------+-------------------------------------------------+

.. config:setting:: plugins-demousername
  :displayname: Username (Plugins - Demo)
  :systemconsole: Plugins > Demo Plugin
  :configjson: N/A
  :environment: N/A
  :description: Specify the user to use as part of the demo plugin. If the specified user does not exist, the plugin creates the user for you.

Username
~~~~~~~~

+----------------------------------------------------------------------------+-------------------------------------------------+
| Specify the user for the demo plugin, when enabled.                        | - System Config path: **Plugins > Demo Plugin** |
|                                                                            |                                                 |
| If the specified user does not exist, the plugin creates the user for you. |                                                 |
+----------------------------------------------------------------------------+-------------------------------------------------+

----

GIF commands
------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Plugins > GIF commands**.

This plugin is used to post GIFs from Gfycat, Giphy, or Tenor using slash commands.

.. config:setting:: plugins-gifenable
  :displayname: Enable plugins (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the GIF commands plugin on your Mattermost server.
  - **false**: (Default) Disables the GIF commands plugin on your Mattermost server.

Enable plugin
~~~~~~~~~~~~~

+------------------------------------------------------------------------------------+--------------------------------------------------+
| - **true**: Enables the GIF commands plugin on your Mattermost server.             | - System Config path: **Plugins > GIF commands** |
| - **false**: (Default) Disables the GIF commands plugin on your Mattermost server. |                                                  |
+------------------------------------------------------------------------------------+--------------------------------------------------+

.. config:setting:: plugins-gifdisplayas
  :displayname: Display the GIF as (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A
  :description: Display the GIF as an embedded image where the GIF can't be collapsed, or as a collapsible image preview where the full URL displays.

Display the GIF as
~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| Display the GIF as an embedded image where the GIF can't be collapsed, or as a collapsible image preview where the full URL displays. | - System Config path: **Plugins > GIF commands** |
|                                                                                                                                       |                                                  |
|                                                                                                                                       |                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| **Note**:                                                                                                                                                                                | 
|  - `Link previews <https://docs.mattermost.com/configure/site-configuration-settings.html#enable-website-link-previews>`__ must be enabled to display GIF previews.                      |
|  -  Mattermost deployments behind a firewall must open port 443 to both ``https://api.gfycat.com/v1`` and ``https://gfycat.com/<id>`` for all request types.                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-gifprovider
  :displayname: GIF provider (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A
  :description: Specify the GIF provider as **GIPHY**, **Tenor**, or **Gfycat**.

GIF provider
~~~~~~~~~~~~

+-------------------------------------------------------------------+-----------------------------------------------------+
| Specify the GIF provider as **GIPHY**, **Tenor**, or **Gfycat**.  | - System Config path: **Plugins > GIF commands**    |
+-------------------------------------------------------------------+-----------------------------------------------------+
| **Note**: Selecting GIPHY or Tenor requires an API key. A key is not required for Gfycat.                               |
+-------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-gifgiphytenorapikey
  :displayname: Giphy/Tenor API key (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A
  :description: Configure your own API Key when specifying the GIF Provider as GIPHY or Tenor. An API key is not required for Gfycat.

Giphy/Tenor API key
~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| Configure your own API key when specifying the GIF Provider as GIPHY or Tenor. An API key is not required for Gfycat. | - System Config path: **Plugins > GIF commands** |
|                                                                                                                       |                                                  |
| See the `GIPHY <https://developers.giphy.com/docs/api/#quick-start-guide>`__                                          |                                                  |
| or `Tenor <https://tenor.com/developer/keyregistration>`__ documentation for details.                                 |                                                  |
+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+

.. config:setting:: plugins-gifcontentrating
  :displayname: Content rating (GIPHY & Tenor only) (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A
  :description: Select an `MPAA-style content rating <https://en.wikipedia.org/wiki/Motion_Picture_Association_film_rating_system>`__ for GIFs from GIPHY or Tenor. Leave this field empty to disable content filtering.

Content rating (GIPHY & Tenor only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| Select an `MPAA-style content rating <https://en.wikipedia.org/wiki/Motion_Picture_Association_film_rating_system>`__ | - System Config path: **Plugins > GIF commands** |
| for GIFs from GIPHY or Tenor. Leave this field empty to disable content filtering.                                    |                                                  |
+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+

.. config:setting:: plugins-gifgfycatdisplaystyle
  :displayname: Gfycat display style (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A
  :description: Specify the display style for GIFs from Gfycat. See the `Gfycat Developer API <https://developers.gfycat.com/api/>`__ documentation for details.

Gfycat display style
~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------+--------------------------------------------------+
| Specify the display style for GIFs from Gfycat. See the `Gfycat Developer API | - System Config path: **Plugins > GIF commands** |
| <https://developers.gfycat.com/api/>`__ documentation for details.            |                                                  |
+-------------------------------------------------------------------------------+--------------------------------------------------+

.. config:setting:: plugins-gifgiphydisplaystyle
  :displayname: GIPHY display style (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A
  :description: Specify the display style for GIFs from GIPHY. See the `GIPHY Developers Rendition Guide <https://developers.giphy.com/docs/optional-settings/>`__ for details.

GIPHY display style
~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------+--------------------------------------------------+
| Specify the display style for GIFs from GIPHY. See the `GIPHY Developers               | - System Config path: **Plugins > GIF commands** |
| Rendition Guide <https://developers.giphy.com/docs/optional-settings/>`__ for details. |                                                  |
+----------------------------------------------------------------------------------------+--------------------------------------------------+

.. config:setting:: plugins-giftenordisplaystyle
  :displayname: Tenor display style (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A
  :description: Specify the display style for GIFs from Tenor. See the `Tenor API <https://tenor.com/gifapi/documentation#responseobjects-gifformat>`__ documentation for details.

Tenor display style
~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------+--------------------------------------------------+
| Specify the display style for GIFs from Tenor. See the `Tenor API                                | - System Config path: **Plugins > GIF commands** |
| <https://tenor.com/gifapi/documentation#responseobjects-gifformat>`__ documentation for details. |                                                  |
+--------------------------------------------------------------------------------------------------+--------------------------------------------------+

.. config:setting:: plugins-giflanguage
  :displayname: Language (Plugins - GIF)
  :systemconsole: Plugins > GIF commands 
  :configjson: N/A
  :environment: N/A
  :description: Specify the language used to search GIFs from GIPHY. See the `GIPHY Developers Language Support <https://developers.giphy.com/docs/optional-settings/#language-support>`__ documentation for details.

Language
~~~~~~~~

+-----------------------------------------------------------------------------------------+--------------------------------------------------+
| Specify the language used to search GIFs from GIPHY. See the `GIPHY Developers Language | - System Config path: **Plugins > GIF commands** |
| Support <https://developers.giphy.com/docs/optional-settings/#language-support>`__      |                                                  |
| documentation for details.                                                              |                                                  |
+-----------------------------------------------------------------------------------------+--------------------------------------------------+

.. config:setting:: plugins-gifforcepreview
  :displayname: Force GIF preview before posting (force /gifs) (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A

  - **true**: Prevents accidental posting of inappropriate GIFs from a provider that does not support content rating filtering.
  - **false**: (Default) Both ``/gif`` and ``/gifs`` slash commands are available for the GIF commands plugin on your Mattermost server.

Force GIF preview before posting (force /gifs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+
| - **true**: Prevents accidental posting of inappropriate GIFs from a provider that does not support content rating filtering.                         | - System Config path: **Plugins > GIF commands** |
| - **false**: (Default) Both ``/gif`` and ``/gifs`` slash commands are available for the GIF commands plugin on your Mattermost server.                |                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+

----

Mattermost Boards
-----------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Mattermost Boards is an open source alternative to Trello, Notion, and Asana. Boards is a project management tool that helps define, organize, track and manage work across teams, using a familiar kanban board view. See the `Mattermost Boards <https://docs.mattermost.com/guides/boards.html>`__ product documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Mattermost Boards**.

.. config:setting:: plugins-boardsenable
  :displayname: Enable plugin (Plugins - Boards)
  :systemconsole: Plugins > Mattermost Boards
  :configjson: 
  :environment: 

  - **true**: Enables the Mattermost Boards plugin on your Mattermost workspace.
  - **false**: Disables the Mattermost Boards plugin on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

+----------------------------------------------------------------------------------+-------------------------------------------------------+
| - **true**: Enables the Mattermost Boards plugin on your Mattermost workspace.   | - System Config path: **Plugins > Mattermost Boards** |
| - **false**: Disables the Mattermost Boards plugin on your Mattermost workspace. | - ``config.json`` setting:                            |
|                                                                                  | - Environment variable:                               |
+----------------------------------------------------------------------------------+-------------------------------------------------------+

----

Mattermost Playbooks
--------------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Mattermost Playbooks is an open source, self-hosted collaboration tool for teams. Each playbook represents a recurring outcome or specific goal that your teams collaborate on to achieve, such as service outage recovery or customer onboarding. Teams run a playbook every time they want to orchestrate people, tools, and data to achieve that outcome as quickly as possible while providing visibility to stakeholders. Playbooks also allow teams to incorporate learnings from the retrospective to tweak and improve the playbook with every iteration. See the `Mattermost Playbooks <https://docs.mattermost.com/guides/playbooks.html>`__ documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Playbooks**.

.. config:setting:: plugins-playbooksenable
  :displayname: Enable plugin (Plugins - Playbooks)
  :systemconsole: Plugins > Playbooks
  :configjson: 
  :environment: 

  - **true**: Enables the Mattermost Playbooks plugin on your Mattermost workspace.
  - **false**: Disables the Mattermost Playbooks plugin on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------+-----------------------------------------------+
| - **true**: Enables the Mattermost Playbooks plugin on your Mattermost workspace.   | - System Config path: **Plugins > Playbooks** |
| - **false**: Disables the Mattermost Playbooks plugin on your Mattermost workspace. | - ``config.json`` setting:                    |
|                                                                                     | - Environment variable:                       |
+-------------------------------------------------------------------------------------+-----------------------------------------------+

.. config:setting:: plugins-playbooksenabledteams
  :displayname: Enabled teams (Plugins - Playbooks)
  :systemconsole: Plugins > Playbooks
  :configjson: 
  :environment: 
  :description: Enable Playbooks for all Mattermost teams, or for only selected teams.

Enabled teams
~~~~~~~~~~~~~

+------------------------------------------------------------------------+-----------------------------------------------+
| Enable Playbooks for all Mattermost teams, or for only selected teams. | - System Config path: **Plugins > Playbooks** |
|                                                                        | - ``config.json`` setting:                    |
|                                                                        | - Environment variable:                       |
+------------------------------------------------------------------------+-----------------------------------------------+

.. config:setting:: plugins-playbooksexperimentalfeatures
  :displayname: Enable experimental features (Plugins - Playbooks)
  :systemconsole: Plugins > Playbooks
  :configjson: 
  :environment: 

  - **true**: Enables experimental Playbooks features on your Mattermost workspace.
  - **false**: Disables experimental Playbooks features on your Mattermost workspace.

Enable experimental features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------+-----------------------------------------------+
| - **true**: Enables experimental Playbooks features on your Mattermost workspace.   | - System Config path: **Plugins > Playbooks** |
| - **false**: Disables experimental Playbooks features on your Mattermost workspace. | - ``config.json`` setting:                    |
|                                                                                     | - Environment variable:                       |
+-------------------------------------------------------------------------------------+-----------------------------------------------+

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
