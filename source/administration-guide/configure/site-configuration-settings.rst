Site configuration settings
===========================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Review and manage the following site configuration options in the System Console by selecting the **Product** |product-list| menu, selecting **System Console**, and then selecting **Site Configuration**:

- `Customization <#customization>`__
- `Localization <#localization>`__
- `Users and Teams <#users-and-teams>`__
- `Notifications <#notifications>`__
- `System-wide notifications <#system-wide-notifications>`__
- `Emoji <#emoji>`__
- `Posts <#posts>`__
- `File Sharing and Downloads <#file-sharing-and-downloads>`__
- `Public Links <#public-links>`__
- `Notices <#notices>`__
- `Connected Workspaces <#connected-workspaces>`__

.. tip::

  System admins managing a self-hosted Mattermost deployment can edit the ``config.json`` file as described in the following tables. Each configuration value below includes a JSON path to access the value programmatically in the ``config.json`` file using a JSON-aware tool. For example, the ``SiteName`` value is under ``TeamSettings``.

  - If using a tool such as `jq <https://stedolan.github.io/jq/>`__, you'd enter: ``cat config/config.json | jq '.TeamSettings.SiteName'``
  - When working with the ``config.json`` file manually, look for an object such as ``TeamSettings``, then within that object, find the key ``SiteName``.

----

Customization
-------------

Access the following configuration settings in the System Console by going to **Site Configuration > Customization**.

