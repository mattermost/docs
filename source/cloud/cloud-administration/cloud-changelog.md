# Mattermost Cloud Changelog

This changelog summarizes updates to [Mattermost Cloud](https://mattermost.com/get-started/), an enterprise-grade SaaS offering hosted by Mattermost.

## Release 2021-02-24

### Highlights

#### Custom Statuses
 - Custom Statuses allow users to add a descriptive status message and emoji that’s visible to everyone. Users now gain the flexibility to express their current status in any way they prefer. Mobile support is coming soon.

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
