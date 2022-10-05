Site configuration settings
===========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration**, or by editing the ``config.json`` file as described in the following tables:

- `Customization <#customization>`__
- `Localization <#localization>`__
- `Users and Teams <#users-and-teams>`__
- `Notifications <#notifications>`__
- `Announcement Banner <#announcement-banner>`__
- `Emoji <#emoji>`__
- `Posts <#posts>`__
- `File Sharing and Downloads <#file-sharing-and-downloads>`__
- `Public Links <#public-links>`__
- `Notices <#notices>`__

----

Customization
-------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Customization**.

Site name
~~~~~~~~~

Name of service shown in login screens and UI. Maximum 30 characters.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SiteName": "Mattermost"`` with string input. |
+-------------------------------------------------------------------------------------------+

Site description
~~~~~~~~~~~~~~~~

Description of service shown in login screens and UI. When not specified, "All team communication in one place, searchable and accessible anywhere" is displayed.

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CustomDescriptionText": ""`` with string input. |
+----------------------------------------------------------------------------------------------+

Enable custom branding
~~~~~~~~~~~~~~~~~~~~~~

*This feature was moved to Team Edition in Mattermost v5.0, released June 16th, 2018. Prior to v5.0, this feature is available in legacy Enterprise Edition E10 and E20.*

**True**: Enables custom branding to show a JPG image some custom text on the server login page.

**False**: Custom branding is disabled.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCustomBrand": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Custom brand image
~~~~~~~~~~~~~~~~~~~

Custom JPG image is displayed on left side of server login page. Recommended maximum image size is less than 2 MB because image will be loaded for every user who logs in.

+----------------------------------------------------------------------------------------------------+
| This features has no ``config.json`` setting and must be set in the System Console user interface. |
+----------------------------------------------------------------------------------------------------+

Custom brand text
~~~~~~~~~~~~~~~~~

Custom text will be shown below custom brand image on left side of server login page. Maximum 500 characters allowed. You can format this text using the same `Markdown formatting codes <https://docs.mattermost.com/help/messaging/formatting-text.html>`__ as using in Mattermost messages.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CustomBrandText": ""`` with string input. |
+----------------------------------------------------------------------------------------+

Enable Ask Community link
~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: **Ask the community** link is visible in the Mattermost channel header, under the **Help** menu. When selected, users are redirected to https://mattermost.com/pl/default-ask-mattermost-community/, where they can join the Mattermost Community to ask questions and help others troubleshoot issues. This option is not available on the mobile apps.

**False**: The link is not visible to users.

+--------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"enable_ask_community_link": ""`` with options ``true`` and ``false``. Defaults to true. |
+--------------------------------------------------------------------------------------------------------------------------------------+

Help link
~~~~~~~~~

Configurable link to a Help page your organization may provide to end users. By default, links to Mattermost help documentation are hosted on `docs.mattermost.com <https://docs.mattermost.com/>`__.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"HelpLink": "https://docs.mattermost.com/"`` with string input.               |
+---------------------------------------------------------------------------------------------------------------------------+

Terms of Use link
~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

Configurable link to Terms of Use your organization may provide to end users on the footer of Mattermost sign-up and login pages. By default, links to a `Terms of Use <https://mattermost.com/terms-of-use/>`__ page hosted on ``mattermost.com``. If changing the link to a different Terms of Use, make sure to include the "Mattermost Acceptable Use Policy" notice to end users that must also be shown to users from the "Terms of Use" link.

From Mattermost v5.17, this setting doesn't change the terms of use link displayed in the **About Mattermost** dialog, which refers to the Mattermost Terms of Use.

+--------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TermsOfServiceLink": "https://mattermost.com/terms-of-use/"`` with string input.        |
+--------------------------------------------------------------------------------------------------------------------------------------+

Privacy Policy link
~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

Configurable link to Privacy Policy your organization may provide to end users on the footer of the sign-up and login pages. By default, links to a Privacy Policy page hosted on mattermost.com.

In version 5.17 and later, this setting does not change the privacy policy link in **Main Menu > About Mattermost**, which refers to the Mattermost Privacy Policy.

+----------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PrivacyPolicyLink": "https://mattermost.com/privacy-policy/"`` with string input.               |
+----------------------------------------------------------------------------------------------------------------------------------------------+

About link
~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

Configurable link to an About page describing your organization may provide to end users. By default, links to an About page hosted on mattermost.com.

+-----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AboutLink": "https://mattermost.com/platform-overview/"`` with string input.   |
+-----------------------------------------------------------------------------------------------------------------------------+

Report a Problem link
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

Set the link for the support website.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ReportAProblemLink": "https://handbook.mattermost.com/contributors/contributors/ways-to-contribute#report-a-bug"`` with string input.    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Mattermost apps download page link
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

Configurable link to a download page for Mattermost Apps. When a link is present, an option to **Download Apps** will be added in the Main Menu so users can find the download page. Leave this field blank to hide the option from the Main Menu. Defaults to a page on mattermost.com where users can download the iOS, Android, and Desktop clients. If you're using an Enterprise App Store for your mobile apps, change this link to point to a customized download page where users can find the correct apps.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AppDownloadLink": "https://mattermost.com/apps/"`` with string input.     |
+------------------------------------------------------------------------------------------------------------------------+

Android app download link
~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

Configurable link to download the Android app. When a link is present, users who access the site on a mobile web browser will be prompted with a page giving them the option to download the app. Leave this field blank to prevent the page from appearing. If you are using an Enterprise App Store for your mobile apps, change this link to point to the correct app.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AndroidAppDownloadLink": "https://play.google.com/store/apps/details?id=com.mattermost.rn"`` with string input. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

iOS app download link
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

Configurable link to download the iOS app. When a link is present, users who access the site on a mobile web browser will be prompted with a page giving them the option to download the app. Leave this field blank to prevent the page from appearing. If you are using an Enterprise App Store for your mobile apps, change this link to point to the correct app.

+------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IosAppDownloadLink": "https://apps.apple.com/us/app/mattermost/id1257222717"`` with string input. |
+------------------------------------------------------------------------------------------------------------------------------------------------+

----

Localization
-------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Localization**.

Default server language
~~~~~~~~~~~~~~~~~~~~~~~

Default language for system messages and logs.

Changes to this setting require a server restart before taking effect.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DefaultServerLocale": "en"`` with options ``"bg"``, ``"de"``, ``"en"``, ``en-AU``, ``"es"``, ``"fa"``, ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``, ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``, ``"zh_CN"``, and ``"zh_TW"``. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Default client language
~~~~~~~~~~~~~~~~~~~~~~~

Default language for newly-created users and pages where the user hasn't logged in.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DefaultClientLocale": "en"`` with options ``"bg"``, ``"de"``, ``"en"``, ``en-AU``, ``"es"``, ``"fa"``, ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``, ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``, ``"zh_CN"``, and ``"zh_TW"``. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Available languages
~~~~~~~~~~~~~~~~~~~

Sets which languages are available for users in **Settings > Display > Language**. Leave the field blank to add new languages automatically by default, or add new languages using the dropdown menu manually as they become available. If you're manually adding new languages, the **Default Client Language** must be added before saving the setting.

.. note::
  Servers which upgraded to v3.1 need to manually set this field blank to have new languages added by default.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AvailableLocales": ""`` with options ``""``, ``"bg"``, ``"de"``, ``"en"``, ``en-AU``, ``"es"``, ``"fa"``, ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``, ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``, ``"zh_CN"``, and ``"zh_TW"``.  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

Users and teams
---------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Users and Teams**.

Max users per team
~~~~~~~~~~~~~~~~~~~

Maximum number of users per team, excluding inactive users.

The **Max Users Per Team** refers to the size of the "team site" which is workspace a "team of people" inhabits. A team of people is considered a small organization where people work closely together towards a specific shared goal and share the same etiquette. In the physical world, a team of people could typically be seated around a single table to have a meal and discuss their project.

