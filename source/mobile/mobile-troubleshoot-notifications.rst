Troubleshooting Push Notifications
==================================

If you did not receive a push notification when :doc:`testing push notifications <mobile-testing-notifications>`, use the following procedure to troubleshoot:

1. Under **System Console** > **General** > **Logging** > **File Log Level** select **DEBUG** in order to watch for push notifications in the server log.

2. Delete your mobile application, and install it again.

3. Sign in with "Account A" and **confirm you want to receive push notifications** when prompted by the mobile app.

4. On desktop, go to **Account Settings** > **Security** > **View and Logout of Active Sessions** and check that there is a session for the native mobile app matching your login time.

5. Repeat the procedure for :doc:`testing push notifications <mobile-testing-notifications>`.

6. If no push notification appears go to **System Console** > **Logs** and click **Reload**. Look at the bottom of the logs for a message similar to:

``[2016/04/21 03:16:44 UTC] [DEBG] Sending push notification to 608xyz0... wi msg of '@accountb: Hello'``

  - If the log message appears, it means a message was sent to the HPNS server and was not received by your mobile application. Please contact support@mattermost.com with the subject "HPNS issue on Step 8" for help from the commercial support team.
  - If the log message does not appear, it means no mobile push notification was sent to “Account A”. Please repeat starting at step 2 and double check each step.

5. **IMPORTANT:** After your issue is resolved, go to **System Console** > **General** > **Logging** > **File Log Level** and select **ERROR** to switch your logging detail level to Errors Only, instead of DEBUG, in order to conserve disk space.
