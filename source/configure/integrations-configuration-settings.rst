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

Access the following configuration settings in the System Console by going to **Integrations**.

Integration Management
~~~~~~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Integrations > Integration Management**.

Enable Incoming Webhooks
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

Developers building integrations can create webhook URLs for Public channels and Private channels. Please see our `documentation page <https://docs.mattermost.com/developer/webhooks-incoming.html>`__ to learn about creating webhooks, viewing samples, and letting community know about integrations you've built.

**True**: Incoming webhooks are allowed. To manage incoming webhooks, select **Integrations** from the Mattermost Product menu. The webhook URLs created can be used by external applications to create posts in any Public or Private channels that you have access to.

**False**: The **Integrations > Incoming Webhooks** section of the Mattermost Product menu is hidden and all incoming webhooks are disabled.

.. important::
   Security note: By enabling this feature, users may be able to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`__ by attempting to impersonate other users. To combat these attacks, a BOT tag appears next to all posts from a webhook. Enable at your own risk.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableIncomingWebhooks": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

Enable Outgoing Webhooks
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

Developers building integrations can create webhook tokens for Public channels. Trigger words are used to fire new message events to external integrations. For security reasons, outgoing webhooks are only available in Public channels. Please see our `documentation page <https://docs.mattermost.com/developer/webhooks-outgoing.html>`__ to learn about creating webhooks and viewing samples.

**True**: Outgoing webhooks will be allowed. To manage outgoing webhooks, select **Integrations** from the Mattermost Product menu.

**False**: The **Integrations > Outgoing Webhooks** of the Mattermost Product menu is hidden and all outgoing webhooks are disabled.

.. important:: 
   Security note: By enabling this feature, users may be able to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`__ by attempting to impersonate other users. To combat these attacks, a BOT tag appears next to all posts from a webhook. Enable at your own risk.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOutgoingWebhooks": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

Enable Custom Slash Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

Slash commands send events to external integrations that send a response back to Mattermost.

**True**: Allow users to create custom slash commands from **Main Menu > Integrations > Commands**.

**False**: Slash commands are hidden in the **Integrations** user interface.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCommands": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

Enable OAuth 2.0 Service Provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: Mattermost acts as an OAuth 2.0 service provider allowing Mattermost to authorize API requests from external applications.

**False**: Mattermost does not function as an OAuth 2.0 service provider.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOAuthServiceProvider": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

Enable integrations to override usernames
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: Webhooks, slash commands, OAuth 2.0 apps, and other integrations such as `Zapier <https://docs.mattermost.com/integrations/zapier.html>`__, will be allowed to change the username they are posting as. If no username is present, the username for the post is the same as it would be for a setting of ``False``.

**False**: Custom slash commands can only post as the username of the user who used the slash command. OAuth 2.0 apps can only post as the username of the user who set up the integration. For incoming webhooks and outgoing webhooks, the username is "webhook". See https://developers.mattermost.com/integrate/other-integrations/ for more details.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostUsernameOverride": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

Enable integrations to override profile picture icons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: Webhooks, slash commands, and other integrations, such as `Zapier <https://docs.mattermost.com/integrations/zapier.html>`__, will be allowed to change the profile picture they post with.

**False**: Webhooks, slash commands, and OAuth 2.0 apps can only post with the profile picture of the account they were set up with. See https://developers.mattermost.com/integrate/other-integrations/ for more details.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostIconOverride": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Enable Personal Access Tokens
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: Users can create `personal access tokens <https://developers.mattermost.com/integrate/admin-guide/admin-personal-access-token/>`__ for integrations in **Profile > Security**. They can be used to authenticate against the API and give full access to the account.

To manage who can create personal access tokens or to search users by token ID, go to the **System Console > Users** page.

**False**: Personal access tokens are disabled on the server.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserAccessTokens": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Bot Accounts
~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Integrations > Bot Accounts**.

Enable Bot Account Creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: Users can create bot accounts for integrations in **Integrations > Bot Accounts**. Bot accounts are similar to user accounts except they cannot be used to log in. See `documentation <https://developers.mattermost.com/integrate/admin-guide/admin-bot-accounts/>`__ to learn more.

**False**: Bot accounts cannot be created through the user interface or the RESTful API. Plugins can still create and manage bot accounts.

+----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableBotAccountCreation": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------+

Disable bot accounts when owner is deactivated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: When a user is deactivated, disables all bot accounts managed by the user. To re-enable bot accounts, go to **Integrations > Bot Accounts**.

**False**: When a user is deactivated, all bot accounts managed by the user remain active.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DisableBotsWhenOwnerIsDeactivated": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------+

GIF (Beta)
~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Integrations > GIF (Beta)**.

Enable GIF Picker
^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

**True**: Allow users to select GIFs from the emoji picker via a Gfycat integration.

**False**: GIFs cannot be selected in the emoji picker.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableGifPicker": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

.. note::
   `Link previews <https://docs.mattermost.com/configure/configuration-settings.html#enable-link-previews>`__ must be enabled in order to display GIF link previews. Mattermost deployments restricted to access behind a firewall must open port 443 to both https://api.gfycat.com/v1 and https://gfycat.com/<id> (for all request types) for this feature to work.

Gfycat API Key
^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

When blank, uses the default API key provided by Gfycat. Alternatively, a unique API key can be requested at https://developers.gfycat.com/signup/#/. Enter the client ID you receive via email to this field.

+-----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GfycatApiKey": "2_KtH_W5"`` with string input.   |
+-----------------------------------------------------------------------------------------------+

Gfycat API Secret
^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

The API secret generated by Gfycat for your API key. When blank, uses the default API secret provided by Gfycat.

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GfycatApiSecret": "3wLVZPiswc3DnaiaFoLkDvB4X0IV6CpMkj4tf2inJRsBY6-FnkT08zGmppWFgeof"`` with string input.  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

CORS
~~~~~

Access the following configuration settings in the System Console by going to **Integrations > CORS**.

Enable cross-origin requests from
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

Enable HTTP cross-origin requests from specific domains separated by spaces. Type ``*`` to allow CORS from any domain or leave it blank to disable it.

.. note::
 Please make sure you have entered your Site URL before enabling this setting to prevent losing access to the System Console after saving. If you experience lost access to the System Console after changing this setting, you can set your `Site URL <https://docs.mattermost.com/configure/configuration-settings.html#site-url>`__ through the ``config.json`` file.

+--------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowCorsFrom": ""`` with string input. |
+--------------------------------------------------------------------------------------+

CORS Exposed Headers
^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

Whitelist of headers that will be accessible to the requester.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CorsExposedHeaders": ""`` with string input. |
+-------------------------------------------------------------------------------------------+

CORS Allow Credentials
^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

**True**: Requests that pass validation will include the ``Access-Control-Allow-Credentials`` header.

**False**: Requests won't include the ``Access-Control-Allow-Credentials`` header.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CorsAllowCredentials": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

CORS Debug
^^^^^^^^^^^^

|all-plans| |self-hosted|

**True**: Prints messages to the logs to help when developing an integration that uses CORS. These messages will include the structured key value pair ``"source": "cors"``.

**False**: Debug messages not printed to the logs.

+-------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CorsDebug": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------+