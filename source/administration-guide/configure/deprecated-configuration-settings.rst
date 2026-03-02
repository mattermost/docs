Deprecated configuration settings
=================================

The following Mattermost configuration settings are deprecated and are no longer supported in current Mattermost releases:

- `Bleve settings <#bleve-settings>`__
- `Elasticsearch settings <#elasticsearch-settings>`__
- `Service settings <#service-settings>`__
- `Database settings <#database-settings>`__
- `Data retention settings <#data-retention-settings>`__
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
- `Experimental API endpoint settings <#experimental-api-endpoint-settings>`__
- `Shared channels settings <#shared-channels-settings>`__
- `User satisfaction survey plugin settings <#user-satisfaction-surveys-plugin-settings>`__
- `Other deprecated settings <#other-deprecated-settings>`__

----

Bleve settings
--------------

*Bleve search has been deprecated from Mattermost v11.0. We recommend using Elasticsearch or OpenSearch for enterprise search capabilities.*

Enable Bleve indexing
~~~~~~~~~~~~~~~~~~~~~

*Deprecated from Mattermost v11.0*

This setting was available in the System Console by going to **Experimental > Bleve**, or by editing the ``config.json`` file.

**True**: The indexing of new posts occurs automatically.

**False**: The indexing of new posts does not occur automatically.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableIndexing": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

Index directory
~~~~~~~~~~~~~~~

*Deprecated from Mattermost v11.0*

This setting was available in the System Console by going to **Experimental > Bleve**, or by editing the ``config.json`` file.

Directory path to use for storing bleve indexes.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IndexDir": ""`` with string input.                           |
+-----------------------------------------------------------------------------------------------------------+

Bulk index now
~~~~~~~~~~~~~~

Select **Index Now** to index all users, channels, and posts in the database from oldest to newest. Bleve is available during indexing, but search results may be incomplete until the indexing job is complete.

Purge indexes
~~~~~~~~~~~~~

Select **Purge Index** to remove the contents of the Bleve index directory. Search results may be incomplete until a bulk index of the existing database is rebuilt.

.. config:setting:: enable-bleve-indexingsearch
  :displayname: Enable Bleve for search queries (Experimental)
  :systemconsole: Experimental > Bleve
  :configjson: EnableSearching
  :environment: N/A

  - **true**: Search queries will use bleve search.
  - **false**: **(Default)** Search queries will not use bleve search.


Enable Bleve for search queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Deprecated from Mattermost v11.0*

This setting was available in the System Console by going to **Experimental > Bleve**, or by editing the ``config.json`` file.

**True**: Search queries will use bleve search.

**False**: Search queries will not use bleve search.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSearching": false`` with options ``true`` and ``false``.  |
+--------------------------------------------------------------------------------------------------------------+

Enable Bleve for autocomplete queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Deprecated from Mattermost v11.0*

This setting was available in the System Console by going to **Experimental > Bleve**, or by editing the ``config.json`` file.

**True**: Autocomplete queries will use bleve search.

**False**: Autocomplete queries will not use bleve search.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAutocomplete": false`` with options ``true`` and ``false``.  |
+-----------------------------------------------------------------------------------------------------------------+

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

Deprecated. Not used in Mattermost v6.0 and later.

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

Data retention settings
-----------------------

MessageRetentionDays
~~~~~~~~~~~~~~~~~~~~

*Deprecated in Mattermost v9.5 release in favor of MessageRetentionHours*

Set how long Mattermost keeps messages across all teams and channels. This setting doesn't apply to custom retention policies. The minimum time is 1 hour.

From Mattermost v9.5, this setting has been replaced by :ref:`MessageRetentionHours <administration-guide/configure/compliance-configuration-settings:global retention policy for messages>` which provides more granular control over message retention periods.

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MessageRetentionDays": 365`` with numerical input.                                     |
+-------------------------------------------------------------------------------------------------------------------------------------+

FileRetentionDays
~~~~~~~~~~~~~~~~~

*Deprecated in Mattermost v9.5 release in favor of FileRetentionHours*

Set how long Mattermost keeps files across all teams and channels. This setting doesn't apply to custom retention policies. The minimum time is 1 hour.

