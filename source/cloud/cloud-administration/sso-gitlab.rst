GitLab Single Sign-On
=====================

Follow these steps to configure Mattermost to use GitLab as a Single Sign-on (SSO) service for team creation, account creation, and user sign-in.

.. Note::  
  Only the default GitLab SSO is officially supported. "Double SSO", where GitLab SSO is chained to other SSO solutions, is not supported. It may be possible to connect GitLab SSO with AD, LDAP, SAML, or MFA add-ons in some cases, but because of the special logic required, they're not officially supported, and they're known not to work in some cases. 

Migrating an existing connection
-------------------------------------------------

To migrate an existing GitLab OAuth connection to OpenID:

[TBD]

Creating a new connection
------------------------------------------

Step 1: Add an OAuth application to your GitLab account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Sign in to your GitLab account, then go to ``https://{gitlab-site-name}/profile/applications``. 

  For *{gitlab-site-name}* use the name of your GitLab instance. If you're using GitLab itself as your OAuth provider, use *gitlab.com*.

2. Add a new application:

  a. In the **Name** field, type *Mattermost*.
  b. In the **Redirect URI** field add the following two lines, using your own value for *{mattermost-site-name}*.

    .. code-block:: text

      https://{mattermost-site-name}/login/gitlab/complete
      https://{mattermost-site-name}/signup/gitlab/complete

     If your GitLab instance is not set up to use SSL, your URIs must begin with ``http://`` instead of ``https://``.

  c. Do not select any options under **Scopes**.

3. Select **Save application**.

4. Keep the GitLab window open. You need the *Application Id* and *Applicatio Secret Key* when you configure Mattermost.

Step 2: Configure Mattermost for GitLab SSO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Log in to Mattermost, then go to the **System Console > Authentication > OpenID Connect**.
2. Select **GitLab** as the service provider.
3. Copy and paste the *Application ID* from GitLab to Mattermost.
4. Copy and paste the *Application Secret Key* from GitLab to Mattermost. 
5. Enter the **Gitlab Site URL** of our GitLab instance. 

  If your GitLab instance is not set up to use SSL, the endpoints must begin with ``http://`` instead of ``https://``. If you are using GitLab itself as your OAuth provider, use *gitlab.com*.

6. Enter the **User API Endpoint**. 

  Use ``https://{gitlab-site-name}/api/v3/user`` if you're running GitLab v8.17.8 or earlier.

(Optional) Step 3: Forcing all users to sign up with SSO only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To force all users to sign-up with SSO only, set **System Console > Authentication > Email > Enable sign-in with email** to ``false``

Users must change their sign-in method before they can sign in to Mattermost with GitLab.
