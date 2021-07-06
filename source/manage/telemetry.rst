:orphan:

.. _telemetry:

Telemetry
=========

As described in the privacy policy in each Mattermost server, telemetry data optionally shared from your Mattermost servers is used to identify security and reliability issues, to analyze and fix software problems, to help improve the quality of Mattermost software and related services, and to make design decisions for future releases.

Telemetry data is encrypted in transit, does not include personally identifiable information or message contents, and details of how the information is used and processed is available in our `Privacy Policy <https://about.mattermost.com/default-privacy-policy/>`__.

We use the data for the following purposes:

- To identify security and reliability issues.
- To analyze and fix software problems.
- To help improve the quality of Mattermost software and related services.
- To make design decisions for future releases.

Security Update Check Feature
-----------------------------

New threats to system security constantly arise. To alert you of relevant, high priority security updates, Mattermost servers are configured to share diagnostic information with Mattermost Inc. so that we can provide appropriate alerts.

The following data is collected once every 24 hours:

- Mattermost server build number and version
- Type of build (Enterprise Edition or Team Edition)
- Server operating system
- The server diagnostic ID (same as the ID accessing the push notification proxy, and is used to prevent double-counting of telemetry data)
- Database type
- Database version
- Number of teams
- Number of users 
- Number of active users
- Whether or not the unit tests have been run
- Date and time of the last check for security updates
- The location of the Amazon Cloudfront server used for telemetry data

To opt out, disable the feature in **System Console > Environment > SMTP**. When the feature is disabled, you will not receive any security alerts.

Error and Diagnostics Reporting Feature
---------------------------------------

Mattermost error and diagnostic data is collected for the following purposes:
- To add improvements that are specific to your usage and deployment patterns, including identifying security and reliability issues.
- To analyze and fix software problems.
- To help improve the quality of Mattermost software and related services.
- To make design decisions for future releases.

.. note:: 

  Error and diagnostic reporting is sent by the client to the endpoint ``api.segment.io``. From Mattermost v5.23 the segment endpoint is being deprecated in favor of ``https://pdat.matterlytics.com``, a custom Rudder domain. To opt out, you can disable the feature in **System Console > Environment > Logging > Enable Diagnostics and Error Reporting**. Starting in Mattermost v5.26, when this feature is enabled, any 500 errors will be automatically sent to the Mattermost-hosted `Sentry <https://sentry.io/welcome/>`_ endpoint.

Deployment and Server Configuration Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reporting Frequency
- When starting the server for the first time: Every 10 minutes for the first hour, then every hour for the first 12 hours.
- At the 24 hour mark and every 24 hours thereafter.

Deployment Configuration Information
  Basic information including Mattermost server version, database and operating system type and version, and count of System Administrator accounts.

Deployment Type
- Manual install (includes ``wget`` installs)
- Docker
- Mattermost Omnibus
- Kubernetes operator
- GitLab Omnibus

