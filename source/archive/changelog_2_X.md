# Mattermost Changelog Archive v2.0.0 - v.2.2.0

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