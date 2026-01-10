Audit Log JSON Schema
==============================

.. include:: ../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

The audit log JSON schema functions as a standardized blueprint or schematic that consistently defines how a single event should appear when being written to the audit log, including: field names, data types, objects, and structure.

An outline of the JSON audit logging schema is provided below. See the `JSON data model <#json-data-model>`__ for additional details.

.. code-block:: json

    {
        "timestamp": "",       // Event time
        "status": "",          // Success or failure of the audited event or activity
        "event_name": "",      // Logged event name
        "error": {             // Error if status = fail
            "status_code": 0,
            "description": ""
        },
        "actor": {             // The user performing the action
            "user_id": ""           // Unique identifier of the event user
            "session_id": ""        // Unique session identifier of the event user
            "client": ""            // User agent of the client/platform in use by the event user
            "ip_address": ""        // IPv4/IPv6 IP address of the event user
        },
        "event": {             // Event-specific data
            "parameters": {}        // Map containing parameters of the audited event or activity
            "prior_state": {}       // Pre-event state of the object
            "resulting_state": {}   // Post-event state of the object
            "object_type": ""       // Object targeted by the event or activity
        },
        "meta": {
            "api_path": "",         // API endpoint interacted with for event or activity
            "cluster_id": ""        // Unique identifier of the cluster in use by the event user
        }
    }


Audit log record examples
-------------------------

Update user preferences
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

    {
        "timestamp": "2022-08-17 20:37:52.846 +01:00",
        "event_name": "updatePreferences",
        "status": "success",
        "actor": {
            "user_id": "aw8ehkwaziytzry1qqxi9tsqwh",
            "session_id": "kth3jyadc3b1p84kbz6y3o75na",
            "client": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15",
            "ip_address": "192.168.0.169"
        },
        "event": {
            "parameters": {},
            "prior_state": {},
            "resulting_state": {},
            "object_type": ""
        },
        "meta": {
            "api_path": "/api/v4/users/aw8ehkwaziytzry1qqxi9tsqwh/preferences",
            "cluster_id": "8dxdbfx6fpdwtki1z6n8whtkho"
        },
        "error": {}
    }

Create post
~~~~~~~~~~~

.. code-block:: json

    {
        "timestamp": "2025-04-30 16:17:44.207 Z",
        "event_name": "createPost",
        "status": "success",
        "actor": {
            "user_id": "i764hi6h5bbz8p1955ed4ahj6y",
            "session_id": "t7894ft76igtpb788nkkej1yoy",
            "client": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            "ip_address": "172.19.0.8"
        },
        "event": {
            "parameters": {
                "post": {
                    "channel_id": "pfis7ycuy78o7m3zebajmxqeuo",
                    "user_id": "i764hi6h5bbz8p1955ed4ahj6y",
                    "message": "Sample post content"
                }
            },
            "prior_state": {},
            "resulting_state": {
                "channel_id": "pfis7ycuy78o7m3zebajmxqeuo",
                "create_at": 1746029864145,
                "id": "xpw97hf6kfncirzhqisb5sym7e",
                "user_id": "i764hi6h5bbz8p1955ed4ahj6y"
            },
            "object_type": "post"
        },
        "meta": {
            "api_path": "/api/v4/posts",
            "cluster_id": "i5twhjm3ainatcifiy3oksshae"
        },
        "error": {}
    }

System configuration change
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

    {
        "timestamp": "2025-04-30 16:18:30.803 Z",
        "event_name": "patchConfig",
        "status": "success",
        "actor": {
            "user_id": "i764hi6h5bbz8p1955ed4ahj6y",
            "session_id": "t7894ft76igtpb788nkkej1yoy",
            "client": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            "ip_address": "172.19.0.8"
        },
        "event": {
            "parameters": {},
            "prior_state": {
                "config_diffs": [
                    {
                        "actual_val": false,
                        "base_val": true,
                        "path": "MetricsSettings.EnableClientMetrics"
                    }
                ]
            },
            "resulting_state": {},
            "object_type": "config"
        },
        "meta": {
            "api_path": "/api/v4/config/patch",
            "cluster_id": "i5twhjm3ainatcifiy3oksshae"
        },
        "error": {}
    }

Audit event types
-----------------

The following tables list the comprehensive audit event types (``event_name`` values) that are captured in Mattermost audit logs:

