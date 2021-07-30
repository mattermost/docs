Elasticsearch (E20)
===================

*Available in Mattermost Enterprise Edition E20*

Elasticsearch provides enterprise-scale deployments with optimized search performance and prevents performance degradation and timeouts.

The implementation uses `Elasticsearch <https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html>`__ as a distributed, RESTful search engine supporting highly efficient database searches in a `cluster environment <https://docs.mattermost.com/deployment/cluster.html>`__. Elasticsearch v5.x, v6.x, and v7.x are supported. 
    
Deployment Guide
----------------

Elasticsearch allows you to search large volumes of data quickly, in near real-time, by creating and managing an index of post data. The indexing process can be managed from the System Console after setting up and connecting an Elasticsearch server. The post index is stored on the Elasticsearch server and is updated constantly after new posts are made. In order to index existing posts, a bulk index of the entire post database must be generated.

.. important::
    The default Mattermost database search starts to show performance degradation at around 2.5 million posts, depending on the specifications for the database server. If you expect your Mattermost server to have more than 2.5 million posts, we recommend using Elasticsearch for optimum search performance. For deployments with over 5 million posts, Elasticsearch is required to avoid significant performance issues (such as timeouts) with search and at-mentions.

.. note::
    From Mattermost v5.26, you can filter inactive users, search by user role, and also search for terms inside links. This update introduces a breaking change which affects the "from" part of the search. To avoid this, reindex your Elasticsearch instance/cluster prior to upgrading.
    
Setting Up an Elasticsearch Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The set up process for the Elasticsearch server is documented in the `official Elasticsearch documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html>`__.

.. note::
  You must install the `ICU Analyzer Plugin <https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu.html>`__ when setting up Elasticsearch for Mattermost.

Configuring Elasticsearch in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow these steps to connect your Elasticsearch server to Mattermost and to generate the post index.

1. Go to **System Console > Environment > Elasticsearch**.
2. Set **Enable Elasticsearch Indexing** to ``true`` to enable the other the settings on the page. Once the configuration is saved, new posts made to the database will be automatically indexed on the Elasticsearch server.
3. Set the Elasticsearch server connection details:
  a) Enter **Server Connection Address** for the Elasticsearch server you set up earlier.
  b) (Optional) Enter **Server Username** used to access the Elasticsearch server.
    - Note: For AWS Elasticsearch leave this field blank.
  c) (Optional) Enter **Server Password** associated with the username.
    - Note: For AWS Elasticsearch leave this field blank.
  d) Set **Enable Cluster Sniffing** (Optional). Sniffing finds and connects to all data nodes in your cluster automatically.
    - Note: For AWS Elasticsearch this field should be set to ``false``.
4. Select **Test Connection** and **Save** the configuration.
  - If the server connection is unsuccessful you will not be able to save the configuration or enable searching with Elasticsearch.
5. Select **Build Index** to build the post index of existing posts.
  - This process can take up to a few hours depending on the size of the post database and number of messages. The progress percentage can be seen as the index is created. To avoid downtime set **Enable Elasticsearch for search queries** to ``false`` so that database search is available during the indexing process.
6. Enable Elasticsearch by setting **Enable Elasticsearch for search queries** to ``true``.
  - **Note:** Complete bulk indexing before enabling Elasticsearch. Otherwise, search results will be incomplete. When this setting is ``false``, database search is used for all search queries.
7. Restart the Mattermost server.

.. note::

   - Additional advanced Elasticsearch settings for large deployments can be configured outside the System Console in the ``config.json`` file. Read the `documentation to learn more <https://docs.mattermost.com/administration/config-settings.html#elasticsearch>`__.
   - If your deployment has a large number of posts (typically in excess of one million but not strictly defined), the reindexing progress percentage may stay at 99% for a long time. The size of the data to be indexed is estimated, and on large databases, estimations can become inaccurate. While progress estimates may be inaccurate, and the progress percentage may appear stuck at near completion, indexing will continue behind the scenes until complete.
   - Search results for files shared before upgrading to Mattermost Server 5.35 may be incomplete until an `extraction command <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-extract-documents-content>`__ is executed using the CLI. After running this command, the search index must be rebuilt. Go to **System Console > Environment > Elasticsearch > Bulk Indexing**, then select **Index Now** to rebuild the search index to include older file contents.
    
Limitations
------------

