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
  :configjson: Enable
  :environment: N/A

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
  :configjson: RequirePluginSignature
  :environment: N/A

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
  :configjson: AutomaticPrepackagedPlugins
  :environment: N/A

  - **true**: **(Default)** Mattermost automatically installs and upgrades any enabled pre-packaged plugins.
  - **false**: Mattermost does not automatically install or upgrade pre-packaged plugins.

Automatic prepackaged plugins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| - **true**: **(Default)** Mattermost automatically installs and upgrades any enabled pre-packaged plugins. If a newer version is installed, no changes are made.                | - System Config path: **Plugins > Plugin Management**                            |
| - **false**: Mattermost does not automatically install or upgrade pre-packaged plugins. Pre-packaged plugins may be installed manually from the Marketplace, even when offline. | - ``config.json`` setting: ``.PluginSettings.AutomaticPrepackagedPlugins: true`` |
|                                                                                                                                                                                 | - Environment variable: ``MM_PLUGINSETTINGS_AUTOMATICPREPACKAGEDPLUGINS``        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: plugins-enablemarketplace
  :displayname: Enable marketplace (Plugins - Management)
  :systemconsole: Plugins > Plugin Management
  :configjson: EnableMarketplace
  :environment: N/A

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
  :configjson: EnableRemoteMarketplace
  :environment: N/A

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
  :configjson: MarketplaceUrl
  :environment: N/A
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
  :configjson: PluginStates
  :environment: N/A
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
  :configjson: Plugins
  :environment: N/A
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
  - **false**: Disables the Agenda plugin on your Mattermost server.

Enable plugin
~~~~~~~~~~~~~

+--------------------------------------------------------------------+--------------------------------------------+
| - **true**: Enables the Agenda plugin on your Mattermost server.   | - System Config path: **Plugins > Agenda** |
| - **false**: Disables the Agenda plugin on your Mattermost server. | - ``config.json`` setting: N/A             |
|                                                                    | - Environment variable: N/A                |
+--------------------------------------------------------------------+--------------------------------------------+

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
  - **false**: Disables the Antivirus plugin on your Mattermost server.

Enable plugin
~~~~~~~~~~~~~

+-----------------------------------------------------------------------+-----------------------------------------------+
| - **true**: Enables the Antivirus plugin on your Mattermost server.   | - System Config path: **Plugins > Antivirus** |
| - **false**: Disables the Antivirus plugin on your Mattermost server. | - ``config.json`` setting: N/A                |
|                                                                       | - Environment variable: N/A                   |
+-----------------------------------------------------------------------+-----------------------------------------------+

.. config:setting:: plugins-antivirusclamavhostport
  :displayname: ClamAV - host and port (Plugins - Antivirus)
  :systemconsole: Plugins > Antivirus
  :configjson: N/A
  :environment: N/A
  :description: Specify the hostname and port to connect to the ClamAV server.

ClamAV - host and port
~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------+-----------------------------------------------+
| Sets the **hostname** and **port** to connect to the ClamAV server. | - System Config path: **Plugins > Antivirus** |
|                                                                     | - ``config.json`` setting: N/A                |
|                                                                     | - Environment variable: N/A                   |
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
| Sets the length of time, in seconds, before the virus scan times out. | - System Config path: **Plugins > Antivirus** |
|                                                                       | - ``config.json`` setting: N/A                |
|                                                                       | - Environment variable: N/A                   |
+-----------------------------------------------------------------------+-----------------------------------------------+

----

Apps
----

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. config:setting:: plugins-appsenable
  :displayname: Enable plugin (Plugins - Apps)
  :systemconsole: Plugins > Apps
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the Apps plugin on your Mattermost server.
  - **false**: Disables the Apps plugin on your Mattermost server.

Enable plugin
~~~~~~~~~~~~~

**True**: Enables the Apps plugin on your Mattermost server.

**False**: Disables the Apps plugin on your Mattermost server.

To create your own Mattermost App, see the `Mattermost Apps <https://developers.mattermost.com/integrate/apps/>`__ developer documentation.

----

Autolink
--------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This plugin creates regular expression (regexp) patterns that are reformatted into a Markdown link before the message is saved into the database. System Admins can configure this plugin in the ``config.json`` file, using the ``/autolink`` slash command (when enabled), or through using the System Console. See the `Autolink Plugin <https://github.com/mattermost/mattermost-plugin-autolink/blob/master/README.md>`__ documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Autolink**.

