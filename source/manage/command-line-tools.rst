Command line tools
==================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

In self-managed deployments, a ``mattermost`` command is available for configuring the system from the directory where the Mattermost server is installed. For an overview of the Mattermost command line interface (CLI), `read this article <https://medium.com/@santosjs/plugging-in-to-the-mattermost-cli-8cdcef2bd1f6>`__ from Santos.

.. important::

  From Mattermost v6.0, the majority of these CLI commands have been replaced with equivalents available using the `mmctl command line tool </manage/mmctl-command-line-tool.html>`__. However, `mattermost import </manage/command-line-tools.html#mattermost-import>`__ commands, `mattermost export </manage/command-line-tools.html#mattermost-export>`__ commands, and related subcommands, remain available and fully supported from Mattermost v6.0.

These ``mattermost`` commands include the following functionality:

**Compliance Export**

- Export data
- Schedule an export job

**Database**

- Initialize the database, execute migrations, and load custom defaults
- Migrate the database schema for unapplied migrations
- Reset the database to its initial state
- Return the most recently applied version number
- Roll back database migrations

**Server Operations**

- Start the Mattermost job server
- Run the Mattermost server
- Display Mattermost version information

Use the CLI
-----------

.. tab:: Via Mattermost 

  To run the CLI commands, you must be in the Mattermost root directory. On a default installation of Mattermost, the root directory is ``/opt/mattermost``. If you followed our standard `installation process <../guides/administrator.html#installing-mattermost>`__, you must run the commands as the user ``mattermost``. The name of the executable is ``mattermost``, and it can be found in the ``/opt/mattermost/bin`` directory.

  For example, to get the Mattermost version on a default installation of Mattermost:

  .. code-block:: bash

    cd /opt/mattermost/
    sudo -u mattermost bin/mattermost version

  .. note::

    - Ensure you run the Mattermost binary as the ``mattermost`` user. Running it as ``root`` user (for example) may cause complications with permissions as the binary initiates plugins and accesses various files when running CLI commands. Running the server as ``root`` may result in ownership of the plugins and files to be overwritten as well as other potential permissions errors.
    - When running CLI commands on a Mattermost installation that has the configuration stored in the database, you might need to pass the database connection string as: 

      .. code-block:: bash

        bin/mattermost --config="postgres://mmuser:mostest@localhost:5432/mattermost_test?sslmode=disable\u0026connect_timeout=10"

.. tab:: Via GitLab Omnibus

  On GitLab Omnibus, you must be in the following directory when you run CLI commands: ``/opt/gitlab/embedded/service/mattermost``. Also, you must run the commands as the user *mattermost* and specify the location of the configuration file. The executable is ``/opt/gitlab/embedded/bin/mattermost``.

  For example, to get the Mattermost version on GitLab Omnibus:

  .. code-block:: bash

    cd /opt/gitlab/embedded/service/mattermost
    sudo /opt/gitlab/embedded/bin/chpst -e /opt/gitlab/etc/mattermost/env -P -U mattermost:mattermost -u mattermost:mattermost /opt/gitlab/embedded/bin/mattermost version

  .. note::
  
    The example commands on this documentation page are for a default installation of Mattermost. You must modify the commands so that they work on GitLab Omnibus.

.. tab:: Via Docker Install

  On Docker install, the ``/mattermost/bin`` directory was added to ``PATH``, so you can use the CLI directly with the ``docker exec`` command. Note that the container name may be ``mattermostdocker_app_1`` if you installed Mattermost with ``docker-compose.yml``.

  For example, to get the Mattermost version on a Docker Install:

  .. code-block:: bash

    docker exec -it <your-mattermost-container-name> mattermost version

.. tab:: Via Docker Preview

  The Docker Install tab details and command references below also apply to the `Mattermost docker preview image <https://github.com/mattermost/mattermost-docker-preview>`__.

