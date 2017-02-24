..  _push_test:

==============================================
Mobile Applications Guide
==============================================

This guide summarizes the deployment and security options for Mattermost mobile apps with push notifications. 

OVERVIEW:

.. contents::
  :backlinks: top
  :local:

Quick install for mobile apps via iTunes and Google Play 
-----------------------------------------------------------

For a quick evaluation of mobile applications after the Mattermost server is deployed in a test environment: 

1. Set up an external proxy with encrypted transport, and optionally a mobile VPN client, to securely connect the mobile apps to your internal Mattermost instance.

2. Enable mobile push notifications:

  - Go to **System Console > Notifications > Mobile Push > Send Push Notifications** and select **Use iOS and Android apps on iTunes and Google Play with TPNS**. 

  - *Optional:* To show full messages snippets in mobile push notifications, set **System Console > Notifications > Mobile Push > Push Notification Contents** to **Send full message snippet**. Most deployments enable this unless they're under specific policies to not allow confidential information in push notifications. 

3. Download the mobile applications to your mobile device: 

  - `Mattermost iOS App on iTunes <https://itunes.apple.com/us/app/mattermost/id984966508?mt=8>`_ or
  - `Mattermost Android App on Google Play <https://play.google.com/store/apps/details?id=com.mattermost.mattermost&hl=en>`_.

4. Open the mobile application and enter the address of your proxy and connect.

After mobile apps are tested they can be further secured according to your internal compliance and security policies. 

Production deployment options  
--------------------------------------------------

There are two options for deploying Mattermost mobile applications with push notifications to work with the Mattermost server you deploy in your private cloud: 

- **Deploying with publicly-hosted mobile apps by Mattermost, Inc.** - For quick and easy deployment, end users download the Mattermost mobile applications from iTunes and Google Play and connect to an appropriate proxy to reach your internal Mattermost deployment, and your Mattermost server sends push notifications to a hosted proxy server, which relays them via mobile push notification services provided by Apple and Google. 
 
  Enterprise customers may choose to secure these apps with a mobile VPN clients, single-sign-on, multi-factor authentication, proxy connection restrictions and encrypted transport.

- **Deploying with privately-hosted mobile apps within your private network** - To customize the capabilities or appearance of mobile apps, to secure them within a private network or to meet other security and compliance policies, an organization may choose to compile their own Mattermost mobile applications and push notification service from their open source repositories. 

The following sections detail setup of these two options: 

Deploying with publicly-hosted mobile apps by Mattermost, Inc. 
`````````````````````````````````````````````````````````````````

To deploy in production with publicly-hosted mobile apps compiled by Mattermost, Inc. and hosted in iTunes and Google Play: 

1. Complete the `Quick install for mobile apps via iTunes and Google Play `_ in a test environment. 

2. Review the `Securing mobile deployments`_ documentation and apply the options appropriate to meet the security and compliance requirements of your organization in your production environment. 

Deploying with privately-hosted mobile apps within your private network
`````````````````````````````````````````````````````````````````````````

To deploy in production with privately-hosted mobile apps compiled by your organization in an Enterprise App Store: 

1. Compile your own iOS, Android mobile applications and Mattermost Push Notification Service (MPNS) via their open source repositories:

  - `Open source repository for the Mattermost Push Notification Service <https://github.com/mattermost/push-proxy>`_
  - `Open source repository for the Mattermost iOS application <https://github.com/mattermost/ios>`_
  - `Open source repository for the Mattermost Android application <https://github.com/mattermost/android>`_

2. Connect your Mattermost server with your privately hosted MPNS service

  - Go to **System Console** > **Notifications** > **Mobile Push** > **Send Push Notifications** > **Manually enter Push Notification Service location** and enter the location of your Mattermost Push Notification Service in the **Push Notification Server** field.  

3. Review the `Securing mobile deployments`_ documentation and apply the options appropriate to meet the security and compliance requirements of your organization. 

Securing mobile deployments
---------------------------------

The following options for security mobile application deployments are available: 

Securing network connection to mobile apps 
``````````````````````````````````````````````````

- Use HTTPS and WSS network connections to encrypt transport.
- Use of a mobile VPN client on mobile devices to establish secure connection to Mattermost server within private network. 

Configuring authentication options in mobile apps 
``````````````````````````````````````````````````

- If VPN client with multi-factor authentication is not used, it's highly recommended that MFA is required on authenticating into Mattermost, either within Mattermost itself or via single-sign-on options requiring MFA.

Securing availability of mobile applications 
``````````````````````````````````````````````````

