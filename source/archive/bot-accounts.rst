:nosearch:

.. _bot-accounts:

Bot Accounts
=================

Use Bot accounts to integrate with Mattermost through `plugins <https://developers.mattermost.com/extend/plugins/>`_ or the `Mattermost RESTful API <https://api.mattermost.com>`_. Bot accounts access the RESTful API on behalf of a bot through the use of the :doc:`personal access tokens feature <personal-access-tokens>`.

Bot accounts are just like user accounts, except they:

- Can't be logged into.
- Can't be used to create other bot accounts.
- Don't count as a registered user and therefore don't count towards the total number of users for an Enterprise Edition license.

Additional benefits include:

- System Admins can enable Bot accounts to post to any channel in the system, including private teams, private channels, or Direct Message channels.
- Integrations created by a user and tied to a bot account no longer break if the user leaves the company.
- Once created, bot accounts behave just like regular user accounts and can be added to teams and channels similar to users.
- Bot accounts are a safer way to integrate with Mattermost through the RESTful API and Plugin API because there is no need to manage shared logins with these accounts.
- A ``BOT`` tag is used throughout Mattermost where bot accounts are referenced, including messages and user lists.

Note that currently:

- Only System Admins or plugins can create or manage bot accounts.
- Only user accounts can create and configure webhooks and slash commands.
- In Mattermost Enterprise Edition, service accounts without an email address pulled from LDAP or SAML systems are not yet supported.

If you would like to see improvements to bot accounts, `let us know in the Feature Proposal Forum <https://mattermost.uservoice.com>`_.

.. contents::
  :backlinks: top
  :depth: 1
  :local:

Configuration Settings
----------------------

By default, plugins can create and manage bot accounts. To enable bot account creation through the user interface or the RESTful API:

1. Go to **System Console > Integrations > Bot Accounts**.
2. Set **Enable Bot Account Creation** to ``true``.

Once set, System Admin can create bot accounts for integrations using the **Integrations > Bot Accounts** link in the description provided.

Bot Account Creation
--------------------

Below are different ways to create bot accounts. After the bot account is created, make sure to:

1. Copy the generated bot access token for your integration.
2. Add the bot account to teams and channels you want it to interact in.

User Interface (UI)
^^^^^^^^^^^^^^^^^^^

1. Go to **Main Menu > Integrations > Bot Accounts**.
2. Select **Add Bot Account**.
3. Set the **Username** of the bot. The username must begin with a letter, and contain between 3 and 22 lowercase characters made up of numbers, letters, and symbols including ".", "-", or "_".
4. (Optional) Upload an image for the **Bot Icon**. This will be used as the profile image of the bot throughout Mattermost.
5. (Optional) Set a **Display Name** and **Description**.
6. (Optional) Choose what role the bot should have. Defaults to **Member**. If you assign **System Admin**, the bot will have read and write access for any Public channels, Private channels, and Direct Messages.
7. (Optional) Select additional permissions for the account. Enable the bot to post to all Mattermost channels, or post to all Mattermost Public channels.

RESTful API
^^^^^^^^^^^

Use the RESTful API ``POST /bots`` to create a bot. You must have permissions to create bots.

See our `API documentation <https://api.mattermost.com/#tag/bots>`_ to learn more about creating and managing bots through the API.

To authorize your bot via RESTful API use ``curl -i -H 'authorization: Bearer <Access Token>' http://localhost:8065/api/v4/users/me``. **Access Token** is not the ``Token ID`` and won't be visible again once created.

Command Line Interface (CLI)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use the following CLI command to convert an existing user account to a bot:

.. code-block:: text

  user convert user@example.com --bot

In addition to email, you may identify the user by its username or user ID.

Bot accounts which were converted from user accounts will have their authentication data cleared if they were email/password accounts. Those synchronized from LDAP/SAML will not have their authentication data cleared so that LDAP/SAML synchronization performs correctly.

Plugins
^^^^^^^^

Plugins can create bot accounts through an ``EnsureBot`` helper function. For an example, see `the Demo Plugin <https://github.com/mattermost/mattermost-plugin-demo/blob/master/server/configuration.go#L210-L217>`_.

Bots created by a plugin use the plugin's ID as the creator, unless otherwise specified by the plugin.

Technical Notes
---------------

Data Model
^^^^^^^^^^^

Each bot account has a row in the **Users** table and the **Bots** table. The entries are tied together by ``User.Id = Bot.UserId``.

The Bots table schema is described as follows:

.. csv-table::
    :header: "Field", "Description", "Type", "Required"

    "UserId", "User ID of the bot user", "string", "Y"
    "Username", "Username of the bot account", "string", "Y"
    "DisplayName", "Display name of the bot account", "string", "N"
    "Description", "Description of the bot account", "string", "N"    
    "OwnerId", "User ID of the owner of the bot", "string", "Y"
    "CreateAt", "Unix timestamp of creation time", "int64", "Y"
    "UpdateAt", "Unix timestamp of update time", "int64", "Y"
    "DeleteAt", "Unix timestamp of deletion time", "int64", "Y"