.. note::
  - The CLI is run in a single node which bypasses the mechanisms that a `High Availability environment </scale/high-availability-cluster.html>`__ uses to perform actions across all nodes in the cluster. As a result, when running `CLI commands </manage/command-line-tools.html>`__ in a High Availability environment, tasks that change configuration settings require a server restart.
  -  Parameters in CLI commands are order-specific.
  -  If special characters (``!``, ``|``, ``(``, ``)``, ``\``, ``'``, or ``"``) are used, the entire argument needs to be surrounded by single quotes, or the individual characters need to be escaped out.

mattermost cli commands
-----------------------

Description
  Commands for configuring and managing your Mattermost instance and users.

Options
  .. code-block:: none

    -c, --config {string}           Configuration file to use. (default "config.json")
    --disableconfigwatch {boolean}  When true, the config.json file will not be reloaded automatically when another process changes it (default "false")

Child Commands
  -  `mattermost db`_ - Database commands
  -  `mattermost export`_ - Compliance export commands 
  -  `mattermost help`_ - Generate full documentation for the CLI
  -  `mattermost import`_ - Legacy import command
  -  `mattermost jobserver`_ - Start the Mattermost job server
  -  `mattermost server`_ - Run the Mattermost server
  -  `mattermost version`_ - Display version information

mattermost db
--------------

Description
  Commands related to the database

Child Commands
  -  `mattermost db downgrade`_ - Roll back database migrations. Requires either an update plan to roll back to, or comma-separated version numbers to be rolled back.
  -  `mattermost db init`_ - Initialize the database, execute migrations, and load custom defaults
  -  `mattermost db migrate`_ - Migrate the database schema for unapplied migrations
  -  `mattermost db reset`_ - Reset the database to its initial state
  -  `mattermost db version`_ - Return the most recently applied version number

Options
  .. code-block:: none

    -h, --help   help for db
    -c, --config string   Configuration file to use

mattermost db downgrade
~~~~~~~~~~~~~~~~~~~~~~~

Description
  Rolls back database migrations. Requires either an update plan to roll back to, or comma-separated version numbers to be rolled back.

Format
  .. code-block:: none

    mattermost db downgrade

Example
  .. code-block:: none

    mattermost db downgrade 99,100,101

Options
  .. code-block:: none

    --<plan-file> string      Runs the rollback migrations defined in the plan file.

mattermost db init
~~~~~~~~~~~~~~~~~~

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

mattermost db migrate
~~~~~~~~~~~~~~~~~~~~~

Description
  Migrates the database schema if there are any unapplied migrations.

Child Commands
  -  `mattermost db downgrade`_ - Roll back database migrations.

Format
  .. code-block:: none

    mattermost db migrate

Example
  .. code-block:: none

    mattermost db migrate

Options
  .. code-block:: none

    --auto-recover bool     If the migration plan receives an error during migrations, this command will try to rollback migrations already applied within the plan. Not recommended without reviewing migration plan by combining --save-plan and --dry-run options.
    --save-plan bool        Saves the plan for the migration into the file store so that it can be used for reviewing the plan or for downgrading.
    --dry-run bool          Does not apply the migrations, but it validates how the migration would run based on the given conditions.

mattermost db reset
~~~~~~~~~~~~~~~~~~~~

Description
  Resets the database to its initial state. Doesn't start the application server. Only starts the store layer and truncates the tables, excluding the ``migrations`` table.

Format
  .. code-block:: none

    mattermost db reset

Example
  .. code-block:: none

    bin/mattermost db reset

mattermost db version
~~~~~~~~~~~~~~~~~~~~~~

Description
  Returns the most recently applied version number.

Format
  .. code-block:: none

    mattermost db version

Example
  .. code-block:: none

    bin/mattermost export actiance --exportFrom=1513102632

Options
  .. code-block:: none

    --exportFrom string     Unix timestamp (milliseconds since epoch, UTC) to export data from.
    --batchSize int         The number of posts to export. The default of -1 means no limit.

----

mattermost export
-----------------

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

Description
  Commands for exporting data for compliance and for merging multiple Mattermost instances.

Child Commands
  -  `mattermost export actiance`_ - Export data from Mattermost in Actiance XML format. Requires a Mattermost Enterprise subscription plan.
  -  `mattermost export bulk`_ - Export data to a file compatible with the Mattermost `Bulk Import format </onboard/bulk-loading-data.html>`__. Deprecated in favor of `mmctl export commands </manage/mmctl-command-line-tool.html#mmctl-export>`__.
  -  `mattermost export csv`_ - Export data from Mattermost in CSV format. Requires a Mattermost Enterprise subscription plan.
  -  `mattermost export global-relay-zip`_ - Export data from Mattermost into a ZIP file containing emails to send to Global Relay for debug and testing purposes only. Requires a Mattermost Enterprise subscription plan.
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
    --batchSize int         The number of posts to export. The default of -1 means no limit.

mattermost export bulk
~~~~~~~~~~~~~~~~~~~~~~

From Mattermost v6.0, this command has been deprecated in favor of `mmctl export commands </manage/mmctl-command-line-tool.html#mmctl-export>`__ as the supported way to export data out of Mattermost.

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
    --batchSize int         The number of posts to export. The default of -1 means no limit.

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
    --batchSize int         The number of posts to export. The default of -1 means no limit.

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

----

mattermost help
---------------

Description
  Generate full documentation in Markdown format for the Mattermost command line tools.

Format
  .. code-block:: none

    mattermost help {outputdir}

.. _command-line-tools-mattermost-jobserver:

----

mattermost import
-----------------

Description
  Import data into Mattermost.

Child Command
  -  `mattermost import bulk`_ - Import a Mattermost Bulk Import File. Deprecated in favor of `mmctl import commands </manage/mmctl-command-line-tool.html#mmctl-import>`__.
  -  `mattermost import slack`_ - Import a team from Slack.

mattermost import bulk
~~~~~~~~~~~~~~~~~~~~~~

From Mattermost v6.0, this command has been deprecated in favor of `mmctl import commands </manage/mmctl-command-line-tool.html#mmctl-import>`__ as the supported way to import data into Mattermost.

mattermost import slack
~~~~~~~~~~~~~~~~~~~~~~~

See the `mmctl import commands </manage/mmctl-command-line-tool.html#mmctl-import>`__ documentation as the preferred way to import Slack data into Mattermost.

Description
  Import a team from a Slack export zip file.

Format
    . code-block:: none

    mattermost import slack {team} {file}

Example
  .. code-block:: none

    bin/mattermost import slack myteam slack_export.zip

----

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

----

mattermost server
-----------------

Description
  Runs the Mattermost server.

Format
  .. code-block:: none

    mattermost server

----

mattermost version
------------------

.. note::

  From Mattermost v6.5, this CLI command no longer interacts with the database. The `mattermost db migrate </manage/command-line-tools.html#mattermost-db-migrate>`__ CLI command has been introduced to trigger schema migrations.

Desription
    Displays Mattermost version information.

Format
  .. code-block:: none

    mattermost version

----

Troubleshooting
----------------

Executing a command hangs and doesn't complete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have Bleve search indexing enabled, temporarily disable it in **System Console > Experimental > Bleve** and run the command again. You can also optionally use the new `mmctl Command Line Tool </manage/mmctl-command-line-tool.html>`_.

Bleve does not support multiple processes opening and manipulating the same index. Therefore, if the Mattermost server is running, an attempt to run the CLI will lock when trying to open the indeces.

If you aren't using the Bleve search indexing, feel free to post in our `Troubleshooting forum <https://forum.mattermost.com/c/trouble-shoot/16>`__ to get help.
