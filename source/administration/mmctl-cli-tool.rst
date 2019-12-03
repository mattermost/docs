mmctl Command Line Tool (Beta)
==============================

The mmctl tool is a remote CLI tool for Mattermost which is installed locally and uses the Mattermost API. Authentication
is done with either login credentials or an authentication token. <elaborate more on this, provide links to other docs>.

Being installed locally allows a System Admin to run CLI commands even in instances where there is no access to the
server (e.g., via SSH).

This tool is in beta and can be used alongside the Mattermost CLI tool. In the future, the Mattermost CLI tool will be
deprecated. The following list describes the commands that have been migrated.

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

 You can also refer to the Mattermost CLI documentation for additional commands.

 Notes:

 -  Parameters in CLI commands are order-specific.
 -  If special characters (``!``, ``|``, ``(``, ``)``, ``\``, ``'``, and ``"``) are used, the entire argument needs to be surrounded
 by single quotes (e.g. ``-password 'mypassword!'``, or the individual characters need to be escaped out (e.g. ``-password mypassword\!``).
 -  Team name and channel name refer to the handles, not the display names. So in the url ``https://community.mattermost.com/core/channels/town-square`` team
 name would be ``core`` and channel name would be ``town-square``



Installing mmctl
----------------

To install the project in your `$GOPATH` run:

.. code-block:: bash

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

.. _channel create:


mmctl channel add
~~~~~~~~~~~~~~~~~~~~~~

  Description
    Add users to a channel. If adding multiple users, use a space-separated list.

Format
       .. code-block:: none

         mmctl channel add [channel] [users][flags]

Examples
       .. code-block:: none

       channel add myteam:mychannel user@example.com username

Options Inherited from Parent Commands

   .. code-block:: none

      --format string   the format of the command output [plain, json] (default "plain")


mmctl channel archive
----------------------

Description
  Archive some channels. Archive a channel along with all related information including posts from the database. Channels can be
  specified by [team]:[channel]. (i.e., myteam:mychannel or by channel ID).

Format
     .. code-block:: none

       mmctl channel archive [channel][flags]

Examples
     .. code-block:: none

     channel archive myteam:mychannel

Options
.. code-block:: none

    -h, --help   help for archive

Options Inherited from Parent Commands

 .. code-block:: none

    --format string   the format of the command output [plain, json] (default "plain")

mmctl channel create
~~~~~~~~~~~~~~~~~~~~~~

Description
        Create a channel.

Format
        .. code-block:: none

          mmctl channel create [flags]

Examples
        .. code-block:: none

        channel create --team myteam --name mynewchannel --display_name "My New Channel"
        channel create --team myteam --name mynewprivatechannel --display_name "My New Private Channel" --private

Options

    .. code-block:: none

         --display_name string   Channel Display Name
         --header string         Channel header
     -h, --help                  help for create
         --name string           Channel Name
         --private               Create a private channel.
         --purpose string        Channel purpose
         --team string           Team name or ID

Options Inherited from Parent Commands

    .. code-block:: none

     --format string   the format of the command output [plain, json] (default "plain")


mmctl channel list
-------------------

Description
  List all channels on specified teams. Archived channels are appended with '(archived)'.

Format
     .. code-block:: none

       mmctl channel list [teams] [flags]

Examples
     .. code-block:: none

     channel list myteam

Options
.. code-block:: none

    -h, --help   help for list

Options Inherited from Parent Commands

 .. code-block:: none

    --format string   the format of the command output [plain, json] (default "plain")


mmctl make private
------------------

Description
  Set the type of a channel from public to private. Channel can be specified by [team]:[channel] (e.g., myteam:mychannel or by channel ID).

Format
     .. code-block:: none

     mmctl channel make_private [channel] [flags]

Examples
     .. code-block:: none

    channel make_private myteam:mychannel

Options
.. code-block:: none

    -h, --help   help for make_private

Options Inherited from Parent Commands

 .. code-block:: none

    --format string   the format of the command output [plain, json] (default "plain")

mmctl channel move
------------------

<comnfirm where this is>

mmctl channel remove
--------------------

Description
  Remove specified users from a channel.

Format
     .. code-block:: none

     mmctl channel remove [channel] [users] [flags]

Examples
     .. code-block:: none

   channel remove myteam:mychannel user@example.com username
   channel remove myteam:mychannel --all-users

Options
.. code-block:: none

  --all-users   Remove all users from the indicated channel.
  -h, --help    help for remove

Options Inherited from Parent Commands

 .. code-block:: none

    --format string   the format of the command output [plain, json] (default "plain")

mmctl channel rename
--------------------

Description
  Remove specified users from a channel.

Format
     .. code-block:: none

    mmctl channel rename [flags]

Examples
     .. code-block:: none

   channel rename myteam:mychannel newchannelname --display_name "New Display Name"


Options
.. code-block:: none

  --display_name string   Channel Display Name
  -h, --help              help for rename

Options Inherited from Parent Commands

 .. code-block:: none

    --format string   the format of the command output [plain, json] (default "plain")

mmctl channel restore
---------------------

Description
  Restore a previously deleted channel Channels can be specified by [team]:[channel] (e.g., myteam:mychannel or by channel ID).

Format
     .. code-block:: none

    mmctl channel restore [channels] [flags]

Examples
     .. code-block:: none

   channel restore myteam:mychannel


Options
.. code-block:: none

   -h, --help   help for restore

Options Inherited from Parent Commands

 .. code-block:: none

  --format string   the format of the command output [plain, json] (default "plain")


mmctl channel search
--------------------

Description
  Search a channel by channel name. Channel can be specified by team (e.g., --team myTeam myChannel) or by team ID.

Format
     .. code-block:: none

   mmctl channel search [channel]
   mmctl search --team [team] [channel] [flags]

Examples
     .. code-block:: none

  channel search myChannel
  channel search --team myTeam myChannel


Options
.. code-block:: none

  -h, --help          help for search
  --team string   Team name or ID

Options Inherited from Parent Commands

 .. code-block:: none

  --format string   the format of the command output [plain, json] (default "plain")



m
