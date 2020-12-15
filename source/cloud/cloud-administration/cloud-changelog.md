# Mattermost Cloud Changelog

This changelog summarizes updates to [Mattermost Cloud](https://mattermost.com/get-started/), an enterprise-grade SaaS offering hosted by Mattermost.

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
