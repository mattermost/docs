Mobile Apps FAQ
===============

Can I connect to multiple Mattermost servers using the mobile apps?
-------------------------------------------------------------------

At the moment, we only support connecting to one server at a time; however, we are aware that this is one of the `top feature requests <https://mattermost.uservoice.com/forums/306457-general/suggestions/10975938-ios-and-android-apps-should-allow-multiple-server>`_ for the mobile app. We are currently investigating some technical challenges, such as how to handle push notifications coming from multiple servers. We expect to add multiserver support by end of 2018.

As a workaround, you can install both the released "Mattermost" app and sign up to be a `tester <https://github.com/mattermost/mattermost-mobile/blob/master/README.md#testing>`_ for the "Mattermost Beta" app. This allows you to connect and log in to a different server from each app.

Is there a tablet version of the mobile apps?
---------------------------------------------

“Mattermost Classic” mobile apps support tablets.

Our second generation mobile apps (“Mattermost”) have beta support for tablets.

How is data handled on mobile devices after a user account is deactivated?
--------------------------------------------------------------------------

App data is wiped from the device when a user logs out of the app. If the user is logged in when the account is deactivated, then within one minute the system logs the user out, and as a result all app data is wiped from the device.

Do I need to compile the mobile apps to host my own push notification server?
------------------------------------------------------------------------------

Yes. To host your own push notification server, you'll need to compile the mobile apps. See `documentation <https://docs.mattermost.com/mobile/mobile-compile-yourself.html>`_ to learn how to compile your own mobile apps.

.. _push-faq:
How do push notifications work?
-------------------------------

Your Mattermost server sends push notifications to a hosted push proxy server, which relays them via mobile push notification services provided by Apple and Google.

To ensure push notifications are coming from a trusted source, Apple and Google only allow push notifications sent from a service using a key or signature corresponding to a secret compiled into the mobile application itself.

The full process is outlined below:

1. An action triggering a push notification is detected in the Mattermost server running in your private network.

2. Your Mattermost server sends a push notification message to a Mattermost Push Notification Service (MPNS), either self-hosted in your private network, or publicly hosted by Mattermost, Inc.

3. MPNS sends a push notification message to either Apple Push Notification Service (APNS) or to Google’s Firebase Cloud Messaging (FCM) service over a TLS connection.

  - If sent to Apple, the message has a signature corresponding to a secret compiled in the iOS app.
  - If sent to Google, the message uses a key corresponding to a secret compiled in the Android app.

  Regardless of whether you're using iOS or Android, the Mattermost Push Notification Service needs to have access to the appropriate secret compiled into the mobile app.

  This means if you use the Mattermost apps from the Apple App Store or Google Play, you need to use the hosted push notification service from Mattermost, Inc. If you compile the apps yourself, you must also compile and use your own MPNS with the corresponding secret.

4. Either APNS or FCM receives the push notification message from MPNS over TLS, and then relays the message to the user's iOS or Android device to be displayed.

.. Note:: The use of push notifications with iOS and Android applications will require a moment where the contents of push notifications are visible unencrypted by a server controlled by either Apple or Google. This is standard for any iOS or Android app. For this reasons, there is an option to omit the contents of Mattermost messages from push notifications in order to meet certain compliance requirements.

What are my options for securing the mobile apps?
-------------------------------------------------

The following options for security mobile application deployments are available:

1. Securing network connection to mobile apps
  - Use HTTPS and WSS network connections to encrypt transport.
  - Use of a mobile VPN client on mobile devices to establish secure connection to Mattermost server within private network.

2. Use multifactor authentication options
  - If a VPN client with multifactor authentication is not used, it's highly recommended that MFA is required on authenticating into Mattermost, either within Mattermost itself or via your SSO provider

What are my options for securing push notifications?
----------------------------------------------------

The following options are available for securing your push notification service:

1.  Protecting notification contents
  - You can `choose what type of information to include in push notifications <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`_, like excluding the message contents if your compliance policies require it. Default server settings have message contents turned off.

2. Disabling push notifications
  - Push notifications can also be disabled entirely depending on security requirements. Default server settings have push notifications disabled.

3. Encrypting connections for apps you compile yourself:
  - When using a privately-hosted Mattermost Push Notification Service (MPNS), use encrypted TLS connections between:

    - MNPS and Apple Push Notification Service
    - MPNS and Google’s Firebase Cloud Messaging
    - MPNS and your Mattermost server

4. Securing the Mattermost Apple App Store and Google Play apps:
  - When using Mattermost mobile apps from the App Store and Google Play, purchase an annual subscription to Mattermost Enterprise Edition E10 or higher, which offers a :doc:`Hosted Push Notification Service (HPNS) <mobile-hpns>`.

.. Note:: For configuration details, see guides for :doc:`deploying the Mattermost App Store and Google Play apps <mobile-appstore-install>` and :doc:`deploying your own version of the apps <mobile-compile-yourself>`.

