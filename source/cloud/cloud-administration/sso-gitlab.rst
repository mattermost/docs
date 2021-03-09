
GitLab Single Sign-On
=====================

Migrating from OAuth 2.0 to OpenID Connect
-------------------------------------------

OAuth 2.0 is being deprecated and replaced by OpenID Connect. Refer to product documentation to `convert your existing OAuth configuration <https://docs.mattermost.com/cloud/cloud-administration/converting-oauth-2.0-to-openid-connect.html>`__ for GitLab to the OpenID Connect standard. 

Configuring GitLab as a Single Sign-On (SSO) service
----------------------------------------------------

Follow these steps to configure Mattermost to use GitLab as a Single Sign-on (SSO) service for team creation, account creation, and user sign-in.

.. note::  
  Only the default GitLab SSO is officially supported. "Double SSO", where GitLab SSO is chained to other SSO solutions, is not supported. It may be possible to connect GitLab SSO with AD, LDAP, SAML, or MFA add-ons in some cases, but because of the special logic required, they're not officially supported, and they're known not to work in some cases. 

Step 1: Add an OpenID Connect application to your GitLab account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Sign in to your GitLab account, then go to ``https://{gitlab-site-name}/profile/applications``. For *{gitlab-site-name}* use the name of your GitLab instance. If you're using GitLab itself as your service provider, use ``gitlab.com``.

2. Add a new application:

  a. In the **Name** field, enter ``Mattermost``.
  b. In the **Redirect URI** field, add the following two lines using your own value for *{mattermost-site-name}*.

    .. code-block:: text

      https://{mattermost-site-name}/login/gitlab/complete
      https://{mattermost-site-name}/signup/gitlab/complete

   If your GitLab instance is not set up to use SSL, your URIs must begin with ``http://`` instead of ``https://``.

  c. Do not select any options under **Scopes**.

3. Select **Save application**.

4. Keep the GitLab window open. You need the *Application Id* and *Application Secret Key* when you configure Mattermost.

Step 2: Configure Mattermost for GitLab SSO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Log in to Mattermost, then go to **System Console > Authentication > OpenID Connect**.
2. Select **GitLab** as the service provider.
3. Enter the **Gitlab Site URL** of your GitLab instance. If your GitLab instance is not set up to use SSL, start the URL with ``http://`` instead of ``https://``. If you are using GitLab itself as your provider, use ``gitlab.com``.
4. The **Discovery Endpoint** for OpenID Connect with GitLab is prepopulated with ``https://gitlab.com/.well-known/openid-configuration``.
5. Paste the **Application ID** from GitLab as the **Client ID** in Mattermost.
6. Paste the **Application Secret Key** from GitLab as the **Client Secret** in Mattermost. 
7. Select **Save**.
8. Restart your Mattermost server to see the changes take effect.

(Optional) Step 3: Force users to sign up using SSO only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To force all users to sign-up with SSO only, set **System Console > Authentication > Email > Enable sign-in with email** to ``false``
Users must change their sign-in method before they can sign in to Mattermost with GitLab.
