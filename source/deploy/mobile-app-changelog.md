# Mattermost mobile apps changelog

Latest Mattermost Mobile Apps releases:

- [2.7.0 Release](#release)
- [2.6.0 Release](#id1)
- [2.5.1 Release](#id6)
- [2.5.0 Release](#id9)
- [2.4.0 Release](#id14)
- [2.3.0 Release](#id19)

## 2.7.0 Release
- Release Date: August 16, 2023
- Server Versions Supported: Server v7.8.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v7.8.0 or later is required.** Support for server [Extended Support Release](https://docs.mattermost.com/upgrade/extended-support-release.html) (ESR) v7.1.0 has ended and upgrading to server ESR v7.8.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Improvements
 - Guest tags are now removed based on server configuration under **System Console > Authentication > Guest Access > Show Guest Tag**.
 - Improved behavior of multi-request environments (such as HTTP/1.1).
 - Added search result highlight that matches the words being searched.
 - Added a new feature for remembering the last viewed channel or thread that takes returning users to the last channel or thread they visited.
 - Improved the appearance of the search results.
 - User’s current status is now shown at the bottom tab bar profile image.
 - Added a **Copy info** button to the **About** page.

### Bug Fixes
 - Fixed issues with timeouts when uploading files.
 - Fixed hashtag search to match the hashtag and not the word.
 - Fixed search results to match the webapp.
 - Fixed an issue with selecting the custom theme from the display setting.
 - Fixed an issue where the keyboard overlapped with recent search items in the search tab.
 - Fixed an issue with notifications showing a session expired message when it shouldn't.

### Known Issues
 - Users are unable to adjust the font size via the OS font size setting.
 - Some Google Pixel phones on Android 12+ might not continue past the login screen. This is a known issue with the OS, and the current workaround is to restart the device.

## 2.6.0 Release
- Release Date: July 14, 2023
- Server Versions Supported: Server v7.8.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v7.8.0 or later is required.** Support for server [Extended Support Release](https://docs.mattermost.com/upgrade/extended-support-release.html) (ESR) v7.1.0 has ended and upgrading to server ESR v7.8.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Improvements
 - Calls: ``/call start`` will now start calls within an existing thread.
 - Improved logging for mobile apps.
 - Added localization support to iOS share extension.
 - Improved the user interface of the **Edit Post** screen.

### Bug Fixes
 - Fixed a rare issue when changing the role of the current user in a channel.
 - Calls: Fixed an issue for blank screen after ending a call and exiting its thread.
 - Fixed an issue where the Global Threads screens didn't show a badge if the user had mentions in other channels / servers.
 - Removed unneeded fetch posts for unread archived channels that were appearing in the logs.
 - Removed unneeded group calls that were appearing in the logs.
 - Fixed an issue with the progress indicator when uploading files on Android.
 - Fixed a few issues with app initialization.
 - Fixed an issue where notifications would show "Session expired" instead of the message.
 - Fixed a crash when users that reacted with a certain emoji were listed and a user was missing.

### Known Issues
 - Users are unable to adjust the font size via the OS font size setting.
 - Some Google Pixel phones on Android 12+ might not continue past the login screen. This is a known issue with the OS, and the current workaround is to restart the device.

## 2.5.1 Release
- Release Date: June 23, 2023
- Server Versions Supported: Server v7.8.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v7.8.0 or later is required.** Support for server [Extended Support Release](https://docs.mattermost.com/upgrade/extended-support-release.html) (ESR) v7.1.0 has ended and upgrading to server ESR v7.8.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

**Note:** Mattermost Mobile App v2.5.1 contains a high level security fix. Upgrading is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Bug Fixes
 - Fixed an issue where reading a thread could lead to the phone and server to overwork.
 - Fixed the overlap between image attachments and the post footer with Collapsed Reply Threads enabled.

## 2.5.0 Release
- Release Date: June 16, 2023
- Server Versions Supported: Server v7.8.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v7.8.0 or later is required.** Support for server [Extended Support Release](https://docs.mattermost.com/upgrade/extended-support-release.html) (ESR) v7.1.0 has ended and upgrading to server ESR v7.8.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Improvements
 - Calls: Added call quality degradation logic and a banner to alert users when they are on unstable connections.
 - Improved client error handling.
 - Post editing now respects the ``message_source`` field.
 - Improved reaction time for the **Copy Text** option.
 - Improved behavior around "Maximum call stack size exceeded" errors.
 - Android: removed unneeded space after the list in the **Find Channels** screen.

### Bug Fixes
 - Fixed an issue where **Search** and **Recent Mentions** did not highlight saved posts.
 - Fixed the interactive dialog radio buttons style when using the light theme.
 - Fixed a small issue when marking threads as read.
 - Fixed an issue where the **Save** button sometimes did not show on the Edit Post screen.
 - Fixed theming issues in the login screen.
 - Fixed an issue where replies sometimes seemed to be attributed to the wrong person or the wrong thread.
 - Ensured users mentioned in message attachments are loaded by the app.
 - Fixed issues with user status synchronization.
 - Fixed duplicated text for SSO login method when only SSO was available.

### Known Issues
 - Users are unable to adjust the font size via the OS font size setting.
 - Some Google Pixel phones on Android 12+ might not continue past the login screen. This is a known issue with the OS, and the current workaround is to restart the device.

## 2.4.0 Release
- Release Date: May 17, 2023
- Server Versions Supported: Server v7.8.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v7.8.0 or later is required.** Support for server [Extended Support Release](https://docs.mattermost.com/upgrade/extended-support-release.html) (ESR) v7.1.0 has ended and upgrading to server ESR v7.8.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Improvements
 - Added mobile support for message acknowledgements and persistent notifications.
 - Added the ability to add members to channels.
 - Increased the character limit for the user's nickname from 22 to 64 characters.
 - Added localization support for iOS usage description strings in permission dialogs.
 - Users can now follow or unfollow a thread and undo the action if needed.
 - Added the ability to search for files posted in a channel.
 - Added support for ``ExperimentalSettings.DelayChannelAutocomplete`` to make the channel autocomplete only appear after typing a couple letters instead of immediately after a tilde.
 - Calls: Redesigned the Calls user interface.
 - Calls: Call threads are now auto-followed when joining from mobile.
 - Calls (Android): Fixed an issue with Bluetooth, and added audio device selection menu.
 - Added support for self-hosted Sentry URL parameters in build scripts.

### Bug Fixes
 - Fixed an issue where the app did not now show an error when adding servers without a diagnostic ID.
 - Fixed an issue where users were unable to select several files when attaching files to a message.
 - Fixed an issue where some channels would appear as if no messages were there.
 - Fixed an issue with using the camera to capture photos/videos on Android versions 9 and below.
 - Fixed a crash on iOS when attempting to open a Thread by tapping on the notification.
 - Fixed an incomplete setup of ``sentry-cli`` node package.
 - Fixed an issue with out of order websocket event handling for posts.
 - Fixed a crash when opening a push notification for a thread when the Thread screen was already opened in the background.
 - Fixed a crash issue and error ``Cannot read property "id" of undefined``.
 - RN Image is now used on local images to avoid cache problems.

### Known Issues
 - Users are unable to adjust the font size via the OS font size setting.
 - Some Google Pixel phones on Android 12+ might not continue past the login screen. This is a known issue with the OS, and the current workaround is to restart the device.

## 2.3.0 Release
- Release Date: April 14, 2023
- Server Versions Supported: Server v7.1.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v7.1.0 or later is required.** Support for server [Extended Support Release](https://docs.mattermost.com/upgrade/extended-support-release.html) (ESR) 6.3.0 has ended and upgrading to server ESR v7.1.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Improvements
 - Calls: Raising a hand will now take precedence when ordering participants in the call screen.
 - Calls: Optimized screensharing in landscape mode for Android and iOS and unlocked landscape mode for iOS phone devices.
 - Channel names are now tappable in threads and in recent mentions, search, and saved message screens.
 - The ``ExperimentalGroupUnreadChannels`` server config is now respected.
 - Added more information to the logs for better debugging.

### Bug Fixes
 - Calls: Fixed an issue with emoji rendering.
 - Calls: Fixed an issue that caused a crash when the current presenter left the call without stopping the screenshare.
 - Fixed an issue with guest badges not appearing on the channel member list.
 - Added minor performance fixes to the channel member list screen.
 - Fixed an issue where some notifications did not show when a channel sidebar category was collapsed.
 - Fixed an issue where tapping on a custom status in the message list did not open the user's profile card.
 - Fixed an issue where the channel members count did not get updated after removing users.
 - Fixed a crash on markdown table images and prevented image-related crashes on other parts of the app.
 - Fixed websocket not connecting during rare scenarios.
 - Fixed the sort order of the search results. Search results now display from newest to oldest.

### Open Source Components
 - Added ``mattermost/calls-common`` to https://github.com/mattermost/mattermost-mobile.

### Known Issues
 - Users are unable to adjust the font size via the OS font size setting.
 - Some Google Pixel phones on Android 12+ might not continue past the login screen. This is a known issue with the OS, and the current workaround is to restart the device.

## 2.2.0 Release
- Release Date: March 17, 2023
- Server Versions Supported: Server v7.1.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v7.1.0 or later is required.** Support for server [Extended Support Release](https://docs.mattermost.com/upgrade/extended-support-release.html) (ESR) 6.3.0 has ended and upgrading to server ESR v7.1.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Improvements
 - Added the ability to set mobile notifications preferences per channel.
 - Added support for connecting the WebSocket over TLS1.3.
 - Calls: Added slash commands to start/stop call recordings (``/call recording [start|stop]``).
 - Calls: Implemented glare free negotiation. This fix prevents potential negotiation problems when two clients try to connect simultaneously.
 - The Help link now is not converted to lowercase.
 - Added minor performance improvements on sending a message.
 - Archived channels show a more detailed warning.

### Bug Fixes
 - Calls: Fixed a rare case where the Join Call banner showed that a call started "53 years ago".
 - Calls: Fixed a crash on joining calls.
 - Fixed an issue where tapping **Send Message** in a user’s profile pop-over did not open a Direct Message channel.
 - Fixed an issue where an incorrect skin tone was applied to emojis selected in the emoji picker.
 - Fixed an issue where the channel list displayed Direct Messages with user accounts that had been deactivated.
 - Fixed an issue with searching for channels and users that contain non-Latin characters.
 - Fixed an issue where selecting an item from the autocomplete doubled tilde and slash characters.
 - Fixed an "Unable to reset your password" issue.
 - Fixed an issue where the Group Message member count showed as 0 on GraphQL enabled instances.
 - Fixed an issue with missing posts in a thread when a post gets deleted.
 - Fixed an issue with saving a draft when navigating away from a thread or channel screens.
 - Fixed an issue with running the app in a Stage Manager on iPad.
 - Fixed an issue with the timing of showing the tutorial for the skin tone selector in the emoji picker.
 - Fixed a crash when toggling Collapsed Reply Thread on/off.
 - Fixed an issue with the push notification display when push notifications were set as a generic message with sender only.

### Known Issues
 - Users are unable to adjust the font size via the OS font size setting.
 - Moving posts with the Wrangler plugin causes database "Unique key" errors [MM-44960](https://mattermost.atlassian.net/browse/MM-44960).
 - Some pixel phones on Android 12+ might not go past the login screen. This is a known issue with the OS and the current workaround is to restart the device.

## 2.1.0 Release
- Release Date: February 16, 2023
- Server Versions Supported: Server v7.1.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v7.1.0 or later is required.** Support for server [Extended Support Release](https://docs.mattermost.com/upgrade/extended-support-release.html) (ESR) 6.3.0 has ended and upgrading to server ESR v7.1.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Improvements
 - Added the ability to manage channel members.
 - Added the option in **Profile > Settings > Display** settings to enable/disable Collapsed Reply Threads.
 - Added functionality to invite users by email and to invite users from other teams on the server.
 - Calls: Calls now start in speaker mode by default.
 - Calls: Calls now show the call thread in root calls posts.
 - Implemented Data Retention for mobile.

### Bug Fixes
 - Calls: fixed an issue with displaying recording messages.
 - Fixed an issue where a long team name wasn’t wrapped and pushed the  "+ icon " next to it.
 - Fixed an issue on Android where user avatars instead of webhook avatars were shown in notifications.
 - Fixed an issue where the file menu remained open after the option to "open in channel" was selected.
 - Fixed the ability to mark a post as unread if the post was created from a webhook.
 - Fixed a crash on iOS versions lower than 16.x when opening an item in the gallery.
 - Fixed an issue where ``enableMobileUploadFiles`` setting was not working correctly.

### Open Source Components
 - Added ``@gorhom/bottom-sheet`` and ``react-native-walkthrough-tooltip`` https://github.com/mattermost/mattermost-mobile.

### Known Issues
 - Selecting an item from autocomplete doubles tilde and slash characters [MM-50351](https://mattermost.atlassian.net/browse/MM-50351).
 - Users are unable to adjust the font size via the OS font size setting.
 - Drafts are lost when following a notification [MM-47373](https://mattermost.atlassian.net/browse/MM-47373).
 - Moving posts with the Wrangler plugin causes database "Unique key" errors [MM-44960](https://mattermost.atlassian.net/browse/MM-44960).
 - Some pixel phones on Android 12+ might not go past the login screen. This is a known issue with the OS and the current workaround is to restart the device.

## 2.0.1 Release
- Release Date: February 7, 2023
- Server Versions Supported: Server v7.1.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v7.1.0 or later is required.** Support for server [Extended Support Release](https://docs.mattermost.com/upgrade/extended-support-release.html) (ESR) 6.3.0 has ended and upgrading to server ESR v7.1.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Improvements
 - Added support for Android tablets and foldables.
 - Added support to rotate iPads in all orientations.
 - Improved the mobile emoji picker user interface and interaction.

### Bug Fixes
 - Fixed a crash when dismissing a notification on Android.
 - Fixed a potential crash when trying access non existent database records.
 - Fixed opening a link when the server is hosted on a subpath.
 - Fixed an issue with uploading certain files.
 - Fixed an issue with downloading certain files from the search results.
 - Disabled top domain level verification.
 - Fixed some potential crashes in the iOS Share Extension and Notification Service.
 - Fixed some screens in the login flow not showing the content when animations are turned off in the device settings.
 - Fixed an issue where new Direct and Group Messages sometimes did not appear in the channel list until reopening the app.
 - The permissions required to receive push notifications is now always requested if needed.
 - Fixed ANRs found with some Android devices.
 - Fixed an issue where the keyboard changed on iOS when a code block was started.
 - Fixed an issue where the EMM configuration for VPN timeouts were in ``seconds`` instead of in ``ms``.
 - Fixed an issue with markdown bolded strings.
 - Fixed an issue where the markdown for mentions did not inherit heading fonts.
 - Fixed an issue where a crash occurred when attempting to download a profile image.
 
### Known Issues
 - Selecting an item from autocomplete doubles tilde and slash characters [MM-50351](https://mattermost.atlassian.net/browse/MM-50351).
 - Users are unable to adjust the font size via the OS font size setting.
 - **Manage Members** modal is not yet added [MM-48489](https://mattermost.atlassian.net/browse/MM-48489).
 - Posts may remain in the local device database after data retention job has been run [MM-47548](https://mattermost.atlassian.net/browse/MM-47548).
 - Drafts are lost when following a notification [MM-47373](https://mattermost.atlassian.net/browse/MM-47373).
 - Moving posts with the Wrangler plugin causes database "Unique key" errors [MM-44960](https://mattermost.atlassian.net/browse/MM-44960).
 - Some pixel phones on Android 12+ might not go past the login screen. This is a known issue with the OS and the current workaround is to restart the device.

## 2.0.0 Release
- Release Date: January 16, 2023
- Server Versions Supported: Server v7.1.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - Please [see here](https://mattermost.com/blog/preparing-for-mobile-v2-0/) for more details on preparing for the mobile v2 release.
 - **Upgrade to server version v7.1.0 or later is required.** Support for server [Extended Support Release](https://docs.mattermost.com/upgrade/extended-support-release.html) (ESR) 6.3.0 has ended and upgrading to server ESR v7.1.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Highlights

Mattermost mobile v2.0 is a major update to the iOS and Android apps bringing support for multiple workspaces and a more stable and performant user experience that includes:

 - Support for collaborating in multiple workspaces with a redesigned channel and team sidebar for easier navigation. 
 - Improved app responsiveness to user input, faster launch, and less memory consumed when running.
 - Improved app stability so users encounter fewer crashes and bugs, as well as reduced app hang and errors if internet connectivity becomes unstable. 

Users now gain a more reliable and feature-rich application, improving their experience for collaborating with their teams on the go.

### Known Issues
 - Landscape mode doesn't work on Android tablets.
 - Users are unable to adjust the font size via the OS font size setting.
 - **Add Members** and **Manage Members** modals are not yet added [MM-48489](https://mattermost.atlassian.net/browse/MM-48489).
 - Posts may remain in the local device database after data retention job has been run [MM-47548](https://mattermost.atlassian.net/browse/MM-47548).
 - Drafts are lost when following a notification [MM-47373](https://mattermost.atlassian.net/browse/MM-47373).
 - Moving posts with the Wrangler plugin causes database "Unique key" errors [MM-44960](https://mattermost.atlassian.net/browse/MM-44960).
 - Some pixel phones on Android 12+ might not go past the login screen. This is a known issue with the OS and the current workaround is to restart the device.
 - The app crashes when uploading a PDF file [MM-49707](https://mattermost.atlassian.net/browse/MM-49707).
 - The ``timeoutVPN`` values are not converted from milliseconds to seconds in v2 [MM-49722](https://mattermost.atlassian.net/browse/MM-49722).

## 1.55.1 Release
- Release Date: September 15, 2022
- Server Versions Supported: Server v6.3.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - Mobile App v1.55.1 is our first extended support release (ESR). We are very excited about the upcoming general availability of the v2.0 mobile app in December. We recognize that some customers may have a custom build of Mattermost mobile and need more time to test or implement their custom changes on mobile v2.0. The mobile ESR will be supported until July 2023. v1.55.1 will receive critical security fixes only and will be released as needed via unsigned builds to our mobile GitHub repository.
 - **Upgrade to server version v6.3.0 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.37 has ended and upgrading to server ESR v6.3.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Bug Fixes
 - Fixed an issue where users were unable to convert public channels to private.
 - Fixed an issue where selected boxes in app forms and interactive dialogs could not be cleared.

### Known Issues
 - Channel sidebar disappears sometimes when the channel categories are not fetched from the server.
 - Posts sometimes get stuck behind the post textbox on iPad.

## 1.55.0 Release
- Release Date: August 16, 2022
- Server Versions Supported: Server v6.3.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v6.3.0 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.37 has ended and upgrading to server ESR v6.3.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Improvements
 - Calls: Implemented WebSocket reconnection support.

### Bug Fixes
 - Calls: Fixed a crash on "cannot replaceTrack after peer is destroyed" error.
 - Fixed an issue with sharing of text alongside an image on Android.
 - Fixed an issue on Android where clicking on a hashtag from the Saved Posts modal returned the user to the channel instead of taking the user to the search results.
 - Fixed an issue where the select modal value was not getting populated.

### Known Issues
 - Channel sidebar disappears sometimes when the channel categories are not fetched from the server.
 - Posts sometimes get stuck behind the post textbox on iPad.

## 1.54.0 Release
- Release Date: July 15, 2022
- Server Versions Supported: Server v6.3.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v6.3.0 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.37 has ended and upgrading to server ESR v6.3.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Improvements
 - Calls: Added support for accepting advanced ICE server configurations through the config.
 - Calls: Added support for using Calls when the Mattermost installation is served under a subpath.
 - Calls: Added support for generating short-lived TURN credentials.

### Bug Fixes
 - Fixed an issue where Latex in root posts crashed the global Threads screen.

### Known Issues
 - The app crashes when the session length for mobile is changed via webapp.
 - Channel sidebar disappears sometimes when the channel categories are not fetched from the server.
 - Posts sometimes get stuck behind the post textbox on iPad.

## 1.53.0 Release
- Release Date: June 15, 2022
- Server Versions Supported: Server v6.3.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v6.3.0 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.37 has ended and upgrading to server ESR v6.3.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Improvements
 - Added Calls Cloud Freemium limits.
 - Added a handler for a new ``call_end`` event.
 - Added support for a new ``MaxCallParticipants`` config setting.

### Known Issues
 - Channel sidebar disappears sometimes when the channel categories are not fetched from the server.
 - Posts sometimes get stuck behind the post textbox on iPad.

## 1.52.0 Release
- Release Date: May 16, 2022
- Server Versions Supported: Server v6.3.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v6.3.0 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.37 has ended and upgrading to server ESR v6.3.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Improvements
 - Added .m4a audio file preview support via the video player.
 - Added the ability to render latex code blocks.

### Known Issues
 - Channel sidebar disappears sometimes when the channel categories are not fetched from the server.
 - Posts sometimes get stuck behind the post textbox on iPad.

## 1.51.2 Release
- Release Date: May 5, 2022
- Server Versions Supported: Server v6.3.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v6.3.0 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.37 has ended and upgrading to server ESR v6.3.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Bug Fixes

#### All apps
 - Fixed an issue with Calls where multiple "Access to route for non-existent plugin" errors got logged in the server logs.

## 1.51.1 Release
- Release Date: April 22, 2022
- Server Versions Supported: Server v6.3.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v6.3.0 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.37 has ended and upgrading to server ESR v6.3.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Bug Fixes

#### All apps
 - Fixed an issue with logging in when multiple SSO methods are enabled while email/password is disabled.

## 1.51.0 Release
- Release Date: April 16, 2022
- Server Versions Supported: Server v6.3.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v6.3.0 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.37 has ended and upgrading to server ESR v6.3.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Breaking Changes
 - The [Apps Framework protocol](https://developers.mattermost.com/integrate/apps/) for binding/form submissions has changed, by separating the single `call` into separate `submit`, `form`, `refresh` and `lookup` calls. If any users have created their own Apps, they have to be updated to the new system.

### Improvements
 - Users are now taken directly to the SSO login if only one SSO login method is enabled.
 - Calls are now enabled on mobile if the server has Calls enabled.
 - For Calls, added "raise hand" functionality and a screensharing icon.
 - "Default Enabled Calls" and "Allow Enable Calls" server settings are now respected by Calls on mobile.
 - Added a speakerphone button to the Calls interface.
 - Added support for link highlighting for capitalized link schemes, such as ``Https://`` instead of ``https://``.
 - Changed the search bar in manual timezone selection view to be consistent with the rest of the app.
 - The mobile app no longer attempts to fetch thread bindings when the ``AppsEnabled`` feature flag is ``false``.
 - The mobile app will now only fetch App bindings if the Apps plugin is enabled.
 - Added support for allowing 1-character channel names.

### Bug Fixes

#### All apps
 - Fixed an issue with Calls banner locations for earlier iPhone models.
 - Fixed an issue where users were not able to scroll down to view custom themes.
 - Fixed a bug that resulted in dropping the Call state when switching to another app and returning.
 - Fixed an issue where some messages could have been cut off if the markdown used had two or more links with an ``=`` sign.

### Known Issues
 - Channel sidebar disappears sometimes when the channel categories are not fetched from the server.
 - Posts sometimes get stuck behind the post textbox on iPad.

## 1.50.1 Release
- Release Date: March 21, 2022
- Server Versions Supported: Server v5.37.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrading to server version v5.37.0 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) v5.31 has ended and upgrading to server ESR v5.37.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Bug Fixes

#### All apps
 - Fixed an issue where Latex-formatted text caused the mobile app to crash.

## 1.50.0 Release
- Release Date: March 16, 2022
- Server Versions Supported: Server v5.37.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v5.37.0 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.31 has ended and upgrading to server ESR v5.37.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Improvements
 - Added support for markdown inline image custom sizes.

### Bug Fixes

#### All apps
 - Fixed an issue where setting a custom status failed silently.

### Known Issues
 - Channel sidebar disappears sometimes when the channel categories are not fetched from the server.
 - Posts sometimes get stuck behind the post textbox on iPad.
 - Various known issues with Collapsed Reply Threads (Beta) feature:
   - New messages banner should only count root posts.
   - Threads item unread state (bolding) does not persist when deleting documents and data.

## 1.49.1 Release
- Release Date: February 23, 2022.
- Server Versions Supported: Server v5.37.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v5.37.0 or later is required.** Support for server [Extended Support Release](/administration/extended-support-release.html) (ESR) 5.31 has ended and upgrading to server ESR v5.37.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Bug Fixes

#### Android specific
 - Fixed an issue on Android where document files did not open.

## 1.49.0 Release
- Release Date: February 16, 2022
- Server Versions Supported: Server v5.37.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v5.37.0 or later is required.** Support for server [Extended Support Release](/administration/extended-support-release.html) (ESR) 5.31 has ended and upgrading to server ESR v5.37.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Improvements
 - Added SVG support for markdown inline images.

### Bug Fixes

#### All apps
 - Fixed an issue where the date picker jumped back to the current month after the past date selection.
 - Fixed a crash issue on markdown table images.
 - Fixed an issue with Collapsed Reply Threads where clicking on a permalink added the thread replies in the channel view.
 - Fixed an issue with Collapsed Reply Threads where link previews disappeared when a thread was created.

### Known Issues
 - Some files (such as PDFs) fail to open/download on v1.49.0 [MM-41968](https://mattermost.atlassian.net/browse/MM-41968).
 - Channel sidebar disappears sometimes when the channel categories are not fetched from the server.
 - Posts sometimes get stuck behind the post textbox on iPad.
 - Various known issues with Collapsed Reply Threads (Beta) feature:
   - New messages banner should only count root posts.
   - Threads item unread state (bolding) does not persist when deleting documents and data.

## 1.48.2 Release
- Release Date: January 6, 2022
- Server Versions Supported: Server v5.37.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v5.37.0 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.31 has ended and upgrading to server ESR v5.37.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Bug Fixes

#### All apps
 - Fixed an issue with custom status updates with no expiry.

### Known Issues
 - Channel sidebar disappears sometimes when the channel categories are not fetched from the server.
 - Posts sometimes get stuck behind the post textbox on iPad.
 - Various known issues with Collapsed Reply Threads (Beta) feature:
   - New messages banner should only count root posts.
   - Clicking on a permalink adds the thread replies in the channel view.
   - Threads item unread state (bolding) does not persist when deleting documents and data.

## 1.48.1 Release
- Release Date: December 15, 2021
- Server Versions Supported: Server v5.37.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v5.37.0 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.31 has ended and upgrading to server ESR v5.37.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Bug Fixes

#### All apps
 - Fixed a crash on collapsed reply threads when opening the Gallery view from within a Thread.
 - Fixed an issue with clearing and grouping of push notifications when Collapsed Reply Threads is enabled.
 - Fixed an issue with opening the YouTube app from within Mattermost.

### Known Issues
 - Channel sidebar disappears sometimes when the channel categories are not fetched from the server.
 - Posts sometimes get stuck behind the post textbox on iPad.
 - Various known issues with Collapsed Reply Threads (Beta) feature:
   - New messages banner should only count root posts.
   - Clicking on a permalink adds the thread replies in the channel view.
   - Threads item unread state (bolding) does not persist when deleting documents and data.

## 1.48.0 Release
- Release Date: November 16, 2021
- Server Versions Supported: Server v5.37.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v5.37.0 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.31 has ended and upgrading to server ESR v5.37.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Highlights

#### Cross-team Recent Mentions
 - Recent mentions and saved posts now show across all teams.

### Improvements
 - Adjusted channel override mobile notification preferences for Threads.
 - Added long-press options to the Global Threads screen.
 - Added a new messages line to the Threads screen.
 - Added "pull to refresh" to load threads in the Global Threads screen.
 - Added OAuth support for plugins and apps.
 - Added multiselect support for apps forms.
 - Added a "Rest" field app command to filter empty options on static and dynamic selects and to prohibit executing non-leaf commands.
 - App bindings now recognize the post menu options for each channel they live in.
 - Added ``@here`` mention to the ``EnableConfirmNotificationsToChannel`` config setting to show a warning modal when over 5 members might be alerted with ``@here``.
 - Updated "Jump to..." to match webapp equivalent user interface string.

### Bug Fixes

#### All apps
 - Fixed an issue where image previews could only be viewed once while on the Thread view.

### Known Issues
 - Channel sidebar disappears sometimes when the channel categories are not fetched from the server.
 - Posts sometimes get stuck behind the post textbox on iPad.
 - Various known issues with Collapsed Reply Threads (Beta) feature:
   - New messages banner should only count root posts.
   - Clicking on a permalink adds the thread replies in the channel view.
   - Threads item unread state (bolding) does not persist when deleting documents and data.

## 1.47.2 Release
- Release Date: October 25, 2021
- Server Versions Supported: Server v5.37.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v5.37.0 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.31 has ended and upgrading to server ESR v5.37.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Bug Fixes

#### iOS specific
 - Fixed an issue copying and pasting files on iOS.

#### Android specific
 - Fixed a crash when switching channels or focusing the text input area on Android.
 - Fixed a crash while opening notifications on Android.

## 1.47.1 Release
- Release Date: October 19, 2021
- Server Versions Supported: Server v5.37.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v5.37.0 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.31 has ended and upgrading to server ESR v5.37.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Bug Fixes

#### All apps
 - Fixed an issue where navigating to Global Threads crashed the app.
 - Fixed Text input font scaling to follow the OS setting to fix an issue where iOS Dynamic Type size was not correct in the message box.

#### iOS specific
 - Updated the iOS app icon to a flattened version.
 - Fixed a gesture conflict between the drawers and the post input on iOS.

## 1.47.0 Release
- Release Date: October 13, 2021
- Server Versions Supported: Server v5.37.0+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v5.37.0 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.31 has ended and upgrading to server ESR v5.37.0 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 12.1+ is required.

### Highlights

#### Branding Changes
 - Updated the Splash Screen, app icons, and Threads illustration to align with new branding.
 - Added a new default brand theme named "Denim".
 - The existing theme names and colors, including "Mattermost", "Organization", "Mattermost Dark", and "Windows Dark" have been updated to the new "Denim", "Sapphire", "Indigo", and "Onyx" theme names and colors, respectively. Anyone using the existing themes will see slightly modified theme colors after their server or workspace is upgraded. The theme variables for the existing "Mattermost", "Organization", "Mattermost Dark", and "Windows Dark" themes will still be accessible in [our documentation](/messaging/customizing-theme-colors.html#custom-theme-examples), so a custom theme can be created with these theme variables if desired. Custom themes are unaffected by this change.
 - Added a new light theme named "Quartz" to the default available list of themes.

#### Deprecations
 - Stopped evaluating deprecated config settings starting with server version 6.0.

#### Custom, Collapsible Channel Categories
 - App now displays custom categories in the sidebar.

### Improvements
 - Added mobile push notifications for followed Threads.
 - Increased the limit of uploaded file attachments per post from 5 to 10.
 - Removed deprecated ``Posts.ParentId`` in favor of the semantically equivalent ``Posts.RootId``.
 - Added better support for channel and user selection from within Apps commands.
 - Added better binding filtering for Apps.

### Bug Fixes

#### All apps
 - Added an option to download a video in the gallery view if it failed to playback.
 - Fixed an issue where the emojis were cutoff when editing a message with jumbo emojis.
 - Fixed an issue where some mentions were highlighted when the mention key partially matched the mention in the message.
 - Fixed an issue with in-app notifications that caused the keyboard to blur when the notifications were automatically dismissed.
 - Fixed an issue where the autocomplete options were still visible when the keyboard was dismissed.
 - Fixed an issue where the “Loading messages…” text was upside down.
 - Fixed an issue where tapping on the push notification for a new reply did not open the thread with the post.
 - Fixed an issue where opening a push notification while in the Thread screen did not take the user to the channel screen.
 - Fixed an issue where a System message was missing when a guest user was added to a channel or when a guest joined a channel.
 - Fixed an error where the submit button on interactive dialogs was not shown when the dialog did not specify ``submit_label``.
 - Fixed an issue where pressing **Jump to** on mobile showed a different highlighted channels list than the sidebar highlighted channels list.
 - Removed Date and Time label from recently used custom statuses.
 - Fixed an error with locations and binding filtering.

#### iOS specific
 - Fixed a crash when attempting to share content into Mattermost on iOS when Biometric authentication was required.

#### Android specific
 - Fixed the ability to snooze push notifications on Android.
 - Fixed an issue with uploading of animated gif files on Android.

### Known Issues
 - An error may occur when archiving a channel or when attempting to post to an archived channel.
 - The "+" to add a reaction is still visible in archived channels.
 - Close Preview X and Close Settings X are themed incorrectly in Quartz theme.
 - Channel sidebar disappears sometimes in Airplane mode.
 - Posts sometimes get stuck behind the post textbox on iPad.
 - Various known issues with Collapsed Reply Threads (Beta) feature:
   - New messages banner should only count root posts.
   - Turning the feature on and off does not push an update to the Mobile client.
   - Clicking on a permalink adds the thread replies in the channel view.
   - Threads item unread state (bolding) does not persist when deleting documents and data.

## 1.46.0 Release
- Release Date: August 16, 2021
- Server Versions Supported: Server v5.31.3+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v5.31.3 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.25 has ended and upgrading to server ESR v5.31.3 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 11+ is required.

### Highlights

#### Collapsed Reply Threads (Beta)
 - Added support for [Collapsed Reply Threads](https://mattermost.com/blog/collapsed-reply-threads-beta/) for the mobile apps.

#### Custom Status Expiry
 - Added a feature to choose expiry time when setting a custom status. Requires server version 5.37 or later. Also added new screens such as **Clear** and new components such as ``DateTime`` picker.

#### Granular Data Retention Policies 
 - Added support for Granular Data Retention Policies for the mobile apps. Requires server version 5.37 or later.

### Improvements
 - Added the custom statuses to the mention autocomplete.
 - Changed the default behavior of autocomplete user interface for cases of long display names. Long display names will be truncated to show the username.
 - Added support for showing plugin slash command icons.
 - Added support for apps to add arbitrary markdown in between fields on forms.
 - Implemented a new style for app submit buttons.
 - Added markdown support for app fields descriptions and errors.

### Bug Fixes

#### All apps
 - Fixed an issue where boolean fields did not get disabled on dialogs when they should have.
 - Fixed an issue with displaying the current user when multiple users were part of the System join / leave messages.
 - Fixed a race condition when bringing the app to the foreground by tapping in a notification that belongs to a channel other than the current channel that caused the current channel to miss any mentions if it had any.
 - Fixed an issue with attaching files to the correct post.

#### Android specific
 - Fixed a silent crash that could happen for some users when receiving a push notification on Android.

### Known Issues
 - Posts sometimes get stuck behind the post textbox on iPad.
 - User may need to log out and back in from the app to see data retention results on the app.
 - Various known issues with Collapsed Reply Threads (Beta) feature:
   - Mobile app top bar disappears after resuming app from screen lock.
   - New messages banner should only count root posts.
   - Clicking Jump to on mobile shows a different highlighted channel list than the sidebar highlighted channel list.
   - Only the last six threads are visible in the Threads view.
   - Some unread channels with leave/join system messages are doubled in search results.
   - Tapping on the push notification for new reply should open the thread with the post.
   - Turning the feature on and off does not push an update to the Mobile client.
   - Clicking on a permalink adds the thread replies in the channel view.
   - Threads item is lost when clearing search in the channel sideabar.
   - Previously viewed Thread is auto-followed after new replies come in.
   - Threads item unread state (bolding) does not persist when deleting documents and data.
   - Clicking Jump to on mobile shows different highlighted channels list than the sidebar unread channels list.

### Contributors
 - [anurag6713](https://github.com/anurag6713), [ashishbhate](https://github.com/ashishbhate), [enahum](https://github.com/enahum), [larkox](https://github.com/larkox), [manojmalik20](https://github.com/manojmalik20)

## 1.45.1 Release
- Release Date: July 20, 2021
- Server Versions Supported: Server v5.31.3+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v5.31.3 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.25 has ended and upgrading to server ESR v5.31.3 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes

#### All apps
 - Fixed an issue where the app crashed when a message with only emojis included a hard break.

#### Android specific
 - Fixed Android push notifications so that they are now grouped by channel.

## 1.45.0 Release
- Release Date: July 16, 2021
- Server Versions Supported: Server v5.31.3+ is required. Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device.

### Compatibility
 - **Upgrade to server version v5.31.3 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.25 has ended and upgrading to server ESR v5.31.3 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 11+ is required.

### Highlights

#### Emoji Enhancements with Skin Tone Selection
 - Added support for emoji standard v13.0 with Mattermost server v5.37. **Note: Due to the upgrade to Emoji 13.0, some emojis may be missing on Android older than 11 and iOS older than 14.2.**

#### English-Australian Language Support
 - Mattermost is now available in English-Australian.

### Improvements
 - Added the ability to reply to individual messages from push notifications on Android.
 - Included message sender's user icon in push notifications.
 - Removed the nickname from the user autocomplete when the item is the current user.
 - The "swipe up to refresh" functionality was added back.

### Bug Fixes

#### All apps
 - Fixed an issue where the progress indicator did not display for all attachments in the post draft when adding multiple images at once.
 - Fixed an issue where tapping a channel link from a reply thread did not open the channel.
 - Fixed an issue that caused the reply from a push notification to fail when the message belonged to a thread.
 - Fixed an issue where the at-sign ``@`` was not ignored when searching for users.
 - Fixed the post draft to correctly detect if the channel being viewed is read only, including when the thread view is from a different channel than the current channel.
 - Fixed the render of auto-responder posts.
 - Fixed an issue where the option to join another team was not present after deleting cache & data.

#### Android specific
 - Fixed Android not being hidden when going back in the thread screen when the keyboard was opened.

#### iOS specific
 - Fixed an animation transition when displaying the options menu on iOS.

### Known Issues
 - Android app doesn't group notifications properly [MM-37134](https://mattermost.atlassian.net/browse/MM-37134).

## 1.44.1 Release
- Release Date: June 28, 2021
- Server Versions Supported: Server v5.31.3+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.31.3 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.25 has ended and upgrading to server ESR v5.31.3 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes

#### All apps
 - Added a fix to prevent a crash when message attachments or app bindings were ``null``.
 - Fixed an issue where the app crashed when bringing the app from the background after tapping on a deep link.
 - Added back the permalink view from search, recent mentions, pinned and saved posts.
 - Fixed an issue where the custom status did not get reflected on the Mobile App until closing and reopening the app when changing the custom status from the webapp while the Mobile App was in the background.

#### iOS specific
 - Fixed an issue where the keyboard covered the messages on the channel screen.
 - Fixed an issue where a YouTube playback error could appear when clicking the thumbnail of a linked YouTube video.
 - Fixed an issue where the badge count on the app icon for iOS was incorrect.

## 1.44.0 Release
- Release Date: June 16, 2021
- Server Versions Supported: Server v5.31.3+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.31.3 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.25 has ended and upgrading to server ESR v5.31.3 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 11+ is required.

**Note:** Mattermost Mobile App v1.44.0 contains low to high level security fixes. Upgrading is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Highlights

#### Custom Statuses
 - Added the custom status feature support for mobile apps. Mattermost server v5.36+ is required to access custom statuses on mobile.
 
#### Shared Channels
 - Added support for Shared Channels feature (Experimental, Enterprise Edition E20) by displaying information and icons for the shared channels and remote users. Also added shared channel filter for browser channels. This feature is available in Mattermost server versions v5.35.0+.

#### Hungarian Language (Beta)
 - Added a new language, Hungarian (beta).

### Improvements
 - Added support for localization with country variants.
 - The "swipe up to refresh" functionality was removed to fix an issue where the app performed slowly on Android devices.

### Bug Fixes

#### Android specific
 - Fixed an issue where the app performed slowly on Android devices that ran at 120fps instead of the normal 60fps.

### Known Issues
 - When changing the custom status from the webapp while the Mobile App is in the background, the custom status does not get reflected on the Mobile App until you close and re-open the Mobile App.
 - Users will need to be on v5.31.3 for the "Unsupported server version" in-app notice to go away as [5.31.3 fixes an issue](/install/self-managed-changelog.html#release-v5-31-esr) where the server version was reported as v5.30.0.
 - On iOS, a YouTube playback error may appear when clicking the thumbnail of a linked YouTube video. A workaround is to tap on the link to open the video in YouTube.

## 1.43.0 Release
- Release Date: May 16, 2021
- Server Versions Supported: Server v5.31.3+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.31.3 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.25 has ended and upgrading to server ESR v5.31.3 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 11+ is required.

### Highlights

#### Support for Apps Framework (Developer Preview)
 - Apps Framework is now supported on the mobile client and allows developers to create Apps which have interactivity and buttons on mobile. You can learn more at https://developers.mattermost.com/integrate/apps/.

### Improvements
 - Added avatars to the sidebar Direct Messages and channel info.
 - On Websocket reconnect, instead of getting all the groups, only the updated groups are now fetched.
 - Team channels including archived channels are now fetched since the last known timestamp.

### Bug Fixes

#### All apps
 - Fixed an issue where appended skin tone emoji didn't render on the app.
 - Fixed an issue where users were unable to get to the last line when editing a very long post.
 - Fixed the user autocomplete by adding the current user to the list.

#### Android specific
 - Fixed an issue where archived teams were accessible and functional.
 - Fixed an issue where uploading files failed when uploading multiple files.

#### iOS specific
 - Fixed an issue on iPad where the last message rendered behind the input box.
 - Fixed an issue that caused the draft to be saved for a different channel when running the app on tablet devices.
 - Fixed an issue where the **Automatic replies** setting's **Done** button on the keyboard added a new line.

### Known Issues
 - Users will need to be on v5.31.3 for the "Unsupported server version" in-app notice to go away as [5.31.3 fixes an issue](/install/self-managed-changelog.html#release-v5-31-esr) where the server version was reported as v5.30.0.
 - On iOS, a YouTube playback error may appear when clicking the thumbnail of a linked YouTube video. A workaround is to tap on the link to open the video in YouTube.
 - The app has been reported to perform slowly on Android devices that run at 120fps instead of the normal 60fps.

## 1.42.1 Release
- Release Date: April 19, 2021
- Server Versions Supported: Server v5.31.3+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.31.3 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.25 has ended and upgrading to server ESR v5.31.3 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes

#### All apps
 - Set the minimum server version to 5.31.3 instead of 5.31.0 for the "Unsupported server version" in-app notice. Servers will need to be on v5.31.3 for the in-app notice to go away as [5.31.3 fixes an issue](/install/self-managed-changelog.html#release-v5-31-esr) where the server version was reported as v5.30.0.

#### iOS specific
 - Fixed an issue where the app crashed on launch.

## 1.42.0 Release
- Release Date: April 16, 2021
- Server Versions Supported: Server v5.31.3+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.31.3 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.25 has ended and upgrading to server ESR v5.31.3 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 11+ is required.

### Highlights

#### Support for Apps Framework (Developer Preview)
 - This feature is available on Mobile Apps when Apps Framework becomes available on Mattermost v5.35.0 and the proxy plugin is loaded on an instance. The launch for the Developer Preview of the Apps Framework is scheduled for April 29th.

### Bug Fixes

#### All apps
 - Fixed an issue where the parser of images did not accept URL escaped string, contrary to what happens in the webapp.
 - Fixed an issue where images with a transparent background showed as black in the gallery.
 - Fixed an issue where the Mention Highlight Link Color was not being used properly.
 - Fixed an issue where sliding did not work when five images were uploaded.
 - Fixed a minor typo in the search **in:** modifier label.
 - Fixed an issue where OpenGraph without images did not show the image placeholder.

#### Android specific
 - Fixed an issue with frequent logouts on the latest Android OS.
 - Fixed an issue where the app crashed when pressing the back button while sharing an image.
 - Fixed an issue where uploading and sharing PDFs crashed the app.
 - Fixed an issue where the image gallery view had a weird behaviour and did not close smoothly.

### Known Issues
 - Users will need to be on v5.31.3 for the "Unsupported server version" in-app notice to go away as [5.31.3 fixes an issue](/install/self-managed-changelog.html#release-v5-31-esr) where the server version was reported as v5.30.0.
 - The app has been reported to perform slowly on Android devices that run at 120fps instead of the normal 60fps.
 - The last message in a channel is sometimes rendered behind the message box on iPad devices.

## 1.41.1 Release
- Release Date: April 7, 2021
- Server Versions Supported: Server v5.25+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.25 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.19 has ended and upgrading to server ESR v5.25 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed an issue where authenticating with any SAML provider opened the default browser, breaking the app VPN tunnel.

## 1.41.0 Release
- Release Date: March 16, 2021
- Server Versions Supported: Server v5.25+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.25 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.19 has ended and upgrading to server ESR v5.25 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 11+ is required.

**Note:** Mattermost Mobile App v1.41.0 contains a high level security fix. Upgrading is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Improvements
 - Refined animations for the new image gallery.
 - System Admins are now prompted before joining a private channel via a permalink.
 - The ``filteredEmojis`` is now calculated on first change.

### Bug Fixes

#### All apps
 - Fixed an issue where the status and reminder time did not get updated in "Update Status" screen in the Incident Collaboration plugin on the mobile apps.
 - Fixed an issue where a handler was missing for permalinks with ``_redirect``.

### Known Issues
 - Frequent logouts from the app have been experienced on the latest Android OS. Some ways to recover include logging out from the app and then uninstalling and installing the app, as well as restarting the device.
 - On Pixel 4a, uploading PDFs crashes the app and sharing files does not work.
 - The app has been reported to perform slowly on Android devices that run at 120fps instead of the normal 60fps.
 - The last message in a channel is sometimes rendered behind the message box on iPad devices.

## 1.40.0 Release
- Release Date: February 25, 2021
- Server Versions Supported: Server v5.25+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.25 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.19 has ended and upgrading to server ESR v5.25 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).	
 - iPhone 5s devices and later with iOS 11+ is required.
 
**Note:** Mattermost Mobile App v1.40.0 contains a low level security fix. Upgrading is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Improvements
 - Added support for OpenID Connect (E20 Edition) - **This feature is available in Mattermost Cloud and will be available in upcoming server v5.33.0 (March 16th) release.**
 - Changed the OAuth / SAML login flow to utilize an external browser instead of the WebView in the Mobile App.
 - Added new languages, Bulgarian and Swedish.

### Bug Fixes

#### All apps
 - Fixed an issue where deeply nested asterisks caused the app to crash.
 - Fixed an issue where the app crashed when attempting to render a post whose attachment value was null.
 - Fixed an issue where in-app notification banner locked user interaction until the notification banner was dismissed.
 - Fixed an issue where posts with at-mentions were double posting if the user hit the **Send** button quickly multiple times in a thread.
 - Fixed an issue where users were unable to add more than 40 emoji reactions on a post.
 - Fixed an issue where unexpected emoji picker sometimes appeared in search results.
 - Fixed an issue where "(you)" did not appear after the current username when using ``@yourself`` autocomplete in a channel.

#### iOS specific
 - Fixed an issue where users were unable to scroll horizontally to view multiple file attachments.

### Known Issues
 - Frequent logouts from the app have been experienced on the latest Android OS. Some ways to recover include logging out from the app and then uninstalling and installing the app, as well as restarting the device.
 - On Pixel 4a, uploading PDFs crashes the app and sharing files does not work.
 - The app has been reported to perform slowly on Android devices that run at 120fps instead of the normal 60fps.
 - The last message in a channel is sometimes rendered behind the message box on iPad devices.

## 1.39.0 Release
- Release Date: January 16, 2021
- Server Versions Supported: Server v5.25+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.25 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.19 has ended and upgrading to server ESR v5.25 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Improvements
 - Teams in the sidebar are now ordered by user preference.
 - Typing an emoji in a post now adds the emoji to the list of recently used emojis.

### Bug Fixes
 
#### All apps
 - Fixed an issue where users were unable to open files with file names that contained multiple dots.
 - Fixed an issue where ``/mscalendar settings`` did not redirect a user to the bot Direct Message channel.
 - Fixed an issue where tapping on an archived channel link from the app did not redirect the user to the archived channel.

#### Android specific
 - Fixed an issue where in some cases the deviceID used to receive push notifications wasn't being attached to the session as the registration completed.

#### iOS specific
 - Fixed an issue where custom URL schemes didn't work.

### Known Issues
 - Frequent logouts from the app have been experienced on the latest Android OS. Some ways to recover include logging out from the app and then uninstalling and installing the app, as well as restarting the device.
 - The app has been reported to perform slowly on Android devices that run at 120fps instead of the normal 60fps.
 - In-app notification banner locks user interaction until the notification banner is dismissed.
 - The last message in a channel is sometimes rendered behind the message box on iPad devices.

## 1.38.1 Release
- Release Date: December 18, 2020
- Server Versions Supported: Server v5.25+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.25 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.19 has ended and upgrading to server ESR v5.25 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed an issue where the v1.38.0 app crashed on iPadOS 14 when reopened from the app switcher.
 - Fixed an issue where the at-mention and slash command suggestion autocomplete modals blocked the post draft.

## 1.38.0 Release
- Release Date: December 16, 2020
- Server Versions Supported: Server v5.25+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.25 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.19 has ended and upgrading to server ESR v5.25 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.
 
**Note:** Support for landscape orientation was removed for non-tablet devices.

### Improvements
 - Added gallery user interface improvements.
 - Images now load progressively as the image comes into view-port instead of loading all the images on mount.
 - Mattermost is now resizeable on Android Desktops such as Samsung DeX.
 - "Something went wrong" message block is now vertically centered.

### Bug Fixes

#### All apps
 - Fixed an issue where the apps frequently failed to load channels for initial team.
 - Fixed an issue where all channel push notifications were cleared when opening one channel's push notification.
 - Fixed an issue where post edits and deletes propagated inconsistently.
 
#### Android specific
 - Fixed an issue where the list of Group Mentions was not updated when Groups were added or removed in an LDAP Group Synced Team.
 - Fixed an issue where a group mention was highlighted by default before it was posted.

#### iOS specific
 - Fixed an issue where the header area overlapped notch on launch on iPhone 12.
 
### Known Issues
 - At-mention and slash command suggestion autocomplete modals block post draft.

## 1.37.0 Release
- Release Date: November 16, 2020
- Server Versions Supported: Server v5.25+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.25 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.19 has ended and upgrading to server ESR v5.25 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Improvements
 - Icons have been updated across the app to be more consistent and adhere to new design standards.
 - The user autocomplete now allows matching on terms with spaces (For example: @firstname lastName) the same way as in the WebApp.

### Bug Fixes

#### All apps
 - Fixed an issue where the app crashed when a user received a notification while dismissing a modal.
 - Fixed an issue where users were still able to paste files in the message box even when mobile file uploads were disabled in the System Console.
 - Fixed an issue where tapping on an invalid permalink showed an error.
 - Fixed an issue where Global Default notification channel setting displayed incorrect notification defaults.
 - Fixed an issue where the channel info count for Group Messages did not match the total number of users when both active and deactivated users were present.
 - Fixed an issue where the hamburger icon width had changed and notification badges were misaligned.
 - Fixed an issue where the redux-persist serializer did not return a value based on the type of the argument.
 
#### Android specific
 - Fixed an issue where the Android app added autofill data in the chat box.
 - Fixed an issue where the Android app defaulted to Town Square after sharing a file outside of the app.

## 1.36.0 Release
- Release Date: October 16, 2020
- Server Versions Supported: Server v5.25+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.25 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.19 has ended and upgrading to server ESR v5.25 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Improvements
 - Added **Channel Info > Notification Preferences** to add the ability to edit mobile push notification settings at the channel level.
 - Server URL now autofills when opening the app from a mobile browser landing page.
 - Added support for accessibility to the channel header buttons.
 - Refactored the post draft component, including writing and posting messages, attaching images, using the autocomplete functionality, showing alerts from group mentions and channel wide mentions, and executing slash commands.
 - Improved the empty state screen for Recent Mentions.
 - Improved ``in:@user`` search to return Direct and Group Message search results.
 - Improved styling of Read Only channels.
 - Removed the filename from an error message when an image/video was too large.
 - Improved unread badge styling of the hamburger menu and team icons.
 - Improved styling of autocomplete modals.
 - Improved the validation error message of the Enter Server URL screen when entering an invalid server URL.

### Bug Fixes

#### All apps
 - Fixed an issue where a hashtag (#) character added to an announcement banner caused the app to display a blank screen.
 - Fixed an issue where users were still able to upload files via the share extension when ``EnableMobileFileUpload`` was disabled on the server.
 - Fixed an issue where a draft message on the reply thread was not retained if the user navigated away from the thread.
 - Fixed an issue where a thumbnail of a file attachment posted in a reply thread displayed in the center channel.
 - Fixed an issue where users were unable to join public channels via channel links.

#### iOS specific
 - Fixed an issue where user received an error when opening links on iOS 14 when Safari was not set as the default browser.

## 1.35.1 Release
- Release Date: September 21, 2020
- Server Versions Supported: Server v5.19+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.19 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.9 has ended and upgrading to server ESR v5.19 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app. See [this blog post](https://mattermost.com/blog/support-for-esr-5-9-has-ended/) for more details.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed an issue where the app crashed when tapping on "Show More" on a long post and then tapping on the post to go to the thread.

## 1.35.0 Release
- Release Date: September 16, 2020
- Server Versions Supported: Server v5.19+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.19 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.9 has ended and upgrading to server ESR v5.19 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app. See [this blog post](https://mattermost.com/blog/support-for-esr-5-9-has-ended/) for more details.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Highlights

#### Upgrade to React Native 0.63.2
 - React Native 0.63.2 introduces performance and stability improvements to the core app platform.

### Improvements
 - Addded a default empty search state for the emoji picker screen.
 - Added an alert box to let users know what happened when removed from a channel they were viewing.

### Bug Fixes

#### All apps
 - Fixed an issue where the app crashed on a channel that had lot of images and attachments.
 - Fixed an issue where YouTube videos rendered as OpenGraph objects but also displayed play buttons when posted using bit.ly links.
 - Fixed an issue where at-mention notifications followed by a period were not highlighted.
 - Fixed an issue where the permission to delete other users' posts did not function independently of deleting own posts.
 - Fixed an issue where archiving a channel while in the permalink view cleared the permalink view content.
 - Fixed an issue where edits to “Full Name” in Mattermost profile got overwritten by the setting from the GitLab / Google / Office365 Single Sign-On providers.
 - Fixed an issue where an AD/LDAP group mention of an outsider group was highlighted on a Group Synced channel.

#### Android specific
 - Fixed an issue where users were unable to upload files with spaces in the file name.

#### iOS specific
 - Fixed an issue where using keyboard dictation sent a blank message.
 - Fixed an issue where users were unable to swipe to close the left-hand side after closing the keyboard.
 - Fixed an issue where the channel info screen ``This channel has guests`` text was out of safe area.
 
### Known Issues
 - Some Android devices running Android 11 may notice some choppiness in certain animations.

## 1.34.1 Release
- Release Date: August 27, 2020
- Server Versions Supported: Server v5.19+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.19 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.9 has ended and upgrading to server ESR v5.19 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app. See [this blog post](https://mattermost.com/blog/support-for-esr-5-9-has-ended/) for more details.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed an issue where GitLab SSO was appending a # sign causing the app to fail on further requests.
 - Fixed an issue where an "Hair on fire" emoji caused the app to crash.
 - Fixed an issue where the app crashed when receiving a push notification when having special characters in the Nickname field.

## 1.34.0 Release
- Release Date: August 16, 2020
- Server Versions Supported: Server v5.19+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.19 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.9 has ended and upgrading to server ESR v5.19 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app. See [this blog post](https://mattermost.com/blog/support-for-esr-5-9-has-ended/) for more details.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.
 
### Highlights
 - End users will now receive an in-app notification to contact their System Admin to upgrade the server version if they are running versions v5.18 and below.
 - Added support for [LDAP group mentions (E20 feature)](/onboard/ad-ldap-groups-synchronization.html) for mobile apps.
 - Added support for non-cached slash command autocomplete for mobile apps.

### Improvements
 - Removed auto-scrolling to the new message line on channel load and added a "More Messages" button when there are unread posts.
 - Improved screen styling for iOS Settings, Profile, Channel Info, "+" button for DMs and channels, Create Channel, and other user profile pages.
 - Added the ability to view users' first and last name in the profile view.
 - Added support on Android for showing a toast to exit when pressing the back button on channel screen.
 - Added the ability for editing others' posts to function independently of Edit Own Posts.
 
### Bug Fixes

#### All apps
 - Fixed an issue where an endless spinner instead of an error message was displayed when SSO login action failed.
 - Fixed an issue where users were unable to create channels when first joining a team.
 - Fixed an issue where an extra separator line appeared above the message box in landscape view after using mentions autocomplete.
 - Fixed an issue where the at-symbol was shown twice when clicking on the at-icon.

#### Android specific
 - Fixed an issue with keyboard glitches after using an invalid slash command.
 - Fixed an issue where the keyboard did not disappear when closing the channel sidebar **More** screen.
 - Fixed an issue where typing right after clicking the send button didn't clear the old message.

#### iOS specific
 - Fixed an issue where users were unable to edit a message that contained a bullet list.
 - Fixed an issue where user was unable to scroll or tap on emoji autocomplete in post **Edit** screen.
 - Fixed an issue where the channel list was not scrolled to the bottom when a new message was received while the keyboard was open.

## 1.33.1 Release
- Release Date: July 15, 2020
- Server Versions Supported: Server v5.19+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.19 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.9 has ended and upgrading to server ESR v5.19 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app. See [this blog post](https://mattermost.com/blog/support-for-esr-5-9-has-ended/) for more details.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.
 
### Bug Fixes
 - Fixed an issue where the apps crashed when a malformed YouTube link was posted in a channel.

## 1.33.0 Release
- Release Date: July 16, 2020
- Server Versions Supported: Server v5.19+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.19 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.9 has ended and upgrading to server ESR v5.19 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app. See [this blog post](https://mattermost.com/blog/support-for-esr-5-9-has-ended/) for more details.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.
 
### Breaking Changes
 - Starting with mobile app v1.33.0, users on server versions below v5.19 may experience issues with how attachments, link previews, reactions and embed data are displayed. Updating your server to v5.19 or later is required.
 
**Note:** Mattermost Mobile App v1.33.0 contains a low level security fix. Upgrading is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
 
### Highlights
 -  System admins will now receive an in-app notification to upgrade their server version if they are running versions v5.18 and below.

### Improvements
 - Removed **Select Team** title in cases where teams aren't loading.
 - The at-mention and search autocompletes now render even if there is a server request or a network outage.
 
### Bug Fixes

#### All apps
 - Fixed an issue where push notifications did not redirect to the correct channel when the app was not running in the background.
 - Fixed an issue where Enterprise mobility management (EMM) filled username field was not accepted as a valid username.
 - Fixed an issue where the app did not open on server url screen with previous server url filled in after logging out.
 - Fixed an issue where leaving a team in a browser while the mobile app was open caused the app to be stuck in the team.
 - Fixed an issue where, when hitting the **Delete Documents & Data** button, the button to join the team disappeared.
 - Fixed an issue where the channel header transition to landscape mode was slow.
 - Fixed an issue where teams were not listed alphabetically on the **Select Team** screen.
 - Fixed an issue where a currently active unread channel was not bolded.
 - Fixed an issue where a team icon was not visible on the left-hand side.
 - Fixed an issue where user was unable to create channels directly after joining a team.
 - Fixed an issue where the **:** search date picker on edit replaced the date and left old date info.
 - Fixed an issue where a confusing **Invalid Message** banner was present on Edit Message modal when typing a message that was over the character limit.
 - Fixed an issue with an unhandled error when logging out from the **Select Team** screen.
 - Fixed an issue where an error message on Server URL screen moved strangely when the keyboard slid on.
 - Fixed an issue with an uneven horizontal margins around **Jump to** box.
 - Fixed an issue where the OneLogin button had a blue outline, but a green fill.

#### Android specific
 - Fixed an issue where hitting edit multiple times opened the edit window without a save button.

#### iOS specific
 - Fixed an issue where ``switchKeyboardForCodeBlocks`` crashed the app on iOS 11.
 - Fixed an issue where the Enter key did not work in search when using an iPad with an external keyboard.
 - Fixed an issue where OAuth and SAML single sign-on (SSO) no longer required re-entering credentials after logging out and logging back in.

## 1.32.2 Release
- Release Date: June 26, 2020
- Server Versions Supported: Server v5.19+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.19 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.9 has ended and upgrading to server ESR v5.19 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app. See [this blog post](https://mattermost.com/blog/support-for-esr-5-9-has-ended/) for more details.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed an issue where some users on the v1.32.0 or v1.32.1 mobile apps authenticating with GitLab or Office365 Single Sign-On (SSO) to a Mattermost server using a subpath were unable to login to the app. Some users authenticating to Mattermost using SAML SSO with two-factor authentication or authenticating to Mattermost with an SSO provider that utilizes query strings as part of the authentication URLs were also impacted.
 - Fixed an issue where opening the app was causing an "Unexpected Error" due to a failed migration.

## 1.32.1 Release
- Release Date: June 25, 2020
- Server Versions Supported: Server v5.19+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.19 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.9 has ended and upgrading to server ESR v5.19 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app. See [this blog post](https://mattermost.com/blog/support-for-esr-5-9-has-ended/) for more details.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed an issue where Android app cold start and channel switching were slow.

## 1.32.0 Release
- Release Date: June 16, 2020
- Server Versions Supported: Server v5.19+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.19 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.9 has ended and upgrading to server ESR v5.19 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app. See [this blog post](https://mattermost.com/blog/support-for-esr-5-9-has-ended/) for more details.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Breaking Changes
 - On mobile apps, users will not be able to see group mentions (E20 feature) in the autocomplete dropdown. Users will still receive notifications if they are part of an LDAP group. However, the group mention keyword will not be highlighted.
 - **Upcoming breaking change** Starting with mobile app v1.33.0 (to be released on July 16th), users on server versions below v5.19 may experience issues with how attachments, link previews, reactions and embed data are displayed. Updating your server to v5.19 or later is required.
 
### Highlights

#### Quick access to emoji reactions 
 - Long press on a post and add recently used reactions in a single tap.
 
#### Upgrade to React Native 0.62
 - React Native 0.62 introduces performance and stability improvements to the core app platform.

### Improvements
 - Automatic retry when id-loaded push notification fails to fetch on receipt.
 - An appropriate error message is now shown when connecting to the server on the mobile app with an invalid SSL certificate.
 - Added the ability to find users by nickname when searching using ``@``.
 - Added the ability to view first and last name in profile view.
 - Improved the search bar to have smoother animations.
 
### Bug Fixes

#### All apps
 - Fixed an issue with an infinite skeleton channel screen on app relaunch when ``ExperimentalPrimaryTeam setting`` was enabled.
 - Fixed an issue where users were scrolled to old messages when switching to a channel with unread messages.
 - Fixed an issue where a logout message for session expiration was missing.
 - Fixed an issue where the app did not properly handle server URL and SSO redirects.
 - Fixed an issue where Direct and Group Messages disappeared from the left-hand side after opening them on webapp.
 - Fixed an issue where a crash occurred instead of showing proper error on entering invalid MFA token.
 - Fixed an issue where a user could not interact with the app until in-app notifications were dismissed.
 - Fixed an issue where using emoji on an instance with the custom emoji feature disabled triggered a "Custom emoji have been disabled by the system admin" error in the server logs.
 - Fixed an issue where the replay icon was cut off on full screen video preview.

#### Android specific
 - Fixed an issue where dropdowns in the channel modal were hard to read.
 
#### Known issues
 - Signing in with supported SSO methods (OKTA, OneLogin, GitLab and Office365) may fail to redirect on iOS 12. It is recommended to use iOS 13 if any issues are encountered.

## 1.31.2 Release
- Release Date: May 27, 2020
- Server Versions Supported: Server v5.19+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.19 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.9 has ended and upgrading to server ESR v5.19 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app. See [this blog post](https://mattermost.com/blog/support-for-esr-5-9-has-ended/) for more details.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.
 
Mattermost Mobile App v1.31.2 contains a high level security fix. [Upgrading](/upgrade/upgrading-mattermost-server.html) is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
 
### Bug Fixes
 - Fixed an issue where file uploads failed due to a time out when the [Antivirus plugin](https://github.com/mattermost/mattermost-plugin-antivirus) was enabled.

## 1.31.1 Release
- Release Date: May 22, 2020
- Server Versions Supported: Server v5.19+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.19 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.9 has ended and upgrading to server ESR v5.19 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app. See [this blog post](https://mattermost.com/blog/support-for-esr-5-9-has-ended/) for more details.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.
 
### Bug Fixes
 - Fixed a crash issue on Android when preloading images.

## 1.31.0 Release
- Release Date: May 16, 2020
- Server Versions Supported: Server v5.19+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - **Upgrade to server version v5.19 or later is required.** Support for server [Extended Support Release](/upgrade/extended-support-release.html) (ESR) 5.9 has ended and upgrading to server ESR v5.19 or later is required. As we innovate and offer newer versions of our mobile apps, we maintain backwards compatibility only with supported server versions. Users who upgrade to the newest mobile apps while being connected to an unsupported server version can be exposed to compatibility issues, which can cause crashes or severe bugs that break core functionality of the app. See [this blog post](https://mattermost.com/blog/support-for-esr-5-9-has-ended/) for more details.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Improvements
 - Improved network reliability and channel switching time for unread channels by fetching new posts as soon as the app reconnects.
 
### Bug Fixes

#### All apps
 - Fixed an issue where slash commands with long descriptions had their description text truncated in the slash command autocomplete.
 - Fixed an issue where users could not swipe up to dismiss in-app push notifications.
 - Fixed an issue where the username that created the webhook was shown on webhook posts instead of the name of the bot.
 - Fixed an issue where posts on the same thread appeared to be from different threads since the "...commented on [Thread Title]" was shown on all posts in the thread.
 - Fixed an issue where the system message for "Edit Channel Purpose" rendered markdown.

#### iOS specific
 - Fixed an issue where code block numbering was obstructed by the iPhone's notch.
 - Fixed an issue where the search text box was partially obstructed in landscape mode.
 - Fixed an issue where using `Share...` option to post highlighted text to the app threw an error.
 - Fixed an issue where the "back" button color was incorrect when transitioning from Thread screen to Channel screen.
 - Fixed an issue where the keyboard flashed a darker color when opening Keywords from **Settings > Notifications > Mentions and replies**.

#### Android specific
 - Fixed an issue where the keyboard did not close after editing a message.

## 1.30.1 Release
- Release Date: April 24, 2020
- Server Versions Supported: Server v5.19+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.
 
### Bug Fixes

#### All apps
 - Fixed an issue with repeated forced logouts.
 - Fixed an issue where channels appeared as read-only when opening the app.
 - Fixed an issue where users were unable to log in if ``ExperimentalStrictCSRFEnforcement`` setting was enabled.
    - A clean install may be required for the fix to take effect by uninstalling v1.30.0 (Build 285) and then installing v1.30.1 (Build 287).
 - Fixed an issue where a "No internet connection" error occurred when deleting documents and data.

#### iOS specific
 - Fixed an issue where Mattermost app crashed when Enterprise mobility management (EMM) was enabled.

#### Android specific
 - Fixed an issue where using backspace out of a conversation thread or a channel caused a forced logout.
 - Fixed an issue where a video upload attempt failed with an error.

## 1.30.0 Release
- Release Date: April 16, 2020
- Server Versions Supported: Server v5.19+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.
 
Mattermost Mobile App v1.30.0 contains a high level security fix. [Upgrading](/upgrade/upgrading-mattermost-server.html) is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
 
**Note:** v5.9.0 as our Extended Support Release (ESR) is coming to the end of its lifecycle and upgrading to 5.19.0 ESR or a later version is highly recommended. v5.19.0 will continue to be our current ESR until October 15, 2020. [Learn more in our forum post](https://forum.mattermost.com/t/upcoming-extended-support-release-updates/8526>).

**Note:** [The Channel Moderation Settings feature](/manage/team-channel-members.html#channel-moderation-e20) released in v5.22.0 is supported on mobile app versions v1.30 and later. In earlier versions of the mobile app, users who attempt to post or react to posts without proper permissions will see an error.
 
### Improvements
 - Significantly improved Android performance, including how quickly posts in the center screen are displayed.
 - Added support for different interactive message button styles on mobile.
 - Enter key on hardware Android keyboard now posts a message.
 - The statuses of those users that are in the Direct Message list are now fetched when opening the app and on login.
 - Added "Unarchive Channel" option to the channel info screen.
 
### Bug Fixes

#### All apps
 - Fixed an issue where the modal popped down when attempting to scroll down to see if there are more emoji.
 - Fixed a few crash issues.
 - Fixed an issue where the navigation bar tucked under status bar when using photo or camera post icons in landscape.
 - Removed mark as unread option from post menus for archived channels.
 - Fixed an issue where the "Refreshing message failed" error was shown when starting a Direct Message with a new user without a verified email.
 - Fixed an issue where Markdown tables was rendering in full in the center channel on larger screen sizes.
 - Made the name displayed consistent with teammate display name setting.
 - Fixed some selected emojis in autocomplete from rendering properly when posted.

#### iOS specific
 - Fixed an issue on iOS where the navigation bar tucked under status bar when using photo or camera post icons in landscape.
 - Fixed an issue on iOS where Automatic Replies custom message text box was obstructed by the iPhone's notch.
 - Fixed an issue on iOS where double dashes in mobile inside a code block got converted to emdash.

#### Android specific
 - Fixed an issue on Android where downloading a file or video was not reporting progress.
 - Fixed an issue on Android that was preventing to share content through the share extension.

## 1.29.0 Release
- Release Date: March 16, 2020
- Server Versions Supported: Server v5.9+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

**Note:** The persisted sidebar on Android tablets was removed in order to significantly improve the mobile app performance.

**Note:** An issue was fixed where a user's status was set as online when replying to a message from a push notification. This fix only works in combination with server v5.20.0+.
 
### Improvements
 - Significantly improved how quickly channels load when you open the app and when you switch between them.
 - Set all requests timeouts to a maximum of five seconds to improve reliability on bad networks.
 - Changed "Copy Permalink" to "Copy Link" for readability.
 
### Bug Fixes
 - Fixed an issue where downloaded files on Android had the words `download successful` appended to their filenames, preventing the file from being opened until it was renamed in the file manager.
 - Fixed a silent crash on Android when receiving a push notification.
 - Fixed an issue on Android where users could not swipe to close sidebar unless the gesture was initiated outside of the sidebar.
 - Fixed an issue where channels drawers were partially shown with orientation change on iOS RN61.
 - Fixed an issue on iOS where the message box obstructed the bottom part of the message when opened from the notification banner.
 - Fixed an issue where switching teams showed the center channel from the old team until the new team's channel data got loaded.
 - Fixed an issue where users could not post messages after returning from an archived channel.
 - Fixed an issue where user experienced infinite scrolling when viewing all public joinable/archived channels.
 - Fixed an issue where archived channels membership was lost on the client.
 - Fixed an issue on iOS where the channel intro scrolled past the top of the channel.
 - Fixed an issue on Android where inline custom emojis did not display in portrait mode.
 - Fixed an issue where markdown tables did not display all rows in a post when it had multiple heights.
 - Fixed an issue where deleting documents and data caused a flash of the background when the app reloaded.
 - Fixed an issue where tall and thin image attachments got pushed to the left instead of appearing centered.
 
### Known Issues
 - Some gender neutral emojis don't render as jumbo emojis.

## 1.28.0 Release
- Release Date: February 16, 2020
- Server Versions Supported: Server v5.9+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.
 
### Highlights

#### UI/UX Improvements to the Post Draft Area
 - Links added to facilitate easier access to common functions:
   - finding channel members for @mentioning;
   - finding and referencing slash commands;
   - attaching photos and videos;
   - accessing the camera

#### Deep Linking
 - Links to posts in email notifications now launch to a browser landing page with option to open in the Mobile app.

### Improvements
 - Removed markdown rendering from Channel Purpose in channel info screen.
 - Improved channel info transition so that it opens up as a modal rather than as a drawer from the right.
 - Clicking on the time in the iOS status bar now scrolls up the center channel.
 - Improved the sliding behaviour of the left-hand sidebar on iOS.
 - Added more responsiveness to markdown tables.
 - User's own username with a suffix 'you' is now shown in the username autocomplete.
 - Improved sorting of emojis in the emoji picker so that thumbsup is sorted first, then thumbsdown, and then custom emoji.

### Bug Fixes
 - Fixed an issue on Android where the app displayed an incorrect timestamp when the experimental Timezone setting was disabled.
 - Fixed an issue where combined system messages with many users listed hid posts above them.
 - Fixed an issue on iOS where the app crashed when pasting a GIF via the keyboard.
 - Fixed an issue where explicit links to teams and channels on the same server currently logged in to didn't switch to that team and channel.
 - Fixed an issue where the keyboard glitched when returning to the main channel view after viewing a code block in the right-hand side.
 - Fixed an issue with default boolean values in interactive dialogs.
 
### Known Issues
 - Markdown tables are missing a header colour.

## 1.27.1 Release
- Release Date: January 21, 2020
- Server Versions Supported: Server v5.9+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed an issue where all previously auto-closed Direct Message channels were listed in the channel sidebar.
 - Fixed a regression affecting webapp and mobile apps where some users were experiencing client-side performance issues. This was mainly affecting users with more than 100 channels listed in the channel sidebar and with channels sorted alphabetically.

## 1.27.0 Release
- Release Date: January 16, 2020
- Server Versions Supported: Server v5.9+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed an issue where flaky networks caused users to miss messages when at the top of the channel.
 - Fixed an issue where uploading image attachments in the mobile app was not working in some cases.
 - Fixed an issue where joining a user's first team from the mobile apps failed.
 - Fixed an issue where an unexpected `More New Messages Above` line appeared when marking a first post as unread in a Direct Message or Group Message channel.
 - Fixed an issue where disagreeing with custom Terms of Service gives users a glimpse of the app.
 - Fixed an issue on Android where the Back button did not dismiss the modal before dismissing the sidebar.
 - Fixed an issue where a message draft was lost after attempting to post an invalid slash command.
 - Fixed an issue where timestamps on 12-hour format had a leading zero.
 - Fixed an issue where the display name of a post was truncated even when there was enough space to render it on landscape.
 - Fixed an issue where the post input field icon was mis-aligned.
 - Fixed an issue where system message mentions were not at 100% opacity compared to non-system messages.
 
### Known Issues
 - Text box obstructs bottom part of messages in Direct Message channels when opened from a notification banner. [MM-21276](https://mattermost.atlassian.net/browse/MM-21276)

## 1.26.2 Release
- Release Date: January 7, 2020
- Server Versions Supported: Server v5.9+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed an issue on iOS where the mobile app was not usable if ``inAppPincode`` was enabled.

## 1.26.1 Release
- Release Date: December 20, 2019
- Server Versions Supported: Server v5.9+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed a crash issue on Android and iOS on server versions prior to the v5.9.0 Extended Support Release (ESR).
 - Fixed a crash when connecting the WebSocket to a server with Cert Based Auth (CBA) enabled.

## 1.26.0 Release
- Release Date: December 16, 2019
- Server Versions Supported: Server v5.9+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.
 
Mattermost Mobile App v1.26.0 contains low to medium level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Highlights

#### Improved Styling for File, Image and Video Attachments, Including In-line Image Thumbnails

#### Mark as Unread
 - With server v5.18 and above, users can stay on top of important messages with a new feature that allows marking posts as unread. After doing so, users will automatically land on the unread post the next time they click on the relevant channel.

#### Push Notification Message Contents Fetched from the Server on Receipt (E20)
 - Allows push notifications to be delivered showing the full message contents that are fetched from the server once the notification is delivered to the device. This means that Apple Push Notification Service (APNS) or Google Firebase Cloud Messaging (FCM) cannot read the message contents since only a unique message ID is sent in the notification payload. 

#### Upgraded RN to v0.61

### Improvements
- Added support for pasting other file types such as videos, PDFs and documents.
- Added the option to convert public channels to private in the channel info screen.
- Added support for reading the channel drawer button with voice-over.
- Made usernames in system messages tappable.
- Added an autocomplete to edit post screen.
- Added a count for pinned posts icon.
- Updated the channel name length character limit to 64 to match server.
- Added an expand button to truncated markdown tables to improve discoverability of opening them in full screen.
- Added an error message when trying to share too long text from share extension.
- Improved behaviour where posts from different authors in the same thread appeared to be from different threads if separated by new message line.
- Added support for native emojis in the emoji picker and autocomplete.
- Removed reactions and file attachments from the long post view.
- Large number of emoji reactions now wrap instead of introducing horizontal scroll.
- Added support for a generic error message in interactive dialog responses.
- Added the ability to disable attachment buttons and fields.

### Bug Fixes
- Fixed an issue on Android where the app slowed down when opening a channel with large number of animated emoji.
- Fixed an issue where the app crashed when pasting a large file to the text box from the clipboard.
- Fixed an issue where the app crashed when previewing large GIF files.
- Fixed an issue where the app crashed when using the emoji category selector.
- Fixed an issue where the app was not able to play YouTube videos.
- Fixed an issue where images/videos could not be saved.
- Fixed an issue where channels archived via the command line interface were still visible on the left-hand side and accessible on mobile apps.
- Fixed an issue where the thread header in landscape view was wider than the main channel view header.
- Fixed an issue where sidebar separator line was misaligned between Teams and Channel view.
- Fixed an issue on iOS where the channel spinner appeared black on a dark theme.
- Fixed an issue where an asterisk appeared on the "Nickname" and "Position" fields in Edit Profile screen even though nickname is not handled through the login provider.
- Fixed an issue where the filtered list for emojis opened above the edit box and behind the channel header when adding an emoji to channel header using ``:emoji:``.

## 1.25.1 Release
- Release Date: November 22, 2019
- Server Versions Supported: Server v5.9+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed a crash issue on iOS when SSO cookies did not contain an expiration date during login.
 - Fixed a crash issue on Android caused by notification channels being unavailable in Android 7.
 - Fixed an issue on Android where Enterprise Mobility Management (EMM) blur app screen did not work.
 - Fixed an issue where changing team/channel when sharing several files closed the share dialog.

## 1.25.0 Release
- Release Date: November 16, 2019
- Server Versions Supported: Server v5.9+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed an issue where Mattermost monokai theme no longer worked properly on mobile apps.
 - Fixed an issue on Android where the notification badge count didn't update when using multiple channels.
 - Fixed an issue on Android where test notifications did not work properly.
 - Fixed an issue where "In-app" notifications caused the app badge count to get out of sync.
 - Fixed an issue on Android where email notification setting displayed was not updated when the setting was changed.
 - Fixed an issue where Favorite channels list didn't update if the app was running in the background.
 - Fixed an issue where the timezone setting did not update when changing it back to set automatically.
 - Fixed an issue on iOS where clicking on a hashtag from "recent mentions" (or flagged posts) returned the user to the channel instead of displaying hashtag search results.
 - Fixed an issue where tapping on a hashtag engaged a keyboard for a moment before displaying search results.
 - Fixed an issue where posts of the same thread appeared to be from different threads if separated by a new message line.
 - Fixed styling issues on iOS for Name, Purpose and Header information on the channel info screen.
 - Fixed styling issues with bot posts timestamps in search results and pinned posts.
 - Fixed styling issues on single sign-on screen in landscape view on iOS iPhone X and later.
 - Fixed styling issues on iOS for the Helper text on Settings screens.
 - Fixed an issue where the thread view header theme was inconsistent during transition back to main channel view.
 - Fixed an issue on iOS where the navigation bar tucked under the phone's status bar when switching orientation.
 - Fixed an issue on iOS where the keyboard flashed darker when Automatic Replies had been previously enabled.
 - Fixed an issue on Android where uploading pictures from storage or camera required unwanted permissions.
 - Fixed an issue where ``mobile.message_length.message`` did not match webapp's ``create_post.error_message``.
 
### Known Issues
 - App slows down when opening a channel with large number of animated emoji. [MM-15792](https://mattermost.atlassian.net/browse/MM-15792)

## 1.24.0 Release
- Release Date: October 16, 2019
- Server Versions Supported: Server v5.9+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Highlights

#### Sidebar UI/UX improvements
 - Improved usability and styling of the channel drawer.

### Improvements
 - Added the ability to paste images on input text box.
 - Added copy and paste protection managed configuration support for Android.
 - Added a confirmation dialog when posting a message with `@channel` and `@all`.
 - Added support for safe area in landscape view on iOS.
 - Changed recent date separators to read Today/Yesterday.
 - Added an autocomplete to the edit channel screen.
 - Emoji picker search now ignores the leading colon.
 - Added support for emoji not requiring a whitespace to render.
 - Added support for footer and footer_icon in message attachments.
 - Added a password type for interactive dialogs.
 - Added support for introductory markdown paragraph in interactive dialogs.
 - Added support for boolean elements in interactive dialogs.
 - Improved the permissions prompt if Mattermost doesn't have permission to the photo library.

### Bug Fixes
 - Fixed an issue where the notification badge could get out of sync when reading messages in another client.
 - Fixed an issue where the notification badge number did not reset when opening a push notification.
 - Fixed an issue where SafeArea insets were not working properly on new iPhone 11 models.
 - Fixed an issue where long press on a system message in an archived channel locked up the app.
 - Fixed an issue where tapping on a hashtag while replying to search results didn't open search correctly.
 - Fixed an issue where the channel list panel was missing for a user when they were added to a new team by another user.
 - Fixed an issue where once in a thread, pressing a channel link appeared to do nothing.
 - Fixed an issue where file previews could scroll to the left until all files were out of view.
 - Fixed an issue on iOS where user was unable to select an emoji from two rows on the bottom of the emoji picker.
 - Fixed an issue where duplicate pinned posts displayed after editing pinned post from Pinned Posts screen.
 - Fixed an issue where the reply arrow overlapped a posts's timestamp in some cases.
 - Fixed an issue where post textbox did not clear after using a slash command.
 - Fixed an issue where users were are not immediately removed from the mention auto-complete when those users were deactivated.
 - Fixed an issue where returning to a channel from a thread view could trigger a long-press menu that couldn't be dismissed.
 - Fixed an issue with a missing "(you)" suffix in the channel header of a self Direct Message.
 - Fixed an issue where the Connected banner got stuck open after the WebSocket was connected.
 - Fixed an issue where the text input area in Android Share extension did not use available space.
 - Fixed an issue where Windows dark theme was not consistent when viewing an archived channel.
 - Fixed an issue where interactive dialogs rendered out of safe area view on landscape orientation.
 - Fixed an issue where a themed "Delete Documents & Data" action flashed a white screen.

### Known Issues
 - App slows down when opening a channel with large number of animated emoji. [MM-15792](https://mattermost.atlassian.net/browse/MM-15792)

## 1.23.1 Release
- Release Date: September 27, 2019
- Server Versions Supported: Server v5.9+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed issues causing the app to crash on some devices.

## 1.23.0 Release
- Release Date: September 16, 2019
- Server Versions Supported: Server v5.9+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed an issue where some Giphy actions were not working in ephemeral posts on mobile.
 - Fixed an issue where users were unable to create new channels when "Combine all channel types" was selected.
 - Fixed an issue on Android EMM where a crash occurred when tapping **Go to Settings**.
 - Fixed an issue on iOS where the in-app "Date" localization persisted after server and user changed.
 - Fixed an issue where the download step was showing when previewing a video right after posting it. 
 - Fixed an issue on Android where cancelling a video download twice in a row showed an error.
 - Fixed an issue where file attachment thumbnail/preview could fail to load and not be able to be reloaded.
 - Fixed an issue on Android where **Channel > Add Members > ADD** text changed to black.
 - Fixed an issue on iOS where the **Cancel** label text didn't fit in one line in German language.
 - Fixed an issue where longer than allowed reply posts kept showing a warning with every backspace.
 - Fixed an issue where there was a delay in search box and emoji content width change when switching to/from portrait/landscape view.
 - Fixed an issue where deactivated users did not appear in the "Jump to..." screen.
 - Fixed an issue where "@undefined has joined the channel" was shown instead of "Someone has joined the channel" when a user joined a channel that another user was viewing.
 - Fixed an issue on Android where the reply arrow was cut off in search results.
 - Fixed an issue where changing display theme from webapp didn't work properly on mobile.
 - Fixed an issue on iOS where a bot account icon style was broken.
 - Fixed an issue with an incorrect UI text for location of touch ID setting.
 
### Known Issues
  - App slows down when opening a channel with large number of animated emoji. [MM-15792](https://mattermost.atlassian.net/browse/MM-15792)
  - When users are deactivated, they are not immediately removed from the mention auto-complete. [MM-17953](https://mattermost.atlassian.net/browse/MM-17953)

## 1.22.1 Release
- Release Date: August 23, 2019
- Server Versions Supported: Server v5.9+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed an issue where the apps crashed when setting the language to Chinese Traditional.
 - Fixed an issue on Android where push notification receipt delivery failed due to invalid server URL.
 - Fixed an issue where the apps crashed when launched via a notification.
 - Fixed an issue where posts made while the app was closed did not appear until refresh.

## 1.22.0 Release
- Release Date: August 16, 2019
- Server Versions Supported: Server v5.9+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Highlights

#### Support for iOS13 and Android Q
 - Added support for iOS13 and Android Q which are to be released later this year.

### Improvements
 - Added support for Interactive Dialog with no elements.
 - Added a setting for tablets to enable or disable fixed sidebar.
 - Changed "about" section references to use the site name when it is configured in **System Console > Custom Branding > Site Name**.
 - Added support for plus-sign and period/dot in custom URL schemes.
 - Added "Edit profile" button to right-hand side menu and to users' own profile pop-over.
 - Message draft is now saved when closing the app.
 - Removing a link preview on webapp now also removes it on the mobile app.
 - Added ability to select and copy channel header text and purpose.

### Bug Fixes
 - Fixed a few mobile app crash / fatal error issues.
 - Fixed an issue where timestamps were off on Android.
 - Fixed an issue where contents of ephemeral posts from /giphy were not being displayed on mobile.
 - Fixed an issue where team/channel page dots at the bottom of left-hand side overlapped with the last Direct Message channel.
 - Fixed an issue where network reconnection incorrectly showed refreshing messages failed.
 - Fixed an issue with the channel sidebar theme colors not being respected on iPhone X.
 - Fixed an issue where "Message failed to send" had incorrect app badge behaviour.
 - Fixed an issue where a white screen was briefly shown after pressing "Send Message" when viewing a user's profile.
 - Fixed an issue on Android where using "Https" instead of "https" in the url of an image didn't show the preview.
 - Fixed an issue where the client ``setCSRFFromCookie`` did not look for subpaths when accessing cookies.
 - Fixed an issue where archived teams reappeared in selector.
 - Fixed an issue where users' profile picture and name did not get updated after websocket disconnect.
 
### Known Issues
  - App slows down when opening a channel with large number of animated emoji. [MM-15792](https://mattermost.atlassian.net/browse/MM-15792)
  - Some Giphy actions do not work in ephemeral posts. [MM-17842](https://mattermost.atlassian.net/browse/MM-17842)

## 1.21.2 Release
- Release Date: August 1, 2019
- Server Versions Supported: Server v5.9+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed an issue where the mobile apps logged out without a session expiry notification.

## 1.21.1 Release
- Release Date: July 22, 2019
- Server Versions Supported: Server v5.9+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed an issue on Android where logging in using SSO failed when the Mattermost server was running on a subpath.

## 1.21.0 Release
- Release Date: July 16, 2019
- Server Versions Supported: Server v5.9+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed a few mobile app crash / fatal error issues.
 - Fixed an issue where having the sidebar open at all times on tablets did not work for split view.
 - Fixed an issue where new messages were often hidden behind a keyboard or text field.
 - Fixed an issue on Android where channel sorting didn't match the web app.
 - Fixed an issue where sharing a GIF via keyboard resulted in an error screen.
 - Fixed an issue where long-press menu could not be dragged up when rotating the device to landscape view while the menu was open.
 - Fixed an issue on Android where push notification settings were only saved after closing the settings page.
 - Fixed an issue where users on View Members list had an icon that appeared to be selectable but was not.
 - Fixed an issue where "Jump To" showed archived channels the user did not belong to instead of the ones the user was a member of.
 - Fixed an issue where changing the timezone setting manually to "Set automatically" did not work on the mobile app.
 - Fixed an issue where setting a position field for AD/LDAP sync or SAML in the System Console did not block the user from changing it in account settings.
 - Fixed an issue where **Channel Info > Manage/View Members** screen didn't load channel users.
 - Fixed an issue where enabling large fonts on iOS caused the left-hand side text to be cut off.
 - Fixed an issue on Android where users could not reply to a push notification if the mention was in a thread message.

### Known Issues
  - (Android) On subpath server, logging in using GitLab or OneLogin fails to display Mattermost. [MM-16829](https://mattermost.atlassian.net/browse/MM-16829)
  - Buttons inside ephemeral posts are not clickable / functional on the mobile app. [MM-15084](https://mattermost.atlassian.net/browse/MM-15084)
  - Android apps slow down when opening a channel with large number of animated emoji. [MM-15792](https://mattermost.atlassian.net/browse/MM-15792)

## 1.20.2 Release
- Release Date: July 10, 2019
- Server Versions Supported: Server v4.10+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Mobile App v1.13+ is required for Mattermost Server v5.4+.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.
 
### Bug Fixes
 - Fixed an issue where Moto G7 devices were detected as tablets and showed a fixed width sidebar.
 - Fixed an issue where having the sidebar open at all times on tablets did not work on split view.

## 1.20.1 Release
- Release Date: June 21, 2019
- Server Versions Supported: Server v4.10+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Mobile App v1.13+ is required for Mattermost Server v5.4+.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes
 - Fixed an issue where some Android devices were crashing.
 - Fixed an issue where messages were missing after reconnecting the network.

## 1.20.0 Release
- Release Date: June 16, 2019
- Server Versions Supported: Server v4.10+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Mobile App v1.13+ is required for Mattermost Server v5.4+.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Highlights

#### Tablet Improvements
 - Channel sidebar now remains open at a fixed width on tablet devices.
 
#### iOS Keyboard Dismissal
 - If the keyboard is open, swiping down past it now closes it.
 
#### Profile Telemetry for Android Beta Builds
 - To improve Android app performance, we are collecting trace events and device information, collectively known as metrics, to identify slow performing key areas. Those metrics will be sent only from users using Android app beta build starting in version v1.20, who are logged in to servers that allow sending [diagnostic information](/configure/configuration-settings.html#enable-diagnostics-and-error-reporting).

### Improvements
 - Increased the double tap delay for post action buttons.
 - Implemented assets for Adaptive icons.
 - Users are now brought to the bottom of the channel when posting a message.
 - Users can now execute actions while the keyboard is open.
 - Added support on iOS for IPv6 on LTE networks.
 - Added support for LDAP Group constrained feature with v5.12 servers.

### Bug Fixes
 - Fixed an issue where a post wasn't immediately removed when deleting another user's post.
 - Fixed an issue where the cursor jumped back when typing after auto-completing a slash command.
 - Fixed an issue where the iOS app didn’t properly restore its connection after disconnect.
 - Fixed an issue where the long press menu persisted after returning from a thread.
 - Fixed an issue on Android where the "Write to [channel name]" was cut off for group messages with several users.
 - Fixed an issue where users were not able to flag or unflag posts in a read-only channel.
 - Fixed an issue where the progress indicator was negative while downloading a video.
 - Fixed an issue where the edit post modal didn’t have an autocorrect.
 - Fixed an issue where the 'I forgot my password' option was available on the mobile client even with Email Authentication disabled on the server.
 - Fixed an issue with large separation between placeholders on iPad when a channel was loading.
 - Fixed an issue where "Show More" was not removed after the post was edited to a single line.
 
### Known Issues
  - Buttons inside ephemeral posts are not clickable / functional on the mobile app. [MM-15084](https://mattermost.atlassian.net/browse/MM-15084)
  - App slows down when opening a channel with large number of animated emoji. [MM-15792](https://mattermost.atlassian.net/browse/MM-15792)
 
## 1.19.0 Release
- Release Date: May 16, 2019
- Server Versions Supported: Server v4.10+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Mobile App v1.13+ is required for Mattermost Server v5.4+.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.
 
### Bug Fixes
 - Fixed an issue where Android managed config was lost on the thread view.
 - Fixed an issue where contents of ephemeral posts did not display on the mobile app.
 - Fixed a few mobile app crash / fatal error issues.
 - Fixed an issue with an expanding animation when tapping on Jump to Channel in the channel list.
 - Fixed an issue on iOS where animated custom emoji weren't animated.
 - Fixed an issue on iOS where users were unable to create channel name of two characters.
 - Fixed an issue on iOS where emoji appeared too close, with uneven spacing, and too small in the info modal.
 - Added an error handler when sharing text that was over server's maximum post size with the iOS Share Extension.
 - Fixed an issue where users could upload a GIF as a profile image.
 
### Known Issues
 - Buttons inside ephemeral posts are not clickable / functional on the mobile app.

## 1.18.1 Release
- Release Date: April 18, 2019
- Server Versions Supported: Server v4.10+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Mobile App v1.13+ is required for Mattermost Server v5.4+.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.

### Bug Fixes 
 - Fixed a crash issue caused by a malformed post textbox localize string.
 - Fixed an issue where iOS crashed when trying to log in using SSO and the SSO provider set a cookie without an expiration date.

## 1.18.0 Release
- Release Date: April 16, 2019
- Server Versions Supported: Server v4.10+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Mobile App v1.13+ is required for Mattermost Server v5.4+.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.
 - ``Bot`` tags were added for bot accounts feature in server v5.10 and mobile v1.18, meaning that mobile v1.17 and earlier don't support the tags.
 
### Highlights
 - Added support for Office365 single sign-on (SSO).
 - Added support for Integrated Windows Authentication (IWA).

### Improvements
 - Added the ability for channel links to open inside the app.
 - Added ability for emojis and hyperlinks to render in the message attachment title.
 - Added Chinese support for words that trigger mentions.
 - Added a setting to the system console to change the minimum length of hashtags.
 - Added a reply option to long press context menu.

### Bug Fixes
 - Fixed an issue where blank spaces broke markdown tables.
 - Fixed an issue where deactivated users appeared on "Add Members" modal but not on the search results.
 - Fixed an issue on Android where extra text in the search box appeared after using the autocomplete drop-down.
 - Fixed an issue with multiple text entries when typing with Shift+Letter on Android.
 - Fixed an issue where push notifications badges did not always clear when read on another device.
 - Fixed an issue where opening a single or group notification did not take the user into the channel where the notification came from.
 - Fixed an issue where timezone did not automatically update on Android when travelling to another timezone.
 - Fixed an issue where the user mention autocomplete drop-down was case sensitive.
 - Fixed an issue where system administrators were able to see the full long press menu when long pressing a system message.
 - Fixed an issue where users were not able to unflag posts from "Flagged Posts" when opened from a read-only channel.
 - Fixed an issue where users were unable to create channel names of two byte characters.
 
### Known Issues
 - Content for ephemeral messages is not displayed on Mattermost Mobile Apps.

## 1.17.0 Release
- Release Date: March 20, 2019
- Server Versions Supported: Server v4.10+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - If **DisableLegacyMfa** setting in ``config.json`` is set to ``true`` and [multi-factor authentication](/onboard/multi-factor-authentication.html) is enabled, ensure your users have upgraded to mobile app version 1.17 or later. See [Important Upgrade Notes](/upgrade/important-upgrade-notes.html) for more details.
 - If you are using an EMM provider via AppConfig, make sure to add two new settings, `useVPN` and `timeoutVPN`, to your AppConfig file. The settings were added for EMM connections using VPN on-demand - one to indicate if every request should wait for the VPN connection to be established, and another to set the timeout in seconds. See docs for more details on [setting AppConfig values](/deploy/mobile-appconfig.html#mattermost-appconfig-values) for VPN support.
 - Mobile App v1.13+ is required for Mattermost Server v5.4+.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 - iPhone 5s devices and later with iOS 11+ is required.
 
### Highlights
 - iOS Share Extension now supports large file sizes and improved performance

### Bug Fixes
 - Fixed support for EMM connections using VPN on-demand. See docs for more details on [setting AppConfig values](/deploy/mobile-appconfig.html#mattermost-appconfig-values) for VPN support.
 - Fixed several Android app crash / fatal error issues.
 - Fixed an issue on Android where the app crashed intermittently when selecting a link.
 - Fixed an issue where email notifications setting was out of sync with the webapp until the setting was edited.
 - Fixed an issue where notification badges were not cleared from other clients when clicking on a push notification after opening the mobile app.
 - Fixed an issue where the app did not show local notification when session expired.
 - Fixed an issue where the profile picture for webhooks was showing the hook owner picture.
 - Fixed an issue where some emoji were not rendered as jumbo.
 - Fixed an issue where jumbo emoji posted as a reply sometimes appeared with large space beneath.
 - Fixed an issue where the "No Internet Connection" banner did not always display when internet connectivity was lost.
 - Fixed an issue where the "No Internet Connection" banner did not always disappear when connection was re-estabilished.
 - Fixed an issue where opening channels with unreads had loading indicator placed above unread messages line.

## 1.16.1 Release
- Release Date: February 21, 2019
- Server Versions Supported: Server v4.10+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility
 - Mobile App v1.13+ is required for Mattermost Server v5.4+.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).

### Bug Fixes
 - Fixed an issue where link previews and reactions weren't displayed when post metadata was disabled.
 - Fixed an issue on Android where the app crashed when sharing multiple files.
 
## 1.16.0 Release
- Release Date: February 16, 2019
- Server Versions Supported: Server v4.10+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility

 - Mobile App v1.13+ is required for Mattermost Server v5.4+.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).

### Improvements
 - Added the ability to remove own profile picture.
 - Changed "X" to "Cancel" on Edit Profile page.
 - Added support for relative permalinks.

### Bug Fixes
 - Fixed an issue where the iOS app did not wait until the on-demand VPN connection was established. (EMM Providers)
 - Fixed an issue with a white screen caused by missing Russian translations.
 - Fixed an issue where the iOS badge notification did not always clear.
 - Fixed an issue where the thread view displayed a new message indicator.
 - Fixed an issue where quick multiple taps on the file icon opened multiple file previews.
 - Fixed an issue where the settings page did not show an option to join other teams.
 - Fixed an issue where image previews didn't work after using Delete File Cache.
 - Fixed an issue on Android where the notification trigger word modal title was "Send email notifications" instead of "Keywords".
 - Fixed an issue where the Webhook icon was misaligned and bottom edges were cut off.
 - Fixed an issue on Android where the user was not asked to authenticate to the app first when trying to share a photo, resulting in a white "Share modal" screen with a never-ending loading indicator.
 - Fixed an issue on iOS where push notifications were not preserved when opening the app via the Mattermost icon.

## 1.15.2 Release
- Release Date: January 16, 2019
- Server Versions Supported: Server v4.10+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility

 - Mobile App v1.13+ is required for Mattermost Server v5.4+.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).

### Bug Fixes

 - Fixed an issue where the status changes for other users did not always stay current in the mobile app.
 - Fixed an issue where a post did not fail properly when the user attempted to send the post while there was no network access.
 - Fixed an issue where date separators did not update when changing timezones.
 - Fixed an issue where the Favorites section did not clear from a users's channel drawer.
 - Removed an extra divider below "Edit Channel" of Direct Message Channel Info.
 - Fixed an issue where a user was not returned to previously viewed channel after viewing and then closing an archived channel.
 - Fixed an issue where a quick double tap on switch of Channel Info created and extra on/off state.
 - Fixed an issue where iOS long press menu didn't have rounded corners.

## 1.15.1 Release
- Release Date: December 28, 2018
- Server Versions Supported: Server v4.10+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility

 - Mobile App v1.13+ is required for Mattermost Server v5.4+.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).
 
### Bug Fixes
 - Fixed an issue preventing some users from logging in using OKTA.

## 1.15.0 Release
- Release Date: December 16, 2018
- Server Versions Supported: Server v4.10+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

### Compatibility

 - Mobile App v1.13+ is required for Mattermost Server v5.4+.
 - Android operating system 7+ [is required by Google](https://android-developers.googleblog.com/2017/12/improving-app-security-and-performance.html).

### Highlights
 - Added mention and reply mention highlighting.
 - Added a sliding animation for the reaction list.
 - Added support for pinned posts.
 - Added support for jumbo emojis.
 - Added support for interactive dialogs.
 - Improved UI for the long press menu and emoji reaction viewer.

### Improvements
 - Added the ability to include custom headers with requests for custom builds.
 - Push Notifications that are grouped by channels are cleared once the channel is read.
- Improved auto-reconnect when unable to reach the server.
 - Added support for changing the mobile client status to offline when the app loses connection.
 - Added 'View Members' button to archived channels.
 - Added support on iOS for keeping the postlist in place without scrolling when new content is available.

### Bug Fixes
 - Fixed an issue where clicking on a file did not show downloading progress.
 - Fixed an issue on Android where on fresh install the share extension would not properly show available channels.
 - Fixed an issue where recently archived channels remained in in: autocomplete when they had been archived.
 - Fixed an issue where text should render when no actual custom emoji matched the named emoji pattern.
 - Fixed an issue on iOS where text got cut-off after replying to a message.
 - Fixed an issue where search modifier for channels was showing Direct Messages without usernames.
 - Fixed an issue where "Close Channel" did not work properly when viewing two archived channels in a row.
 - Fixed an issue with "Critical Error" screen when trying to upload certain file types from "+" to the left of message input box.

## 1.14.0 Release
- Release Date: November 16, 2018
- Server Versions Supported: Server v4.10+ is required, Self-Signed SSL Certificates are not supported unless the user installs the CA certificate on their device

**Compatibility Note: Mobile App v1.13+ is required for Mattermost Server v5.4+**

### Bug Fixes
- Fixed an issue where the Android app did not allow establishing a network connection with any server that used a self-signed certificate that had the CA certificate user installed on the device.
- Removed "Copy Post" option on long-press message menu for posts without text.
- Fixed an issue where the "Search Results" header was not fully scrolled to top on search "from:username".
- Fixed an issue where channel names truncated at fewer characters than necessary.
- Fixed an issue where the same uploaded photo generated a different file size.
- Fixed an issue where the "(you)" was not displayed to the right of a user's name in the channel drawer when a user opened a Direct Message channel with themself.
- Fixed an issue where a dark theme set from webapp broke mobile display.
- Fixed an issue where channel drawer transition sometimes lagged.
- Fixed an issue where sending photos to Mattermost created large files.
- Fixed an issue where the apps showed "Select a Team" screen when opened.
- Fixed an issue where at-mention, emoji, and slash command autocompletes had a double top border.
- Fixed an issue where the drawer was unable to close when showing the team list.
- Fixed an issue where team sidebar showed + sign even without more teams to join.


## 1.13.1 Release
- Release Date: October 18, 2018
- Server Versions Supported: Server v4.10+ is required, Self-Signed SSL Certificates are not supported

**Compatibility Note: Mobile App v1.13+ is required for Mattermost Server v5.4+**

### Bug Fixes
- Fixed an issue preventing some users from authenticating using OKTA

## v1.13.0 Release
- Release Date: October 16, 2018
- Server Versions Supported: Server v4.10+ is required, Self-Signed SSL Certificates are not supported

**Compatibility Note: Mobile App v1.13+ is required for Mattermost Server v5.4+**

### Highlights

#### View Emoji Reactions
- Hold down on any emoji reaction to see who reacted to the post.

#### Hashtags
- Added support for searching for hashtags in posts.

#### Dropdown menus
- Added support for dropdown menus in message attachments.

### Improvements
- Added support for iPhone XR, XS and XS Max.
- Added support for nicknames on user profile.
- On servers 5.4+, added support for searching in direct and group message channels using the "in:" modifier.
- Channel autocomplete now gets closed if multiple tildes are typed.
- Added a draft icon in sidebar and channel switcher for channels with unsent messages.
- Users are now redirected to the archived channel view (rather than to Town Square) when a channel is archived.
- When closing an archived channel, users are now returned to the previously viewed channel.

### Bug Fixes
- Refactored postlist to include Android Pie fixes and smoother scrolling.
- Fixed an issue where deactivated users were not marked as such in "Jump To" search.
- Fixed an issue where users got a permission error when trying to open a file from within the image preview screen.
- Fixed an issue where session expiry notifications were not being sent on Android.
- Fixed an issue where post attachments failed to upload.
- Fixed an issue where the "DM More..." list cut off user info.
- Fixed an issue where the user would briefly see a system message when loading a reply thread.
- Fixed an issue where the error message was incorrectly formatted if the login method was set to email/password and the user tried to log in with SAML.
- Fixed an issue on Android where the keyboard sometimes overlapped the bottom of the post textbox.
- Fixed an issue where there was no option to take video via "+" > "Take Photo or Video" on iOS.

## v1.12.0 Release
- Release Date: September 16, 2018
- Server Versions Supported: Server v4.10+ is required, Self-Signed SSL Certificates are not supported

### Highlights

#### Search Date Filters
- Search for messages before, on, or after a specified date.

### Improvements
- Added notification support for Android O and P.

### Bug Fixes
- Fixed an issue where Okta was not able to login in some deployments.
- Fixed an issue where messages in Direct Message channels did not show when clicking "Jump To".
- Fixed an issue where `Show More` on a post with a message attachment displayed a blank where content should have been.
- Prevent downloading of files when disallowed in the System Console.
- Fixed an issue where users could not click on attachment filenames to open them.
- Fixed an issue where email notification settings did not save from mobile.
- Fixed an issue where the share extension allowed users to select and attempt to share content to channels that had been archived.
- Fixed an issue where reacting to an existing emoji in an archived channel was allowed.
- Fixed an issue where archived channels sometimes remained in the drawer.
- Fixed an issue where deactivated users were not marked as such in Direct Message search.


## v1.11.0 Release
- Release Date: August 16, 2018
- Server Versions Supported: Server v4.10+ is required, Self-Signed SSL Certificates are not supported

### Highlights

#### Searching Archived Channels
- Added ability to search for archived channels. Requires Mattermost server v5.2 or later.

#### Deep Linking
- Added the ability for custom builds to open Mattermost links directly in the app rather than the default mobile browser. Learn more in our [documentation](/deploy/mobile-faq.html#how-do-i-configure-deep-linking)

### Improvements
- Added profile pop-up to combined system messages.
- Force re-entering SSO auth credentials after logout.
- Added consecutive posts by the same user.
- Added a loading indicator when user info is still loading in the left-hand side.

### Bug Fixes
- Fixed an issue where Android devices showed an incorrect timestamp.
- Fixed an issue on Android where the app did not get sent to the background when pressing the hardware back button in the channel screen.
- Fixed an issue with video playback when the filename had spaces.
- Fixed an issue where the app crashed when playing YouTube videos.
- Fixed an issue with session expiration notification.
- Fixed an issue with sharing files from Google Drive in Android Share Extension.
- Fixed an issue on Android where replying to a push notification sometimes went to the wrong channel.
- Fixed an issue where the previous server URL was present on the input textbox before changing the screen to Login.
- Fixed an issue where user menu was not translated correctly.
- Fixed an issue where some field lengths in Account Settings didn't match the desktop app.
- Fixed an issue where long URLs for embedded images in message attachments got cut off and didn't render.
- Fixed an issue where link preview images were not cropped properly.
- Fixed an issue where long usernames didn't wrap properly in the Account Settings menu.
- Fixed an issue where DMs would not open if users were using "Jump To".
- Fixed an issue where no message was displayed after removing a user from a channel with join/leave messages disabled.

## v1.10.0 Release
- Release Date: July 16, 2018
- Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported

### Highlights

#### Channel drawer performance
- Android devices will notice significant performance improvements when opening and closing the channel drawer.

#### Channel loading performance
- Improved channel loading performance as post are retrieved with every push notification

#### Announcement banner improvements
- Markdown now renders when announcement banners are expanded
- When enabled by the System Admin, users can now dismiss announcement banners until their next session

### Improvements

 - Combined consecutive messages from the same user.
 - Added experimental support for certificate-based authentication (CBA) for iOS to identify a user or a device before granting access to Mattermost. See [documentation](/onboard/certificate-based-authentication.html) to learn more.
 - Added support for the experimental automatic direct message replies feature.
 - Added support for the experimental timezone feature.
 - Changed post textbox to not be a connected component.
 - Allow connecting to mattermost instances hosted at subpaths.
 - Added support for starting YouTube videos at a given time.
 - Added support for keeping messages if slash command fails.

### Bug Fixes

 - Fixed an issue where the unread badge background was always white.
 - Fixed an issue where a username repeated in system message if user was added to a channel more than once.
 - Fixed an issue where Android Sharing from Microsoft apps failed.
 - Fixed an issue where YouTube crashed the app if link did not have a time set.
 - Fixed an issue where System Admins did not see all teams available to join on mobile.
 - Fixed an issue where users were unable to share from Files app.
 - Fixed an issue where viewing a non-existent permalink didn't show an error message.
 - Fixed an issue where jumping to a channel search did not bold unread channels.
 - Fixed an issue with being able to add own user to a Group Message channel.
 - Fixed an issue with not being able to reply from a push notification on iOS.
 - Fixed an issue where the app did not display Brazilian language.
 
## 1.9.3 Release
- Release Date: July 04, 2018
- Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported

### Bug Fixes

- Fixed multiple issues causing app crashes
- Fixed an issue on iOS devices with typing non-english characters in the post input box

## 1.9.2 Release
- Release Date: June 27, 2018
- Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported

### Bug Fixes

- Fixed an issue where attached videos did not play for the poster
- Fixed an issue where "Jump to recent messages" from the permalink view did not direct the user to the bottom of the channel
- Fixed an issue where post comments did not identify which parent post they belonged to
- Fixed multiple issues with typing non-english characters in the post input box
- Fixed multiple issues causing random app crashes
- Fixed an issue where files from the Android Files app failed to upload
- Fixed an issue where the iOS share extension crashed when switching the team or channel
- Fixed an issue where files from the Microsoft app failed to upload
- Fixed an issue on Android devices where sharing files changed the file extension of the attachment

## 1.9.1 Release
- Release Date: June 23, 2018
- Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported

### Bug Fixes
- Fixed an issue with typing lag on Android devices
- Fixed an issue causing users to be logged out after upgrading to v1.9.0
- Fixed an issue where the ``in:`` and ``from:`` modifiers were not being added to the search field

## v1.9.0 Release
- Release Date: June 16, 2018
- Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported

### Highlights

#### Improved first load time on Android
 - Significantly decreased first load time on Android devices from cold start.
 
#### iOS Files app support
- Added support for attaching files from the iOS Files app from within Mattermost.

#### Improved styling of push notification
- Improved the layout of message content, channel name and sender name in push notifications.

### Improvements

 - Combined join/leave system messages.
 - Added splash screen and channel loader improvements.
 - Removed the desktop notification duration setting.
 - Added cache team icon and set background to always be white if using a PNG file.
 - Added whitelabel for icons and splash screen.

### Bug Fixes

 - Fixed an issue where other user's display name did not render in combined system messages after joining the channel.
 - Fixed an issue where posts incorrectly had "Commented on Someone's message" above them.
 - Fixed an issue where deleting a post or its parent in permalink view left permalink view blank.
 - Fixed an issue where "User is typing" message cut was off.
 - Fixed an issue where `More New Messages Above` appeared at the top of new channel on joining.
 - Fixed an issue where a user was not directed to Town Square when leaving a channel.
 - Fixed an issue where long post were not collapsed on Android.
 - Fixed an issue where a user's name was initially shown as "someone" when opening a direct message with the user.
 - Fixed an issue where an error was received when trying to change the team or channel from the share extension.
 - Fixed an issue where switching to a newly created channel from a push notification redirected a user to Town Square.
 - Fixed an issue where a public channel made private did not disappear automatically from clients not part of the channel.

## v1.8.0 Release
- Release Date: April 27, 2018
- Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported

### Highlights

#### Image performance
- Images are now downloaded and stored locally for better performance

#### Flagged Posts and Recent Mentions
- Access all your flagged posts and recent mentions from the buttons in the sidebar

#### Muted Channels
- Added support for Muted Channels released with Mattermost server v4.9 

### Improvements
- Date separators now appear between each posts in the search view
- Deactivated users are now filtered out of the channel members lists
- Direct Messages user list is now sorted by username first
- Added the option to Direct Message yourself from your user profile screen
- Improved performance on the post list
- Improved matching and display when searching for users in the Direct Message user list

### Bug Fixes
- Fixed an issue where emoji reactions could be added from the search view but did not appear
- Fixed an issue causing the app to crash when trying to share content from a custom keyboard
- Fixed an issue where team names were being sorted based on letter case
- Fixed an issue where username would not be inserted to the post draft when using experimental configuration settings
- Fixed an issue with nested bullet lists being cut off in the user interface
- Fixed an issue where private channels were listed in the public channels section of the channel autocomplete list
- Fixed an issue where a profile images could not be updated from the app

## v1.7.1 Release
- Release Date: April 3, 2018
- Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported

### Bug Fixes
- Fixed an issue where the iOS share extension sometimes crashed the Mattermost app
- Fixed an issue preventing Markdown tables from rendering with some international characters 

## v1.7.0 Release
- Release Date: March 26, 2018
- Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported

### Highlights

#### iOS File Sharing
- Share files and images from other applications as attached files in Mattermost

#### Markdown Tables
- Tables created using markdown formatting can now be viewed in the app

#### Permalinks
- Permalinks now open in the app instead of launching a browser window 

### Improvements
- Increased the tappable area of various icons for improved usability
- Announcement banners now display in the app
- Added "+" button to add emoji reactions to a post
- Minor performance improvements for app launch time
- Text files can now be viewed in the app
- Support for email autolinking into the app

### Bugs
- Fixed an issue causing some devices to hang at the splash screen on app launch
- Fixed an issue causing some letters to be hidden in the Android search input box
- Fixed an issue causing some Direct Message channels to show date stamps below the most recent message
- Fixed an issue where users weren't able to join open teams they've never been a member of
- Fixed an issue so double tapping buttons can no longer cause UI issues
- Fixed an issue where changing the channel display name wasn't being updated in the UI appropriately
- Fixed an issue where searhing for public channels sometimes showed no results
- Fixed an issue where the post menu could remain open while scrolling in the post list
- Fixed an issue where the system message to add users to a channel was missing the execution link
- Fixed an issue where bulleted lists cut off text if nested deeper than two levels
- Fixed an issue where logging into an account that is not on any team freezes the app
- Fixed an issue on iOS causing the app to crash when taking a photo then attaching it to a post

## v1.6.1 Release
- Release Date: February 13, 2018
- Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported

### Bug Fixes
- Fixed an issue preventing the app from going to the correct channel when opened from a push notification
- Fixed an issue on Android devices where the app could sometimes freeze on the launch screen
- Fixed an issue on Samsung devices causing extra letters to be insterted when typing to filter user lists

## v1.6.0 Release
- Release Date: February 6, 2018
- Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported

### Highlights

#### Android File Sharing
- Share files and images from other applications as attached files in Mattermost 

### Improvements
- Added a right drawer to access settings, edit profile information, change online status and logout
- Added support for opening a Direct Message channel with yourself

### Bugs
- Fixed a number of issues causing crashes on Android devices
- Fixed an issue with auto capitalization on Android keyboards
- Fixed an issue where the GitLab SSO login button sometimes didn't appear
- Fixed an issue with link previews not appearing on some accounts
- Fixed an issue where logging out of the app didn't clear the notification badge on the homescreen icon
- Fixed an issue where interactive message buttons would not wrap to a new line
- Fixed an issue where the keyboard would sometimes overlap the text input box
- Fixed an issue where the Direct Message channel wouldn't open from the profile page
- Fixed an issue where posts would sometimes overlap
- Fixed an issue where the app sometimes hangs on logout

## v1.5.3 Release
- Release Date: February 1, 2018
- Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported
- Fixed a login issue when connecting to servers running a Data Retention policy 

## v1.5.2 Release
- Release Date: January 12, 2018
- Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported

### Bug Fixes
- Fixed an issue causing some Android devices to crash on launch
- Fixed an issue with the app occasionally crashing when receiving push notifications in a new channel 
- Channel footer area is now refreshed when switching between Group and Direct Message channels
- Fixed an issue on some Android devices so Mattermost verifies it has permissions to access ringtones
- Fixed an issue where the text box overlapped the keyboard on some iOS devices using multiple keyboard layouts
- Fixed an issue with video uploads on Android devices
- Fixed an issue with GIF uploads on iOS devices
- Fixed an issue with the mention badge flickering on the channel drawer icon when there were over 10 unread mentions
- Fixed an issue with the app occasionally freezing when requesting the RefreshToken

## v1.5.1 Release

- Release Date: December 7, 2017
- Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported

### Bug Fixes
- Fixed an issue with the upgrade app screen showing with a transparent background
- Fixed an issue with clearing or replying to notifications sometimes crashing the app on Android
- Fixed an issue with the app sometimes crashing due to a missing function in the swiping control

## v1.5 Release 

- Release Date: December 6, 2017
- Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported

### Highlights 

#### File Viewer
- Preview videos, RTF,  PDFs, Word, Excel, and Powerpoint files 

#### iPhone X Compatibility
- Added support for iPhone X

#### Slash Commands
- Added support for using custom slash commands
- Added support for built-in slash commands /away, /online, /offline, /dnd, /header, /purpose, /kick, /me, /shrug

### Improvements
- In iOS, 3D touch can now be used to peek into a channel to view the contents, and quickly mark it as read
- Markdown images in posts now render 
- Copy posts, URLs, and code blocks
- Opening a channel with Unread messages takes you to the "New Messages" indicator 
- Support for data retention, interactive message buttons, and viewing Do Not Disturb statuses depending on the server version
- (Edited) indicator now shows up beside edited posts 
- Added a "Recently Used" section for emoji reactions

### Bug Fixes 
- Android notifications now follow the default system setting for vibration 
- Fixed app crashing when opening notification settings on Android 
- Fixed an issue where the "Proceed" button on log in screen stopped working after pressing logout multiple times
- HEIC images posted from iPhones now get converted to JPEG before uploading

## v1.4.1 Release

Release Date: Nov 15, 2017
Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported

### Bug Fixes

- Fixed network detection issue causing some people to be unable to access the app
- Fixed issue with lag when pressing send button 
- Fixed app crash when opening notification settings
- Fixed various other bugs to reduce app crashes

## v1.4 Release 

- Release Date: November 6, 2017
- Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported

### Highlights 

#### Performance improvements
- Various performance improvements to decrease channel load times 

### Bug Fixes
- Fixed issue with Android app sometimes showing a white screen when re-opening the app
- Fixed an issue with orientation lock not working on Android 

## v1.3 Release 

- Release Date: October 5, 2017
- Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported

### Highlights 

#### Tablet Support (Beta) 
- Added support for landscape view, so the app may be used on tablets
- Note: Tablet support is in beta, and further improvements are planned for a later date

#### Link Previews 
- Added support for image, GIF, and youtube link previews

#### Notifications
- Android: Added the ability to set light, vibrate, and sound settings
- Android: Improved notification stacking so most recent notification shows first 
- Updated the design for Notification settings to improve usability 
- Added the ability to reply from a push notification without opening the app (requires Android v7.0+, iOS 10+) 
- Increased speed when opening app from a push notification

#### Download Files 
- Added the ability to download all files on Android and images on iOS

### Improvements
- Using `+` shortcut for emoji reactions is now supported 
- Improved emoji formatting (alignment and rendering of non-square aspect ratios)
- Added support for error tracking with Sentry
- Only show the "Connecting..." bar after two connection attempts 

### Bug Fixes
- Fixed link rendering not working in certain cases
- Fixed theme color issue with status bar on Android

## v1.2 Release

- Release Date: September 5, 2017 
- Server Versions Supported: Server v4.0+ is required, Self-Signed SSL Certificates are not supported

### Highlights 

#### AppConfig Support for EMM solutions
- Added [AppConfig](https://www.appconfig.org/) support, to make it easier to integrate with a variety of EMM solutions

#### Code block viewer
- Tap on a code block to open a viewer for easier reading 

### Improvements
- Updated formatting for markdown lists and code blocks
- Updated formatting for `in:` and `from:` search autocomplete 

### Emoji Picker for Emoji Reactions
- Added an emoji picker for selecting a reaction 

### Bug Fixes
- Fixed issue where if only LDAP and GitLab login were enabled, LDAP did not show up on the login page
- Fixed issue with three digit mention count UI in channel drawer

### Known Issues
- Using `+:emoji:` to react to a message is not yet supported 

## v1.1 Release

- Release Date: August 2017 
- Server Versions Supported: Server v3.10+ is required, Self-Signed SSL Certificates are not supported

### Highlights 

#### Search
- Search posts and tap to preview the result
- Click "Jump" to open the channel the search result is from 

#### Emoji Reactions
- View Emoji Reactions on a post

#### Group Messages
- Start Direct and Group Messages from the same screen

#### Improved Performance on Poor Connections
- Added auto-retry to automatically reattempt to get posts if the network connection is intermittent
- Added manual loading option if auto-retry fails to retrieve new posts

### Improvements
- Android: Added Big Text support for Android notifications, so they expand to show more details
- Added a Reset Cache option
- Improved "Jump to conversation" filter so it matches on nickname, full name, or username 
- Tapping on an @username mention opens the user's profile
- Disabled the send button while attachments upload
- Adjusted margins on icons and elsewhere to make spacing more consistent
- iOS URL scheme: mattermost:// links now open the new app
- About Mattermost page now includes a link to NOTICES.txt for platform and the mobile app
- Various UI improvements

### Bug Fixes
- Fixed an issue where sometimes an unmounted badge caused app to crash on start up 
- Group Direct Messages now show the correct member count 
- Hamburger icon does not break after swiping to close sidebar
- Fixed an issue with some image thumbnails appearing out of focus
- Uploading a file and then leaving the channel no longer shows the file in a perpetual loading state
- For private channels, the last member can no longer delete the channel if the EE server permissions do not allow it
- Error messages are now shown when SSO login fails
- Android: Leaving a channel now redirects to Town Square instead of the Town Square info page
- Fixed create new public channel screen shown twice when trying to create a channel
- Tapping on a post will no longer close the keyboard

## v1.0.1 Release 

- Release Date: July 20, 2017 
- Server Versions Supported: Server v3.8+ is required, Self-Signed SSL Certificates are not yet supported

### Bug Fixes
- Huawei devices can now load messages
- GitLab SSO now works if there is a trailing `/` in the server URL
- Unsupported server versions now show a prompt clarifying that a server upgrade is necessary

## v1.0 Release 

- Release Date: July 10, 2017 
- Server Versions Supported: Server v3.8+ is required, Self-Signed SSL Certificates are not supported

### Highlights 

#### Authentication (Requires v3.10+ [Mattermost server](https://github.com/mattermost/platform))
- GitLab login 

#### Offline Support
- Added offline support, so already loaded portions of the app are accessible without a connection
- Retry mechanism for posts sent while offline 
- See [FAQ](https://github.com/mattermost/mattermost-mobile#frequently-asked-questions) for information on how data is handled for deactivated users

#### Notifications (Requires v3.10+ [push proxy server](https://github.com/mattermost/mattermost-push-proxy)) 
- Notifications are cleared when read on another device
- Notification sent just before session expires to let people know login is required to continue receiving notifications

#### Channel and Team Sidebar
- Unreads section to easily access channels with new messages
- Search filter to jump to conversations quickly 
- Improved team switching design for better cross-team notifications 
- Added ability to join open teams on the server 

#### Posts
- Emojis now render
- Integration attachments now render 
- ~channel links now render 

#### Navigation
- Updated navigation to have smoother transitions 

### Known Issues
- [Android: Swipe to close in-app notifications does not work](https://mattermost.atlassian.net/browse/RN-45)
- Apps are not yet at feature parity for desktop, so features not mentioned in the changelog are not yet supported

### Contributors

Many thanks to all our contributors. In alphabetical order:
- asaadmahmood, cpanato, csduarte, enahum, hmhealey, jarredwitt, JeffSchering, jasonblais, lfbrock, omar-dev, rthill

## Beta Release

- Release Date: March 29, 2017
- Server Versions Supported: Server v3.7+ is required, Self-Signed SSL Certificates are not yet supported

Note: If you need an SSL certificate, consider using [Let's Encrypt](/install/config-ssl-http2-nginx.html) instead of a self-signed one.

### Highlights

The Beta apps are a work in progress, supported features are listed below. You can become a beta tester by [downloading the Android app](https://play.google.com/store/apps/details?id=com.mattermost.react.native&hl=en) or [signing up to test iOS](https://mattermost-fastlane.herokuapp.com/). 

#### Authentication
- Email login
- LDAP/AD login
- Multi-factor authentication 
- Logout

#### Messaging
- View and send posts in the center channel
- Automatically load more posts in the center channel when scrolling
- View and send replies in thread view
- "New messages" line in center channel (app does not yet scroll to the line)
- Date separators 
- @mention autocomplete
- ~channel autocomplete
- "User is typing" message
- Edit and delete posts
- Flag/Unflag posts
- Basic markdown (lists, headers, bold, italics, links)

#### Notifications
- Push notifications
- In-app notifications when you receive a message in another channel while the app is open
- Clicking on a push notification takes you to the channel

#### User profiles
- Status indicators
- View profile information by clicking on someone's username or profile picture

#### Files
- File thumbnails for posts with attachments
- Upload up to five images
- Image previewer to view images when clicked on

#### Channels
- Channel drawer for selecting channels
- Bolded channel names for Unreads, and mention jewel for Mentions
- (iOS only) Unread posts above/below indicator
- Favorite channels (Section in sidebar, and ability to favorite/unfavorite from channel menu)
- Create new public or private channels
- Create new Direct Messages (Group Direct Messages are not yet supported) 
- View channel info (name, header, purpose) 
- Join public channels
- Leave channel
- Delete channel
- View people in a channel
- Add/remove people from a channel
- Loading screen when opening channels 

#### Settings
- Account Settings > Notifications page
- About Mattermost info dialog
- Report a problem link that opens an email for bug reports

#### Teams
- Switch between teams using "Team Selection" in the main menu (viewing which teams have notifications is not yet supported) 

### Contributors

Many thanks to all our contributors. In alphabetical order:
- csduarte, dmeza, enahum, hmhealey, it33, jarredwitt, jasonblais, lfbrock, mfpiccolo, saturninoabril, thomchop
