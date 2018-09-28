..  _troubleshooting:

Troubleshooting
===============

This document summarizes common troubleshooting issues and techinques.

.. contents::
    :backlinks: top

Important notes
---------------

**DO NOT Manipulate the Mattermost Database**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Do not manipulate the database directly. Mattermost is designed to stop working if data integrity is compromised. 
- Any manipulation of the database must be done using the built in command-line tools

Troubleshooting Basics
----------------------

If you're new to Mattermost or troubleshooting consider the following steps:

- Start simple with the step-by-step install guides for your operating system.

- Check the logs (``mattermost.log`` and NGINX logs) for errors.

- Search error messages online (Google, Yahoo, Bing, or your favorite search engine), existing solutions can often work.

- For more help, create a troubleshooting report at `Troubleshooting Forum <https://forum.mattermost.org/t/how-to-use-the-troubleshooting-forum/150>`__.

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

User statues get stuck on away or offline status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you notice more than one user being stuck at an Away or Offline status, try one of the following steps:

1. If you are using an NGINX proxy, configure IP Hash load balancing to determine what server should be selected for the next request (based on the client’s IP address) `as described here <http://nginx.org/en/docs/http/load_balancing.html>`_.

2. If you are using an AWS Application Load Balancer (ALB), enable Sticky Sessions feature in Amazon EC2’s Elastic Load Balancing `as described here <https://aws.amazon.com/blogs/aws/new-elastic-load-balancing-feature-sticky-sessions/>`_.

If neither of the above steps help resolve the issue, please open a new topic `in the Mattermost forums <https://forum.mattermost.org/>`_ for further troubleshooting.

System Console settings revert to previous values after saving
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you try to save a System Console page and notice that the settings revert to previous values, your ``config.json`` file may have a permissions issue.

Check that the ``config.json`` file is owned by the same user as the process that runs the Mattermost server. If not, change the owner to be the mattermost user and restart the server.

YouTube videos show a "Video not found" preview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. First, make sure the YouTube video exists by pasting a link to the video into your browser's address bar.
2. If you are using the Mattermost Desktop App, please ensure you have installed version 3.5.0 or later.
3. If you have specified `a Google API key <https://docs.mattermost.com/administration/config-settings.html#google-api-key>`_ to enable the display of titles for embedded YouTube video previews, regenerate the key.

Mattermost can't connect to LDAP/AD server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

LDAP and Active Directory troubleshooting can be found on `this page. <https://docs.mattermost.com/deployment/sso-ldap.html#troubleshooting-faq>`_

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

1. Upgrade to a Mattermost server v3.8.0 or later, which adds `WebSocket CORS support <https://github.com/mattermost/mattermost-server/pull/5667>`_.
2. Follow the installation guide to configure `NGINX as a proxy for Mattermost server <https://docs.mattermost.com/install/install-ubuntu-1604.html#configuring-nginx-as-a-proxy-for-mattermost-server>`_.
3. If you're doing reverse proxy with IIS, upgrade to IIS 8.0 or later and enable WebSockets. For more information, see `IIS 8.0 WebSocket Protocol Support <https://www.iis.net/learn/get-started/whats-new-in-iis-8/iis-80-websocket-protocol-support>`_.

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

If you are using NGINX as a proxy, set the ``ssl_ecdh_curve`` directive in your site configuration file (for example, in ``/etc/nginx/sites-available/mattermost``), to a value that is supported by both client and server. Suggested values for varying levels of compatibility can be found at `Mozilla's Security/Server Side TLS <https://wiki.mozilla.org/Security/Server_Side_TLS>`_ page.

As security and encryption standards often change rapidly, it is best to check for up-to-date information. However, the suggested value as of January 2018, is to use the curves: prime256v1, secp384r1, secp521r1.

For NGINX, this would translate to ``ssl_ecdh_curve prime256v1:secp384r1:secp521r1;``

*Note: Setting multiple curves requires nginx 1.11.0, if you can only set one curve, the most compatible is prime256v1.*
