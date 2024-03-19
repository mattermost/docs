Experimental configuration settings
=====================================

Both self-hosted and Cloud admins can access the following configuration settings in the System Console. Self-hosted admins can also edit the ``config.json`` file as described in the following tables. 

- `Experimental System Console configuration settings <#experimental-system-console-configuration-settings>`__
- `Experimental Bleve configuration settings <#experimental-bleve-configuration-settings>`__
- `Beta Audit logging configuration settings <#beta-audit-logging-configuration-options>`__
- `Experimental job configuration settings <#experimental-job-configuration-settings>`__
- `Experimental configuration settings for self-hosted deployments only <#experimental-configuration-settings-for-self-hosted-deployments-only>`__

----

Experimental System Console configuration settings
--------------------------------------------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following experimental configuration settings in the System Console by going to **Experimental > Features**.

.. config:setting:: exp-ldaploginbuttoncolor
  :displayname: AD/LDAP login button color (Experimental)
  :systemconsole: Experimental > Features
  :configjson: LoginButtonColor
  :environment: N/A
  :description: Specify the color of the AD/LDAP login button for white labeling purposes. Use a hex code with a #-sign before the code.

AD/LDAP login button color
~~~~~~~~~~~~~~~~~~~~~~~~~~

Specify the color of the AD/LDAP login button for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile app.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonColor": ""`` with string input.                                       |
+-------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-ldaploginbuttonbordercolor
  :displayname: AD/LDAP login button border color (Experimental)
  :systemconsole: Experimental > Features
  :configjson: LoginButtonBorderColor
  :environment: N/A
  :description: Specify the color of the AD/LDAP login button border for white labeling purposes. Use a hex code with a #-sign before the code.

AD/LDAP login button border color
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

Specify the color of the AD/LDAP login button border for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile app.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonBorderColor": ""`` with string input.                                 |
+-------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-ldaploginbuttontextcolor
  :displayname: AD/LDAP login button text color (Experimental)
  :systemconsole: Experimental > Features
  :configjson: LoginButtonTextColor
  :environment: N/A
  :description: Specify the color of the AD/LDAP login button text for white labeling purposes. Use a hex code with a #-sign before the code.

AD/LDAP login button text color
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

Specify the color of the AD/LDAP login button text for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile app.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonTextColor": ""`` with string input.                                   |
+-------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enableauthenticationtransfer
  :displayname: Change authentication method (Experimental)
  :systemconsole: Experimental > Features
  :configjson: ExperimentalEnableAuthenticationTransfer
  :environment: N/A

  - **true**: **(Default)** Users can change their sign-in method to any that is enabled on the server, either via their Profile or the APIs.
  - **false**: Users cannot change their sign-in method, regardless of which authentication options are enabled.

Change authentication method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

**True**: Users can change their sign-in method to any that is enabled on the server, either via their Profile or the APIs.

**False**: Users cannot change their sign-in method, regardless of which authentication options are enabled.

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalEnableAuthenticationTransfer": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-linkmetadatatimeout
  :displayname: Link metadata timeout (Experimental)
  :systemconsole: Experimental > Features
  :configjson: LinkMetadataTimeoutMilliseconds
  :environment: N/A
  :description: Adds a configurable timeout for requests made to return link metadata. Default is **5000** milliseconds.

Link metadata timeout
~~~~~~~~~~~~~~~~~~~~~

Adds a configurable timeout for requests made to return link metadata. If the metadata is not returned before this timeout expires, the message will post without requiring metadata. This timeout covers the failure cases of broken URLs and bad content types on slow network connections.

+---------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LinkMetadataTimeoutMilliseconds": 5000`` with numerical input.                     |
+---------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-emailbatchbuffersize
  :displayname: Email batching buffer size (Experimental)
  :systemconsole: Experimental > Features
  :configjson: EmailBatchingBufferSize
  :environment: N/A
  :description: Specify the maximum number of notifications batched into a single email. Default is **256** notifications.

Email batching buffer size
~~~~~~~~~~~~~~~~~~~~~~~~~~

Specify the maximum number of notifications batched into a single email.

+--------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``EmailBatchingBufferSize": 256`` with numerical input.                        |
+--------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-emailbatchinterval
  :displayname: Email batching interval (Experimental)
  :systemconsole: Experimental > Features
  :configjson: EmailBatchingInterval
  :environment: N/A
  :description: Specify the maximum frequency, in seconds, which the batching job checks for new notifications. Default is **30** seconds.

Email batching interval
~~~~~~~~~~~~~~~~~~~~~~~

Specify the maximum frequency, in seconds, which the batching job checks for new notifications. Longer batching intervals will increase performance.

+-----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``EmailBatchingInterval": 30`` with numerical input.                        |
+-----------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-emailloginbuttoncolor
  :displayname: Email login button color (Experimental)
  :systemconsole: Experimental > Features
  :configjson: LoginButtonColor
  :environment: N/A
  :description: Specify the color of the email login button for white labeling purposes. Use a hex code with a #-sign before the code.

Email login button color
~~~~~~~~~~~~~~~~~~~~~~~~

Specify the color of the email login button for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile app.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonColor": ""`` with string input.                                       |
+-------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-emailloginbuttonbordercolor
  :displayname: Email login button border color (Experimental)
  :systemconsole: Experimental > Features
  :configjson: LoginButtonBorderColor
  :environment: N/A
  :description: Specify the color of the email login button border for white labeling purposes. Use a hex code with a #-sign before the code.

Email login button border color
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Specify the color of the email login button border for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile app.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonBorderColor": ""`` with string input.                                 |
+-------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-emailloginbuttontextcolor
  :displayname: Email login button text color (Experimental)
  :systemconsole: Experimental > Features
  :configjson: LoginButtonTextColor
  :environment: N/A
  :description: Specify the color of the email login button text for white labeling purposes. Use a hex code with a #-sign before the code.

Email login button text color
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Specify the color of the email login button text for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile app.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonTextColor": ""`` with string input.                                   |
+-------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enableaccountdeactivation
  :displayname: Enable account deactivation (Experimental)
  :systemconsole: Experimental > Features
  :configjson: EnableUserDeactivation
  :environment: N/A

  - **true**: Ability for users to deactivate their own account from **Settings > Advanced** is enabled.
  - **false**: **(Default)** Ability for users to deactivate their own account is disabled.

Enable account deactivation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Ability for users to deactivate their own account from **Settings > Advanced > Deactivate Account**. If a user deactivates their own account, they will get an email notification confirming they were deactivated. Available only when authentication is set to use email/password. Not available when authentication uses SAML or AD/LDAP.

**False**: Ability for users to deactivate their own account is disabled.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserDeactivation": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enableautoreplies
  :displayname: Enable automatic replies
  :systemconsole: Experimental > Features
  :configjson: ExperimentalEnableAutomaticReplies
  :environment: N/A

  - **true**: Users can enable Automatic Replies in **Settings > Notifications**.
  - **false**: **(Default)** Disables the Automatic Direct Message Replies feature and hides it from **Settings**.

Enable automatic replies
~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Users can enable Automatic Replies in **Settings > Notifications**. Users set a custom message that will be automatically sent in response to Direct Messages.

**False**: Disables the Automatic Direct Message Replies feature and hides it from **Settings**.

+--------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalEnableAutomaticReplies": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enablechannelviewedmessages
  :displayname: Enable channel viewed websocket messages (Experimental)
  :systemconsole: Experimental > Features
  :configjson: EnableChannelViewedMessages
  :environment: N/A
  :description: This setting determines whether ``channel_viewed WebSocket`` events are sent, which synchronize unread notifications across clients and devices. Default is **true**.

Enable channel viewed websocket messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting determines whether ``channel_viewed WebSocket`` events are sent, which synchronize unread notifications across clients and devices. Disabling the setting in larger deployments may improve server performance.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableChannelViewedMessages": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enabledefaultchannelleavejoinmessages
  :displayname: Enable default channel leave/join system messages (Experimental)
  :systemconsole: Experimental > Features
  :configjson: ExperimentalEnableDefaultChannelLeaveJoinMessages
  :environment: N/A
  :description: This setting determines whether team leave/join system messages are posted in the default ``town-square`` channel.

  - **true**: **(Default)** Enables leave/join system messages in the default ``town-square`` channel.
  - **false**: Disables leave/join messages from the default ``town-square`` channel.

