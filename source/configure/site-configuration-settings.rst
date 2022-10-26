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

+--------------------------------------------------------------------+--------------------------------------------------------------+
|Name of the site shown in login screens and UI.                     | - System Config path: **Site Configuration > Customization** |
|                                                                    | - ``config.json`` setting: ``.TeamSettings.SiteName``        |
|String input. Maximum 30 characters. Default is ``Mattermost``.     | - Environment variable: ``MM_TEAMSETTINGS_SITENAME``         |
+--------------------------------------------------------------------+--------------------------------------------------------------+

Site description
~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+--------------------------------------------------------------------+
|Displays as a title above the login form. When not specified, the   | - System Config path: **Site Configuration > Customization**       |
|phrase "Log in" is displayed.                                       | - ``config.json`` setting: ``.TeamSettings.CustomDescriptionText`` |
|                                                                    | - Environment variable: ``MM_TEAMSETTINGS_CUSTOMDESCRIPTIONTEXT``  |
|String input.                                                       |                                                                    |
+--------------------------------------------------------------------+--------------------------------------------------------------------+

Enable custom branding
~~~~~~~~~~~~~~~~~~~~~~

*This feature was moved to Team Edition in Mattermost v5.0, released June 16th, 2018. Prior to v5.0, this feature is available in legacy Enterprise Edition E10 and E20.*

+-------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| - **true**: Enables the display of a custom image and text on the login page (see settings for **Custom brand image** and **Custom brand text**)| - System Config path: **Site Configuration > Customization**          |
| - **false: (Default)** Custom branding is disabled.                                                                                             | - ``config.json`` setting: ``.TeamSettings.EnableCustomBrand: false`` |
|                                                                                                                                                 | - Environment variable: ``MM_TEAMSETTINGS_ENABLECUSTOMBRAND``         |
|                                                                                                                                                 |                                                                       |
|                                                                                                                                                 |                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
 								     	     
Custom brand image
~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+-----------------------------------------------------------------+
|Upload a JPG image for display on the login page. The image must be | - System Config path: **Site Configuration > Customization**    |
|uploaded through the System Console. The file should be **smaller   | - ``config.json`` setting: N/A                                  |
|than 2 MB**.                                                        | - Environment variable: N/A                                     |
|                                                                    |                                                                 |
|**Enable custom branding** must be set to ``true`` to display the   |                                                                 |
|image.                                                              |                                                                 |
|                                                                    |                                                                 |
+--------------------------------------------------------------------+-----------------------------------------------------------------+

Custom brand text
~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------+--------------------------------------------------------------+
|Text that will be shown below the **Custom brand image** on left side of | - System Config path: **Site Configuration > Customization** |
|login page. You can format this text using the same `Markdown formatting | - ``config.json`` setting: ``.TeamSettings.CustomBrandText`` |
|<https://docs.mattermost.com/help/messaging/formatting-text.html>`__ as  | - Environment variable: ``MM_TEAMSETTINGS_CUSTOMBRANDTEXT``  |
|in Mattermost messages.                                                  |                                                              |
|                                                                         |                                                              |
|String input. Maximum 500 characters. **Enable custom branding** must be |                                                              |
|set to ``true`` to display the image.                                    |                                                              |
|                                                                         |                                                              |
+-------------------------------------------------------------------------+--------------------------------------------------------------+

Enable Ask Community link
~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| - **true: (Default)** **Ask the community** link to the `Mattermost Community <https://mattermost.com/pl/default-ask-mattermost-community>`__ appears under the **Help** menu in the channel header. | - System Config path: **Site Configuration > Customization**                 |
| - **false**: The link is not visible to users.                                                                                                                                                       | - ``config.json`` setting: ``.SupportSettings.EnableAskCommunityLink: true`` |
|                                                                                                                                                                                                      | - Environment variable: ``MM_SUPPORTSETTINGS_ENABLEASKCOMMUNITYLINK``        |
|The link does not appear on mobile apps.                                                                                                                                                              |                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+

Help link
~~~~~~~~~

