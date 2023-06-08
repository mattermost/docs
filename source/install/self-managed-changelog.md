# Mattermost self-hosted changelog

[Mattermost](https://mattermost.com) is an open source platform for secure collaboration across the entire software development lifecycle. This changelog summarizes updates for the latest self-hosted versions of Mattermost to be [deployed and upgraded on infrastructure you control](https://docs.mattermost.com/guides/deployment.html).

See the [changelog in progress](https://bit.ly/2nK3cVf) for the upcoming release. See the [Legacy Self-Hosted Mattermost Changelog](legacy-self-hosted-changelog) for details on all Mattermost self-hosted releases prior to v7.1.

Latest Mattermost Releases:

- [Release v8.0 - Major Release](#release-v8-0-major-release)
- [Release v7.11 - Feature Release](#release-v7-11-feature-release)
- [Release v7.10 - Feature Release](#release-v7-10-feature-release)
- [Release v7.9 - Feature Release](#release-v7-9-feature-release)
- [Release v7.8 - Extended Support Release](#release-v7-8-extended-support-release)

## Release v8.0 - [Major Release](https://docs.mattermost.com/upgrade/release-definitions.html#major-release)

**Release Day: July 14, 2023**

### Important Upgrade Notes

 - In v8.0, the following repositories are merged into one: ``mattermost-server``, ``mattermost-webapp``, and ``mattermost-plugin-playbooks``. Developers should read the updated [Developer Guide](https://developers.mattermost.com/contribute/developer-setup/) for details.
 - Fixed an issue caused by a migration in the previous release. Query takes around 11ms on a PostgreSQL 14 DB t3.medium RDS instance. Locks on the preferences table will only be acquired if there are rows to delete, but the time taken is negligible.
 - Removed the deprecated ``model.CommandArgs.Session``.
 - Fixed an issue where a user would still see threads in the threads view of channels they have left. Migration execution time in MySQL: Query OK, 2766769 rows affected (4 min 47.57 sec). Migration execution time in PostgreSQL: Execution time: 58.11 sec, DELETE 2766690.
 - For servers wanting to allow websockets to connect from other origins, please set the ``ServiceSettings.AllowCorsFrom`` config setting.
 - The file info stats query is now optimized by denormalizing the ``channelID`` column into the table itself. This will speed up the query to get the file count for a channel when selecting the right-hand pane. Migration times:

   - On a MySQL 8.0.31 DB with 1405 rows in FileInfo and 11M posts, it took around 0.3s
   - On a PostgreSQL 12.14 DB with 1731 rows in FileInfo and 11M posts, it took around 0.27s

**IMPORTANT:** If you upgrade from a release earlier than v7.10, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).

### Highlights

#### Persistent Notifications
 - Added a persistent notification option when sending urgent priority posts.

### Improvements

#### User Interface (UI)
 - Added a **Mattermost Marketplace** option to the bottom of the apps bar. The option is visible when the Marketplace is enabled, and the user has ``SYSCONSOLE_WRITE_PLUGINS`` permissions.
 - Added an **Add channels** button to the bottom of the left-hand sidebar to make the action more obvious for users who want to create or join channels.
 - Removed the Webapp Build Hash from **Main Menu > About Mattermost** since it is now identical to Server Build Hash.
 - Replaced the ``compass-components`` icon component with ``compass-icons``.
 - Added “hours ahead” timezone details to the user profile popover.
 - Added an experimental feature to disable re-fetching of channel and channel members on browser focus.
 - Bot users are now hidden in the user selector in apps forms.
 - Removed the fetching of archived channels on page load.
 - The **Channel Type** dropdown within the **Browse Channels** modal can now be focused.
 - Removed in-app help pages that were no longer accessible.
 - Removed system join/leave messages from thread replies and post them instead in the main channel.
 - Added an experimental setting to make the channel autocomplete only appear after typing two characters instead of immediately after the tilde (~).
 - Users with default profile pictures will now regenerate a new picture when their username is changed.
 - Implemented URL auto generation on channel creation for when there's no URL safe characters on its name.
 - Added a new option to auto-follow all threads in the channel **Notification Preference** settings.
 - ``CTRL/CMD + K`` shortcut can now be used to insert link formatting when text is selected.
 - ``pas`` and ``pascal`` code blocks are now higlighted.
 - Language setting in Boards was removed. The main language setting under **Settings -> Display Settings** now covers Boards. Boards previously supported Catalan, Greek, Indonesian, and Occitan, but since these 4 languages were only partially translated (<40%; Boards-only), they have been removed until more areas of Mattermost are translated into these languages.
 - Removed websocket state effects for the collapse/expand state of categories.
 - Pre-packaged Calls version 0.16.1.
 - Pre-packaged Jira plugin version 3.2.5.
 - Pre-packaged GitHub plugin version 2.1.6.
 - Pre-packaged Autolink plugin version 1.4.0.
 - Pre-packaged Welcomebot plugin version 1.3.0.

#### Administration
 - Self-hosted admins can now define a separate shipping address during in-product license purchase.
 - Added updates to the trial request forms to allow for a more tailored trial experience.
 - First admins will now have an onboarding experience that includes first team creation based on company name and invite members link steps. 
 - Adds the ability to expand seats in-product for self-hosted servers.
 - Added a new section in the **System Console > Products** for Boards.
 - Added the ability to search a partial first name, last name, nickname, or username on the **System Console > Users** page.
 - **Contact Support** now redirects users to Zendesk and pre-fills known information.
 - Added a mechanism for public routes on products and used it to support publicly shared Board links.
 - The database section in the **System Console** now has an additional read-only section which shows the active search backend in use. This can be helpful to confirm which search engine is currently active when there are multiple configured.
 - Updated Docker Base Image from Debian to Ubuntu 22.04 LTS.
 -  - The Go module has been upgraded to v8.0. All packages are now under the new path ``github.com/mattermost-server/server/v8``.
 - Type-generated settings will now be generated (only for future generations) with a URL-safe version of base64 encoding.
 - Mattermost is now resilient against database replica outages and will dynamically choose a replica if it's alive. Also a config parameter ``ReplicaMonitorIntervalSeconds`` was added and the default value is 5. This controls how frequently unhealthy replicas will be monitored for liveness check.
 - Removed ``ExperimentalSettings.PatchPluginsReactDOM``.
 - Removed deprecated ``PermissionUseSlashCommands``.
 - Added support for attachments when importing/exporting Boards.
 - Updated Docker Base Image from Debian to Ubuntu 22.04 LTS.
 - Removed support for PostgreSQL v10. The new minimum PostgreSQL version is now v11.
 - The Mattermost public API for Go is now available as a distinctly versioned package. Instead of pinning a particular commit hash, use idiomatic Go to add this package as a dependency: go get github.com/mattermost/mattermost-server/server/public. This relocated Go API maintains backwards compatibility with Mattermost v7. Furthermore, the existing Go API previously at github.com/mattermost/mattermost-server/v6/model remains forward compatible with Mattermost v8, but may not contain newer features. Plugins do not need to be recompiled, but developers may opt in to using the new package to simplify their build process. The new public package is shipping alongside Mattermost v8 as version 0.5.0 to allow for some additional code refactoring before releasing as v1 later this year.
 - Three configuration fields have been added, ``LogSettings.AdvancedLoggingJSON``, ``ExperimentalAuditSettings.AdvancedLoggingJSON``, and ``NotificationLogSettings.AdvancedLoggingJSON`` which support multi-line JSON, escaped JSON as a string, or a filename that points to a file containing JSON.  The ``AdvancedLoggingConfig`` fields have been deprecated.
 - The Go MySQL driver has changed the ``maxAllowedPacket`` size from 4MiB to 64MiB. This is to make it consistent with the change in the server side default value from MySQL 5.7 to MySQL 8.0. If your ``max_allowed_packet`` setting is not 64MiB, then please update the MySQL config DSN with an additional param of ``maxAllowedPacket`` to match with the server side value. Alternatively, a value of 0 can be set to to automatically fetch the server side value, on every new connection, which has a performance overhead.
 - For servers wanting to allow websockets to connect from other origins, please set the ``ServiceSettings.AllowCorsFrom`` config setting.
 
#### Performance
 - Improved the performance of webapp related to timezone calculations.
 - Improved performance of code used for post list screen reader support.

### API Changes
 - An underscore is now used in the timeline API (``event-id`` -> ``event_id``) for consistency with other API arguments.

### Bug Fixes
 - Fixed a scrolling issue in the purchase modals.
 - Fixed an issue where the **Delete Category Dialog** message was not visible in Boards.
 - Fixed an issue where the experimental Shared Channels feature failed to synchronize if a previously removed table column was still present.
 - Fixed an innocuous panic in Boards Rest API when requesting files and an error other than ``not found`` is encountered.
 - Fixed an issue where clicking on a channel link (for a channel the user was not a part of) caused the webapp to refresh, dropping the user from a call.
 - Fixed an issue with PDF preview rendering for certain Japanese characters.
 - Fixed an issue where the screen reader did not announce the action of copying the link in the invite modal.
 - Fixed an issue with post metadata not generating correctly for images due to missing content-type in response. This would result in certain embedded images not to display on mobile clients.
 - Fixed an issue where edits to messages persisted after canceling.
 - Added a condition for bot tags for webhook posts when a bot account is used for webhooks.
 - Fixed the sorting value of categories in ``CreateSidebarCategoryForTeamForUser``.
 - Fixed a potential crash when opening the user profile popover.
 - Fixed permalink and thread reply navigation between teams.
 - Fixed an issue with the installation of pre-packaged plugins that are not in the Marketplace.
 - Fixed an issue caused by a migration in a previous release. The query takes around 11ms on a PostgreSQL 14 DB t3.medium RDS instance. Locks on the preferences table will only be acquired if there are rows to delete, but the time taken is negligible.
 - Fixed an issue where modals did not close when clicking below them on certain screen sizes.
 - Fixed an issue with a few translation labels that couldn't be translated.
 - Fixed an issue where the server log UI for plain text formatting was unexpectedly removed in a previous release.
 - Fixed an issue where combined system messages did not display in chronological order.
 - Fixed an issue where the current user and status were not updated on WebSocket reconnect.
 - Fixed an issue where certain hashtags were not searchable when using database search.
 
### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:
 - Removed ``EnableInactivityEmail`` config setting.
 - Added a new config setting section ``ProductSettings``.
 
### Go Version
 - v8.0 is built with Go ``v1.19.5``.

### Known Issues
 - Using the "link" button puts the URL after ``[url]`` instead of replacing ``[url]`` when pasting [MM-53006](https://mattermost.atlassian.net/browse/MM-53006).
 - Saved posts in right-hand side show both the team and channel name in the post header [MM-53005](https://mattermost.atlassian.net/browse/MM-53005).
 - In a cluster config save scenario, it is difficult to disinguish between a timeout and a semantic error in the config if a config save in one node gets stuck [MM-52968](https://mattermost.atlassian.net/browse/MM-52968).
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.
 
### Contributors
 - [adj2908](https://github.com/adj2908), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [amyblais](https://github.com/amyblais), [andersonjeccel](https://translate.mattermost.com/user/andersonjeccel), [andriusbal](https://github.com/andriusbal), [andrleite](https://github.com/andrleite), [AshishDhama](https://github.com/AshishDhama), [avas27JTG](https://github.com/avas27JTG), [ayusht2810](https://github.com/ayusht2810), [bedo2991](https://github.com/bedo2991), [BenCookie95](https://github.com/BenCookie95), [calebroseland](https://github.com/calebroseland), [codyhall](https://github.com/codyhall), [collinewait](https://github.com/collinewait), [coltoneshaw](https://github.com/coltoneshaw), [ConorMacpherson](https://github.com/ConorMacpherson), [cpoile](https://github.com/cpoile), [cricrio](https://github.com/cricrio), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [d-wierdsma](https://github.com/d-wierdsma), [devinbinnie](https://github.com/devinbinnie), [Dismated](https://github.com/Dismated), [dsa-t](https://github.com/dsa-t), [DSchalla](https://github.com/DSchalla), [Eleferen](https://translate.mattermost.com/user/Eleferen), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [esarafianou](https://github.com/esarafianou), [exbu](https://github.com/exbu), [fmartingr](https://github.com/fmartingr), [fnogcps](https://github.com/fnogcps), [fr0mdual](https://github.com/fr0mdual), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gitstart](https://github.com/gitstart), [gomessguii](https://github.com/gomessguii), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [ifoukarakis](https://github.com/ifoukarakis), [isacikgoz](https://github.com/isacikgoz), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [johndavidlugtu](https://github.com/johndavidlugtu), [johnsonbrothers](https://github.com/johnsonbrothers), [jprusch](https://github.com/jprusch), [JulienTant](https://github.com/JulienTant), [julmondragon](https://github.com/julmondragon), [justinegeffen](https://github.com/justinegeffen), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [komoon8934](https://github.com/komoon8934), [koox00](https://github.com/koox00), [korkoshko](https://github.com/korkoshko), [kostaspt](https://github.com/kostaspt), [krisfremen](https://translate.mattermost.com/user/krisfremen), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [larkox](https://github.com/larkox), [laurensramandt](https://github.com/laurensramandt), [LeonardJouve](https://github.com/LeonardJouve), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [m1lt0n](https://github.com/m1lt0n), [majo](https://translate.mattermost.com/user/majo), [manojmalik20](https://github.com/manojmalik20), [maruTA-bis5](https://github.com/maruTA-bis5), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-src](https://github.com/matthew-src), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [maxtrem271991](https://github.com/maxtrem271991), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [milotype](https://translate.mattermost.com/user/milotype), [mirshahriar](https://github.com/mirshahriar), [morgancz](https://github.com/morgancz), [Mshahidtaj](https://github.com/Mshahidtaj), [munish7771](https://github.com/munish7771), [nab-77](https://github.com/nab-77), [neallred](https://github.com/neallred), [nevyangelova](https://github.com/nevyangelova), [nickmisasi](https://github.com/nickmisasi), [Nityanand13](https://github.com/Nityanand13), [oh6hay](https://github.com/oh6hay), [okanisildar](https://github.com/okanisildar), [panklobouk](https://translate.mattermost.com/user/panklobouk), [Partizann](https://github.com/Partizann), [phoinixgrr](https://github.com/phoinixgrr), [pjenicot](https://github.com/pjenicot), [potatogim](https://github.com/potatogim), [pvev](https://github.com/pvev), [qvarnstr0m](https://github.com/qvarnstr0m), [roadt](https://github.com/roadt), [Roy-Orbison](https://github.com/Roy-Orbison), [Rutboy](https://github.com/Rutboy), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [sinansonmez](https://github.com/sinansonmez), [Sjazz](https://github.com/Sjazz), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [srkgupta](https://github.com/srkgupta), [stafot](https://github.com/stafot), [stevemudie](https://github.com/stevemudie), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [tanmay-des](https://github.com/tanmay-des), [tanmaydatta](https://github.com/tanmaydatta), [tanmaythole](https://github.com/tanmaythole), [thinkGeist](https://github.com/thinkGeist), [toninis](https://github.com/toninis), [trilopin](https://github.com/trilopin), [unode](https://github.com/unode), [varghesejose2020](https://github.com/varghesejose2020), [vish9812](https://github.com/vish9812), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [wuwinson](https://github.com/wuwinson), [Yananeer](https://github.com/Yananeer), [yasserfaraazkhan](https://github.com/yasserfaraazkhan)

## Release v7.11 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

  - The Mattermost v7.11 release has been canceled as we are working on architectural changes for the Mattermost Suite (Channels, Playbooks, Boards, and Calls). The next scheduled release is v8.0 this summer.

## Release v7.10 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

- **v7.10.2, released 2023-05-18**
  - Fixed an issue where v7.10 reported an incorrect mmctl version.
- **v7.10.1, released 2023-05-16**
  - Mattermost v7.10.1 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where a user would still see threads in the threads view of channels they have left. Migration execution time in MySQL: Query OK, 2766769 rows affected (4 min 47.57 sec). Migration execution time in PostgreSQL: 58.11 sec, DELETE 2766690.
  - Pre-packaded version 1.2.1 of the Apps plugin.
  - Pre-packaded version 2.1.5 of the GitHub plugin.
  - Updated prepackaged Playbooks v1.36.1.
  - Fixed an issue where true-up review submissions always failed.
  - Fixed an issue caused by a migration in the previous release. Query takes around 11ms on a PostgreSQL 14 DB t3.medium RDS instance. Locks on the preferences table will only be acquired if there are rows to delete, but the time taken is negligible.
- **v7.10.0, released 2023-04-14**
  - Original 7.10.0 release

Mattermost v7.10.0 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Important Upgrade Notes

 - In the next release, v7.11, the following repositories will be merged into one: ``mattermost-server``, ``mattermost-webapp``, ``focalboard`` and ``mattermost-plugin-playbooks``. Developers should read the updated [Developer Guide](https://developers.mattermost.com/contribute/developer-setup/) for details. **Playbooks and Boards will be core parts of the product that cannot be disabled**.

**IMPORTANT:** If you upgrade from a release earlier than v7.9, please read the other [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).

### Improvements

#### User Interface (UI)
 - Added the ability to set a reminder to read a message at a specific time via the **More** menu in messages.
 - Mentions from muted channels are no longer shown or counted on the browser and desktop tabs.
 - Updated descriptions for **Environment > Developer** settings in the **System Console** to clarify that changes require a server restart to take effect.
 - The custom user status is now shown in the right-hand side **Members** pane and in **System Console > Users**.
 - Added the ability to invite multiple people at a time by email to a Mattermost instance.
 - Added accessibility support to the date picker.
 - System admins are prompted to complete a feedback survey during a workspace downgrade process from Cloud Professional to Cloud Free.
 - Migrated the message (...) **More** option to a Material UI (MUI) menu.
 - Updated pre-packaged Boards to v7.10.0.
 - Updated pre-packaged Calls to v0.15.1.

#### Administration
 - The ``ServiceSettings.PostEditTimeLimit`` config setting no longer affects Plugins, Shared Channels, Integration Actions, or Mattermost Products.
 - The app server no longer starts if the telemetry ID in the systems table doesn't exist. Although there is no action required by the administrators, it may be good to be aware of this change. If the ID doesn't exist, administrators can read the error log and take action against it.
 - Added additional values to the support packet.
 - Self-hosted instances will now show invoices in **System Console > Billing & Account > Billing History*** for prior self-serve purchases.
 - A 404 error is now returned if an invoice could not be fetched for a self-hosted deployment.
 
#### Performance
 - Writes to websocket now take 13% less memory and happen 22% faster per message.

### API Changes
 - Added a ``exclude_files_count`` parameter to exclude file counts from channel stats API.

### Bug Fixes
 - Fixed an issue where Shared Channels wasn't properly added to the Professional license.
 - Fixed new teams to use the updated translation for default channels after a config change.
 - Fixed issues with spacing in the channel categories and maintained the same spacing in the left-hand side.
 - Fixed disproportionate height issues for tall single images.
 - Fixed an issue where a single WebSocket reconnect could be handled multiple times which would negatively affect performance.
 - Fixed an issue in **Top DM Insights**, where a deleted participant caused DM Insights to fail.
 - Fixed an issue where Cloud limits would briefly flash in the System Console before disappearing.
 - Fixed an issue with the compact message mode.
 
### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:
 - Under ``ServiceSettings`` in the ``config.json``:
   - ``SelfHostedExpansion`` config setting was added to support incremental additions/changes to this feature.
 
### Go Version
 - v7.10 is built with Go ``v1.19.5``.
 
### Open Source Components
 - Added ``date-fns`` to https://github.com/mattermost/mattermost-webapp/.

### Known Issues
 - Users are unexpectedly forced to enable JSON logging [MM-51453](https://mattermost.atlassian.net/browse/MM-51453).
 - The new Insights feature has some performance costs that we are working to optimize. This feature can be disabled by setting the ``MM_FEATUREFLAGS_INSIGHTSENABLED`` environment variable to ``false``. See the `Insights </welcome/insights.html>`__ documentation for details.
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - Boards export and reimport results in duplicates boards because all IDs are replaced by new ones on the server. See the [GitHub issue](https://github.com/mattermost/focalboard/issues/1924) for more information.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.
 
### Contributors
 - [11sma](https://github.com/11sma), [adj2908](https://github.com/adj2908), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [amyblais](https://github.com/amyblais), [amynicol1985](https://github.com/amynicol1985), [andrius.balsevicius](https://translate.mattermost.com/user/andrius.balsevicius), [angeloskyratzakos](https://github.com/angeloskyratzakos), [AntalaFilip](https://github.com/AntalaFilip), [anx-ag](https://github.com/anx-ag), [aputtu](https://github.com/aputtu), [asaadmahmood](https://github.com/asaadmahmood), [AshishDhama](https://github.com/AshishDhama), [avas27JTG](https://github.com/avas27JTG), [ayusht2810](https://github.com/ayusht2810), [BenCookie95](https://github.com/BenCookie95), [bfontaine](https://github.com/bfontaine), [byigorv](https://github.com/byigorv), [calebroseland](https://github.com/calebroseland), [coltoneshaw](https://github.com/coltoneshaw), [ConorMacpherson](https://github.com/ConorMacpherson), [cpoile](https://github.com/cpoile), [creeper-0910](https://translate.mattermost.com/user/creeper-0910), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [d-wierdsma](https://github.com/d-wierdsma), [DaDummy](https://github.com/DaDummy), [devinbinnie](https://github.com/devinbinnie), [Dmitry](https://translate.mattermost.com/user/Dmitry), [dylanrichards](https://github.com/dylanrichards), [EduardoSellanes](https://github.com/EduardoSellanes), [Eleferen](https://translate.mattermost.com/user/Eleferen), [Elpunical](https://github.com/Elpunical), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [ericgaspar](https://github.com/ericgaspar), [esarafianou](https://github.com/esarafianou), [ewwollesen](https://github.com/ewwollesen), [fmartingr](https://github.com/fmartingr), [fnogcps](https://github.com/fnogcps), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gitstart](https://github.com/gitstart), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hattori611](https://github.com/hattori611), [hmhealey](https://github.com/hmhealey), [ialorro](https://github.com/ialorro), [ifoukarakis](https://github.com/ifoukarakis), [isaacbegit](https://github.com/isaacbegit), [isacikgoz](https://github.com/isacikgoz), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jnsgruk](https://github.com/jnsgruk), [Johennes](https://github.com/Johennes), [johnsonbrothers](https://github.com/johnsonbrothers), [jprusch](https://github.com/jprusch), [JulienTant](https://github.com/JulienTant), [julmondragon](https://github.com/julmondragon), [justinegeffen](https://github.com/justinegeffen), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [kaykayehnn](https://github.com/kaykayehnn), [KBeDevel](https://github.com/KBeDevel), [khoipro](https://github.com/khoipro), [kmaed](https://github.com/kmaed), [komoon8934](https://translate.mattermost.com/user/komoon8934), [koox00](https://github.com/koox00), [kostaspt](https://github.com/kostaspt), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [kwiersgalla](https://github.com/kwiersgalla), [larkox](https://github.com/larkox), [leonambeez](https://translate.mattermost.com/user/leonambeez), [lieut-data](https://github.com/lieut-data), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [m1lt0n](https://github.com/m1lt0n), [majo](https://translate.mattermost.com/user/majo), [manojmalik20](https://github.com/manojmalik20), [marianunez](https://github.com/marianunez), [maruTA-bis5](https://translate.mattermost.com/user/maruTA-bis5), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-src](https://github.com/matthew-src), [matthew-w](https://translate.mattermost.com/user/matthew-w), [MatthewDorner](https://github.com/MatthewDorner), [MattSilvaa](https://github.com/MattSilvaa), [metanerd](https://github.com/metanerd), [mgdelacroix](https://github.com/mgdelacroix), [michael_kim](https://translate.mattermost.com/user/michael_kim), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [mini-bomba](https://github.com/mini-bomba), [mirshahriar](https://github.com/mirshahriar), [moatasim](https://translate.mattermost.com/user/moatasim), [MoatazMuhammad51](https://github.com/MoatazMuhammad51), [Mshahidtaj](https://github.com/Mshahidtaj), [munish7771](https://github.com/munish7771), [muratbayan](https://translate.mattermost.com/user/muratbayan), [mvitale1989](https://github.com/mvitale1989), [natalie-hub](https://github.com/natalie-hub), [neallred](https://github.com/neallred), [nevyangelova](https://github.com/nevyangelova), [nickmisasi](https://github.com/nickmisasi), [Nityanand13](https://github.com/Nityanand13), [NixemDEV](https://translate.mattermost.com/user/NixemDEV), [oraliahdz](https://github.com/oraliahdz), [paolo-rossi](https://github.com/paolo-rossi), [Peytob](https://github.com/Peytob), [phoinixgrr](https://github.com/phoinixgrr), [pjenicot](https://translate.mattermost.com/user/pjenicot), [plant99](https://github.com/plant99), [plut0s](https://translate.mattermost.com/user/plut0s), [potatogim](https://translate.mattermost.com/user/potatogim), [pureiris](https://github.com/pureiris), [pvev](https://github.com/pvev), [Qui3t0wL](https://github.com/Qui3t0wL), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [roadt](https://github.com/roadt), [Rutboy](https://translate.mattermost.com/user/Rutboy), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [Sharuru](https://github.com/Sharuru), [sibasankarnayak](https://github.com/sibasankarnayak), [simcard0000](https://github.com/simcard0000), [sinansonmez](https://github.com/sinansonmez), [Sjazz](https://github.com/Sjazz), [smallcms](https://github.com/smallcms), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [srkgupta](https://github.com/srkgupta), [stafot](https://github.com/stafot), [stevemudie](https://github.com/stevemudie), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [tanmay-des](https://github.com/tanmay-des), [tanmaythole](https://github.com/tanmaythole), [Tasy218](https://translate.mattermost.com/user/Tasy218), [toninis](https://github.com/toninis), [trilopin](https://github.com/trilopin), [varghesejose2020](https://github.com/varghesejose2020), [Wainwright0830](https://github.com/Wainwright0830), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [wuwinson](https://github.com/wuwinson), [xiao](https://translate.mattermost.com/user/xiao), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yomiadetutu1](https://github.com/yomiadetutu1)

### Upcoming Deprecations and Breaking Changes in Mattermost v8.0

The following deprecations and breaking changes are planned for the Mattermost v8.0 release, which is scheduled for the summer of 2023. This list is subject to change prior to the release.

1. Update module version to v8.0. Clients will have to change their module path to the new structure. Very minimal change. There are no API level breaking changes that would require code changes.
2. Remove ``ExperimentalSettings.PatchPluginsReactDOM``. If this setting was previously enabled, confirm that:
    1. All Mattermost-supported plugins are updated to the latest versions.
    2. Any other plugins have been updated to support React 17. See the [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) for v7.7 for more information.
3. Three configuration fields have been added, ``LogSettings.AdvancedLoggingJSON``, ``ExperimentalAuditSettings.AdvancedLoggingJSON``, and ``NotificationLogSettings.AdvancedLoggingJSON`` which support multi-line JSON, escaped JSON as a string, or a filename that points to a file containing JSON.  The ``AdvancedLoggingConfig`` fields have been deprecated.
4. Remove deprecated ``PermissionUseSlashCommands``.
5. Remove deprecated ``model.CommandArgs.Session``.
6. Remove support for PostgreSQL v10. The new minimum PostgreSQL version will be v11.
7. Enable Apps Bar by default.
8. Pass a ``context.Context`` to Client4 methods.
9. The Mattermost public API for Go is now available as a distinctly versioned package. Instead of pinning a particular commit hash, use idiomatic Go to add this package as a dependency: go get github.com/mattermost/mattermost-server/server/public. This relocated Go API maintains backwards compatibility with Mattermost v7. Furthermore, the existing Go API previously at github.com/mattermost/mattermost-server/v6/model remains forward compatible with Mattermost v8, but may not contain newer features. Plugins do not need to be recompiled, but developers may opt in to using the new package to simplify their build process. The new public package is shipping alongside Mattermost v8 as version 0.5.0 to allow for some additional code refactoring before releasing as v1 later this year.

## Release v7.9 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

- **v7.9.4, released 2023-05-16**
  - Mattermost v7.9.4 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where a user would still see threads in the threads view of channels they have left. Migration execution time in MySQL: Query OK, 2766769 rows affected (4 min 47.57 sec). Migration execution time in PostgreSQL: 58.11 sec, DELETE 2766690.
  - Pre-packaded version 1.2.1 of the Apps plugin.
  - Pre-packaded version 2.1.5 of the GitHub plugin.
  - Backporting fix for oauth 2. Query times depend on if you have rows to delete or not. Please see the [important upgrade notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) for more details.
- **v7.9.3, released 2023-04-27**
  - Mattermost v7.9.3 contains a medium severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where true-up review submissions always failed.
- **v7.9.2, released 2023-04-12**
  - Mattermost v7.9.2 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Updated prepackaged Boards to v7.9.3.
  - Updated prepackaged Playbooks to v1.36.1.
  - Fixed an issue with compact message mode.
  - Fixed an issue where ``NotifyAdmin`` job reported an error for unlicensed servers.
- **v7.9.1, released 2023-03-17**
  - Mattermost v7.9.1 contains a high severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
- **v7.9.0, released 2023-03-16**
  - Original 7.9.0 release

Mattermost v7.9.0 contains a low severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Important Upgrade Notes

- Added a new index on ``Posts(OriginalId)``. For a database with 11.8 million posts, on a machine with a i7-11800H CPU (8 cores, 16 threads), 32GiB of RAM and SSD, the index creation takes 98.51s on MYSQL and 2.6s on PostgreSQL. 
- In PostgreSQL databases, the ``Posts`` table will be locked during index creation. To avoid locking this table, admins can create the index manually before performing the upgrade using the following non-blocking query: ``CREATE INDEX CONCURRENTLY idx_posts_original_id ON Posts(OriginalId);``. 
- Admins managing PostgreSQL deployments containing fewer posts may prefer that the migration process creates the index, and accept that ``Posts`` table will remain locked until the migration is complete.

**IMPORTANT:** If you upgrade from a release earlier than v7.8, please read the other [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).

### Compatibility
 - Updated Firefox minimum supported version to 102+.
 - Updated Safari minimum supported version to 16.2+.
 - Updated Windows minimum supported version to 10+.
 - Updated Chromium minimum supported version to 110+.
 - Updated Edge minimum supported version to 110+.

### Highlights

#### Boards
 - System and team admins are now able to join any board on the team as a board admin via the board URL.
 - Additional Compliance APIs to return the history of boards and blocks, including deleted items (available in Mattermost Enterprise Edition and above).

### Improvements

#### User Interface (UI)
 - Prepackaged Calls v0.14.0.
 - All post components were removed in favor of a unified approach.
 - App bindings are now refreshed when a App plugin-enabled event gets triggered.
 - Improvements were added to the sidebar channel and category menus.
 - Removed right-click hijacking on code blocks in messages.
 - The order of the Leave Channel and Archive Channel settings were updated to match the mobile app.
 - Added the condition to remove unread styling for archived channels and to filter archived channels from local data.
 - Changed the collapsed post fade out effect to be less buggy.
 - Users now have the ability to see the history of edited messages and to restore an old message version with the current version.
 - Improved the user interface of the user profile popover.

#### Administration
 - Boards cards are no longer mentioned as being limited in the **System Console**, the limits usage modal, the downgrade modal, or the left-hand side menu.
 - Removed unused ``ProductLimits.Integrations``.
 - Export files now contain the read and unread status for channels.
 - Added an error message when running an LDAP sync with ``SyncEnabled`` set to ``false``.
 - Added Admin log table filtering and sorting.
 - GraphQL APIs are now correctly counted when measuring performance telemetry.
 - Added a dynamic call-to-action under **System Console > Site Statistics and > Team Statistics** for air-gapped and non-air-gapped systems. The banner reminding about true-up follows the schedule [outlined here](https://docs.mattermost.com/about/self-hosted-subscriptions.html#quarterly-true-up-report).
 - Screened self-hosted purchases now block the Admin from re-attempting a purchase for three days.

#### Performance
 - Reduced the rate that unreads are resynced when the window is focused from ten seconds to two minutes.
 - The center channel is no longer shown as loading when switching teams.
 - Added logging fixes: empty ``short_message`` for Gelf formatter is no longer allowed and ``params.Host`` is now used over ``params.IP`` for syslog config.

### Bug Fixes
 - Fixed an issue where the System Console link to purchase a self-hosted license would get stuck showing the in-product purchase progress modal.
 - Fixed an issue where the true-up notification in the invite modal did not render the call-to-action correctly.
 - Fixed new teams to use the updated translation for default channels after a configuration change.
 - Fixed a layout issue in the System Console for smaller-sized tablets.
 - Fixed an issue where a "plugin configured with a nil SecureConfig" warning was logged when starting each plugin.
 - Fixed an issue where portal availability was checked when not on Enterprise edition.
 - Fixed an issue where C# syntax highlighting was not working.
 - Fixed an issue where incoming webhooks changed the user's activity while the user was offline/away.
 - Fixed an issue where usernames were not clickable in the right-hand side.

### API Changes
 - Added an ``exclude_files_count`` parameter to exclude file counts from the channel stats API.
 - Added a new API endpoint ``GET api/v4/posts/[POST_ID]/edit_history``.
 - Added a new API endpoint ``DELETE /api/v4/cloud/delete-workspace``.

### Database Changes
 - Added the ``SentAt`` column to ``NotifyAdmin``.
 - Updated ``NotifyAdmin.RequiredFeature`` column type to ``varchar(255)``.
 - Updated ``NotifyAdmin.RequiredPlan`` column type to ``varchar(100)``.

### Go Version
 - v7.9 is built with Go ``v1.19.0``.
 
### Open Source Components
 - Added ``@mui/base``, ``@mui/material`` and ``@mui/styled-engine-sc``, and removed ``form-data`` from https://github.com/mattermost/mattermost-webapp/.

### Known Issues
 - Users are unexpectedly forced to enable JSON logging [MM-51453](https://mattermost.atlassian.net/browse/MM-51453).
 - Checkmarks are missing from the left-hand side submenus [MM-51091](https://mattermost.atlassian.net/browse/MM-51091).
 - The new Insights feature has some performance costs that we are working to optimize. This feature can be disabled by setting the ``MM_FEATUREFLAGS_INSIGHTSENABLED`` environment variable to ``false``.
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - Boards export and reimport results in duplicates boards because all IDs are replaced by new ones on the server. See the [GitHub issue](https://github.com/mattermost/focalboard/issues/1924) for more information.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.
 
### Contributors
 - [11sma](https://translate.mattermost.com/user/11sma), [aashish0909](https://github.com/aashish0909), [AbhinavVihan](https://github.com/AbhinavVihan), [aeomin](https://github.com/aeomin), [Afsoon](https://github.com/Afsoon), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [akaMrDC](https://github.com/akaMrDC), [alzee](https://github.com/alzee), [amyblais](https://github.com/amyblais), [andrleite](https://github.com/andrleite), [AntalaFilip](https://translate.mattermost.com/user/AntalaFilip), [anurag6713](https://github.com/anurag6713), [anx-ag](https://github.com/anx-ag), [aputsiak](https://translate.mattermost.com/user/aputsiak), [aputtu](https://github.com/aputtu), [asaadmahmood](https://github.com/asaadmahmood), [AshishDhama](https://github.com/AshishDhama), [avas27JTG](https://github.com/avas27JTG), [azigler](https://github.com/azigler), [BenCookie95](https://github.com/BenCookie95), [BenLloydPearson](https://github.com/BenLloydPearson), [calebroseland](https://github.com/calebroseland), [cedricstocke](https://github.com/cedricstocke), [CI-YU](https://github.com/CI-YU), [coltoneshaw](https://github.com/coltoneshaw), [ConorMacpherson](https://github.com/ConorMacpherson), [cpoile](https://github.com/cpoile), [creeper-0910](https://github.com/creeper-0910), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [d-wierdsma](https://github.com/d-wierdsma), [davidboto](https://github.com/davidboto), [david.mach@mdsystem.cz](https://translate.mattermost.com/user/david.mach@mdsystem.cz), [devinbinnie](https://github.com/devinbinnie), [doc-sheet](https://github.com/doc-sheet), [DummyThatMatters](https://github.com/DummyThatMatters), [Eleferen](https://translate.mattermost.com/user/Eleferen), [Elpunical](https://github.com/Elpunical), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [fmartingr](https://github.com/fmartingr), [FMP-Dev](https://github.com/FMP-Dev), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gbochora](https://github.com/gbochora), [gitstart](https://github.com/gitstart), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hattori611](https://translate.mattermost.com/user/hattori611), [hereje](https://github.com/hereje), [hmhealey](https://github.com/hmhealey), [ichistmeinname](https://github.com/ichistmeinname), [icq4ever](https://github.com/icq4ever), [ifoukarakis](https://github.com/ifoukarakis), [iogungbade](https://github.com/iogungbade), [iot-defcon](https://github.com/iot-defcon), [isacikgoz](https://github.com/isacikgoz), [jasonblais](https://github.com/jasonblais), [javaguirre](https://github.com/javaguirre), [jecepeda](https://github.com/jecepeda), [jfrerich](https://github.com/jfrerich), [jgilliam17](https://github.com/jgilliam17), [johndavidlugtu](https://github.com/johndavidlugtu), [johnsonbrothers](https://github.com/johnsonbrothers), [jordanafung](https://github.com/jordanafung), [josephbaylon](https://github.com/josephbaylon), [jprusch](https://github.com/jprusch), [JtheBAB](https://github.com/JtheBAB), [JulienTant](https://github.com/JulienTant), [justinegeffen](https://github.com/justinegeffen), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [kjh0523](https://github.com/kjh0523), [kayazeren](https://translate.mattermost.com/user/kayazeren), [KazminM](https://translate.mattermost.com/user/KazminM), [KBeDevel](https://translate.mattermost.com/user/KBeDevel), [koox00](https://github.com/koox00), [kostaspt](https://github.com/kostaspt), [krisfremen](https://github.com/krisfremen), [krmh04](https://github.com/krmh04), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [larkox](https://github.com/larkox), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [liz-segura98](https://github.com/liz-segura98), [m-ripper](https://github.com/m-ripper), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [m1lt0n](https://github.com/m1lt0n), [maisnamrajusingh](https://github.com/maisnamrajusingh), [majo](https://translate.mattermost.com/user/majo), [manojmalik20](https://github.com/manojmalik20), [marciohouse](https://github.com/marciohouse), [marciosantos](https://translate.mattermost.com/user/marciosantos), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-src](https://github.com/matthew-src), [matthew-w](https://translate.mattermost.com/user/matthew-w), [mdsystem](https://github.com/mdsystem), [metanerd](https://github.com/metanerd), [mhd-sln](https://github.com/mhd-sln), [michelengelen](https://github.com/michelengelen), [mickmister](https://github.com/mickmister), [microolapshare](https://github.com/microolapshare), [milotype](https://github.com/milotype), [mini-bomba](https://translate.mattermost.com/user/mini-bomba), [mirshahriar](https://github.com/mirshahriar), [MoatazMuhammad51](https://translate.mattermost.com/user/MoatazMuhammad51), [moussetc](https://github.com/moussetc), [munish7771](https://github.com/munish7771), [mvitale1989](https://github.com/mvitale1989), [mylonsuren](https://github.com/mylonsuren), [nathanaelhoun](https://github.com/nathanaelhoun), [neallred](https://github.com/neallred), [neflyte](https://github.com/neflyte), [nevyangelova](https://github.com/nevyangelova), [nickmisasi](https://github.com/nickmisasi), [nikolaizah](https://github.com/nikolaizah), [nishit-prasad](https://github.com/nishit-prasad), [Nityanand13](https://github.com/Nityanand13), [nltb99](https://github.com/nltb99), [OGreSiv](https://translate.mattermost.com/user/OGreSiv), [oleksandr-kucheriavyi](https://github.com/oleksandr-kucheriavyi), [orsczech](https://translate.mattermost.com/user/orsczech), [OstapMelnychuk](https://github.com/OstapMelnychuk), [phoinixgrr](https://github.com/phoinixgrr), [plant99](https://github.com/plant99), [potatogim](https://github.com/potatogim), [pvev](https://github.com/pvev), [Rajat-Dabade](https://github.com/Rajat-Dabade), [Rizumu85](https://github.com/Rizumu85), [Roy-Orbison](https://github.com/Roy-Orbison), [saturninoabril](https://github.com/saturninoabril), [satya-vinay](https://github.com/satya-vinay), [sbishel](https://github.com/sbishel), [Schleuse](https://github.com/Schleuse), [Sharuru](https://github.com/Sharuru), [shinnlok](https://github.com/shinnlok), [sinansonmez](https://github.com/sinansonmez), [Sjazz](https://github.com/Sjazz), [Sn-Kinos](https://translate.mattermost.com/user/Sn-Kinos), [Soldierplayz6867](https://github.com/Soldierplayz6867), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [stevemudie](https://github.com/stevemudie), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [Sudhanva-Nadiger](https://github.com/Sudhanva-Nadiger), [tboulis](https://github.com/tboulis), [tiagodll](https://github.com/tiagodll), [toninis](https://github.com/toninis), [trilopin](https://github.com/trilopin), [tsabi](https://github.com/tsabi), [Udval.O](https://translate.mattermost.com/user/Udval.O), [Van-cmyk](https://github.com/Van-cmyk), [varghesejose2020](https://github.com/varghesejose2020), [vhaarr](https://translate.mattermost.com/user/vhaarr), [Wainwright0830](https://github.com/Wainwright0830), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [xiao](https://translate.mattermost.com/user/xiao), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [zclk](https://github.com/zclk)

## Release v7.8 - [Extended Support Release](https://docs.mattermost.com/upgrade/release-definitions.html#extended-support-release-esr)

- **v7.8.6, released 2023-05-31**
  - Fixed an issue where the total user count was fetched for every client connection. It is only necessary to fetch this once.
  - Prepackaged version 1.3.0 of the Welcomebot plugin.
- **v7.8.5, released 2023-05-17**
  - Mattermost v7.8.5 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where a user would still see threads in the threads view of channels they have left. Migration execution time in MySQL: Query OK, 2766769 rows affected (4 min 47.57 sec). Migration execution time in PostgreSQL: 58.11 sec, DELETE 2766690.
  - Prepackaged version 1.2.1 of the Apps plugin.
  - Prepackaged version 2.1.5 of the GitHub plugin.
  - Updated the Docker Base Image from Debian to Ubuntu 22.04 LTS.
  - Backported a fix related to Oauth 2. Query times depend on if you have rows to delete or not. Please see the [important upgrade notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) for more details.
- **v7.8.4, released 2023-04-27**
  - Mattermost v7.8.4 contains a medium severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Limited channel search results to 50 to fix a performance issue.
  - Fixed an issue where true-up review submissions always failed.
- **v7.8.3, released 2023-04-12**
  - Mattermost v7.8.3 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Updated prepackaged Boards to v7.8.4.
  - Updated prepackaged Playbooks to v1.36.1.
  - Added additional values to the support packet.
- **v7.8.2, released 2023-03-17**
  - Mattermost v7.8.2 contains a high severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Added a ``exclude_files_count`` parameter to exclude file counts from channel stats API.
  - Excluded the file count on channel stats API call on from channel header.
  - Fixed an issue where the Shared Channels feature wasn't properly included in the Professional license.
- **v7.8.1, released 2023-03-01**
  - Mattermost v7.8.1 contains a medium level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
- **v7.8.0, released 2023-02-16**
  - Original 7.8.0 release

Mattermost v7.8.0 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Important Upgrade Notes

 - [Message Priority & Acknowledgement](https://docs.mattermost.com/configure/site-configuration-settings.html#message-priority) is now enabled by default for all instances. You may disable this feature in the System Console by going to **Posts > Message Priority** or via the config ``PostPriority`` setting.

**IMPORTANT:** If you upgrade from a release earlier than v7.5, please read the other [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).

### Highlights

#### Boards
 - Added support for person, multi-person, and date property filters in Boards.
 - Added support for person property groups in Boards.
 - See [the docs](https://docs.mattermost.com/boards/groups-filter-sort.html#work-with-groups-filter-and-sort) for more details.

### Improvements

#### User Interface (UI)
 - Pre-packaged Calls v0.13.0.
 - Pre-packaged Playbooks v1.36.0.
 - Insights and drafts are now included when navigating through channels in the channel sidebar using ALT+UP/DOWN arrow keyboard keys.
 - Added an onboarding tour point for Global Drafts.
 - Updated prepackaged version of Apps plugin to 1.2.0.
 - Added group members count to the group autocomplete.
 - Selecting a group mention now displays group details and membership.
 - Improved the collapsed state of the message formatting toolbar.
 - App Framework channel and user fields now support multi-select properties to allow users to select multiple values in a form.
 - Increased the character count for desktop notifications on Windows to 120 from 50.
 - Prioritized members of recently viewed direct or group messages when adding users to a channel.
 - Added support for multiple users and channels to the ``/invite`` slash command.

#### Administration
 - Self-hosted admins can now purchase licenses in-app when service setting ``SelfHostedPurchase`` is true.
 - Endpoint to portal added to detect whether a license is suitable for self-expansion. Customers over their seat limit can expand their license seats.
 - Airgapped purchase experience is now shown only when appropriate and a simplified authentication flow is now used for the self-hosted purchase.
 - The export file now contains the server version and a creation timestamp.
 - Total Activated Users was changed back to Total Active Users on the **System Console > Reporting > Site Statistics** page.
 - Added ``restore_group`` permission to the mmctl and to the **System Console > Permissions**.
 - Improved bulk export logging.
 - Compliance export jobs can now cancel the SQL query execution during server shutdown which will allow the job to exit faster.
 - The message export compliance job can now survive server restarts. The job will pause and save state when the server is shutting down, and resume from the previously saved state when the server starts back up.
 - Only one instance of the job will be automatically scheduled to run as per the ``MessageExportSettings.DailyRunTime`` config value.
 - Mattermost will throw an error if it detects an Elasticsearch version greater than 7.
 - The maximum size of uploaded emojis is reduced to 512KB to reduce image download bandwidth.
 - Users can now monitor the progress of the bulk export job via its metadata field. It is available at ``mmctl export job show <jobID>``.
 - Compliance exports no longer time out when uploading to S3.
 - Users can now supply a certificate authority (CA) file and client certificates for the Elasticsearch client.
 - Enabled ``EnableOAuthServiceProvider`` by default.
 - Grafana metrics are now available for database connection metrics. They are:
    - ``max_open_connections``
    - ``open_connections``
    - ``in_use_connections``
    - ``idle_connections``
    - ``wait_count_total``
    - ``wait_duration_seconds_total``
    - ``max_idle_closed_total``
    - ``max_idle_time_closed_total``
    - ``max_lifetime_closed_total``
 - Made the ``registerChannelIntroButtonAction`` plugin API usable by plugins other than Boards.
 - The following new HTTP headers and values are now written on all responses. These default values should make sense in most installations and can be overridden by a reverse proxy or ingress configuration. Note that the empty ``Permissions-Policy`` header does not have any actual effect. Users are recommended to change it to a more restrictive value based on their use case. For more information, see the [W3C Reference](https://www.w3.org/TR/permissions-policy/) or [this article](https://developer.mozilla.org/en-US/docs/Web/HTTP/Permissions_Policy).

	```
	Permissions-Policy: 
	Referrer-Policy: no-referrer
	X-Content-Type-Options: nosniff
	```

### Bug Fixes
 - Fixed an issue where if a self-hosted purchase was not available, an air-gapped modal was shown instead of going to the CWS purchase portal experience directly.
 - Fixed small visual issues with self-hosted purchase modal. Adjusted wording for admins trying to purchase when a purchase is already in progress.
 - Fixed an issue where attempting to create a team with a duplicate URL displayed the wrong error.
 - Fixed an issue where the custom status modal did not close when navigating to the custom emoji page.
 - Fixed an issue where selections within a code block were not properly copied to clipboard.
 - Fixed an issue where threads with 0 replies would show in all threads.
 - Fixed an issue with the styling of date pickers.
 - Fixed an issue with fetching the latest user's profile picture in Insights.
 - Fixed an issue where ``--center-channel-text`` CSS variable was used instead of ``--center-channel-color``.
 - Fixed an issue where the screen reader timestamp announcement was too long.
 - Fixed an issue where profile pictures, usernames, and full names did not update instantly in Insights.
 - Fixed an issue where the metrics server restarted for every config change.
 - Fixed the slash command description help text.
 - Fixed an issue where selecting **Contact Sales** didn't pre-fill the reason for contacting sales.
 - Fixed an issue where the screen readers did not announce the selected state of the sidebar submenu items.
 - Fixed an issue where the metrics server was not prevented from starting while running export commands.
 - Fixed an issue where long group mentions and user mentions didn't wrap properly.
 - Fixed an issue with fetching first/last name for GitLab user using OpenID.
 - Fixed an issue with the plugin ``/public`` handling for subpaths.
 - Fixed an issue where selecting **Pinned** on a post in the Threads view would result in the right-hand side being stuck in a loading state.
 - Fixed an issue where the profile popover did not dismiss when opening a modal through a shortcut.
 - Fixed an issue where the **Run Deletion Job Now** button for Data Retention wasn’t disabled when all policies were set to **keep forever**.
 - Fixed an issue that prevented the creation of the initial admin user for new servers.
 - Fixed an issue where making a channel non-read-only required a refresh of the client to see the change.
 - Fixed an issue where Top Channels for Insights didn't show results if the current user's configured timezone wasn't present in MySQL's ``mysql.time_zone_name table``.
 - Fixed an issue where a white screen appeared when a guest was removed from the last channel while on Threads.
 - Fixed an issue where a Direct Message thread did not get disabled when a user was deactivated.
 - Fixed an issue where email notifications for Direct Messages from Playbooks contained broken URLs.
 - Fixed an issue where bulk import crashed with invalid memory address or nil pointer dereference.
 - Fixed an issue with special characters in the System Console log filename causing logging configuration to break.
 - Fixed an issue where the PDF renderer was not rendering all the pages.
 - Fixed a 404 error from requests to ``/api/v4/system/notices/`` on page load.
 - Fixed an issue where file uploading appeared "stuck" in processing state.
 - Fixed an issue where archived channels appeared as unread in the channel switcher.

### API Changes
 - Added new API endpoint ``GET /api/v4/posts/:post_id/info`` to allow checking if the post that a permalink is pointing to is accessible by joining teams or channels.
 - Added validity checks for role related parameters in ``GET /users``.

### Go Version
 - v7.8 is built with Go ``v1.18.1``.

### Known Issues
 - The new Insights feature has some performance costs that we are working to optimize. This feature can be disabled by setting the ``MM_FEATUREFLAGS_INSIGHTSENABLED`` environment variable to ``false``.
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in high availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in high availability mode.
 - Boards export and reimport results in duplicates boards because all IDs are replaced by new ones on the server. See the [GitHub issue](https://github.com/mattermost/focalboard/issues/1924) for more information.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.
 
### Contributors
 - [AbhinavVihan](https://github.com/AbhinavVihan), [adityash1](https://github.com/adityash1), [Afsoon](https://github.com/Afsoon), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [amayasova](https://github.com/amayasova), [amyblais](https://github.com/amyblais), [andrewbrown00](https://github.com/andrewbrown00), [andrleite](https://github.com/andrleite), [anurag6713](https://github.com/anurag6713), [anx-ag](https://github.com/anx-ag), [asaadmahmood](https://github.com/asaadmahmood), [ashishbhate](https://github.com/ashishbhate), [AshishDhama](https://github.com/AshishDhama), [avinashlng1080](https://github.com/avinashlng1080), [BenCookie95](https://github.com/BenCookie95), [BenLloydPearson](https://github.com/BenLloydPearson), [bobf7](https://github.com/bobf7), [calebroseland](https://github.com/calebroseland), [cedricstocke](https://github.com/cedricstocke), [CI-YU](https://github.com/CI-YU), [coltoneshaw](https://github.com/coltoneshaw), [ConorMacpherson](https://github.com/ConorMacpherson), [core](https://translate.mattermost.com/user/core), [cpoile](https://github.com/cpoile), [creeper-0910](https://github.com/creeper-0910), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [cybersmurf](https://github.com/cybersmurf), [d-wierdsma](https://github.com/d-wierdsma), [david.mach@mdsystem.cz](https://translate.mattermost.com/user/david.mach@mdsystem.cz), [devinbinnie](https://github.com/devinbinnie), [dfun90](https://github.com/dfun90), [dontoisme](https://github.com/dontoisme), [Eleferen](https://translate.mattermost.com/user/Eleferen), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [exbu](https://github.com/exbu), [florian-busch](https://github.com/florian-busch), [fmartingr](https://github.com/fmartingr), [fr0mdual](https://github.com/fr0mdual), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gbochora](https://github.com/gbochora), [geonmo](https://github.com/geonmo), [hamzaMM](https://github.com/hamzaMM), [hannaparks](https://github.com/hannaparks), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [icq4ever](https://translate.mattermost.com/user/icq4ever), [ifoukarakis](https://github.com/ifoukarakis), [iomodo](https://github.com/iomodo), [isacikgoz](https://github.com/isacikgoz), [ivenkwan](https://github.com/ivenkwan), [jasonblais](https://github.com/jasonblais), [javaguirre](https://github.com/javaguirre), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [jgilliam17](https://github.com/jgilliam17), [johndavidlugtu](https://github.com/johndavidlugtu), [johnsonbrothers](https://github.com/johnsonbrothers), [josephbaylon](https://github.com/josephbaylon), [jprusch](https://github.com/jprusch), [JtheBAB](https://github.com/JtheBAB), [JulienTant](https://github.com/JulienTant), [julmondragon](https://github.com/julmondragon), [justinegeffen](https://github.com/justinegeffen), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [KazminM](https://github.com/KazminM), [kevfocke](https://github.com/kevfocke), [koox00](https://github.com/koox00), [kostaspt](https://github.com/kostaspt), [krisfremen](https://github.com/krisfremen), [krmh04](https://github.com/krmh04), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [kwiersgalla](https://github.com/kwiersgalla), [kyeongsoosoo](https://github.com/kyeongsoosoo), [larkox](https://github.com/larkox), [levb](https://github.com/levb), [li11amy](https://github.com/li11amy), [lieut-data](https://github.com/lieut-data), [luc-ass](https://github.com/luc-ass), [lynn915](https://github.com/lynn915), [m-ripper](https://github.com/m-ripper), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [m1lt0n](https://github.com/m1lt0n), [majo](https://translate.mattermost.com/user/majo), [manojmalik20](https://github.com/manojmalik20), [maruTA-bis5](https://github.com/maruTA-bis5), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-src](https://github.com/matthew-src), [matthew-w](https://translate.mattermost.com/user/matthew-w), [mdsystem](https://github.com/mdsystem), [mhd-sln](https://github.com/mhd-sln), [michelengelen](https://github.com/michelengelen), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [mirshahriar](https://github.com/mirshahriar), [misaka10843](https://github.com/misaka10843), [mkraft](https://github.com/mkraft), [munish7771](https://github.com/munish7771), [mylonsuren](https://github.com/mylonsuren), [neallred](https://github.com/neallred), [neflyte](https://github.com/neflyte), [nevyangelova](https://github.com/nevyangelova), [nickmisasi](https://github.com/nickmisasi), [Nityanand13](https://github.com/Nityanand13), [noxer](https://github.com/noxer), [NuriInfos_JSK](https://translate.mattermost.com/user/NuriInfos_JSK), [nydhy](https://github.com/nydhy), [ogi-m](https://github.com/ogi-m), [oh6hay](https://github.com/oh6hay), [okias](https://github.com/okias), [oleksandr-kucheriavyi](https://github.com/oleksandr-kucheriavyi), [phuoc94](https://github.com/phuoc94), [pjenicot](https://github.com/pjenicot), [plant99](https://github.com/plant99), [potatogim](https://github.com/potatogim), [pvev](https://github.com/pvev), [Rajat-Dabade](https://github.com/Rajat-Dabade), [rimakan](https://github.com/rimakan), [ronzim](https://github.com/ronzim), [Roy-Orbison](https://github.com/Roy-Orbison), [sadohert](https://github.com/sadohert), [safakkizkin](https://github.com/safakkizkin), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [SeoJoonsoo](https://github.com/SeoJoonsoo), [seoyeongeun](https://github.com/seoyeongeun), [Sharuru](https://github.com/Sharuru), [simcard0000](https://github.com/simcard0000), [sinansonmez](https://github.com/sinansonmez), [Sjazz](https://github.com/Sjazz), [sonichigo](https://github.com/sonichigo), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [stevemudie](https://github.com/stevemudie), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [tboulis](https://github.com/tboulis), [tintou](https://github.com/tintou), [trilopin](https://github.com/trilopin), [tsabi](https://github.com/tsabi), [varghesejose2020](https://github.com/varghesejose2020), [vish9812](https://github.com/vish9812), [wgshtg](https://github.com/wgshtg), [wiggin77](https://github.com/wiggin77), [witjem](https://github.com/witjem), [worldworm](https://github.com/worldworm), [wuwinson](https://github.com/wuwinson), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [zeraussiul](https://github.com/zeraussiul), [zygfryd](https://github.com/zygfryd)

## Release v7.7 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

- **v7.7.4, released 2023-04-12**
  - Mattermost v7.7.4 contains medium level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
- **v7.7.3, released 2023-03-17**
  - Mattermost v7.7.3 contains a high severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
- **v7.7.2, released 2023-03-01**
  - Mattermost v7.7.2 contains medium to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - [Message Priority & Acknowledgement](https://docs.mattermost.com/configure/site-configuration-settings.html#message-priority) is now enabled by default for all instances. You may disable this feature in the System Console by going to **Posts > Message Priority** or via the config ``PostPriority`` setting.
  - Fixed an issue where threads were not marked as unread in the Threads view.
  - Fixed an issue where the server sent a wrong badge number when marking a message as unread in a Direct Message channel.
  - Fixed an issue where the Team edition returned a 400 Bad request for attempts to check CWS availability.
  - Fixed an issue where file uploading would appear "stuck" in processing state.
  - Fixed an issue where the Shared Channels feature wasn't properly included in the Professional license.
- **v7.7.1, released 2023-01-20**
  - Fixed an issue that prevented the creation of the initial admin user for new servers [MM-49720](https://mattermost.atlassian.net/browse/MM-49720).
  - Fixed an issue where the Top Channels for Insights didn't show results if the current user's configured timezone wasn't present in MySQL's ``mysql.time_zone_name table`` [MM-49688](https://mattermost.atlassian.net/browse/MM-49688).
- **v7.7.0, released 2023-01-16**
  - Original 7.7.0 release

Mattermost v7.7.0 contains low severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Important Upgrade Notes

 - Plugins with a webapp component may need to be updated to work with Mattermost v7.7 release and the updated ``React v17`` dependency. 
 	- This is to avoid plugins crashing with an error about ``findDOMNode`` being called on an unmounted component. While our [starter template](https://github.com/mattermost/mattermost-plugin-starter-template) depended on an external version of ``React``, it did not do the same for ``ReactDOM``. Plugins need to update their ``webpack.config.js`` directives to externalize ``ReactDOM``. For reference, see https://github.com/mattermost/mattermost-plugin-playbooks/pull/1489. Server-side only plugins are unaffected. This change can be done for existing plugins any time prior to upgrading to Mattermost v7.7 and is backwards compatible with older versions of Mattermost. If you run into issues, you can either enable ``ExperimentalSettings.PatchPluginsReactDOM`` or just disable the affected plugin while it's updated.
 - Denormalized ``Threads`` table by adding the ``ThreadTeamId`` column. See details for schema changes in the [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).
 - Starting with the Calls version shipping with v7.7, there's now a minimum version requirement when using the external RTCD service. This means that if Calls is configured to use the external service, customers need to upgrade RTCD first to at least version 0.8.0 or the plugin will fail to start.

**IMPORTANT:** If you upgrade from a release earlier than v7.5, please read the other [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).

### Compatibility
 - Updated the minimum version of MacOS to 11+.

### Highlights

#### Calls
 - [Audio calling and screen sharing](https://docs.mattermost.com/configure/calls-deployment.html) in channels is now generally available to all Mattermost customers.
 - Updated [the keyboard shortcut](https://docs.mattermost.com/channels/keyboard-shortcuts-for-channels.html#calls-shortcuts) to start and join calls.
 - Please see [the docs](https://docs.mattermost.com/configure/plugins-configuration-settings.html#calls) for additional details on configuration setting updates.

#### Boards
 - Boards now supports [file attachments](https://docs.mattermost.com/boards/work-with-cards.html#attach-files), including PDFs, images, videos, and any other file types.
 - Users can now [drag and drop boards and categories](https://docs.mattermost.com/boards/navigate-boards.html#manage-boards-on-the-sidebar) on the sidebar and organize them in any order they prefer.
 - The [template picker](https://docs.mattermost.com/boards/work-with-boards.html#choose-a-board-template) has been improved to make it easier for users to find the best template for their project.
 
#### Playbooks
 - Added an option to [run playbooks](https://docs.mattermost.com/playbooks/work-with-playbooks.html#runs-and-channel-behavior) without creating a new channel every time in order to reduce the unnecessary overhead.
 - In addition to the daily digest, users can now also view [a task inbox](https://docs.mattermost.com/playbooks/work-with-tasks.html#task-inbox) from the global header bar while in Playbooks.

#### Message Priority and Acknowledgments
 - Added [message priority labels](https://docs.mattermost.com/channels/message-priority.html) to the Threads view.
 - Added support for users to request acknowledgements on posts and to acknowledge posts (Professional license).

#### Global Drafts
 - Added [a centralized Drafts view](https://docs.mattermost.com/channels/send-messages.html#draft-messages) for draft messages.
 
#### ServiceNow Integration
 - ServiceNow customers can now access and share their ServiceNow data from within Mattermost.
 
#### ServiceNow Virtual Agent Integration
 - The [Mattermost ServiceNow Virtual Agent Integration](https://mattermost-2.wistia.com/medias/ixvgukv2qf) makes it easy for employees and customers to resolve issues fast.
 
#### GitLab Playbooks Integration
 - Through the updated [GitLab integration and playbook task actions](https://mattermost.com/marketplace/gitlab-plugin/), teams can automate release management processes to help increase efficiency and reduce errors.

### Improvements

#### User Interface (UI)
 - Implemented progressive image loading in the webapp.
 - When the "Custom Brand Text" is left blank with custom branding enabled, the default text is now hidden.
 - The **Mark as Unread** option was added to the **More** (...) menu for channels in the left-hand side sidebar. Pressing Alt while selecting a channel on the left-hand side now also marks the last post in the channel as unread.
 - Channel members are now able to remove themselves from a channel via the right-hand side channel members list.
 - Removed video check to allow the browser to decide what video types it can play.
 - Added a tooltip to the right-hand side files filter icon.
 - The number of users that can be added to a user group at once was increased to 256.
 - Keyboard and focus handling was improved in profile popovers and @mentions.
 - Updated prepackaged version of plugins affected by React 17 upgrade.
 - Updated the **Remove license and download** text in-product to clarify that server will be downgraded to Mattermost Free as a result.
 - Updated prepackaged NPS version to 1.3.1.
 - Updated in-product confirmation modal for ``@here`` mentions to clarify that people & timezone counts don't include the current user.
 - Downgraded French language support to Beta.

#### Administration
 - If an Admin encounters an invitation error “SMTP is not configured in System Console", a link to the SMTP configuration within the **System Console** is now included in the error message.
 - Crashing jobs now sets the job status to "failed".
 - Optimized ``ThreadStore.MarkAllAsUnreadByTeam``.
 - SQL migrations for PostgreSQL will now filter by the current schema name when checking for information from the ``information_schema.columns`` view. This does not affect anything because usually there's only one installation in a given database, but this gives flexibility to users to store multiple Mattermost instances under a single database.
 - **My Insights** was added to the Free plan.
 - Team scheme APIs are now allowed to be administered with a Professional plan.
 - A global banner as well as a notice banner are displayed to admins on the **Invite** modal and on **System Console > Site Statistics > Total Activated Users** page when the workspace exceeds the maximum number of users allowed. If the number of actual users exceeds the number of paid users by less than 5%, the banner is dismissible. If the number of actual users exceeds the number of paid users by more than 10%, the banner is non-dismissible until the license seat count has been updated.
 - For admins to see if the amount of users exceeds the license seats, a warning is now shown in the **System Console > Team Statistics** page.
 - Added a new menu item on the **System Console > Users** page that re-adds users to all of their default teams and channels associated with the groups they're a member of.
 - Added ``acknowledgements`` field to the post's metadata.
 - Added support for product websocket messages on high availability instances.
 - The import job now logs the progress of the import.
 - Exports to S3 no longer time out.
 - Shared Channels (Experimental) was moved to Professional license.

### Bug Fixes
 - Fixed an issue where custom group actions were appearing in the user interface even when the user didn't have the permissions for them.
 - Fixed issues with branding in email notifications.
 - Fixed an issue where text could be dragged and dropped into input-fields.
 - Fixed an issue where the profile popover failed to dismiss when selecting one of the options from the popover.
 - Fixed an issue where imports containing the team name with the wrong capitalization crashed the import job.
 - Fixed an issue where ``getPostSince`` didn't properly return deleted posts when Collapsed Reply Threads was enabled.
 - Fixed an issue where the screen reader did not announce emojis from the autocomplete list.
 - Fixed an issue where the scroll position in a channel was not maintained when opening reply message permalinks.
 - Fixed an issue where ``OwnerId`` was not set for bots created via ``EnsureBotUser``.
 - Fixed an issue where exports did not contain favorited Direct Message channels.
 - Fixed an issue where screen readers did not announce search results on the **Invite members to channel** modal.
 - Fixed an issue where screen readers did not announce the status of the user when hovering over the user status icon.
 - Fixed an issue where users with narrow screens could not see the **Profile Settings** section within the **Settings** modal.
 - Fixed an issue where users were unable to access the **Create an account** option on narrow screens.
 - Fixed an issue where users on desktop were unable to grab the vertical scroll bar without accidently resizing the window.
 - Fixed an issue where special characters weren't allowed in group mention names.
 - Fixed an issue where screen readers didn't read the **Switch Channels** modal header.
 - Fixed an issue in OAuth services where malformed redirect URLs were generated if the registered callback URLs already had static query parameters.
 - Fixed an issue where suggestion dividers were displayed as undefined.
 - Fixed an issue where a blank message was displayed in threads if the leave/join messages were disabled.
 - Fixed an issue where threads would appear duplicated in the Threads view after leaving a channel.
 - Fixed an issue with email search when using a PostgreSQL database.
 - Fixed an issue where message drafts were not saved after pasting them into the post textbox.
 - Fixed an issue where the team name in the channel sidebar header was not accessible.
 - Fixed an issue where users were unable to open the user's profile popover from the channel members list in the right panel.
 - Fixed an issue where the OAuth 2.0 deprecation notice was still displayed in the system console.
 - Fixed an issue where clicking on a reply post time stamp in the global threads inbox opened two right-hand side panels.
 - Fixed an issue where batch notifications failed while rendering.
 - Prevented browsers and CDNs from caching remote entrypoint files.
 - Fixed an issue where the unreads button in the channel sidebar was missing alternative text for screen readers.
 - Fixed a potential read-after-write issue when uploading data through the resumable uploads API.
 - Removed duplicate text in the self-hosted pricing modal.
 - Fixed the position of the Boards icon in the app bar when Boards is running without a plugin.
 - Fixed ability to create a board when Boards is running without a plugin.
 - Fixed Boards tour tips not appearing when Boards is running without a plugin.
 - Fixed an issue where a confusing System Console banner was displayed when a license was set to expire.
 - Fixed an issue where screen readers did not announce selected state of the sidebar submenu items.
 - Fixed an issue where servers with an encrypted key did not throw an error during startup.
 - Fixed an issue where the **Test Connection** button in **System Console > Environment > Elasticsearch** did not correctly take the right config settings specified in the page. Earlier, it would always take the previously saved config.

### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:
 - Under ``ServiceSettings`` in the ``config.json``:
    - ``PostPriority``, to add an option to select a message priority label for root posts.
    - ``AllowSyncedDrafts``, to add an option to display a centralized page for draft messages.
    - ``SelfHostedPurchase``, to add an option for self-hosted admins to purchase licenses in-app.
 - Under ``ExperimentalSettings`` in the ``config.json``:
    - ``PatchPluginsReactDOM``, to enable the patching of the React DOM library when loading web app plugins so that the plugin uses the version matching the web app.

### API Changes
 - The resumable uploads API was exposed to plugins.
 - Added a new API endpoint ``POST /api/v4/ldap/users/:user_id/group_sync_memberships`` to add (or re-add) users to all of their default teams and channels for all of the groups they're a member of.
 - Added two new URL parameters to the ``GET /api/v4/groups`` endpoint to get the ``ChannelMemberCount`` for a group.
 - Added new API endpoints ``POST /api/v4/users/:user_id/posts/:post_id/ack`` and ``DELETE /api/v4/users/:user_id/posts/:post_id/ack``.
 - Added a new API endpoint ``POST /api/v4/groups/:group_id:/restore``.
 - Added an allowed value ``sort=display_name`` to ``GET /api/v4/users?in_group=<groupid>``.
 - Added a new endpoint ``api/v4/cloud/products/selfhosted``.
 - A new API method ``RegisterCollectionAndTopic(collectionType, topicType string) (error)`` was added to the Plugin API and the following hooks. This API method is in beta, subject to change, and not covered by our backwards compatibility guarantee.
    - ``UserHasPermissionToCollection(c *Context, userID, collectionType, collectionId string, permission *model.Permission) (bool, error)``
    - ``GetAllCollectionIDsForUser(c *Context, userID, collectionType string) ([]string, error)``
    - ``GetAllUserIdsForCollection(c *Context, collectionType, collectionID string) ([]string, error)``
    - ``GetTopicRedirect(c *Context, topicType, topicID string) (string, error)``
    - ``GetCollectionMetadataByIds(c *Context, collectionType string, collectionIds []string) (map[string]model.CollectionMetadata, error)``
    - ``GetTopicMetadataByIds(c *Context, topicType string, topicIds []string) (map[string]*model.TopicMetadata, error)``

### Database Changes
 - Added a new Database table ``PostAcknowledgements``.
 
### Websocket Event Changes
 - Added new websocket events ``post_acknowledgement_added`` and ``post_acknowledgement_removed``.

### Go Version
 - v7.7 is built with Go ``v1.18.1``.

### Known Issues
 - Your profile image moves up when changing your status manually [MM-49159](https://mattermost.atlassian.net/browse/MM-49159).
 - The new Insights feature has some performance costs that we are working to optimize. This feature can be disabled by setting the ``MM_FEATUREFLAGS_INSIGHTSENABLED`` environment variable to ``false``.
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in high availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in high availability mode.
 - Boards are not refreshing on creation. See the [GitHub discussion](https://github.com/mattermost/focalboard/discussions/1971) for more information.
 - Boards export and reimport results in duplicates boards because all IDs are replaced by new ones on the server. See the [GitHub issue](https://github.com/mattermost/focalboard/issues/1924) for more information.
 - Boards linked to a channel you're a member of do not automatically appear on your sidebar unless you're an explicit member of the board. As a workaround, you can access the board from the channel RHS or by searching for the board via the board switcher (Ctrl/Cmd+K). Alternatively, you can ask the board admin to add you to the board as an explicit member. See the [issue-focalboard-4179](https://github.com/mattermost/focalboard/issues/4179) for more details.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.
 - If a user is not a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels or remove those channels from the run configuration.
 
### Contributors
 - [abhijit-singh](https://github.com/abhijit-singh), [AbhinavVihan](https://github.com/AbhinavVihan), [adithyaakrishna](https://github.com/adithyaakrishna), [aeomin](https://github.com/aeomin), [Afsoon](https://github.com/Afsoon), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [aiden](https://translate.mattermost.com/user/aiden), [alauregaillard](https://github.com/alauregaillard), [alexkuryshko](https://github.com/alexkuryshko), [alexpjohnson](https://github.com/alexpjohnson), [alzee](https://github.com/alzee),  [Amin913](https://github.com/Amin913), [amitpatelx3](https://github.com/amitpatelx3), [amyblais](https://github.com/amyblais), [amynicol1985](https://github.com/amynicol1985), [andrewbrown00](https://github.com/andrewbrown00), [andrewwutw](https://github.com/andrewwutw), [anurag6713](https://github.com/anurag6713), [ariyonaty](https://github.com/ariyonaty), [arjitc](https://github.com/arjitc), [asaadmahmood](https://github.com/asaadmahmood), [ashishbhate](https://github.com/ashishbhate), [AshishDhama](https://github.com/AshishDhama), [avas27JTG](https://github.com/avas27JTG), [avinashlng1080](https://github.com/avinashlng1080), [axilleas](https://github.com/axilleas), [ayrotideysarkar](https://github.com/ayrotideysarkar), [ayusht2810](https://github.com/ayusht2810), [azigler](https://github.com/azigler), [babinderrathi](https://github.com/babinderrathi), [ballista01](https://github.com/ballista01), [batebobo](https://github.com/batebobo), [belope](https://github.com/belope), [BenCookie95](https://github.com/BenCookie95), [BenLloydPearson](https://github.com/BenLloydPearson), [bpodwinski](https://github.com/bpodwinski), [calebroseland](https://github.com/calebroseland), [cecilysullivan](https://github.com/cecilysullivan), [ChandanChainani](https://github.com/ChandanChainani), [chay](https://translate.mattermost.com/user/chay), [CI-YU](https://github.com/CI-YU), [cinlloc](https://github.com/cinlloc), [coltoneshaw](https://github.com/coltoneshaw), [ConorMacpherson](https://github.com/ConorMacpherson), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [cs4p](https://github.com/cs4p), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [cyrilzhang-mm](https://github.com/cyrilzhang-mm), [d-wierdsma](https://github.com/d-wierdsma), [developbit](https://github.com/developbit), [devinbinnie](https://github.com/devinbinnie), [dfun90](https://translate.mattermost.com/user/dfun90), [Drishti-jain21](https://github.com/Drishti-jain21), [DSchalla](https://github.com/DSchalla), [dsharma522](https://github.com/dsharma522), [dylanrichards](https://github.com/dylanrichards), [ehsandiary](https://github.com/ehsandiary), [Eleferen](https://translate.mattermost.com/user/Eleferen), [ellisonleao](https://github.com/ellisonleao), [emmyni](https://github.com/emmyni), [enahum](https://github.com/enahum), [EricssonLiu](https://github.com/EricssonLiu), [esethna](https://github.com/esethna), [Eugene-grb](https://github.com/Eugene-grb), [Fjoerfoks](https://github.com/Fjoerfoks), [fmartingr](https://github.com/fmartingr), [furqanmlk](https://github.com/furqanmlk), [gabor-boros](https://github.com/gabor-boros),  [gabrieljackson](https://github.com/gabrieljackson), [gbochora](https://github.com/gbochora), [Genei180](https://github.com/Genei180), [Gitnube](https://github.com/Gitnube), [gkech](https://github.com/gkech), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [henry-shxu](https://github.com/henry-shxu), [hereje](https://github.com/hereje), [hionay](https://github.com/hionay), [hmhealey](https://github.com/hmhealey), [hokandil](https://github.com/hokandil), [homerCOD](https://github.com/homerCOD), [Hunter-Thompson](https://github.com/Hunter-Thompson), [idChef](https://github.com/idChef), [ifoukarakis](https://github.com/ifoukarakis), [Inutit](https://translate.mattermost.com/user/Inutit), [iomodo](https://github.com/iomodo),  [irdiOL](https://github.com/irdiOL), [isacikgoz](https://github.com/isacikgoz), [ivenkwan](https://translate.mattermost.com/user/ivenkwan), [iyampaul](https://github.com/iyampaul), [JakobMiksch](https://github.com/JakobMiksch), [javaguirre](https://github.com/javaguirre), [jecepeda](https://github.com/jecepeda), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [jgilliam17](https://github.com/jgilliam17), [johnsonbrothers](https://github.com/johnsonbrothers), [jordanafung](https://github.com/jordanafung), [josephbaylon](https://github.com/josephbaylon), [jprusch](https://github.com/jprusch), [JtheBAB](https://github.com/JtheBAB), [jufab](https://github.com/jufab), [JulienTant](https://github.com/JulienTant), [julmondragon](https://github.com/julmondragon), [justinegeffen](https://github.com/justinegeffen), [jwilander](https://github.com/jwilander), [k4awon](https://github.com/k4awon), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [kamre](https://github.com/kamre), [Kaorw](https://github.com/Kaorw), [kelderek](https://github.com/kelderek), [koox00](https://github.com/koox00), [kostaspt](https://github.com/kostaspt), [krisfremen](https://github.com/krisfremen), [krmh04](https://github.com/krmh04), [ksankeerth](https://github.com/ksankeerth), [kyeongsoosoo](https://github.com/kyeongsoosoo), [larkox](https://github.com/larkox), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [ludovicobesana](https://github.com/ludovicobesana), [lynn915](https://github.com/lynn915), [m-ripper](https://github.com/m-ripper), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [m1lt0n](https://github.com/m1lt0n), [maddy8381](https://github.com/maddy8381), [majo](https://translate.mattermost.com/user/majo), [manhdd610](https://translate.mattermost.com/user/manhdd610), [Manishpandey11](https://github.com/Manishpandey11), [manojmalik20](https://github.com/manojmalik20), [marianunez](https://github.com/marianunez), [maruTA-bis5](https://translate.mattermost.com/user/maruTA-bis5), [master7](https://translate.mattermost.com/user/master7), [mastersb](https://github.com/mastersb), [matt-w99](https://github.com/matt-w99), [matthew-src](https://github.com/matthew-src), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [mattlam88](https://github.com/mattlam88), [metanerd](https://github.com/metanerd), [mgdelacroix](https://github.com/mgdelacroix), [mhd-sln](https://github.com/mhd-sln), [michaelgamble](https://github.com/michaelgamble), [michelengelen](https://github.com/michelengelen), [michkrej](https://github.com/michkrej), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [mirshahriar](https://github.com/mirshahriar), [mkraft](https://github.com/mkraft), [Mshahidtaj](https://github.com/Mshahidtaj), [munish7771](https://github.com/munish7771), [muratbayan](https://github.com/muratbayan), [mvitale1989](https://github.com/mvitale1989), [mylonsuren](https://github.com/mylonsuren), [nab-77](https://github.com/nab-77), [naggie](https://github.com/naggie), [nathanaelhoun](https://github.com/nathanaelhoun), [neallred](https://github.com/neallred), [neflyte](https://github.com/neflyte), [nevyangelova](https://github.com/nevyangelova), [nickmisasi](https://github.com/nickmisasi), [noxer](https://github.com/noxer), [NuriInfos_JSK](https://translate.mattermost.com/user/NuriInfos_JSK), [ogi-m](https://github.com/ogi-m), [oh6hay](https://github.com/oh6hay), [PhilippeWeidmann](https://translate.mattermost.com/user/PhilippeWeidmann), [phoinixgrr](https://github.com/phoinixgrr), [Pinjasaur](https://github.com/Pinjasaur), [pjenicot](https://github.com/pjenicot), [plant99](https://github.com/plant99), [potatogim](https://github.com/potatogim), [prashant-15](https://github.com/prashant-15), [PSyton](https://github.com/PSyton), [pvev](https://github.com/pvev), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [Rajat-Dabade](https://github.com/Rajat-Dabade), [redhoyasa](https://github.com/redhoyasa), [remyj38](https://translate.mattermost.com/user/remyj38), [RoyI99](https://github.com/RoyI99), [s4kh](https://github.com/s4kh),[sadohert](https://github.com/sadohert), [sarz4fun](https://translate.mattermost.com/user/sarz4fun), [saturninoabril](https://github.com/saturninoabril), [satya-vinay](https://github.com/satya-vinay), [sbishel](https://github.com/sbishel), [seowglen](https://github.com/seowglen), [seoyeongeun](https://github.com/seoyeongeun), [sgmadankar](https://translate.mattermost.com/user/sgmadankar), [ShajithaMohammed](https://github.com/ShajithaMohammed), [simcard0000](https://github.com/simcard0000), [sinansonmez](https://github.com/sinansonmez), [sk409](https://github.com/sk409), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [srkgupta](https://github.com/srkgupta), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [sumanpaikdev](https://github.com/sumanpaikdev), [svbnbyrk](https://github.com/svbnbyrk), [tanmay-des](https://github.com/tanmay-des), [tboulis](https://github.com/tboulis), [tiagocorreiaalmeida](https://github.com/tiagocorreiaalmeida), [toomore](https://github.com/toomore), [trilopin](https://github.com/trilopin), [tsabi](https://github.com/tsabi), [varghesejose2020](https://github.com/varghesejose2020), [varunKT001](https://github.com/varunKT001), [VictorAssunc](https://github.com/VictorAssunc), [vish9812](https://github.com/vish9812), [vitorcruzfaculdade](https://github.com/vitorcruzfaculdade), [vivekkj123](https://github.com/vivekkj123), [wget](https://translate.mattermost.com/user/wget), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [WilliamLongKing](https://github.com/WilliamLongKing), [Willyfrog](https://github.com/Willyfrog), [witjem](https://github.com/witjem), [wuwinson](https://github.com/wuwinson), [Yakikim](https://github.com/Yakikim), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yegorov-p](https://github.com/yegorov-p), [zefhemel](https://github.com/zefhemel), [ziriuz84](https://github.com/ziriuz84), [zuhairHussain](https://github.com/zuhairHussain), [ZurabBalamtsarashvili](https://github.com/ZurabBalamtsarashvili)

## Release v7.6 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

  - The Mattermost v7.6 release has been cancelled as we are working on investigating performance issues. The next scheduled release is v7.7 in January 16th, 2023.

## Release v7.5 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

- **v7.5.2, released 2022-12-21**
  - Mattermost v7.5.2 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where email notifications looked broken when email batching was enabled [MM-48521](https://mattermost.atlassian.net/browse/MM-48521).
  - Updated prepackaged Boards version to 7.5.4.
  - Updated prepackaged NPS version to 1.3.1.
- **v7.5.1, released 2022-11-16**
  - Fixed an upgrade issue affecting servers on Ubuntu v18.04.
- **v7.5.0, released 2022-11-16**
  - Original 7.5.0 release

Mattermost v7.5.0 contains a medium severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Important Upgrade Notes

 - Adds a new schema migration to ensure ``ParentId`` column is dropped from the ``Posts`` table. Depending on the table size, if the column is not dropped before, a significant spike in database CPU usage is expected on MySQL databases. Writes to the table will be limited during the migration.
 - For ``PluginRegistry.registerCustomRoute``, when you register a custom route component, you must specify a CSS ``grid-area`` in order for it to be placed properly into the root layout (recommended: ``grid-area: center``).

**IMPORTANT:** If you upgrade from a release earlier than v7.4, please read the other [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).

### Compatibility
 - Updated the minimum version of Chrome and Edge to v106+.

### Highlights

#### Calls
 - Added new message threads with emoji reactions and @mentions to calls. After joining a call, expand the widget to the window mode, and then select the comment button to access the real-time message thread in the right-hand sidebar.

#### Boards
 - Added additional standard [board templates](https://docs.mattermost.com/boards/work-with-boards.html#choose-a-board-template) to help users kick-off their next projects.
 - Filters now support all [text properties](https://docs.mattermost.com/boards/work-with-cards.html#work-with-property-types).
 - Added two new tiles for System Console [Boards metrics](https://docs.mattermost.com/configure/reporting-configuration-settings.html#site-statistics) under **System Console > Site Statistics**.
 
#### Last active status
 - Added a [“Last active” status](https://docs.mattermost.com/channels/channels-settings.html#share-last-active-time) to the profile popover and to the **Direct Message** channel header that indicates when a user was last online. This status only displays for users who are Away, Offline, or in do-not-disturb (DND). This can be disabled via **Settings > Display > Share last active time**.

### Improvements

#### User Interface (UI)
 - Renamed "Starter" plan to "Free" plan in product.
 - Added a new grid-based layout to the right-hand side and globalized the right-hand side and the Apps Bar.
 - A confirmation modal is now displayed before a user marks all threads as read.
 - Added the ability to hide the “required” asterisk in the App Field.
 - Added a fading effect to the Apps Modal body while an Apps Modal is refreshing.
 - Insights now filters out posts made by plugins and OAuth apps.
 - Added a shortcut ``Ctrl/Cmd + Shift + U`` to filter channels by unread.
 - The default number of **Direct Message** channels shown in the sidebar is now 40.
 - Added Insights to the channel switcher.
 - Added a button to easily copy the content of text or code files in file previews.
 - The team unread icon for muted channels is now hidden in the sidebar.
 - Added the ability to create a new channel along with a new board associated with the created channel.
 - Added markdown formatting for hyperlinks when pasted into the text editor.
 - Email notifications from new messages now also support displaying Slack attachments from the channel post.
 - Updated NPS plugin to version 1.3.0.
 - Downgraded Bulgarian, Persian, and Simplified Chinese language support to Alpha.

#### Administration
 - After 90 days since missing a payment, admins will see a modal where they can choose between updating the billing status or staying on the Free subscription.
 - Autocomplete results using Elasticsearch or Bleve will correctly show a user as a channel member in direct message and group message channels. To force this change to appear, a re-indexing will be necessary.
 - Introduced an **Invite Guests** prompt to self-hosted.
 - Added JSON-compatible nested configuration value parsing from environment variables.
 - An AD/LDAP prompt banner is now shown for self-hosted instances with a Professional license when visiting the invite guests modal.
 - Self-hosted Admins now see "User Groups" in the product switcher with a call to action (CTA) to start a trial.
 - Added logic to package product version of Boards with production builds.

### Bug Fixes
 - Fixed an issue where Enterprise features labeled as "Professional Feature" appeared in the **System Console** sidebar.
 - Fixed an issue where the transparency for PNG images in image previews and thumbnails was not preserved.
 - Fixed an issue where screen readers failed to announce “No results found” in the direct message modal.
 - Fixed an issue where minipreview data was not generated nor stored for images imported from Slack.
 - Fixed the error message that appears on the **Reset Password** page when inputting a password with fewer than five characters.
 - Fixed an issue where ``Get categories`` with the "exclude" option did not return categories for deleted teams a user was no longer a member of.
 - Fixed an issue where a randomly-generated default message-ID wasn't added for every outgoing email.
 - Fixed an issue where custom groups could be created with @mention names that are reserved words (@channel, @here, @all).
 - Fixed an issue where 404 errors were shown when APIv4 had an incorrect content-type header.
 - Fixed an issue where messages from bots and webhooks could not be forwarded.
 - Fixed an issue where inline images did not appear in the channel header.
 - Fixed an issue with the emoji skin tone selector animation.
 - Fixed an issue where the screen reader did not announce a successful login when logging in.
 - Fixed a few broken links at **System Console > User Management > Permission Schemes**.
 - Fixed an issue where users were able to forward messages to users who are deactivated.
 - Fixed an issue where "Threads" were not shown in the unread filter view even if there weren't unread threads.
 - Fixed an issue where the user’s full name was not shown when adding people to a channel via the ``Add people`` modal.
 - Fixed an issue where formatting keyboard shortcuts were conflicting with existing shortcuts.
 - Fixed an issue where the markdown style for horizontal rules was too thick.
 - Fixed an issue where the emoji reaction overlay blocked part of the message it belonged to in compact view.
 - Fixed an issue with incorrect mention counts in unread channels.
 - Fixed an issue where the cursor displayed as a pointer instead of as an arrow in embedded YouTube preview images.
 - Fixed an issue where formatting was applied to selected spaces after a word.
 - Fixed an issue where screen readers did not announce that the channel interface language dropdown in **Settings > Display > Language > Change** is a dropdown.
 - Fixed a bug where role filters weren't being applied for ``GetProfilesInChannel``.
 - Fixed an issue where the guest onboarding checklist contained an “Invite team members” link as a tour point.
 - Fixed an issue where the **Enterprise license is expired** banner was non-dismissible.
 - Fixed an issue where the **Renew Now** option was not showing in-product and always defaulted to Contact Sales.
 - Fixed an issue where ``getPostSince`` didn't properly return deleted posts when Collapsed Reply Threads was enabled.
 - Fixed an issue where ``OwnerId`` was not set for bots created via ``EnsureBotUser``.

### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:
 - Under ``TeamSettings`` in the ``config.json``:
    - Added ``EnableLastActiveTime`` to add a **Last active** status to the profile popover and to the **Direct Message** channel header that indicates when a user was last online.

### API Changes
 - Added a new response-header ``First-Inaccessible-File-Time`` to the APIs fetching single file information.
 - Added a new query parameter to include deleted posts as long as it's requested by a system admin in ``/api/v4/channels/{channel_id}/posts``.
 - Added new plugin endpoints to ``PermissionService`` interface.

### Go Version
 - v7.5 is built with Go ``v1.18.1``.

### Known Issues
 - Guest users are unable to return to the login screen after being removed from all channels [MM-48438](https://mattermost.atlassian.net/browse/MM-48438).
 - Users are unable to open threads from recent mentions when switching to another team [MM-48399](https://mattermost.atlassian.net/browse/MM-48399).
 - When the right-hand side is expanded, an overlay is displayed with the Threads help text popup [MM-48412](https://mattermost.atlassian.net/browse/MM-48412).
 - The new Insights feature has some performance costs that we are working to optimize. This feature can be disabled by setting the ``MM_FEATUREFLAGS_INSIGHTSENABLED`` environment variable to ``false``.
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in high availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in high availability mode.
 - Boards are not refreshing on creation. See the [GitHub discussion](https://github.com/mattermost/focalboard/discussions/1971) for more information.
 - Boards export and reimport results in duplicates boards because all IDs are replaced by new ones on the server. See the [GitHub issue](https://github.com/mattermost/focalboard/issues/1924) for more information.
 - Boards linked to a channel you're a member of do not automatically appear on your sidebar unless you're an explicit member of the board. As a workaround, you can access the board from the channel RHS or by searching for the board via the board switcher (Ctrl/Cmd+K). Alternatively, you can ask the board admin to add you to the board as an explicit member. See the [issue-focalboard-4179](https://github.com/mattermost/focalboard/issues/4179) for more details.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.
 
### Contributors
 - [f2010126](https://translate.mattermost.com/user/f2010126/), [AbhinavVihan](https://github.com/AbhinavVihan), [adithyaakrishna](https://github.com/adithyaakrishna), [Aditya-Kapadiya](https://github.com/Aditya-Kapadiya), [adj2908](https://github.com/adj2908), [Afsoon](https://github.com/Afsoon), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [akhil-ghatiki](https://github.com/akhil-ghatiki), [alannatodd](https://github.com/alannatodd), [alauregaillard](https://github.com/alauregaillard), [alexkuryshko](https://translate.mattermost.com/user/alexkuryshko/), [alexpjohnson](https://github.com/alexpjohnson), [alzee](https://github.com/alzee), [amogh2019](https://github.com/amogh2019), [amyblais](https://github.com/amyblais), [andrewwutw](https://translate.mattermost.com/user/andrewwutw/), [angeloskyratzakos](https://github.com/angeloskyratzakos), [aniketh-varma](https://github.com/aniketh-varma), [AntiGhot](https://github.com/AntiGhot), [anwarchk](https://github.com/anwarchk), [anx-ag](https://github.com/anx-ag), [ashishbhate](https://github.com/ashishbhate), [AshishDhama](https://github.com/AshishDhama), [atlekbai](https://github.com/atlekbai), [ayrotideysarkar](https://github.com/ayrotideysarkar), [Azanul](https://github.com/Azanul), [azigler](https://github.com/azigler), [babinderrathi](https://github.com/babinderrathi), [batebobo](https://github.com/batebobo), [BediNimret](https://github.com/BediNimret), [BenCookie95](https://github.com/BenCookie95), [bpodwinski](https://translate.mattermost.com/user/bpodwinski/), [calebroseland](https://github.com/calebroseland), [cannalee90](https://github.com/cannalee90), [cecilysullivan](https://github.com/cecilysullivan), [chirag-ghosh](https://github.com/chirag-ghosh), [cinlloc](https://github.com/cinlloc), [codewithshariq](https://github.com/codewithshariq), [Conor0Callaghan](https://github.com/Conor0Callaghan), [ConorMacpherson](https://github.com/ConorMacpherson), [core](https://translate.mattermost.com/user/core/), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [cyberbuff](https://github.com/cyberbuff), [cyrilzhang-mm](https://github.com/cyrilzhang-mm), [d-wierdsma](https://github.com/d-wierdsma), [daniloff200](https://github.com/daniloff200), [den13501](https://github.com/den13501), [devinbinnie](https://github.com/devinbinnie), [devXprite](https://github.com/devXprite), [dibash](https://translate.mattermost.com/user/dibash/), [dibashthapa](https://github.com/dibashthapa), [Drishti-jain21](https://github.com/Drishti-jain21), [dsharma522](https://github.com/dsharma522), [Eleferen](https://translate.mattermost.com/user/Eleferen/), [emmyni](https://github.com/emmyni), [enahum](https://github.com/enahum), [enderahmetyurt](https://github.com/enderahmetyurt), [eraykisabacak](https://github.com/eraykisabacak), [erezo9](https://github.com/erezo9), [EricssonLiu](https://github.com/EricssonLiu), [ermanimer](https://github.com/ermanimer), [esethna](https://github.com/esethna), [EshaanAgg](https://github.com/EshaanAgg), [f2010126](https://github.com/f2010126), [Fanch](https://translate.mattermost.com/user/Fanch/), [Fjoerfoks](https://github.com/Fjoerfoks), [fmartingr](https://github.com/fmartingr), [francisco-core](https://github.com/francisco-core), [furqanmlk](https://github.com/furqanmlk), [gabor-boros](https://github.com/gabor-boros), [gabrieljackson](https://github.com/gabrieljackson), [gaston-flores](https://github.com/gaston-flores), [gbochora](https://github.com/gbochora), [gvlx](https://translate.mattermost.com/user/gvlx/), [hannaparks](https://github.com/hannaparks), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hawkril](https://github.com/hawkril), [henry-shxu](https://github.com/henry-shxu), [hereje](https://github.com/hereje), [hmhealey](https://github.com/hmhealey), [hmmmmmmm](https://github.com/hmmmmmmm), [hokandil](https://github.com/hokandil), [homerCOD](https://github.com/homerCOD), [ifoukarakis](https://github.com/ifoukarakis), [iogungbade](https://github.com/iogungbade), [iomodo](https://github.com/iomodo), [isacikgoz](https://github.com/isacikgoz), [javaguirre](https://github.com/javaguirre), [jeromegrosse](https://github.com/jeromegrosse), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [johndavidlugtu](https://github.com/johndavidlugtu), [johnsonbrothers](https://github.com/johnsonbrothers), [jordanafung](https://github.com/jordanafung), [joremysh](https://github.com/joremysh), [josephjosedev](https://github.com/josephjosedev), [josevcsouza](https://translate.mattermost.com/user/josevcsouza/), [joshalling](https://github.com/joshalling), [jprusch](https://github.com/jprusch), [JtheBAB](https://github.com/JtheBAB), [jufab](https://github.com/jufab), [JulienTant](https://github.com/JulienTant), [julmondragon](https://github.com/julmondragon), [justinegeffen](https://github.com/justinegeffen), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kamre](https://github.com/kamre), [kayazeren](https://github.com/kayazeren), [krisfremen](https://github.com/krisfremen), [krmh04](https://github.com/krmh04), [kscheel](https://github.com/kscheel), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [KuSh](https://github.com/KuSh), [kVarunkk](https://github.com/kVarunkk), [kyeongsoosoo](https://github.com/kyeongsoosoo), [larkox](https://github.com/larkox), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [lindy65](https://github.com/lindy65), [ludovicobesana](https://translate.mattermost.com/user/ludovicobesana/), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [m1lt0n](https://github.com/m1lt0n), [majo](https://translate.mattermost.com/user/majo/), 
[master7/](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-src](https://github.com/matthew-src), [matthew-w](https://translate.mattermost.com/user/matthew-w/), [matthewbirtch](https://github.com/matthewbirtch), [mgdelacroix](https://github.com/mgdelacroix), [mhd-sln](https://github.com/mhd-sln), [michelengelen](https://github.com/michelengelen), [michizhou](https://github.com/michizhou), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [misantron](https://github.com/misantron), [mukul-kr](https://github.com/mukul-kr), [munish7771](https://github.com/munish7771), [nab-77](https://github.com/nab-77), [nayane95](https://github.com/nayane95), [neallred](https://github.com/neallred), [neflyte](https://github.com/neflyte), [nevyangelova](https://github.com/nevyangelova), [nickmisasi](https://github.com/nickmisasi), [noxer](https://github.com/noxer), [oetiker](https://github.com/oetiker), [ogi-m](https://github.com/ogi-m), [oh6hay](https://github.com/oh6hay), [patatman](https://github.com/patatman), [phoinixgrr](https://github.com/phoinixgrr), [Phrynobatrachus](https://github.com/Phrynobatrachus), [pikami](https://github.com/pikami), [Pinjasaur](https://github.com/Pinjasaur), [plant99](https://github.com/plant99), [pvev](https://github.com/pvev), [rafaelrubbioli](https://github.com/rafaelrubbioli), [Rajat-Dabade](https://github.com/Rajat-Dabade), [RobBie1221](https://github.com/RobBie1221), [rolwin100](https://github.com/rolwin100), [RoyI99](https://github.com/RoyI99), [s4kh](https://github.com/s4kh), [saturninoabril](https://github.com/saturninoabril), [satya-vinay](https://github.com/satya-vinay), [sbishel](https://github.com/sbishel), [seanohue](https://github.com/seanohue), [seoyeongeun](https://translate.mattermost.com/user/seoyeongeun/), [shawnaym](https://github.com/shawnaym), [shikhar13012001](https://github.com/shikhar13012001), [simcard0000](https://github.com/simcard0000), [sinansonmez](https://github.com/sinansonmez), [sk409](https://github.com/sk409), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [srkgupta](https://github.com/srkgupta), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [Szymongib](https://github.com/Szymongib), [tboulis](https://github.com/tboulis), [thenishantsapkota](https://github.com/thenishantsapkota), [tilto0822](https://github.com/tilto0822), [TomerPacific](https://github.com/TomerPacific), [trilopin](https://github.com/trilopin), [tsabi](https://github.com/tsabi), [uravgkarthik](https://github.com/uravgkarthik), [varghesejose2020](https://github.com/varghesejose2020), [varunKT001](https://github.com/varunKT001), [vish9812](https://github.com/vish9812), [VishakhaPoonia](https://github.com/VishakhaPoonia), [vitorcruzfaculdade](https://github.com/vitorcruzfaculdade), [vivekkj123](https://github.com/vivekkj123), [Wetula](https://github.com/Wetula), [WhiteHsu](https://github.com/WhiteHsu), [wiggin77](https://github.com/wiggin77), [WilliamLongKing](https://github.com/WilliamLongKing), [Willyfrog](https://translate.mattermost.com/user/Willyfrog/), [wralith](https://github.com/wralith), [yakuter](https://github.com/yakuter), [Yordaniss](https://translate.mattermost.com/user/Yordaniss/), [zafar-hussain](https://github.com/zafar-hussain), [zefhemel](https://github.com/zefhemel)

## Release v7.4 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

- **v7.4.1, released 2022-12-21**
  - Mattermost v7.4.1 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Added a new schema migration to ensure ``ParentId`` column is dropped from the ``Posts`` table. Depending on the table size, if the column is not dropped before, a significant spike in database CPU usage is expected on MySQL databases. Writes to the table will be limited during the migration.
  - Updated prepackaged Boards version to 7.4.3.
- **v7.4.0, released 2022-10-16**
  - Original 7.4.0 release

Mattermost v7.4.0 contains a medium severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Highlights

#### Boards
 - Added new [board roles](https://docs.mattermost.com/boards/share-and-collaborate.html#roles), **Commenter** and **Viewer**.
 - Added [minimum default board roles](https://docs.mattermost.com/boards/share-and-collaborate.html#manage-team-access) to reduce permissioning ambiguity and to prevent security loopholes.
 - Added support for [guest accounts](https://docs.mattermost.com/onboard/guest-accounts.html).
 - Added the ability to add a team member to a board by selecting their name from [an autocomplete list](https://docs.mattermost.com/boards/work-with-cards.html#mention-people).
 - Added channel notifications for linked boards.
 - Added a new [multi-person property](https://docs.mattermost.com/boards/work-with-cards.html#work-with-property-types) to easily set multiple assignees or owners on a card.

#### Calls
 - Added new [keyboard shortcuts for Calls](https://docs.mattermost.com/channels/keyboard-shortcuts-for-channels.html#calls-shortcuts).

### Improvements

#### User Interface (UI)
 - Added a red destructive action color to the **Leave Channel** button in the channel header.
 - Downgraded Brazilian Portuguese and Romanian language support to Alpha.
 - Pre-packaged Playbooks v1.32.6.

#### Administration
 - A ``batchSize`` option has been added to the ``mattermost export`` CLI command to limit the number of items exported. By default, if it is not included, it exports all posts.
 - Added more context to the “Notify admin” feature to help Admins, such as who asked to upgrade, why they requested the upgrade, and how many people requested it.

### Bug Fixes
 - Fixed an issue with a nil point exception error during imports.
 - Fixed an issue where users were unable to download a [Support Packet](https://docs.mattermost.com/manage/generating-support-packet.html) using the Desktop App.
 - Fixed an issue with the **Message forward** modal where the auto-complete in the comment box moved with the text cursor.
 - Fixed an issue where muted channels with an at-mention were displayed under the **Unreads** section of the channel switcher.
 - Fixed an issue where the Collapsed Reply Threads setting was displayed in the **System Console > Experimental Features** section.
 - Fixed an issue with the badge count on the mobile app when a channel/thread was viewed.
 - Fixed an issue where typing ``@`` in the right-hand side rendered a cut-off user suggestion list.
 - Fixed an issue where an error screen was briefly flashed when the first Admin signed up into a new server.
 - Fixed an issue where users were unable to add Japanese comments correctly in the message **Forward** modal.
 - Fixed an issue where unsaved edits to a post were lost when switching channels or threads.
 - Fixed an issue on larger screen sizes where the Insights widgets were pushed to the side when the right-hand side was open.
 - Fixed an issue where the ability to forward messages from public channels wasn't possible when messaging someone directly for the first time.
 - Fixed an issue where custom emojis were sometimes not visible in **Insights > Top Reactions**.
 - Fixed an issue where channels with no posts within a particular timeframe didn't show in **Insights > Least Active Channel**.
 - Fixed an issue where the Channel Info right-hand side shortcut was not disabled in the Insights view.
 - Fixed an issue where an in-product link was missing from **Integrations > Bot Accounts > Add Bot Account**.
 - Reverted the new search of names in PostgreSQL using full text search introduced in v7.3.0 due to a performance regression.

### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:
 - Under ``ServiceSettings`` in ``config.json``:
    - Added ``EnableAPITriggerAdminNotifications`` to add an option to receive more context from the “Notify admin” feature to help Admins.

### API Changes
 - If ``EnableConfirmNotificationsToChannel`` is disabled, channel member counts by group API are no longer called.

### Websocket Event Changes
 - Added ``OmitConnection`` to the websocket broadcast parameters.

### Go Version
 - v7.4 is built with Go ``v1.18.1``.

### Known Issues
 - The **More** menu for Pinned posts on the right-hand side is cut-off [MM-46987](https://mattermost.atlassian.net/browse/MM-46987).
 - The new Insights feature has some performance costs that we are working to optimize. This feature can be disabled by setting the ``MM_FEATUREFLAGS_INSIGHTSENABLED`` environment variable to ``false``.
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - Boards are not refreshing on creation. See the [GitHub discussion](https://github.com/mattermost/focalboard/discussions/1971) for more information.
 - Boards export and reimport results in duplicates boards because all IDs are replaced by new ones on the server. See the [GitHub issue](https://github.com/mattermost/focalboard/issues/1924) for more information.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.
 
### Contributors
 - [abhijit-singh](https://github.com/abhijit-singh), [AbhinavVihan](https://github.com/AbhinavVihan), [adrian.lee](https://translate.mattermost.com/user/adrian.lee), [aerokite](https://github.com/aerokite), [Afsoon](https://github.com/Afsoon), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [alauregaillard](https://translate.mattermost.com/user/alauregaillard), [amyblais](https://github.com/amyblais), [amynicol1985](https://github.com/amynicol1985), [angeloskyratzakos](https://github.com/angeloskyratzakos), [anurag6713](https://github.com/anurag6713), [anx-ag](https://github.com/anx-ag), [asaadmahmood](https://github.com/asaadmahmood), [AshishDhama](https://github.com/AshishDhama), [azigler](https://github.com/azigler), [babinderrathi](https://github.com/babinderrathi), [BenCookie95](https://github.com/BenCookie95), [boahc077](https://github.com/boahc077), [bpodwinski](https://translate.mattermost.com/user/bpodwinski), [calebroseland](https://github.com/calebroseland), [catalintomai](https://github.com/catalintomai), [cecilysullivan](https://github.com/cecilysullivan), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [cyrilzhang-mm](https://github.com/cyrilzhang-mm), [d-wierdsma](https://github.com/d-wierdsma), [danielsischy](https://github.com/danielsischy), [darkLord19](https://github.com/darkLord19), [devinbinnie](https://github.com/devinbinnie), [dezerb](https://github.com/dezerb), [dontoisme](https://github.com/dontoisme), [edlerd](https://github.com/edlerd), [ehsan](https://translate.mattermost.com/user/ehsan), [enahum](https://github.com/enahum), [fmartingr](https://github.com/fmartingr), [frstier](https://github.com/frstier), [ftonato](https://github.com/ftonato), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gbochora](https://github.com/gbochora), [gvlx](https://github.com/gvlx), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [henry-shxu](https://github.com/henry-shxu), [hmhealey](https://github.com/hmhealey), [Hornet-Wing](https://github.com/Hornet-Wing), [info4pdv](https://github.com/info4pdv), [iomodo](https://github.com/iomodo), [jaskiratsingh2000](https://github.com/jaskiratsingh2000), [jasonblais](https://github.com/jasonblais), [javaguirre](https://github.com/javaguirre), [jespino](https://github.com/jespino), [Jio007](https://github.com/Jio007), [johnsonbrothers](https://github.com/johnsonbrothers), [josevcsouza](https://translate.mattermost.com/user/josevcsouza), [jprusch](https://github.com/jprusch), [JtheBAB](https://github.com/JtheBAB), [JulienTant](https://github.com/JulienTant), [julmondragon](https://github.com/julmondragon), [justinegeffen](https://github.com/justinegeffen), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [koox00](https://github.com/koox00), [ksankeerth](https://github.com/ksankeerth), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [lafriks](https://github.com/lafriks), [larkox](https://github.com/larkox), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [m1lt0n](https://github.com/m1lt0n), [majo](https://translate.mattermost.com/user/majo), [maruTA-bis5](https://github.com/maruTA-bis5), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [mehran-prs](https://github.com/mehran-prs), [metanerd](https://github.com/metanerd), [mgdelacroix](https://github.com/mgdelacroix), [michaelgamble](https://github.com/michaelgamble), [michelengelen](https://github.com/michelengelen), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [mjnagel](https://github.com/mjnagel), [mkraft](https://github.com/mkraft), [Mshahidtaj](https://github.com/Mshahidtaj), [munish7771](https://github.com/munish7771), [MusabShakeel576](https://github.com/MusabShakeel576), [mylonsuren](https://github.com/mylonsuren), [natalie-hub](https://github.com/natalie-hub), [neallred](https://github.com/neallred), [neflyte](https://github.com/neflyte), [nevyangelova](https://github.com/nevyangelova), [nickmisasi](https://github.com/nickmisasi), [noxer](https://github.com/noxer), [ogi-m](https://github.com/ogi-m), [orlandorode97](https://github.com/orlandorode97), [pejotu](https://github.com/pejotu), [pfltdv](https://github.com/pfltdv), [Phrynobatrachus](https://github.com/Phrynobatrachus), [Pinjasaur](https://github.com/Pinjasaur), [plant99](https://github.com/plant99), [potatogim](https://github.com/potatogim), [Rajat-Dabade](https://github.com/Rajat-Dabade), [rolwin100](https://github.com/rolwin100), [RoyI99](https://github.com/RoyI99), [safakkizkin](https://github.com/safakkizkin), [salmanmanekia](https://github.com/salmanmanekia), [SaptarshiSarkar12](https://github.com/SaptarshiSarkar12), [sashashura](https://github.com/sashashura), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [SelyanKab](https://github.com/SelyanKab), [shiken](https://translate.mattermost.com/user/shiken), [simcard0000](https://github.com/simcard0000), [sinansonmez](https://github.com/sinansonmez), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [Szymongib](https://github.com/Szymongib), [tboulis](https://github.com/tboulis), [tilto0822](https://translate.mattermost.com/user/tilto0822), [TMaYaD](https://github.com/TMaYaD), [trilopin](https://github.com/trilopin), [tsabi](https://github.com/tsabi), [urvesh20](https://github.com/urvesh20), [varghesejose2020](https://github.com/varghesejose2020), [vdvukhzhilov](https://github.com/vdvukhzhilov), [vetash](https://github.com/vetash), [vish9812](https://github.com/vish9812), [VishakhaPoonia](https://github.com/VishakhaPoonia), [wgshtg](https://github.com/wgshtg), [wiggin77](https://github.com/wiggin77), [yangyangdaji](https://github.com/yangyangdaji), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [zefhemel](https://github.com/zefhemel)

## Release v7.3 - [Feature Release](/upgrade/release-definitions.html#feature-release)

- **v7.3.1, released 2022-10-14**
  - Mattermost v7.3.1 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Reverted the new search of names in PostgreSQL using full text search introduced in v7.3.0 due to a performance regression.
- **v7.3.0, released 2022-09-16**
  - Original 7.3.0 release

Mattermost v7.3.0 contains a medium severity level security fix. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Important Upgrade Notes
 - Boards is moving from a channel-based to a role-based permissions system. The migration will happen automatically, but your administrator should perform a backup prior to the upgrade. We removed workspaces, so if you were a member of many boards prior to migration, they will now all appear under the same sidebar. Please see [this document](https://docs.mattermost.com/welcome/whats-new-in-v72.html) for more details.

**IMPORTANT:** If you upgrade from a release earlier than v7.2, please read the other [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).

### Highlights

#### Playbooks
 - Navigate between teams in Playbooks with the new team switcher.
 - Manage playbooks and runs in the new left-hand sidebar.
 - View the runs you're participating in or following in the **Runs** sidebar category, and view the playbooks you're a member of in the **Playbooks** sidebar category.
 - Favorite runs or playbooks to prioritize them in the **Favorites** category.
 - Participants now have access to every run feature on the new run details page.
 - Users can now request status updates (Professional).

#### Boards
 - All the boards you’re currently a member of from your current team will appear on the sidebar without needing to switch workspaces.
 - Organize boards on the sidebar with custom categories.
 - Press CTRL+K/CMD+K to find additional boards.
 - Navigate between teams in Boards with the new team switcher.
 - Set board and template permissions in the new **Share** setting.
 - Link boards to channels to automatically grant board permissions to channel members.
 - See [the documentation](/welcome/whats-new-in-v72.html) for more details.

#### Calls
 - Added support for standalone Calls server and Kubernetes (Enterprise).
 
#### New Insights Widgets
 - Added four new [Insights widgets](/welcome/insights.html): Most Active Direct Messages, Least Active Channels, Top Playbooks, and New Team Members.

### Improvements

#### User Interface (UI)
 - Added Calls keyboard shortcuts to the **Keyboard shortcuts** help modal.
 - Updated the "Contact Sales" link to ``mattermost.com/pl/contact-sales`` and update the pricing modal user interface.
 - Introduced a new ``/marketplace`` slash command that brings up the marketplace modal for the Admin, and changed the ``/help`` command so that it now keeps the user internal to Mattermost.
 - Team unreads are now calculated based on the channel membership and threads only. Team membership is no longer taken into account.
 - For introducing Boards and Playbooks to new users, an “explore other tools in platform” item was added to the end user onboarding checklist.
 - Added the **Save** option to the post menu.
 - Only the most recent message is now marked as unread when marking a thread as unread from the Threads list.
 - Insights filters now persist instead of being reset to default when switching to channels and returning back to the Insights view.
 - Code blocks now have better support for language filetype extensions and are a smaller bundle size.
 - A Desktop App prompt is now always shown on first visit to a Mattermost server from an email notification.
 - Search dropdown options now allow focusing by pressing the tab key.
 - Downgraded Bulgarian language support to Beta.

#### Administration
 - Added a **View Plan** button within the plan card via **System Console > License**.
 - Started tracking the join time of team members and added a new API endpoint to retrieve information about team members who have joined during a given time.
 - Introduced an optional ``shouldRender`` function parameter to ``registerchannelHeaderMenuAction`` plugin function. This allows menu items to conditionally render depending on the current state prior to rendering.
 - Plugins can now hide plugin settings based on the server's hosting environment.
 - Customers who are on a 30-day free trial are now notified three days before the trial ends.

### Bug Fixes
 - Fixed an issue where muted channels with an at-mention were displayed under the **Unreads** section of the channel switcher.
 - Fixed an issue where starting a trial failed if ``SiteURL`` was not set.
 - Fixed an issue where reading a thread on the mobile app caused a negative mention count to display on the web app.
 - Fixed an issue where the user's profile image persisted after user account deletion.
 - Fixed an issue where exports generated via mmctl without attachments still included the file properties in the post, so they couldn't be imported.
 - Fixed an issue that caused a crash when unread posts were fetched.
 - Fixed an issue where updating a profile image and creating new emojis used multipart uploads when using S3 storage.
 - Fixed an issue where the input legend on the custom group modal was cut off in Chrome.
 - Fixed an issue where the **Disable post formatting** setting was hidden when the advanced text editor was enabled.
 - Fixed an issue where we didn’t fall back to the user's default picture if a profile picture failed to load.
 - Fixed an issue where disabling a WebApp plugin from its configuration page resulted in the radio button reverting to ``true``.
 - Fixed an issue where the cursor sometimes jumped to the center channel textbox when the right-hand side was open.
 - Fixed an issue where closing the right-hand side also closed the edited post in the center channel.
 - Fixed an issue where selecting "Try free now" opened the top three enterprise features instead of the "Your trial has started" modal.
 - Fixed an issue where the Threads view displayed as unread even if there were no unread threads.
 - Fixed an issue where configuration changes could not be saved in the **System Console** in some cases.
 - Fixed typos in some translations that caused some in-product links to be broken.

### API Changes
 - Added new API endpoints:
 
	  - ``GET /api/v4/users/me/top/dms``
	  - ``GET /api/v4/users/me/top/threads``
	  - ``GET /api/v4/teams/:team_id/top/team_members``
	  - ``GET /api/v4/teams/:team_id:/top/threads``
 - Added ``first_inaccessible_post_time`` to post API responses.
 - Adds query parameter ``include_deleted`` to endpoint: ``{{[http://your-mattermost-url.com/api/v4/posts/{post_id}/files/info}}](http://your-mattermost-url.com/api/v4/posts/%7Bpost_id%7D/files/info%7D%7D)``.

### Go Version
 - v7.3 is built with Go ``v1.18.1``.

### Open Source Components
 - Added ``@floating-ui/react-dom-interactions`` to https://github.com/mattermost/mattermost-webapp.

### Known Issues
 - The new Insights feature has some performance costs that we are working to optimize. This feature can be disabled by setting the ``MM_FEATUREFLAGS_INSIGHTSENABLED`` environment variable to ``false``.
 - On larger screens, the Insights widgets are pushed to the side when the right-hand side is open [MM-46886](https://mattermost.atlassian.net/browse/MM-MM-46886).
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - Boards are not refreshing on creation. See the [GitHub discussion](https://github.com/mattermost/focalboard/discussions/1971) for more information.
 - Boards export and reimport results in duplicates boards because all IDs are replaced by new ones on the server. See the [GitHub issue](https://github.com/mattermost/focalboard/issues/1924) for more information.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.
 
### Contributors
 - [97amarnathk](https://github.com/97amarnathk), [AbhinavVihan](https://github.com/AbhinavVihan), [Afsoon](https://github.com/Afsoon), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [AlexanderMC8533](https://github.com/AlexanderMC8533), [amyblais](https://github.com/amyblais), [antonbuks](https://github.com/antonbuks), [anx-ag](https://github.com/anx-ag), [aperez900907](https://github.com/aperez900907), [asaadmahmood](https://github.com/asaadmahmood), [asatkinson](https://github.com/asatkinson), [ashishbhate](https://github.com/ashishbhate), [AshishDhama](https://github.com/AshishDhama), [azigler](https://github.com/azigler), [BenCookie95](https://github.com/BenCookie95), [BenLloydPearson](https://github.com/BenLloydPearson), [calebroseland](https://github.com/calebroseland), [ComicShrimp](https://github.com/ComicShrimp), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [d-wierdsma](https://github.com/d-wierdsma), [danielsischy](https://github.com/danielsischy), [devinbinnie](https://github.com/devinbinnie), [dimeko](https://github.com/dimeko), [dipak-demansol](https://github.com/dipak-demansol), [dsharma522](https://github.com/dsharma522), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [francescbassas](https://github.com/francescbassas), [frstier](https://github.com/frstier), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gbochora](https://github.com/gbochora), [gmerz](https://github.com/gmerz), [HandsomeChoco](https://github.com/HandsomeChoco), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [hyugabokko](https://github.com/hyugabokko), [ijansky](https://github.com/ijansky), [iogungbade](https://github.com/iogungbade), [iomodo](https://github.com/iomodo), [isacikgoz](https://github.com/isacikgoz), [it33](https://github.com/it33), [jacodaybson](https://github.com/jacodaybson), [jaskiratsingh2000](https://github.com/jaskiratsingh2000), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [jgilliam17](https://github.com/jgilliam17), [johndavidlugtu](https://github.com/johndavidlugtu), [johnsonbrothers](https://github.com/johnsonbrothers), [jpmastermind](https://github.com/jpmastermind), [jprusch](https://github.com/jprusch), [JtheBAB](https://github.com/JtheBAB), [JulienTant](https://github.com/JulienTant), [julmondragon](https://github.com/julmondragon), [justinegeffen](https://github.com/justinegeffen), [kaakaa](https://github.com/kaakaa), [kamre](https://github.com/kamre), [kayazeren](https://github.com/kayazeren), [koox00](https://github.com/koox00), [krisfremen](https://github.com/krisfremen), [kyeongsoosoo](https://github.com/kyeongsoosoo), [larkox](https://github.com/larkox), [levb](https://github.com/levb), [Liberontissauri](https://github.com/Liberontissauri), [lieut-data](https://github.com/lieut-data), [lindy65](https://github.com/lindy65), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [m1lt0n](https://github.com/m1lt0n), [majo](https://translate.mattermost.com/user/majo), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w), [mbc](https://translate.mattermost.com/user/mbc), [metanerd](https://github.com/metanerd), [mgdelacroix](https://github.com/mgdelacroix), [michelengelen](https://github.com/michelengelen), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [mjnagel](https://github.com/mjnagel), [mkraft](https://github.com/mkraft), [Mshahidtaj](https://github.com/Mshahidtaj), [munish7771](https://github.com/munish7771), [nadeem-hassan](https://github.com/nadeem-hassan), [natalie-hub](https://github.com/natalie-hub), [neallred](https://github.com/neallred), [neflyte](https://github.com/neflyte), [nevyangelova](https://github.com/nevyangelova), [nickmisasi](https://github.com/nickmisasi), [noxer](https://github.com/noxer), [orlandorode97](https://github.com/orlandorode97), [petrmifek](https://github.com/petrmifek), [pfltdv](https://github.com/pfltdv), [pheel](https://github.com/pheel), [phoinixgrr](https://github.com/phoinixgrr), [phpfs](https://github.com/phpfs), [Phrynobatrachus](https://github.com/Phrynobatrachus), [Pinjasaur](https://github.com/Pinjasaur), [plant99](https://github.com/plant99), [potatogim](https://github.com/potatogim), [pvev](https://github.com/pvev), [Rajat-Dabade](https://github.com/Rajat-Dabade), [RoyI99](https://github.com/RoyI99), [rtfm98](https://github.com/rtfm98), [sadohert](https://github.com/sadohert), [safakkizkin](https://github.com/safakkizkin), [salmanmanekia](https://github.com/salmanmanekia), [santoniriccardo](https://github.com/santoniriccardo), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [seoyeongeun](https://github.com/seoyeongeun), [shamboozles](https://github.com/shamboozles), [sibasankarnayak](https://github.com/sibasankarnayak), [sinansonmez](https://github.com/sinansonmez), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [suzutatsu](https://github.com/suzutatsu), [svelle](https://github.com/svelle), [Szymongib](https://github.com/Szymongib), [TalelingFantasy](https://translate.mattermost.com/user/TalelingFantasy), [tboulis](https://github.com/tboulis), [thepra](https://translate.mattermost.com/user/thepra), [thinkGeist](https://github.com/thinkGeist), [trilopin](https://github.com/trilopin), [tsabi](https://github.com/tsabi), [varghesejose2020](https://github.com/varghesejose2020), [varundey](https://github.com/varundey), [vetash](https://github.com/vetash), [vish9812](https://github.com/vish9812), [wgshtg](https://translate.mattermost.com/user/wgshtg), [whiver](https://github.com/whiver), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [wsh](https://translate.mattermost.com/user/wsh), [wuwinson](https://github.com/wuwinson), [yangyangdaji](https://github.com/yangyangdaji), [zefhemel](https://github.com/zefhemel)

## Release v7.2 - [Feature Release](/upgrade/release-definitions.html#feature-release)

- **v7.2.1, released 2022-10-14**
  - Mattermost v7.2.1 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
- **v7.2.0, released 2022-08-16**
  - Original 7.2.0 release

Mattermost v7.2.0 contains low to medium severity level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Important Upgrade Notes
Several schema changes impose additional database constraints to make the data more strict. All the commands listed below were tested on a 8 core, 16GB RAM machine. Here are the times recorded:

**PostgreSQL (131869 channels, 2 teams)**:

- ``CREATE TYPE channel_type AS ENUM ('P', 'G', 'O', 'D');`` took 14.114 milliseconds
- ``ALTER TABLE channels alter column type type channel_type using type::channel_type;`` took 3856.790 milliseconds (3.857 seconds)
- ``CREATE TYPE team_type AS ENUM ('I', 'O');`` took 4.191 milliseconds
- ``ALTER TABLE teams alter column type type team_type using type::team_type;`` took 116.205 milliseconds
- ``CREATE TYPE upload_session_type AS ENUM ('attachment', 'import');`` took 4.266 milliseconds
- ``ALTER TABLE uploadsessions alter column type type upload_session_type using type::upload_session_type;`` took 37.099 milliseconds

**MySQL (270959 channels, 2 teams)**:

- ``ALTER TABLE Channels MODIFY COLUMN Type ENUM("D", "O", "G", "P");`` took 13.24 seconds
- ``ALTER TABLE Teams MODIFY COLUMN Type ENUM("I", "O");`` took 0.04 seconds
- ``ALTER TABLE UploadSessions MODIFY COLUMN Type ENUM("attachment", "import");`` took 0.03 seconds

**IMPORTANT:** If you upgrade from a release earlier than v7.1, please read the other [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).

### Highlights

#### Message Forwarding
 - You can now easily share messages as permalinks and respective permalink previews via the new [Post Forwarding feature](/channels/forward-messages.html). Simply select the new **Forward** option from the **More** section of the message hover actions menu on a given message, choose a desired destination, and optionally add a comment for context.
 
#### Audit Log v2 (Beta)
 - Added support for new [schema and output log types](/comply/audit-log.html). Contrary to the previous audit log implementation, all audit log records now have the same schema.

### Improvements

#### User Interface (UI)
 - Pre-packaged Calls v0.7.1.
 - Added the option to colorize usernames in compact display mode when **Account Settings > Display > Message Display > Compact** is selected.
 - Added a setting to always land users at the newest messages in a channel via **Account settings > Advanced > Scroll position when viewing an unread channel**.
 - Added email headers to notification emails so they can be threaded by email clients.
 - Added **Save** and **Cancel** buttons for post inline editing.
 - Enterprise trial details are now displayed for end users in the product switcher menu.
 - Updated the **Edit Header** modal text description to be applicable to channels, direct messages, and group messages.
 - Added a red destructive action color to ``Archive Channel`` and ``Leave Channel`` menu actions.
 - Plugin activation errors now show in the plugin management page and marketplace.
 - Added accessibility to the emoji picker skin tone selector and reversed the order of the skin tone selections in the emoji selector.

#### Administration
 - Added an **Upgrade** button for Admins on the navigation bar.
 - Added the ability for Admins to quickly view different paid license options inside the product.
 - Added the ability to start a trial from the **Invite People** modal.
 - Admins are now able to search for channel IDs via **System Console > User Management > Channels** page.
 - In the **System Console** left-hand side, paid features icons are now displayed on the menu entries to indicate enterprise features.
 - Added ``webSocketClient`` to ``Pluggable`` and ``PostWillRenderEmbed`` plugin registered components.
 - Added a new static system-level role called [Custom Group Manager](/onboard/system-admin-roles.html). This role has permissions to create, edit, and delete custom user groups via User Groups in the Products menu. It can be used to assign individual users this ability when Custom Groups permissions are removed for All Members via the **System Console** (**System Console > Permissions > Edit Scheme > Custom Groups**).
 - Export file names now contain the ID of the job they were generated by.

### Performance
 - Removed ``getLastPostPerChannel`` selector for improved performance in channel sorting.

### Bug Fixes
 - Fixed an issue with pasting a GitHub code snippet in the message box when text is selected.
 - Fixed an issue where fully typed emojis that contained a capital letter were not correctly displayed.
 - Fixed an issue where the archive icon for channels did not display correctly in dark themes.
 - Fixed an issue where password requirements were not enforced when Development Mode was enabled.
 - Fixed an issue where users were able to attempt to edit the channel header of an archived channel on the right-hand side.
 - Fixed an issue where the “Your Trial Ended” banner hid the product switcher menu.
 - Fixed an issue where the custom status date format was not set to ``YYYY-MM-DD``.
 - Fixed an issue where users were unable to remove themselves from a custom role.
 - Fixed an issue where some images in link previews overflowed.
 - Fixed an issue where accessing the **System Console** and then exiting changed the user's status to "Offline".
 - Fixed an issue where the **New Messages** line sometimes appeared when viewing a channel that was previously read.
 - Fixed an issue with incorrectly formatted text in the **System Console**.
 - Fixed an issue where the thread's view would appear as if it has unread threads even if no unread threads existed.
 - Fixed an issue that caused a crash when fetching unread posts.
 - Fixed an issue where the mobile app crashed when unfollowing a thread of a channel that a user was no longer a member of.
 - Fixed an issue where the Custom Brand text was not centered and Site Description configuration did not show a placeholder.
 - Fixed an issue where the group permissions had an extra level of nesting in the user interface. Also the permissions checkboxes were split out into their individual custom group permissions for a greater granularity of control.
 - Fixed an issue where the OpenID Connect authentication button was missing from the signup page.
 - Fixed an issue with autocomplete sorting regression in channels and threads.
 - Fixed an issue where the custom branding logo was distorted on the login screen.

### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:
 - Under ``FileSettings`` in ``config.json``:
    - A new config setting ``AmazonS3RequestTimeoutMilliseconds`` was added which sets a timeout for requests to AWS S3. By default, the timeout is at 30 seconds.

#### API Changes
 - Added a new response-header ``Has-Inaccessible-Posts`` for ``getPost`` and ``getPostByIDs`` APIs.

### Go Version
 - v7.2 is built with Go ``v1.18.1``.

### Open Source Components
 - Added ``@types/color-hash``, ``color-contrast-checker``, ``color-hash``, and ``webpack`` to https://github.com/mattermost/mattermost-webapp.

### Known Issues
 - The new Insights feature has some performance costs that we are working to optimize. This feature can be disabled by setting the ``MM_FEATUREFLAGS_INSIGHTSENABLED`` environment variable to ``false``.
 - Forwarding messages: pressing Enter key on an auto-complete item in the comment box sends the forward message [MM-46142](https://mattermost.atlassian.net/browse/MM-46142).
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - Boards are not refreshing on creation. See the [GitHub discussion](https://github.com/mattermost/focalboard/discussions/1971) for more information.
 - Boards export and reimport results in duplicates boards because all IDs are replaced by new ones on the server. See the [GitHub issue](https://github.com/mattermost/focalboard/issues/1924) for more information.
 
### Contributors
 - [64bitpandas](https://github.com/64bitpandas), [Afsoon](https://github.com/Afsoon), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [amyblais](https://github.com/amyblais), [Apahadi73](https://github.com/Apahadi73), [asaadmahmood](https://github.com/asaadmahmood), [ashishbhate](https://github.com/ashishbhate), [AshishDhama](https://github.com/AshishDhama), [avinashlng1080](https://github.com/avinashlng1080), [azigler](https://github.com/azigler), [ballista01](https://github.com/ballista01), [BenCookie95](https://github.com/BenCookie95), [calebroseland](https://github.com/calebroseland), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [d-wierdsma](https://github.com/d-wierdsma), [debasish4patra](https://github.com/debasish4patra), [devinbinnie](https://github.com/devinbinnie), [eggmoid](https://github.com/eggmoid), [filipeandrade6](https://github.com/filipeandrade6), [gabrieljackson](https://github.com/gabrieljackson), [gbochora](https://github.com/gbochora), [Haliax](https://github.com/Haliax), [hannaparks](https://github.com/hannaparks), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hegocre](https://github.com/hegocre), [hmhealey](https://github.com/hmhealey), [ifnotak](https://github.com/ifnotak), [imasdekar](https://github.com/imasdekar), [imskr](https://github.com/imskr), [iomodo](https://github.com/iomodo), [isacikgoz](https://github.com/isacikgoz), [iyampaul](https://github.com/iyampaul), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [johnsonbrothers](https://github.com/johnsonbrothers), [jonathanwiemers](https://github.com/jonathanwiemers), [josephbaylon](https://github.com/josephbaylon), [jprusch](https://github.com/jprusch), [JtheBAB](https://github.com/JtheBAB), [JulienTant](https://github.com/JulienTant), [julmondragon](https://github.com/julmondragon), [justinegeffen](https://github.com/justinegeffen), [kaakaa](https://github.com/kaakaa), [kamre](https://github.com/kamre), [KantinHoll](https://translate.mattermost.com/user/KantinHoll), [karistuck](https://github.com/karistuck), [kayazeren](https://github.com/kayazeren), [komarnitskyi](https://github.com/komarnitskyi), [koox00](https://github.com/koox00), [krisfremen](https://github.com/krisfremen), [krmh04](https://github.com/krmh04), [kyeongsoosoo](https://github.com/kyeongsoosoo), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo/), [maksimatveev](https://github.com/maksimatveev), [manojmalik20](https://github.com/manojmalik20), [MarkAndersonTrocme](https://github.com/MarkAndersonTrocme), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w), [mgdelacroix](https://github.com/mgdelacroix), [michelengelen](https://github.com/michelengelen), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [mkraft](https://github.com/mkraft), [Mshahidtaj](https://github.com/Mshahidtaj), [munish7771](https://github.com/munish7771), [muratbayan](https://github.com/muratbayan), [neallred](https://github.com/neallred), [neflyte](https://github.com/neflyte), [nevyangelova](https://github.com/nevyangelova), [nickmisasi](https://github.com/nickmisasi), [noxer](https://github.com/noxer), [ogi-m](https://github.com/ogi-m), [oh6hay](https://github.com/oh6hay), [pfltdv](https://github.com/pfltdv), [phoinixgrr](https://github.com/phoinixgrr), [Phrynobatrachus](https://github.com/Phrynobatrachus), [Pinjasaur](https://github.com/Pinjasaur), [pjenicot](https://github.com/pjenicot), [plant99](https://github.com/plant99), [potatogim](https://github.com/potatogim), [pvev](https://github.com/pvev), [Rajat-Dabade](https://github.com/Rajat-Dabade), [RKRohk](https://github.com/RKRohk), [RoyI99](https://github.com/RoyI99), [sadohert](https://github.com/sadohert), [samia64saleem](https://github.com/samia64saleem), [santoniriccardo](https://github.com/santoniriccardo), [saosangmo](https://github.com/saosangmo), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [seoyeongeun](https://github.com/seoyeongeun), [serhack](https://github.com/serhack), [shamboozles](https://github.com/shamboozles), [Sharuru](https://github.com/Sharuru), [sibasankarnayak](https://github.com/sibasankarnayak), [SilverKnightKMA](https://github.com/SilverKnightKMA), [sinansonmez](https://github.com/sinansonmez), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [svelle](https://github.com/svelle), [Szymongib](https://github.com/Szymongib), [t0mm0](https://github.com/t0mm0), [tboulis](https://github.com/tboulis), [thePanz](https://github.com/thePanz), [thinkGeist](https://github.com/thinkGeist), [tiagodll](https://github.com/tiagodll), [trilopin](https://github.com/trilopin), [tsabi](https://github.com/tsabi), [varghesejose2020](https://github.com/varghesejose2020), [vdvukhzhilov](https://github.com/vdvukhzhilov), [vish9812](https://github.com/vish9812), [weblate](https://github.com/weblate), [whiver](https://github.com/whiver), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [yoikeda](https://github.com/yoikeda), [zefhemel](https://github.com/zefhemel)

## Release v7.1 - [Extended Support Release](/upgrade/release-definitions.html#extended-support-release-esr)

- **v7.1.9, released 2023-04-27**
  - Mattermost v7.1.9 contains a medium severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
- **v7.1.8, released 2023-04-12**
  - Mattermost v7.1.8 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
- **v7.1.7, released 2023-03-17**
  - Added a ``exclude_files_count`` parameter to exclude file counts from channel stats API.
  - Excluded the file count on channel stats API call on from channel header.
- **v7.1.6, released 2023-03-01**
  - Mattermost v7.1.6 contains medium to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where threads were not marked as unread in the Threads view.
  - Fixed an issue where the server sent a wrong badge number when marking a message as unread in a Direct Message channel.
- **v7.1.5, released 2022-12-21**
  - Mattermost v7.1.5 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Added a new schema migration to ensure ``ParentId`` column is dropped from the ``Posts`` table. Depending on the table size, if the column is not dropped before, a significant spike in database CPU usage is expected on MySQL databases. Writes to the table will be limited during the migration.
  - Fixed an issue where **Renew Now** option was not available in-product for self-serve eligible licenses [MM-47045](https://mattermost.atlassian.net/browse/MM-47045).
  - ``getPostSince`` now properly returns deleted posts when Collapsed Reply Threads is enabled.
  - Fixed an issue where the ``Enterprise license is expired`` banner was undismissable [MM-47396](https://mattermost.atlassian.net/browse/MM-47396).
  - Fixed an issue where screen readers did not announce search results in the "Invite members to channel" modal [MM-44859](https://mattermost.atlassian.net/browse/MM-44859).
  - Fixed an issue where screen readers did not announce emojis in the autocomplete list [MM-44877](https://mattermost.atlassian.net/browse/MM-44877).
  - Fixed an issue where screen readers did not announce successful logins [MM-46596](https://mattermost.atlassian.net/browse/MM-46596).
  - Fixed an issue where screen readers incorrectly announced the **Settings > Display > Language > Change interface language** field [MM-44114](https://mattermost.atlassian.net/browse/MM-44114).
  - Fixed an issue where the search dropdown options did not allow focusing with a tab [MM-34969](https://mattermost.atlassian.net/browse/MM-34969).
  - Fixed an issue where screen readers failed to announce "no results found" in the **Direct Message** modal [MM-44858](https://mattermost.atlassian.net/browse/MM-44858).
  - Fixed an issue where the **Test Connection** button in **System Console > Environment > Elasticsearch** did not correctly take the right config settings specified in the page. Earlier, it would always take the previously saved config [MM-47154](https://mattermost.atlassian.net/browse/MM-47154).
- **v7.1.4, released 2022-10-14**
  - Mattermost v7.1.4 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
- **v7.1.3, released 2022-08-23**
  - Mattermost v7.1.3 contains a medium severity level security fix. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where Admins were unable to save configuration changes in the **System Console** in some cases [MM-45875](https://mattermost.atlassian.net/browse/MM-45875).
- **v7.1.2, released 2022-07-21**
  - Fixed an issue where mmctl checked the server version incorrectly.
- **v7.1.1, released 2022-07-15**
  - Fixed an issue where selecting "Update" next to an outdated Marketplace plugin didn't work [MM-45731](https://mattermost.atlassian.net/browse/MM-45731).
- **v7.1.0, released 2022-07-15**
  - Original 7.1.0 release

Mattermost v7.1.0 contains low severity level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Important Upgrade Notes
 - A new configuration option ``MaxImageDecoderConcurrency`` indicates how many images can be decoded concurrently at once. The default is -1, and the value indicates the number of CPUs present. This affects the total memory consumption of the server. The maximum memory of a single image is dictated by ``MaxImageResolution * 24 bytes``. Therefore, we recommend that ``MaxImageResolution * MaxImageDecoderConcurrency * 24`` should be less than the allocated memory for image decoding.
 - Mattermost v7.1 introduces schema changes in the form of a new column and its index. The following notes our test results for the schema changes:
    - MySQL 12M Posts, 2.5M Reactions - ~1min 34s (instance: PC with 8 cores, 16GB RAM)
    - PostgreSQL 12M Posts, 2.5M Reactions - ~1min 18s (instance: db.r5.2xlarge)
 - You can run the following SQL queries before the upgrade to obtain a lock on ``Reactions`` table, so that users' reactions posted during this time won't be reflected in the database until the migrations are complete. This is fully backwards-compatible.
    - For MySQL:
      - ``ALTER TABLE Reactions ADD COLUMN ChannelId varchar(26) NOT NULL DEFAULT "";``
      - ``UPDATE Reactions SET ChannelId = COALESCE((select ChannelId from Posts where Posts.Id = Reactions.PostId), '') WHERE ChannelId="";`` 
      - ``CREATE INDEX idx_reactions_channel_id ON Reactions(ChannelId) LOCK=NONE;``
  
    - For PostgreSQL:
      - ``ALTER TABLE reactions ADD COLUMN IF NOT EXISTS channelid varchar(26) NOT NULL DEFAULT '';``
      - ``UPDATE reactions SET channelid = COALESCE((select channelid from posts where posts.id = reactions.postid), '') WHERE channelid='';`` 
      - ``CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_reactions_channel_id on reactions (channelid);`` 

**IMPORTANT:** If you upgrade from a release earlier than v7.0, please read the other [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).

### Highlights

#### Insights (Beta) (Enterprise and Professional)
 - Added workplace insights consisting of usage and behavior data, which helps Enterprises further increase productivity of their employees through Mattermost functionality. This feature can be disabled by setting the ``MM_FEATUREFLAGS_INSIGHTSENABLED`` environment variable to ``false``.

### Improvements

#### User Interface (UI)
 - Pre-packaged Playbooks v1.29.1, Boards v7.1.0, and Calls v0.7.0.
 - Recent emojis are now sorted based on the number of times an emoji has been used.
 - Improved the link preview user interface.
 - Added new search shortcuts to the **Keyboard Shortcuts** modal. 
    - CMD+F (macOS) and CTRL+F (Windows) for Desktop App
    - CMD+SHIFT+F (macOS) and CTRL+SHIFT+F (Windows) for webapp
 - Changed some tooltips to appear when focused instead of just on hover.
- Added support for syntax highlighting for 1C:Enterprise (BSL) language.

#### Administration
 - Default password requirements have been loosened to eight characters and no numeric, casing, or special characters required. These requirements can be configured by the System Admin as needed via **System Console > Password**.
 - The System Console now also searches and returns channels based on the channel ID. A new parameter ``IncludeSearchById`` was added to the channel search endpoint, allowing requests to include searches that match IDs in response.
 - Search results in PostgreSQL will now respect the ``default_text_search_config`` value instead of being hardcoded to English. Mattermost System Admins should check this value in case of any discrepancies with what is expected.
 - Moved ``UserHasJoinedTeam`` callback to after a user is added to a team.

#### Performance
 - Reduced the number of calls made to ``viewChannel`` API during regular usage.
 - Added pagination to the ``getPostThread`` API calls.

### Bug Fixes
 - Fixed an issue where links to internal help pages did not always open in a new browser tab.
 - Fixed an issue that caused the Channel Members right-hand side search input to not search all the members of a channel.
 - Fixed an issue where the feature discovery page still displayed a **Start Trial** button after a trial was completed.
 - Fixed an issue where channel recency sorting was not consistent between mobile and webapp.
 - Fixed an issue with uploading SVG files.
 - Fixed an issue where thread posts were not left-aligned in compact message display mode.
 - Fixed an error about a missing column for the Shared Channels experimental feature.
 - Fixed an issue where the channel menu drop-down option "Move to..." was skipped when pressing the TAB keyboard key.
 - Fixed an issue where the bulk import failed due to reply ``CreateAt`` being greater than that of the parent post.
 - Fixed an undefined error when leaving a channel with the Unreads filter enabled.
 - Fixed an issue where clicking on a quick emoji reaction opened the right-hand pane.
 - Fixed an issue where the keyboard focus did not go back to the post textbox after hitting CTRL/CMD+SHIFT+P twice.
 - Fixed an issue where the upload files button was positioned incorrectly.
 - Fixed an issue where duplicated emojis sometimes displayed as recently used emojis.
 - Fixed an issue where autocomplete "@" search for names did not normalize UTF-8 characters.
 - Fixed an issue where **Group Messages** with long display names didn't have a tooltip in the left-hand sidebar.
 - Fixed an issue where the file icon was sometimes unresponsive.
 - Fixed a race condition where switching teams to an unread channel did not appear to mark that channel as read.
 - Fixed an issue where the error message did not appear if a user drafted a too long post.
 - Fixed an issue where channels with more than 100 members only showed 100 channel members in the right-hand side.
 - Fixed an issue where the preview mode in the advanced text editor did not reset after posting a message.
   
### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:
 - Under ``ServiceSettings`` in ``config.json``:
    - The setting ``EnableInsecureOutgoingConnections`` is now applicable to S3 clients as well. If that is set, s3 clients will skip TLS verification.

#### API Changes
 - To allow Admins to retrieve contents of posts whether they are deleted or not, ``include_deleted`` query parameter was introduced to ``GetPost`` endpoint.

### Go Version
 - v7.1 is built with Go ``v1.18.1``.

### Open Source Components
 - Added ``@floating-ui/react-dom`` and removed ``superagent`` and ``jasny-bootstrap`` from https://github.com/mattermost/mattermost-webapp/.

### Known Issues
 - The new Insights feature has some performance costs that we are working to optimize. This feature can be disabled by setting the ``MM_FEATUREFLAGS_INSIGHTSENABLED`` environment variable to ``false``.
 - The Top Boards widget in Insights is slow to load.
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - Boards are not refreshing on creation. See the [GitHub discussion](https://github.com/mattermost/focalboard/discussions/1971) for more information.
 - Boards export and reimport results in duplicates boards because all IDs are replaced by new ones on the server. See the [GitHub issue](https://github.com/mattermost/focalboard/issues/1924) for more information.

### Contributors
 - [3ach](https://github.com/3ach), [abhijit-singh](https://github.com/abhijit-singh), [aeomin](https://github.com/aeomin), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [alejdg](https://github.com/alejdg), [amyblais](https://github.com/amyblais), [angeloskyratzakos](https://github.com/angeloskyratzakos), [antonbuks](https://github.com/antonbuks), [anurag6713](https://github.com/anurag6713), [armanchand](https://github.com/armanchand), [ashishbhate](https://github.com/ashishbhate), [AshishDhama](https://github.com/AshishDhama), [azigler](https://github.com/azigler), [Ballista01](https://github.com/Ballista01), [BenCookie95](https://github.com/BenCookie95), [BenLloydPearson](https://github.com/BenLloydPearson), [calebroseland](https://github.com/calebroseland), [chenilim](https://github.com/chenilim), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [d-wierdsma](https://github.com/d-wierdsma), [darkLord19](https://github.com/darkLord19), [devinbinnie](https://github.com/devinbinnie), [dimoiko100](https://github.com/dimoiko100), [dipak-demansol](https://github.com/dipak-demansol), [dontoisme](https://github.com/dontoisme), [DSchalla](https://github.com/DSchalla), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [engineereng](https://github.com/engineereng), [erezo9](https://github.com/erezo9), [esethna](https://github.com/esethna), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gbochora](https://github.com/gbochora), [gbyx3](https://github.com/gbyx3), [hannaparks](https://github.com/hannaparks), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [imasdekar](https://github.com/imasdekar), [imskr](https://github.com/imskr), [iomodo](https://github.com/iomodo), [isacikgoz](https://github.com/isacikgoz), [ismaaylSpiria](https://github.com/ismaaylSpiria), [IsmailTakriti](https://translate.mattermost.com/user/IsmailTakriti/), [it33](https://github.com/it33), [jaskiratsingh2000](https://github.com/jaskiratsingh2000), [jasonblais](https://github.com/jasonblais), [jbattistispiria](https://github.com/jbattistispiria), [jespino](https://github.com/jespino), [jfcastroluis](https://github.com/jfcastroluis), [jgilliam17](https://github.com/jgilliam17), [johnsonbrothers](https://github.com/johnsonbrothers), [jprusch](https://github.com/jprusch), [JtheBAB](https://github.com/JtheBAB), [JulienTant](https://github.com/JulienTant), [julmondragon](https://github.com/julmondragon), [justinegeffen](https://github.com/justinegeffen), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kamre](https://github.com/kamre), [kayazeren](https://github.com/kayazeren), [keremkurtulus](https://github.com/keremkurtulus), [Kirill](https://github.com/Kirill), [koox00](https://github.com/koox00), [krisfremen](https://github.com/krisfremen), [kyeongsoosoo](https://github.com/kyeongsoosoo), [lapaz17](https://github.com/lapaz17), [larkox](https://github.com/larkox), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [lindy65](https://github.com/lindy65), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo/), [maksimatveev](https://translate.mattermost.com/user/maksimatveev/), [manojmalik20](https://github.com/manojmalik20), [marianunez](https://github.com/marianunez), [maruTA-bis5](https://github.com/maruTA-bis5), [master7](https://translate.mattermost.com/user/master7/), [matt-w99](https://github.com/matt-w99), [matthewbirtch](https://github.com/matthewbirtch), [mayur_dhamecha](@mayur_dhamecha), [metanerd](https://github.com/metanerd), [metehankaraca](https://github.com/metehankaraca), [mgdelacroix](https://github.com/mgdelacroix), [michelengelen](https://github.com/michelengelen), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [miltalex](https://github.com/miltalex), [mkraft](https://github.com/mkraft), [Mshahidtaj](https://github.com/Mshahidtaj), [munish7771](https://github.com/munish7771), [mvitale1989](https://github.com/mvitale1989), [natalie-hub](https://github.com/natalie-hub), [neallred](https://github.com/neallred), [neflyte](https://github.com/neflyte), [nevyangelova](https://github.com/nevyangelova), [Ngwind](https://github.com/Ngwind), [nickmisasi](https://github.com/nickmisasi), [nikolaizah](https://github.com/nikolaizah), [noxer](https://github.com/noxer), [ogi-m](https://github.com/ogi-m), [pfltdv](https://github.com/pfltdv), [pheel](https://github.com/pheel), [phoinixgrr](https://github.com/phoinixgrr), [Phrynobatrachus](https://github.com/Phrynobatrachus), [Pinjasaur](https://github.com/Pinjasaur), [plant99](https://github.com/plant99), [prathers](https://github.com/prathers), [pvev](https://github.com/pvev), [Rajat-Dabade](https://github.com/Rajat-Dabade), [respinffs](https://github.com/respinffs), [rodrigopinero](https://github.com/rodrigopinero), [RoyI99](https://github.com/RoyI99), [Rutam21](https://github.com/Rutam21), [sadohert](https://github.com/sadohert), [santoniriccardo](https://github.com/santoniriccardo), [sayanta66](https://github.com/sayanta66), [sbishel](https://github.com/sbishel), [serhack](https://github.com/serhack), [sinansonmez](https://github.com/sinansonmez),  [sonichigo](https://github.com/sonichigo), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [srkgupta](https://github.com/srkgupta), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [Szymongib](https://github.com/Szymongib), [tboulis](https://github.com/tboulis), [thinkGeist](https://github.com/thinkGeist), [topelrapha](https://github.com/topelrapha), [trilopin](https://github.com/trilopin), [tsabi](https://github.com/tsabi), [varghesejose2020](https://github.com/varghesejose2020), [vish9812](https://github.com/vish9812), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [wuwinson](https://github.com/wuwinson), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [YetAnotherBlogArticle](https://github.com/YetAnotherBlogArticle), [zefhemel](https://github.com/zefhemel), [zsichina](https://github.com/zsichina)
