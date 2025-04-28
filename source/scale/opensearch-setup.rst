AWS OpenSearch server setup
============================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

AWS OpenSearch Service allows you to search large volumes of data quickly, in near real-time, by creating and managing an index of post data. The indexing process can be managed from the System Console after setting up and connecting an OpenSearch server. The post index is stored on the OpenSearch server and updated constantly after new posts are made. In order to index existing posts, a bulk index of the entire post database must be generated.

Deploying AWS OpenSearch includes the following two steps: `setting up AWS OpenSearch <#set-up-aws-opensearch>`__, and `configuring Mattermost <#configure-mattermost>`_. 

Set up AWS OpenSearch
----------------------

From Mattermost v9.11, beta support is available for `AWS OpenSearch v1.x and v2.x <https://opensearch.org/>`_. We highly recommend that you set up an AWS OpenSearch server on a separate machine from the Mattermost server.

1. Download and install the latest release of AWS OpenSearch. See the `OpenSearch <https://docs.opensearch.org/docs/latest/install-and-configure/>`_ documentation for installation details.

<additional AWS OpenSearch setup instructions here>

Configure Mattermost
---------------------

Follow these steps to configure Mattermost to use AWS OpenSearch server and to generate the post index:

1. Go to **System Console > Environment > Elasticsearch**.
2. Set **Enable Elasticsearch Indexing** to ``true`` to enable the other the settings on the page. Once the configuration is saved, new posts made to the database are automatically indexed on the OpenSearch server.
3. Change the Mattermost ``ElasticsearchSettings.Backend`` configuration setting value to ``opensearch``.
4. Set the AWS OpenSearch server connection details:

  a. Enter **Server Connection Address** for the AWS OpenSearch server you set up earlier.
  b. (Optional) Enter **Server Username** used to access the OpenSearch server. For OpenSearch, leave this field blank.
  c. (Optional) Enter **Server Password** associated with the username. For OpenSearch, leave this field blank.
  d. Set **Enable Cluster Sniffing** (Optional). Sniffing finds and connects to all data nodes in your cluster automatically. For OpenSearch, this field should be set to ``false``.

.. tip::

  Optional CA and client certificate configuration settings are available for use with basic auth credentials or to replace them. See the :ref:`Elasticsearch configuration settings <configure/environment-configuration-settings:elasticsearch>` documentation for details.

5. Select **Test Connection** and then select **Save**. If the server connection is unsuccessful you won't be able to save the configuration or enable searching with OpenSearch.

6. Select **Build Index** to build the post index of existing posts. This process can take up to a few hours depending on the size of the post database and number of messages. The progress percentage can be seen as the index is created. To avoid downtime, set **Enable Elasticsearch for search queries** to ``false`` so that database search is available during the indexing process.

  .. important::

    Complete bulk indexing before enabling OpenSearch in the next step. Otherwise, search results will be incomplete.

7. Enable Elasticsearch by setting **Enable Elasticsearch for search queries** to ``true``, and setting **Enable Elasticsearch for autocomplete** to ``true``. 

8. Save your configuration updates and restart the Mattermost server.

.. note::

  - Additional advanced Elasticsearch settings for large deployments can be configured outside the System Console in the ``config.json`` file. Read the :ref:`Elasticsearch configuration settings <configure/environment-configuration-settings:elasticsearch>` documentation to learn more.
  - If your deployment has a large number of posts (typically in excess of one million but not strictly defined), the reindexing progress percentage may stay at 99% for a long time. The size of the data to be indexed is estimated, and on large databases, estimations can become inaccurate. While progress estimates may be inaccurate, and the progress percentage may appear stuck at near completion, indexing will continue behind the scenes until complete.
  - Search results for files shared before upgrading to Mattermost Server v5.35 may be incomplete until an extraction command is run using the :ref:`mmctl <manage/mmctl-command-line-tool:mmctl extract>`. After running this command, the search index must be rebuilt. Go to **System Console > Environment > Elasticsearch > Bulk Indexing**, then select **Index Now** to rebuild the search index to include older file contents.
  - For high post volume deployments, we strongly encourage you to read and properly configure the Mattermost :ref:`LiveIndexingBatchSize <configure/environment-configuration-settings:live indexing batch size>` configuration setting.
    
Limitations
------------

TBD