Enable default channel leave/join system messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting determines whether team leave/join system messages are posted in the default ``town-square`` channel.

**True**: Enables leave/join system messages in the default ``town-square`` channel.

**False**: Disables leave/join messages from the default ``town-square`` channel. These system messages won't be added to the database either.

+----------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalEnableDefaultChannelLeaveJoinMessages": true`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-hardenedmode
  :displayname: Enable hardened mode (Experimental)
  :systemconsole: Experimental > Features
  :configjson: ExperimentalEnableHardenedMode
  :environment: N/A

  - **true**: Enables a hardened mode for Mattermost that makes user experience trade-offs in the interest of security.
  - **false**: **(Default)** Disables hardened mode.

Enable hardened mode
~~~~~~~~~~~~~~~~~~~~

**True**: Enables a hardened mode for Mattermost that makes user experience trade-offs in the interest of security.

**False**: Disables hardened mode.

Changes made when hardened mode is enabled:

- Failed login returns a generic error message instead of a specific message for username and password.
- If :doc:`multi-factor authentication (MFA) </onboard/multi-factor-authentication>` is enabled, the route to check if a user has MFA enabled always returns true. This causes the MFA input screen to appear even if the user does not have MFA enabled. The user may enter any value to pass the screen. Note that hardened mode does not affect user experience when MFA is enforced.
- Password reset does not inform the user that they can not reset their SSO account through Mattermost and instead claims to have sent the password reset email.
- Mattermost sanitizes all 500 errors before returned to the client. Use the supplied ``request_id`` to match user facing errors with the server logs.
- Standard users authenticated via username and password can't use post props reserved for integrations, such as ``override_username`` or ``override_icon_url``.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalEnableHardenedMode": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enablethemeselection
  :displayname: Enable theme selection (Experimental)
  :systemconsole: Experimental > Features
  :configjson: EnableThemeSelection
  :environment: N/A

  - **true**: **(Default)** Enables the **Display > Theme** tab in **Settings** so users can select their theme.
  - **false**: Users cannot select a different theme. The **Display > Theme** tab is hidden in **Settings**.

Enable theme selection
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

**True**: Enables the **Display > Theme** tab in **Settings** so users can select their theme.

**False**: Users cannot select a different theme. The **Display > Theme** tab is hidden in **Settings**.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableThemeSelection": true`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-allowcustomthemes
  :displayname: Allow custom themes (Experimental)
  :systemconsole: Experimental > Features
  :configjson: AllowCustomThemes
  :environment: N/A

  - **true**: **(Default)** Enables the **Display > Theme > Custom Theme** section in **Settings**.
  - **false**: Users cannot use a custom theme. The **Display > Theme > Custom Theme** section is hidden in **Settings**.

Allow custom themes
~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

**True**: Enables the **Display > Theme > Custom Theme** section in **Settings**.

**False**: Users cannot use a custom theme. The **Display > Theme > Custom Theme** section is hidden in **Settings**.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowCustomThemes": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-defaulttheme
  :displayname: Default theme (Experimental)
  :systemconsole: Experimental > Features
  :configjson: DefaultTheme
  :environment: N/A
  :description: Set a default theme that applies to all new users on the system. Default is **default**.

Default theme
~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

Set a default theme that applies to all new users on the system.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DefaultTheme": "default"`` with options ``"default"``, ``"organization"``, ``"mattermostDark"``, and ``"windows10"``. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enabletutorial
  :displayname: Enable tutorial (Experimental)
  :systemconsole: Experimental > Features
  :configjson: EnableTutorial
  :environment: N/A

  - **true**: **(Default)** Users are prompted with a tutorial when they open Mattermost for the first time after account creation.
  - **false**: The tutorial is disabled. Users are placed in Town Square when they open Mattermost for the first time after account creation.

Enable tutorial
~~~~~~~~~~~~~~~

**True**: Users are prompted with a tutorial when they open Mattermost for the first time after account creation.

**False**: The tutorial is disabled. Users are placed in Town Square when they open Mattermost for the first time after account creation.

+--------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableTutorial": true`` with options ``true`` and ``false``.                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enableonboarding
  :displayname: Enable onboarding (Experimental)
  :systemconsole: Experimental > Features
  :configjson: EnableOnboarding
  :environment: N/A

  - **true**: **(Default)** New Mattermost users are shown key tasks to complete as part of initial onboarding.
  - **false**: User onboarding tasks are disabled. Users are placed in Town Square when they open Mattermost for the first time after account creation.

Enable onboarding
~~~~~~~~~~~~~~~~~

**True**: New Mattermost users are shown key tasks to complete as part of initial onboarding.

**False**: User onboarding tasks are disabled. Users are placed in Town Square when they open Mattermost for the first time after account creation.

+--------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOnboarding": true`` with options ``true`` and ``false``.                                |
+--------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enableusertypingmessages
  :displayname: Enable user typing messages (Experimental)
  :systemconsole: Experimental > Features
  :configjson: EnableUserTypingMessages
  :environment: N/A
  :description: This setting determines whether "user is typing..." messages are displayed below the message box. Default is **true**.

Enable user typing messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting determines whether "user is typing..." messages are displayed below the message box. Disabling the setting in larger deployments may improve server performance.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserTypingMessages": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-usertypingtimeout
  :displayname: User typing timeout (Experimental)
  :systemconsole: Experimental > Features
  :configjson: TimeBetweenUserTypingUpdatesMilliseconds
  :environment: N/A
  :description: This setting defines how frequently "user is typing..." messages are updated, measured in milliseconds. Default is **5000** milliseconds.

User typing timeout
~~~~~~~~~~~~~~~~~~~

This setting defines how frequently "user is typing..." messages are updated, measured in milliseconds.

+----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TimeBetweenUserTypingUpdatesMilliseconds": 5000`` with numerical input. |
+----------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-primaryteam
  :displayname: Primary team (Experimental)
  :systemconsole: Experimental > Features
  :configjson: ExperimentalPrimaryTeam
  :environment: N/A
  :description: The primary team of which users on the server are members. When a primary team is set, the options to join other teams or leave the primary team are disabled.

Primary team
~~~~~~~~~~~~

The primary team of which users on the server are members. When a primary team is set, the options to join other teams or leave the primary team are disabled.

If the team URL of the primary team is https://example.mattermost.com/myteam/, then set the value to ``myteam`` in ``config.json``.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalPrimaryTeam": ""`` with string input.                  |
+-----------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-samlloginbuttoncolor
  :displayname: SAML login button color (Experimental)
  :systemconsole: Experimental > Features
  :configjson: LoginButtonColor
  :environment: N/A
  :description: Specify the color of the SAML login button for white labeling purposes. Use a hex code with a #-sign before the code.

SAML login button color
~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

Specify the color of the SAML login button for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile app.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonColor": ""`` with string input.                                       |
+-------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-samlloginbuttonbordercolor
  :displayname: SAML login button border color (Experimental)
  :systemconsole: Experimental > Features
  :configjson: LoginButtonBorderColor
  :environment: N/A
  :description: Specify the color of the SAML login button border for white labeling purposes. Use a hex code with a #-sign before the code.

SAML login button border color
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

Specify the color of the SAML login button border for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile app.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonBorderColor": ""`` with string input.                                 |
+-------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-samlloginbuttontextcolor
  :displayname: SAML login button text color (Experimental)
  :systemconsole: Experimental > Features
  :configjson: LoginButtonTextColor
  :environment: N/A
  :description: Specify the color of the SAML login button text for white labeling purposes. Use a hex code with a #-sign before the code.

SAML login button text color
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

Specify the color of the SAML login button text for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile app.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonTextColor": ""`` with string input.                                   |
+-------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-usechannelinemailnotifications
  :displayname: Use channel name in email notifications (Experimental)
  :systemconsole: Experimental > Features
  :configjson: UseChannelInEmailNotifications
  :environment: N/A

  - **true**: Channel and team name appears in email notification subject lines.
  - **false**: **(Default)** Only team name appears in email notification subject line.

Use channel name in email notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Channel and team name appears in email notification subject lines. Useful for servers using only one team.