User Management Events
~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------+-------------------------------------------------------------------+
| **Event Name**                      | **Description**                                                   |
+=====================================+===================================================================+
| ``attachDeviceId``                  | Attaching device IDs to user sessions                             |
+-------------------------------------+-------------------------------------------------------------------+
| ``createUser``                      | Creating new user accounts                                        |
+-------------------------------------+-------------------------------------------------------------------+
| ``createUserAccessToken``           | Creating user access tokens                                       |
+-------------------------------------+-------------------------------------------------------------------+
| ``deleteUser``                      | Deleting user accounts                                            |
+-------------------------------------+-------------------------------------------------------------------+
| ``demoteUserToGuest``               | Demoting users to guest status                                    |
+-------------------------------------+-------------------------------------------------------------------+
| ``disableUserAccessToken``          | Disabling user access tokens                                      |
+-------------------------------------+-------------------------------------------------------------------+
| ``enableUserAccessToken``           | Enabling user access tokens                                       |
+-------------------------------------+-------------------------------------------------------------------+
| ``followThreadByUser``              | Following message threads by user                                 |
+-------------------------------------+-------------------------------------------------------------------+
| ``getUserAudits``                   | Retrieving user audit logs                                        |
+-------------------------------------+-------------------------------------------------------------------+
| ``login``                           | User login events                                                 |
+-------------------------------------+-------------------------------------------------------------------+
| ``logout``                          | User logout events                                                |
+-------------------------------------+-------------------------------------------------------------------+
| ``migrateAuthToLdap``               | Migrating user authentication to LDAP                             |
+-------------------------------------+-------------------------------------------------------------------+
| ``migrateAuthToSaml``               | Migrating user authentication to SAML                             |
+-------------------------------------+-------------------------------------------------------------------+
| ``patchUser``                       | Updating user properties                                          |
+-------------------------------------+-------------------------------------------------------------------+
| ``promoteGuestToUser``              | Promoting guest users to regular users                            |
+-------------------------------------+-------------------------------------------------------------------+
| ``resetPassword``                   | Resetting user passwords                                          |
+-------------------------------------+-------------------------------------------------------------------+
| ``resetPasswordFailedAttempts``     | Resetting password failed attempt counters                        |
+-------------------------------------+-------------------------------------------------------------------+
| ``revokeUserAccessToken``           | Revoking user access tokens                                       |
+-------------------------------------+-------------------------------------------------------------------+
| ``sendPasswordReset``               | Sending password reset emails                                     |
+-------------------------------------+-------------------------------------------------------------------+
| ``sendVerificationEmail``           | Sending email verification messages                               |
+-------------------------------------+-------------------------------------------------------------------+
| ``setDefaultProfileImage``          | Setting default profile images                                    |
+-------------------------------------+-------------------------------------------------------------------+
| ``setProfileImage``                 | Setting custom profile images                                     |
+-------------------------------------+-------------------------------------------------------------------+
| ``setUnreadThreadByPostId``         | Setting unread thread status by post ID                           |
+-------------------------------------+-------------------------------------------------------------------+
| ``switchAccountType``               | Switching account types                                           |
+-------------------------------------+-------------------------------------------------------------------+
| ``unfollowThreadByUser``            | Unfollowing message threads by user                               |
+-------------------------------------+-------------------------------------------------------------------+
| ``updatePassword``                  | Updating user passwords                                           |
+-------------------------------------+-------------------------------------------------------------------+
| ``updateReadStateAllThreadsByUser`` | Updating read state for all threads by user                       |
+-------------------------------------+-------------------------------------------------------------------+
| ``updateReadStateThreadByUser``     | Updating read state for specific threads by user                  |
+-------------------------------------+-------------------------------------------------------------------+
| ``updateUser``                      | Updating user account information                                 |
+-------------------------------------+-------------------------------------------------------------------+
| ``updateUserActive``                | Updating user active/inactive status                              |
+-------------------------------------+-------------------------------------------------------------------+
| ``updateUserAuth``                  | Updating user authentication settings                             |
+-------------------------------------+-------------------------------------------------------------------+
| ``updateUserMfa``                   | Updating user multi-factor authentication                         |
+-------------------------------------+-------------------------------------------------------------------+
| ``updateUserRoles``                 | Updating user roles and permissions                               |
+-------------------------------------+-------------------------------------------------------------------+
| ``verifyUserEmail``                 | Verifying user email addresses                                    |
+-------------------------------------+-------------------------------------------------------------------+
| ``verifyUserEmailWithoutToken``     | Verifying user email without token                                |
+-------------------------------------+-------------------------------------------------------------------+

Channel Management Events
~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------+-------------------------------------------------------------------+
| **Event Name**                     | **Description**                                                   |
+====================================+===================================================================+
| ``addChannelMember``               | Adding members to channels                                        |
+------------------------------------+-------------------------------------------------------------------+
| ``convertGroupMessageToChannel``   | Converting group messages to channels                             |
+------------------------------------+-------------------------------------------------------------------+
| ``createChannel``                  | Creating new channels                                             |
+------------------------------------+-------------------------------------------------------------------+
| ``createChannelBookmark``          | Creating channel bookmarks                                        |
+------------------------------------+-------------------------------------------------------------------+
| ``createDirectChannel``            | Creating direct message channels                                  |
+------------------------------------+-------------------------------------------------------------------+
| ``createGroupChannel``             | Creating group message channels                                   |
+------------------------------------+-------------------------------------------------------------------+
| ``deleteChannel``                  | Deleting channels                                                 |
+------------------------------------+-------------------------------------------------------------------+
| ``deleteChannelBookmark``          | Deleting channel bookmarks                                        |
+------------------------------------+-------------------------------------------------------------------+
| ``moveChannel``                    | Moving channels between teams                                     |
+------------------------------------+-------------------------------------------------------------------+
| ``patchChannel``                   | Updating channel properties                                       |
+------------------------------------+-------------------------------------------------------------------+
| ``patchChannelModerations``        | Updating channel moderation settings                              |
+------------------------------------+-------------------------------------------------------------------+
| ``removeChannelMember``            | Removing members from channels                                    |
+------------------------------------+-------------------------------------------------------------------+
| ``restoreChannel``                 | Restoring deleted channels                                        |
+------------------------------------+-------------------------------------------------------------------+
| ``updateChannel``                  | Updating channel information                                      |
+------------------------------------+-------------------------------------------------------------------+
| ``updateChannelBookmark``          | Updating channel bookmarks                                        |
+------------------------------------+-------------------------------------------------------------------+
| ``updateChannelBookmarkSortOrder`` | Updating channel bookmark sort order                              |
+------------------------------------+-------------------------------------------------------------------+
| ``updateChannelMemberNotifyProps`` | Updating channel member notification properties                   |
+------------------------------------+-------------------------------------------------------------------+
| ``updateChannelMemberRoles``       | Updating channel member roles                                     |
+------------------------------------+-------------------------------------------------------------------+
| ``updateChannelMemberSchemeRoles`` | Updating channel member scheme roles                              |
+------------------------------------+-------------------------------------------------------------------+
| ``updateChannelPrivacy``           | Updating channel privacy settings                                 |
+------------------------------------+-------------------------------------------------------------------+
| ``updateChannelScheme``            | Updating channel permission schemes                               |
+------------------------------------+-------------------------------------------------------------------+

