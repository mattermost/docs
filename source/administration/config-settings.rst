Configuration Settings
======================
Configuration settings let System Admins manage their Mattermost server and multiple teams. System Admins can modify configuration settings directly in the ``config.json`` file or by using the web-based System Console user interface. Setting changes in the System Console are stored in ``config/config.json``. 

The first user added to a new Mattermost install is assigned the System Admin role and can access the System Console from the Main Menu of any team. 

Note: For any setting not explicitly set in ``config.json`` the Mattermost server will use the default value as documented here, which can be observed in the default ``config/config.json`` file included in each Mattermost release. 

Quick Links:

`General <http://docs.mattermost.com/administration/config-settings.html#id2>`_
	`Configuration <http://docs.mattermost.com/administration/config-settings.html#id3>`_ - `Localization <http://docs.mattermost.com/administration/config-settings.html#id4>`_ - `Users and Teams <http://docs.mattermost.com/administration/config-settings.html#id5>`_ - `Privacy <http://docs.mattermost.com/administration/config-settings.html#id6>`_ - `Compliance <http://docs.mattermost.com/administration/config-settings.html#complicance-enterprise>`_ - `Logging <http://docs.mattermost.com/administration/config-settings.html#id7>`_

`Authentication <http://docs.mattermost.com/administration/config-settings.html#id12>`_
	`Email <http://docs.mattermost.com/administration/config-settings.html#id13>`_ - `GitLab <http://docs.mattermost.com/administration/config-settings.html#id14>`_ - `LDAP <http://docs.mattermost.com/administration/config-settings.html#ldap-enterprise>`_

`Security <http://docs.mattermost.com/administration/config-settings.html#id15>`_
	`Sign Up <http://docs.mattermost.com/administration/config-settings.html#id16>`_ - `Login <http://docs.mattermost.com/administration/config-settings.html#id17>`_ - `Public Links <http://docs.mattermost.com/administration/config-settings.html#id18>`_ - `Sessions <http://docs.mattermost.com/administration/config-settings.html#id19>`_ - `Connections <http://docs.mattermost.com/administration/config-settings.html#id20>`_

`Notifications <http://docs.mattermost.com/administration/config-settings.html#id21>`_
	`Email <http://docs.mattermost.com/administration/config-settings.html#id22>`_ - `Mobile Push <http://docs.mattermost.com/administration/config-settings.html#id24>`_

`Integrations <http://docs.mattermost.com/administration/config-settings.html#id25>`_
	`Webhooks and Commands <http://docs.mattermost.com/administration/config-settings.html#id26>`_ - `External Services <http://docs.mattermost.com/administration/config-settings.html#id29>`_

`Files <http://docs.mattermost.com/administration/config-settings.html#id30>`_
	`Storage <http://docs.mattermost.com/administration/config-settings.html#id31>`_ - `Images <http://docs.mattermost.com/administration/config-settings.html#id32>`_

`Customization <http://docs.mattermost.com/administration/config-settings.html#id33>`_
	`Custom Branding <http://docs.mattermost.com/administration/config-settings.html#id34>`_ - `Legal and Support <http://docs.mattermost.com/administration/config-settings.html#id35>`_

`Advanced <http://docs.mattermost.com/administration/config-settings.html#id36>`_
	`Rate Limiting <http://docs.mattermost.com/administration/config-settings.html#id37>`_ - `Database <http://docs.mattermost.com/administration/config-settings.html#id38>`_ - `Developer <http://docs.mattermost.com/administration/config-settings.html#id39>`_

General
---------------------------------
General settings for server configuration, language defaults, user and team management, privacy, compliance reporting and logs.

Configuration
``````````````````````````
Listen Address ``"ListenAddress": ":8065"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
The IP address on which to listen and the port on which to bind. Entering ":8065" will bind to all interfaces or you can choose one like ``127.0.0.1:8065``. Changing this will require a server restart before taking effect.

Reload Configuration from Disk (Enterprise)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
This button resets the configuration settings by reloading the settings from the disk. The server will still need to be restarted if a setting requiring server restart was changed.

The workflow for failover without downing the server is to change the database line in the config.json file, click **Reload Configuration from Disk** then click **Recycle Database Connections** in the Advanced > Database section.

________

