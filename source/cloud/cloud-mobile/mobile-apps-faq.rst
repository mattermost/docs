
Mobile Apps FAQ
===============

Can I connect to multiple Mattermost workspaces using the mobile apps?
----------------------------------------------------------------------

At the moment, we only support connecting to one workspace at a time; however, we are aware that this is one of the `top feature requests <https://mattermost.uservoice.com/forums/306457-general/suggestions/10975938-ios-and-android-apps-should-allow-multiple-server>`__ for the mobile app. We are currently investigating some technical challenges, such as how to handle push notifications coming from multiple workspaces. To follow our progress on this feature, you can join the `RN: Multi-Server <https://community.mattermost.com/core/channels/rn-multi-server-suppot>`_ channel on our community server.

As a workaround, you can install the released Mattermost mobile app and sign up to be a `tester <https://github.com/mattermost/mattermost-mobile/blob/master/README.md#testing>`__ for the Mattermost Beta mobile app. This allows you to connect and log in to a different workspace from each app.

Is there a tablet version of the mobile apps?
---------------------------------------------

Mattermost Classic mobile apps support tablets.

Our second generation mobile apps (Mattermost) have beta support for tablets.

Can the permanent sidebar on tablet devices be disabled?
--------------------------------------------------------

The permanent sidebar is on by default for tablet-sized devices, but can be disabled from **Settings > Display > Sidebar > Permanent Sidebar**. When disabled, the sidebar behaves similarly to mobile devices where the user must open it using the button in the top-left corner of the screen.

How is data handled on mobile devices after a user account is deactivated?
--------------------------------------------------------------------------

App data is wiped from the device when a user logs out of the app. If the user is logged in when the account is deactivated, then within one minute of deactivation the system logs the user out. Thereafter all app data is wiped from the device.

What post metadata is sent in mobile push notifications?
--------------------------------------------------------

The following post metadata is sent in all push notifications:

- ``Team ID``
- ``Channel ID``
- ``Post ID``
- ``User ID`` (post author)
- ``Username`` (post author or webhook override username)
- ``Root ID`` (only if the post is in a thread)
- ``Type`` (create or clear push notification)
- ``Category`` (iOS only, determines if the notifications can be replied to)
- ``Badge number`` (what the notification badge on the app icon should be set to when the notification is received)

Additional metadata may be sent depending on the System Console setting for `Push Notification Contents <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`__:

- **Generic description with sender and channel names:** ``Channel name`` metadata will be included.
- **Full message content sent in the notification payload:** ``Post content`` and ``Channel name`` metadata will be included.
- **Full message content fetched from the server on receipt:** ``Post content`` and ``Channel name`` are not included in the notification payload. Instead the ``Post ID`` is used to fetch ``Post content`` and ``Channel name`` from the workspace after the push notification is received on the device.

How can I use ID-Only push notifications to protect notification content from being exposed to third-party services?
--------------------------------------------------------------------------------------------------------------------

When it comes to mobile data privacy, many organizations prioritize secure handling of messaging data, particularly when it may contain mission-critical or proprietary information. These organizations may have concerns about using mobile notifications because data must pass through third-party entities like Apple Push Notification Service (APNS) or Google Firebase Cloud Messaging (FCM) before it reaches a device. This poses a potential risk for organizations that operate under strict compliance requirements and cannot expose message data to external entities.

To solve this, we offer an option for greater protection for Mattermost push notification message data by only sending a unique message ID in the notification payload rather than the full message data. Once the device receives the ID, it then fetches the message content directly from Mattermost and displays the notification per usual. External entities, such as APNS and FCM, handle only the ID and are unable to read any part of the message itself.

If your organization has strict privacy or compliance needs, the `ID-Only Push Notification <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`_ setting offers a high level of privacy while still allowing your team members to benefit from mobile push notifications.

What are my options for securing the mobile apps?
-------------------------------------------------

The following options for secure mobile app deployments are available:

1. Securing network connection to mobile apps
  - Use HTTPS and WSS network connections to encrypt transport.
  - Use of a mobile VPN client on mobile devices to establish a secure connection to Mattermost within a private network.

2. Use multifactor authentication options
  - If a VPN client with multifactor authentication is not in use, it's highly recommended that MFA is required on authenticating into Mattermost, either within Mattermost itself or via your SSO provider.

Why do I sometimes see a delay in receiving a push notification?
----------------------------------------------------------------

`Apple Push Notification Service (APNS) <https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1>`_ and `Google Fire Cloud Messaging (FCM) <https://firebase.google.com/docs/cloud-messaging>`_ determine when your device receives a push notification from Mattermost. Thus, a delay is usually as a result of those services.

The technical flow for the device to receive a push notification is as follows:

1. User posts a message in Mattermost.
2. Mattermost identifies whether a notification needs to be sent.
3. If yes, Mattermost sends a payload containing the push notification to the push proxy.
4. The push proxy parses the notification and relays it to APNS and FCM.
5. APNS and FCM informs the relevant devices that there is a push notification for Mattermost. This usually happens almost immediately, but may be delayed by a couple of minutes.
6. Mattermost processes the notification and displays it on the user's device.

How do I deploy Mattermost with Enterprise Mobility Management (EMM) providers?
-------------------------------------------------------------------------------

Mattermost enables customers with high privacy and custom security requirements to deploy mobile app and push notification services using keys that they alone control.

`Learn more about using AppConfig for EMM providers <https://docs.mattermost.com/cloud/cloud-mobile/cloud-app-config.html>`__.

How can I get Google SSO to work with the Mattermost mobile app?
----------------------------------------------------------------

The apps on the Apple App Store and Google Play Store cannot support Google SSO out of the box. This is because Google requires a unique Google API key that's specific to each organization.

If you need Google SSO support, you can create a custom version of the app for your own organization. Fork the `mattermost-mobile <https://github.com/mattermost/mattermost-mobile>`__  repository and add support for Google SSO before compiling the app yourself. If this is something you’re interested in, please `file an issue in GitHub <https://github.com/mattermost/mattermost-mobile/issues>`__ to start the discussion.
