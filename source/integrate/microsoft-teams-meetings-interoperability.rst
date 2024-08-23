Connect Microsoft Meetings to Mattermost
=========================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Start and join voice calls, video calls, and use screen sharing with your team members in Microsoft Teams without leaving Mattermost.

Setup
-----

Setup starts in Microsoft Azure and ends in Mattermost.

Create a Mattermost App in Azure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Sign in to the `Azure portal <https://portal.azure.com>`_ using an admin Azure account.
2. Navigate to `App Registrations <https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/RegisteredApps>`_.
3. Select **New registration** at the top of the page.

  .. image:: ../images/ms-teams-meetings-new-azure-registration.png
    :alt: In Azure, create a new app registration.

4. Fill out the form with the following values, then select **Register** to submit the form:

  - **Name**: Mattermost Microsoft Teams Meetings Plugin
  - **Supported account types**: Default value (Single tenant)
  - **Redirect URI**: ``https://<MM_SITE_URL>/plugins/com.mattermost.msteamsmeetings/oauth2/complete``. Replace ``<MM_SITE_URL>`` with your Mattermost server's Site URL. 

  .. image:: ../images/ms-teams-meetings-reg-info.png
    :alt: In Azure, create a new app registration.

5. Go to **Certificates & secrets** in the left pane.

  .. image:: ../images/ms-teams-meetings-certs-secrets.png
    :alt: In Azure, go to Certificates & secrets located in the left pane.

6. Select **New client secret > Add**, then copy the new secret in the bottom right corner of the screen. We'll use this value later in the Mattermost System Console.

  .. image:: ../images/ms-teams-meetings-new-client-secret.png
    :alt: In Azure, create a new client secret and copy the value for later.

7. Go to **API permissions** in the left pane.

  .. image:: ../images/ms-teams-meetings-api-permissions.png
    :alt: In Azure, go to API permissions located in the left pane.

8. Select **Add a permission** and select **Microsoft Graph** in the right pane.

  .. image:: ../images/ms-teams-meetings-add-permission.png
    :alt: In Azure, add a permission for Microsoft Graph.

9. Select **Delegated permissions**, and scroll down to select the ``OnlineMeetings.ReadWrite`` permissions. Select **Add permissions** to submit the form.

  .. image:: ../images/ms-teams-meetings-delegated-permissions.png
    :alt: In Azure, select OnlineMeetings.ReadWrite permissions.

10. Select **Grant admin consent for mattermost** to grant the permissions for the application.

  .. image:: ../images/ms-teams-meetings-grant-admin-consent.png
    :alt: In Azure, grant admin consent permissions for the application.

You're all set for configuration inside of the Azure portal.

Enable and configure the Microsoft Teams Meetings integration in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. In Azure, copy the **Application (client) ID** and **Directory (tenant) ID** from the Azure portal.

  .. image:: ../images/ms-teams-meetings-copy-ids.png
    :alt: In Azure, copy the Client ID and Tenant ID values.

2. In Mattermost, go to **System Console > Plugins > Microsoft Calendar** to enable this integration.

3. In Mattermost, enter the following values in the fields provided. Select **Save** to apply the configuration:

  - **Azure - Directory (tenant) ID** - Paste the **Directory (tenant) ID** from the Azure portal.
  - **Azure - Application (client) ID** - Paste the **Application (client) ID** from the Azure portal.
  - **Azure - Application (client) Secret** - Copy from the Azure portal (generated in **Certificates & secrets** earlier in these instructions).

Notify your teams that they can `connect their Microsoft Teams Meetings accounts to Mattermost <#connect-a-microsoft-teams-account-to-mattermost>`__.

Usage
-----

Users who want to use MS Teams Meetings interconnectivity must connect a Microsoft Teams Meetings account to Mattermost. 

Once connected, you'll receive direct messages from the Microsoft Teams Meetings bot in Mattermost for Microsoft Teams Meetings activity.

Connect a Microsoft Teams account to Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the `/mstmeetings connect` slash command to connect an MS Teams account to Mattermost.

Start a call
~~~~~~~~~~~~

Start a call either by selecting the video icon in a Mattermost channel or by running the `/mstmeetings start` slash command. Every meeting you start creates a new meeting room in Microsoft Teams. 

.. note::
    
    If you start two meetings less than 30 seconds apart you'll be prompted to confirm that you want to create the meeting.

Disconnect a Microsoft Teams account from Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the `/mstmeetings disconnect` slash command to disconnect a Microsoft Teams account from Mattermost.

Get help
--------

If you face issues while installing this integration, gather relevant information, including reproduction steps to accelerate troubleshooting. You're welcome to open a new issue in the `Mattermost for Microsoft Teams Meetings GitHub repository <https://github.com/mattermost-community/mattermost-plugin-msteams-meetings/issues/new>`_.

- **Mattermost Commercial Customers (including Enterprise and Professional plans)**: Visit `Mattermost Support <https://mattermost.com/support/>`_ to `submit a support ticket <https://support.mattermost.com/hc/en-us/requests/new>`_.

- **Mattermost Team Edition and Free customers** Visit the Mattermost `peer-to-peer troubleshooting forum <https://forum.mattermost.com/c/trouble-shoot/16>`_ where you can access the global Mattermost Community for assistance.