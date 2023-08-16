Set up the Mattermost Google Calendar plugin
=============================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Setting up the Mattermost Google Calendar integration requires the following 3 steps:

1. (Mattermost admin) `Install the Google Calendar plugin <#install-the-mattermost-google-calendar-plugin>`__ on your Mattermost instance.
2. (Google admin) `Create a Google Calendar service <#create-a-google-calendar-service>`__ by creating a Google Cloud project.
3. (Mattermost admin) `Configure the Mattermost Google Calendar plugin <#configure-the-matermost-google-calendar-plugin>`__.

Once setup is complete, see the `get started <#get-started-with-the-plugin>`__ section below to learn how to use the plugin.

Install the Mattermost Google Calendar plugin
---------------------------------------------

To install the `Mattermost Google Calendar </plugins/mattermost-google-calendar>`__ plugin on your Mattermost server:

1. Log in to your Mattermost workspace as a system administrator.
2. Download the latest version of `the plugin binary release <https://github.com/mattermost/xxx>`__, compatible with Mattermost v8.x and later. 

  .. tip::

    If you are using an earlier version of Mattermost, `follow our documentation </upgrade/upgrading-mattermost-server.html>`__ to upgrade to Mattermost v8.x or later.

Create a Google Calendar service
--------------------------------

1. In a browser, as a Google admin, create a project in the Google Cloud Console by going to ``https://console.cloud.google.com/``, selecting the project option in the top left corner of the screen, then selecting **New Project** option in the top right corner of the popup window.

  .. image:: ../images/google-cloud-console-create-project.png
    :alt: In Google Cloud Console, select New Project to create up a new project.

  .. image:: ../images/google-cloud-console-new-project.png
    :alt: Use Google Cloud Console to set up a new project.

2. When your project is created, go to **APIs & Services** to search for and enable the following 2 services:

  - **Google Calendar API**: Used for anything related to the calendar and events.
  - **Google People API**: Used to link your Mattermost account to your Google account.

  .. image:: ../images/google-cloud-console-apis.png
    :alt: In Google Cloud Console, select APIs & Services to search for services to enable.

  .. image:: ../images/enable-google-cloud-console-google-calendar-api.png
    :alt: In Google Cloud Console, search for and enable the Google Calendar API.

  .. image:: ../images/enable-google-cloud-console-google-people-api.png
    :alt: In Google Cloud Console, search for and enable the Google People API.

3. Choose how to configure and register the application by selecting the user type as **Internal** or **External**, then select **Create**.

  .. image:: ../images/google-cloud-console-OAuth-consent-screen.png
    :alt: On the OAuth consent screen, configure and register the application as internal or external.

4. When prompted, set the following app information:

  - **App name**: `Google Calendar Mattermost Plugin`
  - **User support email** 
  - **Developer contact information**
  - Populate the remaining fields as needed.

  .. image:: ../images/google-cloud-console-app-information.png
    :alt: Configure the consent screen app name and user support email.

  .. image:: ../images/google-cloud-console-developer-contact-information.png
    :alt: Configure the consent screen developer contact information.

5. Under Credentials, create new OAuth 2.0 credentials by selecting **Create Credentials > OAuth client ID**.

  - Under **Application type**, select **Web Application**.
  - Under **Authorized redirect URIs** add ``https://(MM_SITE_URL)/plugins/com.mattermost.gcal/oauth2/complete`` and replace ``MM_SITE_URL`` with your Mattermost Server Site URL.

  .. image:: ../images/google-cloud-console-web-application.png
    :alt: Under Credentials, select Web application.

  .. image:: ../images/google-cloud-console-authorized-redirect-uris.png
    :alt: Configure the authorized redirect URI for Mattermost.

6. Once the OAuth client is created, make a copy of the **Client ID** and **Client Secret** values for the next and final setup step below.

  .. image:: ../images/google-cloud-console-OAuth-client-created.png
    :alt: Copy the Client ID and Client secret values. You'll need these values in the next step.

Configure the Mattermost Google Calendar plugin
-----------------------------------------------

In Mattermost, configure the plugin by going to **System Console > Plugin Management > Google Calendar**, enter the following values, and select **Save**.

- **Enable Plugin**: Select **true** to enable the plugin for your Mattermost instance.
- **Admin User IDs**: Specify the user IDs who are authorized to manage the plugin in addition to Mattermost system admins. Separate multiple user IDs with commas. Go to **System Console > User Management > Users** to obtain a user's ID.
- **Encryption key**: Generate an encryption key used to store data in the database. Regenerating this value forces users to re-link their Google Calendars in Mattermost.
- **Google Application Client ID**: Paste the Client ID value from the Google Cloud Console.
- **Google Client Secret**: Paste the Client Secret value from the Google Cloud Console.
- **Google Domain verify key**: TBD

.. note::

    Additional Mattermost Google Calendar configuration options are available for troubleshooting, including the admin log level of plugin logs, and  displaying full or partial context for admin log messages. See the `plugin configuration settings </configure/plugins-configuration-settings.html#mattermost-google-calendar-plugin>`__ documentation for details.

Get started with the plugin
---------------------------

See the `use Mattermost Google Calendar plugin </channels/use-mattermost-google-calendar-plugin>`__ documentation for details on how users can `link their Google Calendar to Mattermost </channels/use-mattermost-google-calendar-plugin.html#connect-your-google-calendar-account-to-mattermost>`__, `customize plugin preferences </channels/use-mattermost-google-calendar-plugin.html#customize-your-google-calendar-plugin>`__, and `create calendar events in Mattermost <channels/use-mattermost-google-calendar-plugin.html#create-a-calendar-event>`__ that are added to their Google Calendar automatically.

Troubleshooting
---------------

If you encounter issues when connecting calendars, creating events, inviting guests to events, or linking channels, we recommend restarting the plugin as a Mattermost system admin. 

1. Go to **System Console > Plugins > Plugin Management**.
2. Under **Installed Plugins**, scroll to the **Google Calendar** section, select **Disable** then wait for the State to change to **Not running**.
3. Select **Enable** and wait for the State to change to **Running**.

Get help
---------

If you face any issues while installing the Mattermost Google Calendar plugin, you can either:

- Open a new issue in the `Mattermost Google Calendar repository <https://github.com/mattermost/mattermost-plugin-mscalendar/issues/new>`__. 
- Or, create a new topic in our `peer-to-peer troubleshooting forum <https://forum.mattermost.com/c/trouble-shoot/16>`__.