From Mattermost v9.5, this setting has been replaced by :ref:`FileRetentionHours <administration-guide/configure/compliance-configuration-settings:global retention policy for files>` which provides more granular control over file retention periods.

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileRetentionDays": 365`` with numerical input.                                        |
+-------------------------------------------------------------------------------------------------------------------------------------+

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

Deprecated. Not used in Mattermost v6.0 and later.

Enable team creation
~~~~~~~~~~~~~~~~~~~~~

Deprecated. Not used in Mattermost v6.0 and later.

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

Deprecated. Not used in Mattermost v6.0 and later.

Experimental sidebar features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Deprecated. Not used in Mattermost v5.32 and later*

.. note::
   This experimental configuration setting has been deprecated, and the ability to organize channels in the sidebar has been promoted to general availability from Mattermost v5.32. See the :doc:`Organizing Your Sidebar documentation </end-user-guide/preferences/customize-your-channel-sidebar>` for details on customizing the sidebar.

**Disabled**: Users cannot access the experimental channel sidebar feature set.

**Enabled (Default On)**: Enables the experimental sidebar features for all users on this server. Users can disable the features in **Settings > Sidebar > Experimental Sidebar Features**. Features include custom collapsible channel categories, drag and drop to reorganize channels, and unread filtering.

**Enabled (Default Off)**: Users must enable the experimental sidebar features in **Settings**.

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalChannelSidebarOrganization": off`` with options ``off``, ``default_on`` and ``default_off``. |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Sidebar organization
~~~~~~~~~~~~~~~~~~~~

Deprecated. Not used in Mattermost v6.0 and later.

Enable X to leave channels from left hand sidebar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deprecated. Not used in Mattermost v6.0 and later.

Autoclose direct messages in sidebar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deprecated. Not used in Mattermost v6.0 and later.

----

Town Square channel settings
-----------------------------

Town Square is hidden in left hand sidebar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deprecated. Not used in Mattermost v6.0 and later.

Town Square is read-only
~~~~~~~~~~~~~~~~~~~~~~~~

From Mattermost v.6.0, this feature has been deprecated in favor of :ref:`advanced access controls <administration-guide/manage/team-channel-members:advanced access controls>` which allows you to set any channel as read-only, including Town Square.

----

Custom emoji settings
---------------------

Restrict custom emoji creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deprecated. Not used in Mattermost v6.0 and later.

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

Use gossip
~~~~~~~~~~~~~~~

*Removed in Mattermost v6.0*

**True**: The server attempts to communicate via the gossip protocol over the gossip port specified.

**False**: The server attempts to communicate over the streaming port.

+--------------------------------------------------------------------------------------------------------------+
| This feature’s config.json setting is ``"UseExperimentalGossip": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

Streaming port
~~~~~~~~~~~~~~~

*Deprecated. Not used in Mattermost v6.0 and later*

The port used for streaming data between servers.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"StreamingPort": ":8075"`` with string input. |
+-------------------------------------------------------------------------------------------+


Maximum idle connections for high availability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Deprecated. Not used in Mattermost v7.0 and later*

+-----------------------------------------------------------------+------------------------------------------------------------------------+
| The maximum number of idle connections held open from one       | - System Config path: N/A                                              |
| server to all others in the cluster.                            | - ``config.json`` setting: ``".ClusterSettings.MaxIdleConns: 100,``    |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_MAXIDLECONNS``            |
| Numerical input. Default is **100**.                            |                                                                        |
+-----------------------------------------------------------------+------------------------------------------------------------------------+

Maximum idle connections per host
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Deprecated. Not used in Mattermost v7.0 and later*

+-----------------------------------------------------------------+------------------------------------------------------------------------------+
| The maximum number of idle connections held open from one       | - System Config path: N/A                                                    |
| server to another server in the cluster.                        | - ``config.json`` setting: ``".ClusterSettings.MaxIdleConnsPerHost: 128",``  |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_MAXIDLECONNSPERHOST``           |
| Numerical input. Default is **128**.                            |                                                                              |
+-----------------------------------------------------------------+------------------------------------------------------------------------------+

Idle connection timeout
~~~~~~~~~~~~~~~~~~~~~~~

