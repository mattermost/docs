.. _telemetry:

Telemetry
=========

As described in the privacy policy in each Mattermost server, telemetry data optionally shared from your Mattermost servers is used to identify security and reliability issues, to analyze and fix software problems, to help improve the quality of Mattermost software and related services, and to make design decisions for future releases.

Telemetry data is encrypted in transit, does not include personally identifiable information or message contents, and details of how the information is used and processed is available in our `Privacy Policy <https://about.mattermost.com/default-privacy-policy/>`__.

We use the data for the following purposes:

  - to identify security and reliability issues
  - to analyze and fix software problems
  - to help improve the quality of Mattermost software and related services
  - to make design decisions for future releases

Security Update Check Feature
-----------------------------

New threats to system security constantly arise. To alert you of relevant, high priority security updates, Mattermost servers are configured to share diagnostic information with Mattermost Inc. so that we can provide appropriate alerts.

The following data is collected once every 24 hours: Mattermost server build number and version, type of build (Enterprise or Team), server operating system, the server diagnostic ID (same as the ID accessing the push notification proxy, and is used to prevent double-counting of telemetry data), database type, number of teams, number of users, number of active users, whether or not the unit tests have been run, date and time of the last check for security updates, and the location of the Amazon Cloudfront server used for telemetry data.

To opt out, disable the feature in **System Console > Notifications > Email > Enable Security Alerts** in prior versions or **System Console > Environment > SMTP** in versions after 5.12. When the feature is disabled, you will not receive any security alerts.

Error and Diagnostics Reporting Feature
---------------------------------------

Error and diagnostic data is collected for the following purposes: to add improvements to Mattermost software that are specific to your usage and deployment patterns, including identifying security and reliability issues;  to analyze and fix software problems; to help improve the quality of Mattermost software and related services; and to make design decisions for future releases.

The following data is sent once every 24 hours:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deployment Configuration Information
  Basic information including Mattermost server version, database and operating system type and version, and count of System Administrator accounts

