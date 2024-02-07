Deprecated configuration settings
=================================

The following Mattermost configuration settings are deprecated and are no longer supported in current Mattermost releases:

- `Mattermost Boards settings <#mattermost-boards-settings>`__
- `Bleve settings <#bleve-settings>`__
- `Elasticsearch settings <#elasticsearch-settings>`__
- `Service settings <#service-settings>`__
- `Database settings <#database-settings>`__
- `Users and teams settings <#users-and-teams-settings>`__
- `SAML 2.0 settings <#saml-2-0-settings>`__
- `Legacy sidebar settings <#legacy-sidebar-settings>`__
- `Town Square channel settings <#town-square-channel-settings>`__
- `Custom emoji settings <#custom-emoji-settings>`__
- `Timezone settings <#timezone-settings>`__
- `High availablity settings <#high-availability-settings>`__
- `Rest API V3 settings <#rest-api-v3-settings>`__
- `Integrations settings <#integrations-settings>`__
- `Permission policy settings <#permission-policy-settings>`__
- `Image settings <#image-settings>`__
- `Experimental display settings <#experimental-display-settings>`__
- `Other deprecated settings <#other-deprecated-settings>`__

----

Mattermost Boards setting
--------------------------

*Removed in the Mattermost v8.0 release*

Enable publicly-shared boards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+--------------------------------------------------------------------------------------+
| Enable or disable the ability to share               | - System Config path: **Products > Boards**                                          |
| links to Mattermost boards with other users.         | - ``config.json`` setting: ``".ProductSettings.EnablePublicSharedBoards: false”,``   |
|                                                      | - Environment variable: ``MM_PRODUCTSETTINGS_ENABLEPUBLICSHAREDBOARDS``              |
| - **true**: Enables the ability to share links to    |                                                                                      |
|   Mattermost boards with other users.                |                                                                                      |
| - **false**: **(Default)** Mattermost boards can't   |                                                                                      |
|   be shared with other users.                        |                                                                                      |
+------------------------------------------------------+--------------------------------------------------------------------------------------+
| **Notes**:                                                                                                                                  |
|                                                                                                                                             |
| - From Mattermost v7.7 through Mattermost v7.10, this configuration setting applies to Mattermost Boards available as an official           |
|   in-product vertical.                                                                                                                      |
| - See the `Focalboard <guides/focalboard-plugin.html>`__ documentation for details on `sharing boards links with other                      |
|   users <boards/share-and-collaborate.html#share-a-board-publicly>`__.                                                                      |
| - Cloud admins can't modify this configuration setting.                                                                                     |
+------------------------------------------------------+--------------------------------------------------------------------------------------+

Bleve settings
--------------

Bulk Indexing Time Window Seconds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in May 16, 2022 release*

This setting isn't available in the System Console and can only be set in ``config.json``.

Determines the maximum time window for a batch of posts being indexed by the Bulk Indexer. This setting serves as a performance optimization for installs with over ~10 million posts in the database. You can approximate this value based on the average number of seconds for 2,000 posts to be added to the database on a typical day in production. Setting this value too low will cause bulk indexing jobs to run slowly.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BulkIndexingTimeWindowSeconds": 3600`` with numerical input.   |
+-------------------------------------------------------------------------------------------------------------+

----

Elasticsearch settings
----------------------

Bulk Indexing Time Window
~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in May 16, 2022 release*

This setting isn't available in the System Console and can only be set in ``config.json``.

Determines the maximum time window for a batch of posts being indexed by the Bulk Indexer. This setting serves as a performance optimization for installs with over ~10 million posts in the database. You can approximate this value based on the average number of seconds for 2,000 posts to be added to the database on a typical day in production. Setting this value too low will cause bulk indexing jobs to run slowly.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BulkIndexingTimeWindowSeconds": 3600`` with numerical input.       |
+-----------------------------------------------------------------------------------------------------------------+

----

Service settings
----------------

Enable reliable websockets
~~~~~~~~~~~~~~~~~~~~~~~~~~

*This configuration setting has been deprecated, and the ability to buffer messages during a connection loss has been promoted to general availability from Mattermost v6.3. This setting is enabled for older clients to maintain backwards compatibility.*

