Mobile deployment troubleshooting
==================================

I keep getting a message "Cannot connect to the server. Please check your server URL and internet connection."
--------------------------------------------------------------------------------------------------------------

First, confirm that your server URL has no typos and that it includes ``http://`` or ``https://`` according to the server deployment configuration.

If the server URL is correct, there could be an issue with the SSL certificate configuration.

To check your SSL certificate set up, test it by visiting a site such as `SSL Labs <https://www.ssllabs.com/ssltest/index.html>`__. If there’s an error about the missing chain or certificate path, there is likely an intermediate certificate missing that needs to be included.

Please note that the apps cannot connect to servers with self-signed certificates, consider using :ref:`Let's Encrypt <deploy/server/setup-nginx-proxy:configure nginx with ssl and http/2>` instead.

Login with ADFS/Office365 is not working
----------------------------------------

In line with Microsoft guidance we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://learn.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_. 

I see a “Connecting…” bar that does not go away
-----------------------------------------------

If your app is working properly, you should see a grey “Connecting…” bar that clears or says “Connected” after the app reconnects.

If you are seeing this message all the time, and your internet connection seems fine, ask your server administrator if the server uses NGINX or another webserver as a reverse proxy. If so, they should check that it is configured correctly for :ref:`supporting the websocket connection for APIv4 endpoints <deploy/server/setup-nginx-proxy:configure nginx as a proxy for mattermost server>`.

All my outbound connections need to go through a proxy. How can I connect to the Mattermost Hosted Push Notification Service?
-----------------------------------------------------------------------------------------------------------------------------

You can set up an internal server to proxy the connection out of their network to the Mattermost Hosted Push Notification Service (HPNS) by following the steps below:

1. Make sure your proxy server is properly configured to support SSL. Confirm it works by checking the URL at https://www.digicert.com/help/.
2. Setup a proxy to forward requests to ``https://push.mattermost.com``.
3. In Mattermost set **System Console** > **Notification Settings** > **Mobile Push** > **Enable Push Notifications** in prior versions or **System Console > Environment > Push Notification Server > Enable Push Notifications** in versions after 5.12 to "Manually enter Push Notification Service location"
4. Enter the URL of your proxy in the **Push Notification Server** field.

.. Note:: 

  Depending on how your proxy is configured you may need to add a port number and create a URL like ``https://push.internalproxy.com:8000`` mapped to ``https://push.mattermost.com``

Build gets stuck at ``bundleReleaseJsAndAssets``
------------------------------------------------

As a workaround, you can bundle the ``js`` manually first with

.. code-block:: sh

  react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res/

and then ignore the gradle task with

.. code-block:: sh

  ./gradlew assembleRelease -x bundleReleaseJsAndAssets

No image previews available in the mobile app
---------------------------------------------

This can happen if the server running Mattermost has its mime types not set up correctly.
A server running Linux has this file located in ``/etc/mime.types``. This might vary depending on your specific OS and distribution.

Some distributions also ship without ``mailcap`` which can result in missing or incorrectly configured mime types.

Messages with emojis aren't being sent from the Mobile App
----------------------------------------------------------

This can occur if the server running Mattermost is configured with an incorrect character set. To resolve this issue, in the ``config.json`` file under ``SqlSettings``, ensure that the ``DataSource`` key is configured correctly, then restart the Mattermost server. 

For example:

.. code-block:: text

  "SqlSettings": {
      "DataSource": "<user:pass>@<servername>/mattermost?charset=utf8mb4,utf8",
      [...]
    }

See our :ref:`Configuration Settings <configure/environment-configuration-settings:data source>` documentation for details on configuring the connection string to the master database.

Testing mobile push notifications
----------------------------------

Make sure to configure push notifications for your :doc:`pre-built mobile apps </deploy/mobile/mobile-app-deployment>`, or for :doc:`your custom built mobile apps </deploy/mobile/distribute-custom-mobile-apps>`. 

Then use the following instructions to confirm push notifications are working properly.

1. Log in to your mobile app with an account on your Mattermost Server, which we’ll refer to as “Account A”.

2. (iOS) When the app asks whether you wish to receive notifications, **confirm you want to receive notifications**.

  .. image:: ../../images/mobile_push_prompt.png
    :alt: Mattermost prompts you to confirm whether you want to allow mobile push notifications. To test mobile push notifications, you must select Allow.
    :width: 300 px

3. Confirm push notifications are enabled for “Account A”.

  A. Go to the notification settings menu in the mobile app.

  .. image:: ../../images/mobile_notification_settings.gif
    :alt: Access notification settings by selecting your profile picture to access Settings > Notifications.
    :width: 300 px

  B. Check that the mobile push notifications are set to send.

  .. image:: ../../images/mobile_push_send_for.png
    :alt: Select Push Notifications to confirm when mobile push notifications will be sent.
    :width: 300 px

  .. image:: ../../images/mobile_push_send_when.png
    :alt: Specify whether all new messages or only mentions and direct messages send push notifications. 
    :width: 300 px

4. Have “Account A” put the app to background or close the app.

5. Using a browser, log in to “Account B” on the same Mattermost Server.

6. Open a direct message with “Account A”, and send a message.

7. A push notification with the message should appear on the mobile device of “Account A”.

Troubleshooting push notifications
----------------------------------

If you did not receive a push notification when testing push notifications, use the following procedure to troubleshoot:

1. In **System Console > Environment > Logging > File Log Level**, select **DEBUG** in order to watch for push notifications in the server log.

2. Delete your mobile application, and reinstall it.

3. Log in with "Account A" and **confirm you want to receive push notifications** when prompted by the mobile app.

4. Go to **Profile** > **Security** > **View and Logout of Active Sessions** to confirm that there is a session for the native mobile app matching your login time.

5. Retest push notifications.

6. If no push notification displays, go to **System Console** > **Server Logs**, then select **Reload**. Look at the bottom of the logs for a message similar to:

``[2016/04/21 03:16:44 UTC] [DEBG] Sending push notification to 608xyz0... wi msg of '@accountb: Hello'``

  - If the log message displays, it means a message was sent to the HPNS server and was not received by your mobile app. Please `create a support ticket <https://support.mattermost.com/hc/en-us/requests/new>`_ with the subject "HPNS issue" for help from Mattermost's Support team.
  - If the log message does not display, it means no mobile push notification was sent to “Account A”. Please repeat the process starting at step 2 and double-check each step.

.. important::

  To conserve disk space, once your push notification issue is resolved, go to  **System Console > Environment > Logging > File Log Level**, then select **ERROR** to switch your logging detail level from **DEBUG** to **Errors Only**.

If push notifications are not being delivered on the mobile device, confirm that you're logged in to the **Native** mobile app session through **Profile > Security > View and Log Out of Active Sessions**. Otherwise, the `DeviceId` won't get registered in the `Sessions` table and notifications won't be delivered.