# Mattermost Cloud changelog

This changelog summarizes updates to [Mattermost Cloud](https://mattermost.com/get-started/), an enterprise-grade SaaS offering hosted by Mattermost.

Latest Mattermost Cloud releases:

- [Release 2023-09-26](#release-2023-09-26)
- [Release 2023-09-12](#release-2023-09-12)
- [Release 2023-08-29](#release-2023-08-29)
- [Release 2023-08-09](#release-2023-08-09)
- [Release 2023-08-03](#release-2023-08-03)
- [Release 2023-07-26](#release-2023-07-26)

## Release 2023-09-26

### Improvements

#### User Interface (UI)
 - Pre-packaged GitLab plugin version v1.7.0.
 - Added additional reaction options when viewing threads or messages when the sidebar is larger than its minimum width.
 - Added block changes to name, display name, and purpose for direct and group messages.
 - Added a link to [notification documentation](https://docs.mattermost.com/preferences/manage-your-notifications.html) in the **Notification Settings** modal.
 - Updated the post textbox measurement code to be more reliable.
 - Pre-packaged Calls version v0.19.1.
 - The ``invite`` slash command now supports custom user groups.
 - Re-enabled the remote marketplace functionality, when configured as per ``PluginSettings.EnableRemoteMarketplace`` [documentation](https://docs.mattermost.com/configure/plugins-configuration-settings.html#plugins-enableremotemarketplace).
 - Added the ability to convert a group message channel to a private channel.
 - Group message channels now behave like direct message channels, showing a new mention for every new message.

#### Administration
 - Added 2 new URL parameters to ``GET /api/v4/groups``: ``include_archived`` and ``filter_archived``. Added the ability to restore archived groups from the user groups modal.
 - Added file storage information to the support package.
 - Improved performance on data retention ``DeleteOrphanedRows`` queries. Removed feature flag ``DataRetentionConcurrencyEnabled``. Data retention now runs without concurrency in order to avoid any performance degradation. Added a new configuration setting ``DataRetentionSettings.RetentionIdsBatchSize``, which allows admins to to configure how many batches of IDs will be fetched at a time when deleting orphaned reactions. The default value is 100.
 - The Go version was bumped to v1.20.
 - A ``user_id`` is now included in all HTTP logs (debug level) to help determine who is generating unexpected traffic.
 - Added a setting ``DisplaySettings.MaxMarkdownNodes`` to limit the maximum complexity of markdown text on mobile.
 - Added new URL Parameter to ``GET /api/v4/groups`` and ``GET /api/v4/groups/:group_id``. ``include_member_ids`` will add all the members ``user_ids`` to the group response objects. You can now also add group members to a channel, any members that are not part of the team can be added to the team through this flow and subsequently added the channel.

### API Changes
 - Added new API endpoint ``GET`` ``/api/v4/channels/<channel-id>/common_teams`` to fetch list of teams common between members of a group message.
 - Added new API endpoint ``POST`` ``/api/v4/channels/<channel-id>/convert_to_channel`` to convert a group message to a private channel.
 - Added a new ``MessageHasBeenDeleted`` hook to the plugin API.
 - Moved the ``request`` package into the public shared folder.

### Bug Fixes
 - Fixed an issue with keyboard support for some menus with submenus.
 - Fixed an issue with a disappearing punctuation when following a group mention.
 - Fixed an issue where compliance export jobs were not able to start after disabling and enabling the compliance export.
 - Fixed a potential read after write issue when loading a license.

### Known Issues
 - Known issues related to the new feature to convert a Group Message channel to a private channel: [MM-54525](https://mattermost.atlassian.net/browse/MM-54525), [MM-54526](https://mattermost.atlassian.net/browse/MM-54526), [MM-54541](https://mattermost.atlassian.net/browse/MM-54541), [MM-54542](https://mattermost.atlassian.net/browse/MM-54542).
 - ``/invite`` user to a channel incorrectly posts an ephemeral message of ``<no value> added to {channel_name} channel`` [MM-54555](https://mattermost.atlassian.net/browse/MM-54555).
 - Left-hand side resize option overrides the **Browse/Create Channel** menu if To-Do plugin is installed [MM-54367](https://mattermost.atlassian.net/browse/MM-54367).

## Release 2023-09-12

### Compatibility
 - Updated Chromium minimum supported version to 116+.

### Improvements

#### User Interface (UI)
 - Added a **Cancel** button to the **Delete category** modal.
 - Added the ability to resize the channel sidebar and right-hand sidebar.
 - Added two new filtering options (show all channel types, show private channels) to the **Browse channels** modal.
 - Pre-packaged Calls version v0.19.0.

#### Administration
 - Added ``mattermost-plugin-api`` into the mono repo.
 - Added a new config setting ``TeamSettings.EnableJoinLeaveMessageByDefault`` that sets the default value for ``UserSetting``, ``ADVANCED_FILTER_JOIN_LEAVE``.

#### API Changes
 - Added the ``X-Forwarded-For`` request header to the audit stream for all Rest API calls.
 - Added API endpoint ``POST /api/v4/user/login/desktop_login``. Modified OAuth/SAML flows to include ``desktop_login`` where applicable.

### Bug Fixes
 - Fixed keyboard support for the left-hand side channel menu, the left-hand side category menu, and the post dot menu.
 - Fixed display name in the ``comment_on`` component.

### Known Issues
 - Left-hand side resize option overrides the **Browse/Create Channel** menu [MM-54367](https://mattermost.atlassian.net/browse/MM-54367).

## Release 2023-08-29

### Improvements

#### User Interface (UI)
 - Added functionality to bulk mark a whole channel category as read.
 - Removed Boards product tour code.
 - Replaced Gfycat with Giphy in the gif picker.
 - Updated Focalboard plugin version to 7.11.3.
 - Pre-packaged Playbooks version 1.38.1.
 - Upgraded prepackaged Zoom plugin to v1.6.2.
 - Enabled prepackaged plugins to be included in the in-product marketplace for Cloud.

#### Administration
 - API examples are now updated to reflect latest Go API conventions, deprecating older code samples.
 - Updated the public server module version to v0.0.7.
 - Added a ``Post Action`` plugin hook to allow plugins to register new items in the post menu.
 - Added a ``Post Editor Action`` plugin hook to allow plugins to register new items in the post editor menu.
 - Improved logging on plugin initialization, activation, and removal.
 - Removed the deprecated ``ManifestExecutables`` struct.
 - Removed the deprecated ``UserAuth.Password`` field.
 - Remote users are no longer counted as part of the license.
 - Improved data retention logs.
 - Removed ``/opengraph`` endpoint as it was unused.
 - Transitionally prepackaged plugins are now installed to the filestore for continuity when a future release stops prepackaging those plugins.
 - Removed the deprecated ``Manifest.RequiredConfig`` field.
 - Added a ``NotificationWillBePushed`` plugin hook invoked before the push notification is processed and sent to the notification service. Plugins may modify or reject the push notification.
 - Added a `SendPushNotification` plugin api method which allows plugins to send push notifications to a specific user's mobile sessions.
 - Disabled ``PluginSettings.EnableRemoteMarketplace`` functionality.

### Bug Fixes
 - Fixed accessibility issues: tab support at login, reset pages, sign up pages, and App bar.
 - Fixed an issue where CRLF line endings passed to mmctl commands were not being stripped from commands.
 - Fixed an issue where text copied from Microsoft OneNote is pasted as an image.
 - Fixed an issue preventing successful activation of trial licenses.
 - Fixed an issue where a custom group wouldn't get marked as a mention if it was not part of the webapp's local state.
 - Fixed several issues with loading of licenses.
 - Fixed an issue with the in-product marketplace theming.

### Known Issues
 - Text overlaps when opening the Playbook RHS panel [MM-54261](https://mattermost.atlassian.net/browse/MM-54261).

## Release 2023-08-09

### Improvements

#### User Interface (UI)
 - The number of channel members is now shown in the **Browse channels** modal.
 - Updated the minimum required Edge version to 112+.
 - An error is now displayed if a post edit history fails to load.
 - Removed the deprecated Insights feature.
 - Prepackaged Calls plugin version 0.18.0.
 - Pre-packaged Playbooks version 1.38.0.

### Bug Fixes
 - Fixed an issue with missing time zone metadata in the Docker container.
 - Fixed the error returned by ``PUT /api/v4/channels/{channelid}`` when the provided name already existed in the team.
 - Fixed the clickable area of post textboxes being too small.
 - Fixed a UI bug in the bot profile popover.
 - Fixed an issue with the ``registerMessageWillBeUpdatedHook`` plugin hook.
 - Fixed an issue where the **Saved Posts** section would not show channel and team names.

### Known Issues
 - Boards public links that follow the URL schema `/boards/public/...` no longer work. They can either be regenerated through the application by going to the board and selecting the **Share** button at the top right, or they can be obtained by replacing the `/boards/public/` part of the URL with `/plugins/focalboard/`.

## Release 2023-08-03

### Bug Fixes
 - Fixed an issue where ``FileExportBackend`` should not use Bifrost.
 - Fixed an issue related to the export configuration settings.

## Release 2023-07-26

### Improvements

#### User Interface (UI)
 - The emoji picker view modal is now displayed on mobile browsers.
 - Prepackaged v1.2.2 of the Apps plugin.
 - Prepackaged Focalboard plugin version 7.11.2.
 - The current user object is now updated more frequently.
 - Updated the user interface so that system admins no longer appear editable by system/user managers in the System Console.

#### Administration
 - Using ``https://github.com/reduxjs/redux-devtools`` in production builds is now allowed.
 - Added a new feature flag, ``DataRetentionConcurrencyEnabled``, to enable/disable concurrency for data retention batch deletion. Also added a new configuration setting  ``DataRetentionSettings.TimeBetweenBatchesMilliseconds`` to control the sleep time between batch deletions.
 - Added a setting under **System Console > Authentication > Guest Access > Show Guest Tag** to remove the **Guest** badges from within the product.
- Added Apache 2.0 license to the public submodule, explicitly signalling to [pkg.go.dev](https://pkg.go.dev/github.com/mattermost/mattermost/server/public@v0.0.6) the license in play for this source code.
 - Added the ability for admins to hide or customize the **Forgot password** link on the login page.

### Bug Fixes
 - Fixed an issue where drafts would persist after sending an ``@here`` mention in the right-hand side.
 - Fixed an issue where the **New messages** toast appeared on channels that were completely visible.
 - Fixed an UI issue related to profile popover on channel member search in the right hand pane.
 - Fixed an issue where the multi-line channel header preview was too narrow on mobile web view.
 - Fixed the render of the **Add Slash Command** page in the backstage area.
 - Fixed an issue where user's timezone affected the date selection in the calendar.

### Known Issues
 - Boards public links that follow the URL schema `/boards/public/...` will not work after this update. They can either be regenerated through the application by going to the board and selecting the **Share** button at the top right, or they can be obtained by replacing the `/boards/public/` part of the URL with `/plugins/focalboard/`.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

## Release 2023-07-20

### Bug Fixes
 - Added support for a new Cloud Export storage and a presigned URL generation.

## Release 2023-07-19

### Bug Fixes
 - Fixed an issue where a "Seeker can't seek" error was displayed when viewing older image attachments.

## Release 2023-07-11

### Highlights

#### Calls
 - Calls v0.17.0 introduces a new ringing feature (Beta): Calls in Direct and Group Message channels will ring and pop up a visual notification for the incoming call. Check out the Calls v0.17.0 release notes and Calls documentation for more details.

### Improvements

#### User Interface (UI)
 - Updated the user interface for the **Browse channels** modal.
 - Increased the nickname field in the user interface from 22 to 64 characters.
 - Updated links to documentation in the **System Console**.
 - Emoji size is now in scale with the text size in the channel header.
 - Prepackaged Focalboard plugin version 7.11.0.
 - Prepackaged Playbooks plugin version 1.37.0.

### Bug Fixes
 - Fixed an issue where scrollbars were not visible enough on the **File Preview** screen.
 - Fixed an issue where SAML Admin Attribute only compared the first value instead of looping through the assertion values array.
 - Fixed an issue where updates to recent emojis were not batched when multiple emojis were posted at once.
 - Reverted a change that could cause the webapp to forget the current user's authentication method.

### Known Issues
 - Boards public links that follow the URL schema `/boards/public/...` will not work after this update. They can either be regenerated through the application by going to the board and selecting the **Share** button at the top right, or they can be obtained by replacing the `/boards/public/` part of the URL with `/plugins/focalboard/`.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

## Release 2023-06-26

### Highlights
 - Insights has been disabled for all new instances and for existing servers that upgrade to v8.0. See more details in [this forum post](https://forum.mattermost.com/t/proposal-to-revise-our-insights-feature-due-to-known-performance-issues/16212) on why Insights has been disabled.
 - Boards is now operating as a plugin and can be enabled or disabled in the **System Console > Plugin settings**. The Boards configuration, ``EnablePublicSharedBoards``, was also removed from the config and the **System Console**.
 - The Channel Export and Apps plugins are now disabled by default.

### Improvements

#### User Interface (UI)
 - Added support to specify different desktop notification sounds per channel.
 - Calls: Ringing sounds can be enabled/disabled and selected in the Desktop Notifications preferences panel.
 - Bumped the pre-packaged version of NPS to 1.3.2.

#### Administration
 - Playbooks is again shipped as a prepackaged plugin, with version 1.36.1.
 - Added a new ``ConfigurationWillBeSaved`` plugin hook which is invoked before the configuration object is committed to the backing store.
 - Admins can now specify index names to ignore while purging indexes from Elasticsearch with the ``ElasticsearchSettings.IgnoredPurgeIndexes`` setting.
 - Added an option to use the German HPNS notification proxy.
 - New flags were added to the database migrate command as following:

    - ``auto-recover``: If the migration plan receives an error during migrations, this command will try to rollback migrations already applied within the plan. This option is not recommended to be added without reviewing migration plan. You can review the plan by combining ``--save-plan`` and ``--dry-run`` flags.
    - ``save-plan``: The plan for the migration will be saved into the file store so that it can be used for reviewing the plan or to be used for downgrading.
    - ``dry-run``: Does not apply the migrations, but it validates how the migration would run with the given conditions.

 - A new database subcommand "downgrade" was added to be able to rollback database migrations. The command either requires an update plan to rollback, or comma separated version numbers.
 - Removed ``/api/v4/users/stats`` network request from ``InviteMembersButton``.

### API Changes
 - Introduce the [public](https://github.com/mattermost/mattermost/tree/master/server/public) submodule, housing the familiar `model` and `plugin` packages, but now discretely versioned from the server. It is no longer necessary to `go get` a particular commit hash, as Go programs and plugins can now opt-in to importing `github.com/mattermost/mattermost-server/server/public` and managing versions idiomatically. While this submodule has not yet shipped a v1 and will introduce breaking changes before stabilizing the API, it remains both forwards and backwards compatible with the Mattermost server itself.
  - In the main `server package`, the Go module path has changed from ``github.com/mattermost/mattermost-server/server/v8`` to ``github.com/mattermost/mattermost/server/v8``. But with the introduction of the `public` submodule, it should no longer be necessary for third-party code to import this `server` package.
 - As part of the `public` submodule above, a ``context.Context`` is now passed to ``model.Client4`` methods.

### Bug Fixes
 - Fixed the **New Messages** line overlapping date lines in the post list.
 - Fixed an issue where post reactions disappeared when the search sidebar was open.
 - Fixed an issue with broken "medical_symbol", "male_sign", and "female_sign" emojis.
 - Fixed a panic where a JSON null value was passed as a channel update.
 - Fixed an issue where the draft counter badge remained in cases where a deleted parent post was removed.
 - Fixed an issue where posts were not fully sanitized for audit output when a link preview was included.
 - Fixed an issue where the footer with **Save/Cancel** buttons did not get anchored properly in the System Console.
 - Fixed an issue where the undo history was erased when links, tables, or code was pasted into the textbox.
 - Fixed an issue where Elasticsearch didn't properly start on startup when enabled. Also added a missing ``IsEnabled`` method to Elasticsearch.
 - Fixed an issue where text couldn't be copied from the post textbox.

### Known Issues
 - Boards public links that follow the URL schema `/boards/public/...` will not work after this update. They can either be regenerated through the application by going to the board and selecting the **Share** button at the top right, or they can be obtained by replacing the `/boards/public/` part of the URL with `/plugins/focalboard/`.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

## Release 2023-06-13

### Compatibility
- Updated Chromium minimum supported version to 112+.

### Improvements

#### User Interface (UI)
 - Reworked some of the components used for showing autocomplete results.

#### Administration
 - Added support for environment variable overrides of ``AdvancedLoggingConfigJSON`` configuration fields.

### Bug Fixes
 - Ensured users mentioned in message attachments are loaded by the web app.
 - Fixed an issue where the reply bar did not get highlighted when a user was mentioned by a reply because of their Reply Notifications setting.
 - Fixed an issue where the total user count was fetched for every client connection. It is only necessary to fetch this once.
 - Fixed an issue where the date separator displayed in the center channel for every post when the pinned posts right-hand side panel was open.

### Known Issues
 - Using the "link" button puts the URL after ``[url]`` instead of replacing ``[url]`` when pasting [MM-53006](https://mattermost.atlassian.net/browse/MM-53006).
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

## Release 2023-05-31

### Improvements

#### User Interface (UI)
 - Added a persistent notification option when sending urgent priority posts.
 - Added an experimental feature to disable re-fetching of channel and channel members on browser focus.
 - Bot users are now hidden in the user selector in apps forms.
 - Removed the fetching of archived channels on page load.
 - The **Channel Type** dropdown within the **Browse Channels** modal can now be focused.
 - Removed in-app help pages that were no longer accessible.
 - Removed system join/leave messages from thread replies and post them instead in the main channel.
 - Added an experimental setting to make the channel autocomplete only appear after typing two characters instead of immediately after the tilde (~).
 - Users with default profile pictures will now regenerate a new picture when their username is changed.
 - Implemented URL auto generation on channel creation for when there's no URL safe characters on its name.
 - Added a new option to auto-follow all threads in the channel **Notification Preference** settings.
 - ``CTRL/CMD + K`` shortcut can now be used to insert link formatting when text is selected.
 - ``pas`` and ``pascal`` code blocks are now higlighted.
 - Language setting in Boards was removed. The main language setting under **Settings -> Display Settings** now covers Boards. Boards previously supported Catalan, Greek, Indonesian, and Occitan, but since these 4 languages were only partially translated (<40%; Boards-only), they have been removed until more areas of Mattermost are translated into these languages.
 - Removed websocket state effects for the collapse/expand state of categories.
 - Pre-packaged Calls version 0.16.1.
 - Pre-packaged Jira plugin version 3.2.5.
 - Pre-packaged GitHub plugin version 2.1.6.
 - Pre-packaged Autolink plugin version 1.4.0.
 - Pre-packaged Welcomebot plugin version 1.3.0.

#### Administration
 - The Go module has been upgraded to v8.0. All packages are now under the new path ``github.com/mattermost-server/server/v8``.
 - Type-generated settings will now be generated (only for future generations) with a URL-safe version of base64 encoding.
 - Mattermost is now resilient against database replica outages and will dynamically choose a replica if it's alive. Also a config parameter ``ReplicaMonitorIntervalSeconds`` was added and the default value is 5. This controls how frequently unhealthy replicas will be monitored for liveness check.
 - Removed ``ExperimentalSettings.PatchPluginsReactDOM``.
 - Removed deprecated ``PermissionUseSlashCommands``.
 - Added support for attachments when importing/exporting Boards.
 - Updated Docker Base Image from Debian to Ubuntu 22.04 LTS.
 - Removed support for PostgreSQL v10. The new minimum PostgreSQL version is now v11.
 - The Mattermost public API for Go is now available as a distinctly versioned package. Instead of pinning a particular commit hash, use idiomatic Go to add this package as a dependency: go get github.com/mattermost/mattermost-server/server/public. This relocated Go API maintains backwards compatibility with Mattermost v7. Furthermore, the existing Go API previously at github.com/mattermost/mattermost-server/v6/model remains forward compatible with Mattermost v8, but may not contain newer features. Plugins do not need to be recompiled, but developers may opt in to using the new package to simplify their build process. The new public package is shipping alongside Mattermost v8 as version 0.5.0 to allow for some additional code refactoring before releasing as v1 later this year.
 - Three configuration fields have been added, ``LogSettings.AdvancedLoggingJSON``, ``ExperimentalAuditSettings.AdvancedLoggingJSON``, and ``NotificationLogSettings.AdvancedLoggingJSON`` which support multi-line JSON, escaped JSON as a string, or a filename that points to a file containing JSON.  The ``AdvancedLoggingConfig`` fields have been deprecated.
 - The Go MySQL driver has changed the ``maxAllowedPacket`` size from 4MiB to 64MiB. This is to make it consistent with the change in the server side default value from MySQL 5.7 to MySQL 8.0. If your ``max_allowed_packet`` setting is not 64MiB, then please update the MySQL config DSN with an additional param of ``maxAllowedPacket`` to match with the server side value. Alternatively, a value of 0 can be set to to automatically fetch the server side value, on every new connection, which has a performance overhead.
 - For servers wanting to allow websockets to connect from other origins, please set the ``ServiceSettings.AllowCorsFrom`` config setting.

### Bug Fixes
 - Fixed the sorting value of categories in ``CreateSidebarCategoryForTeamForUser``.
 - Fixed a potential crash when opening the user profile popover.
 - Fixed permalink and thread reply navigation between teams.
 - Fixed an issue with the installation of pre-packaged plugins that are not in the Marketplace.
 - Fixed an issue caused by a migration in a previous release. The query takes around 11ms on a PostgreSQL 14 DB t3.medium RDS instance. Locks on the preferences table will only be acquired if there are rows to delete, but the time taken is negligible.
 - Fixed an issue where modals did not close when clicking below them on certain screen sizes.
 - Fixed an issue with a few translation labels that couldn't be translated.
 - Fixed an issue where the server log UI for plain text formatting was unexpectedly removed in a previous release.
 - Fixed an issue where combined system messages did not display in chronological order.
 - Fixed an issue where the current user and status were not updated on WebSocket reconnect.
 - Fixed an issue where certain hashtags were not searchable when using database search.

### Known Issues
 - Selecting the **replies** option for a thread doesn't navigate to the thread when Collapsed Reply Threads is enabled. A workaround is to use the reply arrow in the post menu, or to navigate to the **Threads** view when replying to messages [MM-52995](https://mattermost.atlassian.net/browse/MM-52995).
 - Using the "link" button puts the URL after ``[url]`` instead of replacing ``[url]`` when pasting [MM-53006](https://mattermost.atlassian.net/browse/MM-53006).
 - Saved posts in right-hand side show both the team and channel name in the post header [MM-53005](https://mattermost.atlassian.net/browse/MM-53005).
 - In a cluster config save scenario, it is difficult to disinguish between a timeout and a semantic error in the config if a config save in one node gets stuck [MM-52968](https://mattermost.atlassian.net/browse/MM-52968).
 - The URL of the post in a reminder post for direct and group messages have a double slash on mobile [MM-51026](https://mattermost.atlassian.net/browse/MM-51026).
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

## Release 2023-05-01

### Highlights
 - Added an improved Cloud trial experience in preparation for replacing the Cloud Free experience. See more details in these Forum posts:
    - https://forum.mattermost.com/t/cloud-monthly-billing-deprecation/15804
    - https://forum.mattermost.com/t/cloud-free-deprecation/15802

### Improvements

#### User Interface (UI)
 - Replaced the ``compass-components`` icon component with ``compass-icons``.
 - Added “hours ahead” timezone details to the user profile popover.
 - Pre-packaged Calls v0.15.1.

#### Administration
 - Removed the deprecated ``model.CommandArgs.Session``.
 - The database section in the **System Console** now has an additional read-only section which shows the active search backend in use. This can be helpful to confirm which search engine is currently active when there are multiple configured.
 
#### Performance
 - Improved the performance of webapp related to timezone calculations.
 - Improved performance of code used for post list screen reader support.
 
### API Changes
 - An underscore is now used in the timeline API (``event-id`` -> ``event_id``) for consistency with other API arguments.

### Bug Fixes
 - Fixed an issue where a user would still see threads in the threads view of channels they have left. Migration execution time in MySQL: Query OK, 2766769 rows affected (4 min 47.57 sec). Migration execution time in PostgreSQL: Execution time: 58.11 sec, DELETE 2766690.
 - Fixed an issue where clicking on a channel link (for a channel the user was not a part of) caused the webapp to refresh, dropping the user from a call.
 - Fixed an issue with PDF preview rendering for certain Japanese characters.
 - Fixed an issue where the screen reader did not announce the action of copying the link in the invite modal.
 - Fixed an issue with post metadata not generating correctly for images due to missing content-type in response. This would result in certain embedded images not to display on mobile clients.
 - Fixed an issue where edits to messages persisted after canceling.
 - Added a condition for bot tags for webhook posts when a bot account is used for webhooks.

### Known Issues
 - Message Actions … ellipsis menu icon only displays rectangle when clicked on [MM-52444](https://mattermost.atlassian.net/browse/MM-52444).
 - The URL of the post in a reminder post for direct and group messages have a double slash on mobile [MM-51026](https://mattermost.atlassian.net/browse/MM-51026).
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

## Release 2023-04-21

### Improvements

#### User Interface (UI)
 - Enabled Work Templates in the Onboarding checklist and the `+` Menu.
 - Added a **Mattermost Marketplace** option to the bottom of the apps bar. The option is visible when the Marketplace is enabled, and the user has ``SYSCONSOLE_WRITE_PLUGINS`` permissions.
 - Added an **Add channels** button to the bottom of the left-hand sidebar to make the action more obvious for users who want to create or join channels.
 - Removed the Webapp Build Hash from **Main Menu > About Mattermost** since it is now identical to Server Build Hash.

#### Administration
 - The following repositories have been merged into one: ``mattermost-server``, ``mattermost-webapp``, ``focalboard`` and ``mattermost-plugin-playbooks``. Developers should read the updated [Developer Guide](https://developers.mattermost.com/contribute/developer-setup/) for details. Playbooks and Boards are now core parts of the product that cannot be disabled.
 - The file info stats query is now optimized by denormalizing the ``channelID`` column into the table itself. This will speed up the query to get the file count for a channel when selecting the right-hand pane. Migration times:

   - On a MySQL 8.0.31 DB with 1405 rows in FileInfo and 11M posts, it took around 0.3s
   - On a PostgreSQL 12.14 DB with 1731 rows in FileInfo and 11M posts, it took around 0.27s

 - Added the ability to search a partial first name, last name, nickname, or username on the **System Console > Users** page.
 - **Contact Support** now redirects users to Zendesk and pre-fills known information.
 - Added a mechanism for public routes on products and used it to support publicly shared Board links.

### Bug Fixes
 - Fixed a scrolling issue in the purchase modals.
 - Fixed an issue where the **Delete Category Dialog** message was not visible in Boards.
 - Fixed an issue where the experimental Shared Channels feature failed to synchronize if a previously removed table column was still present.
 - Fixed an innocuous panic in Boards Rest API when requesting files and an error other than ``not found`` is encountered.
 - Fixed an issue with the compact message mode.

### Known Issues
 - The URL of the post in a reminder post for direct and group messages have a double slash on mobile [MM-51026](https://mattermost.atlassian.net/browse/MM-51026).
 - A user gets scrolled to the bottom of the post editor after pasting long text in the right-hand pane [MM-51302](https://mattermost.atlassian.net/browse/MM-51302).
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

## Release 2023-03-29

### Improvements

#### Administration
 - The ``ServiceSettings.PostEditTimeLimit`` config setting no longer affects Plugins, Shared Channels, Integration Actions, or Mattermost Products.
 - The app server no longer starts if the telemetry ID in the systems table doesn't exist. Although there is no action required by the administrators, it may be good to be aware of this change.
 - Added additional values to the support packet.

#### Performance
 - Writes to websocket now take 13% less memory and happen 22% faster per message.

### API Changes
 - Added a ``exclude_files_count`` parameter to exclude file counts from channel stats API.

### Bug Fixes
 - Fixed an issue where Shared Channels wasn't properly added to the Professional license.

### Known Issues
 - The URL of the post in a reminder post for Direct and Group Messages have a double slash on mobile [MM-51026](https://mattermost.atlassian.net/browse/MM-51026).
 - A user gets scrolled to the bottom of the post editor after pasting long text in the right-hand side [MM-51302](https://mattermost.atlassian.net/browse/MM-51302).
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

## Release 2023-03-20

### Compatibility
 - Updated Firefox minimum supported version to 102+.
 - Updated Safari minimum supported version to 16.2+.
 - Updated Windows minimum supported version to 10+.
 - Updated Chromium minimum supported version to 110+.
 - Updated Edge minimum supported version to 110+.

### Highlights

#### Annual Cloud Subscriptions
 - On the purchase modal, admins are now able to buy an annual cloud subscription starting from their current user count.
 - The **System Console > Billing & Account > Subscriptions** page now reflects whether the plan is monthly or annual.
 - Cloud Professional monthly will no longer be offered to new customers starting March 20, 2023.
 - Added the option to migrate from a monthly to an annual Cloud Professional plan for existing Cloud Professional monthly customers.

#### Boards
 - Added support for person, multi-person, and date property filters in Boards.
 - Added support for person property groups in Boards.
 - System and team admins are now able to join any board on the team as a board admin via the board URL.
 - Additional Compliance APIs to return the history of boards and blocks, including deleted items (available in Mattermost Enterprise Edition and above).
 - See [the Boards product documentation](https://docs.mattermost.com/boards/groups-filter-sort.html#work-with-groups-filter-and-sort) for more details.

### Improvements

#### User Interface (UI)
 - Pre-packaged Calls v0.14.0.
 - Pre-packaged Playbooks v1.36.0.
 - All post components were removed in favor of a unified approach.
 - App bindings are now refreshed when a App plugin enabled event gets triggered.
 - Improvements were added to the sidebar channel and category menus.
 - Removed right-click hijacking on code blocks in messages.
 - The order of the Leave Channel and Archive Channel settings were updated to match the mobile app.
 - Added the condition to remove unread styling for archived channels and to filter archived channels from local data.
 - Changed the collapsed post fade out effect to be less buggy.
 - Users now have the ability to see the history of edited messages and to restore an old message version with the current version.
 - Improved the user interface of the user profile popover.
 - Added the ability to set a reminder to read a post at a specific time via the “More” menu in posts.
 - Mentions from muted channels are no longer shown or counted on the browser and desktop tabs.
 - Updated **System Console** descriptions for **Environment > Developer configuration** settings in the **System Console** to clarify that changes require a server restart to take effect.
 - The custom user status is now shown in the right-hand side and in the **System Console**.
 - Added the ability to handle multiple emails at once when inviting users.
 - Added accessibility support to the date picker.
 - A feedback survey is displayed during a workspace downgrade process from Cloud Professional to Cloud Free.
 - Migrated the post dot menu to a Material UI (MUI) menu.

#### Administration
 - The invoice is now sent attached when an Admin upgrades to Cloud annual subscription.
 - Removed Boards limits from Cloud Starter subscription.
 - Enabled ``EnableOAuthServiceProvider`` by default.
 - Export files now contain the read and unread status for channels.
 - Added the ``SentAt`` column to ``NotifyAdmin``.
 - Updated ``NotifyAdmin.RequiredFeature`` column type to ``varchar(255)``.
 - Updated ``NotifyAdmin.RequiredPlan`` column type to ``varchar(100)``.
 - [Message Priority & Acknowledgement](https://docs.mattermost.com/configure/site-configuration-settings.html#message-priority) is now enabled by default for all instances.
 - Added the ability to delete a workspace via **System Console > Billing & Account > Subscription**.
 - Added an error message when running an LDAP sync with ``SyncEnabled`` set to ``false``.
 - Added Admin log table filtering and sorting.
 - Go version was bumped to v1.19.
 - GraphQL APIs are now correctly counted when measuring performance telemetry.
 - Boards cards are no longer mentioned as being limited in the **System Console**, the limits usage modal, the downgrade modal, or the left-hand side menu.
 - Removed an unused ``ProductLimits.Integrations``.

#### Performance
 - Reduced the rate that unreads are resynced when the window is focused from 10 seconds to 2 minutes.
 - The center channel is no longer shown as loading when switching teams.
 - Added logging fixes: empty ``short_message`` for Gelf formatter is no longer allowed and ``params.Host`` is now used over ``params.IP`` for syslog config.
 - Added minor performance improvements.

### API Changes
 - Added an ``exclude_files_count`` parameter to exclude file counts from the channel stats API.
 - Added a new API endpoint ``GET api/v4/posts/[POST_ID]/edit_history``.
 - Added a new API endpoint ``DELETE /api/v4/cloud/delete-workspace``.

### Bug Fixes
 - Fixed new teams to use the updated translation for default channels after a config change.
 - Fixed a layout issue in the System Console for smaller-sized tablets.
 - Fixed an issue where a "plugin configured with a nil SecureConfig" warning was logged when starting each plugin.
 - Fixed an issue where portal availability was checked when not on enterprise edition.
 - Fixed a 404 error from requests to ``/api/v4/system/notices/`` on page load.
 - Fixed an issue where OpenID Connect was configurable for Cloud Starter licenses.
 - Fixed an issue where C# syntax highlighting was not working.
 - Fixed an issue where incoming webhooks changed the user's activity while the user was offline/away.
 - Fixed an issue where usernames were not clickable in the right-hand side.
 - Fixed issues with spacing in the channel categories and maintained the same spacing in the left-hand side.
 - Fixed an issue where the setting `Restrict new system and team members to specified email domains` was not visible in Cloud Starter.
 - Fixed disproportionate height issues for tall single images.
 - Fixed an issue where a single WebSocket reconnect could be handled multiple times which would negatively affect performance.
 - Fixed an issue in Top DM Insights, where a deleted participant caused DM Insights to fail.
 - Fixed an issue where Cloud limits would briefly flash in the **System Console** before disappearing.

### Known Issues
 - The URL of the post in a reminder post for Direct and Group Messages have a double slash on mobile [MM-51026](https://mattermost.atlassian.net/browse/MM-51026).
 - A user gets scrolled to the bottom of the post editor after pasting long text in the right-hand side [MM-51302](https://mattermost.atlassian.net/browse/MM-51302).
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

## Release 2023-01-26

### Highlights

#### GitLab Playbooks Integration
 - Using the updated [GitLab integration and task actions in Mattermost Playbooks](https://mattermost.com/marketplace/gitlab-plugin/), teams can automate release management processes to help increase efficiency and reduce errors.

### Improvements

#### User Interface (UI)
 - Insights and drafts are now included when navigating through channels in the channel sidebar using ALT+UP/DOWN arrow keyboard keys.
 - Added an onboarding tour point for Global Drafts.

#### Administration
 - The maximum size of uploaded emojis is reduced to 512KB to reduce image download bandwidth.
 - Users can now monitor the progress of the bulk export job via its metadata field. It is available at ``mmctl export job show <jobID>``.
 - Compliance exports no longer time out when uploading to S3.
 - Users can now supply a certificate authority (CA) file and client certificates for the Elasticsearch client.
 - Grafana metrics are now available for database connection metrics. They are:
    - ``max_open_connections``
    - ``open_connections``
    - ``in_use_connections``
    - ``idle_connections``
    - ``wait_count_total``
    - ``wait_duration_seconds_total``
    - ``max_idle_closed_total``
    - ``max_idle_time_closed_total``
    - ``max_lifetime_closed_total``
 - Boards are served as an in-built product from within Mattermost server instead of a plugin and is now always enabled. While running in product mode, the Boards plugin will remain disabled. 
 - Added a new section in the **System Console** for products. For now, it only contains Boards-specific settings.
 - Made ``registerChannelIntroButtonAction`` plugin API usable by plugins other than Boards.
 - The following new HTTP headers and values are now written on all responses. These default values should make sense in most installations and can be overridden by a reverse proxy or ingress configuration. Note that the empty ``Permissions-Policy`` header does not have any actual effect. Users are recommended to change it to a more restrictive value based on their use case. For more information, see the [W3C Reference](https://www.w3.org/TR/permissions-policy/) or [this article](https://developer.mozilla.org/en-US/docs/Web/HTTP/Permissions_Policy).

	```
	Permissions-Policy: 
	Referrer-Policy: no-referrer
	X-Content-Type-Options: nosniff
	```

### Bug Fixes
 - Fixed an issue with the plugin ``/public`` handling for subpaths.
 - Fixed an issue where selecting **Pinned** on a post in the Threads view would result in the right-hand side being stuck in a loading state.
 - Fixed an issue where the profile popover did not dismiss when opening a modal through a shortcut.
 - Fixed an issue where the **Run Deletion Job Now** button for Data Retention wasn’t disabled when all policies were set to **keep forever**.
 - Fixed an issue that prevented the creation of the initial admin user for new servers.
 - Fixed an issue where making a channel non-read-only required a refresh of the client to see the change.
 - Fixed an issue where Top Channels for Insights didn't show results if the current user's configured timezone wasn't present in MySQL's ``mysql.time_zone_name table``.
 - Fixed an issue where a white screen appeared when a guest was removed from the last channel while on Threads.
 - Fixed an issue where a Direct Message thread did not get disabled when a user was deactivated.
 - Fixed an issue where email notifications for Direct Messages from Playbooks contained broken URLs.

### Known Issues
 - Bot and guest tags truncated on suggestion autocomplete [MM-49973](https://mattermost.atlassian.net/browse/MM-49973).
 - Horizontal scroll displays in the Threads list due to a new tags component [MM-49854](https://mattermost.atlassian.net/browse/MM-49854).
 - Login/create account screen layout breaks when Javascript error banner displays [MM-49587](https://mattermost.atlassian.net/browse/MM-49587).
 - Spacing in the channel switcher is incorrect [MM-49853](https://mattermost.atlassian.net/browse/MM-49853).
 - Spacing issue is displayed between the Global Drafts tour point title and “New” tag [MM-49866](https://mattermost.atlassian.net/browse/MM-49866).
 - The message box flashes controls while typing in the right-hand side [MM-49266](https://mattermost.atlassian.net/browse/MM-49266).
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.
 - Publicly shared boards lead to a "Team not found" error page. See [issue-focalboard-4450](https://github.com/mattermost/focalboard/issues/4450) for more details.
 - If a user is not a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels or remove those channels from the run configuration.

## Release 2023-01-16

### Highlights

#### Calls
 - An important change was made to calls participants limits. The Cloud free plan now supports up to 8 participants per call in group messages, public, or private channels (it was previously direct messages only).
 - [Audio calling and screen sharing](https://docs.mattermost.com/configure/calls-deployment.html) in channels is now generally available to all Mattermost customers.
 - Updated [the keyboard shortcut](https://docs.mattermost.com/channels/keyboard-shortcuts-for-channels.html#calls-shortcuts) to start and join calls.

#### Boards
 - Boards now supports [file attachments](https://docs.mattermost.com/boards/work-with-cards.html#attach-files), including PDFs, images, videos, and any other file types.
 - Users can now [drag and drop boards and categories](https://docs.mattermost.com/boards/navigate-boards.html#manage-boards-on-the-sidebar) on the sidebar and organize them in any order they prefer.
 - The [template picker](https://docs.mattermost.com/boards/work-with-boards.html#choose-a-board-template) has been improved to make it easier for users to find the best template for their project.
 
#### Playbooks
 - Added an option to [run playbooks](https://docs.mattermost.com/playbooks/work-with-playbooks.html#runs-and-channel-behavior) without creating a new channel every time in order to reduce the unnecessary overhead.
 - In addition to the daily digest, users can now also view [a task inbox](https://docs.mattermost.com/playbooks/work-with-tasks.html#task-inbox) from the global header bar while in Playbooks.

#### Message Priority and Acknowledgments
 - Added [message priority labels](https://docs.mattermost.com/channels/message-priority.html) to the Threads view.
 - Added support for users to request acknowledgements on posts and to acknowledge posts (Professional license).

#### Global Drafts
 - Added [a centralized Drafts view](https://docs.mattermost.com/channels/send-messages.html#draft-messages) for draft messages.
 
#### ServiceNow Integration
 - ServiceNow customers can now access and share their ServiceNow data from within Mattermost.
 
#### ServiceNow Virtual Agent Integration
 - The [Mattermost ServiceNow Virtual Agent Integration](https://www.loom.com/share/36f60299c6c349729160d6d8bce75c3c) makes it easy for employees and customers to resolve issues fast.

### Improvements

#### User Interface (UI)
 - Updated prepackaged version of plugins affected by React v17 upgrade.
 - Corrected in-product System Console legacy link to the Cloud Administrator's Guide.
 - Updated prepackaged NPS version to 1.3.1.
 - Updated prepackaged version of Apps plugin to 1.2.0.
 - Added group members count to the group autocomplete.
 - Clicking a group mention now displays group details and membership.
 - Improved the collapsed state of the post formatting toolbar.
 - App Framework channel and user fields now support multi-select properties to allow users to select multiple values in a form.
 - Increased the character count for desktop notifications on Windows to 120 from 50.
 - Prioritized members of recently viewed direct or group messages when adding users to a channel.
 - Updated in-product confirmation modal for ``@here`` mentions to clarify that people & timezone counts don't include the current user.
 - Added support for multiple users and channels to the ``/invite`` slash command.
 - Downgraded French language support to Beta.

#### Administration
 - The export file now contains the server version and a creation timestamp.
 - Plugins with a webapp component may need to be updated to work with Mattermost and the updated React v17 dependency. This is to avoid plugins crashing with an error about ``findDOMNode`` being called on an unmounted component. While our `starter template <https://github.com/mattermost/mattermost-plugin-starter-template>`_ depended on an external version of ``React``, it did not do the same for ``ReactDOM``. Plugins need to update their ``webpack.config.js`` directives to externalize ``ReactDOM``. For reference, see https://github.com/mattermost/mattermost-plugin-playbooks/pull/1489. Server-side only plugins are unaffected. This change can be done for existing plugins any time prior to upgrading Mattermost and is backwards compatible with older versions of Mattermost.
 - Added ``acknowledgements`` field to the post's metadata.
 - Added the ability for customers to view their upcoming invoice on the **System Console > Billing & Account > Subscriptions** page.
 - **Total Activated Users** was changed back to **Total Active Users** on the **System Console > Reporting > Site Statistics** page.
 - The import job now logs the progress of the import.
 - Added ``restore_group`` permission to the mmctl and to the **System Console > Permissions**.
 - Improved bulk export logging.
 - Compliance export job can now cancel the SQL query execution during server shutdown which will allow the job to exit faster.
 - Shared Channels (Experimental) is now available with a Professional license.
 - Removed Cloud Professional file storage limits.
 - The message export compliance job can now survive server restarts. The job will pause and save state when the server is shutting down, and resume from the previously saved state when the server starts back up.
 - Only one instance of the job will be automatically scheduled to run as per the ``MessageExportSettings.DailyRunTime`` config value.
 - Mattermost will throw an error if it detects an Elasticsearch version greater than 7.

### API Changes
 - Added new API endpoint ``GET /api/v4/posts/:post_id/info`` to allow checking if the post that a permalink is pointing to is accessible by joining teams or channels.
 - Added validity checks for role related parameters in ``GET /users``.
 - Added an allowed value ``sort=display_name`` to ``GET /api/v4/users?in_group=<groupid>``.

### Bug Fixes
 - Fixed an issue where batch notifications failed while rendering.
 - Fixed an issue where the unreads button in the channel sidebar was missing alternative text for screen readers.
 - Fixed an issue where there was no feedback that a downgrade was in progress when selecting **Downgrade** under **System Console > Billing & Account > Subscriptions** page.
 - Fixed an issue where attempting to create a team with a duplicate URL displayed the wrong error.
 - Fixed an issue where the custom status modal did not close when navigating to the custom emoji page.
 - Fixed an issue where selections within a code block were not properly copied to clipboard.
 - Fixed an issue where threads with 0 replies would show in all threads.
 - Fixed an issue with the styling of date pickers.
 - Fixed an issue with fetching the latest user's profile picture in Insights.
 - Fixed an issue where ``--center-channel-text`` CSS variable was used instead of ``--center-channel-color``.
 - Fixed an issue where the screen reader timestamp announcement was too long.
 - Fixed an issue where upgrade emails were still sent when downgrading to the Cloud Starter plan.
 - Fixed an issue where profile pictures, usernames, and full names did not update instantly in Insights.
 - Fixed an issue where the metrics server restarted for every config change.
 - Prevented browsers and CDNs from caching remote entrypoint files.
 - Fixed a potential read-after-write issue when uploading data through the resumable uploads API.
 - Fixed the position of the Boards icon in the Apps Bar when Boards is running without a plugin.
 - Fixed ability to create a board when Boards is running without a plugin.
 - Fixed Boards tour tips not appearing when Boards is running without a plugin.
 - Fixed the slash command description help text.
 - Fixed an issue where selecting **Contact Sales** didn't pre-fill the reason for contacting sales.
 - Fixed an issue where the screen readers did not announce the selected state of the sidebar submenu items.
 - Fixed an issue where the metrics server was not prevented from starting while running export commands.
 - Fixed an issue where long group mentions and user mentions didn't wrap properly.
 - Fixed an issue with fetching first/last name for GitLab user using OpenID.
 - Fixed an issue where servers with an encrypted key did not throw an error during startup.
 - Fixed an issue where the **Test Connection** button in **System Console > Environment > Elasticsearch** did not correctly take the right config settings specified in the page. Earlier, it would always take the previously saved config.

### Known Issues
 - The message box flashes controls while typing in the right-hand side [MM-49266](https://mattermost.atlassian.net/browse/MM-49266).
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

## Release 2022-12-20

### Bug Fixes
 - Fixed a deadlock in the export job which caused export jobs to hang forever.
 - Uploading exports to S3 no longer times out.

## Release 2022-12-01

### Improvements

#### User Interface (UI)
 - Removed video check to allow the browser to decide what video types it can play.
 - Added a tooltip to the right-hand side files filter icon.
 - The number of users that can be added to a user group at once was increased to 256.
 - Keyboard and focus handling was improved in profile popovers and @mentions.
 - If a channel has a draft message, the pencil icon is now displayed on the right side of the channel name in the channel sidebar.
 - Pre-packaged Boards v7.5.2.

#### Administration
 - Updated macOS supported version to 11+.
 - **My Insights** and OpenId Connect were added to the Mattermost Free plan.
 - All integration limits and usage limit components were removed.
 - Team scheme APIs are now allowed to be administered with a Professional plan.
 - Added a new menu item on the **System Console > Users** page that re-adds users to all of their default teams and channels associated with the groups they're a member of.
 - Changing the license in a cloud environment will now force an update of the subscription and kick the cache for all cluster members.
 - Added support for product websocket messages on high availability instances.

### API Changes
 - The resumable uploads API was exposed to plugins.
 - Added a new API endpoint ``POST /api/v4/ldap/users/:user_id/group_sync_memberships`` to add (or re-add) users to all of their default teams and channels for all of the groups they're a member of.
 - Added two new URL parameters to the ``GET /api/v4/groups`` endpoint to get the ``ChannelMemberCount`` for a group.
 - Added new API endpoints ``POST /api/v4/users/:user_id/posts/:post_id/ack`` and ``DELETE /api/v4/users/:user_id/posts/:post_id/ack``.

### Bug Fixes
 - Fixed an issue where a blank message was displayed in threads if the leave/join messages were disabled.
 - Fixed an issue where threads would appear duplicated in the Threads view after leaving a channel.
 - Fixed an issue with email search when using a PostgreSQL database.
 - Fixed an issue where message drafts were not saved after pasting them into the post textbox.
 - Fixed an issue where the team name in the channel sidebar header wasn't accessible.
 - Fixed an issue where users were unable to open the user's profile popover from the channel members list in the right panel.
 - Fixed an issue where the OAuth 2.0 deprecation notice was still displayed in the System Console.
 - Fixed an issue where clicking on a reply post time stamp in the global threads inbox opened two right-hand side panels.

### Known Issues
 - Boards linked to a channel you're a member of don't automatically appear on your sidebar unless you're an explicit member of the board. As a workaround, you can access the board from the channel RHS, or by searching for the board via the board switcher (Ctrl/Cmd+K). Alternatively, you can ask the board admin to add you to the board as an explicit member. See the [issue-focalboard-4179](https://github.com/mattermost/focalboard/issues/4179) for more details.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

## Release 2022-11-24

### Improvements

#### User Interface (UI)
 - Changed Cloud defaults for ``MaxUsersPerTeam`` and ``MaxChannelsPerTeam`` to 10000.
 - Added a Monthly versus Annual pricing toggle to the pricing modal.

#### API Changes
 - Added a new API endpoint ``POST /api/v4/groups/:group_id:/restore``.

### Bug Fixes
 - Fixed an issue where special characters weren't allowed in group mention names.
 - Fixed an issue where screen readers didn't read the **Switch Channels** modal header.
 - Fixed an issue in OAuth services where malformed redirect URLs were generated if the registered callback URLs already had static query parameters.
 - Fixed an issue where suggestion dividers were displayed as undefined.

### Known Issues
 - Boards linked to a channel you're a member of doesn't automatically appear on your sidebar unless you're an explicit member of the board. As a workaround, you can access the board from the channel RHS, or by searching for the board via the board switcher (Ctrl/Cmd+K). Alternatively, you can ask the board admin to add you to the board as an explicit member. See the [issue-focalboard-4179](https://github.com/mattermost/focalboard/issues/4179) for more details.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

## Release 2022-11-17

### Highlights

#### Calls
 - Added new message threads with emoji reactions and at-mentions to Calls. After joining a call, expand the widget to the window mode and then select the comment button to access the real-time message thread in the right-hand sidebar.

#### Boards
 - Added additional standard board templates to help users kick-off their next projects.
 - Filters now support all text properties.
 - Added two new tiles for System Console Boards metrics under **System Console > Site Statistics**.

### Improvements

#### User Interface (UI)
 - The **Mark as Unread** option was added to the ``…`` menu for channels in the left-hand side sidebar. Pressing Alt while selecting a channel on the left-hand side now also marks the last post in the channel as unread.
 - Channel members are now able to remove themselves from a channel via the right-hand side channel members list.
 - Downgraded Bulgarian, Persian, and Simplified Chinese language support to Alpha.

#### Administration
 - The **System Console > File Sharing and Download** setting is now unhidden and honored in Cloud.
 - **Total Active Users** was renamed to **Total Activated Users** in **System Console > Reporting > Site Statistics**.
 - Optimized ``ThreadStore.MarkAllAsUnreadByTeam``.
 - SQL migrations for PostgreSQL will now filter by the current schema name when checking for information from the ``information_schema.columns`` view. This does not affect anything because usually there's only one installation in a given database, but this gives flexibility to users to store multiple Mattermost instances under a single database.

### API Changes
 - A new API method ``RegisterCollectionAndTopic(collectionType, topicType string) (error)`` was added to the Plugin API and the following hooks. This API method is in beta, subject to change, and not covered by our backwards compatibility guarantee.
    - ``UserHasPermissionToCollection(c *Context, userID, collectionType, collectionId string, permission *model.Permission) (bool, error)``
    - ``GetAllCollectionIDsForUser(c *Context, userID, collectionType string) ([]string, error)``
    - ``GetAllUserIdsForCollection(c *Context, collectionType, collectionID string) ([]string, error)``
    - ``GetTopicRedirect(c *Context, topicType, topicID string) (string, error)``
    - ``GetCollectionMetadataByIds(c *Context, collectionType string, collectionIds []string) (map[string]model.CollectionMetadata, error)``
    - ``GetTopicMetadataByIds(c *Context, topicType string, topicIds []string) (map[string]*model.TopicMetadata, error)``

### Bug Fixes
 - Fixed an issue where exports did not contain favorited Direct Message channels.
 - Fixed an issue where screen readers did not announce search results on the **Invite members to channel** modal.
 - Fixed an issue where screen readers did not announce the status of the user when hovering over the user status icon.
 - Fixed an issue where users with narrow screens could not see the **Profile Settings** section within the **Settings** modal.
 - Fixed an issue where users were unable to access the **Create an account** option on narrow screens.
 - Fixed an issue where users on desktop were unable to grab the vertical scroll bar without accidently resizing the window.

### Known Issues
 - Boards linked to a channel you're a member of do not automatically appear on your sidebar unless you're an explicit member of the board. As a workaround, you can access the board from the channel RHS or by searching for the board via the board switcher (Ctrl/Cmd+K). Alternatively, you can ask the board Admin to add you to the board as an explicit member. See the [issue-focalboard-4179](https://github.com/mattermost/focalboard/issues/4179) for more details.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

## Release 2022-11-10

### Improvements

#### User Interface (UI)
 - Implemented progressive image loading in the webapp.
 - Renamed "Starter" plan to "Free" plan in product.
 - Updated NPS plugin to version 1.3.0.
 - Removed the user interface for the legacy "Mattermost Cloud" plan (removal effective on November 1st).
 - When the "Custom Brand Text" is left blank with custom branding enabled, the default text is now hidden.

#### Administration
 - If an Admin encounters an invitation error “SMTP is not configured in System Console", a link to the SMTP configuration within the **System Console** is now included in the error message.
 - Crashing jobs now sets the job status to "failed".
 - Added the ability for Cloud customers to submit their feedback for wire transfers to buy a monthly subscription. 
 - Added logic to package product version of Boards with production builds.
 - **System Console** settings that Cloud Admins cannot configure are now hidden.

### Bug Fixes
 - Fixed an issue where custom group actions were appearing in the user interface even when the user didn't have the permissions for them.
 - Fixed issues with branding in email notifications.
 - Fixed an issue where text could be dragged and dropped into input-fields.
 - Fixed an issue where the profile popover failed to dismiss when selecting one of the options from the popover.
 - Fixed an issue where imports containing the team name with the wrong capitalization crashed the import job.
 - Fixed an issue where ``getPostSince`` didn't properly return deleted posts when Collapsed Reply Threads was enabled.
 - Fixed an issue where the screen reader did not announce emojis from the autocomplete list.
 - Fixed an issue where the scroll position in a channel was not maintained when opening reply message permalinks.
 - Fixed an issue where ``OwnerId`` was not set for bots created via ``EnsureBotUser``.

### Known Issues
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

## Release 2022-10-27

### Improvements

#### User Interface (UI)
 - Added the ability to create a new channel along with a new board associated with the created channel.
 - Added the ability for end users to notify their Admins to reactivate a paid plan during the delinquency period by selecting “Notify admin to update billing”.
 - Added markdown formatting for hyperlinks when pasted into the text editor.
 - Email notifications from new messages now also support displaying Slack attachments from the channel post.
 - Updated prepackaged Boards version to v7.4.3.

#### Administration
 - Autocompletion results using Elasticsearch or Bleve will correctly show a user as a channel member in Direct Message and Group Message channels. To force this change to appear, a re-indexing will be necessary.
 
#### API Changes
 - Added new plugin endpoints to ``PermissionService`` interface.

### Bug Fixes
 - Fixed an issue with incorrect mention counts in unread channels.
 - Fixed an issue where the cursor displayed as a pointer instead of as an arrow in embedded Youtube preview images.
 - Fixed an issue where formatting was applied to selected spaces after a word.
 - Fixed an issue where an error with an option to refetch data was not displayed and instead a blank screen was shown when there was a failure fetching Cloud data.
 - Fixed an issue where screen readers did not announce that the channel interface language dropdown in **Settings > Display > Language > Change** is a dropdown.
 - Fixed a bug where role filters weren't being applied for ``GetProfilesInChannel``.
 - Fixed an issue where the guest onboarding checklist contained an “Invite team members” link as a tour point.

### Known Issues
 - Users cannot be added to teams from the **System Console** [MM-47667](https://mattermost.atlassian.net/browse/MM-47667).
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

## Release 2022-10-20

### Compatibility
 - Updated the minimum version of Chrome to v106+ and the minimum version of Edge to 95+.

### Improvements

#### User Interface (UI)
 - A confirmation modal is now displayed before a user marks all threads as read.
 - Added the ability to hide the “required” asterisk in the App Field.
 - Added a fading effect to the Apps Modal body while an Apps Modal is refreshing.

### Bug Fixes
 - Fixed an issue where "Multi-server licensing support (Self-hosted)" feature appeared in the Cloud pricing modal.
 - Fixed an issue where Enterprise features labeled as "Professional Feature" appeared in the **System Console** sidebar.
 - Fixed an issue where the transparency for PNG images in image previews and thumbnails was not preserved.
 - Fixed an issue where no success screen was displayed after upgrading to Cloud Professional.
 - Fixed an issue where screen readers failed to announce “No results found” in the Direct Message modal.
 - Fixed an issue where minipreview data was not generated nor stored for images imported from Slack.
 - Fixed the error message that appears on the **Reset Password** page when inputting a password with fewer than 5 characters.
 - Fixed an issue where ``Get categories`` with the "exclude" option did not return categories for deleted teams a user was no longer a member of.

### Known Issues
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

## Release 2022-10-13

### Highlights

#### Boards
 - Added new board roles, **Commenter** and **Viewer**.
 - Added minimum default board roles to reduce permissioning ambiguity and to prevent security loopholes.
 - Added support for guest accounts.
 - Added the ability to add a team member to a board by selecting their name from an autocomplete list.
 - Added channel notifications for linked boards.
 - Added a new multi-person property to easily set multiple assignees or owners on a card.

#### Calls
 - Added new keyboard shortcuts for Calls.

### Improvements

#### User Interface (UI)
 - Insights now filters out posts made by plugins and OAuth apps.
 - Added a “Last active” status to the profile popover and to the **Direct Message** channel header that indicates when a user was last online. This status only displays for users who are Away, Offline, or DND.
 - Added a shortcut ``Ctrl/Cmd + Shift + U`` to filter channels by unread.
 - The default number of **Direct Message** channels shown in the sidebar is now 40.
 - Updated the company name in the **About Modal** to use the company name of the cloud customer instead of the company name in the cloud license.
 - Downgraded Brazilian Portuguese and Romanian language support to Alpha.
 - Pre-packaged Playbooks v1.32.6.
 
#### Administration
 - After 90 days since the day of missing a payment, Admins will see a modal where they can choose between updating the billing status or staying on the Starter subscription.
 - A banner is now shown to legacy Enterprise Mattermost Cloud Admins informing them that they need to change their workspace soon.

### Bug Fixes
 - Fixed an issue where a randomly generated default message-ID was not added for every outgoing email.
 - Fixed an issue where custom groups could be created with at-mention names that are reserved words (@channel, @here, @all).
 - Fixed an issue where 404 errors were shown when APIv4 had an incorrect content-type header.
 - Fixed an issue where messages from bots and webhooks could not be forwarded.
 - Fixed an issue where the **Integrations limit** warning modal stated "You're getting closer to the 5 enabled integrations limit" even when 5 plugins were already enabled.
 - Fixed an issue where inline images did not appear in the channel header.
 - Fixed an issue with the emoji skin tone selector animation.
 - Fixed an issue where attempting to access a post from the channel **Files** view caused a crash if the Cloud account had reached the message limit.
 - Fixed an issue where the screen reader did not announce a successful login when logging in.
 - Fixed a few broken links at **System Console > User Management > Permission Schemes**.
 - Fixed an issue where users were able to forward messages to users who are deactivated.
 - Fixed an issue where "Threads" were not shown in the unread filter view even if there weren't unread threads.
 - Fixed an issue where the user’s full name was not shown when adding people to a channel via the ``Add people`` modal.
 - Reverted the new search of names in PostgreSQL using full text search introduced in v7.3.0 due to a performance regression.

### Known Issues
 - "More" menu for Pinned posts on the right-hand side is cut-off [MM-46987](https://mattermost.atlassian.net/browse/MM-46987).
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

## Release 2022-10-06

### Improvements

#### User Interface (UI)
 - Added Insights to the channel switcher.
 - Added a button to easily copy the content of text or code files in file previews.
 - The team unread icon for muted channels is now hidden in the sidebar.
 - Updated the designs for the “payment failed” email notifications.

#### Administration
 - A ``batchSize`` option has been added to the ``mattermost export`` CLI command to limit the number of items exported. By default, if it is not included, it exports all posts.
 - Added a credit card update modal that communicates arrears for Admins.

#### API Changes
 - Updated the Files search and GET APIs to filter out files beyond the Cloud plan's configured limit.
 - Added a new response-header ``First-Inaccessible-File-Time`` to the APIs fetching single file info.
 - Added a new query parameter to include deleted posts as long as it's requested by a System Admin in ``/api/v4/channels/{channel_id}/posts``.

### Bug Fixes
 - Fixed an issue with the badge count on the mobile app when a channel/thread was viewed.
 - Fixed an issue where typing ``@`` in the right-hand side rendered a cut-off user suggestion list.
 - Fixed an issue where an error screen was briefly flashed when the first Admin signed up into a new server.
 - Fixed an issue where users were unable to add Japanese comments correctly in the message **Forward** modal.
 - Fixed an issue where unsaved edits to a post were lost when switching channels or threads.
 - Fixed an issue on larger screen sizes where the Insights widgets were pushed to the side when the right-hand side was open.
 - Fixed an issue where the ability to forward messages from public channels wasn't possible when messaging someone directly for the first time.
 - Fixed an issue where custom emojis were sometimes not visible in **Insights > Top Reactions**.
 - Fixed an issue where channels with no posts within a particular timeframe didn't show in **Insights > Least Active Channel**.
 - Fixed an issue where the Channel Info right-hand side shortcut was not disabled in the Insights view.
 - Fixed an issue where formatting keyboard shortcuts were conflicting with existing shortcuts.
 - Fixed an issue where the markdown style for horizontal rules was too thick.
 - Fixed an issue where the emoji reaction overlay blocked part of the message it belonged to in compact view.
 - Fixed an issue where an in-product link was missing from **Integrations > Bot Accounts > Add Bot Account**.

### Known Issues
 - Clicking "Back to team" link from the **System Console** causes a white screen if the righ-hand side was open [MM-47226](https://mattermost.atlassian.net/browse/MM-47226).
 - "More" menu for Pinned posts on the right-hand side is cut-off [MM-46987](https://mattermost.atlassian.net/browse/MM-46987).
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.
 - On the new Boards RHS from the channel Apps Bar, channel members who are not board Admins are incorrectly able to see the **Unlink** board button. However, selecting the button doesn't actually unlink the board unless the user is a board Admin [issue-focalboard-3600](https://github.com/mattermost/focalboard/issues/3600).

## Release 2022-09-15

### Highlights

#### Notify Admin v2
 - Added more context to the “Notify admin” feature to help Admins, such as who asked to upgrade, why they requested the upgrade, and how many people requested it.

### Improvements

#### User Interface (UI)
 - Added a new Top Playbooks Insights widget.
 - Added Calls keyboard shortcuts to the **Keyboard shortcuts** help modal.
 - Pre-packaged Playbooks v1.32.3.
 - Pre-packaged Calls v0.8.1.
 - Downgraded Bulgarian language support to Beta.

#### Administration
 - If ``EnableConfirmNotificationsToChannel`` is disabled, channel member counts by group API are no longer called.
 - Added ``OmitConnection`` to the websocket broadcast parameters.

### Bug Fixes
 - Fixed an issue with a nil point exception error during imports.
 - Fixed an issue where users were unable to download a [Support Packet](/manage/generating-support-packet.html) using the Desktop App.
 - Fixed an issue with the **Message forward** modal where the auto-complete in the comment box moved with the text cursor.
 - Fixed typos in some translations strings that caused some in-product links to be broken.

### Known Issues
 - On larger screens, the Insights widgets are pushed to the side when the right-hand side is open [MM-46886](https://mattermost.atlassian.net/browse/MM-46886).
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.
 - On the new Boards RHS from the channel Apps Bar, channel members who are not board admins are incorrectly able to see the **Unlink** board button. However, selecting the button doesn't actually unlink the board unless the user is a board admin [issue-focalboard-3600](https://github.com/mattermost/focalboard/issues/3600).

## Release 2022-09-08

### Improvements

#### User Interface (UI)
 - Added a red destructive action color to the **Leave Channel** button in the channel header.
 - The "limits reached" modal is now shown to Admins who are doing a fresh login on Cloud instances that hit the message history limit.

### Bug Fixes
 - Fixed an issue where muted channels with an at-mention were displayed under the **Unreads** section of the channel switcher.
 - Fixed an issue where the Collapsed Reply Threads setting was displayed in the **System Console > Experimental Features** section.

### Known Issues
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.
 - The runs and playbooks in the Playbooks left-hand sidebar don't have dot-menus that allow interaction with each item [MM-44752](https://mattermost.atlassian.net/browse/MM-44752).
 - On the new Boards RHS from the channel Apps Bar, channel members who are not board admins are incorrectly able to see the **Unlink** board button. However, selecting the button doesn't actually unlink the board unless the user is a board admin [issue-focalboard-3600](https://github.com/mattermost/focalboard/issues/3600).

## Release 2022-09-01

### Improvements

#### Boards
 - Added indexes to improve performance.
 - Fixed a bug where the **New** button in Kanban columns didn't always work [issue-focalboard-3600](https://github.com/mattermost/focalboard/issues/3600).
 - Fixed issues with 'single-user' mode.

#### User Interface (UI)
 - Added new Insights widgets: Most Active Direct Messages, Least Active Channels, and New Team Members.
 - Introduced a new ``/marketplace command`` that brings up the marketplace modal for the Admin, and changed the ``/help`` command so that it now keeps the user internal to Mattermost.
 - Team unreads are now calculated based on the channel membership and threads only. Team membership is no longer taken into account.
 - For introducing Boards and Playbooks to new users, an “explore other tools in platform” item was added to the end user onboarding checklist.
 
#### API Changes
 - Added new API endpoints:
 
	  - ``GET /api/v4/users/me/top/dms``
	  - ``GET /api/v4/users/me/top/threads``
	  - ``GET /api/v4/teams/:team_id/top/team_members``
	  - ``GET /api/v4/teams/:team_id:/top/threads``

### Bug Fixes
 - Fixed an issue in **System Console > Subscription** where the completed Company Information screen read "Provide your company name and address".
 - Fixed an issue where reading a thread on the mobile app caused a negative mention count to display on the web app.
 - Fixed an issue where the user profile image persisted after user account deletion.

### Known Issues
 - Known issues related to the new Insights widgets, such as that pagination displays for 10 items or less [MM-46595](https://mattermost.atlassian.net/browse/MM-46595).
 - ``/marketplace`` slash command opens the Marketplace with an error displayed [MM-46663](https://mattermost.atlassian.net/browse/MM-46663).
 - Alt+click does not mark a root post as unread on global threads inbox [MM-46683](https://mattermost.atlassian.net/browse/MM-46683).
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.
 - The runs and playbooks in the Playbooks left-hand sidebar don't have dot-menus that allow interaction with each item [MM-44752](https://mattermost.atlassian.net/browse/MM-44752).
 - On the new Boards RHS from the channel Apps Bar, channel members who are not board admins are incorrectly able to see the **Unlink** board button. However, selecting the button doesn't actually unlink the board unless the user is a board admin [issue-focalboard-3600](https://github.com/mattermost/focalboard/issues/3600).

## Release 2022-08-25

### Improvements

#### User Interface (UI)
 - Added the **Save** option to the post menu.
 - Added a banner to communicate delinquency to Cloud Customers.
 - Cloud instances with a file limit (Starter and Professional subscriptions) now display icons notifying that the limit has been hit and that archived files are unavailable until upgrade.

#### Administration
 - Started tracking the join time of team members and added a new API endpoint to retrieve information about team members who have joined during a given time.
 - Introduced an optional ``shouldRender`` function parameter to ``registerchannelHeaderMenuAction`` plugin function. This allows menu items to conditionally render depending on the current state prior to rendering.

### Bug Fixes
 - Fixed an issue where exports generated via mmctl without attachments still included the file properties in the post, so they couldn't be imported.
 - Fixed an issue that caused a crash when unread posts were fetched.

### Known Issues
 - Mentions incorrectly show users as not in a channel [MM-44157](https://mattermost.atlassian.net/browse/MM-44157).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.
 - The runs and playbooks in the Playbooks left-hand sidebar does not have dot-menus that allow interaction with each item [MM-44752](https://mattermost.atlassian.net/browse/MM-44752).
 - On the new Boards RHS from the channel Apps Bar, channel members who are not board admins are incorrectly able to see the **Unlink** board button. However, selecting the button doesn't actually unlink the board unless the user is a board admin [issue-focalboard-3600](https://github.com/mattermost/focalboard/issues/3600).
 - On Boards, selecting the **+ New** button below a column on the Kanban view doesn't always create a new card. As a workaround, set a new default card template by going to the dropdown menu from the blue **New** button on the header of the board, opening the **Options** menu on any card template, and selecting **Set as default** [issue-focalboard-3676](https://github.com/mattermost/focalboard/issues/3676).

## Release 2022-08-18

### Highlights

### Playbooks
 - Navigate between teams in Playbooks with the new team switcher.
 - Manage playbooks and runs in the new left-hand sidebar.
 - View the runs you're participating in or following in the **Runs** sidebar category, and view the playbooks you're a member of in the **Playbooks** sidebar category.
 - Favorite runs or playbooks to prioritize them in the **Favorites** category.
 - Participants now have access to every run feature on the new run details page.
 - In Cloud Professional and Enterprise plans, stakeholders can request status updates from runs.

### Boards
 - All the boards you’re currently a member of from your current team will appear on the sidebar without needing to switch workspaces.
 - Organize boards on the sidebar with custom categories.
 - Press CTRL+K/CMD+K to find additional boards.
 - Navigate between teams in Boards with the new team switcher.
 - Set board and template permissions in the new **Share** setting.
 - Link boards to channels to automatically grant board permissions to channel members.
 - See [the documentation](/welcome/whats-new-in-v72.html) for more details.

### Improvements

#### User Interface (UI)
 - Only the most recent message is now marked as unread when marking a thread as unread from the Threads list.
 - Insights filters now persist instead of being reset to default when switching to channels and returning back to the Insights view.
 - Code blocks now have better support for language filetype extensions and are a smaller bundle size.

### Bug Fixes
 - Fixed an issue where updating a profile image and creating new emojis used multipart uploads when using S3 storage.
 - Fixed an issue where the input legend on the custom group modal was cut off in Chrome.
 - Fixed an issue where the **Disable post formatting** setting was hidden when the advanced text editor was enabled.
 - Fixed an issue where we didn’t fall back to the user's default picture if a profile picture failed to load.
 - Fixed an issue where disabling a WebApp plugin from its configuration page resulted in the radio button reverting to ``true``.

### Known Issues
 - Mentions incorrectly shows users as not in a channel [MM-44157](https://mattermost.atlassian.net/browse/MM-44157).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.
 - The runs and playbooks in the Playbooks left-hand sidebar does not have dot-menus that allow interaction with each item [MM-44752](https://mattermost.atlassian.net/browse/MM-44752).
 - On the new Boards RHS from the channel Apps Bar, channel members who are not admins of the board are incorrectly able to see the "unlink" board button. However, clicking on the button will not actually unlink the board unless the user is a board admin [issue-focalboard-3600](https://github.com/mattermost/focalboard/issues/3600).
 - On Boards, clicking on `+ New` button below a column on the Kanban view does not always create a new card. As a workaround, set a new default card template by going to the dropdown menu from the blue `New` button on the header of the board, then open the Options Menu on any card template and select "Set as default" [issue-focalboard-3676](https://github.com/mattermost/focalboard/issues/3676).

## Release 2022-08-10

### Improvements

#### User Interface (UI)
 - A Desktop App prompt is now always shown on first visit to a Mattermost server from an email notification.

### Bug Fixes
 - Fixed an issue where the cursor sometimes jumped to the center channel textbox when the right-hand side was open.
 - Fixed an issue where closing the right-hand side also closed the edited post in the center channel.
 - Fixed an issue where clicking "Try free now" opened the top 3 enterprise features instead of the "Your trial has started" modal.
 - Fixed an issue where the Threads view displayed as unread even if there were no unread threads.

### Known Issues
 - Mentions incorrectly shows users as not in a channel [MM-44157](https://mattermost.atlassian.net/browse/MM-44157).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-08-03

### Improvements

#### User Interface (UI)
 - Search dropdown options now allow focusing with tab.

#### Administration
 - Plugins can now hide plugin settings based on the server's hosting environment.
 - For Cloud instances, when messages limit is reached, a notification is shown in a channel if the limit is being hit in that channel.
 - Customers who are on a 30-day free trial are now notified 3 days before the trial ends.

### API Changes
 - Added ``first_inaccessible_post_time`` to post API responses.
 - Updated permissions of the ``api/v4/posts/{post_id:[A-Za-z0-9]+}/thread`` endpoint. If compliance is enabled, a user can on longer view threads in a public channel they are not a member of.
 - Adds query parameter 'include_deleted' to endpoint: {{[http://your-mattermost-url.com/api/v4/posts/{post_id}/files/info}}](http://your-mattermost-url.com/api/v4/posts/%7Bpost_id%7D/files/info%7D%7D).

### Bug Fixes
 - Fixed an issue where configuration changes could not be saved in the **System Console** in some cases.
 - Custom Brand Text is now centered and the Site Description configuration now doesn't show a placeholder.
 - Removed a bug where the group permissions had an extra level of nesting in the UI. The permissions checkboxes were also split out into their individual custom group permissions for a greater granularity of control.

### Known Issues
 - Mentions incorrectly shows users as not in a channel [MM-44157](https://mattermost.atlassian.net/browse/MM-44157).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-07-28

### Improvements

#### User Interface (UI)
 - Added the ability to quickly and easily forward posts as permalinks with their respective permalink previews.
 - Added a red destructive action color to ``Archive Channel`` and ``Leave Channel`` menu actions.
 - Plugin activation errors now show in the plugin management page and marketplace.
 - Added accessibility to the emoji picker skin tone selector and reversed the order of the skin tone selections in the emoji selector.

#### Administration
 - A new schema and API for audit logs was defined. Contrary to the previous audit log implementation, all audit log records now have the same schema.
 - Added a new static system-level role called Custom Group Manager. This role has permissions to create, edit, and delete custom user groups via User Groups in the Products menu. It can be used to assign individual users this ability when Custom Groups permissions are removed for All Members via the **System Console** (**System Console > Permissions > Edit Scheme > Custom Groups**).
 - Export file names now contain the ID of the job they were generated by.

### Bug Fixes
 - Fixed an issue where a users were unable to remove themselves from a custom role.
 - Fixed an issue where some images in link previews overflowed.
 - Fixed an issue where accessing the **System Console** and then exiting changed the user's status to "Offline".
 - Fixed an issue where the **New Messages** line sometimes appeared when viewing a channel that was previously read.
 - Fixed an issue with incorrectly formatted text in the **System Console**.

### Known Issues
 - Mentions incorrectly shows users as not in a channel [MM-44157](https://mattermost.atlassian.net/browse/MM-44157).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-07-20

### Improvements

#### User Interface (UI)
- Added **Save** and **Cancel** buttons for post inline editing.
- Enterprise trial details are now displayed for end users in the product switcher menu.
- Updated the Edit Header modal text description to be applicable to channels, direct messages, and group messages.

#### Administration
 - Admins are now able to search for channel IDs via **System Console > User Management > Channels** page.
 - In the **System Console** left-hand side, paid features icons are now displayed on the menu entries to indicate enterprise features.
 - Cloud usage rounding for posts and messages is now precise enough to know when a limit has been reached or exceeded.
 - Added ``webSocketClient`` to ``Pluggable`` and ``PostWillRenderEmbed`` plugin registered components.

### Performance
 - Removed ``getLastPostPerChannel`` selector for improved performance in channel sorting.

### Bug Fixes
 - Fixed an issue where users were able to attempt to edit the channel header of an archived channel on the right-hand side.
 - Decreased flakiness of requesting a Cloud trial.
 - Fixed an issue where the “Your Trial Ended” banner hid the product switcher menu.
 - Fixed an issue where the custom status date format was not set to ``yyyy-MM-dd``.

### Known Issues
 - Custom status does not appear until refresh [MM-45334](https://mattermost.atlassian.net/browse/MM-45334).
 - Mentions incorrectly shows users as not in a channel [MM-44157](https://mattermost.atlassian.net/browse/MM-44157).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-07-13

### Highlights

#### Insights (Beta) (Enterprise and Professional subscriptions)
 - Added workplace insights consisting of usage and behavior data, which helps Enterprises further increase productivity of their employees through Mattermost functionality.

### Improvements

#### User Interface (UI)

 - Added the option to colorize usernames in compact display mode when **Account Settings > Display > Message Display > Compact** is selected.
 - Added a setting to always land users at the newest messages in a channel via **Account settings > Advanced > Scroll position when viewing an unread channel**.
 - Added email headers to notification emails so they can be threaded by email clients.

#### Administration
 - Added the ability to start a trial from the **Invite People** modal.
 - Added the ability for end users to notify Admins to upgrade their workspace.
 - Updated the Posts search and get APIs to filter out posts beyond the Cloud plan's limit.
 - The claim of 10 GB storage per user is no longer shown for grandfathered Cloud plan.

### API Changes
 - Added a new response-header ``Has-Inaccessible-Posts`` for ``getPost`` and ``getPostByIDs`` APIs.

### Bug Fixes
 - Fixed an issue with pasting a GitHub code snippet in the message box when text is selected.
 - Fixed an issue where fully typed emojis that contained a capital letter were not correctly displayed.
 - Fixed an issue where the archived icon did not display correctly in dark themes.
 - Fixed an issue where password requirements were not enforced when Development Mode was enabled.

### Known Issues
 - The Top Boards widget in Insights is slow to load.
 - Custom status does not appear until refresh [MM-45334](https://mattermost.atlassian.net/browse/MM-45334).
 - Mentions incorrectly shows users as not in a channel [MM-44157](https://mattermost.atlassian.net/browse/MM-44157).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-06-29

### Improvements

#### User Interface (UI)
- Added support for syntax highlighting for 1C:Enterprise (BSL) language.

#### Administration
 - The System Console now also searches and returns channels based on the channel ID. A new parameter ``IncludeSearchById`` was added to the channel search endpoint, allowing requests to include searches that match IDs in response.
 - Admins now have the ability to downgrade from Professional to Starter subscription via **System Console > Subscription**.
 - The setting ``ServiceSettings.EnableInsecureOutgoingConnections`` is now applicable to S3 clients as well. If this setting is set, S3 clients will skip the TLS verification.
 - Changed the "Enable Authentication Transfer" to be configurable in Cloud by the System Admin.
 - Search results in PostgreSQL will now respect the ``default_text_search_config`` value instead of being hardcoded to English. System Admins are requested to check this value in case of any discrepancies with what is expected.

### API Changes
 - Added new API endpoints ``GET /api/v4/teams/:team_id/top/threads`` and ``GET /api/v4/users/me/top/threads`` to get top threads for a team and user.

### Bug Fixes
 - Fixed an issue where duplicated emojis sometimes displayed as recently used emojis.
 - Fixed an issue where autocomplete "@" search for names did not normalize UTF-8 characters.
 - Fixed an issue where **Group Messages** with long display names didn't have a tooltip in the left-hand sidebar.
 - Fixed an issue where the file icon was sometimes unresponsive.

### Known Issues
 - Custom status does not appear until refresh [MM-45334](https://mattermost.atlassian.net/browse/MM-45334).
 - Images in OpenGraph previews appear broken [MM-45164](https://mattermost.atlassian.net/browse/MM-45164).
 - Channels sometimes don't get marked as read [MM-44900](https://mattermost.atlassian.net/browse/MM-44900).
 - After server upgrade, usage limit warning may stay in the Main Menu until page refresh [MM-45056](https://mattermost.atlassian.net/browse/MM-45056).
 - Mentions incorrectly shows users as not in a channel [MM-44157](https://mattermost.atlassian.net/browse/MM-44157).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-06-22

### Improvements

#### User Interface (UI)
 - Recent emojis are now sorted based on the number of times an emoji has been used.
 - Improved the link preview user interface.
 - Added new search shortcuts to the **Keyboard Shortcuts** modal. 
    - CMD+F (macOS) and CTRL+F (Windows) for Desktop App
    - CMD+SHIFT+F (macOS) and CTRL+SHIFT+F (Windows) for webapp
 - Added a Trial info panel and end date in the Trial section in **System Console > Subscriptions** page.

### Bug Fixes
 - Fixed an issue where links to internal help pages did not always open in a new browser tab.
 - Fixed an issue that caused the Channel Members right-hand side search input to not search all the members of a channel.
 - Fixed an issue where the feature discovery page still displayed a **Start Trial** button after a trial was completed.
 - Fixed an issue where channel recency sorting was not consistent between mobile and webapp.

### Known Issues
 - Images in OpenGraph previews appear broken [MM-45164](https://mattermost.atlassian.net/browse/MM-45164).
 - Channels sometimes don't get marked as read [MM-44900](https://mattermost.atlassian.net/browse/MM-44900).
 - After server upgrade, usage limit warning may stay in the Main Menu until page refresh [MM-45056](https://mattermost.atlassian.net/browse/MM-45056).
 - Post list doesn't always scroll down to show new messages [MM-44131](https://mattermost.atlassian.net/browse/MM-44131).
 - Mentions incorrectly shows users as not in a channel [MM-44157](https://mattermost.atlassian.net/browse/MM-44157).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-06-15

### Bug Fixes
 - Fixed an issue where multiple backend errors displayed when file storage usage got fetched if no files had been uploaded.

## Release 2022-06-14

### Highlights

#### Free Forever Mattermost Cloud Plan
 - Mattermost Cloud now supports a free forever plan, Cloud Starter, for unlimited users for unlimited time.
 - Access unlimited channels, playbooks, and boards across the Mattermost platform, with unlimited voice calls and screen sharing in Direct Messages.
 - The free plan includes a few workspace limits. [Upgrade to Professional for unlimited access](https://mattermost.com/pricing/):
    - Ability to start a free 30-day Enterprise trial, with access to all features during the trial period.
    - Maximum 1 team. Additional teams can be created during a trial or on a paid plan, which are archived if downgraded back to Starter. History will be preserved, though that archived history can only be accessed if a free user upgrades to a paid subscription plan.
    - 10GB file storage across the platform, with 100MB upload limit. History will be preserved.
    - Unlimited installed apps or plugins, with maximum of 5 enabled at one time. History will be preserved.
    - Access to 10,000 most recent messages. History will be preserved.
    - Access to 500 most recently updated cards.
    - Maximum 5 saved views per board.

#### Calls (Beta)
 - [Native voice calling and screen sharing](/channels/make-calls.html) is now available. This is a Channels-specific integration.

#### Collapsed Reply Threads (General Availability)
 - [Collapsed Reply Threads](/channels/organize-conversations.html) is now generally available and enabled by default for all Cloud users. Administrators may disable it in **System Console > Posts**.

#### Apps Bar (Beta)
 - The channel header is now decluttered to make it more obvious how to access Calls, Playbooks, and Boards when viewing a channel. All channel header icons registered by plugins are moved to the new Apps Bar, while Calls remains in the channel header.

### Improvements

#### User Interface (UI)
 - Applied new designs for the Login screen.
 - Changed some tooltips to appear when focused instead of just on hover.
 - The legacy **Settings > Advanced Settings > Enable Post Formatting** and **Settings > Advanced Settings > Preview Pre-release Features** settings are now deprecated in favor of the the new formatting toolbar.
 - Romanian language support was downgraded to Beta.

#### Administration
 - For all Cloud Workspaces, the default value for Collapsed Reply Threads in **System Console > Posts** is now set to **Always On**. You may choose a different [configuration](/configure/configuration-settings.html#collapsed-reply-threads) as desired.
 - Mattermost Cloud Professional plan now includes a 250GB file storage limit.
 - Default password requirements have been loosened to eight characters and no numeric, casing, or special characters required by default. These requirements can be configured by the System Admin as needed via **System Console > Password**.
 - The Collapsed Reply Threads configuration option was moved in the **System Console** from **Experimental** to **Site Configuration > Posts**.

#### API Changes
 - To allow Admins to retrieve contents of posts whether they are deleted or not, ``include_deleted`` query parameter was introduced to ``GetPost`` endpoint.

#### Performance
 - Reduced the number of calls made to ``viewChannel`` API during regular usage.
 - Added pagination to the ``getPostThread`` API calls.

### Bug Fixes
 - Fixed an issue with uploading SVG files.
 - Fixed an issue where thread posts were not left-aligned in compact message display mode.
 - Fixed an error about a missing column for the Shared Channels experimental feature.
 - Fixed an issue where the channel menu drop-down option "Move to..." was skipped when pressing the TAB keyboard key.
 - Fixed an issue where the bulk import failed due to reply ``CreateAt`` being greater than that of the parent post.
 - Fixed an undefined error when leaving a channel with the Unreads filter enabled.
 - Fixed an issue where clicking on a quick emoji reaction opened the right-hand pane.
 - Fixed an issue where the keyboard focus did not go back to the post textbox after hitting CTRL/CMD+SHIFT+P twice.
 - Fixed an issue where the upload files button was positioned incorrectly.

### Known Issues
 - Channels sometimes don't get marked as read [MM-44900](https://mattermost.atlassian.net/browse/MM-44900).
 - After server upgrade, usage limit warning may stay in the Main Menu until page refresh [MM-45056](https://mattermost.atlassian.net/browse/MM-45056).
 - Back bar is showing over the channel header in the Desktop App [MM-44644](https://mattermost.atlassian.net/browse/MM-44644).
 - Post list doesn't always scroll down to show new messages [MM-44131](https://mattermost.atlassian.net/browse/MM-44131).
 - Mentions incorrectly shows users as not in a channel [MM-44157](https://mattermost.atlassian.net/browse/MM-44157).
 - Channel switcher does not show cross team unreads on refresh [MM-44073](https://mattermost.atlassian.net/browse/MM-44073).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-05-26

### Highlights

#### Advanced Text Editor
 - To make markdown features more accessible, an Advanced Text editor was added with new shortcuts to preview, open the emoji picker, strike out text, add headings, format numbered steps, add bullets, and hide the formatting options.

### Improvements

#### User Interface (UI)
 - To keep users in Mattermost when opening documentation links from the **System Console > Plugin** settings page, all the links now open in another tab.
 - Users are no longer hidden from search results in the "Add members" modal, even if they are already members of the channel.
 - Applied new designs for the Login screen:
     - Default login
     - OAuth options
     - Custom branding
     - MFA token
 - Changed **Actions** post menu hover text to **Message Actions**.
 - Enabled the new onboarding task list for end users.
 - Added pre-packaged Calls v0.5.3.

#### Administration
 - Added ``always-on`` and ``default-on`` settings to **System Console > Experimental Features** for Collapsed Reply Threads. When enabled (default-on), users see Collapsed Reply Threads by default and have the option to disable it in **Settings**. When always on, users are required to use Collapsed Reply Threads and can't disable it. The default state is still ``default-off``.

### Bug Fixes
 - Fixed an issue where the shortcut modal for channel info showed ``ALT`` instead of ``SHIFT`` for Mac.
 - Fixed an issue where the **Help > Report a Problem** link was not hidden when a URL was not set for **System Console > Customization > Report a Problem**.

### Known Issues
 - Known issues related to the Advanced Text editor, including text overlapping the preview button when formatting is collapsed [MM-44457](https://mattermost.atlassian.net/browse/MM-44457).
 - Mentions incorrectly show users as not in a channel [MM-44157](https://mattermost.atlassian.net/browse/MM-44157).
 - Channel switcher does not show cross team unreads on refresh [MM-44073](https://mattermost.atlassian.net/browse/MM-44073).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-05-12

### Improvements

#### User Interface (UI)
 - For toggling the channel information in the right-hand pane, a shortcut CTRL/CMD+ALT+I was added.
 - Added an "Unread Channels" section to the channel switcher and included "Threads" in the results.
 - Added pre-packaged Calls v0.5.1.

#### Administration
 - An email is now sent to Cloud Admins after upgrading their workspace.

#### API Changes
 - Added new API endpoints ``GET /api/v4/teams/:team_id/top/channels`` and ``GET /api/v4/users/me/top/channels``.

#### Bug Fixes
 - Fixed an issue with ADA Accessibility where screen readers did not TAB to or read "This channel has guests" in the channel header bar.
 - Fixed an issue where the at-mention autosuggest of users was no longer grouped by channel membership status.
 - Fixed an issue where the New Messages toast was not fully tappable in the mobile web view.

### Known Issues
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-04-28

### Improvements

#### User Interface (UI)
 - Added the channel members list to the right-hand side Channel Info modal.
 - Added the ability to invite new users to a team from the **Add to channel** modal.
 - To be able to download images and copy public links for images quicker, a copy URL and download buttons were added to image thumbnails.
 - Added the ability to have one-character long channel names.

#### API Changes for Custom Integrations
 - Added a new API endpoint ``POST /api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/set_unread/{post_id}`` to set a thread as unread by post id.
 - Added new API endpoints ``GET /api/v4/teams/:team_id/top/reactions`` and ``GET /api/v4/users/me/top/reactions`` to get top reactions for a team and user.
 - Fixed an issue where the ``UpdateUser`` API endpoint required a ``create_at`` field.

#### Performance
 - Improved the performance of ``GetTeamsUnreadForUser`` when Collapsed Reply Threads is enabled.

#### Bug Fixes
 - Fixed an issue where permalinks to direct and group message posts did not show a preview.
 - Fixed an issue when Collapsed Reply Threads are enabled where marking a root post with a mention as unread displayed both a mention badge and the thread item being bolded.
 - Fixed an issue where the public link to generate the API was getting called even if public links were disabled.
 - Fixed an issue with onboarding page view events.
 - Fixed an issue where the custom emoji **Next** button was out of view when a banner was present.
 - Fixed an issue where it would appear that a user had a negative number of unread threads.
 - Fixed an issue where marking the last post in a thread as unread didn't mark the thread as unread.

### Known Issues
 - The Cloud login screen is not centered [MM-43719](https://mattermost.atlassian.net/browse/MM-43719).
 - Shortcut keys for **Add Reaction** and **Save** are missing in mobile web view [MM-42715](https://mattermost.atlassian.net/browse/MM-42715).
 - Image link previews may show a blank space [MM-40448](https://mattermost.atlassian.net/browse/MM-40448).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-04-13

### Improvements

#### User Interface (UI)
 - Added Files and Pinned Messages to the right-hand side Channel Info.
 - Improved the New Channel modal user interface.

#### Administration
 - To add the ability to toggle sending inactivity email notification to Admins, a configuration setting ``EmailSettings.EnableInactivityEmail`` was added.
 - To filter out inactive users in the System Console, an **Active** filter was added for users and Admins in **System Console > User Management > Users**.

#### Performance
 - Added an index to the ``UserGroups DisplayName`` for improved autosuggest query performance.
 - Improved the performance of permission selectors.

#### Bug Fixes
 - Restored the rendering of main menu items from plugins in non-mobile view.
 - Fixed the overflow of text in **Manage Channel Members** modal title.
 - Fixed an issue where pagination was broken in **System Console > Groups**.
 - Fixed an issue where thread updates did not show correctly after the computer woke up.
 - Fixed an issue where a negative unread count sometimes appeared with Collapsed Reply Threads enabled.
 - Fixed an issue where the modal to create a Custom Group got closed when pressing ENTER.

### Known Issues
 - Shortcut keys for **Add Reaction** and **Save** are missing in mobile web view [MM-42715](https://mattermost.atlassian.net/browse/MM-42715).
 - Image link previews may show a blank space [MM-40448](https://mattermost.atlassian.net/browse/MM-40448).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-03-30

### Improvements

#### User Interface (UI)
 - The **More Actions** menu was restructured to reduce the clutter from Plugins and Apps.
 - Made it easier to copy code blocks by adding a copy button on hover.
 - Added a right-hand side panel to see and interact with channel information.
 - Changed the Mattermost indigo theme to match the dark theme in code blocks.
 - Updated in-product links from legacy domain about.mattermost.com to mattermost.com.
 - Made it easier to copy a message via a new **Copy Text** post menu item.
 - The default for ``ThreadAutoFollow`` has been changed to ``true`` with performance improvements to prepare for the enabling of Collapsed Reply Threads by default in a later release. This does not affect existing configurations where this value is already set to ``false``.

#### Performance
 - Improved performance when clearing notifications with Collapsed Reply Threads enabled.

#### Bug Fixes
 - Fixed an issue where ``ThreadStore.GetThreadsForUser`` did not count correctly when no team ID was specified.
 - Fixed an issue where ``zip`` file creation failed when adding attachments.
 - Fixed an issue where emoji short codes written in Markdown were not added to recently used emojis.
 - Fixed the positioning of SVGs in admin onboarding when the screen doesn't have a previous button.
 - Fixed an issue with the displayed channel name in the channel tutorial tip.
 - Fixed an issue with the clickable area for emojis in the emoji picker to match the interface.
 - Fixed an issue where usernames with periods in the channel switcher input showed Group Messages over matching Direct Messages.
 - Fixed an issue on Collapsed Reply Threads compact message view where clicking on the thread footer avatar did not open the profile modal.

### Known Issues
 - The archived channels search doesn't work as expected [MM-42889](https://mattermost.atlassian.net/browse/MM-42889).
 - Actions menu has inconsistent shading on hover on dark theme [MM-42869](https://mattermost.atlassian.net/browse/MM-42869).
 - Actions menu: "x" and the link inside the tooltip don't work [MM-42769](https://mattermost.atlassian.net/browse/MM-42769).
 - Shortcut keys for **Add Reaction** and **Save** are missing in mobile web view [MM-42715](https://mattermost.atlassian.net/browse/MM-42715).
 - Image link previews may show a blank space [MM-40448](https://mattermost.atlassian.net/browse/MM-40448).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-03-16

### Compatibility
 - Updated Safari recommended minimum version to v14.1+.

### Improvements

#### User Interface (UI)
 - The support email field has moved from **Customization** to **Notifications** in the System Console. Also, a support email is now required when configuring email notifications.
 - The ping endpoint can now receive a device ID, which will report whether the device is able to receive push notifications.
 - Added a loading indicator to the **Threads** global list each time more posts are fetched on infinite scroll.
 - Added search guidance to the **Threads** global list when no more posts can be loaded. This is only shown if you’ve scrolled to load older posts and reach the end of the list.
 - Added support for inline editing of posts.
 - Added accessibility support for custom statuses.
 - Feature flags are now automatically refreshed when the server undergoes a restart.
 - Added nested previews for permalinks.
 - Added a sort order to the category API, and included category data in the websocket category update event.
 - Updated the plugin registry's ``registerCallButtonAction`` method to allow for displaying custom calls buttons in the channel header.
 - Added a debugging setting to turn off client-side plugins for the current user.
 - Tooltip is now only displayed when text is too long in the announcement banner.
 - When restricting direct messages to users on the same team, bots are now excluded from that restriction.

#### Performance
 - Improved performance of Collapsed Reply Threads when backend is enabled but frontend is disabled.
 - Fixed a potential memory leak in the sidebar when using accessibility hotkeys.
 - Virtualized the emoji picker and added other performance improvements to the emoji picker.
 - Improved the performance of storing users in webapp.
 - Fixed a small memory leak in the System Console.

#### Bug Fixes
 - Fixed a scan error on column name "LastRootPostAt": converting NULL to int64.
 - Fixed an issue where selecting a custom status from Recent statuses used the original expiration time.
 - Fixed an issue that caused a gap to appear on the left-hand side in products using the team sidebar.
 - Fixed an issue where moving up or down in the channel switcher didn’t work as expected when Global Threads was in the background.
 - Fixed an issue where pressing ENTER opened the onboarding tutorial tip.
 - Fixed an issue where some permission checkboxes had been moved to different categories in the System Console.
 - Fixed an issue where a blank screen occurred upon leaving a currently open unread channel with the channel unread grouping enabled.
 - Fixed an issue related to disabling and re-enabling Custom Terms of Service.
 - Fixed an issue where channel links on hover overlapped the channels menus.
 - Fixed the positioning of the post menu in mobile web view.
 - Fixed an issue where closing the keyboard shortcut modal by "CTRL/CMD + /" didn’t work.
 - Fixed an issue where the channel keyboard navigation was broken in the Threads view.

### Known Issues
 - In compact message view, the inline post edit help text and emoji picker are not aligned [MM-42402](https://mattermost.atlassian.net/browse/MM-42402).
 - Image link previews may show a blank space [MM-40448](https://mattermost.atlassian.net/browse/MM-40448).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-03-08

### Bug Fixes
 - Fixed an issue where imports failed when the channel display name was empty.

## Release 2022-03-02

### Highlights

#### Custom User Groups
 - Added the APIs and app, store, and authorization methods to create and delete custom groups and to add and remove custom group members.

### Improvements

#### User Interface (UI)
 - Added a new onboarding experience for first System Admin user.
 - Added a dashboard that displays the health of the server.
 - Added new tutorial tours for Channels, Boards and Playbooks to help orient first time users.
 - Added a new plugin registry entry to append menu items to the user guide dropdown.
 - Removed extra telemetry events that were tracked during page loads.
 - Added a feature card slide for Playbooks.
 - Removed ``admin-advisor`` bot's ability to notify admins about missing support email.

#### Performance
 - Improved perceived typing performance by moving heavy code around and effective memoization related to the textbox component.
 - Fixed a memory leak caused by the post textbox.

#### Bug Fixes
 - Fixed an issue with clicking images in the message attachment.
 - Fixed an issue that caused Rudder to create their cookies on the top-level domain when Mattermost was installed on a subdomain.
 - Fixed an issue where **Total Posts** and **Active Users With Posts** graphs did not render in **System Console** > **Team Statistics**.
 - Fixed an issue where telemetry events attempted to get sent even when blocked by an ad blocker.
 - Fixed an issue where the channel switcher stopped showing search results when the first few characters were removed.
 - Fixed an issue where notification sounds didn't trigger on the Desktop App for new accounts.
 - Fixed an issue where users got multiple sounds for a single notification on the Linux Desktop App.
 - Fixed an issue where posting frequent messages to followed threads caused jittery typing.
 - Fixed an issue where the **Add to channel** permission was available in private channels for non-admin users.

### Known Issues
 - Pressing Enter opens the onboarding tutorial tip [MM-42188](https://mattermost.atlassian.net/browse/MM-42188).
 - Some Permission checkboxes have been moved to different categories in the System Console [MM-42020](https://mattermost.atlassian.net/browse/MM-42020).
 - Unread channels names and sidebar item render on top of channel options menu [MM-41952](https://mattermost.atlassian.net/browse/MM-41952).
 - Image link previews may show a blank space [MM-40448](https://mattermost.atlassian.net/browse/MM-40448).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - ``CMD+/`` does not close the shortcuts modal [MM-38971](https://mattermost.atlassian.net/browse/MM-38971).
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-02-16

### Compatibility
 - Updated the recommended minimum supported Firefox version to v91+.

### Improvements

#### User Interface (UI)
 - Users are now able to use the channel switcher to search channels across teams if the users are part of more than one team.
 - Clarified in-product error string "Oops!" as "Unable to continue" for both translators and target audiences in cases where a user doesn't have sufficient permissions to add users or guests.
 - Removed incorrect in-product string text from the **Send full message contents** email notification option description displayed via **System Console > Site Configuration > Notifications**.
 - Added the ability to send an unsanitized user to the source user on ``user_updated`` event.
 - In the compact view, the sender's username is now always shown on posts.
 - Added a **Create board** button to the Channel intro header.
 - The post menu is now only rendered on the root post on hover over.
 - Updated a library used for storing drafts and other data in browser storage.
 - Updated Playbooks version to 1.24.1.
 - Update Boards version to 0.14.0.
 - Enabled performance telemetry tracking for production deployments not running in developer mode. This telemetry tracking is disabled when telemetry is toggled off.

#### Performance
 - Reduced the number of menu components listening for keyboard and mouse events.
 - Re-rendering of ``CustomStatusEmoji`` component is now avoided on post hovering.
 - Removed the collapsed sidebar menu from the DOM on sidebar collapse and expand.
 - Re-rendering of ``TextBox`` links component below the post box while typing is now avoided.

#### Plugins
 - Added an ``OnInstall()`` plugin hook.
 - Added an ``OnSendDailyTelemetry()`` plugin hook.

### Bug Fixes
 - Fixed an issue where the reply notification setting was still in effect even when Collapsed Reply Threads was enabled.
 - Fixed an issue where running ``mmctl config migrate`` reset the configuration settings to defaults if the settings were already in the database.
 - Fixed an issue where the custom status menu option was missing the "x" to clear status.
 - Fixed an issue where the password reset link was valid for 1 hour instead of 24 hours.
 - Fixed an issue where the Mattermost import failed if an export contained a soft-deleted team.
 - Fixed an issue where search results in the right-hand side did not clear when changing screens from file results to any other.

### Known Issues
 - Image link previews may show a blank space [MM-40448](https://mattermost.atlassian.net/browse/MM-40448).
 - Member type is missing from autocomplete [MM-38989](https://mattermost.atlassian.net/browse/MM-38989).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - ``CMD+/`` does not close the shortcuts modal [MM-38971](https://mattermost.atlassian.net/browse/MM-38971).
 - ``CTRL/CMD + SHIFT + A`` shortcut does not open **Settings** [MM-38236](https://mattermost.atlassian.net/browse/MM-38236).
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-02-10

### Bug Fixes
 - Fixed an issue where an emoji import failed when the emoji name conflicted with a system emoji.

## Release 2022-02-03

### Improvements

#### User Interface (UI)
 - Updated prepackaged Boards version to 0.12.1.
 - Added Boards support for Global Retention Policy.
 - Added Collapsed Reply Threads (Beta) tour functionality.
 - Added the current product name information to invoices.
 - Added support for metered billing invoices.
 - Added a keyboard shortcut to open and expand the right-hand pane.

### Bug Fixes
 - Fixed an issue where the user menu header was visible when custom statuses were disabled.
 - Fixed an issue where the markdown **Preview** link was not hidden in read-only channels.
 - Fixed an issue where Cloud admins were unable to download an invoice via the Desktop App.
 - Fixed an issue that caused a gap to appear on the left-hand side in products using the team sidebar.
 - Fixed an issue with Collapsed Reply Threads (Beta) where clearing a deleted root post left the right-hand side blank.
 - Fixed an issue where the **Add** channel member button text was cut off in Safari.

### Known Issues
 - Announcement banner can cause the top team to be partially obstructed [MM-40887](https://mattermost.atlassian.net/browse/MM-40887).
 - Image link previews may show a blank space [MM-40448](https://mattermost.atlassian.net/browse/MM-40448).
 - "New Replies" banner is displayed in the right-hand side for a thread that is entirely visible [MM-40317](https://mattermost.atlassian.net/browse/MM-40317).
 - Member type is missing from autocomplete [MM-38989](https://mattermost.atlassian.net/browse/MM-38989).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - ``CMD+/`` does not close the shortcuts modal [MM-38971](https://mattermost.atlassian.net/browse/MM-38971).
 - ``CTRL/CMD + SHIFT + A`` shortcut does not open **Settings** [MM-38236](https://mattermost.atlassian.net/browse/MM-38236).
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-01-27

### Bug Fixes
 - Fixed an issue where replying to posts, pinning posts, and editing posts did not work.

## Release 2022-01-25

### Improvements

#### User Interface (UI)
 - Invite to team modal now auto-focuses its email search input.
 - Updated "Terms of Service" terminology to "Terms of Use" product-wide.
 - Updated **Account Settings** terminology to **Settings**.
 - Added Accept-Language header to generate link previews in the default Server language.
 - The **Invite Members** button is now hidden when the Direct Message category is collapsed.

#### Administration
 - Improved plugins performance by re-initializing only upon plugin configuration changes.

### Bug Fixes
 - Fixed an issue where the user avatar wasn’t removed from the participants list after the user’s only post in a thread was deleted.
 - Fixed an issue with the exit animation on the invitation modal.
 - Fixed an issue where the file preview modal info bar showed the channel id instead of the channel name for Direct Messages.
 - Fixed an issue with post hover menu overlap.
 - Changed Client4 to properly set Content-Type as application/json on API calls.
 - Fixed an issue to add a loader when fetching data from the backend in the channel switcher if there are no results matching local data.
 - Fixed an issue where the **Get a Public Link** button in the file preview modal was hidden if the image was an external link.
 - Fixed an issue where the click effect on **Copy** invite link button was incorrect.
 - Reinstalling a previously-enabled plugin now correctly reports enabled status as false.
 - Fixed an issue where the Ctrl/Cmd+Shift+A hotkey to open **Settings** didn't work in desktop view.
 - Fixed an issue where the "Leave Channel" button didn't work from the channel sidebar 3-dot menu when clicking on it a second time.

### Known Issues
 - Announcement banner can cause the top team to be partially obstructed [MM-40887](https://mattermost.atlassian.net/browse/MM-40887).
 - Some plugin full screen modals are broken [MM-40625](https://mattermost.atlassian.net/browse/MM-40625).
 - Image link previews may show a blank space [MM-40448](https://mattermost.atlassian.net/browse/MM-40448).
 - "New Replies" banner is displayed in the right-hand side for a thread that is entirely visible [MM-40317](https://mattermost.atlassian.net/browse/MM-40317).
 - Member type is missing from autocomplete [MM-38989](https://mattermost.atlassian.net/browse/MM-38989).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - ``CMD+/`` does not close the shortcuts modal [MM-38971](https://mattermost.atlassian.net/browse/MM-38971).
 - ``CTRL/CMD + SHIFT + A`` shortcut does not open **Settings** [MM-38236](https://mattermost.atlassian.net/browse/MM-38236).
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2022-01-11

### Bug Fixes
 - Fixed an issue where the license expired announcement banner was unexpectedly displaying for Cloud workspaces.

## Release 2021-12-08

### Improvements

#### User Interface (UI)
 - Added thread replies to search results when Collapsed Reply Threads is enabled.
 - Updated "Terms of Service" terminology to "Terms of Use" product-wide.

#### Performance
 - Added a general performance fix for loading the web application and typing.
 - Improved performance while typing by moving some autocomplete layout calculations.
 - Improved performance by reducing DOM usage during render.
 - Removed real-time updates of a couple of features to prevent overloading servers on user updates. The "This channel has guests" indicator and the number of timezones displayed when notifying members of a group will only be updated on channel change now.

### Bug Fixes
 - Fixed slow channel loading for instances with website link previews enabled.
 - Fixed an issue where the webapp crashed sometimes when selecting an image file from "Recent files".
 - Fixed an issue where the status menu unexpectedly closed when selecting the "Disable Notifications Until" header.

### Known Issues
 - Image link previews may show a blank space [MM-40448](https://mattermost.atlassian.net/browse/MM-40448).
 - Spacing of ``from:`` autocomplete items are off [MM-40447](https://mattermost.atlassian.net/browse/MM-40447).
 - "New Replies" banner is displayed in the right-hand side for a thread that is entirely visible [MM-40317](https://mattermost.atlassian.net/browse/MM-40317).
 - Member type is missing from autocomplete [MM-38989](https://mattermost.atlassian.net/browse/MM-38989).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - ``CMD+/`` does not close the shortcuts modal [MM-38971](https://mattermost.atlassian.net/browse/MM-38971).
 - ``CTRL/CMD + SHIFT + A`` shortcut does not open **Settings** [MM-38236](https://mattermost.atlassian.net/browse/MM-38236).
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-12-01

### Improvements

#### User Interface (UI)
 - Clarified Latex Rendering config setting descriptions and fixed a broken product documentation link.
 - Updated the "One-click reactions on messages" user setting to "Quick reactions on messages".
 - Added tab focus support to the global header and user avatars.
 - Added a new **Replies** banner to the right-hand side Thread viewer.

### Bug Fixes
 - Fixed an issue where Mattermost Cloud installations were panicing after the November 23, 2021 release.
 - Fixed an issue where the default log rotation file size was mistakenly set to 10GB, and is now reverted back to 100MB.
 - Fixed an issue where OpenID redirects didn't work when hosting Mattermost on a subdirectory.
 - Fixed an issue where using CMD/CTRL + SHIFT + F in global threads did not add a search term automatically.
 - Fixed the alignment of the “X” button in the “message deleted” System message.
 - Fixed an issue where the long post "Show More/Less" background was broken in the Thread viewer.

### Known Issues
 - Member type is missing from autocomplete [MM-38989](https://mattermost.atlassian.net/browse/MM-38989).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - ``CMD+/`` does not close the shortcuts modal [MM-38971](https://mattermost.atlassian.net/browse/MM-38971).
 - ``CTRL/CMD + SHIFT + A`` shortcut does not open **Settings** [MM-38236](https://mattermost.atlassian.net/browse/MM-38236).
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-11-23

### Improvements

#### User Interface (UI)
 - Updated **Account Settings** terminology to **Profile**.
 - Updated instances of **switch** to **navigate**.
 - Updated in-product text terminology to shift from **comments** to **conversations** and **replies**.
 - Do Not Disturb option for **Tomorrow** now displays the expiry time.
 - Recent emojis now get updated based on the default selected skin tone.
 - Updated **SingleImageView** to hide the image name for attached images until the image is collapsed.
 - Moved the expand arrow to the left of image name. 
 - The image expansion icon now appears on image hover.

### Bug Fixes
 - Fixed an issue where emoji reaction buttons on posts did not respect user permissions.
 - Fixed an issue where unchecking the automatic timezone changed the timezone in the selector.
 - Fixed an issue where emoji names were being truncated too soon in the emoji picker.
 - Fixed an issue where the thread footer did not allow the user to follow a Thread.
 - Fixed an issue where the app crashed when switching to Threads view after leaving a channel.
 - Fixed an issue where push notifications did not clear from the lock screen or the notification center with Collapsed Reply Threads enabled.
 - Fixed an issue where Direct Message notifications were missing the sender name with Collapsed Reply Threads enabled.
 - Fixed an issue where keyboard shortcuts were not working with Global Threads.

### Known Issues
 - Member type is missing from autocomplete [MM-38989](https://mattermost.atlassian.net/browse/MM-38989).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - ``CMD+/`` does not close the shortcuts modal [MM-38971](https://mattermost.atlassian.net/browse/MM-38971).
 - ``Ctrl/Cmd+Shift+A`` shortcut does not open **Account Settings** [MM-38236](https://mattermost.atlassian.net/browse/MM-38236).
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-11-11

### Bug Fixes
 - Fixed an issue with panics in a ``patchChannel`` function [MM-40014](https://mattermost.atlassian.net/browse/MM-40014).

## Release 2021-11-10

### Improvements

#### User Interface (UI)
 - Added online status to profile images on user autocomplete.
 - App Commands now have an option to open them as modals.
 - Added support for navigating through Collapsed Reply Threads via arrow keys.
 - Added support for focusing the input box in Collapsed Reply Threads while typing.
 - Added support for blurring the input box in Collapsed Reply Threads on pressing Escape.
 - Adjusted the channel override desktop notification preference for Threads.
 - Added a **Click to open thread** setting for all users.
 - User interface is now improved when no text is set for a custom status.

### Bug Fixes
 - Fixed an issue where API allowed changing the name of the Town Square channel.
 - Fixed an issue where errors were logged if a user disabled notifications.
 - Fixed an issue where a channel was not immediately removed from the sidebar when the current user was removed from it.

### Known Issues
 - Member type is missing from autocomplete [MM-38989](https://mattermost.atlassian.net/browse/MM-38989).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - ``CMD+/`` does not close the shortcuts modal [MM-38971](https://mattermost.atlassian.net/browse/MM-38971).
 - ``Ctrl/Cmd+Shift+A`` shortcut does not open **Account Settings** [MM-38236](https://mattermost.atlassian.net/browse/MM-38236).
 - Close button on the Invite People page is incorrectly themed [MM-37852](https://mattermost.atlassian.net/browse/MM-37852).
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-10-27

### Highlights

#### Timed Do Not Disturb
 - Added the ability to disable all notifications for a specified period of time to avoid distractions, without losing important messages when you're back.

### Improvements

#### User Interface (UI)
 - Recent mentions and saved posts now show across all teams.
 - Added ``@here`` mention to the ``EnableConfirmNotificationsToChannel`` config setting to show a warning modal when over 5 members might be alerted with ``@here``.
 - Added one-click reactions for posts. Also, the three most recently used emojis will display when the mouse is hovered on a post. 
 - Added support for selecting names and aliases in the emoji picker.
 - The updated "Tips & Next Steps" screen is now shown to all System Admins.
 - Updated in-product text for the invitation modal for clarity.
 - Updated the file attachment limits and sizes within in-product help documentation.

#### Performance
 - Reduced storage-related slow-downs on page load.

### Bug Fixes
 - Fixed a broken link to the **Custom Emoji** page on servers with a subpath configured.
 - Fixed an issue where a "No results found" error string was displayed in the **Direct Messages** modal.
 - Fixed an issue where the caret was placed in the middle of the emojis when picking two emojis from the emoji picker.
 - Fixed an issue where **System Console > Channels > Channel Management** displayed an option to toggle group management in Team Edition, Starter, and Professional.
 - Fixed an issue where the channel switcher was missing the "(You)" indicator on the user's own Direct Message channel.
 - Fixed an issue where the clock format set by the user was not respected on the edit indicator popover.
 - Replaced Metropolis font files with a new set to correct a kerning issue.
 - Fixed an issue where deep links opened on mobile displayed an incorrect text directing users to open the Desktop app.
 - Addressed various user interface style bugs from the Oct 13 release.
 - Fixed emails templates for clients that do not support the `<style>` tag.
 - Fixed an issue where the scrollbar was hardly visible with Denim & Sapphire Themes.
 - Fixed various bugs for the Collapsed Reply Threads (Beta) feature, including:
    - Fixed an issue where the recent sidebar sorting option didn't only consider parent posts.
    - Fixed an issue where a badge was displayed on a thread list when the thread was started by another user in a Direct Message.
    - Fixed an issue where the user avatar was displayed in the participants list after their post was deleted and if they had no other posts in the thread.
    - Fixed an issue where the ephemeral message was not displyaed as the centre post.
    - Fixed an issue with dragging and dropping files on a thread while on a Threads panel.
    - Fixed an issue where permalinks were not highlighting a post on a thread that was already open on the right-hand side.
    - Fixed an issue with missing threads in the Thread list.

### Known Issues
 - Member type is missing from autocomplete [MM-38989](https://mattermost.atlassian.net/browse/MM-38989).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - ``CMD+/`` does not close the shortcuts modal [MM-38971](https://mattermost.atlassian.net/browse/MM-38971).
 - Deep link opened on mobile shows incorrect text directing the user to open the Desktop app [MM-38913](https://mattermost.atlassian.net/browse/MM-38913).
 - LDAP Sync job inserting invalid NULL unicode character into job's Data column [MM-38711](https://mattermost.atlassian.net/browse/MM-38711).
 - ``Ctrl/Cmd+Shift+A`` shortcut does not open **Account Settings** [MM-38236](https://mattermost.atlassian.net/browse/MM-38236).
 - Close button on the Invite People page is incorrectly themed [MM-37852](https://mattermost.atlassian.net/browse/MM-37852).
 - Indigo theme glitch may occur when returning from Playbooks [MM-38910](https://mattermost.atlassian.net/browse/MM-38910).
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-10-13

### Highlights

#### Multi-Product Platform
 - Mattermost now ships as one platform with three products - Channels, Playbooks, and Boards.

#### Global Product Launcher
 - Added a global header for product navigation for Channels, Playbooks, and Boards. This is disabled on the mobile web view and mobile apps.

#### Packaging Changes
 - Introducing [updated packaging](https://mattermost.com/pricing) with new Starter, Professional and Enterprise plans to better serve our customers.
 - Existing paying Cloud Professional customers will automatically be upgraded to Cloud Enterprise with no change to pricing or feature set for the next 12 months. More information will be shared to the workspace owner's email address shortly after the release.
 - Existing free Cloud customers will be asked to enter their credit card by January 15th, 2022 to continue using Mattermost Cloud. More information will be shared to the workspace owner's email address shortly after the release.

#### Beta features Promoted to General Availability
   - Archived channels
   - Compliance exports
   - Custom terms of service
   - Guest accounts
   - System roles
   - Plugins

### Improvements

#### User Interface (UI)
 - Added a query param to translate in-product help pages when opened from the Desktop App.
 - Added rendering for posts containing markdown in email notifications.
 - Added support for inline Latex rendering.
 - Added the **Move to...** option menu item to the channel header dropdown.
 - Added keyboard shortcuts to tooltips. Use shortcut key component for displaying keys.
 - Changed the user interface of the edit-indicator of posts and moved it inline.
 - Added support for Global threads infinite scroll.

#### Integrations
 - Added support for multi-select on Apps slash commands.
 - App commands now make a distinction between the central channel and the right-hand side channel.
 - App bindings now recognize the post menu options for each channel they live in.
 - Added new ``registerMessageWillBeUpdatedHook(newPost, oldPost)`` client-side plugin hook to intercept edited messages.

#### Performance
 - Added performance improvements for draft storage with multiple tabs open.
 - Improved performance of draft loading.
 - Slightly improved performance around rendering of system messages.

#### Administration
 - Bulk imports with attached files now log and continue when a file fails to upload instead of halting.
 - ``get flagged posts`` endpoint will now return only flagged posts for channels the user is member of.
 - Minimum supported browser versions changes:
   - Chrome updated from ``61+`` to ``89+``.
   - Firefox updated from ``60+`` to ``78+``.
   - MacOS updated from ``10.9+`` to ``10.14+``.

### Bug Fixes
 - Fixed an issue where creating a bot with an invalid username returned an "invalid email" error.
 - Fixed an issue where using ``/code`` did not render initial whitespace characters.
 - Fixed an issue where **Try Enterprise for Free** option was missing spacing in mobile webview.

### Known Issues
 - Clicking on "..." post menu on a System message crashes the webapp [MM-39116](https://mattermost.atlassian.net/browse/MM-39116).
 - Desktop notifications don't work intermittently [MM-39052](https://mattermost.atlassian.net/browse/MM-39052).
 - Member type is missing from autocomplete [MM-38989](https://mattermost.atlassian.net/browse/MM-38989).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - ``CMD+/`` does not close shortcuts modal [MM-38971](https://mattermost.atlassian.net/browse/MM-38971).
 - Deep link opened on mobile shows incorrect text directing the opening to the Desktop app [MM-38913](https://mattermost.atlassian.net/browse/MM-38913).
 - Channel switcher is missing "(You)" indicator on your own Direct Message channel [MM-38798](https://mattermost.atlassian.net/browse/MM-38798).
 - LDAP Sync job inserting invalid NULL unicode character into job's Data column [MM-38711](https://mattermost.atlassian.net/browse/MM-38711).
 - ``Ctrl/Cmd+Shift+A`` shortcut does not open **Account Settings** [MM-38236](https://mattermost.atlassian.net/browse/MM-38236).
 - Close button on invite people page is incorrectly themed [MM-37852](https://mattermost.atlassian.net/browse/MM-37852).
 - Indigo theme glitch may occur when returning from Playbooks [MM-38910](https://mattermost.atlassian.net/browse/MM-38910).
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-09-29

### Highlights

#### Permalink Previews
 - Added support for permalink previews for posts in Mattermost. Previews are generated to minimize context switching when sharing message links in Channels.

#### Tutorial Updates
 - Added a tip to the **Getting Started** page for downloading Desktop Apps.
 - Updated tutorial icons and changed text content in tutorial tips.

#### Branding Changes
 - Added a new default brand theme named "Denim".
 - The existing theme names and colors, including "Mattermost", "Organization", "Mattermost Dark", and "Windows Dark" have been updated to the new "Denim", "Sapphire", "Indigo", & "Onyx" theme names and colours, respectively. Anyone using the existing themes will see slightly modified theme colors after their server or workspace is upgraded. The theme variables for the existing "Mattermost", "Organization", "Mattermost Dark", and "Windows Dark" themes will still be accessible in [our documentation](/messaging/customizing-theme-colors.html#custom-theme-examples), so a custom theme can be created with these theme variables if desired. Custom themes are unaffected by this change.
 - Added a new light theme named "Quartz" to the default available list of themes.
 - Updated email templates to the new branding.

### Improvements

#### User Interface (UI)
 - Added “Invite People” to the main "+" button below the hamburger menu.
 - The whole category bounds are now highlighted while holding a channel above a category name on the left-hand side.
 - Updated **Account Settings > Display > Timezone** to be more user friendly.
 - New theme agnostic file preview modal takes up the full screen. The file preview now has information about the user, channel, and the file, and moves away from text-based buttons to icon-based buttons.
 - Increased the limit of uploaded file attachments per post from 5 to 10.
 - Added desktop notifications for followed Threads.
 - Hungarian and English-Australian are now official languages.
 - Added a query param to translate in-product help pages when opened from the Desktop App.
 - Added rendering for posts containing markdown in email notifications.

#### Performance
 - Improved typing performance when the emoji autocomplete is open.

#### Integrations
 - Dropped support for left-hand side-specific bot icons.
 - Added a "rest field" to the App command parser.
 - Added support for multiselect on Apps slash commands.
 - App commands now make a distinction between the central channel and the right-hand side channel.
 - Removed a deprecated "Backend" field from the plugin manifest.
 - Converted the "Executables" field in the plugin manifest to a map.
 - Added support for React components in channel header tooltips registered by plugins.

#### Administration
 - Upgraded Go to v1.16.7.
 - Removed the Slack importer from the user interface.
 - Migrated the extraction command to mmctl.
 - Dropped support for Elasticsearch versions earlier than v7.
 - Removed the convert channel endpoint to use ``/channels/{channel_id}/privacy`` instead.
 - Removed deprecated ``Posts.ParentId`` in favor of the semantically equivalent ``Posts.RootId``. Also removed ``CommandWebhook.ParentId`` and ``CompliancePost.ParentId`` for the same reason.
 - Bulk imports with attached files now log and continue when a file fails to upload instead of halting.
 - Updated Bleve to v2 to use the scorch index type.

### Bug Fixes
 - Fixed an issue where floating timestamps appeared incorrectly on the right-hand side with Collapsed Reply Threads (Beta) enabled.
 - Fixed an issue where pinned and saved posts were no longer highlighted.
 - Disabled admin support email status check job on server startup.
 - Fixed an issue on joining a missing channel as a System Admin.
 - Fixed an issue where creating a bot with invalid username returned an "invalid email" error.
 - Fixed an error with app locations and binding filtering.
 - Fixed an issue where /code was not rendering initial whitespace characters.
 - Fixed import process for imports with attachments.

### Known Issues
 - To exit Playbooks, uers can press the **Back** button or use a keyboard shortcut to go back.
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - Sometimes an "Unable to get role" error appears when changing a channel member role in **System Console > User Management > Channels**.
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-08-12

### Highlights

#### Beta features promoted from Beta to General Availability
   - Archived channels
   - Compliance exports
   - Custom terms of service
   - Guest Accounts
   - System Roles
   - Plugins

#### Focalboard
 - Added support for Focalboard for Mattermost Cloud.

### Improvements

#### User Interface (UI)
 - Changed H1-H3 heading font from Open Sans to Metropolis.

#### Administration
 - Added ``playbooks`` and ``boards`` to restricted team URLs list.
 - Mattermost is now built with Go v1.16.6.
 - Added the ability for Team Edition to edit role permissions.
 - Removed hard-coded override of ``TeamSettings.MaxNotificationsPerChannel`` on unlicensed servers (e.g. Team Edition).
 - Exported ``ChannelInviteModal`` and ``ChannelMembersModal`` components for plugins.

### Bug Fixes
 - Fixed an issue where GitLab ``ButtonText`` and ``ButtonColor`` settings were not reflected on the login screen.
 - Fixed an issue where Mattermost panicked on ``docx`` files uploaded with ``.doc`` extension.
 - Prevented users from having the unreads filter enabled when the button to toggle it is not shown.
 - Fixed an issue where the timestamp on deleted messages was not correctly positioned.
 - Fixed an issue where a space was missing between sentences in the banner to refresh app.
 - Fixed an issue where Mattermost's shortcut key CTRL+SHIFT+A to open **Account Settings** clashed with Chrome's CTRL+SHIFT+A that opens a "Search Tabs" pop-up.
 - Fixed an issue with Collapsed Reply Threads (Beta) where replying to a thread caused users to re-follow the previously unfollowed thread.

### Known Issues
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - Sometimes an "Unable to get role" error appears when changing a channel member role in **System Console > User Management > Channels**.
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-07-29

### Improvements

#### User Interface (UI)
 - Improved typing performance in affected environments by reducing the frequency in which drafts are saved.
 - Improved user and channel selector for app commands.
 - Enabled the **Set Status** button if the custom status hasn't changed from currently set status.
 - Added plugin API methods for user access tokens and OAuth apps.
 - Improved default rendering of images inserted via the GIF picker.
 - Small text changes were added to Direct and Group Message menus: 'Mute channel' and 'Edit Channel Header' now reads 'Mute Conversation' and 'Edit Conversation Header'.
 - Added support for ``react-intl`` and ``<Timestamp/>`` usage in plugins.

#### Administration
 - The “config watcher” (the mechanism that automatically reloads the config.json file) has been deprecated in favor of an mmctl command that will need to be run to apply configuration changes after they are made. This change improves configuration performance and robustness.
 - Fixed some of the incorrect mention counts and unreads around threads and channels since the introduction of Collapsed Reply Threads (Beta). This fix is done through a SQL migration, and it may take several minutes to complete for large databases.
 - Upgraded the builder image to use Go v1.16.
 - Added a new feature to archive and unarchive teams through **System Console** > **Teams**.

### Bug Fixes
 - Fixed an issue where the "Find channel" channel switcher text overflowed beyond the button for some languages.
 - Fixed an issue where inter-plugin requests without a body didn't work.
 - Fixed an issue with opening a dialog from an interactive message when returning an empty response.
 - Fixed an issue where the **Add Members** modal was incorrectly themed on the Mattermost Dark theme.
 - Fixed a panic in the ``getPrevTrialLicense`` API request when loading the System Console on Team Edition.
 - Fixed various bugs for the Collapsed Reply Threads (Beta) feature, including:
   - Fixed an issue where an error occurred while following a thread with no replies.
   - Fixed an issue where ``reply_count`` of 0 was always returned for GET single Post on ``/posts/<postid>`` API.
   - Fixed an issue where following a single message returned a status 500.
   - Fixed an issue where when replying in a thread after unfollowing it, the thread was not auto-followed again.
   - Fixed an issue where when enabling Collapsed Reply Threads, channels that had no new activity were showing as unread.
   - Fixed an issue with thread unreads when the feature was enabled by a user.
   - Fixed an issue where self replies were marking threads as unread.
   - Unread threads are now correctly displayed on app load for teams in the sidebar when Collapsed Reply Threads feature is enabled.
   - Fixed an issue where "Thread" in the thread viewer was displayed vertically in some languages.
   - Fixed an issue where opening global threads containing a root post markdown image crashed the app.
   - Fixed an issue where the app crashed when switching to the Threads view after leaving a channel.

### Known Issues
 - Known issues related to the new Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - Sometimes an "Unable to get role" error appears when changing a channel member role in **System Console > User Management > Channels**.
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-07-15

### Highlights

#### Granular Data Retention Policies
 - A ``data_retention`` type job can now be run even if the global policy is disabled. The granular (i.e. team and channel-specific) policies will be executed when the data retention job is run. Please note there is a known issue where deleted posts get displayed in channels without new activity after the retention job is run.  This issue is tracked with [this ticket](https://mattermost.atlassian.net/browse/MM-36574).

### Improvements

#### User Interface (UI)
 - Markdown formatting is now stripped from push notifications.
 - Improved performance of components that show reactions on posts.
 - Improved performance of certain components when viewing non-Direct Message channels.
 - Added minor improvements to performance of messages posted in the right-hand side.
 - Added icons to apps in the Marketplace.
 - Apps can now add arbitrary markdown in between fields on forms.
 - Added support for markdown in apps forms, interactive dialogs field descriptions, errors, and slash commands.

### Known Issues
 - Known issues related to the new collapsed reply threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - Sometimes an "Unable to get role" error appears when changing a channel member role in **System Console > User Management > Channels**.
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-07-01

### Highlights

#### Collapsed Reply Threads (Early Beta Access)

 - We're excited to give you early access to Collapsed Reply Threads (Beta). It can be enabled in the **System Console > Experimental > Collapsed Reply Threads (Beta)**. Learn more about the features and known issues in [our documentation](/help/messaging/organizing-conversations.html).

#### Emoji Enhancements with Skin Tone Selection
 - Added support for emoji standard v13.0. Users now have the ability to choose various skin tones using the Mattermost emoji picker. Mobile support is planned for v1.45 Mobile App release (July 16th), so some emojis selected on desktop won't be visible on mobile apps.

### Improvements

#### User Interface (UI)
 - Added English-Australian language variation.
 - Added the ability to upload ``.jpeg`` files on Linux. Uploading ``.jpg`` files was already supported.
 - Before anything is typed, a list of channels you are a member of is now shown and sorted by recency in the channel switcher. The number of channels shown in the channel switcher in the default state are capped to maximum of 20. If there is no recent channel activity (in the case of new users), an alphabetical list of channels is shown displaying **My Channels** first and other **Public Channels** next, capped at a maximum of 20 by default.
 - Polish, German, and Italian languages were downgraded to beta as they are [no longer actively maintained](https://handbook.mattermost.com/contributors/contributors/localization#translation-quality).
 - Added the ability in the custom status tooltips, status dropdown and profile popover to select an expiry time for custom statuses. Also added new components ``ExpiryMenu`` and ``DateTimeInput`` to the custom status modal.

#### Administration
 - Optimized the bulk import process by no longer requiring the server to write the incoming archive to the filesystem when unzipping it.
 - Added channel restore and channel privacy change endpoints to the local mode using the System bot.

### Bug Fixes
 - Fixed an issue where sidebar icons were not aligned with the navigator area icons.
 - Fixed an issue where using CTRL+F in a **Direct Message** channel added the user ID rather than the user's name into the search field.
 - Fixed an issue where user icons were displayed at full opacity in muted channels.
 - Fixed an issue where a redundant ``user_update`` websocket event was generated for bot users.

### Known Issues
 - Sometimes an "Unable to get role" error appears when changing a channel member role in **System Console > User Management > Channels**.
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-06-16

### Improvements

#### User Interface (UI)
 - In the at-mention autocomplete, the user’s nickname is no longer shown when (you) is present.
 - Updated the help text on the **Add Users** channel modal.

#### Administration
 - The platform binary file has been removed from the distribution files. It should be replaced by the Mattermost binary file if it's being used in scripts.
 - Improved memory performance for large image uploads, particularly PNGs with transparency.

### Bug Fixes
 - Fixed an issue where users were unable to set a custom status emoji via slash command by adding the logic for detecting unicode emoji and setting it as custom status emoji via slash commands.
 - Fixed an issue where messages with fallback text were repeated.
 - Fixed an issue where a persistent unread badge showed on the **Main Menu** when **Enable Marketplace** or **Enable Plugins** was disabled.

### Known Issues
 - Pinned posts are no longer highlighted.
 - Sometimes an "Unable to get role" error appears when changing a channel member role in **System Console > User Management > Channels**.
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-06-02

### Improvements

#### User Interface (UI)
 - Removed status icon from the profile image in the center channel and the right-hand side view.
 - Added a performance improvement to the emoji picker overlay to improve typing performance.
 - Added performance improvements when receiving new posts.

#### Administration
 - Team-restricted direct channel creation is now also applied to the backend. Previously, this was restricted to the frontend.
 - Refactored the config storing logic to improve its robustness and performance.
 - Added a visual grouping of related settings under AD/LDAP in the System Console.

### Bug Fixes
 - Fixed an issue where the job scheduler server could miss a "changed leader" cluster event.
 - Fixed an issue where using ``Ctrl+Cmd+F`` on the MacOS Desktop App opened the search instead of full-screened the app.
 - Fixed an issue where the message input box was shadowed when uploading a file in the center channel.
 - Fixed an error caused by a post created with a non-string attachment field.
 - Fixed the opacity of the read state in the channel sidebar, as well as enhanced the opacity of the channel icon when the channel was unread.
 - Fixed an issue where users were unable to log in with O365 authentication when the AuthData was formatted differently between Office365 OAuth and Office 365 OpenID.

### Known Issues
 - Pinned posts are no longer highlighted.
 - Sometimes an "Unable to get role" error appears when changing a channel member role in **System Console > User Management > Channels**.
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

## Release 2021-05-21

### Improvements

#### User Interface (UI)
 - Added Hungarian (Beta) language.
 - A search tip is now shown when scrolling back in a channel.
 - Improved the error text in the **Edit Channel Header** modal.
 - Added the ability to clear a custom status when only an emoji and no text is set.
 - Redesigned message notification emails.

#### Administration
 - The default value of the [Support Email](/administration/config-settings.html#support-email) (previously ``_feedback@mattermost.com_``) has been removed. Admin Advisor will now prompt System Admins about missing configuration for the [Support Email](/administration/config-settings.html#support-email). This value is required, and it ensures Mattermost account requests are sent to the correct team for resolution.
 - The **Marketplace** button in the **Main Menu** is now displayed if the user has the ``sysconsole_write_plugins`` permission.
 - Added new feature discoveries in the System Console, including Data Retention Policy and OpenID Connect.
 - Added basic intra-cluster communication support for plugins.
 - Improved error messages for ``/header`` and ``/purpose`` commands.

### Bug Fixes
 - Fixed a race condition where enabling plugins would result in spurious errors in the logs.
 - Fixed a bug where team member permissions were not updated after associating a team with a permission scheme.
 - Fixed the responses of the role by ID and all roles of API endpoints when the role was associated to channel schemes.
 - Removed sticky sidebar headings in favor of fixing nesting errors.
 - Fixed an issue where the **Close** button in the **Create New Category** modal was only visible on mouse hover.
 - Fixed a bug where session expiration was extended with activity regardless of what the config setting ``ServiceSettings.ExtendSessionLengthWithActivity`` was set to.
 - Fixed an issue where the ``idmigrate`` command did not update values if they were not already present as LDAP attributes in the ``config.json``.

### Known Issues
 - Pinned posts are no longer highlighted.
 - Sometimes an "Unable to get role" error appears when changing a channel member role in **System Console > User Management > Channels**.
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows **License** and **Environment** as possible permissions, but they are always hidden in Cloud.

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