.. config:setting:: plugins-autolinkenable
  :displayname: Enable plugin (Plugins - Autolink)
  :systemconsole: Plugins > Autolink
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the Autolink plugin on your Mattermost server.
  - **false**: Disables the Autolink plugin on your Mattermost server.

Enable plugin
~~~~~~~~~~~~~

**True**: Enables the Autolink plugin on your Mattermost server.

**False**: Disables the Autolink plugin on your Mattermost server.

.. config:setting:: plugins-autolinkenableadmin
  :displayname: Enable administration with /autolink command (Plugins - Autolink)
  :systemconsole: Plugins > Autolink
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the ability to configure the Apps plugin using the ``/autolink`` slash command.
  - **false**: Disables the ability to use the slash command to configure the plugin.

Enable administration with /autolink command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Enables the ability to configure the Apps plugin using the ``/autolink`` slash command.

**False**: Disables the ability to use the slash command to configure the plugin.

.. config:setting:: plugins-autolinkapplytoupdatedposts
  :displayname: Apply plugin to updated posts as well as new posts (Plugins - Autolink)
  :systemconsole: Plugins > Autolink
  :configjson: N/A
  :environment: N/A

  - **true**: Applies the plugin to updated posts as well as new posts.
  - **false**: Applies the plugin to new posts only.

Apply plugin to updated posts as well as new posts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Applies the plugin to updated posts as well as new posts.

**False**: Applies the plugin to new posts only.

.. config:setting:: plugins-autolinkadminuserids
  :displayname: Admin user IDs (Plugins - Autolink)
  :systemconsole: Plugins > Autolink
  :configjson: N/A
  :environment: N/A
  :description: Specify users authorized to administer the plugin in addition to System Admins. Separate multiple user IDs with commas.

Admin user IDs
~~~~~~~~~~~~~~

Specify users authorized to administer the plugin in addition to system admins. Separate multiple user IDs with commas.

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
  - **false**: Disables the AWS SNS plugin on your Mattermost server.

Enable plugin
~~~~~~~~~~~~~

**True**: Enables the AWS SNS plugin on your Mattermost server.

**False**: Disables the AWS SNS plugin on your Mattermost server.

.. config:setting:: plugins-awssnsnotificationchannel
  :displayname: Channel to send notifications to (Plugins - AWS SNS)
  :systemconsole: Plugins > AWS SNS
  :configjson: N/A
  :environment: N/A
  :description: Specify the channel to send notifications to in the format ``teamname,channelname``.

Channel to send notifications to
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Specify the channel to send notifications to in the format ``teamname,channelname``. For example, for a channel with a URL of ``https://example.com/myteam/channels/mychannel``, set the value to ``myteam,mychannel``. If the specified channel does not exist, the plugin creates the channel for you.

.. config:setting:: plugins-awssnsauthorizeduserids
  :displayname: Authorized user IDs (Plugins - AWS SNS)
  :systemconsole: Plugins > AWS SNS
  :configjson: N/A
  :environment: N/A
  :description: Specify users authorized to accept AWS SNS subscriptions to a Mattermost channel. Separate multiple user IDs with commas.

Authorized user IDs
~~~~~~~~~~~~~~~~~~~

Specify users authorized to accept AWS SNS subscriptions to a Mattermost channel. Separate multiple user IDs with commas.

.. tip::

  Find user IDs by going to **System Console > User Management > Users**.

Token
~~~~~

Generate a token to validate incoming requests from AWS SNS by selecting ``Regenerate``.

----

Calls
-----

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Plugins > Calls**.

