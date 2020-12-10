# Mattermost Cloud Changelog

This changelog summarizes updates to [Mattermost Cloud](https://mattermost.com/get-started/), an enterprise-grade SaaS offering hosted by Mattermost.

## Release 2020-12-09

### Highlights

#### Incident Management provided out-of-the-box (E20)
 - Pre-packaged and pre-installed the Incident Management as well as Channel Export plugins for enterprise-ready builds.

### Improvements

#### Cloud-specific
 - The Customer Web Server can now make HTTP requests to an installation by passing the X-Cloud-Token header, with the value being that installation's Customer API Key.
 - System Admins can receive an email notifying them of a failed payment in Mattermost cloud.
 - In the event a subscription has a payment and there is no card on the account when that payment is processed, an email will be sent to attempt to get the user to pay up.

#### User Interface (UI)
 - Added the ability to mute categories with the experimental sidebar feature.
 - Added support for multi-selection of channels for dragging and dropping between channels in the experimental sidebar feature.
 - Group messages are now returned in the channel switcher when only first names are typed.
 - /dnd command will only set a do not disturb status whatever the current user status is.

#### Administration
 - Added a new `manage_remote_clusters` permission.
 - Enabled goSAML2 library as the only supported SAML Library.

### Bug Fixes
 - Cleaned up the config store on server initialization errors.
 - Fixed an issue where permissions did not grant read and/or write access to the Global Relay configuration settings.
 - Fixed an issue where the site configuration ‘’Read only’’ permission did not make the "Notice" section as read-only for the System Manager.
 - Fixed an issue where importing Client4 in a node server caused an exception due to rudder modules.
 - Fixed an issue where LDAP ‘’FirstLoginSync’’ didn't close LDAP Session.

### Database Changes
 - Added ``UnreadMentions`` column to ``ThreadMembership`` table.
 
### Websocket Event Changes
 - New websocket events added: ``thread_updated``, ``thread_follow_changed``, ``thread_read_changed``.

### Known Issues
 - System Manager does not have access to Billing section and sees blank screen.
 - Cloud > "Tips & Next Steps" should not show "Explore channels" section for guest users.
 - System Roles shows License and Environment as possible permissions but are always hidden in Cloud

## Release 2020-12-03

### Bug Fixes
  - Disabled the xmlsec1-based SAML library in favor of the re-enabled and improved SAML library.

## Release 2020-11-24

### Compatibility
 - PostgreSQL ended long-term support for [version 9.4 in February 2020](https://www.postgresql.org/support/versioning). Mattermost is officially supporting PostgreSQL version 10 with v5.26 release as PostgreSQL 9.4 is no longer supported. New installs will require PostgreSQL 10+. Previous Mattermost versions, including our current ESR, will continue to be compatible with PostgreSQL 9.4. We plan on fully deprecating PostgreSQL 9.4 and all 9.x versions in our v5.30 release (December 16, 2020). Please follow the instructions under the Upgrading Section within [the PostgreSQL documentation](https://www.postgresql.org/support/versioning/).

### Highlights

#### Modify new Admin roles permissions in the System Console (Beta)
 - Added a user interface for the existing new system roles functionality including a new permission to read and write system_roles.

#### Pre-package and enable incident management v1.1.1

### Improvements

#### Cloud-specific
 - Slack imports are no longer allowed in Cloud installations.
 - Mattermost cloud instances with delinquent subscriptions will be sent emails on a certain cadence, in certain cases:
    - A check happens twice per day to see if an installation is over the user limit
    - If that installation is over the user limit, they are marked for notification during the next billing cycle
    - If that installation is still over the limit 7, 14, 30, and 90 days into the next billing cycle, they will be sent emails with various wording to get them to add a payment method and upgrade their cloud billing 
    - If that installation is no longer over the limit 7, 14, and 30 days into the next billing cycle, we will "forgive" them, and not send any emails for that cycle. 
    - After the installation has gone over the limit, each time the job runs, it checks Stripe to check the state of the subscription. If it's flipped from "past_due" to active, it will cancel any emails for that cycle. Otherwise, it will continue on.

#### User Interface
 - @-autocomplete results are now prioritized based on recency and thread activity.
 - File attachments below size of 10 now show fractions.
 - The formatting of the channel header change message was improved.
 - Team invite workflow now shows BOT tags when the search returns Bot users.
 - Added the ability to zoom in/out of PDF files.
 - Added support for 16x16 base64 encoded mini images to use with progressive rendering.

#### Notifications
 - Channel-wide mentions are now automatically disabled when a user mutes a channel.

#### Integrations
 - Updated icon_emoji field in incoming webhooks to allow for emojis to also be specified with surrounding colons.
 - Dynamic auto-completion is now supported for built-in slash commands.
 - Added plugin hooks for ReationHasBeenAdded and ReactionHasBeenRemoved.

#### Administration
 - Added the ability to load a set of configuration custom defaults from a MM_CUSTOM_DEFAULTS_PATH environment variable.
 - Added AWS metering service support.
 - Added the ability to retrieve compliance files from the System Console.

### Bug Fixes
 - Fixed an issue with broken link previews for twitter links.
 - Fixed an issue where editing a post did not submit with CMD+ENTER.
 - Fixed an issue where users were able to create or edit slash commands to have more than two slashes in the URL.
 - Fixed an issue where resized emojis got overwritten with original data.
 - Fixed an issue where the sidebar category "More" menu was not shown when hovering over a long category name.
 - Fixed an issue where a received direct message did not show up on the sidebar if it wasn't previously created.
 - Fixed an issue where a search using from: failed to auto-load more results in the right-hand side when Elasticsearch was enabled.
 - Fixed an issue where s3 file backend TestFileConnection failed due to permissions if S3PathPrefix was in use.
 - Fixed an issue where an id was missing for Tooltip in PostInfo.

#### Websocket Event Changes
 - In post_deleted websocket event, System Admins are now notified when a user initiates a post deletion.

#### API Changes
 - Added new local API endpoints for getting, updating and deleting incoming and outgoing webhooks.
 - Added new API endpoints to work with experimental collapsed threads.

### Known Issues
 - System Manager does not have access to Billing section and sees blank screen.
 - Cloud > "Tips & Next Steps" should not show "Explore channels" section for guest users.
 - System Roles shows License and Environment as possible permissions but are always hidden in Cloud
