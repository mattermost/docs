Elasticsearch configuration settings
====================================

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 25
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 25
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Elasticsearch provides enterprise-scale deployments with optimized search performance and prevents performance degradation and timeouts. Learn more about `Elasticsearch <https://docs.mattermost.com/scale/elasticsearch.html>`__ in our product documentation. 

Configure the Elasticsearch environment in which Mattermost is deployed by going to **System Console > Environment > Elasticsearch**, or by editing the ``config.json`` file as described in the following table. Changes to configuration settings in this section require a server restart before taking effect.

.. include:: common-config-settings-notation.rst
    :start-after: :nosearch:

Enable Elasticsearch indexing
-----------------------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------------+
| New posts can be automatically indexed.                       | - System Config path: **Environment > Elasticsearch**                          |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.EnableIndexing: false",`` |
| - **true**: Indexing of new posts occurs automatically.       | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_ENABLEINDEXING``            |
| - **false**: **(Default)** Elasticsearch indexing is disabled |                                                                                |
|   and new posts are not indexed.                              |                                                                                |
+---------------------------------------------------------------+--------------------------------------------------------------------------------+
| **Note**:                                                                                                                                      |
|                                                                                                                                                |
| - If indexing is disabled and re-enabled after an index is created, we recommend you purge and rebuild the index to ensure complete            |
|   search results.                                                                                                                              |
| - Search queries will use database search until Elasticsearch for search queries is enabled.                                                   |
+----------------------------------------------------------------------+-------------------------------------------------------------------------+

Server connection address
--------------------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The address of the Elasticsearch server.                      | - System Config path: **Environment > Elasticsearch**                    |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.ConnectionUrl",``   |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CONNECTIONURL``       |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Skip TLS verification
----------------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+-------------------------------------------------------------------------------------+
| The certificate step for TLS connections can be skipped.      | - System Config path: **Environment > Elasticsearch**                               |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.SkipTLSVerification: false",`` |
| - **true**: Skips the certificate verification step for       | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_SKIPTLSVERIFICATION``            |
|   TLS connections.                                            |                                                                                     |
| - **false**: **(Default)** Mattermost does not skip           |                                                                                     |
|   certificate verification.                                   |                                                                                     |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------+

Server username
---------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| (Optional) The username to authenticate to the                | - System Config path: **Environment > Elasticsearch**                    |
| Elasticsearch server.                                         | - ``config.json`` setting: ``".Elasticsearchsettings.UserName",``        |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_USERNAME``            |
| String input.                                                 |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Server password
---------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| (Optional) The password to authenticate to the                | - System Config path: **Environment > Elasticsearch**                    |
| Elasticsearch server.                                         | - ``config.json`` setting: ``".Elasticsearchsettings.Password",``        |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_PASSWORD``            |
| String input.                                                 |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Enable cluster sniffing
------------------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+----------------------------------------------------------------+--------------------------------------------------------------------------+
| Automatically find and connect to all data nodes in a cluster. | - System Config path: **Environment > Elasticsearch**                    |
|                                                                | - ``config.json`` setting: ``".Elasticsearchsettings.Sniff: false",``    |
| - **true**: Sniffing finds and connects to all data nodes      | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_SNIFF``               |
|   in your cluster automatically.                               |                                                                          |
| - **false**: **(Default)** Cluster sniffing is disabled .      |                                                                          |
+----------------------------------------------------------------+--------------------------------------------------------------------------+
| Select the **Test Connection** button in the System Console to validate the connection between Mattermost and the Elasticsearch server.   |
+----------------------------------------------------------------+--------------------------------------------------------------------------+

