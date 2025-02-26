# v10 changelog

```{Important}
```{include} common-esr-support-upgrade.md
```

(release-v10.5-extended-support-release)=
## Release v10.5 - [Extended Support Release](https://docs.mattermost.com/about/release-policy.html#release-types)

- **10.5.1, released 2025-02-19**
  - Mattermost v10.5.1 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Boards plugin [v9.1.1](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.1.1).
  - Pre-packaged Playbooks plugin [v2.1.1](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v2.1.1).
  - Fixed an issue in Compliance Exports whereby a missing file attachment in S3 could prevent the export run from completing [MM-62527](https://mattermost.atlassian.net/browse/MM-62527).
  - Mattermost v10.5.1 contains the following functional changes:
      - A new configuration setting ``ServiceSettings.EnableWebHubChannelIteration`` was added which allows a user to control the performance of websocket broadcasting. By default, this setting is turned off. If it is turned on, it improves the websocket broadcasting performance at the expense of poor performance when users join/leave a channel. It is not recommended to turn it on unless you have atleast 200,000 concurrent users actively using Mattermost.
- **10.5.0, released 2025-02-14**
  - Original 10.5.0 release.

### Compatibility
 - Updated minimum Safari version to 17.4+ and minimum Firefox version to 119+.

### Important Upgrade Notes
 - v10.5 introduces Property System Architecture schema migration. See the [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) for details.
 - The Compliance Export system has been overhauled. See the [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) for details.
 - The Mattermost server has stopped supporting manual plugin deployment. Plugins were deployed manually when an administrator or some deployment automation copies the contents of a plugin bundle into the server's working directory. If a manual or automated deployment workflow is still required, administrators can instead prepackage the plugin bundles. See more details in [this forum post](https://forum.mattermost.com/t/deprecation-notice-manual-plugin-deployment/21192).
 - Mattermost has stopped official Mattermost server builds for the Microsoft Windows operating system. Administrators should migrate existing Mattermost server installations to use the official Linux builds. See more details in [this forum post](https://forum.mattermost.com/t/deprecation-notice-server-builds-for-microsoft-windows/21498).

### Breaking Changes
- The internal workings of the `PluginLinkComponent` in the web app have been changed to unmount link tooltips from the DOM by default, significantly improving performance. Plugins that register link tooltips using `registerLinkTooltipComponent` will experience changes in how tooltip components are managed—they are now only mounted when a link is hovered over or focused. As a result, plugins may need to update their components to properly handle mounting and unmounting scenarios. For example, changes were made in [mattermost-plugin-jira](https://github.com/mattermost/mattermost-plugin-jira/pull/1145), where componentDidUpdate lifecycle hook was replaced with componentDidMount. If your plugin’s tooltip component is a functional React component, there is a high chance that this behavior will be handled automatically, as it would be managed by useEffect with an empty dependency array.

```{Important}
If you upgrade from a release earlier than v10.3, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Improvements