+-------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
|The URL for the Help link on the login page, sign-up pages, and the Help | - System Config path: **Site Configuration > Customization**                      |
|Resources link under the **Help** menu. If this field is empty, the link | - ``config.json`` setting: ``.SupportSettings.HelpLink``                          |
|does not appear.                                                         | - Environment variable: ``MM_SUPPORTSETTINGS_HELPLINK``                           |
|                                                                         |                                                                                   |
|String input. Default is ``https://about.mattermost.com/default-help/``. |                                                                                   |
|                                                                         |                                                                                   |
+-------------------------------------------------------------------------+-----------------------------------------------------------------------------------+

Terms of Use link
~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
|The URL for the Terms of Use of a self-hosted site. A link to the terms appears at the      | - System Config path: **Site Configuration > Customization**        |
|bottom of the sign-up and login pages.                                                      | - ``config.json`` setting: ``.SupportSettings.TermsOfServiceLink``  |
|                                                                                            | - Environment variable: ``MM_SUPPORTSETTINGS_TERMSOFSERVICELINK``   |
| The default URL links to a `Terms of Use <https://about.mattermost.com/default-terms>`__   |                                                                     |
|page hosted on ``mattermost.com``. This includes the Mattermost Acceptable Use Policy       |                                                                     |
|explaining the terms under which Mattermost software is provided to end users. If you change|                                                                     |
|the default link to add your own terms for using the service you provide, your new terms    |                                                                     |
|**must include a link** to the default terms so end users are aware of the Mattermost       |                                                                     |
|Acceptable Use Policy.                                                                      |                                                                     |
|                                                                                            |                                                                     |
|From Mattermost v5.17, this setting doesn't change the terms of use link displayed in the   |                                                                     |
|**About Mattermost** dialog, which refers to the Mattermost Terms of Use.                   |                                                                     |
|                                                                                            |                                                                     |
|String input. Default is ``https://about.mattermost.com/default-terms/``.                   |                                                                     |
|                                                                                            |                                                                     |
|                                                                                            |                                                                     |
|                                                                                            |                                                                     |
|                                                                                            |                                                                     |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

Privacy Policy link
~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:
 		
+----------------------------------------------------------------------------------+-------------------------------------------------------------------+
|The URL for the Privacy Policy of a self-hosted site. A link to the policy appears| - System Config path: **Site Configuration > Customization**      |
|at the bottom of the sign-up and login pages. If this field is empty, the link    | - ``config.json`` setting: ``.SupportSettings.PrivacyPolicyLink`` |
|does not appear.                                                                  | - Environment variable: ``MM_SUPPORTSETTINGS_PRIVACYPOLICYLINK``  |
|                                                                                  |                                                                   |
|In version 5.17 and later, this setting does not change the Privacy Policy link in|                                                                   |
|the **About Mattermost** dialog, which refers to the Mattermost Privacy Policy.   |                                                                   |
|                                                                                  |                                                                   |
|String input. Default is ``https://about.mattermost.com/default-privacy-policy/``.|                                                                   |
|                                                                                  |                                                                   |
|                                                                                  |                                                                   |
|                                                                                  |                                                                   |
|                                                                                  |                                                                   |
+----------------------------------------------------------------------------------+-------------------------------------------------------------------+

About link
~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-------------------------------------------------------------------------+--------------------------------------------------------------+
|The URL for general information about a self-hosted site. A link to the  | - System Config path: **Site Configuration > Customization** |               
|About page appears at the bottom of the sign-up and login pages. If this | - ``config.json`` setting: ``.SupportSettings.AboutLink``    |
|field is empty, the link does not appear.                                | - Environment variable: ``MM_SUPPORTSETTINGS_ABOUTLINK``     |
|                                                                         |                                                              |       
|String input. Default is ``https://about.mattermost.com/default-about/``.|                                                              |
|                                                                         |                                                              |
|                                                                         |                                                              |
+-------------------------------------------------------------------------+--------------------------------------------------------------+