The default maximum of 50 people, is at the extreme high end of a single team of people. At this point organizations are more often "multiple teams of people" and investments in explicitly defining etiquette, such as `channel organization <https://docs.mattermost.com/messaging/organizing-mattermost.html>`__ in Enterprise Edition, are often used to scale the high levels of productivity found in a team of people using Mattermost to multiple teams of people.

In terms of technical performance, `with appropriate hardware, Mattermost can easily scale to hundreds and even thousands of users <https://docs.mattermost.com/install/software-hardware-requirements.html>`__, and provided the administrator believes the appropriate etiquette is in place, they should feel free to increase the default value.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxUsersPerTeam": 50`` with numerical input. |
+-------------------------------------------------------------------------------------------+

Max channels per team
~~~~~~~~~~~~~~~~~~~~~~

Maximum number of channels per team, including both active and deleted channels.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxChannelsPerTeam": 2000`` with numerical input.    |
+---------------------------------------------------------------------------------------------------+

Enable users to open direct message channels with
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Any user on the Mattermost server**: The Direct Messages **More** menu has the option to open a Direct Message channel with any user on the server.

**Any member of the team**: The Direct Messages **More** menu only has the option to open a Direct Message channel with users on the current team, and pressing :kbd:`Ctrl` :kbd:`K` on Windows or Linux, or :kbd:`⌘` :kbd:`K` on Mac only lists users on the current team. If a user belongs to multiple teams, direct messages will still be received regardless of what team they are currently on.

This setting only affects the UI, not permissions on the server. For instance, a direct message channel can be created with anyone on the server regardless of this setting.

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictDirectMessage": "any"`` with options ``"any"`` and ``"team"`` for the above settings, respectively. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

Teammate name display
~~~~~~~~~~~~~~~~~~~~~

Specifies how names are displayed in the user interface by default. Please note that users can override this setting in **Settings > Display > Teammate Name Display**.

**Show username**: Displays the user's username.

**Show nickname if one exists**: Displays the user's nickname. If the user does not have a nickname, their full name is displayed. If the user does not have a full name, their username is displayed.

**Show first and last name**: Displays the user's full name. If the user does not have a full name, their username is displayed. Recommended when using SAML or LDAP if first name and last name attributes are configured.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TeammateNameDisplay": "username"`` with options ``"username"``, ``"nickname_full_name"``, and ``"full_name"`` for the above settings, respectively. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Lock teammate name display for all users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

**True**: Disables users' ability to change settings under **Settings > Display > Teammate Name Display**.

**False**: Users can change how their teammate name displays.

Allow users to view archived channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Allows users to view, share, and search for content of channels that have been archived. Users can only view the content in channels of which they were a member before the channel was archived.

**False**: Users are unable to view, share, or search for content of channels that have been archived.

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalViewArchivedChannels": true`` with options ``true`` and ``false``.         |
+-------------------------------------------------------------------------------------------------------------------------------------+

Show email address
~~~~~~~~~~~~~~~~~~

**True**: Show email address of all users.

**False**: Hide email address of users from other users in the user interface, including Team Admins. This is designed for managing teams where users choose to keep their contact information private. System Admins will still be able to see email addresses in the UI.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ShowEmailAddress": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

Show full name
~~~~~~~~~~~~~~~

**True**: Show full name of all users.

**False**: Hide full name of users from other users including Team Admins. This is designed for managing teams where users choose to keep their contact information private. System Admins will still be able to see full names in the UI.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ShowFullName": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+

Enable custom user statuses
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Users can set descriptive status messages and optional status emojis that are visible to all users.

**False**: Users are unable to set custom user statuses.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCustomUserStatuses": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------------+

----

Notifications
-------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Notifications**.

Show @channel, @all, or @here confirmation dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Users will be prompted to confirm when posting @channel, @all, or @here in channels with over five members.

**False**: No confirmation is required.

+--------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableConfirmNotificationsToChannel": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------------------+

Enable email notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Enables sending of email notifications.

**False**: Disables email notifications for posts. This is useful for developers who may want to skip email setup for faster development. In order to remove the **Preview Mode: Email notifications have not been configured** banner, you should also set **Enable Preview Mode Banner** to ``false``.