#### User Interface (UI)
 - Pre-packaged Boards plugin [v9.1.0](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.1.0).
 - Pre-packaged Calls plugin [v1.5.1](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v1.5.1).
 - Pre-packaged MS Teams plugin [v2.1.0](https://github.com/mattermost/mattermost-plugin-msteams/releases/tag/v2.1.0).
 - Pre-packaged Channel Export plugin [v1.2.1](https://github.com/mattermost/mattermost-plugin-channel-export/releases/tag/v1.2.1).
 - Pre-packaged Jira plugin [v4.2.0](https://github.com/mattermost/mattermost-plugin-jira/releases/tag/v4.2.0).
 - Added the ability to modify post attachments during edit.
 - The channel bookmarks bar is now hidden when there are no bookmarks in the channel. Bookmarks can now be added from the channel menu.
 - Removed the video from the onboarding checklist.
 - Improved accessibility throughout the webapp by fixing several issues around keyboard navigation and screen reader focused on modals, right-hand side and core chat functionality. 

#### Administration
 - Added the migrations, store layer and service for the Property System Architecture.
 - Added Custom Profile Attributes, an experimental Enterprise-only feature. This feature is disabled by default. To enable this feature, set the feature flag `CustomProfileAttributes`. Once enabled, administrators can access the System Properties section in the System Console to create and manage custom user profile fields. The initial release supports text fields only.
 - Added the Custom Profile Attribute fields store, app and API endpoints.
 - Introduced V2 of the Support Packet, containing improvement diagnosis information for high-availability deployments.
 - Added a new ``Fallback`` field to ``PluginSettingsSection`` that controls whether the settings defined under the section should still render as fallback when the plugin is disabled.
 - Updated the library used for tooltips throughout the app to fix a memory leak.
 - Reduced the volume of unnecessary debug logs generated during scheduled post job execution.
 - Removed ``form-data`` from @mattermost/client.

### Bug Fixes
 - Fixed archived filter behavior in System Console > User Management > Channels to restore the ability to exclude archived channels.
 - Fixed an issue where DMs/GMs with a `DeleteAt` non-zero value in the database might cause issues with several APIs.
 - Fixed an issue where the team sidebar's mention count could be out of sync with the thread count.
 - Fixed an issue where replies with props could not be imported.
 - Fixed an issue where ``pluginapi.store.GetReplicaDB`` returned nil if masterDB was not initialized.
 - Fixed an issue in ``SqlPostStore.PermanentDeletebyUser`` where no error was returned when 10K posts were exceeded.
 - Fixed an issue where a channel would no longer be exported for Bulk Export workflow if any of the users of a Direct or Group Message channel were permanently deleted.
 - Fixed an issue where the scroll position reset when custom emojis were requested.
 - Fixed a panic during LDAP synchronization.
 - Fixed an issue where the bulk export retention job would accidentally delete non-bulk export files and directories.
 - Fixed an issue where archived channels were not searchable with Elasticsearch/OpenSearch if ``TeamSettings.ExperimentalViewArchivedChannels`` was enabled. If there are old channels which were archived before a bulk index was run, users would need to purge indexes, and do bulk index again. Because those old archived channels are removed from the index when a bulk index is run.

### config.json
New setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Enterprise plans:
 - Under ``essageExportSettings`` in ``config.json``:
   - Added ``ComplianceExportDirectoryFormat``, ``ComplianceExportPath``, ``ComplianceExportPathCLI``, ``ComplianceExportChannelBatchSizeDefault``, and ``ComplianceExportChannelHistoryBatchSizeDefault`` for compliance export overhaul.

### API Changes
 - ``GetUsersInChannelDuring`` now accepts a slice; added ``GetChannelsWithActivityDuring``.
 - Two new boolean query parameters were added to the ``api/v4/config`` endpoint:
    - ``remove_defaults`` (filters out default values).
    - ``remove_masked`` (removes masked fields). 

### Go Version
 - v10.5 is built with Go ``v1.22.6``.

### Known Issues
 - Setting the license file location through an envvar still gives the option to upload a new license through the System Console, resulting in the license being overwritten by the one set through the envvar. See this [knowledge base article](https://support.mattermost.com/hc/en-us/articles/33911983851284-System-console-still-displays-old-license-after-uploading-a-new-one) on how to resolve this issue.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.

### Contributors
 - [agarciamontoro](https://github.com/agarciamontoro), [agardelein](https://github.com/agardelein), [agnivade](https://github.com/agnivade), [amyblais](https://github.com/amyblais), [andrleite](https://github.com/andrleite), [angeloskyratzakos](https://github.com/angeloskyratzakos), [Aryakoste](https://github.com/Aryakoste), [asaadmahmood](https://github.com/asaadmahmood), [AulakhHarsh](https://github.com/AulakhHarsh), [ayush-chauhan233](https://github.com/ayush-chauhan233), [BenCookie95](https://github.com/BenCookie95), [bshumylo](https://translate.mattermost.com/user/bshumylo), [calebroseland](https://github.com/calebroseland), [code1492](https://github.com/code1492), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [devinbinnie](https://github.com/devinbinnie), [dmanpearl](https://github.com/dmanpearl), [Dschoordsch](https://github.com/Dschoordsch), [ebuildy](https://github.com/ebuildy), [Eleferen](https://translate.mattermost.com/user/Eleferen), [emmapeel2](https://github.com/emmapeel2), [enahum](https://github.com/enahum), [enzowritescode](https://github.com/enzowritescode), [esarafianou](https://github.com/esarafianou), [fmartingr](https://github.com/fmartingr), [frankps](https://translate.mattermost.com/user/frankps), [fsilye](https://github.com/fsilye), [fume4mattermost](https://github.com/fume4mattermost), [gabrieljackson](https://github.com/gabrieljackson), [hannaparks](https://github.com/hannaparks), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [henrique](https://translate.mattermost.com/user/henrique), [hmhealey](https://github.com/hmhealey), [Honsei901](https://github.com/Honsei901), [hpflatorre](https://github.com/hpflatorre), [ifoukarakis](https://github.com/ifoukarakis), [isacikgoz](https://github.com/isacikgoz), [jespino](https://github.com/jespino), [johnsonbrothers](https://github.com/johnsonbrothers), [jprusch](https://github.com/jprusch), [juliemanalo](https://github.com/juliemanalo), [JulienTant](https://github.com/JulienTant), [jure](https://translate.mattermost.com/user/jure), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kasyap1234](https://github.com/kasyap1234), [kayazeren](https://translate.mattermost.com/user/kayazeren), [kondo97](https://github.com/kondo97), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo), [marianunez](https://github.com/marianunez), [master7](https://translate.mattermost.com/user/master7), [matthewbirtch](https://github.com/matthewbirtch), [MattSilvaa](https://github.com/MattSilvaa), [mgdelacroix](https://github.com/mgdelacroix), [Morgansvk](https://github.com/Morgansvk), [mvitale1989](https://github.com/mvitale1989), [NadavTasher](https://github.com/NadavTasher), [narutoxboy](https://translate.mattermost.com/user/narutoxboy), [NCPSNetworks](https://github.com/NCPSNetworks), [nickmisasi](https://github.com/nickmisasi), [otbutz](https://github.com/otbutz), [pvev](https://github.com/pvev), [rahimrahman](https://github.com/rahimrahman), [Rajat-Dabade](https://github.com/Rajat-Dabade), [Reinkard](https://github.com/Reinkard), [robregonm](https://github.com/robregonm), [sarthak0714](https://github.com/sarthak0714), [saturninoabril](https://github.com/saturninoabril), [SaurabhSharma-884](https://github.com/SaurabhSharma-884), [sbishel](https://github.com/sbishel), [Sharuru](https://github.com/Sharuru), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [svelle](https://github.com/svelle), [ThrRip](https://github.com/ThrRip), [toninis](https://github.com/toninis), [tormi](https://translate.mattermost.com/user/tormi), [uday-rana](https://github.com/uday-rana), [unode](https://github.com/unode), [varghesejose2020](https://github.com/varghesejose2020), [Victor-Nyagudi](https://github.com/Victor-Nyagudi), [vish9812](https://github.com/vish9812), [wetneb](https://github.com/wetneb), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [willypuzzle](https://github.com/willypuzzle), [X1Vi](https://github.com/X1Vi), [yasserfaraazkhan](https://github.com/yasserfaraazkhan)

(release-v10.4-feature-release)=
## Release v10.4 - [Feature Release](https://docs.mattermost.com/about/release-policy.html#release-types)

- **10.4.3, released 2025-02-19**
  - Mattermost v10.4.3 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Boards plugin [v9.1.1](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.1.1).
  - Pre-packaged Playbooks plugin [v2.1.1](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v2.1.1).
  - Fixed an issue in Compliance Exports whereby a missing file attachment in S3 could prevent the export run from completing [MM-62527](https://mattermost.atlassian.net/browse/MM-62527).
  - Fixed an issue where the bulk export retention job could accidentally delete non-bulk export files and directories [MM-62527](https://mattermost.atlassian.net/browse/MM-62527).
  - Mattermost v10.4.3 contains the following functional changes:
      - A new configuration setting ``ServiceSettings.EnableWebHubChannelIteration`` was added which allows a user to control the performance of websocket broadcasting. By default, this setting is turned off. If it is turned on, it improves the websocket broadcasting performance at the expense of poor performance when users join/leave a channel. It is not recommended to turn it on unless you have atleast 200,000 concurrent users actively using Mattermost.
- **10.4.2, released 2025-01-22**
  - Mattermost v10.4.2 contains critical severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Boards plugin [v9.0.5](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.0.5).
  - Pre-packaged Channel Export plugin [v1.2.1](https://github.com/mattermost/mattermost-plugin-channel-export/releases/tag/v1.2.1).
  - Fixed a panic during LDAP synchronization [MM-61239](https://mattermost.atlassian.net/browse/MM-61239).
  - Fixed an issue with webhook attachment button styles [MM-62400](https://mattermost.atlassian.net/browse/MM-62400).
  - Mattermost v10.4.2 contains no database or functional changes.
- **10.4.1, released 2025-01-16**
  - Fixed errors logged by performance telemetry due to certain browser extensions [MM-62371](https://mattermost.atlassian.net/browse/MM-62371).
  - Fixed an issue with insertion errors to ``LinkMetadata`` table.
  - Mattermost v10.4.1 contains no database or functional changes.
- **10.4.0, released 2025-01-16**
  - Original 10.4.0 release.

```{Important}
If you upgrade from a release earlier than v10.3, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Improvements

#### User Interface (UI)
 - Pre-packaged Calls plugin [v1.4.0](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v1.4.0).
 - Pre-packaged Boards plugin [v9.0.2](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.0.2).
 - Improved the handling of Thai script in search terms.
 - Added tooltips to the buttons shown in the channel info in the right pane.
 - Downgraded Spanish language to Alpha.
 - Removed the feature to import themes from Slack.

#### Administration
 - Redis is now available as an alternative cache backend for all Enterprise customers. It can be leveraged to run Mattermost at a very high scale.
 - Plugins are now allowed to add Support Packet data without user interface elements.
 - Improved the detection of the mobile app operating system as stored in the **Sessions** table.

### Bug Fixes
 - Fixed an issue where imported replies were missing their reactions.
 - Fixed an issue with how links in Markdown headings are displayed in the Threads list.
 - Fixed an issue where marking a channel as read wouldn't persist through a refresh.
 - Fixed a warning in the Support Packet about an unreadable LDAP server even if LDAP was disabled.
 - Fixed an issue where multiple timezones were highlighted when selecting certain timezones.
 - Fixed an issue where unread messages on other teams would not appear after the application reconnected to the server.
 - Fixed an issue where the scrollbar was not clickable when there was a toaster.
 - Fixed an issue when pressing **Page Up** or **Page Down** on a long message (scrollable) with the right sidebar open.
 - Fixed an issue with incorrect reporting in the **Server Updates** section in **System Console > Workspace Optimizations**.
 - Fixed an issue where EXIF rotated image previews did not have the correct size.
 - Fixed an issue where the search input field in the emoji picker did not accept uppercase letters.
 - Fixed an issue where imported replies were missing their reactions.
 - Fixed an issue where System Administrators could not pull posts from Direct Message channels that they were not in.
 - Fixed an issue by restoring System Administrator access to Direct and Group Messages without being a member.

### config.json
New setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
- Under ``LocalizationSettings`` in ``config.json``:
  - Added a new ``EnableExperimentalLocales`` configuration setting that controls whether to allow the selection of experimental (e.g., in progress) languages.

#### Changes to Enterprise plans:
 - Under ``CacheSettings`` in ``config.json``:
   - Added ``CacheType``: This can be either ``lru`` or ``redis``. ``lru`` is the default choice which will use the in-memory cache store that we use currently.
   - Added ``RedisAddress``: The hostname of the Redis host.
   - Added ``RedisPassword``: The password of the Redis host (can be left blank if there is no password).
   - Added ``RedisDB``: The database of the Redis host. Typically ``0``.
   - Added ``DisableClientCache``: This can be set to ``true`` if you decide to disable the client-side cache of Redis. Typically there is no need to do this in production, and this is mainly used as a test option.
 - Under ``FileSettings`` in ``config.json``:
   - Added new ``AmazonS3StorageClass`` and ``ExportAmazonS3StorageClass``, both default to ``""`` to preserve the current behavior. Administrators may configure this storage class to the storage class required by their S3 solution.

### API Changes
 - Added a new query string to exclude threads that are not part of the team ``GET api/v4/users/{user_id:[A-Za-z0-9]+}/teams/{team_id:[A-Za-z0-9]+}/threads``.

### Websocket Event Changes
 - Added a new ``server_hostname`` field to the websocket ``HELLO`` event.

### Go Version
 - v10.4 is built with Go ``v1.22.6``.

### Known Issues
 - Setting the license file location through an envvar still gives the option to upload a new license through the System Console, resulting in the license being overwritten by the one set through the envvar. See this [knowledge base article](https://support.mattermost.com/hc/en-us/articles/33911983851284-System-console-still-displays-old-license-after-uploading-a-new-one) on how to resolve this issue.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.

### Contributors
 - [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [akbarkz](https://translate.mattermost.com/user/akbarkz), [amyblais](https://github.com/amyblais), [and-ri](https://github.com/and-ri), [andreabia](https://translate.mattermost.com/user/andreabia), [andrleite](https://github.com/andrleite), [angeloskyratzakos](https://github.com/angeloskyratzakos), [Aryakoste](https://github.com/Aryakoste), [AulakhHarsh](https://github.com/AulakhHarsh), [ayush-chauhan233](https://github.com/ayush-chauhan233), [BenCookie95](https://github.com/BenCookie95), [calebroseland](https://github.com/calebroseland), [callmeott](https://github.com/callmeott), [catalintomai](https://github.com/catalintomai), [creeper-0910](https://github.com/creeper-0910), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [davidkrauser](https://github.com/davidkrauser), [Destrosvet](https://translate.mattermost.com/user/Destrosvet), [devinbinnie](https://github.com/devinbinnie), [DHaussermann](https://github.com/DHaussermann), [Eleferen](https://translate.mattermost.com/user/Eleferen), [enahum](https://github.com/enahum), [enzowritescode](https://github.com/enzowritescode), [esarafianou](https://github.com/esarafianou), [esethna](https://github.com/esethna), [ewwollesen](https://github.com/ewwollesen), [fmartingr](https://github.com/fmartingr), [frankps](https://translate.mattermost.com/user/frankps), [fsilye](https://github.com/fsilye), [fume4mattermost](https://github.com/fume4mattermost), [fxnm](https://github.com/fxnm), [gabrielctn](https://github.com/gabrielctn), [gabrieljackson](https://github.com/gabrieljackson), [gabsfrancis](https://translate.mattermost.com/user/gabsfrancis), [Gesare5](https://github.com/Gesare5), [Haliax](https://translate.mattermost.com/user/Haliax), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [henrique](https://translate.mattermost.com/user/henrique), [hmhealey](https://github.com/hmhealey), [Honsei901](https://github.com/Honsei901), [hpflatorre](https://github.com/hpflatorre), [ifoukarakis](https://github.com/ifoukarakis), [isacikgoz](https://github.com/isacikgoz), [jespino](https://github.com/jespino), [jessiekahn](https://github.com/jessiekahn), [joakim.rivera](https://translate.mattermost.com/user/joakim.rivera), [johnsonbrothers](https://github.com/johnsonbrothers), [jprusch](https://translate.mattermost.com/user/jprusch), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [Kuruyia](https://github.com/Kuruyia), [kyrillosisaac2](https://github.com/kyrillosisaac2), [lani009](https://translate.mattermost.com/user/lani009), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [lorumic](https://github.com/lorumic), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo), [marianunez](https://github.com/marianunez), [massimo](https://translate.mattermost.com/user/massimo), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w), [mh4ckt3mh4ckt1c4s](https://translate.mattermost.com/user/mh4ckt3mh4ckt1c4s), [minchae.lee](https://translate.mattermost.com/user/minchae.lee), [morgancz](https://translate.mattermost.com/user/morgancz), [Morgansvk](https://github.com/Morgansvk), [muratbayan](https://translate.mattermost.com/user/muratbayan), [mvitale1989](https://github.com/mvitale1989), [nbruneau71250](https://translate.mattermost.com/user/nbruneau71250), [nickmisasi](https://github.com/nickmisasi), [nikolaiz](https://translate.mattermost.com/user/nikolaiz), [Nityanand13](https://github.com/Nityanand13), [pmokeev](https://github.com/pmokeev), [potatogim](https://github.com/potatogim), [pvev](https://github.com/pvev), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [rahimrahman](https://github.com/rahimrahman), [Rajat-Dabade](https://github.com/Rajat-Dabade), [Reinkard](https://github.com/Reinkard), [renaudk](https://github.com/renaudk), [ricardogalvao](https://translate.mattermost.com/user/ricardogalvao), [RS-labhub](https://github.com/RS-labhub), [Rutam21](https://github.com/Rutam21), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [Sharuru](https://github.com/Sharuru), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [sypianski](https://translate.mattermost.com/user/sypianski), [TenGentoppa](https://translate.mattermost.com/user/TenGentoppa), [TheInvincibleRalph](https://github.com/TheInvincibleRalph), [ThrRip](https://github.com/ThrRip), [tnir](https://github.com/tnir), [tokipulan](https://translate.mattermost.com/user/tokipulan), [tomdereub](https://translate.mattermost.com/user/tomdereub), [toninis](https://github.com/toninis), [wetneb](https://github.com/wetneb), [wiggin77](https://github.com/wiggin77), [YahyaHaq](https://github.com/YahyaHaq), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yesbhautik](https://github.com/yesbhautik), [zenocode-org](https://translate.mattermost.com/user/zenocode-org)

(release-v10.3-feature-release)=
## Release v10.3 - [Feature Release](https://docs.mattermost.com/about/release-policy.html#release-types)

- **10.3.4, released 2025-02-19**
  - Mattermost v10.3.4 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Boards plugin [v9.1.1](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.1.1).
  - Pre-packaged Playbooks plugin [v2.1.1](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v2.1.1).
  - Fixed an issue in Compliance Exports whereby a missing file attachment in S3 could prevent the export run from completing [MM-62527](https://mattermost.atlassian.net/browse/MM-62527).
  - Mattermost v10.3.4 contains the following functional changes:
      - A new configuration setting ``ServiceSettings.EnableWebHubChannelIteration`` was added which allows a user to control the performance of websocket broadcasting. By default, this setting is turned off. If it is turned on, it improves the websocket broadcasting performance at the expense of poor performance when users join/leave a channel. It is not recommended to turn it on unless you have atleast 200,000 concurrent users actively using Mattermost.
- **10.3.3, released 2025-01-22**
  - Mattermost v10.3.3 contains critical severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Boards plugin [v9.0.5](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.0.5).
  - Pre-packaged Channel Export plugin [v1.2.1](https://github.com/mattermost/mattermost-plugin-channel-export/releases/tag/v1.2.1).
  - Fixed a panic during LDAP synchronization [MM-61239](https://mattermost.atlassian.net/browse/MM-61239).
  - Fixed an issue where the bulk export retention job would accidentally delete non-bulk export files and directories [MM-60888](https://mattermost.atlassian.net/browse/MM-60888).
  - Mattermost v10.3.3 contains no database or functional changes.
- **10.3.2, released 2025-01-15**
  - Mattermost v10.3.2 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Boards plugin [v9.0.2](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.0.2).
  - Fixed an issue with the webhook attachment button style [MM-62400](https://mattermost.atlassian.net/browse/MM-62400).
  - Mattermost v10.3.2 contains no database or functional changes.
- **10.3.1, released 2024-12-16**
  - Fixed an issue where user statuses weren't synced properly between servers [MM-61438](https://mattermost.atlassian.net/browse/MM-61438).
  - Fixed an accessibility problem in the new search input [MM-61234](https://mattermost.atlassian.net/browse/MM-61234).
  - Mattermost v10.3.1 contains no database or functional changes.
- **10.3.0, released 2024-12-16**
  - Original 10.3.0 release.

### Important Upgrade Notes

 - The Classic Mobile App has been phased out. Please download the new v2 Mobile App from the [Apple App Store](https://apps.apple.com/us/app/mattermost/id1257222717) or [Google Play Store](https://play.google.com/store/apps/details?id=com.mattermost.rn). See more details in the [classic mobile app deprecation](https://forum.mattermost.com/t/classic-mobile-app-deprecation/18703) Mattermost forum post.

### Compatibility

 - Updated minimum Edge and Chrome versions to 130+.

```{Important}
If you upgrade from a release earlier than v10.2, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Improvements

See [this walkthrough video](https://mattermost.com/video/mattermost-v10-3-changelog/) on some of the highlights and improvements in our latest release below.

#### User Interface (UI)
 - Pre-packaged Calls plugin [v1.3.0](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v1.3.0).
 - Downgraded Traditional Chinese language to Beta.
 - Added a feature to schedule a message at a future date (Professional and Enterprise plans).
 - Copilot plugin is now installed and enabled by default.
 - Added an option to test notifications.
 - Added a new search interface.
 - Updated product string for clarity.
 - Removed most places where deprecated translation code is used in the web app.
 - Removed some duplicate CSS from the web app bundle.

#### Administration
 - A 200 response is now returned for HEAD requests to a sub-path rather than responding with a 302. This fixes mobile devices trying to connect to a server hosted on a sub-path.
 - Added the ``fetchMissingUsers`` option to ``PostUtils.messageHtmlToComponent`` for use by plugins.
 - Added support for exporting and importing bot users via mmctl.
 - Added a warning to mmctl for cases where a user specifies a per-page parameter that's larger than the maximum value supported.

#### Performance
 - Added Desktop App performance metrics.

### Bug Fixes
 - Fixed an issue with post drafts being unnecessarily saved when changing channels.
 - Fixed an issue where the Web App would feel slower to load than the Desktop App.
 - Fixed an issue where new messages from new channels wouldn't appear in the sidebar after reconnecting the websocket.
 - Fixed an issue with a link in the Compliance Monitoring page banner in the System Console.
 - Fixed an issue that no longer allowed managing user tokens via the System Console.
 - Fixed a SVG image rendering issue by setting conditional width and height attributes in ``ImagePreview`` and ``SizeAwareImage`` components.
 - Fixed an issue with the web app status not being updated correctly for the current user.

### config.json
New setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
 - Under ``ServiceSettings `` in ``config.json``:
    - Added ``ScheduledPosts`` to enable the feature to schedule and send message in the future.

### Go Version
 - v10.3 is built with Go ``v1.22.6``.

### Open Source Components
 - Added ``opensearch-project/opensearch-go`` to https://github.com/mattermost/mattermost.

### Known Issues
 - The bottom padding is missing in the edit state of a scheduled messages [MM-61722](https://mattermost.atlassian.net/browse/MM-61722).
 - An incorrect count is displayed in channels for scheduled messages [MM-62197](https://mattermost.atlassian.net/browse/MM-62197).
 - The scheduled post channel indicator sometimes ends up in a bad state [MM-62222](https://mattermost.atlassian.net/browse/MM-62222).
 - Scheduled messages are not removed from queued list when sent while being disconnected [MM-62229](https://mattermost.atlassian.net/browse/MM-62229).
 - Scheduled message date displayed for Direct Message users is sometimes incorrect [MM-62244](https://mattermost.atlassian.net/browse/MM-62244).
 - The new search modal doesn't autocomplete after a space [MM-62199](https://mattermost.atlassian.net/browse/MM-62199).
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.

### Contributors
 - [7+7](https://translate.mattermost.com/user/7+7), [abdellani](https://github.com/abdellani), [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [akbarkz](https://translate.mattermost.com/user/akbarkz), [Alenoda](https://github.com/Alenoda), [amyblais](https://github.com/amyblais), [amynicol1985](https://github.com/amynicol1985), [and-ri](https://translate.mattermost.com/user/and-ri), [andr-sokolov](https://github.com/andr-sokolov), [andreabia](https://github.com/andreabia), [andrleite](https://github.com/andrleite), [angeloskyratzakos](https://github.com/angeloskyratzakos), [Aryakoste](https://github.com/Aryakoste), [asaadmahmood](https://github.com/asaadmahmood), [AulakhHarsh](https://github.com/AulakhHarsh), [ayusht2810](https://github.com/ayusht2810), [azadDsync](https://github.com/azadDsync), [BenCookie95](https://github.com/BenCookie95), [calebroseland](https://github.com/calebroseland), [callmeott](https://github.com/callmeott), [carlosGuimaraesTc](https://github.com/carlosGuimaraesTc), [catalintomai](https://github.com/catalintomai), [cedric.lamalle](https://translate.mattermost.com/user/cedric.lamalle), [creeper-0910](https://translate.mattermost.com/user/creeper-0910), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [cyberm8](https://github.com/cyberm8), [cyrusjc](https://github.com/cyrusjc), [decke](https://github.com/decke), [devinbinnie](https://github.com/devinbinnie), [Dishika18](https://github.com/Dishika18), [Dzenan](https://translate.mattermost.com/user/Dzenan), [edlerd](https://github.com/edlerd), [Eleferen](https://translate.mattermost.com/user/Eleferen), [enahum](https://github.com/enahum), [esarafianou](https://github.com/esarafianou), [frankps](https://translate.mattermost.com/user/frankps), [fsilye](https://github.com/fsilye), [gabsfrancis](https://translate.mattermost.com/user/gabsfrancis), [Gesare5](https://github.com/Gesare5), [guruprasath-v](https://github.com/guruprasath-v), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [HarshitVashisht11](https://github.com/HarshitVashisht11), [henrique](https://translate.mattermost.com/user/henrique), [hmhealey](https://github.com/hmhealey), [Honsei901](https://github.com/Honsei901), [hpflatorre](https://github.com/hpflatorre), [hun-a](https://github.com/hun-a), [ifoukarakis](https://github.com/ifoukarakis), [isacikgoz](https://github.com/isacikgoz), [Jelmerovereem](https://github.com/Jelmerovereem), [jespino](https://github.com/jespino), [jlandells](https://github.com/jlandells), [johnsonbrothers](https://github.com/johnsonbrothers), [jonathan-dove](https://github.com/jonathan-dove), [jprusch](https://github.com/jprusch), [JulienTant](https://github.com/JulienTant), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [kczpl](https://github.com/kczpl), [Killer2OP](https://github.com/Killer2OP), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [Kuruyia](https://github.com/Kuruyia), [KuSh](https://github.com/KuSh), [kyrillosisaac2](https://github.com/kyrillosisaac2), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo), [mas-who](https://github.com/mas-who), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [mentz](https://translate.mattermost.com/user/mentz), [minkyngkm](https://github.com/minkyngkm), [molejnik88](https://github.com/molejnik88), [morgancz](https://translate.mattermost.com/user/morgancz), [Morgansvk](https://github.com/Morgansvk), [mvitale1989](https://github.com/mvitale1989), [NadavTasher](https://github.com/NadavTasher), [nickmisasi](https://github.com/nickmisasi), [Niharika0104](https://github.com/Niharika0104), [nikolaiz](https://translate.mattermost.com/user/nikolaiz), [NilsArnlund](https://github.com/NilsArnlund), [potatogim](https://translate.mattermost.com/user/potatogim), [pranay-0512](https://github.com/pranay-0512), [pvev](https://github.com/pvev), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [rahimrahman](https://github.com/rahimrahman), [Rajat-Dabade](https://github.com/Rajat-Dabade), [Reinkard](https://github.com/Reinkard), [ricardogalvao](https://translate.mattermost.com/user/ricardogalvao), [RS-labhub](https://github.com/RS-labhub), [Rutam21](https://github.com/Rutam21), [s1Sharp](https://github.com/s1Sharp), [samarth29jc](https://github.com/samarth29jc), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [Seyifunmi](https://github.com/Seyifunmi), [Sharuru](https://github.com/Sharuru), [sohzm](https://github.com/sohzm), [sparr](https://github.com/sparr), [srisri332](https://github.com/srisri332), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [sumedhakoranga](https://github.com/sumedhakoranga), [TheInvincibleRalph](https://github.com/TheInvincibleRalph), [thelizardreborn](https://github.com/thelizardreborn), [theoforger](https://github.com/theoforger), [ThrRip](https://translate.mattermost.com/user/ThrRip), [tokipulan](https://translate.mattermost.com/user/tokipulan), [toninis](https://github.com/toninis), [verdel](https://github.com/verdel), [Victor-Nyagudi](https://github.com/Victor-Nyagudi), [vish9812](https://github.com/vish9812), [wetneb](https://github.com/wetneb), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [willypuzzle](https://github.com/willypuzzle), [yanyiyi](https://github.com/yanyiyi), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yesbhautik](https://github.com/yesbhautik)

(release-v10.2-feature-release)=
## Release v10.2 - [Feature Release](https://docs.mattermost.com/about/release-policy.html#release-types)

- **10.2.3, released 2025-01-22**
  - Mattermost v10.2.3 contains critical severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Boards plugin [v9.0.5](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.0.5).
  - Pre-packaged Channel Export plugin [v1.2.1](https://github.com/mattermost/mattermost-plugin-channel-export/releases/tag/v1.2.1).
  - Fixed a panic during LDAP synchronization [MM-61239](https://mattermost.atlassian.net/browse/MM-61239).
  - Fixed an issue where the bulk export retention job would accidentally delete non-bulk export files and directories [MM-60888](https://mattermost.atlassian.net/browse/MM-60888).
  - Mattermost v10.2.3 contains no database or functional changes.
- **10.2.2, released 2025-01-15**
  - Mattermost v10.2.2 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Boards plugin [v9.0.2](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.0.2).
  - Mattermost v10.2.2 contains no database or functional changes.
- **10.2.1, released 2024-12-10**
  - Mattermost v10.2.1 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where plugin settings got wiped if the plugin declared some of its fields as secrets [MM-61441](https://mattermost.atlassian.net/browse/MM-61441).
  - Pre-packaged Calls plugin [v1.3.2](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v1.3.2).
  - Mattermost v10.2.1 contains no database or functional changes.
- **10.2.0, released 2024-11-15**
  - Original 10.2.0 release.

### Important Upgrade Notes

 - Docker Content Trust (DCT) for signing Docker image artifacts has been replaced by Sigstore Cosign in v10.2 (November, 2024). If you rely on artifact verification using DCT, please [transition to using Cosign](https://edu.chainguard.dev/open-source/sigstore/cosign/how-to-install-cosign/). See the [DCT deprecation Mattermost forum post](https://forum.mattermost.com/t/upcoming-dct-deprecation/19275) for more details. 

```{Important}
If you upgrade from a release earlier than v10.0, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Improvements

See [this walkthrough video](https://mattermost.com/video/mattermost-v10-2-changelog/) on some of the highlights and improvements in our latest release below.

#### User Interface (UI)
 - Pre-packaged Calls plugin [v1.2.1](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v1.2.1).
 - Changed the logic of ``useMilitaryTime`` to ``false`` to default to 12-hour time format unless the user's preference from ``data.Value`` is ``true``. When a notification email is sent to a user, the time should now default to the 12-hour format unless otherwise stated by the user. 
 - A warning is now shown when deleting a post or comment from a remote/shared channel.
 - Bot messages will now properly mention both users when they happen on non-bot Direct Messages.
 - Updated the channel header to hide pinned posts when there aren't any in the channel.
 - Added full support for @mentions in the values of fields in message attachments.

#### Administration
 - Added a new URL parameter called ``permanent`` to ``DELETE /api/v4/posts/<post-id>``, and set ``permanent`` to ``true`` in order to permanently delete a post and its attachments.
 - Added Connected Workspaces (Beta) administration page to the System Console when Connected Workspaces are [enabled](https://docs.mattermost.com/onboard/connected-workspaces.html#enable-connected-workflows) for the server.
 - Added a team selector to accept connection invite flow in Connected Workspaces.
 - Restricted activation and deactivation of LDAP-managed users through both the System Console UI and Mattermost API.
 - Export/import improvements: added the ability to export all user preferences and flagged posts.
 - Increased timeouts to fetch cluster logs.
 - Improved log messages for cluster communication.
 - Information about deleted rows from the Data Retention job are now logged.
 - License details to logs are now emitted when added or removed.
 - Added a new mmctl command, ``mmctl post delete <post-id>``, in order to permanently delete a post and its attachments.

#### Performance
 - Added metrics to prometheus to check the mobile versions for each session daily.
 - Improved the performance of LDAP sync jobs when group-contained teams and channels are used.
 - Added minor improvements to notification metrics.
 - Added minor improvements to mobile push notifications.

### Bug Fixes
 - Fixed an issue with email notifications using 24-hour timestamps by default.
 - Fixed an issue where bots were not ignored when counting deactivated accounts for statistics.
 - Fixed an issue where drafts didn’t allow scrolling if the user had many drafts.
 - Fixed an issue that caused Javascript errors in the System Console.
 - Fixed racy use of session in ``NewWebConn``.
 - Fixed a race condition that would happen after a server start if ``EnableTesting`` was enabled.
 - Fixed an issue where no error message was shown when replying to a deleted post from the draft screen.
 - Fixed an issue where the check icons were missing from the Sort and Show options in the Direct Messages tab, and the Sort tab of the Channels tab.
 - Fixed desyncing issues with unreads between the team sidebar and the title bar.
 - Fixed an issue with message export file attachments with dedicated filestore: when the dedicated filestore is set, file attachments will be found and exported correctly.
 - Reverted a change enforcing usernames to start with alpha characters on the server.
 - Reverted a breaking change in ``registerSlashCommandWillBePostedHook`` that caused errors to surface in case an expected empty object was returned.

### config.json
New setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
 - Under ``ServiceSettings`` in ``config.json``:
    - Added a new configuration setting ``EnableAPIPostDeletion`` in order to enable/disable post deletion. This configuration setting does not need to be enabled when running mmctl in local mode.
    - Added ``EnableDesktopLandingPage`` to allow the desktop app landing page to be disabled.
 - Under ``NativeAppSettings`` in ``config.json``:
     - Added a configuration setting ``MobileExternalBrowser`` that tells the Mobile app to perform SSO Authentication using the external default browser.

### Go Version
 - v10.2 is built with Go ``v1.22.6``.

### Known Issues
 - The scrollbar is not clickable when there is a "Jump to recents" toaster [MM-61526](https://mattermost.atlassian.net/browse/MM-61526).
 - Shared Channels: Direct Messages are not supported.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.

### Contributors
 - [047pegasus](https://github.com/047pegasus), [1510janu](https://github.com/1510janu), [aamfahim](https://github.com/aamfahim), [aditipatelpro](https://github.com/aditipatelpro), [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [amyblais](https://github.com/amyblais), [andreabia](https://translate.mattermost.com/user/andreabia), [andrleite](https://github.com/andrleite), [angeloskyratzakos](https://github.com/angeloskyratzakos), [anudhyan](https://github.com/anudhyan), [Arch130](https://github.com/Arch130), [arilloid](https://github.com/arilloid), [Aryakoste](https://github.com/Aryakoste), [asaadmahmood](https://github.com/asaadmahmood), [azadDsync](https://github.com/azadDsync), [azigler](https://github.com/azigler), [belkhoujaons](https://github.com/belkhoujaons), [BenCookie95](https://github.com/BenCookie95), [calebroseland](https://github.com/calebroseland), [Camillarhi](https://github.com/Camillarhi), [CarlssonFilip](https://github.com/CarlssonFilip), [catalintomai](https://github.com/catalintomai), [CBID2](https://github.com/CBID2), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [danielsischy](https://github.com/danielsischy), [devinbinnie](https://github.com/devinbinnie), [DHaussermann](https://github.com/DHaussermann), [diamant3](https://github.com/diamant3), [Dishika18](https://github.com/Dishika18), [Eleferen](https://translate.mattermost.com/user/Eleferen), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [enzowritescode](https://github.com/enzowritescode), [esarafianou](https://github.com/esarafianou), [esethna](https://github.com/esethna), [fmartingr](https://github.com/fmartingr), [frankps](https://translate.mattermost.com/user/frankps), [fsilye](https://github.com/fsilye), [fume4mattermost](https://github.com/fume4mattermost), [gabrieljackson](https://github.com/gabrieljackson), [Gesare5](https://github.com/Gesare5), [Good-Soma](https://github.com/Good-Soma), [grubbins](https://github.com/grubbins), [gvarma28](https://github.com/gvarma28), [hamzawritescode](https://github.com/hamzawritescode), [hannaparks](https://github.com/hannaparks), [hanzei](https://github.com/hanzei), [HarshitVashisht11](https://github.com/HarshitVashisht11), [hereje](https://github.com/hereje), [hmhealey](https://github.com/hmhealey), [ifoukarakis](https://github.com/ifoukarakis), [isacikgoz](https://github.com/isacikgoz), [ja49619](https://translate.mattermost.com/user/ja49619), [jespino](https://github.com/jespino), [jlandells](https://github.com/jlandells), [johnsonbrothers](https://github.com/johnsonbrothers), [jopaleti](https://github.com/jopaleti), [jprusch](https://github.com/jprusch), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [Killer2OP](https://github.com/Killer2OP), [kom-senapati](https://github.com/kom-senapati), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [KuSh](https://github.com/KuSh), [KvngMikey](https://github.com/KvngMikey), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo), [Malay-dev](https://github.com/Malay-dev), [master7](https://translate.mattermost.com/user/master7), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [mgdelacroix](https://github.com/mgdelacroix), [mm-prodsec-bot](https://github.com/mm-prodsec-bot), [moda-l10n](https://translate.mattermost.com/user/moda-l10n), [Morgan_svk](https://translate.mattermost.com/user/Morgan_svk), [Movion](https://github.com/Movion), [mvitale1989](https://github.com/mvitale1989), [nickmisasi](https://github.com/nickmisasi), [Niharika0104](https://github.com/Niharika0104), [nikolaiz](https://translate.mattermost.com/user/nikolaiz), [NilsArnlund](https://github.com/NilsArnlund), [panoramix360](https://github.com/panoramix360), [pradeepmurugesan](https://github.com/pradeepmurugesan), [pvev](https://github.com/pvev), [qfrigolac](https://github.com/qfrigolac), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [rahimrahman](https://github.com/rahimrahman), [Rajat-Dabade](https://github.com/Rajat-Dabade), [Ranjana761](https://github.com/Ranjana761), [raremax](https://translate.mattermost.com/user/raremax), [Reinkard](https://github.com/Reinkard), [RS-labhub](https://github.com/RS-labhub), [Ruhi14](https://github.com/Ruhi14), [Rutam21](https://github.com/Rutam21), [s4kh](https://github.com/s4kh), [sahariardev](https://github.com/sahariardev), [samarth29jc](https://github.com/samarth29jc), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [sedivst](https://translate.mattermost.com/user/sedivst), [Sharuru](https://translate.mattermost.com/user/Sharuru), [shraddha761](https://github.com/shraddha761), [space-w-alker](https://github.com/space-w-alker), [srisri332](https://github.com/srisri332), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [svelle](https://github.com/svelle), [swills](https://github.com/swills), [tanmaythole](https://github.com/tanmaythole), [TealWater](https://github.com/TealWater), [TheInvincibleRalph](https://github.com/TheInvincibleRalph), [theoforger](https://github.com/theoforger), [ThrRip](https://github.com/ThrRip), [TomerPacific](https://github.com/TomerPacific), [toninis](https://github.com/toninis), [varghesejose2020](https://github.com/varghesejose2020), [vawaver](https://translate.mattermost.com/user/vawaver), [vhaska](https://translate.mattermost.com/user/vhaska), [Victor-Nyagudi](https://github.com/Victor-Nyagudi), [vish9812](https://github.com/vish9812), [WeBjAnJaN](https://translate.mattermost.com/user/WeBjAnJaN), [wetneb](https://github.com/wetneb), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [yanyiyi](https://github.com/yanyiyi), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [z44440000z](https://github.com/z44440000z), [ZubairImtiaz3](https://github.com/ZubairImtiaz3)

(release-v10.1-feature-release)=
## Release v10.1 - [Feature Release](https://docs.mattermost.com/about/release-policy.html#release-types)

- **10.1.7, released 2025-01-15**
  - Mattermost v10.1.7 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Boards plugin [v9.0.2](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.0.2).
  - Mattermost v10.1.7 contains no database or functional changes.
- **10.1.6, released 2024-12-20**
  - Fixed an issue by restoring System Administrator access to Direct and Group Messages without being a member.
  - Mattermost v10.1.6 contains no database or functional changes.
- **10.1.5, released 2024-12-18**
  - Fixed an issue where System Administrators could not pull posts in from Direct Message channels they were not in [MM-62092](https://mattermost.atlassian.net/browse/MM-62092).
  - Mattermost v10.1.5 contains no database or functional changes.
- **10.1.4, released 2024-12-10**
  - Mattermost v10.1.4 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Calls plugin [v1.3.2](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v1.3.2).
  - Mattermost v10.1.4 contains no database or functional changes.
- **10.1.3, released 2024-11-14**
  - Mattermost v10.1.3 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Reverted a change enforcing usernames to start with alpha characters on the server [MM-61143](https://mattermost.atlassian.net/browse/MM-61143).
  - Reverted a breaking change in ``registerSlashCommandWillBePostedHook`` that caused errors to surface in case an expected empty object was returned [MM-61233](https://mattermost.atlassian.net/browse/MM-61233).
  - Mattermost v10.1.3 contains no database or functional changes.
- **10.1.2, released 2024-10-28**
  - Mattermost v10.1.2 contains a high severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue with message export file attachments with a dedicated filestore [MM-60063](https://mattermost.atlassian.net/browse/MM-60063).
  - Mattermost v10.1.2 contains the following functional change:
      - Added a configuration setting **NativeAppSettings > MobileExternalBrowser** that tells the Mobile app to perform SSO Authentication using the external default browser [MM-60332](https://mattermost.atlassian.net/browse/MM-60332).
- **10.1.1, released 2024-10-16**
  - Fixed an issue where a shared indicator was shown in all Direct Messages, regardless of the user coming from a shared server [MM-60744](https://mattermost.atlassian.net/browse/MM-60744).
  - Mattermost v10.1.1 contains no database or functional changes.
- **10.1.0, released 2024-10-16**
  - Original 10.1.0 release.

```{Important}
If you upgrade from a release earlier than v10.0, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Improvements

#### User Interface (UI)
 - Added Metrics plugin to the prepackaged plugins, [v0.5.3](https://github.com/mattermost/mattermost-plugin-metrics/releases/tag/v0.5.3).
 - Pre-packaged Calls plugin [v1.1.0](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v1.1.0).
 - Enabled Channel Bookmarks, added re-ordering, and fixed URL validity checking.
 - Added a more descriptive error message, "Uploaded plugin size exceeds limit." for plugin uploads that are too large.
 - Added channel specific message notification sounds configuration.

#### Administration
 - Added ``DeleteAt`` field for ``SharedChannelRemotes`` and ``RemoteClusters``.
 - Added support for sending channel invites to offline remotes in Shared Channels.
 - Changed server-side logic to return a ``413: Request Entity Too Large`` HTTP status code for a plugin upload that is too large.
 - Direct and Group Message unread/read state over export and import will now be carried over.
 - CRT memberships are now importable for import.
 - CRT memberships are now exportable for bulk export.
 - Added ``--local mode`` support in MMCTL to handle user preferences.
 - Plugins are now allowed to mark setting fields as secret, obfuscating them in the System Console and the Support Packet.

#### Performance
 - Improved metrics related to push proxy errors.
 - Improved metrics around notifications.

### Bug Fixes
 - Fixed an issue where threads would be marked as read if they were open in the background.
 - Fixed an issue where Direct and Group Messages didn't load correctly in the sidebar when refreshing the app from Drafts.
 - Fixed an issue attempting to bind to Apps plugin when the plugin was not enabled.
 - Fixed an issue where the Unreads tab would not update correctly after the websocket reconnected.
 - Fixed an issue with focusing on the main box when loading the app.
 - Fixed an issue where Team and Channel Admins could lose the ability to create posts in a moderated channel.
 - Fixed an issue where marking a channel as unread did not show immediately in other clients.
 - Fixed an issue with not allowing to use ``@`` and ``~`` in the ``in:`` search modifier without affecting search results.
 - Fixed an issue with YouTube previews no longer being displayed.

### config.json
New setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
 - Under ``ExperimentalSettings`` in ``config.json``:
    - Added ``YoutubeReferrerPolicy`` to fix an issue where YouTube previews showed an “Video Unavailable” error instead of the video.

#### Changes to the Enterprise plan:
 - Under ``ConnectedWorkspacesSettings`` in ``config.json``:
    - Added ``DisableSharedChannelsStatusSync`` to add status sync support to Shared Channels.
 - Under ``ConnectedWorkspacesSettings`` in ``config.json``:
    - Moved the Shared Channel related configuration properties out of the Experimental section.
    - Added the ``MaxPostsPerSync`` configuration property.

### API Changes
 - Added new API endpoints to manage shared channels.
 - Added proper response to ``/api/v4/client_perf`` endpoint.

### Go Version
 - v10.1 is built with Go ``v1.22.6``.

### Known Issues
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.

### Contributors
 - [adityasoni2019](https://github.com/adityasoni2019), [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [algeorgiadis](https://github.com/algeorgiadis), [amyblais](https://github.com/amyblais), [andreabia](https://translate.mattermost.com/user/andreabia), [andrleite](https://github.com/andrleite), [angeloskyratzakos](https://github.com/angeloskyratzakos), [armmanvaillancourt](https://github.com/armmanvaillancourt), [Aryakoste](https://github.com/Aryakoste), [ayusht2810](https://github.com/ayusht2810), [azistellar](https://translate.mattermost.com/user/azistellar), [azizthegit](https://github.com/azizthegit), [BenCookie95](https://github.com/BenCookie95), [calebroseland](https://github.com/calebroseland), [catalintomai](https://github.com/catalintomai), [ChinoUkaegbu](https://github.com/ChinoUkaegbu), [Chlbek](https://translate.mattermost.com/user/Chlbek), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [danielsischy](https://github.com/danielsischy), [daveseo901](https://github.com/daveseo901), [devinbinnie](https://github.com/devinbinnie), [DHaussermann](https://github.com/DHaussermann), [Eleferen](https://translate.mattermost.com/user/Eleferen), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [enzowritescode](https://github.com/enzowritescode), [esarafianou](https://github.com/esarafianou), [esethna](https://github.com/esethna), [fmartingr](https://github.com/fmartingr), [frankps](https://translate.mattermost.com/user/frankps), [fsilye](https://github.com/fsilye), [gabrieljackson](https://github.com/gabrieljackson), [Gesare5](https://github.com/Gesare5), [Glandos](https://github.com/Glandos), [grundleborg](https://github.com/grundleborg), [gvarma28](https://github.com/gvarma28), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hereje](https://github.com/hereje), [hmhealey](https://github.com/hmhealey), [ifoukarakis](https://github.com/ifoukarakis), [isacikgoz](https://github.com/isacikgoz), [ja49619](https://translate.mattermost.com/user/ja49619), [johnsonbrothers](https://github.com/johnsonbrothers), [jones](https://translate.mattermost.com/user/jones), [jprusch](https://github.com/jprusch), [JulienTant](https://github.com/JulienTant), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kaoski](https://github.com/kaoski), [kayazeren](https://github.com/kayazeren), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [L3o-pold](https://github.com/L3o-pold), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lukasMega](https://github.com/lukasMega), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo), [manujgrover71](https://github.com/manujgrover71), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [mgdelacroix](https://github.com/mgdelacroix), [milotype](https://translate.mattermost.com/user/milotype), [Morgan_svk](https://translate.mattermost.com/user/Morgan_svk), [Movion](https://github.com/Movion), [mvitale1989](https://github.com/mvitale1989), [nekodayo2222](https://translate.mattermost.com/user/nekodayo2222), [nickmisasi](https://github.com/nickmisasi), [nikhilskul7](https://github.com/nikhilskul7), [Porma120](https://github.com/Porma120), [pvev](https://github.com/pvev), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [rahimrahman](https://github.com/rahimrahman), [Rajat-Dabade](https://github.com/Rajat-Dabade), [Rishiii7](https://github.com/Rishiii7), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [Sharuru](https://github.com/Sharuru), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [testtomato1230](https://translate.mattermost.com/user/testtomato1230), [TheInvincibleRalph](https://github.com/TheInvincibleRalph), [ThrRip](https://translate.mattermost.com/user/ThrRip), [toninis](https://github.com/toninis), [tsabi](https://github.com/tsabi), [vish9812](https://github.com/vish9812), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yaz](https://translate.mattermost.com/user/yaz), [yuney-worx4you](https://github.com/yuney-worx4you)

(release-v10.0-major-release)=
## Release v10.0 - [Major Release](https://docs.mattermost.com/about/release-policy.html#release-types)

- **10.0.4, released 2024-12-10**
  - Mattermost v10.0.4 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Calls plugin [v1.3.2](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v1.3.2).
  - Mattermost v10.0.4 contains no database or functional changes.
- **10.0.3, released 2024-11-14**
  - Mattermost v10.0.3 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v10.0.3 contains no database or functional changes.
- **10.0.2, released 2024-10-28**
  - Mattermost v10.0.2 contains a high severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Reverted a change enforcing usernames to start with alpha characters on the server [MM-61143](https://mattermost.atlassian.net/browse/MM-61143).
  - Reverted a breaking change in ``registerSlashCommandWillBePostedHook`` that caused errors to surface in case an expected empty object was returned [MM-61233](https://mattermost.atlassian.net/browse/MM-61233).
  - Mattermost v10.0.2 contains no database or functional changes.
- **10.0.1, released 2024-10-10**
  - Mattermost v10.0.1 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue enabling Professional customers and Team Edition users to upgrade to Playbooks v2 via the in-product marketplace, which fails to start without an Enterprise License. Additional details and discussion can be found on the [forums here](https://forum.mattermost.com/t/clarification-on-playbooks-in-mattermost-v10/20563) [MM-60679](https://mattermost.atlassian.net/browse/MM-60679).
  - Mattermost v10.0.1 contains no database or functional changes.
- **10.0.0, released 2024-09-16**
  - Original 10.0.0 release.

### Important Upgrade Notes
 - We no longer support new installations using MySQL starting in v10. All new customers and/or deployments will only be supported with the minimum supported version of the PostgreSQL database. End of support for MySQL is targeted for Mattermost v11.
 - Apps Framework is deprecated for new installs. Please extend Mattermost using webhooks, slash commands, OAuth2 apps, and plugins.
 - Mattermost v10 introduces Playbooks v2 for all Enterprise licensed customers. Professional SKU customers may continue to use Playbooks v1 uninterrupted which will be maintained and supported until September 2025, followed by an appropriate grandfathering strategy. More detailed information and the discussion are available on the [Mattermost discussion forum](https://forum.mattermost.com/t/clarification-on-playbooks-in-mattermost-v10/20563).
 - Renamed ``Channel Moderation`` to ``Advanced Access Control`` in the channel management section in the **System Console**.
 - Renamed announcement banner feature to “system-wide notifications”.
 - Renamed “Collapsed Reply Threads” to “Threaded Discussions” in the System Console.
 - Renamed “System Roles” to “Delegated Granular Administration” in the System Console.
 - Renamed "Office 365" to "Entra ID" for SSO logins.
 - Fully deprecated the ``/api/v4/image`` endpoint when the image proxy is disabled.
 - Pre-packaged Calls plugin [v1.0.1](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v1.0.1). This includes breaking changes including removal of group calls from unlicensed servers in order to focus supportability and quality on licensed servers. Unlicensed servers can continue to use Calls in direct message channels, which represent the majority of activity.
 - Removed deprecated ``Config.ProductSettings``, ``LdapSettings.Trace``, and ``AdvancedLoggingConfig`` configuration fields.
 - Removed deprecated ``pageSize`` query parameter from most API endpoints.
 - Deprecated the experimental Strict CSRF token enforcement. This feature will be fully removed in Mattermost v11.

```{Important}
If you upgrade from a release earlier than v9.11, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Highlights

See [this walkthrough video](https://mattermost.com/video/mattermost-v10-0-changelog/) on some of the highlights and improvements in our latest release below.

#### Mattermost Microsoft Teams Plugin
 - Pre-packaged the Microsoft Teams plugin for Mattermost, [v2.0.3](https://github.com/mattermost/mattermost-plugin-msteams/releases/tag/v2.0.3).

#### Mattermost Microsoft Calendar and Microsoft Teams Meetings Plugins
 - Pre-packaged Microsoft Calendar [v1.3.4](https://github.com/mattermost/mattermost-plugin-mscalendar/releases/tag/v1.3.4) and Microsoft Teams Meetings [v2.2.0](https://github.com/mattermost-community/mattermost-plugin-msteams-meetings/releases/tag/v2.2.0) plugins.

#### Mattermost Copilot GA
 - Pre-packaged Mattermost Copilot plugin version [v1.0.0](https://github.com/mattermost/mattermost-plugin-ai/releases/tag/v1.0.0).

### Improvements

#### User Interface (UI)
 - Pre-packaged Calls plugin [v1.0.1](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v1.0.1).
 - Added Playbooks [v2.0.1](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v2.0.1) to the prepackaged plugins.
 - Added Mattermost user survey plugin to pre-packaged plugins, [v1.1.1](https://github.com/mattermost/mattermost-plugin-user-survey/releases).
 - Changed the right-hand side scroll direction and fixed the advanced text editor to the bottom.
 - Added Do not disturb and late timezone warnings to Direct Message posts.
 - Added user statuses to the Group Members modal.
 - Added labels for channel header and purpose in the right-hand side channel info view.
 - Added pagination user interface to the ``BackstageList`` component.
 - Made various improvements to code involving user preferences.
 - Promoted GIF picker, custom groups and message priority out of Beta.
 - Removed the **Pre-release features** section from **Settings > Advanced** due to lack of usage.

#### Administration
 - Made payload size limit error more clearly visible and recognisable in API responses and server error logs.
 - Extended the plugin schema to support defining sections for **System Console** settings.
 - Added support for a default team on secure connections for incoming channel invites.
 - Remote clusters can now be created without explicitly providing a password.
 - Files are now fetched from all nodes in a cluster when generating a Support Packet.
 - Docker images are now based on Ubuntu Noble.

#### Performance
 - Removed a re-render on channel change.
 - Batched requests made by certain components for loading users and their statuses from the server.
 - Cleaned up some unused post handling logic.

### Bug Fixes
 - Fixed an issue with web app notifications not being shown in the **Notification Center** on Windows or Mac.
 - Fixed an issue with ``mmctl webhooks list`` to paginate past 200 results.
 - Fixed an issue where scrolling capability and a visible scrollbar were missing in post textboxes.
 - Fixed an issue where false warnings about Channel indexes being incorrect were sent to system admins.
 - Fixed an issue where indexing would always be done async even after setting ``LiveIndexingBatchSize`` to ``1``. Now we respect the config and index synchronously if the value is set to ``1``.
 - Fixed an issue where the **Edit Post Time Limit** button was not being displayed in the System Console.
 - Fixed another issue where users would not see channels they were added to/messages from those channels in clustered environments.

### config.json
New setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
 - Under ``ServiceSettings`` in ``config.json``:
    - Added a new setting ``MaximumURLLength`` to remove the hardcoded URL length limit.
 - Removed deprecated ``Config.ProductSettings``.
 - Removed ``EnablePreviewFeatures`` setting.

#### Changes to the Enterprise plan:
 - Removed deprecated ``LdapSettings.Trace`` setting.
 - Removed deprecated ``AdvancedLoggingConfig`` setting.

### API Changes
 - Reduced the number of API requests made to fetch user information for Group Messages on page load.
 - User APIs now enforce username beginning with alphabetic character, matching client-side validation.
 - Added a new request parameter ``include_total_count`` to API endpoint ``GET /api/v4/hooks/incoming``.

### Go Version
 - v10.0 is built with Go ``v1.21.8``.

### Open Source Components
 - Added ``redis/rueidis`` to https://github.com/mattermost/mattermost.

### Known Issues
 - The cursor is not placed in the "Write to" field on login [MM-60275](https://mattermost.atlassian.net/browse/MM-60275).
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.

### Contributors
 - [abhijit-singh](https://github.com/abhijit-singh), [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [alexcekay](https://github.com/alexcekay), [amyblais](https://github.com/amyblais), [andreabia](https://github.com/andreabia), [andrleite](https://github.com/andrleite), [angeloskyratzakos](https://github.com/angeloskyratzakos), [Aryakoste](https://github.com/Aryakoste), [asaadmahmood](https://github.com/asaadmahmood), [AshishDhama](https://github.com/AshishDhama), [axu-trex](https://github.com/axu-trex), [ayusht2810](https://github.com/ayusht2810), [azigler](https://github.com/azigler), [BenCookie95](https://github.com/BenCookie95), [Boruus](https://github.com/Boruus), [BrandonS09](https://github.com/BrandonS09), [bruno-keiko](https://github.com/bruno-keiko), [Camillarhi](https://github.com/Camillarhi), [catalintomai](https://github.com/catalintomai), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [danielsischy](https://github.com/danielsischy), [DemoYeti](https://github.com/DemoYeti), [devinbinnie](https://github.com/devinbinnie), [DHaussermann](https://github.com/DHaussermann), [Eleferen](https://translate.mattermost.com/user/Eleferen), [elewis787](https://github.com/elewis787), [enahum](https://github.com/enahum), [enzowritescode](https://github.com/enzowritescode), [esethna](https://github.com/esethna), [ezekielchow](https://github.com/ezekielchow), [fmartingr](https://github.com/fmartingr), [frankps](https://translate.mattermost.com/user/frankps), [gabrieljackson](https://github.com/gabrieljackson), [Gesare5](https://github.com/Gesare5), [gvarma28](https://github.com/gvarma28), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hereje](https://github.com/hereje), [hmhealey](https://github.com/hmhealey), [ifoukarakis](https://github.com/ifoukarakis), [imanmagomedov.said](https://translate.mattermost.com/user/imanmagomedov.said), [isacikgoz](https://github.com/isacikgoz), [ja49619](https://translate.mattermost.com/user/ja49619), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [johnsonbrothers](https://github.com/johnsonbrothers), [jprusch](https://translate.mattermost.com/user/jprusch), [JulienTant](https://github.com/JulienTant), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [KvngMikey](https://github.com/KvngMikey), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo), [marianunez](https://github.com/marianunez), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [MattSilvaa](https://github.com/MattSilvaa), [mgdelacroix](https://github.com/mgdelacroix), [movion](https://github.com/movion), [mvitale1989](https://github.com/mvitale1989), [NCPSNetworks](https://translate.mattermost.com/user/NCPSNetworks), [nickmisasi](https://github.com/nickmisasi), [ovrheat](https://github.com/ovrheat), [petersauvignon](https://translate.mattermost.com/user/petersauvignon), [phoinixgrr](https://github.com/phoinixgrr), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [rahimrahman](https://github.com/rahimrahman), [Rajat-Dabade](https://github.com/Rajat-Dabade), [RS-labhub](https://github.com/RS-labhub), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [sblaisot](https://github.com/sblaisot), [Sn-Kinos](https://github.com/Sn-Kinos), [spirosoik](https://github.com/spirosoik), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [tasnim0tantawi](https://github.com/tasnim0tantawi), [TealWater](https://github.com/TealWater), [theaino](https://github.com/theaino), [ThrRip](https://translate.mattermost.com/user/ThrRip), [Tihomir-N](https://github.com/Tihomir-N), [tnir](https://translate.mattermost.com/user/tnir), [toninis](https://github.com/toninis), [vish9812](https://github.com/vish9812), [wiggin77](https://github.com/wiggin77), [willypuzzle](https://github.com/willypuzzle), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yomiadetutu1](https://github.com/yomiadetutu1), [ZubairImtiaz3](https://github.com/ZubairImtiaz3)
