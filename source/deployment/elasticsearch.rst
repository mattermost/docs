Elasticsearch Beta (E20)
========================

*Available in Enterprise Edition E20.*

`Elasticsearch <https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html>`_ is a distributed, RESTful search engine capable of supporting search in large scale enterprise deployments with millions of messages. 

.. toctree::
    :maxdepth: 2

Deployment Guide
----------------

Overview
~~~~~~~~

Elasticsearch allows you to search large volumes of data quickly, and in near real time, by creating and managing an index of post data. The indexing process can be managed from the System Console after setting up and connecting an Elasticsearch server. The post index is stored on the Elasticsearch server and is updated constantly after new posts are made. In order to index existing posts, a bulk index of the enitre post database must be generated. 

Setting up an Elasticsearch Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The setup process for the Elasticsearch server is documented in the `official Elasticsearch documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html>`_. 


Hardware Requirements
`````````````````````
Elasticsearch should run alone on a server and use all of the resources available to it.

XXXXXX George: hardware requirements for the elasticsearch server?

Configuring Elasticsearch in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Follow these steps to connect your Elasticsearch server to Mattermost and generate the post index.

1. Open the **System Console** > **ADVANCED** > **Elasticsearch (Beta)** section.
2. Set **Enable Elasticsearch Indexing** to `true` to enable the other the settings on the page. Once the configuration is saved, new posts made to the database will be automatically indexed on the Elasticsearch server.
3. Set the Elasticsearch server connection details:
  a) Enter **Server Connection Address**
  b) Enter **Server Username** used to access the Elasticsearch server (Optional)
    - Note: For AWS Elasticsearch leave this field blank
  c) Enter **Server Password** associated with the username (Optional)
    - Note: For AWS Elasticsearch leave this field blank
  d) Set **Enable Cluster Sniffing**. Sniffing finds and connects to all data nodes in your cluster automatically.
    - Note: For AWS Elasticsearch this field should be set to `false`
4. Click **Test Connection** and **Save** the configuration.
  - If the server connection is unsuccessful you will not be able to save the configuration or enable searching with Elasticsearch
5. Build the post index of existing posts by clicking **Build Index**
  - This process can take up to a few hours depending on the size of the post database and number of messages. The progress percentage can be seen as the index is created.
6. Enable Elasticsearch by setting **Enable Elasticsearch for search queries** to `true`
  - Note: It is recommended that bulk indexing be completed before enabling Elasticsearch, otherwise search results will be incomplete.
7. Restart the Mattermost server


Beta Limitations
-----------------

1. Elasticsearch uses a standard selection of "stop words" that are filtered out of search results: "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", "with"  

2. Known Issues in Beta:

  - Searching stop words in quotes returns more results than just the searched terms (`ticket <https://mattermost.atlassian.net/browse/PLT-7314>`_)
  - Pressing ESC in the search box clears the search text (`ticket <https://mattermost.atlassian.net/browse/PLT-7368>`_)
  - AWS Elasticsearch implementations have a limit of 1000 days of post history that is searchable in Beta.
  - Highlighting of search terms is sometimes missing from the results list

Frequently Asked Questions (FAQ)
--------------------------------

Why do I need to use Elasticsearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Due to the limitations of scaling with database search, Enterprise deployments with more than 5,000,000 messages require Elasticsearch in order to execute performant search queries.

Are there any new search features are offered with Elasticsearch Beta?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Beta implementation of Elasticsearch matches the search features currently available with database search. The Mattermost team is working on Elasticsearch features such as file name and content search, date filters, and operators and modifiers.



