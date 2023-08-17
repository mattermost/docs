Migration Guidelines from MySQL to PostgreSQL
=============================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

As of version 8.0, a significant decision has been made to establish PostgreSQL as the default database for Mattermost, a step taken to enhance the platform’s performance and capabilities. Recognizing the importance of supporting the community members who are interested in migrating from a MySQL database, we have taken proactive measures to provide them with some assistance. To streamline the migration process and alleviate any potential challenges, we have prepared a comprehensive set of basic guidelines to facilitate a smooth transition. Additionally, we want to offer recommendations for various tools that have proven to be highly effective in simplifying the migration efforts.

Note that this guideline is still in development and we are working to streamline the migration process. We are planning to improve this guide by periodically updating it. Please use this guide as a starting point and always backup your database before starting the migration.

Table of Contents
-----------------

-  `Required tools <#required-tools>`__
-  `Before the migration <#before-the-migration>`__
-  `Prepare target database <#prepare-target-database>`__
-  `Schema Differences <#schema-diffs>`__
-  `Migrate the data <#migrate-the-data>`__
-  `Compare the data <#compare-the-data>`__
-  `Notes <#notes>`__

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
-  Find your mattermost version. You can look to the about modal from the web app.
-  Determine migration window the process requires application to stop.
-  See the `schema-diffs <#schema-diffs>`__ section to ensure data compatibility between schemas.
-  Prepare your PostgreSQL environment by creating a database and user. See more info `here <https://docs.mattermost.com/install/prepare-mattermost-database.html>`__

Prepare target database
-----------------------

-  Clone mattermost repository for your specific version:
   ``git clone -b <your current version (eg. release-7.8)> git@github.com:mattermost/mattermost.git --depth=1``
-  ``cd`` into ``mattermost`` project*.
-  Create a postgres database using morph CLI with the following command:

.. code:: bash

   morph apply up --driver postgres --dsn "postgres://user:pass@localhost:5432/<target_db_mame>?sslmode=disable" --path ./db/migrations/postgres --number -1

\* After ``v8`` due to project re-organization, the migrations directory has been changed to ``./server/channels/db/migrations/postgres/`` relative to project root. Therefore ``cd`` into ``mattermost/server/channels``.

Schema Diffs
------------

Before the migration, due to differences between two schemas some manual steps may required to have an error-free migration.

Text to Character Varying
~~~~~~~~~~~~~~~~~~~~~~~~~

Since our MySQL schema uses ``text`` column type in the various tables instead of ``varchar`` represantation in the PostgreSQL schema, we encourage to check if the sizes are consistent within the Postgres schema limits.

================ ================ =====================
Table            Column           Data Type Casting
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

As you can see there are several occurrences where schema can differ and data size constaints within the Postgres schema can result in errors. Several reports have been received from our community members that ``LinkMetadata`` and ``FileInfo`` tables indeed had some overflows so we recommend checking these tables in particular. Please do check if your data in MySQL schema exceed these limitations. You can check if there are any required deletions. For example to do so in the Audits table/Action column; run:

.. code:: sql

   DELETE FROM mattermost.Audits where LENGTH(Action) > 512;

Full-text indexes
~~~~~~~~~~~~~~~~~

There is a possibility where some words in the ``Posts`` ans ``FileInfo`` tables can exceed the `limits of the maximum token length <https://www.postgresql.org/docs/11/textsearch-limitations.html>`__ for full text search indexing. In that case we recommend dropping ``idx_posts_message_txt`` and ``idx_fileinfo_content_txt`` indexes from the PostgreSQL schema and creating these indexes after the migration by running following queries:

Tp drop indexes run these before the migration:

.. code:: sql

   DROP INDEX IF EXISTS idx_posts_message_txt;
   DROP INDEX IF EXISTS idx_fileinfo_content_txt;

To re-create indexes, run these once the migration is completed:

.. code:: sql

   CREATE INDEX IF NOT EXISTS idx_posts_message_txt ON posts USING gin(to_tsvector('english', message));
   CREATE INDEX IF NOT EXISTS idx_fileinfo_content_txt ON fileinfo USING gin(to_tsvector('english', content));

Migrate the data
----------------

Now we set the schema to desired state and we can start migrating the **data** by running ``pgLoader`` \*\*

\*\* Use the following configuration for the baseline of the data migration:

.. code:: sql

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

Once you save this configuration file eg. ``migration.load``, you can run the ``pgLoader`` with following command:

.. code:: bash

   pgLoader migration.load > migration.log

Feel free to contribute and/or report your findings through the migration.

Compare the data
----------------

We internally developed a tool to simplify the process of comparing contents of two databases. The ``dbcmp`` tool compares every table and reports whether if there is a diversity between two schemas.

The tool has a few flags needs to be supplied to run a comparison:

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

   dbcmp --source "${MYSQL_DSN}" --target "${POSTGRES_DSN}" --exclude="db_migrations","ir_","focalboard","systems"

Note that the migration guide only covers the tables for Mattermost channels, the support for other plugins such as Boards and Playbooks will be added in the future. Another exlusion we are making is in the ``db_migrations`` table which has a small difference (a typo in a single migration name) creates a diff. Since we created the Postgres schema with morph and the official mattermost source, we can consider to skip it safely. On the other hand, ``systems`` table may contain additional diffs if there was extra keys added during some of the migrations. Consider excluding ``systems`` table if you run into issues and do a manual comparison as the data in the ``systems`` table is relatively smaller in size.

Notes
-----

Keep in mind that this migration guide primarily focuses on providing step-by-step instructions for the migration; however, it is essential to note that it does not encompass migration configurations for any plugins, such as Focalboard and Playbooks. If your system utilizes these plugins, we highly advise exercising patience until we incorporate the necessary configurations specifically tailored to ensure a smooth transition for those plugins as well.
