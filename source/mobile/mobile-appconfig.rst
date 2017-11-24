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

3. Select the already published Mattermost app, or choose to add a new one.  When adding a new app, select **App Store** or **Google Play** to use the published apps by Mattermost. If you are building the apps yourself, use the option for **Internal apps** and then browse to select the .apk or .ipa file.

.. image:: browse_apps.png

4. Next fill in the app name, description, and any other information needed for deployment in the screen below. See Blackberry documentation for more details on the settings for internal apps, public iOS apps, and Android for Work apps.

.. image:: fill_in_information_apps.png

5. In the same screen look for **App configuration**. You can either upload this xml file as the template, or add the configuration manually with the keys and values described in the AppConfig table (see above).
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

.. image:: select_apps.png

3. Click the “Add” button

4. Select **App Store** or **Google Play** to use the published apps by Mattermost. If you are building the apps yourself, use the option for **In-House** and then browse to select the .apk or .ipa file.

.. image:: select_2_apps.png

5. After uploading the .ipa or .apk file or selecting **Mattermost** from the published app search results, click “Next”. In our example will be using the app in the Apple App Store.

6. Review or fill in the information for the app, and click “Next”

7. Choose an option for distributing the Mattermost app to users and click “Next”

8. Here you'll be presented different options to configure the app. Fill in the ones you need, and then go to **iOS Managed App Configuration** and click on the "+" sign

9. Fill in a name for the configuration an optional description. Then fill the **AppConnect Custom Configuration** using the values from the AppConfig table above

10. Select a distribution option for this configuration and click “Next”

11. Review all you config settings one more time and click “Done”

Mattermost WebRTC Guide
----------------------------------------------

This guide is aimed to set up Mattermost WebRTC with a docker container if you need support for a full `Janus Gateway <https://janus.conf.meetecho.com/>`_ please visit their `Github repo <https://github.com/meetecho/janus-gateway>`_ for detail instructions.

Assertions about using the Mattermost `WebRTC docker image <https://hub.docker.com/r/mattermost/webrtc/>`_
 - You need docker to install this image (docker installation, configuration and management is out of the scope of this guide)
 - You need a working Mattermost server (installation, configuration and management of the Mattermost server is out of the scope of this guide)
 - Janus version is 0.2.2
 - No TURN or STUN service included
 - SSL Certificate valid for host **dockerhost** and until 2 January 2018
 - Ability to connect using SSL or plain WebSocket and HTTP

Deploying Mattermost WebRTC Docker Container
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assuming you have docker installed and running you'll need to execute in a terminal the following command to install the Mattermost WebRTC docker image

`docker run --name mattermost-webrtc -p 7088:7088 -p 7089:7089 -p 8188:8188 -p 8189:8189 -d mattermost/webrtc:latest`

This will download, install and run your mattermost-webrtc container with the Janus Gateway pre-configured to use WebRTC within the Mattermost WebApp and Desktop Apps.

Note: Make sure your Mattermost server can reach the running docker Mattermost WebRTC container.

Configuring Mattermost to Enable WebRTC
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first thing you need to decide is whether your are going to establish the connections to the Mattermost WebRTC container running the Janus Gateway with or without SSL, this is particularly important in this case because the SSL certificate used to run the Janus Gateway is not being signed by a trusted CA, that means that you will need to make some additional configuration changes in your Mattermost Server.

In case you decide to go ahead with SSL then you need to go to **System Console** -> **Security** -> **Connections and Enable Insecure Outgoing Connections**

The reason for this is that Mattermost will make a http request to the Janus Gateway service to get a Token that is used to identify the user and so on and if you configure Mattermost to make requests to that service with SSL then the certificate won't be valid thus returns a status code of 500.

Next we need to configure the WebRTC service on our Mattermost Server for that go to **System Console** -> **Integrations** -> **WebRTC (Beta)**

Once you enable WebRTC you'll need to input a few values
 - **Gateway WebSocket URL**: This is the WebSocket route for the Janus Gateway service inside the Mattermost WebRTC container used to connect the peers on a Video Call. If you want to establish the connection using SSL then you need to set the protocol to **wss://**  and the port to **8189**, for non-SSL use protocol **ws://** and port **8188**.
 - **Gateway Admin URL**: This is the admin route for the Janus Gateway service inside the Mattermost WebRTC container use to fetch a valid Token. If you want to establish the connection using SSL then you need to set the protocol to **https://**  and the port to **7089**, for non-SSL use protocol **http://** and port **7088**.
 - **Gateway Admin Secret**: This is the admin's secret to validate the request being made to fetch the token, for any Janus  Gateway installation the default is **janusoverlord**, you can change it by editing the janus.cfg under /opt/janus/etc/janus and modify the value for admin_secret
 - **STUN URI**: This is the Stun server to use, you need to have one so either deploy one or use the public google one. The google public stun server is **stun:stun.l.google.com:19302**
 - **TURN URI**: In case you need NAT Traversal you'll need to configure a TURN server, you can use Coturn to accomplish that but is out of the scope of this guide
 - **TURN Username**: The username of your TURN server if you have one.
 - **TURN Shared Key**: The password of your TURN server if you have one.

Don't forget to Save your configuration Changes

Finally, because this feature is in Beta every user has to enable WebRTC in order to establish a video call with other users on the server. Go to  Main Menu -> Account Settings -> Advanced -> Preview pre-release features and select Enable the ability to make and receive one-on-one WebRTC calls.

.. image:: enable_webb_rtc_calls_apps.png
