..  _troubleshooting:

Troubleshooting
===============

This document summarizes common troubleshooting issues and techniques.

.. contents::
    :backlinks: top

Important Notes
---------------

**DO NOT Manipulate the Mattermost Database**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Do not manipulate the database directly. Mattermost is designed to stop working if data integrity is compromised. 
- Any manipulation of the database must be done using the built in command-line tools
- Start simple with the step-by-step install guides for your operating system.


Troubleshooting Basics
----------------------

Depending on what type of error or problem you're experiencing, refer to the list below for troubleshooting guidance. If you're a new user, it might help to go over the installation steps again to confirm the process. Depending on the type of error you're seeing or issue you're encountering, the Troubleshooting forum might be helpful as someone may have experienced the same error in the past. For more troubleshooting help, `open a new topic in our forums <https://forum.mattermost.org/c/trouble-shoot>`__ with steps to reproduce your issue. If you're an Enterprise Edition subscriber, you can also email subscribers@mattermost.com for support.


General Troubleshooting
-----------------------
 
- Error logs
    - Depending on the error/problem you're experiencing, take a look at the logs (``mattermost.log`` and NGINX logs) for errors. 
    - Search error messages online (Google, Yahoo, Bing, or your favorite search engine), existing solutions can often work.

To increase log level, you can do the following: Set the File Log Level to Debug: Go to System Console > General > Logging and set File Log Level to DEBUG. If you can’t access the System Console find this line in config.json

- What Mattermost server version are you on?
- What is the device (webapp, desktop app) and what is the browser (Windows, Mac, etc.)?
- When did the problem start?
    - It can be helpful to put together a timeline to eliminate events prior to the error/problem occurring. For example, if you recently reconfigured your firewall and are now having connection issues it might be worth reviewing the settings or rolling back to see whether that resolves the problem.  
- If the problem occurred subsequent to some period of normal operation, did anything change in the environment?
    - Was the client, host, or server upgraded?
    - Was an operating system update applied?
    - Did the network environment change? For example, was a server moved or a domain migrated?
    - Did the system (client or server) recently fail or abnormally terminate?
    - Depending on your organization's environment and the problems you're experiencing, contact your network administrator and share the error you're experiencing. 
- How many users are impacted?
    - Is this problem affecting one, some, or all users?
    - Is the problem occurring only for a user who was recently added to the environment, such as a new employee?
    - Do differences exist between the users who are affected and the users who are not affected?

These questions are quite general but should help guide you to a point where the root cause of the problem can be found. If, after following these guidelines, you're still facing the issue, visit the `Troubleshooting Forum <https://forum.mattermost.org/t/how-to-use-the-troubleshooting-forum/150>`__. 

Configuration Issues
---------------------
- In some cases, the configuration from the product’s website differs from the Mattermost configuration. Review the configuration to ensure it’s aligned with Mattermost. 
    - See detailed client software requirements for PC, mobile and email
    - See detailed server software requirements for operating system and database
- Have you made any changes to the default settings in the System Console (or in config.json file)?
- Did you at any point deviate from the step-by-step Mattermost install guides?
What happens if you try Ctrl+R or Command+R?


Certificate Issues
-------------------
- Was SSL/TLS certificate installed successfully (if applicable)? You can confirm it by entering your Mattermost server URL to Symantec’s online SSL/TLS certificate checker.
- Do you see any JavaScript errors in the Chrome developer console? 
    - Open the Chrome menu in the top-right of the browser window and select More Tools > Developer Tools. 

Mobile Troubleshooting
----------------------
Troubleshooting Push Notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you did not receive a push notification when :doc:`testing push notifications <mobile-testing-notifications>`, use the following procedure to troubleshoot:

1. Under **System Console** > **General** > **Logging** > **File Log Level** in prior versions or **System Console > Environment > Logging > File Log Level** in versions after 5.12 select **DEBUG** in order to watch for push notifications in the server log.

2. Delete your mobile application, and install it again.

3. Sign in with "Account A" and **confirm you want to receive push notifications** when prompted by the mobile app.

4. On desktop, go to **Account Settings** > **Security** > **View and Logout of Active Sessions** and check that there is a session for the native mobile app matching your login time.

5. Repeat the procedure for :doc:`testing push notifications <mobile-testing-notifications>`.

6. If no push notification appears go to **System Console** > **Logs** and click **Reload**. Look at the bottom of the logs for a message similar to:

``[2016/04/21 03:16:44 UTC] [DEBG] Sending push notification to 608xyz0... wi msg of '@accountb: Hello'``

  - If the log message appears, it means a message was sent to the HPNS server and was not received by your mobile application. Please contact support@mattermost.com with the subject "HPNS issue on Step 8" for help from the commercial support team.
  - If the log message does not appear, it means no mobile push notification was sent to “Account A”. Please repeat starting at step 2 and double check each step.

