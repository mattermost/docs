Command Line Tools
==================

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

      -version                          Display the current of the Mattermost platform

      -help                             Displays this help page