Server Configuration Settings
  Non-personally identifiable data from configuration settings file (``config.json``) in the form of type ("enumerated integer" or "enumerated boolean") values, true/false ("boolean"), and count ("integer"). Specifically these include:

  **Type values (enumerated integer and enumerated boolean)**

  **ServiceSettings**: enum WebserverMode, bool EnableSecurityFixAlert, bool EnableInsecureOutgoingConnections, bool EnableIncomingWebhooks, bool EnableOutgoingWebhooks, bool EnableCommands, bool EnableOnlyAdminIntegrations, bool EnablePostUsernameOverride, bool EnablePostIconOverride, bool EnableCustomEmoji, enum RestrictCustomEmojiCreation, bool EnableTesting, bool EnableDeveloper, bool EnableMultifactorAuthentication, bool EnableOAuthServiceProvider, enum ConnectionSecurity, bool UseLetsEncrypt, bool Forward80To443, enum ConnectionSecurity, bool TLSStrictTransport, bool EnforceMultifactorAuthentication, enum RestrictPostDelete, bool AllowEditPost, bool EnableUserTypingMessages, bool EnablePostSearch, bool EnableUserStatuses, bool EnableChannelViewMessages, bool EnableEmojiPicker, bool EnableGifPicker, bool ExperimentalEnableAuthenticationTransfer, enum TeammateNameDisplay, bool EnableUserAccessTokens, enum MaximumLoginAttempts, enum SessionLengthWebInDays, enum SessionLengthMobileInDays, int SessionCacheInMinutes, enum SessionIdleTimeoutInMinutes, enum PostEditTimeLimit, enum TimeBetweenUserTypingUpdatesMilliseconds, enum ClusterLogTimeoutMilliseconds, bool CloseUnusedDirectMessages, bool EnablePreviewFeatures, bool EnableTutorial, bool ExperimentalEnableDefaultChannelLeaveJoinMessages, bool ExperimentalGroupUnreadChannels, bool AllowCookiesForSubdomains, bool EnableAPITeamDeletion, bool ExperimentalEnableHardenedMode, bool DisableLegacyMFA, bool CorsAllowCredentials, bool CorsDebug, bool DisableBotsWhenOwnerIsDeactivated, bool EnableBotAccountCreation; **TeamSettings**: bool EnableUserCreation, bool EnableTeamCreation, bool RestrictTeamNames, enum RestrictTeamInvite, enum RestrictPublicChannelManagement, enum RestrictPrivateChannelManagement, enum RestrictPublicChannelCreation, enum RestrictPrivateChannelCreation, enum RestrictPublicChannelDeletion, enum RestrictPrivateChannelDeletion, enum RestrictPrivateChannelManageMembers, bool EnableOpenServer, bool EnableUserDeactivation, bool EnableCustomBrand, bool RestrictDirectMessage, enum MaxNotificationsPerChannel, bool EnableConfirmNotificationsToChannel; enum MaxUsersPerTeam, enum MaxChannelsPerTeam, bool ExperimentalTownSquareIsReadOnly, bool ExperimentalHideTownSquareinLHS, bool EnableXToLeaveChannelsFromLHS, bool ExperimentalEnableAutomaticReplies, bool ExperimentalViewArchivedChannels, bool LockTeammateNameDisplay; **ClientRequirementSettings**: enum AndroidLatestVersion, enum AndroidMinVersion, enum DesktopLatestVersion, enum DesktopMinVersion, enum IosLatestVersion, enum IosMinVersion; **DisplaySettings**: bool ExperimentalTimezone; **GuestAccountsSettings**: bool Enable, bool AllowEmailAccounts, bool EnforceMultifactorAuthentication; **SqlSettings**: enum DriverName, bool Trace, enum MaxIdleConns, bool ConnMaxLifetimeMilliseconds; enum MaxOpenC onns, enum QueryTimeout, **LogSettings**: bool EnableConsole, enum ConsoleLevel, bool ConsoleJson, bool EnableFile, enum FileLevel, bool FileJson, bool EnableWebhookDebugging; **NotificationLogSettings**: bool EnableConsole, bool ConsoleLevel, bool ConsoleJson, bool EnableFile, bool FileLevel, bool FileJson **PasswordSettings**: bool Lowercase, bool Number, bool Uppercase, bool Symbol, enum MinimumLength; **FileSettings**: bool EnablePublicLink, enum DriverName, bool AmazonS3SSL, bool AmazonS3SignV2, bool AmazonS3SSE, bool AmazonS3Trace, bool EnableFileAttachments, bool EnableMobileUpload, bool EnableMobileDownload; **EmailSettings**: bool EnableSignUpWithEmail, bool EnableSignInWithEmail, bool EnableSignInWithUsername, bool RequireEmailVerification, bool SendEmailNotifications, bool UseChannelInEmailNotifications, bool EmailNotificationContentsType, bool EnableSMTPAuth, enum ConnectionSecurity, bool SendPushNotifications, enum PushNotificationContents, bool EnableEmailBatching, bool SkipServerCertificateVerification, enum EmailBatchingBufferSize, enum EmailBatchingInterval, bool EnablePreviewModeBanner; **RateLimitSettings**: bool EnableRateLimiter, bool VaryByRemoteAddr,  bool VaryByUser, enum PerSec, enum MaxBurst, enum MemoryStoreSize; **PrivacySettings**: bool ShowEmailAddress, bool ShowFullName; **ThemeSettings**: bool EnableThemeSelection, bool AllowCustomThemes; **GitLabSettings**: bool Enable; **GoogleSettings**: bool Enable; **Office365Settings**: bool Enable; **SupportSettings**: bool CustomTermsOfServiceEnabled; enum CustomTermsOfServiceReAcceptancePeriod; **LdapSettings**: bool Enable, bool EnableSync, enum ConnectionSecurity, bool SkipCertificateVerification, enum SyncIntervalMinutes, enum QueryTimeout, enum MaxPageSize, bool EnableAdminFilter; **ComplianceSettings**: bool Enable, bool EnableDaily; **LocalizationSettings**: enum DefaultServerLocale, enum DefaultClientLocale, enum AvailableLocales; **SamlSettings**: bool Enable, bool EnableSyncWithLdap, bool EnableSyncWithLdapIncludeAuth, bool Verify, bool Encrypt, bool SignRequest, bool EnableAdminFilter; **ClusterSettings**: bool Enable, bool UseIpAddress, bool UseExperimentalGossip, bool ReadOnlyConfig; **MetricsSettings**: bool Enable, enum BlockProfileRate; **WebrtcSettings** (only in v5.5 and earlier): bool Enable; **ExperimentalSettings** bool ClientSideCertEnable, bool EnablePostMetadata, bool EnableClickToReply, bool RestrictSystemAdmin, bool UseNewSAMLLibrary; **AnnouncementSettings**: bool EnableBanner, bool AllowBannerDismissal; **ElasticsearchSettings**: bool EnableIndexing, bool EnableSearching, bool Sniff, enum PostIndexReplicas, enum PostIndexShards, enum LiveIndexingBatchSize, enum BulkIndexingTimeWindowSeconds, enum RequestTimeoutSeconds, bool SkipTLSVerification, bool Trace; **PluginSettings**: bool Enable, bool EnableUploads, bool EnableHealthCheck, bool EnableMarketplace, bool EnableRemoteMarketplace, bool AutomaticPrepackagedPlugins, bool RequirePluginSignature; **DataRetentionSettings**: bool EnableMessageDeletion, bool MessageRetentionDays, bool AllowInsecureDownloadUrl, bool EnableFileDeletion, bool FileRetentionDays, enum DeletionJobStartTime; **MessageExportSettings**: bool EnableExport, enum ExportFormat, enum DailyRunTime, enum ExportFromTimestamp, enum BatchSize, enum GlobalRelaySettings.CustomerType

  **Counts (integer)**

    **SqlSettings**: int DataSourceReplicas, int DataSourceSearchReplicas; **ThemeSettings**: int AllowedThemes; **PluginSettings**: int SignaturePublicKeyFiles

  **True/false (boolean)** value whether setting remains default (true) or non-default (false). **NOTE: No input data is used**:

     **ServiceSettings**: bool SiteURL, bool WebsocketURL, bool TLSCertFile, bool TLSKeyFile, bool ReadTimeout, bool WriteTimeout, bool GoogleDeveloperKey, bool AllowCorsFrom, bool CorsExposedHeaders, bool AllowedUntrustedInternalConnections, bool GfycatApiKey, bool GfycatApiSecret; **TeamSettings**: bool SiteName, bool CustomBrandText, bool CustomDescriptionText, bool UserStatusAwayTimeout, bool ExperimentalPrimaryTeam; **DisplaySettings**: bool CustomUrlSchemes; **GuestAccountSettings**: bool RestrictCreationToDomains; **LogSettings**: bool FileLocation; **NotificationLogSettings**: bool FileLocation; **EmailSettings**: bool FeedbackName, bool FeedbackEmail, bool FeedbackOrganization, bool LoginButtonColor, bool LoginButtonBorderColor, bool LoginButtonTextColor, bool ImageProxyType, bool ImageProxyURL, bool ImageProxyOptions; **RateLimitSettings**: bool VaryByHeader; **SupportSettings**: bool TermsOfServiceLink, bool PrivacyPolicyLink, bool AboutLink, bool HelpLink, bool ReportAProblemLink, bool SupportEmail; **ThemeSettings**: bool DefaultTheme; **TimeZoneSettings**: bool SupportedTimezonesPath; **LdapSettings**: bool FirstNameAttribute, bool LastNameAttribute, bool EmailAttribute, bool UserNameAttribute, bool NicknameAttribute, bool IdAttribute, bool PositionAttribute, bool LoginFieldName, bool LoginButtonColor, bool LoginButtonBorderColor, bool LoginButtonTextColor, bool GroupFilter, bool GroupDisplayNameAttribute, bool GroupIdAttribute, bool GuestFilter, bool AdminFilter; **SamlSettings**: bool SignatureAlgorithm, bool CanonicalAlgorithm, bool ScopingIDPProviderId, bool ScopingIDPName, bool IdAttribute, bool GuestAttribute, bool FirstNameAttribute, bool LastNameAttribute, bool EmailAttribute, bool UserNameAttribute, bool NicknameAttribute, bool LocaleAttribute, bool PositionAttribute, bool LoginIdAttribute, bool LoginButtonText, bool LoginButtonColor, bool LoginButtonBorderColor, bool LoginButtonTextColor, bool AdminFilter; **NativeAppSettings**: bool AppDownloadLink, bool  AndroidAppDownloadLink, bool IosAppDownloadLink; **WebrtcSettings** (only in v5.5 and earlier): bool StunURI, bool TurnURI; **ClusterSettings**: bool NetworkInterface, bool BindAddress, bool AdvertiseAddress; **MetricsSettings**: bool BlockProfileRate; **AnalyticsSettings**: bool MaxUsersForStatistics; **ExperimentalSettings** bool ClientSideCertCheck; **AnnouncementSettings**: bool BannerColor, bool BannerTextColor; **ElasticsearchSettings**: bool ConnectionUrl, bool Username, bool Password, bool IndexPrefix; **PluginSettings**: bool MarketplaceUrl, bool SignaturePublicKeyFiles; **MessageExportSettings**: bool GlobalRelaySettings.SmtpUsername, bool GlobalRelaySettings.SmtpPassword, bool GlobalRelaySettings.EmailAddress

