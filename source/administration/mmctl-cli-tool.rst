MMCTL Command Line Tool (Beta)
==============================

The MMCTL tool is a remote CLI tool for Mattermost which is installed locally and uses the Mattermost API. Authentication
is done ith either login credentials or an authentication token.

Being installed locally allows a System Admin to run CLI commands even in instances where there is no access to the
server (e.g., via SSH).

This tool is in beta and can be used alongside the Mattermost CLI tool. In the future, the Mattermost CLI tool will be
deprecated.

Installing MMCTL
----------------

To install the project in your `$GOPATH`, simply run:

.. code-block:: bash

   go get -u github.com/mattermost/mmctl

Installing Shell Completions
^^^^^^^^^^^^^^^^^^^^^^^^^^

To install the shell completions for bash, add the following line to your `~/.bashrc` or `~/.profile` file:

.. code-block:: sh

   source <(mmctl completion bash)

For zsh, add the following line to your `~/.zshrc` file:

.. code-block:: sh

  source <(mmctl completion zsh)

Compiling
^^^^^^^^^

First we have to install the dependencies of the project. `mmctl` uses `go` modules to manage the dependencies, so you need to have installed
`go` 1.11 or greater. We can compile the binary with:

.. code-block:: sh

  make build


Logging In
----------

First we have to log into a mattermost instance:

  ```sh
  $ mmctl auth login https://my-instance.example.com --name my-instance --username john.doe --password mysupersecret

    credentials for my-instance: john.doe@https://my-instance.example.com stored

  ```

  We can check the currently stored credentials with:

  ```sh
  $ mmctl auth list

      | Active |        Name | Username |                     InstanceUrl |
      |--------|-------------|----------|---------------------------------|
      |      * | my-instance | john.doe | https://my-instance.example.com |

  ```

  And now we can run commands normally:

  ```sh
  $ mmctl user search john.doe
  id: qykfw3t933y38k57ubct77iu9c
  username: john.doe
  nickname:
  position:
  first_name: John
  last_name: Doe
  email: john.doe@example.com
  auth_service:
  ```

  ## Login methods

  ### Password

  ```sh
  $ mmctl auth login https://community.mattermost.com --name community --username my-username --password mysupersecret
  ```

  The `login` command can also work interactively, so if you leave any
  needed flag empty, `mmctl` will ask you for it interactively:

  ```sh
  $ mmctl auth login https://community.mattermost.com
  Connection name: community
  Username: my-username
  Password:
  ```

  ### MFA

  If you want to login with MFA, you just need to use the `--mfa-token`
  flag:

  ```sh
  $ mmctl auth login https://community.mattermost.com --name community --username my-username --password mysupersecret --mfa-token 123456
  ```

  ### Access tokens

  Instead of using username and password to log in, you can generate and
  use a personal access token to authenticate with a server:

  ```sh
  $ mmctl auth login https://community.mattermost.com --name community --access-token MY_ACCESS_TOKEN
  ```

Using MMCTL
-----------

