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

+--------------------------------------------------------------+-----------------------------------------------------------------+
| Name of the site shown in login screens and UI.              | - System Config path: **Site Configuration > Customization**    |
|                                                              | - ``config.json`` setting: ``.TeamSettings.SiteName``           |
| String input. Maximum 30 characters. Default: ``Mattermost`` | - Environment variable: ``MM_TEAMSETTINGS_SITENAME``            |
+--------------------------------------------------------------+-----------------------------------------------------------------+

Site description
~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| Text displayed above the login form. When not specified, the phrase "Log in" is displayed.| - System Config path: **Site Configuration > Customization**      |
|                                                                                           | - ``config.json`` setting: ``.TeamSettings.CustomDescriptionText``|
| String input.                                                                             | - Environment variable: ``MM_TEAMSETTINGS_CUSTOMDESCRIPTIONTEXT`` |
+-------------------------------------------------------------------------------------------+-------------------------------------------------------------------+

Enable custom branding
~~~~~~~~~~~~~~~~~~~~~~

*This feature was moved to Team Edition in Mattermost v5.0, released June 16th, 2018. Prior to v5.0, this feature is available in legacy Enterprise Edition E10 and E20.*

+--------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| - ***true***: Enables the display of a custom image and text on the login page | - System Config path: **Site Configuration > Customization**            |
| - ***false***: **(Default)** Custom branding is disabled                       | - ``config.json`` setting: ``.TeamSettings.EnableCustomBrand: false``   |
| See **Custom brand image** and **Custom brand text** settings                  | - Environment variable: MM_TEAMSETTINGS_ENABLECUSTOMBRAND               |
+--------------------------------------------------------------------------------+-------------------------------------------------------------------------+

Custom brand image
~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Upload a JPG image for display on the login page. The image must be uploaded through the System Console. The file should be **smaller than 2 MB**. | - System Config path: **Site Configuration > Customization** |
|                                                                                                                                                    | - ``config.json`` setting: N/A                               |
| Enable custom branding must be set to ``true`` to display the image.                                                                               | - Environment variable: N/A                                  |
|                                                                                                                                                    |                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

Custom brand text
~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Text that will be shown below the ***Custom brand image*** on left side of login page. You can format this text using the same `Markdown formatting <https://docs.mattermost.com/help/messaging/formatting-text.html>`__ as in Mattermost messages. | - System Config path: **Site Configuration > Customization** |
|                                                                                                                                                                                                                                                     | - ``config.json`` setting: ``.TeamSettings.CustomBrandText`` |
| String input. Maximum 500 characters. ***Enable custom branding*** must be set to ``true`` to display the image.                                                                                                                                    | - Environment variable: MM_TEAMSETTINGS_CUSTOMBRANDTEXT      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

Enable Ask Community link
~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
|  - **true: (Default)** **Ask the community** link to the `Mattermost Community <https://mattermost.com/pl/default-ask-mattermost-community/>`__ appears under the **Help** menu in the channel header. |  - System Config path: **Site Configuration > Customization**                 |
|                                                                                                                                                                                                        |  - ``config.json`` setting: ``.SupportSettings.EnableAskCommunityLink: true`` |
|  - **false**: The link does not appear.                                                                                                                                                                |  - Environment variable: ``MM_SUPPORTSETTINGS_ENABLEASKCOMMUNITYLINK``        |
|                                                                                                                                                                                                        |                                                                               |
|  The link does not appear on mobile apps.                                                                                                                                                              |                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

Help link
~~~~~~~~~

+--------------------------------------------------------------------------+--------------------------------------------------------------+
| The URL for the Help link on the login page, sign-up pages, and the Help | - System Config path: **Site Configuration > Customization** |
| Resources link under the **Help** menu. If this field is empty, the link | - ``config.json`` setting: ``.SupportSettings.HelpLink``     |
| does not appear.                                                         | - Environment variable: ``MM_SUPPORTSETTINGS_HELPLINK``      |
|                                                                          |                                                              |
| String input. Default is ``https://about.mattermost.com/default-help/``. |                                                              |
|                                                                          |                                                              |
+--------------------------------------------------------------------------+--------------------------------------------------------------+

Terms of Use link
~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| The URL for the Terms of Use of a self-hosted site. A link to the terms appears at the bottom of the sign-up and login pages.                                                                                                                                                                                                                                                                                                                                                      | - **Site Configuration > Customization**                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | - ``config.json`` setting: ``.SupportSettings.TermsOfServiceLink`` |
| The default URL links to a `Terms of Use <https://about.mattermost.com/default-terms/>`__ page hosted on ``mattermost.com``. This includes the Mattermost Acceptable Use Policy explaining the terms under which Mattermost software is provided to end users. If you change the default link to add your own terms for using the service you provide, your new terms **must include a link** to the default terms so end users are aware of the Mattermost Acceptable Use Policy. | - Environment variable: ``MM_SUPPORTSETTINGS_TERMSOFSERVICELINK``  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                    |
| String input. Default is ``https://about.mattermost.com/default-terms/``.                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| **Note**: From Mattermost v5.17, this setting doesn't change the Terms of Use link in the **About Mattermost** dialog.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Privacy Policy link
~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| The URL for the Privacy Policy of a self-hosted site. A link to the policy appears at the bottom of the sign-up and login pages. If this field is empty, the link does not appear. | - **Site Configuration > Customization**                          |
|                                                                                                                                                                                    | - ``config.json`` setting: ``.SupportSettings.PrivacyPolicyLink`` |
|                                                                                                                                                                                    | - Environment variable: ``MM_SUPPORTSETTINGS_PRIVACYPOLICYLINK``  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| **Note**: In version 5.17 and later, this setting does not change the Privacy Policy link in the **About Mattermost** dialog.                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

