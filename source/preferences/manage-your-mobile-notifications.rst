Manage your mobile notifications
=================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Enable notifications
--------------------

From Mattermost v9.9, Mattermost prompts you to enable notifications via web/desktop. Is there a mobile equivalent? Or must the user enable via desktop or web first to enable them via mobile?

When notifications are enabled, you're notified of all Mattermost activity by default with `badges <#badge-based-notifications>`__ and `push notifications <#push-notifications>`. You can `customize your mobile notifications <#customize-your-notifications>`__ for Mattermost activity.

When using Mattermost on a mobile device, you're notified of all new messages, @mentions, or keywords all of the time.

Badge-based notifications
-------------------------

Mattermost mobile app icons display number badges for new messages, @mentions, or keywords.

.. note ::

  The Mattermost mobile app doesn't display dot badges indicating new unread activity. This can result in the Android users seeing Mattermost notifications in the Android Notification Shade while the Mattermost icon shows no badge.

Push notifications
------------------

Mobile push notifications popup notifications that display on iOS and Android mobile devices as follows:

- iOS: On the Lock Screen, Notification Center, and as Banners/Alerts based on your iOS settings.
- Android: On the Lock Screen, Notification Shade, and as Banners/Heads-Up Notifications based on your Android settings.

Customize your notifications
----------------------------

To reduce the number of notifications you receive, tap your profile picture, then tap **Settings**, and **Notifications**.

- Tap **Mentions** to disable notifications based on keywords that trigger mentions, including first name, username, channel-wide @mentions, and keywords you've specified.
- Tap **Push Notifications** to get notified about **mentions, direct messages, and group messages** only, and only when you're **away or offline**, or only when you're **offline**.

Want to hear a sound on your mobile device when a Mattermost call starts? If your Mattermost admin :ref:`enables this Beta feature <configure/plugins-configuration-settings:enable call ringing>`, select **Call Notifications** to choose the sound that plays when a call is started within a direct or group message you're participating in.

.. tip::

  - From Mattermost mobile app v2.19, incoming call sounds also include vibration, and vibration only when your device is in silent mode
  - When you set a separate call sound on mobile, your mobile change applies only to mobile.
  - Are you a desktop app user who also used mobile? You can customize your mobile notifications in the Mattermost desktop app by going to **Settings > Desktop and mobile notifications**, enabling notifications for **all new messages**, or **mentions, direct messages and group messages**, and then selecting **Use different settings for my mobile devices**.

Disable all desktop notifications
-----------------------------------

Tap **Push Notifications** to get notified about **Nothing**.