Report a Problem link
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------------+--------------------------------------------------------------------+
|The URL for the Report a Problem link in the **Help** menu. If this field is     | - System Config path: **Site Configuration > Customization**       |
|empty, the link does not appear.                                                 | - ``config.json`` setting: ``.SupportSettings.ReportAProblemLink`` |
|                                                                                 | - Environment variable: ``MM_SUPPORTSETTINGS_REPORTAPROBLEMLINK``  |
| String input. Default is                                                        |                                                                    |
|``https://about.mattermost.com/default-report-a-problem``.                       |                                                                    |
|                                                                                 |                                                                    |
+---------------------------------------------------------------------------------+--------------------------------------------------------------------+

Mattermost apps download page link
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------+-------------------------------------------------------------------+
|The URL for the Download Apps link in the **Product** menu. If   | - System Config path: **Site Configuration > Customization**      |
|this field is empty, the link does not appear.                   | - ``config.json`` setting: ``.NativeAppSettings.AppDownloadLink`` |
|                                                                 | - Environment variable: ``MM_NATIVEAPPSETTINGS_APPDOWNLOADLINK``  |
|If you have an Enterprise App Store, use this setting to link to |                                                                   |
|the appropriate download page for your Mattermost apps.          |                                                                   |
|                                                                 |                                                                   |
|String input. Default is https://about.mattermost.com/downloads/.|                                                                   |
+-----------------------------------------------------------------+-------------------------------------------------------------------+

Android app download link
~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:+

+-----------------------------------------------------------------------------+--------------------------------------------------------------------------+
|The URL to download the Mattermost Android app. Users who access the site on | - System Config path: **Site Configuration > Customization**             |
|a mobile browser will be prompted to download the app through this link. If  | - ``config.json`` setting: ``.NativeAppSettings.AndroidAppDownloadLink`` |
|this field is empty, the prompt does not appear.                             | - Environment variable: ``MM_NATIVEAPPSETTINGS_ANDROIDAPPDOWNLOADLINK``  |
|                                                                             |                                                                          |
|If you have an Enterprise App Store, use this setting to link to the correct |                                                                          |
|app.                                                                         |                                                                          |
|                                                                             |                                                                          |
|String input. Default is                                                     |                                                                          |
|https://about.mattermost.com/mattermost-android-app/.                        |                                                                          |
+-----------------------------------------------------------------------------+--------------------------------------------------------------------------+

iOS app download link
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------+---------------------------------------------------------------------------+
|The URL to download the Mattermost iOS app. Users who access the site on a| - System Config path: **Site Configuration > Customization**              |
|mobile browser will be prompted to download the app through this link. If | - ``config.json`` setting: ``.NativeAppSettings.IosAppDownloadLink``      |
|this field is empty, the prompt does not appear.                          | - Environment variable: ``MM_NATIVEAPPSETTINGS_IOSAPPDOWNLOADLINK``       |
|                                                                          |                                                                           |
|If you use an Enterprise App Store, change this link to point to the      |                                                                           |
|correct app.                                                              |                                                                           |
|                                                                          |                                                                           |
|String input. Default is https://about.mattermost.com/mattermost-ios-app/.|                                                                           |
+--------------------------------------------------------------------------+---------------------------------------------------------------------------+

----

Localization
-------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Localization**.

Default server language
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|Default language for system messages and logs.                   | - System Config path: **Site Configuration > Localization**     |
|                                                                 | - This feature's ``config.json`` setting is                     |
|Changes to this setting require a server restart before taking   |``"DefaultServerLocale": "en"`` with options ``"bg"``, ``"de"``, |
|effect.                                                          |``"en"``, ``en-AU``, ``"es"``, ``"fa"``, ``"fr"``, ``"hu"``,     |
|                                                                 |``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``, ``"pt-br"``,   |
|                                                                 |``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``, ``"zh_CN"``, and |
|                                                                 |``"zh_TW"``.                                                     |
|                                                                 |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Default client language
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|Default language for newly-created users and pages where the user| - System Config path: **Site Configuration > Localization**     |
|hasn't logged in.                                                | - This feature's ``config.json`` setting is                     |
|                                                                 |``"DefaultClientLocale": "en"`` with options ``"bg"``, ``"de"``, |
|                                                                 |``"en"``, ``en-AU``, ``"es"``, ``"fa"``, ``"fr"``, ``"hu"``,     |
|                                                                 |``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``, ``"pt-br"``,   |
|                                                                 |``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``, ``"zh_CN"``, and |
|                                                                 |``"zh_TW"``.                                                     |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Available languages
~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|Sets which languages are available for users in **Settings >     | - System Config path: **Site Configuration > Localization**     |
|Display > Language**. Leave the field blank to add new languages | - This feature's ``config.json`` setting is                     |
|automatically by default, or add new languages using the dropdown|``"AvailableLocales": ""`` with options ``""``, ``"bg"``,        |
|menu manually as they become available. If you're manually adding|``"de"``, ``"en"``, ``en-AU``, ``"es"``, ``"fa"``, ``"fr"``,     |
|new languages, the **Default Client Language** must be added     |``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``,      |
|before saving the setting.                                       |``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``,     |
|                                                                 |``"zh_CN"``, and ``"zh_TW"``.                                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