Team Management Events
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------+-------------------------------------------------------------------+
| **Event Name**                  | **Description**                                                   |
+=================================+===================================================================+
| ``addTeamMember``               | Adding members to teams                                           |
+---------------------------------+-------------------------------------------------------------------+
| ``addTeamMembers``              | Adding multiple members to teams                                  |
+---------------------------------+-------------------------------------------------------------------+
| ``addUserToTeamFromInvite``     | Adding users to teams from invitations                            |
+---------------------------------+-------------------------------------------------------------------+
| ``createTeam``                  | Creating new teams                                                |
+---------------------------------+-------------------------------------------------------------------+
| ``deleteTeam``                  | Deleting teams                                                    |
+---------------------------------+-------------------------------------------------------------------+
| ``importTeam``                  | Importing team data                                               |
+---------------------------------+-------------------------------------------------------------------+
| ``invalidateAllEmailInvites``   | Invalidating all email invitations                                |
+---------------------------------+-------------------------------------------------------------------+
| ``inviteGuestsToChannels``      | Inviting guests to channels                                       |
+---------------------------------+-------------------------------------------------------------------+
| ``inviteUsersToTeam``           | Inviting users to teams                                           |
+---------------------------------+-------------------------------------------------------------------+
| ``patchTeam``                   | Updating team properties                                          |
+---------------------------------+-------------------------------------------------------------------+
| ``regenerateTeamInviteId``      | Regenerating team invitation IDs                                  |
+---------------------------------+-------------------------------------------------------------------+
| ``removeTeamIcon``              | Removing team icons                                               |
+---------------------------------+-------------------------------------------------------------------+
| ``removeTeamMember``            | Removing members from teams                                       |
+---------------------------------+-------------------------------------------------------------------+
| ``restoreTeam``                 | Restoring deleted teams                                           |
+---------------------------------+-------------------------------------------------------------------+
| ``setTeamIcon``                 | Setting team icons                                                |
+---------------------------------+-------------------------------------------------------------------+
| ``updateTeam``                  | Updating team information                                         |
+---------------------------------+-------------------------------------------------------------------+
| ``updateTeamMemberRoles``       | Updating team member roles                                        |
+---------------------------------+-------------------------------------------------------------------+
| ``updateTeamMemberSchemeRoles`` | Updating team member scheme roles                                 |
+---------------------------------+-------------------------------------------------------------------+
| ``updateTeamPrivacy``           | Updating team privacy settings                                    |
+---------------------------------+-------------------------------------------------------------------+
| ``updateTeamScheme``            | Updating team permission schemes                                  |
+---------------------------------+-------------------------------------------------------------------+

Posts & Content Events
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``createPost``                | Creating new posts                                                |
+-------------------------------+-------------------------------------------------------------------+
| ``createSchedulePost``        | Creating scheduled posts                                          |
+-------------------------------+-------------------------------------------------------------------+
| ``deletePost``                | Deleting posts                                                    |
+-------------------------------+-------------------------------------------------------------------+
| ``deleteScheduledPost``       | Deleting scheduled posts                                          |
+-------------------------------+-------------------------------------------------------------------+
| ``moveThread``                | Moving message threads                                            |
+-------------------------------+-------------------------------------------------------------------+
| ``patchPost``                 | Updating post properties                                          |
+-------------------------------+-------------------------------------------------------------------+
| ``restorePostVersion``        | Restoring previous post versions                                  |
+-------------------------------+-------------------------------------------------------------------+
| ``saveIsPinnedPost``          | Saving pinned post status                                         |
+-------------------------------+-------------------------------------------------------------------+
| ``searchPosts``               | Searching through posts                                           |
+-------------------------------+-------------------------------------------------------------------+
| ``updatePost``                | Updating post content                                             |
+-------------------------------+-------------------------------------------------------------------+
| ``updateScheduledPost``       | Updating scheduled posts                                          |
+-------------------------------+-------------------------------------------------------------------+

Authentication and Security Events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------+-------------------------------------------------------------------+
| **Event Name**                   | **Description**                                                   |
+==================================+===================================================================+
| ``addLdapPrivateCertificate``    | Adding LDAP private certificates                                  |
+----------------------------------+-------------------------------------------------------------------+
| ``addLdapPublicCertificate``     | Adding LDAP public certificates                                   |
+----------------------------------+-------------------------------------------------------------------+
| ``addSamlIdpCertificate``        | Adding SAML IDP certificates                                      |
+----------------------------------+-------------------------------------------------------------------+
| ``addSamlPrivateCertificate``    | Adding SAML private certificates                                  |
+----------------------------------+-------------------------------------------------------------------+
| ``addSamlPublicCertificate``     | Adding SAML public certificates                                   |
+----------------------------------+-------------------------------------------------------------------+
| ``completeSaml``                 | Completing SAML authentication                                    |
+----------------------------------+-------------------------------------------------------------------+
| ``extendSessionExpiry``          | Extending session expiry times                                    |
+----------------------------------+-------------------------------------------------------------------+
| ``idMigrateLdap``                | Migrating IDs to LDAP                                             |
+----------------------------------+-------------------------------------------------------------------+
| ``linkLdapGroup``                | Linking LDAP groups                                               |
+----------------------------------+-------------------------------------------------------------------+
| ``removeLdapPrivateCertificate`` | Removing LDAP private certificates                                |
+----------------------------------+-------------------------------------------------------------------+
| ``removeLdapPublicCertificate``  | Removing LDAP public certificates                                 |
+----------------------------------+-------------------------------------------------------------------+
| ``removeSamlIdpCertificate``     | Removing SAML IDP certificates                                    |
+----------------------------------+-------------------------------------------------------------------+
| ``removeSamlPrivateCertificate`` | Removing SAML private certificates                                |
+----------------------------------+-------------------------------------------------------------------+
| ``removeSamlPublicCertificate``  | Removing SAML public certificates                                 |
+----------------------------------+-------------------------------------------------------------------+
| ``revokeAllSessionsAllUsers``    | Revoking all sessions for all users                               |
+----------------------------------+-------------------------------------------------------------------+
| ``revokeAllSessionsForUser``     | Revoking all sessions for specific user                           |
+----------------------------------+-------------------------------------------------------------------+
| ``revokeSession``                | Revoking individual sessions                                      |
+----------------------------------+-------------------------------------------------------------------+
| ``syncLdap``                     | Synchronizing LDAP data                                           |
+----------------------------------+-------------------------------------------------------------------+
| ``unlinkLdapGroup``              | Unlinking LDAP groups                                             |
+----------------------------------+-------------------------------------------------------------------+

