Elasticsearch
=============

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Mattermost Enterprise Edition E20*

Elasticsearch provides enterprise-scale deployments with optimized search performance and prevents performance degradation and timeouts. The implementation uses `Elasticsearch <https://www.elastic.co>`__ v7.x as a distributed, RESTful search engine supporting highly efficient database searches in a `cluster environment </scale/high-availability-cluster.html>`__. 

.. important::
  
  - The default Mattermost database search starts to show performance degradation at around 2 million posts, on a server with 32 GB RAM and 4 CPUs. We recommend using Elasticsearch for optimum search performance. If you anticipate your Mattermost server reaching more than 2.5 million posts, we recommend enabling Elasticsearch for optimum search performance before you reach 3 million posts. 
  - For deployments with over 5 million posts, Elasticsearch is required to avoid significant performance issues (such as timeouts) with search and at-mentions.
  - We highly recommend that you install Elasticsearch on a different machine than the Mattermost Server. 
    
Deployment guide
----------------

Elasticsearch allows you to search large volumes of data quickly, in near real-time, by creating and managing an index of post data. The indexing process can be managed from the System Console after setting up and connecting an Elasticsearch server. The post index is stored on the Elasticsearch server and updated constantly after new posts are made. In order to index existing posts, a bulk index of the entire post database must be generated.

Deploying Elasticsearch includes the following two steps: `setting up the Elasticsearch server <#set-up-an-elasticsearch-server>`_, and `configuring Elasticsearch in Mattermost <#configure-elasticsearch-in-mattermost>`_.
    
Set up an Elasticsearch server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Download and install the latest release of Elasticsearch v7. See the `Elasticsearch <https://www.elastic.co/guide/en/elasticsearch/reference/7.17/install-elasticsearch.html>`__ documentation for details. 

2. Set up Elasticsearch with systemd by running the following commands:

  .. code-block:: none

    sudo /bin/systemctl daemon-reload
    sudo /bin/systemctl enable elasticsearch.service
    sudo systemctl start elasticsearch.service

3. Confirm Elasticsearch is working on the server by running the following command:

  .. code-block:: none

    curl localhost:9200

4. Get your network interface name by running the following command:

  .. code-block:: none

    ip addr

5. Edit the Elasticsearch configuration file in vi by running the following command:

  .. code-block:: none

    vi /etc/elasticsearch/elasticsearch.yml

6. In this file, replace the ``network.host`` value of ``_eth0_`` with your network interface name, and save your changes.

7. Restart Elasticsearch by running the following commands:

  .. code-block:: none

    sudo systemctl stop elasticsearch
    sudo systemctl start elasticsearch

8. Confirm the ports are listenings by running the following command:

  .. code-block:: none

    netstat -plnt

  You should see the following ports, including  the ones listening on ports 9200 and 9300. Confirm these are listening on your server's IP address. 

9. Create an Elasticsearch directory and give it the proper permissions.

10. Install the `icu-analyzer plugin <https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu.html>`__ to the ``/usr/share/elasticsearch/plugins`` directory by running the following command:

  .. code-block:: none

    sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu

11. Test the connection from Mattermost to Elasticsearch by running the following command:

  .. code-block:: none

    curl 172.31.80.220:9200

Configure Elasticsearch in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow these steps to configure Mattermost to use your Elasticsearch server, and to generate the post index.

.. tip::

    Advanced Elasticsearch configuration settings for large deployments can be configured outside the System Console in the ``config.json`` file. See the `Elasticsearch configuration settings </configure/configuration-settings.html#elasticsearch>`__ documentation to learn more. 

1. Go to **System Console > Environment > Elasticsearch**.
2. Set **Enable Elasticsearch Indexing** to ``true`` to enable the other the settings on the page. Once the configuration is saved, new posts made to the database are automatically indexed on the Elasticsearch server.
3. Set the Elasticsearch server connection details:

  a. Enter **Server Connection Address** for the Elasticsearch server you set up earlier.
  b. (Optional) Enter **Server Username** used to access the Elasticsearch server. For AWS Elasticsearch, leave this field blank.
  c. (Optional) Enter **Server Password** associated with the username. For AWS Elasticsearch, leave this field blank.
  d. Set **Enable Cluster Sniffing** (Optional). Sniffing finds and connects to all data nodes in your cluster automatically. For AWS Elasticsearch, this field should be set to ``false``.

.. tip::

  From Mattermost v7.8, optional CA and client certificate configuration settings are available for use with basic auth credentials or to replace them. See the `Elasticsearch configuration settings </configure/environment-configuration-settings.html#elasticsearch>`__ documentation for details.

