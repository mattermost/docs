Migration guidelines from MySQL to PostgreSQL
=============================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

From Mattermost v8.0, PostgreSQL is our database of choice for Mattermost to enhance the platform’s performance and capabilities. Recognizing the importance of supporting the community members who are interested in migrating from a MySQL database, we have taken proactive measures to provide guidance and best practices. 

To streamline the migration process and alleviate any potential challenges, we have prepared a comprehensive set of guidelines to facilitate a smooth transition. Additionally, we want to offer recommendations for various tools that have proven to be highly effective in simplifying your migration efforts.

.. note::

   These guidelines are in development and we are working to streamline the migration process. We plan to improve this guide by updating it as new information becomes available. Please use this guide as a starting point and always backup your database before starting a migration.

Required tools
--------------

- Install ``pgLoader``. See the official `installation guide <https://pgloader.readthedocs.io/en/latest/install.html>`__.

.. note::

   - If you are using MySQL v8: Due to a `known bug <https://github.com/dimitri/pgloader/issues/1183>`__ in pgLoader compiled binaries, you need to compile pgLoader from the source. Please follow the steps `here <https://pgloader.readthedocs.io/en/latest/install.html#build-from-sources>`__ to build from the source.
   - We have received reports that the pgloader Docker image can be limited in terms of memory resources. Please use pgloader directly instead of a Docker container. 

- Install morph CLI by running the following command:

 - ``go install github.com/mattermost/morph/cmd/morph@v1``

- Optionally install ``dbcmp`` to compare the data after a migration:

 - ``go install github.com/mattermost/dbcmp/cmd/dbcmp@latest``

Before the migration
--------------------

.. important::

   This guide requires a schema of v6.4 or later. So, if you have an earlier version and planning to migrate, please update your Mattermost Server to v6.4 at a minimum.

   - Back up your MySQL data.
   - Confirm your Mattermost version. See the **About** modal for details. 
   - Determine the migration window needed. This process requires you to stop the Mattermost Server during the migration.
   - See the `schema-diffs <#schema-diffs>`__ section to ensure data compatibility between schemas.
   - Prepare your PostgreSQL environment by creating a database and user. See the `database </install/prepare-mattermost-database.html>`__ documentation for details.
   - If you are planning to run an iterative migration (running the pgloader several times), please see the `iterative-migrations <#iterative-migrations>`_ section.
   - On `newer versions <https://www.postgresql.org/docs/release/15.0/>`__ of PostgreSQL, newly created users do not have access to ``public`` schema. The access should be explicitly granted by running ``GRANT ALL ON SCHEMA public to mmuser'``.

Prepare target database
-----------------------

- Clone the ``mattermost`` repository for your specific version:
   ``git clone -b <your current version (eg. release-7.8)> git@github.com:mattermost/mattermost.git --depth=1``
- ``cd`` into ``mattermost`` project*.
- Create a PostgreSQL database using morph CLI with the following command:

.. code:: bash

   morph apply up --driver postgres --dsn "postgres://user:pass@localhost:5432/<target_db_mame>?sslmode=disable" --path ./db/migrations/postgres --number -1

\* After ``v8``, due to project re-organization, the migrations directory has been changed to ``./server/channels/db/migrations/postgres/`` relative to the project root. Therefore ``cd`` into ``mattermost/server/channels``.

Schema diffs
------------

Before the migration, due to differences between the two schemas, some manual steps may be required for an error-free migration.

Text to character varying
~~~~~~~~~~~~~~~~~~~~~~~~~

We encourage you to check if the sizes are consistent within the PostgreSQL schema limits since the Mattermost MySQL schema uses the ``text`` column type in the various tables instead of ``varchar`` representation in the PostgreSQL schema.

You can check if there are any required deletions or updates. For example, to do so in the ``Audits`` table/``Action`` column; run:

.. code:: sql

   SELECT FROM mattermost.Audits where LENGTH(Action) > 512;

The following table shows the deletions or updates you can proceed with that don't incur further consequences. 

================ ================ ===================== =============================================================================
Table            Column           Data type casting     Consequence on deletion
================ ================ ===================== =============================================================================
Audits           Action           text -> varchar(512)  No side effect on how the application works (The affected row needs to be deleted).
Audits           ExtraInfo        text -> varchar(1024) No side effect on how the application works (The affected row needs to be deleted).
ClusterDiscovery HostName         text -> varchar(512)  No side effect on how the application works (The affected row needs to be deleted).
Commands         IconURL          text -> varchar(1024) The field can be deleted or updated with a new URL.
Commands         AutoCompleteDesc text -> varchar(1024) The field can be deleted or rewritten.
Commands         AutoCompleteHint text -> varchar(1024) The field can be deleted or rewritten.
RemoteClusters   Topics           text -> varchar(512)  The field can be removed.
Systems          Value            text -> varchar(1024) Edge case, ideally should never happen.
================ ================ ===================== =============================================================================