Frequently Asked Questions
--------------------------

Should I migrate all my integrations to use bot accounts?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For your integrations using RESTful API and plugins, yes. To do so, you can either convert an existing account to a bot, or create a new bot account using the steps outlined above.

Once you create a bot account, use the generated token to access the RESTful API on behalf of a bot and interact in the Mattermost server.

For your webhook and slash command integrations, you cannot migrate them to use bot accounts, as they require a user account at this time. However, an option is to migrate the webhooks or slash commands to a plugin, which in turn can use bot accounts.

What happens if a plugin is using a bot account that already exists as a user account?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For a concrete example, suppose you enable the `Mattermost GitHub plugin <https://github.com/mattermost/mattermost-plugin-github>`_, which uses a ``github`` bot account, while an existing ``github`` user account was created for webhook integrations.

Once the plugin is enabled, the plugin posts as the ``github`` account but without a `BOT` tag. An error message is logged to the server logs recommending the System Admin to convert the ``github`` user to a bot account by running ``mattermost user convert <username> --bot`` in the CLI.

If the user is an existing user account you want to preserve, change its username and restart the Mattermost server, after which the plugin will create a bot account with the name ``github``.

How do I convert an existing account to a bot account?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use the `mmctl command line tool </manage/mmctl-command-line-tool.html>`_ to convert a user to a bot, with the following command:

.. code-block:: text

  mmctl user convert user@example.com --bot

In addition to an email address, users can be identified by their Mattermost username or user ID.

Bot accounts which were converted from user accounts will have their authentication data cleared if they were email/password accounts. Those synchronized from LDAP/SAML will not have their authentication data cleared so that LDAP/SAML synchronization performs correctly.

How can I quickly test if my bot account is working?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add the bot to a team and channel you belong to, then use the following curl command to post with the bot:

.. code-block:: text

  curl -i -X POST -H 'Content-Type: application/json' -d '{"channel_id":"<channel-id>", "message":"This is a message from a bot", "props":{"attachments": [{"pretext": "Look some text","text": "This is text"}]}}' -H 'Authorization: Bearer <bot-access-token>' <mattermost-url>/api/v4/posts

Replace the following parameters:

- ``<channel-id>`` with the channel you added the bot to
- ``<bot-access-token>`` with the bot access token generated when you created the bot account
- ``<mattermost-url>`` with your Mattermost domain, e.g. ``https://example.mattermost.com``

Do bot access tokens expire?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No, but you can automate your integration to cycle its token `through the REST API <https://api.mattermost.com/#tag/users%2Fpaths%2F~1users~1%7Buser_id%7D~1tokens%2Fpost>`_.

For more information about access tokens, see :doc:`the personal access tokens documentation <personal-access-tokens>`.

Do bot accounts make it easier to impersonate someone else such as the CEO or an HR coordinator?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Possibly yes. Currently a System Admin can disable overriding the profile picture and the username from integrations to help prevent impersonation, but this is not the case for bot accounts.

Mitigations:

- ``BOT`` tag is used everywhere in the UI where bot accounts are referenced, including messages and user lists.
- For Direct Message channels, the channel header distinguishes the bot from a regular user account with a ``BOT`` tag.

What happens when a user who owns bot accounts is disabled?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, bot accounts managed by the deactivated user are disabled for enhanced security. Those with permissions to manage bot accounts can re-enable them in **Main Menu > Integrations > Bot Accounts**.

We strongly recommend creating new tokens for the bot, to ensure the user who was deactivated no longer has access to read or write data in the system via the bot access token.

If you prefer to have bot accounts remain enabled after user deactivation, set ``DisableBotsWhenOwnerIsDeactivated`` to ``false`` in your ``config.json`` file.

Can bot accounts edit messages through the RESTful API?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Yes. By default, bot accounts can update their own posts.

If you find yourself unable to edit posts as a bot, check the following:

1. Instead of using a slash command to respond directly, use an an API call for the initial interaction with a user to enable message edits.
2. If your system is using `advanced permissions </deployment/advanced-permissions.html>`_, then post edits could be disabled for users.

If neither of the above help resolve your issue, you also have the option to choose what role the bot account has. If System Admin is chosen, then the bot can update any posts in the system. Note that giving the System Admin role to a bot account enables the bot with other System Admin privileges so this should be done with care.

If AD/LDAP or SAML synchronization is enabled, do bot accounts need to have an associated email address in AD/LDAP or SAML?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When AD/LDAP or SAML synchronization is enabled, you can create bot accounts using the steps outlined above. These bot accounts won't require an email address.

If you need to sync service accounts from AD/LDAP or SAML to Mattermost and use them as bot accounts, `please reach out to us <https://mattermost.com/contact-us>`_ to discuss in detail. You may not need to sync service accounts and use them as bot accounts to meet your use case.

How are bot accounts identified in compliance exports?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As of v5.14, a field named ``UserType`` is added to Compliance Exports, including Global Relay, Actiance, and CSV. The field identifies whether a message was posted by a ``user`` or by a ``bot`` account.  
