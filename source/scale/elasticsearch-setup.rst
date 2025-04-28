Elasticsearch server setup
===========================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Elasticsearch allows you to search large volumes of data quickly, in near real-time, by creating and managing an index of post data. The indexing process can be managed from the System Console after setting up and connecting an Elasticsearch server. The post index is stored on the Elasticsearch server and updated constantly after new posts are made. In order to index existing posts, a bulk index of the entire post database must be generated.

Deploying Elasticsearch includes the following two steps: `setting up Elasticsearch <#set-up-elasticsearch>`__, and `configuring Mattermost <#configure-mattermost>`_. 

Set up Elasticsearch
---------------------

We highly recommend that you set up Elasticsearch server on a dedicated machine separate from the Mattermost Server. 

1. Download and install the latest release of `Elasticsearch v8 <https://www.elastic.co/guide/en/elasticsearch/reference/8.15/install-elasticsearch.html>`_, or `Elasticsearch v7.17+ <https://www.elastic.co/guide/en/elasticsearch/reference/7.17/install-elasticsearch.html>`_. See the Elasticsearch documentation for installation details.

2. Set up Elasticsearch with ``systemd`` by running the following commands:

  .. code-block:: sh

    sudo /bin/systemctl daemon-reload
    sudo /bin/systemctl enable elasticsearch.service
    sudo systemctl start elasticsearch.service

3. Confirm Elasticsearch is working on the server by running the following command:

  .. code-block:: sh

    curl localhost:9200

4. Get your network interface name by running the following command:

  .. code-block:: sh

    ip addr

5. Edit the Elasticsearch configuration file in ``vi`` by running the following command:

  .. code-block:: sh

    vi /etc/elasticsearch/elasticsearch.yml

6. In this file, replace the ``network.host`` value of ``_eth0_`` with your network interface name, and save your changes.

7. Restart Elasticsearch by running the following commands:

  .. code-block:: sh

    sudo systemctl stop elasticsearch
    sudo systemctl start elasticsearch

8. Confirm the ports are listenings by running the following command:

  .. code-block:: sh

    netstat -plnt

  You should see the following ports, including  the ones listening on ports 9200 and 9300. Confirm these are listening on your server's IP address. 

9. Create an Elasticsearch directory and give it the proper permissions.

10. Install the `icu-analyzer plugin <https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu.html>`__ to the ``/usr/share/elasticsearch/plugins`` directory by running the following command:

  .. code-block:: sh

    sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu

11. Test the connection from Mattermost to Elasticsearch by running the following command:

  .. code-block:: sh

    curl 172.31.80.220:9200

Configure Mattermost
---------------------

Follow these steps to configure Mattermost to use your Elasticsearch server and to generate the post index:

.. tip::

    Advanced Elasticsearch configuration settings for large deployments can be configured outside the System Console in the ``config.json`` file. See the :ref:`Elasticsearch configuration settings <configure/environment-configuration-settings:elasticsearch>` documentation to learn more. 

1. Go to **System Console > Environment > Elasticsearch**.
2. Set **Enable Elasticsearch Indexing** to ``true`` to enable the other the settings on the page. Once the configuration is saved, new posts made to the database are automatically indexed on the Elasticsearch server.
3. Set the Elasticsearch server connection details:

  a. Enter **Server Connection Address** for the Elasticsearch server you set up earlier.
  b. (Optional) Enter **Server Username** used to access the Elasticsearch server. For AWS Elasticsearch, leave this field blank.
  c. (Optional) Enter **Server Password** associated with the username. For AWS Elasticsearch, leave this field blank.
  d. Set **Enable Cluster Sniffing** (Optional). Sniffing finds and connects to all data nodes in your cluster automatically. For AWS Elasticsearch, this field should be set to ``false``.

.. tip::

  From Mattermost v7.8, optional CA and client certificate configuration settings are available for use with basic auth credentials or to replace them. See the :ref:`Elasticsearch configuration settings <configure/environment-configuration-settings:elasticsearch>` documentation for details.

4. Select **Test Connection** and then select **Save**. If the server connection is unsuccessful you won't be able to save the configuration or enable searching with Elasticsearch.

5. Select **Build Index** to build the post index of existing posts. This process can take up to a few hours depending on the size of the post database and number of messages. The progress percentage can be seen as the index is created. To avoid downtime, set **Enable Elasticsearch for search queries** to ``false`` so that database search is available during the indexing process.

  .. important::

    Complete bulk indexing before enabling Elasticsearch in the next step. Otherwise, search results will be incomplete.

6. Enable Elasticsearch by setting **Enable Elasticsearch for search queries** to ``true``, and setting **Enable Elasticsearch for autocomplete** to ``true``. 

7. Save your configuration updates and restart the Mattermost server.

.. note::

   - Additional advanced Elasticsearch settings for large deployments can be configured outside the System Console in the ``config.json`` file. Read the :ref:`Elasticsearch configuration settings <configure/environment-configuration-settings:elasticsearch>` documentation to learn more.
   - If your deployment has a large number of posts (typically in excess of one million but not strictly defined), the reindexing progress percentage may stay at 99% for a long time. The size of the data to be indexed is estimated, and on large databases, estimations can become inaccurate. While progress estimates may be inaccurate, and the progress percentage may appear stuck at near completion, indexing will continue behind the scenes until complete.
   - Search results for files shared before upgrading to Mattermost Server v5.35 may be incomplete until an extraction command is run using the :ref:`mmctl <manage/mmctl-command-line-tool:mmctl extract>`. After running this command, the search index must be rebuilt. Go to **System Console > Environment > Elasticsearch > Bulk Indexing**, then select **Index Now** to rebuild the search index to include older file contents.
   - For high post volume deployments, we strongly encourage you to read and properly configure the Mattermost :ref:`LiveIndexingBatchSize <configure/environment-configuration-settings:live indexing batch size>` configuration setting.
    
Limitations
------------

1. Elasticsearch uses a standard selection of "stop words" to keep search results relevant. Results for the following words will not be returned: "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", and "with".
2. Searching stop words in quotes returns more results than just the searched terms (`ticket <https://mattermost.atlassian.net/browse/MM-7216>`__).
3. Search results are limited to a user's team and channel membership. This is enforced by the Mattermost server. The entities are indexed in Elasticsearch in a way that allows Mattermost to filter them when querying, so the Mattermost server narrows down the results on every Elasticsearch request applying those filters.