Server Configuration Settings
  Non-personally identifiable data from configuration settings file (``config.json``) in the form of ``type`` ("enumerated integer" or "enumerated boolean") values, ``true/false`` ("boolean"), and ``count`` ("integer"). Specifically these include:

  **Type values (enumerated integer and enumerated boolean)**

  **ServiceSettings**: enum WebserverMode, bool EnableSecurityFixAlert, bool EnableInsecureOutgoingConnections, bool EnableIncomingWebhooks, bool EnableOutgoingWebhooks, bool EnableCommands, bool EnableOnlyAdminIntegrations, bool EnablePostUsernameOverride, bool EnablePostIconOverride, bool EnableCustomEmoji, enum RestrictCustomEmojiCreation, bool EnableTesting, bool EnableDeveloper, bool EnableMultifactorAuthentication, bool EnableOAuthServiceProvider, enum ConnectionSecurity, bool UseLetsEncrypt, bool Forward80To443, enum ConnectionSecurity, bool TLSStrictTransport, bool EnforceMultifactorAuthentication, enum RestrictPostDelete, bool AllowEditPost, bool EnableUserTypingMessages, bool EnablePostSearch, bool EnableUserStatuses, bool EnableChannelViewMessages, bool EnableEmojiPicker, bool EnableGifPicker, bool xEnableAuthenticationTransfer, enum TeammateNameDisplay, bool EnableUserAccessTokens, enum MaximumLoginAttempts, bool ExtendSessionLengthWithActivity, enum SessionLengthWebInDays, enum SessionLengthMobileInDays, int SessionCacheInMinutes, enum SessionIdleTimeoutInMinutes, enum PostEditTimeLimit, enum TimeBetweenUserTypingUpdatesMilliseconds, enum ClusterLogTimeoutMilliseconds, bool CloseUnusedDirectMessages, bool EnablePreviewFeatures, bool EnableTutorial, bool ExperimentalEnableDefaultChannelLeaveJoinMessages, bool ExperimentalGroupUnreadChannels, bool AllowCookiesForSubdomains, bool EnableAPITeamDeletion, bool EnableAPIUserDeletion, bool EnableAPIChannelDeletion, bool ExperimentalEnableHardenedMode, bool DisableLegacyMFA, bool ExperimentalStrictCSRFEnforcement, bool EnableEmailInvitations, bool ExperimentalChannelOrganization, bool ExperimentalChannelSidebarOrganization, bool EnableLegacySidebar, bool CorsAllowCredentials, bool CorsDebug, bool DisableBotsWhenOwnerIsDeactivated, bool EnableBotAccountCreation, bool RestrictLinkPreviews, bool EnableSVGs, bool EnableLatex, bool EnableOpenTracing, bool Directory, bool RetentionDays, bool ExperimentalDataPrefetch, bool EnableLocalMode; **TeamSettings**: bool EnableUserCreation, bool EnableTeamCreation, bool RestrictTeamNames, enum RestrictTeamInvite, enum RestrictPublicChannelManagement, enum RestrictPrivateChannelManagement, enum RestrictPublicChannelCreation, enum RestrictPrivateChannelCreation, enum RestrictPublicChannelDeletion, enum RestrictPrivateChannelDeletion, enum RestrictPrivateChannelManageMembers, bool EnableOpenServer, bool EnableUserDeactivation, bool EnableCustomBrand, bool RestrictDirectMessage, enum MaxNotificationsPerChannel, bool EnableConfirmNotificationsToChannel; enum MaxUsersPerTeam, enum MaxChannelsPerTeam, bool EnableCustomUserStatuses, bool ExperimentalTownSquareIsReadOnly, bool ExperimentalHideTownSquareinLHS, bool EnableXToLeaveChannelsFromLHS, bool ExperimentalEnableAutomaticReplies, bool ExperimentalViewArchivedChannels, bool LockTeammateNameDisplay; **ClientRequirementSettings**: enum AndroidLatestVersion, enum AndroidMinVersion, enum DesktopLatestVersion, enum DesktopMinVersion, enum IosLatestVersion, enum IosMinVersion; **DisplaySettings**: bool ExperimentalTimezone; **GuestAccountsSettings**: bool Enable, bool AllowEmailAccounts, bool EnforceMultifactorAuthentication; **SqlSettings**: enum DriverName, bool Trace, enum MaxIdleConns, enum ConnMaxIdleTimeMilliseconds, bool ConnMaxLifetimeMilliseconds; enum MaxOpenC onns, enum QueryTimeout, bool DisableDatabaseSearch; **LogSettings**: bool EnableConsole, enum ConsoleLevel, bool ConsoleJson, bool EnableFile, enum FileLevel, bool FileJson, bool EnableWebhookDebugging; **NotificationLogSettings**: bool EnableConsole, bool ConsoleLevel, bool ConsoleJson, bool EnableFile, bool FileLevel, bool FileJson **PasswordSettings**: bool Lowercase, bool Number, bool Uppercase, bool Symbol, enum MinimumLength; **FileSettings**: bool EnablePublicLink, enum DriverName, enum MaxFileSize, bool FileSettings.ExtractContent, bool FileSettings.ArchiveRecursion, bool AmazonS3SSL, bool AmazonS3SignV2, bool AmazonS3SSE, bool AmazonS3Trace, bool EnableFileAttachments, bool EnableMobileUpload, bool EnableMobileDownload; **EmailSettings**: bool EnableSignUpWithEmail, bool EnableSignInWithEmail, bool EnableSignInWithUsername, bool RequireEmailVerification, bool SendEmailNotifications, bool UseChannelInEmailNotifications, bool EmailNotificationContentsType, bool EnableSMTPAuth, enum ConnectionSecurity, bool SendPushNotifications, enum PushNotificationContents, bool EnableEmailBatching, bool SkipServerCertificateVerification, enum EmailBatchingBufferSize, enum EmailBatchingInterval, bool EnablePreviewModeBanner, enum SMTPServerTimeout; **MessageExportSettings**: bool DownloadExportResults; **RateLimitSettings**: bool EnableRateLimiter, bool VaryByRemoteAddr,  bool VaryByUser, enum PerSec, enum MaxBurst, enum MemoryStoreSize; **PrivacySettings**: bool ShowEmailAddress, bool ShowFullName; **ThemeSettings**: bool EnableThemeSelection, bool AllowCustomThemes; **GitLabSettings**: bool Enable; **GoogleSettings**: bool Enable; **Office365Settings**: bool Enable; **SupportSettings**: bool CustomTermsOfServiceEnabled; enum CustomTermsOfServiceReAcceptancePeriod; **LdapSettings**: bool Enable, bool EnableSync, enum ConnectionSecurity, bool SkipCertificateVerification, enum SyncIntervalMinutes, enum QueryTimeout, enum MaxPageSize, bool EnableAdminFilter; **ComplianceSettings**: bool Enable, bool EnableDaily; **LocalizationSettings**: enum DefaultServerLocale, enum DefaultClientLocale, enum AvailableLocales; **SamlSettings**: bool Enable, bool EnableSyncWithLdap, bool IgnoreGuestsLdapSync, bool EnableSyncWithLdapIncludeAuth, bool Verify, bool Encrypt, bool SignRequest, bool EnableAdminFilter; **ClusterSettings**: bool Enable, bool UseIpAddress, bool UseExperimentalGossip, bool ReadOnlyConfig, bool EnableExperimentalGossipEncryption, bool EnableGossipCompression; **MetricsSettings**: bool Enable, enum BlockProfileRate; **WebrtcSettings** (only in v5.5 and earlier): bool Enable; **ExperimentalSettings** bool ClientSideCertEnable, bool EnablePostMetadata, bool LinkMetadataTimeoutMilliseconds, bool EnableClickToReply, bool RestrictSystemAdmin, bool UseNewSAMLLibrary, bool CloudBilling, bool CloudUserLimit, bool RemoteClusters, bool EnableSharedChannels; **AnnouncementSettings**: bool EnableBanner, bool AllowBannerDismissal, bool AdminNoticesEnabled, bool UserNoticesEnabled; **ElasticsearchSettings**: bool EnableIndexing, bool EnableSearching, bool Sniff, enum PostIndexReplicas, enum PostIndexShards, enum LiveIndexingBatchSize, enum BulkIndexingTimeWindowSeconds, enum RequestTimeoutSeconds, bool SkipTLSVerification, bool Trace; **PluginSettings**: bool Enable, bool EnableUploads, bool EnableHealthCheck, bool EnableMarketplace, bool EnableRemoteMarketplace, bool AutomaticPrepackagedPlugins, bool RequirePluginSignature; **DataRetentionSettings**: bool EnableMessageDeletion, bool MessageRetentionDays, bool AllowInsecureDownloadUrl, bool EnableFileDeletion, bool FileRetentionDays, enum DeletionJobStartTime; **MessageExportSettings**: bool EnableExport, enum ExportFormat, enum DailyRunTime, enum ExportFromTimestamp, enum BatchSize, enum GlobalRelaySettings.CustomerType; **ExperimentalAuditSettings**: bool SysLogEnabled, bool SysLogInsecure, enum SysLogMaxQueueSize, bool FileEnabled, enum FileMaxSizeMB, enum FileMaxAgeDays, bool FileMaxBackups, bool FileCompress, enum FileMaxQueueSize; **BleveSettings**: bool EnableIndexing, bool EnableSearching, bool EnableAutocomplete, enum BulkIndexingTimeWindowSeconds; bool FeatureFlags
  
  **Counts (integer)**

   **SqlSettings**: int DataSourceReplicas, int DataSourceSearchReplicas, int ReplicaLagSettings; **ThemeSettings**: int AllowedThemes; **PluginSettings**: int SignaturePublicKeyFiles

  **True/false (boolean)** value whether setting remains default (true) or non-default (false). **NOTE: No input data is used**:

   **ServiceSettings**: bool SiteURL, bool WebsocketURL, bool TLSCertFile, bool TLSKeyFile, bool ReadTimeout, bool WriteTimeout,bool IdleTimeout, bool GoogleDeveloperKey, bool AllowCorsFrom, bool CorsExposedHeaders, bool AllowedUntrustedInternalConnections, bool GfycatApiKey, bool GfycatApiSecret, bool ManagedResourcePaths; **TeamSettings**: bool SiteName, bool CustomBrandText, bool CustomDescriptionText, bool UserStatusAwayTimeout, bool ExperimentalPrimaryTeam; **DisplaySettings**: bool CustomUrlSchemes; **GuestAccountSettings**: bool RestrictCreationToDomains; **LogSettings**: bool FileLocation; **NotificationLogSettings**: bool FileLocation; **EmailSettings**: bool FeedbackName, bool FeedbackEmail, bool FeedbackOrganization, bool LoginButtonColor, bool LoginButtonBorderColor, bool LoginButtonTextColor, bool ImageProxyType, bool ImageProxyURL, bool ImageProxyOptions; **RateLimitSettings**: bool VaryByHeader; **SupportSettings**: bool TermsOfServiceLink, bool PrivacyPolicyLink, bool AboutLink, bool HelpLink, bool ReportAProblemLink, bool AppCustomURLSchemes, bool SupportEmail; **ThemeSettings**: bool DefaultTheme; **TimeZoneSettings**: bool SupportedTimezonesPath; **LdapSettings**: bool FirstNameAttribute, bool LastNameAttribute, bool EmailAttribute, bool UserNameAttribute, bool NicknameAttribute, bool IdAttribute, bool PositionAttribute, bool LoginFieldName, bool LoginButtonColor, bool LoginButtonBorderColor, bool LoginButtonTextColor, bool GroupFilter, bool GroupDisplayNameAttribute, bool GroupIdAttribute, bool GuestFilter, bool AdminFilter; **SamlSettings**: bool SignatureAlgorithm, bool CanonicalAlgorithm, bool ScopingIDPProviderId, bool ScopingIDPName, bool IdAttribute, bool GuestAttribute, bool FirstNameAttribute, bool LastNameAttribute, bool EmailAttribute, bool UserNameAttribute, bool NicknameAttribute, bool LocaleAttribute, bool PositionAttribute, bool LoginIdAttribute, bool LoginButtonText, bool LoginButtonColor, bool LoginButtonBorderColor, bool LoginButtonTextColor, bool AdminFilter; **NativeAppSettings**: bool AppDownloadLink, bool  AndroidAppDownloadLink, bool IosAppDownloadLink; **WebrtcSettings** (only in v5.5 and earlier): bool StunURI, bool TurnURI; **ClusterSettings**: bool NetworkInterface, bool BindAddress, bool AdvertiseAddress; **MetricsSettings**: bool BlockProfileRate; **AnalyticsSettings**: bool MaxUsersForStatistics; **ExperimentalSettings** bool ClientSideCertCheck; **AnnouncementSettings**: bool BannerColor, bool BannerTextColor; **ElasticsearchSettings**: bool ConnectionUrl, bool Username, bool Password, bool IndexPrefix; **PluginSettings**: bool MarketplaceUrl, bool SignaturePublicKeyFiles; **MessageExportSettings**: bool GlobalRelaySettings.SmtpUsername, bool GlobalRelaySettings.SmtpPassword, bool GlobalRelaySettings.EmailAddress