Localization
```````````````````````````
Default Server Language ``"DefaultServerLocale": "en"``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
Default language for system messages and logs. Changing this will require a server restart before taking effect.

Default Client Language ``"DefaultClientLocale": "en"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Default language for newly created users and pages where the user hasn't logged in.

Available Languages ``"AvailableLocales": "en,es,fr,ja,pt-BR"``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
Sets which languages are available for users in **Account Settings** > **Display** > **Languages**. Add new languages using the dropdown menu as they become available.

________

Users and Teams
``````````````````````````
Enable User Creation ``"EnableUserCreation": true``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
``true``: Ability to create new accounts is enabled via inviting new members or sharing the team invite link.

``false``: Ability to create accounts is disabled. The **Create Account** button displays an error when trying to signup via an email invite or team invite link.

Enable Team Creation ``"EnableTeamCreation": true``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
``true``: Ability to create a new team is enabled for all users.

``false``: Only System Administrators can create teams from the team selection page. The **Create A New Team** button is hidden in the main menu UI.

Max Users Per Team ``"MaxUsersPerTeam": 50``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
Maximum number of users per team, including both active and inactive users.

Restrict Creation To Domains ``"RestrictCreationToDomains": ""``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
Teams and user accounts can only be created by a verified email from this list of comma-separated domains (e.g. "corp.mattermost.com, mattermost.org").

Restrict Team Names ``"RestrictTeamNames": true``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
``true``: Newly created team names cannot contain the following restricted words: www, web, admin, support, notify, test, demo, mail, team, channel, internal, localhost, dockerhost, stag, post, cluster, api, oauth.

``false``: Newly created team names are not restricted. 

Enable users to open Direct Message channels with ``"RestrictDirectMessage": "any"``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Any user on the Mattermost server (``any``): The Direct Messages "More" menu has the option to open a Direct Message channel with any user on the server.  

Any member of the team (``team``): The Direct Messages "More" menu only has the option to open a Direct Message channel with users on the current team.  If a user belongs to multiple teams, direct messages will still be received regardless of what team they are currently on. 

Enable Team Directory ``"EnableTeamListing": false`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*Removed in May 16th, 2016 release* 

``true``: Teams that are configured to appear in the team directory will appear on the system main page. Teams can configure this setting from **Team Settings > Include this team in the Team Directory**.

``false``: Team directory on the system main page is disabled.

________

Privacy
``````````````````````````
Settings to configure the name and email privacy of users on your system.  

Show Email Address ``"ShowEmailAddress": true``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
``true``: Show email address of all users.

``false``: Hide email address of users from other users in the user interface, including Team Admins. This is designed for managing teams where users choose to keep their contact information private. System Administrators will still be able to see email addresses in the UI. 

Show Full Name ``"ShowFullName": true``  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Show full name of all users.

``false``: hide full name of users from other users including Team Admins. This is designed for managing teams where users choose to keep their contact information private. System Administrators will still be able to see full names in the UI.

________

Complicance (Enterprise)
```````````````````````````
Settings used to enable and configure Mattermost compliance reports. 

Enable Compliance ``"Enable": false``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Compliance reporting is enabled in Mattermost.

``false``: Compliance reporting is disabled. 

Compliance Directory Location ``"Directory": "./data/"``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Sets the directory where compliance reports are written. 

Compliance Directory Location ``"EnableDaily": false``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Mattermost generates a daily compliance report.

``false``: Daily reports are not generated. 

________

Logging
``````````````````````````
Log To The Console ``"EnableConsole": true`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	

``true``: Output log messages to the console based on **ConsoleLevel** option. The server writes messages to the standard output stream (stdout).

Console Log Level ``"ConsoleLevel": "DEBUG"``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Level of detail at which log events are written to the console when **EnableConsole**= ``true``. 

``ERROR``: Outputs only error messages.

``INFO``: Outputs error messages and information around startup and initialization,

``DEBUG``: Prints high detail for developers debugging issues.

Log To File ``"EnableFile": true``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
``true``:  Log files are written to files specified in **FileLocation**.

File Log Level ``"FileLevel": "INFO"``  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Level of detail at which log events are written to log files when **EnableFile**=``true``.

``ERROR``: Outputs only error messages.

``INFO``: Outputs error messages and information around startup and initialization,

``DEBUG``: Prints high detail for developers debugging issues.

File Location ``"FileLocation": ""``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
Directory to which log files are written. If blank, log files write to ./logs/mattermost/mattermost.log. Log rotation is enabled and every 10,000 lines of log information is written to new files stored in the same directory, for example mattermost.2015-09-23.001, mattermost.2015-09-23.002, and so forth.

File Format ``"FileFormat": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Format of log message output. If blank, FileFormat = "[%D %T] [%L] (%S) %M", where:

.. list-table::
   :widths: 20 80

   * - %T
     - Time (15:04:05 MST) 
   * - %t
     - Time (15:04) 
   * - %D
     - Date (2006/01/02)
   * - %d
     - Date (01/02/06) 
   * - %L
     - Level (FNST, FINE, DEBG, TRAC, WARN, EROR, CRIT)
   * - %S
     - Source
   * - %M
     - Message  

________


Authentication
-------------------------------
Authentication settings to enable account creation and sign in with email, GitLab OAuth or LDAP.

Email
``````````````````````````
Allow Sign Up With Email ``"EnableSignUpWithEmail": true``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

