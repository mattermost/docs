.. meta::
   :name: robots
   :content: noindex

:orphan:
:nosearch:

Configure mobile push notifications for Mattermost by going to **System Console > Environment > Push Notification Server**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: enable-push-notifications
  :displayname: Enable push notifications (Push Notifications)
  :systemconsole: Environment > Push Notification Server
  :configjson: .EmailSettings.SendPushNotifications
  :environment: MM_EMAILSETTINGS_SENDPUSHNOTIFICATIONS

  - **Do not send push notifications**:  Mobile push notifications are disabled.
  - **Use HPNS connection with uptime SLA to send notifications to iOS and Android apps**: **(Default)** Use Mattermost's hosted push notification service.
  - **Use TPNS connection to send notifications to iOS and Android apps**: Use Mattermost's test push notification service.
  - **Manually enter Push Notification Service location**: When building your own custom mobile apps, you must host your own mobile push proxy service, and specify that URL in the Push Notification Server field.

Enable push notifications
~~~~~~~~~~~~~~~~~~~~~~~~~

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

Hosted Push Notifications Service (HPNS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-pro-cloud-selfhosted.rst
  :start-after: :nosearch:

Mattermost Enterprise, Professional, and Cloud customers can use Mattermost's Hosted Push Notification Service (HPNS). The HPNS offers:

- Access to a publicly-hosted Mattermost Push Notification Service (MPNS) `available on GitHub. <https://github.com/mattermost/mattermost-push-proxy>`__
- An explicit `privacy policy <https://mattermost.com/data-processing-addendum/>`__ for the contents of unencrypted messages.
- Encrypted TLS connections:

  - Between HPNS and Apple Push Notification Services 
  - Between HPNS and Google’s Firebase Cloud Messaging Service 
  - HPNS and your Mattermost Server
- Production-level uptime expectations.
- Out-of-box configuration for new servers means nothing is required to enable HPNS for new deployments. HPNS can be `enabled for existing deployments <#enable-hpns-for-existing-deployments>`_.

.. note:: 
  - The HPNS only works with pre-built apps Mattermost deploys through the Apple App Store and Google Play Store. If you build your own mobile apps, you must also `host your own Mattermost push proxy server <#host-your-own-push-proxy-service>`_.
  - You must ensure that the push proxy can be reached on the correct port. For HPNS, it's port 443 from the Mattermost server.
  - Mattermost doesn't store any notification data. Any data being stored is at the server level only, such as the ``device_id``, since the HPNS needs to know which device the notification must be sent to.

Test Push Notifications Service (TPNS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Non-commercial and self-hosted customers can use Mattermost's free, basic Test Push Notifications Service (TPNS).

.. note::
  - The TPNS isn’t recommended for use in production environments, and doesn’t offer production-level update service level agreements (SLAs). 
  - The TPNS isn't available for Mattermost Cloud deployments.
  - The TPNS only works with the pre-built mobile apps that Mattermost deploys through the Apple App Store and Google Play Store. If you have built your own mobile apps, you must also `host your own Mattermost push proxy service <#host-your-own-push-proxy-service>`_.
  - You must ensure that the push proxy can be reached on the correct port. For TPNS, it's port 80 from the Mattermost server.
  - If you don't need or want Mattermost to send mobile push notifications, disabling this configuration setting in larger deployments may improve server performance in the following areas:

    - Reduced Processing Load: Generating and sending push notifications requires processing power and resources. By disabling them, the server can allocate those resources to other tasks.
    - Decreased Network Traffic: Push notifications involve network communication. Disabling them reduces the amount of data being transferred, which can enhance overall network performance.
    - Lower Database Load: Each push notification may involve reading from and writing to the database. Reducing these operations decreases the load on the database, improving response times for other queries.
    - Faster Response Times: With fewer tasks to handle related to notifications, the system can respond faster to other requests from users, leading to a better user experience.
    - Simplified Error Handling: Push notification services can sometimes fail or have latency issues, requiring additional error handling. Disabling these notifications simplifies the system's operations.
    - However, disabling push notifications can negatively impact user experience, communication efficiency, and overall productivity. It’s important to balance performance improvements with the needs of your organization and users.

ID-only push notifications
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Admins can enable mobile notifications to be fully private to protect a Mattermost customer against breaches in iOS and Android notification infrastructure by limiting the data sent to Apple and Google through a Mattermost configuration setting.

The standard way to send notifications to iOS and Android applications requires sending clear text messages to Apple or Google so they can be forwarded to a user’s phone and displayed on iOS or Android. While Apple or Google assure the data is not collected or stored, should the organizations be breached or coerced, all standard mobile notifications on the platform could be compromised.

To avoid this risk, Mattermost can be configured to replace mobile notification text with message ID numbers that pass no information to Apple of Google. When received by the Mattermost mobile application on a user’s phone, the message IDs are used to privately communicate with their Mattermost server and to retrieve mobile notification messages over an encrypted channel. This means that, at no time, is the message text visible to Apple or Google’s message relay system. The contents of the message also won't reach Mattermost.

.. note::
  Because of the extra steps to retrieve the notifications messages under Mattermost’s private mobility capability with ID-only push notifications, end users may experience a slight delay before the mobile notification is fully displayed compared to sending clear text through Apple and Google’s platform.

See our :ref:`configuration settings <configure/site-configuration-settings:push notification contents>` documentation to learn more about the ID-only push notifications configuration setting. See our :ref:`Mobile Apps FAQ documentation <deploy/mobile/mobile-faq:how can i use id-only push notifications to protect notification content from being exposed to third-party services?>` for details on using ID-only push notifications for data privacy.

.. config:setting:: push-notification-server-location
  :displayname: Push notification server location (Push Notifications)
  :systemconsole: Environment > Push Notification Server
  :configjson: .EmailSettings.PushNotificationServer
  :environment: MM_EMAILSETTINGS_PUSHNOTIFICATIONSERVER
  :description: The physical location of the Mattermost Hosted Notification Service (HPNS) server.

Push notification server location
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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