Customize Mattermost notifications
==================================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

On this page, you'll learn about Mattermost notifications and how to set notification preferences.

Default notifications
---------------------

By default, when new channel messages, thread responses, mentions, key trigger words, or new direct or group messages are received, Mattermost users are notified in the following ways:

- **Desktop App notifications** - All users can `personalize Desktop App notifications, <https://docs.mattermost.com/channels/channels-settings.html#desktop-notifications>`__, including collapsed reply thread notifications, based on preference.
- **Mobile Apps push notifications** - You can `control the contents of push notification <https://docs.mattermost.com/configure/configuration-settings.html#push-notification-contents>`__, and all users can `personalize push notifications based on preference <https://docs.mattermost.com/channels/channels-settings.html#mobile-push-notifications>`__. Mattermost subscription plans also include access to Mattermost's `Hosted Push Notification Service <https://docs.mattermost.com/deploy/mobile-hpns.html#hosted-push-notifications-service-hpns>`__ featuring encrypted TLS connections and production-level uptime service level agreements.
- **Browser tab notifications** - Unread messages and a count of mentions or direct messages is displayed on Chrome, Edge, Firefox, and Safari.

Email notifications
-------------------

You can `enable email notifications <https://docs.mattermost.com/configure/configuration-settings.html#enable-email-notifications>`__ for mentions and direct messages received while users are away from or logged out of Mattermost. If email notifications are too noisy, you can also `enable batched email notifications <https://docs.mattermost.com/configure/configuration-settings.html#enable-email-batching>`__. Email notifications require a configured `SMTP email server <https://docs.mattermost.com/configure/configuration-settings.html#smtp-email-server>`__.

What's next?
------------

Now that you've learned about Mattermost notifications, next you'll want to learn how to :doc:`monitor your Mattermost deployment </getting-started/get-started-monitor>` with logging, audit logging, performance monitoring tools, and using workspace optimization tools available from Mattermost v6.5.