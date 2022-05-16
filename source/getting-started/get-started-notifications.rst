Customize Mattermost notifications
==================================

all-plans | self-hosted


Desktop app & browser tab notifications, email notifications, and mobile push notifications: https://docs.mattermost.com/channels/channels-settings.html#notifications

Option
Recommendations
Desktop Notifications
For efficient focus, select the following options:
Only for mentions and direct messages
Notify me about threads I’m following

Tips:
A notification sound can be enabled or disabled based on preference.
For deployments with Collapsed Reply Threads (Beta) enabled:
Follow threads of interest on demand.
Unfollow threads that become less relevant over time.
Email Notifications
Valuable to new users, but may be noisy for experienced users.
Mobile Push Notifications
For efficient focus, select the following options:
Only for mentions and direct messages
Trigger push notifications can be updated based on specific circumstances, such as when in meetings or workshops.
Notify me about threads I’m following
Words that Trigger Mentions
Specify any additional non-case sensitive words to be notified on, such as hashtags, subjects, or customer names.
Reply notifications
For deployments with Collapsed Reply Threads (Beta) disabled:
Receive notifications when someone replies to a thread the user started only, or started and participated in.
Automatic Direct Message Replies
Enable Automatic Replies by going to System Console > Experimental > Features to allow all users to set an automated custom message that will be sent once per day in response to Direct Messages.


**4. Enable full content push notifications**

Enable push notifications on mobile devices to deliver messages in real time by setting **System Console > Push Notification Server > Enable Push Notifications** to **Use TPNS**. See the `Push notification server <https://docs.mattermost.com/configure/configuration-settings.html#push-notification-server>`__ configuration settings documentation for details.

Enable full content push notifications, including the sender’s name, the channel name, and the message text, by setting **System Console > Notifications > Push Notification Contents** to **Full message contents**. See the `Push notification contents <https://docs.mattermost.com/configure/configuration-settings.html#push-notification-contents>`__ configuration settings documentation for details.

.. note::

  - Mattermost subscription plans allow you to `enable HPNS <https://docs.mattermost.com/deploy/mobile-hpns.html#hosted-push-notifications-service-hpns>`__ that includes production-level uptime SLAs.

  - Mattermost Enterprise customers can `enable ID-Only push notifications <https://docs.mattermost.com/configure/configuration-settings.html#push-notification-contents>`__ so push notification content is not passed through Apple Push Notification Service (APNS) or Google Firebase Cloud Messaging (FCM) before reaching the device. The ID-only push notification setting `offers a high level of privacy <https://mattermost.com/blog/id-only-push-notifications/>`__ while allowing team members to benefit from mobile push notifications.



  **8. Enable batched email notifications**

Email notifications can be batched together so users don’t get overwhelmed with too many emails.

Enable email notifications first by setting **System Console > Notifications > Enable Email Notifications** to **true**. See the `Enable email notifications <https://docs.mattermost.com/configure/configuration-settings.html#enable-email-notifications>`__ configuration settings documentation for details. Note that email notifications require an `SMTP email server <https://docs.mattermost.com/configure/configuration-settings.html#smtp-email-server>`__ to be configured.

Then, enable batched email notifications by setting **System Console > Notifications > Enable Email Batching** to **true**. See the `Enable email batching <https://docs.mattermost.com/configure/configuration-settings.html#enable-email-batching>`__ configuration settings documentation for details. Note that email batching is not available if you are running your deployment in `High Availability <https://docs.mattermost.com/scale/high-availability-cluster.html>`__.
