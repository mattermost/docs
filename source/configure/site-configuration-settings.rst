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
| Name of the site shown in login screens and user interface.  | - System Config path: **Site Configuration > Customization**    |
|                                                              | - ``config.json`` setting: ``.TeamSettings.SiteName``           |
| String input. Maximum 30 characters. Default: ``Mattermost`` | - Environment variable: ``MM_TEAMSETTINGS_SITENAME``            |
+--------------------------------------------------------------+-----------------------------------------------------------------+

Site description
~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| Text displayed above the login form. When not specified, the phrase "Log in" is displayed. | - System Config path: **Site Configuration > Customization**       |
|                                                                                            | - ``config.json`` setting: ``.TeamSettings.CustomDescriptionText`` |
| String input.                                                                              | - Environment variable: ``MM_TEAMSETTINGS_CUSTOMDESCRIPTIONTEXT``  |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

Enable custom branding
~~~~~~~~~~~~~~~~~~~~~~

*This feature was moved to Team Edition in Mattermost v5.0, released June 16th, 2018. Prior to v5.0, this feature is available in legacy Enterprise Edition E10 and E20.*

+--------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| - **true**: Enables the display of a custom image and text on the login page   | - System Config path: **Site Configuration > Customization**          |
| - **false**: **(Default)** Custom branding is disabled                         | - ``config.json`` setting: ``.TeamSettings.EnableCustomBrand: false`` |
| See the **Custom brand image** and **Custom brand text** settings              | - Environment variable: MM_TEAMSETTINGS_ENABLECUSTOMBRAND             |
|                                                                                |                                                                       |
+--------------------------------------------------------------------------------+-----------------------------------------------------------------------+

Custom brand image
~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| A JPG image for display on the login page. The image **must** be uploaded through the System Console. There is no ``config.json`` setting. The file should be **smaller than 2 MB**. | - System Config path: **Site Configuration > Customization** |
|                                                                                                                                                                                      | - ``config.json`` setting: N/A                               |
| Enable custom branding must be set to ``true`` to display the image.                                                                                                                 | - Environment variable: N/A                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

Custom brand text
~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Text that will be shown below the **Custom brand image** on the login page. You can format this text using the same `Markdown formatting <https://docs.mattermost.com/help/messaging/formatting-text.html>`__ as in Mattermost messages. | - System Config path: **Site Configuration > Customization** |
|                                                                                                                                                                                                                                          | - ``config.json`` setting: ``.TeamSettings.CustomBrandText`` |
| String input. Maximum 500 characters. **Enable custom branding** must be set to ``true`` to display the text.                                                                                                                            | - Environment variable: MM_TEAMSETTINGS_CUSTOMBRANDTEXT      |
|                                                                                                                                                                                                                                          |                                                              |
|                                                                                                                                                                                                                                          |                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

Enable Ask Community link
~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
|  - **true**: **(Default)** A link to the `Mattermost Community <https://mattermost.com/pl/default-ask-mattermost-community/>`__ appears as **Ask the community** under the **Help** menu in the channel header. |  - System Config path: **Site Configuration > Customization**                 |
|  - **false**: The link does not appear.                                                                                                                                                                         |  - ``config.json`` setting: ``.SupportSettings.EnableAskCommunityLink: true`` |
|                                                                                                                                                                                                                 |  - Environment variable: ``MM_SUPPORTSETTINGS_ENABLEASKCOMMUNITYLINK``        |
|  The link does not appear on mobile apps.                                                                                                                                                                       |                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

Help link
~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| This field sets the URL for the Help link on the login and sign-up pages, as well as the **Help Resources** link under the **Help** menu in the channel header. If this field is empty, those links do not appear. | - System Config path: **Site Configuration > Customization** |
|                                                                                                                                                                                                                    | - ``config.json`` setting: ``.SupportSettings.HelpLink``     |
| String input. Default is ``https://about.mattermost.com/default-help/``.                                                                                                                                           | - Environment variable: ``MM_SUPPORTSETTINGS_HELPLINK``      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

Terms of Use link
~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| This field sets the URL for the Terms of Use of a self-hosted site. A link to the terms appears at the bottom of the sign-up and login pages.                                                                                                                                                                                                                                                                                                   | - System Config path: **Site Configuration > Customization**       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 | - ``config.json`` setting: ``.SupportSettings.TermsOfServiceLink`` |
| The default URL links to a `Terms of Use <https://about.mattermost.com/default-terms/>`__ page hosted on ``mattermost.com``. This includes the Mattermost Acceptable Use Policy explaining the terms under which Mattermost software is provided to end users. If you change the default link to add your own terms, the new terms **must include a link** to the default terms so end users are aware of the Mattermost Acceptable Use Policy. | - Environment variable: ``MM_SUPPORTSETTINGS_TERMSOFSERVICELINK``  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                    |
| String input. Default is ``https://about.mattermost.com/default-terms/``.                                                                                                                                                                                                                                                                                                                                                                       |                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| **Note**: From Mattermost v5.17, this setting doesn't change the Terms of Use link in the **About Mattermost** window.                                                                                                                                                                                                                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Privacy Policy link
~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| This field sets the URL for the Privacy Policy of a self-hosted site. A link to the policy appears at the bottom of the sign-up and login pages. If this field is empty, the link does not appear. | - System Config path: **Site Configuration > Customization**      |
|                                                                                                                                                                                                    | - ``config.json`` setting: ``.SupportSettings.PrivacyPolicyLink`` |
| String input. Default is ``https://about.mattermost.com/default-privacy-policy/``.                                                                                                                 | - Environment variable: ``MM_SUPPORTSETTINGS_PRIVACYPOLICYLINK``  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| **Note**: In version 5.17 and later, this setting does not change the Privacy Policy link in the **About Mattermost** window.                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

