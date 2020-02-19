..  _troubleshooting:

This document summarizes common troubleshooting issues and techniques.

Depending on the type of error or problem you're experiencing, refer to the sections below for troubleshooting guidance. If you're a new user, it might help to go over the installation steps again to confirm the process. Alternatively, the `Troubleshooting forum <https://forum.mattermost.org/c/trouble-shoot>`__ might be helpful as someone may have experienced the same error in the past.

If you're an Enterprise Edition subscriber, you may open a support ticket in the `Enterprise Edition Support portal <https://mattermost.zendesk.com/hc/en-us/requests/new>`_.


Important Notes
---------------

- Do not manipulate the Mattermost database directly. Mattermost is designed to stop working if data integrity is compromised.
- Any manipulation of the database must be done using the built in command-line tools.
- Start simple with the step-by-step install guides for your operating system.


General Troubleshooting
-----------------------
Some of these suggestions can be done directly, and others may need consultation from your network administrator.

- Take a look at the logs (``mattermost.log`` and NGINX logs) for errors.
- You can also search the error messages online - existing solutions can often be applied.
- Open **System Console > General > Logging** and set File Log Level to **DEBUG**. Make sure to revert to **INFO** after troubleshooting to save disk space.

Put together a timeline to eliminate events prior to the error/problem occurring. For example, if you recently reconfigured your firewall and are now having connection issues it might be worth reviewing the settings or rolling back to see whether that resolves the problem.

- If the problem occurred subsequent to some period of normal operation, did anything change in the environment?
    - Was the client, host, or server upgraded?
    - Was an operating system update applied?
    - Did the network environment change? For example, was a server moved or a domain migrated?
    - Did the system (client or server) recently fail or abnormally terminate?
- How many users are impacted?
    - Is this problem affecting one, some, or all users?
    - Is the problem occurring only for a user who was recently added to the environment, such as a new employee?
    - Do differences exist between the users who are affected and the users who are not affected?

These questions are quite general but should help guide you to a point where the root cause of the problem can be found. If, after following these guidelines, you're still facing the issue, visit the `Troubleshooting Forum <https://forum.mattermost.org/t/how-to-use-the-troubleshooting-forum/150>`__.

Administration Issues
-----------------------------

Lost System Administrator Account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  To reset the account, run from the command line:
   ``./mattermost -assign_role -team_name="yourteam" -email="you@example.com" -role="system_admin"``.
-  Log out and back in to apply the change.