- To limit access to mobile applications to a privately hosted Enterprise App Store, you can compile your own mobile applications and push notificiation service from their open source repositories.

Securing push notifications 
``````````````````````````````````````````````````

To describe options for securing mobile push notifications we begin with an overview of how push notifications are delivered, then the security options in the context of that process. 

How push notifications are delivered
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To ensure push notifications are coming from a trusted source, mobile applications hosted in iTunes and Google Play can only receive push notifications sent from a service using a key or signature corresponding to a secret compiled into the mobile application itself. 

Therefore, the following process is used: 

1. An action triggering a push notification is detected in the Mattermost server running in your private network. 

2. Your Mattermost server sends a push notification message to a Mattermost Push Notification Service (MPNS), either self-hosted in your private network, or publicly hosted by Mattermost, Inc. 

3. MPNS sends a push notification message to either Apple Push Notification Service (APNS) or to the Google Cloud Messaging (GCM) service over a TLS connection depending on whether you're sending to an iOS or Android device. 

  - If sent to Apple, the message has a signature corresponding to a secret compiled in the iOS app.
  - If sent to Google, the message uses a key corresponding to a secret compiled in the Android app. 
  
  Regardless of whether you're using iOS or Android, the MPNS used needs to have access to the appropriate secret compiled into the mobile app. 
  
  - If you use the publicly hosted mobile apps in iTunes or Google Play, you need to use the publicly hosted MPNS from Mattermost, Inc., which uses the corresponding secret. 
  - If you use a privately-hosted mobile app in an Enterprise App Store by compiling your own app, you need to also compile and use your own MPNS with the corresponding secret.  

4. Either APNS or GCM receives the push notification message from MPNS over TLS, and then relays the message to the user's iOS or Android mobile app to be displayed.  

.. Note: 

   The use of push notifications with either iOS or Android mobile applications will require a moment where the contents of push notifications are visible unencrypted by a server controlled by either Apple or Google. This is standard for any iOS or Android app. For this reasons, there is an option to omit the contents of Mattermost messages from push notifications in order to meet certain compliance requrements. 
 
Securing your Mattermost Push Notification Service 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following options are available for securing your push notification service: 

- The system can be `configured to prevent the inclusion of message contents in push notifications <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`_ and send only generic messages that a notification event took place. Default server settings have message contents turned off. 
- Push notifications can also be disabled entirely depending on security requirements. Default server settings have push notifications disabled. 
- When using a privately-hosted MPNS, use encrypted TLS connections between MNPS and APNS, MPNS and GCM, MPNS and your Mattermost server.
- When using Mattermost mobile apps in iTunes and Google Play, purchase an annual subcription to Mattermost Enterprise Edition E10 or higher, which offers a Hosted Push Notification Service (HPNS), offering: 

  - Access to a publicly-hosted MPNS service offering an explicit privacy policy where the contents of unencrypted messages are not examined or stored. 
  - Encrypted TLS connections between the hosted HPNS and APNS, HPNS and GCM, HPNS and your Mattermost server. 
  - Production-level uptime expectations.
  
  After purchasing a subscription to Mattermost E10 or higher from Mattermost, Inc. follow the `Setting up HPNS push notifications in Enterprise Edition`_ instructions to set up and test your system.

  Note: Mattermost, Inc. also offers a free basic hosted service for testing setups, Test Push Notification Service (TPNS), which is referenced in the `Quick install for mobile apps via iTunes and Google Play`_ instructions. It does not offer a production-level uptime expectation, nor does it offer encrypted transport. 

Setting up HPNS push notifications in Enterprise Edition 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To setup HPNS please follow the following steps: 

1. Install HPNS

     1. Follow the `instructions you received with your Mattermost Enterprise Edition purchase to install or upgrade to Enterprise Edition <http://docs.mattermost.com/install/ee-install.html>`_
     2. Under **System Console** > **Notifications** > **Mobile Push** > **Send Push Notifications**  select **Use encrypted, production-quality HPNS connection to iOS and Android apps** (this option appears only in Enterprise Edition, not Team Edition)
     3. Check the box "I understand and accept the Mattermost Hosted Push Notification Service Terms of Service and Privacy Policy." after reading the documents referenced, then click **Save**. 
     4. Download either the Mattermost iOS app from iTunes or the Mattermost Android app from Google Play and sign into the app using an account on your Mattermost server, which we'll refer to as "Account A". 
     5. When asked whether you wish to receive notifications, **confirm you want to receive notifications**
     
