# Mattermost Changelog

This changelog summarizes updates to [Mattermost Team Edition](http://www.mattermost.org/), an open source team messaging solution released monthly under an MIT license, and [Mattermost Enterprise Edition](https://about.mattermost.com/pricing/), a commercial upgrade offering enterprise messaging for large organizations.

Also see [changelog in progress](http://bit.ly/2nK3cVf) for the next release.

## Release v4.2.0
Release date: 2017-09-16

### Security Update

- Mattermost v4.2.0 contains multiple security fixes ranging from low to moderate severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Highlights

#### Interactive Message Buttons
- Added message buttons to support user interactions with posts made by incoming webhooks and custom slash commands.

#### Mobile Support for AppConfig
- iOS and Android mobile apps now support Enterprise Mobility Management (EMM) solutions through integration with [App Config](https://www.appconfig.org/). See [documentation](https://docs.mattermost.com/deployment/mobile-appconfig.html) to learn more.

### Improvements

#### Web User Interface
- Redesigned the channel member list.
- Redesigned the message input box.
- Redesigned the keyboard shortcuts dialog (CTRL/CMD+/).
- Added a loading indicator when selecting a team on team selection page.
- Added an on hover effect for team icons in the team sidebar, and the channel name and favorite button in channel header.
- Added an active state for the channel member icon in channel header.
- Added a "+" icon next to the Direct Messages header on channel sidebar to open a new direct or group message.
- Added a tooltip for Main Menu next to user profile picture.
- Mouse cursor now changes to a "hand selector" when hovering over the paperclip icon to upload a file.

#### Mobile View
- Made hover effects consistent across all header icons.
- Removed transparency of the [...] menu in the right-hand sidebar.
- Reduced opacity in channel info dialog.
- Updated background color of search bar.

#### Integrations
- Added support for Slack-compatible delayed slash commands through the `response_url` parameter.
- Improved handling of content-types for integrations.

#### Notifications
- Added support for plain text version of email notifications.
- Added "Joined the channel" system message for the person who created the channel.

#### Administration
- Added a CLI command `platform channel move` to move a channel to another team.
- CLI command `platform team delete` now lets you delete teams with no channels.

#### Enterprise Edition
- Removed the "Delete Channel" option for private channels, if you're the last channel member and policy setting restricts channel deletion to admins only.
- In multi-node cluster environment, scheduled tasks such as LDAP sync will only happen on a single node through leader election for increased performance.
- Added direct message channels to compliance exports.
- Added a CLI command `platform channel modify` to convert a public channel to private, and vice versa.
- Elasticsearch indexes over a certain age can be aggregated as part of the daily scheduled job.

### Bug Fixes
- Fixed permalinks not always loading in the channel.
- Fixed an issue where a System Admin couldn't scroll to the bottom of the System Console sidebar in Firefox.
- Flag icon and the "x" icon to close website previews now properly aligned for replies in compact view.
- Fixed expand/collapse arrows not being visible for YouTube videos when image links are expanded by default.
- Fixed an issue where reacting to a post in the right-hand sidebar via emoji picker didn't add the emoji to "Recently Used" section.
- Pressing the ESC key no longer clears search box contents.
- Fixed an issue where turning off email batching in the System Console resulted in no email notification option selected in Account Settings.
- Fixed an issue where a user wasn't able to scroll down in message preview mode when using Markdown headings.
- Fixed an issue on Safari browsers where file thumbnails were sometimes blank.
- Fixed an issue where quotes weren't working inside URL links.
- Fixed an error when the language set in **Account Settings > Display** was removed from available languages in **System Console > Localization**.
- Fixed out-of-channel mentions for usernames with dashes and periods.
- Fixed an issue where a missing config setting sometimes caused server panic.
- Jumping to a group message channel from a flagged message list now adds the channel to the channel list.
- Character limits are no enforced when renaming a channel via `/rename`.
- Fixed channel header icons when WebRTC call is on-going.
- Fixed webhook message attachments not appearing in search results or flagged messages list.
- Timestamp on deleted, ephemeral, or pending posts is no longer a permalink, causing a blank page.
- Fixed focus issues on iPad Classic app.
- Fixed an issue where changing other user's profile image as a System Admin via the API didn't work.
- Fixed mention notifications firing for mentions inside triple backticks.
- Collapse and expand arrows no longer shown for image links when no image is available.
- A single collapsed link preview now stays collapsed after page refresh.
- With email batching enabled, if there is activity in Mattermost before email batch is sent, the email notification is not sent.
- Fixed an issue where copying and pasting SVG files into message draft never finish uploading.
- Autocomplete is no longer cut on the channel header modal.
- Fixed email notifications settings appearing saved despite cancelling the change.
- Notification confirmation message no longer appears when sending channel wide @-all and @-channel mentions in code blocks.

### Compatibility

#### Breaking Changes

1 - Mattermost now handles multiple content types for integrations, including plaintext content type. If your integration suddenly prints the JSON payload data instead of rendering the generated message, make sure your integration is returning the `application/json` content-type to retain previous behavior.

2 - By default, user-supplied URLs such as those used for Open Graph metadata, webhooks, or slash commands will no longer be allowed to connect to reserved IP addresses including loopback or link-local addresses used for internal networks. 

This change may cause private integrations to break in testing environments, which may point to a URL such as http://127.0.0.1:1021/my-command.

If you point private integrations to such URLs, you may whitelist such domains, IP addresses, or CIDR notations via the [AllowedUntrustedInternalConnections config setting](https://docs.mattermost.com/administration/config-settings.html#allow-untrusted-internal-connections-to) in your local environment. Although not recommended, you may also whitelist the addresses in your production environments. See [documentation to learn more](https://docs.mattermost.com/administration/config-settings.html#allow-untrusted-internal-connections-to).

Push notification, OAuth 2.0 and WebRTC server URLs are trusted and not affected by this setting.

3 - Mattermost `/platform` repo has been separated to `/mattermost-webapp` and `/mattermost-server`. This may affect you if you have a private fork of the `/platform` repo. [More details here](https://forum.mattermost.org/t/mattermost-separating-platform-into-two-repositories-on-september-6th/3708).

#### Removed and Deprecated Features
- All APIv3 endpoints are scheduled for removal on January 16, 2018.

For a list of past and upcoming deprecated features, [see our website](https://about.mattermost.com/deprecated-features/).

#### config.json

The following settings were unintentionally added to ``config.json`` and are removed in Mattermost 4.2.

- Under `SupportSettings` in `config.json`:
  - `"AdministratorsGuideLink": "https://about.mattermost.com/administrators-guide/"`
  - `"TroubleshootingForumLink": "https://about.mattermost.com/troubleshooting-forum/"`
  - `"CommercialSupportLink": "https://about.mattermost.com/commercial-support/"`

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

**Changes to Team Edition and Enterprise Edition**:

- Under `ServiceSettings` in `config.json`:
  - Added `AllowedUntrustedInternalConnections": ""` to specify domains, IP address or CIDR notations for internal connections. Used in testing environments when developing integrations locally on a development machine. Not recommended for use in production.
- Under `TeamSettings` in `config.json`:
  - Added `EnableXToLeaveChannelsFromLHS: false` to set if a user can leave a channel by clicking "X" next to a channel in the channel sidebar. This setting is Beta and may be replaced or removed in a future release.
- Under `FileSettings` in `config.json`:
  - Added `AmazonS3Trace: false` to enable additional debugging for Amazon S3.

**Additional Changes to Enterprise Edition**:

- Under `ElasticsearchSettings` in `config.json`:
  - Added `AggregatePostsAfterDays": ""` to specify the age at which indexes will be aggregated as part of the daily scheduled job
  - Added `PostsAggregatorJobStartTime": ""` to specify the start time of the daily scheduled aggregator job.
- Under `TeamSettings` in `config.json`:
  - Added `ExperimentalTownSquareIsReadOnly: false` to set if Town Square is a read-only channel. Applies to all teams in the Mattermost server. This setting is Beta and may be replaced or removed in a future release.
- Added `ThemeSettings` in `config.json`. These settings are Beta and may be replaced or removed in a future release.
  - Added `"EnableThemeSelection": true` to set whether end users can change their Mattermost theme.
  - Added `"DefaultTheme": "default"` to set default theme for new users.
  - Added `"AllowCustomThemes": true` to set whether end users can set a custom theme.
  - Added `"AllowedThemes": []` to list which built-in Mattermost themes are available to users.

### Database Changes

### API v4 Changes
- It is recommended that any new integrations use APIv4 endpoints. For more details, and for a complete list of available endpoints, see [https://api.mattermost.com/](https://api.mattermost.com/).
- All APIv3 endpoints are scheduled for removal on January 16, 2018.

**Added routes (API v4)**
- `POST` at `/posts/{post_id}/actions/{action_id}`
  - To perform a post action, which allows users to interact with integrations through messages.

### Known Issues
- Google login fails on the Classic mobile apps.
- Clicking on a channel during the tutorial makes the tutorial disappear.
- User can receive a video call from another browser tab while already on a call.
- Jump link in search results does not always jump to display the expected post.
- First load of the emoji picker is slow on low-speed connections or on deployments with hundreds of custom emoji.
- Scrollbar is sometimes not visible in the left-hand sidebar after switching teams.
- Certain code block labels don't appear while scrolling on iOS mobile web.
- Deleted message doesn't clear unreads or unread mentions.
- Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
- Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
- Searching with Elasticsearch enabled may not always highlight the searched terms.
- Channel links to channels that the current user does not belong to may not render correctly.
- Pinned posts list header sometimes shows an incorrect channel name.
- Missing an indication if a message is pending but not yet sent.
- Searching for users with one or two-letter names doesn't work.

### Contributors

/platform

- [asaadmahmood](https://github.com/asaadmahmood), [ccbrown](https://github.com/ccbrown), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [dmeza](https://github.com/dmeza), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [jasonblais](https://github.com/jasonblais), [jwilander](https://github.com/jwilander), [KenmyZhang](https://github.com/KenmyZhang), [lindalumitchell](https://github.com/lindalumitchell), [meilon](https://github.com/meilon), [MusikPolice](https://github.com/MusikPolice), [n1aba](https://github.com/n1aba), [pruthvip](https://github.com/pruthvip), [saturninoabril](https://github.com/saturninoabril), [stanhu](https://github.com/stanhu), [sudheerDev](https://github.com/sudheerDev), [Whiteaj36](https://github.com/Whiteaj36)

/docs

- [amyblais](https://github.com/amyblais), [balasankarc](https://github.com/balasankarc), [esethna](https://github.com/esethna), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jwilander](https://github.com/jwilander), [lfbrock](https://github.com/lfbrock), [lindy65](https://github.com/lindy65)

/mattermost-redux

- [aditya-konarde](https://github.com/aditya-konarde), [brettmc](https://github.com/brettmc), [ccbrown](https://github.com/ccbrown), [enahum](https://github.com/enahum), [hmhealey](https://github.com/hmhealey), [jwilander](https://github.com/jwilander), [kevin3274](https://github.com/kevin3274), [saturninoabril](https://github.com/saturninoabril)

/mattermost-mobile

- [csduarte](https://github.com/csduarte), [enahum](https://github.com/enahum), [hmhealey](https://github.com/hmhealey), [lfbrock](https://github.com/lfbrock), [onepict](https://github.com/onepict)

/desktop

- [jasonblais](https://github.com/jasonblais), [yuya-oc](https://github.com/yuya-oc)

/mattermost-kubernetes

- [coreyhulen](https://github.com/coreyhulen), [crspeller](https://github.com/crspeller), [escardin](https://github.com/escardin), [grundleborg](https://github.com/grundleborg)
	
/mattermost-docker

- [jasonblais](https://github.com/jasonblais), [pichouk](https://github.com/pichouk), [tejasbubane](https://github.com/tejasbubane)
	
/mattermost-push-proxy

- [coreyhulen](https://github.com/coreyhulen), [enahum](https://github.com/enahum)

/mattermost-mdk

- [jwilander](https://github.com/jwilander)

/mattermost-api-reference

- [ccbrown](https://github.com/ccbrown), [cpanato](https://github.com/cpanato), [jasonblais](https://github.com/jasonblais), [jwilander](https://github.com/jwilander), [prixone](https://github.com/prixone)

/mattermost-load-test

- [crspeller](https://github.com/crspeller)

## Release v4.1.1

 - **v4.1.1, released 2017-09-16**
   - Mattermost v4.1.1 contains multiple security fixes ranging from low to medium severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.1.0, released 2017-08-16**
   - Original 4.1.0 release

### Security Update

- Mattermost v4.1.0 contains multiple security fixes ranging from low to high severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Highlights

#### JIRA App
- Built-in JIRA integration that can post to multiple channels using a single webhook. [See documentation](https://about.mattermost.com/default-jira-plugin) 

#### Personal Access Tokens
- Enables easier and more flexible integrations by authenticating against the REST API. See [documentation](https://about.mattermost.com/default-user-access-tokens/)

#### Updated iOS and Android Apps
- v1.1 of the Native [iOS](https://itunes.apple.com/us/app/mattermost/id1257222717?mt=8) and [Android]() Apps are released with support for search, group messaging, viewing emoji reactions and improved performance on poor connections.

#### Elasticsearch Beta ([Enterprise Edition E20](https://about.mattermost.com/pricing/))
- Connect your Elasticsearch server to Mattermost, then build and manage your post index via the System Console interface.
- [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html) is a distributed, RESTful search engine supporting highly efficient database searches in a [cluster environment](https://docs.mattermost.com/deployment/cluster.html).

### Improvements

#### Web User Interface
- Ephemeral messages now note that they are "(Only visible to you)" .
- Navigating to an invalid team invite link will now redirect to an error page.
- Cropping of image thumbnails now looks the same before and after posting.
- Clicking on @mentions will now open the contact card for the user.
- User lists now display full name and nickname.
- Added over 500 new emoji.
- Searching on slow connections now shows a loading spinner in the right-hand side.
- Added a close button next to link previews.
- Ephemeral messages will now always appear as parent posts.
- Added [...] menu to search results, pinned posts and flagged posts lists.
- Clicking the username in a profile popover inserts the username to the message box.

#### Notifications
- Added an option to Push Notification Contents to send no channel name or message text
- Updated the default email frequency to 15 minutes if email batching is enabled by the System Admin.
- Users are now prompted from Account Settings to set Edge notification sounds in their browser settings.
- Updated the desktop notification text for incoming webhooks to more accurately reflect the payload.

#### Files
- File uploads in a single message are ordered based on time of upload. When multiple files are selected, files are ordered in alphabetical order based on file name.

#### Administration
- No longer require a refresh after a user is promoted to a Team Admin.
- Announcement banner now supports URLs.
- Bulk importer now supports user preferences, including favorite channels, flagged posts and notification preferences.
- Changed username to be the default name display setting in the System Console.
- Channel member list now follows the Teammate name display configuration setting.
- Added more debugging info to server logs for failed OAuth requests.
- Added a new System Console push notification content setting to only display sender name.
- Added support for unauthenticated, but encrypted SMTP connection.

#### Integrations
- Null values are now ignored in webhook attachments.
- Outgoing webhooks can now fire if the post contains only an attachment.
- Added ``/code`` built-in slash command to create a code block.
- Added ``/purpose`` built-in slash command to set the channel purpose.
- Added ``/rename`` built-in slash command to rename the channel.
- Added ``/leave`` built-in slash command to leave a channel.

#### Enterprise Edition E20
- Added a System Console setting to disable file uploads and downloads on mobile.
- Added a new Email Notification Content setting to specify the amount of detail sent in email notification.
- Added support for server-side encryption of files in Amazon S3, using Amazon S3-managed keys.

### Bug Fixes
- Fixed incorrectly rotated image thumbnails that were uploaded from mobile devices.
- Adding or removing reactions from a post with an image preview no longer causes the preview to expand or collapse.
- JavaScript error no longer thrown when file upload fails due to network interruption.
- Error messages in Account Setting fields no longer stack.
- Fixed Slack Import of non-ascii channel names.
- Changing the search term in the More Direct Messages member list now resets the search.
- Help text for the Channel Switcher (CTRL/CMD+K) is now shown on small desktop windows, and removed on mobile.
- Keyboard shortcut for Account Settings (CTR/CMD+SHIFT+A) now toggles.
- Fixed the Preview button in the text input box and message edit modal.
- Fixed a JavaScript error when switching teams while uploading a file.
- CLI tool to delete all users no longer requires a user argument.
- CLI tool now deletes webhooks and slash commands when deleting teams and channels.
- Custom slash commands no longer throw an error if used in a Direct Message channel.
- System Console now reads and honors the Amazon S3 Region setting.
- Fixed whitespace and trimming on code blocks and empty table cells.
- Disabled the "Create Account" button after the first click so the system does not attempt to create the account twice.
- More Channels modal no longer stops paging after the first two pages.
- Editing channel names now correctly limits character count to 22.
- Fixed broken links on the **System Console > Mobile Push** page.
- `/away` and `/offline` ephemeral messages can no longer contain extra text posted with the slash command.
- Fixed teams being sometimes incorrectly marked unread across tabs.
- Fixed JavaScript error thrown when viewing a channel containing an invalid emoji reaction.
- Periods after URLs are no longer added to the link.
- Recent emoji in emoji picker no longer shows deleted custom emoji.
- Fixed image thumbnails and previews on IE11.
- Fixed message attachments in incoming webhooks and slash commands not always truncating properly.
- Non-admins can now view their previously created integrations.

### Compatibility

#### Removed and deprecated features
- All APIv3 endpoints are scheduled for removal on January 16, 2018.

For a list of past and upcoming deprecated features, [see our website](https://about.mattermost.com/deprecated-features/).

#### config.json

The following settings were unintentionally added to ``config.json`` and will be removed in Mattermost 4.2, released on September 16th.

- Under `SupportSettings` in `config.json`:
  - `"AdministratorsGuideLink": "https://about.mattermost.com/administrators-guide/"`
  - `"TroubleshootingForumLink": "https://about.mattermost.com/troubleshooting-forum/"`
  - `"CommercialSupportLink": "https://about.mattermost.com/commercial-support/"`

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

**Changes to Team Edition and Enterprise Edition**:

- Under `ServiceSettings` in `config.json`:
  - `"EnableUserAccessTokens": false` to enable personal access tokens for integrations to authenticate against the REST API
- Under `EmailSettings` in `config.json`:
  - Added `"EnableSMTPAuth": false` to support SMTP servers requiring no authentication
  - Added `"EmailNotificationContentType": "full"` to specify the amount of detail sent in email notification contents

**Additional Changes to Enterprise Edition**:

- Under `FileSettings` in `config.json`:
  - Added `"AmazonS3SSE": false` to enable server-side encryption for files in Amazon S3.
  - Added `"EnableMobileUpload": true` to enable file uploads on mobile devices
  - Added `"EnableMobileDownload": true` to enable file downloads on mobile devices
- Under `JobSettings` in `config.json`:
  - Added `"RunJobs": true` to enable running jobs on the jobs server
  - Added `"RunScheduler": true` to enable scheduling jobs on the job server
- Under `ElasticsearchSettings` in `config.json`:
  - Added `"ConnectionUrl": "http://dockerhost:9200"` to set the URL of the Elasticsearch server
  - Added `"Username": ""` to specify the username to access the Elasticsearch server
  - Added `"Password": ""` to specify the password to access the Elasticsearch server
  - Added `"EnableIndexing": false` to enable Elasticsearch indexing
  - Added `"EnableSearching": false` to enable searching using Elasticsearch
  - Added `"Sniff": true` to enable sniffing on the Elasticsearch server
  - Added `"PostIndexReplicas": 1` to specify how many replicas to use for each post index
  - Added `"PostIndexShards": 1` to specify how many shards to use for each post index

### Database Changes

**UserAccessToken Table:**
- Added table

**JobStatuses Table:**
- Removed table

**Jobs Table:**
- Added table

**Users Table:**
- Modified ``Roles`` column maximum size from 64 to 256 characters

### API v4 Changes
- Mattermost 4.0 has a stable release of API v4 endpoints. It is recommended that any new integrations use the v4 endpoints. For more details, and for a complete list of available endpoints, see [https://api.mattermost.com/](https://api.mattermost.com/).
- All APIv3 endpoints are scheduled for removal on January 16, 2018.

**Added routes (API v4)**
See [api.mattermost.com](https://api.mattermost.com/) for more details:
- `GET` at `api/v4/jobs`
- `POST` at `api/v4/jobs` 
- `GET` at `api/v4/jobs/{job_id:[A-Za-z0-9]+}`
- `POST` at `api/v4/jobs/{job_id:[A-Za-z0-9]+}/cancel`
- `GET` at `api/v4/jobs/type/{job_type:[A-Za-z0-9_-]+}`
- `POST` at `api/v4/elasticsearch/purge_indexes`
- `POST` at `api/v4/users/{user_id:[A-Za-z0-9]+}/tokens`
- `GET` at `api/v4/users/{user_id:[A-Za-z0-9]+}/tokens`
- `GET` at `api/v4/users/{user_id:[A-Za-z0-9]+}/tokens/{token_id:[A-Za-z0-9]+}`
- `POST` at `api/v4/users/{user_id:[A-Za-z0-9]+}/tokens/revoke`

### Known Issues

- Google login fails on the Classic mobile apps.
- Clicking on a channel during the tutorial makes the tutorial disappear.
- User can receive a video call from another browser tab while already on a call.
- Jump link in search results does not always jump to display the expected post.
- First load of the emoji picker is slow on low-speed connections or on deployments with hundreds of custom emoji.
- Scrollbar is sometimes not visible in the left-hand sidebar after switching teams.
- Certain code block labels don't appear while scrolling on iOS mobile web.
- A public channel doesn't always show up in another browser tab or client until after refresh.
- Deleted message doesn't clear unreads or unread mentions.
- Changing the search term in the More Direct Messages modal doesn't reset the page.
- Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
- Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms
- Searching with Elasticsearch enabled may not always highlight the searched terms
- Channels links to channels that the current user does not belong to may not render correctly

### Contributors

Many thanks to all our contributors. In alphabetical order:

/mattermost-server

- [94117nl](https://github.com/94117nl), [asaadmahmood](https://github.com/asaadmahmood), [ccbrown](https://github.com/ccbrown), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [debanshuk](https://github.com/debanshuk), [dmeza](https://github.com/dmeza), [enahum](https://github.com/enahum), [fraziern](https://github.com/fraziern), [grundelborg](https://github.com/grundelborg), [harshavardhana](https://github.com/harshavardhana), [hmhealey](https://github.com/hmhealey), [jasonblais](https://github.com/jasonblais), [jwilander](https://github.com/jwilander), [lindalumitchell](https://github.com/lindalumitchell), [megos](https://github.com/megos), [moonmeister](https://github.com/moonmeister), [MusikPolice](https://github.com/MusikPolice), [Ppjet6](https://github.com/Ppjet6), [saturninoabril](https://github.com/saturninoabril), [tejaycar](https://github.com/tejaycar), [Whiteaj36](https://github.com/Whiteaj36)

/docs

- [amyblais](https://github.com/amyblais), [bkmgit](https://github.com/bkmgit), [esethna](https://github.com/esethna), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [JeffSchering](https://github.com/JeffSchering), [john-combs](https://github.com/john-combs), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [lindy65](https://github.com/lindy65), [pichouk](https://github.com/pichouk), [prixone](https://github.com/prixone), [Samiksha416](https://github.com/Samiksha416)

/mattermost-mobile

- [csduarte](https://github.com/csduarte), [enahum](https://github.com/enahum), [hmhealey](https://github.com/hmhealey), [lfbrock](https://github.com/lfbrock)

/mattermost-push-proxy

- [coreyhulen](https://github.com/coreyhulen)

/mattermost-redux

- [94117nl](https://github.com/94117nl), [csduarte](https://github.com/csduarte), [enahum](https://github.com/enahum), [grundelborg](https://github.com/grundelborg), [hmhealey](https://github.com/hmhealey), [jwilander](https://github.com/jwilander), [saturninoabril](https://github.com/saturninoabril)

/mattermost-api-reference

- [ccbrown](https://github.com/ccbrown), [grundelborg](https://github.com/grundelborg), [jwilander](https://github.com/jwilander), [thePanz](https://github.com/thePanz)

/mattermost-kubernetes

- [crspeller](https://github.com/crspeller)

/mattermost-docker

- [jminardi](https://github.com/jminardi), [jnbt](https://github.com/jnbt), [pichouk](https://github.com/pichouk)

/mattermost-load-test

- [crspeller](https://github.com/mattermost/crspeller)

/mattermost-bot-sample-golang

- [fkr](https://github.com/fkr), [hmhealey](https://github.com/hmhealey)

## Release v4.0.5

 - **v4.0.5, released 2017-09-16**
   - Mattermost v4.0.5 contains multiple security fixes ranging from low to medium severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.0.4, released 2017-08-18**
   - Mattermost v4.0.4 contains multiple security fixes ranging from low to high severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
   - Fixed issue when using single-sign-on with GitLab where using a non-English language option in **System Console > Localization** sometimes resulted in a login failure.
 - **v4.0.3, released 2017-08-10**
   - Fixed issue with `AmazonS3Region` config setting being ignored in Minio file storage setup.
   - Fixed issue when using high availability mode in Enteprise Edition E20 where the bind address wasn't set correctly for the hashicorp memberlist.
 - **v4.0.2, released 2017-07-31**
   - Fixed issue when using single-sign-on with GitLab (and in Enterprise Edition with SAML, Office365 and G Suite), where using a non-English language option in Account Settings resulted in a login failure.
   - Fixed issue with custom slash commands not working in direct message channels.
   - Fixed issue with GitLab and SAML single sign-on in Mattermost mobile apps redirecting to a browser page.
 - **v4.0.1, released 2017-07-18**
   - Fixed issue where pinning or un-pinning messages didn't work if `AllowTimeLimit` config setting is set to `Never`.
   - Fixed issue where uploading or removing the **Service Provider Public Certificate** file in **System Console > SAML** refreshed the page, losing all unchanged settings.
   - Fixed deactivated users appearing in channel member, team member and direct message lists.
   - Fixed PDF previews not loading.
 - **v4.0.0, released 2017-07-16**
   - Original 4.0.0 release

### Security Update

- Mattermost v4.0.0 contains multiple security fixes ranging from low to high severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Highlights

#### Native iOS and Android Apps
- Second generation mobile apps released for [iOS](https://itunes.apple.com/us/app/mattermost/id1257222717?mt=8) and [Android](https://play.google.com/store/apps/details?id=com.mattermost.rn).
- The apps are [EMM compatible starting with BlackBerry Dynamics](https://about.mattermost.com/mattermost-2nd-gen-mobile-apps-released-emm-compatible-starting-with-blackberry-dynamics/).

#### Updated Web User Interface
- Updated the appearance of channel header and channel sidebar in the web user interface.
- Updated the default theme, "Mattermost". To try it, go to **Account Settings > Display > Theme**.

#### Emoji Picker
- The emoji picker offers quick access to emoji when composing messages or adding reactions.
- Promoted from Beta, and enabled to all users by default.

#### Languages
- Added Italian translations to the user interface.

#### API v4 (Stable Release)
- Mattermost webapp moved to API v4 endpoints, which allow for more powerful integrations and server interaction.
- API v3 endpoints are supported until January 16, 2018. To learn more about migrating to APIv4 endpoints, [see https://api.mattermost.com/](https://api.mattermost.com/).

#### High Availability ([Enterprise Edition E20](https://about.mattermost.com/pricing/))
- Mattermost servers are dynamically added and removed based on discovery and their cluster name using the hashicorp memberlist.
- Added support for experimental gossip protocol, where the server will attempt to communicate via the gossip protocol over the gossip port.

### Improvements

#### Web User Interface
- Adjusted post spacing to be consistent across Markdown formatting, replies and consecutive posts.
- On hover colour for pin and channel member icons now consistent with flag and recent mentions icons.
- Emojis are now vertically aligned in post view.
- Channel name, header and purpose now update in real time for all users.
- For reply threads in the center channel, the "Commented on" phrase now respects the teammate name display config setting.
- Code block language tag is no longer selectable making it easier to copy the code.
- Aligned the search box with right-hand side reply thread.
- New user profile pictures now update for other users upon refresh.
- Improved rendering of @mention highlighting in message view.

#### Mobile Web
- Added "Create Team" and "Leave Team" options to the Main Menu.
- Updated the look of Account Settings pages on mobile.
- User profile popover no longer gets cropped in the center channel on iOS browser.
- Link preview image now resizes correctly on iOS browser.

#### Notifications
- Unread messages and mentions now sync across browser tabs and devices.
- Improved desktop notifications for webhook attachments.

#### Emoji Picker & Custom Emoji
- Newly created custom emoji immediately display to all users without requiring a refresh.
- Improved position of the emoji picker near the top of the channel or the right-hand side comment thread.

#### Keyboard Shortcuts
- CTRL+SHIFT+K shortcut now toggles the Direct Message dialog open and closed.
- SHIFT+UP now opens a reply thread for the most recent message posted by a user, skipping system messages.

#### Slash Commands
- Added the following built-in slash commands:
  - `/header` command to set the channel header.
  - `/help` command to open the Mattermost help page in a new browser tab.
  - `/open` command to switch or join a channel.
  - `/search` command to search text in messages.
  - `/settings` command to open the Account Settings dialog.
- `/invite_people` slash command is now disabled when account creation is set to false.
- If a message starts with a / but fails to send (either due to timeout or invalid command), the message is put back to the input box.

#### Bulk Import Tool
- Added support for Direct Message channels and posts to the [bulk import tool](https://docs.mattermost.com/deployment/bulk-loading.html).

#### Authentication
- User creation via OAuth (GitLab/Google/Office365) properly restricted to accepted domains, [if specified](https://docs.mattermost.com/administration/config-settings.html#restrict-account-creation-to-specified-email-domains).
- **Invite New Member** dialog validates email addresses against accepted domains, if set.

#### New URL Routes
- Added the ability to Direct Message by email or username with the following new routes for Direct Message channels:
  - `.../teamname/messages/@username`
  - `.../teamname/messages/email`
  - `.../teamname/messages/user_id` (redirects to `...teamname/messages/@username`)
  - `.../teamname/messages/id1_id2` (redirects to `...teamname/messages/@username`)
- Also added a new route for Group Message channels:
  - `.../teamname/messages/generated_id`

#### Link Previews
- After posting a message containing an image link, a preview is loaded only if one is available.

#### Enterprise Edition
- When a SAML user uses a non-supported locale, the language now defaults to English, preventing login issues.

### Bug Fixes
- Emoji picker now closes in Firefox when clicking outside of it.
- [...] menu no longer disappears in the comment thread when hovering over another post.
- New direct messages received while in no teams do not show as unread after rejoining a team.
- Fixed JavaScript errors when receiving messages when not belonging to a team.
- An empty push notification no longer sent for messages only containing file attachments.
- Custom emoji search results no longer filter by creator's first and last name.
- `/expand` and `/collapse` slash commands now properly collapse images in website link previews.
- Group Message channels that are favorited can now be closed.
- Deactivated users now properly listed in Direct and Group Message channels in the left-hand sidebar.
- Fixed search in team and channel Manage Members dialog.
- File upload cancelled if you click "x" on thumbnail while file is uploading in your message draft.
- Status no longer appears offline after joining a new team.
- An empty push notification is no longer sent for messages only containing file attachments.
- Center channel maintains scroll position when new messages are received in the channel.
- Deleting the focused post in permalink view now sends user to normal channel view.
- Max Users per Team setting in **System Console > Users and Teams** no longer includes inactive users.

### Compatibility

#### Breaking Changes

- If you are using NGINX as a proxy for the Mattermost Server, replace the `location /api/v3/users/websocket {` line with `location ~ /api/v[0-9]+/(users/)?websocket$ {` in the `/etc/nginx/sites-available/mattermost` NGINX configuration file. [See documentation to learn more](https://docs.mattermost.com/install/install-ubuntu-1404.html#configuring-nginx-as-a-proxy-for-mattermost-server).
- If you are upgrading a High Availability Cluster: When upgrading from 3.10 or earlier to 4.0 or later, you must manually add new items to the *ClusterSettings* section of your existing ``config.json``. For more information about this, see the *Upgrading to Version 4.0 and Later* section of :doc:`../deployment/cluster`.
 - Microsoft Edge v39 and earlier (EdgeHTML v14 and earlier) has [an issue](https://developer.microsoft.com/en-us/microsoft-edge/platform/issues/8546263/) that may case errors during account creation, login and if MFA is enforced. We recommend upgrading to Edge v40 (or EdgeHTML v15).

#### Removed and deprecated features
- System Console settings in **Files > Images** removed. This includes:
  - Image preview height and width
  - Profile picture height and width
  - Image thumbnail height and width
- Font setting in Account Settings > Display removed.
- Account Settings option **Display** > **Teammate Name Display** moved to the System Console.
- All APIv3 endpoints are scheduled for removal on January 16, 2018.

For a list of past and upcoming deprecated features, [see our website](https://about.mattermost.com/deprecated-features/).

#### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

**Changes to Team Edition and Enterprise Edition**:

- Under `ServiceSettings` in `config.json`:
   - Added `"EnableEmojiPicker": true` to control whether emoji picker is enabled on the server. Enabling the emoji picker with a large number of custom emoji may slow down performance.
   - Added `"EnableChannelViewedMessages": true` to control whether `channel_viewed` WebSocket event is sent, which syncs unreads across clients and devices. Setting to false can lead to higher performance in large deployments.
   - Added `"EnableAPIv3": true` to control whether version 3 endpoints of the REST API are allowed on the server. If the setting is disabled, integrations that rely on API v3 will fail and can then be identified for migration to API v4.
- Under `TeamSettings` in `config.json`:
   - Added `"TeammateNameDisplay": "username"` to set how to display users' names in posts and the Direct Messages list. Deployments with LDAP or SAML enabled will have this set to `full_name` by default for better experience.
- Under `FileSettings` in `config.json`:
   - Removed System Console settings in **Files > Images**, including:
     - `"ThumbnailWidth": 120`
     - `"ThumbnailHeight": 100`
     - `"PreviewWidth": 1024`
     - `"PreviewHeight": 0`
     - `"ProfileWidth": 128`
     - `"ProfileHeight": 128`
- Under `SqlSettings` in `config.json`:
   - Modified `"QueryTimeout": 30` to also support query timeouts on PostgreSQL, in addition to MySQL.

**Additional Changes to Enterprise Edition**:

- Under `ClusterSettings` in `config.json`:
   - Added `"ClusterName": ""` to set the cluster to join by name. Only nodes with the same cluster name will join together. This is to support Blue-Green deployments or staging pointing to the same database.
   - Added `"OverrideHostname": ""` to override the hostname of this server with this property. It is not recommended to override the Hostname unless needed.
   - Added `"UseIpAddress": true` to control whether the cluster attempts to communicate using the IP Address.
   - Added `"UseExperimentalGossip": false` to control whether the server attempts to communicate via the gossip protocol over the gossip port.
   - Added `"ReadOnlyConfig": true` to control whether changes made to settings in the System Console are ignored. When running in production it is recommended to set this value to true.
   - Added `"GossipPort": 8074` to set the port used for the gossip protocol. Both UDP and TCP should be allowed on this port.
   - Added `"StreamingPort": 8075` to set the port used for streaming data between servers.
   - Removed ``"InterNodeListenAddress": ":8075"`` as this setting is no longer used.
   - Removed ``"InterNodeUrls": []`` as this setting is no longer used.

### API v4 Changes
- Mattermost 4.0 has a stable release of API v4 endpoints. It is recommended that any new integrations use the v4 endpoints. For more details, and for a complete list of available endpoints, see [https://api.mattermost.com/](https://api.mattermost.com/).
- All APIv3 endpoints are scheduled for removal on January 16, 2018.

**Added routes (API v4)**
- `GET` at `/teams/invite/{invite_id}`
  - To retrieve information about a team (including the name and id) corresponding to an invite_id.

**Modified routes (API v4)**
- `DELETE` at `/teams/{team_id}`
  - Added an optional query parameter, `permanent`, to permanently delete a team for compliance reasons.
- `GET` at `/users`
  - Added the `sort` query parameter to add basic sorting when selecting users on a team.
- `GET` at `/emoji`
  - Added paging to the `/emoji` call for increased performance.
- `POST` at `/teams/{team_id}/import`
   - Updated to return a JSON body with the import results under a `results` JSON field to allow more data to be returned in the future without breaking changes.

### Websocket Event Changes

**Added:**
- `channel_updated` that occurs each time channel information is updated (such as name or header), so that the changes are propagated across clients.
- `channel_viewed` that occurs each time you view a channel, propagating the event to all clients and devices and syncing unreads.

### Known Issues

- Google login fails on the Classic mobile apps.
- Edge overlays desktop notification sound and system notification sound.
- Clicking on a channel during the tutorial makes the tutorial disappear.
- User can receive a video call from another browser tab while already on a call.
- Search autocomplete picker is broken on Classic Android app.
- Jump link in search results does not always jump to display the expected post.
- First load of the emoji picker is slow on low-speed connections or on deployments with hundreds of custom emoji.
- Scrollbar is sometimes not visible in the left-hand sidebar after switching teams.
- Certain code block labels don't appear while scrolling on iOS mobile web.
- Outgoing webhooks do not fire when posts have no text content.
- A public channel doesn't always show up in another browser tab or client until after refresh.
- Null values in Slack attachments cause a 500 error for incoming webhooks.
- Keyboard shortcut CTRL/CMD+SHIFT+A does not close Account Settings.
- Deleted message doesn't clear unreads or unread mentions.
- Changing the search term in the More Direct Messages modal doesn't reset the page.
- Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
- Cannot delete or edit parent posts in right-hand side reply threads.
- Empty cells in Markdown tables render incorrectly.
- `platform user deleteall` CLI command expects a user as an argument.

### Contributors

Many thanks to all our contributors. In alphabetical order:

/mattermost-server

- [94117nl](https://github.com/94117nl), [abustany](https://github.com/abustany), [alexrford](https://github.com/alexrford), [asaadmahmood](https://github.com/asaadmahmood), [ccbrown](https://github.com/ccbrown), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [dmeza](https://github.com/dmeza), [enahum](https://github.com/enahum), [ftKnox](https://github.com/ftKnox), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [JeffSchering](https://github.com/JeffSchering), [jwilander](https://github.com/jwilander), [kkamdooong](https://github.com/kkamdooong), [lindalumitchell](https://github.com/lindalumitchell), [megos](https://github.com/megos), [meilon](https://github.com/meilon), [moonmeister](https://github.com/moonmeister), [pieterlexis](https://github.com/pieterlexis), [saturninoabril](https://github.com/saturninoabril), [VeraLyu](https://github.com/VeraLyu), [ZJvandeWeg](https://github.com/ZJvandeWeg)

/mattermost-mobile

- [asaadmahmood](https://github.com/asaadmahmood), [csduarte](https://github.com/csduarte), [enahum](https://github.com/enahum), [hmhealey](https://github.com/hmhealey), [lfbrock](https://github.com/lfbrock), [omar-dev](https://github.com/omar-dev)

/mattermost-redux

- [94117nl](https://github.com/94117nl), [csduarte](https://github.com/csduarte), [enahum](https://github.com/enahum), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [jarredwitt](https://github.com/jarredwitt), [jwilander](https://github.com/jwilander), [saturninoabril](https://github.com/saturninoabril)

/mattermost-api-reference

- [cpanato](https://github.com/cpanato), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [jasonblais](https://github.com/jasonblais), [jwilander](https://github.com/jwilander), [Vaelor](https://github.com/Vaelor), [ZJvandeWeg](https://github.com/ZJvandeWeg)

/docs

- [94117nl](https://github.com/94117nl), [acgustafson](https://github.com/acgustafson), [amyblais](https://github.com/amyblais), [ccbrown](https://github.com/ccbrown), [crspeller](https://github.com/crspeller), [esethna](https://github.com/esethna), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [JeffSchering](https://github.com/JeffSchering), [jwilander](https://github.com/jwilander), [kjkeane](https://github.com/kjkeane), [megos](https://github.com/megos), [pieterlexis](https://github.com/pieterlexis)

/desktop

- [yuya-oc](https://github.com/yuya-oc)

/mattermost-kubernetes

- [coreyhulen](https://github.com/coreyhulen)

/mattermost-push-proxy

- [coreyhulen](https://github.com/coreyhulen), [ftKnox](https://github.com/ftKnox)

/mattermost-docker

- [pichouk](https://github.com/pichouk), [tejasbubane](https://github.com/tejasbubane)

/mattermost-load-test

- [crspeller](https://github.com/crspeller), [JeffSchering](https://github.com/JeffSchering)

## Release v3.10.3

 - **v3.10.3, released 2017-08-18**
   - Mattermost v3.10.3 contains multiple security fixes ranging from low to high severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
   - Fixed issue when using single-sign-on with GitLab where using a non-English language option in **System Console > Localization** sometimes resulted in a login failure.
 - **v3.10.2, released 2017-07-18**
   - Mattermost v3.10.2 contains low severity security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v3.10.1, released 2017-07-16**
   - Mattermost v3.10.1 contains a high severity security fix for an OAuth SSO vulnerability and two additional fixes for low severity security issues. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v3.10.0, released 2017-06-16**
   - Original 3.10 release

### Highlights

#### Languages
- Added Turkish translations for the user interface.

#### New and Improved Keyboard Shortcuts
- Redesigned the channel switcher (CTRL/CMD+K) for increased productivity.
- Browse direct and group message channels (CTRL/CMD+SHIFT+K) and reply to the most recent message (SHIFT+UP) with new shortcuts.

### Improvements

#### Web User Interface
- Enter key now confirms deletion on the screens to delete a custom emoji and delete a channel.
- Team and channel URLs now replace accented characters with their ASCII equivalents.
- Recent mentions and flagged posts icons in the header are now highlighted when they are active in the right-hand sidebar.
- Empty rows are now ignored in the Send Email Invite modal.
- Enter key now confirms leaving a team from the Leave Team modal.
- Profile popover now opens when clicking a username in mobile browser view.
- /join now allows switching to a private channel to which the user has access.
- Improved the formatting of Mattermost content when copying and pasting to other apps.
- Added the ability for users to view and modify their online status from their profile picture in the header.
- /loadtest command changed to /test.
- Ephemeral messages are removed from the right-hand sidebar after it is reopened.
- Added a markdown preview option to the message editing modal.
- Status indicators are now shown in the Direct Messages list.

#### Notifications
- Added "@here" to the list of channel-wide mentions in Account Settings.
- Added a reminder when your Mattermost window is refreshed if a status override slash command is used to set yourself as /away or /offline.
- Users will see a confirmation dialog when attempting to use @all or @channel in a channel with over 5 users.
- Messages for others being added to a channel no longer trigger channels to be unread.

#### Administration
- Added CLI tool for permanently deleting channels.
- Channel Admins can now delete user's messages within their channel if permitted in the System Console.
- Errors are now logged when failing to load config through the command line.
- Reduced unnecessary database reads and writes when bulk importing users.

#### System Console
- System Console main dropdown menu now has links to the Admin Guide, Troubleshooting Forum, Commercial Support Page and the About Mattermost dialog.
- Added the ability to enable Legacy Signature (AWS Signature V2) with S3 compatible servers.

#### Authentication
- Added a redirect to the appropriate team, channel or post if navigating to a Mattermost URL when logged out.
- Clicking a team invite link now joins the team in all active sessions.

#### Performance
- Upgraded GORP to support connection timeouts on MySQL and missing database columns on MySQL and Postgres.

#### Integrations
- Posts from webhooks that are greater than 4000 characters are now broken into multiple posts.

#### Enterprise Edition
- Added an announcement banner visible to all end users to make maintenance announcements across the system.

### Bug Fixes
- Dragging and dropping a file onto the left-hand sidebar no longer navigates away from Mattermost to open the file in the browser.
- Textbox will no longer overlap the center pane message area as it expands when typing.
- Fixed an issue where statuses could get stuck online after quitting the desktop app or closing the browser window in some cases.
- Profile pictures uploaded on mobile are now rotated in their correct orientation.
- The System Console help text for Minimum Password Length no longer dynamically updates as the input is changed.
- Fixed an issue where the autocomplete list may appear underneath a modal overlay.
- Updated error text when uploading a profile picture that is in an unsupported image format.
- Joined channels no longer appear in the "More..." channels list.
- Wide markdown images no longer cause horizontal scrolling in the center pane.
- Fixed theme styling for button active states.
- Fixed an issue where channels sometimes did not appear read if the channel was in focus when a new message was received.
- Fixed an issue where the autocomplete list would not close after using a slash command.
- Removed the system warning message that appears if mentioning a user that is not a member of a group message.
- Fixed an issue where wide embedded images produce horizontal scroll.
- Fixed a Javascript error that would occur when opening the System Console > SAML page.
- Removed the Channel Admin user interface in Team Edition since the policy restrictions are only available in Enterprise Edition.
- Adding a reaction to an ephemeral message no longer throws a Javascript error.
- Fixed an issue where clicking autocomplete suggestions would not populate the search box with the appropriate text.
- Fixed an issue where the System Console users list ignored the search term after selecting a team from the filter.
- Channel header messages no longer appear cut-off if using a slash.
- Corrected the formatting of the "Edited" indicator in the right-hand sidebar.
- Fixed the positioning of the pin icon and channel header on Edge.

### Compatibility  

#### Removed and deprecated features
- System Console settings in **Files > Images** scheduled for removal in July 2017 release. This includes:
  - Image preview height and width
  - Profile picture height and width
  - Image thumbnail height and width
- Font setting in Account Settings > Display scheduled for removal in July 2017 release.
- Account Settings options for **Display** > **Display Font** and **Display** > **Teammate Name Display** are scheduled for removal in July 2017 release.
- All APIv3 endpoints are scheduled for removal six months after APIv4 is stable.

For a list of past and upcoming deprecated features, [see our website](https://about.mattermost.com/deprecated-features/).

#### config.json   

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

**Changes to Team Edition and Enterprise Edition**:
 - Under `ServiceSettings` in `config.json`:
   - Added `"GoroutineHealthThreshold": -1,` to set a threshold for number of goroutines.
- Under `SqlSettings` in `config.json`:
   - Added `"QueryTimeout": 30` to set the number of seconds to wait for a response from the database after opening a connection and sending the query.
- Under `FileSettings` in `config.json`:
   - Added `"AmazonS3SignV2": false` to enable Legacy Signature (AWS Signature V2) with S3 compatible servers.

**Additional Changes to Enterprise Edition**:
 - Under `AnnoucementSettings` in `config.json`:
   - Added `"EnableBanner": false,` to enable an announcement banner visible for all users.
   - Added `"BannerText": "",` to specify the text shown in the banner.
   - Added `"BannerColor": "#f2a93b",` to set the banner background color.
   - Added `"BannerTextColor": "#333333",` to set the banner text color.
   - Added `"AllowBannerDismissal": true` to set whether the banner can be dismissed by users.

### API Changes
- Mattermost 3.10 has a release candidate of APIv4 endpoints. To see the complete list of available endpoints, see [https://api.mattermost.com/v4/](https://api.mattermost.com/v4/).
- All APIv3 endpoints are scheduled for removal six months after APIv4 is stable.

**Modified routes (APIv4)**
- `/system/ping` updated to return `500 Internal Server Error` with `{"status": "unhealthy"}` in the response body when `GoroutineHealthThreshold` is set in config.json and the number of goroutines on the server exceeds that threshold. If the number of goroutines is below the threshold or `GoroutineHealthThreshold` is not set in config.json, `200 OK` is returned with no response body.

### Known Issues

- Google login fails on the mobile apps.
- Edge overlays desktop notification sound and system notification sound.
- Status appears offline briefly after joining a new team.
- User popover can get cropped in the center channel on iOS.
- Clicking on a channel during the tutorial makes the tutorial disappear.
- Custom emoji search results filter by the creator's first/last name in addition to the emoji name.
- Reactions are displayed on messages deleted by other users.
- User can receive a video call from another browser tab while already on a call.
- Search autocomplete picker is broken on Android.
- Jump link in search results does not always jump to display the expected post.
- First load of the emoji picker is slow on low-speed connections.
- Emoji picker for reactions doesn't always position correctly.
- Scrollbar is sometimes not visible in the left-hand sidebar after switching teams.
- New direct messages received while in no teams do not show as unread after joining a team.
- User is not logged out immediately when logging self out from Active Sessions list.
- Certain code block labels don't appear while scrolling on iOS mobile web.
- CTRL+SHIFT+K doesn't toggle modal open and closed.
- Deactivated users do not appear in the Direct Message and Group Message sidebar channel list.
- Outgoing webhooks do not fire when posts have no text content.

### Contributors

Many thanks to all our contributors. In alphabetical order:

/mattermost-server

- [asaadmahmood](https://github.com/asaadmahmood), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [dmeza](https://github.com/dmeza), [doh5](https://github.com/doh5), [enahum](https://github.com/enahum), [grundleborg](https://github.com/grundleborg), [harshavardhana](https://github.com/harshavardhana), [hmhealey](https://github.com/hmhealey), [jasonblais](https://github.com/jasonblais), [jwilander](https://github.com/jwilander), [kulak-at](https://github.com/kulak-at), [saturninoabril](https://github.com/saturninoabril), [tjuerge](https://github.com/tjuerge)

/docs

- [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [esethna](https://github.com/esethna), [hmhealey](https://github.com/hmhealey),  [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [JeffSchering](https://github.com/JeffSchering), [jwilander](https://github.com/jwilander), [kjkeane](https://github.com/kjkeane), [lindy65](https://github.com/lindy65), [mikedaniel18](https://github.com/MikeDaniel18)

/mattermost-api-reference

- [94117nl](https://github.com/94117nl), [cpanato](https://github.com/cpanato),  [hmhealey](https://github.com/hmhealey), [jwilander](https://github.com/jwilander), [senk](https://github.com/senk)

/mattermost-redux

- [94117nl](https://github.com/94117nl), [cpanato](https://github.com/cpanato), [enahum](https://github.com/enahum), [jarredwitt](https://github.com/jarredwitt), [jwilander](https://github.com/jwilander)

/mattermost-mobile

-  [asaadmahmood](https://github.com/asaadmahmood), [cpanato](https://github.com/cpanato), [csduarte](https://github.com/csduarte), [enahum](https://github.com/enahum), [hmhealey](https://github.com/hmhealey), [lfbrock](https://github.com/lfbrock), [rthill](https://github.com/rthill)

/desktop

- [yuya-oc](https://github.com/yuya-oc)

/mattermost-docker

- [carlosasj](https://github.com/carlosasj), [FingerLiu](https://github.com/FingerLiu), [mkdbns](https://github.com/mkdbns),  [pichouk](https://github.com/pichouk), [xcompass](https://github.com/xcompass)

/android

- [coreyhulen](https://github.com/coreyhulen), [der-test](https://github.com/der-test),  [lfbrock](https://github.com/lfbrock)

/mattermost-selenium

- [doh5](https://github.com/doh5),  [lindalumitchell](https://github.com/lindalumitchell)

/gorp

- [jwilander](https://github.com/jwilander)

/ios

- [coreyhulen](https://github.com/coreyhulen), [PrestonL](https://github.com/PrestonL)

/mattermost-kubernetes

- [coreyhulen](https://github.com/coreyhulen)

## Release v3.9.2

 - **v3.9.2, released 2017-07-18**
   - Mattermost v3.9.2 contains low severity security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v3.9.1, released 2017-07-16**
   - Mattermost v3.9.1 contains a high severity security fix for an OAuth SSO vulnerability and two additional fixes for low severity security issues. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v3.9.0, released 2017-05-16**
   - Original 3.9 release

### Security Update

- Mattermost v3.9.0 contains a low severity [security update](http://about.mattermost.com/security-updates/). [Upgrading to Mattermost v3.9.0](http://docs.mattermost.com/administration/upgrade.html) is highly recommended.

### Highlights

#### Languages

- Added Polish translations for the user interface.

#### Redux

- Mattermost Webapp moved over to Redux for increased performance and more stable infrustructure.

#### APIv4 Release Candidate

- Mattermost HTTP REST APIs moved to v4 endpoints allowing for more powerful integrations and server interaction.
- To learn more about the available APIv4 endpoints, [see our documentation](https://api.mattermost.com/v4/).
- APIv3 endpoints are supported until six months after the stable release of APIv4 endpoints in Q3 of 2017.

### Improvements

#### Web User Interface
- Lower and upper vertical margins for posts are now equal.
- Comments only containing a file attachment have a reduced vertical spacing in the center channel.
- First line of message text is now aligned with username.
- Added padding between timestamp and pinned posts badge in comment threads in compact view.
- Added "View Members" option to Town Square.
- Moved "Start Video Call" option to the bottom of the profile popover.
- Added a confirmation dialog when leaving a private channel.
- User preferences such as display settings now sync between browser tabs, between different browsers, and across devices.

#### Performance
- Added the ability to isolate searches to specific read-replicas for full text search queries for higher performance.
- Added default read and write timeouts for MySQL datasource to prevent hub processing deadlock.
- Added password field to the [bulk import tool](https://docs.mattermost.com/deployment/bulk-loading.html).
- Added the ability to disable full text search queries and statuses via `config.json` for higher performance.

#### Emoji Picker (Beta)
- Enable the emoji picker in **Account Settings > Advanced > Preview pre-release features**.
- Custom emoji now maintains aspect ratio in the emoji picker.
- Improved user experience for closing the Emoji picker after reacting to a message.

#### Keyboard Shortcuts
- Added a link to keyboard shortcuts documentation via the team Main Menu.
- Pressing ENTER once in the channel switcher (CTRL/CMD+K) now switches the channel.
- Using a mouse to select a channel in the channel switcher (CTRL/CMD+K) now switches to the correct channel.

#### Markdown Text Formatting
- Added a margin for Markdown inline images.
- Improved Markdown heading sizes in the desktop view.

#### On-Boarding
- Added "Already have an account? Click here to sign in" link to the sign up page.
- Improved experience of joining a team using an invite link.

#### Files
- SVG files now render in file preview.

#### CLI Tool
- Added new CLI commands:
    - `platform config validate` for validating the `config.json` file.
    - `platform user search` for searching users based on username, email, or user ID.

#### OAuth 2.0 Service Provider
- OAuth 2.0 service provider now always returns the refresh token.
- New refresh token now issued when granting a new access token.

#### System Console
 - Added a confirmation dialog when deactivating a user.
 - Server logs are now always printed in English regardless of Default Server Language, for easier troubelshooting.
 - The `AllowCorsFrom` config setting (in **System Console > Connections > Enable cross-origin requests from**) now supports multiple domain names.
 - Added a setting to disable file and image uploads on messages.

#### Enterprise Edition
 - Added new [performance monitoring metrics](https://docs.mattermost.com/deployment/metrics.html) for
     - The total number of connections to all the search replica databases
     - The total number of WebSocket broadcasts sent

### Bug Fixes
- Long custom emoji names no longer float out of the emoji picker.
- Deleted custom emojis no longer stay in "recently used" section of the emoji picker.
- The maximum length of the "Position" field increased to 64 characters in the database. The previous limit caused problems with LDAP synchronization.
- Pinning a post in center channel no longer changes pinned posts list in the right-hand sidebar.
- Pinning a post in center channel now adds the pinned post badge to search results.
- Fixed error message text for **Edit URL** field in channel creation dialog.
- Disabled config file watcher while running from makefile.
- Fixed Go client's `GetTeamByName()` function.
- Recent mentions search now properly includes `@[username]` in the search.
- Updated error message when entering a password longer than maximum number of characters.
- Don't send the same message multiple times when hitting "Retry" on a failed post.
- Fixed the help text for the channel purpose in private channels.
- When ability to change the header is restricted, "Set a Header" option is no longer shown in the channel intro.
- Mention notifications now trigger if the word is formatted in bold, italic or strikethrough, and won't if it's inside a code block.
- In mobile view, Manage Members menu option no longer reads "View Members" for channel admins.
- Usernames with dots now get mention notifications when followed by a comma or other symbol.
- Deactivated users are no longer listed in the "Manage Members" modal.
- Collapsible Account Setting menus now open properly in iOS Safari and Chrome browsers.
- Removing an expired license now removes the blue bar header message.
- "Next" button in More Channels list now takes you to the top of the next page, instead of the bottom.
- Blue bar "Preview Mode" header message now disappears after enabling email notifications.
- Full name is now editable in Account Settings if the first and last name attributes are not specified in **System Console > Authentication > LDAP**.
- Added a back button to pinned posts list on the right-hand sidebar.
- "Pinned" icon no longer overlaps text on consecutive posts or replies that have Markdown headings.
- Uploading a profile picture on iOS no longer throws an error.
- Fixed group message names in channel switcher (CTRL/CMD+K) for group messages that are not in your sidebar.
- Channel notification preferences no longer appear saved when clicking Cancel.
- Channel creation permissions aren't set to channel admins when it doesn't exist.

### Compatibility  

#### Breaking changes:

- If you're using NGINX as a proxy for the Mattermost Server, replace the `location /api/v3/users/websocket {` line with `location ~ /api/v[0-9]+/(users/)?websocket$ {` in the `/etc/nginx/sites-available/mattermost` NGINX configuration file. [See documentation to learn more](https://docs.mattermost.com/install/install-ubuntu-1404.html#configuring-nginx-as-a-proxy-for-mattermost-server).
- Existing email invite links, password reset links, and email verification links in emails generated by your Mattermost server will be invalidated after upgrading to v3.9.0.
- Firefox ESR 45 has an [end-of-life scheduled for June 13](https://en.wikipedia.org/wiki/Firefox_version_history) and is therefore no longer supported. We recommend upgrading to [Firefox ESR 52](https://www.mozilla.org/en-US/firefox/organizations/all/).

#### Removed and deprecated features
- System Console settings in **Files > Images** scheduled for removal in July 2017 release. This includes:
  - Image preview height and width
  - Profile picture height and width
  - Image thumbnail height and width
- All APIv3 endpoints are scheduled for removal six months after APIv4 is stable.

For a list of past and upcoming deprecated features, [see our website](https://about.mattermost.com/deprecated-features/).

#### config.json   

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

**Changes to Team Edition and Enterprise Edition**:

 - Under `ServiceSettings` in `config.json`:
   - Added `"EnablePostSearch": true` to control whether users can search messages. Disabling can lead to higher performance in large deployments.
   - Added `"EnableUserStatuses": true` to control whether user statuses are shown in the web user interface. Disabling can lead to higher performance in large deployments.
 - Under `FileSettings` in `config.json`:
   - Added `"EnableFileAttachments": true` to control whether users can upload files and images on messages.

 - Under `EmailSettings` in `config.json`:
   - Removed `"PasswordResetSalt": ""` given tokens are now used for signing of password reset emails.

 - Under `SqlSettings` in `config.json`:
   - Added `"DataSourceSearchReplicas": []` to specify the connection strings for search replica databases for handling search queries.

**Additional Changes to Enterprise Edition**:

 - Under `ServiceSettings` in `config.json`:
   - Added `"LicenseFileLocation": ""` to specify the path and filename of the Enterprise license file on disk. On startup, if Mattermost cannot find a valid license in the database from a previous upload, it will look for the file specified here.

### Database Changes

**OAuthAccessData Table:**
- Added `Scope` column

**PasswordRecovery Table:**
- Removed `PasswordRecovery` table and moved entries to a common token store

### API Changes

- Mattermost 3.9 has a release candidate of APIv4 endpoints. To see the complete list of available endpoints, see [https://api.mattermost.com/v4/](https://api.mattermost.com/v4/).
- All APIv3 endpoints to be removed six months after APIv4 endpoints are stable.

### Websocket Event Changes

- Added `preferences_changed` and `preferences_deleted` to sync preferences between browser tabs, between different browsers, and across devices when a preference is changed or deleted.

### Known Issues

- Google login fails on the mobile apps.
- Slack import doesn't add merged members/e-mail accounts to imported channels.
- User can receive a video call from another browser tab while already on a call.
- Sequential messages from the same user appear as separate posts on mobile view.
- Search autocomplete picker is broken on Android.
- Jump link in search results does not always jump to display the expected post.
- First load of the emoji picker is slow at low connections.
- Emoji picker for reactions doesn't always position correctly.
- Scrollbar is sometimes not visible in the left-hand sidebar after switching teams.
- Emoji picker is sometimes cut off on comment threads on the right-hand sidebar.
- User status can get stuck online after quitting the desktop app or closing the browser window.
- New direct messages received while in no teams do not show as unread after joining a team.
- Profile picture uploaded from mobile appears rotated.
- User is not logged out immediately when logging self out from Active Sessions list.
- Certain code block labels don't appear while scrolling on iOS mobile web.
- System Console user list filter does not show accurate results if applied after entering a search query.

### Contributors

Many thanks to all our contributors. In alphabetical order:

/mattermost-server

- [asaadmahmood](https://github.com/asaadmahmood), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [doh5](https://github.com/doh5), [enahum](https://github.com/enahum), [grundleborg](https://github.com/grundleborg), [gstraube](https://github.com/gstraube) , [hmhealey](https://github.com/hmhealey), [jasonblais](https://github.com/jasonblais), [JeffSchering](https://github.com/JeffSchering), [justinwyer](https://github.com/justinwyer), [jwilander](https://github.com/jwilander), [lindalumitchell](https://github.com/lindalumitchell), [prixone](https://github.com/prixone), [Rudloff](https://github.com/Rudloff), [R-Wang97](https://github.com/R-Wang97), [saturninoabril](https://github.com/saturninoabril), [simon0191](https://github.com/simon0191), [VeraLyu](https://github.com/VeraLyu)

/docs

- [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [fjarlq](https://github.com/fjarlq), [it33](https://github.com/it33), [ivernus](https://github.com/ivernus), [jasonblais](https://github.com/jasonblais), [JeffSchering](https://github.com/JeffSchering), [justinwyer](https://github.com/justinwyer), [lindy65](https://github.com/lindy65), [senk](https://github.com/senk)

/mattermost-api-reference

- [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [dagit](https://github.com/dagit), [hmhealey](https://github.com/hmhealey), [jwilander](https://github.com/jwilander), [saturninoabril](https://github.com/saturninoabril)

/mattermost-redux

- [enahum](https://github.com/enahum), [jarredwitt](https://github.com/jarredwitt), [jwilander](https://github.com/jwilander)

/desktop

- [jasonblais](https://github.com/jasonblais), [jnugh](https://github.com/jnugh), [yuya-oc](https://github.com/yuya-oc)

/mattermost-mobile

- [asaadmahmood](https://github.com/asaadmahmood), [cpanato](https://github.com/cpanato), [csduarte](https://github.com/csduarte), [enahum](https://github.com/enahum), [jasonblais](https://github.com/jasonblais), [lfbrock](https://github.com/lfbrock)

/mattermost-docker

- [esethna](https://github.com/esethna), [pichouk](https://github.com/pichouk), [xcompass](https://github.com/xcompass)

/mattermost-push-proxy

- [coreyhulen](https://github.com/coreyhulen)

/mattermost-selenium

- [doh5](https://github.com/doh5), [lindalumitchell](https://github.com/lindalumitchell), [coreyhulen](https://github.com/)

/mattermost-kubernetes

- [coreyhulen](https://github.com/coreyhulen)

/gcm

- [coreyhulen](https://github.com/coreyhulen), [csduarte](https://github.com/csduarte)

## Release v3.8.3

### Notes on Patch Release

 - **v3.8.3, released 2017-07-16**
   - Mattermost v3.8.3 contains a high severity security fix for an OAuth SSO vulnerability and two additional fixes for low severity security issues. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v3.8.2, released 2017-04-21**
   - Changed the client to use `window.location.origin` instead of siteURL, fixing WebSocket connection issues with Mattermost 3.8 upgrade.
   - Fixed a few APIv4 endpoints in support of the next [React Native mobile app](https://github.com/mattermost/mattermost-mobile) release.
 - **v3.8.1, released 2017-04-19**
   - Mattermost v3.8.1 contains a security update and [upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
   - Fixed an issue with Site URL sometimes breaking the OAuth2 login flow, including login using GitLab.
   - Reverted a change preventing LDAP usernames from beginning with a number.
   - Fixed a permission issue with group message channel creation.
 - **v3.8.0, released 2017-04-16**
   - Original 3.8 release

### Security Update

- Mattermost v3.8.0 contains multiple [security updates](http://about.mattermost.com/security-updates/). [Upgrading to Mattermost v3.8.0](http://docs.mattermost.com/administration/upgrade.html) is highly recommended.

### Highlights

#### Native iOS and Android Apps (Beta)
- Second generation mobile apps, built using React Native, are [available for beta testing](https://about.mattermost.com/a-native-mobile-experience-second-generation-mobile-apps-released-in-beta/) on [iOS](https://mattermost-fastlane.herokuapp.com/) and [Android](https://play.google.com/apps/testing/com.mattermost.react.native).

#### Pinned Posts
- Important messages can be pinned to the channel for easy reference. Pinned posts are visible to all channel members.

#### Emoji Picker and Improved Emoji Reactions (Beta)
- The picker offers quick access to emoji when composing messages or adding reactions. Enable the emoji picker in **Account Settings > Advanced > Preview pre-release features**.
- The picker is "Beta" while speed of the first load with lots of custom emoji is improved.

#### System Users List
- The System Console now consolidates all users into a system-wide list that can be filtered by team. The users list can be used to manage team membership and team roles for any user on the system.

#### Configure Using Environment Variables
- Override `config.json` settings using environment variables.

### Improvements

#### Web User Interface
- Date separators now appear between posts in the right-hand sidebar.
- Non-square profile pictures are now cropped in the middle rather than being stretched.
- Post timestamps now have an expanded date tooltip.
- The "Add Members" modal now autofocuses on the search box when opened from the "Manage Members" modal.
- Reduced the margins and line height in compact view.
- There is now a confirmation dialog before deleting a custom emoji.
- Updated the error page for invalid permalinks.
- Updated the error page for "Private browsing not supported" in Safari.

#### Performance
- Added index and cache to reactions store

#### Search
- File attachments thumbnails are now shown in search results.
- Flagged posts from other teams are no longer displayed.

#### Channels
- Favorite channels are now sorted alphabetically regardless of channel type.
- Town Square now has a default channel purpose.
- Users added to a group message are now removed from the Direct Messages search list.
- "Private Groups" have been renamed to "Private Channels".

#### Mobile
- Executing a search now closes the keyboard and removes the keyboard focus from the text box.

#### Integrations
- The integrations confirmation page can now be dismissed with the ENTER key.

#### Link Previews
- Updated the UI for link previews by removing an extra blue vertical bar.
- Added support for link preview requests through a separate proxy.

#### Notifications
- Users can no longer configure email notification settings if the notifications are disabled for the system.

#### Onboarding
- Existing users on the server can now easily be added to a team via the Main Menu.

#### Enterprise Edition
- Policy controls for restricting permissions to add and remove members from private channels.
- Added the ability to read the license file from the disk.
- The configuration file is now reloaded after applying an Enterprise Edition license on startup.

### Bug Fixes
- Fixed line wrapping of the timestamp in Account Settings > Security > View Access History.
- Fixed an inconsistent error message when creating a channel with a display name of one or two characters.
- Removed the duplicate "Back" button on the Team Creation page.
- The AltGR key no longer triggers keyboard shortcuts.
- Saving a team name without making changes no longer throws an error message.
- Group messages are now sorted alphabetically with direct messages.
- The "Create Channel" button will now only appear in the "More Channels" modal when the user has the permission to create channels.
- The Town Square channel menu no longer has redundant dividers with certain combinations of System Console > Policy settings.
- Fixed an issue where some conversations would not trigger the channel to appear unread in the left-hand sidebar.
- Fixed an issue where usernames sometimes did not appear when hovering over reactions.
- Fixed an issue where link previews would sometimes cause a horizontal scroll bar to appear.
- iOS code blocks no longer wrap to the next line.
- Removed an extra border in Markdown tables on iOS.
- Usernames in the channel member list are now properly aligned.
- Fixed a console error that was thrown when switching teams.
- Fixed occasionial flickering of channel autocomplete.
- Link preview images no longer appear outside of the preview container.

### Compatibility  

#### Breaking changes:
- The **System Console > Configuration > [Site URL](../../administration/config-settings.html#site-url)** field is now mandatory. Set the Site URL in the System Console, or in the `gitlab.rb` file if you are using GitLab Mattermost.
- Server logs are now written to the `mattermost.log` file located in the directory specified in **System Console > Logging > [File Log Directory](../../administration/config-settings.html#file-log-directory)**. Set the directory name in the System Console, or in the `gitlab.rb` file if you are using GitLab Mattermost.

#### Removed and deprecated features
- Backwards compatibility with the old CLI tool is removed in v3.8. See [documentation to learn more about the new CLI tool](../../administration/command-line-tools.html).
- Deprecated APIv3 routes removed in v3.8:
   - `GET` at `/channels/more` (replaced by /`channels/more/{offset}/{limit}`)
   - `POST` at `/channels/update_last_viewed_at` (replaced by `/channels/view`)
   - `POST` at `/channels/set_last_viewed_at` (replaced by `/channels/view`)
   - `POST` at `/users/status/set_active_channel` (replaced by `/channels/view`)
- All APIv3 endpoints to be removed six months after APIv4 goes stable (replaced by APIv4 endpoints).

For a list of past and upcoming deprecated features, [see our website](https://about.mattermost.com/deprecated-features/).

#### config.json   

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json` or the System Console.

**Changes to Team Edition and Enterprise Edition**:

 - Under `EmailSettings` in `config.json`:
   - Added `"SkipServerCertificateVerification": false` to skip verification of smtp server certificates.

**Additional Changes to Enterprise Edition**:

 - Under `TeamSettings` in `config.json`:
   - Added `"RestrictPrivateChannelManageMembers": all` to set who can add and remove members from private groups.

### Database Changes

**Posts Table:**
- Added `IsPinned` column

### API Changes

**New routes (APIv3):**
- `GET` at `/channels/{channel_id}/pinned`
  - Returns the pinned posts in a channel
- `POST` at `/channels/{channel_id}/posts/{post_id}/pin`
  - Pins a post to a channel
- `POST` at `/channels/{channel_id}/posts/{post_id}/unpin`
  - Unpins a post from a channel

**Removed routes (APIv3):**
- `GET` at `/channels/more` (replaced by /`channels/more/{offset}/{limit}`)
- `POST` at `/channels/update_last_viewed_at` (replaced by `/channels/view`)
- `POST` at `/channels/set_last_viewed_at` (replaced by `/channels/view`)
- `POST` at `/users/status/set_active_channel` (replaced by `/channels/view`)

### Websocket Event Changes

**Added:**
- `added_to_team` that occurs when the current user is added to a team by another user.

**Modified**
- Added a `seq` field to websocket events that increments with each event sent to the client.

### Known Issues

- "Pinned" icon sometimes overlaps image posts.
- Full name is not editable in Account Settings if the first and last name attributes are removed from **System Console > Authentication > LDAP**.
- Usernames with dots do not get mention notifications when followed by a comma.
- Slack import doesn't add merged members/e-mail accounts to imported channels.
- User can receive a video call from another browser tab while already on a call.
- Sequential messages from the same user appear as separate posts on mobile view.
- Search autocomplete picker is broken on Android.
- Jump link in search results does not always jump to display the expected post.
- Blue bar "Preview Mode" header message sometimes does not disappear after enabling email notifications.
- Removing an expired license may not remove the blue bar header message until a refresh.
- First load of the emoji picker is slow at low connections.
- Emoji picker for reactions doesn't always position correctly.
- Deleted custom emoji stay in "recently used" section of the emoji picker.
- Scrollbar is sometimes not visible in the left-hand sidebar after switching teams.

### Contributors

Many thanks to all our contributors. In alphabetical order:

/mattermost-server:

- [aautio](https://github.com/aautio), [asaadmahmood](https://github.com/asaadmahmood), [bonespiked](https://github.com/bonespiked), [bradhowes](https://github.com/bradhowes), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [doh5](https://github.com/doh5), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [jasonblais](https://github.com/jasonblais), [JeffSchering](https://github.com/JeffSchering), [jostyee](https://github.com/jostyee), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [lindalumitchell](https://github.com/lindalumitchell), [prixone](https://github.com/prixone), [R-Wang97](https://github.com/R-Wang97), [saturninoabril](https://github.com/saturninoabril), [VeraLyu](https://github.com/VeraLyu)

/docs:

- [coreyhulen](https://github.com/coreyhulen), [esethna](https://github.com/esethna), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [JeffSchering](https://github.com/JeffSchering), [jwilander](https://github.com/jwilander), [lindy65](https://github.com/lindy65), [Rohlik](https://github.com/Rohlik)

/mattermost-redux:

- [enahum](https://github.com/enahum), [hmhealey](https://github.com/hmhealey), [jarredwitt](https://github.com/jarredwitt), [jwilander](https://github.com/jwilander)

/mattermost-api-reference:

- [cpanato](https://github.com/cpanato), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [jwilander](https://github.com/jwilander), [saturninoabril](https://github.com/saturninoabril), [senk](https://github.com/senk)

/mattermost-mobile:

- [csduarte](https://github.com/csduarte), [enahum](https://github.com/enahum), [hmhealey](https://github.com/hmhealey), [jasonblais](https://github.com/jasonblais), [JeffSchering](https://github.com/JeffSchering), [lfbrock](https://github.com/lfbrock), [saturninoabril](https://github.com/saturninoabril)

/mattermost-selenium:

- [coreyhulen](https://github.com/coreyhulen), [lindalumitchell](https://github.com/lindalumitchell)

/desktop:

- [jasonblais](https://github.com/jasonblais), [yuya-oc](https://github.com/yuya-oc)

/mattermost-docker:

- [xcompass](https://github.com/xcompass)

/mattermost-kubernetes:

- [coreyhulen](https://github.com/coreyhulen)

/mattermost-load-test:

- [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte)


## Release v3.7.5

### Notes on Patch Release

 - **v3.7.5, released 2017-04-27**
   - Fixed a number of low to moderate severity security issues, and [upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/)
     - Note: The **System Console > Configuration > [Site URL](../../administration/config-settings.html#site-url)** field is now mandatory. Set the Site URL in the System Console, or in the `gitlab.rb` file if you are using GitLab Mattermost.
 - **v3.7.4, released 2017-04-13**
   - Fixed a number of low to high severity security issues, and [upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/)
 - **v3.7.3, released 2017-03-23**
   - Fixed a high severity security issue, and [upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/)
   - Fixed an issue with telemetry data collection
 - **v3.7.2, released 2017-03-17**
   - Fixed an issue with LDAP, SAML, and OAuth logins where 1 and 2 character usernames displayed incorrectly
 - **v3.7.1, released 2017-03-16**
   - Fixed an issue where some [System Console > Policy settings](https://docs.mattermost.com/administration/config-settings.html#policy) were incorrectly applied to Team Edition, breaking the System Console UI
 - **v3.7.0, released 2017-03-16**
   - Original 3.7 release

### Security Update

- Mattermost v3.7.0 contains a [security update](http://about.mattermost.com/security-updates/). [Upgrading to Mattermost v3.7.0](http://docs.mattermost.com/administration/upgrade.html) is highly recommended.

### Highlights

#### Group Messaging

- Added support for multi-party direct messages, you can now quickly create conversations with a small group of people directly from the Direct Message list

#### Channel Push Notification Preferences

- Added channel notification preferences for mobile push to customize your notification settings

#### New Website Link Previews

- Improved display of link previews for website content when available, replacing the previous preview feature that handled only a subset of links

#### Bulk User Import Tool

- Convert your existing data into our new import format, and use this tool to import teams, channels, users and posts from other systems

#### Channel Admins ([Enterprise E10 & E20](https://about.mattermost.com/pricing/))

- Added a new "Channel Admin" role to grant permissions for renaming and deleting a channel

#### SAML OneLogin ([Enterprise E20](https://about.mattermost.com/pricing/))

- Added support for OneLogin authentication and account creation via SAML 2.0.

### Improvements

#### Performance

- Loading new users can now be run on a live system without a major impact on performance through the new bulk user import tool
- Optimized SQL queries by adding index for PostId, removing ParentId from delete post queries, and fixing blank post queries
- Increased performance for "user typing..." messages by moving the check from server to client
- Increased performance for direct message channels by removing `MakeDirectChannelVisible` call and adding client handling
- Moved channel permission checks back to using cache
- Added caching for emoji, file info, profile images and website link previews
- Adding index and caching to reactions
- Increased performance when receiving messages by
    - removing the `viewChannel` requests when receiving a new post and only marking the channel as read when switching into it, out of it or when closing the app
    - removing the `view_channel` websocket event from the server
    - removing the `getChannel` and `getTeamUnreads` requests when receiving a new post
    - adding client handling for marking channels and teams unread
    - adding `getMyChannelMembers` request to web app when window becomes active after ten seconds
- Increased time between database recycles
- Improved mobile push proxy connections by disabling keep-alives
- Fixed Minio not properly closing read objects
- Fixed file info caching and emoji reaction issues on Aurora read replicas
- Added reloading, removing and uploading of Enterprise license key to cache purge

#### Web User Interface

- Update status indicators shown in post view
- Show `(Edited)` indicator if a message has been edited
- `(message deleted)` placeholder is no longer shown to the user that deleted the message
- Added a link to Manage Members modal from channel members list
- Added support for image previews if the URL contains a custom query
- Added support for all timecode formats for YouTube previews
- System message is now posted after changing channel purpose
- Reinstated the delete option on system messages
- Clicking on timestamps on messages now open a permalink view
- Removed new lines for system messages posted after updating channel header
- Focus is set back to message box after uploading a file
- Added machine-readable date and time to timestamps
- Adjusted tablet view so the browser URL bar doesn't overlap the message box
- Channel header can now be up to 1024 characters long
- Changed custom theme vector to a list of name value pairs to more easily add new theme colours

#### Mobile

- New push proxy server supports multiple apps (in preparation for the second generation mobile apps)
- New push proxy server is backwards compatible with the old iOS and Android apps
- Unread channels on the channel view are indicated with a red dot, and unread mentions with a red dot and mention count
- Added floating timestamp to mobile right hand side
- Send icon is disabled for messages and comments until a valid message is typed
- Removed redundant search hint popover and updated search buttons
- Removed "@"-symbol preceeding usernames and full names in push notifications

#### Text Formatting

- Added support for explicit image sizes in markdown
- Terms such as `_AAA_BBB_` now italicize correctly
- First backslash is now truncated when posting file paths that start with `\\`
- Markdown isn't rendered for system messages posted after renaming a channel
- Messages beginning with `[some_text]: some_text` now longer post as blank space
- Pipe characters (`|`) in a Markdown table now work

#### Integrations

- Added edit screens for incoming and outgoing webhooks
- When no username is set for a slash command response, the username of the person is now used instead of "webhook"
- Added a confirmation dialog to prevent accidentally deleting an integration

#### Localization

- System messages are now localized based on language set in the Account Settings

#### Onboarding

- Clicking on email verification link now automatically fills in your email address on the sign in page
- On login with GitLab SSO, Mattermost username and email are now synced with GitLab username and email

#### Slack Import

- Added support for Slack's Markdown-like post formatting
- Added support for topic & purpose system messages
- Channels imported from Slack with the same name as a deleted channel now import successfully
- Added support for users who don't have a non-empty email address in Slack

#### System Console

- Added active users statistics to Site Statistics page
- Focus is set to server log control in **System Console > Reporting > Logs** when loading the panel

#### Enterprise Edition

- Added WebSocket events, webhook events and cluster request time logging for Performance Monitoring
- Added new policy settings to **System Console > General > Policy** to
   - restrict who can delete messages
   - restrict whether messages can be edited and for how long

### Bug Fixes

- Fixed an error where a channel would no longer load after using a GitLab built-in Mattermost slash command `/project issue show <number>`
- Outdated results in modal searches are now properly discarded
- Fixed order of channels on the sidebar
- Fixed search highlighting for wildcard searches and hashtags
- Clicking "Send message" link in profile popover in a comment thread, now properly opens the direct message channel
- Fixed channels missing from "More Channels" modal after leaving them
- Fixed webhook messages not appearing in channels the creator wasn't in
- Angled brackets around mailto links now longer autolink
- Fixed an issue where "New messages below" bubble didn't disappear properly on mobile view
- Fixed CLI panic on `platform channel create` command if team does not exist
- Team invite link now directs user to a private team after account creation with LDAP
- `Create a New Team` menu option is now in the Main Menu for System Admins when team creation is disabled
- Fixed the response for malformed command execute request
- New message indicator no longer appears for ephemeral posts
- Fixed emoji aliases not showing up in autocomplete
- Mention badge now properly updates on the team sidebar when switching teams
- (at)-mention preceeded by a "#"-symbol now displays correctly
- Don't allow APIs to create user accounts that start with a number preventing them from signing in
- Using a mouse to choose an emoji from the autocomplete now works
- Fixed syntax highlighting on mobile
- Fixed inconsistent styling of file uploads between mobile and desktop
- Push notifications are no longer missing username when preferences set to "For all activity"
- Fixed a bug where the Go driver was using a wrong URL for `/users/claim/email_to_oauth` route

### Compatibility  

#### Removed and deprecated features

 - Removed `ServiceSettings: "SegmentDeveloperKey"` setting in `config.json`
 - Backwards compatibility with the old CLI tool will be removed in Mattermost v3.8 April/2017 release. See [documentation to learn more about the new CLI tool](https://docs.mattermost.com/administration/command-line-tools.html).
 - Deprecated APIv3 routes to be removed in Mattermost v3.8 April/2017 release:
   - `GET` at `/channels/more` (replaced by /`channels/more/{offset}/{limit}`)
   - `POST` at `/channels/update_last_viewed_at` (replaced by `/channels/view`)
   - `POST` at `/channels/set_last_viewed_at` (replaced by `/channels/view`)
   - `POST` at `/users/status/set_active_channel` (replaced by `/channels/view`)
 - All APIv3 endpoints to be removed six months after APIv4 goes stable (replaced by APIv4 endpoints).)

For a list of past and upcoming deprecated features, [see our website](https://about.mattermost.com/deprecated-features/).

#### config.json   

Changes from v3.6 to v3.7:

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json` or the System Console.

**Changes to Team Edition and Enterprise Edition**:

 - Under `ServiceSettings` in `config.json`:
   - Added `"TimeBetweenUserTypingUpdatesMilliseconds": 5000` to control how frequently the "user is typing..." messages are updated
   - Added `"EnableUserTypingMessages": true` to control whether "user is typing..." messages are displayed below the message box
   - Added `"EnableLinkPreviews": false` to control whether a preview of website content is displayed below the message

**Additional Changes to Enterprise Edition**:

 - Under `ServiceSettings` in `config.json`:
   - Added `"RestrictPostDelete": all` to set who can delete messages
   - Added `"AllowEditPost": always` to set whether messages can be edited
   - Added `"PostEditTimeLimit": 300` to set how long messages can be edited, if `"AllowEditPost": time_limit` is specified
   - Added `"ClusterLogTimeoutMilliseconds": 2000` to control frequency of cluster request time logging for [performance monitoring](https://docs.mattermost.com/deployment/metrics.html)

### Database Changes from v3.6 to v3.7

**Posts Table:**
- Added `EditAt` column

### API Changes from v3.6 to v3.7

**New routes (APIv3):**
- `POST` at `/channels/create_group`
  - Creates a new group message channel
- `POST` at `/hooks/incoming/update`
  - Updates an incoming webhook
- `POST` at `/hooks/outgoing/update`
  - Updates an outgoing webhook
- `GET` at `/teams/{team_id}/...`
  - Returns a post list, based on the provided channel and post ID.
- `POST` at `/channels/{channel_id}/update_member_roles`
  - Updates the user's roles in a channel

### Websocket Event Changes from v3.6 to v3.7

**Added:**
- `channel_create` that occurs each time a channel is created
- `group_added` that occures when a new group message channel is created

**Removed:**
- `view_channel` that occurred when a new message was received

### Known Issues

- Slack import doesn't add merged members/e-mail accounts to imported channels
- User can receive a video call from another browser tab while already on a call
- Sequential messages from the same user appear as separate posts on mobile view
- Edge overlays desktop notification sound with system notification sound
- Search autocomplete picker is broken on Android
- Jump link in search results does not always jump to display the expected post
- Running CLI without access to logs causes panic
- Switching channels with CTRL/CMD+K doesn't work properly when using the mouse
- Reacting to a deleted message in the right-hand sidebar throws an error
- Sometimes no email verification is sent to the new email address after changing your email in Account Settings. A workaround is to sign in with the new email address and hitting "Resend Email" on the "Email not verified" page
- Clicking "Load more messages" sometimes brings you to the bottom of the page
- Switching to a channel with unreads sometimes doesn't jump to the correct scrolling position

### Contributors

Many thanks to all our contributors. In alphabetical order:

/mattermost-server

- [aautio](https://github.com/aautio), [akihikodaki](https://github.com/akihikodaki), [andreistanciu24](https://github.com/andreistanciu24), [asaadmahmood](https://github.com/asaadmahmood), [ayadav](https://github.com/ayadav), [AymaneKhouaji](https://github.com/AymaneKhouaji), [bjoernr-de](https://github.com/bjoernr-de), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [CrEaK](https://github.com/CrEaK), [crspeller](https://github.com/crspeller), [DavidLu1997](https://github.com/DavidLu1997), [debanshuk](https://github.com/debanshuk), [enahum](https://github.com/enahum), [erikgui](https://github.com/erikgui), [favadi](https://github.com/favadi), [gig177](https://github.com/gig177), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jazzzz](https://github.com/jazzzz), [JeffSchering](https://github.com/JeffSchering), [joannekoong](https://github.com/joannekoong), [jostyee](https://github.com/jostyee), [jurgenhaas](https://github.com/jurgenhaas), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [khawerrind](https://github.com/khawerrind), [laur89](https://github.com/laur89), [lfbrock](https://github.com/lfbrock), [mikaoelitiana](https://github.com/mikaoelitiana), [morenoh149](https://github.com/morenoh149), [mpoornima](https://github.com/mpoornima), [pan-feng](https://github.com/pan-feng), [pepf](https://github.com/pepf), [Rudloff](https://github.com/Rudloff), [ruzette](https://github.com/ruzette), [saturninoabril](https://github.com/saturninoabril), [senk](https://github.com/senk), [Zaicon](https://github.com/Zaicon), [ZJvandeWeg](https://github.com/ZJvandeWeg)

/api-reference

- [debanshuk](https://github.com/debanshuk), [enahum](https://github.com/enahum), [jwilander](https://github.com/jwilander), [ruzette](https://github.com/ruzette), [Zaicon](https://github.com/Zaicon)

/docs

- [asaadmahmood](https://github.com/asaadmahmood), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [esethna](https://github.com/esethna), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [ilabdsf](https://github.com/ilabdsf), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [JeffSchering](https://github.com/JeffSchering), [jostyee](https://github.com/jostyee), [jwilander](https://github.com/jwilander), [lfbrock](https://github.com/lfbrock), [lindy65](https://github.com/lindy65), [matmorel](https://github.com/matmorel), [senk](https://github.com/senk), [vladimirprieto](https://github.com/vladimirprieto), [wget](https://github.com/wget)

/mobile

- [asaadmahmood](https://github.com/asaadmahmood), [csduarte](https://github.com/csduarte), [enahum](https://github.com/enahum), [hmhealey](https://github.com/hmhealey), [jasonblais](https://github.com/jasonblais), [lfbrock](https://github.com/lfbrock)

/docker

- [darkrasid](https://github.com/darkrasid), [nikosch86](https://github.com/nikosch86), [xcompass](https://github.com/xcompass)

/desktop

- [asaadmahmood](https://github.com/asaadmahmood), [jasonblais](https://github.com/jasonblais), [jnugh](https://github.com/jnugh), [yuya-oc](https://github.com/yuya-oc)

/selenium

- [coreyhulen](https://github.com/coreyhulen), [esethna](https://github.com/esethna), [lindalumitchell](https://github.com/lindalumitchell)

/push-proxy

- [coreyhulen](https://github.com/coreyhulen), [jostyee](https://github.com/jostyee), [it33](https://github.com/it33)

/load-test

- [coreyhulen](https://github.com/coreyhulen), [crspeller](https://github.com/crspeller)

## Release v3.6.7

### Notes on Patch Release

 - **v3.6.7, released 2017-04-27**
   - Fixed a number of low to moderate severity security issues, and [upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/)
     - Note: The **System Console > Configuration > [Site URL](../../administration/config-settings.html#site-url)** field is now mandatory. Set the Site URL in the System Console, or in the `gitlab.rb` file if you are using GitLab Mattermost.
 - **v3.6.6, released 2017-04-13**
   - Fixed a number of low to high severity security issues, and [upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/)
   - Fixed an issue where Direct Messages list didn't always properly update in the left-hand sidebar
   - Upgraded MySQL driver for better performance
 - **v3.6.5, released 2017-03-23**
   - Fixed a high severity security issue, and [upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/)
 - **v3.6.4, released 2017-03-16**
   - Fixed an issue where some [System Console > Policy settings](https://docs.mattermost.com/administration/config-settings.html#policy) were incorrectly applied to Team Edition, breaking the System Console UI
 - **v3.6.3, released 2017-03-16**
   - Fixed a security issue, and [upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/)
 - **v3.6.2, released 2017-01-31**
   - Fixed a high severity security issue, and [upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/)
   - Improved performance of web sockets and typing messages
   - Note: Some deployments using multiple URLs to reach Mattermost via proxy forwarding are reporting issues with the security fix in 3.6.2. [The issue is being tracked in our ticketing system](https://mattermost.atlassian.net/browse/PLT-5635).
 - **v3.6.1, released 2017-01-19**
   - Fixed a performance regression when sending many notifications at once (for example, when `@all` or `@channel` is used in a channel with many users)
   - Fixed an issue where the config flag for the CLI was not backwards compatible
   - Fixed an upgrade issue where for some databases, the Team Description index was not created properly
   - Fixed an issue with messages not showing up after computer wakes from sleep
 - **v3.6.0, released 2017-01-16**
   - Original 3.6 release.

### Security Update

- Mattermost v3.6.0 contains a [security update](http://about.mattermost.com/security-updates/). [Upgrading to Mattermost v3.6.0](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Thanks to Julien Ahrens for contributing the security report through the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Highlights

#### Team Sidebar
- Added a new sidebar on left-hand side to improve cross-team notifications and team switching
- New sidebar improves user experience on the [Mattermost Desktop Apps](https://about.mattermost.com/downloads/) when engaging with multiple teams

#### MFA Enforcement ([Enterprise E10 & E20](https://about.mattermost.com/pricing/))
- Added support for MFA Enforcement. When set to true, all users with email or LDAP authentication are required to set up MFA for their accounts

#### Performance Monitoring ([Enterprise E20](https://about.mattermost.com/pricing/))
- Added support for performance monitoring in large-scale deployments to help optimize systems for maximum performance using integrations with [Prometheus](https://github.com/prometheus/prometheus) and [Grafana](http://grafana.org/)
- Includes metrics for caching, database connections, processing, logins and messaging. See [documentation to learn more](https://docs.mattermost.com/deployment/metrics.html)

#### Improved Command Line Interface
- New version of CLI with a more intuitive interface, interactive help documentation, and some added functionality. See [documentation to learn more](https://docs.mattermost.com/administration/command-line-tools.html)

### Improvements

#### Performance
- Added server-based channel autocomplete, search and paging
- Reduced lag on channel switcher (CTRL/CMD+K) and at-mention autocomplete
- Improved on-boarding performance by removing new user event handling on the client
- Improved channel switching performance by combining API events and only pulling user statuses the client doesn't yet have
- Added session cache directly to web connections
- Added caching for files, user profiles and for the last 60 posts in a channel
- Added ETag for user profile pictures and modified ETag for posts to improve caching validation
- Added caching to post and channel calls
- Fixed channel cache not being sent to a cluster
- Added a configuration setting to disable intensive System Console statistics queries for maximum performance ([Enterprise E10 & E20 only](https://about.mattermost.com/pricing/))

#### Notifications
- Desktop notifications no longer appear for the channel you are actively viewing
- Push and email notifications now follow the setting for Teammate Name Display
- Notifications for @mentions of your username can no longer be turned off

#### Account Settings
- Added a "Position" field, where users can add a job title to be shown in their profile popover

#### Team Settings
- Team description can be set by a Team Admin and is visible to all users on the join teams screen and in the tool tip over the team name
- Slack Import can now import integration messages

#### Slash Commands
- Existing slash commands can now be edited by the creator or by Team and System Admins
- Slash commands now work on the right-hand sidebar
- Added support for slash commands to set the username and icon directly from the reply payload

#### Channels
- System message is now posted for all users when a channel or group is renamed
- Any channel member can now remove other users from the channel

#### Messaging
- Added support for non-alphanumeric unicode characters in hashtags
- Custom Emojis larger than 64kB can now be uploaded and they will be appropriately resized

#### User Interface
- Added a direct message link to the profile popover
- Added an indicator to convey a new message is received when scrolled up in the center pane
- Removed status indicators on posts by webhooks
- Channel switcher (CTRL/CMD+K) search results for direct messages now match message autocomplete
- Autocomplete is now case insensitive for @-mentions, emojis, slash commands and channel linking

#### Enterprise Edition
- Split out channel management permissions into separate settings for creation, deletion, and renaming a channel
- Ability to set the maximum number of users in a channel that will disable @all and @channel notifications
- Added ability to set a user's Position field with LDAP sync or SAML
- New option to purge all in-memory caches for sessions, accounts and channels

### Bug Fixes
- Integrations that post to Direct Message channels now mark the channel as Unread
- @mention autocomplete will now filter on Chinese, Japanese, Korean names
- Text focus is now set on the text input area after channel creation
- Editing old posts no longer causes them to repost for other members of the channel
- Email invitation subject line no longer displays HTML characters in place of apostrophes in the team name
- Current user is no longer displayed in the direct messages modal
- Searching on direct messages modal now happens on typing rather than after hitting ENTER
- More Channels modal now resets search when opening and closing the dialog
- Channel switcher (CTRL/CMD+K) now works for direct message channels of users outside the team
- Using the command line to invite users no longer sends an invalid join team link
- Sleeping and waking your computer while logged into Mattermost no longer causes a console error
- Searching for users in double in quotes in the direct message modal no longer throws an error
- XML file preview no longer throws a JavaScript error
- User autocomplete in message box no longer matches against email
- Channel linking (with ~ shortcut) now works for channels you don't belong to
- Fixed statistics for websockets and database connections in **System Console** > **Site Statistics** to work in [High Availability mode](https://docs.mattermost.com/deployment/cluster.html)
- Slash commands now work in newly created private channels without requiring a refresh
- Zapier app channel dropdown selector works again
- Fixed sign in errors for non-admin accounts when custom emojis are restricted to Team and System Admins
- Fixed encoding of file names when downloading attachments
- Unflagging or flagging a post in the right-hand sidebar no longer forces a scroll to the top of the flagged posts list
- User list in **System Console > Teams** is no longer blank on first load
- Fixed a bug where sometimes the right-hand sidebar would not display properly when switching to view another channel

### Compatibility  
Changes from v3.5 to v3.6:

**Special Upgrade Note:**
(Enterprise Edition) If you previously had values set for `RestrictPublicChannelManagement` and `RestrictPrivateChannelManagement`, the new settings for  `RestrictPublicChannelCreation`, `RestrictPrivateChannelCreation`, `RestrictPublicChannelDeletion`, and `RestrictPrivateChannelDeletion` will take those settings as their default values.

#### config.json   

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json` or the System Console.

**Changes to Team Edition and Enterprise Edition**:

Deprecated Settings:

 - Under `ServiceSettings` in `config.json`:
   - `"SegmentDeveloperKey"` to be removed in v3.7

**Additional Changes to Enterprise Edition**:

The following config settings will only work on servers with an Enterprise License that has the feature enabled.

- Under `ServiceSettings` in `config.json`:
   - Added `”EnforceMultifactorAuthentication": false` to control whether MFA in enforced
- Under `TeamSettings` in `config.json`:
   - Changed `"RestrictPublicChannelManagement": "all"` to only control who can edit the channel header, purpose, and name of public channels (previously it also controlled creation and deletion)
  - Changed `"RestrictPrivateChannelManagement": "all"` to only control who can edit the channel header, purpose, and name of private groups (previously it also controlled creation and deletion)
  - Added `"RestrictPublicChannelCreation": "all"` to control who can create public channels
  - Added `"RestrictPrivateChannelCreation": "all"` to control who can create private groups
  - Added `"RestrictPublicChannelDeletion”: "all"` to control who can delete public channels
  - Added `"RestrictPrivateChannelDeletion": "all"` to control who can delete private channels
  - Added `"MaxNotificationsPerChannel": 1000` to set the maximum number of channel members for which `@all` and `@channel` notifications will be sent
- Under `LdapSettings` in `config.json`:
  - Added `"PositionAttribute": ""` to select an LDAP attribute to synchronize for the user position (job title) field
- Under `SamlSettings` in `config.json`:
  - Added `"PositionAttribute": ""` to select an LDAP attribute to synchronize for the user position (job title) field
- Added `MetricsSettings` in `config.json` for performance monitoring settings:
  - Added `"Enable": false` to control whether performance monitoring is enabled
  - Added `"BlockProfileRate": 0` to control the [fraction of goroutine blocking events that are reported in the blocking profile](https://golang.org/pkg/runtime/#SetBlockProfileRate)
  - Added `"ListenAddress": ":8067"` to control the address the server will listen on to expose performance metrics
- Added `AnalyticsSettings` in `config.json` for analytics settings:
  - Added `"MaxUsersForStatistics": 2500` to set the maximum number of users on the server before statistics for total posts, total hashtag posts, total file posts, posts per day, and active users with posts per day are no longer counted (use this setting to improve performance on large instances)

### Database Changes from v3.5 to v3.6

**Posts Table:**
- Added `HasReactions` column

**Teams Table:**
- Added `Description` column

**Users Table:**
- Added `Position` column

**Status Table:**
- Removed `ActiveChannel` column

### API Changes from v3.5 to v3.6

**New routes:**
- Added `POST` at `/commands/update`
  - Updates a slash command
- Added `GET` at `/users/name/{username}`
  - Returns a user matching the given username
- Added `GET` at `/users/email/{email}`
  - Returns a user matching the given email
- Added `GET` at `/users/autocomplete`
  - Returns a list of users on the system that have a username, full name, or nickname that match against the provided term
- Added `GET` at `/teams/name/{team_name}`
  - Returns team object for a given team name
- Added `GET` at `/teams/{team_id}/channels/name/{channel_name}`
  - Returns a channel for a given channel name
- Added `POST` at `/teams/{team_id}/channels/{channel_id}/members/ids`
  - Returns channel member objects for the channel and user IDs specified
- Added `GET` at `/teams/members`
  - Returns an array with the teams the current user belongs to
- Added `GET` at `/teams/unread`
  - Returns an array containing the amount of unread messages and mentions for the teams the current user belongs to
- Added `POST` at `/teams/{team_id}/channels/view`
  - Performs all actions related to viewing a channel, including marking channels as read, clearing push notifications, and updating the active channel
- Added `POST` at `/teams/{team_id}/channels/{channel_id}/posts/{post_id}/reactions/save`
  - Saves an emoji reaction for a post, returns the saved reaction if successful
- Added `POST` at `/teams/{team_id}/channels/{channel_id}/posts/{post_id}/reactions/delete`
  - Removes an emoji reaction for a post in the given channel, returns nil if successful
- Added `GET` at `/teams/{team_id}/channels/{channel_id}/posts/{post_id}/reactions'`
  - Returns a list of all emoji reactions for a post
- Added `GET` at `/admin/invalidate_all_caches`
  - Purge all the in-memory caches for things like sessions, accounts, channels; deployments using High Availability will attempt to purge all the servers in the cluster (this may adversely impact performance)
- Added `GET` at `/channels/more/{offset}/{limit}`
  - Returns a page of public channels the user is not in based on the provided offset and limit
-  Added `POST` at `/channels/more/search`
  - Returns a list of public channels the user is not in that match the search criteria
- Added `GET` at `/channels/autocomplete`
  - Returns a list of public channels that match the provided string

**Deprecated routes:**
- `GET` at `/channels/more` (replaced by /`channels/more/{offset}/{limit}`) to be removed in v3.7
- `POST` at `/channels/update_last_viewed_at` (replaced by `/channels/view`) to be removed in v3.8
- `POST` at `/channels/set_last_viewed_at` (replaced by `/channels/view`) to be removed in v3.8
- `POST` at `/users/status/set_active_channel` (replaced by `/channels/view`) to be removed in v3.8

**Removed routes:**
- `POST` at `/teams/create_from_signup`
- `POST` at `/teams/signup`

**Changed routes:**
 - Updated `teams/{team_id}/commands/execute` endpoint request body field from `channelId` to `channel_id`

### Websocket Event Changes from v3.5 to v3.6

**Added:**
- `update_team` that occurs each time the team info is updated
- `reaction_added` that occurs when an emoji reaction is added to a post
- `reaction_removed` that occurs when an emoji reaction is removed from a post

### Known Issues

- Slack Import doesn't add merged members/e-mail accounts to imported channels
- User can receive a video call from another browser tab while already on a call
- Video calls do not work with Chrome v56 and later
- Sequential messages from the same user appear as separate posts on mobile view
- Edge overlays desktop notification sound with system notification sound
- Deleting a message from a permalink view doesn't show delete until refresh
- Search autocomplete picker is broken on Android

### Contributors

Many thanks to all our contributors. In alphabetical order:

/mattermost-server

- [asaadmahmood](https://github.com/asaadmahmood), [bjoernr-de](https://github.com/bjoernr-de), [bolecki](https://github.com/bolecki), [brendanbowidas](https://github.com/brendanbowidas), [CometKim](https://github.com/CometKim), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [debanshuk](https://github.com/debanshuk), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [fraziern](https://github.com/fraziern), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [khawerrind](https://github.com/khawerrind), [lfbrock](https://github.com/lfbrock), [maruTA-bis](https://github.com/maruTA-bis), [pepf](https://github.com/pepf), [raphael0202](https://github.com/raphael0202), [Rudloff](https://github.com/Rudloff), [Yangchen1](https://github.com/Yangchen1), [ZJvandeWeg](https://github.com/ZJvandeWeg)

/docs

- [aureliojargas](https://github.com/aureliojargas), [axilleas](https://github.com/axilleas), [esethna](https://github.com/esethna), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [JeffSchering](https://github.com/JeffSchering), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [lfbrock](https://github.com/lfbrock), [lindy65](https://github.com/lindy65), [nils-werner](https://github.com/nils-werner), [okin](https://github.com/okin), [quentinus95](https://github.com/quentinus95), [qyra](https://github.com/qyra), [shieldsjared](https://github.com/shieldsjared), [tejasbubane](https://github.com/tejasbubane), [Tethik](https://github.com/Tethik), [yangchen1](https://github.com/yangchen1), [yumenohosi](https://github.com/yumenohosi), [yuya-oc](https://github.com/yuya-oc), [ZJvandeWeg](https://github.com/ZJvandeWeg)

/mattermost-docker-preview

- [cpanato](https://github.com/cpanato), [hyeseongkim](https://github.com/hyeseongkim), [jasonblais](https://github.com/jasonblais), [mattermost-build](https://github.com/mattermost-build)

/desktop

- [jasonblais](https://github.com/jasonblais), [jnugh](https://github.com/jnugh), [yuya-oc](https://github.com/yuya-oc)

/mattermost-mobile

- [csduarte](https://github.com/csduarte), [enahum](https://github.com/enahum), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [thomchop](https://github.com/thomchop)

/mattermost-load-test

- [crspeller](https://github.com/crspeller), [it33](https://github.com/it33)

/mattermost-driver-javascript

- [Mattermost-build](https://github.com/Mattermost-build)

/android

- [CometKim](https://github.com/CometKim), [coreyhulen](https://github.com/coreyhulen), [DavidLu1997](https://github.com/DavidLu1997), [dmeza](https://github.com/dmeza), [esethna](https://github.com/esethna)

/mattermost-webrtc

- [enahum](https://github.com/enahum)

/mattermost-api-reference

- [CometKim](https://github.com/CometKim), [cpanato](https://github.com/cpanato), [enahum](https://github.com/enahum), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [jwilander](https://github.com/jwilander), [MartinDelille](https://github.com/MartinDelille), [trarbr](https://github.com/trarbr), [ZJvandeWeg](https://github.com/ZJvandeWeg)

/mattermost-docker

- [Andrey9kin](https://github.com/Andrey9kin), [esethna](https://github.com/esethna), [jasonblais](https://github.com/jasonblais)

/ios

- [esethna](https://github.com/esethna)

/mattermost-push-proxy

- [coreyhulen](https://github.com/coreyhulen)

Thanks also to those who reported bugs that benefited the release, in alphabetical order:

 - [bjoernr-de](https://github.com/bjoernr-de) ([#5079](https://github.com/mattermost//mattermost-server/issues/5079)), [S6066](https://github.com/S6066) ([#5011](https://github.com/mattermost//mattermost-server/issues/5011))

## Release v3.5.1  

### Notes on Patch Release

 - **v3.5.1, released 2016-11-23**
   - Security update to preventing cross-site scripting and remote code execution, thanks to Harrison Healey for [reporting responsibly](http://www.mattermost.org/responsible-disclosure-policy/).
   - Fixed an issue where usernames would sometimes not appear beside posts and the reply arrow would throw an error.
   - The channel purpose is no longer cut off in the user interface of the **More...** channel menu.
   - Fixed a scroll issue where the center channel didn't always scroll to the bottom when switching channels.
   - Fixed a server error that occurred when searching for users using an asterisk.
   - Fixed an issue where direct message channel headers would sometimes disappear.
   - "New Messages" indicator is fixed so it no longer remains visible after switching channels.
   - Fixed an issue where users could not join a public channel by navigating to the channel URL.
   - Email and push notifications are made asynchronous to fix a delay sending messages when HPNS was enabled.
   - Autocomplete timeout is decreased to make autocomplete more responsive to quick typing.
 - **v3.5.0, released 2016-11-16**
   - Original 3.5 release.

### Security Update

- Mattermost v3.5.1 contains multiple [security updates](http://about.mattermost.com/security-updates/). [Upgrading to Mattermost v3.5.1](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Thanks to Alyssa Milburn and Harrison Healey for contributing security reports through the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Highlights

#### Languages
- Added Russian translations for the user interface.
- Promoted Chinese (both simplified and traditional), German, French and Japanese to release-quality translations, removing beta tags.

#### Performance improvements for mobile and web experience

 - Ability to download assets in parallel via HTTP2 support.
 - Reduced CPU bottlenecks and optimized SQL queries.
 - Reduced load times through paging controls, server-side search and on-the-fly data loading that requests data as the client needs it.
 - Added paging APIs for profiles, channels and user lists.
 - Added client-scaling for auto-complete and status indicators.
 - Added server-side in-memory caching to reduce DB reads/writes.

#### Connection Security
- TLS is now supported directly on the Mattermost server. Learn more in our [documentation](https://docs.mattermost.com/install/config-tls-mattermost.html).
- Support for automatically fetching certificates through Let's Encrypt.

#### Minio File Storage
- Minio fully manages S3 API requests with automatic bucket location management across S3 regions.

#### Favorite Channels
- Added the ability to select Favorite Channels that appear at the top of the channels sidebar.

#### Video and Audio Calling (early-preview)
- Added early preview of video and audio calling option using self-hosted proxy.
- Intended as working prototype for community development, not recommended for production.
- Early preview does not include logging or detailed documentation.

#### Improved Slack Import
- Added the ability to import files from Slack (CLI command also supported).
- Added the ability to import bot/integration messages, Join/Leave messages, and /me messages.
- Duplicate users are now merged.
- Channel topics, purpose, and users now import correctly.
- Channel links now import correctly.

### Improvements

#### iOS Apps
- Channel settings, account settings, and channel header now render as full screen modals for better visibility
- [...] menu options now displayed larger for better usability
- Keyboard doesn't automatically close when sending a message, letting you quickly send several messages in succession
- When the "Download" link is clicked on files, a "Back" button lets users get back to the app

#### Android Apps
- Channel settings, account settings, and channel header now render as full screen modals for better visibility
- [...] menu options now displayed larger for better usability
- Disabled screen rotation
- Fixed where clicking on download button for a file attachment did nothing
- Keyboard doesn't automatically close when sending a message, letting you quickly send several messages in succession

#### User Interface
- Text (.txt) files now show a preview in the image previewer
- Status indicators are now visible in compact view
- Clicking on a profile picture in center channel or right hand sidebar brings up profile popover
- The "@" and flag icons next to search bar now toggles results
- [...] menu no longer displayed for system messages
- Browser tab name now changes when switching to System Console or Integrations pages
- A loading icon now shows on the team selection page
- On mobile devices, the keyboard now stays open after sending a message to make sending multiple messages easier

#### Notifications
- Notification sound settings are now honored on the [Mattermost Desktop Apps](https://about.mattermost.com/download/#mattermostApps)
- Push notifications can now be received on more than one device

#### Channel Shortlinking
- Channels can be shortlinked using the ~ character.
- Auto-complete works with both the channel handle and name

#### Integrations
- If a webhook is sent to a direct message channel that has not been created yet, the channel is now automatically created

#### Keyboard Shortcuts
- CTRL/CMD+SHIFT+M now toggles recent mentions results

#### Team Settings
- Team names are now restricted to be a minimum of two characters long, instead of four, to support abbreviated team names

#### System Console
- Maximum number of channels per team is now configurable

#### Enterprise Edition:
- Made the MFA secret key visible, so it's possible to set up Google Authenticator without scanning the QR code

### Bug Fixes
- Files can now be sent in Direct Messages across teams
- Correct login method now shown in System Console user lists
- Channel switcher (CTRL/CMD+K) no longer throws an error when switching to a user outside of your current team
- Channel switcher (CTRL/CMD+K) now works for creating new Direct Message channels
- Channels on the left hand side now sort numerically, alphabetically, and based on locale
- Fixed incorrect error message when trying a team URL with one character
- `/join` no longer throws an error for non-admin accounts
- Added System Message when user joins Off-Topic channel
- Added the "View Members" option to the channel menu on mobile
- Send button is now visible on tablet sized screens

### Compatibility  
Changes from v3.4 to v3.5:

#### config.json   

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json` or the System Console.

**Changes to Team Edition and Enterprise Edition**:

- Under `ServiceSettings` in `config.json`:
    - Added `"ConnectionSecurity": ""` to select the type of encryption between Mattermost and your server
    - Added `"TLSCertFile": ""` to specify the certificate file to use.
    - Added `"TLSKeyFile": ""` to specify the private key to use.
    - Added `"UseLetsEncrypt": false` to enable automatic retreval of certificates from the Let's Encrypt.
    - Added `"LetsEncryptCertificateCacheFile": "./config/letsencrypt.cache"` to specify the file to store certificates retrieved and other data about the Let's Encrypt service.
    - Added `"Forward80To443": false` to enable forwarding of all insecure traffic from port 80 to secure port 443.
    - Added `"ReadTimeout": 300` to specify the maximum time allowed from when the connection is accepted to when the request body is fully read.
    - Added `"WriteTimeout": 300` to specify the maximum time allowed from the end of reading the request headers until the response is written.
- Under `FileSettings` in `config.json`:
    - Addded `AmazonS3SSL": true` to allow insecure connections to Amazon S3.
- Under `RateLimitSettings` in `config.json`:
    - Changed: `"Enable": false` to disable rate limiting by default
    - Added `"MaxBurst": 100` to set the maximum number of requests allowed beyond the per second query limit
- Under `TeamSettings` in `config.json`:
    - Added `"MaxChannelsPerTeam": 2000` to set the maximum number of channels per team
- Under `WebrtcSettings` in `config.json`
    - Added `"Enable": false` to enable one-on-one video calls.
    - Added `"GatewayWebsocketUrl": ""` to specify the websocket used to signal and establish communication between the peers.
    - Added `"GatewayAdminUrl": ""` to specify the URl to obtain valid tokens for each peer to establish the connection.
    - Added `"GatewayAdminSecret": ""` to specify your admin secret password to access the Gateway Admin URL.
    - Added `"StunURI": ""` to specify your STUN URI.
    - Added `"TurnURI": ""` to specify your TURN URI.
    - Added `"TurnUsername": ""` to specify your TURN username
    - Added `"TurnSharedKey": ""` to specify your TURN server shared key to created dynamic passwords to establish the connection.

### Database Changes from v3.4 to v3.5

**FileInfo Table**

- Added `FileInfo` table

**Posts Table**

- Added `FileIds` column
- Added indexes for `DeleteAt`

**Channels Table**, **Commands Table**, **Emoji Table**, **Teams Table**, **IncomingWebhooks Table**, **OutgoingWebhooks Table**

- Added indexes for `CreateAt`
- Added indexes for `UpdateAt`
- Added indexes for `DeleteAt`

**TeamMembers Table**

- Added indexes for `DeleteAt`

**Sessions Table**

- Added indexes for `ExpiresAt`
- Added indexes for `CreateAt`
- Added indexes for `Last ActivityAt`

**Users Table**

- Added indexes for `CreateAt`
- Added indexes for `UpdateAt`
- Added indexes for `DeleteAt`
- Added full text indexes for `idx_users_all_txt`: Username, FirstName, LastName, Nickname, Email
- Added full text indexes for `idx_users_names_txt`:Username, FirstName, LastName, Nickname

### API Changes from v3.4 to v3.5

**New routes:**

- Added `POST` at `/users/search`
    - Search for user profiles based on username, full name and optionally team id.
- Added `GET` at `/users/{offset}/{limit}`
    - Retrieves a page of system-wide users
- Added `POST` at `/teams/{team_id}/update_member_roles`
    - Update a user's roles for the specified team.
- Added `GET` at `/teams/{team_id}/channels/{channel_id}/members/{user_id}`
    - Retrieves the channel member for the specified user. Useful for fetching the channel member after updates are made to it. If the channel member does not exist, then return an error.
- Added `GET` at `/teams/{team_id}/stats`
    - Returns stats for teams which includes total user count and total active user count.
- Added `GET` at `/teams/{team_id}/members/{offset}/{limit}`
    - To page through team members
- Added `POST` at `/teams/{team_id}/members/ids`
    - Retrieves a list of team members based on user ids
- Added `GET` at `/teams/{team_id}/members/{user_id}`
    - Retrieves a single team member
- Added `GET` at `/teams/{team_id}/posts/{post_id}/get_file_infos`
    - Retrieves file attachment info for a post
- Added `GET` at `/channels/{channel_id}/users/{offset}/{limit}`
    - Retrieves profiles for users in the channel
- Added `GET` at `/channels/{channel_id}/users/not_in_channel/{offset}/{limit}`
    - Retrieves profiles for users not in the channel
- Added `POST` at `/webrtc/token`
    - Retrieves a valid token and servers to establish a webrtc connection between the peers

**Moved routes:**

- Updated `GET` at `/channels/{channel_id}/extra_info` to `/channels/{channel_id}/stats`
    - No longer returns a list of channel members and only returns the member count
- Updated `POST` at `/users/profiles/{team_id}` to `/teams/{team_id}/users/{offset}/{limit}`
    - Functionally performs the same, just moves it to match our other APIs that need a team ID.
- Updated `GET` at `/members/{team_id}` to `/teams/{team_id}/members/{offset}/{limit}`
    - Allows paging through team members

**Removed routes:**

- Removed `GET` at `/users/direct_profiles`
- Removed `GET` at `/users/profiles_for_dm_list/{team_id}/{offset}/{limit}`

**Modified Routes**

- Added `POST` at `/users/{user_id}/update_roles`
    - Only allows updating of system wide roles. If you want to update team wide roles, please use the new route `/teams/{team_id}/update_member_roles`

**Changes to File Routes:**

Routes used to get files and their metadata from the server have been changed substantially in 3.5 so that each file will be given a unique identifier to make them easier to use through the API. In addition, the `Filenames` field of each post has been deprecated in favor of the new `FileIds` field.

- The response type of `GET` at `/teams/{team_id}/files/upload` has been changed to return more information about the uploaded file. See [the documentation for this route on api.mattermost.com](https://api.mattermost.com/#tag/files%2Fpaths%2F~1teams~1%7Bteam_id%7D~1files~1upload%2Fpost) for more information
- Split `GET` at `/teams/{team_id}/files/get/{channel_id}/{user_id}/{filename}` into:
    - `GET` at `/files/{file_id}/get`
        - Get a file
    - `GET` at `/files/{file_id}/get_thumbnail`
        - Get a small thumbnail for image files
    - `GET` at `/files/{file_id}/get_preview`
        - Get a medium-sized preview image for image files
- Updated `GET` at `/teams/{team_id}/files/get_info/{channel_id}/{user_id}/{filename}` to `/files/{file_id}/get_info`
- Updated `GET` at `/teams/{team_id}/files/get_public_link` to `/files/{file_id}/get_public_link`
- Added `GET` at `/public/files/{file_id}/get`
    - Get a file without logging in
    - The previous route `GET` at `/public/files/get/{team_id}/{channel_id}/{user_id}/filename` has been deprecated, but will remain available for files that were uploaded prior to 3.5

### Known Issues

- Channel autolinking with `~` only works if you are a member of the channel
- Slack Import doesn't add merged members/e-mail accounts to imported channels
- User can receive a video call from another browser tab while already on a call
- Video calls do not work with Chrome v56 and later
- Sequential messages from the same user appear as separate posts on mobile view
- Slash commands do not work in newly created private channels until a hard refresh
- Edge overlays desktop notification sound with system notification sound
- Pressing escape to close autocomplete clears the textbox on IE11
- Channel switcher doesn't work for users outside of your current team
- Deleting a messages from a permalink view doesn't show delete until refresh
- Channel dropdown selector no longer works in the Zapier App but the Channel ID can still be entered manually
- Search autocomplete picker is broken on Android
- Channel push notification preferences do not work for the inactive teams if you have multiple teams on a single server.

### Contributors

Many thanks to all our contributors. In alphabetical order:

/mattermost-server

- [alsma](https://github.com/alsma), [asaadmahmood](https://github.com/asaadmahmood), [coreyhulen](https://github.com/coreyhulen), [crspeller](https://github.com/crspeller), [DavidLu1997](https://github.com/DavidLu1997), [digitaltoad](https://github.com/digitaltoad), [dmeza](https://github.com/dmeza), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [grundleborg](https://github.com/grundleborg), [harshavardhana](https://github.com/harshavardhana), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [lfbrock](https://github.com/lfbrock), [npcode](https://github.com/npcode), [R-Wang97](https://github.com/R-Wang97), [Rudloff](https://github.com/Rudloff), [S4KH](https://github.com/S4KH), [shieldsjared](https://github.com/shieldsjared), [thomchop](https://github.com/thomchop), [usmanarif](https://github.com/usmanarif), [wget](https://github.com/wget), [yangchen1](https://github.com/yangchen1)

/ios

- [coreyhulen](https://github.com/coreyhulen), [lfbrock](https://github.com/lfbrock), [thomchop](https://github.com/thomchop)

/desktop

- [asaadmahmood](https://github.com/asaadmahmood), [itsmartin](https://github.com/itsmartin), [jasonblais](https://github.com/jasonblais), [jcomack](https://github.com/jcomack), [jnugh](https://github.com/jnugh), [magicmonty](https://github.com/magicmonty), [Razzeee](https://github.com/Razzeee), [yuya-oc](https://github.com/yuya-oc)

/docs

- [asaadmahmood](https://github.com/asaadmahmood), [chikei](https://github.com/chikei), [crspeller](https://github.com/crspeller), [erikthered](https://github.com/erikthered), [esethna](https://github.com/esethna), [gabx](https://github.com/gabx), [gmorel](https://github.com/gmorel), [grundleborg](https://github.com/grundleborg), [hannaparks](https://github.com/hannaparks), [harshavardhana](https://github.com/harshavardhana), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [JeffSchering](https://github.com/JeffSchering), [kunthar](https://github.com/kunthar), [lfbrock](https://github.com/lfbrock), [lindy65](https://github.com/lindy65), [npcode](https://github.com/npcode), [reach3r](https://github.com/reach3r), [Rudloff](https://github.com/Rudloff), [rwillmer](https://github.com/rwillmer), [shieldsjared](https://github.com/shieldsjared), [StraylightSky](https://github.com/StraylightSky), [thiyagaraj](https://github.com/thiyagaraj), [yangchen1](https://github.com/yangchen1), [yumenohosi](https://github.com/yumenohosi), [yuya-oc](https://github.com/yuya-oc), [Zhouzi](https://github.com/Zhouzi)

/mattermost-docker

- [5ak3t](https://github.com/5ak3t), [npcode](https://github.com/npcode), [rothgar](https://github.com/rothgar)

/android

- [coreyhulen](https://github.com/coreyhulen), [DavidLu1997](https://github.com/DavidLu1997), [dmeza](https://github.com/dmeza), [it33](https://github.com/it33), [mattchue](https://github.com/mattchue)

/mattermost-bot-sample-golang

- [hmhealey](https://github.com/hmhealey), [pneisen](https://github.com/pneisen)

/mattermost-load-test

- [athingisathing](https://github.com/athingisathing), [coreyhulen](https://github.com/coreyhulen), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [enahum](https://github.com/enahum), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais)

/mattermost-driver-javascript

- [crspeller](https://github.com/crspeller)

/mattermost-api-reference

- [coreyhulen](https://github.com/coreyhulen), [crspeller](https://github.com/crspeller), [hmhealey](https://github.com/hmhealey), [jwilander](https://github.com/jwilander)

/mattermost-mobile

- [dmeza](https://github.com/dmeza), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [mfpiccolo](https://github.com/mfpiccolo), [thomchop](https://github.com/thomchop)

## Release v3.4.0  

Release date: 2016-09-16

### Highlights

#### Zapier Integration
- Integrate over [700 public cloud applications](https://zapier.com/zapbook/) using [Zapier](https://zapier.com), with full support for Markdown formatting. To start, [click here to accept an invitation to Zapier](https://zapier.com/developer/invite/47050/902cde1eb8e0b3eb1223a2cf05331abd/), then [follow the setup guide](https://docs.mattermost.com/integrations/zapier.html).

#### OAuth 2.0 Service Provider
- Users with an account on a Mattermost server can securely sign in to third-party applications with an OAuth 2.0 protocol. See [documentation](https://docs.mattermost.com/developer/oauth-2-0-applications.html) to learn more.

#### Improved Notifications and Status Indicators
- Users can now control how often email notifications are sent
- Users can now control whether push notifications are sent when they are online, offline or away
- Users can now set the display duration of a desktop notification
- Email notifications now include channel names
- Android push notifications are now cleared after the message is read somewhere else
- /away, /online, /offline can now be used to manually set your status
- Status indicators are now shown on the profile pictures in the centre channel and right hand side

### Improvements

#### Files and Images
- PDFs now show a preview in the image previewer on browsers, desktop apps, and mobile apps

#### Integrations
- After an integration is created, a confirmation screen now displays the relevant token, webhook URL or OAuth client secret

#### System Console
- Added connection security option `PLAIN` for SMTP
- Salt settings in the config.json now ship blank and are autogenerated after install
- Added [Error and Diagnostics Reporting option](https://docs.mattermost.com/administration/config-settings.html#enable-diagnostics-and-error-reporting) to help Mattermost, Inc. improve reliability and performance for your deployment configuration.

#### Slack Import
- Slack import now imports @mentions mapped to user names

#### User Interface
- Improved design of signup pages when multiple account creation methods are enabled
- User profile popover now shows both username and full name (if available)
- @mention autocomplete now groups users according to who is in the channel
- Channel URL no longer updates when the Channel Name changes
- Markdown headings are now rendered in Compact View
- A System Message now posts when new users join Town Square

#### Enterprise Edition:
- Added a CLI tool for creating channels
- Added a display option to hide join/leave messages from view (user added and user removed messages still appear)
- System Admins can now test their LDAP connection using a “Test Connection” button
- FirstName and LastName fields are now optional for LDAP and SAML

### Bug Fixes
- Old public links are now invalidated when the salt is regenerated.
- Messages can now be flagged from the search results list
- Count of unread mentions are no longer mixed when switching between multiple teams.
- Recent Mentions search on mobile no longer contains `@all`
- For those using the mobile view on desktop, CTRL+ENTER now sends messages on mobile web view
- User removed from team now shows up in DM list under "Outside this team"
- Mentions update properly when team is switched

### Compatibility  
Changes from v3.3 to v3.4:

**Special Note**

(Only affects servers with public links enabled) After upgrading to v3.4, existing public links will no longer be valid. This is because in past versions, when the Public Link Salt was regenerated existing public links were not invalidated. Now, when the salt is regenerated, existing links are made invalid.

#### config.json   

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json` or the System Console.

**Changes to Team Edition and Enterprise Edition**:

 - Under `EmailSettings` in `config.json`:
    - Added `"EnableEmailBatching": false` to enable batching of email notifications configurable in Account Settings. To enable email batching, the `SiteURL` field must be filled out and `Enable` under `ClusterSettings` must be set to `false` to disable high availability mode.
    - Added `"EmailBatchingBufferSize": 256` to specify the maximum number of notifications batched into a single email.
    - Added `"EmailBatchingInterval": 30` to specify the maximum frequency, in seconds, which the batching job checks for new notifications.

 - Under `LogSettings` in `config.json`:
    - Added `"EnableDiagnostics": true` to increase reliability and performance of Mattermost for your deployment configuration by sending encrypted [error reporting and diagnostic information](https://docs.mattermost.com/administration/config-settings.html#enable-diagnostics-and-error-reporting) to Mattermost, Inc.

**Additional Changes to Enterprise Edition:**    

The following config settings will only work on servers with an Enterprise License that has the feature enabled.

- Under `LdapSettings` in `config.json`:
    - `"FirstNameAttribute": ""` is no longer a required field
    - `"LastNameAttribute": ""` is no longer a required field
- Under `SamlSettings` in `config.json`:
    - `"FirstNameAttribute": ""` is no longer a required field
    - `"LastNameAttribute": ""` is no longer a required field

### Database Changes from v3.3 to v3.4

**Status Table**

 - Added `Manual` column.
 - Added `ActiveChannel` column.

### API Changes from v3.3 to v3.4

**New routes:**
 - Added `GET` at `/oauth/authorized`
     - Returns the OAuth2 Apps authorized by the user.  On success it returns a list of sanitized OAuth2 Authorized Apps by the user.
 - Added `POST` at `/oauth/"+clientId+"/deauthorize`
     - Deauthorizes a user on an OAuth 2.0 app, where `clientId` corresponds to the application. Returns status OK on success or an AppError on fail.
 - Added `POST` at `/oauth/"+clientId+"/regen_secret`
     - Generates a new OAuth App Client Secret, where `clientId` corresponds to the application. Returns an OAuth2 App on success. Must be authenticated as a user and the same user who registered the app or a System Admin.
 - Added `POST` at `/admin/ldap_test`
     - Will run a connection test on the current LDAP settings. It will return the standard OK response if settings work. Otherwise it will return an appropriate error.
 - Added `POST` at `/users/status/set_active_channel`
     - Sets the Status.ActiveChannel field which is used to tell if the user is actively viewing a channel or not.
 - Added `GET` at `/admin/recently_active_users/{teamId}`
     - Returns a list of recent active users.

### Known Issues

- Upgrading from 3.2 to 3.4 will be incomplete due to a migration code not being run properly. You can either:
    - Upgrade from 3.2 to 3.3 and then from 3.3 to 3.4, or
    - Upgrade from 3.2 to 3.4, then run the following SQL query to make Mattermost rerun upgrade steps that were not properly completed: `UPDATE Systems SET Value = '3.1.0' WHERE Name = 'Version';`
- Deleted messages don't disappear from the channel for the user who deleted the message, if the message was previously edited and right hand sidebar is open.
- A single collapsed link or image preview re-opens after refresh.
- Files sent in private chat to members in a different team are not accessible.
- YouTube video links show as “Video not found” on Desktop App if "Allow mixed content" is turned on.
- “More” option under Direct Message list no longer shows count of team members not in your direct message list.
- On Firefox, CTRL/CMD+U keyboard shortcut to upload a file doesn’t work.
- Webhook attachments don’t show up in search results.
- Messages sometimes don't appear deleted until the page is refreshed.
- When joining a channel from a public link, the page sometimes loads for a long time and requires a refresh.

### Contributors

Many thanks to all our contributors. In alphabetical order:

/mattermost-server
- [asaadmahmood](https://github.com/asaadmahmood), [coreyhulen](https://github.com/coreyhulen), [crspeller](https://github.com/crspeller), [cybershambles](https://github.com/cybershambles), [daizenberg](https://github.com/daizenberg), [DavidLu1997](https://github.com/DavidLu1997), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [gramakri](https://github.com/gramakri), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [HugoGiraudel](https://github.com/HugoGiraudel), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [joonsun-baek](https://github.com/joonsun-baek), [jwilander](https://github.com/jwilander), [lfbrock](https://github.com/lfbrock), [npcode](https://github.com/npcode), [paranbaram](https://github.com/paranbaram), [phrix32](https://github.com/phrix32), [R-Wang97](https://github.com/R-Wang97), [shieldsjared](https://github.com/shieldsjared)

/ios
- [jasonblais](https://github.com/jasonblais), [lfbrock](https://github.com/lfbrock)

/desktop
- [asaadmahmood](https://github.com/asaadmahmood), [jasonblais](https://github.com/jasonblais), [jgis](https://github.com/jgis), [jnugh](https://github.com/jnugh), [Razzeee](https://github.com/Razzeee), [St-Ex](https://github.com/St-Ex), [yuya-oc](https://github.com/yuya-oc)

/docs
- [asaadmahmood](https://github.com/asaadmahmood), [coreyhulen](https://github.com/coreyhulen), [DavidLu1997](https://github.com/DavidLu1997), [esethna](https://github.com/esethna), [friism](https://github.com/friism), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [lfbrock](https://github.com/lfbrock), [lindy65](https://github.com/lindy65), [pmccarthy01](https://github.com/pmccarthy01), [rudloff](https://github.com/Rudloff),  [shieldsjared](https://github.com/shieldsjared), [yangchen1](https://github.com/yangchen1)

/mattermost-docker
- [npcode](https://github.com/npcode), [xcompass](https://github.com/xcompass)

/android
- [coreyhulen](https://github.com/coreyhulen), [enahum](https://github.com/enahum), [jasonblais](https://github.com/jasonblais), [jwilander](https://github.com/jwilander), [lfbrock](https://github.com/lfbrock)

/push-proxy
- [jwilander](https://github.com/jwilander)

/mattermost-heroku
- [it33](https://github.com/it33), [jwilander](https://github.com/jwilander)

## Release v3.3.0

Expected release date: 2016-08-16

### Security Update

- Mattermost v3.3.0 contains [security updates](http://about.mattermost.com/security-updates/). [Upgrading to Mattermost v3.3.0](http://docs.mattermost.com/administration/upgrade.html) is highly recommended.
- Thanks to Bastian Ike for contributing security reports through the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Highlights

#### Languages
- Added Dutch, Korean, Simplified Chinese and Traditional Chinese translations for the user interface.
- Promoted Portuguese and Spanish to release-quality translations.

#### Flagged Messages
- Added the ability to flag a message for follow up, so users can track messages they want to go back to later.

#### Improved Statuses
- Improved response time of status indicator changing between online/offline/away.
- Added status indicators to the Direct Message and Channel member lists.
- Added `@here` to mention users who are online.

#### Google SSO ([Enterprise E20](https://about.mattermost.com/pricing/))
- Users can sign in to Mattermost with their Google credentials and new Mattermost user accounts are automatically created on first login.

#### Office 365 SSO (Beta) ([Enterprise E20](https://about.mattermost.com/pricing/))
- Users can sign in to Mattermost with their Office 365 credentials and new Mattermost user accounts are automatically created on first login.

#### High Availability Mode (Beta) ([Enterprise E20](https://about.mattermost.com/pricing/))
- Support for highly available application servers configurable in the System Console and configuration files. See [documentation](http://docs.mattermost.com/deployment/cluster.html) for more details.

### Improvements

#### iOS app
- Fixed issue where “Refresh/Log out” was appearing frequently.
- Fixed issue where center channel appears blank after initial page load.
- Keyboard is now closed when a user executes a search.

#### Mobile (iOS and Android apps)
- Enter key now creates a new line instead of sending the message.
- Added links to the mobile apps in the welcome email, tutorial, and main menu.
- Added a landing page that informs users of the mobile app when they access the site on a mobile web browser.
- Permalinks are now available on mobile.
- Made it easier to click on the ... menu when in the right-hand sidebar view.
- Enable auto-complete for "from:" and "in:".

#### User Interface
- Channel header is now added to the View Info modal.
- Configured channel introduction to respect the full width and centred channel views.
- Removed signup link from sign in page if all signup methods are disabled.
- Improved channel header popover behaviour.

#### Authentication
- The username "matterbot" is now restricted from account creation.
- Link to create an account is hidden on the login page if no account creation methods are turned on in the System Console.
- All team members can View Members for the team or specific channels.

#### Notifications
- Mention notifications can be turned on for any new messages in comment threads that you participate in.

#### Keyboard Shortcuts
- Added icons next to channel names and improved sorting in the channel switcher (CTRL/CMD+K).
- Keyboard shortcuts that open modals can now toggle them open and closed (CTRL/CMD+SHIFT+A, CTRL/CMD+K).

#### Integrations
- Added an option to trigger outgoing webhook if the first word starts with the specified trigger word.

#### System Console
- Username is now added to the System Console users list.
- Legal and Support links are now hidden in the user interface if no link is specified in the System Console.
- If the Terms of Service link is left blank in the System Console then it defaults to the "Mattermost Conditions of Use" page.

#### [Enterprise E10, E20](https://about.mattermost.com/pricing/)

- Added the ability to set different themes for each team.
- Added a checkbox to apply theme settings to all teams of which you are a member.
- Users disabled or removed from the AD/LDAP server are now made “Inactive” in Mattermost (previously their sessions were revoked and could no longer log in, but their account status was not set to “Inactive”).
- Added the ability to force migrating authentication methods.
- Added Site Description field to the System Console > Customization > Custom Branding section.
- AD/LDAP `Bindusername` and `Bindpassword` fields in the System Console are now optional to support anonymous binding.

### Bug Fixes

- The behavior of setting for Link Previews in Account Settings is no longer reversed.
- Hitting the URL of a private team you used to belong to now redirects properly.
- Search terms contained in hashtags are now highlighted in the search results.
- Fixed an issue with quick typesetting on IE-11 and Edge.
- Fixed an issue with uploading SAML certificates if the files were removed from `config.json`.
- Multiple files can now be selected on the file upload dialog of the desktop app.
- Fixed a scrolling issue with the channel switcher.
- Fixed system messages showing a small empty white box.
- Fixed a markdown formatting issue with multiple lists in a row.
- Team Admins can no longer demote System Admins.
- The channel header now respects the setting for Channel Display Mode.
- The System Console no longer freezes if accessing via URL when not logged in.
- Site Name is now restricted to 30 characters to avoid text overflow.
- Error is no longer thrown when switching between teams in the System Console.
- Invalid password error is thrown if System Admin resets a password to something that doesn't meet the specified password requirements.
- Fixed the percentage loading indicator on the image preview modal.
- File upload overlay now appears on Edge.
- Maximum Users per Team and Minimum Password Length now default to reasonable values if a bad input is saved.
- Right-hand side now updates when a new profile picture is saved.
- Channels in the Channel Switcher are sorted by their handle if their display name is identical.
- Setting the length for mobile sessions is now fixed in the System Console.
- The “Test Connection” button in the System Console > Notifications > Email section now properly uses the saved SMTP password.
- System Admins no longer receive a JavaScript error if a new message is received while in the System Console.
- Dropdown in the Manage Members modal is no longer empty for System Admins.
- @all is now correctly highlighted if the trigger setting is selected in Account Settings.
- Fixed unformatted error message on account creation page if no creation methods are enabled.
- Corrected the formatting of some help text in the System Console.
- Color picker in Custom Theme settings now disappears once setting has been saved on mobile.
- System Console menu no longer cuts off long team names.

### Compatibility  
Changes from v3.2 to v3.3:

#### config.json   

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json` or the System Console.

**Changes to Team Edition and Enterprise Edition:**

- Under a new section `NativeAppSettings`:
   - Added `"AppDownloadLink": "https://about.mattermost.com/downloads/"` to point towards a download page for native apps.
   - Added `"AndroidAppDownloadLink": "https://about.mattermost.com/mattermost-android-app/"` to point towards the Android app.
   - Added `"IosAppDownloadLink": "https://about.mattermost.com/mattermost-ios-app/"` to point towards the iOS app.
- Under `ServiceSettings`:
    - Added `"SiteURL": ""` to allow the server to overwrite the site_url.
- Under `TeamSettings`:
    - Added `"UserStatusAwayTimeout": 300` to specify the number of seconds before users are considered "away".

**Additional Changes to Enterprise Edition:**    

The following config settings will only work on servers with an Enterprise License that has the feature enabled.

- Under `TeamSettings`:
    - Added `"CustomDescriptionText": ""` to set the site description shown in login screens and user interface.
- Under `GoogleSettings` in `config.json`:
   - Changed: `"Scope": "profile email"` to set the standard setting for OAuth to determine the scope of information shared with OAuth client.
   - Changed: `"AuthEndpoint": "https://accounts.google.com/o/oauth2/v2/auth"` to set the authorization endpoint for Google SSO.
   - Changed: `"TokenEndpoint": "https://www.googleapis.com/oauth2/v4/token"` to set the token endpoint for Google SSO.
   - Changed: `"UserApiEndpoint": "https://www.googleapis.com/plus/v1/people/me"` to set the user API endpoint for Google SSO.
- Under a new section `Office365Settings`:
   - Added `"Enable": false` to allow login using Office 365 SSO when set to `true`.
   - Added `"Secret": ""` to set the Client Secret received when registering the application with Google.
   - Added `"Id": ""` to set the Client ID received when registering the application with Google.
   - Added `"Scope": "User.Read"` to set the standard setting for OAuth to determine the scope of information shared with OAuth client.
   - Added `"AuthEndpoint": "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"` to set the authorization endpoint for Office 365 SSO.
   - Added `"TokenEndpoint": "https://login.microsoftonline.com/common/oauth2/v2.0/token"` to set the token endpoint for Office 365 SSO.
   - Added `"UserApiEndpoint": "https://graph.microsoft.com/v1.0/me"` to set the user API endpoint for Office 365 SSO.
- Under `LdapSettings` in `config.json`:
   - `"BindUsername": ""` and `"BindPassword": ""` are no longer required fields, so anonymous binding is possible.
- Under a new section `ClusterSettings`:
    - Added `"Enable": false` to enable High Availability mode.
    - Added `"InterNodeListenAddress": ":8075"` to specify the address the server will listen on for communicating with other servers.
    - Added `"InterNodeUrls": []` to specify the internal/private URLs of all the Mattermost servers separated by commas.

### Database Changes from v3.2 to v3.3

**OAuthAccessData Table**

 - Added `ClientId` column.
 - Added `UserId` column.
 - Removed `AuthCode` column.
 - Set Unique key on `ClientId` and `UserId` columns.
 - Removed index from `idx_oauthaccessdata_auth_code` column.
 - Added indexes to `idx_oauthaccessdata_client_id`, `idx_oauthaccessdata_user_id` and `idx_oauthaccessdata_refresh_token` columns.

**OAuthApps Table**

 - Added `IconURL` column.

**OutgoingWebhooks Table**

 - Added `TriggerWhen` column.

**Status Table**

 - Added `Status` table.

**Users Table**

 - Removed `LastActivityAt` column.
 - Removed `LastPingAt` column.
 - Removed `ThemeProps` column.

### API Changes from v3.2 to v3.3

**Updated admin routes:**
 - Changed `users/status` from `POST` to `GET`

**New admin routes:**
 - Added `GET` at `/posts/flagged/{offset:[0-9]+}/{limit:[0-9]+}`
     - Returns a list of posts that have been flagged by the user; `offset` is the offset to start the page at; `limit` is the max number of posts to return.
 - Added `GET` at `/admin/cluster_status`
     - Returns a json with a status of each of the reachable nodes in the cluster
 - Added `GET` at `/oauth/list`
     - Returns a list of OAuth 2.0 apps registered by the user
 - Added `GET` at `/oauth/app/{clientId:""}`
     - Returns a Sanitized OAuth 2.0 application where `clientId` corresponds to the application
 - Added `POST` at `/oauth/delete`
     - Returns status = OK if the OAuth 2.0 application owned by the current user was successfully deleted.
 - Added `GET` at `/oauth/access_token`
     - Returns the access token for OAuth 2.0 application
 - Added `POST` at `/preferences/delete`
     - Returns status = OK if the list of preferences owned by the current user were successfully deleted.
 - Added `POST` at `/admin/remove_certificate`
     - Returns a map[string]interface{} if removing the x509 base64 Certificates and Private Key files used with SAML exists on the file system.

### Known Issues

- Desktop apps sometimes require a refresh to solve 404 errors.
- Deleted messages don't disappear from the channel for the user who deleted the message, if the message was previously edited and right hand sidebar is open.
- After receiving an error for creating a channel with one character, updated channel name is not saved.
- A single collapsed preview re-opens after refresh.
- Removed user from team still appears in DM list from the team.
- Files sent in private messages to members in a different team are not accessible.
- YouTube videos show as “Video not found” on Desktop App.
- “More” option under Direct Message list no longer shows count of team members not in your direct message list.
- /join sometimes throws an error.
- On Firefox, CTRL/CMD+U keyboard shortcut doesn’t work.
- Sometimes only the last character typed in the channel switcher appears.
- Webhook attachments don’t show up in search results.
- Count of unread mentions are sometimes mixed when switching between multiple teams.
- Office 365 login sometimes causes a bad token error.
- Messages sometimes don't appear deleted until the page is refreshed.
- When joining a channel from a public link, the page sometimes loads for a long time and requires a refresh.
- After leaving a team, joining or creating a team sometimes causes an error.

### Contributors

Many thanks to all our contributors. In alphabetical order:

/mattermost-server

- [asaadmahmood](https://github.com/asaadmahmood), [coreyhulen](https://github.com/coreyhulen), [crspeller](https://github.com/crspeller), [DavidLu1997](https://github.com/DavidLu1997), [eadmund](https://github.com/eadmund), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [hmhealey](https://github.com/hmhealey), [jasonblais](https://github.com/jasonblais), [jwilander](https://github.com/jwilander), [lfbrock](https://github.com/lfbrock), [maruTA-bis5](https://github.com/maruTA-bis5), [Rudloff](https://github.com/Rudloff), [samogot](https://github.com/samogot), [yuters](https://github.com/yuters)

/desktop

- [jasonblais](https://github.com/jasonblais), [jnugh](https://github.com/jnugh), [Razzeee](https://github.com/Razzeee), [timroes](https://github.com/timroes), [yuya-oc](https://github.com/yuya-oc)

/android

- [coreyhulen](https://github.com/coreyhulen), [jasonblais](https://github.com/jasonblais)

/ios

- [coreyhulen](https://github.com/coreyhulen), [macdabby](https://github.com/macdabby), [jasonblais](https://github.com/jasonblais)

/docs

- [asaadmahmood](https://github.com/asaadmahmood), [esethna](https://github.com/esethna), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [lfbrock](https://github.com/lfbrock), [lindy65](https://github.com/lindy65)

/mattermost-docker

- [npcode](https://github.com/npcode)

/mattermost-driver-javascript

- [jwilander](https://github.com/jwilander)

/mattermost-bot-sample-golang

- [coreyhulen](https://github.com/coreyhulen), [jasonblais](https://github.com/jasonblais)

If we missed your name, please let us know at feedback@mattermost.com. Recognition is a manual process and mistakes can happen. We want to include anyone who's made a pull request that got merged during the release.

## Release v3.2.0

Release date: 2016-07-16

### Security Update

- Mattermost v3.2.0 contains [multiple security updates](http://about.mattermost.com/security-updates/). [Upgrading to Mattermost v3.2.0](http://docs.mattermost.com/administration/upgrade.html) is highly recommended.
- Thanks to Bastian Ike, Mohammad Razavi, Steve MacQuiddy, Christer Mjellem Strand and Jonas Arneberg for contributing security reports through the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Highlights

#### Languages

- Added German translation for the user interface if enabled by the System Admin from **System Console > Localization > Available Languages**.

#### Custom Emoji

- Create Custom Emoji from the **Main Menu** > **Custom Emoji** when enabled from **System Console** > **Customization** > **Custom Emoji**.
- Restrict the permissions required to create Custom Emoji (Enterprise).

#### Performance
- Gzip compression for static content files decreases time for first page load, enabled from **System Console** > **Configuration**.
- Reduced the total Mattermost package size from 25.7MB to 18.9MB.

#### Policy ([Enterprise E10, E20](https://about.mattermost.com/pricing/))

- Restrict the permission levels required to send team invitiations in **System Console** > **Policy**.
- Restrict the permission levels required to manage public and private channels, including creating, deleting, renaming, and setting the channel header or purpose.

#### SAML Single Sign-On ([Enterprise E20](https://about.mattermost.com/pricing/)):

- Users can sign in to Mattermost with their SAML credentials and new Mattermost user accounts are automatically created on first login. Mattermost pulls user information from SAML, including first and last name, email and username.
- Mattermost officially supports Okta and Microsoft ADFS as the identity providers (IDPs), but you may also try configuring SAML for a custom IDP.

### Improvements

**On-Boarding and Off-Boarding**

- After account creation, users are automatically directed to the team where they were invited instead of the Team Selection page.
- "Get Team Invite Link" is now accessible on mobile.
- Users can now be removed from teams via the **Main Menu** > **Manage Members** modal.

**System Console**

- Updated labeling of System Console settings in the UI for consistency and accuracy.
- ([Enterprise E20](https://about.mattermost.com/pricing/)) High availability support via **Reload Configuration from Disk** and **Recycle Database Connections** buttons had help text added so they're easier to understand.
- Allow System Admins to create teams even if team creation is disabled via the System Console.

**Notifications**

- Address displayed in the email notification footer is now configurable in the System Console.
- Direct Message desktop notifications now display with a "Direct Message" title.

**Web UI**

- Reply button and [...] menu now appear in a hovering UI element to increase the available margin width in the center channel.
- Right-hand sidebar can now be expanded when viewing threads or search results.
- Text emoticons now show up as the first entries in the autocomplete list
- @mention autocomplete now filters on nickname, full name, and username.
- Added an online indicator to the header of Direct Message channels.
- Added database type to the About Mattermost dialog.
- Removed unnecessary resizing when opening and closing the right hand sidebar.
- Removed jumping of the center channel when new messages are posted.
- Updated the channel info dialog to be more user friendly.

**[Enterprise E10, E20](https://about.mattermost.com/pricing/)**

-  [New command line tools](http://docs.mattermost.com/administration/command-line-tools.html) added, such as adding and removing users from channels, and restoring previously deleted channels.
- Added a button to manually trigger AD/LDAP synchronization.
- Updating AD/LDAP Synchronization Interval to no longer require a server restart to take effect.
- Improved logging for AD/LDAP synchronization.
- Added validation to the AD/LDAP settings in the System Console so an error is triggered if required fields are missing.

### Bug Fixes

- Privacy settings in the system console now refresh correctly when hiding email addresses or full names.
- Fixed the cross contamination of new channels created on different teams in the same browser.
- Updated the GitLab SSO error message for clarity if another Mattermost account is already associated with the GitLab account.
- Team creation via GitLab SSO no longer throws an error if email domains are restricted.
- Channel header no longer disappears after renaming a channel
- Testing the email connection in the System Console no longer throws an error.
- Multiline list items are now displayed correctly on new lines.
- Error message is updated when switching from email to GitLab SSO authentication that is already used by another account.
- Timestamps no longer require a page refresh when switching between 12h and 24h display formats.
- Hashtags containing `¿` are now returned with proper highlighting in search results.
- No longer require a page refresh before enabling compliance reporting in the System Console.
- `@all` no longer sends mentions if unselected in Account Settings.
- Users are no longer redirected to the switch teams page after changing authentication method from GitLab SSO to email.
- Invalid MFA token error message now clears correcly from the UI.
- Errors now correctly clear from the UI when changing passwords.
- System Console users list no longer throws an error when trying to demote a member from a System Admin.
- iOS radio buttons no longer stay selected when switching between options.
- Email addresses now display for System Admins even if hidden in the System Console.
- Code themes now save when updated via Account settings.
- File name is now displayed instead of the full path to the file in code snippet previews.
- Config settings are refreshed immediately when **Reload Configuration from Disk** is clicked.
- Preview feature checkboxes now reset after changes are canceled.
- Updated the markdown parser to fix poor handling of certain links.
- Error box highlighting on the claim AD/LDAP account page is fixed to only highlight the invalid input box.
- Errors in the system console are now properly aligned.
- Button to resend verification email no longer throws an error when clicked.
- Direct Messages modal loads faster since it is no longer cleared from memory each time it closes.
- Graphs in the **System Console > Site Statistics** now have the same start date for comparison.
- Fixed an issue where new languages are not added by default. Any server which is upgraded to Mattermost v3.1 will need to manually set **System Console > Localization > Available Languages** blank to have new languages added by default.
- Previously, a few shortcuts that used CTRL were overwriting existing messaging shortcuts in Mac. This has been changed so they only work with CMD. See [documentation](http://docs.mattermost.com/help/messaging/keyboard-shortcuts.html) for more details.
- Email body now contains the `siteURL` when inviting a user by email via CLI (command line interface)
- YouTube videos now stop playing when collapsed.
- Fixed error when adding an incoming webhook to a public channel the user is currently not in.
- Error merssage displayed on password reset page is now formatted correctly.


### Compatibility
Changes from v3.1 to v3.2:

#### config.json   

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json` or the System Console.

**Changes to Team Edition and Enterprise Edition**:

- Under `EmailSettings` in `config.json`:
   - Added `"FeedbackOrganization": ""` to specify organization name and address, which will be displayed on email notifications from Mattermost.

- Under `ServiceSettings` in `config.json`:
   - Added `"EnableCustomEmoji": false`. When set to `true`, enables Custom Emoji option in the Main Menu where users can create customized emoji.

- Under `LocalizationSettings` in `config.json`:
   - Changed: `"AvailableLocales": ""` to allow new languages be added by default.

- Under `LogSettings` in `config.json`:
   - Added `"EnableWebhookDebugging": true`. When set to `true`, contents of incoming webhooks are printed to log files for debugging.

**Additional Changes to Enterprise Edition:**    

The following config settings will only work on servers with an Enterprise License that has the feature enabled.

- Under `TeamSettings` in `config.json`:
   - Added `"RestrictTeamInvite": "all"` to set the permissions required to send team invites.
   - Added `"RestrictPublicChannelManagement": "all"` to set the permissions required to manage public channels.
   - Added `"RestrictPrivateChannelManagement": "all"` to set the permissions required to manage private channels.

- Under `ServiceSettings` in `config.json`:
   - Added `"RestrictCustomEmojiCreation": "all"` to set the permissions required to create custom emoji.

- Under `SamlSettings` in `config.json`:
   - Added `"Enable": false` to allow login using SAML. See [documentation](http://docs.mattermost.com/deployment/sso-saml.html) to learn more about configuring SAML for Mattermost.
   - Added `"Verify": false` to control whether Mattermost verifies the signature sent from the SAML Response matches the Service Provider Login URL.
   - Added `"Encrypt": false`to control whether Mattermost will decrypt SAML Assertions encrypted with your Service Provider Public Certificate.
   - Added `"IdpUrl": ""` to set the SAML SSO URL where Mattermost sends a SAML request to start login sequence.
   - Added `"IdpDescriptorUrl": ""` to set the Identity Provider Issuer URL for the Identity Provider you use for SAML requests.
   - Added `"AssertionConsumerServiceURL": ""` to set the Service Provider Login URL.
   - Added `"IdpCertificateFile": ""` to set the public authentication certificate issued by your Identity Provider.
   - Added `"PublicCertificateFile": ""` to set certificate used to generate the signature on a SAML request to the Identity Provider for a service provider initiated SAML login, when Mattermost is the Service Provider.
   - Added `"PrivateKeyFile": ""` to set the private key used to decrypt SAML Assertions from the Identity Provider.
   - Added `"FirstNameAttribute": ""` to set the attribute in the SAML Assertion that will be used to populate the first name of users in Mattermost.
   - Added `"LastNameAttribute": ""` to set the attribute in the SAML Assertion that will be used to populate the last name of users in Mattermost.
   - Added `"EmailAttribute": ""` to set the attribute in the SAML Assertion that will be used to populate the email of users in Mattermost.
   - Added `"UsernameAttribute": ""` to set the attribute in the SAML Assertion that will be used to populate the username of users in Mattermost.
   - Added `"NicknameAttribute": ""` to set the attribute in the SAML Assertion that will be used to populate the nickname of users in Mattermost.
   - Added `"LocaleAttribute": ""` to set the attribute in the SAML Assertion that will be used to populate the language of users in Mattermost.
   - Added `"LoginButtonText": ""` set the text that appears in the login button on the login page.

- Under `LdapSettings` in `config.json`:
   - `"FirstNameAttribute": ""`, `"LastNameAttribute": ""`, `"BindUsername": ""`, and `"BindPassword": ""` are now required fields.
   - Added `"MaxPageSize": 0` to set the maximum number of users that will be requested from the AD/LDAP server at one time.

#### Database Changes from v3.1 to v3.2

**TeamMembers Table**    
- Added `DeleteAt` column.

**Emoji Table**    
- Added `Emoji` table.

### Known Issues

- In System Console > Notifications > Email the "Test Connection" button does not properly use the saved SMTP password. The temporary workaround is to re-type your SMTP Server Password into the field prior to using the "Test Connection", and then to "Save" afterwards.
- The behavior of setting for Link Previews in Account Settings is reversed.
- “More” option under Direct Message list no longer shows count of team members not in your direct message list.
- Webhook attachments don't show up in search results.
- On Firefox, System Console sidebar completely disappears when an AD/LDAP setting is saved.
- On Firefox, CTRL/CMD+U keyboard shortcut doesn't work.
- `/join` sometimes throws an error.
- Sometimes only the last character typed in the channel switcher appears.
- Formatting of multiple lists in a row breaks markdown.
- Hitting the URL of a private team you used to belong to shows a blank Team Selection page.
- Accessing the System Console URL when logged out causes the browser to hang.
- Youtube videos show as "Video not found" on Desktop App
- Search terms contained in hashtags are not highlighted in the search results.
- Files sent in private messages to members in a different team are not accessible.
- Center channel appears blank after initial page load on iOS.

### Contributors

Many thanks to all our contributors. In alphabetical order:

/mattermost-server
- [42wim](https://github.com/42wim), [apheleia](https://github.com/apheleia), [asaadmahmood](https://github.com/asaadmahmood), [coreyhulen](https://github.com/coreyhulen),[crspeller](https://github.com/crspeller), [DavidLu1997](https://github.com/DavidLu1997), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [hmhealey](https://github.com/hmhealey), [iansim](https://github.com/iansim), [it33](https://github.com/it33), [jwilander](https://github.com/jwilander), [kevynb](https://github.com/kevynb), [lfbrock](https://github.com/lfbrock), [samogot](https://github.com/samogot), [tbalthazar](https://github.com/tbalthazar), [tehraven](https://github.com/tehraven), [thiyagaraj](https://github.com/thiyagaraj), [yumenohosi](https://github.com/yumenohosi)

/ios  
- [coreyhulen](https://github.com/coreyhulen)

/desktop    
- [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [magicmonty](https://github.com/magicmonty), [Razzeee](https://github.com/Razzeee), [yuya-oc](https://github.com/yuya-oc)

/docs    
- [apheleia](https://github.com/apheleia), [asaadmahmood](https://github.com/asaadmahmood), [crspeller](https://github.com/crspeller), [esethna](https://github.com/esethna), [Fonata](https://github.com/Fonata), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [lfbrock](https://github.com/lfbrock), [lindy65](https://github.com/lindy65), [npcode](https://github.com/npcode), [yangchen1](https://github.com/yangchen1)

/mattermost-driver-javascript    
- [coreyhulen](https://github.com/coreyhulen), [crspeller](https://github.com/crspeller), [DavidLu1997](https://github.com/DavidLu1997), [enahum](https://github.com/enahum), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [samogot](https://github.com/samogot)

/mattermost-docker
- [npcode](https://github.com/npcode)

/mattermost/push-proxy
- [coreyhulen](https://github.com/coreyhulen)

If we missed your name, please let us know at feedback@mattermost.com. Recognition is a manual process and mistakes can happen. We want to include anyone who's made a pull request that got merged during the release.

## Release v3.1.0

Release date: 2016-06-16

### Security Update

- Mattermost v3.1.0 contains [multiple security updates](http://about.mattermost.com/security-updates/). [Upgrading to Mattermost v3.1.0](http://docs.mattermost.com/administration/upgrade.html) is highly recommended.
- Thanks to Uchida Taishi for contributing security reports through the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Highlights

#### Keyboard shortcuts and channel switcher

- Added keyboard shortcuts for navigation, messages and files
- Added channel switcher available from CTRL+K in Windows and CMD+K on Mac.
- See [shortcut documentation](http://docs.mattermost.com/help/messaging/keyboard-shortcuts.html) or use the `/shortcuts` slash command for details.

#### Upgraded System Console

- Re-organized System Console to make settings easier to find for new users.
- Added setting to set default server and client languages.

#### Upgraded Push Notification options

- Added ability for mobile push notifications to trigger on only mentions, all activity and no activity, configurable from **Account Settings** > **Notifications** > **Mobile push notifications**
- Added ability to trigger mobile push notifications while user is logged into Mattermost on desktop.

#### Compact View

- Added "Compact" view option to display more text on a smaller screen, configurable from **Account Settings** > **Display** > **Message Display**.

### Improvements

iOS App
- Account Settings > Notifications option lets users to enable mobile push notifications for chosen activities.
- Push notifications sent even if a user is online on desktop.
- Removed auto-capitalization on login screen, so email is no longer capitalized.

Android App
- Account Settings > Notifications option lets users to enable mobile push notifications for chosen activities.
- Push notifications sent even if a user is online on desktop.
- Removed auto-capitalization on login screen, so email is no longer capitalized.

User Interface

- Account Settings > Display option lets users set channels to compact view.
- Autocomplete closes with ESC button.
- Sequential messages with a username also show profile pictures.
- Channel introduction message conforms to the channel width chosen in Account Settings > Display.
- The message '[user] is typing' now uses the username instead of the display name.
- Date markers now show absolute time.

Performance

- Performance improvements to posting and replying.
- Online status in Direct Message list updated on first load.

Notifications

- `@all` mention added back with equivalent functionality to `@channel`.
- An email notification is now sent when username is changed.

Channels
- Removed the option to leave a channel for the last person in a private group, so private groups can no longer end up in an ownerless state.

Messaging

- Move link preview toggle out of preview feature list and add /collapse and /expand.

Localization

- New settings to configure localization options for teams, including default language.
- [Mattermost Translation Server](http://translate.mattermost.com/) upgraded to better support [localization process](http://docs.mattermost.com/developer/localization.html).

Integrations

- Integrations now support advanced formatting through [message attachments](http://docs.mattermost.com/developer/message-attachments.html).
- Added support for sending `@channel` notifications by using `<!channel>`.
- Added support for raw new lines in the text payload.
- Added validation for command trigger words.

Onboarding

- Slash command `/invite_people [email address]` sends an email invite to your Mattermost team.

Enterprise

- (E10 and higher): Added AD/LDAP synchronization to automatically deactivate Mattermost accounts after AD/LDAP accounts are deactivated. Previous behavior only checked AD/LDAP credentials on sign-in. Synchronization time defaults to one hour and is configurable from **System Console** > **Synchronization Interval**.
- (E20 and higher): Added support for [high availability database configurations](http://docs.mattermost.com/deployment/ha.html) using read replicas and a manual failover process to deploy database reconfigurations without stopping the Mattermost server.

### Bug Fixes

- Incoming webhooks have been made available in all public channels, and in private channels the user belongs to.
- A space between two named emojis is no longer required for correct rendering.
- Emojis now render inside parenthesis or brackets.
- Links that are enclosed with a right parenthesis now work properly.
- Search term highlighting now updates when search terms change but return the same posts.
- Search results now properly highlight for searches containing @username, non-latin characters, terms inside Markdown code blocks, and hashtags containing a dash.
- A single numbered item no longer resets numbering to 1.
- Previews for removed YouTube videos no longer throw a 404 error.
- Team and System Admins can now update channel settings after leaving and rejoining the channel.
- After initial load on iOS, centre channel no longer appears blank.
- When creating a team with a new account, channel introduction message is now displayed.
- Sidebar notification for direct messages now clear once viewed, regardless of which team you are in.
- Custom brand image size is now properly limited on IE11.

### Compatibility  
Changes from v3.0 to v3.1:

**config.json**    

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json` or the System Console.

**Changes to Team Edition and Enterprise Edition**:

 - Under `LocalizationSettings` in `config.json`:
    - Added `"DefaultServerLocale": “en”` to set default language for the system messages and logs
    - Added `"DefaultClientLocale": “en”` to set default language for newly created users and for pages where the user hasn't logged in
    - Added `"AvailableLocales": “en,es,fr,ja,pt-BR”` to set which languages are available for users in Account Settings. The language specified in `DefaultClientLocale` should be included in this list.

**Additional Changes to Enterprise Edition:**    

The following config settings will only work on servers with an Enterprise License that has the feature enabled.

 - Under `LdapSettings` in `config.json`:
    - Added `"SyncIntervalMinutes": "60"` to allow system admins adjust how frequently Mattermost performs AD/LDAP synchronization to update users

### Known Issues

- “More” option under Direct Message list no longer shows count of team members not in your direct message list.
- Emoji smileys ending with a letter at the end of a message do not auto-complete as expected.
- Incorrect formatting when a new line is added directly after a list.
- On Postgres databases, searching for websites and emails does not work properly and hashtags which end with an inverted questionmark aren't properly highlighted.
- On Firefox, search results for hashtags are not properly highlighted.
- Clicking on a desktop notification from another team doesn’t open the team.
- Webhook attachments don't show up in search results.
- On Firefox, System Console sidebar completely disappears when an AD/LDAP setting is saved
- On Firefox, CTRL/CMD+U keyboard shortcut doesn't work
- Copying and pasting an image from a browser doesn't work
- Youtube videos continue playing when collapsed
- Code theme under Account Settings > Display > Theme doesn't save unless entered in vectorized form
- `/join` sometimes throws an error
- When upgrading to 3.X, syntax highlighting using Solarized code theme is lost
- In Compact view, clicking on a file in the first post in the right hand sidebar attempts to download the file
- Unable to leave a private channel in mobile view
- `@all` notifications received even after being unselected from notification options
- Channel header disappears after renaming a channel (fixed with channel switch)
- Updates to **System Console** > **Privacy** settings for existing users requires a session update
- Invalid config setting causes server to panic on start

### Contributors

Many thanks to all our contributors. In alphabetical order:

/mattermost-server
- [apheleia](https://github.com/apheleia), [ArthurHlt](https://github.com/ArthurHlt), [asaadmahmood](https://github.com/asaadmahmood), [coreyhulen](https://github.com/coreyhulen), [crspeller](https://github.com/crspeller), [DavidLu1997](https://github.com/DavidLu1997), [enahum](https://github.com/enahum), [goofy-bz](https://github.com/goofy-bz), [gramakri](https://github.com/gramakri), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jwilander](https://github.com/jwilander), [kevynb](https://github.com/kevynb), [khoa-le](https://github.com/khoa-le), [lfbrock](https://github.com/lfbrock), [rompic](https://github.com/rompic), [ryoon](https://github.com/ryoon), [samogot](https://github.com/samogot), [ScriptAutomate](https://github.com/ScriptAutomate), [tbalthazar](https://github.com/tbalthazar), [tehraven](https://github.com/tehraven/)

/ios
- [coreyhulen](https://github.com/coreyhulen), [lfbrock](https://github.com/lfbrock)

/android
- [coreyhulen](https://github.com/coreyhulen), [DavidLu1997](https://github.com/DavidLu1997), [it33](https://github.com/it33), [lfbrock](https://github.com/lfbrock), [nineinchnick](https://github.com/nineinchnick)

/desktop
- [CarmDam](https://github.com/CarmDam), [it33](https://github.com/it33), [jnugh](https://github.com/jnugh), [MetalCar](https://github.com/MetalCar), [Razzeee](https://github.com/Razzeee), [yuya-oc](https://github.com/yuya-oc)

/docs    
- [apheleia](https://github.com/apheleia), [coreyhulen](https://github.com/coreyhulen), [crspeller](https://github.com/crspeller), [DavidLu1997](https://github.com/DavidLu1997), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [hannaparks](https://github.com/hannaparks), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [lfbrock](https://github.com/lfbrock), [maxlmo](https://github.com/maxlmo), [mkhsueh](https://github.com/mkhsueh), [npcode](https://github.com/npcode), [TwizzyDizzy](https://github.com/TwizzyDizzy)

/mattermost-driver-javascript    
- [coreyhulen](https://github.com/coreyhulen), [crspeller](https://github.com/crspeller), [enahum](https://github.com/enahum), [jwilander](https://github.com/jwilander)

/mattermost-docker    
- [npcode](https://github.com/npcode), [pierreozoux](https://github.com/pierreozoux)

/mattermost/push-proxy    
- [coreyhulen](https://github.com/coreyhulen)

/mattermost/mattermost-docker-preview    
- [crspeller](https://github.com/crspeller)

If we missed your name, please let us know at feedback@mattermost.com. Recognition is a manual process and mistakes can happen. We want to include anyone who's made a pull request that got merged during the release.

## Release v3.0.3

Release date: 2016-05-27

Notes on patch releases:
- v3.0.3, released 2016-05-27
   - Fixed an error with AD/LDAP signup if user already existed.
   - Fixed an error where setting language to one of the supported langugages caused a blank page.
   - Fixed an error where upgrading team admins on the primary team with AD/LDAP and Gitlab accounts caused an error.
- v3.0.2, released 2016-05-17
   - Security update to reduce information disclosure, thanks to Andreas Lindh for [reporting responsibly](http://www.mattermost.org/responsible-disclosure-policy/)
   - Fixed an error where, when using Postgres, attempting to log in with an AD/LDAP that has the same email address or username as an email-based account shows a confusing error message.
   - Fixed an error accounts using email authentation attempt to create new teams.
   - Fixed an error where if you upgrade having never previously saved config.json from System Console, saving from System Console will not work.
- v3.0.1, released 2016-05-16
   - v3.0.1 fixed an error in GitLab SSO, thanks to [ArthurHlt](https://github.com/ArthurHlt) for the pull request fixing the issue.
- v3.0.0, released 2016-05-16
   - Original 3.0 release.

### Security Update

- Mattermost v3.0.3 contains multiple security updates. [Upgrading to Mattermost v3.0.3](http://docs.mattermost.com/administration/upgrade.html#upgrading-to-team-edition-3-0-x-from-2-x) is highly recommended.
- Thanks to Yoni Ramon from the Tesla security team, Andreas Lindh and Uchida Ta for contributing security reports through the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Major Version Release

Mattermost 3.0 is a new major version of Mattermost with fundamental changes affecting Mattermost 2.x deployments. [An understanding of the upgrade process from 2.x to 3.0](http://www.mattermost.org/upgrading-to-mattermost-3-0/), including manual steps, is required to upgrade successfully.

### Highlights

#### Unified Accounts

- Users manage a single account across multiple teams
- Users from different teams can share messages and files
- Improved multi-team login and sign-up experience

#### Enterprise Edition Security, Authentication and Branding Upgrades

- Added multi-factor authentication
- Added multiple Active Directory/LDAP upgrades (TLS, filters, custom labels, nickname support)
- Added tools for custom branding

#### User Interface Upgrades
- New Emoji set
- Added full width option for text display
- Improved UI for managing webhooks and slash commands

#### iOS and Android mobile app improvements
- Added support for multiple teams
- New option to include message snippets in push notifications
- Added auto-correct

### Languages

- Added Japanese translation for user interface.

### Improvements

iOS app
- Added support for multiple teams on the same server.
- Added autocorrect.
- Note: Users of Mattermost 3.0 server need to install new iOS 3.0 app. iOS 2.x apps are not compatible with Mattermost 3.0 server. Also, iOS 3.0 app is not compatible with Mattermost 2.x server.

Android app
- Added support for multiple teams on the same server.
- Added autocorrect.
- Note: Users of Mattermost 3.0 server need to install new Android 3.0 app. Android 2.x apps are not compatible with Mattermost 3.0 server. Also, Android 3.0 app is not compatible with Mattermost 2.x server.

User Interface
- Switched to new emoji set.
- Account Settings > Display option lets users set the channel view to full width.
- Smoother overlay transition when opening sidebar on mobile.
- Back and forward browser buttons can now move back and forward in channel history.

Integrations
- Moved webhooks and slash command settings to a new “Integrations” page.
- Added "Display Name" and “Description” to incoming and outgoing webhooks.
- Changed webhooks to always show the username and profile picture, even if posts are consecutive.
- Added a /msg command to open a direct message channel with another user.

Authentication
- Changed the user model so accounts are per server instead of per team.
- Updated the login flow so users can select which team to open after signing in.
- Combined Email, Username, and AD/LDAP options into one login box so users can enter their credentials and the system will identify which kind of authentication to use.
- GitLab SSO now creates an account from the "Sign In" button if an account previously did not exist.

Files and Attachments
- Added a preview for code files in the image viewer.

Notifications
- Added the option to enable full snippets in push notifications.

Search
- Changed searches to connect terms with "AND" instead of "OR".

Enterprise:
- Added the ability to map nickname to an AD/LDAP field.
- Added the ability to filter AD/LDAP users, so only users selected by the filter can log in to Mattermost.
- Added the option to connect to AD/LDAP with TLS or STARTTLS
- Added the option to replace the “AD/LDAP username” login field placeholder text with custom text.
- Users can now switch between AD/LDAP and email login from Account Settings > Security > Sign-in Method.
- Added the option to sign up with AD/LDAP on the "Get Team Invite" link and email invite sign up pages.
- Added multi-factor authentication.
- Added compliance reporting and the option to generate daily compliance reports.
- Added custom branding, so System Admins can set a custom logo and text on the sign in page.
- Added a command line option to upload a license file.

### Bug Fixes

- Posts from webhooks now fire notifications to the user who created the webhook.
- Edit post option no longer appears, but doesn't work, on other users' posts in the right-hand sidebar.
- Text input box does not stay scrolled to the bottom when drafting a long message in Firefox.
- Webhooks in search results now show the username/profile pic of the bot, instead of the user who set up the webhook.
- Outgoing webhooks triggers now work when followed by any type of white space, instead of only spaces
- "User is typing" message now follows Teammate Name Display setting
- Log in with GitLab on mobile now works in the case where there is a space after the email address
- Links in System Console > Legal and Support settings now open properly even if http or https is not included
- Timestamps are displayed in 12-hour format when set to 24-hour format.

### Compatibility  
Changes from v2.2 to v3.0:

**iOS and Android**  

Mattermost iOS and Android app v3.0 requires Mattermost server v3.0 and higher.

**APIs**

Web Service API is upgraded to Version 3 and previous Version 1 API is no longer supported. Golang driver, Javascript driver, incoming and outgoing webhooks and Slash commands continue to function as in previous release

**config.json**    

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json` or the System Console.  

**Changes to Team Edition and Enterprise Edition**:

- Under `TeamSettings` in `config.json`:
    - Added `"EnableOpenServer": false` to set whether users can sign up to the server without an invite.    
    - Removed `"EnableTeamListing": false` since the team directory was replaced with new functionality.

- Under `EmailSettings` in `config.json`:
    -  Added `"PushNotificationContents": "generic"` to set whether push notifications send a generic message (`generic`) or send a snippet of the conversation (`full`)

- Under `SupportSettings` in `config.json`, default support links were changed and need to be manually updated for existing installs:
    - Changed: `"TermsOfServiceLink": "https://about.mattermost.com/default-terms/"`
    - Changed: `"PrivacyPolicyLink": "https://about.mattermost.com/default-privacy-policy/"`
    - Changed: `"AboutLink": "https://about.mattermost.com/default-about/"`
    - Changed: `"HelpLink": "https://about.mattermost.com/default-help/"`
    - Changed: `"ReportAProblemLink": "https://about.mattermost.com/default-report-a-problem/"`
    - Changed: `"SupportEmail": "feedback@mattermost.com"`

**Additional Changes to Enterprise Edition:**    

The following config settings will only work on servers with an Enterprise License that has the feature enabled.

- Under `ServiceSettings` in `config.json`:
  - Added `"EnableMultifactorAuthentication": false` to enable Multifactor Authentication

- Under `TeamSettings` in `config.json`:
    -  Added `"EnableCustomBrand": false` to set whether custom branding of the login page is turned on.
    -  Added `"CustomBrandText": ""` to set what text will show up on the login page, if `"EnableCustomBrand":` is set to `true`.

- Under `LdapSettings` in `config.json`:
    - Added `"ConnectionSecurity":""` to set the type of connection security Mattermost uses to connect to AD/LDAP. Options are `""` (no security), `TLS` or `STARTTLS`.
    - Added `"UserFilter": ""` (optional) to set an AD/LDAP Filter to use when searching for user objects.
    - Added `"NicknameAttribute": ""` to set the attribute in the AD/LDAP server that will be used to populate the nickname field in Mattermost.
    - Added `"SkipCertificateVerification": false` to set whether the certificate verification step for TLS or STARTTLS connections is skipped. (For testing purposes only. Should be set to `false` in production.)
    - Added `"LoginFieldName": ""` to set the help text in the login box (for example, AD/LDAP username or Company username).

- Added `ComplianceSettings` to `config.json`:
    - Added `"Enable": false` to set whether compliance reports are enabled.
    - Added `"Directory": "./data/"` to set where the reports are stored.
    - Added `"EnableDaily": false` to set whether Daily Reports are turned on.

#### Database Changes from v2.2 to v3.0

Version 3.0 uses a different database than version 2.0. A one-way change to the database will be required when upgrading from v2.2 to v3.0.  

### Known Issues

- “More” option under Direct Message list no longer shows count of team members not in your direct message list.
- Emoji smileys ending with a letter at the end of a message do not auto-complete as expected.
- Incorrect formatting when a new line is added directly after a list.
- Searching for a username or hashtag containing a dot now returns the correct results.
- On Postgres databases, searching for websites, emails, and searching with quotations does not work properly.
- Search term highlighting doesn't update when search terms change but return the same posts.
- Search results don't highlight properly for searches containing @username, non-latin characters, terms inside Markdown code blocks, or hashtags containing a dash.
- Custom brand image size isn’t properly limited on IE11.

### Contributors

Many thanks to all our contributors. In alphabetical order:

/mattermost-server
- [alanmoo](https://github.com/alanmoo), [ArthurHlt](https://github.com/ArthurHlt), [asaadmahmood](https://github.com/asaadmahmood), [augustohp](https://github.com/augustohp),  [brunoqc](https://github.com/brunoqc), [chengweiv5](https://github.com/chengweiv5), [Compaurum](https://github.com/Compaurum), [coreyhulen](https://github.com/coreyhulen), [crspeller](https://github.com/crspeller), [CyrilTerets](https://github.com/CyrilTerets), [DavidLu1997](https://github.com/DavidLu1997), [enahum](https://github.com/enahum), [FeliciousX](https://github.com/FeliciousX), [hauschke](https://github.com/hauschke), [hmhealey](https://github.com/hmhealey), [insin](https://github.com/insin), [it33](https://github.com/it33), [jwilander](https://github.com/jwilander), [khoa-le](https://github.com/khoa-le), [lfbrock](https://github.com/lfbrock), [loafoe](https://github.com/loafoe), [maruTA-bis5](https://github.com/maruTA-bis5), [moogle19](https://github.com/moogle19), [olivierperes](https://github.com/olivierperes), [pjgrizel](https://github.com/pjgrizel), [qcu](https://github.com/qcu), [rodrigocorsi2](https://github.com/rodrigocorsi2), [ryoon](https://github.com/ryoon), [samogot](https://github.com/samogot), [stupied4ever](https://github.com/stupied4ever), [takashibagura](https://github.com/takashibagura), [usmanarif](https://github.com/usmanarif), [yumenohosi](https://github.com/yumenohosi)

/mattermost-docker
- [npcode](https://github.com/npcode), [xcompass](https://github.com/xcompass), [it33](https://github.com/it33)

/ios
- [coreyhulen](https://github.com/coreyhulen), [it33](https://github.com/it33)

/android
- [arusahni](https://github.com/arusahni), [JohnMaguire](https://github.com/JohnMaguire), [lindy65](https://github.com/lindy65), [nicolas-raoul](https://github.com/nicolas-raoul), [ptersilie](https://github.com/ptersilie)

/desktop
- [asaadmahmood](https://github.com/asaadmahmood), [it33](https://github.com/it33), [jeremycook](https://github.com/jeremycook), [lloeki](https://github.com/lloeki), [mgielda](https://github.com/mgielda), [yuya-oc](https://github.com/yuya-oc)

/docs
- [ajerezr](https://github.com/ajerezr), [apheleia](https://github.com/apheleia), [asaadmahmood](https://github.com/asaadmahmood), [crspeller](https://github.com/crspeller), [DavidLu1997](https://github.com/DavidLu1997), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [it33](https://github.com/it33), [lfbrock](https://github.com/lfbrock), [lindy65](https://github.com/lindy65), [pjgrizel](https://github.com/pjgrizel), [schemacs](https://github.com/schemacs)

## Release v2.2.0

Release date: 2016-04-16

### Security Update

- Mattermost v2.2.0 contains multiple security updates. [Upgrading to Mattermost v2.2.0](http://docs.mattermost.com/administration/upgrade.html#upgrading-team-edition) is highly recommended.
- Thanks to Jim Hebert from Fitbit Security, Andreas Lindh, and Uchida Taishi for contributing security reports through the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Highlights

#### New themes

- User now have access to additional themes from Account Settings > Display Settings > Themes > See other themes
- A [contest for the user community to contribute new themes is now available.](https://forum.mattermost.org/t/share-your-favorite-mattermost-theme-colors/1330)

#### French language translation

- French language translation is now available.

#### TPNS and EAS options

- [Enterprise App Store](http://docs.mattermost.com/deployment/push.html#enterprise-app-store-eas) (EAS) and [Test Push Notification Service](http://docs.mattermost.com/deployment/push.html#test-push-notifications-service-tpns) (TPNS) option are now included in **System Console** > **Email Settings** > **Push Notification Settings** as built-in options.

### Languages

- Added French language translation (Beta) available from **Account Settings** > **Display**.

### Improvements

User Interface

- New themes can be imported into Mattermost user interface from [production documentation](http://docs.mattermost.com/help/settings/theme-colors.html#custom-theme-examples).

### Bug Fixes

- Characters in some posts will no longer display as HTML entities, such as `&#39;`

### Known Issues

- Regression: Get Public Link downloads a file and does not product a public link.
- Edit post option appears, but doesn't work, on other users' posts in the right-hand sidebar.
- Text input box does not stay scrolled to the bottom when drafting a long message in Firefox.
- File name tooltip stays open after clicking to download.
- Unable to paste images into the text box on Firefox, Safari, and IE11.
- Archived channels are not removed from the "More" menu for the person that archived the channel until after refresh.
- First load of an empty channel does not display the introduction message.
- Search results don't highlight searches for @username, non-latin characters, or terms inside Markdown code blocks.
- Searching for a username or hashtag containing a dot returns a search where the dot is replaced with the "or" operator.
- Hashtags containing a dash incorrectly highlight in the search results.
- Emoji smileys ending with a letter at the end of a message do not auto-complete as expected.
- Incorrect formatting when a new line is added directly after a list.
- Timestamps are displayed in 12-hour format when set to 24-hour format.
- Syntax highlighting code block is missing the label for Latex documents.
- Posts from webhooks do not fire notifications to the user who created the webhook.
- Theme color vector is not updated after making custom changes to a default theme.
- Search term highlighting doesn't update on IE11 when search terms change but return the same posts.
- Team creation via SSO fails when email domain is restricted.

### Contributors

Many thanks to all our external contributors. In no particular order:

- [pjgrizel](https://github.com/pjgrizel), [tbolon](https://github.com/tbolon) , [jblobel](https://github.com/jblobel), [rodrigocorsi2](https://github.com/rodrigocorsi2) , [enahum](https://github.com/enahum), [schemacs](https://github.com/schemacs), [raelga](https://github.com/raelga)

## Release v2.1.0

Release date: 2016-03-16

### Highlights

- New Android application now available.
- New desktop applications for Windows, Mac and Linux now in beta.
- Brazilian Portuguese translation added.

### Security Update

Mattermost v2.1.0 contains a security update for a cross-site scripting vulnerability in Mattermost v1.2, v1.3, v1.4 and v2.0. [Upgrading to Mattermost v2.1.0](http://docs.mattermost.com/administration/upgrade.html#upgrading-team-edition) is highly recommended. Thanks to Luke Arntson for the [RPD report](https://www.mattermost.org/responsible-disclosure-policy/).

### New Features

Android Application

- New [Mattermost Android App](https://github.com/mattermost/android) supporting push notifications available for devices running Android 4.4.2+. Requires Mattermost server 2.1 and higher. See [list of tested devices](https://github.com/mattermost/android/blob/master/DEVICES.md).

Desktop Application

- New [Desktop Application](https://github.com/mattermost/desktop) for Windows, Mac, and Linux now available as a beta release.

Languages

- Added Portuguese language translation (Beta) available from **Account Settings** > **Display**.

### Improvements

System Console

- Removed unused “Disable File Storage” option from the System Console as it is no longer relevant.
- Added a warning message if a system admin demotes themselves.
- System Console statistics now use a client store instead of fetching data and storing it in state.

Messaging

- Custom slash commands now support temporary messages that appear only to the user that issued the command.
- Username autocomplete list no longer suggests inactive users.

Mobile

- Significant responsiveness and speed improvements using [fastclick](https://github.com/ftlabs/fastclick).
- Team name and username are now shown in the LHS header.
- Added a button to go back to the team URL page from the login page.

Files and Images

- Increased the maximum size of image uploads to 24 megapixels.

User Interface

- Custom theme color selectors are now organized into categories.
- Add Members and Manage Members dialogs can now be filtered using a search bar.
- Deactivated members no longer appear in the channel members list.
- Keyboard focus is set to the text input box in the right-hand sidebar if a user clicks the reply icon.
- Permalinks are now displayed in a Copy Permalink dialog instead of a popover.
- Permalink option is now available from the [...] menu on messages and comments in the right-hand sidebar.
- Reply icon now only appears on-hover for messages that don’t have replies.
- Scroll bar now appears in the center channel.

#### Bug Fixes

- System console user management tab now shows username and email on different lines.
- Yellow text box error no longer appears when the system is connected.
- Wildcard search on MySQL databases is now fixed.
- Usernames in the center channel no longer appear as “...” on login.
- Deleted messages now delete in the right-hand sidebar and center channel without requiring a page refresh.
- Contact us email address in the footer of notification emails now uses the SupportEmail config setting instead of FeedbackEmail.
- Email addresses are now required to have at least one letter before and after the @ sign.
- Firefox desktop notifications are now fixed for some users experiencing missed notifications.
- “User is typing” message containing long usernames no longer causes text wrapping.
- Usernames appearing as “...” in the right-hand sidebar when performing a search is fixed.
- Links that end in image extensions but do not actually link to raw images no longer generate a blank image preview.
- Channel handle field in the Rename Channel dialog is now visible on themes with dark backgrounds.
- Autolinked images no longer persist after the post containing the link is deleted.
- Code theme selector on IE11 now only shows one dropdown arrow and clicking directly on the arrow opens the dropdown.
- Save/Cancel buttons for language selection in Account Settings are now formatted the same as other settings.
- Inconsistent field spacing in the Channel Info dialog is fixed.
- Recent mentions icon no longer jumps to the left of the search bar when the right-hand sidebar is opened.
- Custom slash command hints now show up in the autocomplete list.
- GIF links inside code blocks no longer auto-post the GIFs.
- Changing usernames no longer adds the old username to “words that trigger mentions”.
- Notification email footer is now translated based on the sender’s language setting.
- Slash command `/me` now posts as the user instead of a webhook message.
- Logout slash command now forces logout.
- Public links to file attachments on deleted posts no longer work.
- Error message is now shown in IE11 when uploading more than 5 files or a file over 50 MB.


### Compatibility  
Changes from v2.0 to v2.1:

**Android**  
- Mattermost Android Application is for use with Mattermost server v2.1 and higher.

**config.json**    
- The following setting was added and can be modified under `ServiceSettings` in `config.json` or the System Console.  
    - `"AllowCorsFrom": ""` to allow the system to serve HTTP requests to other domains specified.

#### Known Issues

- Edit post option appears, but doesn't work, on other users' posts in the right-hand sidebar.
- Text input box does not stay scrolled to the bottom when drafting a long message in Firefox.
- Some characters in posts may display as HTML entities, such as `&#39;`. This can be fixed by switching to a different language and then back again.
- File name tooltip stays open after clicking to download.
- Unable to paste images into the text box on Firefox, Safari, and IE11.
- Archived channels are not removed from the "More" menu for the person that archived the channel until after refresh.
- First load of an empty channel does not display the introduction message.
- Search results don't highlight searches for @username, non-latin characters, or terms inside Markdown code blocks.
- Searching for a username or hashtag containing a dot returns a search where the dot is replaced with the "or" operator.
- Hashtags containing a dash incorrectly highlight in the search results.
- Emoji smileys ending with a letter at the end of a message do not auto-complete as expected.
- Incorrect formatting when a new line is added directly after a list.
- Timestamps are displayed in 12-hour format when set to 24-hour format.
- Syntax highlighting code block is missing the label for Latex documents.
- Posts from webhooks do not fire notifications to the user who created the webhook.
- Theme color vector is not updated after making custom changes to a default theme.
- Search term highlighting doesn't update on IE11 when search terms change but return the same posts.
- Team creation via SSO fails when email domain is restricted.

#### Contributors

Many thanks to all our external contributors. In no particular order:

- [yuya-oc](https://github.com/yuya-oc), [rodrigocorsi2](https://github.com/rodrigocorsi2), [enahum](https://github.com/enahum), [khoa-le](https://github.com/khoa-le), [alanmoo](https://github.com/alanmoo), [daizenberg](https://github.com/daizenberg), [GuillaumeAmat](https://github.com/GuillaumeAmat), [kernicPanel](https://github.com/kernicPanel), [timlyo](https://github.com/timlyo), [ttyniwa](https://github.com/ttyniwa)

## Release v2.0.0

Expected Release date: 2016-02-16

### Highlights

#### Incremented Version Number: Mattermost "2.0"

- Version number incremented from "1.x" to "2.x" indicating major product changes, including:

##### Localization

- Addition of localization support to entire user interface plus error and log messages
- Added Spanish language translation (Beta quality) available from **Account Settings** > **Display**

##### Enhanced Support for Mobile Devices

- BREAKING CHANGE to APIs: New Android and updated iOS apps require Mattermost server 2.0 and higher
- iOS added app support for GitLab single sign-on
- iOS added app support for AD/LDAP single sign-on (Enterprise Edition only)

##### Upgrade and Deployment Improvements
- Mattermost v2.0 now upgrades from up to two previous major builds (e.g. v1.4.x and v1.3.x)
- Added option to allow use of insecure TLS outbound connections to allow use of self-signed certificates

### New Features

Localization

- Addition of localization support to entire user interface plus error and log messages
- Added Spanish language translation (Beta quality) available from **Account Settings** > **Display**

Slash Commands

- Added [Slack-compatible slash commands](http://docs.mattermost.com/developer/slash-commands.html) to integrate with external systems

iOS

- [iOS app](https://github.com/mattermost/ios) added support for GitLab single sign-on
- [iOS app](https://github.com/mattermost/ios) added support for AD/LDAP single sign-on (Enterprise Edition only)

Android

- New open source Android application compatible with Mattermost 2.0 and higher

System Console

- Added **Site Reports** to view system statistics on posts, channels and users.

### Improvements

Upgrading

- Mattermost v2.0 now upgrades from up to two previous major builds (e.g. v1.4.x and v1.3.x).

Files and Images

- Public links to images and files created by users no longer expire
- OGG attachments now play in preview window on Chrome and Firefox

Onboarding

- “Get Team Invite Link” option is disabled from the main menu if user creation is disabled for the team
- Tutorial colors improved to provide higher contrast with new default theme

Authentication

- Added ability to sign in with username as an alternative to email address
- Switching from email to SSO for sign in now updates email address to use the SSO email

System Console

- Added option to allow use of insecure TLS outbound connections to allow use of self-signed certificates
- Removed unused "Disable File Storage" option from **System Console** > **File Storage**
- Added warning if a user demotes their account from System Administrator

Search

- Hashtag search is no longer case sensitive
- System messages no longer appear in search results
- Date separator added to search results
- Moved the recent mentions icon to the right of the search bar

Messaging
- Changed the comment bubble to a reply arrow to make post replies and the right-hand sidebar more discoverable
- Time stamp next to sequential posts made by users now shows HH:MM instead of on-hover timestamp
- Code blocks now support horizontal scrolling if content exceeds the max width

User Interface

- Away status added to note users who have been idle for more than 5 minutes.
- Long usernames are now truncated in the center channel and right-hand sidebar
- Added more favicon sizes for home screen icons on mobile devices

#### Bug Fixes  

- Incorrect “Mattermost unreachable” error on iOS no longer appears
- Dialog to confirm deletion of a post now supports hitting “ENTER” to confirm deletion.
- Keyboard focus on the New Channel modal on IE11 is now contained within the text box.
- LHS indicator for “Unread Posts Above/Below” now displays on IE11
- Unresponsive UI when viewing a permalink is fixed if a user clicks outside the text on the "Click here to jump to recent messages" bar.
- Dismissed blue bar error messages no longer re-appear on page refresh.
- Console error is no longer thrown on first page load in Firefox and Edge.
- Console error and missing notification is fixed for the first direct message received from any user.
- Comment bubble in Firefox no longer appears with a box around it on-hover.
- Home screen icons on Android and iOS devices now appear with the Mattermost logo.
- Switching channels now clears the “user is typing” message below the text input box.
- iOS devices are no longer detected as “unknown” devices in the session history.

### Compatibility  
Changes from v1.4 to v2.0:

**iOS**  

Mattermost iOS app v2.0 requires Mattermost server v2.0 and higher.

**config.json**    

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json` or the System Console.  

- Under `ServiceSettings` in `config.json`:
    - `"EnableCommands": false` to set whether users can create slash commands from **Account Settings** > **Integrations** > **Commands**
    - `"EnableOnlyAdminIntegrations": true` to restrict integrations to being created by admins only.
    - `"EnableInsecureOutgoingConnections": false` sets whether outgoing HTTPS requests can accept unverified, self-signed certificates.
    - Optional: `"WebsocketSecurePort" : 443` sets the port on which the secured WebSocket will listen using the `wss` protocol. If this setting is not present in `config.json`, it defaults to `443`.
    - Optional: `"WebsocketPort": 80` sets the port on which the unsecured WebSocket will listen using the `ws` protocol. If this setting is not present in `config.json`, it defaults to `80`.

- Under `EmailSettings` in `config.json`:
    -  `"EnableSignInWithEmail": true` allows users to sign in using their email.    
    -  `"EnableSignInWithUsername": false` sets whether users can sign in with their username. Typically only used when email verification is disabled.

**Localization**  

There are two new directories for i18n localization JSON files:
- mattermost-server/i18n for server-side localization files
- mattermost-webapp/i18n for client-side localization files

#### Database Changes from v1.4 to v2.0

The following is for informational purposes only, no action needed. Mattermost automatically upgrades database tables from the previous version's schema using only additions.

##### Users Table
1. Added `Locale` column

##### Licenses Table
1. Added `Licenses` Table

##### Commands Table
1. Added `Commands` Table

#### Known Issues

- Navigating to a page with new messages containing inline images added via markdown causes the channel to scroll up and down while loading the inline images.
- Microsoft Edge does not yet support drag and drop for file attachments.
- No error message on IE11 when uploading more than 5 files or a file over 50 MB.
- File name tooltip stays open after clicking to download.
- Scroll bar does not appear in the center channel.
- Unable to paste images into the text box on Firefox, Safari, and IE11.
- Importing from Slack fails to load channels in certain cases.
- System Console > Teams > Statistics > Newly Created Users shows all users as created "just now".
- Username and email display on single line in System Console user management tab.
- Searching for a phrase in quotations returns more than just the phrase on installations with a Postgres database.
- Archived channels are not removed from the "More" menu for the person that archived the channel until after refresh.
- First load of an empty channel does not display the introduction message.
- Search results don't highlight searches for @username, non-latin characters, or terms inside Markdown code blocks.
- Searching for a username or hashtag containing a dot returns a search where the dot is replaced with the "or" operator.
- Search term highlighting doesn't update on IE11 when search terms change but return the same posts.
- Hashtags less than three characters long are not searchable.
- Hashtags containing a dash incorrectly highlight in the search results.
- Users remain in the channel counter after being deactivated.
- Permalinks for the second message or later consecutively sent in a group by the same author displaces the copy link popover or causes an error.
- Emoji smileys ending with a letter at the end of a message do not auto-complete as expected.
- Logout slash command does not force a logout.
- Incorrect formatting when a new line is added directly after a list.
- Timestamps are displayed in 12-hour format when set to 24-hour format.
- GIF links inside code blocks auto-post the GIFs.
- Syntax highlighting code block is missing the label for Latex documents.
- Deleted messages don't delete in the right-hand sidebar until a page refresh.

#### Contributors

Special thanks to [enahum](https://github.com/enahum) for creating the Spanish localization!

Many thanks to all our external contributors. In no particular order:

- [enahum](https://github.com/enahum), [trashcan](https://github.com/trashcan), [khoa-le](https://github.com/khoa-le), [alanmoo](https://github.com/alanmoo), [fallenby](https://github.com/fallenby), [loafoe](https://github.com/loafoe), [gramakri](https://github.com/gramakri), [pawelad](https://github.com/pawelad), [cifvts](https://github.com/cifvts), [rosskusler](https://github.com/rosskusler), [apskim](https://github.com/apskim)

## Release v1.4.0

Expected Release date: 2016-01-16

### Release Highlights

#### Data Center Support

- Deployment guides on Red Hat Enterprise Linux 6 and 7 now available
- Legal disclosure and support links (terms of service, privacy policy, help, about, and support email) now configurable
- Over a dozen new configuration options in System Console

#### Mobile Experience

- iOS reference app [now available from iTunes](https://itunes.apple.com/us/app/mattermost/id984966508?ls=1&mt=8), compiled from [open source repo](https://github.com/mattermost/ios)
- Date headers now show when scrolling on mobile, so you can quickly see when messages were sent
- Added "rapid scroll" support for jumping quickily to bottom of channels on mobile

### New Features

Mobile Experience
- Date headers now show when scrolling on mobile, so you can quickly see when messages were sent
- Added "rapid scroll" support for jumping quickily to bottom of channels on mobile

Authentication

- Accounts can now switch between email and GitLab SSO sign-in options
- New ability to customize session token length

System Console

- Added **Legal and Support Settings** so System Administrators can change the default Terms of Service, Privacy Policy, and Help links
- Under **Service Settings** added options to customize expiry of web, mobile and SSO session tokens, expiry of caches in memory, and an EnableDeveloper option to turn on Developer Mode which alerts users to any console errors that occur

### Improvements

Performance and Testing

- Added logging for email and push notifications events in DEBUG mode

Integrations

- Added support to allow optional parameters in the `Content-Type` of incoming webhook requests

Files and Images

- Animated GIFs autoplay in the image previewer

Notifications and Email

- Changed email notifications to display the server's local timezone instead of UTC

User Interface

- Updated the "About Mattermost" dialog formatting
- Going to domain/teamname now goes to the last channel of your previous session, instead of Town Square
- Various improvements to mobile UI, including a floating date indicator and the ability to quickly scroll to the bottom of the channel

#### Bug Fixes  

- Fixed issue where usernames containing a "." did not get mention notifications
- Fixed issue where System Console did not save the "Send push notifications" setting
- Fixed issue with Font Display cancel button not working in Account Settings menu
- Fixed incorrect default for "Team Name Display" settings
- Fixed issue where various media files appeared broken in the media player on some browsers
- Fixed cross-contamination issue when multiple accounts log into the same team on the same browser
- Fixed issue where color pickers did not update when a theme was pasted in
- Increased the maximum number of channels

### Compatibility  

#### Config.json Changes from v1.3 to v1.4

Multiple settings were added to `config.json`. Below is a list of the changes and their new default values in a fresh install.

The following options can be modified in the System Console:  

- Under `ServiceSettings` in `config.json`:
  - Added: `"EnableDeveloper": false` to set whether developer mode is enabled, which alerts users to any console errors that occur
  - Added: `"SessionLengthWebInDays" : 30` to set the number of days before web sessions expire and users will need to log in again
  - Added: `"SessionLengthMobileInDays" : 30` to set the number of days before native mobile sessions expire
  - Added: `"SessionLengthSSOInDays" : 30` to set the number of days before  SSO sessions expire
  - Added: `"SessionCacheInMinutes" : 10` to set the number of minutes to cache a session in memory
- Added `SupportSettings` section to `config.json`:
  - Added: `"TermsOfServiceLink": "/static/help/terms.html"` to allow System Administrators to set the terms of service link
  - Added: `"PrivacyPolicyLink": "/static/help/privacy.html"` to allow System Administrators to set the privacy policy link
  - Added: `"AboutLink": "/static/help/about.html"` to allow System Administrators to set the about page link
  - Added: `"HelpLink": "/static/help/help.html"` to allow System Administrators to set the help page link
  - Added: `"ReportAProblemLink": "/static/help/report_problem.html"` to allow System Administrators to set the home page for the support website
  - Added: `"SupportEmail":"feedback@mattermost.com"` to allow System Administrators to set an email address for feedback and support requests

The following options are not present in the System Console, and can be modified manually in the `config.json` file:  

- Under `FileSettings` in `config.json`:
  - Added: `"AmazonS3Endpoint": ""` to set an endpoint URL for an Amazon S3 instance
  - Added: `"AmazonS3BucketEndpoint": ""` to set an endpoint URL for Amazon S3 buckets
  - Added: `"AmazonS3LocationConstraint": false` to set whether the S3 region is location constrained
  - Added: `"AmazonS3LowercaseBucket": false` to set whether bucket names are fully lowercase or not

#### Known Issues

- When navigating to a page with new messages as well as message containing inline images added via markdown, the channel may move up and down while loading the inline images
- Microsoft Edge does not yet support drag and drop
- No scroll bar in center channel
- Pasting images into text box fails to upload on Firefox, Safari, and IE11
- Public links for attachments attempt to download the file on IE, Edge, and Safari
- Importing from Slack breaks @mentions and fails to load in certain cases with comments on files
- System Console > TEAMS > Statistics > Newly Created Users shows all of the users are created "just now"
- Favicon does not always become red when @mentions and direct messages are received on an inactive browser tab
- Searching for a phrase in quotations returns more than just the phrase on Mattermost installations with a Postgres database
- Deleted/Archived channels are not removed from the "More" menu of the person that deleted/archived the channel until after refresh
- Search results don't highlight searches for @username, non-latin characters, or terms inside Markdown code blocks
- Searching for a username or hashtag containing a dot returns a search where the dot is replaced with the "or" operator
- Hashtags less than three characters long are not searchable
- After deactivating a team member, the person remains in the channel counter
- Certain symbols (<,>,-,+,=,%,^,#,*,|) directly before or after a hashtag cause the message to not show up in a hashtag search
- Security tab > Active Sessions reports iOS devices as "unknown"
- Getting a permalink for the second message or later consecutively sent in a group by the same author displaces the copy link popover or causes an error

#### Contributors

Many thanks to our external contributors. In no particular order:

- [npcode](https://github.com/npcode), [hjf288](https://github.com/hjf288), [apskim](https://github.com/apskim), [ejm2172](https://github.com/ejm2172), [hvnsweeting](https://github.com/hvnsweeting), [benburkert](https://github.com/benburkert), [erikthered](https://github.com/erikthered)

## Release v1.3.0

Release date: 2015-12-16

### Release Highlights

#### iOS App

- New [Mattermost iOS App](https://github.com/mattermost/ios) now available for iPhone, iPad, and iPod Touch
- New [Mattermost Push Notification Service](https://github.com/mattermost/push-proxy) to relay notifications to custom iOS applications

#### Search Upgrades

- Jump to search results in archives using new message permalinks
- It's easier to find what you're looking for with improved auto-complete in search

#### Advanced Formatting

- Express more in symbols, with new emoji auto-complete
- Express more in numbers, with rendering of mathematical expressions using Latex (start code blocks with ```latex)
- Personalize your look with new custom font settings under **Account Settings** > **Display** > **Display Font**

### New Features

Authentication
- Added unofficial SSO support for GitHub.com and GitHub Enterprise using GitLab UI

Archives
- Added permalink feature that lets users link to a post in the message archives
- Added ability to "Jump" to archives from a search result

Account Settings
- Added "Preview pre-release features" setting, to allow user to preview early features ahead of their official release
- Added "Display font" setting, so users can select which font to use

Messaging & Comments
- Added in-line previews for links from select websites and for URLs pointing to an image (enabled via Account Settings -> Advanced -> Preview pre-release features)
- Added emoji autocomplete

Extras
- Added `/loadtest url` tool for manually [testing text processing](https://github.com/mattermost//mattermost-server/tree/master/tests)

### Improvements

Performance
- Updated getProfiles service to return less data
- Refactored several modals to use React-Boostrap
- Refactored the center channel

Messaging & Comments
- Added Markdown support for task lists
- Added "Help" link for messaging
- Added ability to preview a Markdown message before sending (enabled via Account Settings -> Advanced -> Preview pre-release features)

Onboarding
- Minor upgrades to tutorial

User Interface
- Visually combined sequential messages from the same user
- Added ability to rename "Town Square"
- Teammate name display option now applies to messages and comments
- Menus and search improved on mobile UI
- Switched to Emoji One style emojis

#### Bug Fixes  

- Removed the @all mention to keep users from accidentally spamming team sites
- Fixed bug where the member list only showed "20" members for channels with more than 20 members
- Fixed bug where the channel sidebar didn't order correctly on Postgres databases
- Fixed bug where search results did not highlight when searching with quotation marks, wildcard, or in: and from: modifiers
- Fixed bug with the cancel button not properly resetting the text in some account settings fields
- Fixed bug where editing a post to be empty caused a 404 error
- Fixed bug where logging out did not work properly on IE11
- Fixed issue where refreshing the page with the right hand sidebar open caused "..." to show up in place of usernames
- Fixed issue where invite to channel modal did not update properly when switching between channels

### Compatibility  

#### Config.json Changes from v1.2 to v1.3

Multiple settings were added to `config.json`. These options can be modified in the System Console, or manually updated in the existing config.json file. This is a list of changes and their new default values in a fresh install:
- Under `EmailSettings` in `config.json`:
  - Removed: `"ApplePushServer": ""` which is replaced with `SendPushNotifications` and `PushNotificationServer`
  - Removed: `"ApplePushCertPublic": ""`  which is replaced with `SendPushNotifications` and `PushNotificationServer`
  - Removed: `"ApplePushCertPrivate": ""` which is replaced with `SendPushNotifications` and `PushNotificationServer`
  - Added: `"SendPushNotifications": false` to control whether mobile push notifications are sent to the server specified in `PushNotificationServer`
  - Added: `"PushNotificationServer": ""` to specify the address of the proxy server that re-sends push notifications to their respective services like APNS (Apple Push Notification Services)

#### Known Issues

- System Console does not save Email Settings when "Save" is clicked
- When navigating to a page with new messages as well as message containing inline images added via markdown, the channel may move up and down while loading the inline images
- Microsoft Edge does not yet support drag and drop
- Media files of type .avi .mkv .wmv .mov .flv .mp4a do not play  properly
- No scroll bar in center channel
- Pasting images into text box fails to upload on Firefox, Safari, and IE11
- Slack import @mentions break
- Usernames containing a "." do not get mention notifications

#### Contributors

Many thanks to our external contributors. In no particular order:

- [florianorben](https://github.com/florianorben), [npcode](https://github.com/npcode), [42wim](https://github.com/42wim), [cifvts](https://github.com/cifvts), [rompic](https://github.com/rompic), [jdhoek](https://github.com/jdhoek), [Tsynapse](https://github.com/Tsynapse), [alexgaribay](https://github.com/alexgaribay), [vladikoff](https://github.com/vladikoff), [jonathanwiesel](https://github.com/jonathanwiesel), [tamtamchik](https://github.com/tamtamchik)

## Release v1.2.1

- **Released:** 2015-11-16

### Security Notice

Mattermost v1.2.1 is a bug fix release addressing a security issue in v1.2.0 affecting a newly introduced outgoing webhooks feature. Specifically, in v1.2.0 there was a check missing from outgoing webhooks, so a team member creating outgoing webhooks could in theory find a way to listen to messages in private channels containing popular words like "a", "the", "at", etc. For added security, Mattermost v1.2.1 now installs with incoming and outgoing webhooks disabled by default.

To limit the impact of this security issue, Mattermost v1.2.0 has been removed from the source repo. It is recommended that anyone who's installed v1.2.0 upgrade to v1.2.1 via [the procedure described in the Mattermost Upgrade Guide](http://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-for-2-2-x-and-earlier).

### Release Highlights

#### Outgoing webhooks

- Mattermost users can now interact with external applications using [outgoing webhooks](http://docs.mattermost.com/developer/webhooks-outgoing.html)
- An [application template](https://github.com/mattermost/mattermost-integration-giphy) demonstrating user queries sent to the Giphy search engine via Mattermost webhooks now available
- A community application, [Matterbridge](https://github.com/42wim/matterbridge?files=1), shows how to use webhooks to connect Mattermost with IRC

#### Search Scope Modifiers

- Adding search term `in:[channel_url_name]` now limits searches within a specific channel
- Adding search term `from:[username]` now limits searches to messages from a specific user

#### Syntax Highlighting

- Syntax highlight for code blocks now available for `Diff, Apache, Makefile, HTTP, JSON, Markdown, JavaScript, CSS, nginx, ObjectiveC, Python, XML, Perl, Bash, PHP, CoffeeScript, C, SQL, Go, Ruby, Java, and ini`

#### Usability Improvements

- Added tutorial to teach new users how to use Mattermost
- Various performance improvements to support teams with hundreds of users
- Direct Messages "More" menu now lets you search for users by username and real name

### Improvements

Onboarding

- New tutorial explaining how to use Mattermost for new users

Messaging and Notifications

- Users can now search for teammates to add to **Direct Message** list via **More** menu
- Users can now personalize Direct Messages list by removing users listed
- Link previews - Adding URL with .gif file adds image below message
- Added new browser tab alerts to indicate unread messages and mentions

Search

- Adding search term `in:[channel_url_name]` now limits searches within a specific channel
- Adding search term `from:[username]` now limits searches to messages from a specific user
- Tip explaining search options when clicking into search box

Integrations

- [Outgoing webhooks](http://docs.mattermost.com/developer/webhooks-outgoing.html) now available
- Made available [application template showing outgoing webhooks working with Mattermost and external application](https://github.com/mattermost/mattermost-integration-giphy)

User Interface

- Member list in Channel display now scrollable, and includes Message button to message channel members directly
- Added ability to edit previous message by hitting UP arrow
- Syntax highlighting added for code blocks
   - Languages include `Diff, Apache, Makefile, HTTP, JSON, Markdown, Java, CSS, nginx, ObjectiveC, Python, XML, Perl, Bash, PHP, CoffeeScript, C, SQL, Go, Ruby, Java, and ini`.
   - Use by adding the name of the language on the first link of the code block, for example: ```python
   - Syntax color theme can be defined under **Account Settings** > **Appearance Settings** > **Custom Theme**
- Updated Drag & Drop UI
- Added 24 hour time display option

Team Settings

- Added Team Settings option to include account creation URL on team login page
- Added Team Settings option to include link to given team on root page
- Ability to rotate invite code for invite URL

Extras

- Added `/shrug KEYWORD` command to output: `¯\_(ツ)_/¯ KEYWORD`
- Added `/me KEYWORD` command to output: _`KEYWORD`_
- Added setting option to send a message on control-enter instead of enter

System Console

- New statistics page
- Configurable option to create an account directly from team page

#### Bug Fixes  

- Various fixes to theme colors
- Fixed issue with the centre channel scroll position jumping when right hand side was opened and closed
- Added support for simultaneous login to different teams in different browser tabs
- Incoming webhooks no longer disrupted when channel is deleted
- You can now paste a Mattermost incoming webhook URL into the same field designed for a Slack URL and integrations will work

### Compatibility  

- IE 11 new minimum version for IE, since IE 10 share fell below 5% on desktop
- Safari 9 new minimum version for Safari, since Safari 7 and 8 fell below 1% each on desktop

#### Config.json Changes from v1.1 to v1.2

Multiple settings were added to `config.json`. These options can be modified in the System Console, or manually updated in the existing config.json file. This is a list of changes and their new default values in a fresh install:
- Under `TeamSettings` in `config.json`:
  - Added: `"RestrictTeamNames": true` to control whether team names can contain reserved words like www, admin, support, test, etc.
  - Added: `"EnableTeamListing": false` to control whether teams can be listed on the root page of the site
- Under `ServiceSettings` in `config.json`
  - Added: `"EnableOutgoingWebhooks": false` to control whether outgoing webhooks are enabled
  - Changed: `"EnableIncomingWebhooks": true` to `"EnableIncomingWebhooks": false` to turn incoming webhooks off by default, to increase security of default install. Documentation updated to enable webhooks before use.

#### Database Changes from v1.1 to v1.2

The following is for informational purposes only, no action needed. Mattermost automatically upgrades database tables from the previous version's schema using only additions. Sessions table is dropped and rebuilt, no team data is affected by this.

##### Channels Table
1. Renamed `Description` to `Header`
2. Added `Purpose` column with type `varchar(1024)`

##### Preferences Table
1. Added `Preferences` Table

##### Teams Table
1. Added `InviteId` column with type `varchar(32)`
2. Added `AllowOpenInvite` column with type `tinyint(1)`
3. Added `AllowTeamListing` column with type `tinyint(1)`
4. Added `idx_teams_invite_id` index

#### Known Issues

- When navigating to a page with new messages as well as message containing inline images added via markdown, the channel may move up and down while loading the inline images
- Microsoft Edge does not yet support drag and drop
- After upgrading to v1.2 existing users will see the newly added tutorial tips upon login (this is a special case for v1.2 and will not happen in future upgrades)
- Channel list becomes reordered when there are lowercase channel names in a Postgres database
- Member list only shows "20" members for channels with more than 20 members
- Searches containing punctuation are not highlighted in the results (including in: or from: search modifiers and searches with quotations)
- Media files of type .avi .mkv .wmv .mov .flv .mp4a do not play  properly
- Editing a post so that it's text is blank (which should delete it) throws a 404
- No scroll bar in centre channel
- Theme color import from Slack fails to import the “Active Channel” selection color
- Pasting images into text box fails to upload on Firefox and Safari
- Users cannot claim accounts imported from Slack via password reset
- Slack import @mentions break

#### Contributors

Many thanks to our external contributors. In no particular order:

- [florianorben](https://github.com/florianorben), [trashcan](https://github.com/trashcan), [girishso](https://github.com/girishso), [apaatsio](https://github.com/apaatsio), [jlebleu](https://github.com/jlebleu), [stasvovk](https://github.com/stasvovk), [mcmillhj](https://github.com/mcmillhj), [sharms](https://github.com/sharms), [jvasallo](https://github.com/jvasallo), [layzerar](https://github.com/layzerar), [optimistiks](https://github.com/optimistiks), [Tsynapse](https://github.com/Tsynapse), [vinnymac](https://github.com/vinnymac), [yuvipanda](https://github.com/yuvipanda), [toyorg](https://github.com/toyorg)

## Release v1.2.0 (Redacted Release)

- **Final release:** 2015-11-16 (**Note:** This release was removed from public availability and replaced by v1.2.1 owing to a security issue with the new outgoing webhooks feature. See v1.2.1 Release Notes for details).

## Release v1.1.1 (Bug Fix Release)

Released 2015-10-20

### About Bug Fix Releases

This is a bug fix release (v1.1.1) and recommended only for users needing a fix to the specific issue listed below. All other users should use the most recent major stable build release (v1.1.0).

[View more information on Mattermost release numbering](http://docs.mattermost.com/process/release-process.html#release-numbering).

### Release Purpose

#### Provide option for upgrading database from Mattermost v0.7 to v1.1

Upgrading Mattermost v0.7 to Mattermost v1.1 originally required installing Mattermost v1.0 to upgrade from the Mattermost v0.7 database, followed by an install of Mattermost v1.1.

This was problematic for installing Mattermost with GitLab omnibus since GitLab 8.0 contained Mattermost v0.7 and GitLab 8.1 was to include Mattermost v1.1

Therefore Mattermost v1.1.1 was created that can upgrade the database in Mattermost v0.7 to Mattermost v1.1 directly.

Users who configured Mattermost v0.7 within GitLab via the `config.json` file should consult [documentation on upgrading configurations from Mattermost v0.7 to Mattermost v1.1](http://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-for-2-2-x-and-earlier).

#### Removes 32-char limit on salts

Mattermost v1.1 introduced a 32-char limit on salts that broke the salt generating in GitLab and this restriction was removed for 1.1.1.

## Release v1.1.0

Released: 2015-10-16

### Release Highlights

#### Incoming Webhooks

Mattermost now supports incoming webhooks for channels and private groups. This developer feature is available from the Account Settings -> Integrations menu. Documentation on how developers can use the webhook functionality to build custom integrations, along with samples, is available at http://mattermost.org/webhooks.

### Improvements

Integrations

- Improved support for incoming webhooks, including the ability to override a username and post as a bot instead

Documentation

- Added documentation on config.json and System Console settings
- Docker Toolbox replaces deprecated Boot2Docker instructions in container install documentation

Theme Colors

- Improved appearance of dark themes

System Console

- Client side errors now written to server logs
- Added "EnableSecurityFixAlert" option to receive alerts on relevant security fix alerts
- Various improvements to System Console UI and help text

Messaging and Notifications

- Replaced "Quiet Mode" in the Channel Notification Settings with an option to only show unread indicator when mentioned

### Bug Fixes

- Fixed regression causing "Get Public Link" on images not to work
- Fixed bug where certain characters caused search errors
- Fixed bug where System Administrator did not have Team Administrator permissions
- Fixed bug causing scrolling to jump when the right hand sidebar opened and closed

### Known Issues

- Slack import is unstable due to change in Slack export format
- Uploading a .flac file breaks the file previewer on iOS

### Compatibility

#### Config.json Changes from v1.0 to v1.1

##### Service Settings

Multiple settings were added to `config.json` and System Console UI. Prior to upgrading the Mattermost binaries from the previous versions, these options would need to be manually updated in existing config.json file. This is a list of changes and their new default values in a fresh install:
- Under `ServiceSettings` in `config.json`:
  - Added: `"EnablePostIconOverride": false` to control whether webhooks can override profile pictures
  - Added: `"EnablePostUsernameOverride": false` to control whether webhooks can override profile pictures
  - Added: `"EnableSecurityFixAlert": true` to control whether the system is alerted to security updates

#### Database Changes from v1.0 to v1.1

The following is for informational purposes only, no action needed. Mattermost automatically upgrades database tables from the previous version's schema using only additions. Sessions table is dropped and rebuilt, no team data is affected by this.

##### ChannelMembers Table
1. Removed `NotifyLevel` column
2. Added `NotifyProps` column with type `varchar(2000)` and default value `{}`

### Contributors

Many thanks to our external contributors. In no particular order:

- [chengweiv5](https://github.com/chengweiv5), [pstonier](https://github.com/pstonier), [teviot](https://github.com/teviot), [tmuwandi](https://github.com/tmuwandi), [driou](https://github.com/driou), [justyns](https://github.com/justyns), [drbaker](https://github.com/drbaker), [thomas9987](https://github.com/thomas9987), [chuck5](https://github.com/chuck5), [sjmog](https://github.com/sjmog), [chengkun](https://github.com/chengkun), [sexybern](https://github.com/sexybern), [tomitm](https://github.com/tomitm), [stephenfin](https://github.com/stephenfin)

## Release v1.0.0

Released 2015-10-02

### Release Highlights

#### Markdown

Markdown support is now available across messages, comments and channel descriptions for:

- **Headings** - in five different sizes to help organize your thoughts
- **Lists** - both numbered and bullets
- **Font formatting** - including **bold**, _italics_, ~~strikethrough~~, `code`, links, and block quotes)
- **In-line images** - useful for creating buttons and status messages
- **Tables** - for keeping things organized
- **Emoticons** - translation of emoji codes to images like :sheep: :boom: :rage1: :+1:

See [documentation](https://docs.mattermost.com/help/messaging/formatting-text.html) for full details.

#### Themes

Themes as been significantly upgraded in this release with:

- 4 pre-set themes, two light and two dark, to customize your experience
- 18 detailed color setting options to precisely match the colors of your other tools or preferences
- Ability to import themes from Slack

#### System console and command line tools

Added new web-based System Console for managing instance level configuration. This lets IT admins conveniently:

- _access core settings_, like server, database, email, rate limiting, file store, SSO, and log settings,
- _monitor operations_, by quickly accessing log files and user roles, and
- _manage teams_, with essential functions such as team role assignment and password reset

In addition new command line tools are available for managing Mattermost system roles, creating users, resetting passwords, getting version info and other basic tasks.

Run `./platform -h` for documentation using the new command line tool.


### New Features

Messaging, Comments and Notifications

- Full markdown support in messages, comments, and channel description
- Support for emoji codes rendering to image files

Files and Images

- Added ability to play video and audio files

System Console

- UI to change config.json settings
- Ability to view log files from console
- Ability to reset user passwords
- Ability for IT admin to manage members across multiple teams from single interface

User Interface

- Ability to set custom theme colors
- Replaced single color themes with pre-set themes
- Added ability to import themes from Slack

Integrations

- (Preview) Initial support for incoming webhooks

### Improvements

Documentation

- Added production installation instructions
- Updated software and hardware requirements documentation
- Re-organized install instructions out of README and into separate files
- Added Code Contribution Guidelines
- Added new hardware sizing recommendations
- Consolidated licensing information into LICENSE.txt and NOTICE.txt
- Added markdown documentation

Performance

- Enabled Javascript optimizations
- Numerous improvements in center channel and mobile web

Code Quality

- Reformatted Javascript per Mattermost Style Guide

User Interface

- Added version, build number, build date and build hash under Account Settings -> Security

Licensing

- Compiled version of Mattermost v1.0.0 now available under MIT license

### Bug Fixes

- Fixed issue so that SSO option automatically set `EmailVerified=true` (it was false previously)

### Compatibility

A large number of settings were changed in `config.json` and a System Console UI was added. This is a very large change due to Mattermost releasing as v1.0 and it's unlikely a change of this size would happen again.

Prior to upgrading the Mattermost binaries from the previous versions, the below options would need to be manually updated in your existing config.json file to migrate successfully. This is a list of changes and their new default values in a fresh install:
#### Config.json Changes from v0.7 to v1.0

##### Service Settings

- Under `ServiceSettings` in `config.json`:
  - Moved: `"SiteName": "Mattermost"` which was added to `TeamSettings`
  - Removed: `"Mode" : "dev"` which deprecates a high level dev mode, now replaced by granular controls
  - Renamed: `"AllowTesting" : false` to `"EnableTesting": false` which allows the use of `/loadtest` slash commands during development
  - Removed: `"UseSSL": false` boolean replaced by `"ConnectionSecurity": ""` under `Security` with new options: _None_ (`""`), _TLS_ (`"TLS"`) and _StartTLS_ ('"StartTLS"`)
  - Renamed: `"Port": "8065"` to `"ListenAddress": ":8065"` to define address on which to listen. Must be prepended with a colon.
  - Removed: `"Version": "developer"` removed and version information now stored in `model/version.go`
  - Removed: `"Shards": {}` which was not used
  - Moved: `"InviteSalt": "gxHVDcKUyP2y1eiyW8S8na1UYQAfq6J6"` to `EmailSettings`
  - Moved: `"PublicLinkSalt": "TO3pTyXIZzwHiwyZgGql7lM7DG3zeId4"` to `FileSettings`
  - Renamed and Moved `"ResetSalt": "IPxFzSfnDFsNsRafZxz8NaYqFKhf9y2t"` to `"PasswordResetSalt": "vZ4DcKyVVRlKHHJpexcuXzojkE5PZ5eL"` and moved to `EmailSettings`
  - Removed: `"AnalyticsUrl": ""` which was not used
  - Removed: `"UseLocalStorage": true` which is replaced by `"DriverName": "local"` in `FileSettings`
  - Renamed and Moved: `"StorageDirectory": "./data/"` to `Directory` and moved to `FileSettings`
  - Renamed: `"AllowedLoginAttempts": 10` to `"MaximumLoginAttempts": 10`
  - Renamed, Reversed and Moved: `"DisableEmailSignUp": false` renamed `"EnableSignUpWithEmail": true`, reversed meaning of `true`, and moved to `EmailSettings`
  - Added: `"EnableOAuthServiceProvider": false` to enable OAuth2 service provider functionality
  - Added: `"EnableIncomingWebhooks": false` to enable incoming webhooks feature

##### Team Settings

- Under `TeamSettings` in `config.json`:
  - Renamed: `"AllowPublicLink": true` renamed to `"EnablePublicLink": true` and moved to `FileSettings`
  - Removed: `AllowValetDefault` which was a guest account feature that is deprecated
  - Removed: `"TermsLink": "/static/help/configure_links.html"` removed since option didn't need configuration
  - Removed: `"PrivacyLink": "/static/help/configure_links.html"` removed since option didn't need configuration
  - Removed: `"AboutLink": "/static/help/configure_links.html"` removed since option didn't need configuration
  - Removed: `"HelpLink": "/static/help/configure_links.html"` removed since option didn't need configuration
  - Removed: `"ReportProblemLink": "/static/help/configure_links.html"` removed since option didn't need configuration
  - Removed: `"TourLink": "/static/help/configure_links.html"` removed since option didn't need configuration
  - Removed: `"DefaultThemeColor": "#2389D7"` removed since theme colors changed from 1 to 18, default theme color option may be added back later after theme color design stablizes
  - Renamed: `"DisableTeamCreation": false` to `"EnableUserCreation": true` and reversed
  - Added: ` "EnableUserCreation": true` added to disable ability to create new user accounts in the system

##### SSO Settings

- Under `SSOSettings` in `config.json`:
  - Renamed Category: `SSOSettings` to `GitLabSettings`
  - Renamed: `"Allow": false` to `"Enable": false` to enable GitLab SSO

##### AWS Settings

- Under `AWSSettings` in `config.json`:
  - This section was removed and settings moved to `FileSettings`
  - Renamed and Moved: `"S3AccessKeyId": ""` renamed `"AmazonS3AccessKeyId": "",` and moved to `FileSettings`
  - Renamed and Moved: `"S3SecretAccessKey": ""` renamed `"AmazonS3SecretAccessKey": "",` and moved to `FileSettings`
  - Renamed and Moved: `"S3Bucket": ""` renamed `"AmazonS3Bucket": "",` and moved to `FileSettings`
  - Renamed and Moved: `"S3Region": ""` renamed `"AmazonS3Region": "",` and moved to `FileSettings`

##### Image Settings

- Under `ImageSettings` in `config.json`:
  - Renamed: `"ImageSettings"` section to `"FileSettings"`
  - Added: `"DriverName" : "local"` to specify the file storage method, `amazons3` can also be used to setup S3

##### EmailSettings

- Under `EmailSettings` in `config.json`:
  - Removed: `"ByPassEmail": "true"` which is replaced with `SendEmailNotifications` and `RequireEmailVerification`
  - Added: `"SendEmailNotifications" : "false"` to control whether email notifications are sent
  - Added: `"RequireEmailVerification" : "false"` to control if users need to verify their emails
  - Replaced: `"UseTLS": "false"` with `"ConnectionSecurity": ""` with options: _None_ (`""`), _TLS_ (`"TLS"`) and _StartTLS_ (`"StartTLS"`)
  - Replaced: `"UseStartTLS": "false"` with `"ConnectionSecurity": ""` with options: _None_ (`""`), _TLS_ (`"TLS"`) and _StartTLS_ (`"StartTLS"`)

##### Privacy Settings

- Under `PrivacySettings` in `config.json`:
  - Removed: `"ShowPhoneNumber": "true"` which was not used
  - Removed: `"ShowSkypeId" : "true"` which was not used

### Database Changes from v0.7 to v1.0

The following is for informational purposes only, no action needed. Mattermost automatically upgrades database tables from the previous version's schema using only additions. Sessions table is dropped and rebuilt, no team data is affected by this.

##### Users Table
1. Added `ThemeProps` column with type `varchar(2000)` and default value `{}`

##### Teams Table
1. Removed `AllowValet` column

##### Sessions Table
1. Renamed `Id` column `Token`
2. Renamed `AltId` column `Id`
3. Added `IsOAuth` column with type `tinyint(1)` and default value `0`

##### OAuthAccessData Table
1. Added new table `OAuthAccessData`
2. Added `AuthCode` column with type `varchar(128)`
3. Added `Token` column with type `varchar(26)` as the primary key
4. Added `RefreshToken` column with type `varchar(26)`
5. Added `RedirectUri` column with type `varchar(256)`
6. Added index on `AuthCode` column

##### OAuthApps Table
1. Added new table `OAuthApps`
2. Added `Id` column with type `varchar(26)` as primary key
2. Added `CreatorId` column with type `varchar(26)`
2. Added `CreateAt` column with type `bigint(20)`
2. Added `UpdateAt` column with type `bigint(20)`
2. Added `ClientSecret` column with type `varchar(128)`
2. Added `Name` column with type `varchar(64)`
2. Added `Description` column with type `varchar(512)`
2. Added `CallbackUrls` column with type `varchar(1024)`
2. Added `Homepage` column with type `varchar(256)`
3. Added index on `CreatorId` column

##### OAuthAuthData Table
1. Added new table `OAuthAuthData`
2. Added `ClientId` column with type `varchar(26)`
2. Added `UserId` column with type `varchar(26)`
2. Added `Code` column with type `varchar(128)` as primary key
2. Added `ExpiresIn` column with type `int(11)`
2. Added `CreateAt` column with type `bigint(20)`
2. Added `State` column with type `varchar(128)`
2. Added `Scope` column with type `varchar(128)`

##### IncomingWebhooks Table
1. Added new table `IncomingWebhooks`
2. Added `Id` column with type `varchar(26)` as primary key
2. Added `CreateAt` column with type `bigint(20)`
2. Added `UpdateAt` column with type `bigint(20)`
2. Added `DeleteAt` column with type `bigint(20)`
2. Added `UserId` column with type `varchar(26)`
2. Added `ChannelId` column with type `varchar(26)`
2. Added `TeamId` column with type `varchar(26)`
3. Added index on `UserId` column
3. Added index on `TeamId` column

##### Systems Table
1. Added new table `Systems`
2. Added `Name` column with type `varchar(64)` as primary key
3. Added `Value column with type `varchar(1024)`

### Contributors

Many thanks to our external contributors. In no particular order:

- [jdeng](https://github.com/jdeng), [Trozz](https://github.com/Trozz), [LAndres](https://github.com/LAndreas), [JessBot](https://github.com/JessBot), [apaatsio](https://github.com/apaatsio), [chengweiv5](https://github.com/chengweiv5)

## Release v0.7.0 (Beta1)

Released 2015-09-05

### Release Highlights

#### Improved GitLab Mattermost support

Following the release of Mattermost v0.6.0 Alpha, GitLab 7.14 offered an automated install of Mattermost with GitLab Single Sign-On (co-branded as "GitLab Mattermost") in its omnibus installer.

New features, improvements, and bug fixes recommended by the GitLab community were incorporated into Mattermost v0.7.0 Beta1--in particular, extending support of GitLab SSO to team creation, and restricting team creation to users with verified emails from a configurable list of domains.

#### Slack Import (Preview)

Preview of Slack import functionality supports the processing of an "Export" file from Slack containing account information and public channel archives from a Slack team.   

- In the feature preview, emails and usernames from Slack are used to create new Mattermost accounts, which users can activate by going to the Password Reset screen in Mattermost to set new credentials.
- Once logged in, users will have access to previous Slack messages shared in public channels, now imported to Mattermost.  

Limitations:

- Slack does not export files or images your team has stored in Slack's database. Mattermost will provide links to the location of your assets in Slack's web UI.
- Slack does not export any content from private groups or direct messages that your team has stored in Slack's database.
- The Preview release of Slack Import does not offer pre-checks or roll-back and will not import Slack accounts with username or email address collisions with existing Mattermost accounts. Also, Slack channel names with underscores will not import. Also, mentions do not yet resolve as Mattermost usernames (still show Slack ID). These issues are being addressed in [Mattermost v0.8.0 Migration Support](https://mattermost.atlassian.net/browse/PLT-22?filter=10002).

### New Features

GitLab Mattermost

- Ability to create teams using GitLab SSO (previously GitLab SSO only supported account creation and sign-in)
- Ability to restrict team creation to GitLab SSO and/or users with email verified from a specific list of domains.

File and Image Sharing

- New drag-and-drop file sharing to messages and comments
- Ability to paste images from clipboard to messages and comments

Messaging, Comments and Notifications

- Send messages faster with from optimistic posting and retry on failure

Documentation

- New style guidelines for Go, React and Javascript

### Improvements

Messaging, Comments and Notifications

- Performance improvements to channel rendering
- Added "Unread posts" in left hand sidebar when notification indicator is off-screen

Documentation

- Install documentation improved based on early adopter feedback

### Bug Fixes

- Fixed multiple issues with GitLab SSO, installation and on-boarding
- Fixed multiple IE 10 issues
- Fixed broken link in verify email function
- Fixed public links not working on mobile

### Contributors

Many thanks to our external contributors. In no particular order:

- [asubset](https://github.com/asubset), [felixbuenemann](https://github.com/felixbuenemann), [CtrlZvi](https://github.com/CtrlZvi), [BastienDurel](https://github.com/BastienDurel), [manusajith](https://github.com/manusajith), [doosp](https://github.com/doosp), [zackify](https://github.com/zackify), [willstacey](https://github.com/willstacey)

Special thanks to the GitLab Mattermost early adopter community who influenced this release, and who play a pivotal role in bringing Mattermost to over 100,000 organizations using GitLab today. In no particular order:

- [cifvts](http://forum.mattermost.org/users/cifvts/activity), [Chryb](https://gitlab.com/u/Chryb), [cookacounty](https://gitlab.com/u/cookacounty), [bweston92](https://gitlab.com/u/bweston92), [mablae](https://gitlab.com/u/mablae), [picharmer](https://gitlab.com/u/picharmer), [cmtonkinson](https://gitlab.com/u/cmtonkinson), [cmthomps](https://gitlab.com/u/cmthomps), [m.gamperl](https://gitlab.com/u/m.gamperl), [StanMarsh](https://gitlab.com/u/StanMarsh), [jeanmarc-leroux](https://gitlab.com/u/jeanmarc-leroux), [dnoe](https://gitlab.com/u/dnoe), [dblessing](https://gitlab.com/u/dblessing), [mechanicjay](https://gitlab.com/u/mechanicjay), [larsemil](https://gitlab.com/u/larsemil), [vga](https://gitlab.com/u/vga), [stanhu](https://gitlab.com/u/stanhu), [kohenkatz](https://gitlab.com/u/kohenkatz), [RavenB1](https://gitlab.com/u/RavenB1), [booksprint](http://forum.mattermost.org/users/booksprint/activity), [scottcorscadden](http://forum.mattermost.org/users/scottcorscadden/activity), [sskmani](http://forum.mattermost.org/users/sskmani/activity), [gosure](http://forum.mattermost.org/users/gosure/activity), [jigarshah](http://forum.mattermost.org/users/jigarshah/activity)

Extra special thanks to GitLab community leaders for successful release of GitLab Mattermost Alpha:

- [marin](https://gitlab.com/u/marin), [sytse](https://gitlab.com/u/sytse)


## Release v0.6.0 (Alpha)

Released 2015-08-07

### Release Highlights

- Simplified on-prem install
- Support for GitLab Mattermost (GitLab SSO, Postgres support, IE 10+ support)

### Compatibility

*Note: While use of Mattermost Preview (v0.5.0) and Mattermost Alpha (v0.6.0) in production is not recommended, we document compatibility considerations for a small number of organizations running Mattermost in production, supported directly by Mattermost product team.*

- Switched Team URLs from team.domain.com to domain.com/team

### New Features

GitLab Mattermost

- OAuth2 support for GitLab Single Sign-On
- PostgreSQL support for GitLab Mattermost users
- Support for Internet Explorer 10+ for GitLab Mattermost users

File and Image Sharing

- New thumbnails and formatting for files and images

Messaging, Comments and Notifications

- Users now see posts they sent highlighted in a different color
- Mentions can now also trigger on user-defined words

Security and Administration

- Enable users to view and log out of active sessions
- Team Admin can now delete posts from any user

On-boarding

- “Off-Topic” now available as default channel, in addition to “Town Square”

### Improvements

Installation

- New "ByPassEmail" setting enables Mattermost to operate without having to set up email
- New option to use local storage instead of S3
- Removed use of Redis to simplify on-premise installation

On-boarding

- Team setup wizard updated with usability improvements

Documentation

- Install documentation improved based on early adopter feedback

### Contributors

Many thanks to our external contributors. In no particular order:

- [ralder](https://github.com/ralder), [jedisct1](https://github.com/jedisct1), [faebser](https://github.com/faebser), [firstrow](https://github.com/firstrow), [haikoschol](https://github.com/haikoschol), [adamenger](https://github.com/adamenger)

## Release v0.5.0 (Preview)

Released 2015-06-24

### Release Highlights

- First release of Mattermost as a team communication service for sharing messagse and files across PCs and phones, with archiving and instant search.

### New Features

Messaging and File Sharing

- Send messages, comments, files and images across public, private and 1-1 channels
- Personalize notifications for unreads and mentions by channel
- Use #hashtags to tag and find messages, discussions and files

Archiving and Search

- Search public and private channels for historical messages and comments
- View recent mentions of your name, username, nickname, and custom search terms

Anywhere Access

- Use Mattermost from web-enabled PCs and phones
- Define team-specific branding and color themes across your devices