**False**: Only team name appears in email notification subject line.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UseChannelInEmailNotifications": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-userstatusawaytimeout
  :displayname: User status away timeout (Experimental)
  :systemconsole: Experimental > Features
  :configjson: UserStatusAwayTimeout
  :environment: N/A
  :description: This setting defines the number of seconds after which the user's status indicator changes to "Away", when they are away from Mattermost. Default is **300** seconds.

User status away timeout
~~~~~~~~~~~~~~~~~~~~~~~~

This setting defines the number of seconds after which the user's status indicator changes to "Away", when they are away from Mattermost.

+--------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserStatusAwayTimeout": 300`` with numerical input. |
+--------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enablesharedchannels
  :displayname: Enable shared channels (Experimental)
  :systemconsole: Experimental > Features
  :configjson: ExperimentalSettings:EnableSharedChannels, ExperimentalSettings:EnableRemoteClusterService
  :environment: N/A

  Shared channels enables the ability to establish secure connections between Mattermost instances, and invite secured connections to shared channels where secure connections can participate as they would in any public and private channel.
  Both configuration settings must be enabled in order to share channels with secure connections. Only the **Enable Shared Channels** configuration option is available through the System Console. Default value of both settings is **false**.

Enable shared channels
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-selfhosted-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

Shared channels enables the ability to establish secure connections between Mattermost instances, and invite secured connections to shared channels where secure connections can participate as they would in any public and private channel. Enabling shared channels functionality requires a server restart.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's two ``config.json`` settings include ``"ExperimentalSettings:EnableSharedChannels": false`` with options ``true`` or ``false``, and ``"ExperimentalSettings:EnableRemoteClusterService": false`` with options ``true`` or ``false``. |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   - Both configuration settings must be enabled in order to share channels with secure connections. Only the **Enable Shared Channels** configuration option is available through the System Console.
   - System Admins for Cloud deployments can submit a request to have the ``EnableRemoteClusterService`` configuration setting enabled in their Cloud instance.

.. config:setting:: exp-enableappbar
  :displayname: Disable Apps Bar (Experimental)
  :systemconsole: Experimental > Features
  :configjson: DisableAppBar
  :environment: ExperimentalSettings.DisableAppBar
  :description: This setting disables the Apps Bar and moves all Mattermost integration icons from the vertical pane on the far right back to the channel header.

  - **true**: All integration icons in the channel header move to the Apps Bar with the exception of the calls beta feature.
  - **false**: **(Default)** All integration icons in the channel header display in the channel header.

Disable Apps Bar
~~~~~~~~~~~~~~~~

This setting disables the Apps Bar and moves all Mattermost integration icons from the vertical pane on the far right back to the channel header.

.. note::

  We strongly encourage Mattermost integrators to update their integrations to provide the best user experience. See the `channel header plugin changes <https://forum.mattermost.com/t/channel-header-plugin-changes/13551>`__ user forum discussion for details on how to register integrations with the Apps Bar.

**True**:  All integration icons in the channel header display in the channel header.

**False**: **(Default)** All integration icons, except the Calls icon, are available in the vertical Apps Bar pane on the right side of the screen. 

+--------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalSettings.DisableAppBar": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------------------+

Delay channel autocomplete
~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting controls whether or not the channel link autocomplete triggers immediately when after a tilde is typed when composing a message. This setting makes the channel autocomplete, such as ``~town-square``, less obtrusive for people who use tildes ``~`` as punctuation. 

**True**: The autocomplete appears after the user types a tilde followed by two or more characters. For example, typing ``~to`` will show the autocomplete, but typing ``~`` will not. 

**False**: **(Default)** The autocomplete appears immediately after the user types a tilde. For example, typing ``~`` will show the autocomplete.

+-------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalSettings.DelayChannelAutocomplete": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------------------+

Disable data refetching on browser refocus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting disables re-fetching of channel and channel members on browser focus.

**True**: Mattermost won't refetch channels and channel members when the browser regains focus. This may result in improved performance for users with many channels and channel members.

**False**: (Default) Mattermost will refetch channels and channel members when the browser regains focus.

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalSettings.DisableRefetchingOnBrowserFocus": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

Enable dedicated export filestore target
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting enables you to specify an alternate filestore target for Mattermost :doc:`bulk exports </manage/bulk-export-tool>` and :doc:`compliance exports </comply/compliance-export>`. 

**True**: A new ``ExportFileBackend()`` is generated under ``FileSettings`` using new configuration values for the following configuration settings:

- ``ExportDriverName``
- ``ExportDirectory``
- ``ExportAmazonS3AccessKeyId``
- ``ExportAmazonS3SecretAccessKey``
- ``ExportAmazonS3Bucket``
- ``ExportAmazonS3PathPrefix``
- ``ExportAmazonS3Region``
- ``ExportAmazonS3Endpoint``
- ``ExportAmazonS3SSL``
- ``ExportAmazonS3SignV2``
- ``ExportAmazonS3SSE``
- ``ExportAmazonS3Trace``
- ``ExportAmazonS3RequestTimeoutMilliseconds``
- ``ExportAmazonS3PresignExpiresSeconds``

**False**: Standard :ref:`file storage <configure/environment-configuration-settings:file storage>` is used (or when the configuration setting is omitted).

When an alternate filestore target is configured, Mattermost Cloud admins can generate an S3 presigned URL for exports using the ``/exportlink [job-id|zip file|latest]`` slash command. See the :ref:`Mattermost workspace migration <manage/cloud-data-export:create the export>` documentation for details. Alternatively, Cloud and self-hosted admins can use the :ref:`mmctl export generate-presigned-url <manage/mmctl-command-line-tool:mmctl export generate-presigned-url>` command to generate a presigned URL directly from mmctl.

.. note::

  Generating an S3 presigned URL requires the feature flag ``EnableExportDirectDownload`` to be set to ``true``,  the storage must be compatible with generating an S3 link, and this experimental configuration setting must be set to ``true``. Presigned URLs for exports aren't supported for systems with shared storage.

+-------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalSettings.DedicatedExportStore": false`` with options ``true`` and ``false``.     |
+-------------------------------------------------------------------------------------------------------------------------------------------+

----

Experimental Bleve configuration settings
-----------------------------------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Experimental > Bleve**, or by editing the ``config.json`` file as described in the following tables:

.. config:setting:: exp-bleveenable
  :displayname: Enable Bleve indexing (Experimental)
  :systemconsole: Experimental > Bleve
  :configjson: EnableIndexing
  :environment: N/A

  - **true**: The indexing of new posts occurs automatically.
  - **false**: **(Default)** The indexing of new posts does not occur automatically.

Enable Bleve indexing
~~~~~~~~~~~~~~~~~~~~~

**True**: The indexing of new posts occurs automatically. Search queries will not use bleve search until :ref:`Enable Bleve for search queries <configure/experimental-configuration-settings:enable bleve for search queries>` is enabled.

**False**: The indexing of new posts does not occur automatically.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableIndexing": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-bleveindexdir
  :displayname: Index directory (Experimental)
  :systemconsole: Experimental > Bleve
  :configjson: IndexDir
  :environment: N/A
  :description: Directory path to use for storing bleve indexes.

Index directory
~~~~~~~~~~~~~~~

Directory path to use for storing bleve indexes.

.. tip::

   The bleve index directory path isn't required to exist within the ``mattermost`` directory. When it exists outside of the ``mattermost`` directory, no  additional steps are needed to preserve or reindex these files as part of a Mattermost upgrade. See our :doc:`Upgrading Mattermost Server </upgrade/upgrading-mattermost-server>` documentation for details.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IndexDir": ""`` with string input.                           |
+-----------------------------------------------------------------------------------------------------------+

Bulk index now
~~~~~~~~~~~~~~

Select **Index Now** to index all users, channels, and posts in the database from oldest to newest. Bleve is available during indexing, but search results may be incomplete until the indexing job is complete.

You can configure the maximum time window used for a batch of posts being indexed. See the :ref:`Bulk Indexing Time Window Seconds <configure/environment-configuration-settings:bulk indexing time window>` documentation for details.

Purge indexes
~~~~~~~~~~~~~

Select **Purge Index** to remove the contents of the Bleve index directory. Search results may be incomplete until a bulk index of the existing database is rebuilt.

