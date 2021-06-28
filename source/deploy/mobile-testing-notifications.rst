Testing Push Notifications
==========================

Make sure to configure push notifications for your `pre-built mobile apps <https://docs.mattermost.com/mobile/use-prebuilt-mobile-apps.html>`__, or for `your custom built mobile apps <https://docs.mattermost.com/mobile/build-custom-mobile-apps.html>`__. 

Then use the following instructions to confirm push notifications are working properly.

1. Sign in to your mobile app with an account on your Mattermost Server, which we’ll refer to as “Account A”.

2. (iOS) When the app asks whether you wish to receive notifications, **confirm you want to receive notifications**.

  .. image:: ../images/mobile_push_prompt.png
    :width: 300 px

3. Confirm push notifications are enabled for “Account A”.

  A. Go to the notification settings menu in the mobile app.

  .. image:: ../images/mobile_notification_settings.png

  B. Check that the mobile push notifications are set to send.

  .. image:: ../images/mobile_push_send_for.png
    :width: 300 px
  .. image:: ../images/mobile_push_send_when.png
    :width: 300 px

4. Have “Account A” put the app to background or close the app.

5. Using a browser, sign in to “Account B” on the same Mattermost Server.

6. Open a Direct Message with “Account A”, and send a message.

7. A push notification with the message should appear on the mobile device of “Account A”.

If the push notification does not appear, follow :doc:`troubleshooting steps <mobile-troubleshoot-notifications>` to look for issues.
