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
 - Please read the [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) before upgrading.

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