About link
~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| The URL for a page containing general information about a self-hosted site. A link to the About page appears at the bottom of the sign-up and login pages. If this field is empty the link does not appear.  | - System Config path: **Site Configuration > Customization**  |
|                                                                                                                                                                                                              | - ``config.json`` setting: ``.SupportSettings.AboutLink``     |
| String input. Default is ``https://about.mattermost.com/default-about/``.                                                                                                                                    | - Environment variable: ``MM_SUPPORTSETTINGS_ABOUTLINK``      |
|                                                                                                                                                                                                              |                                                               |
|                                                                                                                                                                                                              |                                                               |
|                                                                                                                                                                                                              |                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

Report a Problem link
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| The URL for the Report a Problem link in the **Help** menu. If this field is empty the link does not appear.  | - System Config path: **Site Configuration > Customization**       |
|                                                                                                               | - ``config.json`` setting: ``.SupportSettings.ReportAProblemLink`` |
| String input. Default: ``https://about.mattermost.com/default-report-a-problem``.                             | - Environment variable: ``MM_SUPPORTSETTINGS_REPORTAPROBLEMLINK``  |
|                                                                                                               |                                                                    |
|                                                                                                               |                                                                    |
+---------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

Mattermost apps download page link
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------+-------------------------------------------------------------------+
| The URL for the Download Apps link in the **Product** menu. If        | - System Config path: **Site Configuration > Customization**      |
| this field is empty, the link does not appear.                        | - ``config.json`` setting: ``.NativeAppSettings.AppDownloadLink`` |
|                                                                       | - Environment variable: ``MM_NATIVEAPPSETTINGS_APPDOWNLOADLINK``  |
| If you have an Enterprise App Store, use this setting to link to      |                                                                   |
| the appropriate download page for your Mattermost apps.               |                                                                   |
|                                                                       |                                                                   |
| String input. Default is ``https://about.mattermost.com/downloads/``. |                                                                   |
+-----------------------------------------------------------------------+-------------------------------------------------------------------+

Android app download link
~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:+

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| The URL to download the Mattermost Android app. Users who access the Mattermost site on a mobile browser will be prompted to download the app through this link. If this field is empty, the prompt does not appear.                              | - **Site Configuration > Customization**                                 |
|                                                                                                                                                                                                                                                   | - ``config.json`` setting: ``.NativeAppSettings.AndroidAppDownloadLink`` |
| If you have an Enterprise App Store, use this setting to link to your Android app.                                                                                                                                                                | - Environment variable: ``MM_NATIVEAPPSETTINGS_ANDROIDAPPDOWNLOADLINK``  |
|                                                                                                                                                                                                                                                   |                                                                          |
| String input. Default is ``https://about.mattermost.com/mattermost-android-app/``.                                                                                                                                                                |                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

iOS app download link
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------------+------------------------------------------------------------------------+
| The URL to download the Mattermost iOS app. Users who access the site on a      | - System Config path: **Site Configuration > Customization**           |
| mobile browser will be prompted to download the app through this link. If       | - ``config.json`` setting: ``.NativeAppSettings.IosAppDownloadLink``   |
| this field is empty, the prompt does not appear.                                | - Environment variable: ``MM_NATIVEAPPSETTINGS_IOSAPPDOWNLOADLINK``    |
|                                                                                 |                                                                        |
| If you use an Enterprise App Store, change this link to point to your iOS app.  |                                                                        |
|                                                                                 |                                                                        |
|                                                                                 |                                                                        |
| String input. Default: ``https://about.mattermost.com/mattermost-ios-app/``.    |                                                                        |
+---------------------------------------------------------------------------------+------------------------------------------------------------------------+

----

Localization
-------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Localization**.

Default server language
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| The default language for system messages and logs. Changes to this setting require a server restart before taking effect.                                                                                                             | - **Site Configuration > Localization**                                  |
|                                                                                                                                                                                                                                       | - ``config.json`` setting: ``.LocalizationSettings.DefaultServerLocale`` |
| Options: ``"bg"``, ``"de"``, ``"en"``, ``en-AU``, ``"es"``, ``"fa"``, ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``, ``"pt-br"``, `"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``, ``"zh_CN"``, and ``"zh_TW"``. | - Environment variable: ``MM_LOCALIZATIONSETTINGS_DEFAULTSERVERLOCALE``  |
|                                                                                                                                                                                                                                       |                                                                          |
| Default: ``"en"``.                                                                                                                                                                                                                    |                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

Default client language
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| The default language for new users and pages where the user is not logged in. Changes to this setting require a server restart before taking effect.                                                                                  | - **Site Configuration > Localization**                                  |
|                                                                                                                                                                                                                                       | - ``config.json`` setting: ``.LocalizationSettings.DefaultClientLocale`` |
| Options: ``"bg"``, ``"de"``, ``"en"``, ``en-AU``, ``"es"``, ``"fa"``, ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``, ``"pt-br"``, `"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``, ``"zh_CN"``, and ``"zh_TW"``. | - Environment variable: ``MM_LOCALIZATIONSETTINGS_DEFAULTCLIENTLOCALE``  |
|                                                                                                                                                                                                                                       |                                                                          |
| Default: ``"en"``.                                                                                                                                                                                                                    |                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

Available languages
~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| Sets the list of languages users see under **Settings > Display > Language**. If this field is blank, users see all supported languages. If this field is not blank, it must contain the **Default client language**, in addition to any other languages.                                                                                                                                                                             | - **Site Configuration > Localization**                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       | - ``config.json`` setting: ``.LocalizationSettings.AvailableLocales`` |
| The ``config.json`` setting is a string that can contain the following comma-separated entries: ``"bg"``, ``"de"``, ``"en"``, ``en-AU``, ``"es"``, ``"fa"``, ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``, ``"pt-br"``, `"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``, ``"zh_CN"``, and ``"zh_TW"``. For example, to limit the language choices to English (US) and Español, the string would be ``”en,es”``. | - Environment variable: ``MM_LOCALIZATIONSETTINGS_AVAILABLELOCALES``  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                       |
| Default: ``""``.                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
|  **Note**: Servers which upgraded to v3.1 need to manually set this field blank to have new languages added by default.                                                                                                                                                                                                                                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

Users and teams
---------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Users and Teams**.

Max users per team
~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| The **Max users per team** is the maximum total number of users per team, including active and inactive users. In Mattermost, a team of people should be a small organization with a specific goal. In the physical world, a team could sit around a single table to discuss their project. The default maximum (50) should be appropriate for most teams, but with appropriate `hardware <https://docs.mattermost.com/install/software-hardware-requirements.html>`_, this limit can be increased to thousands of users. `Channels <https://docs.mattermost.com/guides/channels.html>`_ are another way of organizing communications on different topics.              | - **Site Configuration > Users and teams**                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | - ``config.json`` setting: ``.TeamSettings.MaxUsersPerTeam: 50`` |
| Numerical input. Default: 50.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | - Environment variable: ``MM_TEAMSETTINGS_MAXUSERSPERTEAM``      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+


Max channels per team
~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| The maximum number of channels per team, including both active and deleted channels. | - **Site Configuration > Users and teams**                            |
|                                                                                      | - ``config.json`` setting: ``.TeamSettings.MaxChannelsPerTeam: 2000`` |
|                                                                                      | - Environment variable: ``MM_TEAMSETTINGS_MAXCHANNELSPERTEAM``        |
+--------------------------------------------------------------------------------------+-----------------------------------------------------------------------+

Enable users to open direct message channels with
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| This setting determines whether a user can open a Direct Message channel to anyone on the server or only to members of the same team.                                                                                                                                                                                                                                                                                                    | - **Site Configuration > Users and teams**                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                          | - ``config.json`` setting: ``.TeamSettings.RestrictDirectMessage``   |
| - **Any user on the Mattermost server**: **(Default)** Users can open a Direct Messages channel to any user on the server through the **Direct Messages > More** menu.                                                                                                                                                                                                                                                                   | - Environment variable: ``MM_TEAMSETTINGS_RESTRICTDIRECTMESSAGE``    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                      |
| - **Any member of the team**: The **Direct Messages > More** menu only allows Direct Messages to users on the same team. Pressing :kbd:`Ctrl` :kbd:`K` on Windows or Linux, or :kbd:`⌘` :kbd:`K` on Mac, only lists other users on the team currently being viewed. A user who is a member of multiple teams can only send Direct Messages to the team that is being viewed in the UI, but will still receive messages from other teams. |                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                      |
| This setting only affects the UI, not permissions on the server.                                                                                                                                                                                                                                                                                                                                                                         |                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+

Teammate name display
~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| Specifies how names are displayed in the user interface by default. Users can override this setting in **Settings > Display > Teammate Name Display**.                                                                                                                 | - **Site Configuration > Users and teams**                       |
|                                                                                                                                                                                                                                                                        | - ``config.json`` setting: ``.TeamSettings.TeammateNameDisplay`` |
| - **Show username**:**(Default)** Displays the user’s username. ``config.json`` option: ``"username"``.                                                                                                                                                                | - Environment variable: ``MM_TEAMSETTINGS_TEAMMATENAMEDISPLAY``  |
|                                                                                                                                                                                                                                                                        |                                                                  |
| - **Show nickname if one exists...**: Displays the user’s nickname. If the user does not have a nickname, their full name is displayed. If the user does not have a full name, their username is displayed. ``config.json`` option: ``"nickname_full_name"``.          |                                                                  |
|                                                                                                                                                                                                                                                                        |                                                                  |
| - **Show first and last name**: Displays the user’s full name. If the user does not have a full name, their username is displayed. Recommended when using SAML or LDAP if first name and last name attributes are configured. ``config.json`` option: ``"full_name"``. |                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+


Lock teammate name display for all users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Controls whether users can change settings under **Settings > Display > Teammate Name Display**. | - **Site Configuration > Users and teams**                                  |
|                                                                                                  | - ``config.json`` setting: ``.TeamSettings.LockTeammateNameDisplay: false`` |
| - **false**: **(Default)** Users can change their Teammate Name Display                          | - Environment variable: ``MM_TEAMSETTINGS_LOCKTEAMMATENAMEDISPLAY``         |
| - **true**: Users **cannot** change their Teammate Name Dispaly                                  |                                                                             |
+--------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

