:orphan:
:nosearch:

Configure the database environment in which Mattermost is deployed by going to **System Console > Environment > Database**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. include:: ../_static/badges/academy-mattermost-database.rst
  :start-after: :nosearch:

.. config:setting:: database-drivername
  :displayname: Driver name (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.DriverName
  :environment: MM_SQLSETTINGS_DRIVERNAME
  :description: The type of database. Either **postgres** or **mysql**. The default value is **mysql**.

Driver name
~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The type of database. Can be either:                          | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``".SqlSettings.DriverName",``                |
| - **mysql**: **(Default)** Enables driver to MySQL database.  | - Environment variable: ``MM_SQLSETTINGS_DRIVERNAME``                    |
| - **postgres**: Enables driver to PostgreSQL database.        |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: database-datasource
  :displayname: Data source (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.DataSource
  :environment: MM_SQLSETTINGS_DATASOURCE
  :description: The connection string to the master database.

Data source
~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The connection string to the master database.                 | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``".SqlSettings.DataSource",``                |
| String input.                                                 | - Environment variable: ``MM_SQLSETTINGS_DATASOURCE``                    |
|                                                               |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **PostgreSQL databases**                                                                                                                 |
|                                                                                                                                          |
| When **Driver Name** is set to ``postgres``, use a connection string in the form of:                                                     |
| ``postgres://mmuser:password@hostname_or_IP:5432/mattermost_test?sslmode=disable&connect_timeout=10``                                    |
|                                                                                                                                          |
| **To use TLS with PostgreSQL databases**                                                                                                 |
|                                                                                                                                          |
| The parameter to encrypt connection against a PostgreSQL server is ``sslmode``. The library used to interact with PostgreSQL server is   |
| `pq <https://pkg.go.dev/github.com/lib/pq>`__. Currently, it's not possible to use all the values that you could pass to a standard      |
| PostgreSQL Client ``psql "sslmode=value"`` See the `SSL Mode Descriptions <https://www.postgresql.org/docs/current/libpq-ssl.html>`__    |
| documentation for details.                                                                                                               |
|                                                                                                                                          |
| Your database admin must configure the functionality according to the supported values described below:                                  |
|                                                                                                                                          |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
| | Short description of the ``sslmode``   | Value           | Example of a data source name                                             | |
| | parameter                              |                 |                                                                           | |
| +========================================+=================+===========================================================================+ |
| | Don't use TLS / SSL encryption against | ``disable``     | ``postgres://mmuser:password@hostname_or_IP:5432/mattermost_test          | |
| | the PostgreSQL server.                 |                 | ?sslmode=disable&connect_timeout=10``                                     | |
| |                                        |                 |                                                                           | |
| | Default value in file ``config.json``  |                 |                                                                           | |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
| | The data is encrypted and the network  | ``require``     | ``postgres://mmuser:password@hostname_or_IP:5432/mattermost_test          | |
| | is trusted.                            |                 | ?sslmode=require&connect_timeout=10``                                     | |
| |                                        |                 |                                                                           | |
| | Default value is ``sslmode`` when      |                 |                                                                           | |
| | omitted.                               |                 |                                                                           | |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
| | The data is encrypted when connecting  | ``verify-ca``   | ``postgres://mmuser:password@hostname_or_IP:5432/mattermost_test          | |
| | to a trusted server.                   |                 | ?sslmode=verify-ca&connect_timeout=10``                                   | |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
| | The data is encrypted when connecting  | ``verify-full`` | ``postgres://mmuser:password@hostname_or_IP:5432/mattermost_test          | |
| | to a trusted server.                   |                 | ?sslmode=verify-full&connect_timeout=10``                                 | |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
|                                                                                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **MySQL databases**                                                                                                                      |
|                                                                                                                                          |
| When **Driver Name** is set to ``mysql``, we recommend using ``collation`` over using ``charset``.                                       |
|                                                                                                                                          |
| To specify collation:                                                                                                                    |
|                                                                                                                                          |
| .. code-block:: none                                                                                                                     |
|                                                                                                                                          |
|   "SqlSettings": {                                                                                                                       |
|       "DataSource":                                                                                                                      |
|   "<mmuser:password>@tcp(hostname or IP:3306)/mattermost?charset=utf8mb4,utf8&collation=utf8mb4_general_ci",                             |
|       [...]                                                                                                                              |
|    }                                                                                                                                     |
|                                                                                                                                          |
| If collation is omitted, the default collation, ``utf8mb4_general_ci`` is used:                                                          |
|                                                                                                                                          |
| .. code-block:: none                                                                                                                     |
|                                                                                                                                          |
|   "SqlSettings": {                                                                                                                       |
|       "DataSource": "<mmuser:password>@tcp(hostname or IP:3306)/mattermost?charset=utf8mb4,utf8",                                        |
|       [...]                                                                                                                              |
|    }                                                                                                                                     |
|                                                                                                                                          |
| **Note**: If you’re using MySQL 8.0 or later, the default collation has changed to ``utf8mb4_0900_ai_ci``. See our `Database Software    |
| Requirements </install/software-hardware-requirements.html>`__ documentation for details on MySQL 8.0 support.                           |
|                                                                                                                                          |
| **To use TLS with MySQL databases**                                                                                                      |
|                                                                                                                                          |
| The parameter to encrypt connection against a MySQL server is ``tls``.                                                                   |
| The library used to interact with MySQL is `Go-MySQL-Driver <https://pkg.go.dev/github.com/go-sql-driver/mysql>`__.                      |
| For the moment, it's not possible to use all the values that you could pass to a standard MySQL Client ``mysql --ssl-mode=value``.       |
| See `Connection-Encryption Option Summary <https://dev.mysql.com/doc/refman/8.0/en/connection-options.html #option_general_ssl-mode>`__  |
| documentation for a version 8.0 example.                                                                                                 |
|                                                                                                                                          |
| Your database admin must configure the functionality according to supported values described below:                                      |
|                                                                                                                                          |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
| | Short description of the ``tls``       | Value           | Example of a data source name                                             | |
| | parameter                              |                 |                                                                           | |
| +========================================+=================+===========================================================================+ |
| | Don't use TLS / SSL encryption against | ``false``       | ``"<mmuser:password>@tcp(hostname or IP:3306)/mattermost_test             | |
| | MySQL server.                          |                 | ?charset=utf8mb4,utf8&writeTimeout=30s&tls=false"``                       | |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
| | Use TLS / SSL encryption against       | ``true``        | ``"<mmuser:password>@tcp(hostname or IP:3306)/mattermost_test             | |
| | MySQL server.                          |                 | ?charset=utf8mb4,utf8&writeTimeout=30s&tls=true"``                        | |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
| | Use TLS / SSL encryption with a self-  | ``skip-verify`` | ``"<mmuser:password>@tcp(hostname or IP:3306)/mattermost_test             | |
| | signed certificate against             |                 | ?charset=utf8mb4,utf8&writeTimeout=30s&tls=skip-verify"``                 | |
| | MySQL server.                          |                 |                                                                           | |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
| | Use TLS / SSL encryption if server     | ``preferred``   | ``"<mmuser:password>@tcp(hostname or IP:3306)/mattermost_test             | |
| | advertises a possible fallback;        |                 | ?charset=utf8mb4,utf8&writeTimeout=30s&tls=preferred"``                   | |
| | unencrypted if it's not advertised.    |                 |                                                                           | |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
|                                                                                                                                          |
+------------------------------------------------------------+-----------------------------------------------------------------------------+
| **AWS High Availablity RDS cluster deployments**                                                                                         |
|                                                                                                                                          |
| For an AWS High Availability RDS cluster deployment, point this configuration setting to the write/read endpoint at the **cluster**      |
| level to benefit from the AWS failover handling. AWS takes care of promoting different database nodes to be the writer node.             |
| Mattermost doesn't need to manage this. See the                                                                                          |
| `high availablility database configuration </scale/high-availability-cluster.html#database-configuration>`__ documentation for details.  |
+------------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: database-maxidleconnections
  :displayname: Maximum idle database connections (Database)
  :systemconsole: Environment > Database
  :configjson: SqlSettings.MaxIdleConns
  :environment: MM_SQLSETTINGS_MAXIDLECONNS
  :description: The maximum number of idle connections held open to the database. Default is **10**.

Maximum idle database connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+------------------------------------------------------------------+
| The maximum number of idle connections held open       | - System Config path: **Environment > Database**                 |
| to the database.                                       | - ``config.json`` setting: ``".SqlSettings.MaxIdleConns": 10,``  |
|                                                        | - Environment variable: ``MM_SQLSETTINGS_MAXIDLECONNS``          |
| Numerical input. Default is **10**.                    |                                                                  |
+--------------------------------------------------------+------------------------------------------------------------------+

.. config:setting:: database-maxopenconnections
  :displayname: Maximum open connections (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.MaxOpenConns
  :environment: MM_SQLSETTINGS_MAXOPENCONNS
  :description: The maximum number of idle connections held open to the database. Default is **300**.

Maximum open connections
~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+------------------------------------------------------------------+
| The maximum number of open connections to the          | - System Config path: **Environment > Database**                 |
| database.                                              | - ``config.json`` setting: ``".SqlSettings.MaxOpenConns": 300,`` |
|                                                        | - Environment variable: ``MM_SQLSETTINGS_MAXOPENCONNS``          |
| Numerical input. Default is **300** for self-hosted    |                                                                  |
| deployments, and **100** for Cloud deployments.        |                                                                  |
+--------------------------------------------------------+------------------------------------------------------------------+

.. config:setting:: database-querytimeout
  :displayname: Query timeout (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.QueryTimeout
  :environment: MM_SQLSETTINGS_QUERYTIMEOUT
  :description: The amount of time to wait, in seconds, for a response from the database after opening a connection and sending the query. Default is **30** seconds.

Query timeout
~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+------------------------------------------------------------------+
| The amount of time to wait, in seconds, for a response | - System Config path: **Environment > Database**                 |
| from the database after opening a connection and       | - ``config.json`` setting: ``".SqlSettings.QueryTimeout: 30",``  |
| sending the query.                                     | - Environment variable: ``MM_SQLSETTINGS_QUERYTIMEOUT``          |
|                                                        |                                                                  |
| Numerical input in seconds. Default is **30** seconds. |                                                                  |
+--------------------------------------------------------+------------------------------------------------------------------+

.. config:setting:: database-maxconnectionlifetime
  :displayname: Maximum connection lifetime (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.ConnMaxLifetimeMilliseconds
  :environment: MM_SQLSETTINGS_CONNMAXLIFETIMEMILLISECONDS
  :description: Maximum lifetime for a connection to the database, in milliseconds. Default is **3600000** milliseconds (1 hour).

Maximum connection lifetime
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+-------------------------------------------------------------------------------------+
| Maximum lifetime for a connection to the database,     | - System Config path: **Environment > Database**                                    |
| in milliseconds. Use this setting to configure the     | - ``config.json`` setting: ``".SqlSettings.ConnMaxLifetimeMilliseconds: 3600000",`` |
| maximum amount of time a connection to the database    | - Environment variable: ``MM_SQLSETTINGS_CONNMAXLIFETIMEMILLISECONDS``              |
| may be reused                                          |                                                                                     |
|                                                        |                                                                                     |
| Numerical input in milliseconds. Default is            |                                                                                     |
| **3600000** milliseconds (1 hour).                     |                                                                                     |
+--------------------------------------------------------+-------------------------------------------------------------------------------------+

.. config:setting:: database-connmaxidletime
  :displayname: Maximum connection idle timeout (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.ConnMaxIdleTimeMilliseconds
  :environment: MM_SQLSETTINGS_CONNMAXIDLETIMEMILLISECONDS
  :description: Maximum time a database connection can remain idle, in milliseconds. Default is **300000** milliseconds (5 minutes).

Maximum connection idle timeout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+-------------------------------------------------------------------------------------+
| Maximum time a database connection can remain idle,    | - System Config path: **Environment > Database**                                    |
| in milliseconds.                                       | - ``config.json`` setting: ``".SqlSettings.ConnMaxIdleTimeMilliseconds: 300000",``  |
|                                                        | - Environment variable: ``MM_SQLSETTINGS_CONNMAXIDLETIMEMILLISECONDS``              |
| Numerical input in milliseconds. Default is **300000** |                                                                                     |
| (5 minutes).                                           |                                                                                     |
+--------------------------------------------------------+-------------------------------------------------------------------------------------+

.. config:setting:: database-minhashtaglength
  :displayname: Minimum hashtag length (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.MinimumHashtagLength
  :environment: MM_SQLSETTINGS_MINIMUMHASHTAGLENGTH
  :description: Minimum number of characters in a hashtag. This value must be greater than or equal to **2**. Default is **3**.

Minimum hashtag length
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------------+-------------------------------------------------------------------------+
| Minimum number of characters in a hashtag.                           | - System Config path: **Environment > Database**                        |
| This value must be greater than or equal to **2**.                   | - ``config.json`` setting: ``".SqlSettings.MinimumHashtagLength: 3",``  |
|                                                                      | - Environment variable: ``MM_SQLSETTINGS_MINIMUMHASHTAGLENGTH``         |
+----------------------------------------------------------------------+-------------------------------------------------------------------------+
| **Note**: MySQL databases must be configured to support searching strings shorter than three characters. See the                               |
| `MySQL documentation <https://dev.mysql.com/doc/refman/8.0/en/fulltext-fine-tuning.html>`__ for details.                                       |
+----------------------------------------------------------------------+-------------------------------------------------------------------------+

.. config:setting:: database-sqltrace
  :displayname: SQL statement logging (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.Trace
  :environment: MM_SQLSETTINGS_TRACE

  - **true**: Executing SQL statements are written to the log.
  - **false**: **(Default)** SQL statements aren't written to the log.

SQL statement logging
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

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

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+--------------------------------------------------------+------------------------------------------------------------------+
| Select the **Recycle Database Connections** button to  | - System Config path: **Environment > Database**                 |
| manually recycle the connection pool by closing the    | - ``config.json`` setting: N/A                                   |
| current set of open connections to the database        | - Environment variable: N/A                                      |
| within 20 seconds, and then creating a new set of      |                                                                  |
| connections.                                           |                                                                  |
|                                                        |                                                                  |
| To fail over without stopping the server, change the   |                                                                  |
| database line in the ``config.json`` file, select      |                                                                  |
| **Reload Configuration from Disk** via **Environment   |                                                                  |
| > Web Server**, then select **Recycle Database         |                                                                  |
| Connections**.                                         |                                                                  |
+--------------------------------------------------------+------------------------------------------------------------------+

.. config:setting:: database-disablesearch
  :displayname: Disable database search (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.DisableDatabaseSearch
  :environment: MM_SQLSETTINGS_DISABLEDATABASESEARCH

  - **true**: Disables the use of the database to perform searches. If another search engine isn't configured, setting this value to ``true`` will result in empty search results.
  - **false**: **(Default)** Database search isn't disabled.

Disable database search
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+------------------------------------------------------------------------------+
| When other search engines are configured, such as             | - System Config path: **Environment > Database**                             |
| `Elasticsearch </scale/elasticsearch.html>`__,                | - ``config.json`` setting: ``".SqlSettings.DisableDatabaseSearch: false",``  |
| the database can be disabled to perform searches.             | - Environment variable: ``MM_SQLSETTINGS_DISABLEDATABASESEARCH``             |
|                                                               |                                                                              |
| - **true**: Disables the use of the database to perform       |                                                                              |
|   searches. If another search engine isn't configured,        |                                                                              |
|   setting this value to ``true`` will result in empty search  |                                                                              |
|   results.                                                    |                                                                              |
| - **false**: **(Default)** Database search isn't disabled.    |                                                                              |
+---------------------------------------------------------------+------------------------------------------------------------------------------+
| Search behavior in Mattermost depends on which search engines are enabled.                                                                   |
|                                                                                                                                              |
| - When `Elasticsearch </scale/elasticsearch.html>`__ is enabled, Mattermost will try to use it first.                                        |
| - If Elasticsearch fails or is disabled, Mattermost will attempt to use `Bleve </deploy/bleve-search.html>`__, if enabled. If this occurs,   |
|   you will see the warning ``Encountered error on SearchPostsInTeamForUser.``                                                                |
| - If both Elasticsearch and Bleve fail or are disabled, Mattermost tries to search the database directly, if this is enabled.                |
| - If all of the above methods fail or are disabled, the search results will be empty.                                                        |
+---------------------------------------------------------------+------------------------------------------------------------------------------+

Applied schema migrations
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

A list of all migrations that have been applied to the data store based on the version information available in the ``db_migrations`` table. Select **About Mattermost** from the product menu to review the current database schema version applied to your deployment.


.. config:setting:: database-activesearchbackend
  :displayname: Active search backend (Database)
  :systemconsole: Environment > Database
  :configjson: N/A
  :environment: N/A
  :description: Read-only display of the currently active backend used for search.

Active Search Backend
~~~~~~~~~~~~~~~~~~~~~

Read-only display of the currently active backend used for search. Values can include ``none``, ``database``, ``elasticsearch``, or ``bleve``.

.. config:setting:: database-readreplicas
  :displayname: Read replicas (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.DataSourceReplicas
  :environment: MM_SQLSETTINGS_DATASOURCEREPLICAS
  :description: Specifies the connection strings for the read replica databases.

Read replicas
~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+-----------------------------------------------------------------------+
| Specifies the connection strings for the read replica  | - System Config path: N/A                                             |
| databases.                                             | - ``config.json`` setting: ``".SqlSettings.DataSourceReplicas": []``  |
|                                                        | - Environment variable: ``MM_SQLSETTINGS_DATASOURCEREPLICAS``         |
+--------------------------------------------------------+-----------------------------------------------------------------------+
| **Note**: Each database connection string in the array must be in the same form used for the                                   |
| `Data source <#data-source>`__ setting.                                                                                        |
+--------------------------------------------------------+-----------------------------------------------------------------------+
| **AWS High Availablity RDS cluster deployments**                                                                               |
|                                                                                                                                |
| For an AWS High Availability RDS cluster deployment, point this configuration setting directly to the underlying read-only     |
| node endpoint within the RDS cluster to circumvent the failover/load balancing that AWS/RDS takes care of (except for the      |
| write traffic). Mattermost has its own method of balancing the read-only connections, and can also balance those queries to    |
| the data source/write+read connection should those nodes fail. See the                                                         |
| `high availablility database configuration </scale/high-availability-cluster.html#database-configuration>`__ documentation     |
| for details.                                                                                                                   |
+--------------------------------------------------------+-----------------------------------------------------------------------+

.. config:setting:: database-searchreplicas
  :displayname: Search replicas (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.DataSourceSearchReplicas
  :environment: MM_SQLSETTINGS_DATASOURCESEARCHREPLICAS

  Specifies the connection strings for the search replica databases.
  A search replica is similar to a read replica, but is used only for handling search queries.

Search replicas
~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+-----------------------------------------------------------------------------+
| Specifies the connection strings for the search        | - System Config path: N/A                                                   |
| replica databases. A search replica is similar to a    | - ``config.json`` setting: ``".SqlSettings.DataSourceSearchReplicas": []``  |
| read replica, but is used only for handling search     | - Environment variable: ``MM_SQLSETTINGS_DATASOURCESEARCHREPLICAS``         |
| queries.                                               |                                                                             |
+--------------------------------------------------------+-----------------------------------------------------------------------------+
| **Note**: Each database connection string in the array must be in the same form used for the `Data source <#data-source>`__          |
| setting.                                                                                                                             |
+--------------------------------------------------------+-----------------------------------------------------------------------------+
| **AWS High Availablity RDS cluster deployments**                                                                                     |
|                                                                                                                                      |
| For an AWS High Availability RDS cluster deployment, point this configuration setting directly to the underlying read-only           |
| node endpoint within the RDS cluster to circumvent the failover/load balancing that AWS/RDS takes care of (except for the            |
| write traffic). Mattermost has its own method of balancing the read-only connections, and can also balance those queries to          |
| the data source/write+read connection should those nodes fail. See the                                                               |
| `high availablility database configuration </scale/high-availability-cluster.html#database-configuration>`__ documentation for       |
| details.                                                                                                                             |
+--------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: database-replicalagsettings
  :displayname: Replica lag settings (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.ReplicaLagSettings
  :environment: MM_SQLSETTINGS_REPLICALAGSETTINGS
  :description: Specifies a connection string and user-defined SQL queries on the database to measure replica lag for a single replica instance.

Replica lag settings
~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

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
|   to the database instance.                            |                                                                                  |
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
| **Notes**:                                                                                                                                |
|                                                                                                                                           |
| - The ``QueryAbsoluteLag`` and ``QueryTimeLag`` queries must return a single row.                                                         |
| - To properly monitor this you must setup `performance monitoring </scale/performance-monitoring.html>`__ for Mattermost.                 |
+--------------------------------------------------------+----------------------------------------------------------------------------------+

1. Configure the replica lag metric based on your database type. See the following tabs for details on configuring this for each database type.

  .. tabs::

    .. tab:: AWS Aurora

      Add the configuration highlighted below to your ``SqlSettings.ReplicaLagSettings`` array. You only need to add this once because replication statistics for AWS Aurora nodes are visible across all server instances that are members of the cluster. Be sure to change the ``DataSource`` to point to a single node in the group. 

      For more information on Aurora replication stats, see the `AWS Aurora documentaion <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_global_db_instance_status.html>`__.

          **Example:**

          .. code-block:: json
            :emphasize-lines: 4,5,6,7,8
    
            {
              "SqlSettings": {
                  "ReplicaLagSettings": [
                    {
                        "DataSource": "replica-1",
                        "QueryAbsoluteLag": "select server_id, highest_lsn_rcvd-durable_lsn as bindiff from aurora_global_db_instance_status() where server_id=<>",
                        "QueryTimeLag": "select server_id, visibility_lag_in_msec from aurora_global_db_instance_status() where server_id=<>"
                    }
                  ]
              }
            }

    .. tab:: MySQL Group Replication

      Add the configuration highlighted below to your ``SqlSettings.ReplicaLagSettings`` array. You only need to add this once because replication statistics for all nodes are shared across all server instances that are members of the MySQL replication group. Be sure to change the ``DataSource`` to point to a single node in the group. 

      For more information on group replication stats, see the `MySQL documentation <https://dev.mysql.com/doc/refman/8.0/en/group-replication-replication-group-member-stats.html>`__.

          **Example:**

          .. code-block:: json
            :emphasize-lines: 4,5,6,7,8
    
            {
              "SqlSettings": {
                  "ReplicaLagSettings": [
                    {
                        "DataSource": "replica-1",
                        "QueryAbsoluteLag": "select member_id, count_transactions_remote_in_applier_queue FROM performance_schema.replication_group_member_stats where member_id=<>",
                        "QueryTimeLag": ""
                    }
                  ]
              }
            }

    .. tab:: PostgreSQL replication slots

      1. Add the configuration highlighted below to your ``SqlSettings.ReplicaLagSettings`` array. This query should run against the **primary** node in your cluster, to do this change the ``DataSource`` to match the `SqlSettings.DataSource <#data-source>`__ setting you have configured. 

          For more information on pg_stat_replication, see the `PostgreSQL documentation <https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-REPLICATION-VIEW>`__.

              **Example:**

              .. code-block:: json
                :emphasize-lines: 4,5,6,7,8
        
                {
                  "SqlSettings": {
                      "ReplicaLagSettings": [
                        {
                            "DataSource": "postgres://mmuser:password@localhost:5432/mattermost_test?sslmode=disable&connect_timeout=10.",
                            "QueryAbsoluteLag": "select usename, pg_wal_lsn_diff(pg_current_wal_lsn(),replay_lsn) as metric from pg_stat_replication;",
                            "QueryTimeLag": ""
                        }
                      ]
                  }
                }

      2. Grant permissions to the database user for ``pg_monitor``. This user should be the same user configured above in the ``DataSource`` string.

          For more information on roles, see the `PostgreSQL documentation <https://www.postgresql.org/docs/10/default-roles.html>`__.

          .. code-block:: bash

            sudo -u postgres psql
            postgres=# GRANT pg_monitor TO mmuser;

      
2. Save the config and restart all Mattermost nodes.
3. Navigate to your Grafana instance monitoring Mattermost and open the `Mattermost Performance Monitoring v2 <https://grafana.com/grafana/dashboards/15582-mattermost-performance-monitoring-v2/>`__ dashboard.
4. The ``QueryTimeLag`` chart is already setup for you utilizing the existing ``Replica Lag`` chart. If using ``QueryAbsoluteLag`` metric clone the ``Replica Lag`` chart and edit the query to use the below absolute lag metrics and modify the title to be ``Replica Lag Absolute``.

    .. code-block:: none

      mattermost_db_replica_lag_abs{instance=~"$server"}

    .. image::  ../../source/images/database-configuration-settings-replica-lag-grafana-1.jpg
      :alt: A screenshot showing how to clone a chart within Grafana


    .. image:: ../../source/images/database-configuration-settings-replica-lag-grafana-2.jpg
      :alt: A screenshot showing the specific edits to make to the cloned grafana chart.


.. config:setting:: database-replicamonitorintervalseconds
  :displayname: Replica monitor interval (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.ReplicaMonitorIntervalSeconds
  :environment: MM_SQLSETTINGS_REPLICAMONITORINTERVALSECONDS

  Specifies how frequently unhealthy replicas will be monitored for liveness check. Mattermost will dynamically choose a replica if it's alive.

Replica monitor interval (seconds)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

+--------------------------------------------------------+---------------------------------------------------------------------------------+
| Specifies how frequently unhealthy replicas will be    | - System Config path: N/A                                                       |
| monitored for liveness check. Mattermost will          | - ``config.json`` setting: ``".SqlSettings.ReplicaMonitorIntervalSeconds": 5``  |
| dynamically choose a replica if it's alive.            | - Environment variable: ``MM_SQLSETTINGS_REPLICAMONITORINTERVALSECONDS``        |
|                                                        |                                                                                 |
| Numerical input. Default is 5 seconds.                 |                                                                                 |
+--------------------------------------------------------+---------------------------------------------------------------------------------+