If this setting is set to ``false`` and the SMTP server is set up, account related emails (such as password, email, username, user token, MFA, and other authentication related changes) will be sent regardless of this setting. 

Email invitations and account deactivation emails are not affected by this setting.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SendEmailNotifications": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

.. _email-preview-mode-banner-config:

Enable preview mode banner
~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Preview Mode banner is displayed to all users when ``"SendEmailNotifications": false`` so users are aware that email notifications are disabled.

**False**: Preview Mode banner is not displayed to users.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePreviewModeBanner": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Enable email batching
~~~~~~~~~~~~~~~~~~~~~

**True**: Users can select how often to receive email notifications, and multiple notifications within that timeframe will be combined into a single email. Batching will occur at a default interval of 15 minutes, configurable in **Settings > Notifications**.

.. note::
  - Email batching cannot be enabled unless the `SiteURL <https://docs.mattermost.com/configure/configuration-settings.html#site-url>`__ is configured and the `SMTP Email Server <https://docs.mattermost.com/configure/configuration-settings.html#smtp-email-server>`__ is configured. 
  - Email batching in `High Availability mode <https://docs.mattermost.com/configure/configuration-settings.html#enable-high-availability-mode>`__ is planned but not yet supported.

**False**: If email notifications are enabled in **Settings**, emails will be sent individually for every mention or direct message received.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableEmailBatching": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------+

Email notification contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

**Send full message contents**: Sender name and channel are included in email notifications.

**Send generic description with only sender name**: The team name and name of the person who sent the message, with no information about channel name or message contents, is included in email notifications. Typically used for compliance reasons if Mattermost contains confidential information and policy dictates it cannot be stored in email.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EmailNotificationContentsType": "full"`` with options ``"full"`` and ``"generic"`` for the above settings, respectively.             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Support email address
~~~~~~~~~~~~~~~~~~~~~

Set an email address for feedback or support requests. This field is required, and if a value isn't set, email notifications don't include a way for users to request assistance.

To ensure that users can contact you for assistance, set this value to an email address your System Admin receives, such as ``"support@yourcompany.com"``. This address is displayed on email notifications and during the Getting Started tutorial.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SupportEmail": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Notification display name
~~~~~~~~~~~~~~~~~~~~~~~~~~

Name displayed on email account used when sending notification emails from Mattermost system. This field is required, and if a value isn't set, email notifications don't include a way for users to request assistance.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FeedbackName": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Notification from address
~~~~~~~~~~~~~~~~~~~~~~~~~~

Address displayed on email account used when sending notification emails from within Mattermost. This field is required, and if a value isn't set, email notifications don't include a way for users to request assistance.

So you don't miss messages, please make sure to change this value to an email your system administrator receives, such as ``"admin@yourcompany.com"``.

+--------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FeedbackEmail": ""`` with string input. |
+--------------------------------------------------------------------------------------+

Notification reply-to address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Email address used in the Reply-To header when sending notification emails from Mattermost.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ReplyToAddress": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Notification footer mailing address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Organization name and mailing address displayed in the footer of email notifications from Mattermost, such as "© ABC Corporation, 565 Knight Way, Palo Alto, California, 94305, USA". If the field is left empty, the organization name and mailing address will not be displayed.

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FeedbackOrganization": ""`` with string input. |
+---------------------------------------------------------------------------------------------+

Push notification contents
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Generic description with only sender name**: Push notifications include only the name of the person who sent the message but no information about channel name or message text.

**Generic description with sender and channel names**: Push notifications include names of users and channels but no specific details from the message text.

**Full message content sent in the notification payload**: Selecting **Send full message snippet** sends excerpts from messages triggering notifications with specifics and may include confidential information sent in messages. If your Push Notification Service is outside your firewall, it is HIGHLY RECOMMENDED this option only be used with an "https" protocol to encrypt the connection.