7. **IMPORTANT:** After your issue is resolved, go to **System Console** > **General** > **Logging** > **File Log Level** in prior versions or **System Console > Environment > Logging > File Log Level** in versions after 5.12 and select **ERROR** to switch your logging detail level to Errors Only, instead of DEBUG, in order to conserve disk space.

Troubleshooting Mobile Applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I keep getting a message "Cannot connect to the server. Please check your server URL and internet connection."
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, confirm that your server URL has no typos and that it includes ``http://`` or ``https://`` according to the server deployment configuration.

If the server URL is correct, there could be an issue with the SSL certificate configuration.

To check your SSL certificate set up, test it by visiting a site such as `SSL Labs <https://www.ssllabs.com/ssltest/index.html>`__. If there’s an error about the missing chain or certificate path, there is likely an intermediate certificate missing that needs to be included.

Please note that the apps cannot connect to servers with self-signed certificates, consider using `Let's Encrypt <https://docs.mattermost.com/install/config-ssl-http2-nginx.html>`__ instead.

Login with ADFS/Office365 is not working
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In line with Microsoft guidance we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_. 

I see a “Connecting…” bar that does not go away
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your app is working properly, you should see a grey “Connecting…” bar that clears or says “Connected” after the app reconnects.

If you are seeing this message all the time, and your internet connection seems fine, ask your server administrator if the server uses NGINX or another webserver as a reverse proxy. If so, they should check that it is configured correctly for `supporting the websocket connection for APIv4 endpoints <https://docs.mattermost.com/install/install-ubuntu-1604.html#configuring-nginx-as-a-proxy-for-mattermost-server>`__.

I’m not receiving push notifications on my device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see our documentation on :doc:`troubleshooting push notifications <mobile-troubleshoot-notifications>`.

All my outbound connections need to go through a proxy. How can I connect to the Mattermost Hosted Push Notification Service?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can set up an internal server to proxy the connection out of their network to the Mattermost Hosted Push Notification Service (HPNS) by following the steps below:

1. Make sure your proxy server is properly configured to support SSL. Confirm it works by checking the URL at https://www.digicert.com/help/.
2. Setup a proxy to forward requests to ``https://push.mattermost.com``.
3. In Mattermost set **System Console** > **Notification Settings** > **Mobile Push** > **Enable Push Notifications** in prior versions or **System Console > Environment > Push Notification Server > Enable Push Notifications** in versions after 5.12 to "Manually enter Push Notification Service location"
4. Enter the URL of your proxy in the **Push Notification Server** field.

.. Note:: Depending on how your proxy is configured you may need to add a port number and create a URL like ``https://push.internalproxy.com:8000`` mapped to ``https://push.mattermost.com``

Build gets stuck at ``bundleReleaseJsAndAssets``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
As a workaround, you can bundle the ``js`` manually first with

.. code-block:: none

  react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res/

and then ignore the gradle task with

.. code-block:: none

  ./gradlew assembleRelease -x bundleReleaseJsAndAssets

No image previews available in the mobile app
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This can happen if the server running Mattermost has its mime types not set up correctly.
A server running Linux has this file located in ``/etc/mime.types``. This might vary depending on your specific OS and distribution.

Some distributions also ship without ``mailcap`` which can result in missing or incorrectly configured mime types.


None of these solve my problem!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To help us narrow down whether it’s a server configuration issue, device specific issue, or an issue with the app, please try the following things and include the results in your support request:

**Connect to another server**

1. Create an account at https://demo.mattermost.com
2. Erase your mobile application and reinstall it
3. In your mobile app, enter the server URL https://demo.mattermost.com and then your login credentials to see if the connection is working

**Connect with another device**

If you have another mobile device available, try connecting with that to see if your issue still reproduces.

If you don’t have another device available, check with other teammates to see if they are having the same issue.


Common Issues
-------------

Lost System Administrator account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  To reset the account, run from the command line:
   ``./mattermost -assign_role -team_name="yourteam" -email="you@example.com" -role="system_admin"``.
-  Log out and back in for the change to apply.

Switching System Administrator Account to SSO Sign-in
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When Mattermost is initially set up, the first account created becomes the System Administrator account. This account will typically use email authentication to sign-in, since it is usually created before other sign-in methods are configured.

After setting up SSO authentication, it is common for the System Administrator to want to turn off email sign-in so users will only have SSO as a sign-in option.

Before doing this, the System Administrator needs to change their sign-in method to SSO by doing the following:

