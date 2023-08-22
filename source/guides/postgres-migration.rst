Migration guidelines from MySQL to PostgreSQL
=============================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

From Mattermost v8.0, PostgreSQL is our database of choice for Mattermost to enhance the platform’s performance and capabilities. Recognizing the importance of supporting the community members who are interested in migrating from a MySQL database, we have taken proactive measures to provide guidance and best practices. 

To streamline the migration process and alleviate any potential challenges, we have prepared a comprehensive set of guidelines to facilitate a smooth transition. Additionally, we want to offer recommendations for various tools that have proven to be highly effective in simplifying your migration efforts.

.. note::

   These guidelines are in development and we are working to streamline the migration process. We plan to improve this guide by updating it as new information becomes available. It is essential to note that it does not encompass migration configurations for any plugins, such as Focalboard and Playbooks. If your system utilizes these plugins, we highly advise exercising patience until we incorporate the necessary configurations specifically tailored to ensure a smooth transition for those plugins as well. Please use this guide as a starting point and always backup your database before starting a migration.

.. contents:: On this page:
  :backlinks: top
  :local:
  :depth: 1

Required tools
--------------

-  Install ``pgLoader``. See the official `installation
   guide <https://pgloader.readthedocs.io/en/latest/install.html>`__.
-  Install morph CLI via running the following command:

   -  ``go install github.com/mattermost/morph/cmd/morph@v1``

-  Optinally install ``dbcmp`` to compare the data after a migration:

   -  ``go install github.com/mattermost/dbcmp/cmd/dbcmp@latest``

Before the migration
--------------------

-  Backup your MySQL data.
-  Confirm your Mattermost version. See the **About** modal for details. 
-  Determine the migration window needed. This process requires you to stop the Mattermost Server during the migration.
-  See the `schema-diffs <#schema-diffs>`__ section to ensure data compatibility between schemas.
-  Prepare your PostgreSQL environment by creating a database and user. See the `database </install/prepare-mattermost-database.html>`__ documentation for details.

Prepare target database
-----------------------

-  Clone the ``mattermost`` repository for your specific version:
   ``git clone -b <your current version (eg. release-7.8)> git@github.com:mattermost/mattermost.git --depth=1``
-  ``cd`` into ``mattermost`` project*.
-  Create a PostgreSQL database using morph CLI with the following command:

.. code:: bash

   morph apply up --driver postgres --dsn "postgres://user:pass@localhost:5432/<target_db_mame>?sslmode=disable" --path ./db/migrations/postgres --number -1

\* After ``v8`` due to project re-organization, the migrations directory has been changed to ``./server/channels/db/migrations/postgres/`` relative to project root. Therefore ``cd`` into ``mattermost/server/channels``.

Schema diffs
------------

Before the migration, due to differences between two schemas, some manual steps may required to have an error-free migration.

Text to character varying
~~~~~~~~~~~~~~~~~~~~~~~~~

Since the Mattermost MySQL schema uses the ``text`` column type in the various tables instead of ``varchar`` representation in the PostgreSQL schema, we encourage you to check if the sizes are consistent within the PostgreSQL schema limits.

================ ================ =====================
Table            Column           Data type casting
================ ================ =====================
Audits           Action           text -> varchar(512)
Audits           ExtraInfo        text -> varchar(1024)
ClusterDiscovery HostName         text -> varchar(512)
Commands         IconURL          text -> varchar(1024)
Commands         AutoCompleteDesc text -> varchar(1024)
Commands         AutoCompleteHint text -> varchar(1024)
Compliances      Keywords         text -> varchar(512)
Compliances      Emails           text -> varchar(1024)
FileInfo         Path             text -> varchar(512)
FileInfo         ThumbnailPath    text -> varchar(512)
FileInfo         PreviewPath      text -> varchar(512)
FileInfo         Name             text -> varchar(256)
FileInfo         MimeType         text -> varchar(256)
LinkMetadata     URL              text -> varchar(2048)
RemoteClusters   SiteURL          text -> varchar(512)
RemoteClusters   Topics           text -> varchar(512)
Sessions         DeviceId         text -> varchar(512)
Systems          Value            text -> varchar(1024)
UploadSessions   FileName         text -> varchar(256)
UploadSessions   Path             text -> varchar(512)
================ ================ =====================

As you can see, there are several occurrences where the schema can differ and data size constraints within the PostgreSQL schema can result in errors. Several reports have been received from our community that ``LinkMetadata`` and ``FileInfo`` tables had some overflows, so we recommend checking these tables in particular. Please do check if your data in the MySQL schema exceeds these limitations. You can check if there are any required deletions. For example, to do so in the ``Audits`` table/``Action`` column; run:

.. code:: sql

   DELETE FROM mattermost.Audits where LENGTH(Action) > 512;

Full-text indexes
~~~~~~~~~~~~~~~~~

It's possible that some words in the ``Posts`` and ``FileInfo`` tables can exceed the `limits of the maximum token length <https://www.postgresql.org/docs/11/textsearch-limitations.html>`__ for full text search indexing. In these cases, we recommend dropping the ``idx_posts_message_txt`` and ``idx_fileinfo_content_txt`` indexes from the PostgreSQL schema, and creating these indexes after the migration by running following queries:

To drop indexes, run the following commands before the migration:

.. code:: sql

   DROP INDEX IF EXISTS idx_posts_message_txt;
   DROP INDEX IF EXISTS idx_fileinfo_content_txt;

To re-create indexes, run the following once the migration is completed:

.. code:: sql

   CREATE INDEX IF NOT EXISTS idx_posts_message_txt ON posts USING gin(to_tsvector('english', message));
   CREATE INDEX IF NOT EXISTS idx_fileinfo_content_txt ON fileinfo USING gin(to_tsvector('english', content));

Migrate the data
----------------

Once we set the schema to desired state, we can start migrating the **data** by running ``pgLoader`` \*\*

\*\* Use the following configuration for the baseline of the data migration:

.. code::

   LOAD DATABASE
        FROM      mysql://{{ .mysql_user }}:{{ .mysql_password }}@mysql:3306/{{ .source_schema }}
        INTO      pgsql://{{ .pg_user }}:{{ .pg_password }}@postgres:5432/{{ .target_schema }}

   WITH data only,
        workers = 8, concurrency = 1,
        multiple readers per thread, rows per range = 50000,
        create no tables,
        create no indexes,
        preserve index names

   SET PostgreSQL PARAMETERS
        maintenance_work_mem to '128MB',
        work_mem to '12MB'

   SET MySQL PARAMETERS
         net_read_timeout  = '120',
         net_write_timeout = '120'

   CAST column Channels.Type to channel_type drop typemod,
        column Teams.Type to team_type drop typemod,
        column UploadSessions.Type to upload_session_type drop typemod,
        column Drafts.Priority to text,
        type int when (= precision 11) to integer drop typemod,
        type bigint when (= precision 20) to bigint drop typemod,
        type text to varchar drop typemod,
        type tinyint when (<= precision 4) to boolean using tinyint-to-boolean,
        type json to jsonb drop typemod

   MATERIALIZE VIEWS exclude_products
        excluding table names matching ~<IR_>, ~<focalboard>

   BEFORE LOAD DO
        $$ ALTER SCHEMA public RENAME TO {{ .source_schema }}; $$

   AFTER LOAD DO
        $$ UPDATE {{ .source_schema }}.db_migrations set name='add_createat_to_teamembers' where version=92; $$,
        $$ ALTER SCHEMA {{ .source_schema }} RENAME TO public; $$;

Once you save this configuration file, eg. ``migration.load``, you can run the ``pgLoader`` with following command:

.. code:: bash

   pgLoader migration.load > migration.log

Feel free to contribute to and/or report your findings through your migration to us.

Compare the data
----------------

We internally developed a tool to simplify the process of comparing contents of two databases. The ``dbcmp`` tool compares every table and reports whether if there is a diversion between two schemas.

The tool includes a few flags to run a comparison:

.. code:: sh

   Usage:
     dbcmp [flags]

   Flags:
         --exclude strings   exclude tables from comparison, takes comma-separated values.
     -h, --help              help for dbcmp
         --source string     source database dsn
         --target string     target database dsn
     -v, --version           version for dbcmp

For our case we can simply run the following command:

.. code:: sh

   dbcmp --source "${MYSQL_DSN}" --target "${POSTGRES_DSN}" --exclude="db_migrations,ir_,focalboard,systems"

Note that this migration guide only covers the tables for Mattermost channels. Support for other plugins, such as Playbooks, will be added in the future. 

Another exclusion we are making is in the ``db_migrations`` table which has a small difference (a typo in a single migration name) creates a diff. Since we created the PostgreSQL schema with morph, and the official ``mattermost`` source, we can skip it safely without concerns. On the other hand, ``systems`` table may contain additional diffs if there were extra keys added during some of the migrations. Consider excluding the ``systems`` table if you run into issues, and perform a manual comparison as the data in the ``systems`` table is relatively smaller in size.