About link
~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| This field sets the URL for a page containing general information about a self-hosted site. A link to the About page appears at the bottom of the sign-up and login pages. If this field is empty the link does not appear. | - System Config path: **Site Configuration > Customization**  |
|                                                                                                                                                                                                                             | - ``config.json`` setting: ``.SupportSettings.AboutLink``     |
| String input. Default is ``https://about.mattermost.com/default-about/``.                                                                                                                                                   | - Environment variable: ``MM_SUPPORTSETTINGS_ABOUTLINK``      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

Report a Problem link
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| This field sets the URL for the **Report a Problem** link in the channel header **Help** menu. If this field is empty the link does not appear. | - System Config path: **Site Configuration > Customization**       |
|                                                                                                                                                 | - ``config.json`` setting: ``.SupportSettings.ReportAProblemLink`` |
| String input. Default: ``https://about.mattermost.com/default-report-a-problem``.                                                               | - Environment variable: ``MM_SUPPORTSETTINGS_REPORTAPROBLEMLINK``  |
+-------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

Mattermost apps download page link
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| This field sets the URL for the Download Apps link in the **Product** menu. If this field is empty, the link does not appear. | - System Config path: **Site Configuration > Customization**      |
|                                                                                                                               | - ``config.json`` setting: ``.NativeAppSettings.AppDownloadLink`` |
| If you have an Enterprise App Store, set the link to the appropriate download page for your Mattermost apps.                  | - Environment variable: ``MM_NATIVEAPPSETTINGS_APPDOWNLOADLINK``  |
|                                                                                                                               |                                                                   |
| String input. Default is ``https://about.mattermost.com/downloads/``.                                                         |                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+

Android app download link
~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:+

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| This field sets the URL to download the Mattermost Android app. Users who access the Mattermost site on a mobile browser will be prompted to download the app through this link. If this field is empty, the prompt does not appear. | - System Config path: **Site Configuration > Customization**             |
|                                                                                                                                                                                                                                      | - ``config.json`` setting: ``.NativeAppSettings.AndroidAppDownloadLink`` |
| If you have an Enterprise App Store, link to your Android app.                                                                                                                                                                       | - Environment variable: ``MM_NATIVEAPPSETTINGS_ANDROIDAPPDOWNLOADLINK``  |
|                                                                                                                                                                                                                                      |                                                                          |
| String input. Default is ``https://about.mattermost.com/mattermost-android-app/``.                                                                                                                                                   |                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

iOS app download link
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| This field sets the URL to download the Mattermost iOS app. Users who access the site on a mobile browser will be prompted to download the app through this link. If this field is empty, the prompt does not appear. | - System Config path: **Site Configuration > Customization**           |
|                                                                                                                                                                                                                       | - ``config.json`` setting: ``.NativeAppSettings.IosAppDownloadLink``   |
| If you use an Enterprise App Store, link to your iOS app.                                                                                                                                                             | - Environment variable: ``MM_NATIVEAPPSETTINGS_IOSAPPDOWNLOADLINK``    |
|                                                                                                                                                                                                                       |                                                                        |
| String input. Default: ``https://about.mattermost.com/mattermost-ios-app/``.                                                                                                                                          |                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

----

Localization
-------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Localization**.

Default server language
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| The default language for system messages and logs. Changes to this setting require a server restart before taking effect.                                                                                                             | - System Config path: **Site Configuration > Localization**              |
|                                                                                                                                                                                                                                       | - ``config.json`` setting: ``.LocalizationSettings.DefaultServerLocale`` |
| Options: ``"bg"``, ``"de"``, ``"en"``, ``en-AU``, ``"es"``, ``"fa"``, ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``, ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``, ``"zh_CN"``, and ``"zh_TW"``.| - Environment variable: ``MM_LOCALIZATIONSETTINGS_DEFAULTSERVERLOCALE``  |
|                                                                                                                                                                                                                                       |                                                                          |
| Default: ``"en"``.                                                                                                                                                                                                                    |                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

Default client language
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| The default language for new users and pages where the user is not logged in. Changes to this setting require a server restart before taking effect.                                                                                  | - System Config path: **Site Configuration > Localization**              |
|                                                                                                                                                                                                                                       | - ``config.json`` setting: ``.LocalizationSettings.DefaultClientLocale`` |
| Options: ``"bg"``, ``"de"``, ``"en"``, ``en-AU``, ``"es"``, ``"fa"``, ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``, ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``, ``"zh_CN"``, and ``"zh_TW"``.| - Environment variable: ``MM_LOCALIZATIONSETTINGS_DEFAULTCLIENTLOCALE``  |
|                                                                                                                                                                                                                                       |                                                                          |
| Default: ``"en"``.                                                                                                                                                                                                                    |                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

