Prepare your Mattermost MySQL database
======================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. contents:: On this page
  :backlinks: top
  :local:
  :depth: 1

.. important::
    
    PostgreSQL is our preferred database of choice. See the `database software </install/software-hardware-requirements.html#database-software>`__ documentation for details on database version support.

Set up the Mattermost MySQL database
------------------------------------

To set up a MySQL database for use by the Mattermost server:

1. Log into the server that will host the database, ands install MySQL.

2. Log in to MySQL as *root* by running ``sudo mysql``.

3. Create the Mattermost user *mmuser* by running ``mysql> create user 'mmuser'@'%' identified by 'mmuser-password';``. 

  - Use a password that is more secure than ``mmuser-password``.
  - The ``%`` means that ``mmuser`` can connect from any machine on the network. However, it's more secure to use the IP address of the machine that hosts Mattermost. For example, if you install Mattermost on the machine with IP address ``10.10.10.2``, then use the following command: ``mysql> create user 'mmuser'@'10.10.10.2' identified by 'mmuser-password';``

4. Create the Mattermost database by running ``mysql> create database mattermost;``.

5. Grant access privileges to the user ``mmuser`` by running ``mysql> grant all privileges on mattermost.* to 'mmuser'@'%';``.

  .. note::
      
    This query grants the MySQL user we just created all privileges on the database for convenience. If you need more security, use the following query to grant the user only the privileges necessary to run Mattermost: ``mysql> GRANT ALTER, CREATE, DELETE, DROP, INDEX, INSERT, SELECT, UPDATE, REFERENCES ON mattermost.* TO 'mmuser'@'%';``

6. Log out of MySQL by running ``mysql> exit``. Once the database is installed and the initial setup is complete, you can install the Mattermost server.\

.. note::

  If you have installed MySQL on its own server, edit the ``/etc/mysql/mysql.conf.d/mysqld.cnf`` file and comment out the ``bind-address = 127.0.0.1`` using the ``#`` symbol, then restart your database server.

Back up the database
--------------------

Back up your Mattermost database using standard procedures depending on your database version. `MySQL backup documentation <https://dev.mysql.com/doc/refman/5.6/en/backup-types.html>`__ is available online. Use the selector on the page to choose your MySQL version.

Upgrade Mattermost
-------------------

.. tabs::

    .. tab:: Upgrade to v7.1

        Mattermost v7.1 introduces schema changes in the form of a new column and its index. Our test results for the schema changes include: 12M Posts, 2.5M Reactions - ~1min 34s (instance: PC with 8 cores, 16GB RAM).

        You can run the following SQL queries before the upgrade that obtains a lock on ``Reactions`` table. 

        ``ALTER TABLE Reactions ADD COLUMN ChannelId varchar(26) NOT NULL DEFAULT "";``

        ``UPDATE Reactions SET ChannelId = COALESCE((select ChannelId from Posts where Posts.Id = Reactions.PostId), '') WHERE ChannelId="";``

        ``CREATE INDEX idx_reactions_channel_id ON Reactions(ChannelId) LOCK=NONE;``

        Users' reactions posted during this time won't be reflected in the database until the migrations are complete. This is fully backwards-compatible.

        If your connection collation and table collations are different, this can result in the error `Illegal mix of collations`. To resolve this error, set the same collation for both the connection and the table. There are different collations at different levels - connection, database, table, column, and database administrators may choose to set different collation levels for different objects.

    .. tab:: Upgrade to v7.0

        Self-hosted Mattermost customers using MySQL databases may notice the migration to release v7.0 taking longer than usual when there are a large number of rows in the ``FileInfo`` table. See the `important upgrade notes </upgrade/important-upgrade-notes.html>`__ documentation for details.

    .. tab:: Upgrade to v6.7

        Mattermost v6.7 introduces schema changes in the form of a new index. The following notes our test results for the schema changes:

        - 7M Posts - ~17s (instance: db.r5.xlarge)
        - 9M Posts - 2min 12s (instance: db.r5.large)

        If you want a zero downtime upgrade, you can apply this index prior to doing the upgrade:

        ``CREATE INDEX idx_posts_create_at_id on Posts(CreateAt, Id) LOCK=NONE;``

        This is fully backwards-compatible and will not acquire any table lock or affect any existing operations on the table.

    .. tab:: v6.0 database schema migrations

        The release of v6.0 introduces database schema changes and longer migration times should be expected, especially on MySQL installations. 

        Mattermost v6.0 introduces several database schema changes to improve both database and application performance. The upgrade will run significant database schema changes that can cause an extended startup time depending on the dataset size. We've conducted extensive tests on supported MySQL database drivers, using realistic datasets of more than 10 million posts and more than 72 million posts.

        A migration to v6.0 of 10+ million posts will take approximately 1 hour and 22 minutes to complete for a MySQL database. See the `Mattermost v6.0 DB schema migrations analysis <https://gist.github.com/streamer45/59b3582118913d4fc5e8ff81ea78b055>`__ documentation for test specifications, data sizes, and test results.

        A large migration from v5.39 to v6.0 of 72+ million posts will take approximately 3 hours and 40 minutes to complete for a MySQL database. See the `Migration results analysis <https://gist.github.com/streamer45/868c451164f6e8069d8b398685a31b6e>`__ documentation for test specifications, data sizes, and test results.

        The following queries, executed during the migration process on an environment with 10+ million posts, will have a significant impact on database CPU usage and write operation restrictions for the duration of the query:

        ``ALTER TABLE Posts MODIFY Props JSON;`` (~26 minutes)

        ``ALTER TABLE Posts DROP COLUMN ParentId;`` (~26 minutes)

        ``ALTER TABLE Posts MODIFY COLUMN FileIds text;`` (~26 minutes)

        For a complete breakdown of MySQL queries, as well as their impact and duration, see the `Mattermost v6.0 DB schema migrations analysis <https://gist.github.com/streamer45/59b3582118913d4fc5e8ff81ea78b055#mysql-1>`__ documentation.

        **MySQL Mitigation Strategies**

        Run combined queries prior to the upgrade. The previous queries can be combined when run prior to the upgrade as follows:

        ``ALTER TABLE Posts MODIFY COLUMN FileIds text, MODIFY COLUMN Props JSON;``

        This limits the time taken to that of a single query of that type.

        **Online migration**: An online migration that avoids locking can be attempted on MySQL installations, especially for particularly heavy queries or very big datasets (tens of millions of posts or more). This can be done through an external tool like `pt-online-schema-change <https://www.percona.com/doc/percona-toolkit/LATEST/pt-online-schema-change.html>`__. However, the online migration process can cause a significant spike in CPU usage on the database instance it runs.

        See the `Mattermost v6.0 DB schema migrations analysis <https://gist.github.com/streamer45/59b3582118913d4fc5e8ff81ea78b055#online-migration-mysql>`__ documentation for a sample execution and additional caveats.

