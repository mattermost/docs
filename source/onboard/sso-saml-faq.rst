Frequently Asked Questions
--------------------------

How to Bind Authentication to Id Attribute instead of Email
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alternatively, you can use an Id Attribute instead of email to bind the user.  We recommend choosing an ID that is unique and will not change over time.  

Configuring with an Id Attribute allows you to reuse an email address for a new user without the old user's information being exposed. For instance, if a user with an email address joe.smith@mattermost.com was once an employee, a new employee named Joe Smith can use the same email. This configuration is also useful when a user's name changes and their email needs to be updated. 

This process was designed with backwards compatibility to email binding. Here is the process applied to new account creations and to accounts logging in after the configuration:

 - A user authenticated with SAML is bound to the SAML service user using the Id Attribute (as long as it has been configured) or bound by email using the email received from SAML. 
 - When the user tries to login and the SAML server responds with a valid authentication, then the server uses the "Id" field of the SAML authentication to search the user. 
 - If a user bound to that ID already exists, it logs in as that user. 
 - If a user bound to that ID does not exist, it will search base on the email. 
 - If a user bound to the email exists, it logs in with email and updates the autentication data to the ID, instead of the email. 
 - If a user bound to the ID or email does not exist, it will create a new Mattermost account bound to the SAML account by ID and will allow the user to log in. 

 Note:  Existing accounts will not update until they log in to the server. 
 
Can SAML via Microsoft ADFS be configured with Integrated Windows Authentication (IWA)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. IWA is supported on the browser, with support added to iOS and Android mobile apps in Q2/2019 (mobile apps v1.18 and later).

However, IWA is not supported on the Mattermost Desktop Apps due to a limitation in Electron. As a workaround you may create a browser desktop shortcut for quick access to Mattermost, just like a Desktop App.

How do I migrate users from one authentication method (e.g. email) to SAML?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the :doc:`mattermost user migrate_auth CLI command <cli-user-migrate-auth>`.

How is SAML different from OAuth 2.0 and OpenId Connect?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

OAuth 2.0 was primarily intended for delegated authorization, where an app is authorized to access resources, such as Google contact list. It doesn’t deal with authentication.

OpenID Connect is built on top of OAuth 2.0, which supports authentication and thus direct SSO.

SAML is like OpenID Connect, except typically used in enterprise settings. OpenID Connect is more common in consumer websites and web/mobile apps.

Learn more at https://hackernoon.com/demystifying-oauth-2-0-and-openid-connect-and-saml-12aa4cf9fdba.