Available languages
~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| Sets the list of languages users see under **Settings > Display > Language**. If this field is blank, users see all supported languages. Newly supported languages are added automatically. If this field is not blank, it must contain the **Default client language**, in addition to any other languages.                                                                                                                           | - System Config path: **Site Configuration > Localization**           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        | - ``config.json`` setting: ``.LocalizationSettings.AvailableLocales`` |
| The ``config.json`` setting is a string that can contain the following comma-separated entries: ``"bg"``, ``"de"``, ``"en"``, ``en-AU``, ``"es"``, ``"fa"``, ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``, ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``, ``"zh_CN"``, and ``"zh_TW"``. For example, to limit the language choices to English (US) and Español, the string would be ``”en,es”``. | - Environment variable: ``MM_LOCALIZATIONSETTINGS_AVAILABLELOCALES``  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                        |                                                                       |
| Default: ``""``.                                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
|  **Note**: Servers which upgraded to v3.1 need to manually set this field blank to have new languages added by default.                                                                                                                                                                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

Users and teams
---------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Users and Teams**.

Max users per team
~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| The **Max users per team** is the maximum total number of users per team, including active and inactive users.                                                                                                                                                                                                                                                                | - System Config path: **Site Configuration > Users and teams**   |
|                                                                                                                                                                                                                                                                                                                                                                               | - ``config.json`` setting: ``.TeamSettings.MaxUsersPerTeam: 50`` |
| In Mattermost, a team of people should be a small organization with a specific goal. In the physical world, a team could sit around a single table. The default maximum (50) should be enough for most teams, but with appropriate `hardware <https://docs.mattermost.com/install/software-hardware-requirements.html>`__, this limit can be increased to thousands of users. | - Environment variable: ``MM_TEAMSETTINGS_MAXUSERSPERTEAM``      |
|                                                                                                                                                                                                                                                                                                                                                                               |                                                                  |
| `Channels <https://docs.mattermost.com/guides/channels.html>`__ are another way of organizing communications within teams on different topics.                                                                                                                                                                                                                                |                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                               |                                                                  |
| Numerical input. Default: 50.                                                                                                                                                                                                                                                                                                                                                 |                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+


Max channels per team
~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| The maximum number of channels per team, including both active and archived channels. | - System Config path: **Site Configuration > Users and teams**        |
|                                                                                       | - ``config.json`` setting: ``.TeamSettings.MaxChannelsPerTeam: 2000`` |
| Numerical input. Default: 2000.                                                       | - Environment variable: ``MM_TEAMSETTINGS_MAXCHANNELSPERTEAM``        |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------------------+

Enable users to open direct message channels with
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| This setting determines whether a user can open a direct message channel with anyone on the Mattermost server or only to members of the same team. This setting only affects the options presented in the user interface. It does not affect permissions on the backend server.                                                                                                                                                                                                                                          | - System Config path: **Site Configuration > Users and teams**       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | - ``config.json`` setting: ``.TeamSettings.RestrictDirectMessage``   |
| - **Any user on the Mattermost server**: **(Default)** Users can send a direct message to any user through the **Direct Messages > More** menu. ``config.json`` setting: ``"any"``                                                                                                                                                                                                                                                                                                                                       | - Environment variable: ``MM_TEAMSETTINGS_RESTRICTDIRECTMESSAGE``    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                      |
| - **Any member of the team**: The **Direct Messages > More** menu only allows direct messages to users on the same team. Pressing :kbd:`Ctrl` :kbd:`K` on Windows or Linux, or :kbd:`⌘` :kbd:`K` on Mac, only lists other users on the team currently being viewed. A user who is a member of multiple teams can only send direct messages to the team that is being viewed. However, the user can receive messages from other teams, regardless of the team currently being viewed. ``config.json`` setting: ``"team"`` |                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+

Teammate name display
~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| This setting determines how names appear in posts and under the **Direct Messages** list. Users can change this setting in their interface under **Settings > Display > Teammate Name Display**, unless this setting is locked by a System Admin (see **Lock teammate name display...**).                                                                                                            | - System Config path: **Site Configuration > Users and teams**   |
|                                                                                                                                                                                                                                                                                                                                                                                                      | - ``config.json`` setting: ``.TeamSettings.TeammateNameDisplay`` |
| - **Show username**: **(Default)** Displays usernames. ``config.json`` option: ``"username"``.                                                                                                                                                                                                                                                                                                       | - Environment variable: ``MM_TEAMSETTINGS_TEAMMATENAMEDISPLAY``  |
|                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                  |
| - **Show nickname if one exists...**: Displays the user’s nickname. If the user does not have a nickname, their full name is displayed. If the user does not have a full name, their username is displayed. ``config.json`` option: ``"nickname_full_name"``.                                                                                                                                        |                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                  |
| - **Show first and last name**: Displays the user’s full name. If the user does not have a full name, their username is displayed. This option is recommended when using `SAML <https://docs.mattermost.com/onboard/sso-saml.html>`__ or `LDAP <https://docs.mattermost.com/onboard/ad-ldap.html>`__ if first name and last name attributes are configured. ``config.json`` option: ``"full_name"``. |                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+


