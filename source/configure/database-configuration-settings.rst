:orphan:
:nosearch:

Configure the database environment in which Mattermost is deployed by going to **System Console > Environment > Database**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

Driver name
~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The type of database. Can be either:                          | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``".SqlSettings.DriverName",``                |
| - **mysql**: **(Default)** Enables driver to MySQL database.  | - Environment variable: ``MM_SQLSETTINGS_DRIVERNAME``                    |
| - **postgres**: Enables driver to PostgreSQL database.        |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Data source
~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The connection string to the master database.                 | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``".SqlSettings.DataSource",``                |
| String input.                                                 | - Environment variable: ``MM_SQLSETTINGS_DATASOURCE``                    |
|                                                               |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| To enable SSL:                                                                                                                           |
|                                                                                                                                          |
| - Add ``&tls=true`` to your database connection string if your SQL driver supports it.                                                   |   
| - Add ``&tls=skip-verify`` if you use self-signed certificates.                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **MySQL databases**                                                                                                                      |
|                                                                                                                                          |
| When **Driver Name** is set to ``mysql``, using ``collation`` is recommended over using ``charset``.                                     |
|                                                                                                                                          |
| To specify collation:                                                                                                                    |
|                                                                                                                                          |
| .. code-block:: none                                                                                                                     |
|                                                                                                                                          |
|   "SqlSettings": {                                                                                                                       |
|       "DataSource":                                                                                                                      |
|   "<user:pass>@<servername>/mattermost?charset=utf8mb4,utf8&collation=utf8mb4_general_ci",                                               |
|       [...]                                                                                                                              |
|    }                                                                                                                                     |
|                                                                                                                                          |
| If collation is omitted, the default collation, ``utf8mb4_general_ci`` is used:                                                          |
|                                                                                                                                          |
| .. code-block:: none                                                                                                                     |
|                                                                                                                                          |
|   "SqlSettings": {                                                                                                                       |
|       "DataSource": "<user:pass>@<servername>/mattermost?charset=utf8mb4,utf8",                                                          |
|       [...]                                                                                                                              |
|    }                                                                                                                                     |
|                                                                                                                                          |
| **Note**: If you’re using MySQL 8.0 or later, the default collation has changed to ``utf8mb4_0900_ai_ci``. See our `Database Software    |
| Requirements </install/software-hardware-requirements.html>`__ documentation for details on MySQL 8.0 support.                           |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **PostgreSQL databases**                                                                                                                 |
|                                                                                                                                          |
| When **Driver Name** is set to ``postgres``, use a connection string in the form of:                                                     |
| ``postgres://mmuser:password@localhost:5432/mattermost_test?sslmode=disable&connect_timeout=10.``                                        |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Maximum idle database connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+--------------------------------------------------------+------------------------------------------------------------------+
| The maximum number of idle connections held open       | - System Config path: **Environment > Database**                 |
| to the database.                                       | - ``config.json`` setting: ``".SqlSettings.MaxIdleConns": 10,``  |
|                                                        | - Environment variable: ``MM_SQLSETTINGS_MAXIDLECONNS``          |
| Numerical input. Default is **10**.                    |                                                                  |
+--------------------------------------------------------+------------------------------------------------------------------+

Maximum open connections
~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+--------------------------------------------------------+------------------------------------------------------------------+
| The maximum number of idle connections held open       | - System Config path: **Environment > Database**                 |
| to the database.                                       | - ``config.json`` setting: ``".SqlSettings.MaxOpenConns": 300,`` |
|                                                        | - Environment variable: ``MM_SQLSETTINGS_MAXOPENCONNS``          |
| Numerical input. Default is **300**.                   |                                                                  |
+--------------------------------------------------------+------------------------------------------------------------------+

Query timeout
~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+--------------------------------------------------------+------------------------------------------------------------------+
| The amount of time to wait, in seconds, for a response | - System Config path: **Environment > Database**                 |
| from the database after opening a connection and       | - ``config.json`` setting: ``".SqlSettings.QueryTimeout: 30",``  |
| sending the query.                                     | - Environment variable: ``MM_SQLSETTINGS_QUERYTIMEOUT``          |
|                                                        |                                                                  |
| Numerical input in seconds. Default is **30** seconds. |                                                                  |
+--------------------------------------------------------+------------------------------------------------------------------+

