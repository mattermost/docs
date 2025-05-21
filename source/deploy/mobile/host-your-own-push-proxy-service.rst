Host your own push proxy service
=================================

Customers building their own custom mobile apps must host their own push proxy service using one of the following methods:

- Compile your own MPNS from the `open source repository <https://github.com/mattermost/mattermost-push-proxy>`__.
- Use the `pre-compiled version of MPNS available on GitHub <https://github.com/mattermost/mattermost-push-proxy/releases>`__. 

See our `developer documentation <https://developers.mattermost.com/contribute/mobile/push-notifications/service/>`__ on working with the Mattermost Push Notification Service.

Enable MPNS
~~~~~~~~~~~

1. Go to **System Console > Environment > Push Notification Server**.
2. Under **Enable Push Notifications**, select **Manually enter Push Notification Service location**.
3. Enter the location of your MPNS in the **Push Notification Server** field, then select **Save**.

Configure ID-only push notification contents (Enterprise)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
By default, push notification message content passes through Apple Push Notification Service (APNS) or Google Firebase Cloud Messaging (FCM) before it reaches a device. This potentially presents a problem for organizations with ultra-strict security and compliance requirements.

With the ID-only option, message contents can be fetched directly from the server once a push notification is delivered to a device. APNS and FCM can’t read push notifications since only a unique message ID is sent in each notification payload. While message content will take slightly longer to send, this feature helps organizations meet advanced compliance requirements.

To set mobile push notification contents to ID-only: 

1. Go to **System Console > Site Configuration > Notifications**.
2. Under **Push Notification Contents**, select **Full message content fetched from the server on receipt**, then select **Save**.


.. note::

   - We recommend that your instance of the MPNS be behind your firewall inside your private network, or in your DMZ, in a way that the Mattermost server can access it.
   - The MPNS does not connect with Mattermost mobile apps directly; the MPNS parses and forwards push notifications from the Mattermost server to the Apple Push Notification Service (APNS) or the Firebase Cloud Messaging (FCM).
   - The MPNS must be able to communicate with the Apple Push Notification Service over HTTP/2. If an outbound proxy appliance is deployed between the MPNS and APNS, ensure it supports HTTP/2.
     - Ensure you use encrypted TLS connections between your MPNS and Apple Push Notification Service, between your MPNS and Google FCM, and between your MPNS and your Mattermost server.
   - You must ensure that the push proxy can be reached on the correct port. The default port is 8086.
   - As part of the process of building the applications, you'll need to sign the applications. You must also obtain the appropriate certificate for both Android and iOS. If this isn't done, the applications won't be able to interact with your instance of the MPNS. Once this is complete, you can proceed with the deployment of your MPNS instance.
   - We strongly recommend that you subscribe to `Mattermost Security Bulletins <https://mattermost.com/security-updates/#sign-up>`__. When you're notified of security updates for the MPNS, apply them promptly.