2. Trigger a push notification

     1. From the mobile application used by "Account A", click the three dot menu on the top right and go to **Account Settings** > **Notifications** > **Mobile push notifications**. Click **Edit** and select **For mentions and direct messages**, then **Save** the setting. 
     2. Have "Account A" close the mobile application, but do not log out. The mobile app needs to be in the background for the test to work. 
     3. Using "Account B", on the same Mattermost team as "Account A", Click the **More** menu under the Direct Messages section in the left hand side of the team site to add "Account A" to the Direct Message list. 
     4. Have "Account B" send a direct message "Hello" to "Account A". 
     5. This should trigger a push notification to the mobile device of "Account A".  
     
3. If you did not receive a push notification, use the following procedure to troubleshoot: 

     1. Under **System Console** > **General** > **Logging** > **File Log Level** select **DEBUG** in order to watch for push notifications in the server log. IMPORTANT: Make sure to switch this back to ERROR level logging after setting up push notifications to conserve disk space. 
     
     2. Delete your mobile application, install it again and sign-in with "Account A" and **confirm you want to receive push notifications** when prompted by the mobile app. 
     
     3. Repeat the "Trigger a push notification" procedure above and if you still don't receive a push notification, go to **System Console** > **Logs** click **Reload** and scroll to the bottom and look for a message similar to: ```[2016/04/21 03:16:44 UTC] [DEBG] Sending push notification to 63c06ca8e3949ca7e5996c31fcf07ecb36c658a3e7c2c227a4af949cc4777a87 wi msg of '@accountb: Hello'```
     
         - If the log message appears, it means a message was sent to the HPNS server and was not received by your mobile application. Please contact support@mattermost.com with the subject "HPNS issue on Step 8" for help from the commercial support team. 
           
         - If the log message does not appear, it means no mobile push notification was sent to "Account A". Please repeat step 2 and double check each step. 
         
4. After your issue is resolved, go to **System Console** > **General** > **Logging** > **File Log Level** and select **ERROR** to switch your logging detail level to Errors Only, instead of DEBUG, in order to conserve disk space. 

Confirming performance of mobile applications 
----------------------------------------------------

The response times of Mattermost mobile apps should perform to standard benchmarks, provided device model, connection speed and server configuration are comparable to benchmark setups.

.. Note: 

   A 2nd generation of open source iOS and Android apps are under development with a beta release planned at the end of March 2017. They are developed using "React Native", a high performance mobile application framework created by Facebook and used in Facebook mobile applications. 

   The current 1st generation Mattermost mobile apps in iTunes and Android are in "maintenance mode", meaning serious bugs found will be fixed, but no new improvements are being added, since the apps will be replaced by the 2nd generation apps. 

   Performance benchmarks below are for 1st generation apps.

Mobile performance benchmarks
`````````````````````````````````````````````````````````

Properly configured mobile applications on 4G/LTE or wifi should perform as follows: 

iPhone 6s Plus on 4G/LTE connection (50 ms ping time, 50 Mb/s download, 8 Mb/s upload): 

- **Loading a new channel:** less than 4 seconds
- **Returning to a channel previously viewed:** less than 1 second
- **Switching to app when it is running in the background:** less than 1 second
- **Switching to the app and loading a channel after the phone has been asleep:** less than 5 seconds
- **Fresh start of the app until first page load:** less than 10 seconds

iPhone 5s on 5G connection (20 ms ping time, 77 Mb/s download, 12 Mb/s upload):

- **Loading a new channel:** less than 3 seconds
- **Returning to a channel previously viewed:** less than 1 second
- **Switching to app when it is running in the background:** less than 1 second
- **Switching to the app and loading a channel after the phone has been asleep:** less than 3 seconds
- **Fresh start of the app until first page load:** less than 5 seconds

Samsung Galaxy S6 on 4G/LTE connection (23 ms ping time, 36 Mb/s download, 17 Mb/s upload):

- **Loading a new channel:** less than 4 seconds
- **Returning to a channel previously viewed:** less than 1 second
- **Switching to app when it is running in the background:** less than 1 second
- **Switching to the app and loading a channel after the phone has been asleep:** less than 5 seconds
- **Fresh start of the app until first page load:** less than 5 seconds

Samsung Galaxy S6 on wifi connection (23 ms ping time, 138 Mb/s download, 12 Mb/s upload):

- **Loading a new channel:** less than 3 seconds
- **Returning to a channel previously viewed:** less than 1 second
- **Switching to app when it is running in the background:** less than 1 second
- **Switching to the app and loading a channel after the phone has been asleep:** less than 5 seconds
- **Fresh start of the app until first page load:** less than 4 seconds

Note: While Mattermost mobile applications may be used on 3G (and lower) connections, this configuration is not recommended.

Removing bottlenecks to mobile app performance 
`````````````````````````````````````````````````````````