System Administration Events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------+-------------------------------------------------------------------+
| **Event Name**                 | **Description**                                                   |
+================================+===================================================================+
| ``clearServerBusy``            | Clearing server busy status                                       |
+--------------------------------+-------------------------------------------------------------------+
| ``completeOnboarding``         | Completing system onboarding                                      |
+--------------------------------+-------------------------------------------------------------------+
| ``configReload``               | Reloading system configuration                                    |
+--------------------------------+-------------------------------------------------------------------+
| ``databaseRecycle``            | Recycling database connections                                    |
+--------------------------------+-------------------------------------------------------------------+
| ``downloadLogs``               | Downloading system logs                                           |
+--------------------------------+-------------------------------------------------------------------+
| ``getAppliedSchemaMigrations`` | Getting applied schema migrations                                 |
+--------------------------------+-------------------------------------------------------------------+
| ``getAudits``                  | Retrieving audit logs                                             |
+--------------------------------+-------------------------------------------------------------------+
| ``getConfig``                  | Getting system configuration                                      |
+--------------------------------+-------------------------------------------------------------------+
| ``getLogs``                    | Getting system logs                                               |
+--------------------------------+-------------------------------------------------------------------+
| ``getOnboarding``              | Getting onboarding status                                         |
+--------------------------------+-------------------------------------------------------------------+
| ``invalidateCaches``           | Invalidating system caches                                        |
+--------------------------------+-------------------------------------------------------------------+
| ``migrateConfig``              | Migrating configuration                                           |
+--------------------------------+-------------------------------------------------------------------+
| ``patchConfig``                | Updating configuration properties                                 |
+--------------------------------+-------------------------------------------------------------------+
| ``queryLogs``                  | Querying system logs                                              |
+--------------------------------+-------------------------------------------------------------------+
| ``restartServer``              | Restarting server                                                 |
+--------------------------------+-------------------------------------------------------------------+
| ``setServerBusy``              | Setting server busy status                                        |
+--------------------------------+-------------------------------------------------------------------+
| ``updateConfig``               | Updating system configuration                                     |
+--------------------------------+-------------------------------------------------------------------+
| ``updateViewedProductNotices`` | Updating viewed product notices                                   |
+--------------------------------+-------------------------------------------------------------------+
| ``upgradeToEnterprise``        | Upgrading to Enterprise edition                                   |
+--------------------------------+-------------------------------------------------------------------+

File Management Events
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``createUpload``              | Creating file uploads                                             |
+-------------------------------+-------------------------------------------------------------------+
| ``getFile``                   | Retrieving files                                                  |
+-------------------------------+-------------------------------------------------------------------+
| ``getFileLink``               | Getting file links                                                |
+-------------------------------+-------------------------------------------------------------------+
| ``uploadData``                | Uploading data                                                    |
+-------------------------------+-------------------------------------------------------------------+
| ``uploadFileMultipart``       | Uploading multipart files                                         |
+-------------------------------+-------------------------------------------------------------------+
| ``uploadFileMultipartLegacy`` | Uploading legacy multipart files                                  |
+-------------------------------+-------------------------------------------------------------------+
| ``uploadFileSimple``          | Uploading simple files                                            |
+-------------------------------+-------------------------------------------------------------------+

OAuth Applications Events
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``authorizeOAuthApp``         | Authorizing OAuth applications                                    |
+-------------------------------+-------------------------------------------------------------------+
| ``authorizeOAuthPage``        | OAuth authorization page access                                   |
+-------------------------------+-------------------------------------------------------------------+
| ``completeOAuth``             | Completing OAuth flow                                             |
+-------------------------------+-------------------------------------------------------------------+
| ``createOAuthApp``            | Creating OAuth applications                                       |
+-------------------------------+-------------------------------------------------------------------+
| ``deauthorizeOAuthApp``       | Deauthorizing OAuth applications                                  |
+-------------------------------+-------------------------------------------------------------------+
| ``deleteOAuthApp``            | Deleting OAuth applications                                       |
+-------------------------------+-------------------------------------------------------------------+
| ``getAccessToken``            | Getting OAuth access tokens                                       |
+-------------------------------+-------------------------------------------------------------------+
| ``loginWithOAuth``            | Login with OAuth                                                  |
+-------------------------------+-------------------------------------------------------------------+
| ``mobileLoginWithOAuth``      | Mobile login with OAuth                                           |
+-------------------------------+-------------------------------------------------------------------+
| ``regenerateOAuthAppSecret``  | Regenerating OAuth app secrets                                    |
+-------------------------------+-------------------------------------------------------------------+
| ``signupWithOAuth``           | Signup with OAuth                                                 |
+-------------------------------+-------------------------------------------------------------------+
| ``updateOAuthApp``            | Updating OAuth applications                                       |
+-------------------------------+-------------------------------------------------------------------+