**Full message content fetched from the server on receipt** (*Available in Mattermost Enterprise*): The notification payload relayed through the `Apple Push Notification service <https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1>`__ or `Firebase Cloud Messaging <https://firebase.google.com/docs/cloud-messaging>`__ service contains no message content. Instead it contains a unique message ID used to fetch message content from the server when a push notification is received by a device via a `notification service app extension <https://developer.apple.com/documentation/usernotifications/modifying_content_in_newly_delivered_notifications>`__ on iOS or `an expandable notification pattern <https://developer.android.com/training/notify-user/expanded>`__ on Android. If the server cannot be reached, a generic push notification message is displayed without message content or sender name. 

For customers who choose to wrap the Mattermost mobile application in a secure container, such as BlackBerry Dynamics, MobileIron, AirWatch or other solutions, the container needs to execute the fetching of message contents from the unique message ID when push notification are received. If the container is unable to execute the fetch, the push notification contents cannot be received by the customer's mobile application without passing the message contents through either the `Apple Push Notification service <https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1>`__ or `Firebase Cloud Messaging <https://firebase.google.com/docs/cloud-messaging>`__ service. 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PushNotificationContents": "full"`` with options ``"generic_no_channel"``, ``"generic"``, ``"full"``, and ``"id_loaded"`` for the above settings, respectively.    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

Announcement banner
-------------------

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Announcement Banner**.

Enable announcement banner
~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable an announcement banner across all teams. The banner is displayed at the top of the screen and is the entire width of the screen. By default, users can dismiss the banner until you either change the text of the banner or until you re-enable the banner after it has been disabled. You can prevent users from dismissing the banner, and you can control the text color and the background color.

**True**: Enable the announcement banner. The banner is displayed only if ``BannerText`` has a value.

**False**: Disable the announcement banner.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableBanner": false`` with options ``true`` and ``false``.  |
+-----------------------------------------------------------------------------------------------------------+

Banner text
~~~~~~~~~~~

The text of the announcement banner.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BannerText": ""`` with string input.  |
+------------------------------------------------------------------------------------+

Banner color
~~~~~~~~~~~~~

The background color of the announcement banner.

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BannerColor": "#f2a93b"`` with string input.   |
+---------------------------------------------------------------------------------------------+

Banner text color
~~~~~~~~~~~~~~~~~

The color of the text in the announcement banner.

+-------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BannerTextColor": "#333333"`` with string input.   |
+-------------------------------------------------------------------------------------------------+

Allow banner dismissal
~~~~~~~~~~~~~~~~~~~~~~

**True**: Users can dismiss the banner until the next time they log in or the banner is updated.

**False**: The banner is permanently visible until it is turned off by the System Admin.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowBannerDismissal": true`` with options ``true`` and ``false``.   |
+-------------------------------------------------------------------------------------------------------------------+

----

Emoji
------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Emoji**.

Enable emoji picker
~~~~~~~~~~~~~~~~~~~

**True**: Enables an emoji picker that allows users to select emojis to add as reactions or use in messages. Enabling the emoji picker with a large number of custom emojis may slow down performance.

**False**: The emoji picker is disabled.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableEmojiPicker": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

Enable custom emoji
~~~~~~~~~~~~~~~~~~~

**True**: Enables a **Custom Emoji** option in the emoji picker, where users can go to add custom emojis.

**False**: Custom emojis are disabled.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCustomEmoji": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

----

Posts
-----

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Posts**.

Automatically follow threads
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

This setting must be enabled to support `Collapsed Reply Threads <https://docs.mattermost.com/channels/organize-conversations.html>`__. See the `administrator’s guide to enabling Collapsed Reply Threads <https://support.mattermost.com/hc/en-us/articles/6880701948564>`__ knowledge base article for details.

**True**: Threads a user starts, participates in, or is mentioned in are automatically followed. A new ``Threads`` table is added in the database that tracks threads and thread participants, and a ``ThreadMembership`` table tracks followed threads for each user and the read or unread state of each followed thread. Mattermost Cloud workspaces have this setting enabled.

**False**: All backend operations for Collapsed Reply Threads are disabled and server performance will not be impacted by the feature. Collapsed Reply Threads (``CollapsedThreads``) cannot be enabled if ``ThreadAutoFollow`` is disabled.    

