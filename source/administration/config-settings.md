# Configuration Settings
Configuration settings can be modified by system administrators from the system console or directly in the config.json file.

## System Console Settings

The System Console user interface lets system administrators manage a Mattermost server and multiple teams from a web-based user interface. The first user added to a new Mattermost install is assigned the system administrator role and can access the System Console from the main menu of any team. 

Setting changes in the System Console are stored in `config/config.json`. 

Note: For any setting not explicitly set in `config.json` the Mattermost server will use the default value as documented here, and which can be observed in the default `config/config.json` file included in each Mattermost release. 

### Service Settings

General settings to configure the listening address, login security, testing, webhooks and service integration of Mattermost. 

#### System

**Listen Address** (`"ListenAddress": ":8065"`)  

The IP address on which to listen and the port on which to bind. Entering ":8065" will bind to all interfaces or you can choose one like `127.0.0.1:8065`. Changing this will require a server restart before taking effect.

**Maximum Login Attempts** (`"MaximumLoginAttempts": 10`)  

Failed login attempts allowed before a user is locked out and required to reset their password via email.

**Segment Developer Key** (`"SegmentDeveloperKey": ""`)  

For users running SaaS services, signup for a key at Segment.com to track metrics.

**Google Developer Key** (`"GoogleDeveloperKey": ""`)  

Set this key to enable embedding of YouTube video previews based on hyperlinks appearing in messages or comments. Instructions to obtain a key available at https://www.youtube.com/watch?v=Im69kzhpR3I. Leaving the field blank disables the automatic generation of YouTube video previews from links.

**Enable Testing** (`"EnableTesting": false`)  

`true`: `/loadtest` slash command is enabled to load test accounts and test data.

**Enable Developer Mode** (`"EnableDeveloper": false`)  

`true`: Users are alerted to any console errors that occur.

**Enable Security Fix Alert** (`"EnableSecurityFixAlert": true`)  

`true`: System Administrators are notified by email if a relevant security fix alert has been announced in the last 12 hours. Requires email to be enabled.

**Enable Insecure Outgoing Connections** (`"EnableInsecureOutgoingConnections": false`)  

`true`: Outgoing HTTPS requests can accept unverified, self-signed certificates. For example, outgoing webhooks to a server with a self-signed TLS certificate, using any domain, will be allowed; `false`: Only secure HTTPS requests are allowed.

Security note: Enabling this feature makes these connections susceptible to man-in-the-middle attacks.

**Session Length for Web in days** (`"SessionLengthWebInDays" : 30`)  

Set the number of days before web sessions expire and users will need to log in again.

**Session Length for Mobile in days** (`"SessionLengthMobileInDays" : 30`)  

Set the number of days before native mobile sessions expire.

**Session Length for SSO in days** (`"SessionLengthSSOInDays" : 30`)  

Set the number of days before SSO sessions expire.

**Session Cache in Minutes** (`"SessionCacheInMinutes" : 10`)  

Set the number of minutes to cache a session in memory.

#### Webhooks and Slash Commands

**Enable Incoming Webhooks** (`"EnableIncomingWebhooks": true`)    