.. note::
  Servers which upgraded to v3.1 need to manually set this field blank to have new languages added by default.
																			  
----

Users and teams
---------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Users and Teams**.

Max users per team
~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------+-----------------------------------------------------------------+
|The **Max Users Per Team** refers to the size of the "team site" which is    | - System Config path: **Site Configuration > Users and Teams**  |
|workspace a "team of people" inhabits. A team of people is considered a small| - This feature's ``config.json`` setting is ``"MaxUsersPerTeam":|
|organization where people work closely together towards a specific shared    |50`` with numerical input.                                       |
|goal and share the same etiquette. In the physical world, a team of people   |                                                                 |
|could typically be seated around a single table to have a meal and discuss   |                                                                 |
|their project.                                                               |                                                                 |
|                                                                             |                                                                 |
|The default maximum of 50 people, is at the extreme high end of a single team|                                                                 |
|of people. At this point organizations are more often "multiple teams of     |                                                                 |
|people" and investments in explicitly defining etiquette, such as `channel   |                                                                 |
|organization                                                                 |                                                                 |
|<https://docs.mattermost.com/messaging/organizing-mattermost.html>`__ in     |                                                                 |
|Enterprise Edition, are often used to scale the high levels of productivity  |                                                                 |
|found in a team of people using Mattermost to multiple teams of people.      |                                                                 |
|                                                                             |                                                                 |
|In terms of technical performance, `with appropriate hardware, Mattermost can|                                                                 |
|easily scale to hundreds and even thousands of users                         |                                                                 |
|<https://docs.mattermost.com/install/software-hardware-requirements.html>`__,|                                                                 |
|and provided the administrator believes the appropriate etiquette is in      |                                                                 |
|place, they should feel free to increase the default value.                  |                                                                 |
+-----------------------------------------------------------------------------+-----------------------------------------------------------------+


Max channels per team
~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|Maximum number of channels per team, including both active and   | - System Config path: **Site Configuration > Users and Teams**  |
|deleted channels.                                                | - This feature's ``config.json`` setting is                     |
|                                                                 |``"MaxChannelsPerTeam": 2000`` with numerical input.             |
|                                                                 |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Enable users to open direct message channels with
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**Any user on the Mattermost server**: The Direct Messages       | - System Config path: **Site Configuration > Users and Teams**  |
|**More** menu has the option to open a Direct Message channel    | - This feature's ``config.json`` setting is                     |
|with any user on the server.                                     |``"RestrictDirectMessage": "any"`` with options ``"any"`` and    |
|                                                                 |``"team"`` for the above settings, respectively.                 |
|**Any member of the team**: The Direct Messages **More** menu    |                                                                 |
|only has the option to open a Direct Message channel with users  |                                                                 |
|on the current team, and pressing :kbd:`Ctrl` :kbd:`K` on Windows|                                                                 |
|or Linux, or :kbd:`⌘` :kbd:`K` on Mac only lists users on the    |                                                                 |
|current team. If a user belongs to multiple teams, direct        |                                                                 |
|messages will still be received regardless of what team they are |                                                                 |
|currently on.                                                    |                                                                 |
|                                                                 |                                                                 |
|This setting only affects the UI, not permissions on the         |                                                                 |
|server. For instance, a direct message channel can be created    |                                                                 |
|with anyone on the server regardless of this setting.            |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Teammate name display
~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|Specifies how names are displayed in the user interface by       |  - System Config path: **Site Configuration > Users and Teams** |
|default. Please note that users can override this setting in     | - This feature's ``config.json`` setting is                     |
|**Settings > Display > Teammate Name Display**.                  |``"TeammateNameDisplay": "username"`` with options               |
|                                                                 |``"username"``, ``"nickname_full_name"``, and ``"full_name"`` for|
|**Show username**: Displays the user's username.                 |the above settings, respectively.                                |
|                                                                 |                                                                 |
|**Show nickname if one exists**: Displays the user's nickname. If|                                                                 |
|the user does not have a nickname, their full name is            |                                                                 |
|displayed. If the user does not have a full name, their username |                                                                 |
|is displayed.                                                    |                                                                 |
|                                                                 |                                                                 |
|**Show first and last name**: Displays the user's full name. If  |                                                                 |
|the user does not have a full name, their username is            |                                                                 |
|displayed. Recommended when using SAML or LDAP if first name and |                                                                 |
|last name attributes are configured.                             |                                                                 |
|                                                                 |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+


