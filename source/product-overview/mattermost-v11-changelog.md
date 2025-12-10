# v11 Changelog

```{eval-rst}
.. meta::
  :page_title: Mattermost Server v11 Release Notes
```

```{Important}
```{include} common-esr-support-upgrade.md
```

(release-v11.2-feature-release)=
## Release v11.2 - [Feature Release](https://docs.mattermost.com/product-overview/release-policy.html#release-types)

**Release day: 2025-12-16**

### Upgrade Impact

#### Database Schema Changes
 - Added a new column to the ``OAuthApps`` table called ``isdynamicallyregistered``. It has a default value of ``false``. Also added three new columns to the ``OAuthAuthData`` table called ``resource``, ``codechallenge`` and ``codechallengemethod``. All columns default to ``‘’``. Also added a new column to the ``OAuthAccessData`` table called ``audience``. It has a default value of ``‘’``. No database downtime is expected for this upgrade. See the [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) for more details.

#### config.json
New setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.
 - **Changes to Enterprise plans:**
   - Under ``ServiceSettings`` in ``config.json``, added ``EnableDynamicClientRegistration`` configuration setting to control whether Dynamic Client Registration is enabled in your Mattermost instance. The default value is ``false``.

```{Important}
If you upgrade from a release earlier than v11.1, please read the other [Important Upgrade Notes](https://docs.mattermost.com/administration-guide/upgrade/important-upgrade-notes.html). In case of an upgrade failure, please check the [Downgrade Guide](https://docs.mattermost.com/administration-guide/upgrade/downgrading-mattermost-server.html) and the [Recovery Guide](https://docs.mattermost.com/deployment-guide/backup-disaster-recovery.html) for rollback steps and interim mitigation strategy.
```

### Improvements

#### User Interface (UI)
 - Pre-packaged Playbooks plugin [v2.6.1](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v2.6.1).
 - Pre-packaged Zoom plugin [v1.10.0](https://github.com/mattermost/mattermost-plugin-zoom/releases/tag/v1.10.0).
 - Pre-packaged Agents plugin [v1.6.2](https://github.com/mattermost/mattermost-plugin-agents/releases/tag/v1.6.2).
 - Pre-packaged ServiceNow plugin [v2.4.0](https://github.com/mattermost/mattermost-plugin-servicenow/releases/tag/v2.4.0).
 - Pre-packaged MS Calendar plugin [v1.4.0](https://github.com/mattermost/mattermost-plugin-mscalendar/releases/tag/v1.4.0).
 - Pre-packaged Channel Export plugin [v1.3.0](https://github.com/mattermost/mattermost-plugin-channel-export/releases/tag/v1.3.0).
 - Pre-packaged Boards plugin version [v9.2.1](https://github.com/mattermost/mattermost-plugin-boards/releases).
 - Pre-packaged Jira plugin version [v4.4.1](https://github.com/mattermost/mattermost-plugin-jira/releases/tag/v4.4.1).
 - Enabled thread popouts in the browser.
 - Reduced the channel banner height.
 - Improved license and plan name clarity throughout the user interface. License settings and the **About** modal now display specific plan names (Professional, Enterprise, Entry) instead of the generic "Enterprise Edition" label, reducing confusion between edition and plan terminology.

#### Administration
 - Introduced authentication token generation for Hosted Push Notification Service.
 - Added search backend type to the Support Packet.
 - Added SAML provider type to the Support Packet.

#### Integrations
 - Permission schemes now fully expose controls for managing other users' integrations (Webhooks, Slash Commands, OAuth Apps) in the **System Console** for greater administrative clarity. Additionally, permissions for managing your own integrations have been renamed for consistency, and a new configuration option allows administrators to enforce Incoming Webhook channel locking.
 - Added AI-enabled rewriting of messages for servers with the Agents plugin.
 - Applicable posts are now marked as AI-generated.
 - Added an authorization metadata endpoint and [Dynamic Client Registration of Confidential OAuth Apps](https://docs.mattermost.com/administration-guide/configure/integrations-configuration-settings.html#enable-dynamic-client-registration).
 - Added OAuth public client support through DCR and PKCE for public/confidential clients.
 - Added support for a resource parameter with OAuth.
 - Added ability to create OAuth public clients through the **Integrations** page.
 - Added ``http.Flusher`` support to the plugin RPC layer.

### Bug Fixes
 - Fixed a server panic that could occur when patching channel moderations with restricted permissions.
 - Fixed the justification of sidebar icons for plugins.
 - Fixed an issue with the translation of "Until <time>" text for custom statuses.
 - Fixed an issue where guest users could not log in via SAML when "Ignore Guest Users when Synchronizing with AD/LDAP" was enabled.
 - Fixed an issue where length validation was missing for LDAP user fields.
 - Fixed an issue where some modals would appear when editing messages.
 - Fixed an issue where the slash command autocomplete did not preserve user input case when forwarding pretext to backend.
 - Fixed an issue where some text on the signup page was not translatable.
 - Fixed an issue where thread popouts did not show the current user's status.
 - Fixed an issue where clicking on a permalink to a reply in another thread would not navigate the main window.
 - Fixed an issue where focusing on the thread popout would not mark the thread as read.
 - Fixed an issue where a content reviewer could not download file attachments from a flagged post.
 - Fixed an issue where users could not add bots without an error message popping up.
 - Fixed an issue displaying custom emojis in thread popouts.

### API Changes
 - Added a new ``api/v4/posts/rewrite`` endpoint to enable AI-powered message rewriting. It accepts a message, an AI agent ID, and a rewrite action, and returns a JSON object with a ``rewritten_text`` field containing the rewritten text. The endpoint supports six predefined actions: ``shorten``, ``elaborate``, ``improve_writing``, ``fix_spelling``, ``simplify``, and ``summarize``. A custom action is also available, which requires a ``custom_prompt`` parameter to specify the desired transformation.
 - Updated the ``GetFile``  ``GET`` ``api/v4/files/file_id`` endpoint to include two new query params: ``as_content_reviewer`` and ``flagged_post_id``. These are used for the Data Spillage feature to allow content reviewers to download files from flagged posts.
 - Added two new fields to the ``/oauth/authorize`` endpoints called ``code_challenge`` and ``code_challenge_method`` in order to support PKCE with our OAuth authorization flow.
 - Added ``/.well-known/oauth-authorization-server`` so that OAuth clients can check what Mattermost supports. The endpoint returns a 501 error if ``ServiceSettings.EnableOAuthServiceProvider`` is disabled.
 - Added ``/api/v4/oauth/apps/register`` in order to support Dynamic Client Registration for OAuth. This allows **any** external OAuth client to automatically register an OAuth App within Mattermost without requiring authentication. The endpoint requires ``ServiceSettings.EnableOAuthServiceProvider`` and ``ServiceSettings.EnableDynamicClientRegistration`` to be enabled.
 - Introduced ``GET /api/v4/agents`` and ``GET /api/v4/llmservices`` to allow authenticated clients to fetch available agents and LLM services.

### Audit Log Event Changes
 - Added new ``AuditEventRegisterOAuthClient``.

### Go Version
 - v11.2 is built with Go ``v1.24.6``.

### Contributors
 - [abbas-dependable-naqvi](https://github.com/abbas-dependable-naqvi), [agarciamontoro](https://github.com/agarciamontoro), [amyblais](https://github.com/amyblais), [andrleite](https://github.com/andrleite), [Arusekk](https://github.com/Arusekk), [asaadmahmood](https://github.com/asaadmahmood), [AurelienS](https://github.com/AurelienS), [BenCookie95](https://github.com/BenCookie95), [bgardner8008](https://github.com/bgardner8008), [calebroseland](https://github.com/calebroseland), [carlisgg](https://github.com/carlisgg), [catenacyber](https://github.com/catenacyber), [coltoneshaw](https://github.com/coltoneshaw), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [David](https://translate.mattermost.com/user/David), [davidkrauser](https://github.com/davidkrauser), [devinbinnie](https://github.com/devinbinnie), [DHaussermann](https://github.com/DHaussermann), [domibarton](https://github.com/domibarton), [efemonge](https://translate.mattermost.com/user/efemonge), [enahum](https://github.com/enahum), [enzowritescode](https://github.com/enzowritescode), [esarafianou](https://github.com/esarafianou), [evituzas](https://translate.mattermost.com/user/evituzas), [ferdymercury](https://github.com/ferdymercury), [feyzaozcann](https://github.com/feyzaozcann), [fmartingr](https://github.com/fmartingr), [frankps](https://translate.mattermost.com/user/frankps), [guenjun](https://translate.mattermost.com/user/guenjun), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [helloinah](https://translate.mattermost.com/user/helloinah), [hmhealey](https://github.com/hmhealey), [iamleson98](https://translate.mattermost.com/user/iamleson98), [isacikgoz](https://github.com/isacikgoz), [itz-Me-Pj](https://github.com/itz-Me-Pj), [j0taD](https://translate.mattermost.com/user/j0taD), [jgheithcock](https://github.com/jgheithcock), [jprusch](https://github.com/jprusch), [JulienTant](https://github.com/JulienTant), [kaakaa](https://translate.mattermost.com/user/kaakaa), [kayazeren](https://translate.mattermost.com/user/kayazeren), [KuSh](https://github.com/KuSh), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo), [mansil](https://translate.mattermost.com/user/mansil), [marianunez](https://github.com/marianunez), [master7](https://translate.mattermost.com/user/master7), [matthewbirtch](https://github.com/matthewbirtch), [mgdelacroix](https://github.com/mgdelacroix), [Morgan_svk](https://translate.mattermost.com/user/Morgan_svk), [mrckndt](https://github.com/mrckndt), [nevyangelova](https://github.com/nevyangelova), [nickmisasi](https://github.com/nickmisasi), [oberleg](https://translate.mattermost.com/user/oberleg), [pvev](https://github.com/pvev), [quarac](https://translate.mattermost.com/user/quarac), [rahimrahman](https://github.com/rahimrahman), [Rajat-Dabade](https://github.com/Rajat-Dabade), [Reinkard](https://github.com/Reinkard), [RS-labhub](https://github.com/RS-labhub), [sadohert](https://github.com/sadohert), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [Sharuru](https://translate.mattermost.com/user/Sharuru), [svelle](https://github.com/svelle), [TimTin](https://translate.mattermost.com/user/TimTin), [tsakmas](https://translate.mattermost.com/user/tsakmas), [tuladhar](https://github.com/tuladhar), [uright](https://github.com/uright), [vpecinka](https://github.com/vpecinka), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [willypuzzle](https://github.com/willypuzzle), [wooki-00](https://translate.mattermost.com/user/wooki-00), [yasserfaraazkhan](https://github.com/yasserfaraazkhan), [zlv](https://github.com/zlv)

(release-v11.1-feature-release)=
## Release v11.1 - [Feature Release](https://docs.mattermost.com/product-overview/release-policy.html#release-types)

- **11.1.1, released 2025-11-21**
 ```{Attention}
 **Critical Fixes**
  - Mattermost v11.1.1 contains a Critical severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release as soon as possible is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
 ```
  - Pre-packaged Jira plugin version [v4.4.1](https://github.com/mattermost/mattermost-plugin-jira/releases/tag/v4.4.1).
  - Fixed an issue where thread popouts did not show the current user's status [MM-66586](https://mattermost.atlassian.net/browse/MM-66586).
  - Fixed an issue where clicking on a permalink to a reply in another thread would not navigate the main window [MM-66614](https://mattermost.atlassian.net/browse/MM-66614).
  - Fixed an issue where users could not add bots without an error message popping up [MM-66684](https://mattermost.atlassian.net/browse/MM-66684).
  - Mattermost v11.1.1 contains no database or functional changes.
- **11.1.0, released 2025-11-14**
  - Original 11.1.0 release.

```{Attention}
**Breaking Changes**
 - The version of React used by the Mattermost web app has been updated from React 17 to React 18. See more details in [this forum post](https://forum.mattermost.com/t/upgrading-the-mattermost-web-app-to-react-18-v11/25000).
```

### Compatibility
 - Updated minimum required Edge, Firefox and Chrome versions to v140+ and updated minimum supported Windows version to v11+.

### Important Upgrade Notes
 - Added three new tables, ``ContentFlaggingCommonReviewers``, ``ContentFlaggingTeamSettings``, and ``ContentFlaggingTeamReviewers`` for storing Data Spillage settings. Added an index on ``ContentFlaggingTeamReviewers`` table to optimize fetching the team settings.  No database downtime is expected for this upgrade. See the [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) for more details.

```{Important}
If you upgrade from a release earlier than v11.0, please read the other [Important Upgrade Notes](https://docs.mattermost.com/administration-guide/upgrade/important-upgrade-notes.html).
```

### Improvements

#### User Interface (UI)
 - Pre-packaged Agents plugin version [v1.4.0](https://github.com/mattermost/mattermost-plugin-agents/releases/tag/v1.4.0).
 - Pre-packaged Playbooks plugin version [v2.5.1](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v2.5.1).
 - Pre-packaged GitLab plugin version [v1.11.0](https://github.com/mattermost/mattermost-plugin-gitlab/releases/tag/v1.11.0).
 - Pre-packaged Jira plugin version [v4.4.0](https://github.com/mattermost/mattermost-plugin-jira/releases/tag/v4.4.0).
 - Pre-packaged GitHub plugin version [v2.5.0](https://github.com/mattermost/mattermost-plugin-github/releases/tag/v2.5.0).
 - Pre-packaged Boards plugin version [v9.1.7](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.1.7).
 - Pre-packaged MS Teams Meetings plugin version [v2.3.0](https://github.com/mattermost/mattermost-plugin-msteams-meetings/releases/tag/v2.3.0).
 - Pre-packaged Calls plugin version [v1.11.0](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v1.11.0).
 - Removed Mattermost MS Teams Sync plugin from pre-packaged plugins.
 - Added support for standalone windows pop-out. Threads can now be popped out to its own window in Desktop. 
 - The desktop app version is now shown on the **About** modal, allowing clicking to copy both the server and desktop app versions.
 - Downgraded French language support from Beta to Alpha.

#### Administration
 - Added the ability to edit User Attributes in **System Console > Users > User Configuration**.

#### Integrations
 - Added ``Date`` and ``DateTime`` types for interactive dialogs.
 - Added ``MultiForm`` and ``Element`` refresh support for interactive dialogs.

### Bug Fixes
 - Fixed an issue where email address verification for SAML/LDAP users was required when a user’s email address changed.
 - Fixed an issue where users could still message each other when not sharing a team, despite the configuration setting stating otherwise.
 - Fixed an issue with the mmctl system status to return non-zero exit codes when health checks fail, ensuring proper integration with container orchestration health check systems.
 - Fixed a configuration retention issue where even active configuration got deleted.
 - Fixed an issue where plugins could not receive 3rd-party authorization headers.

### config.json
New setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to Enterprise Advanced plan: 
 - Added a new ``AutoTranslationSettings`` configuration settings section. The auto-translation feature will be available in a future release.

### API Changes
 - Added a new API endpoint ``POST /api/v4/groups/names``.
 - Added a ``since`` parameter to the property value search method of the ``PluginApi``.

### Audit Log Event Changes
 - Added ``AuditEventFlagPost``, ``AuditEventGetFlaggedPost``, ``AuditEventPermanentlyRemoveFlaggedPost``, ``AuditEventKeepFlaggedPost``, ``AuditEventUpdateContentFlaggingConfig``, and ``AuditEventSetReviewer``.

### Go Version
 - v11.1 is built with Go ``v1.24.6``.

### Open Source Components
 - Added ``@redux-devtools/extension`` and ``@types/react-is``, and removed ``react-intl`` from https://github.com/mattermost/mattermost/.

### Contributors
 - [abbas-dependable-naqvi](https://github.com/abbas-dependable-naqvi), [abhijit-singh](https://github.com/abhijit-singh), [agarciamontoro](https://github.com/agarciamontoro), [amyblais](https://github.com/amyblais), [andrleite](https://github.com/andrleite), [Arusekk](https://translate.mattermost.com/user/Arusekk), [asaadmahmood](https://github.com/asaadmahmood), [BenCookie95](https://github.com/BenCookie95), [bgardner8008](https://github.com/bgardner8008), [buzzyboy](https://github.com/buzzyboy), [calebroseland](https://github.com/calebroseland), [codiphile](https://github.com/codiphile), [cpoile](https://github.com/cpoile), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [davidkrauser](https://github.com/davidkrauser), [devinbinnie](https://github.com/devinbinnie), [DHaussermann](https://github.com/DHaussermann), [enahum](https://github.com/enahum), [enzowritescode](https://github.com/enzowritescode), [esarafianou](https://github.com/esarafianou), [esethna](https://github.com/esethna), [ewwollesen](https://github.com/ewwollesen), [fmartingr](https://github.com/fmartingr), [franklinferre](https://translate.mattermost.com/user/franklinferre), [frankps](https://translate.mattermost.com/user/frankps), [fsilye](https://github.com/fsilye), [grubbins](https://github.com/grubbins), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hereje](https://github.com/hereje), [hmhealey](https://github.com/hmhealey), [homerCOD](https://github.com/homerCOD), [isacikgoz](https://github.com/isacikgoz), [itz-Me-Pj](https://github.com/itz-Me-Pj), [iyampaul](https://github.com/iyampaul), [jgheithcock](https://github.com/jgheithcock), [johnsonbrothers](https://github.com/johnsonbrothers), [jprusch](https://github.com/jprusch), [jsedy7](https://translate.mattermost.com/user/jsedy7), [JulienTant](https://github.com/JulienTant), [kaakaa](https://github.com/kaakaa), [kayazeren](https://github.com/kayazeren), [KohheiAdachi](https://github.com/KohheiAdachi), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [l-ra](https://github.com/l-ra), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [lindy65](https://github.com/lindy65), [lynn915](https://github.com/lynn915), [majo](https://translate.mattermost.com/user/majo), [mansil](https://github.com/mansil), [marianunez](https://github.com/marianunez), [master7](https://translate.mattermost.com/user/master7), [matt-w99](https://github.com/matt-w99), [matthew-w](https://translate.mattermost.com/user/matthew-w), [matthewbirtch](https://github.com/matthewbirtch), [mental-space1532](https://translate.mattermost.com/user/mental-space1532), [mgdelacroix](https://github.com/mgdelacroix), [moi90](https://github.com/moi90), [neflyte](https://github.com/neflyte), [nickmisasi](https://github.com/nickmisasi), [Omar8345](https://github.com/Omar8345), [pavelzeman](https://github.com/pavelzeman), [pnaskardev](https://github.com/pnaskardev), [polyacedev](https://translate.mattermost.com/user/polyacedev), [pvev](https://github.com/pvev), [rahimrahman](https://github.com/rahimrahman), [Rajat-Dabade](https://github.com/Rajat-Dabade), [Reinkard](https://github.com/Reinkard), [roberson-io](https://github.com/roberson-io), [roskee](https://github.com/roskee), [saturninoabril](https://github.com/saturninoabril), [sbishel](https://github.com/sbishel), [Sharuru](https://translate.mattermost.com/user/Sharuru), [shawnaym](https://github.com/shawnaym), [svelle](https://github.com/svelle), [thejoeejoee](https://translate.mattermost.com/user/thejoeejoee), [ThrRip](https://github.com/ThrRip), [tnir](https://github.com/tnir), [Victor-Nyagudi](https://github.com/Victor-Nyagudi), [vpecinka](https://translate.mattermost.com/user/vpecinka), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [yairsz](https://github.com/yairsz), [Yash-Chakerverti](https://github.com/Yash-Chakerverti), [yasserfaraazkhan](https://github.com/yasserfaraazkhan)

(release-v11.0-major-release)=
## Release v11.0 - [Major Release](https://docs.mattermost.com/product-overview/release-policy.html#release-types)

- **11.0.6, released 2025-11-21**
 ```{Attention}
 **Critical Fixes**
  - Mattermost v11.0.6 contains a Critical severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release as soon as possible is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
 ```
  - Pre-packaged Jira plugin version [v4.4.1](https://github.com/mattermost/mattermost-plugin-jira/releases/tag/v4.4.1).
  - Mattermost v11.0.6 contains no database or functional changes.
- **11.0.5, released 2025-11-17**
  - Mattermost v11.0.5 contains medium severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged MS Teams Meetings plugin version [v2.3.0](https://github.com/mattermost/mattermost-plugin-msteams-meetings/releases/tag/v2.3.0).
  - Pre-packaged Calls plugin version [v1.11.0](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v1.11.0).
  - Fixed a configuration retention issue where even active configuration got deleted [MM-66216](https://mattermost.atlassian.net/browse/MM-66216).
  - Fixed an issue where plugins could not receive 3rd-party authorization headers [MM-66335](https://mattermost.atlassian.net/browse/MM-66335).
  - Mattermost v11.0.5 contains no database or functional changes.
- **11.0.4, released 2025-10-28**
 ```{Attention}
 **Critical Fixes**
  - Mattermost v11.0.4 contains Critical severity level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release as soon as possible is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
 ```
  - Fixed an issue where plugin configuration settings were incorrectly sanitized, causing API endpoints and plugins to receive masked values instead of actual configuration values.
  - Pre-packaged Boards plugin [v9.1.7](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.1.7).
  - Mattermost v11.0.4 contains no database or functional changes.
- **11.0.3, released 2025-10-27**
  - Mattermost v11.0.3 contains no database or functional changes.
- **11.0.2, released 2025-10-16**
  - Reverted a breaking change related to ``ServiceSettings.ExperimentalStrictCSRFEnforcement`` setting.
- **11.0.1, released 2025-10-16**
  - Original 11.0.1 release.

```{Attention}
**Breaking Changes**
 - GitLab SSO has been deprecated from Team Edition. Deployments using GitLab SSO can remain on v10.11 ESR (with 12 months of security updates), transition to our new free offering Mattermost Entry, or can explore commercial/nonprofit options. See more details in [this forum post](https://forum.mattermost.com/t/mattermost-v11-changes-in-free-offerings/25126). 
 - The ``TeamSettings.ExperimentalViewArchivedChannels`` setting has been deprecated. Archived channels will always be accessible, subject to normal channel membership. The server will fail to start if this setting is set to ``false``. To deny access to archived channels, mark them as private and remove affected channel members. See more details in [this forum post](https://forum.mattermost.com/t/viewing-accessing-archived-channels-v11/22626).
 - Playbooks has been deprecated from Team Edition. Entry, Professional, Enterprise, and Enterprise Advanced plans are automatically upgraded to Playbooks v2 with no expected downtime. See more details in [this forum post](https://forum.mattermost.com/t/clarification-and-update-on-the-playbooks-plugin-v11/25192).
 - Experimental Bleve Search functionality has been retired. If Bleve is enabled, search will not work until ``DisableDatabaseSearch`` is set to ``false``. See more details in [this forum post](https://forum.mattermost.com/t/transitioning-from-bleve-search-in-mattermost-v11/22982).
 - Support for MySQL has ended. Our [Migration Guide](https://docs.mattermost.com/deployment-guide/postgres-migration.html) outlines the steps, tools and support available for migrating to PostgreSQL. See more details in [this forum post](https://forum.mattermost.com/t/transition-to-postgresql/19551).
 - The ``registerPostDropdownMenuComponent`` hook in the web app’s plugin API has been removed in favour of ``registerPostDropdownMenuAction``. See more details in [this forum post](https://forum.mattermost.com/t/deprecating-a-post-dropdown-menu-component-plugin-api-v11/25001).
 - The web app is no longer exposing the [Styled Components](https://styled-components.com/) dependency for use by web app plugins. See more details in [this forum post](https://forum.mattermost.com/t/removing-styled-components-export-for-web-app-plugins-v11/25002).
 - Omnibus support has been deprecated. The last ``mattermost-omnibus`` release was v10.12. See more details in [this forum post](https://forum.mattermost.com/t/mattermost-omnibus-to-reach-end-of-life-v11/25175).
 - Deprecated ``include_removed_members`` option in ``api/v4/ldap/sync`` has been removed. Admins can use the LDAP setting ``ReAddRemovedMembers``.
 - Customers that have the NPS plugin enabled can remove it as it no longer sends the feedback over through telemetry.
 - Format query parameter requirement in the ``/api/v4/config/client`` endpoint has been deprecated.
 - Removed deprecated mmctl commands and flags:
    - ``channel add`` - use ``channel users add``
    - ``channel remove`` - use ``channel users remove``
    - ``channel restore`` - use ``channel unarchive``
    - ``channel make-private`` - use ``channel modify --private``
    - ``command delete`` - use ``command archive``
    - ``permissions show`` - use ``permissions role show``
    - ``mmctl user email`` - use ``mmctl user edit email`` 
    - ``mmctl user username`` - use ``mmctl user edit username``
 - Experimental certificate-based authentication feature has been removed. ``ExperimentalSettings.ClientSideCertEnable`` must be ``false`` to start the server.
 - Added logic to migrate the password hashing method from bcrypt to PBKDF2. The migration will happen progressively, migrating the password of a user as soon as they enter it; e.g. when logging in or when double-checking their password for any sensitive action. There is an edge case where users might get locked out of their account: if a server upgrades to v11 and user A logs in (i.e., they need to enter their password), and then the server downgrades to v10.12 or previous, user A will no longer be able to log in. In this case, admins will need to manually reset the password of such users, through the system console or through the [mmctl user reset-password [users]](https://docs.mattermost.com/administration-guide/manage/mmctl-command-line-tool.html#mmctl-user-reset-password) command. The new password hashing method is more CPU-intensive. Admins of servers with password-based login should monitor the performance on periods where many users log in at the same time.
 - ``/api/v4/teams/{team_id}/channels/search_archived`` has been deprecated in favour of ``/api/v4/channels/search`` with the deleted parameter.
 - Changed default database connection pool settings: changed ``MaxOpenConns`` from 300 to 100 and ``MaxIdleConns`` from 20 to 50, establishing a healthier 2:1 ratio for better database connection management.
 - Separate notification log file has been deprecated. If admins want to continue using a separate log file for notification logs, they can use the ``AdvancedLoggingJSON`` configuration. See the [Important Upgrade Notes](https://docs.mattermost.com/administration-guide/upgrade/important-upgrade-notes.html) for an example configuration.
 - Stopped supporting manually installed plugins as per https://forum.mattermost.com/t/deprecation-notice-manual-plugin-deployment/21192
 - Support for PostgreSQL v13 has been removed. The new minimum PostgreSQL version is v14+. See the [minimum supported PostgreSQL version policy](https://docs.mattermost.com/deployment-guide/software-hardware-requirements.html#minimum-postgresql-database-support-policy) documentation for details.
```

```{Important}
If you upgrade from a release earlier than v10.10, please read the other [Important Upgrade Notes](https://docs.mattermost.com/administration-guide/upgrade/important-upgrade-notes.html).
```

### Improvements

#### User Interface (UI)
 - Pre-packaged Agents plugin [v1.3.1](https://github.com/mattermost/mattermost-plugin-agents/releases/tag/v1.3.1).
 - Pre-packaged Boards plugin [v9.1.6](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.1.6).
 - Pre-packaged MS Teams plugin [v2.2.2](https://github.com/mattermost/mattermost-plugin-msteams/releases/tag/v2.2.2).
 - Pre-packaged Playbooks plugin [v2.4.2](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v2.4.2), allowing Professional licenses to use playbooks v2.
 - Removed Playbooks v1 from pre-packaged plugins.
 - Updated the library used for customizing scrollbars.
 - Increased page size when retrieving posts in channels with high number of hidden messages.

#### Administration
 - Introduced support for Mattermost Entry, a commercial evaluation environment to explore Enterprise Advanced with usage limits. See more details in [this forum post](https://forum.mattermost.com/t/mattermost-v11-changes-in-free-offerings/25126).
 - User limits were lowered to final threshold of 250 for Mattermost Team Edition (MIT-Compiled License).
 - Added support for a [FIPS-compliant Mattermost image](https://docs.mattermost.com/deployment-guide/server/deploy-containers.html).
 - PBKDF2 is now used as the new key derivation algorithm for remote cluster invitations. We do this in a backward compatible way such that invitations generated from new/old clusters work in all clusters.
 - Updated the default SAML signature algorithm from SHA1 to SHA256 for improved security.
 - Added admin-managed property fields to Custom Profile Attributes.
 - Admin managed Custom Profile Attribute fields can now be used as part of Attribute Based Access Control policies.
 - System Admins can now mark Custom Profile Attribute fields as “admin managed” from the System Console.
 - Added Channel-Level Attribute-Based Access Control (Available only in Enterprise Advanced). Channel Admins can now configure attribute-based access rules directly in Channel Settings through a new Access Control tab when the ``EnableChannelScopeAccessControl`` setting is enabled.
 - Channel access control policies now support multiple parent inheritances.
 - Updated interactive dialogs to use the apps form framework. Implemented dynamic select and multi-select for interactive dialogs. Also, ``UserId`` and ``TeamId`` are now passed in interactive dialog submissions.
 - Mattermost profile image is now deleted when LDAP profile picture is deleted.
 - User ``auth_data`` is now shown in the System Console user details page.
 - Added Elasticsearch test to Support Packet diagnostics.
 - Added support for a new ``EmailNotificationWillBeSent`` plugin hook.
 - Added a console warning when a plugin uses the now-deprecated ``registerPostDropdownMenuComponent`` API.

#### mmctl
 - Added ``mmctl user edit`` command.
 - Updated mmctl shell completion to fully support zsh, powershell, and fish. Check out ``mmctl completion`` for a guide on how to set it up for your shell.
 - Added the ``mmctl cpa`` set of commands to manage Custom Profile Attributes.

### Bug Fixes
 - Fixed an issue where extra date separators were added in search results, pinned posts and saved messages.
 - Fixed an issue where MFA warning was thrown in the logs for unauthenticated plugin requests.
 - Fixed an issue that prevented new users from searching channels right after joining a team when Elasticsearch was enabled.
 - Fixed some crashes in the threads screen.

### config.json
New setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
 - Under ``CloudSettings`` in ``config.json``:
     - Added ``PreviewModalBucketURL``.
 - Removed ``VerboseDiagnostics`` configuration setting as part of removing all telemetry support from Mattermost.
 - Removed ``BleveSettings`` configuration setting as part of removing Bleve.
 - Removed ``NotificationLogSettings`` as part of deprecating the separate notification log file.

#### Changes to Enterprise and Enterprise Advanced plans: 
 - Removed ``ClientSideCertCheck`` as part of removing the experimental certificate-based authentication feature.

### API Changes
 - Added a counting plugin API for properties.
 - Added a new API endpoint to update Custom Profile Attribute values for a given user.

### Go Version
 - v11.0 is built with Go ``v1.24.6``.

### Open Source Components
 - Added ``simplebar-react``, and removed ``go-sql-driver/mysql``, ``blevesearch/bleve`` and ``axios`` from https://github.com/mattermost/mattermost/. 

### Contributors
 - [abbas-dependable-naqvi](https://github.com/abbas-dependable-naqvi), [adityadav1987](https://github.com/adityadav1987), [agarciamontoro](https://github.com/agarciamontoro), [amyblais](https://github.com/amyblais), [andrleite](https://github.com/andrleite), [angeloskyratzakos](https://github.com/angeloskyratzakos), [arush-vashishtha](https://github.com/arush-vashishtha), [AulakhHarsh](https://github.com/AulakhHarsh), [AurelienS](https://github.com/AurelienS), [avasconcelos114](https://github.com/avasconcelos114), [azistellar](https://translate.mattermost.com/user/azistellar), [azizthegit](https://github.com/azizthegit), [BenCookie95](https://github.com/BenCookie95), [bndn](https://github.com/bndn), [Boruus](https://translate.mattermost.com/user/Boruus), [bshumylo](https://translate.mattermost.com/user/bshumylo), [buzzyboy](https://github.com/buzzyboy), [calebroseland](https://github.com/calebroseland), [catalintomai](https://github.com/catalintomai), [crspeller](https://github.com/crspeller), [ctlaltdieliet](https://translate.mattermost.com/user/ctlaltdieliet), [cwarnermm](https://github.com/cwarnermm), [danilvalov](https://github.com/danilvalov), [David](https://translate.mattermost.com/user/David), [davidkrauser](https://github.com/davidkrauser), [devinbinnie](https://github.com/devinbinnie), [eagerid](https://github.com/eagerid), [enahum](https://github.com/enahum), [enzowritescode](https://github.com/enzowritescode), [esarafianou](https://github.com/esarafianou), [esethna](https://github.com/esethna), [flyply](https://translate.mattermost.com/user/flyply), [fmartingr](https://github.com/fmartingr), [frankps](https://translate.mattermost.com/user/frankps), [fsilye](https://github.com/fsilye), [gabrieljackson](https://github.com/gabrieljackson), [grubbins](https://github.com/grubbins), [guenjun](https://github.com/guenjun), [hanzei](https://github.com/hanzei), [harshilsharma63](https://github.com/harshilsharma63), [hmhealey](https://github.com/hmhealey), [isacikgoz](https://github.com/isacikgoz), [jabi27](https://translate.mattermost.com/user/jabi27), [jgheithcock](https://github.com/jgheithcock), [johnsonbrothers](https://github.com/johnsonbrothers), [jprusch](https://github.com/jprusch), [JulienTant](https://github.com/JulienTant), [jwilander](https://github.com/jwilander), [kayazeren](https://github.com/kayazeren), [Kshitij-Katiyar](https://github.com/Kshitij-Katiyar), [ladudu](https://github.com/ladudu), [lani009](https://github.com/lani009), [lani009217f4195555e46f1](https://translate.mattermost.com/user/lani009217f4195555e46f1), [larkox](https://github.com/larkox), [lieut-data](https://github.com/lieut-data), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [majo](https://translate.mattermost.com/user/majo), [mansil](https://github.com/mansil), [marianunez](https://github.com/marianunez), [master7](https://translate.mattermost.com/user/master7), [matthewbirtch](https://github.com/matthewbirtch), [mgdelacroix](https://github.com/mgdelacroix), [minchae.lee](https://translate.mattermost.com/user/minchae.lee), [mrckndt](https://github.com/mrckndt), [neflyte](https://github.com/neflyte), [nickmisasi](https://github.com/nickmisasi), [onovy](https://translate.mattermost.com/user/onovy), [polnetwork](https://translate.mattermost.com/user/polnetwork), [pvev](https://github.com/pvev), [raghavaggarwal2308](https://github.com/raghavaggarwal2308), [rahimrahman](https://github.com/rahimrahman), [Rajat-Dabade](https://github.com/Rajat-Dabade), [saturninoabril](https://github.com/saturninoabril), [sayzard](https://github.com/sayzard), [sbishel](https://github.com/sbishel), [Sharuru](https://github.com/Sharuru), [stafot](https://github.com/stafot), [thejoeejoee](https://github.com/thejoeejoee), [ThrRip](https://translate.mattermost.com/user/ThrRip), [tnir](https://github.com/tnir), [Victor-Nyagudi](https://github.com/Victor-Nyagudi), [vish9812](https://github.com/vish9812), [vpecinka](https://github.com/vpecinka), [wiersgallak](https://github.com/wiersgallak), [wiggin77](https://github.com/wiggin77), [Willyfrog](https://github.com/Willyfrog), [Yash-Chakerverti](https://github.com/Yash-Chakerverti), [yasserfaraazkhan](https://github.com/yasserfaraazkhan)
