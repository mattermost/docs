GitLab Single Sign-On
=====================

Configure Mattermost to use GitLab as a single sign-on (SSO) service for team creation, account creation, and user sign-in.

Step 1: Add an OAuth application to your GitLab account
-------------------------------------------------------

1. Sign in to your GitLab account and go to ``https://{gitlab-site-name}/profile/applications``. For *{gitlab-site-name}* use the name of your GitLab instance. If you are using GitLab itself as your OAuth provider, use *gitlab.com*.
2. Add a new application:

  a. In the **Name** field, type *Mattermost*.
  b. In the **Redirect URI** field add the following two lines, using your own value for *{mattermost-site-name}*.

    .. code-block:: text

      https://{mattermost-site-name}/login/gitlab/complete
      https://{mattermost-site-name}/signup/gitlab/complete

    If your GitLab instance is not set up to use SSL, your URIs must begin with ``http://`` instead of ``https://``.

  c. In the *Scopes* section, select **api**.

3. Click **Save application**.

Keep the GitLab window open because you need the *Application Id* and *Secret* when you configure Mattermost.

Step 2: Configure Mattermost for GitLab SSO
-------------------------------------------

1. On your Mattermost server, add the *Application Id* and the *Secret* to the *GitLab* settings section in the ``config.json`` file:

  a. Open ``config.json`` as root in a text editor. It's usually in ``/opt/mattermost/config`` but might be elsewhere on your system.
  b. Locate the *GitLabSettings* section and add or update the following information:

    .. code-block:: javascript

      "GitLabSettings": {
          "Enable": true,
          "Secret": "{mattermost-app-secret-from-gitlab}",
          "Id": "{mattermost-app-application-id-from-gitlab}",
          "Scope": "",
          "AuthEndpoint": "https://{gitlab-site-name}/oauth/authorize",
          "TokenEndpoint": "https://{gitlab-site-name}/oauth/token",
          "UserApiEndpoint": "https://{gitlab-site-name}/api/v3/user"
      }

    For *{gitlab-site-name}* use the name of your GitLab instance. If your GitLab instance is not set up to use SSL, the endpoints must begin with ``http://`` instead of ``https://``. If you are using GitLab itself as your OAuth provider, use *gitlab.com*.

2. [Optional] To force all users to sign-up with SSO only, in the *EmailSettings* section of ``config.json`` set *EnableSignUpWithEmail* to ``false``.

3. Restart your Mattermost server.

  On Ubuntu 14.04 and RHEL 6: ``sudo restart mattermost``

  On Ubuntu 16.04 and RHEL 7: ``sudo systemctl restart mattermost``

After the server restarts, users must change their sign-in method before they can sign in with GitLab.