Commercial License Information (Enterprise Edition Only)
  Information about commercial license key purchased or trial license key used for Enterprise Edition servers: Company ID, license ID, license issue date, license start date, license expiry date, number of licensed users, license short name (E10 vs E20), list of unlocked Enterprise features.

Channel Moderation Configuration Information (Enterprise Edition Only)
  Information related to channel moderation, including number of channel schemes, number of channels with posting messages disabled for users or guests, number of channels with emoji reactions disabled for users or guests, number of channels with managing members disabled, number of channels with channel mentions disabled for users or guests.
  
Channel Member Management Information (Enterprise Edition Only)
  Information related to bulk user management and team and channel filtering, including number of users added, number of users removed, number of users promoted, number of users demoted, number of times archive and unarchive is used from any channel configuration page, and number of times channel search or team search filters are used.

Groups Configuration Information (Enterprise Edition Only)
  Information related to AD/LDAP groups, including number of groups synced to Mattermost, teams and channels associated to groups, teams and channels synced with groups, and number of group members.

Plugin Configuration Information
  Basic information including number of active and inactive plugins, which are using webapp or backend portions, and which `Mattermost plugins <https://github.com/mattermost/mattermost-server/blob/master/app/diagnostics.go#L668>`__ are enabled along with their versions. Some plugins may send summary data such as number of authenticated users of the plugin. From version 5.26, the list of plugins is obtained from the Marketplace. If the Marketplace can't be reached, the list of known plugins is used instead.