.. config:setting:: exp-bleveenablesearch
  :displayname: Enable Bleve for search queries (Experimental)
  :systemconsole: Experimental > Bleve
  :configjson: EnableSearching
  :environment: N/A

  - **true**: Search queries will use bleve search.
  - **false**: **(Default)** Search queries will not use bleve search.

Enable Bleve for search queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Search queries will use bleve search.

**False**: Search queries will not use bleve search.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSearching": false`` with options ``true`` and ``false``.  |
+--------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-bleveenableautocomplete
  :displayname: Enable Bleve for autocomplete queries (Experimental)
  :systemconsole: Experimental > Bleve
  :configjson: EnableAutocomplete
  :environment: N/A

  - **true**: Autocomplete queries will use bleve search.
  - **false**: **(Default)** Autocomplete queries will not use bleve search.

Enable Bleve for autocomplete queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Autocomplete queries will use bleve search.

**False**: Autocomplete queries will not use bleve search.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAutocomplete": false`` with options ``true`` and ``false``.  |
+-----------------------------------------------------------------------------------------------------------------+

----

Beta audit logging configuration settings
-----------------------------------------

Enable the following settings to output audit events. You can specify these settings independently for audit events and AD/LDAP events. 
When audit logging is enabled, you can specify size, backup interval, compression, maximium age to manage file rotation, and timestamps for audit logging.

.. note::
  
  These settings aren't available in the System Console and can only be set in ``config.json``.

.. config:setting:: exp-wroteauditfileslocally
  :displayname: File name (Beta Audit Logging)
  :systemconsole: N/A
  :configjson: FileName
  :environment: N/A
  :description: Write audit files locally.

Write audit files locally
~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Audit files are written locally to a file.

**False**: Audit logs aren't written locally to a file.

+--------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``".ExperimentalAuditSettings.FileEnabled": false",`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-auditfilename
  :displayname: File name (Beta Audit Logging)
  :systemconsole: N/A
  :configjson: FileName
  :environment: N/A
  :description: Specify the path to the audit file.

File name
~~~~~~~~~

Specify the path to the audit file.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``".ExperimentalAuditSettings.FileName": ""`` with string input consisting of a user-defined path (e.g. ``/var/log/mattermost_audit.log``).         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-filemaxsize
  :displayname: File max size MB (Beta Audit Logging)
  :systemconsole: N/A
  :configjson: FileMaxSizeMB
  :environment: N/A
  :description: This is the maximum size (measured in megabytes) that the file can grow before triggering rotation. Default is **100** MB.

File max size MB
~~~~~~~~~~~~~~~~

This is the maximum size (in megabytes) that the file can grow before triggering rotation. The default setting is ``100``.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``".ExperimentalAuditSettings.FileMaxSizeMB": 100`` with numerical input. |
+---------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-filemaxage
  :displayname: File max age days (Beta Audit Logging)
  :systemconsole: N/A
  :configjson: FileMaxAgeDays
  :environment: N/A
  :description: This is the maximum age in days a file can reach before triggering rotation. The default value is **0**, indicating no limit on the age.

File max age days
~~~~~~~~~~~~~~~~~

This is the maximum age in days a file can reach before triggering rotation. The default value is ``0``, indicating no limit on the age.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``".ExperimentalAuditSettings.FileMaxAgeDays": 0`` with numerical input. |
+--------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-filemaxbackups
  :displayname: File max backups (Beta Audit Logging)
  :systemconsole: N/A
  :configjson: FileMaxBackups
  :environment: N/A
  :description: This is the maximum number of rotated files kept; the oldest is deleted first. The default value is **0**, indicating no limit on the number of backups.

File max backups
~~~~~~~~~~~~~~~~

This is the maximum number of rotated files kept; the oldest is deleted first. The default value is ``0``, indicating no limit on the number of backups.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``".ExperimentalAuditSettings.FileMaxBackups": 0`` with numerical input. |
+--------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-filecompress
  :displayname: File compress (Beta Audit Logging)
  :systemconsole: N/A
  :configjson: FileCompress
  :environment: N/A
  :description: When ``true``, rotated files are compressed using ``gzip``. Default value is **false**.

File compress
~~~~~~~~~~~~~

When ``true``, rotated files are compressed using ``gzip``.

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``".ExperimentalAuditSettings.FileCompress": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-filemaxqueuesize
  :displayname: File max queue size (Beta Audit Logging)
  :systemconsole: N/A
  :configjson: FileMaxQueueSize
  :environment: N/A
  :description: This setting determines how many audit records can be queued/buffered at any point in time when writing to a file. Default is **1000** records.

File max queue size
~~~~~~~~~~~~~~~~~~~

This setting determines how many audit records can be queued/buffered at any point in time when writing to a file. The default is ``1000`` records.
This setting can be left as default unless you are seeing audit write failures in the server log and need to adjust the number accordingly.

+-------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``".ExperimentalAuditSettings.FileMaxQueueSize": 1000`` with numerical input. |
+-------------------------------------------------------------------------------------------------------------------------+

Experimental configuration settings for self-hosted deployments only
--------------------------------------------------------------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Access the following self-hosted configuration settings by editing the ``config.json`` file as described in the following tables. These configuration settings are not accessible through the System Console.

.. include:: common-config-settings-notation.rst
    :start-after: :nosearch:

.. config:setting:: exp-allowedthemes
  :displayname: Allowed themes (Experimental)
  :systemconsole: N/A
  :configjson: AllowedThemes
  :environment: N/A
  :description: Select the themes that can be chosen by users when ``EnableThemeSelection`` is set to ``true``.

Allowed themes
~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

This setting isn't available in the System Console and can only be set in ``config.json``.

Select the themes that can be chosen by users when ``EnableThemeSelection`` is set to ``true``.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowedThemes": []`` with string array input consisting of the options ``"default"``, ``"organization"``, ``"mattermostDark"``, and ``"windows10"``, such as ``["mattermostDark", "windows10"]``.     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-maxusersforstatistics
  :displayname: Maximum users for statistics (Experimental)
  :systemconsole: N/A
  :configjson: MaxUsersForStatistics
  :environment: N/A
  :description: Sets the maximum number of users on the server before statistics for total posts, total hashtag posts, total file posts, posts per day, and activated users with posts per day are disabled. Default is **2500** users.

Maximum users for statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

This setting isn't available in the System Console and can only be set in ``config.json``.

Sets the maximum number of users on the server before statistics for total posts, total hashtag posts, total file posts, posts per day, and activated users with posts per day are disabled.

This setting is used to maximize performance for large Enterprise deployments.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxUsersForStatistics": 2500`` with numerical input. |
+---------------------------------------------------------------------------------------------------+

.. config:setting:: exp-latestandroidversion
  :displayname: Latest Android version (Experimental)
  :systemconsole: N/A
  :configjson: AndroidLatestVersion
  :environment: N/A
  :description: The latest version of the Android React Native app that is recommended for use.

Latest Android version
~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

The latest version of the Android React Native app that is recommended for use.

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AndroidLatestVersion": ""`` with string input corresponding to a version string, such as ``"1.2.0"``. |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-minimumandroidversion
  :displayname: Minimum Android version (Experimental)
  :systemconsole: N/A
  :configjson: AndroidMinVersion
  :environment: N/A
  :description: The minimum version of the Android React Native app that is required to be used.

Minimum Android version
~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

The minimum version of the Android React Native app that is required to be used.

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AndroidMinVersion": ""`` with string input corresponding to a version string, such as ``"1.2.0"``. |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-latestiosversion
  :displayname: Latest iOS version (Experimental)
  :systemconsole: N/A
  :configjson: IosLatestVersion
  :environment: N/A
  :description: The latest version of the iOS app that is recommended for use.

Latest iOS version
~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

The latest version of the iOS app that is recommended for use.

+------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IosLatestVersion": ""`` with string input corresponding to a version string, such as ``"1.2.0"``. |
+------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-minimumiosversion
  :displayname: Minimum iOS version (Experimental)
  :systemconsole: N/A
  :configjson: IosMinVersion
  :environment: N/A
  :description: The minimum version of the iOS React Native app that is required to be used.

Minimum iOS version
~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

The minimum version of the iOS React Native app that is required to be used.

+---------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IosMinVersion": ""`` with string input corresponding to a version string, such as ``"1.2.0"``. |
+---------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-batchsize
  :displayname: Batch size (Experimental)
  :systemconsole: N/A
  :configjson: BatchSize
  :environment: N/A
  :description: Determines how many new posts are batched together to a compliance export file. Default is **10000** posts.

