# Mattermost Changelog

This changelog summarizes updates to [Mattermost Team Edition](http://www.mattermost.org/), an open source team messaging solution released monthly under an MIT license, and [Mattermost Enterprise Edition](https://about.mattermost.com/pricing/), a commercial upgrade offering enterprise messaging for large organizations.

Also see [changelog in progress](http://bit.ly/2nK3cVf) for the next release.

## Release v5.15 - [Quality Release](https://docs.mattermost.com/process/release-faq.html#release-overview)

- **v5.15.1, released 2019-10-11**
  - Fixed an issue that will be introduced with a change in upcoming server v5.16 and desktop app v4.3 releases where desktop notifications will be broken as the desktop app will no longer be able to directly interact with the web app. [MM-18819](https://mattermost.atlassian.net/browse/MM-18819)
  - Fixed an issue where server-side telemetry was not reporting back after 5.14 release. [MM-18115](https://mattermost.atlassian.net/browse/MM-18115)
- **v5.15.0, released 2019-09-16**
  - Original 5.15.0 release

Mattermost v5.15.0 contains low level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Bug Fixes
 - Fixed an issue where an invalid locale caused a white screen.
 - Fixed an issue where rate limited posts failed to load threads.
 - Improved the group linking failure error message and logging to make it clear that the group id attribute is most likely misconfigured.
 - Fixed an issue where the right-hand side did not fetch messages on socket reconnect when a different channel was in center.
 - Fixed an issue where posting a message in an empty channel sometimes caused the channel to display a loading spinner.
 - Fixed an issue where deleting the last post in a channel caused the channel to only display a loading spinner.
 - Fixed an issue with an absence of unread badges on private channels on mobile apps.
 - Fixed an issue where at-sign was missing in front of usernames in push notifications.
 - Fixed some bugs related to the new [keyboard accessibility](https://docs.mattermost.com/help/getting-started/accessibility.html) feature.
 - Fixed an issue where the "@" sign was replaced with keyboard accessibility feature on Italian keyboard.
 - Fixed an issue where joining a new channel with few posts sometimes did not take the user to the bottom of the channel.
 - Fixed an issue where scroll pop sometimes occured with embedded Youtube links.
 - Fixed an issue with stuttery dropdowns in Safari.
 - Fixed an issue where clicking on a post would highlight it after returning to the tab/window.
 - Fixed an issue where SVG attachments bled over into subsequent posts.
 - Fixed an issue where long posts were overlapping in compact view.
 - Fixed an issue where the expand/collapse button in images were underlined.
 - Fixed an issue where incoming webhook URL was clickable and shown as a link on the desktop app.
 - Fixed an issue where the markdown helper text was missing on Edit Channel Header modal.
 - Fixed an issue on mobile view where Edit/Delete/More options were not displayed on the right-hand side after a message was posted.
 - Fixed an issue where the channel mute icon was displayed in the incorrect position when a channel was muted.
 - Fixed an issue where there was an extra menu divider on Town Square channel menu.
 - Fixed an issue on Firefox where post and comment boxes were expanding too early.
 - Fixed an issue where focus was not automatically set on text input box after selecting an emoji from the emoji picker.
 - Fixed an issue where channel changes were not updated for other users until refresh.
 - Fixed an issue where changes to Account Settings were being saved even when the user did not click the **Save** button.
 - Fixed an issue where some of the links in System Console opened the page on the same tab instead of opening it on a new browser/tab.
 - Fixed an issue where installing a plugin via URL failed if the download took longer then 30 seconds.
 - Fixed an issue where plugins did not get disabled when removing them.
 - Fixed an issue where plugin translation files were not updated on web-clients when plugins were upgraded.
 - Fixed an issue where bots could not be added to any team if server wide email domain restriction was enabled.
 - Fixed an issue where pagination broke when adding users to a team.
 - Fixed an issue where list of users were not paginated on warning modal for LDAP group sync team / channel removal.
 - Fixed an issue where enabling LDAP Trace prevented login.
 - Fixed an issue where Google User API Endpoint showed an outdated helper text.
 - Fixed an issue where a markdown image with an SVG briefly displayed for sender with ``EnableSVGs`` set to false.
 - Fixed an issue with an incorrect error message on Custom URL Schemes field.

### Known Issues
 - JS console error may appear when uploading an image from the right-hand side.
 - Scroll pop may occur in channels with markdown images.
 - Trailing white space is not ignored when saving bot user name.
 - Clicking "Edit" of another sub-section in Account Settings appears to save the setting that is currently being edited in an open sub-section in the same modal.
 - Some pre-packaged plugins show as removable in the User Interface.
 - If ``ExperimentalStrictCSRFEnforcement`` is set to True, attempts to use ``/jira subscribe`` fail.
 - Users are unable to type in any other channel after leaving a draft post in preview mode in one channel and then switching to another channel.
 - User count in a channel does not update until after refresh if a user automatically joins a channel.
 - Scrolling upwards while loading more posts sometimes causes you to jump upwards on Firefox.
 - Modifying config files causes compliance exports to run twice.
 - Using channel autocomplete while editing post causes current channel to be unread.
 - On a server using a subpath, the URL opens a blank page if the System Admin changes the Site URL in the System Console UI. To fix, the System Admin should restart the server.
 - Login does not work when Custom Terms of Service is enabled and MFA is enforced.
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 
### Contributors

 - [a-arias](https://github.com/a-arias), [aaronrothschild](https://github.com/aaronrothschild), [accxiagmbh](https://github.com/accxiagmbh), [aeomin](https://translate.mattermost.com/user/aeomin/), [Akito13](https://github.com/Akito13), [ali-farooq0](https://github.com/ali-farooq0), [Amonith](https://github.com/Amonith), [amyblais](https://github.com/amyblais), [angelbarrera92](https://github.com/angelbarrera92), [ankitrgadiya](https://github.com/ankitrgadiya), [asaadmahmood](https://github.com/asaadmahmood), [atpons](https://github.com/atpons), [bradjcoughlin](https://github.com/bradjcoughlin), [cardoso](https://github.com/cardoso), [cdncat](https://github.com/cdncat), [chikei](https://github.com/chikei), [comharris](https://github.com/comharris), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [deanwhillier](https://github.com/deanwhillier), [der-test](https://github.com/der-test), [devinbinnie](https://github.com/devinbinnie), [DHaussermann](https://github.com/DHaussermann), [DSchalla](https://github.com/DSchalla), [eilgin](https://github.com/eilgin), [ejachang](https://github.com/ejachang), [elyscape](https://github.com/elyscape), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [eshyong](https://github.com/eshyong), [ethervoid](https://github.com/ethervoid), [g3rv4](https://github.com/g3rv4), [gabrieljackson](https://github.com/gabrieljackson), [gigawhitlocks](https://github.com/gigawhitlocks), [goku321](https://github.com/goku321), [gruceqq](https://translate.mattermost.com/user/gruceqq/), [grundleborg](https://github.com/grundleborg), [hahmadia](https://github.com/hahmadia), [hanzei](https://github.com/hanzei), [healthchecks](https://github.com/healthchecks), [hectorskypl](https://github.com/hectorskypl), [hmhealey](https://github.com/hmhealey), [iomodo](https://github.com/iomodo), [irbrad](https://github.com/irbrad), [it33](https://github.com/it33), [ivenk](https://github.com/ivenk), [janvt](https://github.com/janvt), [jasonblais](https://github.com/jasonblais), [jesperhansen17](https://github.com/jesperhansen17), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [jozuenoon](https://github.com/jozuenoon), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [Kaya_Zeren](https://twitter.com/kaya_zeren), [kdenz](https://github.com/kdenz), [kosgrz](https://github.com/kosgrz), [krjn](https://github.com/krjn), [Lena](https://translate.mattermost.com/user/Lena/), [levb](https://github.com/levb), [lfbrock](https://github.com/lfbrock), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [Lisenish](https://github.com/Lisenish), [liusy182](https://github.com/liusy182), [lurcio](https://github.com/lurcio), [manland](https://github.com/manland), [marianunez](https://github.com/marianunez), [MatthewDorner](https://github.com/MatthewDorner), [matthewshirley](https://github.com/matthewshirley), [meilon](https://github.com/meilon), [metanerd](https://github.com/metanerd), [mgdelacroix](https://github.com/mgdelacroix), [michaelgamble](https://github.com/michaelgamble), [mickmister](https://github.com/mickmister), [migbot](https://github.com/migbot), [mjthomp95](https://github.com/mjthomp95), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [pichouk](https://github.com/pichouk), [Rajakavitha1](https://github.com/Rajakavitha1), [reflog](https://github.com/reflog), [rodcorsi](https://github.com/rodcorsi), [Roy-Orbison](https://github.com/Roy-Orbison), [sadohert](https://github.com/sadohert), [saturninoabril](https://github.com/saturninoabril), [scottleedavis](https://github.com/scottleedavis), [sij507](https://github.com/sij507), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [sudheerDev](https://github.com/sudheerDev), [thekiiingbob](https://github.com/thekiiingbob), [thePanz](https://github.com/thePanz), [threepwood-mm](https://github.com/threepwood-mm), [tnir](https://github.com/tnir), [ulhosting](https://github.com/uhlhosting), [uusijani](https://github.com/uusijani), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [Willyfrog](https://github.com/Willyfrog), [wyze](https://github.com/wyze)

## Release v5.14 - [Feature Release](https://docs.mattermost.com/process/release-faq.html#release-overview)

- **v5.14.4, released 2019-10-11**
  - Fixed an issue that will be introduced with a change in upcoming server v5.16 and desktop app v4.3 releases where desktop notifications will be broken as the desktop app will no longer be able to directly interact with the web app. [MM-18819](https://mattermost.atlassian.net/browse/MM-18819)
  - Fixed an issue where server-side telemetry was not reporting back after 5.14 release. [MM-18115](https://mattermost.atlassian.net/browse/MM-18115)
- **v5.14.3, released 2019-09-16**
  - Fixed an issue where edited posts were not included in Compliance Export (Beta). [MM-18522](https://mattermost.atlassian.net/browse/MM-18522)
- **v5.14.2, released 2019-08-30**
  - Fixed an issue where Mattermost crashed when date-related search terms `on:` `before:` and `after:` were used in search. [MM-18143](https://mattermost.atlassian.net/browse/MM-18143)
- **v5.14.1, released 2019-08-28**
  - Fixed issues with [keyboard accessibility](https://docs.mattermost.com/help/getting-started/accessibility.html) where post and search textboxes did not read characters when using the arrow keys to move back and forth through the text. [MM-17964](https://mattermost.atlassian.net/browse/MM-17964) and [MM-17974](https://mattermost.atlassian.net/browse/MM-17974)
- **v5.14.0, released 2019-08-16**
  - Original 5.14.0 release

Mattermost v5.14.0 contains a medium level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Compatibility

#### Removed and Deprecated Features

 - We are removing support for Internet Explorer (IE11) in Mattermost v5.16.0, which releases on October 16, 2019. Learn more in our [forum post](https://forum.mattermost.org/t/mattermost-is-dropping-support-for-internet-explorer-ie11-in-v5-16/7575).
 
### Breaking Changes

 - Webhooks are now only displayed if the user is the creator of the webhook or a system administrator.
 - With the update from Google+ to Google People, system admins need to ensure the ``GoogleSettings.Scope`` config.json setting is set to ``profile email`` and ``UserAPIEndpoint`` setting should be set to ``https://people.googleapis.com/v1/people/me?personFields=names,emailAddresses,nicknames,metadata`` per [updated documentation](https://docs.mattermost.com/deployment/sso-google.html).

**IMPORTANT:** If you upgrade from a release earlier than 5.13, please read the other [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html).

### Highlights

#### Keyboard navigation and screen reader improvements

 - New keyboard navigation improvements enable you to move between app regions—like the post list, channel sidebar, and header—using F6 on the Desktop App and CTRL-F6 on a web browser. You can also use TAB, arrow keys, and ENTER to interact with buttons, links, and other elements in Mattermost.
 - Screen readers are now much more compatible with Mattermost. Buttons, links, and app regions now have accurate readouts that enable visually impaired users to use Mattermost productively with screen readers.
 - [Learn more](https://docs.mattermost.com/help/getting-started/accessibility.html)

#### Bidirectional scrolling to land on oldest unread post
 - No more scrolling required to get to the oldest unread post. Now when the channel opens when there are unreads it opens at the new messages line, regardless of how many unreads exist since the last time the user viewed the channel.

#### Jira V2.1
 - Full list of features in v2.1: https://github.com/mattermost/mattermost-plugin-jira#jira-21-features.

#### System Console tools to manage LDAP Groups within Teams and Channels (EE)
 - New Team and Channel pages in the System Console allow administrators to easily manage teams and channels membership with LDAP Group Synchronization instead of using the CLI group commands released in v5.12.
 
#### Pre-packaged Plugins
 - [Jenkins plugin](https://github.com/mattermost/mattermost-plugin-jenkins) for interacting with jobs and builds via slash commands in Mattermost.
 - [Antivirus plugin](https://github.com/mattermost/mattermost-plugin-antivirus) for scanning files uploaded to Mattermost.
 - [GitLab plugin](https://github.com/mattermost/mattermost-plugin-gitlab) for getting notifications in Mattermost about mentions, review requests and comments.

### Improvements

#### User Interface (UI)
 - Added support for allowing ``+`` and ``.`` in **System Console > Customization > Posts > Custom URL Schemes**.
 - Added support for Range on files needed by Safari to view videos.
 - Added ability to add info cards to the right-hand side section.
 - Added support for rendering emojis in Message Attachment field titles.
 - Changed "About" section references to use the site name when it is configured in **System Console > Custom Branding > Site Name**.
 - Combined "Send messages on CTRL+ENTER" with code block setting.
 - Added ability to upload files on paste when file constructor is not supported (ie. in Edge or IE11).
 
#### Import/Export
 - Added the ability to import Slack corporate export files with direct messages, group messages and private channels.
 - Added support for exporting Global Relay to zip file.

#### Webhooks
- ``EnableWebhookDebugging`` now logs the request id for additional context when debugging.
 - Added support for plugins to dismiss posts through the ``MessageWillBePosted`` hook. Dismissed posts no longer show up as a client-side error.
 - Added an optional "icon_emoji" field to incoming webhooks to use an emoji in place of the display picture when the webhook posts into Mattermost.
 
#### Integrations
 - Added support for interactive dialogs without elements, e.g. for confirmation dialogs.
 - Added support for relative links in interactive message buttons, simplifying plugin development.
 
#### Plugins
 - Added support for plugins to override right-hand sidebar.
 - Added support for plugins to trigger interactive dialogs programmatically, instead of only after a user action.
 
#### Bot Accounts
 - Added an identifier for compliance exports when a message is posted by a bot account.
 - Created a dedicated System Console page at /admin_console/integrations/bot_accounts to organize bot configuration options.
 
#### Command Line Interface (CLI)
 - Added support for converting bot accounts to user accounts with email/password login through the CLI.
 - Extended the config migrate command to handle SAML keys and certificates.
 - Updated CLI channel list and search commands to show if a channel is private.
 - Create CLI command "team modify" to modify team's privacy setting.
 
#### Administration
 - Office365 SSO was promoted out of beta.
 - Removed maximum length from ``LinkMetadata`` value so that links can generate OpenGraph previews and be stored in the database.
 - The config.json file is now generated with build time using defaults in code and not in ``default.json``.
 - Added new settings to have more control over ``BindAddress`` and ``AdvertiseAddress`` in the cluster server to allow users to configure properly in situations where the servers are communicating through another server using NAT.
 - implemented enhanced logging for CSRF warnings by adding the following information to each request: Remote Adddress, Path, User ID, Session ID.
 
#### Enterprise Edition (EE)
 - Added support for signing SAML requests, as required for Infosec approval.
 - Added support for configuring the interface used for cluster peer discovery in High Availability clusters.

### Bug Fixes
 - Fixed an issue where pagination of group members was broken in LDAP Groups.
 - Fixed an issue where the options to leave a team was disabled for all teams and not just the primary team when a primary team was set.
 - Fixed an issue where bulk import got stuck when importing lines were missing the "type" entry.
 - Fixed an issue where titles for webhooks, commands and OAuth apps were no longer bolded in the System Console.
 - Fixed an issue where disabling email notifications also disabled email invites.
 - Fixed an issue where Admins were shown a warning of a user's bot being deactivated even if they already were.
 - Fixed an issue where a bot profile image disappeared when saving bot details.
 - Fixed an issue where plus-sign was not visible on mobile browser view for reacting with a new emoji next to existing reactions.
 - Fixed an issue in the System Console where the UserID in User Activity Logs changed from email to UserID.
 - Fixed an issue where user got a notification to add a bot to a channel when mentioning it.
 - Fixed an issue where permanenently deleting a bot user didn't remove it from the bots table.
 - Fixed an issue where a scroll pop was caused by large image dimensions in markdown.

### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:

 - Under ``ClusterSettings`` in ``config.json``:
    - Added ``NetworkInterface`` to allow configuring devices to detect the IP in High Availability clusters.
    - Added ``BindAddress`` and ``AdvertiseAddress`` to add more control over bind and advertising address in a cluster server.
 - Under ``ComplianceSettings`` in ``config.json``:
    - Added ``SignRequest`` to add support for signing SAML requests.
 - Under ``PluginSettings`` in ``config.json``:
    - Added ``AllowInsecureDownloadUrl`` to allow servers to download and install a plugin from a remote url via the System Console.

### Open Source Components

 - Added ``core-js`` in https://github.com/mattermost/mattermost-mobile/.
 - Added ``deepmerge`` in https://github.com/mattermost/mattermost-mobile/.
 - Removed ``react-native-bottom-sheet`` from https://github.com/mattermost/mattermost-mobile/.
 - Added ``react-hot-loader`` in https://github.com/mattermost/mattermost-webapp.
 - Removed ``@babel/polyfill`` from https://github.com/mattermost/mattermost-webapp.
 - Removed ``redux-persist-transform-filter`` from https://github.com/mattermost/mattermost-webapp.
 - Removed ``url-search-params-polyfill`` from https://github.com/mattermost/mattermost-webapp.
 - Removed ``whatwg-fetch`` from https://github.com/mattermost/mattermost-webapp.

### API Changes
 - Migrated user API endpoint from Google+ API to People API.
 - Added ``api/v4/channels/group/search`` API endpoint to return the group channels whose members' usernames match the search term.
 - Added ``/api/v4/channels/:channel_id/members_minus_group_members`` API endpoint to determine users who will be removed from a group-synchronized channel.
 - Added ``api/v4/posts/unread`` API endpoint to support landing on the last unread post.
 - Added ``api/v4/teams/:team_id/members_minux_group_members`` API endpoint to determine users who will be removed from a group-synchronized team.
 - Added ``api/v4/users/group_channels`` API endpoint to get an object containing a key per group channel id in the query and its value as a list of users members of that group channel.
 - Added ``api/v4/sessions/revoke/all`` API endpoint to add the ability to revoke sessions from all users.

#### Plugin API
 - Added ``GetBotIconImage``, ``SetBotIconImage`` and ``DeleteBotIconImage`` API endpoints to control bot icon images.
 - Added ``api/v4/plugins/install_from_url`` API endpoint to allow server to download and install a plugin from a remote url.

### Known Issues
 - Users are unable to type in any other channel after leaving a draft post in preview mode in one channel and then switching to another channel.
 - Google User API Endpoint shows outdated helper text.
 - Making a post in an empty channel sometimes causes the channel to display a loading spinner.
 - Deleting the last post in a channel causes the channel to only display a loading spinner.
 - Markdown helper text is missing on Edit Channel Header modal.
 - User count in a channel does not update until after refresh if a user automatically joins a channel.
 - Long posts might overlap in compact view.
 - Joining a new channel with few posts might not take the user to the bottom of the channel.
 - Missing messages can be caused if network fails on API calls.
 - Search help text popover may not display on narrow screen view.
 - Expand/collapse in image icons are underlined.
 - Messages may not load when opening a channel with multiple unread messages.
 - Scrolling upwards while loading more posts sometimes causes you to jump upwards on Firefox.
 - Post and comment boxes are expanding too early on Firefox.
 - Modifying config files causes compliance exports to run twice.
 - Using channel autocomplete while editing post causes current channel to be unread.
 - Scroll pop may occur with embedded Youtube links.
 - Clicking on a post will highlight it after returning to the tab/window.
 - Plugin translation files are not updated on web-client when plugins are upgraded.
 - Changes to Account Settings are being saved even when user does not clicks on Save button.
 - SVG attachments bleed over into subsequent posts.
 - Custom-Attributes plugin might crash.
 - Pagination breaks when adding users to a team.
 - On a server using a subpath, the URL opens a blank page if the System Admin changes the Site URL in the System Console UI. To fix, the System Admin should restart the server.
 - Login does not work when Custom Terms of Service is enabled and MFA is enforced.
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.

### Contributors

 - [a-arias](https://github.com/a-arias), [aaronrothschild](https://github.com/aaronrothschild), [aayushbisen](https://github.com/aayushbisen), [adzimzf](https://github.com/adzimzf), [aeomin](https://translate.mattermost.com/user/aeomin/), [AGMETEOR](https://github.com/AGMETEOR), [alejandrosame](https://github.com/alejandrosame), [ali-farooq0](https://github.com/ali-farooq0), [alxsah](https://github.com/alxsah), [amyblais](https://github.com/amyblais), [asaadmahmood](https://github.com/asaadmahmood), [bbodenmiller](https://github.com/bbodenmiller), [bnoggle](https://github.com/bnoggle), [bradjcoughlin](https://github.com/bradjcoughlin), [chikei](https://github.com/chikei), [comharris](https://github.com/comharris), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [deanwhillier](https://github.com/deanwhillier), [der-test](https://github.com/der-test), [devinbinnie](https://github.com/devinbinnie), [DSchalla](https://github.com/DSchalla), [elyscape](https://github.com/elyscape), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [eshyong](https://github.com/eshyong), [gabrieljackson](https://github.com/gabrieljackson), [gruceqq](https://translate.mattermost.com/user/gruceqq/), [grundleborg](https://github.com/grundleborg), [gupsho](https://github.com/gupsho), [hanzei](https://github.com/hanzei), [hectorskypl](https://github.com/hectorskypl), [hmhealey](https://github.com/hmhealey), [hvhallmann](https://github.com/hvhallmann), [Hyaxia](https://github.com/Hyaxia), [Inconnu08](https://github.com/Inconnu08), [irbrad](https://github.com/irbrad), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jesperhansen17](https://github.com/jesperhansen17), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [johnthompson365](https://github.com/johnthompson365), [Jonany](https://github.com/Jonany), [joshuabezaleel](https://github.com/joshuabezaleel), [justinegeffen](https://github.com/justinegeffen), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [Kaya_Zeren](https://twitter.com/kaya_zeren), [keaton185](https://github.com/keaton185), [kosgrz](https://github.com/kosgrz), [krjn](https://github.com/krjn), [Lena](https://translate.mattermost.com/user/Lena/), [levb](https://github.com/levb), [lfbrock](https://github.com/lfbrock), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lpadgett](https://github.com/lpadgett), [lurcio](https://github.com/lurcio), [manland](https://github.com/manland), [marianunez](https://github.com/marianunez), [meilon](https://github.com/meilon), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [migbot](https://github.com/migbot), [mjthomp95](https://github.com/mjthomp95), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [mounicapaladugu](https://github.com/mounicapaladugu), [mzaks](https://github.com/mzaks), [noxer](https://github.com/noxer), [ollykel](https://github.com/ollykel), [PeterDaveHello](https://github.com/PeterDaveHello), [phillipahereza](https://github.com/phillipahereza), [piperRyan](https://github.com/piperRyan), [Rajakavitha1](https://github.com/Rajakavitha1), [RajatVaryani](https://github.com/RajatVaryani), [rajiv-k](https://github.com/rajiv-k), [reflog](https://github.com/reflog), [rexredinger](https://github.com/rexredinger), [rodcorsi](https://github.com/rodcorsi), [rvillablanca](https://github.com/rvillablanca), [saturninoabril](https://github.com/saturninoabril), [scottleedavis](https://github.com/scottleedavis), [Selimix](https://github.com/Selimix), [SezalAgrawal](https://github.com/SezalAgrawal), [srkgupta](https://github.com/srkgupta), [steevsachs](https://github.com/steevsachs), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [sudheerDev](https://github.com/sudheerDev), [svelle](https://github.com/svelle), [tapaswenipathak](https://github.com/tapaswenipathak), [tekminewe](https://github.com/tekminewe), [thekiiingbob](https://github.com/thekiiingbob), [thePanz](https://github.com/thePanz), [ulhosting](https://github.com/uhlhosting), [VolatianaYuliana](https://github.com/VolatianaYuliana), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [Willyfrog](https://github.com/Willyfrog)

## Release v5.13 - [Quality Release](https://docs.mattermost.com/process/release-faq.html#release-overview)

Mattermost v5.13.0 contains low level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

- **v5.13.3, released 2019-08-22**
  - Mattermost v5.13.3 contains a medium level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
- **v5.13.2, released 2019-07-24**
  - Fixed performance issues in channels with large message history due to a change made to posts query. [MM-16936](https://mattermost.atlassian.net/browse/MM-16936)
  - Fixed an issue where some settings were not visible in the System Console. [MM-17114](https://mattermost.atlassian.net/browse/MM-17114)
  - Fixed an issue where announcement banner overlapped content. [MM-17115](https://mattermost.atlassian.net/browse/MM-17115)
  - Fixed an issue where the scroll position was not at the new message indicator on switching channels when there were 30-60 unread messages. [MM-17078](https://mattermost.atlassian.net/browse/MM-17078)
- **v5.13.1, released 2019-07-19**
  - Fixed an issue with Jira plugin where creating or attaching to Jira issues failed due to GDPR changes released by Atlassian. Affected Jira Cloud only, not Jira Server or Jira Data Center. [MM-17060](https://mattermost.atlassian.net/browse/MM-17060)
  - Fixed an issue in server logs where messages related to OpenGraph API were unnecessarily reported as errors. [MM-17043](https://mattermost.atlassian.net/browse/MM-17043)
  - Fixed an issue in the System Console without an Enterprise Edition license where **Push Notification Contents** setting was not available. [MM-17008](https://mattermost.atlassian.net/browse/MM-17008)
- **v5.13.0, released 2019-07-16**
  - Original 5.13.0 release

### Compatibility

#### Removed and Deprecated Features

 - We are removing support for Internet Explorer (IE11) in Mattermost v5.16.0, which releases on October 16, 2019. Learn more in our [forum post](https://forum.mattermost.org/t/mattermost-is-dropping-support-for-internet-explorer-ie11-in-v5-16/7575).
 - v4.10.0 as our current Extended Support Release (ESR) is coming to the end of its lifecycle. We will be implementing version v5.9.0 as a new ESR starting July 16, 2019. Learn more in our [forum post](https://forum.mattermost.org/t/extended-support-release-update/7099).

### Bug Fixes
 - Fixed an issue where changing the timezone setting to "Set automatically" did not work on the mobile app.
 - Fixed an issue where the channel introduction content sometimes disappeared on opening a channel.
 - Fixed an issue with missing messages.
 - Fixed an issue where disabling Join/Leave Messages and switching to a specific channel caused a white screen.
 - Fixed an issue where the SMTP server password was no longer concealed in the System Console.
 - Fixed an issue where Notifications and Plugins settings were missing in the System Console for restricted system administrators.
 - Fixed an issue where "Enable AD/LDAP Group Sync" was visible in experimental System Console settings section in Team Edition servers.
 - Fixed an issue where **System Console > SMTP > Connection Security** setting was missing in Team Edition servers.
 - Fixed an issue where "Allow Mobile upload/download Files" options in the System Console where not hidden in Team Edition servers.
 - Fixed an issue where channel links did not work inside brackets.
 - Fixed an issue where uploading a team icon image fired a JS console error and a blank image preview.
 - Fixed an issue on Safari where a user jumped to the top of the Direct Messages selection list every few seconds.
 - Fixed an issue where "Error populating syncables" was seen on login when LDAP groups tried to add a user to a team that was at its maximum number of users.
 - Fixed an issue where the slash command ``/rename`` was restricted to 22-character maximum channel name length.
 - Fixed an issue where Manage Members menu was visible even if a user did not have Manage Member permissions when viewing the Main Menu.
 - Fixed an issue where the "Set a Header" button in the channel introduction was not clickable.
 - Fixed an issue where Group Message and private channel icons in the sidebar were misaligned.
 - Fixed an issue where custom emojis sometimes overlapped in messages.
 - Fixed an issue where bot tags were misaligned in search results and in the "in:" modifier in the search bar autocomplete.
 - Fixed an issue where the post menu divider had a gap in mobile view.
 - Fixed an issue where the bottom of right-hand side was cut off in tablet view.
 - Fixed an issue where the channel dropdown menu user interface was broken in mobile view when Zoom plugin was enabled.
 - Fixed an issue where the Save button was hidden in the System Console when a banner was displayed at the top of the page.
 - Fixed an issue where users were not able to search for split parts of first/last names or for split characters such as ``_`` with elasticsearch autocomplete enabled.
 - Fixed an issue where OAuth endpoints returned application/json content type for HTML redirects.
 - Fixed an issue where json responses were not returned for errors on oauth API endpoints, and a 500 error was returned instead of 4xx errors.
 
### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:

 - Under ``ElasticsearchSettings`` in ``config.json``:
    - Added ``SkipTLSVerification`` to ignore certificate verification for Elasticsearch.
 
#### Open Source Components

 - Added ``moment-timezone`` in https://github.com/mattermost/mattermost-redux/.

#### Database Changes

 - ``plugins`` type entries in the ``Jobs`` table will be purged on upgrade. This job was incorrectly configured to run every minute, spamming the table with mostly useless records. All old records will be removed on upgrade, and the job will run daily instead.

### Known Issues
 - Cannot leave any team when a default [primary team](https://docs.mattermost.com/administration/config-settings.html#primary-team-experimental) is set.
 - Titles for webhooks, commands and OAuth apps are no longer bolded in the System Console.
 - Users can get logged out of server without a session expiry notification.
 - Desktop app hangs on opening emoji picker.
 - When a primary team is set, the options to leave a team is disabled for all teams, not just the primary team.
 - Plugin crashes the server when calling ``w.WriteHeader(0)``.
 - Bot account profile image disappears when saving bot details.
 - Custom emoji containing specified letters do not appear in emoji autocomplete, unless they start with the letters or have been returned in the autocomplete before.
 - Buttons inside ephemeral messages are not clickable / functional on the mobile app.
 - On a server using a subpath, the URL opens a blank page if the System Admin changes the Site URL in the System Console UI. To fix, the System Admin should restart the server.
 - Login does not work when Custom Terms of Service is enabled and MFA is enforced.
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 
### Contributors

 - [aaronrothschild](https://github.com/aaronrothschild), [aeomin](https://translate.mattermost.com/user/aeomin/), [adzimzf](https://github.com/adzimzf), [alxsah](https://github.com/alxsah), [amyblais](https://github.com/amyblais), [asaadmahmood](https://github.com/asaadmahmood), [Banyango](https://github.com/Banyango), [bbodenmiller](https://github.com/bbodenmiller), [bezumkin](https://github.com/bezumkin), [bolariin](https://github.com/bolariin), [bradjcoughlin](https://github.com/bradjcoughlin), [carmo-evan](https://github.com/carmo-evan), [chikei](https://github.com/chikei), [cjohannsen81](https://github.com/cjohannsen81), [cometkim](https://github.com/cometkim), [comharris](https://github.com/comharris), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [cseeger-epages](https://github.com/cseeger-epages), [Dak425](https://github.com/Dak425), [danmaas](https://github.com/danmaas), [deanwhillier](https://github.com/deanwhillier), [dependabot[bot]](https://github.com/dependabot[bot]), [der-test](https://github.com/der-test), [DHaussermann](https://github.com/DHaussermann), [DSchalla](https://github.com/DSchalla), [elyscape](https://github.com/elyscape), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [ewwollesen](https://github.com/ewwollesen), [gabrieljackson](https://github.com/gabrieljackson), [georgewitteman](https://github.com/georgewitteman), [GianOrtiz](https://github.com/GianOrtiz), [giorgosdi](https://github.com/giorgosdi), [glebtv](https://github.com/glebtv), [goku321](https://github.com/goku321), [gruceqq](https://translate.mattermost.com/user/gruceqq/), [grundleborg](https://github.com/grundleborg), [gupsho](https://github.com/gupsho), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hectorskypl](https://github.com/hectorskypl), [hmhealey](https://github.com/hmhealey), [Inconnu08](https://github.com/Inconnu08), [iomodo](https://github.com/iomodo), [it33](https://github.com/it33), [ivenk](https://github.com/ivenk), [jasonblais](https://github.com/jasonblais), [jesperhansen17](https://github.com/jesperhansen17), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [jkl5616](https://github.com/jkl5616), [joewaitye](https://github.com/joewaitye), [johnthompson365](https://github.com/johnthompson365), [Jonany](https://github.com/Jonany), [jsmestad](https://github.com/jsmestad), [JtheBAB](https://github.com/JtheBAB), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [Kaya_Zeren](https://twitter.com/kaya_zeren), [kevinetienne](https://github.com/kevinetienne), [kim95175](https://github.com/kim95175), [kincl](https://github.com/kincl), [kosgrz](https://github.com/kosgrz), [krjn](https://github.com/krjn), [lassimus](https://github.com/lassimus), [Lena](https://translate.mattermost.com/user/Lena/), [letsila](https://github.com/letsila), [levb](https://github.com/levb),[lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lindy65](https://github.com/lindy65), [lisakycho](https://github.com/lisakycho), [LocalHeroPro](https://github.com/LocalHeroPro), [lurcio](https://github.com/lurcio), [manland](https://github.com/manland), [marianunez](https://github.com/marianunez), [maruTA-bis5](https://github.com/maruTA-bis5), [meilon](https://github.com/meilon), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [migbot](https://github.com/migbot), [mjthomp95](https://github.com/mjthomp95), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [moksahero](https://github.com/moksahero), [mounicapaladugu](https://github.com/mounicapaladugu), [mstoli](https://github.com/mstoli), [mzaks](https://github.com/mzaks), [nafisfaysal](https://github.com/nafisfaysal), [nils-schween](https://github.com/nils-schween), [patterns](https://github.com/patterns), [piperRyan](https://github.com/piperRyan), [pradeepmurugesan](https://github.com/pradeepmurugesan), [RajatVaryani](https://github.com/RajatVaryani), [reflog](https://github.com/reflog), [renatopeterman](https://github.com/renatopeterman), [rodcorsi](https://github.com/rodcorsi), [rvillablanca](https://github.com/rvillablanca), [saturninoabril](https://github.com/saturninoabril), [scottleedavis](https://github.com/scottleedavis), [SezalAgrawal](https://github.com/SezalAgrawal), [Sheshagiri](https://github.com/Sheshagiri), [srkgupta](https://github.com/srkgupta), [steevsachs](https://github.com/steevsachs), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [sudheerDev](https://github.com/sudheerDev), [svelle](https://github.com/svelle), [tapaswenipathak](https://github.com/tapaswenipathak), [tarikeshaq](https://github.com/tarikeshaq), [tekminewe](https://github.com/tekminewe), [Theaxiom](https://github.com/Theaxiom), [thekiiingbob](https://github.com/thekiiingbob), [thePanz](https://github.com/thePanz), [ThiefMaster](https://github.com/ThiefMaster), [tomasmik](https://github.com/tomasmik), [ulhosting](https://github.com/uhlhosting), [utaani](https://github.com/utaani), [waseem18](https://github.com/waseem18), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [willdot](https://github.com/willdot), [Willyfrog](https://github.com/Willyfrog), [Wipeout55](https://github.com/Wipeout55), [yuya-oc](https://github.com/yuya-oc), [zkry](https://github.com/zkry)

## Release v5.12 - Feature Release

Mattermost v5.12.0 contains low to medium level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

- **v5.12.6, released 2019-08-22**
  - Mattermost v5.12.6 contains a medium level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
- **v5.12.5, released 2019-07-19**
  - Fixed an issue with Jira plugin where creating or attaching to Jira issues failed due to GDPR changes released by Atlassian. Affected Jira Cloud only, not Jira Server or Jira Data Center. [MM-17060](https://mattermost.atlassian.net/browse/MM-17060)
- **v5.12.4, released 2019-07-15**
  - Fixed an issue with missing messages. [MM-16921](https://mattermost.atlassian.net/browse/MM-16921)
- **v5.12.3, released 2019-07-09**
  - Fixed an issue where setting the MM_SQLSETTINGS_DATASOURCEREPLICAS environment variable broke the server startup. [MM-16719](https://mattermost.atlassian.net/browse/MM-16719)
- **v5.12.2, released 2019-07-03**
  - Fixed an issue where Net Promoter Score (NPS) went into a loop when [Experimental Enable Automatic Replies feature](https://docs.mattermost.com/administration/config-settings.html#enable-automatic-replies-experimental) was turned on in Account Settings.
- **v5.12.1, released 2019-06-28** 
  - Fixed an issue where messages were sometimes missing after reconnecting the network. [MM-16423](https://mattermost.atlassian.net/browse/MM-16423)
  - Fixed an issue where the client sometimes crashed while viewing a direct message channel. [MM-16480](https://mattermost.atlassian.net/browse/MM-16480)
  - Fixed an issue where Net Promoter Score (NPS) printed an error message in server logs when Error and Diagnostics Reporting was disabled. [MM-16465](https://mattermost.atlassian.net/browse/MM-16465)
  - Fixed an issue where Net Promoter Score (NPS) telemetry reporting surveys were disabled if the setting had not been modified. [MM-16554](https://mattermost.atlassian.net/browse/MM-16554)
- **v5.12.0, released 2019-06-16**
  - Original 5.12.0 release

### Breaking changes since last release

 - If your plugin uses the ``DeleteEphemeralMessage`` plugin API, update it to accept a ``postId string`` parameter. See [documentation](https://developers.mattermost.com/extend/plugins/server/reference/#API.DeleteEphemeralPost) to learn more.
 - Image link and YouTube previews do not display unless **System Console > Enable Link Previews** is enabled. Please ensure that your Mattermost server is connected to the internet and has network access to the websites from which previews are expected to appear. [Learn more here](https://docs.mattermost.com/administration/config-settings.html#enable-link-previews).
 - ``ExperimentalEnablePostMetadata`` setting was removed. Post metadata, including post dimensions, is now stored in the database to correct scroll position and eliminate scroll jumps as content loads in a channel.

**IMPORTANT:** If you upgrade from a release earlier than 5.11, please read the other [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html).

### Highlights

#### Infinite Scroll
 - Read messages more easily. Older posts are loaded automatically as you scroll up instead of having to click the "Load more messages" button at the top of the screen. This feature is not supported on Internet Explorer (IE11).
 
#### Bot Accounts
 - Users no longer have to rely on creating fake user accounts to act as bots for integrations. Instead, create a real bot account and use it to generate bot access tokens to interact with users and complete tasks.
 - Users can can also use these bots to post to any channel in the system, whether it’s a private team, private channel or a direct message channel.
 - For Enterprise deployments, bot accounts no longer count as an active user towards licensing subscriptions.
 - To learn more about bot accounts, see [the documentation](https://mattermost.com/pl/default-bot-accounts).
 
#### Jira Plugin 2.0
 - Enhanced existing plugin for a deep two-way integration between Jira and Mattermost.
 - Send notifications for Jira issue creation, issue updates and comments to Mattermost channels.
 - Users can also take quick actions in Mattermost, including creating Jira issues, attaching Mattermost messages to Jira issues, and transitioning issues via slash commands.
 - For a full feature set for 2.0, see https://github.com/mattermost/mattermost-plugin-jira#jira-20-features.
 
#### Pre-packaged Plugins
 - New pre-packaged plugins bundled with this Mattermost release include:
   - [GitHub plugin](https://github.com/mattermost/mattermost-plugin-github) for notifications, reminders and slash commands to stay up-to-date on issues and pull requests. Supports GitHub SaaS and Enterprise versions.
   - [Autolink plugin](https://github.com/mattermost/mattermost-plugin-autolink) to automatically hyperlink text, such as adding links to your issue tracker when someone posts an issue key or number.
   - [Custom Attributes plugin](https://github.com/mattermost/mattermost-plugin-custom-attributes) to add custom attributes in the user profile popover.
   - [Welcome Bot plugin](https://github.com/mattermost/mattermost-plugin-welcomebot) to improve onboarding and HR processes by adding a Welcome Bot that helps add new team members to channels.
   - [Amazon SNS CloudWatch plugin](https://github.com/mattermost/mattermost-plugin-aws-sns) to send alert notifications from [Amazon AWS CloudWatch](https://aws.amazon.com/cloudwatch/) to Mattermost channels via AWS SNS.

#### System Console Reorganization
 - Informational architecture restructure of the System Console to make a more logical flow to the settings and to provide a more cohesive experience for hiding features on the Mattermost Private Cloud product, where the system admin should not have access to change configurations that affect the environment directly.

#### Net Promoter Score (NPS)
 - We are gathering user feedback to help improve user experience and hear directly from our users. The feature can be disabled via **System Console > Plugins > Net Promoter Score**.
 
#### AD/LDAP Group Sync Removals (Enterprise Edition E20)
 - System Admins can manage the membership of private teams and channels with AD/LDAP groups, eliminating the need to individually add and remove members. Users in the groups are automatically removed from the team or channel when removed from an associated group.
 
#### User/Channel Search & Autocomplete in Elasticsearch (Enterprise Edition E20)
 - Added new settings in **System Console > Elasticsearch** to enable [Elasticsearch](https://about.mattermost.com/default-elasticsearch-documentation/) for autocompletion queries. When enabled, Elasticsearch uses its indexed data for user/channel search queries and autocomplete queries.

### Improvements

#### User Interface (UI)
 - Added an option to add a user to a channel from the profile popover.
 - Removed ``@`` for full name display in push notifications.
 
#### Plugins
 - Added support for Markdown in plugin System Console help text fields.
 - Added support for plugins to override ephemeral posts.

#### Localization
 - Promoted Polish language to "official".

#### Command Line Interface (CLI)
 - Added a ``command modify`` CLI command to modify slash commands.
 - Added a ``mattermost user convert --bot`` CLI command to convert user accounts to bot accounts.
 - Implemented a new command ``config migrate`` for migrating configuration to and from the database.
 - For AD/LDAP Group Sync, added the following CLI commands:
   - ``group team enable`` to add the ability to switch a team to be group-constrained.
   - ``group team disable``to add the ability to disable group constraint on the specified team.
   - ``group team list`` to list the groups associated with a team.
   - ``group team status`` to show the group constraint status of the specified team.
   - ``group channel enable`` to add the ability to switch a channel to be group-constrained.
   - ``group channel disable`` to disable group constraint on the specified channel.
   - ``group channel list`` to list the groups associated with a channel.
   - ``group channel status`` to show the group constraint status of the specified channel.
 
#### Administration
 - Added support for running two Mattermost instances on the same domain using subpaths.
 - Added support for importing threads from Slack.

### Bug Fixes
 - Fixed an issue where releasing a mouse click while the cursor was outside of the Rename Channel modal would close the modal.
 - Fixed an issue where a whitepage occured after uploading a plugin with an invalid ``settings_schema`` value.
 - Fixed an issue where the announcement banner overlapped channel content.
 - Fixed an issue where license expiration notice banner could not be dismissed prior to the license expiration date.
 - Fixed an issue where the channel switcher autocomplete didn't function properly when autocompleting the name of a person who was the first person named in a group message channel.
 - Fixed an issue where inline images in markdown preview didn't get expanded.
 - Fixed an issue where replies to the parent post were not left-aligned.
 - Fixed an issue where the timezone picker dropdown closed when trying to drag the scrollbar.
 - Fixed an issue where the ``ExperimentalPrimaryTeam`` config.json setting no longer hid the "Leave Team" option.
 - Fixed an issue where the setting position field for AD/LDAP sync in System Console did not block user from changing it in Account Settings.
 - Fixed an issue where scrolling was not working on iOS browser sign-up and sign-in pages.

### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:

 - Under ``"PluginSettings":`` in ``config.json``:
   - Added ``"EnableHealthCheck": true``, to ensure all plugins are periodically monitored, and restarted or deactivated based on their health status.
 - Under ``"NotificationLogSettings":`` in ``config.json``:
   - Added ``"EnableConsole": true``, ``"ConsoleLevel": "DEBUG"``, ``"ConsoleJson": true``, ``"EnableFile": true``, ``"FileLevel": "INFO"``, ``"FileJson": true``, and ``"FileLocation": ""``, to implement a structured logger to keep track of push notifications.
 - Under ``"ServiceSettings":`` in ``config.json``:
   - Added ``"EnableBotAccountCreation": false`` to enable bot account creation.
   - Added ``"DisableBotsWhenOwnerIsDeactivated": true`` to disable bots automatically when the owner is deactivated.
   - Added ``"TrustedProxyIPHeader": []``, to explicitly define which IP headers are trusted.

### Database Changes
 - `SchemeGuest` column added to the `TeamMembers` table.
 - `SchemeGuest` column added to the `ChannelMembers` table.
 - `DefaultTeamGuestRole` column added to the `Schemes` table, and set to an empty string.
 - `DefaultChannelGuestRole` column added to the `Schemes` table, and set to an empty string.

### API Changes

#### RESTful API v4 Changes
 - Updated API to use gziphandler wrapper if server is configured to use gzip. This ensures that the Mattermost server can respond to REST API requests with compressed data (via gzip) to reduce the amount of bandwidth used.
 - LDAP Group Sync:
    - Added API endpoints ``getGroupsByChannel`` and ``GetGroupsByTeam`` to retrieve groups by team and by channel.
    - Added ``group_constrained`` API to both ``/users`` and ``/users/search`` endpoints to be able to limit users listed to those allowed by group-constraints.
    - Added the ``GetGroups`` API endpoint to retrieve lists of groups with searching, pagination, and member counts.
 - Disabled Team InviteID modification via Create/Update actions and moved it to a dedicated API endpoint.
    
#### Plugin API v4 Changes
 - Added ``KVCompareAndSet(key string, old []byte, new []byte)`` to Plugin API to add support for transactional semantics with KV Store in plugin framework.

### Known Issues
 - Creating or attaching to Jira issues fails for Jira Cloud. This is resolved in v5.12.5.
 - Messages related to OpenGraph API are unnecessarily reported as errors in the server logs. This is resolved in v5.13.1.
 - **Push Notification Contents** setting is not available in the System Console in servers without an Enterprise Edition license. This is resolved in v5.13.1.
 - Channels with large message history may have performance issues. This is resolved in v5.13.2.
 - **Site Configuration > Notifications > Email Notification Contents** is missing from E10 servers. This is resolved in v5.13.2.
 - Changing announcement banner overlaps content. This is resolved in v5.13.2.
 - Scroll position is not at the new message indicator on switching channels with unreads between 30-60. This is resolved in v5.13.2.
 - Titles for webhooks, commands and OAuth apps are no longer bolded in the System Console.
 - Users can get logged out of server without a session expiry notification.
 - Desktop app hangs on opening emoji picker.
 - When a primary team is set, the options to leave a team is disabled for all teams, not just the primary team.
 - Plugin crashes the server when calling ``w.WriteHeader(0)``.
 - Bot account profile image disappears when saving bot details.
 - Custom emoji containing specified letters do not appear in emoji autocomplete, unless they start with the letters or have been returned in the autocomplete before.
 - Buttons inside ephemeral messages are not clickable / functional on the mobile app.
 - On a server using a subpath, the URL opens a blank page if the System Admin changes the Site URL in the System Console UI. To fix, the System Admin should restart the server.
 - Login does not work when Custom Terms of Service is enabled and MFA is enforced.
 - Google login fails on the Classic mobile apps.
 - Jump link in search results does not always jump to display the expected post.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Channel scroll position flickers while images and link previews load.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.

### Contributors
- [aeomin](https://translate.mattermost.com/user/aeomin/), [adzimzf](https://github.com/adzimzf), [amyblais](https://github.com/amyblais), [andresoro](https://github.com/andresoro), [asaadmahmood](https://github.com/asaadmahmood), [bolariin](https://github.com/bolariin), [bradjcoughlin](https://github.com/bradjcoughlin), [carmo-evan](https://github.com/carmo-evan), [chahat-arora](https://github.com/chahat-arora), [chikei](https://github.com/chikei), [cjohannsen81](https://github.com/cjohannsen81), [cometkim](https://github.com/cometkim), [comharris](https://github.com/comharris), [composednitin](https://github.com/composednitin), [CooperAtive](https://github.com/CooperAtive), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [d28park](https://github.com/d28park), [danmaas](https://github.com/danmaas), [deanwhillier](https://github.com/deanwhillier), [der-test](https://github.com/der-test), [DHaussermann](https://github.com/DHaussermann), [DSchalla](https://github.com/DSchalla), [dustinkirkland](https://github.com/dustinkirkland), [ejachang](https://github.com/ejachang), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [evan-a-a](https://github.com/evan-a-a), [farhadab](https://github.com/farhadab), [fjaeger](https://github.com/fjaeger), [gabrieljackson](https://github.com/gabrieljackson), [GianOrtiz](https://github.com/GianOrtiz), [giorgosdi](https://github.com/giorgosdi), [greensteve](https://github.com/greensteve), [gruceqq](https://translate.mattermost.com/user/gruceqq/), [grundleborg](https://github.com/grundleborg), [gupsho](https://github.com/gupsho), [hanzei](https://github.com/hanzei), [hectorskypl](https://github.com/hectorskypl), [henrymori](https://github.com/henrymori), [hmhealey](https://github.com/hmhealey), [icelander](https://github.com/icelander), [iomodo](https://github.com/iomodo), [IshankGulati](https://github.com/IshankGulati), [it33](https://github.com/it33), [ivanaairenee](https://github.com/ivanaairenee), [jasonblais](https://github.com/jasonblais), [JerryFireman](https://github.com/JerryFireman), [jesperhansen17](https://github.com/jesperhansen17), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [jkl5616](https://github.com/jkl5616), [johnthompson365](https://github.com/johnthompson365), [JtheBAB](https://github.com/JtheBAB), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [Kaya_Zeren](https://twitter.com/kaya_zeren), [kkirsche](https://github.com/kkirsche), [kosgrz](https://github.com/kosgrz), [Lena](https://translate.mattermost.com/user/Lena/), [letsila](https://github.com/letsila), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lindy65](https://github.com/lindy65), [lisakycho](https://github.com/lisakycho), [liusy182](https://github.com/liusy182), [marianunez](https://github.com/marianunez), [matshch](https://github.com/matshch), [meilon](https://github.com/meilon), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [migbot](https://github.com/migbot), [MikeNicholls](https://github.com/MikeNicholls), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [pichouk](https://github.com/pichouk), [pradeepmurugesan](https://github.com/pradeepmurugesan), [prapti](https://github.com/prapti), [pravan](https://github.com/pravan), [redg3ar](https://github.com/redg3ar), [reflog](https://github.com/reflog), [rodcorsi](https://github.com/rodcorsi), [rvillablanca](https://github.com/rvillablanca), [sapnasivakumar](https://github.com/sapnasivakumar), [saturninoabril](https://github.com/saturninoabril), [scottleedavis](https://github.com/scottleedavis), [seansackowitz](https://github.com/seansackowitz), [sebastien-prudhomme](https://github.com/sebastien-prudhomme), [sergeyzhukov](https://github.com/sergeyzhukov), [stylianosrigas](https://github.com/stylianosrigas), [sudheerDev](https://github.com/sudheerDev), [svelle](https://github.com/svelle), [tapaswenipathak](https://github.com/tapaswenipathak), [thekiiingbob](https://github.com/thekiiingbob), [thePanz](https://github.com/thePanz), [therealpuneeth20](https://github.com/therealpuneeth20), [torgeirl](https://github.com/torgeirl), [ulhosting](https://github.com/uhlhosting), [VolatianaYuliana](https://github.com/VolatianaYuliana), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [Wipeout55](https://github.com/Wipeout55), [z4cco](https://github.com/z4cco) 

## Release v5.11 - Quality Release

Mattermost v5.11.0 contains low level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

- **v5.11.1, released 2019-06-20** 
  - Mattermost v5.11.1 contains a medium level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
- **v5.11.0, released 2019-06-16**
  - Original 5.11.0 release

### Breaking changes since last release

 - If your integration uses ``Update.Props == nil`` to clear ``Props``, this will no longer work in 5.11+. Instead, use ``Update.Props == {}`` to clear properties. This change was made because ``Update.Props == nil`` unintentionally cleared all ``Props``, such as the profile picture, instead of preserving them.

**IMPORTANT:** If you upgrade from a release earlier than 5.10, please read the other [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html).

### Bug Fixes
 - Fixed an issue where plugin settings link didn't appear until refresh after uploading a plugin in the System Console.
 - Fixed an issue where **System Console** > **Users** bottom section of "user actions" menu was cut off for the last three users in the screen.
 - Fixed an issue where corners on image previews were squared instead of rounded.
 - Fixed an issue where the hover effect was missing on images.
 - Fixed an issue where a post action (via button or menu) reset the profile picture of the webhook post.
 - Fixed an issue where a flagged post containing only file attachments didn't render in the sidebar until loaded in the centre.
 - Fixed an issue where some strings in channel settings weren't localizable.
 - Fixed an issue where clicking "Open" downloaded an image instead of opening it.
 - Fixed an issue where an at-mention user autocomplete overlapped with the channel header when drafting a long message containing a file attachment.
 - Fixed an issue where the reply bar showed gaps between posts in compact view.
 - Fixed an issue where markdown preview of nested lists displayed differently from styling in posted message.
 - Fixed an issue where Safari suggested auto-corrections in the channel switcher.
 - Fixed an issue on Safari where the mention badge count didn't update immediately.
 - Fixed an issue where the post action menu overlapped with posts on iOS/Safari on mobile view.
 - Fixed an issue where interactive dialog's description text colour was difficult to see on dark themes.
 - Fixed an issue where delete permissions for custom emoji team admin role were not always granted.
 - Fixed an issue with a slight scroll pop on reaching loading indictor of search results.
 - Fixed an issue where adding a user to a channel that is in the unreads section caused the channel to become read in the user's view.
 - Fixed an issue where the channel menu dropdown icon had an unnecessary tooltip.
 - Fixed an issue on LDAP Groups where adding a group to a team provided an unnecessary permission confirmation modal.
 - Fixed an issue on mobile view where clicking on the attachment icon didn't bring up the dropdown menu.

### Known Issues
 - Buttons inside ephemeral posts are not clickable / functional on the mobile app.
 - On a server using a subpath, the URL opens a blank page if the system admin changes the Site URL in the System Console UI. The system admin should restart the server to fix it.
 - Login does not work when Custom Terms of Service is enabled and MFA is enforced.
 - Google login fails on the Classic mobile apps.
 - Jump link in search results does not always jump to display the expected post.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Channel scroll position flickers while images and link previews load.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 
### Contributors

Thank you to everyone who contributed to the Mattermost project in April 2019!

[aeomin](https://translate.mattermost.com/user/aeomin/), [akrfjmt](https://github.com/akrfjmt), [ali-farooq0](https://github.com/ali-farooq0), [amyblais](https://github.com/amyblais), [andresoro](https://github.com/andresoro), [asaadmahmood](https://github.com/asaadmahmood), [BotKube](https://www.botkube.io/), [bradjcoughlin](https://github.com/bradjcoughlin), [bytemine GmbH](https://github.com/bytemine), [chikei](https://github.com/chikei), [cometkim](https://github.com/cometkim), [comharris](https://github.com/com/comharris), [CooperAtive](https://github.com/CooperAtive), [coreyhulen](https://github.com/coreyhulen), [courtneypattison](https://github.com/courtneypattison), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [d28park](https://github.com/d28park), [danmaas](https://github.com/danmaas), [deanwhillier](https://github.com/deanwhillier), [der-test](https://github.com/der-test), [DHaussermann](https://github.com/DHaussermann), [DSchalla](https://github.com/DSchalla), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [fcorrea](https://github.com/fcorrea), [gabrieljackson](https://github.com/gabrieljackson), [gnufede](https://github.com/gnufede), [gruceqq](https://translate.mattermost.com/user/gruceqq/), [grundleborg](https://github.com/grundleborg), [hanzei](https://github.com/hanzei), [happygaijin](https://github.com/happygaijin), [harshilsharma](https://github.com/harshilsharma), [hectorskypl](https://github.com/hectorskypl), [Herzum](https://github.com/herzum), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [johnbellone](https://github.com/johnbellone), [johnthompson365](https://github.com/johnthompson365), [JVasky](https://github.com/JVasky), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [Kaya_Zeren](https://twitter.com/kaya_zeren), [kingisaac95](https://github.com/kingisaac95), [kmandagie](https://github.com/kmandagie), [kosgrz](https://github.com/kosgrz), [Lena](https://translate.mattermost.com/user/Lena/), [levb](https://github.com/levb), [lfbrock](https://github.com/lfbrock), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [liusy182](https://github.com/liusy182), [ljmccaff](https://github.com/ljmccaff), [Mario-Hofstaetter](https://github.com/Mario-Hofstaetter), [meilon](https://github.com/meilon), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [migbot](https://github.com/migbot), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [MParvin](https://github.com/MParvin), [mstoli](https://github.com/mstoli), [ninanung](https://github.com/ninanung), [oliverJurgen](https://github.com/oliverJurgen), [PeterDaveHello](https://github.com/PeterDaveHello), [prapti](https://github.com/prapti), [reflog](https://github.com/reflog), [rodcorsi](https://github.com/rodcorsi), [RyPoints](https://github.com/RyPoints), [s4kh](https://github.com/s4kh), [sapnasivakumar](https://github.com/sapnasivakumar), [saturninoabril](https://github.com/saturninoabril), [scottleedavis](https://github.com/scottleedavis), [Sheshagiri](https://github.com/Sheshagiri), [stylianosrigas](https://github.com/stylianosrigas), [sudheerDev](https://github.com/sudheerDev), [svelle](https://github.com/svelle), [tengis617](https://github.com/tengis617), [thekiiingbob](https://github.com/thekiiingbob), [thePanz](https://github.com/thepanz), [thepill](https://github.com/thepill), [therealpuneeth20](https://github.com/therealpuneeth20), [ThiefMaster](https://github.com/ThiefMaster), [torgeirl](https://github.com/torgeirl), [tylarb](https://github.com/tylarb), [ulhosting](https://github.com/uhlhosting), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [z4cco](https://github.com/z4cco) 

## Release v5.10 - Feature Release

Mattermost v5.10.0 contains medium to high level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

- **v5.10.2, released 2019-06-20** 
  - Mattermost v5.10.2 contains a medium level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
- **v5.10.1, released 2019-05-16** 
  - Fixed an issue on Internet Explorer (IE11) where the system console opened a blank page.
- **v5.10.0, released 2019-04-16**
  - Original 5.10.0 release

### Breaking changes since last release

 - ``SupportedTimezonesPath`` setting in config.json and changes to timezones in the UI based on the timezones.json file was removed. This was made to support [storing configurations in the database](https://docs.mattermost.com/administration/config-in-database.html#configuration-in-the-mattermost-database).

**IMPORTANT:** If you upgrade from a release earlier than 5.9, please read the other [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html).

### Highlights
 
#### Interactive Ephemeral Messages
 - Added support for [message actions and buttons](https://docs.mattermost.com/developer/interactive-messages.html) in ephemeral messages.

#### Configuration in Database
 - Added experimental support for storing ``config.json`` in the database, improving the system console experience on read-only filesystems. Storing the configuration in the database is optional, as the existing ``config.json`` remains fully supported.

### Improvements

#### User Interface (UI)
 - Added ability to use "c" and "sh" for code block syntax highlighting.
 - Words that trigger mentions now supports Chinese.
 - Added support for rendering emojis and hyperlinks in message attachment titles.
 - Added support for showing the channel name in the message box.
 - Added support for markdown in plugin system console help text fields.
 - Added ability to convert Excel cells to markdown table when pasting in Mattermost.
 - Added ability to render emojis in interactive message buttons.
 
#### Plugins (Beta)
 - Created a plugin component to override file previews.
 - Added support for plugins to create link tooltips.
 - Added experimental support for plugins to use bot accounts.
 
#### Bulk Import/Export
 - Added User Preference fields in bulk export.
 - Added ability to include direct and group message channels and their posts in bulk export.
 - Added ability to include deactivated users in bulk import.
 
#### Command Line Tools (CLI)
 - Created CLI command ``command show`` to allow seeing detailed information of a slash command.
 - Created CLI command ``webhook show`` to allow seeing detailed information of a webhook.
 - Created CLI command ``team rename`` to allow renaming teams.
 - Created CLI command ``channel search`` to allow searching for channels.
 
#### Administration
 - Improved default session timeout behavour, including changing the default ``SessionLengthWebInDays`` from 30 to 180 days.
 - Added full text search to the system console panel to easily find options in the configuration.
 - (Advanced Permissions) Split managing emoji permissions into "create", "delete own" and "delete others".
 - (Advanced Permissions) Added ``List_Public_Teams``, ``Join_Public_Teams``, ``List_Private_Teams`` and ``Join_Private_Teams`` permissions.
 - Added support for LDAP groups search.
 - Added a setting to the system console to change the minimum length of hashtags.
 - Added support for setting Reply-To header in outbound Mattermost emails.
 - Added support for invalidating all email invitations from the system console.

### Bug Fixes
 - Fixed an issue where enterprise features became immediately unavailable when the enterprise license expired with a 15 day grace period.
 - Fixed an issue where an at-mention for username that starts with "all" did not highlight their entire username.
 - Fixed an issue where the ``migrate_auth`` command did not work with valid license file.
 - Fixed an issue where post metadata was requested if link previews were disabled.
 - Fixed an issue where a channel did not get removed from the unreads section if the user navigated out of it via a permalink.
 - Fixed an issue where a link from Access Control Groups to Group Filter on AD/LDAP did not work for subpath Site URL.
 - Fixed an issue where expired channels appeared in "My Channels" section of channel switcher if using the **Automatically Close Direct Messages** setting.
 - Fixed an issue where the text box reverted to default size after a user returned from the Integrations page.
 - Fixed an issue where the profile popover wasn't allowed to close itself when opened through an at-mention.
 - Fixed an issue where filtering by first name with Korean characters no longer worked for at-mentions.
 - Fixed an issue where the **Remove MFA** option was visible for all users when **Enforce MFA** was enabled.
 
### Compatibility

#### Deprecated Features

 - Deprecated configurable ``timezones.json`` in favour of the existing hard-coded list built into the server.

### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.
 
#### Changes to Team Edition and Enterprise Edition:

- Under ``"ExperimentalSettings":`` in ``config.json``:
   - Added ``"RestrictSystemAdmin": false``, to optionally constrain even system admins from changing critical settings.
- Under ``"ServiceSettings":`` in ``config.json``:
   - Added ``"MinimumHashtagLength": 3``, to add the ability to change the minimum length of hashtags.

### RESTful API Changes
 - Added ``GetUsers`` API method to add the ability to list users.
 - Added ``POST /bots`` to create a bot accounts.
 - Added ``PUT /bots/{bot_user_id}`` to partially update a bot by providing only the fields you want to update.
 - Added ``GET /bots/{bot_user_id}`` to get a bot specified by its bot id.
 - Added ``GET /bots`` to get a page of a list of bots.
 - Added ``POST /bots/{bot_user_id}/disable`` to disable a bot.
 - Added ``POST /bots/{bot_user_id}/enable`` to enable a bot.
 - Added ``POST /bots/{bot_user_id}/assign/{user_id}`` to assign a bot to the specified user.

### Plugin API Changes
 - Added the ``SearchPostsInTeam`` method to add the ability to search posts in a team.
 - Added ``GetTeamMembersForUser`` and ``GetChannelMembersForUser`` to add the ability to get team and channel members for a specific user.
 - Added ``GetBundleInfo() string`` method to add the ability to store assets elsewhere.
 - Added ``CreateBot(bot *model.Bot) (*model.Bot, *model.AppError)`` to create the given bot and corresponding user.
 - Added ``PatchBot(botUserId string, botPatch *model.BotPatch) (*model.Bot, *model.AppError)`` to apply the given patch to the bot and corresponding user.
 - Added ``GetBot(botUserId string, includeDeleted bool) (*model.Bot, *model.AppError)`` to return the given bot.
 - Added ``GetBots(options *model.BotGetOptions) ([]*model.Bot, *model.AppError)`` to return the requested page of bots.
 - Added ``UpdateBotActive(botUserId string, active bool) (*model.Bot, *model.AppError)`` to mark a bot as active or inactive, along with its corresponding user.
 - Added ``PermanentDeleteBot(botUserId string) *model.AppError`` to permanently delete a bot and its corresponding user.

### Database Changes
 - Granted the following permissions for the System Admin, in preparation for an upcoming bot accounts feature:
   - PERMISSION_CREATE_BOT
   - PERMISSION_READ_BOTS
   - PERMISSION_READ_OTHERS_BOTS
   - PERMISSION_MANAGE_BOTS
   - PERMISSION_MANAGE_OTHERS_BOTS
 - `Bots` table was added.

### Known Issues
 - Attachments menu on mobile view is partly cut off on the right-hand side.
 - Clicking on the attachment icon doesn't bring up the dropdown menu on mobile browser.
 - Content for ephemeral messages is not displayed on mobile apps.
 - When login is done through SAML, text in **Account Settings** > **General** > **Email** is misaligned.
 - On a server using a subpath, the URL opens a blank page if the system admin changes the Site URL in the System Console UI. The system admin should restart the server to fix it.
 - Login does not work when Custom Terms of Service is enabled and MFA is enforced.
 - Google login fails on the Classic mobile apps.
 - Jump link in search results does not always jump to display the expected post.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Channel scroll position flickers while images and link previews load.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 
### Contributors

Thank you to everyone who contributed to the Mattermost project in March 2019!

- [7-plus-t](https://github.com/7-plus-t), [aeomin](https://translate.mattermost.com/user/aeomin/), [ali-farooq0](https://github.com/ali-farooq0), [amaddio](https://github.com/amaddio), [amyblais](https://github.com/amyblais), [asaadmahmood](https://github.com/asaadmahmood), [avasconcelos114](https://github.com/avasconcelos114), [bcalik](https://github.com/bcalik), [benschuster788](https://github.com/benschuster788), [bradjcoughlin](https://github.com/bradjcoughlin), [checkaayush](https://github.com/checkaayush), [chetanyakan](https://github.com/chetanyakan), [chikei](https://github.com/chikei), [comharris](https://github.com/comharris), [courtneypattison](https://github.com/courtneypattison), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [d28park](https://github.com/d28park), [danmaas](https://github.com/danmaas), [dchukmasov](https://github.com/dchukmasov), [deanwhillier](https://github.com/deanwhillier), [der-test](https://github.com/der-test), [DHaussermann](https://github.com/DHaussermann), [DSchalla](https://github.com/DSchalla), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [fcorrea](https://github.com/fcorrea), [gnufede](https://github.com/gnufede), [grundleborg](https://github.com/grundleborg), [gruceqq](https://translate.mattermost.com/user/gruceqq/), [gulhe](https://github.com/gulhe), [gupsho](https://github.com/gupsho), [hanzei](https://github.com/hanzei), [harshilsharma](https://github.com/harshilsharma), [hectorskypl](https://github.com/hectorskypl), [hmhealey](https://github.com/hmhealey), [Hobby-Student](https://github.com/Hobby-Student), [it33](https://github.com/it33), [j8r](https://github.com/j8r), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jk2K](https://github.com/jk2K), [johnsenner](https://github.com/johnsenner), [JtheBAB](https://github.com/JtheBAB), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [Kaya_Zeren](https://twitter.com/kaya_zeren), [kelvintyb](https://github.com/kelvintyb), [kjkeane](https://github.com/kjkeane), [kosgrz](https://github.com/kosgrz), [Lena](https://translate.mattermost.com/user/Lena/), [letsila](https://github.com/letsila), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [m3phistopheles](https://github.com/m3phistopheles), [MartB](https://github.com/MartB), [meilon](https://github.com/meilon), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [migbot](https://github.com/migbot), [MirlanMaksv](https://github.com/MirlanMaksv), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [nadaa](https://github.com/nadaa), [oliverJurgen](https://github.com/oliverJurgen), [pesintta](https://github.com/pesintta), [reflog](https://github.com/reflog), [rodcorsi](https://github.com/rodcorsi), [Roy-Orbison](https://github.com/Roy-Orbison), [sadohert](https://github.com/sadohert), [sandlis](https://github.com/sandlis), [saturninoabril](https://github.com/saturninoabril), [stylianosrigas](https://github.com/stylianosrigas), [sudheerDev](https://github.com/sudheerDev), [svelle](https://github.com/svelle), [tejasbubane](https://github.com/tejasbubane), [thekiiingbob](https://github.com/thekiiingbob), [thePanz](https://github.com/thepanz), [ulhosting](https://github.com/uhlhosting), [wbernest](https://github.com/wbernest), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [yuya-oc](https://github.com/yuya-oc)

## Release v5.9 - [ESR](https://docs.mattermost.com/administration/extended-support-release.html)

Mattermost v5.9.0 contains low to medium level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

- **v5.9.5, released 2019-10-12**  
  - Fixed an issue that will be introduced with a change in upcoming server v5.16 and desktop app v4.3 releases where desktop notifications will be broken as the desktop app will no longer be able to directly interact with the web app. [MM-18819](https://mattermost.atlassian.net/browse/MM-18819)
- **v5.9.4, released 2019-08-22** 
  - Mattermost v5.9.4 contains a medium level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
- **v5.9.3, released 2019-07-19** 
  - Fixed an issue with unauthenticated LDAP bind. [MM-17055](https://mattermost.atlassian.net/browse/MM-17055)
- **v5.9.2, released 2019-06-20** 
  - Mattermost v5.9.2 contains a medium level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
- **v5.9.1, released 2019-04-24** 
  - Mattermost v5.9.1 contains a high level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
- **v5.9.0, released 2019-03-16**
  - Original 5.9.0 release
  
### Breaking Changes since last release

 - If **DisableLegacyMfa** setting in ``config.json`` is set to ``true`` and multi-factor authentication is enabled, ensure your users have upgraded to mobile app version 1.17 or later. Otherwise, users who have MFA enabled may not be able to log in successfully. See [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html) for more details.
 - The public IP of the Mattermost application server is considered a reserved IP for additional security hardening in the context of untrusted external requests such as Open Graph metadata, webhooks or slash commands. See [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html) for more details.

**IMPORTANT:** If you upgrade from another release than 5.8, please read the [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html).

### Bug Fixes

 - Fixed an issue where emoji reactions did not appear on posts right away.
 - Fixed an issue where the emoji `Recently Used` cleared entirely after logging out and back in.
 - Fixed an issue where emoji not included in our list of text-based emoji were not rendered as jumboemoji.
 - Fixed an issue where the default server/client locales got reverted to ``en`` on server startup.
 - Fixed an issue where email notification setting in the webapp was out of sync with the mobile apps.
 - Fixed an issue where a broken image displayed on login page if custom branding was enabled but no image had been uploaded.
 - Fixed an issue where at-channel, at-all, at-here followed by a period were not highlighted as mentions.
 - Fixed an issue where the Mattermost icon was pixelated in bookmark rendering on Google Chrome.
 - Fixed an issue where **System Console > Users** page had broken user interface on narrow screens.
 - Fixed an issue where at-channel notification showed incorrect number of timezones.
 - Fixed an issue where leading whitespace with emoji affected emoji size so that they didn't render as jumboemoji.
 - Fixed an issue where the System Console graphs did not load smoothly.
 - Fixed an issue with inconsistent formatting in page header on **System Console > Notifications > Mobile Push**.
 - Fixed an issue where invite tokens with a 48-hour expiry expired after 24 hours.
 - Fixed an issue where a blank screen appeared when opening a group message channel from "More" modal using Enter key.
 - Fixed an issue where Zoom plugin caused link metadata code to print warnings in the System Console.

### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.
 
#### Changes to Team Edition and Enterprise Edition:
 
 - **Enable Image Proxy** setting is now ``false`` by default. See [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html) for more details.
 - Under ``"ServiceSettings"`` in ``config.json``:
    - Added ``"DisableLegacyMFA": false,`` to keep the legacy checkMfa endpoint enabled to support mobile versions 1.16 and earlier. See [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html) for more details.

### Known Issues

 - On a server using a subpath, the URL opens a blank page if the system admin changes the Site URL in the System Console UI. The system admin should restart the server to fix it.
 - Login does not work when Custom Terms of Service is enabled and MFA is enforced.
 - Google login fails on the Classic mobile apps.
 - User can receive a video call from another browser tab while already on a call.
 - Jump link in search results does not always jump to display the expected post.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Channel scroll position flickers while images and link previews load.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - CTRL/CMD+U shortcut to upload a file doesn’t work on Firefox.
 
### Contributors

Thank you to everyone who contributed to the Mattermost project in February 2019!

[adzimzf](https://github.com/adzimzf), [aeomin](https://translate.mattermost.com/user/aeomin/), [amyblais](https://github.com/amyblais), [asaadmahmood](https://github.com/asaadmahmood), [aswathkk](https://github.com/aswathkk), [awbraunstein](https://github.com/awbraunstein), [bbodenmiller](https://github.com/bbodenmiller), [BK1603](https://github.com/BK1603), [bradjcoughlin](https://github.com/bradjcoughlin), [chikei](https://github.com/chikei), [cometkim](https://github.com/cometkim), [comharris](https://github.com/comharris), [courtneypattison](https://github.com/courtneypattison), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [danmaas](https://github.com/danmaas), [dannymohammad](https://github.com/dannymohammad), [deanwhillier](https://github.com/deanwhillier), [der-test](https://github.com/der-test), [DHaussermann](https://github.com/DHaussermann), [dom3k](https://github.com/dom3k), [dos1701](https://github.com/dos1701), [DSchalla](https://github.com/DSchalla), [ejachang](https://github.com/ejachang), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [fcorrea](https://github.com/fcorrea), [gabrieljackson](https://github.com/gabrieljackson), [gruceqq](https://translate.mattermost.com/user/gruceqq/), [gupsho](https://github.com/gupsho), [hannaparks](https://github.com/hannaparks), [hanzei](https://github.com/hanzei), [hectorskypl](https://github.com/hectorskypl), [hmhealey](https://github.com/hmhealey), [icelander](https://github.com/icelander), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jdillard](https://github.com/jdillard), [jespino](https://github.com/jespino), [jfcastroluis](https://github.com/jfcastroluis), [jfrerich](https://github.com/jfrerich), [JtheBAB](https://github.com/JtheBAB), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [Kaya_Zeren](https://twitter.com/kaya_zeren), [kosgrz](https://github.com/kosgrz), [koukouloforos](https://github.com/koukouloforos), [kscheel](https://github.com/kscheel), [Lena](https://translate.mattermost.com/user/Lena/), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [manland](https://github.com/manland), [maruTA-bis5](https://github.com/maruTA-bis5), [meilon](https://github.com/meilon), [mgdelacroix](https://github.com/mgdelacroix), [migbot](https://github.com/migbot), [MirlanMaksv](https://github.com/MirlanMaksv), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [onnadi-work](https://github.com/onnadi-work), [patniharshit](https://github.com/patniharshit), [pichouk](https://github.com/pichouk), [R-Wang97](https://github.com/R-Wang97), [Robbe7730](https://github.com/Robbe7730), [rodcorsi](https://github.com/rodcorsi), [sadohert](https://github.com/sadohert), [sandlis](https://github.com/sandlis), [sanojsubran](https://github.com/sanojsubran), [saturninoabril](https://github.com/saturninoabril), [staabm](https://github.com/staabm), [sudheerDev](https://github.com/sudheerDev), [svelle](https://github.com/svelle), [tauu](https://github.com/tauu), [thedingwing](https://github.com/thedingwing), [thePanz](https://github.com/thepanz), [ulhosting](https://github.com/uhlhosting), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [yuya-oc](https://github.com/yuya-oc), [zetaab](https://github.com/zetaab)

## Release v5.8 - Feature Release

Mattermost v5.8.0 contains low to high level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

- **v5.8.2, released 2019-04-24** 
  - Mattermost v5.8.2 contains a high level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
- **v5.8.1, released 2019-03-16** 
  - Mattermost v5.8.1 contains a medium level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
  - Turned image proxy off by default, unless a server already had it enabled (including new installs). Also, warnings about not getting embedded content for a post were downgraded or removed. See [important upgrade notes](https://docs.mattermost.com/administration/important-upgrade-notes.html) for more details.
- **v5.8.0, released 2019-02-16**
  - Original 5.8.0 release

### Breaking Changes since last release

- The local image proxy has been added, and images displayed within the client are now affected by the ``AllowUntrustedInternalConnections`` setting. See [documentation](https://docs.mattermost.com/administration/image-proxy.html#local-image-proxy) for more details if you have trouble loading images.

**IMPORTANT:** If you upgrade from another release than 5.7, please read the [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html).

### Highlights

#### Added support for LDAP Group Sync
 - Lets admins set default team and channel membership based on LDAP groups. See more details [in the documentation](https://docs.mattermost.com/deployment/ldap-group-sync.html).

#### Added multi-factor authentication support to Team Edition
 - See more details on [this Forum post](https://forum.mattermost.org/t/multi-factor-authentication-mfa-in-team-edition/6287).
 
#### Enhanced image performance
 - Improved performance for images by adding support for image proxy servers, which are now integrated into the server and switched on by default.
 - Note that this may cause problems loading images from within your local network due to security settings. See [here](https://docs.mattermost.com/administration/image-proxy.html#local-image-proxy) for more information.

### Improvements

#### User Interface (UI)
 - Improved sorting of emoji in the emoji autocomplete and emoji picker search results.
 - Added support for emoji picker for mobile web view.

#### Notifications
 - Added a channel notification setting to disable at-channel mentions.
 
#### Administration
 - Added the ability to search users by role in **System Console** > **Users**.
 - Added a CLI command to modify an outgoing webhook.
 - Added a CLI command to restore a team.

#### Performance
 - Added network connectivity improvements where the server no longer allows clients to auto-retry posts and to cause posts to appear twice.

#### Slash Commands
 - Added support for sending a message to a different channel than where the slash command was issued from.
 - Added an option to send a message beginning with a "/" from the right-hand side.

#### Plugins
 - Added server support for updating a plugin instead of having to remove and install them as two separate actions.
 
#### Attachments
 - Optimized file attachment memory usage where possible.

### Bug Fixes
 
 - Fixed an issue where "[user] is typing ..." was not removed when a message was composed and sent very quickly.
 - Fixed an issue where an announcement banner displayed when the banner was enabled but the text field was blank.
 - Fixed an issue where a language was not set if selected in Account Settings.
 - Fixed an issue where removing rows from Send Email Invite modal didn't remove them immediately.

### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.
 
#### Changes to Team Edition and Enterprise Edition:
 
 - Under ``"ServiceSettings"`` in ``config.json``:
    - Added ``"ExperimentalLdapGroupSync": false``, to add support for experimental LDAP Group Sync feature. 
 - Under ``"LdapSettings"`` in ``config.json``:  
    - Added ``"GroupFilter": ""``, ``"GroupDisplayNameAttribute": ""`` and ``"GroupIdAttribute": ""``, to add the ability to configure group display name and unique identifier.
 - Under ``"ImageProxySettings":`` in ``config.json``:
    - Added ``"Enable": true,``, ``"ImageProxyType": "local",``, ``"RemoteImageProxyURL": "",`` and ``"RemoteImageProxyOptions": ""``, to allow integrating image proxy into the server and switching it on by default.
 - Under ``"ExperimentalSettings":`` in ``config.json``:
    - Added ``"LinkMetadataTimeoutMilliseconds": 5000`` and ``"DisablePostMetadata": false``, to enable post metadata by default.

### API Changes

#### RESTful API v4 Changes
 - Added ``SearchTeams`` to plugin API to add the ability to search teams.
 - Added ``GetTeamStats`` to plugin API to add the ability to get team statistics.
 - Added ``/api/v4/posts/ids/reactions`` API endpoint to get the bulk reactions for posts.
 - Added ``UpdateUserActive`` to plugin API to allow updating user's status as active or inactive.
 - Add ``GetFile`` to plugin to add the ability to get files.

### Known Issues

 - On a server using a subpath, the URL opens a blank page if the system admin changes the Site URL in the System Console UI. The system admin should restart the server to fix it.
 - Login does not work when Custom Terms of Service is enabled and MFA is enforced.
 - Google login fails on the Classic mobile apps.
 - User can receive a video call from another browser tab while already on a call.
 - Jump link in search results does not always jump to display the expected post.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Channel scroll position flickers while images and link previews load.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - CTRL/CMD+U shortcut to upload a file doesn’t work on Firefox.
 
### Contributors

Thank you to everyone who contributed to the Mattermost project in January 2019!
 
[adzimzf](https://github.com/adzimzf), [aeomin](https://translate.mattermost.com/user/aeomin/), [amorriscode](https://github.com/amorriscode), [amyblais](https://github.com/amyblais), [ArchRoller](https://github.com/archroller), [asaadmahmood](https://github.com/asaadmahmood), [avasconcelos114](https://github.com/avasconcelos114), [bradjcoughlin](https://github.com/bradjcoughlin), [chikei](https://github.com/chikei), [cometkim](https://github.com/cometkim), [comharris](https://github.com/comharris), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [cvitter](https://github.com/cvitter), [danmaas](https://github.com/danmaas), [dannymohammad](https://github.com/dannymohammad), [deanwhillier](https://github.com/deanwhillier), [der-test](https://github.com/der-test), [DHaussermann](https://github.com/DHaussermann), [dmamills](https://github.com/dmamills), [dom3k](https://github.com/dom3k), [DSchalla](https://github.com/DSchalla), [dv29](https://github.com/dv29), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [gabrieljackson](https://github.com/gabrieljackson), [grundleborg](https://github.com/grundleborg), [hanzei](https://github.com/hanzei), [hmhealey](https://github.com/hmhealey), [icelander](https://github.com/icelander), [it33](https://github.com/it33), [ja11sop](https://github.com/ja11sop), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [JtheBAB](https://github.com/JtheBAB), [JustinReynolds-MM](https://github.com/JustinReynolds-MM), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [Kaya_Zeren](https://twitter.com/kaya_zeren), [kosgrz](https://github.com/kosgrz), [Lena](https://translate.mattermost.com/user/Lena/), [levb](https://github.com/levb), [lfbrock](https://github.com/lfbrock), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lindy65](https://github.com/lindy65), [maruTA-bis5](https://github.com/maruTA-bis5), [meilon](https://github.com/meilon), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [migbot](https://github.com/migbot), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [mollyyoung](https://github.com/mollyyoung), [nashik](https://github.com/nashik), [nlowe](https://github.com/nlowe), [Ovski4](https://github.com/Ovski4), [pichouk](https://github.com/pichouk), [pjgrizel](https://github.com/pjgrizel), [pradeepmurugesan](https://github.com/pradeepmurugesan), [robert843](https://github.com/robert843), [rodcorsi](https://github.com/rodcorsi), [rononline](https://github.com/rononline), [ryoon](https://github.com/ryoon), [s4kh](https://github.com/s4kh), [sadohert](https://github.com/sadohert), [sapnasivakumar](https://github.com/sapnasivakumar), [saturninoabril](https://github.com/saturninoabril), [Sheshagiri](https://github.com/Sheshagiri), [sonasingh46](https://github.com/sonasingh46), [sudheerDev](https://github.com/sudheerDev), [svelle](https://github.com/svelle), [thePanz](https://github.com/thepanz), [tomocy](https://github.com/tomocy), [ulhosting](https://github.com/uhlhosting), [unigiriunini](https://github.com/unigiriunini), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [yuya-oc](https://github.com/yuya-oc), [zeroimpl](https://github.com/zeroimpl), [zetaab](https://github.com/zetaab)
 
## Release v5.7 - Quality Release

Mattermost v5.7.0 contains low to medium level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

- **v5.7.3, released 2019-03-16** 
  - Mattermost v5.7.3 contains a medium level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
- **v5.7.2, released 2019-02-16** 
  - Mattermost v5.7.2 contains low to medium level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
- **v5.7.1, released 2019-02-01** 
  - Mattermost v5.7.1 contains a high level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
- **v5.7.0, released 2019-01-16**
  - Original 5.7.0 release

### Bug Fixes

 - Fixed an issue where push notification to clear unread messages badge from another client was not being forwarded. There are cases on the mobile app where the badge could still linger - see [MM-13722](https://mattermost.atlassian.net/browse/MM-13722) for more details.
 - Fixed a SQL syntax error when a non-existent channelId was attempted to be viewed.
 - Fixed an issue where OpenGraph and Post Metadata cache were purged on any config change with the image proxy enabled.
 - Added a check for percent value on file upload progress to prevent the app from crashing.
 - Fixed an issue where multi-line announcement banner text did not expand its background.
 - Fixed an issue where channel modal text and icons were misaligned if only one channel type was available.
 - Fixed an issue where every channel switch triggered a fetch for users in all Group Message channels for the user.
 - Fixed an issue where the user was not redirected to sign up page to create first account on fresh install.
 - Fixed an issue where scrollbar appeared in team sidebar when a user was a member of too many teams.
 - Fixed an issue where wide images posted by a webhook could be cut off on the right-hand side.
 - Fixed an issue where leaving a team showed a 403 error in the console.
 - Fixed an issue where Code Theme did not save unless other colours were changed.
 - Fixed an issue where Webapp only showed a star or mention count for active team.
 - Fixed an issue where Web mobile view was missing the mute option in the channel menu.
 - Fixed an issue where the "participant is typing" appeared a few seconds after a message was posted.
 - Fixed an issue where a profile popover got cut off on the right-hand side if it included an admin badge and a long username.

### Known Issues

 - Custom Terms of Service returns on refresh after clicking to agree.
 - Google login fails on the Classic mobile apps.
 - User can receive a video call from another browser tab while already on a call.
 - Jump link in search results does not always jump to display the expected post.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Channel scroll position flickers while images and link previews load.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - CTRL/CMD+U shortcut to upload a file doesn’t work on Firefox.

### Contributors

[aeomin](https://github.com/aeomin), [akhilanandbv003](https://github.com/akhilanandbv003), [amyblais](https://github.com/amyblais), [andrewbanchich](https://github.com/andrewbanchich), [ArchRoller](https://github.com/archroller), [asaadmahmood](https://github.com/asaadmahmood), [bezumkin](https://github.com/bezumkin), [bradjcoughlin](https://github.com/bradjcoughlin), [chetanyakan](https://github.com/chetanyakan), [chikei](https://github.com/chikei), [cometkim](https://github.com/cometkim), [comharris](https://github.com/comharris), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [cvitter](https://github.com/cvitter), [danmaas](https://github.com/danmaas), [der-test](https://github.com/der-test), [DHaussermann](https://github.com/DHaussermann), [DSchalla](https://github.com/DSchalla), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [grundleborg](https://github.com/grundleborg), [hanzei](https://github.com/hanzei), [hmhealey](https://github.com/hmhealey), [icelander](https://github.com/icelander), [it33](https://github.com/it33), [ja11sop](https://github.com/ja11sop), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [johnthompson365](https://github.com/johnthompson365), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [kosgrz](https://github.com/kosgrz), [Lena](https://translate.mattermost.com/user/Lena/), [letsila](https://github.com/letsila), [levb](https://github.com/levb), [lfbrock](https://github.com/lfbrock), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [meilon](https://github.com/meilon), [mickmister](https://github.com/mickmister), [migbot](https://github.com/migbot), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [mukulrawat1986](https://github.com/mukulrawat1986), [pichouk](https://github.com/pichouk), [pjgrizel](https://github.com/pjgrizel), [robert843](https://github.com/robert843), [rodcorsi](https://github.com/rodcorsi), [rononline](https://github.com/rononline), [ryoon](https://github.com/ryoon), [s4kh](https://github.com/s4kh), [saturninoabril](https://github.com/saturninoabril), [Schrooms](https://github.com/Schrooms), [sudheerDev](https://github.com/sudheerDev), [svelle](https://github.com/svelle), [thePanz](https://github.com/thePanz), [uhlhosting](https://github.com/uhlhosting), [vaithak](https://github.com/vaithak), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [yakimant](https://github.com/yakimant), [yuya-oc](https://github.com/yuya-oc) 

## Release v5.6 - Feature Release

- **v5.6.5, released 2019-02-16** 
  - Mattermost v5.6.5 contains low to medium level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
- **v5.6.4, released 2019-02-01** 
  - Mattermost v5.6.4 contains a high level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
- **v5.6.3, released 2019-01-16**
  - Mattermost v5.6.3 contains medium level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
- **v5.6.2, released 2018-12-22** 
  - Fixed JIRA plugin not sending messages back to Mattermost channels.
- **v5.6.1, released 2018-12-20** 
  - Fixed an issue where a user is not redirected to the account creation page on a fresh Mattermost server install.
  - Fixed an issue where file uploads crashed the webapp for some users.
  - Fixed slow channel switching load times, where every channel switch fetched users from all group message channels.
  - Fixed JIRA plugin not working due to a rename of the JIRA plugin directory structure.
- **v5.6.0, released 2018-12-16**
  - Original 5.6.0 release

### Breaking Changes since the last release

 - Replaced WebRTC prototype with other video and audio calling solutions. [Learn more here](https://docs.mattermost.com/deployment/video-and-audio-calling.html).
 - Removed support for IE11 Mobile View due to low usage and instability in order to invest that effort in maintaining a high quality experience on other more used browsers. End users on IE11 will thus have an increased minimum screen size.
 - If EnablePublicChannelsMaterialization setting in config.json is set to false, an offline migration prior to upgrade may be required to synchronize the materialized table for public channels to increase channel search performance in the channel switcher (CTRL/CMD+K), channel autocomplete (~) and elsewhere in the UI. See [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html) for more details.
 
**IMPORTANT:** If you upgrade from another release than 5.5, please read the [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html).

### Highlights

#### Interactive Dialogs
 - Added support for interactive dialogs to more easily collect structured information from users to perform an action or submit a request via an integration. [Learn more here](https://docs.mattermost.com/developer/interactive-dialogs.html)

#### Languages
 - Added support for Ukrainian language, bringing the number of supported languages to 16.
 - Romanian language promoted out of beta.

#### Command Line Interface (CLI)
 - Added new CLI commands to improve admin productivity, including:
   - ``command create`` to create a custom slash command for a specified team.
   - ``command delete`` to delete a slash command.
   - ``command move`` to move a slash command to a different team.
   - ``command list`` to list all commands on specified teams or all teams by default.
   - ``config get`` to retrieve the value of a config setting by its name in dot notation.
   - ``config set`` to set the value of a config setting by its name in dot notation.
   - ``config show`` to print the current Mattermost configuration in an easy to read format.
   - ``team archive`` to archive teams based on name.
   - ``team search`` to search for teams based on name.
   - ``webhook create-incoming`` to create incoming webhook within specific channel.
   - ``webhook create-outgoing`` to create outgoing webhook within specific channel.
   - ``webhook delete`` to delete a webhook.
   - ``webhook list`` to list all webhooks for a team or across the server.
   - ``webhook modify-incoming`` to modify existing incoming webhook by changing its title, description, channel or icon url.

### Improvements

#### User Interface
 - Added ability to remove profile pictures in Account Settings.
 - Added a new loading bar that shows progress on file uploads.
 - Added a new badge to the profile popover that indicates if a user is a System Admin.
 - Added new channel sidebar reorganization options for the `ExperimentalGroupUnreadChannels` config.json setting, such as the ability to sort channels by recent messages.
 - Added an option to be able to clear search results.

#### Notifications
 - Enabled push notifications by default on new Mattermost installs, via an encrypted TPNS (test push notification service).
 - Added a channel notification setting to disable @-channel @-here @-all notifications in specific channels.

#### Performance
 - Increased performance for returning user autocomplete results.

#### Plugins
 - Added a "min_server_version" field to plugin.json manifest, which enables built-in control for preventing loading plugins that are not compatible with the Mattermost server version.
 - Added ability for plugins to add channel header tooltips.
 - Stopped hashing plugin keys on write to more effectively enumerate the keys stored by a plugin.
 - Removed support for automatically unmarshalling a plugin's server configuration.

#### Bulk Import/Export
 - Added custom emoji and emoji reactions to bulk export tool.
 - Added favorite channels to bulk export tool.
 - Added user and channel notification preferences to bulk export tool.
 - Added the ability to specify an email batching interval for bulk import.

#### Slash Commands
 - Added support for multiple responses from a slash command.
 - Added an option to send a message when an invalid slash command is entered.

#### Administration
 - Added mobile support for Custom Terms of Service (Beta)
 - Removed **System Console > Plugins (Beta) > Configuration** page and moved enabling plugins setting to the **Plugins (Beta) > Management** page.
 - Introduced mlog/human package to consume and reformat structured logging with a human readable output.

#### Enterprise Edition (E20)
 - Data Retention promoted out of beta.

### Bug Fixes
 - Fixed an issue where pinned post list refreshed when a user posted a new message.

### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:

 - Under ``"ServiceSettings"`` in ``config.json``:
    - Added ``"TLSMinVer": "1.2"``, ``"TLSStrictTransport": false``, ``"TLSStrictTransportMaxAge": 63072000`` and ``"TLSOverwriteCiphers": []``, to configure TLS connection when not using a reverse proxy such as NGINX.
 - Under ``"ExperimentalSettings"`` in ``config.json``:
    - Added ``"EnablePostMetadata": false``, to disable post metadata from being loaded.

### API Changes

#### RESTful API v4 Changes
 - Added ``GET /channels/{channel_id}/timezones`` to get a list of timezones for the users who are in the specified channel.
 - Added ``page`` and ``per_page`` properties to ``POST /teams/{team_id}/posts/search`` call for Elasticsearch paging.
 - Added ``DELETE /users/{user_id}/image`` to remove a user's profile picture.
 - Added ``DELETE /brand/image`` to remove a custom branding image.
 - Added ``POST /actions/dialogs/open`` and ``POST /actions/dialogs/submit`` to open and submit requests via interactive dialogs.

#### Plugin API Changes
 - **Changed ``GetTeamMembers(teamId string, offset, limit int)`` to ``GetTeamMembers(teamId string, page, perPage int)`` to be clearer and consistent with other APIs**
 - **Changed ``GetPublicChannelsForTeam(teamId string, offset, limit int)`` to ``GetPublicChannelsForTeam(teamId string, page, perPage int)`` to be clearer and more consistent with other APIs**
 - Added the following plugin API methods. For more information on each method, see the [server plugin reference](https://developers.mattermost.com/extend/plugins/server/reference/).
     - ``GetChannelsForTeamForUser``     
     - ``GetChannelMembers``
     - ``GetChannelMembersByIds``
     - ``GetChannelStats``
     - ``GetEmoji``
     - ``GetEmojiByName``
     - ``GetEmojiImage``
     - ``GetEmojiList``
     - ``GetPluginConfig``
     - ``SavePluginConfig``
     - ``GetPostsAfter``
     - ``GetPostsBefore``
     - ``GetPostsSince``
     - ``GetPostsForChannel``
     - ``GetPostThread``
     - ``GetProfileImage``
     - ``SetProfileImage``
     - ``GetTeamsForUser``
     - ``GetTeamsUnreadForUser``
     - ``GetTeamIcon``
     - ``SetTeamIcon``
     - ``RemoveTeamIcon``
     - ``GetUsersByUsernames``
     - ``GetUsersInChannel``
     - ``GetUsersInChannelByStatus``
     - ``GetUsersInTeam``
     - ``CreateDirectChannel``
     - ``SearchChannels``
     - ``SearchUsers`` 
     - ``GetFileLink``
     - ``UploadFile``
     - ``SetProfileImage``
     - ``KVSetWithExpiry``
     - ``KVDeleteAll``
     - ``KVList``

#### Database Changes

 - Added ``ExpireAt`` column to the ``PluginKeyValueStore`` table.
 - Migrated user's accepted terms of service data into a new table called ``UserTermsOfService``.
 - Removed ``idx_users_email_lower``, ``idx_users_username_lower``, ``idx_users_nickname_lower``, ``idx_users_firstname_lower`` and ``idx_users_lastname_lower`` indexes.

### Known Issues

 - Login does not work when Custom Terms of Service is enabled and MFA is enforced.
 - Custom Terms of Service returns on refresh after clicking to agree.
 - Google login fails on the Classic mobile apps.
 - User can receive a video call from another browser tab while already on a call.
 - Jump link in search results does not always jump to display the expected post.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Channel scroll position flickers while images and link previews load.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - CTRL/CMD+U shortcut to upload a file doesn’t work on Firefox.

### Contributors

[aeomin](https://github.com/aeomin), [amorriscode](https://github.com/amorriscode), [amyblais](https://github.com/amyblais), [ArchRoller](https://github.com/archroller), [asaadmahmood](https://github.com/asaadmahmood), [bbodenmiller](https://github.com/bbodenmiller), [bd12](https://github.com/bd12), [chclaus](https://github.com/chclaus), [chetanyakan](https://github.com/chetanyakan), [chikei](https://github.com/chikei), [chrux](https://github.com/chrux), [cobenash](https://github.com/cobenash), [cometkim](https://github.com/cometkim), [comharris](https://github.com/comharris), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [danmaas](https://github.com/danmaas), [der-test](https://github.com/der-test), [DSchalla](https://github.com/DSchalla), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [grundleborg](https://github.com/grundleborg), [gupsho](https://github.com/gupsho), [gy741](https://github.com/gy741), [hanzei](https://github.com/hanzei), [harshilsharma](https://github.com/harshilsharma), [hmhealey](https://github.com/hmhealey), [icelander](https://github.com/icelander), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jlevesy](https://github.com/jlevesy), [JustinReynolds-MM](https://github.com/JustinReynolds-MM), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [knrt10](https://github.com/knrt10), [letsila](https://github.com/letsila), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lindy65](https://github.com/lindy65), [lisakycho](https://github.com/lisakycho), [meilon](https://github.com/meilon), [mickmister](https://github.com/mickmister), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [mojicaj](https://github.com/mojicaj), [murugesan](https://github.com/pradeepmurugesan), [patniharshit](https://github.com/patniharshit), [pichouk](https://github.com/pichouk), [pjgrizel](https://github.com/pjgrizel), [robert843](https://github.com/robert843), [rodcorsi](https://github.com/rodcorsi), [rononline](https://github.com/rononline), [ryoon](https://github.com/ryoon), [sandlis](https://github.com/sandlis), [saturninoabril](https://github.com/saturninoabril), [scottleedavis](https://github.com/scottleedavis), [sudheerDev](https://github.com/sudheerDev), [svelle](https://github.com/svelle), [thePanz](https://github.com/thePanz), [ThiefMaster](https://github.com/ThiefMaster), [torlenor](https://github.com/torlenor), [tuxfamily](https://github.com/tuxfamily), [uhlhosting](https://github.com/uhlhosting), [vaithak](https://github.com/vaithak), [waseem18](https://github.com/waseem18), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [yuya-oc](https://github.com/yuya-oc), [zeroimpl](https://github.com/zeroimpl), [zetaab](https://github.com/zetaab)

## Release v5.5 - Quality Release

- **v5.5.3, released 2019-02-01** 
  - Mattermost v5.5.3 contains a high level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
- **v5.5.2, released 2019-01-16**
  - Mattermost v5.5.2 contains medium level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
- **v5.5.1, released 2018-12-06** 
  - Fixed a bug preventing Elasticsearch v6.0+ from working in Mattermost server versions 5.4 and 5.5.
- **v5.5.0, released 2018-11-16**
  - Original 5.5.0 release

### Bug Fixes
 - Fixed an issue where clicking the two arrows to expand/collapse an image didn't work after posting an image.
 - Fixed an issue where switching authentication methods from email/password to SAML (OKTA and OneLogin) showed session expiry message instead of a success message.
 - Fixed an issue where message drafts occasionally posted to the channel even though user did not take any action to post it.
 - Fixed an issue with Autoresponder feature where the reply message did not get inserted consistently.
 - Fixed an issue where bolded channel names rendered over top of unbolded channel names in desktop.
 - Fixed an issue where config.ServiceSettings.SiteURL could contain a trailing slash.
 - Fixed a caching issue with archiving/unarchiving channels through API.
 - Fixed UX issues when trying to edit pending posts from reply thread.
 - Fixed an issue where "Enable Post Formatting" did not actually require page refresh.
 - Fixed an issue where User AuthService Export value of "" could be incompatible for importer.
 - Fixed an issue where search results that did not match case were not highlighted when returning hashtags in search results.
 - Fixed issues with indentation on the right-hand side in desktop app compact view.
 - Fixed an issue where the post header for bot messages was cutting off username before using available horizontal space.
 - Fixed an issue where "undefined" was briefly shown on refresh with combined system messages.
 - Fixed an issue where profile popover was cut-off at right-hand side root post.
 - Fixed UX issues for some plugins that displayed a blank page when clicking on the "Settings" link from "Management" page in System Console.
 - Fixed an issue where uploading a plugin resulted in a JS error and a blank page.
 - Fixed an issue where some team icons did not fill bounding box on MacOS.
 - Fixed an issue where there was no hover effect on emoji reactions.
 - Fixed an issue where a permanent announcement banner pushed the bottom of a channel sidebar off screen.
 - Fixed an issue where cancelling a change to channel notifications settings appeared to save the change.

### Known Issues

 - Google login fails on the Classic mobile apps.
 - User can receive a video call from another browser tab while already on a call.
 - Jump link in search results does not always jump to display the expected post.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Channel scroll position flickers while images and link previews load.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - CTRL/CMD+U shortcut to upload a file doesn’t work on Firefox.

### Contributors

[aeomin](https://github.com/aeomin), [Akash4927](https://github.com/Akash4927), [alexander-akhmetov](https://github.com/alexander-akhmetov), [amogozov](https://github.com/amogozov), [amorriscode](https://github.com/amorriscode), [amyblais](https://github.com/amyblais), [anchepiece](https://github.com/anchepiece), [ArchRoller](https://github.com/archroller), [asaadmahmood](https://github.com/asaadmahmood), [avasconcelos114](https://github.com/avasconcelos114), [Charliekenney23](https://github.com/Charliekenney23), [charvp](https://github.com/charvp), [chetanyakan](https://github.com/chetanyakan), [chikei](https://github.com/chikei), [cjohannsen81](https://github.com/cjohannsen81), [cobenash](https://github.com/cobenash), [cometkim](https://github.com/cometkim), [cored](https://github.com/cored), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [cvitter](https://github.com/cvitter), [czertbytes](https://github.com/czertbytes), [danmaas](https://github.com/danmaas), [der-test](https://github.com/der-test), [DHaussermann](https://github.com/DHaussermann), [dos1701](https://github.com/dos1701), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [florianeichin](https://github.com/florianeichin), [fraziern](https://github.com/fraziern), [grundleborg](https://github.com/grundleborg), [gupsho](https://github.com/gupsho), [gy741](https://github.com/gy741), [hanzei](https://github.com/hanzei), [harshilsharma](https://github.com/harshilsharma), [harshilsharma](https://github.com/harshilsharma), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [jasimmons](https://github.com/jasimmons), [jasonblais](https://github.com/jasonblais), [JayaKrishnaNamburu](https://github.com/JayaKrishnaNamburu), [jespino](https://github.com/jespino), [JtheBAB](https://github.com/JtheBAB), [JustinReynolds-MM](https://github.com/JustinReynolds-MM), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [KerryAlsace](https://github.com/KerryAlsace), [klingtnet](https://github.com/klingtnet), [knrt10](https://github.com/knrt10), [leblanc-simon](https://github.com/leblanc-simon), [lfbrock](https://github.com/lfbrock), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lindy65](https://github.com/lindy65), [lologarithm](https://github.com/lologarithm), [MattMattV](https://github.com/MattMattV), [meilon](https://github.com/meilon), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [mojicaj](https://github.com/mojicaj), [mukulrawat1986](https://github.com/mukulrawat1986), [n7st](https://github.com/n7st), [pichouk](https://github.com/pichouk), [pjgrizel](https://github.com/pjgrizel), [powhu](https://github.com/powhu), [pradeepmurugesan](https://github.com/pradeepmurugesan), [pushkyn](https://github.com/pushkyn), [robert843](https://github.com/robert843), [rodcorsi](https://github.com/rodcorsi), [rononline](https://github.com/rononline), [ryoon](https://github.com/ryoon), [s4kh](https://github.com/s4kh), [SaashaJoshi](https://github.com/SaashaJoshi), [saturninoabril](https://github.com/saturninoabril), [SergeyShpak](https://github.com/SergeyShpak), [sonasingh46](https://github.com/sonasingh46), [sudheerDev](https://github.com/sudheerDev), [thePanz](https://github.com/thePanz), [torlenor](https://github.com/torlenor), [tyvsmith](https://github.com/tyvsmith), [uhlhosting](https://github.com/uhlhosting), [uusijani](https://github.com/uusijani), [VPashkov](https://github.com/VPashkov), [waseem18](https://github.com/waseem18), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [yuya-oc](https://github.com/yuya-oc)

## Release v5.4 - Feature Release

Release date: 2018-10-16

- Mattermost v5.4.0 contains a low level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Breaking Changes since the last release

 - Mattermost mobile app version 1.13+ is required. File uploads will fail on earlier mobile app versions.
 - In certain upgrade scenarios the new Allow Team Administrators to edit others posts setting under General then Users and Teams may be set to True while the Mattermost default in 5.1 and earlier and with new 5.4+ installations is False.

**IMPORTANT:** If you upgrade from another release than 5.3, please read the [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html).

### Highlights

#### Basic Export Tool
 - Created a basic exporter tool to extract objects from Mattermost for allowing to merge two servers.

### Improvements

#### Web User Interface (UI)
 - Added a draft indicator in the channel sidebar and channel switcher for channels with unsent messages.
 - Added support for jumboemojis.
 - Added support for searching in direct message and group message channels using the "in:" modifier.
 - Last viewed channel on logout is restored on next session.
 - Added support for consecutive messages in the right-hand side.
 - Added tooltips to post info overlay buttons.
 - Added a feature to post a code block on CTRL + ENTER.
 - Expanded post text box area when composing long posts.
 - Updated the pinned post list when it's open and the channel is switched so that the pinned post list updates to show the other channel's pinned posts.
 - Download of common file types is not forced when viewing a public link.

#### Command Line Interface (CLI)
 - Added a new Command Line Interface for removing all users from a channel.

#### Performance
 - Improved channel switcher performance.

#### Integrations
 - Added interactive menus to message attachments.
 - Added a autotranslation plugin.
 - Added a button to copy the information from webhooks/slash commands such as the url and token.
 - Added "Commented on..." text for files and message attachment type posts.
 - Updated incoming and outgoing webhook description to 500 characters.
 - Added hook ID to webhook requests in server logs.
 - Plugins without a server or webapp component now fail to be activated.

#### Notifications
 - Desktop notifications now follow teammate name display setting.
 - Added a mute/unmute option to channel dropdown menu.
 - Added a mute icon to mobile view.
 - Added support for notifying users when desktop/browser sessions expire.

#### Autocomplete and Focus
 - With "Send messages on CTRL+ENTER = ON", channel and user autocomplete now work.
 - Cursor is now autofocused on edit box before the modal fully loads.
 - Channel autocomplete closes after two consecutive tildes used for strikethrough formatting.
 - If a user begins typing and the cursor is not in an input box, the cursor is automatically put into the center channel text input box.

#### Administration
 - Moved hiding join/leave messages to Team Edition.
 - Added ``edit_others_posts`` as a permission setting for Team Edition.
 - Added account setting option to hide channel switcher button in the sidebar.

#### Compliance
 - Added changes for E20 custom service terms.
 - Team membership can be restricted based on email domains.

### Bug Fixes
 - Fixed an issue where logging in with LDAP account with MFA enabled resulted in "Error trying to authenticate MFA token" error when "Enable sign-in with username" was set to false.
 - Fixed an issue where log-in page flashed briefly during process of verifying an updated email address.
 - Fixed an issue where ""GET /api/v4/redirect_location" responses got stuck when “EnableLinkPreviews” was set to "false”.
 - Fixed an issue where Account Settings teammate name display setting changed when System Console teammate name display setting was changed.

### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

#### Changes to Enterprise Edition:

 - Under "SqlSettings": in ``config.json``:
   - Added ``"EnablePublicChannelsMaterialization": true``, to increase channel search performance in the channel switcher (CTRL/CMD+K), channel autocomplete (~) and elsewhere in the UI.

### API Changes

#### Plugin API Changes
 - Added slash commands with GET crush query parameters on configured endpoint URL to avoid parameters specified by both the user and Mattermost from being duplicated.
 - Added a GetServerVersion() string method to the plugin API to return the current server version.

#### Database Changes
 - ``Description`` column was added to the ``OutgoingWebhooks`` table.
 - ``Description`` column was added to the ``IncomingWebhooks`` table.
 - ``AcceptedServiceTermsId`` column was added to the ``Users`` table.
 - ``PublicChannels`` table was added.

### Known Issues

 - Google login fails on the Classic mobile apps.
 - User can receive a video call from another browser tab while already on a call.
 - Jump link in search results does not always jump to display the expected post.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Channel scroll position flickers while images and link previews load.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - CTRL/CMD+U shortcut to upload a file doesn’t work on Firefox.

### Contributors

[aeomin](https://github.com/aeomin), [amyblais](https://github.com/amyblais), [asaadmahmood](https://github.com/asaadmahmood), [ArchRoller](https://github.com/archroller), [avasconcelos114](https://github.com/avasconcelos114), [balcsida](https://github.com/balcsida), [bezumkin](https://github.com/bezumkin), [ccpaging](https://github.com/ccpaging), [chetanyakan](https://github.com/chetanyakan), [chikei](https://github.com/chikei), [cimfalab](https://github.com/cimfalab), [cjbirk](https://github.com/cjbirk), [cometkim](https://github.com/cometkim), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [cvitter](https://github.com/cvitter), [danmaas](https://github.com/danmaas), [der-test](https://github.com/der-test), [DHaussermann](https://github.com/DHaussermann), [dmitrysamuylovpharo](https://github.com/dmitrysamuylovpharo), [DSchalla](https://github.com/DSchalla), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [FurmanovD](https://github.com/FurmanovD), [gramakri](https://github.com/gramakri), [greensteve](https://github.com/greensteve), [grundleborg](https://github.com/grundleborg), [gvengel](https://github.com/gvengel), [hanzei](https://github.com/hanzei), [harshilsharma](https://github.com/harshilsharma), [hmhealey](https://github.com/hmhealey), [jasonblais](https://github.com/jasonblais), [jazzzz](https://github.com/jazzzz), [jespino](https://github.com/jespino), [jkurian](https://github.com/jkurian), [JustinReynolds-MM](https://github.com/JustinReynolds-MM), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [kongr45gpen](https://github.com/kongr45gpen), [lfbrock](https://github.com/lfbrock), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [meilon](https://github.com/meilon), [mikroskeem](https://github.com/mikroskeem), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [n1aba](https://github.com/n1aba), [n7st](https://github.com/n7st), [pichouk](https://github.com/pichouk), [pjgrizel](https://github.com/pjgrizel), [pkuhner](https://github.com/pkuhner), [robert843](https://github.com/robert843), [rodcorsi](https://github.com/rodcorsi), [ryoon](https://github.com/ryoon), [R-Wang97](https://github.com/R-Wang97), [saturninoabril](https://github.com/saturninoabril), [sudheerDev](https://github.com/sudheerDev), [tejasbubane](https://github.com/tejasbubane), [thawn](https://github.com/thawn), [thePanz](https://github.com/thepanz), [ThiefMaster](https://github.com/ThiefMaster), [uhlhosting](https://github.com/uhlhosting), [wget](https://github.com/wget), [xcompass](https://github.com/xcompass), [yuya-oc](https://github.com/yuya-oc), [zetaab](https://github.com/zetaab)

## Release v5.3 - Feature Release

Mattermost v5.3.0 contains a high level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

- **v5.3.1, released 2018-09-19**
  - Fixed an issue where HTML elements such as links did not display correctly for non-English languages.
- **v5.3.0, released 2018-09-16**
  - Original 5.3.0 release

### Breaking Changes since the last release

 - Those servers with Elasticsearch enabled will notice that hashtag search is case-sensitive.

**IMPORTANT:** If you upgrade from another release than 5.2, please read the [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html).

### Highlights

#### Search Date Filters
- Search for messages before, on, or after a specified date.

#### IdAttribute Setting for SAML
- Added a new `IdAttribute` setting for SAML, which allows SAML users to change their email address without losing their account.

### Improvements

#### Web User Interface (UI)
- Added ability to set username and profile picture in **Outgoing Webhooks** setup page.
- Added "Deactivate Account" option under **Account Settings > Advanced**.
- Added member count for the **More Direct Messages** list.
- Expanded shortened (e.g. bitly) links for previewable content such as images and YouTube links.

#### Performance
- Improved channel switcher performance by adding a short delay after the last character has been typed before querying  the server for new autocomplete results.

#### Integrations
- Added support for interactive message buttons to, for instance, delete or edit the post after clicking on a message button.

#### Administration
- Created a telemetry event for when telemetry is turned off from the System Console.
- Added support for attachments in Direct Message channels to the [bulk import tool](https://docs.mattermost.com/deployment/bulk-loading.html).

### Bug Fixes
- Fixed an issue where closing an archived channel did not redirect users to the last viewed channel.
- Fixed an issue where users were able to react to existing emojis in an archived channel.
- Fixed an issue where clicking "+" twice to add a public or private channel added a recently archived channel back to the left-hand side.
- Fixed an issue where channel autocomplete appeared to include all public channels, including deleted channels and channels one has never joined.

### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

#### Changes to Enterprise Edition:

 - Under "SamlSettings": in ``config.json``:
    - Added ``"EnableSyncWithLdapIncludeAuth": false,`` to override the SAML ID attribute with the AD/LDAP ID attribute if configured, or override the SAML Email attribute with the AD/LDAP Email attribute if SAML ID attribute is not present. See [documentation](https://about.mattermost.com/default-saml-ldap-sync) to learn more.
    - Added ``"IdAttribute": "",`` to set the attribute in the SAML Assertion that will be used to bind users from SAML to users in Mattermost.

### API Changes

#### Plugin API Changes (Release Candidate)
 - Added ``postId`` as a property for ``PostDropDownMenuComponent`` and as a parameter for the ``PostDropDownMenuAction`` function to improve the ability to add options to the post "..." action menu.
 - Added ``FileInfo`` and ``file []byte`` to retrieve File Info for a specific fileId and to ensure the file is read for a specific path.
 - Added ``GetLDAPUserAttributes``, which matches the functionality of the ``ldapextras`` built-in plugin that was removed in Mattermst v5.2.

### Known Issues

 - When "Enable sign-in with username" is set to false, logging in with LDAP account with MFA enabled results in "Error trying to authenticate MFA token" error.
 - Google login fails on the Classic mobile apps.
 - User can receive a video call from another browser tab while already on a call.
 - Jump link in search results does not always jump to display the expected post.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Channel scroll position flickers while images and link previews load.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - CTRL/CMD+U shortcut to upload a file doesn’t work on Firefox.

### Contributors

[aeomin](https://github.com/aeomin), [amyblais](https://github.com/amyblais), [ArchRoller](https://github.com/archroller), [asaadmahmood](https://github.com/asaadmahmood), [chikei](https://github.com/chikei), [cometkim](https://github.com/cometkim), [comharris](https://github.com/comharris), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [dcherniv](https://github.com/dcherniv), [der-test](https://github.com/der-test), [DHaussermann](https://github.com/DHaussermann), [dmitrysamuylovpharo](https://github.com/dmitrysamuylovpharo), [DSchalla](https://github.com/DSchalla), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [grundleborg](https://github.com/grundleborg), [gvengel](https://github.com/gvengel), [Hanzei](https://github.com/Hanzei), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [Jessica-c53](https://github.com/Jessica-c53), [JustinReynolds-MM](https://github.com/JustinReynolds-MM), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [lfbrock](https://github.com/lfbrock), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lindy65](https://github.com/lindy65), [lisakycho](https://github.com/lisakycho), [meilon](https://github.com/meilon), [MerlinDMC](https://github.com/MerlinDMC), [michaelkochub](https://github.com/michaelkochub), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [n1aba](https://github.com/n1aba), [pichouk](https://github.com/pichouk), [pjgrizel](https://github.com/pjgrizel), [pradeepmurugesan](https://github.com/pradeepmurugesan), [robert843](https://github.com/robert843), [rodcorsi](https://github.com/rodcorsi), [rononline](https://github.com/rononline), [rqtaylor](https://github.com/rqtaylor), [ryoon](https://github.com/ryoon), [R-Wang97](https://github.com/R-Wang97), [saturninoabril](https://github.com/saturninoabril), [sjstyle](https://github.com/sjstyle), [sudheerDev](https://github.com/sudheerDev), [thePanz](https://github.com/thepanz), [ThiefMaster](https://github.com/ThiefMaster), [uhlhosting](https://github.com/uhlhosting), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [yuya-oc](https://github.com/yuya-oc)

## Release v5.2 - Feature Release

 - **v5.2.2, released 2018-09-16**
   - Mattermost v5.2.2 contains a high level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
- **v5.2.1, released 2018-08-23**
  - Disabled the ability to search archived channels by default, given multiple issues were raised after v5.2.0 was released. The feature can be enabled in v5.2.1 via ``ExperimentalViewArchivedChannels`` setting.
- **v5.2.0, released 2018-08-16**
  - Original 5.2.0 release

### Security Update

- Mattermost v5.2.0 contains medium level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Breaking Changes since the last release

 - Those servers upgrading from v4.1 - v4.4 directly to v5.2 or later and have JIRA enabled will need to re-enable the JIRA plugin after an upgrade.

**IMPORTANT:** If you upgrade from another release than 5.1, please read the [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html).

### Highlights

#### Embed Mattermost in Other Apps (Beta)
 - Added support for extensions, which allow you to embed Mattermost in other apps and websites via OAuth 2.0.
 - A sample extension for Chrome [is here](https://github.com/mattermost/mattermost-chrome-extension).

#### Plugins
 - Added support to add/delete and enable/disable plugins via the CLI.
 - See our [demo plugin](https://github.com/mattermost/mattermost-plugin-demo) that demonstrates the capabilities of a Mattermost plugin. For a starting point to write a Mattermost plugin, see our [sample plugin](https://github.com/mattermost/mattermost-plugin-sample).
 - Breaking changes to the plugins framework introduced. To migrate your existing plugins to be compatible with Mattermost 5.2 and later, see our [migration guide](https://developers.mattermost.com/extend/plugins/migration/).

#### Searching Archived Channels
 - Added ability to search for archived channel content on desktop and mobile clients.

#### Romanian Language
 - Added support for Romanian language.

### Improvements

#### Web User Interface (UI)
 - Added experimental custom default channels.
 - Added link to profile pop-over from names in Join/Leave messages.
 - Added support for webhook message attachments to trigger mentions.
 - Stripped markdown formatting characters from desktop notifications and "Commented on..." text.
 - Added ability to bulk import emoji.
 - Added support for file attachments in bulk import.

#### Plugins (All Beta)
 - New [antivirus plugin](https://github.com/mattermost/mattermost-plugin-antivirus) to scan for viruses before uploading a file to Mattermost. Supports [ClamAV anti-virus software](https://www.clamav.net/) across browser, Desktop Apps and the Mobile Apps.
 - New [GitHub plugin](https://github.com/mattermost/mattermost-plugin-github) to subscribe to notifications, and to keep track of unread GitHub messages and open pull requests requiring your attention.
 - [Zoom plugin](https://docs.mattermost.com/integrations/zoom.html) now has one option to start a meeting rather than three separate ones to simplify the user experience.

#### Server Plugins: Release Candidate
 - A release candidate (RC) is released for server plugins. Stable release is expected in v5.3 or v5.4.
 - Added various API methods for plugins to provide the same capabilities as the REST API.
 - Added support to intercept file uploads before the file is uploaded to a Mattermost server.
 - Added support for plugins to respond after a user joins/leaves a channel or a team, or creates a new channel.
 - Added support for plugins to respond prior to or after a user logs in to a Mattermost server.
 - Added support for plugins to update user status. Sample use case is setting a user’s status to Do Not Disturb based on Google Calendar events.
 - Added CSRF tokens that are attached to users sessions. The tokens can be enforced as an alternative to XHR checks in the plugin request system.
 - Added session token to context for ServeHTTP hook.

#### Webapp Plugins: Beta
 - Upcoming Mattermost UI redesign may cause breaking changes to webapp plugins. Hence, webapp plugins remain as beta in v5.2.
 - Added support to override [...] post menu, and paperclip icon for file uploads.
 - Added support for multiple plugins to add components at the same integration points instead of only allowing one plugin to do so.
 - Removed ability to fully override profile popover. Instead, multiple plugins can now add to the profile popover via multiple integration points.
 - For an up-to-date list of pluggable UI components, [see this list in our demo plugin](https://github.com/mattermost/mattermost-plugin-demo/tree/master/webapp#components).

#### Administration
 - In the compliance export status table, in System Console > Compliance > Compliance Export, added a number of exported records to Details column.
 - Added support for cross-origin resource sharing.

#### Command Line Interface (CLI)
 - Enhanced log output from Permanent Delete CLI command to delete FileInfos for a user's posts.
 - Addded channel renaming to CLI.

#### Enterprise Edition
 - Added the Global Relay Export CLI command.
 - Added support to search plugin contents.

### Bug Fixes
 - Fixed an issue where the "Switch Channel" shortcut (⌘K) didn't work on dvorak layout on Mac.
 - Fixed an issue where the Custom Integrations section in the System Console was blank after role changes.
 
### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:

 - Under "ServiceSettings": in ``config.json``:
      - Added ``"CorsExposedHeaders": ""``, to add a whitelist of headers that will be accessible to the requester.
      - Added ``"CorsAllowCredentials": false``, to allow requests that pass validation to include the ``Access-Control-Allow-Credentials`` header.
      - Added ``"CorsDebug": false``, to print messages to the logs to help when developing an integration that uses CORS.
 - Under "TeamSettings" in ``config.json``:
      - Added ``"ViewArchivedChannels": true``, to allow users to share permalinks and search for content of channels that have been archived.
      - Added ``"ExperimentalDefaultChannels": ""``, to allow choosing the default channels every user is added to automatically after joining a new team.

### API Changes

#### RESTful API v4 Changes
 - ``deleteReaction`` API was added to send the correct value for ``post.HasReactions``.
 - Support for add/delete and enable/disable plugins via CLI was added.
 - File download API was improved to stream files instead of loading them entirely into memory.

#### Websocket Changes
 - Support for add/delete and enable/disable plugins via CLI was added.

#### Database Changes
 - Two new columns were added in the ``OutgoingWebhooks`` table, "Username" and "IconURL".

### Known Issues

 - Google login fails on the Classic mobile apps.
 - User can receive a video call from another browser tab while already on a call.
 - Jump link in search results does not always jump to display the expected post.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Channel scroll position flickers while images and link previews load.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - CTRL/CMD+U shortcut to upload a file doesn’t work on Firefox.

### Contributors
[aeomin](https://github.com/aeomin), [alanpog](https://github.com/alanpog), [Alexgoodman7](https://github.com/Alexgoodman7), [amyblais](https://github.com/amyblais), [archroller](https://github.com/archroller), [asaadmahmood](https://github.com/asaadmahmood), [burguyd](https://github.com/burguyd), [chikei](https://github.com/chikei), [cometkim](https://github.com/cometkim), [comharris](https://github.com/comharris), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [der-test](https://github.com/der-test), [DHaussermann](https://github.com/DHaussermann), [DSchalla](https://github.com/DSchalla), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [falcon78921](https://github.com/falcon78921), [fdebrabander](https://github.com/fdebrabander), [grundleborg](https://github.com/grundleborg), [herooftimeandspace](https://github.com/herooftimeandspace), [hmhealey](https://github.com/hmhealey), [icelander](https://github.com/icelander), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [Jessica-c53](https://github.com/Jessica-c53), [JustinReynolds-MM](https://github.com/JustinReynolds-MM), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [kennethjeremyau](https://github.com/kennethjeremyau), [lfbrock](https://github.com/lfbrock), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lindy65](https://github.com/lindy65), [meilon](https://github.com/meilon), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [pepf](https://github.com/pepf), [pichouk](https://github.com/pichouk), [pietroglyph](https://github.com/pietroglyph), [pjgrizel](https://github.com/pjgrizel), [pradeepmurugesan](https://github.com/pradeepmurugesan), [rodcorsi](https://github.com/rodcorsi), [Roy-Orbison](https://github.com/Roy-Orbison), [ryoon](https://github.com/ryoon), [santos22](https://github.com/santos22), [saturninoabril](https://github.com/saturninoabril), [scherno2](https://github.com/scherno2), [seansackowitz](https://github.com/seansackowitz), [sudheerDev](https://github.com/sudheerDev), [tejasbubane](https://github.com/tejasbubane), [theblueskies](https://github.com/theblueskies), [ThiefMaster](https://github.com/ThiefMaster), [uhlhosting](https://github.com/uhlhosting), [uusijani](https://github.com/uusijani), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [yuya-oc](https://github.com/yuya-oc)

## Release v5.1 - Feature Release

 - **v5.1.2, released 2018-09-16**
   - Mattermost v5.1.2 contains a high level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v5.1.1, released 2018-08-07**
   - Mattermost v5.1.1 contains medium level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v5.1.0, released 2018-07-16**
   - Original 5.1.0 release

### Security Update

- Mattermost v5.1.0 contains multiple security fixes ranging from low to high severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Breaking Changes since the last release

 - ``mattermost export`` CLI command is renamed to ``mattermost export schedule``. Make sure to update your scripts if you use this command.

**IMPORTANT:** If you upgrade from another release than 5.0, please read the [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html).

### Highlights

#### Gfycat integration
 - Added easy access to sharing GIFs without leaving the Mattermost interface. System Admins can enable this feature in **System Console > Customization > GIF**.

#### Auto-linking plugin (Beta)
 - Messages can now be formatted into Markdown links automatically before they are saved to the Mattermost database. See [autolink plugin repository](https://github.com/mattermost/mattermost-plugin-autolink) to learn more.

#### Support Mattermost on a subpath
 - Added support for hosting Mattermost at any route (e.g., https://www.example.com/mattermost) with newly added subpath support.

#### CSV Compliance Export ([Enterprise Edition E20](https://about.mattermost.com/pricing))
 - Extended compliance export feature with CSV format. See [documentation](https://docs.mattermost.com/administration/compliance-export.html) to learn more.

### Improvements

#### Web User Interface
 - Added highlighting for Elasticsearch results.
 - Renamed "Delete Channel" to "Archive Channel". Channels can be unarchived [from the commandline](https://docs.mattermost.com/administration/command-line-tools.html#mattermost-channel-restore).
 - Added Channel Purpose as a searchable field in the "More Channels" menu.

#### Administration
 - Added the ability to reset user emails in **System Console > Users**.
 - Server restart is no longer required to run the job server for the first time.

#### Command Line Interface (CLI)
 - Made the `permissions reset` CLI command able to reset all custom-role related data.
 - When `permanent delete user` CLI command is used, all files uploaded by the user are now deleted as well.
 - ``export`` CLI command was updated to support scheduling exports via `export schedule`, and to export files in Actiance XML and CSV formats.
 - Running the CLI outside of the bin directory is now less error prone.

#### Enterprise Edition E20
 - Added experimental support for certificate-based authentication (CBA) to identify a user or a device before granting access to Mattermost. See [documentation](https://docs.mattermost.com/deployment/certificate-based-authentication.html) to learn more.

### Bug Fixes

 - Fixed an issue where users could not reply to push notifications on iOS.
 - Fixed an issue with an incorrect system message after converting a public channel to private.
 - Fixed an issue with being unable to add emoji reactions after expanding the message details sidebar.
 - Fixed an issue where [rate limiting settings](https://docs.mattermost.com/administration/config-settings.html#rate-limiting) could not be edited in the System Console, and weren't displayed in the User Interface if configured via `config.json`.
 - Fixed an issue where deleted users shown as "Someone" in the Favorite Channels section could not be removed.

### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:

 - Under "ExperimentalSettings:" in ``config.json``:
    - Added ``"ClientSideCertEnable": false,``, to enable client-side certification for your Mattermost server.
    - Added ``"ClientSideCertCheck": "secondary"``, to control whether email and password are required following client-side certification.
 - Under "ServiceSettings:" in ``config.json``:
    - Added ``"ExperimentalLimitClientConfig": false``, to limit the number of config settings sent to users prior to login. Supported on mobile apps v1.10 and later.
    - Added ``"EnableGifPicker": false,``, ``"GfycatApiKey": 2_KtH_W5,`` and ``"GfycatApiSecret": 3wLVZPiswc3DnaiaFoLkDvB4X0IV6CpMkj4tf2inJRsBY6-FnkT08zGmppWFgeof,`` to enable a built-in GIF integration with Gfycat.
    - Added ``"EnableEmailInvitations": false``, to disable email invitations on the system.
 - Under "SqlSettings:" in ``config.json``:
    - Added ``"ConnMaxLifetimeMilliseconds": 3600000,``, to configure the maximum lifetime for a connection to the database.

### API Changes

#### RESTful API v4 Changes

 - A new ``matches`` field was added to ``POST teams/{team_id}/posts/search`` to return a list of matched terms within the post. This field will only be populated on servers running version v5.1 or greater with Elasticsearch enabled.

### Known Issues

 - Google login fails on the Classic mobile apps.
 - User can receive a video call from another browser tab while already on a call.
 - Jump link in search results does not always jump to display the expected post.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Channel scroll position flickers while images and link previews load.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - CTRL/CMD+U shortcut to upload a file doesn’t work on Firefox.

### Contributors

[Alexgoodman7](https://github.com/Alexgoodman7), [amyblais](https://github.com/amyblais), [AndersonWebStudio](https://github.com/AndersonWebStudio), [asaadmahmood](https://github.com/asaadmahmood), [Brodan](https://github.com/Brodan), [cjohannsen81](https://github.com/cjohannsen81), [cometkim](https://github.com/cometkim). [comharris](https://github.com/comharris), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [cvitter](https://github.com/cvitter), [dmeza](https://github.com/dmeza), [DSchalla](https://github.com/DSchalla), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [evelikov](https://github.com/evelikov), [fbartels](https://github.com/fbartels), [greensteve](https://github.com/greensteve), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [icelander](https://github.com/icelander), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jkurian](https://github.com/jkurian), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kennethjeremyau](https://github.com/kennethjeremyau), [lfbrock](https://github.com/lfbrock), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lisakycho](https://github.com/lisakycho), [michaelgamble](https://github.com/michaelgamble), [mkraft](https://github.com/mkraft), [pichouk](https://github.com/pichouk), [Roy-Orbison](https://github.com/Roy-Orbison), [R-Wang97](https://github.com/R-Wang97), [saturninoabril](https://github.com/saturninoabril), [stanchan](https://github.com/stanchan), [sudheerDev](https://github.com/sudheerDev),[svelle](https://github.com/svelle), [tejasbubane](https://github.com/tejasbubane), [ThiefMaster](https://github.com/ThiefMaster), [wiersgallak](https://github.com/wiersgallak), [wildloop](https://github.com/wildloop), [yuya-oc](https://github.com/yuya-oc)

## Release v5.0 - Feature Release

 - **v5.0.3, released 2018-08-07**
   - Mattermost v5.0.3 contains a medium level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v5.0.2, released 2018-07-16**
   - Mattermost v5.0.2 contains a high severity security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v5.0.1, released 2018-07-09**
   - Fixed an issue where large Global Relay exports could cause export jobs to fail completely.
 - **v5.0.0, released 2018-06-16**
   - Original 5.0.0 release

### Breaking Changes since the last release

- All API v3 endpoints have been removed. [See documentation](https://api.mattermost.com/#tag/schema) to learn more about how to migrate your integrations to API v4. [Ticket #8708](https://mattermost.atlassian.net/browse/MM-8708).
- `platform` binary has been renamed to mattermost for a clearer install and upgrade experience. **You should point your `systemd` service file at the new `mattermost` binary.** All command line tools, including the bulk loading tool and developer tools, have also been renamed from platform to mattermost. [Ticket #9985](https://mattermost.atlassian.net/browse/MM-9985).
- A Mattermost user setting to configure desktop notification duration in **Account Settings** > **Notifications** > **Desktop Notifications** has been removed.
- Slash commands configured to receive a GET request now have the payload encoded in the query string instead of receiving it in the body of the request, consistent with standard HTTP requests. Although unlikely, this could break custom slash commands that use GET requests incorrectly. [Ticket #10201](https://mattermost.atlassian.net/browse/MM-10201).
- A new `config.json` setting to whitelist types of protocols for auto-linking has been added. [Ticket #9547](https://mattermost.atlassian.net/browse/MM-9547).
- A new `config.json` setting to disable the [permanent APIv4 delete team parameter](https://api.mattermost.com/#tag/teams%2Fpaths%2F~1teams~1%7Bteam_id%7D%2Fput) has been added. The setting is off by default for all new and existing installs, except those deployed on GitLab Omnibus. A System Administrator can enable the API v4 endpoint from the config.json file. [Ticket #9916](https://mattermost.atlassian.net/browse/MM-9916).
- An unused `ExtraUpdateAt` field has been removed from the channel model. [Ticket #9739](https://mattermost.atlassian.net/browse/MM-9739).

**IMPORTANT:** If you upgrade from another release than 4.10, please read the [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html).

### Highlights

#### Plugin Intercept
 - Adds support for plugins to intercept posts prior to saving them into the database.
 - Supports use cases such as auto-detecting and censoring restricted words, and auto-linking phrases. [Read our forum post to learn more](https://forum.mattermost.org/t/coming-soon-apiv4-mattermost-post-intercept/4982).

#### Permissions Schemes
 - System Scheme now sets the default permissions inherited system-wide by System Admins, Team Admins, Channel Admins and everyone else.
 - Added new Team Schemes to override the default permissions in specific teams for Team Admins, Channel Admins and all other team members.

#### Increased Character Limit on Posts
 - Increased character limit to 16,383 on new deployments to allow posting long messages and to allow better Markdown formatting, including tables.
 - For existing deployments, read [how to migrate your system](https://docs.mattermost.com/administration/important-upgrade-notes.html) to support the increased character limit.

#### Combined Join/Leave Messages
 - System messages related to joining, leaving, adding and removing people from channels and teams are combined into a single message to save space in channels.

### Improvements

#### Web User Interface
 - Added a feature to collapse image upload using a collapse icon or using the ``/collapse`` command.
 - Added a whitelist for valid types of links when autolinking.
 - Updated the styling of default team icons.

#### Performance
 - Fixed ``update_status`` cluster event being sent thousands of times on restart of app servers.

#### Integrations
 - Slash commands configured to receive a GET request now have the payload encoded in the query string instead of receiving it in the body of the request.
 - Added ability for webhooks to actually be locked to a channel.

#### Notifications
 - Updated email notification subject line and contents for Group Messages.
 - Updated the styling of push notifications.

#### System Console
 - Added a System Console setting to disable the preview mode banner when email notifications are disabled.

#### Administration
 - Added Password Requirements and Customer Branding to Team Edition.
 - Moved Themes per team to Team Edition.

#### Enterprise Edition
 - Added ``LoginIdAttribute`` to allow LDAP users to change their login ID without losing their account.

### Bug Fixes

 - Fixed an issue where ``EnableUserCreation`` was set to `false` when not included in config.json.
 - Fixed an issue where a public channel made private did not disappear automatically from clients not part of the channel.
 - Fixed an issue where team icon did not get automatically saved when removed.
 - Fixed an issue where Town Square channel disappeared from channel list for a non-admin users when "ExperimentalTownSquareIsReadOnly" `config.json` was set to `true` in config.json.

### Compatibility

 - For a list of important changes with Mattermost v5.0, please [see our Forum announcement](https://forum.mattermost.org/t/upcoming-changes-with-mattermost-v5-0/5119).

### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:

 - Under ``"ServiceSettings":`` in ``config.json``:
   - Added ``"EnableAPITeamDeletion": false,`` to disable the permanent APIv4 delete team parameter.
   - Added ``"ExperimentalEnableHardenedMode": false`` to enable a hardened mode for Mattermost that makes user experience trade-offs in the interest of security.
 - Under ``"EmailSettings":`` in ``config.json``:
   - Added ``"EnablePreviewModeBanner": true,`` to allow Preview Mode banner to be displayed so users are aware that email notifications are disabled.
 - Under ``"ClusterSettings":`` in ``config.json``:
   - Added ``"MaxIdleConns": 100,`` to add the maximum number of idle connections held open from one server to all others in the cluster.
   - Added ``"MaxIdleConnsPerHost": 128,`` to add the maximum number of idle connections held open from one server to another server in the cluster.
   - Added ``"IdleConnTimeoutMilliseconds": 90000`` to add the number of milliseconds to leave an idle connection open between servers in the cluster.
 - Under ``"TeamSettings":`` in ``config.json``:
   - Added ``"ExperimentalHideTownSquareinLHS": false,`` to hide Town Square in the left-hand sidebar if there are no unread messages in the channel.
 - Under ``"DisplaySettings":`` in ``config.json``:
   - Added ``"CustomUrlSchemes": [],``, to add a list of URL schemes that are used for autolinking in message text.
 - Under ``"LdapSettings":`` in ``config.json``:
   - Added ``"LoginIdAttribute": "",`` to add an attribute in the AD/LDAP server used to log in to Mattermost.

#### API Changes

 - All APIv3 endpoints were removed.
 - Improved file upload API to stream files instead of loading them entirely into memory.
 - SAML login endpoints were moved out of API package.
 - ``context.go`` was moved out of Api4 and into web.
 - ``api4/handlers.go`` was created to create the API handlers using the Context and Handler from web.
 - ``web/handlers.go`` was added to define the Handler struct, the base ServeHTTP function and a single web handler.

#### WebSocket Changes

 - Ping/pong and reconnection handling were added to Go WebSocket client.
 - Support was added for WebSocket custom dialer.
 - ``channel_converted`` WebSocket event was added, which is published team-wide whenever a channel is converted from public to private.

### Known Issues

 - [Image proxy](https://docs.mattermost.com/administration/image-proxy.html) cannot be saved in the System Console UI. Configure the settings in your `config.json` file instead.
 - Google login fails on the Classic mobile apps.
 - User can receive a video call from another browser tab while already on a call.
 - Jump link in search results does not always jump to display the expected post.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Channel scroll position flickers while images and link previews load.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - CTRL/CMD+U shortcut to upload a file doesn’t work on Firefox.

### Contributors

[aeomin](https://translate.mattermost.com/user/aeomin/), [amyblais](https://github.com/amyblais), [AndersonWebStudio](https://github.com/AndersonWebStudio), [asaadmahmood](https://github.com/asaadmahmood), [balasankarc](https://github.com/balasankarc), [chclaus](https://github.com/chclaus), [chikei](https://github.com/chikei), [comharris](https://github.com/comharris), [compilenix](https://github.com/compilenix), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [cvitter](https://github.com/cvitter), [der-test](https://github.com/der-test), [dkadioglu](https://github.com/dkadioglu), [DSchalla](https://github.com/DSchalla), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [fbartels](https://github.com/fbartels), [gnufede](https://github.com/gnufede), [grundleborg](https://github.com/grundleborg), [haraldkubota](https://github.com/haraldkubota), [hmhealey](https://github.com/hmhealey), [icelander](https://github.com/icelander), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jordanbuchman](https://github.com/jordanbuchman), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [lfbrock](https://github.com/lfbrock), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lindy65](https://github.com/lindy65), [lisakycho](https://github.com/lisakycho), [meilon](https://github.com/meilon), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [odontomachus](https://github.com/odontomachus), [pichouk](https://github.com/pichouk), [pjgrizel](https://github.com/pjgrizel), [rodcorsi](https://github.com/rodcorsi), [Roy-Orbison](https://github.com/Roy-Orbison), [ryoon](https://github.com/ryoon), [R-Wang97](https://github.com/R-Wang97), [saturninoabril](https://github.com/saturninoabril), [sudheerDev](https://github.com/sudheerDev), [thePanz](https://github.com/thepanz), [uturkdogan](https/github.com/uturkdogan), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [yuya-oc](https://github.com/yuya-oc)

## Release v4.10

 - **v4.10.10, released 2019-06-20** 
   - Mattermost v4.10.10 contains a medium level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.10.9, released 2019-04-24** 
   - Mattermost v4.10.9 contains a medium level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.10.8, released 2019-03-16** 
   - Mattermost v4.10.8 contains a medium level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.10.7, released 2019-02-16** 
   - Mattermost v4.10.7 contains low to medium level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.10.6, released 2019-02-01** 
   - Mattermost v4.10.6 contains a high level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.10.5, released 2019-01-16**
   - Mattermost v4.10.5 contains medium level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.10.4, released 2018-09-16**
   - Mattermost v4.10.4 contains a high level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.10.3, released 2018-08-07**
   - Mattermost v4.10.3 contains a medium level security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.10.2, released 2018-07-16**
   - Mattermost v4.10.2 contains a high severity security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.10.1, released 2018-06-04**
   - Mattermost v4.10.1 contains a moderate severity security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
   - Fixed an issue where the Mattermost screen went blank when viewing "Manage Members" list while another user was added to the channel.
   - Fixed an issue where [automatic replies](https://docs.mattermost.com/administration/config-settings.html#enable-automatic-replies-experimental) weren't properly posting or suppressing emails.
   - Fixed an issue where a member's roles for a team wasn't properly deleted when the team was deleted via the API, causing crashing issues.
 - **v4.10.0, released 2018-05-16**
   - Original 4.10.0 release

### Highlights

#### Convert Public Channels to Private
 - Team and System Admins can now convert a channel to private from the user interface. System Admins can also convert channels back to public [via the commandline](https://docs.mattermost.com/administration/command-line-tools.html#platform-channel-modify).

#### Performance Improvements
 - Decreased loading time by up to 90% for users with lots of direct and group message channels.

#### Environment Variables Support in GitLab Omnibus
 - Simplified Mattermost administration by supporting environment variables in GitLab Omnibus. See [documentation](https://docs.gitlab.com/omnibus/gitlab-mattermost/#upgrading-gitlab-mattermost-from-versions-prior-to-11-0) to learn more.

### Improvements

#### Web User Interface
 - Removed support for transparent team icons to support any sidebar theme colors and added the ability to remove team icons.
 - Added an experimental setting that users can use to set a custom message that will be automatically sent in response to Direct Messages.
 - Added a loading animation for "Add Members" channel invite modal.
 - Made SHIFT+UP switch keyboard focus to right-hand side if it's already open to the current thread.
 - Removed an unnecessary WebRTC end user setting to avoid user errors and confusion.
 - Added an on-hover effect for image link previews.

 #### Plugins
 - Added better plugin error handling and reporting.

 #### Slash Commands
 - Added ``/invite`` slash command to invite users to a channel.
 - Improved slash command error message when payload has invalid JSON.

 #### Administration
 - Added structured logging to more easily review server logs.
 - Users' client no longer refreshes after changing a System Console or ``config.json`` setting.

 #### Command Line Interface (CLI)
 - Added `/platform team list` command to list all teams on the server..

#### Enterprise Edition E20
 - Added cluster event types to [Performance Monitoring](https://docs.mattermost.com/deployment/metrics.html).

### Bug Fixes

 - Fixed an issue where focus with CTRL/CMD+SHIFT+L was always set to the right-hand side when reply thread was open.
 - Fixed an issue where a user added to a channel wasn't immediately removed from other users' "Add Members" dialog.
 - Fixed an issue where 'Copy Link' context menu option was partially hidden when right-clicking a team in team sidebar.
 - Fixed an issue where a user could not log in to Mattermost when their login id ("authdata") failed to migrate properly during migration from LDAP to SAML.
 - Fixed an issue where plugin configuration was not saved in the System Console.
 - Removed duplicate indexes accidentally created on the ``Channels``, ``Emoji`` and ``OAuthAccessData`` tables.

### Compatibility

#### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:

 - Under `"TeamSettings"` in `config.json`:
   - Added ``"ExperimentalEnableAutomaticReplies": false,`` to allow users to set a custom message that will be automatically sent in response to Direct Messages.
 - Under `"LogSettings"` in `config.json`:
   - Removed ``FileFormat`` and added ``"FileJson": true,`` and ``"ConsoleJson": true,`` to allow logged events to be written as a machine readable JSON format instead of the be printed as plain text.

#### API Changes

##### RESTful API v4 Changes

 - Support was added to RESTful API for sending ephemeral messages to users.
 - An APIv4 endpoint of ``POST /channels/{channel_id}/convert`` was added to convert a channel from public to private and to restrict this setting to ``team_admin``.
 - An APIv4 endpoint of ``DELETE /teams/{team_id}/image`` was added to remove team icon and restrict it to ``team_admin``.

#### Database Changes

**Users Table:**

 - Migrates SAML `AuthData` to lowercase via `"UPDATE Users SET AuthData=LOWER(AuthData) WHERE AuthService = 'saml'"` query.

**Channels Table:**

 - Removed duplicate `Name_2` index.

**Emoji Table:**

 - Removed duplicate `Name_2` index.

**OAuthAccessData Table:**

 - Removed duplicate `ClientId_2` index.

#### Upcoming Deprecated Features in Mattermost v5.0

The following deprecations are planned for the Mattermost v5.0 release, which is scheduled for summer/2018. This list is subject to change prior to the release.

1. All API v3 endpoints will be removed. [See documentation](https://api.mattermost.com/#tag/schema) to learn more about how to migrate your integrations to API v4. [Ticket #8708](https://mattermost.atlassian.net/browse/MM-8708).
2. `platform` binary will be renamed to mattermost for a clearer install and upgrade experience. All command line tools, including the bulk loading tool and developer tools, will also be renamed from platform to mattermost. [Ticket #9985](https://mattermost.atlassian.net/browse/MM-9985).
3. A Mattermost user setting to configure desktop notification duration in **Account Settings** > **Notifications** > **Desktop Notifications** will be removed.
4. Slash commands configured to receive a GET request will have the payload being encoded in the query string instead of receiving it in the body of the request, consistent with standard HTTP requests. Although unlikely, this could break custom slash commands that use GET requests incorrectly. [Ticket #10201](https://mattermost.atlassian.net/browse/MM-10201).
5. A new `config.json` setting to whitelist types of protocols for auto-linking will be added. [Ticket #9547](https://mattermost.atlassian.net/browse/MM-9547).
6. A new `config.json` setting to disable the [permanent APIv4 delete team parameter](https://api.mattermost.com/#tag/teams%2Fpaths%2F~1teams~1%7Bteam_id%7D%2Fput) will be added. The setting will be off by default for all new and existing installs, except those deployed on GitLab Omnibus. A System Administrator can enable the API v4 endpoint from the config.json file. [Ticket #9916](https://mattermost.atlassian.net/browse/MM-9916).
7. An unused `ExtraUpdateAt` field will be removed from the channel model. [Ticket #9739](https://mattermost.atlassian.net/browse/MM-9739).

### Known Issues

 - Google login fails on the Classic mobile apps.
 - User can receive a video call from another browser tab while already on a call.
 - Jump link in search results does not always jump to display the expected post.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Channel scroll position flickers while images and link previews load.
 - Numbered lists can sometimes extend beyond the normal post area.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - CTRL/CMD+U shortcut to upload a file doesn’t work on Firefox.

### Contributors
[amyblais](https://github.com/amyblais), [AndersonWebStudio](https://github.com/AndersonWebStudio), [antoineHC](https://github.com/antoineHC), [asaadmahmood](https://github.com/asaadmahmood), [Autre31415](https://github.com/Autre31415), [cometkim](https://github.com/cometkim), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [daanlevi](https://github.com/daanlevi), [DSchalla](https://github.com/DSchalla), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [grundleborg](https://github.com/grundleborg), [guydemi](https://github.com/guydemi), [hmhealey](https://github.com/hmhealey), [icelander](https://github.com/icelander), [iri-dw](https://github.com/iri-dw), [it33](https://github.com/it33), [james-mm](https://github.com/james-mm), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jordanbuchman](https://github.com/jordanbuchman), [jwilander](https://github.com/jwilander), [kethinov](https://github.com/kethinov), [koxen](https://github.com/koxen), [lfbrock](https://github.com/lfbrock), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lindy65](https://github.com/lindy65), [lisakycho](https://github.com/lisakycho), [liusy182](https://github.com/liusy182), [Merlin2001](https://github.com/merlin2001), [michaeltaylor-kerauno](https://github.com/michaeltaylor-kerauno), [mkraft](https://github.com/mkraft), [n1aba](https://github.com/n1aba), [pichouk](https://github.com/pichouk), [saturninoabril](https://github.com/saturninoabril), [stanchan](https://github.com/stanchan), [sudheerDev](https://github.com/sudheerDev), [tejasbubane](https://github.com/tejasbubane), [timconner](https://github.com/timconner), [tomo667a](https://github.com/tomo667a), [yuya-oc](https://github.com/yuya-oc)

## Release v4.9 - Feature Release

 - **v4.9.4, released 2018-06-04**
   - Mattermost v4.9.4 contains a moderate severity security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.9.3, released 2018-05-15**
   - Fixed an issue where plugin configuration got corrupted upon saving the configuration via the System Console.
 - **v4.9.2, released 2018-05-04**
   - Fixed an issue with permissions migration when ``AllowEditPost`` was set to "Always".
 - **v4.9.1, released 2018-04-27**
   - Fixed an issue where System Console permissions settings displayed a false error when running High Availability mode.
   - Fixed a race condition on loading roles in the System Console.
   - Reverted a change causing significant performance degradation when loading posts.
   - Fixed a performance issue causing significant initial load time for the Desktop application.
 - **v4.9.0, released 2018-04-16**
   - Original 4.9.0 release

### Highlights

#### Channel Mute
 - Added a `/mute` command, meaning that when a channel is muted, desktop, push and email notifications are not sent for the channel.
 - Channel Mute is also accessible via Channel Notification Preferences.
 - A muted channel gets sorted at the bottom of the left-hand sidebar section.

#### Teammate Name Display Setting
 - Added the setting for rendering of at-mentions by the teammate name display back to the Account Settings.

#### Team Icons
 - Added support for team icons in the team sidebar.

#### Global Relay (Beta) ([Enterprise Edition E20](https://about.mattermost.com/pricing/) Add-On)
 - Added export support for Global Relay as a compliance solution. [Learn more here](https://about.mattermost.com/default-compliance-export-documentation).

### Improvements

#### Web User Interface
 - Users can now set their timezone in **Account Settings > Timezone**.
 - Cursor now returns to the reply thread input box after deleting a reply on the right-hand sidebar.

#### Performance
 - Decreased channel load time by optimizing database queries used to fetch threads and parent posts in a channel.
 - Decreased load time of large channels with 5,000+ messages by up to 90% by optimizing many client functions related to rendering posts and threads.
 - Changing properties other than Site URL in ``/general/logging`` section will now require a server restart before taking effect.

#### Plugins (Beta)
 - Plugins now have more flexibility to format text, emojis and Markdown.
 - Added support for plugins to add actions to the sidebar dropdowns.

#### Administration
 - Added support for AWS Identity and Access Management (IAM) roles for Amazon S3 file storage.
 - Added a "Test Connection" button to test Amazon S3 connection.

#### Enterprise Edition
 - When `ExperimentalTownSquareIsReadOnly` is set to `true`, non-admins can no longer react to messages, pin messages or update channel information.
 - Added cache invalidation totals to [Performance Monitoring](https://docs.mattermost.com/deployment/metrics.html).

### Bug Fixes

 - Fixed server log 404 error messages "We couldn't get the emoji" for numeric emojis.
 - Fixed an issue where cursor jumped to end of line when trying to edit text in the middle of search bar.
 - Fixed an issue where a download link opened images in a new tab instead of downloading them.
 - Fixed an issue where Direct Message channel with yourself did not show up in channel switcher.
 - Fixed an issue where deleting one username from "add member to a channel" field deleted all names.
 - Fixed an issue where View/Manage members should have been sorted by username, not online status.
 - Fixed an issue where a non-system-admin should not see `Is Trusted` option on OAuth 2.0 integrations.
 - Fixed an issue with being unable to click on pinned post, channel members, and so on with keyboard focus on search box.
 - Fixed an issue where Mattermost only imported first user during Slack import.
 - Fixed an issue where cleared search term reappeared after closing RHS.
 - Fixed an issue where a thumbnail appeared larger than expected in center channel when posting an image while the right hand side was open.
 - Fixed an issue with adding users to channels when the usernames contained periods.
 - Fixed an issue with a JavaScript error when using CMD/CTRL-K keyboard shortcut to change channels.
 - Fixed an issue with not being able to get past second page of `/admin_console/users`.
 - Fixed an issue where ALT+UP/DOWN caused error in console and then stopped working.

### Compatibility

 - IE11 Compatibility View now shows an "Unsupported Browser" error page, [given it's not a supported version](https://docs.mattermost.com/install/requirements.html#pc-web-experience).

#### Removed and Deprecated Features

 - To improve the production use of Mattermost with Docker, the docker image is now running a as non-root user and listening on port 8000. Please read the [upgrade instructions](https://github.com/mattermost/mattermost-docker#upgrading-mattermost-to-49) for important changes to existing installations.

- Several configuration settings have been migrated to roles in the database and changing their `config.json` values no longer takes effect. These permissions can still be modified by their respective System Console settings as before. The affected `config.json` settings are:
   - RestrictPublicChannelManagement
   - RestrictPrivateChannelManagement
   - RestrictPublicChannelCreation
   - RestrictPrivateChannelCreation
   - RestrictPublicChannelDeletion
   - RestrictPrivateChannelDeletion
   - RestrictPrivateChannelManageMembers
   - EnableTeamCreation
   - EnableOnlyAdminIntegrations
   - RestrictPostDelete
   - AllowEditPost
   - RestrictTeamInvite
   - RestrictCustomEmojiCreation

For a list of past and upcoming deprecated features, [see our website](https://about.mattermost.com/deprecated-features/).

#### Upcoming Deprecated Features in Mattermost v5.0

The following deprecations are planned for the Mattermost v5.0 release, which is scheduled for summer/2018. This list is subject to change prior to the release.

1. All API v3 endpoints will be removed. [See documentation](https://api.mattermost.com/#tag/APIv3-Deprecation) to learn more about how to migrate your integrations to API v4. [Ticket #8708](https://mattermost.atlassian.net/browse/MM-8708).
2. `platform` binary will be renamed to mattermost for a clearer install and upgrade experience. All command line tools, including the bulk loading tool and developer tools, will also be renamed from platform to mattermost. [Ticket #9985](https://mattermost.atlassian.net/browse/MM-9985).
3. A new `config.json` setting to whitelist types of protocols for auto-linking will be added. [Ticket #9547](https://mattermost.atlassian.net/browse/MM-9547).
4. A new `config.json` setting to disable the [permanent APIv4 delete team parameter](https://api.mattermost.com/#tag/teams%2Fpaths%2F~1teams~1%7Bteam_id%7D%2Fput) will be added. The setting will be off by default for all new and existing installs, except those deployed on GitLab Omnibus. A System Administrator can enable the API v4 endpoint from the config.json file. [Ticket #9916](https://mattermost.atlassian.net/browse/MM-9916).
5. An unused `ExtraUpdateAt` field will be removed from the channel model. [Ticket #9739](https://mattermost.atlassian.net/browse/MM-9739).

#### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:

 - Under `MessageExportSettings` in `config.json`:
     - Added `"CustomerType": "A9"`, to allow selecting the type of Global Relay customer account the user's organization has.
     - Added `"EmailAddress": ""`, to allow selecting the email address the user's Global Relay server monitors for incoming compliance exports.
 - Under ` "SamlSettings"` in `config.json`:
     - Added `"ScopingIDPProviderId": ""`, to allow an authenticated user to skip the initial login page of their federated Azure AD server, and only require a password to log in.
     - Added `"ScopingIDPName": ""`, to add the name associated with a user's Scoping Identity Provider ID.
 - Under `DisplaySettings"` in `config.json`:
     - Added `"ExperimentalTimezone": false`, to allow selecting the timezone used for timestamps in the user interface and email notifications.

#### API Changes

 - It is required that any new integrations use API v4 endpoints. For more details, and for a complete list of available endpoints, see [https://api.mattermost.com/](https://api.mattermost.com/).
 - All API v3 endpoints have been deprecated and are scheduled for removal in Mattermost v5.0.

#### Database Changes

**Users Table:**

 - Added `Timezone` column.

**Teams Table:**

 - Added `LastTeamIconUpdate` column.

**Channels Table:**

 - Removed `idx_channels_displayname` index.

### Known Issues
 - Google login fails on the Classic mobile apps.
 - User can receive a video call from another browser tab while already on a call.
 - Jump link in search results does not always jump to display the expected post.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Channel scroll position flickers while images and link previews load.
 - Numbered lists can sometimes extend beyond the normal post area.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - CTRL/CMD+U shortcut to upload a file doesn’t work on Firefox.

### Contributors

[amyblais](https://github.com/amyblais), [AndersonWebStudio](https://github.com/AndersonWebStudio), [asaadmahmood](https://github.com/asaadmahmood), [ccbrown](https://github.com/ccbrown), [chclaus](https://github.com/chclaus), [chumbalum](https://github.com/chumbalum), [cjohannsen81](https://github.com/cjohannsen81), [CoolMoeDee](https://github.com/CoolMoeDee), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [dmeza](https://github.com/dmeza), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [gajananpp](https://github.com/gajananpp), [GitHubJasper](https://github.com/GitHubJasper), [gnufede](https://github.com/gnufede), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [icelander](https://github.com/icelander), [it33](https://github.com/it33), [james-mm](https://github.com/james-mm), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [koxen](https://github.com/koxen), [letsila](https://github.com/letsila), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lindy65](https://github.com/lindy65), [mkraft](https://github.com/mkraft), [moonmeister](https://github.com/moonmeister), [MusikPolice](https://github.com/MusikPolice), [panditsavitags](https://github.com/panditsavitags), [philippe-granet](https://github.com/philippe-granet), [pichouk](https://github.com/pichouk), [qichengzx](https://github.com/qichengzx), [Rudloff](https://github.com/Rudloff), [R-Wang97](https://github.com/R-Wang97), [saturninoabril](https://github.com/saturninoabril), [stanchan](https://github.com/stanchan), [stephenkiers](https://github.com/stephenkiers), [sudheerDev](https://github.com/sudheerDev), [svelle](https://github.com/svelle), [tejasbubane](https://github.com/tejasbubane), [thePanz](https://github.com/thePanz), [timconner](https://github.com/timconner), [tomo667a](https://github.com/tomo667a), [Vorlif](https://github.com/Vorlif), [yuya-oc](https://github.com/yuya-oc)

## Release v4.8 - Feature Release

 - **v4.8.2, released 2018-06-04**
   - Mattermost v4.8.2 contains a moderate severity security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.8.1, released 2018-04-09**
   - Mattermost v4.8.1 contains multiple security fixes ranging from low to high severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
   - Fixed a performance issue by removing the `DisplayName` index on the Channels table.
 - **v4.8.0, released 2018-03-16**
   - Original 4.8.0 release

### Security Update

- Mattermost v4.8.0 contains multiple security fixes ranging from low to high severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Highlights

#### Enhanced compatibility with CloudFront

 - Added support for configuring CloudFront to host Mattermost's static assets.
 - Allows for improved caching performance and shorter load times for those members of your team geographically distributed throughout the world.

#### SAML Migration Command  ([Enterprise Edition E20](https://about.mattermost.com/pricing/))

 - Added a CLI command to easily migrate users to SAML.

### Improvements

#### Web User Interface
 - Added a web app build hash to About Mattermost dialog to tell what version of the web app is being used.
 - Switched search bar to a button in tablet view, to increase how much space is available in the channel header.

#### Performance
 - Reduced load times by optimizing database queries and WebSocket events destined for a single user.
 - Created an iOS endpoint that enables users to upload files larger than 20MB.
 - Improved caching of `getRootPosts` call.

#### 508 Compliance
 - Added alt attribute to profile pictures.

#### Integrations
 - Updated incoming webhooks to accept multipart/form-data content type such as that supplied by `curl -F`.

#### Notifications
 - A system message is now posted when a channel is moved between teams by the CLI command.

#### Authentication
 - Reduced OAuth SSO login errors by falling back to a constructed URL if Site URL is blank.

#### System Console
 - Removed plugin upload setting from System Console UI and prevented switching the setting from the API.
 - Added paging to system console log viewer and set default value of `per_paging` for logs to 1000.

### Bug Fixes
 - Fixed an issue where sidebar unreads text setting was ignored in custom theme.
 - Fixed an issue where emoji picker had an empty line at the bottom of the list.
 - Fixed an issue with Markdown help wrapping on a second line in Edit Message dialog.
 - Fixed an issue where after leaving last team the "Logout" link did nothing.
 - Fixed an issue where focus was sometimes wrong on delete post modal.
 - Fixed an issue where the bulk import tool didn't force Town Square membership.
 - Fixed duplicate calls of the "view" request when switching channels.
 - Fixed an issue where channel name was included in push notifications if someone posted only files with Push Notification Contents set to not include channel name.
 - Fixed an issue where attempting to preview an attached document failed to finish "loading" if the file extension didn't match the actual file type.
 - Fixed an issue where focus was not set to input box after replying to a message in Classic Mobile App.
 - Fixed an issue where a username such as "user.name" gets a highlight only on "name" when @-icon is clicked.
 - Fixed an issue where the "More Unreads Above" indicator didn't always work.
 - Fixed an issue where IE11 posted placeholder from hidden textbox.
 - Fixed an issue where last channel was not remembered after refresh when switching teams.
 - Fixed an issue with no auto-focusing into input text when attaching a file in Classic Mobile App.
 - Fixed an issue with not being able to type with composed characters (e.g. CJK) in View Team Members modal and channel switcher.
 - Fixed an issue where insecure images were loaded by sending client before proxying.
 - Fixed an issue with sandboxing support for CentOS and Bosh.
 - Fixed an issue where JIRA plugin posts were not properly truncated.
 - Fixed an issue where tall/wide emojis appeared stretched in emoji picker.
 - Fixed an issue where web app could not be built if not in a git repository.
 - Fixed an issue where jumping to a search result did not always load the context posts.
 - Fixed an issue where edit box changed size on switching to markdown preview in some languages.

### Compatibility

#### Removed and Deprecated Features

 - All API v3 endpoints have been deprecated and are scheduled for removal in Mattermost v5.0.
 - An unused `ExtraUpdateAt` field will be removed from the channel model in Mattermost v5.0.
 - As Mattermost moves to a role-based permissions system in v4.9, a number of configuration settings will be migrated to roles in the database and changing their `config.json` values will no longer take effect. These permissions can still be modified by their respective System Console settings. The `config.json` settings to be migrated are:
   - RestrictPublicChannelManagement
   - RestrictPrivateChannelManagement
   - RestrictPublicChannelCreation
   - RestrictPrivateChannelCreation
   - RestrictPublicChannelDeletion
   - RestrictPrivateChannelDeletion
   - RestrictPrivateChannelManageMembers
   - EnableTeamCreation
   - EnableOnlyAdminIntegrations
   - RestrictPostDelete
   - AllowEditPost
   - RestrictTeamInvite
   - RestrictCustomEmojiCreation

For a list of past and upcoming deprecated features, [see our website](https://about.mattermost.com/deprecated-features/).

#### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:

 - Under `ServiceSettings` in `config.json`:
    - Added `AllowCookiesForSubdomains`, to ensure that the domain parameter is set for cookies, which allows the browser to send the cookies to subdomains as well.
    - Added `WebsocketURL`, which allows the server to instruct clients where they should try to connect WebSockets to.
    - Changed `EnableAPIV3` setting to `false` for new installs, as all API v3 endpoints have been deprecated and are scheduled for removal in Mattermost v5.0.

### API Changes

 - It is required that any new integrations use API v4 endpoints. For more details, and for a complete list of available endpoints, see [https://api.mattermost.com/](https://api.mattermost.com/).
 - All API v3 endpoints have been deprecated and are scheduled for removal in Mattermost v5.0.

#### RESTful API v4 Changes

 - Updated `POST /files` to support requests with only the `channel_id` and `filename` defined as query parameters with the contents of a single file in the body of the request.

### Known Issues

 - Google login fails on the Classic mobile apps.
 - User can receive a video call from another browser tab while already on a call.
 - Jump link in search results does not always jump to display the expected post.
 - Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
 - Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
 - Searching with Elasticsearch enabled may not always highlight the searched terms.
 - Team sidebar on desktop app does not update when channels have been read on mobile.
 - Channel scroll position flickers while images and link previews load.
 - Numbered lists can sometimes extend beyond the normal post area.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - CTRL/CMD+U shortcut to upload a file doesn’t work on Firefox.

### Contributors

[Alexgoodman7](https://github.com/Alexgoodman7), [amyblais](https://github.com/amyblais), [AndersonWebStudio](https://github.com/AndersonWebStudio), [andruwa13](https://github.com/andruwa13), [asaadmahmood](https://github.com/asaadmahmood), [avasconcelos114](https://github.com/avasconcelos114), [billybrown1](https://github.com/billybrown1), [ccbrown](https://github.com/ccbrown), [chumbalum](https://github.com/chumbalum), [cometkim](https://github.com/cometkim), [CoolTomatos](https://github.com/CoolTomatos), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [GitHubJasper](https://github.com/GitHubJasper), [gnufede](https://github.com/gnufede), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [icelander](https://github.com/icelander), [it33](https://github.com/it33), [james-mm](https://github.com/james-mm), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kemenaran](https://github.com/kemenaran), [koxen](https://github.com/koxen), [leblanc-simon](https://github.com/leblanc-simon), [letsila](https://github.com/letsila), [lfbrock](https://github.com/lfbrock), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lindy65](https://github.com/lindy65), [lip-d](https://github.com/lip-d), [liusy182](https://github.com/liusy182), [lmikaellukerad](https://github.com/lmikaellukerad), [mkraft](https://github.com/mkraft), [moonmeister](https://github.com/moonmeister), [MusikPolice](https://github.com/MusikPolice), [pichouk](https://github.com/pichouk), [rqtaylor](https://github.com/rqtaylor), [saturninoabril](https://github.com/saturninoabril), [stanchan](https://github.com/stanchan), [stephenkiers](https://github.com/stephenkiers), [tejasbubane](https://github.com/tejasbubane), [thePanz](https://github.com/thePanz), [torgeirl](https://github.com/torgeirl), [Vaelor](https://github.com/Vaelor), [vordimous](https://github.com/vordimous), [XinyueWang94](https://github.com/XinyueWang94), [yuya-oc](https://github.com/yuya-oc)

## Release v4.7 - Feature Release

 - **v4.7.4, released 2018-04-09**
   - Mattermost v4.7.4 contains multiple security fixes ranging from low to high severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
   - Fixed a performance issue by removing the `DisplayName` index on the Channels table.
 - **v4.7.3, released 2018-03-09**
   - Mattermost v4.7.3 contains a moderate severity security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.7.2, released 2018-02-23**
   - Fixed an issue where message attachments didn’t render emojis.
   - Fixed an issue where channels with a name 26 characters long were inaccessible with a 404 error.
   - Fixed “We couldn’t get the emoji” server log messages.
   - Fixed an issue with being unable to switch to direct or group message channels via CTRL/CMD+K channel switcher or via “msg/groupmsg” slash commands.
   - Fixed an issue where clicking on "Send Message" from a user's profile popover redirected to Town Square instead of the user's direct message channel.
   - Fixed an issue where links to direct and group message channels opened in a new tab.
 - **v4.7.1, released 2018-02-20**
   - Fixed an issue with [compliance export](https://docs.mattermost.com/administration/compliance-export.html) outputs, resulting in `Failed to update ChannelMemberHistory table` error  messages in the log when a user joins or leaves a channel. Issue updates [posted here](https://mattermost.atlassian.net/browse/MM-9633).
 - **v4.7.0, released 2018-02-16**
   - Original 4.7.0 release

### Security Update

- Mattermost v4.7.0 contains multiple security fixes ranging from low to high severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Highlights

#### Client-Side Performance

 - Added user-based rate limiting, in addition to rate limiting API access by IP address.
 - Decreased page load time by loading custom emojis asynchronously rather than all on first page load.
 - Optimized channel autocomplete (~) query by returning client-side results immediately.
 - Decreased the size of most image assets by more than 25% by running `pngquant` to remove unnecessary metadata from PNGs.

#### Image Proxy Support

 - Image proxy servers increase performance through a layer of caching, and provide custom options to resize images.
 - Three new configuration keys, `ImageProxyType`, `ImageProxyURL`, `ImageProxyOptions`, ensure that posts served to the client will have their markdown modified such that all images are loaded through a proxy.

#### Updated Image Thumbnails

 - Updated the appearance of image thumbnails, so that single thumbnails will now expand to a larger preview without clicking the image to open the preview window.

#### Experimental Setting for Unreads Sidebar Section

 - Added an experimental setting to group unread channels in the channel sidebar. The setting [must first be enabled by the System Admin](https://docs.mattermost.com/administration/config-settings.html#group-unread-channels-experimental), by replacing `disabled` with either `default_off` or `default_on` in config.json.

### Improvements

#### Web User Interface
 - Added a status icon in the channel member list and sorted it by user status.
 - Added ability to preview images found in link previews.
 - Added a `Copy Link` option for sidebar channels in the Desktop App.
 - Added focus on the text box after hitting "Edit" on Account Settings options.
 - Improved formatting of quotes in the channel header.
 - Added a date separator for search results.
 - Channel names are now sorted correctly in the left-hand-side by taking non-alphabetical characters into consideration (e.g. brackets, hash sign, etc.)

 #### Integrations
 - Added username and profile picture to incoming webhook set up pages.
 - Added support for Slack attachments in outgoing webhook responses.

#### Emoji Picker
 - Added the ability to navigate emoji picker with the keyboard.
 - Added paging and search of custom emojis to webapp emoji picker.

#### Channels
 - Users are directed to the last channel they viewed in a team when switching to that team.
 - Changed URLs of Direct Messages to use the form of `https://servername.com/messages/@username`, letting users open a direct message with each other via URL.

#### Notifications
 - Added a system message when a team is changed from public to private.

#### Plugins (Beta)
 - Zoom plugin now supports on-premise Zoom servers.

#### Enterprise Edition
- Increased max length of `User.Position` field to 128 characters to meet LDAP max length.
- Increased OAuth state parameter limit. Some systems may send a state longer than 128 characters.

### Bug Fixes
 - Fixed an issue where OAuth account creation error page was unformatted.
 - Fixed tab and alt-tab keyboard navigation for links on sign-in page.
 - Fixed an issue where plugin slash commands didn't override username or icon.
 - Fixed an issue where pagination for team members modal showed a next button when there are no more users to show.
 - Fixed an issue where at-channel in `/header` should not trigger confirmation modal.
 - Fixed an issue where auto-generated SAML Service provider login URL had two slashes instead of one.
 - Fixed an issue where no unread mention appeared on non-mobile platform after receiving push notification.
 - Fixed an issue where the text box was hidden by the keyboard when replying to a post in mobile view.
 - Fixed username autocomplete not working with mixed cases.
 - Fixed not being able to type Korean quickly in some dialogs.
 - Fixed an issue where notification preference settings didn't respect case sensitivity for mention highlighting.
 - Fixed where, after an ephemeral message, couldn't use `+:emoji:` to react to the previous message.
 - Fixed Mattermost not loading on Firefox if the `media.peerconnection.enabled` setting in Firefox is set to false.
 - Fixed login screen sometimes flashing before Mattermost server loads.
 - Fixed an issue where bot messages from the Zoom plugin ignored the Zoom API URL field for on-prem Zoom servers.
 - Disabled pull-to-refresh feature on Android (Chrome) to prevent unwanted page refresh.
 - Fixed an issue where clicking `Save` in `Rename Channel` modal without changes did nothing.
 - Fixed emoji picker search being case-sensitive.
 - Fixed timestamp not being clickable in desktop mobile view.
 - Fixed an issue where deleting a team via the API broke the web user interface.

### Compatibility

#### Removed and Deprecated Features

- All API v3 endpoints have been deprecated, and scheduled for removal in Mattermost v5.0.
- The `mentionKeys` prop in post type plugins is now removed to fix case sensitive mention highlighting. Plugins can retrieve the `mentionKeys` prop from the store as needed.
- The permanent query parameter of the DELETE `/teams/{team_id}` APIv4 endpoint is not removed as previously announced, given customer and community feedback.
- As Mattermost moves to a role based permissions system in v4.8, a number of configuration settings will be migrated to roles in the database, and changing their `config.json` values will no longer take effect. These permissions can still be modified by their respective System Console settings. The `config.json` settings to be migrated are:
  - RestrictPublicChannelManagement
  - RestrictPrivateChannelManagement
  - RestrictPublicChannelCreation
  - RestrictPrivateChannelCreation
  - RestrictPublicChannelDeletion
  - RestrictPrivateChannelDeletion
  - RestrictPrivateChannelManageMembers
  - EnableTeamCreation
  - EnableOnlyAdminIntegrations
  - RestrictPostDelete
  - AllowEditPost
  - RestrictTeamInvite

For a list of past and upcoming deprecated features, [see our website](https://about.mattermost.com/deprecated-features/).

#### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:

 - Under `ServiceSettings` in `config.json`:
    - Added `"ImageProxyType": ""`, `"ImageProxyOptions": ""`, and `"ImageProxyURL": ""` to ensure posts served to the client will have their markdown modified such that all images are loaded through a proxy.
    - Added `"ExperimentalGroupUnreadChannels": disabled` to show an unread channel section in the webapp sidebar. The setting must first be enabled by the System Admin, by replacing `disabled` with either `default_off` or `default_on`.
    - Added `"ExperimentalEnableDefaultChannelLeaveJoinMessages": true` that allows disabling of leave/join messages in the default channel, usually Town Square.
 - Under `RateLimitingSettings` in `config.json`:
    - Added `"VaryByUser": false`, a user-based rate limiting, to rate limit on token and on userID.

### API Changes

 - It is required that any new integrations use API v4 endpoints. For more details, and for a complete list of available endpoints, see [https://api.mattermost.com/](https://api.mattermost.com/).
 - All API v3 endpoints have been deprecated, and scheduled for removal in Mattermost v5.0.

#### RESTful API v4 Changes

 - Added `GetChannelByName` and `GetTeamByName` to auto lowercase team and channel names in API requests. This ensures that the channel name is automatically lowercased for endpoints taking team or channel names as URL parameters.
 - Added `POST /emoji/search`, `GET /emojis/name/{emoji_name}`, and `GET /emoji/autocomplete` to add consistency with user search/autocomplete endpoints. These API endpoints ensure that the benefits of `GET` for important performance related actions such as autocompleting are included.
 - Added `/users/tokens/search` to allow System Admin to be able to find, manage and revoke personal access tokens as needed. This endpoint gets all tokens for all users if one has the `manage_system` permission.

### WebSocket Event Changes

 - Added `delete_team` web socket event to notify client whenever a team is deleted (e.g. via API call).

### Database Changes

**Users Table:**

 - Increased size of `Position` field from 35 to 128 characters.

**OAuthAuthData Table:**

 - Increased size of `State` field from 128 to 1024 characters.

**ChannelMemberHistory Table:**

 - Removed `Email` column.
 - Removed `Username` column.

### Known Issues

- Google login fails on the Classic mobile apps.
- User can receive a video call from another browser tab while already on a call.
- Jump link in search results does not always jump to display the expected post.
- Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
- Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
- Searching with Elasticsearch enabled may not always highlight the searched terms.
- Team sidebar on desktop app does not update when channels have been read on mobile.
- Channel scroll position flickers while images and link previews load.
- CTRL/CMD+U shortcut to upload a file doesn't work on Firefox.
- Numbered lists can sometimes extend beyond the normal post area.
- Slack import through the CLI fails if email notifications are enabled.
- Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
- `[WARN] plugin sandboxing is not supported. plugins will run with the same access level as the server` log message is created when sandboxing isn't enabled for plugins. If you don't use plugins, you can ignore this message. If you have plugins enabled, [learn how to enable sandboxing](https://developers.mattermost.com/extend/plugins/security/#sandboxing).

### Contributors

[amyblais](https://github.com/amyblais), [AndersonWebStudio](https://github.com/AndersonWebStudio), [andruwa13](https://github.com/andruwa13), [asaadmahmood](https://github.com/asaadmahmood), [bbodenmiller](https://github.com/bbodenmiller), [Brunzer](https://github.com/Brunzer), [ccbrown](https://github.com/ccbrown), [chclaus](https://github.com/chclaus), [cherniavskii](https://github.com/cherniavskii), [CometKim](https://github.com/CometKim), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [cvitter](https://github.com/cvitter), [darkman](https://github.com/darkman), [der-test](https://github.com/der-test), [dlahn](https://github.com/dlahn), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [fermulator](https://github.com/fermulator), [gig177](https://github.com/gig177), [grundleborg](https://github.com/grundleborg), [Hanzei](https://github.com/Hanzei), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [james-mm](https://github.com/james-mm), [jarredwitt](https://github.com/jarredwitt), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kemenaran](https://github.com/kemenaran), [knechtionscoding](https://github.com/knechtionscoding), [laginha87](https://github.com/laginha87), [lasley](https://github.com/lasley), [letsila](https://github.com/letsila), [lfbrock](https://github.com/lfbrock), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lindy65](https://github.com/lindy65), [liusy182](https://github.com/liusy182), [Matterchen](https://github.com/Matterchen), [mkraft](https://github.com/mkraft), [MusikPolice](https://github.com/MusikPolice), [phuihock](https://github.com/phuihock), [pichouk](https://github.com/pichouk), [Rohlik](https://github.com/Rohlik), [R-Wang97](https://github.com/R-Wang97), [santos22](https://github.com/santos22), [saturninoabril](https://github.com/saturninoabril), [stephenkiers](https://github.com/stephenkiers), [sudheerDev](https://github.com/sudheerDev), [tayre](https://github.com/tayre), [tejasbubane](https://github.com/tejasbubane), [tkbky](https://github.com/tkbky), [Tristramg](https://github.com/Tristramg), [ulm0](https://github.com/ulm0), [watadarkstar](https://github.com/watadarkstar), [xuxip](https://github.com/xuxip), [yeoji](https://github.com/yeoji), [yuya-oc](https://github.com/yuya-oc)

## Release v4.6 - Feature Release

 - **v4.6.3, release date 2018-04-09**
   - Mattermost v4.6.3 contains a low severity security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.6.2, release date 2018-02-23**
   - Mattermost v4.6.2 contains multiple security fixes ranging from low to high severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.6.1, release date 2018-01-30**
   - Fixed an issue where Let's Encrypt certificates were broken on Mattermost servers. The cache will be deleted upon upgrade so your certificate will be immediately renewed. Moreover, port 80 must be forwarded through a firewall, with [Forward80To443](https://docs.mattermost.com/administration/config-settings.html#forward-port-80-to-443) `config.json` setting set to `true`, to complete the Let's Encrypt certification.
 - **v4.6.0, released 2018-01-16**
   - Original 4.6.0 release

### Highlights

#### Client-Side Performance

- Decreased channel switching time up to 45% by reducing post mounting time.
- Decreased up to 85% of the memory retained following a channel switch by fixing memory leaks of the `post_time.jsx` component.
- Decreased size of the most used icons and logos by 70-80% by running `pngquant` to remove unnecessary metadata from PNGs.

### Improvements

#### Web User Interface

- Added a loading indicator while pinned posts and flagged posts lists are loading.
- Added a loading indicator to MFA sign in button.
- Added a tooltip for the '+' button when adding emoji reactions.
- Channel switcher (CTRL/CMD+K) now filters by usernames, full names and nicknames.
- Channel links are now rendered in the channel header.
- File names are now shown in attachment previews.

#### Plugins (Beta)

- Plugins now support slash commands.

#### Notifications

- Updated default notification settings for new accounts to provide a better onboarding experience. Each of these can be configured in Account Settings. In particular, the updated default settings include:
   - Desktop notifications only sent for mentions and direct messages.
   - Mobile push notifications only sent when the user is away or offline, not when online.
   - Mentions of the user's first name doesn't trigger mentions.

#### 508 Compliance

- Default language is now declared in HTML for Mattermost webpages.
- Position of status indicators and reply icons updated when no CSS is rendered.
- Use programmatically identifiable headings for team and channel name.

#### Administration

- Incoming webhook display name is now included in the post.Props field for better auditing.
- System Admins can now reset their own password from the System Console users list.

### Bug Fixes

- Username updates are now immediately visible across all browser tabs.
- Server logs no longer contain info messages about initializing plugins when plugins are disabled.
- Fixed Mattermost not loading on Firefox v52.
- Fixed issues with user at-mention autocomplete when using Tab multiple times.
- Fixed an issue where typing an emoji reaction didn't add it to recently used emojis list.
- OAuth and SAML users can now be deactivated from the Mattermost System Console, assuming they are also deactivated in the SSO provider.
- Fixed email address validation for Microsoft Outlook formatted email addresses.
- Fixed an issue where posts sometimes didn't send on iOS Classic app.
- Team name can no longer be edited to be only one character long.
- Editing a message to remove all text no longer deletes the message if it contains a file attachment.
- Fixed an issue where searching for a channel using the second or third word in the name didn't work.
- Other users no longer see deleted GIF previews in reply threads.
- Fixed an issue where channels with Japanese or Cyrillic characters couldn't be created.
- Fixed timestamp minute display for Zoom plugins.
- Fixed an issue where page would load infinitely when trying to join a team with maximum capacity.
- Fixed an issue where channel notification preferences reverted to defaults after updating preferences in one of the channels.

### Compatibility

#### Removed and Deprecated Features

- All API v3 endpoints are now deprecated, and scheduled for removal in Mattermost v5.0.
- The permanent query parameter of the DELETE `/teams/{team_id}` APIv4 endpoint for permanently deleting a team is scheduled for removal in Mattermost v4.7.

For a list of past and upcoming deprecated features, [see our website](https://about.mattermost.com/deprecated-features/).

#### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

**Changes to Team Edition and Enterprise Edition**:

- Under `ServiceSettings` in `config.json`:
  - Added `"EnableTutorial": true` to control whether tutorial is shown to end users after account creation. This setting is experimental and may be replaced or removed in a future release.
- Under `TeamSettings` in `config.json`:
  - Added `"ExperimentalPrimaryTeam": ""` to set the primary team of the server. This setting is experimental and may be replaced or removed in a future release.
- Under `EmailSettings` in `config.json`:
  - Added `"LoginButtonColor": ""`, `"LoginButtonBorderColor": ""` and `"LoginButtonTextColor": ""` to set the style of the email login button for white labelling purposes.

**Additional Changes to Enterprise Edition**:

- Under `LdapSettings` in `config.json`:
  - Added `"LoginButtonColor": ""`, `"LoginButtonBorderColor": ""` and `"LoginButtonTextColor": ""` to set the style of the LDAP login button for white labelling purposes.
- Under `SamlSettings` in `config.json`:
  - Added `"LoginButtonColor": ""`, `"LoginButtonBorderColor": ""` and `"LoginButtonTextColor": ""` to set the style of the SAML login button for white labelling purposes.

### API Changes

- It is required that any new integrations use API v4 endpoints. For more details, and for a complete list of available endpoints, see [https://api.mattermost.com/](https://api.mattermost.com/).
- All API v3 endpoints are now deprecated, and scheduled for removal in Mattermost v5.0.
- The permanent query parameter of the DELETE `/teams/{team_id}` APIv4 endpoint for permanently deleting a team is scheduled for removal in Mattermost v4.7.

#### RESTful API v4 Changes

- Added `/users/{user_id}/auth` to update a user's authentication method. This can be used to change them to/from LDAP authentication, for example.

#### Plugin API Changes (Beta)

- Added `RegisterCommand` to register a custom slash command. When the command is triggered, your plugin can fulfil it via the `ExecuteCommand` hook.
- Added `UnregisterCommand` to unregister a command previously registered via `RegisterCommand`.
- Added `GetChannelMember` to get a channel membership for a user.

#### Plugin Hook Changes (Beta)

- Added `ExecuteCommand` hook to execute a command that was previously registered via the `RegisterCommand` plugin API.

### Database Changes

**IncomingWebhooks Table:**
- Renamed `PostUsername` column to `Username`.
- Renamed `PostIconURL` column to `IconURL`.

### Known Issues

- Google login fails on the Classic mobile apps.
- User can receive a video call from another browser tab while already on a call.
- Jump link in search results does not always jump to display the expected post.
- Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
- Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
- Searching with Elasticsearch enabled may not always highlight the searched terms.
- Team sidebar on desktop app does not update when channels have been read on mobile.
- Channel scroll position flickers while images and link previews load.
- CTRL/CMD+U shortcut to upload a file doesn't work on Firefox.
- Numbered lists can sometimes extend beyond the normal post area.
- Slack import through the CLI fails if email notifications are enabled.
- Letters are skipped in a few dialogs when using Korean keyboard in IE11.
- Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
- Deleting a team via the API breaks the user interface.
- Bot messages from the Zoom plugin ignore the Zoom API URL field for on-prem Zoom servers.

### Contributors

- [amyblais](https://github.com/amyblais), [AndersonWebStudio](https://github.com/AndersonWebStudio), [asaadmahmood](https://github.com/asaadmahmood), [ccbrown](https://github.com/ccbrown), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [cvitter](https://github.com/cvitter), [dlahn](https://github.com/dlahn), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [g3d](https://github.com/g3d), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [james-mm](https://github.com/james-mm), [jarredwitt](https://github.com/jarredwitt), [jespino](https://github.com/jespino), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [letsila](https://github.com/letsila), [lfbrock](https://github.com/lfbrock), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lindy65](https://github.com/lindy65), [lisakycho](https://github.com/lisakycho), [liusy182](https://github.com/liusy182), [LordVeovis](https://github.com/LordVeovis), [Matterchen](https://github.com/Matterchen), [mkraft](https://github.com/mkraft), [MusikPolice](https://github.com/MusikPolice), [panditsavitags](https://github.com/panditsavitags), [pichouk](https://github.com/pichouk), [pixelbrackets](https://github.com/pixelbrackets), [pruthvip](https://github.com/pruthvip), [R-Wang97](https://github.com/R-Wang97), [saturninoabril](https://github.com/saturninoabril), [skvale](https://github.com/skvale), [stephenkiers](https://github.com/stephenkiers), [sudheerDev](https://github.com/sudheerDev), [sumantro93](https://github.com/sumantro93), [tayre](https://github.com/tayre), [tborg](https://github.com/tborg), [tejasbubane](https://github.com/tejasbubane), [watadarkstar](https://github.com/watadarkstar), [yuya-oc](https://github.com/yuya-oc)

## Release v4.5 - Feature Release

 - **v4.5.2, release date 2018-02-23**
   - Mattermost v4.5.2 contains multiple security fixes ranging from low to high severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.5.1, released 2018-01-16**
   - Fixed an issue where Mattermost wouldn't load on certain versions of Firefox, including v52-54 and v57 in private mode.
 - **v4.5.0, released 2017-12-16**
   - Original 4.5.0 release

### Highlights

#### Zoom Plugin (Beta)

- [Zoom](https://www.zoom.us/) video calling and screensharing plugin. Learn more [here](https://about.mattermost.com/default-zoom-documentation).
- Manage plugins from the **System Console > Plugins (Beta)** section.

#### Actiance Support (Beta) ([Enterprise Edition E20](https://about.mattermost.com/pricing/) Add-On)

- Compliance export support for [Actiance](https://www.actiance.com/) as a compliance solution. Learn more [here](https://about.mattermost.com/default-compliance-export-documentation).
- Access compliance export from the **System Console > Advanced > Compliance Export (Beta)**.

### Improvements

#### Web User Interface
- `CTRL/CMD` + `/` now toggles the keyboard shortcuts dialog.
- Link previews now appear in the right-hand side in comment threads.
- Timestamp permalinks now open in the current view on desktop and browser.
- Pinned posts are now sorted newest to oldest.
- Updated markdown to better handle non-Latin characters in URLs.
- Added WebRTC call icon to desktop mobile view header.
- Added a '+' sign to quickly add emoji reactions to a post.
- Added support for different emoji skintones.
- Added inline playback for GIF attachments.

#### Integrations

- Added an option for an outgoing webhook to reply to the posted message as a comment.
- JIRA plugin is now bundled as a pre-packaged plugin manageable from the System Console > Plugins > Management.
- Added support for mentions with <@userid>, <!channel>, <!all> and <!here> in webhook posts.
- Personal access tokens can now be temporarily deactivated in the Account Settings.

#### Channels

- Direct Message channels with deactivated users are now hidden in the sidebar and can be reopened from the **More...**  Direct Messages list.
- You can now open a direct message channel with yourself.

#### Notifications

- Removed unnecessary log messages posted when pending email notifications are deleted because a user comes online before the batch is sent.
- Desktop notification icon has been updated on Edge browsers.

#### Keyboard Shortcuts

- Added a `/groupmsg` command to start a new group message channel.
- Added CTRL+SHIFT+L to set focus to the message input box.

#### System Console

- Added a confirm modal to the Data Retention settings page.
- Added settings pages for uploading and managing plugins in the System Console > Plugins (Beta) section.
- Added the ability to revoke a user's sessions from the System Console.

### Bug Fixes

- Closing a direct or group message channel no longer purges channel preferences.
- Users no longer get a blank page after hitting "x" on a deleted message in permalink view.
- Fixed an issue where `AmazonS3Region` defaults to us-east-1 regardless of the value input.
- Channel links render as expected when linking to a channel that the current user does not belong to.
- Uppercase letter is no longer required for a password if the password requirement is set to at least 5 characters and a number.
- Profile image updates are now visible in other active clients and the right-hand side after the change.
- Plugins can no longer be uploaded if they have the same plugin ID.
- Creating a channel with a name including a reserved word no longer breaks the user interface.
- Fixed the AD/LDAP Test Connection button.
- Fixed an issue causing `invalid or expired session` server logs.
- Removed a duplicate error message on the login page after a password reset.
- Fixed an issue where the OAuth ClientID and Secret values were missing after setup.
- Emoji picker now works when the right-hand side is expanded.
- Error messages in the System Console user list no longer breaks the user interface.
- Fixed an issue where only System Admins could edit OAuth apps even if integration creation was not restricted to admins.
- Fixed an issue where "New messages v" bubble didn't always clear in a fresh direct message channel.
- Fixed channel preferences not restoring after closing and reopening a direct or group message channel.

### Compatibility

#### Removed and Deprecated Features
- All APIv3 endpoints are scheduled for removal on January 16, 2018.

For a list of past and upcoming deprecated features, [see our website](https://about.mattermost.com/deprecated-features/).

#### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

**Changes to Team Edition and Enterprise Edition**:

- Under `ServiceSettings` in `config.json`:
  - Added `"EnablePreviewFeatures": true` to hide the **Advanced** > **Preview re-release features** section from Account Settings.
  - Added `"CloseUnusedDirectMessages": false` to hide inactive direct message channels from the sidebar.
  - Added `"ExperimentalEnableAuthenticationTransfer": true` to set whether users can change authentication methods.
- Under `EmailSettings` in `config.json`:
  - Added `"UseChannelInEmailNotifications": false` to set whether email notifications contain the channel name in the subject line.
- Under `PluginSettings` in `config.json`:
  - Added `"ClientDirectory": "./client/plugins"` to set the location of client plugins.

**Additional Changes to Enterprise Edition**:

- Added `MessageExportSettings` in `config.json`:
  - Added `"EnableExport": false` to enable message export.
  - Added `"DailyRunTime": "01:00"` to set the time for the daily export job.
  - Added `"ExportFromTimestamp": 0` to set the timestamp for which posts to include in the message export.
  - Added `"FileLocation": "export"` to set the message export location.
  - Added `"BatchSize": 10000` to set how many new posts are batched together to a compliance export file.

### API v4 Changes

- It is recommended that any new integrations use API v4 endpoints. For more details, and for a complete list of available endpoints, see [https://api.mattermost.com/](https://api.mattermost.com/).
- All API v3 endpoints are scheduled for removal on January 16, 2018.

### Known Issues

- Google login fails on the Classic mobile apps.
- User can receive a video call from another browser tab while already on a call.
- Jump link in search results does not always jump to display the expected post.
- Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
- Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
- Searching with Elasticsearch enabled may not always highlight the searched terms.
- Team sidebar doesn't always show unreads from other teams on first load.
- Team sidebar on desktop app does not update when channels have been read on mobile.
- System Admin cannot reset their own password via the System Console.
- Channel scroll position flickers while images and link previews load.
- CTRL/CMD+U shortcut to upload a file doesn't work on Firefox.
- Profile pictures and usernames don't immediately update across tabs or in the right-hand side comment threads.
- Numbered lists can sometimes extend beyond the normal post area.
- Typing an emoji reaction does not add it to recently used emojis.
- Server logs contain messages about initializing plugins even when plugins are disabled.

### Contributors

/mattermost-webapp

- [asaadmahmood](https://github.com/asaadmahmood), [avasconcelos114](https://github.com/avasconcelos114), [ccbrown](https://github.com/ccbrown), [CometKim](https://github.com/CometKim), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [deveshjadon98](https://github.com/deveshjadon98), [enahum](https://github.com/enahum), [fraziern](https://github.com/fraziern), [grundleborg](https://github.com/grundleborg), [h2oloopan](https://github.com/h2oloopan), [hmhealey](https://github.com/hmhealey), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [KishoreFartiyal](https://github.com/KishoreFartiyal), [lfbrock](https://github.com/lfbrock), [mikelinden1](https://github.com/mikelinden1), [mkraft](https://github.com/mkraft), [MusikPolice](https://github.com/MusikPolice), [QuantumKing](https://github.com/QuantumKing), [rickbatka](https://github.com/rickbatka), [R-Wang97](https://github.com/R-Wang97), [santos22](https://github.com/santos22), [saturninoabril](https://github.com/saturninoabril), [sudheerDev](https://github.com/sudheerDev), [tkbky](https://github.com/tkbky), [yth0625](https://github.com/yth0625)

/mattermost-plugin-zoom

- [crspeller](https://github.com/crspeller), [jwilander](https://github.com/jwilander)

/mattermost-server

- [amyblais](https://github.com/amyblais), [ccbrown](https://github.com/ccbrown), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [cpfeiffer](https://github.com/cpfeiffer), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [enahum](https://github.com/enahum), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jwilander](https://github.com/jwilander), [letsila](https://github.com/letsila), [lindalumitchell](https://github.com/lindalumitchell), [mkraft](https://github.com/mkraft), [mogul](https://github.com/mogul),
[MusikPolice](https://github.com/MusikPolice), [yeoji](https://github.com/yeoji)

/mattermost-mobile

- [cpfeiffer](https://github.com/cpfeiffer), [csduarte](https://github.com/csduarte), [enahum](https://github.com/enahum), [hmhealey](https://github.com/hmhealey), [jarredwitt](https://github.com/jarredwitt), [lfbrock](https://github.com/lfbrock), [mkraft](https://github.com/mkraft)

/docs

- [amyblais](https://github.com/amyblais), [bbodenmiller](https://github.com/bbodenmiller), [ccbrown](https://github.com/ccbrown), [comharris](https://github.com/comharris), [esethna](https://github.com/esethna), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais),
[jespino](https://github.com/jespino), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [lfbrock](https://github.com/lfbrock), [lindalumitchell](https://github.com/lindalumitchell), [lindy65](https://github.com/lindy65), [mkdbns](https://github.com/mkdbns), [mkraft](https://github.com/mkraft), [saturninoabril](https://github.com/saturninoabril)

/mattermost-docker

- [andruwa13](https://github.com/andruwa13), [muffl0n](https://github.com/muffl0n), [pichouk](https://github.com/pichouk), [xcompass](https://github.com/xcompass)

/mattermost-load-test

- [ccbrown](https://github.com/ccbrown), [crspeller](https://github.com/crspeller), [jasonblais](https://github.com/jasonblais)

/mattermost-redux

- [brettmc](https://github.com/brettmc), [ccbrown](https://github.com/ccbrown), [csduarte](https://github.com/csduarte), [enahum](https://github.com/enahum), [hmhealey](https://github.com/hmhealey), [jespino](https://github.com/jespino), [jwilander](https://github.com/jwilander), [mkraft](https://github.com/mkraft), [sudheerDev](https://github.com/sudheerDev)

/mattermost-developer-documentation

- [ccbrown](https://github.com/ccbrown), [coreyhulen](https://github.com/coreyhulen), [crspeller](https://github.com/crspeller), [jwilander](https://github.com/jwilander), [MusikPolice](https://github.com/MusikPolice)

/mattermost-plugin-jira

- [ccbrown](https://github.com/ccbrown)

/mattermost-webrtc

- [enahum](https://github.com/enahum)

/desktop

- [dmeza](https://github.com/dmeza), [jasonblais](https://github.com/jasonblais), [yuya-oc](https://github.com/yuya-oc)

/mattermost-kubernetes

- [cpanato](https://github.com/cpanato)

/mattermost-selenium

- [lindalumitchell](https://github.com/lindalumitchell)

/mattermost-api-reference

- [grundleborg](https://github.com/grundleborg), [jasonblais](https://github.com/jasonblais), [jwilander](https://github.com/jwilander), [saturninoabril](https://github.com/saturninoabril)

/mattermost-ios-classic

- [coreyhulen](https://github.com/coreyhulen)

/mattermost-developer-kit

- [jwilander](https://github.com/jwilander)

/mattermost-build

- [crspeller](https://github.com/crspeller), [mthornba](https://github.com/mthornba)

/marked

- [hmhealey](https://github.com/hmhealey)

## Release v4.4.5 - Feature Release

 - **v4.4.5, release date 2017-12-11**
   - Mattermost v4.4.5 contains a medium severity security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.4.4, release date 2017-12-06**
   - Added a config.json setting, `ClientDirectory`, to set the directory to write web app plugins to. Added to better support plugins in GitLab Omnibus.
 - **v4.4.3, released 2017-12-05**
   - Fixed a medium level security issue affecting servers with [EnableOAuthServiceProvider](https://docs.mattermost.com/administration/config-settings.html#enable-oauth-2-0-service-provider) set to `true` and  [EnableOnlyAdminIntegrations](https://docs.mattermost.com/administration/config-settings.html#restrict-managing-integrations-to-admins) set to `false`. If you're affected, [upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.4.2, released 2017-11-23**
   - Fixed an issue where AD/LDAP accounts get deactivated following an AD/LDAP sync if their email address between the AD/LDAP server and Mattermost don't match case.
   - Fixed synchronization of SAML accounts with AD/LDAP.
   - Fixed AD/LDAP "Test Connection" button in the System Console not working when AD/LDAP login is disabled.
   - Fixed system messages not being translated into user's language set in **Account Settings > Display > Language**.
   - Fixed system messages about channel header updates sometimes being incorrectly formatted.
 - **v4.4.1, released 2017-11-16**
   - Fixed an upgrade issue where an alternative config file location via ``--config`` flag is ignored.
 - **v4.4.0, released 2017-11-16**
   - Original 4.4.0 release

### Highlights

#### Plugins (Beta)
- Beta release of Mattermost plugins, which allow admins to more easily integrate with third-party systems, extend functionality and customize the user interface of your Mattermost server. See [documentation](https://about.mattermost.com/default-plugins) to learn more.

#### Do Not Disturb Status
- Added "Do Not Disturb" status to temporarily turn off all desktop and mobile push notifications.

#### Support SAML sync via AD/LDAP ([Enterprise Edition E20](https://about.mattermost.com/pricing))
- Added support for periodically synchronizing SAML user attributes, including user deactivation and removal, from AD/LDAP. See [documentation](https://about.mattermost.com/default-saml-ldap-sync) to learn more.

### Improvements

#### Web User Interface
- Added an experimental feature to hide direct and group message channels after 7 days with no new messages. To enable it set `CloseUnusedDirectMessages` in `config.json` to `true`.
- Moved website previews out of beta, configurable in **Account Settings > Display**. Enable link previews in the [System Console](https://docs.mattermost.com/administration/config-settings.html#enable-link-previews).
- Made it easier to add a user to channel if mentioned user is not already a channel member.
- Added "Edit Account Settings" link to the bottom of your own profile popover to more easily edit your settings.
- URL address for internal links such as when hovering over the flag icon, is now hidden for better user experience.
- URL addresses for channels on the left-hand sidebar are now hidden on the desktop app.
- Added a loading spinner to Account Settings dialog after clicking the "Save" button.
- Added full date tooltip to post timestamps in right-hand sidebar and search results.
- Added "@" in front of the username field in user lists.

#### Performance
- Reduced load times by optimizing database queries and adding composite indexes for the `Posts` table.
- Prevented sessions from being stuck in cache by clearing the session cache if permission is denied.
- Improved Elasticsearch bulk indexing query performance.

#### Emoji Picker
- Added emoji picker to the Edit Message dialog.
- Removed categorization when searching for emojis in the emoji picker.

#### Integrations
- Added the ability to edit OAuth 2.0 applications.
- Added improvements for interactive message buttons, such as displaying your username in ephemeral messages triggered by the message buttons.

#### Slash Commands
- Added `/remove` and `/kick` slash commands to remove a user from the channel.

#### WebRTC Video and Audio Calls (Beta)
- When you have multiple browser tabs open and receive a video call, the ringtone stops in all tabs when you accept the call.
- Multiple STUN and TURN servers are now supported.

#### System Console
- Added a setting to disable channel wide (@-channel, @-all) mention confirmation in channels with more than five members.
- Admin now receives a prompt when leaving a System Console page with unsaved changes.

#### Elasticsearch ([Enterprise Edition E20](https://about.mattermost.com/pricing))
- Added support for batched live indexing for Elasticsearch.
- Added a configurable timeout for Elasticsearch requests.
- Added a table to Elasticsearch System Console page to monitor indexing jobs.
- Elasticsearch connection is now asynchronous so that a broken Elasticsearch server cannot block the startup of the Mattermost server.

### Bug Fixes
- Fixed mobile push notification settings not saving in the System Console.
- Fixes to channel link (~) autocomplete, such as not being able to autocomplete 'Town Square'.
- Fixed an issue where System Console was sometimes temporarily accessible after demoting a user to a member.
- Fixed failure to switch from email to SAML sign-in method if the user's email address has a plus sign.
- Fixed "More Channels" modal not showing the correct the page number when displaying search results.
- Fixed an incorrect error message when trying to add a user to a direct or group message channel via the APIs.
- Fixed an issue where downloading a file containing spaces didn't preserve the name.
- Fixed thumbnail image for .m4r file types.
- Fixed an issue where search in Manage Members dialog didn't update results when there were no matches.
- Fixed an issue where `in:` autocomplete for text search didn't display results after a hyphen in some servers.
- Fixed a missing "No results" screen for Elasticsearch text search.
- Fixed channel member count not updating until refresh when a user is added or removed.
- Fixed timestamp links on desktop app opening permalink view in a new app window.
- Fixed an error caused by creating a new direct message channel via the channel switcher (CTRL/CMD+K).
- Fixed SVG thumbnails not showing a preview.
- Fixed team sidebar showing unreads for deleted channels.
- Fixed a missing indicator when a message is pending but not yet sent.
- Fixed emoji autocomplete appearing when typing an emoticon like :-D.
- Fixed emoji names matching usernames triggering mentions.
- Fixed incorrect order of recent mentions when a hashtag is a word that triggers mentions.
- Fixed webhook message attachments longer than 8000 characters failing to post by truncating them, or splitting to multiple posts if the message has multiple attachments.
- Fixed `/msg` command arbitrarily switching teams.
- Fixed mentions not appearing linked in message drafts when in preview mode.
- Fixed an issue where an existing account could change their email address to one not in the [restricted domain list](https://docs.mattermost.com/administration/config-settings.html#restrict-account-creation-to-specified-email-domains).
- Fixed emoji reactions being added to system messages when using the `+:emoji:` command.
- Fixed an issue where message retention policy didn't work in Postgres databases if there were emoji reactions to delete.

### Compatibility

Composite database indexes were added to the `Posts` table. This may lead to longer upgrade times for servers with more than 1 million messages.

Moreover, LDAP sync now depends on email. If you have AD/LDAP login enabled, make sure all users on your AD/LDAP server have an email address or that their account is deactivated in Mattermost.

#### Removed and Deprecated Features
- All APIv3 endpoints are scheduled for removal on January 16, 2018.

For a list of past and upcoming deprecated features, [see our website](https://about.mattermost.com/deprecated-features/).

#### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

**Changes to Team Edition and Enterprise Edition**:

- Under `ServiceSettings` in `config.json`:
  - Added `"CloseUnusedDirectMessages": false` to set whether users have the option to automatically close direct and group message channels older than 7 days.
- Under `TeamSettings` in `config.json`:
  - Added `"EnableConfirmNotificationsToChannel": true` to set whether a confirmation is shown for channel wide (@-channel, @-all) mentions in channels with more than five members.
- Under `PluginSettings` in `config.json`:
  - Added `"Enable": true` to set whether plugins are enabled on the server.
  - Added `"EnableUploads": false` to set whether manual plugin uploads are enabled on the server. Disabling will keep existing plugins, including pre-packaged Mattermost plugins, installed on the server.
  - Added `"Directory": "./plugins"` to specify the directory of where plugins are stored.
  - Added `"Plugins": {}` to list installed plugins on the Mattermost server.
  - Added `"PluginStates": {}` to set whether an installed plugin is active or inactive on the Mattermost server.

**Additional Changes to Enterprise Edition**:

- Under `SamlSettings` in `config.json`:
  - Added `EnableSync: false` to set whether AD/LDAP synchronization is enabled.
- Under `LdapSettings` in `config.json`:
  - Added `EnableSyncWithLdap: false` to set whether SAML user attributes, including deactivation, are periodically synchronized from AD/LDAP.
- Under `ElasticsearchSettings` in `config.json`:
  - Added `"LiveIndexingBatchSize": 1` to set how many new posts are batched together before they are added to the Elasticsearch index.
  - Added `"RequestTimeoutSeconds": 30` to set the timeout in seconds for Elasticseaerch calls.
  - Added `"BulkIndexingTimeWindowSeconds": 3600` to set the maximum time window for a batch of posts being indexed by the Bulk Indexer.

### Database Changes

**Posts Table:**
- Added a composite index for `ChannelId, DeleteAt, CreateAt`
- Added a composite index for `ChannelId, UpdateAt`

**UserAccessTokens Table:**
- Added `IsActive` column

### API v4 Changes

- It is recommended that any new integrations use API v4 endpoints. For more details, and for a complete list of available endpoints, see [https://api.mattermost.com/](https://api.mattermost.com/).
- All API v3 endpoints are scheduled for removal on January 16, 2018.

**Added routes (API v4)**
- `POST` at `/users/token/enable`
  - Re-enables a personal access token that was previously disabled.
- `POST` at `/users/token/disable`
  - Disables a personal access token and deletes any sessions that uses the token. The token can be re-enabled using `/users/tokens/enable.`
- `POST` at `/users/{user_id}/sessions/revoke/all`
  - Revokes all user sessions from the provided user id and session id strings.
- `POST` at `/plugins`
  - Uploads a plugin in a compressed .tar.gz.
- `GET` at `/plugins`
  - Gets a list of active and inactive plugins.
- `DELETE` at `/plugins/{plugin_id}`
  - Removes a previously uploaded plugin.
- `POST` at `/plugins/{plugin_id}/activate`
  - Activates an installed plugin.
- `POST` at `/plugins/{plugin_id}/deactivate`
  - Deactivates an active plugin.
- `GET` at `/plugins/webapp`
  - Gets a list of plugin manifests for active plugins with webapp components.

**Modified routes (API v4)**
- `POST` at `/logs`
  - Unauthenticated users can now log ERROR or DEBUG messages when `ServiceSettings.EnableDeveloper` is set to `true`.

### Websocket Event Changes

**Added:**
- `user_role_updated` that occurs when a user role is updated.

### Known Issues

- Google login fails on the Classic mobile apps.
- User can receive a video call from another browser tab while already on a call.
- Jump link in search results does not always jump to display the expected post.
- Scrollbar is sometimes not visible in the left-hand sidebar after switching teams.
- Certain code block labels don't appear while scrolling on iOS mobile web.
- Deleted message doesn't clear unreads or unread mentions.
- Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
- Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
- Searching with Elasticsearch enabled may not always highlight the searched terms.
- Channel links to channels that the current user does not belong to may not render correctly.
- Team sidebar doesn't always show unreads from other teams on first load.
- Uppercase letter is required for a password if the password requirement is set to at least 5 characters and a number.
- System Admin cannot reset their own password via the System Console.
- Channel scroll position flickers while images and link previews load.
- Closing a direct or group message channel, then re-opening later, doesn't restore channel preferences.
- CTRL/CMD+U shortcut to upload a file doesn't work on Firefox.
- Website previews are not displayed for comments on threads.
- User gets a blank page after hitting "x" on a deleted message in permalink view.
- Profile pictures don't immediately update across tabs or in the right-hand side comment threads.

### Contributors

/mattermost-webapp

- [asaadmahmood](https://github.com/asaadmahmood), [ccbrown](https://github.com/ccbrown), [cherealnice](https://github.com/cherealnice), [CometKim](https://github.com/CometKim), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [enahum](https://github.com/mattermost/enahum), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [Hyeongmin-Kwon](https://github.com/Hyeongmin-Kwon), [jasonblais](https://github.com/jasonblais), [johncoleman83](https://github.com/johncoleman83), [jwilander](https://github.com/jwilander), [letsila](https://github.com/letsila), [longsleep](https://github.com/mattermost/longsleep), [maruTA-bis5](https://github.com/maruTA-bis5), [MusikPolice](https://github.com/MusikPolice), [R-Wang97](https://github.com/R-Wang97), [ryantm](https://github.com/ryantm), [santos22](https://github.com/mattermost/santos22), [saturninoabril](https://github.com/saturninoabril), [sudheerDev](https://github.com/sudheerDev), [tkbky](https://github.com/tkbky), [yeoji](https://github.com/yeoji), [Zapix](https://github.com/Zapix)

/docs

- [amyblais](https://github.com/amyblais), [asaadmahmood](https://github.com/asaadmahmood), [bbodenmiller](https://github.com/bbodenmiller), [ccbrown](https://github.com/ccbrown), [comharris](https://github.com/comharris), [coreyhulen](https://github.com/coreyhulen), [esethna](https://github.com/esethna), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jwilander](https://github.com/jwilander), [lfbrock](https://github.com/lfbrock), [lindalumitchell](https://github.com/lindalumitchell), [lindy65](https://github.com/lindy65), [saturninoabril](https://github.com/saturninoabril), [shieldsjared](https://github.com/shieldsjared), [tolidano](https://github.com/tolidano)

/mattermost-server

- [ccbrown](https://github.com/ccbrown), [chclaus](https://github.com/chclaus), [coreyhulen](https://github.com/coreyhulen), [cpanato](https://github.com/cpanato), [crspeller](https://github.com/crspeller), [enahum](https://github.com/enahum), [fraziern](https://github.com/fraziern), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [ivernus](https://github.com/ivernus), [jasonblais](https://github.com/jasonblais), [jwilander](https://github.com/jwilander), [longsleep](https://github.com/longsleep), [MusikPolice](https://github.com/MusikPolice), [rickbatka](https://github.com/rickbatka), [santos22](https://github.com/santos22), [saturninoabril](https://github.com/saturninoabril), [thePanz](https://github.com/thePanz)

/mattermost-redux

- [ccbrown](https://github.com/ccbrown), [CometKim](https://github.com/CometKim), [enahum](https://github.com/enahum), [fraziern](https://github.com/fraziern), [hmhealey](https://github.com/hmhealey), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jwilander](https://github.com/jwilander), [MusikPolice](https://github.com/MusikPolice), [rickbatka](https://github.com/rickbatka), [saturninoabril](https://github.com/saturninoabril), [sudheerDev](https://github.com/sudheerDev), [tkbky](https://github.com/tkbky),

/mattermost-mobile

- [csduarte](https://github.com/csduarte), [enahum](https://github.com/enahum), [gelim](https://github.com/gelim), [hmhealey](https://github.com/hmhealey), [jarredwitt](https://github.com/jarredwitt)

/desktop

- [dmeza](https://github.com/dmeza), [jarredwitt](https://github.com/jarredwitt), [yuya-oc](https://github.com/yuya-oc)

/mattermost-docker

- [pichouk](https://github.com/pichouk), [sebgl](https://github.com/sebgl)

/mattermost-api-reference

- [fraziern](https://github.com/fraziern), [jasonblais](https://github.com/jasonblais), [jwilander](https://github.com/jwilander), [rickbatka](https://github.com/rickbatka)

/mattermost-load-test

- [crspeller](https://github.com/crspeller), [jasonblais](https://github.com/jasonblais)

## Release v4.3.4 - Feature Release

 - **v4.3.4, release date 2017-12-11**
   - Mattermost v4.3.4 contains a medium severity security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.3.3, released 2017-12-05**
   - Fixed a medium level security issue affecting servers with [EnableOAuthServiceProvider](https://docs.mattermost.com/administration/config-settings.html#enable-oauth-2-0-service-provider) set to `true` and  [EnableOnlyAdminIntegrations](https://docs.mattermost.com/administration/config-settings.html#restrict-managing-integrations-to-admins) set to `false`. If you're affected, [upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.3.2, released 2017-11-10**
   - Fixed an issue where after creating a new direct message channel via channel switcher (CTRL/CMD+K), all messages fail to post until a page refresh.
 - **v4.3.1, released 2017-10-20**
   - Fixed an upgrade issue where the database schema would appear to be out of date and throw a log warning.
   - Fixed the Idle Timeout setting in `config.json` by changing the setting title from `SessionIdleTimeout` to `SessionIdleTimeoutInMinutes`.
   - Fixed a regression where slash commands were not functional in Direct or Group Messages.
   - Mattermost v4.3.1 contains a low severity security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.3.0, released 2017-10-16**
   - Original 4.3.0 release

### Security Update

- Mattermost v4.3.0 contains multiple security fixes ranging from low to high severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Highlights

#### Data Retention Beta ([Enterprise Edition E20](https://about.mattermost.com/pricing/))
- Automatically delete old messages and file uploads through custom data retention policies.

#### Languages
- Promoted Italian and Turkish out of beta to release-quality translations.

### Improvements

#### Web User Interface
- Clicking on "More Unreads" bubble on channel sidebar now scrolls you to the next unread channel.
- Added status indicators to direct message channel header.

#### Search
- Improved user search that supports two character full names and usernames.

#### Integrations
- Ephemeral slash command responses now support attachements without text.
- Added CLI command to move custom slash commands between teams.

#### Notifications
- Updating the channel header with channel-wide mentions no longer triggers notifications.

#### Performance
- Improved initial load of the emoji picker, now supporting thousands of custom emojis including GIFs.

#### Enterprise Edition
- Added tables in System Console for AD/LDAP sync, Elasticsearch and Data Retention to track the success of scheduled jobs.
- Added an idle timeout setting to automatically log out users who are inactive for a specified amount of time.
- Elasticsearch can now be used on a shared Elasticsearch cluster.
- Added metrics for monitoring Elasticsearch system health and usage.

### Bug Fixes
- Fixed an issue where closing brackets were ignored in URL links.
- Fixed Leave Team icon size and inconsistent channel header icon hover effects on IE11 mobile view.
- Fixed an issue where right side menu disappeared after viewing search results on IE11 mobile view.
- Fixed other minor UI issues on IE11 desktop view.
- Fixed an issue where system and ephemeral messages could be flagged.
- Error text in Edit modal no longer overlaps with help text.
- Integration message attachments without `pretext` no longer overlap with username in Compact view.
- Fixed channel member list being sorted by username instead of teammate name display.
- "Password updated successfully" bar is now displayed after resetting password.
- Fixed a broken UI for an expired email verification link.
- Fixed integration message attachments not always rendering in comment threads.
- Fixed an issue where "Add Members" dialog would sometimes break.
- Slash command responses now handle charset and boundary sets correctly.
- Deactivated users are no longer counted in the Town Square member count.
- iOS push notifications are now consistently cleared from the homescreen if all mentions are read on another device.
- Webhooks no longer continue sending to the original channel if the target channel is changed.
- Emails containing symbols now render correctly when switching to email authentication from other methods.
- Attempting to open an invalid public file link no longer displays an unformatted error page.
- Interactive message action buttons no longer disappear after updating the message.
- Ticket links posted by the built-in JIRA plug-in are now correct if the JIRA URL has a custom context path.
- Error message is now displayed in the System Console if the localization available languages does not include the default client language.
- Fixed a race condition where bulk import sometimes fails to get team member when importing users.
- Closing the channel switcher on mobile no longer sets focus to the text box.
- Fixed an issue where the wrong channel name might appear in the right-hand side pinned post list.
- Fixed team sidebar now always showing unreads from other teams on first load.

### Compatibility

#### Removed and Deprecated Features
- All APIv3 endpoints are scheduled for removal on January 16, 2018.

For a list of past and upcoming deprecated features, [see our website](https://about.mattermost.com/deprecated-features/).

#### config.json

Multiple setting options were added to `config.json`. Below is a list of the additions and their default values on install. The settings can be modified in `config.json`, or the System Console when available.

**Changes to Enterprise Edition**:

- Under `ServiceSettings` in `config.json`:
  - Added `"SessionIdleTimeoutInMinutes": 0` to specify how long to wait before logging out inactive users.
- Under `ElasticsearchSettings` in `config.json`:
  - Added `"IndexPrefix": ""` to allow Elasticsearch to be used on a shared Elasticseearch cluster.
- Under `DataRetentionSettings` in `config.json`:
  - Added `"EnableMessageDeletion": false` to enable message deletion.
  - Added `"EnableFileDeletion": false` to enable file deletion.
  - Added `"MessageRetentionDays": 365` to set how long Mattermost keeps messages in channels and direct messages.
  - Added `"FileRetentionDays": 365` to set how long Mattermost keeps file uploads in channels and direct messages.
  - Added `"DeletionJobStartTime": "02:00"` to specify when to start the data retention job.

### API v4 Changes

- It is recommended that any new integrations use APIv4 endpoints. For more details, and for a complete list of available endpoints, see [https://api.mattermost.com/](https://api.mattermost.com/).
- All APIv3 endpoints are scheduled for removal on January 16, 2018.

**Added routes (API v4)**
- `PUT` at `/oauth/apps/{app_id}`
  - Update an OAuth 2.0 client application.
- `GET` at `/data_retention/policy`
  - Gets the current data retention policy details from the server, including what data should be purged and the cutoff times for each data type that should be purged.

**Modified routes (API v4)**
- `POST` at `/channels/members/{user_id}/view`
  - Response includes `last_viewed_at_times` for Mattermost server 4.3 and newer.

### Known Issues

- Google login fails on the Classic mobile apps.
- User can receive a video call from another browser tab while already on a call.
- Jump link in search results does not always jump to display the expected post.
- Scrollbar is sometimes not visible in the left-hand sidebar after switching teams.
- Certain code block labels don't appear while scrolling on iOS mobile web.
- Deleted message doesn't clear unreads or unread mentions.
- Status may sometimes get stuck as away or offline in High Availability mode with IP Hash turned off.
- Searching stop words in quotes with Elasticsearch enabled returns more than just the searched terms.
- Searching with Elasticsearch enabled may not always highlight the searched terms.
- Channel links to channels that the current user does not belong to may not render correctly.
- Missing an indication if a message is pending but not yet sent.
- Recent mention results are not sorted correctly if hashtags is included in "words that trigger mentions".
- SVG thumbnails don't preview in the posted thumbnail.
- Emojis names matching usernames can trigger mentions.
- Integration message attachment fails to post if attachment length exceeds 7900 characters.
- Uppercase letter is required for a password if the password requirement is set to at least 5 characters and a number.
- Message retention policy may not work in Postgres databases if there are emoji reactions to delete.

### Contributors

/mattermost-server

- [ccbrown](https://github.com/ccbrown), [coreyhulen](https://github.com/coreyhulen), [crspeller](https://github.com/crspeller), [enahum](https://github.com/enahum), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jwilander](https://github.com/jwilander), [moonmeister](https://github.com/moonmeister), [MusikPolice](https://github.com/MusikPolice), [n1aba](https://github.com/n1aba), [saturninoabril](https://github.com/saturninoabril)

/mattermost-webapp

- [asaadmahmood](https://github.com/asaadmahmood), [bbodenmiller](https://github.com/bbodenmiller), [ccbrown](https://github.com/ccbrown), [coreyhulen](https://github.com/coreyhulen), [crspeller](https://github.com/crspeller), [enahum](https://github.com/enahum), [grundleborg](https://github.com/grundleborg), [hmhealey](https://github.com/hmhealey), [jasonblais](https://github.com/jasonblais), [jazzzz](https://github.com/jazzzz), [jwilander](https://github.com/jwilander), [R-Wang97](https://github.com/R-Wang97), [saturninoabril](https://github.com/saturninoabril), [sudheerDev](https://github.com/sudheerDev)

/desktop

- [csduarte](https://github.com/csduarte), [dmeza](https://github.com/dmeza), [yuya-oc](https://github.com/yuya-oc)

/mattermost-mobile

- [csduarte](https://github.com/csduarte), [enahum](https://github.com/enahum), [hmhealey](https://github.com/hmhealey), [jarredwitt](https://github.com/jarredwitt), [lfbrock](https://github.com/lfbrock)

/mattermost-api-reference

- [atpons](https://github.com/atpons), [grundleborg](https://github.com/grundleborg), [jwilander](https://github.com/jwilander), [n1aba](https://github.com/n1aba), [pichouk](https://github.com/pichouk)

/docs

- [ccbrown](https://github.com/ccbrown), [crspeller](https://github.com/crspeller), [esethna](https://github.com/esethna), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jwilander](https://github.com/jwilander), [lfbrock](https://github.com/lfbrock), [lindy65](https://github.com/lindy65)

/mattermost-developer-kit

- [jwilander](https://github.com/jwilander)

/marked

- [hmhealey](https://github.com/hmhealey)

/mattermost-docker

- [localsnet](https://github.com/localsnet), [pdemagny](https://github.com/pdemagny), [pichouk](https://github.com/pichouk), [tivvit](https://github.com/tivvit)

/mattermost-redux

- [enahum](https://github.com/enahum), [hmhealey](https://github.com/hmhealey), [jespino](https://github.com/jespino), [jwilander](https://github.com/jwilander), [n1aba](https://github.com/n1aba), [saturninoabril](https://github.com/saturninoabril)

/mattermost-selenium

- [lindalumitchell](https://github.com/lindalumitchell)

/mattermost-mattermod

- [crspeller](https://github.com/crspeller), [hmhealey](https://github.com/hmhealey)

/mattermost-build

- [crspeller](https://github.com/crspeller)

## Release v4.2.2 - Feature Release

 - **v4.2.2, release date 2017-12-11**
   - Mattermost v4.2.2 contains a medium severity security fix. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.2.1, released 2017-10-20**
   - Mattermost v4.2.1 contains multiple security fixes ranging from low to high severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
 - **v4.2.0, released 2017-09-16**
   - Original 4.2.0 release

### Security Update

- Mattermost v4.2.0 contains multiple security fixes ranging from low to moderate severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Highlights

#### Interactive Message Buttons
- Added message buttons to support user interactions with posts made by incoming webhooks and custom slash commands.

#### Mobile Support for AppConfig
- iOS and Android mobile apps now support Enterprise Mobility Management (EMM) solutions through integration with [App Config](https://www.appconfig.org/). See [documentation](https://docs.mattermost.com/mobile/mobile-appconfig.html) to learn more.

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

3 - Uploaded file attachments are now grouped by day and stored in `/data/<date-of-upload-as-YYYYMMDD>/teams/...` of your file storage system.

4 - Mattermost `/platform` repo has been separated to `/mattermost-webapp` and `/mattermost-server`. This may affect you if you have a private fork of the `/platform` repo. [More details here](https://forum.mattermost.org/t/mattermost-separating-platform-into-two-repositories-on-september-6th/3708).

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

## Release v4.1.2 - Feature Release

 - **v4.1.2, released 2017-10-20**
   - Mattermost v4.1.2 contains multiple security fixes ranging from low to high severity. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 14 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).
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

## Release v4.0.5 - Feature Release

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
- The apps are [EMM compatible starting with BlackBerry Dynamics](https://about.mattermost.com/releases/mattermost-2nd-gen-mobile-apps-released-emm-compatible-starting-with-blackberry-dynamics/).

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
- Second generation mobile apps, built using React Native, are [available for beta testing](https://about.mattermost.com/releases/a-native-mobile-experience-second-generation-mobile-apps-released-in-beta/) on [iOS](https://mattermost-fastlane.herokuapp.com/) and [Android](https://play.google.com/apps/testing/com.mattermost.react.native).

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
    - Removed `"RestrictTeamNames": true` that controlled whether newly created team names were restricted.
    - Added `"ConnectionSecurity": ""` to select the type of encryption between Mattermost and your server.
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

Mattermost v1.2.1 is a Quality Release addressing a security issue in v1.2.0 affecting a newly introduced outgoing webhooks feature. Specifically, in v1.2.0 there was a check missing from outgoing webhooks, so a team member creating outgoing webhooks could in theory find a way to listen to messages in private channels containing popular words like "a", "the", "at", etc. For added security, Mattermost v1.2.1 now installs with incoming and outgoing webhooks disabled by default.

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

## Release v1.1.1 (Quality Release)

Released 2015-10-20

### About Quality Releases

This is a Quality Release (v1.1.1) and recommended only for users needing a fix to the specific issue listed below. All other users should use the most recent major stable build release (v1.1.0).

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
