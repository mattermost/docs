Troubleshooting Mobile Applications
===================================

.. contents::
  :backlinks: top
  :local:

I keep getting a message "Cannot connect to the server. Please check your server URL and internet connection."
--------------------------------------------------------------------------------------------------------------

First, confirm that your server URL has no typos and that it includes ``http://`` or ``https://`` according to the server deployment configuration.

If the server URL is correct, there could be an issue with the SSL certificate configuration.

To check your SSL certificate set up, test it by visiting a site such as `SSL Labs <https://www.ssllabs.com/ssltest/index.html>`__. If there’s an error about the missing chain or certificate path, there is likely an intermediate certificate missing that needs to be included.

Please note that the apps cannot connect to servers with self-signed certificates, consider using `Let's Encrypt <https://docs.mattermost.com/install/config-ssl-http2-nginx.html>`__ instead.

Login with ADFS/Office365 is not working
----------------------------------------

In line with Microsoft guidance we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_. 

I see a “Connecting…” bar that does not go away
-----------------------------------------------

If your app is working properly, you should see a grey “Connecting…” bar that clears or says “Connected” after the app reconnects.

If you are seeing this message all the time, and your internet connection seems fine, ask your server administrator if the server uses NGINX or another webserver as a reverse proxy. If so, they should check that it is configured correctly for `supporting the websocket connection for APIv4 endpoints <https://docs.mattermost.com/install/install-ubuntu-1604.html#configuring-nginx-as-a-proxy-for-mattermost-server>`__.

I’m not receiving push notifications on my device
-------------------------------------------------

Please see our documentation on :doc:`troubleshooting push notifications <mobile-troubleshoot-notifications>`.

All my outbound connections need to go through a proxy. How can I connect to the Mattermost Hosted Push Notification Service?
-----------------------------------------------------------------------------------------------------------------------------

You can set up an internal server to proxy the connection out of their network to the Mattermost Hosted Push Notification Service (HPNS) by following the steps below:

1. Make sure your proxy server is properly configured to support SSL. Confirm it works by checking the URL at https://www.digicert.com/help/.
2. Setup a proxy to forward requests to ``https://push.mattermost.com``.
3. In Mattermost set **System Console** > **Notification Settings** > **Mobile Push** > **Enable Push Notifications** in prior versions or **System Console > Environment > Push Notification Server > Enable Push Notifications** in versions after 5.12 to "Manually enter Push Notification Service location"
4. Enter the URL of your proxy in the **Push Notification Server** field.

.. Note:: Depending on how your proxy is configured you may need to add a port number and create a URL like ``https://push.internalproxy.com:8000`` mapped to ``https://push.mattermost.com``

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

This can happen if the server running Mattermost has its mime types not set up correctly.
A server running Linux has this file located in ``/etc/mime.types``. This might vary depending on your specific OS and distribution.

Some distributions also ship without ``mailcap`` which can result in missing or incorrectly configured mime types.

Messages with emojis aren't being sent from the mobile app
----------------------------------------------------------

This can happen if the server running Mattermost is configured with an incorrect character set. To correct this issue, in the ``config.json`` file under ``SqlSettings``, ensure that the ``DataSource`` key has the ``charset`` configured as ``utf8mb4,utf8``, then restart the Mattermost server.

For example:

.. code-block:: none

  "SqlSettings": {
      "DataSource": "<user:pass>@<servername>/mattermost?charset=utf8mb4,utf8",
      [...]
    }

None of these solve my problem!
-------------------------------

For more troubleshooting help, `open a new topic in our forums <https://forum.mattermost.org/c/trouble-shoot>`__ with steps to reproduce your issue. If you're an Enterprise Edition subscriber, you may open a support ticket in the `Enterprise Edition Support portal <https://mattermost.zendesk.com/hc/en-us/requests/new>`_.

To help us narrow down whether it’s a server configuration issue, device specific issue, or an issue with the app, please try the following things and include the results in your support request:

**Connect to another server**

1. Create an account at https://demo.mattermost.com
2. Erase your mobile application and reinstall it
3. In your mobile app, enter the server URL https://demo.mattermost.com and then your login credentials to see if the connection is working

**Connect with another device**

If you have another mobile device available, try connecting with that to see if your issue still reproduces.

If you don’t have another device available, check with other teammates to see if they are having the same issue.