Bulk indexing
-------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Start a bulk index of all existing posts in the database.     | - System Config path: **Environment > Elasticsearch**                    |
|                                                               | - ``config.json`` setting: N/A                                           |
| Select the **Index Now** button in the System Console to      | - Environment variable: N/A                                              |
| start a bulk index of all posts. If the indexing process is   |                                                                          |
| canceled, the index and search results will be incomplete.    |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Purge indexes
-------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+-------------------------------------------------------------+
| Purge the entire Elasticsearch index.                         | - System Config path: **Environment > Elasticsearch**       |        
| Typically only used if the index has corrupted and search     | - ``config.json`` setting: N/A                              |
| isn't behaving as expected.                                   | - Environment variable: N/A                                 |          
|                                                               |                                                             |
| Select the **Purge Indexes** button in the System Console to  |                                                             |
| purge the index. After purging the index, create a new        |                                                             |
| index with the **Index Now** button.                          |                                                             |
+---------------------------------------------------------------+-------------------------------------------------------------+

Enable Elasticsearch for search queries
---------------------------------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------------+
| Use the latest index for all search queries.                  | - System Config path: **Environment > Elasticsearch**                          |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.EnableSearching:false",`` |
| - **true**: Elasticsearch will be used for all search         | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_ENABLESEARCHING``           | 
|   queries using the latest index. Search results may be       |                                                                                |
|   incomplete until a bulk index of the existing post database |                                                                                |
|   is finished.                                                |                                                                                |
| - **false**: **(Default)** Database search is used for        |                                                                                |
|   search queries.                                             |                                                                                |
+---------------------------------------------------------------+--------------------------------------------------------------------------------+

Enable Elasticsearch for autocomplete queries
---------------------------------------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+------------------------------------------------------------------------------------+
| Elasticsearch can use the latest index for all autocompletion | - System Config path: **Environment > Elasticsearch**                              |
| queries on users and channels.                                | - ``config.json`` setting: ``".Elasticsearchsettings.EnableAutocomplete: false",`` |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_ENABLEAUTOCOMPLETE``            |
| - **true**: Elasticsearch will be used for all autocompletion |                                                                                    |
|   queries on users and channels using the latest index.       |                                                                                    |
| - **false**: **(Default)** Database autocomplete is used.     |                                                                                    |
+---------------------------------------------------------------+------------------------------------------------------------------------------------+
| **Note**: Autocompletion results may be incomplete until a bulk index of the existing users and channels database is finished.                     |
+---------------------------------------------------------------+------------------------------------------------------------------------------------+

Post index replicas
-------------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The number of replicas to use for each post index.            | - System Config path: N/A                                                     |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.PostIndexReplicas: 1",`` |
| Numerical input. Default is 1.                                | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_POSTINDEXREPLICAS``        |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Important**: If this setting is changed, the changed configuration only applies to newly-created indexes. To apply the change to            | 
| existing indexes, purge and rebuild the index after changing this setting.                                                                    |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

Post index shards
-----------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The number of shards to use for each post index.              | - System Config path: N/A                                                     |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.PostIndexShards: 1",``   |
| Numerical input. Default is 1.                                | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_POSTINDEXSHARDS``          |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Important**: If this setting is changed, the changed configuration only applies to newly-created indexes. To apply the change to            | 
| existing indexes, purge and rebuild the index after changing this setting.                                                                    |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

Channel index replicas
-----------------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+----------------------------------------------------------------------------------+
| The number of replicas to use for each channel index.         | - System Config path: N/A                                                        |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.ChannelIndexReplicas: 1",`` |
| Numerical input. Default is 1.                                | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CHANNELINDEXREPLICAS``        |
+---------------------------------------------------------------+----------------------------------------------------------------------------------+

Channel index shards
--------------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+----------------------------------------------------------------------------------+
| The number of shards to use for each channel index.           | - System Config path: N/A                                                        |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.ChannelIndexShards: 1",``   |
| Numerical input. Default is 1.                                | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CHANNELINDEXSHARDS``          |
+---------------------------------------------------------------+----------------------------------------------------------------------------------+

User index replicas
-------------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The number of replicas to use for each user index.            | - System Config path: N/A                                                     |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.UserIndexReplicas: 1",`` |
| Numerical input. Default is 1.                                | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_USERINDEXREPLICAS``        |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

