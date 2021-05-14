GitLab Single Sign-On
=====================

Configure Mattermost to use GitLab as a single sign-on (SSO) service for team creation, account creation, and user sign-in. 

.. Note:: 
  Only the default GitLab SSO is officially supported. "Double SSO", where GitLab SSO is chained to other SSO solutions, is not supported. It may be possible to connect GitLab SSO with AD, LDAP, SAML, or MFA add-ons in some cases, but because of the special logic required they're not officially supported and are known not to work in some instances. If having official AD, LDAP, SAML, or MFA support is critical to your enterprise, please consider `Mattermost Enterprise Edition <https://mattermost.com/pricing/>`__ as an option. 

Step 1: Add an application to your GitLab account
-------------------------------------------------

1. Sign in to your GitLab account, then go to ``https://{gitlab-site-name}/profile/applications``. For ``{gitlab-site-name}`` use the name of your GitLab instance. If you're using GitLab itself as your OAuth provider, use ``gitlab.com``.
2. Add a new application:

  a. In the **Name** field, enter ``Mattermost``.
  b. In the **Redirect URI** field, add the following two lines, using your own value for ``{mattermost-site-name}``:

    .. code-block:: text

      https://{mattermost-site-name}/login/gitlab/complete
      https://{mattermost-site-name}/signup/gitlab/complete

    If your GitLab instance is not set up to use SSL, your URIs must begin with ``http://`` instead of ``https://``.

  c. Do not select any options under **Scopes**.

3. Click **Save application**.
4. Keep the GitLab window open. You need the **Application Id** and **Application Secret** when you configure Mattermost.

Step 2: Configure Mattermost for GitLab SSO
--------------------------------------------

.. note::
  When Mattermost is configured to use OpenID Connect or OAuth 2.0 for user authentication, the following user attribute changes can't be made through the Mattermost API: first name, last name, or username. OpenID Connect or OAuth 2.0 must be the authoritative source for these user attributes.

The steps to configure Mattermost for GitLab SSO depends on your edition of Mattermost. To confirm your Mattermost edition, go to **System Console > About > Edition and License**.

Mattermost Team Edition
~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Team Edition customers can set up a GitLab OAuth 2.0 identity provider in Mattermost.

1. Log in to Mattermost, then go to **System Console > Authentication > Gitlab**.
2. Set **Enable authentication with GitLab** to **true**.
3. Paste the **Application ID** from GitLab into Mattermost.
4. Paste the **Application Secret** from GitLab as the **Application Secret Key** in Mattermost
5. Enter the **GitLab Site URL** of your GitLab instance. If your GitLab instance is not set up with SSL, start the URL with ``http://`` instead of ``https://``. If you're using GitLab itself as your provider, use ``gitlab.com``.
6. (Optional) Enter a **User API Endpoint**.
7. (Optional) Enter an **Auth Endpoint**.
8. (Optional) Enter a **Token Endpoint**.
9. Select **Save**.

Alternatively, you can add the GitLab settings directly to the ``config.json`` file on your Mattermost server.

1. Open ``config.json`` as *root* in a text editor. It’s usually in ``/opt/mattermost/config`` but it might be elsewhere on your system.
2. Locate the ``GitLabSettings`` section, then add or update the following information:

.. code-block:: text

  "GitLabSettings": {
    "Enable": true,
    "Secret": "{mattermost-app-secret-from-gitlab}",
    "Id": "{mattermost-app-application-id-from-gitlab}",
    "Scope": "",
    "AuthEndpoint": "https://{gitlab-site-name}/oauth/authorize",
    "TokenEndpoint": "https://{gitlab-site-name}/oauth/token",
    "UserApiEndpoint": "https://{gitlab-site-name}/api/v4/user"
  }
  
3. Save your changes, then restart your Mattermost server. After the server restarts, users must change their sign-in method before they can sign in with GitLab.

Mattermost Enterprise Edition E10
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Enterprise Edition E10 customers can set up a GitLab OAuth 2.0 identity provider in Mattermost.