Allow users to view archived channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| - **true**: **(Default)** Allows users to access content of archived channels of which they were a member. | - **Site Configuration > Users and teams**                                          |
| - **false**: Users are unable to access content in archived channels.                                      | - ``config.json`` setting: ``.TeamSettings.ExperimentalViewArchivedChannels: true`` |
|                                                                                                            | - Environment variable: ``MM_TEAMSETTINGS_EXPERIMENTALVIEWARCHIVEDCHANNELS``        |
+------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

Show email address
~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| - **true**: **(Default)** All users can see each others’ email addresses.                                                                            | - **Site Configuration > Users and teams**                             |
| - **false**: Hides email addresses in the UI, except from System Admins.                                                                             | - ``config.json`` setting: ``.PrivacySettings.ShowEmailAddress: true`` |
|                                                                                                                                                      | - Environment variable: ``MM_PRIVACYSETTINGS_SHOWEMAILADDRESS``        |
+------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

Show full name
~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| - **true**: **(Default)** Full names are visible to all users in the UI.                                                   | - **Site Configuration > Users and teams**                         |
| - **false**: Hides full names from all users in the UI, except System Admins. Username is shown in place of the full name. | - ``config.json`` setting: ``.PrivacySettings.ShowFullName: true`` |
|                                                                                                                            | - Environment variable: ``MM_PRIVACYSETTINGS_SHOWFULLNAME``        |
+----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

Enable custom user statuses
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| - **true**: **(Default)** Users can set status messages and emojis that are visible to all users. | - **Site Configuration > Users and teams**                                  |
| - **false**: Users cannot set custom statuses.                                                    | - ``config.json`` setting: ``.TeamSettings.EnableCustomUserStatuses: true`` |
|                                                                                                   | - Environment variable: ``MM_TEAMSETTINGS_ENABLECUSTOMUSERSTATUSES``        |
+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

----

Notifications
-------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Notifications**.

Show @channel, @all, or @here confirmation dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| - **true**: **(Default)** Requires users to confirm when posting @channel, @all, @here, or group mentions in channels with more than 5 members.     | - **Site Configuration > Notifications**                                               |
| - **false**: No confirmation is required.                                                                                                           | - ``config.json`` setting: ``.TeamSettings.EnableConfirmNotificationsToChannel: true`` |
|                                                                                                                                                     | - Environment variable: ``MM_TEAMSETTINGS_ENABLECONFIRMNOTIFICATIONSTOCHANNEL``        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+

Enable email notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| - **true**: **(Default)** Enables automatic email notifications for posts.                                                                                                 | - **Site Configuration > Notifications**                                    |
| - **false**: Disables notifications. A developer may choose this option to speed development by skipping email setup. See also the **Enable preview mode banner** setting. | - ``config.json`` setting: ``.EmailSettings.SendEmailNotifications: false`` |
|                                                                                                                                                                            | - Environment variable: ``MM_EMAILSETTINGS_SENDEMAILNOTIFICATIONS``         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| **Notes**:                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                          |
| - If this setting is ``false``, and the SMTP server is set up, account-related emails (such as authentication messages) will be sent regardless of this setting.                                                                                         |
| - Email invitations and account deactivation emails are not affected by this setting.                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _email-preview-mode-banner-config:

Enable preview mode banner
~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| - **true**: **(Default)** When **Send email notifications** is ``false``, users see the Preview Mode banner. This banner alerts users that email notifications are disabled. | - **Site Configuration > Notifications**                                    |
| - **false**: Preview Mode banner does not appear.                                                                                                                            | - ``config.json`` setting: ``.EmailSettings.EnablePreviewModeBanner: true`` |
|                                                                                                                                                                              | - Environment variable: ``MM_EMAILSETTINGS_ENABLEPREVIEWMODEBANNER``        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

Enable email batching
~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| - **true**: Multiple email notifications for mentions and direct messages over a given time period are batched into a single email. The time period can be customized by each user under **Settings > Notifications**. The default time period is 15 minutes.                | - **Site Configuration > Notifications**                                 |
| - **false**: **(Default)** Emails will be sent for each mention or direct message.                                                                                                                                                                                           | - ``config.json`` setting: ``.EmailSettings.EnableEmailBatching: false`` |
|                                                                                                                                                                                                                                                                              | - Environment variable: ``MM_EMAILSETTINGS_ENABLEEMAILBATCHING``         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| **Notes**:                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                         |
| - Regardless of this setting, a user can turn off these notifications under **Settings > Notifications**.                                                                                                                                                                                                                                               |
| - The `Site Url <https://docs.mattermost.com/configure/environment-configuration-settings.html#site-url>`_  and `SMTP Email Server <https://docs.mattermost.com/configure/environment-configuration-settings.html#smtp-server>`_ must be configured to allow email batching.                                                                            |
| - Email batching in `High Availability Mode <https://docs.mattermost.com/configure/environment-configuration-settings.html#enable-high-availability-mode>`_ is planned, but not yet supported.                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Email notification contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| - **Send full message contents**: **(Default)** Email notifications include the full message contents, along with the name of the sender and the channel. ``config.json`` setting: ``"full"``                                                                                                                                                          | - **Site Configuration > Notifications**                                            |
|                                                                                                                                                                                                                                                                                                                                                        | - ``config.json`` setting: ``.EmailSettings.EmailNotificationContentsType: "full"`` |
| - **Send generic description with only sender name**: Only the name of the sender and team name are included in email notifications. Use this option if Mattermost contains confidential information and policy dictates it cannot be stored in email. ``config.json`` setting: ``"generic"``                                                          | - Environment variable: ``MM_EMAILSETTINGS_EMAILNOTIFICATIONCONTENTSTYPE``          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

