AppConfig for EMM Solutions with Mattermost Mobile Apps
=======================================================

What is AppConfig?
------------------

AppConfig is a standard approach for app configuration and management introduced by the AppConfig Community, a group of leading EMM providers and app developers. 

It provides an easy way to configure enterprise mobile applications with any of the EMM providers listed on the `AppConfig website <https://www.appconfig.org/members/>`_.

Mattermost mobile apps can be configured in your EMM solution using AppConfig with the apps on the public app stores (Google Play and Apple App Store), or as an "in-house app" you compile yourself.

For example set up instructions, see our documentation on :doc:`MobileIron <mobile-mobileiron>` and :doc:`Blackberry UEM <mobile-blackberry>`.

.. _appconfig-table:

Mattermost AppConfig Values
---------------------------

The following table shows all the configuration options that can be sent from the EMM provider of your choice to the Mattermost mobile apps. You can also :download:`download an XML template <mattermost-specfile.xml>` of the configuration file for use with your EMM provider. 

+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| Key                    | Description                                                                                                                                                                                                     | Type   | Default Value | Valid Values     | iOS Support | Android for Work Support |
+========================+=================================================================================================================================================================================================================+========+===============+==================+=============+==========================+
| inAppPinCode           | Require users to authenticate as the owner of the phone before using the app. Prompts for fingerprint or passcode when the app first opens and when the app has been in the background for more than 5 minutes. | String | ``false``     | ``true | false`` | Yes         | Yes                      |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| blurApplicationScreen  | Blur the app when it’s set to background to protect any confidential on-screen information. On Android, it also prevents taking screenshots of the app.                                                         | String | ``false``     | ``true | false`` | Yes         | Yes                      |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| jailbreakDetection     | Disable app launch on jailbroken or rooted devices.                                                                                                                                                             | String | ``false``     | ``true | false`` | Yes         | Yes                      |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| copyAndPasteProtection | Disable the ability to copy from or paste into any text inputs in the app.                                                                                                                                      | String | ``false``     | ``true | false`` | Yes         | No                       |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| serverUrl              | Set a default Mattermost server URL.                                                                                                                                                                            | String |               | URL              | Yes         | Yes                      |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| allowOtherServers      | Allow the user to change the above server URL.                                                                                                                                                                  | String | ``true``      | ``true | false`` | Yes         | Yes                      |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| username               | Set the username or email address to use to authenticate against the Mattermost Server.                                                                                                                         | String |               |                  | Yes         | Yes                      |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| vendor                 | Name of the EMM vendor or company deploying the app. Used in help text when prompting for passcodes so users are aware why the app is being protected.                                                          | String | Mattermost    |                  | Yes         | Yes                      |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+

Other AppConfig Settings
------------------------

As part of AppConfig, EMM administrators can set the following additional configuration options for the Mattermost mobile apps:

1. **App Tunnel:** Leverage the "Per-app VPN" capabilities in most commercial VPN solutions.
2. **Prevent App Backup:** Prevent users from backing up app data.
3. **Enforce App Encryption:** Set security policies such as requiring encryption.
4. **Remotely Wipe App:** Use the EMM tool to distribute the app to devices as a managed application so it can be remotely wiped. If the app was previously installed, mark it so the EMM converts the app to a managed app.

Other configurations may be available depending on your EMM provider.

Adding Mattermost mobile apps to your EMM provider
------------------------------------------------------------------------

Because the Mattermost mobile apps have support for AppConfig you can deploy the apps found in Google Play and the Apple App Store, or you can choose to deploy it as an in-house app.

AppConfig EMM Members
------------------------

Mattermost mobile apps can be deployed with any of the EMM providers listed in the AppConfig Website 

Mattermost Support for AppConfig in Native Mobile apps
---------------------------------------------------------------------

What is the AppConfig Community?

The AppConfig Community is a collection of industry leading EMM solution providers and app developers that have come together to make it easier for developers and customers to drive mobility in business. The community’s mission is to streamline the adoption and deployment of mobile enterprise applications by providing a standard approach to app configuration and management, building upon the extensive app security and configuration frameworks available in the OS.

Historically, developers used proprietary software development kits (SDKs) to enable configuration and management features of their apps through EMM. This required app developers to build different versions of their apps for each EMM vendor. Now, with AppConfig Community tools and best practices, developers do not require EMM-specific integrations for many enterprise use cases. End users also benefit from automated features such as an out-of-the-box experience to give the users instant app access without requiring cumbersome setup flows or user credentials.

Setup Mattermost with BlackBerry EMM
----------------------------------------------

1. Login to your BlackBerry UEM environment. 
2. Click on Apps

.. image:: clicks_on_apps.png

3. Select the already published Mattermost app, or choose to add a new one.  When adding a new app, select App Store or Google Play to use the published apps by Mattermost. If you are building the apps yourself, use the option for Internal apps and then browse to select the .apk or .ipa file.

.. image:: browse_apps.png

4. Next fill in the app name, description, and any other information needed for deployment in the screen below. See Blackberry documentation for more details on the settings for internal apps, public iOS apps, and Android for Work apps.

.. image:: fill_in_information_apps.png

5. In the same screen look for App configuration. You can either upload this xml file as the template, or add the configuration manually with the keys and values described in the AppConfig table (see above).
 - Using the template
  - Browse for the xml template file (Note: If you build the app yourself, make sure to edit the template to use your bundle or package ID)

.. image:: app_configuration_apps.png

  - Set the name of the app configuration and edit the settings that appear on screen, then click “Save”
  
.. image:: save_apps.png

 - Manual configuration
  - Click on the "+" at the far right of the App configuration table and select "Configure Manually"

  - Enter a name for the app configuration, and then add the key value pairs found in the App configuration table (see above)
  
.. image:: name_key_values_apps.png

 - Save your configuration
 
Setup Mattermost with MobileIron Cloud EMM
----------------------------------------------

1. Log in to your MobileIron Cloud tenant

2. Click on “Apps” and then “App Catalog” 
