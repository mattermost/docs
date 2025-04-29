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

Follow these steps to configure Mattermost to use your AWS OpenSearch server and to generate the post index:

1. Go to **System Console > Environment > Elasticsearch**.
2. Set **Enable Elasticsearch Indexing** to ``true`` to enable the other the settings on the page. Once the configuration is saved, new posts made to the database are automatically indexed on the AWS OpenSearch server.
3. Ensure **Backend type** is set to ``opensearch``.

.. include:: /scale/common-configure-mattermost-for-enterprise-search.rst
   :start-after: :nosearch: