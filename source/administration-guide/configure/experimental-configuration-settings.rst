Experimental configuration settings
=====================================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Review and manage the following :ref:`experimental <administration-guide/manage/feature-labels:experimental>` configuration options in the System Console by selecting the **Product** |product-list| menu, selecting **System Console**, and then selecting **Experimental > Features**:

- `Experimental System Console configuration settings <#experimental-system-console-configuration-settings>`__
- `Experimental audit logging configuration settings <#experimental-audit-logging-configuration-settings>`__
- `Experimental job configuration settings <#experimental-job-configuration-settings>`__
- `Experimental configuration settings for self-hosted deployments only <#experimental-configuration-settings-for-self-hosted-deployments-only>`__

.. tip::

  System admins managing a self-hosted Mattermost deployment can edit the ``config.json`` file as described in the following tables. Each configuration value below includes a JSON path to access the value programmatically in the ``config.json`` file using a JSON-aware tool. For example, one ``LoginButtonColor`` value is under ``LdapSettings``.

  - If using a tool such as `jq <https://stedolan.github.io/jq/>`__, you'd enter: ``cat config/config.json | jq '.LdapSettings.LoginButtonColor'``
  - When working with the ``config.json`` file manually, look for an object such as ``LdapSettings``, then within that object, find the key ``LoginButtonColor``.

----

Experimental System Console configuration settings
--------------------------------------------------

.. config:setting:: adldap-login-button-color
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

.. config:setting:: adldap-login-button-border-color
  :displayname: AD/LDAP login button border color (Experimental)
  :systemconsole: Experimental > Features
  :configjson: LoginButtonBorderColor
  :environment: N/A
  :description: Specify the color of the AD/LDAP login button border for white labeling purposes. Use a hex code with a #-sign before the code.

AD/LDAP login button border color
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Specify the color of the AD/LDAP login button border for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile app.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonBorderColor": ""`` with string input.                                 |
+-------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: adldap-login-button-text-color
  :displayname: AD/LDAP login button text color (Experimental)
  :systemconsole: Experimental > Features
  :configjson: LoginButtonTextColor
  :environment: N/A
  :description: Specify the color of the AD/LDAP login button text for white labeling purposes. Use a hex code with a #-sign before the code.

AD/LDAP login button text color
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Specify the color of the AD/LDAP login button text for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile app.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonTextColor": ""`` with string input.                                   |
+-------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: change-authentication-method
  :displayname: Change authentication method (Experimental)
  :systemconsole: Experimental > Features
  :configjson: ExperimentalEnableAuthenticationTransfer
  :environment: N/A

  - **true**: **(Default)** Users can change their sign-in method to any that is enabled on the server, either via their Profile or the APIs.
  - **false**: Users cannot change their sign-in method, regardless of which authentication options are enabled.

Change authentication method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Users can change their sign-in method to any that is enabled on the server, either via their Profile or the APIs.

**False**: Users cannot change their sign-in method, regardless of which authentication options are enabled.

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalEnableAuthenticationTransfer": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: link-metadata-timeout
  :displayname: Link metadata timeout (Experimental)
  :systemconsole: Experimental > Features
  :configjson: LinkMetadataTimeoutMilliseconds
  :environment: N/A
  :description: Adds a configurable timeout for requests made to return link metadata. Default is **5000** milliseconds.

Link metadata timeout
~~~~~~~~~~~~~~~~~~~~~

Adds a configurable timeout for requests made to return link metadata. If the metadata is not returned before this timeout expires, the message will post without requiring metadata. This timeout covers the failure cases of broken URLs and bad content types on slow network connections.

+---------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LinkMetadataTimeoutMilliseconds``: 5000`` with numerical input.                    |
+---------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: email-batching-buffer-size
  :displayname: Email batching buffer size (Experimental)
  :systemconsole: Experimental > Features
  :configjson: EmailBatchingBufferSize
  :environment: N/A
  :description: Specify the maximum number of notifications batched into a single email. Default is **256** notifications.

Email batching buffer size
~~~~~~~~~~~~~~~~~~~~~~~~~~

Specify the maximum number of notifications batched into a single email.

.. note::
  
  - We recommend increasing the buffer size from the default value if you see the following error in the Mattermost logs: ``Email batching job's receiving buffer was full. Please increase the EmailBatchingBufferSize. Falling back to sending immediate mail.`` Increasing this value will ensure emails are queued up, without impacting server performance.
  - Notifications will be sent instantly if the queue of emails exceeds the `email batching interval <#id1>`_ configured. 

+--------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``EmailBatchingBufferSize``: 256`` with numerical input.                       |
+--------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: email-batching-interval
  :displayname: Email batching interval (Experimental)
  :systemconsole: Experimental > Features
  :configjson: EmailBatchingInterval
  :environment: N/A
  :description: Specify the maximum frequency, in seconds, which the batching job checks for new notifications. Default is **30** seconds.

Email batching interval
~~~~~~~~~~~~~~~~~~~~~~~

Specify the maximum frequency, in seconds, which the batching job checks for new notifications. 

.. note::

  - We recommend decreasing the email batching interval from the default value if you see the following error in the Mattermost logs: ``Email batching job's receiving buffer was full. Please increase the EmailBatchingBufferSize. Falling back to sending immediate mail.``. 
  - Longer batching intervals may increase performance.
  - Notifications will be sent instantly if the `queue of emails <#email-batching-buffer-size>`_ exceeds the email batching interval configured. 

+-----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``EmailBatchingInterval": 30`` with numerical input.                        |
+-----------------------------------------------------------------------------------------------------------------------+

.. config:setting:: email-login-button-color
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

.. config:setting:: email-login-button-border-color
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

.. config:setting:: email-login-button-text-color
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

.. config:setting:: enable-account-deactivation
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

.. config:setting:: enable-automatic-replies
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

.. config:setting:: enable-channel-viewed-websocket-messages
  :displayname: Enable channel viewed websocket messages (Experimental)
  :systemconsole: Experimental > Features
  :configjson: EnableChannelViewedMessages
  :environment: N/A
  :description: This setting determines whether ``channel_viewed WebSocket`` events are sent, which synchronize unread notifications across clients and devices. Default is **true**.

Enable channel viewed websocket messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting determines whether ``channel_viewed WebSocket`` events are sent, which synchronize unread notifications across clients and devices.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableChannelViewedMessages": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

.. note::

  Disabling this experimental configuration setting in larger deployments may improve server performance in the following areas:

  - Reduced Database Load: When channel_viewed events are disabled, the server no longer needs to log these events in the database. This reduces the number of write and update operations, which can be substantial in a busy server with many users frequently switching channels.
  - Decreased Network Traffic: Disabling these events means there are fewer messages sent between the server and clients. This reduction in network traffic can lower latency and improve the overall responsiveness of the server, especially for users with slower connections.
  - Lower Server CPU Usage: Processing channel_viewed events requires CPU resources to handle database transactions and network communication. Without these events, the server's CPU can be utilized more efficiently for other tasks, improving the overall performance.
  - Improved User Experience: With reduced server load and network traffic, users may experience faster loading times and a more fluid interaction with the application.
  - However, disabling this configuration setting affects some functionality, such as accurate tracking of read and unread messages in channels. It’s important to balance performance improvements with the needs of your organization and users.

.. config:setting:: enable-default-channel-leavejoin-system-messages
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

.. config:setting:: enable-hardened-mode
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
- If :doc:`multi-factor authentication (MFA) </administration-guide/onboard/multi-factor-authentication>` is enabled, the route to check if a user has MFA enabled always returns true. This causes the MFA input screen to appear even if the user does not have MFA enabled. The user may enter any value to pass the screen. Note that hardened mode does not affect user experience when MFA is enforced.
- Password reset does not inform the user that they can not reset their SSO account through Mattermost and instead claims to have sent the password reset email.
- Mattermost sanitizes all 500 errors before returned to the client. Use the supplied ``request_id`` to match user facing errors with the server logs.
- Standard users authenticated via username and password can't use post props reserved for integrations, such as ``override_username`` or ``override_icon_url``.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalEnableHardenedMode": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: enable-theme-selection
  :displayname: Enable theme selection (Experimental)
  :systemconsole: Experimental > Features
  :configjson: EnableThemeSelection
  :environment: N/A

  - **true**: **(Default)** Enables the **Display > Theme** tab in **Settings** so users can select their theme.
  - **false**: Users cannot select a different theme. The **Display > Theme** tab is hidden in **Settings**.

Enable theme selection
~~~~~~~~~~~~~~~~~~~~~~

**True**: Enables the **Display > Theme** tab in **Settings** so users can select their theme.

**False**: Users cannot select a different theme. The **Display > Theme** tab is hidden in **Settings**.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableThemeSelection": true`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------+

.. config:setting:: allow-custom-themes
  :displayname: Allow custom themes (Experimental)
  :systemconsole: Experimental > Features
  :configjson: AllowCustomThemes
  :environment: N/A

  - **true**: **(Default)** Enables the **Display > Theme > Custom Theme** section in **Settings**.
  - **false**: Users cannot use a custom theme. The **Display > Theme > Custom Theme** section is hidden in **Settings**.

Allow custom themes
~~~~~~~~~~~~~~~~~~~

**True**: Enables the **Display > Theme > Custom Theme** section in **Settings**.

**False**: Users cannot use a custom theme. The **Display > Theme > Custom Theme** section is hidden in **Settings**.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowCustomThemes": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

.. config:setting:: default-theme
  :displayname: Default theme (Experimental)
  :systemconsole: Experimental > Features
  :configjson: DefaultTheme
  :environment: N/A
  :description: Set a default theme that applies to all new users on the system. Default is **default**.

Default theme
~~~~~~~~~~~~~

Set a default theme that applies to all new users on the system.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DefaultTheme": "default"`` with options ``"default"``, ``"organization"``, ``"mattermostDark"``, and ``"windows10"``. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: enable-tutorial
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
| This feature's ``config.json`` setting is ``"ServiceSettings.EnableTutorial": true`` with options ``true`` and ``false``.                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: enable-onboarding-flow
  :displayname: Enable onboarding flow (Experimental)
  :systemconsole: Experimental > Features
  :configjson: EnableOnboardingFlow
  :environment: N/A

  - **true**: **(Default)** New Mattermost users are shown key tasks to complete as part of initial onboarding.
  - **false**: User onboarding tasks are disabled. Users are placed in Town Square when they open Mattermost for the first time after account creation.

Enable onboarding flow
~~~~~~~~~~~~~~~~~~~~~~

**True**: New Mattermost users are shown key tasks to complete as part of initial onboarding.

**False**: User onboarding tasks are disabled. Users are placed in Town Square when they open Mattermost for the first time after account creation.

+--------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ServiceSettings.EnableOnboardingFlow": true`` with options ``true`` and ``false``.            |
+--------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: enable-user-typing-messages
  :displayname: Enable user typing messages (Experimental)
  :systemconsole: Experimental > Features
  :configjson: EnableUserTypingMessages
  :environment: N/A
  :description: This setting determines whether "user is typing..." messages are displayed below the message box. Default is **true**.

Enable user typing messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting determines whether "user is typing..." messages are displayed below the message box when using Mattermost in a web browser or the desktop app. 

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserTypingMessages": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------------+

.. note::

  Disabling this experimental configuration setting in larger deployments may improve server performance in the following areas:

  - Reduced Server Load: Typing events generate additional websocket traffic. Disabling them can reduce the amount of data that needs to be handled by the server, improving the overall response time and decreasing server load.
  - Lower Network Traffic: When typing events are enabled, every keystroke generates a network event. This can lead to a significant amount of network traffic, particularly in busy channels. Disabling these events reduces the amount of information transmitted over the network.
  - Client Performance: On the client side, processing typing events requires resources. By not having to handle these events, the client can be more responsive and use less memory and CPU.

.. config:setting:: user-typing-timeout
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

.. config:setting:: users-status-and-profile-fetching-poll-interval
  :displayname: User's status and profile fetching poll interval (Experimental)
  :systemconsole: Experimental > Features
  :configjson: UsersStatusAndProfileFetchingPollIntervalMilliseconds
  :environment: N/A
  :description: The number of milliseconds to wait between fetching user statuses and profiles periodically.

User's status and profile fetching poll interval
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting configures the number of milliseconds to wait between fetching user statuses and profiles periodically. Set to ``0`` to disable.

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalSettings.UsersStatusAndProfileFetchingPollIntervalMilliseconds": 3000`` with numerical input. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

  Decrease this configuration setting value to increase how often Mattermost checks for and retrieves updated user profile datails. Reducing this value can be particularly helpful to reduce the likelyhood of usernames being displayed in channels as **Someone** due to outdated or missing data.

.. config:setting:: primary-team
  :displayname: Primary team (Experimental)
  :systemconsole: Experimental > Features
  :configjson: ExperimentalPrimaryTeam
  :environment: N/A
  :description: The primary team of which users on the server are members. When a primary team is set, the options to join other teams or leave the primary team are disabled.

Primary team
~~~~~~~~~~~~

The primary team of which users on the server are members. When a primary team is set, the options to join other teams or leave the primary team are disabled.

If the team URL of the primary team is ``https://example.mattermost.com/myteam/``, then set the value to ``myteam`` in ``config.json``.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalPrimaryTeam": ""`` with string input.                  |
+-----------------------------------------------------------------------------------------------------------------+

.. config:setting:: saml-login-button-color
  :displayname: SAML login button color (Experimental)
  :systemconsole: Experimental > Features
  :configjson: LoginButtonColor
  :environment: N/A
  :description: Specify the color of the SAML login button for white labeling purposes. Use a hex code with a #-sign before the code.

SAML login button color
~~~~~~~~~~~~~~~~~~~~~~~

Specify the color of the SAML login button for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile app.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonColor": ""`` with string input.                                       |
+-------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: saml-login-button-border-color
  :displayname: SAML login button border color (Experimental)
  :systemconsole: Experimental > Features
  :configjson: LoginButtonBorderColor
  :environment: N/A
  :description: Specify the color of the SAML login button border for white labeling purposes. Use a hex code with a #-sign before the code.

SAML login button border color
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Specify the color of the SAML login button border for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile app.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonBorderColor": ""`` with string input.                                 |
+-------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: saml-login-button-text-color
  :displayname: SAML login button text color (Experimental)
  :systemconsole: Experimental > Features
  :configjson: LoginButtonTextColor
  :environment: N/A
  :description: Specify the color of the SAML login button text for white labeling purposes. Use a hex code with a #-sign before the code.

SAML login button text color
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Specify the color of the SAML login button text for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile app.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonTextColor": ""`` with string input.                                   |
+-------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: use-channel-name-in-email-notifications
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

.. config:setting:: user-status-away-timeout
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

Disable data refetching on browser refocus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting disables re-fetching of channel and channel members on browser focus.

**True**: Mattermost won't refetch channels and channel members when the browser regains focus. This may result in improved performance for users with many channels and channel members.

**False**: (Default) Mattermost will refetch channels and channel members when the browser regains focus.

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalSettings.DisableRefetchingOnBrowserFocus": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

Disable wake up reconnect handler
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting disables attempts to detect when the computer has woken up and refetch data.

**True**: Mattermost won't attempt to detect when the computer has woken up and refetch data. This might reduce the amount of regular network traffic the app is sending.

**False**: (**Default**) Mattermost attempts to detect when the computer has woken up and refreshes data.

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalSettings.DisableWakeUpReconnectHandler": false`` with options ``true`` and ``false``.   |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

Delay channel autocomplete
~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting controls whether or not the channel link autocomplete triggers immediately when after a tilde is typed when composing a message. This setting makes the channel autocomplete, such as ``~town-square``, less obtrusive for people who use tildes ``~`` as punctuation. 

**True**: The autocomplete appears after the user types a tilde followed by two or more characters. For example, typing ``~to`` will show the autocomplete, but typing ``~`` will not. 

**False**: **(Default)** The autocomplete appears immediately after the user types a tilde. For example, typing ``~`` will show the autocomplete.

+-------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalSettings.DelayChannelAutocomplete": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------------------+

YouTube referrer policy
~~~~~~~~~~~~~~~~~~~~~~~

This setting resolves issues where YouTube video previews display as unavailable.

**True**: The referrer policy for embedded YouTube videos is set to ``strict-origin-when-cross-origin``.

**False**: (Default) The referrer policy is set to ``no-referrer`` which enhances user privacy by not disclosing the source URL, but limits the ability to track user engagement and traffic sources in analytics tools.

+-------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalSettings.YoutubeReferrerPolicy": false`` with options ``true`` and ``false``.    |
+-------------------------------------------------------------------------------------------------------------------------------------------+

----

Experimental Bleve configuration settings
-----------------------------------------

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

.. important::
  **From Mattermost v11, Bleve search has been deprecated.** These configuration settings are only available for Mattermost versions prior to v11.0. For v11.0 and later, :doc:`Elasticsearch </administration-guide/scale/elasticsearch-setup>` or :doc:`OpenSearch </administration-guide/scale/opensearch-setup>` for :doc:`enterprise search </administration-guide/scale/enterprise-search>` capabilities.

Access the following configuration settings in the System Console by going to **Experimental > Bleve**, or by editing the ``config.json`` file as described in the following tables:

.. config:setting:: enable-bleve-indexing
  :displayname: Enable Bleve indexing (Experimental)
  :systemconsole: Experimental > Bleve
  :configjson: EnableIndexing
  :environment: N/A

  - **true**: The indexing of new posts occurs automatically.
  - **false**: **(Default)** The indexing of new posts does not occur automatically.

Enable Bleve indexing
~~~~~~~~~~~~~~~~~~~~~

**True**: The indexing of new posts occurs automatically. Search queries will not use bleve search until :ref:`Enable Bleve for search queries <administration-guide/configure/experimental-configuration-settings:enable bleve for search queries>` is enabled.

**False**: The indexing of new posts does not occur automatically.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableIndexing": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

.. config:setting:: index-directory
  :displayname: Index directory (Experimental)
  :systemconsole: Experimental > Bleve
  :configjson: IndexDir
  :environment: N/A
  :description: Directory path to use for storing bleve indexes.

Index directory
~~~~~~~~~~~~~~~

Directory path to use for storing bleve indexes.

.. tip::

   The bleve index directory path isn't required to exist within the ``mattermost`` directory. When it exists outside of the ``mattermost`` directory, no  additional steps are needed to preserve or reindex these files as part of a Mattermost upgrade. See our :doc:`Upgrading Mattermost Server </administration-guide/upgrade/upgrading-mattermost-server>` documentation for details.

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

**True**: Search queries will use bleve search.

**False**: Search queries will not use bleve search.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSearching": false`` with options ``true`` and ``false``.  |
+--------------------------------------------------------------------------------------------------------------+

.. config:setting:: enable-bleve-indexingautocomplete
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

Experimental audit logging configuration settings
--------------------------------------------------------

Enable the following settings to output audit events in the System Console by going to **Compliance > Audit Logging**, or in the ``config.json`` file. 

.. note::

  The ability to enable and configure audit logging is currently in :ref:`Beta <administration-guide/manage/feature-labels:beta>`.

.. config:setting:: advanced-logging
  :displayname: Advanced Logging (Audit Logging > Cloud)
  :systemconsole: Experimental > Features
  :configjson: AdvancedLoggingJSON
  :environment: N/A
  :description: Output log and audit records to any combination of console, local file, syslog, and TCP socket targets for a Mattermost Cloud deployment.

Advanced logging
~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

Output log and audit records to any combination of console, local file, syslog, and TCP socket targets for a Mattermost Cloud deployment. See the :ref:`advanced logging <administration-guide/manage/logging:advanced logging>` documentation for details about logging options.

.. config:setting:: enable-audit-logging
  :displayname: Enable audit logging (Audit Logging > Self-Hosted)
  :systemconsole: Experimental > Features
  :configjson: FileEnabled
  :environment: N/A
  :description: Write audit files locally for a self-hosted deployment.

Enable audit logging
~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

When audit logging is enabled in a self-hosted instance, you can specify size, backup interval, compression, maximium age to manage file rotation, and timestamps for audit logging, as defined below. You can specify these settings independently for audit events and AD/LDAP events. 

**True**: Audit logging files are enabled, and audit files are written locally to a file for a self-hosted deployment.

**False**: Audit logging files aren't enabled, and audit logs aren't written locally to a file for a self-hosted deployment.

+--------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``".ExperimentalAuditSettings.FileEnabled": false",`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: file-name
  :displayname: File name (Audit Logging > Self-Hosted)
  :systemconsole: Experimental > Features
  :configjson: FileName
  :environment: N/A
  :description: Specify the path to the audit file for a self-hosted deployment.

File name
~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

Specify the path to the audit file for a self-hosted deployment.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``".ExperimentalAuditSettings.FileName": ""`` with string input consisting of a user-defined path (e.g. ``/var/log/mattermost_audit.log``).         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: max-file-size
  :displayname: File max size MB (Audit Logging > Self-Hosted)
  :systemconsole: Experimental > Features
  :configjson: FileMaxSizeMB
  :environment: N/A
  :description: This is the maximum size (measured in megabytes) that the file can grow before triggering rotation for a self-hosted deployment.. Default is **100** MB.

Max file size
~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

This is the maximum size, in megabytes, that the file can grow before triggering rotation for a self-hosted deployment. The default setting is ``100``.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``".ExperimentalAuditSettings.FileMaxSizeMB": 100`` with numerical input. |
+---------------------------------------------------------------------------------------------------------------------+

.. config:setting:: max-file-age
  :displayname: File max age days (Audit Logging > Self-Hosted)
  :systemconsole: Experimental > Features
  :configjson: FileMaxAgeDays
  :environment: N/A
  :description: This is the maximum age in days a file can reach before triggering rotation for a self-hosted deployment.. The default value is **0**, indicating no limit on the age.

Max file age
~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

This is the maximum age, in days, a file can reach before triggering rotation for a self-hosted deployment. The default value is ``0``, indicating no limit on the age.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``".ExperimentalAuditSettings.FileMaxAgeDays": 0`` with numerical input. |
+--------------------------------------------------------------------------------------------------------------------+

.. config:setting:: maximum-file-backups
  :displayname: File max backups (Audit Logging > Self-Hosted)
  :systemconsole: Experimental > Features
  :configjson: FileMaxBackups
  :environment: N/A
  :description: This is the maximum number of rotated files kept for a self-hosted deployment. The oldest is deleted first. The default value is **0**, indicating no limit on the number of backups.

Maximum file backups
~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

This is the maximum number of rotated files kept for a self-hosted deployment. The oldest is deleted first. The default value is ``0``, indicating no limit on the number of backups.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``".ExperimentalAuditSettings.FileMaxBackups": 0`` with numerical input. |
+--------------------------------------------------------------------------------------------------------------------+

.. config:setting:: file-compression
  :displayname: File compress (Audit Logging > Self-Hosted)
  :systemconsole: Experimental > Features
  :configjson: FileCompress
  :environment: N/A
  :description: When ``true``, rotated files are compressed using ``gzip`` in a self-hosted deployment. Default value is **false**.

File compression
~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

When ``true``, rotated files are compressed using ``gzip`` in a self-hosted deployment.

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``".ExperimentalAuditSettings.FileCompress": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: maximum-file-queue
  :displayname: File max queue size (Audit Logging > Self-Hosted)
  :systemconsole: Experimental > Features
  :configjson: FileMaxQueueSize
  :environment: N/A
  :description: This setting determines how many audit records can be queued/buffered at any point in time when writing to a file for a self-hosted deployment. Default is **1000** records.

Maximum file queue 
~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

This setting determines how many audit records can be queued/buffered at any point in time when writing to a file for a self-hosted deployment. The default is ``1000`` records.
This setting can be left as default unless you are seeing audit write failures in the server log and need to adjust the number accordingly.

+-------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``".ExperimentalAuditSettings.FileMaxQueueSize": 1000`` with numerical input. |
+-------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: audit-logging-certificate
  :displayname: Audit logging certificate upload (Audit Logging > Cloud Enterprise)
  :systemconsole: Audit Log Settings > Certificate
  :configjson: N/A
  :environment: N/A
  :description: Cloud Enterprise customers can upload and manage a certificate for audit logging encryption on Syslog or TCP logging targets.

Certificate
~~~~~~~~~~~~

Cloud Enterprise customers can upload and manage a certificate for audit logging encryption on Syslog or TCP logging targets. The ability to upload a certificate is only available when the feature flag ``ExperimentalAuditSettingsSystemConsoleUI`` is enabled.

Upload the certificate PEM file in the System Console by going to **System Console > Audit Log Settings > Certificate** and selecting **File/Remove Certificate**. The certificate file can be stored in the filestore or stored locally on the filesystem. 

.. config:setting:: advanced-logging
  :displayname: Advanced Logging (Audit Logging > Self-Hosted)
  :systemconsole: Experimental > Features
  :configjson: AdvancedLoggingJSON
  :environment: N/A
  :description: Output log and audit records to any combination of console, local file, syslog, and TCP socket targets for a Mattermost self-hosted deployment.

Experimental configuration settings for self-hosted deployments only
--------------------------------------------------------------------

Access the following self-hosted configuration settings by editing the ``config.json`` file as described in the following tables. These configuration settings are not accessible through the System Console.

.. tip::

  Each configuration value below includes a JSON path to access the value programmatically in the ``config.json`` file using a JSON-aware tool. For example, the ``SiteURL`` value is under ``ServiceSettings``.

  - If using a tool such as `jq <https://stedolan.github.io/jq/>`__, you'd enter: ``cat config/config.json | jq '.ServiceSettings.SiteURL'``
  - When working with the ``config.json`` file manually, look for the key ``ServiceSettings``, then within that object, find the key ``SiteURL``.

.. config:setting:: allowed-themes
  :displayname: Allowed themes (Experimental)
  :systemconsole: N/A
  :configjson: AllowedThemes
  :environment: N/A
  :description: Select the themes that can be chosen by users when ``EnableThemeSelection`` is set to ``true``.

Allowed themes
~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Select the themes that can be chosen by users when ``EnableThemeSelection`` is set to ``true``.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowedThemes": []`` with string array input consisting of the options ``"default"``, ``"organization"``, ``"mattermostDark"``, and ``"windows10"``, such as ``["mattermostDark", "windows10"]``.     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: file-location
  :displayname: File location (Experimental)
  :systemconsole: N/A
  :configjson: FileLocation
  :environment: N/A
  :description: Set the file location of the compliance exports. Default value is **export**.

File Location
~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

Set the file location of the compliance exports. By default, they are written to the ``exports`` subdirectory of the configured :ref:`Local Storage directory <administration-guide/configure/environment-configuration-settings:local storage directory>`.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileLocation": "export"`` with string input. |
+-------------------------------------------------------------------------------------------+

.. config:setting:: push-notification-buffer
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

.. config:setting:: restrict-system-admin
  :displayname: File configuration settings
  :systemconsole: N/A
  :configjson: FileEnabled
  :environment: N/A
  :description: Enable this setting to write audit files locally, specifying size, backup interval, compression, maximum age to manage file rotation, and timestamps. Default value is **false**.

Restrict system admin
~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: **(Default for Cloud deployments)** Restricts the system admin from viewing and modifying a subset of server configuration settings from the System Console. Not recommended for use in on-prem installations. This is intended to support Mattermost Private Cloud in giving the system admin role to users but restricting certain actions only for Cloud Admins.

**False**: **(Default for self-host deployments)** No restrictions are applied to the system admin role.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictSystemAdmin": "false"`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

.. note::

  The ability to restrict the system admin from viewing and modifying a subset of server configuration settings is currently in :ref:`Beta <administration-guide/manage/feature-labels:beta>`.


.. config:setting:: enable-client-side-certification
  :displayname: Enable client-side certification (Experimental)
  :systemconsole: N/A
  :configjson: ClientSideCertEnable
  :environment: N/A

  - **true**: Enables client-side certification for your Mattermost server.
  - **false**: **(Default)** Client-side certification is disabled.

Enable client-side certification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

.. important::

  **Certificate-based authentication has been deprecated from Mattermost v11.0.** This setting must be set to ``false`` to start the server from v11. Setting this to ``true`` will prevent the server from starting.

**True**: Enables client-side certification for your Mattermost server. See :doc:`the documentation </administration-guide/onboard/certificate-based-authentication>` to learn more.

**False**: **(Default)** Client-side certification is disabled.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ClientSideCertEnable": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

.. config:setting:: client-side-certification-login-method
  :displayname: Client-side certification login method (Experimental)
  :systemconsole: N/A
  :configjson: ClientSideCertCheck
  :environment: N/A

  - **primary**: After the client side certificate is verified, user's email is retrieved from the certificate and is used to log in without a password.
  - **secondary**: **(Default)** After the client side certificate is verified, user's email is retrieved from the certificate and matched against the one supplied by the user. If they match, the user logs in with regular email/password credentials.

Client-side certification login method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

.. important::

  **Certificate-based authentication has been deprecated from Mattermost v11.0.** This setting is no longer functional from Mattermost v11.0 and should be left at the default value.

This configuration setting is used in combination with the ``ClientSideCertEnable`` configuration setting and has the following possible values:

**Primary**: After the client side certificate is verified, user's email is retrieved from the certificate and is used to log in without a password.

**Secondary**: **(Default)** After the client side certificate is verified, user's email is retrieved from the certificate and matched against the one supplied by the user. If they match, the user logs in with regular email/password credentials.

+----------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ClientSideCertCheck": "secondary"`` with options ``"primary"`` and ``"secondary"``. |
+----------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: export-output-directory
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

.. config:setting:: export-retention-days
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

.. config:setting:: maximum-image-resolution
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

.. config:setting:: maximum-image-decoder-concurrency
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

  - This configuration setting affects the total memory consumption of the server. The maximum memory of a single image is dictated by ``MaxImageResolution * 24 bytes``, where the default maximum image resolution value is 33MB.
  - Therefore, a good rule of thumb to follow is that ``33MB * MaxImageDecoderConcurrency * 24`` should be less than the total memory for the server. 
  - For example, if you have a 4-core server, you should leave aside at least ``33 * 4 * 24 = 3168MB`` memory for image processing. Otherwise, adjust the `MaxImageResolution <#maximum-image-resolution>`_ configuration setting to adjust the amount of memory needed for image processing.

+--------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxImageDecoderConcurrency": "-1"`` with numerical input. |
+--------------------------------------------------------------------------------------------------------+

.. config:setting:: initial-font
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

.. config:setting:: amazon-s3-signature-v2
  :displayname: Amazon S3 signature v2 (Experimental)
  :systemconsole: N/A
  :configjson: AmazonS3SignV2
  :environment: N/A

  - **true**: Use Signature Version 2 Signing Process.
  - **false**: **(Default)** Use Signature Version 4 Signing Process.

Amazon S3 signature v2
~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

By default, Mattermost uses Signature V4 to sign API calls to AWS, but under some circumstances, V2 is required. For more information about when to use V2, see https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html.

**True**: Use Signature Version 2 Signing Process.

**False**: Use Signature Version 4 Signing Process.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3SignV2": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

.. config:setting:: amazon-s3-path
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

.. config:setting:: gitlab-scope
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

.. config:setting:: global-relay-smtp-server-timeout
  :displayname: Global relay SMTP server timeout (Experimental)
  :systemconsole: N/A
  :configjson: GlobalRelaySettings.SMTPServerTimeout
  :environment: N/A
  :description: The number of seconds that can elapse before the connection attempt to the SMTP server is abandoned. Default is **1800** seconds.

Global relay SMTP server timeout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

The number of seconds that can elapse before the connection attempt to the SMTP server is abandoned. The default value is 1800 seconds. This setting is currently not available in the System Console and can only be set in ``config.json``.

+-----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GlobalRelaySettings.SMTPServerTimeout": "1800"`` with numerical input.   |
+-----------------------------------------------------------------------------------------------------------------------+

.. config:setting:: google-scope
  :displayname: Google scope (Experimental)
  :systemconsole: N/A
  :configjson: Scope
  :environment: N/A
  :description: Standard setting for OAuth to determine the scope of information shared with OAuth client. Default value is **profile email**.

Google scope
~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Standard setting for OAuth to determine the scope of information shared with OAuth client. Recommended setting is ``profile email``.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Scope": "profile email"`` with string input. |
+-------------------------------------------------------------------------------------------+

.. config:setting:: import-input-directory
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

.. config:setting:: import-retention-days
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

.. config:setting:: export-from-timestamp
  :displayname: Export from timestamp (Experimental)
  :systemconsole: N/A
  :configjson: ExportFromTimestamp
  :environment: N/A
  :description: Set the Unix timestamp (seconds since epoch, UTC) to export data from. Default is **0**.

Export from timestamp
~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

Set the Unix timestamp (seconds since epoch, UTC) to export data from.

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExportFromTimestamp": 0`` with numerical input. |
+----------------------------------------------------------------------------------------------+


.. config:setting:: entra-id-scope
  :displayname: Entra ID scope (Experimental)
  :systemconsole: N/A
  :configjson: Scope
  :environment: N/A
  :description: Standard setting for OAuth to determine the scope of information shared with OAuth client. Recommended setting is ``User.Read``.

Entra ID Scope
~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Standard setting for OAuth to determine the scope of information shared with OAuth client. Recommended setting is ``User.Read``.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Scope": "User.Read"`` with string input. |
+---------------------------------------------------------------------------------------+

.. config:setting:: enable-plugin-uploads
  :displayname: Enable plugin uploads (Experimental)
  :systemconsole: N/A
  :configjson: EnableUploads
  :environment: N/A

  - **true**: Enables plugin uploads by system admins at **Plugins > Management**.
  - **false**: **(Default)** Disables plugin uploads on your Mattermost server.

Enable plugin uploads
~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables plugin uploads by system admins at **Plugins > Management**. If you do not plan to upload a plugin, set to ``false`` to control which plugins are installed on your server. See `documentation <https://developers.mattermost.com/integrate/admin-guide/admin-plugins-beta/>`__ to learn more.

**False**: Disables plugin uploads on your Mattermost server.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUploads": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------+

.. config:setting:: allow-insecure-download-url
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

.. config:setting:: enable-plugin-health-check
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

.. config:setting:: plugin-directory
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

.. config:setting:: client-plugin-directory
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

.. config:setting:: scoping-idp-provider-id
  :displayname: Scoping IDP provider ID (Experimental)
  :systemconsole: N/A
  :configjson: ScopingIDPProviderId
  :environment: N/A
  :description: Allows an authenticated user to skip the initial login page of their federated Azure AD server, and only require a password to log in.

Scoping IDP provider ID
~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Allows an authenticated user to skip the initial login page of their federated Azure AD server, and only require a password to log in.

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ScopingIDPProviderId": ""`` with string input. |
+---------------------------------------------------------------------------------------------+

.. config:setting:: scoping-idp-provider-name
  :displayname: Scoping IDP provider name (Experimental)
  :systemconsole: N/A
  :configjson: ScopingIDPName
  :environment: N/A
  :description: Adds the name associated with a user's Scoping Identity Provider ID.

Scoping IDP provider name
~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Adds the name associated with a user's Scoping Identity Provider ID.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ScopingIDPName": ""`` with string input. |
+---------------------------------------------------------------------------------------+

.. config:setting:: group-unread-channels
  :displayname: Group unread channels (Experimental)
  :systemconsole: N/A
  :configjson: ExperimentalGroupUnreadChannels
  :environment: N/A

  - **default_off**: **(Default)** Disables the unread channels sidebar section for all users by default. Users can enable it in **Settings > Sidebar > Group unread channels separately**.
  - **default_on**: Enables the unread channels sidebar section for all users by default. Users can disable it in **Settings > Sidebar > Group unread channels separately**.

Group unread channels
~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

This setting applies to the new sidebar only. You must disable the :ref:`Enable Legacy Sidebar <administration-guide/configure/deprecated-configuration-settings:enable legacy sidebar>` configuration setting to see and enable this functionality in the System Console.

**Default Off**: Disables the unread channels sidebar section for all users by default. Users can enable it in **Settings > Sidebar > Group unread channels separately**.

**Default On**: Enables the unread channels sidebar section for all users by default. Users can disable it in **Settings > Sidebar > Group unread channels separately**.

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalGroupUnreadChannels": "default_off"`` with options ``"default_off"`` and ``"default_on"``. |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: enable-channel-category-sorting
  :displayname: Enable channel category sorting (Experimental)
  :systemconsole: Experimental > Features
  :configjson: ExperimentalEnableChannelCategorySorting
  :environment: N/A

  - **true**: Users can assign channels to new or existing channel categories when creating or renaming channels.
  - **false**: **(Default)** Disables the ability to assign channels to new or existing channel categories when creating or renaming channels.