Developers building integrations can create webhook URLs for channels and private groups. Please see our [documentation page](http://docs.mattermost.com/developer/webhooks-incoming.html) to learn about creating webhooks, view samples, and to let the community know about integrations you have built. `true`: Incoming webhooks will be allowed. To manage incoming webhooks, go to **Account Settings > Integrations**. The webhook URLs created in Account Settings can be used by external applications to create posts in any channels or private groups that you have access to; `false`: The Integrations > Incoming Webhooks section of Account Settings is hidden and all incoming webhooks are disabled.

Security note: By enabling this feature, users may be able to perform [phishing attacks](https://en.wikipedia.org/wiki/Phishing) by attempting to impersonate other users. To combat these attacks, a BOT tag appears next to all posts from a webhook. Enable at your own risk.

**Enable Outgoing Webhooks** (`"EnableOutgoingWebhooks": true`)    

Developers building integrations can create webhook tokens for public channels. Trigger words are used to fire new message events to external integrations. For security reasons, outgoing webhooks are only available in public channels. Please see our [documentation page](http://docs.mattermost.com/developer/webhooks-outgoing.html) to learn about creating webhooks and view samples. `true`: Outgoing webhooks will be allowed. To manage outgoing webhooks, go to **Account Settings > Integrations**; `false`: The Integrations > Outgoing Webhooks section of Account Settings is hidden and all outgoing webhooks are disabled.

Security note: By enabling this feature, users may be able to perform [phishing attacks](https://en.wikipedia.org/wiki/Phishing) by attempting to impersonate other users. To combat these attacks, a BOT tag appears next to all posts from a webhook. Enable at your own risk.

**Enable Slash Commands** (`"EnableCommands": false`)  

Slash commands send events to external integrations that send a response back to Mattermost. `true`: Allow users to create custom slash commands from **Account Settings** > **Integrations** > **Commands**; `false`: Slash Commands are hidden in the **Integrations** user interface.

**Enable Integrations for Admin Only** (`"EnableOnlyAdminIntegrations": true`)  

`true`: User created integrations can only be created by System or Team Admins. Members who are not admins trying to create integrations will hit an error message in the **Account Settings** dialog; `false`: Any team members can create integrations from **Account Settings** > **Inegrations**.

**Enable Overriding Usernames from Webhooks and Slash Commands** (`"EnablePostUsernameOverride": false`)  

`true`: Webhooks will be allowed to change the username they are posting as; `false`: Webhooks can only post as the username they were set up with. See http://mattermost.org/webhooks for more details.

**Enable Overriding Icon from Webhooks and Slash Commands** (`"EnablePostIconOverride": false`)  

`true`: Webhooks will be allowed to change the icon they post with; `false`: Webhooks can only post with the profile picture of the account they were set up with. See http://mattermost.org/webhooks for more details.

### Team Settings

Settings to configure the appearance, size, and access options for teams.

**Site Name** (`"SiteName": "Mattermost"`)  

Name of service shown in login screens and UI.

**Max Users Per Team** (`"MaxUsersPerTeam": 50`)  

Maximum number of users per team, including both active and inactive users.

**Enable Team Creation** (`"EnableTeamCreation": true`)  

`true`: Ability to create a new team is enabled for all users; `false`: the ability to create teams is disabled. The Create A New Team button is hidden in the main menu UI.

**Enable User Creation** (`"EnableUserCreation": true`)  

`true`: Ability to create new accounts is enabled via inviting new members or sharing the team invite link; `false`: the ability to create accounts is disabled. The create account button displays an error when trying to signup via an email invite or team invite link.

**Restrict Creation To Domains** (`"RestrictCreationToDomains": ""`)    

Teams and user accounts can only be created by a verified email from this list of comma-separated domains (e.g. "corp.mattermost.com, mattermost.org").

**Restrict Team Names** (`"RestrictTeamNames": true`)  

`true`: Newly created team names cannot contain the following restricted words: www, web, admin, support, notify, test, demo, mail, team, channel, internal, localhost, dockerhost, stag, post, cluster, api, oauth; `false`: Newly created team names are not restricted. 

**Enable Team Directory** (`"EnableTeamListing": false`)  

`true`: Teams that are configured to appear in the team directory will appear on the system main page. Teams can configure this setting from **Team Settings > Include this team in the Team Directory**; `false`: Team directory on the system main page is disabled.


### SQL Settings

Settings to configure the data sources, connections, and encryption of SQL databases. Changing properties in this section will require a server restart before taking effect. 

**Driver Name** (`"DriverName": "mysql"`)  

`mysql`: enables driver to MySQL database; `postgres`: enables driver to PostgreSQL database. This setting can only be changed from config.json file, it cannot be changed from the System Console user interface.

**Data Source** (`"DataSource": "mmuser:mostest@tcp(dockerhost:3306)/mattermost_test?charset=utf8mb4,utf8"`)  

This is the connection string to the master database. When **DriverName**="postgres" then use a connection string in the form `postgres://mmuser:password@localhost:5432/mattermost_test?sslmode=disable&connect_timeout=10`. This setting can only be changed from config.json file, it cannot be changed from the System Console user interface.

**Maximum Idle Connections** (`"MaxIdleConns": 10`)  

Maximum number of idle connections held open to the database.

**Maximum Open Connections** (`"MaxOpenConns": 10`)  

Maximum number of open connections held open to the database.

**At Rest Encrypt Key** (`"AtRestEncryptKey": "7rAh6iwQCkV4cA1Gsg3fgGOXJAQ43QVg"`)  

32-character (to be randomly generated via Admin Console) salt available to encrypt and decrypt sensitive fields in database.

**Trace** (`"Trace": false`)  

`true`: Executing SQL statements are written to the log for development.

### Email Settings

Settings to configure email signup, notifications, security, and SMTP options. 

#### Sign Up  

**Allow Sign Up With Email** (`"EnableSignUpWithEmail": true`)  

`true`: Allow team creation and account signup using email and password; `false`: Email signup is disabled and users are not able to invite new members. This limits signup to single-sign-on services like OAuth or LDAP.

#### Sign In  

**Allow Sign In With Email** (`"EnableSignInWithEmail": true`)  

`true`: Mattermost allows users to sign in using their email and password; `false`: sign in with email is disabled and does not appear on the login screen.

**Allow Sign In With Username** (`EnableSignInWithUsername": false`)  

`true`: Mattermost allows users to sign in using their username and password. This setting is typically only used when email verification is disabled; `false`: sign in with username is disabled and does not appear on the login screen.

#### Notifications

**Send Email Notifications** (`"SendEmailNotifications": false`)  

`true`: Enables sending of email notifications. `false`: Disables email notifications for developers who may want to skip email setup for faster development. Setting this to true removes the **Preview Mode: Email notifications have not been configured** banner (requires logging out and logging back in after setting is changed)

**Require Email Verification** (`"RequireEmailVerification": false`)  

`true`: Require email verification after account creation prior to allowing login; `false`: Users do not need to verify their email address prior to login. Developers may set this field to false so skip sending verification emails for faster development.

**Notification Display Name** (`"FeedbackName": ""`)  

Name displayed on email account used when sending notification emails from Mattermost system.

**Notification Email Address** (`"FeedbackEmail": ""`)  

Address displayed on email account used when sending notification emails from Mattermost system.

#### SMTP

**SMTP Username** (`"SMTPUsername": ""`)  

Obtain this credential from the administrator setting up your email server.

**SMTP Password** (`"SMTPPassword": ""`)  

Obtain this credential from the administrator setting up your email server.

**SMTP Server** (`"SMTPServer": ""`)  

Location of SMTP email server.

**SMTP Port** (``"SMTPPort": ""`)  

Port of SMTP email server.

#### Security

**Connection Security** (`"ConnectionSecurity": ""`)  

"none": Send email over an unsecure connection; "TLS": Communication between Mattermost and your email server is encrypted; “STARTTLS”: Attempts to upgrade an existing insecure connection to a secure connection using TLS.

**Invite Salt** (`"InviteSalt": "bjlSR4QqkXFBr7TP4oDzlfZmcNuH9YoS"`)  

32-character (to be randomly generated via Admin Console) salt added to signing of email invites.

**Password Reset Salt**  (`"PasswordResetSalt": "vZ4DcKyVVRlKHHJpexcuXzojkE5PZ5eL"`)  

32-character (to be randomly generated via Admin Console) salt added to signing of password reset emails.  

#### Push Notification Settings  

**Send Push Notifications** (`"SendPushNotifications": false`)  

`true`: Your Mattermost server sends mobile push notifications to the server specified in **PushNotificationServer**; `false`: Mobile push notifications are disabled.  

**Push Notification Server** (`"PushNotificationServer": ""`)  

Location of Mattermost Push Notification Service (MPNS), which re-sends push notifications from Mattermost to services like Apple Push Notification Service (APNS) and Google Cloud Messaging (GCM).  

To confirm push notifications are working, connect to the [Mattermost iOS App on iTunes](https://itunes.apple.com/us/app/mattermost/id984966508?mt=8) or the Mattermost Android App on Google Play (release pending): 

- For Enterprise Edition, enter `http://push.mattermost.com`
- For Team Edition, enter `http://push-test.mattermost.com`

Please review full documentation on [push Notifications and mobile applications](http://docs.mattermost.com/deployment/push.html) including guidance on compiling your own mobile apps and MPNS before deploying to production. 

Note: The `http://push-test.mattermost.com` provided for testing push notifications prior to compiling your own service please make sure [to read about its limitations.](http://docs.mattermost.com/deployment/push.html#push-notifications-for-team-edition-users) 

#### Troubleshooting Push Notifications 

To confirm push notifications are working: 

1. Set **System Console** > **Email Settings** > **Send Push Notifications** to `true`.
2. Set **System Console** > **Email Settings** > **Send Push Notifications** to `true` (if using Mattermost 1.4 or earlier).
3. Set **System Console** > **Email Settings** > **Push Notification Server** to `http://push.mattermost.com` if using Enterprise Edition or if using Team Edition, set the value to `http://push-test.mattermost.com`.
4. Download and install [the Mattermost iOS app from iTunes](https://itunes.apple.com/us/app/mattermost/id984966508?mt=8) on your iPhone or iPad and log in to your team site. 
5. Close the app on your device, and close any other connections to your team site.
6. Wait 5 minutes and have another team member send you a direct messages, which should trigger a push notification to the Mattermost app on your mobile device. 
7. You should receive a push notification on your device alerting you of the direct message. 

If you did not receive an alert: 

1. Set **System Console** > **Log Settings** > **File Log Level** to `DEBUG` (make sure to set this back to `INFO` after troubleshooting to save disk space). 
2. Repeat the above steps
3. Go to **System Console** > **OTHER** > **Logs** and copy the log output into a file 
4. For Enterprise Edition customers, [submit a support request with the file attached](https://mattermost.zendesk.com/hc/en-us/requests/new). For Team Edition users, please start a thread in the [Troubleshooting forum](https://forum.mattermost.org/t/how-to-use-the-troubleshooting-forum/150) for peer-to-peer support. 

### File Settings

Settings to configure storage, appearance, and security of files and images.

#### File Storage

**Store Files In** (`"DriverName": "local"`)  

System used for file storage. “local”: Files and images are stored on the local file system. “amazons3”: Files and images are stored on Amazon S3 based on the provided access key, bucket and region fields.

**Local Directory Location** (`"Directory": "./data/"`)  

Directory to which files are written. If blank, directory will be set to ./data/.

**Amazon S3 Access Key Id** (`"AmazonS3AccessKeyId": ""`)  

Obtain this credential from your Amazon EC2 administrator.

**Amazon S3 Secret Access Key** (`"AmazonS3SecretAccessKey": ""`)  

Obtain this credential from your Amazon EC2 administrator.

**Amazon S3 Bucket** (`"AmazonS3Bucket": ""`)  

Name you selected for your S3 bucket in AWS.

**Amazon S3 Region** (`"AmazonS3Region": ""`)  

AWS region you selected for creating your S3 bucket. Refer to [AWS Reference Documentation](http://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region) and choose this variable from the Region column.

#### Image Settings

**Thumbnail Width** (`"ThumbnailWidth": 120`)  

Width of thumbnails generated from uploaded images. Updating this value changes how thumbnail images render in future, but does not change images created in the past.

**Thumbnail Height** (`"ThumbnailHeight": 100`)  

Height of thumbnails generated from uploaded images. Updating this value changes how thumbnail images render in future, but does not change images created in the past.

**Preview Width** (`"PreviewWidth": 1024`)  

Maximum width of preview image. Updating this value changes how preview images render in future, but does not change images created in the past.

**Preview Height** (`"PreviewHeight": 0`)  

Maximum height of preview image ("0": Sets to auto-size). Updating this value changes how preview images render in future, but does not change images created in the past.

**Profile Width** (`"ProfileWidth": 128`)  

The width to which profile pictures are resized after being uploaded via Account Settings.

**Profile Height** (`"ProfileHeight": 128`)  

The height to which profile pictures are resized after being uploaded via Account Settings.

**Share Public File Link** (`"EnablePublicLink": true`)  

`true`: Allow users to share public links to files and images when previewing; `false`: The Get Public Link option is hidden from the image preview user interface.

**Public Link Salt** (`"PublicLinkSalt": "A705AklYF8MFDOfcwh3I488G8vtLlVip"`)  

32-character (to be randomly generated via Admin Console) salt added to signing of public image links.


### Log Settings

Settings to configure the console and log file output, detail level, format and location of error messages.

#### Console Settings

**Log To The Console** (`"EnableConsole": true`)  

`true`: Output log messages to the console based on **ConsoleLevel** option. The server writes messages to the standard output stream (stdout).

**Console Log Level** (`"ConsoleLevel": "DEBUG"`)  

Level of detail at which log events are written to the console when **EnableConsole**=true. ”ERROR”: Outputs only error messages; “INFO”: Outputs error messages and information around startup and initialization; “DEBUG”: Prints high detail for developers debugging issues.

#### Log File Settings

**Log To File** (`"EnableFile": true`)  

`true`:  Log files are written to files specified in **FileLocation**.

**File Log Level** (`"FileLevel": "INFO"`)  

Level of detail at which log events are written to log files when **EnableFile**=true. “ERROR”: Outputs only error messages; “INFO”: Outputs error messages and information around startup and initialization; “DEBUG”: Prints high detail for developers debugging issues.

**File Location** (`"FileLocation": ""`)  

Directory to which log files are written. If blank, log files write to ./logs/mattermost/mattermost.log. Log rotation is enabled and every 10,000 lines of log information is written to new files stored in the same directory, for example mattermost.2015-09-23.001, mattermost.2015-09-23.002, and so forth.

**File Format** (`"FileFormat": ""`)  

Format of log message output. If blank, **FileFormat** = "[%D %T] [%L] (%S) %M", where: 
  
    %T		Time (15:04:05 MST) 
    %t		Time (15:04) 
    %D		Date (2006/01/02) 
    %d		Date (01/02/06) 
    %L		Level (FNST, FINE, DEBG, TRAC, WARN, EROR, CRIT) 
    %S		Source 
    %M		Message

### Rate Limit Settings

Settings to enable API rate limiting and configure requests per second, user sessions and variables for rate limiting. Changing properties in this section will require a server restart before taking effect.

**Enable Rate Limiter** (`"EnableRateLimiter": true`)  

`true`: APIs are throttled at the rate specified by **PerSec**.

**Number Of Queries Per Second** (`"PerSec": 10`)  

Throttle API at this number of requests per second if **EnableRateLimiter**=true.

**Memory Store Size** (`"MemoryStoreSize": 10000`)  

Maximum number of user sessions connected to the system as determined by **VaryByRemoteAddr** and **VaryByHeader** variables.

**Vary By Remote Address** (`"VaryByRemoteAddr": true`)  

`true`: Rate limit API access by IP address.

**Vary By HTTP Header** (`"VaryByHeader": ""`)  

Vary rate limiting by HTTP header field specified (e.g. when configuring Ngnix set to "X-Real-IP", when configuring AmazonELB set to "X-Forwarded-For").

### Privacy Settings

Settings to configure the name and email privacy of users on your system.  

**Show Email Address** (`"ShowEmailAddress": true`)  

`true`: Show email address of all users; `false`: Hide email address of users from other users in the user interface, including team owners and team administrators. This is designed for managing teams where users choose to keep their contact information private.

**Show Full Name** (`"ShowFullName": true`)  

`true`: Show full name of all users; `false`: hide full name of users from other users including team owner and team administrators.

### GitLab Settings

Settings to configure account and team creation using GitLab OAuth.

**Enable Sign Up With GitLab** (`"Enable": false`)  

`true`: Allow team creation and account signup using GitLab OAuth. To configure, input the **Secret** and **Id** credentials. 

**Id** (`"Id": ""`)  

Obtain this value by logging into your GitLab account. Go to Profile Settings > Applications > New Application, enter a Name, then enter Redirect URLs `https://<your-mattermost-url>/login/gitlab/complete` (example: `https://example.com:8065/login/gitlab/complete`) and `https://<your-mattermost-url>/signup/gitlab/complete`.

**Secret** (`"Secret": ""`)  

Obtain this value by logging into your GitLab account. Go to Profile Settings > Applications > New Application, enter a Name, then enter Redirect URLs `https://<your-mattermost-url>/login/gitlab/complete` (example: `https://example.com:8065/login/gitlab/complete`) and `https://<your-mattermost-url>/signup/gitlab/complete`.

**Auth Endpoint** (`"AuthEndpoint": ""`)  

Enter `https://<your-gitlab-url>/oauth/authorize` (example: `https://example.com:3000/oauth/authorize`). Use HTTP or HTTPS depending on how your server is configured.

**Token Endpoint** (`"TokenEndpoint": ""`)  

Enter `https://<your-gitlab-url>/oauth/authorize` (example: `https://example.com:3000/oauth/token`). Use HTTP or HTTPS depending on how your server is configured.

**User API Endpoint** (`"UserApiEndpoint": ""`)  

Enter `https://<your-gitlab-url>/oauth/authorize` (example: `https://example.com:3000/api/v3/user`). Use HTTP or HTTPS depending on how your server is configured.

### Legals and Support Settings

**Terms of Service link** (`"TermsOfServiceLink": "/static/help/terms.html"`)  

Configurable link to Terms of Service your organization may provide to end users. By default, links to an editable file hosted in the `static/help/terms.html` found in the directory where the Mattermost server installed. Default file may be updated to state the terms under which your organization is providing its server to end users, in addition to the "Mattermost Conditions of Use" notice to end users that must also be shown to users from the "Terms of Service" link. 

**Privacy Policy link** (`"PrivacyPolicyLink": "/static/help/privacy.html"`)  

Configurable link to Privacy Policy your organization may provide to end users. By default, links to an editable file hosted in the `static/help/privacy.html` found in the directory where the Mattermost server installed. 

**About link** (`"AboutLink": "/static/help/about.html"`)  

Configurable link to an About page describing your organization may provide to end users. By default, links to an editable file hosted in the `static/help/about.html` found in the directory where the Mattermost server installed. 

**Help link** (`"HelpLink": "/static/help/help.html"`)  

Configurable link to an About page describing your organization may provide to end users. By default, points to Mattermost default help documentation. Can be links to an editable file hosted in the `static/help/help.html` found in the directory where the Mattermost server installed. 

**Report a Problem link** (`"ReportAProblemLink": "/static/help/report_problem.html"`)  

Set the link for the support website.

**Support email** (`"SupportEmail":"feedback@mattermost.com"`)  

Set an email for feedback or support requests.

### LDAP Settings (Enterprise)  
Settings used to enable and configure LDAP authentication with Mattermost. Available in the Enterprise version of Mattermost.

**Enable Login With LDAP** (`"Enable": false`)  

`true`: Mattermost allows login using LDAP.

**LDAP Server** (`"LdapServer": ""`)  

The domain or IP address of the LDAP server.

**LDAP Port** (`"LdapPort": 389`)    

The port Mattermost will use to connect to the LDAP server. Default is 389.

**Base DN** (`"BaseDN": ""`)    

The Base DN is the Distinguished Name of the location where Mattermost should start its search for users in the LDAP tree.

**Bind Username** (`"BindUsername": ""`)  

The username used to perform the LDAP search. This should typically be an account created specifically for use with Mattermost. It should be a read only account with access limited to the portion of the LDAP tree specified in the BaseDN field.

**Bind Password** (`"BindPassword": ""`)  

Password of the user given in “Bind Username”.

**First Name Attribute** (`"FirstNameAttribute": ""`)  

The attribute in the LDAP server that will be used to populate the first name of users in Mattermost.

**Last Name Attribute** (`"LastNameAttribute": ""`)  

The attribute in the LDAP server that will be used to populate the last name of users in Mattermost.

**Email Attribute** (`"EmailAttribute": ""`)  

The attribute in the LDAP server that will be used to populate the email addresses of users in Mattermost.

**Username Attribute** (`"UsernameAttribute": ""`)  

The attribute in the LDAP server that will be used to populate the username field in Mattermost. This may be the same as the ID Attribute.

**ID Attribute** (`"IdAttribute": ""`)  

The attribute in the LDAP server that will be used as a unique identifier in Mattermost.

This is the attribute that will be used to create Mattermost accounts. It should be an LDAP attribute with a value that does not change, such as username or uid. If a user’s Id Attribute changes, it will create a new Mattermost account unassociated with their old one. 

This is also the value used to log in to Mattermost in the “LDAP Username” field on the sign in page. Normally this attribute is the same as the “Username Attribute” field above. If your team typically uses domain\username to sign in to other services with LDAP, you may choose to put domain\username in this field to maintain consistency between sites.

**Query Timeout (seconds)** (`"QueryTimeout": 60`)  

The timeout value for queries to the LDAP server. Increase this value if you are getting timeout errors caused by a slow LDAP server.

## Config.json settings not in System Console

System Console allows an IT Admin to update settings defined in `config.json`. However there are a number of settings in `config.json` unavailable in the System Console and require update from the file itself. We describe them here: 

### Service Settings

**Enable OAuth Service Provider** (`"EnableOAuthServiceProvider": false`)  

`true`: Allow Mattermost to function as an OAuth provider, allowing 3rd party apps access to your user store for authentication.

**WebSocket Secure Port** (`"WebsocketSecurePort" : 443`)  

When present in `config.json`, this setting defines the port on which the secured WebSocket will listen using the `wss` protocol. Otherwise it defaults to `443`. When the client attempts to make a WebSocket connection it first checks to see if the page is loaded with HTTPS. If so, it will use the secure WebSocket connection. If not, it will use the unsecure WebSocket connection. IT IS HIGHLY RECOMMENDED PRODUCTION DEPLOYMENTS ONLY OPERATE UNDER HTTPS AND WSS. 

**WebSocket Port** (`WebsocketPort": 80`)  

When present in `config.json`, this setting defines the port on which the unsecured WebSocket will listen using the `ws` protocol. Otherwise it defaults to `80`. When the client attempts to make a WebSocket connection it first checks to see if the page is loaded with HTTPS. If so, it will use the secure WebSocket connection. If not, it will use the unsecure WebSocket connection. IT IS HIGHLY RECOMMENDED PRODUCTION DEPLOYMENTS ONLY OPERATE UNDER HTTPS AND WSS. 

### File Settings

**Initial Font** (`"InitialFont": "luximbi.ttf"`)  

Font used in auto-generated profile pics with colored backgrounds.

**Amazon S3 Endpoint** (`"AmazonS3Endpoint": ""`)  

Set an endpoint URL for an Amazon S3 instance.

**Amazon S3 Bucket Endpoint** (`"AmazonS3BucketEndpoint": ""`)  

Set an endpoint URL for Amazon S3 buckets.

**Amazon S3 Location Constraint** (`"AmazonS3LocationConstraint": false`)  

Set whether the S3 region is location constrained.

**Amazon S3 Lowercase Bucket** (`"AmazonS3LowercaseBucket": false`)    

Set whether bucket names are fully lowercase or not.

### GitLab Settings

**Scope** (`"Scope": ""`)  

Standard setting for OAuth to determine the scope of information shared with OAuth client. Not currently supported by GitLab OAuth.
