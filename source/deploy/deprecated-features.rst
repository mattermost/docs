Removed and deprecated features for Mattermost
==============================================

This page describes features that are removed from support for Mattermost, or will be removed in a future update (deprecated), and provides early notice about future changes that might affect your use of Mattermost. This information is subject to change with future releases, and might not include each deprecated feature.

Removed features in upcoming versions
-------------------------------------


Removed features by Mattermost version
----------------------------------------

Mattermost Server v9.9.0
~~~~~~~~~~~~~~~~~~~~~~~~

- Removed support for self-serve purchases of Mattermost Subscriptions in various flows, throughout Cloud and Self Hosted environments.
- Removed support for self-serve true up review submission in the **System Console**. 

Mattermost Server v9.5.0
~~~~~~~~~~~~~~~~~~~~~~~~

- MySQL v5.7 is at end of life. We recommend all customers to upgrade to at least 8.x. From Mattermost v9.5, which is the latest Extended Support Release, we have stopped supporting MySQL v5.7 altogether.

Mattermost Server v9.0.0
~~~~~~~~~~~~~~~~~~~~~~~~

- Mattermost Boards and various other plugins have transitioned to being fully community supported. See this `forum post <https://forum.mattermost.com/t/upcoming-product-changes-to-boards-and-various-plugins/16669>`_ for more details.
- Removed the deprecated Insights feature.

Mattermost Server v8.0.0
~~~~~~~~~~~~~~~~~~~~~~~~

- Removed ``ExperimentalSettings.PatchPluginsReactDOM``. If this setting was previously enabled, confirm that:
  - All Mattermost-supported plugins are updated to the latest versions.
  - Any other plugins have been updated to support React 17. See the :doc:`Important Upgrade Notes </upgrade/important-upgrade-notes>` for v7.7 for more information.
- Deprecated Insights for all new instances and for existing servers that upgrade to Mattermost v8.0.
- Removed deprecated ``PermissionUseSlashCommands``.
- Removed deprecated ``model.CommandArgs.Session``.
- Removed support for PostgreSQL v10. The new minimum PostgreSQL version is now v11.
- Deprecated the ``AdvancedLoggingConfig`` fields, and replaced them with ``AdvancedLoggingJSON`` fields which accept inline JSON or a filename.

Mattermost Server v6.0.0
~~~~~~~~~~~~~~~~~~~~~~~~

- :doc:`Legacy Command Line Tools </manage/command-line-tools>`. Most commands have been replaced by :doc:`mmctl </manage/mmctl-command-line-tool>` and new commands have been added over the last few months, making this tool a full and robust replacement.
- `Slack Import via the web app </administration/migrating.html?highlight=mmetl#migrating-from-slack-using-the-mattermost-web-app>`_. The Slack import tool accessible via the Team Setting menu is being replaced by the mmetl tool that is much more comprehensive for the types of data it can assist in uploading.
- MySQL versions below 5.7.12. Minimum support will now be for 5.7.12. This version introduced a native JSON data type that lets us improve performance and scalability of several database fields (most notably Users and Posts props). Additionally, version 5.6 (our current minimum version) reached `EOL in February 2021 <https://www.mysql.com/support/eol-notice.html>`_.
- Elasticsearch 5 and 6. `Versions 5.x reached EOL in March of 2019, and versions 6.x reached EOL in November 2020 <https://www.elastic.co/support/eol>`_. Our minimal supported version with Mattermost v6.0 will be Elasticsearch version 7.0.
- Windows 7 reached `EOL in January 2020 <https://support.microsoft.com/en-us/windows/windows-7-support-ended-on-january-14-2020-b75d4580-2cc7-895a-2c9c-1466d9a53962>`_. We will no longer provide support for the desktop app issues on Windows 7.
- :ref:`DisableLegacyMFAEndpoint <configure/deprecated-configuration-settings:disable legacy mfa api endpoint>` configuration setting.
- :ref:`Experimental Timezone <configure/deprecated-configuration-settings:timezone>` configuration setting.
- All legacy channel sidebar experimental configuration settings. We encourage customers using these settings to upgrade to v5.32 or later to access custom, collapsible channel categories among many other channel organization features. The settings being deprecated include:
  
  - :ref:`EnableLegacySidebar <configure/deprecated-configuration-settings:enable legacy sidebar>`
  - :ref:`ExperimentalTownSquareIsReadOnly <configure/deprecated-configuration-settings:town square is read-only>`
  - :ref:`ExperimentalHideTownSquareinLHS <configure/deprecated-configuration-settings:town square is hidden in left hand sidebar>`
  - :ref:`EnableXToLeaveChannelsFromLHS <configure/deprecated-configuration-settings:enable x to leave channels from left hand sidebar>`
  - :ref:`CloseUnusedDirectMessages <configure/deprecated-configuration-settings:autoclose direct messages in sidebar>`
  - :ref:`ExperimentalChannelOrganization <configure/deprecated-configuration-settings:sidebar organization>`
  - :ref:`ExperimentalChannelSidebarOrganization <configure/deprecated-configuration-settings:experimental sidebar features>`

