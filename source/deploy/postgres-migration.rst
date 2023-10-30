Migration guidelines from MySQL to PostgreSQL
=============================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

From Mattermost v8.0, PostgreSQL is our database of choice for Mattermost to enhance the platform’s performance and capabilities. Recognizing the importance of supporting the community members who are interested in migrating from a MySQL database, we have taken proactive measures to provide guidance and best practices. 

To streamline the migration process and alleviate any potential challenges, we have prepared a comprehensive set of guidelines to facilitate a smooth transition. Additionally, we want to offer recommendations for various tools that have proven to be highly effective in simplifying your migration efforts.

.. note::

   These guidelines are in development and we are working to streamline the migration process. We plan to improve this guide by updating it as new information becomes available. Please use this guide as a starting point and always backup your database before starting a migration.

.. contents:: On this page
  :backlinks: top
  :local:
  :depth: 1

Required tools
--------------

-  Install ``pgLoader``. See the official `installation
   guide <https://pgloader.readthedocs.io/en/latest/install.html>`__.
-  Install morph CLI by running the following command:

   -  ``go install github.com/mattermost/morph/cmd/morph@v1``

-  Optinally install ``dbcmp`` to compare the data after a migration:

   -  ``go install github.com/mattermost/dbcmp/cmd/dbcmp@latest``

Before the migration
--------------------

.. note::
   This guide requires a schema of v6.4 or later. So, if you have an earlier version and planning to migrate, please update your Mattermost Server to v6.4 at a minimum. 

-  Back up your MySQL data.
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

Before the migration, due to differences between two schemas, some manual steps may be required for an error-free migration.

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

It's possible that some words in the ``Posts`` and ``FileInfo`` tables can exceed the `limits of the maximum token length <https://www.postgresql.org/docs/11/textsearch-limitations.html>`__ for full text search indexing. In these cases, we recommend dropping the ``idx_posts_message_txt`` and ``idx_fileinfo_content_txt`` indexes from the PostgreSQL schema, and creating these indexes after the migration by running the following queries:

To drop indexes, run the following commands before the migration (These are included in the script, so you may not need to run these manually):

.. code:: sql

   DROP INDEX IF EXISTS idx_posts_message_txt;
   DROP INDEX IF EXISTS idx_fileinfo_content_txt;

Artifacts may remain from previous configurations/versions
~~~~~~~~~~~~~~~~~

Prior to ``v6.4``, Mattermost was using `golang-migrate <https://github.com/golang-migrate/migrate>`__ to handle the schema migrations. Since we don't use it anymore, we exclude the table ``schema_migrations``. If you were using Mattermost before ``v6.4`` consider dropping this table and excluding it from comparison as well.

.. code:: sql

   DROP TABLE mattermost.schema_migrations;

Also, if you were previously utilizing a database for handling the Mattermost configuration, those tables should be removed from your MySQL database. Consider running following DDL to drop tables.

.. code:: sql

   DROP TABLE ConfigurationFiles;
   DROP TABLE Configurations;
   DROP TABLE db_config_migrations;

Some community members have reported that they had ``description`` and ``nextsyncat`` columns in their ``SharedChannelRemotes`` table. These columns should be removed from the table. Consider running following DDL to drop the columns. (This migration will be added to future versions of Mattermost).

.. code:: sql

   ALTER TABLE SharedChannelRemotes DROP COLUMN description, DROP COLUMN nextsyncat;

Migrate the data
----------------

Once we set the schema to a desired state, we can start migrating the **data** by running ``pgLoader`` \*\*

\*\* Use the following configuration for the baseline of the data migration:

