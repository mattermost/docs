Command Line Tools
==================

From the directory where the Mattermost server is installed, a ``mattermost`` command is available for configuring the system. For an overview of the Mattermost command line interface (CLI), `read this article <https://medium.com/@santosjs/plugging-in-to-the-mattermost-cli-8cdcef2bd1f6>`__ from Santos.

.. note::
   This CLI will be replaced in a future release with the `mmctl CLI <https://docs.mattermost.com/administration/mmctl-cli-tool.html>`__.

.. note::
  The CLI is run in a single node which bypasses the mechanisms that a `High Availability environment <https://docs.mattermost.com/deployment/cluster.html>`__ uses to perform actions across all nodes in the cluster. As a result, when running `CLI commands <https://docs.mattermost.com/administration/command-line-tools.html>`__ in a High Availability environment, tasks such as creating and deleting users or changing configuration settings require a server restart.

These ``mattermost`` commands include:

**General Administration**

-  Creating teams
-  Creating users
-  Assigning roles to users
-  Resetting user passwords
-  Inviting users to teams

**Advanced Administration**

-  Permanently deleting users (use cautiously - database backup recommended before use)
-  Permanently deleting teams (use cautiously - database backup recommended before use)

**Advanced Automation**

-  Creating channels
-  Inviting users to channels
-  Removing users from channels
-  Listing all channels for a team
-  Restoring previously deleted channels
-  Modifying a channel's public/private type
-  Migrating sign-in options
-  Resetting multi-factor authentication for a user
-  Creating sample data

**Diagnostics**

- Analyzing the database for relational consistency

.. contents::
    :backlinks: top
    :local:

Using the CLI
-------------

To run the CLI commands, you must be in the Mattermost root directory. On a default installation of Mattermost, the root directory is ``/opt/mattermost``. If you followed our standard `installation process <../guides/administrator.html#installing-mattermost>`__, you must run the commands as the user ``mattermost``. The name of the executable is ``mattermost``, and it can be found in the ``/opt/mattermost/bin`` directory.

**For example, to get the Mattermost version on a default installation of Mattermost:**

.. code-block:: bash

    cd /opt/mattermost/
    sudo -u mattermost bin/mattermost version

.. note::

Ensure you run the Mattermost binary as the ``mattermost`` user. Running it as ``root`` user (for example) may cause complications with permissions as the binary initiates plugins and accesses various files when running CLI commands. Running the server as ``root`` may result in ownership of the plugins and files to be overwritten as well as other potential permissions errors.

.. note::

   When running CLI commands on a Mattermost installation that has the configuration stored in the database, you might need to pass the database connection string as: 

.. code-block:: bash
 
   bin/mattermost --config="postgres://mmuser:mostest@localhost:5432/mattermost_test?sslmode=disable\u0026connect_timeout=10"

Using the CLI on GitLab Omnibus
-------------------------------

On GitLab Omnibus, you must be in the following directory when you run CLI commands: ``/opt/gitlab/embedded/service/mattermost``. Also, you must run the commands as the user *mattermost* and specify the location of the configuration file. The executable is ``/opt/gitlab/embedded/bin/mattermost``.

**For example, to get the Mattermost version on GitLab Omnibus:**

.. code-block:: bash

    cd /opt/gitlab/embedded/service/mattermost
    sudo /opt/gitlab/embedded/bin/chpst -e /opt/gitlab/etc/mattermost/env -P -U mattermost:mattermost -u mattermost:mattermost /opt/gitlab/embedded/bin/mattermost --config=/var/opt/gitlab/mattermost/config.json version

.. note::
   
   The example commands in the documentation are for a default installation of Mattermost. You must modify the commands so that they work on GitLab Omnibus.

Using the CLI on Docker Install
-------------------------------

On Docker install, the ``/mattermost/bin`` directory was added to ``PATH``, so you can use the CLI directly with the ``docker exec`` command. Note that the container name may be ``mattermostdocker_app_1`` if you installed Mattermost with ``docker-compose.yml``.

**For example, to get the Mattermost version on a Docker install:**

.. code-block:: bash

    docker exec -it <your-mattermost-container-name> mattermost version

Using the CLI on Docker Preview
-------------------------------

The preceding documentation and command reference below also applies to the `Mattermost docker preview image <https://github.com/mattermost/mattermost-docker-preview>`__.

Mattermost 3.6 and later
~~~~~~~~~~~~~~~~~~~~~~~~

The new CLI tool is supported in Mattermost 3.6 and later. To see available commands in the old CLI tool, see `Mattermost 3.5 and earlier`_.

.. note::
   
   For Mattermost 4.10 and earlier, the commands used the ``platform`` executable instead of ``mattermost``. For example, to check the Mattermost version, one would run ``./platform version`` instead of ``./mattermost version``.

Notes:

