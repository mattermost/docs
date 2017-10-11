Hosted Push Notification Service
================================

Securing your Mattermost Push Notification Service
--------------------------------------------------

When using Mattermost mobile apps in the Apple App Store and Google Play, purchase an annual subscription to `Mattermost Enterprise Edition E10 <https://about.mattermost.com/pricing/>`_ or higher to receive access to our Hosted Push Notification Service (HPNS).

Our Hosted Push Notification Service offers:

  - Access to a publicly-hosted Mattermost Push Notification Service (MPNS) offering an explicit privacy policy where the contents of unencrypted messages are not examined or stored
  - Encrypted TLS connections between HPNS and Apple Push Notification Services, HPNS and Google’s Firebase Cloud Messaging service, and HPNS and your Mattermost server
  - Production-level uptime expectation

After purchasing a subscription to Mattermost E10 or higher from Mattermost, Inc. follow the instructions below to set up and test your system.

.. Note:: Mattermost, Inc. also offers a free basic hosted service for testing setups called the Test Push Notification Service (TPNS). It does not offer a production-level uptime expectation, nor does it offer encrypted transport.

Both TPNS and HPNS only work with the Mattermost Apple App Store and Google Play apps. If you have compiled the apps yourselves, you must also host your own Mattermost push proxy server. See our FAQ on :ref:`how push notifications work <push-faq>` for more details.


Setting up HPNS push notifications in Enterprise Edition
--------------------------------------------------------

Follow these steps to set up HPNS:

1. Follow the instructions to `install or upgrade to Enterprise Edition <http://docs.mattermost.com/install/ee-install.html>`_

2. Go to **System Console** > **Notifications** > **Mobile Push** > **Send Push Notifications**

3. Select "Use encrypted, production-quality HPNS connection to iOS and Android apps" (this option appears only in Enterprise Edition)

.. image:: ../images/mobile_hpns.png

4. Check the box "I understand and accept the Mattermost Hosted Push Notification Service Terms of Service and Privacy Policy" after reading the documents referenced

5. Click **Save**

After setup, :doc:`test push notifications <mobile-testing-notifications>` to confirm they are working.