Batch size
~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

This setting isn't available in the System Console and can only be set in ``config.json``.

Determines how many new posts are batched together to a compliance export file.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BatchSize": 10000`` with numerical input. |
+----------------------------------------------------------------------------------------+

.. config:setting:: exp-filelocation
  :displayname: File location (Experimental)
  :systemconsole: N/A
  :configjson: FileLocation
  :environment: N/A
  :description: Set the file location of the compliance exports. Default value is **export**.

File Location
~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

This setting isn't available in the System Console and can only be set in ``config.json``.

Set the file location of the compliance exports. By default, they are written to the ``exports`` subdirectory of the configured :ref:`Local Storage directory <configure/environment-configuration-settings:local storage directory>`.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileLocation": "export"`` with string input. |
+-------------------------------------------------------------------------------------------+

.. config:setting:: exp-pushnotificationbuffer
  :displayname: Push notification buffer (Experimental)
  :systemconsole: N/A
  :configjson: PushNotificationBuffer
  :environment: N/A
  :description: Used to control the buffer of outstanding Push Notification messages to be sent. Default is **1000** notifications.

Push notification buffer
~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Used to control the buffer of outstanding Push Notification messages to be sent. If the number of messages exceeds that number, then the request making the Push Notification will be blocked until there's room.

+---------------------------------------------------------------------------------------------------------------------------------------------+
| This feature’s ``config.json`` setting is ``"PushNotificationBuffer": 1000"`` with numerical input.                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enableauditfiles
  :displayname: File configuration settings (Beta)
  :systemconsole: N/A
  :configjson: FileEnabled
  :environment: N/A
  :description: Enable this setting to write audit files locally, specifying size, backup interval, compression, maximum age to manage file rotation, and timestamps. Default value is **false**.

Restrict system admin
~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: **(Default for Cloud deployments)** Restricts the System Admin from viewing and modifying a subset of server configuration settings from the System Console. Not recommended for use in on-prem installations. This is intended to support Mattermost Private Cloud in giving the System Admin role to users but restricting certain actions only for Cloud Admins.

**False**: **(Default for self-host deployments)** No restrictions are applied to the System Admin role.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictSystemAdmin": "false"`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-remoteclusters
  :displayname: Remote clusters (Experimental)
  :systemconsole: N/A
  :configjson: RemoteClusters
  :environment: N/A

  - **true**: System Admins can manage remote clusters using the System Console.
  - **false**: **(Default)** Remote cluster management is disabled.

Remote clusters
~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

This setting isn't available in the System Console and can only be set in ``config.json``.

Enable this setting to add, remove, and view remote clusters for shared channels.

**True**: System Admins can manage remote clusters using the System Console.

**False**: Remote cluster management is disabled.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RemoteClusters": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enableclientcert
  :displayname: Enable client-side certification (Experimental)
  :systemconsole: N/A
  :configjson: ClientSideCertEnable
  :environment: N/A

  - **true**: Enables client-side certification for your Mattermost server.
  - **false**: **(Default)** Client-side certification is disabled.

Enable client-side certification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

**True**: Enables client-side certification for your Mattermost server. See :doc:`the documentation </onboard/certificate-based-authentication>` to learn more.

**False**: Client-side certification is disabled.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ClientSideCertEnable": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-clientcertcheck
  :displayname: Client-side certification login method (Experimental)
  :systemconsole: N/A
  :configjson: ClientSideCertCheck
  :environment: N/A

  - **primary**: After the client side certificate is verified, user's email is retrieved from the certificate and is used to log in without a password.
  - **secondary**: **(Default)** After the client side certificate is verified, user's email is retrieved from the certificate and matched against the one supplied by the user. If they match, the user logs in with regular email/password credentials.

Client-side certification login method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

Used in combination with the ``ClientSideCertEnable`` configuration setting.

**Primary**: After the client side certificate is verified, user's email is retrieved from the certificate and is used to log in without a password.

**Secondary**: After the client side certificate is verified, user's email is retrieved from the certificate and matched against the one supplied by the user. If they match, the user logs in with regular email/password credentials.

+----------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ClientSideCertCheck": "secondary"`` with options ``"primary"`` and ``"secondary"``. |
+----------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-outputdirectory
  :displayname: Export output directory (Experimental)
  :systemconsole: N/A
  :configjson: .ExportSettings.Directory
  :environment: N/A
  :description: The directory where the exported files are stored. The path is relative to the ``FileSettings`` directory. Default value is **./export**.

Export output directory
~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

The directory where the exported files are stored. The path is relative to the ``FileSettings`` directory. By default, exports are stored under ``./data/export``.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting under the ``ExportSettings`` section is ``Directory: ./export`` with string input. |
+---------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-exportretentiondays
  :displayname: Export retention days (Experimental)
  :systemconsole: N/A
  :configjson: .ExportSettings.RetentionDays
  :environment: N/A
  :description: The number of days to retain the exported files before deleting them. Default value is **30** days.

Export retention days
~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

The number of days to retain the exported files before deleting them.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting under the ``ExportSettings`` section is ``RetentionDays: 30`` with numerical input. |
+----------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-maximageresolution
  :displayname: Maximum image resolution (Experimental)
  :systemconsole: N/A
  :configjson: MaxImageResolution
  :environment: N/A
  :description: Maximum image resolution size for message attachments in pixels. Default value is **33177600** pixels.

Maximum image resolution
~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Maximum image resolution size for message attachments in pixels.

+--------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxImageResolution": 33177600`` with numerical input.     |
+--------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-maximagedecoderconcurrency
  :displayname: Maximum image decoder concurrency (Experimental)
  :systemconsole: N/A
  :configjson: MaxImageDecoderConcurrency
  :environment: N/A
  :description: Indicates how many images can be decoded concurrently at once. The default value of **-1** configures Mattermost to automatically use the number of CPUs present.

Maximum image decoder concurrency
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Indicates how many images can be decoded concurrently at once. The default value of ``-1`` configures Mattermost to automatically use the number of CPUs present.

.. note::

  This configuration setting affects the total memory consumption of the server. The maximum memory of a single image is dictated by ``MaxImageResolution * 24 bytes`` Therefore, a good rule of thumb to follow is that ``MaxImageResolution* MaxImageDecoderConcurrency * 24`` should be less than the allocated memory for image decoding.

+--------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxImageDecoderConcurrency": "-1"`` with numerical input. |
+--------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-initialfont
  :displayname: Initial font (Experimental)
  :systemconsole: N/A
  :configjson: InitialFont
  :environment: N/A
  :description: Font used in auto-generated profile pics with colored backgrounds. Default value is **luximbi.ttf**.

Initial font
~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Font used in auto-generated profile pics with colored backgrounds.

+-----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"InitialFont": "luximbi.ttf"`` with string input. |
+-----------------------------------------------------------------------------------------------+

.. config:setting:: exp-amazons3signv2
  :displayname: Amazon S3 signature v2 (Experimental)
  :systemconsole: N/A
  :configjson: AmazonS3SignV2
  :environment: N/A

  - **true**: Use Signature Version 2 Signing Process.
  - **false**: **(Default)** Use Signature Version 4 Signing Process.

Amazon S3 signature v2
~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

By default, Mattermost uses Signature V4 to sign API calls to AWS, but under some circumstances, V2 is required. For more information about when to use V2, see https://docs.aws.amazon.com/general/latest/gr/signature-version-2.html.

**True**: Use Signature Version 2 Signing Process.

**False**: Use Signature Version 4 Signing Process.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3SignV2": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-amazons3pathprefix
  :displayname: Amazon S3 path (Experimental)
  :systemconsole: N/A
  :configjson: AmazonS3PathPrefix
  :environment: N/A
  :description: Allows using the same S3 bucket for multiple deployments.

Amazon S3 path
~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Allows using the same S3 bucket for multiple deployments.

+------------------------------------------------------------------------------------------------------------+
| This feature’s ``config.json`` setting is ``"AmazonS3PathPrefix: ""`` with string input.                   |
+------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-gitlabscope
  :displayname: GitLab scope (Experimental)
  :systemconsole: N/A
  :configjson: Scope
  :environment: N/A
  :description: Standard setting for OAuth to determine the scope of information shared with OAuth client. Not currently supported by GitLab OAuth.