High availabiilty configuration setting recommendations 
--------------------------------------------------------

For MySQL, we recommend the following configuration options for high performance:

- ``innodb_buffer_pool_size``: Set to ~70% of your total RAM.
- ``innodb_log_file_size``: Set to 256 MB. Increasing this helps in write intensive operations. Recovery times will be longer.
- ``innodb_flush_log_at_trx_commit``: 2. This can potentially cause up to one second of loss of transaction data.
- ``max_heap_table_size``: 64 MB.
- ``tmp_table_size``: 64 MB.

Encryption-at-rest
------------------

Encryption-at-rest is available for messages via hardware and software disk encryption solutions applied to the Mattermost database, which resides on its own server within your infrastructure. See the `MySQL <https://www.percona.com/blog/2016/04/08/mysql-data-at-rest-encryption/>`__ database documentation for details on encryption options at the disk level.

Use sockets for the database
----------------------------

.. code-block:: bash

    $ mysql -u root -p
    CREATE DATABASE mattermostdb;
    CREATE USER mmuser IDENTIFIED BY 'mmuser_password';
    GRANT ALL ON mattermostdb.* TO mmuser;

Mattermost is configured in ``/etc/webapps/mattermost/config.json``, and strings need to be quoted.

- set ``DriverName`` to ``mysql``.
- set ``DataSource`` to ``mmuser:mmuser_password@unix(/run/mysqld/mysqld.sock)/mattermostdb?charset=utf8mb4,utf8``.

Mattermost configuration in the database
----------------------------------------

You can use the database as the single source of truth for the active configuration of your Mattermost installation. This changes the Mattermost binary from reading the default ``config.json`` file to reading the configuration settings stored within a configuration table in the database.

.. code-block:: text

   mysql://mmuser:really_secure_password@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8&writeTimeout=30s

Create an environment file
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

   If you're running Mattermost in a High Availability cluster, this step must be done on all servers in the cluster.

Create the file ``/opt/mattermost/config/mattermost.environment`` to set the ``MM_CONFIG`` environment variable to the database connection string. For example:

.. code-block:: text

   MM_CONFIG='mysql://mmuser:mostest@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8&writeTimeout=30s'

.. note::
  
  Be sure to escape any single quotes in the database connection string by placing a ``\`` in front of them like this ``\'``. For example: ``MM_CONFIG='mysql://mmuser:it\'s-a-password!@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8&writeTimeout=30s'``

.. code-block:: text

   MM_CONFIG='mysql://mmuser:it\'s-a-password!@tcp(127.0.0.1:3306)/mattermost?charset=utf8mb4,utf8&writeTimeout=30s'

Finally, run this command to verify the permissions on your Mattermost directory:

.. code-block:: bash

   sudo chown -R mattermost:mattermost /opt/mattermost

Modify the Mattermost ``systemd`` file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, find the ``mattermost.service`` file using:

.. code-block:: bash

   sudo systemctl status mattermost.service

