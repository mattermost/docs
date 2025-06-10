Deploy using an EMM provider
=============================

You can enhance mobile security by deploying the Mattermost mobile app with `Enterprise Mobility Management (EMM) <https://en.wikipedia.org/wiki/Enterprise_mobility_management>`__ and :doc:`Mattermost AppConfig </deploy/mobile/deploy-mobile-apps-using-emm-provider>` compatibility to secure mobile endpoints with management application configuration.

You can use an EMM to:

- Enforce users to download the Mattermost pre-built or custom apps managed by your organization.
- Set default server url address.
- Restrict users from changing servers.
- Enforce security policies.

An EMM provider pushes Mattermost Mobile apps to EMM-enrolled devices. This approach is recommended for organizations that typically use EMM solutions to deploy Mobile apps to meet security and compliance policies.

Manage app configuration using AppConfig
----------------------------------------

AppConfig is our recommended approach for app configuration and management. It was introduced by the `AppConfig Community <https://www.appconfig.org/>`__, a group of leading EMM providers and app developers who have come together to make it easier for developers and customers to drive mobility in business.

AppConfig provides an easy way to configure enterprise mobile apps with any EMM providers listed on the `AppConfig website <https://www.appconfig.org/>`__. Using AppConfig, you can manage default settings and security controls on public app stores and custom-built mobile clients. For example, you can pre-configure your Mattermost server URL and username.

Mattermost AppConfig values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following table shows all the configuration options that can be sent from the EMM provider of your choice to the Mattermost mobile apps. You can also :download:`download an XML template </samples/mattermost-specfile.xml>` of the configuration file for use with your EMM provider. 

+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| Key                    | Description                                                                                                                                                                                                     | Type   | Default Value | Valid Values     | iOS Support | Android for Work Support |
+========================+=================================================================================================================================================================================================================+========+===============+==================+=============+==========================+
| inAppPinCode           | Require users to authenticate as the device owner before using the app. Prompts for fingerprint or passcode when the app first opens and when the app has been in the background for more than five minutes.    | String | ``false``     | ``true | false`` | Yes         | Yes                      |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| blurApplicationScreen  | Blur the app when it's set to background to protect any confidential on-screen information. On Android, it also prevents taking screenshots of the app.                                                         | String | ``false``     | ``true | false`` | Yes         | Yes                      |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| jailbreakDetection     | Disable app launch on jailbroken or rooted devices.                                                                                                                                                             | String | ``false``     | ``true | false`` | Yes         | Yes                      |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| copyAndPasteProtection | Disable the ability to copy from or paste into any text inputs in the app.                                                                                                                                      | String | ``false``     | ``true | false`` | Yes         | Yes (since v1.24.0)      |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| serverUrl              | Set a default Mattermost server URL. Supports a single server only while v2.0 of the mobile app supports multiple server connections.                                                                           | String |               | URL              | Yes         | Yes                      |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| serverName             | Automatically populates the server display name for the URL specified in serverURL.                                                                                                                             | String |               | alphanumeric or  | Yes         | Yes                      |
|                        |                                                                                                                                                                                                                 |        |               | empty            |             |                          |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| allowOtherServers      | Allow the user to change the above server URL. If set to ``true``, users can connect to multiple servers that aren't specified in the server URL setting.                                                       | String | ``true``      | ``true | false`` | Yes         | Yes                      |
|                        | If set to ``false``, users can only connect to a single defined server.                                                                                                                                         |        |               |                  |             |                          |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| username               | Set the username or email address to use to authenticate against the Mattermost Server.                                                                                                                         | String |               |                  | Yes         | Yes                      |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| useVPN                 | Enable connection to the Mattermost Server to use a per-app VPN or VPN on-demand.                                                                                                                               | String | ``false``     | ``true | false`` | Yes         | No                       |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| timeoutVPN             | Set how long the request waits (in milliseconds) for an initial VPN connection to establish before timeout.                                                                                                     | String | 30000         |                  | Yes         | No                       |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| vendor                 | Name of the EMM vendor or company deploying the app. Used in help text when prompting for passcodes so users are aware why the app is being protected.                                                          | String | Mattermost    |                  | Yes         | Yes                      |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+
| inAppSessionAuth       | Use the app's internal browser for SSO instead of an external browser. From Mattermost v10.2 and mobile v2.2.1, deprecated in favor of the                                                                      | String | ``false``     | ``true | false`` | Yes         | Yes                      |
|                        | :ref:`mobile external browser <configure/site-configuration-settings:mobile external browser>` server configuration setting.                                                                                    |        |               |                  |             |                          |
+------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+---------------+------------------+-------------+--------------------------+

Other AppConfig settings
~~~~~~~~~~~~~~~~~~~~~~~~~

As part of AppConfig, EMM administrators can set the following additional configuration options for the Mattermost mobile apps:

1. **App Tunnel:** Leverage the "Per-app VPN" capabilities in most commercial VPN solutions.
2. **Prevent App Backup:** Prevent users from backing up app data.
3. **Enforce App Encryption:** Set security policies such as requiring encryption.
4. **Remotely Wipe App:** Use the EMM tool to distribute the app to devices as a managed application so it can be remotely wiped. If the app was previously installed, mark it so the EMM converts the app to a managed app.

Other configurations may be available depending on your EMM provider.

.. important::
    - Mattermost only supports the AppConfig standard for securing Mattermost mobile apps via an EMM provider due to incompatibilities with app wrapping and React Native applications. Different EMM vendors refer to “wrapping” in different ways, but it ultimately comes down to unpacking the mobile client bundle, injecting additional SDKs, and re-packaging/re-signing. React Native is the technology used to develop the Mattermost mobile apps.
    - Mattermost doesn’t support app wrapping, and Mattermost mobile apps won't function properly when using app wrapping (e.g., Websockets for real-time messaging will break). Use app wrapping/containerization technology at your own risk.
    - A Mattermost Enterprise subscription plan (or a legacy Enterprise Edition license) is required to request assistance or troubleshooting help from `Mattermost Customer Support <https://mattermost.com/support/>`__ when building and deploying custom mobile apps. Customers on other Mattermost subscription plans can develop and deploy custom mobile apps, but can't request technical support assistance through Mattermost Customer Support.
    - With the release of Mattermost mobile app v2.0, mobile app v1.55 becomes the official :doc:`extended support mobile release </about/mattermost-mobile-releases>`, and will be supported for an extended timeframe.

Enroll devices
--------------

When building your own custom versions or deploying the pre-built Mattermost Mobile apps, consider your organization’s mobile policy:

- Can users bring their own device (BYOD) If so, what devices will be used?
- Are devices company-owned and company-issued?
- Are both options supported?
- What operating systems do you want to start testing?

Once you know what possible device configurations you’ll be supporting, consider creating a sample configuration, then running validation tests against each configuration item.

Generate and assign device profiles
-----------------------------------

Generate and assign a device profile for device-wide configurations through the EMM provider.