Command Line Tools
==================

From the directory where the Mattermost server is installed, a
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

-  Creating channels
-  Inviting users to channels
-  Removing users from channels
-  Listing all channels for a team
-  Restoring previously deleted channels
-  Modifying a channel's public/private type
-  Migrating sign-in options
-  Resetting multi-factor authentication for a user

.. contents::
    :backlinks: top
    :local:

Using the CLI
^^^^^^^^^^^^^

.. Isn't "-" the conventional second level indicator not "^"?

To run the CLI commands, you must be in the directory that contains the Mattermost executable. On a default install of Mattermost, the directory is ``/opt/mattermost/bin``. The name of the executable is ``platform``.

**For example, to get the Mattermost version on a default installation of Mattermost:**

  .. code-block:: bash

    cd /opt/mattermost/bin
    sudo ./platform version

Using the CLI on GitLab Omnibus
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On GitLab Omnibus, you must be in the following directory when you run CLI commands: ``/opt/gitlab/embedded/service/mattermost``. Also, you must run the commands as the user *mattermost* and specify the location of the configuration file. The executable is ``/opt/gitlab/embedded/bin/mattermost``.

**For example, to get the Mattermost version on GitLab Omnibus:**

  .. code-block:: bash

    cd /opt/gitlab/embedded/service/mattermost
    sudo -u mattermost /opt/gitlab/embedded/bin/mattermost ---config=/var/opt/gitlab/mattermost/config.json version

.. note::
  The example commands in the documentation are for a default installation of Mattermost. You must modify the commands so that they work on GitLab Omnibus.

Mattermost 3.6 and later
^^^^^^^^^^^^^^^^^^^^^^^^

The new CLI tool is supported in Mattermost 3.6 and later. To see available commands in the old CLI tool, see `Mattermost 3.5 and earlier`_.

.. Identify the commands that are enterprise-only.

Notes:

-  Parameters in CLI commands are order-specific.
-  If special characters (``!``, ``|``, ``(``, ``)``, ``\``, ``'``, and ``"``) are used, the entire argument needs to be surrounded by single quotes (e.g. ``-password 'mypassword!'``, or the individual characters need to be escaped out (e.g. ``-password mypassword\!``).
-  Team name and channel name refer to the handles, not the display names. So in the url ``https://pre-release.mattermost.com/core/channels/town-square`` team name would be ``core`` and channel name would be ``town-square``

.. Why a single dash with the password above? Don't you need a double dash with the "password" option?

.. tip::
   If you automate user creation through the CLI tool with SMTP enabled, emails will be sent to all new users created. If you run such a load script, it is best to disable SMTP or to use test accounts so that new account creation emails aren't unintentionally sent to people at your organization who aren't expecting them.

.. It looks like the last argument for a command can be a single item or a space-separated list of items. For example, 'channel add' takes two arguments, a channel and a user. The first argument is the channel and any successive argument is a user. This does not apply to commands that are naturally singular, such as the 'channel move' command. A channel can only be associated with one team, so can only move from a single team to one other team. If this is always true, it should be made clear in the introduction or perhaps every time multiple arguments apply. 
   
platform
--------

  Description
    Commands for configuring and managing your Mattermost instance and users. The ---config option is only required if your configuration file is not in the default location.

.. Is the --config option only required if your configuration file is not in the default location?

  Options
    .. code-block:: none

      -c, --config {string}   Configuration file to use. (default "config.json")

  Child Commands
    -  `platform channel`_ - Management of channels
    -  `platform command`_ - Management of slash commands
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
    -  `platform config`_ - Work with the configuration file

platform channel
-----------------

  Description
    Commands for channel management.

  Child Commands
    -  `platform channel add`_ - Add users to a channel
    -  `platform channel archive`_ - Archive a channel
    -  `platform channel create`_ - Create a channel
    -  `platform channel delete`_ - Delete a channel
    -  `platform channel list`_ - List all channels on specified teams
    -  `platform channel modify`_ - Modify a channel's public/private type
    -  `platform channel move`_ - Move a channel to another team
    -  `platform channel remove`_ - Remove users from a channel
    -  `platform channel restore`_ - Restore a channel from the archive

.. _channel-value-note:

.. note::
    **{channel} value**

    For the *add*, *archive*, *delete*, *move*, *remove* and *restore* commands, you can specfiy the *{channels}* value by *{team}:{channel}* using the team and channel URLs, or by using channel IDs. For example, in the following URL the *{channels}* value is *myteam:mychannel*:

    ``https://example.com/myteam/channels/mychannel``

.. Describe how to determine a channel ID. Using the 'channel list' command?

platform channel add
~~~~~~~~~~~~~~~~~~~~

  Description
    Add users to a channel. Use a space-separated list to add multiple users.
    This feature requires an enterprise license.

  .. Identify which enterprise version required for this command ('channel add'). E10? Add output if applicable.

  Format
    .. code-block:: none

      platform channel add {channel} {emails | usernames | userIds}
      
  .. Suggest using "|" to indicate 'or' in {emails | usernames | userIds}

  Examples
    .. code-block:: none

      sudo ./platform channel add 8soyabwthjnf9qibfztje5a36h user@example.com username
      sudo ./platform channel add myteam:mychannel user@example.com username


platform channel archive
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Archive a channel. Archived channels are not accessible to users, but remain in the database. To restore a channel from the archive, see `platform channel restore`_. Channels can be specified by {team}:{channel} using the team and channel names, or by using channel IDs. Use a space-separated list to specify multiple channels.

  .. warning:: Do not use this command with the community edition; the ``platform channel restore`` command is only available in the enterprise version.

  .. The 'channel archive' and the 'channel restore' commands should both be available or both unavailable in the community edition. I don't see a restore option in the web UI so you're introuble if you are using the community edition and archive a channel. 
  
  Format
    .. code-block:: none

      platform channel archive {channels}

  Examples
    .. code-block:: none

      sudo ./platform channel archive 8soyabwthjnf9qibfztje5a36h
      sudo ./platform channel archive myteam:mychannel

platform channel create
~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Create a channel. The ``---team`` and the ``---name`` options are required. This feature requires an enterprise license.

  .. Identify which enterprise version required for this command. E10? Add output. Also use CSS span styling when referencing required options.

  Format
    .. code-block:: none

     platform channel create

  Examples
    .. code-block:: none

      sudo ./platform channel create --team myteam --name mynewchannel --display_name "My New Channel"
      sudo ./platform channel create --team myteam --name mynewprivatechannel --display_name "My New Private Channel" --private

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
    Permanently delete a channel along with all related information, including posts from the database. Channels can be specified by {team}:{channel} using the team and channel names, or by using channel IDs. You must confirm or deny deletion.

    .. warning:: Deleting a channel permanently removes all related data.

  Format
    .. code-block:: none

      platform channel delete {channels}

  Examples
    .. code-block:: none

      sudo ./platform channel delete 8soyabwthjnf9qibfztje5a36h
      sudo ./platform channel delete myteam:mychannel

  Output
    .. code-block:: none

      Are you sure you want to delete the channels specified?
      All data will be permanently deleted? (YES/NO):


platform channel list
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    List all channels on a specified team. Archived channels are appended with ``(archived)``. This feature requires an enterprise license.

  .. Identify which enterprise version is required for the list command. E10? Add output.

  Format
    .. code-block:: none

      platform channel list {teams}

  Example
    .. code-block:: none

      sudo ./platform channel list myteam

  .. Put output for the 'channel list' command here.


platform channel modify
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Modify a channel's public/private type.

  .. This command won't execute (channel modify). It returns the error message "Error: unknown flag: --public [or --private]"

  Format
    .. code-block:: none

      platform channel modify {channel}

  Example
    .. code-block:: none

      sudo ./platform channel modify myteam:mychannel --private

  Options
    .. code-block:: none

          --public   Change a private channel to be public.
          --private  Change a public channel to be private.

platform channel move
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Move channels to another team. The command validates that all users in the channel belong to the target team. Incoming/Outgoing webhooks are moved along with the channel. Channels can be specified by ``[team]:[channel]`` or by using channel IDs.

  .. The 'channel move' command will not execute. Is it an enterprise only command?

  Format
    .. code-block:: none

      platform channel move {channel} {team}

  Example
    .. code-block:: none

      sudo ./platform channel move 8soyabwthjnf9qibfztje5a36h otherteam
      sudo ./platform channel move myteam:mychannel otherteam

platform channel remove
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Remove users from a channel. Channels can be specified by [team]:[channel] or by channel ID. Users can be specified by email address, username, or User ID. To specify multiple users, separate them using spaces. This feature requires an enterprise license.

  .. Identify which enterprise version required for 'channel remove'. E10? Add output if applicable.

  Format
    .. code-block:: none

      platform channel remove {channel} {emails | usernames | userIds}

  Examples
    .. code-block:: none

      sudo ./platform channel remove 8soyabwthjnf9qibfztje5a36h 
      user@example.com username
      sudo ./platform channel remove myteam:mychannel user@example.com username

platform channel restore
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Restore a channel from the archive. Channels can be specified by
    {team}:{channel} using the team and channel names, or by using channel IDs.
    This feature requires an enterprise license.

  .. Identify which enterprise version required for 'channel restore'. E10? Add output if applicable.

  Format
    .. code-block:: none

      platform channel restore {channels}

  Examples
    .. code-block:: none

      sudo ./platform channel restore 8soyabwthjnf9qibfztje5a36h
      sudo ./platform channel restore myteam:mychannel

platform command
-----------------

  Description
    Commands for slash command management.

  Child Commands
    -  `platform command move`_ - Move a slash command to a different team

platform command move
~~~~~~~~~~~~~~~~~~~~~~

  Description
    Move a slash command to a different team. Commands can be specified by {team}:{command-trigger-word}, or by using command IDs.

  Format
    .. code-block:: none

      platform command move

  Examples
    .. code-block:: none

      sudo ./platform command move newteam oldteam:command-trigger-word
      sudo ./platform channel move newteam o8soyabwthjnf9qibfztje5a36h

platform help
---------------

  Description
    Generate full documentation in Markdown format for the Mattermost command line tools.
    
  .. The help command generates documentation in Markdown format? Is this correct?

  Format
    .. code-block:: none

      platform help {outputdir}
      
  .. The platform help command has an 'outputdir' argument. What does this mean?

  Output
    .. code-block:: none
  
      Mattermost offers workplace messaging across web, PC and phones with
      archiving, search and integration with your existing systems.
      Documentation available at https://docs.mattermost.com
  
      Usage:
        platform [flags]
        platform [command]
  
      Available Commands:
        channel     Management of channels
        config      Configuration
        help        Help about any command
        import      Import data.
        jobserver   Start the Mattermost job server
        ldap        LDAP related utilities
        license     Licensing commands
        reset       Reset the database to initial state
        roles       Management of user roles
        server      Run the Mattermost server
        team        Management of teams
        user        Management of users
        version     Display version information
  
      Flags:
        -c, --config string        Configuration file to use. (default  "config.json")
            --disableconfigwatch   When set config.json will not be loaded from
            disk when the file is changed.
        -h, --help                 help for platform
  
      Use "platform [command] --help" for more information about a command.

platform import
----------------

  Description
    Import data into Mattermost.

  Child Command
    -  `platform import slack`_ - Import a team from Slack.

platform import slack
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Import a team from a Slack export zip file. For more information, see :ref:`migrating_from_slack`.

  Format
    .. code-block:: none

      platform import slack {team} {file}

  Example
    .. code-block:: none

      sudo ./platform import slack myteam slack_export.zip

platform ldap
-------------

  Description
    Commands to configure and synchronize LDAP.

  .. The 'ldap' command should reference the ss-ldap.md file. How do you reference a Markdown file? Is this command only available in the enterprise edition?

  Child Command
    -  `platform ldap sync`_ - Synchronize now

platform ldap sync
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Synchronize all LDAP users now.

  .. Is 'ldap sync' only available in the enterprise edition? Provide link to ss-ldap.md.

  Format
    .. code-block:: none

      platform ldap sync

  Example
    .. code-block:: none

      sudo ./platform ldap sync

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

      sudo ./platform license upload /path/to/license/mylicensefile.mattermost-license

platform reset
---------------

  Description
    Completely erase the database causing the loss of all data. This resets Mattermost to its initial state.

  .. warning:: This command removes all data from your database.

  Format
    .. code-block:: none

      platform reset

  Options
    .. code-block:: none

      --confirm   Confirm you really want to delete everything and a DB backup has been performed.
      
    .. This option (reset --confirm) does not seem to work--you are not asked to confirm. It just goes ahead and wipes out the database. Remove this option until it is implemented/fixed?

platform roles
---------------

  Description
    Commands to manage user roles. The user can be specified by a username, an email a user ID. Use a space-separated list to specify multiple users.

  Child Commands
    -  `platform roles member`_ - Remove System Admin privileges from a user
    -  `platform roles system_admin`_ - Make a user into a System Admin

platform roles member
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Remove system admin privileges from a user.

  Format
    .. code-block:: none

      platform roles member {emails | usernames | userIds}

  Example
    .. code-block:: none

      sudo ./platform roles member user1

platform roles system\_admin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Promote a user or a number of users to System Admin.

  Format
    .. code-block:: none

      platform roles system_admin {emails | usernames | userIds}

  Example
    .. code-block:: none

      sudo ./platform roles system_admin user1

platform server
----------------

  Description
    Runs the Mattermost server.

    .. How does 'platform server' differ from running the 'platform' command? 

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

.. _team-value-note:

.. note::
    **{team-name} value**

    For the *add*, *delete*, and *remove* commands, you can determine the *{team-name}* value from the URLs that you use to access your instance of Mattermost. For example, in the following URL the *{team-name}* value is *myteam*:

    ``https://example.com/myteam/channels/mychannel``

platform team add
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Add users to a team. Use a space-separated list to add multiple users. Before running this command, see the :ref:`note about {team-name} <team-value-note>`.

  Format
    .. code-block:: none

      platform team add {team-name} {emails | usernames | userIds}

  Example
    .. code-block:: none

      sudo ./platform team add myteam user@example.com username

platform team create
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Create a team. The ``---display_name`` and ``---name`` options are required.

  Format
    .. code-block:: none

      platform team create

  Examples
    .. code-block:: none

      sudo ./platform team create --name mynewteam --display_name "My New Team"
      sudo ./platform teams create --name private --display_name "My New Private Team" --private

  Options
    .. code-block:: none

          --display_name string   Team Display Name
          --email string          Administrator Email (anyone with this email is automatically a team admin)
          --name string           Team Name
          --private               Create a private team.

platform team delete
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Permanently delete a team along with all related information, including posts from the database. Before running this command, see the :ref:`note about {team-name} <team-value-note>`.
    
  .. warning:: Deleting a team permanently removes the team and all team-related data.

  Format
    .. code-block:: none

      platform team delete {team-name}

  Example
    .. code-block:: none

      sudo ./platform team delete myteam

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete the team and a DB backup has been performed.
          
  .. When deleting a team, the --confirm option doesn't do anything. Remove documentation of this option?

platform team remove
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Remove users from a team. Use a space-separated list to remove multiple users. Before running this command, see the :ref:`note about {team-name} <team-value-note>`.

  Format
    .. code-block:: none

      platform team remove {team-name} {emails | usernames | userIds}

  Example
    .. code-block:: none

      sudo ./platform team remove myteam user@example.com username

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
    -  `platform user search`_ - Search for users based on username, email, or user ID
    -  `platform user verify`_ - Verify email address of a new user

platform user activate
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Activate users that have been deactivated. If activating multiple users, use a space-separated list.

  Format
    .. code-block:: none

      platform user activate {emails | usernames | userIds}

  Examples
    .. code-block:: none

      sudo ./platform user activate user@example.com
      sudo ./platform user activate username1 username2

platform user create
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Create a user. The ``--username``, ``---password``, and ``---email`` options are required.

  Format
    .. code-block:: none

      platform user create

  Examples
    .. code-block:: none

      sudo ./platform user create --email user@example.com --username userexample --password Password1
      sudo ./platform user create --firstname Joe --system_admin --email joe@example.com --username joe --password Password1

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
    Deactivate a user. Use a space-separated list to deactivate multiple users. Deactivated users are immediately logged out of all sessions and are unable to log back in.

  Format
    .. code-block:: none

      platform user deactivate {emails | usernames | userIds}

  Examples
    .. code-block:: none

      sudo ./platform user deactivate user@example.com
      sudo ./platform user deactivate username

platform user delete
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Permanently delete a user and all related information, including posts. Use a space-separated list to delete multiple users.
    
  .. warning:: Deleting a user permanently removes the user and all related data.

  Format
    .. code-block:: none

      platform user delete {emails | usernames | userIds}

  Example
    .. code-block:: none

      sudo ./platform user delete user@example.com

  Options
    .. code-block:: none

        --confirm   Confirm you really want to delete the user and a DB backup has been performed.
          
  .. The --confirm option doesn't seem to do anything when used with the user delete command. Remove documentation of this option?

platform user deleteall
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Permanently delete all users and all related information, including posts. After executing this command you will not be able to log in to the web UI until you create new users. Use the `platform user create`_ command. If you do not specify the ``-system_admin`` option, the first user that you create will be a system adminstrator.
    
  .. warning:: This command removes all users and their data.

  Format
    .. code-block:: none

      platform user deleteall

  Example
    .. code-block:: none

      sudo ./platform user deleteall

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete the user and a DB backup has been performed.
          
  .. The --confirm option doesn't seem to do anything when used with the user delete command. Remove documentation of this option?

platform user invite
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Send a user an email invite to a team. You can invite a user to multiple teams by listing the team names or team IDs.
    
  .. How do you determine a team ID? 

  Format
    .. code-block:: none

      platform user invite {email} {teams}

  Examples
    .. code-block:: none

      sudo ./platform user invite user@example.com myteam
      sudo ./platform user invite user@example.com myteam1 myteam2

platform user migrate\_auth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Migrates all user accounts from one authentication provider to another. For example, you can upgrade your authentication provider from email to LDAP. Output will display any accounts that are not migrated successfully.

    -  ``from_auth``: The authentication service from which to migrate user accounts. Supported options: ``email``, ``gitlab``, ``saml``.

    -  ``to_auth``: The authentication service to which to migrate user accounts. Supported options: ``ldap``.

    -  ``match_field``: The field that is guaranteed to be the same in both authentication services. For example, if the user emails are consistent set to email. Supported options: ``email``, ``username``.

  Format
    .. code-block:: none

      platform user migrate_auth {from_auth} {to_auth} {match_field}

  Example
    .. code-block:: none

      sudo ./platform user migrate_auth email ladp email
  Options
    .. code-block:: none

      --force  Ignore duplicate entries on the LDAP server.

platform user password
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Set a user's password.

  Format
    .. code-block:: none

      platform user password {email | username | userId} {password}

  Example
    .. code-block:: none

      sudo ./platform user password user@example.com Password1

platform user resetmfa
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Turns off multi-factor authentication for a user. If MFA enforcement is enabled, the user will be forced to re-enable MFA with a new device as soon as they log in.

  Format
    .. code-block:: none

      platform user resetmfa {emails | usernames | userIds}

  Example
    .. code-block:: none

      sudo ./platform user resetmfa user@example.com

platform user search
~~~~~~~~~~~~~~~~~~~~

  Description
    Search for users based on username, email, or user ID.

  Format
    .. code-block:: none

      platform user search {email | username | userId}

  Example
    .. code-block:: none

      sudo ./platform user search user1@example.com user2@example.com
      
  Output
    .. code-block:: none
      
      id: pthktognwpyw7q1w851swcf39c
      username: thomas
      nickname: tom
      position: 
      first_name: thomas
      last_name: piperson
      email: tom@example.com
      auth_service: 

platform user verify
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Verify the email address of a new user.
    
  .. What does 'verify' mean in this context ('user verify')? Just the format of the email address? Not that the address exists?

  Format
    .. code-block:: none

      platform user verify {email | username | userId}

  Example
    .. code-block:: none

      sudo ./platform user verify user1

platform version
------------------

  Description
    Displays Mattermost version information.

  Format
    .. code-block:: none

      platform version
      
  Output
    .. code-block:: none
    
      Version: 4.1.0
      Build Number: 4.1.0
      Build Date: Tue Aug 15 22:11:43 UTC 2017
      Build Hash: 0033e3e37b12cb5d951d21492500d66a6abc472b
      Build Enterprise Ready: true
      DB Version: 4.1.0

platform config
---------------

  Description
    Commands for managing the configuration file.

  Child Command
    - `platform config validate`_ - Validate the configuration file.

platform config validate
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Makes sure the configuration file has the following properties:

    - Is valid JSON.
    - Has attributes of the correct type, such as *bool*, *int*, and *str*.
    - All entries are valid. For example, checks that entries are below the maximum length.
    
    If the configuration file is valid, you will see the message: ``The document is valid``

    Format
      .. code-block:: none

        platform config validate

    Example
      .. code-block:: none

        sudo ./platform config validate

Mattermost 3.5 and earlier
^^^^^^^^^^^^^^^^^^^^^^^^^^

Typing ``sudo ./platform -help`` brings up documentation for the CLI tool. To return the help documentation in GitLab omnibus, type

    .. code-block:: none

      sudo -u mattermost /opt/gitlab/embedded/bin/mattermost --config=/var/opt/gitlab/mattermost/config.json -help

Notes:

- Parameters in CLI commands are order-specific.
- If special characters (``!``, ``|``, ``(``, ``)``, ``\``, `````, and ``"``) are used, the entire argument needs to be surrounded by single quotes (e.g. ``-password 'mypassword!'``, or the individual characters need to be escaped out (e.g. ``-password mypassword\!``).
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
                                          "P" - private channel

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

      -list_channels                     Lists all channels for a given team.
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
