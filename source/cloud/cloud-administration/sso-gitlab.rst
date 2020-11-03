GitLab Single Sign-On
=====================

Configure Mattermost to use GitLab as a Single Sign-on (SSO) service for team creation, account creation, and user sign-in.

.. Note:: Only the default GitLab SSO is officially supported. "Double SSO", where GitLab SSO is chained to other SSO solutions, is not supported. It may be possible to connect GitLab SSO with AD, LDAP, SAML, or MFA add-ons in some cases, but because of the special logic required they're not officially supported and are known not to work on some experiences. 


Step 1: Add an OAuth application to your GitLab account
-------------------------------------------------------

1. Sign in to your GitLab account and go to ``https://{gitlab-site-name}/profile/applications``. For *{gitlab-site-name}* use the name of your GitLab instance. If you're using GitLab itself as your OAuth provider, use *gitlab.com*.
2. Add a new application:

  a. In the **Name** field, type *Mattermost*.
  b. In the **Redirect URI** field add the following two lines, using your own value for *{mattermost-site-name}*.

    .. code-block:: text

      https://{mattermost-site-name}/login/gitlab/complete
      https://{mattermost-site-name}/signup/gitlab/complete

     If your GitLab instance is not set up to use SSL, your URIs must begin with ``http://`` instead of ``https://``.
  c. Do not select any options under **Scopes**.

3. Click **Save application**.

Keep the GitLab window open because you need the *Application Id* and *Secret* when you configure Mattermost.

Step 2: Configure Mattermost for GitLab SSO
-------------------------------------------

1. Navigate to **System Console > Authentication > OAuth 2.0**. Select ``Gitlab`` in the *Select OAuth 2.0 service provider* dropdown and add other required fields.  
2. Add the Application ID. 
3. Add the Application Secret Key. 
4. Add the Gitlab Sire URL. If your GitLab instance is not set up to use SSL, the endpoints must begin with ``http://`` instead of ``https://``. If you are using GitLab itself as your OAuth provider, use *gitlab.com*.
5. Add the UserApiEndpoint. Use ``https://{gitlab-site-name}/api/v3/user`` if you're running GitLab v8.17.8 or earlier.
6. [Optional] To force all users to sign-up with SSO only, set **System Console > Authentication > Email > Enable sign-in with email** to ``false``

Users must change their sign-in method before they can sign in with GitLab.