``true``: Allow team creation and account signup using email and password.

``false``: Email signup is disabled and users are not able to invite new members. This limits signup to single-sign-on services like OAuth or LDAP.  

Allow Sign In With Email ``"EnableSignInWithEmail": true``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  

``true``: Mattermost allows users to sign in using their email and password.

``false``: sign in with email is disabled and does not appear on the login screen.

Allow Sign In With Username ``EnableSignInWithUsername": false`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``true``: Mattermost allows users to sign in using their username and password. This setting is typically only used when email verification is disabled.

``false``: sign in with username is disabled and does not appear on the login screen.

________

GitLab
``````````````````````````
Enable Sign Up With GitLab ``"Enable": false`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Allow team creation and account signup using GitLab OAuth. To configure, input the **Secret** and **Id** credentials. 

``false``: GitLab OAuth cannot be used for team creation or account signup. 

Id ``"Id": ""``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Obtain this value by logging into your GitLab account. Go to Profile Settings > Applications > New Application, enter a Name, then enter Redirect URLs ``https://<your-mattermost-url>/login/gitlab/complete`` (example: ``https://example.com:8065/login/gitlab/complete``and ``https://<your-mattermost-url>/signup/gitlab/complete``.

Secret ``"Secret": ""``  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Obtain this value by logging into your GitLab account. Go to Profile Settings > Applications > New Application, enter a Name, then enter Redirect URLs ``https://<your-mattermost-url>/login/gitlab/complete`` (example: ``https://example.com:8065/login/gitlab/complete``and ``https://<your-mattermost-url>/signup/gitlab/complete``.

User API Endpoint ``"UserApiEndpoint": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Enter ``https://<your-gitlab-url>/oauth/authorize`` (example: ``https://example.com:3000/api/v3/user``). Use HTTP or HTTPS depending on how your server is configured.

Auth Endpoint ``"AuthEndpoint": ""``  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Enter ``https://<your-gitlab-url>/oauth/authorize`` (example: ``https://example.com:3000/oauth/authorize``). Use HTTP or HTTPS depending on how your server is configured.

Token Endpoint ``"TokenEndpoint": ""``  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Enter ``https://<your-gitlab-url>/oauth/authorize`` (example: ``https://example.com:3000/oauth/token``). Use HTTP or HTTPS depending on how your server is configured.

________

LDAP (Enterprise)
```````````````````````````
Enable Login With LDAP ``"Enable": false``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Mattermost allows login using LDAP.

LDAP Server ``"LdapServer": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
The domain or IP address of the LDAP server.

LDAP Port ``"LdapPort": 389``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The port Mattermost will use to connect to the AD/LDAP server. Default is 389.

Connection Security ``"ConnectionSecurity": ""``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
The type of connection security Mattermost uses to connect to LDAP. 

``""``: No encryption, Mattermost will not attempt to establish an encrypted connection to the LDAP server.

``TLS``: Encrypts the communication between Mattermost and your server using TLS. 

``STARTTLS``: Takes an existing insecure connection and attempts to upgrade it to a secure connection using TLS. 

If the "No encryption" option is selected it is highly recommended that the LDAP connection is secured outside of Mattermost, for example, by adding a stunnel proxy. 

Base DN ``"BaseDN": ""``  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
The **Base Distinguished Name** of the location where Mattermost should start its search for users in the LDAP tree.

Bind Username ``"BindUsername": ""``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
The username used to perform the AD/LDAP search. This should be an account created specifically for use with Mattermost  Its permissions should be limited to read-only access to the portion of the LDAP tree specified in the **Base DN** field. When using Active Directory, **Bind Username** should specify domain in ``DOMAIN/username`` format. 

Bind Password ``"BindPassword": ""``  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Password of the user given in **Bind Username**.

User Filter ``"UserFilter": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
(Optional) Enter an LDAP Filter to use when searching for user objects (accepts `general syntax <http://www.ldapexplorer.com/en/manual/109010000-ldap-filter-syntax.htm>`_). Only the users selected by the query will be able to access Mattermost. For Active Directory, the query to filter out disabled users is ``(&(objectCategory=Person)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))``

This filter uses the permissions of the **Bind Username** account to execute the search. Administrators should make sure to use a specially created account for Bind Username with read-only access to the portion of the LDAP tree specified in the **Base DN** field. 

First Name Attribute ``"FirstNameAttribute": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The attribute in the LDAP server that will be used to populate the first name of users in Mattermost.

Last Name Attribute ``"LastNameAttribute": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The attribute in the LDAP server that will be used to populate the last name of users in Mattermost.

Nickname Attribute ``"NicknameAttribute": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
(Optional) The attribute in the LDAP server that will be used to populate the nickname of users in Mattermost.