This setting isn't available in the System Console and can only be set in ``config.json``.

Enable this setting to make websocket messages more reliable by buffering messages during a connection loss and then re-transmitting all unsent messages when the connection is revived.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableReliableWebsockets": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------------+

Data prefetch
~~~~~~~~~~~~~

*Removed in February 16, 2021 release*

**True**: Messages in all unread channels are pre-loaded from the server whenever the client reconnects to the network to eliminate loading time when users switch to unread channels.

**False**: Messages are fetched on-demand from the server when users switch channels.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalDataPrefetch": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------------+

Segment write key
~~~~~~~~~~~~~~~~~

*Removed in March 16, 2017 release*

For deployments seeking additional tracking of system behavior using Segment.com, you can enter a Segment ``WRITE_KEY`` using this field. This value works like a tracking code and is used in client-side JavaScript and will send events to Segment.com attributed to the account you used to generate the ``WRITE_KEY``.

+--------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SegmentDeveloperKey": ""`` with string input. |
+--------------------------------------------------------------------------------------------+

Limit access to config settings prior to login
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in December 16, 2018 release*

Enable this setting to limit the number of config settings sent to users prior to login.

Supported for Mattermost server v5.1.0 and later, and Mattermost Mobile apps v1.10.0 and later.

+-----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalLimitClientConfig": "false"`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------------------+

Disable legacy MFA API endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. tab:: Mattermost v6.0 onwards

      Deprecated. Not used in Mattermost v6.0 and later.

   .. tab:: Mattermost v5.39 and earlier

      This setting isn't available in the System Console and can only be set in ``config.json``.

      **True**: Disables the legacy ``checkMfa`` endpoint, which is only required for Mattermost mobile apps v1.16 or earlier when using multi-factor authentication (MFA). Recommended to set to ``true`` for additional security hardening.

      **False**: Keeps the legacy ``checkMfa`` endpoint enabled to support mobile versions 1.16 and earlier. Keeping the endpoint enabled creates an information disclosure about whether a user has set up MFA.

      +--------------------------------------------------------------------------------------------------------------+
      | This feature's ``config.json`` setting is ``"DisableLegacyMFA": true,`` with options ``true`` and ``false``. |
      +--------------------------------------------------------------------------------------------------------------+

----

Database settings
------------------

At rest encrypt key
~~~~~~~~~~~~~~~~~~~

*Removed in August 23, 2018 release*

This setting isn't available in the System Console and can only be set in ``config.json``. It's a legacy setting used to encrypt data stored at rest in the database, and no fields are encrypted using ``AtRestEncryptKey``.

A 32-character key for encrypting and decrypting sensitive fields in the database. When using high availability, this value must be identical in each instance of Mattermost.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AtRestEncryptKey": ""`` with string input.  |
+------------------------------------------------------------------------------------------+

Amazon S3 bucket endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in November 16th, 2016 release*

Set an endpoint URL for Amazon S3 buckets.

+-----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3BucketEndpoint": ""`` with string input. |
+-----------------------------------------------------------------------------------------------+

Amazon S3 Location Constraint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in November 16th, 2016 release*

**True**: S3 region is location constrained.

**False**: S3 region is not location constrained.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3LocationConstraint": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

Amazon S3 lowercase bucket
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in November 16th, 2016 release*

**True**: S3 bucket names are fully lowercase.

**False**: S3 bucket names may contain uppercase and lowercase letters.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3LowercaseBucket": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------------+

----

Users and teams settings
------------------------

Enable team directory
~~~~~~~~~~~~~~~~~~~~~

*Removed in May 16th, 2016 release*

**True**: Teams that are configured to appear in the team directory will appear on the system main page. Teams can configure this setting from **Team Settings > Include this team in the Team Directory**.