The second line of output will have the location of the running ``mattermost.service``.

.. code-block:: text

    Loaded: loaded (/lib/systemd/system/mattermost.service; enabled; vendor preset: enabled)

Edit this file as *root* to add the below text just above the line that begins with ``ExecStart``\ :

.. code-block:: text

   EnvironmentFile=/opt/mattermost/config/mattermost.environment

Here's a complete ``mattermost.service`` file with the ``EnvironmentFile`` line added:

.. code-block:: text

   [Unit]
   Description=Mattermost
   After=network.target
   After=mysql.service
   Requires=mysql.service

   [Service]
   Type=notify
   EnvironmentFile=/opt/mattermost/config/mattermost.environment
   ExecStart=/opt/mattermost/bin/mattermost
   TimeoutStartSec=3600
   KillMode=mixed
   Restart=always
   RestartSec=10
   WorkingDirectory=/opt/mattermost
   User=mattermost
   Group=mattermost
   LimitNOFILE=49152

   [Install]
   WantedBy=mysql.service

Technical notes about searching
-------------------------------

By default, Mattermost uses full text search support included in MySQL. Select the **product menu** |product-list| then select **About Mattermost** to see which database you’re using.

- Stop words are filtered out of search results. See `MySQL <https://dev.mysql.com/doc/refman/5.7/en/fulltext-stopwords.html>`__ database documentation for a full list of applicable stop words.
- Hashtags or recent mentions of usernames containing a dot don't return results.
- Avoid using underline ``_`` symbol to `perform a wildcard search <#wildcards>`__. Use the asterisk ``*`` symbol instead.
- Stop words that are excluded from search in MySQL include: ``"a", "about", "an", "are", "as", "at", "be", "by", "com", "de", "en", "for", "from", "how", "i", "in", "is", "it", "la", "of", "on", "or", "that", "the", "this", "to", "was", "what", "when", "where", "who", "will", "with", "und", "the", "www"``.

Perform searches in Chinese, Korean, and Japanese
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The best experience for searching in Chinese, Korean, and Japanese is to use MySQL 5.7.6 or later with special configuration. See the `Chinese, Japanese and Korean Search documentation </install/i18n.html>`__ for details.

You can perform searches without this configuration by adding wildcards ``*`` to the end of search terms.

Migrate from Bitnami to a self-hosted Mattermost deployment
------------------------------------------------------------

If you're planning a migration from Bitnami to a self-hosted Mattermost installation with a MySQL database, read these notes in our migration guide: `Migrating from Bitnami </onboard/migrating-to-mattermost.html#migrating-from-bitnami>`__.



Downgrade Mattermost v6.0 to v5.38
-----------------------------------

.. code-block:: sh
    
    INSERT INTO Systems (Name,Value) VALUES ('Version','5.38.0') ON DUPLICATE KEY UPDATE Value = '5.38.0';

    CREATE INDEX idx_status_status ON Status (Status);
    DROP INDEX idx_status_status_dndendtime ON Status;
    CREATE INDEX idx_channelmembers_user_id ON ChannelMembers (UserId);
    DROP INDEX idx_channelmembers_channel_id_scheme_guest_user_id ON ChannelMembers;
    DROP INDEX idx_channelmembers_user_id_channel_id_last_viewed_at ON ChannelMembers;
    CREATE INDEX idx_threads_channel_id ON Threads (ChannelId);
    DROP INDEX idx_threads_channel_id_last_reply_at ON Threads;
    CREATE INDEX idx_channels_team_id ON Channels (TeamId);
    DROP INDEX idx_channels_team_id_type ON Channels;
    DROP INDEX idx_channels_team_id_display_name ON Channels;
    CREATE INDEX idx_posts_root_id ON Posts (RootId);
    DROP INDEX idx_posts_root_id_delete_at ON Posts;

    ALTER TABLE CommandWebhooks ADD COLUMN ParentId varchar(26);
    UPDATE CommandWebhooks SET ParentId = '';
    ALTER TABLE Posts ADD COLUMN ParentId varchar(26);
    UPDATE Posts SET ParentId = '';

    ALTER TABLE Users MODIFY Timezone text;
    ALTER TABLE Users MODIFY NotifyProps text;
    ALTER TABLE Users MODIFY Props text;
    ALTER TABLE Threads MODIFY Participants longtext;
    ALTER TABLE Sessions MODIFY Props text;
    ALTER TABLE Posts MODIFY Props text;
    ALTER TABLE Jobs MODIFY Data text;
    ALTER TABLE LinkMetadata MODIFY Data text;
    ALTER TABLE ChannelMembers MODIFY NotifyProps text;

.. note:: 
      
    The inverse of `the final v6.0 upgrade query <https://gist.github.com/streamer45/59b3582118913d4fc5e8ff81ea78b055#mysql-1>`__ is intentionally omitted from these downgrade queries because its result is backwards compatible, and running the query would unnecessarily delay the downgrade process.
