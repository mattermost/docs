Integrations configuration settings
===================================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Review and manage the following integration configuration options in the System Console by selecting the **Product** |product-list| menu, selecting **System Console**, and then selecting **Integrations**:

- `Integrations management <#integrations-management>`__
- `Bot Accounts <#bot-acocunts>`__
- `GIF <#gif>`__
- `CORS <#cors>`__

.. tip::

  System admins managing a self-hosted Mattermost deployment can edit the ``config.json`` file as described in the following tables. Each configuration value below includes a JSON path to access the value programmatically in the ``config.json`` file using a JSON-aware tool. For example, the ``EnableIncomingWebhooks`` value is under ``ServiceSettings``.

  - If using a tool such as `jq <https://stedolan.github.io/jq/>`__, you'd enter: ``cat config/config.json | jq '.ServiceSettings.EnableIncomingWebhooks'``
  - When working with the ``config.json`` file manually, look for an object such as ``ServiceSettings``, then within that object, find the key ``EnableIncomingWebhooks``.

----

Integrations management
-----------------------

Access the following configuration settings in the System Console by going to **Integrations > Integration Management**.

.. config:setting:: enable-incoming-webhooks
  :displayname: Enable incoming webhooks (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnableIncomingWebhooks
  :environment: MM_SERVICESETTINGS_ENABLEINCOMINGWEBHOOKS

  - **true**: **(Default)** Incoming webhooks are allowed. To manage incoming webhooks, select **Integrations** from the Mattermost Product menu.
  - **false**: The **Integrations > Incoming Webhooks** section of the Mattermost Product menu is hidden and all incoming webhooks are disabled.

Enable incoming webhooks
~~~~~~~~~~~~~~~~~~~~~~~~

Developers building integrations can create webhook URLs for public channels and private channels. See the `incoming webhooks <https://developers.mattermost.com/integrate/webhooks/incoming/>`_ developer documentation to learn about creating webhooks, viewing samples, and letting community know about integrations you've built.

**True**: Incoming webhooks are allowed. To manage incoming webhooks, select **Integrations** from the Mattermost Product menu. The webhook URLs created can be used by external applications to create posts in any public or private channels that you have access to.

**False**: The **Integrations > Incoming Webhooks** section of the Mattermost Product menu is hidden and all incoming webhooks are disabled.

.. important::
   Security note: By enabling this feature, users may be able to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`_ by attempting to impersonate other users. To combat these attacks, a BOT tag appears next to all posts from a webhook. Enable at your own risk.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableIncomingWebhooks": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

.. config:setting:: enable-outgoing-webhooks
  :displayname: Enable outgoing webhooks (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnableOutgoingWebhooks
  :environment: MM_SERVICESETTINGS_ENABLEOUTGOINGWEBHOOKS

  - **true**: **(Default)** Outgoing webhooks will be allowed. To manage outgoing webhooks, select **Integrations** from the Mattermost Product menu.
  - **false**: The **Integrations > Outgoing Webhooks** of the Mattermost Product menu is hidden and all outgoing webhooks are disabled.

Enable outgoing webhooks
~~~~~~~~~~~~~~~~~~~~~~~~

Developers building integrations can create webhook tokens for public channels. Trigger words are used to fire new message events to external integrations. For security reasons, outgoing webhooks are only available in public channels. See the `outgoing webhooks <https://developers.mattermost.com/integrate/webhooks/outgoing/>`_ developer documentation to learn about creating webhooks and viewing samples.

**True**: Outgoing webhooks will be allowed. To manage outgoing webhooks, select **Integrations** from the Mattermost Product menu.

**False**: The **Integrations > Outgoing Webhooks** of the Mattermost Product menu is hidden and all outgoing webhooks are disabled.

.. important::
   Security note: By enabling this feature, users may be able to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`_ by attempting to impersonate other users. To combat these attacks, a BOT tag appears next to all posts from a webhook. Enable at your own risk.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOutgoingWebhooks": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

.. note::

  Disabling this configuration setting in larger deployments may improve server performance in the following areas:

  - Reduced Network Traffic: Outgoing webhooks generate network requests to external services. Disabling them reduces the amount of traffic and resource usage related to those requests.
  - Decreased Load on Server: Handling webhook events and managing connections to external services uses server resources. By disabling outgoing webhooks, the server workload is reduced, allowing it to allocate more resources to other important tasks.
  - Improved Response Time: When outgoing webhooks are enabled, the server waits for the external services to return responses, potentially slowing down the performance if the external services are slow or unresponsive. Disabling them removes this dependency, leading to faster response times for user requests.
  - Lower Memory Usage: Webhooks need memory to process and store data about the requests and responses. Disabling them can free up memory which can be used to improve overall server performance.
  - Simplified Error Handling: Managing errors and retries for outgoing webhook failures can add complexity and overhead. Disabling outgoing webhooks can simplify error handling and reduce the processing overhead associated with it.
  - However, outgoing webhooks are often essential for integrating Mattermost with other services and workflows. It’s important to balance performance improvements with the needs of your organization and users.

.. config:setting:: enable-custom-slash-commands
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

.. config:setting:: enable-oauth-20-service-provider
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

.. config:setting:: enable-dynamic-client-registration
  :displayname: Enable dynamic client registration (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnableDynamicClientRegistration
  :environment: MM_SERVICESETTINGS_ENABLEDYNAMICCLIENTREGISTRATION

  - **true**: Enables Dynamic Client Registration (DCR) per RFC 7591, allowing applications to programmatically register OAuth 2.0 clients via the public API endpoint.
  - **false**: **(Default)** Dynamic Client Registration is disabled.

Enable dynamic client registration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Enables Dynamic Client Registration (DCR) allowing applications to programmatically register OAuth 2.0 clients without manual admin intervention via the ``POST /api/v4/oauth/apps/register`` endpoint.

**False**: Dynamic Client Registration is disabled. OAuth 2.0 applications must be registered manually through the System Console.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableDynamicClientRegistration": false`` with options ``true`` and ``false``.   |
+-------------------------------------------------------------------------------------------------------------------------------+

.. important::

  **Security Warning**: When enabled, the DCR endpoint (``/api/v4/oauth/apps/register``) is **publicly accessible without authentication**. Any user or application can register OAuth clients on your Mattermost server. Only enable this setting if you understand and accept this security model, or have additional network-level access controls in place.

.. note::

  Cloud admins can't modify this configuration setting.

.. config:setting:: integration-request-timeout
  :displayname: Integration request timeout (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.OutgoingIntegrationRequestsDefaultTimeout
  :environment: MM_SERVICESETTINGS_OUTGOINGINTEGRATIONREQUESTDEFAULTTIMEOUT
  :description: The number of seconds to wait for external integration HTTP requests, before timing out. Default value is **3 seconds**.

Integration request timeout
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The number of seconds to wait for external integration HTTP requests, before timing out, including `custom slash commands <https://developers.mattermost.com/integrate/slash-commands/custom/>`_, `outgoing webhooks <https://developers.mattermost.com/integrate/webhooks/outgoing/>`_, `interactive messages <https://developers.mattermost.com/integrate/plugins/interactive-messages/>`_, and `interactive dialogs <https://developers.mattermost.com/integrate/plugins/interactive-dialogs/>`_. Increase this value if you have external integrations that can take some time to generate an HTTP response, or experience delayed responses due to latency.

+------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"OutgoingIntegrationRequestsDefaultTimeout": 3``.  |
+------------------------------------------------------------------------------------------------+

.. config:setting:: enable-integrations-to-override-usernames
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

.. config:setting:: enable-integrations-to-override-profile-picture-icons
  :displayname: Enable integrations to override profile picture icons (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnablePostIconOverride
  :environment: MM_SERVICESETTINGS_ENABLEPOSTICONOVERRIDE

  - **true**: Webhooks, slash commands, and other integrations, such as `Zapier <https://docs.mattermost.com/integrations/zapier.html>`_, will be allowed to change the profile picture they post with.
  - **false**: **(Default)** Webhooks, slash commands, and OAuth 2.0 apps can only post with the profile picture of the account they were set up with.

Enable integrations to override profile picture icons
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Webhooks, slash commands, and other integrations, will be allowed to change the profile picture they post with.

**False**: **(Default)** Webhooks, slash commands, and OAuth 2.0 apps can only post with the profile picture of the account they were set up with. See https://developers.mattermost.com/integrate/other-integrations/ for more details.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostIconOverride": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

.. config:setting:: enable-personal-access-tokens
  :displayname: Enable personal access tokens (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnableUserAccessTokens
  :environment: MM_SERVICESETTINGS_ENABLEUSERACCESSTOKENS

  - **true**: Users can create `personal access tokens <https://developers.mattermost.com/integrate/admin-guide/admin-personal-access-token/>`_ for integrations in **Profile > Security**.
  - **false**: **(Default)** Personal access tokens are disabled on the server.

Enable personal access tokens
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Users can create `personal access tokens <https://developers.mattermost.com/integrate/admin-guide/admin-personal-access-token/>`_ for integrations in **Profile > Security**. They can be used to authenticate against the API and give full access to the account.

To manage who can create personal access tokens or to search users by token ID, go to the **System Console > Users** page.

**False**: Personal access tokens are disabled on the server.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserAccessTokens": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

.. config:setting:: enforce-incoming-webhook-channel-locking
  :displayname: Enforce incoming webhook channel locking (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnforceIncomingWebhookChannelLocking
  :environment: MM_SERVICESETTINGS_ENFORCEINCOMINGWEBHOOKCHANNELLOCKING

  - **true**: Incoming webhooks are required to be locked to their specific channel and cannot post to other channels.
  - **false**: **(Default)** Incoming webhook creators can choose whether to lock webhooks to a specific channel or allow posting to any channel they have access to.

Enforce incoming webhook channel locking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When enabled, this setting enforces that all incoming webhooks must be locked to their designated channel and cannot post messages to other channels. This provides administrators with greater control over webhook security and ensures that webhooks can only post to their intended channels.

**True**: Incoming webhooks are required to be locked to their specific channel. The **Lock to this channel** option is automatically enabled and cannot be disabled when creating or editing webhooks.

**False**: **(Default)** Incoming webhook creators can choose whether to lock webhooks to a specific channel by selecting **Lock to this channel**, or allow the webhook to post to any public channel or private channel the webhook creator is a member of.

+----------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnforceIncomingWebhookChannelLocking": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------------------+

----

Bot accounts
------------

Access the following configuration settings in the System Console by going to **Integrations > Bot Accounts**.

.. config:setting:: enable-bot-account-creation
  :displayname: Enable bot account creation (Integrations)
  :systemconsole: Integrations > Bot Accounts
  :configjson: .ServiceSettings.EnableBotAccountCreation
  :environment: MM_SERVICESETTINGS_ENABLEBOTACCOUNTCREATION

  - **true**: Users can create bot accounts for integrations in **Integrations > Bot Accounts**.
  - **false**: **(Default)** Bot accounts cannot be created through the user interface or the RESTful API.

Enable bot account creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: **(Default for Cloud deployments)** Users can create bot accounts for integrations in **Integrations > Bot Accounts**. Bot accounts are similar to user accounts except they cannot be used to log in. See `documentation <https://developers.mattermost.com/integrate/admin-guide/admin-bot-accounts/>`_ to learn more.

**False**: **(Default for self-hosted deployments)** Bot accounts cannot be created through the user interface or the RESTful API. Plugins can still create and manage bot accounts.

+----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableBotAccountCreation": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------+

.. config:setting:: disable-bot-accounts-when-owner-is-deactivated
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

GIF
----

Access the following configuration settings in the System Console by going to **Integrations > GIF**.

.. config:setting:: enable-gif-picker
  :displayname: Enable GIF picker (Integrations)
  :systemconsole: Integrations > GIF
  :configjson: .ServiceSettings.EnableGifPicker
  :environment: MM_SERVICESETTINGS_ENABLEGIFPICKER

  - **true**: **(Default)** Allow users to select GIFs from the emoji picker via a GIPHY integration.
  - **false**: GIFs cannot be selected in the emoji picker.

Enable GIF picker
~~~~~~~~~~~~~~~~~

**True**: Allow users to select GIFs from the emoji picker via a GIPHY integration.

**False**: GIFs cannot be selected in the emoji picker.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableGifPicker": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

.. important::
   :ref:`Link previews <administration-guide/configure/site-configuration-settings:enable message link previews>` must be enabled in order to display GIF link previews. Mattermost deployments restricted to access behind a firewall must open port 443 (for all request types) for this feature to work.

----

CORS
----

The following configuration settings are applicable only to self-hosted deployments. Access the following configuration settings in the System Console by going to **Integrations > CORS**.

.. config:setting:: enable-cross-origin-requests-from
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

  Ensure you've entered your :ref:`Site URL <administration-guide/configure/environment-configuration-settings:site url>` before enabling this setting to prevent losing access to the System Console after saving. If you lose access to the System Console after changing this setting, you can set your Site URL through the ``config.json`` file.

+--------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowCorsFrom": ""`` with string input. |
+--------------------------------------------------------------------------------------+

.. config:setting:: cors-exposed-headers
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

.. config:setting:: cors-allow-credentials
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

.. config:setting:: cors-debug
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

----

Embedding
---------

The following configuration settings are applicable only to self-hosted deployments. Access the following configuration settings in the System Console by going to **Integrations > Embedding**.

.. config:setting:: frame-ancestors
  :displayname: Frame ancestors (Integrations)
  :systemconsole: Integrations > Embedding
  :configjson: .ServiceSettings.FrameAncestors
  :environment: MM_SERVICESETTINGS_FRAMEANCESTORS
  :description: Specify domains that Mattermost can be embedded in via an iFrame. Blank by default to disable embedding.

Frame ancestors
~~~~~~~~~~~~~~~~

Enter a space-separated list of domains that are allowed to embed the Mattermost web client via an iFrame. Leave blank to disallow embedding. Leave blank to disable embedding. Blank by default.

+------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FrameAncestors".``  |
+------------------------------------------------------------------+

.. note::

  Embedding Mattermost via an iFrame can provide seamless integration for collaboration into an organization’s existing tools and workflows. However, you must ensure that correct configurations are in place to allow communication between the iframe and the parent domain without violating security.