**False**: Team directory on the system main page is disabled.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableTeamListing": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Allow team admins to edit others' posts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. tab:: Mattermost v6.0 onwards

      Deprecated. Not used in Mattermost v6.0 and later.

   .. tab:: Mattermost v5.39 and earlier

      This permission is stored in the database and can be modified using the System Console user interface.

      **True**: Team Admins and System Admins can edit other users' posts.

      **False**: Only System Admins can edit other users' posts.

      .. note::

         System Admins and Team Admins can always delete other users' posts. This setting is only available for Team Edition servers. Enterprise Edition servers can use `Advanced Permissions </onboard/advanced-permissions.html>`__ to configure this permission.

Enable team creation
~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. tab:: Mattermost v6.0 onwards

      Deprecated. Not used in Mattermost v6.0 and later.

   .. tab:: Mattermost v5.39 and earlier

      After upgrading to v4.9 (released April 16, 2018), changing this ``config.json`` value no longer takes effect because this permission has been migrated to the database. This permission can be modified using the System Console user interface.

      **True**: Ability to create a new team is enabled for all users.

      **False**: Only System Admins can create teams from the team selection page. The **Create A New Team** button is hidden.

      +---------------------------------------------------------------------------------------------------------------+
      | This feature's ``config.json`` setting is ``"EnableTeamCreation": true`` with options ``true`` and ``false``. |
      +---------------------------------------------------------------------------------------------------------------+

----

SAML 2.0 settings
-----------------

Use new SAML library
~~~~~~~~~~~~~~~~~~~~

*Removed in December 16, 2020 release*

**True**: Enable an updated SAML Library, which does not require the XML Security Library (xmlsec1) to be installed.

**False**: Continue using the existing implementation which uses the XML Security Library (xmlsec1).

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UseNewSAMLLibrary": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

----

Legacy sidebar settings
-----------------------

Enable legacy sidebar
~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. tab:: Mattermost v6.0 onwards

      Deprecated. Not used in Mattermost v6.0 and later.

   .. tab:: Mattermost v5.39 and earlier

      *Not available in Mattermost Cloud*

      This setting re-enables the legacy sidebar functionality for all users on this server. We strongly recommend System Admins disable this setting so users can access `enhanced sidebar features <https://mattermost.com/blog/custom-collapsible-channel-categories/>`__, including custom, collapsible channel categories, drag and drop, unread filtering, channel sorting options, and more.

      **False**: Users can access all new channel sidebar features, including custom, collapsible channel categories, drag and drop, unread filtering, channel sorting options, and more. See `the documentation </messaging/organizing-your-sidebar.html>`_ for more information about these features.

      **True**: When enabled, the legacy sidebar is enabled for all users on this server and users cannot access any new channel sidebar features. The legacy channel sidebar is scheduled to be deprecated, and is only recommended if your deployment is experiencing bugs or other issues with the new channel sidebar.

      +----------------------------------------------------------------------------------------------------------------+
      | This feature's ``config.json`` setting is ``"EnableLegacySidebar": false`` with options ``true`` or ``false``. |
      +----------------------------------------------------------------------------------------------------------------+

Experimental sidebar features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Deprecated. Not used in Mattermost v5.32 and later*

.. note::
   This experimental configuration setting has been deprecated, and the ability to organize channels in the sidebar has been promoted to general availability from Mattermost v5.32. See the `Organizing Your Sidebar documentation </messaging/organizing-your-sidebar.html#customizing-your-sidebar>`__ for details on customizing the sidebar.

**Disabled**: Users cannot access the experimental channel sidebar feature set.

**Enabled (Default On)**: Enables the experimental sidebar features for all users on this server. Users can disable the features in **Settings > Sidebar > Experimental Sidebar Features**. Features include custom collapsible channel categories, drag and drop to reorganize channels, and unread filtering.