User index shards
-----------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+----------------------------------------------------------------------------------+
| The number of shards to use for each user index.              | - System Config path: N/A                                                        |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.UserIndexShards: 1",``      |
| Numerical input. Default is 1.                                | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_USERINDEXSHARDS``             |
+---------------------------------------------------------------+----------------------------------------------------------------------------------+

Aggregate search indexes
-------------------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Elasticsearch indexes older than the age specified by this    | - System Config path: N/A                                                              |
| setting, in days, will be aggregated during the daily         | - ``config.json`` setting: ``".Elasticsearchsettings.AggregatePostsAfterDays: 365",``  |
| scheduled job.                                                | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_AGGREGATEPOSTSAFTERDAYS``           |
|                                                               |                                                                                        |
| Numerical input. Default is 365 days.                         |                                                                                        |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
| **Note**: If you’re using `data retention <https://docs.mattermost.com/comply/data-retention-policy.html>`__ and                                       |
| `Elasticsearch <https://docs.mattermost.com/scale/elasticsearch.html>`__, configure this with a value greater than your data retention policy.         |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------+

Post aggregator start time
--------------------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| The start time of the daily scheduled aggregator job.         | - System Config path: N/A                                                                   |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.PostsAggregatorJobStartTime: "03:00"`` | | Must be a 24-hour time stamp in the form ``HH:MM`` based  on  | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_POSTSAGGREGATORJOBSTARTTIME``            |
| the local time of the server.                                 |                                                                                             |
|                                                               |                                                                                             |
| Default is 03:00 (3 a.m.).                                    |                                                                                             |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+

Index prefix
------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Prefix added to the Elasticsearch index name.                 | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.IndexPrefix",``     |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_INDEXPREFIX``         |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: When this setting is used, all Elasticsearch indexes created by Mattermost are given this prefix. You can set different        |
| prefixes so that multiple Mattermost deployments can share an Elasticsearch cluster without the index names colliding.                   |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Live indexing batch size
------------------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+-----------------------------------------------------------------------------------+
| Determines how many new posts are batched together before     | - System Config path: N/a                                                         |
| they are added to the Elasticsearch index.                    | - ``config.json`` setting: ``".Elasticsearchsettings.LiveIndexingBatchSize: 1",`` |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_LIVEINDEXINGBATCHSIZE``        |
| Numerical input. Default is 1.                                |                                                                                   |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------+
| **Note**: It may be necessary to increase this value to avoid hitting the rate limit of your Elasticsearch cluster on installs handling           | 
| multiple messages per second.                                                                                                                     |    
+---------------------------------------------------------------+-----------------------------------------------------------------------------------+

Bulk indexing time window
-------------------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Determines the maximum time window for a batch of posts       | - System Config path: **Environment > Elasticsearch**                                        |
| being indexed by the Bulk Indexer. This setting serves as a   | - ``config.json`` setting: ``".Elasticsearchsettings.BulkIndexingTimeWindowSeconds: 3600",`` |
| performance optimization for installs with over ~10 million   | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_BULKINDEXINGTIMEWINDOWSECONDS``           |
| posts in the database.                                        |                                                                                              |
|                                                               |                                                                                              |
| Numerical input in seconds. Default is 3600 seconds (1 hour). |                                                                                              |
| Approximate this value based on the average number of seconds |                                                                                              |
| for 2,000 posts to be added to the database on a typical      |                                                                                              |
| day in production.                                            |                                                                                              |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| **Note**: Setting this value too low will cause Bulk Indexing jobs to run slowly.                                                                            |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------------+

Request timeout
---------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+------------------------------------------------------------------------------------+
| Timeout in seconds for Elasticsearch calls.                   | - System Config path: N/A                                                          |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.RequestTimeoutSeconds:30",``  |
| Numerical input in seconds. Default is 30 seconds.            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_REQUESTTIMEOUTSECONDS``         |
+---------------------------------------------------------------+------------------------------------------------------------------------------------+

Trace
-----

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

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