# Command Line Tools

From the directory where the Mattermost platform is installed a `platform` command is available for configuring the system, including: 

- Creating teams
- Creating users
- Inviting users
- Assigning roles to users 
- Reseting user passwords
- Permanently deleting users (use cautiously - database backup recommended before use)
- Permanently deleting teams (use cautiously - database backup recommended before use)

Typing `platform -help` brings up the below documentation on usage. 


```
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

    -join_team                        Joins a user to the team.  It required the -email and
                                       -team_name.  You may need to logout of your current session
                                       for the new team to be applied.
        Example:
            platform -join_team -email="user@example.com" -team_name="name"

    -assign_role                      Assigns role to a user.  It requires the -role and
                                      -email flag.  You may need to log out
                                      of your current sessions for the new role to be
                                      applied.
        Example:
            platform -assign_role -email="user@example.com" -role="system_admin"

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

    -upgrade_db_30                   Upgrades the database from a version 2.x schema to version 3 see
                                      http://www.mattermost.org/upgrading-to-mattermost-3-0/

        Example:
            platform -upgrade_db_30

    -version                          Display the current of the Mattermost platform

    -help                             Displays this help page
```
