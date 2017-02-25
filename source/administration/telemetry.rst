.. _telemetry:

Telemetry
=========

Mattermost servers are configured to share anonymous usage and deployment information with Mattermost, Inc. Participation is optional and you can opt out at any time. The data is collected, encrypted, and transmitted in accordance with our `privacy policy <https://about.mattermost.com/default-privacy-policy/>`_. No personally identifiable information is transmitted, and the contents of messages are not transmitted.

We use the data for the following purposes:

  - to identify security and reliability issues
  - to analyze and fix software problems
  - to help improve the quality of Mattermost software and related services
  - to make design decisions for future releases

Security Fix Alert Feature
--------------------------

New threats to system security constantly arise. To alert you of relevant, high priority security updates, Mattermost servers are configured to share anonymous deployment information with Mattermost Inc. so that we can provide appropriate alerts.

To opt out, disable the feature in **System Console > Notifications > Email > Enable Security Alerts**. When the feature is disabled, you will not receive any security alerts.

The following data is collected once every 24 hours:

 - Mattermost server version
 - server operating system and database type
 - number of teams
 - number of user logins in the last 24 hours
 - the ID of the Amazon Cloudfront server used for telemetry data

Error and Diagnostics Reporting Feature
---------------------------------------

Error and diagnostic data is collected for the following purposes:

  - to add improvements to Mattermost software that are specific to your usage and deployment patterns, including identifying security and reliability issues
  - to analyze and fix software problems
  - to help improve the quality of Mattermost software and related services
  - to make design decisions for future releases

To opt out, disable the feature in **System Console > General > Logging > Enable Error and Diagnostics Reporting**.

The following data is collected after an error event:

Deployment Configuration Information
  Basic information including Mattermost server version, database and operating system type and version, and count of System Administrator accounts

Server Configuration Settings
  Non-personally identifiable data from configuration settings file (``config.json``) in the form of type ("enumerated integer" or "enumerated boolean") values, true/false ("boolean"), and count ("integer"). Specifically these include:

  **Type values (enumerated integer and enumerated boolean)**

    **ServiceSettings**: enum WebserverMode, bool EnableSecurityFixAlert, bool EnableInsecureOutgoingConnections, bool EnableIncomingWebhooks, bool EnableOutgoingWebhooks, bool EnableCommands, bool EnableOnlyAdminIntegrations, bool EnablePostUsernameOverride, bool EnablePostIconOverride, bool EnableCustomEmoji, enum RestrictCustomEmojiCreation, bool EnableTesting, bool EnableDeveloper, bool EnableMultifactorAuthentication, bool EnableOAuthServiceProvider, enum ConnectionSecurity, bool UseLetsEncrypt, bool Forward80To443, enum ConnectionSecurity, bool EnforceMultifactorAuthentication, enum RestrictPostDelete, bool AllowEditPost, bool EnableUserTypingMessages; **TeamSettings**: bool EnableUserCreation, bool EnableTeamCreation, bool RestrictTeamNames, enum RestrictTeamInvite, enum RestrictPublicChannelManagement, enum RestrictPrivateChannelManagement, enum RestrictPublicChannelCreation, enum RestrictPrivateChannelCreation, enum RestrictPublicChannelDeletion, enum RestrictPrivateChannelDeletion, bool EnableOpenServer, bool EnableCustomBrand, bool RestrictDirectMessag; **SqlSettings**: enum DriverName, bool Trace; **LogSettings**: bool EnableConsole, enum ConsoleLevel, bool EnableFile, enum FileLevel, bool EnableWebhookDebugging; **PasswordSettings**: bool Lowercase, bool Number, bool Uppercase, bool Symbol; **FileSettings**: bool EnablePublicLink, enum DriverName, bool AmazonS3SSL; **EmailSettings**: bool EnableSignUpWithEmail, bool EnableSignInWithEmail, bool EnableSignInWithUsername, bool RequireEmailVerification, bool SendEmailNotifications, enum ConnectionSecurity, bool SendPushNotifications, enum PushNotificationContents, bool EnableEmailBatching; **RateLimitSettings**: bool EnableRateLimiter, bool VaryByRemoteAddr; **PrivacySettings**: bool ShowEmailAddress, bool ShowFullName; **GitLabSettings**: bool Enable; **GoogleSettings**: bool Enable; **Office365Settings**: bool Enable; **LdapSettings**: bool Enable, enum ConnectionSecurity, bool SkipCertificateVerification; **ComplianceSettings**: bool Enable, bool EnableDaily; **LocalizationSettings**: enum DefaultServerLocale, enum DefaultClientLocale, enum AvailableLocales; **SamlSettings**: bool Enable, bool Verify, bool Encrypt; **ClusterSettings**: bool Enable; **MetricsSettings**: bool Enable; **WebrtcSettings**: bool Enable

  **Counts (integer)**

    **ServiceSettings**: int MaximumLoginAttempts, int SessionLengthWebInDays, int SessionLengthMobileInDays, int SessionLengthSSOInDays, int SessionCacheInMinutes, int PostEditTimeLimit, int TimeBetweenUserTypingUpdatesMilliseconds, int ClusterLogTimeoutMilliseconds; **TeamSettings**: int MaxNotificationsPerChannel, int MaxUsersPerTeam, int MaxChannelsPerTeam; **SqlSettings**: int DriverName, int MaxIdleConns, int MaxOpenConns; **PasswordSettings**: int MinimumLength; **FileSettings**: int ThumbnailWidth, int ThumbnailHeight, int PreviewWidth, int PreviewHeight, int ProfileWidth, int ProfileHeight, int MaxFileSize; **EmailSettings**: int EmailBatchingBufferSize, int EmailBatchingInterval; **RateLimitSettings**: int PerSec, int MaxBurst, int MemoryStoreSize; **LdapSettings**: int SyncIntervalMinutes, int QueryTimeout, int MaxPageSize; **SqlSettings**: int DataSourceReplicas; **MetricsSettings**: int BlockProfileRate

  **True/false (boolean)** value whether setting remains default (true) or non-default (false). **NOTE: No input data is used**:

     **ServiceSettings**: bool SiteURL, bool TLSCertFile, bool TLSKeyFile, bool ReadTimeout, bool WriteTimeout, bool GoogleDeveloperKey, bool AllowCorsFrom; **TeamSettings**: bool SiteName, bool CustomBrandText, bool CustomDescriptionText, bool UserStatusAwayTimeout; **LogSettings**: bool FileFormat, bool FileLocation; **EmailSettings**: bool FeedbackName, bool FeedbackEmail, bool FeedbackOrganization; **RateLimitSettings**: bool VaryByHeader; **SupportSettings**: bool TermsOfServiceLink, bool PrivacyPolicyLink, bool AboutLink, bool HelpLink, bool ReportAProblemLink, bool SupportEmail; **LdapSettings**: bool FirstNameAttribute, bool LastNameAttribute, bool EmailAttribute, bool UserNameAttribute, bool NicknameAttribute, bool IdAttribute, bool PositionAttribute, bool LoginFieldName; **SamlSettings**: bool FirstNameAttribute, bool LastNameAttribute, bool EmailAttribute, bool UserNameAttribute, bool NicknameAttribute, bool LocaleAttribute, bool PositionAttribute, bool LoginButtonText; **NativeAppSettings**: bool AppDownloadLink, bool  AndroidAppDownloadLink, bool IosAppDownloadLink; **WebrtcSettings**: bool StunURI, bool TurnURI; **MetricsSettings**: bool BlockProfileRate; **AnalyticsSettings**: bool MaxUsersForStatistics