.. note::

   Enabling this configuration setting doesn’t retroactively follow threads for actions taken prior to the setting being enabled. For example, threads a user participated in prior to enabling this setting won't be automatically followed. However, if this setting is enabled, and a user adds a new comment on an old thread, they will automatically start following the thread.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ThreadAutoFollow": true`` with options ``true`` and ``false``.  |
+--------------------------------------------------------------------------------------------------------------+

Collapsed reply threads
~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

Collapsed Reply Threads offers an enhanced experience for users communicating in threads and replying to messages. Collapsed Reply Threads is generally available in Mattermost Cloud and from self-hosted Mattermost v7.0, and is enabled by default for all new Mattermost deployments. See our `Organizing Conversations using Collapsed Reply Threads <https://docs.mattermost.com/channels/organize-conversations.html>`__ documentation to learn more about this feature.

.. important::
    
    Customers upgrading to v7.0 must review the `administrator’s guide to enabling Collapsed Reply Threads <https://support.mattermost.com/hc/en-us/articles/6880701948564>`__ knowledge base article to learn about the system requirements, steps to enable, and self-host prerequisites to consider prior to enabling this functionality. 

System Admins can set the default availability of Collapsed Reply Threads for their workspace by going to **System Console > Site Configuration > Posts**, then setting **Collapsed Reply Threads** to one of the following options:

**Always On**: Enables Collapsed Reply Threads functionality on the server and for all users. Users can't disable this functionality. This is the recommended configuration for optimal user experience and to ensure consistency in how users read and respond to threaded conversations. Mattermost Cloud workspaces have Collapsed Reply Threads set to ``always_on`` by default.

**Default On**: Enables Collapsed Reply Threads functionality on the server and for all users. Users can choose to `disable Collapsed Reply Threads <https://docs.mattermost.com/channels/channels-settings.html#collapsed-reply-threads>`__ for their Mattermost account in **Settings > Display > Collapsed Reply Threads**. 

**Default Off**: Enables Collapsed Reply Threads functionality on the server but not for users. Users can choose to `enable Collapsed Reply Threads <https://docs.mattermost.com/channels/channels-settings.html#collapsed-reply-threads>`__ for their Mattermost account in **Settings > Display > Collapsed Reply Threads**.

**Disabled**: Disables Collapsed Reply Threads front-end functionality.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CollapsedThreads": always_on`` with options ``disabled``, ``default_off``, ``default_on``, and ``always_on`` |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable link previews
~~~~~~~~~~~~~~~~~~~~~

Link previews are previews of linked website content, image links, and YouTube videos that are displayed below posts when available.

Link previews are requested by the server, meaning the Mattermost server must be connected to the internet for previews to be displayed. This connection can be established through a `firewall or outbound proxy <https://docs.mattermost.com/install/outbound-proxy.html>`__ in environments where direct internet connectivity is not given or security policies make this necessary.

**True**: Website link previews, image link previews, and YouTube previews are enabled on the server. Users can enable or disable website previews for themselves from **Settings > Display > Website Link Previews**.

**False**: Website link previews, image link previews, and YouTube previews are disabled. The server does not request metadata for any links sent in messages.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableLinkPreviews": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Disable link previews for specific domains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Link previews are disabled for this list of comma-separated domains (e.g. “github.com, mattermost.com”). 

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictLinkPreviews": ""`` with string input. |
+---------------------------------------------------------------------------------------------+

Enable message link previews
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Links to messages generate a preview for any users with access to the original message. 

**False**: Links to messages don't include a preview.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePermalinkPreviews": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Enable SVGs
~~~~~~~~~~~

**True**: Enables users to see previews of SVG file attachments and SVG image links.

**False**: Previews of SVG file attachments and SVG image links are not displayed.

+--------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSVGs": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------+

Enable LaTeX code block rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Enables rendering of LaTeX code in a ``latex`` code block.

**False**: Disables rendering of LaTeX code to prevent the app from crashing when sharing code that might outgrow assigned memory. When disabled, LaTeX code will be highlighted.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableLatex": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+

