:orphan:

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 25
  :target: https://mattermost.com/sign-up
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 25
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

:nosearch:

Access the following configuration settings in the System Console by going to **Plugins**.

Plugin Management
~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Plugins > Plugin Management**.

Enable Plugins
^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: Enables plugins on your Mattermost server. Use plugins to integrate with third-party systems, extend functionality, or customize the user interface of your Mattermost server. See `documentation <https://developers.mattermost.com/integrate/admin-guide/admin-plugins-beta/>`__ to learn more.

**False**: Disables plugins on your Mattermost server.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------+

Require Plugin Signature
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: Require valid plugin signatures before starting managed or unmanaged plugins. Pre-packaged plugins are not subject to plugin signature verification. Plugins installed through the Plugin Marketplace are always subject to plugin signature verification at the time of download.

**False**: Don't require valid plugin signatures before starting managed or unmanaged plugins. Pre-packaged plugins are not subject to plugin signature verification. Plugins installed through the Plugin Marketplace are always subject to plugin signature verification at the time of download.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RequirePluginSignature": true`` with options ``true`` and ``false``.   |
+---------------------------------------------------------------------------------------------------------------------+

Automatic Prepackaged Plugins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: Any pre-packaged plugins enabled in the configuration will be installed or upgraded automatically. If a newer version is already installed, no changes are made.

**False**: Pre-packaged plugins aren't installed or upgraded automatically but may be installed manually from the Plugin Marketplace, even when offline.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AutomaticPrepackagedPlugins": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

Enable Marketplace
^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: Enables Plugin Marketplace on your Mattermost server for all System Admins.

**False**: Disables Plugin Marketplace on your Mattermost server for all System Admins.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableMarketplace": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

Enable Remote Marketplace
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: The server will attempt to connect to the configured Plugin Marketplace to show the latest plugins. If the connection fails, the Plugin Marketplace shows only pre-packaged and already installed plugins alongside a connection error.

**False**: The server won't attempt to connect to a remote marketplace, and will show only pre-packaged and already installed plugins. Use this setting if your server can't connect to the internet.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableRemoteMarketplace": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

This setting only takes effect when ``"EnableMarketplace": true``.