*Deprecated. Not used in Mattermost v7.0 and later*

+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| The amount of time, in milliseconds, to leave an idle           | - System Config path: N/A                                                             |
| connection open between servers in the cluster.                 | - ``config.json`` setting: ``".ClusterSettings.IdleConnTimeoutMilliseconds: 90000",`` |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_IDLECONNTIMEOUTMILLISECONDS``            |
| Numerical input. Default is **90000**.                          |                                                                                       |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+

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

Deprecated. Not used in Mattermost v6.0 and later.


Patch React DOM used by plugins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Deprecated. Not used in Mattermost v8.0 and later*

This setting enables the patching of the React DOM library when loading web app plugins so that the plugin uses the version matching the web app. This should only be needed temporarily after upgrading to Mattermost v7.7 for plugins that have not been updated yet. Changes to this setting require a server restart before taking effect.

See the :doc:`Important Upgrade Notes </administration-guide/upgrade/important-upgrade-notes>` for more information.

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

   From Mattermost v5.0, these settings are found in the :doc:`Advanced Permissions </administration-guide/onboard/advanced-permissions>` page instead of configuration settings.

Enable sending team invites from
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the :doc:`Advanced Permissions documentation </administration-guide/onboard/advanced-permissions>` for more details.

Set policy on who can invite others to a team using the **Send Email Invite**, **Get Team Invite Link**, and **Add Members to Team** options on the product menu. If **Get Team Invite Link** is used to share a link, you can expire the invite code from **Team Settings > Invite Code** after the desired users have joined the team. Options include:

**All team members**: Allows any team member to invite others using an email invitation, team invite link, or by adding members to the team directly.

**Team and System Admins**: Hides the email invitation, team invite link, and the add members to team buttons in the product menu from users who are not team admins or system admins.

**System Admins**: Hides the email invitation, team invite link, and add members to team buttons in the product menu from users who are not system admins.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictTeamInvite": "all"`` with options ``"all"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable public channel creation for
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the :doc:`Advanced Permissions documentation </administration-guide/onboard/advanced-permissions>` for more details.

Restrict the permission level required to create public channels.

**All team members**: Allow all team members to create public channels.

**Team Admins and System Admins**: Restrict creating public channels to team admins and system admins.

**System Admins**: Restrict creating public channels to system admins.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPublicChannelCreation": "all"`` with options ``"all"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable public channel renaming for
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the :doc:`Advanced Permissions documentation </administration-guide/onboard/advanced-permissions>` for more details.

Restrict the permission level required to rename and set the header or purpose for Public channels.

**All channel members**: Allow all channel members to rename Public channels.

**Channel Admins, Team Admins, and System Admins**: Restrict renaming public channels to channel admins, team admins, and system admins who are members of the channel.

**Team Admins and System Admins**: Restrict renaming public channels to Team Admins and system admins who are members of the channel.

**System Admins**: Restrict renaming public channels to system admins who are members of the channel.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPublicChannelManagement": "all"`` with options ``"all"``, ``"channel_admin"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable public channel deletion for
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the :doc:`Advanced Permissions documentation </administration-guide/onboard/advanced-permissions>` for more details.

Restrict the permission level required to delete Public channels. Deleted channels can be recovered from the database using a :doc:`command line tool </administration-guide/manage/command-line-tools>`.

**All channel members**: Allow all channel members to delete public channels.

**Channel Admins, Team Admins, and System Admins**: Restrict deleting public channels to channel admins, team admins, and system admins who are members of the channel.

**Team Admins and System Admins**: Restrict deleting public channels to team admins and system admins who are members of the channel.

**System Admins**: Restrict deleting public channels to system admins who are members of the channel.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPublicChannelDeletion": "all"`` with options ``"all"``, ``"channel_admin"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable private channel creation for
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the :doc:`Advanced Permissions documentation </administration-guide/onboard/advanced-permissions>` for more details.

Restrict the permission level required to create private channels.

**All team members**: Allow all team members to create private channels.

**Team Admins and System Admins**: Restrict creating private channels to team admins and system admins.