Email Attribute ``"EmailAttribute": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The attribute in the LDAP server that will be used to populate the email addresses of users in Mattermost. 

Email notifications will be sent to this email address, and this email address may be viewable by other Mattermost users depending on privacy settings choosen by the System Admin. 

Username Attribute ``"UsernameAttribute": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The attribute in the LDAP server that will be used to populate the username field in Mattermost user interface. This attribute will be used within the Mattermost user interface to identify and mention users. For example, if a Username Attribute is set to **john.smith** a user typing ``@john`` will see ``@john.smith`` in their auto-complete options and posting a message with ``@john.smith`` will send a notification to that user that they've been mentioned. 

The **Username Attribute** may be set to the same value used to sign-in to the system, called an **ID Attribute**, or it can be mapped to a different value. 

ID Attribute ``"IdAttribute": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The attribute in the LDAP server that will be used as a unique identifier in Mattermost. It serves two purposes: 

This value is used to sign in to Mattermost in the **LDAP Username** field on the sign in page. This attribute can be the same as the **Username Attribute** field above, which is what is used to identify users in the Mattermost interface, or it can be a different value, for example a User ID number. If your team typically uses ``DOMAIN\username`` to sign in to other services with LDAP, you may enter a field name that maps to ``DOMAIN\username`` to maintain consistency between sites.

**This is the attribute that will be used to create unique Mattermost accounts.** This attribute should be an LDAP attribute with a value that does not change, such as ``username`` or ``uid``. If a user’s **ID Attribute** changes and the user attempts to login the Mattermost server will attempt to create a new Mattermost user account based on the new **ID Attribute** and fail since new Mattermost users accounts can't be created with duplicate email addresses or Mattermost usernames (as defined in the **Username Attribute**).  

Skip Certificate Verification ``"SkipCertificateVerification": false`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
(Optional) The attribute in the LDAP server that will be used to populate the nickname of users in Mattermost.

``true``: Skips the certificate verification step for TLS or STARTTLS connections. Not recommended for production environments where TLS is required. For testing only.

Synchronization Interval (minutes) ``"SyncIntervalMinutes": 60``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set how often Mattermost accounts synchronize attributes with AD/LDAP, in minutes. When synchronizing, Mattermost queries AD/LDAP for relevant account information and updates Mattermost accounts based on changes to attributes (first name, last name, and nickname). When accounts are disabled in AD/LDAP users can no longer sign-in to Mattermost using AD/LDAP credentials, and their active sessions are revoked once Mattermost synchronizes attributes. Disabling a user in AD/LDAP does not automatically set its Mattermost account to "Inactive" it only disables AD/LDAP authentication. 

Query Timeout ``"QueryTimeout": 60`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The timeout value for queries to the LDAP server. Increase this value if you are getting timeout errors caused by a slow LDAP server.

Login Field Name ``"LoginFieldName": ""``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The placeholder text that appears in the login field on the login page. Typically this would be whatever name is used to refer to LDAP credentials in your company, so it is recognizable to your users. Defaults to **LDAP Username**.

________


Security
--------------------------------
Configure security settings for account creation, login, public links and connection requests.

Sign Up
```````````````````````````
Require Email Verification ``"RequireEmailVerification": false`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Require email verification after account creation prior to allowing login.

``false``: Users do not need to verify their email address prior to login. Developers may set this field to false so skip sending verification emails for faster development.

Invite Salt ``"InviteSalt": "bjlSR4QqkXFBr7TP4oDzlfZmcNuH9YoS"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
32-character (to be randomly generated via Admin Console) salt added to signing of email invites. Click **Regenerate** to create new salt.

Enable Open Server ``"EnableOpenServer": false`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Users can sign up to the server from the root page without an invite. 

``false``: Users can only sign up to the server if they receive an invite.

________

Login
```````````````````````````
Password Reset Salt ``"PasswordResetSalt": "vZ4DcKyVVRlKHHJpexcuXzojkE5PZ5eL"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
32-character (to be randomly generated via Admin Console) salt added to signing of password reset emails. Click **Regenerate** to create new salt.

Maximum Login Attempts ``"MaximumLoginAttempts": 10`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Failed login attempts allowed before a user is locked out and required to reset their password via email.

Enable Multi-factor Authentication ``"EnableSecurityFixAlert": true`` (Enterprise) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: When true, users will be given the option to require a phone-based passcode, in addition to their password-based authentication, to sign-in to the Mattermost server. Specifically, they will be asked to download the `Google Authenticator <https://en.wikipedia.org/wiki/Google_Authenticator>`_ app to their iOS or Android mobile device, connect the app with their account, and then enter a passcode generated by the app on their phone whenever they log in to the Mattermost server.

________

Public Links
```````````````````````````
Share Public File Link ``"EnablePublicLink": true`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Allow users to share public links to files and images when previewing.