Webhooks Events
~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``createIncomingHook``        | Creating incoming webhooks                                        |
+-------------------------------+-------------------------------------------------------------------+
| ``createOutgoingHook``        | Creating outgoing webhooks                                        |
+-------------------------------+-------------------------------------------------------------------+
| ``deleteIncomingHook``        | Deleting incoming webhooks                                        |
+-------------------------------+-------------------------------------------------------------------+
| ``deleteOutgoingHook``        | Deleting outgoing webhooks                                        |
+-------------------------------+-------------------------------------------------------------------+
| ``getIncomingHook``           | Getting incoming webhooks                                         |
+-------------------------------+-------------------------------------------------------------------+
| ``getOutgoingHook``           | Getting outgoing webhooks                                         |
+-------------------------------+-------------------------------------------------------------------+
| ``regenOutgoingHookToken``    | Regenerating outgoing webhook tokens                              |
+-------------------------------+-------------------------------------------------------------------+
| ``updateIncomingHook``        | Updating incoming webhooks                                        |
+-------------------------------+-------------------------------------------------------------------+
| ``updateOutgoingHook``        | Updating outgoing webhooks                                        |
+-------------------------------+-------------------------------------------------------------------+

Slash Commands Events
~~~~~~~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``createCommand``             | Creating slash commands                                           |
+-------------------------------+-------------------------------------------------------------------+
| ``deleteCommand``             | Deleting slash commands                                           |
+-------------------------------+-------------------------------------------------------------------+
| ``executeCommand``            | Executing slash commands                                          |
+-------------------------------+-------------------------------------------------------------------+
| ``moveCommand``               | Moving slash commands                                             |
+-------------------------------+-------------------------------------------------------------------+
| ``regenCommandToken``         | Regenerating command tokens                                       |
+-------------------------------+-------------------------------------------------------------------+
| ``updateCommand``             | Updating slash commands                                           |
+-------------------------------+-------------------------------------------------------------------+

Plugins Events
~~~~~~~~~~~~~~

+-----------------------------------------+-------------------------------------------------------------------+
| **Event Name**                          | **Description**                                                   |
+=========================================+===================================================================+
| ``disablePlugin``                       | Disabling plugins                                                 |
+-----------------------------------------+-------------------------------------------------------------------+
| ``enablePlugin``                        | Enabling plugins                                                  |
+-----------------------------------------+-------------------------------------------------------------------+
| ``getFirstAdminVisitMarketplaceStatus`` | Getting first admin visit marketplace status                      |
+-----------------------------------------+-------------------------------------------------------------------+
| ``installMarketplacePlugin``            | Installing marketplace plugins                                    |
+-----------------------------------------+-------------------------------------------------------------------+
| ``installPluginFromURL``                | Installing plugins from URL                                       |
+-----------------------------------------+-------------------------------------------------------------------+
| ``removePlugin``                        | Removing plugins                                                  |
+-----------------------------------------+-------------------------------------------------------------------+
| ``setFirstAdminVisitMarketplaceStatus`` | Setting first admin visit marketplace status                      |
+-----------------------------------------+-------------------------------------------------------------------+
| ``uploadPlugin``                        | Uploading plugins                                                 |
+-----------------------------------------+-------------------------------------------------------------------+

Groups & LDAP Events
~~~~~~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``addGroupMembers``           | Adding members to groups                                          |
+-------------------------------+-------------------------------------------------------------------+
| ``addUserToGroupSyncables``   | Adding users to group syncables                                   |
+-------------------------------+-------------------------------------------------------------------+
| ``createGroup``               | Creating new groups                                               |
+-------------------------------+-------------------------------------------------------------------+
| ``deleteGroup``               | Deleting groups                                                   |
+-------------------------------+-------------------------------------------------------------------+
| ``deleteGroupMembers``        | Removing members from groups                                      |
+-------------------------------+-------------------------------------------------------------------+
| ``linkGroupSyncable``         | Linking group syncables to teams/channels                         |
+-------------------------------+-------------------------------------------------------------------+
| ``patchGroup``                | Updating group properties                                         |
+-------------------------------+-------------------------------------------------------------------+
| ``patchGroupSyncable``        | Updating group syncable properties                                |
+-------------------------------+-------------------------------------------------------------------+
| ``restoreGroup``              | Restoring deleted groups                                          |
+-------------------------------+-------------------------------------------------------------------+
| ``unlinkGroupSyncable``       | Unlinking group syncables from teams/channels                     |
+-------------------------------+-------------------------------------------------------------------+

Remote Clusters Events
~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------+-------------------------------------------------------------------+
| **Event Name**                     | **Description**                                                   |
+====================================+===================================================================+
| ``createRemoteCluster``            | Creating remote cluster connections                               |
+------------------------------------+-------------------------------------------------------------------+
| ``deleteRemoteCluster``            | Deleting remote cluster connections                               |
+------------------------------------+-------------------------------------------------------------------+
| ``generateRemoteClusterInvite``    | Generating invites for remote clusters                            |
+------------------------------------+-------------------------------------------------------------------+
| ``inviteRemoteClusterToChannel``   | Inviting remote clusters to channels                              |
+------------------------------------+-------------------------------------------------------------------+
| ``patchRemoteCluster``             | Updating remote cluster properties                                |
+------------------------------------+-------------------------------------------------------------------+
| ``remoteClusterAcceptInvite``      | Accepting remote cluster invites                                  |
+------------------------------------+-------------------------------------------------------------------+
| ``remoteClusterAcceptMessage``     | Accepting messages from remote clusters                           |
+------------------------------------+-------------------------------------------------------------------+
| ``remoteUploadProfileImage``       | Uploading profile images from remote clusters                     |
+------------------------------------+-------------------------------------------------------------------+
| ``uninviteRemoteClusterToChannel`` | Removing remote cluster invites from channels                     |
+------------------------------------+-------------------------------------------------------------------+
| ``uploadRemoteData``               | Uploading data from remote clusters                               |
+------------------------------------+-------------------------------------------------------------------+