Permissions Configuration Information (Enterprise Edition Only)
  Permissions configured for each role for the System Scheme and each Team Override Scheme created in the system. Scheme ID; Team Admin permissions; team user permissions; Channel Admin permissions; channel user permissions; number of teams the scheme is associated with; number of users assigned to each admin role; Number of admin roles not using default privileges; Changes to default privileges of each admin role.

Aggregated Usage Statistics
  Non-personally identifiable summations of basic usage statistics: Number of enabled and disabled accounts, number of user logins in the last 24 hours and the last 30 days, number of users active in the last day/month, whether APIv3 endpoints were used in the last 24 hours, number of posts, channels, teams, guest accounts, and bots.

Event data
~~~~~~~~~~~

Reporting Frequency
  - Immediately after the specific event occurs.

.. note::

  The majority of these events have been disabled since Mattermost v5.8. Refer to the source file for the `current list of events sent via telemetry <https://github.com/mattermost/mattermost-redux/blob/master/src/client/client4.ts#L3069>`__.

Non-personally Identifiable Error Information, distinguished by end users and System Admins
  Boolean when the following events occur:
  
  - *Sign-in Error*: Email login error, AD/LDAP login error, SAML login error
  
  Boolean when the following events occur, including the error message, recently dispatched Redux actions, and non-identifiable information of the device, operating system, and the app:

  - *Mobile App Errors*: App crashes caused by type errors, exceptions, and failed logins