Lock teammate name display for all users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------+-----------------------------------------------------------------+
| **True**: Disables users' ability to change settings under      | - System Config path: **Site Configuration > Users and Teams**  |
|**Settings > Display > Teammate Name Display**.                  |                                                                 |
|                                                                 |                                                                 |
|**False**: Users can change how their teammate name displays.    |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Allow users to view archived channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**True**: Allows users to view, share, and search for content of | - System Config path: **Site Configuration > Users and Teams**  |
|channels that have been archived. Users can only view the content| - This feature's ``config.json`` setting is                     |
|in channels of which they were a member before the channel was   |``"ExperimentalViewArchivedChannels": true`` with options        |
|archived.                                                        |``true`` and ``false``.                                          |
|                                                                 |                                                                 |
|**False**: Users are unable to view, share, or search for content|                                                                 |
|of channels that have been archived.                             |                                                                 |
|                                                                 |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Show email address
~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**True**: Show email address of all users.                       | - System Config path: **Site Configuration > Users and Teams**  |
|                                                                 | - This feature's ``config.json`` setting is                     |
|**False**: Hide email address of users from other users in the   |``"ShowEmailAddress": true`` with options ``true`` and ``false``.|
|user interface, including Team Admins. This is designed for      |                                                                 |
|managing teams where users choose to keep their contact          |                                                                 |
|information private. System Admins will still be able to see     |                                                                 |
|email addresses in the UI.                                       |                                                                 |
|                                                                 |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Show full name
~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**True**: Show full name of all users.                           | - System Config path: **Site Configuration > Users and Teams**  |
|                                                                 | - This feature's ``config.json`` setting is ``"ShowFullName":   |
|**False**: Hide full name of users from other users including    |true`` with options ``true`` and ``false``.                      |
|Team Admins. This is designed for managing teams where users     |                                                                 |
|choose to keep their contact information private. System Admins  |                                                                 |
|will still be able to see full names in the UI.                  |                                                                 |
|                                                                 |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Enable custom user statuses
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**True**: Users can set descriptive status messages and optional | - System Config path: **Site Configuration > Users and Teams**  |
|status emojis that are visible to all users.                     | - This feature's ``config.json`` setting is                     |
|                                                                 |``"EnableCustomUserStatuses": true`` with options ``true`` and   |
|**False**: Users are unable to set custom user statuses.         |``false``.                                                       |
|                                                                 |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

----

Notifications
-------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Notifications**.

