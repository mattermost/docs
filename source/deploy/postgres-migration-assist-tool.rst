Automated PostgreSQL migration
===============================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Migrating databases can be a daunting task, and it can be easy to overlook or misinterpret some of the required steps if you haven't performed a migration before. Our ``migration-assist`` tool provides an efficient, error-free migration experience that automates the :doc:`tasks to be executed </deploy/manual-postgres-migration>`, even in air-gapped deployment environments.

Not sure this tool is right for your Mattermost deployment? Mattermost customers looking for tailored guidance based on their Mattermost deployment can contact a `Mattermost Expert <https://mattermost.com/contact-sales/>`_.

Install
-------

Download the Mattermost ``migration-assist`` tool from the GitHub repository `releases page <https://github.com/mattermost/migration-assist/releases>`_.

While you can run the ``migration-assist`` tool on the same server as your Mattermost deployment, we recommend running the tool in a virtual machine on the same network as your Mattermost server instead. The tool itself is lightweight and does not require a large server. A server with 2 CPU cores and 16 GB of RAM should be sufficient. If preferred, you can download and `compile <#compile-the-migration-assist-tool>`__ the ``migration-assist`` tool yourself.

You'll also need to install the ``pgloader`` tool to migrate your data from MySQL to PostgreSQL. We recommend running ``pgloader`` in a virtual machine on the same network as your Mattermost server. See the :ref:`pgloader <deploy/manual-postgres-migration:install pgloader>` installation documentation for details.

Usage
-----

.. important::

   Please make sure you have the necessary environment to perform the migration. Ensure that the MySQL and PostgreSQL databases are running and accessible. To set up a PostgreSQL instance, see the :doc:`prepare your Mattermost database </deploy/server/preparations>` documentation for details.

Step 1 - Check the MySQL database schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following command to check the MySQL database schema:

.. code-block:: sh

   migration-assist mysql "<MYSQL_DSN>" # example DSN: "user:password@tcp(address:3306)/db_name"

This command outputs the readiness status and prints required fixes for common issues. The flags for fixes are as follows (where all fixes can be used together at the same time):

.. code-block:: text

   --fix-artifacts               Removes the artifacts from older versions of Mattermost
   --fix-unicode                 Removes the unsupported unicode characters from MySQL tables
   --fix-varchar                 Removes the rows with varchar overflow

Step 2 - Create the PostgreSQL database schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following command to create the Postgres database schema:

.. code-block:: sh

   migration-assist postgres "<POSTGRES_DSN>" --run-migrations --mattermost-version="<MATTERMOST_VERSION>" # example DSN: "postgres://user:password@address:5432/db_name", example Mattermost version: "v9.4.0"

This command downloads the necessary migrations and applies them to the Postgres database. The ``--mattermost-version`` flag is required to specify the Mattermost version you are migrating from.

There are two flags that can be used with the ``migration-assist postgres`` command to run a few checks before running the migrations. You can disable them by setting the following flags to false:

.. code-block:: shell

   --check-schema-owner          Check if the schema owner is the same as the user running the migration (default true)
   --check-tables-empty          Check if tables are empty before running migrations (default true)

Step 3 - Generate a pgloader configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following command to generate a pgloader configuration:

.. code-block:: sh

   migration-assist pgloader --mysql="<MYSQL_DSN>" --postgres="<POSTGRES_DSN>" > migration.load

This command will generate a pgloader configuration file that can be used to migrate the data from MySQL to Postgres.

The generated configuration has the setting to remove the null character from the text type data. This is to ensure the migration won't return errors while inserting data into Postgres. However, if you want to disable this behavior, you can set the ``--remove-null-chars`` to ``false``.

Step 4 - Run pgloader
~~~~~~~~~~~~~~~~~~~~~

:ref:`Run pgloader <deploy/manual-postgres-migration:pgloader>` with the generated configuration file:

.. code-block:: sh

   pgloader migration.load > migration.log

Carefully read the log file to analyze whether there were any errors during the migration process. If there were any errors, please contact Mattermost for further guidance.

Step 5 - Restore full-text indexes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following command to create the full-text indexes for the ``Posts`` and ``FileInfo`` tables:

.. code-block:: sh

   migration-assist postgres post-migrate "<POSTGRES_DSN>" --create-indexes

This command creates the full-text indexes for the ``Posts`` and ``FileInfo`` tables. See the :ref:`Restore full-text indexes <deploy/manual-postgres-migration:restore full-text indexes>` documentation for more information.

Step 6 - Complete plugin migrations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generate migration configuration for collaborative playbooks, boards and calls:

.. code-block:: sh

   migration-assist pgloader boards --mysql="<MYSQL_DSN>" --postgres="<POSTGRES_DSN>" > boards.load
   migration-assist pgloader playbooks --mysql="<MYSQL_DSN>" --postgres="<POSTGRES_DSN>" > playbooks.load
   migration-assist pgloader calls --mysql="<MYSQL_DSN>" --postgres="<POSTGRES_DSN>" > calls.load

Then run pgloader with the generated configuration files:

.. code-block:: sh

   pgloader boards.load > boards_migration.log
   pgloader playbooks.load > playbooks_migration.log
   pgloader calls.load > calls.log

Carefully read the log file to analyze whether there were any errors during the migration process. See the :ref:`Plugin migrations <deploy/manual-postgres-migration:plugin migrations>` documentation for information on migrating Playbooks, Boards and Calls.

Step 7 - Configure Mattermost to utilize the new PostgreSQL database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the final step of the migration process, where we need to update the Mattermost configuration to point to the new PostgreSQL database. To do so, locate the ``SqlSettings.DataSource`` and ``SqlSettings.DriverName`` fields in the ``config.json`` then modify these fields to reflect the new PostgreSQL database connection details. See the :ref:`Environment configuration settings <configure/environment-configuration-settings:database>` documentation for more information.

.. note::

  If your configuration was stored in the database, see the :ref:`configuration in database <deploy/manual-postgres-migration:configuration in database>` documentation for migration details. Once migrated, you should also update the ``MM_CONFIG`` environment variable to point to the new DSN.

.. note::
  If your Mattermost deployment was initially configured with MySQL, there's a good chance your systemd service file has a ``BindsTo=mysql.service`` directive in it. This will cause the Mattermost server to be shut down if you deactivate your MySQL service. To fix this, update all references to ``mysql.service`` in your service file to use ``postgresql.service`` instead. This is only an issue if your Database and Mattermost are running on the same system.

Air-gapped environments
------------------------

The ``migration-assist`` tool contains all necessary files for migration, removing any need for external access to repositories. Once transferred across the air gap, the tool operates independently. Follow the guidance below to perform a seamless MySQL to PostgreSQL migration in an air-gapped environment without needing external dependencies:

1. Verify that the ``migration-assist`` binary is the latest version available to benefit from improvements and fixes.

2. Transfer the latest version of the ``migration-assist`` binary into the air-gapped environment.

3. Generate the schema and data output file from MySQL using the ``--fix`` flags for Unicode, artifacts, and VARCHAR. This step is crucial to ensure the MySQL database is ready for migration. The following command checks the MySQL database schema, applies necessary fixes, and automatically produces a file named ``mysql.output``:

   .. code-block:: sh

      migration-assist mysql "user:password@tcp(localhost:3306)/mattermost" --fix-unicode --fix-artifacts --fix-varchar

4. Use the ``mysql.output`` file to apply the schema and data into the PostgreSQL database:

   .. code-block:: sh

      migration-assist postgres "postgres://mmuser:mostest@localhost:5432/imported?sslmode=disable" --run-migrations --applied-migrations="./mysql.output"

5. Follow `step 3 <#step-3-generate-a-pgloader-configuration>`__ through `step 7 <#step-7-configure-mattermost-to-utilize-the-new-postgresql-database>`__ above to complete the migration process using the ``migration-assist`` tool.

Tool commands
--------------

The ``migration-assist`` tool offers 3 core utility commands:

1. ``migration-assist mysql``

   Checks the MySQL database schema to ensure readiness for migration, and offers fixes for common issues. See the `install <#install>`__ section below for details on installing the ``migration-assist`` tool.

2. ``migration-assist postgres``

   Creates the PostgreSQL database schema, and prepares it for Mattermost deployment by downloading the necessary migrations and applying them.

3. ``migration-assist pgloader``

   Generates a pgloader configuration from DSN values, ensuring accurate data transfer. See the :ref:`install pgloader <deploy/manual-postgres-migration:install pgloader>` documentation for details on installing the pgloader tool.

Compile the migration-assist tool
---------------------------------

You can download and compile the ``migration-assist`` tool with the `Go <https://go.dev/>`__ toolchain. The tool requires at least ``v1.22`` of the Go compiler.

Use ``go install`` to install the tool:

.. code-block:: shell

   go install github.com/mattermost/migration-assist/cmd/migration-assist@latest

Troubleshooting
---------------

See :ref:`troubleshooting errors during migration from MySQL to PostgreSQL <deploy/postgres-migration:troubleshooting>`