GitLab scope
~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Standard setting for OAuth to determine the scope of information shared with OAuth client. Not currently supported by GitLab OAuth.

+------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Scope": ""`` with string input. |
+------------------------------------------------------------------------------+

.. config:setting:: exp-globalrelaysmtptimeout
  :displayname: Global relay SMTP server timeout (Experimental)
  :systemconsole: N/A
  :configjson: GlobalRelaySettings.SMTPServerTimeout
  :environment: N/A
  :description: The number of seconds that can elapse before the connection attempt to the SMTP server is abandoned. Default is **1800** seconds.

Global relay SMTP server timeout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available as an add-on to legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

The number of seconds that can elapse before the connection attempt to the SMTP server is abandoned. The default value is 1800 seconds. This setting is currently not available in the System Console and can only be set in ``config.json``.

+-----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GlobalRelaySettings.SMTPServerTimeout": "1800"`` with numerical input.   |
+-----------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-googlescope
  :displayname: Google scope (Experimental)
  :systemconsole: N/A
  :configjson: Scope
  :environment: N/A
  :description: Standard setting for OAuth to determine the scope of information shared with OAuth client. Default value is **profile email**.

Google scope
~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

This setting isn't available in the System Console and can only be set in ``config.json``.

Standard setting for OAuth to determine the scope of information shared with OAuth client. Recommended setting is ``profile email``.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Scope": "profile email"`` with string input. |
+-------------------------------------------------------------------------------------------+

.. config:setting:: exp-importinputdirectory
  :displayname: Import input directory (Experimental)
  :systemconsole: N/A
  :configjson: ImportSettings.Directory
  :environment: N/A
  :description: The directory where the imported files are stored. The path is relative to the ``FileSettings`` directory. Default value is **./import**.

Import input directory
~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

The directory where the imported files are stored. The path is relative to the ``FileSettings`` directory. By default, imports are stored under ``./data/import``.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting under the ``ImportSettings`` section is ``Directory: ./import`` with string input. |
+---------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-importretentiondays
  :displayname: Import retention days (Experimental)
  :systemconsole: N/A
  :configjson: ImportSettings.RetentionDays
  :environment: N/A
  :description: The number of days to retain the imported files before deleting them. Default is **30** days.

Import retention days
~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

The number of days to retain the imported files before deleting them.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting under the ``ImportSettings`` section is ``RetentionDays: 30`` with numerical input. |
+----------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-exportfromtimestamp
  :displayname: Export from timestamp (Experimental)
  :systemconsole: N/A
  :configjson: ExportFromTimestamp
  :environment: N/A
  :description: Set the Unix timestamp (seconds since epoch, UTC) to export data from. Default is **0**.

Export from timestamp
~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

This setting isn't available in the System Console and can only be set in ``config.json``.

Set the Unix timestamp (seconds since epoch, UTC) to export data from.

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExportFromTimestamp": 0`` with numerical input. |
+----------------------------------------------------------------------------------------------+

.. config:setting:: exp-blockprofilerate
  :displayname: Block profile rate (Experimental)
  :systemconsole: N/A
  :configjson: BlockProfileRate
  :environment: N/A

  Value that controls the `fraction of goroutine blocking events reported in the blocking profile <https://golang.org/pkg/runtime/#SetBlockProfileRate>`__.
  To include every blocking event in the profile, set the rate to ``1``. To turn off profiling entirely, set the rate to ``0``.
  Default is **0**.

Block profile rate
~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``. Changes to this setting require a server restart before taking effect.

Value that controls the `fraction of goroutine blocking events reported in the blocking profile <https://golang.org/pkg/runtime/#SetBlockProfileRate>`__.

The profiler aims to sample an average of one blocking event per rate nanoseconds spent blocked.

To include every blocking event in the profile, set the rate to ``1``. To turn off profiling entirely, set the rate to ``0``.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BlockProfileRate": 0`` with options ``0`` and ``1``. |
+---------------------------------------------------------------------------------------------------+

.. config:setting:: exp-appcustomurlschemes
  :displayname: App custom URL schemes (Experimental)
  :systemconsole: N/A
  :configjson: .NativeAppSettings.AppCustomURLSchemes
  :environment: N/A
  :description: Define valid custom URL schemes for redirect links provided by custom-built mobile Mattermost apps.

App custom URL schemes
~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Define valid custom URL schemes for redirect links provided by custom-built mobile Mattermost apps. This ensures users are redirected to the custom-built mobile app and not Mattermost's mobile client.

When configured, after OAuth or SAML user authentication is complete, custom URL schemes sent by mobile clients are validated to ensure they don't include default schemes such as ``http`` or ``https``. Mobile users are then redirected back to the mobile app using the custom scheme URL provided by the mobile client. We recommend that you update your mobile client values as well with valid custom URL schemes.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"NativeAppSettings.AppCustomURLSchemes"`` with an array of strings as input. For example: ``[custom-app://, some-app://]``.                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-o365scope
  :displayname: Office 365 scope (Experimental)
  :systemconsole: N/A
  :configjson: Scope
  :environment: N/A
  :description: Standard setting for OAuth to determine the scope of information shared with OAuth client. Recommended setting is ``User.Read``.

Office 365 Scope
~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

This setting isn't available in the System Console and can only be set in ``config.json``.

Standard setting for OAuth to determine the scope of information shared with OAuth client. Recommended setting is ``User.Read``.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Scope": "User.Read"`` with string input. |
+---------------------------------------------------------------------------------------+

.. config:setting:: exp-enablepluginuploads
  :displayname: Enable plugin uploads (Experimental)
  :systemconsole: N/A
  :configjson: EnableUploads
  :environment: N/A

  - **true**: Enables plugin uploads by System Admins at **Plugins > Management**.
  - **false**: **(Default)** Disables plugin uploads on your Mattermost server.

Enable plugin uploads
~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables plugin uploads by System Admins at **Plugins > Management**. If you do not plan to upload a plugin, set to ``false`` to control which plugins are installed on your server. See `documentation <https://developers.mattermost.com/integrate/admin-guide/admin-plugins-beta/>`__ to learn more.

**False**: Disables plugin uploads on your Mattermost server.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUploads": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-allowinsecuredownloadurl
  :displayname: Allow insecure download URL (Experimental)
  :systemconsole: N/A
  :configjson: AllowInsecureDownloadUrl
  :environment: N/A

  - **true**: Enables downloading and installing a plugin from a remote URL.
  - **false**: **(Default)** Disables downloading and installing a plugin from a remote URL.

Allow insecure download URL
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables downloading and installing a plugin from a remote URL.

**False**: Disables downloading and installing a plugin from a remote URL.

+-----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowInsecureDownloadUrl": false`` with options ``true`` and ``false``.                    |
+-----------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enablepluginhealthcheck
  :displayname: Enable plugin health check (Experimental)
  :systemconsole: N/A
  :configjson: EnableHealthCheck
  :environment: N/A

  - **true**: **(Default)** Enables plugin health check to ensure all plugins are periodically monitored, and restarted or deactivated based on their health status.
  - **false**: Disables plugin health check on your Mattermost server.

Enable plugin health check
~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables plugin health check to ensure all plugins are periodically monitored, and restarted or deactivated based on their health status. The health check runs every 30 seconds. If the plugin is detected to fail 3 times within an hour, the Mattermost server attempts to restart it. If the restart fails 3 successive times, it's automatically disabled.

**False**: Disables plugin health check on your Mattermost server.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableHealthCheck": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-plugindirectory
  :displayname: Plugin directory (Experimental)
  :systemconsole: N/A
  :configjson: Directory
  :environment: N/A
  :description: The location of the plugin files. If blank, they are stored in the ``./plugins`` directory. Default value is **./plugins**.

Plugin directory
~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

The location of the plugin files. If blank, they are stored in the ``./plugins`` directory. The path that you set must exist and Mattermost must have write permissions in it.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Directory": "./plugins"`` with string input.                       |
+-----------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-clientplugindirectory
  :displayname: Client plugin directory (Experimental)
  :systemconsole: N/A
  :configjson: ClientDirectory
  :environment: N/A
  :description: The location of client plugin files. If blank, they are stored in the ``./client/plugins`` directory. Default value is **./client/plugins**.