Enable inline LaTeX rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Enables inline rendering of LaTeX code.

**False**: Disables inline rendering of LaTeX code to prevent the app from crashing when sharing code that might outgrow assigned memory. When disabled, LaTeX code will be highlighted. When disabled, Latex code can only be `rendered in a code block using syntax highlighting <https://docs.mattermost.com/configure/configuration-settings.html#enable-latex-code-block-rendering>`__. 

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableInlineLatex": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Custom URL schemes
~~~~~~~~~~~~~~~~~~~

A list of URL schemes that are used for autolinking in message text. ``http``, ``https``, ``ftp``, ``tel`` and ``mailto`` always create links.

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CustomUrlSchemes": []`` with string array input consisting of URL schemes, such as ``["git", "smtp"]``. |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

Google API key
~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

Mattermost offers the ability to embed YouTube videos from URLs shared by end users. 

Set this key and add YouTube Data API v3 as a service to your key to enable the display of titles for embedded YouTube video previews. Without the key, YouTube previews will still be created based on hyperlinks appearing in messages or comments but they will not show the video title. If Google detects the number of views is exceedingly high, they may throttle embed access. 

Should this occur, you can remove the throttle by registering for a Google Developer Key and entering it in this field following these instructions: https://www.youtube.com/watch?v=Im69kzhpR3I. Your Google Developer Key is used in client-side Javascript.

Using a Google API Key allows Mattermost to detect when a video is no longer available and display the post with a *Video not found* label.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GoogleDeveloperKey": ""`` with string input. |
+-------------------------------------------------------------------------------------------+

----

File sharing and downloads
---------------------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > File Sharing and Downloads**.

Allow file sharing
~~~~~~~~~~~~~~~~~~

When ``false``, disables file sharing on the server. All file and image uploads on messages are forbidden across clients and devices, including mobile.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableFileAttachments": true`` with options ``true`` and ``false``.    |
+---------------------------------------------------------------------------------------------------------------------+

Allow file uploads on mobile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Enables file uploads on messages using Mattermost clients.

**False**: Disables file uploads on mobile apps. All file and image uploads on messages are forbidden across clients and devices, including mobile.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableMobileUpload": true`` with options ``true`` and ``false``.       |
+---------------------------------------------------------------------------------------------------------------------+

Allow file downloads on mobile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Enables file downloads on Mattermost mobile apps.

**False**: Disables file downloads on mobile apps. Users can still download files from a mobile web browser.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableMobileDownload": true`` with options ``true`` and ``false``.     |
+---------------------------------------------------------------------------------------------------------------------+

----

Public Links
------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Public Links**.

Enable public file links
~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Allow users to generate public links to files and images for sharing outside the Mattermost system with a public URL.

**False**: The **Get Public Link** option is hidden from the image preview user interface.

.. note:: 

   When set to ``False``, anyone who tries to visit a previously generated public link will receive an error message saying public links have been disabled. When set back to ``True``, old public links will work again unless the **Public Link Salt** has been regenerated.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePublicLink": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

Public link salt
~~~~~~~~~~~~~~~~

32-character salt added to the URL of public links when public links are enabled. Select **Regenerate** in the System Console to create a new salt, which will invalidate all existing public links.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PublicLinkSalt": ""`` with string input. |
+---------------------------------------------------------------------------------------+

----

Notices
--------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Notices**.

Enable admin notices
~~~~~~~~~~~~~~~~~~~~~

**True**: System Admins will receive notices about available server upgrades and relevant system administration features. `Learn more <https://docs.mattermost.com/manage/in-product-notices.html>`__.

**False**: System Admins will not receive notices except those that apply to all end users (See ``UserNoticesEnabled``). 

+----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AdminNoticesEnabled": true`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------+

Enable end user notices
~~~~~~~~~~~~~~~~~~~~~~~

**True**: All users will receive notices about available client upgrades and relevant end user features to improve user experience. `Learn more <https://docs.mattermost.com/manage/in-product-notices.html>`__.

**False**: Users will not receive notices about available client upgrades and relevant end user features. 

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserNoticesEnabled": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+