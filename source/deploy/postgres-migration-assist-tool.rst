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

You'll also need to install the ``pgloader`` tool to migrate your data from MySQL to PostgreSQL. We recommend running ``pgloader`` in a virtual machine on the same network as your Mattermost server. You can use our official Mattermost Docker image for pgloader (``mattermost/pgloader:latest``); please note that it does **not** currently support MySQL’s ``caching_sha2_password`` authentication plugin. If you require ``caching_sha2_password`` support, you’ll need to build your own image and include the `qitab/qmynd <https://github.com/qitab/qmynd>`_ library. See the :ref:`pgloader <deploy/manual-postgres-migration:install pgloader>` installation documentation for details.

Usage
-----

.. important::

  - If you encounter heap exhaustion errors in ``pgloader``, edit your generated ``migration.load`` and under the ``WITH`` block set: ``prefetch rows = 1000`` and consider reducing it if the issue persists.
  - Please make sure you have the necessary environment to perform the migration. Ensure that the MySQL and PostgreSQL databases are running and accessible. To set up a PostgreSQL instance, see the :doc:`prepare your Mattermost database </deploy/server/preparations>` documentation for details.

Step 1 - Check the MySQL database schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following command to check the MySQL database schema:

.. code-block:: sh

   migration-assist mysql "<MYSQL_DSN>"  # example DSN: "user:password@tcp(address:3306)/db_name"

This command outputs the readiness status and prints required fixes for common issues. The flags for fixes are as follows (you can combine all of them):

.. code-block:: text

   --fix-artifacts   Removes the artifacts from older versions of Mattermost
   --fix-unicode     Strips unsupported Unicode characters from MySQL tables
   --fix-varchar     Removes rows exceeding column lengths

Step 2 - Create the PostgreSQL database schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before running migrations, ensure the ``public`` schema is owned by your migration user:

.. code-block:: sql

   sudo -u postgres psql -d mattermost -c "ALTER SCHEMA public OWNER TO mmuser; GRANT ALL ON SCHEMA public TO mmuser;"

Then run:

.. code-block:: sh

   migration-assist postgres "<POSTGRES_DSN>" \
     --run-migrations \
     --mattermost-version="<MATTERMOST_VERSION>"

- ``<POSTGRES_DSN>`` example: ``postgres://user:password@address:5432/db_name``
- ``<MATTERMOST_VERSION>`` example: ``10.5.4``

By default, two pre-checks run before migration:

- ``--check-schema-owner=true``
- ``--check-tables-empty=true``

To disable them:

.. code-block:: sh

   --check-schema-owner=false \
   --check-tables-empty=false

Step 3 - Generate a pgloader configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following command to emit a pgloader configuration file:

.. code-block:: sh

   migration-assist pgloader \
     --mysql="<MYSQL_DSN>" \
     --postgres="<POSTGRES_DSN>" \
     --remove-null-chars \
     > migration.load

- By default, null characters in text columns are stripped. Disable with ``--remove-null-chars=false``.
- If you run out of heap, edit ``migration.load`` and under the ``WITH`` block set:

  .. code-block:: text

     prefetch rows = 1000

Step 4 - Run pgloader
~~~~~~~~~~~~~~~~~~~~~

:ref:`Run pgloader <deploy/manual-postgres-migration:pgloader>` with the generated configuration file:

.. code-block:: sh

   pgloader migration.load > migration.log

Carefully review `migration.log` for errors (e.g., duplicate-key or missing-table warnings). Use the ``mattermost/pgloader:latest`` Docker image to avoid build/auth issues.

Step 5 - Restore full-text indexes & create all indexes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run:

.. code-block:: sh

   migration-assist postgres post-migrate --create-indexes "<POSTGRES_DSN>"

- The ``--create-indexes`` flag rebuilds full-text indexes on ``Posts`` and ``FileInfo``, plus all other Mattermost indexes.
- Omitting that flag only restores full-text indexes for ``Posts`` and ``FileInfo``.

See the :ref:`Restore full-text indexes <deploy/manual-postgres-migration:restore full-text indexes>` documentation for details.

Step 6 - Complete plugin migrations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generate pgloader configs for Playbooks, Boards, and Calls:

.. code-block:: sh

   migration-assist pgloader boards \
     --mysql="<MYSQL_DSN>" \
     --postgres="<POSTGRES_DSN>" > boards.load
   migration-assist pgloader playbooks \
     --mysql="<MYSQL_DSN>" \
     --postgres="<POSTGRES_DSN>" > playbooks.load
   migration-assist pgloader calls \
     --mysql="<MYSQL_DSN>" \
     --postgres="<POSTGRES_DSN>" > calls.load

Run each:

.. code-block:: sh

   pgloader boards.load           > boards_migration.log
   pgloader playbooks.load        > playbooks_migration.log
   pgloader calls.load            > calls_migration.log

Skip any plugin you don't use; check logs for JSON or missing-table errors. See the :ref:`Plugin migrations <deploy/manual-postgres-migration:plugin migrations>` guide for more.

Step 7 - Configure Mattermost to use PostgreSQL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In your ``config.json`` or via environment variables, update:

.. code-block:: json

   "SqlSettings": {
     "DriverName": "postgres",
     "DataSource": "postgres://mmuser:pass@db:5432/mattermost?sslmode=disable"
   }

If your config was stored in the database, update ``MM_CONFIG`` accordingly. See the :ref:`environment configuration settings <configure/environment-configuration-settings:database>` documentation for details.

.. note::
  If your Mattermost deployment was initially configured with MySQL, there's a good chance your systemd service file has a ``BindsTo=mysql.service`` directive in it. This will cause the Mattermost server to be shut down if you deactivate your MySQL service. To fix this, update all references to ``mysql.service`` in your service file to use ``postgresql.service`` instead. This is only an issue if your Database and Mattermost are running on the same system.

Air-gapped environments
------------------------

Follow these steps to migrate within an air-gapped environment:

1. **Verify** that the `migration-assist` binary is the latest version available to benefit from improvements and fixes.
2. **Transfer** the latest `migration-assist` binary into the air-gapped environment (e.g., via secure media).
3. **Generate** the MySQL schema+data output using fix flags. This produces ``mysql.output``:

   .. code-block:: sh

      migration-assist mysql "user:pass@tcp(localhost:3306)/mattermost" \
        --fix-artifacts --fix-unicode --fix-varchar > mysql.output

4. **Apply** migrations using the generated output:

   .. code-block:: sh

      migration-assist postgres \
        "postgres://mmuser:pass@localhost:5432/imported?sslmode=disable" \
        --run-migrations --applied-migrations="./mysql.output"

5. **Continue** from **Step 3** through **Step 7** above to complete data transfer and configuration.

Tool commands
--------------

The ``migration-assist`` tool offers 3 core commands:

1. ``migration-assist mysql`` — Checks MySQL schema readiness and offers fixes.
2. ``migration-assist postgres`` — Builds the PostgreSQL schema and applies migrations.
3. ``migration-assist pgloader`` — Generates a pgloader config for data transfer.

Compile the migration-assist tool
---------------------------------

Requires Go ≥ v1.22. Install with:

.. code-block:: shell

   go install github.com/mattermost/migration-assist/cmd/migration-assist@latest

Troubleshooting
---------------

See :ref:`troubleshooting errors during migration from MySQL to PostgreSQL <deploy/postgres-migration:troubleshooting>`.
