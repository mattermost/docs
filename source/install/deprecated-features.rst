Removed and deprecated features for Mattermost
==============================================

This page describes features that are removed from support for Mattermost, or will be removed in a future update (deprecated), and provides early notice about future changes that might affect your use of Mattermost. This information is subject to change with future releases, and might not include each deprecated feature.

Removed features in upcoming versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Server v8.0.0
^^^^^^^^^^^^^^^^^^^^^^^^

- Remove ExperimentalSettings.PatchPluginsReactDOM
- Remove deprecated PermissionUseSlashCommands

Removed features by Mattermost version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Server v6.0.0
^^^^^^^^^^^^^^^^^^^^^^^^

- `Legacy Command Line Tools </manage/command-line-tools.html>`__. Most commands have been replaced by `mmctl </manage/mmctl-command-line-tool.html>`_ and new commands have been added over the last few months, making this tool a full and robust replacement.
- `Slack Import via the web app </administration/migrating.html?highlight=mmetl#migrating-from-slack-using-the-mattermost-web-app>`_. The Slack import tool accessible via the Team Setting menu is being replaced by the mmetl tool that is much more comprehensive for the types of data it can assist in uploading.
- MySQL versions below 5.7.12. Minimum support will now be for 5.7.12. This version introduced a native JSON data type that lets us improve performance and scalability of several database fields (most notably Users and Posts props). Additionally, version 5.6 (our current minimum version) reached `EOL in February 2021 <https://www.mysql.com/support/eol-notice.html>`_.
- Elasticsearch 5 and 6. `Versions 5.x reached EOL in March of 2019, and versions 6.x reached EOL in November 2020 <https://www.elastic.co/support/eol>`_. Our minimal supported version with Mattermost v6.0 will be Elasticsearch version 7.0.
- Windows 7 reached `EOL in January 2020 <https://support.microsoft.com/en-us/windows/windows-7-support-ended-on-january-14-2020-b75d4580-2cc7-895a-2c9c-1466d9a53962>`_. We will no longer provide support for the desktop app issues on Windows 7.
- `DisableLegacyMFAEndpoint </administration/config-settings.html#disable-legacy-mfa-api-endpoint>`_ configuration setting.
- `Experimental Timezone </administration/config-settings.html#timezone>`_ configuration setting.
- All legacy channel sidebar experimental configuration settings. We encourage customers using these settings to upgrade to v5.32 or later to access custom, collapsible channel categories among many other channel organization features. The settings being deprecated include:
  
  - `EnableLegacySidebar </administration/config-settings.html#enable-legacy-sidebar>`_
  - `ExperimentalTownSquareIsReadOnly </administration/config-settings.html#town-square-is-read-only-experimental>`_
  - `ExperimentalHideTownSquareinLHS </administration/config-settings.html#town-square-is-hidden-in-left-hand-sidebar-experimental>`_
  - `EnableXToLeaveChannelsFromLHS </administration/config-settings.html#enable-x-to-leave-channels-from-left-hand-sidebar-experimental>`_
  - `CloseUnusedDirectMessages </administration/config-settings.html#autoclose-direct-messages-in-sidebar-experimental>`_
  - `ExperimentalChannelOrganization </administration/config-settings.html#sidebar-organization>`_
  - `ExperimentalChannelSidebarOrganization </administration/config-settings.html#experimental-sidebar-features>`_

- `All configuration settings previously marked as “Deprecated” </administration/config-settings.html#deprecated-configuration-settings>`_.
- Changes to mattermost-server/model for naming consistency.

Mattermost Server v5.38.0
^^^^^^^^^^^^^^^^^^^^^^^^^

- In the v5.38 release (August 16, 2021), the “config watcher” (the mechanism that automatically reloads the “config.json“ file), has been removed in favor of the “mmctl config“ command that will need to be run to apply configuration changes after they are made. This change will improve configuration performance and robustness.

Mattermost Server v5.37.0
^^^^^^^^^^^^^^^^^^^^^^^^^

- The “platform“ binary and “–platform” flag have been removed. If you are using the “–platform” flag or are using the “platform“ binary directly to run the Mattermost server application via a systemd file or custom script, you will be required to use only the “mattermost“ binary.

Mattermost Server v5.32.0
^^^^^^^^^^^^^^^^^^^^^^^^^

- TLS versions 1.0 and 1.1 have been deprecated by browser vendors. Starting in Mattermost Server v5.32 (February 16), mmctl returns an error when connected to Mattermost servers deployed with these TLS versions and System Admins will need to explicitly add a flag in their commands to continue to use them. We recommend upgrading to TLS version 1.2 or higher.