Data Retention Events
~~~~~~~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``addChannelsToPolicy``       | Adding channels to data retention policies                        |
+-------------------------------+-------------------------------------------------------------------+
| ``addTeamsToPolicy``          | Adding teams to data retention policies                           |
+-------------------------------+-------------------------------------------------------------------+
| ``createPolicy``              | Creating data retention policies                                  |
+-------------------------------+-------------------------------------------------------------------+
| ``deletePolicy``              | Deleting data retention policies                                  |
+-------------------------------+-------------------------------------------------------------------+
| ``patchPolicy``               | Updating data retention policies                                  |
+-------------------------------+-------------------------------------------------------------------+
| ``removeChannelsFromPolicy``  | Removing channels from data retention policies                    |
+-------------------------------+-------------------------------------------------------------------+
| ``removeTeamsFromPolicy``     | Removing teams from data retention policies                       |
+-------------------------------+-------------------------------------------------------------------+

Jobs Events
~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``cancelJob``                 | Canceling background jobs                                         |
+-------------------------------+-------------------------------------------------------------------+
| ``createJob``                 | Creating new background jobs                                      |
+-------------------------------+-------------------------------------------------------------------+
| ``jobServer``                 | Job server operations                                             |
+-------------------------------+-------------------------------------------------------------------+
| ``updateJobStatus``           | Updating job status/progress                                      |
+-------------------------------+-------------------------------------------------------------------+

Licensing Events
~~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``addLicense``                | Adding enterprise licenses                                        |
+-------------------------------+-------------------------------------------------------------------+
| ``localAddLicense``           | Local license addition (cluster mode)                             |
+-------------------------------+-------------------------------------------------------------------+
| ``localRemoveLicense``        | Local license removal (cluster mode)                              |
+-------------------------------+-------------------------------------------------------------------+
| ``removeLicense``             | Removing enterprise licenses                                      |
+-------------------------------+-------------------------------------------------------------------+
| ``requestTrialLicense``       | Requesting trial licenses                                         |
+-------------------------------+-------------------------------------------------------------------+

Bot Management Events
~~~~~~~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``assignBot``                 | Assigning bots to users                                           |
+-------------------------------+-------------------------------------------------------------------+
| ``convertBotToUser``          | Converting bot accounts to user accounts                          |
+-------------------------------+-------------------------------------------------------------------+
| ``convertUserToBot``          | Converting user accounts to bot accounts                          |
+-------------------------------+-------------------------------------------------------------------+
| ``createBot``                 | Creating new bot accounts                                         |
+-------------------------------+-------------------------------------------------------------------+
| ``patchBot``                  | Updating bot account properties                                   |
+-------------------------------+-------------------------------------------------------------------+
| ``updateBotActive``           | Updating bot account active/inactive status                       |
+-------------------------------+-------------------------------------------------------------------+

Custom Emojis Events
~~~~~~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``createEmoji``               | Creating custom emojis                                            |
+-------------------------------+-------------------------------------------------------------------+
| ``deleteEmoji``               | Deleting custom emojis                                            |
+-------------------------------+-------------------------------------------------------------------+

Branding Events
~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``deleteBrandImage``          | Deleting brand images                                             |
+-------------------------------+-------------------------------------------------------------------+
| ``uploadBrandImage``          | Uploading brand images                                            |
+-------------------------------+-------------------------------------------------------------------+

Search Events
~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``purgeBleveIndexes``         | Purging Bleve search indexes                                      |
+-------------------------------+-------------------------------------------------------------------+
| ``purgeElasticsearchIndexes`` | Purging Elasticsearch search indexes                              |
+-------------------------------+-------------------------------------------------------------------+

Roles and Schemes Events
~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``createScheme``              | Creating permission schemes                                       |
+-------------------------------+-------------------------------------------------------------------+
| ``deleteScheme``              | Deleting permission schemes                                       |
+-------------------------------+-------------------------------------------------------------------+
| ``patchRole``                 | Updating role permissions                                         |
+-------------------------------+-------------------------------------------------------------------+
| ``patchScheme``               | Updating permission schemes                                       |
+-------------------------------+-------------------------------------------------------------------+

Preferences Events
~~~~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``deletePreferences``         | Deleting user preferences                                         |
+-------------------------------+-------------------------------------------------------------------+
| ``updatePreferences``         | Updating user preferences                                         |
+-------------------------------+-------------------------------------------------------------------+

Channel Categories Events
~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------+-------------------------------------------------------------------+
| **Event Name**                        | **Description**                                                   |
+===============================+===========================================================================+
| ``createCategoryForTeamForUser``      | Creating channel categories for users                             |
+---------------------------------------+-------------------------------------------------------------------+
| ``deleteCategoryForTeamForUser``      | Deleting channel categories for users                             |
+---------------------------------------+-------------------------------------------------------------------+
| ``updateCategoriesForTeamForUser``    | Updating multiple channel categories for users                    |
+---------------------------------------+-------------------------------------------------------------------+
| ``updateCategoryForTeamForUser``      | Updating single channel category for users                        |
+---------------------------------------+-------------------------------------------------------------------+
| ``updateCategoryOrderForTeamForUser`` | Updating channel category order for users                         |
+---------------------------------------+-------------------------------------------------------------------+

