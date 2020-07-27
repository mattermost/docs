mmctl Command Line Tool (Beta)
==============================

The mmctl tool is a remote CLI tool for Mattermost which is installed locally and uses the Mattermost API. Authentication
is done with either login credentials or an authentication token.

Being installed locally allows a System Admin to run CLI commands even in instances where there is no access to the
server (e.g., via SSH). This tool is currently in beta and can be used alongside the Mattermost CLI tool.
In the future, the Mattermost CLI tool will be deprecated.

This feature was developed to a large extent by community contributions and we'd like to extend our gratitude to the contributors who have worked on this project. We are currently accepting pull requests for Help Wanted issues
in the `mattermost-server <https://github.com/mattermost/mattermost-server/issues?q=is%3Aissue+is%3Aopen+label%3A%22Help+Wanted%22+label%3AArea%2Fmmctl>`__ repo. You can learn more about
the unit test coverage campaign for mmctl in the `Unit testing mmctl commands <https://mattermost.com/blog/unit-testing-mmctl-commands/>`__ blog post.

**Notes**

-  Parameters in CLI commands are order-specific.
-  If special characters (``!``, ``|``, ``(``, ``)``, ``\``, ``'``, and ``"``) are used, the entire argument needs to be surrounded by single quotes (e.g. ``-password 'mypassword!'``, or the individual characters need to be escaped out (e.g. ``password mypassword\!``).
- Team name and channel name refer to the handles, not the display names. So in the URL ``https://community.mattermost.com/core/channels/town-square`` team name would be ``core`` and channel name would be ``town-square``.

**Commands**
   - `mmctl auth`_ - Authentication Management
   - `mmctl bot`_ - Bot Management
   - `mmctl channel`_ - Channel Management
   - `mmctl command`_ - Command Management
   - `mmctl completion`_ - Generates autocompletion scripts for bash and zsh
   - `mmctl config`_ - Configuration Management
   - `mmctl docs`_ - Generates mmctl documentation
   - `mmctl group`_ - Group Management
   - `mmctl ldap`_ - LDAP Management
   - `mmctl license`_ - License Management
   - `mmctl logs`_ - Log Management
   - `mmctl permissions`_ - Permissions Management
   - `mmctl plugin`_ - Plugin Management
   - `mmctl post`_ - Post Management
   - `mmctl roles`_ - Roles Management
   - `mmctl system`_ - System Management
   - `mmctl team`_ - Team Management
   - `mmctl token`_ - Token Management
   - `mmctl user`_ - User Management
   - `mmctl version`_ - Version Management
   - `mmctl websocket`_ - Websocket Management

**Options**

.. code-block:: sh

       --format string               the format of the command output [plain, json] (default "plain")
       -h, --help                    help for mmctl
       --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
       --local                       allows communicating with the server through a unix socket
       --strict                      will only run commands if the mmctl version matches the server one


Installing mmctl
----------------

There are different methods available to install mmctl.

**Using brew (Linux, macOS)**

Use this option on Linux and macOS if you have Homebrew installed.

.. code-block:: sh

   brew install mmctl

**Using go get (Linux, macOS, Windows)**

Use this option on Linux, macOS, and Windows if you have a ``go`` environment configured.

To add the project in your `$GOPATH` run the following command:

.. code-block:: sh

   go get -u github.com/mattermost/mmctl

**Using release package (Linux, macOS, Windows)**

Vist the `mmctl releases page <https://github.com/mattermost/mmctl/releases>`__ and download the appropriate release for your OS, and install the binary.


Building mmctl
----------------

The ``mmctl`` tool uses ``go`` modules to manage dependencies, so you need to have installed
``go`` 1.11 or greater and compile the binary using:

.. code-block:: sh

  make build

Local mode
----------

Local mode allows platform administrators with access to the Mattermost server to run mmctl commands against the API without needing to have a user registered. To ensure secure usage of this API, the server exposes a local socket that only a user with access to the server's file system can access. The requests coming from the socket are treated as authorized, so they can reach the handlers without requiring a user session.

The API that the socket exposes follows the same specification that can be found `in the API documentation <https://api.mattermost.com>`_, so mmctl is able to interact with it without needing any modifications. When a request comes in through the socket, it is flagged as local by the server, and this flag is taken into account when checking for session permissions to correctly authorize the sessions.

To use local mode, the Mattermost server first needs to `have local mode enabled <https://docs.mattermost.com/administration/config-settings.html#enable-local-mode>`_. When local mode is enabled, a socket is created at ``/var/tmp/mattermost_local.socket`` by default.

Running the tests
------------------

mmctl has two types of tests: unit tests and end to end tests. To run the unit tests, you just need to execute:

.. code-block:: sh

  make test

To run the end to end test suite, you need to have a Mattermost server instance running. Check the `Developer Setup guide <https://developers.mattermost.com/contribute/server/developer-setup/>`_ for instructions around how to configure a local test server instance.

Once the development server is set up, cd into the ``mattermost-server directory``:

- Start it with ``make run``. To confirm that the instance is running correctly, you can access the web interface at ``http://localhost:8065``.
- Run ``make test-data`` to preload your server instance with initial seed data. Generated data such as users are typically used for logging, etc.

Change your directory to ``mmctl`` and run the end to end test suite with:

.. code-block:: sh
  
  make test-e2e

Authenticating and logging in
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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


Authenticate to a server (e.g. >mmctl auth login https://test.mattermost.com), then enter your username and password
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

Access tokens
^^^^^^^^^^^^^

You can generate and use a personal access token to authenticate with a server, instead of using username and password to log in:

.. code-block:: sh

   $ mmctl auth login https://community.mattermost.com --name community --access-token MY_ACCESS_TOKEN


Alternatively, you can log in to your Mattermost server with a username and password:

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


Installing shell completions
^^^^^^^^^^^^^^^^^^^^^^^^^^

To install the shell completions for bash, add the following line to your ``~/.bashrc`` or ``~/.profile`` file:

.. code-block:: sh

  source <(mmctl completion bash)

For zsh, add the following line to your ``~/.zshrc`` file:

.. code-block:: sh

  source <(mmctl completion zsh)

mmctl bot
--------------

Management of bots.

  Child Commands
    -  `mmctl bot assign`_ - Assign bot ownership
    -  `mmctl bot create`_ - Create a new bot
    -  `mmctl bot disable`_ - Disble a bot
    -  `mmctl bot enable`_ - Enable a bot
    -  `mmctl bot list`_ - List all bots
    -  `mmctl bot update`_ - Update bot configuration
    
**Options**

.. code-block:: sh

   -h, --help   help for bot
   
mmctl bot assign
^^^^^^^^^^^^^^^^^

**Description**

  Assign the ownership of a bot to another user.

**Format**

.. code-block:: sh

   mmctl bot assign [bot-username] [new-owner-username] [flags]

**Examples**

.. code-block:: sh

   bot assign testbot user2

**Options**

 .. code-block:: sh

   -h, --help              help for assign

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl bot create
^^^^^^^^^^^^^^^^^

**Description**

  Create a bot.

**Format**

.. code-block:: sh

   mmctl bot create [username] [flags]

**Examples**

.. code-block:: sh

   bot create testbot

**Options**

 .. code-block:: sh

  --description string    Optional. The description text for the new bot.
  --display-name string   Optional. The display name for the new bot.
  -h, --help              help for create

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one
   
mmctl bot disable
^^^^^^^^^^^^^^^^^

**Description**

  Disable an enabled bot.

**Format**

.. code-block:: sh

   mmctl bot disable [username] [flags]

**Examples**

.. code-block:: sh

   bot disable testbot

**Options**

 .. code-block:: sh

  -h, --help              help for disable

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one
   
   
mmctl bot enable
^^^^^^^^^^^^^^^^^

**Description**

  Enable a disabled bot.

**Format**

.. code-block:: sh

   mmctl bot enable [username] [flags]

**Examples**

.. code-block:: sh

   bot enable testbot

**Options**

 .. code-block:: sh

  -h, --help              help for enable

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one
   
mmctl bot list
^^^^^^^^^^^^^^^^^

**Description**

  List the bot's users.

**Format**

.. code-block:: sh

   mmctl bot list [flags]

**Examples**

.. code-block:: sh

   bot list

**Options**

 .. code-block:: sh

   --all        Optional. Show all bots (including deleleted and orphaned)
   -h, --help   help for list
   --orphaned   Optional. Only show orphaned bots

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one
   
mmctl bot update
^^^^^^^^^^^^^^^^^

**Description**

  Update bot information.

**Format**

.. code-block:: sh

   mmctl bot update [username] [flags]

**Examples**

.. code-block:: sh

   bot update testbot --username newbotusername

**Options**

 .. code-block:: sh

   --description string    Optional. The new description text for the bot
   --display-name string   Optional. The new display name for the bot
   -h, --help              help for update
   --username string       Optional. The new username for the bot

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl channel
--------------

Commands for channel management.

  Child Commands
    -  `mmctl channel add`_ - Add a channel
    -  `mmctl channel archive`_ - Archive a channel
    -  `mmctl channel create`_ - Create a channel
    -  `mmctl channel list`_ - List all channels on specified teams
    -  `mmctl channel make_private`_ - Set a channel's type to "private"
    -  `mmctl channel modify`_ - Modify a channel's type (private/public)
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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl channel list
^^^^^^^^^^^^^^^^^

**Description**

  List all public and archived channels on specified teams. Archived channels are appended with '(archived)'.

**Format**

.. code-block:: sh

   mmctl channel list [teams] [flags]

**Examples**

.. code-block:: sh

  channel list myteam

**Options**

.. code-block:: sh

  -h, --help   help for list


**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl channel modify
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Description**

   Change the public/private type of a channel. Channel can be specified by [team]:[channel]. ie. myteam:mychannel or by channel ID.

**Format**

.. code-block:: sh

    mmctl channel modify [channel] [flags]

**Examples**

.. code-block:: sh

    channel modify myteam:mychannel --private
    channel modify channelId --public

**Options**

.. code-block:: sh

  -h, --help    help for modify
    --private   Convert the channel to a private channel
    --public    Convert the channel to a public channel

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


mmctl command
-------------

Management of slash commands.

  Child Commands
    -  `mmctl command archive`_ - Archive a slash command
    -  `mmctl command create`_ - Create a custom command
    -  `mmctl command delete`_ - Delete a specified slash command
    -  `mmctl command list`_ - List slash commands on specified teams
    -  `mmctl command modify`_ - Modify a slash command
    -  `mmctl command move`_ - Move a slash command to a different team
    -  `mmctl command show`_ - Show a custom slash command
    

**Options**

.. code-block:: sh

    -h, --help      help for command
    

mmctl command archive
^^^^^^^^^^^^^^^^^^^^

**Dscription**

  Archive a slash command. Commands can be specified by command ID.

**Format**

.. code-block:: sh

   mmctl command archive [commandID] [flags]

**Examples**

.. code-block:: sh

  command archive commandID

**Options**

.. code-block:: sh

   -h, --help   help for archive

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl command modify
^^^^^^^^^^^^^^^^^^^^

**Description**

  Modify a slash command. Commands can be specified by command ID.

**Format**

.. code-block:: sh

  mmctl command modify [commandID] [flags]

**Examples**

.. code-block:: sh

 command modify commandID --title MyModifiedCommand --description "My Modified Command Description" --trigger-word mycommand --url http://localhost:8000/my-slash-handler --creator myusername --response-username my-bot-username --icon http://localhost:8000/my-slash-handler-bot-icon.png --autocomplete --post

**Options**

.. code-block:: sh

    --autocomplete               Show Command in autocomplete list
    --autocompleteDesc string    Short Command Description for autocomplete list
    --autocompleteHint string    Command Arguments displayed as help in autocomplete list
    --creator string             Command Creator's username, email or id (required)
    --description string         Command Description
    -h, --help                   help for modify
    --icon string                Command Icon URL
    --post                       Use POST method for Callback URL
    --response-username string   Command Response Username
    --title string               Command Title
    --trigger-word string        Command Trigger Word (required)
    --url string                 Command Callback URL (required)

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl command move
^^^^^^^^^^^^^^^^^^^^

**Description**

  Move a slash command to a different team. Commands can be specified by command ID.

**Format**

.. code-block:: sh

  mmctl command move [team] [commandID] [flags]

**Examples**

.. code-block:: sh

 command move newteam commandID

**Options**

.. code-block:: sh

   -h, --help   help for move

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl command show
^^^^^^^^^^^^^^^^^^^^

**Description**

  Show a custom slash command. Commands can be specified by command ID. Returns command ID, team ID, trigger word, display name and creator username.

**Format**

.. code-block:: sh

  mmctl command [commandID] [flags]

**Examples**

.. code-block:: sh

 command show commandID

**Options**

.. code-block:: sh

   -h, --help   help for show

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl completion
----------------

Generates autocompletion scripts for bash and zsh.

  Child Commands
    -  `mmctl completion bash`_ - Edit the configuration settings
    -  `mmctl completion zsh`_ - Get the value of a configuration setting
    
**Options**

.. code-block:: sh

   -h, --help   help for completion

mmctl completion bash
^^^^^^^^^^^^^^^^^^^^^

**Description**

  Generates the bash autocompletion scripts.
  
  To load completion, run

.. code-block:: sh

  . <(mmctl completion bash)

  To configure your bash shell to load completions for each session, add the above line to your ``~/.bashrc``.

**Format**

.. code-block:: sh

   mmctl completion bash [flags]

**Options**

.. code-block:: sh

   -h, --help   help for bash

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl completion zsh
^^^^^^^^^^^^^^^^^^^^

**Description**

  Generates the zsh autocompletion scripts.
  
  To load completion, run

.. code-block:: sh

  . <(mmctl completion zsh)

  To configure your zsh shell to load completions for each session, add the above line to your ``~/.zshrc``.

**Format**

.. code-block:: sh

  mmctl completion zsh [flags]

**Options**

.. code-block:: sh

   -h, --help   help for zsh

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


mmctl config
------------

Configuration settings.

  Child Commands
    -  `mmctl config edit`_ - Edit the configuration settings
    -  `mmctl config get`_ - Get the value of a configuration setting
    -  `mmctl config reset`_ - Reset the configuration
    -  `mmctl config set`_ - Set the value of a configuration
    -  `mmctl config show`_ - Writes the server configuration to STDOUT

**Options**

.. code-block:: sh

   -h, --help   help for config

mmctl config edit
^^^^^^^^^^^^^^^^^

**Description**

  Opens the editor defined in the EDITOR environment variable to modify the server's configuration and then uploads it.

**Format**

.. code-block:: sh

   mmctl config edit [flags]

**Examples**

.. code-block:: sh

  config edit

**Options**

.. code-block:: sh

   -h, --help   help for edit

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl config reset
^^^^^^^^^^^^^^^^^

**Description**

 Resets the value of a config setting by its name in dot notation or a setting section. Accepts multiple values for array settings.

**Format**

.. code-block:: sh

   mmctl config reset [flags]

**Examples**

.. code-block:: sh

  config reset SqlSettings.DriverName LogSettings

**Options**

.. code-block:: sh

  --confirm   Confirm you really want to reset all configuration settings to its default value
  -h, --help  help for reset

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl config set
^^^^^^^^^^^^^^^^^

**Description**

  Sets the value of a config setting by its name in dot notation. Accepts multiple values for array settings.

**Format**

.. code-block:: sh

  mmctl config set [flags]

**Examples**

.. code-block:: sh

   config set SqlSettings.DriverName mysql

**Options**

.. code-block:: sh

   -h, --help   help for set

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl docs
----------

**Description**

  Generates mmctl documentation

**Format**

.. code-block:: sh

      mmctl docs [flags]

**Options**

.. code-block:: sh

      -d, --directory string   The directory where the docs would be generated in. (default "docs")
      -h, --help               help for docs

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl group
-----------

Management of groups (channel and teams).

Child Commands
  -  `mmctl group channel`_ - Manage channel groups
  -  `mmctl group list-ldap`_ - List LDAP groups
  -  `mmctl group team`_ - Manage team groups

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


mmctl ldap
----------

LDAP-related utilities.

Child Commands
  -  `mmctl ldap sync`_ - Sync all LDAP users and groups

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl logs
----------

**Description**

  Display logs in a human-readable format.

**Format**

.. code-block:: sh

    mmctl logs [flags]

**Options**

.. code-block:: sh

    -h, --help         help for logs
    -l, --logrus       Use logrus for formatting
    -n, --number int   Number of log lines to retrieve (default 200)

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl roles
-----------

This command will be available in a future release.

mmctl system
------------

System management commands for interacting with the server state and configuration.

Child Commands
  -  `mmctl system clearbusy`_ - Clears the busy state
  -  `mmctl system getbusy`_ - Get the current busy state
  -  `mmctl system setbusy`_ - Set the busy state to ``true``
  
**Options**

.. code-block:: sh

  -h, --help   help for system

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string                the format of the command output [plain, json] (default "plain")
    --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
    --local                        allows communicating with the server through a unix socket
    --strict                       will only run commands if the mmctl version matches the server one

mmctl system clearbusy
^^^^^^^^^^^^^^^^^^^^^

**Description**

  Clear the busy state which re-enables non-critical services.

**Format**

.. code-block:: sh

    mmctl system clearbusy [flags]

**Examples**

.. code-block:: sh

    system clearbusy

**Options**

.. code-block:: sh

   -h, --help   help for clearbusy

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string                the format of the command output [plain, json] (default "plain")
    --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
    --local                        allows communicating with the server through a unix socket
    --strict                       will only run commands if the mmctl version matches the server one

mmctl system getbusy
^^^^^^^^^^^^^^^^^^

**Description**

 Gets the server busy state (high load) and timestamp corresponding to when the server busy flag will be automatically cleared.

**Format**

.. code-block:: sh

   mmctl system getbusy [flags]

**Examples**

.. code-block:: sh

   system getbusy

**Options**

.. code-block:: sh

    -h, --help   help for getbusy

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string                the format of the command output [plain, json] (default "plain")
    --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
    --local                        allows communicating with the server through a unix socket
    --strict                       will only run commands if the mmctl version matches the server one
    

mmctl system setbusy
^^^^^^^^^^^^^^^^^^

**Description**

 Set the busy state to ``true`` for the specified number of seconds, which disables non-critical services.

**Format**

.. code-block:: sh

   mmctl system setbusy -s [seconds] [flags]

**Examples**

.. code-block:: sh

   system setbusy -s 3600

**Options**

.. code-block:: sh

    -h, --help   help for setbusy
    -s, --seconds uint   Number of seconds until server is automatically marked as not busy (default 3600)

**Options Inherited from Parent Commands**

.. code-block:: sh

    --format string                the format of the command output [plain, json] (default "plain")
    --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
    --local                        allows communicating with the server through a unix socket
    --strict                       will only run commands if the mmctl version matches the server one


mmctl team
----------

Management of teams.

Child Commands
  -  `mmctl team archive`_ - Archive some teams
  -  `mmctl team create`_ - Create teams
  -  `mmctl team delete`_ - Delete teams
  -  `mmctl team list`_ - List teams
  -  `mmctl team modify`_ - Modify teams
  -  `mmctl team rename`_ - Rename teams
  -  `mmctl team restore`_ - Restore teams
  -  `mmctl team search`_ - Search teams
  -  `mmctl team users`_ - Manage team users

**Options**

.. code-block:: sh

  -h, --help   help for team


mmctl team archive
^^^^^^^^^^^^^^^^

**Description**

  Archives a team along with all related information including posts from the database.

**Format**

.. code-block:: sh

  mmctl team archive [teams] [flags]

**Examples**

.. code-block:: sh

  team archive myteam

**Options**

.. code-block:: sh

  --confirm   Confirm you really want to archive the team and a DB backup has been performed
  -h, --help  help for archive

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl team modify
^^^^^^^^^^^^^^^^^^

**Description**

  Modify team's privacy setting to public or private.

**Format**

.. code-block:: sh

   mmctl team modify [teams] [flag] [flags]

**Examples**

.. code-block:: sh

   team modify myteam --private

**Options**

.. code-block:: sh

    -h, --help  help for modify
    --private   Modify team to be private
    --public    Modify team to be public

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl team rename
^^^^^^^^^^^^^^^^^^

**Description**

  Rename an existing team.

**Format**

.. code-block:: sh

   mmctl team rename [team] [flags]

**Examples**

.. code-block:: sh

   team rename old-team --display_name 'New Display Name'

**Options**

.. code-block:: sh

    --display_name string Team Display Name
    -h, --help            help for rename

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


mmctl team restore
^^^^^^^^^^^^^^^^^^

**Description**

  Restores archived teams.

**Format**

.. code-block:: sh

   mmctl team restore [teams] [flags]

**Examples**

.. code-block:: sh

   team restore myteam

**Options**

.. code-block:: sh

   -h, --help   help for restore

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl team search
^^^^^^^^^^^^^^^^^^

**Description**

  Search for teams based on name.

**Format**

.. code-block:: sh

   mmctl team search [teams] [flags]

**Examples**

.. code-block:: sh

   team search team1

**Options**

.. code-block:: sh

   -h, --help  help for search

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


mmctl team users
^^^^^^^^^^^^^^^^^^

Child Commands
  -  `mmctl team users add`_ - Add users to a team
  -  `mmctl team users remove`_ - Remove users from a team

mmctl team users add
~~~~~~~~~~~~~~~~~~

**Description**

  Add specified users to a team.

**Format**

.. code-block:: sh

   mmctl team users add [team] [users] [flags]

**Examples**

.. code-block:: sh

  team add myteam user@example.com username

**Options**

.. code-block:: sh

   -h, --help  help for add

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


mmctl team users remove
~~~~~~~~~~~~~~~~~~

**Description**

  Remove some users from a team.

**Format**

.. code-block:: sh

  mmctl team users remove [team] [users] [flags]

**Examples**

.. code-block:: sh

 team remove myteam user@example.com username

**Options**

.. code-block:: sh

  -h, --help  help for remove

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl token
---------

Management of users' access tokens.

Child Commands
  -  `mmctl token generate`_ - Generate token for a user
  -  `mmctl token list`_ - List users' tokens
  -  `mmctl token revoke`_ - Revoke tokens for a user

**Options**

.. code-block:: sh

   -h, --help       help for token


mmctl token generate
^^^^^^^^^^^^^^^^^^

**Description**

  Generate token for a user.

**Format**

.. code-block:: sh

   mmctl token generate [user] [description] [flags]

**Examples**

.. code-block:: sh

   generate testuser test-token

**Options**

.. code-block:: sh

   -h, --help           help for generate


**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one
   

mmctl token list
^^^^^^^^^^^^^^^^^^

**Description**

  List the tokens belonging to a user.

**Format**

.. code-block:: sh

   mmctl token list [user] [flags]

**Examples**

.. code-block:: sh

   user tokens testuser

**Options**

.. code-block:: sh

   --active         List only active tokens (default true)
   --all            Fetch all tokens. --page flag will be ignore if provided
   -h, --help       help for list
   --inactive       List only inactive tokens
   --page int       Page number to fetch for the list of users
   --per-page int   Number of users to be fetched (default 200) 


**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one
   
mmctl token revoke
^^^^^^^^^^^^^^^^^^

**Description**

  Revoke tokens for a user.

**Format**

.. code-block:: sh

   mmctl token revoke [token-ids] [flags]

**Examples**

.. code-block:: sh

   revoke testuser test-token-id

**Options**

.. code-block:: sh

   -h, --help       help for revoke

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl user
---------

Management of users.

Child Commands
  -  `mmctl user activate`_ - Activate a user
  -  `mmctl user create`_ - Create user
  -  `mmctl user deactivate`_ - Deactivate user
  -  `mmctl user email`_ - Set user email
  -  `mmctl user invite`_ - Invite user
  -  `mmctl user list`_ - List users
  -  `mmctl user reset_password`_ - Reset user password
  -  `mmctl user resetmfa`_ - Reset user's MFA token
  -  `mmctl user search`_ - Search for a user

**Options**

.. code-block:: sh

   -h, --help       help for user


mmctl user activate
^^^^^^^^^^^^^^^^^^

**Description**

 Activate users that have been deactivated.

**Format**

.. code-block:: sh

   mmctl user activate [emails, usernames, userIds] [flags]

**Examples**

.. code-block:: sh

   user activate user@example.com
   user activate username

**Options**

.. code-block:: sh

   -h, --help           help for activate


**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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


**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one


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


**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one
   
mmctl user list
^^^^^^^^^^^^^^^^^^

**Description**

  List all users.

**Format**

.. code-block:: sh

    mmctl user list [flags]

**Examples**

.. code-block:: sh

  user list

**Options**

.. code-block:: sh

    --all            Fetch all users. --page flag will be ignore if provided
    -h, --help       help for list
    --page int       Page number to fetch for the list of users
    --per-page int   Number of users to be fetched (default 200)

**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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


**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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


**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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


**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

mmctl version
-------------

**Description**

  Prints the version of mmctl.

**Format**

.. code-block:: sh

    mmctl version [flags]

**Options**

.. code-block:: sh

    -h, --help       help for version


**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one

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


**Options inherited from parent commands**

.. code-block:: sh

   --format string               the format of the command output [plain, json] (default "plain")
   --insecure-sha1-intermediate  allows the use of insecure TLS protocols, such as SHA-1
   --local                       allows communicating with the server through a unix socket
   --strict                      will only run commands if the mmctl version matches the server one
