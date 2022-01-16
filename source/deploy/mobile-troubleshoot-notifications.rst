:orphan:

Troubleshooting Push Notifications
==================================

If you did not receive a push notification when :doc:`testing push notifications <mobile-testing-notifications>`, use the following procedure to troubleshoot:

1. In **System Console > Environment > Logging > File Log Level**, select **DEBUG** in order to watch for push notifications in the server log.

2. Delete your mobile application, and reinstall it.

3. Sign in with "Account A" and **confirm you want to receive push notifications** when prompted by the mobile app.

4. Go to **Profile** > **Security** > **View and Logout of Active Sessions** to confirm that there is a session for the native mobile app matching your login time.

5. Repeat the procedure for :doc:`testing push notifications <mobile-testing-notifications>`.

6. If no push notification displays, go to **System Console** > **Server Logs**, then select **Reload**. Look at the bottom of the logs for a message similar to:

``[2016/04/21 03:16:44 UTC] [DEBG] Sending push notification to 608xyz0... wi msg of '@accountb: Hello'``

  - If the log message displays, it means a message was sent to the HPNS server and was not received by your mobile app. Please contact support@mattermost.com with the subject "HPNS issue" for help from Mattermost's Support team.
  - If the log message does not display, it means no mobile push notification was sent to “Account A”. Please repeat the process starting at step 2 and double-check each step.

.. important::

  To conserve disk space, once your push notification issue is resolved, go to  **System Console > Environment > Logging > File Log Level**, then select **ERROR** to switch your logging detail level from **DEBUG** to **Errors Only**.

If push notifications are not being delivered on the mobile device, confirm that you're logged in to the **Native** mobile app session through **Profile > Security > View and Log Out of Active Sessions**. Otherwise, the `DeviceId` won't get registered in the `Sessions` table and notifications won't be delivered.