How do I white label the app and customize build settings?
----------------------------------------------------------

All files in the ``/assets/base`` folder can be overriden as needed without conflicting with changes made to the upstream version of the app. To do this:

1. Create the folder ``/assets/override``.
2. Copy any files or folders that you wish to replace from ``/assets/base`` into ``/assets/override``.
3. Make your changes to the files in ``/assets/override``.

When you compile the app or run ``make dist/assets``, the contents of those two folders will be merged with files in ``/assets/override``, taking precedence in the case of any conflicts. For binary files such as images, an overridden file will completely replace the base version, while json files will be merged so that fields not set in the overridden copy use the base version.

For a more specific example of how to use this feature, see the following section.

How do I pre-configure the server URL for my users?
----------------------------------------------------

You can pre-configure the server URL and other settings by overriding default config.json settings and building the mobile apps yourself.

1. Fork the `mattermost-mobile repository <https://github.com/mattermost/mattermost-mobile>`_. 
2. Create the file ``/assets/override/config.json`` in your forked mattermost-mobile repository.
3. Copy and paste all the settings from ``assets/base/config.json`` to the newly created ``/assets/override/config.json`` file that you want to override.
4. To override the server URL, set ``DefaultServerURL`` to server URL of your Mattermost server in ``/assets/override/config.json``.
5. (Optional) If you want to prevent users from changing the server URL, set ``AutoSelectServerUrl`` to ``true``.
6. (Optional) Override any other settings you like.

After the above, your ``/assets/override/config.json`` file would look something like this:

  .. code-block:: json
  
    {
        "DefaultServerURL": "my-mattermost-instance.example.com",
        "AutoSelectServerUrl": true,
        "ExperimentalUsernamePressIsMention": true
    }

7. Finally, `compile your own version <https://docs.mattermost.com/mobile/mobile-compile-yourself.html>`_ of the Mattermost mobile applications and Mattermost push proxy server.

How can I get Google SSO to work with the Mattermost Mobile Apps?
-----------------------------------------------------------------

The apps on the Apple App Store and Google Play Store cannot support Google SSO out of the box. This is because Google requires a unique Google API key that's specific to each organization.

If you need Google SSO support, you can create a custom version of the app for your own organization. Fork the `mattermost-mobile <https://github.com/mattermost/mattermost-mobile>`_  repository and add support for Google SSO before compiling the app yourself. If this is something you’re interested in, please `file an issue in GitHub <https://github.com/mattermost/mattermost-mobile/issues>`_ to start the discussion.

How do I configure Deep Linking?
--------------------------------------

The app checks for platform specific configuration on app install. If no configuration is found, then the deep linking code sits silently and permalinks act as regular links.

**Setup for iOS:**

1. Create an ``apple-app-site-association`` file in the ``.well-known`` directory at the root of your server. It should be accessible by navigating to ``https://<your-site-name>/.well-known/apple-app-site-association``. There should NOT be a file extension.
2. In order to handle deep links, paste the following JSON into the ``apple-app-site-association`` file. Make sure to place your app ID in the ``appID`` property:

    {
        "applinks": {
            "apps": [],
            "details": [
                {
                    "appID": "<your-app-id-here>",
                    "paths": ["**/pl/*"]
                }
            ]
        }
    }

3. Add the associated domains entitlement to your app via the Apple developer portal.
4. Add an entitlement that specifies the domains your app supports via the Xcode entitlements manager.
5. Before installing the app with the new entitlement, make sure that you can view the contents of the ``apple-app-site-association`` file via a browser by navigating to ``https://<your-site-name>/.well-known/apple-app-site-association``. The app will check for this file on install and if found, will allow outside permalinks to open the app.

Official documentation for configuring deep linking on iOS can be found `here <https://developer.apple.com/library/archive/documentation/General/Conceptual/AppSearch/UniversalLinks.html>`_.

**Setup for Android:**

Please refer to the the App Links Assistant in Android Studio for configuring `deep linking on Android <https://developer.android.com/studio/write/app-link-indexing>`_.

How do I connect users across internal and external networks?
-----------------------------------------------------------------

By setting up global network traffic management, you can send a user to an internal or external network when connecting with a mobile app. Moreover, you can have two separate layers of restrictions on internal and external traffic, such as:

 - In the internal network, deploy on a private network via per device VPN
 - In the external network, deploy with `TLS mutual auth <https://docs.mattermost.com/deployment/ssl-client-certificate.html>`_ with an NGINX proxy, and `client-side certificates <https://docs.mattermost.com/deployment/certificate-based-authentication.html>`_ for desktop and iOS.
 
Many services such as Microsoft Azure provide options for `managing network traffic <https://docs.microsoft.com/en-us/azure/traffic-manager/traffic-manager-overview>`_, or you can engage a services partner to assist.