1. Sign in to Mattermost using email and password 
2. Go to Account Settings > Security > Sign-in Method 
3. Click the "Switch" button for the sign in method you would like to use, and complete the process for switching sign-in method.

The System Administrator can now turn off email sign-in and still access their account. (To avoid locking other existing users out of their accounts, it is recommended the System Administrator ask them to switch authentication methods as well.)

Locked out of System Administrator account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If email sign-in was turned off before the System Administrator switched sign-in methods, sign up for a new account and promote it to System Administrator from the command line: 

1. Sign in to the server Mattermost is running on via ``ssh``.
2. Go to the directory of the Mattermost application. If you've followed our setup process this is ``/opt/mattermost``.
3. Run

  .. code-block:: none

    $ sudo ./mattermost roles system_admin {username}

4. Replace ``{username}`` with the name of the user you'd like to promote to an admin.

User statuses get stuck on away or offline status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you notice more than one user being stuck at an Away or Offline status, try one of the following steps:

1. If you are using an NGINX proxy, configure IP Hash load balancing to determine what server should be selected for the next request (based on the client’s IP address) `as described here <http://nginx.org/en/docs/http/load_balancing.html>`__.

2. If you are using an AWS Application Load Balancer (ALB), enable Sticky Sessions feature in Amazon EC2’s Elastic Load Balancing `as described here <https://aws.amazon.com/blogs/aws/new-elastic-load-balancing-feature-sticky-sessions/>`__.

If neither of the above steps help resolve the issue, please open a new topic `in the Mattermost forums <https://forum.mattermost.org/>`__ for further troubleshooting.

System Console settings revert to previous values after saving
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you try to save a System Console page and notice that the settings revert to previous values, your ``config.json`` file may have a permissions issue.

Check that the ``config.json`` file is owned by the same user as the process that runs the Mattermost server. If not, change the owner to be the mattermost user and restart the server.

YouTube videos show a "Video not found" preview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. First, make sure the YouTube video exists by pasting a link to the video into your browser's address bar.
2. If you are using the Mattermost Desktop App, please ensure you have installed version 3.5.0 or later.
3. If you have specified `a Google API key <https://docs.mattermost.com/administration/config-settings.html#google-api-key>`__ to enable the display of titles for embedded YouTube video previews, regenerate the key.

Mattermost can't connect to LDAP/AD server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LDAP and Active Directory troubleshooting can be found on `this page. <https://docs.mattermost.com/deployment/sso-ldap.html#troubleshooting-faq>`__

Hitting an error "Command with a trigger of failed" when configuring Giphy integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When trying to configure the Giphy integration in Mattermost, you may hit the error "Command with a trigger of <keyword> failed". To solve this, you need to edit your ``config.json`` and configure ``AllowedUntrustedInternalConnections`` to contain the hostname of the webhook.

Mattermost Error Messages
-------------------------

The following is a list of common error messages and solutions:

``Please check connection, Mattermost unreachable. If issue persists, ask administrator to check WebSocket port.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Message appears in blue bar on team site.
-  To check the websocket connection, open the developer console in your browser and view the Network panel. If the websocket is not connecting properly, you will see a pending websocket connection show up in the list. The screenshot below shows an example from Chrome. 
.. image:: ../images/websocket.png
-  **If this issue is reported repeatedly**, the most likely cause is a proxy being misconfigured somewhere in your infrastructure, and possibly stripping headers off of WebSocket communications.

-  Mattermost clients connect to the server using multiple protocols, ``https`` to enable general site functionality, and ``wss`` for real-time updates. This error message appears when the ``https`` connection is working, but the ``wss`` connection has issues, most commonly having headers stripped off by a firewall or proxy that is either misconfigure or which does not support secure WebSockets.

**Note:** If your ``https`` connection is working and ``wss`` is not, and you dismiss the blue bar message, your team site will render, but will not support real time communications (you will need to refresh to see updates and the system is effectively "broken").

**Solution:**

      1. Follow the `installation guide to set up your WebSocket port properly <https://docs.mattermost.com/install/install-ubuntu-1604.html#installing-nginx-server>`__.
      2. Speak with the owner of any other proxies between your device and the Mattermost server to ensure ``wss`` connections are passing through without issue.

If this issue is reported rarely, in some cases the issue comes from *intermittent* internet connectivity, where the initial load works, but the device then becomes disconnected from the internet and real time updates over the ``wss`` connection fail repeatedly and the error is displayed to check if the ``wss`` connection were misconfigured.

If only a small number of users have this issue, it could be from intermittent internet access, if almost every user has this issue, it's likely from a misconfiguration of the ``wss`` connection.

``x509: certificate signed by unknown authority``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error may appear in server logs when attempting to sign-up when using self-signed certificates to setup SSL, which is not yet supported by Mattermost.

