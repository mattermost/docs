# Mattermost self-hosted changelog

[Mattermost](https://mattermost.com) is an open source platform for secure collaboration across the entire software development lifecycle. This changelog summarizes updates for the latest self-hosted versions of Mattermost to be [deployed and upgraded on infrastructure you control](/guides/deployment.html).

See the [changelog in progress](https://bit.ly/2nK3cVf) for the upcoming release. See the [Legacy Self-Hosted Mattermost Changelog](legacy-self-hosted-changelog) for details on all Mattermost self-hosted releases prior to v6.0.

Latest Mattermost Releases:

- [Release v7.11 - Feature Release](#release-v7-11-feature-release)
- [Release v7.10 - Feature Release](#release-v7-10-feature-release)
- [Release v7.9 - Feature Release](#release-v7-9-feature-release)
- [Release v7.8 - Extended Support Release](#release-v7-8-extended-support-release)

## Release v7.11 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

  - The Mattermost v7.11 release has been canceled as we are working on architectural changes for the Mattermost Suite (Channels, Playbooks, Boards, and Calls). The next scheduled release is v8.0 on June 16th.

## Release v7.10 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

- **v7.10.1, released 2023-05-16**
  - Mattermost v7.10.1 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where a user would still see threads in the threads view of channels they have left. Migration execution time in MySQL: Query OK, 2766769 rows affected (4 min 47.57 sec). Migration execution time in PostgreSQL: 58.11 sec, DELETE 2766690.
  - Pre-packaded version 1.2.1 of Apps plugin.
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
 - [11sma](https://github.com/11sma), [adj2908](https://github.com/adj2908), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [amyblais](https://github.com/amyblais), [amynicol1985](https://github.com/amynicol1985), [andrius.balsevicius](https://translate.mattermost.com/user/andrius.balsevicius), [angeloskyratzakos](https://github.com/angeloskyratzakos), [AntalaFilip](https://github.com/AntalaFilip), [anx-ag](https://github.com/anx-ag), [aputtu](https://github.com/aputtu), [asaadmahmood](https://github.com/asaadmahmood), [AshishDhama](https://github.com/AshishDhama), [avas27JTG](https://github.com/avas27JTG), [ayusht2810](https://github.com/ayusht2810), [BenCookie95](https://github.com/BenCookie95), [bfontaine](https://github.com/bfontaine), [byigorv](https://github.com/byigorv), [calebroseland](https://github.com/calebroseland), [coltoneshaw](https://github.com/coltoneshaw), [ConorMacpherson](https://github.com/ConorMacpherson), [cpoile](https://github.com/cpoile), [creeper-0910](https://translate.mattermost.com/user/creeper-0910), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [d-wierdsma](https://github.com/d-wierdsma), [DaDummy](https://github.com/DaDummy), [devinbinnie](https://github.com/devinbinnie), [Dmitry](https://translate.mattermost.com/user/Dmitry), [dylanrichards](https://github.com/dylanrichards), [EduardoSellanes](https://github.com/EduardoSellanes), [Eleferen](https://translate.mattermost.com/user/Eleferen), [Elpunical](https://github.com/Elpunical), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [ericgaspar](https://github.com/ericgaspar), [esarafianou](https://github.com/esarafianou), [ewwollesen](https://github.com/ewwollesen), [fmartingr](https://github.com/fmartingr), [fnogcps](https://github.com/fnogcps), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gitstart](https://github.com/gitstart), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hattori611](https://github.com/hattori611), [hmhealey](https://github.com/hmhealey), [ialorro](https://github.com/ialorro), [ifoukarakis](https://github.com/ifoukarakis), [isaacbegit](https://github.com/isaacbegit), [isacikgoz](https://github.com/isacikgoz), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jnsgruk](https://github.com/jnsgruk), [Johennes](https://github.com/Johennes), [johnsonbrothers](https://github.com/johnsonbrothers), [jprusch](https://github.com/jprusch), [JulienTant](https://github.com/JulienTant), [julmondragon](https://github.com/julmondragon), [justinegeffen](https://github.com/justinegeffen), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [kaykayehnn](https://github.com/kaykayehnn), [KBeDevel](https://github.com/KBeDevel), [khoipro](https://github.com/khoipro), [kmaed](https://github.com/kmaed), [komoon8934](https://translate.mattermost.com/user/komoon8934), [koox00](https://github.com/koox00), [kostaspt](https://github.com/kostaspt), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [kwiersgalla](https://github.com/kwiersgalla), [larkox](https://github.com/larkox), [leonambeez](https://translate.mattermost.com/user/leonambeez), [lieut-data](https://github.com/lieut-data), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [m1lt0n](https://github.com/m1lt0n), [majo](https://translate.mattermost.com/user/majo), [manojmalik20](https://github.com/manojmalik20), [marianunez](https://github.com/marianunez), [maruTA-bis5](https://translate.mattermost.com/user/maruTA-bis5), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-src](https://github.com/matthew-src), [matthew-w](https://translate.mattermost.com/user/matthew-w), [MatthewDorner](https://github.com/MatthewDorner), [MattSilvaa](https://github.com/MattSilvaa), [metanerd](https://github.com/metanerd), [mgdelacroix](https://github.com/mgdelacroix), [michael_kim](https://translate.mattermost.com/user/michael_kim), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [mini-bomba](https://github.com/mini-bomba), [mirshahriar](https://github.com/mirshahriar), [moatasim](https://translate.mattermost.com/user/moatasim), [MoatazMuhammad51](https://github.com/MoatazMuhammad51), [Mshahidtaj](https://github.com/Mshahidtaj), [munish7771](https://github.com/munish7771), [muratbayan](https://translate.mattermost.com/user/muratbayan), [mvitale1989](https://github.com/mvitale1989), [natalie-hub](https://github.com/natalie-hub), [neallred](https://github.com/neallred), [nevyangelova](https://github.com/nevyangelova), [nickmisasi](https://github.com/nickmisasi), [Nityanand13](https://github.com/Nityanand13), [NixemDEV](https://translate.mattermost.com/user/NixemDEV), [oraliahdz](https://github.com/oraliahdz), [paolo-rossi](https://github.com/paolo-rossi), [Peytob](https://github.com/Peytob), [phoinixgrr](https://github.com/phoinixgrr), [pjenicot](https://translate.mattermost.com/user/pjenicot), [plant99](https://github.com/plant99), [plut0s](https://translate.mattermost.com/user/plut0s), [potatogim](https://translate.mattermost.com/user/potatogim), [pureiris](https://github.com/pureiris), [pvev](https://github.com/pvev), [Qui3t0wL](https://github.com/Qui3t0wL), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [roadt](https://github.com/roadt), [Rutboy](https://translate.mattermost.com/user/Rutboy), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [Sharuru](https://github.com/Sharuru), [sibasankarnayak](https://github.com/sibasankarnayak), [simcard0000](https://github.com/simcard0000), [sinansonmez](https://github.com/sinansonmez), [Sjazz](https://github.com/Sjazz), [smallcms](https://github.com/smallcms), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [srkgupta](https://github.com/srkgupta), [stafot](https://github.com/stafot), [stevemudie](https://github.com/stevemudie), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [tanmay-des](https://github.com/tanmay-des), [tanmaythole](https://github.com/tanmaythole), [Tasy218](https://translate.mattermost.com/user/Tasy218), [toninis](https://github.com/toninis), [trilopin](https://github.com/trilopin), [varghesejose2020](https://github.com/varghesejose2020), [Wainwright0830](https://github.com/Wainwright0830), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [wuwinson](https://github.com/wuwinson), [xiao](https://translate.mattermost.com/user/xiao), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yomiadetutu1](https://github.com/yomiadetutu1)

### Upcoming Deprecations and Breaking Changes in Mattermost v8.0

The following deprecations and breaking changes are planned for the Mattermost v8.0 release, which is scheduled for 2023/06/16. This list is subject to change prior to the release.

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
  - Pre-packaded version 1.2.1 of Apps plugin.
  - Backporting fix for oauth 2. Query times depend on if you have rows to delete or not. Please see the [important upgrade notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) for more details.
- **v7.9.3, released 2023-04-27**
  - Mattermost v7.9.3 contains a medium severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where true-up review submissions always failed.
- **v7.9.2, released 2023-04-12**
  - Mattermost v7.9.2 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Updated prepackaged boards to v7.9.3.
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

- **v7.8.5, released 2023-05-17**
  - Mattermost v7.8.5 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where a user would still see threads in the threads view of channels they have left. Migration execution time in MySQL: Query OK, 2766769 rows affected (4 min 47.57 sec). Migration execution time in PostgreSQL: 58.11 sec, DELETE 2766690.
  - Pre-packaded version 1.2.1 of Apps plugin.
  - Updated the Docker Base Image from Debian to Ubuntu 22.04 LTS.
  - Backported a fix related to Oauth 2. Query times depend on if you have rows to delete or not. Please see the [important upgrade notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) for more details.
- **v7.8.4, released 2023-04-27**
  - Mattermost v7.8.4 contains a medium severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Limited channel search results to 50 to fix a performance issue.
  - Fixed an issue where true-up review submissions always failed.
- **v7.8.3, released 2023-04-12**
  - Mattermost v7.8.3 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Updated prepackaged boards to v7.8.4.
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

## Release v7.0 - [Major Release](/upgrade/release-definitions.html#major-release)

- **v7.0.2, released 2022-08-23**
  - Mattermost v7.0.2 contains a medium severity level security fix. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
- **v7.0.1, released 2022-06-24**
  - Fixed an issue where mmctl checked the server version incorrectly [MM-45161](https://mattermost.atlassian.net/browse/MM-45161).
  - Fixed an issue where the file icon was sometimes unresponsive [MM-45097](https://mattermost.atlassian.net/browse/MM-45097).
  - Fixed an issue with Compliance Exports where the zip file creation failed when adding attachments to a post [MM-40179](https://mattermost.atlassian.net/browse/MM-40179).
  - Fixed the notification title for ``id_loaded`` push notifications [MM-43655](https://mattermost.atlassian.net/browse/MM-43655).
  - Pre-packaged Playbooks v1.28.2.
- **v7.0.0, released 2022-06-15**
  - Original 7.0.0 release

Mattermost v7.0.0 contains medium severity level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Important Upgrade Notes
 - **IMPORTANT:** Session length configuration settings have changed from using a unit of *days* to *hours*. Instances using a config.json file or a database configuration for the following values should be automatically migrated to the new units, but instances using environment variables must make the following changes:
 1. replace `MM_SERVICESETTINGS_SESSIONLENGTHWEBINDAYS` with `MM_SERVICESETTINGS_SESSIONLENGTHWEBINHOURS` (x24 the value).
 2. replace `MM_SERVICESETTINGS_SESSIONLENGTHMOBILEINDAYS` with `MM_SERVICESETTINGS_SESSIONLENGTHMOBILEINHOURS` (x24 the value).
 3. replace `MM_SERVICESETTINGS_SESSIONLENGTHSSOINDAYS` with `MM_SERVICESETTINGS_SESSIONLENGTHSSOINHOURS` (x24 the value).
 - MySQL self-hosted customers may notice the migration taking longer than usual when having a large number of rows in the ``FileInfo`` table. For MySQL, it takes around 19 seconds for a table of size 700,000 rows. The time required for PostgreSQL is negligible. The testing was performed on a machine with specifications of ``CPU - Intel i7 6-cores @ 2.6 GHz`` and ``Memory - 16 GB``.
 - When a new configuration setting via **System Console > Experimental > Features > Enable App Bar** is enabled, all channel header icons registered by plugins will be moved to the new Apps Bar, even if they do not explicitly use the new registry function to render a component there. The setting for Apps Bar defaults to ``false`` for self-hosted deployments.
 - The value of ``ServiceSettings.TrustedProxyIPHeader`` defaults to empty from now on. A previous bug prevented this from happening in certain conditions. Customers are requested to check for these values in their config and set them to nil if necessary. See more details [here](/configure/configuration-settings.html#trusted-proxy-ip-header).
 - Upgrading the Microsoft Teams Calling plugin to v2.0.0 requires users to reconnect their accounts.

**IMPORTANT:** If you upgrade from a release earlier than v6.7, please read the other [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).

### Highlights

#### Collapsed Reply Threads (General Availability)
 - [Collapsed Reply Threads](/channels/organize-conversations.html) is now generally available. Please reference [this article](https://support.mattermost.com/hc/en-us/articles/6880701948564) for more information and guidance for enabling the feature.

#### Calls (Beta)
 - [Native voice calling and screen sharing](/channels/make-calls.html) is now available. This is a Channels-specific integration.

#### Apps Bar (Beta)
 - Channel header is now decluttered when a new configuration setting via **System Console > Experimental > Features > Enable App Bar** is enabled, to make it more obvious how to access Calls, Playbooks, and Boards when viewing a channel. All channel header icons registered by plugins will be moved to the new Apps Bar when the configuration setting is enabled, while Calls remains in the channel header. We recommend enabling the Apps Bar for servers with Calls enabled since the Apps Bar helps make space for the dedicated **Start Call** button in the channel header.

#### Playbooks Updates
 - Users can now easily keep processes up-to-date with [the inline playbook editor](/playbooks/customize-a-playbook.html).
 - A new statistics dashboard was added that displays the number of playbooks and run instances within the server alongside other system statistics in the **System Console**.
 - Run triggers and actions now provide more control over where [status updates are posted](/playbooks/customize-a-run.html) throughout a run.

#### Message Formatting Toolbar
 - The [new formatting toolbar](/channels/format-messages.html#use-the-messaging-formatting-toolbar) makes Markdown accessible to everyone with easy to use controls for commonly used message formatting, such as bold, headings, links, and more.

### Improvements

#### User Interface (UI)
 - For toggling the channel information in the right-hand pane, a shortcut CTRL/CMD+ALT+I was added.
 - Added an "Unread Channels" section to the channel switcher and included threads in the results.
 - Users are no longer hidden from search results in the "Add members" modal, even if they are already members of the channel.
 - Applied new designs for the Login screen.
 - Enabled the new onboarding task list for end users.
 - The legacy **Settings > Advanced Settings > Enable Post Formatting** and **Settings > Advanced Settings > Preview Pre-release Features** settings are now deprecated in favor of the the new formatting toolbar.
 - Romanian language support was downgraded to Beta.
 
#### Performance
 - Improved the performance of aggregate queries related to Collapsed Reply Threads. Learn more about these server performance optimizations in [this article](https://support.mattermost.com/hc/en-us/articles/6880701948564).

#### Integrations
 - To keep users in Mattermost when opening documentation links from the **System Console > Plugin** settings page, all the links now open in another tab.
 - Changed **Actions** post menu hover text to **Message Actions**.
 - Updated Apps Framework to version 1.1.0 to add improved logging.

#### Administration
 - Timestamps are now enabled in the default audit configuration.
 - The Collapsed Reply Threads configuration option was moved in the **System Console** from **Experimental** to **Site Configuration > Posts**.
 
#### Enterprise Subscription
 - Upgraded the minor version of the ElasticSearch development Docker image.
 - The Support Packet now contains two additional fields in the ``support_packet.yaml`` file: Active users and License-supported users.

### Bug Fixes
 - Fixed an issue with ADA Accessibility where screen readers did not TAB to or read "This channel has guests" in the channel header bar.
 - Fixed an issue where the @mention autosuggest of users was no longer grouped by channel membership status.
 - Fixed an issue where the New Messages toast was not fully tappable in narrow view.
 - Fixed an issue where the shortcut modal for channel info showed ``ALT`` instead of ``SHIFT`` for Mac.
 - Fixed an issue where the **Help > Report a Problem** link was not hidden when a URL was not set for **System Console > Customization > Report a Problem**.
 - Fixed an issue with the timing of selector performance metrics.
 - Fixed an issue where the S3 **Test Connection** button deceptively failed unless the user pressed **Save** first.
 - Fixed an issue where Workspace Optimization did not load in the System Console on subpath servers.
 - Fixed an issue where an error was logged when ``SendEmailNotifications`` was not set to ``true``.
   
### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:
 - Under ``ServiceSettings`` in ``config.json``:
   - Changed ``SessionLengthWebInDays`` to ``SessionLengthWebInHours``.
   - Changed ``SessionLengthMobileInDays`` to ``SessionLengthMobileInHours``.
   - Changed ``SessionLengthSSOInDays`` to ``SessionLengthSSOInHours``.
   - The value of ``TrustedProxyIPHeader`` defaults to empty from now on. A previous bug prevented this from happening in certain conditions. Customers are requested to check for these values in their config and set them to nil if necessary.
   - Added ``always-on`` and ``default-on`` settings to **System Console > Posts** for Collapsed Reply Threads. When enabled (default-on), users see Collapsed Reply Threads by default and have the option to disable it in **Settings**. When always on, users are required to use Collapsed Reply Threads and can't disable it.
   - The default for ``CollapsedThreads`` has been changed to ``always_on``. This change impacts new Mattermost deployments, and doesn't affect existing configurations where this value is already set to some other value.
 - Under ``ExperimentalSettings`` in ``config.json``:
   - Added a new config setting ``EnableAppBar`` to enable and disable the new Apps Bar. This setting is disabled by default, but we recommend enabling the Apps Bar for servers with Calls enabled since the Apps Bar helps make space for the dedicated **Start Call** button in the channel header.

#### API Changes
 - Added new API endpoints ``GET /api/v4/teams/:team_id/top/channels`` and ``GET /api/v4/users/me/top/channels`` to get top channels for a team and user.

#### Websocket Event Changes
 - Added a new ``ConnectionId`` field to ``model.WebsocketBroadcast`` that allows broadcasting a message only to a specific connection.

### Go Version
 - v7.0 is built with Go ``v1.18.1``.

### Known Issues
 - Post list doesn't always scroll down to show new messages [MM-44131](https://mattermost.atlassian.net/browse/MM-44131).
 - Mentions incorrectly shows users as not in a channel [MM-44157](https://mattermost.atlassian.net/browse/MM-44157).
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - Boards are not refreshing on creation. See the [GitHub discussion](https://github.com/mattermost/focalboard/discussions/1971) for more information.
 - Boards export and reimport duplicate boards because all IDs are replaced by new ones on the server. See the [GitHub issue](https://github.com/mattermost/focalboard/issues/1924) for more information.

### Contributors
 - [Abrahamology](https://github.com/Abrahamology), [AbrahamQll](https://translate.mattermost.com/user/AbrahamQll), [aeomin](https://github.com/aeomin), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [Altaaya](https://github.com/Altaaya), [amyblais](https://github.com/amyblais), [angeloskyratzakos](https://github.com/angeloskyratzakos), [asaadmahmood](https://github.com/asaadmahmood), [ashishbhate](https://github.com/ashishbhate), [AshishDhama](https://github.com/AshishDhama), [BenCookie95](https://github.com/BenCookie95), [BenLloydPearson](https://github.com/BenLloydPearson), [bobmaster](https://translate.mattermost.com/user/bobmaster), [Borknab](https://github.com/Borknab), [bpmct](https://github.com/bpmct), [calebroseland](https://github.com/calebroseland), [catalintomai](https://github.com/catalintomai), [chenilim](https://github.com/chenilim), [cohu-dev](https://github.com/cohu-dev), [coltoneshaw](https://github.com/coltoneshaw), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [debasish4patra](https://github.com/debasish4patra), [devinbinnie](https://github.com/devinbinnie), [dipak-demansol](https://github.com/dipak-demansol), [djanda97](https://github.com/djanda97), [eggmoid](https://github.com/eggmoid), [elyscape](https://github.com/elyscape), [enahum](https://github.com/enahum), [flynbit](https://github.com/flynbit), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gavin-luo](https://github.com/gavin-luo), [gbochora](https://github.com/gbochora), [gin-melodic](https://github.com/gin-melodic), [hamzaMM](https://github.com/hamzaMM), [HandsomeChoco](https://github.com/HandsomeChoco), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [ialorro](https://github.com/ialorro), [iomodo](https://github.com/iomodo), [isacikgoz](https://github.com/isacikgoz), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jbattistispiria](https://github.com/jbattistispiria), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [johnsonbrothers](https://github.com/johnsonbrothers), [jonathanwiemers](https://github.com/jonathanwiemers), [jprusch](https://github.com/jprusch), [jsoref](https://github.com/jsoref), [jtdspiria](https://github.com/jtdspiria), [JtheBAB](https://github.com/JtheBAB), [JulienTant](https://github.com/JulienTant), [julmondragon](https://github.com/julmondragon), [justinegeffen](https://github.com/justinegeffen), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kamre](https://github.com/kamre), [kayazeren](https://github.com/kayazeren), [kkennethlee](https://github.com/kkennethlee), [koox00](https://github.com/koox00), [krisfremen](https://github.com/krisfremen), [krmh04](https://github.com/krmh04), [kyeongsoosoo](https://github.com/kyeongsoosoo), [larkox](https://github.com/larkox), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [lisez](https://github.com/lisez), [lkyuchukov](https://github.com/lkyuchukov), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo/), [maksimatveev](https://github.com/maksimatveev), [master7](https://translate.mattermost.com/user/master7),  [matthew-w](https://translate.mattermost.com/user/matthew-w/), [matt-w99](https://github.com/matt-w99), [maxtrem271991](https://github.com/maxtrem271991), [metanerd](https://github.com/metanerd), [metehankaraca](https://translate.mattermost.com/user/metehankaraca/), [mgdelacroix](https://github.com/mgdelacroix), [michelengelen](https://github.com/michelengelen), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [miltalex](https://github.com/miltalex), [mjnagel](https://github.com/mjnagel), [mkraft](https://github.com/mkraft), [Mshahidtaj](https://github.com/Mshahidtaj), [munish7771](https://github.com/munish7771), [neallred](https://github.com/neallred), [nickmisasi](https://github.com/nickmisasi), [nzeemin](https://github.com/nzeemin), [pfltdv](https://github.com/pfltdv), [phoinixgrr](https://github.com/phoinixgrr), [Phrynobatrachus](https://github.com/Phrynobatrachus), [plykung](https://translate.mattermost.com/user/plykung/), [prakharporwal](https://github.com/prakharporwal), [pvev](https://github.com/pvev), [Rajat-Dabade](https://github.com/Rajat-Dabade), [RoyI99](https://github.com/RoyI99), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [seoyeongeun](https://github.com/seoyeongeun), [sibasankarnayak](https://github.com/sibasankarnayak), [SiderealArt](https://github.com/SiderealArt), [sinansonmez](https://github.com/sinansonmez), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [Szymongib](https://github.com/Szymongib), [TQuock](https://github.com/TQuock), [trilopin](https://github.com/trilopin), [tsabi](https://github.com/tsabi), [vaaas](https://github.com/vaaas), [vadimasadchi](https://github.com/vadimasadchi), [vaheed](https://github.com/vaheed), [varghesejose2020](https://github.com/varghesejose2020), [vish9812](https://github.com/vish9812), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [windane](https://translate.mattermost.com/user/windane)

## Release v6.7 - [Feature Release](/upgrade/release-definitions.html#feature-release)

- **v6.7.2, released 2022-06-15**
  - Fixed an issue with Compliance Exports where the zip file creation failed when adding attachments to a post [MM-40179](https://mattermost.atlassian.net/browse/MM-40179).
- **v6.7.1, released 2022-06-13**
  - Mattermost v6.7.1 contains medium severity level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - The value of ``ServiceSettings.TrustedProxyIPHeader`` defaults to empty from now on. A previous bug prevented this from happening
in certain conditions. Customers are requested to check for these values in their config and set them to nil if necessary. See more details [here](/configure/configuration-settings.html#trusted-proxy-ip-header).
- **v6.7.0, released 2022-05-16**
  - Original 6.7.0 release

Mattermost v6.7.0 contains low severity level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Compatibility
 - Updated Chrome recommended minimum version to v100+.

### Important Upgrade Notes
 - New schema changes were introduced in the form of a new index. The following summarizes the test results measuring how long it took for the database queries to run with these schema changes:
    - MySQL 7M Posts - ~17s (Instance: db.r5.xlarge)
    - MySQL 9M Posts - 2min 12s (Instance: db.r5.large)
    - Postgres 7M Posts - ~9s  (Instance: db.r5.xlarge)
 - For customers wanting a zero downtime upgrade, they are encouraged to apply this index prior to doing the upgrade. This is fully backwards compatible and will not acquire any table lock or affect any existing operations on the table when run manually. Else, the queries will run during the upgrade process and will lock the table in non-MySQL environments. Run the following to apply this index:
    - For MySQL: `CREATE INDEX idx_posts_create_at_id on Posts(CreateAt, Id) LOCK=NONE;`
    - For Postgres: `CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_posts_create_at_id on posts(createat, id);`

**IMPORTANT:** If you upgrade from a release earlier than v6.6, please read the other [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).

### Highlights

#### Playbooks Updates
 - To keep procedures on track while reducing noise, task due dates can now be added to playbook runs (Professional and Enterprise subscriptions).

### Improvements

#### User Interface (UI)
 - Added Files and Pinned Messages to the right-hand side Channel Info.
 - Improved the New Channel modal user interface.
 - Added the channel members list to the right-hand side Channel Info modal.
 - Added the ability to invite new users to a team from the **Add to channel** modal.
 - To be able to download images and copy public links for images more quickly, a copy URL and download buttons were added to image thumbnails.
 - Added the ability to have one character long channel names.
 - Pre-packaged Calls v0.4.9 with Mattermost server v6.7 (closed Beta). To participate in Beta testing, please contact [Mattermost](https://mattermost.com/contact-sales/).
 - Updated the NPS plugin to version 1.2.0 to add a new **Give Feedback** menu item to the **Help** menu to send feedback at anytime.
 
#### Performance
 - Improved the performance of ``GetTeamsUnreadForUser`` when Collapsed Reply Threads is enabled.
 - Added an index to the ``UserGroups DisplayName`` for improved autosuggest query performance.
 - Improved the performance of permission selectors.
 - Improved the performance of configuration read/writes if the configuration is stored on a database.

#### Administration
 - To add the ability to toggle sending inactivity email notification to Admins, a configuration setting ``EmailSettings.EnableInactivityEmail`` was added.
 - To filter out inactive users in the System Console, an **Active** filter was added for users and Admins in **System Console > User Management > Users**.
 - Added a ``threadsOnly`` query parameter for getting user threads.
 - To allow Admins to add a new license without having to first remove the old one, a new “License" button was added to **System Console > Edition and License**.

#### Enterprise Subscription
 - The Elasticsearch indexing job is resumable now. Stopping a server while the job is running will put the job in pending status and will resume the job when the server starts. The job can still be explicitly canceled via the **System Console**.

### Bug Fixes
 - Fixed an issue where permalinks to direct and group message posts did not show a preview.
 - Fixed an issue when Collapsed Reply Threads are enabled where marking a root post with a mention as unread displayed both a mention badge and the thread item being bolded.
 - Fixed an issue where the public link to generate the API was getting called even if public links were disabled.
 - Fixed an issue with onboarding page view events.
 - Fixed an issue where the custom emoji **Next** button was out of view when a banner was present.
 - Fixed an issue where it would appear that a user had a negative number of unread threads.
 - Fixed an issue where marking the last post in a thread as unread didn't mark the thread as unread.
 - Restored the rendering of main menu items from plugins in non-mobile view.
 - Fixed the overflow of text in **Manage Channel Members** modal title.
 - Fixed an issue where pagination was broken in **System Console > Groups**.
 - Fixed an issue where thread updates did not show correctly after the computer woke up.
 - Fixed an issue where a negative unread count sometimes appeared with Collapsed Reply Threads enabled.
 - Fixed an issue where the modal to create a Custom Group got closed when pressing ENTER.
 - Fixed an issue where group mention did not get highlighted in Professional subscription.
 - Fixed an issue where users were unable to edit posts with markdown code blocks.
 - Fixed an issue where sending test (empty) notifications was allowed even when the ``SendPushNotifications`` config setting was set to ``false``.
   
### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:
 - Under ``EmailSettings`` in ``config.json``:
    - Added ``EnableInactivityEmail`` setting to be able to disable inactive server email notifications.
 - Under ``JobSettings`` in ``config.json``:
    - Added a new cleanup job to regularly remove outdated config entries from the database. The threshold for this setting can be adjusted with ``CleanupConfigThresholdDays``.
 - Under ``ElasticsearchSettings`` in ``config.json``:
    - Elasticsearch (Enterprise subscription) and Bleve indexing have been revamped to be much more efficient and faster. The config parameter ``BulkIndexingTimeWindowSeconds`` for both Elasticsearch and Bleve is now deprecated and no longer used. A new config parameter called ``BatchSize`` has been introduced instead. This parameter controls the number of objects that can be indexed in a single batch. This makes things more efficient and maintains a constant workload.

#### API Changes
 - Added a new API endpoint ``POST /api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/set_unread/{post_id}`` to set a thread as unread by post id.
 - Added new API endpoints ``GET /api/v4/teams/:team_id/top/reactions`` and ``GET /api/v4/users/me/top/reactions`` to get top reactions for a team and user.
 - Fixed an issue where the ``UpdateUser`` API endpoint required a ``create_at`` field.
 - ``api/v4/file/s3_test`` now requires ``FileSettings`` to be all set to run.
 - ``api/v4/email/test`` now requires ``EmailSettings`` to be all set to run.
 - Added ``fromWebhook`` property to the webapp plugin API.

### Go Version
 - v6.7 is built with Go ``v1.18.1``.

### Open Source Components
 - Added ``react-native-math-view`` to https://github.com/mattermost/mattermost-mobile.
 - Removed ``flux`` and ``react-slidedown`` from https://github.com/mattermost/mattermost-webapp.
 - Added ``@mattermost/compass-icons``, ``bootstrap-dark``, ``fs-extra``, and ``pretty-bytes`` to https://github.com/mattermost/desktop.

### Known Issues
 - Channels with more than 100 members only show 100 members in the right-hand side [MM-44159](https://mattermost.atlassian.net/browse/MM-44159).
 - Shortcut modal for channel info shows ``Alt`` instead of ``Shift`` for Mac [MM-44172](https://mattermost.atlassian.net/browse/MM-44172).
 - A blank screen is seen when returning from the System Console while the Channel Info is open on the right-hand side [MM-44435](https://mattermost.atlassian.net/browse/MM-44435).
 - [Collapsed Reply Threads](/messaging/organizing-conversations.html) is currently in beta. Before enabling the feature, please ensure you are well versed in the [known issues](/messaging/organizing-conversations.html#known-issues), particularly relating to database resource requirements and server performance implications. If you cannot easily scale up your database size, or are running the Mattermost application server and database server on the same machine, we recommended waiting to enable Collapsed Reply Threads until it's [promoted to general availability in Q2 2022](https://mattermost.com/blog/collapsed-reply-threads-ga). Learn more about these [performance considerations here](https://support.mattermost.com/hc/en-us/articles/4413183568276).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - Boards are not refreshing on creation. See the [GitHub discussion](https://github.com/mattermost/focalboard/discussions/1971) for more information.
 - Boards export and reimport duplicates boards because all IDs are replaced by new ones on the server. See the [GitHub issue](https://github.com/mattermost/focalboard/issues/1924) for more information.

### Contributors
 - [aeomin](https://github.com/aeomin), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [alexkoala](https://github.com/alexkoala), [alieh-rymasheuski](https://github.com/alieh-rymasheuski), [allonios](https://github.com/allonios), [amyblais](https://github.com/amyblais), [amynicol1985](https://github.com/amynicol1985), [andrewodri](https://github.com/andrewodri), [angeloskyratzakos](https://github.com/angeloskyratzakos), [asaadmahmood](https://github.com/asaadmahmood), [ashishbhate](https://github.com/ashishbhate), [AshishDhama](https://github.com/AshishDhama), [azigler](https://github.com/azigler), [BenCookie95](https://github.com/BenCookie95), [BenLloydPearson](https://github.com/BenLloydPearson), [bermelmike](https://translate.mattermost.com/user/bermelmike), [boxiyang](https://translate.mattermost.com/user/boxiyang), [bpodwinski](https://github.com/bpodwinski), [calebroseland](https://github.com/calebroseland), [cdump](https://github.com/cdump), [cecilysullivan](https://github.com/cecilysullivan), [chenilim](https://github.com/chenilim), [cleferman](https://github.com/cleferman), [codedsun](https://github.com/codedsun), [coltoneshaw](https://github.com/coltoneshaw), [cota-eng](https://translate.mattermost.com/user/cota-eng), [cpoile](https://github.com/cpoile), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [devinbinnie](https://github.com/devinbinnie), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [ewwollesen](https://github.com/ewwollesen), [flynbit](https://github.com/flynbit), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gbochora](https://github.com/gbochora), [HandsomeChoco/](https://translate.mattermost.com/user/HandsomeChoco/), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [ialorro](https://github.com/ialorro), [iomodo](https://github.com/iomodo), [isacikgoz](https://github.com/isacikgoz), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jbattistispiria](https://github.com/jbattistispiria), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [johndavidlugtu](https://github.com/johndavidlugtu), [johnsonbrothers](https://github.com/johnsonbrothers), [josephbaylon](https://github.com/josephbaylon), [jpaldeano](https://github.com/jpaldeano), [jprusch](https://github.com/jprusch), [JtheBAB](https://translate.mattermost.com/user/JtheBAB), [JulienTant](https://github.com/JulienTant), [jupenur](https://github.com/jupenur), [justinegeffen](https://github.com/justinegeffen), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [KevinSJ](https://github.com/KevinSJ), [kherwata](https://translate.mattermost.com/user/kherwata), [KobeBergmans](https://github.com/KobeBergmans), [koox00](https://github.com/koox00), [krmh04](https://github.com/krmh04), [kyeongsoosoo](https://github.com/kyeongsoosoo), [larkox](https://github.com/larkox), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [lindy65](https://github.com/lindy65), [lkyuchukov](https://github.com/lkyuchukov), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo/), [maksimatveev](https://github.com/maksimatveev), [marianunez](https://github.com/marianunez), [master7](https://translate.mattermost.com/user/master7/), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w/), [maxtrem271991](https://translate.mattermost.com/user/maxtrem271991), [mgdelacroix](https://github.com/mgdelacroix), [michaelgamble](https://github.com/michaelgamble), [michelengelen](https://github.com/michelengelen), [mickmister](https://github.com/mickmister), [mikebermel](https://github.com/mikebermel), [milotype](https://github.com/milotype), [mkraft](https://github.com/mkraft), [Mshahidtaj](https://github.com/Mshahidtaj), [muratbayan](https://github.com/muratbayan), [mvitale1989](https://github.com/mvitale1989), [mylonsuren](https://github.com/mylonsuren), [nat-gunner](https://github.com/nat-gunner), [natalie-hub](https://github.com/natalie-hub), [nathanaelhoun](https://github.com/nathanaelhoun), [neallred](https://github.com/neallred), [nickmisasi](https://github.com/nickmisasi), [ogi-m](https://github.com/ogi-m), [pfltdv](https://github.com/pfltdv), [phoinixgrr](https://github.com/phoinixgrr), [Phrynobatrachus](https://github.com/Phrynobatrachus), [Pinjasaur](https://github.com/Pinjasaur), [plant99](https://github.com/plant99), [pvev](https://github.com/pvev), [Rajat-Dabade](https://github.com/Rajat-Dabade), [rebornwwp](https://github.com/rebornwwp), [RoyI99](https://github.com/RoyI99), [ryoarmanda](https://github.com/ryoarmanda), [saturninoabril](https://github.com/saturninoabril), [sayanta66](https://github.com/sayanta66), [sbishel](https://github.com/sbishel), [serhack](https://github.com/serhack), [seoyeongeun](https://translate.mattermost.com/user/seoyeongeun), [shadowshot-x](https://github.com/shadowshot-x), [SiderealArt](https://translate.mattermost.com/user/SiderealArt), [silentyak](https://github.com/silentyak), [sinansonmez](https://github.com/sinansonmez), [Sonichigo](https://github.com/Sonichigo), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [svelle](https://github.com/svelle), [Szymongib](https://github.com/Szymongib), [TQuock](https://github.com/TQuock), [trilopin](https://github.com/trilopin), [tsabi](https://github.com/tsabi), [TylerStilson](https://github.com/TylerStilson), [unode](https://github.com/unode), [vadimasadchi](https://github.com/vadimasadchi), [varghesejose2020](https://github.com/varghesejose2020), [VishakhaPoonia](https://github.com/VishakhaPoonia), [Vovcharaa](https://github.com/Vovcharaa), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [zefhemel](https://github.com/zefhemel)

## Release v6.6 - [Feature Release](/upgrade/release-definitions.html#feature-release)

- **v6.6.2, released 2022-06-13**
  - Mattermost v6.6.2 contains medium severity level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - The value of ``ServiceSettings.TrustedProxyIPHeader`` defaults to empty from now on. A previous bug prevented this from happening
in certain conditions. Customers are requested to check for these values in their config and set them to nil if necessary. See more details [here](/configure/configuration-settings.html#trusted-proxy-ip-header).
  - Fixed a bug that allowed to send test (empty) notifications even if the ``SendPushNotifications`` config was set to ``false``.
- **v6.6.1, released 2022-04-28**
  - Mattermost v6.6.1 contains a medium severity level security fix. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Replaced an expired GPG key which is used to verify the enterprise binary.
  - Fixed an issue with null values in the OAuthApps table's MattermostAppID column, which was introduced in v6.6.0 [MM-43500](https://mattermost.atlassian.net/browse/MM-43500).
  - Fixed an issue where the Workspace Optimization dashboard mentioned that the workspace had reached over 100 users, when fewer than 100 users were registered [MM-43215](https://mattermost.atlassian.net/browse/MM-43215).
- **v6.6.0, released 2022-04-16**
  - Original 6.6.0 release

Mattermost v6.6.0 contains a low severity level security fix. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Compatibility
 - Updated Safari recommended minimum version to v14.1+.

### Important Upgrade Notes
 - The [Apps Framework protocol](https://developers.mattermost.com/integrate/apps/) for binding/form submissions has changed, by separating the single `call` into separate `submit`, `form`, `refresh` and `lookup` calls. If any users have created their own Apps, they have to be updated to the new system.

**IMPORTANT:** If you upgrade from a release earlier than v6.5, please read the other [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).

### Highlights

#### Apps Framework 1.0: General Availability
 - The [Apps Framework](https://developers.mattermost.com/integrate/apps/) allows developers to build integrations with Mattermost that seamlessly work across Mattermost’s desktop and mobile clients. Apps can be developed using any programming language, as opposed to plugins which must be developed in Go.

#### Triggers and Actions
 - Channel admins can now configure [certain actions](/channels/create-channels.html) to be executed automatically based on trigger conditions without writing any code. Users running an older Playbooks release need to upgrade their Playbooks instance to at least v1.26 to take advantage of the channel actions functionality.

#### Actions Restructure
 - The **Actions** menu was restructured to reduce the clutter from Plugins and Apps.

#### Playbook Updates
 - Added [retrospective metrics](/playbooks/metrics-and-goals.html) (Enterprise edition) to track up to four key metrics that indicate performance of every run.

### Improvements

#### User Interface (UI)
 - Pre-packaged Calls v0.4.8 with Mattermost server v6.6 (closed Beta). To participate in Beta testing, please contact [Mattermost](https://mattermost.com/contact-sales/).
 - Added nested previews for permalinks.
 - Added a right-hand side Channel Info panel to see and interact with channel information.
 - Added support for inline editing of posts.
 - Changed the Mattermost indigo theme to match the dark theme in code blocks.
 - Updated in-product links from legacy domain about.mattermost.com to mattermost.com.
 - Made it easier to copy code blocks by adding a copy button on hover.
 - Made it easier to copy a message via a new **Copy Text** post menu item.
 - Added a loading indicator to the **Threads** global list each time more posts are fetched on infinite scroll.
 - Added search guidance to the **Threads** global list when no more posts can be loaded. This is only shown if you’ve scrolled to load older posts and reach the end of the list.
 - Added accessibility support for custom statuses.
 - Tooltip is now only displayed when text is too long in the announcement banner.
 - When restricting direct messages to users on the same team, bots are now excluded from that restriction.
 - Brazilian Portuguese language support was downgraded to Beta.
 
#### Performance
 - Improved performance when clearing notifications with Collapsed Reply Threads enabled.
 - Improved performance of Collapsed Reply Threads when ``ThreadAutoFollow`` is enabled but ``CollapsedThreads`` is disabled.
 - Fixed a potential memory leak in the sidebar when using accessibility hotkeys.
 - Virtualized the emoji picker and added other performance improvements to the emoji picker.
 - Improved the performance of storing users in webapp.
 - Fixed a small memory leak in the **System Console**.

#### Plugins
 - Updated the plugin registry's ``registerCallButtonAction`` method to allow for displaying custom calls buttons in the channel header.
 - Added a debugging setting to turn off client-side plugins for the current user.
 - Added performance metrics related to plugin loading on page load.

#### Administration
 - The default for [``ThreadAutoFollow``](/configure/configuration-settings.html#automatically-follow-threads) has been changed to ``true``. This does not affect existing configurations where this value is already set to ``false``; however, we recommend enabling ``ThreadAutoFollow`` if you plan to enable [Collapsed Reply Threads](/channels/organize-conversations.html) in the future.
 - Improved the license upload flow.
 - The Start Trial CTA presents a modal exposing the benefits the client gets by starting the trial, encouraging Admins to request a trial license and engage them with the product.
 - A new field was added to the client configuration to let clients know the database schema version of the server. The applied database migrations have also been added to the **System Console**.
 - Added a ``Automatically Follow Threads`` configuration setting to the **System Console** to expose the ``threadAutoFollow`` config setting to the User Interface.
 - An error is now shown on the email invitation modal if SMTP is not configured but email invitations are ``true``.
 - Logs from third-party libraries are now included in the default logging configuration.
 - Added additional performance debugging settings.
 - The support email field has moved from **Customization** to **Notifications** in the System Console. Also, a support email is now required when configuring email notifications.
 - The ping endpoint can now receive a device ID, which will report whether the device is able to receive push notifications.
 - [Feature flags](https://developers.mattermost.com/contribute/server/feature-flags/) are now automatically refreshed when the server undergoes a restart.
 - Added a sort order to the category API, and included category data in the websocket category update event.
 - Permissions for private playbooks are now hidden unless running an Enterprise license.

### Bug Fixes
 - Fixed an error that occured when a non-logged-in user attempted to view a page that required being logged in while MFA was required on the server.
 - Fixed an issue where the channel switcher displayed channels from teams the Admin was no longer part of.
 - Fixed an issue where ``ThreadStore.GetThreadsForUser`` did not count correctly when no team ID was specified.
 - Fixed an issue where ``zip`` file creation failed when adding attachments.
 - Fixed an issue where emoji short codes written in Markdown were not added to recently used emojis.
 - Fixed the positioning of SVGs in admin onboarding when the screen doesn't have a previous button.
 - Fixed an issue with the displayed channel name in the channel tutorial tip.
 - Fixed an issue with the clickable area for emojis in the emoji picker to match the interface.
 - Fixed an issue where usernames with periods in the channel switcher input showed Group Messages over matching Direct Messages.
 - Fixed an issue on Collapsed Reply Threads compact message view where clicking on the thread footer avatar did not open the profile modal.
 - Fixed a scan error on column name "LastRootPostAt": converting NULL to int64.
 - Fixed an issue where selecting a custom status from Recent statuses used the original expiration time.
 - Fixed an issue that caused a gap to appear on the left-hand side in products using the team sidebar.
 - Fixed an issue where moving up or down in the channel switcher didn’t work as expected when Global Threads was in the background.
 - Fixed an issue where pressing ENTER opened the onboarding tutorial tip.
 - Fixed an issue where some permission checkboxes had been moved to different categories in the System Console.
 - Fixed an issue where a blank screen occurred upon leaving a currently open unread channel with the channel unread grouping enabled.
 - Fixed an issue related to disabling and re-enabling Custom Terms of Service.
 - Fixed an issue where channel links on hover overlapped the channels menus.
 - Fixed the positioning of the post menu in mobile web view.
 - Fixed an issue where closing the keyboard shortcut modal by "CTRL/CMD + /" didn’t work.
 - Fixed an issue where the channel keyboard navigation was broken in the Threads view.
   
### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:
 - Under ``ServiceSettings`` in ``config.json``:
    - The default for ``ThreadAutoFollow`` has been changed to ``true``. This does not affect existing configurations where this value is already set to ``false``.

### Go Version
 - v6.6 is built with Go ``v1.16.7``.

### Open Source Components
 - Added ``@tippyjs/react``, ``react-popper``, ``react-slidedown`` and ``smooth-scroll-into-view-if-needed`` , and removed ``prettier`` and ``xregexp`` from https://github.com/mattermost/mattermost-webapp.

### Known Issues
 - On subpath, 404 can be seen on OpenID or SAML redirect after changing login method. The login change is successful, and manually adding the subpath name into the URL opens the expected page [MM-43114](https://mattermost.atlassian.net/browse/MM-43114).
 - [Collapsed Reply Threads](/messaging/organizing-conversations.html) is currently in beta. Before enabling the feature, please ensure you are well versed in the [known issues](/messaging/organizing-conversations.html#known-issues), particularly relating to database resource requirements and server performance implications. If you cannot easily scale up your database size, or are running the Mattermost application server and database server on the same machine, we recommended waiting to enable Collapsed Reply Threads until it's [promoted to general availability in Q2 2022](https://mattermost.com/blog/collapsed-reply-threads-ga). Learn more about these [performance considerations here](https://support.mattermost.com/hc/en-us/articles/4413183568276).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - Boards are not refreshing on creation. See the [GitHub discussion](https://github.com/mattermost/focalboard/discussions/1971) for more information.
 - Boards export and reimport duplicates boards because all IDs are replaced by new ones on the server. See the [GitHub issue](https://github.com/mattermost/focalboard/issues/1924) for more information.

### Contributors
 - [AccountingMattermost](https://github.com/AccountingMattermost), [aeomin](https://translate.mattermost.com/user/aeomin/), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [akkivasu](https://github.com/akkivasu), [Alexnoj](https://github.com/Alexnoj), [amyblais](https://github.com/amyblais), [andreygolubkow](https://github.com/andreygolubkow), [asaadmahmood](https://github.com/asaadmahmood), [ashishbhate](https://github.com/ashishbhate), [AshishDhama](https://github.com/AshishDhama), [azigler](https://github.com/azigler), [BenCookie95](https://github.com/BenCookie95), [BenLloydPearson](https://github.com/BenLloydPearson), [blocodenotas](https://github.com/blocodenotas), [bobertoyin](https://github.com/bobertoyin), [Borknab](https://github.com/Borknab), [bpodwinski](https://github.com/bpodwinski), [calebroseland](https://github.com/calebroseland), [CeesJol](https://github.com/CeesJol), [chenilim](https://github.com/chenilim), [ChristieBavelaar](https://github.com/ChristieBavelaar), [cleferman](https://github.com/cleferman), [coltoneshaw](https://github.com/coltoneshaw), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ct7amz](https://translate.mattermost.com/user/ct7amz/), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [darkonovkina](https://translate.mattermost.com/user/darkonovkina/), [debasish4patra](https://github.com/debasish4patra), [devinbinnie](https://github.com/devinbinnie), [dipak-demansol](https://github.com/dipak-demansol), [dontoisme](https://github.com/dontoisme), [DSchalla](https://github.com/DSchalla), [emdecr](https://github.com/emdecr), [emilyacook](https://github.com/emilyacook), [enahum](https://github.com/enahum), [EragonRD](https://github.com/EragonRD), [erdeerdeerde](https://github.com/erdeerdeerde), [ericocesar](https://github.com/ericocesar), [ewwollesen](https://github.com/ewwollesen), [flynbit](https://github.com/flynbit), [fromhro](https://github.com/fromhro), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gbochora](https://github.com/gbochora), [glennschler](https://github.com/glennschler), [gmerz](https://github.com/gmerz), [gyeben](https://github.com/gyeben), [hannaparks](https://github.com/hannaparks), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [htlcnn](https://github.com/htlcnn), [hydeenoble](https://github.com/hydeenoble), [icelander](https://github.com/icelander), [iomodo](https://github.com/iomodo), [isacikgoz](https://github.com/isacikgoz), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [jgilliam17](https://github.com/jgilliam17), [johndavidlugtu](https://github.com/johndavidlugtu), [johnsonbrothers](https://github.com/johnsonbrothers), [jordanafung](https://github.com/jordanafung), [jpetazzo](https://github.com/jpetazzo), [jprusch](https://github.com/jprusch), [JtheBAB](https://github.com/JtheBAB), [JulienTant](https://github.com/JulienTant), [julmondragon](https://github.com/julmondragon), [justinegeffen](https://github.com/justinegeffen), [jwilander](https://github.com/jwilander), [k4awon](https://github.com/k4awon), [kaakaa](https://github.com/kaakaa), [kamre](https://github.com/kamre), [karistuck](https://github.com/karistuck), [kayazeren](https://github.com/kayazeren), [KevinSJ](https://github.com/KevinSJ), [koox00](https://github.com/koox00), [krmh04](https://github.com/krmh04), [kzmi](https://translate.mattermost.com/user/kzmi/), [larkox](https://github.com/larkox), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [lindy65](https://github.com/lindy65), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo/), [maksimatveev](https://github.com/maksimatveev), [marianunez](https://github.com/marianunez), [maruTA-bis5](https://github.com/maruTA-bis5), [master7](https://translate.mattermost.com/user/master7/), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w/), [metanerd](https://github.com/metanerd), [michelengelen](https://github.com/michelengelen), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [mkdbns](https://github.com/mkdbns), [mkraft](https://github.com/mkraft), [Mshahidtaj](https://github.com/Mshahidtaj), [mylonsuren](https://github.com/mylonsuren), [nasermoein](https://github.com/nasermoein), [natalie-hub](https://github.com/natalie-hub), [nathanaelhoun](https://github.com/nathanaelhoun), [neallred](https://github.com/neallred), [nickmisasi](https://github.com/nickmisasi), [nikolaizah](https://github.com/nikolaizah), [Nothing23yeh](https://github.com/Nothing23yeh), [noxer](https://github.com/noxer), [ogi-m](https://github.com/ogi-m), [oh6hay](https://github.com/oh6hay), [pfltdv](https://github.com/pfltdv), [Phrynobatrachus](https://github.com/Phrynobatrachus), [potatogim](https://github.com/potatogim), [pvev](https://github.com/pvev), [ramirezjag00](https://github.com/ramirezjag00), [rodcorsi](https://github.com/rodcorsi), [ruckc](https://github.com/ruckc), [ryoarmanda](https://github.com/ryoarmanda), [saturninoabril](https://github.com/saturninoabril), [sayanta66](https://github.com/sayanta66), [sbishel](https://github.com/sbishel), [sc](https://translate.mattermost.com/user/_sc/), [sibasankarnayak](https://github.com/sibasankarnayak), [sinansonmez](https://github.com/sinansonmez), [spirosoik](https://github.com/spirosoik), [src-r-r](https://github.com/src-r-r), [sri-byte](https://github.com/sri-byte), [sridhar02](https://github.com/sridhar02), [srkgupta](https://github.com/srkgupta), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [superkkt](https://github.com/superkkt), [Szymongib](https://github.com/Szymongib), [ThiefMaster](https://github.com/ThiefMaster), [thorkemado](https://github.com/thorkemado), [tilto0822](https://github.com/tilto0822), [tmotyl](https://github.com/tmotyl), [tomaszn](https://github.com/tomaszn), [TQuock](https://github.com/TQuock), [trilopin](https://github.com/trilopin), [tsabi](https://github.com/tsabi), [vadimasadchi](https://github.com/vadimasadchi), [varghesejose2020](https://github.com/varghesejose2020), [vish9812](https://github.com/vish9812), [VishakhaPoonia](https://github.com/VishakhaPoonia), [wandersiemers](https://github.com/wandersiemers), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [wuwinson](https://github.com/wuwinson), [Zxce3](https://github.com/Zxce3)

## Release v6.5 - [Feature Release](/upgrade/release-definitions.html#feature-release)

- **v6.5.2, released 2022-06-13**
  - Mattermost v6.5.2 contains medium severity level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - The value of ``ServiceSettings.TrustedProxyIPHeader`` defaults to empty from now on. A previous bug prevented this from happening
in certain conditions. Customers are requested to check for these values in their config and set them to nil if necessary. See more details [here](/configure/configuration-settings.html#trusted-proxy-ip-header).
  - Fixed a bug that allowed to send test (empty) notifications even if the ``SendPushNotifications`` config was set to ``false``.
  - The ping endpoint now can receive a device ID, which will report whether the device is able to receive push notifications.
- **v6.5.1, released 2022-04-28**
  - Mattermost v6.5.1 contains a medium severity level security fix. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/). 
  - Fixed an issue on schema migrations where the Mattermost server failed to restart after having an error in the migration process.
  - Fixed an issue where the Get trial endpoint did not seem to complete.
- **v6.5.0, released 2022-03-16**
  - Original 6.5.0 release

Mattermost v6.5.0 contains low to medium severity level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Compatibility
 - Updated the recommended minimum supported Firefox version to v91+.

### Important Upgrade Notes
 - The ``mattermost version`` CLI command does not interact with the database anymore. Therefore the database version is not going to be printed. Also, the database migrations are not going to be applied with the version sub command. [A new db migrate sub command](/manage/command-line-tools.html#mattermost-db-migrate) is added to enable administrators to trigger migrations.

**IMPORTANT:** If you upgrade from a release earlier than v6.4, please read the other [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).

### Highlights

#### Custom User Groups (Beta; Professional and Enterprise Plans)
 - Added the ability to mention a group of members at a time in a workspace. Users can create groups, edit group details, join groups, archive groups, and add group members.

#### Cross-team Channel Navigation
 - You can now find and jump to channels across all your teams by typing any channel name in the **Find Channels** modal.

#### Workspace Optimizations
 - System Admins can now review their overall health and growth scores and take recommended actions for ensuring their workspace is running smoothly, so users can get the most out of Mattermost.

#### Playbook Updates
 - Added a new onboarding tour for Playbooks.
 - Existing playbooks can now be duplicated by copying and modifying your colleague’s processes. Playbooks can also be exported.

#### Boards Updates
 - Added a new onboarding tour for Boards.
 - Improved the share boards user interface.
 - A link to Boards is now included in the channel intro whenever a new channel or direct message is started.
 - Added in-app links to import Help Docs.

### Improvements

#### User Interface (UI)
 - Added Persian as an official supported language (Beta).
 - Added a new onboarding experience for first System Admin user.
 - Added new tutorial tours for Channels, Boards, and Playbooks to help orient first time users.
 - Removed extra telemetry events that were tracked during page loads.
 - Added a feature card slide for Playbooks.
 - Removed ``admin-advisor`` bot's ability to notify admins about missing support email.
 - Clarified in-product error string "Oops!" as "Unable to continue" for both translators and target audiences in cases where a user doesn't have sufficient permissions to add users or guests.
 - Removed incorrect in-product string text from the **Send full message contents** email notification option description displayed via **System Console > Site Configuration > Notifications**.
 - Added the ability to send an unsanitized user to the source user on ``user_updated`` event.
 - In the compact view, the sender's username is now always shown on posts.
 - The post menu is now only rendered on the root post on hover over.
 - Updated a library used for storing drafts and other data in browser storage.
 - Enabled performance telemetry tracking for production deployments not running in developer mode. This telemetry tracking is disabled when telemetry is toggled off.
 - Inactive server email notifications will now be sent to System Admins occasionally if there have been no telemetry events on their server for 100 hours or more. Inactivity is determined by reviewing all activity on the server. This feature can also be disabled using the ``MM_FeatureFlag_EnableInactivityCheckJob`` feature flag.

#### Performance
 - Improved database performance when ``ThreadAutoFollow`` is enabled but ``CollapsedThreads`` is disabled. Learn more about ``ThreadAutoFollow`` and Collapsed Reply Threads [here](/configure/configuration-settings.html#collapsed-reply-threads-beta).
 - Improved perceived typing performance by moving heavy code around and effective memoization related to the textbox component.
 - Fixed a memory leak caused by the post textbox.
 - Reduced the number of menu components listening for keyboard and mouse events.
 - Re-rendering of ``CustomStatusEmoji`` component is now avoided on post hovering.
 - Removed the collapsed sidebar menu from the DOM on sidebar collapse and expand.
 - Re-rendering of ``TextBox`` links component below the post box while typing is now avoided.

#### Plugins
 - Added an ``OnInstall()`` plugin hook.
 - Added an ``OnSendDailyTelemetry()`` plugin hook.
 - Added a new plugin registry entry to append menu items to the user guide dropdown.

### Bug Fixes
 - Fixed an issue with clicking images in the message attachment.
 - Fixed an issue that caused Rudder to create their cookies on the top-level domain when Mattermost was installed on a subdomain.
 - Fixed an issue where **Total Posts** and **Active Users With Posts** graphs did not render in **System Console** > **Team Statistics**.
 - Fixed an issue where telemetry events attempted to get sent even when blocked by an ad blocker.
 - Fixed an issue where the channel switcher stopped showing search results when the first few characters were removed.
 - Fixed an issue where notification sounds didn't trigger on the Desktop App for new accounts.
 - Fixed an issue where users got multiple sounds for a single notification on the Linux Desktop App.
 - Fixed an issue where posting frequent messages to followed threads caused jittery typing.
 - Fixed an issue where the **Add to channel** permission was available in private channels for non-admin users.
 - Fixed an issue where the reply notification setting was still in effect even when Collapsed Reply Threads was enabled.
 - Fixed an issue where running ``mmctl config migrate`` reset the configuration settings to defaults if the settings were already in the database.
 - Fixed an issue where the custom status menu option was missing the "x" to clear status.
 - Fixed an issue where the password reset link was valid for 1 hour instead of 24 hours.
 - Fixed an issue where the Mattermost import failed if an export contained a soft-deleted team.
 - Fixed an issue where search results in the right-hand side did not clear when changing screens from file results to any other.
 - Fixed an issue where an emoji import failed when the emoji name conflicted with a system emoji.
 - Fixed an issue where the **Edition and License** page displayed a prompt to upgrade to Enterprise for servers that already had an E20 license.
   
### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:
 - Under ``ServiceSettings`` in ``config.json``:
   - Added a new ``EnableClientPerformanceDebugging`` setting to enable some options for users on the web app to enable and disable different parts of the web app to help us isolate performance issues while debugging.
   - Added a new ``EnableCustomGroups`` setting to create and delete custom groups and to add and remove custom group members.

#### API Changes
 - Added new endpoint GET /api/v4/users/invalid_emails. This endpoint will return a list of non-guest users who are not in your whitelisted domains on a server where EnableOpenServer is false.
 - Added new API endpoint ``POST /system/onboarding/complete`` to complete onboarding.
 - Added a new API endpoint ``GET api/v4/latest_version`` to fetch the latest Mattermost version.
 - Modified an existing API endpoint ``${baseUrl}/api/v4/channels/search?system_console=false`` and added additional parameters ``${baseUrl}/api/v4/users/me/channels`` to fetch all the channel across teams and ``${baseUrl}/api/v4/users/${userId/channel_members`` to fetch all the channel_members across teams).

#### Websocket Changes
 - Refactored `user-update` websocket event handler to prevent extra get request to server for unsanitized user.
 - Added a new ``ReliableClusterSend`` field to ``model.WebsocketBroadcast`` to allow sending events through the cluster using the reliable channel.

### Go Version
 - v6.5 is built with Go ``v1.16.7``.

### Known Issues
 - The mmctl command built into version v6.5.0 appears to be from v6.4.1 [MM-42588](https://mattermost.atlassian.net/browse/MM-42588).
 - The new onboarding menu icon obscures System Console menu items [MM-42353](https://mattermost.atlassian.net/browse/MM-42353).
 - For Custom Groups, the user activity doesn't sync in two sessions [MM-42242](https://mattermost.atlassian.net/browse/MM-42242).
 - For Custom Groups, the last action popup menu is cut off [MM-42189](https://mattermost.atlassian.net/browse/MM-42189).
 - [Collapsed Reply Threads](/messaging/organizing-conversations.html) is currently in beta. Before enabling the feature, please ensure you are well versed in the [known issues](/messaging/organizing-conversations.html#known-issues), particularly relating to database resource requirements and server performance implications. If you cannot easily scale up your database size, or are running the Mattermost application server and database server on the same machine, we recommended waiting to enable Collapsed Reply Threads until it's [promoted to general availability in Q2 2022](https://mattermost.com/blog/collapsed-reply-threads-ga). Learn more about these [performance considerations here](https://support.mattermost.com/hc/en-us/articles/4413183568276).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - Boards are not refreshing on creation. See the [GitHub discussion](https://github.com/mattermost/focalboard/discussions/1971) for more information.
 - Boards export and reimport duplicates boards because all IDs are replaced by new ones on the server. See the [GitHub issue](https://github.com/mattermost/focalboard/issues/1924) for more information.

### Contributors
 - [97amarnathk](https://github.com/97amarnathk), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [akshitarora921](https://github.com/akshitarora921), [alerque](https://github.com/alerque), [amyblais](https://github.com/amyblais), [andrewbrown00](https://github.com/andrewbrown00), [angeloskyratzakos](https://github.com/angeloskyratzakos), [anurag6713](https://github.com/anurag6713), [asaadmahmood](https://github.com/asaadmahmood), [ashishbhate](https://github.com/ashishbhate), [AshishDhama](https://github.com/AshishDhama), [bbodenmiller](https://github.com/bbodenmiller), [BenCookie95](https://github.com/BenCookie95), [BenLloydPearson](https://github.com/BenLloydPearson), [calebroseland](https://github.com/calebroseland), [CeesJol](https://github.com/CeesJol), [chenilim](https://github.com/chenilim), [chris-nee](https://github.com/chris-nee), [codedsun](https://github.com/codedsun), [coltoneshaw](https://github.com/coltoneshaw), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cvockrodt](https://github.com/cvockrodt), [cwarnermm](https://github.com/cwarnermm), [danielsischy](https://github.com/danielsischy), [debasish4patra](https://github.com/debasish4patra), [devinbinnie](https://github.com/devinbinnie), [dipak-demansol](https://github.com/dipak-demansol), [DIVYA-19](https://github.com/DIVYA-19), [dontoisme](https://github.com/dontoisme), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [EragonRD](https://github.com/EragonRD), [fromhro](https://github.com/fromhro), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gbochora](https://github.com/gbochora), [ggu1012](https://github.com/ggu1012), [gohyinhao](https://github.com/gohyinhao), [GR34SE](https://github.com/GR34SE), [gtapiasgt](https://github.com/gtapiasgt), [gyeben](https://translate.mattermost.com/user/gyeben/), [haardikdharma10](https://github.com/haardikdharma10), [hamzaMM](https://github.com/hamzaMM), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [hojin-kim](https://translate.mattermost.com/user/hojin-kim/), [iomodo](https://github.com/iomodo), [isacikgoz](https://github.com/isacikgoz), [it33](https://github.com/it33), [ITKozak](https://github.com/ITKozak), [jaz-on](https://github.com/jaz-on), [jespino](https://github.com/jespino), [johnsonbrothers](https://github.com/johnsonbrothers), [joriki](https://github.com/joriki), [josephbaylon](https://github.com/josephbaylon), [jprusch](https://github.com/jprusch), [jsoref](https://github.com/jsoref), [JtheBAB](https://github.com/JtheBAB), [JulienTant](https://github.com/JulienTant), [julmondragon](https://github.com/julmondragon), [jupriano](https://github.com/jupriano), [justinegeffen](https://github.com/justinegeffen), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kamre](https://github.com/kamre), [karistuck](https://github.com/karistuck), [kayazeren](https://github.com/kayazeren), [koox00](https://github.com/koox00), [krmh04](https://github.com/krmh04), [krotovkk](https://github.com/krotovkk), [larkox](https://github.com/larkox), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo/), [maksimatveev](https://github.com/maksimatveev), [mamounjamous](https://github.com/mamounjamous), [manojmalik20](https://github.com/manojmalik20), [master7](https://translate.mattermost.com/user/master7/), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w/), [matthewbirtch](https://github.com/matthewbirtch), [maurobraggio](https://github.com/maurobraggio), [metanerd](https://github.com/metanerd), [michelengelen](https://github.com/michelengelen), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [mkraft](https://github.com/mkraft), [mylonsuren](https://github.com/mylonsuren), [nasermoein](https://github.com/nasermoein), [nathanaelhoun](https://github.com/nathanaelhoun), [NathanBnm](https://github.com/NathanBnm), [neallred](https://github.com/neallred), [nevyangelova](https://github.com/nevyangelova), [nickmisasi](https://github.com/nickmisasi), [nikolaizah](https://github.com/nikolaizah), [Nothing23yeh](https://github.com/Nothing23yeh), [ogi-m](https://github.com/ogi-m), [oh6hay](https://github.com/oh6hay), [penthaapatel](https://github.com/penthaapatel), [persian@mattermost.com](https://translate.mattermost.com/user/persiantranslator@mattermost.com/), [persiantranslator@mattermost.com](https://translate.mattermost.com/user/persiantranslator@mattermost.com/), [Phrynobatrachus](https://github.com/Phrynobatrachus), [Pinjasaur](https://github.com/Pinjasaur), [plant99](https://github.com/plant99), [poflankov](https://github.com/poflankov), [potatogim](https://github.com/potatogim), [Profesor08](https://github.com/Profesor08), [pvev](https://github.com/pvev), [rodcorsi](https://github.com/rodcorsi), [Rutam21](https://github.com/Rutam21), [saeid.hmdr](https://translate.mattermost.com/user/saeid.hmdr/), [sargreal](https://github.com/sargreal), [Sayanta66](https://github.com/Sayanta66), [sbishel](https://github.com/sbishel), [scottaudet](https://github.com/scottaudet), [seoyeongeun](https://github.com/seoyeongeun), [serhack](https://github.com/serhack), [sibasankarnayak](https://github.com/sibasankarnayak), [sinansonmez](https://github.com/sinansonmez), [snan](https://github.com/snan), [Sonichigo](https://github.com/Sonichigo), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [superkkt](https://github.com/superkkt), [svelle](https://github.com/svelle), [Szymongib](https://github.com/Szymongib), [ThiefMaster](https://github.com/ThiefMaster), [tilto0822](https://github.com/tilto0822), [TQuock](https://github.com/TQuock), [tsabi](https://github.com/tsabi), [ukewea](https://github.com/ukewea), [varghesejose2020](https://github.com/varghesejose2020), [vinod-demansol](https://github.com/vinod-demansol), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [wuwinson](https://github.com/wuwinson), [zefhemel](https://github.com/zefhemel), [Zxce3](https://translate.mattermost.com/user/Zxce3/).

## Release v6.4 - [Feature Release](/upgrade/release-definitions.html#feature-release)

- **v6.4.3, released 2022-04-28**
  - Mattermost v6.4.3 contains a medium severity level security fix. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue on schema migrations where the Mattermost server failed to restart after having an error in the migration process.
- **v6.4.2, released 2022-03-10**
  - Mattermost v6.4.2 contains medium severity level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where the webapp did not route notifications correctly when the computer was locked.
- **v6.4.1, released 2022-02-25**
  - Fixed a major web and desktop app performance issue for users with a large accumulated number of Direct Messages and Group Messages.
- **v6.4.0, released 2022-02-16**
  - Original 6.4.0 release

Mattermost v6.4.0 contains low severity level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Important Upgrade Notes
 - A new schema migration system has been introduced, so we strongly recommend backing up the database before updating the server to this version. The new migration system will run through all existing migrations to record them to a new table. This will only happen for the first run in order to migrate the application to the new system. The table where migration information is stored is called ``db_migrations``. Additionally, a ``db_lock`` table is used to prevent multiple installations from running migrations in parallel. Any downtime depends on how many records the database has and whether there are missing migrations in the schema. In case of an error while applying the migrations, please check this table first. If you encounter an issue please file [an Issue](https://github.com/mattermost/mattermost-server/issues) by including the failing migration name, database driver/version, and the server logs. 
 - On MySQL, if you encounter an error "Failed to apply database migrations" when upgrading to v6.4.0, it means that there is a mismatch between the table collation and the default database collation. You can manually fix this by changing the database collation with ``ALTER DATABASE <YOUR_DB_NAME> COLLATE = 'utf8mb4_general_ci',``. Then do the server upgrade again and the migration will be successful. 
 - It has been commonly observed on MySQL 8+ systems to have an error ``Error 1267: Illegal mix of collations`` when upgrading due to changing the default collation. This is caused by the database and the tables having different collations. If you get this error, please change the collations to have the same value with, for example, ``ALTER DATABASE <db_name> COLLATE = '<collation>'``.
 - The new migration system requires the MySQL database user to have additional *EXECUTE*, *CREATE ROUTINE*, *ALTER ROUTINE* and *REFERENCES* privileges to run schema migrations.                   

**IMPORTANT:** If you upgrade from a release earlier than v6.3, please read the other [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).

### Highlights

#### Playbook Updates
 - The Team and Starter plans no longer have a limit to the number of playbooks that can be created.

#### Boards Updates
 - Redesigned the Boards template selector to help users find the best template for projects.
 - Board archives now support images. All image attachments on cards will be included the next time a board archive is exported and imported. The archive format is changing with a new ``.boardarchive`` extension and all new exports will only be in this format.
 - Added card badges to indicate the type of content in a card, such as the description, comments, and checklists, without needing to open the card.
 - The entire text on URL properties is now clickable, so users can easily open links from a card without needing to click on a small link icon.
 - GIF file types are now supported as image attachments in card descriptions.

### Improvements

#### User Interface (UI)
 - Updated **Account Settings** terminology to **Settings**.
 - Added Accept-Language header to generate link previews in the default Server language.
 - The **Invite Members** button is now hidden when the Direct Message category is collapsed.
 - Added Collapsed Reply Threads (Beta) tour functionality.
 - Added a keyboard shortcut to open and expand the right-hand pane.
 - UX improvements to the **System Console > Licensing** page: added a new modal for the upload license workflow.

#### Administration
 - Improved plugins performance by re-initializing only after plugin configuration changes.
 - Removed dead struct ``ManifestExecutables``.
 - Added support for exporting and importing the post type and ``edit_at`` post details.
 - Added support for ``postgresql`` schema designator.

### Bug Fixes
 - Fixed an issue where the "Make channel admin" option did not display without a license.
 - Fixed an issue where the user menu header was visible when custom statuses were disabled.
 - Fixed an issue where the "New Replies" banner on the right-hand side was displayed for a thread that was entirely visible.
 - Fixed an issue where the markdown **Preview** link was not hidden in read-only channels.
 - Fixed an issue that caused a gap to appear on the left-hand side in products using the team sidebar.
 - Fixed an issue with Collapsed Reply Threads (Beta) where clearing a deleted root post left the right-hand side blank.
 - Fixed an issue where the **Add** channel member button text was cut off in Safari.
 - Fixed an issue where the file preview modal info bar showed the channel id instead of the channel name for Direct Messages.
 - Fixed an issue to add a loader when fetching data from the backend in the channel switcher if there are no results matching local data.
 - Fixed an issue where the **Get a Public Link** button in the file preview modal was hidden if the image was an external link.
 - Fixed an issue where the click effect on **Copy** invite link button was incorrect.
 - Reinstalling a previously-enabled plugin now correctly reports enabled status as false.
 - Fixed an issue where the Ctrl/Cmd+Shift+A hotkey to open **Settings** didn't work in desktop view.
 - Fixed an issue where the "Leave Channel" button didn't work from the channel sidebar 3-dot menu when clicking on it a second time.
   
### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:
 - Under ``DataRetentionSettings`` in ``config.json``:
   - Added ``EnableBoardsDeletion`` and ``BoardsRetentionDays`` to add support for Global Retention Policy for Boards.

#### API Changes
 - The ``api/v4/config/migrate`` API endpoint has been removed in favor of the mmctl ``--local`` endpoint. API clients won't be able to access this endpoint without having physical access to the server.

### Go Version
 - v6.4 is built with Go ``v1.16.7``.

### Open Source Components
 - Removed ``@formatjs/intl-pluralrules`` and ``@formatjs/intl-relativetimeformat`` from https://github.com/mattermost/mattermost-webapp.
 - Added ``msgpack/msgpack`` and ``pako`` to https://github.com/mattermost/mattermost-mobile.

### Known Issues
 - [Collapsed Reply Threads](/messaging/organizing-conversations.html) is currently in beta. Before enabling the feature, please ensure you are well versed in the [known issues](/messaging/organizing-conversations.html#known-issues), particularly relating to database resource requirements and server performance implications. If you cannot easily scale up your database size, or are running the Mattermost application server and database server on the same machine, we recommended waiting to enable Collapsed Reply Threads until it's [promoted to general availability in Q2 2022](https://mattermost.com/blog/collapsed-reply-threads-ga). Learn more about these [performance considerations here](https://support.mattermost.com/hc/en-us/articles/4413183568276).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - Boards are not refreshing on creation. See the [GitHub discussion](https://github.com/mattermost/focalboard/discussions/1971) for more information.
 - Boards export and reimport duplicates boards because all IDs are replaced by new ones on the server. See the [GitHub issue](https://github.com/mattermost/focalboard/issues/1924) for more information.

### Contributors
 - [3ach](https://github.com/3ach), [abdusabri](https://github.com/abdusabri), [abhijit-singh](https://github.com/abhijit-singh), [adithyaakrishna](https://github.com/adithyaakrishna), [Adovenmuehle](https://github.com/Adovenmuehle), [aeomin](https://github.com/aeomin), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [alauregaillard](https://github.com/alauregaillard), [alieh-rymasheuski](https://github.com/alieh-rymasheuski), [amyblais](https://github.com/amyblais), [anurag6713](https://github.com/anurag6713), [arjitc](https://github.com/arjitc), [asaadmahmood](https://github.com/asaadmahmood), [ashishbhate](https://github.com/ashishbhate), [AshishDhama](https://github.com/AshishDhama), [balajivenkatesh](https://github.com/balajivenkatesh), [BenHargreaves](https://github.com/BenHargreaves), [BenLloydPearson](https://github.com/BenLloydPearson), [bhimeshchauhan](https://github.com/bhimeshchauhan), [bobychaudhary](https://github.com/bobychaudhary), [calebroseland](https://github.com/calebroseland), [ChaseKnowlden](https://github.com/ChaseKnowlden), [chenilim](https://github.com/chenilim), [codedsun](https://github.com/codedsun), [coltoneshaw](https://github.com/coltoneshaw), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [debasish4patra](https://github.com/debasish4patra), [debci](https://translate.mattermost.com/user/debci/), [devinbinnie](https://github.com/devinbinnie), [dfun90](https://github.com/dfun90), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [evil.com](https://translate.mattermost.com/user/evil.com/), [flynbit](https://translate.mattermost.com/user/flynbit/), [frnkshin](https://github.com/frnkshin), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gbochora](https://github.com/gbochora), [gtapias](https://translate.mattermost.com/user/gtapias/), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [icelander](https://github.com/icelander), [iomodo](https://github.com/iomodo), [isacikgoz](https://github.com/isacikgoz), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jayaddison-collabora](https://github.com/jayaddison-collabora), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [jgilliam17](https://github.com/jgilliam17), [jihoon-seo](https://github.com/jihoon-seo), [johnsonbrothers](https://github.com/johnsonbrothers), [josephjosedev](https://github.com/josephjosedev), [jpaldeano](https://github.com/jpaldeano), [jprusch](https://github.com/jprusch), [jsoref](https://github.com/jsoref), [JtheBAB](https://github.com/JtheBAB), [jufab](https://github.com/jufab), [JulienTant](https://github.com/JulienTant), [justinegeffen](https://github.com/justinegeffen), [jwilander](https://github.com/jwilander), [K3UL](https://github.com/K3UL), [kaakaa](https://github.com/kaakaa), [kamre](https://github.com/kamre), [kayazeren](https://github.com/kayazeren), [koox00](https://github.com/koox00), [krmh04](https://github.com/krmh04), [krotovkk](https://github.com/krotovkk), [LaoshuBaby](https://github.com/LaoshuBaby), [larkox](https://github.com/larkox), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [maisnamrajusingh](https://github.com/maisnamrajusingh), [majo](https://translate.mattermost.com/user/majo/), [maksimatveev](https://github.com/maksimatveev), [manojmalik20](https://github.com/manojmalik20), [MarcCeleiro](https://translate.mattermost.com/user/MarcCeleiro/), [marianunez](https://github.com/marianunez), [master7](https://translate.mattermost.com/user/master7/), [matt-w99](https://github.com/matt-w99), [matthewbirtch](https://github.com/matthewbirtch), [matthew-w](https://translate.mattermost.com/user/matthew-w/), [Mercbot7](https://github.com/Mercbot7), [meshal](https://translate.mattermost.com/user/meshal/), [Meshalaw](https://github.com/Meshalaw), [mgdelacroix](https://github.com/mgdelacroix), [michaelgamble](https://github.com/michaelgamble), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [mkbox](https://github.com/mkbox), [mkraft](https://github.com/mkraft), [mxschumacher](https://github.com/mxschumacher), [mylonsuren](https://github.com/mylonsuren), [nathanaelhoun](https://github.com/nathanaelhoun), [neallred](https://github.com/neallred), [nickmisasi](https://github.com/nickmisasi), [ogi-m](https://github.com/ogi-m), [oh6hay](https://github.com/oh6hay), [onoklin](https://github.com/onoklin), [pablovelezvidal](https://github.com/pablovelezvidal), [patatman](https://github.com/patatman), [Phrynobatrachus](https://github.com/Phrynobatrachus), [potatogim](https://github.com/potatogim), [R](https://translate.mattermost.com/user/R/), [RenePinnow](https://github.com/RenePinnow), [ricosega](https://github.com/ricosega), [rinkimekari](https://github.com/rinkimekari), [sadohert](https://github.com/sadohert), [sangramrath](https://github.com/sangramrath), [sanjaydemansol](https://github.com/sanjaydemansol), [saturninoabril](https://github.com/saturninoabril), [Sayanta66](https://github.com/Sayanta66), [sbishel](https://github.com/sbishel), [Schweinepriester](https://github.com/Schweinepriester), [scottaudet](https://github.com/scottaudet), [seoyeongeun](https://github.com/seoyeongeun), [shadowshot-x](https://github.com/shadowshot-x), [shrzkhn](https://github.com/shrzkhn), [sibasankarnayak](https://github.com/sibasankarnayak), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [srkgupta](https://github.com/srkgupta), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [svelle](https://github.com/svelle), [Szymongib](https://github.com/Szymongib), [tilto0822](https://github.com/tilto0822), [TQuock](https://github.com/TQuock), [tsabi](https://github.com/tsabi), [tw-ayush](https://github.com/tw-ayush), [varghesejose2020](https://github.com/varghesejose2020), [venarius](https://github.com/venarius), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [willpwa](https://github.com/willpwa), [Willyfrog](https://github.com/Willyfrog), [wqweto](https://translate.mattermost.com/user/wqweto/), [wuwinson](https://github.com/wuwinson), [zefhemel](https://github.com/zefhemel)

## Release v6.3 - [Extended Support Release](/upgrade/release-definitions.html#extended-support-release-esr)

- **v6.3.10, released 2022-08-23**
  - Mattermost v6.3.10 contains a medium severity level security fix. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
- **v6.3.9, released 2022-06-13**
  - Mattermost v6.3.9 contains medium severity level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - The value of ``ServiceSettings.TrustedProxyIPHeader`` defaults to empty from now on. A previous bug prevented this from happening
in certain conditions. Customers are requested to check for these values in their config and set them to nil if necessary. See more details [here](/configure/configuration-settings.html#trusted-proxy-ip-header).
  - Fixed a bug that allowed to send test (empty) notifications even if the ``SendPushNotifications`` config was set to ``false``.
  - Pre-packaged Playbooks v1.23.2.
- **v6.3.8, released 2022-04-28**
  - Mattermost v6.3.8 contains a medium severity level security fix. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Ping endpoint now can receive a device ID, which will report whether the device is able to receive push notifications.
- **v6.3.7, released 2022-04-13**
  - Fixed an issue where users were able to attempt to create private playbooks with the Professional license.
- **v6.3.6, released 2022-03-24**
  - Fixed an issue with a slow delete of posts and ``context deadline exceeded`` errors after upgrading to v6.3.
  - Fixed an issue where the announcement banner caused the top team to be partially obstructed [MM-40887](https://mattermost.atlassian.net/browse/MM-40887).
- **v6.3.5, released 2022-03-10**
  - Mattermost v6.3.5 contains medium severity level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Improved the performance of code for storing users in the webapp.
  - Fixed a memory leak caused by the post textbox.
  - Removed the collapsed sidebar menu from the DOM on sidebar collapse and expand.
  - Fixed an issue with disabling and re-enabling Custom Terms of Service.
- **v6.3.4, released 2022-02-21**
  - Fixed a major web and desktop app performance issue for users with a large accumulated number of Direct Messages and Group Messages.
  - The right-hand side dot menu of root posts are now rendered to DOM only when hovered upon.
  - The re-rendering of the ``CustomStatusEmoji`` component is now avoided on post hover.
  - The re-rendering of the ``TextBox`` links component below post box is now avoided while typing.
  - Reduced the number of post components listening for keyboard and mouse events.
- **v6.3.3, released 2022-02-03**
  - Mattermost v6.3.3 contains medium level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - The default for ``ThreadAutoFollow`` has been changed to ``false``. This does not affect existing configurations where this value is already set to ``true`` [MM-41351](https://mattermost.atlassian.net/browse/MM-41351). 
  - Prevented some instances where operations relating to Collapsed Reply Threads added load to the database server even when the ``ThreadAutoFollow`` and ``CollapsedThreads`` config settings were disabled [MM-41350](https://mattermost.atlassian.net/browse/MM-41350).
  - ``.pages`` content search is no longer available due to technical difficulties.
  - Fixed an issue where the "New Replies" banner displayed in the right-hand side for threads that were entirely visible [MM-40317](https://mattermost.atlassian.net/browse/MM-40317).
- **v6.3.2, released 2022-01-28**
  - Fixed an issue where MySQL installations re-triggered the v6.0 migration on server restart [MM-41330](https://mattermost.atlassian.net/browse/MM-41330).
  - Fixed an issue where Actiance compliance jobs caused the Mattermost server process to crash with a panic [MM-41245](https://mattermost.atlassian.net/browse/MM-41245).
- **v6.3.1, released 2022-01-21**
  - Mattermost v6.3.1 contains a medium level security fix. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Updated Mattermost Boards to v0.12.1 with various bug fixes.
  - Added the ability to normalize DN strings if they were returned with a different attribute letter casing for LDAP users versus LDAP group members [MM-40753](https://mattermost.atlassian.net/browse/MM-40753).
  - Removed file attachment options in channels when file attachments are disabled on the server [MM-38054](https://mattermost.atlassian.net/browse/MM-38054).
  - Fixed a bug causing the team sidebar to display for servers running in a subpath.
- **v6.3.0, released 2022-01-16**
  - Original 6.3.0 release

### Important Upgrade Notes
 -  [Collapsed Reply Threads](/messaging/organizing-conversations.html), available in beta, are known to have a negative impact on server performance. If you cannot easily scale up and tune your database, or if you are running the Mattermost application server and database server on the same machine, we recommended disabling [``ThreadAutoFollow``](/configure/configuration-settings.html#automatically-follow-threads) and [``CollapsedThreads``](/configure/configuration-settings.html#collapsed-reply-threads-beta) until Collapsed Reply Threads is promoted to general availability in Q2 2022. Learn more about these [performance considerations here](https://support.mattermost.com/hc/en-us/articles/4413183568276).

IMPORTANT: If you upgrade from a release earlier than v6.2, please read the other [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).

### Highlights

#### Playbook Updates
 - (Enterprise Edition) Granular permission schemes enable more access control of playbooks.
 - Playbooks is now completely translatable with over a dozen languages in-progress.
 - All in-channel notifications are removed, with high-value notifications being delivered via direct message from the Playbooks Bot to reduce channel noise. 

#### Boards Updates
 - Boards is now officially in General Availability (GA).
 - Ability to follow cards and get a message notification with details of all the changes made on the card.
 - Ability to quickly identify users and assign them tasks with avatars now supported in the person properties.
 - Newest comments are now sorted at the top to easily find the most recent comment.

### Improvements

#### User Interface (UI)
 - Webapp plugins can now register components in the App Bar on the right-hand side of the screen. This feature is hidden behind a feature flag and disabled by default.
 - Updated “Terms of Service” terminology to “Terms of Use” product-wide.
 - Added threaded replies to search results when Collapsed Reply Threads is enabled.
 - Updated the “One-click reactions on messages” user setting to “Quick reactions on messages”.
 - Added tab focus support to the global header and user avatars.
 - Added a new Replies banner to the right-hand side Thread viewer.
 - Updated the About Mattermost Team Edition modal to change the community link from `mattermost.org` to `mattermost.com/community/`.
 - Invite to team modal now auto-focuses its email search input.

#### Enterprise Edition
 - Added a new dialog for Remove License confirmation.
 - The **Renew Now** button is no longer shown if the license ID does not exist in the portal. Instead, **Contact Sales** is shown.
 - System Admins are now able to upgrade the server to the Enterprise edition and request the trial license with a single click for a simplified user experience.

#### Administration
 - The config setting ``ServiceSettings.EnableReliableWebSockets`` promoted to general availability. For compatibility with older clients, the server will always return ``true`` for the ``/v4/config/client`` endpoint.
 - Added server support for receiving binary (messagepack encoded) WebSocket messages.
 - Added new flag ``showTeamSidebar`` in ``registerProducts``, which, when set to ``true``, displays the team sidebar in the product.
 - Memberlist logs and buckets are now parsed by DEBUG, INFO, WARN, or ERROR appropriately.
 - Increased key length in plugin KV store to 150.

### Bug Fixes
 - Fixed an issue where when selecting the **Upgrade to Enterprise Edition** option. The upgrade progress bar and the **Restart** button were no longer shown once the progress reached 100%.
 - Fixed an issue where the user avatar wasn’t removed from the participants list after the user’s only post in a thread was deleted.
 - Fixed an issue with the exit animation on the invitation modal.
 - Fixed an issue where the status menu unexpectedly closed when selecting the “Disable Notifications Until” header.
 - Fixed an issue where using CMD/CTRL + SHIFT + F in global threads did not add a search term automatically.
 - Fixed the alignment of the “X” button in the “message deleted” system message.
 - Fixed an issue where the long post “Show More/Less” background was broken in the Thread viewer.
 - Changed Client4 to properly set Content-Type as application/json on API calls.
 - Fixed an issue with post hover menu overlap.

### config.json

#### Changes to Team Edition and Enterprise Edition:
- The config setting ``ServiceSettings.EnableReliableWebSockets`` was removed, and the ability to buffer messages during a connection loss has been promoted to general availability. This setting is enabled for older clients to maintain backwards compatibility.

### Go Version
 - v6.3 is built with Go ``v1.16.7``.

### Known Issues
 - Announcement banner can cause the top team to be partially obstructed [MM-40887](https://mattermost.atlassian.net/browse/MM-40887).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - ``CTRL/CMD + SHIFT + A`` shortcut does not open **Account Settings** [MM-38236](https://mattermost.atlassian.net/browse/MM-38236).
 - Known issues related to the Collapsed Reply Threads (Beta) are [listed here](/messaging/organizing-conversations.html#known-issues).
 - Adding an at-mention at the start of a post draft and pressing the leftwards or rightwards arrow can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - Boards are not refreshing on creation. See the [GitHub discussion](https://github.com/mattermost/focalboard/discussions/1971) for more information.
 - Boards export and reimport duplicates boards because all IDs are replaced by new ones on the server. See the [GitHub issue](https://github.com/mattermost/focalboard/issues/1924) for more information.

### Contributors
- [AccountingMattermost](https://github.com/AccountingMattermost), [Adovenmuehle](https://github.com/Adovenmuehle), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [amyblais](https://github.com/amyblais), [amynicol1985](https://github.com/amynicol1985), [asaadmahmood](https://github.com/asaadmahmood), [AshishDhama](https://github.com/AshishDhama), [BenLloydPearson](https://github.com/BenLloydPearson), [calebroseland](https://github.com/calebroseland), [chenilim](https://github.com/chenilim), [ChristophKaser](https://github.com/ChristophKaser), [coltoneshaw](https://github.com/coltoneshaw), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [craph](https://github.com/craph), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet/), [cwarnermm](https://github.com/cwarnermm), [danielsischy](https://github.com/danielsischy), [darmen](https://translate.mattermost.com/user/darmen/), [darmenerk](https://github.com/darmenerk), [deanwhillier](https://github.com/deanwhillier), [devinbinnie](https://github.com/devinbinnie), [dunak-debug](https://github.com/dunak-debug), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [ewwollesen](https://github.com/ewwollesen), [gbochora](https://github.com/gbochora), [Grucqq](https://github.com/Grucqq), [hahmadia](https://github.com/hahmadia), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [iomodo](https://github.com/iomodo), [isacikgoz](https://github.com/isacikgoz), [it33](https://github.com/it33), [jamiehurewitz](https://github.com/jamiehurewitz), [jasonblais](https://github.com/jasonblais), [jayaddison-collabora](https://github.com/jayaddison-collabora), [JenyaFTW](https://github.com/JenyaFTW), [jespino](https://github.com/jespino), [johnsonbrothers](https://github.com/johnsonbrothers), [JoomlaEstonia](https://github.com/JoomlaEstonia), [josephbaylon](https://github.com/josephbaylon), [jprusch](https://github.com/jprusch), [JtheBAB](https://github.com/JtheBAB), [JulienTant](https://github.com/JulienTant), [jupenur](https://github.com/jupenur), [justinegeffen](https://github.com/justinegeffen), [kaakaa](https://github.com/kaakaa), [kamre](https://github.com/kamre), [kayazeren](https://github.com/kayazeren), [koox00](https://github.com/koox00), [krotovkk](https://github.com/krotovkk), [larkox](https://github.com/larkox), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo/), [maksimatveev](https://github.com/maksimatveev), [master7](https://translate.mattermost.com/user/master7/), [mateioprea](https://github.com/mateioprea), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w/), [metanerd](https://github.com/metanerd), [mgdelacroix](https://github.com/mgdelacroix), [michelengelen](https://github.com/michelengelen), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [mjnagel](https://github.com/mjnagel), [mrckndt](https://github.com/mrckndt), [Mshahidtaj](https://github.com/Mshahidtaj), [nab-77](https://github.com/nab-77), [nathanaelhoun](https://github.com/nathanaelhoun), [neallred](https://github.com/neallred), [nickmisasi](https://github.com/nickmisasi), [nikolaizah](https://github.com/nikolaizah), [nishantwrp](https://github.com/nishantwrp), [ogi-m](https://github.com/ogi-m), [olaysco](https://github.com/olaysco), [pablovelezvidal](https://github.com/pablovelezvidal), [Phrynobatrachus](https://github.com/Phrynobatrachus), [poflankov](https://github.com/poflankov), [Profesor08](https://github.com/Profesor08), [puerco](https://github.com/puerco), [rubenmeza](https://github.com/rubenmeza), [sanjaydemansol](https://github.com/sanjaydemansol), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [SebastianSpeitel](https://github.com/SebastianSpeitel), [seoyeongeun](https://translate.mattermost.com/user/seoyeongeun/), [serhack](https://github.com/serhack), [shadowshot-x](https://github.com/shadowshot-x), [shazm](https://github.com/shazm), [sibasankarnayak](https://github.com/sibasankarnayak), [srkgupta](https://github.com/srkgupta), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [Szymongib](https://github.com/Szymongib), [tilto0822](https://github.com/tilto0822), [tsabi](https://github.com/tsabi), [varghese.jose](https://translate.mattermost.com/user/varghese.jose/), [vinod-demansol](https://github.com/vinod-demansol), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [YairFernando67](https://github.com/YairFernando67), [YC](https://github.com/YC)

## Release v6.2 - [Feature Release](/upgrade/release-definitions.html)

- **v6.2.5, released 2022-03-10**
  - Mattermost v6.2.5 contains medium severity level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
- **v6.2.4, released 2022-02-21**
  - Fixed a major web and desktop app performance issue for users with a large accumulated number of Direct Messages and Group Messages.
- **v6.2.3, released 2022-02-03**
  - Mattermost v6.2.3 contains medium level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - The default for ``ThreadAutoFollow`` has been changed to ``false``. This does not affect existing configurations where this value is already set to ``true`` [MM-41351](https://mattermost.atlassian.net/browse/MM-41351). 
  - Prevented some instances where operations relating to Collapsed Reply Threads added load to the database server even when the ``ThreadAutoFollow`` and ``CollapsedThreads`` config settings were disabled [MM-41350](https://mattermost.atlassian.net/browse/MM-41350).
  - ``.pages`` content search is no longer available due to technical difficulties.
  - Fixed an issue where MySQL installations re-triggered the v6.0 migration on server restart [MM-41330](https://mattermost.atlassian.net/browse/MM-41330).
- **v6.2.2, released 2022-01-21**
  - Mattermost v6.2.2 contains a medium level security fix. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue with the v6 migration where the ``Users.Timezone`` column had a default. This affected servers that had Mattermost v4.9 or earlier installed before upgrading to v6.0 or later [MM-39297](https://mattermost.atlassian.net/browse/MM-39297).
  - Fixed an issue where attempting to parse an empty flag resulted in a spurious log line which clogged up the console.
- **v6.2.1, released 2021-12-17**
  - Mattermost v6.2.1 contains a medium level security fix. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where a SIGSEGV error occurred after upgrading to v6.2.0 when plugins were disabled in configuration.
- **v6.2.0, released 2021-12-16**
  - Mattermost v6.2.0 contains low to medium level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Important Upgrade Notes
 -  Channel results in the channel autocomplete will include private channels. Customers using [Bleve](/deploy/bleve-search.html) or [Elasticsearch](/scale/elasticsearch.html) for autocomplete will have to reindex their data to get the new results. Since this can take a long time, we suggest disabling autocomplete and running indexing in the background. When this is complete, re-enable autocomplete. Note that only channel members will see private channel names in autocomplete results.
 -  [Collapsed Reply Threads](/messaging/organizing-conversations.html), available in beta, are known to have a negative impact on server performance. If you cannot easily scale up and tune your database, or if you are running the Mattermost application server and database server on the same machine, we recommended disabling [``ThreadAutoFollow``](/configure/configuration-settings.html#automatically-follow-threads) and [``CollapsedThreads``](/configure/configuration-settings.html#collapsed-reply-threads-beta) until Collapsed Reply Threads is promoted to general availability in Q2 2022. Learn more about these [performance considerations here](https://support.mattermost.com/hc/en-us/articles/4413183568276).

**IMPORTANT:** If you upgrade from a release earlier than v6.1, please read the other [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).

### Highlights

#### Playbook Updates
 - Added the ability to follow playbook runs to stay informed about the procedures you care about.
 - Added other improvements including the ability to search playbooks, share URLs of individual runs and playbooks, and filter runs by playbook.

#### Boards Updates
 - Added a calendar view to stay on track with deadlines.
 - Added the ability to @mention someone on a card with ease.

### Improvements

#### User Interface (UI)
 - Clarified Latex Rendering config setting descriptions and fixed a broken product documentation link.
 - Updated the "One-click reactions on messages" user setting to "Quick reactions on messages".
 - Updated **Account Settings** terminology to **Profile**.
 - Updated instances of **switch** to **navigate**.
 - Updated in-product text terminology to shift from **comments** to **conversations** and **replies**.
 - Added a **Click to open thread** setting for all users, to allow users to click anywhere on a message to open the reply thread.
 - Do Not Disturb option for **Tomorrow** now displays the expiry time.
 - Recent emojis now get updated based on the default selected skin tone.
 - Updated **SingleImageView** to hide the image name for attached images until the image is collapsed.
 - Moved the expand arrow to the left of an image name. 
 - The image expansion icon now appears on image hover.
 - Added online status to profile images on user autocomplete.
 - App Commands now have an option to be opened as modals.
 - Added support for navigating through Collapsed Reply Threads via arrow keys.
 - Added support for focusing the input box in Collapsed Reply Threads while typing.
 - Added support for blurring the input box in Collapsed Reply Threads by pressing ESCAPE.
 - Adjusted the channel override desktop notification preference for Threads.
 - User interface is now improved when no text is set for a custom status.

#### Performance
 - Added a general performance fix for loading the web application and typing.
 - Improved performance while typing by moving some autocomplete layout calculations.
 - Improved performance by reducing DOM usage during render.

#### Enterprise Edition
 - Implemented a new design for the current **Edition and License** System Console page in Self-Hosted installs.

### Bug Fixes
 - Fixed an issue where OpenID redirects didn't work when hosting Mattermost on a subdirectory.
 - Fixed an issue where the webapp crashed sometimes when clicking on an image file from "Recent files".
 - Fixed an issue where the default log rotation file size was mistakenly set to 10GB, and is now reverted back to 100MB.
 - Fixed an issue where emoji reaction buttons on posts did not respect user permissions.
 - Fixed an issue where unchecking the automatic timezone changed the timezone in the selector.
 - Fixed an issue where emoji names were being truncated too soon in the emoji picker.
 - Fixed an issue where the thread footer did not allow the user to follow a Thread.
 - Fixed an issue where the app crashed when switching to Threads view after leaving a channel.
 - Fixed an issue where Mattermost crashed when deleting a root post from Global Threads.
 - Fixed an issue where push notifications did not clear from the lock screen or the notification center with Collapsed Reply Threads enabled.
 - Fixed an issue where Direct Message notifications were missing the sender name with Collapsed Reply Threads enabled.
 - Fixed an issue where keyboard shortcuts were not working with Global Threads.
 - Fixed an issue where API allowed changing the name of the Town Square channel.
 - Fixed an issue where errors were logged if a user disabled notifications.
 - Fixed an issue where a channel was not immediately removed from the sidebar when the current user was removed from it.
 - Fixed a potential server crash when creating or updating posts with permalink previews.
 - Fixed an issue where permalinks created from saved posts did not correctly redirect to the correct team.
 - Fixed an issue where long file extension names pushed out of the bounds of the module.
 - Fixed slow channel loading for instances with website link previews enabled.
 - Removed real-time updates of a couple of features to prevent overloading servers on user updates. The "This channel has guests" indicator and the number of timezones displayed when notifying members of a group will only be updated on channel change now.
   
### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:
 - Under ``ServiceSettings`` in ``config.json``:
   - Added a new config setting ``DeveloperFlags``.
 - Removed ``DesktopLatestVersion`` and ``DesktopMinVersion`` config settings.

### API Changes
 - Added a new ``IsEnterpriseReady()`` plugin API.
 - Added a new ``GET /api/v4/roles`` API endpoint.
 - Added new ``UpdateCustomStatus`` and ``RemoveUserCustomStatus`` plugin APIs for user custom status.
 - Added CRUD methods for user sessions to the plugin API.
 
### Go Version
 - v6.2 is built with Go ``v1.16.7``.

### Known Issues
 - [Collapsed Reply Threads](/messaging/organizing-conversations.html) is currently in beta. Before enabling the feature, please ensure you are well versed in the [known issues](/messaging/organizing-conversations.html#known-issues), particularly relating to database resource requirements and server performance implications. If you cannot easily scale up your database size, or are running the Mattermost application server and database server on the same machine, we recommended waiting to enable Collapsed Reply Threads until it's [promoted to general availability in Q2 2022](https://mattermost.com/blog/collapsed-reply-threads-ga). Learn more about these [performance considerations here](https://support.mattermost.com/hc/en-us/articles/4413183568276).
 - Member type is missing from autocomplete [MM-38989](https://mattermost.atlassian.net/browse/MM-38989).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - ``CTRL/CMD + SHIFT + A`` shortcut does not open **Settings** [MM-38236](https://mattermost.atlassian.net/browse/MM-38236).
 - Adding an at-mention at the start of a post draft and pressing the leftwards or rightwards arrow can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - Boards are not refreshing on creation. See the [GitHub discussion](https://github.com/mattermost/focalboard/discussions/1971) for more information.
 - When selecting the **Upgrade to Enterprise Edition** button, the upgrade progress bar and the restart button are no longer shown once progress reaches 100%. Users can't restart the server directly from the Mattermost user interface, and must restart the server manually.

### Contributors
 - [aaronrothschild](https://github.com/aaronrothschild), [aeomin](https://github.com/aeomin), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [ahills60](https://github.com/ahills60), [alauregaillard](https://github.com/alauregaillard), [amyblais](https://github.com/amyblais), [anchepiece](https://github.com/anchepiece), [angeloskyratzakos](https://github.com/angeloskyratzakos), [anurag6713](https://github.com/anurag6713), [arjitc](https://github.com/arjitc), [asaadmahmood](https://github.com/asaadmahmood), [ashishbhate](https://github.com/ashishbhate), [AshishDhama](https://github.com/AshishDhama), [AWerbrouck](https://github.com/AWerbrouck), [BenCookie95](https://github.com/BenCookie95), [berkeka](https://github.com/berkeka), [bretanac93](https://github.com/bretanac93), [calebroseland](https://github.com/calebroseland), [chenilim](https://github.com/chenilim), [cleferman](https://github.com/cleferman), [clovis1122](https://github.com/clovis1122), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [daovansonbg](https://github.com/daovansonbg), [De1ain](https://github.com/De1ain), [devinbinnie](https://github.com/devinbinnie), [dipak-demansol](https://github.com/dipak-demansol), [dontoisme](https://github.com/dontoisme), [ekl1773](https://github.com/ekl1773), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [enelson720](https://github.com/enelson720), [engineereng](https://github.com/engineereng), [Ericliu1912](https://github.com/Ericliu1912), [erik](https://translate.mattermost.com/user/erik), [erni27](https://github.com/erni27), [esethna](https://github.com/esethna), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [Genei180](https://github.com/Genei180), [gigawhitlocks](https://github.com/gigawhitlocks), [Grucqq](https://github.com/Grucqq), [gtanczyk](https://github.com/gtanczyk), [haardikdharma10](https://github.com/haardikdharma10), [hahmadia](https://github.com/hahmadia), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [iomodo](https://github.com/iomodo), [iOSGeekster](https://github.com/iOSGeekster), [ironbyte](https://github.com/ironbyte), [isacikgoz](https://github.com/isacikgoz), [it33](https://github.com/it33), [ivernus](https://github.com/ivernus), [jamiehurewitz](https://github.com/jamiehurewitz), [jasonblais](https://github.com/jasonblais), [jayaddison-collabora](https://github.com/jayaddison-collabora), [JenyaFTW](https://github.com/JenyaFTW), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [Johennes](https://github.com/Johennes), [johnsonbrothers](https://github.com/johnsonbrothers), [josephbaylon](https://github.com/josephbaylon), [joseph.jose](https://translate.mattermost.com/user/joseph.jose), [jprusch](https://github.com/jprusch), [jrester](https://github.com/jrester), [JtheBAB](https://github.com/JtheBAB), [jufab](https://github.com/jufab), [JulienTant](https://github.com/JulienTant), [jupenur](https://github.com/jupenur), [justinegeffen](https://github.com/justinegeffen), [kaakaa](https://github.com/kaakaa), [kaitrin](https://github.com/kaitrin), [kamre](https://github.com/kamre), [kayazeren](https://github.com/kayazeren), [kayge](https://github.com/kayge), [kirtilodha](https://github.com/kirtilodha), [KKVANONYMOUS](https://github.com/KKVANONYMOUS), [koox00](https://github.com/koox00), [korvmoij](https://github.com/korvmoij), [kott](https://github.com/kott), [KuSh](https://github.com/KuSh), [larkox](https://github.com/larkox), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [LSantos06](https://github.com/LSantos06), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [marcvelasco](https://github.com/marcvelasco), [marianunez](https://github.com/marianunez), [majo](https://translate.mattermost.com/user/majo), [maruTA-bis5](https://github.com/maruTA-bis5), [master7](https://translate.mattermost.com/user/master7), [mathiasvr](https://github.com/mathiasvr), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matt-w99](https://github.com/matt-w99), [metanerd](https://github.com/metanerd), [mgdelacroix](https://github.com/mgdelacroix), [michaelgamble](https://github.com/michaelgamble), [michelengelen](https://github.com/michelengelen), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [mkraft](https://github.com/mkraft), [mr-aboutin](https://github.com/mr-aboutin), [mRuggi](https://github.com/mRuggi), [Mshahidtaj](https://github.com/Mshahidtaj), [namreg](https://github.com/namreg), [nat-gunner](https://github.com/nat-gunner), [nathanaelhoun](https://github.com/nathanaelhoun), [neallred](https://github.com/neallred), [nevyangelova](https://github.com/nevyangelova), [nickmisasi](https://github.com/nickmisasi), [nikolaiz](https://translate.mattermost.com/user/nikolaiz/), [nikolaizah](https://github.com/nikolaizah), [nishantwrp](https://github.com/nishantwrp), [ogi-m](https://github.com/ogi-m), [pablovelezvidal](https://github.com/pablovelezvidal), [pascalhein](https://github.com/pascalhein), [penthaapatel](https://github.com/penthaapatel), [Phrynobatrachus](https://github.com/Phrynobatrachus), [poflankov](https://github.com/poflankov), [prakharporwal](https://github.com/prakharporwal), [Prassud](https://github.com/Prassud), [puerco](https://github.com/puerco), [Quentin](https://translate.mattermost.com/user/Quentin), [rakshit087](https://github.com/rakshit087), [ramiyengar](https://github.com/ramiyengar), [Roy-Orbison](https://github.com/Roy-Orbison), [sadohert](https://github.com/sadohert), [saeid.hmdr](https://translate.mattermost.com/user/saeid.hmdr/), [saeidkh6991](https://github.com/saeidkh6991), [sangramrath](https://github.com/sangramrath), [sarvani1997](https://github.com/sarvani1997), [saturninoabril](https://github.com/saturninoabril), [Sayanta66](https://github.com/Sayanta66), [sbishel](https://github.com/sbishel), [seoyeongeun](https://github.com/seoyeongeun), [serhack](https://github.com/serhack), [shadowshot-x](https://github.com/shadowshot-x), [SharathHuddar](https://github.com/SharathHuddar), [shzmr](https://github.com/shzmr), [sibasankarnayak](https://github.com/sibasankarnayak), [SiderealArt](https://github.com/SiderealArt), [sondv](https://translate.mattermost.com/user/sondv), [spirosoik](https://github.com/spirosoik), [srijit2002](https://github.com/srijit2002), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [Szymongib](https://github.com/Szymongib), [teamzamong](https://github.com/teamzamong), [tsabi](https://github.com/tsabi), [valentinrozman](https://github.com/valentinrozman), [varghese.jose](https://translate.mattermost.com/user/varghese.jose), [vicky-demansol](https://github.com/vicky-demansol), [weblate](https://github.com/weblate), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [YairFernando67](https://github.com/YairFernando67), [YoheiZuho](https://github.com/YoheiZuho), [zchezgi](https://github.com/zchezgi), [Zeezee1210](https://github.com/Zeezee1210), [Ziggiz](https://github.com/Ziggiz)

## Release v6.1 - [Feature Release](/upgrade/release-definitions.html)

- **v6.1.3, released 2022-02-03**
  - Mattermost v6.1.3 contains medium level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - The default for ``ThreadAutoFollow`` has been changed to ``false``. This does not affect existing configurations where this value is already set to ``true`` [MM-41351](https://mattermost.atlassian.net/browse/MM-41351). 
  - Prevented some instances where operations relating to Collapsed Reply Threads added load to the database server even when the ``ThreadAutoFollow`` and ``CollapsedThreads`` config settings were disabled [MM-41350](https://mattermost.atlassian.net/browse/MM-41350).
  - ``.pages`` content search is no longer available due to technical difficulties.
  - Fixed an issue where MySQL installations re-triggered the v6.0 migration on server restart [MM-41330](https://mattermost.atlassian.net/browse/MM-41330).
- **v6.1.2, released 2022-01-21**
  - Mattermost v6.1.2 contains a medium level security fix. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue with the v6 migration where the ``Users.Timezone`` column had a default. This affected servers that had Mattermost v4.9 or earlier installed before upgrading to v6.0 or later [MM-39297](https://mattermost.atlassian.net/browse/MM-39297).
- **v6.1.1, released 2021-12-17**
  - Mattermost v6.1.1 contains medium level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Added a general performance fix for loading the web application and typing.
  - Improved performance while typing by moving some autocomplete layout calculations.
  - Improved performance by reducing DOM usage during render.
  - Removed real-time updates of a couple of features to prevent overloading servers on user updates. The "This channel contains guests" indicator and the number of timezones displayed when notifying members of a group will only be updated on channel change now.
  - Fixed slow channel loading for instances with website link previews enabled.
  - Fixed an issue with Focalboard where an empty white screen appeared in Mattermost desktop app on reload.
  - Fixed an issue where v6.1 reported an incorrect mmctl version.
- **v6.1, released 2021-11-16**
  - Mattermost v6.1.0 contains low level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

### Important Upgrade Notes
 - Please refer to [the schema migration analysis](https://gist.github.com/streamer45/997b726a86b5d2a624ac2af435a66086) when upgrading to v6.1.
 - The Bleve index has been updated to use the scorch index type. This new default index type features some efficiency improvements which means that the indexes use significantly less disk space. To use this new type of index, after upgrading the server version, run a purge operation and then a reindex from the Bleve section of the System Console. Bleve is still compatible with the old indexes, so the currently indexed data will work fine if the purge and reindex is not run.
 - A composite index has been added to the jobs table for better query performance. For some customers with a large jobs table, this can take a long time, so we recommend adding the index during off-hours, and then running the migration. A table with more than 1 million rows can be considered as large enough to be updated prior to the upgrade.
   - For PostgreSQL: ``create index concurrently idx_jobs_status_type on jobs (status,type);``
   - For MySQL: ``create index idx_jobs_status_type on Jobs (Status,Type);``
 - [Collapsed Reply Threads](/messaging/organizing-conversations.html), available in beta, are known to have a negative impact on server performance. If you cannot easily scale up and tune your database, or if you are running the Mattermost application server and database server on the same machine, we recommended disabling [``ThreadAutoFollow``](/configure/configuration-settings.html#automatically-follow-threads) and [``CollapsedThreads``](/configure/configuration-settings.html#collapsed-reply-threads-beta) until Collapsed Reply Threads is promoted to general availability in Q2 2022. Learn more about these [performance considerations here](https://support.mattermost.com/hc/en-us/articles/4413183568276).

**IMPORTANT:** If you upgrade from a release earlier than v6.0, please read the other [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).

### Highlights

#### Timed Do Not Disturb
 - Added the ability to disable all notifications for a specified period of time to avoid distractions, without losing important messages when you're back.

#### Cross-team Recent Mentions
 - Recent mentions and saved posts now show across all teams.

#### Playbooks Updates
 - Added a wiki-style page with a playbook preview as well as new playbook notifications.

#### Boards Updates
 - Added a new create board user interface, Board calculations to quickly get basic metrics on projects, at-mention notifications, as well as card previews.

### Improvements

#### User Interface (UI)
 - Polish is promoted to an officially supported language.
 - Added one-click reactions for posts. A user's three most recently used emojis display when the user hovers over a message.
 - Added support for selecting names and aliases in the emoji picker.
 - Changed the user interface of the edit-indicator of posts and moved it inline.
 - Added a query param to translate in-product help pages when opened from the Desktop App.
 - Updated in-product text for the invitation modal for clarity.
 - Updated the file attachment limits and sizes within in-product help documentation.
 - Added rendering for posts containing markdown in email notifications.
 - Added support for inline Latex rendering.
 - Added the **Move to...** option menu item to the channel header dropdown.
 - Added keyboard shortcuts to tooltips. The shortcut key component is now used for displaying keys.
 - Added support for Global threads infinite scroll.
 - Added ``@here`` mention to the ``EnableConfirmNotificationsToChannel`` config setting to show a warning modal when over 5 members might be alerted with ``@here``.

#### Integrations
 - Added support for multi-select on Apps slash commands.
 - App commands now make a distinction between the central channel and the right-hand side channel.
 - App bindings now recognize the post menu options for each channel they live in.
 - Added new ``registerMessageWillBeUpdatedHook(newPost, oldPost)`` client-side plugin hook to intercept edited messages.

#### Performance
 - Improved performance around rendering of system messages.
 - Reduced storage-related slow-downs on page load.

#### Administration
 - Bulk imports with attached files now log and continue when a file fails to upload instead of halting.
 - ``get flagged posts`` endpoint will now return only flagged posts for channels the user is a member of.
 - Updated Bleve to v2 to use the scorch index type.
 - Minimum supported browser versions changes:
   - Chrome updated from ``61+`` to ``89+``.
   - Firefox updated from ``60+`` to ``78+``.
   - MacOS updated from ``10.9+`` to ``10.14+``.

#### Enterprise Edition
 - Once the user has selected **Start Trial**, they will see a modal that lists all of the features now available to them through the Enterprise plan.
 - Once a non-licensed server has reached 10 users, a one-time modal is displayed to System Admins encouraging them to start a 30-day trial.
 - Prometheus metrics are now enabled when running a standalone jobserver.

### Bug Fixes
 - Fixed a broken link to the **Custom Emoji** page on servers with a subpath configured.
 - Fixed an issue where a "No results found" error string was displayed in the **Direct Messages** modal.
 - Fixed an issue where the caret was placed in the middle of the emojis when picking two emojis from the emoji picker.
 - Fixed an issue where **System Console > Channels > Channel Management** displayed an option to toggle group management in Team Edition, Starter, and Professional.
 - Fixed an issue where the channel switcher was missing the "(You)" indicator on the user's own Direct Message channel.
 - Fixed an issue where the clock format set by the user was not respected on the edit indicator popover.
 - Replaced Metropolis font files with a new set to correct a kerning issue.
 - Fixed an issue where deep links opened on mobile displayed an incorrect message directing users to open the Desktop app.
 - Addressed various user interface style bugs from v6.0 release.
 - Fixed emails templates for clients that do not support the ``style`` tag.
 - Fixed an issue where the scrollbar was hardly visible with Denim & Sapphire themes.
 - Fixed an issue where creating a bot with an invalid username returned an "invalid email" error.
 - Fixed an issue where using ``/code`` did not render initial whitespace characters.
 - Fixed an issue where **Try Enterprise for Free** option was missing spacing in mobile webview.
 - Fixed an issue where the SQLStore cache was relied on when populating the WebConn channel memberships.
 - Fixed an issue where logging was not re-configured when the server config was changed via the System Console.
 - Fixed a display issue with the Indigo theme when returning from Playbooks to Channels.
 - Fixed an issue where the offline indicator color did not use the correct theme color.
 - Fixed various bugs for the Collapsed Reply Threads (Beta) feature, including:
    - Fixed an issue where the recent sidebar sorting option didn't only consider parent posts.
    - Fixed an issue where a badge was displayed on a thread list when the thread was started by another user in a Direct Message.
    - Fixed an issue where the user avatar was displayed in the participants list after their post was deleted when the user had no other posts in the thread.
    - Fixed an issue where the ephemeral message was not displyaed as the centre post.
    - Fixed an issue with dragging and dropping files on a thread while on the Threads panel.
    - Fixed an issue where permalinks were not highlighting a post on a thread that was already open on the right-hand side.
    - Fixed an issue with missing threads in the Threads list.
   
### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:
 - Under ``ServiceSettings`` in ``config.json``:
   - Added ``EnableInlineLatex`` to add support for inline Latex rendering.
 - Under ``JobSettings`` in ``config.json``
   - Added ``CleanupJobsThresholdDays``. This defines the time gap in days beyond which older jobs will be removed. Default is -1 which means the feature is disabled. Setting to 0 will clean all completed jobs.
   
#### Database Changes
 - Extended the maximum size to 256 characters for the following database columns:
    - ``Sessions.Roles``
    - ``ChannelMembers.Roles``
    - ``TeamMembers.Roles``

### API Changes
 - Added a new API endpoint ``POST /api/v4/posts/search`` to perform searches across all channels.
 
### Go Version
 - v6.1 is built with Go ``v1.16.7``.

### Open Source Components
 - Added ``fast-deep-equal``, ``luxon``, and ``react-window-infinite-loader`` to https://github.com/mattermost/mattermost-webapp.
 - Added ``@mattermost/react-native-paste-input`` to https://github.com/mattermost/mattermost-mobile.

### Known Issues
 - [Collapsed Reply Threads](/messaging/organizing-conversations.html) is currently in beta. Before enabling the feature, please ensure you are well versed in the [known issues](/messaging/organizing-conversations.html#known-issues),  particularly relating to database resource requirements and server performance implications. If you cannot easily scale up your database size, or are running the Mattermost application server and database server on the same machine, we recommended waiting to enable Collapsed Reply Threads until it's [promoted to general availability in Q2 2022](https://mattermost.com/blog/collapsed-reply-threads-ga/). Learn more about these [performance considerations here](https://support.mattermost.com/hc/en-us/articles/4413183568276).
 - Created permalinks from saved posts do not correctly redirect to the correct team [MM-39816](https://mattermost.atlassian.net/browse/MM-39816).
 - Recent Mentions search sometimes includes incorrect results [MM-39867](https://mattermost.atlassian.net/browse/MM-39867).
 - Experimental timezones and custom statuses can cause an increase in CPU usage and database connections for servers with an E20 license. A current workaround is to disable custom statuses or to disable experimental timezones.
 - Webapp sometimes crashes when clicking an image from "Recent files" [MM-38239](https://mattermost.atlassian.net/browse/MM-38239).
 - Member type is missing from autocomplete [MM-38989](https://mattermost.atlassian.net/browse/MM-38989).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - ``Ctrl/Cmd+Shift+A`` shortcut does not open **Account Settings** [MM-38236](https://mattermost.atlassian.net/browse/MM-38236).
 - Adding an at-mention at the start of a post draft and pressing the leftwards or rightwards arrow can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.

### Contributors
 - [A9u](https://github.com/A9u), [aaronrothschild](https://github.com/aaronrothschild), [abhijit-singh](https://github.com/abhijit-singh), [achie27](https://github.com/achie27), [achromik](https://translate.mattermost.com/user/achromik/), [adithyaakrishna](https://github.com/adithyaakrishna), [Adovenmuehle](https://github.com/Adovenmuehle), [aeomin](https://github.com/aeomin), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [alauregaillard](https://github.com/alauregaillard), [alejandrovelez7](https://github.com/alejandrovelez7), [alieh-rymasheuski](https://github.com/alieh-rymasheuski), [aloks98](https://github.com/aloks98), [amyblais](https://github.com/amyblais), [anchepiece](https://github.com/anchepiece), [andrewbrown00](https://github.com/andrewbrown00), [angeloskyratzakos](https://github.com/angeloskyratzakos), [anoopmsivadas](https://github.com/anoopmsivadas), [anurag6713](https://github.com/anurag6713), [asaadmahmood](https://github.com/asaadmahmood), [ashishbhate](https://github.com/ashishbhate), [AshishDhama](https://github.com/AshishDhama), [astraldawn](https://github.com/astraldawn), [audreyaudz](https://github.com/audreyaudz), [Audrey Kon](https://github.com/audreyaudz), [Avinaba-Mazumdar](https://github.com/Avinaba-Mazumdar), [avinashlng1080](https://github.com/avinashlng1080), [AWerbrouck](https://github.com/AWerbrouck), [b4sen](https://github.com/b4sen), [banaboi](https://github.com/banaboi), [bartfelder](https://github.com/bartfelder), [bbodenmiller](https://github.com/bbodenmiller), [BenCookie95](https://github.com/BenCookie95), [BenLloydPearson](https://github.com/BenLloydPearson), [bensiauu](https://github.com/bensiauu), [berkeka](https://github.com/berkeka), [bhaveshgoyal182](https://github.com/bhaveshgoyal182), [Bhavin789](https://github.com/Bhavin789), [Bruno-366](https://github.com/Bruno-366), [calebroseland](https://github.com/calebroseland), [caugner](https://github.com/caugner), [chenilim](https://github.com/chenilim), [chetanyakan](https://github.com/chetanyakan), [chrysillala](https://github.com/chrysillala), [cinlloc](https://github.com/cinlloc), [cleferman](https://github.com/cleferman), [cognvn](https://github.com/cognvn), [coltoneshaw](https://github.com/coltoneshaw), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [craph](https://github.com/craph), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [darkLord19](https://github.com/darkLord19), [DarshanKansara2015](https://github.com/DarshanKansara2015), [deanwhillier](https://github.com/deanwhillier), [DeeJayBro](https://github.com/DeeJayBro), [devinbinnie](https://github.com/devinbinnie), [dialvarezs](https://github.com/dialvarezs), [dimitraz](https://github.com/dimitraz), [dizlv](https://github.com/dizlv), [donno2048](https://github.com/donno2048), [drobiu](https://github.com/drobiu), [Duaard](https://github.com/Duaard), [echobash](https://github.com/echobash), [elyscape](https://github.com/elyscape), [emdecr](https://github.com/emdecr), [emilyacook](https://github.com/emilyacook), [enahum](https://github.com/enahum), [enelson720](https://github.com/enelson720), [EranKricheli](https://github.com/EranKricheli), [erezo9](https://github.com/erezo9), Erik Pfeiffer, [esethna](https://github.com/esethna), [fareskalaboud](https://github.com/fareskalaboud), [fcoiuri](https://github.com/fcoiuri), [firasm](https://github.com/firasm), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gagandeepp](https://github.com/gagandeepp), [garanews](https://github.com/garanews), [gaurav-baghel](https://github.com/gaurav-baghel), [Gauravsaha-97](https://github.com/Gauravsaha-97), [GianOrtiz](https://github.com/GianOrtiz), [gigawhitlocks](https://github.com/gigawhitlocks), [gpt14](https://github.com/gpt14), [grsky360](https://github.com/grsky360), [gupsho](https://github.com/gupsho), [haardikdharma10](https://github.com/haardikdharma10), [hahmadia](https://github.com/hahmadia), [hanzei](https://github.com/hanzei), [Hard-Coder05](https://github.com/Hard-Coder05), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [Hridoy-31](https://github.com/Hridoy-31), [iamquang95](https://github.com/iamquang95), [icelander](https://github.com/icelander), [igordsm](https://github.com/igordsm), [im-endangered](https://github.com/im-endangered), [iomodo](https://github.com/iomodo), [iOSGeekster](https://github.com/iOSGeekster), [isacikgoz](https://github.com/isacikgoz), [jamiehurewitz](https://github.com/jamiehurewitz), [Jasmin F](https://github.com/jasmezz), [jasonblais](https://github.com/jasonblais), [jayaddison-collabora](https://github.com/jayaddison-collabora), [JenyaFTW](https://github.com/JenyaFTW), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [jlram](https://github.com/jlram), [Johennes](https://github.com/Johennes), [johnsonbrothers](https://github.com/johnsonbrothers), [joremysh](https://github.com/joremysh), [josephbaylon](https://github.com/josephbaylon), [joshalling](https://github.com/joshalling), [jprusch](https://github.com/jprusch), [JtheBAB](https://github.com/JtheBAB), [jufab](https://github.com/jufab), [jupenur](https://github.com/jupenur), [justinegeffen](https://github.com/justinegeffen), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kaitrin](https://github.com/kaitrin), [kamre](https://github.com/kamre), [kanitmann](https://github.com/kanitmann), [KavyaJaiswal](https://github.com/KavyaJaiswal), [kayazeren](https://github.com/kayazeren), [koox00](https://github.com/koox00), [korvmoij](https://translate.mattermost.com/user/korvmoij/), [krmh04](https://github.com/krmh04), [KuSh](https://github.com/KuSh), [larkox](https://github.com/larkox), [leosunmo](https://github.com/leosunmo), [levb](https://github.com/levb), [lex111](https://github.com/lex111), [lieut-data](https://github.com/lieut-data), [lindy65](https://github.com/lindy65), [lonnelars](https://github.com/lonnelars), [LSantos06](https://github.com/LSantos06), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [maisnamrajusingh](https://github.com/maisnamrajusingh), [majo](https://translate.mattermost.com/user/majo/), [maknop](https://github.com/maknop), [marcvelasco](https://github.com/marcvelasco), [marianunez](https://github.com/marianunez), [Mark E Fuller](https://github.com/mefuller), [Markus Hermann](https://github.com/MarHerUMR), [maruTA-bis5](https://github.com/maruTA-bis5), [master7](https://translate.mattermost.com/user/master7/), [mathiasvr](https://github.com/mathiasvr), [matt-w99](https://github.com/matt-w99), [matthewbirtch](https://github.com/matthewbirtch), [Matthew Williams](https://github.com/matthew-w), [metanerd](https://github.com/metanerd), [mgdelacroix](https://github.com/mgdelacroix), [michelengelen](https://github.com/michelengelen), [michizhou](https://github.com/michizhou), [mickmister](https://github.com/mickmister), [mishmanners](https://github.com/mishmanners), [mjnagel](https://github.com/mjnagel), [mkraft](https://github.com/mkraft), [mohitsaxenaknoldus](https://github.com/mohitsaxenaknoldus), [Mshahidtaj](https://github.com/Mshahidtaj), [NakulChauhan2001](https://github.com/NakulChauhan2001), [naltang](https://github.com/naltang), [namreg](https://github.com/namreg), [naresh1205](https://github.com/naresh1205), [nathanaelhoun](https://github.com/nathanaelhoun), [neallred](https://github.com/neallred), [NeroBurner](https://github.com/NeroBurner), [nevyangelova](https://github.com/nevyangelova), [ngmmartins](https://github.com/ngmmartins), [nishantwrp](https://github.com/nishantwrp), [noviicee](https://github.com/noviicee), [ogi-m](https://github.com/ogi-m), [pablovelezvidal](https://github.com/pablovelezvidal), [pascalhein](https://github.com/pascalhein), [pawankm21](https://github.com/pawankm21), [penthaapatel](https://github.com/penthaapatel), [Phrynobatrachus](https://github.com/Phrynobatrachus), [pikami](https://github.com/pikami), [pjenicot](https://github.com/pjenicot), [poflankov](https://github.com/poflankov), [prabhigupta](https://github.com/prabhigupta), [prakharporwal](https://github.com/prakharporwal), [prapti](https://github.com/prapti), [Privatecoder](https://github.com/Privatecoder), [prograde](https://translate.mattermost.com/user/prograde/), [puerco](https://github.com/puerco), [radiantly](https://github.com/radiantly), [rafaeelaudibert](https://github.com/rafaeelaudibert), [Ray0Emma](https://github.com/Ray0Emma), [rbradleyhaas](https://github.com/rbradleyhaas), [rootbid](https://github.com/rootbid), [Roy-Orbison](https://github.com/Roy-Orbison), [rutulganatra](https://github.com/rutulganatra), [s4kh](https://github.com/s4kh), [sadohert](https://github.com/sadohert), [sahil9001](https://github.com/sahil9001), [sakaitsu](https://github.com/sakaitsu), [sangramrath](https://github.com/sangramrath), [sanjaydemansol](https://github.com/sanjaydemansol), [sapora1](https://github.com/sapora1), [saturninoabril](https://github.com/saturninoabril), [Sayanta66](https://github.com/Sayanta66), [sbishel](https://github.com/sbishel), [seoyeongeun](https://github.com/seoyeongeun), [shadowshot-x](https://github.com/shadowshot-x), [shazm](https://github.com/shazm), [shinnlok](https://github.com/shinnlok), [shzmr](https://github.com/shzmr), [sibasankarnayak](https://github.com/sibasankarnayak), [spinales](https://github.com/spinales), [spirosoik](https://github.com/spirosoik), [srijit2002](https://github.com/srijit2002), [ssensalo](https://github.com/ssensalo), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [svelle](https://github.com/svelle), [syauqy](https://github.com/syauqy), [Szymongib](https://github.com/Szymongib), [TautZuk](https://github.com/TautZuk), [teamzamong](https://translate.mattermost.com/user/teamzamong/), [TheLaw1337](https://github.com/TheLaw1337), [tiago154](https://github.com/tiago154), [triogempar](https://github.com/triogempar), [tsabi](https://github.com/tsabi), [ucyang](https://github.com/ucyang), [vblz](https://github.com/vblz), [vinod-demansol](https://github.com/vinod-demansol), [void-hr](https://github.com/void-hr), [weblate](https://github.com/weblate), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [xMicky24GIT](https://github.com/xMicky24GIT), [yeongeun.seo](https://github.com/seoyeongeun),  [ZeeshanAmjad0495](https://github.com/ZeeshanAmjad0495), [Zeezee1210](https://github.com/Zeezee1210), [zefhemel](https://github.com/zefhemel), [zolikonta](https://github.com/zolikonta), [zulmarij](https://github.com/zulmarij)
 
## Release v6.0 - [Feature Release](/upgrade/release-definitions.html)

- **v6.0.4, released 2021-12-17**
  - Mattermost v6.0.4 contains medium level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Added a general performance fix for loading the web application and typing.
  - Improved performance while typing by moving some autocomplete layout calculations.
  - Improved performance by reducing DOM usage during render.
  - Removed real-time updates of a couple of features to prevent overloading servers on user updates. The "This channel contains guests" indicator and the number of timezones displayed when notifying members of a group will only be updated on channel change now.
  - Fixed slow channel loading for instances with website link previews enabled.
  - Fixed an issue where v6.0 reported an incorrect mmctl version.
- **v6.0.3, released 2021-11-15**
  - Mattermost v6.0.3 contains a medium level security fix. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed a possible panic during data retention jobs when ``DataRetentionSettings.EnableMessageDeletion`` was set to ``true`` [MM-39378](https://mattermost.atlassian.net/browse/MM-39378).
  - Fixed a potential panic during the message export job [MM-39521](https://mattermost.atlassian.net/browse/MM-39521).
  - Fixed some sentry crashes [MM-38565](https://mattermost.atlassian.net/browse/MM-38565), [MM-39208](https://mattermost.atlassian.net/browse/MM-39208), [MM-39420](https://mattermost.atlassian.net/browse/MM-39420).
- **v6.0.2, released 2021-10-27**
  - Mattermost v6.0.2 contains medium level security fixes. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed a race condition in telemetry IDs on High Availability servers [MM-39343](https://mattermost.atlassian.net/browse/MM-39343).
  - Update prepackaged Boards version to 0.9.4.
- **v6.0.1, released 2021-10-18**
  - Mattermost v6.0.1 contains a medium level security fix. [Upgrading](/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed a panic in translations that caused the server to not run properly. The panic caused the server to be terminated [MM-39299](https://mattermost.atlassian.net/browse/MM-39299).
  - Fixed an issue with the v6.0 migration where the ``Users.Timezone`` column had a default. This affected servers that had Mattermost v4.9 or earlier installed before upgrading [MM-39297](https://mattermost.atlassian.net/browse/MM-39297).
  - Fixed an issue where a migration check failed for MariaDB databases. The data type JSON was aliased to ``LONGTEXT`` and the check was failing and causing the database migrations to run every restart.
  - Added a fix to display ``tableName`` and ``columnName`` for JSONB schema failures. When there was a schema upgrade failure related to jsonb columns, the log line didn't mention which table/column was affected.
  - Fixed an issue where selecting the "..." post menu on a System message crashed the webapp [MM-39116](https://mattermost.atlassian.net/browse/MM-39116).
- **v6.0.0, released 2021-10-13**
  - Original 6.0.0 release

### Deprecations

1. [Legacy Command Line Tools](/manage/command-line-tools.html). Most commands have been replaced by [mmctl](/manage/mmctl-command-line-tool.html) and new commands have been added over the last few months, making this tool a robust replacement.

2. [Slack Import via the web app](/onboard/migrating-to-mattermost.html#migrating-from-slack-using-the-mattermost-web-app). The Slack import tool accessible via the Team Setting menu has been replaced by the [mmetl](/onboard/migrating-to-mattermost.html#migrating-from-slack-using-the-mattermost-mmetl-tool-and-bulk-import) tool that is much more comprehensive for the types of data it can assist in uploading. 

3. MySQL versions below 5.7.12. Minimum support is now for 5.7.12+. This version introduced a native JSON data type that lets us improve performance and scalability of several database fields (most notably Users and Posts props). Additionally, version 5.6 (our current minimum version) reached [EOL in February 2021](https://www.mysql.com/support/eol-notice.html).

4. Elasticsearch 5 and 6 - [versions 5.x reached EOL in March of 2019, and versions 6.x reached EOL in November 2020](https://www.elastic.co/support/eol). Our minimal supported version with Mattermost v6.0 is Elasticsearch version 7.0.

5. Windows 7 reached [EOL in January 2020](https://support.microsoft.com/en-us/windows/windows-7-support-ended-on-january-14-2020-b75d4580-2cc7-895a-2c9c-1466d9a53962). We no longer provide support for Mattermost Desktop App issues on Windows 7.

6. [DisableLegacyMFAEndpoint](/configure/configuration-settings.html#disable-legacy-mfa-api-endpoint) configuration setting.

7. [ExperimentalTimezone](/configure/configuration-settings.html#timezone) configuration setting. The config setting is removed and the feature is promoted to general availability.

8. All legacy channel sidebar experimental configuration settings. We encourage customers using these settings to upgrade to v5.32 or later to access [custom, collapsible channel categories](https://mattermost.com/blog/custom-collapsible-channel-categories/) among many other channel organization features. The deprecated settings include:

   - [EnableLegacySidebar](/configure/configuration-settings.html#enable-legacy-sidebar)
   - [ExperimentalTownSquareIsReadOnly](/configure/configuration-settings.html#town-square-is-read-only-experimental) (Please see [channel moderation settings](/onboard/advanced-permissions.html#read-only-channels), which allow you to set any channel as read-only, including Town Square) 
   - [ExperimentalHideTownSquareinLHS](/configure/configuration-settings.html#town-square-is-hidden-in-left-hand-sidebar-experimental)
   - [EnableXToLeaveChannelsFromLHS](/configure/configuration-settings.html#enable-x-to-leave-channels-from-left-hand-sidebar-experimental)
   - [CloseUnusedDirectMessages](/configure/configuration-settings.html#autoclose-direct-messages-in-sidebar-experimental)
   - [ExperimentalChannelOrganization](/configure/configuration-settings.html#sidebar-organization)
   - [ExperimentalChannelSidebarOrganization](/configure/configuration-settings.html#experimental-sidebar-features)

9. [All configuration settings previously marked as “Deprecated”](/configure/configuration-settings.html#deprecated-configuration-settings).

10. Changes to ``mattermost-server/model`` for naming consistency.

### Important Upgrade Notes

 - Longer migration times can be expected. See [this document](https://gist.github.com/streamer45/59b3582118913d4fc5e8ff81ea78b055) for the estimated upgrade times with datasets of 10+ million posts. See [this document](https://gist.github.com/streamer45/868c451164f6e8069d8b398685a31b6e) for the estimated upgrade times with datasets of 70+ million posts. The field type of Data in model.ClusterMessage was changed to []byte from string. Therefore, a major thing to note is that a v6 server is incompatible to run along with a v5 server in a cluster. Customers upgrading from 5.x to 6.x cannot do a High Availability upgrade. While upgrading, it is required that no other v5 server runs when a v6 server is brought up. A v6 server will run significant database schema changes that can cause a large startup time depending on the dataset size. Zero downtime will not be possible, but depending on the efforts made during the migration process, it can be minimized to a large extent. It is recommended to start Mattermost directly and not through systemctl to avoid the server process getting killed during the migration. This can happen since the value of ``TimeoutStartSec`` in the provided systemctl service file is set to 1 hour. Customers using the Mattermost Kubernetes operator should be aware of the above migration information and choose the path that is most appropriate for them. If (1) is acceptable, then the normal upgrade process using the operator will suffice. For minimum downtime, follow (2) before using the operator to update Mattermost following the normal upgrade process.
   1. Low effort, long downtime - This is the usual process of starting a v6 server normally. This has 2 implications: during the migration process, various tables will be locked which will render those tables read-only during that period. Secondly, once the server finishes migration and starts the application, no other v5 server can run in the cluster.
   2. Medium effort, medium downtime - This process will require SQL queries to be executed manually on the server. To avoid causing a table lock, a customer can choose to use the pt-online-schema-change tool for MySQL. For Postgres, the table locking is very minimal. The advantage is that since there are a lot of queries, the customer can take their own time to run individual queries during off-hours. All queries except #11 are safe to be executed this way. Then the usual method of (1) can be followed.
   3. High effort, low downtime - This process requires everything of (2), plus it tries to minimize the impact of query #11. We can do this by following step 2, and then starting v6 along with a running v5 server, and then monitor the application logs. As soon as the v6 application starts up, we need to bring down a v5 node. This minimizes the downtime to only a few seconds.
 - While trying to upgrade to a Mattermost version >= 6.0.x, you might encounter the following error: ``Failed to alter column type. It is likely you have invalid JSON values in the column. Please fix the values manually and run the migration again.`` This means that the particular column has some invalid JSON values which need to be fixed manually. A common fix that is known to work is to wipe out all \u0000 characters. Please follow these steps:
   1. Check the affected values by: ``SELECT COUNT(*) FROM <table> WHERE <column> LIKE '%\u0000%';``
   2. If you get a count more than 0, check those values manually, and confirm they are okay to be removed.
   3. Remove them by ``UPDATE <table> SET <column> = regexp_replace(<column>, '\\u0000', '', 'g') where <column> like '%\u0000%';``
   4. Then try to start Mattermost again.
 - Focalboard plugin has been renamed to Mattermost Boards, and v0.9.1 (released with Mattermost v6.0) is now enabled by default.
 - The advanced logging configuration schema changed. This is a breaking change relative to 5.x. See updated [documentation](/comply/audit-log.html).
 - Some breaking changes to plugins are included:
   - Support for left-hand side-specific bot icons was dropped.
   - Removed a deprecated "Backend" field from the plugin manifest.
   - Converted the "Executables" field in the plugin manifest to a map.
 -  [Collapsed Reply Threads](/messaging/organizing-conversations.html), available in beta, are known to have a negative impact on server performance. If you cannot easily scale up and tune your database, or if you are running the Mattermost application server and database server on the same machine, we recommended disabling [``ThreadAutoFollow``](/configure/configuration-settings.html#automatically-follow-threads) and [``CollapsedThreads``](/configure/configuration-settings.html#collapsed-reply-threads-beta) until Collapsed Reply Threads is promoted to general availability in Q2 2022. Learn more about these [performance considerations here](https://support.mattermost.com/hc/en-us/articles/4413183568276).

**IMPORTANT:** If you upgrade from a release earlier than v5.39, please read the other [Important Upgrade Notes](/upgrade/important-upgrade-notes.html).

### Highlights

#### Multi-Product Platform
 - Mattermost now ships as one platform with three products - Channels, Playbooks, and Boards.
 - Playbooks and Boards are visible when [plugins are enabled system-wide](/configure/configuration-settings.html#enable-plugins). 

#### Global Product Launcher
 - Added a global header for product navigation for Channels, Playbooks, and Boards. This is disabled on the mobile web view and mobile apps.

#### Branding Changes
 - Added a new default brand theme named "Denim".
 - The existing theme names and colors, including "Mattermost", "Organization", "Mattermost Dark", and "Windows Dark" have been updated to the new "Denim", "Sapphire", "Quartz", "Indigo", and "Onyx" theme names and colors, respectively. Anyone using the existing themes will see slightly modified theme colors after their server or workspace is upgraded. The theme variables for the existing "Mattermost", "Organization", "Mattermost Dark", and "Windows Dark" themes will still be accessible in [our documentation](/messaging/customizing-theme-colors.html#custom-theme-examples), so a custom theme can be created with these theme variables if desired. Custom themes are unaffected by this change.
 - Added a new light theme named "Quartz" to the default available list of themes.
 - Updated email templates to the new branding.

#### Packaging Changes
 - Updated in-product strings referencing E10 & E20 to [new packaging](https://mattermost.com/pricing).
 - Features moved from legacy E10 to all plans, including Team Edition:
   - System default permissions, e.g. permission to create and archive channels system-wide.
      - Specifically, “System Scheme” only in **System Console > User Management > Permissions**. 
      - Existing permissions/policies in TE/E0 for "Enable Team Creation" and "Allow Team Administrators to edit others’ posts" are properly handled. 
   - Team and Channel management pages (but without channel moderation, e.g. read-only channels).
 - Features moved from legacy E20 to Professional plan:
   - SSO with OpenID Connect, SAML, Google and O365
   - O365 integrations including MS Teams Calling and MS Calendar
   - Jira multi-server support
   - Advanced team permissions
   - Channel moderation
 - E20, Professional, and Enterprise license SKUs are now supported for installing Enterprise plugins.

#### Beta features Promoted to General Availability
   - Archived channels
   - Compliance exports
   - Custom terms of service
   - Guest accounts
   - System roles
   - Plugins

#### Permalink Previews
 - Added support for permalink previews for posts in Mattermost. Previews are generated to minimize context switching when sharing message links in Channels.

#### Tutorial Updates
 - Added a tip to the **Getting Started** page for downloading Desktop Apps.
 - Updated tutorial icons and changed text content in tutorial tips.
 - Updated the default treatment for the ``Add channel`` button to the current color and by team name.
 - Added a tutorial tip for new settings and status buttons.
 - Added a tip for the product switcher. This tip is skipped if not applicable.

### Improvements

#### User Interface (UI)
 - Added “Invite People” to the main "+" button below the hamburger menu.
 - The whole category bounds are now highlighted while holding a channel above a category name on the left-hand side.
 - Updated **Account Settings > Display > Timezone** to be more user friendly.
 - New theme agnostic file preview modal takes up the full screen. The file preview now has information about the user, channel, and the file, and moves away from text-based buttons to icon-based buttons.
 - Increased the limit of uploaded file attachments per post from 5 to 10.
 - Added desktop notifications for followed Threads.
 - Hungarian and English-Australian are now official languages.
 - Added a **Start Trial** call-to action to the **Main Menu**.
 - Changed H1-H3 heading font from Open Sans to Metropolis.

#### Performance
 - Improved typing performance when the emoji autocomplete is open.
 - Added performance improvements for draft storage with multiple tabs open.
 - Improved performance of draft loading.

#### Integrations
 - Pre-packaged Channel Export plugin v1.0.0.
 - Added a "rest field" to the App command parser.
 - Added support for React components in channel header tooltips registered by plugins.
 - Exported ``ChannelInviteModal`` and ``ChannelMembersModal`` components for plugins.

#### Administration
 - Added ``playbooks`` and ``boards`` to restricted team URLs list. Conflict exists if users hit the URL to the team directly without the trailing channel, permalink or threads information (ie server/team) and they have a team name “playbooks” or “boards”. User would expect to be taken to their messaging team.  
 - Added the ability for Team Edition to edit role permissions.
 - Removed a hard-coded override of ``TeamSettings.MaxNotificationsPerChannel`` on unlicensed servers (e.g. Team Edition).
 - Migrated the extraction command to mmctl.
 - Removed the convert channel endpoint to use ``/channels/{channel_id}/privacy`` instead.
 - Removed deprecated ``Posts.ParentId`` in favor of the semantically equivalent ``Posts.RootId``. Also removed ``CommandWebhook.ParentId`` and ``CompliancePost.ParentId`` for the same reason.
 - Added a field to each of the compliance export formats (CSV, Global Relay, and Actiance) to indicate that a post was viewable via the new permalink preview feature.
 - Removed the following deprecated CLI commands in favor of [mmctl](/manage/mmctl-command-line-tool.html):
   - channel
   - command
   - config
   - extract
   - group
   - integrity
   - ldap
   - license
   - logs
   - permissions
   - plugin
   - reset
   - roles
   - sampledata
   - team
   - user
   - webhook

### Bug Fixes
 - Fixed an issue where GitLab ``ButtonText`` and ``ButtonColor`` settings were not reflected on the login screen.
 - Fixed an issue with Collapsed Reply Threads (Beta) where replying to a Thread caused users to re-follow the previously unfollowed Thread.
 - Fixed an issue where floating timestamps appeared incorrectly on the right-hand side with Collapsed Reply Threads (Beta) enabled.
 - Fixed an issue where pinned and saved posts were no longer highlighted.
 - Disabled admin support email status check job on server startup.
 - Fixed an issue on joining a missing channel as a System Admin.
 - Fixed import process for imports with attachments.
 - Fixed an error with app locations and binding filtering.

### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:
 - Under ``ServiceSettings`` in ``config.json``:
    - Added ``EnableOnboardingFlow``, for enhanced user onboarding experience feature.
    - Added ``EnablePermalinkPreviews`` to enable permalink previews.
 - Under ``FileSettings`` in ``config.json``:
    - Added ``MaxImageResolution`` config setting to control the maximum dimension (in pixels) of image uploads.
 - Removed all of the following configs:
   - ``EnableOnlyAdminIntegrations``
   - ``RestrictCustomEmojiCreation``
   - ``RestrictPostDelete``
   - ``AllowEditPost``
   - ``ImageProxyType``
   - ``ImageProxyURL``
   - ``ImageProxyOptions``
   - ``UseExperimentalGossip``
   - ``EnableTeamCreation``
   - ``RestrictTeamInvite``
   - ``RestrictPublicChannelManagement``
   - ``RestrictPrivateChannelManagement``
   - ``RestrictPublicChannelCreation``
   - ``RestrictPrivateChannelCreation``
   - ``RestrictPublicChannelDeletion``
   - ``RestrictPrivateChannelDeletion``
   - ``RestrictPrivateChannelManageMembers``
   - ``DisableLegacyMFAEndpoint``
   - ``ExperimentalTownSquareIsReadOnly``
   - ``ExperimentalHideTownSquareinLHS``
   - ``EnableXToLeaveChannelsFromLHS``
   - ``CloseUnusedDirectMessages``
   - ``ExperimentalChannelOrganization``
   - ``ExperimentalChannelSidebarOrganization``
   - ``EnableLegacySidebar``
   - The legacy MFA endpoint
   - ``utils/authorization.go`` and moved any permissions to the ``MakeDefaultRoles()`` function.

### Database Changes
 - Added the following database indexes:
   - ``idx_posts_root_id_delete_at_create_at``
   - ``idx_channels_team_id_display_name``
   - ``idx_channels_team_id_type``
   - ``idx_threads_channel_id_last_reply_at``
   - ``idx_channelmembers_user_id_channel_id_last_viewed_at``
   - ``idx_channelmembers_channel_id_scheme_guest_user_id``
 - Removed the following redundant database indexes:
   - ``idx_posts_root_id``
   - ``idx_channels_team_id``
   - ``idx_threads_channel_id``
   - ``idx_channelmembers_user_id``
 - Updated all references of ``ToJson/FromJson`` methods to be in the form ``ToJSON/FromJSON``.
 - Increased ``Post.Props`` size limit to 800,000 characters.

### API Changes
 - Updated API to use ``per_page`` query parameter instead of ``pageSize``. This makes the threads API consistent with other endpoints, and automatically limits the number of requested threads with our param handling code. The ``pageSize`` query parameter will still be supported until version 6.0 of the server becomes the minimum version required by the mobile client.

### Websocket Event Changes
 - Added Websocket client to products.
 - Added plugin Websocket hooks: ``OnWebSocketConnect``, ``OnWebSocketDisconnect`` and ``WebSocketMessageHasBeenPosted``.

### Library Changes
 - Removed deprecated ``model.ComparePassword`` method.
 - Removed deprecated ``Context.SourcePluginId`` field.
 - Removed ``(*model.Client4).CheckUserMfa``.
 - Removed ``(*model.Client4).GetServerBusyExpires``.
 - Removed MB constant from model package.
 - Removed use of pointers to the following types: 
   - ``model.ChannelList``
   - ``model.ChannelListWithTeamData``
   - ``model.ChannelMembers``
   - ``model.Preferences``
   - ``model.ProductNotices``
 - Renamed ``plugin.Context.IpAddress`` to ``plugin.Context.IPAddress``.
 - Renamed fields in the model package to have more idiomatic names.

### Go Version
 - v6.0 is built with Go ``v1.16.7``.

### Open Source Components
 - Added ``@mattermost/compass-components``, ``@mattermost/compass-icons``, ``styled-components`` and ``timezones.json``, and removed ``react-inlinesvg`` from https://github.com/mattermost/mattermost-webapp.
 - Added ``@types/redux-mock-store`` to https://github.com/mattermost/mattermost-mobile.

### Known Issues
 - [Collapsed Reply Threads](/messaging/organizing-conversations.html) is currently in beta. Before enabling the feature, please ensure you are well versed in the [known issues](/messaging/organizing-conversations.html#known-issues),  particularly relating to database resource requirements and server performance implications. If you cannot easily scale up your database size, or are running the Mattermost application server and database server on the same machine, we recommended waiting to enable Collapsed Reply Threads until it is [promoted to general availability in Q2 2022](https://mattermost.com/blog/collapsed-reply-threads-ga/). Learn more about these [performance considerations here](https://support.mattermost.com/hc/en-us/articles/4413183568276).
 - Webapp sometimes crashes when clicking an image from "Recent files" [MM-38239](https://mattermost.atlassian.net/browse/MM-38239).
 - Member type is missing from autocomplete [MM-38989](https://mattermost.atlassian.net/browse/MM-38989).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - Deep link opened on mobile shows incorrect text directing the opening to the Desktop app [MM-38913](https://mattermost.atlassian.net/browse/MM-38913).
 - Channel switcher is missing "(You)" indicator on your own Direct Message channel [MM-38798](https://mattermost.atlassian.net/browse/MM-38798).
 - ``Ctrl/Cmd+Shift+A`` shortcut does not open **Account Settings** [MM-38236](https://mattermost.atlassian.net/browse/MM-38236).
 - Indigo theme glitch may occur when returning from Playbooks [MM-38910](https://mattermost.atlassian.net/browse/MM-38910).
 - **System Console > Channels > Channel Management** has an option to toggle group management in Team Edition, Starter, and Professional [MM-39216](https://mattermost.atlassian.net/browse/MM-39216).
 - Experimental timezones and custom statuses can cause an increase in CPU usage and database connections for servers with an E20 license. A current workaround is to disable custom statuses or to disable experimental timezones.
 - Adding an at-mention at the start of a post draft and pressing the leftwards or rightwards arrow can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.

### Contributors
 - [Adovenmuehle](https://github.com/Adovenmuehle), [aeomin](https://github.com/aeomin), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [alieh-rymasheuski](https://github.com/alieh-rymasheuski), [amyblais](https://github.com/amyblais), [amynicol1985](https://github.com/amynicol1985), [angeloskyratzakos](https://github.com/angeloskyratzakos), [arpit1912](https://github.com/arpit1912), [asaadmahmood](https://github.com/asaadmahmood), [ashishbhate](https://github.com/ashishbhate), [AshishDhama](https://github.com/AshishDhama), [ashutoshpw](https://github.com/ashutoshpw), [BenCookie95](https://github.com/BenCookie95), [BenLloydPearson](https://github.com/BenLloydPearson), [BoFFire](https://github.com/BoFFire), [calebroseland](https://github.com/calebroseland), [chenilim](https://github.com/chenilim), [chikei](https://github.com/chikei), [cjmartian](https://github.com/cjmartian), [coltoneshaw](https://github.com/coltoneshaw), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [CuriousCorrelation](https://github.com/CuriousCorrelation), [cwarnermm](https://github.com/cwarnermm), [danielsischy](https://github.com/danielsischy), [darkLord19](https://github.com/darkLord19), [deanwhillier](https://github.com/deanwhillier), [devinbinnie](https://github.com/devinbinnie), [dihmuzikien](https://github.com/dihmuzikien), [Duaard](https://github.com/Duaard), [emilyacook](https://github.com/emilyacook), [enahum](https://github.com/enahum), [enelson720](https://github.com/enelson720), [esethna](https://github.com/esethna), [flynbit](https://github.com/flynbit), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gigawhitlocks](https://github.com/gigawhitlocks), [gruceqq](https://translate.mattermost.com/user/gruceqq/), [haardikdharma10](https://github.com/haardikdharma10), [hahmadia](https://github.com/hahmadia), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hectorskypl](https://github.com/hectorskypl), [himanshu007-creator](https://github.com/himanshu007-creator), [hmhealey](https://github.com/hmhealey), [ialorro](https://github.com/ialorro), [icelander](https://github.com/icelander), [iomodo](https://github.com/iomodo), [isacikgoz](https://github.com/isacikgoz), [it33](https://github.com/it33), [itao](https://github.com/itao), [ivernus](https://github.com/ivernus), [jasonblais](https://github.com/jasonblais), [jayaddison-collabora](https://github.com/jayaddison-collabora), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [johnsonbrothers](https://github.com/johnsonbrothers), [josephbaylon](https://github.com/josephbaylon), [JtheBAB](https://github.com/JtheBAB), [jtwillis92](https://github.com/jtwillis92), [justinegeffen](https://github.com/justinegeffen), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kamre](https://github.com/kamre), [kayazeren](https://github.com/kayazeren), [KobeBergmans](https://github.com/KobeBergmans), [koox00](https://github.com/koox00), [krmh04](https://github.com/krmh04), [krutarththakkar](https://github.com/krutarththakkar), [larkox](https://github.com/larkox), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [maisnamrajusingh](https://github.com/maisnamrajusingh), [majidsajadi](https://github.com/majidsajadi), [marianunez](https://github.com/marianunez), [matthewbirtch](https://github.com/matthewbirtch), [matthew.williams](https://translate.mattermost.com/user/matthew-w/), [metanerd](https://github.com/metanerd), [mgdelacroix](https://github.com/mgdelacroix), [michaelgamble](https://github.com/michaelgamble), [michelengelen](https://github.com/michelengelen), [mickmister](https://github.com/mickmister), [migbot](https://github.com/migbot), [mikhailrimashevski](https://github.com/mikhailrimashevski), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [Mshahidtaj](https://github.com/Mshahidtaj), [neallred](https://github.com/neallred), [neflyte](https://github.com/neflyte), [nevyangelova](https://github.com/nevyangelova), [nickmisasi](https://github.com/nickmisasi), [nikolaizah](https://github.com/nikolaizah), [pablovelezvidal](https://github.com/pablovelezvidal), [petrmifek](https://github.com/petrmifek), [poflankov](https://github.com/poflankov), [puerco](https://github.com/puerco), [rbradleyhaas](https://github.com/rbradleyhaas), [Rina-dsg](https://github.com/Rina-dsg), [rodcorsi](https://github.com/rodcorsi), [Rutam21](https://github.com/Rutam21), [sadohert](https://github.com/sadohert), [sakaitsu](https://translate.mattermost.com/user/sakaitsu/), [saturninoabril](https://github.com/saturninoabril), [Sayanta66](https://github.com/Sayanta66), [sbishel](https://github.com/sbishel), [shazm](https://github.com/shazm), [sibasankarnayak](https://github.com/sibasankarnayak), [spirosoik](https://github.com/spirosoik), [sshiv5768](https://github.com/sshiv5768), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [svelle](https://github.com/svelle), [Szymongib](https://github.com/Szymongib), [thePanz](https://github.com/thePanz), [tsabi](https://translate.mattermost.com/user/tsabi/), [vadimasadchi](https://github.com/vadimasadchi), [vinod-demansol](https://github.com/vinod-demansol), [Westacular](https://github.com/Westacular), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [yedamao](https://github.com/yedamao), [Zeezee1210](https://github.com/Zeezee1210), [zefhemel](https://github.com/zefhemel)
