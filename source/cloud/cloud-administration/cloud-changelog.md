# Mattermost Cloud Changelog

This changelog summarizes updates to [Mattermost Cloud](https://mattermost.com/get-started/), an enterprise-grade SaaS offering hosted by Mattermost.

## Release 2021-01-26

### Highlights

#### Channel Sidebar General Availability
 - The new channel sidebar is enabled system-wide by default. Mattermost now gives users flexibility to organize channels and direct messages into custom, collapsible sidebar categories. Users now gain full personalization of their sidebar to improve productivity, reduce clutter and focus on what matters. Features include custom, collapsible sidebar categories, unread channel management, and new channel menus.

### Improvements

#### User Interface (UI)
 - Added new languages, Bulgarian and Swedish.
 - Moved the header icons to the left of the header beside the channel description.

#### Plugins
 - Enabled experimental support for arm64 plugins by allowing any matching ``GOOS-GOOARCH`` combination in the plugin manifest.

#### Administration
 - The ``UseExperimentalGossip`` field under ClusterSettings is now ``true`` by default. This means that new installations will use the gossip protocol for cluster communication. There will be no changes to existing installations. The Gossip protocol is now considered to be in General Availability and is the recommended clustering mode.
 - ``AnalyticsPostCount`` now avoids unnecessary table scans during various background jobs.
 - Added a ``CollapsedThreads`` feature flag.
 - The Help text for Rate Limiting setting was updated to explain the purpose of rate limiting.
 - Removed the word "experimental" from gossip setting in the System Console.
 - The Database search using Postgresql now supports searching for terms with underscore.
 - Removed the `ExperimentalChannelSidebarOrganization` setting and added an `EnableLegacySidebar` setting. The new channel sidebar will be enabled system-wide by default.

#### Bug Fixes
 - Fixed an issue where the Admin Filter option was not disabled in the AD/LDAP page for Admin roles with a ``sysconsole_write_authentication`` permission.
 - Fixed an issue where channels would sometimes be removed from custom categories when a user left a team.
 - Fixed an issue where the error text was missing when the team name was left blank on the Team Create page.
 - Fixed an issue where the System Manager was able to download the Compliance Export files.
 - Fixed an issue where themed button colours in interactive message attachments in Mattermost’s default dark theme were mismatched.
 - Fixed an issue where bold and italics shortcuts triggered with ctrl+b on Mac.
 - Fixed an issue where a "Your license does not support cloud requests” log error appeared on self-hosted servers.

#### Known Issues
 - **Cloud > "Tips & Next Steps"** should not show an "Explore channels" section for guest users.
 - System Roles shows License and Environment as possible permissions but they are always hidden in Cloud.

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
