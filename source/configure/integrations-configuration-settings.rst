Integrations configuration settings
===================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
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

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Integrations > Integration Management**.

.. config:setting:: enable-incoming-webhooks
  :displayname: Enable incoming webhooks (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnableIncomingWebhooks
  :environment: MM_SERVICESETTINGS_ENABLEINCOMINGWEBHOOKS

  - **true**: **(Default)** Incoming webhooks are allowed. To manage incoming webhooks, select **Integrations** from the Mattermost Product menu.
  - **false**: The **Integrations > Incoming Webhooks** section of the Mattermost Product menu is hidden and all incoming webhooks are disabled.


.. config:setting:: enable-outgoing-webhooks
  :displayname: Enable outgoing webhooks (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnableOutgoingWebhooks
  :environment: MM_SERVICESETTINGS_ENABLEOUTGOINGWEBHOOKS

  - **true**: **(Default)** Outgoing webhooks will be allowed. To manage outgoing webhooks, select **Integrations** from the Mattermost Product menu.
  - **false**: The **Integrations > Outgoing Webhooks** of the Mattermost Product menu is hidden and all outgoing webhooks are disabled.


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


.. config:setting:: enable-oauth-20-service-provider
  :displayname: Enable OAuth 2.0 service provider (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnableOAuthServiceProvider
  :environment: MM_SERVICESETTINGS_ENABLEOAUTHSERVICEPROVIDER

  - **true**: **(Default)** Mattermost acts as an OAuth 2.0 service provider allowing Mattermost to authorize API requests from external applications.
  - **false**: Mattermost does not function as an OAuth 2.0 service provider.


.. note::

  Cloud admins can't modify this configuration setting.

.. config:setting:: integration-request-timeout
  :displayname: Integration request timeout (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.OutgoingIntegrationRequestsDefaultTimeout
  :environment: MM_SERVICESETTINGS_OUTGOINGINTEGRATIONREQUESTDEFAULTTIMEOUT
  :description: The number of seconds to wait for external integration HTTP requests, before timing out. Default value is **3 seconds**.


.. config:setting:: enable-integrations-to-override-usernames
  :displayname: Enable integrations to override usernames (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnablePostUsernameOverride
  :environment: MM_SERVICESETTINGS_ENABLEPOSTUSERNAMEOVERRIDE

  - **true**: Webhooks, slash commands, OAuth 2.0 apps, and other integrations will be allowed to change the username they are posting as.
  - **false**: **(Default)** Custom slash commands can only post as the username of the user who used the slash command.


.. config:setting:: enable-integrations-to-override-profile-picture-icons
  :displayname: Enable integrations to override profile picture icons (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnablePostIconOverride
  :environment: MM_SERVICESETTINGS_ENABLEPOSTICONOVERRIDE

  - **true**: Webhooks, slash commands, and other integrations, such as `Zapier <https://docs.mattermost.com/integrations/zapier.html>`_, will be allowed to change the profile picture they post with.
  - **false**: **(Default)** Webhooks, slash commands, and OAuth 2.0 apps can only post with the profile picture of the account they were set up with.


.. config:setting:: enable-personal-access-tokens
  :displayname: Enable personal access tokens (Integrations)
  :systemconsole: Integrations > Integration Management
  :configjson: .ServiceSettings.EnableUserAccessTokens
  :environment: MM_SERVICESETTINGS_ENABLEUSERACCESSTOKENS

  - **true**: Users can create `personal access tokens <https://developers.mattermost.com/integrate/admin-guide/admin-personal-access-token/>`_ for integrations in **Profile > Security**.
  - **false**: **(Default)** Personal access tokens are disabled on the server.


----

Bot accounts
------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Integrations > Bot Accounts**.

.. config:setting:: enable-bot-account-creation
  :displayname: Enable bot account creation (Integrations)
  :systemconsole: Integrations > Bot Accounts
  :configjson: .ServiceSettings.EnableBotAccountCreation
  :environment: MM_SERVICESETTINGS_ENABLEBOTACCOUNTCREATION

  - **true**: Users can create bot accounts for integrations in **Integrations > Bot Accounts**.
  - **false**: **(Default)** Bot accounts cannot be created through the user interface or the RESTful API.


.. config:setting:: disable-bot-accounts-when-owner-is-deactivated
  :displayname: Disable bot accounts when owner is deactivated (Integrations)
  :systemconsole: Integrations > Bot Accounts
  :configjson: .ServiceSettings.DisableBotsWhenOwnerIsDeactivated
  :environment: MM_SERVICESETTINGS_DISABLEBOTSWHENOWNERISDEACTIVATED

  - **true**: When a user is deactivated, disables all bot accounts managed by the user.
  - **false**: **(Default)** When a user is deactivated, all bot accounts managed by the user remain active.


----

GIF
----

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Integrations > GIF**.

.. config:setting:: enable-gif-picker
  :displayname: Enable GIF picker (Integrations)
  :systemconsole: Integrations > GIF
  :configjson: .ServiceSettings.EnableGifPicker
  :environment: MM_SERVICESETTINGS_ENABLEGIFPICKER

  - **true**: **(Default)** Allow users to select GIFs from the emoji picker via a GIPHY integration.
  - **false**: GIFs cannot be selected in the emoji picker.


.. important::
   :ref:`Link previews <configure/site-configuration-settings:enable message link previews>` must be enabled in order to display GIF link previews. Mattermost deployments restricted to access behind a firewall must open port 443 (for all request types) for this feature to work.

----

CORS
----

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Integrations > CORS**.

.. config:setting:: enable-cross-origin-requests-from
  :displayname: Enable cross-origin requests from (Integrations)
  :systemconsole: Integrations > CORS
  :configjson: .ServiceSettings.AllowCorsFrom
  :environment: MM_SERVICESETTINGS_ALLOWCORSFROM
  :description: Enable HTTP cross-origin requests from all, none, or specific domains.


.. config:setting:: cors-exposed-headers
  :displayname: CORS exposed headers (Integrations)
  :systemconsole: Integrations > CORS
  :configjson: .ServiceSettings.CorsExposedHeaders
  :environment: MM_SERVICESETTINGS_CORSEXPOSEDHEADERS
  :description: Whitelist of headers that will be accessible to the requester.


.. config:setting:: cors-allow-credentials
  :displayname: CORS allow credentials (Integrations)
  :systemconsole: Integrations > CORS
  :configjson: .ServiceSettings.CorsAllowCredentials
  :environment: MM_SERVICESETTINGS_CORSALLOWCREDENTIALS

  - **true**: Requests that pass validation will include the ``Access-Control-Allow-Credentials`` header.
  - **false**: **(Default)** Requests won't include the ``Access-Control-Allow-Credentials`` header.


.. config:setting:: cors-debug
  :displayname: CORS debug (Integrations)
  :systemconsole: Integrations > CORS
  :configjson: .ServiceSettings.CorsDebug
  :environment: MM_SERVICESETTINGS_CORSDEBUG

  - **true**: Prints messages to the logs to help when developing an integration that uses CORS.
  - **false**: **(Default)** Debug messages not printed to the logs.


----

Embedding
---------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Integrations > Embedding**.

.. config:setting:: frame-ancestors
  :displayname: Frame ancestors (Integrations)
  :systemconsole: Integrations > Embedding
  :configjson: .ServiceSettings.FrameAncestors
  :environment: MM_SERVICESETTINGS_FRAMEANCESTORS
  :description: Specify domains that Mattermost can be embedded in via an iFrame. Blank by default to disable embedding.


.. note::

  Embedding Mattermost via an iFrame can provide seamless integration for collaboration into an organization’s existing tools and workflows. However, you must ensure that correct configurations are in place to allow communication between the iframe and the parent domain without violating security.