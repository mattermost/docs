Site configuration settings
===========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Both self-hosted and Cloud admins can access the following configuration settings in the System Console by going to **Site Configuration**. Self-hosted admins can also edit the ``config.json`` file as described in the following tables. 

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

.. config:setting:: custom-name
  :displayname: Site name (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .TeamSettings.SiteName
  :environment: MM_TEAMSETTINGS_SITENAME
  :description: Name of the site shown in login screens and user interface. Default value is **Mattermost**.

Site name
~~~~~~~~~

+----------------------------------------------------------------+-----------------------------------------------------------------+
| Name of the site shown in login screens and user interface.    | - System Config path: **Site Configuration > Customization**    |
|                                                                | - ``config.json`` setting: ``.TeamSettings.SiteName``           |
| String input. Maximum 30 characters. Default is ``Mattermost`` | - Environment variable: ``MM_TEAMSETTINGS_SITENAME``            |
+----------------------------------------------------------------+-----------------------------------------------------------------+

.. config:setting:: custom-description
  :displayname: Site description (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .TeamSettings.CustomDescriptionText
  :environment: MM_TEAMSETTINGS_CUSTOMDESCRIPTIONTEXT
  :description: Text displayed above the login form. When not specified, the phrase **Log in** is displayed.

Site description
~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| Text displayed above the login form. When not specified, the phrase "Log in" is displayed. | - System Config path: **Site Configuration > Customization**       |
|                                                                                            | - ``config.json`` setting: ``.TeamSettings.CustomDescriptionText`` |
| String input.                                                                              | - Environment variable: ``MM_TEAMSETTINGS_CUSTOMDESCRIPTIONTEXT``  |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

.. config:setting:: custom-enablecustombranding
  :displayname: Enable custom branding (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .TeamSettings.EnableCustomBrand
  :environment: MM_TEAMSETTINGS_ENABLECUSTOMBRAND

  - **true**: Enables the display of a custom image and text on the login page
  - **false**: **(Default)** Custom branding is disabled

Enable custom branding
~~~~~~~~~~~~~~~~~~~~~~

*This feature is available in legacy Enterprise Edition E10 and E20.*

+--------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| - **true**: Enables the display of a custom image and text on the login page   | - System Config path: **Site Configuration > Customization**          |
| - **false**: **(Default)** Custom branding is disabled                         | - ``config.json`` setting: ``.TeamSettings.EnableCustomBrand: false`` |
|                                                                                | - Environment variable: ``MM_TEAMSETTINGS_ENABLECUSTOMBRAND``         |
| See also the `custom brand image <#custom-brand-image>`__ and                  |                                                                       |
| `custom brand text <#custom-brand-text>`__ configuration settings for more     |                                                                       |
| branding options.                                                              |                                                                       |
+--------------------------------------------------------------------------------+-----------------------------------------------------------------------+

.. config:setting:: custom-custombrandimage
  :displayname: Custom brand image (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: N/A
  :environment: N/A
  :description: A JPG image for display on the login page. The image **must** be uploaded through the System Console. The file should be **smaller than 2 MB**.

Custom brand image
~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| A JPG image for display on the login page. The image **must** be uploaded through the System Console. There is no ``config.json`` setting. The file should be **smaller than 2 MB**. | - System Config path: **Site Configuration > Customization** |
|                                                                                                                                                                                      | - ``config.json`` setting: N/A                               |
| `Enable custom branding <#enable-custom-branding>`__ must be set to **true** to display the image.                                                                                   | - Environment variable: N/A                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

.. config:setting:: custom-custombrandtext
  :displayname: Custom brand text (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .TeamSettings.CustomBrandText
  :environment: MM_TEAMSETTINGS_CUSTOMBRANDTEXT
  :description: Text that will be shown below the **Custom brand image** on the login page. Maximum 500 characters.

Custom brand text
~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Text that will be shown below the **Custom brand image** on the login page. You can format this text using the same `Markdown formatting <https://docs.mattermost.com/help/messaging/formatting-text.html>`__ as in Mattermost messages. | - System Config path: **Site Configuration > Customization** |
|                                                                                                                                                                                                                                          | - ``config.json`` setting: ``.TeamSettings.CustomBrandText`` |
| String input. Maximum 500 characters. `Enable custom branding <#enable-custom-branding>`__ must be set to **true** to display the text.                                                                                                  | - Environment variable: ``MM_TEAMSETTINGS_CUSTOMBRANDTEXT``  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

.. config:setting:: custom-enableaskcommunitylink
  :displayname: Enable Ask Community link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .SupportSettings.EnableAskCommunityLink
  :environment: MM_SUPPORTSETTINGS_ENABLEASKCOMMUNITYLINK

  - **true**: **(Default)** A link to the `Mattermost Community <https://mattermost.com/pl/default-ask-mattermost-community/>`__ appears as **Ask the community** under the **Help** menu in the channel header.
  - **false**: The link does not appear.

Enable Ask Community link
~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
|  - **true**: **(Default)** A link to the `Mattermost Community <https://mattermost.com/pl/default-ask-mattermost-community/>`__ appears as **Ask the community** under the **Help** menu in the channel header. |  - System Config path: **Site Configuration > Customization**                 |
|  - **false**: The link does not appear.                                                                                                                                                                         |  - ``config.json`` setting: ``.SupportSettings.EnableAskCommunityLink: true`` |
|                                                                                                                                                                                                                 |  - Environment variable: ``MM_SUPPORTSETTINGS_ENABLEASKCOMMUNITYLINK``        |
|  The link does not display on mobile apps.                                                                                                                                                                      |                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

.. config:setting:: custom-helplink
  :displayname: Help link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .SupportSettings.HelpLink
  :environment: MM_SUPPORTSETTINGS_HELPLINK

  This field sets the URL for the Help link on the login and sign-up pages, as well as the **Help Resources** link under the **Help** menu in the channel header.
  Default value is **https://about.mattermost.com/default-help/**.

Help link
~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| This field sets the URL for the Help link on the login and sign up pages, as well as the **Help Resources** link under the **Help** menu in the channel header.  | - System Config path: **Site Configuration > Customization** |
|                                                                                                                                                                  | - ``config.json`` setting: ``.SupportSettings.HelpLink``     |
| String input. Default is ``https://about.mattermost.com/default-help/``.                                                                                         | - Environment variable: ``MM_SUPPORTSETTINGS_HELPLINK``      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| **Note**: If this value is empty, the Help link is hidden on the login and sign up pages. However, the **Help Resources** link remains available under the **Help** menu.                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

.. config:setting:: custom-termsofuselink
  :displayname: Terms of Use link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .SupportSettings.TermsOfServiceLink
  :environment: MM_SUPPORTSETTINGS_TERMSOFSERVICELINK

  This field sets the URL for the Terms of Use of a self-hosted site. A link to the terms appears at the bottom of the sign-up and login pages.
  Default value is **https://about.mattermost.com/default-terms/**.

Terms of Use link
~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| This field sets the URL for the Terms of Use of a self-hosted site. A link to the terms appears at the bottom of the sign-up and login pages.                                                                                                                                                                                                                                                                                                   | - System Config path: **Site Configuration > Customization**       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 | - ``config.json`` setting: ``.SupportSettings.TermsOfServiceLink`` |
| The default URL links to a `Terms of Use <https://about.mattermost.com/default-terms/>`__ page hosted on ``mattermost.com``. This includes the Mattermost Acceptable Use Policy explaining the terms under which Mattermost software is provided to end users. If you change the default link to add your own terms, the new terms **must include a link** to the default terms so end users are aware of the Mattermost Acceptable Use Policy. | - Environment variable: ``MM_SUPPORTSETTINGS_TERMSOFSERVICELINK``  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                    |
| String input. Default is ``https://about.mattermost.com/default-terms/``.                                                                                                                                                                                                                                                                                                                                                                       |                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| **Note**: This setting doesn't change the **Terms of Use** link in the **About Mattermost** window.                                                                                                                                                                                                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: custom-privacypolicylink
  :displayname: Privacy Policy link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .SupportSettings.PrivacyPolicyLink
  :environment: MM_SUPPORTSETTINGS_PRIVACYPOLICYLINK

  This field sets the URL for the Privacy Policy of a self-hosted site. A link to the policy appears at the bottom of the sign-up and login pages.
  Default value is **https://about.mattermost.com/default-privacy-policy/**.

Privacy Policy link
~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| This field sets the URL for the Privacy Policy of a self-hosted site. A link to the policy appears at the bottom of the sign-up and login pages. If this field is empty, the link does not appear. | - System Config path: **Site Configuration > Customization**      |
|                                                                                                                                                                                                    | - ``config.json`` setting: ``.SupportSettings.PrivacyPolicyLink`` |
| String input. Default is ``https://about.mattermost.com/default-privacy-policy/``.                                                                                                                 | - Environment variable: ``MM_SUPPORTSETTINGS_PRIVACYPOLICYLINK``  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| **Note**: This setting does not change the **Privacy Policy** link in the **About Mattermost** window.                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: custom-aboutlink
  :displayname: About link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .SupportSettings.AboutLink
  :environment: MM_SUPPORTSETTINGS_ABOUTLINK

  This field sets the URL for a page containing general information about a self-hosted site. A link to the About page appears at the bottom of the sign-up and login pages.
  Default value is **https://about.mattermost.com/default-about/**.

About link
~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| This field sets the URL for a page containing general information about a self-hosted site. A link to the About page appears at the bottom of the sign-up and login pages. If this field is empty the link does not appear. | - System Config path: **Site Configuration > Customization**  |
|                                                                                                                                                                                                                             | - ``config.json`` setting: ``.SupportSettings.AboutLink``     |
| String input. Default is ``https://about.mattermost.com/default-about/``.                                                                                                                                                   | - Environment variable: ``MM_SUPPORTSETTINGS_ABOUTLINK``      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

.. config:setting:: custom-forgotpasswordurl
  :displayname: Forgot Password custom link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .SupportSettings.ForgetPasswordCustomLink
  :environment: MM_SUPPORTSETTINGS_FORGETPASSWORDCUSTOMLINK
  :description: Set a custom URL for the **Forgot Password** link on the Mattermost login page. Leave this field blank to use Mattermost's Password Reset workflow.

Forgot Password custom link
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| When the **Forgot Password** link is enabled on the Mattermost login page,    | - System Config path: **Site Configuration > Forgot password custom link**    |
| users are taken to a custom URL to recover or change their password.          | - ``config.json`` setting: ``.SupportSettings.ForgetPasswordCustomLink``      |
|                                                                               | - Environment variable: ``MM_SUPPORTSETTINGS_FORGETPASSWORDCUSTOMLINK``       |
| Leave this field blank to use Mattermost's Password Reset workflow.           |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Note**: You can control whether the **Forgot Password** link is visible or hidden by going to **Authentication > Password > Enable Forgot Password Link**.  |
| See the `configuration </configure/authentication-configuration-settings.html#enable-forgot-password-link>`__ documentation for details.                      |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

.. config:setting:: custom-reportaproblemlink
  :displayname: Report a Problem link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .SupportSettings.ReportAProblemLink
  :environment: MM_SUPPORTSETTINGS_REPORTAPROBLEMLINK
  :description: This field sets the URL for the **Report a Problem** link in the channel header **Help** menu.  Default value is **https://about.mattermost.com/default-report-a-problem**.

Report a Problem link
~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| This field sets the URL for the **Report a Problem** link in the channel header **Help** menu. If this field is empty the link does not appear. | - System Config path: **Site Configuration > Customization**       |
|                                                                                                                                                 | - ``config.json`` setting: ``.SupportSettings.ReportAProblemLink`` |
| String input. Default is ``https://about.mattermost.com/default-report-a-problem``.                                                             | - Environment variable: ``MM_SUPPORTSETTINGS_REPORTAPROBLEMLINK``  |
+-------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

.. config:setting:: custom-appdownloadlink
  :displayname: Mattermost apps download page link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .NativeAppSettings.AppDownloadLink
  :environment: MM_NATIVEAPPSETTINGS_APPDOWNLOADLINK
  :description: This field sets the URL for the Download Apps link in the **Product** menu. Default value is **https://about.mattermost.com/downloads/**.

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

.. config:setting:: custom-androiddownloadlink
  :displayname: Android app download link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .NativeAppSettings.AndroidAppDownloadLink
  :environment: MM_NATIVEAPPSETTINGS_ANDROIDAPPDOWNLOADLINK
  :description: This field sets the URL to download the Mattermost Android app. Default value is **https://about.mattermost.com/mattermost-android-app/**.

Android app download link
~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| This field sets the URL to download the Mattermost Android app. Users who access the Mattermost site on a mobile browser will be prompted to download the app through this link. If this field is empty, the prompt does not appear. | - System Config path: **Site Configuration > Customization**             |
|                                                                                                                                                                                                                                      | - ``config.json`` setting: ``.NativeAppSettings.AndroidAppDownloadLink`` |
| If you have an Enterprise App Store, link to your Android app.                                                                                                                                                                       | - Environment variable: ``MM_NATIVEAPPSETTINGS_ANDROIDAPPDOWNLOADLINK``  |
|                                                                                                                                                                                                                                      |                                                                          |
| String input. Default is ``https://about.mattermost.com/mattermost-android-app/``.                                                                                                                                                   |                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: custom-iosdownloadlink
  :displayname: iOS app download link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .NativeAppSettings.IosAppDownloadLink
  :environment: MM_NATIVEAPPSETTINGS_IOSAPPDOWNLOADLINK
  :description: This field sets the URL to download the Mattermost iOS app. Default value is **https://about.mattermost.com/mattermost-ios-app/**.

iOS app download link
~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| This field sets the URL to download the Mattermost iOS app. Users who access the site on a mobile browser will be prompted to download the app through this link. If this field is empty, the prompt does not appear. | - System Config path: **Site Configuration > Customization**           |
|                                                                                                                                                                                                                       | - ``config.json`` setting: ``.NativeAppSettings.IosAppDownloadLink``   |
| If you use an Enterprise App Store, link to your iOS app.                                                                                                                                                             | - Environment variable: ``MM_NATIVEAPPSETTINGS_IOSAPPDOWNLOADLINK``    |
|                                                                                                                                                                                                                       |                                                                        |
| String input. Default is ``https://about.mattermost.com/mattermost-ios-app/``.                                                                                                                                        |                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

----

Localization
------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Localization**. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: l10n-defaultserverlanguage
  :displayname: Default server language (Localization)
  :systemconsole: Site Configuration > Localization
  :configjson: .LocalizationSettings.DefaultServerLocale
  :environment: MM_LOCALIZATIONSETTINGS_DEFAULTSERVERLOCALE
  :description: The default language for system messages and logs. Default value is **en**.

Default server language
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| The default language for system messages and logs.                             | - System Config path: **Site Configuration > Localization**               |
|                                                                                | - ``config.json`` setting: ``.LocalizationSettings.DefaultServerLocale``  |
| Options: ``"bg"``, ``"de"``, ``"en"``, ``en-AU``, ``"es"``, ``"fa"``,          | - Environment variable: ``MM_LOCALIZATIONSETTINGS_DEFAULTSERVERLOCALE``   |
| ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``,          |                                                                           |
| ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``, ``"zh_CN"``,      |                                                                           |
| and ``"zh_TW"``.                                                               |                                                                           |
|                                                                                |                                                                           |
| Default is ``"en"``.                                                           |                                                                           |
+--------------------------------------------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: l10n-defaultclientlanguage
  :displayname: Default client language (Localization)
  :systemconsole: Site Configuration > Localization
  :configjson: .LocalizationSettings.DefaultClientLocale
  :environment: MM_LOCALIZATIONSETTINGS_DEFAULTCLIENTLOCALE
  :description: The default language for new users and pages where the user isn't logged in. Default value is **en**.

Default client language
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| The default language for new users and pages where the user isn't logged in.   | - System Config path: **Site Configuration > Localization**               |
|                                                                                | - ``config.json`` setting: ``.LocalizationSettings.DefaultClientLocale``  |
| Options: ``"bg"``, ``"de"``, ``"en"``, ``en-AU``, ``"es"``, ``"fa"``,          | - Environment variable: ``MM_LOCALIZATIONSETTINGS_DEFAULTCLIENTLOCALE``   |
| ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``,          |                                                                           |
| ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``, ``"zh_CN"``,      |                                                                           |
| and ``"zh_TW"``.                                                               |                                                                           |
|                                                                                |                                                                           |
| Default is ``"en"``.                                                           |                                                                           |
+--------------------------------------------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: l10n-availablelanguages
  :displayname: Available languages (Localization)
  :systemconsole: Site Configuration > Localization
  :configjson: .LocalizationSettings.AvailableLocales
  :environment: MM_LOCALIZATIONSETTINGS_AVAILABLELOCALES
  :description: Sets the list of languages users see under **Settings > Display > Language**. Default is **en**.

Available languages
~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| Sets the list of languages users see under **Settings > Display > Language**.  | - System Config path: **Site Configuration > Localization**               |
| If this field is left blank, users see all supported languages.                | - ``config.json`` setting: ``.LocalizationSettings.AvailableLocales``     |
| Newly supported languages are added automatically.                             | - Environment variable: ``MM_LOCALIZATIONSETTINGS_AVAILABLELOCALES``      |
| If this field is not blank, it must contain the **Default client language**,   |                                                                           |
| in addition to any other languages. For example, to limit the language         |                                                                           |
| choices to US English and Español (es), the string would be ``”en,es”``.       |                                                                           |
|                                                                                |                                                                           |
| Options: ``"bg"``, ``"de"``, ``"en"``, ``en-AU``, ``"es"``, ``"fa"``,          |                                                                           |
| ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``,          |                                                                           |
| ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``uk``, ``"zh_CN"``,      |                                                                           |
| and ``"zh_TW"``.                                                               |                                                                           |
|                                                                                |                                                                           |
| Default is ``"en"``.                                                           |                                                                           |
+--------------------------------------------------------------------------------+---------------------------------------------------------------------------+

----

Users and teams
---------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Users and Teams**.

.. config:setting:: users-maxusersperteam
  :displayname: Max users per team (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .TeamSettings.MaxUsersPerTeam
  :environment: MM_TEAMSETTINGS_MAXUSERSPERTEAM
  :description: The maximum total number of users per team, including active and inactive users. Default is **50** users per team.

Max users per team
~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------+-------------------------------------------------------------------+
| The **Max users per team** is the maximum total number of users per team,    | - System Config path: **Site Configuration > Users and Teams**    |
| including active and inactive users.                                         | - ``config.json`` setting: ``.TeamSettings.MaxUsersPerTeam: 50``  |
|                                                                              | - Environment variable: ``MM_TEAMSETTINGS_MAXUSERSPERTEAM``       |
| In Mattermost, a team of people should be a small organization with a        |                                                                   |
| specific goal. In the physical world, a team could sit around a single       |                                                                   |
| table. The default maximum (50) should be enough for most teams, but         |                                                                   |
| with appropriate `hardware <https://docs.mattermost.com/install/             |                                                                   |
| software-hardware-requirements.html>`__, this limit can be increased to      |                                                                   |
| thousands of users.                                                          |                                                                   |
|                                                                              |                                                                   |
| `Channels </collaborate/collaborate-within-channels.html>`__ are             |                                                                   |
| another way of organizing communications within teams on different topics.   |                                                                   |
|                                                                              |                                                                   |
| Numerical input. Default is **50** self-hosted deployments, and **10000**    |                                                                   |
| for Cloud deployments.                                                       |                                                                   |
+------------------------------------------------------------------------------+-------------------------------------------------------------------+

.. config:setting:: users-maxchannelsperteam
  :displayname: Max channels per team (Users and teams)
  :systemconsole: Site Configuration > Users and teams
  :configjson: .TeamSettings.MaxChannelsPerTeam
  :environment: MM_TEAMSETTINGS_MAXCHANNELSPERTEAM
  :description: The maximum number of channels per team, including both active and archived channels. Default is **2000** channels per team.

Max channels per team
~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| The maximum number of channels per team, including both active and archived channels. | - System Config path: **Site Configuration > Users and Teams**        |
|                                                                                       | - ``config.json`` setting: ``.TeamSettings.MaxChannelsPerTeam: 2000`` |
| Numerical input. Default is **2000** for self-hosted deployments, and **10000**       | - Environment variable: ``MM_TEAMSETTINGS_MAXCHANNELSPERTEAM``        |
| for Cloud deployments.                                                                |                                                                       |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------------------+

.. config:setting:: users-enablejoinleavemessages
  :displayname: Enable join/leave messages by default (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .TeamSettings.EnableJoinLeaveMessageByDefault
  :environment: MM_TEAMSETTINGS_ENABLEJOINLEAVEMESSAGEBYDEFAULT
  :description: Specify the default configuration of system messages displayed when users join or leave channels.

  - **true**: **(Default)** Join/Leave messages are displayed.
  - **false**: Join/Leave messages are hidden.

Enable join/leave messages by default
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| Specify the default configuration of system messages displayed when users             | - System Config path: **Site Configuration > Users and Teams**                     |
| join or leave channels.                                                               | - ``config.json`` setting: ``.TeamSettings.EnableJoinLeaveMessageByDefault: true`` |
|                                                                                       | - Environment variable: ``MM_TEAMSETTINGS_ENABLEJOINLEAVEMESSAGEBYDEFAULT``        |
| - **true**: **(Default)** Join/Leave messages are displayed.                          |                                                                                    |
| - **false**: Join/Leave messages are hidden.                                          |                                                                                    |
|                                                                                       |                                                                                    |
| Users can override this default by going to **Settings > Advanced >                   |                                                                                    |
| Enable Join/Leave Messages**.                                                         |                                                                                    |
+---------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

.. config:setting:: users-restrictdirectmessage
  :displayname: Enable users to open direct message channels with (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .TeamSettings.RestrictDirectMessage
  :environment: MM_TEAMSETTINGS_RESTRICTDIRECTMESSAGE
  :description: This setting determines whether a user can open a direct message channel with anyone on the Mattermost server or only to members of the same team.

  - **Any user on the Mattermost server**: **(Default)** Users can send a direct message to any user through the **Direct Messages > More** menu. ``config.json`` setting: ``"any"``
  - **Any member of the team**: The **Direct Messages > More** menu only allows direct messages to users on the same team. ``config.json`` setting: ``"team"``

Enable users to open direct message channels with
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| This setting determines whether a user can open a direct message channel with anyone on the Mattermost server or only to members of the same team. This setting only affects the options presented in the user interface. It does not affect permissions on the backend server.                                                                                                                                                                                                                                          | - System Config path: **Site Configuration > Users and Teams**       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | - ``config.json`` setting: ``.TeamSettings.RestrictDirectMessage``   |
| - **Any user on the Mattermost server**: **(Default)** Users can send a direct message to any user through the **Direct Messages > More** menu. ``config.json`` setting: ``"any"``                                                                                                                                                                                                                                                                                                                                       | - Environment variable: ``MM_TEAMSETTINGS_RESTRICTDIRECTMESSAGE``    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                      |
| - **Any member of the team**: The **Direct Messages > More** menu only allows direct messages to users on the same team. Pressing :kbd:`Ctrl` :kbd:`K` on Windows or Linux, or :kbd:`⌘` :kbd:`K` on Mac, only lists other users on the team currently being viewed. A user who is a member of multiple teams can only send direct messages to the team that is being viewed. However, the user can receive messages from other teams, regardless of the team currently being viewed. ``config.json`` setting: ``"team"`` |                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+

.. config:setting:: users-teammatenamedisplay
  :displayname: Teammate name display (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .TeamSettings.TeammateNameDisplay
  :environment: MM_TEAMSETTINGS_TEAMMATENAMEDISPLAY
  :description: This setting determines how names appear in posts and under the **Direct Messages** list.

  - **Show username**: **(Default)** Displays usernames. ``config.json`` option: ``"username"``.
  - **Show nickname if one exists...**: Displays the user’s nickname. ``config.json`` option: ``"nickname_full_name"``.
  - **Show first and last name**: Displays the user’s full name. ``config.json`` option: ``"full_name"``.

Teammate name display
~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| This setting determines how names appear in posts and under the **Direct Messages** list.       | - System Config path: **Site Configuration > Users and Teams**             |
| Users can change this setting in their interface under **Settings > Display >                   | - ``config.json`` setting: ``.TeamSettings.TeammateNameDisplay: username`` |
| Teammate Name Display**, unless this setting is locked by a System Admin                        | - Environment variable: ``MM_TEAMSETTINGS_TEAMMATENAMEDISPLAY``            |
| via the **Lock teammate name display for all users** configuration setting.                     |                                                                            |
|                                                                                                 |                                                                            |
| - **Show username**: **(Default for self-hosted deployments)** Displays usernames.              |                                                                            |
|   ``config.json`` option: ``"username"``.                                                       |                                                                            |
| - **Show nickname if one exists...**: Displays the user’s nickname. If the user doesn't have a  |                                                                            |
|   nickname, their full name is displayed. If the user doesn't have a full name, their username  |                                                                            |
|   is displayed. ``config.json`` option: ``"nickname_full_name"``.                               |                                                                            |
| - **Show first and last name**: **(Default for Cloud deployments)** Displays user’s full name.  |                                                                            |
|   If the user doesn't have a full name, their username is displayed. Recommended when using     |                                                                            |
|   `SAML <https://docs.mattermost.com/onboard/sso-saml.html>`__ or                               |                                                                            |
|   `LDAP <https://docs.mattermost.com/onboard/ad-ldap.html>`__ if first name and last name       |                                                                            |
|   attributes are configured. ``config.json`` option: ``"full_name"``.                           |                                                                            |
+-------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------+

.. config:setting:: users-lockteammatenamedisplay
  :displayname: Lock teammate name display for all users (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .TeamSettings.LockTeammateNameDisplay
  :environment: MM_TEAMSETTINGS_LOCKTEAMMATENAMEDISPLAY
  :description: This setting controls whether users can change settings under **Settings > Display > Teammate Name Display**.

  - **true**: Users **cannot** change the Teammate Name Display.
  - **false**: **(Default)** Users can change the Teammate Name Display setting.

Lock teammate name display for all users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| This setting controls whether users can change settings under **Settings > Display > Teammate Name Display**. | - System Config path: **Site Configuration > Users and Teams**              |
|                                                                                                               | - ``config.json`` setting: ``.TeamSettings.LockTeammateNameDisplay: false`` |
| - **true**: Users **cannot** change the Teammate Name Display.                                                | - Environment variable: ``MM_TEAMSETTINGS_LOCKTEAMMATENAMEDISPLAY``         |
| - **false**: **(Default)** Users can change the Teammate Name Display setting.                                |                                                                             |
|                                                                                                               |                                                                             |
+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: users-viewarchivedchannels
  :displayname: Allow users to view archived channels (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .TeamSettings.ExperimentalViewArchivedChannels
  :environment: MM_TEAMSETTINGS_EXPERIMENTALVIEWARCHIVEDCHANNELS

  - **true**: **(Default)** Allows users to access the content of archived channels of which they were a member.
  - **false**: Users are unable to access content in archived channels.

Allow users to view archived channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| - **true**: **(Default)** Allows users to access the content of archived channels of which they were a member. | - System Config path: **Site Configuration > Users and Teams**                      |
| - **false**: Users are unable to access content in archived channels.                                          | - ``config.json`` setting: ``.TeamSettings.ExperimentalViewArchivedChannels: true`` |
|                                                                                                                | - Environment variable: ``MM_TEAMSETTINGS_EXPERIMENTALVIEWARCHIVEDCHANNELS``        |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| **Note**: Cloud admins can't modify this configuration setting.                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

.. config:setting:: users-showemailaddress
  :displayname: Show email address (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .PrivacySettings.ShowEmailAddress
  :environment: MM_PRIVACYSETTINGS_SHOWEMAILADDRESS

  - **true**: **(Default)** All users can see the email addresses of every other user.
  - **false**: Hides email addresses in the client user interface, except for System Admins and the System Roles with read/write access to Compliance, Billing, or User Management (users/teams/channels/groups etc).

Show email address
~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| - **true**: **(Default)** All users can see the email addresses of every other user.        | - System Config path: **Site Configuration > Users and teams**         |
| - **false**: Hides email addresses in the client user interface, except from System Admins  | - ``config.json`` setting: ``.PrivacySettings.ShowEmailAddress: true`` |
|   and the System Roles with read/write access to Compliance, Billing, or User Management    | - Environment variable: ``MM_PRIVACYSETTINGS_SHOWEMAILADDRESS``        |
|   (users/teams/channels/groups etc).                                                        |                                                                        |
+---------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. config:setting:: users-showfullname
  :displayname: Show full name (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .PrivacySettings.ShowFullName
  :environment: MM_PRIVACYSETTINGS_SHOWFULLNAME

  - **true**: **(Default)** Full names are visible to all users in the client user interface.
  - **false**: Hides full names from all users, except System Admins.

Show full name
~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| - **true**: **(Default)** Full names are visible to all users in the client user interface.                      | - System Config path: **Site Configuration > Users and Teams**     |
| - **false**: Hides full names from all users, except System Admins. Username is shown in place of the full name. | - ``config.json`` setting: ``.PrivacySettings.ShowFullName: true`` |
|                                                                                                                  | - Environment variable: ``MM_PRIVACYSETTINGS_SHOWFULLNAME``        |
+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

.. config:setting:: users-enablecustomstatuses
  :displayname: Enable custom user statuses (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .TeamSettings.EnableCustomUserStatuses
  :environment: MM_TEAMSETTINGS_ENABLECUSTOMUSERSTATUSES

  - **true**: **(Default)** Users can set status messages and emojis that are visible to all users.
  - **false**: Users cannot set custom statuses.

Enable custom user statuses
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| - **true**: **(Default)** Users can set status messages and emojis that are visible to all users. | - System Config path: **Site Configuration > Users and Teams**              |
| - **false**: Users cannot set custom statuses.                                                    | - ``config.json`` setting: ``.TeamSettings.EnableCustomUserStatuses: true`` |
|                                                                                                   | - Environment variable: ``MM_TEAMSETTINGS_ENABLECUSTOMUSERSTATUSES``        |
+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: users-enablelastactivetime
  :displayname: Enable last active time (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .TeamSettings.EnableLastActiveTime
  :environment: MM_TEAMSETTINGS_ENABLELASTACTIVETIME

  - **true**: **(Default)** Users can see when inactive users were last active on a user's profile and in direct message channel headers.
  - **false**: Users can't see when inactive users were last online.

Enable last active time
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| - **true**: **(Default)** Users can see when inactive users were last active on a                 | - System Config path: **Site Configuration > Users and Teams**              |
|   user's profile and in direct message channel headers.                                           | - ``config.json`` setting: ``.TeamSettings.EnableLastActiveTime: true``     |
| - **false**: Users can't see when inactive users were last online.                                | - Environment variable: ``MM_TEAMSETTINGS_ENABLELASTACTIVETIME``            |
+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: users-enablecustomusergroups
  :displayname: Enable custom user groups (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: N/A
  :environment: N/A

  - **true**: **(Default)** Users with appropriate permissions can create custom user groups, and users can @mention custom user groups in Mattermost conversations.
  - **false**: Users cannot set custom statuses.

Enable custom user groups (Beta)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| - **true**: **(Default)** Users with appropriate permissions can create custom user groups,       | - System Config path: **Site Configuration > Users and Teams**              |
|   and users can @mention custom user groups in Mattermost conversations.                          | - ``config.json`` setting: N/A                                              |
| - **false**: Users cannot set custom statuses.                                                    | - Environment variable: N/A                                                 |
+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: users-userstatsupdatetime
  :displayname: User statistics update time (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .ServiceSettings.RefreshPostStatsRunTime
  :environment: MM_SERVICESETTINGS.REFRESHPOSTSTATSRUNTIME
  :description: Set the server time for updating the user post statistics, including each user's total message count, and the timestamp of each user's most recently sent message. Default is **00:00**.

User statistics update time
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| Set the server time for updating the user post statistics, including each user's total     | - System Config path: **Site Configuration > Users and Teams**                 |
| message count, and the timestamp of each user's most recently sent message.                | - ``config.json`` setting: ``.ServiceSettings.RefreshPostStatsRunTime: 00:00`` |
|                                                                                            | - Environment variable: ``MM_SERVICESETTINGS.REFRESHPOSTSTATSRUNTIME``         |
| Must be a 24-hour time stamp in the form ``HH:MM`` based on the local time of the server.  |                                                                                |
| Default is **00:00**.                                                                      |                                                                                |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

----

Notifications
-------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Notifications**.

.. config:setting:: notification-confirmtochannel
  :displayname: Show @channel, @all, or @here confirmation dialog (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .TeamSettings.EnableConfirmNotificationsToChannel
  :environment: MM_TEAMSETTINGS_ENABLECONFIRMNOTIFICATIONSTOCHANNEL

  - **true**: **(Default)** Requires users to confirm when posting @channel, @all, @here, or group mentions in channels with more than 5 members.
  - **false**: No confirmation is required.

Show @channel, @all, or @here confirmation dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| - **true**: **(Default)** Requires users to confirm when posting @channel, @all, @here, or group mentions in channels with more than 5 members.     | - System Config path: **Site Configuration > Notifications**                           |
| - **false**: No confirmation is required.                                                                                                           | - ``config.json`` setting: ``.TeamSettings.EnableConfirmNotificationsToChannel: true`` |
|                                                                                                                                                     | - Environment variable: ``MM_TEAMSETTINGS_ENABLECONFIRMNOTIFICATIONSTOCHANNEL``        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------+

.. config:setting:: notification-enableemail
  :displayname: Enable email notifications (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.SendEmailNotifications
  :environment: MM_EMAILSETTINGS_SENDEMAILNOTIFICATIONS

  - **true**: **(Default)** Enables automatic email notifications for posts.
  - **false**: Disables notifications.

Enable email notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| - **true**: **(Default)** Enables automatic email notifications for posts.                                                                                                  | - System Config path: **Site Configuration > Notifications**                |
| - **false**: Disables notifications. A developer may choose this option to speed development by skipping email setup (see also the **Enable preview mode banner** setting). | - ``config.json`` setting: ``.EmailSettings.SendEmailNotifications: ture``  |
|                                                                                                                                                                             | - Environment variable: ``MM_EMAILSETTINGS_SENDEMAILNOTIFICATIONS``         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| **Notes**:                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                           |
| - Cloud admins can't modify this configuration setting.                                                                                                                                                                                                   |
| - If this setting is **false**, and the SMTP server is set up, account-related emails (such as authentication messages) will be sent regardless of this setting.                                                                                          |
| - Email invitations and account deactivation emails aren't affected by this setting.                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: notification-enablepreviewbanner
  :displayname: Enable preview mode banner (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.EnablePreviewModeBanner
  :environment: MM_EMAILSETTINGS_ENABLEPREVIEWMODEBANNER

  - **true**: **(Default)** When **Send email notifications** is **false**, users see the Preview Mode banner.
  - **false**: Preview Mode banner does not appear.

.. _email-preview-mode-banner-config:

Enable preview mode banner
~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| - **true**: **(Default)** When **Send email notifications** is **false**, users see the Preview Mode banner. This banner alerts users that email notifications are disabled. | - System Config path: **Site Configuration > Notifications**                |
| - **false**: Preview Mode banner does not appear.                                                                                                                            | - ``config.json`` setting: ``.EmailSettings.EnablePreviewModeBanner: true`` |
|                                                                                                                                                                              | - Environment variable: ``MM_EMAILSETTINGS_ENABLEPREVIEWMODEBANNER``        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| **Note**: Cloud admins can't modify this configuration setting.                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: notification-enableemailbatching
  :displayname: Enable email batching (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.EnableEmailBatching
  :environment: MM_EMAILSETTINGS_ENABLEEMAILBATCHING

  - **true**: Multiple email notifications for mentions and direct messages over a given time period are batched into a single email.
  - **false**: **(Default)** Emails will be sent for each mention or direct message.

Enable email batching
~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| - **true**: Multiple email notifications for mentions and direct messages over a given time period are batched into a single email. The time period can be customized by each user under **Settings > Notifications**. The default time period is 15 minutes.                | - System Config path: **Site Configuration > Notifications**             |
| - **false**: **(Default)** Emails will be sent for each mention or direct message.                                                                                                                                                                                           | - ``config.json`` setting: ``.EmailSettings.EnableEmailBatching: false`` |
|                                                                                                                                                                                                                                                                              | - Environment variable: ``MM_EMAILSETTINGS_ENABLEEMAILBATCHING``         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| **Notes**:                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                         |
| - Cloud admins can't modify this configuration setting.                                                                                                                                                                                                                                                                                                 |
| - Regardless of this setting, a user can turn off these notifications under **Settings > Notifications**.                                                                                                                                                                                                                                               |
| - The `Site Url <https://docs.mattermost.com/configure/environment-configuration-settings.html#site-url>`__ and `SMTP Email Server <https://docs.mattermost.com/configure/environment-configuration-settings.html#smtp-server>`__ must be configured to allow email batching.                                                                           |
| - Email batching in `High Availability Mode <https://docs.mattermost.com/configure/environment-configuration-settings.html#enable-high-availability-mode>`__ is planned, but not yet supported.                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: notification-emailcontents
  :displayname: Email notification contents (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.EmailNotificationContentsType
  :environment: MM_EMAILSETTINGS_EMAILNOTIFICATIONCONTENTSTYPE

  - **Send full message contents**: **(Default)** Email notifications include the full message contents, along with the name of the sender and the channel. ``config.json`` setting: ``"full"``
  - **Send generic description with only sender name**: Only the name of the sender and team name are included in email notifications. ``config.json`` setting: ``"generic"``

Email notification contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| - **Send full message contents**: **(Default)** Email notifications include the full message contents, along with the name of the sender and the channel. ``config.json`` setting: ``"full"``                                                                                                 | - System Config path: **Site Configuration > Notifications**                |
|                                                                                                                                                                                                                                                                                               | - ``config.json`` setting: ``.EmailSettings.EmailNotificationContentsType`` |
| - **Send generic description with only sender name**: Only the name of the sender and team name are included in email notifications. Use this option if Mattermost contains confidential information and policy dictates it cannot be stored in email. ``config.json`` setting: ``"generic"`` | - Environment variable: ``MM_EMAILSETTINGS_EMAILNOTIFICATIONCONTENTSTYPE``  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: notification-displayname
  :displayname: Notification display name (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.FeedbackName
  :environment: MM_EMAILSETTINGS_FEEDBACKNAME
  :description: Display name for email notifications sent from the Mattermost system.

Notification display name
~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Display name for email notifications sent from the Mattermost system.                                  | - System Config path: **Site Configuration > Notifications** |
|                                                                                                        | - ``config.json`` setting: ``.EmailSettings.FeedbackName``   |
| String input. No default setting. This field is required when changing settings in the System Console. | - Environment variable: ``MM_EMAILSETTINGS_FEEDBACKNAME``    |
+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

.. config:setting:: notification-fromaddress
  :displayname: Notification from address (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.FeedbackEmail
  :environment: MM_EMAILSETTINGS_FEEDBACKEMAIL
  :description: Email address for notification emails from the Mattermost system. Default value is **test@example.com**.

Notification from address
~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| Email address for notification emails from the Mattermost system. This address should be monitored by a System Admin. | - System Config path: **Site Configuration > Notifications**  |
|                                                                                                                       | - ``config.json`` setting: ``.EmailSettings.FeedbackEmail``   |
| String input. Default is ``test@example.com``. This field is required when changing settings in the System Console.   | - Environment variable: ``MM_EMAILSETTINGS_FEEDBACKEMAIL``    |
+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

.. config:setting:: notification-supportemailaddress
  :displayname: Support email address (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .SupportSettings.SupportEmail
  :environment: MM_SUPPORTSETTINGS_SUPPORTEMAIL
  :description: Sets a user support (or feedback) email address that is displayed on email notifications and during the Getting Started tutorial.

Support email address
~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Sets a user support (or feedback) email address that is displayed on email notifications and during the Getting Started tutorial. This address should be monitored by a System Admin. If no value is set, email notifications will not contain a way for users to request assistance. | - System Config path: **Site Configuration > Notifications** |
|                                                                                                                                                                                                                                                                                       | - ``config.json`` setting: ``.SupportSettings.SupportEmail`` |
| String input. Default is ``feedback@mattermost.com``. This field is required when changing settings in the System Console.                                                                                                                                                            | - Environment variable: ``MM_SUPPORTSETTINGS_SUPPORTEMAIL``  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

.. config:setting:: notification-replytoaddress
  :displayname: Notification reply-to address (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.ReplyToAddress
  :environment: MM_EMAILSETTINGS_REPLYTOADDRESS
  :description: Email address used in the reply-to header when sending notification emails from the Mattermost system. Default value is **test@example.com**.

Notification reply-to address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+
| Email address used in the reply-to header when sending notification emails from the Mattermost system. This address should be monitored by a System Admin. | - System Config path: **Site Configuration > Notifications**   |
|                                                                                                                                                            | - ``config.json`` setting: ``.EmailSettings.ReplyToAddress``   |
| String input. Default is ``test@example.com``.                                                                                                             | - Environment variable: ``MM_EMAILSETTINGS_REPLYTOADDRESS``    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------+

.. config:setting:: notification-feedbackorganization
  :displayname: Notification footer mailing address (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.FeedbackOrganization
  :environment: MM_EMAILSETTINGS_FEEDBACKORGANIZATION
  :description: Optional setting to include the organization’s name and mailing address in the footer of email notifications.

Notification footer mailing address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| Optional setting to include the organization’s name and mailing address in the footer of email notifications. If not set, nothing will appear. | - System Config path: **Site Configuration > Notifications**         |
|                                                                                                                                                | - ``config.json`` setting: ``.EmailSettings.FeedbackOrganization``   |
| String input.                                                                                                                                  | - Environment variable: ``MM_EMAILSETTINGS_FEEDBACKORGANIZATION``    |
+------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+

.. config:setting:: notification-pushnotificationcontents
  :displayname: Push notification contents (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.PushNotificationContents
  :environment: MM_EMAILSETTINGS_PUSHNOTIFICATIONCONTENTS

  - **Generic description with only sender name**: Push notifications include the sender’s name, but not the channel name or message contents. ``config.json`` setting: ``"generic_no_channel"``
  - **Generic description with sender and channel names**: **(Default)** Push notifications include the name of the sender and channel, but not the message contents. ``config.json`` setting: ``"generic"``
  - **Full message content sent in the notification payload**: Includes the message contents in the push notification payload. ``config.json`` setting: ``"full"``
  - **Full message content fetched from the server on receipt** (*Available in Mattermost Enterprise*): The notification payload contains no message content; the content is fetched separately. ``config.json`` setting: ``"id_loaded"``

Push notification contents
~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| - **Generic description with only sender name**: Push notifications include the sender’s name,         | - System Config path: **Site Configuration > Notifications**           |
|   but not the channel name or message contents. ``config.json`` setting: ``"generic_no_channel"``      | - ``config.json`` setting: ``.EmailSettings.PushNotificationContents`` |
|                                                                                                        | - Environment variable: ``MM_EMAILSETTINGS_PUSHNOTIFICATIONCONTENTS``  |
| - **Generic description with sender and channel names**: **(Default)** Push notifications              |                                                                        |
|   include the name of the sender and channel, but not the message contents.                            |                                                                        |
|   ``config.json`` setting: ``"generic"``                                                               |                                                                        |
|                                                                                                        |                                                                        |
| - **Full message content sent in the notification payload**: Includes the message                      |                                                                        |
|   contents in the push notification payload, which may be sent through                                 |                                                                        |
|   `Apple’s Push Notification service <https://developer.apple.com/library/archive/documentation/       |                                                                        |
|   NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//                             |                                                                        |
|   apple_ref/doc/uid/TP40008194-CH8-SW1>`__ or `Google’s Firebase Cloud Messaging <https://firebase.    |                                                                        |
|   google.com/docs/cloud-messaging>`__ .                                                                |                                                                        |
|   We **highly recommended** this option only be used with an ``https`` protocol to encrypt             |                                                                        |
|   the connection and protect confidential information. ``config.json`` setting: ``"full"``             |                                                                        |
|                                                                                                        |                                                                        |
| - **Full message content fetched from the server on receipt** (*Available in Mattermost Enterprise*):  |                                                                        |
|   The notification payload contains no message content. Instead it contains a unique message ID used   |                                                                        |
|   to fetch message content from the Mattermost server when a push notification is received via a       |                                                                        |
|   `notification service app extension <https://developer.apple.com/documentation/usernotifications/    |                                                                        |
|   modifying_content_in_newly_delivered_notifications>`__ on iOS or `an expandable notification         |                                                                        |
|   pattern <https://developer.android.com/training/notify-user/expanded>`__ on Android.                 |                                                                        |
|                                                                                                        |                                                                        |
|   If the server cannot be reached, a generic push notification is displayed without message            |                                                                        |
|   content or sender name. For customers who wrap the Mattermost mobile application in a secure         |                                                                        |
|   container, the container must fetch the message contents using the unique message ID when            |                                                                        |
|   push notifications are received.                                                                     |                                                                        |
|                                                                                                        |                                                                        |
|   If the container is unable to execute the fetch, the push notification contents cannot be received   |                                                                        |
|   by the customer's mobile application without passing the message contents through Apple's or         |                                                                        |
|   Google's notification service. ``config.json`` setting: ``"id_loaded"``                              |                                                                        |
+--------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

----

Announcement banner
-------------------

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Announcement Banner**.

.. config:setting:: banner-enable
  :displayname: Enable announcement banner (Announcement banner)
  :systemconsole: Site Configuration > Announcement banner
  :configjson: .AnnouncementSettings.EnableBanner
  :environment: MM_ANNOUNCEMENTSETTINGS_ENABLEBANNER

  - **true**: Enable an announcement banner that is displayed across the top of the screen for all teams.
  - **false**: **(Default)** Disable the announcement banner.

Enable announcement banner
~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| - **true**: Enable an announcement banner that is displayed across the top of the screen for all teams.              | - System Config path: **Site Configuration > Announcement banner**       |
|                                                                                                                      | - ``config.json`` setting: ``.AnnouncementSettings.EnableBanner: false`` |
| - **false**: **(Default)** Disable the announcement banner.                                                          | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_ENABLEBANNER``         |
+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: banner-text
  :displayname: Banner text (Announcement banner)
  :systemconsole: Site Configuration > Announcement banner
  :configjson: .AnnouncementSettings.BannerText
  :environment: MM_ANNOUNCEMENTSETTINGS_BANNERTEXT
  :description: The text of the announcement banner.

Banner text
~~~~~~~~~~~

+------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| The text of the announcement banner. If no text is provided, the banner will not appear. | - System Config path: **Site Configuration > Announcement banner** |
|                                                                                          | - ``config.json`` setting: ``.AnnouncementSettings.BannerText``    |
| String input.                                                                            | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_BANNERTEXT``     |
+------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

.. config:setting:: banner-color
  :displayname: Banner color (Announcement banner)
  :systemconsole: Site Configuration > Announcement banner
  :configjson: .AnnouncementSettings.BannerColor
  :environment: MM_ANNOUNCEMENTSETTINGS_BANNERCOLOR
  :description: The background color of the announcement banner. Default value is **#f2a93b**.

Banner color
~~~~~~~~~~~~

+--------------------------------------------------+-----------------------------------------------------------------------------+
| The background color of the announcement banner. | - System Config path: **Site Configuration > Announcement banner**          |
|                                                  | - ``config.json`` setting: ``.AnnouncementSettings.BannerColor: "#f2a93b"`` |
| String input of a CSS color value.               | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_BANNERCOLOR``             |
+--------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: banner-textcolor
  :displayname: Banner text color (Announcement banner)
  :systemconsole: Site Configuration > Announcement banner
  :configjson: .AnnouncementSettings.BannerTextColor
  :environment: MM_ANNOUNCEMENTSETTINGS_BANNERTEXTCOLOR
  :description: The color of the text in the announcement banner. Default value is **#333333**.

Banner text color
~~~~~~~~~~~~~~~~~

+---------------------------------------------------+---------------------------------------------------------------------------------+
| The color of the text in the announcement banner. | - System Config path: **Site Configuration > Announcement banner**              |
|                                                   | - ``config.json`` setting: ``.AnnouncementSettings.BannerTextColor: "#333333"`` |
| String input of a CSS color value.                | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_BANNERTEXTCOLOR``             |
+---------------------------------------------------+---------------------------------------------------------------------------------+

.. config:setting:: banner-allowdismissal
  :displayname: Allow banner dismissal (Announcement banner)
  :systemconsole: Site Configuration > Announcement banner
  :configjson: .AnnouncementSettings.AllowBannerDismissal
  :environment: MM_ANNOUNCEMENTSETTINGS_ALLOWBANNERDISMISSAL

  - **true**: **(Default)** Users can dismiss the banner. The banner will re-appear the next time the user logs in.
  - **false**: Users cannot dismiss the banner.

Allow banner dismissal
~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| - **true**: **(Default)** Users can dismiss the banner. The banner will re-appear the next time the user logs in. The banner will also re-appear if the text is updated, or a System Admin disables the banner and re-enables it. | - System Config path: **Site Configuration > Announcement banner**              |
|                                                                                                                                                                                                                                   | - ``config.json`` setting: ``.AnnouncementSettings.AllowBannerDismissal: true`` |
| - **false**: Users cannot dismiss the banner.                                                                                                                                                                                     | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_ALLOWBANNERDISMISSAL``        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+

----

Emoji
-----

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Emoji**.

.. config:setting:: emoji-enablepicker
  :displayname: Enable emoji picker (Emoji)
  :systemconsole: Site Configuration > Emoji
  :configjson: .ServiceSettings.EnableEmojiPicker
  :environment: MM_SERVICESETTINGS_ENABLEEMOJIPICKER

  - **true**: **(Default)** Enables an emoji picker when composing messages and for message reactions.
  - **false**: Disables the emoji picker in message composition and reactions.

Enable emoji picker
~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| - **true**: **(Default)** Enables an emoji picker when composing messages and for message reactions. | - System Config path: **Site Configuration > Emoji**                    |
| - **false**: Disables the emoji picker in message composition and reactions.                         | - ``config.json`` setting: ``.ServiceSettings.EnableEmojiPicker: true`` |
|                                                                                                      | - Environment variable: ``MM_SERVICESETTINGS_ENABLEEMOJIPICKER``        |
+------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

.. config:setting:: emoji-enablecustom
  :displayname: Enable custom emoji (Emoji)
  :systemconsole: Site Configuration > Emoji
  :configjson: .ServiceSettings.EnableCustomEmoji
  :environment: MM_SERVICESETTINGS_ENABLECUSTOMEMOJI

  - **true**: Allows users to add emojis through a **Custom Emoji** option in the emoji picker.
  - **false**: **(Default)** Disables custom emojis.

Enable custom emoji
~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| - **true**: **(Default)** Allows users to add emojis through a                | - System Config path: **Site Configuration > Emoji**                     |
|   **Custom Emoji** option in the emoji picker. Emojis can be GIF, PNG, or     | - ``config.json`` setting: ``.ServiceSettings.EnableCustomEmoji: true``  |
|   JPG files up to 512 KB in size.                                             | - Environment variable: ``MM_SERVICESETTINGS_ENABLECUSTOMEMOJI``         |
| - **false**:  Disables custom emojis.                                         |                                                                          |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: Too many custom emojis can slow your server’s performance.                                                                                     |
+-------------------------------------------------------------------------------+--------------------------------------------------------------------------+

----

Posts
-----

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Posts**.

.. config:setting:: posts-automaticallyfollowthreads
  :displayname: Automatically follow threads (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.ThreadAutoFollow
  :environment: MM_SERVICESETTINGS_THREADAUTOFOLLOW

  - **true**: **(Default)** Enables automatic following for all threads that a user starts, or in which the user participates or is mentioned.
  - **false**: Disables automatic following of threads.

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
| - This setting **must** be enabled for `Collapsed Reply Threads <https://docs.mattermost.com/collaborate/organize-conversations.html>`__ to function. See the `administrator’s guide to enabling Collapsed Reply Threads <https://support.mattermost.com/hc/en-us/articles/6880701948564>`__ for details.                                                                                                      |
| - Enabling this setting does not automatically follow threads based on previous user actions. For example, threads a user participated in prior to enabling this setting won't be automatically followed, unless the user adds a new comment or is mentioned in the thread.                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: posts-collapsedreplythreads
  :displayname: Collapsed reply threads (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.CollapsedThreads
  :environment: MM_SERVICESETTINGS_COLLAPSEDTHREADS

  - **Always On**: **(Default)** Enables `Collapsed Reply Threads <https://docs.mattermost.com/collaborate/organize-conversations.html>`__ on the server and for all users. ``config.json`` setting: ``"always_on"``
  - **Default On**: Enables Collapsed Reply Threads on the server and for all users. ``config.json`` setting: ``"default_on"``
  - **Default Off**: Enables Collapsed Reply Threads on the server but **not** for users. ``config.json`` setting: ``"default_off"``
  - **Disabled**: Users cannot enable Collapsed Reply Threads. ``config.json`` setting: ``"disabled"``

Collapsed reply threads
~~~~~~~~~~~~~~~~~~~~~~~

.. important::

    Customers upgrading to v7.0 must review the `administrator’s guide to enabling Collapsed Reply Threads <https://support.mattermost.com/hc/en-us/articles/6880701948564>`__ prior to enabling this functionality.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| - **Always On**: **(Default)** Enables `Collapsed Reply Threads <https://docs.mattermost.com/collaborate/organize-conversations.html>`__ on the server and for all users. This is the recommended configuration for optimal user experience and to ensure consistency in how users read and respond to threaded conversations. ``config.json`` setting: ``"always_on"`` | - System Config path: **Site Configuration > Posts**               |
| - **Default On**: Enables Collapsed Reply Threads on the server and for all users. Users can choose to `disable Collapsed Reply Threads </preferences/manage-your-display-options.html#collapsed-reply-threads>`__ for their Mattermost account in **Settings > Display > Collapsed Reply Threads**. ``config.json`` setting: ``"default_on"``                          | - ``config.json`` setting: ``.ServiceSettings.CollapsedThreads``   |
| - **Default Off**: Enables Collapsed Reply Threads on the server but **not** for users. Users can choose to enable Collapsed Reply Threads for their Mattermost account in **Settings > Display > Collapsed Reply Threads**. ``config.json`` setting: ``"default_off"``                                                                                                 | - Environment variable: ``MM_SERVICESETTINGS_COLLAPSEDTHREADS``    |
| - **Disabled**: Users cannot enable Collapsed Reply Threads. ``config.json`` setting: ``"disabled"``                                                                                                                                                                                                                                                                    |                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

.. config:setting:: posts-messagepriority
  :displayname: Message priority (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.PostPriority
  :environment: MM_SERVICESETTINGS_POSTPRIORITY

  - **true**: **(Default)** Enables message priority for all users.
  - **false**: Disables the ability to set message priority and request acknowlegements.

Message priority
~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------+------------------------------------------------------------------------+
| - **true**: **(Default)** Enables message priority for all users which      | - System Config path: **Site Configuration > Posts**                   |
|   enables them to set a visual indiciator for important or urgent root      | - ``config.json`` setting: ``.ServiceSettings.PostPriority: true``     |
|   messages.                                                                 | - Environment variable: ``MM_SERVICESETTINGS_POSTPRIORITY``            |
| - **false**: Disables the ability to set message priority and request       |                                                                        |
|   acknowledgements.                                                         |                                                                        |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------+
| **Note**: `Mattermost Professional or Enterprise <https://mattermost.com/pricing>`__ customers can additionally request message acknowledgements to  |
| track that specific, time-sensitive messages have been seen and actioned. See the                                                                    |
| `message priority <https://docs.mattermost.com/collaborate/message-priority.html>`__ documentation to learn more.                                    |
+-----------------------------------------------------------------------------+------------------------------------------------------------------------+

.. config:setting:: posts-persistentnotifications
  :displayname: Persistent notifications (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.AllowPersistentNotifications
  :environment: MM_SERVICESETTINGS_ALLOWPERSISTENTNOTIFICATIONS

  - **true**: **(Default)** Users can trigger repeating notifications to mentioned recipients of urgent messages.
  - **false**: Disables the ability to send repeating notifications.

Persistent notifications
~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| - **true**: **(Default)** Users can trigger repeating notifications to   | - System Config path: **Site Configuration > Posts**                                |
|   mentioned recipients of urgent messages.                               | - ``config.json`` setting: ``.ServiceSettings.AllowPersistentNotifications: true``  |
| - **false**: Disables the ability to send repeating notifications.       | - Environment variable: ``MM_SERVICESETTINGS_ALLOWPERSISTENTNOTIFICATIONS``         |
+--------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

.. config:setting:: posts-maxnumberofrecipientsforpersistentnotifications
  :displayname: Maximum number of recipients for persistent notifications (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.PersistentNotificationMaxRecipients
  :environment: MM_SERVICESETTINGS_PERSISTENTNOTIFICATIONSMAXRECIPIENTS
  :description: The maximum number of recipients users may send persistent notifications to. Default is **5**.

Maximum number of recipients for persistent notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| The maximum number of recipients users may send persistent    | - System Config path: **Site Configuration > Posts**                                    |
| notifications to.                                             | - ``config.json`` setting: ``.ServiceSettings.PersistentNotificationMaxRecipients: 5``  |
|                                                               | - Environment variable: ``MM_SERVICESETTINGS_PERSISTENTNOTIFICATIONSMAXRECIPIENTS``     |
| Numerical input. Default is **5**.                            |                                                                                         |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. config:setting:: posts-frequencyofpersistentnotifications
  :displayname: Frequency of persistent notifications (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.PersistentNotificationIntervalMinutes
  :environment: MM_SERVICESETTINGS_PERSISTENTNOTIFICATIONINTERVALMINUTES
  :description: The number of minutes between repeated notifications for urgent messages sent with persistent notifications. Default is **5**.

Frequency of persistent notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| The number of minutes between repeated notifications for      | - System Config path: **Site Configuration > Posts**                                      |
| urgent messages sent with persistent notifications.           | - ``config.json`` setting: ``.ServiceSettings.PersistentNotificationIntervalMinutes: 5``  |
|                                                               | - Environment variable: ``MM_SERVICESETTINGS_PERSISTENTNOTIFICATIONINTERVALMINUTES``      |
| Numerical input. Default is **5**. Minimum is **2**.          |                                                                                           |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------+

.. config:setting:: posts-totalnumberofpersistentnotificationsperpost
  :displayname: Total number of persistent notifications per post (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.PersistentNotificationMaxCount
  :environment: MM_SERVICESETTINGS_PERSISTENTNOTIFICATIONMAXCOUNT
  :description: The maximum number of times users may receive persistent notifications. Default is **6**.

Total number of persistent notifications per post
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+------------------------------------------------------------------------------------+
| The maximum number of times users may receive persistent    | - System Config path: **Site Configuration > Posts**                               |
| notifications.                                              | - ``config.json`` setting: ``.ServiceSettings.PersistentNotificationMaxCount: 6``  |
|                                                             | - Environment variable: ``MM_SERVICESETTINGS_PERSISTENTNOTIFICATIONMAXCOUNT``      |
| Numerical input. Default is **6**.                          |                                                                                    |
+-------------------------------------------------------------+------------------------------------------------------------------------------------+

.. config:setting:: posts-enablelinkpreviews
  :displayname: Enable website link previews (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.EnableLinkPreviews
  :environment: MM_SERVICESETTINGS_ENABLELINKPREVIEWS

  - **true**: The server generates a preview of the first website, image, or YouTube video linked in a message.
  - **false**: **(Default)** All previews are disabled and the server does not request metadata for any links contained in messages.

Enable website link previews
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| - **true**: The server generates a preview of the first website, image, or YouTube video linked in a message. Users can disable website previews, but not image or YouTube previews, under **Settings > Display > Website Link Previews**. | - System Config path: **Site Configuration > Posts**                     |
| - **false**: **(Default)** All previews are disabled and the server does not request metadata for any links contained in messages.                                                                                                         | - ``config.json`` setting: ``.ServiceSettings.EnableLinkPreviews: true`` |
|                                                                                                                                                                                                                                            | - Environment variable: ``MM_SERVICESETTINGS_ENABLELINKPREVIEWS``        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: The server must be connected to the internet to generate previews. This connection can be established through a `firewall or outbound proxy <https://docs.mattermost.com/install/outbound-proxy.html>`__ if necessary.                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: posts-disablepreviewsperdomain
  :displayname: Disable link previews for specific domains (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.RestrictLinkPreviews
  :environment: MM_SERVICESETTINGS_RESTRICTLINKPREVIEWS
  :description: Use this setting to disable previews of links for specific domains.

Disable link previews for specific domains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| Use this setting to disable previews of links for specific domains.                                      | - System Config path: **Site Configuration > Posts**                   |
|                                                                                                          | - ``config.json`` setting: ``.ServiceSettings.RestrictLinkPreviews``   |
| String input of a comma-separated list of domains, for example: ``"mattermost.com, images.example.com"`` | - Environment variable: ``MM_SERVICESETTINGS_RESTRICTLINKPREVIEWS``    |
+----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. config:setting:: posts-enablemessagelinkpreviews
  :displayname: Enable message link previews (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.EnablePermalinkPreviews
  :environment: MM_SERVICESETTINGS_ENABLEPERMALINKPREVIEWS

  - **true**: **(Default)** `Share links to Mattermost messages <https://docs.mattermost.com/collaborate/share-links.html>`__ will generate a preview for any users that have access to the original message.
  - **false**: Share links do not generate a preview.

Enable message link previews
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| - **true**: **(Default)** `Share links to Mattermost messages <https://docs.mattermost.com/collaborate/share-links.html>`__ will generate a preview for any users that have access to the original message. | - System Config path: **Site Configuration > Posts**                          |
| - **false**: Share links do not generate a preview.                                                                                                                                                         | - ``config.json`` setting: ``.ServiceSettings.EnablePermalinkPreviews: true`` |
|                                                                                                                                                                                                             | - Environment variable: ``MM_SERVICESETTINGS_ENABLEPERMALINKPREVIEWS``        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

.. config:setting:: posts-enablesvg
  :displayname: Enable SVGs (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.EnableSVGs
  :environment: MM_SERVICESETTINGS_ENABLESVGS

  - **true**: Enables previews of SVG files attached to messages.
  - **false**: **(Default)** Disables previews of SVG files.

Enable SVGs
~~~~~~~~~~~

+-------------------------------------------------------------------------------+------------------------------------------------------------------+
| - **true**: Enables previews of SVG files attached to messages.               | - System Config path: **Site Configuration > Posts**             |
| - **false**: **(Default)** Disables previews of SVG files.                    | - ``config.json`` setting: ``.ServiceSettings.EnableSVGs: false``|
|                                                                               | - Environment variable: ``MM_SERVICESETTINGS_ENABLESVGS``        |
+-------------------------------------------------------------------------------+------------------------------------------------------------------+
| **Warning**: Enabling SVGs is not recommended in environments where not all users are trusted.                                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: posts-enablelatex
  :displayname: Enable LaTeX code block rendering (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.EnableLatex
  :environment: MM_SERVICESETTINGS_ENABLELATEX

  - **true**: Enables rendering of `LaTeX in code blocks <https://docs.mattermost.com/collaborate/format-messages.html#math-formulas>`__.
  - **false**: **(Default)** Disables rendering in blocks. Instead, LaTeX code is highlighted.

Enable LaTeX code block rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| - **true**: Enables rendering of `LaTeX in code blocks <https://docs.mattermost.com/collaborate/format-messages.html#math-formulas>`__.            | - System Config path: **Site Configuration > Posts**              |
| - **false**: **(Default)** Disables rendering in blocks. Instead, LaTeX code is highlighted.                                                       | - ``config.json`` setting: ``.ServiceSettings.EnableLatex: false``|
|                                                                                                                                                    | - Environment variable: ``MM_SERVICESETTINGS_ENABLELATEX``        |
+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| **Warning**: Enabling LaTeX rendering is not recommended in environments where not all users are trusted.                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+

.. config:setting:: posts-enableinlinelatex
  :displayname: Enable inline LaTeX rendering (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.EnableInlineLatex
  :environment: MM_SERVICESETTINGS_ENABLEINLINELATEX

  - **true**: **(Default)** Enables rendering of `LaTeX in message text <https://docs.mattermost.com/collaborate/format-messages.html#math-formulas>`__.
  - **false**: Disables inline rendering of LaTeX. Instead, LaTeX in message text is highlighted.

Enable inline LaTeX rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| - **true**: **(Default)** Enables rendering of `LaTeX in message text <https://docs.mattermost.com/collaborate/format-messages.html#math-formulas>`__.                                                             | - System Config path: **Site Configuration > Posts**                    |
| - **false**: Disables inline rendering of LaTeX. Instead, LaTeX in message text is highlighted. LaTeX can also be rendered in a code block, if that feature is enabled. See **Enable LaTeX code block rendering**. | - ``config.json`` setting: ``.ServiceSettings.EnableInlineLatex: true`` |
|                                                                                                                                                                                                                    | - Environment variable: ``MM_SERVICESETTINGS_ENABLEINLINELATEX``        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| **Warning**: Enabling LaTeX rendering is not recommended in environments where not all users are trusted.                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

.. config:setting:: posts-customurlschemes
  :displayname: Custom URL schemes (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .DisplaySettings.CustomURLSchemes
  :environment: MM_DISPLAYSETTINGS_CUSTOMURLSCHEMES
  :description: A list of URL schemes that will automatically create a link in message text.

Custom URL schemes
~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| A list of URL schemes that will automatically create a link in message text, for example: ``["git", "smtp"]``. These schemes always create links: ``http``, ``https``, ``ftp``, ``tel``, and ``mailto``. | - System Config path: **Site Configuration > Posts**                  |
|                                                                                                                                                                                                          | - ``config.json`` setting: ``.DisplaySettings.CustomURLSchemes: []``  |
| ``config.json`` setting: an array of strings                                                                                                                                                             | - Environment variable: ``MM_DISPLAYSETTINGS_CUSTOMURLSCHEMES``       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+

.. config:setting:: posts-maxmarkdownnodes
  :displayname: Maximum Markdown nodes (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .DisplaySettings.MaxMarkdownNodes
  :environment: MM_DISPLAYSETTINGS_MAXMARKDOWNNODES
  :description: The maximum number of Markdown elements that can be included in a single piece of text in a message. Default is 0 which applies a Mattermost-specified limit.

Maximum Markdown nodes
~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+-----------------------------------------------------------------------+
| The maximum number of Markdown elements (such as emojis,    | - System Config path: **Site Configuration > Posts**                  |
| links, or table cells), that can be included in a single    | - ``config.json`` setting: ``.DisplaySettings.MaxMarkdownNodes: 0``   |
| piece of text in a message.                                 | - Environment variable: ``MM_DISPLAYSETTINGS_MAXMARKDOWNNODES``       |
|                                                             |                                                                       |
| Numerical input. Default is **0** which applies a           |                                                                       |
| Mattermost-specified limit.                                 |                                                                       |
+-------------------------------------------------------------+-----------------------------------------------------------------------+

.. config:setting:: posts-googleapikey
  :displayname: Google API key (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.GoogleDeveloperKey
  :environment: MM_SERVICESETTINGS_GOOGLEDEVELOPERKEY
  :description: If a key is provided in this setting, Mattermost displays titles of embedded YouTube videos and detects if a video is no longer available.

Google API key
~~~~~~~~~~~~~~

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

.. config:setting:: posts-AllowSyncedDrafts
  :displayname: Enable server syncing of message drafts (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.AllowSyncedDrafts
  :environment: MM_SERVICESETTINGS_ALLOWSYNCEDDRAFTS
  :description: Enable or disable the ability to synchronize draft messages across all supported Mattermost clients.

Enable server syncing of message drafts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+--------------------------------------------------------------------------------------+
| Enable or disable the ability to synchronize draft   | - System Config path: **Site Configuration > Posts**                                 |
| messages across all supported Mattermost clients.    | - ``config.json`` setting: ``".ServiceSettings.AllowSyncedDrafts: true,``            |
|                                                      | - Environment variable: ``MM_SERVICESETTINGS_ALLOWSYNCEDDRAFTS``                     |
| - **true**: **(Default)** Message drafts are saved   |                                                                                      |
|   on the server and may be accessed from different   |                                                                                      |
|   clients. Users may still disable server            |                                                                                      |
|   synchronization of draft messages by going         |                                                                                      |
|   to **Settings > Advanced Settings**.               |                                                                                      |
| - **false**: Draft messages are stored locally       |                                                                                      |
|   on each device.                                    |                                                                                      |
+------------------------------------------------------+--------------------------------------------------------------------------------------+

----

File sharing and downloads
--------------------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > File Sharing and Downloads**.

.. config:setting:: fileshare-allowfilesharing
  :displayname: Allow file sharing (File sharing)
  :systemconsole: Site Configuration > File Sharing and Downloads
  :configjson: .FileSettings.EnableFileAttachments
  :environment: MM_FILESETTINGS_ENABLEFILEATTACHMENTS

  - **true**: **(Default)** Allows users to attach files to messages.
  - **false**: Prevents users from attaching files (including images) to a message.

Allow file sharing
~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| - **true**: **(Default)** Allows users to attach files to messages.                                                                                     | - System Config path: **Site Configuration > File Sharing and Downloads** |
| - **false**: Prevents users from attaching files (including images) to a message. This affects users on all clients and devices, including mobile apps. | - ``config.json`` setting: ``.FileSettings.EnableFileAttachments: true``  |
|                                                                                                                                                         | - Environment variable: ``MM_FILESETTINGS_ENABLEFILEATTACHMENTS``         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: fileshare-allowuploadsonmobile
  :displayname: Allow file uploads on mobile (File sharing)
  :systemconsole: Site Configuration > File Sharing and Downloads
  :configjson: .FileSettings.EnableMobileUpload
  :environment: MM_FILESETTINGS_ENABLEMOBILEUPLOAD

  - **true**: **(Default)** Allows users to attach files to messages from mobile apps.
  - **false**: Prevents users from attaching files (including images) to messages from mobile apps.

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

.. config:setting:: fileshare-allowdownloadsonmobile
  :displayname: Allow file downloads on mobile (File sharing)
  :systemconsole: Site Configuration > File sharing and downloads
  :configjson: .FileSettings.EnableMobileDownload
  :environment: MM_FILESETTINGS_ENABLEMOBILEDOWNLOAD

  - **true**: **(Default)** Enables file downloads on mobile apps.
  - **false**: Disables file downloads on mobile apps. Users can still download files from a mobile web browser.

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

.. config:setting:: publink-enable
  :displayname: Enable public file links (Public links)
  :systemconsole: Site Configuration > Public Links
  :configjson: .FileSettings.EnablePublicLink
  :environment: MM_FILESETTINGS_ENABLEPUBLICLINK

  - **true**: Allows users to create `public links <https://docs.mattermost.com/collaborate/share-files-in-messages.html#share-public-links>`__ to files attached to Mattermost messages.
  - **false**: **(Default)** Prevents users from creating public links to files and disables all previously created links.

Enable public file links
~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| - **true**: Allows users to create `public links <https://docs.mattermost.com/collaborate/share-files-in-messages.html#share-public-links>`__ to files attached to Mattermost messages.       | - System Config path: **Site Configuration > Public Links**           |
| - **false**: **(Default)** Prevents users from creating public links to files and disables all previously created links.                                                                      | - ``config.json`` setting: ``.FileSettings.EnablePublicLink: false``  |
|                                                                                                                                                                                               | - Environment variable: ``MM_FILESETTINGS_ENABLEPUBLICLINK``          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| **Note**: When set to ``false``, anyone who tries to visit a previously created public link will receive an error message. If the setting is returned to ``true``, previously created links will be accessible, unless the **Public link salt** has been regenerated. |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: publink-salt
  :displayname: Public link salt (Public links)
  :systemconsole: Site Configuration > Public Links
  :configjson: .FileSettings.EnablePublicLink
  :environment: MM_FILESETTINGS_ENABLEPUBLICLINK
  :description: 32-character salt added to the URL of public file links. Changing this setting will **invalidate** all previously generated links.

Public link salt
~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| 32-character salt added to the URL of public file links. Changing this setting will **invalidate** all previously generated links. The salt is randomly generated when Mattermost is installed, and can be regenerated by selecting **Regenerate** in the System Console. | - System Config path: **Site Configuration > Public Links**     |
|                                                                                                                                                                                                                                                                           | - ``config.json`` setting: ``.FileSettings.PublicLinkSalt``     |
| String input.                                                                                                                                                                                                                                                             | - Environment variable: ``MM_FILESETTINGS_PUBLICLINKSALT``      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+

----

Notices
-------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Notices**.

.. config:setting:: notices-enableadminnotices
  :displayname: Enable admin notices (Notices)
  :systemconsole: Site Configuration > Notices
  :configjson: .AnnouncementSettings.AdminNoticesEnabled
  :environment: MM_ANNOUNCEMENTSETTINGS_ADMINNOTICESENABLED

  - **true**: **(Default)** System Admins will receive `in-product notices <https://docs.mattermost.com/manage/in-product-notices.html>`__ about server upgrades and administration features.
  - **false**: System Admins will not receive specific notices. Admins will still receive notices for all users (see **Enable end user notices**).

Enable admin notices
~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| - **true**: **(Default)** System Admins will receive `in-product notices <https://docs.mattermost.com/manage/in-product-notices.html>`__ about server upgrades and administration features. | - System Config path: **Site Configuration > Notices** -                         |
|                                                                                                                                                                                             | - ``config.json`` setting: ``.AnnouncementSettings.AdminNoticesEnabled: true``   |
| - **false**: System Admins will not receive specific notices. Admins will still receive notices for all users (see **Enable end user notices**)                                             | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_ADMINNOTICESENABLED``          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: notices-enableendusernotices
  :displayname: Enable end user notices (Notices)
  :systemconsole: Site Configuration > Notices
  :configjson: .AnnouncementSettings.UserNoticesEnabled
  :environment: MM_ANNOUNCEMENTSETTINGS_USERNOTICESENABLED

  - **true**: **(Default)** All users receive `in-product notices <https://docs.mattermost.com/manage/in-product-notices.html>`__ about client upgrades and end user features.
  - **false**: Users will not receive in-product notices.

Enable end user notices
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| - **true**: **(Default)** All users receive `in-product notices <https://docs.mattermost.com/manage/in-product-notices.html>`__ about client upgrades and end user features.   | - System Config path: **Site Configuration > Notices**                        |
| - **false**: Users will not receive in-product notices.                                                                                                                        | - ``config.json`` setting: ``.AnnouncementSettings.UserNoticesEnabled: true`` |
|                                                                                                                                                                                | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_USERNOTICESENABLED``        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
