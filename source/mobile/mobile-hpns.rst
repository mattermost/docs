Hosted Push Notification Service
================================

Securing your Mattermost Push Notification Service
--------------------------------------------------

When using Mattermost mobile apps in the Apple App Store and Google Play, purchase an annual subscription to `Mattermost Enterprise Edition E10 <https://mattermost.com/pricing-self-managed/>`__ or higher to receive access to our Hosted Push Notification Service (HPNS).

Our Hosted Push Notification Service offers:

- Access to a publicly-hosted Mattermost Push Notification Service (MPNS) offering an explicit `privacy policy <https://mattermost.com/data-processing-addendum/>`__ where the contents of unencrypted messages are not examined or stored.
- Encrypted TLS connections between HPNS and Apple Push Notification Services, HPNS and Google’s Firebase Cloud Messaging service, and HPNS and your Mattermost server.
- Production-level uptime expectation.

After purchasing a subscription to Mattermost Enterprise Edition E10 or higher from Mattermost, Inc. follow the instructions below to set up and test your system.

.. Note:: 

  - Both TPNS and HPNS only work with the Mattermost Apple App Store and Google Play apps. If you have compiled the apps yourself, you must also host your own Mattermost push proxy server. See our FAQ on :ref:`how push notifications work <push-faq>` for more details. Our push proxy server is `available on Github. <https://github.com/mattermost/mattermost-push-proxy>`__
- You must ensure that the push proxy can be reached on the correct port. For HPNS, it's port 443 from the Mattermost server, and for TPNS, it's port 80. If you host your own proxy server, the default port is 8086.
- Mattermost, Inc. also offers a free basic hosted service for testing called the Test Push Notification Service (TPNS). It does not offer production-level uptime service level agreements (SLAs).

Setting up HPNS Push Notifications in Enterprise Edition
--------------------------------------------------------

Follow these steps to set up HPNS:

1. Follow the instructions to `install or upgrade to Enterprise Edition <https://docs.mattermost.com/install/ee-install.html>`__.

2. Go to **System Console > Environment > Push Notification Server** (or go to **System Console > Notifications > Mobile Push > Send Push Notifications** in versions prior to v5.12).

3. Set **Enable Push Notifications** to **Use HPNS connection with uptime SLA to send notifications to iOS and Android apps**. Note that this option appears only in Enterprise Edition.

.. image:: ../images/mobile_hpns.png

4. Review the Mattermost Terms of Service and the Mattermost Privacy Policy, then select the box "I understand and accept the Mattermost Hosted Push Notification Service Terms of Service and Privacy Policy" to acknowledge that you understand the terms of use.

.. Note:: 

  The default **Push Notification Server** address is ``https://push.mattermost.com`` and the server is hosted inside the United States. Mattermost also offers a push notification server hosted in Germany. If you wish to use that server, please update the **Push Notification Server** address to ``https://hpns-de.mattermost.com/``.

5. Select **Save**

After setup, :doc:`test push notifications <mobile-testing-notifications>` to confirm they are working.
