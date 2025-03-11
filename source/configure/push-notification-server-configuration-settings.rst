:orphan:
:nosearch:

Configure Mattermost to enable push notifications to Mattermost clients by going to **System Console > Environment > Push Notification Server**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: enable-push-notifications
  :displayname: Enable push notifications (Push Notifications)
  :systemconsole: Environment > Push Notification Server
  :configjson: .EmailSettings.SendPushNotifications
  :environment: MM_EMAILSETTINGS_SENDPUSHNOTIFICATIONS

  - **true**: **(Default)** Your Mattermost server sends mobile push notifications.
  - **false**: Mobile push notifications are disabled.

Enable push notifications
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+------------------------------------------------------------------+--------------------------------------------------------------------------------+
| Enable or disable Mattermost push notifications.                 | - System Config path: **Environment > Push Notification Server**               |
|                                                                  | - ``config.json setting``: ``".EmailSettings.SendPushNotifications": true",``  |
| - **Do not send push notifications**: Mobile push notifications  | - Environment variable: ``MM_EMAILSETTINGS_SENDPUSHNOTIFICATIONS``             |
|   are disabled.                                                  |                                                                                |
| - **Use HPNS connection with uptime SLA to send notifications    |                                                                                |
|   to iOS and Android apps**: **(Default)** Use Mattermost's      |                                                                                |
|   hosted push notification service.                              |                                                                                |
| - **Use TPNS connection to send notifications to iOS and         |                                                                                |
|   Android apps**: Use Mattermost's test push notification        |                                                                                |
|   service.                                                       |                                                                                |
| - **Manually enter Push Notification Service location**:         |                                                                                |
|   When building your own custom mobile apps, you must host your  |                                                                                |
|   own mobile push proxy service, and specify that URL in the     |                                                                                |
|   **Push Notification Server** field.                            |                                                                                |
+------------------------------------------------------------------+--------------------------------------------------------------------------------+

.. note::

  - Mattermost Enterprise, Professional, and Cloud customers can use Mattermost’s SLA-bound :ref:`Hosted Push Notification Service (HPNS) <deploy/mobile-hpns:hosted push notifications service (hpns)>` in one of two locations, including the United States and Germany.
  - Mattermost Team Edition customers can use Mattermost's :ref:`Test Push Notification server (TPNS) <deploy/mobile-hpns:test push notifications service (tpns)>`.
  - The TPNS is provided for testing push notifications prior to compiling your own service, and isn't available for Mattermost Cloud deployments. Ensure you’re familiar with its limitations.
  - Review the :doc:`mobile push notifications </deploy/mobile-hpns>` and :doc:`mobile apps </deploy/build-custom-mobile-apps>` documentation, including guidance on compiling your own mobile apps and MPNS, before deploying to production. See the :ref:`documentation <deploy/mobile-hpns:host your own push proxy service>` for details on hosting your own push proxy service.
  - To confirm push notifications are working, connect to the `Mattermost iOS App <https://apps.apple.com/us/app/mattermost/id1257222717>`__ available on the App Store, or the `Mattermost Android App <https://play.google.com/store/apps/details?id=com.mattermost.rn>`__ available on Google Play.
  - If you don't need or want Mattermost to send mobile push notifications, disabling this configuration setting in larger deployments may improve server performance in the following areas:

    - Reduced Processing Load: Generating and sending push notifications requires processing power and resources. By disabling them, the server can allocate those resources to other tasks.
    - Decreased Network Traffic: Push notifications involve network communication. Disabling them reduces the amount of data being transferred, which can enhance overall network performance.
    - Lower Database Load: Each push notification may involve reading from and writing to the database. Reducing these operations decreases the load on the database, improving response times for other queries.
    - Faster Response Times: With fewer tasks to handle related to notifications, the system can respond faster to other requests from users, leading to a better user experience.
    - Simplified Error Handling: Push notification services can sometimes fail or have latency issues, requiring additional error handling. Disabling these notifications simplifies the system's operations.
    - However, disabling push notifications can negatively impact user experience, communication efficiency, and overall productivity. It’s important to balance performance improvements with the needs of your organization and users.

.. config:setting:: push-notification-server-location
  :displayname: Push notification server location (Push Notifications)
  :systemconsole: Environment > Push Notification Server
  :configjson: .EmailSettings.PushNotificationServer
  :environment: MM_EMAILSETTINGS_PUSHNOTIFICATIONSERVER
  :description: The physical location of the Mattermost Hosted Notification Service (HPNS) server.

Push notification server location
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+--------------------------------------------------------------------------------+
| The physical location of the Mattermost Hosted Push             | - System Config path: **Environment > Push Notification Server**               |
| Notification Service (HPNS) server.                             | - ``config.json setting``: ``".EmailSettings.PushNotificationServer",``        |
|                                                                 | - Environment variable: ``MM_EMAILSETTINGS_PUSHNOTIFICATIONSERVER``            |
| Select from **US** **(Default)** or **Germany** to              |                                                                                |
| automatically populate the **Push Notification Server**         |                                                                                |
| field server URL.                                               |                                                                                |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------+

.. config:setting:: maximum-notifications-per-channel
  :displayname: Maximum notifications per channel (Push Notifications)
  :systemconsole: Environment > Push Notification Server
  :configjson: .TeamSettings.MaxNotificationsPerChannel
  :environment: MM_EMAILSETTINGS_MAXNOTIFICATIONSPERCHANNEL
  :description: The maximum total number of users in a channel before @all, @here, and @channel no longer send desktop, email, or mobile push notifications to maximize performance. Default is **1000** users.

Maximum notifications per channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+--------------------------------------------------------------------------------------+
| The maximum total number of users in a channel before @all,     | - System Config path: **Environment > Push Notification Server**                     |
| @here, and @channel no longer send desktop, email, or mobile    | - ``config.json setting``: ``".TeamSettings.MaxNotificationsPerChannel: 1000",``     |
| push notifications to maximize performance.                     | - Environment variable: ``MM_EMAILSETTINGS_MAXNOTIFICATIONSPERCHANNEL``              |
|                                                                 |                                                                                      |
| Numerical input. Default is **1000**.                           |                                                                                      |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. note::

  - We recommend increasing this value a little at a time, monitoring system health by tracking :doc:`performance monitoring metrics </scale/deploy-prometheus-grafana-for-performance-monitoring>`, and only increasing this value if large channels have restricted permissions controlling who can post to the channel, such as a :ref:`read-only channel <onboard/advanced-permissions:read only channels>`.
  - Reducing this configuration setting value to **10** in larger deployments may improve server performance in the following areas:

    - Reduced Load on Notification System: Each notification generates a certain amount of computational and network load. By limiting the number of notifications per channel, the system processes fewer notifications, thereby reducing the load on servers.
    - Database Efficiency: Notifications are typically stored in a database. Fewer notifications mean less frequent database writes and reads, leading to quicker database operations and reduced latency.
    - Minimized Client Processing: Users' clients (e.g., desktop and mobile apps) have to fetch and process notifications. With fewer notifications, clients can operate more efficiently, reducing memory and CPU usage on users' devices.
    - Improved User Experience: An overload of notifications can lead to performance lags and a cluttered experience for users. Limiting the number ensures that users receive only the most important notifications, which can enhance usability and response times.
    - Network Bandwidth: High numbers of notifications can consume a lot of bandwidth, particularly if they are being sent to many users. Fewer notifications can lead to lower overall network usage and potentially faster delivery of critical messages.
    - Server Load Balancing: By reducing the number of notifications, the workload can be more evenly distributed across the servers, leading to better load balancing and preventing any single server from becoming a bottleneck.