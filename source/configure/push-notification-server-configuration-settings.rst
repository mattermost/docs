:orphan:
:nosearch:

Configure Mattermost to enable push notifications to Mattermost clients by going to **System Console > Environment > Push Notification Server**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: push-enablenotifications
  :displayname: Enable push notifications (Push Notifications)
  :systemconsole: Environment > Push Notification Server
  :configjson: .EmailSettings.SendPushNotifications
  :environment: MM_EMAILSETTINGS_SENDPUSHNOTIFICATIONS

  - **true**: **(Default)** Your Mattermost server sends mobile push notifications to the server specified.
  - **false**: Mobile push notifications are disabled.

Enable push notifications
~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+--------------------------------------------------------------------------------+
| Enable or disable Mattermost push notifications.                | - System Config path: **Environment > Push Notification Server**               |
|                                                                 | - ``config.json setting``: ``".EmailSettings.SendPushNotifications": true",``  |
| - **true**: **(Default)** Your Mattermost server sends mobile   | - Environment variable: ``MM_EMAILSETTINGS_SENDPUSHNOTIFICATIONS``             |
|   push notifications to the server specified.                   |                                                                                |
| - **false**: Mobile push notifications are disabled.            |                                                                                |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------+

.. config:setting:: push-serverlocation
  :displayname: Push notification server location (Push Notifications)
  :systemconsole: Environment > Push Notification Server
  :configjson: .EmailSettings.PushNotificationServer
  :environment: MM_EMAILSETTINGS_PUSHNOTIFICATIONSERVER
  :description: The URL of the Mattermost Push Notification Service (MPNS), which re-sends push notifications from Mattermost to services like Apple Push Notification Service (APNS) and Google Cloud Messaging (GCM).

Push notification server location
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+--------------------------------------------------------------------------------+
| The location of Mattermost Push Notification Service (MPNS),    | - System Config path: **Environment > Push Notification Server**               |
| which re-sends push notifications from Mattermost to services   | - ``config.json setting``: ``".EmailSettings.PushNotificationServer",``        |
| like Apple Push Notification Service (APNS) and Google Cloud    | - Environment variable: ``MM_EMAILSETTINGS_PUSHNOTIFICATIONSERVER``            |
| Messaging (GCM).                                                |                                                                                |
|                                                                 |                                                                                |
| - Customers running a Professional or Enterprise Edition        |                                                                                |
|   workspace should enter ``https://push.mattermost.com`` for    |                                                                                |
|   the push notification server hosted in the United States.     |                                                                                |
| - If you prefer to use a push notification server hosted in     |                                                                                |
|   Germany, enter ``https://hpns-de.mattermost.com/``.           |                                                                                |
| - Team Edition customers should enter                           |                                                                                |
|   ``https://push-test.mattermost.com``.                         |                                                                                |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------+
| **Notes**:                                                                                                                                       |
|                                                                                                                                                  |
| - The TPNS is provided for testing push notifications prior to compiling your own service. Ensure you’re familiar with its `limitations          |
|   </deploy/mobile-hpns.html#test-push-notifications-service-tpns>`__. Review the                                                                 |
|   `mobile push notifications </deploy/mobile-hpns.html>`__                                                                                       |
|   and `mobile apps </deploy/build-custom-mobile-apps.html>`__ documentation, including guidance on compiling your own                            |
|   mobile apps and MPNS, before deploying to production.                                                                                          |
| - To confirm push notifications are working, connect to the `Mattermost iOS App <https://apps.apple.com/us/app/mattermost/id1257222717>`__       |
|   available on the App Store, or the `Mattermost Android App <https://play.google.com/store/apps/details?id=com.mattermost.rn>`__ available on   |
|   Google Play.                                                                                                                                   |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------+

.. config:setting:: push-maxnotificationsperchannel
  :displayname: Maximum notifications per channel (Push Notifications)
  :systemconsole: Environment > Push Notification Server
  :configjson: .TeamSettings.MaxNotificationsPerChannel
  :environment: MM_EMAILSETTINGS_MAXNOTIFICATIONSPERCHANNEL
  :description: The maximum total number of users in a channel before @all, @here, and @channel no longer send desktop, email, or mobile push notifications to maximize performance. Default is **1000** users.

Maximum notifications per channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+--------------------------------------------------------------------------------------+
| The maximum total number of users in a channel before @all,     | - System Config path: **Environment > Push Notification Server**                     |
| @here, and @channel no longer send desktop, email, or mobile    | - ``config.json setting``: ``".TeamSettings.MaxNotificationsPerChannel: 1000",``     |
| push notifications to maximize performance.                     | - Environment variable: ``MM_EMAILSETTINGS_MAXNOTIFICATIONSPERCHANNEL``              |
|                                                                 |                                                                                      |
| Numerical input. Default is **1000**.                           |                                                                                      |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------+
| **Note**: We recommend increasing this value a little at a time, monitoring system health by tracking `performance monitoring metrics                  |
| </scale/performance-monitoring.html>`__, and only increasing this value if large channels have restricted permissions                                  |
| controlling who can post to the channel, such as a read-only Town Square channel.                                                                      |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------+
