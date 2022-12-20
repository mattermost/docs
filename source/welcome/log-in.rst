Log in to Mattermost
=====================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Mattermost is accessible through a server link. You'll receive the server link from your Mattermost system admin or through an email invitation. You can use that link in a web browser, or as a server connection in the `desktop app </install/desktop-app-install.html>`__, or the `mobile app </deploy/use-prebuilt-mobile-apps.html>`__.

.. tip::
  
  - If you're looking to create a Mattermost workspace, start a `free Cloud trial <https://mattermost.com/get-started/>`_ and then come back to this page.
  - Mattermost Cloud customers can log into their Cloud workspaces from the `Cloud Workspace Connection <https://customers.mattermost.com/cloud/connect-workspace>`__ page by specifying their company or domain name.
  - Can't find your Mattermost link? Ask your company's IT department or your Mattermost system admin for your organization's **Mattermost Site URL**. It'll look something like ``https://example.com/company/mattermost``, ``mattermost.yourcompanydomain.com``, or ``chat.yourcompanydomain.com``. These URLs could also end in ``.net``.



.. tabs::

  .. tab:: Desktop

    **Web browser**

    1. Open a web browser.
    2. Copy and paste the Mattermost server link into the browser's address field.
    3. Enter your user credentials to log into Mattermost. 

    .. tip::

      - We recommend bookmarking the Mattermost URL in your browser of choice so logging into Mattermost is easy in the future.
      - The credentials you use to log in depend on how your system admin has configured Mattermost. You may be prompted for an `email address or username <#email-address-or-username>`__ and a password, or you may be able to `log in using other credentials <#single-sign-on-sso>`__. Contact your system admin for more information.
    
    **Desktop app**

    1. Download and install the Mattermost `desktop app </install/desktop-app-install.html>`__.
    2. When prompted, enter the Mattermost server link and a display name for the Mattermost instance. The display name is helpful in cases where you connect to multiple Mattermost instances. See the `server connections </welcome/manage-multiple-server-connections.html>`__ documentation for details.
    3. Enter your user credentials to log into Mattermost. 
    4. The team that displays first in the team sidebar opens. If you're not a member of a team yet, you're prompted to select a team to join.


  .. tab:: Mobile

    1. Download and install the Mattermost `mobile app </deploy/use-prebuilt-mobile-apps.html>`__.
    2. When prompted, enter the Mattermost server link and a display name for the Mattermost instance. The display name is helpful in cases where you connect to multiple Mattermost instances. See the `server connections </welcome/manage-multiple-server-connections.html>`__ documentation for details.
    3. Enter your user credentials to log into Mattermost. 
    4. The team that displays first in the team sidebar opens. If you're not a member of a team yet, you're prompted to select a team to join.

    .. tip::
      
      The credentials you use to log in depend on how your system admin has configured Mattermost. You may be prompted for an email address or username and a password, or you may be able to log in using other credentials. Contact your system admin for details.

Reset your password
--------------------

If you've forgotten your password, you can reset it on the login screen by selecting **Forgot your password?**, or by contacting your system admin for assistance.

Email address or username
--------------------------

When enabled by your system admin, you can log in with the username or email address used to create your account.

.. image:: ../images/sign-in_with_email.png
  :alt: Log in to Mattermost with your username or email address, or reset your password.

Single Sign-On (SSO)
--------------------

When enabled by your system admin, you may log in using your GitLab, Google, Office 365, AD/LDAP, or SAML credentials.

.. tabs::

  .. tab:: GitLab

      When enabled by your system admin, you can log in with your GitLab account using a one-click login option.

      .. image:: ../images/sign-in-gitlab.png
        :alt: Log in to Mattermost using your GitLab credentials.

  .. tab:: Google

      When enabled by your system admin, you can log in with your Google account using a one-click login option.

      .. image:: ../images/sign-in-google-apps.png
        :alt: Log in to Mattermost using your Google Apps credentials.

  .. tab:: Office 365

      When enabled by your system admin, you can log in with your Office 365 account using a one-click login option.

      .. image:: ../images/sign-in-office365.png
        :alt: Log in to Mattermost with your Office 365 credentials.

  .. tab:: AD/LDAP

    When enabled by your system admin, you can log in with your AD/LDAP credentials. This lets you use the same username and password for Mattermost that you use for various other company services.

    .. image:: ../images/sign-in_with_ldap.png
      :alt: Log in to Mattermost with your AD/LDAP credentials.

  .. tab:: SAML

    When enabled by your system admin, you can log in with your SAML credentials. This lets you use the same username and password for Mattermost that you use for various other company services. 
    
    Mattermost officially supports `Okta </onboard/sso-saml-okta.html>`__, `OneLogin </onboard/sso-saml-onelogin.html>`__, and Microsoft ADFS as an identity provider (IDP) for SAML, but you may use other SAML IDPs as well. See our `SAML Single Sign-On documentation </onboard/sso-saml.html>`__ to learn more about configuring SAML for Mattermost.

    .. image:: ../images/sign-in_with_saml.png
      :alt: Log in to Mattermost with your SAML credentials.