``false``: The Get Public Link option is hidden from the image preview user interface.

Public Link Salt ``"PublicLinkSalt": "A705AklYF8MFDOfcwh3I488G8vtLlVip"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
32-character (to be randomly generated via Admin Console) salt added to signing of public image links. Click **Regenerate** to create new salt.

_________

Sessions
``````````````````````````
Session Length for Web in days ``"SessionLengthWebInDays" : 30`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set the number of days before web sessions expire and users will need to log in again.

Session Length for Mobile in days ``"SessionLengthMobileInDays" : 30`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set the number of days before native mobile sessions expire.

Session Length for SSO in days ``"SessionLengthSSOInDays" : 30`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set the number of days before SSO sessions expire.

Session Cache in Minutes ``"SessionCacheInMinutes" : 10`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set the number of minutes to cache a session in memory.

________

Connections
``````````````````````````
Allow Cross-origin Requests ``"AllowCorsFrom": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Enable HTTP cross-origin requests from specific domains separated by spaces. Type ``*`` to allow CORS from any domain or leave it blank to disable it.

Enable Insecure Outgoing Connections ``"EnableInsecureOutgoingConnections": false`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Outgoing HTTPS requests can accept unverified, self-signed certificates. For example, outgoing webhooks to a server with a self-signed TLS certificate, using any domain, will be allowed.

``false``: Only secure HTTPS requests are allowed.

Security note: Enabling this feature makes these connections susceptible to man-in-the-middle attacks.

________

Notifications
--------------------------------
Settings to configure email and mobile push notifications.

Email
``````````````````````````
Send Email Notifications ``"SendEmailNotifications": false`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Enables sending of email notifications. 

``false``: Disables email notifications for developers who may want to skip email setup for faster development. Setting this to true removes the **Preview Mode: Email notifications have not been configured** banner (requires logging out and logging back in after setting is changed)

Notification Display Name ``"FeedbackName": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Name displayed on email account used when sending notification emails from Mattermost system.

Notification Email Address ``"FeedbackEmail": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Address displayed on email account used when sending notification emails from Mattermost system.

SMTP Username ``"SMTPUsername": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Obtain this credential from the administrator setting up your email server.

SMTP Password ``"SMTPPassword": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Obtain this credential from the administrator setting up your email server.

SMTP Server ``"SMTPServer": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Location of SMTP email server.

SMTP Port ``"SMTPPort": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Port of SMTP email server.

Connection Security ``"ConnectionSecurity": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``""``: Send email over an unsecure connection.

``TLS``: Communication between Mattermost and your email server is encrypted.

``STARTTLS``: Attempts to upgrade an existing insecure connection to a secure connection using TLS.

Enable Security Alerts ``"EnableSecurityFixAlert": true`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: System Admins are notified by email if a relevant security fix alert has been announced in the last 12 hours. Requires email to be enabled.

________

Mobile Push
```````````````````````````
Send Push Notifications ``"SendPushNotifications": false`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Your Mattermost server sends mobile push notifications to the server specified in **PushNotificationServer**.

``false``: Mobile push notifications are disabled.  

Push Notification Server ``"PushNotificationServer": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Location of Mattermost Push Notification Service (MPNS), which re-sends push notifications from Mattermost to services like Apple Push Notification Service (APNS) and Google Cloud Messaging (GCM).  

To confirm push notifications are working, connect to the `Mattermost iOS App on iTunes <https://itunes.apple.com/us/app/mattermost/id984966508?mt=8>`_ or the `Mattermost Android App on Google Play <https://play.google.com/store/apps/details?id=com.mattermost.mattermost&hl=en>`_: 

- For Enterprise Edition, enter ``http://push.mattermost.com``
- For Team Edition, enter ``http://push-test.mattermost.com``

Please review full documentation on `push Notifications and mobile applications <http://docs.mattermost.com/deployment/push.html>`_ including guidance on compiling your own mobile apps and MPNS before deploying to production. 

Note: The ``http://push-test.mattermost.com`` provided for testing push notifications prior to compiling your own service please make sure `to read about its limitations <http://docs.mattermost.com/deployment/push.html#push-notifications-for-team-edition-users>`_. 

Push Notification Contents ``"PushNotificationContents": "generic"``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``generic``: Selecting "Send generic description with user and channel names" provides push notifications with generic messages, including names of users and channels but no specific details from the message text.  

``full``: Selecting "Send full message snippet" sends excerpts from messages triggering notifications with specifics and may include confidential information sent in messages. If your Push Notification Service is outside your firewall, it is HIGHLY RECOMMENDED this option only be used with an "https" protocol to encrypt the connection.

**Troubleshooting Push Notifications**

To confirm push notifications are working: 