Client plugin directory
~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

The location of client plugin files. If blank, they are stored in the ``./client/plugins`` directory. The path that you set must exist and Mattermost must have write permissions in it.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ClientDirectory": "./client/plugins"`` with string input.          |
+-----------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-scopingidpproviderid
  :displayname: Scoping IDP provider ID (Experimental)
  :systemconsole: N/A
  :configjson: ScopingIDPProviderId
  :environment: N/A
  :description: Allows an authenticated user to skip the initial login page of their federated Azure AD server, and only require a password to log in.

Scoping IDP provider ID
~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

This setting isn't available in the System Console and can only be set in ``config.json``.

Allows an authenticated user to skip the initial login page of their federated Azure AD server, and only require a password to log in.

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ScopingIDPProviderId": ""`` with string input. |
+---------------------------------------------------------------------------------------------+

.. config:setting:: exp-scopingidpprovidername
  :displayname: Scoping IDP provider name (Experimental)
  :systemconsole: N/A
  :configjson: ScopingIDPName
  :environment: N/A
  :description: Adds the name associated with a user's Scoping Identity Provider ID.

Scoping IDP provider name
~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

This setting isn't available in the System Console and can only be set in ``config.json``.

Adds the name associated with a user's Scoping Identity Provider ID.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ScopingIDPName": ""`` with string input. |
+---------------------------------------------------------------------------------------+

.. config:setting:: exp-groupunreadchannels
  :displayname: Group unread channels (Experimental)
  :systemconsole: N/A
  :configjson: ExperimentalGroupUnreadChannels
  :environment: N/A

  - **default_off**: **(Default)** Disables the unread channels sidebar section for all users by default. Users can enable it in **Settings > Sidebar > Group unread channels separately**.
  - **default_on**: Enables the unread channels sidebar section for all users by default. Users can disable it in **Settings > Sidebar > Group unread channels separately**.

Group unread channels
~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

This setting applies to the new sidebar only. You must disable the :ref:`Enable Legacy Sidebar <configure/deprecated-configuration-settings:enable legacy sidebar>` configuration setting to see and enable this functionality in the System Console.

**Default Off**: Disables the unread channels sidebar section for all users by default. Users can enable it in **Settings > Sidebar > Group unread channels separately**.

**Default On**: Enables the unread channels sidebar section for all users by default. Users can disable it in **Settings > Sidebar > Group unread channels separately**.

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalGroupUnreadChannels": "default_off"`` with options ``"default_off"`` and ``"default_on"``. |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-strictcsrftoken
  :displayname: Strict CSRF token enforcement (Experimental)
  :systemconsole: N/A
  :configjson: ExperimentalStrictCSRFEnforcement
  :environment: N/A

  - **true**: Enables CSRF protection tokens for additional hardening compared to the currently used custom header.
  - **false**: **(Default)** Disables CSRF protection tokens.

Strict CSRF token enforcement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables CSRF protection tokens for additional hardening compared to the currently used custom header. When the user logs in, an additional cookie is created with the CSRF token contained.

**False**: Disables CSRF protection tokens.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalStrictCSRFEnforcement": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-developerflags
  :displayname: Developer flags (Experimental)
  :systemconsole: N/A
  :configjson: DeveloperFlags
  :environment: N/A
  :description: This configuration setting specifies a list of strings where each string is a flag used to set the content security policy (CSP) for the Mattermost Web App.

Developer flags
~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

This configuration setting specifies a list of strings where each string is a flag used to set the content security policy (CSP) for the Mattermost Web App. Each flag must be in the format ``flag=true`` (e.g. ``unsafe-eval=true,unsafe-inline=true``). Not recommended for production environments.

The following values are currently supported:

- ``unsafe-eval``: Adds the ``unsafe-eval`` CSP directive to the root webapp, allowing increased debugging in developer environments.
- ``unsafe-inline``: Adds the ``unsafe-inline`` CSP directive to the root webapp, allowing increased debugging in developer environments.

This configuration setting is disabled by default and requires :ref:`developer mode <configure/environment-configuration-settings:enable developer mode>` to be enabled.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DeveloperFlags": ""`` with string input.  |
+----------------------------------------------------------------------------------------+

.. config:setting:: exp-enablepostsearch
  :displayname: Enable post search (Experimental)
  :systemconsole: N/A
  :configjson: EnablePostSearch
  :environment: N/A
  :description: If this setting is enabled, users can search messages. Default is **true**.

Enable post search
~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

If this setting is enabled, users can search messages. Disabling search can result in a performance increase, but users get an error message when they attempt to use the search box.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostSearch": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enablefilesearch
  :displayname: Enable file search (Experimental)
  :systemconsole: N/A
  :configjson: EnableFileSearch
  :environment: N/A
  :description: This configuration setting enables users to search documents attached to messages by filename. Default is **true**.

Enable file search
~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

This configuration setting enables users to search documents attached to messages by filename. To enable users to search documents by their content, you must also enable the ``ExtractContent`` configuration setting. See our :ref:`Enable Document Search by Content <configure/environment-configuration-settings:enable document search by content>` documentation for details. Document content search is available in Mattermost Server from v5.35, with mobile support coming soon.

**True**: Supported document types are searchable by their filename.

**False**: File-based searches are disabled.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableFileSearch": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enableuserstatusupdates
  :displayname: Enable user status updates (Experimental)
  :systemconsole: N/A
  :configjson: EnableUserStatuses
  :environment: N/A
  :description: Turn status updates off to improve performance. Default is **true**.

Enable user status updates
~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Turn status updates off to improve performance. When status updates are off, users appear online only for brief periods when posting a message, and only to members of the channel in which the message is posted.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserStatuses": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-websocketsecureport
  :displayname: Websocket secure port (Experimental)
  :systemconsole: N/A
  :configjson: WebsocketSecurePort
  :environment: N/A
  :description: This setting defines the port on which the secured WebSocket will listen using the ``wss`` protocol. Default is **443**.

Websocket secure port
~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``. Changes to this setting require a server restart before taking effect.

(Optional) This setting defines the port on which the secured WebSocket will listen using the ``wss`` protocol. Defaults to ``443``. When the client attempts to make a WebSocket connection it first checks to see if the page is loaded with HTTPS. If so, it will use the secure WebSocket connection. If not, it will use the unsecure WebSocket connection. IT IS HIGHLY RECOMMENDED PRODUCTION DEPLOYMENTS ONLY OPERATE UNDER HTTPS AND WSS.

+------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"WebsocketSecurePort": 443`` with numerical input. |
+------------------------------------------------------------------------------------------------+

.. config:setting:: exp-websocketport
  :displayname: Websocket port (Experimental)
  :systemconsole: N/A
  :configjson: WebsocketPort
  :environment: N/A
  :description: This setting defines the port on which the unsecured WebSocket will listen using the ``ws`` protocol. Default is **80**.

Websocket port
~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``. Changes to this setting require a server restart before taking effect.

(Optional) This setting defines the port on which the unsecured WebSocket will listen using the ``ws`` protocol. Defaults to ``80``. When the client attempts to make a WebSocket connection it first checks to see if the page is loaded with HTTPS. If so, it will use the secure WebSocket connection. If not, it will use the unsecure WebSocket connection. IT IS HIGHLY RECOMMENDED PRODUCTION DEPLOYMENTS ONLY OPERATE UNDER HTTPS AND WSS.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``WebsocketPort": 80`` with numerical input. |
+----------------------------------------------------------------------------------------+

.. config:setting:: exp-enableapiteamdeletion
  :displayname: Enable API team deletion (Experimental)
  :systemconsole: N/A
  :configjson: EnableAPITeamDeletion
  :environment: N/A

  - **true**: The ``api/v4/teams/{teamid}?permanent=true`` API endpoint can be called by Team and System Admins to permanently delete a team.
  - **false**: **(Default)** The API endpoint cannot be called.

Enable API team deletion
~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: The ``api/v4/teams/{teamid}?permanent=true`` API endpoint can be called by Team and System Admins to permanently delete a team.