Maximum connection lifetime
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+--------------------------------------------------------+-------------------------------------------------------------------------------------+
| Maximum lifetime for a connection to the database,     | - System Config path: **Environment > Database**                                    |
| in milliseconds. Use this setting to configure the     | - ``config.json`` setting: ``".SqlSettings.ConnMaxLifetimeMilliseconds: 3600000",`` |
| maximum amount of time a connection to the database    | - Environment variable: ``MM_SQLSETTINGS_CONNMAXLIFETIMEMILLISECONDS``              |
| may be reused                                          |                                                                                     |
|                                                        |                                                                                     |
| Numerical input in milliseconds. Default is            |                                                                                     |
| **3,600,000** milliseconds (1 hour).                   |                                                                                     |
+--------------------------------------------------------+-------------------------------------------------------------------------------------+

Maximum connection idle timeout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+--------------------------------------------------------+-------------------------------------------------------------------------------------+
| Maximum time a database connection can remain idle,    | - System Config path: **Environment > Database**                                    |
| in milliseconds.                                       | - ``config.json`` setting: ``".SqlSettings.ConnMaxIdleTimeMilliseconds: 300000",``  |
|                                                        | - Environment variable: ``MM_SQLSETTINGS_CONNMAXIDLETIMEMILLISECONDS``              |
| Numerical input in milliseconds. Default is **300000** |                                                                                     | 
| (5 minutes).                                           |                                                                                     |
+--------------------------------------------------------+-------------------------------------------------------------------------------------+

Minimum hashtag length
~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+----------------------------------------------------------------------+-------------------------------------------------------------------------+
| Minimum number of characters in a hashtag.                           | - System Config path: **Environment > Database**                        |
| This value must be greater than or equal to **2**.                   | - ``config.json`` setting: ``".SqlSettings.MinimumHashtagLength: 3",``  |
|                                                                      | - Environment variable: ``MM_SQLSETTINGS_MINIMUMHASHTAGLENGTH``         |
+----------------------------------------------------------------------+-------------------------------------------------------------------------+
| **Note**: MySQL databases must be configured to support searching strings shorter than three characters. See the                               |
| `MySQL documentation <https://dev.mysql.com/doc/refman/8.0/en/fulltext-fine-tuning.html>`__ for details.                                       |
+----------------------------------------------------------------------+-------------------------------------------------------------------------+

SQL statement logging
~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Executed SQL statements can be written to the log for         | - System Config path: **Environment > Database**                         |
| development.                                                  | - ``config.json`` setting: ``".SqlSettings.Trace: false",``              |
|                                                               | - Environment variable: ``MM_SQLSETTINGS_TRACE``                         |
| - **true**: Executing SQL statements are written to the log.  |                                                                          |
| - **false**: **(Default)** SQL statements aren't written      |                                                                          |
|   to the log.                                                 |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Recycle database connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

+--------------------------------------------------------+------------------------------------------------------------------+
| Select the **Recycle Database Connections** button to  | - System Config path: **Environment > Database**                 |
| reconnect to the configured database.                  | - ``config.json`` setting: N/A                                   |
| All old connections are closed after 20 seconds.       | - Environment variable: N/A                                      |
|                                                        |                                                                  |
| To fail over without downing the server, change the    |                                                                  |
| database line in the ``config.json`` file, select      |                                                                  |
| **Reload Configuration from Disk** via **Environment   |                                                                  |
| > Web Server**, then select **Recycle Database         |                                                                  |
| Connections**.                                         |                                                                  |
+--------------------------------------------------------+------------------------------------------------------------------+

Disable database search
~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+------------------------------------------------------------------------------+
| When other search engines are configured, such as             | - System Config path: **Environment > Database**                             |
| `Elasticsearch                                                | - ``config.json`` setting: ``".SqlSettings.DisableDatabaseSearch: false",``  |
| </scale/elasticsearch.html>`__,                               | - Environment variable: ``MM_SQLSETTINGS_DISABLEDATABASESEARCH``             |
| the database can be disabled to perform searches.             |                                                                              |
|                                                               |                                                                              |
| - **true**: Disables the use of the database to perform       |                                                                              |
|   searches. If another search engine isn't configured,        |                                                                              |
|   setting this value to ``true`` will result in empty search  |                                                                              |
|   results.                                                    |                                                                              |
| - **false**: **(Default)** Database search isn't disabled.    |                                                                              |
+---------------------------------------------------------------+------------------------------------------------------------------------------+

Applied schema migrations
~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

