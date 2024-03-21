Integrations configuration settings
===================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Both self-hosted and Cloud admins can access the following configuration settings in **System Console > Integrations**. Self-hosted admins can also edit the ``config.json`` file as described in the following tables.

- `Integrations management <#integrations-management>`__
- `Bot Accounts <#bot-acocunts>`__
- `GIF (beta) <#gif-beta>`__
- `CORS <#cors>`__

----

Integrations management
-----------------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Integrations > Integration Management**.

.. config:setting:: integrate-enableincomingwebhooks
  :displayname: Enable incoming webhooks (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnableIncomingWebhooks
  :environment: MM_SERVICESETTINGS_ENABLEINCOMINGWEBHOOKS

  - **true**: **(Default)** Incoming webhooks are allowed. To manage incoming webhooks, select **Integrations** from the Mattermost Product menu.
  - **false**: The **Integrations > Incoming Webhooks** section of the Mattermost Product menu is hidden and all incoming webhooks are disabled.

Enable incoming webhooks
~~~~~~~~~~~~~~~~~~~~~~~~

Developers building integrations can create webhook URLs for public channels and private channels. Please see our `documentation page <https://developers.mattermost.com/integrate/webhooks/incoming/>`__ to learn about creating webhooks, viewing samples, and letting community know about integrations you've built.

**True**: Incoming webhooks are allowed. To manage incoming webhooks, select **Integrations** from the Mattermost Product menu. The webhook URLs created can be used by external applications to create posts in any public or private channels that you have access to.

**False**: The **Integrations > Incoming Webhooks** section of the Mattermost Product menu is hidden and all incoming webhooks are disabled.

.. important::
   Security note: By enabling this feature, users may be able to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`__ by attempting to impersonate other users. To combat these attacks, a BOT tag appears next to all posts from a webhook. Enable at your own risk.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableIncomingWebhooks": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

.. config:setting:: integrate-enableoutgoingwebhooks
  :displayname: Enable outgoing webhooks (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnableOutgoingWebhooks
  :environment: MM_SERVICESETTINGS_ENABLEOUTGOINGWEBHOOKS

  - **true**: **(Default)** Outgoing webhooks will be allowed. To manage outgoing webhooks, select **Integrations** from the Mattermost Product menu.
  - **false**: The **Integrations > Outgoing Webhooks** of the Mattermost Product menu is hidden and all outgoing webhooks are disabled.

Enable outgoing webhooks
~~~~~~~~~~~~~~~~~~~~~~~~

Developers building integrations can create webhook tokens for public channels. Trigger words are used to fire new message events to external integrations. For security reasons, outgoing webhooks are only available in public channels. Please see our `documentation page <https://developers.mattermost.com/integrate/webhooks/outgoing/>`__ to learn about creating webhooks and viewing samples.

**True**: Outgoing webhooks will be allowed. To manage outgoing webhooks, select **Integrations** from the Mattermost Product menu.

**False**: The **Integrations > Outgoing Webhooks** of the Mattermost Product menu is hidden and all outgoing webhooks are disabled.

.. important::
   Security note: By enabling this feature, users may be able to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`__ by attempting to impersonate other users. To combat these attacks, a BOT tag appears next to all posts from a webhook. Enable at your own risk.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOutgoingWebhooks": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

.. config:setting:: integrate-enablecustomslashcommands
  :displayname: Enable custom slash commands (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnableCommands
  :environment: MM_SERVICESETTINGS_ENABLECOMMANDS

  - **true**: Allow users to create custom slash commands from **Main Menu > Integrations > Commands**.
  - **false**: **(Default)** Slash commands are hidden in the **Integrations** user interface.

Enable custom slash commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Slash commands send events to external integrations that send a response back to Mattermost.

**True**: Allow users to create custom slash commands from **Main Menu > Integrations > Commands**.

**False**: Slash commands are hidden in the **Integrations** user interface.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCommands": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

.. config:setting:: integrate-enableoauthserviceprovider
  :displayname: Enable OAuth 2.0 service provider (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnableOAuthServiceProvider
  :environment: MM_SERVICESETTINGS_ENABLEOAUTHSERVICEPROVIDER

  - **true**: **(Default)** Mattermost acts as an OAuth 2.0 service provider allowing Mattermost to authorize API requests from external applications.
  - **false**: Mattermost does not function as an OAuth 2.0 service provider.

Enable OAuth 2.0 service provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Mattermost acts as an OAuth 2.0 service provider allowing Mattermost to authorize API requests from external applications.

**False**: Mattermost does not function as an OAuth 2.0 service provider.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOAuthServiceProvider": true`` with options ``true`` and ``false``.  |
+------------------------------------------------------------------------------------------------------------------------+

.. note::

  Cloud admins can't modify this configuration setting.

.. config:setting:: integrate-request-timeout
  :displayname: Integration request timeout (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.OutgoingIntegrationRequestsDefaultTimeout
  :environment: MM_SERVICESETTINGS_OUTGOINGINTEGRATIONREQUESTDEFAULTTIMEOUT
  :description: The number of seconds to wait for external integration HTTP requests, before timing out. Default value is **30 seconds**.

Integration request timeout
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The number of seconds to wait for external integration HTTP requests, before timing out, including `custom slash commands <https://developers.mattermost.com/integrate/slash-commands/custom/>`__, `outgoing webhooks <https://developers.mattermost.com/integrate/webhooks/outgoing/>`__, `interactive messages <https://developers.mattermost.com/integrate/plugins/interactive-messages/>`__, and `interactive dialogs <https://developers.mattermost.com/integrate/plugins/interactive-dialogs/>`__. Increase this value if you have external integrations that can take some time to generate an HTTP response, or experience delayed responses due to latency.

+------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"OutgoingIntegrationRequestsDefaultTimeout": 30``. |
+------------------------------------------------------------------------------------------------+

.. config:setting:: integrate-enableusernameoverride
  :displayname: Enable integrations to override usernames (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnablePostUsernameOverride
  :environment: MM_SERVICESETTINGS_ENABLEPOSTUSERNAMEOVERRIDE

  - **true**: Webhooks, slash commands, OAuth 2.0 apps, and other integrations will be allowed to change the username they are posting as.
  - **false**: **(Default)** Custom slash commands can only post as the username of the user who used the slash command.

Enable integrations to override usernames
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Webhooks, slash commands, OAuth 2.0 apps, and other integrations, will be allowed to change the username they are posting as. If no username is present, the username for the post is the same as it would be for a setting of ``False``.

**False**: **(Default)** Custom slash commands can only post as the username of the user who used the slash command. OAuth 2.0 apps can only post as the username of the user who set up the integration. For incoming webhooks and outgoing webhooks, the username is "webhook". See https://developers.mattermost.com/integrate/other-integrations/ for more details.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostUsernameOverride": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: integrate-enableiconoverride
  :displayname: Enable integrations to override profile picture icons (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnablePostIconOverride
  :environment: MM_SERVICESETTINGS_ENABLEPOSTICONOVERRIDE

  - **true**: Webhooks, slash commands, and other integrations, such as `Zapier <https://docs.mattermost.com/integrations/zapier.html>`__, will be allowed to change the profile picture they post with.
  - **false**: **(Default)** Webhooks, slash commands, and OAuth 2.0 apps can only post with the profile picture of the account they were set up with.

Enable integrations to override profile picture icons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Webhooks, slash commands, and other integrations, will be allowed to change the profile picture they post with.

**False**: **(Default)** Webhooks, slash commands, and OAuth 2.0 apps can only post with the profile picture of the account they were set up with. See https://developers.mattermost.com/integrate/other-integrations/ for more details.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostIconOverride": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

.. config:setting:: integrate-enableuseraccesstokens
  :displayname: Enable personal access tokens (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnableUserAccessTokens
  :environment: MM_SERVICESETTINGS_ENABLEUSERACCESSTOKENS

  - **true**: Users can create `personal access tokens <https://developers.mattermost.com/integrate/admin-guide/admin-personal-access-token/>`__ for integrations in **Profile > Security**.
  - **false**: **(Default)** Personal access tokens are disabled on the server.

Enable personal access tokens
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Users can create `personal access tokens <https://developers.mattermost.com/integrate/admin-guide/admin-personal-access-token/>`__ for integrations in **Profile > Security**. They can be used to authenticate against the API and give full access to the account.

To manage who can create personal access tokens or to search users by token ID, go to the **System Console > Users** page.

**False**: Personal access tokens are disabled on the server.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserAccessTokens": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

----

Bot accounts
------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Integrations > Bot Accounts**.

.. config:setting:: integrate-enablebotaccounts
  :displayname: Enable bot account creation (Integrations)
  :systemconsole: Integrations > Bot Accounts
  :configjson: .ServiceSettings.EnableBotAccountCreation
  :environment: MM_SERVICESETTINGS_ENABLEBOTACCOUNTCREATION

  - **true**: Users can create bot accounts for integrations in **Integrations > Bot Accounts**.
  - **false**: **(Default)** Bot accounts cannot be created through the user interface or the RESTful API.

Enable bot account creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: **(Default for Cloud deployments)** Users can create bot accounts for integrations in **Integrations > Bot Accounts**. Bot accounts are similar to user accounts except they cannot be used to log in. See `documentation <https://developers.mattermost.com/integrate/admin-guide/admin-bot-accounts/>`__ to learn more.

**False**: **(Default for self-hosted deployments)** Bot accounts cannot be created through the user interface or the RESTful API. Plugins can still create and manage bot accounts.

+----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableBotAccountCreation": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------+

.. config:setting:: integrate-disablebotswhenownerisdeactivated
  :displayname: Disable bot accounts when owner is deactivated (Integrations)
  :systemconsole: Integrations > Bot Accounts
  :configjson: .ServiceSettings.DisableBotsWhenOwnerIsDeactivated
  :environment: MM_SERVICESETTINGS_DISABLEBOTSWHENOWNERISDEACTIVATED

  - **true**: When a user is deactivated, disables all bot accounts managed by the user.
  - **false**: **(Default)** When a user is deactivated, all bot accounts managed by the user remain active.

Disable bot accounts when owner is deactivated
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: When a user is deactivated, disables all bot accounts managed by the user. To re-enable bot accounts, go to **Integrations > Bot Accounts**.

**False**: When a user is deactivated, all bot accounts managed by the user remain active.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DisableBotsWhenOwnerIsDeactivated": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------+

----

GIF (Beta)
----------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Integrations > GIF (Beta)**.

.. config:setting:: integrate-enablegifpicker
  :displayname: Enable GIF picker (Integrations)
  :systemconsole: Integrations > GIF (Beta)
  :configjson: .ServiceSettings.EnableGifPicker
  :environment: MM_SERVICESETTINGS_ENABLEGIFPICKER

  - **true**: **(Default)** Allow users to select GIFs from the emoji picker via a Gfycat integration.
  - **false**: GIFs cannot be selected in the emoji picker.

Enable GIF picker
~~~~~~~~~~~~~~~~~

**True**: Allow users to select GIFs from the emoji picker via a Gfycat integration.

**False**: GIFs cannot be selected in the emoji picker.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableGifPicker": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

.. note::
   :ref:`Link previews <configure/site-configuration-settings:enable message link previews>` must be enabled in order to display GIF link previews. Mattermost deployments restricted to access behind a firewall must open port 443 to both https://api.gfycat.com/v1 and https://gfycat.com/<id> (for all request types) for this feature to work.

.. config:setting:: integrate-gfycatapikey
  :displayname: Gfycat API key (Integrations)
  :systemconsole: Integrations > GIF (Beta)
  :configjson: .ServiceSettings.GfycatAPIKey
  :environment: MM_SERVICESETTINGS_GFYCATAPIKEY
  :description: The Gfycat API key. Default value is **2_KtH_W5**.

Gfycat API key
~~~~~~~~~~~~~~

When blank, uses the default API key provided by Gfycat. Alternatively, a unique API key can be requested at https://developers.gfycat.com/signup/#/. Enter the client ID you receive via email to this field.

+-----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GfycatApiKey": "2_KtH_W5"`` with string input.   |
+-----------------------------------------------------------------------------------------------+

.. config:setting:: integrate-gfycatapisecret
  :displayname: Gfycat API secret (Integrations)
  :systemconsole: Integrations > GIF (Beta)
  :configjson: .ServiceSettings.GfycatAPISecret
  :environment: MM_SERVICESETTINGS_GFYCATAPISECRET
  :description: The API secret generated by Gfycat for your API key. Default value is **3wLVZPiswc3DnaiaFoLkDvB4X0IV6CpMkj4tf2inJRsBY6-FnkT08zGmppWFgeof**.

Gfycat API secret
~~~~~~~~~~~~~~~~~

The API secret generated by Gfycat for your API key. When blank, uses the default API secret provided by Gfycat.

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GfycatApiSecret": "3wLVZPiswc3DnaiaFoLkDvB4X0IV6CpMkj4tf2inJRsBY6-FnkT08zGmppWFgeof"`` with string input.  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

----

CORS
----

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Integrations > CORS**.

.. config:setting:: integrate-allowcorsfrom
  :displayname: Enable cross-origin requests from (Integrations)
  :systemconsole: Integrations > CORS
  :configjson: .ServiceSettings.AllowCorsFrom
  :environment: MM_SERVICESETTINGS_ALLOWCORSFROM
  :description: Enable HTTP cross-origin requests from all, none, or specific domains.

Enable cross-origin requests from
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable HTTP cross-origin requests from specific domains.

- Type ``*`` to allow CORS from any domain.
- Enter a specific domain or multiple domains separated by spaces.
- Type ``null`` to prevent CORS from any domain.
- Leave blank to disable it and use the Mattermost **Site URL** instead.

.. note::

  Ensure you've entered your :ref:`Site URL <configure/environment-configuration-settings:site url>` before enabling this setting to prevent losing access to the System Console after saving. If you lose access to the System Console after changing this setting, you can set your Site URL through the ``config.json`` file.

+--------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowCorsFrom": ""`` with string input. |
+--------------------------------------------------------------------------------------+

.. config:setting:: integrate-corsexposedheaders
  :displayname: CORS exposed headers (Integrations)
  :systemconsole: Integrations > CORS
  :configjson: .ServiceSettings.CorsExposedHeaders
  :environment: MM_SERVICESETTINGS_CORSEXPOSEDHEADERS
  :description: Whitelist of headers that will be accessible to the requester.

CORS exposed headers
~~~~~~~~~~~~~~~~~~~~

Whitelist of headers that will be accessible to the requester.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CorsExposedHeaders": ""`` with string input. |
+-------------------------------------------------------------------------------------------+

.. config:setting:: integrate-corsallowcredentials
  :displayname: CORS allow credentials (Integrations)
  :systemconsole: Integrations > CORS
  :configjson: .ServiceSettings.CorsAllowCredentials
  :environment: MM_SERVICESETTINGS_CORSALLOWCREDENTIALS

  - **true**: Requests that pass validation will include the ``Access-Control-Allow-Credentials`` header.
  - **false**: **(Default)** Requests won't include the ``Access-Control-Allow-Credentials`` header.

CORS allow credentials
~~~~~~~~~~~~~~~~~~~~~~

**True**: Requests that pass validation will include the ``Access-Control-Allow-Credentials`` header.

**False**: Requests won't include the ``Access-Control-Allow-Credentials`` header.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CorsAllowCredentials": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

.. config:setting:: integrate-corsdebug
  :displayname: CORS debug (Integrations)
  :systemconsole: Integrations > CORS
  :configjson: .ServiceSettings.CorsDebug
  :environment: MM_SERVICESETTINGS_CORSDEBUG

  - **true**: Prints messages to the logs to help when developing an integration that uses CORS.
  - **false**: **(Default)** Debug messages not printed to the logs.

CORS debug
~~~~~~~~~~

**True**: Prints messages to the logs to help when developing an integration that uses CORS. These messages will include the structured key value pair ``"source": "cors"``.

**False**: Debug messages not printed to the logs.

+-------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CorsDebug": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------+
