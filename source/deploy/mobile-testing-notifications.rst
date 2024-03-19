Testing push notifications
==========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Make sure to configure push notifications for your :doc:`pre-built mobile apps </deploy/use-prebuilt-mobile-apps>`, or for :doc:`your custom built mobile apps </deploy/build-custom-mobile-apps>`. 

Then use the following instructions to confirm push notifications are working properly.

1. Log in to your mobile app with an account on your Mattermost Server, which we’ll refer to as “Account A”.

2. (iOS) When the app asks whether you wish to receive notifications, **confirm you want to receive notifications**.

  .. image:: ../images/mobile_push_prompt.png
    :alt: Mattermost prompts you to confirm whether you want to allow mobile push notifications. To test mobile push notifications, you must select Allow.
    :width: 300 px

3. Confirm push notifications are enabled for “Account A”.

  A. Go to the notification settings menu in the mobile app.

  .. image:: ../images/mobile_notification_settings.png
    :alt: Access notification settings by selecting your profile picture to access Settings > Notifications.

  B. Check that the mobile push notifications are set to send.

  .. image:: ../images/mobile_push_send_for.png
    :alt: Select Push Notifications to confirm when mobile push notifications will be sent.
    :width: 300 px

  .. image:: ../images/mobile_push_send_when.png
    :alt: Specify whether all new messages or only mentions and direct messages send push notifications. 
    :width: 300 px

4. Have “Account A” put the app to background or close the app.

5. Using a browser, log in to “Account B” on the same Mattermost Server.

6. Open a direct message with “Account A”, and send a message.

7. A push notification with the message should appear on the mobile device of “Account A”. If the push notification does not appear, follow :doc:`troubleshooting steps <mobile-troubleshoot-notifications>` to look for issues.
