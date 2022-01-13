# Mattermost Self-Hosted Changelog
[Mattermost](https://mattermost.com) is an open source platform for secure collaboration across the entire software development lifecycle. This changelog summarizes updates for the latest self-hosted versions of Mattermost.

See the [changelog in progress](https://bit.ly/2nK3cVf) for the upcoming release. See the [Legacy Self-Hosted Mattermost Changelog](legacy-self-hosted-changelog) for details on all Mattermost self-hosted releases prior to v5.37. 

## Latest Mattermost releases
- [Release v6.2 - Feature Release](#release-v6.2-feature-release)
- [Release v6.1 - Feature Release](#release-v6.1-feature-release)
- [Release v6.0 - Feature Release](#release-v6.0-feature-release)
- [Release v5.39 - Quality Release](#release-v5-39-quality-release)

## Release v6.2 - [Feature Release](https://docs.mattermost.com/administration/release-definitions.html#feature-release)

- **v6.2.1, released 2021-12-17**
  - Mattermost v6.2.1 contains a medium level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue where a SIGSEGV error occurred after upgrading to v6.2.0 when plugins were disabled in configuration.
- **v6.2.0, released 2021-12-16**
  - Mattermost v6.2.0 contains low to medium level security fixes. [Upgrading](https://docs.mattermost.com/administration/upgrade.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.org/responsible-disclosure-policy/).

### Important Upgrade Notes
 -  Channel results in the channel autocomplete will include private channels. Customers using [Bleve](https://docs.mattermost.com/deploy/bleve-search.html) or [Elasticsearch](https://docs.mattermost.com/scale/elasticsearch.html) for autocomplete will have to reindex their data to get the new results. Since this can take a long time, we suggest disabling autocomplete and running indexing in the background. When this is complete, re-enable autocomplete. Note that only channel members will see private channel names in autocomplete results.

**IMPORTANT:** If you upgrade from a release earlier than v6.1, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).

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
 - [Collapsed Reply Threads](https://docs.mattermost.com/messaging/organizing-conversations.html) is currently in beta. Before enabling the feature, please ensure you are well versed in the [known issues](https://docs.mattermost.com/messaging/organizing-conversations.html#known-issues), particularly relating to database resource requirements and server performance implications. If you cannot easily scale up your database size, or are running the Mattermost application server and database server on the same machine, we recommended waiting to enable Collapsed Reply Threads until it's [promoted to general availability in Q1 2022](https://mattermost.com/blog/collapsed-reply-threads-ga). Learn more about these [performance considerations here](https://support.mattermost.com/hc/en-us/articles/4413183568276).
 - Member type is missing from autocomplete [MM-38989](https://mattermost.atlassian.net/browse/MM-38989).
 - File upload might fail for SVG files [MM-38982](https://mattermost.atlassian.net/browse/MM-38982).
 - ``CTRL/CMD + SHIFT + A`` shortcut does not open **Settings** [MM-38236](https://mattermost.atlassian.net/browse/MM-38236).
 - Known issues related to the Collapsed Reply Threads (Beta) are [listed here](https://docs.mattermost.com/messaging/organizing-conversations.html#known-issues).
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

## Release v6.1 - [Feature Release](https://docs.mattermost.com/administration/release-definitions.html#feature-release)

- **v6.1.1, released 2021-12-17**
  - Mattermost v6.1.1 contains medium level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Added a general performance fix for loading the web application and typing.
  - Improved performance while typing by moving some autocomplete layout calculations.
  - Improved performance by reducing DOM usage during render.
  - Removed real-time updates of a couple of features to prevent overloading servers on user updates. The "This channel contains guests" indicator and the number of timezones displayed when notifying members of a group will only be updated on channel change now.
  - Fixed slow channel loading for instances with website link previews enabled.
  - Fixed an issue with Focalboard where an empty white screen appeared in Mattermost desktop app on reload.
  - Fixed an issue where v6.1 reported an incorrect mmctl version.
- **v6.1, released 2021-11-16**
  - Mattermost v6.1.0 contains low level security fixes. [Upgrading](https://docs.mattermost.com/administration/upgrade.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.org/responsible-disclosure-policy/).

### Important Upgrade Notes
 - Please refer to [the schema migration analysis](https://gist.github.com/streamer45/997b726a86b5d2a624ac2af435a66086) when upgrading to v6.1.
 - The Bleve index has been updated to use the scorch index type. This new default index type features some efficiency improvements which means that the indexes use significantly less disk space. To use this new type of index, after upgrading the server version, run a purge operation and then a reindex from the Bleve section of the System Console. Bleve is still compatible with the old indexes, so the currently indexed data will work fine if the purge and reindex is not run.
 - A composite index has been added to the jobs table for better query performance. For some customers with a large jobs table, this can take a long time, so we recommend adding the index during off-hours, and then running the migration. A table with more than 1 million rows can be considered as large enough to be updated prior to the upgrade.
   - For PostgreSQL: ``create index concurrently idx_jobs_status_type on jobs (status,type);``
   - For MySQL: ``create index idx_jobs_status_type on Jobs (Status,Type);``

**IMPORTANT:** If you upgrade from a release earlier than v6.0, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).

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
 - [Collapsed Reply Threads](https://docs.mattermost.com/messaging/organizing-conversations.html) is currently in beta. Before enabling the feature, please ensure you are well versed in the [known issues](https://docs.mattermost.com/messaging/organizing-conversations.html#known-issues),  particularly relating to database resource requirements and server performance implications. If you cannot easily scale up your database size, or are running the Mattermost application server and database server on the same machine, we recommended waiting to enable Collapsed Reply Threads until it's [promoted to general availability in Q1 2022](https://mattermost.com/blog/collapsed-reply-threads-ga/). Learn more about these [performance considerations here](https://support.mattermost.com/hc/en-us/articles/4413183568276).
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
 
## Release v6.0 - [Feature Release](https://docs.mattermost.com/administration/release-definitions.html#feature-release)

- **v6.0.4, released 2021-12-17**
  - Mattermost v6.0.4 contains medium level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Added a general performance fix for loading the web application and typing.
  - Improved performance while typing by moving some autocomplete layout calculations.
  - Improved performance by reducing DOM usage during render.
  - Removed real-time updates of a couple of features to prevent overloading servers on user updates. The "This channel contains guests" indicator and the number of timezones displayed when notifying members of a group will only be updated on channel change now.
  - Fixed slow channel loading for instances with website link previews enabled.
  - Fixed an issue where v6.0 reported an incorrect mmctl version.
- **v6.0.3, released 2021-11-15**
  - Mattermost v6.0.3 contains a medium level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed a possible panic during data retention jobs when ``DataRetentionSettings.EnableMessageDeletion`` was set to ``true`` [MM-39378](https://mattermost.atlassian.net/browse/MM-39378).
  - Fixed a potential panic during the message export job [MM-39521](https://mattermost.atlassian.net/browse/MM-39521).
  - Fixed some sentry crashes [MM-38565](https://mattermost.atlassian.net/browse/MM-38565), [MM-39208](https://mattermost.atlassian.net/browse/MM-39208), [MM-39420](https://mattermost.atlassian.net/browse/MM-39420).
- **v6.0.2, released 2021-10-27**
  - Mattermost v6.0.2 contains medium level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed a race condition in telemetry IDs on High Availability servers [MM-39343](https://mattermost.atlassian.net/browse/MM-39343).
  - Update prepackaged Boards version to 0.9.4.
- **v6.0.1, released 2021-10-18**
  - Mattermost v6.0.1 contains a medium level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed a panic in translations that caused the server to not run properly. The panic caused the server to be terminated [MM-39299](https://mattermost.atlassian.net/browse/MM-39299).
  - Fixed an issue with the v6.0 migration where the ``Users.Timezone`` column had a default. This affected servers that had Mattermost v4.9 or earlier installed before upgrading [MM-39297](https://mattermost.atlassian.net/browse/MM-39297).
  - Fixed an issue where a migration check failed for MariaDB databases. The data type JSON was aliased to ``LONGTEXT`` and the check was failing and causing the database migrations to run every restart.
  - Added a fix to display ``tableName`` and ``columnName`` for JSONB schema failures. When there was a schema upgrade failure related to jsonb columns, the log line didn't mention which table/column was affected.
  - Fixed an issue where selecting the "..." post menu on a System message crashed the webapp [MM-39116](https://mattermost.atlassian.net/browse/MM-39116).
- **v6.0.0, released 2021-10-13**
  - Original 6.0.0 release

### Deprecations

1. [Legacy Command Line Tools](https://docs.mattermost.com/manage/command-line-tools.html). Most commands have been replaced by [mmctl](https://docs.mattermost.com/manage/mmctl-command-line-tool.html) and new commands have been added over the last few months, making this tool a robust replacement.

2. [Slack Import via the web app](https://docs.mattermost.com/onboard/migrating-to-mattermost.html#migrating-from-slack-using-the-mattermost-web-app). The Slack import tool accessible via the Team Setting menu has been replaced by the [mmetl](https://docs.mattermost.com/onboard/migrating-to-mattermost.html#migrating-from-slack-using-the-mattermost-mmetl-tool-and-bulk-import) tool that is much more comprehensive for the types of data it can assist in uploading. 

3. MySQL versions below 5.7.12. Minimum support is now for 5.7.12+. This version introduced a native JSON data type that lets us improve performance and scalability of several database fields (most notably Users and Posts props). Additionally, version 5.6 (our current minimum version) reached [EOL in February 2021](https://www.mysql.com/support/eol-notice.html).

4. Elasticsearch 5 and 6 - [versions 5.x reached EOL in March of 2019, and versions 6.x reached EOL in November 2020](https://www.elastic.co/support/eol). Our minimal supported version with Mattermost v6.0 is Elasticsearch version 7.0.

5. Windows 7 reached [EOL in January 2020](https://support.microsoft.com/en-us/windows/windows-7-support-ended-on-january-14-2020-b75d4580-2cc7-895a-2c9c-1466d9a53962). We no longer provide support for Mattermost Desktop App issues on Windows 7.

6. [DisableLegacyMFAEndpoint](https://docs.mattermost.com/configure/configuration-settings.html#disable-legacy-mfa-api-endpoint) configuration setting.

7. [ExperimentalTimezone](https://docs.mattermost.com/configure/configuration-settings.html#timezone) configuration setting. The config setting is removed and the feature is promoted to general availability.

8. All legacy channel sidebar experimental configuration settings. We encourage customers using these settings to upgrade to v5.32 or later to access [custom, collapsible channel categories](https://mattermost.com/blog/custom-collapsible-channel-categories/) among many other channel organization features. The deprecated settings include:

   - [EnableLegacySidebar](https://docs.mattermost.com/configure/configuration-settings.html#enable-legacy-sidebar)
   - [ExperimentalTownSquareIsReadOnly](https://docs.mattermost.com/configure/configuration-settings.html#town-square-is-read-only-experimental)
   - [ExperimentalHideTownSquareinLHS](https://docs.mattermost.com/configure/configuration-settings.html#town-square-is-hidden-in-left-hand-sidebar-experimental)
   - [EnableXToLeaveChannelsFromLHS](https://docs.mattermost.com/configure/configuration-settings.html#enable-x-to-leave-channels-from-left-hand-sidebar-experimental)
   - [CloseUnusedDirectMessages](https://docs.mattermost.com/configure/configuration-settings.html#autoclose-direct-messages-in-sidebar-experimental)
   - [ExperimentalChannelOrganization](https://docs.mattermost.com/configure/configuration-settings.html#sidebar-organization)
   - [ExperimentalChannelSidebarOrganization](https://docs.mattermost.com/configure/configuration-settings.html#experimental-sidebar-features)

9. [All configuration settings previously marked as “Deprecated”](https://docs.mattermost.com/configure/configuration-settings.html#deprecated-configuration-settings).

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
 - The advanced logging configuration schema changed. This is a breaking change relative to 5.x. See updated [documentation](https://docs.mattermost.com/comply/audit-log.html).
 - Some breaking changes to plugins are included:
   - Support for left-hand side-specific bot icons was dropped.
   - Removed a deprecated "Backend" field from the plugin manifest.
   - Converted the "Executables" field in the plugin manifest to a map.

**IMPORTANT:** If you upgrade from a release earlier than v5.39, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).

### Highlights

#### Multi-Product Platform
 - Mattermost now ships as one platform with three products - Channels, Playbooks, and Boards.
 - Playbooks and Boards are visible when [plugins are enabled system-wide](https://docs.mattermost.com/configure/configuration-settings.html#enable-plugins). 

#### Global Product Launcher
 - Added a global header for product navigation for Channels, Playbooks, and Boards. This is disabled on the mobile web view and mobile apps.

#### Branding Changes
 - Added a new default brand theme named "Denim".
 - The existing theme names and colors, including "Mattermost", "Organization", "Mattermost Dark", and "Windows Dark" have been updated to the new "Denim", "Sapphire", "Quartz", "Indigo", and "Onyx" theme names and colors, respectively. Anyone using the existing themes will see slightly modified theme colors after their server or workspace is upgraded. The theme variables for the existing "Mattermost", "Organization", "Mattermost Dark", and "Windows Dark" themes will still be accessible in [our documentation](https://docs.mattermost.com/messaging/customizing-theme-colors.html#custom-theme-examples), so a custom theme can be created with these theme variables if desired. Custom themes are unaffected by this change.
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
 - Removed the following deprecated CLI commands in favor of [mmctl](https://docs.mattermost.com/manage/mmctl-command-line-tool.html):
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
 - [Collapsed Reply Threads](https://docs.mattermost.com/messaging/organizing-conversations.html) is currently in beta. Before enabling the feature, please ensure you are well versed in the [known issues](https://docs.mattermost.com/messaging/organizing-conversations.html#known-issues),  particularly relating to database resource requirements and server performance implications. If you cannot easily scale up your database size, or are running the Mattermost application server and database server on the same machine, we recommended waiting to enable Collapsed Reply Threads until it is [promoted to general availability in Q1 2022](https://mattermost.com/blog/collapsed-reply-threads-ga/). Learn more about these [performance considerations here](https://support.mattermost.com/hc/en-us/articles/4413183568276).
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

## Release v5.39 - [Quality Release](https://docs.mattermost.com/upgrade/release-definitions.html#quality-release)

- **v5.39.3, released 2021-12-17**
  - Mattermost v5.39.3 contains medium level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Added a general performance fix for loading the web application and typing.
  - Improved performance while typing by moving some autocomplete layout calculations.
  - Improved performance by reducing DOM usage during render.
  - Removed real-time updates of a couple of features to prevent overloading servers on user updates. The "This channel contains guests" indicator and the number of timezones displayed when notifying members of a group will only be updated on channel change now.
  - Fixed an issue where v5.39 reported an incorrect mmctl version.
- **v5.39.2, released 2021-11-15**
  - Mattermost v5.39.1 contains a medium level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
- **v5.39.1, released 2021-10-27**
  - Mattermost v5.39.1 contains a medium level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed an issue with fetching threads upon websocket reconnection.
  - Fixed a race condition in telemetry IDs on High Availability servers [MM-39343](https://mattermost.atlassian.net/browse/MM-39343).
- **5.39.0, released 2021-09-16**
  - Original 5.39 release

Mattermost v5.39.0 contains a low level security fix. [Upgrading](https://docs.mattermost.com/administration/upgrade.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.org/responsible-disclosure-policy/).

### Improvements

#### User Interface (UI)
 - Updated in-product help documentation to fix broken links and to correct outdated information.
 - Italian, Polish, Korean, and Ukrainian languages have been downgraded to alpha. Korean and Ukrainian are [no longer actively maintained](https://handbook.mattermost.com/contributors/join-us/localization#translation-quality).

### Bug Fixes
 - Fixed a possible panic during license validation.
 - Fixed an issue with loading of emojis in message attachment titles.
 - Fixed an issue where the timestamp in deleted messages was not correctly positioned.
 - Changed the whitespace in the refresh bar so that it always displays to the user.
 - Fixed an issue where email invites were not sent when clicking the **Next** button during onboarding.
 - Fixed an issue where clicking "View Message" in an email did not navigate to the post or remember the user's preference to "View in App".
 - Fixed an issue with the detection of certain collapsible images.
 - Prevented users from having the unreads filter enabled when the button to toggle it was not shown.
 - Fixed an issue where Mattermost's shortcut key CTRL+SHIFT+A to open the **Account Settings** clashed with Chrome's CTRL+SHIFT+A that opens a "Search Tabs" pop-up.
 - Fixed a crash when markdown images were present on the message attachments and embedded bindings.
 - Fixed an issue that kept message attachment fields unaligned.
 - Fixed an issue with right-hand side ``SuggestionList`` positioning.
 - Fixed an issue where Mattermost panicked on ``docx`` files uploaded with ``.doc`` extension.
 - Fixed a bug with the auto-responder where it would incorrectly calculate the time interval and never send the message.
 - Fixed a decoding problem for OpenID integration. The requests are now decoded against ``RawURLEncoding``.
 - Fixed various bugs for the Collapsed Reply Threads (Beta) feature, including:
   - Fixed an issue where a gap appeared between the first and second consecutive message from the same user.
   - Fixed an issue where the thread unread state would not update on websocket reconnect.
   - Fixed an issue where the main channel view root post timestamp added a horizontal scrollbar on hover.
   -  The ``ThreadAutoFollow`` setting must now be enabled in order to enable ``CollapsedThreads``.
   - Fixed issue with users re-following a previously unfollowed thread when other users replied to the thread.
   - Clicking code blocks and in-line code no longer open the associated thread.
   - Fixed an issue where two scrollbars appeared in the Threads view on high resolution monitors using zoom.
   - Fixed an issue where the quick channel switcher mention counts did not follow collapsed threads logic.
   - Fixed an issue where threads started by webhooks/integrations were being auto-followed by the webhook/integration creator when collapsed threads was enabled.
   - Fixed an issue where re-connecting to the websocket caused thread mentions to be cleared in the user interface with collapsed reply threads enabled.
   - Fixed an issue where the **New messages** line and date separators overlapped text in a thread.

### Go Version
 - v5.39 is built with Go ``1.16.7``.

### Upcoming Deprecations in Mattermost v6.0

The following deprecations are planned for the Mattermost v6.0 release, which is scheduled for 2021/10/13. This list is subject to change prior to the release.

1. [Legacy Command Line Tools](https://docs.mattermost.com/manage/command-line-tools.html). All commands have been fully replaced by [mmctl](https://docs.mattermost.com/manage/mmctl-command-line-tool.html) and new commands have been added over the last few months, making this tool a full and robust replacement. 

2. [Slack Import via the web app](https://docs.mattermost.com/onboard/migrating-to-mattermost.html#migrating-from-slack-using-the-mattermost-web-app). The Slack import tool accessible via the Team Setting menu is being replaced by the [mmetl](https://docs.mattermost.com/onboard/migrating-to-mattermost.html#migrating-from-slack-using-the-mattermost-mmetl-tool-and-bulk-import) tool that is much more comprehensive for the types of data it can assist in uploading. 

3. MySQL versions below 5.7.7. Minimum support will now be for 5.7.12. This version introduced a native JSON data type that lets us improve performance and scalability of several database fields (most notably Users and Posts props). Additionally, version 5.6 (our current minimum version) reached [EOL in February 2021](https://www.mysql.com/support/eol-notice.html).

4. Elasticsearch 5 and 6 - [versions 5.x reached EOL in March of 2019, and versions 6.x reached EOL in November 2020](https://www.elastic.co/support/eol). Our minimal supported version with Mattermost v6.0 will be Elasticsearch version 7.0.

5. Windows 7 reached [EOL in January 2020](https://support.microsoft.com/en-us/windows/windows-7-support-ended-on-january-14-2020-b75d4580-2cc7-895a-2c9c-1466d9a53962). We will no longer provide support for Mattermost Desktop App issues on Windows 7.

6. [DisableLegacyMFAEndpoint](https://docs.mattermost.com/configure/configuration-settings.html#disable-legacy-mfa-api-endpoint) configuration setting.

7. [ExperimentalTimezone](https://docs.mattermost.com/configure/configuration-settings.html#timezone) configuration setting. The config setting will be removed and the feature will be promoted to general availability.

8. All legacy channel sidebar experimental configuration settings. We encourage customers using these settings to upgrade to v5.32 or later to access [custom, collapsible channel categories](https://mattermost.com/blog/custom-collapsible-channel-categories/) among many other channel organization features. The settings being deprecated include:

   - [EnableLegacySidebar](https://docs.mattermost.com/configure/configuration-settings.html#enable-legacy-sidebar)
   - [ExperimentalTownSquareIsReadOnly](https://docs.mattermost.com/configure/configuration-settings.html#town-square-is-read-only-experimental)
   - [ExperimentalHideTownSquareinLHS](https://docs.mattermost.com/configure/configuration-settings.html#town-square-is-hidden-in-left-hand-sidebar-experimental)
   - [EnableXToLeaveChannelsFromLHS](https://docs.mattermost.com/configure/configuration-settings.html#enable-x-to-leave-channels-from-left-hand-sidebar-experimental)
   - [CloseUnusedDirectMessages](https://docs.mattermost.com/configure/configuration-settings.html#autoclose-direct-messages-in-sidebar-experimental)
   - [ExperimentalChannelOrganization](https://docs.mattermost.com/configure/configuration-settings.html#sidebar-organization)
   - [ExperimentalChannelSidebarOrganization](https://docs.mattermost.com/configure/configuration-settings.html#experimental-sidebar-features)

9. [All configuration settings previously marked as “Deprecated”](https://docs.mattermost.com/configure/configuration-settings.html#deprecated-configuration-settings).

10. Changes to ``mattermost-server/model`` for naming consistency.

### Known Issues
 - [Collapsed Reply Threads](https://docs.mattermost.com/messaging/organizing-conversations.html) is currently in beta. Before enabling the feature, please ensure you are well versed in the [known issues](https://docs.mattermost.com/messaging/organizing-conversations.html#known-issues),  particularly relating to database resource requirements and server performance implications. If you cannot easily scale up your database size, or are running the Mattermost application server and database server on the same machine, we recommended waiting to enable Collapsed Reply Threads until it is [promoted to general availability in Q1 2022](https://mattermost.com/blog/collapsed-reply-threads-ga/). Learn more about these [performance considerations here](https://support.mattermost.com/hc/en-us/articles/4413183568276).
 - Experimental timezones and custom statuses can cause an increase in CPU usage and database connections for servers with an E20 license. A current workaround is to disable custom statuses or to disable experimental timezones.
 - Adding an at-mention at the start of a post draft and pressing the leftwards or rightwards arrow can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Pinned posts are no longer highlighted [MM-34870](https://mattermost.atlassian.net/browse/MM-34870).
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.

### Contributors
 - [aaronrothschild](https://github.com/aaronrothschild), [adammorawski1](https://github.com/adammorawski1), [Adovenmuehle](https://github.com/Adovenmuehle), [aeomin](https://github.com/aeomin), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [amirmoyousefi](https://github.com/amirmoyousefi), [amyblais](https://github.com/amyblais), [amynicol1985](https://github.com/amynicol1985), [anurag6713](https://github.com/anurag6713), [arjitc](https://github.com/arjitc), [ArmanChand](https://github.com/ArmanChand), [asaadmahmood](https://github.com/asaadmahmood), [ashishbhate](https://github.com/ashishbhate), [AshishDhama](https://github.com/AshishDhama), [asimsedhain](https://github.com/asimsedhain), [aspleenic](https://github.com/aspleenic), [BenCookie95](https://github.com/BenCookie95), [BenLloydPearson](https://github.com/BenLloydPearson), [calebroseland](https://github.com/calebroseland), [chenilim](https://github.com/chenilim), [chikei](https://github.com/chikei), [chitramdasgupta](https://github.com/chitramdasgupta), [cobenash](https://github.com/cobenash), [coltoneshaw](https://github.com/coltoneshaw), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cvockrodt](https://github.com/cvockrodt), [cwarnermm](https://github.com/cwarnermm), [dbpolito](https://github.com/dbpolito), [deanwhillier](https://github.com/deanwhillier), [devinbinnie](https://github.com/devinbinnie), [DeviousLab](https://github.com/DeviousLab), [DjMagicFingers](https://github.com/DjMagicFingers), [Duaard](https://github.com/Duaard), [elyscape](https://github.com/elyscape), [emilyacook](https://github.com/emilyacook), [enahum](https://github.com/enahum), [enelson720](https://github.com/enelson720), [engineereng](https://github.com/engineereng), [ewwollesen](https://github.com/ewwollesen), [fksu](https://github.com/fksu), [flynbit](https://github.com/flynbit), [Francois-D](https://github.com/Francois-D), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gigawhitlocks](https://github.com/gigawhitlocks), [gozeloglu](https://github.com/gozeloglu), [gruceqq](https://translate.mattermost.com/user/gruceqq/), [haalcala](https://github.com/haalcala), [haardikdharma10](https://github.com/haardikdharma10), [hahmadia](https://github.com/hahmadia), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hectorskypl](https://github.com/hectorskypl), [hmhealey](https://github.com/hmhealey), [icelander](https://github.com/icelander), [iomodo](https://github.com/iomodo), [isacikgoz](https://github.com/isacikgoz), [it33](https://github.com/it33), [ivanaairenee](https://github.com/ivanaairenee), [jadrales](https://github.com/jadrales), [jamiehurewitz](https://github.com/jamiehurewitz), [jasonblais](https://github.com/jasonblais), [jayaddison-collabora](https://github.com/jayaddison-collabora), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [Johennes](https://github.com/Johennes), [johnsonbrothers](https://github.com/johnsonbrothers), [josephbaylon](https://github.com/josephbaylon), [JtheBAB](https://github.com/JtheBAB), [jufab](https://github.com/jufab), [jupenur](https://github.com/jupenur), [justinegeffen](https://github.com/justinegeffen), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kamre](https://github.com/kamre), [kayazeren](https://github.com/kayazeren), [KobeBergmans](https://github.com/KobeBergmans), [koox00](https://github.com/koox00), [krutarththakkar](https://github.com/krutarththakkar), [kscheel](https://github.com/kscheel), [larkox](https://github.com/larkox), [LauSam09](https://github.com/LauSam09), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [maisnamrajusingh](https://github.com/maisnamrajusingh), [majidsajadi](https://github.com/majidsajadi), [maliur](https://github.com/maliur), [manojmalik20](https://github.com/manojmalik20), [marianunez](https://github.com/marianunez), [mattermod](https://github.com/mattermod), [matthewbirtch](https://github.com/matthewbirtch), [matthew.williams](https://translate.mattermost.com/user/matthew-w/), [metanerd](https://github.com/metanerd), [mgdelacroix](https://github.com/mgdelacroix), [michelengelen](https://github.com/michelengelen), [mickmister](https://github.com/mickmister), [migbot](https://github.com/migbot), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [mmskv](https://github.com/mmskv), [mrckndt](https://github.com/mrckndt), [Mshahidtaj](https://github.com/Mshahidtaj), [nat-gunner](https://github.com/nat-gunner), [neallred](https://github.com/neallred), [nevyangelova](https://github.com/nevyangelova), [nikolaizah](https://github.com/nikolaizah), [Nog-Frog](https://github.com/Nog-Frog), [pablovelezvidal](https://github.com/pablovelezvidal), [Prassud](https://github.com/Prassud), [rbradleyhaas](https://github.com/rbradleyhaas), [redrru](https://github.com/redrru), [rodcorsi](https://github.com/rodcorsi), [roopakv](https://github.com/roopakv), [rrey](https://github.com/rrey), [Rutam21](https://github.com/Rutam21), [sakaitsu](https://translate.mattermost.com/user/sakaitsu/), [saturninoabril](https://github.com/saturninoabril), [Sayanta66](https://github.com/Sayanta66), [sbishel](https://github.com/sbishel), [Shahzayb](https://github.com/Shahzayb), [Shaz-25](https://github.com/Shaz-25), [sibasankarnayak](https://github.com/sibasankarnayak), [sonereker](https://github.com/sonereker), [spirosoik](https://github.com/spirosoik), [srkgupta](https://github.com/srkgupta), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [Szymongib](https://github.com/Szymongib), [talesmc](https://github.com/talesmc), [thePanz](https://github.com/thePanz), [tsabi](https://translate.mattermost.com/user/tsabi/), [VA2XJM](https://github.com/VA2XJM), [vadimasadchi](https://github.com/vadimasadchi), [vinod-demansol](https://github.com/vinod-demansol), [wget](https://github.com/wget), [WietseWind](https://github.com/WietseWind), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [yedamao](https://github.com/yedamao), [YJSoft](https://github.com/YJSoft), [zefhemel](https://github.com/zefhemel), [Ziggiz](https://github.com/Ziggiz)

## Release v5.38 - [Feature Release](https://docs.mattermost.com/administration/release-definitions.html#feature-release)

- **v5.38.4, released 2021-11-15**
  - Mattermost v5.38.4 contains a medium level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
- **v5.38.3, released 2021-10-27**
  - Mattermost v5.38.3 contains a medium level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed a race condition in telemetry IDs on High Availability servers [MM-39343](https://mattermost.atlassian.net/browse/MM-39343).
- **v5.38.2, released 2021-08-26**
  - Upgraded Go version to 1.16.7 to fix an application crash issue.
  - Fixed an issue where mmctl ``config reload`` command was missing local-mode server-side implementation. [MM-38082](https://mattermost.atlassian.net/browse/MM-38082)
- **v5.38.1, released 2021-08-18**
  - Fixed an issue where Playbooks v1.16.0 could not be installed as a pre-packaged plugin [MM-37928](https://mattermost.atlassian.net/browse/MM-37928).
- **v5.38.0, released 2021-08-16**
  - Original 5.38.0 release

Mattermost v5.38.0 contains low to medium level security fixes. [Upgrading](https://docs.mattermost.com/administration/upgrade.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.org/responsible-disclosure-policy/).

### Deprecations
 - The “config watcher” (the mechanism that automatically reloads the ``config.json`` file) has been removed in favor of the ``mmctl config reload`` command, which must be run to apply configuration changes after they are made on disk. This change improves configuration performance and robustness.

### Important Upgrade Notes
 - v5.38 adds fixes for some of the incorrect mention counts and unreads around threads and channels since the introduction of Collapsed Reply Threads (Beta). This fix is done through a SQL migration, and it may take several minutes to complete for large databases. The ``fixCRTChannelMembershipCounts`` fix takes 1 minute and 20 seconds for a database containing approximately 4 million channel memberships and about 130,000 channels. The ``fixCRTThreadCountsAndUnreads`` fix takes about 3 minutes and 30 seconds for a database containing 56367 threads, 124587 thread memberships, and 220801 channel memberships. These are on MySQL v5.6.51.
 - Focalboard v0.8.2 (released with Mattermost v5.38.0) requires Mattermost v5.37+ due to the new database connection system.

**IMPORTANT:** If you upgrade from a release earlier than v5.37, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).

### Highlights

#### Granular Data Retention Policies (Enterprise E20)
 - A ``data_retention`` type job can now be run even if the global policy is disabled. The granular (i.e. team and channel-specific) policies will be executed when the data retention job is run. Please note there is a known issue where deleted posts get displayed in channels without new activity after the retention job is run.  This issue is tracked with [this ticket](https://mattermost.atlassian.net/browse/MM-36574).

#### Enhanced User Onboarding Experience
 - To help new users get started with Mattermost, new Getting Started steps have been added to the onboarding experience. These steps help users to complete their profile, name their teams, configure desktop notifications, and invite others to join their team. Additionally, once the onboarding is complete, users are provided with helpful tips to get started with channels, plugins, and more.

#### Playbooks Updates
 - ``Incident Collaboration`` was rebranded to ``Playbooks``. Also the channel right-hand sidebar is redesigned, our own playbooks are shared as templates, and more triggers and actions were added.

#### Focalboard Updates
 - Added created-by property and improved performance with shared database connections. Focalboard 0.8.2 requires Mattermost v5.37+ due to a new database connection system.

### Improvements

#### User Interface (UI)
 - Upgraded German language back to an official language.
 - Markdown formatting is now stripped from push notifications.
 - Enabled the **Set Status** button if the custom status hasn't changed from currently set status.
 - Improved default rendering of images inserted via the GIF picker.
 - Small text changes were added to Direct and Group Message menus: **Mute channel** and **Edit Channel Header** now reads as **Mute Conversation** and **Edit Conversation Header**.

#### Performance
 - Improved performance of components that show reactions on posts.
 - Improved performance of certain components when viewing non-Direct Message channels.
 - Added minor improvements to performance of messages posted in the right-hand side.
 - Improved typing performance in affected environments by reducing the frequency in which drafts are saved.

#### Integrations
 - Added icons to apps in the Marketplace.
 - Apps can now add arbitrary markdown in between fields on forms.
 - Added support for markdown in apps forms, interactive dialogs field descriptions, errors, and slash commands.
 - Improved user and channel selector for app commands.
 - Added support for ``react-intl`` and ``<Timestamp/>`` usage in plugins.
 - Added plugin API methods for user access tokens and OAuth apps.

#### Administration
 - Added a new feature to archive and unarchive teams through **System Console** > **Teams**.

### Bug Fixes
 - Fixed an issue where the "Find channel" channel switcher text overflowed beyond the button for some languages.
 - Fixed an issue where inter-plugin requests without a body didn't work.
 - Fixed an issue with opening a dialog from an interactive message when returning an empty response.
 - Fixed an issue where the **Add Members** modal was incorrectly themed on the Mattermost Dark Theme.
 - Fixed a panic in the ``getPrevTrialLicense`` API request when loading the System Console on Team Edition.
 - Fixed an issue where admin advisor notifications were accidentally re-enabled in a previous release.
 - Fixed various bugs for the Collapsed Reply Threads (Beta) feature, including:
   - Fixed an issue where an error occurred while following a thread with no replies.
   - Fixed an issue where ``reply_count`` of 0 was always returned for GET single Post on ``/posts/<postid>`` API.
   - Fixed an issue where following a single message returned a status 500.
   - Fixed an issue where when replying in a thread after unfollowing it, the thread was not auto-followed again.
   - Fixed an issue where when enabling Collapsed Reply Threads, channels that had no new activity were showing as unread.
   - Fixed an issue with thread unreads when the feature was enabled by a user.
   - Fixed an issue where self replies were marking threads as unread.
   - Unread threads are now correctly displayed on app load for teams in the sidebar when Collapsed Reply Threads feature is enabled.
   - Fixed an issue where "Thread" in the thread viewer was displayed vertically in some languages.
   - Fixed an issue where opening global threads containing a root post markdown image crashed the app.
   - Fixed an issue where the app crashed when switching to the Threads view after leaving a channel.
   - Fixed an issue where replying to a thread from the global threads screen marked the channel as read.
   - The **Mark all as unread** button is now no longer disabled for Collapsed Reply Threads.
   - Fixed root posts not being shown as followed for the post creator after receiving the first reply that affected servers with Collapsed Reply Threads enabled and database read replicas configured.

### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:
 - Under ``PluginSettings`` in ``config.json``:
    - Added ``ChimeraOAuthProxyURL`` to allow specifying Chimera URL that can be used by plugins to connect with pre-created OAuth applications.
 - The config setting ``EnableReliableWebSockets`` now defaults to ``true``.

### API Changes
 - Added ``CreateChannelSidebarCategory``, ``GetChannelSidebarCategories`` and ``UpdateChannelSidebarCategories`` to the Plugin API.
 - Add a new Plugin API method that allows files to register dropdown menu actions.

### Go Version
 - v5.38 is built with Go ``1.16.0``.

### Open Source Components
 - Added ``classnames`` and ``react-window`` to https://github.com/mattermost/mattermost-webapp/.
 - Added ``@react-native-community/datetimepicker``, ``array.prototype.flat``, and ``base-64`` to https://github.com/mattermost/mattermost-mobile/.

### Upcoming Deprecations in Mattermost v6.0

The following deprecations are planned for the Mattermost v6.0 release, which is scheduled for 2021/10/15. This list is subject to change prior to the release.

1. [Legacy Command Line Tools](https://docs.mattermost.com/manage/command-line-tools.html). All commands have been fully replaced by [mmctl](https://docs.mattermost.com/manage/mmctl-command-line-tool.html) and new commands have been added over the last few months, making this tool a full and robust replacement. 

2. [Slack Import via the web app](https://docs.mattermost.com/onboard/migrating-to-mattermost.html#migrating-from-slack-using-the-mattermost-web-app). The Slack import tool accessible via the Team Setting menu is being replaced by the [mmetl](https://docs.mattermost.com/onboard/migrating-to-mattermost.html#migrating-from-slack-using-the-mattermost-mmetl-tool-and-bulk-import) tool that is much more comprehensive for the types of data it can assist in uploading. 

3. MySQL versions below 5.7.7. Minimum support will now be for 5.7.12. This version introduced a native JSON data type that lets us improve performance and scalability of several database fields (most notably Users and Posts props). Additionally, version 5.6 (our current minimum version) reached [EOL in February 2021](https://www.mysql.com/support/eol-notice.html).

4. Elasticsearch 5 and 6 - [versions 5.x reached EOL in March of 2019, and versions 6.x reached EOL in November 2020](https://www.elastic.co/support/eol). Our minimal supported version with Mattermost v6.0 will be Elasticsearch version 7.0.

5. Windows 7 reached [EOL in January 2020](https://support.microsoft.com/en-us/windows/windows-7-support-ended-on-january-14-2020-b75d4580-2cc7-895a-2c9c-1466d9a53962). We will no longer provide support for Mattermost Desktop App issues on Windows 7.

6. [DisableLegacyMFA](https://docs.mattermost.com/configure/configuration-settings.html#disable-legacy-mfa-api-endpoint) configuration setting.

7. [ExperimentalTimezone](https://docs.mattermost.com/configure/configuration-settings.html#timezone) configuration setting.

8. All legacy channel sidebar experimental configuration settings. We encourage customers using these settings to upgrade to v5.32 or later to access [custom, collapsible channel categories](https://mattermost.com/blog/custom-collapsible-channel-categories/) among many other channel organization features. The settings being deprecated include:

   - [EnableLegacySidebar](https://docs.mattermost.com/configure/configuration-settings.html#enable-legacy-sidebar)
   - [ExperimentalTownSquareIsReadOnly](https://docs.mattermost.com/configure/configuration-settings.html#town-square-is-read-only-experimental)
   - [ExperimentalHideTownSquareinLHS](https://docs.mattermost.com/configure/configuration-settings.html#town-square-is-hidden-in-left-hand-sidebar-experimental)
   - [EnableXToLeaveChannelsFromLHS](https://docs.mattermost.com/configure/configuration-settings.html#enable-x-to-leave-channels-from-left-hand-sidebar-experimental)
   - [CloseUnusedDirectMessages](https://docs.mattermost.com/configure/configuration-settings.html#autoclose-direct-messages-in-sidebar-experimental)
   - [ExperimentalChannelOrganization](https://docs.mattermost.com/configure/configuration-settings.html#sidebar-organization)
   - [ExperimentalChannelSidebarOrganization](https://docs.mattermost.com/configure/configuration-settings.html#experimental-sidebar-features)

9. [All configuration settings previously marked as “Deprecated”](https://docs.mattermost.com/configure/configuration-settings.html#deprecated-configuration-settings).

10. Changes to ``mattermost-server/model`` for naming consistency.

### Known Issues
 - [Collapsed Reply Threads](https://docs.mattermost.com/messaging/organizing-conversations.html) is currently in beta. Before enabling the feature, please ensure you are well versed in the [known issues](https://docs.mattermost.com/messaging/organizing-conversations.html#known-issues),  particularly relating to database resource requirements and server performance implications. If you cannot easily scale up your database size, or are running the Mattermost application server and database server on the same machine, we recommended waiting to enable Collapsed Reply Threads until it is [promoted to general availability in Q1 2022](https://mattermost.com/blog/collapsed-reply-threads-ga/). Learn more about these [performance considerations here](https://support.mattermost.com/hc/en-us/articles/4413183568276).
 - The server version for v5.38.2 for Team Edition is reported as ``5.39.2``.
 - Deleted posts get displayed in channels without new activity after the data retention job is run [MM-36574](https://mattermost.atlassian.net/browse/MM-36574).
 - Adding an at-mention at the start of a post draft and pressing the leftwards or rightwards arrow can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Emoji counter in the center channel doesn't always update immediately when a reaction is added in the right-hand side [MM-31994](https://mattermost.atlassian.net/browse/MM-31994).
 - Fields on the right column in a message attachment render unevenly [MM-36943](https://mattermost.atlassian.net/browse/MM-36943).
 - Pinned posts are no longer highlighted.
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.

### Contributors
 - [Adovenmuehle](https://github.com/Adovenmuehle), [aeomin](https://github.com/aeomin), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [ahmaddanialmohd](https://github.com/ahmaddanialmohd), [aileenpalafox](https://github.com/aileenpalafox), [amyblais](https://github.com/amyblais), [amynicol1985](https://github.com/amynicol1985), [angeloskyratzakos](https://github.com/angeloskyratzakos), [anurag6713](https://github.com/anurag6713), [arjitc](https://github.com/arjitc), [arvinDarmawan](https://github.com/arvinDarmawan), [asaadmahmood](https://github.com/asaadmahmood), [ashishbhate](https://github.com/ashishbhate), [AshishDhama](https://github.com/AshishDhama), [aspleenic](https://github.com/aspleenic), [avinashlng1080](https://github.com/avinashlng1080), [bakurits](https://github.com/bakurits), [bbodenmiller](https://github.com/bbodenmiller), [BenCookie95](https://github.com/BenCookie95), [calebroseland](https://github.com/calebroseland), [chenilim](https://github.com/chenilim), [chikei](https://github.com/chikei), [cognvn](https://github.com/cognvn), [colorfusion](https://github.com/colorfusion), [coltoneshaw](https://github.com/coltoneshaw), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [darkLord19](https://github.com/darkLord19), [deanwhillier](https://github.com/deanwhillier), [devinbinnie](https://github.com/devinbinnie), [ditsemto](https://github.com/ditsemto), [DSchalla](https://github.com/DSchalla), [enahum](https://github.com/enahum), [enelson720](https://github.com/enelson720), [engineereng](https://github.com/engineereng), [esethna](https://github.com/esethna), [evelikov](https://github.com/evelikov), [ewwollesen](https://github.com/ewwollesen), [flynbit](https://github.com/flynbit), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gbonnefille](https://github.com/gbonnefille), [gigawhitlocks](https://github.com/gigawhitlocks), [gruceqq](https://translate.mattermost.com/user/gruceqq/), [hackercat3211](https://github.com/hackercat3211), [hahmadia](https://github.com/hahmadia), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hectorskypl](https://github.com/hectorskypl), [hmhealey](https://github.com/hmhealey), [iomodo](https://github.com/iomodo), [isacikgoz](https://github.com/isacikgoz), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jayaddison-collabora](https://github.com/jayaddison-collabora), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [johnsonbrothers](https://github.com/johnsonbrothers), [josephbaylon](https://github.com/josephbaylon), [jprusch](https://github.com/jprusch), [justinegeffen](https://github.com/justinegeffen), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kamre](https://github.com/kamre), [kayazeren](https://github.com/kayazeren), [Konghuy](https://github.com/Konghuy), [koox00](https://github.com/koox00), [larkox](https://github.com/larkox), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lordinkavu](https://github.com/lordinkavu), [lynn915](https://github.com/lynn915), [madhavhugar](https://github.com/madhavhugar), [maisnamrajusingh](https://github.com/maisnamrajusingh), [majidsajadi](https://github.com/majidsajadi), [manojmalik20](https://github.com/manojmalik20), [marianunez](https://github.com/marianunez), [matthewbirtch](https://github.com/matthewbirtch), [matthew.williams](https://translate.mattermost.com/user/matthew-w/), [metanerd](https://github.com/metanerd), [mgdelacroix](https://github.com/mgdelacroix), [michaelgamble](https://github.com/michaelgamble), [michelengelen](https://github.com/michelengelen), [mickmister](https://github.com/mickmister), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [mrckndt](https://github.com/mrckndt), [Mshahidtaj](https://github.com/Mshahidtaj), [N3rdP1um23](https://github.com/N3rdP1um23), [nat-gunner](https://github.com/nat-gunner), [natalie-hub](https://github.com/natalie-hub), [neallred](https://github.com/neallred), [nevyangelova](https://github.com/nevyangelova), [nickboldt](https://github.com/nickboldt), [nickmisasi](https://github.com/nickmisasi), [nika-begiashvili](https://github.com/nika-begiashvili), [nikolaizah](https://github.com/nikolaizah), [ogi-m](https://github.com/ogi-m), [oh6hay](https://github.com/oh6hay), [pablovelezvidal](https://github.com/pablovelezvidal), [papanireal](https://github.com/papanireal), [petrmifek](https://github.com/petrmifek), [Pezhvak](https://github.com/Pezhvak), [robinmetral](https://github.com/robinmetral), [rodcorsi](https://github.com/rodcorsi), [Roy-Orbison](https://github.com/Roy-Orbison), [sakaitsu](https://translate.mattermost.com/user/sakaitsu/), [saturninoabril](https://github.com/saturninoabril), [Sayanta66](https://github.com/Sayanta66), [source-punk](https://github.com/source-punk), [stafot](https://github.com/stafot), [stevemudie](https://github.com/stevemudie), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [Szymongib](https://github.com/Szymongib), [thePanz](https://github.com/thePanz), [thierrymarianne](https://github.com/thierrymarianne), [tronginc](https://github.com/tronginc), [tsabi](https://translate.mattermost.com/user/tsabi/), [VA2XJM](https://github.com/VA2XJM), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [xlanor](https://github.com/xlanor), [xuanvi26](https://github.com/xuanvi26), [yedamao](https://github.com/yedamao), [zefhemel](https://github.com/zefhemel)

## Release v5.37 - [Extended Support Release](https://docs.mattermost.com/administration/extended-support-release.html)

- **v5.37.6, released 2021-12-17**
  - Mattermost v5.37.6 contains medium level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Added a general performance fix for loading the web application and typing.
  - Improved performance while typing by moving some autocomplete layout calculations.
  - Improved performance by reducing DOM usage during render.
  - Removed real-time updates of a couple of features to prevent overloading servers on user updates. The "This channel contains guests" indicator and the number of timezones displayed when notifying members of a group will only be updated on channel change now.
- **v5.37.5, released 2021-11-30**
  - Fixed an issue where OpenID redirect did not work when hosting Mattermost on a subdirectory [MM-40151](https://mattermost.atlassian.net/browse/MM-40151).
  - Fixed an issue where v5.37 reported an incorrect mmctl version.
- **v5.37.4, released 2021-11-15**
  - Mattermost v5.37.4 contains a medium level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed a potential panic during the message export job [MM-39521](https://mattermost.atlassian.net/browse/MM-39521).
  - Fixed some sentry crashes [MM-38565](https://mattermost.atlassian.net/browse/MM-38565), [MM-39208](https://mattermost.atlassian.net/browse/MM-39208).
  - Updated in-product help documentation to fix broken links and to correct outdated information.
- **v5.37.3, released 2021-10-27**
  - Mattermost v5.37.3 contains a medium level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Fixed a race condition in telemetry IDs on High Availability servers [MM-39343](https://mattermost.atlassian.net/browse/MM-39343).
  - Fixed import process for imports with attachments [MM-38375](https://mattermost.atlassian.net/browse/MM-38375).
  - Fixed an issue that kept message attachment fields unaligned [MM-36943](https://mattermost.atlassian.net/browse/MM-36943).
- **v5.37.2, released 2021-08-26**
  - Upgraded Go version to 1.16.7 to fix an application crash issue. 
  - Fixed a server panic issue. [MM-37574](https://mattermost.atlassian.net/browse/MM-37574)
  - Fixed an issue where saving or updating user statuses caused the logs to be filled with multiple key insertion errors. [MM-37202](https://mattermost.atlassian.net/browse/MM-37202).
  - Fixed a panic in the ``getPrevTrialLicense`` API request when loading the System Console on Team Edition. [MM-37108](https://mattermost.atlassian.net/browse/MM-37108)
  - Fixed an issue where screen readers read “user object” instead of reading the username or channel in the **Switch Channels** modal.
- **v5.37.1, released 2021-08-04**
  - Mattermost v5.37.1 contains a medium level security fix. [Upgrading](https://docs.mattermost.com/administration/upgrade.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.org/responsible-disclosure-policy/).
  - Improved typing performance in affected environments by reducing the frequency at which drafts are saved.
  - Fixed an issue in clustering where a mutex would fail to be unlocked when a timeout happened. [MM-37246](https://mattermost.atlassian.net/browse/MM-37246)
- **v5.37.0, released 2021-07-16**
  - Original 5.37.0 release

### Deprecations
 - The ``platform`` binary and “--platform” flag have been removed. If you are using the “--platform” flag or are using the ``platform`` binary directly to run the Mattermost server application via a systemd file or custom script, you will be required to use only the mattermost binary.

### Important Upgrade Notes
 - [Collapsed Reply Threads](https://mattermost.com/blog/collapsed-reply-threads-beta/) are available as beta in Mattermost Server v5.37 and later. It’s expected that you may experience bugs as we stabilize the feature. In particular, please be aware of [the known issues documented here](https://docs.mattermost.com/messaging/organizing-conversations.html#known-issues).
 - v5.37 adds support for emoji standard v13.0. If you have added a custom emoji in the past that uses one of the new system names, then that custom emoji is going to get overwritten by the system emoji. The workaround is to change the custom emoji name.
 - Parts of Incident Collaboration are now available to all Mattermost editions. As part of this update, Incident Collaboration will require a minimum server version of v5.37. To learn more about what is available in each edition, visit [our pricing page](https://mattermost.com/pricing-self-managed/).
 - Support for Mattermost Server v5.31 [Extended Support Release](https://docs.mattermost.com/administration/extended-support-release.html) will come to the end of its life cycle on October 15, 2021. Upgrading to Mattermost Server v5.37 or later is required.

**IMPORTANT:** If you upgrade from a release earlier than v5.36, please read the other [Important Upgrade Notes](https://docs.mattermost.com/administration/important-upgrade-notes.html).

### Highlights

#### Collapsed Reply Threads (Beta)
 - We're excited to give you early access to Collapsed Reply Threads (Beta). It can be enabled in the **System Console > Experimental > Collapsed Reply Threads (Beta)**. Learn more about the features and known issues in [our documentation](https://docs.mattermost.com/help/messaging/organizing-conversations.html).

#### Emoji Enhancements with Skin Tone Selection
 - Added support for emoji standard v13.0. Users now have the ability to choose various skin tones using the Mattermost emoji picker. Mobile support is included in v1.45 Mobile App release (July 16th).

#### Improved Enterprise Trial Experience (Enterprise Editions E0, E10, E20)
 - After a Self-Managed trial ends, admins can optionally contact sales or make a purchase in a single click.

#### Focalboard: Grouped Table view, New properties, and More (Beta)
 - Focalboard tables can now be grouped by a property, for example allowing you to quickly see tasks per epic or owner.

#### Incident Collaboration Updates
 - The update includes availability on all editions, playbook keyword monitoring, retrospective report, and playbook dashboard.

#### English-Australian Language Support
 - Mattermost is now available in English-Australian.

### Improvements

#### User Interface (UI)
 - In the at-mention autocomplete, the user’s nickname is no longer shown when (you) is present.
 - Updated the help text on the **Add Users** channel modal.
 - Added the ability to upload ``.jpeg`` files on Linux. Uploading ``.jpg`` files was already supported.
 - The **Channel Switcher** now displays recently viewed channels when launched.
 - Polish, German, and Italian languages were downgraded to beta as they are [no longer actively maintained](https://handbook.mattermost.com/contributors/contributors/localization#translation-quality).
 - Custom statuses can now be set to expire after common time intervals or custom selected dates and times. Mobile App support will be added in a future release.

#### Performance
 - Added some improvements to typing performance.

#### Administration
 - Improved memory performance for large image uploads, particularly PNGs with transparency.
 - Optimized the bulk import process by no longer requiring the server to write the incoming archive to the filesystem when unzipping it.
 - Added channel restore and channel privacy change endpoints to the local mode using the System bot.

### Bug Fixes
 - Fixed an issue where users were unable to set a custom status emoji via slash command. Added the logic for detecting unicode emoji and setting it as a custom status emoji via slash commands.
 - Fixed an issue where messages with fallback text were repeated.
 - Fixed an issue where a persistent unread badge showed on the **Main Menu** when **Enable Marketplace** or **Enable Plugins** was disabled.
 - Fixed an issue where sidebar icons were not aligned with the navigator area icons.
 - Fixed an issue where using CTRL+F in a **Direct Message** channel added the user ID rather than the user's name into the search field.
 - Fixed an issue where user icons were displayed at full opacity in muted channels.
 - Fixed an issue where a redundant ``user_update`` websocket event was generated for bot users.
 - Fixed an issue where a Self-Managed Enterprise Edition E20 trial could be activated more than once without contacting the Mattermost support team.

### config.json
Multiple setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Team Edition and Enterprise Edition:
 - Under ``ServiceSettings`` in ``config.json``:
    - Added ``CollapsedThreads`` to add support for Collapsed Reply Threads (Beta).

#### Database Changes
 - Removed several redundant Database indexes.

### API Changes
 - Added a new field, team_id, to the response of ``POST api/v4/groups/{group_id}/channels/{channel_id}/link`` to add a team ID to the response when linking a channel to a group.
 - Added an optional ``collapsed_threads_supported`` parameter to /channels/members/{userId}/view to indicate that the client supports collapsed threads.
 - Added an optional ``collapsed_threads_supported`` parameter to /users/{userId}/posts/{postId}/set_unread to indicate that the client supports collapsed threads.
 - Updated the webapp to pass ``collapsed_threads_supported`` parameters to the server to indicate that the webapp supports collapsed reply threads.
 - Updated the webapp to correctly mark channels and threads as unread/read when marking root and reply posts as unread/read.
 - Added a new endpoint ``GET /trial-license/prev`` for fetching last used trial license.
 - Added two new fields in ``CustomStatus`` struct and modified the APIs to validate and handle them.

### Go Version
 - v5.37 is built with Go ``1.15.5``.

### Open Source Components
 - Removed ``reselect`` from https://github.com/mattermost/mattermost-webapp/.

### Upcoming Deprecations in Mattermost v6.0

The following deprecations are planned for the Mattermost v6.0 release, which is scheduled for 2021/10/15. This list is subject to change prior to the release.

1. [Legacy Command Line Tools](https://docs.mattermost.com/administration/command-line-tools.html). All commands have been fully replaced by [mmctl](https://docs.mattermost.com/administration/mmctl-cli-tool.html) and new commands have been added over the last few months, making this tool a full and robust replacement. 

2. [Slack Import via the web app](https://docs.mattermost.com/administration/migrating.html?highlight=mmetl#migrating-from-slack-using-the-mattermost-web-app). The Slack import tool accessible via the Team Setting menu is being replaced by the [mmetl](https://docs.mattermost.com/administration/migrating.html#migrating-from-slack-using-the-mattermost-mmetl-tool-and-bulk-import) tool that is much more comprehensive for the types of data it can assist in uploading. 

3. MySQL versions below 5.7.7. Minimum support will now be for 5.7.12. This version introduced a native JSON data type that lets us improve performance and scalability of several database fields (most notably Users and Posts props). Additionally, version 5.6 (our current minimum version) reached [EOL in February 2021](https://www.mysql.com/support/eol-notice.html).

4. Elasticsearch 5 and 6 - [versions 5.x reached EOL in March of 2019, and versions 6.x reached EOL in November 2020](https://www.elastic.co/support/eol). Our minimal supported version with Mattermost v6.0 will be Elasticsearch version 7.0.

5. Windows 7 reached [EOL in January 2020](https://support.microsoft.com/en-us/windows/windows-7-support-ended-on-january-14-2020-b75d4580-2cc7-895a-2c9c-1466d9a53962). We will no longer provide support for the Desktop App issues on Windows 7.

6. [DisableLegacyMFA](https://docs.mattermost.com/configure/configuration-settings.html#disable-legacy-mfa-api-endpoint) configuration setting.

7. [ExperimentalTimezone](https://docs.mattermost.com/configure/configuration-settings.html#timezone) configuration setting.

8. All legacy channel sidebar experimental configuration settings. We encourage customers using these settings to upgrade to v5.32 or later to access [custom, collapsible channel categories](https://mattermost.com/blog/custom-collapsible-channel-categories/) among many other channel organization features. The settings being deprecated include:

   - [EnableLegacySidebar](https://docs.mattermost.com/administration/config-settings.html#enable-legacy-sidebar)
   - [ExperimentalTownSquareIsReadOnly](https://docs.mattermost.com/administration/config-settings.html#town-square-is-read-only-experimental)
   - [ExperimentalHideTownSquareinLHS](https://docs.mattermost.com/administration/config-settings.html#town-square-is-hidden-in-left-hand-sidebar-experimental)
   - [EnableXToLeaveChannelsFromLHS](https://docs.mattermost.com/administration/config-settings.html#enable-x-to-leave-channels-from-left-hand-sidebar-experimental)
   - [CloseUnusedDirectMessages](https://docs.mattermost.com/administration/config-settings.html#autoclose-direct-messages-in-sidebar-experimental)
   - [ExperimentalChannelOrganization](https://docs.mattermost.com/administration/config-settings.html#sidebar-organization)
   - [ExperimentalChannelSidebarOrganization](https://docs.mattermost.com/administration/config-settings.html#experimental-sidebar-features)

9. [All configuration settings previously marked as “Deprecated”](https://docs.mattermost.com/administration/config-settings.html#deprecated-configuration-settings).

10. Changes to ``mattermost-server/model`` for naming consistency.

### Known Issues
 - [Collapsed Reply Threads](https://docs.mattermost.com/messaging/organizing-conversations.html) is currently in beta. Before enabling the feature, please ensure you are well versed in the [known issues](https://docs.mattermost.com/messaging/organizing-conversations.html#known-issues),  particularly relating to database resource requirements and server performance implications. If you cannot easily scale up your database size, or are running the Mattermost application server and database server on the same machine, we recommended waiting to enable Collapsed Reply Threads until it is [promoted to general availability in Q1 2022](https://mattermost.com/blog/collapsed-reply-threads-ga/). Learn more about these [performance considerations here](https://support.mattermost.com/hc/en-us/articles/4413183568276).
 - When upgrading to 5.37.0, the Incident Collaboration plugin may not be automatically installed in some cases.
 - Add Members modal is incorrectly themed on the Mattermost Dark theme [MM-37220](https://mattermost.atlassian.net/browse/MM-37220).
 - ``config.json`` can reset when running the command ``systemctl restart mattermost``, and when running any commands that write to the config (e.g. ``config`` or ``plugin``) [MM-33752](https://mattermost.atlassian.net/browse/MM-33752), [MM-32390](https://mattermost.atlassian.net/browse/MM-32390).
 - Adding an at-mention at the start of a post draft and pressing the leftwards or rightwards arrow can clear the post draft and the undo history [MM-33823](https://mattermost.atlassian.net/browse/MM-33823).
 - Emoji counter in the center channel doesn't always update immediately when a reaction is added in the right-hand side [MM-31994](https://mattermost.atlassian.net/browse/MM-31994).
 - Fields on the right column in a message attachment render unevenly [MM-36943](https://mattermost.atlassian.net/browse/MM-36943).
 - Pinned posts are no longer highlighted.
 - Google login fails on the Classic mobile apps.
 - Status may sometimes get stuck as **Away** or **Offline** in High Availability mode with IP Hash turned off.
 - Searching stop words in quotation marks with Elasticsearch enabled returns more than just the searched terms.
 - The team sidebar on the desktop app does not update when channels have been read on mobile.
 - Slack import through the CLI fails if email notifications are enabled.
 - Push notifications don't always clear on iOS when running Mattermost in High Availability mode.

### Contributors
 - [aaronrothschild](https://github.com/aaronrothschild), [Aashimalik](https://github.com/Aashimalik), [Adovenmuehle](https://github.com/Adovenmuehle), [aedott](https://github.com/aedott), [aeomin](https://github.com/aeomin), [agarciamontoro](https://github.com/agarciamontoro), [AGMETEOR](https://github.com/AGMETEOR), [agnivade](https://github.com/agnivade), [ahmaddanialmohd](https://github.com/ahmaddanialmohd), [ahmadkarlam](https://github.com/ahmadkarlam), [amyblais](https://github.com/amyblais), [amynicol1985](https://github.com/amynicol1985), [angeloskyratzakos](https://github.com/angeloskyratzakos), [anurag6713](https://github.com/anurag6713), [arvinDarmawan](https://github.com/arvinDarmawan), [asaadmahmood](https://github.com/asaadmahmood), [ashishbhate](https://github.com/ashishbhate), [AshishDhama](https://github.com/AshishDhama), [aspleenic](https://github.com/aspleenic), [balan2010](https://github.com/balan2010), [BenCookie95](https://github.com/BenCookie95), [berkeka](https://github.com/berkeka), [calebroseland](https://github.com/calebroseland), [catalintomai](https://github.com/catalintomai), [cedricziel](https://github.com/cedricziel), [chenilim](https://github.com/chenilim), [chetanyakan](https://github.com/chetanyakan), [chikei](https://github.com/chikei), [cognvn](https://github.com/cognvn), [coltoneshaw](https://github.com/coltoneshaw), [cpanato](https://github.com/cpanato), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://github.com/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [danielsischy](https://github.com/danielsischy), [darkLord19](https://github.com/darkLord19), [dbpolito](https://github.com/dbpolito), [devinbinnie](https://github.com/devinbinnie), [elsiehupp](https://github.com/elsiehupp), [elyscape](https://github.com/elyscape), [emilyacook](https://github.com/emilyacook), [enahum](https://github.com/enahum), [enelson720](https://github.com/enelson720), [esethna](https://github.com/esethna), [EugenMayer](https://github.com/EugenMayer), [ewwollesen](https://github.com/ewwollesen), [flynbit](https://github.com/flynbit), [furqanmlk](https://github.com/furqanmlk), [gabrieljackson](https://github.com/gabrieljackson), [gigawhitlocks](https://github.com/gigawhitlocks), [gruceqq](https://translate.mattermost.com/user/gruceqq/), [haardikdharma10](https://github.com/haardikdharma10), [hahmadia](https://github.com/hahmadia), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hason](https://github.com/hason), [hectorskypl](https://github.com/hectorskypl), [hmhealey](https://github.com/hmhealey), [ialorro](https://github.com/ialorro), [icelander](https://github.com/icelander), [iomodo](https://github.com/iomodo), [isacikgoz](https://github.com/isacikgoz), [it33](https://github.com/it33), [itao](https://github.com/itao), [jamiehurewitz](https://github.com/jamiehurewitz), [jasonblais](https://github.com/jasonblais), [jayaddison-collabora](https://github.com/jayaddison-collabora), [jespino](https://github.com/jespino), [jfrerich](https://github.com/jfrerich), [JoelRummel](https://github.com/JoelRummel), [Johennes](https://github.com/Johennes), [johnsonbrothers](https://github.com/johnsonbrothers), [josephbaylon](https://github.com/josephbaylon), [jplda23](https://github.com/jplda23), [jprusch](https://github.com/jprusch), [jufab](https://github.com/jufab), [justinegeffen](https://github.com/justinegeffen), [jwilander](https://github.com/jwilander), [kaakaa](https://github.com/kaakaa), [kamre](https://github.com/kamre), [kayazeren](https://github.com/kayazeren), [koox00](https://github.com/koox00), [larkox](https://github.com/larkox), [levb](https://github.com/levb), [lieut-data](https://github.com/lieut-data), [lindalumitchell](https://github.com/lindalumitchell), [lynn915](https://github.com/lynn915), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [madhavhugar](https://github.com/madhavhugar), [maisnamrajusingh](https://github.com/maisnamrajusingh), [majidsajadi](https://github.com/majidsajadi), [manojmalik20](https://github.com/manojmalik20), [matheusmosca](https://github.com/matheusmosca), [matt-w99](https://github.com/matt-w99), [matthewbirtch](https://github.com/matthewbirtch), [maxerenberg](https://github.com/maxerenberg), [metanerd](https://github.com/metanerd), [mgdelacroix](https://github.com/mgdelacroix), [michelengelen](https://github.com/michelengelen), [mickmister](https://github.com/mickmister), [migbot](https://github.com/migbot), [mkraft](https://github.com/mkraft), [mlongo4290](https://github.com/mlongo4290), [moussetc](https://github.com/moussetc), [MrLemur](https://github.com/MrLemur), [msal4](https://github.com/msal4), [MusiCode1](https://github.com/MusiCode1), [naderm11](https://github.com/naderm11), [neallred](https://github.com/neallred), [nevyangelova](https://github.com/nevyangelova), [ogi-m](https://github.com/ogi-m), [pablovelezvidal](https://github.com/pablovelezvidal), [parsaakbari1209](https://github.com/parsaakbari1209), [prakharporwal](https://github.com/prakharporwal), [prathers](https://github.com/prathers), [rbradleyhaas](https://github.com/rbradleyhaas), [rodcorsi](https://github.com/rodcorsi), [rohit1101](https://github.com/rohit1101), [sadohert](https://github.com/sadohert), [sakaitsu](https://github.com/sakaitsu), [saturninoabril](https://github.com/saturninoabril), [Sayanta66](https://github.com/Sayanta66), [sbishel](https://github.com/sbishel), [senylove1403](https://github.com/senylove1403), [srkgupta](https://github.com/srkgupta), [stafot](https://github.com/stafot), [streamer45](https://github.com/streamer45), [stylianosrigas](https://github.com/stylianosrigas), [Szymongib](https://github.com/Szymongib), [teresa-novoa](https://github.com/teresa-novoa), [thePanz](https://github.com/thePanz), [tsabi](https://translate.mattermost.com/user/tsabi), [txeli](https://github.com/txeli), [wget](https://github.com/wget), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [yulyanaR](https://github.com/yulyanaR)

