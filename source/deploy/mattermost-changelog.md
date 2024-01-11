# Mattermost changelog

[Mattermost](https://mattermost.com) is an open source platform for secure collaboration across the entire software development lifecycle. 

```{Important}
From Mattermost v9.2, this changelog summarizes updates for the latest cloud and self-hosted versions of Mattermost to be [deployed and upgraded on infrastructure you control](https://docs.mattermost.com/guides/deployment.html).

- See the [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) documentation for details on upgrading.
- See the [changelog in progress](https://bit.ly/2nK3cVf) for details about the upcoming release.
- **Self-Hosted Releases Prior to v9.2**: See the [Mattermost Legacy Self-Hosted Changelog](/deploy/legacy-self-hosted-changelog) for details.
- **Cloud Releases Prior to v9.2**: See the [Mattermost Legacy Cloud Changelog](/deploy/legacy-cloud-changelog) for details.
```

```{contents} On ths page
:depth: 2
```

## Release v9.4 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

- **9.4.1, released 2024-01-16**
  - Fixed an issue where ``getChannelMemberOnly`` failed to fetch data when certain fields were NULL.
- **9.4.0, released 2024-01-16**
  - Original 9.4.0 release.

### Important Upgrade Notes
 - MySQL v5.7 is at end of life. We recommend all customers to upgrade to at least 8.x. For now, we are logging a warning. From Mattermost v9.5, which is the next Extended Support Release, we will stop supporting MySQL v5.7 altogether.

```{Important}
If you upgrade from a release earlier than v9.3, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Compatibility
 - Updated the minimum required Edge version to v118+.

### Improvements

#### User Interface (UI)
 - Updated the pre-packaged GitHub plugin version to [v2.1.7](https://github.com/mattermost/mattermost-plugin-github/releases/tag/v2.1.7).
 - Pre-packaged Calls plugin version [v0.22.2](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.22.2).
 - Improved the user interface of the channel notifications modal.
 - Emojis are now enlarged in emoji tooltips on mouse hover.
 - Added a gap of 8px between buttons in the modal footer when opened in the mobile web view.
 - Updated empty states to align with new branding and made changes to the empty state copy.
 - Adjusted the position of the suggestion list in "Add <user> to a channel" modal to be below or above the text field.

#### Administration
 - Added support for IP Filtering in Cloud (Cloud Enterprise plan) (this feature is behind a feature flag).
 - Added support for Bring Your Own Key (BYOK) Encryption (Cloud Enterprise plan).
 - An optional dedicated filestore is now used for compliance exports if configured (Cloud Enterprise plan).
 - ``MessageExportSettings.GlobalRelaySettings.CustomerType`` now supports "CUSTOM".
 - Added new ``ServerMetrics`` hook to allow plugins to register a custom HTTP endpoint to serve their metrics under the server's metrics HTTP listener.
 - Admins now have the ability to pipe the output of ``mmctl websocket`` into the JSON parser.
 - Added stores for OAuth **Outgoing Connections**.
 - Added last login timestamp for users, and added a materialized view and a refresh job to keep track of post stats for PostgreSQL.
 - Allowed plugin requests to include **Authorization** headers from external systems.
 - Added a mmctl command ``mmctl system supportpacket`` to download the **Support Packet**.
 - Added a new mmctl command ``oauth list`` for listing registered OAuth2 applications.

### Bug Fixes
 - Fixed an issue with the emoji reaction toggle behavior.
 - Fixed an issue with the spacing between Playbooks and the separator in the Apps bar.

### config.json
 - Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
 - Under ``RefreshPostStatsRunTime`` in ``config.json``:
    - Added ``RefreshPostStatsRunTime`` to add last login timestamp for users and to add materialized view and refresh job to keep track of post stats for PostgreSQL.
  
#### Changes to the Enterprise plan:
 - Under ``GlobalRelayMessageExportSettings`` in ``config.json``:
    - Added two new configuration settings ``CustomSMTPServerName`` and ``CustomSMTPPort`` to allow setting a custom URL and port for Global Relay export. ``CustomSMTPServerName`` and ``CustomSMTPPort`` cannot be configured in the system console UI.

### Open Source Components:
 - Added ``@mattermost/desktop-api`` and ``ipaddr.js`` to https://github.com/mattermost/mattermost/.

### Go Version
 - v9.4 is built with Go ``v1.20.7``.

### Known Issues
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.
 
### Contributors
 - [AayushChaudhary0001](https://github.com/AayushChaudhary0001), [aditipatelpro](https://github.com/aditipatelpro), [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [akbarkz](https://github.com/akbarkz), [Alpha-4](https://github.com/Alpha-4), [amyblais](https://github.com/amyblais), [andrius](https://translate.mattermost.com/user/andrius), [andriuspetrauskis](https://github.com/andriuspetrauskis), [andrleite](https://github.com/andrleite), [arthurhrg](https://github.com/arthurhrg), [arush-vashishtha](https://github.com/arush-vashishtha), [asaadmahmood](https://github.com/asaadmahmood), [avas27JTG](https://github.com/avas27JTG), [ayusht2810](https://github.com/ayusht2810), [azigler](https://github.com/azigler), [BenCookie95](https://github.com/BenCookie95), [caotanduc99](https://github.com/caotanduc99), [CI-YU](https://github.com/CI-YU), [codejagaban](https://github.com/codejagaban), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [cyberjam](https://github.com/cyberjam), [danielsischy](https://github.com/danielsischy), [Dev-A-Line](https://translate.mattermost.com/user/Dev-A-Line), [devinbinnie](https://github.com/devinbinnie), [DHaussermann](https://github.com/DHaussermann), [dkkb](https://github.com/dkkb), [Eleferen](https://translate.mattermost.com/user/Eleferen), [enahum](https://github.com/enahum), [fmartingr](https://github.com/fmartingr), [FokinAleksandr](https://github.com/FokinAleksandr), [GabrielCasaro](https://github.com/GabrielCasaro), [gabrieljackson](https://github.com/gabrieljackson), [gabsfrancis](https://translate.mattermost.com/user/gabsfrancis), [grundleborg](https://github.com/grundleborg), [hanzei](https://github.com/hanzei), [harsh4723](https://github.com/harsh4723), [harshilsharma63](https://github.com/harshilsharma63), [hasancankucuk](https://github.com/hasancankucuk), [hereje](https://github.com/hereje), [hmhealey](https://github.com/hmhealey), [ifoukarakis](https://github.com/ifoukarakis), [isacikgoz](https://github.com/isacikgoz), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [johnsonbrothers](https://github.com/johnsonbrothers), [jprusch](https://translate.mattermost.com/user/jprusch), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [ludvigbolin](https://github.com/ludvigbolin), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [morgancz](https://github.com/morgancz), [mvitale1989](https://github.com/mvitale1989), [neflyte](https://github.com/neflyte), [nickmisasi](https://github.com/nickmisasi), [Paul-Stern](https://github.com/Paul-Stern), [pgteekens](https://translate.mattermost.com/user/pgteekens), [phoinixgrr](https://github.com/phoinixgrr), [PromoFaux](https://github.com/PromoFaux), [PulkitGarg-code](https://github.com/PulkitGarg-code), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [rajatdangat](https://github.com/rajatdangat), [relwell](https://github.com/relwell), [roaslin](https://github.com/roaslin), [rohan-kapse](https://github.com/rohan-kapse), [rohitkbc](https://github.com/rohitkbc), [Rutam21](https://github.com/Rutam21), [RyoKub](https://github.com/RyoKub), [saakshiraut28](https://github.com/saakshiraut28), [San4es](https://github.com/San4es), [sapnasivakumar](https://github.com/sapnasivakumar), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [Sharuru](https://github.com/Sharuru), [ShlokJswl](https://github.com/ShlokJswl), [sinansonmez](https://github.com/sinansonmez), [srappan](https://github.com/srappan), [sri-byte](https://github.com/sri-byte), [srisri332](https://github.com/srisri332), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [Sudhanva-Nadiger](https://github.com/Sudhanva-Nadiger), [svelle](https://github.com/svelle), [Syed-Ali-Abbas-Zaidi](https://github.com/Syed-Ali-Abbas-Zaidi), [tanmaythole](https://github.com/tanmaythole), [TealWater](https://github.com/TealWater), [thomasbrq](https://github.com/thomasbrq), [ThrRip](https://github.com/ThrRip), [toninis](https://github.com/toninis), [tsabi](https://github.com/tsabi), [umrkhn](https://github.com/umrkhn), [varghesejose2020](https://github.com/varghesejose2020), [Vinecreeper888](https://github.com/Vinecreeper888), [weblate](https://github.com/weblate), [wiggin77](https://github.com/wiggin77), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yomiadetutu1](https://github.com/yomiadetutu1), [ZubairImtiaz3](https://github.com/ZubairImtiaz3)

## Release v9.3 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

**Release Date: December 15, 2023**

### Important Upgrade Notes
 - Please read the [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) before upgrading.

### Compatibility
 - Updated minimum required Firefox version to v115+.
 - Updated minimum supported Chromium version to 118+.

### Improvements

See [this walkthrough video](https://www.youtube.com/watch?v=eXA8emM97Bo) on some of the improvements in our latest release below.

#### User Interface (UI)
 - Updated pre-packaged Playbooks plugin version to [v1.39.1](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v1.39.1).
 - Updated pre-packaged Calls version to [v0.21.1](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.21.1).
 - Updated pre-packaged Jira plugin version to [v4.0.1](https://github.com/mattermost/mattermost-plugin-jira/releases/tag/v4.0.1). Also see [v4.0.0](https://github.com/mattermost/mattermost-plugin-jira/releases/tag/v4.0.0) for recent breaking changes.
 - Added Vietnamese (Beta) as a new language.
 - Added the ability to passively track keywords with highlights without triggering a notification (Professional and Enterprise plans).
 - Updated the **Settings** modal with an improved user interface.
 - Added a new **Jump to recents** banner when a channel is scrolled up.
 - Modified the behavior of the code button (Ctrl+Alt+C) to create inline codes or code blocks.
 - Disabled markdown keybindings within code blocks.
 - Added a **Back** button to the ``/access_problem`` page.
 - Added a default limit of the number of reactions per post.

#### Performance
 - Removed pre-fetch preference and set new prefetch limits for the webapp.
 - Improved websocket event marshaling performance.
 - Batched loading of recently used emojis on initial load.

#### Administration
 - The tooltip on the announcement bar in the **System Console** is now widened.
 - Improved the error message when trying to activate a plugin in an unsupported environment.
 - Added a file storage permission check to the workspace health dashboard.
 - Performed a cleanup in preparation for adding support for multi-word keywords that trigger notification.
 - Added a warning log message when the app runs as root.
 - Removed all uses of the ``ExperimentalTimezone`` setting. The Timezone feature is now always enabled and no longer behind a configuration setting.
 - Added support for previewing WebVTT attachments.
 - Introduced separate ``AdvancedLogging`` levels for LDAP messages.
 - Introduced trace logging level for LDAP messages.
 - Added a new way to modify ``WebSocket`` messages sent to individual connections.
 - Added a new server side hook ``MessagesWillBeConsumed`` to allow modifying post objects after they are grabbed from the database but before they are delivered to the client. This is behind a feature flag and disabled by default.
 - Users and posts are now pretty-printed in the logs.
 - Improved file extraction logging.
 - Exposed ``ThreadView`` and ``AdvancedCreateComment`` components in the webapp plugin exported components list.
 - Added **Logging > Advanced Logging** setting to the **System Console** to allow admins to configure custom log targets via the user interface.

### Bug Fixes
 - Fixed an issue where marking a Group Message as unread didn't show the badge count correctly.
 - Fixed an issue where ``invite_id`` was being reset on all team changes.
 - Fixed an issue where interactive dialog elements with subtype ``number`` didn't handle a ``0`` value properly.
 - Fixed an issue with the download link in channel file search items when including a path in the **Site URL** setting.
 - Fixed an issue with the formatting of special mentions in the right-hand side.
 - Fixed ``MessageWillBeUpdated`` plugin hook to allow rejections.
 - Fixed an issue with some shortcuts not working as expected.
 - Fixed the message history not clearing the input on the center channel.
 - Fixed an issue where a higher contrast was generated for some usernames.
 - Fixed an issue where newly created Group Messages showed having 0 members.
 - Fixed an issue where an incorrect timestamp was assigned to support packet files.
 - Fixed an issue where the **Reset Password** link was not displayed if only LDAP/AD was enabled.
 - Fixed an issue where **Recent Mentions** showed posts for other similar named users.
 - Fixed an error that appeared when updating the header of Group Messages.
 - Fixed an issue that caused the server to get stuck during shutdown due to a deadlock in a dependency.
 - Fixed an issue where Desktop App clients would be shown an error when trying to open file preview links.
 - Fixed an issue with double URL encoding of Oauth redirect URI params.
 - Fixed an issue where users couldn't at-mention custom groups in group constrained teams and channels.
 - Fixed an issue where the channel admin wasn't being set when converting a Group Message to a private channel.

### config.json
 - Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
 - Removed ``DisplaySettings.ExperimentalTimezone`` setting.
 - Under ``ServiceSettings`` in ``config.json``:
    - Added ``DefaultUniqueReactionsPerPost`` and ``MaxUniqueReactionsPerPost`` to fix an issue where invalid reactions could be added to posts and to add a default limit for the number of reactions per post.

### API Changes
 - Added an API to batch requests for custom emojis on page load.

### Database Changes
 - ``NextSyncAt`` and ``Description`` columns are removed from the ``SharedChannelsRemotes`` table. Migration impact is considered to be minimal considering the possible table size.

### Go Version
 - v9.3 is built with Go ``v1.20.7``.

### Known Issues
 - Mattermost Omnibus: Unable to install omnibus due to unmet dependencies [MM-56080](https://mattermost.atlassian.net/browse/MM-56080).
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

### Contributors
 - [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [AirGoatOne](https://github.com/AirGoatOne), [akbarkz](https://github.com/akbarkz), [amigo7kr](https://github.com/amigo7kr), [amyblais](https://github.com/amyblais), [anneschuth](https://github.com/anneschuth), [ARJ2160](https://github.com/ARJ2160), [Arslan-work](https://github.com/Arslan-work), [arthurh](https://translate.mattermost.com/user/arthurh), [arthurhrg](https://github.com/arthurhrg), [Aryakoste](https://github.com/Aryakoste), [asaadmahmood](https://github.com/asaadmahmood), [AshishDhama](https://github.com/AshishDhama), [avas27JTG](https://github.com/avas27JTG), [AvaterClasher](https://github.com/AvaterClasher), [ayusht2810](https://github.com/ayusht2810), [azigler](https://github.com/azigler), [BandhiyaHardik](https://github.com/BandhiyaHardik), [BenCookie95](https://github.com/BenCookie95), [Benjamin-Loison](https://github.com/Benjamin-Loison), [calebroseland](https://github.com/calebroseland), [catenacyber](https://github.com/catenacyber), [cedarice](https://github.com/cedarice), [CI-YU](https://github.com/CI-YU), [coltoneshaw](https://github.com/coltoneshaw), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [Davut97](https://github.com/Davut97), [deepakumarvu](https://github.com/deepakumarvu), [devinbinnie](https://github.com/devinbinnie), [Dhoni77](https://github.com/Dhoni77), [DimitriDR](https://translate.mattermost.com/user/DimitriDR), [edwardnguyen225](https://github.com/edwardnguyen225), [Eleferen](https://translate.mattermost.com/user/Eleferen), [emdecr](https://github.com/emdecr), [Emil-Carlsson](https://github.com/Emil-Carlsson), [enahum](https://github.com/enahum), [escofresco](https://github.com/escofresco), [fandour](https://translate.mattermost.com/user/fandour), [fazil-syed](https://github.com/fazil-syed), [fmartingr](https://github.com/fmartingr), [gabrieljackson](https://github.com/gabrieljackson), [hanzei](https://github.com/hanzei), [harshal2030](https://github.com/harshal2030), [harshilsharma63](https://github.com/harshilsharma63), [heisdinesh](https://github.com/heisdinesh), [hmhealey](https://github.com/hmhealey), [ifoukarakis](https://github.com/ifoukarakis), [imamimam113](https://github.com/imamimam113), [imkrishnasarathi](https://github.com/imkrishnasarathi), [isacikgoz](https://github.com/isacikgoz), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [johndavidlugtu](https://github.com/johndavidlugtu), [johnsonbrothers](https://github.com/johnsonbrothers), [jonathanwiemers](https://github.com/jonathanwiemers), [jprusch](https://github.com/jprusch), [JulienTant](https://github.com/JulienTant), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kapdev](https://translate.mattermost.com/user/kapdev), [kayazeren](https://github.com/kayazeren), [Kimbohlovette](https://github.com/Kimbohlovette), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [KuSh](https://github.com/KuSh), [kyeongsoosoo](https://github.com/kyeongsoosoo), [larkox](https://github.com/larkox), [LeonardJouve](https://github.com/LeonardJouve), [lieut-data](https://github.com/lieut-data), [lindy65](https://github.com/lindy65), [linkvn](https://github.com/linkvn), [ludvigbolin](https://github.com/ludvigbolin), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [m1lt0n](https://github.com/m1lt0n), [majo](https://translate.mattermost.com/user/majo), [manojmalik20](https://github.com/manojmalik20), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [maxtrem271991](https://github.com/maxtrem271991), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [mozi47](https://github.com/mozi47), [mvitale1989](https://github.com/mvitale1989), [nathanaelhoun](https://github.com/nathanaelhoun), [newdominic](https://github.com/newdominic), [nickmisasi](https://github.com/nickmisasi), [nosyn](https://github.com/nosyn), [otilor](https://github.com/otilor), [pacop](https://github.com/pacop), [Paul-Stern](https://github.com/Paul-Stern), [Paul-vrn](https://github.com/Paul-vrn), [phoinixgrr](https://github.com/phoinixgrr), [proggga](https://github.com/proggga), [pvev](https://github.com/pvev), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [rahulsuresh-git](https://github.com/rahulsuresh-git), [rashmibharambe](https://github.com/rashmibharambe), [Reene-Simon](https://github.com/Reene-Simon), [rohan-kapse](https://github.com/rohan-kapse), [rohitkbc](https://github.com/rohitkbc), [rubinaga](https://github.com/rubinaga), [RyoKub](https://github.com/RyoKub), [san70sh](https://github.com/san70sh), [sapnasivakumar](https://github.com/sapnasivakumar), [sbishel](https://github.com/sbishel), [seoyeongeun](https://github.com/seoyeongeun), [Sharuru](https://github.com/Sharuru), [shivamjosh](https://github.com/shivamjosh), [sinansonmez](https://github.com/sinansonmez), [Sn-Kinos](https://github.com/Sn-Kinos), [sp6370](https://github.com/sp6370), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [Sudhanva-Nadiger](https://github.com/Sudhanva-Nadiger), [sudheer121](https://github.com/sudheer121), [Syed-Ali-Abbas-Zaidi](https://github.com/Syed-Ali-Abbas-Zaidi), [tanmaythole](https://github.com/tanmaythole), [tejas161](https://github.com/tejas161), [thomasbrq](https://github.com/thomasbrq), [ThrRip](https://github.com/ThrRip), [TomerPacific](https://github.com/TomerPacific), [toninis](https://github.com/toninis), [trivikr](https://github.com/trivikr), [tsabi](https://github.com/tsabi), [turretkeeper](https://github.com/turretkeeper), [umrkhn](https://github.com/umrkhn), [vish9812](https://github.com/vish9812), [wcdfilll](https://translate.mattermost.com/user/wcdfilll), [wiebel](https://github.com/wiebel), [wiggin77](https://github.com/wiggin77), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yomiadetutu1](https://github.com/yomiadetutu1)

## Release v9.2 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

- **9.2.3, released 2023-11-29**
  - Mattermost v9.2.3 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.2.3 contains no database or functional changes.
  - Pre-packaged Calls plugin version [v0.21.1](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.21.1).
- **9.2.2, released 2023-11-08**
  - Mattermost v9.2.2 contains a high severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Playbooks plugin version [v1.39.1](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v1.39.1).
  - Fixed an issue where the **About Mattermost** dialog reported an incorrect server version.
- **9.2.1, released 2023-11-06**
  - Fixed an issue where Ubuntu GLIBC errors were thrown on Ubuntu 20.04 and Debian Bullseye versions.
- **9.2.0, released 2023-11-02**
  - Original 9.2.0 release

### Important Upgrade Notes
 - Fixed data retention policies to run jobs when any custom retention policy is enabled even when the global retention policy is set to **keep-forever**. Before this fix, the enabled custom data retention policies wouldn’t run as long as the global data retention policy was set to **keep-forever** or was disabled. After the fix, the custom data retention policies will run automatically even when the global data retention policy is set to **keep-forever**. Once the server is upgraded, posts may unintentionally be deleted. Admins should make sure to disable all custom data retention policies before upgrading, and then re-enable them again after upgrading.

```{Important}
If you upgrade from a release earlier than v9.1, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Compatibility
 - Updated minimum required Edge version to 116+.

### Improvements

See [this walkthrough video](https://www.youtube.com/watch?v=udC2OCTGooc&feature=youtu.be&ab_channel=Mattermost) on some of the improvements in our latest release below.

#### User Interface (UI)
 - Improved readability by displaying system messages on multiple lines when editing a channel header.
 - Combined "joined/left" event types in system messages.
 - Added a new user preference to disable webapp prefetching via **Settings > Advanced > Allow Mattermost to prefetch channel posts**. You must enable **Client Performance Debugging** in the System Console by going to **Environment > Developer** in order for this setting to appear. This setting and Client Performance Debugging should only be enabled temporarily if users are experiencing performance issues.
 - Pre-packaged NPS plugin version [v1.3.3](https://github.com/mattermost/mattermost-plugin-nps/releases/tag/v1.3.3).
 - Pre-packaged Todo plugin version [v0.7.1](https://github.com/mattermost/mattermost-plugin-todo/releases/tag/v0.7.1).

#### Administration
 - JSON null value cases are now handled correctly by also checking that the pointer is no longer null when unmarshalling to a pointer.
 - An annotated logger is now used to capture LDAP and SAML logs.
 - Replaced ``github.com/mattermost/gziphandler`` with ``github.com/klauspost/compress/gzhttp``.
 - Performance metrics now contain information on if a given request was sent during a page load or a websocket reconnect.
 - Elasticsearch aggregation jobs no longer start when a bulk indexing job is currently running.
 - Added heap profile, CPU profile, and goroutines profile to the support package.
 - Merged WIP i18n locales, but disallowed selecting unsupported locales.

### Bug Fixes
 - Fixed a panic where a simple worker would crash if it failed to get a job.
 - Fixed post props on update to properly see channel links.
 - Fixed an issue where the API for drafts would return empty drafts.
 - Fixed the alignment of the **Help** menu in the global header.
 - Fixed a broken link in the **Edit Channel** header modal.
 - Fixed an issue that prevented users to be added to channels from the System Console.
 - Fixed an issue where the channel member count increased when adding an already present user.
 - Fixed an issue where plugin developers were unable to create a ``textarea`` in interactive dialogs.
 - Fixed an issue where copy pasting images from Chrome failed.

### config.json
 - Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
 - Under ``LogSettings`` in ``config.json``:
   - Added a new configuration setting ``MaxFieldSize`` to add the ability to size-limit log fields during logging.

### API Changes
 - Added ``origin_client`` to the ``mattermost_api_time`` metrics.

### Go Version
 - v9.2 is built with Go ``v1.20.7``.

### Known Issues
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

### Contributors
 - [aayushborkar14](https://github.com/aayushborkar14), [AayushChaudhary0001](https://github.com/AayushChaudhary0001), [AbhineshJha](https://github.com/AbhineshJha), [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [akaMrDC](https://github.com/akaMrDC), [akbarkz](https://github.com/akbarkz), [alejdg](https://github.com/alejdg), [Alphanum404](https://github.com/Alphanum404), [amigo7kr](https://translate.mattermost.com/user/amigo7kr), [amyblais](https://github.com/amyblais), [amynicol1985](https://github.com/amynicol1985), [andrew-delph](https://github.com/andrew-delph), [andrleite](https://github.com/andrleite), [angeloskyratzakos](https://github.com/angeloskyratzakos), [aniketh-varma](https://github.com/aniketh-varma), [anneschuth](https://translate.mattermost.com/user/anneschuth), [apshada](https://github.com/apshada), [ARJ2160](https://github.com/ARJ2160), [ArturBa](https://github.com/ArturBa), [asaadmahmood](https://github.com/asaadmahmood), [AsisRout](https://github.com/AsisRout), [avas27JTG](https://github.com/avas27JTG), [AvaterClasher](https://github.com/AvaterClasher), [ayrotideysarkar](https://github.com/ayrotideysarkar), [ayusht2810](https://github.com/ayusht2810), [balajik](https://github.com/balajik), [Bangik](https://github.com/Bangik), [bartaz](https://translate.mattermost.com/user/bartaz), [BaumiCoder](https://github.com/BaumiCoder), [BenCookie95](https://github.com/BenCookie95), [bishalpal](https://github.com/bishalpal), [calebroseland](https://github.com/calebroseland), [cedarice](https://translate.mattermost.com/user/cedarice), [cescpmantidfly](https://translate.mattermost.com/user/cescpmantidfly), [CI-YU](https://github.com/CI-YU), [Ciggzy1312](https://github.com/Ciggzy1312), [codeEmpress1](https://github.com/codeEmpress1), [coltoneshaw](https://github.com/coltoneshaw), [costa-neto](https://github.com/costa-neto), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [danialkeimasi](https://github.com/danialkeimasi), [Delaney](https://github.com/Delaney),  [devinbinnie](https://github.com/devinbinnie), [DHaussermann](https://github.com/DHaussermann), [dhnlr](https://github.com/dhnlr), [dipandhali2021](https://github.com/dipandhali2021), [Eleferen](https://translate.mattermost.com/user/Eleferen), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [escofresco](https://github.com/escofresco), [esethna](https://github.com/esethna), [fazil-syed](https://github.com/fazil-syed), [fmartingr](https://github.com/fmartingr), [frjaraur](https://github.com/frjaraur), [fyfirman](https://github.com/fyfirman), [gabrieljackson](https://github.com/gabrieljackson), [Gauravpadam](https://github.com/Gauravpadam), [gibsonliketheguitar](https://github.com/gibsonliketheguitar), [h1usertest](https://translate.mattermost.com/user/h1usertest), [hanzei](https://github.com/hanzei), [harsh-solanki21](https://github.com/harsh-solanki21), [harshal2030](https://github.com/harshal2030), [harshalkh](https://github.com/harshalkh), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [ialorro](https://github.com/ialorro), [ifoukarakis](https://github.com/ifoukarakis), [imamimam113](https://translate.mattermost.com/user/imamimam113), [isacikgoz](https://github.com/isacikgoz), [iyampaul](https://github.com/iyampaul), [izruff](https://github.com/izruff), [janlengyel](https://github.com/janlengyel), [jannikbertram](https://github.com/jannikbertram), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jgilliam17](https://github.com/jgilliam17), [jlandells](https://github.com/jlandells), [johnsonbrothers](https://github.com/johnsonbrothers), [josephjosedev](https://github.com/josephjosedev), [jprusch](https://github.com/jprusch), [js029](https://github.com/js029), [jufab](https://github.com/jufab), [JulienTant](https://github.com/JulienTant), [kaakaa](https://github.com/kaakaa), [kalvdans](https://github.com/kalvdans), [kayazeren](https://github.com/kayazeren), [komodin](https://github.com/komodin), [Kritik-J](https://github.com/Kritik-J), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [KuSh](https://github.com/KuSh), [larkox](https://github.com/larkox), [letehaha](https://github.com/letehaha), [libklein](https://github.com/libklein), [lieut-data](https://github.com/lieut-data), [linkvn](https://github.com/linkvn), [ludvigbolin](https://github.com/ludvigbolin), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo), [manojmalik20](https://github.com/manojmalik20), [ManuMinue](https://github.com/ManuMinue), [marianunez](https://github.com/marianunez), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99),  [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [maxtrem271991](https://github.com/maxtrem271991), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [milotype](https://translate.mattermost.com/user/milotype), [mishmanners](https://github.com/mishmanners), [MixeroTN](https://github.com/MixeroTN), [mnj93](https://github.com/mnj93), [mujpao](https://github.com/mujpao), [mustdiechik](https://github.com/mustdiechik), [mvitale1989](https://github.com/mvitale1989), [namanh-asher](https://github.com/namanh-asher), [Navystack](https://github.com/Navystack), [nickmisasi](https://github.com/nickmisasi), [Nico7as](https://translate.mattermost.com/user/Nico7as), [Nityanand13](https://github.com/Nityanand13), [NohaFahmi](https://github.com/NohaFahmi), [otilor](https://github.com/otilor), [Paul-vrn](https://github.com/Paul-vrn), [Peyo6565](https://github.com/Peyo6565), [phoinixgrr](https://github.com/phoinixgrr), [pvev](https://github.com/pvev), [qryptdev](https://github.com/qryptdev), [Quijuletim470](https://translate.mattermost.com/user/Quijuletim470), [returnedinformation](https://github.com/returnedinformation), [riteshmukim](https://github.com/riteshmukim), [rubinaga](https://github.com/rubinaga), [Rutam21](https://github.com/Rutam21), [saideepesh000](https://github.com/saideepesh000), [SaketKaswa20](https://github.com/SaketKaswa20), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [seoyeongeun](https://translate.mattermost.com/user/seoyeongeun), [Sharuru](https://github.com/Sharuru), [sjcode99](https://github.com/sjcode99), [sondrekje](https://github.com/sondrekje), [sonu27](https://github.com/sonu27), [sp6370](https://github.com/sp6370), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [StreakInTheSky](https://github.com/StreakInTheSky), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [Sudhanva-Nadiger](https://github.com/Sudhanva-Nadiger), [sudheer121](https://github.com/sudheer121), [syedzubeen](https://github.com/syedzubeen), [Tahanima](https://github.com/Tahanima),[tanmaythole](https://github.com/tanmaythole), [this-is-tobi](https://github.com/this-is-tobi), [ThrRip](https://github.com/ThrRip), [TomerPacific](https://github.com/TomerPacific), [toninis](https://github.com/toninis), [trilopin](https://github.com/trilopin), [umrkhn](https://github.com/umrkhn), [varghesejose2020](https://github.com/varghesejose2020), [venugopal1234567](https://github.com/venugopal1234567), [vip2441](https://github.com/vip2441), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yesbhautik](https://github.com/yesbhautik), [ylac](https://github.com/ylac), [ZubairImtiaz3](https://github.com/ZubairImtiaz3)