1. Set **System Console** > **Email Settings** > **Send Push Notifications** to `true`.
2. Set **System Console** > **Email Settings** > **Send Push Notifications** to `true` (if using Mattermost 1.4 or earlier).
3. Set **System Console** > **Email Settings** > **Push Notification Server** to ``http://push.mattermost.com`` if using Enterprise Edition or if using Team Edition, set the value to `http://push-test.mattermost.com`.
4. Download and install `the Mattermost iOS app from iTunes <https://itunes.apple.com/us/app/mattermost/id984966508?mt=8>`_ on your iPhone or iPad and log in to your team site. 
5. Close the app on your device, and close any other connections to your team site.
6. Wait 5 minutes and have another team member send you a direct messages, which should trigger a push notification to the Mattermost app on your mobile device. 
7. You should receive a push notification on your device alerting you of the direct message. 

If you did not receive an alert: 

1. Set **System Console** > **Log Settings** > **File Log Level** to `DEBUG` (make sure to set this back to `INFO` after troubleshooting to save disk space). 
2. Repeat the above steps
3. Go to **System Console** > **OTHER** > **Logs** and copy the log output into a file 
4. For Enterprise Edition customers, `submit a support request with the file attached <https://mattermost.zendesk.com/hc/en-us/requests/new>`_. For Team Edition users, please start a thread in the `Troubleshooting forum <https://forum.mattermost.org/t/how-to-use-the-troubleshooting-forum/150>`_ for peer-to-peer support. 

________

Integrations
--------------------------------
Settings to configure webhooks, slash commands and external integration services.

Webhooks and Commands
``````````````````````````
Enable Incoming Webhooks ``"EnableIncomingWebhooks": true``   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Developers building integrations can create webhook URLs for channels and private groups. Please see our `documentation page <http://docs.mattermost.com/developer/webhooks-incoming.html>`_ to learn about creating webhooks, view samples, and to let the community know about integrations you have built. 

``true``: Incoming webhooks will be allowed. To manage incoming webhooks, go to **Account Settings > Integrations**. The webhook URLs created in Account Settings can be used by external applications to create posts in any channels or private groups that you have access to.

``false``: The Integrations > Incoming Webhooks section of Account Settings is hidden and all incoming webhooks are disabled.

Security note: By enabling this feature, users may be able to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`_ by attempting to impersonate other users. To combat these attacks, a BOT tag appears next to all posts from a webhook. Enable at your own risk.

Enable Outgoing Webhooks ``"EnableOutgoingWebhooks": true``   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Developers building integrations can create webhook tokens for public channels. Trigger words are used to fire new message events to external integrations. For security reasons, outgoing webhooks are only available in public channels. Please see our `documentation page <http://docs.mattermost.com/developer/webhooks-outgoing.html>`_ to learn about creating webhooks and view samples. 

``true``: Outgoing webhooks will be allowed. To manage outgoing webhooks, go to **Account Settings > Integrations**.

``false``: The Integrations > Outgoing Webhooks section of Account Settings is hidden and all outgoing webhooks are disabled.

Security note: By enabling this feature, users may be able to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`_ by attempting to impersonate other users. To combat these attacks, a BOT tag appears next to all posts from a webhook. Enable at your own risk.

Enable Slash Commands ``"EnableCommands": false`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Slash commands send events to external integrations that send a response back to Mattermost. 

``true``: Allow users to create custom slash commands from **Main Menu** > **Integrations** > **Commands**.

``false``: Slash Commands are hidden in the **Integrations** user interface.

Enable Integrations for Admin Only ``"EnableOnlyAdminIntegrations": true`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: User created integrations can only be created by System or Team Admins. Members who are not admins trying to create integrations will hit an error message on the **Integrations** page.

``false``: Any team members can create integrations from **Main Menu** > **Integrations**.

Enable Overriding Usernames from Webhooks and Slash Commands ``"EnablePostUsernameOverride": false`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Webhooks will be allowed to change the username they are posting as.

``false``: Webhooks can only post as the username they were set up with. See http://mattermost.org/webhooks for more details.

Enable Overriding Icon from Webhooks and Slash Commands ``"EnablePostIconOverride": false`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Webhooks will be allowed to change the icon they post with.

``false``: Webhooks can only post with the profile picture of the account they were set up with. See http://mattermost.org/webhooks for more details.

________

External Services
```````````````````````````
Segment Developer Key ``"SegmentDeveloperKey": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For deployments seeking additional tracking of system behavior using Segment.com, you can enter a Segment WRITE_KEY using this field. This value works like a tracking code and is used in client-side Javascript and will send events to Segment.com attributed to the account you used to generate the WRITE_KEY.

Google Developer Key ``"GoogleDeveloperKey": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Mattermost offers the ability to embed YouTube videos from URLs shared by end users. If Google detects the number of views is exceedingly high, they may throttle embed access. Should this occur, you can remove the throttle by registering for a Google Developer Key and entering it in this field following these instructions: https://www.youtube.com/watch?v=Im69kzhpR3I. Your Google Developer Key is used in client-side Javascript.

