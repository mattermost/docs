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
 - GitLab SSO has been deprecated from Team Edition. Deployments using GitLab SSO can remain on v10.11 ESR (with 12 months of security updates) while transitioning to our new free offering Mattermost Entry, or exploring commercial/nonprofit options. See more details in [this forum post](https://forum.mattermost.com/t/mattermost-v11-changes-in-free-offerings/25126).
 - The ``TeamSettings.ExperimentalViewArchivedChannels`` setting has been deprecated. Archived channels will always be accessible, subject to normal channel membership. The server will fail to start if this setting is set to ``false``; to deny access to archived channels, mark them as private and remove affected channel members. See more details in [this forum post](https://forum.mattermost.com/t/viewing-accessing-archived-channels-v11/22626).
 - Playbooks has stopped working for Team Edition. Entry, Professional, Enterprise, and Enterprise Advanced plans are automatically upgraded to Playbooks v2 with no expected downtime. See more details in [this forum post](https://forum.mattermost.com/t/clarification-and-update-on-the-playbooks-plugin-v11/25192).
 - Experimental Bleve Search functionality has been retired. If Bleve is enabled, search will not work until ``DisableDatabaseSearch`` is set to ``false``. See more details in [this forum post](https://forum.mattermost.com/t/transitioning-from-bleve-search-in-mattermost-v11/22982).
 - Support for MySQL has ended. See more details in [this forum post](https://forum.mattermost.com/t/transition-to-postgresql/19551).
 - The ``ExperimentalStrictCSRFEnforcement`` setting has been renamed to ``StrictCSRFEnforcement`` and the default value has been changed to ``true`` for new installations. See more details in [this forum post](https://forum.mattermost.com/t/default-value-of-the-experimental-strict-csrf-enforcement-setting-to-be-changed-to-true-v11/23139).
 - The ``registerPostDropdownMenuComponent`` hook in the web app’s plugin API has been removed in favour of ``registerPostDropdownMenuAction``. See more details in [this forum post](https://forum.mattermost.com/t/deprecating-a-post-dropdown-menu-component-plugin-api-v11/25001).
 - The web app is no longer exposing the [Styled Components](https://styled-components.com/) dependency for use by web app plugins. See more details in [this forum post](https://forum.mattermost.com/t/removing-styled-components-export-for-web-app-plugins-v11/25002).
 - Omnibus support has been deprecated. The last ``mattermost-omnibus`` release was v10.12. See more details in [this forum post](https://forum.mattermost.com/t/mattermost-omnibus-to-reach-end-of-life-v11/25175).
 - Deprecated ``include_removed_members`` option in ``api/v4/ldap/sync`` have been removed. Admins can use the LDAP setting ``ReAddRemovedMembers``.
 - Customers that have the NPS plugin enabled can remove it as it no longer sends the feedback over through telemetry.
 - Format query parameter requirement in ``/api/v4/config/client`` endpoint has been deprecated.
 - Removed deprecated mmctl commands and flags:
    - ``channel add`` - use ``channel users add``
    - ``channel remove`` - use ``channel users remove``
    - ``channel restore`` - use ``channel unarchive``
    - ``channel make-private`` - use ``channel modify --private``
    - ``command delete`` - use ``command archive``
    - ``permissions show`` - use ``permissions role show``
 - Experimental certificate-based authentication feature has been removed. ``ExperimentalSettings.ClientSideCertEnable`` must be ``false`` to start the server.
 - Added logic to migrate the password hashing method from bcrypt to PBKDF2. The migration will happen progressively, migrating the password of a user as soon as they enter it; e.g. when logging in or when double-checking their password for any sensitive action. There is an edge case where users might get locked out of their account: if a server upgrades to v11 and user A logs in (i.e., they need to enter their password), and then the server downgrades to v10.12 or previous, user A will no longer be able to log in. In this case, admins will need to manually reset the password of such users, through the system console or through the [mmctl user reset-password [users]](https://docs.mattermost.com/administration-guide/manage/mmctl-command-line-tool.html#mmctl-user-reset-password) command.
 - ``/api/v4/teams/{team_id}/channels/search_archived`` has been deprecated in favour of ``/api/v4/channels/search`` with the deleted parameter.
 - Changed default database connection pool settings: changed ``MaxOpenConns`` from 300 to 100 and ``MaxIdleConns`` from 20 to 50, establishing a healthier 2:1 ratio for better database connection management.
 - Separate notification log file has been deprecated. If admins want to continue using a separate log file for notification logs, they can use the ``AdvancedLoggingJSON`` configuration. An example configuration to use is:

 ```
   {
     "LogSettings": {
       "AdvancedLoggingJSON": {
         "notifications_file": {
           "type": "file",
           "format": "json",
           "levels": [
               {"id": 300, "name": "NotificationError"},
               {"id": 301, "name": "NotificationWarn"},
               {"id": 302, "name": "NotificationInfo"},
               {"id": 303, "name": "NotificationDebug"},
               {"id": 304, "name": "NotificationTrace"}
           ],
           "options": {
               "filename": "notifications.log",
               "max_size": 100,
               "max_age": 0,
               "max_backups": 0,
               "compress": true
           }, 
           "maxqueuesize": 1000 
         }
       }
     }
   }
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
 - Introduced support for Mattermost Entry Edition with message history limits.
 - User limits were lowered to final threshold of 250 for Mattermost Team Edition (MIT-Compiled License).
 - Added support for a FIPS-compliant Mattermost image.
 - PBKDF2 is now used as the new key derivation algorithm for remote cluster invitations. We do this in a backward compatible way such that invitations generated from new/old clusters work in all clusters.
 - Updated the default SAML signature algorithm from SHA1 to SHA256 for improved security.
 - Added admin-managed property fields to Custom Profile Attributes.
 - Admin managed Custom Profile Attribute fields can now be used as part of Attribute Based Access Control policies.
 - System Admins can now mark Custom Profile Attribute fields as “admin managed” from the System Console.
 - Added Channel-Level Attribute-Based Access Control (Available only in Enterprise Advanced). Channel Admins can now configure attribute-based access rules directly in Channel Settings through a new Access Control tab when the ``EnableChannelScopeAccessControl`` setting is enabled.
 - Channel access control policies now support multiple parent inheritances.
 - Updated interactive dialogs to use the apps form framework. Implemented dynamic select and multi-select for interactive dialogs. Also, ``UserId`` and ``TeamId`` are now passed in interactive dialog submissions.
 - Stopped supporting manually installed plugins as per https://forum.mattermost.com/t/deprecation-notice-manual-plugin-deployment/21192.
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
 - Under ``ServiceSettings`` in ``config.json``:
     - ``ExperimentalStrictCSRFEnforcement`` has been renamed to ``StrictCSRFEnforcement`` and has been changed to be ``true`` by default for new installations. For existing installations, the value will remain unchanged.
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
 - Added a new API endpoint ``POST /api/v4/groups/names``.

### Go Version
 - v11.0 is built with Go ``v1.24.5``.

### Open Source Components
 - Added ``simplebar-react``, and removed ``go-sql-driver/mysql``, ``blevesearch/bleve`` and ``axios`` from https://github.com/mattermost/mattermost/. 

### Contributors
 - 