Enable channel category sorting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From Mattermost v10.10, when this :ref:`experimental <administration-guide/manage/feature-labels:experimental>` feature is enabled, users can assign channels to new or existing channel categories when creating or renaming channels. 

**This configuration setting applies only to cloud-based deployments.**

**True**: Users can assign channels to new or existing channel categories when creating or renaming channels.

**False**: **(Default)** Disables the ability to automatically assign channels to new or existing channel categories.

+------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalEnableChannelCategorySorting": false`` with options ``true`` and ``false``.     |
+------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: strict-csrf-token-enforcement
  :displayname: Strict CSRF token enforcement (Experimental)
  :systemconsole: N/A
  :configjson: ExperimentalStrictCSRFEnforcement
  :environment: N/A

  - **true**: Enables CSRF protection tokens for additional hardening compared to the currently used custom header.
  - **false**: **(Default)** Disables CSRF protection tokens and enables legacy X-Requested-With header fallback.

Strict CSRF token enforcement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables CSRF protection tokens for additional hardening compared to the currently used custom header. When the user logs in, an additional cookie is created with the CSRF token contained.

**False**: Disables CSRF protection tokens and enables legacy X-Requested-With header fallback for backward compatibility.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalStrictCSRFEnforcement": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: developer-flags
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

This configuration setting is disabled by default and requires :ref:`developer mode <administration-guide/configure/environment-configuration-settings:enable developer mode>` to be enabled.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DeveloperFlags": ""`` with string input.  |
+----------------------------------------------------------------------------------------+

.. config:setting:: enable-post-search
  :displayname: Enable post search (Experimental)
  :systemconsole: N/A
  :configjson: EnablePostSearch
  :environment: N/A
  :description: If this setting is enabled, users can search messages. Default is **true**.

Enable post search
~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

If this setting is enabled, users can search for messages in their Mattermost instance.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostSearch": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

.. note::

  Disabling this experimental configuration setting in larger deployments may improve server performance in the following areas:

  - Reduced Database Load: When post search is enabled, every search query adds additional load to the database. Disabling search reduces these queries, leading to better database performance and lower response times for other operations.
  - Lower Memory Usage: Search functionality often requires indexing of posts, which consumes memory. By disabling search, the memory required for maintaining these indexes is freed up for other uses, improving overall system performance.
  - Faster Write Operations: When post search is enabled, indexing has to be updated with every new post, edit, or deletion. Disabling search avoids this overhead, allowing for faster write operations.
  - Performance Consistency: Without the search feature, the application avoids potential performance bottlenecks and can maintain more consistent performance levels, especially under heavy usage scenarios with a high number of posts.
  - Simplified System Maintenance: Managing search indexes can be complex and resource-intensive. Disabling search simplifies this aspect of system maintenance, potentially reducing the risk of performance issues related to search index corruption or degradation.
  - However, the ability to search messages in Mattermost is a critical feature for many users, and disabling this feature will result in users seeing an error if they attempt to use the Mattermost Search box. It’s important to balance performance improvements with the needs of your organization and users.

.. config:setting:: enable-file-search
  :displayname: Enable file search (Experimental)
  :systemconsole: N/A
  :configjson: EnableFileSearch
  :environment: N/A
  :description: This configuration setting enables users to search documents attached to messages by filename. Default is **true**.

Enable file search
~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

.. important::

  This experimental configuration setting enables users to search documents attached to messages by filename. To enable users to search documents by their content, you must also enable the ``ExtractContent`` configuration setting. See our :ref:`Enable Document Search by Content <administration-guide/configure/environment-configuration-settings:enable document search by content>` documentation for details. Document content search is available in Mattermost Server from v5.35, with mobile support coming soon.

**True**: Supported document types are searchable by their filename.

**False**: File-based searches are disabled.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableFileSearch": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

.. note::

  Disabling this experimental configuration setting in larger deployments may improve server performance in the following areas:

  - Less Data to Index: Indexing files in addition to messages adds to the amount of data that needs to be processed and stored in the search index.
  - Fewer Complex Queries: Searching through files can require more complex queries, which can be more resource-intensive and time-consuming as compared to searching through messages alone.
  - Lower IO Operations: Searching files can generate more input/output operations, impacting the overall disk performance, especially if the system handles a large volume of file uploads and searches.
  - However, the ability to search for files in Mattermost is a critical feature for many users, and disabling this feature will result in users seeing an error if they attempt to use the Mattermost Search box. It’s important to balance performance improvements with the needs of your organization and users.

.. config:setting:: enable-user-status-updates
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

.. config:setting:: websocket-secure-port
  :displayname: Websocket secure port (Experimental)
  :systemconsole: N/A
  :configjson: WebsocketSecurePort
  :environment: N/A
  :description: This setting defines the port on which the secured WebSocket will listen using the ``wss`` protocol. Default is **443**.

Websocket secure port
~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``. Changes to this setting require a server restart before taking effect.

(Optional) This setting defines the port on which the secured WebSocket is listening using the ``wss`` protocol. Defaults to ``443``. When the client attempts to make a WebSocket connection it first checks to see if the page is loaded with HTTPS. If so, it will use the secure WebSocket connection. If not, it will use the unsecure WebSocket connection. IT IS HIGHLY RECOMMENDED PRODUCTION DEPLOYMENTS ONLY OPERATE UNDER HTTPS AND WSS.

+------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"WebsocketSecurePort": 443`` with numerical input. |
+------------------------------------------------------------------------------------------------+

.. note::
   This is a client only override that doesn't affect the listening port of the server process which is controlled by the :ref:`Web server listen address <administration-guide/configure/environment-configuration-settings:web server listen address>` setting.

.. config:setting:: websocket-port
  :displayname: Websocket port (Experimental)
  :systemconsole: N/A
  :configjson: WebsocketPort
  :environment: N/A
  :description: This setting defines the port on which the unsecured WebSocket will listen using the ``ws`` protocol. Default is **80**.

Websocket port
~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``. Changes to this setting require a server restart before taking effect.

(Optional) This setting defines the port on which the unsecured WebSocket is listening using the ``ws`` protocol. Defaults to ``80``. When the client attempts to make a WebSocket connection it first checks to see if the page is loaded with HTTPS. If so, it will use the secure WebSocket connection. If not, it will use the unsecure WebSocket connection. IT IS HIGHLY RECOMMENDED PRODUCTION DEPLOYMENTS ONLY OPERATE UNDER HTTPS AND WSS.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``WebsocketPort": 80`` with numerical input. |
+----------------------------------------------------------------------------------------+