4. Select **Test Connection** and then select **Save**. If the server connection is unsuccessful you won't be able to save the configuration or enable searching with Elasticsearch.

5. Select **Build Index** to build the post index of existing posts. This process can take up to a few hours depending on the size of the post database and number of messages. The progress percentage can be seen as the index is created. To avoid downtime, set **Enable Elasticsearch for search queries** to ``false`` so that database search is available during the indexing process.

  .. important::

    Complete bulk indexing before enabling Elasticsearch in the next step. Otherwise, search results will be incomplete.

6. Enable Elasticsearch by setting **Enable Elasticsearch for search queries** to ``true``, and setting **Enable Elasticsearch for autocomplete** to ``true``. 

7. Save your configuration updates and restart the Mattermost server.

.. note::

   - Additional advanced Elasticsearch settings for large deployments can be configured outside the System Console in the ``config.json`` file. Read the `Elasticsearch configuration settings </configure/configuration-settings.html#elasticsearch>`__ documentation to learn more.
   - If your deployment has a large number of posts (typically in excess of one million but not strictly defined), the reindexing progress percentage may stay at 99% for a long time. The size of the data to be indexed is estimated, and on large databases, estimations can become inaccurate. While progress estimates may be inaccurate, and the progress percentage may appear stuck at near completion, indexing will continue behind the scenes until complete.
   - Search results for files shared before upgrading to Mattermost Server v5.35 may be incomplete until an extraction command is run using the `mmctl </manage/mmctl-command-line-tool.html#mmctl-extract>`__. After running this command, the search index must be rebuilt. Go to **System Console > Environment > Elasticsearch > Bulk Indexing**, then select **Index Now** to rebuild the search index to include older file contents.
   - For high post volume deployments it is strongly encouraged to read and properly configure the `LiveIndexingBatchSize </configure/environment-configuration-settings.html#live-indexing-batch-size>`__     
    
Limitations
------------

1. Elasticsearch uses a standard selection of "stop words" to keep search results relevant. Results for the following words will not be returned: "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", and "with".
2. Searching stop words in quotes returns more results than just the searched terms (`ticket <https://mattermost.atlassian.net/browse/MM-7216>`__).
3. AWS Elasticsearch implementations have a limit of 1000 days of post history that is searchable.
4. Search results are limited to a user's team and channel membership. This is enforced by the Mattermost server. The entities are indexed in Elasticsearch in a way that allows Mattermost to filter them when querying, so the Mattermost server narrows down the results on every Elasticsearch request applying those filters.

Frequently asked questions (FAQ)
--------------------------------

Do I need to use Elasticsearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Elasticsearch engine is designed for large Enterprise deployments to run highly efficient database searches in a cluster environment. The default Mattermost database search starts to show performance degradation at around 2.5 million posts, depending on the specifications for the database server. If you expect your Mattermost server to have more than 2.5 million posts, we recommend using Elasticsearch for optimum search performance.

Should I install Elasticsearch on the same machine as Mattermost Server?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. We strongly recommend that you install Elasticsearch on a different machine than the Mattermost Server.

What types of indexes are created?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost creates three types of indexes: users, channels, and posts. Users and channels have one index each. Posts are aggregated by date, into multiple indexes.

Can I pause an Elasticsearch indexing job?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. From Mattermost v.6.7, the Elasticsearch indexing job is resumable. Stopping a server while the Elasticsearch indexing job is running puts the job in pending status. The job resumes when the server restarts. System Admins can cancel an indexing job through the System Console.

Can an index rollover policy be defined?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `AggregatePostsAfterDays </configure/configuration-settings.html#aggregate-search-indexes>`__ configuration setting defines a cutoff value. All posts preceding this value are reindexed and aggregated into new and bigger indexes. The default setting is 365 days.

Are there any new search features offered with Elasticsearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The current implementation of Elasticsearch matches the search features currently available with database search. The Mattermost team is working on extending the Elasticsearch feature set with file name and content search, date filters, and operators and modifiers.

Are my files stored in Elasticsearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, files and attachments are not stored.

How do I monitor system health of an Elasticsearch server?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use this Prometheus exporter to monitor `various metrics <https://github.com/justwatchcom/elasticsearch_exporter#metrics>`__ about Elasticsearch: `justwatchcom/elasticsearch_exporter <https://github.com/justwatchcom/elasticsearch_exporter>`__.

You can also refer to this `article about Elasticsearch performance monitoring <https://www.datadoghq.com/blog/monitor-elasticsearch-performance-metrics/#key-elasticsearch-performance-metrics-to-monitor>`__. It's not written specifically for Prometheus, which `Mattermost's performance monitoring </scale/performance-monitoring.html>`__ system uses, but has several tips and best practices.
 
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