Export and Import Events
~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``bulkExport``                | Bulk data export operations                                       |
+-------------------------------+-------------------------------------------------------------------+
| ``bulkImport``                | Bulk data import operations                                       |
+-------------------------------+-------------------------------------------------------------------+
| ``deleteExport``              | Deleting export files                                             |
+-------------------------------+-------------------------------------------------------------------+
| ``deleteImport``              | Deleting import files                                             |
+-------------------------------+-------------------------------------------------------------------+
| ``generatePresignURLExport``  | Generating presigned URLs for exports                             |
+-------------------------------+-------------------------------------------------------------------+
| ``scheduleExport``            | Scheduling export operations                                      |
+-------------------------------+-------------------------------------------------------------------+
| ``slackImport``               | Slack data import operations                                      |
+-------------------------------+-------------------------------------------------------------------+

Access Control Events
~~~~~~~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``applyIPFilters``            | Applying IP filtering rules                                       |
+-------------------------------+-------------------------------------------------------------------+
| ``assignAccessPolicy``        | Assigning access policies to users/teams                          |
+-------------------------------+-------------------------------------------------------------------+
| ``createAccessControlPolicy`` | Creating new access control policies                              |
+-------------------------------+-------------------------------------------------------------------+
| ``deleteAccessControlPolicy`` | Deleting access control policies                                  |
+-------------------------------+-------------------------------------------------------------------+
| ``unassignAccessPolicy``      | Unassigning access policies from users/teams                      |
+-------------------------------+-------------------------------------------------------------------+
| ``updateActiveStatus``        | Updating active status of access control policies                 |
+-------------------------------+-------------------------------------------------------------------+

User Attributes Events
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``createCPAField``            | Creating custom profile attribute fields                          |
+-------------------------------+-------------------------------------------------------------------+
| ``deleteCPAField``            | Deleting custom profile attribute fields                          |
+-------------------------------+-------------------------------------------------------------------+
| ``patchCPAField``             | Updating custom profile attribute fields                          |
+-------------------------------+-------------------------------------------------------------------+
| ``patchCPAValues``            | Updating custom profile attribute values                          |
+-------------------------------+-------------------------------------------------------------------+

Outgoing OAuth Connections Events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------+-------------------------------------------------------------------+
| **Event Name**                                 | **Description**                                                   |
+================================================+===================================================================+
| ``createOutgoingOauthConnection``              | Creating outgoing OAuth connections                               |
+------------------------------------------------+-------------------------------------------------------------------+
| ``deleteOutgoingOAuthConnection``              | Deleting outgoing OAuth connections                               |
+------------------------------------------------+-------------------------------------------------------------------+
| ``updateOutgoingOAuthConnection``              | Updating outgoing OAuth connections                               |
+------------------------------------------------+-------------------------------------------------------------------+
| ``validateOutgoingOAuthConnectionCredentials`` | Validating outgoing OAuth connection credentials                  |
+------------------------------------------------+-------------------------------------------------------------------+

Terms of Service Events
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``createTermsOfService``      | Creating terms of service                                         |
+-------------------------------+-------------------------------------------------------------------+
| ``saveUserTermsOfService``    | Saving user acceptance of terms of service                        |
+-------------------------------+-------------------------------------------------------------------+

Compliance and Audit Events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------+-------------------------------------------------------------------+
| **Event Name**                | **Description**                                                   |
+===============================+===================================================================+
| ``addAuditLogCertificate``    | Adding audit log certificates                                     |
+-------------------------------+-------------------------------------------------------------------+
| ``createComplianceReport``    | Creating compliance reports                                       |
+-------------------------------+-------------------------------------------------------------------+
| ``downloadComplianceReport``  | Downloading compliance reports                                    |
+-------------------------------+-------------------------------------------------------------------+
| ``getComplianceReport``       | Getting compliance reports                                        |
+-------------------------------+-------------------------------------------------------------------+
| ``getComplianceReports``      | Getting multiple compliance reports                               |
+-------------------------------+-------------------------------------------------------------------+
| ``removeAuditLogCertificate`` | Removing audit log certificates                                   |
+-------------------------------+-------------------------------------------------------------------+

Local Operations Events
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------+-------------------------------------------------------------------+
| **Event Name**                   | **Description**                                                   |
+==================================+===================================================================+
| ``localCheckIntegrity``          | Local integrity checks                                            |
+----------------------------------+-------------------------------------------------------------------+
| ``localCreateChannel``           | Local channel creation                                            |
+----------------------------------+-------------------------------------------------------------------+
| ``localCreateCommand``           | Local command creation                                            |
+----------------------------------+-------------------------------------------------------------------+
| ``localCreateIncomingHook``      | Local incoming webhook creation                                   |
+----------------------------------+-------------------------------------------------------------------+
| ``localCreateTeam``              | Local team creation                                               |
+----------------------------------+-------------------------------------------------------------------+
| ``localDeleteChannel``           | Local channel deletion                                            |
+----------------------------------+-------------------------------------------------------------------+
| ``localDeletePost``              | Local post deletion                                               |
+----------------------------------+-------------------------------------------------------------------+
| ``localDeleteTeam``              | Local team deletion                                               |
+----------------------------------+-------------------------------------------------------------------+
| ``localDeleteUser``              | Local user deletion                                               |
+----------------------------------+-------------------------------------------------------------------+
| ``localGetClientConfig``         | Local client configuration retrieval                              |
+----------------------------------+-------------------------------------------------------------------+
| ``localGetConfig``               | Local configuration retrieval                                     |
+----------------------------------+-------------------------------------------------------------------+
| ``localInviteUsersToTeam``       | Local user invitation to teams                                    |
+----------------------------------+-------------------------------------------------------------------+
| ``localMoveChannel``             | Local channel moving                                              |
+----------------------------------+-------------------------------------------------------------------+
| ``localPatchChannel``            | Local channel patching                                            |
+----------------------------------+-------------------------------------------------------------------+
| ``localPatchConfig``             | Local configuration patching                                      |
+----------------------------------+-------------------------------------------------------------------+
| ``localPermanentDeleteAllUsers`` | Local permanent deletion of all users                             |
+----------------------------------+-------------------------------------------------------------------+
| ``localRemoveChannelMember``     | Local channel member removal                                      |
+----------------------------------+-------------------------------------------------------------------+
| ``localRestoreChannel``          | Local channel restoration                                         |
+----------------------------------+-------------------------------------------------------------------+
| ``localUpdateChannelPrivacy``    | Local channel privacy update                                      |
+----------------------------------+-------------------------------------------------------------------+
| ``localUpdateConfig``            | Local configuration update                                        |
+----------------------------------+-------------------------------------------------------------------+