.. config:setting:: plugins-callsenable
  :displayname: Enable plugin (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the calls plugin on your Mattermost workspace.
  - **false**: Disables the calls plugin on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

+----------------------------------------------------------------------+-------------------------------------------+
| - **true**: Enables the Calls plugin on your Mattermost workspace.   | - System Config path: **Plugins > Calls** |
| - **false**: Disables the Calls plugin on your Mattermost workspace. | - ``config.json`` setting: N/A            |
|                                                                      | - Environment variable: N/A               |
+----------------------------------------------------------------------+-------------------------------------------+

.. config:setting:: plugins-callsrtcserverport
  :displayname: RTC server port (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: N/A
  :environment: N/A
  :description: The UDP port the RTC server will listen on. All calls traffic will be served through this port. Default port is **8443**.

RTC server port
~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------------------------------------------------+-------------------------------------------+
| This setting controls the UDP port listened on by the RTC server. All Calls traffic will be served through this port. | - System Config path: **Plugins > Calls** |
|                                                                                                                       | - ``config.json`` setting: N/A            |
| Changing this setting requires a plugin restart to take effect.                                                       | - Environment variable: N/A               |
|                                                                                                                       |                                           |
| Default is **8443**.                                                                                                  |                                           |
+-----------------------------------------------------------------------------------------------------------------------+-------------------------------------------+

.. config:setting:: plugins-enableonspecificchannels
  :displayname: Enable on specific channels (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: N/A
  :environment: N/A
  :description: Manage who can enable or disable calls on specific channels (deprecated from Mattermost v7.7)

Enable on specific channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Admins can't configure this setting from Mattermost v7.7; it's hidden and always enabled*

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+
| - **true**: Channel admins can enable or disable calls on specific channels. Participants in DMs/GMs can also enable or disable calls. | - System Config path: **Plugins > Calls** |
| - **false**: Only System Admins can enable or disable calls on specific channels.                                                      | - ``config.json`` setting: N/A            |
|                                                                                                                                        | - Environment variable: N/A               |
|                                                                                                                                        |                                           |
|                                                                                                                                        |                                           |
+----------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+

.. config:setting:: plugins-testmode
  :displayname: Test mode (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: N/A
  :environment: N/A
  :description: A setting to allow system admins to test calls before making them available across the deployment. This setting was called **Enable on all channels** up until Mattermost v7.7.

Test mode
~~~~~~~~~

*This setting was called Enable on all channels up until Mattermost v7.7*

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| - **true**: Only System Admins can start calls in channels.                                                                                | - System Config path: **Plugins > Calls**                                                                                                          |
| - **false**: All team members can start calls in channels.                                                                                 | - ``config.json`` setting: N/A                                                                                                                     |
|                                                                                                                                            | - Environment variable: N/A                                                                                                                        |
|                                                                                                                                            |                                                                                                                                                    |
|                                                                                                                                            |                                                                                                                                                    |
+--------------------------------------------------------------+-----------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **Note**: Use this setting to confirm calls work as expected. When **true**, users attempting to start calls are prompted to contact System Admins. System Admins are prompted to confirm that calls are working as expected before switching to live mode.                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsmaxcallparticipants
  :displayname: Max call participants (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: N/A
  :environment: N/A
  :description: The maximum number of participants that can join a single call. Default value is **0** (unlimited). The maximum recommended setting is 200.

Max call participants
~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------+-------------------------------------------+
| This setting limits the number of participants that can join a single call. | - System Config path: **Plugins > Calls** |
|                                                                             | - ``config.json`` setting: N/A            |
|                                                                             | - Environment variable: N/A               |
| Default is **0** (no limit).                                                |                                           |
+-----------------------------------------------------------------------------+-------------------------------------------+
| **Note**: This setting is optional, but the recommended maximum number of participants is **200**.                      |
+-------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: plugins-callsicehost
  :displayname: ICE host override (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: N/A
  :environment: N/A
  :description: An optional override to the host that gets advertised to clients when connecting to calls. When empty or unset, the RTC service will attempt to automatically find the instance's public IP through STUN.

ICE host override
~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This setting overrides the host advertised to clients when connecting to calls.                                                                                          | - System Config path: **Plugins > Calls**                                                                                                                                                                                                                                                      |
|                                                                                                                                                                          | - ``config.json`` setting: N/A                                                                                                                                                                                                                                                                 |
| This is an optional field. Changing this setting requires a plugin restart to take effect.                                                                               | - Environment variable: N/A                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Note**:                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|   - Depending on the network infrastructure (e.g. instance behind a NAT device) it may be necessary to set this field to the client facing external IP for clients to connect. When empty or unset, the RTC service will attempt to find the instance's public IP through STUN.                                                                                                                                                                                           |
|   - A hostname (e.g. domain name) can be specified in this setting, but an IP address will be passed to clients. This means that a DNS resolution happens on the Mattermost instance which could result in a different IP address from the one the clients would see, causing connectivity to fail. When in doubt, we recommend using an IP address directly or confirming that the resolution on the host side reflects the one on the client.                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+



.. config:setting:: plugins-callsiceservers
  :displayname: ICE server configurations (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: N/A
  :environment: N/A
  :description: A list of ICE servers (STUN/TURN) to be used by the service. Value should be valid JSON. Default value is **[{"urls": ["stun:stun.global.calls.mattermost.com:3478"]}]**.

ICE servers configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-------------------------------------------------------------------------------------------------+-------------------------------------------+
| This setting stores a list of ICE servers (STUN/TURN) in JSON format to be used by the service. | - System Config path: **Plugins > Calls** |
|                                                                                                 | - ``config.json`` setting: N/A            |
| This is an optional field. Changing this setting may require a plugin restart to take effect.   | - Environment variable: N/A               |
|                                                                                                 |                                           |
| Default is **[{"urls": ["stun:stun.global.calls.mattermost.com:3478"]}]**                       |                                           |
+-------------------------------------------------------------------------------------------------+-------------------------------------------+
 
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
 
 

.. config:setting:: plugins-callsturnauthsecret
  :displayname: TURN static auth secret (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: N/A
  :environment: N/A
  :description: A static secret used to generate short-lived credentials for TURN servers.

TURN static auth secret
~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+----------------------------------------------------------------------------+-------------------------------------------+
| A static secret used to generate short-lived credentials for TURN servers. | - System Config path: **Plugins > Calls** |
|                                                                            | - ``config.json`` setting: N/A            |
| This is an optional field.                                                 | - Environment variable: N/A               |
+----------------------------------------------------------------------------+-------------------------------------------+

.. config:setting:: plugins-callsturncredentialsexpiration
  :displayname: TURN credentials expiration (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: N/A
  :environment: N/A
  :description: The expiration, in minutes, of the short-lived credentials generated for TURN servers.

TURN credentials expiration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+----------------------------------------------------------------------------------------+-------------------------------------------+
| The expiration, in minutes, of the short-lived credentials generated for TURN servers. | - System Config path: **Plugins > Calls** |
|                                                                                        | - ``config.json`` setting: N/A            |
|                                                                                        | - Environment variable: N/A               |
+----------------------------------------------------------------------------------------+-------------------------------------------+

.. config:setting:: plugins-callsserversideturn
  :displayname: Server side TURN (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: N/A
  :environment: N/A

  - **true**: The RTC server will use the configured TURN candidates for server-initiated connections.
  - **false**: TURN will be used only on the client-side.

Server side TURN
~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+------------------------------------------------------------------------------------------------------+-------------------------------------------+
| - **true**: The RTC server will use the configured TURN candidates for server-initiated connections. | - System Config path: **Plugins > Calls** |
| - **false**: TURN will be used only on the client-side.                                              | - ``config.json`` setting: N/A            |
|                                                                                                      | - Environment variable: N/A               |
| Changing this setting requires a plugin restart to take effect.                                      |                                           |
+------------------------------------------------------------------------------------------------------+-------------------------------------------+

.. config:setting:: plugins-callsallowscreensharing
  :displayname: Allow screen sharing (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: N/A
  :environment: N/A

  - **true**: Call participants will be allowed to share their screen.
  - **false**: Call participants won't be allowed to share their screen.

Allow screen sharing
~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+------------------------------------------------------------------------+-------------------------------------------+
| - **true**: Call participants will be allowed to share their screen.   | - System Config path: **Plugins > Calls** |
| - **false**: Call participants won't be allowed to share their screen. | - ``config.json`` setting: N/A            |
|                                                                        | - Environment variable: N/A               |
| Changing this setting requires a plugin restart to take effect.        |                                           |
+------------------------------------------------------------------------+-------------------------------------------+

.. config:setting:: plugins-callsrtcdserviceurl
  :displayname: RTCD service URL (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: N/A
  :environment: N/A
  :description: The URL to a running `rtcd <https://github.com/mattermost/rtcd>`__ service instance that will host the calls. When set (non empty) all the calls will be handled by this external service.

RTCD service URL
~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------------------------------------------+-------------------------------------------+
| The URL to a running `rtcd <https://github.com/mattermost/rtcd>`__ service instance that will host the calls. | - System Config path: **Plugins > Calls** |
|                                                                                                               | - ``config.json`` setting: N/A            |
| When set (non empty) all the calls will be handled by this external service.                                  | - Environment variable: N/A               |
|                                                                                                               |                                           |
| This is an optional field. Changing this setting requires a plugin restart to take effect.                    |                                           |
+---------------------------------------------------------------------------------------------------------------+-------------------------------------------+

.. config:setting:: plugins-enablecallrecordings
  :displayname: Enable call recordings (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: N/A
  :environment: N/A
  :description: Allow call hosts to record meeting video and audio. 

Enable call recordings (beta)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+
| - **true**: Allows call hosts to record meeting video and audio.                                                                                      | - System Config path: **Plugins > Calls** |
| - **false**: **(Default)** Call recording functionality is not available to hosts.                                                                    | - ``config.json`` setting: N/A            |
|                                                                                                                                                       | - Environment variable: N/A               |
| Recordings include the entire call window view along with participants' audio track and any shared screen video. Recordings are stored in Mattermost. |                                           |
|                                                                                                                                                       |                                           |
| Changing this setting requires a plugin restart to take effect.                                                                                       |                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+

.. config:setting:: plugins-jobserviceurl
  :displayname: Job service URL (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: N/A
  :environment: N/A
  :description: The URL to a running job service where all the processing related to recordings happens.
  
Job service URL
~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

The URL to a running job service where all the processing related to recordings happens. The recorded files produced are stored in Mattermost.

This is a required field. Changing this setting requires a plugin restart to take effect.

.. config:setting:: plugins-maximumcallrecordingduration
  :displayname: Maximum call recording duration (Plugins - Calls)
  :systemconsole: Plugins > Calls
  :configjson: N/A
  :environment: N/A
  :description: The maximum duration of a call recording in minutes.
  
Maximum call recording duration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

The maximum duration of a call recording in minutes. The default is 60 with a maximum of 180. A recording of a 60-minute call will result in a file of about 700 MB.

This is a required value.

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
  - **false**: Disables the Channel Export plugin on your Mattermost workspace.

Enable Plugin
~~~~~~~~~~~~~

**True**: Enables the Channel Export plugin on your Mattermost workspace.

**False**: Disables the Channel Export plugin on your Mattermost workspace.

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
  - **false**: Disables the Demo plugin on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

**True**: Enables the Demo plugin on your Mattermost workspace.

**False**: Disables the Demo plugin on your Mattermost workspace.

.. config:setting:: plugins-demochannelname
  :displayname: Channel name (Plugins - Demo)
  :systemconsole: Plugins > Demo Plugin
  :configjson: N/A
  :environment: N/A
  :description: Specify the channel to use as part of the demo plugin. If the specified channel does not exist, the plugin creates the channel for you.

Channel name
~~~~~~~~~~~~

Specify the channel to use as part of the demo plugin. If the specified channel does not exist, the plugin creates the channel for you.

.. config:setting:: plugins-demousername
  :displayname: Username (Plugins - Demo)
  :systemconsole: Plugins > Demo Plugin
  :configjson: N/A
  :environment: N/A
  :description: Specify the user to use as part of the demo plugin. If the specified user does not exist, the plugin creates the user for you.

Username
~~~~~~~~

Specify the user to use as part of the demo plugin. If the specified user does not exist, the plugin creates the user for you.

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
  - **false**: Disables the GIF commands plugin on your Mattermost server.

Enable plugin
~~~~~~~~~~~~~

**True**: Enables the GIF commands plugin on your Mattermost server.

**False**: Disables the GIF commands plugin on your Mattermost server.

.. config:setting:: plugins-gifdisplayas
  :displayname: Display the GIF as (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A
  :description: Display the GIF as an embedded image where the GIF can't be collapsed, or as a collapsible image preview where the full URL displays.

Display the GIF as
~~~~~~~~~~~~~~~~~~

Display the GIF as an embedded image where the GIF can't be collapsed, or as a collapsible image preview where the full URL displays.

.. note::
   `Link previews <https://docs.mattermost.com/configure/configuration-settings.html#enable-link-previews>`__ must be enabled in order to display GIF link previews. Mattermost deployments restricted to access behind a firewall must open port 443 to both ``https://api.gfycat.com/v1`` and ``https://gfycat.com/<id>`` (for all request types) for this feature to work.

.. config:setting:: plugins-gifprovider
  :displayname: GIF provider (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A
  :description: Specify the GIF provider as GIPHY, Tenor, or Gfycat.

GIF provider
~~~~~~~~~~~~

Specify the GIF provider as GIPHY, Tenor, or Gfycat.

.. note::
  Selecting GIPHY or Tenor requires an API Key for this feature to work. An API key is not required for Gfycat.

.. config:setting:: plugins-gifgiphytenorapikey
  :displayname: Giphy/Tenor API key (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A
  :description: Configure your own API Key when specifying the GIF Provider as GIPHY or Tenor. An API key is not required for Gfycat.

Giphy/Tenor API key
~~~~~~~~~~~~~~~~~~~

Configure your own API key when specifying the GIF Provider as GIPHY or Tenor. An API key is not required for Gfycat.

To get your own API key, see the `GIPHY Developers Quick Start <https://developers.giphy.com/docs/api/#quick-start-guide>`__ documentation, or the `Tenor Developer <https://tenor.com/developer/keyregistration>`__ documentation for details.

.. config:setting:: plugins-gifcontentrating
  :displayname: Content rating (GIPHY & Tenor only) (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A
  :description: Select an `MPAA-style content rating <https://en.wikipedia.org/wiki/Motion_Picture_Association_film_rating_system>`__ for GIFs from GIPHY or Tenor. Leave this field empty to disable content filtering.

Content rating (GIPHY & Tenor only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select an `MPAA-style content rating <https://en.wikipedia.org/wiki/Motion_Picture_Association_film_rating_system>`__ for GIFs from GIPHY or Tenor. Leave this field empty to disable content filtering.

.. config:setting:: plugins-gifgfycatdisplaystyle
  :displayname: Gfycat display style (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A
  :description: Specify the display style for GIFs from Gfycat. See the `Gfycat Developer API <https://developers.gfycat.com/api/>`__ documentation for details.

Gfycat display style
~~~~~~~~~~~~~~~~~~~~

Specify the display style for GIFs from Gfycat. See the `Gfycat Developer API <https://developers.gfycat.com/api/>`__ documentation for details.

.. config:setting:: plugins-gifgiphydisplaystyle
  :displayname: GIPHY display style (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A
  :description: Specify the display style for GIFs from GIPHY. See the `GIPHY Developers Rendition Guide <https://developers.giphy.com/docs/optional-settings/>`__ for details.

GIPHY display style
~~~~~~~~~~~~~~~~~~~

Specify the display style for GIFs from GIPHY. See the `GIPHY Developers Rendition Guide <https://developers.giphy.com/docs/optional-settings/>`__ for details.

.. config:setting:: plugins-giftenordisplaystyle
  :displayname: Tenor display style (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A
  :description: Specify the display style for GIFs from Tenor. See the `Tenor API <https://tenor.com/gifapi/documentation#responseobjects-gifformat>`__ documentation for details.

Tenor display style
~~~~~~~~~~~~~~~~~~~

Specify the display style for GIFs from Tenor. See the `Tenor API <https://tenor.com/gifapi/documentation#responseobjects-gifformat>`__ documentation for details.

.. config:setting:: plugins-giflanguage
  :displayname: Language (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A
  :description: Specify the language used to search GIFs from GIPHY. See the `GIPHY Developers Language Support <https://developers.giphy.com/docs/optional-settings/#language-support>`__ documentation for details.

Language
~~~~~~~~

Specify the language used to search GIFs from GIPHY. See the `GIPHY Developers Language Support <https://developers.giphy.com/docs/optional-settings/#language-support>`__ documentation for details.

.. config:setting:: plugins-gifforcepreview
  :displayname: Force GIF preview before posting (force /gifs) (Plugins - GIF)
  :systemconsole: Plugins > GIF commands
  :configjson: N/A
  :environment: N/A

  - **true**: Enabled by default to prevent accidental posting of inappropriate GIFs from a provider that does not support content rating filtering.
  - **false**: Both ``/gif`` and ``/gifs`` slash commands are available for the GIF commands plugin on your Mattermost server.

Force GIF preview before posting (force /gifs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Enabled by default to prevent accidental posting of inappropriate GIFs from a provider that does not support content rating filtering.

**False**: Both ``/gif`` and ``/gifs`` slash commands are available for the GIF commands plugin on your Mattermost server.

----

Mattermost Boards
-----------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Mattermost Boards is an open source alternative to Trello, Notion, and Asana that's integrated from Mattermost v5.36. Boards is a project management tool that helps define, organize, track and manage work across teams, using a familiar kanban board view. See the `Mattermost Boards <https://docs.mattermost.com/guides/boards.html>`__ product documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Mattermost Boards**.

.. config:setting:: plugins-boardsenable
  :displayname: Enable plugin (Plugins - Boards)
  :systemconsole: Plugins > Mattermost Boards
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the Mattermost Boards plugin on your Mattermost workspace.
  - **false**: Disables the Mattermost Boards plugin on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

**True**: Enables the Mattermost Boards plugin on your Mattermost workspace.

**False**: Disables the Mattermost Boards plugin on your Mattermost workspace.

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
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the Mattermost Playbooks plugin on your Mattermost workspace.
  - **false**: Disables the Mattermost Playbooks plugin on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

**True**: Enables the Mattermost Playbooks plugin on your Mattermost workspace.

**False**: Disables the Mattermost Playbooks plugin on your Mattermost workspace.

.. config:setting:: plugins-playbooksenabledteams
  :displayname: Enabled teams (Plugins - Playbooks)
  :systemconsole: Plugins > Playbooks
  :configjson: N/A
  :environment: N/A
  :description: Enable Playbooks for all Mattermost teams, or for only selected teams.

Enabled teams
~~~~~~~~~~~~~

Enable Playbooks for all Mattermost teams, or for only selected teams.

.. config:setting:: plugins-playbooksexperimentalfeatures
  :displayname: Enable experimental features (Plugins - Playbooks)
  :systemconsole: Plugins > Playbooks
  :configjson: N/A
  :environment: N/A

  - **true**: Enables experimental Playbooks features on your Mattermost workspace.
  - **false**: Disables experimental Playbooks features on your Mattermost workspace.

Enable experimental features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Enables experimental Playbooks features on your Mattermost workspace.

**False**: Disables experimental Playbooks features on your Mattermost workspace.

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

  - **true**: Enables the Mattermost User Satisfaction Surveys plugin on your Mattermost workspace.
  - **false**: Disables the Mattermost User Satisfaction Surveys plugin on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

**True**: Enables the Mattermost User Satisfaction Surveys plugin on your Mattermost workspace.

**False**: Disables the Mattermost User Satisfaction Surveys plugin on your Mattermost workspace.

.. config:setting:: plugins-surveysenablesend
  :displayname: Enable user satisfaction survey (Plugins - User Satisfaction Surveys)
  :systemconsole: Plugins > User Satisfaction Surveys
  :configjson: N/A
  :environment: N/A

  - **true**: A user satisfaction survey will be sent out to all users on a quarterly basis.
  - **false**: User satisfaction surveys are disabled.

Enable user satisfaction survey
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: A user satisfaction survey will be sent out to all users on a quarterly basis. The survey results will be used by Mattermost, Inc. to improve the quality and user experience of the product. Please refer to the `Mattermost Privacy Policy <https://mattermost.com/privacy-policy/>`__ for more information on the collection and use of information received through Mattermost services.

**False**: User satisfaction surveys are disabled.

----

Zoom
----

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This plugin allows team members to initiate a Zoom meeting with a single click. All participants in a channel can easily join the Zoom meeting and the shared link is updated when the meeting is over. See the `Zoom Conferencing Plugin <https://mattermost.gitbook.io/plugin-zoom/>`__ product documentation for details.

.. note::

  To set up this plugin, you need to create a Zoom App using a Zoom Administrator account. See the `Zoom configuration <https://mattermost.gitbook.io/plugin-zoom/installation/zoom-configuration>`__ documentation for details. 

Access the following configuration settings in the System Console by going to **Plugins > Zoom**.

.. config:setting:: plugins-zoomenable
  :displayname: Enable plugin (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A

  - **true**: Enables the Zoom plugin on your Mattermost server.
  - **false**: Disables the Zoom plugin on your Mattermost server.

Enable plugin
~~~~~~~~~~~~~

**True**: Enables the Zoom plugin on your Mattermost server.

**False**: Disables the Zoom plugin on your Mattermost server.

.. config:setting:: plugins-zoomurl
  :displayname: Zoom URL (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A
  :description: Specify the URL for a self-hosted private cloud or on-premise Zoom server. Leave blank if you're using Zoom's vendor-hosted SaaS service.

Zoom URL
~~~~~~~~

Specify the URL for a self-hosted private cloud or on-premise Zoom server. For example, ``https://yourzoom.com``. Leave blank if you're using Zoom's vendor-hosted SaaS service.

.. config:setting:: plugins-zoomapiurl
  :displayname: Zoom API URL (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A
  :description: Specify the API URL for a self-hosted private cloud or on-premise Zoom server. Leave blank if you're using Zoom's vendor-hosted SaaS service.

Zoom API URL
~~~~~~~~~~~~

Specify the API URL for a self-hosted private cloud or on-premises Zoom server. For example, ``https://api.yourzoom.com/v2``. Leave blank if you're using Zoom's vendor-hosted SaaS service.

.. config:setting:: plugins-zoomoauth
  :displayname: Enable OAuth (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A

  - **true**: OAuth will be used as the authentication means with Zoom.
  - **false**: JWT will be used as the authentication means with Zoom.

Enable OAuth
~~~~~~~~~~~~

**True**: OAuth will be used as the authentication means with Zoom.

**False**: JWT will be used as the authentication means with Zoom.

.. note::

  If you are currently using a JWT Zoom application and switch to OAuth, all users will need to connect their Zoom account using OAuth the next time they try to start a meeting. See the `Zoom Configuration <https://mattermost.gitbook.io/plugin-zoom/installation/zoom-configuration>`__ documentation for details.

.. config:setting:: plugins-zoomoauthbyaccountlevel
  :displayname: OAuth by account level app (Beta) (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A

  - **true**: Only an account administrator has to log in. The rest of the users will use their e-mail to log in.
  - **false**: All users must use their e-mail to log in.

OAuth by account level app (Beta)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Only an account administrator has to log in. The rest of the users will use their email to log in.

**False**: All users must use their email to log in.

.. config:setting:: plugins-zoomoauthclientid
  :displayname: Zoom OAuth client ID (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A
  :description: Specify the Client ID for the OAuth app registered with Zoom. Leave blank if not using OAuth.

Zoom OAuth client ID
~~~~~~~~~~~~~~~~~~~~

Specify the Client ID for the OAuth app registered with Zoom. Leave blank if not using OAuth.

.. config:setting:: plugins-zoomoauthclientsecret
  :displayname: Zoom OAuth client secret (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A
  :description: Specify the Client Secret for the OAuth app registered with Zoom. Leave blank if not using OAuth.

Zoom OAuth client secret
~~~~~~~~~~~~~~~~~~~~~~~~

Specify the Client Secret for the OAuth app registered with Zoom. Leave blank if not using OAuth.

At rest token encryption key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generate an AES encryption key for Zoom OAuth Token used to encrypt stored access tokens by selecting ``Regenerate``. Regenerating the key invalidates your existing Zoom OAuth.

.. config:setting:: plugins-zoomapikey
  :displayname: API key (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A
  :description: Specify the API Key generated by Zoom used to create meetings and pull user data.

API key
~~~~~~~

Specify the API Key generated by Zoom used to create meetings and pull user data.

.. config:setting:: plugins-zoomapisecret
  :displayname: API secret (Plugins - Zoom)
  :systemconsole: Plugins > Zoom
  :configjson: N/A
  :environment: N/A
  :description: Specify the API Secret generated by Zoom for your API key.

API secret
~~~~~~~~~~

Specify the API Secret generated by Zoom for your API key.

Webhook secret
~~~~~~~~~~~~~~

Generate a secret for the webhook URL endpoint used to authenticate the webhook to Mattermost. Regenerating the secret invalidates your existing Zoom plugin.

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