.. config:setting:: site-name
  :displayname: Site name (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .TeamSettings.SiteName
  :environment: MM_TEAMSETTINGS_SITENAME
  :description: Name of the site shown in login screens and user interface. Default value is **Mattermost**.

Site name
~~~~~~~~~

+----------------------------------------------------------------+-----------------------------------------------------------------+
| Name of the site shown in login screens and user interface.    | - System Config path: **Site Configuration > Customization**    |
|                                                                | - ``config.json`` setting: ``TeamSettings`` > ``SiteName``      |
| String input. Maximum 30 characters. Default is ``Mattermost`` | - Environment variable: ``MM_TEAMSETTINGS_SITENAME``            |
+----------------------------------------------------------------+-----------------------------------------------------------------+

.. config:setting:: site-description
  :displayname: Site description (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .TeamSettings.CustomDescriptionText
  :environment: MM_TEAMSETTINGS_CUSTOMDESCRIPTIONTEXT
  :description: Text displayed above the login form. When not specified, the phrase **Log in** is displayed.

Site description
~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Text displayed above the login form. When not specified, the phrase "Log in" is displayed. | - System Config path: **Site Configuration > Customization**                |
|                                                                                            | - ``config.json`` setting: ``TeamSettings`` > ``CustomDescriptionText``     |
| String input.                                                                              | - Environment variable: ``MM_TEAMSETTINGS_CUSTOMDESCRIPTIONTEXT``           |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: enable-custom-branding
  :displayname: Enable custom branding (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .TeamSettings.EnableCustomBrand
  :environment: MM_TEAMSETTINGS_ENABLECUSTOMBRAND
  :description: Enables the display of a custom image and text on the login page. Default value is **false**.

  - **true**: Enables the display of a custom image and text on the login page
  - **false**: **(Default)** Custom branding is disabled

Enable custom branding
~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| - **true**: Enables the display of a custom image and text on the login page   | - System Config path: **Site Configuration > Customization**                     |
| - **false**: **(Default)** Custom branding is disabled                         | - ``config.json`` setting: ``TeamSettings`` > ``EnableCustomBrand``  > ``false`` |
|                                                                                | - Environment variable: ``MM_TEAMSETTINGS_ENABLECUSTOMBRAND``                    |
| See also the `custom brand image <#custom-brand-image>`__ and                  |                                                                                  |
| `custom brand text <#custom-brand-text>`__ configuration settings for more     |                                                                                  |
| branding options.                                                              |                                                                                  |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: custom-brand-image
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

.. config:setting:: custom-brand-text
  :displayname: Custom brand text (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .TeamSettings.CustomBrandText
  :environment: MM_TEAMSETTINGS_CUSTOMBRANDTEXT
  :description: Text that will be shown below the **Custom brand image** on the login page. Maximum 500 characters.

Custom brand text
~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| Text that will be shown below the **Custom brand image** on the login page.                                       | - System Config path: **Site Configuration > Customization**      |
| You can format this text using the same :doc:`Markdown formatting </end-user-guide/collaborate/format-messages>`  | - ``config.json`` setting: ``TeamSettings`` > ``CustomBrandText`` |
| as in Mattermost messages.                                                                                        | - Environment variable: ``MM_TEAMSETTINGS_CUSTOMBRANDTEXT``       |
|                                                                                                                   |                                                                   |
| String input. Maximum 500 characters. `Enable custom branding <#enable-custom-branding>`__                        |                                                                   |
| must be set to **true** to display the text.                                                                      |                                                                   |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+

.. config:setting:: enable-ask-community-link
  :displayname: Enable Ask Community link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .SupportSettings.EnableAskCommunityLink
  :environment: MM_SUPPORTSETTINGS_ENABLEASKCOMMUNITYLINK
  :description: This setting controls whether a link to the Mattermost Community appears under the **Help** menu in the channel header. Default is **true**.

  - **true**: **(Default)** A link to the `Mattermost Community <https://mattermost.com/community/>`__ appears as **Ask the community** under the **Help** menu in the channel header.
  - **false**: The link does not appear.

Enable Ask Community link
~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
|  - **true**: **(Default)** A link to the `Mattermost Community <https://mattermost.com/community/>`__ appears as **Ask the community** under the **Help** menu in the channel header.                           |  - System Config path: **Site Configuration > Customization**                           |
|  - **false**: The link does not appear.                                                                                                                                                                         |  - ``config.json`` setting: ``SupportSettings`` > ``EnableAskCommunityLink`` > ``true`` |
|                                                                                                                                                                                                                 |  - Environment variable: ``MM_SUPPORTSETTINGS_ENABLEASKCOMMUNITYLINK``                  |
|  The link does not display on mobile apps.                                                                                                                                                                      |                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. config:setting:: help-link
  :displayname: Help link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .SupportSettings.HelpLink
  :environment: MM_SUPPORTSETTINGS_HELPLINK
  :description: This field sets the URL for the Help link on the login and sign-up pages, as well as the **Help Resources** link under the **Help** menu in the channel header. Default value is **https://about.mattermost.com/default-help/**.

Help link
~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| This field sets the URL for the Help link on the login and sign up pages, as well as the **Help Resources** link under the **Help** menu in the channel header.  | - System Config path: **Site Configuration > Customization**      |
|                                                                                                                                                                  | - ``config.json`` setting: ``SupportSettings`` > ``HelpLink``     |
| String input. Default is ``https://about.mattermost.com/default-help/``.                                                                                         | - Environment variable: ``MM_SUPPORTSETTINGS_HELPLINK``           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+

.. note::
  If this value is empty, the Help link is hidden on the login and sign up pages. However, the **Help Resources** link remains available under the **Help** menu.

.. config:setting:: terms-of-use-link
  :displayname: Terms of Use link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .SupportSettings.TermsOfServiceLink
  :environment: MM_SUPPORTSETTINGS_TERMSOFSERVICELINK
  :description: This field sets the URL for the Terms of Use of a self-hosted site. A link to the terms appears at the bottom of the sign-up and login pages.

Terms of Use link
~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| This field sets the URL for the Terms of Use of a self-hosted site. A link to the terms appears at the bottom of the sign-up and login pages.                                                                                                                                                                                                                                                                                                   | - System Config path: **Site Configuration > Customization**            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 | - ``config.json`` setting: ``SupportSettings`` > ``TermsOfServiceLink`` |
| The default URL links to a `Terms of Use <https://mattermost.com/terms-of-use/>`__ page hosted on ``mattermost.com``. This includes the Mattermost Acceptable Use Policy explaining the terms under which Mattermost software is provided to end users. If you change the default link to add your own terms, the new terms **must include a link** to the default terms so end users are aware of the Mattermost Acceptable Use Policy.        | - Environment variable: ``MM_SUPPORTSETTINGS_TERMSOFSERVICELINK``       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                         |
| String input. Default is ``https://about.mattermost.com/default-terms/``.                                                                                                                                                                                                                                                                                                                                                                       |                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

.. note::
  - Customers with a Mattermost subscription may replace or override the Acceptable Use Policy with their own acceptable use or conduct policies, based on contractual terms with Mattermost, so long as your own terms either incorporate the Acceptable Use Policy or include equivalent terms. If you change the default link to add your own terms for using the service you provide, your new terms must include a `link to the default terms <https://mattermost.com/terms-of-use/#acceptable-use-policy>`_ so end users are aware of the Mattermost Acceptable Use Policy for Mattermost software.
  - This setting is applicable to self-hosted deployments only and doesn't change the **Terms of Use** link in the **About Mattermost** window.

.. config:setting:: privacy-policy-link
  :displayname: Privacy Policy link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .SupportSettings.PrivacyPolicyLink
  :environment: MM_SUPPORTSETTINGS_PRIVACYPOLICYLINK
  :description: This field sets the URL for the Privacy Policy of a self-hosted site. A link to the policy appears at the bottom of the sign-up and login pages. Default value is **https://about.mattermost.com/default-privacy-policy/**.

Privacy Policy link
~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| This field sets the URL for the Privacy Policy of a self-hosted site. A link to the policy appears at the bottom of the sign-up and login pages. If this field is empty, the link does not appear. | - System Config path: **Site Configuration > Customization**           |
|                                                                                                                                                                                                    | - ``config.json`` setting: ``SupportSettings`` > ``PrivacyPolicyLink`` |
| String input. Default is ``https://about.mattermost.com/default-privacy-policy/``.                                                                                                                 | - Environment variable: ``MM_SUPPORTSETTINGS_PRIVACYPOLICYLINK``       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. note::
  - This setting is applicable to self-hosted deployments only and doesn't change the **Privacy Policy** link in the **About Mattermost** window. 

.. config:setting:: about-link
  :displayname: About link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .SupportSettings.AboutLink
  :environment: MM_SUPPORTSETTINGS_ABOUTLINK
  :description: This field sets the URL for a page containing general information about a self-hosted site. A link to the About page appears at the bottom of the sign-up and login pages. Default value is **https://about.mattermost.com/default-about/**.

About link
~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+
| This field sets the URL for a page containing general information about a self-hosted site. A link to the About page appears at the bottom of the sign-up and login pages. If this field is empty the link does not appear. | - System Config path: **Site Configuration > Customization**  |
|                                                                                                                                                                                                                             | - ``config.json`` setting: ``SupportSettings`` > ``AboutLink``|
| String input. Default is ``https://about.mattermost.com/default-about/``.                                                                                                                                                   | - Environment variable: ``MM_SUPPORTSETTINGS_ABOUTLINK``      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------+

.. note::
  This setting is applicable to self-hosted deployments only.

.. config:setting:: forgot-password-custom-link
  :displayname: Forgot Password custom link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .SupportSettings.ForgetPasswordLink
  :environment: MM_SUPPORTSETTINGS_FORGOTPASSWORDLINK
  :description: Set a custom URL for the **Forgot Password** link on the Mattermost login page. Leave this field blank to use Mattermost's Password Reset workflow.

Forgot Password custom link
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| When the **Forgot Password** link is enabled on the Mattermost login page,    | - System Config path: **Site Configuration > Forgot password custom link**    |
| users are taken to a custom URL to recover or change their password.          | - ``config.json`` setting: ``SupportSettings`` > ``ForgetPasswordLink``       |
|                                                                               | - Environment variable: ``MM_SUPPORTSETTINGS_FORGETPASSWORDLINK``             |
| Leave this field blank to use Mattermost's Password Reset workflow.           |                                                                               |
+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

.. note::
  This configuration setting applies to all Mattermost clients, including web, desktop app, and mobile app. You can control whether the **Forgot Password** link is visible or hidden in clients by going to **Authentication > Password > Enable Forgot Password Link**. See the :ref:`configuration <administration-guide/configure/authentication-configuration-settings:enable forgot password link>` documentation for details.

.. config:setting:: report-a-problem-type
  :displayname: Report a Problem type (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .SupportSettings.ReportAProblemType
  :environment: MM_SUPPORTSETTINGS_REPORTAPROBLEMTYPE
  :description: Specify how the Report a Problem option behaves in the Mattermost app via the Help menu.

Report a Problem
~~~~~~~~~~~~~~~~~

With self-hosted deployments, you can specify how the **Report a Problem** option behaves in the Mattermost app via the **Help** menu:

- **Default link**: Uses the default Mattermost URL to report a problem. Customers with a Mattermost subscription are directed to the `Mattermost Support Portal <https://support.mattermost.com/hc/en-us/requests/new>`_. Community deployments are directed to `create a new issue on the Mattermost GitHub repository <https://github.com/mattermost/mattermost/issues/new>`_.
- **Email address**: Enables you to :ref:`enter an email address <administration-guide/configure/site-configuration-settings:report a problem email address>` that users will be prompted to send a message to when they choose **Report a Problem** in Mattermost.
- **Custom link**: Enables you to :ref:`enter a URL <administration-guide/configure/site-configuration-settings:report a problem link>` that users will be directed to when they choose **Report a Problem** in Mattermost.
- **Hide link**: Removes the **Report a Problem** option from Mattermost.

.. config:setting:: report-a-problem-link
  :displayname: Report a Problem link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .SupportSettings.ReportAProblemLink
  :environment: MM_SUPPORTSETTINGS_REPORTAPROBLEMLINK
  :description: Users will be directed to this link when they choose Report a Problem in Mattermost.

Report a Problem link
~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| This field sets the URL for the **Report a Problem** link in the channel header **Help** menu.    | - System Config path: **Site Configuration > Customization**            |
| If this field is empty the link does not appear.                                                  | - ``config.json`` setting: ``SupportSettings`` > ``ReportAProblemLink`` |
|                                                                                                   | - Environment variable: ``MM_SUPPORTSETTINGS_REPORTAPROBLEMLINK``       |
| String input. Default is ``https://mattermost.com/pl/report-a-bug``.                              |                                                                         |
+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

.. note::
  This setting is applicable to self-hosted deployments only.

.. config:setting:: report-a-problem-email
  :displayname: Report a Problem email (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .SupportSettings.ReportAProblemMail
  :environment: MM_SUPPORTSETTINGS_REPORTAPROBLMEMAIL
  :description: Enter the email address that users will be prompted to send a message to when they choose Report a Problem in Mattermost.

Report a Problem email address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| This field sets the email address for the **Report a Problem** link in the channel                | - System Config path: **Site Configuration > Customization**            |
| header **Help** menu.                                                                             | - ``config.json`` setting: ``SupportSettings`` > ``ReportAProblemMail`` |
|                                                                                                   | - Environment variable: ``MM_SUPPORTSETTINGS_REPORTAPROBLMEMAIL``       |
| String input. Cannot be left blank.                                                               |                                                                         |
+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

.. note::
  This setting is applicable to self-hosted deployments only.

.. config:setting:: allow-mobile-app-log-downloads
  :displayname: Allow Mobile App Log Downloads (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .SupportSettings.AllowDownloadLogs
  :environment: MM_SUPPORTSETTINGS_ALLOWDOWNLOADLOGS
  :description: When enabled, users can download app logs for troubleshooting. If a Report a Problem link is shown, logs can be downloaded as part of this workflow.

Allow mobile app log downloads
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Enable users to download mobile app logs for troubleshooting.            | - System Config path: **Site Configuration > Customization**            |
| When the **Report a Problem** link is shown, mobile logs can be          | - ``config.json`` setting: ``SupportSettings`` > ``AllowDownloadLogs``  |
| downloaded as part of the reporting flow.                                | - Environment variable: ``MM_SUPPORTSETTINGS_ALLOWDOWNLOADLOGS``        |
|                                                                          |                                                                         |
| - **true** (**Default**): Users can download mobile app logs.            |                                                                         |
| - **false** Users can't download mobile app logs.                        |                                                                         |
+--------------------------------------------------------------------------+-------------------------------------------------------------------------+

.. note::
  This setting is applicable to self-hosted deployments only.

.. config:setting:: mattermost-apps-download-page-link
  :displayname: Mattermost apps download page link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .NativeAppSettings.AppDownloadLink
  :environment: MM_NATIVEAPPSETTINGS_APPDOWNLOADLINK
  :description: This field sets the URL for the Download Apps link in the Product menu. Default value is https://mattermost.com/pl/download-apps.

Mattermost apps download page link
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| This field sets the URL for the Download Apps link in the **Product** menu. If this field is empty, the link does not appear. | - System Config path: **Site Configuration > Customization**           |
|                                                                                                                               | - ``config.json`` setting: ``NativeAppSettings`` > ``AppDownloadLink`` |
| If you have an Enterprise App Store, set the link to the appropriate download page for your Mattermost apps.                  | - Environment variable: ``MM_NATIVEAPPSETTINGS_APPDOWNLOADLINK``       |
|                                                                                                                               |                                                                        |
| String input. Default is ``https://mattermost.com/pl/download-apps``.                                                         |                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. note::
  This setting is applicable to self-hosted deployments only.

.. config:setting:: android-app-download-link
  :displayname: Android app download link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .NativeAppSettings.AndroidAppDownloadLink
  :environment: MM_NATIVEAPPSETTINGS_ANDROIDAPPDOWNLOADLINK
  :description: This field sets the URL to download the Mattermost Android app. Default value is https://mattermost.com/pl/android-app/.

Android app download link
~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| This field sets the URL to download the Mattermost Android app. Users who access the Mattermost site on a mobile browser will be prompted to download the app through this link. If this field is empty, the prompt does not appear. | - System Config path: **Site Configuration > Customization**                  |
|                                                                                                                                                                                                                                      | - ``config.json`` setting: ``NativeAppSettings`` > ``AndroidAppDownloadLink`` |
| If you have an Enterprise App Store, link to your Android app.                                                                                                                                                                       | - Environment variable: ``MM_NATIVEAPPSETTINGS_ANDROIDAPPDOWNLOADLINK``       |
|                                                                                                                                                                                                                                      |                                                                               |
| String input. Default is ``https://mattermost.com/pl/android-app/``.                                                                                                                                                                 |                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

.. note::
  This setting is applicable to self-hosted deployments only.

.. config:setting:: ios-app-download-link
  :displayname: iOS app download link (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: .NativeAppSettings.IosAppDownloadLink
  :environment: MM_NATIVEAPPSETTINGS_IOSAPPDOWNLOADLINK
  :description: This field sets the URL to download the Mattermost iOS app. Default value is https://mattermost.com/pl/ios-app/.

iOS app download link
~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| This field sets the URL to download the Mattermost iOS app. Users who access the site on a mobile browser will be prompted to download the app through this link. If this field is empty, the prompt does not appear. | - System Config path: **Site Configuration > Customization**             |
|                                                                                                                                                                                                                       | - ``config.json`` setting: ``NativeAppSettings`` > ``IosAppDownloadLink``|
| If you use an Enterprise App Store, link to your iOS app.                                                                                                                                                             | - Environment variable: ``MM_NATIVEAPPSETTINGS_IOSAPPDOWNLOADLINK``      |
|                                                                                                                                                                                                                       |                                                                          |
| String input. Default is ``https://mattermost.com/pl/ios-app/``.                                                                                                                                                      |                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

.. note::
  This setting is applicable to self-hosted deployments only.

.. config:setting:: enable-desktop-app-landing-page
  :displayname: Enable desktop app landing page (Customization)
  :systemconsole: Site Configuration > Customization
  :configjson: N/A
  :environment: N/A
  :description: Control whether or not to prompt users to use the Desktop App when first visiting Mattermost from a new browser.
  
  - **true**: **(Default)** Mattermost prompts users to use the desktop app.
  - **false**:  Mattermost doesn't prompt users to use the desktop app.

Enable desktop app landing page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+------------------------------------------------------------------------------------------+
| - **true**: **(Default)** Prompts users to use the desktop app. | - System Config path: **Site Configuration > Customization**                             |
| - **false**: Doesn't prompt users to use the desktop app.       | - ``config.json`` setting: ``ServiceSettings`` > ``EnableDesktopLandingPage`` > ``true`` |
|                                                                 | - Environment variable: ``MM_SERVICESETTINGS_ENABLEDESKTOPLANDINGPAGE``                  |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------+

.. config:setting:: app-custom-url-schemes
  :displayname: App custom URL schemes (Customization)
  :systemconsole: N/A
  :configjson: .NativeAppSettings.AppCustomURLSchemes
  :environment: MM_NativeAppSettings_AppCustomURLSchemes = mmauth:// mmauthbeta://
  :description: Define valid custom URL schemes for redirect links provided by custom-built mobile Mattermost apps.

App custom URL schemes
~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Define valid custom URL schemes for redirect links provided by custom-built mobile Mattermost apps. This ensures users are redirected to the custom-built mobile app and not Mattermost's mobile client.

When configured, after OAuth or SAML user authentication is complete, custom URL schemes sent by mobile clients are validated to ensure they don't include default schemes such as ``http`` or ``https``. Mobile users are then redirected back to the mobile app using the custom scheme URL provided by the mobile client. We recommend that you update your mobile client values as well with valid custom URL schemes.

+------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"NativeAppSettings.AppCustomURLSchemes"`` with an array of strings as input separated by spaces.   |
+------------------------------------------------------------------------------------------------------------------------------------------------+
| For example:                                                                                                                                   |
|                                                                                                                                                |
| - ``MM_NativeAppSettings_AppCustomURLSchemes = mmauth:// mmauthbeta://``                                                                       |
| - Via mmctl: ``mmctl config set NativeAppSettings.AppCustomURLSchemes "mmauth://" "mmauthbeta://"``                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: mobile-external-browser
  :displayname: Mobile external browser (Customization)
  :systemconsole: N/A
  :configjson: NativeAppSettings.MobileExternalBrowser
  :environment: MM_NATIVEAPPSETTINGS_MOBILEEXTERNALBROWSER
  :description: Configure the mobile app to use the default mobile browser to perform SSO authentication. It should be enabled when there are issues with the mobile app SSO redirect flow. Disabled by default.

  - **true**:  The mobile app uses the default internal mobile browser to perform SSO authentication.
  - **false**: **(Default)** The mobile app uses an external mobile browser to perform SSO authentication.

Mobile external browser
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| From Mattermost v10.2 and Mobile v2.2.1, this setting configures the mobile app       | - System Config path: N/A                                                   |
| to use an external mobile browser to perform SSO authentication.                      | - ``config.json`` setting: ``NativeAppSettings.MobileExternalBrowser``      |
|                                                                                       | - Environment variable: ``MM_NATIVEAPPSETTINGS_MOBILEEXTERNALBROWSER``      |
| - **true**:  The mobile app uses the default internal mobile browser to perform SSO   |                                                                             |
|   authentication.                                                                     |                                                                             |
| - **false**: **(Default)** The mobile app uses an external mobile browser to          |                                                                             |
|   perform SSO authentication.                                                         |                                                                             |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

.. note::

  - This setting is applicable to self-hosted deployments only. 
  - We recommend enabling this configuration setting when there are issues with the mobile app SSO redirect flow.

----

Localization
------------

Access the following configuration settings in the System Console by going to **Site Configuration > Localization**. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: default-server-language
  :displayname: Default server language (Localization)
  :systemconsole: Site Configuration > Localization
  :configjson: .LocalizationSettings.DefaultServerLocale
  :environment: MM_LOCALIZATIONSETTINGS_DEFAULTSERVERLOCALE
  :description: The default language for system messages and logs. Default value is **en**.

Default server language
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| The default language for system messages and logs.                             | - System Config path: **Site Configuration > Localization**                    |
|                                                                                | - ``config.json`` setting: ``LocalizationSettings`` > ``DefaultServerLocale``  |
| Options: ``"bg"``, ``"de"``, ``"en"``, ``"en-AU"``, ``"es"``, ``"fa"``,        | - Environment variable: ``MM_LOCALIZATIONSETTINGS_DEFAULTSERVERLOCALE``        |
| ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``,          |                                                                                |
| ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``"uk"``, ``"vi"``,       |                                                                                |
| ``"zh-Hans"``, and ``"zh-Hant"``.                                              |                                                                                |
|                                                                                |                                                                                |
| Default is ``"en"``.                                                           |                                                                                |
+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

.. note::
  Changing this configuration setting changes the default server language for users who haven't set a language preference via **Settings**.        
  Mattermost applies the user's language preference when specified. 

.. config:setting:: default-client-language
  :displayname: Default client language (Localization)
  :systemconsole: Site Configuration > Localization
  :configjson: .LocalizationSettings.DefaultClientLocale
  :environment: MM_LOCALIZATIONSETTINGS_DEFAULTCLIENTLOCALE
  :description: The default language for new users and pages where the user isn't logged in. Default value is **en**.

Default client language
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| The default language for new users and pages where the user isn't logged in.   | - System Config path: **Site Configuration > Localization**                    |
|                                                                                | - ``config.json`` setting: ``LocalizationSettings`` > ``DefaultClientLocale``  |
| Options: ``"bg"``, ``"de"``, ``"en"``, ``"en-AU"``, ``"es"``, ``"fa"``,        | - Environment variable: ``MM_LOCALIZATIONSETTINGS_DEFAULTCLIENTLOCALE``        |
| ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``,          |                                                                                |
| ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``"uk"``, ``"vi"``,       |                                                                                |
| ``"zh-Hans"``, and ``"zh-Hant"``.                                              |                                                                                |
|                                                                                |                                                                                |
| Default is ``"en"``.                                                           |                                                                                |
+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

.. note::
  Changing this configuration setting changes the default client language for users who haven't set a language preference via **Settings**. Mattermost applies the user's language preference when specified.

.. config:setting:: available-languages
  :displayname: Available languages (Localization)
  :systemconsole: Site Configuration > Localization
  :configjson: .LocalizationSettings.AvailableLocales
  :environment: MM_LOCALIZATIONSETTINGS_AVAILABLELOCALES
  :description: Sets the list of languages users see under **Settings > Display > Language**. Default is **en**.

Available languages
~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| Sets the list of languages users see under **Settings > Display > Language**.  | - System Config path: **Site Configuration > Localization**               |
| If this field is left blank, users see all supported languages.                | - ``config.json`` setting: ``LocalizationSettings`` > ``AvailableLocales``|
| Newly supported languages are added automatically.                             | - Environment variable: ``MM_LOCALIZATIONSETTINGS_AVAILABLELOCALES``      |
| If this field is not blank, it must contain the **Default client language**,   |                                                                           |
| in addition to any other languages. For example, to limit the language         |                                                                           |
| choices to US English and Español (es), the string would be ``"en,es"``.       |                                                                           |
|                                                                                |                                                                           |
| Options: ``"bg"``, ``"de"``, ``"en"``, ``"en-AU"``, ``"es"``, ``"fa"``,        |                                                                           |
| ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``,          |                                                                           |
| ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``"uk"``, ``"vi"``,       |                                                                           |
| ``"zh-Hans"``, and ``"zh-Hant"``.                                              |                                                                           |
|                                                                                |                                                                           |
| Default is ``"en"``.                                                           |                                                                           |
+--------------------------------------------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: enable-experimental-locales
  :displayname: Enable experimental locales (Localization)
  :systemconsole: Site Configuration > Localization
  :configjson: EnableExperimentalLocales
  :environment: MM_LOCALIZATIONETTINGS_ENABLEEXPERIMENTALLOCALES
  :description: nable work in progress languages in Mattermost to review translations and identify translation gaps. Default is **false**.

  - **true**: Work in progress languages are available in Mattermost in addition to officially supported languages.
  - **false**: **(Default)** Only officially supported languages are available in Mattermost.

Enable experimental locales
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable work in progress languages in Mattermost to review translations and identify translation gaps.

+--------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| - **true**: Work in progress languages are available   | - System Config path: **Site Configuration > Localization**                                      |
|   in Mattermost in addition to officially supported    | - ``config.json`` setting: ``LocalizationSettings`` > ``EnableExperimentalLocales`` > ``false``  |
|   languages.                                           | - Environment variable: ``MM_LOCALIZATIONETTINGS_ENABLEEXPERIMENTALLOCALES``                     |
| - **false**: **(Default)** Only officially supported   |                                                                                                  |
|   languages are available in Mattermost.               |                                                                                                  |
+--------------------------------------------------------+--------------------------------------------------------------------------------------------------+

.. note::

  - Cloud system admins can request this configuration setting to be enabled for their instance by contacting their Mattermost Account Manager.
  - Work in progress languages may be incomplete. Strings missing translations display in US English.
  - Currently, only web and desktop app product strings are impacted by this configuration setting. Server and mobile product strings aren't impacted by this setting.
  - See the :ref:`language <end-user-guide/preferences/manage-your-display-options:language>` documentation for details on selecting a language preference in Mattermost.

----

Users and teams
---------------

Access the following configuration settings in the System Console by going to **Site Configuration > Users and Teams**.

.. config:setting:: max-users-per-team
  :displayname: Max users per team (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .TeamSettings.MaxUsersPerTeam
  :environment: MM_TEAMSETTINGS_MAXUSERSPERTEAM
  :description: The maximum total number of users per team, including activated and deactivated users. Default is **50** users per team.

Max users per team
~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| The **Max users per team** is the maximum total number of users per team,    | - System Config path: **Site Configuration > Users and Teams**              |
| including activated and deactivated users.                                   | - ``config.json`` setting: ``TeamSettings`` > ``MaxUsersPerTeam`` > ``50``  |
|                                                                              | - Environment variable: ``MM_TEAMSETTINGS_MAXUSERSPERTEAM``                 |
| In Mattermost, a team of people should be a small organization with a        |                                                                             |
| specific goal. In the physical world, a team could sit around a single       |                                                                             |
| table. The default maximum (50) should be enough for most teams, but         |                                                                             |
| with appropriate `hardware <https://docs.mattermost.com/install/             |                                                                             |
| software-hardware-requirements.html>`__, this limit can be increased to      |                                                                             |
| thousands of users.                                                          |                                                                             |
|                                                                              |                                                                             |
| :doc:`Channels </end-user-guide/collaborate/collaborate-within-channels>`    |                                                                             |
| are another way of organizing communications within teams on various topics. |                                                                             |
|                                                                              |                                                                             |
| Numerical input. Default is **50** self-hosted deployments, and **10000**    |                                                                             |
| for Cloud deployments.                                                       |                                                                             |
+------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: max-channels-per-team
  :displayname: Max channels per team (Users and teams)
  :systemconsole: Site Configuration > Users and teams
  :configjson: .TeamSettings.MaxChannelsPerTeam
  :environment: MM_TEAMSETTINGS_MAXCHANNELSPERTEAM
  :description: The maximum number of channels per team, including both active and archived channels. Default is **2000** channels per team.

Max channels per team
~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| The maximum number of channels per team, including both active and archived channels. | - System Config path: **Site Configuration > Users and Teams**                  |
|                                                                                       | - ``config.json`` setting: ``TeamSettings`` > ``MaxChannelsPerTeam`` > ``2000`` |
| Numerical input. Default is **2000** for self-hosted deployments, and **10000**       | - Environment variable: ``MM_TEAMSETTINGS_MAXCHANNELSPERTEAM``                  |
| for Cloud deployments.                                                                |                                                                                 |
+---------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+

.. config:setting:: enable-joinleave-messages-by-default
  :displayname: Enable join/leave messages by default (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .TeamSettings.EnableJoinLeaveMessageByDefault
  :environment: MM_TEAMSETTINGS_ENABLEJOINLEAVEMESSAGEBYDEFAULT
  :description: Specify the default configuration of system messages displayed when users join or leave channels. Default is **true**.

  - **true**: **(Default)** Join/Leave messages are displayed.
  - **false**: Join/Leave messages are hidden.

Enable join/leave messages by default
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Specify the default configuration of system messages displayed when users             | - System Config path: **Site Configuration > Users and Teams**                               |
| join or leave channels.                                                               | - ``config.json`` setting: ``TeamSettings`` > ``EnableJoinLeaveMessageByDefault`` > ``true`` |
|                                                                                       | - Environment variable: ``MM_TEAMSETTINGS_ENABLEJOINLEAVEMESSAGEBYDEFAULT``                  |
| - **true**: **(Default)** Join/Leave messages are displayed.                          |                                                                                              |
| - **false**: Join/Leave messages are hidden.                                          |                                                                                              |
|                                                                                       |                                                                                              |
| Users can override this default by going to **Settings > Advanced >                   |                                                                                              |
| Enable Join/Leave Messages**.                                                         |                                                                                              |
+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+

.. config:setting:: enable-users-to-open-direct-message-channels-with
  :displayname: Enable users to open direct message channels with (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .TeamSettings.RestrictDirectMessage
  :environment: MM_TEAMSETTINGS_RESTRICTDIRECTMESSAGE
  :description: This setting determines whether a user can open a direct message channel with anyone on the Mattermost server or only to members of the same team. Default is **Any user on the Mattermost server**.

  - **Any user on the Mattermost server**: **(Default)** Users can send a direct message to any user through the **Direct Messages > More** menu. ``config.json`` setting: ``"any"``
  - **Any member of the team**: The **Direct Messages > More** menu only allows direct messages to users on the same team. ``config.json`` setting: ``"team"``

Enable users to open direct message channels with
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| This setting determines whether a user can open a direct message channel with anyone on the Mattermost server or only to members of the same team. This setting only affects the options presented in the user interface. It does not affect permissions on the backend server.                                                                                                                                                                                                                                          | - System Config path: **Site Configuration > Users and Teams**         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | - ``config.json`` setting: ``TeamSettings`` > ``RestrictDirectMessage``|
| - **Any user on the Mattermost server**: **(Default)** Users can send a direct message to any user through the **Direct Messages > More** menu. ``config.json`` setting: ``"any"``                                                                                                                                                                                                                                                                                                                                       | - Environment variable: ``MM_TEAMSETTINGS_RESTRICTDIRECTMESSAGE``      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                        |
| - **Any member of the team**: The **Direct Messages > More** menu only allows direct messages to users on the same team. Pressing :kbd:`Ctrl` :kbd:`K` on Windows or Linux, or :kbd:`⌘` :kbd:`K` on Mac, only lists other users on the team currently being viewed. A user who is a member of multiple teams can only send direct messages to the team that is being viewed. However, the user can receive messages from other teams, regardless of the team currently being viewed. ``config.json`` setting: ``"team"`` |                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. config:setting:: teammate-name-display
  :displayname: Teammate name display (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .TeamSettings.TeammateNameDisplay
  :environment: MM_TEAMSETTINGS_TEAMMATENAMEDISPLAY
  :description: This setting determines how names appear in posts and under the **Direct Messages** list. Default is **Show username** for self-hosted deployments and **Show first and last name** for Cloud deployments.

  - **Show username**: **(Default)** Displays usernames. ``config.json`` option: ``"username"``.
  - **Show nickname if one exists...**: Displays the user's nickname. ``config.json`` option: ``"nickname_full_name"``.
  - **Show first and last name**: Displays the user's full name. ``config.json`` option: ``"full_name"``.

Teammate name display
~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| This setting determines how names appear in posts and under the **Direct Messages** list.       | - System Config path: **Site Configuration > Users and Teams**                       |
| Users can change this setting in their interface under **Settings > Display >                   | - ``config.json`` setting: ``TeamSettings`` > ``TeammateNameDisplay`` > ``username`` |
| Teammate Name Display**, unless this setting is locked by a system admin                        | - Environment variable: ``MM_TEAMSETTINGS_TEAMMATENAMEDISPLAY``                      |
| via the **Lock teammate name display for all users** configuration setting.                     |                                                                                      |
|                                                                                                 |                                                                                      |
| - **Show username**: **(Default for self-hosted deployments)** Displays usernames.              |                                                                                      |
|   ``config.json`` option: ``"username"``.                                                       |                                                                                      |
| - **Show nickname if one exists...**: Displays the user's nickname. If the user doesn't have a  |                                                                                      |
|   nickname, their full name is displayed. If the user doesn't have a full name, their username  |                                                                                      |
|   is displayed. ``config.json`` option: ``"nickname_full_name"``.                               |                                                                                      |
| - **Show first and last name**: **(Default for Cloud deployments)** Displays user's full name.  |                                                                                      |
|   If the user doesn't have a full name, their username is displayed. Recommended when using     |                                                                                      |
|   :doc:`SAML </administration-guide/onboard/sso-saml>` or                                       |                                                                                      |
|   :doc:`LDAP </administration-guide/onboard/ad-ldap>` if first name and last name               |                                                                                      |
|   attributes are configured. ``config.json`` option: ``"full_name"``.                           |                                                                                      |
+-------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. config:setting:: lock-teammate-name-display-for-all-users
  :displayname: Lock teammate name display for all users (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .TeamSettings.LockTeammateNameDisplay
  :environment: MM_TEAMSETTINGS_LOCKTEAMMATENAMEDISPLAY
  :description: This setting controls whether users can change settings under **Settings > Display > Teammate Name Display**. Default is **false**.

  - **true**: Users **cannot** change the Teammate Name Display.
  - **false**: **(Default)** Users can change the Teammate Name Display setting.

Lock teammate name display for all users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| This setting controls whether users can change settings under **Settings > Display > Teammate Name Display**. | - System Config path: **Site Configuration > Users and Teams**                        |
|                                                                                                               | - ``config.json`` setting: ``TeamSettings`` > ``LockTeammateNameDisplay`` > ``false`` |
| - **true**: Users **cannot** change the Teammate Name Display.                                                | - Environment variable: ``MM_TEAMSETTINGS_LOCKTEAMMATENAMEDISPLAY``                   |
| - **false**: **(Default)** Users can change the Teammate Name Display setting.                                |                                                                                       |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

.. config:setting:: allow-users-to-view-archived-channels
  :displayname: Allow users to view archived channels (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .TeamSettings.ExperimentalViewArchivedChannels
  :environment: MM_TEAMSETTINGS_EXPERIMENTALVIEWARCHIVEDCHANNELS
  :description: This setting controls whether users can view archived channels.

    - **true**: **(Default)** Allows users to access the content of archived channels of which they were a member.
    - **false**: Users are unable to access content in archived channels.

Allow users to view archived channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| - **true**: **(Default)** Allows users to access the content of archived channels of which they were a member. | - System Config path: **Site Configuration > Users and Teams**                                |
| - **false**: Users are unable to access content in archived channels.                                          | - ``config.json`` setting: ``TeamSettings`` > ``ExperimentalViewArchivedChannels`` > ``true`` |
|                                                                                                                | - Environment variable: ``MM_TEAMSETTINGS_EXPERIMENTALVIEWARCHIVEDCHANNELS``                  |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+

.. note::
  - From Mattermost v11, this configuration setting is always enabled and no longer configurable. Users can always access archived channels where they are members.
  - Cloud admins can't modify this configuration setting.

.. config:setting:: show-email-address
  :displayname: Show email address (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .PrivacySettings.ShowEmailAddress
  :environment: MM_PRIVACYSETTINGS_SHOWEMAILADDRESS
  :description: This setting controls whether users can see the email addresses of other users in the client user interface. Default is **true**.

  - **true**: **(Default)** All users can see the email addresses of every other user.
  - **false**: Hides email addresses in the client user interface, except for system admins and the System Roles with read/write access to Compliance, Billing, or User Management (users/teams/channels/groups etc).

Show email address
~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+ 
| - **true**: **(Default)** All users can see the email addresses of every other user.        | - System Config path: **Site Configuration > Users and teams**                   |
| - **false**: Hides email addresses in the client user interface, except from system admins  | - ``config.json`` setting: ``PrivacySettings`` > ``ShowEmailAddress`` > ``true`` |
|   and the System Roles with read/write access to Compliance, Billing, or User Management    | - Environment variable: ``MM_PRIVACYSETTINGS_SHOWEMAILADDRESS``                  |
|   (users/teams/channels/groups etc).                                                        |                                                                                  |
+---------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: show-full-name
  :displayname: Show full name (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .PrivacySettings.ShowFullName
  :environment: MM_PRIVACYSETTINGS_SHOWFULLNAME
  :description: This setting controls whether users can see the full names of other users in the client user interface. Default is 

  - **true**: **(Default)** Full names are visible to all users in the client user interface.
  - **false**: Hides full names from all users, except system admins.

Show full name
~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| - **true**: **(Default)** Full names are visible to all users in the client user interface.                      | - System Config path: **Site Configuration > Users and Teams**               |
| - **false**: Hides full names from all users, except system admins. Username is shown in place of the full name. | - ``config.json`` setting: ``PrivacySettings`` > ``ShowFullName`` > ``true`` |
|                                                                                                                  | - Environment variable: ``MM_PRIVACYSETTINGS_SHOWFULLNAME``                  |
+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+

.. config:setting:: enable-custom-user-statuses
  :displayname: Enable custom user statuses (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .TeamSettings.EnableCustomUserStatuses
  :environment: MM_TEAMSETTINGS_ENABLECUSTOMUSERSTATUSES
  :description: This setting controls whether users can set custom status messages and emojis that are visible to all users. Default is **true**.

  - **true**: **(Default)** Users can set status messages and emojis that are visible to all users.
  - **false**: Users cannot set custom statuses.

Enable custom user statuses
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| - **true**: **(Default)** Users can set status messages and emojis that are visible to all users. | - System Config path: **Site Configuration > Users and Teams**                        |
| - **false**: Users cannot set custom statuses.                                                    | - ``config.json`` setting: ``TeamSettings`` > ``EnableCustomUserStatuses`` > ``true`` |
|                                                                                                   | - Environment variable: ``MM_TEAMSETTINGS_ENABLECUSTOMUSERSTATUSES``                  |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

.. config:setting:: enable-last-active-time
  :displayname: Enable last active time (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .TeamSettings.EnableLastActiveTime
  :environment: MM_TEAMSETTINGS_ENABLELASTACTIVETIME
  :description: This setting controls whether users can see when deactivated users were last active on a user's profile and in direct message channel headers. Default is **true**.

  - **true**: **(Default)** Users can see when deactivated users were last active on a user's profile and in direct message channel headers.
  - **false**: Users can't see when deactivated users were last online.

Enable last active time
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| - **true**: **(Default)** Users can see when deactivated users were last active on a              | - System Config path: **Site Configuration > Users and Teams**                        |
|   user's profile and in direct message channel headers.                                           | - ``config.json`` setting: ``TeamSettings`` > ``EnableLastActiveTime`` > ``true``     |
| - **false**: Users can't see when deactivated users were last online.                             | - Environment variable: ``MM_TEAMSETTINGS_ENABLELASTACTIVETIME``                      |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

.. config:setting:: enable-custom-user-groups
  :displayname: Enable custom user groups (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: ServiceSettings.EnableCustomGroups
  :environment: MM_SERVICESETTINGS_ENABLECUSTOMGROUPS
  :description: This setting controls whether users with appropriate permissions can create custom user groups, and whether users can @mention custom user groups in Mattermost conversations. Default is **true**.

  - **true**: **(Default)** Users with appropriate permissions can create custom user groups, and users can @mention custom user groups in Mattermost conversations.
  - **false**: Custom user groups cannot be created.

Enable custom user groups
~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| - **true**: **(Default)** Users with appropriate permissions can create custom user groups,       | - System Config path: **Site Configuration > Users and Teams**                     |
|   and users can @mention custom user groups in Mattermost conversations.                          | - ``config.json`` setting: ``ServiceSettings`` > ``EnableCustomGroups`` > ``true`` |
| - **false**: Custom user groups cannot be created.                                                | - Environment variable: ``MM_SERVICESETTINGS_ENABLECUSTOMGROUPS``                  |
+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

.. config:setting:: user-statistics-update-time
  :displayname: User statistics update time (Users and Teams)
  :systemconsole: Site Configuration > Users and Teams
  :configjson: .ServiceSettings.RefreshPostStatsRunTime
  :environment: MM_SERVICESETTINGS_REFRESHPOSTSTATSRUNTIME
  :description: Set the server time for updating the user post statistics, including each user's total message count, and the timestamp of each user's most recently sent message. Default is **00:00**.

User statistics update time
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Set the server time for updating the user post statistics, including each user's total     | - System Config path: **Site Configuration > Users and Teams**                           |
| message count, and the timestamp of each user's most recently sent message.                | - ``config.json`` setting: ``ServiceSettings`` > ``RefreshPostStatsRunTime`` > ``00:00`` |
|                                                                                            | - Environment variable: ``MM_SERVICESETTINGS_REFRESHPOSTSTATSRUNTIME``                   |
| Must be a 24-hour time stamp in the form ``HH:MM`` based on the local time of the server.  |                                                                                          |
| Default is **00:00**.                                                                      |                                                                                          |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+

----

Notifications
-------------

Access the following configuration settings in the System Console by going to **Site Configuration > Notifications**.

.. config:setting:: show-channel-all-or-here-confirmation-dialog
  :displayname: Show @channel, @all, or @here confirmation dialog (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .TeamSettings.EnableConfirmNotificationsToChannel
  :environment: MM_TEAMSETTINGS_ENABLECONFIRMNOTIFICATIONSTOCHANNEL
  :description: This setting controls whether users are prompted to confirm when posting @channel, @all, @here, or group mentions in channels with more than 5 members. Default is **true**.

  - **true**: **(Default)** Requires users to confirm when posting @channel, @all, @here, or group mentions in channels with more than 5 members.
  - **false**: No confirmation is required.

Show @channel, @all, or @here confirmation dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| - **true**: **(Default)** Requires users to confirm when posting @channel, @all, @here, or group mentions in channels with more than 5 members.     | - System Config path: **Site Configuration > Notifications**                                     |
| - **false**: No confirmation is required.                                                                                                           | - ``config.json`` setting: ``TeamSettings`` > ``EnableConfirmNotificationsToChannel`` > ``true`` |
|                                                                                                                                                     | - Environment variable: ``MM_TEAMSETTINGS_ENABLECONFIRMNOTIFICATIONSTOCHANNEL``                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+

.. config:setting:: enable-email-notifications
  :displayname: Enable email notifications (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.SendEmailNotifications
  :environment: MM_EMAILSETTINGS_SENDEMAILNOTIFICATIONS
  :description: This setting controls whether Mattermost sends email notifications for posts. Default is **true**.

  - **true**: **(Default)** Enables automatic email notifications for posts.
  - **false**: Disables notifications.

Enable email notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| - **true**: **(Default)** Enables automatic email notifications for posts.                                                                                                  | - System Config path: **Site Configuration > Notifications**                          |
| - **false**: Disables notifications. A developer may choose this option to speed development by skipping email setup (see also the **Enable preview mode banner** setting). | - ``config.json`` setting: ``EmailSettings`` > ``SendEmailNotifications`` > ``ture``  |
|                                                                                                                                                                             | - Environment variable: ``MM_EMAILSETTINGS_SENDEMAILNOTIFICATIONS``                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

.. note::
  - Cloud admins can't modify this configuration setting.
  - If this setting is **false**, and the SMTP server is set up, account-related emails (such as authentication messages) will be sent regardless of this setting.
  - Email invitations and account deactivation emails aren't affected by this setting.
  - If you don't plan on :doc:`configuring Mattermost for email </administration-guide/configure/smtp-email>`, disabling this configuration setting in larger deployments may improve server performance in the following areas, particularly in high-traffic environments where performance is a key concern:

    - **Reduced Server Load**: Generating and sending emails requires processing power and resources. By disabling email notifications, you reduce the load on the server, which can be reallocated to other tasks.
    - **Decreased I/O Operations**: Sending emails involves input/output (I/O) operations, such as writing to logs and databases, and handling communication with the email server. Reducing these I/O operations can improve overall system efficiency.
    - **Lowered Network Traffic**: Each email sent contributes to network traffic. Disabling email notifications decreases the amount of data being transmitted, which can lead to better performance, especially in environments with limited bandwidth.
    - **Faster Response Times**: With fewer background tasks (like sending emails) to handle, the application can potentially respond to user requests more quickly, improving perceived performance.
    - **Resource Allocation**: Resources like CPU cycles, memory, and network bandwidth that would have been used for sending emails can be used elsewhere, possibly improving the performance of other critical components of the system.
    - However, disabling email notifications can negatively impact user experience, communication efficiency, and overall productivity. It's important to balance performance improvements with the needs of your organization and users.

.. config:setting:: enable-preview-mode-banner
  :displayname: Enable preview mode banner (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.EnablePreviewModeBanner
  :environment: MM_EMAILSETTINGS_ENABLEPREVIEWMODEBANNER
  :description: This setting controls whether users see a banner in the Mattermost client when email notifications are disabled. Default is **true**.

  - **true**: **(Default)** When **Send email notifications** is **false**, users see the Preview Mode banner.
  - **false**: Preview Mode banner does not appear.

.. _email-preview-mode-banner-config:

Enable preview mode banner
~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| - **true**: **(Default)** When **Send email notifications** is **false**, users see the Preview Mode banner. This banner alerts users that email notifications are disabled. | - System Config path: **Site Configuration > Notifications**                          |
| - **false**: Preview Mode banner does not appear.                                                                                                                            | - ``config.json`` setting: ``EmailSettings`` > ``EnablePreviewModeBanner`` > ``true`` |
|                                                                                                                                                                              | - Environment variable: ``MM_EMAILSETTINGS_ENABLEPREVIEWMODEBANNER``                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

.. note::
  Cloud admins can't modify this configuration setting.

.. config:setting:: enable-email-batching
  :displayname: Enable email batching (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.EnableEmailBatching
  :environment: MM_EMAILSETTINGS_ENABLEEMAILBATCHING
  :description: This setting controls whether email notifications for mentions and direct messages are batched into a single email over a given time period. Default is **false**.

  - **true**: Multiple email notifications for mentions and direct messages over a given time period are batched into a single email. Users can customize how often to receive batched notifications.
  - **false**: **(Default)** Emails will be sent for each mention or direct message.

Enable email batching
~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| - **true**: Multiple email notifications for mentions and direct messages       | - System Config path: **Site Configuration > Notifications**                       |
|   over a given time period are batched into a single email.                     | - ``config.json`` setting: ``EmailSettings`` > ``EnableEmailBatching`` > ``false`` |
|                                                                                 | - Environment variable: ``MM_EMAILSETTINGS_ENABLEEMAILBATCHING``                   |
| - **false**: **(Default)** Email notifications are sent for each mention or     |                                                                                    |
|   direct message.                                                               |                                                                                    |
+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

.. note::

  - Cloud admins can't modify this configuration setting.
  - The :ref:`Site Url <administration-guide/configure/environment-configuration-settings:site url>` and :ref:`SMTP Email Server <administration-guide/configure/environment-configuration-settings:smtp server>` must be configured to allow email batching.
  - Regardless of how this setting is configured, users can :ref:`disable email-based notifications altogether <end-user-guide/preferences/manage-your-notifications:email notifications>`.
  - When email batching is enabled, users can :ref:`customize how often to receive batched notifications <end-user-guide/preferences/manage-your-notifications:email notifications>`. The default frequency is 15 minutes.
  - Email batching in :ref:`High Availability Mode <administration-guide/configure/environment-configuration-settings:enable high availability mode>` is planned, but not yet supported.

.. config:setting:: email-notification-contents
  :displayname: Email notification contents (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.EmailNotificationContentsType
  :environment: MM_EMAILSETTINGS_EMAILNOTIFICATIONCONTENTSTYPE
  :description: This setting controls the contents of email notifications sent by the Mattermost system. Default is **Send full message contents**.

  - **Send full message contents**: **(Default)** Email notifications include the full message contents, along with the name of the sender and the channel. ``config.json`` setting: ``"full"``
  - **Send generic description with only sender name**: Only the name of the sender and team name are included in email notifications. ``config.json`` setting: ``"generic"``

Email notification contents
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| - **Send full message contents**: **(Default)** Email notifications include the full message contents, along with the name of the sender and the channel. ``config.json`` setting: ``"full"``                                                                                                 | - System Config path: **Site Configuration > Notifications**                     |
|                                                                                                                                                                                                                                                                                               | - ``config.json`` setting: ``EmailSettings`` > ``EmailNotificationContentsType`` |
| - **Send generic description with only sender name**: Only the name of the sender and team name are included in email notifications. Use this option if Mattermost contains confidential information and policy dictates it cannot be stored in email. ``config.json`` setting: ``"generic"`` | - Environment variable: ``MM_EMAILSETTINGS_EMAILNOTIFICATIONCONTENTSTYPE``       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: notification-display-name
  :displayname: Notification display name (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.FeedbackName
  :environment: MM_EMAILSETTINGS_FEEDBACKNAME
  :description: Display name for email notifications sent from the Mattermost system. No default setting.

Notification display name
~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| Display name for email notifications sent from the Mattermost system.                                  | - System Config path: **Site Configuration > Notifications**      |
|                                                                                                        | - ``config.json`` setting: ``EmailSettings`` > ``FeedbackName``   |
| String input. No default setting. This field is required when changing settings in the System Console. | - Environment variable: ``MM_EMAILSETTINGS_FEEDBACKNAME``         |
+--------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+

.. config:setting:: notification-from-address
  :displayname: Notification from address (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.FeedbackEmail
  :environment: MM_EMAILSETTINGS_FEEDBACKEMAIL
  :description: Email address for notification emails from the Mattermost system. Default value is **test@example.com**.

Notification from address
~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| Email address for notification emails from the Mattermost system. This address should be monitored by a system admin. | - System Config path: **Site Configuration > Notifications**       |
|                                                                                                                       | - ``config.json`` setting: ``EmailSettings`` > ``FeedbackEmail``   |
| String input. Default is ``test@example.com``. This field is required when changing settings in the System Console.   | - Environment variable: ``MM_EMAILSETTINGS_FEEDBACKEMAIL``         |
+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

.. note::
  Cloud admins can't modify this configuration setting.

.. config:setting:: support-email-address
  :displayname: Support email address (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .SupportSettings.SupportEmail
  :environment: MM_SUPPORTSETTINGS_SUPPORTEMAIL
  :description: Sets a user support (or feedback) email address that is displayed on email notifications and during the Getting Started tutorial. Default is feedback@mattermost.com

Support email address
~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+
| Sets a user support (or feedback) email address that is displayed on email notifications and during the Getting Started tutorial. This address should be monitored by a system admin. If no value is set, email notifications will not contain a way for users to request assistance. | - System Config path: **Site Configuration > Notifications**      |
|                                                                                                                                                                                                                                                                                       | - ``config.json`` setting: ``SupportSettings`` > ``SupportEmail`` |
| String input. Default is ``feedback@mattermost.com``. This field is required when changing settings in the System Console.                                                                                                                                                            | - Environment variable: ``MM_SUPPORTSETTINGS_SUPPORTEMAIL``       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+

.. config:setting:: notification-reply-to-address
  :displayname: Notification reply-to address (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.ReplyToAddress
  :environment: MM_EMAILSETTINGS_REPLYTOADDRESS
  :description: Email address used in the reply-to header when sending notification emails from the Mattermost system. Default value is **test@example.com**.

Notification reply-to address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+
| Email address used in the reply-to header when sending notification emails from the Mattermost system. This address should be monitored by a system admin. | - System Config path: **Site Configuration > Notifications**        |
|                                                                                                                                                            | - ``config.json`` setting: ``EmailSettings`` > ``ReplyToAddress``   |
| String input. Default is ``test@example.com``.                                                                                                             | - Environment variable: ``MM_EMAILSETTINGS_REPLYTOADDRESS``         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: notification-footer-mailing-address
  :displayname: Notification footer mailing address (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.FeedbackOrganization
  :environment: MM_EMAILSETTINGS_FEEDBACKORGANIZATION
  :description: Optional setting to include the organization's name and mailing address in the footer of email notifications.

Notification footer mailing address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| Optional setting to include the organization's name and mailing address in the footer of email notifications. If not set, nothing will appear. | - System Config path: **Site Configuration > Notifications**              |
|                                                                                                                                                | - ``config.json`` setting: ``EmailSettings`` > ``FeedbackOrganization``   |
| String input.                                                                                                                                  | - Environment variable: ``MM_EMAILSETTINGS_FEEDBACKORGANIZATION``         |
+------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: push-notification-contents
  :displayname: Push notification contents (Notifications)
  :systemconsole: Site Configuration > Notifications
  :configjson: .EmailSettings.PushNotificationContents
  :environment: MM_EMAILSETTINGS_PUSHNOTIFICATIONCONTENTS
  :description: This setting controls the contents of push notifications sent by the Mattermost system. Default is **Generic description with sender and channel names**.

  - **Generic description with only sender name**: Push notifications include the sender's name, but not the channel name or message contents. ``config.json`` setting: ``"generic_no_channel"``
  - **Generic description with sender and channel names**: **(Default)** Push notifications include the name of the sender and channel, but not the message contents. ``config.json`` setting: ``"generic"``
  - **Full message content sent in the notification payload**: Includes the message contents in the push notification payload. ``config.json`` setting: ``"full"``
  - **Full message content fetched from the server on receipt** (*Available in Mattermost Enterprise*): The notification payload contains no message content; the content is fetched separately. ``config.json`` setting: ``"id_loaded"``

Push notification contents
~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| - **Generic description with only sender name**: Push notifications include the sender's name,         | - System Config path: **Site Configuration > Notifications**                |
|   but not the channel name or message contents. ``config.json`` setting: ``"generic_no_channel"``      | - ``config.json`` setting: ``EmailSettings`` > ``PushNotificationContents`` |
|                                                                                                        | - Environment variable: ``MM_EMAILSETTINGS_PUSHNOTIFICATIONCONTENTS``       |
| - **Generic description with sender and channel names**: **(Default)** Push notifications              |                                                                             |
|   include the name of the sender and channel, but not the message contents.                            |                                                                             |
|   ``config.json`` setting: ``"generic"``                                                               |                                                                             |
|                                                                                                        |                                                                             |
| - **Full message content sent in the notification payload**: Includes the message                      |                                                                             |
|   contents in the push notification payload, which may be sent through                                 |                                                                             |
|   `Apple's Push Notification service <https://developer.apple.com/documentation/usernotifications>`__  |                                                                             |
|   or `Google's Firebase Cloud Messaging <https://firebase.                                             |                                                                             |
|   google.com/docs/cloud-messaging>`__ .                                                                |                                                                             |
|   We **highly recommended** this option only be used with an ``https`` protocol to encrypt             |                                                                             |
|   the connection and protect confidential information. ``config.json`` setting: ``"full"``             |                                                                             |
|                                                                                                        |                                                                             |
| - **Full message content fetched from the server on receipt** (*Available in Mattermost Enterprise*):  |                                                                             |
|   The notification payload contains no message content. Instead it contains a unique message ID used   |                                                                             |
|   to fetch message content from the Mattermost server when a push notification is received via a       |                                                                             |
|   `notification service app extension <https://developer.apple.com/documentation/usernotifications/    |                                                                             |
|   modifying-content-in-newly-delivered-notifications>`_  on iOS or `an expandable notification         |                                                                             |
|   pattern <https://developer.android.com/develop/ui/views/notifications/expanded>`_ on Android.        |                                                                             |
|                                                                                                        |                                                                             |
|   If the server cannot be reached, a generic push notification is displayed without message            |                                                                             |
|   content or sender name. For customers who wrap the Mattermost mobile application in a secure         |                                                                             |
|   container, the container must fetch the message contents using the unique message ID when            |                                                                             |
|   push notifications are received.                                                                     |                                                                             |
|                                                                                                        |                                                                             |
|   If the container is unable to execute the fetch, the push notification contents cannot be received   |                                                                             |
|   by the customer's mobile application without passing the message contents through Apple's or         |                                                                             |
|   Google's notification service. ``config.json`` setting: ``"id_loaded"``                              |                                                                             |
+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: enable-notification-monitoring
  :displayname: Enable notification monitoring (Notification Monitoring)
  :systemconsole: Site Configuration > Notifications
  :configjson: .MetricsSettings.EnableNotificationMetrics
  :environment: MM_METRICSSETTINGS_ENABLENOTIFICATIONMETRICS
  :description: This setting controls whether Mattermost collects notification metrics data for client-side web and desktop app users. Default is **true**.

  - **true**: **(Default)** Mattermost notification data collection is enabled for client-side web and desktop app users.
  - **false**: Mattermost notification data collection is disabled.

Enable notification monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------+----------------------------------------------------------------------------------------------------+
| Enable or disable notification metrics data   | - System Config path: **Environment > Performance Monitoring**                                     |
| collection.                                   | - ``config.json`` setting: ``MetricsSettings`` > ``EnableNotificationMetrics`` > ``true``          |
|                                               | - Environment variable: ``MM_METRICSSETTINGS_ENABLENOTIFICATIONMETRICS``                           |
| - **true**: **(Default)** Mattermost          |                                                                                                    |
|   notification data collection is enabled for |                                                                                                    |
|   client-side web and desktop app users.      |                                                                                                    |
| - **false**: Mattermost notification          |                                                                                                    |
|   data collection is disabled.                |                                                                                                    |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------+

.. note::
  See the :ref:`performance monitoring <administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring:getting started>` documentation 
  to learn more about Mattermost Notification Health metrics.

----

System-wide notifications
-------------------------

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > System-wide notifications**.

.. config:setting:: enable-system-wide-notifications
  :displayname: System-wide notifications
  :systemconsole: Site Configuration > System-wide notifications
  :configjson: .AnnouncementSettings.SystemWideNotifications
  :environment: MM_ANNOUNCEMENTSETTINGS_SYSTEMWIDENOTIFICATIONS
  :description: This setting controls whether system-wide notifications are enabled. Default is **false**.

  - **true**: Enable system-wide notifications that display at the top of the Mattermost interface for all users across all teams.
  - **false**: **(Default)** Disable system-wide notifications.

Enable system-wide notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------+---------------------------------+-------------------------------------------------------------+
| - **true**: Enable system-wide notifications to display at the top    | - System Config path: **Site Configuration > System-wide notifications**                      |
|   of the Mattermost interface for all users across all teams.         | - ``config.json`` setting: ``AnnouncementSettings`` > ``SystemWideNotifications`` > ``false`` |
| - **false**: **(Default)** Disable system-wide notifications.         | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_SYSTEMWIDENOTIFICATIONS``                   |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+

.. config:setting:: banner-text
  :displayname: Banner text (System-wide notifications)
  :systemconsole: Site Configuration > System-wide notifications
  :configjson: .AnnouncementSettings.BannerText
  :environment: MM_ANNOUNCEMENTSETTINGS_BANNERTEXT
  :description: The text of the system-wide notification, when enabled.

Banner text
~~~~~~~~~~~

+------------------------------------------------------------+----------------------------------+--------------------------------------------+
| The text of the system-wide notification, when enabled.    | - System Config path: **Site Configuration > System-wide notifications**      |
|                                                            | - ``config.json`` setting: ``AnnouncementSettings`` > ``BannerText``          |
| String input.                                              | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_BANNERTEXT``                |
+------------------------------------------------------------+-------------------------------------------------------------------------------+

.. config:setting:: banner-color
  :displayname: Banner color (System-wide notifications)
  :systemconsole: Site Configuration > System-wide notifications
  :configjson: .AnnouncementSettings.BannerColor
  :environment: MM_ANNOUNCEMENTSETTINGS_BANNERCOLOR
  :description: The background color of system-wide notifications. Default value is **#f2a93b**.

Banner color
~~~~~~~~~~~~

+-----------------------------------------------------+---------------------------------------------------------------------------------------+
| The background color of system-wide notifications.  | - System Config path: **Site Configuration > System-wide notifications**              |
|                                                     | - ``config.json`` setting: ``AnnouncementSettings`` > ``BannerColor`` > ``"#f2a93b"`` |
| String input of a CSS color value.                  | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_BANNERCOLOR``                       |
+-----------------------------------------------------+---------------------------------------------------------------------------------------+

.. config:setting:: banner-text-color
  :displayname: Banner text color (System-wide notifications)
  :systemconsole: Site Configuration > System-wide notifications
  :configjson: .AnnouncementSettings.BannerTextColor
  :environment: MM_ANNOUNCEMENTSETTINGS_BANNERTEXTCOLOR
  :description: The color of the text in system-wide notifications. Default value is **#333333**.

Banner text color
~~~~~~~~~~~~~~~~~

+------------------------------------------------------+-------------------------------------------------------------------------------------------+
| The color of the text in system-wide notifications.  | - System Config path: **Site Configuration > System-wide notifications**                  |
|                                                      | - ``config.json`` setting: ``AnnouncementSettings`` > ``BannerTextColor`` > ``"#333333"`` |
| String input of a CSS color value.                   | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_BANNERTEXTCOLOR``                       |
+------------------------------------------------------+-------------------------------------------------------------------------------------------+

.. config:setting:: allow-banner-dismissal
  :displayname: Allow banner dismissal (System-wide notifications)
  :systemconsole: Site Configuration > System-wide notifications
  :configjson: .AnnouncementSettings.AllowBannerDismissal
  :environment: MM_ANNOUNCEMENTSETTINGS_ALLOWBANNERDISMISSAL
  :description: This setting controls whether users can dismiss the system-wide notification. Default is **true**.

  - **true**: **(Default)** Users can dismiss the system-wide notification. It will re-appear the next time the user logs in, or when the text is updated by an admin.
  - **false**: Users cannot dismiss the system-wide notification.

Allow banner dismissal
~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| - **true**: **(Default)** Users can dismiss the system-wide notification.   | - System Config path: **Site Configuration > System-wide notifications**                  |
|   It will re-appear the next time the user logs in, and when the text is    | - ``config.json`` setting: ``AnnouncementSettings`` > ``AllowBannerDismissal`` > ``true`` |
|   updated by an admin, or when an admin disables system-wide notifications  | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_ALLOWBANNERDISMISSAL``                  |
|   and reenables them.                                                       |                                                                                           |
| - **false**: Users cannot dismiss the banner.                               |                                                                                           |
+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+

----

Emoji
-----

Access the following configuration settings in the System Console by going to **Site Configuration > Emoji**.

.. config:setting:: enable-emoji-picker
  :displayname: Enable emoji picker (Emoji)
  :systemconsole: Site Configuration > Emoji
  :configjson: .ServiceSettings.EnableEmojiPicker
  :environment: MM_SERVICESETTINGS_ENABLEEMOJIPICKER
  :description: This setting controls whether the emoji picker is enabled when composing messages and for message reactions. Default is **true**.

  - **true**: **(Default)** Enables an emoji picker when composing messages and for message reactions.
  - **false**: Disables the emoji picker in message composition and reactions.

Enable emoji picker
~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| - **true**: **(Default)** Enables an emoji picker when composing messages and for message reactions. | - System Config path: **Site Configuration > Emoji**                              |
| - **false**: Disables the emoji picker in message composition and reactions.                         | - ``config.json`` setting: ``ServiceSettings`` > ``EnableEmojiPicker`` > ``true`` |
|                                                                                                      | - Environment variable: ``MM_SERVICESETTINGS_ENABLEEMOJIPICKER``                  |
+------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+

.. config:setting:: enable-custom-emoji
  :displayname: Enable custom emoji (Emoji)
  :systemconsole: Site Configuration > Emoji
  :configjson: .ServiceSettings.EnableCustomEmoji
  :environment: MM_SERVICESETTINGS_ENABLECUSTOMEMOJI
  :description: This setting controls whether users can add custom emojis to the server. Default is **true**.

  - **true**: Allows users to add up to 6000 emojis through a **Custom Emoji** option in the emoji picker.
  - **false**: **(Default)** Disables custom emojis.

Enable custom emoji
~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| - **true**: **(Default)** Allows users to add up to 6000 emojis through a     | - System Config path: **Site Configuration > Emoji**                               |
|   **Custom Emoji** option in the emoji picker. Emojis can be GIF, PNG, or     | - ``config.json`` setting: ``ServiceSettings`` > ``EnableCustomEmoji`` > ``true``  |
|   JPG files up to 512 KB in size.                                             | - Environment variable: ``MM_SERVICESETTINGS_ENABLECUSTOMEMOJI``                   |
| - **false**:  Disables custom emojis.                                         |                                                                                    |
+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

.. note::
  While Mattermost supports up to 6000 custom emojis, an increase in custom emojis can slow your server's performance.

----

Posts
-----

Access the following configuration settings in the System Console by going to **Site Configuration > Posts**.

.. config:setting:: automatically-follow-threads
  :displayname: Automatically follow threads (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.ThreadAutoFollow
  :environment: MM_SERVICESETTINGS_THREADAUTOFOLLOW
  :description: 

  - **true**: **(Default)** Enables automatic following for all threads that a user starts, or in which the user participates or is mentioned.
  - **false**: Disables automatic following of threads.

Automatically follow threads
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| - **true**: **(Default)** Enables automatic following for all threads that a user starts,       | - System Config path: **Site Configuration > Posts**                             |
|   or in which the user participates or is mentioned. A **Threads** table in the database        | - ``config.json`` setting: ``ServiceSettings`` > ``ThreadAutoFollow`` > ``true`` |
|   tracks threads and thread participants. A **ThreadMembership** table tracks followed threads  | - Environment variable: ``MM_SERVICESETTINGS_THREADAUTOFOLLOW``                  |
|   for each user and whether the thread is read or unread.                                       |                                                                                  |
| - **false**: Disables automatic following of threads.                                           |                                                                                  |
+-------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

.. note::
  - This setting is applicable to self-hosted deployments only.
  - This setting **must** be enabled for :doc:`threaded discussions </end-user-guide/collaborate/organize-conversations>` to function.
  - Enabling this setting does not automatically follow threads based on previous user actions.
    For example, threads a user participated in prior to enabling this setting won't be automatically followed, unless the user adds a new comment or is mentioned
    in the thread.

.. config:setting:: threaded-discussions
  :displayname: Threaded discussions (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.CollapsedThreads
  :environment: MM_SERVICESETTINGS_COLLAPSEDTHREADS
  :description: Controls the availability of `threaded discussions on the server and for users. Default is **Always On**.

  - **Always On**: **(Default)** Enables `threaded discussions <https://docs.mattermost.com/end-user-guide/collaborate/organize-conversations.html>`__ on the server and for all users. ``config.json`` setting: ``"always_on"``
  - **Default On**: Enables threaded discussions on the server and for all users. ``config.json`` setting: ``"default_on"``
  - **Default Off**: Enables threaded discussions on the server but **not** for users. ``config.json`` setting: ``"default_off"``
  - **Disabled**: Users cannot enable threaded discussions. ``config.json`` setting: ``"disabled"``

Threaded discussions
~~~~~~~~~~~~~~~~~~~~~

.. important::

  Customers upgrading from a legacy Mattermost release prior to v7.0 must review the `administrator's guide to enabling threaded discussions <https://support.mattermost.com/hc/en-us/articles/6880701948564-Administrator-s-guide-to-enabling-Collapsed-Reply-Threads>`_ (formerly known as Collapsed Reply Threads) prior to enabling this functionality.

+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+
| - **Always On**: **(Default)** Enables :doc:`threaded discussions                                             | - System Config path: **Site Configuration > Posts**                      |
|   </end-user-guide/collaborate/organize-conversations>`                                                       | - ``config.json`` setting: ``ServiceSettings`` > ``CollapsedThreads``     |
|   on the server and for all users. This is the recommended configuration for optimal user experience          | - Environment variable: ``MM_SERVICESETTINGS_COLLAPSEDTHREADS``           |
|   and to ensure consistency in how users read and respond to threaded conversations.                          |                                                                           |
|   ``config.json`` setting: ``"always_on"``                                                                    |                                                                           |
| - **Default On**: Enables threaded discussions on the server and for all users.                               |                                                                           |
| - **Default Off**: Enables threaded discussions on the server but **not** for users.                          |                                                                           |
| - **Disabled**: Users cannot enable threaded discussions. ``config.json`` setting: ``"disabled"``             |                                                                           |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: message-priority
  :displayname: Message priority (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.PostPriority
  :environment: MM_SERVICESETTINGS_POSTPRIORITY
  :description: This setting enables users to set a visual indicator for important or urgent root messages. Default is **true**.

  - **true**: **(Default)** Enables message priority for all users.
  - **false**: Disables the ability to set message priority and request acknowlegements.

Message priority
~~~~~~~~~~~~~~~~~

.. tip::
  `Mattermost Enterprise or Professional <https://mattermost.com/pricing>`__ customers can additionally request message acknowledgements to
  track that specific, time-sensitive messages have been seen and actioned. See the :doc:`message priority </end-user-guide/collaborate/message-priority>` documentation to learn more.

+-----------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| - **true**: **(Default)** Enables message priority for all users which      | - System Config path: **Site Configuration > Posts**                             |
|   enables them to set a visual indiciator for important or urgent root      | - ``config.json`` setting: ``ServiceSettings`` > ``PostPriority`` > ``true``     |
|   messages.                                                                 | - Environment variable: ``MM_SERVICESETTINGS_POSTPRIORITY``                      |
| - **false**: Disables the ability to set message priority and request       |                                                                                  |
|   acknowledgements.                                                         |                                                                                  |
+-----------------------------------------------------------------------------+----------------------------------------------------------------------------------+

.. note::

  Disabling this configuration setting in larger deployments may improve server performance in the following areas, particularly in environments where performance and responsiveness are critical:

  - Simplified Processing: When post priority is enabled, the system has to manage and prioritize posts based on their designated priority levels. This adds additional processing overhead as the system must evaluate and sort posts accordingly. By disabling this feature, all posts are treated equally, which simplifies the processing logic and reduces the computational load.
  - Reduced Latency: With post priority enabled, there might be delays introduced while the system determines the priority of each post and processes them in the correct order. Disabling post priority can lead to more consistent and potentially quicker handling of posts because the system processes them on a first-come, first-served basis.
  - Lower Resource Utilization: Managing post priorities can consume additional system resources such as CPU and memory. Disabling this feature can free up these resources, allowing the system to allocate them to other tasks, thereby improving overall performance.
  - Improved Scalability: In a high-traffic environment, the complexity of managing post priorities can become more pronounced. Disabling this feature simplifies the system's operations, making it easier to scale as the number of users and posts increases.

.. config:setting:: persistent-notifications
  :displayname: Persistent notifications (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.AllowPersistentNotifications
  :environment: MM_SERVICESETTINGS_ALLOWPERSISTENTNOTIFICATIONS
  :description: This setting controls whether users can send repeating notifications to mentioned recipients of urgent messages. Default is **true**.

  - **true**: **(Default)** Users can trigger repeating notifications to mentioned recipients of urgent messages.
  - **false**: Disables the ability to send repeating notifications.

Persistent notifications
~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| - **true**: **(Default)** Users can trigger repeating notifications to   | - System Config path: **Site Configuration > Posts**                                          |
|   mentioned recipients of urgent messages.                               | - ``config.json`` setting: ``ServiceSettings`` > ``AllowPersistentNotifications`` > ``true``  |
| - **false**: Disables the ability to send repeating notifications.       | - Environment variable: ``MM_SERVICESETTINGS_ALLOWPERSISTENTNOTIFICATIONS``                   |
+--------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+

.. config:setting:: maximum-number-of-recipients-for-persistent-notifications
  :displayname: Maximum number of recipients for persistent notifications (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.PersistentNotificationMaxRecipients
  :environment: MM_SERVICESETTINGS_PERSISTENTNOTIFICATIONMAXRECIPIENTS
  :description: The maximum number of recipients users may send persistent notifications to. Default is **5**.

Maximum number of recipients for persistent notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| The maximum number of recipients users may send persistent    | - System Config path: **Site Configuration > Posts**                                              |
| notifications to.                                             | - ``config.json`` setting: ``ServiceSettings`` > ``PersistentNotificationMaxRecipients`` > ``5``  |
|                                                               | - Environment variable: ``MM_SERVICESETTINGS_PERSISTENTNOTIFICATIONMAXRECIPIENTS``                |
| Numerical input. Default is **5**.                            |                                                                                                   |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

.. config:setting:: frequency-of-persistent-notifications
  :displayname: Frequency of persistent notifications (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.PersistentNotificationIntervalMinutes
  :environment: MM_SERVICESETTINGS_PERSISTENTNOTIFICATIONINTERVALMINUTES
  :description: The number of minutes between repeated notifications for urgent messages sent with persistent notifications. Default is **5**.

Frequency of persistent notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| The number of minutes between repeated notifications for      | - System Config path: **Site Configuration > Posts**                                                |
| urgent messages sent with persistent notifications.           | - ``config.json`` setting: ``ServiceSettings`` > ``PersistentNotificationIntervalMinutes`` > ``5``  |
|                                                               | - Environment variable: ``MM_SERVICESETTINGS_PERSISTENTNOTIFICATIONINTERVALMINUTES``                |
| Numerical input. Default is **5**. Minimum is **2**.          |                                                                                                     |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+

.. config:setting:: total-number-of-persistent-notifications-per-post
  :displayname: Total number of persistent notifications per post (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.PersistentNotificationMaxCount
  :environment: MM_SERVICESETTINGS_PERSISTENTNOTIFICATIONMAXCOUNT
  :description: The maximum number of times users may receive persistent notifications. Default is **6**.

Total number of persistent notifications per post
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| The maximum number of times users may receive persistent    | - System Config path: **Site Configuration > Posts**                                         |
| notifications.                                              | - ``config.json`` setting: ``ServiceSettings`` > ``PersistentNotificationMaxCount`` > ``6``  |
|                                                             | - Environment variable: ``MM_SERVICESETTINGS_PERSISTENTNOTIFICATIONMAXCOUNT``                |
| Numerical input. Default is **6**.                          |                                                                                              |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------+

.. config:setting:: enable-burn-on-read
  :displayname: Enable burn-on-read messages (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.EnableBurnOnRead
  :environment: MM_SERVICESETTINGS_ENABLEBURNONREAD
  :description: Controls whether users can send burn-on-read messages. Default is **false**.

  - **true**: Users can send burn-on-read messages in channels, direct messages, and group messages.
  - **false**: **(Default)** The option to send a burn-on-read message isn't available.

Enable burn-on-read messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/entry-adv.rst
  :start-after: :nosearch:

:ref:`Burn-on-read messages <end-user-guide/collaborate/send-messages:send burn-on-read messages>` have irreversible behavior:

- Once a recipient reveals a burn-on-read message, it can't be hidden again.
- Once a burn-on-read message expires or is burned, it is permanently deleted and can't be recovered.
- Recipients can't reply to, edit, or thread burn-on-read messages.

+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| Enable or disable burn-on-read messages.                                                                   | - System Config path: **Site Configuration > Posts**                               |
|                                                                                                            | - ``config.json`` setting: ``ServiceSettings`` > ``EnableBurnOnRead`` > ``false``  |
| - **false**: **(Default)** The option to send a burn-on-read message isn't available.                      | - Environment variable: ``MM_SERVICESETTINGS_ENABLEBURNONREAD``                    |
| - **true**: Users can send burn-on-read messages in channels, direct messages, and group messages.         |                                                                                    |
+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

.. note::
  Disabling this feature prevents users from sending new burn-on-read messages. Once disabled, users can interact with existing burn-on-read messages.

.. config:setting:: burn-on-read-duration
  :displayname: Burn-on-read duration (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.BurnOnReadDurationSeconds
  :environment: MM_SERVICESETTINGS_BURNONREADDURATIONSECONDS
  :description: Sets the countdown duration for burn-on-read messages once they are revealed. Default is **10 minutes**.

Burn-on-read duration
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/entry-adv.rst
  :start-after: :nosearch:

+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Sets the countdown duration for burn-on-read messages once they are revealed. After a recipient reveals a burn-on-read message,   | - System Config path: **Site Configuration > Posts**                                                |
| the message is deleted for that user after the specified duration. This setting applies to all burn-on-read messages.             | - ``config.json`` setting: ``ServiceSettings`` > ``BurnOnReadDurationSeconds`` > ``600``            |
|                                                                                                                                   | - Environment variable: ``MM_SERVICESETTINGS_BURNONREADDURATIONSECONDS``                            |
| Numerical input in seconds. Default is **600** seconds (10 minutes).                                                              |                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+

.. config:setting:: burn-on-read-maximum-time-to-live
  :displayname: Maximum time to live for burn-on-read messages (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.BurnOnReadMaximumTimeToLiveSeconds
  :environment: MM_SERVICESETTINGS_BURNONREADMAXIMUMTIMETOLIVESECONDS
  :description: Sets the maximum duration that burn-on-read messages can exist after they are sent. Default is **7 days**.

Maximum time to live for burn-on-read messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/entry-adv.rst
  :start-after: :nosearch:

+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Sets the maximum duration that burn-on-read messages can exist after they are sent. The message is deleted after the specified      | - System Config path: **Site Configuration > Posts**                                                 |
| duration, even if it hasn't been revealed by all recipients.                                                                        | - ``config.json`` setting: ``ServiceSettings`` > ``BurnOnReadMaximumTimeToLiveSeconds`` > ``604800`` |
|                                                                                                                                     | - Environment variable: ``MM_SERVICESETTINGS_BURNONREADMAXIMUMTIMETOLIVESECONDS``                    |
| Numerical input in seconds. Default is **604800** seconds (7 days).                                                                 |                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

.. config:setting:: enable-website-link-previews
  :displayname: Enable website link previews (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.EnableLinkPreviews
  :environment: MM_SERVICESETTINGS_ENABLELINKPREVIEWS
  :description: This setting controls whether the server generates previews for website, image, and YouTube links. Default is **false**.

  - **true**: The server generates a preview of the first website, image, or YouTube video linked in a message.
  - **false**: **(Default)** All previews are disabled and the server does not request metadata for any links contained in messages.

Enable website link previews
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::

  The server must be connected to the internet to generate previews. This connection can be established through a :ref:`firewall or outbound proxy <deployment-guide/server/preparations:outbound proxy configuration>` if necessary.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| - **true**: The server generates a preview of the first website, image, or YouTube video linked in a message. Users can disable website previews, but not image or YouTube previews, under **Settings > Display > Website Link Previews**. | - System Config path: **Site Configuration > Posts**                               |
| - **false**: **(Default)** All previews are disabled and the server does not request metadata for any links contained in messages.                                                                                                         | - ``config.json`` setting: ``ServiceSettings`` > ``EnableLinkPreviews`` > ``true`` |
|                                                                                                                                                                                                                                            | - Environment variable: ``MM_SERVICESETTINGS_ENABLELINKPREVIEWS``                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

.. note::

  Disabling this configuration setting in larger deployments may improve server performance in the following areas:

  - Reduced Network Requests: When link previews are enabled, the system needs to fetch metadata (such as title, description, or image) from the linked webpage. This requires additional network requests, which can slow down the system.
  - Lower Server Load: Creating link previews involves parsing the content of the linked pages. If many users are sharing links, the server will have to perform numerous network requests and process a lot of additional data, increasing the load on the server.
  - Less Data Processing: Every link shared needs to be processed to extract the necessary preview information. This processing consumes CPU and memory resources, which can otherwise be reserved for other tasks.
  - Decreased Client-Side Rendering Time: On the client side, rendering link previews (adding text, images, and layouts) takes time and resources. Disabling link previews means that clients do not need to render these elements, leading to faster message display.
  - Saved Bandwidth: Link previews often include images and other data from the linked content. By disabling them, you save the bandwidth that would be used to download these additional resources.
  - However, disabling link previews can negatively impact user experience, communication efficiency, and overall productivity. It's important to balance performance improvements with the needs of your organization and users.

.. config:setting:: disable-link-previews-for-specific-domains
  :displayname: Disable link previews for specific domains (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.RestrictLinkPreviews
  :environment: MM_SERVICESETTINGS_RESTRICTLINKPREVIEWS
  :description: Use this setting to disable previews of links for specific domains.

Disable link previews for specific domains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| Use this setting to disable previews of links for specific domains.                                      | - System Config path: **Site Configuration > Posts**                        |
|                                                                                                          | - ``config.json`` setting: ``ServiceSettings`` > ``RestrictLinkPreviews``   |
| String input of a comma-separated list of domains, for example: ``"mattermost.com, images.example.com"`` | - Environment variable: ``MM_SERVICESETTINGS_RESTRICTLINKPREVIEWS``         |
+----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: enable-message-link-previews
  :displayname: Enable message link previews (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.EnablePermalinkPreviews
  :environment: MM_SERVICESETTINGS_ENABLEPERMALINKPREVIEWS
  :description: This setting controls whether message link previews are enabled. Default is **true**.

  - **true**: **(Default)** `Share links to Mattermost messages <https://docs.mattermost.com/end-user-guide/collaborate/share-links.html>`__ will generate a preview for any users that have access to the original message.
  - **false**: Share links do not generate a preview.

Enable message link previews
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| - **true**: **(Default)** :doc:`Share links to Mattermost messages </end-user-guide/collaborate/share-links>`       | - System Config path: **Site Configuration > Posts**                                    |
|   will generate a preview for any users that have access to the original message.                                   | - ``config.json`` setting: ``ServiceSettings`` > ``EnablePermalinkPreviews`` > ``true`` |
| - **false**: Share links do not generate a preview.                                                                 | - Environment variable: ``MM_SERVICESETTINGS_ENABLEPERMALINKPREVIEWS``                  |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. note::

  Disabling this configuration setting in larger deployments may improve server performance in the following areas, particularly in environments with high message throughput or limited resources:

  - Reduced Server Load: When permalink previews are enabled, the server has to generate preview summaries for each shared link. This generates additional requests to fetch metadata and may involve parsing web pages, which increases the processing load on the server.
  - Less Data Transfer: Permalink previews include additional metadata such as images, titles, and descriptions. Disabling previews reduces the amount of data that needs to be transferred, which can decrease bandwidth usage and improve message load times, particularly for channels with a high volume of links.
  - Faster Message Rendering: On the client-side, rendering messages with multimedia previews takes more time compared to plain text messages. Disabling previews can reduce rendering complexity and improve client performance, especially on devices with limited resources.
  - Network Latency: Fetching metadata for link previews may introduce network latency, as the server must reach out to external resources. Disabling this can eliminate these delays, ensuring faster message processing and display.
  - Simplified Message Handling: In the absence of previews, messages are simpler and less resource-intensive to store, retrieve, and display. This can contribute to overall improved system responsiveness and efficiency.
  - However, disabling permalink previews can negatively impact user experience, communication efficiency, and overall productivity. It's important to balance performance improvements with the needs of your organization and users.

.. config:setting:: enable-svgs
  :displayname: Enable SVGs (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.EnableSVGs
  :environment: MM_SERVICESETTINGS_ENABLESVGS
  :description: This setting controls whether previews of SVG files attached to messages are enabled. Default is **false**.

  - **true**: Enables previews of SVG files attached to messages.
  - **false**: **(Default)** Disables previews of SVG files.

Enable SVGs
~~~~~~~~~~~

+-------------------------------------------------------------------------------+----------------------------------------------------------------------------+
| - **true**: Enables previews of SVG files attached to messages.               | - System Config path: **Site Configuration > Posts**                       |
| - **false**: **(Default)** Disables previews of SVG files.                    | - ``config.json`` setting: ``ServiceSettings`` > ``EnableSVGs`` > ``false``|
|                                                                               | - Environment variable: ``MM_SERVICESETTINGS_ENABLESVGS``                  |
+-------------------------------------------------------------------------------+----------------------------------------------------------------------------+

.. warning::
  Enabling SVGs is not recommended in environments where not all users are trusted.

.. config:setting:: enable-latex-code-block-rendering
  :displayname: Enable LaTeX code block rendering (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.EnableLatex
  :environment: MM_SERVICESETTINGS_ENABLELATEX
  :description: This setting controls whether LaTeX code blocks are rendered as images. Default is **false**.

  - **true**: Enables rendering of `LaTeX in code blocks <https://docs.mattermost.com/end-user-guide/collaborate/format-messages.html#math-formulas>`__.
  - **false**: **(Default)** Disables rendering in blocks. Instead, LaTeX code is highlighted.

Enable LaTeX code block rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| - **true**: Enables rendering of :ref:`LaTeX in code blocks <end-user-guide/collaborate/format-messages:math formulas>`.                           | - System Config path: **Site Configuration > Posts**                        |
| - **false**: **(Default)** Disables rendering in blocks. Instead, LaTeX code is highlighted.                                                       | - ``config.json`` setting: ``ServiceSettings`` > ``EnableLatex`` > ``false``|
|                                                                                                                                                    | - Environment variable: ``MM_SERVICESETTINGS_ENABLELATEX``                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

.. warning::
  Enabling LaTeX rendering is not recommended in environments where not all users are trusted.

.. config:setting:: enable-inline-latex-rendering
  :displayname: Enable inline LaTeX rendering (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.EnableInlineLatex
  :environment: MM_SERVICESETTINGS_ENABLEINLINELATEX
  :description: This setting controls whether inline LaTeX in message text is rendered. Default is **false**.

  - **true**: Enables rendering of `LaTeX in message text <https://docs.mattermost.com/end-user-guide/collaborate/format-messages.html#math-formulas>`__.
  - **false**: **(Default)** Disables inline rendering of LaTeX. Instead, LaTeX in message text is highlighted.

Enable inline LaTeX rendering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| - **true**: Enables rendering of                                                                                        | - System Config path: **Site Configuration > Posts**                               |
|   :ref:`LaTeX in message text <end-user-guide/collaborate/format-messages:math formulas>`.                              | - ``config.json`` setting: ``ServiceSettings`` > ``EnableInlineLatex`` > ``false`` |
| - **false**: **(Default)** Disables inline rendering of LaTeX. Instead, LaTeX in message text is highlighted.           | - Environment variable: ``MM_SERVICESETTINGS_ENABLEINLINELATEX``                   |
|   LaTeX can also be rendered in a code block, if that feature is enabled. See **Enable LaTeX code block rendering**.    |                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------+

.. warning::
  Enabling LaTeX rendering isn't recommended in environments where not all users are trusted.

.. config:setting:: custom-url-schemes
  :displayname: Custom URL schemes (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .DisplaySettings.CustomURLSchemes
  :environment: MM_DISPLAYSETTINGS_CUSTOMURLSCHEMES
  :description: A list of URL schemes that will automatically create a link in message text.

Custom URL schemes
~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| A list of URL schemes that will automatically create a link in message text, for example: ``["git", "smtp"]``. These schemes always create links: ``http``, ``https``, ``ftp``, ``tel``, and ``mailto``. | - System Config path: **Site Configuration > Posts**                            |
|                                                                                                                                                                                                          | - ``config.json`` setting: ``DisplaySettings`` > ``CustomURLSchemes`` > ``[]``  |
| ``config.json`` setting: an array of strings                                                                                                                                                             | - Environment variable: ``MM_DISPLAYSETTINGS_CUSTOMURLSCHEMES``                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+

.. config:setting:: maximum-markdown-nodes
  :displayname: Maximum Markdown nodes (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .DisplaySettings.MaxMarkdownNodes
  :environment: MM_DISPLAYSETTINGS_MAXMARKDOWNNODES
  :description: The maximum number of Markdown elements that can be included in a single piece of text in a message. Default is 0 which applies a Mattermost-specified limit.

Maximum Markdown nodes
~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+---------------------------------------------------------------------------------+
| The maximum number of Markdown elements (such as emojis,    | - System Config path: **Site Configuration > Posts**                            |
| links, or table cells), that can be included in a single    | - ``config.json`` setting: ``DisplaySettings`` > ``MaxMarkdownNodes`` > ``0``   |
| piece of text in a message.                                 | - Environment variable: ``MM_DISPLAYSETTINGS_MAXMARKDOWNNODES``                 |
|                                                             |                                                                                 |
| Numerical input. Default is **0** which applies a           |                                                                                 |
| Mattermost-specified limit.                                 |                                                                                 |
+-------------------------------------------------------------+---------------------------------------------------------------------------------+

.. note::
  This limit applies to all Mattermost clients, including web, desktop app, and mobile app.
  
.. config:setting:: google-api-key
  :displayname: Google API key (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.GoogleDeveloperKey
  :environment: MM_SERVICESETTINGS_GOOGLEDEVELOPERKEY
  :description: If a key is provided in this setting, Mattermost displays titles of embedded YouTube videos and detects if a video is no longer available.

Google API key
~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| If a key is provided in this setting, Mattermost displays titles of embedded YouTube videos and detects if a video is no longer available. Setting a key should also prevent Google from throttling access to embedded videos that receive a high number of views. | - System Config path: **Site Configuration > Posts**                    |
|                                                                                                                                                                                                                                                                    | - ``config.json`` setting: ``ServiceSettings`` > ``GoogleDeveloperKey`` |
| String input.                                                                                                                                                                                                                                                      | - Environment variable: ``MM_SERVICESETTINGS_GOOGLEDEVELOPERKEY``       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

.. note::

  - This setting is applicable to self-hosted deployments only.
  - This key is used in client-side Javascript, and must have the YouTube Data API added as a service.

.. config:setting:: enable-server-syncing-of-message-drafts
  :displayname: Enable server syncing of message drafts (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.AllowSyncedDrafts
  :environment: MM_SERVICESETTINGS_ALLOWSYNCEDDRAFTS
  :description: Enable or disable the ability to synchronize draft messages across all supported Mattermost clients. Default is **true**.

  - **true**: **(Default)** Message drafts are saved on the server and may be accessed from different clients. Users may still disable server synchronization of draft messages by going to **Settings > Advanced Settings**.
  - **false**:   Draft messages are stored locally on each device.

Enable server syncing of message drafts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+------------------------------------------------------------------------------------------+
| Enable or disable the ability to synchronize draft   | - System Config path: **Site Configuration > Posts**                                     |
| messages across all supported Mattermost clients.    | - ``config.json`` setting: ``ServiceSettings`` > ``AllowSyncedDrafts`` > ``true``        |
|                                                      | - Environment variable: ``MM_SERVICESETTINGS_ALLOWSYNCEDDRAFTS``                         |
| - **true**: **(Default)** Message drafts are saved   |                                                                                          |
|   on the server and may be accessed from different   |                                                                                          |
|   clients. Users may still disable server            |                                                                                          |
|   synchronization of draft messages by going         |                                                                                          |
|   to **Settings > Advanced Settings**.               |                                                                                          |
| - **false**: Draft messages are stored locally       |                                                                                          |
|   on each device.                                    |                                                                                          |
+------------------------------------------------------+------------------------------------------------------------------------------------------+

.. note::

  While drafts can be very useful for maintaining work continuity, especially in collaborative environments, disabling draft synchronization across devices can lead to noticeable performance improvements by reducing the computational and data management overhead as follows:

  - Reduced Data Synchronization: When drafts are enabled and synchronized across devices, the system needs to handle those data synchronization operations which can consume significant bandwidth and computing resources. Disabling draft syncing reduces the load on servers and networks.
  - Lower Storage Usage: Storing drafts requires additional database operations and storage space. Each draft is an extra piece of data that needs to be saved, managed, and retrieved. Without drafts, the system has fewer records to keep, which can streamline database operations.
  - Decreased Client Processing: On the client side, draft management involves monitoring changes, saving drafts periodically, and handling conflict resolution if multiple drafts are edited from different devices. Disabling drafts reduces these client-side processes, thus freeing up memory and CPU resources.
  - Simplified Architecture: Maintaining synced drafts often requires complex backend logic to ensure consistency and avoid data conflicts. Simplifying this architecture by removing draft syncing can lead to more efficient and faster backend operations.
  - Improved User Experience: Users may experience faster load times and reduced latency without the overhead of draft syncing. This can be particularly noticeable in environments with limited or variable internet connectivity.
  - However, disabling draft synchronization can negatively impact user experience, communication efficiency, and overall productivity. It's important to balance performance improvements with the needs of your organization and users.

.. config:setting:: unique-emoji-reaction-limit
  :displayname: Unique emoji reaction limit (Posts)
  :systemconsole: Site Configuration > Posts
  :configjson: .ServiceSettings.UniqueEmojiReactionLimitPerPost
  :environment: MM_SERVICESETTINGS_UNIQUEEMOJIREACTIONLIMITPERPOST
  :description: Limit the number of unique emoji reactions on each post. Default is 50. Maximum is 500.

Unique emoji reaction limit
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Limit the number of unique emoji reactions on each   | - System Config path: **Site Configuration > Posts**                                               |
| message. Increasing this limit can lead to poor      | - ``config.json`` setting: ``ServiceSettings`` > ``UniqueEmojiReactionLimitPerPost`` > ``50``      |
| client performance.                                  | - Environment variable: ``MM_SERVICESETTINGS_UNIQUEEMOJIREACTIONLIMITPERPOST``                     |
|                                                      |                                                                                                    |
| Numerical input. Default is **50**. Maximum is 500.  |                                                                                                    |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------+

----

Content flagging
----------------

.. include:: ../../_static/badges/entry-adv.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Site Configuration > Content Flagging**.

.. config:setting:: enable-content-flagging
  :displayname: Enable content flagging (Content flagging)
  :systemconsole: Site Configuration > Content Flagging
  :configjson: .ContentFlaggingSettings.EnableContentFlagging
  :environment: MM_CONTENTFLAGGINGSETTINGS_ENABLECONTENTFLAGGING
  :description: Enable or disable the Content Flagging feature. Default is **false**.

  - **true**: Enables the Content Flagging feature.
  - **false**: **(Default)** Disables the Content Flagging feature.

Enable content flagging
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| - **true**: Enables the Content Flagging feature.    | - System Config path: **Site Configuration > Content Flagging**                                    |
| - **false**: **(Default)** Disables the feature.     | - ``config.json`` setting: ``ContentFlaggingSettings`` > ``EnableContentFlagging`` > ``false``     |
|                                                      | - Environment variable: ``MM_CONTENTFLAGGINGSETTINGS_ENABLECONTENTFLAGGING``                       |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------+

.. config:setting:: content-flagging-notification-settings
  :displayname: Notification settings (Content flagging)
  :systemconsole: Site Configuration > Content Flagging
  :configjson: .ContentFlaggingSettings.NotificationSettings.EventTargetMapping
  :environment: N/A
  :description: Map content‑flagging events to who gets notified by the system bot. The value is an object where each key is an event name and each value is an array of recipients. Supported events: ``flagged``, ``assigned``, ``removed``, ``dismissed``. Supported recipients: ``reviewers``, ``author``, ``reporter``. Defaults are shown below.

Notification settings
~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| Default notification recipients for each event:      | - System Config path: **Site Configuration > Content Flagging**                                             |
|                                                      | - ``config.json`` setting: ``ContentFlaggingSettings`` > ``NotificationSettings`` > ``EventTargetMapping``  |
| - Events: flagged, assigned, removed, dismissed      | - Environment variable: N/A                                                                                 |
| - Recipients: reviewers, author, reporter            |                                                                                                             |
|                                                      |                                                                                                             |
| Default mappings include:                            |                                                                                                             |
|                                                      |                                                                                                             |
| - flagged = reviewers                                |                                                                                                             |
| - assigned = reviewers                               |                                                                                                             |
| - removed = reviewers, author, reporter              |                                                                                                             |
| - dismissed = reviewers, reporter                    |                                                                                                             |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+

.. config:setting:: content-flagging-additional-settings
  :displayname: Additional settings (Content flagging)
  :systemconsole: Site Configuration > Content Flagging
  :configjson: .ContentFlaggingSettings.AdditionalSettings
  :environment: N/A
  :description: Configure reasons for flagging and related behavior. Defaults include a preset list of editable reasons.

Additional settings
~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Specify the reasons for flagging.                     | - System Config path: **Site Configuration > Content Flagging**                                    |
|                                                       | - ``config.json`` setting: ``ContentFlaggingSettings`` > ``AdditionalSettings`` > ``Reasons``      |
| Default reasons include:                              | - Environment variable: N/A                                                                        |
|                                                       |                                                                                                    |
| - Inappropriate content                               |                                                                                                    |
| - Sensitive data                                      |                                                                                                    |
| - Security concern                                    |                                                                                                    |
| - Harassment or abuse                                 |                                                                                                    |
| - Spam or phishing                                    |                                                                                                    |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------+

.. config:setting:: content-flagging-reporter-comment-required
  :displayname: Require reporters to add comment (Content flagging)
  :systemconsole: Site Configuration > Content Flagging
  :configjson: .ContentFlaggingSettings.AdditionalSettings.ReporterCommentRequired
  :environment: MM_CONTENTFLAGGINGSETTINGS_ADDITIONALSETTINGS_REPORTERCOMMENTREQUIRED
  :description: Require reporters to provide a comment when flagging content. Default is **true**.

  - **true**: **(Default)** Reporters must add a comment when flagging.
  - **false**: Reporters aren't required to add a comment when flagging.

Require reporters to add comment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| - **true**: **(Default)** Reporters must add a comment when flagging.| - System Config path: **Site Configuration > Content Flagging**                                                           |
| - **false**: Reporters aren't required to add a comment.             | - ``config.json`` setting: ``ContentFlaggingSettings`` > ``AdditionalSettings`` > ``ReporterCommentRequired`` > ``true``  |
|                                                                      | - Environment variable: ``MM_CONTENTFLAGGINGSETTINGS_ADDITIONALSETTINGS_REPORTERCOMMENTREQUIRED``                         |
+----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: content-flagging-reviewer-comment-required
  :displayname: Require reviewers to add comment (Content flagging)
  :systemconsole: Site Configuration > Content Flagging
  :configjson: .ContentFlaggingSettings.AdditionalSettings.ReviewerCommentRequired
  :environment: MM_CONTENTFLAGGINGSETTINGS_ADDITIONALSETTINGS_REVIEWERCOMMENTREQUIRED
  :description: Require reviewers to provide a comment when reviewing flagged content. Default is **true**.

  - **true**: **(Default)** Reviewers must add a comment when reviewing flagged content.
  - **false**: Reviewers aren't required to add a comment when reviewing flagged content.

Require reviewers to add comment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| - **true**: **(Default)** Reviewers must add a comment when         | - System Config path: **Site Configuration > Content Flagging**                                                          |
|   reviewing flagged content.                                        | - ``config.json`` setting: ``ContentFlaggingSettings`` > ``AdditionalSettings`` > ``ReviewerCommentRequired`` > ``true`` |
| - **false**: Reviewers aren't required to add a comment.            | - Environment variable: ``MM_CONTENTFLAGGINGSETTINGS_ADDITIONALSETTINGS_REVIEWERCOMMENTREQUIRED``                        |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: content-flagging-hide-flagged-content
  :displayname: Hide message while under review (Content flagging)
  :systemconsole: Site Configuration > Content Flagging
  :configjson: .ContentFlaggingSettings.AdditionalSettings.HideFlaggedContent
  :environment: MM_CONTENTFLAGGINGSETTINGS_ADDITIONALSETTINGS_HIDEFLAGGEDCONTENT
  :description: Show or hide flagged content from the channel while it is being reviewed. Default is **true**.

  - **true**: **(Default)** Hide flagged content from the channel while under review.
  - **false**: Keep flagged content visible while under review.

Hide message from channel while it is being reviewed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| - **true**: **(Default)** Hide flagged content from the channel     | - System Config path: **Site Configuration > Content Flagging**                                                      |
|   while under review.                                               | - ``config.json`` setting: ``ContentFlaggingSettings`` > ``AdditionalSettings`` > ``HideFlaggedContent`` > ``true``  |
| - **false**: Keep flagged content visible while under review.       | - Environment variable: ``MM_CONTENTFLAGGINGSETTINGS_ADDITIONALSETTINGS_HIDEFLAGGEDCONTENT``                         |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+

.. config:setting:: content-flagging-common-reviewers
  :displayname: Same reviewers for all teams (Content flagging)
  :systemconsole: Site Configuration > Content Flagging
  :configjson: .ContentFlaggingSettings.ReviewerSettings.CommonReviewers
  :environment: MM_CONTENTFLAGGINGSETTINGS_REVIEWERSETTINGS_COMMONREVIEWERS
  :description: Use the same set of reviewers across all teams. Default is **true**.

  - **true**: **(Default)** The same set of reviewers is used across all teams.
  - **false**: Reviewers can be managed per team.

Same reviewers for all teams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| - **true**: **(Default)** Use the same set of        | - System Config path: **Site Configuration > Content Flagging**                                                 |
|   reviewers across all teams.                        | - ``config.json`` setting: ``ContentFlaggingSettings`` > ``ReviewerSettings`` > ``CommonReviewers`` > ``true``  |
| - **false**: Reviewers can be managed per team.      | - Environment variable: ``MM_CONTENTFLAGGINGSETTINGS_REVIEWERSETTINGS_COMMONREVIEWERS``                         |
+------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+

.. config:setting:: content-flagging-system-admins-as-reviewers
  :displayname: System administrators as reviewers (Content flagging)
  :systemconsole: Site Configuration > Content Flagging
  :configjson: .ContentFlaggingSettings.ReviewerSettings.SystemAdminsAsReviewers
  :environment: MM_CONTENTFLAGGINGSETTINGS_REVIEWERSETTINGS_SYSTEMADMINSASREVIEWERS
  :description: Include system administrators as reviewers for flagged content. Default is **false**.

  - **true**: System administrators are included as reviewers for all teams they belong to.
  - **false**: **(Default)** System administrators are not included by default.

System administrators as reviewers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| - **true**: Include system administrators as         | - System Config path: **Site Configuration > Content Flagging**                                                         |
|   reviewers.                                         | - ``config.json`` setting: ``ContentFlaggingSettings`` > ``ReviewerSettings`` > ``SystemAdminsAsReviewers`` > ``false`` |
| - **false**: **(Default)** System administrators     | - Environment variable: ``MM_CONTENTFLAGGINGSETTINGS_REVIEWERSETTINGS_SYSTEMADMINSASREVIEWERS``                         |
|   are not included by default.                       |                                                                                                                         |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: content-flagging-team-admins-as-reviewers
  :displayname: Team administrators as reviewers (Content flagging)
  :systemconsole: Site Configuration > Content Flagging
  :configjson: .ContentFlaggingSettings.ReviewerSettings.TeamAdminsAsReviewers
  :environment: MM_CONTENTFLAGGINGSETTINGS_REVIEWERSETTINGS_TEAMADMINSASREVIEWERS
  :description: Include team administrators as reviewers for flagged content. Default is **true**.

  - **true**: **(Default)** Team administrators are included as reviewers for their respective teams.
  - **false**: Team administrators are not included as reviewers.

Team administrators as reviewers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| - **true**: **(Default)** Include team administrators | - System Config path: **Site Configuration > Content Flagging**                                                      |
|   as reviewers for their respective teams.            | - ``config.json`` setting: ``ContentFlaggingSettings`` > ``ReviewerSettings`` > ``TeamAdminsAsReviewers`` > ``true`` |
| - **false**: Team administrators aren't included      | - Environment variable: ``MM_CONTENTFLAGGINGSETTINGS_REVIEWERSETTINGS_TEAMADMINSASREVIEWERS``                        |
|   as reviewers.                                       |                                                                                                                      |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+

----

File sharing and downloads
--------------------------

Access the following configuration settings in the System Console by going to **Site Configuration > File Sharing and Downloads**.

.. config:setting:: allow-file-sharing
  :displayname: Allow file sharing (File sharing)
  :systemconsole: Site Configuration > File Sharing and Downloads
  :configjson: .FileSettings.EnableFileAttachments
  :environment: MM_FILESETTINGS_ENABLEFILEATTACHMENTS
  :description: This setting controls whether users can attach files to messages. Default is **true**.

  - **true**: **(Default)** Allows users to attach files to messages.
  - **false**: Prevents users from attaching files (including images) to a message.

Allow file sharing
~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| - **true**: **(Default)** Allows users to attach files to messages.                                                                                     | - System Config path: **Site Configuration > File Sharing and Downloads**           |
| - **false**: Prevents users from attaching files (including images) to a message. This affects users on all clients and devices, including mobile apps. | - ``config.json`` setting: ``FileSettings`` > ``EnableFileAttachments`` > ``true``  |
|                                                                                                                                                         | - Environment variable: ``MM_FILESETTINGS_ENABLEFILEATTACHMENTS``                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

.. config:setting:: allow-file-uploads-on-mobile
  :displayname: Allow file uploads on mobile (File sharing)
  :systemconsole: Site Configuration > File Sharing and Downloads
  :configjson: .FileSettings.EnableMobileUpload
  :environment: MM_FILESETTINGS_ENABLEMOBILEUPLOAD
  :description: This setting controls whether users can attach files to messages from mobile apps. Default is **true**.

  - **true**: **(Default)** Allows users to attach files to messages from mobile apps.
  - **false**: Prevents users from attaching files (including images) to messages from mobile apps.

Allow file uploads on mobile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| - **true**: **(Default)** Allows users to attach files to messages from mobile apps.              | - System Config path: **Site Configuration > File Sharing and Downloads**            |
| - **false**: Prevents users from attaching files (including images) to messages from mobile apps. | - ``config.json`` setting: ``FileSettings`` > ``EnableMobileUpload`` > ``true``      |
|                                                                                                   | - Environment variable: ``MM_FILESETTINGS_ENABLEMOBILEUPLOAD``                       |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. config:setting:: allow-file-downloads-on-mobile
  :displayname: Allow file downloads on mobile (File sharing)
  :systemconsole: Site Configuration > File sharing and downloads
  :configjson: .FileSettings.EnableMobileDownload
  :environment: MM_FILESETTINGS_ENABLEMOBILEDOWNLOAD
  :description: This setting controls whether users can download files from mobile apps. Default is **true**.

  - **true**: **(Default)** Enables file downloads on mobile apps.
  - **false**: Disables file downloads on mobile apps. Users can still download files from a mobile web browser.

Allow file downloads on mobile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| - **true**: **(Default)** Enables file downloads on mobile apps.                                               | - System Config path: **Site Configuration > File sharing and downloads**           |
| - **false**: Disables file downloads on mobile apps. Users can still download files from a mobile web browser. | - ``config.json`` setting: ``FileSettings`` > ``EnableMobileDownload`` > ``true``   |
|                                                                                                                | - Environment variable: ``MM_FILESETTINGS_ENABLEMOBILEDOWNLOAD``                    |
+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

.. config:setting:: mobile-enable-secure-file-preview
  :displayname: Enable secure file preview on mobile (File sharing)
  :systemconsole: Site Configuration > File sharing and downloads
  :configjson: .FileSettings.MobileEnableSecureFilePreview
  :environment: MM_FILESETTINGS_MOBILEENABLESECUREFILEPREVIEW
  :description: 

  - **true**: Prevents file downloads, previews, and sharing for most file types. Allows in-app previews for PDFs, videos, and images only. Files are stored temporarily in the app's cache and cannot be exported or shared.
  - **false**: **(Default)** Secure file preview mode is disabled.

Enable secure file preview on mobile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-adv.rst
  :start-after: :nosearch:

This setting improves an organization's mobile security posture by restricting file access while still allowing essential file viewing capabilities. 

+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| - **true**: Prevents file downloads, previews, and sharing for most file types,                                                       | - System Config path: **Site Configuration > File sharing and downloads**                         |
|   even when the                                                                                                                       | - ``config.json`` setting: ``FileSettings`` > ``MobileEnableSecureFilePreview`` > ``false``       |
|   :ref:`Allow file downloads on mobile <administration-guide/configure/site-configuration-settings:allow file downloads on mobile>`   | - Environment variable: ``MM_FILESETTINGS_MOBILEENABLESECUREFILEPREVIEW``                         |
|   configuration setting is enabled. Allows in-app previews for PDFs,                                                                  |                                                                                                   |
|   videos, and images only. Files are stored temporarily in the app's cache and cannot be exported or shared.                          |                                                                                                   |
| - **false**: **(Default)** Secure file preview mode is disabled.                                                                      |                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

.. config:setting:: mobile-allow-pdf-link-navigation
  :displayname: Allow PDF link navigation on mobile (File sharing)
  :systemconsole: Site Configuration > File sharing and downloads
  :configjson: .FileSettings.MobileAllowPdfLinkNavigation
  :environment: MM_FILESETTINGS_MOBILEALLOWPDFLINKNAVIGATION
  :description: This setting controls whether users can tap links inside PDFs when Secure File Preview Mode is active. Default is **true**.

  - **true**: **(Default)** Enables tapping links inside PDFs when Secure File Preview Mode is active. Links will open in the device browser or supported app.
  - **false**: Disables link navigation in PDFs when Secure File Preview Mode is active.

Allow PDF link navigation on mobile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-adv.rst
  :start-after: :nosearch:

+---------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| - **true**: **(Default)** Enables tapping links inside PDFs               | - System Config path: **Site Configuration > File sharing and downloads**                     |
|   when Secure File Preview Mode is active. Links will open                | - ``config.json`` setting: ``FileSettings`` > ``MobileAllowPdfLinkNavigation`` > ``true``     |
|   in the device browser or supported app.                                 | - Environment variable: ``MM_FILESETTINGS_MOBILEALLOWPDFLINKNAVIGATION``                      |
| - **false**: Disables link navigation in PDFs                             |                                                                                               |
|   when Secure File Preview Mode is active.                                |                                                                                               |
+---------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+

.. note::

  This setting has no effect when the :ref:`Secure file preview on mobile <administration-guide/configure/site-configuration-settings:enable secure file preview on mobile>` configuration setting is disabled.

----

Public Links
------------

With self-hosted deployments, you can access the following configuration settings in the System Console by going to **Site Configuration > Public Links**.

.. config:setting:: enable-public-file-links
  :displayname: Enable public file links (Public links)
  :systemconsole: Site Configuration > Public Links
  :configjson: .FileSettings.EnablePublicLink
  :environment: MM_FILESETTINGS_ENABLEPUBLICLINK
  :description: This setting controls whether users can create public links to files attached to Mattermost messages. Default is **false**.

  - **true**: Allows users to create `public links <https://docs.mattermost.com/end-user-guide/collaborate/share-files-in-messages.html#share-public-links>`__ to files attached to Mattermost messages.
  - **false**: **(Default)** Prevents users from creating public links to files and disables all previously created links.

Enable public file links
~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| - **true**: Allows users to create :doc:`public links </end-user-guide/collaborate/share-files-in-messages>` to files attached to Mattermost messages.                                        | - System Config path: **Site Configuration > Public Links**                     |
| - **false**: **(Default)** Prevents users from creating public links to files and disables all previously created links.                                                                      | - ``config.json`` setting: ``FileSettings`` > ``EnablePublicLink`` > ``false``  |
|                                                                                                                                                                                               | - Environment variable: ``MM_FILESETTINGS_ENABLEPUBLICLINK``                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------+

.. note::
  When set to **false**, anyone who tries to visit a previously created public link will receive an error message. If the setting is returned to **true**, previously created links will be accessible, unless the **Public link salt** has been regenerated.

.. config:setting:: public-link-salt
  :displayname: Public link salt (Public links)
  :systemconsole: Site Configuration > Public Links
  :configjson: .FileSettings.EnablePublicLink
  :environment: MM_FILESETTINGS_ENABLEPUBLICLINK
  :description: 32-character salt added to the URL of public file links. Changing this setting will **invalidate** all previously generated links.

Public link salt
~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+
| 32-character salt added to the URL of public file links. Changing this setting will **invalidate** all previously generated links. The salt is randomly generated when Mattermost is installed, and can be regenerated by selecting **Regenerate** in the System Console. | - System Config path: **Site Configuration > Public Links**     |
|                                                                                                                                                                                                                                                                           | - ``config.json`` setting: ``FileSettings`` > ``PublicLinkSalt``|
| String input.                                                                                                                                                                                                                                                             | - Environment variable: ``MM_FILESETTINGS_PUBLICLINKSALT``      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------+

----

Notices
-------

Access the following configuration settings in the System Console by going to **Site Configuration > Notices**.

.. config:setting:: enable-admin-notices
  :displayname: Enable admin notices (Notices)
  :systemconsole: Site Configuration > Notices
  :configjson: .AnnouncementSettings.AdminNoticesEnabled
  :environment: MM_ANNOUNCEMENTSETTINGS_ADMINNOTICESENABLED
  :description: This setting controls whether system admins receive in-product notices about server upgrades and administration features. Default is **true**.

  - **true**: **(Default)** System admins will receive `in-product notices <https://docs.mattermost.com/administration-guide/manage/in-product-notices.html>`__ about server upgrades and administration features.
  - **false**: System admins will not receive specific notices. Admins will still receive notices for all users (see **Enable end user notices**).

Enable admin notices
~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| - **true**: **(Default)** System admins will receive :doc:`in-product notices </administration-guide/manage/in-product-notices>` about server upgrades and administration features.         | - System Config path: **Site Configuration > Notices** -                                   |
|                                                                                                                                                                                             | - ``config.json`` setting: ``AnnouncementSettings`` > ``AdminNoticesEnabled`` > ``true``   |
| - **false**: System admins will not receive specific notices. Admins will still receive notices for all users (see **Enable end user notices**)                                             | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_ADMINNOTICESENABLED``                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+

.. config:setting:: enable-end-user-notices
  :displayname: Enable end user notices (Notices)
  :systemconsole: Site Configuration > Notices
  :configjson: .AnnouncementSettings.UserNoticesEnabled
  :environment: MM_ANNOUNCEMENTSETTINGS_USERNOTICESENABLED
  :description: This setting controls whether all users receive in-product notices about client upgrades and end user features. Default is **true**.

  - **true**: **(Default)** All users receive `in-product notices <https://docs.mattermost.com/administration-guide/manage/in-product-notices.html>`__ about client upgrades and end user features.
  - **false**: Users will not receive in-product notices.

Enable end user notices
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| - **true**: **(Default)** All users receive :doc:`in-product notices </administration-guide/manage/in-product-notices>` about client upgrades and end user features.           | - System Config path: **Site Configuration > Notices**                                  |
| - **false**: Users will not receive in-product notices.                                                                                                                        | - ``config.json`` setting: ``AnnouncementSettings`` > ``UserNoticesEnabled`` > ``true`` |
|                                                                                                                                                                                | - Environment variable: ``MM_ANNOUNCEMENTSETTINGS_USERNOTICESENABLED``                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+

Connected workspaces
----------------------

.. include:: ../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

The following settings aren't available in the System Console and can only be set in ``config.json``. 

When connected workspaces are enabled, system admins can :doc:`create and manage connected workspaces </administration-guide/onboard/connected-workspaces>` in the System Console by going to **Site Configuration > Connected Workspaces**.

.. config:setting:: enable-connected-workspaces
  :displayname: Enable connected workspaces
  :systemconsole: Site Configuration > Connected Workspaces
  :configjson: ConnectedWorkspacesSettings.EnableSharedChannels, ConnectedWorkspacesSettings.EnableRemoteClusterService 
  :environment: N/A
  :description: Establish secure connections between Mattermost instances, and invite secured connections to shared channels. 

Enable connected workspaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable the ability to establish secure connections between Mattermost instances, and invite secured connections to shared channels where users can participate as they would in any public and private channel.

Connected workspaces requires Mattermost Enterprise servers running v10.2 or later.

By default, both configuration settings are disabled and must be enabled in order to share channels with secure connections. Enabling connected workspace functionality requires a server restart.

This feature's two ``config.json`` settings include:

- ``ConnectedWorkspacesSettings.EnableRemoteClusterService: false`` with options ``true`` and ``false``.
- ``ConnectedWorkspacesSettings.EnableSharedChannels: false`` with options ``true`` and ``false``.

.. note::

  - Neither setting is available in the System Console and can only be set in ``config.json`` under ``ConnectedWorkspacesSettings``. 
  - System admins for Cloud deployments can submit a request to have these required configuration settings enabled for their Cloud deployment instance.
  - Following an upgrade to Mattermost v10.2 or later, existing configuration values for shared channels, including ``EnableSharedChannels`` and ``EnableRemoteClusterService`` are automatically converted to connected workspace configuration settings in the ``config.json`` file. The :ref:`deprecated shared channels experimental settings <administration-guide/configure/deprecated-configuration-settings:shared channels settings>` remain in the ``config.json`` file to support backwards compatibility.

.. config:setting:: disable-shared-channel-status-sync
  :displayname: Disable shared channel status sync (Connected Workspaces)
  :systemconsole: N/A
  :configjson: ConnectedWorkspacesSettings.DisableSharedChannelsStatusSync
  :environment: N/A
  :description: Disable member status and availability synchronization between connected workspaces. Default is false.

  - **true**: Channel as well as member status and availability isn't synchronized.
  - **false**: **(Default)** Channel as well as channel member status and availability is synchronized at regular intervals.

Disable shared channel status sync
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disable member status and availability synchronization between connected workspaces.

+----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| - **true**: Channel as well as member status and availability isn't synchronized.                                          | - System Config path: N/A                                                                                      |
| - **false**: **(Default)** Channel as well as channel member status and availability is synchronized at regular intervals. | - ``config.json`` setting: ``ConnectedWorkspacesSettings`` > ``DisableSharedChannelsStatusSync`` > ``false``   |
|                                                                                                                            | - Environment variable: N/A                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+

.. note::

  Enabling these features can increase the load on your Mattermost server’s CPU, memory, and database due to frequent updates, database queries, and API communication. Excessive sync frequency and retries can overwhelm system resources, potentially causing performance degradation or instability. Monitor your system carefully when enabling these features.

.. config:setting:: default-maximum-posts-per-sync
  :displayname: Default maximum posts per sync (Connected Workspaces)
  :systemconsole: N/A
  :configjson: ConnectedWorkspacesSettings.DefaultMaxPostsPerSync
  :environment: N/A
  :description: Define the default maximum number of mesages to synchronize at a time between connected workspaces. Default is 50.

Default maximum posts per sync
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| Define the default maximum number of mesages to synchronize at a time.    | - System Config path: N/A                                                                        |
|                                                                           | - ``config.json`` setting: ``ConnectedWorkspacesSettings`` > ``DefaultMaxPostsPerSync`` > ``50`` |
| Default is **50**.                                                        | - Environment variable: N/A                                                                      |
+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+

.. config:setting:: sync-users-on-connection-open
  :displayname: Sync users on connection open (Connected Workspaces)
  :systemconsole: N/A
  :configjson: ConnectedWorkspacesSettings.SyncUsersOnConnectionOpen
  :environment: N/A
  :description: Automatically synchronize users when a new connection between workspaces is established. Default is **true**.

  - **true**: **(Default)** Users are automatically synchronized when a new connection is established.
  - **false**: Users are not automatically synchronized when a new connection is established.

Sync users on connection open
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Automatically synchronize users when a new connection between workspaces is established. This ensures that remote users are immediately discoverable for direct and group messages without requiring them to post in a shared channel first.

+----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| - **true**: **(Default)** Users are automatically synchronized when a new connection is established.                       | - System Config path: N/A                                                                                |
| - **false**: Users are not automatically synchronized when a new connection is established.                                | - ``config.json`` setting: ``ConnectedWorkspacesSettings`` > ``SyncUsersOnConnectionOpen`` > ``true``    |
|                                                                                                                            | - Environment variable: N/A                                                                              |
+----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

.. note::

  Enabling these features can increase the load on your Mattermost server’s CPU, memory, and database due to frequent updates, database queries, and API communication. Excessive sync frequency and retries can overwhelm system resources, potentially causing performance degradation or instability. Monitor your system carefully when enabling these features.

.. config:setting:: global-user-sync-batch-size
  :displayname: Global user sync batch size (Connected Workspaces)
  :systemconsole: N/A
  :configjson: ConnectedWorkspacesSettings.GlobalUserSyncBatchSize
  :environment: N/A
  :description: The number of users to sync in each batch when performing global user synchronization. Default is 100.

Global user sync batch size
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| The number of users to sync in each batch when performing global user     | - System Config path: N/A                                                                                  |
| synchronization between connected workspaces.                             | - ``config.json`` setting: ``ConnectedWorkspacesSettings`` > ``GlobalUserSyncBatchSize`` > ``100``         |
|                                                                           | - Environment variable: N/A                                                                                |
| Default is **100**.                                                       |                                                                                                            |
+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

.. note::

  Enabling these features can increase the load on your Mattermost server’s CPU, memory, and database due to frequent updates, database queries, and API communication. Excessive sync frequency and retries can overwhelm system resources, potentially causing performance degradation or instability. Monitor your system carefully when enabling these features.

.. config:setting:: member-sync-batch-size
  :displayname: Member sync batch size (Connected Workspaces)
  :systemconsole: N/A
  :configjson: ConnectedWorkspacesSettings.MemberSyncBatchSize
  :environment: N/A
  :description: The number of channel members to sync in each batch when synchronizing channel membership. Default is 100.

Member sync batch size
~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| The number of channel members to sync in each batch when synchronizing    | - System Config path: N/A                                                                                  |
| channel membership between connected workspaces.                          | - ``config.json`` setting: ``ConnectedWorkspacesSettings`` > ``MemberSyncBatchSize`` > ``100``             |
|                                                                           | - Environment variable: N/A                                                                                |
| Default is **100**.                                                       |                                                                                                            |
+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

.. note::

  Enabling these features can increase the load on your Mattermost server’s CPU, memory, and database due to frequent updates, database queries, and API communication. Excessive sync frequency and retries can overwhelm system resources, potentially causing performance degradation or instability. Monitor your system carefully when enabling these features.

----

config.json-only settings
-------------------------

The following self-hosted deployment settings are only configurable in the ``config.json`` file and are not available in the System Console.

.. config:setting:: enable-cross-team-search
  :displayname: Enable cross-team search
  :systemconsole: N/A
  :configjson: ServiceSettings.EnableCrossTeamSearch
  :environment: SERVICESETTINGS_ENABLECROSSTEAMSEARCH
  :description: Disable the ability to search all channels the user is a member of across all teams or a specific team, and search all channels the user is a member of within the current team only. Enabled by default.

Cross-team search
~~~~~~~~~~~~~~~~~

+---------------------------------------------------+-----------------------------------------------------------------------------------+
| Disable the ability to search across all teams    | - System Config path: N/A                                                         |
| or a specific team.                               | - ``config.json`` setting: ``ServiceSettings.EnableCrossTeamSearch`` > ``true``   |
|                                                   | - Environment variable: ``MM_SERVICESETTINGS_ENABLECROSSTEAMSEARCH``              |
| - **true**: **(Default)** Cross-team search is    |                                                                                   |
|   enabled. Searches can be performed against all  |                                                                                   |
|   channels the user is a member of across all     |                                                                                   |
|   teams, a specific team, or the current team.    |                                                                                   |
| - **false**: Cross-team search is disabled.       |                                                                                   |
|   Searches are performed on all channels the user |                                                                                   |
|   is member of within the current team only.      |                                                                                   |
+---------------------------------------------------+-----------------------------------------------------------------------------------+