**Enabled (Default Off)**: Users must enable the experimental sidebar features in **Settings**.

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalChannelSidebarOrganization": off`` with options ``off``, ``default_on`` and ``default_off``. |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Sidebar organization
~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. tab:: Mattermost v6.0 onwards

      Deprecated. Not used in Mattermost v6.0 and later.

   .. tab:: Mattermost v5.39 and earlier

      *Not available in Mattermost Cloud*

      This setting applies to the legacy sidebar only. You must enable the `Enable Legacy Sidebar </configure/configuration-settings.html#enable-legacy-sidebar>`__ configuration setting to see and enable this functionality in the System Console.

      .. note::

         This experimental setting is not recommended for production environments. The new channel sidebar matches and exceeds the feature set offered by this configuration setting.

      We strongly recommend that you leave the **Enable Legacy Sidebar** configuration setting disabled so users can access new channel sidebar features, including custom, collapsible channel categories, drag and drop, unread filtering, channel sorting options, and more. See `the channel sidebar documentation </messaging/organizing-your-sidebar.html#organizing-your-sidebar>`__ for more information about these features.

      **True**: Enables channel sidebar organization options in **Settings > Sidebar > Channel grouping and sorting**. Includes options for grouping unread channels, sorting channels by most recent post, and combining all channel types into a single list.

      **False**: Hides the channel sidebar organization options in **Settings > Sidebar > Channel grouping and sorting**.

      +-----------------------------------------------------------------------------------------------------------------------------+
      | This feature's ``config.json`` setting is ``"ExperimentalChannelOrganization": false`` with options ``true`` and ``false``. |
      +-----------------------------------------------------------------------------------------------------------------------------+

Enable X to leave channels from left hand sidebar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. tab:: Mattermost v6.0 onwards

      Deprecated. Not used in Mattermost v6.0 and later.

   .. tab:: Mattermost v5.39 and earlier

      *Not available in Mattermost Cloud*

      This setting applies to the legacy sidebar only. You must first enable the `Enable Legacy Sidebar </configure/configuration-settings.html#enable-legacy-sidebar>`__ configuration setting if you want to see and enable this functionality in the System Console.

      .. note::

         This experimental setting is not recommended for production environments. The new channel sidebar matches and exceeds the feature set offered by this configuration setting.

      We strongly recommend that you leave the **Enable Legacy Sidebar** configuration setting disabled so users can access new channel sidebar features, including custom, collapsible channel categories, drag and drop, unread filtering, channel sorting options, and more. See `the channel sidebar documentation </messaging/organizing-your-sidebar.html>`_ for more information about these features.

      **True**: Users can leave public and private channels by clicking the "x" beside the channel name.

      **False**: Users must use the **Leave Channel** option from the channel menu to leave channels.

      +---------------------------------------------------------------------------------------------------------------------------+
      | This feature's ``config.json`` setting is ``"EnableXToLeaveChannelsFromLHS": false`` with options ``true`` and ``false``. |
      +---------------------------------------------------------------------------------------------------------------------------+

Autoclose direct messages in sidebar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. tab:: Mattermost v6.0 onwards

      Deprecated. Not used in Mattermost v6.0 and later.

   .. tab:: Mattermost v5.39 and earlier

      *Not available in Mattermost Cloud*

      This setting applies to the legacy sidebar only. You must enable the `Enable Legacy Sidebar </configure/configuration-settings.html#enable-legacy-sidebar>`__ configuration setting to see and enable this functionality in the System Console.

      .. note::

         This experimental setting is not recommended for production environments. The new channel sidebar matches and exceeds the feature set offered by this configuration setting.

      We strongly recommend that you leave the **Enable Legacy Sidebar** configuration setting disabled so users can access new channel sidebar features, including custom, collapsible channel categories, drag and drop, unread filtering, channel sorting options, and more. See `the channel sidebar documentation </messaging/organizing-your-sidebar.html>`_ for more information about these features.

      **True**: By default, direct message conversations with no activity for 7 days will be hidden from the sidebar. Users can disable this in **Settings > Sidebar**.

      **False**: Conversations remain in the sidebar until they are manually closed.

      +-----------------------------------------------------------------------------------------------------------------------+
      | This feature's ``config.json`` setting is ``"CloseUnusedDirectMessages": false`` with options ``true`` and ``false``. |
      +-----------------------------------------------------------------------------------------------------------------------+

----

Town Square channel settings
-----------------------------