Support email address
~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+
| Sets a user support (or feedback) email address that is displayed on email notifications and during the Getting Started tutorial. This address should be monitored by a System Admin. If no value is set, email notifications will not contain a way for users to request assistance.                                                    | - **Site Configuration > Notifications**                       |
|                                                                                                                                                                                                                                                                                                                                          | - ``config.json`` setting: ``.SupportSettings.SupportEmail``   |
| String input. This field is required when changing settings in the System Console.                                                                                                                                                                                                                                                       | - Environment variable: ``MM_SUPPORTSETTINGS_SUPPORTEMAIL``    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+

Notification display name
~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Display name for email notifications sent from the Mattermost system.              | - **Site Configuration > Notifications**                     |
|                                                                                    | - ``config.json`` setting: ``.EmailSettings.FeedbackName``   |
| String input. This field is required when changing settings in the System Console. | - Environment variable: ``MM_EMAILSETTINGS_FEEDBACKNAME``    |
+------------------------------------------------------------------------------------+--------------------------------------------------------------+

Notification from address
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| Email address for notification emails from the Mattermost system. This address should be monitored by a System Admin. | - **Site Configuration > Notifications**                      |
|                                                                                                                       | - ``config.json`` setting: ``.EmailSettings.FeedbackEmail``   |
| String input. This field is required when changing settings in the System Console.                                    | - Environment variable: ``MM_EMAILSETTINGS_FEEDBACKEMAIL``    |
+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

Notification reply-to address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+
| Email address used in the reply-to header when sending notification emails from the Mattermost system. This address should be monitored by a System Admin. | - **Site Configuration > Notifications**                       |
|                                                                                                                                                            | - ``config.json`` setting: ``.EmailSettings.ReplyToAddress``   |
| String input.                                                                                                                                              | - Environment variable: ``MM_EMAILSETTINGS_REPLYTOADDRESS``    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+

Notification footer mailing address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| Optional setting to include the organization’s name and mailing address in the footer of email notifications. If not set, nothing will appear. | - **Site Configuration > Notifications**                             |
|                                                                                                                                                | - ``config.json`` setting: ``.EmailSettings.FeedbackOrganization``   |
| String input.                                                                                                                                  | - Environment variable: ``MM_EMAILSETTINGS_FEEDBACKORGANIZATION``    |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+


Push notification contents
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| - **Generic description with only sender name**: Push notifications include the sender’s name, but not the channel name or message contents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | - **Site Configuration > Notifications**                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | - ``config.json`` setting: ``.EmailSettings.PushNotificationContents: `` |
| - **Generic description with sender and channel names**: **(Default)** Push notifications include the name of the sender and channel, but not the message contents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | - Environment variable: ``MM_EMAILSETTINGS_PUSHNOTIFICATIONCONTENTS``    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                          |
| - **Full message content sent in the notification payload**: Includes the message contents in the push notification payload, which may be sent through `Apple’s Push Notification service <https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1>`__ `or Google’s Firebase Cloud Messaging <https://firebase.google.com/docs/cloud-messaging>`__ . It is **highly recommended** this option only be used with an ``"https"`` protocol to encrypt the connection and protect confidential information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                          |
| - **Full message content fetched from the server on receipt** (*Available in Mattermost Enterprise*): The notification payload contains no message content. Instead it contains a unique message ID used to fetch message content from the Mattermost server when a push notification is received via a `notification service app extension <https://developer.apple.com/documentation/usernotifications/modifying_content_in_newly_delivered_notifications>`__ on iOS or `an expandable notification pattern <https://developer.android.com/training/notify-user/expanded>`__ on Android. If the server cannot be reached, a generic push notification is displayed without message content or sender name. For customers who wrap the Mattermost mobile application in a secure container, such as BlackBerry Dynamics, MobileIron, or AirWatch, the container must fetch the message contents using the unique message ID when push notifications are received. If the container is unable to execute the fetch, the push notification contents cannot be received by the customer's mobile application without passing the message contents through Apple or Google's notification service. |                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

----

Announcement banner
-------------------

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Announcement Banner**.

Enable announcement banner
~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| - **true**: Enable an announcement banner that is displayed across the top of the screen for all teams.              | - **Site Configuration > Announcement banner**                           |
|                                                                                                                      | - ``config.json`` setting: ``.AnnouncementSettings.EnableBanner: false`` |
| - **false**: **(Default)** Disable the announcement banner.                                                          | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_ENABLEBANNER``         |
|                                                                                                                      |                                                                          |
| See **Banner text**, **Banner color**, **Banner text color**, and **Allow banner dismissal** for additional options. |                                                                          |
+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+


Banner text
~~~~~~~~~~~

+------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| The text of the announcement banner. If no text is provided, the banner will not appear. | - **Site Configuration > Announcement banner**                    |
|                                                                                          | - ``config.json`` setting: ``.AnnouncementSettings.BannerText``   |
| String input.                                                                            | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_BANNERTEXT``    |
+------------------------------------------------------------------------------------------+-------------------------------------------------------------------+