Lock teammate name display for all users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| This setting controls whether users can change settings under **Settings > Display > Teammate Name Display**. | - System Config path: **Site Configuration > Users and teams**              |
|                                                                                                               | - ``config.json`` setting: ``.TeamSettings.LockTeammateNameDisplay: false`` |
| - **true**: Users **cannot** change the Teammate Name Display                                                 | - Environment variable: ``MM_TEAMSETTINGS_LOCKTEAMMATENAMEDISPLAY``         |
| - **false**: **(Default)** Users can change the Teammate Name Display setting                                 |                                                                             |
|                                                                                                               |                                                                             |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

Allow users to view archived channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| - **true**: **(Default)** Allows users to access the content of archived channels of which they were a member. | - System Config path: **Site Configuration > Users and teams**                      |
| - **false**: Users are unable to access content in archived channels.                                          | - ``config.json`` setting: ``.TeamSettings.ExperimentalViewArchivedChannels: true`` |
|                                                                                                                | - Environment variable: ``MM_TEAMSETTINGS_EXPERIMENTALVIEWARCHIVEDCHANNELS``        |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

Show email address
~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| - **true**: **(Default)** All users can see the email addresses of every other user.        | - System Config path: **Site Configuration > Users and teams**         |
| - **false**: Hides email addresses in the client user interface, except from System Admins. | - ``config.json`` setting: ``.PrivacySettings.ShowEmailAddress: true`` |
|                                                                                             | - Environment variable: ``MM_PRIVACYSETTINGS_SHOWEMAILADDRESS``        |
+---------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

Show full name
~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| - **true**: **(Default)** Full names are visible to all users in the client user interface.                      | - System Config path: **Site Configuration > Users and teams**     |
| - **false**: Hides full names from all users, except System Admins. Username is shown in place of the full name. | - ``config.json`` setting: ``.PrivacySettings.ShowFullName: true`` |
|                                                                                                                  | - Environment variable: ``MM_PRIVACYSETTINGS_SHOWFULLNAME``        |
+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

Enable custom user statuses
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| - **true**: **(Default)** Users can set status messages and emojis that are visible to all users. | - System Config path: **Site Configuration > Users and teams**              |
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
| - **true**: **(Default)** Requires users to confirm when posting @channel, @all, @here, or group mentions in channels with more than 5 members.     | - System Config path: **Site Configuration > Notifications**                           |
| - **false**: No confirmation is required.                                                                                                           | - ``config.json`` setting: ``.TeamSettings.EnableConfirmNotificationsToChannel: true`` |
|                                                                                                                                                     | - Environment variable: ``MM_TEAMSETTINGS_ENABLECONFIRMNOTIFICATIONSTOCHANNEL``        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+

Enable email notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| - **true**: **(Default)** Enables automatic email notifications for posts.                                                                                                  | - System Config path: **Site Configuration > Notifications**                |
| - **false**: Disables notifications. A developer may choose this option to speed development by skipping email setup (see also the **Enable preview mode banner** setting). | - ``config.json`` setting: ``.EmailSettings.SendEmailNotifications: ture``  |
|                                                                                                                                                                             | - Environment variable: ``MM_EMAILSETTINGS_SENDEMAILNOTIFICATIONS``         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| **Notes**:                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| - If this setting is ``false``, and the SMTP server is set up, account-related emails (such as authentication messages) will be sent regardless of this setting.                                                                                          |
| - Email invitations and account deactivation emails are not affected by this setting.                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _email-preview-mode-banner-config:

Enable preview mode banner
~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| - **true**: **(Default)** When **Send email notifications** is ``false``, users see the Preview Mode banner. This banner alerts users that email notifications are disabled. | - System Config path: **Site Configuration > Notifications**                |
| - **false**: Preview Mode banner does not appear.                                                                                                                            | - ``config.json`` setting: ``.EmailSettings.EnablePreviewModeBanner: true`` |
|                                                                                                                                                                              | - Environment variable: ``MM_EMAILSETTINGS_ENABLEPREVIEWMODEBANNER``        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

Enable email batching
~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| - **true**: Multiple email notifications for mentions and direct messages over a given time period are batched into a single email. The time period can be customized by each user under **Settings > Notifications**. The default time period is 15 minutes.                | - System Config path: **Site Configuration > Notifications**             |
| - **false**: **(Default)** Emails will be sent for each mention or direct message.                                                                                                                                                                                           | - ``config.json`` setting: ``.EmailSettings.EnableEmailBatching: false`` |
|                                                                                                                                                                                                                                                                              | - Environment variable: ``MM_EMAILSETTINGS_ENABLEEMAILBATCHING``         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| **Notes**:                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                         |
| - Regardless of this setting, a user can turn off these notifications under **Settings > Notifications**.                                                                                                                                                                                                                                               |
| - The `Site Url <https://docs.mattermost.com/configure/environment-configuration-settings.html#site-url>`__ and `SMTP Email Server <https://docs.mattermost.com/configure/environment-configuration-settings.html#smtp-server>`__ must be configured to allow email batching.                                                                           |
| - Email batching in `High Availability Mode <https://docs.mattermost.com/configure/environment-configuration-settings.html#enable-high-availability-mode>`__ is planned, but not yet supported.                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Email notification contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| - **Send full message contents**: **(Default)** Email notifications include the full message contents, along with the name of the sender and the channel. ``config.json`` setting: ``"full"``                                                                                                 | - System Config path: **Site Configuration > Notifications**                |
|                                                                                                                                                                                                                                                                                               | - ``config.json`` setting: ``.EmailSettings.EmailNotificationContentsType`` |
| - **Send generic description with only sender name**: Only the name of the sender and team name are included in email notifications. Use this option if Mattermost contains confidential information and policy dictates it cannot be stored in email. ``config.json`` setting: ``"generic"`` | - Environment variable: ``MM_EMAILSETTINGS_EMAILNOTIFICATIONCONTENTSTYPE``  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

