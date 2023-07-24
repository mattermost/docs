GitLab Single Sign-On
=====================

.. include:: ../_static/badges/entpro-cloud-free.rst
  :start-after: :nosearch:

Configuring GitLab as a Single Sign-On (SSO) service
----------------------------------------------------

Follow these steps to configure Mattermost to use GitLab as a Single Sign-on (SSO) service for team creation, account creation, and user login.

.. note::  
  - Only the default GitLab SSO is officially supported. 
  - "Double SSO", where GitLab SSO is chained to other SSO solutions, is not supported. It may be possible to connect GitLab SSO with AD, LDAP, SAML, or MFA add-ons in some cases, but because of the special logic required, they're not officially supported, and they're known not to work in some cases. 
  - Mattermost's open source Team Edition supports the OAuth 2.0 standard.
  - Mattermost Professional and Enterprise support the OpenID Connect standard.

Step 1: Add a Mattermost application to your GitLab account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Log in to your GitLab account, then go to ``https://{gitlab-site-name}/profile/applications``. For *{gitlab-site-name}* use the name of your GitLab instance. If you're using GitLab itself as your service provider, use ``gitlab.com``.

2. Add a new application:

  a. In the **Name** field, enter ``Mattermost``.
  b. In the **Redirect URI** field, add the following two lines using your own value for *{mattermost-site-name}*.

    .. code-block:: text

      https://{mattermost-site-name}/login/gitlab/complete
      https://{mattermost-site-name}/signup/gitlab/complete

   If your GitLab instance is not set up to use SSL, your URIs must begin with ``http://`` instead of ``https://``.

  c. Select scopes.
  
     - For Mattermost Team Edition, select ``read_user``.
     - For Mattermost Enterprise, select ``openid``, ``profile``, and ``email``.

3. Select **Save application**.

4. Keep the GitLab window open. You need the *Application Id* and *Application Secret Key* when you configure Mattermost.

Step 2: Configure Mattermost for GitLab SSO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Log in to Mattermost, then go to **System Console > Authentication > OpenID Connect**.
2. Select **GitLab** as the service provider.
3. Enter the **GitLab Site URL** of your GitLab instance. If your GitLab instance is not set up to use SSL, start the URL with ``http://`` instead of ``https://``. If you are using GitLab itself as your provider, use ``gitlab.com``.
4. The **Discovery Endpoint** for OpenID Connect with GitLab is prepopulated with ``https://gitlab.com/.well-known/openid-configuration``.
5. Paste the **Application ID** from GitLab as the **Client ID** in Mattermost.
6. Paste the **Application Secret Key** from GitLab as the **Client Secret** in Mattermost. 
7. Update the ``config.json`` file and specify the scopes you selected in GitLab under the ``GitLabSettings`` property. At a minimum, ``openid`` is a required scope for Mattermost Professional and Enterprise, and ``read_user`` is a required scope for Mattermost Team Edition. Mattermost Team Edition does not work with scopes other than ``read_user``. Changes to this setting require a server restart before taking effect. 
8. Select **Save**.

.. note::

  - When Mattermost is configured to use OpenID Connect or OAuth 2.0 for user authentication, the following user attribute changes can't be made through the Mattermost API: first name, last name, or username. OpenID Connect or OAuth 2.0 must be the authoritative source for these user attributes.
  - If you are using Mattermost behind a load balancer and you have SSL configured, you may need to set `X-Forwarded-Proto` header to https at your load balancer.

(Optional) Step 3: Force users to sign up using SSO only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To force all users to sign-up with SSO only, set **System Console > Authentication > Email > Enable sign-in with email** to ``false``
Users must change their login method before they can log in to Mattermost with GitLab.

Frequently Asked Questions
--------------------------

How can I use LDAP attributes or Groups with OpenID?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At this time, LDAP data isn't compatible with OpenID. If you currently rely on LDAP to manage your users' teams, channels, groups, or attributes, you won't be able to do this automatically with users who have logged in with OpenID. If you need LDAP synced to each user, we suggest using SAML or LDAP as the login provider. Some OpenID providers can use SAML instead, like Keycloak.