Banner color
~~~~~~~~~~~~~

+--------------------------------------------------+-----------------------------------------------------------------------------+
| The background color of the announcement banner. | - **Site Configuration > Announcement banner**                              |
|                                                  | - ``config.json`` setting: ``.AnnouncementSettings.BannerColor: "#f2a93b"`` |
| String input of a CSS color value.               | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_BANNERCOLOR``             |
+--------------------------------------------------+-----------------------------------------------------------------------------+

Banner text color
~~~~~~~~~~~~~~~~~

+---------------------------------------------------+---------------------------------------------------------------------------------+
| The color of the text in the announcement banner. | - **Site Configuration > Announcement banner**                                  |
|                                                   | - ``config.json`` setting: ``.AnnouncementSettings.BannerTextColor: "#333333"`` |
| String input of a CSS color value.                | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_BANNERTEXTCOLOR``             |
+---------------------------------------------------+---------------------------------------------------------------------------------+


Allow banner dismissal
~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| - **true**: **(Default)** Users can dismiss the banner. The banner will re-appear the next time the user logs in, the banner text is updated, or a System Admin disables the banner and re-enables it. | - **Site Configuration > Announcement banner**                                  |
|                                                                                                                                                                                                        | - ``config.json`` setting: ``.AnnouncementSettings.AllowBannerDismissal: true`` |
| - **false**: Users cannot dismiss the banner.                                                                                                                                                          | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_ALLOWBANNERDISMISSAL``        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+

----

Emoji
------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Emoji**.

Enable emoji picker
~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**True**: Enables an emoji picker that allows users to select    | - System Config path: **Site Configuration > Emoji**            |
|emojis to add as reactions or use in messages. Enabling the emoji| - ``config.json`` setting:                                      |
|picker with a large number of custom emojis may slow down        |``.ServiceSettings.EnableEmojiPicker`` with options ``true`` and |
|performance.                                                     |``falt                                                           |
|                                                                 |                                                                 |
|**False**: The emoji picker is disabled.                         |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Enable custom emoji
~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|                                                                 |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+


+----------------------------------------------------------------+------------------------------------------------------------------+
|**True**: Enables a **Custom Emoji** option in the emoji picker,| - System Config path: **Site Configuration > Emoji**             |
|where users can go to add custom emojis.                        | - ``config.json`` setting:``.ServiceSettings.EnableCustomEmoji`` |
|                                                                |with options ``true`` and ``false``.                              |
|**False**: Custom emojis are disabled.                          |                                                                  |
|                                                                |                                                                  |
+----------------------------------------------------------------+------------------------------------------------------------------+

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

+--------------------------------------------------------------------------+-----------------------------------------------------------------+
|This setting must be enabled to support `Collapsed Reply Threads          |  - System Config path: **Site Configuration > Posts**           |
|<https://docs.mattermost.com/channels/organize-conversations.html>`__. See| - ``config.json`` setting is                                    |
|the `administrator’s guide to enabling Collapsed Reply Threads            |``.ServiceSettings.ThreadAutoFollow: true`` with options ``true``|
|<https://support.mattermost.com/hc/en-us/articles/6880701948564>`__       | and ``false``.                                                  |
|knowledge base article for details.                                       |                                                                 |
|                                                                          |                                                                 |
|**True**: Threads a user starts, participates in, or is mentioned in are  |                                                                 |
|automatically followed. A new ``Threads`` table is added in the database  |                                                                 |
|that tracks threads and thread participants, and a ``ThreadMembership``   |                                                                 |
|table tracks followed threads for each user and the read or unread state  |                                                                 |
|of each followed thread. Mattermost Cloud workspaces have this setting    |                                                                 |
|enabled.                                                                  |                                                                 |
|                                                                          |                                                                 |
|**False**: All backend operations for Collapsed Reply Threads are disabled|                                                                 |
|and server performance will not be impacted by the feature. Collapsed     |                                                                 |
|Reply Threads (``CollapsedThreads``) cannot be enabled if                 |                                                                 |
|``ThreadAutoFollow`` is disabled.                                         |                                                                 |
|                                                                          |                                                                 |
+--------------------------------------------------------------------------+-----------------------------------------------------------------+


.. note::

   Enabling this configuration setting doesn’t retroactively follow threads for actions taken prior to the setting being enabled. For example, threads a user participated in prior to enabling this setting won't be automatically followed. However, if this setting is enabled, and a user adds a new comment on an old thread, they will automatically start following the thread.

Collapsed reply threads
~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------+-----------------------------------------------------------------+
|Collapsed Reply Threads offers an enhanced experience for users      | - System Config path: **Site Configuration > Posts**            |
|communicating in threads and replying to messages. Collapsed Reply   | This feature's ``config.json`` setting is                       |
|Threads is generally available in Mattermost Cloud and from          |``.ServiceSettings.CollapsedThread: always_on`` with options     |
|self-hosted Mattermost v7.0, and is enabled by default for all new   |``disabled``, ``default_off``, ``default_on``, and ``always_on`` |
|Mattermost deployments. See our `Organizing Conversations using      |                                                                 |
|Collapsed Reply Threads                                              |                                                                 |
|<https://docs.mattermost.com/channels/organize-conversations.html>`__|                                                                 |
|documentation to learn more about this feature.                      |                                                                 |
+---------------------------------------------------------------------+-----------------------------------------------------------------+