**False**: The API endpoint cannot be called. Note that ``api/v4/teams/{teamid}`` can still be used to soft delete a team.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAPITeamDeletion": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enableapiuserdeletion
  :displayname: Enable API user deletion
  :systemconsole: N/A
  :configjson: EnableAPIUserDeletion
  :environment: N/A

  - **true**: The ``api/v4/users/{userid}?permanent=true`` API endpoint can be called by System Admins, or users with appropriate permissions, to permanently delete a user.
  - **false**: **(Default)** The API endpoint cannot be called.

Enable API user deletion
~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: The ``api/v4/users/{userid}?permanent=true`` API endpoint can be called by System Admins, or users with appropriate permissions, to permanently delete a user.

**False**: The API endpoint cannot be called. Note that ``api/v4/users/{userid}`` can still be used to soft delete a user.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAPIUserDeletion": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enableapichanneldeletion
  :displayname: Enable API channel deletion (Experimental)
  :systemconsole: N/A
  :configjson: EnableAPIChannelDeletion
  :environment: N/A

  - **true**: The ``api/v4/channels/{channelid}?permanent=true`` API endpoint can be called by System Admins, or users with appropriate permissions, to permanently delete a channel.
  - **false**: **(Default)** The API endpoint cannot be called.

Enable API channel deletion
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: The ``api/v4/channels/{channelid}?permanent=true`` API endpoint can be called by System Admins, or users with appropriate permissions, to permanently delete a channel.

**False**: The API endpoint cannot be called. Note that ``api/v4/channels/{channelid}`` can still be used to soft delete a channel.

+----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAPIChannelDeletion": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enableopentracing
  :displayname: Enable OpenTracing (Experimental)
  :systemconsole: N/A
  :configjson: EnableOpenTracing
  :environment: N/A

  - **true**: A Jaeger client is instantiated and is used to trace each HTTP request as it goes through App and Store layers.
  - **false**: **(Default)** OpenTracing is not enabled.

Enable OpenTracing
~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: A Jaeger client is instantiated and is used to trace each HTTP request as it goes through App and Store layers. Context is added to App and Store and is passed down the layer chain to create OpenTracing 'spans'.

By default, in order to avoid leaking sensitive information, no method parameters are reported to OpenTracing. Only the name of the method is reported.

**False**: OpenTracing is not enabled.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOpenTracing": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enablelocalmode
  :displayname: Enable local mode for mmctl (Experimental)
  :systemconsole: N/A
  :configjson: EnableLocalMode
  :environment: N/A

  - **true**: Enables local mode for mmctl.
  - **false**: **(Default)** Prevents local mode for mmctl.

Enable local mode for mmctl
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables local mode for mmctl.

**False**: Prevents local mode for mmctl.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableLocalMode": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

.. tip::

  When trying to use local mode with mmctl, ensure you're using the same user when running the server and mmctl, or clean up the socket file before switching to a new user. If you encounter an error like ``socket file "/var/tmp/mattermost_local.socket" doesn't exists, please check the server configuration for local mode``, this can be resolved by setting this configuration setting to ``true``.

.. config:setting:: exp-localmodesocketlocation
  :displayname: Enable local mode socket location (Experimental)
  :systemconsole: N/A
  :configjson: LocalModeSocketLocation
  :environment: N/A
  :description: The path for the socket that the server will create for mmctl to connect and communicate through local mode. Default value is **/var/tmp/mattermost_local.socket**.

Enable local mode socket location
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

The path for the socket that the server will create for mmctl to connect and communicate through local mode. If the default value for this key is changed, you will need to point mmctl to the new socket path when in local mode, using the ``--local-socket-path /new/path/to/socket`` flag in addition to the ``--local`` flag.

If nothing is specified, the default path that both the server and mmctl assumes is ``/var/tmp/mattermost_local.socket``.

+--------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LocalModeSocketLocation": "/var/tmp/mattermost_local.socket"`` with string input. |
+--------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-defaultchannels
  :displayname: Default channels (Experimental)
  :systemconsole: N/A
  :configjson: ExperimentalDefaultChannels
  :environment: N/A
  :description: Default channels every user is added to automatically after joining a new team. Only applies to Public channels, but affects all teams on the server.

Default channels
~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Default channels every user is added to automatically after joining a new team. Only applies to Public channels, but affects all teams on the server.

When not set, every user is added to the ``off-topic`` and ``town-square`` channels by default.

.. note::

   Even if ``town-square`` is not listed, every user is added to that channel after joining a new team.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalDefaultChannels": []`` with string array input consisting of channel names, such as ``["announcement", "developers"]``. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

Experimental job configuration settings
---------------------------------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Settings to configure how Mattermost schedules and completes periodic tasks such as the deletion of old posts with Data Retention enabled or indexing posts with Elasticsearch. These settings control which Mattermost servers are designated as a Scheduler, a server that queues the tasks at the correct times, and as a Worker, a server that completes the given tasks.

When running Mattermost on a single machine, both ``RunJobs`` and ``RunScheduler`` should be enabled. Without both of these enabled, Mattermost will not function properly.

When running Mattermost in High Availability mode, ``RunJobs`` should be enabled on one or more servers while ``RunScheduler`` should be enabled on all servers under normal circumstances. A High Availability cluster will have one Scheduler and one or more Workers. See the below sections for more information.

.. config:setting:: exp-runjobs
  :displayname: Run jobs (Experimental)
  :systemconsole: N/A
  :configjson: RunJobs
  :environment: N/A
  :description: Set whether or not this Mattermost server will handle tasks created by the Scheduler. Default is **true**.

Run jobs
~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Set whether or not this Mattermost server will handle tasks created by the Scheduler. When running Mattermost on a single machine, this setting should always be enabled.

When running Mattermost in :doc:`High Availablity mode </scale/high-availability-cluster>`, one or more servers should have this setting enabled. We recommend that your High Availability cluster has one or more dedicated Workers with this setting enabled while the remaining Mattermost app servers have it disabled.

+------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RunJobs": true`` with options ``true`` and ``false``.                                 |
+------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-runscheduler
  :displayname: Run scheduler (Experimental)
  :systemconsole: N/A
  :configjson: RunScheduler
  :environment: N/A
  :description: Set whether or not this Mattermost server will schedule tasks that will be completed by a Worker. Default is **true**.

Run scheduler
~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Set whether or not this Mattermost server will schedule tasks that will be completed by a Worker. When running Mattermost on a single machine, this setting should always be enabled.

When running Mattermost in :doc:`High Availablity mode </scale/high-availability-cluster>`, this setting should always be enabled. In a High Availability cluster, exactly one of the servers will be designated as the Scheduler at a time to ensure that duplicate tasks aren't created. See :doc:`High Availability documentation </scale/high-availability-cluster>` for more details.

.. warning::

   We strongly recommend that you not change this setting from the default setting of ``true`` as this prevents the ``ClusterLeader`` from being able to run the scheduler. As a result, recurring jobs such as LDAP sync, Compliance Export, and data retention will no longer be scheduled. In previous Mattermost Server versions, and this documentation, the instructions stated to run the Job Server with ``RunScheduler: false``. The cluster design has evolved and this is no longer the case.

+-----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RunScheduler": true`` with options ``true`` and ``false``.                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-cleanupjobs
  :displayname: Clean up old database jobs (Experimental)
  :systemconsole: N/A
  :configjson: .JobSettings.CleanupJobsThresholdDays
  :environment: N/A
  :description: Defines the threshold in hours beyond which older completed database jobs are removed. Must be set to a value greater than or equal to ``0`` to be enabled. Default value is **-1**

Clean up old database jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Defines the threshold in days beyond which older completed database jobs are removed. This setting is disabled by default, and must be set to a value greater than or equal to ``0`` to be enabled.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"JobSettings.CleanupJobsThresholdDays": -1`` with numerical input.     |
+--------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-cleanupdatabaseentries
  :displayname: Clean up outdated database entries (Experimental)
  :systemconsole: N/A
  :configjson: .JobSettings.CleanupConfigThresholdDays
  :environment: N/A
  :description: Defines the threshold in days beyond which outdated configurations are removed from the database. Default is **30** days.

Clean up outdated database entries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting only applies to configuration in the database. It isn't available in the System Console and can be set via mmctl or changed in the database.

Defines the threshold in days beyond which outdated configurations are removed from the database.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"JobSettings.CleanupConfigThresholdDays": 30`` with numerical input.   |
+--------------------------------------------------------------------------------------------------------------------+
