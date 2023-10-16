mmctl command line tool
=======================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

The mmctl is a CLI tool for the Mattermost server which is installed locally and uses the Mattermost API, but may also be used remotely. Authentication is done with either login credentials or an authentication token. This mmctl tool is included and replaces the `CLI </manage/command-line-tools.html>`__. The mmctl can currently be used alongside the Mattermost CLI tool. The Mattermost CLI tool will be deprecated in a future release.

Being installed locally enables System Admins for both self-hosted and Cloud Mattermost instances to run CLI commands even in instances where there's no access to the server (e.g., via SSH).

This feature was developed to a large extent by community contributions and we'd like to extend our gratitude to the contributors who have worked on this project. We are currently accepting pull requests for Help Wanted issues in the `mattermost-server <https://github.com/mattermost/mattermost/issues?q=is%3Aissue+is%3Aopen+label%3A%22Help+Wanted%22+label%3AArea%2Fmmctl>`__ repo. You can learn more about the unit test coverage campaign for mmctl in the `Unit testing mmctl commands <https://mattermost.com/blog/unit-testing-mmctl-commands/>`__ blog post.

mmctl usage notes
-----------------

- System Admins have two ways to run ``mmctl`` commands: by downloading ``mmctl`` from the release URLs, which you can find in the :ref:`installation instructions <install-mmctl-options>`, or by building it directly, for which you can check the :ref:`build instructions <build-mmctl>` below. The source code lives in the `server/cmd/mmctl directory within the mattermost repository <https://github.com/mattermost/mattermost/tree/master/server/cmd/mmctl>`__.
- ``mmctl`` also comes bundled with the Mattermost distribution, and is located in the ``bin`` folder of the installation, next to the ``CLI``.

  - We recommend you add the path to the Mattermost ``bin`` folder into your ``$PATH`` environment variable. This ensures that you can run mmctl commands locally regardless of your current directory location.
  - If the ``bin`` directory is not added to the ``$PATH`` environment variable, each time you use mmctl you must be in the ``bin`` directory to run mmctl commands, and the commands must be prefixed with ``./``. If you're working from a different directory, make sure you specify the full path to mmctl when running mmctl commands.
