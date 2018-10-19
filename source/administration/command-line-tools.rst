Command Line Tools
==================

From the directory where the Mattermost server is installed, a ``mattermost`` command is available for configuring the system. For an overview of the Mattermost command line interface (CLI), `read this article <https://medium.com/@santosjs/plugging-in-to-the-mattermost-cli-8cdcef2bd1f6>`_ from Santos.

These ``mattermost`` commands include:

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
-  Creating sample data

.. contents::
    :backlinks: top
    :local:

Using the CLI
^^^^^^^^^^^^^

To run the CLI commands, you must be in the directory that contains the Mattermost executable. On a default install of Mattermost, the directory is ``/opt/mattermost/bin``. The name of the executable is ``mattermost``.

**For example, to get the Mattermost version on a default installation of Mattermost:**

  .. code-block:: bash

    cd /opt/mattermost/bin
    sudo ./mattermost version

Using the CLI on GitLab Omnibus
-------------------------------

On GitLab Omnibus, you must be in the following directory when you run CLI commands: ``/opt/gitlab/embedded/service/mattermost``. Also, you must run the commands as the user *mattermost* and specify the location of the configuration file. The executable is ``/opt/gitlab/embedded/bin/mattermost``.

**For example, to get the Mattermost version on GitLab Omnibus:**

  .. code-block:: bash

    cd /opt/gitlab/embedded/service/mattermost
    sudo -u mattermost /opt/gitlab/embedded/bin/mattermost --config=/var/opt/gitlab/mattermost/config.json version

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

The preceding documentation and command reference below also applies to the `Mattermost docker preview image <https://github.com/mattermost/mattermost-docker-preview>`_.

Mattermost 3.6 and later
^^^^^^^^^^^^^^^^^^^^^^^^

The new CLI tool is supported in Mattermost 3.6 and later. To see available commands in the old CLI tool, see `Mattermost 3.5 and earlier`_.

.. note::
  For Mattermost 4.10 and earlier, the commands used the ``platform`` executable instead of ``mattermost``. For example, to check the Mattermost version, one would run ``sudo ./platform version`` instead of ``sudo ./mattermost version``.

Notes:

-  Parameters in CLI commands are order-specific.
-  If special characters (``!``, ``|``, ``(``, ``)``, ``\``, ``'``, and ``"``) are used, the entire argument needs to be surrounded by single quotes (e.g. ``-password 'mypassword!'``, or the individual characters need to be escaped out (e.g. ``-password mypassword\!``).
-  Team name and channel name refer to the handles, not the display names. So in the url ``https://pre-release.mattermost.com/core/channels/town-square`` team name would be ``core`` and channel name would be ``town-square``

.. tip::
   If you automate user creation through the CLI tool with SMTP enabled, emails will be sent to all new users created. If you run such a load script, it is best to disable SMTP or to use test accounts so that new account creation emails aren't unintentionally sent to people at your organization who aren't expecting them.

mattermost
--------

  Description
    Commands for configuring and managing your Mattermost instance and users.

  Options
    .. code-block:: none

      -c, --config {string}   Configuration file to use. (default "config.json")

  Child Commands
    -  `mattermost channel`_ - Management of channels
    -  `mattermost command`_ - Management of slash commands
    -  `mattermost config`_ - Work with the configuration file
    -  `mattermost export`_ - Compliance export commands
    -  `mattermost help`_ - Generate full documentation for the CLI
    -  `mattermost import`_ - Import data
    -  `mattermost jobserver`_ - Start the Mattermost job server
    -  `mattermost ldap`_ - AD/LDAP related utilities
    -  `mattermost license`_ - Licensing commands
    -  `mattermost permissions`_ - Management of the permissions system
    -  `mattermost plugin`_ - Management of plugins
    -  `mattermost reset`_ - Reset the database to initial state
    -  `mattermost roles`_ - Management of user roles
    -  `mattermost sampledata`_ - Sample data generation
    -  `mattermost server`_ - Run the Mattermost server
    -  `mattermost team`_ - Management of teams
    -  `mattermost user`_ - Management of users
    -  `mattermost version`_ - Display version information

mattermost channel
-----------------

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

.. _channel-value-note:

.. note::
    **{channel} value**

    For the *add*, *archive*, *delete*, *remove* and *restore* commands, you can specfiy the *{channels}* value by {team}:{channel} using the team and channel URLs, or by using channel IDs. For example, in the following URL the *{channels}* value is *myteam:mychannel*:

    ``https://example.com/myteam/channels/mychannel``
    
    Also, the team and channel names in the URL should be written in lowercase.

mattermost channel add
~~~~~~~~~~~~~~~~~~~~

  Description
    Add users to a channel. If adding multiple users, use a space-separated list.

  Format
    .. code-block:: none

      mattermost channel add {channel} {users}

  Examples
    .. code-block:: none

      sudo ./mattermost channel add 8soyabwthjnf9qibfztje5a36h user@example.com username
      sudo ./mattermost channel add myteam:mychannel user@example.com username

mattermost channel archive
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Archive a channel. Archived channels are not accessible to users, but remain in the database. To restore a channel from the archive, see `mattermost channel restore`_. Channels can be specified by {team}:{channel} using the team and channel names, or by using channel IDs.

  Format
    .. code-block:: none

      mattermost channel archive {channels}

  Examples
    .. code-block:: none

      sudo ./mattermost channel archive 8soyabwthjnf9qibfztje5a36h
      sudo ./mattermost channel archive myteam:mychannel

mattermost channel create
~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Create a channel.

  Format
    .. code-block:: none

     mattermost channel create

  Examples
    .. code-block:: none

      sudo ./mattermost channel create --team myteam --name mynewchannel --display_name "My New Channel"
      sudo ./mattermost channel create --team myteam --name mynewprivatechannel --display_name "My New Private Channel" --private

  Options
    .. code-block:: none

          --display_name string   Channel Display Name
          --header string         Channel header
          --name string           Channel Name
          --private               Create a private channel.
          --purpose string        Channel purpose
          --team string           Team name or ID

mattermost channel delete
~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Permanently delete a channel along with all related information, including posts from the database. Channels can be specified by {team}:{channel} using the team and channel names, or by using channel IDs.

  Format
    .. code-block:: none

      mattermost channel delete {channels}

  Examples
    .. code-block:: none

      sudo ./mattermost channel delete 8soyabwthjnf9qibfztje5a36h
      sudo ./mattermost channel delete myteam:mychannel

mattermost channel list
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    List all channels on a specified team. Archived channels are appended with ``(archived)``.

  Format
    .. code-block:: none

      mattermost channel list {teams}

  Example
    .. code-block:: none

      sudo ./mattermost channel list myteam

mattermost channel modify
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Modify a channel's public/private type.

  Format
    .. code-block:: none

      mattermost channel modify

  Example
    .. code-block:: none

      sudo ./mattermost channel modify myteam:mychannel --username myusername --private

  Options
    .. code-block:: none

          --username [REQUIRED] Username of the user who is changing the channel privacy.
          --public   Change a private channel to be public.
          --private  Change a public channel to be private.

mattermost channel move
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Move channels to another team. The command validates that all users in the channel belong to the target team. Incoming/Outgoing webhooks are moved along with the channel. Channels can be specified by ``[team]:[channel]`` or by using channel IDs.

  Format
    .. code-block:: none

      mattermost channel move

  Example
    .. code-block:: none

      sudo ./mattermost channel move newteam 8soyabwthjnf9qibfztje5a36h --username myusername
      sudo ./mattermost channel move newteam myteam:mychannel --username myusername

  Options
    .. code-block:: none

          --username [REQUIRED] Username of the user who is moving the team.

mattermost channel remove
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Remove users from a channel.

  Format
    .. code-block:: none

      mattermost channel remove {channel} {users}

  Examples
    .. code-block:: none

      sudo ./mattermost channel remove 8soyabwthjnf9qibfztje5a36h user@example.com username
      sudo ./mattermost channel remove myteam:mychannel user@example.com username
      sudo ./mattermost channel remove myteam:mychannel --all-users
      
  Options
    .. code-block:: none

          --all-users string     Remove all users from the channel.
      
mattermost channel rename
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Rename a channel. Channels can be specified by *{team}:{channel}* using the team and channel names, or by using channel IDs.

  Format
    .. code-block:: none

      mattermost channel rename {channel} newchannelname --display_name "New Display Name"

  Examples
    .. code-block:: none

      sudo ./mattermost channel rename 8soyabwthjnf9qibfztje5a36h newchannelname --display_name "New Display Name"
      sudo ./mattermost channel rename myteam:mychannel newchannelname --display_name "New Display Name"
      
  Options
    .. code-block:: none

      --display_name string   Channel Display Name

mattermost channel restore
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Restore a channel from the archive. Channels can be specified by {team}:{channel} using the team and channel names, or by using channel IDs.

  Format
    .. code-block:: none

      mattermost channel restore {channels}

  Examples
    .. code-block:: none

      sudo ./mattermost channel restore 8soyabwthjnf9qibfztje5a36h
      sudo ./mattermost channel restore myteam:mychannel

mattermost command
-----------------

  Description
    Commands for slash command management.

  Child Commands
    -  `mattermost command move`_ - Move a slash command to a different team

mattermost command move
~~~~~~~~~~~~~~~~~~~~~~

  Description
    Move a slash command to a different team. Commands can be specified by {team}:{command-trigger-word}, or by using command IDs.

  Format
    .. code-block:: none

      mattermost command move

  Examples
    .. code-block:: none

      sudo ./mattermost command move newteam oldteam:command-trigger-word
      sudo ./mattermost channel move newteam o8soyabwthjnf9qibfztje5a36h

mattermost config
---------------

  Description
    Commands for managing the configuration file.

  Child Command
    - `mattermost config validate`_ - Validate the configuration file.

mattermost config validate
~~~~~~~~~~~~~~~~~~~~~~~~

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

        sudo ./mattermost config validate

mattermost export
-----------------

  Description
   Commands for exporting data for compliance and for merging multiple Mattermost instances.

  Child Commands
    -  `mattermost export actiance`_ - Export data from Mattermost in Actiance XML format.  Requires an E20 license
    -  `mattermost export bulk`_ - Export data to a file compatible with the Mattermost `Bulk Import format <https://docs.mattermost.com/deployment/bulk-loading.html>`_
    -  `mattermost export csv`_ - Export data from Mattermost in CSV format. Requires an E20 license
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

      sudo ./mattermost export actiance --exportFrom=1513102632

  Options
    .. code-block:: none

          --exportFrom string     Unix timestamp (seconds since epoch, UTC) to export data from.

mattermost export bulk
~~~~~~~~~~~~~~~~~~~~~

  Description
    Export data to a file compatible with the Mattermost `Bulk Import format <https://docs.mattermost.com/deployment/bulk-loading.html>`_.

  Format
    .. code-block:: none

      mattermost export bulk 

  Example
    .. code-block:: none

      sudo ./mattermost export bulk --all-teams file.json

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

      sudo ./mattermost export csv --exportFrom=1513102632

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

      sudo ./mattermost export schedule --format=actiance --exportFrom=1513102632

  Options
    .. code-block:: none

          --format string         Output file format. Currently, only ``actiance`` is supported.
          --exportFrom string     Unix timestamp (seconds since epoch, UTC) to export data from.
          --timeoutSeconds string Set how long the export should run for before timing out.

mattermost help
---------------

  Description
    Generate full documentation in Markdown format for the Mattermost command line tools.

  Format
    .. code-block:: none

      mattermost help {outputdir}

mattermost import
----------------

  Description
    Import data into Mattermost.

  Child Command
    -  `mattermost import slack`_ - Import a team from Slack.

mattermost import slack
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Import a team from a Slack export zip file.

  Format
    .. code-block:: none

      mattermost import slack {team} {file}

  Example
    .. code-block:: none

      sudo ./mattermost import slack myteam slack_export.zip

mattermost jobserver
--------------------

  Description
    Start the Mattermost job server.
    
  Format
    .. code-block:: none

      mattermost jobserver
      
  Example
    .. code-block:: none

      sudo ./mattermost jobserver

mattermost ldap
----------------

  Description
    Commands to configure and synchronize AD/LDAP.

  Child Command
    -  `mattermost ldap idmigrate`_ - Migrate the LDAP Id Attribute to a new value
    -  `mattermost ldap sync`_ - Synchronize now

mattermost ldap idmigrate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

      sudo ./mattermost ldap idmigrate objectGUID

mattermost ldap sync
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Synchronize all AD/LDAP users now.

  Format
    .. code-block:: none

      mattermost ldap sync

  Example
    .. code-block:: none

      sudo ./mattermost ldap sync

mattermost license
--------------------

  Description
    Commands to manage licensing.

  Child Command
    -  `mattermost license upload`_ - Upload a license.

mattermost license upload
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Upload a license. This command replaces the current license if one is already uploaded.

  Format
    .. code-block:: none

      mattermost license upload {license}

  Example
    .. code-block:: none

      sudo ./mattermost license upload /path/to/license/mylicensefile.mattermost-license

mattermost permissions
--------------------

  Description
    Commands to manage advanced permissions.

  Child Commands
    -  `mattermost permissions export`_ - Export Schemes and Roles.
    -  `mattermost permissions import`_ - Import Schemes and Roles from a permissions export.
    -  `mattermost permissions reset`_ - Reset the permissions system to its default state on new installs.
    
mattermost permissions export
~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

      sudo ./mattermost permissions export > my-permissions-export.jsonl

mattermost permissions import
~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Creates Roles and Schemes on a Mattermost instance from a jsonl input file in the format outputted by
    `mattermost permissions export`.

  Format
    .. code-block:: none

      mattermost permissions import {file}

  Example
    .. code-block:: none

      sudo ./mattermost permissions import my-permissions-export.jsonl

mattermost permissions reset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Reset permissions for all users, including Admins, to their default state on new installs. Note: **this will delete 
    all custom schemes**.

  Format
    .. code-block:: none

      mattermost permissions reset

  Example
    .. code-block:: none

      sudo ./mattermost permissions reset

  Options
    .. code-block:: none

          --confirm   Confirm you really want to reset the permissions system and a DB backup has been performed.

mattermost plugin
--------------------

  Description
    Commands to manage plugins.

  Child Commands
    -  `mattermost plugin add`_ - Add plugins to your Mattermost server.
    -  `mattermost plugin delete`_ - Delete previously uploaded plugins.
    -  `mattermost plugin disable`_ - Enable plugins for use.
    -  `mattermost plugin enable`_ - Disable plugins.
    -  `mattermost plugin list`_ - List plugins installed on your Mattermost server.
    
mattermost plugin add
~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Add plugins to your Mattermost server. If adding multiple plugins, use a space-separated list.

  Format
    .. code-block:: none

      mattermost plugins add {plugin tar file}

  Example
    .. code-block:: none

      sudo ./mattermost plugin add hovercardexample.tar.gz pluginexample.tar.gz

mattermost plugin delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Delete previously uploaded plugins from your Mattermost server. If deleting multiple plugins, use a space-separated list.

  Format
    .. code-block:: none

      mattermost plugins delete {plugin_id}

  Example
    .. code-block:: none

      sudo ./mattermost plugin delete hovercardexample.tar.gz pluginexample.tar.gz

mattermost plugin disable
~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Disable plugins. Disabled plugins are immediately removed from the user interface and logged out of all sessions. If disabling multiple plugins, use a space-separated list.

  Format
    .. code-block:: none

      mattermost plugins disable {plugin_id}

  Example
    .. code-block:: none

      sudo ./mattermost plugin disable hovercardexample.tar.gz pluginexample.tar.gz
      
mattermost plugin enable
~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Enable plugins for use on your Mattermost server. If enabling multiple plugins, use a space-separated list.

  Format
    .. code-block:: none

      mattermost plugins enable {plugin_id}

  Example
    .. code-block:: none

      sudo ./mattermost plugin enable hovercardexample.tar.gz pluginexample.tar.gz

mattermost plugin list
~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    List all active and inactive plugins installed on your Mattermost server.

  Format
    .. code-block:: none

      mattermost plugins list

  Example
    .. code-block:: none

      sudo ./mattermost plugin list

mattermost reset
---------------

  Description
    Completely erase the database causing the loss of all data. This resets Mattermost to its initial state.

  Format
    .. code-block:: none

      mattermost reset

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete everything and a DB backup has been performed.

mattermost roles
---------------

  Description
    Commands to manage user roles.

  Child Commands
    -  `mattermost roles member`_ - Remove System Admin privileges from a user
    -  `mattermost roles system_admin`_ - Make a user into a System Admin

mattermost roles member
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Remove system admin privileges from a user.

  Format
    .. code-block:: none

      mattermost roles member {users}

  Example
    .. code-block:: none

      sudo ./mattermost roles member user1

mattermost roles system\_admin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Promote a user to a System Admin.

  Format
    .. code-block:: none

      mattermost roles system_admin {users}

  Example
    .. code-block:: none

      sudo ./mattermost roles system_admin user1

mattermost sampledata
-------------------

  Description
    .. versionadded:: 4.7
      Generate sample data and populate the Mattermost database.

  Format
    .. code-block:: none

      mattermost sampledata

  Example
    .. code-block:: none

      sudo ./mattermost sampledata --seed 10 --teams 4 --users 30

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
----------------

  Description
    Runs the Mattermost server.

  Format
    .. code-block:: none

      mattermost server

mattermost team
----------------

  Description
    Commands to manage teams.

  Child Commands
    -  `mattermost team add`_ - Add users to a team
    -  `mattermost team create`_ - Create a team
    -  `mattermost team delete`_ - Delete a team
    -  `mattermost team list`_ - List all teams
    -  `mattermost team remove`_ - Remove users from a team

.. _team-value-note:

.. note::
    **{team-name} value**

    For the *add*, *delete*, and *remove* commands, you can determine the *{team-name}* value from the URLs that you use to access your instance of Mattermost. For example, in the following URL the *{team-name}* value is *myteam*:

    ``https://example.com/myteam/channels/mychannel``
    
    Also, the team and channel names in the URL should be written in lowercase.

mattermost team add
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Add users to a team. Before running this command, see the :ref:`note about {team-name} <team-value-note>`.

  Format
    .. code-block:: none

      mattermost team add {team-name} {users}

  Example
    .. code-block:: none

      sudo ./mattermost team add myteam user@example.com username

mattermost team create
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Create a team.

  Format
    .. code-block:: none

      mattermost team create

  Examples
    .. code-block:: none

      sudo ./mattermost team create --name mynewteam --display_name "My New Team"
      sudo ./mattermost teams create --name private --display_name "My New Private Team" --private

  Options
    .. code-block:: none

          --display_name string   Team Display Name
          --email string          Administrator Email (anyone with this email is automatically a team admin)
          --name string           Team Name
          --private               Create a private team.

mattermost team delete
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Permanently delete a team along with all related information, including posts from the database. Before running this command, see the :ref:`note about {team-name} <team-value-note>`.

  Format
    .. code-block:: none

      mattermost team delete {team-name}

  Example
    .. code-block:: none

      sudo ./mattermost team delete myteam

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete the team and a DB backup has been performed.

mattermost team list
~~~~~~~~~~~~~~~~~~~~~~~~

*Supported in Mattermost v4.10 and later*

  Description
    List all teams on the server.

  Format
    .. code-block:: none

      mattermost team list

  Example
    .. code-block:: none

      sudo ./mattermost team list

mattermost team remove
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Remove users from a team. Before running this command, see the :ref:`note about {team-name} <team-value-note>`.

  Format
    .. code-block:: none

      mattermost team remove {team-name} {users}

  Example
    .. code-block:: none

      sudo ./mattermost team remove myteam user@example.com username

mattermost user
---------------

  Description
    Commands to manage users.

  Child Commands

mattermost user activate

    -  `mattermost user activate`_ - Activate a user
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

  Description
    Activate users that have been deactivated. If activating multiple users, use a space-separated list.

  Format
    .. code-block:: none

      mattermost user activate {emails, usernames, userIds}

  Examples
    .. code-block:: none

      sudo ./mattermost user activate user@example.com
      sudo ./mattermost user activate username1 username2

mattermost user create
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Create a user.

  Format
    .. code-block:: none

      mattermost user create

  Examples
    .. code-block:: none

      sudo ./mattermost user create --email user@example.com --username userexample --password Password1
      sudo ./mattermost user create --firstname Joe --system_admin --email joe@example.com --username joe --password Password1

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
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Deactivate a user. Deactivated users are immediately logged out of all sessions and are unable to log back in.

  Format
    .. code-block:: none

      mattermost user deactivate {emails, usernames, userIds}

  Examples
    .. code-block:: none

      sudo ./mattermost user deactivate user@example.com
      sudo ./mattermost user deactivate username

mattermost user delete
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Permanently delete a user and all related information, including posts from the database.
    
    Does not delete content from the file storage. You can manually delete all file uploads for a given user as uploads contain the ``CreatorId`` field. User avatars are stored in ``data/users/<userid>/profile.png``.

  Format
    .. code-block:: none

      mattermost user delete {users}

  Example
    .. code-block:: none

      sudo ./mattermost user delete user@example.com

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete the user and a DB backup has been performed.

mattermost user deleteall
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Permanently delete all users and all related information, including posts.
    
    Does not delete content from the file storage. You can manually delete all file uploads and avatars. All uploads contain the ``CreatorId`` field and user avatars are stored in ``data/users/<userid>/profile.png``.

  Format
    .. code-block:: none

      mattermost user deleteall

  Example
    .. code-block:: none

      sudo ./mattermost user deleteall

  Options
    .. code-block:: none

          --confirm   Confirm you really want to delete the user and a DB backup has been performed.
          
mattermost user email	
~~~~~~~~~~~~~~~~~~~~~~~~	
	
  Description	
    Set a user's email.	
	
  Format	
    .. code-block:: none	
	
       mattermost user email {user} {new email}	
	
  Example	
    .. code-block:: none	
	
      sudo ./mattermost user email user@example.com newuser@example.com

mattermost user invite
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Send a user an email invite to a team. You can invite a user to multiple teams by listing the team names or team IDs.

  Format
    .. code-block:: none

      mattermost user invite {email} {teams}

  Examples
    .. code-block:: none

      sudo ./mattermost user invite user@example.com myteam
      sudo ./mattermost user invite user@example.com myteam1 myteam2

mattermost user migrate_auth
~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Migrates all existing Mattermost user accounts from one authentication provider to another. For example, you can upgrade your authentication provider from email to AD/LDAP, or from AD/LDAP to SAML. Output will display any accounts that are not migrated successfully.

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

      sudo ./mattermost user migrate_auth email ldap email
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
          "user1@email.com": "user.one",
          "user2@email.com": "user.two"
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

  Format
    .. code-block:: none

      mattermost user migrate_auth {from_auth} saml {users_file}

  Example
    .. code-block:: none

      sudo ./mattermost user migrate_auth email saml users.json

  Options
    .. code-block:: none

      --auto   Automatically migrate all users without a {users_file}. Assumes the usernames and emails are identical between Mattermost and SAML services.
      --dryRun Run a simulation of the migration process without changing the database. Useful to test if the migration results in any errors. You can use this option with or without a {users_file}.

mattermost user password
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Set a user's password.

  Format
    .. code-block:: none

      mattermost user password {user} {password}

  Example
    .. code-block:: none

      sudo ./mattermost user password user@example.com Password1

mattermost user resetmfa
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Turns off multi-factor authentication for a user. If MFA enforcement is enabled, the user will be forced to re-enable MFA with a new device as soon as they log in.

  Format
    .. code-block:: none

      mattermost user resetmfa {users}

  Example
    .. code-block:: none

      sudo ./mattermost user resetmfa user@example.com

mattermost user search
~~~~~~~~~~~~~~~~~~~~

  Description
    Search for users based on username, email, or user ID.

  Format
    .. code-block:: none

      mattermost user search {users}

  Example
    .. code-block:: none

      sudo ./mattermost user search user1@example.com user2@example.com

mattermost user verify
~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Verify the email address of a new user.

  Format
    .. code-block:: none

      mattermost user verify {users}

  Example
    .. code-block:: none

      sudo ./mattermost user verify user1

mattermost version
------------------

  Description
    Displays Mattermost version information.

  Format
    .. code-block:: none

      mattermost version

Mattermost 3.5 and earlier
^^^^^^^^^^^^^^^^^^^^^^^^^^

Typing ``sudo ./platform -help`` brings up documentation for the CLI tool. To return the help documentation in GitLab omnibus, type

    .. code-block:: none

      sudo -u mattermost /opt/gitlab/embedded/bin/mattermost --config=/var/opt/gitlab/mattermost/config.json -help

Notes:

- Parameters in CLI commands are order-specific.
- If special characters (``!``, ``|``, ``(``, ``)``, ``\``, `````, and ``"``) are used, the entire argument needs to be surrounded by single quotes (e.g. ``-password 'mypassword!'``, or the individual characters need to be escaped out (e.g. ``-password mypassword\!``).
- Team name and channel name refer to the handles, not the display names. So in the url ``https://pre-release.mattermost.com/core/channels/town-square`` team name would be ``core`` and channel name would be ``town-square``

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