Using a Google Developer Key allows Mattermost to detect when a video is no longer available and display the post with a *Video not found* label.

________

Files
--------------------------------
Settings to configure files storage and image handling.

Storage
```````````````````````````
Store Files In ``"DriverName": "local"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
System used for file storage. “local”: Files and images are stored on the local file system. “amazons3”: Files and images are stored on Amazon S3 based on the provided access key, bucket and region fields.

Local Directory Location ``"Directory": "./data/"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Directory to which files are written. If blank, directory will be set to ./data/.

Amazon S3 Access Key Id ``"AmazonS3AccessKeyId": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Obtain this credential from your Amazon EC2 administrator.

Amazon S3 Secret Access Key ``"AmazonS3SecretAccessKey": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Obtain this credential from your Amazon EC2 administrator.

Amazon S3 Bucket ``"AmazonS3Bucket": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Name you selected for your S3 bucket in AWS.

Amazon S3 Region ``"AmazonS3Region": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
AWS region you selected for creating your S3 bucket. Refer to `AWS Reference Documentation <http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region>`_ and choose this variable from the Region column.

________

Images
```````````````````````````
Thumbnail Width ``"ThumbnailWidth": 120`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Width of thumbnails generated from uploaded images. Updating this value changes how thumbnail images render in future, but does not change images created in the past.

Thumbnail Height ``"ThumbnailHeight": 100`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Height of thumbnails generated from uploaded images. Updating this value changes how thumbnail images render in future, but does not change images created in the past.

Preview Width ``"PreviewWidth": 1024`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Maximum width of preview image. Updating this value changes how preview images render in future, but does not change images created in the past.

Preview Height ``"PreviewHeight": 0`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Maximum height of preview image ("0": Sets to auto-size). Updating this value changes how preview images render in future, but does not change images created in the past.

Profile Width ``"ProfileWidth": 128`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The width to which profile pictures are resized after being uploaded via Account Settings.

Profile Height ``"ProfileHeight": 128`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The height to which profile pictures are resized after being uploaded via Account Settings.

________

Customization
--------------------------------
Settings to customize your deployment with custom branding and legal and support links.

Custom Branding
```````````````````````````

Site Name ``"SiteName": "Mattermost"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Name of service shown in login screens and UI.


Enable Custom Branding ``"EnableCustomBrand": false`` (Enterprise)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Enables custom branding to show a JPG image some custom text on the server login page. 

Custom Brand Image (Enterprise)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Custom JPG image is displayed on left side of server login page. Recommended maximum image size is less than 2 MB because image will be loaded for every user who logs in.

Custom Brand Text ``"CustomBrandText": [BLANK]`` (Enterprise)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Custom text will be shown below custom brand image on left side of server login page. Maximum 500 characters allowed. You can format this text using the same `Markdown formatting codes <http://docs.mattermost.com/help/messaging/formatting-text.html>`_ as using in Mattermost messages. 

________

Legal and Support
```````````````````````````
Terms of Service link ``"TermsOfServiceLink": "/static/help/terms.html"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Configurable link to Terms of Service your organization may provide to end users. By default, links to an editable file hosted in the ``static/help/terms.html`` found in the directory where the Mattermost server installed. Default file may be updated to state the terms under which your organization is providing its server to end users, in addition to the "Mattermost Conditions of Use" notice to end users that must also be shown to users from the "Terms of Service" link. 

Privacy Policy link ``"PrivacyPolicyLink": "/static/help/privacy.html"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Configurable link to Privacy Policy your organization may provide to end users. By default, links to an editable file hosted in the ``static/help/privacy.html`` found in the directory where the Mattermost server installed. 

About link ``"AboutLink": "/static/help/about.html"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Configurable link to an About page describing your organization may provide to end users. By default, links to an editable file hosted in the ``static/help/about.html`` found in the directory where the Mattermost server installed. 

Help link ``"HelpLink": "/static/help/help.html"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Configurable link to an About page describing your organization may provide to end users. By default, points to Mattermost default help documentation. Can be links to an editable file hosted in the ``static/help/help.html`` found in the directory where the Mattermost server installed. 

Report a Problem link ``"ReportAProblemLink": "/static/help/report_problem.html"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set the link for the support website.

Support email ``"SupportEmail":"feedback@mattermost.com"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set an email for feedback or support requests.

________


Advanced
--------------------------------
Advanced settings to configure rate limiting, databases and developer options.

Rate Limiting
```````````````````````````
Changing properties in this section will require a server restart before taking effect.

Enable Rate Limiter ``"EnableRateLimiter": true`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: APIs are throttled at the rate specified by **PerSec**.

Number Of Queries Per Second ``"PerSec": 10`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Throttle API at this number of requests per second if rate limiting is enabled.

