Configuration settings
======================

Mattermost configuration settings are maintained in the ``config.json`` configuration file, located in the ``mattermost/config`` directory. System Admins can manage Mattermost configuration using the System Console, or by modifying the ``config.json`` file directly using a text editor. 

.. note::

   Mattermost must have write permissions to ``config.json``, otherwise configuration changes made within the System Console will have no effect.

Configuration in database
--------------------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

From Mattermost v5.10, self-hosted system configuration can be stored in the database. This changes the Mattermost binary from reading the default ``config.json`` file to reading the configuration settings stored within a configuration table in the database. See the `Mattermost database configuration <https://docs.mattermost.com/configure/configuation-in-mattermost-database.html>`__ documentation for migration details.

Environment variables
---------------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

From Mattermost v3.8, you can use `environment variables <https://docs.mattermost.com/configure/environment-variables.html>`__ to manage Mattermost configuration. Environment variables override settings in ``config.json``. If a change to a setting in ``config.json`` requires a restart to take effect, then changes to the corresponding environment variable also require a server restart. 

Configuration reload
--------------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

From Mattermost v5.38, the “config watcher”, the mechanism that automatically reloads the ``config.json`` file, has been deprecated in favor of the `mmctl config reload <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-config-reload>`__ command that must be run to apply configuration changes after they’re made. This change will improve configuration performance and robustness.

Deprecated configuration settings
---------------------------------

See the `deprecated configuration settings documentation <https://docs.mattermost.com/configure/deprecated-configuration-settings.html>`__ for details on all deprecated Mattermost configuration settings that are no longer supported.

Site Configuration
-------------------

Settings for customizing your Mattermost deployment.

Customization
~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Customization**.

Site Name
^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Name of service shown in login screens and UI. Maximum 30 characters.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SiteName": "Mattermost"`` with string input. |
+-------------------------------------------------------------------------------------------+

Site Description
^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Description of service shown in login screens and UI. When not specified, "All team communication in one place, searchable and accessible anywhere" is displayed.

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CustomDescriptionText": ""`` with string input. |
+----------------------------------------------------------------------------------------------+

Enable Custom Branding
^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

*This feature was moved to Team Edition in Mattermost v5.0, released June 16th, 2018. Prior to v5.0, this feature is available in legacy Enterprise Edition E10 and E20.*

**True**: Enables custom branding to show a JPG image some custom text on the server login page.

**False**: Custom branding is disabled.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCustomBrand": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Custom Brand Image
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Custom JPG image is displayed on left side of server login page. Recommended maximum image size is less than 2 MB because image will be loaded for every user who logs in.

+----------------------------------------------------------------------------------------------------+
| This features has no ``config.json`` setting and must be set in the System Console user interface. |
+----------------------------------------------------------------------------------------------------+

Custom Brand Text
^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Custom text will be shown below custom brand image on left side of server login page. Maximum 500 characters allowed. You can format this text using the same `Markdown formatting codes <https://docs.mattermost.com/help/messaging/formatting-text.html>`__ as using in Mattermost messages.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CustomBrandText": ""`` with string input. |
+----------------------------------------------------------------------------------------+

Enable Ask Community Link
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: **Ask the community** link is visible in the Mattermost channel header, under the **Help** menu. When selected, users are redirected to https://mattermost.com/pl/default-ask-mattermost-community/, where they can join the Mattermost Community to ask questions and help others troubleshoot issues. This option is not available on the mobile apps.

**False**: The link is not visible to users.

+--------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"enable_ask_community_link": ""`` with options ``true`` and ``false``. Defaults to true. |
+--------------------------------------------------------------------------------------------------------------------------------------+

Help link
^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Configurable link to a Help page your organization may provide to end users. By default, links to Mattermost help documentation are hosted on `docs.mattermost.com <https://docs.mattermost.com/>`__.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"HelpLink": "https://docs.mattermost.com/"`` with string input.               |
+---------------------------------------------------------------------------------------------------------------------------+

Terms of Use link
^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Configurable link to Terms of Use your organization may provide to end users on the footer of Mattermost sign-up and login pages. By default, links to a `Terms of Use <https://mattermost.com/terms-of-use/>`__ page hosted on ``mattermost.com``. If changing the link to a different Terms of Use, make sure to include the "Mattermost Acceptable Use Policy" notice to end users that must also be shown to users from the "Terms of Use" link.

From Mattermost v5.17, this setting doesn't change the terms of use link displayed in the **About Mattermost** dialog, which refers to the Mattermost Terms of Use.

+--------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TermsOfServiceLink": "https://mattermost.com/terms-of-use/"`` with string input.        |
+--------------------------------------------------------------------------------------------------------------------------------------+

Privacy Policy link
^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Configurable link to Privacy Policy your organization may provide to end users on the footer of the sign-up and login pages. By default, links to a Privacy Policy page hosted on mattermost.com.

In version 5.17 and later, this setting does not change the privacy policy link in **Main Menu > About Mattermost**, which refers to the Mattermost Privacy Policy.

+----------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PrivacyPolicyLink": "https://mattermost.com/privacy-policy/"`` with string input.               |
+----------------------------------------------------------------------------------------------------------------------------------------------+

About Link
^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Configurable link to an About page describing your organization may provide to end users. By default, links to an About page hosted on mattermost.com.

+-----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AboutLink": "https://mattermost.com/platform-overview/"`` with string input.   |
+-----------------------------------------------------------------------------------------------------------------------------+

Report a Problem link
^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Set the link for the support website.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ReportAProblemLink": "https://handbook.mattermost.com/contributors/contributors/ways-to-contribute#report-a-bug"`` with string input.    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Mattermost Apps Download Page Link
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Configurable link to a download page for Mattermost Apps. When a link is present, an option to **Download Apps** will be added in the Main Menu so users can find the download page. Leave this field blank to hide the option from the Main Menu. Defaults to a page on mattermost.com where users can download the iOS, Android, and Desktop clients. If you're using an Enterprise App Store for your mobile apps, change this link to point to a customized download page where users can find the correct apps.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AppDownloadLink": "https://mattermost.com/apps/"`` with string input.     |
+------------------------------------------------------------------------------------------------------------------------+

Android App Download Link
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Configurable link to download the Android app. When a link is present, users who access the site on a mobile web browser will be prompted with a page giving them the option to download the app. Leave this field blank to prevent the page from appearing. If you are using an Enterprise App Store for your mobile apps, change this link to point to the correct app.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AndroidAppDownloadLink": "https://play.google.com/store/apps/details?id=com.mattermost.rn"`` with string input. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

iOS App Download Link
^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Configurable link to download the iOS app. When a link is present, users who access the site on a mobile web browser will be prompted with a page giving them the option to download the app. Leave this field blank to prevent the page from appearing. If you are using an Enterprise App Store for your mobile apps, change this link to point to the correct app.

+------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IosAppDownloadLink": "https://apps.apple.com/us/app/mattermost/id1257222717"`` with string input. |
+------------------------------------------------------------------------------------------------------------------------------------------------+

Localization
~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Localization**.

Default Server Language
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Default language for system messages and logs.

Changes to this setting require a server restart before taking effect.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DefaultServerLocale": "en"`` with options ``"bg"``, ``"de"``, ``"en"``, ``en-AU``, ``"es"``, ``"fa"``, ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``, ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``, ``"zh_CN"``, and ``"zh_TW"``. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Default Client Language
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Default language for newly-created users and pages where the user hasn't logged in.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DefaultClientLocale": "en"`` with options ``"bg"``, ``"de"``, ``"en"``, ``en-AU``, ``"es"``, ``"fa"``, ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``, ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``, ``"zh_CN"``, and ``"zh_TW"``. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Available Languages
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Sets which languages are available for users in **Settings > Display > Language**. Leave the field blank to add new languages automatically by default, or add new languages using the dropdown menu manually as they become available. If you're manually adding new languages, the **Default Client Language** must be added before saving the setting.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AvailableLocales": ""`` with options ``""``, ``"bg"``, ``"de"``, ``"en"``, ``en-AU``, ``"es"``, ``"fa"``, ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``, ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``, ``"zh_CN"``, and ``"zh_TW"``.  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Users and Teams
~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Users and Teams**.

Max Users Per Team
^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Maximum number of users per team, excluding inactive users.

The **Max Users Per Team** refers to the size of the "team site" which is workspace a "team of people" inhabits. A team of people is considered a small organization where people work closely together towards a specific shared goal and share the same etiquette. In the physical world, a team of people could typically be seated around a single table to have a meal and discuss their project.

The default maximum of 50 people, is at the extreme high end of a single team of people. At this point organizations are more often "multiple teams of people" and investments in explicitly defining etiquette, such as `channel organization <https://docs.mattermost.com/messaging/organizing-mattermost.html>`__ in Enterprise Edition, are often used to scale the high levels of productivity found in a team of people using Mattermost to multiple teams of people.

In terms of technical performance, `with appropriate hardware, Mattermost can easily scale to hundreds and even thousands of users <https://docs.mattermost.com/install/software-hardware-requirements.html>`__, and provided the administrator believes the appropriate etiquette is in place, they should feel free to increase the default value.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxUsersPerTeam": 50`` with numerical input. |
+-------------------------------------------------------------------------------------------+

Max Channels Per Team
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Maximum number of channels per team, including both active and deleted channels.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxChannelsPerTeam": 2000`` with numerical input.    |
+---------------------------------------------------------------------------------------------------+

Enable users to open Direct Message channels with
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**Any user on the Mattermost server**: The Direct Messages **More** menu has the option to open a Direct Message channel with any user on the server.

**Any member of the team**: The Direct Messages **More** menu only has the option to open a Direct Message channel with users on the current team, and pressing :kbd:`Ctrl` :kbd:`K` on Windows or Linux, or :kbd:`⌘` :kbd:`K` on Mac only lists users on the current team. If a user belongs to multiple teams, direct messages will still be received regardless of what team they are currently on.

This setting only affects the UI, not permissions on the server. For instance, a direct message channel can be created with anyone on the server regardless of this setting.

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictDirectMessage": "any"`` with options ``"any"`` and ``"team"`` for the above settings, respectively. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

Teammate Name Display
^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Specifies how names are displayed in the user interface by default. Please note that users can override this setting in **Settings > Display > Teammate Name Display**.

**Show username**: Displays the user's username.

**Show nickname if one exists**: Displays the user's nickname. If the user does not have a nickname, their full name is displayed. If the user does not have a full name, their username is displayed.

**Show first and last name**: Displays the user's full name. If the user does not have a full name, their username is displayed. Recommended when using SAML or LDAP if first name and last name attributes are configured.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TeammateNameDisplay": "username"`` with options ``"username"``, ``"nickname_full_name"``, and ``"full_name"`` for the above settings, respectively. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Lock Teammate Name Display for all users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Disables users' ability to change settings under **Settings > Display > Teammate Name Display**.

**False**: Users can change how their teammate name displays.

Allow Users to View Archived Channels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Allows users to view, share, and search for content of channels that have been archived. Users can only view the content in channels of which they were a member before the channel was archived.

**False**: Users are unable to view, share, or search for content of channels that have been archived.

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalViewArchivedChannels": true`` with options ``true`` and ``false``.         |
+-------------------------------------------------------------------------------------------------------------------------------------+

Show Email Address
^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Show email address of all users.

**False**: Hide email address of users from other users in the user interface, including Team Admins. This is designed for managing teams where users choose to keep their contact information private. System Admins will still be able to see email addresses in the UI.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ShowEmailAddress": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

Show Full Name
^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Show full name of all users.

**False**: Hide full name of users from other users including Team Admins. This is designed for managing teams where users choose to keep their contact information private. System Admins will still be able to see full names in the UI.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ShowFullName": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+

Enable Custom User Statuses
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Users can set descriptive status messages and optional status emojis that are visible to all users.

**False**: Users are unable to set custom user statuses.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCustomUserStatuses": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------------+

Notifications
~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Notifications**.

Show @channel, @all, or @here confirmation dialog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Users will be prompted to confirm when posting @channel, @all, or @here in channels with over five members.

**False**: No confirmation is required.

+--------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableConfirmNotificationsToChannel": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------------------+

Enable Email Notifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables sending of email notifications.

**False**: Disables email notifications for posts. This is useful for developers who may want to skip email setup for faster development. In order to remove the **Preview Mode: Email notifications have not been configured** banner, you should also set **Enable Preview Mode Banner** to ``false``.

If this setting is set to ``false`` and the SMTP server is set up, account related emails (such as password, email, username, user token, MFA, and other authentication related changes) will be sent regardless of this setting. 

Email invitations and account deactivation emails are not affected by this setting.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SendEmailNotifications": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

.. _email-preview-mode-banner-config:

Enable Preview Mode Banner
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Preview Mode banner is displayed to all users when ``"SendEmailNotifications": false`` so users are aware that email notifications are disabled.

**False**: Preview Mode banner is not displayed to users.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePreviewModeBanner": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Enable Email Batching
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Users can select how often to receive email notifications, and multiple notifications within that timeframe will be combined into a single email. Batching will occur at a default interval of 15 minutes, configurable in **Settings > Notifications**.

.. note::
  - Email batching cannot be enabled unless the `SiteURL <https://docs.mattermost.com/configure/configuration-settings.html#site-url>`__ is configured and the `SMTP Email Server <https://docs.mattermost.com/configure/configuration-settings.html#smtp-email-server>`__ is configured. 
  - Email batching in `High Availability mode <https://docs.mattermost.com/configure/configuration-settings.html#enable-high-availability-mode>`__ is planned but not yet supported.

**False**: If email notifications are enabled in **Settings**, emails will be sent individually for every mention or direct message received.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableEmailBatching": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------+

Email Notification Contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**Send full message contents**: Sender name and channel are included in email notifications.

**Send generic description with only sender name**: The team name and name of the person who sent the message, with no information about channel name or message contents, is included in email notifications. Typically used for compliance reasons if Mattermost contains confidential information and policy dictates it cannot be stored in email.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EmailNotificationContentsType": "full"`` with options ``"full"`` and ``"generic"`` for the above settings, respectively.             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Support Email Address
^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Set an email address for feedback or support requests. This field is required, and if a value isn't set, email notifications don't include a way for users to request assistance.

To ensure that users can contact you for assistance, set this value to an email address your System Admin receives, such as ``"support@yourcompany.com"``. This address is displayed on email notifications and during the Getting Started tutorial.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SupportEmail": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Notification Display Name
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Name displayed on email account used when sending notification emails from Mattermost system. This field is required, and if a value isn't set, email notifications don't include a way for users to request assistance.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FeedbackName": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Notification From Address
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Address displayed on email account used when sending notification emails from within Mattermost. This field is required, and if a value isn't set, email notifications don't include a way for users to request assistance.

So you don't miss messages, please make sure to change this value to an email your system administrator receives, such as ``"admin@yourcompany.com"``.

+--------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FeedbackEmail": ""`` with string input. |
+--------------------------------------------------------------------------------------+

Notification Reply-To Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Email address used in the Reply-To header when sending notification emails from Mattermost.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ReplyToAddress": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Notification Footer Mailing Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Organization name and mailing address displayed in the footer of email notifications from Mattermost, such as "© ABC Corporation, 565 Knight Way, Palo Alto, California, 94305, USA". If the field is left empty, the organization name and mailing address will not be displayed.

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FeedbackOrganization": ""`` with string input. |
+---------------------------------------------------------------------------------------------+

Push Notification Contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**Generic description with only sender name**: Push notifications include only the name of the person who sent the message but no information about channel name or message text.

**Generic description with sender and channel names**: Push notifications include names of users and channels but no specific details from the message text.

**Full message content sent in the notification payload**: Selecting **Send full message snippet** sends excerpts from messages triggering notifications with specifics and may include confidential information sent in messages. If your Push Notification Service is outside your firewall, it is HIGHLY RECOMMENDED this option only be used with an "https" protocol to encrypt the connection.

**Full message content fetched from the server on receipt** (*Available in Mattermost Enterprise*): The notification payload relayed through the `Apple Push Notification service <https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1>`__ or `Firebase Cloud Messaging <https://firebase.google.com/docs/cloud-messaging>`__ service contains no message content. Instead it contains a unique message ID used to fetch message content from the server when a push notification is received by a device via a `notification service app extension <https://developer.apple.com/documentation/usernotifications/modifying_content_in_newly_delivered_notifications>`__ on iOS or `an expandable notification pattern <https://developer.android.com/training/notify-user/expanded>`__ on Android. If the server cannot be reached, a generic push notification message is displayed without message content or sender name. 