Non-personally Identifiable Diagnostic Information, distinguished by end users and System Admins
  Boolean when the following events occur:

  - *Team and Account Setup Diagnostics:* Account creation via email, invite or UI, account creation page view, account creation completion; tutorial step and tip completion or opt out, team creation page view, team name and URL entry, team creation completion, clicks on all form elements, buttons, textboxes and links on sign up page, team selection page, and team creation pages
  - *Sign-in Diagnostics:* Login succeeded or failed for email, LDAP, or SAML/SSO; logout succeeded; switched authentication method from email to LDAP or SAML/SSO or vice versa; reset password; updated password
  - *Navigation Discovery Diagnostics:* Joined a channel from the "More" list, through an invite or by clicking a public link; created a channel, direct, or group direct message conversation; renamed, joined, left or deleted an existing channel; updated header or purpose; added or removed members; updated channel notification preferences; loaded more messages in a channel; switched a channel or a team; opened the "More" modal for channels or direct message conversations; updated team name; invited members; updated account settings
  - *Core Feature Discovery Diagnostics:* Created, edited or deleted a message; posted a message containing a hashtag, link, mention or file attachment; searched for a term; searched for saved posts or recent mentions
  - *Advanced Feature Discovery Diagnostics:* Reacted to a message; favorited or unfavorited a channel; saved or unsaved a message; pinned or unpinned a message; replied to a message; expanded the right-hand sidebar; started or finished a WebRTC video call (only in v5.5 and earlier); created or deleted a personal access token; added or removed post:all or post:channels permission; created a category in the sidebar
  - *Integration Discovery Diagnostics:* Created or triggered a webhook or slash command; created, authroized or deleted an OAuth 2.0 app; created, posted, or deleted a custom emoji
  - *Plugin Discovery Diagnostics:* Number of installed plugins containing either server or webapp portions, or both; number of those plugins being activated
  - *Plugin Marketplace Diagnostics:* Plugin ID, current version, and target version for all install and update events. Only sent when the default Marketplace is configured
  - *Commercial License Diagnostics (Enterprise Edition Only):* Uploaded an Enterprise license key to the server
  - *Mobile Performance Diagnostics:* Load times for starting the app, switching channels, and switching teams
  - *Permissions Discovery Diagnostics (Enterprise Edition Only):* Provides all the permissions configured for each role for the System Scheme and each Team Override Scheme created in the system. Scheme ID; Team Admin permissions; Team user permissions; Channel Admin permissions; Channel user permissions; Number of teams the scheme is associated with
  - *Group Discovery Diagnostics (Enterprise Edition Only):* Provides information related to AD/LDAP groups, including number of groups synced to Mattermost, teams and channels associated to groups, teams and channels synced with groups, and number of group members
  - *System Console Menu Discovery Diagnostics:* Clicks on the hamburger menu items of the System Console, including Administrator's Guide, Troubleshooting Forum, Commercial Support, About Mattermost, and clicks on the left-hand side navigation menu items
  - *In Product Notices Diagnostics:* Notices viewed, and the notices on which an action button was clicked.