Show @channel, @all, or @here confirmation dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**True**: Users will be prompted to confirm when posting         | - System Config path: **Site Configuration > Notifications**    |
|@channel, @all, or @here in channels with over five members.     |This feature's ``config.json`` setting is                        |
|                                                                 |``"EnableConfirmNotificationsToChannel": true`` with options     |
|**False**: No confirmation is required.                          |``true`` and ``false``.                                          |
|                                                                 |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Enable email notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**True**: Enables sending of email notifications.                | - System Config path: **Site Configuration > Notifications**    |
|                                                                 |This                                                             |
|**False**: Disables email notifications for posts. This is useful|feature's ``config.json`` setting is ``"SendEmailNotifications": |
|for developers who may want to skip email setup for faster       |false`` with options ``true`` and ``false``.                     |
|development. In order to remove the **Preview Mode: Email        |                                                                 |
|notifications have not been configured** banner, you should also |                                                                 |
|set **Enable Preview Mode Banner** to ``false``.                 |                                                                 |
|                                                                 |                                                                 |
|If this setting is set to ``false`` and the SMTP server is set   |                                                                 |
|up, account related emails (such as password, email, username,   |                                                                 |
|user token, MFA, and other authentication related changes) will  |                                                                 |
|be sent regardless of this setting.                              |                                                                 |
|                                                                 |                                                                 |
|Email invitations and account deactivation emails are not        |                                                                 |
|affected by this setting.                                        |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

.. _email-preview-mode-banner-config:

Enable preview mode banner
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|                                                                 | - System Config path: **Site Configuration > Notifications**    |
|**True**: Preview Mode banner is displayed to all users when     |This                                                             |
|``"SendEmailNotifications": false`` so users are aware that email|feature's ``config.json`` setting is ``"EnablePreviewModeBanner":|
|notifications are disabled.                                      |true`` with options ``true`` and ``false``.                      |
|                                                                 |                                                                 |
|**False**: Preview Mode banner is not displayed to users.        |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Enable email batching
~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|**True**: Users can select how often to receive email notifications, and multiple notifications     | - System Config path: **Site Configuration > Notifications**    |
|within that timeframe will be combined into a single email. Batching will occur at a default        |                                                                 |
|interval of 15 minutes, configurable in **Settings > Notifications**.                               |                                                                 |
|                                                                                                    |                                                                 |
|.. note::                                                                                           |                                                                 |
|  - Email batching cannot be enabled unless the `SiteURL                                            |                                                                 |
|<https://docs.mattermost.com/configure/configuration-settings.html#site-url>`__ is configured and   |                                                                 |
|the `SMTP Email Server                                                                              |                                                                 |
|<https://docs.mattermost.com/configure/configuration-settings.html#smtp-email-server>`__ is         |                                                                 |
|configured.                                                                                         |                                                                 |
|  - Email batching in `High Availability mode                                                       |                                                                 |
|<https://docs.mattermost.com/configure/configuration-settings.html#enable-high-availability-mode>`__|                                                                 |
|is planned but not yet supported.                                                                   |                                                                 |
|                                                                                                    |                                                                 |
|**False**: If email notifications are enabled in **Settings**, emails will be sent individually for |                                                                 |
|every mention or direct message received.                                                           |                                                                 |
+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+



+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableEmailBatching": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------+

Email notification contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**Send full message contents**: Sender name and channel are      | - System Config path: **Site Configuration > Notifications**    |
|included in email notifications.                                 |This feature's ``config.json`` setting is                        |
|                                                                 |``"EmailNotificationContentsType": "full"`` with options         |
|**Send generic description with only sender name**: The team name|``"full"`` and ``"generic"`` for the above settings,             |
|and name of the person who sent the message, with no information |respectively.                                                    |
|about channel name or message contents, is included in email     |                                                                 |
|notifications. Typically used for compliance reasons if          |                                                                 |
|Mattermost contains confidential information and policy dictates |                                                                 |
|it cannot be stored in email.                                    |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+