Notification display name
~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Display name for email notifications sent from the Mattermost system.                                  | - System Config path: **Site Configuration > Notifications** |
|                                                                                                        | - ``config.json`` setting: ``.EmailSettings.FeedbackName``   |
| String input. No default setting. This field is required when changing settings in the System Console. | - Environment variable: ``MM_EMAILSETTINGS_FEEDBACKNAME``    |
+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

Notification from address
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| Email address for notification emails from the Mattermost system. This address should be monitored by a System Admin. | - System Config path: **Site Configuration > Notifications**  |
|                                                                                                                       | - ``config.json`` setting: ``.EmailSettings.FeedbackEmail``   |
| String input. Default is ``test@example.com``. This field is required when changing settings in the System Console.   | - Environment variable: ``MM_EMAILSETTINGS_FEEDBACKEMAIL``    |
+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

Support email address
~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Sets a user support (or feedback) email address that is displayed on email notifications and during the Getting Started tutorial. This address should be monitored by a System Admin. If no value is set, email notifications will not contain a way for users to request assistance. | - System Config path: **Site Configuration > Notifications** |
|                                                                                                                                                                                                                                                                                       | - ``config.json`` setting: ``.SupportSettings.SupportEmail`` |
| String input. Default is ``feedback@mattermost.com``. This field is required when changing settings in the System Console.                                                                                                                                                            | - Environment variable: ``MM_SUPPORTSETTINGS_SUPPORTEMAIL``  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

Notification reply-to address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+
| Email address used in the reply-to header when sending notification emails from the Mattermost system. This address should be monitored by a System Admin. | - System Config path: **Site Configuration > Notifications**   |
|                                                                                                                                                            | - ``config.json`` setting: ``.EmailSettings.ReplyToAddress``   |
| String input. Default is ``test@example.com``.                                                                                                             | - Environment variable: ``MM_EMAILSETTINGS_REPLYTOADDRESS``    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+

Notification footer mailing address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| Optional setting to include the organization’s name and mailing address in the footer of email notifications. If not set, nothing will appear. | - System Config path: **Site Configuration > Notifications**         |
|                                                                                                                                                | - ``config.json`` setting: ``.EmailSettings.FeedbackOrganization``   |
| String input.                                                                                                                                  | - Environment variable: ``MM_EMAILSETTINGS_FEEDBACKORGANIZATION``    |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+

Push notification contents
~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| - **Generic description with only sender name**: Push notifications include the sender’s name, but not the channel name or message contents. ``config.json`` setting: ``"generic_no_channel"``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | - System Config path: **Site Configuration > Notifications**           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | - ``config.json`` setting: ``.EmailSettings.PushNotificationContents`` |
| - **Generic description with sender and channel names**: **(Default)** Push notifications include the name of the sender and channel, but not the message contents. ``config.json`` setting: ``"generic"``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | - Environment variable: ``MM_EMAILSETTINGS_PUSHNOTIFICATIONCONTENTS``  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                        |
| - **Full message content sent in the notification payload**: Includes the message contents in the push notification payload, which may be sent through `Apple’s Push Notification service <https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1>`__ or `Google’s Firebase Cloud Messaging <https://firebase.google.com/docs/cloud-messaging>`__ . It is **highly recommended** this option only be used with an ``https`` protocol to encrypt the connection and protect confidential information. ``config.json`` setting: ``"full"``                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |                                                                        |
| - **Full message content fetched from the server on receipt** (*Available in Mattermost Enterprise*): The notification payload contains no message content. Instead it contains a unique message ID used to fetch message content from the Mattermost server when a push notification is received via a `notification service app extension <https://developer.apple.com/documentation/usernotifications/modifying_content_in_newly_delivered_notifications>`__ on iOS or `an expandable notification pattern <https://developer.android.com/training/notify-user/expanded>`__ on Android. If the server cannot be reached, a generic push notification is displayed without message content or sender name. For customers who wrap the Mattermost mobile application in a secure container, such as BlackBerry Dynamics, MobileIron, or AirWatch, the container must fetch the message contents using the unique message ID when push notifications are received. If the container is unable to execute the fetch, the push notification contents cannot be received by the customer's mobile application without passing the message contents through Apple's or Google's notification service. ``config.json`` setting: ``"id_loaded"`` |                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

----

Announcement banner
-------------------

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Announcement Banner**.