A list of all migrations that have been applied to the data store based on the version information available in the ``db_migrations`` table. Select **About Mattermost** from the product menu to review the current database schema version applied to your deployment.

Read replicas
~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20*

+--------------------------------------------------------+-----------------------------------------------------------------------+
| Specifies the connection strings for the read replica  | - System Config path: N/A                                             |
| databases.                                             | - ``config.json`` setting: ``".SqlSettings.DataSourceReplicas": []``  |
|                                                        | - Environment variable: ``MM_SQLSETTINGS_DATASOURCEREPLICAS``         |
+--------------------------------------------------------+-----------------------------------------------------------------------+
| **Note**: Each database connection string in the array must be in the same form used for the                                   |
| `Data source <#data-source>`__ setting.                                                                                        |
+--------------------------------------------------------+-----------------------------------------------------------------------+

Search replicas
~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10 and E20*

+--------------------------------------------------------+-----------------------------------------------------------------------------+
| Specifies the connection strings for the search        | - System Config path: N/A                                                   |
| replica databases. A search replica is similar to a    | - ``config.json`` setting: ``".SqlSettings.DataSourceSearchReplicas": []``  |
| read replica, but is used only for handling search     | - Environment variable: ``MM_SQLSETTINGS_DATASOURCESEARCHREPLICAS``         |
| queries.                                               |                                                                             |
+--------------------------------------------------------+-----------------------------------------------------------------------------+
| **Note**: Each database connection string in the array must be in the same form used for the `Data source <#data-source>`__          |
| setting.                                                                                                                             |
+--------------------------------------------------------+-----------------------------------------------------------------------------+

Replica lag settings
~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

+--------------------------------------------------------+----------------------------------------------------------------------------------+
| String array input specifies a connection string and   | - System Config path: N/A                                                        |
| user-defined SQL queries on the database to measure    | - ``config.json`` setting: ``".SqlSettings.ReplicaLagSettings": []``             |
| replica lag for a single replica instance.             | - Environment variable: ``MM_SQLSETTINGS_REPLICALAGSETTINGS``                    |
|                                                        |                                                                                  |   
| These settings monitor absolute lag based on binlog    |                                                                                  |
| distance/transaction queue length, and the time taken  |                                                                                  |
| for the replica to catch up.                           |                                                                                  |
|                                                        |                                                                                  |
| String array input consists of:                        |                                                                                  |
|                                                        |                                                                                  |
| - ``DataSource``: The database credentials to connect  |                                                                                  |
|   to the replica instance.                             |                                                                                  |
| - ``QueryAbsoluteLag``: A plain SQL query that must    |                                                                                  |
|   return a single row. The first column must be the    |                                                                                  |
|   node value of the Prometheus metric, and the second  |                                                                                  |
|   column must be the value of the lag used to          |                                                                                  |
|   measure absolute lag.                                |                                                                                  |
| - ``QueryTimeLag``: A plain SQL query that must        |                                                                                  |
|   return a single row. The first column must be the    |                                                                                  |
|   node value of the Prometheus metric, and the second  |                                                                                  |
|   column must be the value of the lag used to measure  |                                                                                  |
|   the time lag.                                        |                                                                                  |
+--------------------------------------------------------+----------------------------------------------------------------------------------+
| Examples:                                                                                                                                 |
|                                                                                                                                           |
| For AWS Aurora instances, ``QueryAbsoluteLag`` can be:                                                                                    |
|                                                                                                                                           |
| .. code-block:: sh                                                                                                                        |
|                                                                                                                                           |
|   select server_id, highest_lsn_rcvd-durable_lsn as bindiff from aurora_global_db_instance_status() where server_id=<>                    |
|                                                                                                                                           |
| And for AWS Aurora instances, ``QueryTimeLag`` can be:                                                                                    |
|                                                                                                                                           |
| .. code-block:: sh                                                                                                                        |
|                                                                                                                                           |
|   select server_id, visibility_lag_in_msec from aurora_global_db_instance_status() where server_id=<>                                     |
|                                                                                                                                           |
| For MySQL Group Replication, the absolute lag can be measured from the number of pending transactions in the applier queue:               |
|                                                                                                                                           |
| .. code-block:: sh                                                                                                                        |
|                                                                                                                                           |
|   select member_id, count_transactions_remote_in_applier_queue FROM performance_schema.replication_group_member_stats where member_id=<>  |
+--------------------------------------------------------+----------------------------------------------------------------------------------+
