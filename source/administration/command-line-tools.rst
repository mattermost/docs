Command Line Tools
==================

From the directory where the Mattermost platform is installed, a
``platform`` command is available for configuring the system, including:

**General Administration**

-  Creating teams
-  Creating users
-  Assigning roles to users
-  Resetting user passwords
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

Typing ``platform help`` and ``platform help {command}`` returns help documentation for the CLI tool or any CLI command in particular.

Notes:

-  Parameters in CLI commands are order-specific.
-  If special characters (``!``, ``|``, ``(``, ``)``, ``\``, ``'``, and ``"``) are used, the entire argument needs to be surrounded by single quotes (e.g. ``-password 'mypassword!'``, or the individual characters need to be escaped out (e.g. ``-password mypassword/!``).
-  Team name and channel name refer to the handles, not the display names. So in the url ``https://pre-release.mattermost.com/core/channels/town-square`` team name would be ``core`` and channel name would be ``town-square``

.. tip::
   If you automate user creation through the CLI tool with SMTP enabled, emails will be sent to all new users created. If you run such a load script, it is best to disable SMTP or to use test accounts so that new account creation emails aren't unintentionally sent to people at your organization who aren't expecting them.

platform
--------

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
-----------------

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
~~~~~~~~~~~~~~~~~~~~

  Description
    Add users to a channel. If adding multiple users, use a space-separated list.

  Format
    .. code-block:: none

      platform channel add {channel} {users}

  Example
    .. code-block:: none

      platform channel add mychannel user@example.com username

platform channel create
~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Create a channel.

  Format
    .. code-block:: none

      platform channel create

  Examples
    .. code-block:: none

      platform channel create --team myteam --name mynewchannel --display_name "My New Channel"
      platform channel create --team myteam --name mynewprivatechannel --display_name "My New Private Channel" --private

  Options
    .. code-block:: none

          --display_name string   Channel Display Name
          --header string         Channel header
          --name string           Channel Name
          --private               Create a private channel.
          --purpose string        Channel purpose
          --team string           Team name or ID

platform channel delete
~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Permanently delete a channel along with all related information, including posts from the database. Channels can be specified by {team}:{channel} using the team and channel names or IDs.

  Format
    .. code-block:: none

      platform channel delete {channels}

  Example
    .. code-block:: none

      platform channel delete myteam:mychannel

platform channel list
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    List all channels on a specified team. Archived channels are appended with ``(archived)``.

  Format
    .. code-block:: none

      platform channel list {teams}

  Example
    .. code-block:: none

      platform channel list myteam

platform channel remove
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Remove users from a channel.

  Format
    .. code-block:: none

      platform channel remove {channel} {users}

  Example
    .. code-block:: none

      platform channel remove mychannel user@example.com username

platform channel restore
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Restore a previously deleted channel. Channels can be specified by {team}:{channel} using the team and channel names or IDs.

  Format
    .. code-block:: none

      platform channel restore {channels}

  Example
    .. code-block:: none

      platform channel restore myteam:mychannel

platform help
---------------

  Description
    Generate full documentation in Markdown format for the Mattermost command line tools.

  Format
    .. code-block:: none

      platform help {outputdir}

platform import
----------------

  Description
    Import data into Mattermost.

  Child Command
    -  `platform import slack`_ - Import a team from Slack.

platform import slack
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Import a team from a Slack export zip file.

  Format
    .. code-block:: none

      platform import slack {team} {file}

  Example
    .. code-block:: none

      platform import slack myteam slack_export.zip

platform ldap
-------------

  Description
    Commands to configure and syncronize LDAP.

  Child Command
    -  `platform ldap sync`_ - Synchronize now

platform ldap sync
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Synchronize all LDAP users now.

  Format
    .. code-block:: none

      platform ldap sync

  Example
    .. code-block:: none

      platform ldap sync

platform license
-----------------

  Description
    Commands to manage licensing.

  Child Command
    -  `platform license upload`_ - Upload a license.

platform license upload
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Upload a license. This command replaces the current license if one is already uploaded.

  Format
    .. code-block:: none

      platform license upload {license}

  Example
    .. code-block:: none

      platform license upload /path/to/license/mylicensefile.mattermost-license

platform reset
---------------

  Description
    Completely erase the database causing the loss of all data. This resets Mattermost to its initial state.

  Format
    .. code-block:: none

      platform reset

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete everything and a DB backup has been performed.

platform roles
---------------

  Description
    Commands to manage user roles.

  Child Commands
    -  `platform roles member`_ - Remove System Admin privileges from a user
    -  `platform roles system_admin`_ - Make a user into a System Admin

platform roles member
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Remove system admin privileges from a user.

  Format
    .. code-block:: none

      platform roles member {users}

  Example
    .. code-block:: none

      platform roles member user1

platform roles system\_admin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Promote a user to a System Admin.

  Format
    .. code-block:: none

      platform roles system_admin {users}

  Example
    .. code-block:: none

      platform roles system_admin user1

platform server
----------------

  Description
    Runs the Mattermost server.

  Format
    .. code-block:: none

      platform server

platform team
----------------

  Description
    Commands to manage teams.

  Child Commands
    -  `platform team add`_ - Add users to a team
    -  `platform team create`_ - Create a team
    -  `platform team delete`_ - Delete a team
    -  `platform team remove`_ - Remove users from a team

platform team add
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Add users to a team.

  Format
    .. code-block:: none

      platform team add {team} {users}

  Example
    .. code-block:: none

      platform team add myteam user@example.com username

platform team create
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Create a team.

  Format
    .. code-block:: none

      platform team create

  Examples
    .. code-block:: none

      platform team create --name mynewteam --display_name "My New Team"
      platform teams create --name private --display_name "My New Private Team" --private

  Options
    .. code-block:: none

          --display_name string   Team Display Name
          --email string          Administrator Email (anyone with this email is automatically a team admin)
          --name string           Team Name
          --private               Create a private team.

platform team delete
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Permanently delete a team along with all related information, including posts from the database.

  Format
    .. code-block:: none

      platform team delete {teams}

  Example
    .. code-block:: none

      platform team delete myteam

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete the team and a DB backup has been performed.

platform team remove
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Remove users from a team.

  Format
    .. code-block:: none

      platform team remove {team} {users}

  Example
    .. code-block:: none

      platform team remove myteam user@example.com username

platform user
---------------

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
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Activate users that have been deactivated. If activating multiple users, use a space-separated list.

  Format
    .. code-block:: none

      platform user activate {emails, usernames, userIds}

  Examples
    .. code-block:: none

      platform user activate user@example.com
      platform user activate username1 username2

platform user create
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Create a user.

  Format
    .. code-block:: none

      platform user create

  Examples
    .. code-block:: none

      platform user create --email user@example.com --username userexample --password Password1 
      platform user create --firstname Joe --system_admin --email joe@example.com --username joe --password Password1

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
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Deactivate a user. Deactivated users are immediately logged out of all sessions and are unable to log back in.

  Format
    .. code-block:: none

      platform user deactivate {emails, usernames, userIds}

  Examples
    .. code-block:: none

      platform user deactivate user@example.com
      platform user deactivate username

platform user delete
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Permanently delete a user and all related information, including posts.

  Format
    .. code-block:: none

      platform user delete {users}

  Example
    .. code-block:: none

        platform user delete user@example.com

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete the user and a DB backup has been performed.

platform user deleteall
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Permanently delete all users and all related information, including posts.

  Format
    .. code-block:: none

      platform user deleteall

  Example
    .. code-block:: none

      platform user deleteall

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete the user and a DB backup has been performed.

platform user invite
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Send a user an email invite to a team. You can invite a user to multiple teams by listing the team names or team IDs.

  Format
    .. code-block:: none

      platform user invite {email} {teams}

  Examples
    .. code-block:: none

      platform user invite user@example.com myteam
      platform user invite user@example.com myteam1 myteam2

platform user migrate\_auth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Migrates all user accounts from one authentication provider to another. For example, you can upgrade your authentication provider from email to ldap. Output will display any accounts that are not migrated successfully.

    -  ``from_auth``: The authentication service from which to migrate user accounts. Supported options: ``email``, ``gitlab``, ``saml``.

    -  ``to_auth``: The authentication service to which to migrate user accounts. Supported options: ``ldap``.

    -  ``match_field``: The field that is guaranteed to be the same in both authentication services. For example, if the user emails are consistent set to email. Supported options: ``email``, ``username``.

  Format
    .. code-block:: none

      platform user migrate_auth {from_auth} {to_auth} {match_field}

  Example
    .. code-block:: none

      platform user migrate_auth email ladp email

platform user password
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Set a user's password.

  Format
    .. code-block:: none

      platform user password {user} {password}

  Example
    .. code-block:: none

      platform user password user@example.com Password1

platform user resetmfa
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Turns off multi-factor authentication for a user. If MFA enforcement is enabled, the user will be forced to re-enable MFA with a new device as soon as they log in.

  Format
    .. code-block:: none

      platform user resetmfa {users}

  Example
    .. code-block:: none

      platform user resetmfa user@example.com

platform user verify
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Verify the email address of a new user.

  Format
    .. code-block:: none

      platform user verify {users}

  Example
    .. code-block:: none

        platform user verify user1

platform version
------------------

  Description
    Displays Mattermost version information.

  Format
    .. code-block:: none

      platform version
=======
From the directory where the Mattermost platform is installed a ``platform`` command is available for configuring the system, including:

General Administration
----------------------

- Creating teams
- Creating users
- Assigning roles to users
- Reseting user passwords
- Inviting users to teams

Advanced Administration
-----------------------

- Permanently deleting users (use cautiously - database backup recommended before use)
- Permanently deleting teams (use cautiously - database backup recommended before use)

Advanced Automation
-------------------

`Available in Enterprise Edition E10 and higher`

- Creating channels
- Inviting users to channels
- Removing users from channels
- Listing all public channels and private groups for a team
- Restoring previously deleted channels
- Migrating sign-in options
- Resetting multi-factor authentication for a user

Using the CLI tool
-------------------

Typing ``platform -help`` brings up documentation for the CLI tool.

Notes:

- Parameters in CLI commands are order-specific.
- If special characters (``!``, ``|``, ``(``, ``)``, ``\``, `````, and ``"``) are used, the entire argument needs to be surrounded by single quotes (e.g. ``-password 'mypassword!'``, or the individual characters need to be escaped out (e.g. ``-password mypassword/!``).
- Team name and channel name refer to the handles, not the display names. So in the url ``https://pre-release.mattermost.com/core/channels/town-square`` team name would be ``core`` and channel name would be ``town-square``


.. tip :: If you automate user creation through the CLI tool with SMTP enabled emails will be sent to all new users created. If you run such a load script, it is best to disable SMTP or to use test accounts so that new account creation emails aren't unintentionally set to people at your organization who aren't expecting them.

CLI Documentation:

::

  Mattermost commands to help configure the system

  NAME:
      platform -- platform configuration tool

  USAGE:
      platform [options]

  FLAGS:
      -config="config.json"             Path to the config file

      -username="someuser"              Username used in other commands

      -license="ex.mattermost-license"  Path to your license file

      -email="user@example.com"         Email address used in other commands

      -password="mypassword"            Password used in other commands

      -team_name="name"                 The team name used in other commands

      -channel_name="name"	        The channel name used in other commands

      -channel_header="string"	        The channel header used in other commands

      -channel_purpose="string"	        The channel purpose used in other commands

      -channel_type="type"	        The channel type used in other commands
                                        valid values are
                                          "O" - public channel
                                          "P" - private group

      -role="system_admin"               The role used in other commands
                                         valid values are
                                           "" - The empty role is basic user
                                              permissions
                                           "system_admin" - Represents a system
                                              admin who has access to all teams
                                              and configuration settings.
  COMMANDS:
      -create_team                      Creates a team.  It requires the -team_name
                                        and -email flag to create a team.
          Example:
              platform -create_team -team_name="name" -email="user@example.com"

      -create_user                      Creates a user.  It requires the -email and -password flag,
                                         and -team_name and -username are optional to create a user.
          Example:
              platform -create_user -team_name="name" -email="user@example.com" -password="mypassword" -username="user"

      -invite_user                      Invites a user to a team by email. It requires the -team_name
                                          and -email flags.
          Example:
              platform -invite_user -team_name="name" -email="user@example.com"

      -join_team                        Joins a user to the team.  It requires the -email and
                                         -team_name flags.  You may need to logout of your current session
                                         for the new team to be applied.
          Example:
              platform -join_team -email="user@example.com" -team_name="name"

      -assign_role                      Assigns role to a user.  It requires the -role and
                                        -email flag.  You may need to log out
                                        of your current sessions for the new role to be
                                        applied.
          Example:
              platform -assign_role -email="user@example.com" -role="system_admin"

      -create_channel		        Create a new channel in the specified team. It requires the -email,
                                        -team_name, -channel_name, -channel_type flags. Optional you can set
                                        the -channel_header and -channel_purpose.
          Example:
              platform -create_channel -email="user@example.com" -team_name="name" -channel_name="channel_name" -channel_type="O"

      -join_channel                     Joins a user to the channel.  It requires the -email, -channel_name and
                                        -team_name flags.  You may need to logout of your current session
                                        for the new channel to be applied.  Requires an enterprise license.
          Example:
              platform -join_channel -email="user@example.com" -team_name="name" -channel_name="channel_name"

      -leave_channel                     Removes a user from the channel.  It requires the -email, -channel_name and
                                         -team_name flags.  You may need to logout of your current session
                                         for the channel to be removed.  Requires an enterprise license.
          Example:
              platform -leave_channel -email="user@example.com" -team_name="name" -channel_name="channel_name"

      -list_channels                     Lists all public channels and private groups for a given team.
                                         It will append ' (archived)' to the channel name if archived.  It requires the
                                         -team_name flag.  Requires an enterprise license.
          Example:
              platform -list_channels -team_name="name"

      -restore_channel                  Restores a previously deleted channel.
                                        It requires the -channel_name flag and
                                        -team_name flag.  Requires an enterprise license.
          Example:
              platform -restore_channel -team_name="name" -channel_name="channel_name"

      -reset_password                   Resets the password for a user.  It requires the
                                        -email and -password flag.
          Example:
              platform -reset_password -email="user@example.com" -password="newpassword"

      -reset_mfa                        Turns off multi-factor authentication for a user.  It requires the
                                        -email or -username flag.
          Example:
              platform -reset_mfa -username="someuser"

      -reset_database                   Completely erases the database causing the loss of all data. This
                                        will reset Mattermost to it's initial state. (note this will not
                                        erase your configuration.)

          Example:
              platform -reset_database

      -permanent_delete_user            Permanently deletes a user and all related information
                                        including posts from the database.  It requires the
                                        -email flag.  You may need to restart the
                                        server to invalidate the cache
          Example:
              platform -permanent_delete_user -email="user@example.com"

      -permanent_delete_all_users       Permanently deletes all users and all related information
                                        including posts from the database.  It requires the
                                        -team_name, and -email flag.  You may need to restart the
                                        server to invalidate the cache
          Example:
              platform -permanent_delete_all_users -team_name="name" -email="user@example.com"

      -permanent_delete_team            Permanently deletes a team along with
                                        all related information including posts from the database.
                                        It requires the -team_name flag.  You may need to restart
                                        the server to invalidate the cache.
          Example:
              platform -permanent_delete_team -team_name="name"

      -upload_license                   Uploads a license to the server. Requires the -license flag.

          Example:
              platform -upload_license -license="/path/to/license/example.mattermost-license"

      -migrate_accounts                 Migrates accounts from one authentication provider to another.
                                        Requires -from_auth -to_auth and -match_field flags. Supported
                                        options for -from_auth: email, gitlab, saml. Supported options
                                        for -to_auth: ldap. Supported options for -match_field: email,
                                        username. Output will display any accounts that are not migrated
                                        successfully.

          Example:
              platform -migrate_accounts -from_auth email -to_auth ldap -match_field username

      -upgrade_db_30                   Upgrades the database from a version 2.x schema to version 3 see
                                        http://www.mattermost.org/upgrading-to-mattermost-3-0/

          Example:
              platform -upgrade_db_30

      -version                          Display the current version of the Mattermost platform

      -help                             Displays this help page
