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
  :configjson: EnableIncomingWebhooks
  :environment: N/A

  - **true**: **(Default)** Incoming webhooks are allowed. To manage incoming webhooks, select **Integrations** from the Mattermost Product menu.
  - **false**: The **Integrations > Incoming Webhooks** section of the Mattermost Product menu is hidden and all incoming webhooks are disabled.

Enable incoming webhooks
~~~~~~~~~~~~~~~~~~~~~~~~

Developers building integrations can create webhook URLs for Public channels and Private channels. Please see our `documentation page <https://docs.mattermost.com/developer/webhooks-incoming.html>`__ to learn about creating webhooks, viewing samples, and letting community know about integrations you've built.

**True**: Incoming webhooks are allowed. To manage incoming webhooks, select **Integrations** from the Mattermost Product menu. The webhook URLs created can be used by external applications to create posts in any Public or Private channels that you have access to.

**False**: The **Integrations > Incoming Webhooks** section of the Mattermost Product menu is hidden and all incoming webhooks are disabled.

.. important::
   Security note: By enabling this feature, users may be able to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`__ by attempting to impersonate other users. To combat these attacks, a BOT tag appears next to all posts from a webhook. Enable at your own risk.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableIncomingWebhooks": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

.. config:setting:: integrate-enableoutgoingwebhooks
  :displayname: Enable outgoing webhooks (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: EnableOutgoingWebhooks
  :environment: N/A

  - **true**: **(Default)** Outgoing webhooks will be allowed. To manage outgoing webhooks, select **Integrations** from the Mattermost Product menu.
  - **false**: The **Integrations > Outgoing Webhooks** of the Mattermost Product menu is hidden and all outgoing webhooks are disabled.

Enable outgoing webhooks
~~~~~~~~~~~~~~~~~~~~~~~~

Developers building integrations can create webhook tokens for Public channels. Trigger words are used to fire new message events to external integrations. For security reasons, outgoing webhooks are only available in Public channels. Please see our `documentation page <https://docs.mattermost.com/developer/webhooks-outgoing.html>`__ to learn about creating webhooks and viewing samples.

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
  :configjson: EnableCommands
  :environment: N/A

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
  :configjson: EnableOAuthServiceProvider
  :environment: N/A

  - **true**: Mattermost acts as an OAuth 2.0 service provider allowing Mattermost to authorize API requests from external applications.
  - **false**: **(Default)** Mattermost does not function as an OAuth 2.0 service provider.

Enable OAuth 2.0 service provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Mattermost acts as an OAuth 2.0 service provider allowing Mattermost to authorize API requests from external applications.

**False**: Mattermost does not function as an OAuth 2.0 service provider.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOAuthServiceProvider": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: integrate-enableusernameoverride
  :displayname: Enable integrations to override usernames (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: EnablePostUsernameOverride
  :environment: N/A

  - **true**: Webhooks, slash commands, OAuth 2.0 apps, and other integrations such as `Zapier <https://docs.mattermost.com/integrations/zapier.html>`__, will be allowed to change the username they are posting as.
  - **false**: **(Default)** Custom slash commands can only post as the username of the user who used the slash command.

Enable integrations to override usernames
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Webhooks, slash commands, OAuth 2.0 apps, and other integrations such as `Zapier <https://docs.mattermost.com/integrations/zapier.html>`__, will be allowed to change the username they are posting as. If no username is present, the username for the post is the same as it would be for a setting of ``False``.

**False**: Custom slash commands can only post as the username of the user who used the slash command. OAuth 2.0 apps can only post as the username of the user who set up the integration. For incoming webhooks and outgoing webhooks, the username is "webhook". See https://developers.mattermost.com/integrate/other-integrations/ for more details.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostUsernameOverride": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: integrate-enableiconoverride
  :displayname: Enable integrations to override profile picture icons (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: EnablePostIconOverride
  :environment: N/A

  - **True**: Webhooks, slash commands, and other integrations, such as `Zapier <https://docs.mattermost.com/integrations/zapier.html>`__, will be allowed to change the profile picture they post with.
  - **False**: Webhooks, slash commands, and OAuth 2.0 apps can only post with the profile picture of the account they were set up with.

Enable integrations to override profile picture icons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Webhooks, slash commands, and other integrations, such as `Zapier <https://docs.mattermost.com/integrations/zapier.html>`__, will be allowed to change the profile picture they post with.

**False**: Webhooks, slash commands, and OAuth 2.0 apps can only post with the profile picture of the account they were set up with. See https://developers.mattermost.com/integrate/other-integrations/ for more details.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostIconOverride": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

.. config:setting:: integrate-enableuseraccesstokens
  :displayname: Enable personal access tokens (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: EnableUserAccessTokens
  :environment: N/A

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
  :configjson: EnableBotAccountCreation
  :environment: N/A

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
  :configjson: DisableBotsWhenOwnerIsDeactivated
  :environment: N/A

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
  :configjson: EnableGifPicker
  :environment: N/A

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
   `Link previews <https://docs.mattermost.com/configure/configuration-settings.html#enable-link-previews>`__ must be enabled in order to display GIF link previews. Mattermost deployments restricted to access behind a firewall must open port 443 to both https://api.gfycat.com/v1 and https://gfycat.com/<id> (for all request types) for this feature to work.

.. config:setting:: integrate-gfycatapikey
  :displayname: Gfycat API key (Integrations)
  :systemconsole: Integrations > GIF (Beta)
  :configjson: GfycatApiKey
  :environment: N/A
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
  :configjson: GfycatApiSecret
  :environment: N/A
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
  :configjson: AllowCorsFrom
  :environment: N/A
  :description: Enable HTTP cross-origin requests from specific domains separated by spaces. Type ``*`` to allow CORS from any domain or leave it blank to disable it.

Enable cross-origin requests from
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable HTTP cross-origin requests from specific domains separated by spaces. Type ``*`` to allow CORS from any domain or leave it blank to disable it.

.. note::
 Please make sure you have entered your Site URL before enabling this setting to prevent losing access to the System Console after saving. If you experience lost access to the System Console after changing this setting, you can set your `Site URL <https://docs.mattermost.com/configure/configuration-settings.html#site-url>`__ through the ``config.json`` file.

+--------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowCorsFrom": ""`` with string input. |
+--------------------------------------------------------------------------------------+

.. config:setting:: integrate-corsexposedheaders
  :displayname: CORS exposed headers (Integrations)
  :systemconsole: Integrations > CORS
  :configjson: CorsExposedHeaders
  :environment: N/A
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
  :configjson: CorsAllowCredentials
  :environment: N/A

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
  :configjson: CorsDebug
  :environment: N/A

  - **true**: Prints messages to the logs to help when developing an integration that uses CORS.
  - **false**: **(Default)** Debug messages not printed to the logs.

CORS debug
~~~~~~~~~~

**True**: Prints messages to the logs to help when developing an integration that uses CORS. These messages will include the structured key value pair ``"source": "cors"``.

**False**: Debug messages not printed to the logs.

+-------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CorsDebug": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------+