Commercial License Information (Enterprise Edition Only)
  Information about commercial license key purchased or trial license key used for Enterprise Edition servers: Company name, full name, license issue date, license start date, license expiry date, number of licensed users, list of unlocked Enterprise features

Aggregated Usage Statistics
  Non-personally identifiable summations of basic usage statistics: Number of enabled and disabled accounts, number of user logins in the last 24 hours, number of posts, channels and teams

Non-personally Identifiable Error Information
  Boolean when the following events occur: Email login error, AD/LDAP login error, SAML login error

Non-personally Identifiable Diagnostic Information
  Boolean when the following events occur:

  - *Team and Account Setup Diagnostics:* Account creation via email, invite or UI, account creation page view, account creation completion; tutorial step & tip completion or opt out, team creation page view, team name and URL entry, team creation completion
  - *Sign-in Diagnostics:* Login succeeded or failed for email, LDAP or SAML/SSO; logout succeeded; switched authentication method from email to LDAP or SAML/SSO or vice versa; reset password; updated password
  - *Navigation Discovery Diagnostics:* Joined a channel from the "More" list, through an invite or by clicking a public link; created a channel or direct message conversation; renamed, joined, left or deleted an existing channel; updated header or purpose; added or removed members; viewed a channel in permalink view; loaded more messages in a channel; switched a channel or a team; opened the "More" modal for channels or direct message conversations; updated team name; invited members; updated account settings
  - *Core Feature Discovery Diagnostics:* Created, edited or deleted a message; posted a message containing a hashtag, link, mention or file attachment; searched for a term; searched for flagged posts or recent mentions
  - *Advanced Feature Discovery Diagnostics:* Reacted to a message; favorited or un-favorited a channel; flagged or un-flagged a message; replied to a message; expanded the right-hand sidebar; started or finished a WebRTC video call
  - *Integration Discovery Diagnostics:* Created or triggered a webhook or slash command; created, authroized or deleted an OAuth 2.0 app; created, posted or deleted a custom emoji
  - *Commercial License Diagnostics (Enterprise Edition Only):* Uploaded an Enterprise license key to the server
