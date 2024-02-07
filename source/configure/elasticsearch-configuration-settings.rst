:orphan:
:nosearch:

Elasticsearch provides enterprise-scale deployments with optimized search performance and prevents performance degradation and timeouts. Learn more about `Elasticsearch </scale/elasticsearch.html>`__ in our product documentation.

You can configure the Elasticsearch environment in which Mattermost is deployed in **System Console > Environment > Elasticsearch**. You can also edit the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: elastic-enableindexing
  :displayname: Enable Elasticsearch indexing (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.EnableIndexing
  :environment: MM_ELASTICSEARCHSETTINGS_ENABLEINDEXING
  :description: Configure Mattermost to index new posts automatically.

  - **true**: Indexing of new posts occurs automatically.
  - **false**: **(Default)** Elasticsearch indexing is disabled and new posts are not indexed.

Enable Elasticsearch indexing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------------+
| Configure Mattermost to index new posts automatically.        | - System Config path: **Environment > Elasticsearch**                          |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.EnableIndexing: false",`` |
| - **true**: Indexing of new posts occurs automatically.       | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_ENABLEINDEXING``            |
| - **false**: **(Default)** Elasticsearch indexing is disabled |                                                                                |
|   and new posts are not indexed.                              |                                                                                |
+---------------------------------------------------------------+--------------------------------------------------------------------------------+
| **Notes**:                                                                                                                                     |
|                                                                                                                                                |
| - If indexing is disabled and re-enabled after an index is created, we recommend you purge and rebuild the index to ensure complete            |
|   search results.                                                                                                                              |
| - Search queries will use database search until Elasticsearch for search queries is enabled.                                                   |
+----------------------------------------------------------------------+-------------------------------------------------------------------------+

.. config:setting:: elastic-serverconnectionaddress
  :displayname: Server connection address (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.ConnectionUrl
  :environment: MM_ELASTICSEARCHSETTINGS_CONNECTIONURL
  :description: The address of the Elasticsearch server.

Server connection address
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------+--------------------------------------------------------------------------+
| The address of the Elasticsearch server.           | - System Config path: **Environment > Elasticsearch**                    |
|                                                    | - ``config.json`` setting: ``".Elasticsearchsettings.ConnectionUrl",``   |
|                                                    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CONNECTIONURL``       |
+----------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-CApath
  :displayname: CA path (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.CA
  :environment: MM_ELASTICSEARCHSETTINGS_CA
  :description: Optional path to the Custom Certificate Authority certificates for the Elasticsearch server.

CA path
~~~~~~~

+----------------------------------------------------+--------------------------------------------------------------------------+
| Optional path to the Custom Certificate Authority  | - System Config path: **Environment > Elasticsearch**                    |
| certificates for the Elasticsearch server.         | - ``config.json`` setting: ``".Elasticsearchsettings.CA",``              |
|                                                    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CA``                  |
+----------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: Available from Mattermost v7.8. Can be used in conjunction with basic auth credentials or to replace them.          |
| Leave this setting blank to use the default Certificate Authority certificates for the operating system.                      |
+----------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-clientcertificatepath
  :displayname: Client certificate path (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.ClientCert
  :environment: MM_ELASTICSEARCHSETTINGS_CLIENTCERT
  :description: Optional client certificate for the connection to the Elasticsearch server in PEM format.

Client certificate path
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+--------------------------------------------------------------------------+
| Optional client certificate for the connection to  | - System Config path: **Environment > Elasticsearch**                    |
| the Elasticsearch server in the PEM format.        | - ``config.json`` setting: ``".Elasticsearchsettings.ClientCert",``      |
|                                                    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CLIENTCERT``          |
+----------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: Available from Mattermost v7.8. Can be used in conjunction with basic auth credentials or to replace them.          |
+----------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-clientcertificatekeypath
  :displayname: Client certificate key path (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.ClientKey
  :environment: MM_ELASTICSEARCHSETTINGS_CLIENTKEY
  :description: Optional key for the client certificate in PEM format.

Client certificate key path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+--------------------------------------------------------------------------+
| Optional key for the client certificate in the PEM | - System Config path: **Environment > Elasticsearch**                    |
| format.                                            | - ``config.json`` setting: ``".Elasticsearchsettings.ClientKey",``       |
|                                                    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CLIENTKEY``           |
+----------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: Available from Mattermost v7.8. Can be used in conjunction with basic auth credentials or to replace them.          |
+----------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-skiptlsverification
  :displayname: Skip TLS verification (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.SkipTLSVerification
  :environment: MM_ELASTICSEARCHSETTINGS_SKIPTLSVERIFICATION
  :description: The certificate step for TLS connections can be skipped.

  - **true**: Skips the certificate verification step for TLS connections.
  - **false**: **(Default)** Mattermost does not skip certificate verification.

Skip TLS verification
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------------------------------+
| The certificate step for TLS connections can be skipped.      | - System Config path: **Environment > Elasticsearch**                               |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.SkipTLSVerification: false",`` |
| - **true**: Skips the certificate verification step for       | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_SKIPTLSVERIFICATION``            |
|   TLS connections.                                            |                                                                                     |
| - **false**: **(Default)** Mattermost does not skip           |                                                                                     |
|   certificate verification.                                   |                                                                                     |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------+

.. config:setting:: elastic-serverusername
  :displayname: Server username (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.UserName
  :environment: MM_ELASTICSEARCHSETTINGS_USERNAME
  :description: (Optional) The username to authenticate to the Elasticsearch server.

Server username
~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| (Optional) The username to authenticate to the                | - System Config path: **Environment > Elasticsearch**                    |
| Elasticsearch server.                                         | - ``config.json`` setting: ``".Elasticsearchsettings.UserName",``        |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_USERNAME``            |
| String input.                                                 |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-serverpassword
  :displayname: Server password (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.Password
  :environment: MM_ELASTICSEARCHSETTINGS_PASSWORD
  :description: (Optional) The password to authenticate to the Elasticsearch server.

Server password
~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| (Optional) The password to authenticate to the                | - System Config path: **Environment > Elasticsearch**                    |
| Elasticsearch server.                                         | - ``config.json`` setting: ``".Elasticsearchsettings.Password",``        |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_PASSWORD``            |
| String input.                                                 |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-enablesniffing
  :displayname: Enable cluster sniffing (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.Sniff
  :environment: MM_ELASTICSEARCHSETTINGS_SNIFF
  :description: Configure Mattermost to automatically find and connect to all data nodes in a cluster.

  - **true**: Sniffing finds and connects to all data nodes in your cluster automatically.
  - **false**: **(Default)** Cluster sniffing is disabled.

Enable cluster sniffing
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------+--------------------------------------------------------------------------+
| Configure Mattermost to automatically find and connect to      | - System Config path: **Environment > Elasticsearch**                    |
| all data nodes in a cluster.                                   | - ``config.json`` setting: ``".Elasticsearchsettings.Sniff: false",``    |
|                                                                | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_SNIFF``               |
| - **true**: Sniffing finds and connects to all data nodes      |                                                                          |
|   in your cluster automatically.                               |                                                                          |
| - **false**: **(Default)** Cluster sniffing is disabled.       |                                                                          |
+----------------------------------------------------------------+--------------------------------------------------------------------------+
| Select the **Test Connection** button in the System Console to validate the connection between Mattermost and the Elasticsearch server.   |
+----------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-bulkindexing
  :displayname: Bulk indexing (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: N/A
  :environment: N/A
  :description: Configure Mattermost to start a bulk index of all existing posts in the database by selecting Index Now.

Bulk indexing
~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Configure Mattermost to start a bulk index of all existing    | - System Config path: **Environment > Elasticsearch**                    |
| posts in the database.                                        | - ``config.json`` setting: N/A                                           |
|                                                               | - Environment variable: N/A                                              |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Select the **Index Now** button in the System Console to start a bulk index of all posts. If the indexing process is canceled, the       |
| index and search results will be incomplete.                                                                                             |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-indexestoskipwhilepurging
  :displayname: Indexes to skip while purging (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.IgnoredPurgeIndexes
  :environment: MM_ELASTICSEARCHSETTINGS_IGNOREDPURGEINDEXES
  :description: Specify index names to ignore while purging indexes, separated by commas.


Indexes to skip while purging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Specify index names to ignore while purging indexes.          | - System Config path: **Environment > Elasticsearch**                    |
| Separate multiple index names with commas.                    | - ``config.json`` setting: ElasticsearchSettings.IgnoredPurgeIndexes     |
|                                                               | - Environment variable: MM_ELASTICSEARCHSETTINGS_IGNOREDPURGEINDEXES     |
| Use an asterisk (*) to match a sequence of index name         |                                                                          |
| characters.                                                   |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-purgeindexes
  :displayname: Purge indexes (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: N/A
  :environment: N/A
  :description: Purge the entire Elasticsearch index by selecting Purge Indexes.

Purge indexes
~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------+
| Purge the entire Elasticsearch index.                         | - System Config path: **Environment > Elasticsearch**       |
| Typically only used if the index has corrupted and search     | - ``config.json`` setting: N/A                              |
| isn't behaving as expected.                                   | - Environment variable: N/A                                 |
+---------------------------------------------------------------+-------------------------------------------------------------+
| Select the **Purge Indexes** button in the System Console to purge the index.                                               |
| After purging the index, create a new index by selecting the **Index Now** button.                                          |
+---------------------------------------------------------------+-------------------------------------------------------------+

.. config:setting:: elastic-enablesearch
  :displayname: Enable Elasticsearch for search queries (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.EnableSearching
  :environment: MM_ELASTICSEARCHSETTINGS_ENABLESEARCHING
  :description: Configure Mattermost to use Elasticsearch for all search queries using the latest index.

  - **true**: Elasticsearch will be used for all search queries using the latest index. Search results may be incomplete until a bulk index of the existing post database is finished.
  - **false**: **(Default)** Database search is used for search queries.

Enable Elasticsearch for search queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+---------------------------------------------------------------------------------+
| Configure Mattermost to use Elasticsearch for all search      | - System Config path: **Environment > Elasticsearch**                           |
| queries using the latest index                                | - ``config.json`` setting: ``".Elasticsearchsettings.EnableSearching: false",`` |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_ENABLESEARCHING``            |
| - **true**: Elasticsearch will be used for all search         |                                                                                 |
|   queries using the latest index. Search results may be       |                                                                                 |
|   incomplete until a bulk index of the existing post database |                                                                                 |
|   is finished.                                                |                                                                                 |
| - **false**: **(Default)** Database search is used for        |                                                                                 |
|   search queries.                                             |                                                                                 |
+---------------------------------------------------------------+---------------------------------------------------------------------------------+

.. config:setting:: elastic-enableautocomplete
  :displayname: Enable Elasticsearch for autocomplete queries (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.EnableAutocomplete
  :environment: MM_ELASTICSEARCHSETTINGS_ENABLEAUTOCOMPLETE
  :description: Configure Mattermost to use Elasticsearch for all autocompletion queries on users and channels using the latest index.

  - **true**: Elasticsearch will be used for all autocompletion queries on users and channels using the latest index.
  - **false**: **(Default)** Database autocomplete is used.

Enable Elasticsearch for autocomplete queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+------------------------------------------------------------------------------------+
| Configure Mattermost to use Elasticsearch for all             | - System Config path: **Environment > Elasticsearch**                              |
| autocompletion queries on users and channels using the        | - ``config.json`` setting: ``".Elasticsearchsettings.EnableAutocomplete: false",`` |
| latest index.                                                 | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_ENABLEAUTOCOMPLETE``            |
|                                                               |                                                                                    |
| - **true**: Elasticsearch will be used for all autocompletion |                                                                                    |
|   queries on users and channels using the latest index.       |                                                                                    |
| - **false**: **(Default)** Database autocomplete is used.     |                                                                                    |
+---------------------------------------------------------------+------------------------------------------------------------------------------------+
| **Note**: Autocompletion results may be incomplete until a bulk index of the existing users and channels database is finished.                     |
+---------------------------------------------------------------+------------------------------------------------------------------------------------+

.. config:setting:: elastic-postindexreplicas
  :displayname: Post index replicas (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.PostIndexReplicas
  :environment: MM_ELASTICSEARCHSETTINGS_POSTINDEXREPLICAS
  :description: The number of replicas to use for each post index. Default is **1**.

Post index replicas
~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The number of replicas to use for each post index.            | - System Config path: N/A                                                     |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.PostIndexReplicas: 1",`` |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_POSTINDEXREPLICAS``        |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Important note**: If this setting is changed, the changed configuration only applies to newly-created indexes. To apply the change to       |
| existing indexes, purge and rebuild the index after changing this setting.                                                                    |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

.. config:setting:: elastic-postindexshards
  :displayname: Post index shards (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.PostIndexShards
  :environment: MM_ELASTICSEARCHSETTINGS_POSTINDEXSHARDS
  :description: The number of shards to use for each post index. Default is **1**.

Post index shards
~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The number of shards to use for each post index.              | - System Config path: N/A                                                     |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.PostIndexShards: 1",``   |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_POSTINDEXSHARDS``          |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Important note**: If this setting is changed, the changed configuration only applies to newly-created indexes. To apply the change to       |
| existing indexes, purge and rebuild the index after changing this setting.                                                                    |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

.. config:setting:: elastic-channelindexreplicas
  :displayname: Channel index replicas (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.ChannelIndexReplicas
  :environment: MM_ELASTICSEARCHSETTINGS_CHANNELINDEXREPLICAS
  :description: The number of replicas to use for each channel index. Default is **1**.

Channel index replicas
~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+----------------------------------------------------------------------------------+
| The number of replicas to use for each channel index.         | - System Config path: N/A                                                        |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.ChannelIndexReplicas: 1",`` |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CHANNELINDEXREPLICAS``        |
+---------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: elastic-channelindexshards
  :displayname: Channel index shards (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.ChannelIndexShards
  :environment: MM_ELASTICSEARCHSETTINGS_CHANNELINDEXSHARDS
  :description: The number of shards to use for each channel index. Default is **1**.

Channel index shards
~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+----------------------------------------------------------------------------------+
| The number of shards to use for each channel index.           | - System Config path: N/A                                                        |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.ChannelIndexShards: 1",``   |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CHANNELINDEXSHARDS``          |
+---------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: elastic-userindexreplicas
  :displayname: User index replicas (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.UserIndexReplicas
  :environment: MM_ELASTICSEARCHSETTINGS_USERINDEXREPLICAS
  :description: The number of replicas to use for each user index. Default is **1**.

User index replicas
~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The number of replicas to use for each user index.            | - System Config path: N/A                                                     |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.UserIndexReplicas: 1",`` |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_USERINDEXREPLICAS``        |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

.. config:setting:: elastic-userindexshards
  :displayname: User index shards (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.UserIndexShards
  :environment: MM_ELASTICSEARCHSETTINGS_USERINDEXSHARDS
  :description: The number of shards to use for each user index. Default is **1**.

User index shards
~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+----------------------------------------------------------------------------------+
| The number of shards to use for each user index.              | - System Config path: N/A                                                        |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.UserIndexShards: 1",``      |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_USERINDEXSHARDS``             |
+---------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: elastic-aggregatesearchindexes
  :displayname: Aggregate search indexes (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.AggregatePostsAfterDays
  :environment: MM_ELASTICSEARCHSETTINGS_AGGREGATEPOSTSAFTERDAYS
  :description: Elasticsearch indexes older than the age specified by this setting, in days, will be aggregated during the daily scheduled job. Default is **365** days.

Aggregate search indexes
~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Elasticsearch indexes older than the age specified by this    | - System Config path: N/A                                                              |
| setting, in days, will be aggregated during the daily         | - ``config.json`` setting: ``".Elasticsearchsettings.AggregatePostsAfterDays: 365",``  |
| scheduled job.                                                | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_AGGREGATEPOSTSAFTERDAYS``           |
|                                                               |                                                                                        |
| Numerical input. Default is **365** days.                     |                                                                                        |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
| **Note**: If you’re using `data retention </comply/data-retention-policy.html>`__ and                                                                  |
| `Elasticsearch </scale/elasticsearch.html>`__, configure this with a value greater than your data retention policy.                                    |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------+

.. config:setting:: elastic-postaggregatorstarttime
  :displayname: Post aggregator start time (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.PostsAggregatorJobStartTime
  :environment: MM_ELASTICSEARCHSETTINGS_POSTSAGGREGATORJOBSTARTTIME
  :description: The start time of the daily scheduled aggregator job. Must be a 24-hour time stamp in the form ``HH:MM`` based on the local time of the server. Default is **03:00** (3 AM).

Post aggregator start time
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| The start time of the daily scheduled aggregator job.         | - System Config path: N/A                                                                   |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.PostsAggregatorJobStartTime: 03:00",`` |
| Must be a 24-hour time stamp in the form ``HH:MM`` based on   | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_POSTSAGGREGATORJOBSTARTTIME``            |
| the local time of the server.                                 |                                                                                             |
|                                                               |                                                                                             |
| Default is **03:00** (3 AM)                                   |                                                                                             |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+

.. config:setting:: elastic-indexprefix
  :displayname: Index prefix (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.IndexPrefix
  :environment: MM_ELASTICSEARCHSETTINGS_INDEXPREFIX
  :description: The prefix added to the Elasticsearch index name.

Index prefix
~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The prefix added to the Elasticsearch index name.             | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.IndexPrefix",``     |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_INDEXPREFIX``         |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: When this setting is used, all Elasticsearch indexes created by Mattermost are given this prefix. You can set different        |
| prefixes so that multiple Mattermost deployments can share an Elasticsearch cluster without the index names colliding.                   |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-liveindexingbatchsize
  :displayname: Live indexing batch size (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.LiveIndexingBatchSize
  :environment: MM_ELASTICSEARCHSETTINGS_LIVEINDEXINGBATCHSIZE
  :description: The number of new posts batched together before they're added to the Elasticsearch index. Default is **1**.

Live indexing batch size
~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-----------------------------------------------------------------------------------+
| The number of new posts needed before those posts are added   | - System Config path: N/A                                                         |
| to the Elasticsearch index. Once added to the Index,          | - ``config.json`` setting: ``".Elasticsearchsettings.LiveIndexingBatchSize: 1",`` |
| the post becomes searchable.                                  | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_LIVEINDEXINGBATCHSIZE``        |
|                                                               |                                                                                   |
| On servers with more than 1 post per second, we suggest       |                                                                                   |
| setting this value to the average number of  posts over a     |                                                                                   |
| 20 second period of time.                                     |                                                                                   |
|                                                               |                                                                                   |
| Numerical input. Default is **1**. Every post is indexed      |                                                                                   |
| synchronously as they are created.                            |                                                                                   |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------+
| **Note**: It may be necessary to increase this value to avoid hitting the rate limit or resource limit of your Elasticsearch cluster              |
| on installs handling more than 1 post per second.                                                                                                 |
|                                                                                                                                                   |
| **What exactly happens when I increase this value?**                                                                                              |
| The primary impact is that a post will be indexed into Elasticsearch after the threshold of posts is met which then makes the posts searchable    |
| within Mattermost. So, if you set this based on our recommendations for larger servers, and you make a post, you cannot find it via search        | 
| for ~ 10-20 seconds, on average. Realistically, no users should see or feel this impact due to the limited amount of users who are actively       |
| **searching** for a post this quickly. You can set this value to a lower average or higher average as well, depending on your Elasticsearch       |
| server specifications.                                                                                                                            |
|                                                                                                                                                   |
| During busy periods, this delay will be faster as more traffic is happening, causing more posts and a quicker time to hit the index number.       |
| During slow times, expect the reverse.                                                                                                            |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------+

**How to find the right number for your server**

1. You must understand how many posts your server makes every minute. Run the query below to calculate your server's average posts per minute.

    Note that this query can be heavy, so we recommend that you run it during non-peak hours.
    Additionally, you can adjust the ``WHERE`` clause to see the posts per minute over a different time period. Right now ``31536000000`` represents the number of milliseconds in a year. 

    .. code-block:: SQL

      SELECT
        AVG(postsPerMinute) as averagePostsPerMinute
      FROM (
        SELECT 
          count(*) as postsPerMinute, 
          date_trunc('minute', to_timestamp(createat/1000))
        FROM posts
        WHERE createAt > ( (extract(epoch from now()) * 1000 )  - 31536000000)
        GROUP BY date_trunc('minute', to_timestamp(createat/1000))
      ) as ppm;

2. Decide the acceptable index window for your environment, and divide your average posts per minute by that. We suggest 10-20 seconds. Assuming you have ``600`` posts per minute on average, and you want to index every 20 seconds (``60 seconds / 20 seconds = 3```) you would calculate ``600 / 3`` to come to the number ``200``. After 200 posts, Mattermost will index the posts into Elasticsearch. So, on average, there would be a 20-second delay in searchability.

3. Edit the ``config.json`` or run mmctl to modify the ``LiveIndexingBatchSize`` setting
  
    **In the ``config.json``**

    .. code-block:: JSON

      {
        "ElasticsearchSettings": {
          "LiveIndexingBatchSize": 200
        }
      }
    

    **Via mmctl**

    .. code-block:: JSON

      mmctl config set ElasticsearchSettings.LiveIndexingBatchSize 200

    **Via an environment variable**

    .. code-block:: JSON

      MM_ELASTICSEARCHSETTINGS_LIVEINDEXINGBATCHSIZE = 200

4. Restart the Mattermost server.

.. config:setting:: elastic-bulkindexingtimewindow
  :displayname: Bulk indexing time window (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.BulkIndexingTimeWindowSeconds
  :environment: MM_ELASTICSEARCHSETTINGS_BULKINDEXINGTIMEWINDOWSECONDS

  The maximum time window, in seconds, for a batch of posts being indexed by the Bulk Indexer.
  This setting serves as a performance optimization for installs with over ~10 million posts in the database.
  Default is **3600** seconds (1 hour).

Bulk indexing time window
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| The maximum time window, in seconds, for a batch of posts     | - System Config path: **Environment > Elasticsearch**                                        |
| being indexed by the Bulk Indexer. This setting serves as a   | - ``config.json`` setting: ``".Elasticsearchsettings.BulkIndexingTimeWindowSeconds: 3600",`` |
| performance optimization for installs with over               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_BULKINDEXINGTIMEWINDOWSECONDS``           |
| ~10 million posts in the database.                            |                                                                                              |
|                                                               |                                                                                              |
| Numerical input in seconds. Default is **3600** seconds       |                                                                                              |
| (1 hour). Approximate this value based on the average number  |                                                                                              |
| of seconds for 2,000 posts to be added to the database on a   |                                                                                              |
| typical day in production.                                    |                                                                                              |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| **Note**: Setting this value too low will cause bulk indexing jobs to run slowly.                                                                            |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------------+

.. config:setting:: elastic-requesttimeout
  :displayname: Request timeout (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.RequestTimeoutSeconds
  :environment: MM_ELASTICSEARCHSETTINGS_REQUESTTIMEOUTSECONDS
  :description: The timeout, in seconds, for Elasticsearch calls. Default is **30** seconds.

Request timeout
~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+------------------------------------------------------------------------------------+
| The timeout, in seconds, for Elasticsearch calls.             | - System Config path: N/A                                                          |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.RequestTimeoutSeconds :30",`` |
| Numerical input in seconds. Default is **30** seconds.        | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_REQUESTTIMEOUTSECONDS``         |
+---------------------------------------------------------------+------------------------------------------------------------------------------------+

.. config:setting:: elastic-trace
  :displayname: Trace (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.Trace
  :environment: MM_ELASTICSEARCHSETTINGS_TRACE
  :description: Options for printing Elasticsearch trace errors.

  - **error**: Creates the error trace when initializing the Elasticsearch client and prints any template creation or search query that returns an error as part of the error message.
  - **all**: Creates the three traces (error, trace and info) for the driver and doesn’t print the queries because they will be part of the trace log level of the driver.
  - **not specified**: **(Default)** No error trace is created.

Trace
~~~~~

.. raw:: html

 <p class="mm-badge-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Options for printing Elasticsearch trace errors.              | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.Trace",``           |
| - **error**: Creates the error trace when initializing        | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_TRACE``               |
|   the Elasticsearch client and prints any template creation   |                                                                          |
|   or search query that returns an error as part of the        |                                                                          |
|   error message.                                              |                                                                          |
| - **all**: Creates the three traces (error, trace and info)   |                                                                          |
|   for the driver and doesn’t print the queries because they   |                                                                          |
|   will be part of the trace log level of the driver.          |                                                                          |
| - **not specified**: **(Default)** No error trace is created. |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+