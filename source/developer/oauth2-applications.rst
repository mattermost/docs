OAuth 2.0 Applications
===============

OAuth 2.0 is a protocol that allows Mattermost to authorize API requests from external applications. The authorization lets 

1. users with an account on a Mattermost server to sign in to third-party applications. You can find a `sample OAuth2 Client Application for Mattermost here <https://github.com/enahum/mattermost-oauth2-client-sample>`_ to test the functionality.

2. a Mattermost server to authenticate requests to a third-party API. One popular application is Zapier integration which allows you to integrate more than 500 applications with Mattermost through OAuth 2.0. See our `Zapier documentation <https://docs.mattermost.com/integrations/zapier.html>`_ to learn more.

This documentation includes the following details:

 - `Register your application with Mattermost <https://docs.mattermost.com/developer/oauth-2-0-applications#register-your-application-with-mattermost>`_
 - `Permissions to your application  <https://docs.mattermost.com/developer/oauth-2-0-applications#permissions-to-your-application>`_

Register your application with Mattermost
---------------------------------------------------------

You must register your application in Mattermost to generate OAuth 2.0 credentials (client ID and secret), which your application can use to authenticate API calls to Mattermost, and which Mattermost uses to authorize API requests from the application.

If you would like to set up a Zapier integration with OAuth 2.0, see our `Zapier documentation <https://docs.mattermost.com/integrations/zapier.html>`_ to learn more.

Enable OAuth 2.0 Applications
~~~~~~~~~~~~~~~~~~~~~~

OAuth 2.0 applications are off by default and can be enabled by the system administrator as follows:

1. Login to your Mattermost server as the system administrator.
2. Go to **Main Menu > System Console > Integrations > Custom Integrations**.
3. Set `Enable OAuth 2.0 Service Provider <https://docs.mattermost.com/administration/config-settings.html#enable-oauth-2-0-service-provider>`_ to **True**.
4. (Optional) If you would like to allow external applications to post with customizable usernames and profile pictures, then set `Enable integrations to override usernames <https://docs.mattermost.com/administration/config-settings.html#enable-webhooks-and-slash-commands-to-override-usernames>`_ and `Enable integrations to override profile picture icons <https://docs.mattermost.com/administration/config-settings.html#enable-webhooks-and-slash-commands-to-override-profile-picture-iconss>`_ to **True**.
5. (Optional) If you would like to allow users on your system who are not System Admins to create OAuth 2.0 applications, then set `Restrict creating integrations to Team and System Admins <https://docs.mattermost.com/administration/config-settings.html#restrict-creating-integrations-to-team-and-system-admins>`_ to **False**.

Register an OAuth 2.0 Application
~~~~~~~~~~~~~~~~~~~~~~
1. Go to **Main Menu** > **Integrations**
2. Click **OAuth 2.0 Applications**, then click **Add OAuth 2.0 Application** and select your options:
  a. **Is Trusted**: When set to *Yes*, your application is considered trusted by Mattermost. This means Mattermost doesn’t require users to accept authorization when signing to third-party applications. When set to *No*, users will be provided with the following page to accept or deny authorization when authenticating for the first time.



  b. **Display Name**: Enter a name for your application made of up to 64 characters. This is the name users will see when granting access to the application, when viewing a list of authorized applications in **Account Settings > Security > OAuth 2.0 Applications** and when viewing a list of OAuth 2.0 applications that have access to Mattermost in **Main Menu** > **Integrations**.
  c. **Description**: This is a short description of your application that users will see when viewing a list of authorized applications in **Account Settings > Security > OAuth 2.0 Applications**.
  d. **Homepage**: This is the homepage of the OAuth 2.0 application. The URL must be a valid URL and start with http:// or https:// depending on your server configuration.
  e. (Optional) **Icon URL**: The image users will see when viewing a list of authorized applications in **Account Settings > Security > OAuth 2.0 Applications** and when viewing a list of OAuth 2.0 applications that have access to Mattermost in **Main Menu** > **Integrations**. Must be a valid URL and start with http:// or https://.
  f. **Callback URLs**: This is the URL to which Mattermost will redirect users after accepting or denying authorization of your application, and which will handle authorization codes or access tokens. Must be a valid URL that starts with http:// or https://.
3. Click **Save** to create the application. 



4. You will be provided with a **Client ID**, **Client Secret** and the authorized redirect URLs. Save these values and use them in your application to connect it to Mattermost.



Revoke access to your application
---------------------------------------------------------

Once 


You may regenerate **Client Secret** from the OAuth 2.0 Applications page anytime, if needed.



Revoking Access to OAuth 2.0 Applications



Revoking access

Regenerating secret





Create an OAuth 2.0 Application
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

Permissions to your application 
---------------------------------------------------------

Organizations can choose which third-party applications have access to 
their repositories and other resources by enabling third-party application restrictions.

When third-party application restrictions are enabled, organization members 
can request owner approval for third-party applications they'd like to use. 
Organization owners receive a notification of the pending request. Owners can 
also view which third-party applications currently have access to private resources,
 as well as disable access for previously approved applications.

When you create a new organization, third-party applications are restricted by default. 
Organization admins can disable third-party application restrictions at any time.


Once you have registered your OAuth 2.0 application, all users on the Mattermost server are automatically given access to the application. If the application was set up as a trusted OAuth 2.0 app on the Mattermost server, authorization from users is not required.

If you would prefer users to authorize the application to access and connect to their Mattermost If your users request authorizationIf your users request approval 

If the application was set up as a trusted OAuth 2.0 app on the Mattermost server, authorization is not required from users. Otherwise, a page will be displayed requiring the user to authorize the application to access and connect to their Mattermost account.
