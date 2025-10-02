Connect Microsoft Teams to Mattermost
=====================================

.. include:: ../_static/badges/entry-ent.rst
  :start-after: :nosearch:

Break through siloes in a mixed Mattermost and Microsoft Teams environment by forwarding real-time chat notifications from Microsoft Teams to Mattermost.

Deploy
-------

Setup starts in Microsoft Teams and ends in Mattermost.

Set up an OAuth application in Azure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Sign into `portal.azure.com <https://portal.azure.com>`_ using an admin Azure account.
2. Navigate to `App Registrations <https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/RegisteredApps>`_.
3. Select **New registration** at the top of the page.

  .. image:: ../images/new-azure-registration.png
    :alt: In Azure, create a new app registration.

4. Fill out the form with the following values:

 - **Name**: ``Mattermost MS Teams``
 - **Supported account types**: ``Default value (Single tenant)``
 - **Platform**: ``Web``
 - **Redirect URI**: ``https://(MM_SITE_URL)/plugins/com.mattermost.msteams-sync/oauth-redirect``

Replace ``(MM_SITE_URL)`` with your Mattermost server's Site URL. Select **Register** to submit the form.

  .. image:: ../images/register-azure-app.png
    :alt: In Azure, register the new Mattermost app.

5. From this screen, make note of the **Application (client) ID** and **Directory (tenant) ID**, needed later to configure the plugin in Mattermost.

  .. image:: ../images/note-client-and-tenant-id.png
    :alt: Note important IDs to use later.

6. Navigate to **Certificates & secrets** in the left pane.

7. Select **New client secret**. Enter the description and select **Add**. After the creation of the client secret, copy the new secret value, not the secret ID. We'll use this value later in the Mattermost System Console.

  .. image:: ../images/azure-certs-secrets.png
    :alt: In Azure, enter client secret details.

8. Navigate to **API permissions** in the left pane.

9. Select **Add a permission**, then **Microsoft Graph** in the right pane.

  .. image:: ../images/azure-configured-permissions.png
    :alt: In Azure, manage API permissions for the Mattermost app.

10. Select **Delegated permissions**, and scroll down to select the following permissions:

 - ``Chat.Read``
 - ``ChatMessage.Read``
 - ``Files.Read.All``
 - ``offline_access``
 - ``User.Read``

11. Select **Add permissions** to submit the form.

12. Next, add application permissions via **Add a permission > Microsoft Graph > Application permissions**.

13. Select the following permissions:

 - ``Chat.Read.All``
 - ``Presence.Read.All``

14. Select **Add permissions** to submit the form.

15. Select **Grant admin consent for...** to grant the permissions for the application.

Ensure you have the metered APIs enabled (and the pay subscription associated to it)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Subscribing to chat notifications requires assocating the OAuth App with a paid Azure subscription. To complete this setup, follow the instructions at https://learn.microsoft.com/en-us/graph/metered-api-setup.

.. important::

  If you don't configure the metered APIs, you must use the **Evaluation model** (configurable in Mattermost) that is limited to a low rate of changes per month. We strongly recommend that you avoid using the Evaluation model configuration in live production environments because you can stop receiving messages due the rate limit. See `this Microsoft documentation <https://learn.microsoft.com/en-us/graph/teams-licenses>`__ for more details.

You're all set for configuration inside Azure.

Install and configure the Microsoft Teams integration in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

  These installation instructions assume you already have a Mattermost instance running v9.8.0 (or later) and configured to use PostgreSQL. This Mattermost integration doesn't support MySQL databases.

1. Log in to your Mattermost :doc:`workspace </end-user-guide/end-user-guide-index>` as a system admin.
2. In Mattermost, from the Product menu |product-list|, select **App Marketplace**.
3. Search for or scroll to MS Teams, and select **Install**.
4. Once installed, select **Configure**. You're taken to the System Console.
5. Configure the **Tenant ID**, **Client ID**, and **Client Secret** with the values obtained from setting up the OAuth App in Azure above.

See the :ref:`Microsoft Teams plugin configuration settings <administration-guide/configure/plugins-configuration-settings:ms teams>` documentation for additional configuration options.