The following table shows several occurrences where the schema can differ and data size constraints within the PostgreSQL schema can result in errors. Each table/row requires individual inspection hence we added the possible consequence of deletion.

.. tip::

   Several reports have been received from our community that the ``LinkMetadata`` and ``FileInfo`` tables had some overflows, so we recommend checking these tables in particular. Please check if your data in the MySQL schema exceeds these limitations. 

================ ================ ===================== =============================================================================
Table            Column           Data type casting     Consequence on deletion
================ ================ ===================== =============================================================================
Compliances      Keywords         text -> varchar(512)  The filter for compliance needs to be updated.
Compliances      Emails           text -> varchar(1024) The filter for compliance needs to be updated.
FileInfo         Path             text -> varchar(512)  Previous links to this file won't work (The affected row needs to be deleted).
FileInfo         ThumbnailPath    text -> varchar(512)  Previous links to this file won't work (The affected row needs to be deleted).
FileInfo         PreviewPath      text -> varchar(512)  Previous links to this file won't work (The affected row needs to be deleted).
FileInfo         Name             text -> varchar(256)  Previous links to this file won't work (The affected row needs to be deleted).
FileInfo         MimeType         text -> varchar(256)  Previous links to this file won't work (The affected row needs to be deleted).
LinkMetadata     URL              text -> varchar(2048) Previous links to this file won't work (The affected row needs to be deleted).
RemoteClusters   SiteURL          text -> varchar(512)  Previous remote cluster will be removed (The affected row needs to be deleted).
Sessions         DeviceId         text -> varchar(512)  Users will be logged out on these devices (The affected row needs to be deleted).
UploadSessions   FileName         text -> varchar(256)  The upload session will be lost (The affected row needs to be deleted).
UploadSessions   Path             text -> varchar(512)  The upload session will be lost (The affected row needs to be deleted).
================ ================ ===================== =============================================================================

Full-text indexes
~~~~~~~~~~~~~~~~~

It's possible that some words in the ``Posts`` and ``FileInfo`` tables can exceed the `limits of the maximum token length <https://www.postgresql.org/docs/11/textsearch-limitations.html>`__ for full-text search indexing. In these cases, we are dropping the ``idx_posts_message_txt`` and ``idx_fileinfo_content_txt`` indexes from the PostgreSQL schema, and creating these indexes after the migration by running the following queries:

Although these statements are included in the script, we recommend running these manually to prevent errors:

.. code:: sql

   DROP INDEX IF EXISTS idx_posts_message_txt;
   DROP INDEX IF EXISTS idx_fileinfo_content_txt;

The following queries are added to the script to re-create these indexes after migration finishes:

.. code:: sql

   CREATE INDEX IF NOT EXISTS idx_posts_message_txt ON {{ .source_schema }}.posts USING gin(to_tsvector('english', message));
   CREATE INDEX IF NOT EXISTS idx_fileinfo_content_txt ON {{ .source_schema }}.fileinfo USING gin(to_tsvector('english', content));

.. note::
   If any of the entries in your  ``Posts`` and ``FileInfo`` tables exceed the limit, ``pgloader`` will fail with the ``ERROR:  string is too long for tsvector`` error while trying to create these indexes. You should manually remove these indexes.

Artifacts may remain from previous configurations/versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prior to ``v6.4``, Mattermost was using `golang-migrate <https://github.com/golang-migrate/migrate>`__ to handle the schema migrations. Since we don't use it anymore, we exclude the table ``schema_migrations``. If you were using Mattermost before ``v6.4`` consider dropping this table and excluding it from comparison as well.

.. code:: sql

   DROP TABLE mattermost.schema_migrations;

Also, if you were previously utilizing a database for handling the `Mattermost configuration <https://docs.mattermost.com/configure/configuration-in-your-database.html>`__, those tables will not be migrated from your MySQL database with the migration `script <#migrate-the-data>`__. Please use ``mmctl config migrate`` tooling to `migrate your config <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-config-migrate>`__ to the target database. After migrating the config, we should also update the ``SqlSettings.DataSource`` and ``SqlSettings.DriverName`` fields to reflect new changes. To do so, in the Postgres database we should update the active configuration row:

.. code:: sql

   SELECT * FROM Configurations WHERE Active = 't';

You should update the ``SqlSettings.DataSource`` and ``SqlSettings.DriverName`` fields accordingly. Also, note that the ``MM_CONFIG`` environment variable should point to the new DSN after the migration is completed.

Some community members have reported that they had ``description`` and ``nextsyncat`` columns in their ``SharedChannelRemotes`` table. These columns should be removed from the table. Consider running the following DDL to drop the columns. (This migration will be added to future versions of Mattermost).

.. code:: sql

   ALTER TABLE SharedChannelRemotes DROP COLUMN description, DROP COLUMN nextsyncat;

An error has been identified in the 96th migration that was previously released. Before proceeding with the migration, it is necessary to remove a specific column. To ensure the Threads table reaches the expected state, execute the following prepared statement:

.. code:: sql

   SET @preparedStatement = (SELECT IF(
    (
        SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS
        WHERE table_name = 'Threads'
        AND table_schema = DATABASE()
        AND column_name = 'TeamId'
    ) > 0,
    'ALTER TABLE Threads DROP COLUMN TeamId;',
    'SELECT 1'
   ));

   PREPARE alterIfExists FROM @preparedStatement;
   EXECUTE alterIfExists;
   DEALLOCATE PREPARE alterIfExists;

Migrate the data
----------------

Once we set the schema to a desired state, we can start migrating the **data** by running ``pgLoader`` \*\*

.. note::

   In the example below, the hosts for both databases are assumed to be in the same instance. Please update addresses accordingly if they are on different machines.

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

   EXCLUDING TABLE NAMES MATCHING ~<IR_>, ~<focalboard>, 'schema_migrations'

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

We internally developed a tool to simplify the process of comparing the contents of two databases. The ``dbcmp`` tool compares every table and reports whether there is a diversion between two schemas.

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

For our case, we can simply run the following command:

.. code:: sh

   dbcmp --source "${MYSQL_DSN}" --target "${POSTGRES_DSN}" --exclude="db_migrations,ir_,focalboard,systems"

Note that this migration guide only covers the tables for Mattermost products.

Another exclusion we are making is in the ``db_migrations`` table which has a small difference (a typo in a single migration name) and creates a diff. Since we created the PostgreSQL schema with morph, and the official ``mattermost`` source, we can skip it safely without concerns. On the other hand, ``systems`` table may contain additional diffs if there were extra keys added during some of the migrations. Consider excluding the ``systems`` table if you run into issues, and perform a manual comparison as the data in the ``systems`` table is relatively smaller in size.

Plugin migrations
-----------------

On the plugin side, we are going to take a different approach from what we have done above. We are not going to use ``morph`` tool to create tables and indexes this time. We are going to utilize ``pgloader`` to create the tables on behalf of us. The reason for doing so is Boards and Playbooks are leveraging application logic to facilitate SQL queries. But we don't want to use any level of application at this point.

Playbooks
~~~~~~~~~

The ``pgloader`` configuration provided for Playbooks is based on ``v1.38.1`` and the plugin should be at least ``v1.36.0`` to perform the migration.

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

As of ``v9.0`` Boards will transition to being fully community supported as the Focalboard plugin. Hence this guide covers only the version ``v7.10.x`` of the schema. :ref:`Official announcement <deploy/deprecated-features:mattermost server v9.0.0>`.

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

Iterative migrations
--------------------

Several steps in the pgloader configuration file assume migration will take place in one go. If you are planning to run the migration over and over again, please complete the changes defined below:

-  Discard all of the statements defined in the ``BEFORE LOAD DO`` and ``AFTER LOAD DO`` sections.
-  Run the statements defined in ``BEFORE LOAD DO`` section only once before the migration.
-  Once the migration is completed, run the statements defined in the ``AFTER LOAD DO`` section manually.

Troubleshooting
-----------------

Unsupported authentication for MySQL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are facing an error due to authentication with MySQL v8, it may be related to a `known issue <https://github.com/dimitri/pgloader/issues/782>`__ with the pgLoader. The fix is to set the default authentication method to ``mysql_native_password`` in your MySQL configuration. To do so, add the ``default-authentication-plugin=mysql_native_password`` value to your ``mysql.cnf`` file. Also, do not forget to update your user to use this authentication method.

.. code:: sql

   ALTER USER '<mysql_user>'@'%' IDENTIFIED WITH mysql_native_password BY '<mysql_password>';
