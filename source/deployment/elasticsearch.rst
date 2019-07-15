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

Elasticsearch allows you to search large volumes of data quickly, and in near real time, by creating and managing an index of post data. The indexing process can be managed from the System Console after setting up and connecting an Elasticsearch server. The post index is stored on the Elasticsearch server and is updated constantly after new posts are made. In order to index existing posts, a bulk index of the entire post database must be generated. 

When to use Elasticsearch
~~~~~~~~~~~~~~~~~~~~~~~~~

The default Mattermost database search starts to show performance degradation at around 2.5 million posts, depending on the specifications for the database server. If you expect your Mattermost server to have more than 2.5 million posts, we recommend using Elasticsearch for optimum search performance.

Setting up an Elasticsearch Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The setup process for the Elasticsearch server is documented in the `official Elasticsearch documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html>`__. Elasticsearch v5.0 and later is supported.

.. note::
  You must install the `ICU Analyzer Plugin <https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu.html>`__ when setting up Elasticsearch for Mattermost.

Configuring Elasticsearch in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow these steps to connect your Elasticsearch server to Mattermost and generate the post index.

1. Open **System Console** > **Advanced** > **Elasticsearch** in prior versions or **System Console** > **Environment** > **Elasticsearch** in versions after 5.12.
2. Set **Enable Elasticsearch Indexing** to `true` to enable the other the settings on the page. Once the configuration is saved, new posts made to the database will be automatically indexed on the Elasticsearch server.
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
  - This process can take up to a few hours depending on the size of the post database and number of messages. The progress percentage can be seen as the index is created. Indexing does not require downtime as database search is available during the indexing process if **Enable Elasticsearch for search queries** is set to ``false``.
6. Enable Elasticsearch by setting **Enable Elasticsearch for search queries** to ``true``.
  - Note: It is recommended that bulk indexing be completed before enabling Elasticsearch, otherwise search results will be incomplete. When this setting is ``false``, database search is used for all search queries.
7. Restart the Mattermost server.

 .. note::
    Additional advanced Elasticsearch settings for large deployments can be configured outside the System Console in the `config.json`. Please see `documentation to learn more <https://docs.mattermost.com/administration/config-settings.html#elasticsearch>`__.

Limitations
------------

1. Elasticsearch uses a standard selection of "stop words" to keep search results relevant. Results for the following words will not be returned: 

  - "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", "with"  

2. Searching stop words in quotes returns more results than just the searched terms (`ticket <https://mattermost.atlassian.net/browse/PLT-7314>`__).
3. AWS Elasticsearch implementations have a limit of 1000 days of post history that is searchable.

Frequently Asked Questions (FAQ)
--------------------------------

Do I need to use Elasticsearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Elasticsearch engine is designed for large Enterprise deployments wanting to run highly efficient database searches in a cluster environment.

Are there any new search features offered with Elasticsearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The current implementation of Elasticsearch matches the search features currently available with database search. The Mattermost team is working on extending the Elasticsearch feature set with file name and content search, date filters, and operators and modifiers.

How do I monitor system health of an Elasticsearch server?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can use this Prometheus exporter to monitor `various metrics <https://github.com/justwatchcom/elasticsearch_exporter#metrics>`__ about Elasticsearch: `justwatchcom/elasticsearch_exporter <https://github.com/justwatchcom/elasticsearch_exporter>`__

You may also refer to this excellent `article about Elasticsearch performance monitoring <https://www.datadoghq.com/blog/monitor-elasticsearch-performance-metrics/#key-elasticsearch-performance-metrics-to-monitor>`__. It is not written specifically for Prometheus which `Mattermost's performance monitoring <https://docs.mattermost.com/deployment/metrics.html>`__ system uses, but has several tips and best practices.

Why does a 25,000 post database take a long time to index in Elasticsearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
There's a few possible reasons why it might be slow:

 - Querying the posts out of the database is resource limited (i.e. the machine the database is on is not powerful enough).

 - The Elasticsearch cluster is performance limited (i.e. the machines are not powerful enough).

 - The 25,000 messages are spread out over a long time window, and the ``BulkIndexingTimeWindowSeconds`` configuration value is too low for efficient indexing of such a "sparse" database. Optimally the value of that config should be set such that the median number of posts falling within any period of that time in the database is around 700 to 800. The default value is 1 hour, so if you are doing a lot less than 800 posts an hour on average, then the indexing will be much slower in terms of "posts per unit time". This can be sped up by increasing that time window.

How do I know if an elasticsearch job fails?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost provides the status of each elasticsearch indexing job in **System Console** > **Environment** > **Elasticsearch** (or **System Console > Advanced > Elasticsearch** in versions 5.11 and earlier). Here, you can see if the job succeeded or failed, including the details of the error.

Morever, any failures are returned in the server logs. The error log begins with the string ``Failed job`` and includes a job_id key/value pair. Elasticsearch job failures are identified with worker name ``EnterpriseElasticsearchAggregator`` and ``EnterpriseElasticsearchIndexer``. You can optionally create a script that programmatically queries for such failures and notifies the appropriate system.