.. important::

    Customers upgrading to v7.0 must review the `administrator’s guide to enabling Collapsed Reply Threads <https://support.mattermost.com/hc/en-us/articles/6880701948564>`__ knowledge base article to learn about the system requirements, steps to enable, and self-host prerequisites to consider prior to enabling this functionality.

System Admins can set the default availability of Collapsed Reply Threads for their workspace by going to **System Console > Site Configuration > Posts**, then setting **Collapsed Reply Threads** to one of the following options:

**Always On**: Enables Collapsed Reply Threads functionality on the server and for all users. Users can't disable this functionality. This is the recommended configuration for optimal user experience and to ensure consistency in how users read and respond to threaded conversations. Mattermost Cloud workspaces have Collapsed Reply Threads set to ``always_on`` by default.

**Default On**: Enables Collapsed Reply Threads functionality on the server and for all users. Users can choose to `disable Collapsed Reply Threads <https://docs.mattermost.com/channels/channels-settings.html#collapsed-reply-threads>`__ for their Mattermost account in **Settings > Display > Collapsed Reply Threads**.

**Default Off**: Enables Collapsed Reply Threads functionality on the server but not for users. Users can choose to `enable Collapsed Reply Threads <https://docs.mattermost.com/channels/channels-settings.html#collapsed-reply-threads>`__ for their Mattermost account in **Settings > Display > Collapsed Reply Threads**.

**Disabled**: Disables Collapsed Reply Threads front-end functionality.

Enable link previews
~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|Link previews are previews of linked website content, image      |  - System Config path: **Site Configuration > Posts**           |
|links, and YouTube videos that are displayed below posts when    |This                                                             |
|available.                                                       |feature's ``config.json`` setting is `":
|                                                                 |true`` with options ``true`` and ``false``.                      |
|Link previews are requested by the server, meaning the Mattermost|                                                                 |
|server must be connected to the internet for previews to be      |                                                                 |
|displayed. This connection can be established through a `firewall|                                                                 |
|or outbound proxy                                                |                                                                 |
|<https://docs.mattermost.com/install/outbound-proxy.html>`__ in  |                                                                 |
|environments where direct internet connectivity is not given or  |                                                                 |
|security policies make this necessary.                           |                                                                 |
|                                                                 |                                                                 |
|**True**: Website link previews, image link previews, and YouTube|                                                                 |
|previews are enabled on the server. Users can enable or disable  |                                                                 |
|website previews for themselves from **Settings > Display >      |                                                                 |
|Website Link Previews**.                                         |                                                                 |
|                                                                 |                                                                 |
|**False**: Website link previews, image link previews, and       |                                                                 |
|YouTube previews are disabled. The server does not request       |                                                                 |
|metadata for any links sent in messages.                         |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+


Disable link previews for specific domains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|Link previews are disabled for this list of comma-separated      | - System Config path: **Site Configuration > Posts**            |
|domains (e.g. “github.com, mattermost.com”).                     | This                                                            |
|                                                                 |feature's ``config.json`` setting is ``"RestrictLinkPreviews":   |
|                                                                 |""`` with string input.                                          |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Enable message link previews
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**True**: Links to messages generate a preview for any users with|  - System Config path: **Site Configuration > Posts**           |
|access to the original message.                                  |This                                                             |
|                                                                 |feature's ``config.json`` setting is ``"EnablePermalinkPreviews":|
|**False**: Links to messages don't include a preview.            |true`` with options ``true`` and ``false``.                      |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Enable SVGs
~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**True**: Enables users to see previews of SVG file attachments  | - System Config path: **Site Configuration > Posts** This       |
|and SVG image links.                                             |feature's ``config.json`` setting is ``"EnableSVGs": false`` with|
|                                                                 |options ``true`` and ``false``.                                  |
|**False**: Previews of SVG file attachments and SVG image links  |                                                                 |
|are not displayed.                                               |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Enable LaTeX code block rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**True**: Enables rendering of LaTeX code in a ``latex`` code    |  - System Config path: **Site Configuration > Posts** This      |
|block.                                                           |feature's ``config.json`` setting is ``"EnableLatex": false``    |
|                                                                 |with options ``true`` and ``false``.                             |
|**False**: Disables rendering of LaTeX code to prevent the app   |                                                                 |
|from crashing when sharing code that might outgrow assigned      |                                                                 |
|memory. When disabled, LaTeX code will be highlighted.           |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Enable inline LaTeX rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| **True**: Enables inline rendering of LaTeX code.                                                       |  - System Config path: **Site Configuration > Posts**           |
|                                                                                                         |This                                                             |
|**False**: Disables inline rendering of LaTeX code to prevent the app from crashing when sharing code    |feature's ``config.json`` setting is ``"EnableInlineLatex":      |
|that might outgrow assigned memory. When disabled, LaTeX code will be highlighted. When disabled, Latex  |false`` with options ``true`` and ``false``.                     |
|code can only be `rendered in a code block using syntax highlighting                                     |                                                                 |
|<https://docs.mattermost.com/configure/configuration-settings.html#enable-latex-code-block-rendering>`__.|                                                                 |
+---------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+