.. note::
   This comprehensive list includes all audit events captured by Mattermost across all major system operations. Additional events may be logged depending on your Mattermost version, enabled features, and configuration settings. Enterprise and Enterprise Advanced features may generate additional audit events.

JSON data model
---------------

+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| **Name**   | **Type**                     | **Description**                                                                                                                     |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| timestamp  | int64                        | Date/time when event or activity has taken place.                                                                                   |
|            |                              |                                                                                                                                     |
|            |                              | Mattermost currently supports three log formats: plain, JSON, and                                                                   |
|            |                              | `GELF <https://go2docs.graylog.org/current/getting_in_log_data/gelf.html>`__.                                                       |
|            |                              |                                                                                                                                     |
|            |                              | - Plain log format uses `RFC3339 <https://www.rfc-editor.org/rfc/rfc3339>`__ by default.                                            |
|            |                              |   See the :ref:`plain log format configuration <administration-guide/manage/logging:plain log format configuration options>`        |
|            |                              |   documentation for supported options.                                                                                              |
|            |                              | - JSON log format uses `RFC3339 <https://www.rfc-editor.org/rfc/rfc3339>`__ by default.                                             |
|            |                              |   See the :ref:`JSON log format configuration <administration-guide/manage/logging:json log format configuration options>`          |
|            |                              |   documentation for supported options.                                                                                              |
|            |                              |                                                                                                                                     |
|            |                              | - GELF log format uses `unixtime <https://www.unixtimestamp.com/>`__.                                                               |
|            |                              |   See the :ref:`GELF log format configuration <administration-guide/manage/logging:gelf log format configuration options>`          |
|            |                              |   documentation for supported options.                                                                                              |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| event_name | string                       | Unique name and identifier of the event type taking place. See the `audit event types <#audit-event-types>`__ section               |
|            |                              | for a comprehensive list of all supported event names.                                                                              |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| status     | string                       | Success or failure of the audited event.                                                                                            |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| event      | `EventData <#eventdata>`__   | Event parameters and object states.                                                                                                 |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| actor      | `EventActor <#eventactor>`__ | User involved with the event.                                                                                                       |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| meta       | `EventMeta <#eventmeta>`__   | Related event metadata.                                                                                                             |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| error      | `EventError <#eventerror>`__ | The resulting error if the status is in a failed state.                                                                             |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+

EventData
~~~~~~~~~

+-------------------+---------------+-------------------------------------------------------------------+
| **Field name**    | **Data type** | **Description**                                                   |
+-------------------+---------------+-------------------------------------------------------------------+
| parameters        | map           | Payload and parameters being processed as part of the request.    |
+-------------------+---------------+-------------------------------------------------------------------+
| prior_state       | map           | Prior state of the entity being modified. ``null`` if there was   |
|                   |               | no prior state.                                                   |
+-------------------+---------------+-------------------------------------------------------------------+
| resulting_state   | map           | Resulting entity after creating or modifying it.                  |
+-------------------+---------------+-------------------------------------------------------------------+
| object_type       | string        | String representation of the entity type (e.g. post)              |
+-------------------+---------------+-------------------------------------------------------------------+

EventActor
~~~~~~~~~~

+-------------------+---------------+-------------------------------------------------------------------+
| **Field name**    | **Data type** | **Description**                                                   |
+-------------------+---------------+-------------------------------------------------------------------+
| user_id           | string        | Unique identifier of the event actor.                             |
+-------------------+---------------+-------------------------------------------------------------------+
| session_id        | string        | Unique session identifier of the event actor.                     |
+-------------------+---------------+-------------------------------------------------------------------+
| client            | string        | User agent of the client/platform in use by the event actor.      |
+-------------------+---------------+-------------------------------------------------------------------+
| ip_address        | string        | IPv4/IPv6 IP address of the event actor.                          |
+-------------------+---------------+-------------------------------------------------------------------+

EventMeta
~~~~~~~~~

+-------------------+---------------+-------------------------------------------------------------------+
| **Field name**    | **Data type** | **Description**                                                   |
+-------------------+---------------+-------------------------------------------------------------------+
| api_path          | string        | The REST endpoint which caused the event.                         |
+-------------------+---------------+-------------------------------------------------------------------+
| cluster_id        | integer       | Cluster identifier.                                               |
+-------------------+---------------+-------------------------------------------------------------------+

EventError
~~~~~~~~~~

+-------------------+---------------+-------------------------------------------------------------------+
| **Field name**    | **Data type** | **Description**                                                   |
+-------------------+---------------+-------------------------------------------------------------------+
| description       | string        | (Optional) Error description.                                     |
+-------------------+---------------+-------------------------------------------------------------------+
| status_code       | integer       | (Optional) Error status code.                                     |
+-------------------+---------------+-------------------------------------------------------------------+