Town Square is hidden in left hand sidebar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. tab:: Mattermost v6.0 onwards

      Deprecated. Not used in Mattermost v6.0 and later.

   .. tab:: Mattermost v5.39 and earlier

      .. raw:: html

       <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

      This setting applies to the legacy sidebar only. You must enable the `Enable Legacy Sidebar </configure/configuration-settings.html#enable-legacy-sidebar>`__ configuration setting to see and enable this functionality in the System Console.

      .. note::

         This experimental setting is not recommended for production environments. The new channel sidebar matches and exceeds the feature set offered by this configuration setting.

      We strongly recommend that you leave the **Enable Legacy Sidebar** configuration setting disabled so users can access new channel sidebar features, including custom, collapsible channel categories, drag and drop, unread filtering, channel sorting options, and more. See `the channel sidebar documentation </messaging/organizing-your-sidebar.html>`_ for more information about these features.

      **True**: Hides Town Square in the left-hand sidebar if there are no unread messages in the channel.

      **False**: Town Square is always visible in the left-hand sidebar even if all messages have been read.

      +-----------------------------------------------------------------------------------------------------------------------------+
      | This feature's ``config.json`` setting is ``"ExperimentalHideTownSquareinLHS": false`` with options ``true`` and ``false``. |
      +-----------------------------------------------------------------------------------------------------------------------------+

Town Square is read-only
~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. tab:: Mattermost v6.0 onwards

      In Mattermost v.6.0, this feature has been deprecated in favor of `channel moderation </manage/team-channel-members.html#channel-moderation>`__ which allows you to set any channel as read-only, including Town Square.

   .. tab:: Mattermost v5.39 and earlier

      .. raw:: html

       <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

      **True**: Only System Admins can post in Town Square. Other members are not able to post, reply, upload files, react using emojis,  pin messages to Town Square, nor are they able to change the channel name, header, or purpose.

      **False**: Anyone can post in Town Square.

      +------------------------------------------------------------------------------------------------------------------------------+
      | This feature's ``config.json`` setting is ``"ExperimentalTownSquareIsReadOnly": false`` with options ``true`` and ``false``. |
      +------------------------------------------------------------------------------------------------------------------------------+

----

Custom emoji settings
---------------------

Restrict custom emoji creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. tab:: Mattermost v6.0 onwards

      Deprecated. Not used in Mattermost v6.0 and later.

   .. tab:: Mattermost v5.39 and earlier

      After upgrading to v4.9 (released April 16th, 2018) or later, changing the ``config.json`` value no longer has an effect because this setting has been migrated to the database. This setting can be modified using the System Console user interface.

      .. raw:: html

       <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

      **Allow everyone to create custom emoji**: Allows everyone to add custom emojis from the emoji picker.

      **Allow System and Team Admins to create custom emoji**: The **Custom Emoji** option is hidden from the emoji picker for users who are not System or Team Admins.

      **Only allow System Admins to create custom emoji**: The **Custom Emoji** option is hidden from the emoji picker for users who are not System Admins.

      +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | This feature's ``config.json`` setting is ``"RestrictCustomEmojiCreation": "all"`` with options ``"all"``, ``"admin"``, and ``"system_admin"`` for the above settings, respectively. |
      +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

Timezone settings
-----------------

Timezone
~~~~~~~~

*This configuration setting has been promoted to General Availability and is no longer configurable in Mattermost v6.0 and later.*

Select the timezone used for timestamps in the user interface and email notifications.

**True**: The **Timezone** setting is visible in the Settings and a timezone is automatically assigned in the next active session.

**False**: The **Timezone** setting is hidden in the Settings.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalTimezone": true`` with options ``true`` and ``false``.  |
+------------------------------------------------------------------------------------------------------------------+

----

High availability settings
--------------------------

Inter-node listen address
~~~~~~~~~~~~~~~~~~~~~~~~~

*Deprecated. Not used in Mattermost v4.0 and later*

The address the Mattermost Server will listen on for inter-node communication. When setting up your network you should secure the listen address so that only machines in the cluster have access to that port. This can be done in different ways, for example, using IPsec, security groups, or routing tables.

+-----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"InterNodeListenAddress": ":8075"`` with string input.  |
+-----------------------------------------------------------------------------------------------------+

Inter-Node URLs
~~~~~~~~~~~~~~~

*Deprecated. Not used in Mattermost v4.0 and later*