.. note::
   For the Remote Marketplace to operate, each host running the Mattermost service requires network access to the marketplace service endpoint (hosted at ``https://api.integrations.mattermost.com``, see `Marketplace URL <#marketplace-url>`__ ).

Marketplace URL
^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

If the Marketplace is enabled, this setting specifies which URL should be used to query for new Marketplace plugins.

+------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MarketplaceUrl": "https://api.integrations.mattermost.com"`` with string input. |
+------------------------------------------------------------------------------------------------------------------------------+

Installed Plugin State
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

Lists installed plugins on your Mattermost server and whether they are enabled. Pre-packaged plugins are installed by default and can be deactivated, but not removed.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PluginStates": {}`` with object input mapping plugin IDs as keys to objects, each of which contains a key ``"Enable": false`` with options ``true`` or ``false``. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Plugin Settings
^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

Settings specific to each Mattermost plugin.

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Plugins": {}`` with object input mapping plugin IDs as keys to objects containing plugin-specific data. |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

Agenda
~~~~~~~

Access the following configuration settings in the System Console by going to **Plugins > Agenda**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |self-hosted|

**True**: Enables the Agenda plugin on your Mattermost server.

**False**: Disables the Agenda plugin on your Mattermost server.

Antivirus
~~~~~~~~~~

This plugin allows the forwarding of uploaded files to an antivirus scanning application, `ClamAV anti-virus software <https://www.clamav.net/>`__, and prevents the upload from completing if there is a virus detected in the file. 

Use this plugin to prevent users from inadvertently spreading malware or viruses via your Mattermost server. See the `Mattermost Antivirus Plugin <https://github.com/mattermost/mattermost-plugin-antivirus>`__ documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Antivirus**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |self-hosted|

**True**: Enables the Antivirus plugin on your Mattermost server.

**False**: Disables the Antivirus plugin on your Mattermost server.

ClamAV - Host and Port
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

Specify the hostname and port to connect to the ClamAV server.

Scan Timeout (seconds)
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

Specify how long the virus scan can take before timing out.

Apps
~~~~

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |cloud|

**True**: Enables the Apps plugin on your Mattermost server.

**False**: Disables the Apps plugin on your Mattermost server.

To create your own Mattermost App, see the `Mattermost Apps <https://developers.mattermost.com/integrate/apps/>`__ developer documentation.

Autolink
~~~~~~~~~

This plugin creates regular expression (regexp) patterns that are reformatted into a Markdown link before the message is saved into the database. System Admins can configure this plugin in the ``config.json`` file, using the ``/autolink`` slash command (when enabled), or through using the System Console. See the `Autolink Plugin <https://github.com/mattermost/mattermost-plugin-autolink/blob/master/README.md>`__ documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Autolink**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |self-hosted|

**True**: Enables the Autolink plugin on your Mattermost server.

**False**: Disables the Autolink plugin on your Mattermost server.

Enable administration with /autolink command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

**True**: Enables the ability to configure the Apps plugin using the ``/autolink`` slash command.

**False**: Disables the ability to use the slash command to configure the plugin.

Apply plugin to updated posts as well as new posts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

**True**: Applies the plugin to updated posts as well as new posts. 

**False**: Applies the plugin to new posts only.

Admin User IDs
^^^^^^^^^^^^^^

|all-plans| |self-hosted|

Specify users authorized to administer the plugin in addition to System Admins. Separate multiple user IDs with commas.

.. tip::
  Find user IDs by going to **System Console > User Management > Users**.

AWS SNS
~~~~~~~~

This plugin is used to receive alert notifications from `Amazon AWS CloudWatch <https://aws.amazon.com/cloudwatch/>`__ to Mattermost channels via `AWS Simple Notification Server (SNS) <https://docs.aws.amazon.com/sns/latest/dg/welcome.html>`__. 

Access the following configuration settings in the System Console by going to **Plugins > AWS SNS**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |self-hosted|

**True**: Enables the AWS SNS plugin on your Mattermost server.

**False**: Disables the AWS SNS plugin on your Mattermost server.

Channel to send notifications to
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

Specify the channel to send notifications to in the format ``teamname,channelname``. For example, for a channel with a URL of ``https://example.com/myteam/channels/mychannel``, set the value to ``myteam,mychannel``. If the specified channel does not exist, the plugin creates the channel for you.

Authorized User IDs
^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

Specify users authorized to accept AWS SNS subscriptions to a Mattermost channel. Separate multiple user IDs with commas.

.. tip::
  Find user IDs by going to **System Console > User Management > Users**.

Token
^^^^^

|all-plans| |self-hosted|

Generate a token to validate incoming requests from AWS SNS by selecting ``Regenerate``.

Calls (beta)
~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Plugins > Calls**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |self-hosted| |cloud|

**True**: Enables the calls plugin on your Mattermost workspace.

**False**: Disables the calls plugin on your Mattermost workspace.

RTC Server Port
^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

The UDP port the RTC server will listen on. All calls traffic will be served through this port. The Default setting is 8443.

Changing this setting requires a plugin restart to take effect.

Enable on specific channels
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

**True**: Allow Channel Admins to enable or disable calls on specific channels. It also allows participants in DMs/GMs to enable or disable calls.

**False**: Only System Admins will be able to enable or disable calls on specific channels.

Enable on all channels
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

**True**: Enable calls by default on all channels.

**False**: Calls have to be explicitly enabled on channels.

Max call participants
^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

The maximum number of participants that can join a single call. This is an optional field and default is 0 (unlimited). The maximum recommended setting is 200.

ICE Host Override
^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

An optional override to the host that gets advertised to clients when connecting to calls. Depending on the network infrastructure (e.g. instance behind a NAT device) it may be necessary to set this field to the client facing external IP in order to let clients connect successfully. When empty or unset, the RTC service will attempt to automatically find the instance's public IP through STUN.

This is an optional field. Changing this setting requires a plugin restart to take effect.

ICE Servers Configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

A list of ICE servers (STUN/TURN) to be used by the service. Value should be valid JSON.

Default is ``[{"urls": ["stun:stun.global.calls.mattermost.com:3478"]}]``

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

This is an optional field. Changing this setting may require a plugin restart to take effect.

TURN Static Auth Secret
^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

A static secret used to generate short-lived credentials for TURN servers.

This is an optional field.

TURN Credentials Expiration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

The expiration, in minutes, of the short-lived credentials generated for TURN servers.

Server Side TURN
^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

**True**: The RTC server will use the configured TURN candidates for server-initiated connections.

**False**: TURN will be used only on the client-side.

Changing this setting requires a plugin restart to take effect.

RTCD Service URL
^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

The URL to a running `rtcd <https://github.com/mattermost/rtcd>`__ service instance that will host the calls. When set (non empty) all the calls will be handled by this external service.

This is an optional field. Changing this setting requires a plugin restart to take effect.

Channel Export
~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Plugins > Channel Export**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: Enables the Channel Export plugin on your Mattermost workspace.

**False**: Disables the Channel Export plugin on your Mattermost workspace.

Demo Plugin
~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Plugins > Demo Plugin**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |self-hosted|

**True**: Enables the Demo plugin on your Mattermost workspace.

**False**: Disables the Demo plugin on your Mattermost workspace.

Channel Name
^^^^^^^^^^^^

|all-plans| |self-hosted|

Specify the channel to use as part of the demo plugin. If the specified channel does not exist, the plugin creates the channel for you.

Username
^^^^^^^^

|all-plans| |self-hosted|

Specify the user to use as part of the demo plugin. If the specified user does not exist, the plugin creates the user for you.

GIF commands
~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Plugins > GIF commands**.

This plugin is used to post GIFs from Gfycat, Giphy, or Tenor using slash commands.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |self-hosted|

**True**: Enables the GIF commands plugin on your Mattermost server.

**False**: Disables the GIF commands plugin on your Mattermost server.

Display the GIF as
^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

Display the GIF as an embedded image where the GIF can't be collapsed, or as a collapsible image preview where the full URL displays. 

.. note::
   `Link previews <https://docs.mattermost.com/configure/configuration-settings.html#enable-link-previews>`__ must be enabled in order to display GIF link previews. Mattermost deployments restricted to access behind a firewall must open port 443 to both ``https://api.gfycat.com/v1`` and ``https://gfycat.com/<id>`` (for all request types) for this feature to work.

GIF Provider
^^^^^^^^^^^^^

|all-plans| |self-hosted|

Specify the GIF provider as GIPHY, Tenor, or Gfycat.

.. note::
  Selecting GIPHY or Tenor requires an API Key for this feature to work. An API key is not required for Gfycat.

Giphy/Tenor API Key
^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

Configure your own API Key when specifying the GIF Provider as GIPHY or Tenor. An API key is not required for Gfycat. 

To get your own API key, see the `GIPHY Developers Quick Start <https://developers.giphy.com/docs/api/#quick-start-guide>`__ documentation, or the `Tenor Developer <https://tenor.com/developer/keyregistration>`__ documentation for details.

Content Rating (GIPHY & Tenor only)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

Select an `MPAA-style content rating <https://en.wikipedia.org/wiki/Motion_Picture_Association_film_rating_system>`__ for GIFs from GIPHY or Tenor. Leave this field empty to disable content filtering.

Gfycat display style
^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

Specify the display style for GIFs from Gfycat. See the `Gfycat Developer API <https://developers.gfycat.com/api/>`__ documentation for details.

GIPHY display style
^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

Specify the display style for GIFs from GIPHY. See the `GIPHY Developers Rendition Guide <https://developers.giphy.com/docs/optional-settings/>`__ for details.

Tenor display style
^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

Specify the display style for GIFs from Tenor. See the `Tenor API <https://tenor.com/gifapi/documentation#responseobjects-gifformat>`__ documentation for details.

Language
^^^^^^^^

|all-plans| |self-hosted|

Specify the language used to search GIFs from GIPHY. See the `GIPHY Developers Language Support <https://developers.giphy.com/docs/optional-settings/#language-support>`__ documentation for details.

Force GIF preview before posting (force /gifs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

**True**: Enabled by default to prevent accidental posting of inappropriate GIFs from a provider that does not support content rating filtering.

**False**: Both ``/gif`` and ``/gifs`` slash commands are available for the GIF commands plugin on your Mattermost server.

Mattermost Boards
~~~~~~~~~~~~~~~~~

Mattermost Boards is an open source alternative to Trello, Notion, and Asana that's integrated from Mattermost v5.36. Boards is a project management tool that helps define, organize, track and manage work across teams, using a familiar kanban board view. See the `Mattermost Boards <https://docs.mattermost.com/guides/boards.html>`__ product documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Mattermost Boards**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: Enables the Mattermost Boards plugin on your Mattermost workspace.

**False**: Disables the Mattermost Boards plugin on your Mattermost workspace.

Mattermost Playbooks
~~~~~~~~~~~~~~~~~~~~

Mattermost Playbooks is an open source, self-hosted collaboration tool for teams. Each playbook represents a recurring outcome or specific goal that your teams collaborate on to achieve, such as service outage recovery or customer onboarding. Teams run a playbook every time they want to orchestrate people, tools, and data to achieve that outcome as quickly as possible while providing visibility to stakeholders. Playbooks also allow teams to incorporate learnings from the retrospective to tweak and improve the playbook with every iteration. See the `Mattermost Playbooks <https://docs.mattermost.com/guides/playbooks.html>`__ documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Playbooks**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: Enables the Mattermost Playbooks plugin on your Mattermost workspace.

**False**: Disables the Mattermost Playbooks plugin on your Mattermost workspace.

Enabled Teams
^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

Enable Playbooks for all Mattermost teams, or for only selected teams.

Enable Experimental Features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: Enables experimental Playbooks features on your Mattermost workspace.

**False**: Disables experimental Playbooks features on your Mattermost workspace.

User Satisfaction Surveys
~~~~~~~~~~~~~~~~~~~~~~~~~

This plugin enables Mattermost to send user satisfaction surveys to gather feedback and improve product quality directly from your Mattermost users. Please refer to the `Mattermost Privacy Policy <https://mattermost.com/privacy-policy/>`__ for more information on the collection and use of information received through Mattermost services.

Access the following configuration settings in the System Console by going to **Plugins > User Satisfaction Surveys**.

Enable Plugin
^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: Enables the Mattermost Playbooks plugin on your Mattermost workspace.

**False**: Disables the Mattermost Playbooks plugin on your Mattermost workspace.

Enable User Satisfaction Survey
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: A user satisfaction survey will be sent out to all users on a quarterly basis. The survey results will be used by Mattermost, Inc. to improve the quality and user experience of the product. Please refer to the `Mattermost Privacy Policy <https://mattermost.com/privacy-policy/>`__ for more information on the collection and use of information received through Mattermost services.

**False**: User satisfaction surveys are disabled. 

Zoom
~~~~

This plugin allows team members to initiate a Zoom meeting with a single click. All participants in a channel can easily join the Zoom meeting and the shared link is updated when the meeting is over. See the `Zoom Conferencing Plugin <https://mattermost.gitbook.io/plugin-zoom/>`__ product documentation for details.

.. note::
  To set up this plugin, you need to create a Zoom App using a Zoom Administrator account. See the `Zoom Configuration <https://mattermost.gitbook.io/plugin-zoom/installation/zoom-configuration>`__ documentation for details. 

Access the following configuration settings in the System Console by going to **Plugins > Zoom**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |self-hosted|

**True**: Enables the Zoom plugin on your Mattermost server.

**False**: Disables the Zoom plugin on your Mattermost server.

Zoom URL
^^^^^^^^

|all-plans| |self-hosted|

Specify the URL for a self-hosted private cloud or on-premise Zoom server. For example, ``https://yourzoom.com``. Leave blank if you're using Zoom's vendor-hosted SaaS service.

Zoom API URL
^^^^^^^^^^^^^

|all-plans| |self-hosted|

Specify the API URL for a self-hosted private cloud or on-premise Zoom server. For example, ``https://api.yourzoom.com/v2``. Leave blank if you're using Zoom's vendor-hosted SaaS service.

Enable OAuth
^^^^^^^^^^^^

|all-plans| |self-hosted|

**True**: OAuth will be used as the authentication means with Zoom.

**False**: JWT will be used as the authentication means with Zoom.

.. note::

  If you are currently using a JWT Zoom application and switch to OAuth, all users will need to connect their Zoom account using OAuth the next time they try to start a meeting. See the `Zoom Configuration <https://mattermost.gitbook.io/plugin-zoom/installation/zoom-configuration>`__ documentation for details.

OAuth by Account Level App (Beta)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

**True**: Only an account administrator has to log in. The rest of the users will use their e-mail to log in.

**False**: All users must use their e-mail to log in.

Zoom OAuth Client ID
^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

Specify the Client ID for the OAuth app registered with Zoom. Leave blank if not using OAuth.

Zoom OAuth Client Secret
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

Specify the Client Secret for the OAuth app registered with Zoom. Leave blank if not using OAuth.

At Rest Token Encryption Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

Generate an AES encryption key for Zoom OAuth Token used to encrypt stored access tokens by selecting ``Regenerate``. Regenerating the key invalidates your existing Zoom OAuth.

API Key
^^^^^^^

|all-plans| |self-hosted|

Specify the API Key generated by Zoom used to create meetings and pull user data.

API Secret
^^^^^^^^^^

|all-plans| |self-hosted|

Specify the API Secret generated by Zoom for your API key.

Webhook Secret
^^^^^^^^^^^^^^

|all-plans| |self-hosted|

Generate a secret for the webhook URL endpoint used to authenticate the webhook to Mattermost. Regenerating the secret invalidates your existing Zoom plugin.

Signature Public Key Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

This setting isn't available in the System Console and can only be set in ``config.json``.

In addition to the Mattermost plugin signing key built into the server, each public key specified here is trusted to validate plugin signatures.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SignaturePublicKeyFiles": {}`` with string array input consisting of contents that are relative or absolute paths to signature files.              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Chimera OAuth Proxy URL
^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

This setting isn't available in the System Console and can only be set in ``config.json``.

Specify the `Chimera <https://github.com/mattermost/chimera>`__ URL used by Mattermost plugins to connect with pre-created OAuth applications.

+-------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ChimeraOAuthProxyUrl": {}`` with string input.                             |
+-------------------------------------------------------------------------------------------------------------------------+