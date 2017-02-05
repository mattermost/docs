..  _push_test:

==============================================
Mobile Applications and Push Notifications
==============================================

This guide summarizes the deployment options and considerations for using Mattermost mobile apps with push notifications. 

OVERVIEW:

.. contents::
  :backlinks: top
  :local:

Quick setup via iTunes and Google Play 
--------------------------------------------------

For a quick evaluation of mobile applications after the Mattermost server is deployed in a test environment: 

1. Set up an external proxy with encrypted transport, and optionally a mobile VPN client, to securely connect the mobile apps to your internal Mattermost instance.
2. Enable mobile push notifications by going to **System Console > Notifications > Mobile Push > Send Push Notifications** and select **Use iOS and Android apps on iTunes and Google Play with TPNS**. 
3. *Optional:* To show full messages snippets in mobile push notifications, set **System Console > Notifications > Mobile Push > Push Notification Contents** to **Send full message snippet**. Most deployments enable this unless they're under specific policies to not allow confidential information in push notifications (contents of push notifications may appear briefly on phones even when they're not locked by passcode). 
4. Download the mobile applications to your mobile device: - `Mattermost iOS App on iTunes <https://itunes.apple.com/us/app/mattermost/id984966508?mt=8>`_ or `Mattermost Android App on Google Play <https://play.google.com/store/apps/details?id=com.mattermost.mattermost&hl=en>`_.
5. Open the mobile application and enter the address of your proxy and connect.

After mobile apps are tested they can be further secured according to your internal compliance and security policies. 

Production deployment options  
--------------------------------------------------

There are two options for deploying Mattermost mobile applications with push notifications to work with the Mattermost server you deploy in your private cloud: 

- **Deploying mobile apps from iTunes or Google Play** - For quick and easy deployment, end users download the Mattermost mobile applications from iTunes and Google Play and connect to an appropriate proxy to reach your internal Mattermost deployment, and your Mattermost server sends push notifications to a hosted proxy server, which relays them via mobile push notification services provided by Apple and Google. 
 
  Enterprise customers may choose to secure these apps with a mobile VPN clients, single-sign-on, multi-factor authentication, proxy connection restrictions and encrypted transport.

- **Compiling mobile apps from source code** - To customize the capabilities or appearance of mobile apps, or to secure their availability to a within a private network or to meet other security and compliance policies, an organization may choose to compile their own Mattermost mobile applications and push notification service from their open source repositories. 

The following sections detail setup of these two options: 

Deploying with publicly-hosted mobile apps by Mattermost, Inc. 
`````````````````````````````````````````````````````````````````

TBD

Deploying with privately-hosted mobile apps within your private network
`````````````````````````````````````````````````````````````````````````

TBD

Options for setting up push notifications
`````````````````````````````````````````````

For Mattermost iOS apps and Android mobile apps to receive puch notifications the service sending notifications needs to be verified as an authorized sender. There are 3 options to provide this verification: 

1. Use the **Hosted Push Notification Service (HPNS)** from Mattermost.com that is trusted by Mattermost iOS and Android applications on iTunes and Google Play.

    - Pros: 
        - Push notifications are encrypted.
        - Saves time over deploying to an Enterprise App Store. 
        - Production quality uptime offered via commercial subscription. 		  
        - Commercial support from Mattermost.com included with subscription.
    - Cons: 
        - Some IT policies only allow mobile apps via Enteprise App Store.

2. Use an **Enterprise App Store (EAS)** by compiling your own push notification service and mobile applications from source code to manually establish verification.

    - Pros: 
        - Push notifications are encrypted.
        - Enterprise App Store provides the highest level of mobile apps security. 
        
    - Cons: 
        - Requires developer time to compile, secure, deploy and maintain components.

    EAS is most convenient when an organization has access to developers experienced in iOS mobile development, Android mobile development, Golang programming, Enterprise App Store administration and system security. 

3. Use the **Test Push Notification Service (TPNS)** and pre-compiled applications with unencrypted push notifications prior to selecting one of the above options.

    - Pros:
        - Easy and free solution to setting up and evaluating mobile apps.
    - Cons: 
        - Does not offer encrypted push notifications.
        - Not intended as a production quality service.
        - No commercial support from Mattermost.com

The below explains each option in detail. 

.. note::  By default, push notifications do not contain specific message contents. They use generic messages like "@frank was mentioned in Town Square" but DO NOT display the contents of messages until System Admins configure the option to include them. 


Hosted Push Notifications Service (HPNS)
----------------------------------------

Mattermost.com offers a Hosted Push Notification Service (HPNS) via commercial subscription for organizations who want encrypted push notifications sent from behind their firewall, with production-quality uptime and commercial support, as an alternative to compiling, deploying and securing their own service from source code provided (see "Enterprise App Store" in next section). 

With HPNS, end users can use publicly available iOS and Android mobile applications on iTunes and Google Play over encrypted connections: 

- `Mattermost iOS App on iTunes with encrypted push notifications <https://itunes.apple.com/us/app/mattermost/id984966508?mt=8>`_
- `Mattermost Android App on Google Play with encrypted push notifications <https://play.google.com/store/apps/details?id=com.mattermost.mattermost&hl=en>`_

