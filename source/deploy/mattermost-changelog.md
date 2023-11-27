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

## Release v9.3 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

**Release Date: December 15, 2023**

### Important Upgrade Notes
 - Please read the [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) before upgrading.

### Compatibility
 - Updated minimum required Firefox version to v115+.
 - Updated minimum supported Chromium version to 118+.

### Improvements

#### User Interface (UI)
 - Updated pre-packaged Playbooks plugin version to [v1.39.1](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v1.39.1).
 - Updated pre-packaged Calls version [v0.21.1](https://github.com/mattermost/mattermost-plugin-calls/releases/tag/v0.21.1).
 - Added Vietnamese (Beta) as a new language.
 - Added the ability to passively track keywords with highlights without triggering a notification.
 - Updated the **Settings** modal with an improved user interface.
 - Added a new **Jump to recents** banner when a channel is scrolled up.
 - Modified the behavior of the code button (Ctrl+Alt+C) to create inline codes or code blocks.
 - Disabled markdown keybindings within code blocks.
 - Added a **Back** button to the ``/access_problem`` page.

#### Performance
 - Removed pre-fetch preference and set new prefetch limits for the webapp.
 - Improved websocket event marshaling performance.
 - Batched loading of recently used emojis on initial load.

#### Administration
 - The tooltip on the announcement bar in the **System Console** is now widened.
 - Improved the error message when trying to activate a plugin in an unsupported environment.
 - Added a file storage permission check to the workspace health dashboard.
 - Performed a cleanup in preparation for adding support for multi-word mentions.
 - Added a warning log message when the app runs as root.
 - Removed all uses of ``ExperimentalTimezone`` in webapp.
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
 - Fixed an issue where marking a Group Message as unread didn't show the mention badges correctly.
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

### API Changes
 - Added an API to batch requests for custom emojis on page load.

### Database Changes
 - ``NextSyncAt`` and ``Description`` columns are removed from the ``SharedChannelsRemotes`` table. Migration impact is considered to be minimal considering the possible table size.

### Go Version
 - v9.3 is built with Go ``v1.20.7``.

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
 - 

## Release v9.2 - [Feature Release](https://docs.mattermost.com/upgrade/release-definitions.html#feature-release)

- **9.2.2, released 2023-11-08**
  - Mattermost v9.2.2 contains a high severity level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) to this release is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Pre-packaged Playbooks plugin version [v1.39.1](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v1.39.1).
  - Fixed an issue where the **About Mattermost** dialog reported an incorrect server version.
- **9.2.1, released 2023-11-06**
  - Fixed an issue where Ubuntu GLIBC errors were thrown on Ubuntu 20.04 and Debian Bullseye versions.
- **9.2.0, released 2023-11-02**
  - Original 9.2.0 release

### Important Upgrade Notes
 - Please read the [Important Upgrade Notes](https://docs.mattermost.com/upgrade/important-upgrade-notes.html) before upgrading.

### Compatibility
 - Updated minimum required Edge version to 116+.

### Improvements

#### User Interface (UI)
 - Improved readability by displaying system messages on multiple lines when editing a channel header.
 - Combined "joined/left" event types in system messages.
 - Added a new user preference to disable webapp prefetching via **Settings > Advanced > Allow Mattermost to prefetch channel posts**.
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
 - To be added.
