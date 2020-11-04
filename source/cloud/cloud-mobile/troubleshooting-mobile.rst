
Troubleshooting Mobile Applications
===================================

I keep getting a message "Cannot connect to the server. Please check your server URL and internet connection."
--------------------------------------------------------------------------------------------------------------

Confirm that your server URL has no typos and that it includes ``https://``.

Login with ADFS/Office365 is not working
----------------------------------------

In line with Microsoft guidance we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_.

I see a “Connecting…” bar that does not go away
-----------------------------------------------

If your app is working properly, you should see a grey “Connecting…” bar that clears or says “Connected” after the app reconnects.

If you are seeing this message all the time, and your internet connection seems fine, ask your server administrator if the server uses NGINX or another webserver as a reverse proxy. If so, they should check that it is configured correctly for `supporting the websocket connection for APIv4 endpoints <https://docs.mattermost.com/install/install-ubuntu-1804.html#configuring-nginx-as-a-proxy-for-mattermost-server>`__.

I’m not receiving push notifications on my device
-------------------------------------------------

If you did not receive a push notification when testing push notifications, use the following procedure to troubleshoot:

1. In **System Console > Environment > Logging > File Log Level** select **DEBUG** in order to watch for push notifications in the server log.
2. Delete your mobile application, and reinstall it.
3. Sign in with "Account A" and **confirm you want to receive push notifications** when prompted by the mobile app.
4. In Mattermost go to **Account Settings > Security > View and Logout of Active Sessions** and check that there is a session for the native mobile app matching your login time.
5. Repeat the procedure testing push notifications.
6. If no push notification appears go to **System Console > Server Logs** and click **Reload**. Look at the bottom of the logs for a message similar to:

``[2016/04/21 03:16:44 UTC] [DEBG] Sending push notification to 608xyz0... wi msg of '@accountb: Hello'``

  - If the log message appears, it means a message was sent to the HPNS server and was not received by your mobile application. Please contact support@mattermost.com with the subject "HPNS issue on Step 8" for help from the support team.
  - If the log message does not appear, it means no mobile push notification was sent to “Account A”. Please repeat the process starting at step 2 and double-check each step.

**IMPORTANT:** In order to conserve disk space, once the issue is resolved, go to  **System Console > Environment > Logging > File Log Level** and select **ERROR** to switch your logging detail level from DEBUG to Errors Only.

Build gets stuck at ``bundleReleaseJsAndAssets``
------------------------------------------------

As a workaround, you can bundle the ``js`` manually first with

.. code-block:: none

  react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res/

and then ignore the gradle task with

.. code-block:: none

  ./gradlew assembleRelease -x bundleReleaseJsAndAssets

No image previews available in the mobile app
---------------------------------------------

This can happen if the server running Mattermost has its mime types not set up correctly. A server running Linux has this file located in ``/etc/mime.types``. This might vary depending on your specific OS and distribution.

Some distributions also ship without ``mailcap`` which can result in missing or incorrectly configured mime types.

None of these solve my problem!
-------------------------------

For more troubleshooting help, `open a new topic in our forums <https://forum.mattermost.org/c/trouble-shoot>`__ with steps to reproduce your issue. If you're an Enterprise Edition subscriber, you may open a support ticket in the `Enterprise Edition Support portal <https://mattermost.zendesk.com/hc/en-us/requests/new>`_.

To help us narrow down whether it’s a server configuration issue, device specific issue, or an issue with the app please try the following steps and include the results in your support request:

**Connect to our community workspace**

1. Create an account at https://community.mattermost.com.
2. Delete your mobile application and reinstall it.
3. In your mobile app, enter the server URL https://community.mattermost.com and then your login credentials to see if the connection is working.

**Connect with another device**

- If you have another mobile device available, try connecting with that to see if your issue still reproduces.
- If you don’t have another device available, check with other teammates to see if they are having the same issue.