Custom URL schemes
~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|A list of URL schemes that are used for autolinking in message   |  - System Config path: **Site Configuration > Posts**           |
|text. ``http``, ``https``, ``ftp``, ``tel`` and ``mailto`` always|This                                                             |
|create links.                                                    |feature's ``config.json`` setting is ``"CustomUrlSchemes": []``  |
|                                                                 |with string array input consisting of URL schemes, such as       |
|                                                                 |``["git", "smtp"]``.                                             |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Google API key
~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|Mattermost offers the ability to embed YouTube videos from URLs  | - System Config path: **Site Configuration > Posts**            |
|shared by end users.                                             | This                                                            |
|                                                                 |feature's ``config.json`` setting is ``"GoogleDeveloperKey": ""``|
|Set this key and add YouTube Data API v3 as a service to your key|with string input.                                               |
|to enable the display of titles for embedded YouTube video       |                                                                 |
|previews. Without the key, YouTube previews will still be created|                                                                 |
|based on hyperlinks appearing in messages or comments but they   |                                                                 |
|will not show the video title. If Google detects the number of   |                                                                 |
|views is exceedingly high, they may throttle embed access.       |                                                                 |
|                                                                 |                                                                 |
|Should this occur, you can remove the throttle by registering for|                                                                 |
|a Google Developer Key and entering it in this field following   |                                                                 |
|these instructions:                                              |                                                                 |
|https://www.youtube.com/watch?v=Im69kzhpR3I. Your Google         |                                                                 |
|Developer Key is used in client-side Javascript.                 |                                                                 |
|                                                                 |                                                                 |
|Using a Google API Key allows Mattermost to detect when a video  |                                                                 |
|is no longer available and display the post with a *Video not    |                                                                 |
|found* label.                                                    |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

----

File sharing and downloads
---------------------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > File Sharing and Downloads**.

Allow file sharing
~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|When ``false``, disables file sharing on the server. All file and|  - System Config path: **Site Configuration > File Sharing and  |
|image uploads on messages are forbidden across clients and       |Downloads** This feature's ``config.json`` setting is            |
|devices, including mobile.                                       |``"EnableFileAttachments": true`` with options ``true`` and      |
|                                                                 |``false``.                                                       |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Allow file uploads on mobile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*


+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**True**: Enables file uploads on messages using Mattermost      |  - System Config path: **Site Configuration > File Sharing and  |
|clients.                                                         |Downloads**                                                      |
|                                                                 |This feature's ``config.json`` setting is                        |
|**False**: Disables file uploads on mobile apps. All file and    |``"EnableMobileUpload": true`` with options ``true`` and         |
|image uploads on messages are forbidden across clients and       |``false``.                                                       |
|devices, including mobile.                                       |                                                                 |
|                                                                 |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Allow file downloads on mobile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**True**: Enables file downloads on Mattermost mobile apps.      |- System Config path: **Site Configuration > File Sharing and    |
|                                                                 |Downloads**                                                      |
|**False**: Disables file downloads on mobile apps. Users can     | This feature's ``config.json`` setting is                       |
|still download files from a mobile web browser.                  |``"EnableMobileDownload": true`` with options ``true`` and       |
|                                                                 |``false``.                                                       |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

----

Public Links
------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Public Links**.

Enable public file links
~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**True**: Allow users to generate public links to files and      |- System Config path: **Site Configuration > Public Links**      |
|images for sharing outside the Mattermost system with a public   | This feature's ``config.json`` setting is ``"EnablePublicLink": |
|URL.                                                             |true`` with options ``true`` and ``false``.                      |
|                                                                 |                                                                 |
|**False**: The **Get Public Link** option is hidden from the     |                                                                 |
|image preview user interface.                                    |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+


.. note::

   When set to ``False``, anyone who tries to visit a previously generated public link will receive an error message saying public links have been disabled. When set back to ``True``, old public links will work again unless the **Public Link Salt** has been regenerated.

Public link salt
~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|32-character salt added to the URL of public links when public   |- System Config path: **Site Configuration > Public Links**      |
|links are enabled. Select **Regenerate** in the System Console to| This                                                            |
|create a new salt, which will invalidate all existing public     |feature's ``config.json`` setting is ``"PublicLinkSalt": ""``    |
|links.                                                           |with string input.                                               |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

----

Notices
--------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Notices**.

Enable admin notices
~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**True**: System Admins will receive notices about available     | - System Config path: **Site Configuration > Notices** This     |
|server upgrades and relevant system administration               |feature's ``config.json`` setting is ``"AdminNoticesEnabled":    |
|features. `Learn more                                            |true`` with options ``true`` and ``false``.                      |
|<https://docs.mattermost.com/manage/in-product-notices.html>`__. |                                                                 |
|                                                                 |                                                                 |
|**False**: System Admins will not receive notices except those   |                                                                 |
|that apply to all end users (See ``UserNoticesEnabled``).        |                                                                 |
|                                                                 |                                                                 |
|                                                                 |                                                                 |
|                                                                 |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Enable end user notices
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**True**: All users will receive notices about available client  |- System Config path: **Site Configuration > Notices**           |
|upgrades and relevant end user features to improve user          | This feature's ``config.json`` setting is                       |
|experience. `Learn more                                          |``"UserNoticesEnabled": true`` with options ``true`` and         |
|<https://docs.mattermost.com/manage/in-product-notices.html>`__. |``false``.                                                       |
|                                                                 |                                                                 |
|**False**: Users will not receive notices about available client |                                                                 |
|upgrades and relevant end user features.                         |                                                                 |
|                                                                 |                                                                 |
|                                                                 |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+
