Mobile Apps FAQ
===============

Can I connect to multiple Mattermost servers using the mobile apps?
-------------------------------------------------------------------

At the moment, we only support connecting to one server at a time. If you need to connect to multiple servers, please `upvote the feature request <https://mattermost.uservoice.com/forums/306457/suggestions/1097593>`_ so we can track demand for it.

As a workaround, you can install both the released "Mattermost" app and sign up to be a `tester <https://github.com/mattermost/mattermost-mobile/blob/master/README.md#testing>`_ for the "Mattermost Beta" app so you can connect to two servers at once.

Is there a tablet version of the mobile apps?
---------------------------------------------

“Mattermost Classic” mobile apps support tablets.

Our second generation mobile apps (“Mattermost”), do not yet support tablets but we plan to add support in future. The timeline depends on how many people have a need for it, so if you're looking for a tablet version please help us out by `upvoting the feature request <https://mattermost.uservoice.com/forums/306457/suggestions/20082079>`_!

How is data handled on mobile devices after a user account is deactivated?
--------------------------------------------------------------------------

App data is wiped from the device when a user logs out of the app. If the user is logged in when the account is deactivated, then within one minute the system logs the user out, and as a result all app data is wiped from the device.

How can I get Google SSO to work with the Mattermost Mobile Apps?
-----------------------------------------------------------------

Google SSO is not supported by the apps on the Apple App Store and Google Play Store.

This is because the Google Login libraries require your own Google API key when the app is compiled, so there’s no way for us to include that in our apps.

If you would like Google SSO, you will need to fork our `mattermost-mobile <https://github.com/mattermost/mattermost-mobile>`_  repository and add support for Google SSO before compiling the app yourself. If this is something you’re interested in, please `file an issue in GitHub <https://github.com/mattermost/mattermost-mobile/issues>`_ to start the discussion.

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
