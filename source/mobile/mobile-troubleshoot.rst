Troubleshooting Mobile Applications
===================================

I keep getting a message "Cannot connect to the server. Please check your server URL and internet connection."
-------------------------------------------------------------------------------------------------------------------

First, confirm that your server URL has no typos and that it includes ``http://`` or ``https://`` according to the server deployment configuration.

If the server URL is correct, there could be an issue with the SSL certificate configuration.

To check your SSL certificate set up, test it by visiting a site such as `SSL Labs <https://www.ssllabs.com/ssltest/index.html>`_. If there’s an error about the missing chain or certificate path, there is likely an intermediate certificate missing that needs to be included.

Please note that the apps cannot connect to servers with self-signed certificates, consider using `Let's Encrypt <https://docs.mattermost.com/install/config-ssl-http2-nginx.html>`_ instead.

Login with ADFS is not working
-------------------------------
Those instances set up for login with ADFS with integrated windows authentication (IWA) should configure `automated fall back to form-based authentication if IWA fails <https://docops.ca.com/ca-single-sign-on/12-7/en/configuring/policy-server-configuration/authentication-schemes/authentication-chaining/configure-iwa-fallback-to-forms-using-authentication-chain>`_. 


I see a “Connecting…” bar that does not go away
-----------------------------------------------

If your app is working properly, you should see a grey “Connecting…” bar that clears or says “Connected” after the app reconnects.

If you are seeing this message all the time, and your internet connection seems fine, ask your server administrator if the server uses NGINX or another webserver as a reverse proxy. If so, they should check that it is configured correctly for `supporting the websocket connection for APIv4 endpoints <https://docs.mattermost.com/install/install-ubuntu-1604.html#configuring-nginx-as-a-proxy-for-mattermost-server>`_.

I’m not receiving push notifications on my device
-------------------------------------------------

Please see our documentation on :doc:`troubleshooting push notifications <mobile-troubleshoot-notifications>`.

All my outbound connections need to go through a proxy. How can I connect to the Mattermost Hosted Push Notification Service?
-----------------------------------------------------------------------------------------------------------------------------

You can set up an internal server to proxy the connection out of their network to the Mattermost Hosted Push Notification Service (HPNS) by following the steps below:

1. Make sure your proxy server is properly configured to support SSL. Confirm it works by checking the URL at https://www.digicert.com/help/.
2. Setup a proxy to forward requests to ``https://push.mattermost.com``.
3. In Mattermost set **System Console** > **Notification Settings** > **Mobile Push** > **Enable Push Notifications** to "Manually enter Push Notification Service location"
4. Enter the URL of your proxy in the **Push Notification Server** field.

.. Note:: Depending on how your proxy is configured you may need to add a port number and create a URL like ``https://push.internalproxy.com:8000`` mapped to ``https://push.mattermost.com``

Build gets stuck at ``bundleReleaseJsAndAssets``
--------------------------------------------------------------------------------

As a workaround, you can bundle the ``js`` manually first with

.. code-block:: none

  react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res/

and then ignore the gradle task with

.. code-block:: none

  ./gradlew assembleRelease -x bundleReleaseJsAndAssets

None of these solve my problem!
-------------------------------

For more troubleshooting help, `open a new topic in our forums <https://forum.mattermost.org/c/trouble-shoot>`_ with steps to reproduce your issue. If you're an Enterprise Edition subscriber, you can also email subscribers@mattermost.com for support.

To help us narrow down whether it’s a server configuration issue, device specific issue, or an issue with the app, please try the following things and include the results in your support request:

**Connect to another server**

1. Create an account at https://demo.mattermost.com
2. Erase your mobile application and reinstall it
3. In your mobile app, enter the server URL https://demo.mattermost.com and then your login credentials to see if the connection is working

**Connect with another device**

If you have another mobile device available, try connecting with that to see if your issue still reproduces.

If you don’t have another device available, check with other teammates to see if they are having the same issue.
