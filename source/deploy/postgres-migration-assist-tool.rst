Automate PostgreSQL migration
=============================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Migrating databases can be a daunting task, and it can be easy to overlook or misinterpret some of the required steps if you haven't performed a migration before. 

Our ``migration-assist`` tool provides an efficient, error-free migration experience that automates the tasks to be executed. The tool offers 3 core utility commands:

1. ``migration-assist mysql``

   Checks the MySQL database schema to ensure readiness for migration, and offers fixes for common issues.

2. ``migration-assist postgres``

   Creates the PostgreSQL database schema, and prepares it for Mattermost deployment by downloading the necessary migrations and applying them.

3. ``migration-assist pgloader``

   Generates a pgloader configuration from DSN values, ensuring accurate data transfer.

Install
-------

The ``migration-assist`` tool can be downloaded and compiled with the `Go <https://go.dev/>`__ toolchain. The tool requires at least ``v1.22`` of the Go compiler.

Use ``go install`` to install the tool:

.. code-block:: shell

   go install github.com/mattermost/migration-assist/cmd/migration-assist@latest

.. note::

   To download pre-compiled versions of migration-assist, visit the `releases page <https://github.com/mattermost/migration-assist/releases>`__ for further guidance.

Usage
-----

.. important::

   Please make sure you have the necessary environment to perform the migration. Ensure that the MySQL and PostgreSQL databases are running and accessible. To setup a PostgreSQL instance, see the :doc:`database </install/prepare-mattermost-database>` documentation for details.

Step 1 - Check the MySQL database schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following command to check the MySQL database schema:

.. code-block:: shell

   migration-assist mysql "<MYSQL_DSN>" # example DSN: "user:password@tcp(address:3306)/db_name"

This command outputs the readiness status and prints required fixes for common issues. The flags for fixes are as follows (where all fixes can be used together at the same time):

.. code-block:: shell

   --fix-artifacts               Removes the artifacts from older versions of Mattermost
   --fix-unicode                 Removes the unsupported unicode characters from MySQL tables
   --fix-varchar                 Removes the rows with varchar overflow

Step 2 - Create the PostgreSQL database schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following command to create the Postgres database schema:

.. code-block:: shell

   migration-assist postgres "<POSTGRES_DSN>" --run-migrations --mattermost-version="<MATTERMOST_VERSION>" # example DSN: "postgres://user:password@address:5432/db_name", example Mattermost version: "v9.4.0"

This command downloads the necessary migrations and applies them to the Postgres database. The ``--mattermost-version`` flag is required to specify the Mattermost version you are migrating from.

Step 3 - Generate a pgloader configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following command to generate a pgloader configuration:

.. code-block:: shell

   migration-assist pgloader --mysql="<MYSQL_DSN>" --postgres="<POSTGRES_DSN>" > migration.load

This command will generate a pgloader configuration file that can be used to migrate the data from MySQL to Postgres.

Step 4 - Run pgloader
~~~~~~~~~~~~~~~~~~~~~

See the `install pgloader <#install-pgloader>`__ section for installation details.

Run pgloader with the generated configuration file:

.. code-block:: shell

   pgloader migration.load > migration.log

Carefully read the log file to analyze whether there were any errors during the migration process. If there were any errors, please contact Mattermost for further guidance.

Step 5 - Restore full-text indexes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following command to create the full-text indexes for the ``Posts`` and ``FileInfo`` tables:

.. code-block:: shell

   migration-assist postgres post-migrate "<POSTGRES_DSN>"

This command creates the full-text indexes for the ``Posts`` and ``FileInfo`` tables. Please refer to the `Restore full-text indexes <#restore-full-text-indexes>`__ section for more information.

Step 6 - Complete plugin migrations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generate migration configuration for Boards and Playbooks:

.. code-block:: shell

   migration-assist pgloader boards --mysql="<MYSQL_DSN>" --postgres="<POSTGRES_DSN>" > boards.load
   migration-assist pgloader playbooks --mysql="<MYSQL_DSN>" --postgres="<POSTGRES_DSN>" > playbooks.load

Then run pgloader with the generated configuration files:

.. code-block:: shell

   pgloader boards.load > boards_migration.log
   pgloader playbooks.load > playbooks_migration.log

Carefully read the log file to analyze whether there were any errors during the migration process. Please refer to the `Plugin migrations <#plugin-migrations>`__ section for further information on migrating Playbooks and Focalboard.

Step 7 - Configure Mattermost to utilize the new PostgreSQL database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the final step of the migration process, where we need to update the Mattermost configuration to point to the new PostgreSQL database. To do so, locate the ``SqlSettings.DataSource`` and ``SqlSettings.DriverName`` fields in the ``config.json`` then modify these fields to reflect the new PostgreSQL database connection details. If your configuration was stored in the database, please follow the detailed steps provided `<here <#configuration-in-database>`__. Once migrated, you should also update the ``MM_CONFIG`` environment variable to point to the new DSN.