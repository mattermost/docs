Command line tools
==================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

In self-managed deployments, a ``mattermost`` command is available for configuring the system from the directory where the Mattermost server is installed. For an overview of the Mattermost command line interface (CLI), `read this article <https://medium.com/@santosjs/plugging-in-to-the-mattermost-cli-8cdcef2bd1f6>`_ from Santos.

.. important::

  From Mattermost v6.0, the majority of these CLI commands have been replaced with equivalents available using the :doc:`mmctl command line tool </administration-guide/manage/mmctl-command-line-tool>`. However, :ref:`mattermost import <administration-guide/manage/command-line-tools:mattermost import>` commands, :ref:`mattermost export <administration-guide/manage/command-line-tools:mattermost export>` commands, and related subcommands, remain available and fully supported from Mattermost v6.0.

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

  To run the CLI commands, you must be in the Mattermost root directory. On a default installation of Mattermost, the root directory is ``/opt/mattermost``. If you followed our standard :doc:`installation process </deployment-guide/deployment-guide-index>`, you must run the commands as the user ``mattermost``. The name of the executable is ``mattermost``, and it can be found in the ``/opt/mattermost/bin`` directory.

  For example, to get the Mattermost version on a default installation of Mattermost:

  .. code-block:: sh

    cd /opt/mattermost/
    sudo -u mattermost bin/mattermost version

  .. note::

    - Ensure you run the Mattermost binary as the ``mattermost`` user. Running it as ``root`` user (for example) may cause complications with permissions as the binary initiates plugins and accesses various files when running CLI commands. Running the server as ``root`` may result in ownership of the plugins and files to be overwritten as well as other potential permissions errors.
    - When running CLI commands on a Mattermost installation that has the configuration stored in the database, you might need to pass the database connection string as: 

      .. code-block:: sh

        bin/mattermost --config="postgres://mmuser:mostest@localhost:5432/mattermost_test?sslmode=disable\u0026connect_timeout=10"

.. tab:: Via GitLab Omnibus

  On GitLab Omnibus, you must be in the following directory when you run CLI commands: ``/opt/gitlab/embedded/service/mattermost``. Also, you must run the commands as the user *mattermost* and specify the location of the configuration file. The executable is ``/opt/gitlab/embedded/bin/mattermost``.

  For example, to get the Mattermost version on GitLab Omnibus:

  .. code-block:: sh

    cd /opt/gitlab/embedded/service/mattermost
    sudo /opt/gitlab/embedded/bin/chpst -e /opt/gitlab/etc/mattermost/env -P -U mattermost:mattermost -u mattermost:mattermost /opt/gitlab/embedded/bin/mattermost version

  .. note::
  
    The example commands on this documentation page are for a default installation of Mattermost. You must modify the commands so that they work on GitLab Omnibus.

.. tab:: Via Docker Install

  On Docker install, the ``/mattermost/bin`` directory was added to ``PATH``, so you can use the CLI directly with the ``docker exec`` command. Note that the container name may be ``mattermostdocker_app_1`` if you installed Mattermost with ``docker-compose.yml``.

  For example, to get the Mattermost version on a Docker Install:

  .. code-block:: sh

    docker exec -it <your-mattermost-container-name> mattermost version

.. tab:: Via Docker Preview

  The Docker Install tab details and command references below also apply to the `Mattermost docker preview image <https://github.com/mattermost/mattermost-docker-preview>`_.