.. note::
   This is a client only override that doesn't affect the listening port of the server process which is controlled by the :ref:`Web server listen address <administration-guide/configure/environment-configuration-settings:web server listen address>` setting.


.. config:setting:: enable-local-mode-for-mmctl
  :displayname: Enable local mode for mmctl (Experimental)
  :systemconsole: N/A
  :configjson: EnableLocalMode
  :environment: N/A

  - **true**: Enables local mode for mmctl.
  - **false**: **(Default)** Prevents local mode for mmctl.

Enable local mode for mmctl
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This self-hosted deployment setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables local mode for mmctl.

**False**: Prevents local mode for mmctl.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableLocalMode": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

.. tip::

  When trying to use local mode with mmctl, ensure you're using the same user when running the server and mmctl, or clean up the socket file before switching to a new user. If you encounter an error like ``socket file "/var/tmp/mattermost_local.socket" doesn't exists, please check the server configuration for local mode``, this can be resolved by setting this configuration setting to ``true``.

.. config:setting:: enable-local-mode-socket-location
  :displayname: Enable local mode socket location (Experimental)
  :systemconsole: N/A
  :configjson: LocalModeSocketLocation
  :environment: N/A
  :description: The path for the socket that the server will create for mmctl to connect and communicate through local mode. Default value is **/var/tmp/mattermost_local.socket**.

Enable local mode socket location
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This self-hosted deployment setting isn't available in the System Console and can only be set in ``config.json``.

The path for the socket that the server will create for mmctl to connect and communicate through local mode. If the default value for this key is changed, you will need to point mmctl to the new socket path when in local mode, using the ``--local-socket-path /new/path/to/socket`` flag in addition to the ``--local`` flag.

If nothing is specified, the default path that both the server and mmctl assumes is ``/var/tmp/mattermost_local.socket``.

+--------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LocalModeSocketLocation": "/var/tmp/mattermost_local.socket"`` with string input. |
+--------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: default-channels
  :displayname: Default channels (Experimental)
  :systemconsole: N/A
  :configjson: ExperimentalDefaultChannels
  :environment: N/A
  :description: Default channels every user is added to automatically after joining a new team. Only applies to Public channels, but affects all teams on the server.

Default channels
~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Default channels every user is added to automatically after joining a new team. Only applies to Public channels, but affects all teams on the server.

When not set, every user is added to the ``town-square`` channel by default.

.. note::

  Even if ``town-square`` isn't listed, every user is added to that channels automatically when joining a new team.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalDefaultChannels": []`` with string array input consisting of channel names, such as ``["announcement", "developers"]``. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

Experimental job configuration settings
---------------------------------------

With self-hosted deployments, you can configure how Mattermost schedules and completes periodic tasks such as the deletion of old posts with Data Retention enabled or indexing posts with Elasticsearch. These settings control which Mattermost servers are designated as a Scheduler, a server that queues the tasks at the correct times, and as a Worker, a server that completes the given tasks.

When running Mattermost on a single machine, both ``RunJobs`` and ``RunScheduler`` should be enabled. Without both of these enabled, Mattermost will not function properly.

When running Mattermost in High Availability mode, ``RunJobs`` should be enabled on one or more servers while ``RunScheduler`` should be enabled on all servers under normal circumstances. A High Availability cluster-based deployment will have one Scheduler and one or more Workers. See the below sections for more information.

.. config:setting:: run-jobs
  :displayname: Run jobs (Experimental)
  :systemconsole: N/A
  :configjson: RunJobs
  :environment: N/A
  :description: Set whether or not this Mattermost server will handle tasks created by the Scheduler. Default is **true**.

Run jobs
~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Set whether or not this Mattermost server will handle tasks created by the Scheduler. When running Mattermost on a single machine, this setting should always be enabled.

When running Mattermost in :doc:`High Availablity mode </administration-guide/scale/high-availability-cluster-based-deployment>`, one or more servers should have this setting enabled. We recommend that your High Availability cluster-based deployment has one or more dedicated Workers with this setting enabled while the remaining Mattermost app servers have it disabled.

+------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RunJobs": true`` with options ``true`` and ``false``.                                 |
+------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: run-scheduler
  :displayname: Run scheduler (Experimental)
  :systemconsole: N/A
  :configjson: RunScheduler
  :environment: N/A
  :description: Set whether or not this Mattermost server will schedule tasks that will be completed by a Worker. Default is **true**.

Run scheduler
~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Set whether or not this Mattermost server will schedule tasks that will be completed by a Worker. When running Mattermost on a single machine, this setting should always be enabled.

When running Mattermost in :doc:`High Availablity mode </administration-guide/scale/high-availability-cluster-based-deployment>`, this setting should always be enabled. In a High Availability cluster-based deployment, exactly one of the servers will be designated as the Scheduler at a time to ensure that duplicate tasks aren't created. See :doc:`High Availability documentation </administration-guide/scale/high-availability-cluster-based-deployment>` for more details.

.. warning::

   We strongly recommend that you not change this setting from the default setting of ``true`` as this prevents the ``ClusterLeader`` from being able to run the scheduler. As a result, recurring jobs such as LDAP sync, Compliance Export, and data retention will no longer be scheduled. In previous Mattermost Server versions, and this documentation, the instructions stated to run the Job Server with ``RunScheduler: false``. The cluster design has evolved and this is no longer the case.

.. tip::

   From Mattermost v11.4, debug-level log messages are available to help verify that specific Recurring Tasks (Scheduled Posts, Post Reminders, and DND Status Reset) are executing correctly in a cluster. Non-leader nodes log messages when they skip execution of these Recurring Tasks, confirming that leader election is functioning as expected. These debug messages do not apply to other job types such as Elasticsearch indexing, SAML sync, or LDAP sync. See :ref:`Cluster job execution debug messages <administration-guide/manage/logging:cluster job execution debug messages>` for details.

+-----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RunScheduler": true`` with options ``true`` and ``false``.                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: clean-up-old-database-jobs
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

.. config:setting:: clean-up-outdated-database-entries
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