.. code::

   LOAD DATABASE
        FROM      mysql://{{ .mysql_user }}:{{ .mysql_password }}@mysql:3306/{{ .source_schema }}
        INTO      pgsql://{{ .pg_user }}:{{ .pg_password }}@postgres:5432/{{ .target_schema }}

   WITH data only,
        workers = 8, concurrency = 1,
        multiple readers per thread, rows per range = 50000,
        create no tables, create no indexes,
        preserve index names

   SET PostgreSQL PARAMETERS
        maintenance_work_mem to '128MB',
        work_mem to '12MB'

   SET MySQL PARAMETERS
         net_read_timeout  = '120',
         net_write_timeout = '120'

   CAST column Channels.Type to "channel_type" drop typemod,
        column Teams.Type to "team_type" drop typemod,
        column UploadSessions.Type to "upload_session_type" drop typemod,
        column Drafts.Priority to text,
        type int when (= precision 11) to integer drop typemod,
        type bigint when (= precision 20) to bigint drop typemod,
        type text to varchar drop typemod,
        type tinyint when (<= precision 4) to boolean using tinyint-to-boolean,
        type json to jsonb drop typemod

   EXCLUDING TABLE NAMES MATCHING ~<IR_>, ~<focalboard>, schema_migrations

   BEFORE LOAD DO
        $$ ALTER SCHEMA public RENAME TO {{ .source_schema }}; $$,
        $$ DROP INDEX IF EXISTS idx_posts_message_txt; $$,
        $$ DROP INDEX IF EXISTS idx_fileinfo_content_txt; $$

   AFTER LOAD DO
        $$ UPDATE {{ .source_schema }}.db_migrations set name='add_createat_to_teamembers' where version=92; $$,
        $$ CREATE INDEX IF NOT EXISTS idx_posts_message_txt ON {{ .source_schema }}.posts USING gin(to_tsvector('english', message)); $$,
        $$ CREATE INDEX IF NOT EXISTS idx_fileinfo_content_txt ON {{ .source_schema }}.fileinfo USING gin(to_tsvector('english', content)); $$,
        $$ ALTER SCHEMA {{ .source_schema }} RENAME TO public; $$,
        $$ SELECT pg_catalog.set_config('search_path', '"$user", public', false); $$,
        $$ ALTER USER {{ .pg_user }} SET SEARCH_PATH TO 'public'; $$;

Once you save this configuration file, e.g. ``migration.load``, you can run the ``pgLoader`` with the following command:

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

Note that this migration guide only covers the tables for Mattermost products.

Another exclusion we are making is in the ``db_migrations`` table which has a small difference (a typo in a single migration name) creates a diff. Since we created the PostgreSQL schema with morph, and the official ``mattermost`` source, we can skip it safely without concerns. On the other hand, ``systems`` table may contain additional diffs if there were extra keys added during some of the migrations. Consider excluding the ``systems`` table if you run into issues, and perform a manual comparison as the data in the ``systems`` table is relatively smaller in size.

Plugin migrations
-----------------

On the plugin side, we are going to take a different approach from what we have done above. We are not going to use ``morph`` tool to create tables and indexes this time. We are going to utilize ``pgloader`` to create the tables on behalf of us. The reason for doing so is Boards and Playbooks are leveraging application logic to facilitate SQL queries. But we don't want to use any level of application at this point.

Playbooks
~~~~~~~~~

The ``pgloader`` configuration provided for Playbooks is based on ``v1.38.1`` and the plugin should be at least ``v1.36.0`` to perform migration.

Once we are ready to migrate, we can start migrating the **schema** and the **data**  by running ``pgLoader`` \*\*

\*\* Use the following configuration for the baseline of the data migration:

.. code::

   LOAD DATABASE
        FROM      mysql://{{ .mysql_user }}:{{ .mysql_password }}@mysql:3306/{{ .source_schema }}
        INTO      pgsql://{{ .pg_user }}:{{ .pg_password }}@postgres:5432/{{ .target_schema }}

   WITH include drop, create tables, create indexes, no foreign keys,
       workers = 8, concurrency = 1,
       multiple readers per thread, rows per range = 50000,
       preserve index names

   SET PostgreSQL PARAMETERS
       maintenance_work_mem to '128MB',
       work_mem to '12MB'

   SET MySQL PARAMETERS
       net_read_timeout  = '120',
       net_write_timeout = '120'

   CAST column IR_ChannelAction.ActionType to text drop typemod,
        column IR_ChannelAction.TriggerType to text drop typemod,
        column IR_Incident.ChecklistsJSON to "json" drop typemod

   INCLUDING ONLY TABLE NAMES MATCHING
       ~/IR_/

   BEFORE LOAD DO
       $$ ALTER SCHEMA public RENAME TO {{ .source_schema }}; $$

   AFTER LOAD DO
       $$ ALTER TABLE {{ .source_schema }}.IR_ChannelAction ALTER COLUMN ActionType TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_ChannelAction ALTER COLUMN TriggerType TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN ReminderMessageTemplate TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN ReminderMessageTemplate SET DEFAULT ''::text;  $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN ConcatenatedInvitedUserIDs TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN ConcatenatedInvitedUserIDs SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN ConcatenatedWebhookOnCreationURLs TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN ConcatenatedWebhookOnCreationURLs SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN ConcatenatedInvitedGroupIDs TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN ConcatenatedInvitedGroupIDs SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN Retrospective TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN Retrospective SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN MessageOnJoin TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN MessageOnJoin SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN ConcatenatedWebhookOnStatusUpdateURLs TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN ConcatenatedWebhookOnStatusUpdateURLs SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN CategoryName TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN CategoryName SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN ConcatenatedBroadcastChannelIds TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN ConcatenatedBroadcastChannelIds SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN ChannelIDToRootID TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Incident ALTER COLUMN ChannelIDToRootID SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN ReminderMessageTemplate TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN ReminderMessageTemplate SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN ConcatenatedInvitedUserIDs TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN ConcatenatedInvitedUserIDs SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN ConcatenatedWebhookOnCreationURLs TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN ConcatenatedWebhookOnCreationURLs SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN ConcatenatedInvitedGroupIDs TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN ConcatenatedInvitedGroupIDs SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN MessageOnJoin TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN MessageOnJoin SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN RetrospectiveTemplate TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN RetrospectiveTemplate SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN ConcatenatedWebhookOnStatusUpdateURLs TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN ConcatenatedWebhookOnStatusUpdateURLs SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN ConcatenatedSignalAnyKeywords TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN ConcatenatedSignalAnyKeywords SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN CategoryName TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN CategoryName SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN ChecklistsJSON TYPE JSON USING ChecklistsJSON::JSON; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN ConcatenatedBroadcastChannelIds TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN ConcatenatedBroadcastChannelIds SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN RunSummaryTemplate TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN RunSummaryTemplate SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN ChannelNameTemplate TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Playbook ALTER COLUMN ChannelNameTemplate SET DEFAULT ''::text; $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_PlaybookMember ALTER COLUMN Roles TYPE varchar(65536); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Category_Item ADD CONSTRAINT ir_category_item_categoryid FOREIGN KEY (CategoryId) REFERENCES {{ .source_schema }}.IR_Category(Id); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Metric ADD CONSTRAINT ir_metric_metricconfigid FOREIGN KEY (MetricConfigId) REFERENCES {{ .source_schema }}.IR_MetricConfig(Id); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Metric ADD CONSTRAINT ir_metric_incidentid FOREIGN KEY (IncidentId) REFERENCES {{ .source_schema }}.IR_Incident(Id); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_MetricConfig ADD CONSTRAINT ir_metricconfig_playbookid FOREIGN KEY (PlaybookId) REFERENCES {{ .source_schema }}.IR_Playbook(Id); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_PlaybookAutoFollow ADD CONSTRAINT ir_playbookautofollow_playbookid FOREIGN KEY (PlaybookId) REFERENCES {{ .source_schema }}.IR_Playbook(Id); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_PlaybookMember ADD CONSTRAINT ir_playbookmember_playbookid FOREIGN KEY (PlaybookId) REFERENCES {{ .source_schema }}.IR_Playbook(Id); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_Run_Participants ADD CONSTRAINT ir_run_participants_incidentid FOREIGN KEY (IncidentId) REFERENCES {{ .source_schema }}.IR_Incident(Id); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_StatusPosts ADD CONSTRAINT ir_statusposts_incidentid FOREIGN KEY (IncidentId) REFERENCES {{ .source_schema }}.IR_Incident(Id); $$,
       $$ ALTER TABLE {{ .source_schema }}.IR_TimelineEvent ADD CONSTRAINT ir_timelineevent_incidentid FOREIGN KEY (IncidentId) REFERENCES {{ .source_schema }}.IR_Incident(Id); $$,
       $$ CREATE UNIQUE INDEX IF NOT EXISTS ir_playbookmember_playbookid_memberid_key on {{ .source_schema }}.IR_PlaybookMember(PlaybookId,MemberId); $$,
       $$ CREATE INDEX IF NOT EXISTS ir_statusposts_incidentid_postid_key on {{ .source_schema }}.IR_StatusPosts(IncidentId,PostId); $$,
       $$ CREATE INDEX IF NOT EXISTS ir_playbookmember_playbookid on {{ .source_schema }}.IR_PlaybookMember(PlaybookId); $$,
       $$ ALTER SCHEMA {{ .source_schema }} RENAME TO public; $$,
       $$ SELECT pg_catalog.set_config('search_path', '"$user", public', false); $$,
       $$ ALTER USER {{ .pg_user }} SET SEARCH_PATH TO 'public'; $$;

