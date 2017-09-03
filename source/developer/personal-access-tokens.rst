.. _personal_access_tokens:

Personal Access Tokens
=======================

Personal access tokens function similar to session tokens and can be used by integrations to `authenticate against the REST API <https://about.mattermost.com/default-api-authentication>`_. It is the most commonly used type of token for integrations.

.. toctree::
   :maxdepth: 2

Creating a Personal Access Token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1 - Enable personal access tokens in **System Console > Integrations > Custom Integrations**.

2 - Identify the account you want to create a personal access token with. You may optionally create a new user account for your integration, such as for a bot account. By default, only System Admins have permissions to create a personal access token. 

3 - To create an access token with a non-admin account, you must first give it the appropriate permissions. Go to **System Console > Users**, search for the user account, and select **Manage Roles** from the dropdown.

.. image:: ../../source/images/access_token_manage_roles.png
  :width: 500 px

4 - Select **Allow this account to generate personal access tokens.**

.. image:: ../../source/images/access_tokens_additional_roles.png
  :width: 500 px

You may optionally allow the account to post to any channel in your Mattermost server, including direct messages by choosing the **post:all** role. **post:channels** role allows the account to post to any public channel in the Mattermost server.

Then hit **Save**.

5 - Sign in to the user account to create a personal access token.

6 - Go to **Account Settings > Security > Personal Access Tokens** and click **Create New Token**.

7 - Enter a description for the token, so you remember what it's used for. Then hit **Save**.

.. note::
  If you create a personal access token for a System Admin account, be extra careful who you share it with. The token enables a user to have full access to the account, including System Admin privileges.
  
  It is recommended to create a personal access token for non-admin accounts.
  
8 - Copy the access token now for your integration and store it in a secure location. You won't be able to see it again!

9 - You're all set! You can now use the personal access token for integrations to interact with your Mattermost server and `authenticate against the Mattermost REST API <https://about.mattermost.com/default-api-authentication>`_.

.. image:: ../../source/images/access_token_settings.png
  :width: 500 px

Revoking a Personal Access Token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A personal access token can be revoked by deleting the token from either the user's account settings or from the System Console.

Once deleted, all sessions using the token are deleted and any attempts using the token to interact with the Mattermost server are blocked.

Account Settings
.................

1 - Sign in to the user account and go to **Account Settings > Security > Personal Access Tokens**. 

2 - Identify the access token you want to revoke and hit **Delete**. Confirm the deletion.

System Console
.................

1 - Go to **System Console > Users**, search for the user account which the token belongs to, and select **Manage Tokens** from the dropdown.

2 - Identify the access token you want to revoke and hit **Delete**. Confirm the deletion.

Frequently Asked Questions (FAQ)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How do personal access tokens differ from regular session tokens?
..................................................................

Personal access tokens do not expire. As a result, you can more easily integrate with Mattermost, bypassing the `session length limits set in the System Console <https://docs.mattermost.com/administration/config-settings.html#sessions>`_.

Moreover, you can optionally assign additional roles for the account creating personal access tokens, letting the account post to any channel in Mattermost, including direct message.

Should I be worried the personal access tokens last forever?
.............................................................

No. Personal access tokens are cryptic random IDs and are not different from user's regular session token created after logging in to Mattermost.

If you do continue to have worries, you can set up your integration to self-rotate the personal access tokens via `available API calls <https://api.mattermost.com/#tag/users%2Fpaths%2F~1users~1%7Buser_id%7D~1tokens%2Fpost>`_, or simply use the regular user session tokens. The API calls support the new **post:all** and **post:channels** roles as well.

How do I identify a badly behaving personal access token?
..........................................................

Best option is to go to **System Console > Logs** and finding error messages relating to a particular token ID.

Once identified, you can search which user account the token ID belongs to in **System Console > Users** and revoke it through the **Manage Tokens** dropdown option.