1. Log in to Mattermost, then go to **System Console > Authentication > OAuth 2.0**. 
2. Select **GitLab** as the service provider.
3. Paste the **Application ID** from GitLab into Mattermost.
4. Paste the **Application Secret** from GitLab as the **Application Secret Key** in Mattermost
5. Enter the **GitLab Site URL** of your GitLab instance. If your GitLab instance is not set up with SSL, start the URL with ``http://`` instead of ``https://``. If you're using GitLab itself as your provider, use ``gitlab.com``.
6. (Optional) Enter a **User API Endpoint**.
7. (Optional) Enter an **Auth Endpoint**.
8. (Optional) Enter a **Token Endpoint**.
9. Select **Save**.

Alternatively, you can add the GitLab settings directly to the ``config.json`` file on your Mattermost server.

1. Open ``config.json`` as *root* in a text editor. It’s usually in ``/opt/mattermost/config`` but it might be elsewhere on your system.
2. Locate the ``GitLabSettings`` section, then add or update the following information:

.. code-block:: text

  "GitLabSettings": {
    "Enable": true,
    "Secret": "{mattermost-app-secret-from-gitlab}",
    "Id": "{mattermost-app-application-id-from-gitlab}",
    "Scope": "",
    "AuthEndpoint": "https://{gitlab-site-name}/oauth/authorize",
    "TokenEndpoint": "https://{gitlab-site-name}/oauth/token",
    "UserApiEndpoint": "https://{gitlab-site-name}/api/v4/user"
  }

3. Save your changes, then restart your Mattermost server. After the server restarts, users must change their sign-in method before they can sign in with GitLab.

Mattermost Enterprise Edition E20
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost Enterprise Edition E20 customers can set up a new GitLab OpenID Connect identity provider, or they can convert an existing OAuth 2.0 configuration for GitLab to the OpenID Connect standard. From Mattermost Enterprise Edition v5.33, OAuth 2.0 is being deprecated and replaced by OpenID Connect. Refer to product documentation to `convert your existing OAuth 2.0 service provider configuration for GitLab <https://docs.mattermost.com/deployment/converting-oauth20-service-providers-to-openidconnect.html>`__ to the OpenID Connect Standard. 

1. Log in to Mattermost, then go to **System Console > Authentication > OpenID Connect**.
2. Select **GitLab** as the service provider.
3. Enter the **Gitlab Site URL** of your GitLab instance. If your GitLab instance is not set up to use SSL, start the URL with ``http://`` instead of ``https://``. If you're using GitLab itself as your provider, use ``gitlab.com``.
4. The **Discovery Endpoint** for OpenID Connect with GitLab is prepopulated with ``https://gitlab.com/.well-known/openid-configuration``.
5. Paste the **Application ID** from GitLab as the **Client ID** in Mattermost.
6. Paste the **Application Secret Key** from GitLab as the **Client Secret** in Mattermost.
7. Select **Save**.

Alternatively, you can add the GitLab settings directly to the ``config.json`` file on your Mattermost server.

1. Open ``config.json`` as *root* in a text editor. It’s usually in ``/opt/mattermost/config`` but it might be elsewhere on your system.
2. Locate the ``GitLabSettings`` section, then add or update the following information:

.. code-block:: text

  "GitLabSettings": {
    "Enable": true,
    "Secret": "d4ff651332d26b0f76a18141ec6b72d59e04ad",
    "Id": "f4c18eb49f437407758de8b9803668ae6",
    "Scope": "profile openid email",
    "AuthEndpoint": "",
    "TokenEndpoint": "",
    "UserApiEndpoint": "",
    "DiscoveryEndpoint": "https://gitlab.com/.well-known/openid-configuration",
    "ButtonText": "",
    "ButtonColor": ""
  }

3. Save your changes, then restart your Mattermost server. After the server restarts, users must change their sign-in method before they can sign in with GitLab.

(Optional) Step 3: Force users to sign up using SSO only
--------------------------------------------------------

To force all users to sign up with SSO only, go to **System Console > Authentication > Email**, then set **Enable sign-in with email** to **false**. 

Alternatively, add this setting to the ``config.json`` file directly in the ``EmailSettings`` section and set ``EnableSignUpWithEmail`` to ``false``. You must save your changes and restart the Mattermost server. Users must change their sign-in method before they can sign in to Mattermost with GitLab.