Support email address
~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|Set an email address for feedback or support requests. This field|- System Config path: **Site Configuration > Notifications**     |
|is required, and if a value isn't set, email notifications don't | This                                                            |
|include a way for users to request assistance.                   |feature's ``config.json`` setting is ``"SupportEmail": ""`` with |
|                                                                 |string input.                                                    |
|To ensure that users can contact you for assistance, set this    |                                                                 |
|value to an email address your System Admin receives, such as    |                                                                 |
|``"support@yourcompany.com"``. This address is displayed on email|                                                                 |
|notifications and during the Getting Started tutorial.           |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Notification display name
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|Name displayed on email account used when sending notification   |- System Config path: **Site Configuration > Notifications**     |
|emails from Mattermost system. This field is required, and if a  | This                                                            |
|value isn't set, email notifications don't include a way for     |feature's ``config.json`` setting is ``"FeedbackName": ""`` with |
|users to request assistance.                                     |string input.                                                    |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Notification from address
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|Address displayed on email account used when sending notification|- System Config path: **Site Configuration > Notifications**     |
|emails from within Mattermost. This field is required, and if a  |                                                                 |
|value isn't set, email notifications don't include a way for     |                                                                 |
|users to request assistance.                                     |                                                                 |
|                                                                 |                                                                 |
|So you don't miss messages, please make sure to change this value|                                                                 |
|to an email your system administrator receives, such as          |                                                                 |
|``"admin@yourcompany.com"``.                                     |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+



+--------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FeedbackEmail": ""`` with string input. |
+--------------------------------------------------------------------------------------+

Notification reply-to address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------+----------------------------------------------------------------+
|Email address used in the Reply-To header when sending            |- System Config path: **Site Configuration > Notifications**    |
|notification emails from Mattermost.                              |                                                                |
|                                                                  |                                                                |
|                                                                  |                                                                |
+------------------------------------------------------------------+----------------------------------------------------------------+


+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ReplyToAddress": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Notification footer mailing address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|Organization name and mailing address displayed in the footer of |- System Config path: **Site Configuration > Notifications**     |
|email notifications from Mattermost, such as "© ABC Corporation, | This                                                            |
|565 Knight Way, Palo Alto, California, 94305, USA". If the field |feature's ``config.json`` setting is ``"FeedbackOrganization":   |
|is left empty, the organization name and mailing address will not|""`` with string input.                                          |
|be displayed.                                                    |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+


Push notification contents
~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
|**Generic description with only sender name**: Push notifications include only the name of the person who sent the message but no information about channel name or message|- System Config path: **Site Configuration > Notifications**     |
|text.                                                                                                                                                                      | This                                                            |
|                                                                                                                                                                           |feature's ``config.json`` setting is                             |
|**Generic description with sender and channel names**: Push notifications include names of users and channels but no specific details from the message text.               |``"PushNotificationContents": "full"`` with options              |
|                                                                                                                                                                           |``"generic_no_channel"``, ``"generic"``, ``"full"``, and         |
|**Full message content sent in the notification payload**: Selecting **Send full message snippet** sends excerpts from messages triggering notifications with specifics and|``"id_loaded"`` for the above settings, respectively.            |
|may include confidential information sent in messages. If your Push Notification Service is outside your firewall, it is HIGHLY RECOMMENDED this option only be used with  |                                                                 |
|an "https" protocol to encrypt the connection.                                                                                                                             |                                                                 |
|                                                                                                                                                                           |                                                                 |
|**Full message content fetched from the server on receipt** (*Available in Mattermost Enterprise*): The notification payload relayed through the `Apple Push Notification  |                                                                 |
|service                                                                                                                                                                    |                                                                 |
|<https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1>`__|                                                                 |
|or `Firebase Cloud Messaging <https://firebase.google.com/docs/cloud-messaging>`__ service contains no message content. Instead it contains a unique message ID used to    |                                                                 |
|fetch message content from the server when a push notification is received by a device via a `notification service app extension                                           |                                                                 |
|<https://developer.apple.com/documentation/usernotifications/modifying_content_in_newly_delivered_notifications>`__ on iOS or `an expandable notification pattern          |                                                                 |
|<https://developer.android.com/training/notify-user/expanded>`__ on Android. If the server cannot be reached, a generic push notification message is displayed without     |                                                                 |
|message content or sender name.                                                                                                                                            |                                                                 |
|                                                                                                                                                                           |                                                                 |
|For customers who choose to wrap the Mattermost mobile application in a secure container, such as BlackBerry Dynamics, MobileIron, AirWatch or other solutions, the        |                                                                 |
|container needs to execute the fetching of message contents from the unique message ID when push notification are received. If the container is unable to execute the      |                                                                 |
|fetch, the push notification contents cannot be received by the customer's mobile application without passing the message contents through either the `Apple Push          |                                                                 |
|Notification service                                                                                                                                                       |                                                                 |
|<https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1>`__|                                                                 |
|or `Firebase Cloud Messaging <https://firebase.google.com/docs/cloud-messaging>`__ service.                                                                                |                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+