1. Elasticsearch uses a standard selection of "stop words" to keep search results relevant. Results for the following words will not be returned: "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", and "with".
2. Searching stop words in quotes returns more results than just the searched terms (`ticket <https://mattermost.atlassian.net/browse/MM-7216>`__).
3. AWS Elasticsearch implementations have a limit of 1000 days of post history that is searchable.
4. Search results are limited to a user's team and channel membership. This is enforced by the Mattermost server. The entities are indexed in Elasticsearch in a way that allows Mattermost to filter them when querying, so the Mattermost server narrows down the results on every Elasticsearch request applying those filters.

Frequently Asked Questions (FAQ)
--------------------------------

Do I need to use Elasticsearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Elasticsearch engine is designed for large Enterprise deployments to run highly efficient database searches in a cluster environment. The default Mattermost database search starts to show performance degradation at around 2.5 million posts, depending on the specifications for the database server. If you expect your Mattermost server to have more than 2.5 million posts, we recommend using Elasticsearch for optimum search performance.

What types of indexes are created?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost creates three types of indexes: users, channels, and posts. Users and channels have one index each. Posts are aggregated by date, into multiple indexes.

Can an index rollover policy be defined?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `AggregatePostsAfterDays <https://docs.mattermost.com/administration/config-settings.html#aggregate-search-indexes>`__ configuration setting defines a cutoff value. All posts preceding this value are reindexed and aggregated into new and bigger indexes. The default setting is 365 days.

Are there any new search features offered with Elasticsearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The current implementation of Elasticsearch matches the search features currently available with database search. The Mattermost team is working on extending the Elasticsearch feature set with file name and content search, date filters, and operators and modifiers.

Are my files stored in Elasticsearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, files and attachments are not stored.

How do I monitor system health of an Elasticsearch server?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use this Prometheus exporter to monitor `various metrics <https://github.com/justwatchcom/elasticsearch_exporter#metrics>`__ about Elasticsearch: `justwatchcom/elasticsearch_exporter <https://github.com/justwatchcom/elasticsearch_exporter>`__.

You can also refer to this `article about Elasticsearch performance monitoring <https://www.datadoghq.com/blog/monitor-elasticsearch-performance-metrics/#key-elasticsearch-performance-metrics-to-monitor>`__. It's not written specifically for Prometheus, which `Mattermost's performance monitoring <https://docs.mattermost.com/deployment/metrics.html>`__ system uses, but has several tips and best practices.

Why does a 25,000 post database take a long time to index in Elasticsearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a few possible reasons:

- Querying the posts out of the database is resource limited (i.e., the machine the database is on is not powerful enough).
- The Elasticsearch cluster is performance limited (i.e., the machines are not powerful enough).
- The 25,000 messages are spread out over a long time window, and the ``BulkIndexingTimeWindowSeconds`` configuration value is too low for efficient indexing of such a "sparse" database. The value of that config should ideally be set so that the median number of posts falling within any period of that time in the database is around 700 to 800. The default value is 1 hour, so if you are doing a lot less than 800 posts an hour on average, then the indexing will be much slower in terms of "posts per unit time". This can be sped up by increasing that time window.
 
What form of data is sent to Elasticsearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost communicates with Elasticsearch through its REST API using JSON messages for indexing and querying entities.

How much data is sent to Elasticsearch and when?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every time a message is published, a channel is created, or a user changes, (either because their properties change e.g.: change of the first name or because they join/leave a channel), the data associated with that event is sent to Elasticsearch.

If search via Elasticsearch is enabled, every search will generate a query. If autocompletion is enabled, every user or channel autocompletion associated with writing a message or user search will generate a query.

How do I know if an Elasticsearch job fails?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost provides the status of each Elasticsearch indexing job in **System Console > Environment > Elasticsearch**. Here you can see if the job succeeded or failed, including the details of the error.

Failures are returned in the server logs. The error log begins with the string ``Failed job`` and includes a job_id key/value pair. Elasticsearch job failures are identified with worker name ``EnterpriseElasticsearchAggregator`` and ``EnterpriseElasticsearchIndexer``. You can optionally create a script that programmatically queries for such failures and notifies the appropriate system.

My Elasticsearch indexes won't complete, what should I do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have an Elasticsearch indexing job that's paused, it's likely your Elasticsearch server has restarted. If you restart your Elasticsearch server, you must also restart Mattermost to ensure jobs are completed. If restarting the Mattermost server does not resolve the issue, please contact Mattermost support.