**Solution:** Set up a load balancer like NGINX `per production install guide <https://docs.mattermost.com/install/install-ubuntu-1604.html#configuring-nginx-with-ssl-and-http-2>`__. The core team is looking into allowing self-signed certificates in the future. 

As a work around, in **System Console** > **Security** > **Connections** set ``Enable Insecure Outgoing Connections`` to ``true``.
   
This will allow insecure TLS connections, but be careful in doing so as it also opens your Mattermost site to man-in-the-middle attacks.

``panic: runtime error: invalid memory address or nil pointer dereference``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error can occur if you have manually manipulated the Mattermost database, typically with deletions. Mattermost is designed to serve as a searchable archive, and manual manipulation of the database elements compromises integrity and may prevent upgrade.

**Solution:** Restore from database backup created prior to manual database updates, or reinstall the system.

``We couldn't find an existing account matching your email address for this team. This team may require an invite from the team owner to join.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error appears when a user tries to sign in, and Mattermost can't find an account matching the credentials they entered.

**Solution:**

1. If you're signing in with email and have previously created an account:

Check that you are using the correct email address. If you can't remember what email address was used, contact the System Administrator for assistance.

2. If you haven't signed up for an account on this team yet:

Click the link at the bottom of the sign-in page that says “Don't have an account? Create one now” to create an account. If the link is not available, contact a Team or System Administrator for an invitation.

3. If your account uses a different sign-in method (for example, the account was created with email but the user is trying to use SSO to sign in):

   - Check the sign-in page.
   - If the sign-in method the account was created with is available, use that to sign in.

      -  *Note: You may then switch authentication methods from Account
         Settings > Security > Sign-in Method.*

   - If the sign-in method is not available, contact the System Administrator.

      -  This can happen if the site was originally set up to allow an
         account to be created using either GitLab or Email, but then the
         System Administrator turned one of the options off.
      -  The System Administrator can fix this issue by:

         1. Turning the sign-in option back on.
         2. Asking the user to switch sign-in methods before turning the
            sign-in option back off.

``Failed to upgrade websocket connection``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error can occur if you're using multiple URLs to reach Mattermost via proxy forwarding.

**Solution:**

1. Upgrade to a Mattermost server v3.8.0 or later, which adds `WebSocket CORS support <https://github.com/mattermost/mattermost-server/pull/5667>`__.
2. Follow the installation guide to configure `NGINX as a proxy for Mattermost server <https://docs.mattermost.com/install/install-ubuntu-1604.html#configuring-nginx-as-a-proxy-for-mattermost-server>`__.
3. If you're doing reverse proxy with IIS, upgrade to IIS 8.0 or later and enable WebSockets. For more information, see `IIS 8.0 WebSocket Protocol Support <https://www.iis.net/learn/get-started/whats-new-in-iis-8/iis-80-websocket-protocol-support>`__.

``Websocket closed`` or ``Websocket re-established connection``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This alert can appear every few seconds in the Desktop application or web browser connected to Mattermost.

**Solution:**

If you are using an Amazon ELB check that ``Idle Timeout`` is set to ``120s``, if it's significantly lower it will cause an undesireable websocket disconnections. 

If you are using NGINX, make sure you follow the `Mattermost configuration instructions <https://docs.mattermost.com/install/config-proxy-nginx.html>`__ for setting the  ``proxy_read_timeout``. 

``Cannot connect to the server. Please check your server URL and internet connection.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error may appear on some devices when trying to connect to a server that is using an SSL curve that is not supported by the client device.

**Solution:**

If you are using NGINX as a proxy, set the ``ssl_ecdh_curve`` directive in your site configuration file (for example, in ``/etc/nginx/sites-available/mattermost``), to a value that is supported by both client and server. Suggested values for varying levels of compatibility can be found at `Mozilla's Security/Server Side TLS <https://wiki.mozilla.org/Security/Server_Side_TLS>`__ page.

As security and encryption standards often change rapidly, it is best to check for up-to-date information. However, the suggested value as of January 2018, is to use the curves: prime256v1, secp384r1, secp521r1.

For NGINX, this would translate to ``ssl_ecdh_curve prime256v1:secp384r1:secp521r1;``

*Note: Setting multiple curves requires nginx 1.11.0, if you can only set one curve, the most compatible is prime256v1.*

``context deadline exceeded``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error appears when a request from Mattermost to another system, such as an Elasticsearch server, experiences a connection timeout.

**Solution:**

1. Verify that the Mattermost server is able to connect to the system referenced in the error message.
2. Increase the request timeout value for that integration in the Mattermost config file.
3. Ensure the target system is behaving properly and has sufficient resources to handle current load.
