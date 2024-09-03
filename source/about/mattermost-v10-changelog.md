# v10 changelog

```{Important}
Support for Mattermost Server v9.5 [Extended Support Release](https://docs.mattermost.com/about/release-policy.html#extended-support-releases) is coming to the end of its life cycle on November 15, 2024. Upgrading to Mattermost Server v9.11 or later is recommended.
- Upgrading from ESR-to-ESR (``major`` -> ``major_next``) is fully supported and tested. However, upgrading from ESR-to-ESR (``major`` to ``major+2``) is supported, but not tested. If you plan to upgrade across multiple releases, we strongly recommend upgrading from an ESR to another ESR. For example, if you're upgrading from the v8.1 ESR, upgrade to the [v9.5 ESR](https://docs.mattermost.com/about/mattermost-v9-changelog.html#release-v9-5-extended-support-release) or the v9.11 ESR.
- See the [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) documentation for details on upgrading to a newer release.
- See the [changelog in progress](https://bit.ly/2nK3cVf) for details about the upcoming release.
```

(release-v10.0-major-release)=
## Release v10.0 - [Major Release](https://docs.mattermost.com/about/release-policy.html#release-types)

**Release day: 2024-09-16**

### Important Upgrade Notes
 - We no longer support new installations using MySQL starting in v10. All new customers and/or deployments will only be supported with the minimum supported version of the PostgreSQL database. End of support for MySQL is targeted for Mattermost v11.
 - Apps Framework is deprecated for new installs. Please extend Mattermost using webhooks, slash commands, OAuth2 apps, and plugins.
 - An Enterprise license will be required to use v2.0+ Playbooks functionality starting in v10. Team Edition and Professional deployments can continue to use Playbooks v1.x. Feature updates will only be added to Playbooks v2.0+.
 - Renamed ``Channel Moderation`` to ``Advanced Access Control`` in the channel management section in the **System Console**.
 - Renamed announcement banner feature to “system-wide notifications”.
 - Renamed “Collapsed Reply Threads” to “Threaded Discussions” in the System Console.
 - Renamed “System Roles” to “Delegated Granular Administration” in the System Console.
 - Renamed "Office 365" to "Entra ID" for SSO logins.
 - Fully deprecated the ``/api/v4/image`` endpoint when the image proxy is disabled.
 - Pre-packaged Calls plugin [v1.0.1](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v1.0.1). This includes breaking changes such as allowing calls in direct message channels only on unlicensed servers.
 - Removed deprecated ``Config.ProductSettings``, ``LdapSettings.Trace``, and ``AdvancedLoggingConfig`` configuration fields.
 - Removed deprecated ``pageSize`` query parameter from most API endpoints.
 - Deprecated the experimental Strict CSRF token enforcement. This feature will be fully removed in Mattermost v11.

```{Important}
If you upgrade from a release earlier than v9.11, please read the other [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html).
```

### Highlights

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
