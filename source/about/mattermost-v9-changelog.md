# v9 Changelog


```{Important}
```{include} common-esr-support-upgrade.md
```


(release-v9-11-extended-support-release)=
## Release v9.11 - [Extended Support Release](https://docs.mattermost.com/about/release-policy.html#release-types)

- **9.11.16, released 2025-05-21**
  - Mattermost v9.11.16 contains medium to critical severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.11.16 contains no database or functional changes.
- **9.11.15, released 2025-05-09**
  - Mattermost v9.11.15 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Brought back the bug fix for [MM-61361](https://mattermost.atlassian.net/browse/MM-61361), since the performance regression has been fixed by tweaking the offending SQL query.
  - Mattermost v9.11.15 contains the following database changes:
    - A new index was added to the ``CategoryId`` column in ``SidebarChannels`` table to improve query performance. No database downtime is expected for this upgrade. It takes around 2s to add the index on a table with 1.2M rows for PostgreSQL, and it takes around 5s on MySQL on a table with 300K rows. The migrations are fully backwards-compatible and no table locks or existing operations on the table are impacted by this upgrade. Zero downtime is expected when upgrading to this release. The SQL queries included are ``CREATE INDEX idx_sidebarchannels_categoryid ON SidebarChannels(CategoryId);`` for MYSQL and ``CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_sidebarchannels_categoryid ON sidebarchannels(categoryid);`` for PostgreSQL.
- **9.11.14, released 2025-05-05**
  - Mattermost v9.11.14 contains a medium severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Reverted a bug fix for [MM-61361](https://mattermost.atlassian.net/browse/MM-61361) that likely introduced a performance regression.
  - Mattermost v9.11.14 contains no database or functional changes.
- **9.11.13, released 2025-04-29**
  - Mattermost v9.11.13 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.11.13 contains no database or functional changes.
- **9.11.12, released 2025-04-15**
  - Mattermost v9.11.12 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Stopped logging websocket PING events received by the server [MM-63693](https://mattermost.atlassian.net/browse/MM-63693).
  - Mattermost v9.11.12 contains no database or functional changes.
- **9.11.11, released 2025-03-24**
  - Mattermost v9.11.11 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Playbooks plugin [v1.41.0](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v1.41.0).
  - Mattermost v9.11.11 contains no database or functional changes.
- **9.11.10, released 2025-03-17**
  - Mattermost v9.11.10 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed errors logged by performance telemetry due to certain browser extensions [MM-62371](https://mattermost.atlassian.net/browse/MM-62371).
  - Pre-packaged Calls plugin version [v0.29.8](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.29.8).
  - Mattermost v9.11.10 contains no database or functional changes.
- **9.11.9, released 2025-02-19**
  - Mattermost v9.11.9 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Boards plugin [v9.1.1](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.1.1).
  - Fixed an issue in Compliance Exports whereby a missing file attachment in S3 could prevent the export run from completing [MM-62527](https://mattermost.atlassian.net/browse/MM-62527).
  - Mattermost v9.11.9 contains no database or functional changes.
- **9.11.8, released 2025-01-22**
  - Mattermost v9.11.8 contains critical severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Boards plugin [v9.0.5](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.0.5).
  - Pre-packaged Channel Export plugin [v1.2.1](https://github.com/mattermost/mattermost-plugin-channel-export/releases/tag/v1.2.1).
  - Pre-packaged Calls plugin [v0.29.7](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.29.7).
  - Fixed a panic during LDAP synchronization [MM-61239](https://mattermost.atlassian.net/browse/MM-61239).
  - Fixed an issue where the bulk export retention job would accidentally delete non-bulk export files and directories [MM-60888](https://mattermost.atlassian.net/browse/MM-60888).
  - Fixed an issue where new messages from new channels wouldn't appear in the sidebar after reconnecting the websocket [MM-61361](https://mattermost.atlassian.net/browse/MM-61361).
  - Mattermost v9.11.8 contains no database or functional changes.
- **9.11.7, released 2025-01-15**
  - Mattermost v9.11.7 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue with the web app status not being updated correctly for the current user [MM-59952](https://mattermost.atlassian.net/browse/MM-59952).
  - Pre-packaged Boards plugin [v9.0.2](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.0.2).
  - Fixed an issue with insertion errors to ``LinkMetadata`` table.
  - Fixed an issue where the scroll position reset when custom emojis were requested [MM-62102](https://mattermost.atlassian.net/browse/MM-62102).
  - Mattermost v9.11.7 contains the following database changes:
    - Fixed an issue where Direct and Group Messages with a ``DeleteAt`` flag in the database could cause issues with some APIs.
- **9.11.6, released 2024-12-10**
  - Mattermost v9.11.6 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - A 200 response is now returned for HEAD requests to a sub-path rather than responding with a 302. This fixes mobile devices trying to connect to a server hosted on a sub-path [MM-58042](https://mattermost.atlassian.net/browse/MM-58042).
  - Pre-packaged Calls plugin [v0.29.6](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.29.6).
  - Fixed an issue with incorrect reporting in the **Server Updates** section in **System Console > Workspace Optimizations** [MM-62030](https://mattermost.atlassian.net/browse/MM-62030).
  - Mattermost v9.11.6 contains no database or functional changes.
- **9.11.5, released 2024-11-14**
  - Mattermost v9.11.5 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Calls plugin [v0.29.4](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.29.4).
  - Mattermost v9.11.5 contains no database or functional changes.
- **9.11.4, released 2024-10-28**
  - Mattermost v9.11.4 contains a high severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where users would not see channels they were added to/messages from those channels in clustered environments [MM-59911](https://mattermost.atlassian.net/browse/MM-59911).
  - Mattermost v9.11.4 contains no database or functional changes.
- **9.11.3, released 2024-10-10**
  - Mattermost v9.11.3 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue with YouTube previews no longer being displayed [MM-60351](https://mattermost.atlassian.net/browse/MM-60351).
  - Improved the performance of LDAP sync jobs when group-contained teams and channels are used [MM-60253](https://mattermost.atlassian.net/browse/MM-60253).
  - Mattermost v9.11.3 contains no database or functional changes.
- **9.11.2, released 2024-09-26**
  - Mattermost v9.11.2 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Added Mattermost user survey plugin to pre-packaged plugins, [v1.1.1](https://github.com/mattermost/mattermost-plugin-user-survey/releases).
  - Pre-packaged Calls plugin [v0.29.2](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.29.2).
  - Pre-packaged Playbooks plugin [v1.40.0](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v1.40.0).
  - Fixed an issue where the **Edit Post Time Limit** button was not being displayed in the System Console ([MM-58529](https://mattermost.atlassian.net/browse/MM-58529), [MM-58824](https://mattermost.atlassian.net/browse/MM-58824)).
  - Fixed racy use of session in ``NewWebConn`` [MM-60307](https://mattermost.atlassian.net/browse/MM-60307).
  - Mattermost v9.11.2 contains the following functional change:
      - Added a configuration setting **NativeAppSettings > MobileExternalBrowser** that tells the Mobile app to perform SSO Authentication using the external default browser [MM-60332](https://mattermost.atlassian.net/browse/MM-60332).
- **9.11.1, released 2024-08-27**
  - Mattermost v9.11.1 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.11.1 contains no database or functional changes.
- **9.11.0, released 2024-08-16**
  - Original 9.11.0 release.

### Important Upgrade Notes

 - Added support for Elasticsearch v8. Also added Beta support for [OpenSearch v1.x and v2.x](https://opensearch.org/). A new config setting ``ElasticsearchSettings.Backend`` has been added to differentiate between Elasticsearch and OpenSearch. The default value is `elasticsearch`, which breaks support for AWS Elasticsearch v7.10.x since the official v8 client only works from Elasticsearch v7.11 and higher versions. See the important note below for details.
 - Mattermost supports Elasticsearch v7.17+. However, we recommend upgrading your Elasticsearch v7 instance to v8.x. See the [Elasticsearch upgrade](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html) documentation for details.
 - When using Elasticsearch v8, ensure you set ``action.destructive_requires_name`` to ``false`` in ``elasticsearch.yml`` to allow for wildcard operations to work.

```{Important}
**AWS Elasticsearch**

