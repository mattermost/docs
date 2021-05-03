# Mattermost Cloud Changelog

This changelog summarizes updates to [Mattermost Cloud](https://mattermost.com/get-started/), an enterprise-grade SaaS offering hosted by Mattermost.

## Release 2021-05-05

### Improvements

#### User Interface (UI)
 - If message autoresponder is set, only one message is now sent to a given user irrespective of how many Direct Message messages the user receives.
 - Added status icons on **Add members** to channel and **Add members** to team lists.
 - Added a keyboard shortcut to focus on the Search bar and search in the current channel.

#### Administration
 - Gossip clustering mode is now in General Availability and is no longer available as an option. All cluster traffic will always use the gossip protocol. The config setting ``UseExperimentalGossip`` has no effect and has only been kept for compatibility purposes. The setting to use gossip has been removed from the System Console. **Note:** For High Availability upgrades, all nodes in the cluster must use a single protocol. If an existing system is not currently using gossip, one node in a cluster can't be upgraded while other nodes in the cluster use an older version. Customers must either use gossip for their High Availability upgrade, or customers must shut down all nodes, perform the upgrade, and then bring all nodes back up.
 - ``TCP_NO_DELAY`` is disabled for Websocket connections to allow for higher throughput.
 - Compliance Monitoring CSV files are no longer limited to 30,000 rows.

### Bug Fixes
 - Fixed an issue where bulk export generated invalid Direct Message channels between deactivated users.
 - Fixed an issue where the custom status cleared slash commands on mobile.
 - Fixed an issue with an incorrect error message when trying to change handle via API to another one that already existed.
 - Fixed an issue where LDAP Group Sync didn't work when using SAML (ADFS) for authentication and AD/LDAP Group Sync unless ``EnableSyncWithLdapIncludeAuth`` was set to ``true``, which caused the ``AuthData`` to be stored in AD/LDAP format.
 - Fixed an issue where a user with 'No Access' permission could still access **Groups**, **Channels** and **Teams** configuration pages through a URL.
 - Fixed an issue where **Remove from channel** and **Remove Team Member** menu items were visible in a group-synced channel or team.
 - Fixed various bugs related to hardcoded theme colours.
 - Fixed UI issues related to hardcoded variables and misalignment of the channel header with the **Has guests** text.
 - Fixed an issue with SAML Sign-on where System Admins were unable to modify **Service Provider Login URL** unless ``VerifySignature`` was enabled.

### Known Issues
 - Pinned posts are no longer highlighted.
 - Sometimes an "Unable to get role" error appears when changing a channel member role in **System Console > User Management > Channels**.
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-04-22

### Highlights

#### Apps Framework (Developer Preview)
 - The Mattermost Apps Framework introduces a new way to integrate with external tools to allow developers to create interactive Apps in Mattermost using any development language they're comfortable with. These Apps work seamlessly across mobile and desktop clients. This is a developer preview that is not yet intended for production instances of Mattermost. The Apps Framework will be available for self-managed customers in Mattermost v5.35 once the Apps Framework Plugin is loaded on an instance. Until then, developers can use the `cloud` branch to get a local test environment running. The launch for the Developer Preview of the Apps Framework is scheduled for April 29th, 2021. Learn more: https://developers.mattermost.com/integrate/apps/.

#### Search Results Are Returned on File Search
 - Searching in Mattermost now finds both relevant messages and files in your team's conversation history. Search will return results for attachments that match the file name or contain matching text content within supported document types. Learn more. To be available for mobile apps in a later release.

#### Granular Access to System Console Pages
 - Migrated the following System Console sections to their respective sub-section permissions: Experimental, About, Reporting, Environment, Site Configuration, Authentication, Integrations, and Compliance.

#### Shared Channels (Experimental)
 - Experimental support was added for sharing channels between Mattermost clusters. This feature is disabled by default.

### Improvements

#### User Interface (UI)
 - Added support to collapse in-line images over 100px in height.
 - Implemented maximum length validation on the status modal for custom statuses.
 - Synchronized collapsed channel sidebar categories on the server.
 - Empty state is no longer off-centered in the **Channel Switcher**.
 - Ephemeral message created from call response ``markdown`` field is now posted by bot.
 - Added improvements and fixes for the custom status feature. For example, fixed an issue where recently selected statuses were missing from the **Set a Status** confirmation screen, and updated the **Mobile Push Notifications** text in **Account Settings** to refer to user **availability** instead of **online status**.
 - Moved the user status in the channel switcher to overlap with user avatars, and added URL 'Slug' information to channel names in the channel switcher.

#### Administration
 - Paused admin advisor notifications from triggering.
 - Added a command line document extraction command that allows indexing documents by content.

### Bug Fixes
 - Fixed link previews on a number of websites, including Reddit.
 - Fixed an issue where SAML assigned Mattermost ``UserID`` as username if the value was invalid and did not log this.
 - Fixed an issue where hover effects for category sorting and **Direct Messages** category limit submenus were too dark on a dark theme.
 - Fixed an issue where users were unable to drag the vertical scroll bar on a PDF preview.
 - Fixed an issue with animations on long posts when highlighted as a permalink.
 - Fixed an issue where the user's nickname was not shown on channel switch.
 - Fixed an issue where deactivated users were not marked as "Deactivated" in the channel switcher.
 - Fixed an issue where queries executed during the upgrade process would preemptively time out on the application side.

### Known Issues
 - Pinned posts are no longer highlighted.
 - Posts in the thread disappear when deleting a post from a permalink view.
 - Sometimes an "Unable to get role" error appears when changing a channel member role in **System Console > User Management > Channels**.
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-04-07

### Improvements

#### User Interface (UI)
 - Added a string field to configuration for restricted domains with the key ``RestrictLinkPreviews`` and added a UI field for restricted domains under **System Console > Site Configuration > Posts**. Also expanded the logic that determines whether a post has a preview or not.
 - Added an unread badge to the **Main Menu** icon and the **Plugin Marketplace** menu that displays until a System Admin visits the **Plugin Marketplace** for the first time.
 - Removed Beta tags from Swedish and Bulgarian languages.
 - Added profile pictures to the **Direct Messages** channel list.
 - Added channel icons for email notifications as part of email notification redesigns.
 - Direct Messages **More...** modal is now sorted by recent conversations when the modal is opened.
 - Removed legacy Open-Sans fonts and upgraded Open-Sans to v18.

#### Administration
 - Removed the utility function ``model.GeneratePassword()`` for security reasons. An improved version is now being used internally to generate passwords for bulk-imported users.
 - Only the System Admin is allowed to have the ability to assign system roles.
 - Two new gauge metrics were added: ``mattermost_db_replica_lag_abs`` and ``mattermost_db_replica_lag_time``, both containing a label of "node", signifying which database host is the metric from. 
     - These metrics signify the replica lag in absolute terms and in the time dimension capturing the whole picture of replica lag. To use these metrics, a separate config section ``ReplicaLagSettings`` was added under ``SqlSettings``. This is an array of maps which contain three keys: ``DataSource``, ``QueryAbsoluteLag``, and ``QueryTimeLag``. Each map entry is for a single replica instance. ``DataSource`` contains the database credentials to connect to the replica instance. ``QueryAbsoluteLag`` is a plain SQL query that must return a single row of which the first column must be the node value of the Prometheus metric, and the second column must be the value of the lag. ``QueryTimeLag`` is the same as above, but used to measure the time lag. 
     - As an example, for AWS Aurora instances, the ``QueryAbsoluteLag`` can be: ``select server_id highest_lsn_rcvd-durable_lsn as bindiff from aurora_global_db_instance_status()`` where ``server_id=<>`` and ``QueryTimeLag`` can be: ``select server_id, visibility_lag_in_msec aurora_global_db_instance_status()`` where ``server_id=<>``. For MySQL Group Replication, the absolute lag can be measured from the number of pending transactions in the applier queue: ``select member_id, count_transactions_remote_in_applier_queue FROM performance_schema.replication_group_member_stats`` where ``member_id=<>``. Overall, what query to choose is left to the administrator, and depending on the database and need, an appropriate query can be chosen.

### Bug Fixes
 - Fixed an issue where users were unable to deactivate MFA for their accounts even if MFA was disabled on the server.
 - Fixed an issue where user settings on API could be set if LDAP Sync was on. For LDAP and SAML users, the following fields cannot be changed via the API if the corresponding LDAP/SAML attributes have been set: first name, last name, position, nickname, email, profile picture. For OAUTH users (i.e., Gitlab, Google, Office365 and OpenID), the following fields cannot be changed via the API: first name, last name. All users who authenticate via a method other than email cannot change their username via the API.
 - Fixed a possible panic on post creation when the collapsed threads feature was enabled.
 - Fixed a database deadlock that could happen if a sidebar category was updated and deleted at the same time.
 - Fixed an issue where the sidebar **Text Hover BG Theme** color didn’t work on the left-hand side.
 - Fixed an issue where the Team Admin’s current role was presented inconsistently in the different areas of the System Console.
 - Fixed an issue where the **Show more** background color on long posts was broken for permalinks.

### Known Issues
 - Channel Members popover menu items have extra spacing.
 - Deactivated users are not marked as "Deactivated" in the channel switcher.
 - User nickname is not shown on channel switch.
 - Sometimes an "Unable to get role" error appears when changing a channel member role in **System Console > User Management > Channels**.
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-03-24

### Improvements

#### User Interface (UI)
 - Added support for automatic right-to-left (RTL) detection in browsers.
 - Updated the font size for the **Add People** channel modal.
 - Online status is now shown in the channel switcher.
 - Improved the design and layout of email notifications for password resets, member invites, member welcome, and verifications.

#### Administration
 - Added ``mmctl`` commands to create, list, download, and delete export files.
 - Profiling the Mattermost server with pprof is now available for Team Edition.
 - Added attributes to split.io feature flags.

### Bug Fixes
 - Fixed bugs related to replication lag for Enterprise Edition instances configured to use read replicas.
 - Fixed an issue where Compliance Report field headers were not correctly aligned.
 - Fixed an issue where the ``/join`` command was case-sensitive.
 - Fixed an issue where one-character sidebar category names were not displayed.
 - Fixed an issue with a theme discrepancy on close buttons on some modals in the System Console (when using a custom team theme).
 - Fixed an issue where long text input in the right-hand pane was jumpy when selected.
 - Fixed an issue where the Zoom level persisted across multi-attachment PDF previews.

### Known Issues
 - Deactivated users are not marked as "Deactivated" in the channel switcher.
 - User nickname is not shown on channel switch.
 - Sometimes an "Unable to get role" error appears when changing a channel member role in **System Console > User Management > Channels**.
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-03-12

### Highlights

#### Custom Statuses
 - Custom Statuses allow users to add a descriptive status message and emoji that’s visible to everyone. Users now gain the flexibility to express their current status in any way they prefer. Mobile support is coming in a future release.

### Improvements

#### User Interface (UI)
 - System Admins are now prompted when joining a private channel via a permalink.
 - Added support for adding in-product notices for external dependency deprecation details.
 - Improved the timezone selector component.
 - Introduced a new theme variable for the team sidebar.

#### Administration
 - Added schema migrations phase 0 (``Teams``, ``TeamMembers``).
 - Removed any references to ``SqlLite3`` from the code.
 - Bleve updates are now logged in the config only when there is an actual change in the ``BleveSettings`` instead of on every config update.

### Bug Fixes
 - Fixed unsafe access of properties of the plugin environment during ``ServePluginPublicRequest``.
 - Fixed an issue where the Admin Console > Server Logs did not focus to the sidebar filter upon reload.
 - Fixed an issue where the Gif picker appeared empty instead of showing a “No results” modal when no results were displayed.
 - Fixed an issue where the keyboard accessibility controller was not allowed to resume left-hand side scroll after drag and drop.
 - Fixed an issue where markdown links rendered incorrectly.
 - Fixed an issue where the slack theme import failed due to changes in formatting of Slack export color schemes.
 - Fixed an issue where tooltips were missing for channels with a long name.
 - Fixed a race condition which would crash the app server due to improper handling of websocket closing.
 - Fixed an issue where the PDF zoom failed to respond to zoom in/out/reset actions until the user scrolled.
 - Fixed an issue where in a reply thread with the right-hand side expanded, attachments in a post draft got hidden behind the center channel text box.

### Known Issues
 - Sometimes an "Unable to get role" error appears when changing a channel member role in **System Console > User Management > Channels**.
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-02-25

### Highlights

#### Support Packet Generation
 - Allows a System Admin to download a support packet which provides helpful information to our internal support team.

### Improvements

#### User Interface (UI)
 - Removed the 5-page limit on previewing PDFs.
 - Added "files" as a reserved team name.
 - Searching for a channel by URL now returns the channel.
 - Users are now provided with feedback when creating a custom category name that exceeds the character limit.

#### Administration
 - Added support for compressed export files with attachments.
 - Server crashes due to runtime panics are now captured as a log line.
 - Optimized Direct Message creation by fetching all users involved in a single database call.
 - During the user import process, a change in a user's ``NotifyProps`` will not send an email notification. This is done to make it consistent with other parts of the import process where a change in user's attributes would also not send any notifications.
 - Implemented a job to delete unused export files.
 - Improved the websocket implementation by using epoll to manually read from a websocket connection. As a result, the number of goroutines is expected to go down by half. This implementation is only available on Linux and FreeBSD-based distributions. If you are using NGINX as a proxy to Mattermost, please ensure to have ``proxy_http_version 1.1;`` in the block that handles the websocket path.

### Bug Fixes
 - Fixed an issue where demoting a user to a guest would not take effect in an environment with read replicas.
 - Fixed an issue where creation of a bot would fail due to replica lag.
 - Fixed an issue where ``mmctl channel move`` did not allow private channels to move.
 - Fixed an issue where markdown tables did not wrap correctly.
 - Fixed an issue where the search bar styling on dark themes was incorrect on mobile web view.
 - Fixed an issue where the **Main Menu** on webapp appeared more left-aligned than previous releases.
 - Fixed an issue where sticky sidebar headings appeared under **More Unreads**.
 - Fixed an issue where the group channel icon was misaligned in the channel switcher.
 - Fixed an issue where line breaks were ignored when used with inline images.
 - Fixed a panic when the OAuth discovery endpoint would not return a Cache-Control header.
 - Fixed an issue where the Cloud onboarding flow referenced OAuth, not OpenID Connect.

### Known Issues
 - PDF zoom fails to respond to zoom in/out/reset actions until the user scrolls.
 - In a reply thread with the right-hand side expanded, attachments in a post draft get hidden behind the center channel text box.
 - Sometimes an "Unable to get role" error appears when changing a channel member role in **System Console > User Management > Channels**.
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-02-10

### Highlights

#### OpenID Connect (Cloud Professional & Enterprise)
 - OpenID Connect enables authentication to Mattermost using any OAuth 2.0 provider that adheres to the OpenID Connect specification. **This feature will be available for Mobile Apps in an upcoming v1.40 release.**

### Improvements

#### User Interface (UI)
 - Improved the **Add Members** modal user interface.
 - Added formatting shortcut keys to the **Shortcut** modal.
 - Added localization to the date picker used when searching for posts around a given date.
 - The autocomplete popover is now positioned relative to the ``@``, ``~``, or ``/`` trigger in the post draft.

#### Notifications
 - Posts from OAuth 2.0 bots no longer trigger mentions for the user.

#### Administration
 - Added an ``ImportDelete`` job to periodically delete unused import files after a configurable retention period has passed.
 - Introduced new ``mattermost_system_server_start_time`` and ``mattermost_jobs_active`` metrics for improved debugging with Grafana dashboards.
 - Deleting a reaction is now a soft delete in the ``Reactions`` table. A schema update is required and may take up to 15 seconds on first run with large data sets.
 - Changed default ``MaxFileSize`` from 50MB to 100MB.
 - Updated Go dependencies to their latest minor version.

### Bug Fixes
 - Fixed an issue where ``mmctl config set PluginSettings.EnableUploads`` did not change the configuration value.
 - The ``DownloadComplianceReport`` function in the Golang driver has been fixed to be able to download a full report as a zip archive.
 - Fixed Cache-Control headers to instruct that responses may only be cached on browsers.
 - Fixed a bug with in-product notices where a date constraint sometimes failed to match, and would lead to the notice not being fetched.
 - Fixed an issue where the channel switcher did not focus on the first list result after a backspace.
 - Fixed an issue where the in-product instructions to search for users under **System Console > Reporting > Server Logs** were outdated.
 - Fixed an issue where no error message was displayed when adding an LDAP Group Synchronized Team in **System Console > User Management > Users**.

### Known Issues
 - The slash command autocomplete options cover the input box on some reply threads on the right-hand side.
 - Sometimes an "Unable to get role" error appears when changing a channel member role in **System Console > User Management > Channels**.
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-01-26

### Highlights

#### Channel Sidebar Improvements
 - New channel sidebar improvements include a configurable **Unreads** category as well as the ability to sort categories by recent activity or alphabetically in addition to manually.
 
### Improvements

#### User Interface (UI)
 - Added new languages, Bulgarian and Swedish.
 - Moved the header icons to the left of the header beside the channel description.
 - The Database search using PostgreSQL now supports searching for terms that contain underscores.

#### Plugins
 - Enabled experimental support for ARM64 plugins by allowing any matching ``GOOS-GOOARCH`` combination in the plugin manifest.

#### Administration
 - The ``UseExperimentalGossip`` field under ClusterSettings is now ``true`` by default. This means that new installations will use the Gossip protocol for cluster communication. There will be no changes to existing installations. The Gossip protocol is now considered to be in General Availability and is the recommended clustering mode.
 - ``AnalyticsPostCount`` now avoids unnecessary table scans during various background jobs.
 - Added a ``CollapsedThreads`` feature flag.
 - The Help text for the Rate Limiting setting was updated to explain the purpose of rate limiting.
 - Removed the word "experimental" from the Gossip setting in the System Console.
 - Deprecated the ``ExperimentalChannelSidebarOrganization`` setting and added a new ``EnableLegacySidebar`` setting. The new channel sidebar will be enabled system-wide by default.

#### Bug Fixes
 - Fixed an issue where the Admin Filter option was not disabled in the AD/LDAP page for Admin roles with a ``sysconsole_write_authentication`` permission.
 - Fixed an issue where channels would sometimes be removed from custom categories when a user left a team.
 - Fixed an issue where the error text was missing when the team name was left blank on the Team Create page.
 - Fixed an issue where the System Manager was able to download the Compliance Export files.
 - Fixed an issue where themed button colours in interactive message attachments in Mattermost’s default dark theme were mismatched.
 - Fixed an issue where bold and italics shortcuts triggered with CTRL+B on Mac.
 - Fixed an issue where a "Your license does not support cloud requests” log error appeared on self-hosted servers.

#### Known Issues
 - Setting changes do not get saved on **System Console > Site Configuration > Public Links**.
 - Alignment of team icons are off on **System Console > User Management >Teams Page**.
 - Alignment of channel header text "This channel has guests" is off.
 - Sometimes an "Unable to get role" error appears when changing a channel member role on **User Management > Channel**.
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-01-12

### Highlights
 - Pre-packaged and pre-installed Mattermost Incident Management v1.2.0.

### Improvements

#### User Interface (UI)
 - Changed the number of file attachments allowed per post, from 5 to 10.
 - Added support to move multi-selected groups of channels to another category via the **More options** menu.
 
#### Administration
 - Updated the Go version to v1.15.5.
 - Added support for automatic installation and enablement of plugins using feature flags.
 - Added ``webhook create`` endpoints to local mode and the ability to create webhooks for other users.
 - Added a Mattermost CLI command to initialize the database.
 - Enabled ``ExperimentalDataPrefetch`` for all servers and removed the corresponding setting.
 - Added support for processing import files through the API.
 - Added support for protocol-relative URLs while using the Image Proxy.
 - Added shared channels and ``remote_cluster_service`` under a license check.
 - A Striped LRU cache is now used by default.

### Bug Fixes
 - Fixed an issue where the permissions of a System Admin role got deleted when changing the access level to any permission.
 - Fixed an issue where editing a ``/me`` post behaved differently within the Mattermost Web App and the Mobile App.
 - Fixed an issue where the hover state on category headers did not span the whole width of the left-hand navigation.
 - Fixed an issue where plugins on the left-hand side of the System Console were sorted differently than the ones in the Plugin Management page.
 - Fixed an issue where 15-character team names were truncated when the experimental channel sidebar was enabled.
 - Fixed an issue where the sidebar menus weren't styled correctly in mobile browser view.
 - Fixed an issue where jumping into an archive channel and clicking the link to jump to recent messages sent the user out of the archived channel.
 - Fixed an issue where the tooltip text for copying an incoming webhook URL was unclear.

### Known Issues
 - Cloud > "Tips & Next Steps" should not show an "Explore channels" section for guest users.
 - System Roles shows License and Environment as possible permissions but they are always hidden in Cloud.

## Release 2020-12-18

### Bug Fixes
 - Fixed a performance issue related to typing lag.
 - Fixed an issue where YouTube previews did not display sometimes.

## Release 2020-12-09

### Improvements

#### User Interface (UI)
 - Added the ability to mute categories with the experimental sidebar feature.
 - Added support for multi-selection of channels when dragging and dropping between channels in the experimental sidebar feature.
 - Group messages are now returned in the channel switcher when only first names are typed.
 - Issuing /dnd consecutively no longer unexpectedly toggles the user status between "Do Not Disturb" and "Online" and will only set the user's status to "Do Not Disturb".

#### Administration
 - Added a new `manage_remote_clusters` permission.
 - Enabled goSAML2 library as the only supported SAML library.

### Bug Fixes
 - Cleaned up the config store on server initialization errors.
 - Fixed an issue where permissions did not grant read and/or write access to the Global Relay configuration settings.
 - Fixed an issue where the site configuration ‘’Read only’’ permission did not make the "Notice" section as read-only for the System Manager.
 - Fixed an issue where importing Client4 in a node server caused an exception due to rudder modules.
 - Fixed an issue where LDAP ‘’FirstLoginSync’’ didn't close the LDAP session.

### Known Issues
 - System Managers do not have access to the Billing section and see a blank screen.
 - Cloud > "Tips & Next Steps" should not show an "Explore channels" section for guest users.
 - System Roles shows License and Environment as possible permissions but they are always hidden in Cloud.

## Release 2020-12-03

### Bug Fixes
  - Disabled the xmlsec1-based SAML library in favor of the re-enabled and improved SAML library.

## Release 2020-11-24

### Highlights

#### Modify new Admin roles permissions in the System Console (Beta)
 - Added a user interface for the existing new system roles functionality including new permissions to read and write system roles.

#### Pre-package and enable incident management v1.1.1

### Improvements

#### User Interface
 - @-autocomplete results are now prioritized based on recency and thread activity.
 - File attachments below the size of 10 (KB, MB, GB, TB, etc.) now allow showing fractions.
 - The formatting of the channel header change message was improved.
 - Team invite workflow now shows BOT tags when the search returns Bot users.
 - Added the ability to zoom in and out of PDF files.
 - Added support for 16x16 base64 encoded mini images to use with progressive rendering.

#### Notifications
 - Channel-wide mentions are now automatically disabled when a user mutes a channel.

#### Integrations
 - Updated icon_emoji field in incoming webhooks to allow emojis to be specified with surrounding colons.
 - Dynamic auto-completion is now supported for built-in slash commands.
 - Added plugin hooks for ReationHasBeenAdded and ReactionHasBeenRemoved.

#### Administration
 - Added the ability to load a set of custom configuration defaults from a MM_CUSTOM_DEFAULTS_PATH environment variable.
 - Added AWS metering service support.
 - Added the ability to retrieve compliance files from the System Console.

### Bug Fixes
 - Fixed an issue with broken link previews for Twitter links.
 - Fixed an issue where editing a post did not submit with CMD+ENTER.
 - Fixed an issue where users were able to create or edit slash commands to contain more than two slashes in the URL.
 - Fixed an issue where resized emojis were being overwritten with original data.
 - Fixed an issue where the sidebar category "More" menu was not shown when hovering over a long category name.
 - Fixed an issue where a received direct message did not show up on the sidebar if the direct message channel was newly created.
 - Fixed an issue where a search using ``from:`` failed to auto-load more results on the right-hand side when Elasticsearch was enabled.
 - Fixed an issue where an s3 file backend TestFileConnection failed due to permissions if S3PathPrefix was in use.
 - Fixed an issue where an id was missing for a Tooltip in PostInfo.

#### API Changes
 - Added new local API endpoints for getting, updating, and deleting incoming and outgoing webhooks.
 - Added new API endpoints to work with experimental collapsed threads.

### Known Issues
 - System Managers do not have access to the Billing section and see a blank screen.
 - Cloud > "Tips & Next Steps" should not show an "Explore channels" section for guest users.
 - System Roles shows License and Environment as possible permissions but they are always hidden in Cloud.