.. code:: bash

   pgLoader playbooks.load > playbooks_migration.log

Focalboard
~~~~~~~~~~

As of ``v9.0`` Boards will transition to being fully community supported as the Focalboard plugin. Hence this guide covers only the version ``v7.10.x`` of the schema. `Official announcement <https://docs.mattermost.com/deploy/deprecated-features.html#mattermost-server-v9-0-0>`__.

Once we are ready to migrate, we can start migrating the **schema** and the **data**  by running ``pgLoader`` \*\*

\*\* Use the following configuration for the baseline of the data migration:

.. code::

   LOAD DATABASE
        FROM      mysql://{{ .mysql_user }}:{{ .mysql_password }}@mysql:3306/{{ .source_schema }}
        INTO      pgsql://{{ .pg_user }}:{{ .pg_password }}@postgres:5432/{{ .target_schema }}

   WITH include drop, create tables, create indexes, reset sequences,
       workers = 8, concurrency = 1,
       multiple readers per thread, rows per range = 50000,
       preserve index names

   SET PostgreSQL PARAMETERS
       maintenance_work_mem to '128MB',
       work_mem to '12MB'

   SET MySQL PARAMETERS
       net_read_timeout  = '120',
       net_write_timeout = '120'

   CAST column focalboard_blocks.fields to "json" drop typemod,
        column focalboard_blocks_history.fields to "json" drop typemod,
        column focalboard_schema_migrations.name to "varchar" drop typemod,
        column focalboard_sessions.props to "json" drop typemod,
        column focalboard_teams.settings to "json" drop typemod,
        column focalboard_users.props to "json" drop typemod,
        type int when (= precision 11) to int4 drop typemod,
        type json to jsonb drop typemod

   INCLUDING ONLY TABLE NAMES MATCHING
       ~/focalboard/

   BEFORE LOAD DO
       $$ ALTER SCHEMA public RENAME TO {{ .source_schema }}; $$

   AFTER LOAD DO
       $$ UPDATE {{ .source_schema }}.focalboard_blocks SET "fields" = '{}'::json WHERE "fields"::text = ''; $$,
       $$ UPDATE {{ .source_schema }}.focalboard_blocks_history SET "fields" = '{}'::json WHERE "fields"::text = ''; $$,
       $$ UPDATE {{ .source_schema }}.focalboard_sessions SET "props" = '{}'::json WHERE "props"::text = ''; $$, 
       $$ UPDATE {{ .source_schema }}.focalboard_teams SET "settings" = '{}'::json WHERE "settings"::text = ''; $$,
       $$ UPDATE {{ .source_schema }}.focalboard_users SET "props" = '{}'::json WHERE "props"::text = ''; $$, 
       $$ ALTER SCHEMA {{ .source_schema }} RENAME TO public; $$,
       $$ SELECT pg_catalog.set_config('search_path', '"$user", public', false); $$,
       $$ ALTER USER {{ .pg_user }} SET SEARCH_PATH TO 'public'; $$;

.. code:: bash

   pgLoader focalboard.load > focalboard_migration.log

Compare the plugin data
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

   dbcmp --source "${MYSQL_DSN}" --target "${POSTGRES_DSN}" --exclude="db_migrations,systems"
