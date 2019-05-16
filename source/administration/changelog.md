# Mattermost Changelog

This changelog summarizes updates to [Mattermost Team Edition](http://www.mattermost.org/), an open source team messaging solution released monthly under an MIT license, and [Mattermost Enterprise Edition](https://about.mattermost.com/pricing/), a commercial upgrade offering enterprise messaging for large organizations.

Also see [changelog in progress](http://bit.ly/2nK3cVf) for the next release.

## Release v5.11

Release Date 2019-05-16

Mattermost v5.11.0 contains low level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

### Breaking Changes since last release

 - If your integration uses ``Update.Props == nil`` to clear ``Props``, this will no longer work in 5.11+. Instead, use ``Update.Props == {}`` to clear properties. This change was made because ``Update.Props == nil`` unintentionally cleared all ``Props``, such as the profile picture, instead of preserving them.

**IMPORTANT:** If you upgrade from another release than 5.10, please read the [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html).

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

[aeomin](https://translate.mattermost.com/user/aeomin/), [akrfjmt](https://github.com/akrfjmt), [ali-farooq0](https://github.com/ali-farooq0), [amyblais](https://github.com/amyblais), [andresoro](https://github.com/andresoro), [asaadmahmood](https://github.com/asaadmahmood), [BotKube](https://www.botkube.io/), [bradjcoughlin](https://github.com/bradjcoughlin), [bytemine GmbH](https://github.com/bytemine), [chikei](https://github.com/chikei), [cometkim](https://github.com/cometkim), [comharris](https://github.com/com/comharris), [CooperAtive](https://github.com/CooperAtive), [coreyhulen](https://github.com/coreyhulen), [courtneypattison](https://github.com/courtneypattison), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [csduarte](https://github.com/csduarte), [d28park](https://github.com/d28park), [danmaas](https://github.com/danmaas), [deanwhillier](https://github.com/deanwhillier), [der-test](https://github.com/der-test), [DHaussermann](https://github.com/DHaussermann), [DSchalla](https://github.com/DSchalla), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [fcorrea](https://github.com/fcorrea), [gabrieljackson](https://github.com/gabrieljackson), [gnufede](https://github.com/gnufede), [gruceqq](https://translate.mattermost.com/user/gruceqq/), [grundleborg](https://github.com/grundleborg), [hanzei](https://github.com/hanzei), [happygaijin](https://github.com/happygaijin), [harshilsharma](https://github.com/harshilsharma), [hectorskypl](https://github.com/hectorskypl), [Herzum](https://github.com/herzum), [hmhealey](https://github.com/hmhealey), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [johnbellone](https://github.com/johnbellone), [johnthompson365](https://github.com/johnthompson365), [JVasky](https://github.com/JVasky), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [Kaya_Zeren](https://twitter.com/kaya_zeren), [kingisaac95](https://github.com/kingisaac95), [kmandagie](https://github.com/kmandagie), [kosgrz](https://github.com/kosgrz), [Lena](https://translate.mattermost.com/user/Lena/), [levb](https://github.com/levb), [lfbrock](https://github.com/lfbrock), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [liusy182](https://github.com/liusy182), [ljmccaff](https://github.com/ljmccaff), [Mario-Hofstaetter](https://github.com/Mario-Hofstaetter), [meilon](https://github.com/meilon), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [migbot](https://github.com/migbot), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [MParvin](https://github.com/MParvin), [mstoli](https://github.com/mstoli), [ninanung](https://github.com/ninanung), [oliverJurgen](https://github.com/oliverJurgen), [PeterDaveHello](https://github.com/PeterDaveHello), [prapti](https://github.com/prapti), [reflog](https://github.com/reflog), [rodcorsi](https://github.com/rodcorsi), [RyPoints](https://github.com/RyPoints), [s4kh](https://github.com/s4kh), [sapnasivakumar](https://github.com/sapnasivakumar), [saturninoabril](https://github.com/saturninoabril), [scottleedavis](https://github.com/scottleedavis), [Sheshagiri](https://github.com/Sheshagiri), [stylianosrigas](https://github.com/stylianosrigas), [sudheerDev](https://github.com/sudheerDev), [svelle](https://github.com/svelle), [tengis617](https://github.com/tengis617), [thekiiingbob](https://github.com/thekiiingbob), [thePanz](https://github.com/thepanz), [thepill](https://github.com/thepill), [therealpuneeth20](https://github.com/therealpuneeth20), [ThiefMaster](https://github.com/ThiefMaster), [torgeirl](https://github.com/torgeirl), [tylarb](https://github.com/tylarb), [ulhosting](https://github.com/uhlhosting), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [z4cco](https://github.com/z4cco) 

## Release v5.10

Mattermost v5.10.0 contains medium to high level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

- **v5.10.1, release date TBD** 
  - Fixing an issue on Internet Explorer (IE11) where the system console opens a blank page.
- **v5.10.0, released 2019-04-16**
  - Original 5.10.0 release

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

### API Changes
 - Added ``GetUsers`` API method to add the ability to list users.
 - Added the ``SearchPostsInTeam`` method to the plugin API to add the ability to search posts in a team.
 - Added ``GetTeamMembersForUser`` and ``GetChannelMembersForUser`` to the plugin API to add the ability to get team and channel members for a specific user.
 - Added ``GetBundleInfo() string`` method to the plugin API to add the ability to store assets elsewhere.

### Database Changes
 - Granted the following permissions for the System Admin, in preparation for an upcoming bot accounts feature:
   - PERMISSION_CREATE_BOT
   - PERMISSION_READ_BOTS
   - PERMISSION_READ_OTHERS_BOTS
   - PERMISSION_MANAGE_BOTS
   - PERMISSION_MANAGE_OTHERS_BOTS

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

## Release v5.9

Mattermost v5.9.0 contains low to medium level security fixes. [Upgrading](http://docs.mattermost.com/administration/upgrade.html) is highly recommended. Details will be posted on our [security updates page](https://about.mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://www.mattermost.org/responsible-disclosure-policy/).

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

## Release v5.8

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
 
## Release v5.7

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

## Release v5.6

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

## Release v5.5

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

## Release v5.4

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

## Release v5.3

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

## Release v5.2

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

## Release v5.1

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

## Release v5.0

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

## Release v4.9

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

## Release v4.8

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

## Release v4.7

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

## Release v4.6

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

## Release v4.5

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
- JIRA plugin is now bundled as a prepackaged plugin manageable from the System Console > Plugins > Management.
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

## Release v4.4.5

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

## Release v4.3.4

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

## Release v4.2.2

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

## Release v4.1.2

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