.. note::
  - The CLI is run in a single node which bypasses the mechanisms that a :doc:`High Availability environment </administration-guide/scale/high-availability-cluster-based-deployment>` uses to perform actions across all nodes in the cluster. As a result, when running :doc:`CLI commands </administration-guide/manage/command-line-tools>` in a High Availability environment, tasks that change configuration settings require a server restart.
  -  Parameters in CLI commands are order-specific.
  -  If special characters (``!``, ``|``, ``(``, ``)``, ``\``, ``'``, or ``"``) are used, the entire argument needs to be surrounded by single quotes, or the individual characters need to be escaped out.

mattermost CLI commands
-----------------------

Description
  Commands for configuring and managing your Mattermost instance and users.

Options
  .. code-block:: text

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
  .. code-block:: text

    -h, --help   help for db
    -c, --config string   Configuration file to use

mattermost db downgrade
~~~~~~~~~~~~~~~~~~~~~~~

Description
  Rolls back database migrations. Requires either an update plan to roll back to, or comma-separated version numbers to be rolled back.

Format
  .. code-block:: sh

    mattermost db downgrade

Example
  .. code-block:: sh

    mattermost db downgrade 99,100,101

Options
  .. code-block:: text

    --<plan-file> string      Runs the rollback migrations defined in the plan file.

mattermost db init
~~~~~~~~~~~~~~~~~~

Description
    Initializes the database for a given data source name (DSN), executes migrations, and loads custom defaults when specified.

Format
  .. code-block:: sh

    mattermost db init

Examples
  Use the ``config`` flag to pass the DSN:
    
  .. code-block:: sh

    mattermost db init --config postgres://localhost/mattermost
       
  Run this command to use the ``MM_CONFIG`` environment variable:
    
  .. code-block:: sh
      
    MM_CONFIG=postgres://localhost/mattermost mattermost db init
    
  Run this command to set a custom defaults file to be loaded into the database: 
    
  .. code-block:: sh
    
    MM_CUSTOM_DEFAULTS_PATH=custom.json MM_CONFIG=postgres://localhost/mattermost mattermost db init

mattermost db migrate
~~~~~~~~~~~~~~~~~~~~~

Description
  Migrates the database schema if there are any unapplied migrations.

Child Commands
  -  `mattermost db downgrade`_ - Roll back database migrations.

Format
  .. code-block:: sh

    mattermost db migrate

Example
  .. code-block:: sh

    mattermost db migrate

Options
  .. code-block:: text

    --auto-recover bool     If the migration plan receives an error during migrations, this command will try to rollback migrations already applied within the plan. Not recommended without reviewing migration plan by combining --save-plan and --dry-run options.
    --save-plan bool        Saves the plan for the migration into the file store so that it can be used for reviewing the plan or for downgrading.
    --dry-run bool          Does not apply the migrations, but it validates how the migration would run based on the given conditions.

mattermost db reset
~~~~~~~~~~~~~~~~~~~~

Description
  Resets the database to its initial state. Doesn't start the application server. Only starts the store layer and truncates the tables, excluding the ``migrations`` table.

Format
  .. code-block:: sh

    mattermost db reset

Example
  .. code-block:: sh

    bin/mattermost db reset

mattermost db version
~~~~~~~~~~~~~~~~~~~~~~

Description
  Returns the most recently applied version number.

Format
  .. code-block:: sh

    mattermost db version

----

mattermost export
-----------------

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

Description
  Commands for exporting data for compliance and for merging multiple Mattermost instances.

Child Commands
  -  `mattermost export actiance`_ - Deprecated from Mattermost v10.5 in favor of `mattermost export schedule`_.
  -  `mattermost export csv`_ - Deprecated from Mattermost v10.5.
  -  `mattermost export global-relay-zip`_ - Deprecated from Mattermost v10.5.
  -  `mattermost export schedule`_ - Schedule a compliance export job.
  -  `mattermost export bulk`_ - Export data to a file compatible with the Mattermost :doc:`Bulk Import format </administration-guide/onboard/bulk-loading-data>`. Deprecated in favor of :ref:`mmctl export commands <administration-guide/manage/mmctl-command-line-tool:mmctl export>`.

mattermost export actiance
~~~~~~~~~~~~~~~~~~~~~~~~~~

From Mattermost v10.5, this command has been deprecated. It will be added to the mmctl command line tool in a future version. Until then, please use `mattermost export schedule`_. 

mattermost export csv
~~~~~~~~~~~~~~~~~~~~~

From Mattermost v10.5, this command has been deprecated. It will be added to the mmctl command line tool in a future version.

mattermost export global-relay-zip
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From Mattermost v10.5, this command has been deprecated. It will be added to the mmctl command line tool in a future version.

mattermost export schedule
~~~~~~~~~~~~~~~~~~~~~~~~~~

Description
    Schedule an export job in a format suitable for importing into a third-party archive system.

Format
  .. code-block:: sh

    mattermost export schedule

Example
  .. code-block:: sh

    bin/mattermost export schedule --exportFrom=1513102632

Options
  .. code-block:: text

    --exportFrom string     Unix timestamp (seconds since epoch, UTC) to export data from.
    --timeoutSeconds string Set how long the export should run for before timing out.

mattermost export bulk
~~~~~~~~~~~~~~~~~~~~~~

From Mattermost v6.0, this command has been deprecated in favor of :ref:`mmctl export commands <administration-guide/manage/mmctl-command-line-tool:mmctl export>` as the supported way to export data out of Mattermost.

----

mattermost help
---------------

Description
  Generate full documentation in Markdown format for the Mattermost command line tools.

Format
  .. code-block:: sh

    mattermost help {outputdir}

.. _command-line-tools-mattermost-jobserver:

----

mattermost import
-----------------

Description
  Import data into Mattermost.

Child Command
  -  `mattermost import bulk`_ - Import a Mattermost Bulk Import File. Deprecated in favor of :ref:`mmctl import commands <administration-guide/manage/mmctl-command-line-tool:mmctl import>`.
  -  `mattermost import slack`_ - Import a team from Slack.

mattermost import bulk
~~~~~~~~~~~~~~~~~~~~~~

From Mattermost v6.0, this command has been deprecated in favor of :ref:`mmctl import commands <administration-guide/manage/mmctl-command-line-tool:mmctl import>` as the supported way to import data into Mattermost.

mattermost import slack
~~~~~~~~~~~~~~~~~~~~~~~

See the :ref:`mmctl import commands <administration-guide/manage/mmctl-command-line-tool:mmctl import>` documentation as the preferred way to import Slack data into Mattermost.

Description
  Import a team from a Slack export zip file.

Format
    . code-block:: sh

    mattermost import slack {team} {file}

Example
  .. code-block:: sh

    bin/mattermost import slack myteam slack_export.zip

----

mattermost jobserver
--------------------

Description
  Start the Mattermost job server.

Format
  .. code-block:: sh

    mattermost jobserver

Example
  .. code-block:: sh

    bin/mattermost jobserver

----

mattermost server
-----------------

Description
  Runs the Mattermost server.

Format
  .. code-block:: sh

    mattermost server

----

mattermost version
------------------

.. note::

  From Mattermost v6.5, this CLI command no longer interacts with the database. The :ref:`mattermost db migrate <administration-guide/manage/command-line-tools:mattermost db migrate>` CLI command has been introduced to trigger schema migrations.

Desription
    Displays Mattermost version information.

Format
  .. code-block:: sh

    mattermost version

----

Troubleshooting
----------------

Executing a command hangs and doesn't complete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have Bleve search indexing enabled, temporarily disable it in **System Console > Experimental > Bleve** and run the command again. You can also optionally use the new :doc:`mmctl Command Line Tool </administration-guide/manage/mmctl-command-line-tool>`.

Bleve does not support multiple processes opening and manipulating the same index. Therefore, if the Mattermost server is running, an attempt to run the CLI will lock when trying to open the indeces.

If you aren't using the Bleve search indexing, feel free to post in our `Troubleshooting forum <https://forum.mattermost.com/c/trouble-shoot/16>`_ to get help.