A list of all the machines in the cluster, such as ``["http://10.10.10.2", "http://10.10.10.4"]``. It is recommended to use the internal IP addresses so all the traffic can be secured.

+--------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"InterNodeUrls": []`` with string array input consisting of the machines in the cluster. |
+--------------------------------------------------------------------------------------------------------------------------------------+

----

REST API V3 settings
--------------------

Allow use of API v3 endpoints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

Set to ``false`` to disable all version 3 endpoints of the REST API. Integrations that rely on API v3 will fail and can then be identified for migration to API v4. API v3 is deprecated and will be removed in the near future. See https://api.mattermost.com for details.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAPIv3": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+

----

Integrations settings
---------------------

Restrict managing integrations to Admins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

   .. tab:: Mattermost v6.0 onwards

      Deprecated. Not used in Mattermost v6.0 and later.

   .. tab:: Mattermost v5.39 and earlier

      After upgrading to v4.9 (released April 16th, 2018) or later, changing the ``config.json`` value no longer has an effect because this setting has been migrated to the database. This setting can be modified using the System Console user interface.

      .. raw:: html

       <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

**True**: Webhooks and slash commands can only be created, edited, and viewed by Team and System Admins, and OAuth 2.0 applications by System Admins. Integrations are available to all users after they have been created by the Admin.

**False**: Any team members can create webhooks, slash commands` and OAuth 2.0 applications from **Product menu > Integrations**.

.. note::
  OAuth 2.0 applications can be authorized by all users if they have the **Client ID** and **Client Secret** for an app setup on the server.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOnlyAdminIntegrations": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

Patch React DOM used by plugins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Deprecated. Not used in Mattermost v8.0 and later*

This setting enables the patching of the React DOM library when loading web app plugins so that the plugin uses the version matching the web app. This should only be needed temporarily after upgrading to Mattermost v7.7 for plugins that have not been updated yet. Changes to this setting require a server restart before taking effect.

See the `Important Upgrade Notes <https://docs.mattermost.com/upgrade/important-upgrade-notes.html>`__ for more information.

**True**: Web app plugins that package their own version of React DOM are patched to instead use the version of React DOM provided by the web app.

**False**: Web app plugins are loaded as normal.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PatchPluginsReactDOM": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

----

Permission policy settings
--------------------------

*Removed in June 16, 2018 release*

.. note::

   Permission policy settings are available in Enterprise Edition E10 and E20. From v5.0, these settings are found in the `Advanced Permissions </onboard/advanced-permissions.html>`__ page instead of configuration settings.

Enable sending team invites from
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the `Advanced Permissions documentation </onboard/advanced-permissions.html>`_ for more details.

Set policy on who can invite others to a team using the **Send Email Invite**, **Get Team Invite Link**, and **Add Members to Team** options on the product menu. If **Get Team Invite Link** is used to share a link, you can expire the invite code from **Team Settings > Invite Code** after the desired users have joined the team. Options include:

**All team members**: Allows any team member to invite others using an email invitation, team invite link, or by adding members to the team directly.

**Team and System Admins**: Hides the email invitation, team invite link, and the add members to team buttons in the product menu from users who are not Team Admins or System Admins.

**System Admins**: Hides the email invitation, team invite link, and add members to team buttons in the product menu from users who are not System Admins.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictTeamInvite": "all"`` with options ``"all"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable public channel creation for
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the `Advanced Permissions documentation </onboard/advanced-permissions.html>`_ for more details.

Restrict the permission level required to create public channels.

**All team members**: Allow all team members to create public channels.

**Team Admins and System Admins**: Restrict creating public channels to Team Admins and System Admins.

**System Admins**: Restrict creating public channels to System Admins.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPublicChannelCreation": "all"`` with options ``"all"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable public channel renaming for
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the `Advanced Permissions documentation </onboard/advanced-permissions.html>`_ for more details.

Restrict the permission level required to rename and set the header or purpose for Public channels.

**All channel members**: Allow all channel members to rename Public channels.

**Channel Admins, Team Admins, and System Admins**: Restrict renaming public channels to Channel Admins, Team Admins, and System Admins who are members of the channel.