Memory Store Size ``"MemoryStoreSize": 10000`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Maximum number of user sessions connected to the system as determined by **VaryByRemoteAddr** and **VaryByHeader** variables.

Vary By Remote Address ``"VaryByRemoteAddr": true`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Rate limit API access by IP address.

Vary By HTTP Header ``"VaryByHeader": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Vary rate limiting by HTTP header field specified (e.g. when configuring Ngnix set to "X-Real-IP", when configuring AmazonELB set to "X-Forwarded-For").

________


Database
```````````````````````````
Changing properties in this section will require a server restart before taking effect. 

Driver Name ``"DriverName": "mysql"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This setting can only be changed from config.json file, it cannot be changed from the System Console user interface.

``mysql``: enables driver to MySQL database.

``postgres``: enables driver to PostgreSQL database.

Data Source ``"DataSource": "mmuser:mostest@tcp(dockerhost:3306)/mattermost_test?charset=utf8mb4,utf8"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is the connection string to the master database. When **DriverName** ="postgres" then use a connection string in the form ``postgres://mmuser:password@localhost:5432/mattermost_test?sslmode=disable&connect_timeout=10``. This setting can only be changed from config.json file, it cannot be changed from the System Console user interface.

Maximum Idle Connections ``"MaxIdleConns": 10`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Maximum number of idle connections held open to the database.

Maximum Open Connections ``"MaxOpenConns": 10`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Maximum number of open connections held open to the database.

At Rest Encrypt Key ``"AtRestEncryptKey": "7rAh6iwQCkV4cA1Gsg3fgGOXJAQ43QVg"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
32-character (to be randomly generated via Admin Console) salt available to encrypt and decrypt sensitive fields in database.

Trace ``"Trace": false`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Executing SQL statements are written to the log for development.

Recycle Database Connections (Enterprise)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This button reconnects to the database listed in the configuration settings. All old connections are closed after 20s.

The workflow for failover without downing the server is to change the database line in the config.json file, click **Reload Configuration from Disk** in the General > Configuration section then click **Recycle Database Connections**.

________


Developer
```````````````````````````

Enable Testing ``"EnableTesting": false`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: `/loadtest` slash command is enabled to load test accounts and test data.

Enable Developer Mode ``"EnableDeveloper": false`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Users are alerted to any console errors that occur.

________


Settings configurable in config.json
-------------------------------

There are a number of settings customizable in ``config.json`` unavailable in the System Console and require updating from the file itself. 

Service Settings
```````````````````````````

Enable OAuth Service Provider ``"EnableOAuthServiceProvider": false`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
``true``: Allow Mattermost to function as an OAuth provider, allowing 3rd party apps access to your user store for authentication.

WebSocket Secure Port ``"WebsocketSecurePort" : 443`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(Optional) This setting defines the port on which the secured WebSocket will listen using the `wss` protocol. Otherwise it defaults to `443`. When the client attempts to make a WebSocket connection it first checks to see if the page is loaded with HTTPS. If so, it will use the secure WebSocket connection. If not, it will use the unsecure WebSocket connection. IT IS HIGHLY RECOMMENDED PRODUCTION DEPLOYMENTS ONLY OPERATE UNDER HTTPS AND WSS. 

WebSocket Port ``WebsocketPort": 80`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(Optional) this setting defines the port on which the unsecured WebSocket will listen using the `ws` protocol. Otherwise it defaults to `80`. When the client attempts to make a WebSocket connection it first checks to see if the page is loaded with HTTPS. If so, it will use the secure WebSocket connection. If not, it will use the unsecure WebSocket connection. IT IS HIGHLY RECOMMENDED PRODUCTION DEPLOYMENTS ONLY OPERATE UNDER HTTPS AND WSS. 

________


File Settings
```````````````````````````
Initial Font ``"InitialFont": "luximbi.ttf"`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Font used in auto-generated profile pics with colored backgrounds.

Amazon S3 Endpoint ``"AmazonS3Endpoint": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set an endpoint URL for an Amazon S3 instance.

Amazon S3 Bucket Endpoint ``"AmazonS3BucketEndpoint": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set an endpoint URL for Amazon S3 buckets.

Amazon S3 Location Constraint ``"AmazonS3LocationConstraint": false`` 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set whether the S3 region is location constrained.

Amazon S3 Lowercase Bucket ``"AmazonS3LowercaseBucket": false``   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set whether bucket names are fully lowercase or not.

________


GitLab Settings
```````````````````````````
Scope ``"Scope": ""`` 
~~~~~~~~~~~~~~~~~~~~~~~~~
Standard setting for OAuth to determine the scope of information shared with OAuth client. Not currently supported by GitLab OAuth.
