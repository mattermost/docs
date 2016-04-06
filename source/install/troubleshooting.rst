..  _troubleshooting:

Troubleshooting
===============

Important notes
---------------

**DO NOT manipulate the Mattermost database**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  In particular, DO NOT delete data from the database, as Mattermost is
   designed to stop working if data integrity has been compromised. The
   system is designed to archive content continously and generally
   assumes data is never deleted.

Troubleshooting Basics
----------------------

If you're new to Mattermost or troubleshooting consider the following
steps:

1. Start simple
   - Use the step-by-step install guides before trying variations.

2. Check the logs for errors
   - In the directory where you installed Mattermost look in the ``mattermost.log`` file for error messages. Also check NGNIX error logs.

3. Web search the error message
   - If you have an error message you don't understand, search the web for the message to try and find an existing article.

4. If you need more help, create a troubleshooting report
   - Please follow the steps at `Troubleshooting Forum <https://forum.mattermost.org/t/how-to-use-the-troubleshooting-forum/150>`__ to share your issue with the community for peer-to-peer support.

Common Issues
-------------

Lost System Administrator account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  If the System Administrator account becomes unavailable, a person
   leaving the organization for example, you can set a new system admin
   from the commandline using
   ``./platform -assign_role -team_name="yourteam" -email="you@example.com" -role="system_admin"``.
-  After assigning the role the user needs to log out and log back in
   before the System Administrator role is applied.

Switching System Administrator Account to SSO Sign-in
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When Mattermost is initially set up, the first account created becomes
the System Administrator account. This account will typically use email
authentication to sign-in, since it is usually created before other
sign-in methods are configured.

After setting up SSO authentication, it is common for the System
Administrator to want to turn off email sign-in so users will only have
SSO as a sign-in option.

Before doing this, the System Administrator needs to change their sign-in method to SSO by doing the following:

1. Sign in to Mattermost using email and password 
2. Go to Account Settings > Security > Sign-in Method 
3. Click the "Switch" button for the sign in method you would like to use, and complete the process for switching sign-in method.

The System Administrator can now turn off email sign-in and still access
their account. (To avoid locking other existing users out of their
accounts, it is recommended the System Administrator ask them to switch
authentication methods as well.)

Locked out of System Administrator account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If email sign-in was turned off before the System Administrator switched
sign-in methods, sign up for a new account and promote it to System
Administrator from the command line.

Mattermost Error Messages
-------------------------

The following is a list of common error messages and solutions:

``Please check connection, Mattermost unreachable. If issue persists, ask administrator to check WebSocket port.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Message appears in blue bar on team site.
-  **If this issue is reported repeatedly**, the most likely cause is a
   proxy being misconfigured somewhere in your infrastructure, and
   possibly stripping headers off of WebSocket communications.

   -  Mattermost clients connect to the server using multiple protocols,
      ``https`` to enable general site functionality, and ``wss`` for
      real-time updates. This error message appears when the ``https``
      connection is working, but the ``wss`` connection has issues, most
      commonly having headers stripped off by a firewall or proxy that is
      either misconfigure or which does not support secure WebSockets.
   -  **Note:** If your ``https`` connection is working and ``wss`` is not,
      and you dismiss the blue bar message, your team site will render, but
      will not support real time communications (you will need to refresh
      to see updates and the system is effectively "broken").
   -  **Solution:**

      1. Follow the `installation guide to set up your WebSocket port
         properly <http://docs.mattermost.com/install/prod-ubuntu.html#set-up-nginx-server>`__.
      2. Speak with the owner of any other proxies between your device and
         the Mattermost server to ensure ``wss`` connections are passing
         through without issue.

-  **If this issue is reported rarely**, in some cases the issue comes
   from *intermittent* internet connectivity, where the initial load
   works, but the device then becomes disconnected from the internet and
   real time updates over the ``wss`` connection fail repeatedly and the
   error is displayed to check if the ``wss`` connection were
   misconfigured.

   -  If only a small number of users have this issue, it could be from
      intermittent internet access, if almost every user has this issue,
      it's likely from a misconfiguration of the ``wss`` connection.

``x509: certificate signed by unknown authority``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  This error may appear in server logs when attempting to sign-up when
   using self-signed certificates to setup SSL, which is not yet
   supported by Mattermost.
-  **Solution:** Set up a load balancer like Ngnix `per production
   install
   guide <http://docs.mattermost.com/install/prod-debian.html#set-up-nginx-with-ssl-recommended>`__.
   The core team is looking into allowing self-signed certificates in
   future. As a work around, in **System Console** > **Service
   Settings** set ``Enable Insecure Outgoing Connections`` to ``true``.
   This will allow insecure TLS connections, but be careful in doing so
   as it also opens your Mattermost site to man-in-the-middle attacks.

