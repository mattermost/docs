# v11 Changelog

```{eval-rst}
.. meta::
  :page_title: Mattermost Server v11 Release Notes
```

```{Important}
```{include} common-esr-support-upgrade.md
```

(release-v11.0-major-release)=
## Release v11.0 - [Major Release](https://docs.mattermost.com/product-overview/release-policy.html#release-types)

**Release day: 2025-10-16**

### Important Upgrade Notes
 - Gitlab SSO will no longer be available in Free Edition, requiring a minimum Professional license as part of [the Gitlab Mattermost deprecation](https://forum.mattermost.com/t/mattermost-v11-changes-in-free-offerings/25126/1).
 - MySQL support has been completely removed from the codebase. Mattermost will completely stop supporting MySQL as a database driver from v11 onwards and will throw an invalid configuration error.
 - Deprecated the format query parameter requirement in ``/api/v4/config/client`` endpoint.
 - Removed deprecated ``include_removed_members`` option in ``api/v4/ldap/sync``.
 - ``TeamSettings.ExperimentalViewArchivedChannels`` must now always be ``true``, always allowing archived channels to be viewed.
 - Added logic to migrate the password hashing method from bcrypt to PBKDF2. The migration will happen progressively, migrating the password of a user as soon as they have to enter it; e.g. when logging in or when double-checking their password for any sensitive action. There is an edge case where users might get locked out of their account: if a server upgrades to v11 and user A logs in (i.e., they need to enter their password), and then the server downgrades to v10.12 or previous, user A will no longer be able to log in. In this case, admins will need to manually reset the password of such users, through the system console or through the ``mmctl user reset-password [users]`` command.

```{Important}
If you upgrade from a release earlier than v10.10, please read the other [Important Upgrade Notes](https://docs.mattermost.com/administration-guide/upgrade/important-upgrade-notes.html).
```

### Highlights
 - Introduced support for Mattermost Entry Edition with Message History Limits.

### Improvements

#### User Interface (UI)
 - Pre-packaged Agents plugin [v1.3.1](https://github.com/mattermost/mattermost-plugin-agents/releases/tag/v1.3.1).
 - Pre-packaged Boards plugin [v9.1.6](https://github.com/mattermost/mattermost-plugin-boards/releases/tag/v9.1.6).
 - Pre-packaged MS Teams plugin [v2.2.2](https://github.com/mattermost/mattermost-plugin-msteams/releases/tag/v2.2.2).
 - Pre-packaged Playbooks plugin [v2.4.1](https://github.com/mattermost/mattermost-plugin-playbooks/releases/tag/v2.4.1), allowing Professional licenses to use playbooks v2.
 - Removed Playbooks v1 from pre-packaged plugins.
 - Updated the library used for customizing scrollbars.

#### Administration
 - User limits were lowered to final threshold of 250 for Mattermost Team Edition (MIT-Compiled License).
 - Added support for a new ``EmailNotificationWillBeSent`` plugin hook.
 - PBKDF2 is now used as the new key derivation algorithm for remote cluster invitations. We do this in a backward compatible way such that invitations generated from new/old clusters work in all clusters.
 - Updated the default SAML signature algorithm from SHA1 to SHA256 for improved security.
 - Added admin-managed property fields to Custom Profile Attributes.
 - Admin managed Custom Profile Attribute fields can now be used as part of Attribute Based Access Control policies.
 - System Admins can now mark Custom Profile Attribute fields as “admin managed” from the System Console.
 - Added Channel-Level Attribute-Based Access Control (Available only in Enterprise Advanced). Channel Admins can now configure attribute-based access rules directly in Channel Settings through a new Access Control tab when the ``EnableChannelScopeAccessControl`` setting is enabled.
 - Added Elasticsearch test to Support Packet diagnostics.
 - Implemented dynamic select for interactive dialogs.
 - Updated interactive dialogs to use the apps form framework.
 - Implemented multi-select for interactive dialogs.
 - ``UserId`` and ``TeamId`` are now passed in interactive dialog submissions.
 - Increased page size when retrieving posts in channels with high number of hidden messages.
 - User ``auth_data`` is now shown in the System Console user details page.
 - Channel access control policies now support multiple parent inheritances.
 - Changed default database connection pool settings: changed ``MaxOpenConns`` from 300 to 100 and ``MaxIdleConns`` from 20 to 50, establishing a healthier 2:1 ratio for better database connection management.
 - Stopped supporting manually installed plugins as per https://forum.mattermost.com/t/deprecation-notice-manual-plugin-deployment/21192.

#### mmctl
 - Removed deprecated mmctl commands and flags:
    - ``channel add`` - use ``channel users add``
    - ``channel remove`` - use ``channel users remove``
    - ``channel restore`` - use ``channel unarchive``
    - ``channel make-private`` - use ``channel modify --private``
    - ``command delete`` - use ``command archive``
    - ``permissions show`` - use ``permissions role show``
 - Added ``mmctl user edit`` command.
 - Updated mmctl shell completion to fully support zsh, powershell, and fish. Check out ``mmctl completion`` for a guide on how to set it up for your shell.
 - Added mmctl commands to manipulate Custom Profile Attribute values.
 - Added a set of mmctl commands to manage Custom Profile Attributes.

### Bug Fixes
 - Fixed an issue where extra date separators were added in search results, pinned posts and saved messages.
 - Fixed an issue where MFA warning was thrown in the logs for unauthenticated plugin requests.
 - Fixed an issue that prevented new users from searching channels right after joining a team when Elasticsearch was enabled.
 - Fixed some crashes in the threads screen. 

### config.json
New setting options were added to ``config.json``. Below is a list of the additions and their default values on install. The settings can be modified in ``config.json``, or the System Console when available.

#### Changes to all plans:
 - 

#### Changes to Professional and Enterprise plans: 
 - 

#### Changes to Enterprise Advanced plan: 
 - 

### API Changes
 - Added a counting plugin API for properties.
 - Added a new API endpoint to update Custom Profile Attribute values for a given user.
 - Added a new API endpoint ``POST /api/v4/groups/names``.

### Open Source Components
 - Added ``simplebar-react`` and removed ``go-sql-driver/mysql``, ``blevesearch/bleve`` and ``axios`` from https://github.com/mattermost/mattermost/. 

### Go Version
 - v11.0 is built with Go v1.24.5.

### Contributors
 - 
