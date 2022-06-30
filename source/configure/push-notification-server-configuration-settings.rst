Push notification server configuration settings
===============================================

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 25
  :target: https://mattermost.com/sign-up
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 25
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Configure Mattermost to enable push notifications to Mattermost clients by going to **System Console > Environment > Push Notification Server**, or by editing the ``config.json`` file as described in the following table. Changes to configuration settings in this section require a server restart before taking effect.

.. include:: common-config-settings-notation.rst
    :start-after: :nosearch:

Enable push notifications
-------------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+--------------------------------------------------------------------------------+
| You can disable Mattermost push notifications.                  | - System Config path: **Environment > Push Notification Server**               |
|                                                                 | - ``config.json setting``: ``".EmailSettings.SendPushNotifications": true",``  |
| - **true**: **(Default)** Your Mattermost server sends mobile   | - Environment variable: ``MM_EMAILSETTINGS_SENDPUSHNOTIFICATIONS``             |
|   push notifications to the server specified.                   |                                                                                |
| - **false**: Mobile push notifications are disabled.            |                                                                                |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------+

Push notification server
-------------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+--------------------------------------------------------------------------------+
| Location of Mattermost Push Notification Service (MPNS),        | - System Config path: **Environment > Push Notification Server**               |
| which re-sends push notifications from Mattermost to services   | - ``config.json setting``: ``".EmailSettings.PushNotificationServer",``        |
| like Apple Push Notification Service (APNS) and Google Cloud    | - Environment variable: ``MM_EMAILSETTINGS_PUSHNOTIFICATIONSERVER``            |
| Messaging (GCM).                                                |                                                                                |
|                                                                 |                                                                                |
| - Customers running an Enterprise or Professional Edition       |                                                                                |
|   workspace should enter ``https://push.mattermost.com`` for    |                                                                                |
|   the push notification server hosted in the United States.     |                                                                                |
| - If you prefer to use a push notification server hosted in     |                                                                                |
|   Germany, enter ``https://hpns-de.mattermost.com/``.           |                                                                                |
| - Team Edition customers should enter                           |                                                                                |
|   ``https://push-test.mattermost.com``.                         |                                                                                |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------+
| **Note**:                                                                                                                                        |
|                                                                                                                                                  |
| - The TPNS is provided for testing push notifications prior to compiling your own service. Ensure you’re familiar with its `limitations          |
|   <https://docs.mattermost.com/deploy/mobile-hpns.html#test-push-notifications-service-tpns>`__. Review the                                      |
|   `mobile push notifications <https://docs.mattermost.com/deploy/mobile-hpns.html>`__                                                            |
|   and `mobile apps <https://docs.mattermost.com/deploy/build-custom-mobile-apps.html>`__ documentation, including guidance on compiling your own |
|   mobile apps and MPNS, before deploying to production.                                                                                          |
| - To confirm push notifications are working, connect to the `Mattermost iOS App <https://apps.apple.com/us/app/mattermost/id1257222717>`__       |
|   available on the App Store, or the `Mattermost Android App <https://play.google.com/store/apps/details?id=com.mattermost.rn>`__ available on   |
|   Google Play.                                                                                                                                   |          
+-----------------------------------------------------------------+--------------------------------------------------------------------------------+

Maximum notifications per channel
---------------------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Maximum total number of users in a channel before @all, @here,  | - System Config path: **Environment > Push Notification Server**                     |
| and @channel no longer send notifications to maximize           | - ``config.json setting``: ``".TeamSettings.MaxNotificationsPerChannel: 1000",``     |
| performance.                                                    | - Environment variable: ``MM_EMAILSETTINGS_MAXNOTIFICATIONSPERCHANNEL``              |
|                                                                 |                                                                                      |
| Numerical input. Default is 1000.                               |                                                                                      |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------+
| **Note**: We recommend increasing this value a little at a time, monitoring system health by tracking `performance monitoring metrics                  |
| <https://docs.mattermost.com/scale/performance-monitoring.html>`__, and only increasing this value if large channels have restricted permissions       |
| controlling who can post to the channel, such as a read-only Town Square channel.                                                                      |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------+