For customers who choose to wrap the Mattermost mobile application in a secure container, such as BlackBerry Dynamics, MobileIron, AirWatch or other solutions, the container needs to execute the fetching of message contents from the unique message ID when push notification are received. If the container is unable to execute the fetch, the push notification contents cannot be received by the customer's mobile application without passing the message contents through either the `Apple Push Notification service <https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1>`__ or `Firebase Cloud Messaging <https://firebase.google.com/docs/cloud-messaging>`__ service. 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PushNotificationContents": "full"`` with options ``"generic_no_channel"``, ``"generic"``, ``"full"``, and ``"id_loaded"`` for the above settings, respectively.    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Announcement Banner
~~~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Announcement Banner**.

Enable Announcement Banner
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Enable an announcement banner across all teams. The banner is displayed at the top of the screen and is the entire width of the screen. By default, users can dismiss the banner until you either change the text of the banner or until you re-enable the banner after it has been disabled. You can prevent users from dismissing the banner, and you can control the text color and the background color.

**True**: Enable the announcement banner. The banner is displayed only if ``BannerText`` has a value.

**False**: Disable the announcement banner.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableBanner": false`` with options ``true`` and ``false``.  |
+-----------------------------------------------------------------------------------------------------------+

Banner Text
^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

The text of the announcement banner.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BannerText": ""`` with string input.  |
+------------------------------------------------------------------------------------+

Banner Color
^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

The background color of the announcement banner.

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BannerColor": "#f2a93b"`` with string input.   |
+---------------------------------------------------------------------------------------------+

Banner Text Color
^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

The color of the text in the announcement banner.

+-------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BannerTextColor": "#333333"`` with string input.   |
+-------------------------------------------------------------------------------------------------+

Allow Banner Dismissal
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Users can dismiss the banner until the next time they log in or the banner is updated.

**False**: The banner is permanently visible until it is turned off by the System Admin.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowBannerDismissal": true`` with options ``true`` and ``false``.   |
+-------------------------------------------------------------------------------------------------------------------+

Emoji
~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Emoji**.

Enable Emoji Picker
^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables an emoji picker that allows users to select emojis to add as reactions or use in messages. Enabling the emoji picker with a large number of custom emojis may slow down performance.

**False**: The emoji picker is disabled.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableEmojiPicker": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

Enable Custom Emoji
^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables a **Custom Emoji** option in the emoji picker, where users can go to add custom emojis.

**False**: Custom emojis are disabled.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCustomEmoji": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

Posts
~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Posts**.

Automatically Follow Threads
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting must be enabled to support `Collapsed Reply Threads <https://docs.mattermost.com/channels/organize-conversations.html>`__. See the `administrator’s guide to enabling Collapsed Reply Threads <https://support.mattermost.com/hc/en-us/articles/6880701948564>`__ knowledge base article for details.

**True**: Threads a user starts, participates in, or is mentioned in are automatically followed. A new ``Threads`` table is added in the database that tracks threads and thread participants, and a ``ThreadMembership`` table tracks followed threads for each user and the read or unread state of each followed thread. Mattermost Cloud workspaces have this setting enabled.

**False**: All backend operations for Collapsed Reply Threads are disabled and server performance will not be impacted by the feature. Collapsed Reply Threads (``CollapsedThreads``) cannot be enabled if ``ThreadAutoFollow`` is disabled.    

.. note::

   Enabling this configuration setting doesn’t retroactively follow threads for actions taken prior to the setting being enabled. For example, threads a user participated in prior to enabling this setting won't be automatically followed. However, if this setting is enabled, and a user adds a new comment on an old thread, they will automatically start following the thread.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ThreadAutoFollow": true`` with options ``true`` and ``false``.  |
+--------------------------------------------------------------------------------------------------------------+

Collapsed Reply Threads
~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/allplans-selfhosted.rst
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

Enable Link Previews
^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Link previews are previews of linked website content, image links, and YouTube videos that are displayed below posts when available.

Link previews are requested by the server, meaning the Mattermost server must be connected to the internet for previews to be displayed. This connection can be established through a `firewall or outbound proxy <https://docs.mattermost.com/install/outbound-proxy.html>`__ in environments where direct internet connectivity is not given or security policies make this necessary.

**True**: Website link previews, image link previews, and YouTube previews are enabled on the server. Users can enable or disable website previews for themselves from **Settings > Display > Website Link Previews**.

**False**: Website link previews, image link previews, and YouTube previews are disabled. The server does not request metadata for any links sent in messages.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableLinkPreviews": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Disable Link Previews for Specific Domains
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Link previews are disabled for this list of comma-separated domains (e.g. “github.com, mattermost.com”). 

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictLinkPreviews": ""`` with string input. |
+---------------------------------------------------------------------------------------------+

Enable message link previews
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Links to messages generate a preview for any users with access to the original message. 

**False**: Links to messages don't include a preview.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePermalinkPreviews": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Enable SVGs
^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables users to see previews of SVG file attachments and SVG image links.

**False**: Previews of SVG file attachments and SVG image links are not displayed.

+--------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSVGs": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------+

Enable LaTeX Code Block Rendering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables rendering of LaTeX code in a ``latex`` code block.

**False**: Disables rendering of LaTeX code to prevent the app from crashing when sharing code that might outgrow assigned memory. When disabled, LaTeX code will be highlighted.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableLatex": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+

Enable Inline LaTeX Rendering
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables inline rendering of LaTeX code.

**False**: Disables inline rendering of LaTeX code to prevent the app from crashing when sharing code that might outgrow assigned memory. When disabled, LaTeX code will be highlighted. When disabled, Latex code can only be `rendered in a code block using syntax highlighting <https://docs.mattermost.com/configure/configuration-settings.html#enable-latex-code-block-rendering>`__. 

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableInlineLatex": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Custom URL Schemes
^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

A list of URL schemes that are used for autolinking in message text. ``http``, ``https``, ``ftp``, ``tel`` and ``mailto`` always create links.

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CustomUrlSchemes": []`` with string array input consisting of URL schemes, such as ``["git", "smtp"]``. |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

Google API Key
^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Mattermost offers the ability to embed YouTube videos from URLs shared by end users. 

Set this key and add YouTube Data API v3 as a service to your key to enable the display of titles for embedded YouTube video previews. Without the key, YouTube previews will still be created based on hyperlinks appearing in messages or comments but they will not show the video title. If Google detects the number of views is exceedingly high, they may throttle embed access. 

Should this occur, you can remove the throttle by registering for a Google Developer Key and entering it in this field following these instructions: https://www.youtube.com/watch?v=Im69kzhpR3I. Your Google Developer Key is used in client-side Javascript.

Using a Google API Key allows Mattermost to detect when a video is no longer available and display the post with a *Video not found* label.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GoogleDeveloperKey": ""`` with string input. |
+-------------------------------------------------------------------------------------------+

File Sharing and Downloads
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > File Sharing and Downloads**.

Allow File Sharing
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

When ``false``, disables file sharing on the server. All file and image uploads on messages are forbidden across clients and devices, including mobile.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableFileAttachments": true`` with options ``true`` and ``false``.    |
+---------------------------------------------------------------------------------------------------------------------+

Allow File Uploads on Mobile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Enables file uploads on messages using Mattermost clients.

**False**: Disables file uploads on mobile apps. All file and image uploads on messages are forbidden across clients and devices, including mobile.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableMobileUpload": true`` with options ``true`` and ``false``.       |
+---------------------------------------------------------------------------------------------------------------------+

Allow File Downloads on Mobile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Enables file downloads on Mattermost mobile apps.

**False**: Disables file downloads on mobile apps. Users can still download files from a mobile web browser.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableMobileDownload": true`` with options ``true`` and ``false``.     |
+---------------------------------------------------------------------------------------------------------------------+

Public Links
~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Public Links**.

Enable Public File Links
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Allow users to generate public links to files and images for sharing outside the Mattermost system with a public URL.

**False**: The **Get Public Link** option is hidden from the image preview user interface.

.. note:: 

   When set to ``False``, anyone who tries to visit a previously generated public link will receive an error message saying public links have been disabled. When set back to ``True``, old public links will work again unless the **Public Link Salt** has been regenerated.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePublicLink": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

Public Link Salt
^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

32-character salt added to the URL of public links when public links are enabled. Select **Regenerate** in the System Console to create a new salt, which will invalidate all existing public links.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PublicLinkSalt": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Notices
~~~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Notices**.

Enable Admin Notices
^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: System Admins will receive notices about available server upgrades and relevant system administration features. `Learn more <https://docs.mattermost.com/manage/in-product-notices.html>`__.

**False**: System Admins will not receive notices except those that apply to all end users (See ``UserNoticesEnabled``). 

+----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AdminNoticesEnabled": true`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------+

Enable End User Notices
^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: All users will receive notices about available client upgrades and relevant end user features to improve user experience. `Learn more <https://docs.mattermost.com/manage/in-product-notices.html>`__.

**False**: Users will not receive notices about available client upgrades and relevant end user features. 

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserNoticesEnabled": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Authentication
---------------

Authentication settings to enable account creation and log in with email, GitLab, Google or Office 365 OAuth, AD/LDAP, or SAML.

Signup
~~~~~~~

Enable Account Creation
^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Ability to create new accounts is enabled via inviting new members or sharing the team invite link.

**False**: Ability to create accounts is disabled. The **Create Account** button displays an error when trying to signup via an email invite or team invite link.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserCreation": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Restrict account creation to specified email domains
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Teams and user accounts can only be created by a verified email from this list of comma-separated domains (e.g. "corp.mattermost.com, mattermost.com").

This setting only affects email login. For domain restrictions to be effective, you must also set `Require Email Verification <https://docs.mattermost.com/configure/configuration-settings.html#require-email-verification>`__ to ``true``.

+--------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictCreationToDomains": ""`` with string input. |
+--------------------------------------------------------------------------------------------------+

Enable Open Server
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Users can sign up to the server from the root page without an invite.

**False**: Users can only sign up to the server if they receive an invite.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOpenServer": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

Enable Email Invitations
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Users can invite others to the Mattermost system by email.

**False**: Email invitations are disabled.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableEmailInvitations": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Invalidate pending email invites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

This button invalidates active email invitations that have not been accepted by the user. By default email invitations expire after 48 hours.

Email
~~~~~

Enable account creation with email
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Allow team creation and account signup using email and password.

**False**: Email signup is disabled. This limits signup to single sign-on services like OAuth or AD/LDAP.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSignUpWithEmail": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

Require Email Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Require email verification after account creation prior to allowing login.

**False**: Users do not need to verify their email address prior to login. Developers may set this field to ``false`` to skip sending verification emails for faster development.

+----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RequireEmailVerification": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------+

Enable sign-in with email
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Mattermost allows account creation using email and password.

**False**: Log in with email is disabled and does not appear on the login screen. Use this value when you want to limit sign up to a Single Sign-on service like AD/LDAP, SAML, or GitLab.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSignInWithEmail": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

Enable sign-in with username
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Mattermost allows users with email login to log in using their username and password. This setting does not affect AD/LDAP login.

**False**: Log in with username is disabled and does not appear on the login screen.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``EnableSignInWithUsername": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Password
~~~~~~~~~

Minimum Password Length
^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

*This feature was moved to Team Edition in Mattermost v5.0, released June 16th, 2018. Prior to v5.0, this feature is available in legacy Enterprise Edition E10 and E20.*

Minimum number of characters required for a valid password. Must be a whole number greater than or equal to 5 and less than or equal to 64.

+----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MinimumLength": 8`` with numerical input.                   |
+----------------------------------------------------------------------------------------------------------+

Password Requirements
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

*This feature was moved to Team Edition in Mattermost v5.0, released June 16th, 2018. Prior to v5.0, this feature is available in legacy Enterprise Edition E10 and E20.*

Set the required character types to be included in a valid password. Defaults to allow any characters unless otherwise specified by the checkboxes. The error message previewed in the System Console will appear on the account creation page if a user enters an invalid password.

- **At least one lowercase letter**: Select this checkbox if a valid password must contain at least one lowercase letter.
- **At least one uppercase letter**: Select this checkbox if a valid password must contain at least one uppercase letter.
- **At least one number**: Select this checkbox if a valid password must contain at least one number.
- **At least one symbol**: Select this checkbox if a valid password must contain at least one symbol. Valid symbols include: ``!"#$%&'()*+,-./:;<=>?@[]^_`|~``.

This feature's ``config.json`` settings are, respectively:

.. list-table::
    :widths: 80

    * - ``"Lowercase": false`` with options ``true`` and ``false``.
    * - ``"Number": false`` with options ``true`` and ``false``.
    * - ``"Uppercase": false`` with options ``true`` and ``false``.
    * - ``"Symbol": false`` with options ``true`` and ``false``.

Maximum Login Attempts
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Failed login attempts allowed before a user is locked out and required to reset their password via email.

+------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaximumLoginAttempts": 10`` with numerical input. |
+------------------------------------------------------------------------------------------------+

MFA
~~~~

Configure security settings for multi-factor authentication.

The default recommendation for secure deployment is to host Mattermost within your own private network, with VPN clients on mobile, so everything works under your existing security policies and authentication protocols, which may already include multi-factor authentication.

If you choose to run Mattermost outside your private network, bypassing your existing security protocols, we recommend you set up a multi-factor authentication service specifically for accessing Mattermost.

Enable Multi-factor Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Users with LDAP and email authentication will be given the option to require a phone-based passcode, in addition to their password-based authentication, to log in to the Mattermost server. Specifically, they'll be asked to download the `Google Authenticator <https://en.wikipedia.org/wiki/Google_Authenticator>`__ app to their iOS or Android mobile device, connect the app with their account, and then enter a passcode generated by the app on their phone whenever they log in to the Mattermost server.

**False**: Multi-factor authentication is disabled.

+-----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableMultifactorAuthentication": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------------------+

Enforce Multi-factor Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20*

**True**: `Multi-factor authentication (MFA) <https://docs.mattermost.com/onboard/multi-factor-authentication.html>`__ is required for login. New users will be required to configure MFA on signup. Logged in users without MFA configured are redirected to the MFA setup page until configuration is complete. If your system has users with login options other than AD/LDAP and email, MFA must be enforced with the authentication provider outside of Mattermost.

**False**: Multi-factor authentication is optional.

+------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnforceMultifactorAuthentication": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------------+

AD/LDAP
~~~~~~~~

Enable sign-in with AD/LDAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20*

**True**: Mattermost allows login using AD/LDAP or Active Directory.

**False**: Login with AD/LDAP is disabled.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Enable Synchronization with AD/LDAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Mattermost periodically synchronizes users from AD/LDAP.

**False**: AD/LDAP synchronization is disabled.

+--------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSync": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------+

Login Field Name
^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

The placeholder text that appears in the login field on the login page. Typically this would be whatever name is used to refer to AD/LDAP credentials in your company, so it is recognizable to your users. Defaults to **AD/LDAP Username**.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginFieldName": ""`` with string input. |
+---------------------------------------------------------------------------------------+

AD/LDAP Server
^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

The domain or IP address of the AD/LDAP server.

+-----------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LdapServer": ""`` with string input. |
+-----------------------------------------------------------------------------------+

AD/LDAP Port
^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

The port Mattermost will use to connect to the AD/LDAP server. Defaults to ``389``.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LdapPort": 389`` with numerical input. |
+-------------------------------------------------------------------------------------+

Connection Security
^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

The type of connection security Mattermost uses to connect to AD/LDAP.

**None**: No encryption, Mattermost will not attempt to establish an encrypted connection to the AD/LDAP server.

**TLS**: Encrypts the communication between Mattermost and your server using TLS.

**STARTTLS**: Takes an existing insecure connection and attempts to upgrade it to a secure connection using TLS.

If the "No encryption" option is selected it is highly recommended that the AD/LDAP connection is secured outside of Mattermost, for example, by adding a stunnel proxy.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ConnectionSecurity": ""`` with options ``""``, ``"TLS"``, and ``"STARTTLS"``. |
+----------------------------------------------------------------------------------------------------------------------------+

Skip Certificate Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Skips the certificate verification step for TLS or STARTTLS connections. Not recommended for production environments where TLS is required. For testing only.

**False**: Mattermost does not skip certificate verification.

+-------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SkipCertificateVerification": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------+

Private Key
^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

(Optional) The private key file provided by your LDAP Authentication Provider and uploaded if TLS client certificates are being used as the primary authentication mechanism.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PrivateKeyFile": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Public Certificate
^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

(Optional) The public TLS certificate file provided by your LDAP Authentication Provider and uploaded if TLS client certificates are being used as the primary authentication mechanism.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PublicCertificateFile": ""`` with with string input. |
+---------------------------------------------------------------------------------------------------+