----

Announcement banner
-------------------

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Announcement Banner**.

Enable announcement banner
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|Enable an announcement banner across all teams. The banner is    |- System Config path: **Site Configuration > Announcement        |
|displayed at the top of the screen and is the entire width of the|Banner**                                                         |
|screen. By default, users can dismiss the banner until you either|This feature's ``config.json`` setting is                        |
|change the text of the banner or until you re-enable the banner  |``"EnableBanner": false`` with options ``true`` and ``false``.   |
|after it has been disabled. You can prevent users from dismissing|                                                                 |
|the banner, and you can control the text color and the background|                                                                 |
|color.                                                           |                                                                 |
|                                                                 |                                                                 |
|**True**: Enable the announcement banner. The banner is displayed|                                                                 |
|only if ``BannerText`` has a value.                              |                                                                 |
|                                                                 |                                                                 |
|**False**: Disable the announcement banner.                      |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+


Banner text
~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|The text of the announcement banner.                             | - System Config path: **Site Configuration > Announcement       |
|                                                                 |Banner**                                                         |
|                                                                 |This feature's ``config.json`` setting is                        |
|                                                                 |``"BannerText": ""`` with string input.                          |
+-----------------------------------------------------------------+-----------------------------------------------------------------+


Banner color
~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|The background color of the announcement banner.                 | - System Config path: **Site Configuration > Announcement       |
|                                                                 |Banner**                                                         |
|                                                                 |This feature's ``config.json`` setting is                        |
|                                                                 |``"BannerColor": "#f2a93b"`` with string input.                  |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Banner text color
~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|The color of the text in the announcement banner.                |- System Config path: **Site Configuration > Announcement        |
|                                                                 |Banner**                                                         |
|                                                                 |This feature's ``config.json`` setting is                        |
|                                                                 |``"BannerTextColor": "#333333"`` with string input.              |
+-----------------------------------------------------------------+-----------------------------------------------------------------+


Allow banner dismissal
~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
|**True**: Users can dismiss the banner until the next time they  | - System Config path: **Site Configuration > Announcement       |
|log in or the banner is updated.                                 |Banner**                                                         |
|                                                                 |This feature's ``config.json`` setting is                        |
|**False**: The banner is permanently visible until it is turned  |``"AllowBannerDismissal": true`` with options ``true`` and       |
|off by the System Admin.                                         |``false``.                                                       |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

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
|emojis to add as reactions or use in messages. Enabling the emoji| This feature's ``config.json`` setting is ``"EnableEmojiPicker":|
|picker with a large number of custom emojis may slow down        |true`` with options ``true`` and ``false``.                      |
|performance.                                                     |                                                                 |
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
|where users can go to add custom emojis.                        |This                                                              |
|                                                                |feature's ``config.json`` setting is ``"EnableCustomEmoji": true``|
|**False**: Custom emojis are disabled.                          |with options ``true`` and ``false``.                              |
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
|<https://docs.mattermost.com/channels/organize-conversations.html>`__. See| This feature's ``config.json`` setting is ``"ThreadAutoFollow": |
|the `administrator’s guide to enabling Collapsed Reply Threads            |true`` with options ``true`` and ``false``.                      |
|<https://support.mattermost.com/hc/en-us/articles/6880701948564>`__       |                                                                 |
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
|communicating in threads and replying to messages. Collapsed Reply   | This                                                            |
|Threads is generally available in Mattermost Cloud and from          |feature's ``config.json`` setting is ``"CollapsedThreads":       |
|self-hosted Mattermost v7.0, and is enabled by default for all new   |always_on`` with options ``disabled``, ``default_off``,          |
|Mattermost deployments. See our `Organizing Conversations using      |``default_on``, and ``always_on``                                |
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
|available.                                                       |feature's ``config.json`` setting is ``"EnableLinkPreviews":     |
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