**System Admins**: Restrict creating private channels to system admins.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPrivateChannelCreation": "all"`` with options ``"all"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable private channel renaming for
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the :doc:`Advanced Permissions documentation </administration-guide/onboard/advanced-permissions>` for more details.

Restrict the permission level required to rename and set the header or purpose for Private channels.

**All channel members**: Allow all channel members to rename private channels.

**Channel Admins, Team Admins, and System Admins**: Restrict renaming private channels to channel admins, team admins, and system admins who are members of the private channel.

**Team Admins and System Admins**: Restrict renaming private channels to team admins and system admins who are members of the private channel.

**System Admins**: Restrict renaming private channels to system admins who are members of the private channel.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPrivateChannelManagement": "all"`` with options ``"all"``, ``"channel_admin"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable managing of private channel members for
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the :doc:`Advanced Permissions documentation </administration-guide/onboard/advanced-permissions>` for more details.

Set policy on who can add and remove members from Private channels.

**All team members**: Allow all team members to add and remove members.

**Team Admins, Channel Admins, and System Admins**: Allow only team admins, channel admins, and system admins to add and remove members.

**Team Admins, and System Admins**: Allow only team admins and system admins to add and remove members.

**System Admins**: Allow only system admins to add and remove members.

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPrivateChannelManageMembers": "all"`` with options ``"all"``, ``"channel_admin"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable private channel deletion for
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the :doc:`Advanced Permissions documentation </administration-guide/onboard/advanced-permissions>` for more details.

Restrict the permission level required to delete Private channels. Deleted channels can be recovered from the database using a :doc:`command line tool </administration-guide/manage/command-line-tools>`.

**All channel members**: Allow all channel members to delete private channels.

**Channel Admins, Team Admins, and System Admins**: Restrict deleting private channels to channel admins, team admins, and system admins who are members of the Private channel.

**Team Admins and System Admins**: Restrict deleting private channels to Team Admins and system admins who are members of the Private channel.

**System Admins**: Restrict deleting private channels to system admins who are members of the private channel.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPrivateChannelDeletion": "all"`` with options ``"all"``, ``"channel_admin"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Allow which users to delete messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the :doc:`Advanced Permissions documentation </administration-guide/onboard/advanced-permissions>` for more details.

Restrict the permission level required to delete messages. Team admins, channel admins, and system admins can delete messages only in channels where they are members. Messages can be deleted any time.

**Message authors can delete their own messages, and Administrators can delete any message**: Allow authors to delete their own messages, and allow team admins, channel admins, and system admins to delete any message.

**Team Admins and System Admins**: Allow only team admins and system admins to delete messages.

**System Admins**: Allow only system admins to delete messages.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictPostDelete": "all"`` with options ``"all"``, ``"team_admin"``, and ``"system_admin"`` for the above settings, respectively. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Allow users to edit their messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in June 16, 2018 release*

.. note::

   From v5.0 this has been replaced by advanced permissions which offers Admins a way to restrict actions in Mattermost to authorized users only. See the :doc:`Advanced Permissions documentation </administration-guide/onboard/advanced-permissions>` for more details.

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

Shared channels settings
------------------------