Enable announcement banner
~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| - **true**: Enable an announcement banner that is displayed across the top of the screen for all teams.              | - System Config path: **Site Configuration > Announcement banner**       |
|                                                                                                                      | - ``config.json`` setting: ``.AnnouncementSettings.EnableBanner: false`` |
| - **false**: **(Default)** Disable the announcement banner.                                                          | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_ENABLEBANNER``         |
+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

Banner text
~~~~~~~~~~~

+------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| The text of the announcement banner. If no text is provided, the banner will not appear. | - System Config path: **Site Configuration > Announcement banner**|
|                                                                                          | - ``config.json`` setting: ``.AnnouncementSettings.BannerText``   |
| String input.                                                                            | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_BANNERTEXT``    |
+------------------------------------------------------------------------------------------+-------------------------------------------------------------------+

Banner color
~~~~~~~~~~~~~

+--------------------------------------------------+-----------------------------------------------------------------------------+
| The background color of the announcement banner. | - System Config path: **Site Configuration > Announcement banner**          |
|                                                  | - ``config.json`` setting: ``.AnnouncementSettings.BannerColor: "#f2a93b"`` |
| String input of a CSS color value.               | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_BANNERCOLOR``             |
+--------------------------------------------------+-----------------------------------------------------------------------------+

Banner text color
~~~~~~~~~~~~~~~~~

+---------------------------------------------------+---------------------------------------------------------------------------------+
| The color of the text in the announcement banner. | - System Config path: **Site Configuration > Announcement banner**              |
|                                                   | - ``config.json`` setting: ``.AnnouncementSettings.BannerTextColor: "#333333"`` |
| String input of a CSS color value.                | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_BANNERTEXTCOLOR``             |
+---------------------------------------------------+---------------------------------------------------------------------------------+

Allow banner dismissal
~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| - **true**: **(Default)** Users can dismiss the banner. The banner will re-appear the next time the user logs in. The banner will also re-appear if the text is updated, or a System Admin disables the banner and re-enables it. | - System Config path: **Site Configuration > Announcement banner**              |
|                                                                                                                                                                                                                                   | - ``config.json`` setting: ``.AnnouncementSettings.AllowBannerDismissal: true`` |
| - **false**: Users cannot dismiss the banner.                                                                                                                                                                                     | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_ALLOWBANNERDISMISSAL``        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+

----

Emoji
------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Emoji**.

Enable emoji picker
~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| - **true**: **(Default)** Enables an emoji picker when composing messages and for message reactions. | - System Config path: **Site Configuration > Emoji**                    |
| - **false**: Disables the emoji picker in message composition and reactions.                         | - ``config.json`` setting: ``.ServiceSettings.EnableEmojiPicker: true`` |
|                                                                                                      | - Environment variable: ``MM_SERVICESETTINGS_ENABLEEMOJIPICKER``        |
+------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

Enable custom emoji
~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| - **true**: Allows users to add emojis through a **Custom Emoji** option in the emoji picker. Emojis can be GIF, PNG, or JPG files up to 1 MB. | - System Config path: **Site Configuration > Emoji**                     |
| - **false**: **(Default)** Disables custom emojis.                                                                                             | - ``config.json`` setting: ``.ServiceSettings.EnableCustomEmoji: false`` |
|                                                                                                                                                | - Environment variable: ``MM_SERVICESETTINGS_ENABLECUSTOMEMOJI``         |
+------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: Too many custom emojis can slow your server’s performance.                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| - **true**: **(Default)** Enables automatic following for all threads that a user starts, or in which the user participates or is mentioned. A **Threads** table in the database tracks threads and thread participants. A **ThreadMembership** table tracks followed threads for each user and whether the thread is read or unread. | - System Config path: **Site Configuration > Posts**                   |
|                                                                                                                                                                                                                                                                                                                                       | - ``config.json`` setting: ``.ServiceSettings.ThreadAutoFollow: true`` |
| - **false**: Disables automatic following of threads.                                                                                                                                                                                                                                                                                 | - Environment variable: ``MM_SERVICESETTINGS_THREADAUTOFOLLOW``        |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| **Notes**:                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| - This setting **must** be enabled for `Collapsed Reply Threads <https://docs.mattermost.com/channels/organize-conversations.html>`__ to function. See the `administrator’s guide to enabling Collapsed Reply Threads <https://support.mattermost.com/hc/en-us/articles/6880701948564>`__ for details.                                                                                                         |
| - Enabling this setting does not automatically follow threads based on previous user actions. For example, threads a user participated in prior to enabling this setting won't be automatically followed, unless the user adds a new comment or is mentioned in the thread.                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Collapsed reply threads
~~~~~~~~~~~~~~~~~~~~~~~

.. important::

    Customers upgrading to v7.0 must review the `administrator’s guide to enabling Collapsed Reply Threads <https://support.mattermost.com/hc/en-us/articles/6880701948564>`__ prior to enabling this functionality.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| - **Always On**: **(Default)** Enables `Collapsed Reply Threads <https://docs.mattermost.com/channels/organize-conversations.html>`__ on the server and for all users. This is the recommended configuration for optimal user experience and to ensure consistency in how users read and respond to threaded conversations. ``config.json`` setting: ``"always_on"`` | - System Config path: **Site Configuration > Posts**               |