Bind Username
^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

The username used to perform the AD/LDAP search. This should be an account created specifically for use with Mattermost. Its permissions should be limited to read-only access to the portion of the AD/LDAP tree specified in the **Base DN** field. When using Active Directory, **Bind Username** should specify domain in ``"DOMAIN/username"`` format. This field is required, and anonymous bind is not currently supported.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BindUsername": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Bind Password
^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Password of the user given in **Bind Username**. Anonymous bind is not currently supported.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BindPassword": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Base DN
^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

The **Base Distinguished Name** of the location where Mattermost should start its search for users in the AD/LDAP tree.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BaseDN": ""`` with string input. |
+-------------------------------------------------------------------------------+

User Filter
^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

(Optional) Enter an AD/LDAP Filter to use when searching for user objects (accepts `general syntax <https://www.ldapexplorer.com/en/manual/109010000-ldap-filter-syntax.htm>`__). Only the users selected by the query will be able to access Mattermost.

Sample filters for Active Directory:

- To filter out disabled users: ``(&(objectCategory=Person)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))``.
- To filter out by group membership, determine the distinguishedName of your group, then use the group membership general syntax format as your filter.

  * For example, if the security group distinguishedName is ``CN=group1,OU=groups,DC=example,DC=com``, then the user filter to use is: ``(memberOf=CN=group1,OU=groups,DC=example,DC=com)``. Note that the user must explicitly belong to this group for the filter to apply.

This filter uses the permissions of the **Bind Username** account to execute the search. Administrators should make sure to use a specially created account for Bind Username with read-only access to the portion of the AD/LDAP tree specified in the **Base DN** field.

+-----------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserFilter": ""`` with string input. |
+-----------------------------------------------------------------------------------+

Group Filter
^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) Enter an AD/LDAP Filter to use when searching for group objects (accepts `general syntax <https://www.ldapexplorer.com/en/manual/109010000-ldap-filter-syntax.htm>`__). Only the groups selected by the query will be able to access Mattermost.

This filter is defaulted to ``(|(objectClass=group)(objectClass=groupOfNames)(objectClass=groupOfUniqueNames))`` when blank.

.. note::
  This filter is used only when AD/LDAP Group Sync is enabled. See `AD/LDAP Group Sync documentation <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`__ for more information on enabling and configuring AD/LDAP Group Sync.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GroupFilter": ""`` with string input. |
+------------------------------------------------------------------------------------+

Enable Admin Filter
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables System Admins to configure an AD/LDAP filter.

**False**: Disables the ability for System Admins to configure an AD/LDAP filter.

Admin Filter
^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) Enter a filter to use for designating the System Admin role to users. When enabled the user is promoted to this role on their next login or at the next scheduled AD/LDAP sync. If the Admin Filter is removed, users who are currently logged in retain their Admin role. When they log out this is revoked and on their next login they will no longer have Admin privileges.

This filter default is ``false`` and must be set to ``true`` in order for the Admin Filter to be used.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAdminFilter": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Guest Filter
^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) Enter an AD/LDAP Filter to use when searching for external users who have Guest Access to Mattermost. Only the users selected by the query will be able to log in to and use Mattermost as Guests. This filter default is blank.

See the `Guest Accounts documentation <https://docs.mattermost.com/onboard/guest-accounts.html>`__ for more information.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GuestFilter": ""`` with string input. |
+------------------------------------------------------------------------------------+

ID Attribute
^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

The attribute in the AD/LDAP server used as a unique identifier in Mattermost. It should be an AD/LDAP attribute with a value that does not change.

If a user's ID Attribute changes, a new Mattermost account (unassociated with the previous one) is created. To prevent this, it's recommended that a unique attribute such as ``objectGUID`` in Active Directory and ``entryUUID`` in LDAP be used instead.

Before making any changes confirm with your LDAP provider whether these attributes are available in your environment.

If you need to change this field after users have already logged in, use the `mattermost ldap idmigrate <https://docs.mattermost.com/manage/command-line-tools.html#mattermost-ldap-idmigrate>`__ CLI tool.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------+

Login ID Attribute
^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

The attribute in the AD/LDAP server used to log in to Mattermost. Normally this attribute is the same as the **Username Attribute** field above.

If your team typically uses domain\username to log in to other services with AD/LDAP, you may enter domain\username in this field to maintain consistency between sites.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginIdAttribute": ""`` with string input. |
+-----------------------------------------------------------------------------------------+

Username Attribute
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

The attribute in the AD/LDAP server used to populate the username field in Mattermost. This may be the same as the Login ID Attribute.

This attribute will be used within the Mattermost user interface to identify and mention users. For example, if a Username Attribute is set to **john.smith** a user typing ``@john`` will see ``@john.smith`` in their auto-complete options and posting a message with ``@john.smith`` will send a notification to that user that they've been mentioned.

The **Username Attribute** may be set to the same value used to log in to the system, called a **Login ID Attribute**, or it can be mapped to a different value.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UsernameAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Email Attribute
^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

The attribute in the AD/LDAP server used to populate the email address field in Mattermost.

Email notifications will be sent to this email address, and this email address may be viewable by other Mattermost users depending on privacy settings chosen by the System Admin.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EmailAttribute": ""`` with string input.    |
+------------------------------------------------------------------------------------------+

First Name Attribute
^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

(Optional) The attribute in the AD/LDAP server used to populate the first name of users in Mattermost. When set, users cannot edit their first name, since it is synchronized with the LDAP server. When left blank, users can set their first name as part of their :doc:`profile settings </welcome/manage-your-profile>`.

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FirstNameAttribute": ""`` with string input.    |
+----------------------------------------------------------------------------------------------+

Last Name Attribute
^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

(Optional) The attribute in the AD/LDAP server used to populate the last name of users in Mattermost. When set, users cannot edit their last name, since it is synchronized with the LDAP server. When left blank, users can set their last name as part of their :doc:`profile settings </welcome/manage-your-profile>`.

+-----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LastNameAttribute": ""`` with string input.      |
+-----------------------------------------------------------------------------------------------+

Nickname Attribute
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

(Optional) The attribute in the AD/LDAP server used to populate the nickname of users in Mattermost. When set, users cannot edit their nickname, since it is synchronized with the LDAP server. When left blank, users can set their nickname as part of their :doc:`profile settings </welcome/manage-your-profile>`.

+--------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"NicknameAttribute": ""`` with string input.   |
+--------------------------------------------------------------------------------------------+

Position Attribute
^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

(Optional) The attribute in the AD/LDAP server used to populate the position field in Mattermost. When set, users cannot edit their position, since it is synchronized with the LDAP server. When left blank, users can set their position as part of their :doc:`profile settings </welcome/manage-your-profile>`.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PositionAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Profile Picture Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

The attribute in the AD/LDAP server used to synchronize (and lock) the profile picture used in Mattermost.

The Mattermost server will replace the user’s profile image upon login (not at the sync interval as with other attributes). The sync will not occur if the current Mattermost profile image matches the image associated with that user in AD/LDAP.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PictureAttribute": ""`` with string input. |
+-----------------------------------------------------------------------------------------+

Group Display Name Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Required) Enter an AD/LDAP Group Display name attribute used to populate Mattermost Group names.

.. note::
  This attribute is used only when AD/LDAP Group Sync is enabled. See `AD/LDAP Group Sync documentation <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`__ for more information on enabling and configuring AD/LDAP Group Sync.

+--------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GroupDisplayNameAttribute": ""`` with string input. |
+--------------------------------------------------------------------------------------------------+

Group Id Attribute
^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Required) Enter an AD/LDAP Group ID attribute to use as a unique identifier for Groups. This should be an AD/LDAP value that does not change. This is usually ``entryUUID`` for LDAP and ``objectGUID`` for AD.

.. note::
  This attribute is used only when AD/LDAP Group Sync is enabled. See `AD/LDAP Group Sync documentation <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`__ for more information on enabling and configuring AD/LDAP Group Sync.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GroupIdAttribute": ""`` with string input. |
+-----------------------------------------------------------------------------------------+