.. note::

  - From Mattermost v9.11.2 (ESR) and Mattermost Cloud v10, v2.0 of this plugin is pre-packaged with the Mattermost Server. If your Mattermost deployment is on a release prior to v9.11.2, download the `latest plugin binary release <https://github.com/mattermost/mattermost-plugin-msteams>`_, and upload it to your server via **System Console > Plugin Management**.
  -  We recommend making a copy of your webhook secret and encryption key, as it will only be visible to you once.

Monitor performance
--------------------

You can set up :doc:`performance monitoring </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>` and :doc:`performance alerting </administration-guide/scale/performance-alerting>` for this plugin using Prometheus and Grafana.

- Monitoring enables you to proactively review the overall health of the plugin, including database calls, HTTP requests, and API latency.
- Alerting enables you to detect and take action as issues come up, such as the integration being offline.

Grafana dashboards `are available on GitHub <https://github.com/mattermost/mattermost-plugin-msteams/tree/main/server/metrics/dashboards>`_ for Mattermost Cloud deployments as a useful starting point. These dashboards are designed for use in Mattermost Cloud, and filter to a given ``namespace``. 

.. image:: ../images/grafana-dashboard-msteams.png
  :alt: Example of a Grafana monitoring dashboard for a Mattermost instance connected to Microsoft Teams.

.. note:: 
  
  Modifications will be necessary for self-hosted Mattermost deployments. See the `Get help <#get-help>`__ section below for details on how to contact us for assistance.

Use
-----

See the :doc:`collaborate within connected microsoft teams </end-user-guide/collaborate/collaborate-within-connected-microsoft-teams>` product documentation to start receiving Microsoft Teams notifications.

Upgrade
-------

We recommend updating this integration as new versions are released. Generally, updates are seamless and don't interrupt the user experience in Mattermost. Visit the `Releases page <https://github.com/mattermost/mattermost-plugin-msteams>`__ for the latest release, available releases, and compatibiilty considerations.

Frequently asked questions
--------------------------

My email address in Mattermost doesn't match my email address in Microsoft Teams: can I still connect?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. Currently, only accounts with the same email addresses are allowed to be connected. Specify the email address that matches your Mattermost account. 

If connecting a Mattermost account to a Microsoft Teams account with a different email address is something your workspace requires, there is an open `GitHub issue <https://github.com/mattermost/mattermost-plugin-msteams/issues/519>`__ for you to share your feedback.

How is encryption handled at rest and in motion?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The configured client secret, stored in the Mattermost configuration, is used for app-only access to the the Microsoft Graph API. As users connect to Microsoft Teams using the integration, the resulting access tokens are encrypted and stored in the Mattermost database to be used for access on behalf of the connected user. All communication between the integration and the Microsoft Graph API is conducted via TLS.

When notifications are enabled, chats and file attachments received by connected users will be stored as posts in the direct message channel between that user and the bot account created by the integration.

Are there any database or network security considerations?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is nothing specific to the integration that is beyond what would apply to a Mattermost instance.

Are there any compliance considerations (ie. GDPR, PCI)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is nothing specific to the integration that is beyond what would apply to a Mattermost instance.

How is this integration architectured?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The integration subscribes to change notifications from the Microsoft Graph API. These change notifications inform Mattermost about new or updated chats within Microsoft Teams. Upon receipt of the change notification, the integration uses a combination of its app-only access (via the client secret) and delegated acess (via connected users) to fetch the contents of these chats and represent them appropriately within Mattermost.

Get help
--------

Mattermost customers can open a `Mattermost support case <https://support.mattermost.com/hc/en-us/requests/new>`_. To report a bug, please open a GitHub issue against the `Mattermost for Microsoft Teams Notifications plugin repository <https://github.com/mattermost/mattermost-plugin-msteams>`_.

For questions, feedback, and assistance, join our pubic `Integrations and Apps channel <https://community.mattermost.com/core/channels/integrations>`_ on the `Mattermost Community Server <https://community.mattermost.com/>`_ for assistance.