If you're using AWS Elasticsearch, you must:
1. Upgrade to AWS OpenSearch. Refer to the [OpenSearch upgrade](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/version-migration.html) documentation for details.
2. Disable "compatibility mode" in OpenSearch.
3. Upgrade Mattermost server.
4. Update the Mattermost `ElasticsearchSettings.Backend` configuration setting value from `elasticsearch` to `opensearch` manually or using [mmctl](https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-config-set). This value cannot be changed using the System Console. See the Mattermost [Elasticsearch backend type](https://docs.mattermost.com/configure/environment-configuration-settings.html#elastic-backendtype) documentation for additional details.
5. Restart the Mattermost server.
```

### Compatibility
 - Updated minimum Edge and Chrome versions to 126+.
 - Added Ubuntu Noble support.

```{Important}
If you upgrade from a release earlier than v9.5, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Improvements

See [this walkthrough video](https://mattermost.com/video/mattermost-v9-11-changelog/) on some of the improvements in our latest release below.

#### User Interface (UI)
 - Pre-packaged Calls version [v0.29.1](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.29.1).
 - Pre-packaged GitHub plugin version [v2.3.0](https://github.com/mattermost/mattermost-plugin-github/releases/tag/v2.3.0).
 - Added user interface improvements to the keyboard shortcuts modal.
 - Added a message "Editing this message with an ``@mention`` will not notify the recipient" in the post edit dialog.
 - Made the appearance of several tooltips more consistent.
 - Updated the help text in the **Direct Messages** modal.
 - Emojis are now placed at cursor position while editing messages.
 - Made keyboard shortcuts modal content DIV-accessible via the keyboard.
 - Added Channel Bookmarks user interface (disabled by default and behind a feature flag).

#### Administration
 - Added a new feature where an admin with user management permission can now edit a user's settings in **System Console > Users**. 
 - Added download functionality for admins to download server logs from **Server Logs** page in the **System Console**.
 - LDAP vendor errors are now included in the Support Packet.
 - Added [metadata](https://docs.mattermost.com/manage/admin/generating-support-packet.html#contents-of-a-support-packet) to the Support Packet.
 - We are now adding the user's ID and session ID to the audit log's Actor field for the login event, to match what we provide for the logout event.
 - Added support for custom status in bulk export/import.
 - Marked the ``RemoteTeamId`` field of the ``RemoteCluster`` entity as deprecated.
 - Added log ``Name`` and ``DisplayName`` of groups.
 - Logged fields of users are now updated.

#### Performance
 - Added platform related information to the notification metrics.
 - Added additional information to INP and LCP client metrics.
 - Added minor performance improvements to webapp initialization.

#### mmctl
 - Added two new commands to mmctl, ``mmctl job list`` and ``mmctl job update``.
 - Panic message is now printed when mmctl panics.
 - Setting ``AdvancedLoggingJSON`` via mmctl is now supported.

### Bug Fixes
 - Fixed an issue that displayed a wrong count for custom group members on the notification warning.
 - Fixed a panic when the password was too long.
 - Fixed an issue where configuration patches through mmctl did not correctly merge plugin configuration values.
 - Fixed issues with the OpenID local development.
 - Fixed an issue where Latex was not rendered in a code block as code when Latex rendering was disabled.
 - Fixed an issue with saving custom roles.
 - Fixed an issue with the left-hand side scrollbar auto-hide functionality for Chrome and Safari.
 - Fixed Group Message to private channel conversion edge cases.
 - Fixed an issue where users with the user management permission were unable to view the list of users in the **System Console > Users** page.
 - Fixed more web app performance reports being marked as outdated after a user's computer woke up from sleep.

### config.json
New setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
 - Under ``ServiceSettings`` in ``config.json``:
    - Added ``TerminateSessionsOnPasswordChange`` to configure the sessions revocation during password resets.

#### Changes to the Enterprise plan:
 - Under ``ElasticsearchSettings`` in ``config.json``:
    - Added ``Backend`` to differentiate between Elasticsearch and OpenSearch. The default value is ``elasticsearch``.

### API Changes
 - Added new API endpoints to manage remote clusters.
 - Added two new query parameters to ``GET /api/v4/jobs, job_type`` and status.
 - Added a new endpoint ``PATCH /api/v4/jobs/{job_id}/status``.
 - Updated ``AddChannelMember`` to accept a list of userIds.
 - Added six new permissions to manage the status of particular jobs:
     - ``PermissionManagePostBleveIndexesJob``
     - ``PermissionManageDataRetentionJob``
     - ``PermissionManageComplianceExportJob``
     - ``PermissionManageElasticsearchPostIndexingJob``
     - ``PermissionManageElasticsearchPostAggregationJob``
     - ``PermissionManageLdapSyncJob``

### Go Version
 - v9.11 is built with Go ``v1.21.8``.

### Open Source Components
 - Removed ``stylelint``, and added ``elastic/go-elasticsearch`` to https://github.com/mattermost/mattermost/.

### Known Issues
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.

### Contributors
 - [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [amyblais](https://github.com/amyblais), [andreabia](https://translate.mattermost.com/user/andreabia), [andrleite](https://github.com/andrleite), [angeloskyratzakos](https://github.com/angeloskyratzakos), [Aryakoste](https://github.com/Aryakoste), [asaadmahmood](https://github.com/asaadmahmood), [AshishDhama](https://github.com/AshishDhama), [ayusht2810](https://github.com/ayusht2810), [bbodenmiller](https://github.com/bbodenmiller), [BenCookie95](https://github.com/BenCookie95), [BrandonS09](https://github.com/BrandonS09), [calebroseland](https://github.com/calebroseland), [Camillarhi](https://github.com/Camillarhi), [catalintomai](https://github.com/catalintomai), [Celeo](https://github.com/Celeo), [chessmadridista](https://github.com/chessmadridista), [ckaznable](https://github.com/ckaznable), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [danielsischy](https://github.com/danielsischy), [devinbinnie](https://github.com/devinbinnie), [Eleferen](https://translate.mattermost.com/user/Eleferen), [enahum](https://github.com/enahum), [enzowritescode](https://github.com/enzowritescode), [ewwollesen](https://github.com/ewwollesen), [fmartingr](https://github.com/fmartingr), [frankps](https://translate.mattermost.com/user/frankps), [gabrieljackson](https://github.com/gabrieljackson), [Gesare5](https://github.com/Gesare5), [grinapo](https://github.com/grinapo), [hanzei](https://github.com/hanzei), [harmeet01singh](https://github.com/harmeet01singh), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [ifoukarakis](https://github.com/ifoukarakis), [imanmagomedov.said](https://translate.mattermost.com/user/imanmagomedov.said), [isacikgoz](https://github.com/isacikgoz), [jespino](https://github.com/jespino), [jprusch](https://github.com/jprusch), [JulienTant](https://github.com/JulienTant), [jwilander](https://github.com/jwilander), [kaakaa](https://translate.mattermost.com/user/kaakaa), [kalil0321](https://github.com/kalil0321), [KellieSue](https://github.com/KellieSue), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo), [marianunez](https://github.com/marianunez), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthewbirtch](https://github.com/matthewbirtch), [matthew-w](https://translate.mattermost.com/user/matthew-w), [MeHow25](https://github.com/MeHow25), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [milotype](https://translate.mattermost.com/user/milotype), [Mohamed-sobhi95](https://translate.mattermost.com/user/Mohamed-sobhi95), [mvitale1989](https://github.com/mvitale1989), [natalie-hub](https://github.com/natalie-hub), [nickmisasi](https://github.com/nickmisasi), [ningthoujamSwamikumar](https://github.com/ningthoujamSwamikumar), [Pawel1894](https://github.com/Pawel1894), [phoinixgrr](https://github.com/phoinixgrr), [poppfredslund](https://translate.mattermost.com/user/poppfredslund), [pvev](https://github.com/pvev), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [rahimrahman](https://github.com/rahimrahman), [Rajat-Dabade](https://github.com/Rajat-Dabade), [recontech404](https://github.com/recontech404), [rOt779kVceSgL](https://translate.mattermost.com/user/rOt779kVceSgL), [sadohert](https://github.com/sadohert), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [shaon72](https://github.com/shaon72), [Sharuru](https://translate.mattermost.com/user/Sharuru), [shieldsjared](https://github.com/shieldsjared), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [suraj-anthwal](https://github.com/suraj-anthwal), [svelle](https://github.com/svelle), [ThrRip](https://translate.mattermost.com/user/ThrRip), [tnir](https://github.com/tnir), [toninis](https://github.com/toninis), [varghesejose2020](https://github.com/varghesejose2020), [vhaska](https://translate.mattermost.com/user/vhaska), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yomiadetutu1](https://github.com/yomiadetutu1), [ythosa](https://github.com/ythosa), [zenocode-org](https://translate.mattermost.com/user/zenocode-org), [ZubairImtiaz3](https://github.com/ZubairImtiaz3)

(release-v9-10-feature-release)=
## Release v9.10 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

- **9.10.3, released 2024-09-26**
  - Mattermost v9.10.3 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Playbooks plugin [v1.40.0](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v1.40.0).
  - Mattermost v9.10.3 contains no database or functional changes.
- **9.10.2, released 2024-08-27**
  - Mattermost v9.10.2 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.10.2 contains no database or functional changes.
- **9.10.1, released 2024-07-22**
  - Mattermost v9.10.1 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Mattermost Copilot plugin version [v0.8.3](https://github.com/mattermost/mattermost-plugin-ai/releases/tag/v0.8.3).
  - Ensured that the web app only requests notification permissions when needed. Fixed an issue with desktop notifications not being sent on Safari [MM-59416](https://mattermost.atlassian.net/browse/MM-59416).
  - Fixed an issue where the app crashed on iOS Safari [MM-59296](https://mattermost.atlassian.net/browse/MM-59296).
  - Mattermost v9.10.1 contains no database or functional changes.
- **9.10.0, released 2024-07-16**
  - Original 9.10.0 release.

```{Important}
If you upgrade from a release earlier than v9.5, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Improvements

See [this walkthrough video](https://mattermost.com/video/mattermost-v9-10-changelog/) on some of the improvements in our latest release below.

#### User Interface (UI)
 - Pre-packaged GitLab plugin version [v1.9.1](https://github.com/mattermost/mattermost-plugin-gitlab/releases/tag/v1.9.1).
 - Pre-packaged Mattermost Copilot plugin version [v0.8.1](https://github.com/mattermost/mattermost-plugin-ai/releases/tag/v0.8.1).
 - Pre-packaged Calls plugin version [v0.28.2](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.28.2).
 - Re-designed the user profile popover and improved its performance.
 - Added banner to prompt users to allow notification permissions when opening the app in web browsers.
 - Increased the width of the profile picture setting to match other user settings.
 - Improved screen reader support for the emoji picker.
 - Improved the accessibility of plugin buttons in the channel header.

#### Administration
 - Extended ``PluginSiteStatsHandler`` to support more advanced visualization types.
 - Stopped broadcasting ``channel_deleted/channel_restored`` messages from private channels to non-members.

#### Performance
 - Added page load time to client performance metrics.
 - Added a metric to track time it takes for the Threads view to load.
 - Added support for mobile client metrics.
 - Increased the range of LCP metrics that can be measured.
 - Added polling of ``getStatusesByIds`` and ``getProfilesByIds`` network calls. The interval of which is configurable with the ``UsersStatusAndProfileFetchingPollIntervalMilliseconds`` configuration variable.
 - Added defer loading plugins scripts.

### Bug Fixes
 - Fixed an issue where the ``RefreshPostStats`` job could fail.
 - Fixed an issue where attempting to create a team with the URL of an existing team showed the wrong error message.
 - Fixed an issue where ``visibilitychange`` JavaScript browser event had not been added for updating the user's current timezone.
 - Fixed an issue where the last admin in the system was allowed to be demoted.
 - Fixed an issue where banners set by system administrators did not stack below system banners, and appeared underneath them instead. Existing system banners have remained unchanged.
 - Fixed an issue with an incorrect wrapping of long words in numbered lists.
 - Fixed an incorrect behavior of the image proxy when site URL is changed.
 - Fixed an issue where cache invalidation messages for websocket connections were not being sent across the cluster, causing missed websocket events.
 - Fixed ``EnableClientMetrics`` setting not being available in the System Console.

### config.json
New setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
 - Under ``ExperimentalSettings`` in ``config.json``:
    - Added ``UsersStatusAndProfileFetchingPollIntervalMilliseconds`` to configure the interval of ``getStatusesByIds`` and ``getProfilesByIds`` network calls.

### API Changes
 - Added a new plugin API endpoint ``GetUsersByIds`` to retrieve a list of users by their ids.

### Go Version
 - v9.10 is built with Go ``v1.21.8``.

### Known Issues
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.

### Contributors
 - [abhijit-singh](https://github.com/abhijit-singh), [aeomin](https://translate.mattermost.com/user/aeomin), [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [ahmadJT](https://github.com/ahmadJT), [amyblais](https://github.com/amyblais), [andrleite](https://github.com/andrleite), [apshada](https://github.com/apshada), [Aryakoste](https://github.com/Aryakoste), [asaadmahmood](https://github.com/asaadmahmood), [AshishDhama](https://github.com/AshishDhama), [BenCookie95](https://github.com/BenCookie95), [BillAnderson304](https://github.com/BillAnderson304), [Boruus](https://translate.mattermost.com/user/Boruus), [BrandonS09](https://github.com/BrandonS09), [bruno-keiko](https://github.com/bruno-keiko), [calebroseland](https://github.com/calebroseland), [Camillarhi](https://github.com/Camillarhi), [catalintomai](https://github.com/catalintomai), [chessmadridista](https://github.com/chessmadridista), [ckaznable](https://github.com/ckaznable), [coltoneshaw](https://github.com/coltoneshaw), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [devinbinnie](https://github.com/devinbinnie), [DHaussermann](https://github.com/DHaussermann), [DSchalla](https://github.com/DSchalla), [Eleferen](https://translate.mattermost.com/user/Eleferen), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [enzowritescode](https://github.com/enzowritescode), [esarafianou](https://github.com/esarafianou), [EyeCantCU](https://github.com/EyeCantCU), [ezekielchow](https://github.com/ezekielchow), [fmartingr](https://github.com/fmartingr), [frankps](https://translate.mattermost.com/user/frankps), [gabrieljackson](https://github.com/gabrieljackson), [Gesare5](https://github.com/Gesare5), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [homerCOD](https://translate.mattermost.com/user/homerCOD), [ifoukarakis](https://github.com/ifoukarakis), [isacikgoz](https://github.com/isacikgoz), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [johnsonbrothers](https://github.com/johnsonbrothers), [jprusch](https://github.com/jprusch), [JtheBAB](https://github.com/JtheBAB), [JulienTant](https://github.com/JulienTant), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo), [marianunez](https://github.com/marianunez), [maruTA-bis5](https://translate.mattermost.com/user/maruTA-bis5), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [MattSilvaa](https://github.com/MattSilvaa), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [mojahani](https://translate.mattermost.com/user/mojahani), [mvitale1989](https://github.com/mvitale1989), [nbruneau71250](https://github.com/nbruneau71250), [nickmisasi](https://github.com/nickmisasi), [phoinixgrr](https://github.com/phoinixgrr), [pvev](https://github.com/pvev), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [Rajat-Dabade](https://github.com/Rajat-Dabade), [sadohert](https://github.com/sadohert), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [ThrRip](https://github.com/ThrRip), [tnir](https://github.com/tnir), [toninis](https://github.com/toninis), [varghesejose2020](https://github.com/varghesejose2020), [wiggin77](https://github.com/wiggin77), [willypuzzle](https://github.com/willypuzzle), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yomiadetutu1](https://github.com/yomiadetutu1), [zenocode-org](https://github.com/zenocode-org)

(release-v9-9-feature-release)=
## Release v9.9 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

- **9.9.3, released 2024-08-27**
  - Mattermost v9.9.3 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.9.3 contains no database or functional changes.
- **9.9.2, released 2024-07-22**
  - Mattermost v9.9.2 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.9.2 contains no database or functional changes.
- **9.9.1, released 2024-07-02**
  - Mattermost v9.9.1 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where banners set by system administrators did not stack below system banners, but rather appeared underneath them. Existing system banners have remained unchanged.
  - Removed feature flag which prevented enabling ``MetricsSettings.EnableClientMetrics`` [MM-58823](https://mattermost.atlassian.net/browse/MM-58823).
  - Added a page load time to the client performance metrics [MM-58359](https://mattermost.atlassian.net/browse/MM-58359).
  - Fixed web app performance reports being marked as outdated after the user's computer woke up from sleep [MM-58772](https://mattermost.atlassian.net/browse/MM-58772).
  - Increased range of LCP metrics and Load Event End metrics that can be measured [MM-59033](https://mattermost.atlassian.net/browse/MM-59033).
  - Fixed an error caused by performance telemetry when using Firefox with ``beacon.enabled`` set to ``false`` [MM-58777](https://mattermost.atlassian.net/browse/MM-58777).
  - Mattermost v9.9.1 contains no database or functional changes.
- **9.9.0, released 2024-06-14**
  - Original 9.9.0 release.

### Compatibility
 - Updated minimum macOS version to 12+ and minimum Safari version to 17+.

```{Important}
If you upgrade from a release earlier than v9.5, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Improvements

See [this walkthrough video](https://mattermost.com/video/video-mattermost-v9-9-changelog/) on some of the improvements in our latest release below.

#### User Interface (UI)
 - Pre-packaged Calls plugin version [v0.27.0](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.27.0).
 - Pre-packaged Jira plugin version [v4.1.1](https://github.com/mattermost/mattermost-plugin-jira/releases/tag/v4.1.1).
 - Pre-packaged GitLab plugin version [v1.9.0](https://github.com/mattermost/mattermost-plugin-gitlab/releases/tag/v1.9.0).
 - Pre-packaged Zoom plugin version [v1.8.0](https://github.com/mattermost/mattermost-plugin-zoom/releases/tag/v1.8.0).
 - Updated the default themes to reduce eye strain (particularly on the dark themes).
 - Added UI improvements to the core layout.
 - Improved error text when inviting guests to a team.
 - Increased the visibility Mattermost edition in-product when using the free edition.
 - Added an **Unsupported** label to the Team/E0 editions in the product menu.
 - Improved the look and feel of the **True/False** selector in the System Console.
 - Updated the channel header layout to reduce height and simplify the UI.

#### Administration
 - Removed safety limit error message in compiled Team Edition and unlicensed Enterprise Edition deployments when message count exceeds 5 million posts.
 - Adjusted safety limit error message to show when users exceed 5,000 in compiled Team Edition and Enterprise Edition deployments when enterprise scale and access control automation features are unavailable. ``ERROR_SAFE_LIMITS_EXCEEDED``.
 - Improved the message length validation step in the ``mmctl import validate`` command.
 - Added shell completion to ``mmctl user active`` and ``mmctl user deactivate``.
 - Removed support for self-serve purchases of Mattermost Subscriptions in various flows, throughout Cloud and Self Hosted environments.
 - Removed support for self-serve true up review submission in the **System Console**. 
 - Added streaming support to the file attachments import process.
 - Added LDAP job command to mmctl.
 - Made LDAP sync jobs more resilient against errors.
 - Removed the ``PostPriority`` feature flag.
 - Improved the error message of ``NotFound`` errors in store.
 - Added support for post priority to incoming webhooks and outgoing webhook responses.
 - Added a validation that the payload for an open Interactive Dialog request is valid according to the rules at https://developers.mattermost.com/integrate/plugins/interactive-dialogs/.
 - Unblocked notification calls by using usernames instead of full names in case of a missing user profile.
 - Increased the maximum password limit from 64 to 72 characters (``PasswordMaximumLength``).

#### Performance
 - Added the initial version of new client-side performance metrics to track web app performance and can be monitored in new [Grafana board](https://grafana.com/grafana/dashboards/21460-web-app-metrics/).
 - Added a metric to track time it takes for the right-hand side to load.
 - Improved js memory profile of status’s reducers.
 - When a user receives a new post that is part of a thread from a root post in a channel they are not currently viewing, we do not fetch the complete root post and its thread posts immediately. However, we still store the newly received post. The root post and its thread posts are only fetched when the user navigates to that specific channel.

### Bug Fixes
 - Fixed an issue with ``aria-label`` for sidebar channel buttons.
 - Fixed an issue where any remaining unclosed database RPC connections were not closed after a plugin shut down.
 - Fixed an issue where the right-hand side stole the focus when coming back from threads or drafts.
 - Fixed an issue where a proxy link was copied instead of the original image link when copying a post that included an embedded image.
 - Fixed an issue where the user status would incorrectly get stuck to online after the user closed the tab.
 - Fixed an issue where on some servers the user could not see the member count in the **Browse Channels** dialog.
 - Fixed an issue with inline display of WebP images accessed through the public-link feature.
 - Fixed an issue where it wasn’t clear that the ``mmctl import process --bypass-upload --local`` doesn't work if the server is in High Availability.
 - Fixed an issue where the user status would incorrectly be set to offline without checking for connections in other nodes in an High Availability cluster.
 - Fixed a longstanding issue where the @mention auto-complete could erase post text following the auto-completed @mention.
 - Fixed an issue with status management to avoid missing notifications.
 - Fixed an issue where audit events were not added for OAuth logins.
 - Fixed an issue with the error check in the message export process.
 - Fixed an issue where pasting in the post text box could not always paste without formatting.
 - Fixed some plugin settings with defaults not changing value.

### config.json
New setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
 - Under ``ExperimentalSettings`` in ``config.json``:
    - Added ``DisableWakeUpReconnectHandler`` to disable the wake up on reconnect handler.
 - Removed ``SelfHostedPurchase`` setting.

#### Changes to the Enterprise plan: 
 - Under ``MetricsSettings`` in ``config.json``:
    - Added a feature flag and a setting ``EnableClientMetrics`` to control new client performance metrics.
    - Added a setting for notification metrics ``EnableNotificationMetrics``.
 - Self-hosted system administrators can now configure all ``ExperimentalAuditSettings`` through the user interface in the ``System Console``. Cloud administrators can now change the ``AdvancedLoggingJSON`` value for the ``ExperimentalAuditSettings``. This is the only configuration that Cloud administrators are able to adjust. Feature flag ``ExperimentalAuditSettingsSystemConsoleUI`` must be enabled in order to leverage this new user interface.

### Websocket Event Changes
 - Changed the semantics of the ``mattermost_http_websockets_total`` metric to track all open WebSocket connections, regardless of whether they are authenticated.
 - Added a ``origin_client`` label to the ``mattermost_http_websockets_total`` Prometheus metric.

### Go Version
 - v9.9 is built with Go ``v1.21.8``.

### Open Source Components
 - Removed ``@stripe/react-stripe-js`` and ``@stripe/stripe-js``, and added ``web-vitals`` at https://github.com/mattermost/mattermost.

### Known Issues
 - Some Cloud workspaces unexpectedly received emails about license expiration.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.
 
### Contributors
 - [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [amyblais](https://github.com/amyblais), [andrleite](https://github.com/andrleite), [arush-vashishtha](https://github.com/arush-vashishtha), [asaadmahmood](https://github.com/asaadmahmood), [ayusht2810](https://github.com/ayusht2810), [azigler](https://github.com/azigler), [BenCookie95](https://github.com/BenCookie95), [bndn](https://translate.mattermost.com/user/bndn), [calebroseland](https://github.com/calebroseland), [coltoneshaw](https://github.com/coltoneshaw), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [devinbinnie](https://github.com/devinbinnie), [DHaussermann](https://github.com/DHaussermann), [Eleferen](https://translate.mattermost.com/user/Eleferen), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [enzowritescode](https://github.com/enzowritescode), [fasal26](https://github.com/fasal26), [fmartingr](https://github.com/fmartingr), [gabrieljackson](https://github.com/gabrieljackson), [grundleborg](https://github.com/grundleborg), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [ifoukarakis](https://github.com/ifoukarakis), [isacikgoz](https://github.com/isacikgoz), [jespino](https://github.com/jespino), [joakim.rivera](https://translate.mattermost.com/user/joakim.rivera), [johnsonbrothers](https://github.com/johnsonbrothers), [jprusch](https://github.com/jprusch), [JulienTant](https://github.com/JulienTant), [kaakaa](https://github.com/kaakaa), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo), [marianunez](https://github.com/marianunez), [marlenekoh](https://github.com/marlenekoh), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [MeHow25](https://github.com/MeHow25), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [mojahani](https://translate.mattermost.com/user/mojahani), [morgancz](https://github.com/morgancz), [mvitale1989](https://github.com/mvitale1989), [nickmisasi](https://github.com/nickmisasi), [nixusUM](https://github.com/nixusUM), [orimaimon](https://github.com/orimaimon), [phoinixgrr](https://github.com/phoinixgrr), [piotr-lasota](https://github.com/piotr-lasota), [pjenicot](https://translate.mattermost.com/user/pjenicot), [pmokeev](https://github.com/pmokeev), [rOt779kVceSgL](https://translate.mattermost.com/user/rOt779kVceSgL), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [svelle](https://github.com/svelle), [tarrow](https://github.com/tarrow), [ThrRip](https://github.com/ThrRip), [tnir](https://github.com/tnir), [toninis](https://github.com/toninis), [umrkhn](https://github.com/umrkhn), [varghesejose2020](https://github.com/varghesejose2020), [vish9812](https://github.com/vish9812), [wiggin77](https://github.com/wiggin77), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yomiadetutu1](https://github.com/yomiadetutu1), [zsrv](https://github.com/zsrv)

(release-v9-8-feature-release)=
## Release v9.8 - Feature Release

- **9.8.3, released 2024-07-22**
  - Mattermost v9.8.3 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.8.3 contains no database or functional changes.
- **9.8.2, released 2024-07-02**
  - Mattermost v9.8.2 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where banners set by system administrators did not stack below system banners, but rather appeared underneath them. Existing system banners have remained unchanged.
  - Mattermost v9.8.2 contains no database or functional changes.
- **9.8.1, released 2024-06-03**
  - Mattermost v9.8.1 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Removed a safety limit error message in compiled Team Edition and unlicensed Enterprise Edition deployments when message count exceeds 5 million posts.
  - Fixed an issue with some plugin settings with defaults not changing value.
  - Mattermost v9.8.1 contains no database or functional changes.
- **9.8.0, released 2024-05-16**
  - Original 9.8.0 release.

### Compatibility
 - Updated minimum required Edge and Chrome versions to 122+.

```{Important}
If you upgrade from a release earlier than v9.7, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Improvements

See [this walkthrough video](https://mattermost.com/video/mattermost-v9-8-changelog/) on some of the improvements in our latest release below.

#### User Interface (UI)
 - Pre-packaged Playbooks version [v1.39.3](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v1.39.3).
 - Pre-packaged GitLab plugin version [v1.8.1](https://github.com/mattermost/mattermost-plugin-gitlab/releases/tag/v1.8.1).
 - Pre-packaged Calls version [v0.26.2](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.26.2).
 - Combined Desktop and Mobile notifications in the user settings modal.
 - Added a **Don't Clear** option for Do Not Disturb.
 - Enhanced the user interface for channel introductions.
 - Added an ephemeral message for non-team member mentions in channels.
 - Added emoji tooltips on hover in post message.
 - Made the appearance of several tooltips more consistent.
 - Updated theme colors for onboarding tour points.
 - Updated the right-hand side Thread view to use relative timestamps to be more consistent with the global Threads view.
 - Added a total reply count to the right-hand side thread view.

#### Administration
 - Added safety limit error message in compiled Team Edition and Enterprise Edition deployments when enterprise scale and access control automation features are unavailable, and message count exceeds 5 million posts. ERROR_SAFE_LIMITS_EXCEEDED.
 - Downloading a support packet is now extensible with plugins. If a plugin can add content to the support packet, it will be displayed in the commercial support modal. Administrators will have the option to include/exclude that from the support package.
 - Upgraded Nodejs to v20.11.
 - Added the backend for Channel Bookmarks (disabled by default). Added Channel Bookmarks permissions to the channel user role and to the channel moderation system.
 - Added Channel Bookmarks permissions to the channel user role and to the channel moderation system.
 - Added progress logs for attachments in bulk exports.
 - Added a **System Console** option to rebuild Elasticsearch channels indexes.
 - Obfuscated ``ReplicaLagSettings`` in the Support Packet.
 - Improved license loading errors.
 - Updated the keycloak docker configs and added a ``make`` command.
 - Removed unused ``IsOAuth`` field from ``AppError``.
 - ``bool`` is now used for ``license_is_trial`` in the Support Packet.
 - Bulk export: added functionality to export roles and permissions schemes.
 - A new flag (``extract-content``) was added to the mmctl import process that allows the server to skip content extraction during the import phase.

### API Changes
 - Added a create channel bookmark endpoint at ``/api/v4/channels/{channel_id}/bookmarks``.
 - Added additional query params to channel endpoints to include channel bookmarks.
 - Added update channel bookmark endpoint at ``/api/v4/channels/{channel_id}/bookmarks/{bookmark_id}``.
 - Added list channel bookmarks endpoint at ``/api/v4/channels/{channel_id}/bookmarks``.
 - Added delete channel bookmark endpoint at ``/api/v4/channels/{channel_id}/bookmarks/{bookmark_id}``.
 - Added update channel bookmark sort order endpoint at ``/api/v4/channels/{channel_id}/bookmarks/{bookmark_id}/sort_order``.
 - Exposed a local-mode only API for reattaching plugins, primarily to facilitate mock-free unit testing.
 - Exposed ``UpdateUserRoles`` in ``pluginapi``.
 - Exposed ``pluginapi.ProfileImageBytes`` to simplify bot setup from a plugin.
 - For ``POST /channels``, added a validation for ``display_name`` to not pass validation if the display name is empty.

### Bug Fixes
 - Fixed an issue with context cancellation for integration requests.
 - Fixed an issue preventing the retrieval of SAML metadata.
 - Fixed an issue causing an empty channel switcher after converting a group message to a private channel.
 - Fixed an issue where System Admins were not allowed to LDAP sync SAML users when ``SamlSettings.EnableSyncWithLdap`` was set to **true**.
 - Fixed an issue with markdown in the AD job status table.
 - Fixed an issue with a control character in the group list modal.
 - Fixed an issue where the auto-complete channels API returned archived channels in response.
 - Fixed a crash issue in the **System Console**.
 - Fixed an issue where links included in notifications were truncated and not clickable.
 - Fixed using local requests instead of HTTP requests in the flow library.
 - Fixed an issue where ``support_packet.yaml`` wasn’t generated even if an error occurred.
 - Fixed an issue where outgoing webhooks did not trigger when using multiple callback URLs.
 - Fixed an issue where it was not possible to clear plugin settings with a default value in the **System Console**.
 - Fixed an issue where ``MaxUsersForStatistics`` wasn’t ignored when generating a Support Packet.
 - Fixed an issue where the ``EnsureBot`` function did not recreate the bot if it had been manually deleted.
 - Fixed an issue where users couldn't look up a user by their ID in the **System Console** anymore.
 - Fixed an accessibility issue where the focus didn’t go back to the originating button when a modal was closed.
 - Fixed an issue where end users were not allowed to fetch the group members list of groups that allow ``@-mentions``.

### config.json
New setting option were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
 - Under ``FileSettings`` in ``config.json``:
   - Added ``AmazonS3UploadPartSizeBytes`` and ``ExportAmazonS3UploadPartSizeBytes`` to control the part size used to upload files to an S3 store.
 - Under ``ServiceSettings`` in ``config.json``:
   - Increased the default payload size limit (``MaximumPayloadSizeBytes``) from 100 kB to 300 kB. Existing servers need to manually update this value.
 - Under ``ClusterSettings`` in ``config.json``:
   - Removed unused settings ``StreamingPort``, ``MaxIdleConns``, ``MaxIdleConnsPerHost`` and ``IdleConnTimeoutMilliseconds``.

 #### Changes to Professional and Enterprise plans:
 - Under ``ExperimentalSettings`` in ``config.json``:
   - Removed the ``UseNewSAMLLibrary`` experimental setting.

### Go Version
 - v9.8 is built with Go ``v1.21.8``.

### Known Issues
 - Status may sometimes get stuck as **Away** or **Offline** with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.
 
### Contributors
 - [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [Amir-Helali](https://github.com/Amir-Helali), [amyblais](https://github.com/amyblais), [andrleite](https://github.com/andrleite), [angeloskyratzakos](https://github.com/angeloskyratzakos), [annaos](https://github.com/annaos), [apshada](https://github.com/apshada), [Aryakoste](https://github.com/Aryakoste), [asaadmahmood](https://github.com/asaadmahmood), [aszakacs](https://github.com/aszakacs), [BarbUk](https://github.com/BarbUk), [BenCookie95](https://github.com/BenCookie95), [Blaieet](https://github.com/Blaieet), [calebroseland](https://github.com/calebroseland), [coltoneshaw](https://github.com/coltoneshaw), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [cyrusjc](https://github.com/cyrusjc), [daran9](https://github.com/daran9), [devharipragaz007](https://github.com/devharipragaz007), [devinbinnie](https://github.com/devinbinnie), [dsspence](https://github.com/dsspence), [Eleferen](https://translate.mattermost.com/user/Eleferen), [EltonGohJH](https://github.com/EltonGohJH), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [ezekielchow](https://github.com/ezekielchow), [fmartingr](https://github.com/fmartingr), [gabrieljackson](https://github.com/gabrieljackson), [gitairman](https://github.com/gitairman), [grundleborg](https://github.com/grundleborg), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [hossain-sazzad](https://github.com/hossain-sazzad), [ifoukarakis](https://github.com/ifoukarakis), [inconnu1](https://github.com/inconnu1), [isacikgoz](https://github.com/isacikgoz), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [johnsonbrothers](https://github.com/johnsonbrothers), [jones](https://translate.mattermost.com/user/jones), [josephjose](https://github.com/josephjose), [jprusch](https://github.com/jprusch), [JulienTant](https://github.com/JulienTant), [jupenur](https://github.com/jupenur), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kaoski](https://github.com/kaoski), [Karimaljandali](https://github.com/Karimaljandali), [kayazeren](https://github.com/kayazeren), [KrisSiegel](https://github.com/KrisSiegel), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [larkox](https://github.com/larkox), [lbr88](https://github.com/lbr88), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [mahdiirar](https://github.com/mahdiirar), [majo](https://translate.mattermost.com/user/majo), [manojmalik20](https://github.com/manojmalik20), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [MeHow25](https://github.com/MeHow25), [mentz](https://translate.mattermost.com/user/mentz), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [movion](https://github.com/movion), [mvitale1989](https://github.com/mvitale1989), [nickmisasi](https://github.com/nickmisasi), [Nityanand13](https://github.com/Nityanand13), [nmnj](https://translate.mattermost.com/user/nmnj), [Obbi89](https://github.com/Obbi89), [pacop](https://github.com/pacop), [phoinixgrr](https://github.com/phoinixgrr), [Pkarle](https://github.com/Pkarle), [poppfredslund](https://translate.mattermost.com/user/poppfredslund), [potatogim](https://github.com/potatogim), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [rahimrahman](https://github.com/rahimrahman), [rOt779kVceSgL](https://translate.mattermost.com/user/rOt779kVceSgL), [RS-labhub](https://github.com/RS-labhub), [Rutam21](https://github.com/Rutam21), [s-krishnaraju](https://github.com/s-krishnaraju), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [Sharuru](https://github.com/Sharuru), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [Syed-Ali-Abbas-Zaidi](https://github.com/Syed-Ali-Abbas-Zaidi), [tanmaythole](https://github.com/tanmaythole), [ThrRip](https://github.com/ThrRip), [tnir](https://github.com/tnir), [toninis](https://github.com/toninis), [topolovac](https://github.com/topolovac), [varghesejose2020](https://github.com/varghesejose2020), [wetneb](https://github.com/wetneb), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yomiadetutu1](https://github.com/yomiadetutu1), [zsrv](https://github.com/zsrv)

----

(release-v9-7-feature-release)=
## Release v9.7 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

- **9.7.6, released 2024-07-02**
  - Mattermost v9.7.6 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where banners set by system administrators did not stack below system banners, but rather appeared underneath them. Existing system banners have remained unchanged.
  - Mattermost v9.7.6 contains no database or functional changes.
- **9.7.5, released 2024-06-03**
  - Mattermost v9.7.5 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.7.5 contains no database or functional changes.
- **9.7.4, released 2024-05-15**
  - Fixed an issue with context cancellation for integration requests [MM-58019](https://mattermost.atlassian.net/browse/MM-58019).
  - Fixed some plugin settings with defaults not changing value [MM-58102](https://mattermost.atlassian.net/browse/MM-58102).
  - Mattermost v9.7.4 contains no database or functional changes.
- **9.7.3, released 2024-04-30**
  - Fixed an issue where creating a Direct Message channel with synthetic users failed [MM-58019](https://mattermost.atlassian.net/browse/MM-58019).
  - Mattermost v9.7.3 contains no database or functional changes.
- **9.7.2, released 2024-04-25**
  - Mattermost v9.7.2 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.7.2 contains no database or functional changes.
  - Pre-packaged Playbooks version [v1.39.3](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v1.39.3).
  - Increased the default payload size limit (``MaximumPayloadSizeBytes``) from 100 kB to 300 kB. Existing servers need to manually update this value.
  - Fixed an issue where it was not possible to clear the plugin settings with a default value in the System Console.
- **9.7.1, released 2024-04-16**
  - Fixed an issue with a noisy log entry for permalink post notifications.
  - Mattermost v9.7.1 contains no database or functional changes.
- **9.7.0, released 2024-04-16**
  - Original 9.7.0 release.

```{Important}
If you upgrade from a release earlier than v9.6, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Improvements

See [this walkthrough video](https://mattermost.com/video/mattermost-v9-7-changelog/) on some of the improvements in our latest release below.

#### User Interface (UI)
 - Added Mattermost [AI plugin](https://github.com/mattermost/mattermost-plugin-ai) to pre-packaged plugins.
 - Pre-packaged Calls version [v0.25.1](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.25.1).
 - Pre-packaged Playbooks version [v1.39.2](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v1.39.2).
 - Pre-packaged GitHub plugin version [v2.2.0](https://github.com/mattermost/mattermost-plugin-github/releases/tag/v2.2.0).
 - The first emoji is now auto-selected in the emoji picker.
 - Added Markdown support for batched email notifications.
 - Users’ timezone is now used in batched email notifications.
 - Removed a conflicting class (``help-text``) from the interactive dialog field description to resolve the black text color in the dark theme.
 - Updated the user interface of **Team Settings** modal.
 - Promoted Simplified Chinese to Beta, and downgraded Hungarian and Spanish languages to Beta.
 - Improved the opening animation of the user settings modal.

#### Administration
 - Upgraded ``@mattermost/client`` and ``@mattermost/types`` to support TypeScript v5.x.
 - Enforced safety limit in compiled Team Edition and Enterprise Edition deployments when enterprise scale and access control automation features are unavailable, and when the count of users who are registered, but not deactivated, exceeds 11,000. ERROR_SAFE_LIMITS_EXCEEDED.
 - Dropped pre-packaged plugins for unsupported OS and architectures.
 - Implemented a new **Export Settings** page in the **System Console** to allow Cloud administrators to customize their dedicated export S3 buckets.
 - LDAP job details are no longer shown until the job runs.
 - Added more logging to the ``NotificationsLog``.
 - A message is now logged when a user tries to log in using an incorrect password.
 - Posts from deactivated users are now included in **Direct Message** channel exports. Also the ``--include-archived-channels`` flag is now respected for **Direct Message** channels.
 - Changed the cache headers for file endpoints to cache privately for 24 hours, instead of not caching at all.
 - Improved the performance of the ElasticSearch indexing job in PostgreSQL installations.
 - Moved following functions from server to public utils:
    - ``ResetReadTimeout``
    - ``AppendMultipleStatementsFlag``
    - ``SetupConnection``
    - ``SanitizeDataSource``

#### mmctl
 - mmctl can now be used to download a Support Packet using ``--local mode``.
 - mmctl system ping will now return detailed server status even if the server status is unhealthy.

### Bug Fixes
 - Fixed an issue where the Desktop App login flow would erroneously show the landing page for first time users.
 - Fixed an issue where a right-hand side card was not reloaded when the card body was updated.
 - Fixed an issue where ``en-AU`` language selection was not allowed.
 - Fixed an issue with the position of text in the default profile picture.
 - Fixed an issue with the group search to parse the display name.
 - Fixed an issue where items with longer text did not widen the user guide dropdown to its max-width.
 - Fixed an issue where the configuration could not be updated from the **System Console** in cloud environments.

### config.json
A new setting option was added to ``config.json``. Below is a list of the addition and its default value on install. The setting can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
 - Under ``CloudSettings`` in ``config.json``:
   - Added a new configuration setting ``Disable`` (via config.json, or environment variable), default ``false``. When set to ``true``, all requests to the Mattermost Customer Portal from a workspace will be disabled.

### Open Source Components
 - Added ``stylelint`` to https://github.com/mattermost/mattermost/.

### Go Version
 - v9.7 is built with Go ``v1.20.7``.

### Known Issues
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.
 
### Contributors
 - [2017Yasu](https://github.com/2017Yasu), [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [amyblais](https://github.com/amyblais), [andriumm](https://github.com/andriumm), [angeloskyratzakos](https://github.com/angeloskyratzakos), [annaos](https://github.com/annaos), [apshada](https://github.com/apshada), [asaadmahmood](https://github.com/asaadmahmood), [ayusht2810](https://github.com/ayusht2810), [azigler](https://github.com/azigler), [BenCookie95](https://github.com/BenCookie95), [Blaieet](https://github.com/Blaieet), [calebroseland](https://github.com/calebroseland), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [devinbinnie](https://github.com/devinbinnie), [dipaksinha1](https://github.com/dipaksinha1), [doc-sheet](https://github.com/doc-sheet), [Eleferen](https://translate.mattermost.com/user/Eleferen),  [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [ezekielchow](https://github.com/ezekielchow), [gabrieljackson](https://github.com/gabrieljackson), [grundleborg](https://github.com/grundleborg), [hannaparks](https://github.com/hannaparks), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hereje](https://github.com/hereje), [hmhealey](https://github.com/hmhealey), [hossain-sazzad](https://github.com/hossain-sazzad), [ifoukarakis](https://github.com/ifoukarakis), [isacikgoz](https://github.com/isacikgoz), [iyampaul](https://github.com/iyampaul), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [johndavidlugtu](https://github.com/johndavidlugtu), [johnsonbrothers](https://github.com/johnsonbrothers), [jones](https://translate.mattermost.com/user/jones), [jprusch](https://github.com/jprusch), [JulienTant](https://github.com/JulienTant), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [Linkinlog](https://github.com/Linkinlog), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo), [marianunez](https://github.com/marianunez), [master7](https://translate.mattermost.com/user/master7), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [mickmister](https://github.com/mickmister), [morgancz](https://github.com/morgancz), [mozi47](https://github.com/mozi47), [mvitale1989](https://github.com/mvitale1989), [nab-77](https://github.com/nab-77), [nachtjasmin](https://github.com/nachtjasmin), [natalie-hub](https://github.com/natalie-hub), [neflyte](https://github.com/neflyte), [nickmisasi](https://github.com/nickmisasi), [phoinixgrr](https://github.com/phoinixgrr), [poppfredslund](https://translate.mattermost.com/user/poppfredslund), [pvev](https://github.com/pvev), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [RyoKub](https://github.com/RyoKub), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [Sharuru](https://translate.mattermost.com/user/Sharuru), [sinansonmez](https://github.com/sinansonmez), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [Syed-Ali-Abbas-Zaidi](https://github.com/Syed-Ali-Abbas-Zaidi), [tanmaythole](https://github.com/tanmaythole), [ThrRip](https://github.com/ThrRip), [toninis](https://github.com/toninis), [varghesejose2020](https://github.com/varghesejose2020), [vish9812](https://github.com/vish9812), [vishal-rathod-07](https://github.com/vishal-rathod-07), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [Wing0515](https://github.com/Wing0515), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yomiadetutu1](https://github.com/yomiadetutu1)

----

(release-v9-6-feature-release)=
## Release v9.6 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

- **9.6.3, released 2024-06-03**
  - Mattermost v9.6.3 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue with some plugin settings with defaults not changing value.
  - Mattermost v9.6.3 contains no database or functional changes.
- **9.6.2, released 2024-04-25**
  - Mattermost v9.6.2 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.6.2 contains no database or functional changes.
  - Pre-packaged Playbooks version [v1.39.3](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v1.39.3).
  - Fixed an issue where it was not possible to clear the plugin settings with a default value in the System Console.
- **9.6.1, released 2024-03-26**
  - Mattermost v9.6.1 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.6.1 contains no database or functional changes.
  - Fixed an issue where the configuration could not be updated from the System Console in cloud environments.
- **9.6.0, released 2024-03-15**
  - Original 9.6.0 release.

### Compatibility
 - Updated minimum required Edge and Chrome versions to 120+.

```{Important}
If you upgrade from a release earlier than v9.5, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Improvements

See [this walkthrough video](https://mattermost.com/video/changelog-v9-6/) on some of the improvements in our latest release below.

#### User Interface (UI)
 - Pre-packaged Calls version [v0.24.0](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.24.0).
 - Pre-packaged GitLab plugin version [v1.8.0](https://github.com/mattermost/mattermost-plugin-gitlab/releases/tag/v1.8.0).
 - Added the [Outgoing OAuth Connections](https://developers.mattermost.com/integrate/slash-commands/outgoing-oauth-connections/) integration type.
 - Re-designed the **System Console > User Management** screen, and added the ability to batch export users in CSV format (Professional and Enterprise plans). On MySQL, users cannot view live results of the batch export in the user interface.
 - Improved the appearance of profile/account menus.
 - Added support for checkbox types in the **System Console** settings.
 - Added support for WebP image previews in the web app similar to PNG and other image formats.
 - Several pre-packaged plugins were removed.

#### Administration
 - Removed some unused Redux actions and reducers, including ``state.entities.posts.selectedPostId``.
 - Limited the number of user preference updates to 10 per call.
 - Clarified that the LDAP profile picture setting is optional.

#### mmctl
 - Extended mmctl with support for user preferences.

### Bug Fixes
 - Fixed an issue with switching to a **Direct Message** channel with a shared channel user (user from another server).
 - Fixed an issue with extra space getting added to code blocks in search results.
 - Fixed an issue where deactivated members were not included in a favorited **Direct Message** channel export.
 - Fixed an issue where password strength settings wouldn't be disabled if they were set through environment variables.
 - Fixed an issue where post mentions would grow outside the viewport on small devices.
 - Fixed an issue with draft removal after deleting the post.
 - Fixed a markdown issue where, on some occasions, extra space was found before a list.
 - Fixed an issue where a sender to a custom group would also receive the message notification themselves.
 - Fixed a web app crash when a System Admin clicked on a link to a private channel that they were not a member of.
 - Fixed ``ChannelHasBeenCreated`` plugin hook not being called when a group channel was created.
 - Fixed thread notifications so that if a user had **Thread Reply Notifications** disabled for your account and **Automatically follow threads in this channel** enabled for a channel, the user wouldn't receive thread notifications for that channel per global setting.

### config.json
 - Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to the Enterprise plan:
 - Under ``ServiceSettings`` in ``config.json``:
    - Added ``EnableOutgoingOAuthConnections`` configuration setting for Outgoing OAuth Connections integration type.

### Open Source Components
 - Added ``@floating-ui/react``, and removed ``@floating-ui/react-dom`` and ``@floating-ui/react-dom-interactions`` from https://github.com/mattermost/mattermost/.

### Go Version
 - v9.6 is built with Go ``v1.20.7``.

### Known Issues
 - Users' initial status is not always loaded correctly [MM-56966](https://mattermost.atlassian.net/browse/MM-56966).
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.
 
### Contributors
 - [abdesslamhouioui](https://github.com/abdesslamhouioui), [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [Alpha-4](https://github.com/Alpha-4), [amyblais](https://github.com/amyblais), [andrleite](https://github.com/andrleite), [angeloskyratzakos](https://github.com/angeloskyratzakos), [apshada](https://github.com/apshada), [arush-vashishtha](https://github.com/arush-vashishtha), [asaadmahmood](https://github.com/asaadmahmood), [avas27JTG](https://github.com/avas27JTG), [ayusht2810](https://github.com/ayusht2810), [azigler](https://github.com/azigler), [BenCookie95](https://github.com/BenCookie95), [bewing](https://github.com/bewing), [calebroseland](https://github.com/calebroseland), [carydrew](https://github.com/carydrew), [Chlbek](https://translate.mattermost.com/user/Chlbek), [compiledsound](https://github.com/compiledsound), [cpatulea](https://github.com/cpatulea), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [devinbinnie](https://github.com/devinbinnie), [DHaussermann](https://github.com/DHaussermann), [edu-ap](https://github.com/edu-ap), [Eleferen](https://translate.mattermost.com/user/Eleferen), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [esarafianou](https://github.com/esarafianou), [ewwollesen](https://github.com/ewwollesen), [gabrieljackson](https://github.com/gabrieljackson), [gourav-varma](https://github.com/gourav-varma), [Gregesp](https://github.com/Gregesp), [grundleborg](https://github.com/grundleborg), [hannaparks](https://github.com/hannaparks), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hereje](https://github.com/hereje), [hmhealey](https://github.com/hmhealey), [iabdousd](https://github.com/iabdousd), [ifoukarakis](https://github.com/ifoukarakis), [isacikgoz](https://github.com/isacikgoz), [it33](https://github.com/it33), [jespino](https://github.com/jespino), [jlandells](https://github.com/jlandells), [johndavidlugtu](https://github.com/johndavidlugtu), [jones](https://translate.mattermost.com/user/jones), [jprusch](https://github.com/jprusch), [JulienTant](https://github.com/JulienTant), [juliovillalvazo](https://github.com/juliovillalvazo), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [lucassabreu](https://github.com/lucassabreu), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo), [marianunez](https://github.com/marianunez), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [MixeroTN](https://translate.mattermost.com/user/MixeroTN), [mjnagel](https://github.com/mjnagel), [morgancz](https://translate.mattermost.com/user/morgancz), [mvitale1989](https://github.com/mvitale1989), [nickmisasi](https://github.com/nickmisasi), [nokedajunky](https://github.com/nokedajunky), [olavinto](https://github.com/olavinto), [oOoBenoitoOo](https://github.com/oOoBenoitoOo), [phoinixgrr](https://github.com/phoinixgrr), [pvev](https://github.com/pvev), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [rOt779kVceSgL](https://translate.mattermost.com/user/rOt779kVceSgL), [sadohert](https://github.com/sadohert), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [Sharuru](https://translate.mattermost.com/user/Sharuru), [sinansonmez](https://github.com/sinansonmez), [sohzm](https://github.com/sohzm), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [svelle](https://github.com/svelle), [Syed-Ali-Abbas-Zaidi](https://github.com/Syed-Ali-Abbas-Zaidi), [TealWater](https://github.com/TealWater), [ThrRip](https://github.com/ThrRip), [titanventura](https://github.com/titanventura), [toninis](https://github.com/toninis), [trangology](https://github.com/trangology), [trivikr](https://github.com/trivikr), [tsabi](https://github.com/tsabi), [Utsav-Ladani](https://github.com/Utsav-Ladani), [varghesejose2020](https://github.com/varghesejose2020), [vidhisaini10](https://github.com/vidhisaini10), [wiggin77](https://github.com/wiggin77), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yeoji](https://github.com/yeoji)

----

(release-v9-5-extended-support-release)=
## Release v9.5 - [Extended Support Release](https://docs.mattermost.com/upgrade/release-definitions.html#extended-support-release-esr)

- **9.5.14, released 2025-05-09**
  - Upgraded logr dependency to v2.0.22 for multiple improvements and bug fixes.
  - Mattermost v9.5.14 contains no database or functional changes.
- **9.5.13, released 2024-11-14**
  - Mattermost v9.5.13 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Calls plugin [v0.29.4](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.29.4).
  - Mattermost v9.5.13 contains no database or functional changes.
- **9.5.12, released 2024-10-28**
  - Mattermost v9.5.12 contains a high severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed desyncing issues with unreads between the team sidebar and the title bar [MM-54021](https://mattermost.atlassian.net/browse/MM-54021).
  - Mattermost v9.5.12 contains no database or functional changes.
- **9.5.11, released 2024-10-10**
  - Mattermost v9.5.11 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue with YouTube previews no longer being displayed [MM-60351](https://mattermost.atlassian.net/browse/MM-60351).
  - Pre-packaged Calls plugin [v0.29.2](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.29.2).
  - Improved the performance of LDAP sync jobs when group-contained teams and channels are used [MM-60253](https://mattermost.atlassian.net/browse/MM-60253).
  - Mattermost v9.5.11 contains no database or functional changes.
- **9.5.10, released 2024-09-26**
  - Mattermost v9.5.10 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed racy use of session in ``NewWebConn`` [MM-60307](https://mattermost.atlassian.net/browse/MM-60307).
  - Pre-packaged Playbooks plugin [v1.40.0](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v1.40.0).
  - Mattermost v9.5.10 contains no database or functional changes.
- **9.5.9, released 2024-08-27**
  - Mattermost v9.5.9 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.5.9 contains no database or functional changes.
- **9.5.8, released 2024-07-22**
  - Mattermost v9.5.8 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.5.8 contains no database or functional changes.
- **9.5.7, released 2024-07-02**
  - Mattermost v9.5.7 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where banners set by system administrators did not stack below system banners, but rather appeared underneath them. Existing system banners have remained unchanged.
  - Added a new configuration setting ``CloudSettings.Disable`` (via config.json, or environment variable), default ``false``. When set to ``true``, all requests to the Mattermost Customer Portal from a workspace will be disabled.
  - Fixed an issue where the user status would incorrectly be set to offline without checking for connections in other nodes in an High Availability cluster [MM-57153](https://mattermost.atlassian.net/browse/MM-57153).
  - Fixed an issue where users could not see the member count in the **Browse Channels** dialog on some servers [MM-56266](https://mattermost.atlassian.net/browse/MM-56266).
  - Increased the maximum length of the ``Value`` column of the ``Preferences`` table [MM-57913](https://mattermost.atlassian.net/browse/MM-57913).
  - Mattermost v9.5.7 contains no database or functional changes.
- **9.5.6, released 2024-06-03**
  - Mattermost v9.5.6 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.5.6 contains no database or functional changes.
- **9.5.5, released 2024-05-15**
  - Fixed an issue where the user status would incorrectly get stuck to online after the user closed their tab [MM-57885](https://mattermost.atlassian.net/browse/MM-57885).
  - Mattermost v9.5.5 contains no database or functional changes.
- **9.5.4, released 2024-04-25**
  - Mattermost v9.5.4 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.5.4 contains no database or functional changes.
  - Pre-packaged Playbooks version [v1.39.3](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v1.39.3).
  - Increased the default payload size limit (``MaximumPayloadSizeBytes``) from 100 kB to 300 kB. Existing servers need to manually update this value.
  - Fixed an issue with context cancellation for integration requests.
  - Fixed an issue where end users were not allowed to fetch the group members list of groups that allow ``@-mentions``.
- **9.5.3, released 2024-03-26**
  - Mattermost v9.5.3 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.5.3 contains no database or functional changes.
  - Improved the performance of the ElasticSearch indexing job in PostgreSQL installations.
- **9.5.2, released 2024-03-06**
  - Mattermost v9.5.2 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.5.2 contains no database or functional changes.
  - Fixed ``ChannelHasBeenCreated`` plugin hook not being called when a group channel was created.
- **9.5.1, released 2024-02-16**
  - Mattermost v9.5.1 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.5.1 contains no database or functional changes.
- **9.5.0, released 2024-02-16**
  - Original 9.5.0 release.

### Important Upgrade Notes
 - We have stopped supporting MySQL v5.7 since it's at the end of life. We urge customers to upgrade their MySQL instance at their earliest convenience.

```{Important}
If you upgrade from a release earlier than v9.4, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Improvements

See [this walkthrough video](https://www.youtube.com/watch?v=b1M2BGGF578&feature=youtu.be) on some of the improvements in our latest release below.

#### User Interface (UI)
 - Pre-packaged Calls version [v0.23.1](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.23.1).
 - Pre-packaged Jira plugin version [v4.1.0](https://github.com/mattermost/mattermost-plugin-jira/releases/tag/v4.1.0).
 - Improved the behavior of suggestion boxes when changing the caret position.
 - Changed the time for tomorrow in the **Do Not Disturb** timer and post reminder to refer to the next day at 9:00am instead of 24hrs from the time of activation.
 - Updated message timestamp tooltips to include seconds.
 - Added a new Wrangler feature to be able to move threads (Experimental). Moving threads requires a Professional/Enterprise license to activate. This feature is not yet recommended for production use. A new feature flag ``MoveThreadsEnabled`` was added and is default OFF. Changing this value to ON will enable the experimental **Move Threads** feature.
 - Applied a wording change for active and activated users in the **System Console** user list.
 - Applied a wording change for active and activated users in the **Team Statistics** page.

#### Administration
 - Added safety limit error message in compiled Team Edition and Enterprise Edition deployments when enterprise scale and access control automation features are unavailable and count of users who are registered and not deactivated exceeds 10,000. ERROR_SAFE_LIMITS_EXCEEDED.
 - The ``where`` field is now rendered in ``model.AppError`` only when it's present.
 - Added Outgoing Oauth implementation ``Get``/``List`` logic.
 - The mmctl bulk import process command in local mode now supports processing an import file without actually uploading it to the server. Simply pass the file path to the import file and the server will directly read from it, and pass the ``--bypass-upload`` flag. There is no need to use the import upload command. NOTE: all of this is applicable only in local mode.
 - Added **Monthly Active Users** (MAU) as part of the true-up report.
 - Prometheus metrics are now available under the Source Available License.

#### Performance
 - Optimized ``createPost`` performance.
 - Improved the performance of emoji uploads.
 - Made small optimizations in several database calls:
     - ``App.HasPermissionToChannel``
     - ``getPostsForChannelAroundLastUnread``
     - ``publishWebsocketEventForPermalinkPost``
     - ``countMentionsFromPost``

#### Plugins
 - Plugins are now allowed to register user settings.
 - Plugins can now register an action in the **User Settings** section. Plugins can also now disable a section in their **User Settings**.
 - Included session id in request payload of the ``WebSocketMessageHasBeenPosted`` plugin hook.

### Bug Fixes
 - Fixed an issue where the right-hand side stopped getting the focus when navigating from **Global Threads** or **Global Drafts**.
 - Fixed a theme issue in the notification settings.
 - Fixed a regression in compliance exports which did not allow the export job to be canceled gracefully on server shutdown.
 - Fixed an error where posts dismissed by a plugin were not properly removed from the view.
 - Fixed an issue where if there were multiple websocket connections from a single user, then in case one connection got removed during a broadcast, there was a possibility that the other good connection would not get the event.
 - Fixed an issue with true-up reports sending active users and not activated users.
 - Fixed an issue where users were not able to navigate through links to private channels they are member of with certain configurations.

### config.json
 - Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
 - Under ``ServiceSettings`` in ``config.json``:
     - Added ``MaximumPayloadSizeBytes`` to add a limit to the payload size of API endpoints passing in arrays.
 - Added a configuration setting ``OutgoingIntegrationRequestsDefaultTimeout`` for integration requests.

#### Changes to the Professional and Enterprise plans:
 - Under ``WranglerSettings`` in ``config.json``:
    - Added ``AllowedEmailDomain`` - a CSV list of strings, where each is an email domain that is allowed to use the feature (e.g. - on community.mattermost.com, ``mattermost.com`` would allow staff to move a thread, while non-staff cannot).
    - ``MoveThreadMaxCount`` - a number representing the maximum number of posts that can be in a thread for it to be moveable.
    - ``MoveThreadToAnotherTeamEnable`` - a boolean value representing whether moving should work across teams.
    - ``MoveThreadFromPrivateChannelEnable`` - a boolean value representing whether moving should work from within a private channel.
    - ``MoveThreadFromDirectMessageChannelEnable`` - a boolean value representing whether moving should be allowed from within a group message.

#### Changes to the Enterprise plan:
 - Under ``DataRetentionSettings`` in ``config.json``:
    - Added two new configuration settings, ``MessageRetentionHours`` and ``FileRetentionHours``, in order to support setting your global retention time in hours. ``DataRetentionSettings.MessageRetentionDays`` and ``DataRetentionSettings.FileRetentionDays`` are deprecated but we will continue to use their value until you set something for their hours equivalent. If Days are set then the hours configuration must be 0 and if hours is set then the days config must be 0. We do not support hours for granular retention policies. Due to how our Elasticsearch indexes are stored, Data retention will now also remove elastic search indexes equal to the day of the retention cut-off time.

### API Changes
 - Added a new API endpoint ``POST /api/v4/posts/<post ID>/move``.
 - Added ``UpdateChannelMembersNotifications`` plugin API.
 - Added plugin APIs and hooks for accessing the **Shared Channels** service via plugins.
 - Added a limit to the payload size of API endpoints passing in arrays.
 - Added ``PreferencesHaveChanged`` plugin hook.
 - Added ``GetPreferenceForUser`` plugin API.
 - Added a new API endpoint ``GET /api/v4/users/report`` for system admin user reporting.
 - Added a new API endpoint ``GET /api/v4/reports/users/count``.

### Open Source Components
 - Added ``@tanstack/react-table`` and ``prometheus/client_model`` to https://github.com/mattermost/mattermost/.

### Go Version
 - v9.5 is built with Go ``v1.20.7``.

### Known Issues
 - User autocomplete no longer stays closed after pressing ESC key [MM-56748](https://mattermost.atlassian.net/browse/MM-56748).
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.
 
### Contributors
 - [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [akbarkz](https://translate.mattermost.com/user/akbarkz), [amyblais](https://github.com/amyblais), [andriuspetrauskis](https://github.com/andriuspetrauskis), [andriuspre](https://github.com/andriuspre), [angeloskyratzakos](https://github.com/angeloskyratzakos), [asaadmahmood](https://github.com/asaadmahmood), [ayusht2810](https://github.com/ayusht2810), [azigler](https://github.com/azigler), [azistellar](https://translate.mattermost.com/user/azistellar), [azizthegit](https://github.com/azizthegit), [bbodenmiller](https://github.com/bbodenmiller), [BenCookie95](https://github.com/BenCookie95), [c0d33ngr](https://github.com/c0d33ngr), [catenacyber](https://github.com/catenacyber), [cedricongjh](https://github.com/cedricongjh), [Chlbek](https://translate.mattermost.com/user/Chlbek), [chriswachira](https://github.com/chriswachira), [coltoneshaw](https://github.com/coltoneshaw), [cpoile](https://github.com/cpoile), [cripton](https://github.com/cripton), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [cyberjam](https://github.com/cyberjam), [devinbinnie](https://github.com/devinbinnie), [duttakapil](https://github.com/duttakapil), [Eleferen](https://translate.mattermost.com/user/Eleferen), [enahum](https://github.com/enahum), [GabrielCasaro](https://github.com/GabrielCasaro), [gabrieljackson](https://github.com/gabrieljackson), [grundleborg](https://github.com/grundleborg), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [heisdinesh](https://github.com/heisdinesh), [hmhealey](https://github.com/hmhealey), [hynex](https://translate.mattermost.com/user/hynex), [ifoukarakis](https://github.com/ifoukarakis), [isacikgoz](https://github.com/isacikgoz), [jespino](https://github.com/jespino), [johndavidlugtu](https://github.com/johndavidlugtu), [johnsonbrothers](https://github.com/johnsonbrothers), [jones](https://translate.mattermost.com/user/jones), [jprusch](https://github.com/jprusch), [JulienTant](https://github.com/JulienTant), [kaakaa](https://github.com/kaakaa), [kerochelo](https://github.com/kerochelo), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo), [marianunez](https://github.com/marianunez), [master7](https://translate.mattermost.com/user/master7), [matoro](https://github.com/matoro), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [milotype](https://translate.mattermost.com/user/milotype), [mkaraki](https://github.com/mkaraki), [mvitale1989](https://github.com/mvitale1989), [nickmisasi](https://github.com/nickmisasi), [Nityanand13](https://github.com/Nityanand13), [norma596](https://translate.mattermost.com/user/norma596), [Omar8345](https://github.com/Omar8345), [phoinixgrr](https://github.com/phoinixgrr), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [Rutam21](https://github.com/Rutam21), [RyoKub](https://github.com/RyoKub), [sapnasivakumar](https://github.com/sapnasivakumar), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [ShrootBuck](https://github.com/ShrootBuck), [SkyDusH](https://translate.mattermost.com/user/SkyDusH), [sonichigo](https://github.com/sonichigo), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [Sudhanva-Nadiger](https://github.com/Sudhanva-Nadiger), [Syed-Ali-Abbas-Zaidi](https://github.com/Syed-Ali-Abbas-Zaidi), [TealWater](https://github.com/TealWater), [thinkGeist](https://github.com/thinkGeist), [thomasbrq](https://github.com/thomasbrq), [ThrRip](https://github.com/ThrRip), [titanventura](https://github.com/titanventura), [toninis](https://github.com/toninis), [trangology](https://github.com/trangology), [tsabi](https://translate.mattermost.com/user/tsabi), [Utsav-Ladani](https://github.com/Utsav-Ladani), [varghesejose2020](https://github.com/varghesejose2020), [vish9812](https://github.com/vish9812), [VishalB98](https://github.com/VishalB98), [wiggin77](https://github.com/wiggin77), [Willy-Wakam](https://github.com/Willy-Wakam), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yaz](https://translate.mattermost.com/user/yaz), [yomiadetutu1](https://github.com/yomiadetutu1)

----

(release-v9-4-feature-release)=
## Release v9.4 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

- **9.4.5, released 2024-03-26**
  - Mattermost v9.4.5 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.4.5 contains no database or functional changes.
- **9.4.4, released 2024-03-06**
  - Mattermost v9.4.4 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.4.4 contains no database or functional changes.
- **9.4.3, released 2024-02-14**
  - Mattermost v9.4.3 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.4.3 contains no database or functional changes.
  - Pre-packaged Jira plugin version [v4.1.0](https://github.com/mattermost/mattermost-plugin-jira/releases/tag/v4.1.0).
- **9.4.2, released 2024-01-30**
  - Mattermost v9.4.2 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue with true-up reports sending active users and not activated users. Added **Monthly Active Users** (MAU) as part of the true-up reports.
  - Mattermost v9.4.2 contains no database or functional changes.
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

See [this walkthrough video](https://www.youtube.com/watch?v=bEMp4vYLi6c&feature=youtu.be&ab_channel=Mattermost) on some of the improvements in our latest release below.

#### User Interface (UI)
 - Updated the pre-packaged GitHub plugin version to [v2.1.7](https://github.com/mattermost/mattermost-plugin-github/releases/tag/v2.1.7).
 - Pre-packaged Calls plugin version [v0.22.2](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.22.2).
 - Improved the user interface of the channel notifications modal.
 - Emojis are now enlarged in emoji tooltips on mouse hover.
 - Added a gap of 8px between buttons in the modal footer when opened in the mobile web view.
 - Updated empty states to align with new branding and made changes to the empty state copy.
 - Adjusted the position of the suggestion list in "Add <user> to a channel" modal to be below or above the text field.

#### Administration
 - Added support for IP Filtering in Cloud (Cloud Enterprise plan) (this feature is disabled by default and behind a feature flag).
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
    - Added two new configuration settings ``CustomSMTPServerName`` and ``CustomSMTPPort`` to allow setting a custom URL and port for Global Relay export. This enables compliance export to integrate with Proofpoint.

### Open Source Components:
 - Added ``@mattermost/desktop-api`` and ``ipaddr.js`` to https://github.com/mattermost/mattermost/.

### Go Version
 - v9.4 is built with Go ``v1.20.7``.

### Known Issues
 - Non-channel-admin users can no longer use message links in private channels [MM-56575](https://mattermost.atlassian.net/browse/MM-56575).
 - Preview doesn't work when editing a channel header [MM-56572](https://mattermost.atlassian.net/browse/MM-56572).
 - The channel member count shows as zero in the **Browse channels** modal [MM-56266](https://mattermost.atlassian.net/browse/MM-56266).
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

----

(release-v9-3-feature-release)=
## Release v9.3 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

- **9.3.3, released 2024-03-06**
  - Mattermost v9.3.3 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.3.3 contains no database or functional changes.
- **9.3.2, released 2024-02-14**
  - Mattermost v9.3.2 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.3.2 contains no database or functional changes.
  - Pre-packaged Jira plugin version [v4.1.0](https://github.com/mattermost/mattermost-plugin-jira/releases/tag/v4.1.0).
- **9.3.1, released 2024-01-30**
  - Mattermost v9.3.1 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.3.1 contains no database or functional changes.
- **9.3.0, released 2023-12-15**
  - Original 9.3.0 release.

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

----

(release-v9-2-feature-release)=
## Release v9.2 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

- **9.2.6, released 2024-02-14**
    - Mattermost v9.2.6 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
    - Mattermost v9.2.6 contains no database or functional changes.
    - Pre-packaged Jira plugin version [v4.1.0](https://github.com/mattermost/mattermost-plugin-jira/releases/tag/v4.1.0).
- **9.2.5, released 2024-01-30**
    - Mattermost v9.2.5 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
    - Mattermost v9.2.5 contains no database or functional changes.
- **9.2.4, released 2024-01-09**
  - Mattermost v9.2.4 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.2.4 contains the following functional changes:
     - Fixed an issue where invalid reactions could be added to posts. Added default limit of the number of reactions per post.
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

----

(release-v9-1-feature-release)=
## Release v9.1 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

- **9.1.5, released 2024-01-09**
  - Mattermost v9.1.5 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.1.5 contains the following functional changes:
     - Fixed an issue where invalid reactions could be added to posts. Added default limit of the number of reactions per post.
- **9.1.4, released 2023-11-29**
  - Mattermost v9.1.4 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.1.4 contains no database or functional changes.
  - Pre-packaged Calls plugin version [v0.21.1](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.21.1).
- **9.1.3, released 2023-11-13**
  - Mattermost v9.1.3 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.1.3 contains no database or functional changes.
  - Pre-packaged Playbooks plugin version [v1.39.1](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v1.39.1).
  - Fixed an issue where the **About Mattermost** dialog reported an incorrect server version.
- **9.1.2, released 2023-11-06**
  - Mattermost v9.1.2 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.1.2 contains no database or functional changes.
- **9.1.1, released 2023-10-27**
  - Mattermost v9.1.1 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Focalboard plugin [v7.11.4](https://github.com/mattermost/focalboard/releases/tag/v7.11.4).
  - Mattermost v9.1.1 contains the following functional changes:
  	- Added a new configuration setting ``MaxFieldSize`` to add the ability to size-limit log fields during logging.
  	- Added a restriction to the mobile Oauth / SAML redirection to match the ``NativeAppSettings.AppCustomURLSchemes`` configuration setting.
- **9.1.0, released 2023-10-16**
  - Original 9.1.0 release

### Important Upgrade Notes
 - Improved performance on data retention ``DeleteOrphanedRows`` queries. See the [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) for notes on a new migration that was added. Removed feature flag ``DataRetentionConcurrencyEnabled``. Data retention now runs without concurrency in order to avoid any performance degradation. Added a new configuration setting ``DataRetentionSettings.RetentionIdsBatchSize``, which allows admins to to configure how many batches of IDs will be fetched at a time when deleting orphaned reactions. The default value is 100.
 - Minimum supported Desktop App version is now v5.3. OAuth/SAML flows were modified to include ``desktop_login`` which makes earlier versions incompatible.

```{Important}
If you upgrade from a release earlier than v9.0, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Compatibility
 - Updated Chromium minimum supported version to 116+.

### Highlights

#### Never Miss Group Messages Again
 - Group messages (GMs) now behave like direct messages (DMs). [The badge count increases for every new message](https://docs.mattermost.com/collaborate/channel-types.html#group-messages).

#### Convert Group Messages to Private Channels
 - Added the ability to [convert a group message to a private channel](https://docs.mattermost.com/collaborate/convert-group-messages.html).

See [this walkthrough video](https://www.youtube.com/watch?v=dbHg-63J9dA) on the highlights and some of the below improvements in our latest release.

### Improvements

#### User Interface (UI)
 - Added a **Cancel** button to the **Delete category** modal.
 - Added the ability to resize the channel sidebar and right-hand sidebar.
 - Added two new filtering options (show all channel types and show private channels) to the **Browse channels** modal.
 - Pre-packaged GitLab plugin version [v1.7.0](https://github.com/mattermost/mattermost-plugin-gitlab/releases/tag/v1.7.0).
 - Pre-packaged Calls plugin version [v0.20.0](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.20.0).
 - Pre-packaged Playbooks version [v1.39.0](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v1.39.0).
 - Added additional reaction options when viewing threads or messages when the sidebar is larger than its minimum width.
 - Added a link to [notification documentation](https://docs.mattermost.com/preferences/manage-your-notifications.html) in the **Notification Settings** modal.
 - Updated the post textbox measurement code to be more reliable.
 - The ``/invite`` slash command now supports custom user groups.
 - Re-enabled the remote marketplace functionality, when configured as per ``PluginSettings.EnableRemoteMarketplace`` [documentation](https://docs.mattermost.com/configure/plugins-configuration-settings.html#plugins-enableremotemarketplace).

#### Administration
 - Added ``mattermost-plugin-api`` into the ``mattermost`` GitHub repository.
 - Updated the public server module version to v0.0.9.
 - Added 2 new URL parameters to ``GET /api/v4/groups``: ``include_archived`` and ``filter_archived``. Added the ability to restore archived groups from the user groups modal.
 - Added file storage information to the support package.
 - A ``user_id`` is now included in all HTTP logs (debug level) to help determine who is generating unexpected traffic.
 - Added new URL parameter to ``GET /api/v4/groups`` and ``GET /api/v4/groups/:group_id``. ``include_member_ids`` will add all the members ``user_ids`` to the group response objects. You can now also add group members to a channel, any members that are not part of the team can be added to the team through this flow and subsequently added the channel.

#### Plugin Changes
 - Added new frontend plugin extension point for the new messages separator bar.
 - Added a new plugin extensibility point to add actions to the code blocks.
 - Added the plugin hook ``UserHasBeenDeactivated``.
 - Added a new server side plugin API method to set the searchable content for file info (``SetFileSearchableContent``). The ``MessageHasBeenPosted`` plugin hook is now executed after the attachments are linked to the post.

### Bug Fixes
 - Fixed keyboard support for the left-hand side channel menu, the left-hand side category menu, and the post dot menu.
 - Fixed display name in the ``comment_on`` component.
 - Fixed an issue with keyboard support for some menus with submenus.
 - Fixed an issue with disappearing punctuation when following a group mention.
 - Fixed an issue where compliance export jobs were not able to start after disabling and enabling the compliance export.
 - Fixed a potential read after write issue when loading a license.
 - Fixed the API to block any changes to direct and group messages names, display name, or purpose.

### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
 - Removed ``ServiceSettingsDefaultGfycatAPISecret`` and ``ServiceSettingsDefaultGfycatAPIKey`` configuration settings.
 - Under ``TeamSettings`` in ``config.json``:
    - Added a new config setting ``EnableJoinLeaveMessageByDefault`` that sets the default value for ``UserSetting``, ``ADVANCED_FILTER_JOIN_LEAVE``.
 - Under ``DisplaySettings`` in ``config.json``:
    - Added a setting ``MaxMarkdownNodes`` to limit the maximum complexity of markdown text on mobile.

 #### Changes to Enterprise plan:
 - Under ``DataRetentionSettings`` in ``config.json``:
    - Added a new configuration setting ``RetentionIdsBatchSize``, which allows admins to to configure how many batches of IDs will be fetched at a time when deleting orphaned reactions. The default value is 100.

### API Changes
 - Added the ``X-Forwarded-For`` request header to the audit stream for all Rest API calls.
 - Added API endpoint ``POST /api/v4/user/login/desktop_login``. Modified OAuth/SAML flows to include ``desktop_login`` where applicable.
 - Added new API endpoint ``GET`` ``/api/v4/channels/<channel-id>/common_teams`` to fetch list of teams common between members of a group message.
 - Added new API endpoint ``POST`` ``/api/v4/channels/<channel-id>/convert_to_channel`` to convert a group message to a private channel.
 - Added a new ``MessageHasBeenDeleted`` hook to the plugin API.
 - Moved the ``request`` package into the public shared folder.

### Go Version
 - v9.1 is built with Go ``v1.20.7``.

### Known Issues
 - Converting a group message to a channel should show an error "A channel with that name already exists on the same team" for duplicate channel names [MM-54713](https://mattermost.atlassian.net/browse/MM-54713).
 - Marking a group message as unread doesn't resurface the numbered notification badge [MM-54778](https://mattermost.atlassian.net/browse/MM-54778).
 - Thread/posts jump when switching to and from preview mode [MM-54758](https://mattermost.atlassian.net/browse/MM-54758).
 - Desktop UI doesn't show all content when the right-hand side thread is opened [MM-54696](https://mattermost.atlassian.net/browse/MM-54696).
 - Left-hand side resize option overrides the **Browse/Create Channel** menu if To-Do plugin is installed [MM-54367](https://mattermost.atlassian.net/browse/MM-54367).
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

### Contributors
 - [abhinav700](https://github.com/abhinav700), [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [alexdecamillo](https://github.com/alexdecamillo), [amyblais](https://github.com/amyblais), [andrleite](https://github.com/andrleite), [angeloskyratzakos](https://github.com/angeloskyratzakos), [asaadmahmood](https://github.com/asaadmahmood), [AsisRout](https://github.com/AsisRout), [ayusht2810](https://github.com/ayusht2810), [azigler](https://github.com/azigler), [BenCookie95](https://github.com/BenCookie95), [calebroseland](https://github.com/calebroseland), [cedarice](https://translate.mattermost.com/user/cedarice), [coltoneshaw](https://github.com/coltoneshaw), [cpoile](https://github.com/cpoile), [Crere89](https://translate.mattermost.com/user/Crere89), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [deivisonrpg](https://github.com/deivisonrpg), [devinbinnie](https://github.com/devinbinnie), [djanda97](https://github.com/djanda97), [Eleferen](https://translate.mattermost.com/user/Eleferen), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [esethna](https://github.com/esethna), [fmartingr](https://github.com/fmartingr), [FokinAleksandr](https://github.com/FokinAleksandr), [gabrieljackson](https://github.com/gabrieljackson), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hibou.sage](https://translate.mattermost.com/user/hibou.sage), [hmhealey](https://github.com/hmhealey), [homerCOD](https://translate.mattermost.com/user/homerCOD), [ialorro](https://github.com/ialorro), [ifoukarakis](https://github.com/ifoukarakis), [intdev32](https://github.com/intdev32), [IronOnet](https://github.com/IronOnet), [isacikgoz](https://github.com/isacikgoz), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [johnsonbrothers](https://github.com/johnsonbrothers), [jprusch](https://github.com/jprusch), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [kyeongsoosoo](https://github.com/kyeongsoosoo), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [LimJiAn](https://github.com/LimJiAn), [limod](https://github.com/limod), [linkvn](https://github.com/linkvn), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo), [manojmalik20](https://github.com/manojmalik20), [marie0394](https://translate.mattermost.com/user/marie0394), [maruTA-bis5](https://github.com/maruTA-bis5), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [mickmister](https://github.com/mickmister), [milotype](https://translate.mattermost.com/user/milotype), [MohammedElansary-dev](https://translate.mattermost.com/user/MohammedElansary-dev), [mornaistar](https://github.com/mornaistar), [mt26691](https://translate.mattermost.com/user/mt26691), [mvitale1989](https://github.com/mvitale1989), [Navystack](https://translate.mattermost.com/user/Navystack), [nickmisasi](https://github.com/nickmisasi), [pvev](https://github.com/pvev), [RayYH](https://github.com/RayYH), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [Sharuru](https://github.com/Sharuru), [sinansonmez](https://github.com/sinansonmez), [speedhs](https://github.com/speedhs), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [teamzamong](https://github.com/teamzamong), [TheRealJoeFriel](https://github.com/TheRealJoeFriel), [ThrRip](https://github.com/ThrRip), [timmycheng](https://github.com/timmycheng), [toninis](https://github.com/toninis), [varghese.jose](https://github.com/varghesejose2020), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [y4aniv](https://github.com/y4aniv), [yasserfaraazkhan](https://github.com/yasserfaraazkhan)

----

(release-v9-0-major-release)=
## Release v9.0 - [Major Release](https://docs.mattermost.com/upgrade/release-definitions.html#major-release)

- **9.0.5, released 2023-11-29**
  - Mattermost v9.0.5 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.0.5 contains no database or functional changes.
  - Pre-packaged Calls plugin version [v0.21.1](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.21.1).
- **9.0.4, released 2023-11-13**
  - Mattermost v9.0.4 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.0.4 contains no database or functional changes.
  - Pre-packaged Playbooks plugin version [v1.39.1](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v1.39.1).
  - Fixed an issue where the **About Mattermost** dialog reported an incorrect server version.
- **9.0.3, released 2023-11-06**
  - Mattermost v9.0.3 contains low to high severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.0.3 contains no database or functional changes.
- **9.0.2, released 2023-10-27**
  - Mattermost v9.0.2 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Focalboard plugin [v7.11.4](https://github.com/mattermost/focalboard/releases/tag/v7.11.4).
  - Mattermost v9.0.2 contains the following functional changes:
  	- Added a new configuration setting ``MaxFieldSize`` to add the ability to size-limit log fields during logging.
  	- Added a restriction to the mobile Oauth / SAML redirection to match the ``NativeAppSettings.AppCustomURLSchemes`` configuration setting.
- **9.0.1, released 2023-10-06**
  - Mattermost v9.0.1 contains low to medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Mattermost v9.0.1 contains no database or functional changes.
- **9.0.0, released 2023-09-15**
  - Original 9.0.0 release

### Important Upgrade Notes
 - Removed the deprecated Insights feature.
 - Mattermost Boards and various other plugins have transitioned to being fully community supported. See this [forum post](https://forum.mattermost.com/t/upcoming-product-changes-to-boards-and-various-plugins/16669) for more details.
 - The ``channel_viewed`` websocket event was changed to ``multiple_channels_viewed``, and is now only triggered for channels that actually have unread messages.

```{Important}
If you upgrade from a release earlier than v8.1, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Highlights

#### Dev/Sec/ChatOps in Strict Security Environments with Jira, Confluence, and Mattermost
 - Accelerate mission-critical workflows that keep your team aligned and your data secure on [the Mattermost and Atlassian platforms](https://mattermost.com/atlassian/).

#### Air-Gapped, Edge-Ready Generative AI with Defense Unicorn's LeapfrogAI
 - Deploy and utilize local GenAI models in edge, air-gapped, and zero-trust environments with [LeapfrogAI and Mattermost](https://defenseunicorns.com/leapfrogai).

#### AI-Accelerated Collaboration
 - Mattermost partner Mobius Logic has enhanced the MS Teams Connector for the Microsoft 365 platform by embedding Mattermost directly inside [Microsoft Teams](https://docs.mattermost.com/about/mattermost-for-microsoft-teams.html).

#### MLOps and Secure Federation with Customer Compliance
 - Our partnership with SOS International (SOSi) enables the integration of advanced military-grade federation using XMPP. Read the [exoINSIGHT announcement from Exovera](https://exovera.com/press-release/exovera-unveils-exoinsight/).

#### Improving Your Organization’s Core Collaboration
 - To optimize the core platform experience, we are reinforcing the fundamentals to ensure Mattermost continues being resilient, stable, and best-in-breed for your critical operations.

### Improvements

#### User Interface (UI)
 - The number of channel members is now shown in the **Browse channels** modal.
 - An error is now displayed if a post edit history fails to load.
 - Added functionality to bulk mark a whole channel category as read.
 - Removed Boards product tour code.
 - Replaced Gfycat with Giphy in the gif picker.
 - Pre-packaged Calls version v0.19.0.
 - Updated Focalboard plugin version to 7.11.3.
 - Pre-packaged Playbooks version 1.38.1.
 - Upgraded prepackaged Zoom plugin to v1.6.2.
 - Upgraded prepackaged Antivirus plugin version to 1.0.0.

#### Administration
 - API examples are now updated to reflect latest Go API conventions, deprecating older code samples.
 - Updated the public server module version to v0.0.8.
 - Added a ``Post Action`` plugin hook to allow plugins to register new items in the post menu.
 - Added a ``Post Editor Action`` plugin hook to allow plugins to register new items in the post editor menu.
 - Improved logging on plugin initialization, activation, and removal.
 - Removed the deprecated ``ManifestExecutables`` struct.
 - Removed the deprecated ``UserAuth.Password`` field.
 - [Remote users](https://docs.mattermost.com/onboard/shared-channels.html) are no longer counted as part of the license.
 - Improved data retention logs.
 - Removed ``/opengraph`` endpoint as it was unused.
 - Transitionally prepackaged plugins are now installed to the filestore for continuity when a future release stops prepackaging those plugins.
 - Removed the deprecated ``Manifest.RequiredConfig`` field.
 - Added a ``NotificationWillBePushed`` plugin hook invoked before the push notification is processed and sent to the notification service. Plugins may modify or reject the push notification.
 - Added a `SendPushNotification` plugin api method which allows plugins to send push notifications to a specific user's mobile sessions.
 - Disabled ``PluginSettings.EnableRemoteMarketplace`` functionality.

### Bug Fixes
 - Fixed the error returned by ``PUT /api/v4/channels/{channelid}`` when the provided name already existed in the team.
 - Fixed an issue where CRLF line endings passed to mmctl commands were not being stripped from commands.
 - Fixed an issue where text copied from Microsoft OneNote is pasted as an image.
 - Fixed an issue preventing successful activation of trial licenses.
 - Fixed an issue where a custom group wouldn't get marked as a mention if it was not part of the webapp's local state.
 - Fixed an issue with the in-product marketplace theming.

### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
 - Under ``ServiceSettings`` in the ``config.json``:
    - Added ``GiphySdkKey`` to replace Gfycat with Giphy in the gif picker.

### Go Version
 - v9.0 is built with Go ``v1.19.5``.

### Open Source Components
 - Added ``@giphy/js-fetch-api`` and ``@giphy/react-components`` to https://github.com/mattermost/mattermost/.
 - Added ``@react-native/eslint-config``, ``@react-native/metro-config``, and ``@tsconfig/react-native`` to https://github.com/mattermost/mattermost-mobile/.

### Known Issues
 - Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
 - The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
 - If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.
 - The Playbooks left-hand sidebar does not update when a user is added to a run or playbook without a refresh.

### Contributors
 - [abdulsmapara](https://github.com/abdulsmapara), [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [akaravashkin](https://github.com/akaravashkin), [amyblais](https://github.com/amyblais), [andrleite](https://github.com/andrleite), [angeloskyratzakos](https://github.com/angeloskyratzakos), [apollo13](https://github.com/apollo13), [aqurilla](https://github.com/aqurilla), [ayusht2810](https://github.com/ayusht2810), [azigler](https://github.com/azigler), [bbodenmiller](https://github.com/bbodenmiller), [BenCookie95](https://github.com/BenCookie95), [Benjamin-Loison](https://github.com/Benjamin-Loison), [calebroseland](https://github.com/calebroseland), [cdmwebs](https://github.com/cdmwebs), [chumano](https://github.com/chumano), [CI-YU](https://github.com/CI-YU), [Coelho](https://translate.mattermost.com/user/Coelho), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [danielsischy](https://github.com/danielsischy), [deivisonrpg](https://github.com/deivisonrpg), [devinbinnie](https://github.com/devinbinnie), [djanda97](https://github.com/djanda97), [douglasstasiak](https://github.com/douglasstasiak), [Eleferen](https://translate.mattermost.com/user/Eleferen), [enahum](https://github.com/enahum), [esarafianou](https://github.com/esarafianou), [esethna](https://github.com/esethna), [gabrieljackson](https://github.com/gabrieljackson), [gary-sixgen](https://github.com/gary-sixgen), [Gobbit69](https://translate.mattermost.com/user/Gobbit69), [grubbins](https://github.com/grubbins), [guneshsji](https://github.com/guneshsji), [hannaparks](https://github.com/hannaparks), [hanzei](https://github.com/hanzei), [harshal2030](https://github.com/harshal2030), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [hpkhanh1610](https://github.com/hpkhanh1610), [ifoukarakis](https://github.com/ifoukarakis), [isacikgoz](https://github.com/isacikgoz), [it33](https://github.com/it33), [ivakorin](https://github.com/ivakorin), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [johndavidlugtu](https://github.com/johndavidlugtu), [johnsonbrothers](https://github.com/johnsonbrothers), [jprusch](https://github.com/jprusch), [JulienTant](https://github.com/JulienTant), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [kyeongsoosoo](https://github.com/kyeongsoosoo), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [LimJiAn](https://github.com/LimJiAn), [lindalumitchell](https://github.com/lindalumitchell), [lindy65](https://github.com/lindy65), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [mahmoudfarouq](https://github.com/mahmoudfarouq), [majo](https://translate.mattermost.com/user/majo), [manojmalik20](https://github.com/manojmalik20), [marianunez](https://github.com/marianunez), [maruTA-bis5](https://translate.mattermost.com/user/maruTA-bis5), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [MatthewDorner](https://github.com/MatthewDorner), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [milotype](https://translate.mattermost.com/user/milotype), [mvitale1989](https://github.com/mvitale1989), [nickmisasi](https://github.com/nickmisasi), [panoramix360](https://github.com/panoramix360), [Partizann](https://github.com/Partizann), [penghao_chn](https://translate.mattermost.com/user/penghao_chn), [phoinixgrr](https://github.com/phoinixgrr), [pjenicot](https://translate.mattermost.com/user/pjenicot), [pvev](https://github.com/pvev), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [RichardScottOZ](https://github.com/RichardScottOZ), [robinsdm](https://github.com/robinsdm), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [Sharuru](https://github.com/Sharuru), [ShrootBuck](https://github.com/ShrootBuck), [sinansonmez](https://github.com/sinansonmez), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [StreakInTheSky](https://github.com/StreakInTheSky), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [svelle](https://github.com/svelle), [tasawar-hussain](https://github.com/tasawar-hussain), [TealWater](https://github.com/TealWater), [thinkGeist](https://github.com/thinkGeist), [ThrRip](https://translate.mattermost.com/user/ThrRip), [timmycheng](https://translate.mattermost.com/user/timmycheng), [toninis](https://github.com/toninis), [tschuyebuhl](https://github.com/tschuyebuhl), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [y4aniv](https://translate.mattermost.com/user/y4aniv), [yash2189](https://github.com/yash2189), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yomiadetutu1](https://github.com/yomiadetutu1), [ZubairImtiaz3](https://github.com/ZubairImtiaz3)
