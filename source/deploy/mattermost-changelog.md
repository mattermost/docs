# Mattermost changelog

[Mattermost](https://mattermost.com) is an open source platform for secure collaboration across the entire software development lifecycle. 
This changelog summarizes updates for the latest self-hosted versions of Mattermost to be [deployed and upgraded on infrastructure you control](https://docs.mattermost.com/guides/deployment.html).

See the [changelog in progress](https://bit.ly/2nK3cVf) for the upcoming release. 
See the [Legacy Self-Hosted Mattermost Changelog](legacy-self-hosted-changelog) for details on all Mattermost self-hosted releases prior to v7.1.

```{contents} On ths page
:depth: 2
```

----

## Release v8.1 - [Extended Support Release](https://docs.mattermost.com/upgrade/release-definitions.html#extended-support-release-esr)

**Release day: August 24, 2023**

### Improvements

#### User interface (UI)
- The number of channel members is now shown in the **Browse channels** modal.
- Increased the nickname field in the user interface from 22 to 64 characters.
- Updated links to documentation in the **System Console**.
- Emoji size is now in scale with the text size in the channel header.
- The emoji picker view modal is now displayed on mobile browsers.
- Updated the minimum required Edge version to 112+.
- An error is now displayed if a post edit history fails to load.
- Removed the deprecated Insights feature.
- Prepackaged Apps plugin version v1.2.2.
- Prepackaged Focalboard plugin version 7.11.2.
- Prepackaged Playbooks version 1.38.0.
- Prepackaged Calls plugin version 0.18.0.

#### Administration
- Added support for a separate Export storage and S3 presigned URLs generation for downloading the export files.
- Using ``https://github.com/reduxjs/redux-devtools`` in production builds is now allowed for webapp.
- Added a new feature flag, ``DataRetentionConcurrencyEnabled``, to enable/disable concurrency for data retention batch deletion. Also added a new configuration setting  ``DataRetentionSettings.TimeBetweenBatchesMilliseconds`` to control the sleep time between batch deletions.
- Added a setting under **System Console > Authentication > Guest Access > Show Guest Tag** to remove the **Guest** badges from within the product.
- Added Apache 2.0 license to the public submodule, explicitly signalling to [pkg.go.dev](https://pkg.go.dev/github.com/mattermost/mattermost/server/public@v0.0.6) the license in play for this source code.
- Added the ability for admins to hide or customize the **Forgot password** link on the login page.
- The ``mattermost database reset`` command no longer starts the application server. It will only start the store layer and truncate the tables excluding the migrations table.

#### Bug fixes
- Fixed an issue where scrollbars were not visible enough on the **File Preview** screen.
- Fixed an issue where SAML Admin Attribute only compared the first value instead of looping through the assertion values array.
- Fixed an issue where updates to recent emojis were not batched when multiple emojis were posted at once.
- Reverted a change that could cause the webapp to forget the current user's authentication method.
- Fixed an issue where drafts would persist after sending an ``@here`` mention in the right-hand side.
- Fixed an issue where the **New messages** toast appeared on channels that were completely visible.
- Fixed an UI issue related to profile popover on channel member search in the right hand pane.
- Fixed an issue where the multi-line channel header preview was too narrow on mobile web view.
- Fixed the render of the **Add Slash Command** page in the backstage area.
- Fixed an issue where user's timezone affected the date selection in the calendar.
- Fixed the clickable area of post textboxes being too small.
- Fixed an UI bug in the bot profile popover.
- Fixed an issue with missing time zone metadata in the Docker container.
- Fixed an issue with the ``registerMessageWillBeUpdatedHook`` plugin hook.
- Fixed an issue where the **Saved Posts** section would not show channel and team names.
- Fixed accessibility issues: tab support at login, reset and signup pages, and controls at the Apps bar.
- Fixed the error returned by ``PUT /api/v4/channels/{channelid}`` when the provided name already existed in the team.

#### Known issues
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
- Boards public links that follow the URL schema `/boards/public/...` no longer work. They can either be regenerated through the application by going to the board and selecting the **Share** button at the top right, or they can be obtained by replacing the `/boards/public/` part of the URL with `/plugins/focalboard/`.

----

:::{figure} ../images/self-hosted-badge.png
:height: 30px
:name: self-hosted
:::

### Go version
 - v8.1 is built with Go ``v1.19.5``.

### Open source components
 - Added ``date-fns`` to https://github.com/mattermost/mattermost/.

### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans
 - Under ``PasswordSettings`` in ``config.json``:
    - Added ``EnableForgotLink`` to add the ability for admins to hide or customize the **Forgot password** link on the login page.
 - Under ``FileSettings`` 
    - Added various export store settings to add support for a new Export storage.

#### Changes to Professional and Enterprise plans
 - Under ``GuestAccountsSettings`` in ``config.json``:
    - Added ``HideTags`` to add the ability to remove the **Guest** badges from within the product.

#### Changes to Enterprise plan
 - ``DataRetentionSettings`` in ``config.json``:
    - Added ``TimeBetweenBatchesMilliseconds`` setting to control the sleep time between batch deletions.

### Contributors

[3kami3](https://github.com/3kami3), [agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [akaMrDC](https://github.com/akaMrDC), [Alanchen](https://translate.mattermost.com/user/Alanchen), [amyblais](https://github.com/amyblais), [andrleite](https://github.com/andrleite), [austin-denoble](https://github.com/austin-denoble), [ayusht2810](https://github.com/ayusht2810), [azigler](https://github.com/azigler), [azistellar](https://translate.mattermost.com/user/azistellar), [bartoszpijet](https://github.com/bartoszpijet), [bbodenmiller](https://github.com/bbodenmiller), [BenCookie95](https://github.com/BenCookie95), [BodhiHu](https://github.com/BodhiHu), [CI-YU](https://translate.mattermost.com/user/CI-YU), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [danielcw-fortuna](https://github.com/danielcw-fortuna), [devinbinnie](https://github.com/devinbinnie), [dirosv-eden](https://translate.mattermost.com/user/dirosv-eden), [dsharma522](https://github.com/dsharma522), [EduardoSellanes](https://github.com/EduardoSellanes), [emdecr](https://github.com/emdecr), [enahum](https://github.com/enahum), [esarafianou](https://github.com/esarafianou), [esethna](https://github.com/esethna), [fmartingr](https://github.com/fmartingr), [gabrieljackson](https://github.com/gabrieljackson), [guuw](https://translate.mattermost.com/user/guuw), [hanh.h.pham](https://translate.mattermost.com/user/hanh.h.pham), [harshal2030](https://github.com/harshal2030), [harshilsharma63](https://github.com/harshilsharma63), [hchorfispiria](https://github.com/hchorfispiria), [hmhealey](https://github.com/hmhealey), [ifoukarakis](https://github.com/ifoukarakis), [invalid-email-address](https://github.com/invalid-email-address), [isacikgoz](https://github.com/isacikgoz), [it33](https://github.com/it33), [janostgren](https://github.com/janostgren), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jlandells](https://github.com/jlandells), [johnsonbrothers](https://github.com/johnsonbrothers), [jprusch](https://github.com/jprusch), [JulienTant](https://github.com/JulienTant), [kaakaa](https://github.com/kaakaa), [karan2704](https://github.com/karan2704), [kayazeren](https://github.com/kayazeren), [komoon8934](https://github.com/komoon8934), [krmh04](https://github.com/krmh04), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [larkox](https://github.com/larkox), [LeonardJouve](https://github.com/LeonardJouve), [lieut-data](https://github.com/lieut-data), [linkvn](https://github.com/linkvn), [loganrosen](https://github.com/loganrosen), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [mahaker](https://github.com/mahaker), [majo](https://translate.mattermost.com/user/majo), [manojmalik20](https://github.com/manojmalik20), [marianunez](https://github.com/marianunez), [master7](https://translate.mattermost.com/user/master7), [matinzd](https://github.com/matinzd), [matt-w99](https://github.com/matt-w99), [matthew-src](https://github.com/matthew-src), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [mkdbns](https://github.com/mkdbns), [morgancz](https://github.com/morgancz), [mustdiechik](https://github.com/mustdiechik), [mvitale1989](https://github.com/mvitale1989), [namanh-asher](https://github.com/namanh-asher), [nickmisasi](https://github.com/nickmisasi), [notlelouch](https://github.com/notlelouch), [orta-contrib](https://github.com/orta-contrib), [panoramix360](https://github.com/panoramix360), [PedroHmaker](https://github.com/PedroHmaker), [phoinix-mm-test](https://github.com/phoinix-mm-test), [phoinixgrr](https://github.com/phoinixgrr), [pjenicot](https://github.com/pjenicot), [potatogim](https://github.com/potatogim), [pvev](https://github.com/pvev), [qryptdev](https://github.com/qryptdev), [ridwankabeer435](https://github.com/ridwankabeer435), [roadt](https://github.com/roadt), [saideepesh000](https://github.com/saideepesh000), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [Sharuru](https://github.com/Sharuru), [ShrootBuck](https://github.com/ShrootBuck), [sinansonmez](https://github.com/sinansonmez), [sonichigo](https://github.com/sonichigo), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [Sudhanva-Nadiger](https://github.com/Sudhanva-Nadiger), [thefourcraft](https://github.com/thefourcraft), [thinkGeist](https://github.com/thinkGeist), [ThrRip](https://github.com/ThrRip), [timmycheng](https://github.com/timmycheng), [toninis](https://github.com/toninis), [tsabi](https://github.com/tsabi), [varghesejose2020](https://github.com/varghesejose2020), [veronicadip](https://github.com/veronicadip), [vish9812](https://github.com/vish9812), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yigitcan-prospr](https://github.com/yigitcan-prospr), [yomiadetutu1](https://github.com/yomiadetutu1)

----

## Release v8.0 - [Major Release](https://docs.mattermost.com/upgrade/release-definitions.html#major-release)

See [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) documentation for details on upgrading to this release.

| **Version** | **Release Date** | **Changes** |
|-------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **v8.0.1**  | 2023-07-26       | Contains medium severity level security fixes. <br> [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. <br> Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).  |
|             |                  | Contains no database or functional changes.  |
|             |                  | Added support for embedding Mattermost in a Microsoft Teams iframe  |
|             |                  | Fixed an issue where the v8.0.0 **About Mattermost** dialog reported an incorrect server version in the Free Plan [MM-53681](https://mattermost.atlassian.net/browse/MM-53681). |
|             |                  | Prepackaged Focalboard plugin version 7.11.2. |
| **8.0.0**   | 2023-07-14       | Original 8.0.0 release  |

:::{admonition} Highlights
:class: tip

- **Private cloud LLMs, Azure AI, and OpenAI integrations**
  - Mattermost provides an OpenOps framework to integrate with private cloud LLMs, Azure AI, and OpenAI models to embed generative AI assistance in collaborative workflows and automation. [Learn more about OpenOps here](https://github.com/mattermost/openops).

- **Mattermost for Microsoft Teams**
  - We’re extending our integration with the Microsoft 365 platform with a new embedded experience directly inside Microsoft Teams, as well as our updated MS Teams Connector.

- **Mattermost for Atlassian Suite**
  - Uplevel your workflows within Mattermost using your Atlassian toolset. [Learn more about Mattermost for Atlassian Suite here](https://mattermost.com/atlassian/).

- **Performance and efficiency with PostgreSQL**
  - To simplify management and scalability challenges, Mattermost 8.0 recommends deploying PostgreSQL over MySQL.

- **New End User Training**
  - We’re introducing [9 new training modules](https://academy.mattermost.com/p/mattermost-end-user-onboarding) dedicated to educating users on the key components of the Mattermost platform and an additional [10 new use case modules](https://academy.mattermost.com/courses/category/use-case-training) tackling technical scenarios within DevOps, Security Ops, and Incident Management.

:::

### Improvements

#### User interface (UI)
- Persistent notifications (Professional and Enterprise Plans) allow users to notify recipients repeatedly until action is taken on an urgent message. Check out [our documentation](https://docs.mattermost.com/channels/message-priority.html#send-persistent-notifications) for more details.
- The apps bar is now enabled by default for on-prem servers. ``ExperimentalSettings.EnableAppBar`` was also renamed to ``ExperimentalSettings.DisableAppBar``. See more details at:
  - https://docs.mattermost.com/configure/experimental-configuration-settings.html#disable-app-bar 
  - https://forum.mattermost.com/t/channel-header-plugin-changes/13551
- Added a **Mattermost Marketplace** option to the bottom of the apps bar. The option is visible when the Marketplace is enabled, and the user has ``SYSCONSOLE_WRITE_PLUGINS`` permissions.
- Calls v0.17.0 introduces a new ringing feature (Beta): Calls in Direct and Group Message channels will ring and pop up a visual notification for the incoming call. Check out the Calls v0.17.0 release notes and [Calls documentation](https://docs.mattermost.com/channels/make-calls.html) for more details.
- Added an **Add channels** button to the bottom of the left-hand sidebar to make the action more obvious for users who want to create or join channels.
- Removed the Webapp Build Hash from **Main Menu > About Mattermost** since it is now identical to Server Build Hash.
- Replaced the ``compass-components`` icon component with ``compass-icons``.
- Added **hours ahead** timezone details to the user profile popover.
- Added an experimental feature to disable re-fetching of channel and channel members on browser focus.
- Bot users are now hidden in the user selector in apps forms.
- Removed the fetching of archived channels on page load.
- The **Channel Type** dropdown within the **Browse Channels** modal can now be focused.
- Removed in-app help pages that were no longer accessible.
- Removed system join/leave messages from thread replies and post them instead in the main channel.
- Added [an experimental setting](https://docs.mattermost.com/configure/experimental-configuration-settings.html#delay-channel-autocomplete) to make the channel autocomplete only appear after typing two characters instead of immediately after the tilde (~).
- Default user profile pictures will now regenerate a new picture when the username changes.
- Implemented URL auto generation on channel creation for when there's no URL-safe characters on its name.
- Added a new option to auto-follow all threads in the channel **Notification Preference** settings.
- ``CTRL/CMD + K`` shortcut can now be used to insert link formatting when text is selected.
- ``pas`` and ``pascal`` code blocks are now higlighted.
- Removed websocket state effects for the collapse/expand state of categories.
- Pre-packaged Jira plugin version 3.2.5.
- Pre-packaged GitHub plugin version 2.1.6.
- Pre-packaged Autolink plugin version 1.4.0.
- Pre-packaged Welcomebot plugin version 1.3.0.
- Pre-packaged NPS plugin version 1.3.2.
- Prepackaged Focalboard plugin version 7.11.0.
- Prepackaged Playbooks plugin version 1.37.0.
- Added support to specify different desktop notification sounds per channel.
- Calls: Ringing sounds can be enabled/disabled and selected in the **Desktop Notifications** preferences panel.

#### Administration
- Added a new ``ConfigurationWillBeSaved`` plugin hook which is invoked before the configuration object is committed to the backing store.
- Admins can now specify index names to ignore while purging indexes from Elasticsearch with the ``ElasticsearchSettings.IgnoredPurgeIndexes`` setting.
- Added an option to use the German HPNS notification proxy.
- New flags were added to the [database migrate command](https://docs.mattermost.com/manage/command-line-tools.html#mattermost-db-migrate) as following:
  - ``auto-recover``: If the migration plan receives an error during migrations, this command will try to rollback migrations already applied within the plan. This option is not recommended to be added without reviewing migration plan. You can review the plan by combining ``--save-plan`` and ``--dry-run`` flags.
  - ``save-plan``: The plan for the migration will be saved into the file store so that it can be used for reviewing the plan or to be used for downgrading.
  - ``dry-run``: Does not apply the migrations, but it validates how the migration would run with the given conditions.
- A new [database subcommand](https://docs.mattermost.com/manage/command-line-tools.html#mattermost-db-downgrade) "downgrade" was added to be able to rollback database migrations. The command either requires an update plan to rollback, or comma separated version numbers.
- Removed ``/api/v4/users/stats`` network request from ``InviteMembersButton``.
- Self-hosted admins can now define a separate shipping address during in-product license purchase.
- Added updates to the trial request forms to allow for a more tailored trial experience.
- First admins will now have an onboarding experience that includes first team creation based on company name and invite members link steps. 
- Adds the ability to expand seats in-product for self-hosted servers.
- Added the ability to search a partial first name, last name, nickname, or username on the **System Console > Users** page.
- **Contact Support** now redirects users to Zendesk and pre-fills known information.
- Added a mechanism for public routes on products and used it to support publicly shared Board links.
- The database section in the **System Console** now has an additional read-only section which shows the active search backend in use. This can be helpful to confirm which search engine is currently active when there are multiple configured.
- Updated Docker Base Image from Debian to Ubuntu 22.04 LTS.
- Type-generated settings will now be generated (only for future generations) with a URL-safe version of base64 encoding.
- Mattermost is now resilient against database replica outages and will dynamically choose a replica if it's alive. Also a config parameter ``ReplicaMonitorIntervalSeconds`` was added and the default value is 5. This controls how frequently unhealthy replicas will be monitored for liveness check.

### Performance
- Improved the performance of webapp related to timezone calculations.
- Improved performance of code used for post list screen reader support.

### API Changes
- An underscore is now used in the timeline API (``event-id`` -> ``event_id``) for consistency with other API arguments.

### Bug fixes
- Fixed a scrolling issue in the purchase modals.
- Fixed an issue where the experimental Shared Channels feature failed to synchronize if a previously removed table column was still present.
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
- Fixed the **New Messages** line overlapping date lines in the post list.
- Fixed an issue where post reactions disappeared when the search sidebar was open.
- Fixed an issue with broken "medical_symbol", "male_sign", and "female_sign" emojis.
- Fixed a panic where a JSON null value was passed as a channel update.
- Fixed an issue where the draft counter badge remained in cases where a deleted parent post was removed.
- Fixed an issue where posts were not fully sanitized for audit output when a link preview was included.
- Fixed an issue where the footer with **Save/Cancel** buttons did not get anchored properly in the System Console.
- Fixed an issue where the undo history was erased when links, tables, or code was pasted into the textbox.
- Fixed an issue where Elasticsearch didn't properly start on startup when enabled. Also added a missing ``IsEnabled`` method to Elasticsearch.
- Fixed an issue where text couldn't be copied from the post textbox.
- Fixed an issue where using **SHIFT+TAB** with a screen reader placed the cursor focus at the bottom of the channel rather than at the post that was linked to.

### Known issues
- White screen might appear when creating a slash command [MM-53665](https://mattermost.atlassian.net/browse/MM-53665).
- When sending a draft message in a Thread, the message is not cleared if the thread is open in the right-hand side [MM-53520](https://mattermost.atlassian.net/browse/MM-53520).
- Channel and team names are missing from **Saved Posts** in the right-hand side [MM-53636](https://mattermost.atlassian.net/browse/MM-53636).
- Adding an @mention at the start of a post draft and pressing the left or right arrow key can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
- Google login fails on the Classic mobile apps.
- Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
- Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
- The team sidebar on the desktop app does not update when channels have been read on mobile.
- Slack import through the CLI fails if email notifications are enabled.
- Push notifications don't always clear on iOS when running Mattermost in High Availability mode.
- The Playbooks left-hand sidebar doesn't update when a user is added to a run or playbook without a refresh.
- If a user isn't a member of a configured broadcast channel, posting a status update might fail without any error feedback. As a temporary workaround, join the configured broadcast channels, or remove those channels from the run configuration.

----

:::{figure} ../images/self-hosted-badge.png
:height: 30px
:name: self-hosted
:::

### Go version
- v8.0 is built with Go ``v1.19.5``.

### Open source components
- Added ``date-fns`` to https://github.com/mattermost/mattermost/.

### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans
- Removed ``EnableInactivityEmail`` config setting.
- Added a new config setting section ``ProductSettings``.
- Under ``ExperimentalSettings`` in ``config.json``:
  - Added ``DelayChannelAutocomplete``, to make the channel autocomplete only appear after typing a couple letters instead of immediately after a tilde.
  - Added ``DisableRefetchingOnBrowserFocus``, to disable re-fetching of channel and channel members on browser focus.
  - Added ``DisableAppBar`` to enable apps bar by default.
- Three configuration fields have been added, ``LogSettings.AdvancedLoggingJSON``, ``ExperimentalAuditSettings.AdvancedLoggingJSON``, and ``NotificationLogSettings.AdvancedLoggingJSON`` which support multi-line JSON, escaped JSON as a string, or a filename that points to a file containing JSON.  The ``AdvancedLoggingConfig`` fields have been deprecated.


#### Changes to Professional and Enterprise plans
- Under ``ServiceSettings`` in ``config.json``:
  - Added new configuration settings ``AllowPersistentNotifications``, ``PersistentNotificationIntervalMinutes``, ``PersistentNotificationMaxCount``, ``PersistentNotificationMaxRecipients``, to add a persistent notification option when sending urgent priority posts.

#### Changes to Enterprise plan
- Under ``ElasticsearchSettings`` in ``config.json``:
  - Now you can specify index names to ignore while purging indexes from Elasticsearch with the ``IgnoredPurgeIndexes`` setting.

### Contributors

[agarciamontoro](https://github.com/agarciamontoro), [agnivade](https://github.com/agnivade), [akaMrDC](https://translate.mattermost.com/user/akaMrDC), [akaravashkin](https://github.com/akaravashkin), [amyblais](https://github.com/amyblais), [andriusbal](https://github.com/andriusbal), [andrleite](https://github.com/andrleite), [aqurilla](https://github.com/aqurilla), [asaadmahmood](https://github.com/asaadmahmood), [ayusht2810](https://github.com/ayusht2810), [azigler](https://github.com/azigler), [bbodenmiller](https://github.com/bbodenmiller), [BenCookie95](https://github.com/BenCookie95), [calebroseland](https://github.com/calebroseland), [chenilim](https://github.com/chenilim), [chumano](https://translate.mattermost.com/user/chumano), [CI-YU](https://translate.mattermost.com/user/CI-YU), [coltoneshaw](https://github.com/coltoneshaw), [cpoile](https://github.com/cpoile), [creeper-0910](https://translate.mattermost.com/user/creeper-0910), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [devinbinnie](https://github.com/devinbinnie), [diciwall](https://translate.mattermost.com/user/diciwall), [DieAkuteSense](https://github.com/DieAkuteSense), [dirosv-eden](https://github.com/dirosv-eden), [Ele7o](https://translate.mattermost.com/user/Ele7o), [Eleferen](https://translate.mattermost.com/user/Eleferen), [enahum](https://github.com/enahum), [Esterjudith](https://github.com/Esterjudith), [fmartingr](https://github.com/fmartingr), [fnogcps](https://github.com/fnogcps), [gabrieljackson](https://github.com/gabrieljackson), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [ifoukarakis](https://github.com/ifoukarakis), [ilies-bel](https://github.com/ilies-bel), [invalid-email-address](https://github.com/invalid-email-address), [isacikgoz](https://github.com/isacikgoz), [it33](https://github.com/it33), [ivalkshfoeif](https://github.com/ivalkshfoeif), [iyampaul](https://github.com/iyampaul), [janostgren](https://github.com/janostgren), [jasonblais](https://github.com/jasonblais), [jespino](https://github.com/jespino), [jprusch](https://github.com/jprusch), [JulienTant](https://github.com/JulienTant), [jupenur](https://github.com/jupenur), [kaakaa](https://translate.mattermost.com/user/kaakaa), [karan2704](https://github.com/karan2704), [kayazeren](https://github.com/kayazeren), [kostaspt](https://github.com/kostaspt), [krmh04](https://github.com/krmh04), [kyeongsoosoo](https://github.com/kyeongsoosoo), [larkox](https://github.com/larkox), [leonambeez](https://github.com/leonambeez), [LeonardJouve](https://github.com/LeonardJouve), [lieut-data](https://github.com/lieut-data), [lmedoshvili](https://translate.mattermost.com/user/lmedoshvili), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [mahaker](https://github.com/mahaker), [majo](https://translate.mattermost.com/user/majo), [manojmalik20](https://github.com/manojmalik20), [marianunez](https://github.com/marianunez), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-src](https://github.com/matthew-src), [matthew-w](https://translate.mattermost.com/user/matthew-w), [MattSilvaa](https://github.com/MattSilvaa), [mgdelacroix](https://github.com/mgdelacroix), [mickmister](https://github.com/mickmister), [milotype](https://github.com/milotype), [morgancz](https://github.com/morgancz), [muratbayan](https://translate.mattermost.com/user/muratbayan), [mvitale1989](https://github.com/mvitale1989), [natalie-hub](https://github.com/natalie-hub), [nathanaelhoun](https://translate.mattermost.com/user/nathanaelhoun), [nevyangelova](https://github.com/nevyangelova), [nickmisasi](https://github.com/nickmisasi), [nihaldivyam](https://github.com/nihaldivyam), [pablo-suazo](https://github.com/pablo-suazo), [panklobouk](https://translate.mattermost.com/user/panklobouk), [Partizann](https://github.com/Partizann), [phoinix-mm-test](https://github.com/phoinix-mm-test), [phoinixgrr](https://github.com/phoinixgrr), [pjenicot](https://translate.mattermost.com/user/pjenicot), [pvev](https://github.com/pvev), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [ridwankabeer435](https://github.com/ridwankabeer435), [rOt779kVceSgL](https://translate.mattermost.com/user/rOt779kVceSgL), [RoyI99](https://github.com/RoyI99), [saideepesh000](https://github.com/saideepesh000), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [shivamjosh](https://github.com/shivamjosh), [sinansonmez](https://github.com/sinansonmez), [SkyLuke91](https://translate.mattermost.com/user/SkyLuke91), [spirosoik](https://github.com/spirosoik), [sri-byte](https://github.com/sri-byte), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [tejaskarelia17](https://github.com/tejaskarelia17), [tfromont](https://translate.mattermost.com/user/tfromont), [ThrRip](https://translate.mattermost.com/user/ThrRip), [timmycheng](https://github.com/timmycheng), [toninis](https://github.com/toninis), [tsabi](https://translate.mattermost.com/user/tsabi), [ujwalkumar1995](https://github.com/ujwalkumar1995), [vish9812](https://github.com/vish9812), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [yomiadetutu1](https://github.com/yomiadetutu1), [zhsj](https://github.com/zhsj)

----

## Release vx.x - [Release Type](xxx)

 **Version** | **Release Date** | **Changes** |
|-------------|------------------|--------------|
| **vx.x.x**  | 2023-0X-XX       | x |

:::{admonition} Highlights
:class: tip
:::

### Improvements

#### User interface (UI)

#### Administration

### Bug fixes

### Known issues

----

:::{figure} ../images/self-hosted-badge.png
:height: 30px
:name: self-hosted
:::

### Go version

### Open source components

### config.json

#### Changes to all plans

#### Changes to Professional and Enterprise plans

#### Changes to Enterprise plan

### Contributors

----

## Release vY.x - [Release Type](xxx)

 **Version** | **Release Date** | **Changes** |
|-------------|------------------|--------------|
| **vY.x.x**  | 2023-0X-XX       | x |

:::{admonition} Highlights
:class: tip
Release highlights
:::

### Improvements

::::{tab-set}
:::{tab-item} Tab 1
:sync: tab1
Tab one
:::

:::{tab-item} Tab 2
:sync: tab2
Tab two
:::
::::

#### User interface (UI)

#### Administration

### Bug fixes

### Known issues

----

:::{figure} ../images/self-hosted-badge.png
:height: 30px
:name: self-hosted
:::

### Go version

### Open source components

### config.json

#### Changes to all plans

#### Changes to Professional and Enterprise plans

#### Changes to Enterprise plan

### Contributors