| - **Default On**: Enables Collapsed Reply Threads on the server and for all users. Users can choose to `disable Collapsed Reply Threads <https://docs.mattermost.com/channels/channels-settings.html#collapsed-reply-threads>`__ for their Mattermost account in **Settings > Display > Collapsed Reply Threads**. ``config.json`` setting: ``"default_on"``         | - ``config.json`` setting: ``.ServiceSettings.CollapsedThreads``   |
| - **Default Off**: Enables Collapsed Reply Threads on the server but **not** for users. Users can choose to `enable Collapsed Reply Threads <https://docs.mattermost.com/channels/channels-settings.html#collapsed-reply-threads>`__ for their Mattermost account in **Settings > Display > Collapsed Reply Threads**. ``config.json`` setting: ``"default_off"``    | - Environment variable: ``MM_SERVICESETTINGS_COLLAPSEDTHREADS``    |
| - **Disabled**: Users cannot enable Collapsed Reply Threads. ``config.json`` setting: ``"disabled"``                                                                                                                                                                                                                                                                 |                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

Enable website link previews
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| - **true**: The server generates a preview of the first website, image, or YouTube video linked in a message. Users can disable website previews, but not image or YouTube previews, under **Settings > Display > Website Link Previews**. | - System Config path: **Site Configuration > Posts**                     |
| - **false**: **(Default)** All previews are disabled and the server does not request metadata for any links contained in messages.                                                                                                         | - ``config.json`` setting: ``.ServiceSettings.EnableLinkPreviews: true`` |
|                                                                                                                                                                                                                                            | - Environment variable: ``MM_SERVICESETTINGS_ENABLELINKPREVIEWS``        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: The server must be connected to the internet to generate previews. This connection can be established through a `firewall or outbound proxy <https://docs.mattermost.com/install/outbound-proxy.html>`__ if necessary.                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Disable link previews for specific domains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| Use this setting to disable previews of links for specific domains.                                      | - System Config path: **Site Configuration > Posts**                   |
|                                                                                                          | - ``config.json`` setting: ``.ServiceSettings.RestrictLinkPreviews``   |
| String input of a comma-separated list of domains, for example: ``"mattermost.com, images.example.com"`` | - Environment variable: ``MM_SERVICESETTINGS_RESTRICTLINKPREVIEWS``    |
+----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

Enable message link previews
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| - **true**: **(Default)** `Share links to Mattermost messages <https://docs.mattermost.com/channels/share-links.html>`__ will generate a preview for any users that have access to the original message. | - System Config path: **Site Configuration > Posts**                          |
| - **false**: Share links do not generate a preview.                                                                                                                                                      | - ``config.json`` setting: ``.ServiceSettings.EnablePermalinkPreviews: true`` |
|                                                                                                                                                                                                          | - Environment variable: ``MM_SERVICESETTINGS_ENABLEPERMALINKPREVIEWS``        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

Enable SVGs
~~~~~~~~~~~

+-------------------------------------------------------------------------------+------------------------------------------------------------------+
| - **true**: **(Default)** Enables previews of SVG files attached to messages. | - **Site Configuration > Posts**                                 |
| - **false**: Disables previews of SVG files.                                  | - ``config.json`` setting: ``.ServiceSettings.EnableSVGs: true`` |
|                                                                               | - Environment variable: ``MM_SERVICESETTINGS_ENABLESVGS``        |
+-------------------------------------------------------------------------------+------------------------------------------------------------------+

Enable LaTeX code block rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| - **true**: **(Default)** Enables rendering of `LaTeX in code blocks <https://docs.mattermost.com/channels/format-messages.html#math-formulas>`__. | - System Config path: **Site Configuration > Posts**              |
| - **false**: Disables rendering in blocks. Instead, LaTeX code is highlighted.                                                                     | - ``config.json`` setting: ``.ServiceSettings.EnableLatex: true`` |
|                                                                                                                                                    | - Environment variable: ``MM_SERVICESETTINGS_ENABLELATEX``        |
+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| **Warning**: Choose **false** to prevent Mattermost from crashing due to code outgrowing its assigned memory when it is rendered.                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable inline LaTeX rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| - **true**: **(Default)** Enables rendering of `LaTeX in message text <https://docs.mattermost.com/channels/format-messages.html#math-formulas>`__.                                                                | - System Config path: **Site Configuration > Posts**                    |
| - **false**: Disables inline rendering of LaTex. Instead, LaTeX in message text is highlighted. LaTex can also be rendered in a code block, if that feature is enabled. See **Enable LaTeX code block rendering**. | - ``config.json`` setting: ``.ServiceSettings.EnableInlineLatex: true`` |
|                                                                                                                                                                                                                    | - Environment variable: ``MM_SERVICESETTINGS_ENABLEINLINELATEX``        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| **Warning**: Choose **false** to prevent Mattermost from crashing due to code outgrowing its assigned memory when it is rendered.                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Custom URL schemes
~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| A list of URL schemes that will automatically create a link in message text, for example: ``["git", "smtp"]``. These schemes always create links: ``http``, ``https``, ``ftp``, ``tel``, and ``mailto``. | - System Config path: **Site Configuration > Posts**                  |
|                                                                                                                                                                                                          | - ``config.json`` setting: ``.DisplaySettings.CustomURLSchemes: []``  |
| ``config.json`` setting: an array of strings                                                                                                                                                             | - Environment variable: ``MM_DISPLAYSETTINGS_CUSTOMURLSCHEMES``       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+