Incident Collaboration Telemetry
--------------------------------

The following list details the types of Incident Collaboration metadata we collect:

**Data collected for all event types**

- ``PluginVersion``: Version of the plugin.
- ``ServerVersion``: Version of the server the plugin is running on.
- ``UserID``: Unique identifier of the server.
- ``Event``: Type of the event. There are three event types that are tracked: ``incident``, ``tasks``, ``playbook``.
- ``UserActualID``: Unique identifier of the user who initiated the action.

**Data collected in incident events**

- ``IncidentID``: Unique identifier of the incident.
- ``IsActive``: Boolean value indicating if the incident is active.
- ``CommanderUserID``: Unique identifier of the commander of the incident.
- ``TeamID``: Unique identifier of the team where the incident channel is created.
- ``CreatedAt``: Timestamp of the incident creation.
- ``PostID``: Unique identifier of the post from which the incident was created (if relevant).
- ``NumChecklists``: Number of stages in this incident.
- ``TotalChecklistItems``: Number of tasks in this incident.
- ``ActiveStage``: A number indicating the stage of the incident (0-based).
- ``Action``: The type of action performed against the incident: ``create``, ``end``, ``restart``, ``change_stage``, ``change_commander``, ``update_status``.
- ``Public``: When creating an incident, ``true`` if it is public, and ``false`` if it is private.
- ``ReminderTimerSeconds``: The next timer for the reminder to update the status, in seconds. It's tracked only when ``Action`` equals ``update_status``.

**Data collected in tasks events**

- ``IncidentID``: Unique identifier of the incident.
- ``NewState``: ``null`` if the task is uncompleted, ``done`` if the task was marked completed.
- ``Action``: The type of action performed against the task: ``add_task``, ``remove_task``, ``rename_task``, ``modify_task_state``, ``move_task``, ``set_assignee_for_task``, ``run_task_slash_command``.
- ``NewState``: When modifying a task state, ``true`` if the task is now checked, ``false`` if the task is now unchecked.
- ``WasCommander``: When modifying a task state, ``true`` if the userId who initiated the event was also the commander of the event, and ``false`` otherwise.
- ``WasAssignee``: When modifying a task state, ``true`` if the userId who initiated the event was also the assignee of the event, and ``false`` otherwise.

**Data collected in playbook events**

- ``PlaybookID``: Unique identifier of the playbook.
- ``TeamID``: Unique identifier of the team associated with this playbook.
- ``NumChecklists``: Number of stages in this playbook.
- ``TotalChecklistItems``: Number of tasks in this incident.
- ``IsPublic``: ``true`` if the playbook is public, ``false`` if it is private.
- ``NumMembers``: The number of members with access to this playbook.
- ``NumSlashCommands``: The number of tasks with slash commands in this playbook.
- ``ReminderTimerDefaultSeconds``: The default timer for the reminder to update the status, in seconds.
- ``BroadcastChannelID``: Unique identifier of the channel where the status updates will be broadcasted.
- ``UsesReminderMessageTemplate``: ``true`` if the playbook has a template for the reminder message, ``false`` otherwise.
- ``Action``: The type of action performed against this playbook: ``create``, ``update``, ``delete``.
  
Error and diagnostic reporting is sent by the client to the endpoint ``api.segment.io``. To opt out, disable the feature in **System Console > Environment > Logging**.

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