**Team Admins and System Admins**: Restrict renaming public channels to Team Admins and System Admins who are members of the channel.

**System Admins**: Restrict renaming public channels to System Admins who are members of the channel.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPublicChannelManagement": "all"`` with options ``"all"``, ``"channel_admin"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable public channel deletion for
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the `Advanced Permissions documentation </onboard/advanced-permissions.html>`_ for more details.

Restrict the permission level required to delete Public channels. Deleted channels can be recovered from the database using a `command line tool </manage/command-line-tools.html>`__.

**All channel members**: Allow all channel members to delete public channels.

**Channel Admins, Team Admins, and System Admins**: Restrict deleting public channels to Channel Admins, Team Admins, and System Admins who are members of the channel.

**Team Admins and System Admins**: Restrict deleting public channels to Team Admins and System Admins who are members of the channel.

**System Admins**: Restrict deleting public channels to System Admins who are members of the channel.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPublicChannelDeletion": "all"`` with options ``"all"``, ``"channel_admin"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable private channel creation for
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the `Advanced Permissions documentation </onboard/advanced-permissions.html>`_ for more details.

Restrict the permission level required to create private channels.

**All team members**: Allow all team members to create private channels.

**Team Admins and System Admins**: Restrict creating private channels to Team Admins and System Admins.

**System Admins**: Restrict creating private channels to System Admins.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPrivateChannelCreation": "all"`` with options ``"all"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable private channel renaming for
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the `Advanced Permissions documentation </onboard/advanced-permissions.html>`_ for more details.

Restrict the permission level required to rename and set the header or purpose for Private channels.

**All channel members**: Allow all channel members to rename private channels.

**Channel Admins, Team Admins, and System Admins**: Restrict renaming private channels to Channel Admins, Team Admins, and System Admins who are members of the private channel.

**Team Admins and System Admins**: Restrict renaming private channels to Team Admins and System Admins who are members of the private channel.

**System Admins**: Restrict renaming private channels to System Admins who are members of the private channel.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPrivateChannelManagement": "all"`` with options ``"all"``, ``"channel_admin"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable managing of private channel members for
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the `Advanced Permissions documentation </onboard/advanced-permissions.html>`_ for more details.

Set policy on who can add and remove members from Private channels.

**All team members**: Allow all team members to add and remove members.

**Team Admins, Channel Admins, and System Admins**: Allow only Team Admins, Channel Admins, and System Admins to add and remove members.

**Team Admins, and System Admins**: Allow only Team Admins and System Admins to add and remove members.

**System Admins**: Allow only System Admins to add and remove members.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPrivateChannelManageMembers": "all"`` with options ``"all"``, ``"channel_admin"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable private channel deletion for
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the `Advanced Permissions documentation </onboard/advanced-permissions.html>`_ for more details.

Restrict the permission level required to delete Private channels. Deleted channels can be recovered from the database using a `command line tool </manage/command-line-tools.html>`__.

**All channel members**: Allow all channel members to delete private channels.

**Channel Admins, Team Admins, and System Admins**: Restrict deleting private channels to Channel Admins, Team Admins, and System Admins who are members of the Private channel.

**Team Admins and System Admins**: Restrict deleting private channels to Team Admins and System Admins who are members of the Private channel.

**System Admins**: Restrict deleting private channels to System Admins who are members of the private channel.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPrivateChannelDeletion": "all"`` with options ``"all"``, ``"channel_admin"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Allow which users to delete messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the `Advanced Permissions documentation </onboard/advanced-permissions.html>`_ for more details.

Restrict the permission level required to delete messages. Team Admins, Channel Admins, and System Admins can delete messages only in channels where they are members. Messages can be deleted any time.

**Message authors can delete their own messages, and Administrators can delete any message**: Allow authors to delete their own messages, and allow Team Admins, Channel Admins, and System Admins to delete any message.

**Team Admins and System Admins**: Allow only Team Admins and System Admins to delete messages.

**System Admins**: Allow only System Admins to delete messages.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPostDelete": "all"`` with options ``"all"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Allow users to edit their messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the `Advanced Permissions documentation </onboard/advanced-permissions.html>`_ for more details.

