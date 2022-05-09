Sign in to Mattermost
=====================

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

You'll receive link to access Mattermost from your Mattermost System Admin or through an email invitation. Once you have your organization's Mattermost link, navigate to that URL in a browser, then enter your user credentials.

.. tip::
  - We recommend bookmarking the Mattermost URL in a browser so signing in to Mattermost is easy in the future.
  - Can't find your Mattermost link? Ask your company's IT department or your Mattermost System Admin for your organization's **Mattermost Site URL**. It'll look something like ``https://example.com/company/mattermost``, ``mattermost.yourcompanydomain.com``, or ``chat.yourcompanydomain.com``. These URLs could also end in ``.net``.
  - Mattermost Cloud customers can reach Cloud workspaces from the [Cloud Workspace Connection](https://customers.mattermost.com/cloud/connect-workspace) page by specifying their company or domain name.

After signing in, the team that appears first on your team sidebar will open. If you have not joined a team, the Team Selection page opens where you can view a list of teams that you can join.

Reset your password
--------------------

If you've forgotten your password, you can reset on the sign-in screen by selecting **I forgot my password**, or by contacting your System Admin for help.

Email address or username
--------------------------

When enabled by your System Admin, you can sign in with the username or email address used to create your account.

.. image:: ../images/sign-in_with_email.png
  :alt: Sign in to Mattermost with your username or email address, or reset your password.

Single Sign-On (SSO)
--------------------
  
When enabled by your System Admin, you can sign in using your GitLab, Google, Office 365, AD/LDAP, or SAML credentials.

GitLab SSO
~~~~~~~~~~

|all-plans| |cloud| |self-hosted|

When enabled by your System Admin, you can sign in with your GitLab account using a one-click sign in option.

.. image:: ../images/sign-in-gitlab.png
  :alt: Sign in to Mattermost using your GitLab credentials.

Google SSO
~~~~~~~~~~~

|enterprise| |professional| |cloud| |self-hosted|

*Available in legacy Mattermost Enterprise Edition E20*

When enabled by your System Admin, you can sign in with your Google account using a one-click sign in option.

.. image:: ../images/sign-in-google-apps.png
  :alt: Sign in to Mattermost using your Google Apps credentials.

Office 365 SSO
~~~~~~~~~~~~~~

|enterprise| |professional| |cloud| |self-hosted|

*Available in legacy Mattermost Enterprise Edition E20*

When enabled by your System Admin, you can sign in with your Office 365 account using a one-click sign in option.

.. image:: ../images/sign-in-office365.png
  :alt: Sign in to Mattermost with your Office 365 credentials.

AD/LDAP SSO
~~~~~~~~~~~

|enterprise| |professional| |cloud| |self-hosted|

*Available in legacy Mattermost Enterprise Edition E10 and E20*

When enabled by your System Admin, you can sign in with your AD/LDAP credentials. This lets you use the same username and password for Mattermost that you use for various other company services.

.. image:: ../images/sign-in_with_ldap.png
  :alt: Sign in to Mattermost with your AD/LDAP credentials.

SAML SSO
~~~~~~~~

|enterprise| |professional| |cloud| |self-hosted|

*Available in legacy Mattermost Enterprise Edition E20*

When enabled by your System Admin, you can sign in with your SAML credentials. This lets you use the same username and password for Mattermost that you use for various other company services. Mattermost officially supports `Okta <https://docs.mattermost.com/onboard/sso-saml-okta.html>`__, `OneLogin <https://docs.mattermost.com/onboard/sso-saml-onelogin.html>`__, and Microsoft ADFS as an identity provider (IDP) for SAML, but you may use other SAML IDPs as well. Please see our `SAML Single Sign-On documentation <https://docs.mattermost.com/onboard/sso-saml.html>`__ to learn more about configuring SAML for Mattermost.

.. image:: ../images/sign-in_with_saml.png
