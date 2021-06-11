Mobile Push Notifications
=========================

A push proxy is a key technology behind notification transmission that enables notifications between the server and a Mobile app. See our `Mobile Apps FAQ documentation <https://docs.mattermost.com/mobile/mobile-faq.html#how-do-push-notifications-work>`__ to learn more about how push notifications work.

Mattermost offers push proxy options for Mattermost Team Edition, Cloud, and Enterprise deployments, including:

- `Test Push Notifications Service (TPNS) <#id1>`_
- `Hosted Push Notifications Service (HPNS) <#id2>`_
- `Mattermost Push Notification Service (MPNS) <#id3>`_
- `Host Your Own Push Proxy Service <#id4>`_

Test Push Notifications Service (TPNS)
--------------------------------------

Mattermost offers a free, basic hosted service for self-managed deployments. 

.. note::
  - The TPNS isn’t recommended for use in production environments, and doesn’t offer production-level update service level agreements (SLAs). 
  - The TPNS isn't available for Mattermost Cloud deployments.

To use the Mattermost TPNS, go to **System Console > Environment > Push Notification Server > Enable Push Notifications**, then select **Use TPNS connection to send notifications to iOS and Android apps**.

See our `Testing Push Notifications <https://docs.mattermost.com/mobile/mobile-testing-notifications.html>`__ documentation to learn more about testing mobile push notifications.

.. note::
  - The TPNS only works with the pre-built apps Mattermost deploys through the Apple App Store and Google Play Store. If you have built your own mobile apps, you must also `host your own Mattermost push proxy service <#id4>`_.  
  - You must ensure that the push proxy can be reached on the correct port. For TPNS, it's port 80.

Hosted Push Notifications Service (HPNS)
----------------------------------------

Mattermost Cloud and Enterprise Edition E10 and E20 customers can use Mattermost's Hosted Push Notification Service (HPNS).

Our Hosted Push Notification Service offers:

- Access to a publicly-hosted Mattermost Push Notification Service (MPNS) `available on GitHub. <https://github.com/mattermost/mattermost-push-proxy>`__
- An explicit `privacy policy <https://mattermost.com/data-processing-addendum/>`__ for the contents of unencrypted messages.
- Encrypted TLS connections:
  - Between HPNS and Apple Push Notification Services 
  - Between HPNS and Google’s Firebase Cloud Messaging Service 
  - HPNS and your Mattermost Server
- Production-level uptime expectations.
- Out-of-box configuration for new servers, so nothing is required to enable it on new deployments.

.. note:: 
  - The TPNS only works with pre-built apps Mattermost deploys through the Apple App Store and Google Play Store. If you have built your own mobile apps, you must also `host your own Mattermost push proxy server <#id4>`_.
  - You must ensure that the push proxy can be reached on the correct port. For HPNS, it's port 443 from the Mattermost server.

ID-Only Push Notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Cloud and Enterprise Edition E20 customers can limit the data sent to Apple and Google through a configuration setting. 

When enabled, a message containing only an ID is transmitted. Once the mobile client receives this ID, the message contents are loaded from the server, and are never transmitted through the Apple Push Notification Service (APNS) or Firebase Cloud Messaging (FCM). The contents of the message also won't reach the `Mattermost Push Notification Service (MPNS) <https://docs.mattermost.com/deployment/deployment.html#push-notification-service>`__.

See our `Configuration Settings <https://docs.mattermost.com/administration/config-settings.html#push-notification-contents>`__ documentation to learn more about the ID-only push notifications configuration setting. See our `Mobile Apps FAQ documentation <https://docs.mattermost.com/mobile/mobile-faq.html#how-can-i-use-id-only-push-notifications-to-protect-notification-content-from-being-exposed-to-third-party-services>`__ for details on using ID-only push notifications for data privacy.

Enabling HPNS Push Notifications on Existing Deployments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuring your existing Mattermost instance to use the Mattermost HPNS is a single, one-time step. 

1. Follow the instructions to `install or upgrade to Enterprise Edition <https://docs.mattermost.com/install/ee-install.html>`__.

2. Go to **System Console > Environment > Push Notification Server**.

3. Set **Enable Push Notifications** to **Use HPNS connection with uptime SLA to send notifications to iOS and Android apps**. Note that this option is only available in Mattermost Enterprise Edition.

4. Specify the URL of the **Push Notification Server** based on your Mattermost edition.

- Mattermost Team Edition: ``https://push-test.mattermost.com``
- Mattermost Enterprise Edition: ``https://push.mattermost.com``

.. image:: ../images/mobile_hpns.png

5. Review the Mattermost Terms of Service and the Mattermost Privacy Policy, then select the box "I understand and accept the Mattermost Hosted Push Notification Service Terms of Service and Privacy Policy" to acknowledge that you understand the terms of use.

.. note:: 

  The default **Push Notification Server** address is ``https://push.mattermost.com``. The server is hosted inside the United States. Mattermost also offers a push notification server hosted in Germany. If you wish to use the server in Germany, update the **Push Notification Server** address to ``https://hpns-de.mattermost.com/``.

6. Select **Save**

After setup, test push notifications to confirm they are working.

Mattermost Push Notification Service (MPNS)
-------------------------------------------

Mattermost provides a self-hosted push proxy you can deploy called the `Mattermost Push Notification Service (MPNS) <https://docs.mattermost.com/deployment/deployment.html#push-notification-service>`__. 

Enabling MPNS in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to **System Console > Environment > Push Notification Server**.
2. Under **Enable Push Notifications**, then select **Manually enter Push Notification Service location**.
3. Enter the location of your MPNS in the **Push Notification Server** field, then select **Save**.
4. (Optional) Customize mobile push notification contents. Most deployments choose to include the full message content sent in the notification payload.
  a. Go to **System Console > Site Configuration > Notifications**.
  b. Under **Push Notification Contents**, select the type of information to include in push notifications, then select **Save**.

Host Your Own Push Proxy Service
--------------------------------

If you choose to build custom versions of the Mattermost Mobile app, you must host your own instance of the MPNS by compiling your own MPNS from the `open source repository <https://github.com/mattermost/mattermost-push-proxy>`__, or by using the `pre-compiled version available on GitHub <https://github.com/mattermost/mattermost-push-proxy/releases>`__. 

See our `developer documentation <https://developers.mattermost.com/contribute/mobile/push-notifications/service/>`__ on installing the Mattermost Push Notification Service for details.

.. note::

   - We recommend that your instance of the MPNS be behind your firewall inside your private network, or in your DMZ, in a way that the Mattermost server can access it.
   - The MPNS does not connect with Mattermost mobile apps directly; the MPNS parses and forwards push notifications from the Mattermost server to the Apple Push Notification Service (APNS) or the Firebase Cloud Messaging (FCM).
   - The MPNS must be able to communicate with the Apple Push Notification Service over HTTP/2. If an outbound proxy appliance is deployed between the MPNS and APNS, ensure it supports HTTP/2.
     - Ensure you use encrypted TLS connections between your MPNS and Apple, between your MPNS and Facebook, and between your MPNS and your Mattermost server.
   - You must ensure that the push proxy can be reached on the correct port. The default port is 8086.
   - As part of the process of building the applications, you'll need to sign the applications. You must also obtain the appropriate certificate for both Android and iOS. If this isn't done, the applications won't be able to interact with your instance of the MPNS. Once this is complete, you can proceed with the deployment of your MPNS instance.
   - We strongly recommend that you subscribe to `Mattermost Security Bulletins <https://mattermost.com/security-updates/#sign-up>`__. When you're notified of security updates for the MPNS, apply them promptly.