- Parameters in mmctl commands are order-specific.
- You can use the ``--local`` flag with mmctl commands to run them without authentication by allowing communicating with the server through a Unix socket. See the `local mode </manage/mmctl-command-line-tool.html#local-mode>`__ documentation for activation and usage details.
- If special characters (``!``, ``|``, ``(``, ``)``, ``\``, ``'``, and ``"``) are used, the entire argument needs to be surrounded by single quotes (e.g. ``-password 'mypassword!'``, or the individual characters need to be escaped out (e.g. ``password mypassword\!``).
- Team name and channel name refer to the handles, not the display names. So in the URL ``https://community.mattermost.com/core/channels/town-square`` team name would be ``core`` and channel name would be ``town-square``.

mmctl commands
--------------

- `mmctl auth`_ - Authentication Management
- `mmctl bot`_ - Bot Management
- `mmctl channel`_ - Channel Management
- `mmctl command`_ - Command Management
- `mmctl completion`_ - Generate autocompletion scripts for bash and zsh
- `mmctl config`_ - Configuration Management
- `mmctl docs`_ - Generate mmctl documentation
- `mmctl export`_ - Exports Management
- `mmctl extract`_ - Content Extraction Job Management
- `mmctl group`_ - Group Management
- `mmctl group channel`_ - Channel Group Management
- `mmctl group team`_ - Team Group Management
- `mmctl group user`_ - Custom User Group Management
- `mmctl import`_ - Import Management
- `mmctl integrity`_ - Database Record Integrity
- `mmctl ldap`_ - LDAP Management
- `mmctl license`_ - License Management
- `mmctl logs`_ - Log Management
- `mmctl permissions`_ - Permissions Management
- `mmctl plugin`_ - Plugin Management
- `mmctl post`_ - Post Management
- `mmctl roles`_ - Roles Management
- `mmctl saml`_ - SAML Management
- `mmctl sampledata`_ - Generate sample data
- `mmctl system`_ - System Management
- `mmctl team`_ - Team Management
- `mmctl team users`_ - Team User Management
- `mmctl token`_ - Token Management
- `mmctl user`_ - User Management
- `mmctl version`_ - Version Management
- `mmctl webhook`_ - Webhook Management
- `mmctl websocket`_ - Websocket Management

**Options**

.. code-block:: sh

       --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
       --disable-pager                disables paged output
       -h, --help                     help for mmctl
       --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
       --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
       --json                         the output format will be in json format
       --local                        allows communicating with the server through a unix socket
       --quiet                        prevent mmctl to generate output for the commands
       --strict                       will only run commands if the mmctl version matches the server one
       --suppress-warnings            disables printing warning messages

Install mmctl
-------------

The mmctl tool comes bundled with Mattermost package. For customers that want to setup it independently from the package, the following methods are available to install mmctl.

.. _install-mmctl-options:

.. tabs::

   .. tab:: Using release package (Linux, macOS, Windows)

      Starting with the release ``v8.0.0`` of Mattermost, you can download the mmctl builds at their release URL: ``https://releases.mattermost.com/mmctl/${MATTERMOST_VERSION}/${PLATFORM}_${ARCHITECTURE}.tar`` (for windows, substitute the ``.tar`` suffix with ``.zip``)

      E.g. to download version ``v8.0.0`` of the mmctl amd64 build for linux, you can run the following:

      .. code-block:: sh

         curl -vfsSL -O https://releases.mattermost.com/mmctl/v8.0.0/linux_amd64.tar

      Supported platforms, and corresponding supported architectures, are: linux (amd64 and arm64), darwin (amd64 and arm64), windows (amd64 only).

      For versions older than ``v8.0.0``, you can instead visit the `mmctl releases page <https://github.com/mattermost/mmctl/releases>`__ and download the appropriate release for your OS, and install the binary.

   .. tab:: Using go install (Linux, macOS, Windows)

      Use this option on Linux, macOS, and Windows if you have a ``go`` environment configured.

      To build and install the mmctl binary in your `$GOPATH`, run the following command:

      .. code-block:: sh

         # For Mattermost versions >= v8.0.0
         go install github.com/mattermost/mattermost/server/v8/cmd/mmctl@master

         # For Mattermost versions < v8.0.0
         go install github.com/mattermost/mmctl@latest

   .. tab:: Use brew (Linux, macOS)

      **NB: this is not an officially supported method.** This installation channel is managed by the community, please refer to the `homebrew/homebrew-core repo <https://github.com/Homebrew/homebrew-core>`__ for reporting issues.

      Use this option on Linux and macOS if you have Homebrew installed.

      .. code-block:: sh

         brew install mmctl

Build mmctl
------------

.. _build-mmctl:

The ``mmctl`` tool uses ``go`` modules to manage dependencies, so you need to have installed ``go`` 1.19 or greater on your machine.

After checking out the `mattermost repository <https://github.com/mattermost/mattermost>`__ locally to your machine, from the root directory of the project, you can compile the mmctl binary by running:

.. code-block:: sh

  make -C server mmctl-build

Local mode
----------

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

Local mode allows platform administrators with access to the Mattermost server to run mmctl commands against the API without needing to have a user registered. To ensure secure usage of this API, the server exposes a local socket that only a user with access to the server's file system can access. The requests coming from the socket are treated as authorized, so they can reach the handlers without requiring a user session.

The API that the socket exposes follows the same specification that can be found `in the API documentation <https://api.mattermost.com>`_, so mmctl is able to interact with it without needing any modifications. When a request comes in through the socket, it is flagged as local by the server, and this flag is taken into account when checking for session permissions to correctly authorize the sessions.

Activating local mode
~~~~~~~~~~~~~~~~~~~~~

To use local mode, the Mattermost server first needs to `have local mode enabled </configure/experimental-configuration-settings.html#enable-local-mode-for-mmctl>`_. When local mode is enabled, a socket is created at ``/var/tmp/mattermost_local.socket`` by default.

.. tip::

  When trying to use local mode with mmctl, ensure you're using the same user when running the server and mmctl, or clean up the socket file before switching to a new user. If you encounter an error like ``socket file "/var/tmp/mattermost_local.socket" doesn't exists, please check the server configuration for local mode``, this can be resolved by setting this configuration setting to ``true``.

Using local mode
~~~~~~~~~~~~~~~~

You need to append ``--local`` to the command you want to use, or set the environment variable as ``MMCTL_LOCAL=true``. To use a socket file other than the default, you need to set the environment variable to ``MMCTL_LOCAL_SOCKET_PATH``. This file must match the `server configuration setting </configure/configuration-settings.html#enable-local-mode-socket-location>`_.

Running mmctl tests
-------------------

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

mmctl has two types of tests: unit tests and end to end tests.

To execute them, you can run the following commands from the mattermost project root directory:

.. code-block:: sh

  # For the unit tests
  make -C server test-mmctl-unit

  # For the end to end tests
  make -C server test-mmctl-e2e

mmctl auth
----------

**Description**

Manage the credentials and authentication methods of remote Mattermost instances.

   Child Commands

      - `mmctl auth clean`_ - Clean credentials
      - `mmctl auth current`_ - Display current credentials
      - `mmctl auth delete`_ - Delete authentication details
      - `mmctl auth list`_ - List registered credentials
      - `mmctl auth login`_ - Log into Mattermost instance
      - `mmctl auth renew`_ - Renew login credentials
      - `mmctl auth set`_ - Set login credentials

**Options**

.. code-block:: sh

   -h, --help   help for auth

mmctl auth clean
~~~~~~~~~~~~~~~~

**Description**

Clean the credentials associated with a Mattermost instance.

**Format**

.. code-block:: sh

   mmctl auth clean [flags]

**Examples**

.. code-block:: sh

   mmctl auth clean

**Options**

.. code-block:: sh

   -h, --help   help for clean

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl auth current
~~~~~~~~~~~~~~~~~~

**Description**

Show the currently stored user credentials.

**Format**

.. code-block:: sh

   mmctl auth current [flags]

**Examples**

.. code-block:: sh

   mmctl auth current

**Options**

.. code-block:: sh

   -h, --help   help for current

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl auth delete
~~~~~~~~~~~~~~~~~

**Description**

Delete a named credential.

**Format**

.. code-block:: sh

   mmctl auth delete [server name] [flags]

**Examples**

.. code-block:: sh

   mmctl auth delete local-server

**Options**

.. code-block:: sh

   -h, --help   help for delete

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl auth list
~~~~~~~~~~~~~~~~

**Description**

Print a list of registered credentials.

**Format**

.. code-block:: sh

   mmctl auth list [flags]

**Examples**

.. code-block:: sh

   mmctl auth list

**Options**

.. code-block:: sh

   -h, --help   help for auth list

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl auth login
~~~~~~~~~~~~~~~~

**Description**

Log in to an instance and store credentials.

**Format**

.. code-block:: sh

   mmctl auth login [instance url] --name [server name] --username [username] --password-file [password-file] [flags]

**Examples**

.. code-block:: sh

   mmctl auth login https://mattermost.example.com
   mmctl auth login https://mattermost.example.com --name local-server --username sysadmin --password-file mysupersecret.txt
   mmctl auth login https://mattermost.example.com --name local-server --username sysadmin --password-file mysupersecret.txt --mfa-token 123456
   mmctl auth login https://mattermost.example.com --name local-server --access-token myaccesstoken

**Options**

.. code-block:: text

   -t, --access-token-file string   Access token file to be read to use instead of username/password
   -h, --help                       help for login
   -m, --mfa-token string           MFA token for the credentials
   -n, --name string                Name for the credentials
       --no-activate                If present, it won't activate the credentials after login
   -f, --password-file string       Password file to be read for the credentials
   -u, --username string            Username for the credentials

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl auth renew
~~~~~~~~~~~~~~~~

**Description**

Renew the credentials for a given server.

**Format**

.. code-block:: sh

   mmctl auth renew [flags]

**Examples**

.. code-block:: sh

   mmctl auth renew local-server

**Options**

.. code-block:: sh

   -t, --access-token-file string   Access token file to be read to use instead of username/password
   -h, --help                       help for renew
   -m, --mfa-token string           MFA token for the credentials
   -f, --password-file string       Password file to be read for the credentials

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl auth set
~~~~~~~~~~~~~~

**Description**

Set credentials to use in the following commands.

**Format**

.. code-block:: sh

   mmctl auth set [server name] [flags]

**Examples**

.. code-block:: sh

   mmctl auth set local-server

**Options**

.. code-block:: sh

   -h, --help   help for set

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

Authenticate to a server (e.g. >mmctl auth login https://test.mattermost.com), then enter your username and password (and MFA token if MFA is enabled on the account).

**Password**

.. code-block:: sh

   $ mmctl auth login https://community.mattermost.com --name community --username my-username --password-file mysupersecret

The ``login`` command can also work interactively, so if you leave any required flag empty, ``mmctl`` will ask you for it interactively:

.. code-block:: sh

   $ mmctl auth login https://community.mattermost.com
   Connection name: community
   Username: my-username
   Password File:

**MFA**

To log in with MFA, use the ``--mfa-token`` flag:

.. code-block:: sh

   $ mmctl auth login https://community.mattermost.com --name community --username my-username --password-file mysupersecret --mfa-token 123456

Access tokens
^^^^^^^^^^^^^

You can generate and use a personal access token to authenticate with a server, instead of using username and password to log in:

.. code-block:: sh

   $ mmctl auth login https://community.mattermost.com --name community --access-token MY_ACCESS_TOKEN

Alternatively, you can log in to your Mattermost server with a username and password:

.. code-block:: sh

   $ mmctl auth login https://my-instance.example.com --name my-instance --username john.doe --password-file mysupersecret
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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To install the shell completions for bash, add the following line to your ``~/.bashrc`` or ``~/.profile`` file:

.. code-block:: sh

   source <(mmctl completion bash)

For zsh, add the following line to your ``~/.zshrc`` file:

.. code-block:: sh

   source <(mmctl completion zsh)

mmctl bot
---------

Manage bots.

   Child Commands
      - `mmctl bot assign`_ - Assign bot ownership
      - `mmctl bot create`_ - Create a new bot
      - `mmctl bot disable`_ - Disable a bot
      - `mmctl bot enable`_ - Enable a bot
      - `mmctl bot list`_ - List all bots
      - `mmctl bot update`_ - Update bot configuration

**Options**

.. code-block:: sh

   -h, --help   help for bot

mmctl bot assign
~~~~~~~~~~~~~~~~

**Description**

Assign the ownership of a bot to another user.

**Format**

.. code-block:: sh

   mmctl bot assign [bot-username] [new-owner-username] [flags]

**Examples**

.. code-block:: sh

   mmctl bot assign testbot user2

**Options**

.. code-block:: sh

   -h, --help              help for assign

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl bot create
~~~~~~~~~~~~~~~~

**Description**

Create a bot.

**Format**

.. code-block:: sh

   mmctl bot create [username] [flags]

**Examples**

.. code-block:: sh

   mmctl bot create testbot

**Options**

.. code-block:: sh

   --description string    Optional. The description text for the new bot.
   --display-name string   Optional. The display name for the new bot.
   -h, --help              help for create
   --with-token            Optional. Auto genreate access token for the bot.

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl bot disable
~~~~~~~~~~~~~~~~~

**Description**

Disable an enabled bot.

**Format**

.. code-block:: sh

   mmctl bot disable [username] [flags]

**Examples**

.. code-block:: sh

   mmctl bot disable testbot

**Options**

.. code-block:: sh

   -h, --help     help for disable

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl bot enable
~~~~~~~~~~~~~~~~

**Description**

Enable a disabled bot.

**Format**

.. code-block:: sh

   mmctl bot enable [username] [flags]

**Examples**

.. code-block:: sh

   mmctl bot enable testbot

**Options**

.. code-block:: sh

   -h, --help              help for enable

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl bot list
~~~~~~~~~~~~~~

**Description**

List the bot's users.

**Format**

.. code-block:: sh

   mmctl bot list [flags]

**Examples**

.. code-block:: sh

   mmctl bot list

**Options**

.. code-block:: sh

   --all        Optional. Show all bots (including deleleted and orphaned)
   -h, --help   help for list
   --orphaned   Optional. Only show orphaned bots

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl bot update
~~~~~~~~~~~~~~~~

**Description**

Update bot information.

**Format**

.. code-block:: sh

   mmctl bot update [username] [flags]

**Examples**

.. code-block:: sh

   mmctl bot update testbot --username newbotusername

**Options**

.. code-block:: sh

   --description string    Optional. The new description text for the bot
   --display-name string   Optional. The new display name for the bot
   -h, --help              help for update
   --username string       Optional. The new username for the bot

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl channel
--------------

Manage channels.

   Child Commands
      -  `mmctl channel archive`_ - Archive a channel
      -  `mmctl channel create`_ - Create a channel
      -  `mmctl channel delete`_ - Delete a channel
      -  `mmctl channel list`_ - List all channels on specified teams
      -  `mmctl channel make-private`_ - Set a channel's type to "private" (Deprecated)
      -  `mmctl channel modify`_ - Modify a channel's type (private/public)
      -  `mmctl channel move`_ - Move channels to the specified team
      -  `mmctl channel rename`_ - Rename a channel
      -  `mmctl channel restore`_ - (Deprecated) Restore a channel from the archive
      -  `mmctl channel search`_ - Search a channel by name
      -  `mmctl channel unarchive`_ - Unarchive a channel
      -  `mmctl channel users`_ - Manage channel users
      -  `mmctl channel users add`_ - Add a user to a channel
      -  `mmctl channel users remove`_ - Remove a user from a channel

**Options**

.. code-block:: sh

   -h, --help   help for channel

mmctl channel archive
~~~~~~~~~~~~~~~~~~~~~

**Description**

Archive channels along with all related information including posts from the database. Channels can be specified by ``[team]:[channel]`` (i.e., ``myteam:mychannel``), or by channel ID.

**Format**

.. code-block:: sh

   mmctl channel archive [channels] [flags]

**Examples**

.. code-block:: sh

   mmctl channel archive myteam:mychannel

**Options**

.. code-block:: sh

   -h, --help   help for archive

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl channel create
~~~~~~~~~~~~~~~~~~~~

**Description**

Create a channel.

**Format**

.. code-block:: sh

   mmctl channel create [flags]

**Examples**

.. code-block:: sh

   mmctl channel create --team myteam --name mynewchannel --display-name "My New Channel"
   mmctl channel create --team myteam --name mynewprivatechannel --display-name "My New Private Channel" --private

**Options**

.. code-block:: sh

   --display-name string   Channel Display Name
   --header string         Channel header
   -h, --help              help for create
   --name string           Channel Name
   --private               Create a private channel
   --purpose string        Channel purpose
   --team string           Team name or ID

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl channel delete
~~~~~~~~~~~~~~~~~~~~

**Description**

Permanently delete channels along with all related information including posts from the database.

.. note::
   Requires the `Enable API Channel Deletion </configure/configuration-settings.html#enable-api-channel-deletion>`__ configuration setting to be enabled. If this configuration setting is disabled, attempting to delete the channel using mmctl fails.

**Format**

.. code-block:: sh

   mmctl channel delete [channels] [flags]

**Examples**

.. code-block:: sh

   mmctl channel delete myteam:mychannel

**Options**

.. code-block:: sh

   --confirm       Confirm you really want to delete the channel and a database backup has been performed.
   -h, --help      help for delete

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl channel list
~~~~~~~~~~~~~~~~~~~~

**Description**

List all Public, Private, and archived channels on specified teams. Archived channels are appended with ``(archived)``. Private channels the user is a member of, or has access to, are appended with ``(private)``.

**Format**

.. code-block:: sh

   mmctl channel list [teams] [flags]

**Examples**

.. code-block:: sh

   mmctl channel list myteam

**Options**

.. code-block:: sh

   -h, --help   help for list

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl channel make-private
~~~~~~~~~~~~~~~~~~~~~~~~~~

This command is deprecated in favour of using `mmctl channel modify </manage/mmctl-command-line-tool.html#mmctl-channel-modify>`__ and the ``--private`` flag instead.

**Description**

Set the type of a channel from Public to Private. Channel can be specified by ``[team]:[channel]`` (e.g., ``myteam:mychannel``), or by channel ID.

**Format**

.. code-block:: sh

   mmctl channel make-private [channel] [flags]

**Examples**

.. code-block:: sh

   mmctl channel make-private myteam:mychannel

**Options**

.. code-block:: sh

   -h, --help   help for make-private

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl channel modify
~~~~~~~~~~~~~~~~~~~~

**Description**

Change the Public/Private type of a channel. Channel can be specified by ``[team]:[channel]`` (e.g., ``myteam:mychannel``), or by channel ID.

**Format**

.. code-block:: sh

   mmctl channel modify [channel] [flags]

**Examples**

.. code-block:: sh

   mmctl channel modify myteam:mychannel --private
   mmctl channel modify channelId --public

**Options**

.. code-block:: sh

   -h, --help  help for modify
   --private   Convert the channel to a private channel
   --public    Convert the channel to a public channel

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl channel move
~~~~~~~~~~~~~~~~~~~

**Description**

Move the provided channels to the specified team. Validate that all users in the channel belong to the target team. Incoming/outgoing webhooks are moved along with the channel. Channels can be specified by ``[team]:[channel]`` (e.g., ``myteam:mychannel``), or by channel ID.

**Format**

.. code-block:: sh

   mmctl channel move [team] [channels] [flags]

**Examples**

.. code-block:: sh

   mmctl channel move newteam oldteam:mychannel

**Options**

.. code-block:: sh

   -h, --help    help for move
   --force       Remove users that are not members of target team before moving the channel.

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl channel rename
~~~~~~~~~~~~~~~~~~~~

**Description**

Rename an existing channel.

**Format**

.. code-block:: sh

   mmctl channel rename [channel] [flags]

**Examples**

.. code-block:: sh

   mmctl channel rename myteam:oldchannel --name 'new-channel' --display_name 'New Display Name'
   mmctl channel rename myteam:oldchannel --name 'new-channel'
   mmctl channel rename myteam:oldchannel --display_name 'New Display Name'

**Options**

.. code-block:: sh

   --display_name string   Channel Display Name
   -h, --help              help for rename
   --name string           Channel Name

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl channel restore
~~~~~~~~~~~~~~~~~~~~~

Deprecated in favor of `mmctl channel unarchive`_. Not used in Mattermost Server version v5.26 and later.

**Description**

Restore a previously deleted channel. Channels can be specified by ``[team]:[channel]`` (e.g., ``myteam:mychannel``), or by channel ID.

**Format**

.. code-block:: sh

   mmctl channel restore [channels] [flags]

**Examples**

.. code-block:: sh

   mmctl channel restore myteam:mychannel

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
~~~~~~~~~~~~~~~~~~~~

**Description**

Search a channel by channel name. Channels can be specified by team (e.g., ``--team myteam mychannel``), or by team ID.

**Format**

.. code-block:: sh

   mmctl channel search [channel]
   mmctl search --team [team] [channel] [flags]

**Examples**

.. code-block:: sh

   mmctl channel search mychannel
   mmctl channel search --team myteam mychannel

**Options**

.. code-block:: sh

   -h, --help      help for search
   --team string   team name or ID

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl channel unarchive
~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Unarchive a previously archived channel. Channels can be specified by ``[team]:[channel]`` (e.g., ``myteam:mychannel``), or by channel ID.

**Format**

.. code-block:: sh

   mmctl channel unarchive [channels] [flags]

**Examples**

.. code-block:: sh

   mmctl channel unarchive myteam:mychannel

**Options**

.. code-block:: sh

   -h, --help   help for unarchive

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl channel users
~~~~~~~~~~~~~~~~~~~~

**Description**

Manage channel users.

**Options**

.. code-block:: sh

   -h, --help   help for users

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl channel users add
~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Add users to a channel.

**Format**

.. code-block:: sh

   mmctl channel users add [channel] [users] [flags]

**Examples**

.. code-block:: sh

   mmctl channel users add myteam:mychannel user@example.com username

**Options**

.. code-block:: sh

   -h, --help   help for add

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl channel users remove
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Remove users from a channel.

**Format**

.. code-block:: sh

   mmctl channel users remove [channel] [users] [flags]

**Examples**

.. code-block:: sh

   mmctl channel users remove myteam:mychannel user@example.com username
   mmctl channel users remove myteam:mychannel --all-users

**Options**

.. code-block:: sh

   --all-users  Remove all users from the indicated channel
   -h, --help   help for remove

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl command
-------------

Manage slash commands.

   Child Commands
      -  `mmctl command archive`_ - Archive a slash command
      -  `mmctl command create`_ - Create a custom command
      -  `mmctl command delete`_ - (Deprecated) Delete a specified slash command
      -  `mmctl command list`_ - List slash commands on specified teams
      -  `mmctl command modify`_ - Modify a slash command
      -  `mmctl command move`_ - Move a slash command to a different team
      -  `mmctl command show`_ - Show a custom slash command

**Options**

.. code-block:: sh

   -h, --help      help for command

mmctl command archive
~~~~~~~~~~~~~~~~~~~~~~

**Description**

Archive a slash command. Commands can be specified by command ID.

**Format**

.. code-block:: sh

   mmctl command archive [commandID] [flags]

**Examples**

.. code-block:: sh

   mmctl command archive commandID

**Options**

.. code-block:: sh

   -h, --help   help for archive

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl command create
~~~~~~~~~~~~~~~~~~~~

**Description**

Create a custom slash command for the specified team.

**Format**

.. code-block:: sh

   mmctl command create [team] [flags]

**Examples**

.. code-block:: sh

   mmctl command create myteam --title MyCommand --description "My Command Description" --trigger-word mycommand --url http://localhost:8000/my-slash-handler --creator myusername --response-username my-bot-username --icon http://localhost:8000/my-slash-handler-bot-icon.png --autocomplete --post

**Options**

.. code-block:: text

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

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl command delete
~~~~~~~~~~~~~~~~~~~~

Deprecated in favor of `mmctl command archive`_.

**Description**

Delete a slash command. Commands can be specified by command ID.

**Format**

.. code-block:: sh

   mmctl command delete [flags]

**Examples**

.. code-block:: sh

   mmctl command delete commandID

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
~~~~~~~~~~~~~~~~~~~

**Description**

List all commands on specified teams.

**Format**

.. code-block:: sh

   mmctl command list [teams] [flags]

**Examples**

.. code-block:: sh

  mmctl command list myteam

**Options**

.. code-block:: sh

   -h, --help   help for list

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl command modify
~~~~~~~~~~~~~~~~~~~~

**Description**

Modify a slash command. Commands can be specified by command ID.

**Format**

.. code-block:: sh

   mmctl command modify [commandID] [flags]

**Examples**

.. code-block:: sh

   mmctl command modify commandID --title MyModifiedCommand --description "My Modified Command Description" --trigger-word mycommand --url http://localhost:8000/my-slash-handler --creator myusername --response-username my-bot-username --icon http://localhost:8000/my-slash-handler-bot-icon.png --autocomplete --post

**Options**

.. code-block:: text

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

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl command move
~~~~~~~~~~~~~~~~~~~

**Description**

Move a slash command to a different team. Commands can be specified by command ID.

**Format**

.. code-block:: sh

   mmctl command move [team] [commandID] [flags]

**Examples**

.. code-block:: sh

   mmctl command move newteam commandID

**Options**

.. code-block:: sh

   -h, --help   help for move

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl command show
~~~~~~~~~~~~~~~~~~~

**Description**

Show a custom slash command. Commands can be specified by command ID. Returns command ID, team ID, trigger word, display name, and creator username.

**Format**

.. code-block:: sh

   mmctl command show [commandID] [flags]

**Examples**

.. code-block:: sh

   mmctl command show commandID

**Options**

.. code-block:: sh

   -h, --help   help for show

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl completion
----------------

Generate autocompletion scripts for ``bash`` and ``zsh``.

   Child Commands
      -  `mmctl completion bash`_ - Edit the configuration settings
      -  `mmctl completion zsh`_ - Get the value of a configuration setting

**Options**

.. code-block:: sh

   -h, --help   help for completion

mmctl completion bash
~~~~~~~~~~~~~~~~~~~~~

**Description**

Generate the ``bash`` autocompletion scripts.

To load completion, run:

.. code-block:: sh

  . <(mmctl completion bash)

To configure your ``bash`` shell to load completions for each session, add the above line to your ``~/.bashrc``.

**Format**

.. code-block:: sh

   mmctl completion bash [flags]

**Options**

.. code-block:: sh

   -h, --help   help for bash

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl completion zsh
~~~~~~~~~~~~~~~~~~~~

**Description**

Generate the ``zsh`` autocompletion scripts.

To load completion, run:

.. code-block:: sh

   . <(mmctl completion zsh)

To configure your ``zsh`` shell to load completions for each session, add the above line to your ``~/.zshrc``.

**Format**

.. code-block:: sh

   mmctl completion zsh [flags]

**Options**

.. code-block:: sh

   -h, --help   help for zsh

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl config
------------

Configuration settings.

   Child Commands
      -  `mmctl config edit`_ - Edit the configuration settings
      -  `mmctl config get`_ - Get the value of a configuration setting
      -  `mmctl config migrate`_ - Migrate existing configuration between backends
      -  `mmctl config patch`_ - Patch the configuration
      -  `mmctl config reload`_ - Reload the server configuration
      -  `mmctl config reset`_ - Reset the configuration
      -  `mmctl config set`_ - Set the value of a configuration
      -  `mmctl config show`_ - Write the server configuration to STDOUT
      -  `mmctl config subpath`_ - Update client asset loading to use the configured subpath

**Options**

.. code-block:: sh

   -h, --help   help for config

mmctl config edit
~~~~~~~~~~~~~~~~~

**Description**

Open the editor defined in the EDITOR environment variable to modify the server's configuration. Once complete, save the file, then upload it to your server.

**Format**

.. code-block:: sh

   mmctl config edit [flags]

**Examples**

.. code-block:: sh

   mmctl config edit

**Options**

.. code-block:: sh

   -h, --help   help for edit

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl config get
~~~~~~~~~~~~~~~~~

**Description**

Get the value of a configuration setting by its name in dot notation.

**Format**

.. code-block:: sh

   mmctl config get [flags]

**Examples**

.. code-block:: sh

   mmctl config get SqlSettings.DriverName

**Options**

.. code-block:: sh

   -h, --help   help for get

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl config migrate
~~~~~~~~~~~~~~~~~~~~~

**Description**

Migrate a file-based configuration to (or from) a database-based configuration. Point the Mattermost server at the target configuration to start using it. This command only migrates the configuration data from one type to another.

.. note::

   To change the store type to use the database, a System Admin needs to set a ``MM_CONFIG`` `environment variable </configure/configuation-in-a-database.html#create-an-environment-file>`_ and restart the Mattermost server.

**Format**

.. code-block:: sh

   mmctl config migrate [from_config] [to_config] [flags]

**Examples**

.. code-block:: sh

   mmctl config migrate path/to/config.json "postgres://mmuser:mostest@localhost:5432/mattermost_test?sslmode=disable&connect_timeout=10"

**Options**

.. code-block:: sh

   -h, --help   help for migrate

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl config patch
~~~~~~~~~~~~~~~~~~

**Description**

Patch the server configuration with the specified configuration file.

**Format**

.. code-block:: sh

   mmctl config patch <config-file> [flags]

**Examples**

.. code-block:: sh

   mmctl config patch /path/to/config.json

**Options**

.. code-block:: sh

   -h, --help   help for reload

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl config reload
~~~~~~~~~~~~~~~~~~~

**Description**

Reload the server configuration and apply new settings.

**Format**

.. code-block:: sh

   mmctl config reload [flags]

**Examples**

.. code-block:: sh

   mmctl config reload

**Options**

.. code-block:: sh

   -h, --help   help for reload

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl config reset
~~~~~~~~~~~~~~~~~~~

**Description**

Reset the value of a configuration setting by its name in dot notation or a setting section. Accepts multiple values for array settings.

**Format**

.. code-block:: sh

   mmctl config reset [flags]

**Examples**

.. code-block:: sh

   mmctl config reset SqlSettings.DriverName LogSettings

**Options**

.. code-block:: sh

   --confirm   Confirm you really want to reset all configuration settings to the default value
   -h, --help  help for reset

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl config set
~~~~~~~~~~~~~~~~~

**Description**

Set the value of a config setting by its name in dot notation. Accepts multiple values for array settings.

**Format**

.. code-block:: sh

   mmctl config set [flags]

**Examples**

.. code-block:: sh

   mmctl config set SqlSettings.DriverName postgres
   mmctl config set SqlSettings.DataSourceReplicas "replica1" "replica2"

**Options**

.. code-block:: sh

   -h, --help   help for set

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl config show
~~~~~~~~~~~~~~~~~~

**Description**

Print the server configuration and write to STDOUT in JSON format.

**Format**

.. code-block:: sh

   mmctl config show [flags]

**Examples**

.. code-block:: sh

   mmctl config show

**Options**

.. code-block:: sh

   -h, --help   help for show

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl config subpath
~~~~~~~~~~~~~~~~~~~~~

**Description**

Update the hard-coded production client asset paths to take into account Mattermost running on a subpath. This command needs access to the Mattermost ``assets`` directory to be able to rewrite the paths.

**Format**

.. code-block:: sh

   mmctl config subpath [flags]

**Examples**

.. code-block:: sh

   # you can rewrite the assets to use a subpath
   mmctl config subpath --assets-dir /opt/mattermost/client --path /mattermost

   # the subpath can have multiple steps
   mmctl config subpath --assets-dir /opt/mattermost/client --path /my/custom/subpath

   # or you can fallback to the root path passing /
   mmctl config subpath --assets-dir /opt/mattermost/client --path /

**Options**

.. code-block:: sh

   -a, --assets-dir string   directory of the Mattermost assets in the local filesystem
   -h, --help                help for subpath
   -p, --path string         path to update the assets with

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl docs
----------

**Description**

Generate mmctl documentation.

**Format**

.. code-block:: sh

   mmctl docs [flags]

**Options**

.. code-block:: sh

   -d, --directory string   The directory where the docs would be generated in. (default "docs")
   -h, --help               help for docs

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl export
------------

Manage exports.

   Child Commands
      -  `mmctl export create`_ - Create an export file
      -  `mmctl export delete`_ - Delete an export file
      -  `mmctl export download`_ - Download export files
      -  `mmctl export generate-presigned-url`_ - Generate a pre-signed URL for an export file
      -  `mmctl export job`_ - List, show, and cancel export jobs
      -  `mmctl export job cancel`_ - Cancel export job
      -  `mmctl export job list`_ - List export jobs
      -  `mmctl export job show`_ - Show export job
      -  `mmctl export list`_ - List export files

**Options**

.. code-block:: sh

   -h, --help   help for group

mmctl export create
~~~~~~~~~~~~~~~~~~~

**Description**

Create an export file.

**Format**

.. code-block:: sh

  mmctl export create [flags]

**Options**

.. code-block:: sh

   --no-attachments              Omit to include file attachments in the export file.
   --include-archived-channels   Include archived channels in the export file.
   -h, --help                    help for create

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl export delete
~~~~~~~~~~~~~~~~~~~

**Description**

Delete an export file.

**Format**

.. code-block:: sh

  mmctl export delete [exportname] [flags]

**Example**

.. code-block:: sh

  mmctl export delete export_file.zip

**Options**

.. code-block:: sh

   -h, --help   help for delete

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages
   
mmctl export download
~~~~~~~~~~~~~~~~~~~~~

**Description**

Download export files.

**Format**

.. code-block:: sh

  mmctl export download [exportname] [filepath] [flags]

**Example**

.. code-block:: sh

   # You can indicate the name of the export and its destination path
   $ mmctl export download samplename sample_export.zip

   # If you only indicate the name, the path will match it
   $ mmctl export download sample_export.zip

**Options**

.. code-block:: sh

   -h, --help          help for download
   --num-retries int   Number of retries to resume a download. (Default is 5)
    
**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl export generate-presigned-url
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Generate a pre-signed URL for an export file in cases where a Mattermost Cloud export is large and challenging to download from the Mattermost server.

**Format**

.. code-block:: sh

  mmctl export generate-presigned-url [exportname] [flags]

**Options**

.. code-block:: sh
   
  -h, --help   help for generate-presigned-url

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl export job
~~~~~~~~~~~~~~~~

**Description**

List, show, and export jobs.

**Options**

.. code-block:: sh

  -h, --help   help for job

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl export job cancel
~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Cancel an export job.

**Format**

.. code-block:: sh

  mmctl export job cancel [exportJobID] [flags]

**Example**

.. code-block:: sh

   export job cancel o98rj3ur83dp5dppfyk5yk6osy

**Options**

.. code-block:: sh

   -h, --help     help for download
    
**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl export job list
~~~~~~~~~~~~~~~~~~~~~

**Description**

List export jobs. Export files include the Job ID in the file name.

**Format**

.. code-block:: sh

  mmctl export job list [flags]

**Example**

.. code-block:: sh

  mmctl export job list

**Options**

.. code-block:: sh

   --all            Fetch all export jobs. ``--page`` flag will be ignored if provided
   -h, --help       help for list
   --page int       Page number to fetch for the list of export jobs
   --per-page int   Number of export jobs to be fetched (default 200)

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl export job show
~~~~~~~~~~~~~~~~~~~~~

**Description**

Show export job.

**Format**

.. code-block:: sh

  mmctl export job show [exportJobID] [flags]

**Example**

.. code-block:: sh

  mmctl export job show
  
**Options**

.. code-block:: sh

   -h, --help   help for show

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl export list
~~~~~~~~~~~~~~~~~

**Description**

List export files. Export files include the job ID in the file name.

**Format**

.. code-block:: sh

   mmctl export list [flags]

**Options**

.. code-block:: sh

   -h, --help   help for list

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl extract
-------------

Manage content extraction jobs.

   Child Commands
      -  `mmctl extract job`_ - List and show content extraction jobs
      -  `mmctl extract run`_ - Start a content extraction job

**Options**

.. code-block:: sh

   -h, --help   help for list

mmctl extract job
~~~~~~~~~~~~~~~~~~

List and show content extraction jobs.

Child Commands
      -  `mmctl extract job list`_ - List content extraction jobs
      -  `mmctl extract job show`_ - Show extract job

mmctl extract job list
~~~~~~~~~~~~~~~~~~~~~~

**Description**

List content extraction jobs.

**Format**

.. code-block:: sh

   mmctl extract job list [flags]

**Examples**

.. code-block:: sh

   mmctl extract job list

**Options**

.. code-block:: sh

   --all            Fetch all export jobs. --page flag will be ignore if provided
   -h, --help       help for list
   --page int       Page number to fetch for the list of export jobs
   --per-page int   Number of export jobs to be fetched (default 200)

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl extract job show
~~~~~~~~~~~~~~~~~~~~~~

**Description**

Show extract job.

**Format**

.. code-block:: sh

   mmctl extract job show [extractJobID] [flags]

**Examples**

.. code-block:: sh

   mmctl extract job show f3d68qkkm7n8xgsfxwuo498rah

**Options**

.. code-block:: sh

   -h, --help   help for disable

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl extract run
~~~~~~~~~~~~~~~~~

**Description**

Start a content extraction job.

**Format**

.. code-block:: sh

   mmctl extract run [flags]

**Examples**

.. code-block:: sh

   mmctl extract run

**Options**

.. code-block:: sh

   --from int   The timestamp of the earliest file to extract, expressed in seconds since the unix epoch.
   -h, --help   help for run
   --to int     The timestamp of the latest file to extract, expressed in seconds since the unix epoch. Defaults to the current time.

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl group
-----------

Manage channel and team groups.

   Child Commands
      -  `mmctl group channel`_ - Manage channel groups
      -  `mmctl group list-ldap`_ - List LDAP groups
      -  `mmctl group team`_ - Manage team groups
      -  `mmctl group user`_ - Manage custom user groups

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Disable group constrains in the specified channel.

**Format**

.. code-block:: sh

   mmctl group channel disable [team]:[channel] [flags]

**Examples**

.. code-block:: sh

   mmctl group channel disable myteam:mychannel

**Options**

.. code-block:: sh

   -h, --help   help for disable

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl group channel enable
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Enable group constrains in the specified channel.

**Format**

.. code-block:: sh

   mmctl group channel enable [team]:[channel] [flags]

**Examples**

.. code-block:: sh

   mmctl group channel enable myteam:mychannel

**Options**

.. code-block:: sh

   -h, --help   help for enable

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl group channel list
~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

List the groups associated with a channel.

**Format**

.. code-block:: sh

   mmctl group channel list [team]:[channel] [flags]

**Examples**

.. code-block:: sh

   mmctl group channel list myteam:mychannel

**Options**

.. code-block:: sh

   -h, --help   help for list

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl group channel status
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Show the group constrain status for the specified channel.

**Format**

.. code-block:: sh

   mmctl group channel status [team]:[channel] [flags]

**Examples**

.. code-block:: sh

   mmctl group channel status myteam:mychannel

**Options**

.. code-block:: sh

   -h, --help   help for status

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl group list-ldap
~~~~~~~~~~~~~~~~~~~~~

**Description**

List LDAP groups.

**Format**

.. code-block:: sh

   mmctl group list-ldap [flags]

**Examples**

.. code-block:: sh

   mmctl group list-ldap

**Options**

.. code-block:: sh

   -h, --help   help for list-ldap

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl group team
----------------

Manage team groups.

   Child Commands
      -  `mmctl group team disable`_ - Disable group team constrains
      -  `mmctl group team enable`_ - Enable group team constrains
      -  `mmctl group team list`_ - List team groups
      -  `mmctl group team status`_ - Check group constrain status

**Options**

.. code-block:: sh

   -h, --help   help for group

mmctl group team disable
~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Disable group constrains in the specified team.

**Format**

.. code-block:: sh

   mmctl group team disable [team] [flags]

**Examples**

.. code-block:: sh
   
   mmctl group team disable myteam

**Options**

.. code-block:: sh

   -h, --help   help for disable

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl group team enable
~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Enable group constrains in the specified team.

**Format**

.. code-block:: sh

   mmctl group team enable [team] [flags]

**Examples**

.. code-block:: sh

   mmctl group team enable myteam

**Options**

.. code-block:: sh

   -h, --help   help for enable

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl group team list
~~~~~~~~~~~~~~~~~~~~~

**Description**

List the groups associated with a team.

**Format**

.. code-block:: sh

   mmctl group team list [team] [flags]

**Examples**

.. code-block:: sh

   mmctl group team list myteam

**Options**

.. code-block:: sh

   -h, --help   help for list

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl group team status
~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Show the group constrain status for the specified team.

**Format**

.. code-block:: sh

   mmctl group team status [team] [flags]

**Examples**

.. code-block:: sh

   mmctl group channel status myteam

**Options**

.. code-block:: sh

   -h, --help   help for status

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages
   
mmctl group user
----------------

Manage custom user groups.

   Child Commands
      - `mmctl group user restore`_ - Restore custom user group

**Options**

.. code-block:: sh

   -h, --help   help for group

mmctl group user restore
~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Restore custom user group.

**Format**

.. code-block:: sh

   mmctl group user restore [groupname] [flags]

**Examples**

.. code-block:: sh
   
   mmctl group user restore examplegroup

**Options**

.. code-block:: sh

   -h, --help   help for disable

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl import
------------

**Description**

Manage imports.

   Child Commands
      -  `mmctl import job`_ - List and show import jobs
      -  `mmctl import job list`_ - List import jobs
      -  `mmctl import job show`_ - Show import job
      -  `mmctl import list`_ - List all import files
      -  `mmctl import list available`_ - List available import files
      -  `mmctl import list incomplete`_ - List incomplete import files uploads
      -  `mmctl import process`_ - Start an import job
      -  `mmctl import upload`_ - Upload import files
      -  `mmctl import validate`_ - Validate an import file

**Options**

.. code-block:: sh

   -h, --help   help for import

mmctl import job
~~~~~~~~~~~~~~~~

**Description**

List and show import jobs.

**Options**

.. code-block:: sh

   -h, --help   help for status

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl import job list
~~~~~~~~~~~~~~~~~~~~~

**Description**

List import jobs

**Format**

.. code-block:: sh

     mmctl import job list [flags]

**Examples**

.. code-block:: sh

     mmctl import job list

**Options**

.. code-block:: sh

   --all            Fetch all import jobs. --page flag will be ignore if provided
   -h, --help       help for list
   --page int       Page number to fetch for the list of import jobs
   --per-page int   Number of import jobs to be fetched (default 200)

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl import job show
~~~~~~~~~~~~~~~~~~~~~

**Description**

Show import job.

**Format**

.. code-block:: sh

     mmctl import job show [importJobID] [flags] 

**Examples**

.. code-block:: sh

     mmctl import job show f3d68qkkm7n8xgsfxwuo498rah

**Options**

.. code-block:: sh

   -h, --help   help for status

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl import list
~~~~~~~~~~~~~~~~~

**Description**

List all import files.

**Examples**

.. code-block:: sh

     mmctl import list

**Options**

.. code-block:: sh

   -h, --help   help for status

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl import list available
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

List available import files.

**Format**

.. code-block:: sh

     mmctl import list available [flags]

**Examples**

.. code-block:: sh

     mmctl import list available

**Options**

.. code-block:: sh

   -h, --help   help for status

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl import list incomplete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

List incomplete import files uploads.

**Format**

.. code-block:: sh

     mmctl import list incomplete [flags]

**Examples**

.. code-block:: sh

     mmctl import list incomplete

**Options**

.. code-block:: sh

   -h, --help   help for status

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages 

mmctl import process
~~~~~~~~~~~~~~~~~~~~

**Description**

Start an import job.

**Format**

.. code-block:: sh

     mmctl import process [importname] [flags]

**Examples**

.. code-block:: sh

     mmctl import process 35uy6cwrqfnhdx3genrhqqznxc_import.zip

**Options**

.. code-block:: sh

   -h, --help   help for status

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl import upload
~~~~~~~~~~~~~~~~~~~

**Description**

Upload import files.

**Format**

.. code-block:: sh

     mmctl import upload [filepath] [flags]

**Examples**

.. code-block:: sh

     mmctl import upload import_file.zip

**Options**

.. code-block:: sh

   -h, --help        help for upload
   --resume          Set to true to resume an incomplete import upload.
   --upload string   The ID of the import upload to resume.

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl import validate
~~~~~~~~~~~~~~~~~~~~~

**Description**

Validate an import file.

**Format**

.. code-block:: sh

     mmctl import validate [filepath] [flags]

**Examples**

.. code-block:: sh

     import validate import_file.zip --team myteam --team myotherteam

**Options**

.. code-block:: sh

      -h, --help              help for validate
      --ignore-attachments    Don't check if the attached files are present in the archive
      --team stringArray      Predefined team[s] to assume as already present on the destination server. Implies ``--check-missing-teams``. The flag can be repeated.

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl integrity
---------------

**Description**

Perform a relational integrity check which returns information about any orphaned record found. This command can only be run using local mode.

**Format**

.. code-block:: sh

   mmctl integrity [flags]

**Options**

.. code-block:: sh

   --confirm       Confirm you really want to run a complete integrity check that may temporarily harm system performance
   -h, --help      help for integrity
   -v, --verbose   Show detailed information on integrity check results

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl ldap
----------

LDAP-related utilities.

   Child Commands
      -  `mmctl ldap idmigrate`_ - Migrate LDAP IdAttribute to a new value
      -  `mmctl ldap sync`_ - Sync all LDAP users and groups

**Options**

.. code-block:: sh

   -h, --help   help for ldap

mmctl ldap idmigrate
~~~~~~~~~~~~~~~~~~~~

**Description**

Migrate LDAP ``IdAttribute`` to a new value. Run this utility to change the value of your ID Attribute without your users losing their accounts. After running the command, you can change the ID Attribute to the new value in the System Console. For example, if your current ID Attribute was ``sAMAccountName`` and you wanted to change it to ``objectGUID``, you would:

1. Wait for an off-peak time when your users won’t be impacted by a server restart.
2. Run the command ``mmctl ldap idmigrate objectGUID``.
3. Update the config within the System Console to the new value ``objectGUID``.
4. Restart the Mattermost server.

**Format**

.. code-block:: sh

   mmctl ldap idmigrate <objectGUID> [flags]

**Examples**

.. code-block:: sh

   mmctl ldap idmigrate objectGUID

**Options**

.. code-block:: sh

   -h, --help   help for idmigrate

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl ldap sync
~~~~~~~~~~~~~~~

**Description**

Synchronize all LDAP users and groups now.

**Format**

.. code-block:: sh

   mmctl ldap sync [flags]

**Examples**

.. code-block:: sh

   mmctl ldap sync

**Options**

.. code-block:: sh

   -h, --help                  help for sync
   --include-removed-members   Include members who left or were removed from a group-synced team/channel. Useful in cases where synchronized groups are unlinked/re-linked for testing purposes, when LDAP users are deactivated and reactivated, or when a user leaves a team in error.

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl license
-------------

Manage the Mattermost license.

   Child Commands
      -  `mmctl license remove`_ - Remove the current license
      -  `mmctl license upload`_ - Upload a new license
      -  `mmctl license upload-string`_ - Upload a license from a string

**Options**

.. code-block:: sh

   -h, --help   help for license

mmctl license remove
~~~~~~~~~~~~~~~~~~~~

**Description**

Remove the current license and use Mattermost Team Edition.

**Format**

.. code-block:: sh

   mmctl license remove [flags]

**Examples**

.. code-block:: sh

   mmctl license remove

**Options**

.. code-block:: sh

   -h, --help   help for remove

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl license upload
~~~~~~~~~~~~~~~~~~~~

**Description**

Upload a license and replace the current license.

**Format**

.. code-block:: sh

   mmctl license upload [license] [flags]

**Examples**

.. code-block:: sh

   mmctl license upload /path/to/license/mylicensefile.mattermost-license

**Options**

.. code-block:: sh

   -h, --help   help for upload

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl license upload-string
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Upload a license from a string. Replaces the current license.

**Format**

.. code-block:: sh

   mmctl license upload-string [license] [flags]

**Examples**

.. code-block:: sh

   license upload-string "mylicensestring"

**Options**

.. code-block:: sh

   -h, --help   help for upload

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl logs
----------

**Description**

Display logs in a human-readable format. As the log format depends on the server, the ``--format`` flag cannot be used with this command.

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

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl permissions
-----------------

Manage permissions and roles.

   Child Commands
      -  `mmctl permissions add`_ - Add permissions to a role
      -  `mmctl permissions remove`_ - Remove permissions from a role
      -  `mmctl permissions reset`_ - Reset default permissions for a role
      -  `mmctl permissions role assign`_ - Assign users to role
      -  `mmctl permissions role show`_ - Show the role information
      -  `mmctl permissions role unassign`_ - Unassign users from a role

**Options**

.. code-block:: sh

   -h, --help   help for permissions

mmctl permissions add
~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available in legacy Mattermost Enterprise Edition E10 and E20*

**Description**

Add one or more permissions to an existing role.

**Format**

.. code-block:: sh

   mmctl permissions add <role> <permission...> [flags]

**Examples**

.. code-block:: sh

   mmctl permissions add system_user list_open_teams
   mmctl permissions add system_manager sysconsole_read_user_management_channels

**Options**

.. code-block:: sh

   -h, --help   help for add

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl permissions remove
~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available in legacy Mattermost Enterprise Edition E10 and E20*

**Description**

Remove one or more permissions from an existing role.

**Format**

.. code-block:: sh

   mmctl permissions remove <role> <permission...> [flags]

**Examples**

.. code-block:: sh

   mmctl permissions remove system_user list_open_teams
   mmctl permissions remove system_manager sysconsole_read_user_management_channels

**Options**

.. code-block:: sh

   -h, --help   help for remove

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl permissions reset
~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available in legacy Mattermost Enterprise Edition E10 and E20*

**Description**

Reset the given role's permissions to the default settings and overwrite custom settings.

**Format**

.. code-block:: sh

   mmctl permissions reset <role_name> [flags]

**Examples**

.. code-block:: sh

   # Reset the permissions of the 'system_read_only_admin' role.
   $ mmctl permissions reset system_read_only_admin

**Options**

.. code-block:: sh

   -h, --help   help for reset

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl permissions role assign
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available in legacy Mattermost Enterprise Edition E10 and E20*

**Description**

Assign users to a role by username. 

**Format**

.. code-block:: sh

   mmctl permissions role assign <role_name> <username...> [flags]

**Examples**

.. code-block:: sh

   # Assign users with usernames 'john.doe' and 'jane.doe' to the role named 'system_admin'.
   mmctl permissions role assign system_admin john.doe jane.doe

   # Examples using other system roles
   mmctl permissions role assign system_manager john.doe jane.doe
   mmctl permissions role assign system_user_manager john.doe jane.doe
   mmctl permissions role assign system_read_only_admin john.doe jane.doe

**Options**

.. code-block:: sh

   -h, --help   help for assign

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl permissions role show
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Show all the information about a role.

**Format**

.. code-block:: sh

   mmctl permissions role show <role_name> [flags]

**Examples**

.. code-block:: sh

   mmctl permissions show system_user

**Options**

.. code-block:: sh

   -h, --help   help for show

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl permissions role unassign
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Unassign users from a role by username. Available in Mattermost Professional and Mattermost Enterprise.

**Format**

.. code-block:: sh

   mmctl permissions role unassign <role_name> <username...> [flags]

**Examples**

.. code-block:: sh

   # Unassign users with usernames 'john.doe' and 'jane.doe' from the role named 'system_admin'.
   mmctl permissions unassign system_admin john.doe jane.doe

   # Examples using other system roles
   mmctl permissions unassign system_manager john.doe jane.doe
   mmctl permissions unassign system_user_manager john.doe jane.doe
   mmctl permissions unassign system_read_only_admin john.doe jane.doe

**Options**

.. code-block:: sh

   -h, --help   help for unassign

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl plugin
-------------

Manage plugins.

   Child Commands
      -  `mmctl plugin add`_ - Add plugins
      -  `mmctl plugin delete`_ - Remove plugins
      -  `mmctl plugin disable`_ - Disable plugins
      -  `mmctl plugin enable`_ - Enable plugins
      -  `mmctl plugin install-url`_ - Install plugin from URL
      -  `mmctl plugin list`_ - List plugins
      -  `mmctl plugin marketplace`_ - Manage Marketplace plugins
  
**Options**

.. code-block:: sh

   -h, --help   help for plugin

mmctl plugin add
~~~~~~~~~~~~~~~~

**Description**

Add plugins to your Mattermost server.

**Format**

.. code-block:: sh

   mmctl plugin add [plugins] [flags]

**Examples**

.. code-block:: sh

   mmctl plugin add hovercardexample.tar.gz pluginexample.tar.gz

**Options**

.. code-block:: sh

   -f, --force   overwrite a previously installed plugin with the same ID, if any
   -h, --help    help for add

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl plugin delete
~~~~~~~~~~~~~~~~~~~~

**Description**

Delete previously uploaded plugins from your Mattermost server.

**Format**

.. code-block:: sh

   mmctl plugin delete [plugins] [flags]

**Examples**

.. code-block:: sh

   mmctl plugin delete hovercardexample pluginexample

**Options**

.. code-block:: sh

   -h, --help   help for delete

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl plugin disable
~~~~~~~~~~~~~~~~~~~~

**Description**

Disable plugins. Disabled plugins are immediately removed from the user interface and logged out of all sessions.

**Format**

.. code-block:: sh

   mmctl plugin disable [plugins] [flags]

**Examples**

.. code-block:: sh

   mmctl plugin disable hovercardexample pluginexample

**Options**

.. code-block:: sh

   -h, --help   help for disable

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl plugin enable
~~~~~~~~~~~~~~~~~~~

**Description**

Enable plugins for use on your Mattermost server.

**Format**

.. code-block:: sh

   mmctl plugin enable [plugins] [flags]

**Examples**

.. code-block:: sh

   mmctl plugin enable hovercardexample pluginexample

**Options**

.. code-block:: sh

   -h, --help   help for enable

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl plugin install-url
~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Supply URLs to plugins compressed in a ``.tar.gz`` file. Plugins must be enabled in the server's config settings.

**Format**

.. code-block:: sh

   mmctl plugin install-url <url>... [flags]

**Examples**

.. code-block:: sh

   # You can install one plugin
   $ mmctl plugin install-url https://example.com/mattermost-plugin.tar.gz

   # Or install multiple plugins at a time
   $ mmctl plugin install-url https://example.com/mattermost-plugin-one.tar.gz https://example.com/mattermost-plugin-two.tar.gz

**Options**

.. code-block:: sh

   -f, --force   overwrite a previously installed plugin with the same ID, if any
   -h, --help    help for install-url

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl plugin list
~~~~~~~~~~~~~~~~~~

**Description**

List all enabled and disabled plugins installed on your Mattermost server.

**Format**

.. code-block:: sh

   mmctl plugin list [flags]

**Examples**

.. code-block:: sh

   mmctl plugin list

**Options**

.. code-block:: sh

   -h, --help   help for list

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl plugin marketplace
-------------------------

Manage Marketplace plugins.

   Child Commands
      -  `mmctl plugin marketplace install`_ - Install a plugin from the Plugin Marketplace
      -  `mmctl plugin marketplace list`_ - List plugins on the Plugin Marketplace

**Options**

.. code-block:: sh

   -h, --help   help for marketplace

mmctl plugin marketplace install
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Install a plugin available on the Plugin Marketplace server. The latest version of the plugin will be installed.

**Format**

.. code-block:: sh

   mmctl plugin marketplace install <id> [flags]

**Examples**

.. code-block:: sh

   $ mmctl plugin marketplace install jitsi

**Options**

.. code-block:: sh

   -h, --help   help for install

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl plugin marketplace list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Get all plugins available from the Plugin Marketplace server, merging data from locally installed plugins as well as prepackaged plugins shipped with the server.

**Format**

.. code-block:: sh

   mmctl plugin marketplace list [flags]

**Examples**

.. code-block:: sh

   # You can list all available plugins
   $ mmctl plugin marketplace list --all

   # Pagination options can be used
   $ mmctl plugin marketplace list --page 2 --per-page 10

   # Filtering narrows down the search
   $ mmctl plugin marketplace list --filter jit

   # You can retrieve only local plugins
   $ mmctl plugin marketplace list --local-only

**Options**

.. code-block:: sh

   --all             Fetch all plugins. --page flag will be ignore if provided
   --filter string   Filter plugins by ID, name or description
   -h, --help        help for list
   --local-only      Only retrieve local plugins
   --page int        Page number to fetch for the list of users
   --per-page int    Number of users to be fetched (default 200)

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl post
----------

Manage posts.

   Child Commands
      -  `mmctl post create`_ - Create a post
      -  `mmctl post list`_ - List posts for a channel

**Options**

.. code-block:: sh

   -h, --help   help for post

mmctl post create
~~~~~~~~~~~~~~~~~~

**Description**

Create a post.

**Format**

.. code-block:: sh

   mmctl post create [flags]

**Examples**

.. code-block:: sh

   mmctl post create myteam:mychannel --message "some text for the post"

**Options**

.. code-block:: sh

   -h, --help              help for create
   -m, --message string    Message for the post
   -r, --reply-to string   Post id to reply to

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl post list
~~~~~~~~~~~~~~~~

**Description**

List posts for a channel.

**Format**

.. code-block:: sh

   mmctl post list [flags]

**Examples**

.. code-block:: sh

   mmctl post list myteam:mychannel
   mmctl post list myteam:mychannel --number 20

**Options**

.. code-block:: sh

   -f, --follow         Output appended data as new messages are posted to the channel
   -h, --help           help for list
   -n, --number int     Number of messages to list (default 20)
   -i, --show-ids       Show posts ids
   -s, --since string   List messages posted after a certain time (ISO 8601)

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl roles
-----------

**Description**

Promote users to the System Admin role, or remove System Admin privileges from users.

**Format**

Promote users to the System Admin role:

.. code-block:: sh

   mmctl roles system_admin [users] [flags]

Remove System Admin privileges:

.. code-block:: sh

   mmctl roles member [users] [flags]

**Examples**

Promote a user to the System Admin role:

.. code-block:: sh

   mmctl roles system_admin john_doe

Promote multiple users to the System Admin role:

.. code-block:: sh

   mmctl roles system_admin john_doe jane_doe

Remove System Admin privileges from a user:

.. code-block:: sh

   mmctl roles member john_doe

Remove System Admin privileges from multiple users:

.. code-block:: sh

   mmctl roles member john_doe jane_doe

**Options**

.. code-block:: sh

   -h, --help   help for roles

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl saml
----------

SAML-related utilities.

Child Commands
      -  `mmctl saml auth-data-reset`_ - Reset AuthData field to Email

**Options**

.. code-block:: sh

   -h, --help   help for system

mmctl saml auth-data-reset
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Resets the AuthData field for SAML users to their email. Run this utility after setting the 'id' SAML attribute to an empty value.

**Format**

.. code-block:: sh

   mmctl saml auth-data-reset [flags]

**Examples**

.. code-block:: sh

   # Reset all SAML users' AuthData field to their email, including deleted users
   $ mmctl saml auth-data-reset --include-deleted

   # Show how many users would be affected by the reset
   $ mmctl saml auth-data-reset --dry-run

   # Skip confirmation for resetting the AuthData
   $ mmctl saml auth-data-reset -y

   # Only reset the AuthData for the following SAML users
   $ mmctl saml auth-data-reset --users userid1,userid2

**Options**

.. code-block:: sh

   --dry-run           Dry run only
   -h, --help          help for auth-data-reset
   --include-deleted   Include deleted users
   --users strings     Comma-separated list of user IDs to which the operation will be applied
   -y, --yes           Skip confirmation

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl sampledata
----------------

**Description**

Generate a sample data file and store it locally, or directly import it to the remote server.

**Format**

.. code-block:: sh

   mmctl sampledata [flags]

**Examples**

.. code-block:: sh

   # You can create a sampledata file and store it locally
   $ mmctl sampledata --bulk sampledata-file.jsonl

   # Or you can simply print it to the STDOUT
   $ mmctl sampledata --bulk -

   # You can customize the amount of entities to create
   $ mmctl sampledata -t 7 -u 20 -g 4

   # The sampledata file can be directly imported into the remote server by not specifying a ``--bulk``` flag
   $ mmctl sampledata

   # Sample users can be created with profile pictures
   $ mmctl sampledata --profile-images ./images/profiles

**Options**

.. code-block:: sh

   -b, --bulk string                Optional. Path to write a JSONL bulk file instead of uploading into the remote server.
   --channel-memberships int        The number of sample channel memberships per user in a team. (default 5)
   --channels-per-team int          The number of sample channels per team. (default 10)
   --deactivated-users int          The number of deactivated users.
   --direct-channels int            The number of sample direct message channels. (default 30)
   --group-channels int             The number of sample group message channels. (default 15)
   -g, --guests int                 The number of sample guests. (default 1)
   -h, --help                       help for sampledata
   --posts-per-channel int          The number of sample post per channel. (default 100)
   --posts-per-direct-channel int   The number of sample posts per direct message channel. (default 15)
   --posts-per-group-channel int    The number of sample posts per group message channel. (default 30)
   --profile-images string          Optional. Path to folder with images to randomly pick as user profile image.
   -s, --seed int                   Seed used for generating the random data (Different seeds generate different data). (default 1)
   --team-memberships int           The number of sample team memberships per user. (default 2)
   -t, --teams int                  The number of sample teams. (default 2)
   -u, --users int                  The number of sample users. (default 15)

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl system
------------

System management commands for interacting with the server state and configuration.

   Child Commands
      -  `mmctl system clearbusy`_ - Clear the busy state
      -  `mmctl system getbusy`_ - Get the current busy state
      -  `mmctl system setbusy`_ - Set the busy state to ``true``
      -  `mmctl system status`_ - Print the status of the server
      -  `mmctl system version`_ - Print the remote server version build number

**Options**

.. code-block:: sh

   -h, --help   help for system

mmctl system clearbusy
~~~~~~~~~~~~~~~~~~~~~~

**Description**

Clear the busy state which re-enables non-critical services.

**Format**

.. code-block:: sh

   mmctl system clearbusy [flags]

**Examples**

.. code-block:: sh

   mmctl system clearbusy

**Options**

.. code-block:: sh

   -h, --help   help for clearbusy

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl system getbusy
~~~~~~~~~~~~~~~~~~~~

**Description**

Get the server busy state (high load) and timestamp corresponding to when the server busy flag will be automatically cleared.

**Format**

.. code-block:: sh

   mmctl system getbusy [flags]

**Examples**

.. code-block:: sh

   mmctl system getbusy

**Options**

.. code-block:: sh

   -h, --help   help for getbusy

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl system setbusy
~~~~~~~~~~~~~~~~~~~~

**Description**

Set the busy state to ``true`` for the specified number of seconds which disables non-critical services.

**Format**

.. code-block:: sh

   mmctl system setbusy -s [seconds] [flags]

**Examples**

.. code-block:: sh

   mmctl system setbusy -s 3600

**Options**

.. code-block:: sh

   -h, --help           help for setbusy
   -s, --seconds uint   Number of seconds until server is automatically marked as not busy (default 3600)

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl system status
~~~~~~~~~~~~~~~~~~~~

**Description**

Print the server status which is calculated using several basic server healthchecks.

**Format**

.. code-block:: sh

   mmctl system status [flags]

**Examples**

.. code-block:: sh

   mmctl system status

**Options**

.. code-block:: sh

   -h, --help   help for status

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl system version
~~~~~~~~~~~~~~~~~~~~

**Description**

Print the server version build number of the currently connected Mattermost instance.

**Format**

.. code-block:: sh

   mmctl system version [flags]

**Examples**

.. code-block:: sh

   mmctl system version

**Options**

.. code-block:: sh

   -h, --help   help for version

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl team
----------

Manage teams.

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
~~~~~~~~~~~~~~~~~~

**Description**

Archive a team along with all related information including posts from the database.

**Format**

.. code-block:: sh

   mmctl team archive [teams] [flags]

**Examples**

.. code-block:: sh

   mmctl team archive myteam

**Options**

.. code-block:: sh

   --confirm   Confirm you really want to archive the team and a database backup has been performed
   -h, --help  help for archive

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl team create
~~~~~~~~~~~~~~~~~

**Description**

Create a team.

**Format**

.. code-block:: sh

   mmctl team create [flags]

**Examples**

.. code-block:: sh

   mmctl team create --name mynewteam --display_name "My New Team"
   mmctl team create --name private --display_name "My New Private Team" --private

**Options**

.. code-block:: sh

   --display_name string   Team Display Name
   --email string          Administrator Email (anyone with this email is automatically a team admin)
   -h, --help              help for create
   --name string           Team Name
   --private               Create a private team

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl team delete
~~~~~~~~~~~~~~~~~

**Description**

Permanently delete a team along with all related information including posts from the database.

.. note::
   Requires the `Enable API Team Deletion </configure/configuration-settings.html#enable-api-team-deletion>`__ configuration setting to be enabled. If this configuration setting is disabled, attempting to delete the team using mmctl fails.

**Format**

.. code-block:: sh

   mmctl team delete [teams] [flags]

**Examples**

.. code-block:: sh

   mmctl team delete myteam

**Options**

.. code-block:: sh

   --confirm   Confirm you really want to delete the team and a database backup has been performed
   -h, --help  help for delete

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl team list
~~~~~~~~~~~~~~~~

**Description**

List all teams on the server.

**Format**

.. code-block:: sh

   mmctl team list [flags]

**Examples**

.. code-block:: sh

   mmctl team list

**Options**

.. code-block:: sh

   -h, --help  help for list

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl team modify
~~~~~~~~~~~~~~~~~

**Description**

Modify a team's privacy setting to public or private.

**Format**

.. code-block:: sh

   mmctl team modify [teams] [flag] [flags]

**Examples**

.. code-block:: sh

   mmctl team modify myteam --private

**Options**

.. code-block:: sh

   -h, --help  help for modify
   --private   Modify team to be private
   --public    Modify team to be public

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl team rename
~~~~~~~~~~~~~~~~~

**Description**

Rename an existing team.

**Format**

.. code-block:: sh

   mmctl team rename [team] [flags]

**Examples**

.. code-block:: sh

   mmctl team rename old-team --display_name 'New Display Name'

**Options**

.. code-block:: sh

   --display_name string   Team Display Name
   -h, --help              help for rename

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl team restore
~~~~~~~~~~~~~~~~~~

**Description**

Restore archived teams.

**Format**

.. code-block:: sh

   mmctl team restore [teams] [flags]

**Examples**

.. code-block:: sh

   mmctl team restore myteam

**Options**

.. code-block:: sh

   -h, --help   help for restore

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl team search
~~~~~~~~~~~~~~~~~

**Description**

Search for teams based on name.

**Format**

.. code-block:: sh

   mmctl team search [teams] [flags]

**Examples**

.. code-block:: sh

   mmctl team search team1

**Options**

.. code-block:: sh

   -h, --help  help for search

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl team users
----------------

Manage team users.

   Child Commands
      -  `mmctl team users add`_ - Add users to a team
      -  `mmctl team users remove`_ - Remove users from a team

**Options**

.. code-block:: sh

   -h, --help       help for token

mmctl team users add
~~~~~~~~~~~~~~~~~~~~

**Description**

Add specified users to a team.

**Format**

.. code-block:: sh

   mmctl team users add [team] [users] [flags]

**Examples**

.. code-block:: sh

   mmctl team users add myteam user@example.com username

**Options**

.. code-block:: sh

   -h, --help  help for add

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl team users remove
~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Remove specified users from a team.

**Format**

.. code-block:: sh

   mmctl team users remove [team] [users] [flags]

**Examples**

.. code-block:: sh

   mmctl team users remove myteam user@example.com username

**Options**

.. code-block:: sh

   -h, --help  help for remove

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl token
-----------

Manage users' access tokens.

   Child Commands
      -  `mmctl token generate`_ - Generate token for a user
      -  `mmctl token list`_ - List users' tokens
      -  `mmctl token revoke`_ - Revoke tokens for a user

**Options**

.. code-block:: sh

   -h, --help       help for token

mmctl token generate
~~~~~~~~~~~~~~~~~~~~

**Description**

Generate token for a user.

**Format**

.. code-block:: sh

   mmctl token generate [user] [description] [flags]

**Examples**

.. code-block:: sh

   mmctl generate testuser test-token

**Options**

.. code-block:: sh

   -h, --help     help for generate

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl token list
~~~~~~~~~~~~~~~~~

**Description**

List the tokens belonging to a user.

**Format**

.. code-block:: sh

   mmctl token list [user] [flags]

**Examples**

.. code-block:: sh

   mmctl user tokens testuser

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

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl token revoke
~~~~~~~~~~~~~~~~~~

**Description**

Revoke tokens for a user.

**Format**

.. code-block:: sh

   mmctl token revoke [token-ids] [flags]

**Examples**

.. code-block:: sh

   mmctl revoke testuser test-token-id

**Options**

.. code-block:: sh

   -h, --help       help for revoke

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user
----------

Manage users.

   Child Commands
      -  `mmctl user activate`_ - Activate a user
      -  `mmctl user change-password`_ - Change a user's password
      -  `mmctl user convert`_ - Convert users to bots or convert bots to users
      -  `mmctl user create`_ - Create user
      -  `mmctl user deactivate`_ - Deactivate user
      -  `mmctl user delete`_ - Delete users
      -  `mmctl user deleteall`_ - Delete all users and all posts (local command only)
      -  `mmctl user demote`_ - Demote users to guests
      -  `mmctl user email`_ - Set user email
      -  `mmctl user invite`_ - Invite user
      -  `mmctl user list`_ - List users
      -  `mmctl user migrate-auth`_ - Bulk migrate user accounts authentication type
      -  `mmctl user reset-password`_ - Reset user password
      -  `mmctl user resetmfa`_ - Reset a user's MFA token
      -  `mmctl user search`_ - Search for a user
      -  `mmctl user username`_ - Change username of the user
      -  `mmctl user verify`_ - Mark user's email as verified

**Options**

.. code-block:: sh

   -h, --help       help for user

mmctl user activate
~~~~~~~~~~~~~~~~~~~~

**Description**

Activate users that have been deactivated.

**Format**

.. code-block:: sh

   mmctl user activate [emails, usernames, userIds] [flags]

**Examples**

.. code-block:: sh

   mmctl user activate user@example.com
   mmctl user activate username

**Options**

.. code-block:: sh

   -h, --help           help for activate

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user change-password
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Change the password of a user to the one provided. If the user is changing their own password, the flag ``--current`` must indicate the current password. The flag ``--hashed`` can be used to indicate that the new password has been introduced as already hashed.

**Format**

.. code-block:: sh

   mmctl user change-password <user> [flags]

**Examples**

.. code-block:: sh

   # If you have system permissions, you can change other user's passwords
   $ mmctl user change-password john_doe --password new-password

   # If you are changing your own password, you need to provide the current one
   $ mmctl user change-password my-username --current current-password --password new-password

   # You can ommit these flags to introduce them interactively
   $ mmctl user change-password my-username
   Are you changing your own password? (YES/NO): YES
   Current password:
   New password:

   # If you have system permissions, you can update the password with the already hashed new
   # password. The hashing method should be the same that the server uses internally.
   $ mmctl user change-password john_doe --password HASHED_PASSWORD --hashed

**Options**

.. code-block:: sh

   -c, --current string    The current password of the user. Use only if changing your own password
   --hashed                The supplied password is already hashed
   -h, --help              help for change-password
   -p, --password string   The new password for the user

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user convert
~~~~~~~~~~~~~~~~~~

**Description**

Convert user accounts to bots, or convert bots to user accounts.

**Format**

.. code-block:: sh

   mmctl user convert (--bot [emails] [usernames] [userIds] | --user <username> --password PASSWORD [--email EMAIL]) [flags]

**Examples**

.. code-block:: sh

   # You can convert a user to a bot providing an email, an ID, or a username
   $ mmctl user convert user@example.com --bot

   # Or you can convert multiple users at a time
   $ mmctl user convert user@example.com anotherUser --bot

   # You can convert a bot to a user and specify the email and password that the user will have after conversion
   $ mmctl user convert botusername --email new.email@email.com --password password --user

**Options**

.. code-block:: sh

   --bot                If supplied, convert users to bots
   --email string       The email address for the converted user account. Required when the "bot" flag is set
   --firstname string   The first name for the converted user account. Required when the "bot" flag is set
   -h, --help           help for convert
   --lastname string    The last name for the converted user account. Required when the "bot" flag is set
   --locale string      The locale (e.g., EN, FR) for the converted new user account. Required when the "bot" flag is set
   --nickname string    The nickname for the converted user account. Required when the "bot" flag is set
   --password string    The password for converted new user account. Required when "user" flag is set
   --system_admin       If supplied, the converted user will be a System Admin. Defaults to false. Required when the "bot" flag is set
   --user               If supplied, convert a bot to a user
   --username string    Username for the converted user account. Required when the "bot" flag is set

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user create
~~~~~~~~~~~~~~~~~

**Description**

Create a user.

**Format**

.. code-block:: sh

   mmctl user create [flags]

**Examples**

.. code-block:: sh

   # You can create a user
   $ mmctl user create --email user@example.com --username userexample --password Password1

   # You can define optional fields like first name, last name, and nickname
   $ mmctl user create --email user@example.com --username userexample --password Password1 --firstname User --lastname Example --nickname userex

   # You can also create the user as a System Admin
   $ mmctl user create --email user@example.com --username userexample --password Password1 --system-admin

   # You can verify user on creation if you have the correct permissions
   $ mmctl user create --email user@example.com --username userexample --password Password1 --system-admin --email-verified

**Options**

.. code-block:: sh

   --disable-welcome-email   Optional. If supplied, the new user will not receive a welcome email. Defaults to false
   --email string            Required. The email address for the new user account
   --email-verified          Optional. If supplied, the new user will have the email verified. Defaults to false
   --firstname string        Optional. The first name for the new user account
   --guest                   Optional. If supplied, the new user will be a guest. Defaults to false
   -h, --help                help for create
   --lastname string         Optional. The last name for the new user account
   --locale string           Optional. The locale (ex: en, fr) for the new user account
   --nickname string         Optional. The nickname for the new user account
   --password string         Required. The password for the new user account
   --system-admin            Optional. If supplied, the new user will be a system administrator. Defaults to false
   --username string         Required. Username for the new user account

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user deactivate
~~~~~~~~~~~~~~~~~~~~~

**Description**

Deactivate users. Deactivated users are immediately logged out of all sessions and are unable to log back in.

**Format**

.. code-block:: sh

   mmctl user deactivate [emails, usernames, userIds] [flags]

**Examples**

.. code-block:: sh

   mmctl user deactivate user@example.com
   mmctl user deactivate username

**Options**

.. code-block:: sh

   -h, --help       help for deactivate

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user delete
~~~~~~~~~~~~~~~~~

**Description**

Permanently delete users along with all related information including posts from the database.

.. note::
   Requires the `Enable API User Deletion </configure/configuration-settings.html#enable-api-user-deletion>`__ configuration setting to be enabled. If this configuration setting is disabled, attempting to delete the user using mmctl fails.

**Format**

.. code-block:: sh

   mmctl user delete [users] [flags]

**Examples**

.. code-block:: sh

   mmctl user delete user@example.com

**Options**

.. code-block:: sh

   --confirm   Confirm you really want to delete the user and a database backup has been performed
   -h, --help  help for delete

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user deleteall
~~~~~~~~~~~~~~~~~~~~

**Description**

Permanently delete all users and all related information including posts. This command can only be run in local mode.

**Format**

.. code-block:: sh

   mmctl user deleteall [flags]

**Examples**

.. code-block:: sh

   mmctl user deleteall

**Options**

.. code-block:: sh

   --confirm   Confirm you really want to delete the user and a database backup has been performed
   -h, --help  help for delete

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user demote
^^^^^^^^^^^^^^^^^

**Description**

Demote a user to a guest.

**Format**

.. code-block:: sh

  mmctl user demote [users] [flags]

**Examples**

.. code-block:: sh

  mmctl user demote user1 user2

**Options**

.. code-block:: sh

  -h, --help   help for demote

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user email
~~~~~~~~~~~~~~~~

**Description**

Change the email address associated with a user.

**Format**

.. code-block:: sh

  mmctl user email [user] [new email] [flags]

**Examples**

.. code-block:: sh

  mmctl user email testuser user@example.com
  
**Options**

.. code-block:: sh

  -h, --help       help for email

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user invite
~~~~~~~~~~~~~~~~~

**Description**

Send an email invite to a user to join a team. You can invite a user to multiple teams by listing them. You can specify teams by name or ID.

**Format**

.. code-block:: sh

   mmctl user invite [email] [teams] [flags]

**Examples**

.. code-block:: sh

   mmctl user invite user@example.com myteam
   mmctl user invite user@example.com myteam1 myteam2

**Options**

.. code-block:: sh

   -h, --help       help for invite

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user list
~~~~~~~~~~~~~~~~

**Description**

List all users.

**Format**

.. code-block:: sh

   mmctl user list [flags]

**Examples**

.. code-block:: sh

   mmctl user list

**Options**

.. code-block:: sh

   --all            Fetch all users. --page flag will be ignore if provided
   -h, --help       help for list
   --page int       Page number to fetch for the list of users
   --per-page int   Number of users to be fetched (default 200)
   --team string    If supplied, only users belonging to this team will be listed

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user migrate-auth
~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Migrate accounts from one authentication provider to another. For example, you can upgrade your authentication provider from email to LDAP.

**Format**

.. code-block:: sh

   mmctl user migrate-auth [from_auth] [to_auth] [migration-options] [flags]

**Arguments**

  **from_auth:**
      The authentication service to migrate users accounts from.
      Supported options: email, gitlab, google, ldap, office365, saml.

  **to_auth:**
      The authentication service to migrate users to.
      Supported options: ldap, saml.

  **migration-options (ldap):**
      match_field:
         The field that is guaranteed to be the same in both authentication services. For example, if the users emails are consistent set to email.
         Supported options: email, username.

  **migration-options (saml):**
      **users_file:**
         The path of a json file with the usernames and emails of all users to migrate to SAML. The username and email must be the same that the SAML service provider store. And the email must match with the email in mattermost database.

      .. code-block:: javascript

         Example json content:
         {
            "usr1@email.com": "usr.one",
            "usr2@email.com": "usr.two"
         }

**Examples**

.. code-block:: sh

   mmctl user migrate-auth email saml users.json

**Options**

.. code-block:: sh

   --auto         Automatically migrate all users. Assumes the usernames and emails are identical between Mattermost and SAML services. (saml only)
   --confirm      Confirm you really want to proceed with auto migration. (saml only)
   --force        Force the migration to occur even if there are duplicates on the LDAP server. Duplicates will not be migrated. (ldap only)
   -h, --help     help for migrate-auth

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user promote
^^^^^^^^^^^^^^^^^^

**Description**

Promote a guest to a user.

**Format**

.. code-block:: sh

   mmctl user promote [guests] [flags]

**Examples**

.. code-block:: sh

   mmctl user promote guest1 guest2

**Options**

.. code-block:: sh

   -h, --help   help for promote

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user reset-password
~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Send users an email to reset their password.

**Format**

.. code-block:: sh

   mmctl user reset-password [users] [flags]

**Examples**

.. code-block:: sh

   mmctl user reset-password user@example.com

**Options**

.. code-block:: sh

   -h, --help       help for reset-password

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user resetmfa
~~~~~~~~~~~~~~~~~~~~

**Description**

Turn off multi-factor authentication for a user. If MFA enforcement is enabled, the user will be forced to re-enable MFA as soon as they log in.

**Format**

.. code-block:: sh

   mmctl user resetmfa [users] [flags]

**Examples**

.. code-block:: sh

   mmctl user resetmfa user@example.com

**Options**

.. code-block:: sh

   -h, --help       help for resetmfa

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user search
~~~~~~~~~~~~~~~~~~

**Description**

Search for users based on username, email, or user ID.

**Format**

.. code-block:: sh

   mmctl user search [users] [flags]

**Examples**

.. code-block:: sh

   mmctl user search user1@mail.com user2@mail.com

**Options**

.. code-block:: sh

   -h, --help       help for search

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user username
~~~~~~~~~~~~~~~~~~~

**Description**

Change the username of the user.

**Format**

.. code-block:: sh

   mmctl user username [user] [new username] [flags]

**Examples**

.. code-block:: sh

   mmctl user username testuser newusername

**Options**

.. code-block:: sh

   -h, --help       help for version

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl user verify
~~~~~~~~~~~~~~~~~

**Description**

Mark user's email as verified without requiring user to complete email verification path.

**Format**

.. code-block:: sh

   mmctl user verify [users] [flags]

**Examples**

.. code-block:: sh

   mmctl user verify user1

**Options**

.. code-block:: sh

   -h, --help       help for version

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl version
-------------

**Description**

Print the version of mmctl.

**Format**

.. code-block:: sh

   mmctl version [flags]

**Options**

.. code-block:: sh

   -h, --help       help for version

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl webhook
-------------

**Description**

Manage webhooks.

   Child Commands
      -  `mmctl webhook create-incoming`_ - Create an incoming webhook
      -  `mmctl webhook create-outgoing`_ - Create an outgoing webhook
      -  `mmctl webhook delete`_ - Delete webhooks
      -  `mmctl webhook list`_ - List webhooks
      -  `mmctl webhook modify-incoming`_ - Modify an incoming webhook
      -  `mmctl webhook modify-outgoing`_ - Modify an outgoing webhook
      -  `mmctl webhook show`_ - Show a webhook

**Options**

.. code-block:: sh

   -h, --help       help for webhook

mmctl webhook create-incoming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Create an incoming webhook to allow external posting of messages to a specific channel.

**Format**

.. code-block:: sh

   mmctl webhook create-incoming [flags]

**Examples**

.. code-block:: sh

   mmctl webhook create-incoming --channel [channelID] --user [userID] --display-name [displayName] --description [webhookDescription] --lock-to-channel --icon [iconURL]

**Options**

.. code-block:: sh

   --channel string        Channel name or ID of the new webhook
   --description string    Incoming webhook description
   --display-name string   Incoming webhook display name
   -h, --help              help for create-incoming
   --icon string           Icon URL
   --lock-to-channel       Lock to channel
   --user string           The username, email, or ID of the user that the webhook should post as

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl webhook create-outgoing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Create an outgoing webhook to allow external posting of messages from a specific channel.

**Format**

.. code-block:: sh

   mmctl webhook create-outgoing [flags]

**Examples**

.. code-block:: sh

   mmctl webhook create-outgoing --team myteam --user myusername --display-name mywebhook --trigger-word "build" --trigger-word "test" --url http://localhost:8000/my-webhook-handler
    mmctl webhook create-outgoing --team myteam --channel mychannel --user myusername --display-name mywebhook --description "My cool webhook" --trigger-when start --trigger-word build --trigger-word test --icon http://localhost:8000/my-slash-handler-bot-icon.png --url http://localhost:8000/my-webhook-handler --content-type "application/json"

**Options**

.. code-block:: sh

   --channel string             Channel name or ID
   --content-type string        Content-type
   --description string         Outgoing webhook description
   --display-name string        Outgoing webhook display name
   -h, --help                   help for create-outgoing
   --icon string                Icon URL
   --team string                Team name or ID (required)
   --trigger-when string        When to trigger webhook (exact: for first word matches a trigger word exactly, start: for first word starts with a trigger word) (default "exact")
   --trigger-word stringArray   Word to trigger webhook (required)
   --url stringArray            Callback URL (required)
   --user string                The username, email, or ID of the user that the webhook should post as (required)

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl webhook delete
~~~~~~~~~~~~~~~~~~~~

**Description**

Delete a webhook with a given ID.

**Format**

.. code-block:: sh

   mmctl webhook delete [flags]

**Examples**

.. code-block:: sh

   mmctl webhook delete [webhookID]

**Options**

.. code-block:: sh

   -h, --help   help for delete

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl webhook list
~~~~~~~~~~~~~~~~~~

**Description**

Print a list of all webhooks.

**Format**

.. code-block:: sh

   mmctl webhook list [flags]

**Examples**

.. code-block:: sh

   mmctl webhook list myteam

**Options**

.. code-block:: sh

   -h, --help   help for list

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl webhook modify-incoming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Modify an existing incoming webhook by changing its title, description, channel, or icon URL.

**Format**

.. code-block:: sh

   mmctl webhook modify-incoming [flags]

**Examples**

.. code-block:: sh

   mmctl webhook modify-incoming [webhookID] --channel [channelID] --display-name [displayName] --description [webhookDescription] --lock-to-channel --icon [iconURL]

**Options**

.. code-block:: sh

   --channel string        Channel ID
   --description string    Incoming webhook description
   --display-name string   Incoming webhook display name
   -h, --help              help for modify-incoming
   --icon string           Icon URL
   --lock-to-channel       Lock to channel

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl webhook modify-outgoing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Description**

Modify an existing outgoing webhook by changing its title, description, channel, icon, url, content-type, or triggers.

**Format**

.. code-block:: sh

   mmctl webhook modify-outgoing [flags]

**Examples**

.. code-block:: sh

   mmctl webhook modify-outgoing [webhookId] --channel [channelId] --display-name [displayName] --description "New webhook description" --icon http://localhost:8000/my-slash-handler-bot-icon.png --url http://localhost:8000/my-webhook-handler --content-type "application/json" --trigger-word test --trigger-when start

**Options**

.. code-block:: sh

   --channel string             Channel name or ID
   --content-type string        Content-type
   --description string         Outgoing webhook description
   --display-name string        Outgoing webhook display name
   -h, --help                   help for modify-outgoing
   --icon string                Icon URL
   --trigger-when string        When to trigger webhook (exact: for first word matches a trigger word exactly, start: for first word starts with a trigger word)
   --trigger-word stringArray   Word to trigger webhook
   --url stringArray            Callback URL

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl webhook show
~~~~~~~~~~~~~~~~~~

**Description**

Show the webhook specified by ``[webhookId]``.

**Format**

.. code-block:: sh

   mmctl webhook show [webhookId] [flags]

**Examples**

.. code-block:: sh

   mmctl webhook show w16zb5tu3n1zkqo18goqry1je

**Options**

.. code-block:: sh

   -h, --help   help for show

**Options inherited from parent commands**

.. code-block:: sh

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages

mmctl websocket
---------------

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

   --config string                path to the configuration file (default "$XDG_CONFIG_HOME/mmctl/config")
   --disable-pager                disables paged output
   --insecure-sha1-intermediate   allows to use insecure TLS protocols, such as SHA-1
   --insecure-tls-version         allows to use TLS versions 1.0 and 1.1
   --json                         the output format will be in json format
   --local                        allows communicating with the server through a unix socket
   --quiet                        prevent mmctl to generate output for the commands
   --strict                       will only run commands if the mmctl version matches the server one
   --suppress-warnings            disables printing warning messages
