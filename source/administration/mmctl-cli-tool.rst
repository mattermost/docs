mmctl Command Line Tool (Beta)
==============================

The mmctl tool is a remote CLI tool for Mattermost which is installed locally and uses the Mattermost API. Authentication
is done with either login credentials or an authentication token. <elaborate more on this, provide links to other docs>.

Being installed locally allows a System Admin to run CLI commands even in instances where there is no access to the
server (e.g., via SSH).

This tool is in beta and can be used alongside the Mattermost CLI tool. In the future, the Mattermost CLI tool will be
deprecated. The following list describes the commands that have been migrated.

.. code-block:: sh

     - auth        Manages the credentials of the remote Mattermost instances
     - channel     Management of channels
     - completion  Generates autocompletion scripts for bash and zsh
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



Notes:

 -  Parameters in CLI commands are order-specific.
 -  If special characters (``!``, ``|``, ``(``, ``)``, ``\``, ``'``, and ``"``) are used, the entire argument needs to be surrounded
 by single quotes (e.g. ``-password 'mypassword!'``, or the individual characters need to be escaped out (e.g. ``-password mypassword\!``).
 -  Team name and channel name refer to the handles, not the display names. So in the url ``https://community.mattermost.com/core/channels/town-square`` team
 name would be ``core`` and channel name would be ``town-square``


Installing mmctl
----------------

To install the project in your `$GOPATH` run:

.. code-block:: sh

   go get -u github.com/mattermost/mmctl

<what happens next? Are there any steps required to access mmctl? E.g., opening terminal, logging in, setting up authentication? Where is authentication done?

Compiling
^^^^^^^^^

First we have to install the dependencies of the project. `mmctl` uses `go` modules to manage the dependencies, so you need to have installed
`go` 1.11 or greater. We can compile the binary with:

.. code-block:: sh

  make build


Logging In
----------

First we have to log into a Mattermost instance:

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

Login methods
^^^^^^^^^^^^^

Password

  .. code-block:: sh

     $ mmctl auth login https://community.mattermost.com --name community --username my-username --password mysupersecret

The `login` command can also work interactively, so if you leave anyneeded flag empty, `mmctl` will ask you for it interactively:

  .. code-block:: sh

    $ mmctl auth login https://community.mattermost.com
    Connection name: community
    Username: my-username
    Password:

MFA
^^^^

If you want to log in with MFA, you just need to use the `--mfa-token` flag:

.. code-block:: sh

   $ mmctl auth login https://community.mattermost.com --name community --username my-username --password mysupersecret --mfa-token 123456

Access tokens
^^^^^^^^^^^^^

Instead of using username and password to log in, you can generate and use a personal access token to authenticate with a server:

.. code-block:: sh

   $ mmctl auth login https://community.mattermost.com --name community --access-token MY_ACCESS_TOKEN

Using mmctl
-----------

For the usage of all the commands, use the `--help` flag or check [the tool's documentation](./docs/mmctl.md).

.. code-block:: sh

   Mattermost offers workplace messaging across web, PC and phones with archiving, search and integration with your existing systems. Documentation available at https://docs.mattermost.com

Installing Shell Completions
^^^^^^^^^^^^^^^^^^^^^^^^^^

To install the shell completions for bash, add the following line to your `~/.bashrc` or `~/.profile` file:

.. code-block:: sh

      source <(mmctl completion bash)

For zsh, add the following line to your `~/.zshrc` file:

.. code-block:: sh

     source <(mmctl completion zsh)


mmctl
-----

Remote client for the Open Source, self-hosted Slack-alternative

Options
  .. code-block:: sh

      --format string    the format of the command output [plain, json] (default "plain")
      -h, --help         help for mmctl

Commands

  - `mmctl channel`_ - Channel Management
  - `mmctl command`_ - Command Management
  - `mmctl config`_ - Configuration Management
  - `mmctl export`_ - Export Management
  - `mmctl group`_ - Group Management
  - `mmctl ldap`_ - LDAP Management
  - `mmctl license`_ - License Management
  - `mmctl logs`_ - Log Management
  - `mmctl permissions`_ - Permissions Management
  - `mmctl plugin`_ - Plugin Management
  - `mmctl roles`_ - Roles Management
  - `mmctl team`_ - Team Management
  - `mmctl user`_ - User Management
  - `mmctl version`_ - Version Management
  - `mmctl webhook`_ - Webhook Management


mmctl channel
--------------

Commands for channel management.

  Child Commands
    -  `mmctl channel add`_ - Add a channel
    -  `mmctl channel archive`_ - Archive a channel
    -  `mmctl channel create`_ - Create a channel
    -  `mmctl channel list`_ - List all channels on specified teams
    -  `mmctl channel move`_ - Move a channel to another team
    -  `mmctl channel remove`_ - Remove users from a channel
    -  `mmctl channel rename`_ - Rename a channel
    -  `mmctl channel restore`_ - Restore a channel from the archive
    -  `mmctl channel make_private`_ - Set a channel's type to "private"
    -  `mmctl channel search`_ -  Search a channel by name

mmctl channel add
^^^^^^^^^^^^^^^^^

Add users to a channel. If adding multiple users, use a space-separated list.

Format

.. code-block:: sh

   mmctl channel add [channel][users][flags]

Examples

.. code-block:: sh

   channel add myteam:mychannel user@example.com username

Options Inherited from Parent Commands

.. code-block:: sh

   --format string the format of the command output [plain, json] (default "plain")

mmctl channel archive
^^^^^^^^^^^^^^^^^^^^

Archive some channels. Archive a channel along with all related information including posts from the database. Channels can be
specified by ``[team]:[channel]. (i.e., myteam:mychannel or by channel ID)``.

Format

.. code-block:: sh

   mmctl channel archive [channels] [flags]

Examples

.. code-block:: sh

   channel archive myteam:mychannel

Options

.. code-block:: sh

   -h, --help   help for archive

Options Inherited from Parent Commands

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl channel create
^^^^^^^^^^^^^^^^^

Create a channel.

Format

.. code-block:: sh

   mmctl channel create [flags]

Examples

.. code-block:: sh

  channel create --team myteam --name mynewchannel --display_name "My New Channel"
  channel create --team myteam --name mynewprivatechannel --display_name "My New Private Channel" --private

Options

.. code-block:: sh

    --display_name string   Channel Display Name
    --header string         Channel header
    -h, --help              help for create
    --name string           Channel Name
    --private               Create a private channel.
    --purpose string        Channel purpose
    --team string           Team name or ID


Options Inherited from Parent Commands

.. code-block:: sh

   --format string   the format of the command output [plain, json] (default "plain")

mmctl channel list
^^^^^^^^^^^^^^^^^

List all channels on specified teams. Archived channels are appended with '(archived)'.

Format

.. code-block:: sh

   mmctl channel list [teams] [flags]

Examples

.. code-block:: sh

  channel list myteam

Options

.. code-block:: sh

  -h, --help   help for list


Options Inherited from Parent Commands

.. code-block:: sh

   --format string   the format of the command output [plain, json] (default "plain")

mmctl channel move
^^^^^^^^^^^^^^^^^

<>

mmctl channel remove
^^^^^^^^^^^^^^^^^

Remove specified users from a channel.

Format

.. code-block:: sh

   mmctl channel remove [channel] [users] [flags]

Examples

.. code-block:: sh

  channel remove myteam:mychannel user@example.com username
  channel remove myteam:mychannel --all-users

Options

.. code-block:: sh

  --all-users   Remove all users from the indicated channel.
  -h, --help    help for remove

Options Inherited from Parent Commands

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl channel rename
^^^^^^^^^^^^^^^^^^^

Rename a channel.

Format

.. code-block:: sh

   mmctl channel rename [flags]

Examples

.. code-block:: sh

   channel rename myteam:mychannel newchannelname --display_name "New Display Name"

Options

.. code-block:: sh

  --display_name string   Channel Display Name
  -h, --help              help for rename

Options Inherited from Parent Commands

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl channel restore
^^^^^^^^^^^^^^^^^^^^^

Restore a previously deleted channel Channels can be specified by ``[team]:[channel] (e.g., myteam:mychannel or by channel ID)``.

Format

.. code-block:: sh

   mmctl channel restore [channels] [flags]

Examples

.. code-block:: sh

   channel restore myteam:mychannel

Options

.. code-block:: sh

   -h, --help   help for restore

Options Inherited from Parent Commands

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl channel make_private
^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the type of a channel from public to private. Channel can be specified by ``[team]:[channel]``. ie. myteam:mychannel or by channel ID.

Format

.. code-block:: sh

   mmctl channel make_private [channel] [flags]

Examples

.. code-block:: sh

   channel make_private myteam:mychannel

Options

.. code-block:: sh

   -h, --help   help for make_private

Options Inherited from Parent Commands

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")

mmctl channel search
^^^^^^^^^^^^^^^^^^^^^

Search a channel by channel name. Channel can be specified by team (e.g., --team myTeam myChannel) or by team ID.

Format

.. code-block:: sh

  mmctl channel search [channel]
  mmctl search --team [team] [channel] [flags]

Examples

.. code-block:: sh

  channel search myChannel
  channel search --team myTeam myChannel

Options

.. code-block:: sh

  -h, --help      help for search
  --team string   Team name or ID

Options Inherited from Parent Commands

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "plain")


mmctl command
-------------

Management of slash commands.

  Child Commands
    -  `mmctl command create`_ - Add a channel
    -  `mmctl command delete`_ - Archive a channel
    -  `mmctl command list`_ - Create a channel

mmctl command create
^^^^^^^^^^^^^^^^^^^^

Add users to a channel. If adding multiple users, use a space-separated list.

Format

.. code-block:: sh

   mmctl command create [team] [flags]

Examples

.. code-block:: sh

   command create myteam --title MyCommand --description "My Command Description" --trigger-word mycommand --url http://localhost:8000/my-slash-handler --creator myusername --response-username my-bot-username --icon http://localhost:8000/my-slash-handler-bot-icon.png --autocomplete --post

Options

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

Options Inherited from Parent Commands

.. code-block:: sh

   --format string   the format of the command output [plain, json] (default "plain")

mmctl command delete
^^^^^^^^^^^^^^^^^^^^

Delete a slash command. Commands can be specified by command ID.

Format

.. code-block:: sh

   mmctl command delete [flags]

Examples

.. code-block:: sh

  command delete commandID

Options

.. code-block:: sh

   -h, --help   help for delete

Options Inherited from Parent Commands

.. code-block:: sh

  --format string the format of the command output [plain, json] (default "plain")


mmctl command list
^^^^^^^^^^^^^^^^^^^^

List all commands on specified teams.

Format

.. code-block:: sh

  mmctl command list [flags]

Examples

.. code-block:: sh

 command list myteam

Options

.. code-block:: sh

   -h, --help   help for list

Options Inherited from Parent Commands

.. code-block:: sh

 --format string the format of the command output [plain, json] (default "plain")

mmctl config
------------

Configuration settings.

  Child Commands
    -  `mmctl config get`_ - Add a channel
    -  `mmctl config show`_ - Archive a channel

mmctl config get
^^^^^^^^^^^^^^^^^

Gets the value of a config setting by its name in dot notation.

Format

.. code-block:: sh

   mmctl config get [flags]

Examples

.. code-block:: sh

  config get SqlSettings.DriverName

Options

.. code-block:: sh

   -h, --help   help for get

Options Inherited from Parent Commands

.. code-block:: sh

   --format string   the format of the command output [plain, json] (default "plain")

mmctl config show
^^^^^^^^^^^^^^^^^

Prints the server configuration and writes to STDOUT in JSON format.

Format

.. code-block:: sh

      mmctl config show [flags]

Examples

.. code-block:: sh

     config show

Options

.. code-block:: sh

      -h, --help   help for show

Options Inherited from Parent Commands

.. code-block:: sh

      --format string   the format of the command output [plain, json] (default "plain")


mmctl export
------------

<>


mmctl group
-----------

Management of groups.

Child Commands
  -  `mmctl group channel`_ - Add a channel
  -  `mmctl group channel disable`_ - Disable groups
  -  `mmctl group channel enable`_ - Enable groups
  -  `mmctl group channel list`_ - List groups
  -  `mmctl group channel status`_ - Check group status

mmctl group channel
^^^^^^^^^^^^^^^^^^^^

Management of channel groups

Format

.. code-block:: sh



Examples

.. code-block:: sh



Options

.. code-block:: sh

      -h, --help   help for group

Options Inherited from Parent Commands

.. code-block:: sh

      --format string   the format of the command output [plain, json] (default "plain")

mmctl group channel disable
^^^^^^^^^^^^^^^^^^^^^^^^^

Disables group constrains in the specified channel

Format

.. code-block:: sh

    mmctl group channel disable [team]:[channel] [flags]

Examples

.. code-block:: sh

    group channel disable myteam:mychannel

Options

.. code-block:: sh

    -h, --help   help for disable

Options Inherited from Parent Commands

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "p

mmctl group channel enable
^^^^^^^^^^^^^^^^^^^^^^^^^

Enables group constrains in the specified channel

Format

.. code-block:: sh

   mmctl group channel enable [team]:[channel] [flags]

Examples

.. code-block:: sh

    group channel enable myteam:mychannel

Options

.. code-block:: sh

    -h, --help   help for emable

Options Inherited from Parent Commands

.. code-block:: sh

    --format string   the format of the command output [plain, json] (default "p

mmctl group channel list
^^^^^^^^^^^^^^^^^^^^^^^^^

List the groups associated with a channel.

Format

.. code-block:: sh

   mmctl group channel list [team]:[channel] [flags]

Examples

.. code-block:: sh

  group channel list myteam:mychannel

Options

.. code-block:: sh

    -h, --help   help for list

Options Inherited from Parent Commands

.. code-block:: sh

  --format string   the format of the command output [plain, json] (def

mmctl group channel status
^^^^^^^^^^^^^^^^^^^^^^^^^

Shows the group constrain status for the specified channel

Format

.. code-block:: sh

     mmctl group channel status [team]:[channel] [flags]

Examples

.. code-block:: sh

     group channel status myteam:mychannel

Options

.. code-block:: sh

    -h, --help   help for status

Options Inherited from Parent Commands

.. code-block:: sh

    --format string   the format of the command output [plain, json] (def

mmctl ldap
----------

mmctl license
-------------

mmctl logs
----------

mmctl permissions
-----------------

mmctl plugin
-------------

mmctl roles
------------

mmctl team
----------

mmctl user
---------

mmctl version
-------------

mmctl webhook
-------------
