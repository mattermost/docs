Mobile push notifications
=========================

A push proxy is a key technology behind notification transmission that enables notifications between the server and a Mobile app. See our :ref:`Mobile Apps FAQ documentation <deploy/mobile-faq:how do push notifications work?>` to learn more about how push notifications work.

Mattermost offers a :doc:`Mattermost Push Notification Service (MPNS) </deploy/deployment-overview>` for Team Edition, Cloud, and Enterprise deployments.

Test Push Notifications Service (TPNS)
--------------------------------------

.. include:: ../../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Self-hosted customers can use Mattermost's free, basic Test Push Notifications Service (TPNS).

.. note::
  - The TPNS isn’t recommended for use in production environments, and doesn’t offer production-level update service level agreements (SLAs). 
  - The TPNS isn't available for Mattermost Cloud deployments.

Enable TPNS
~~~~~~~~~~~

To use the Mattermost TPNS, go to **System Console > Environment > Push Notification Server > Enable Push Notifications**, then select **Use TPNS connection to send notifications to iOS and Android apps**.

See our :doc:`Testing Push Notifications </deploy/mobile-testing-notifications>` documentation to learn more about testing mobile push notifications.

.. note::
  - The TPNS only works with the pre-built mobile apps that Mattermost deploys through the Apple App Store and Google Play Store. If you have built your own mobile apps, you must also `host your own Mattermost push proxy service <#host-your-own-push-proxy-service>`_.
  - You must ensure that the push proxy can be reached on the correct port. For TPNS, it's port 80 from the Mattermost server.

Hosted Push Notifications Service (HPNS)
----------------------------------------

.. include:: ../../_static/badges/ent-pro-cloud-selfhosted.rst
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

Enable HPNS for existing deployments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuring your existing Mattermost instance to use the Mattermost HPNS is a single, one-time step. 

1. Follow the instructions to :doc:`install or upgrade to Enterprise Edition </install/enterprise-install-upgrade>`.

2. Go to **System Console > Environment > Push Notification Server**.

3. Set **Enable Push Notifications** to **Use HPNS connection with uptime SLA to send notifications to iOS and Android apps**. Note that this option is only available in Mattermost Enterprise Edition.

4. Mattermost Enterprise and Professional customers: Specify the physical location of the **Push Notification Server**.

  - United States: ``https://push.mattermost.com``
  - Germany: ``https://hpns-de.mattermost.com``

.. image:: ../../images/mobile_hpns.png
   :alt: Configure a licensed self-hosted Mattermost deployment to use the Mattermost Hosted Push Notification Server (HPNS) in the System Console by going to Environment > Push Notification Server. Select the HPNS option, then specify the server URL.
   
5. Review the Mattermost Terms of Service and the Mattermost Privacy Policy, then select the box "I understand and accept the Mattermost Hosted Push Notification Service Terms of Service and Privacy Policy" to acknowledge that you understand the terms of use.

6. Select **Save**

After setup, test push notifications to confirm they are working.

ID-only push notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Admins can enable mobile notifications to be fully private to protect a Mattermost customer against breaches in iOS and Android notification infrastructure by limiting the data sent to Apple and Google through a Mattermost configuration setting.

The standard way to send notifications to iOS and Android applications requires sending clear text messages to Apple or Google so they can be forwarded to a user’s phone and displayed on iOS or Android. While Apple or Google assure the data is not collected or stored, should the organizations be breached or coerced, all standard mobile notifications on the platform could be compromised.

To avoid this risk, Mattermost can be configured to replace mobile notification text with message ID numbers that pass no information to Apple of Google. When received by the Mattermost mobile application on a user’s phone, the message IDs are used to privately communicate with their Mattermost server and to retrieve mobile notification messages over an encrypted channel. This means that, at no time, is the message text visible to Apple or Google’s message relay system. The contents of the message also won't reach the :ref:`Mattermost Push Notification Service (MPNS) <deploy/deployment-overview:push notification service>`.

.. note::
  Because of the extra steps to retrieve the notifications messages under Mattermost’s private mobility capability with ID-only push notifications, end users may experience a slight delay before the mobile notification is fully displayed compared to sending clear text through Apple and Google’s platform.

See our :ref:`configuration settings <configure/site-configuration-settings:push notification contents>` documentation to learn more about the ID-only push notifications configuration setting. See our :ref:`Mobile Apps FAQ documentation <deploy/mobile-faq:how can i use id-only push notifications to protect notification content from being exposed to third-party services?>` for details on using ID-only push notifications for data privacy.