For the usage of all the commands, use the `--help` flag or check [the tool's documentation](./docs/mmctl.md).

.. code-block:: sh

   Mattermost offers workplace messaging across web, PC and phones with archiving, search and integration with your existing systems. Documentation available at https://docs.mattermost.com

   Usage:
      mmctl [command]

      Available Commands:
        auth        Manages the credentials of the remote Mattermost instances
        channel     Management of channels
        completion  Generates autocompletion scripts for bash and zsh
        group       Management of groups
        help        Help about any command
        license     Licensing commands
        logs        Display logs in a human-readable format
        permissions Management of permissions and roles
        plugin      Management of plugins
        post        Management of posts
        team        Management of teams
        user        Management of users
        websocket   Display websocket in a human-readable format

    Flags:
        -h, --help   help for mmctl

    Use "mmctl [command] --help" for more information about a command.

**Channel Administration**

mmctl channel
------------------

  Description
    Commands for channel management.

  Child Commands
    -  `mmctl channel create`_ - Create a channel
    -  `mmctl channel add`_ - Delete a channel
    -  `mmctl channel archive`_ - Archive a channel
    -  `mmctl channel list`_ - List all channels on specified teams
    -  `mmctl channel move`_ - Move a channel to another team
    -  `mmctl channel remove`_ - Remove users from a channel
    -  `mmctl channel rename`_ - Rename a channel
    -  `mmctl channel restore`_ - Restore a channel from the archive
    -  `mmctl make_private`_ - Set a channel's type to "private"
    -  `mattermost channel search`_ -  Search a channel by name

.. _channel-value-note:

.. note::
    **{channel} value**

    For the *add*, *archive*, *delete*, *remove* and *restore* commands, you can specfiy the *{channels}* value by {team}:{channel} using the team and channel URLs, or by using channel IDs. For example, in the following URL the *{channels}* value is *myteam:mychannel*:

    ``https://example.com/myteam/channels/mychannel``

    Also, the team and channel names in the URL should be written in lowercase.


add
---

archive
-------

create
------

list
----

modify
------

make
----

move
----

remove
------

rename
------

restore
-------

search
------

.. contents::
    :backlinks: top
    :local:

Using the CLI
^^^^^^^^^^^^^

Notes:

-  Parameters in CLI commands are order-specific.
-  If special characters (``!``, ``|``, ``(``, ``)``, ``\``, ``'``, and ``"``) are used, the entire argument needs to be surrounded by single quotes (e.g. ``-password 'mypassword!'``, or the individual characters need to be escaped out (e.g. ``-password mypassword\!``).
-  Team name and channel name refer to the handles, not the display names. So in the url ``https://community.mattermost.com/core/channels/town-square`` team name would be ``core`` and channel name would be ``town-square``

.. tip::
   If you automate user creation through the CLI tool with SMTP enabled, emails will be sent to all new users created. If you run such a load script, it is best to disable SMTP or to use test accounts so that new account creation emails aren't unintentionally sent to people at your organization who aren't expecting them.

mattermost
----------

  Description
    Commands for configuring and managing your Mattermost instance and users.

  Options
    .. code-block:: none

      -c, --config {string}   Configuration file to use. (default "config.json")
      --disableconfigwatch {boolean}  When true, the config.json file will not be reloaded automatically when another process changes it (default "false")

  Child Commands
    -  `mattermost channel`_ - Management of channels
    -  `mattermost command`_ - Management of slash commands
    -  `mattermost config`_ - Work with the configuration file
    -  `mattermost export`_ - Compliance export commands
    -  `mattermost group`_ - Management of Mattermost groups
    -  `mattermost help`_ - Generate full documentation for the CLI
    -  `mattermost import`_ - Import data
    -  `mattermost jobserver`_ - Start the Mattermost job server
    -  `mattermost ldap`_ - AD/LDAP related utilities
    -  `mattermost license`_ - Licensing commands
    -  `mattermost logs`_ - Display human-readable logs
    -  `mattermost permissions`_ - Management of the permissions system
    -  `mattermost plugin`_ - Management of plugins
    -  `mattermost reset`_ - Reset the database to initial state
    -  `mattermost roles`_ - Management of user roles
    -  `mattermost sampledata`_ - Sample data generation
    -  `mattermost server`_ - Run the Mattermost server
    -  `mattermost team`_ - Management of teams
    -  `mattermost user`_ - Management of users
    -  `mattermost version`_ - Display version information
    -  `mattermost webhook`_ - Management of webhooks

mattermost channel
------------------

  Description
    Commands for channel management.

  Child Commands
    -  `mattermost channel add`_ - Add users to a channel
    -  `mattermost channel archive`_ - Archive a channel
    -  `mattermost channel create`_ - Create a channel
    -  `mattermost channel delete`_ - Delete a channel
    -  `mattermost channel list`_ - List all channels on specified teams
    -  `mattermost channel modify`_ - Modify a channel's public/private type
    -  `mattermost channel move`_ - Move a channel to another team
    -  `mattermost channel remove`_ - Remove users from a channel
    -  `mattermost channel rename`_ - Rename a channel
    -  `mattermost channel restore`_ - Restore a channel from the archive
    -  `mattermost channel search`_ -  Search a channel by name

.. _channel-value-note:

.. note::
    **{channel} value**

    For the *add*, *archive*, *delete*, *remove* and *restore* commands, you can specfiy the *{channels}* value by {team}:{channel} using the team and channel URLs, or by using channel IDs. For example, in the following URL the *{channels}* value is *myteam:mychannel*:

    ``https://example.com/myteam/channels/mychannel``

    Also, the team and channel names in the URL should be written in lowercase.

mattermost channel add
~~~~~~~~~~~~~~~~~~~~~~

  Description
    Add users to a channel. If adding multiple users, use a space-separated list.

  Format
    .. code-block:: none

      mattermost channel add {channel} {users}

  Examples
    .. code-block:: none

      ./mattermost channel add 8soyabwthjnf9qibfztje5a36h user@example.com username
      ./mattermost channel add myteam:mychannel user@example.com username

Notes:

- Parameters in CLI commands are order-specific.
- If special characters (``!``, ``|``, ``(``, ``)``, ``\``, `````, and ``"``) are used, the entire argument needs to be surrounded by single quotes (e.g. ``-password 'mypassword!'``, or the individual characters need to be escaped out (e.g. ``-password mypassword\!``).
- Team name and channel name refer to the handles, not the display names. So in the url ``https://community.mattermost.com/core/channels/town-square`` team name would be ``core`` and channel name would be ``town-square``

.. tip :: If you automate user creation through the CLI tool with SMTP enabled, emails will be sent to all new users created. If you run such a load script, it is best to disable SMTP or to use test accounts so that new account creation emails aren't unintentionally sent to people at your organization who aren't expecting them.

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