-  Parameters in CLI commands are order-specific.
-  If special characters (``!``, ``|``, ``(``, ``)``, ``\``, ``'``, and ``"``) are used, the entire argument needs to be surrounded by single quotes (e.g. ``-password 'mypassword!'``, or the individual characters need to be escaped out (e.g. ``-password mypassword\!``).
-  Team name and channel name refer to the handles, not the display names. So in the url ``https://community.mattermost.com/core/channels/town-square`` team name would be ``core`` and channel name would be ``town-square``.

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

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl channel add <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-add>`__.


Description
    Add users to a channel. If adding multiple users, use a space-separated list.

 Format
   .. code-block:: none

      mattermost channel add {channel} {users}

 Examples
   .. code-block:: none

      bin/mattermost channel add 8soyabwthjnf9qibfztje5a36h user@example.com username
      bin/mattermost channel add myteam:mychannel user@example.com username

mattermost channel archive
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl channel archive <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-archive>`__.


Description
    Archive a channel. Archived channels are not accessible to users, but remain in the database. To restore a channel from the archive, see `mattermost channel restore`_. Channels can be specified by {team}:{channel} using the team and channel names, or by using channel IDs.

  Format
    .. code-block:: none

      mattermost channel archive {channels}

  Examples
    .. code-block:: none

      bin/mattermost channel archive 8soyabwthjnf9qibfztje5a36h
      bin/mattermost channel archive myteam:mychannel

mattermost channel create
~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl channel create <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-create>`__.


Description
    Create a channel.

 Format
   .. code-block:: none

     mattermost channel create

 Examples
   .. code-block:: none

      bin/mattermost channel create --team myteam --name mynewchannel --display_name "My New Channel"
      bin/mattermost channel create --team myteam --name mynewprivatechannel --display_name "My New Private Channel" --private

 Options
   .. code-block:: none

      --display_name string   Channel Display Name
      --header string         Channel header
      --name string           Channel Name
      --private               Create a private channel.
      --purpose string        Channel purpose
      --team string           Team name or ID

mattermost channel delete
~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl channel delete <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-delete>`__.

Description
    Permanently delete a channel along with all related information, including posts from the database. Channels can be specified by {team}:{channel} using the team and channel names, or by using channel IDs.

  Format
    .. code-block:: none

      mattermost channel delete {channels}

  Examples
    .. code-block:: none

      bin/mattermost channel delete 8soyabwthjnf9qibfztje5a36h
      bin/mattermost channel delete myteam:mychannel

mattermost channel list
~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl channel list <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-list>`__.


Description
    List all channels on a specified team. Private channels are appended with ``(private)`` and archived channels are appended with ``(archived)``.

  Format
    .. code-block:: none

      mattermost channel list {teams}

  Example
    .. code-block:: none

      bin/mattermost channel list myteam

mattermost channel modify
~~~~~~~~~~~~~~~~~~~~~~~~~

Description
    Modify a channel's public/private type.

  Format
    .. code-block:: none

      mattermost channel modify

  Example
    .. code-block:: none

      bin/mattermost channel modify myteam:mychannel --username myusername --private

  Options
    .. code-block:: none

          --username [REQUIRED] Username of the user who is changing the channel privacy.
          --public   Change a private channel to be public.
          --private  Change a public channel to be private.

mattermost channel move
~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl channel move <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-move>`__.

Description
    Move channels to another team. The command validates that all users in the channel belong to the target team. Incoming/Outgoing webhooks are moved along with the channel. Channels can be specified by ``[team]:[channel]`` or by using channel IDs.

  Format
    .. code-block:: none

      mattermost channel move

  Example
    .. code-block:: none

      bin/mattermost channel move newteam 8soyabwthjnf9qibfztje5a36h --username myusername
      bin/mattermost channel move newteam myteam:mychannel --username myusername

  Options
    .. code-block:: none

          --username [REQUIRED] Username of the user who is moving the team.
          --remove-deactivated-users [OPTIONAL] When moving the channel, remove any users who have been deactivated who may be preventing the move.

mattermost channel remove
~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl channel remove <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-remove>`__.

Description
    Remove users from a channel.

  Format
    .. code-block:: none

      mattermost channel remove {channel} {users}

  Examples
    .. code-block:: none

      bin/mattermost channel remove 8soyabwthjnf9qibfztje5a36h user@example.com username
      bin/mattermost channel remove myteam:mychannel user@example.com username
      bin/mattermost channel remove myteam:mychannel --all-users

  Options
    .. code-block:: none

          --all-users string     Remove all users from the channel.

mattermost channel rename
~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl channel rename <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-rename>`__.

Description
    Rename a channel. Channels can be specified by *{team}:{channel}* using the team and channel names, or by using channel IDs.

  Format
    .. code-block:: none

      mattermost channel rename {channel} newchannelname --display_name "New Display Name"

  Examples
    .. code-block:: none

      bin/mattermost channel rename 8soyabwthjnf9qibfztje5a36h newchannelname --display_name "New Display Name"
      bin/mattermost channel rename myteam:mychannel newchannelname --display_name "New Display Name"

  Options
    .. code-block:: none

      --display_name string   Channel Display Name

mattermost channel restore
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl channel restore <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-restore>`__.

Description
    Restore a channel from the archive. Channels can be specified by {team}:{channel} using the team and channel names, or by using channel IDs.

  Format
    .. code-block:: none

      mattermost channel restore {channels}

  Examples
    .. code-block:: none

      bin/mattermost channel restore 8soyabwthjnf9qibfztje5a36h
      bin/mattermost channel restore myteam:mychannel

mattermost channel search
~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl channel search <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-channel-search>`__.

Description
    Search for a channel by channel name. Returns channel display name, channel Id, and indicates if it is private or archived. Private channels are appended with ``(private)`` and archived channels are appended with ``(archived)``.

  Format
    .. code-block:: none

      mattermost channel search {channelName}

  Examples
    .. code-block:: none

      bin/mattermost channel search mychannel
      bin/mattermost channel search --team myteam mychannel
      bin/mattermost channel search --team f1924a8db44ff3bb41c96424cdc20676 mychannel

  Options
    .. code-block:: none

      --team   Team Name or Team ID

mattermost command
------------------

  Description
    Commands for slash command management.

  Child Commands
    -  `mattermost command create`_ - Create a custom slash command for a specified team.
    -  `mattermost command delete`_ - Delete a slash command.
    -  `mattermost command list`_ - List all commands on specified teams or all teams by default.
    -  `mattermost command modify`_ - Modify a slash command.
    -  `mattermost command move`_ - Move a slash command to a different team.
    -  `mattermost command show`_ - Show a custom slash command.

mattermost command create
~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl command create <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-command-create>`__.

Description
    Create a custom slash command for a specified team.

  Format
    .. code-block:: none

      mattermost command create

  Examples
    .. code-block:: none

       bin/mattermost command create myteam --title MyCommand --description "My Command Description" --trigger-word mycommand --url http://localhost:8000/my-slash-handler --creator myusername --response-username my-bot-username --icon http://localhost:8000/my-slash-handler-bot-icon.png --autocomplete --post

  Options
    .. code-block:: none

          --title string                     Command Title
          --description string               Command Description
          --trigger-word string [REQUIRED]   Command Trigger Word
          --url  string   [REQUIRED]         Command Callback URL
          --creator string  [REQUIRED]       Command Creator's Username
          --response-username string         Command Response Username
          --icon string                      Command icon URL
          --autocomplete bool                Show command in autocomplete list
          --autocompleteDesc string          Short command description for autocomplete list
          --autocompleteHint string          Command arguments displayed as help in autocomplete list
          --post bool                        Use POST method for callback URL

mattermost command delete
~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl command delete <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-command-delete>`__.

Description
    Delete a slash command. Commands can be specified by command ID.

  Format
    .. code-block:: none

      mattermost command delete {commandID}

  Examples
    .. code-block:: none

       bin/mattermost command delete commandID

mattermost command list
~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl command list <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-command-list>`__.


Description
    List all commands on specified teams or all teams by default.

  Format
    .. code-block:: none

      mattermost command list {team}

  Examples
    .. code-block:: none

       bin/mattermost command list myteam

mattermost command modify
~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Modify a slash command. Commands can be specified by command ID.

.. note::
    Only fields that you want to modify need to be specified.  Also, when modifying the command's creator, the new creator specified must have the permission to create commands.


  Format
    .. code-block:: none

      mattermost command modify {commandID}

  Examples
    .. code-block:: none

       bin/mattermost command modify commandID --title MyModifiedCommand --description "My Modified Command Description" --trigger-word mycommand --url http://localhost:8000/my-slash-handler --creator myusername --response-username my-bot-username --icon http://localhost:8000/my-slash-handler-bot-icon.png --autocomplete --post

  Options
    .. code-block:: none

          --title string                     Command Title
          --description string               Command Description
          --trigger-word string              Command Trigger Word
          --url  string                      Command Callback URL
          --creator string                   Command Creator's Username
          --response-username string         Command Response Username
          --icon string                      Command Icon URL
          --autocomplete bool                Show command in autocomplete list
          --autocompleteDesc string          Short command description for autocomplete list
          --autocompleteHint string          Command arguments displayed as help in autocomplete list
          --post bool                        Use POST method for callback URL, else use GET method

mattermost command move
~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Move a slash command to a different team. Commands can be specified by {team}:{command-trigger-word}, or by using command IDs.

  Format
    .. code-block:: none

      mattermost command move

  Examples
    .. code-block:: none

      bin/mattermost command move newteam oldteam:command-trigger-word
      bin/mattermost command move newteam o8soyabwthjnf9qibfztje5a36h

mattermost command show
~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Show a custom slash command. Commands can be specified by command ID. Returns command ID, team ID, trigger word, display name and creator username.

  Format
    .. code-block:: none

      command show {commandID}

  Examples
    .. code-block:: none

      bin/mattermost command show commandID

mattermost config
-----------------

  Description
    Commands for managing the configuration file.

  Child Command
    - `mattermost config get`_ - Retrieve the value of a config setting by its name in dot notation.
    - `mattermost config migrate`_ - Migrate a file-based configuration to (or from) a database-based configuration.
    - `mattermost config reset`_ - Resets the value of a config setting by its name in dot notation or a setting section.
    - `mattermost config set`_ - Set the value of a config setting by its name in dot notation.
    - `mattermost config show`_ - Print the current mattermost configuration in an easy to read format.
    - `mattermost config validate`_ - Validate the configuration file.

mattermost config get
~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl config get <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-config-get>`__.

Description
    Retrieve the value of a config setting by its name in dot notation.

  Format
    .. code-block:: none

      mattermost config get {config.name}

  Examples
    .. code-block:: none

       bin/mattermost config get SqlSettings.DriverName

 Options
    .. code-block:: none

          --path string  Optional subpath; defaults to value in Site URL.

mattermost config migrate
~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Migrate a file-based configuration to (or from) a database-based configuration. Point the Mattermost server at the target configuration to start using it. If using SAML, ensure the SAML certificates and keys are accessible to also migrate into the database.

.. note::
    If a ``from`` parameter is not specified, the command will fall back to what is specified in --config.

  Format
    .. code-block:: none

      mattermost config migrate {config to read} {config to write}

  Examples
    .. code-block:: none

       bin/mattermost config migrate  path/to/config.json "postgres://mmuser:mostest@dockerhost:5432/mattermost_test?sslmode=disable&connect_timeout=10"

mattermost config reset
~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Resets the value of a config setting by its name in dot notation or a setting section to the default value. Accepts multiple values for array settings. When no parameters are given, it will reset all config settings.

  Format
    .. code-block:: none

      mattermost config reset {config.name} {setting section}

  Examples
    .. code-block:: none

       bin/mattermost config reset SqlSettings.DriverName LogSettings

  Options
    .. code-block:: none

       --confirm  Confirm you really want to reset the config setting and a backup has been performed.

mattermost config set
~~~~~~~~~~~~~~~~~~~~~

  Description
    Set the value of a config setting by its name in dot notation. Accepts multiple values for array settings.

  Format
    .. code-block:: none

      mattermost config set {config.name} {setting new value}

  Examples
    .. code-block:: none

       bin/mattermost config set SqlSettings.DriverName mysql

  Options
   .. code-block:: none

       --path string  Optional subpath; defaults to value in Site URL.

mattermost config show
~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl config <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-config-show>`__.

Description
    Print the current mattermost configuration in an easy to read format.

  Format
    .. code-block:: none

      mattermost config show

  Examples
    .. code-block:: none

       bin/mattermost config show

mattermost config validate
~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Makes sure the configuration file has the following properties:

    - Is valid JSON.
    - Has attributes of the correct type, such as *bool*, *int*, and *str*.
    - All entries are valid. For example, checks that entries are below the maximum length.

  Format
      .. code-block:: none

        mattermost config validate

  Example
      .. code-block:: none

        bin/mattermost config validate
	
mattermost db init
------------------

  Description
    Initializes the database for a given data source name (DSN), executes migrations, and loads custom defaults when specified.

  Format
    .. code-block:: none

      mattermost db init

  Examples
  
    Use the ``config`` flag to pass the DSN:
    
    .. code-block:: none

       mattermost db init --config postgres://localhost/mattermost
       
    Run this command to use the ``MM_CONFIG`` environment variable:
    
    .. code-block:: none
      
       MM_CONFIG=postgres://localhost/mattermost mattermost db init
    
    Run this command to set a custom defaults file to be loaded into the database: 
    
    .. code-block:: none
    
       MM_CUSTOM_DEFAULTS_PATH=custom.json MM_CONFIG=postgres://localhost/mattermost mattermost db init

mattermost export
-----------------

  Description
   Commands for exporting data for compliance and for merging multiple Mattermost instances.

  Child Commands
    -  `mattermost export actiance`_ - Export data from Mattermost in Actiance XML format. Requires a Mattermost Enterprise Edition E20 license.
    -  `mattermost export bulk`_ - Export data to a file compatible with the Mattermost `Bulk Import format <https://docs.mattermost.com/deployment/bulk-loading.html>`__
    -  `mattermost export csv`_ - Export data from Mattermost in CSV format. Requires a Mattermost Enterprise Edition E20 license.
    -  `mattermost export global-relay-zip`_ - Export data from Mattermost into a ZIP file containing emails to send to Global Relay for debug and testing purposes only. Requires a Mattermost Enterprise Edition E20 license.
    -  `mattermost export schedule`_ - Schedule an export job

mattermost export actiance
~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Export data from Mattermost in Actiance XML format.

  Format
    .. code-block:: none

      mattermost export actiance

  Example
    .. code-block:: none

      bin/mattermost export actiance --exportFrom=1513102632

  Options
    .. code-block:: none

          --exportFrom string     Unix timestamp (milliseconds since epoch, UTC) to export data from.

mattermost export bulk
~~~~~~~~~~~~~~~~~~~~~~

  Description
    Export data to a file compatible with the Mattermost `Bulk Import format <https://docs.mattermost.com/deployment/bulk-loading.html>`__.

  Format
    .. code-block:: none

      mattermost export bulk

  Example
    .. code-block:: none

      bin/mattermost export bulk file.json --all-teams

  Options
    .. code-block:: none

	--all-teams bool [REQUIRED]  Export all teams from the server.

mattermost export csv
~~~~~~~~~~~~~~~~~~~~~

  Description
    Export data from Mattermost in CSV format.

  Format
    .. code-block:: none

      mattermost export csv

  Example
    .. code-block:: none

      bin/mattermost export csv --exportFrom=1513102632

  Options
    .. code-block:: none

        --exportFrom string     Unix timestamp (seconds since epoch, UTC) to export data from.

mattermost export global-relay-zip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Export data from Mattermost into a zip file containing emails to send to Global Relay for debug and testing purposes only. This does not archive any information in Global Relay.

  Format
    .. code-block:: none

      mattermost export global-relay-zip

  Example
    .. code-block:: none

      bin/mattermost export global-relay-zip --exportFrom=1513102632

  Options
    .. code-block:: none

        --exportFrom string     Unix timestamp (seconds since epoch, UTC) to export data from.

mattermost export schedule
~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Schedule an export job in a format suitable for importing into a third-party archive system.

  Format
    .. code-block:: none

      mattermost export schedule

  Example
    .. code-block:: none

      bin/mattermost export schedule --format=actiance --exportFrom=1513102632

  Options
    .. code-block:: none

          --format string         Output file format. Currently, only ``actiance`` is supported.
          --exportFrom string     Unix timestamp (seconds since epoch, UTC) to export data from.
          --timeoutSeconds string Set how long the export should run for before timing out.

mattermost extract-documents-content 
-------------------------------------

  Description
    Extracts and indexes the contents of files shared prior to upgrading to Mattermost Server v5.35. Running this command is strongly recommended since search results for past file contents may be incomplete. If this command isn't run, users can search older files based on filename only.
    
    If you're using `Elasticsearch <https://docs.mattermost.com/deployment/elasticsearch.html>`__ search, you must rebuild the search index after running the content extraction command.
    
    If you're using `Bleve <https://docs.mattermost.com/deployment/bleve.html>`__ search, you must disable Bleve before running the content extraction command. Once extraction is complete, re-enable Bleve, then rebuild the search index.

    You can run this extraction command while the server is running. Running this command adds load to your server. For large deployments, or teams that share many large, text-heavy documents, we recommended you review our `hardware requirements <https://docs.mattermost.com/install/requirements.html#hardware-requirements>`__, and test `enabling content search <https://docs.mattermost.com/administration/config-settings.html#enable-document-search-by-content>`__ in a staging environment before enabling it in a production environment.
  
  Format
    .. code-block:: none
    
      mattermost extract-documents-content 

  Example
    .. code-block:: none
    
      extract-documents-content --from=12345
  
  Options
    .. code-block:: none
    
      	 --from    Optional. Unix timestamp (seconds since epoch, UTC) of the earliest file to extract. (default 0)
     	 --to 	   Optional. Unix timestamp (seconds since epoch, UTC) of the latest file to extract. (default now)

mattermost group
-----------------

  Description
    Commands for managing Mattermost groups.  For more information on Mattermost groups please see `this documentation. <https://docs.mattermost.com/deployment/ldap-group-sync.html>`_

  Child Commands
    -  `mattermost group channel`_ - Management of Mattermost groups linked to channels
    -  `mattermost group team`_ - Management of Mattermost groups linked to teams

mattermost group channel
------------------------

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl group channel <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-channel>`__.


  Description
    Commands for managing Mattermost groups linked to a channel.

  Child Commands
    -  `mattermost group channel enable`_ - Enables group constraint on the specified channel
    -  `mattermost group channel disable`_ - Disables group constraint on the specified channel
    -  `mattermost group channel list`_ - Lists the groups associated with a channel
    -  `mattermost group channel status`_ - Shows the group constraint status of the specified channel

mattermost group channel enable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl group channel enable <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-channel-enable>`__.


  Description
    Enables group constraint on the specified channel. When a channel is group constrained, channel membership is managed by linked groups instead of managed by manually adding and removing users.

.. note::
  To enable a group constraint on a specific channel, you must already have at least one group associated. See `AD/LDAP Group documentation <https://docs.mattermost.com/deployment/ldap-group-sync.html#add-default-teams-or-channels-for-the-group>`_ for more details on how to associate a group to a channel.


  Format
    .. code-block:: none

      mattermost group channel enable {team}:{channel}

  Examples
    .. code-block:: none

      bin/mattermost group channel enable myteam:mychannel

mattermost group channel disable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl group channel disable <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-channel-disable>`__.

Description
    Disables group constraint on the specified channel.

  Format
    .. code-block:: none

      mattermost group channel disable {team}:{channel}

  Examples
    .. code-block:: none

      bin/mattermost group channel disable myteam:mychannel

mattermost group channel list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl group channel list <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-channel-list>`__.

Description
    Lists the groups associated with a channel.

  Format
    .. code-block:: none

      mattermost group channel list {team}:{channel}

  Examples
    .. code-block:: none

      bin/mattermost group channel list myteam:mychannel


mattermost group channel status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl group channel status <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-channel-status>`__.

Description
    Shows the group constraint status of the specified channel. Returns "Enabled" when channel membership is managed by linked groups.  Returns "Disabled" when the channel membership is managed by manually adding and removing users.

  Format
    .. code-block:: none

      mattermost group channel status {team}:{channel}

  Examples
    .. code-block:: none

      bin/mattermost group channel status myteam:mychannel

mattermost group team
------------------------

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl group team <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-team>`__.

Description
    Commands for managing Mattermost groups linked to a team.

  Child Commands
    -  `mattermost group team enable`_ - Enables group constraint on the specified team
    -  `mattermost group team disable`_ - Disables group constraint on the specified team
    -  `mattermost group team list`_ - Lists the groups associated with a team
    -  `mattermost group team status`_ - Shows the group constraint status of the specified team

mattermost group team enable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl group team enable <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-team-enable>`__.

Description
    Enables group constraint on the specified team. When a team is group constrained, team membership is managed by linked groups instead of managed by manually inviting and removing users.

.. note::
  To enable a group constraint on a specific team, you must already have at least one group associated. See `AD/LDAP Group documentation <https://docs.mattermost.com/deployment/ldap-group-sync.html#add-default-teams-or-channels-for-the-group>`_ for more details on how to associate a group to a team.

  Format
    .. code-block:: none

      mattermost group team enable {team}

  Examples
    .. code-block:: none

      bin/mattermost group team enable myteam

mattermost group team disable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl group team disable <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-team-disable>`__.

Description
    Disables group constraint on the specified team.

  Format
    .. code-block:: none

      mattermost group team disable {team}

  Examples
    .. code-block:: none

      bin/mattermost group team disable myteam

mattermost group team list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl group team list <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-team-list>`__.

Description
    Lists the groups associated with a team.

  Format
    .. code-block:: none

      mattermost group team list {team}

  Examples
    .. code-block:: none

      bin/mattermost group team list myteam


mattermost group team status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl group team status <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-group-team-status>`__.

Description
    Shows the group constraint status of the specified team. Returns "Enabled" when team membership is managed by linked groups.  Returns "Disabled" when the team membership is managed by manually inviting and removing users.

  Format
    .. code-block:: none

      mattermost group team status {team}

  Examples
    .. code-block:: none

      bin/mattermost group team status myteam

mattermost help
---------------

  Description
    Generate full documentation in Markdown format for the Mattermost command line tools.

  Format
    .. code-block:: none

      mattermost help {outputdir}

mattermost import
-----------------

  Description
    Import data into Mattermost.

  Child Command
    -  `mattermost import bulk`_ - Import a Mattermost Bulk Import File.
    -  `mattermost import slack`_ - Import a team from Slack.

mattermost import bulk
~~~~~~~~~~~~~~~~~~~~~~

  Description
    Import data from a Mattermost Bulk Import File.

  Format
    .. code-block:: none

      mattermost import bulk {file}

  Options
    .. code-block:: none

          --apply         Save the import data to the database. Use with caution - this cannot be reverted.
          --validate      Validate the import data without making any changes to the system.
          --workers int   How many workers to run whilst doing the import. (default 2)

  Example
    .. code-block:: none

      bin/mattermost import bulk bulk-file.jsonl

mattermost import slack
~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Import a team from a Slack export zip file.

  Format
    .. code-block:: none

      mattermost import slack {team} {file}

  Example
    .. code-block:: none

      bin/mattermost import slack myteam slack_export.zip

mattermost integrity
--------------------

  Description
    Check database schema integrity as well as referential integrity of channels, slash commands, webhooks, posts, schemes, sessions, users, and teams. This process may temporarily affect live system performance, and should be used during off-peak periods.

  Format
    .. code-block:: none

      mattermost integrity

  Example
    .. code-block:: none

      bin/mattermost integrity --confirm --verbose

  Options
    .. code-block:: none

          --confirm   Optional. Skip the confirmation message which indicates that the complete integrity check may temporarily harm system performance. This is not recommended in production environments.
	  --verbose   Outputs a detailed report of number and type of orphaned records including ids (if any).


.. _command-line-tools-mattermost-jobserver:

mattermost jobserver
--------------------

  Description
    Start the Mattermost job server.

  Format
    .. code-block:: none

      mattermost jobserver

  Example
    .. code-block:: none

      bin/mattermost jobserver

mattermost ldap
---------------

  Description
    Commands to configure and synchronize AD/LDAP.

  Child Command
    -  `mattermost ldap idmigrate`_ - Migrate the LDAP Id Attribute to a new value
    -  `mattermost ldap sync`_ - Synchronize now

mattermost ldap idmigrate
~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Migrate LDAP Id Attribute to new value.

    Run this utility to change the value of your ID Attribute without your users losing their accounts. After running the command you can change the ID Attribute to the new value in your ``config.json``. For example, if your current ID Attribute was ``sAMAccountName`` and you wanted to change it to ``objectGUID``, you would:

    1. Wait for an off-peak time when your users won't be impacted by a server restart.
    2. Run the command ``mattermost ldap idmigrate objectGUID``.
    3. Edit your ``config.json`` and change your ``IdAttribute`` field to the new value ``objectGUID``.
    4. Restart the Mattermost server.

  Format
    .. code-block:: none

      mattermost ldap idmigrate {attribute}

  Example
    .. code-block:: none

      bin/mattermost ldap idmigrate objectGUID

mattermost ldap sync
~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl ldap sync <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-ldap-sync>`__.

Description
    Synchronize all AD/LDAP users now.

  Format
    .. code-block:: none

      mattermost ldap sync

  Example
    .. code-block:: none

      bin/mattermost ldap sync

mattermost license
------------------

  Description
    Commands to manage licensing.

  Child Command
    -  `mattermost license upload`_ - Upload a license.

mattermost license upload
~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl license upload <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-license-upload>`__.

Description
    Upload a license. This command replaces the current license if one is already uploaded.

  Format
    .. code-block:: none

      mattermost license upload {license}

  Example
    .. code-block:: none

      bin/mattermost license upload /path/to/license/mylicensefile.mattermost-license

.. note::
  The Mattermost server needs to be restarted after uploading a license file for any changes to take effect. Also, for cluster setups the license file needs to be uploaded to every node.

mattermost logs
------------------

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl logs <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-logs>`__.

Description
    Displays Mattermost logs in a human-readable format.

  Format
    .. code-block:: none

      mattermost logs

  Example
    .. code-block:: none

      bin/mattermost logs --logrus

  Options
    .. code-block:: none

          --logrus   Displays Mattermost logs in `logrus format <https://github.com/sirupsen/logrus>`_. Else, standard output is returned.


mattermost permissions
----------------------

  Description
    Commands to manage advanced permissions.

  Child Commands
    -  `mattermost permissions export`_ - Export Schemes and Roles.
    -  `mattermost permissions import`_ - Import Schemes and Roles from a permissions export.
    -  `mattermost permissions reset`_ - Reset the permissions system to its default state on new installs.

mattermost permissions export
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Prints to stdout a jsonl representation of Schemes and Roles from a Mattermost instance. Used to export
    Roles and Schemes from one Mattermost instance to another. The output is a jsonl representation with
    each line containing a json representation of a Scheme and its associated Roles. The output is intended
    to be used as the input of `mattermost permissions import`.

  Format
    .. code-block:: none

      mattermost permissions export

  Example
    .. code-block:: none

      bin/mattermost permissions export > my-permissions-export.jsonl

mattermost permissions import
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Creates Roles and Schemes on a Mattermost instance from a jsonl input file in the format outputted by
    `mattermost permissions export`.

  Format
    .. code-block:: none

      mattermost permissions import {file}

  Example
    .. code-block:: none

      bin/mattermost permissions import my-permissions-export.jsonl

mattermost permissions reset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Reset permissions for all users, including Admins, to their default state on new installs. Note: **this will delete
    all custom schemes**.

  Format
    .. code-block:: none

      mattermost permissions reset

  Example
    .. code-block:: none

      bin/mattermost permissions reset

  Options
    .. code-block:: none

          --confirm   Confirm you really want to reset the permissions system and a DB backup has been performed.

mattermost plugin
-----------------

  Description
    Commands to manage plugins.

  Child Commands
    -  `mattermost plugin add`_ - Add plugins to your Mattermost server.
    -  `mattermost plugin delete`_ - Delete previously uploaded plugins.
    -  `mattermost plugin disable`_ - Disable plugins.
    -  `mattermost plugin enable`_ - Enable plugins for use.
    -  `mattermost plugin list`_ - List plugins installed on your Mattermost server.

mattermost plugin add
~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl plugin add <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-plugin-add>`__.

Description
    Add plugins to your Mattermost server. If adding multiple plugins, use a space-separated list.

  Format
    .. code-block:: none

      mattermost plugin add {plugin tar file}

  Example
    .. code-block:: none

      bin/mattermost plugin add hovercardexample.tar.gz pluginexample.tar.gz

mattermost plugin delete
~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl plugin delete <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-plugin-delete>`__.

Description
    Delete previously uploaded plugins from your Mattermost server. If deleting multiple plugins, use a space-separated list.

  Format
    .. code-block:: none

      mattermost plugin delete {plugin_id}

  Example
    .. code-block:: none

      bin/mattermost plugin delete hovercardexample pluginexample

mattermost plugin disable
~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl plugin disable <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-plugin-disable>`__.

Description
    Disable plugins. Disabled plugins are immediately removed from the user interface and logged out of all sessions. If disabling multiple plugins, use a space-separated list.

  Format
    .. code-block:: none

      mattermost plugin disable {plugin_id}

  Example
    .. code-block:: none

      bin/mattermost plugin disable hovercardexample pluginexample

mattermost plugin enable
~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl plugin enable <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-plugin-enable>`__.

Description
    Enable plugins for use on your Mattermost server. If enabling multiple plugins, use a space-separated list.

  Format
    .. code-block:: none

      mattermost plugin enable {plugin_id}

  Example
    .. code-block:: none

      bin/mattermost plugin enable hovercardexample pluginexample

mattermost plugin list
~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl plugin list <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-plugin-list>`__.

Description
    List all active and inactive plugins installed on your Mattermost server.

  Format
    .. code-block:: none

      mattermost plugin list

  Example
    .. code-block:: none

      bin/mattermost plugin list

mattermost reset
----------------

  Description
    Completely erase the database causing the loss of all data. This resets Mattermost to its initial state.

  Format
    .. code-block:: none

      mattermost reset

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete everything and a DB backup has been performed.

mattermost roles
----------------

  Description
    Commands to manage user roles.

  Child Commands
    -  `mattermost roles member`_ - Remove System Admin privileges from a user
    -  `mattermost roles system_admin`_ - Make a user into a System Admin

mattermost roles member
~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Remove system admin privileges from a user.

  Format
    .. code-block:: none

      mattermost roles member {users}

  Example
    .. code-block:: none

      bin/mattermost roles member user1

mattermost roles system\_admin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Promote a user to a System Admin.

  Format
    .. code-block:: none

      mattermost roles system_admin {users}

  Example
    .. code-block:: none

      bin/mattermost roles system_admin user1

mattermost sampledata
---------------------

  Description
    .. versionadded:: 4.7
      Generate sample data and populate the Mattermost database. Supported in Mattermost v4.7 and later.

      The command generates one user as the System Administrator with a username ``sysadmin`` and password ``Sys@dmin-sample1``. Other users are generated following an index, e.g. with username ``user-1`` and password ``SampleUs@r-1``.

  Format
    .. code-block:: none

      mattermost sampledata

  Example
    .. code-block:: none

      bin/mattermost sampledata --seed 10 --teams 4 --users 30

  Options
    .. code-block:: none

          -u, --users int                      The number of sample users. (default 15)
              --profile-images string          Optional. Path to folder with images to randomly pick as user profile image.
          -t, --teams int                      The number of sample teams. (default 2)
              --team-memberships int           The number of sample team memberships per user. (default 2)
              --channels-per-team int          The number of sample channels per team. (default 10)
              --channel-memberships int        The number of sample channel memberships per user in a team. (default 5)
              --posts-per-channel int          The number of sample post per channel. (default 100)
              --direct-channels int            The number of sample direct message channels. (default 30)
              --group-channels int             The number of sample group message channels. (default 15)
              --posts-per-direct-channel int   The number of sample posts per direct message channel. (default 15)
              --posts-per-group-channel int    The number of sample post per group message channel. (default 30)
          -s, --seed int                       Seed used for generating the random data (Different seeds generate different data). (default 1)
          -b, --bulk string                    Optional. Path to write a JSONL bulk file instead of loading into the database.
          -w, --workers int                    How many workers to run during the import. (default 2)

mattermost server
-----------------

  Description
    Runs the Mattermost server.

  Format
    .. code-block:: none

      mattermost server

mattermost team
---------------

  Description
    Commands to manage teams.

  Child Commands
    -  `mattermost team add`_ - Add users to a team.
    -  `mattermost team archive`_ - Archive teams based on name.
    -  `mattermost team create`_ - Create a team.
    -  `mattermost team delete`_ - Delete a team.
    -  `mattermost team list`_ - List all teams.
    -  `mattermost team modify`_ - Modify a team's public/private type.
    -  `mattermost team remove`_ - Remove users from a team.
    -  `mattermost team rename`_ - Rename a team.
    -  `mattermost team restore`_ - Restore a previously archived team.
    -  `mattermost team search`_ - Search for teams based on name.

.. _team-value-note:

.. note::
    **{team-name} value**

    For the *add*, *delete*, and *remove* commands, you can determine the *{team-name}* value from the URLs that you use to access your instance of Mattermost. For example, in the following URL the *{team-name}* value is *myteam*:

    ``https://example.com/myteam/channels/mychannel``

    Also, the team and channel names in the URL should be written in lowercase.

mattermost team add
~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl team add <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-team-add>`__.

Description
    Add users to a team. Before running this command, see the :ref:`note about {team-name} <team-value-note>`.

  Format
    .. code-block:: none

      mattermost team add {team-name} {users}

  Example
    .. code-block:: none

      bin/mattermost team add myteam user@example.com username

mattermost team archive
~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl team archive <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-team-archive>`__.


Description
    Archive teams based on name. Before running this command, see the :ref:`note about {team-name} <team-value-note>`.

  Format
    .. code-block:: none

      mattermost team archive {team}

  Examples
    .. code-block:: none

       bin/mattermost team archive team1

mattermost team create
~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl team create <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-team-create>`__.

Description
    Create a team.

  Format
    .. code-block:: none

      mattermost team create

  Examples
    .. code-block:: none

      bin/mattermost team create --name mynewteam --display_name "My New Team"
      bin/mattermost teams create --name private --display_name "My New Private Team" --private

  Options
    .. code-block:: none

          --display_name string   Team Display Name
          --email string          Administrator Email (anyone with this email is automatically a team admin)
          --name string           Team Name
          --private               Create a private team.

mattermost team delete
~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl team delete <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-team-delete>`__.

Description
    Permanently delete a team along with all related information, including posts from the database. Before running this command, see the :ref:`note about {team-name} <team-value-note>`.

  Format
    .. code-block:: none

      mattermost team delete {team-name}

  Example
    .. code-block:: none

      bin/mattermost team delete myteam

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete the team and a DB backup has been performed.

mattermost team list
~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl team list <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-team-list>`__.

*Supported in Mattermost v4.10 and later*

  Description
    List all teams on the server.

  Format
    .. code-block:: none

      mattermost team list

  Example
    .. code-block:: none

      bin/mattermost team list

mattermost team modify
~~~~~~~~~~~~~~~~~~~~~~

  Description
    Modify a team's public/private type.

  Format
    .. code-block:: none

      mattermost team modify [team] [flag]

  Example
    .. code-block:: none

      bin/mattermost modify team myteam --private
      bin/mattermost modify team myteam --public

mattermost team remove
~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl team remove <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-team-remove>`__.

Description
    Remove users from a team. Before running this command, see the :ref:`note about {team-name} <team-value-note>`.

  Format
    .. code-block:: none

      mattermost team remove {team-name} {users}

  Example
    .. code-block:: none

      bin/mattermost team remove myteam user@example.com username

mattermost team rename
~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl team rename <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-team-rename>`__.

Description
    Rename a team.

  Format
    .. code-block:: none

      mattermost team rename {team} newteamname --display_name "New Display Name"

  Examples
    .. code-block:: none

      bin/mattermost team rename myteam newteamname --display_name "New Display Name"

  Options
    .. code-block:: none

      --display_name string   Team Display Name

mattermost team restore
~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Restore a previously archived team.

  Format
    .. code-block:: none

      mattermost team restore {team}

  Example
    .. code-block:: none

      bin/mattermost team restore myteam

mattermost team search
~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl team search <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-team-search>`__.

Description
    Search for teams based on name. Before running this command, see the :ref:`note about {team-name} <team-value-note>`.

  Format
    .. code-block:: none

      mattermost team search {team}

  Examples
    .. code-block:: none

       bin/mattermost team search team1

mattermost user
---------------

  Description
    Commands to manage users.

  Child Commands

    -  `mattermost user activate`_ - Activate a user
    -  `mattermost user convert`_ - Convert a user to a bot, or a bot to a user
    -  `mattermost user create`_ - Create a user
    -  `mattermost user deactivate`_ - Deactivate a user
    -  `mattermost user delete`_ - Delete a user and all posts
    -  `mattermost user deleteall`_ - Delete all users and all posts
    -  `mattermost user email`_ - Set a user's email
    -  `mattermost user invite`_ - Send a user an email invitation to a team
    -  `mattermost user migrate_auth`_ - Mass migrate all user accounts to a new authentication type
    -  `mattermost user password`_ - Set a user's password
    -  `mattermost user resetmfa`_ - Turn off MFA for a user
    -  `mattermost user search`_ - Search for users based on username, email, or user ID
    -  `mattermost user verify`_ - Verify email address of a new user

~~~~~~~~~~~~~~~~~~~~~~~~

mattermost user activate
~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl user activate <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-user-activate>`__.

Description
    Activate users that have been deactivated. If activating multiple users, use a space-separated list.

  Format
    .. code-block:: none

      mattermost user activate {emails, usernames, userIds}

  Examples
    .. code-block:: none

      bin/mattermost user activate user@example.com
      bin/mattermost user activate username1 username2

mattermost user convert
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Convert a user to a bot, or convert a bot to a user account.

  Format
    .. code-block:: none

      mattermost user convert {emails, usernames, userIds} --bot
      OR
      mattermost user convert {bot_id} --user --email {email_address} --password {new_password}

  Examples
    .. code-block:: none

      bin/mattermost user convert user@example.com --bot
      bin/mattermost user convert username1 username2 --bot
      bin/mattermost user convert old_bot --user --email real_user@example.com --password Password1


  Options
    .. code-block:: none

          --bot string       Convert user to bot.  Supports converting multiple bots at once, use a space-separated list.
          --user string      Convert bot to user.  Supports converting 1 account per command. The converted user will have the role of `system_user` set.

mattermost user create
~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl user create <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-user-create>`__.


Description
    Create a user.

  Format
    .. code-block:: none

      mattermost user create

  Examples
    .. code-block:: none

      bin/mattermost user create --email user@example.com --username userexample --password Password1
      bin/mattermost user create --firstname Joe --system_admin --email joe@example.com --username joe --password Password1

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

mattermost user deactivate
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl user deactivate <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-user-deactivate>`__.

Description
    Deactivate a user. Deactivated users are immediately logged out of all sessions and are unable to log back in.

  Format
    .. code-block:: none

      mattermost user deactivate {emails, usernames, userIds}

  Examples
    .. code-block:: none

      bin/mattermost user deactivate user@example.com
      bin/mattermost user deactivate username

  .. note::
    Users deactivated via this CLI command can continue to use Mattermost, if they are already logged in, until the user cache is manually purged or automatically after 30 minutes. Users who are deactivated when they're not logged in will not be able to log in to Mattermost again.

    If you want to immediately terminate a deactivated user's session, purge all caches in **System Console > Web Server > Purge All Caches** after running this command.

    You can also use the `API command <https://api.mattermost.com/#tag/users%2Fpaths%2F~1users~1%7Buser_id%7D%2Fdelete>`_ to deactivate a user account and immediately terminate the session.

mattermost user delete
~~~~~~~~~~~~~~~~~~~~~~

  Description
    Permanently delete a user and all related information, including posts from the database.

    Does not delete content from the file storage. You can manually delete all file uploads for a given user as uploads contain the ``CreatorId`` field. User avatars are stored in ``data/users/<userid>/profile.png``.

  Format
    .. code-block:: none

      mattermost user delete {users}

  Example
    .. code-block:: none

      bin/mattermost user delete user@example.com

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete the user and a DB backup has been performed.

mattermost user deleteall
~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Permanently delete all users and all related information, including posts.

    Does not delete content from the file storage. You can manually delete all file uploads and avatars. All uploads contain the ``CreatorId`` field and user avatars are stored in ``data/users/<userid>/profile.png``.

  Format
    .. code-block:: none

      mattermost user deleteall

  Example
    .. code-block:: none

      bin/mattermost user deleteall

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete the user and a DB backup has been performed.

mattermost user email
~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl user email <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-user-email>`__.


Description
    Set a user's email.

  Format
    .. code-block:: none

       mattermost user email {user} {new email}

  Example
    .. code-block:: none

      bin/mattermost user email user@example.com newuser@example.com

mattermost user invite
~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl user invite <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-user-invite>`__.


Description
    Send a user an email invite to a team. You can invite a user to multiple teams by listing the team names or team IDs.

  Format
    .. code-block:: none

      mattermost user invite {email} {teams}

  Examples
    .. code-block:: none

      bin/mattermost user invite user@example.com myteam
      bin/mattermost user invite user@example.com myteam1 myteam2

mattermost user migrate_auth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _cli-user-migrate-auth:

  Description
    Migrates all existing Mattermost user accounts from one authentication provider to another. For example, you can upgrade your authentication provider from email to AD/LDAP, or from AD/LDAP to SAML. Output will display any accounts that are not migrated successfully. These accounts might be blocked because of filters in your AD/LDAP configuration in the System Console.

**Migrate to AD/LDAP**

  Parameters
    -  ``from_auth``: The authentication service from which to migrate user accounts. Supported options: ``email``, ``gitlab``, ``saml``.

    -  ``to_auth``: The authentication service to which to migrate user accounts. Supported options: ``ldap``.

    -  ``match_field``: The field that is guaranteed to be the same in both authentication services. For example, if the user emails are consistent set to email. Supported options: ``email``, ``username``.

  Format
    .. code-block:: none

      mattermost user migrate_auth {from_auth} ldap {match_field}

  Example
    .. code-block:: none

      bin/mattermost user migrate_auth email ldap email
  Options
    .. code-block:: none

      --force  Ignore duplicate entries on the AD/LDAP server.
      --dryRun Run a simulation of the migration process without changing the database.

**Migrate to SAML**

*Supported in Mattermost v4.8 and later*

  Parameters

    -  ``from_auth``: The authentication service from which to migrate user accounts. Supported options: ``email``, ``gitlab``. ``ldap``.

    -  ``to_auth``: The authentication service to which to migrate user accounts. Supported options: ``saml``.

    -  ``users_file``: The path of a JSON file with the usernames and emails of all users to migrate to SAML. The username and email must be the same as in your SAML service provider. Moreover, the email must match the email address of the Mattermost user account. An example of the users file is below:

    .. code-block:: json

        {
          "user1@email.com": "username.one",
          "user2@email.com": "username.two"
        }

  Users file generation
    Generating the ``users_file`` depends on how the system is configured and which SAML service provider is used. Below are two sample scripts for OneLogin and Okta service providers. For ADFS, you can use the AD/LDAP protocol to directly extract the users information and export it to a JSON file.

    After generating the ``users_file``, you can manually update the file to obtain a list of Mattermost user accounts you want to migrate to SAML. Note that users listed in ``users_file`` that do not yet exist in Mattermost are ignored during the migration process.

    OneLogin:

    .. code-block:: python

        from onelogin.api.client import OneLoginClient
        import json

        client_id = input("Client id: ")
        client_secret = input("Secret: ")
        region = input("Region (us, eu): ")

        client = OneLoginClient(client_id, client_secret, region)

        mapping = {}
        for user in client.get_users():
            mapping[user.email] = user.username

        with file("saml_users.json", "w") as fd:
            json.dump(mapping, fd)

    Okta:

    .. code-block:: python

        from okta import UsersClient
        import json

        base_url = input("Base url (example: https://example.okta.com): ")
        api_token = input("API Token: ")

        usersClient = UsersClient(base_url, api_token)

        users = usersClient.get_paged_users(limit=25)

        mapping = {}

        for user in users.result:
            mapping[user.profile.email] = user.profile.login

        while not users.is_last_page():
            users = usersClient.get_paged_users(url=users.next_url)
            for user in users.result:
                mapping[user.profile.email] = user.profile.login

        with file("saml_users.json", "w") as fd:
            json.dump(mapping, fd)

    ADFS:

    .. code-block:: python

        import ldap
        import json
        import getpass

        ldap_host = input('Ldap Host (example ldap://localhost:389): ')
        base_dn = input('Base DN (example dc=mm,dc=test,dc=com): ')
        bind_dn = input('Bind DN (example ORGANIZATION\username): ')
        password = getpass.getpass('Password: ')
        user_object_class = input('User object class (example organizationalPerson): ')
        username_field = input('Username field (example sAMAccountName): ')
        mail_field = input('Mail field (example mail): ')

        l = ldap.initialize(ldap_host)
        l.simple_bind_s(bind_dn, password)
        page_control = ldap.controls.libldap.SimplePagedResultsControl(True, size=1000, cookie='')
        r = l.search_ext(base_dn, ldap.SCOPE_SUBTREE, '(objectClass='+user_object_class+')', [username_field, mail_field],         serverctrls=[page_control])

        mapping = {}
        while True:
            rtype, rdata, rmsgid, serverctrls = l.result3(r)

            for dn, entry in rdata:
                if mail_field in entry and len(entry[mail_field]) >= 1 and username_field in entry and len(entry[username_field]) >= 1:
                    mapping[entry[mail_field][0].decode('utf-8')] = entry[username_field][0].decode('utf-8')

            controls = [control for control in serverctrls if control.controlType == ldap.controls.libldap.SimplePagedResultsControl.controlType]
            if not controls:
                print('The server ignores RFC 2696 control')
                break
            if not controls[0].cookie:
                break
            page_control.cookie = controls[0].cookie
            r = l.search_ext(base_dn, ldap.SCOPE_SUBTREE, '(objectClass='+user_object_class+')', [username_field, mail_field], serverctrls=[page_control])

        with open("saml_users.json", "w") as fd:
            json.dump(mapping, fd)

  Format
    .. code-block:: none

      mattermost user migrate_auth {from_auth} saml {users_file}

  Example
    .. code-block:: none

      bin/mattermost user migrate_auth email saml users.json

  Options
    .. code-block:: none

      --auto   Automatically migrate all users without a {users_file}. Assumes the usernames and emails are identical between Mattermost and SAML services.
      --dryRun Run a simulation of the migration process without changing the database. Useful to test if the migration results in any errors. You can use this option with or without a {users_file}.

mattermost user password
~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl user reset_password <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-user-reset-password>`__.


Description
    Set a user's password.

  Format
    .. code-block:: none

      mattermost user password {user} {password}

  Example
    .. code-block:: none

      bin/mattermost user password user@example.com Password1

mattermost user resetmfa
~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl user resetmfa <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-user-resetmfa>`__.


Description
    Turns off multi-factor authentication for a user. If MFA enforcement is enabled, the user will be forced to re-enable MFA with a new device as soon as they log in.

  Format
    .. code-block:: none

      mattermost user resetmfa {users}

  Example
    .. code-block:: none

      bin/mattermost user resetmfa user@example.com

mattermost user search
~~~~~~~~~~~~~~~~~~~~~~

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl user search <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-user-search>`__.


Description
    Search for users based on username, email, or user ID.

  Format
    .. code-block:: none

      mattermost user search {users}

  Example
    .. code-block:: none

      bin/mattermost user search user1@example.com user2@example.com

mattermost user verify
~~~~~~~~~~~~~~~~~~~~~~

  Description
    Verify the email address of a new user.

  Format
    .. code-block:: none

      mattermost user verify {users}

  Example
    .. code-block:: none

      bin/mattermost user verify user1

mattermost version
------------------

.. note::

   This command will be replaced in a future release with the mmctl command `mmctl system version <https://docs.mattermost.com/administration/mmctl-cli-tool.html#mmctl-system-version>`__.


Description
    Displays Mattermost version information.

  Format
    .. code-block:: none

      mattermost version

mattermost webhook
------------------

  Description
    Commands to manage webhooks.

  Child Commands
    -  `mattermost webhook create-incoming`_ - Create an incoming webhook within specific channel.
    -  `mattermost webhook create-outgoing`_ - Create an outgoing webhook within specific channel.
    -  `mattermost webhook delete`_ - Delete incoming and outgoing webhooks.
    -  `mattermost webhook list`_ - List all webhooks.
    -  `mattermost webhook modify-incoming`_ - Modify an existing incoming webhook by changing its title, description, channel, or icon URL.
    -  `mattermost webhook modify-outgoing`_ - Modify an existing outgoing webhook by changing its title, description, channel, icon, URL, content-type, and triggers.
    -  `mattermost webhook move-outgoing`_ - Move an existing outgoing webhook with an ID.
    -  `mattermost webhook show`_ - Show information about a webhook by providing the webhook ID.

mattermost webhook create-incoming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Create an incoming webhook within specific channel.

  Format
    .. code-block:: none

      mattermost webhook create-incoming

  Examples
    .. code-block:: none

       bin/mattermost webhook create-incoming --channel [channelID] --user [userID] --display-name [display-name] --description [webhookDescription] --lock-to-channel --icon [iconURL]

  Options
    .. code-block:: none

          --channel string           Channel ID
          --user string              User ID
          --display-name string      Incoming webhook display name
          --description string       Incoming webhook description
          --lock-to-channel boolean  (True/False) Lock incoming webhook to channel
          --icon [iconURL]           Icon URL

mattermost webhook create-outgoing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Create an outgoing webhook which allows external posting of messages from a specific channel.

  Format
    .. code-block:: none

      mattermost webhook create-outgoing

  Examples
    .. code-block:: none

       bin/mattermost webhook create-outgoing --team myteam --channel mychannel --user myusername --display-name mywebhook --description "My cool webhook" --trigger-when start --trigger-word "build" --icon http://localhost:8000/my-slash-handler-bot-icon.png --url http://localhost:8000/my-webhook-handler --content-type "application/json"

       bin/mattermost webhook create-outgoing --team myotherteam --channel mychannel --user myusername --display-name myotherwebhook --description "My cool webhook" --trigger-when exact --trigger-word "build" --trigger-word "test" --trigger-word "third-trigger" --icon http://localhost:8000/my-slash-handler-bot-icon.png --url http://localhost:8000/my-webhook-handler --url http://example.com --content-type "application/json"

  Options
    .. code-block:: none

          --team string [REQUIRED]                Team name or ID
          --channel string                        Channel name or ID
          --user string [REQUIRED]                User username, email, or ID
          --display-name string [REQUIRED]        Outgoing webhook display name
          --description string                    Outgoing webhook description
          --trigger-words stringArray [REQUIRED]  Words to trigger webhook
          --trigger-when string [REQUIRED]        When to trigger webhook (exact: for first word matches a trigger word exactly, start: for first word starts with a trigger word) (default "exact")
          --icon [iconURL]                        Icon URL
          --url stringArray [REQUIRED]            Callback URLs
          --content-type string                   Content-type
          --h, --help         Help for create-outgoing

mattermost webhook delete
~~~~~~~~~~~~~~~~~~~~~~~~~

   Description
    Delete incoming and outgoing webhooks. If deleting multiple webhooks, use a space-separated list.

   Format
     .. code-block:: none

       mattermost webhook delete [webhookID]

   Examples
     .. code-block:: none

        bin/mattermost webhook delete ggwpz8c1oj883euk98wfm9n1cr

mattermost webhook list
~~~~~~~~~~~~~~~~~~~~~~~

  Description
    List all webhooks.

  Format
    .. code-block:: none

      mattermost webhook list {team}

  Examples
    .. code-block:: none

       bin/mattermost webhook list team1
       bin/mattermost webhook list

  Options
    .. code-block:: none

          --team string  Specific team results to return.  If not specified, all teams will be included.

mattermost webhook modify-incoming
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Modify an existing incoming webhook by changing its title, description, channel or icon url.

  Format
    .. code-block:: none

      mattermost webhook modify-incoming {webhookId}

  Examples
    .. code-block:: none

       bin/mattermost webhook modify-incoming [webhookID] --channel [channelID] --display-name [displayName] --description [webhookDescription] --lock-to-channel --icon [iconURL]

  Options
    .. code-block:: none

          --channel string              Channel ID
          --display-name string         Incoming webhook display name
          --description string          Incoming webhook description
          --lock-to-channel boolean     (True/False) Lock incoming webhook to channel
          --icon [iconURL]              Icon URL

mattermost webhook modify-outgoing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Modify an existing outgoing webhook by changing its title, description, channel, trigger words, icon url, callback url, or content type.

  Format
    .. code-block:: none

      mattermost webhook modify-outgoing {webhookId}

  Examples
    .. code-block:: none

       bin/mattermost webhook modify-outgoing [webhookId] --channel [channelId] --display-name [displayName] --description "New webhook description" --icon http://localhost:8000/my-slash-handler-bot-icon.png --url http://localhost:8000/my-webhook-handler --content-type "application/json" --trigger-word test --trigger-when start`

  Options
    .. code-block:: none

          --channel string              Channel ID
          --display-name string         Incoming webhook display name
          --description string          Incoming webhook description
	  --trigger-word string array	Word(s) to trigger webhook
	  --trigger-when string		When to trigger webhook (exact: for first word matches a trigger word exactly, start: for first word starts with a trigger word)")
         --icon [iconURL]              Icon URL
	  --url [callbackURL]           Callback URL
	  --content-type string         Content type

mattermost webhook move-outgoing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Move an existing outgoing webhook to another team by specifying its id. If the outgoing webhook is triggered by a keyword then assiging a channel is optional.  If the outgoing webhook is associated to a specific channel prior to moving, a channel must be specified within the new team.

  Format
    .. code-block:: none

      mattermost webhook move-outgoing {webhookId}

  Examples
    .. code-block:: none

       bin/mattermost webhook move-outgoing newteam oldteam:[webhookId] --channel [channelId or channelName]

  Options
    .. code-block:: none

          --channel string              Channel ID or Channel Name


mattermost webhook show
~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Show information about a webhook by providing the webhook ID. Returns display name, channel ID and team ID for both incoming and outgoing webhooks.  Additionally returns callback URL, username, and icon URL for outgoing webhooks.

  Format
    .. code-block:: none

      mattermost webhook show {webhookId}

  Examples
    .. code-block:: none

       bin/mattermost webhook show [webhookId]

Mattermost 3.5 and earlier
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Typing ``./platform -help`` brings up documentation for the CLI tool. To return the help documentation in GitLab omnibus, type

    .. code-block:: none

      sudo -u mattermost /opt/gitlab/embedded/bin/mattermost --config=/var/opt/gitlab/mattermost/config.json -help

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
                                        https://mattermost.org/upgrading-to-mattermost-3-0/

          Example:
              platform -upgrade_db_30

      -version                          Display the current of the Mattermost platform

      -help                             Displays this help page


Troubleshooting
^^^^^^^^^^^^^^^^^

Executing a command hangs and doesn't complete
------------------------------------------------

If you have Bleve search indexing enabled, temporarily disable it in **System Console > Experimental > Bleve** and run the command again. You can also optionally use the new `mmctl Command Line Tool <https://docs.mattermost.com/administration/mmctl-cli-tool.html>`_.

Bleve does not support multiple processes opening and manipulating the same index. Therefore, if the Mattermost server is running, an attempt to run the CLI will lock when trying to open the indeces.

If you are not using the Bleve search indexing, feel free to post in our `Troubleshooting forum <https://mattermost.org/troubleshoot/>`__ to get help.