Google API key
~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| If a key is provided in this setting, Mattermost displays titles of embedded YouTube videos and detects if a video is no longer available. Setting a key should also prevent Google from throttling access to embedded videos that receive a high number of views. | - System Config path: **Site Configuration > Posts**               |
|                                                                                                                                                                                                                                                                    | - ``config.json`` setting: ``.ServiceSettings.GoogleDeveloperKey`` |
| String input.                                                                                                                                                                                                                                                      | - Environment variable: ``MM_SERVICESETTINGS_GOOGLEDEVELOPERKEY``  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| **Notes**:                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                         |
| - The key must have the YouTube Data API added as a service.                                                                                                                                                                                                                                                                            |
| - This key is used in client-side Javascript.                                                                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

----

File sharing and downloads
---------------------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > File Sharing and Downloads**.

Allow file sharing
~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| - **true**: **(Default)** Allows users to attach files to messages.                                                                                     | - System Config path: **Site Configuration > File Sharing and Downloads** |
| - **false**: Prevents users from attaching files (including images) to a message. This affects users on all clients and devices, including mobile apps. | - ``config.json`` setting: ``.FileSettings.EnableFileAttachments: true``  |
|                                                                                                                                                         | - Environment variable: ``MM_FILESETTINGS_ENABLEFILEATTACHMENTS``         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+

Allow file uploads on mobile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| - **true**: **(Default)** Allows users to attach files to messages from mobile apps.              |  - System Config path: **Site Configuration > File Sharing and Downloads** |
| - **false**: Prevents users from attaching files (including images) to messages from mobile apps. | - ``config.json`` setting: ``.FileSettings.EnableMobileUpload: true``      |
|                                                                                                   | - Environment variable: ``MM_FILESETTINGS_ENABLEMOBILEUPLOAD``             |
+---------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+

Allow file downloads on mobile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| - **true**: **(Default)** Enables file downloads on mobile apps.                                               | - System Config path: **Site Configuration > File sharing and downloads** |
| - **false**: Disables file downloads on mobile apps. Users can still download files from a mobile web browser. | - ``config.json`` setting: ``.FileSettings.EnableMobileDownload: true``   |
|                                                                                                                | - Environment variable: ``MM_FILESETTINGS_ENABLEMOBILEDOWNLOAD``          |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+

----

Public Links
------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Public Links**.

Enable public file links
~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| - **true**: Allows users to create `public links <https://docs.mattermost.com/channels/share-files-in-messages.html#share-public-links>`__ to files attached to Mattermost messages.          | - System Config path: **Site Configuration > Public Links**           |
| - **false**: **(Default)** Prevents users from creating public links to files and disables all previously created links.                                                                      | - ``config.json`` setting: ``.FileSettings.EnablePublicLink: false``  |
|                                                                                                                                                                                               | - Environment variable: ``MM_FILESETTINGS_ENABLEPUBLICLINK``          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| **Note**: When set to ``false``, anyone who tries to visit a previously created public link will receive an error message. If the setting is returned to ``true``, previously created links will be accessible, unless the **Public link salt** has been regenerated. |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Public link salt
~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| 32-character salt added to the URL of public file links. Changing this setting will **invalidate** all previously generated links. The salt is randomly generated when Mattermost is installed, and can be regenerated by selecting **Regenerate** in the System Console. | - System Config path: **Site Configuration > Public Links**     |
|                                                                                                                                                                                                                                                                           | - ``config.json`` setting: ``.FileSettings.PublicLinkSalt``     |
| String input.                                                                                                                                                                                                                                                             | - Environment variable: ``MM_FILESETTINGS_PUBLICLINKSALT``      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+

----

Notices
--------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Notices**.

Enable admin notices
~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| - **true**: **(Default)** System Admins will receive `in-product notices <https://docs.mattermost.com/manage/in-product-notices.html>`__ about server upgrades and administration features. | - System Config path: **Site Configuration > Notices** -                         |
|                                                                                                                                                                                             | - ``config.json`` setting: ``.AnnouncementSettings.AdminNoticesEnabled: true``   |
| - **false**: System Admins will not receive specific notices. Admins will still receive notices for all users (see **Enable end user notices**)                                             | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_ADMINNOTICESENABLED``          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

Enable end user notices
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| - **true**: **(Default)** All users receive `in-product notices <https://docs.mattermost.com/manage/in-product-notices.html>`__ about client upgrades and end user features.   | - System Config path: **Site Configuration > Notices**                        |
| - **false**: Users will not receive in-product notices.                                                                                                                        | - ``config.json`` setting: ``.AnnouncementSettings.UserNoticesEnabled: true`` |
|                                                                                                                                                                                | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_USERNOTICESENABLED``        |
|                                                                                                                                                                                |                                                                               |
|                                                                                                                                                                                |                                                                               |
|                                                                                                                                                                                |                                                                               |
|                                                                                                                                                                                |                                                                               |
|                                                                                                                                                                                |                                                                               |
|                                                                                                                                                                                |                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