``panic: runtime error: invalid memory address or nil pointer dereference``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  This error can occur if you have manually manipulated the Mattermost
   database, typically with deletions. Mattermost is designed to serve
   as a searchable archive, and manual manipulation of the database
   elements compromises integrity and may prevent upgrade.
-  **Solution:** Restore from database backup created prior to manual
   database updates, or reinstall the system.

``We couldn't find an existing account matching your email address for this team. This team may require an invite from the team owner to join.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  This error appears when a user tries to sign in, and Mattermost can't
   find an account matching the credentials they entered.
-  **Solution:**

1. **If you're signing in with email and have previously created an
   account:**

   - Check that you are using the correct email address. If you can't remember what email address was used, contact the System Administrator for assistance.

2. **If you haven't signed up for an account on this team yet:**

   - Click the link at the bottom of the sign-in page that says “Don't have an account? Create one now” to create an account. If the link is not available, contact a Team or System Administrator for an invitation.

3. **If your account uses a different sign-in method** (for example, the
   account was created with email but the user is trying to use SSO to
   sign in):

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

GitLab Mattermost Error Messages
--------------------------------

``We received an unexpected status code from the server (200)``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  If you have upgraded from a pre-released version of GitLab Mattermost
   or if an unforseen issue has arrisen during the `upgrade
   procedure <http://docs.mattermost.com/administration/upgrade.html>`__,
   you may be able to restore Mattermost using the following procedure:
-  ``sudo stop mattermost``, so DB can be dropped
-  ``sudo gitlab-ctl reconfigure``
-  ``sudo -u gitlab-psql /opt/gitlab/embedded/bin/dropdb -h /var/opt/gitlab/postgresql mattermost_production``
-  ``sudo start mattermost``
-  ``sudo gitlab-ctl reconfigure``
-  `Manually set up GitLab
   SSO <http://docs.mattermost.com/deployment/sso-gitlab.html>`__ by
   copying Secret and ID into ``/var/opt/gitlab/mattermost/config.json``
-  ``sudo gitlab-ctl restart``

``Token request failed``
~~~~~~~~~~~~~~~~~~~~~~~~

-  This error can appear in the web browser after attempting to create a
   new team with GitLab SSO enabled
-  **Solutions:**

   1. Check that your SSL settings for the SSO provider match the
      ``http://`` or ``https://`` choice selected in ``config.json`` under
      ``GitLabSettings``
   2. Follow steps 1 to 3 of the manual `GitLab SSO configuration
      procedure <http://docs.mattermost.com/deployment/sso-gitlab.html>`__
      to confirm your ``Secret`` and ``Id`` settings in ``config.json``
      match your GitLab settings, and if they don't, manually update
      ``config.json`` to the correct settings and see if this clears the
      issue.

``The redirect URI included is not valid.``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  This error may be related to SSL configurations in your proxy after a
   GitLab omnibus upgrade from 8.0, which contained the Mattermost beta
   version.
-  **Solution:**

   -  Please check that each step of `the procedure for upgrading
      Mattermost in GitLab 8.0 to GitLab 8.1 was
      completed <http://docs.mattermost.com/integrations/gitlab.html#upgrading-from-gitlab-mattermost-beta>`__.
      Then check upgrades to successive major versions were completed
      using the procedure in the `Upgrade
      Guide <http://docs.mattermost.com/administration/upgrade.html>`__.

``panic: The database schema version of 1.1.0 cannot be upgraded. You must not skip a version``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  This error may appear in your ``/var/log/gitlab/mattermost/current``
   if you're attempting to skip major versions when upgrading GitLab
   Mattermost (e.g. running an upgrade from GitLab 8.2.x to 8.4.x,
   instead of running from 8.2.x to 8.3.x to 8.4.x which is required for
   GitLab Mattermost). To address this:

   1. Run ``platform -version`` to check your version of Mattermost
   2. If your version of the Mattermost binary doesn't match the version
      listed in the database error message, downgrade the version of the
      Mattermost binary you are using by `following the manual upgrade
      steps for
      Mattermost <http://docs.mattermost.com/administration/upgrade.html>`__
      and using the database schema version listed in the error messages
      for the version you select in Step 1) iv).
   3. Once Mattermost is working again, you can use the same upgrade
      procedure to upgrade Mattermost version by version to your current
      GitLab version. After this is done, GitLab automation should
      continue to work for future upgrades, so long as you don't skip
      versions.

``panic: Error decoding config file=/opt/mattermost/config/config.json, err=invalid character '"' after object key:value pair``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Your ``config.json`` is not a well-formed ``.json`` file. Try using a
   `json validator <https://jsonformatter.curiousconcept.com/>`__ to
   find the error.
