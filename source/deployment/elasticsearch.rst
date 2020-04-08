Elasticsearch (E20)
===================

*Available in Enterprise Edition E20.*

`Elasticsearch <https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html>`__ is a distributed, RESTful search engine supporting highly efficient database searches in a `cluster environment <https://docs.mattermost.com/deployment/cluster.html>`__.

.. toctree::
    :maxdepth: 2
    
Deployment Guide
----------------

Overview
~~~~~~~~

Elasticsearch allows you to search large volumes of data quickly, in near real time, by creating and managing an index of post data. The indexing process can be managed from the System Console after setting up and connecting an Elasticsearch server. The post index is stored on the Elasticsearch server and is updated constantly after new posts are made. In order to index existing posts, a bulk index of the entire post database must be generated. 

Elasticsearch v5.x and v6.x are supported.

When to Use Elasticsearch
~~~~~~~~~~~~~~~~~~~~~~~~~

The default Mattermost database search starts to show performance degradation at around 2.5 million posts, depending on the specifications for the database server. If you expect your Mattermost server to have more than 2.5 million posts, we recommend using Elasticsearch for optimum search performance.

Setting Up an Elasticsearch Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The set up process for the Elasticsearch server is documented in the `official Elasticsearch documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html>`__. 

.. Note::
  You must install the `ICU Analyzer Plugin <https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu.html>`__ when setting up Elasticsearch for Mattermost.


Configuring Elasticsearch in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow these steps to connect your Elasticsearch server to Mattermost and generate the post index.

1. Open **System Console > Environment > Elasticsearch** (or **System Console > Advanced > Elasticsearch** in versions prior to 5.12).
2. Set **Enable Elasticsearch Indexing** to ``true`` to enable the other the settings on the page. Once the configuration is saved, new posts made to the database will be automatically indexed on the Elasticsearch server.
3. Set the Elasticsearch server connection details:
  a) Enter **Server Connection Address** for the Elasticsearch server you set up earlier.
  b) (Optional) Enter **Server Username** used to access the Elasticsearch server.
    - Note: For AWS Elasticsearch leave this field blank.
  c) (Optional) Enter **Server Password** associated with the username.
    - Note: For AWS Elasticsearch leave this field blank.
  d) Set **Enable Cluster Sniffing** (Optional). Sniffing finds and connects to all data nodes in your cluster automatically.
    - Note: For AWS Elasticsearch this field should be set to ``false``.
4. Click **Test Connection** and **Save** the configuration.
  - If the server connection is unsuccessful you will not be able to save the configuration or enable searching with Elasticsearch.
5. Build the post index of existing posts by clicking **Build Index**.
  - This process can take up to a few hours depending on the size of the post database and number of messages. The progress percentage can be seen as the index is created. To avoid downtime set **Enable Elasticsearch for search queries** to ``false`` so that database search is available during the indexing process.
6. Enable Elasticsearch by setting **Enable Elasticsearch for search queries** to ``true``.
  - Note: It is recommended that bulk indexing be completed before enabling Elasticsearch, otherwise search results will be incomplete. When this setting is ``false``, database search is used for all search queries.
7. Restart the Mattermost server.

 .. Note::
    Additional advanced Elasticsearch settings for large deployments can be configured outside the System Console in the ``config.json`` file. Please see `documentation to learn more <https://docs.mattermost.com/administration/config-settings.html#elasticsearch>`__.

Limitations
------------

1. Elasticsearch uses a standard selection of "stop words" to keep search results relevant. Results for the following words will not be returned: 

  - "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", "with"  

2. Searching stop words in quotes returns more results than just the searched terms (`ticket <https://mattermost.atlassian.net/browse/MM-7216>`__).

3. AWS Elasticsearch implementations have a limit of 1000 days of post history that is searchable.

4. Search results are limited to a user's team and channel membership. This is enforced by the Mattermost server. The entities are indexed in Elasticsearch in a way that allows Mattermost to filter them when querying, so the Mattermost server narrows down the results on every Elasticsearch request applying those filters.


Frequently Asked Questions (FAQ)
--------------------------------

Do I need to use Elasticsearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Elasticsearch engine is designed for large Enterprise deployments wanting to run highly efficient database searches in a cluster environment.

What types of indexes are created? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Mattermost creates three types of indexes: users, channels, and posts. Users and channels have one index each. Posts are aggregated by date, into multiple indexes. 

Can an index rollover policy be defined? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The `AggregatePostsAfterDays <https://docs.mattermost.com/administration/config-settings.html#aggregate-search-indexes>`__ configuration setting defines a cutoff value. All posts preceding this value are reindexed and aggregated into new and bigger indexes. The default setting is 365 days. 

Are there any new search features offered with Elasticsearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The current implementation of Elasticsearch matches the search features currently available with database search. The Mattermost team is working on extending the Elasticsearch feature set with file name and content search, date filters, and operators, and modifiers.

Are my files stored in Elasticsearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
No, files and attachments are not stored. 

How do I monitor system health of an Elasticsearch server?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can use this Prometheus exporter to monitor `various metrics <https://github.com/justwatchcom/elasticsearch_exporter#metrics>`__ about Elasticsearch: `justwatchcom/elasticsearch_exporter <https://github.com/justwatchcom/elasticsearch_exporter>`__

You may also refer to this `article about Elasticsearch performance monitoring <https://www.datadoghq.com/blog/monitor-elasticsearch-performance-metrics/#key-elasticsearch-performance-metrics-to-monitor>`__. It is not written specifically for Prometheus, which `Mattermost's performance monitoring <https://docs.mattermost.com/deployment/metrics.html>`__ system uses, but has several tips and best practices.

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost provides the status of each Elasticsearch indexing job in **System Console > Environment > Elasticsearch** (or **System Console > Advanced > Elasticsearch** in versions prior to 5.12). Here you can see if the job succeeded or failed, including the details of the error.

Failures are returned in the server logs. The error log begins with the string ``Failed job`` and includes a job_id key/value pair. Elasticsearch job failures are identified with worker name ``EnterpriseElasticsearchAggregator`` and ``EnterpriseElasticsearchIndexer``. You can optionally create a script that programmatically queries for such failures and notifies the appropriate system.