Switching System Administrator Account to Single Sign-on (SSO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When Mattermost is initially set up, the first account created becomes the System Administrator account. This account will typically use email authentication to sign-in, since it is usually created before other sign-in methods are configured.

After setting up SSO authentication, it is common for the System Administrator to want to turn off email sign-in so users will only have SSO as a sign-in option.

Before doing this, the System Administrator needs to change their sign-in method to SSO by doing the following:

1. Sign in to Mattermost using an email and password.
2. Go to **Account Settings > Security > Sign-in Method**.
3. Click the "Switch" button to select a sign-in method and complete the process provided.

The System Administrator can now turn off email sign-in and still access their account. To avoid locking other existing users out of their accounts, it is recommended the System Administrator ask them to switch authentication methods as well.

Locked Out of System Administrator Account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the System Administrator is locked out of the system during SAML configuration process, they can set an existing account to System Administrator using `a command line tool <https://docs.mattermost.com/deployment/on-boarding.html#common-tasks>`__.

If email sign-in was turned off before the System Administrator switched sign-in methods, sign up for a new account and promote it to System Administrator from the command line:

1. Sign in to the server Mattermost is running on via ``ssh``.
2. Go to the directory of the Mattermost application. If you've followed our setup process this is ``/opt/mattermost``.
3. Run

  .. code-block:: none

    $ sudo ./mattermost roles system_admin {username}

4. Replace ``{username}`` with the name of the user you'd like to promote to an admin.

SAML Issues
-------------------

Unable to Switch to SAML Authentication Successfully
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, ensure you have installed the `XML Security Library <https://www.aleksey.com/xmlsec/download.html>`__ on your Mattermost instance and that **it is available in your** PATH.

Second, ensure you have completed each step of the SAML configuration.

System Administrator locks themselves out of the system
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the System Administrator is locked out of the system during SAML configuration process, they can set an existing account to System Administrator using `a command line tool <https://docs.mattermost.com/deployment/on-boarding.html#common-tasks>`__.

``An account with that username already exists. Please contact your Administrator.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This usually means an existing account has another authentication method enabled. If so, the user should sign in using that method (such as email and password), then change their sign-in method to SAML via **Account Settings > Security > Sign-in method**.

This error message can also be received if the `Username Attribute` of their SAML credentials doesn't match the username of their Mattermost account. If so, the user can update the attribute at their identity provider (for instance, back to the old value if it had been previously updated).

``An account with that email already exists. Please contact your Administrator.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This usually means an existing account has another authentication method enabled. If so, the user should sign in using that method (such as email and password), then change their sign-in method to SAML via **Account Settings > Security > Sign-in method**.

This error message can also be received if the ``Email Attribute`` of their SAML credentials doesn't match the email address of their Mattermost account. If so, the user can update the attribute at their identity provider (for instance, back to the old value if it had been previously updated).

``SAML login was unsuccessful because one of the attributes is incorrect. Please contact your System Administrator.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Confirm all attributes, including `Email Attribute` and `Username Attribute`, are correct in both the Identity Provider configuration and in **System Console > SAML**.


``An error occurred while building Service Provider Metadata.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error indicates that the installation does not have an Enterprise license. The error message you receive will look similar to this:

.. code-block:: sh

     ERRO[2019-12-23T10:04:33.5074-07:00] An error occurred while building Service Provider Metadata.  caller="mlog/log.go:175" err_details="err=Your license does not support SAML authentication." err_where=GetSamlMetadata http_code=501 ip_addr="::1" method=GET path=/api/v4/saml/metadata request_id=fbtsbxzb33f67gn6yuy73asxjw user_id=

To resolve the issue, install an Enterprise License and restart the process.


``SAML 2.0 is not configured or supported on this server.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The error indicates that the installation is using the Mattermost Team Edition. The error message you receive will look similar to this:

.. code-block:: sh

   ERRO[2019-12-23T10:12:56.5884001-07:00] An error occurred while building Service Provider Metadata.  caller="mlog/log.go:175" err_details="err=SAML 2.0 is not configured or supported on this server." err_where=GetSamlMetadata http_code=501 ip_addr="::1" method=GET path=/api/v4/saml/metadata request_id=1c7jrw3fzbggpe9rs83r5ge5fw user_id=

To resolve the issue, install Enterprise Edition and restart the process.

``An error occurred while initiating the request to the Identity Provider. Please contact your System Administrator``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error message can have multiple causes. The log messages provide more information about the root cause and are provided below, along with a suggested fix.

**Issue: Missing a Certificate File.**

.. code-block:: sh

   ERRO[2019-12-20T17:20:24.3999581-07:00] Identity Provider Public Certificate File was not found. Please contact your System Administrator.  caller="mlog/log.go:175" err_details= err_where=SamlInterfaceImpl.BuildRequest http_code=500 ip_addr="::1" method=GET path=/login/sso/saml request_id=tm9ywzxcbj88dypkhjgg8hideo user_id=

Install the Identity Provider Certificate and restart the process.

**Issue: Missing Service Provider Private Key**

.. code-block:: sh

   ERRO[2019-12-23T08:51:28.423397-07:00] An error occurred while configuring SAML Service Provider  caller="app/enterprise.go:154" error="saml-public.crt: cannot read: failed to get config file saml-private.key: failed to read file from .../mattermost-server/config/saml-private.key: open .../mattermost-server/config/saml-private.key: no such file or directory"

Install the Service Provider Private Key and restart the process.

**Issue: Missing Service Provider Public Certificate**

.. code-block:: sh

   ERRO[2019-12-23T09:06:27.654774-07:00] An error occurred while configuring SAML Service Provider  caller="app/enterprise.go:154" error="saml-public.crt: cannot read: failed to get config file saml-public.crt: failed to read file from .../mattermost-server/config/saml-public.crt: open .../mattermost-server/config/saml-public.crt: no such file or directory"

Install the Service Provider Public Certificate and restart the process.

.. note::

   If making adjustments for these errors within System Console, no restart is required. However, if making configuration changes outside System Console, such as moving certificate files to the corrrect path, a server restart is required.

``SAML login was unsuccessful because one of the attributes is incorrect. Please contact your System Administrator.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error indicates that a required attribute was missing from the assertion received from the Idp provider, check log file for which attribute is missing.

.. code-block:: sh

   ERRO[2019-12-09T21:23:24.506631-07:00] SAML login was unsuccessful because one of the attributes is incorrect. Please contact your System Administrator.  caller="mlog/log.go:174" err_details="id attribute is missing" err_where=SamlInterfaceLibImpl.DoLogin http_code=302 ip_addr="::1" method=POST path=/login/sso/saml request_id=5bb6uchhm38kxys6rqm8i5p4ow user_id=

To address the issue, update settings on Idp to include the required attribute.

.. note::

   Turning on debug logging will allow the assertion to be logged.


``SAML login was unsuccessful because encryption is not enabled. Please contact your System Administrator.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error indicates a mismatch between SP Provider (Mattermost) configuration and Idp Provider configuration. The SP
Provider SAML is configured to expect an unencrypted SAML assertion but the assertion received was encrypted.

.. code-block:: sh

   ERRO[2019-12-23T10:53:42.332484-07:00] SAML login was unsuccessful because encryption is not enabled. Please contact your System Administrator.  caller="mlog/log.go:175" err_details= err_where=SamlInterfaceImpl.DoLogin http_code=302 ip_addr="::1" method=POST path=/login/sso/saml request_id=63s9b8i7u38nzfeuqyzdbank7h user_id=

To address this issue, turn on encryption and restart the process.


``SAML login was unsuccessful as the Identity Provider response is not encrypted. Please contact your System Administrator.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error indicates a mismatch between SP Provider (Mattermost) configuration and Idp Provider configuration. The SP
Provider SAML is configured to expect an unencrypted SAML Assertion but the assertion received was encrypted.

.. code-block:: sh

   ERRO[2019-12-23T10:59:13.486763-07:00] SAML login was unsuccessful as the Identity Provider response is not encrypted. Please contact your System Administrator.  caller="mlog/log.go:175" err_details= err_where=SamlInterfaceImpl.DoLogin http_code=302 ip_addr="::1" method=POST path=/login/sso/saml request_id=j61b8mqpc3n97pgqqeuxupx93y user_id=

To address this issue, turn on encryption and restart the process.

``An error occurred while parsing the response from the Identity Provider. Please contact your System Administrator.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error is caused by a malformed response or certificate issue, see log file for more information.

.. code-block:: sh

   ERRO[2019-12-23T11:22:16.733242-07:00] An error occurred while parsing the response from the Identity Provider. Please contact your System Administrator.  caller="mlog/log.go:175" err_details="err=illegal base64 data at input byte 15012" err_where=SamlInterfaceImpl.DoLogin http_code=302 ip_addr="::1" method=POST path=/login/sso/saml request_id=uhnbq1objfyqpyqct3sy3fch9y user_id=

``An error occurred while encoding the request for the Identity Provider. Please contact your System Administrator.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error indicates an issue with ``xmlsec1``; either ``xmlsec1`` is not installed or the version of ``xmlsec1`` in use does not accept self-signed certificate.

.. code-block:: sh

   ERRO[2019-12-23T12:42:04.389431-07:00] An error occurred while encoding the request for the Identity Provider. Please contact your System Administrator.  caller="mlog/log.go:175" err_details= err_where=SamlInterfaceImpl.BuildRequest http_code=500 ip_addr="::1" method=GET path=/login/sso/saml request_id=mg4mdc78q3r798y5ierdz5qqdc user_id=

``SAML login was unsuccessful because an error occurred while decrypting the response from the Identity Provider. Please contact your System Administrator``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error indicates an issue with ``xmlsec1``; either ``xmlsec1`` is not installed or the version of ``xmlsec1`` in use does not accept self-signed certificates.

.. code-block:: sh

   ERRO[2019-12-23T12:45:45.041627-07:00] SAML login was unsuccessful because an error occurred while decrypting the response from the Identity Provider. Please contact your System Administrator.  caller="mlog/log.go:175" err_details="err=failed to decrypt xml: error invoking xmlsec1: : exec: \"xmlsec1\": executable file not found in $PATH" err_where=SamlInterfaceImpl.DoLogin http_code=302 ip_addr="::1" method=POST path=/login/sso/saml request_id=i7d7kc4hk3ymzneetdbuafz9ca user_id=

``An error occurred while validating the response from the Identity Provider. Please contact your System Administrator.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error message applies to various validation issues. The log message provides more information about the cause of the issue.

.. code-block:: sh

   ERRO[2019-12-23T13:09:49.171975-07:00] An error occurred while validating the response from the Identity Provider. Please contact your System Administrator.  caller="mlog/log.go:175" err_details="err=unsupported SAML Version" err_where=SamlInterfaceImpl.DoLogin http_code=302 ip_addr="::1" method=POST path=/login/sso/saml request_id=5omhhgei8jr68jba3j4tiwo48c user_id=

**Parameters**

- ``unsupported SAML Version``: The assertion xml contains the wrong SAML version, 2.0 supported.

- ``missing ID attribute on SAML Response``: The assertion did not contain an ID attribute. Invalid XML received.

- ``no signature``: No signature, but signature validation required.

- ``invalid signature reference uri``: Invalid signature tag. Invalid XML received.

- ``destination mismatch expected: x not y``: ``AssertionConsumerServiceURL`` did not match expected.

- ``too soon`` or ``too late``: Assertion ``NotOnOrAfter`` or ``NotBefore`` attribute outside current time.


Deployment and Clustering
-------------------------

Red Server Status
~~~~~~~~~~~~~~~~~

When high availability is enabled, the System Console displays the server status as red or green, indicating if the servers are communicating correctly with the cluster. The servers use inter-node communication to ping the other machines in the cluster, and once a ping is established the servers exchange information, such as server version and configuration files.

A server status of red can occur for the following reasons:

- **Configuration file mismatch**: Mattermost will still attempt the inter-node communication, but the System Console will show a red status for the server since the high availability feature assumes the same configuration file to function properly.
- **Server version mismatch**: Mattermost will still attempt the inter-node communication, but the System Console will show a red status for the server since the high availability feature assumes the same version of Mattermost is installed on each server in the cluster. It is recommended to use the `latest version of Mattermost <https://www.mattermost.org/download/>`__ on all servers. Follow the upgrade procedure in :doc:`../administration/upgrade` for any server that needs to be upgraded.
- **Server is down**: If an inter-node communication fails to send a message it makes another attempt in 15 seconds. If the second attempt fails, the server is assumed to be down. An error message is written to the logs and the System Console shows a status of red for that server. The inter-node communication continues to ping down the server in 15-second intervals. When the server comes back up, any new messages are sent to it.

WebSocket Disconnect
~~~~~~~~~~~~~~~~~

When a client WebSocket receives a disconnect it will automatically attempt to re-establish a connection every three seconds with a backoff. After the connection is established, the client attempts to receive any messages that were sent while it was disconnected.

App Refreshes Continuously
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When configuration settings are modified through the System Console, the client refreshes every time a user connects to a different app server. This occurs because the servers have different ``config.json`` files in a high availability cluster.

Modify configuration settings directly through ``config.json`` `following these steps <https://docs.mattermost.com/deployment/cluster.html#updating-configuration-changes-while-operating-continuously>`__.

Messages Do Not Post Until After Reloading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When running in high availability mode, make sure all Mattermost application servers are running the same version of Mattermost. If they are running different versions, it can lead to a state where the lower version app server cannot handle a request and the request will not be sent until the frontend application is refreshed and sent to a server with a valid Mattermost version. Symptoms to look for include requests failing seemingly at random or a single application server having a drastic rise in goroutines and API errors.



Server Administration
---------------------

``Please check connection, Mattermost unreachable. If issue persists, ask administrator to check WebSocket port.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Message appears in blue bar on team site.
-  To check the websocket connection, open the developer console in your browser and view the **Network** panel. If the WebSocket is not connecting properly, you will see a pending WebSocket connection show up in the list. The screenshot below shows an example from Chrome.
.. image:: ../images/websocket.png
-  **If this issue is reported repeatedly**, the most likely cause is a proxy being misconfigured somewhere in your infrastructure, and possibly stripping headers off of WebSocket communications.

-  Mattermost clients connect to the server using multiple protocols, ``https`` to enable general site functionality, and ``wss`` for real-time updates. This error message appears when the ``https`` connection is working, but the ``wss`` connection has issues, most commonly having headers stripped off by a firewall or proxy that is either misconfigure or which does not support secure WebSockets.

**Note:** If your ``https`` connection is working and ``wss`` is not, and you dismiss the blue bar message, your team site will render, but will not support real time communications (you will need to refresh to see updates and the system is effectively "broken").

**Solution:**

      1. Follow the `installation guide to set up your WebSocket port properly <https://docs.mattermost.com/install/install-ubuntu-1604.html#installing-nginx-server>`__.
      2. Speak with the owner of any other proxies between your device and the Mattermost server to ensure ``wss`` connections are passing through without issue.

If this issue is reported rarely, in some cases the issue comes from *intermittent* internet connectivity, where the initial load works, but the device then becomes disconnected from the internet and real time updates over the ``wss`` connection fail repeatedly and the error is displayed to check if the ``wss`` connection were misconfigured.

If only a small number of users have this issue, it could be from intermittent internet access, if almost every user has this issue, it's likely from a misconfiguration of the ``wss`` connection.

``Cannot connect to the server. Please check your server URL and internet connection.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error may appear on some devices when trying to connect to a server that is using an SSL curve that is not supported by the client device.

**Solution:**

If you are using NGINX as a proxy, set the ``ssl_ecdh_curve`` directive in your site configuration file (for example, in ``/etc/nginx/sites-available/mattermost``), to a value that is supported by both client and server. Suggested values for varying levels of compatibility can be found at `Mozilla's Security/Server Side TLS <https://wiki.mozilla.org/Security/Server_Side_TLS>`__ page.

As security and encryption standards often change rapidly, it is best to check for up-to-date information. However, the suggested value as of January 2018 is to use the curves: prime256v1, secp384r1, secp521r1.

For NGINX, this would translate to ``ssl_ecdh_curve prime256v1:secp384r1:secp521r1;``.

**Note:** Setting multiple curves requires nginx 1.11.0, if you can only set one curve, the most compatible is prime256v1.

``x509: certificate signed by unknown authority``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error may appear in server logs when attempting to sign-up when using self-signed certificates to setup SSL, which is not yet supported by Mattermost.

**Solution:**

Set up a load balancer like NGINX `per production install guide <https://docs.mattermost.com/install/install-ubuntu-1604.html#configuring-nginx-with-ssl-and-http-2>`__. The core team is looking into allowing self-signed certificates in the future.

As a work around, in **System Console** > **Security** > **Connections** set ``Enable Insecure Outgoing Connections`` to ``true``.

This will allow insecure TLS connections, but be careful in doing so as it also opens your Mattermost site to man-in-the-middle attacks.

``panic: runtime error: invalid memory address or nil pointer dereference``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error can occur if you have manually manipulated the Mattermost database, typically with deletions. Mattermost is designed to serve as a searchable archive, and manual manipulation of the database elements compromises integrity and may prevent upgrade.

**Solution:**

Restore from database backup created prior to manual database updates, or reinstall the system.

``We couldn't find an existing account matching your email address for this team. This team may require an invite from the team owner to join.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error appears when a user tries to sign in, and Mattermost can't find an account matching the credentials they entered.

**Solution:**

1. If you're signing in with email and have previously created an account:

Check that you are using the correct email address. If you can't remember what email address was used, contact the System Administrator for assistance.

2. If you haven't signed up for an account on this team yet:

Click the link at the bottom of the sign-in page that says “Don't have an account? Create one now” to create an account. If the link is not available, contact a Team or System Administrator for an invitation.

3. If your account uses a different sign-in method (for example, the account was created with email but the user is trying to use SSO to sign in):

   - Check the sign-in page.
   - If the sign-in method the account was created with is available, use that to sign in.

      -  **Note:** You may then switch authentication methods from **Account Settings > Security > Sign-in Method**.

   - If the sign-in method is not available, contact the System Administrator.

      -  This can happen if the site was originally set up to allow an
         account to be created using either GitLab or email, but then the
         System Administrator turned one of the options off.
      -  The System Administrator can fix this issue by:

         1. Turning the sign-in option back on.
         2. Asking the user to switch sign-in methods before turning the
            sign-in option off.

``Failed to upgrade websocket connection``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error can occur if you're using multiple URLs to reach Mattermost via proxy forwarding.

**Solution:**

1. Upgrade to a Mattermost server v3.8.0 or later, which adds `WebSocket CORS support <https://github.com/mattermost/mattermost-server/pull/5667>`__.
2. Follow the installation guide to configure `NGINX as a proxy for Mattermost server <https://docs.mattermost.com/install/install-ubuntu-1604.html#configuring-nginx-as-a-proxy-for-mattermost-server>`__.
3. If you're doing reverse proxy with IIS, upgrade to IIS 8.0 or later and enable WebSockets. For more information, see `IIS 8.0 WebSocket Protocol Support <https://www.iis.net/learn/get-started/whats-new-in-iis-8/iis-80-websocket-protocol-support>`__.

``Websocket closed`` or ``Websocket re-established connection``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This alert can appear every few seconds in the desktop application or web browser connected to Mattermost.

**Solution:**

If you are using an Amazon ELB check that ``Idle Timeout`` is set to ``120s``, if it's significantly lower it will cause an undesireable websocket disconnections.

If you are using NGINX, make sure you follow the `Mattermost configuration instructions <https://docs.mattermost.com/install/config-proxy-nginx.html>`__ for setting the  ``proxy_read_timeout``.


``context deadline exceeded``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This error appears when a request from Mattermost to another system, such as an Elasticsearch server, experiences a connection timeout.

**Solution:**

1. Verify that the Mattermost server is able to connect to the system referenced in the error message.
2. Increase the request timeout value for that integration in the Mattermost ``config.json`` file.
3. Ensure the target system is behaving properly and has sufficient resources to handle current load.

Settings
--------

User Statuses get Stuck on "Away" or "Offline" Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you notice more than one user being stuck at an Away or Offline status, try one of the following steps:

1. If you are using an NGINX proxy, configure IP Hash load balancing to determine what server should be selected for the next request (based on the client’s IP address) `as described here <http://nginx.org/en/docs/http/load_balancing.html>`__.

2. If you are using an AWS Application Load Balancer (ALB), enable Sticky Sessions feature in Amazon EC2’s Elastic Load Balancing `as described here <https://aws.amazon.com/blogs/aws/new-elastic-load-balancing-feature-sticky-sessions/>`__.

If neither of the above steps help resolve the issue, please open a new topic `in the Mattermost forums <https://forum.mattermost.org/>`__ for further troubleshooting.

System Console Settings Revert to Previous Values after Saving
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you try to save a System Console page and notice that the settings revert to previous values, your ``config.json`` file may have a permissions issue.

Check that the ``config.json`` file is owned by the same user as the process that runs the Mattermost server. If not, change the owner to be the Mattermost user and restart the server.

Mattermost Can't Connect to LDAP/AD Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LDAP and Active Directory troubleshooting can be found on `this page. <https://docs.mattermost.com/deployment/sso-ldap.html#troubleshooting-faq>`__

Mobile
-------

Login with ADFS/Office365 is Not Working
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In line with Microsoft guidance we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_.

The “Connecting…” Bar Doesn't Clear
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your app is working properly, you should see a grey “Connecting…” bar that clears or says “Connected” after the app reconnects.

If you are seeing this message all the time, and your internet connection seems fine, ask your server administrator whether the server uses NGINX or another webserver as a reverse proxy. If so, they should check that it is configured correctly for `supporting the websocket connection for APIv4 endpoints <https://docs.mattermost.com/install/install-ubuntu-1604.html#configuring-nginx-as-a-proxy-for-mattermost-server>`__.

I’m Not Receiving Push Notifications on my Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you did not receive a push notification when :doc:`testing push notifications <mobile-testing-notifications>`, use the following procedure to troubleshoot:

1. Under **System Console > Environment > Logging > File Log Level** (or **System Console > General > Logging > File Log Level** in versions prior to 5.12) select **DEBUG** in order to watch for push notifications in the server log.

2. Delete and reinstall your mobile application.

3. Sign in with "Account A" and **confirm you want to receive push notifications** when prompted by the mobile app.

4. On desktop, go to **Account Settings > Security > View and Logout of Active Sessions** and check that there is a session for the native mobile app matching your login time.

5. Repeat the procedure for :doc:`testing push notifications <mobile-testing-notifications>`.

6. If no push notification appears go to **System Console > Logs** and click **Reload**. Look at the bottom of the logs for a message similar to:

``[2016/04/21 03:16:44 UTC] [DEBG] Sending push notification to 608xyz0... wi msg of '@accountb: Hello'``

  - If the log message appears, it means a message was sent to the HPNS server and was not received by your mobile application. Please contact support@mattermost.com with the subject "HPNS issue on Step 8" for help from the commercial support team.
  - If the log message does not appear, it means no mobile push notification was sent to “Account A”. Please repeat the process, starting at step 2, and double check each step.

7. **IMPORTANT:** After your issue is resolved, go to **System Console > Environment > Logging > File Log Level** (or **System Console > General > Logging > File Log Level** in versions prior to 5.12) and select **ERROR** to switch your logging detail level to Errors Only, instead of **DEBUG**, in order to conserve disk space.

All Outbound Connections go Through a Proxy. How Can I Connect to the Mattermost Hosted Push Notification Service?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can set up an internal server to proxy the connection out of their network to the Mattermost Hosted Push Notification Service (HPNS) by following the steps below:

1. Make sure your proxy server is properly configured to support SSL. Confirm it works by checking the URL at https://www.digicert.com/help/.
2. Set up a proxy to forward requests to ``https://push.mattermost.com``.
3. In Mattermost set **System Console > Environment > Push Notification Server > Enable Push Notifications** (or **System Console > Notification Settings > Mobile Push > Enable Push Notifications** in versions prior to 5.12) to **Manually enter Push Notification Service location**.
4. Enter the URL of your proxy in the **Push Notification Server** field.

**Note:** Depending on how your proxy is configured you may need to add a port number and create a URL like ``https://push.internalproxy.com:8000`` mapped to ``https://push.mattermost.com``.

``Cannot connect to the server. Please check your server URL and internet connection.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, confirm that your server URL has no typos and that it includes ``http://`` or ``https://`` according to the server deployment configuration.

If the server URL is correct, there could be an issue with the SSL certificate configuration.

To check your SSL certificate set up, test it by visiting a site such as `SSL Labs <https://www.ssllabs.com/ssltest/index.html>`__. If there’s an error about the missing chain or certificate path, there is likely an intermediate certificate missing that needs to be included.

Please note that the apps cannot connect to servers with self-signed certificates, consider using `Let's Encrypt <https://docs.mattermost.com/install/config-ssl-http2-nginx.html>`__ instead.

Configuration Issues
---------------------

In some cases, the configuration from the product’s website differs from the Mattermost configuration. Review the configuration to ensure it’s aligned with Mattermost.

- See detailed client software requirements for PC, mobile, and email.
- See detailed server software requirements for operating system and database.
- Check which Mattermost server version you're on, and confirm whether it's the latest version.
- Have you made any changes to the default settings in the System Console (or in ``config.json`` file)?
- What device (webapp, desktop app), browser, and operating system (Windows, Mac, etc.) are you using?
- Confirm that the SSL/TLS certificate was installed successfully by entering your Mattermost server URL to Symantec’s online SSL/TLS certificate checker.
- Look for JavaScript errors in the Chrome developer console: Open the Chrome menu in the top-right of the browser window and select **More Tools** > **Developer Tools**.

Integrations
~~~~~~~~~~~~

YouTube Videos Show a "Video not found" Preview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. First, make sure the YouTube video exists by pasting a link to the video into your browser's address bar.
2. If you are using the Mattermost Desktop App, please ensure you have installed version 3.5.0 or later.
3. If you have specified `a Google API key <https://docs.mattermost.com/administration/config-settings.html#google-api-key>`__ to enable the display of titles for embedded YouTube video previews, regenerate the key.

Hitting an Error "Command with a trigger of failed" When Configuring Giphy Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When trying to configure the Giphy integration in Mattermost, you may hit the error "Command with a trigger of <keyword> failed". To solve this, you need to edit your ``config.json`` and configure ``AllowedUntrustedInternalConnections`` to contain the hostname of the webhook.

Mobile
~~~~~

Build Gets Stuck at ``bundleReleaseJsAndAssets``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As a workaround, you can bundle the ``js`` manually first with

.. code-block:: none

  react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res/

and then ignore the gradle task with

.. code-block:: none

  ./gradlew assembleRelease -x bundleReleaseJsAndAssets

No Image Previews Available in The Mobile App
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This can happen if the server running Mattermost has its mime types not set up correctly.
A server running Linux has this file located in ``/etc/mime.types``. This might vary depending on your specific OS and distribution.

Some distributions also ship without ``mailcap`` which can result in missing or incorrectly configured mime types.


None of These Solve my Problem!
------------------------------

To help us narrow down whether it’s a server configuration issue, device specific issue, or an issue with the app, please try the following steps and include the results in your support request or `Troubleshooting forum <https://forum.mattermost.org/c/trouble-shoot>`__ post.

**Connect to another server**

1. Create an account at https://demo.mattermost.com.
2. Erase your mobile application and reinstall it.
3. In your mobile app, enter the server URL https://demo.mattermost.com and then your login credentials to test whether the connection is working.

**Connect with another device**

- If you have another mobile device available, try connecting with that to see if your issue still reproduces.
- If you don’t have another device available, check with other teammates to see if they are having the same issue.
