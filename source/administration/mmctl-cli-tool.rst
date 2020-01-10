mmctl Command Line Tool (Beta)
==============================

The mmctl tool is a remote CLI tool for Mattermost which is installed locally and uses the Mattermost API. Authentication
is done with either login credentials or an authentication token.

Being installed locally allows a System Admin to run CLI commands even in instances where there is no access to the
server (e.g., via SSH). This tool is currently in beta and can be used alongside the Mattermost CLI tool.
In the future, the Mattermost CLI tool will be deprecated.

**Notes**

-  Parameters in CLI commands are order-specific.
-  If special characters (``!``, ``|``, ``(``, ``)``, ``\``, ``'``, and ``"``) are used, the entire argument needs to be surrounded by single quotes (e.g. ``-password 'mypassword!'``, or the individual characters need to be escaped out (e.g. `` password mypassword\!``).
- Team name and channel name refer to the handles, not the display names. So in the URL ``https://community.mattermost.com/core/channels/town-square`` team name would be ``core`` and channel name would be ``town-square``.


**Options**

.. code-block:: sh

       --format string    the format of the command output [plain, json] (default "plain")
       -h, --help         help for mmctl

**Commands**

   - `mmctl channel`_ - Channel Management
   - `mmctl command`_ - Command Management
   - `mmctl config`_ - Configuration Management
   - `mmctl group`_ - Group Management
   - `mmctl ldap`_ - LDAP Management
   - `mmctl license`_ - License Management
   - `mmctl logs`_ - Log Management
   - `mmctl permissions`_ - Permissions Management
   - `mmctl plugin`_ - Plugin Management
   - `mmctl post`_ - Post Management
   - `mmctl roles`_ - Roles Management
   - `mmctl team`_ - Team Management
   - `mmctl user`_ - User Management
   - `mmctl version`_ - Version Management
   - `mmctl webhook`_ - Webhook Management


Installing mmctl
----------------

To install the project in your `$GOPATH` run the following command as admin user:

.. code-block:: sh

   go get -u github.com/mattermost/mmctl

The ``mmctl`` tool uses ``go`` modules to manage dependencies, so you need to have installed
``go`` 1.11 or greater and compile the binary using:

.. code-block:: sh

  make build


Authenticating and Logging In
-----------------------------

mmctl auth
^^^^^^^^^^

**Description**

  Manages the credentials and authentication methods of the remote Mattermost instances.

  -  `mmctl auth clean`_ - Clean credentials
  -  `mmctl auth current`_ - Display current credentials
  -  `mmctl auth delete`_ - Delete authentication details
  -  `mmctl auth list`_ - List registered credentials
  -  `mmctl auth login`_ - Log into Mattermost instance
  -  `mmctl auth renew`_ - Renew login credentials
  -  `mmctl auth set`_ - Set login credentials

**Options**

.. code-block:: sh

  -h, --help   help for auth

mmctl auth clean
^^^^^^^^^^^^^^^^^

**Description**

  Clean the credentials associated with a Mattermost instance.

**Format**

.. code-block:: sh

   mmctl auth clean [flags]

**Examples**

.. code-block:: sh

   auth clean

**Options**

.. code-block:: sh

  -h, --help   help for clean

**Options Inherited from Parent Commands**

.. code-block:: sh

   --format string the format of the command output [plain, json] (default "plain")


mmctl auth current
^^^^^^^^^^^^^^^^^

**Description**

  Show the currently stored user credentials.

**Format**

.. code-block:: sh

   mmctl auth current [flags]

**Examples**

.. code-block:: sh

   auth current

**Options**

.. code-block:: sh

     -h, --help   help for current

**Options Inherited from Parent Commands**

.. code-block:: sh

   --format string the format of the command output [plain, json] (default "plain")


mmctl auth delete
^^^^^^^^^^^^^^^^^

**Description**

  Delete a named credential.

**Format**

.. code-block:: sh

   mmctl auth delete [server name] [flags]

**Examples**

.. code-block:: sh

   auth delete local-server

**Options**

.. code-block:: sh

     -h, --help   help for delete

**Options Inherited from Parent Commands**

.. code-block:: sh

   --format string the format of the command output [plain, json] (default "plain")

mmctl auth list
^^^^^^^^^^^^^^^^^

**Description**

  Print a list of registered credentials.

**Format**

.. code-block:: sh

   mmctl auth list [flags]

**Examples**

.. code-block:: sh

   auth list

**Options**

.. code-block:: sh

     -h, --help   help for list

**Options Inherited from Parent Commands**

.. code-block:: sh

   --format string the format of the command output [plain, json] (default "plain")

mmctl auth login
^^^^^^^^^^^^^^^^^

**Description**

  Log in to an instance and store credentials.

**Format**

.. code-block:: sh

   mmctl auth login [instance url] --name [server name] --username [username] --password [password] [flags]

**Examples**

.. code-block:: sh

  auth login https://mattermost.example.com
  auth login https://mattermost.example.com --name local-server --username sysadmin --password mysupersecret
  auth login https://mattermost.example.com --name local-server --username sysadmin --password mysupersecret --mfa-token 123456
  auth login https://mattermost.example.com --name local-server --access-token myaccesstoken

**Options**

.. code-block:: sh

  -a, --access-token string   Access token to use instead of username/password
  -h, --help                  help for login
  -m, --mfa-token string      MFA token for the credentials
  -n, --name string           Name for the credentials
  --no-activate               If present, it won't activate the credentials after login
  -p, --password string       Password for the credentials
  -u, --username string       Username for the credentials

**Options Inherited from Parent Commands**

.. code-block:: sh

   --format string the format of the command output [plain, json] (default "plain")

mmctl auth renew
^^^^^^^^^^^^^^^^^

**Description**

  Renew the credentials for a given server.

**Format**

.. code-block:: sh

   mmctl auth renew [flags]

**Examples**

.. code-block:: sh

   auth renew local-server

**Options**

.. code-block:: sh

  -a, --access-token string   Access token to use instead of username/password
  -h, --help                  help for renew
  -m, --mfa-token string      MFA token for the credentials
  -p, --password string       Password for the credentials

Options Inherited from Parent Commands

.. code-block:: sh

   --format string the format of the command output [plain, json] (default "plain")

mmctl auth set
^^^^^^^^^^^^^^^^^

**Description**

  Set credentials to use in the following commands.

**Format**

.. code-block:: sh

   mmctl auth set [server name] [flags]

**Examples**

.. code-block:: sh

   auth set local-server

**Options**

.. code-block:: sh

   -h, --help   help for set

**Options Inherited from Parent Commands**

.. code-block:: sh

   --format string the format of the command output [plain, json] (default "plain")


Authenticate to a server (e.g. >mmctl auth login https://test.mattermost.com). Then username and password
(and MFA token if MFA is enabled on the account).

Password

.. code-block:: sh

     $ mmctl auth login https://community.mattermost.com --name community --username my-username --password mysupersecret

The ``login`` command can also work interactively, so if you leave any required flag empty, ``mmctl`` will ask you for it interactively:

.. code-block:: sh

    $ mmctl auth login https://community.mattermost.com
    Connection name: community
    Username: my-username
    Password:

MFA

To log in with MFA, use the ``--mfa-token`` flag:

.. code-block:: sh

   $ mmctl auth login https://community.mattermost.com --name community --username my-username --password mysupersecret --mfa-token 123456

Access Tokens
^^^^^^^^^^^^^

You can generate and use a personal access token to authenticate with a server, instead of using username and password to log in:

.. code-block:: sh

   $ mmctl auth login https://community.mattermost.com --name community --access-token MY_ACCESS_TOKEN


into a Mattermost instance:

.. code-block:: sh

     $ mmctl auth login https://my-instance.example.com --name my-instance --username john.doe --password mysupersecret
     credentials for my-instance: john.doe@https://my-instance.example.com stored

We can check the currently stored credentials with:

.. code-block:: sh

    $ mmctl auth list

    | Active |        Name | Username |                     InstanceUrl |
    |--------|-------------|----------|---------------------------------|
    |      * | my-instance | john.doe | https://my-instance.example.com |


And now we can run commands normally:

.. code-block:: sh

   $ mmctl user search john.doe
   id: qykfw3t933y38k57ubct77iu9c
   username: john.doe
   nickname:
   position:
   first_name: John
   last_name: Doe
   email: john.doe@example.com
   auth_service:


Installing Shell Completions
^^^^^^^^^^^^^^^^^^^^^^^^^^

To install the shell completions for bash, add the following line to your ``~/.bashrc`` or ``~/.profile`` file:

.. code-block:: sh

  source <(mmctl completion bash)

For zsh, add the following line to your ``~/.zshrc`` file:

.. code-block:: sh

  source <(mmctl completion zsh)


mmctl channel
--------------

Commands for channel management.

  Child Commands
    -  `mmctl channel add`_ - Add a channel
    -  `mmctl channel archive`_ - Archive a channel
    -  `mmctl channel create`_ - Create a channel
    -  `mmctl channel list`_ - List all channels on specified teams
    -  `mmctl channel make_private`_ - Set a channel's type to "private"
    -  `mmctl channel make`_ - Make a channel
    -  `mmctl channel modify`_ - Modify all channels
    -  `mmctl channel move`_ - Move a channel to another team
    -  `mmctl channel remove`_ - Remove users from a channel
    -  `mmctl channel rename`_ - Rename a channel
    -  `mmctl channel restore`_ - Restore a channel from the archive
    -  `mmctl channel search`_ - Search a channel by name

**Options**

.. code-block:: sh

   -h, --help   help for channel

mmctl channel add
^^^^^^^^^^^^^^^^^

**Description**

  Add users to a channel. If adding multiple users, use a space-separated list.

**Format**

.. code-block:: sh

   mmctl channel add [channel] [users] [flags]

**Examples**

.. code-block:: sh

   channel add myteam:mychannel user@example.com username

**Options**

 .. code-block:: sh

  -h, --help   help for add

**Options Inherited from Parent Commands**

.. code-block:: sh

   --format string the format of the command output [plain, json] (default "plain")

mmctl channel archive
^^^^^^^^^^^^^^^^^^^^

**Description**

  Archive one or multiple channels along with all related information including posts from the database. Channels can be
  specified by ``[team]:[channel]`` (i.e., myteam:mychannel) or by channel ID).

**Format**

.. code-block:: sh

   mmctl channel archive [channels] [flags]

**Examples**

.. code-block:: sh

   channel archive myteam:mychannel

**Options**

.. code-block:: sh

   -h, --help   help for archive

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl channel create
^^^^^^^^^^^^^^^^^

**Description**

  Create a channel.

**Format**

.. code-block:: sh

   mmctl channel create [flags]

**Examples**

.. code-block:: sh

  channel create --team myteam --name mynewchannel --display_name "My New Channel"
  channel create --team myteam --name mynewprivatechannel --display_name "My New Private Channel" --private

**Options**

.. code-block:: sh

    --display_name string   Channel Display Name
    --header string         Channel header
    -h, --help              help for create
    --name string           Channel Name
    --private               Create a private channel
    --purpose string        Channel purpose
    --team string           Team name or ID

**Options Inherited from Parent Commands**

.. code-block:: sh

   --format string   the format of the command output [plain, json] (default "plain")

mmctl channel list
^^^^^^^^^^^^^^^^^

**Description**

  List all channels on specified teams. Archived channels are appended with '(archived)'.

**Format**

.. code-block:: sh

   mmctl channel list [teams] [flags]

**Examples**

.. code-block:: sh

  channel list myteam

**Options**

.. code-block:: sh

  -h, --help   help for list


**Options Inherited from Parent Commands**

.. code-block:: sh

   --format string   the format of the command output [plain, json] (default "plain")

mmctl channel make_private
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Description**

   Set the type of a channel from public to private. Channel can be specified by ``[team]:[channel]`` (i.e., myteam:mychannel)
   or by channel ID.

**Format**

.. code-block:: sh

    mmctl channel make_private [channel] [flags]

**Examples**

.. code-block:: sh

    channel make_private myteam:mychannel

**Options**

.. code-block:: sh

  -h, --help   help for make_private

**Options Inherited from Parent Commands**

.. code-block:: sh

 --format string   the format of the command output [plain, json] (default "plain")


mmctl channel make
^^^^^^^^^^^^^^^^^

 *In progress*

mmctl channel modify
^^^^^^^^^^^^^^^^^

*In progress*

mmctl channel move
^^^^^^^^^^^^^^^^^

*In progress*

mmctl channel remove
^^^^^^^^^^^^^^^^^

**Description**

  Remove specified users from a channel.

**Format**

.. code-block:: sh

   mmctl channel remove [channel] [users] [flags]

**Examples**

.. code-block:: sh

  channel remove myteam:mychannel user@example.com username
  channel remove myteam:mychannel --all-users

**Options**

.. code-block:: sh

  --all-users   Remove all users from the indicated channel
  -h, --help    help for remove

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl channel rename
^^^^^^^^^^^^^^^^^^^

**Description**

  Rename a channel.

**Format**

.. code-block:: sh

   mmctl channel rename [flags]

**Examples**

.. code-block:: sh

   channel rename myteam:mychannel newchannelname --display_name "New Display Name"

**Options**

.. code-block:: sh

  --display_name string   Channel Display Name
  -h, --help              help for rename

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl channel restore
^^^^^^^^^^^^^^^^^^^^^

**Description**

  Restore a previously deleted channel. Channels can be specified by ``[team]:[channel]`` (e.g., myteam:mychannel) or by channel ID.

**Format**

.. code-block:: sh

   mmctl channel restore [channels] [flags]

**Examples**

.. code-block:: sh

   channel restore myteam:mychannel

**Options**

.. code-block:: sh

   -h, --help   help for restore

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")


mmctl channel search
^^^^^^^^^^^^^^^^^^^^^

**Description**

  Search a channel by channel name. Channel can be specified by team (e.g., ``--team myTeam myChannel```) or by team ID.

**Format**

.. code-block:: sh

  mmctl channel search [channel]
  mmctl search --team [team] [channel] [flags]

**Examples**

.. code-block:: sh

  channel search myChannel
  channel search --team myTeam myChannel

**Options**

.. code-block:: sh

  -h, --help      help for search
  --team string   Team name or ID

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")


mmctl command
-------------

Management of slash commands.

  Child Commands
    -  `mmctl command create`_ - Create a custom command
    -  `mmctl command delete`_ - Delete a specified slash command
    -  `mmctl command list`_ - List slash commands on specified teams

**Options**

.. code-block:: sh

    -h, --help      help for command

mmctl command create
^^^^^^^^^^^^^^^^^^^^

**Description**

  Create a custom slash command for the specified team.

**Format**

.. code-block:: sh

   mmctl command create [team] [flags]

**Examples**

.. code-block:: sh

   command create myteam --title MyCommand --description "My Command Description" --trigger-word mycommand --url http://localhost:8000/my-slash-handler --creator myusername --response-username my-bot-username --icon http://localhost:8000/my-slash-handler-bot-icon.png --autocomplete --post

**Options**

.. code-block:: sh

   --autocomplete               Show Command in autocomplete list
   --autocompleteDesc string    Short Command Description for autocomplete list
   --autocompleteHint string    Command Arguments displayed as help in autocomplete list
   --creator string             Command Creator's Username (required)
   --description string         Command Description
   -h, --help                   help for create
   --icon string                Command Icon URL
   --post                       Use POST method for Callback URL
   --response-username string   Command Response Username
   --title string               Command Title
   --trigger-word string        Command Trigger Word (required)
   --url string                 Command Callback URL (required)

**Options Inherited from Parent Commands**

.. code-block:: sh

   --format string   the format of the command output [plain, json] (default "plain")

mmctl command delete
^^^^^^^^^^^^^^^^^^^^

**Dscription**

  Delete a slash command. Commands can be specified by command ID.

**Format**

.. code-block:: sh

   mmctl command delete [flags]

**Examples**

.. code-block:: sh

  command delete commandID

**Options**

.. code-block:: sh

   -h, --help   help for delete

**Options Inherited from Parent Commands**

.. code-block:: sh

  --format string the format of the command output [plain, json] (default "plain")


mmctl command list
^^^^^^^^^^^^^^^^^^^^

**Description**

  List all commands on specified teams.

**Format**

.. code-block:: sh

  mmctl command list [flags]

**Examples**

.. code-block:: sh

 command list myteam

**Options**

.. code-block:: sh

   -h, --help   help for list

**Options Inherited from Parent Commands**

.. code-block:: sh

 --format string the format of the command output [plain, json] (default "plain")

mmctl config
------------

Configuration settings.

  Child Commands
    -  `mmctl config get`_ - Get the value of a configuration setting
    -  `mmctl config show`_ - Writes the server configuration to STDOUT

**Options**

.. code-block:: sh

   -h, --help   help for config

mmctl config get
^^^^^^^^^^^^^^^^^

**Description**

  Gets the value of a config setting by its name in dot notation.

**Format**

.. code-block:: sh

   mmctl config get [flags]

**Examples**

.. code-block:: sh

  config get SqlSettings.DriverName

**Options**

.. code-block:: sh

   -h, --help   help for get

**Options Inherited from Parent Commands**

.. code-block:: sh

   --format string   the format of the command output [plain, json] (default "plain")

mmctl config show
^^^^^^^^^^^^^^^^^

**Description**

  Prints the server configuration and writes to STDOUT in JSON format.

**Format**

.. code-block:: sh

      mmctl config show [flags]

**Examples**

.. code-block:: sh

     config show

**Options**

.. code-block:: sh

      -h, --help   help for show

**Options Inherited from Parent Commands**

.. code-block:: sh

      --format string   the format of the command output [plain, json] (default "plain")


mmctl group
-----------

Management of groups (channel and teams).

Child Commands
  -  `mmctl group channel`_ - Manage channel groups
  -  `mmctl group team`_ - Manage team groups
  -  `mmctl group list-ldap`_ - List LDAP groups


mmctl group channel
--------------------

Management of channel groups

Child Commands
  -  `mmctl group channel disable`_ - Disable group channel constrains
  -  `mmctl group channel enable`_ - Enable group channel constrains
  -  `mmctl group channel list`_ - List channel groups
  -  `mmctl group channel status`_ - Check group status

**Options**

.. code-block:: sh

      -h, --help   help for group

mmctl group channel disable
^^^^^^^^^^^^^^^^^^^^^^^^^

**Description**

  Disables group constrains in the specified channel.

**Format**

.. code-block:: sh

    mmctl group channel disable [team]:[channel] [flags]

**Examples**

.. code-block:: sh

    group channel disable myteam:mychannel

**Options**

.. code-block:: sh

    -h, --help   help for disable

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl group channel enable
^^^^^^^^^^^^^^^^^^^^^^^^^

**Description**

  Enables group constrains in the specified channel.

**Format**

.. code-block:: sh

   mmctl group channel enable [team]:[channel] [flags]

**Examples**

.. code-block:: sh

    group channel enable myteam:mychannel

**Options**

.. code-block:: sh

    -h, --help   help for enable

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl group channel list
^^^^^^^^^^^^^^^^^^^^^^^^^

**Description**

  List the groups associated with a channel.

**Format**

.. code-block:: sh

   mmctl group channel list [team]:[channel] [flags]

**Examples**

.. code-block:: sh

  group channel list myteam:mychannel

**Options**

.. code-block:: sh

    -h, --help   help for list

**Options Inherited from Parent Commands**

.. code-block:: sh

  --format string   the format of the command output [plain, json] (default "plain")

mmctl group channel status
^^^^^^^^^^^^^^^^^^^^^^^^^

**Description**

  Shows the group constrain status for the specified channel.

**Format**

.. code-block:: sh

     mmctl group channel status [team]:[channel] [flags]

**Examples**

.. code-block:: sh

     group channel status myteam:mychannel

**Options**

.. code-block:: sh

    -h, --help   help for status

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")


mmctl group team
--------------------

Management of team groups.

Child Commands
  -  `mmctl group team disable`_ - Disable group team constrains
  -  `mmctl group team enable`_ - Enable group team constrains
  -  `mmctl group team list`_ - List team groups
  -  `mmctl group team status`_ - Check group constrain status

**Options**

.. code-block:: sh

      -h, --help   help for group

mmctl group team disable
^^^^^^^^^^^^^^^^^^^^^^^^^

**Description**

 Disables group constrains in the specified team.

**Format**

.. code-block:: sh

    mmctl group team disable [team] [flags]

**Examples**

.. code-block:: sh

    group team disable myteam

**Options**

.. code-block:: sh

    -h, --help   help for disable

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl group team enable
^^^^^^^^^^^^^^^^^^^^^^^^^

**Description**

  Enables group constrains in the specified team.

**Format**

.. code-block:: sh

   mmctl group team enable [team] [flags]

**Examples**

.. code-block:: sh

    group team enable myteam

**Options**

.. code-block:: sh

    -h, --help   help for enable

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl group team list
^^^^^^^^^^^^^^^^^^^^^^^^^

**Description**

 List the groups associated with a team.

**Format**

.. code-block:: sh

   mmctl group team list [team] [flags]

**Examples**

.. code-block:: sh

  group team list myteam

**Options**

.. code-block:: sh

    -h, --help   help for list

**Options Inherited from Parent Commands**

.. code-block:: sh

  --format string   the format of the command output [plain, json] (default "plain")

mmctl group team status
^^^^^^^^^^^^^^^^^^^^^^^^^

**Description**

 Shows the group constrain status for the specified team.

**Format**

.. code-block:: sh

     mmctl group team status [team] [flags]

**Examples**

.. code-block:: sh

     group channel status myteam

**Options**

.. code-block:: sh

    -h, --help   help for status

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")


mmctl group list-ldap
^^^^^^^^^^^^^^^^^^^^

**Description**

  List LDAP groups.

**Format**

.. code-block:: sh

   mmctl group list-ldap [flags]

**Examples**

.. code-block:: sh

    group list-ldap

**Options**

.. code-block:: sh

    -h, --help   help for list-ldap

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl ldap
----------

LDAP related utilities.

**Options**

.. code-block:: sh

    -h, --help   help for ldap

mmctl ldap sync
^^^^^^^^^^^^^^^

**Description**

  Synchronize all LDAP users and groups now.

**Format**

.. code-block:: sh

   mmctl ldap sync [flags]

**Examples**

.. code-block:: sh

    ldap sync

**Options**

.. code-block:: sh

    -h, --help   help for sync

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")


mmctl license
-------------

Licensing management commands.

Child Commands
  -  `mmctl license remove`_ - Remove current license
  -  `mmctl license upload`_ - Upload a new license

**Options**

.. code-block:: sh

  -h, --help   help for license

mmctl license remove
^^^^^^^^^^^^^^^^^^^^

**Description**

  Remove the current license and use Mattermost in Team Edition.

**Format**

.. code-block:: sh

     mmctl license remove [flags]

**Examples**

.. code-block:: sh

    license remove

**Options**

.. code-block:: sh

    -h, --help   help for remove

**Options Inherited from Parent Commands**

.. code-block:: sh

   --format string   the format of the command output [plain, json] (default "plain")


mmctl license upload
^^^^^^^^^^^^^^^^^^^^

**Description**

  Upload a license. Replaces current license.

**Format**

.. code-block:: sh

    mmctl license upload [license] [flags]

**Examples**

.. code-block:: sh

   license upload /path/to/license/mylicensefile.mattermost-license

**Options**

.. code-block:: sh

    -h, --help   help for upload

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl logs
----------

**Description**

  Display logs in a human-readable format

**Format**

.. code-block:: sh

    mmctl logs [flags]

**Options**

.. code-block:: sh

    -h, --help         help for logs
    -l, --logrus       Use logrus for formatting
    -n, --number int   Number of log lines to retrieve (default 200)

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl permissions
-----------------

Management of permissions and roles.

Child Commands
  -  `mmctl permissions add`_ - Add permissions
  -  `mmctl permissions remove`_ - Remove permissions
  -  `mmctl permissions show`_ - Show permissions

**Options**

.. code-block:: sh

  -h, --help   help for permissions


mmctl permissions add
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Description**

  Add one or more permissions to an existing role (only available in E10 and E20).

**Format**

.. code-block:: sh

    mmctl permissions add [role] [permission...] [flags]

**Examples**

.. code-block:: sh

    permissions add system_user list_open_teams

**Options**

.. code-block:: sh

   -h, --help   help for add

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl permissions remove
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Description**

  Remove one or more permissions from an existing role (only available in E10 and E20).

**Format**

.. code-block:: sh

      mmctl permissions remove [role] [permission...] [flags]

**Examples**

.. code-block:: sh

      permissions remove system_user list_open_teams

**Options**

.. code-block:: sh

     -h, --help   help for remove

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")


mmctl permissions show
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Description**

  Show all the information about a role.

**Format**

.. code-block:: sh

   mmctl permissions show [role_name] [flags]

**Examples**

.. code-block:: sh

   permissions show system_user

**Options**

.. code-block:: sh

   -h, --help   help for show

**Options Inherited from Parent Commands**

.. code-block:: sh

  --format string   the format of the command output [plain, json] (default "plain")

mmctl plugin
-------------

Management of plugins.

Child Commands
  -  `mmctl plugin add`_ - Add plugins
  -  `mmctl plugin delete`_ - Remove plugins
  -  `mmctl plugin disable`_ - Disable plugins
  -  `mmctl plugin enable`_ - Enable plugins
  -  `mmctl plugin list`_ - List plugins

**Options**

.. code-block:: sh

   -h, --help   help for plugin


mmctl plugin add
^^^^^^^^^^^^^^^^^

**Description**

  Add plugins to your Mattermost server.

**Format**

.. code-block:: sh

    mmctl plugin add [plugins] [flags]

**Examples**

.. code-block:: sh

    plugin add hovercardexample.tar.gz pluginexample.tar.gz

**Options**

.. code-block:: sh

   -h, --help   help for add

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")


mmctl plugin delete
^^^^^^^^^^^^^^^^^^^^

**Description**

  Delete previously uploaded plugins from your Mattermost server.

**Format**

.. code-block:: sh

  mmctl plugin delete [plugins] [flags]

**Examples**

.. code-block:: sh

  plugin delete hovercardexample pluginexample

**Options**

.. code-block:: sh

   -h, --help   help for delete

**Options Inherited from Parent Commands**

.. code-block:: sh

  --format string   the format of the command output [plain, json] (default "plain")

mmctl plugin disable
^^^^^^^^^^^^^^^^^^^^^

**Description**

  Disable plugins. Disabled plugins are immediately removed from the user interface and logged out of all sessions.

**Format**

.. code-block:: sh

    mmctl plugin disable [plugins] [flags]

**Examples**

.. code-block:: sh

    plugin disable hovercardexample pluginexample

**Options**

.. code-block:: sh

    -h, --help   help for disable

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")


mmctl plugin enable
^^^^^^^^^^^^^^^^^^^^

**Description**

  Enable plugins for use on your Mattermost server.

**Format**

.. code-block:: sh

    mmctl plugin enable [plugins] [flags]

**Examples**

.. code-block:: sh

    plugin enable hovercardexample pluginexample

**Options**

.. code-block:: sh

    -h, --help   help for enable

**Options Inherited from Parent Commands**

.. code-block:: sh

  --format string   the format of the command output [plain, json] (default "plain")

mmctl plugin list
^^^^^^^^^^^^^^^^^^

**Description**

  List all active and inactive plugins installed on your Mattermost server.

**Format**

.. code-block:: sh

    mmctl plugin list [flags]

**Examples**

.. code-block:: sh

    plugin list

**Options**

.. code-block:: sh

   -h, --help   help for list

**Options Inherited from Parent Commands**

.. code-block:: sh

  --format string   the format of the command output [plain, json] (default "plain")


mmctl post
------------

Management of posts.

Child Commands
  -  `mmctl post create`_ - Create a post
  -  `mmctl post list`_ - List posts

**Options**

.. code-block:: sh

   -h, --help   help for post

mmctl post create
^^^^^^^^^^^^^^^^^^

**Description**

  Create a post.

**Format**

.. code-block:: sh

    mmctl post create [flags]

**Examples**

.. code-block:: sh

    post create myteam:mychannel --message "some text for the post"

**Options**

.. code-block:: sh

  -h, --help              help for create
  -m, --message string    Message for the post
  -r, --reply-to string   Post id to reply to

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl post list
^^^^^^^^^^^^^^^^

**Description**

  List posts for a channel.

**Format**

.. code-block:: sh

   mmctl post list [flags]

**Examples**

.. code-block:: sh

    post list myteam:mychannel
    post list myteam:mychannel --number 20

**Options**

.. code-block:: sh

  -f, --follow       Output appended data as new messages are posted to the channel
  -h, --help         help for list
  -n, --number int   Number of messages to list (default 20)
  -i, --show-ids     Show posts ids

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl roles
-----------

mmctl team
----------

Management of teams.

Child Commands
  -  `mmctl team add`_ - Add teams
  -  `mmctl team archive`_ - Archive teams
  -  `mmctl team create`_ - Create teams
  -  `mmctl team delete`_ - Delete teams
  -  `mmctl team list`_ - List teams
  -  `mmctl team remove`_ - Remove teams
  -  `mmctl team rename`_ - Rename teams
  -  `mmctl team search`_ - Search teams

**Options**

.. code-block:: sh

  -h, --help   help for team

mmctl team add
^^^^^^^^^^^^^^^^

**Description**

  Add specified users to a team.

**Format**

.. code-block:: sh

    mmctl team add [team] [users] [flags]

**Examples**

.. code-block:: sh

    team add myteam user@example.com username

**Options**

.. code-block:: sh

   -h, --help   help for add

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl team archive
^^^^^^^^^^^^^^^^

*In progress*

mmctl team create
^^^^^^^^^^^^^^^^^^

**Description**

  Create a team.

**Format**

.. code-block:: sh

   mmctl team create [flags]

**Examples**

.. code-block:: sh

  team create --name mynewteam --display_name "My New Team"
  team create --name private --display_name "My New Private Team" --private

**Options**

.. code-block:: sh

    --display_name string   Team Display Name
    --email string          Administrator Email (anyone with this email is automatically a team admin)
    -h, --help              help for create
    --name string           Team Name
    --private               Create a private team

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl team delete
^^^^^^^^^^^^^^^^^^

**Description**

  Permanently deletes a team along with all related information including posts from the database.

**Format**

.. code-block:: sh

   mmctl team delete [teams] [flags]

**Examples**

.. code-block:: sh

      team delete myteam

**Options**

.. code-block:: sh

    --confirm   Confirm you really want to delete the team and a DB backup has been performed
    -h, --help  help for delete

**Options Inherited from Parent Commands**

.. code-block:: sh

  --format string   the format of the command output [plain, json] (default "plain")


mmctl team list
^^^^^^^^^^^^^^^^

**Description**

  List all teams on the server.

**Format**

.. code-block:: sh

    mmctl team list [flags]

**Examples**

.. code-block:: sh

    team list

**Options**

.. code-block:: sh

    -h, --help  help for list

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl team remove
^^^^^^^^^^^^^^^^^^

**Description**

  Remove specified users from a team.

**Format**

.. code-block:: sh

    mmctl team remove [team] [users] [flags]

**Examples**

.. code-block:: sh

   team remove myteam user@example.com username

**Options**

.. code-block:: sh

    -h, --help  help for remove

**Options Inherited from Parent Commands**

.. code-block:: sh

   --format string   the format of the command output [plain, json] (default "plain")

mmctl team search
^^^^^^^^^^^^^^^^^^

**Description**

  Search for teams based on name.

**Format**

.. code-block:: sh

   mmmctl team search [teams] [flags]

**Examples**

.. code-block:: sh

   team search team1

**Options**

.. code-block:: sh

   -h, --help  help for search

**Options Inherited from Parent Commands**

.. code-block:: sh

   --format string   the format of the command output [plain, json] (default "plain")

mmctl user
---------

Management of users.

Child Commands
  -  `mmctl user activate`_ - Activate user
  -  `mmctl user create`_ - Create user
  -  `mmctl user deactivate`_ - Deactivate user
  -  `mmctl user email`_ - Set user email
  -  `mmctl user invite`_ - Invite user
  -  `mmctl user reset_password`_ - Reset user password
  -  `mmctl user resetmfa`_ - Reset user's MFA token
  -  `mmctl user search`_ - Search for a user

**Options**

.. code-block:: sh

   -h, --help       help for user


mmctl user activate
^^^^^^^^^^^^^^^^^^^^^

**Description**

  Activate a user.

**Format**

.. code-block:: sh

      mmctl user activate [flags]

**Examples**
.. code-block:: sh

**Options**
.. code-block:: sh

**Options Inherited from Parent Commands**
.. code-block:: sh


mmctl user create
^^^^^^^^^^^^^^^^^^

**Description**

  Create a user.

**Format**

.. code-block:: sh

    mmctl user create [flags]

**Examples**

.. code-block:: sh

    user create --email user@example.com --username userexample --password Password1

**Options**

.. code-block:: sh

   --email string       Required. The email address for the new user account
   --firstname string   Optional. The first name for the new user account
   -h, --help           help for create
   --lastname string    Optional. The last name for the new user account
   --locale string      Optional. The locale (ex: en, fr) for the new user account
   --nickname string    Optional. The nickname for the new user account
   --password string    Required. The password for the new user account
   --system_admin       Optional. If supplied, the new user will be a system administrator. Defaults to false
   --username string    Required. Username for the new user account

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl user deactivate
^^^^^^^^^^^^^^^^^^^^^^

**Description**

  Deactivate users. Deactivated users are immediately logged out of all sessions and are unable to log back in.

**Format**

.. code-block:: sh

    mmctl user deactivate [emails, usernames, userIds] [flags]

**Examples**

.. code-block:: sh

  user deactivate user@example.com
  user deactivate username

**Options**

.. code-block:: sh

    -h, --help       help for deactivate


**Options Inherited from Parent Commands**

.. code-block:: sh

  --format string   the format of the command output [plain, json] (default "plain")


mmctl user email
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Description**

  Change the email address associated with a user.

**Format**

.. code-block:: sh

    mmctl user email [user] [new email] [flags]

**Examples**

.. code-block:: sh

  user email test user@example.com
  user activate username

**Options**

.. code-block:: sh

    -h, --help       help for email


**Options Inherited from Parent Commands**

.. code-block:: sh

  --format string   the format of the command output [plain, json] (default "plain")

mmctl user invite
^^^^^^^^^^^^^^^^^^

**Description**

  Send an email invite to a user, to join a team. You can invite a user to multiple teams by listing
  them. You can specify teams by name or ID.

**Format**

.. code-block:: sh

    mmctl user invite [email] [teams] [flags]

**Examples**

.. code-block:: sh

  user invite user@example.com myteam
  user invite user@example.com myteam1 myteam2

**Options**

.. code-block:: sh

    -h, --help       help for invite

**Options Inherited from Parent Commands**

.. code-block:: sh

  --format string   the format of the command output [plain, json] (default "plain")

mmctl user reset_password
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Description**

  Send users an email to reset their password.

**Format**

.. code-block:: sh

    mmctl user reset_password [users] [flags]

**Examples**

.. code-block:: sh

  user reset_password user@example.com

**Options**

.. code-block:: sh

    -h, --help       help for reset_password


**Options Inherited from Parent Commands**

.. code-block:: sh

  --format string   the format of the command output [plain, json] (default "plain")

mmctl user resetmfa
^^^^^^^^^^^^^^^^^^^^

**Description**

  Turn off multi-factor authentication for a user. If MFA enforcement is enabled, the
  user will be forced to re-enable MFA as soon as they login.

**Format**

.. code-block:: sh

    mmctl user resetmfa [users] [flags]

**Examples**

.. code-block:: sh

    user resetmfa user@example.com

**Options**

.. code-block:: sh

    -h, --help       help for resetmfa


**Options Inherited from Parent Commands**

.. code-block:: sh

  --format string   the format of the command output [plain, json] (default "plain")

mmctl user search
^^^^^^^^^^^^^^^^^^

**Description**

  Search for users based on username, email, or user ID.

**Format**

.. code-block:: sh

    mmctl user search [users] [flags]

**Examples**

.. code-block:: sh

    user search user1@mail.com user2@mail.com

**Options**

.. code-block:: sh

    -h, --help       help for search


**Options Inherited from Parent Commands**

.. code-block:: sh

  --format string   the format of the command output [plain, json] (default "plain")

mmctl version
-------------

mmctl webhook
-------------

mmctl websocket
-------------

**Description**

  Display websocket in a human-readable format.

**Format**

.. code-block:: sh

    mmctl websocket [flags]


**Options**

.. code-block:: sh

    -h, --help       help for websocket


**Options Inherited from Parent Commands**

.. code-block:: sh

  --format string   the format of the command output [plain, json] (default "plain")