Mattermost Server v5.30.0
^^^^^^^^^^^^^^^^^^^^^^^^^

- PostgreSQL ended long-term support for `version 9.4 in February 2020 <https://www.postgresql.org/support/versioning>`_. From v5.26 Mattermost officially supports PostgreSQL version 10 as PostgreSQL 9.4 is no longer supported. New installs will require PostgreSQL 10+. Previous Mattermost versions, including our current ESR, will continue to be compatible with PostgreSQL 9.4. PostgreSQL 9.4 and all 9.x versions are now fully deprecated in our v5.30 release (December 16). Please follow the instructions under the Upgrading Section within `the PostgreSQL documentation <https://www.postgresql.org/support/versioning/>`_.

Mattermost Server v5.16.0
^^^^^^^^^^^^^^^^^^^^^^^^^

- Removed support for Internet Explorer (IE11) in Mattermost v5.16.0. Learn more in our `forum post <https://forum.mattermost.org/t/mattermost-is-dropping-support-for-internet-explorer-ie11-in-v5-16/7575>`_.

Mattermost Server v5.12.0
^^^^^^^^^^^^^^^^^^^^^^^^^

- ExperimentalEnablePostMetadata setting was removed. Post metadata, including post dimensions, is now stored in the database to correct scroll position and eliminate scroll jumps as content loads in a channel.

Mattermost Server v5.6.0
^^^^^^^^^^^^^^^^^^^^^^^^^

- Removed support for WebRTC in beta, and replaced it with other video and audio calling solutions. Learn more in our `documentation </deployment/video-and-audio-calling.html>`_.
- Removed support for IE11 Mobile View due to low usage and instability in order to invest that effort in maintaining a high quality experience on other more used browsers. End users on IE11 will thus have an increased minimum screen size. Mobile View is still supported on Chrome, Firefox, Safari, Edge as well as the desktop apps.

Mattermost Server v5.0.0
^^^^^^^^^^^^^^^^^^^^^^^^

- All API v3 endpoints removed. API v3 endpoints are no longer supported as of Mattermost v4.6 release on January 16th, 2018, and are replaced by API v4 endpoints which were released on July 16th, 2017. See `https://api.mattermost.com <https://api.mattermost.com>`_ to learn more.
- Desktop Notification Duration in Account Settings removed due to inconsistencies on various browsers and operating systems.
- An unused “ExtraUpdateAt” field removed from the channel model.
- ``platform`` binary renamed to mattermost for a clearer install and upgrade experience. All command line tools, including the bulk loading tool and developer tools, also renamed from platform to mattermost.
- Slash commands configured to receive a GET request now have the payload encoded in the query string instead of receiving it in the body of the request, consistent with standard HTTP requests. Although unlikely, this could break custom slash commands that use GET requests incorrectly.
- A new ``config.json`` setting to whitelist types of protocols for auto-linking added.
- A new ``config.json`` setting to disable the `permanent APIv4 delete team parameter <https://api.mattermost.com/#tag/teams%2Fpaths%2F~1teams~1%7Bteam_id%7D%2Fput>`_ added. The setting is off by default for all new and existing installs, except those deployed on GitLab Omnibus. A System Admin can enable the API v4 endpoint from the ``config.json`` file.

Mattermost Server v4.9.0
^^^^^^^^^^^^^^^^^^^^^^^^

- A number of permissions configuration settings will be migrated to roles in the database, and changing their config.json values will no longer take effect. These permissions can still be modified by their respective System Console settings. See `changelog </install/self-managed-changelog.html>`_ for more details.

Mattermost Server v4.0.0
^^^^^^^^^^^^^^^^^^^^^^^^

- System Console settings in **Files > Images**, including:
  
  - Image preview height and width
  - Profile picture height and width
  - Image thumbnail height and width

- Font setting in **Account Settings > Display**
- Teammate Name Display setting moved to the System Console

Mattermost Server v3.8.0
^^^^^^^^^^^^^^^^^^^^^^^^

- Old CLI tool (replaced by `an upgraded CLI tool </administration/command-line-tools.html>`_)
- APIv3 endpoints:
  
  - “GET at /channels/more” (replaced by “/channels/more/{offset}/{limit}”)
  - “POST at /channels/update_last_viewed_at” (replaced by “/channels/view”)
  - “POST at /channels/set_last_viewed_at” (replaced by “/channels/view”)
  - “POST at /users/status/set_active_channel” (replaced by “/channels/view”)

Mattermost Server v3.7.0
^^^^^^^^^^^^^^^^^^^^^^^^

- “ServiceSettings: SegmentDeveloperKey” setting in ``config.json``