Set the time limit that users have to edit their messages after posting.

**Any time**: Allow users to edit their messages at any time after posting.

**Never**: Do not allow users to edit their messages.

**{n} seconds after posting**: Users can edit their messages within the specified time limit after posting. The time limit is applied using the ``config.json`` setting ``PostEditTimeLimit`` described below.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowEditPost": "always"`` with options ``"always"``, ``"never"``, and ``"time_limit"`` for the above settings, respectively. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Post edit time limit
~~~~~~~~~~~~~~~~~~~~

When post editing is permitted, setting this to ``-1`` allows editing any time, and setting this to a positive integer restricts editing time in seconds. If post editing is disabled, this setting does not apply.

**Note:** This setting does not affect plugins, shared channels, integration actions, or Mattermost products.

+--------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PostEditTimeLimit": -1`` with numerical input.      |
+--------------------------------------------------------------------------------------------------+

----

Image settings
--------------

Attachment thumbnail width
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in July 16th, 2017 release*

Width of thumbnails generated from uploaded images. Updating this value changes how thumbnail images render in future, but does not change images created in the past.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ThumbnailWidth": 120`` with numerical input. |
+-------------------------------------------------------------------------------------------+

Attachment thumbnail height
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in July 16th, 2017 release*

Height of thumbnails generated from uploaded images. Updating this value changes how thumbnail images render in future, but does not change images created in the past.

+--------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ThumbnailHeight": 100`` with numerical input. |
+--------------------------------------------------------------------------------------------+

Image preview width
~~~~~~~~~~~~~~~~~~~

*Removed in July 16th, 2017 release*

Maximum width of preview image. Updating this value changes how preview images render in future, but does not change images created in the past.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PreviewWidth": 1024`` with numerical input. |
+------------------------------------------------------------------------------------------+

Image preview height
~~~~~~~~~~~~~~~~~~~~

*Removed in July 16th, 2017 release*

Maximum height of preview image. Setting this value to ``0`` instructs Mattermost to auto-size the preview image height based on the source image aspect ratio and the preview image width. Updating this value changes how preview images render in future, but does not change images created in the past.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PreviewHeight": 0`` with numerical input. |
+----------------------------------------------------------------------------------------+

Profile picture width
~~~~~~~~~~~~~~~~~~~~~

*Removed in July 16th, 2017 release*

The width to which profile pictures are resized after being uploaded via **Account Settings > Profile**.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ProfileWidth": 128`` with numerical input. |
+-----------------------------------------------------------------------------------------+

Profile picture height
~~~~~~~~~~~~~~~~~~~~~~

*Removed in July 16th, 2017 release*

The height to which profile pictures are resized after being uploaded via **Account Settings > Profile**.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ProfileHeight": 128`` with numerical input. |
+------------------------------------------------------------------------------------------+

----

Experimental display settings
-----------------------------

Supported timezones path
~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in April 16, 2019 release*

Set the path of the JSON file that lists supported timezones when ``ExperimentalTimezone`` is set to ``true``.

The file must be in the same directory as your ``config.json`` file if you set a relative path. Defaults to ``timezones.json``.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SupportedTimezonesPath": "timezones.json"`` with string input.     |
+-----------------------------------------------------------------------------------------------------------------+

----

Other deprecated settings
--------------------------

Disable Post Metadata
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Disabling post metadata is only recommended if you are experiencing a significant decrease in performance around channel and post load times.

**False**: Load channels with more accurate scroll positioning by loading post metadata.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DisablePostMetadata": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------+

Enable AD/LDAP group sync
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

**True**: Enables AD/LDAP Group Sync configurable under **User Management > Groups**.

**False**: Disables AD/LDAP Group Sync and removes **User Management > Groups** from the System Console.

For more information on AD/LDAP Group Sync, please see the `AD/LDAP Group Sync documentation <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`__.

+-----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalLdapGroupSync": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------------+

Disable inactive server email notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

This configuration setting disables the ability to send inactivity email notifications to Mattermost System Admins.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableInactivityEmail": true`` with options ``true`` and ``false``.  |
+-------------------------------------------------------------------------------------------------------------------+