If your mobile app is not performing to these sample benchmarks, you can identify bottlenecks using the following process: 

1. Confirm your mobile device meets minimum hardware and operating system requirements 

   - Please confirm the device you're testing `meets the minimum operating system and hardware requirements of Mattermost Mobile Apps. <http://docs.mattermost.com/install/requirements.html#mobile-app-experience>`_

2. Confirm your mobile device connection is on 4G/LTE or Wifi and meets ping time requirements

   - From your mobile browser go to https://speedtest.net/mobile, download the SpeedTest app and begin a test
   - Check if your **ping time** (a measure of signal latency) to see if it's similar to the benchmarks in the above section. If they are significantly higher, move to an area with better reception or contact your wireless provider to correct any technical issues. 

3. Confirm your mobile app is performing properly 

   - Test the response of your iOS or Android app as compared to the above benchmarks
   - Test the response of opening your Mattermost team site on your phone's mobile browser
   - If using your team site in your iOS or Android app is noticebly slower than using it in the browser, delete your mobile app and reinstall it to clear the issue. 
   
4. Check your server performance 

     - If 1) and 2) are working properly and you are still encountering performance issues, please ensure that your server is properly sized.
     
         - Please review the `recommended minimum hardware guidelines <http://docs.mattermost.com/install/requirements.html#hardware-sizing-for-team-deployments>`_ and confirm that you're using properly sized hardware. If you're having performance issues, please do not scale down hardware below the minimum level suggested. 
          
         - If you're using a shared server, you may experience latency with a shared proxy server if it's under load from other applications. You can either switch to a dedicated proxy, or set up your own proxy server using NGINX by following one of the `standard install guides. <http://docs.mattermost.com/#install-guides>`_ 

These procedures summarize all potential bottlenecks in a system for mobile app performance: Connection speed, mobile app performance, and server performance. 

- If you're an Enterprise Edition subscriber and continue to have issues please email support@mattermost.com with a measure of the benchmarks you're experiencing. 

- If you're not a subscriber, please `open a thread in the Mattermost Troubleshooting forum <http://www.mattermost.org/troubleshoot/>`_ with a summary of the performance you're seeing, details on the model of your mobile device, connection speed and server sizing. 

Troubleshooting mobile applications 
--------------------------------------------

Here are solutions to common troubleshooting requests: 

Internal proxy configuration needed for outbound requests to HPNS 
``````````````````````````````````````````````````````````````````````

1. Make sure your proxy server is properly configured to support SSL. Confirm it works by checking the URL at `https://www.digicert.com/help/`. 

2. Setup a proxy to forward requests to `https://push.mattermost.com`. 

3. In Mattermost set **System Console** > **Notification Settings** > **Mobile Push** > **Enable Push Notifications** to "Manually enter Push Notification Service location" and enter the URL of your proxy in the **Push Notification Server** field.

Depending on how your proxy is configured you may need to add a port number and create a URL like `https://push.internalproxy.com:8000` mapped to `https://push.mattermost.com`

Error message: “We would not connect to the Mattermost server or the server is running an incompatible version”
``````````````````````````````````````````````````````````````````````

This error message, whether on iOS or Android, typically results from a typo in the server URL or an SSL configuration issue. To troubleshoot: 

Check that your mobile application works properly with HTTPS by connecting to a test server: 

1. Create an account at https://demo.mattermost.com 
2. Erase your mobile application and reinstall it
3. In your mobile app, enter the server URL https://demo.mattermost.com and confirm the connection is working by entering your credentials to login 

If the login doesn't work, please report an issue to https://github.com/mattermost/platform/issues

If the login does work: 

1. Check that the SSL URL is properly installed by entering it in a certificate checker, such as: https://cryptoreport.websecurity.symantec.com/checker/
2. Correct any issues with your certificate 
3. Try connecting to the HTTPS URL of your server using the mobile app
4. If you're still having issues please `open a new topic in the troubleshooting forum <https://forum.mattermost.org/c/general/trouble-shoot>`_ with steps to reproduce your issue. If you're an Enterprise Edition subscriber, you can also email subscribers@mattermost.com for support. 

Note: Mobile apps do not currenly support self-signed certificates, nor client-side certificates. To use free certificates signed by a Certificate Authority, visit https://letsencrypt.org/
