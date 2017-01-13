Command Line Tools
==================

From the directory where the Mattermost platform is installed, a
``platform`` command is available for configuring the system, including:

**General Administration**

-  Creating teams
-  Creating users
-  Assigning roles to users
-  Reseting user passwords
-  Inviting users to teams

**Advanced Administration**

-  Permanently deleting users (use cautiously - database backup
   recommended before use)
-  Permanently deleting teams (use cautiously - database backup
   recommended before use)

**Advanced Automation**

*Available in Enterprise Edition E10 and higher*

-  Creating channels
-  Inviting users to channels
-  Removing users from channels
-  Listing all public channels and private groups for a team
-  Restoring previously deleted channels
-  Migrating sign-in options
-  Resetting multi-factor authentication for a user

.. contents::
    :backlinks: top

CLI Commands
------------

Typing ``platform help`` and ``platform help {command}`` returns help documentation for the CLI tool or any CLI command in particular.

Notes:

-  Parameters in CLI commands are order-specific.
-  If special characters (``!``, ``|``, ``(``, ``)``, ``\``,
   \`\`\`\ ``, and``"``) are used, the entire argument needs to be surrounded by single quotes (e.g.``-password
   'mypassword!'``, or the individual characters need to be escaped out (e.g.``-password
   mypassword/!\`\`).
-  Team name and channel name refer to the handles, not the display
   names. So in the url
   ``https://pre-release.mattermost.com/core/channels/town-square`` team
   name would be ``core`` and channel name would be ``town-square``

.. tip::
   If you automate user creation through the CLI tool with SMTP enabled, emails will be sent to all new users created. If you run such a load script, it is best to disable SMTP or to use test accounts so that new account creation emails aren't unintentionally set to people at your organization who aren't expecting them.

platform
~~~~~~~~

  Description
    Commands for configuring and managing your Mattermost instance and users.

  Options
    .. code-block:: none

      -c, --config {string}   Configuration file to use. (default "config.json")

  Child Commands
    -  `platform channel`_ - Management of channels
    -  `platform help`_ - Generate full documentation for the CLI
    -  `platform import`_ - Import data
    -  `platform ldap`_ - LDAP related utilities
    -  `platform license`_ - Licensing commands
    -  `platform reset`_ - Reset the database to initial state
    -  `platform roles`_ - Management of user roles
    -  `platform server`_ - Run the Mattermost server
    -  `platform team`_ - Management of teams
    -  `platform user`_ - Management of users
    -  `platform version`_ - Display version information

platform channel
~~~~~~~~~~~~~~~~

  Description
    Commands for channel management.

  Child Commands
    -  `platform channel add`_ - Add users to a channel
    -  `platform channel create`_ - Create a channel
    -  `platform channel delete`_ - Delete a channel
    -  `platform channel list`_ - List all channels on specified teams
    -  `platform channel remove`_ - Remove users from a channel
    -  `platform channel restore`_ - Restore a channels

platform channel add
^^^^^^^^^^^^^^^^^^^^

  Description
    Add users to a channel. If adding multiple users, use a space-separated list.

  Format
    .. code-block:: none

      ./platform channel add {channel} {users}

  Example
    .. code-block:: none

      ./platform channel add mychannel user@example.com username

platform channel create
^^^^^^^^^^^^^^^^^^^^^^^

  Description
    Create a channel.

  Format
    .. code-block:: none

      ./platform channel create

  Examples
    .. code-block:: none

      ./platform channel create --team myteam --name mynewchannel --display_name "My New Channel"
      ./platform channel create --team myteam --name mynewprivatechannel --display_name "My New Private Channel" --private

  Options
    .. code-block:: none

          --display_name string   Channel Display Name
          --header string         Channel header
          --name string           Channel Name
          --private               Create a private channel.
          --purpose string        Channel purpose
          --team string           Team name or ID

platform channel delete
^^^^^^^^^^^^^^^^^^^^^^^

  Description
    Permanently deletes a channel along with all related information, including posts from the database. Channels can be specified by {team}:{channel} using the team and channel names or IDs.

  Format
    .. code-block:: none

      platform channel delete {channels}

  Example
    .. code-block:: none

      channel delete myteam:mychannel

platform channel list
^^^^^^^^^^^^^^^^^^^^^

  Description
    List all channels on a specified team. Archived channels are appended with ``(archived)``.

  Format
    .. code-block:: none

      platform channel list {teams}

  Example
    .. code-block:: none

      channel list myteam

platform channel remove
^^^^^^^^^^^^^^^^^^^^^^^

  Description
    Remove users from a channel.

  Format
    .. code-block:: none

      platform channel remove {channel} {users}

  Example
    .. code-block:: none

      channel remove mychannel user@example.com username

platform channel restore
^^^^^^^^^^^^^^^^^^^^^^^^

  Description
    Restore a previously deleted channel. Channels can be specified by {team}:{channel} using the team and channel names or IDs.

  Format
    .. code-block:: none

      platform channel restore {channels}

  Example
    .. code-block:: none

      channel restore myteam:mychannel

platform help
~~~~~~~~~~~~~~~~

  Description
    Generates full documentation in Markdown format for the Mattermost command line tools.

  Format
    .. code-block:: none

      platform help {outputdir}

platform import
~~~~~~~~~~~~~~~

  Description
    Import data into Mattermost.

  Child Command
    -  `platform import slack`_ - Import a team from Slack.

platform import slack
^^^^^^^^^^^^^^^^^^^^^

  Description
    Import a team from a Slack export zip file.

  Format
    .. code-block:: none

      platform import slack {team} {file}

  Example
    .. code-block:: none

      import slack myteam slack_export.zip

platform ldap
~~~~~~~~~~~~~

  Description
    Commands to configure and syncronize LDAP.

  Child Command
    -  `platform ldap sync`_ - Synchronize now

platform ldap sync
^^^^^^^^^^^^^^^^^^

  Description
    Synchronize all LDAP users now.

  Format
    .. code-block:: none

      platform ldap sync

  Example
    .. code-block:: none

      ldap sync

platform license
~~~~~~~~~~~~~~~~

  Description
    Commands to manage licensing.

  Child Command
    -  `platform license upload`_ - Upload a license.

platform license upload
^^^^^^^^^^^^^^^^^^^^^^^

  Description
    Upload a license. This command replaces the current license if one is already uploaded.

  Format
    .. code-block:: none

      platform license upload {license}

  Example
    .. code-block:: none

      license upload /path/to/license/mylicensefile.mattermost-license

platform reset
~~~~~~~~~~~~~~

  Description
    Completely erases the database causing the loss of all data. This resets Mattermost to its initial state.

  Format
    .. code-block:: none

      platform reset

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete everything and a DB backup has been performed.

platform roles
~~~~~~~~~~~~~~

  Description
    Commands to manage user roles.

  Child Commands
    -  `platform roles member`_ - Remove System Admin privileges from a user
    -  `platform roles system_admin`_ - Make a user into a System Admin

platform roles member
^^^^^^^^^^^^^^^^^^^^^

  Description
    Remove system admin privileges from a user.

  Format
    .. code-block:: none

      platform roles member {users}

  Example

    .. code-block:: none

      roles member user1

platform roles system\_admin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Description
    Promote a user to a System Admin.

  Format
    .. code-block:: none

      platform roles system_admin {users}

  Example
    .. code-block:: none

      roles system_admin user1

platform server
~~~~~~~~~~~~~~~

  Description
    Runs the Mattermost server.

  Format
    .. code-block:: none

      platform server

platform team
~~~~~~~~~~~~~

  Description
    Commands to manage teams.

  Child Commands
    -  `platform team add`_ - Add users to a team
    -  `platform team create`_ - Create a team
    -  `platform team delete`_ - Delete a team
    -  `platform team remove`_ - Remove users from a team

platform team add
^^^^^^^^^^^^^^^^^

  Description
    Add users to a team.

  Format
    .. code-block:: none

      platform team add {team} {users}

  Example
    .. code-block:: none

      team add myteam user@example.com username

platform team create
^^^^^^^^^^^^^^^^^^^^

  Description
    Create a team.

  Format
    .. code-block:: none

      platform team create

  Examples
    .. code-block:: none

      team create --name mynewteam --display_name "My New Team"
      teams create --name private --display_name "My New Private Team" --private

  Options
    .. code-block:: none

          --display_name string   Team Display Name
          --email string          Administrator Email (anyone with this email is automatically a team admin)
          --name string           Team Name
          --private               Create a private team.

platform team delete
^^^^^^^^^^^^^^^^^^^^

  Description
    Permanently deletes a team along with all related information, including posts from the database.

  Format
    .. code-block:: none

      platform team delete {teams}

  Example
    .. code-block:: none

      team delete myteam

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete the team and a DB backup has been performed.

platform team remove
^^^^^^^^^^^^^^^^^^^^

  Description
    Remove users from a team.

  Format
    .. code-block:: none

      platform team remove {team} {users}

  Example
    .. code-block:: none

      team remove myteam user@example.com username

platform user
~~~~~~~~~~~~~

  Description
    Commands to manage users.

  Child Commands
    -  `platform user activate`_ - Activate a user
    -  `platform user create`_ - Create a user
    -  `platform user deactivate`_ - Deactivate a user
    -  `platform user delete`_ - Delete a user and all posts
    -  `platform user deleteall`_ - Delete all users and all posts
    -  `platform user invite`_ - Send a user an email invitation to a team
    -  `platform user migrate_auth`_ - Mass migrate all user accounts to a new authentication type
    -  `platform user password`_ - Set a user's password
    -  `platform user resetmfa`_ - Turn off MFA for a user
    -  `platform user verify`_ - Verify email address of a new user

platform user activate
^^^^^^^^^^^^^^^^^^^^^^

  Description
    Activate users that have been deactivated.

  Format
    .. code-block:: none

      platform user activate {emails, usernames, userIds}

  Examples
    .. code-block:: none

      user activate user@example.com
      user activate username

platform user create
^^^^^^^^^^^^^^^^^^^^

  Description
    Create a user.

  Format
    .. code-block:: none

      platform user create

  Examples
    .. code-block:: none

      user create --email user@example.com --username userexample --password Password1 
      user create --firstname Joe --system_admin --email joe@example.com --username joe --password Password1

  Options
    .. code-block:: none

          --email string       Email
          --firstname string   First Name
          --lastname string    Last Name
          --locale string      Locale (ex: en, fr)
          --nickname string    Nickname
          --password string    Password
          --system_admin       Make the user a system administrator
          --username string    Username

platform user deactivate
^^^^^^^^^^^^^^^^^^^^^^^^

  Description
    Deactivate a user. Deactivated users are immediately logged out of all sessions and are unable to log back in.

  Format
    .. code-block:: none

      platform user deactivate {emails, usernames, userIds}

  Examples
    .. code-block:: none

      user deactivate user@example.com
      user deactivate username

platform user delete
^^^^^^^^^^^^^^^^^^^^

  Description
    Permanently deletes a user and all related information, including posts.

  Format
    .. code-block:: none

      platform user delete {users}

  Example
    .. code-block:: none

        user delete user@example.com

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete the user and a DB backup has been performed.

platform user deleteall
^^^^^^^^^^^^^^^^^^^^^^^

  Description
    Permanently delete all users and all related information, including posts.

  Format
    .. code-block:: none

      platform user deleteall

  Example
    .. code-block:: none

      user deleteall

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete the user and a DB backup has been performed.

platform user invite
^^^^^^^^^^^^^^^^^^^^

  Description
    Send a user an email invite to a team. You can invite a user to multiple teams by listing the team names or team IDs.

  Format
    .. code-block:: none

      platform user invite {email} {teams}

  Examples
    .. code-block:: none

      user invite user@example.com myteam
      user invite user@example.com myteam1 myteam2

platform user migrate\_auth
^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Description
    Migrates all user accounts from one authentication provider to another. For example, you can upgrade your authentication provider from email to ldap. Output will display any accounts that are not migrated successfully.

    -  ``from_auth``: The authentication service to migrate users accounts from. Supported options: ``email``, ``gitlab``, ``saml``.

    -  ``to_auth``: The authentication service to migrate users to. Supported options: ``ldap``.

    -  ``match_field``: The field that is guaranteed to be the same in both authentication services. For example, if the users emails are consistent set to email. Supported options: ``email``, ``username``.

  Format
    .. code-block:: none

      platform user migrate_auth {from_auth} {to_auth} {match_field}

  Example
    .. code-block:: none

      user migrate_auth email ladp email

platform user password
^^^^^^^^^^^^^^^^^^^^^^

  Description
    Set a user's password.

  Format
    .. code-block:: none

      platform user password {user} {password}

  Example
    .. code-block:: none

      user password user@example.com Password1

platform user resetmfa
^^^^^^^^^^^^^^^^^^^^^^

  Description
    Turns off multi-factor authentication for a user. If MFA enforcement is enabled, the user will be forced to re-enable MFA with a new device as soon as they log in.

  Format
    .. code-block:: none

      platform user resetmfa {users}

  Example
    .. code-block:: none

      user resetmfa user@example.com

platform user verify
^^^^^^^^^^^^^^^^^^^^

  Description
    Verify the email address of a new user.

  Format
    .. code-block:: none

      platform user verify {users}

  Example
    .. code-block:: none

        user verify user1

platform version
~~~~~~~~~~~~~~~~

  Description
    Displays Mattermost version information.

  Format
    .. code-block:: none

      platform version