Commercial License Information (Enterprise Edition Only)
  Information about commercial license key purchased or trial license key used for Enterprise Edition servers: Company ID, license ID, license issue date, license start date, license expiry date, number of licensed users, license short name (E10 vs E20), list of unlocked Enterprise features.

Plugin Configuration Information
  Basic information including number of active and inactive plugins, which are using webapp or backend portions, and which pre-packaged plugins are enabled along with their versions.

Aggregated Usage Statistics
  Non-personally identifiable summations of basic usage statistics: Number of enabled and disabled accounts, number of user logins in the last 24 hours and the last 30 days, number of users active in the last day/month, whether APIv3 endpoints were used in the last 24 hours, number of posts, channels, teams and bots.

The following information is sent when the specified event occurs:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Non-personally Identifiable Error Information, distinguished by end users and System Admins
  Boolean when the following events occur:
  
  - *Sign-in Error*: Email login error, AD/LDAP login error, SAML login error
  
  Boolean when the following events occur, including the error message, recently dispatched Redux actions, and non-identifiable information of the device, operating system and the app:

  - *Mobile App Errors*: App crashes caused by type errors, exceptions and failed logins

Non-personally Identifiable Diagnostic Information, distinguished by end users and System Admins
  Boolean when the following events occur:

  - *Team and Account Setup Diagnostics:* Account creation via email, invite or UI, account creation page view, account creation completion; tutorial step and tip completion or opt out, team creation page view, team name and URL entry, team creation completion
  - *Sign-in Diagnostics:* Login succeeded or failed for email, LDAP or SAML/SSO; logout succeeded; switched authentication method from email to LDAP or SAML/SSO or vice versa; reset password; updated password
  - *Navigation Discovery Diagnostics:* Joined a channel from the "More" list, through an invite or by clicking a public link; created a channel, direct, or group direct message conversation; renamed, joined, left or deleted an existing channel; updated header or purpose; added or removed members; updated channel notification preferences; loaded more messages in a channel; switched a channel or a team; opened the "More" modal for channels or direct message conversations; updated team name; invited members; updated account settings
  - *Core Feature Discovery Diagnostics:* Created, edited or deleted a message; posted a message containing a hashtag, link, mention or file attachment; searched for a term; searched for flagged posts or recent mentions
  - *Advanced Feature Discovery Diagnostics:* Reacted to a message; favorited or un-favorited a channel; flagged or un-flagged a message; pinned or un-pinned a message; replied to a message; expanded the right-hand sidebar; started or finished a WebRTC video call (only in v5.5 and earlier); created or deleted a personal access token; added or removed post:all or post:channels permission
  - *Integration Discovery Diagnostics:* Created or triggered a webhook or slash command; created, authroized or deleted an OAuth 2.0 app; created, posted or deleted a custom emoji
  - *Plugin Discovery Diagnostics:* Number of installed plugins containing either server or webapp portions, or both; number of those plugins being activated
  - *Plugin Marketplace Diagnostics:* Plugin id, current version, and target version for all install and update events. Only sent when the default marketplace is configured.
  - *Commercial License Diagnostics (Enterprise Edition Only):* Uploaded an Enterprise license key to the server
  - *Mobile Performance Diagnostics:* Load times for starting the app, switching channels, and switching teams 
  - *Permissions Discovery Diagnostics (Enterprise Edition Only):* Provides all the permissions configured for each role for the System Scheme and each Team Override Scheme created in the system.  Scheme ID; Team Admin Permissions; Team User Permissions; Channel Admin Permissions; Channel User Permissions; Number of teams the scheme is associated with
  - *Group Discovery Diagnostics (Enterprise Edition Only):* Provides information related to AD/LDAP groups, including number of groups synced to Mattermost, teams and channels associated to groups, teams and channels synced with groups, and number of group members