- :ref:`All configuration settings previously marked as “Deprecated” <configure/configuration-settings:deprecated configuration settings>`.
- Changes to mattermost-server/model for naming consistency.

Mattermost Server v5.38.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

- In the v5.38 release (August 16, 2021), the “config watcher” (the mechanism that automatically reloads the “config.json“ file), has been removed in favor of the “mmctl config“ command that will need to be run to apply configuration changes after they are made. This change will improve configuration performance and robustness.

Mattermost Server v5.37.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

- The “platform“ binary and “–platform” flag have been removed. If you are using the “–platform” flag or are using the “platform“ binary directly to run the Mattermost server application via a systemd file or custom script, you will be required to use only the “mattermost“ binary.

Mattermost Server v5.32.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

- TLS versions 1.0 and 1.1 have been deprecated by browser vendors. Starting in Mattermost Server v5.32 (February 16), mmctl returns an error when connected to Mattermost servers deployed with these TLS versions and System Admins will need to explicitly add a flag in their commands to continue to use them. We recommend upgrading to TLS version 1.2 or higher.

Mattermost Server v5.30.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

- PostgreSQL ended long-term support for `version 9.4 in February 2020 <https://www.postgresql.org/support/versioning>`_. From v5.26 Mattermost officially supports PostgreSQL version 10 as PostgreSQL 9.4 is no longer supported. New installs will require PostgreSQL 10+. Previous Mattermost versions, including our current ESR, will continue to be compatible with PostgreSQL 9.4. PostgreSQL 9.4 and all 9.x versions are now fully deprecated in our v5.30 release (December 16). Please follow the instructions under the Upgrading Section within `the PostgreSQL documentation <https://www.postgresql.org/support/versioning/>`_.

Mattermost Server v5.16.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Removed support for Internet Explorer (IE11) in Mattermost v5.16.0. Learn more in our `forum post <https://forum.mattermost.org/t/mattermost-is-dropping-support-for-internet-explorer-ie11-in-v5-16/7575>`__.

Mattermost Server v5.12.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

- ExperimentalEnablePostMetadata setting was removed. Post metadata, including post dimensions, is now stored in the database to correct scroll position and eliminate scroll jumps as content loads in a channel.

Mattermost Server v5.6.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Removed support for WebRTC in beta, and replaced it with other video and audio calling solutions. 
- Removed support for IE11 Mobile View due to low usage and instability in order to invest that effort in maintaining a high quality experience on other more used browsers. End users on IE11 will thus have an increased minimum screen size. Mobile View is still supported on Chrome, Firefox, Safari, Edge as well as the desktop apps.

Mattermost Server v5.0.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

- All API v3 endpoints removed. API v3 endpoints are no longer supported as of Mattermost v4.6 release on January 16th, 2018, and are replaced by API v4 endpoints which were released on July 16th, 2017. See `https://api.mattermost.com <https://api.mattermost.com>`_ to learn more.
- Desktop Notification Duration in Account Settings removed due to inconsistencies on various browsers and operating systems.
- An unused “ExtraUpdateAt” field removed from the channel model.
- ``platform`` binary renamed to mattermost for a clearer install and upgrade experience. All command line tools, including the bulk loading tool and developer tools, also renamed from platform to mattermost.
- Slash commands configured to receive a GET request now have the payload encoded in the query string instead of receiving it in the body of the request, consistent with standard HTTP requests. Although unlikely, this could break custom slash commands that use GET requests incorrectly.
- A new ``config.json`` setting to whitelist types of protocols for auto-linking added.
- A new ``config.json`` setting to disable the `permanent APIv4 delete team parameter <https://api.mattermost.com/#tag/teams%2Fpaths%2F~1teams~1%7Bteam_id%7D%2Fput>`_ added. The setting is off by default for all new and existing installs, except those deployed on GitLab Omnibus. A System Admin can enable the API v4 endpoint from the ``config.json`` file.

Mattermost Server v4.9.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

- A number of permissions configuration settings will be migrated to roles in the database, and changing their config.json values will no longer take effect. These permissions can still be modified by their respective System Console settings. See :doc:`changelog </deploy/legacy-self-hosted-changelog>` for more details.

Mattermost Server v4.0.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

- System Console settings in **Files > Images**, including:
  
  - Image preview height and width
  - Profile picture height and width
  - Image thumbnail height and width

- Font setting in **Account Settings > Display**
- Teammate Name Display setting moved to the System Console

Mattermost Server v3.8.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Old CLI tool (replaced by :doc:`an upgraded CLI tool </manage/command-line-tools>`)
- APIv3 endpoints:
  
  - “GET at /channels/more” (replaced by “/channels/more/{offset}/{limit}”)
  - “POST at /channels/update_last_viewed_at” (replaced by “/channels/view”)
  - “POST at /channels/set_last_viewed_at” (replaced by “/channels/view”)
  - “POST at /users/status/set_active_channel” (replaced by “/channels/view”)

Mattermost Server v3.7.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

- “ServiceSettings: SegmentDeveloperKey” setting in ``config.json``