Enable remote cluster service (Experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deprecated in November 16th, 2024 release in favor of :ref:`Connected Workspaces <administration-guide/configure/site-configuration-settings:enable connected workspaces>` configuration settings

This setting isn't available in the System Console and can only be set in ``config.json``.

Enable this setting to add, remove, and view remote clusters for shared channels.

**True**: System admins can manage remote clusters using the System Console.

**False**: (**Default**) Remote cluster management is disabled.

+---------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalSettings.EnableRemoteClusters": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------------------------------+

Enable shared channels (Experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deprecated in November 16th, 2024 release in favor of :ref:`Connected Workspaces <administration-guide/configure/site-configuration-settings:enable connected workspaces>` configuration settings

This setting isn't available in the System Console and can only be set in ``config.json``.

Enable the ability to establish secure connections between Mattermost instances, and invite secured connections to shared channels where secure connections can participate as they would in any public and private channel.

**True**: System admins can establish secure connections between Mattermost instances.

**False**: (**Default**) The ability to establish secure connections is disabled.

+---------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalSettings.EnableSharedChannels": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------------------------------+

----

User satisfaction surveys plugin settings
-----------------------------------------

.. important::

   This plugin is deprecated from Mattermost v10.11, and is no longer included as a pre-packaged plugin for new Mattermost deployments. For new installations, we strongly recommend using the :doc:`Mattermost User Survey integration </administration-guide/configure/manage-user-surveys>` instead.

This plugin enables Mattermost to send user satisfaction surveys to gather feedback and improve product quality directly from your Mattermost users. Please refer to the `Mattermost Privacy Policy <https://mattermost.com/privacy-policy/>`__ for more information on the collection and use of information received through Mattermost services.

Access the following configuration settings in the System Console by going to **Plugins > User Satisfaction Surveys**.

.. config:setting:: enable-plugin
  :displayname: Enable plugin (Plugins - User Satisfaction Surveys)
  :systemconsole: Plugins > User Satisfaction Surveys
  :configjson: PluginSettings.PluginStates.com.mattermost.user-survey.Enable
  :environment: N/A

  - **true**: (Default) Enables the Mattermost User Satisfaction Surveys plugin on your Mattermost workspace.
  - **false**: Disables the Mattermost User Satisfaction Surveys plugin on your Mattermost workspace.

Enable plugin
~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| - **true**: (Default) Enables the Mattermost User Satisfaction Surveys plugin on your Mattermost workspace.   | - System Config path: **Plugins > User Satisfaction Surveys**                                |
| - **false**: Disables the Mattermost User Satisfaction Surveys plugin on your Mattermost workspace.           | - ``config.json`` setting: ``PluginSettings.PluginStates.com.mattermost.user-survey.Enable`` |
|                                                                                                               | - Environment variable: N/A                                                                  |
+---------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+

.. config:setting:: enable-pluginsend
  :displayname: Enable user satisfaction survey (Plugins - User Satisfaction Surveys)
  :systemconsole: Plugins > User Satisfaction Surveys
  :configjson: PluginSettings.PluginStates.com.mattermost.user-survey.Enable
  :environment: N/A

  - **true**: A user satisfaction survey is sent to all users every quarter.
  - **false**: (Default) User satisfaction surveys are disabled.

Enable user satisfaction survey
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| - **true**: A survey is sent to all users every quarter. Results are used by Mattermost, Inc. to improve the product.       | - System Config path: **Plugins > User Satisfaction Surveys**                                                      |
| - **false**: (Default) User satisfaction surveys are disabled.                                                              | - ``config.json`` setting: ``PluginSettings.Plugins.com.mattermost.user-survey.systemconsolesetting.EnableSurvey`` |
|                                                                                                                             | - Environment variable: N/A                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| **Note**: See the `Mattermost Privacy Policy <https://mattermost.com/privacy-policy/>`__ for more information on the collection and use of information by Mattermost.                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

----

Other deprecated settings
--------------------------

Disable Post Metadata
~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Disabling post metadata is only recommended if you are experiencing a significant decrease in performance around channel and post load times.

**False**: Load channels with more accurate scroll positioning by loading post metadata.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DisablePostMetadata": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------+

Enable AD/LDAP group sync
~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Enables AD/LDAP Group Sync configurable under **User Management > Groups**.

**False**: Disables AD/LDAP Group Sync and removes **User Management > Groups** from the System Console.

For more information on AD/LDAP Group Sync, please see the :doc:`AD/LDAP Group Sync documentation </administration-guide/onboard/ad-ldap-groups-synchronization>`.

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

Disable Apps Bar
~~~~~~~~~~~~~~~~

This setting is enabled for all customers by default from Mattermost v8.0. This setting disables the Apps Bar and moves all Mattermost integration icons from the vertical pane on the far right back to the channel header.

Enable OpenTracing (Experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Removed in March 16, 2025 release*

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: A Jaeger client is instantiated and is used to trace each HTTP request as it goes through App and Store layers. Context is added to App and Store and is passed down the layer chain to create OpenTracing 'spans'.

By default, in order to avoid leaking sensitive information, no method parameters are reported to OpenTracing. Only the name of the method is reported.

**False**: OpenTracing is not enabled.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOpenTracing": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+