Synchronization Interval (minutes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Set how often Mattermost accounts synchronize attributes with AD/LDAP, in minutes. 

When synchronizing, Mattermost queries AD/LDAP for relevant account information and updates Mattermost accounts based on changes to attributes (first name, last name, and nickname). 

When accounts are disabled in AD/LDAP users are made inactive in Mattermost, and their active sessions are revoked once Mattermost synchronizes attributes. To synchronize immediately after disabling an account, use the **AD/LDAP Synchronize Now** button.

+-----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SyncIntervalMinutes": 60`` with numerical input. |
+-----------------------------------------------------------------------------------------------+

.. note::
  LDAP syncs cause a large number of database read queries. Ensure that you monitor database load during a sync to determine how often these syncs should happen in your environment in order to minimize performance degradation.

Maximum Page Size
^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

The maximum number of users the Mattermost server will request from the AD/LDAP server at one time. Use this setting if your AD/LDAP server limits the number of users that can be requested at once.

- A value of 0 is unlimited and does not paginate the results.
- A value of 1500 is recommended to align with the default AD/LDAP ``MaxPageSize`` setting.

+--------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxPageSize": 0`` with numerical input. |
+--------------------------------------------------------------------------------------+

Query Timeout (seconds)
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

The timeout value for queries to the AD/LDAP server. Increase this value if you are getting timeout errors caused by a slow AD/LDAP server.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"QueryTimeout": 60`` with numerical input. |
+----------------------------------------------------------------------------------------+

AD/LDAP Test
^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

This button can be used to test the connection to the AD/LDAP server. If the test is successful, it shows a confirmation message and if there is a problem with the configuration settings it will show an error message.

AD/LDAP Synchronize Now
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

This button causes AD/LDAP synchronization to occur as soon as it is pressed. Use it whenever you have made a change in the AD/LDAP server you want to take effect immediately. After using the button, the next AD/LDAP synchronization will occur after the time specified by the Synchronization Interval.

You can monitor the status of the synchronization job in the table below this button.

.. note::
  If synchronization **Status** displays as ``Pending`` and does not complete, make sure that the **Enable Synchronization with AD/LDAP** setting is set to ``true``.

.. figure:: ../images/ldap-sync-table.png

.. _saml-enterprise:

SAML
~~~~~

.. note::
   In line with Microsoft ADFS guidance we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`__.

Enable Login With SAML
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Mattermost allows login using SAML. Please see `documentation <https://docs.mattermost.com/onboard/sso-saml.html>`__ to learn more about configuring SAML for Mattermost.

**False**: Login with SAML is disabled.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Enable Synchronizing SAML Accounts With AD/LDAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Mattermost periodically synchronizes SAML user attributes, including user deactivation and removal, with AD/LDAP. Enable and configure synchronization settings at **Authentication > AD/LDAP**. See `documentation <https://docs.mattermost.com/onboard/ad-ldap.html>`__ to learn more.

**False**: Synchronization of SAML accounts with AD/LDAP is disabled.

+----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSyncWithLdap": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------+

Ignore Guest Users When Synchronizing with AD/LDAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Available when ``Enable Synchronizing SAML Accounts With AD/LDAP`` is set to ``true``. 

**True**: Mattermost ignores Guest Users identified by the Guest Attribute when synchronizing with AD/LDAP on user deactivation and removal. Manage guest deactivation manually via **System Console > Users**. See `documentation <https://docs.mattermost.com/onboard/ad-ldap.html>`__ to learn more.

**False**: Synchronization of SAML deactivates and removes Guest Users when synchronizing with AD/LDAP.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IgnoreGuestsLdapSync": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

Override SAML Bind Data with AD/LDAP Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Mattermost overrides the SAML ID attribute with the AD/LDAP ID attribute if configured or overrides the SAML Email attribute with the AD/LDAP Email attribute if SAML ID attribute is not present. See `documentation <https://docs.mattermost.com/onboard/ad-ldap.html>`__ to learn more.

**False**: Mattermost uses the email attribute to bind users to SAML.

.. note::
  Moving from ``true`` to ``false`` will prevent the override from happening. To prevent the disabling of user accounts, SAML IDs must match the LDAP IDs when this feature is enabled. This setting should be set to ``false`` unless LDAP sync is enabled.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSyncWithLdapIncludeAuth": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------------------+

Identity Provider Metadata URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The URL where Mattermost sends a request to obtain setup metadata from the provider.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdpMetadataUrl": ""`` with string input. |
+---------------------------------------------------------------------------------------+

SAML SSO URL
^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The URL where Mattermost sends a SAML request to start login sequence.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdpURL": ""`` with string input. |
+-------------------------------------------------------------------------------+

Identity Provider Issuer URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The issuer URL for the Identity Provider you use for SAML requests.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdpDescriptorUrl": ""`` with string input. |
+-----------------------------------------------------------------------------------------+

Identity Provider Public Certificate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The public authentication certificate issued by your Identity Provider.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdpCertificateFile": ""`` with string input. |
+-------------------------------------------------------------------------------------------+

Verify Signature
^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Mattermost verifies that the signature sent from the SAML Response matches the Service Provider Login URL.

**False**: Not recommended for production environments. For testing only.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Verify": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------+

Service Provider Login URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Enter ``https://<your-mattermost-url>/login/sso/saml`` (example: ``https://example.com/login/sso/saml``). Make sure you use HTTP or HTTPS in your URL depending on your server configuration. This field is also known as the Assertion Consumer Service URL.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AssertionConsumerServiceURL": ""`` with string input. |
+----------------------------------------------------------------------------------------------------+

Service Provider Identifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The unique identifier for the Service Provider, usually the same as Service Provider Login URL. In ADFS, this must match the Relying Party Identifier.

+--------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ServiceProviderIdentifier": ""`` with string input. |
+--------------------------------------------------------------------------------------------------+

Enable Encryption
^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Mattermost will decrypt SAML Assertions encrypted with your Service Provider Public Certificate.

**False**: Not recommended for production environments. For testing only.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Encrypt": true`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Service Provider Private Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The private key used to decrypt SAML Assertions from the Identity Provider.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PrivateKeyFile": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Service Provider Public Certificate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The certificate file used to generate the signature on a SAML request to the Identity Provider for a service provider initiated SAML login, when Mattermost is the Service Provider.

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PublicCertificateFile": ""`` with string input. |
+----------------------------------------------------------------------------------------------+

Sign Request
^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

When ``true``, Mattermost signs the SAML request using your Service Provider Private Key. When ``false``, Mattermost does not sign the SAML request.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SignRequest": ""`` with string input. |
+------------------------------------------------------------------------------------+

Signature Algorithm
^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The signature algorithm used to sign the request. Supported options are `RSAwithSHA1 <https://www.w3.org/2000/09/xmldsig#rsa-sha1>`__, `RSAwithSHA256 <https://www.w3.org/2000/09/xmldsig#rsa-sha1>`__, and `RSAwithSHA512 <https://www.w3.org/2001/04/xmldsig-more#rsa-sha512>`__.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SignatureAlgorithm": ""`` with string input. |
+-------------------------------------------------------------------------------------------+

Canonical Algorithm
^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The canonicalization algorithm. Supported options are ``Canonical1.0`` for `Exclusive XML Canonicalization 1.0 (omit comments) <https://www.w3.org/TR/2002/REC-xml-exc-c14n-20020718/>`__ (``http://www.w3.org/2001/10/xml-exc-c14n#``) and ``Canonical1.1`` for `Canonical XML 1.1 (omit comments) <https://www.w3.org/TR/2008/REC-xml-c14n11-20080502/>`__ (``http://www.w3.org/2006/12/xml-c14n11``).

+-------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CanonicalAlgorithm": "Canonical1.0"`` with string input. |
+-------------------------------------------------------------------------------------------------------+

Email Attribute
^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The attribute in the SAML Assertion that will be used to populate the email addresses of users in Mattermost.

Email notifications will be sent to this email address, and this email address may be viewable by other Mattermost users depending on privacy settings chosen by the System Admin.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EmailAttribute": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Username Attribute
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

The attribute in the SAML Assertion that will be used to populate the username field in Mattermost user interface. This attribute will be used within the Mattermost user interface to identify and mention users. For example, if a Username Attribute is set to **john.smith** a user typing ``@john`` will see ``@john.smith`` in their auto-complete options and posting a message with ``@john.smith`` will send a notification to that user that they've been mentioned.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UsernameAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Id Attribute
^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion used to bind users from SAML to users in Mattermost.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------+

Guest Attribute
^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion used to apply a Guest role to users in Mattermost.

See the `Guest Accounts documentation <https://docs.mattermost.com/onboard/guest-accounts.html>`__ for more information.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GuestAttribute": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Enable Admin Attribute
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Enables System Admins to configure the SAML Assertion.

**False**: Disables the ability for System Admins to configure the SAML Assertion.

Admin Attribute
^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion for designating System Admins. The user is automatically promoted to this role on their next login. If the Admin Attribute is removed, users who are currently logged in retain their Admin role. When they log out this is revoked and on their next login they will no longer have Admin privileges.

This attribute's default is ``false`` and must be set to ``true`` in order for the Admin Attribute to be used.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAdminAttribute": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

First Name Attribute
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion that will be used to populate the first name of users in Mattermost.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FirstNameAttribute": ""`` with string input. |
+-------------------------------------------------------------------------------------------+

Last Name Attribute
^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion that will be used to populate the last name of users in Mattermost.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LastNameAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Nickname Attribute
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion that will be used to populate the nickname of users in Mattermost.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"NicknameAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Position Attribute
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion that will be used to populate the position field for users in Mattermost (typically used to describe a person's job title or role at the company).

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PositionAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Preferred Language Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion that will be used to populate the language of users in Mattermost.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LocaleAttribute": ""`` with string input. |
+----------------------------------------------------------------------------------------+

Login Button Text
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

(Optional) The text that appears in the login button on the login page. Defaults to **SAML**.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonText": ""`` with string input. |
+----------------------------------------------------------------------------------------+

OAuth 2.0
~~~~~~~~~

.. note::
  
  OAuth 2.0 is being deprecated and will be replaced by `OpenID Connect <https://docs.mattermost.com/configure/configuration-settings.html#openid-connect>`__ in a future release.

Settings to configure OAuth login for account creation and login.

Select OAuth 2.0 service provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Choose whether OAuth can be used for account creation and login. Options include:

- **Do not allow login via an OAuth 2.0 provider**
- **GitLab** (available in all plans; see `GitLab Settings <https://docs.mattermost.com/configure/configuration-settings.html#gitlab-settings>`__ for details)
- **Google Apps** (Available in Mattermost Enterprise and Professional; see `Google Settings <https://docs.mattermost.com/configure/configuration-settings.html#google-settings>`__ for details)
- **Office 365** (Available in Mattermost Enterprise and Professional; see `Office 365 Settings <https://docs.mattermost.com/configure/configuration-settings.html#office-365-settings>`__ for details)

This feature's setting does not appear in ``config.json``.

GitLab
''''''

Enable authentication with GitLab
.................................

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Allow team creation and account signup using GitLab OAuth. To configure, input the **Secret** and **Id** credentials.

**False**: GitLab OAuth cannot be used for team creation or account signup.

.. note:: 
   For Enterprise subscriptions, GitLab settings can be found under **OAuth 2.0**

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Application ID
..............

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Obtain this value by logging into your GitLab account. Go to **Profile Settings > Applications > New Application**, enter a Name, then enter Redirect URLs ``https://<your-mattermost-url>/login/gitlab/complete`` (example: ``https://example.com:8065/login/gitlab/complete`` and ``https://<your-mattermost-url>/signup/gitlab/complete``.

+---------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input. |
+---------------------------------------------------------------------------+

Application Secret Key
......................

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Obtain this value by logging into your GitLab account. Go to **Profile Settings > Applications > New Application**, enter a Name, then enter Redirect URLs ``https://<your-mattermost-url>/login/gitlab/complete`` (example: ``https://example.com:8065/login/gitlab/complete`` and ``https://<your-mattermost-url>/signup/gitlab/complete``.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input. |
+-------------------------------------------------------------------------------+

GitLab Site URL
................

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Specify the URL of your GitLab instance (example ``https://example.com:3000``). If your GitLab instance is not set up with SSL, start the URL with ``http://`` instead of ``https://``.

User API Endpoint
.................

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Enter ``https://<your-gitlab-url>/api/v3/user`` (example: ``https://example.com:3000/api/v3/user``). Use HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserApiEndpoint": ""`` with string input. |
+----------------------------------------------------------------------------------------+

Auth Endpoint
..............

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Enter ``https://<your-gitlab-url>/oauth/authorize`` (example: ``https://example.com:3000/oauth/authorize``). Use HTTP or HTTPS depending on how your server is configured.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AuthEndpoint": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Token Endpoint
..............

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Enter ``https://<your-gitlab-url>/oauth/token`` (example: ``https://example.com:3000/oauth/token``). Use HTTP or HTTPS depending on how your server is configured.

+--------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TokenEndpoint": ""`` with string input. |
+--------------------------------------------------------------------------------------+

Google
''''''

Enable authentication with Google by selecting ``Google Apps`` from **OAuth 2.0 > Select OAuth 2.0 service provider**.

**True**: Allow team creation and account signup using Google OAuth. To configure, input the **Client ID** and **Client Secret** credentials. See `the documentation <https://docs.mattermost.com/onboard/sso-google.html>`__ for more detail.

**False**: Google OAuth cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Client ID
.........

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

+---------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input. |
+---------------------------------------------------------------------------+

Client Secret
.............

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input. |
+-------------------------------------------------------------------------------+

User API Endpoint
..................

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

We recommend you use ``https://people.googleapis.com/v1/people/me?personFields=names,emailAddresses,nicknames,metadata`` as the User API Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserApiEndpoint": "https://people.googleapis.com/v1/people/me?personFields=names,emailAddresses,nicknames,metadata"``   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Auth Endpoint
..............

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

We recommend you use ``https://accounts.google.com/o/oauth2/v2/auth`` as the Auth Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+---------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AuthEndpoint": "https://accounts.google.com/o/oauth2/v2/auth"`` with string input. |
+---------------------------------------------------------------------------------------------------------------------------------+

Token Endpoint
..............

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

We recommend that you use ``https://www.googleapis.com/oauth2/v4/token`` as the Token Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+--------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TokenEndpoint": "https://www.googleapis.com/oauth2/v4/token"`` with string input. |
+--------------------------------------------------------------------------------------------------------------------------------+

Office 365
'''''''''''

.. note::
   In line with Microsoft ADFS guidance we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`__.

Enable authentication with Office 365 by selecting **Office 365** from **System Console > Authentication > OAuth 2.0 > Select OAuth 2.0 service provider**.

**True**: Allow team creation and account signup using Office 365 OAuth. To configure, input the **Application ID** and **Application Secret Password** credentials. See `the documentation <https://docs.mattermost.com/onboard/sso-office.html>`__ for more detail.

**False**: Office 365 OAuth cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Application ID
..............

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Microsoft or Office account.

+---------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input. |
+---------------------------------------------------------------------------+

Application Secret Password
...........................

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Microsoft or Office account.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input. |
+-------------------------------------------------------------------------------+

Directory (tenant) ID
.....................

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

This value is the ID of the application's AAD directory.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DirectoryId": ""`` with string input. |
+------------------------------------------------------------------------------------+

User API Endpoint
.................

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

We recommend using ``https://graph.microsoft.com/v1.0/me`` as the User API Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserApiEndpoint": "https://graph.microsoft.com/v1.0/me"`` with string input. |
+---------------------------------------------------------------------------------------------------------------------------+

Auth Endpoint
.............

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

We recommend using ``https://accounts.google.com/o/oauth2/v2/auth`` as the Auth Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AuthEndpoint": "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"`` with string input.                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Token Endpoint
..............

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

We recommend that you use ``https://login.microsoftonline.com/common/oauth2/v2.0/token`` as the Token Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TokenEndpoint": "https://login.microsoftonline.com/common/oauth2/v2.0/token"`` with string input. |
+------------------------------------------------------------------------------------------------------------------------------------------------+

OpenID Connect
~~~~~~~~~~~~~~

Select OpenID Connect service provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Choose whether OpenID Connect can be used for account creation and login. Options include:

- **Do not allow login via an OpenID provider**
- **GitLab** (available in all plans; see `GitLab Settings <https://docs.mattermost.com/configure/configuration-settings.html#gitlab-settings>`__ for details)
- **Google Apps** (Available in Mattermost Enterprise and Professional; see `Google Settings <https://docs.mattermost.com/configure/configuration-settings.html#google-settings>`__ for details)
- **Office 365** (Available in Mattermost Enterprise and Professional; see `Office 365 Settings <https://docs.mattermost.com/configure/configuration-settings.html#office-365-settings>`__ for details)
- **OpenID Connect (Other)** (Available in Mattermost Enterprise and Professional; see `OpenID Connect Settings <https://docs.mattermost.com/configure/configuration-settings.html#openid-connect-other-settings>`__ for more detail)

This feature's setting does not appear in ``config.json``.

GitLab Settings
'''''''''''''''

GitLab Site URL
................

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20. Not available in Cloud Starter.*

Specify the URL of your GitLab instance (example ``https://example.com:3000``). If your GitLab instance is not set up with SSL, start the URL with ``http://`` instead of ``https://``.

Discovery Endpoint
..................

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20*
*Not available in Cloud Starter*

Obtain this value by registering Mattermost as an application in your service provider account. Should be in the format ``https://myopenid.provider.com/{my_company}/.well-known/openid-configuration`` where the value of *{my_company}* is replaced with your organization.

Client ID
.........

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20*
*Not available in Cloud Starter*

Obtain this value by registering Mattermost as an application in your service provider account.

Client Secret
..............

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20*
*Not available in Cloud Starter*

Obtain this value by registering Mattermost as an application in your Google account.

Google Settings
'''''''''''''''

Enable authentication with Google by selecting ``Google Apps`` from **System Console > Authentication > OpenID Connect > Select service provider**.

**True**: Allow team creation and account signup using Google OpenID Connect. To configure, input the **Client ID**, **Client Secret**, and **DiscoveryEndpoint** credentials. See `the documentation <https://docs.mattermost.com/onboard/sso-google.html>`__ for more detail.

**False**: Google OpenID Connect cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Discovery Endpoint
...................

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

This value is prepopulated with ``https://accounts.google.com/.well-known/openid-configuration``.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DiscoveryEndpoint": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Client ID
..........

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

+---------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input. |
+---------------------------------------------------------------------------+

Client Secret
.............

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input. |
+-------------------------------------------------------------------------------+

Office 365 Settings
'''''''''''''''''''

.. note::
   In line with Microsoft ADFS guidance, we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_.

Enable authentication with Office 365 by selecting **Office 365** from **System Console > Authentication > OpenID Connect > Select service provider**.

**True**: Allow team creation and account signup using Office 365 OpenID Connect. To configure, input the **Application ID** and **Application Secret Password** credentials. See `the documentation <https://docs.mattermost.com/onboard/sso-office.html>`__ for more detail.

**False**: Office 365 OpenID Connect cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Directory (tenant) ID
.....................

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

This value is the ID of the application's AAD directory.

Discovery Endpoint
..................

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

This value is prepopulated with https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration.

Client ID
..........

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

Client Secret
..............

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

OpenID Connect (Other) 
'''''''''''''''''''''''

Enable authentication with a service provider by selecting ``OpenID Connect (Other)`` from **System Console > Authentication > OpenID Connect > Select service provider**.

**True**: Allow team creation and account signup using OpenID Connect. To configure, input the **Client ID**, **Client Secret**, and **DiscoveryEndpoint** credentials. See `the documentation <https://docs.mattermost.com/onboard/sso-openidconnect.html>`__ for more detail.

**False**: OpenID Connect cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Button Name
............

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Specify the text that displays on the OpenID login button.

+-----------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ButtonText": ""`` with string input. |
+-----------------------------------------------------------------------------------+

Button Color
.............

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Specify the color of the OpenID login button for white labeling purposes. Use a hex code with a #-sign before the code, for example ``#145DBF``.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ButtonColor": ""`` with string input. |
+------------------------------------------------------------------------------------+

Discovery Endpoint
..................

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your service provider account. Should be in the format ``https://myopenid.provider.com/{my_company}/.well-known/openid-configuration`` where the value of *{my_company}* is replaced with your organization.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DiscoveryEndpoint": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Client ID
..........

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your service provider account.

+---------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input. |
+---------------------------------------------------------------------------+

Client Secret
..............

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your service provider account.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input. |
+-------------------------------------------------------------------------------+

Guest Access
~~~~~~~~~~~~

Enable Guest Access
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20*

**True**: Allow guest invitations to channels within teams. Please see `Guest Accounts documentation <https://docs.mattermost.com/onboard/guest-accounts.html>`__ for more information.

**False**: Email signup is disabled. This limits signup to Single sign-on services like OAuth or AD/LDAP.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Whitelisted Guest Domains
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20*

When populated, guest accounts can only be created by a verified email from this list of comma-separated domains.

+--------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictCreationToDomains": ""`` with string input. |
+--------------------------------------------------------------------------------------------------+

Enforce Multi-factor Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20*

This setting defaults to false and is read-only if multi-factor authentication is not enforced for regular users.

**True**: Multi-factor authentication (MFA) is required for login. New guest users will be required to configure MFA on sign-up. Logged in guest users without MFA configured are redirected to the MFA setup page until configuration is complete.

**False**: Multi-factor authentication for guests is optional.

+------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnforceMultifactorAuthentication": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------------+

Plugins
--------

Settings to configure Mattermost plugins.

Plugin Management
~~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Plugins > Plugin Management**.

Enable Plugins
^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables plugins on your Mattermost server. Use plugins to integrate with third-party systems, extend functionality, or customize the user interface of your Mattermost server. See `documentation <https://developers.mattermost.com/integrate/admin-guide/admin-plugins-beta/>`__ to learn more.

**False**: Disables plugins on your Mattermost server.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------+

Require Plugin Signature
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Require valid plugin signatures before starting managed or unmanaged plugins. Pre-packaged plugins are not subject to plugin signature verification. Plugins installed through the Plugin Marketplace are always subject to plugin signature verification at the time of download.

**False**: Don't require valid plugin signatures before starting managed or unmanaged plugins. Pre-packaged plugins are not subject to plugin signature verification. Plugins installed through the Plugin Marketplace are always subject to plugin signature verification at the time of download.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RequirePluginSignature": true`` with options ``true`` and ``false``.   |
+---------------------------------------------------------------------------------------------------------------------+

Automatic Prepackaged Plugins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Any pre-packaged plugins enabled in the configuration will be installed or upgraded automatically. If a newer version is already installed, no changes are made.

**False**: Pre-packaged plugins aren't installed or upgraded automatically but may be installed manually from the Plugin Marketplace, even when offline.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AutomaticPrepackagedPlugins": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

Enable Marketplace
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables Plugin Marketplace on your Mattermost server for all System Admins.

**False**: Disables Plugin Marketplace on your Mattermost server for all System Admins.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableMarketplace": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

Enable Remote Marketplace
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: The server will attempt to connect to the configured Plugin Marketplace to show the latest plugins. If the connection fails, the Plugin Marketplace shows only pre-packaged and already installed plugins alongside a connection error.

**False**: The server won't attempt to connect to a remote marketplace, and will show only pre-packaged and already installed plugins. Use this setting if your server can't connect to the internet.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableRemoteMarketplace": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

This setting only takes effect when ``"EnableMarketplace": true``.

.. note::
   For the Remote Marketplace to operate, each host running the Mattermost service requires network access to the marketplace service endpoint (hosted at ``https://api.integrations.mattermost.com``, see `Marketplace URL <#marketplace-url>`__ ).

Marketplace URL
^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

If the Marketplace is enabled, this setting specifies which URL should be used to query for new Marketplace plugins.

+------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MarketplaceUrl": "https://api.integrations.mattermost.com"`` with string input. |
+------------------------------------------------------------------------------------------------------------------------------+

Installed Plugin State
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Lists installed plugins on your Mattermost server and whether they are enabled. Pre-packaged plugins are installed by default and can be deactivated, but not removed.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PluginStates": {}`` with object input mapping plugin IDs as keys to objects, each of which contains a key ``"Enable": false`` with options ``true`` or ``false``. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Plugin Settings
^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Settings specific to each Mattermost plugin.

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Plugins": {}`` with object input mapping plugin IDs as keys to objects containing plugin-specific data. |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

Agenda
~~~~~~~

Access the following configuration settings in the System Console by going to **Plugins > Agenda**.

Enable Plugin
^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables the Agenda plugin on your Mattermost server.

**False**: Disables the Agenda plugin on your Mattermost server.

Antivirus
~~~~~~~~~~

This plugin allows the forwarding of uploaded files to an antivirus scanning application, `ClamAV anti-virus software <https://www.clamav.net/>`__, and prevents the upload from completing if there is a virus detected in the file. 

Use this plugin to prevent users from inadvertently spreading malware or viruses via your Mattermost server. See the `Mattermost Antivirus Plugin <https://github.com/mattermost/mattermost-plugin-antivirus>`__ documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Antivirus**.

Enable Plugin
^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables the Antivirus plugin on your Mattermost server.

**False**: Disables the Antivirus plugin on your Mattermost server.

ClamAV - Host and Port
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify the hostname and port to connect to the ClamAV server.

Scan Timeout (seconds)
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify how long the virus scan can take before timing out.

Apps
~~~~

Enable Plugin
^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud.rst
  :start-after: :nosearch:

**True**: Enables the Apps plugin on your Mattermost server.

**False**: Disables the Apps plugin on your Mattermost server.

To create your own Mattermost App, see the `Mattermost Apps <https://developers.mattermost.com/integrate/apps/>`__ developer documentation.

Autolink
~~~~~~~~~

This plugin creates regular expression (regexp) patterns that are reformatted into a Markdown link before the message is saved into the database. System Admins can configure this plugin in the ``config.json`` file, using the ``/autolink`` slash command (when enabled), or through using the System Console. See the `Autolink Plugin <https://github.com/mattermost/mattermost-plugin-autolink/blob/master/README.md>`__ documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Autolink**.

Enable Plugin
^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables the Autolink plugin on your Mattermost server.

**False**: Disables the Autolink plugin on your Mattermost server.

Enable administration with /autolink command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables the ability to configure the Apps plugin using the ``/autolink`` slash command.

**False**: Disables the ability to use the slash command to configure the plugin.

Apply plugin to updated posts as well as new posts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Applies the plugin to updated posts as well as new posts. 

**False**: Applies the plugin to new posts only.

Admin User IDs
^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify users authorized to administer the plugin in addition to System Admins. Separate multiple user IDs with commas.

.. tip::
  Find user IDs by going to **System Console > User Management > Users**.

AWS SNS
~~~~~~~~

This plugin is used to receive alert notifications from `Amazon AWS CloudWatch <https://aws.amazon.com/cloudwatch/>`__ to Mattermost channels via `AWS Simple Notification Server (SNS) <https://docs.aws.amazon.com/sns/latest/dg/welcome.html>`__. 

Access the following configuration settings in the System Console by going to **Plugins > AWS SNS**.

Enable Plugin
^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables the AWS SNS plugin on your Mattermost server.

**False**: Disables the AWS SNS plugin on your Mattermost server.

Channel to send notifications to
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify the channel to send notifications to in the format ``teamname,channelname``. For example, for a channel with a URL of ``https://example.com/myteam/channels/mychannel``, set the value to ``myteam,mychannel``. If the specified channel does not exist, the plugin creates the channel for you.

Authorized User IDs
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify users authorized to accept AWS SNS subscriptions to a Mattermost channel. Separate multiple user IDs with commas.

.. tip::
  Find user IDs by going to **System Console > User Management > Users**.

Token
^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Generate a token to validate incoming requests from AWS SNS by selecting ``Regenerate``.

Calls (beta)
~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Plugins > Calls**.

Enable Plugin
^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables the calls plugin on your Mattermost workspace.

**False**: Disables the calls plugin on your Mattermost workspace.

RTC Server Port
^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

The UDP port the RTC server will listen on. All calls traffic will be served through this port. The Default setting is 8443.

Changing this setting requires a plugin restart to take effect.

Enable on specific channels
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Allow Channel Admins to enable or disable calls on specific channels. It also allows participants in DMs/GMs to enable or disable calls.

**False**: Only System Admins will be able to enable or disable calls on specific channels.

Enable on all channels
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Enable calls by default on all channels.

**False**: Calls have to be explicitly enabled on channels.

Max call participants
^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

The maximum number of participants that can join a single call. This is an optional field and default is 0 (unlimited). The maximum recommended setting is 200.

ICE Host Override
^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

An optional override to the host that gets advertised to clients when connecting to calls. Depending on the network infrastructure (e.g. instance behind a NAT device) it may be necessary to set this field to the client facing external IP in order to let clients connect successfully. When empty or unset, the RTC service will attempt to automatically find the instance's public IP through STUN.

This is an optional field. Changing this setting requires a plugin restart to take effect.

ICE Servers Configurations
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

A list of ICE servers (STUN/TURN) to be used by the service. Value should be valid JSON.

Default is ``[{"urls": ["stun:stun.global.calls.mattermost.com:3478"]}]``

**Example**

.. code-block:: json

  [
   {
      "urls":[
         "stun:stun.global.calls.mattermost.com:3478"
      ]
   },
   {
      "urls":[
         "turn:turn.example.com:3478"
      ],
      "username":"webrtc",
      "credentials":"turnpassword"
   }
  ]

This is an optional field. Changing this setting may require a plugin restart to take effect.

TURN Static Auth Secret
^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

A static secret used to generate short-lived credentials for TURN servers.

This is an optional field.

TURN Credentials Expiration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

The expiration, in minutes, of the short-lived credentials generated for TURN servers.

Server Side TURN
^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: The RTC server will use the configured TURN candidates for server-initiated connections.

**False**: TURN will be used only on the client-side.

Changing this setting requires a plugin restart to take effect.

RTCD Service URL
^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

The URL to a running `rtcd <https://github.com/mattermost/rtcd>`__ service instance that will host the calls. When set (non empty) all the calls will be handled by this external service.

This is an optional field. Changing this setting requires a plugin restart to take effect.

Channel Export
~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Plugins > Channel Export**.

Enable Plugin
^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables the Channel Export plugin on your Mattermost workspace.

**False**: Disables the Channel Export plugin on your Mattermost workspace.

Demo Plugin
~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Plugins > Demo Plugin**.

Enable Plugin
^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables the Demo plugin on your Mattermost workspace.

**False**: Disables the Demo plugin on your Mattermost workspace.

Channel Name
^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify the channel to use as part of the demo plugin. If the specified channel does not exist, the plugin creates the channel for you.

Username
^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify the user to use as part of the demo plugin. If the specified user does not exist, the plugin creates the user for you.

GIF commands
~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Plugins > GIF commands**.

This plugin is used to post GIFs from Gfycat, Giphy, or Tenor using slash commands.

Enable Plugin
^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables the GIF commands plugin on your Mattermost server.

**False**: Disables the GIF commands plugin on your Mattermost server.

Display the GIF as
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Display the GIF as an embedded image where the GIF can't be collapsed, or as a collapsible image preview where the full URL displays. 

.. note::
   `Link previews <https://docs.mattermost.com/configure/configuration-settings.html#enable-link-previews>`__ must be enabled in order to display GIF link previews. Mattermost deployments restricted to access behind a firewall must open port 443 to both ``https://api.gfycat.com/v1`` and ``https://gfycat.com/<id>`` (for all request types) for this feature to work.

GIF Provider
^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify the GIF provider as GIPHY, Tenor, or Gfycat.

.. note::
  Selecting GIPHY or Tenor requires an API Key for this feature to work. An API key is not required for Gfycat.

Giphy/Tenor API Key
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Configure your own API Key when specifying the GIF Provider as GIPHY or Tenor. An API key is not required for Gfycat. 

To get your own API key, see the `GIPHY Developers Quick Start <https://developers.giphy.com/docs/api/#quick-start-guide>`__ documentation, or the `Tenor Developer <https://tenor.com/developer/keyregistration>`__ documentation for details.

Content Rating (GIPHY & Tenor only)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Select an `MPAA-style content rating <https://en.wikipedia.org/wiki/Motion_Picture_Association_film_rating_system>`__ for GIFs from GIPHY or Tenor. Leave this field empty to disable content filtering.

Gfycat display style
^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify the display style for GIFs from Gfycat. See the `Gfycat Developer API <https://developers.gfycat.com/api/>`__ documentation for details.

GIPHY display style
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify the display style for GIFs from GIPHY. See the `GIPHY Developers Rendition Guide <https://developers.giphy.com/docs/optional-settings/>`__ for details.

Tenor display style
^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify the display style for GIFs from Tenor. See the `Tenor API <https://tenor.com/gifapi/documentation#responseobjects-gifformat>`__ documentation for details.

Language
^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify the language used to search GIFs from GIPHY. See the `GIPHY Developers Language Support <https://developers.giphy.com/docs/optional-settings/#language-support>`__ documentation for details.

Force GIF preview before posting (force /gifs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Enabled by default to prevent accidental posting of inappropriate GIFs from a provider that does not support content rating filtering.

**False**: Both ``/gif`` and ``/gifs`` slash commands are available for the GIF commands plugin on your Mattermost server.

Mattermost Boards
~~~~~~~~~~~~~~~~~

Mattermost Boards is an open source alternative to Trello, Notion, and Asana that's integrated from Mattermost v5.36. Boards is a project management tool that helps define, organize, track and manage work across teams, using a familiar kanban board view. See the `Mattermost Boards <https://docs.mattermost.com/guides/boards.html>`__ product documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Mattermost Boards**.

Enable Plugin
^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables the Mattermost Boards plugin on your Mattermost workspace.

**False**: Disables the Mattermost Boards plugin on your Mattermost workspace.

Mattermost Playbooks
~~~~~~~~~~~~~~~~~~~~

Mattermost Playbooks is an open source, self-hosted collaboration tool for teams. Each playbook represents a recurring outcome or specific goal that your teams collaborate on to achieve, such as service outage recovery or customer onboarding. Teams run a playbook every time they want to orchestrate people, tools, and data to achieve that outcome as quickly as possible while providing visibility to stakeholders. Playbooks also allow teams to incorporate learnings from the retrospective to tweak and improve the playbook with every iteration. See the `Mattermost Playbooks <https://docs.mattermost.com/guides/playbooks.html>`__ documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Playbooks**.

Enable Plugin
^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables the Mattermost Playbooks plugin on your Mattermost workspace.

**False**: Disables the Mattermost Playbooks plugin on your Mattermost workspace.

Enabled Teams
^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Enable Playbooks for all Mattermost teams, or for only selected teams.

Enable Experimental Features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables experimental Playbooks features on your Mattermost workspace.

**False**: Disables experimental Playbooks features on your Mattermost workspace.

User Satisfaction Surveys
~~~~~~~~~~~~~~~~~~~~~~~~~

This plugin enables Mattermost to send user satisfaction surveys to gather feedback and improve product quality directly from your Mattermost users. Please refer to the `Mattermost Privacy Policy <https://mattermost.com/privacy-policy/>`__ for more information on the collection and use of information received through Mattermost services.

Access the following configuration settings in the System Console by going to **Plugins > User Satisfaction Surveys**.

Enable Plugin
^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables the Mattermost Playbooks plugin on your Mattermost workspace.

**False**: Disables the Mattermost Playbooks plugin on your Mattermost workspace.

Enable User Satisfaction Survey
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: A user satisfaction survey will be sent out to all users on a quarterly basis. The survey results will be used by Mattermost, Inc. to improve the quality and user experience of the product. Please refer to the `Mattermost Privacy Policy <https://mattermost.com/privacy-policy/>`__ for more information on the collection and use of information received through Mattermost services.

**False**: User satisfaction surveys are disabled. 

Zoom
~~~~

This plugin allows team members to initiate a Zoom meeting with a single click. All participants in a channel can easily join the Zoom meeting and the shared link is updated when the meeting is over. See the `Zoom Conferencing Plugin <https://mattermost.gitbook.io/plugin-zoom/>`__ product documentation for details.

.. note::
  To set up this plugin, you need to create a Zoom App using a Zoom Administrator account. See the `Zoom Configuration <https://mattermost.gitbook.io/plugin-zoom/installation/zoom-configuration>`__ documentation for details. 

Access the following configuration settings in the System Console by going to **Plugins > Zoom**.

Enable Plugin
^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables the Zoom plugin on your Mattermost server.

**False**: Disables the Zoom plugin on your Mattermost server.

Zoom URL
^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify the URL for a self-hosted private cloud or on-premise Zoom server. For example, ``https://yourzoom.com``. Leave blank if you're using Zoom's vendor-hosted SaaS service.

Zoom API URL
^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify the API URL for a self-hosted private cloud or on-premise Zoom server. For example, ``https://api.yourzoom.com/v2``. Leave blank if you're using Zoom's vendor-hosted SaaS service.

Enable OAuth
^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: OAuth will be used as the authentication means with Zoom.

**False**: JWT will be used as the authentication means with Zoom.

.. note::

  If you are currently using a JWT Zoom application and switch to OAuth, all users will need to connect their Zoom account using OAuth the next time they try to start a meeting. See the `Zoom Configuration <https://mattermost.gitbook.io/plugin-zoom/installation/zoom-configuration>`__ documentation for details.

OAuth by Account Level App (Beta)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Only an account administrator has to log in. The rest of the users will use their e-mail to log in.

**False**: All users must use their e-mail to log in.

Zoom OAuth Client ID
^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify the Client ID for the OAuth app registered with Zoom. Leave blank if not using OAuth.

Zoom OAuth Client Secret
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify the Client Secret for the OAuth app registered with Zoom. Leave blank if not using OAuth.

At Rest Token Encryption Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Generate an AES encryption key for Zoom OAuth Token used to encrypt stored access tokens by selecting ``Regenerate``. Regenerating the key invalidates your existing Zoom OAuth.

API Key
^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify the API Key generated by Zoom used to create meetings and pull user data.

API Secret
^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Specify the API Secret generated by Zoom for your API key.

Webhook Secret
^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Generate a secret for the webhook URL endpoint used to authenticate the webhook to Mattermost. Regenerating the secret invalidates your existing Zoom plugin.

Integrations
-------------

Settings to configure webhooks, slash commands, and external integration services.

Integration Management
~~~~~~~~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Integrations > Integration Management**.

Enable Incoming Webhooks
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Developers building integrations can create webhook URLs for Public channels and Private channels. Please see our `documentation page <https://docs.mattermost.com/developer/webhooks-incoming.html>`__ to learn about creating webhooks, viewing samples, and letting community know about integrations you've built.

**True**: Incoming webhooks are allowed. To manage incoming webhooks, select **Integrations** from the Mattermost Product menu. The webhook URLs created can be used by external applications to create posts in any Public or Private channels that you have access to.

**False**: The **Integrations > Incoming Webhooks** section of the Mattermost Product menu is hidden and all incoming webhooks are disabled.

.. important::
   Security note: By enabling this feature, users may be able to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`__ by attempting to impersonate other users. To combat these attacks, a BOT tag appears next to all posts from a webhook. Enable at your own risk.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableIncomingWebhooks": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

Enable Outgoing Webhooks
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Developers building integrations can create webhook tokens for Public channels. Trigger words are used to fire new message events to external integrations. For security reasons, outgoing webhooks are only available in Public channels. Please see our `documentation page <https://docs.mattermost.com/developer/webhooks-outgoing.html>`__ to learn about creating webhooks and viewing samples.

**True**: Outgoing webhooks will be allowed. To manage outgoing webhooks, select **Integrations** from the Mattermost Product menu.

**False**: The **Integrations > Outgoing Webhooks** of the Mattermost Product menu is hidden and all outgoing webhooks are disabled.

.. important:: 
   Security note: By enabling this feature, users may be able to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`__ by attempting to impersonate other users. To combat these attacks, a BOT tag appears next to all posts from a webhook. Enable at your own risk.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOutgoingWebhooks": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

Enable Custom Slash Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Slash commands send events to external integrations that send a response back to Mattermost.

**True**: Allow users to create custom slash commands from **Main Menu > Integrations > Commands**.

**False**: Slash commands are hidden in the **Integrations** user interface.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCommands": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

Enable OAuth 2.0 Service Provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Mattermost acts as an OAuth 2.0 service provider allowing Mattermost to authorize API requests from external applications.

**False**: Mattermost does not function as an OAuth 2.0 service provider.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOAuthServiceProvider": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

Enable integrations to override usernames
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Webhooks, slash commands, OAuth 2.0 apps, and other integrations such as `Zapier <https://docs.mattermost.com/integrations/zapier.html>`__, will be allowed to change the username they are posting as. If no username is present, the username for the post is the same as it would be for a setting of ``False``.

**False**: Custom slash commands can only post as the username of the user who used the slash command. OAuth 2.0 apps can only post as the username of the user who set up the integration. For incoming webhooks and outgoing webhooks, the username is "webhook". See https://developers.mattermost.com/integrate/other-integrations/ for more details.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostUsernameOverride": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

Enable integrations to override profile picture icons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Webhooks, slash commands, and other integrations, such as `Zapier <https://docs.mattermost.com/integrations/zapier.html>`__, will be allowed to change the profile picture they post with.

**False**: Webhooks, slash commands, and OAuth 2.0 apps can only post with the profile picture of the account they were set up with. See https://developers.mattermost.com/integrate/other-integrations/ for more details.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostIconOverride": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Enable Personal Access Tokens
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Users can create `personal access tokens <https://developers.mattermost.com/integrate/admin-guide/admin-personal-access-token/>`__ for integrations in **Profile > Security**. They can be used to authenticate against the API and give full access to the account.

To manage who can create personal access tokens or to search users by token ID, go to the **System Console > Users** page.

**False**: Personal access tokens are disabled on the server.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserAccessTokens": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Bot Accounts
~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Integrations > Bot Accounts**.

Enable Bot Account Creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Users can create bot accounts for integrations in **Integrations > Bot Accounts**. Bot accounts are similar to user accounts except they cannot be used to log in. See `documentation <https://developers.mattermost.com/integrate/admin-guide/admin-bot-accounts/>`__ to learn more.

**False**: Bot accounts cannot be created through the user interface or the RESTful API. Plugins can still create and manage bot accounts.

+----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableBotAccountCreation": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------+

Disable bot accounts when owner is deactivated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: When a user is deactivated, disables all bot accounts managed by the user. To re-enable bot accounts, go to **Integrations > Bot Accounts**.

**False**: When a user is deactivated, all bot accounts managed by the user remain active.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DisableBotsWhenOwnerIsDeactivated": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------+

GIF (Beta)
~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Integrations > GIF (Beta)**.

Enable GIF Picker
^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Allow users to select GIFs from the emoji picker via a Gfycat integration.

**False**: GIFs cannot be selected in the emoji picker.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableGifPicker": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

.. note::
   `Link previews <https://docs.mattermost.com/configure/configuration-settings.html#enable-link-previews>`__ must be enabled in order to display GIF link previews. Mattermost deployments restricted to access behind a firewall must open port 443 to both https://api.gfycat.com/v1 and https://gfycat.com/<id> (for all request types) for this feature to work.

Gfycat API Key
^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

When blank, uses the default API key provided by Gfycat. Alternatively, a unique API key can be requested at https://developers.gfycat.com/signup/#/. Enter the client ID you receive via email to this field.

+-----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GfycatApiKey": "2_KtH_W5"`` with string input.   |
+-----------------------------------------------------------------------------------------------+

Gfycat API Secret
^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

The API secret generated by Gfycat for your API key. When blank, uses the default API secret provided by Gfycat.

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GfycatApiSecret": "3wLVZPiswc3DnaiaFoLkDvB4X0IV6CpMkj4tf2inJRsBY6-FnkT08zGmppWFgeof"`` with string input.  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

CORS
~~~~~

Access the following configuration settings in the System Console by going to **Integrations > CORS**.

Enable cross-origin requests from
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Enable HTTP cross-origin requests from specific domains separated by spaces. Type ``*`` to allow CORS from any domain or leave it blank to disable it.

.. note::
 Please make sure you have entered your Site URL before enabling this setting to prevent losing access to the System Console after saving. If you experience lost access to the System Console after changing this setting, you can set your `Site URL <https://docs.mattermost.com/configure/configuration-settings.html#site-url>`__ through the ``config.json`` file.

+--------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowCorsFrom": ""`` with string input. |
+--------------------------------------------------------------------------------------+

CORS Exposed Headers
^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Whitelist of headers that will be accessible to the requester.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CorsExposedHeaders": ""`` with string input. |
+-------------------------------------------------------------------------------------------+

CORS Allow Credentials
^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Requests that pass validation will include the ``Access-Control-Allow-Credentials`` header.

**False**: Requests won't include the ``Access-Control-Allow-Credentials`` header.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CorsAllowCredentials": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

CORS Debug
^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Prints messages to the logs to help when developing an integration that uses CORS. These messages will include the structured key value pair ``"source": "cors"``.

**False**: Debug messages not printed to the logs.

+-------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CorsDebug": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------+

Compliance
------------

Data Retention Policies
~~~~~~~~~~~~~~~~~~~~~~~

Changes to properties in this section require a server restart before taking effect.

.. warning:: 
   Once a message or a file is deleted, the action is irreversible. Please be careful when setting up a custom data retention policy.

Access the following configuration settings in the System Console by going to **Compliance > Data Retention Policies**.


Global Retention Policy for Messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Set how long Mattermost keeps messages across all teams and channels. Doesn't apply to custom retention policies. Requires the `global retention policy for messages <https://docs.mattermost.com/configure/configuration-settings.html#enable-global-retention-policy-for-messages>`__ configuration setting to be set to ``true``.

By default, messages are kept forever. If **Days** or **Years** is chosen, set how many days or years messages are kept in Mattermost. Messages older than the duration you set will be deleted nightly. The minimum time is one day.

+-------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MessageRetentionDays": 365`` with numerical input. |
+-------------------------------------------------------------------------------------------------+

Global Retention Policy for Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Set how long Mattermost keeps files across all teams and channels. Doesn't apply to custom retention policies. Requires the `global retention policy for files <https://docs.mattermost.com/configure/configuration-settings.html#enable-global-retention-policy-for-files>`__ configuration setting to be set to ``true``.

By default, messages are kept forever. If **Days** or **Years** is chosen, set how many days or years files are kept in Mattermost. Files older than the duration you set will be deleted nightly. The minimum time is one day.

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileRetentionDays": 365`` with numerical input. |
+----------------------------------------------------------------------------------------------+

Custom retention policy
^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Set how long Mattermost keeps messages and files across specific teams and channels by specifying a name for the custom retention policy, setting a duration value, specifying the teams and channels that will follow this policy.

Data Deletion Time
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Set the start time of the daily scheduled data retention job. Choose a time when fewer people are using your system. Must be a 24-hour time stamp in the form ``HH:MM``.

This setting is based on the local time of the server.

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DeletionJobStartTime": "02:00"`` with 24-hour timestamp input in the form ``"HH:MM"``. |
+-------------------------------------------------------------------------------------------------------------------------------------+

Run Deletion Job Now
^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Start a Data Retention deletion job immediately. You can monitor the status of the job in the data deletion job table within the Policy Log section.

Compliance Export
~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Compliance > Compliance Export**.

Enable Compliance Export
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available as an add-on to legacy Enterprise Edition E20*

**True**: Mattermost will generate a compliance export file that contains all messages that were posted in the last 24 hours. The export task is scheduled to run once per day. See the `documentation to learn more <https://docs.mattermost.com/comply/compliance-export.html>`__.

**False**: Mattermost doesn't generate a compliance export file.

+----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableExport": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------+

Compliance Export Time
^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available as an add-on to legacy Enterprise Edition E20*

Set the start time of the daily scheduled compliance export job. Choose a time when fewer people are using your system. Must be a 24-hour time stamp in the form ``HH:MM``.

This setting is based on the local time of the server.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DailyRunTime": 01:00`` with 24-hour timestamp input in the form ``"HH:MM"``. |
+---------------------------------------------------------------------------------------------------------------------------+

Export File Format
^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available as an add-on to legacy Enterprise Edition E20*

File format of the compliance export. Corresponds to the system that you want to import the data into.

Currently supported formats are CSV, Actiance XML, and Global Relay EML.

If Global Relay is chosen, the following options will be presented:

Global Relay Customer Account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available as an add-on to legacy Enterprise Edition E20*

Type of Global Relay customer account your organization has, either ``A9/Type 9`` or ``A10/Type 10``.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CustomerType": "A9/Type 9"`` with options ``"A9/Type 9"`` and ``"A10/Type 10"``. |
+-------------------------------------------------------------------------------------------------------------------------------+

Global Relay SMTP Username
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available as an add-on to legacy Enterprise Edition E20*

The username for authenticating to the Global Relay SMTP server.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SmtpUsername": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Global Relay SMTP Password
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available as an add-on to legacy Enterprise Edition E20*

The password associated with the Global Relay SMTP username.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SmtpPassword": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Global Relay Email Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available as an add-on to legacy Enterprise Edition E20*

The email address your Global Relay server monitors for incoming compliance exports.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EmailAddress": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Run Compliance Export Job Now
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available as an add-on to legacy Enterprise Edition E20*

This button initiates a compliance export job immediately. You can monitor the status of the job in the compliance export job table.

Compliance Monitoring
~~~~~~~~~~~~~~~~~~~~~~

Settings used to enable and configure Mattermost compliance reports. 

Access the following configuration settings in the System Console by going to **Compliance > Compliance Monitoring**.

Enable Compliance Reporting
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available as an add-on to legacy Enterprise Edition E20*

**True**: Compliance reporting is enabled in Mattermost.

**False**: Compliance reporting is disabled.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Compliance Report Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available as an add-on to legacy Enterprise Edition E20*

Sets the directory where compliance reports are written.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Directory": "./data/"`` with string input. |
+-----------------------------------------------------------------------------------------+

Enable Daily Report
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available as an add-on to legacy Enterprise Edition E20*

**True**: Mattermost generates a daily compliance report.

**False**: Daily reports are not generated.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableDaily": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+

Batch Size
^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available as an add-on to legacy Enterprise Edition E20*

Set the size of the batches in which posts will be read from the database to generate the compliance report. This setting is currently not available in the System Console and can only be set in ``config.json``.

+------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BatchSize": 30000`` with default value ``30000``. |
+------------------------------------------------------------------------------------------------+

Custom Terms of Service
~~~~~~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Compliance > Custom Terms of Service**.

Enable Custom Terms of Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available as an add-on to legacy Enterprise Edition E20*

.. note::
  This configuration setting can only be modified using the System Console user interface.

**True**: New users must accept the Terms of Service before accessing any Mattermost teams on desktop, web, or mobile. Existing users must accept them after login or a page refresh. To update the Terms of Service link displayed in account creation and login pages, go to **System Console > Legal and Support > Terms of Service Link**.

**False**: During account creation or login, users can review Terms of Service by accessing the link configured via **System Console > Legal and Support > Terms of Service link**.

Custom Terms of Service Text
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available as an add-on to legacy Enterprise Edition E20*

Text that will appear in your custom Terms of Service. Supports Markdown-formatted text.

Re-Acceptance Period
^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available as an add-on to legacy Enterprise Edition E20*

The number of days before Terms of Service acceptance expires, and the terms must be re-accepted.

Defaults to 365 days. 0 indicates the terms do not expire.

Experimental
-------------

There are a number of settings considered "experimental" that are configurable from the System Console. These may be replaced or removed in a future release.

AD/LDAP Settings
~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Experimental > Features**.

AD/LDAP Login Button Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Specify the color of the AD/LDAP login button for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonColor": ""`` with string input.                                       |
+-------------------------------------------------------------------------------------------------------------------------------+

AD/LDAP Login Button Border Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Specify the color of the AD/LDAP login button border for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonBorderColor": ""`` with string input.                                 |
+-------------------------------------------------------------------------------------------------------------------------------+

AD/LDAP Login Button Text Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Specify the color of the AD/LDAP login button text for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonTextColor": ""`` with string input.                                   |
+-------------------------------------------------------------------------------------------------------------------------------+

Allow Authentication Transfer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20*

**True**: Users can change their login method to any that is enabled on the server, either via **Profile > Security** or the APIs.

**False**: Users cannot change their login method, regardless of which authentication options are enabled.

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalEnableAuthenticationTransfer": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------------+

Link Metadata Timeout
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Adds a configurable timeout for requests made to return link metadata. If the metadata is not returned before this timeout expires, the message will post without requiring metadata. This timeout covers the failure cases of broken URLs and bad content types on slow network connections.

+---------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LinkMetadataTimeoutMilliseconds": 5000`` with numerical input.                     |
+---------------------------------------------------------------------------------------------------------------------------------+

Bleve Settings
~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Experimental > Bleve**.

Enable Bleve Indexing
^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: The indexing of new posts occurs automatically. Search queries will not use bleve search until `Enable Bleve for search queries <https://docs.mattermost.com/configure/configuration-settings.html#enable-bleve-for-search-queries>`__ is enabled.

**False**: The indexing of new posts does not occur automatically.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableIndexing": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

Index Directory
^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Directory path to use for storing bleve indexes. 

.. tip::
   
   The bleve index directory path isn't required to exist within the ``mattermost`` directory. When it exists outside of the ``mattermost`` directory, no  additional steps are needed to preserve or reindex these files as part of a Mattermost upgrade. See our `Upgrading Mattermost Server <https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html>`__ documentation for details. 

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IndexDir": ""`` with string input.                           |
+-----------------------------------------------------------------------------------------------------------+

Bulk Index Now
^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Select **Index Now** to index all users, channels, and posts in the database from oldest to newest. Bleve is available during indexing, but search results may be incomplete until the indexing job is complete.

You can configure the maximum time window used for a batch of posts being indexed. See the `Bulk Indexing Time Window Seconds <https://docs.mattermost.com/configure/configuration-settings.html#bulk-indexing-time-window-seconds>`__ documentation for details.

Purge Indexes
^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Select **Purge Index** to remove the contents of the Bleve index directory. Search results may be incomplete until a bulk index of the existing database is rebuilt.

Enable Bleve for search queries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Search queries will use bleve search.

**False**: Search queries will not use bleve search.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSearching": false`` with options ``true`` and ``false``.  |
+--------------------------------------------------------------------------------------------------------------+

Enable Bleve for autocomplete queries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: Autocomplete queries will use bleve search.

**False**: Autocomplete queries will not use bleve search.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAutocomplete": false`` with options ``true`` and ``false``.  |
+-----------------------------------------------------------------------------------------------------------------+

Email Settings
~~~~~~~~~~~~~~

Email Batching Buffer Size
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Specify the maximum number of notifications batched into a single email.

+--------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``EmailBatchingBufferSize": 256`` with numerical input.                        |
+--------------------------------------------------------------------------------------------------------------------------+

Email Batching Interval
^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Specify the maximum frequency, in seconds, which the batching job checks for new notifications. Longer batching intervals will increase performance.

+-----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``EmailBatchingInterval": 30`` with numerical input.                        |
+-----------------------------------------------------------------------------------------------------------------------+

Email Login Button Color
^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Specify the color of the email login button for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonColor": ""`` with string input.                                       |
+-------------------------------------------------------------------------------------------------------------------------------+

Email Login Button Border Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Specify the color of the email login button border for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonBorderColor": ""`` with string input.                                 |
+-------------------------------------------------------------------------------------------------------------------------------+

Email Login Button Text Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Specify the color of the email login button text for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonTextColor": ""`` with string input.                                   |
+-------------------------------------------------------------------------------------------------------------------------------+

Enable Account Deactivation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Ability for users to deactivate their own account from **Settings > Advanced**. If a user deactivates their own account, they will get an email notification confirming they were deactivated.

**False**: Ability for users to deactivate their own account is disabled.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserDeactivation": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Enable Automatic Replies
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Users can enable Automatic Replies in **Settings > Notifications**. Users set a custom message that will be automatically sent in response to Direct Messages.

**False**: Disables the Automatic Direct Message Replies feature and hides it from **Settings**.

+--------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalEnableAutomaticReplies": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------------------+

Enable Channel Viewed WebSocket Messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

This setting determines whether ``channel_viewed WebSocket`` events are sent, which synchronize unread notifications across clients and devices. Disabling the setting in larger deployments may improve server performance.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableChannelViewedMessages": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

Enable Client-Side Certification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Enables client-side certification for your Mattermost server. See `the documentation <https://docs.mattermost.com/onboard/certificate-based-authentication.html>`__ to learn more.

**False**: Client-side certification is disabled.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ClientSideCertEnable": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

Client-Side Certification Login Method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Used in combination with the ``ClientSideCertEnable`` configuration setting.

**Primary**: After the client side certificate is verified, user's email is retrieved from the certificate and is used to log in without a password.

**Secondary**: After the client side certificate is verified, user's email is retrieved from the certificate and matched against the one supplied by the user. If they match, the user logs in with regular email/password credentials.

+----------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ClientSideCertCheck": "secondary"`` with options ``"primary"`` and ``"secondary"``. |
+----------------------------------------------------------------------------------------------------------------------------------+

Enable Default Channel Leave/Join System Messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

This setting determines whether team leave/join system messages are posted in the default ``town-square`` channel.

**True**: Enables leave/join system messages in the default ``town-square`` channel.

**False**: Disables leave/join messages from the default ``town-square`` channel. These system messages won't be added to the database either.

+----------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalEnableDefaultChannelLeaveJoinMessages": true`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------------------------------+

Enable Hardened Mode (Experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Enables a hardened mode for Mattermost that makes user experience trade-offs in the interest of security.

**False**: Disables hardened mode.

Changes made when hardened mode is enabled:

- Failed login returns a generic error message instead of a specific message for username and password.
- If `multi-factor authentication (MFA) <https://docs.mattermost.com/onboard/multi-factor-authentication.html>`__ is enabled, the route to check if a user has MFA enabled always returns true. This causes the MFA input screen to appear even if the user does not have MFA enabled. The user may enter any value to pass the screen. Note that hardened mode does not affect user experience when MFA is enforced.
- Password reset does not inform the user that they can not reset their SSO account through Mattermost and instead claims to have sent the password reset email.
- Mattermost sanitizes all 500 errors before returned to the client. Use the supplied ``request_id`` to match user facing errors with the server logs.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalEnableHardenedMode": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------------+

Enable AD/LDAP Group Sync
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Enables AD/LDAP Group Sync configurable under **User Management > Groups**.

**False**: Disables AD/LDAP Group Sync and removes **User Management > Groups** from the System Console.

For more information on AD/LDAP Group Sync, please see the `AD/LDAP Group Sync documentation <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`__.

+-----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalLdapGroupSync": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------------+

Enable Preview Features
^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Preview features can be enabled from **Settings > Advanced > Preview Pre-release features**.

**False**: Disables and hides preview features from **Settings > Advanced > Preview Pre-release features**.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePreviewFeatures": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

Enable Theme Selection
^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20*

**True**: Enables the **Display > Theme** tab in **Settings** so users can select their theme.

**False**: Users cannot select a different theme. The **Display > Theme** tab is hidden in **Settings**.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableThemeSelection": true`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------+

Allow Custom Themes
^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20*

**True**: Enables the **Display > Theme > Custom Theme** section in **Settings**.

**False**: Users cannot use a custom theme. The **Display > Theme > Custom Theme** section is hidden in **Settings**.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowCustomThemes": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

Default Theme
^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20*

Set a default theme that applies to all new users on the system.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DefaultTheme": "default"`` with options ``"default"``, ``"organization"``, ``"mattermostDark"``, and ``"windows10"``. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Tutorial (Experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Users are prompted with a tutorial when they open Mattermost for the first time after account creation.

**False**: The tutorial is disabled. Users are placed in Town Square when they open Mattermost for the first time after account creation.

+--------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableTutorial": true`` with options ``true`` and ``false``.                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+

Enable Onboarding 
^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

**True**: New Mattermost users are shown key tasks to complete as part of initial onboarding.

**False**: User onboarding tasks are disabled. Users are placed in Town Square when they open Mattermost for the first time after account creation.

+--------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOnboarding": true`` with options ``true`` and ``false``.                                |
+--------------------------------------------------------------------------------------------------------------------------------------------+

Enable User Typing Messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

This setting determines whether "user is typing..." messages are displayed below the message box. Disabling the setting in larger deployments may improve server performance.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserTypingMessages": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------------+

Time Between User Typing Updates (User Typing Timeout)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

This setting defines how frequently "user is typing..." messages are updated, measured in milliseconds.

+----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TimeBetweenUserTypingUpdatesMilliseconds": 5000`` with numerical input. |
+----------------------------------------------------------------------------------------------------------------------+

Primary Team (Experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

The primary team of which users on the server are members. When a primary team is set, the options to join other teams or leave the primary team are disabled.

If the team URL of the primary team is https://example.mattermost.com/myteam/, then set the value to ``myteam`` in ``config.json``.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalPrimaryTeam": ""`` with string input.                  |
+-----------------------------------------------------------------------------------------------------------------+

SAML Settings
~~~~~~~~~~~~~

SAML Login Button Color
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Specify the color of the SAML login button for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonColor": ""`` with string input.                                       |
+-------------------------------------------------------------------------------------------------------------------------------+

SAML Login Button Border Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Specify the color of the SAML login button border for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonBorderColor": ""`` with string input.                                 |
+-------------------------------------------------------------------------------------------------------------------------------+

SAML Login Button Text Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Specify the color of the SAML login button text for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonTextColor": ""`` with string input.                                   |
+-------------------------------------------------------------------------------------------------------------------------------+

Use Channel Name in Email Notifications (Experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

**True**: Channel and team name appears in email notification subject lines. Useful for servers using only one team.

**False**: Only team name appears in email notification subject line.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UseChannelInEmailNotifications": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------------+

User Status Away Timeout
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

This setting defines the number of seconds after which the user's status indicator changes to "Away", when they are away from Mattermost.

+--------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserStatusAwayTimeout": 300`` with numerical input. |
+--------------------------------------------------------------------------------------------------+

Enable Shared Channels
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

Shared channels enables the ability to establish secure connections between Mattermost instances, and invite secured connections to shared channels where secure connections can participate as they would in any public and private channel. Enabling shared channels functionality requires a server restart. 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's two ``config.json`` settings include ``"ExperimentalSettings:EnableSharedChannels": false`` with options ``true`` or ``false``, and ``"ExperimentalSettings:EnableRemoteClusterService": false`` with options ``true`` or ``false``. |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   - Both configuration settings must be enabled in order to share channels with secure connections. Only the **Enable Shared Channels** configuration option is available through the System Console.
   - System Admins for Cloud deployments can submit a request to have the ``EnableRemoteClusterService`` configuration setting enabled in their Cloud instance.

Enable Apps Bar
^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

This setting enables the Apps Bar and moves all Mattermost integration icons from the channel header to a vertical pane on the far right side of the screen. 

.. note::
  
  Integrations currently registered to the channel header will move to the Apps Bar automatically; however, we strongly encourage Mattermost integrators to update their integrations to provide the best user experience. See the `channel header plugin changes <https://forum.mattermost.com/t/channel-header-plugin-changes/13551>`__ user forum discussion for details on how to register integrations with the Apps Bar.

**True**: All integration icons in the channel header move to the Apps Bar with the exception of the calls beta feature.

**False**: All integration icons in the channel header display in the channel header.

+----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAppBar": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------+

Settings configurable only in ``config.json``
----------------------------------------------

There are a number of settings customizable in ``config.json`` which are unavailable in the System Console and require updating from the file itself.

Data Retention Policies
~~~~~~~~~~~~~~~~~~~~~~~

Enable Global Retention Policy for Messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Messages can be deleted as part of a scheduled data retention job. This doesn't apply to custom retention policies.

**False**: Messages can't be deleted as part of a scheduled data retention job.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableMessageDeletion": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

Enable Global Retention Policy for Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

**True**: Files can be deleted as part of a scheduled data retention job. This doesn't apply to custom retention policies.

**False**: Files can't be deleted as part of a scheduled data retention job.

+----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableFileDeletion": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------+

Email Settings
~~~~~~~~~~~~~~

Disable Inactive Server Email Notifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

This configuration setting disables the ability to send inactivity email notifications to Mattermost System Admins.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableInactivityEmail": true`` with options ``true`` and ``false``.  |
+-------------------------------------------------------------------------------------------------------------------+

Service Settings
~~~~~~~~~~~~~~~~

Custom User Groups
^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

This configuration setting controls the ability for users to create custom user groups. This configuration setting is disabled by default.

+----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCustomGroups": true`` with options ``true`` and ``false``.  |
+----------------------------------------------------------------------------------------------------------------+

Developer Flags
^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

This configuration setting specifies a list of strings where each string is a flag used to set the content security policy (CSP) for the Mattermost Web App. Each flag must be in the format ``flag=true`` (e.g. ``unsafe-eval=true,unsafe-inline=true``). Not recommended for production environments.

The following values are currently supported:

- ``unsafe-eval``: Adds the ``unsafe-eval`` CSP directive to the root webapp, allowing increased debugging in developer environments.
- ``unsafe-inline``: Adds the ``unsafe-inline`` CSP directive to the root webapp, allowing increased debugging in developer environments.

This configuration setting is disabled by default and requires `developer mode <https://docs.mattermost.com/configure/configuration-settings.html#enable-developer-mode>`__ to be enabled. 

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DeveloperFlags": ""`` with string input.  |
+----------------------------------------------------------------------------------------+

Enable Post Search
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

If this setting is enabled, users can search messages. Disabling search can result in a performance increase, but users get an error message when they attempt to use the search box.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostSearch": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

Enable File Search
^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

This configuration setting enables users to search documents attached to messages by filename. To enable users to search documents by their content, you must also enable the ``ExtractContent`` configuration setting. See our `Enable Document Search by Content <https://docs.mattermost.com/configure/configuration-settings.html#enable-document-search-by-content>`__ documentation for details. Document content search is available in Mattermost Server from v5.35, with mobile support coming soon. 

**True**: Supported document types are searchable by their filename. 

**False**: File-based searches are disabled.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableFileSearch": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

Enable User Status Updates
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

Turn status updates off to improve performance. When status updates are off, users appear online only for brief periods when posting a message, and only to members of the channel in which the message is posted.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserStatuses": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

WebSocket Secure Port
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``. Changes to this setting require a server restart before taking effect.

(Optional) This setting defines the port on which the secured WebSocket will listen using the ``wss`` protocol. Defaults to ``443``. When the client attempts to make a WebSocket connection it first checks to see if the page is loaded with HTTPS. If so, it will use the secure WebSocket connection. If not, it will use the unsecure WebSocket connection. IT IS HIGHLY RECOMMENDED PRODUCTION DEPLOYMENTS ONLY OPERATE UNDER HTTPS AND WSS.


+------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"WebsocketSecurePort": 443`` with numerical input. |
+------------------------------------------------------------------------------------------------+

WebSocket Port
^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``. Changes to this setting require a server restart before taking effect.

(Optional) This setting defines the port on which the unsecured WebSocket will listen using the ``ws`` protocol. Defaults to ``80``. When the client attempts to make a WebSocket connection it first checks to see if the page is loaded with HTTPS. If so, it will use the secure WebSocket connection. If not, it will use the unsecure WebSocket connection. IT IS HIGHLY RECOMMENDED PRODUCTION DEPLOYMENTS ONLY OPERATE UNDER HTTPS AND WSS.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``WebsocketPort": 80`` with numerical input. |
+----------------------------------------------------------------------------------------+

Enable API Team Deletion
^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: The ``api/v4/teams/{teamid}?permanent=true`` API endpoint can be called by Team and System Admins to permanently delete a team.

**False**: The API endpoint cannot be called. Note that ``api/v4/teams/{teamid}`` can still be used to soft delete a team.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAPITeamDeletion": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

Enable API User Deletion
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: The ``api/v4/users/{userid}?permanent=true`` API endpoint can be called by System Admins, or users with appropriate permissions, to permanently delete a user.

**False**: The API endpoint cannot be called. Note that ``api/v4/users/{userid}`` can still be used to soft delete a user.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAPIUserDeletion": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

Enable API Channel Deletion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: The ``api/v4/channels/{channelid}?permanent=true`` API endpoint can be called by System Admins, or users with appropriate permissions, to permanently delete a channel.

**False**: The API endpoint cannot be called. Note that ``api/v4/channels/{channelid}`` can still be used to soft delete a channel.

+----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAPIChannelDeletion": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------+

Enable OpenTracing
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: A Jaeger client is instantiated and is used to trace each HTTP request as it goes through App and Store layers. Context is added to App and Store and is passed down the layer chain to create OpenTracing 'spans'.

By default, in order to avoid leaking sensitive information, no method parameters are reported to OpenTracing. Only the name of the method is reported.

**False**: OpenTracing is not enabled.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOpenTracing": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Import Settings Default Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

The directory where the imported files are stored. The path is relative to the ``FileSettings`` directory. By default, imports are stored under ``./data/import``.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting under the ``ImportSettings`` section is ``Directory: ./import`` with string input. |
+---------------------------------------------------------------------------------------------------------------------------+

Import Settings Default Retention Days
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

The number of days to retain the imported files before deleting them.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting under the ``ImportSettings`` section is ``RetentionDays: 30`` with numerical input. |
+----------------------------------------------------------------------------------------------------------------------------+

Export Settings Default Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

The directory where the exported files are stored. The path is relative to the ``FileSettings`` directory. By default, exports are stored under ``./data/export``.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting under the ``ExportSettings`` section is ``Directory: ./export`` with string input. |
+---------------------------------------------------------------------------------------------------------------------------+

Export Settings Default Retention Days
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

The number of days to retain the exported files before deleting them.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting under the ``ExportSettings`` section is ``RetentionDays: 30`` with numerical input. |
+----------------------------------------------------------------------------------------------------------------------------+

Enable Local Mode
^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables local mode for mmctl.

**False**: Prevents local mode for mmctl.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableLocalMode": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

Enable Local Mode Socket Location
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

The path for the socket that the server will create for mmctl to connect and communicate through local mode. If the default value for this key is changed, you will need to point mmctl to the new socket path when in local mode, using the ``--local-socket-path /new/path/to/socket`` flag in addition to the ``--local`` flag.

If nothing is specified, the default path that both the server and mmctl assumes is ``/var/tmp/mattermost_local.socket``.

+--------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LocalModeSocketLocation": "/var/tmp/mattermost_local.socket"`` with string input. |
+--------------------------------------------------------------------------------------------------------------------------------+

Scoping IDP Provider Id
^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Allows an authenticated user to skip the initial login page of their federated Azure AD server, and only require a password to log in.

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ScopingIDPProviderId": ""`` with string input. |
+---------------------------------------------------------------------------------------------+

Scoping IDP Name
^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Adds the name associated with a user's Scoping Identity Provider ID.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ScopingIDPName": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Global Relay SMTP Server Timeout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

*Available as an add-on to legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

The number of seconds that can elapse before the connection attempt to the SMTP server is abandoned. The default value is 1800 seconds. This setting is currently not available in the System Console and can only be set in ``config.json``.

+-----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GlobalRelaySettings.SMTPServerTimeout": "1800"`` with numerical input.   |
+-----------------------------------------------------------------------------------------------------------------------+

Batch Size
^^^^^^^^^^^

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Determines how many new posts are batched together to a compliance export file.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BatchSize": 10000`` with numerical input. |
+----------------------------------------------------------------------------------------+

App Custom URL Schemes
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

Define valid custom URL schemes for redirect links provided by custom-built mobile Mattermost apps. This ensures users are redirected to the custom-built mobile app and not Mattermost's mobile client. 

When configured, after OAuth or SAML user authentication is complete, custom URL schemes sent by mobile clients are validated to ensure they don't include default schemes such as ``http`` or ``https``. Mobile users are then redirected back to the mobile app using the custom scheme URL provided by the mobile client. We recommend that you update your mobile client values as well with valid custom URL schemes.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"NativeAppSettings.AppCustomURLSchemes"`` with an array of strings as input. For example: ``[custom-app://, some-app://]``.                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Colorize plain text console logs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: When logged events are output to the console as plain text, colorize log levels details.

**False**: Plain text log details aren't colorized in the console.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableColor": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+

Clean Up Old Database Jobs
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

Defines the threshold in hours beyond which older completed database jobs are removed. This setting applies to both MySQL and PostgreSQL databases, is disabled by default, and must be set to a value greater than or equal to ``0`` to be enabled.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"JobSettings.CleanupJobsThresholdDays": -1`` with numerical input.     |
+--------------------------------------------------------------------------------------------------------------------+

Clean Up Outdated Database Entries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting only applies to configuration in the database. It isn't available in the System Console and can be set via mmctl or changed in the database.

Defines the threshold in days beyond which outdated configurations are removed from the database. This setting applies to both MySQL and PostgreSQL databases.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"JobSettings.CleanupConfigThresholdDays": 30`` with numerical input.   |
+--------------------------------------------------------------------------------------------------------------------+

Image Settings
~~~~~~~~~~~~~~

Maximum Image Resolution
^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

Maximum image resolution size for message attachments in pixels. 

+--------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxImageResolution": 33177600`` with numerical input.     |
+--------------------------------------------------------------------------------------------------------+

File Settings
~~~~~~~~~~~~~~

Maximum Image Decoder Concurrency
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

Indicates how many images can be decoded concurrently at once. The default value of ``-1`` configures Mattermost to automatically use the number of CPUs present.

.. note::

  This configuration setting affects the total memory consumption of the server. The maximum memory of a single image is dictated by ``MaxImageResolution * 24 bytes`` Therefore, a good rule of thumb to follow is that ``MaxImageResolution* MaxImageDecoderConcurrency * 24`` should be less than the allocated memory for image decoding.

+--------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxImageDecoderConcurrency": "-1"`` with numerical input. |
+--------------------------------------------------------------------------------------------------------+

Initial Font
^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

Font used in auto-generated profile pics with colored backgrounds.

+-----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"InitialFont": "luximbi.ttf"`` with string input. |
+-----------------------------------------------------------------------------------------------+

Amazon S3 Signature V2
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

By default, Mattermost uses Signature V4 to sign API calls to AWS, but under some circumstances, V2 is required. For more information about when to use V2, see https://docs.aws.amazon.com/general/latest/gr/signature-version-2.html.

**True**: Use Signature Version 2 Signing Process.

**False**: Use Signature Version 4 Signing Process.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3SignV2": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

Amazon S3 Path
^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

Allows using the same S3 bucket for multiple deployments.

+------------------------------------------------------------------------------------------------------------+
| This feature’s ``config.json`` setting is ``"AmazonS3PathPrefix: ""`` with string input.                   |
+------------------------------------------------------------------------------------------------------------+

GitLab Settings
~~~~~~~~~~~~~~~

Scope
^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

*Not available in Cloud Starter*

This setting isn't available in the System Console and can only be set in ``config.json``.

Standard setting for OAuth to determine the scope of information shared with OAuth client. Not currently supported by GitLab OAuth.

+------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Scope": ""`` with string input. |
+------------------------------------------------------------------------------+

Google Settings
~~~~~~~~~~~~~~~

Scope
^^^^^^

.. include:: ../_static/badges/ent-pro-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Standard setting for OAuth to determine the scope of information shared with OAuth client. Recommended setting is ``profile email``.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Scope": "profile email"`` with string input. |
+-------------------------------------------------------------------------------------------+

Office 365 Settings
~~~~~~~~~~~~~~~~~~~~

Scope
^^^^^^

.. include:: ../_static/badges/ent-pro-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Standard setting for OAuth to determine the scope of information shared with OAuth client. Recommended setting is ``User.Read``.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Scope": "User.Read"`` with string input. |
+---------------------------------------------------------------------------------------+

Metrics Settings
~~~~~~~~~~~~~~~~~

Block Profile Rate
^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``. Changes to this setting require a server restart before taking effect.

Value that controls the `fraction of goroutine blocking events reported in the blocking profile <https://golang.org/pkg/runtime/#SetBlockProfileRate>`__.

The profiler aims to sample an average of one blocking event per rate nanoseconds spent blocked.

To include every blocking event in the profile, set the rate to ``1``. To turn off profiling entirely, set the rate to ``0``.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BlockProfileRate": 0`` with options ``0`` and ``1``. |
+---------------------------------------------------------------------------------------------------+

Plugin Settings
~~~~~~~~~~~~~~~

Signature Public Key Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

In addition to the Mattermost plugin signing key built into the server, each public key specified here is trusted to validate plugin signatures.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SignaturePublicKeyFiles": {}`` with string array input consisting of contents that are relative or absolute paths to signature files.              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Chimera OAuth Proxy URL
^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

Specify the `Chimera <https://github.com/mattermost/chimera>`__ URL used by Mattermost plugins to connect with pre-created OAuth applications.

+-------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ChimeraOAuthProxyUrl": {}`` with string input.                             |
+-------------------------------------------------------------------------------------------------------------------------+

Welcome Bot
^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

The settings for the WelcomeBot plugin aren't available in the System Console, and can only be set in ``config.json``.

Learn more `in our documentation <https://github.com/mattermost/mattermost-plugin-welcomebot/blob/master/README.md>`__.

Experimental Settings only in ``config.json``
---------------------------------------------

Audit settings
~~~~~~~~~~~~~~

The audit settings output audit records to syslog (local or remote server via TLS) and/or to a local file. Both are disabled by default. They can be enabled simultaneously.

Remote Clusters
^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Enable this setting to add, remove, and view remote clusters for shared channels. 

**True**: System Admins can manage remote clusters using the System Console.

**False**: Remote cluster management is disabled.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RemoteClusters": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

Syslog configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

Enable this setting to write audit records to a local or remote syslog, specifying the IP, port, user-generated fields, and certificate settings. 

**True**: Syslog output is enabled.

**False**: Syslog output is disabled.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SysLogEnabled": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------+

Syslog IP
^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

The IP address or domain of the syslog server. Use ``localhost`` for local syslog. 

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SysLogIP": "localhost"`` with string input consisting of an IP address or domain name. |
+-------------------------------------------------------------------------------------------------------------------------------------+

Syslog port
^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

The port that the syslog server is listening on. The default port is 6514. 

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SysLogPort": 6514`` with numeric input consisting of a port number. |
+------------------------------------------------------------------------------------------------------------------+

Syslog tag
^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

The syslog metadata tag field.

+-------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SysLogTag": ""`` with string input consisting of a user-defined tag field. |
+-------------------------------------------------------------------------------------------------------------------------+

Syslog cert
^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

This is the path to the syslog server certificate for TLS connections (``.crt`` or ``.pem``). 

+-----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SysLogCert": ""`` with string input consisting of the path to the certificate. |
+-----------------------------------------------------------------------------------------------------------------------------+

Syslog insecure
^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

This setting controls whether a client verifies the server's certificate chain and host name. If ``true``, TLS accepts any certificate presented by the server and any host name in that certificate. In this mode, TLS is susceptible to man-in-the-middle attacks. 

.. note:: 
   This should be used only for testing and not in a production environment.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SysLogInsecure": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

Syslog max queue size
^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

This setting determines how many audit records can be queued/buffered at any point in time when writing to syslog. The default is 1000 records. 
This setting can be left as default unless you are seeing audit write failures in the server log and need to adjust the number accordingly.

+------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SysLogMaxQueueSize": 1000`` with numerical input. |
+------------------------------------------------------------------------------------------------+

File configuration options
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

Enable this setting to write audit files locally, specifying size, backup interval, compression, maximum age to manage file rotation, and timestamps. 

**True**: File output is enabled.

**False**: File output is disabled.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileEnabled": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+

File name
^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

This is the path to the output file location. 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileName": ""`` with string input consisting of a user-defined path (e.g. ``/var/log/mattermost_audit.log``).                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

File max size MB
^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

This is the maximum size (measured in megabytes) that the file can grow before triggering rotation. The default setting is 100. 

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileMaxSizeMB": 100`` with numerical input. |
+------------------------------------------------------------------------------------------+

File max age days
^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

This is the maximum age in days a file can reach before triggering rotation. The default value is 0, indicating no limit on the age. 

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileMaxAgeDays": 0`` with numerical input. |
+-----------------------------------------------------------------------------------------+

File max backups
^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

This is the maximum number of rotated files kept; the oldest is deleted first. The default value is 0, indicating no limit on the number of backups. 

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileMaxBackups": 0`` with numerical input. |
+-----------------------------------------------------------------------------------------+

File compress
^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

When ``true``, rotated files are compressed using ``gzip``. 

+----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileCompress": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------+

File max queue size
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

This setting determines how many audit records can be queued/buffered at any point in time when writing to a file. The default is 1000 records. 
This setting can be left as default unless you are seeing audit write failures in the server log and need to adjust the number accordingly.

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileMaxQueueSize": 1000`` with numerical input. |
+----------------------------------------------------------------------------------------------+

Advanced Audit Logging Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Output logs to multiple targets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Send log records to multiple targets:

- Multiple local file targets
- Multiple syslogs
- Multiple TCP sockets

Allow any combination of local file, syslog, and TCP socket targets. 

File target supports rotation and compression triggered by size and/or duration. Syslog target supports local and remote syslog servers, with or without TLS transport. TCP socket target can be configured with an IP address or domain name, port, and optional TLS certificate.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``ExperimentalAuditSettings.AdvancedLoggingConfig`` which can contain a filespec to another config file, a database DSN, or JSON.   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Options are outlined in this text file: `Log Settings Options <https://github.com/mattermost/docs/files/5066579/Log.Settings.Options.txt>`__. Sample config: `Advanced Logging Options Sample.json.zip <https://github.com/mattermost/docs/files/5066597/Advanced.Logging.Options.Sample.json.zip>`__.

Service Settings
~~~~~~~~~~~~~~~~

Group Unread Channels (Experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

This setting applies to the new sidebar only. You must disable the `Enable Legacy Sidebar <https://docs.mattermost.com/configure/configuration-settings.html#enable-legacy-sidebar>`__ configuration setting to see and enable this functionality in the System Console. 

**Default Off**: Disables the unread channels sidebar section for all users by default. Users can enable it in **Settings > Sidebar > Group unread channels separately**.

**Default On**: Enables the unread channels sidebar section for all users by default. Users can disable it in **Settings > Sidebar > Group unread channels separately**. 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalGroupUnreadChannels": "default_off"`` with options ``"default_off"`` and ``"default_on"``. |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

Strict CSRF Token Enforcement (Experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables CSRF protection tokens for additional hardening compared to the currently used custom header. When the user logs in, an additional cookie is created with the CSRF token contained.

**False**: Disables CSRF protection tokens.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalStrictCSRFEnforcement": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------+

Restrict System Admin
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Restricts the System Admin from viewing and modifying a subset of server configuration settings from the System Console. Not recommended for use in on-prem installations. This is intended to support Mattermost Private Cloud in giving the System Admin role to users but restricting certain actions only for Cloud Admins.

**False**: No restrictions are applied to the System Admin role.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictSystemAdmin": "false"`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

Team Settings
~~~~~~~~~~~~~~

Teammate Name Display
^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Control Teammate Name Display at the system level. 

**True**: Allows System Admins to control Teammate Name Display at the system level.

**False**: System Admins cannot control Teammate Name Display at the system level.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LockTeammateNameDisplay": []`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

Default Channels (Experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

Default channels every user is added to automatically after joining a new team. Only applies to Public channels, but affects all teams on the server. 

When not set, every user is added to the ``off-topic`` and ``town-square`` channels by default.

.. note::

   Even if ``town-square`` is not listed, every user is added to that channel after joining a new team.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalDefaultChannels": []`` with string array input consisting of channel names, such as ``["announcement", "developers"]``. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Client Requirement Settings (Experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Latest Android Version
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

The latest version of the Android React Native app that is recommended for use. 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AndroidLatestVersion": ""`` with string input corresponding to a version string, such as ``"1.2.0"``. |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

Minimum Android Version
^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

The minimum version of the Android React Native app that is required to be used. 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AndroidMinVersion": ""`` with string input corresponding to a version string, such as ``"1.2.0"``. |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

Latest iOS Version
^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

The latest version of the iOS app that is recommended for use. 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IosLatestVersion": ""`` with string input corresponding to a version string, such as ``"1.2.0"``. |
+------------------------------------------------------------------------------------------------------------------------------------------------+

Minimum iOS Version
^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

The minimum version of the iOS React Native app that is required to be used. 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IosMinVersion": ""`` with string input corresponding to a version string, such as ``"1.2.0"``. |
+---------------------------------------------------------------------------------------------------------------------------------------------+

Push Notification Buffer
^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

Used to control the buffer of outstanding Push Notification messages to be sent. If the number of messages exceeds that number, then the request making the Push Notification will be blocked until there's room. 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| This feature’s ``config.json`` setting is ``"PushNotificationBuffer": 1000"`` with numerical input.                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------+

Theme Settings (Experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allowed Themes
^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Select the themes that can be chosen by users when ``EnableThemeSelection`` is set to ``true``. 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowedThemes": []`` with string array input consisting of the options ``"default"``, ``"organization"``, ``"mattermostDark"``, and ``"windows10"``, such as ``["mattermostDark", "windows10"]``. |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Experimental Settings
~~~~~~~~~~~~~~~~~~~~~

Disable Post Metadata
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Disabling post metadata is only recommended if you are experiencing a significant decrease in performance around channel and post load times.

**False**: Load channels with more accurate scroll positioning by loading post metadata.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DisablePostMetadata": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------+

Analytics Settings
~~~~~~~~~~~~~~~~~~~

Maximum Users for Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Sets the maximum number of users on the server before statistics for total posts, total hashtag posts, total file posts, posts per day, and active users with posts per day are disabled. 

This setting is used to maximize performance for large Enterprise deployments.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxUsersForStatistics": 2500`` with numerical input. |
+---------------------------------------------------------------------------------------------------+

Message Export Settings
~~~~~~~~~~~~~~~~~~~~~~~

Export From Timestamp
^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Set the Unix timestamp (seconds since epoch, UTC) to export data from. 

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExportFromTimestamp": 0`` with numerical input. |
+----------------------------------------------------------------------------------------------+

File Location
^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Set the file location of the compliance exports. By default, they are written to the ``exports`` subdirectory of the configured `Local Storage directory <https://docs.mattermost.com/configure/configuration-settings.html#local-storage-directory>`__.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileLocation": "export"`` with string input. |
+-------------------------------------------------------------------------------------------+

Plugin Settings
~~~~~~~~~~~~~~~

Enable Plugin Uploads
^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables plugin uploads by System Admins at **Plugins > Management**. If you do not plan to upload a plugin, set to ``false`` to control which plugins are installed on your server. See `documentation <https://developers.mattermost.com/integrate/admin-guide/admin-plugins-beta/>`__ to learn more.

**False**: Disables plugin uploads on your Mattermost server.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUploads": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------+

Allow Insecure Download URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables downloading and installing a plugin from a remote URL.

**False**: Disables downloading and installing a plugin from a remote URL.

+-----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowInsecureDownloadUrl": false`` with options ``true`` and ``false``.                    |
+-----------------------------------------------------------------------------------------------------------------------------------------+

Enable Plugin Health Check
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables plugin health check to ensure all plugins are periodically monitored, and restarted or deactivated based on their health status. The health check runs every 30 seconds. If the plugin is detected to fail 3 times within an hour, the Mattermost server attempts to restart it. If the restart fails 3 successive times, it's automatically disabled.

**False**: Disables plugin health check on your Mattermost server.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableHealthCheck": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

Directory
^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

The location of the plugin files. If blank, they are stored in the ``./plugins`` directory. The path that you set must exist and Mattermost must have write permissions in it. 

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Directory": "./plugins"`` with string input.                       |
+-----------------------------------------------------------------------------------------------------------------+

Client Directory
^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

The location of client plugin files. If blank, they are stored in the ``./client/plugins`` directory. The path that you set must exist and Mattermost must have write permissions in it. 

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Directory": "./client/plugins"`` with string input.                |
+-----------------------------------------------------------------------------------------------------------------+

Jobs
~~~~~

Settings to configure how Mattermost schedules and completes periodic tasks such as the deletion of old posts with Data Retention enabled or indexing posts with Elasticsearch. These settings control which Mattermost servers are designated as a Scheduler, a server that queues the tasks at the correct times, and as a Worker, a server that completes the given tasks.

When running Mattermost on a single machine, both ``RunJobs`` and ``RunScheduler`` should be enabled. Without both of these enabled, Mattermost will not function properly.

When running Mattermost in High Availability mode, ``RunJobs`` should be enabled on one or more servers while ``RunScheduler`` should be enabled on all servers under normal circumstances. A High Availability cluster will have one Scheduler and one or more Workers. See the below sections for more information.

Run Jobs
^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This setting isn't available in the System Console and can only be set in ``config.json``.

Set whether or not this Mattermost server will handle tasks created by the Scheduler. When running Mattermost on a single machine, this setting should always be enabled.

When running Mattermost in `High Availablity mode <https://docs.mattermost.com/scale/high-availability-cluster.html>`__, one or more servers should have this setting enabled. We recommend that your High Availability cluster has one or more dedicated Workers with this setting enabled while the remaining Mattermost app servers have it disabled.

+------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RunJobs": true`` with options ``true`` and ``false``.                                 |
+------------------------------------------------------------------------------------------------------------------------------------+

Run Scheduler
^^^^^^^^^^^^^^

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:
This setting isn't available in the System Console and can only be set in ``config.json``.

Set whether or not this Mattermost server will schedule tasks that will be completed by a Worker. When running Mattermost on a single machine, this setting should always be enabled.

When running Mattermost in `High Availablity mode <https://docs.mattermost.com/scale/high-availability-cluster.html>`__, this setting should always be enabled. In a High Availability cluster, exactly one of the servers will be designated as the Scheduler at a time to ensure that duplicate tasks aren't created. See `High Availability documentation <https://docs.mattermost.com/scale/high-availability-cluster.html>`__ for more details.

.. warning::

   We strongly recommend that you not change this setting from the default setting of ``true`` as this prevents the ``ClusterLeader`` from being able to run the scheduler. As a result, recurring jobs such as LDAP sync, Compliance Export, and data retention will no longer be scheduled. In previous Mattermost Server versions, and this documentation, the instructions stated to run the Job Server with ``RunScheduler: false``. The cluster design has evolved and this is no longer the case.

+-----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RunScheduler": true`` with options ``true`` and ``false``.                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------+