Error and diagnostic reporting is sent by the client to the endpoint `api.segment.io`. To opt out, disable the feature in **System Console > General > Logging > Enable Error and Diagnostics Reporting** in prior versions or **System Console > Environment > Logging** in versions after 5.12.

Android Mobile App Performance Monitoring
-----------------------------------------

To improve Android app performance, we are collecting trace events and device information, collectively known as metrics, to identify slow performing key areas. Those metrics will be sent only from users using Android app beta build starting in version v1.20, who are logged in to servers that allow sending `diagnostic information <https://docs.mattermost.com/administration/config-settings.html#enable-diagnostics-and-error-reporting>`__.

Trace events
  Includes duration on how long the action took place like startup, team/channel switch, posts loading/update and channel drawer open/close. The naming convention is interpreted as ``[start observation]:[end observation]``, e.g. ``start:overall`` as from app start until fully rendered or ``post_list:thread`` as on press of post at post list until thread is opened.
  Complete list of trace events are the following:

  - start:overall
  - start:process_packages
  - start:content_appeared
  - start:select_server_screen
  - start:channel_screen
  - team:switch
  - channel:loading
  - channel:switch_loaded
  - channel:switch_initial
  - channel:close_drawer
  - channel:open_drawer
  - posts:loading
  - post_list:thread
  - post_list:permalink

Device information
  The information being collected is non-personally identifiable. Except for system_version, device information is based from `react-native-device-info <https://github.com/mattermost/react-native-device-info#react-native-device-info>`__ library.  Refer to the linked documentation to learn more.
  Complete list of device information are the following:

  - api_level
  - build_number
  - bundle_id
  - brand
  - country
  - device_id
  - device_locale
  - device_type
  - device_unique_id
  - height
  - is_emulator
  - is_tablet
  - manufacturer
  - max_memory
  - model
  - server_version
  - system_name
  - system_version
  - timezone
  - version
  - width
