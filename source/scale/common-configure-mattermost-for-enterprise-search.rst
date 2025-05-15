.. meta::
   :name: robots
   :content: noindex

:orphan:
:nosearch:

.. This page intentionally not accessible via the LHS navigation pane because it's included in other pages

Set server connection details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. (Optional) Enter **Server Username** used to access the enterprise search server.
2. (Optional) Enter **Server Password** associated with the username.
3. Set **Enable Cluster Sniffing** (Optional). Sniffing finds and connects to all data nodes in your cluster automatically.
4. Optional CA and client certificate configuration settings are available for use with basic authentication credentials or to replace them. See the :ref:`Enterprise search configuration settings <configure/environment-configuration-settings:enterprise search>` documentation for details.
5. Select **Test Connection** and then select **Save**. If the server connection is unsuccessful you won't be able to save the configuration or enable searching with Elasticsearch or AWS OpenSearch.

Build the post index of existing messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select **Index Now**. This process can take up to a few hours depending on the size of the post database and number of messages. The progress percentage can be seen as the index is created. To avoid downtime, set **Enable Elasticsearch for search queries** to ``false`` so that database search is available during the indexing process.

Enable enterprise search
~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure bulk indexing is complete before enabling enterprise search, otherwise search results will be incomplete.

Set **Enable Elasticsearch for search queries** to ``true``, and setting **Enable Elasticsearch for autocomplete** to ``true``. Save your configuration updates and restart the Mattermost server.

.. note::

  For high post volume deployments, we strongly encourage you to read and properly configure the Mattermost :ref:`LiveIndexingBatchSize <configure/environment-configuration-settings:live indexing batch size>` configuration setting.

Once the configuration is saved, new posts made to the database are automatically indexed on the Elasticsearch or AWS OpenSearch server.

Enterprise search limitations
-------------------------------

1. Elasticsearch and AWS OpenSearch uses a standard selection of "stop words" to keep search results relevant. Results for the following words will not be returned: "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", and "with".
2. Searching stop words in quotes returns more results than just the searched terms (`ticket <https://mattermost.atlassian.net/browse/MM-7216>`__).
3. Search results are limited to a user's team and channel membership. This is enforced by the Mattermost server. The entities are indexed in Elasticsearch or AWS OpenSearch in a way that allows Mattermost to filter them when querying, so the Mattermost server narrows down the results on every Elasticsearch or AWS OpenSearch request applying those filters.