A license key to activate HPNS is available with a `subscription to Mattermost Enterprise Edition <https://about.mattermost.com/pricing/>`_. 

After purchasing and installing a license key, you can turn on HPNS using **System Console** > **Notifications** > **Mobile Push** > **Send Push Notifications** > **Use encrypted, production-quality HPNS connection to iOS and Android apps**.

Enterprise App Store (EAS)
--------------------------

To set up an Enterprise App Store, teams can set up verified relationships by compiling, deploying, securing and maintaining the following open source repositories: 

- `Open source repository for the Mattermost Push Notification Service <https://github.com/mattermost/push-proxy>`_
- `Open source repository for the Mattermost iOS application <https://github.com/mattermost/ios>`_
- `Open source repository for the Mattermost Android application <https://github.com/mattermost/android>`_

After deploying the mobile applications and push notification service, go to **System Console** > **Notifications** > **Mobile Push** > **Send Push Notifications** > **Manually enter Push Notification Service location** and enter the location of your Push Notification Service in the **Push Notification Server** field. 

Test Push Notifications Service (TPNS) 
--------------------------------------

Mattermost.com also offers a free, unencrypted push notification service for trying out the Mattermost mobile applications prior to deciding whether to use the EAS or HPNS option. 

End users of TPNS can use the publicly available iOS and Android mobile applications on iTunes and Google Play, with unencrypted push notifications: 

- `Mattermost iOS App on iTunes <https://itunes.apple.com/us/app/mattermost/id984966508?mt=8>`_
- `Mattermost Android App on Google Play <https://play.google.com/store/apps/details?id=com.mattermost.mattermost&hl=en>`_

You can connect to the TPNS by going to **System Console** > **Notifications** > **Mobile Push** > **Send Push Notifications** > **Use iOS and Android apps on iTunes and Google Play with TPNS.**

Note: TPNS is a test service that does not encrypt push notifications and does not offer production-quality uptime. 

What happens when a Mattermost push notification is sent? 
`````````````````````````````````````````````````````````

To ensure only push notifications from authorized senders are processed by iOS and Android mobile application, each push notifications need to come from a trusted source.  

Here is the full process: 

1. When triggered, a push notification is sent from the Mattermost server to the Mattermost Push Notification Service over TLS

2. The Mattermost Push Notification Service forwards the message to either Apple Push Notification Service (APNS) or to the Google Cloud Messaging (GCM) service depending on whether you're sending to an iOS or Android device. The message from the Mattermost Push Notification Service is signed with a key that's registered with the recieving service, corresponding to the target mobile app, so its authenticity is verified. 
 
3. The APNS or GCM service confirms that the message from the Mattermost Push Notification Service is authorized for the target mobile application and forwards the message to the app to be displayed. 

Confirming HPNS push notifications are properly configured
``````````````````````````````````````````````````````````

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

Confirming TPNS push notifications are properly configured
``````````````````````````````````````````````````````````

To setup TPNS please `follow the instructions to confirm HPNS is correctly configured <http://docs.mattermost.com/deployment/push.html#confirming-hpns-push-notifications-are-properly-configured>`_ with the following changes: 

1. Omit step 1.1, as there is no need to install Enterprise Edition.
2. In step 1.2, select "User iOS and Android apps on iTunes and Google Play with TPNS"

The same instructions should then verify the functionality of TPNS.


Confirming Performance of Mobile Applications 
`````````````````````````````````````````````

The response times of Mattermost mobile apps should perform to standard benchmarks, provided device model, connection speed and server configuration are comparable to benchmark setups.

Mobile Performance Benchmarks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
```````````````````````````````````

Here are solutions to common troubleshooting requests: 

Internal proxy configuration needed for outbound requests to HPNS 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Make sure your proxy server is properly configured to support SSL. Confirm it works by checking the URL at `https://www.digicert.com/help/`. 

2. Setup a proxy to forward requests to `https://push.mattermost.com`. 

3. In Mattermost set **System Console** > **Notification Settings** > **Mobile Push** > **Enable Push Notifications** to "Manually enter Push Notification Service location" and enter the URL of your proxy in the **Push Notification Server** field.

Depending on how your proxy is configured you may need to add a port number and create a URL like `https://push.internalproxy.com:8000` mapped to `https://push.mattermost.com`

Error message: “We would not connect to the Mattermost server or the server is running an incompatible version”
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
