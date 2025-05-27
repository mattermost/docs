Enterprise search
==================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Mattermost database search starts to show performance degradation at around 2 million posts, on a server with 32 GB RAM and 4 CPUs. If you anticipate your Mattermost server reaching more than 2.5 million posts, we recommend enabling `Elasticsearch <#elasticsearch>`__ or `AWS OpenSearch Service <#aws-opensearch-service>`__ for optimum search performance **before** reaching 3 million posts. Both tools are highly capable and can handle enterprise-scale workloads. The choice between them depends on the following factors:

- **Licensing and cost**: AWS OpenSearch may be preferable for organizations avoiding proprietary licensing or opting for cost-effective solutions.
- **Feature requirements**: Elasticsearch's proprietary features (e.g., advanced analytics, security suites) may be preferred by organizations needing powerful out-of-the-box functionality.
- **Infrastructure alignment**: AWS OpenSearch aligns well with AWS-centric environments, while Elasticsearch offers broader integrations.

.. toctree::
    :maxdepth: 1
    :hidden:
    :titlesonly:

    Elasticsearch setup </scale/elasticsearch-setup>
    AWS OpenSearch setup </scale/opensearch-setup>

Elasticsearch
-------------

Elasticsearch is a well-established and widely used search engine with a large ecosystem and community support that provides enterprise-scale deployments with optimized search performance, dedicated indexing, and usage resourcing via cluster support for fast, predicable search results. 

Mattermost's implementation uses `Elasticsearch <https://www.elastic.co>`_ as a distributed, RESTful search engine supporting highly efficient database searches in a :doc:`cluster environment </scale/high-availability-cluster-based-deployment>`. Learn more about :doc:`setting up and configuring Mattermost for an Elasticsearch server </scale/elasticsearch-setup>`.

AWS OpenSearch Service
-----------------------

AWS OpenSearch Service is the official path forward from Elasticsearch v7.10.x for AWS customers. It's a fully managed service that makes it easy to deploy, operate, and scale OpenSearch clusters in the AWS Cloud to provide a simple and cost-effective way to search, analyze, and visualize data in real time. 

The AWS OpenSearch Service is built on the open-source OpenSearch project, which is a community-driven fork of Elasticsearch. Learn more about :doc:`setting up and configuring Mattermost for an OpenSearch server </scale/opensearch-setup>`.

Supported paths
----------------

Review the following support paths for enterprise search based on the version you're using:

.. tab:: Elasticsearch v8

    `Elasticsearch v8 <https://www.elastic.co/guide/en/elasticsearch/reference/current/elasticsearch-intro.html>`__ is supported from Mattermost v9.11. While Mattermost supports Elasticsearch v7.17+, we recommend upgrading your Elasticsearch v7 instance to v8.x. See the `Elasticsearch upgrade <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ documentation for upgrade details, and see the :doc:`Elasticsearch setup </scale/elasticsearch-setup>` documentation for details on configuring your Mattermost deployment to use Elasticsearch.

.. tab:: AWS OpenSearch Service

    AWS OpenSearch Service is the official path forward from Elasticsearch v7.10.x for AWS customers to provide a simple and cost-effective way to search, analyze, and visual data in real time. It's essentially a continuation of Elasticsearch v7.10.x but maintained as open source by AWS. It provides long-term support, active development, and compatibility with AWS clients, libraries, and managed services. 
    
    See the **AWS Elasticsearch v7.10.x** tab on this page for details on upgrading to AWS OpenSearch, and see the :doc:`AWS OpenSearch setup </scale/opensearch-setup>` documentation for details on configuring your Mattermost deployment to use AWS OpenSearch.

.. tab:: AWS Elasticsearch v7.10.x

    If you're using Elasticsearch v7.10.x under AWS’s managed services, you can't use newer Elasticsearch clients like the v8 client without changing backend infrastructure. If you're using AWS Elasticsearch v7.10.x, you must `upgrade to AWS OpenSearch <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/version-migration.html>`_ for future compatibility.

    The migration path from Elasticsearch v7.10.x to OpenSearch has been designed to be straightforward, minimizing effort:

    1. Disable "compatibility mode" in OpenSearch.
    2. Upgrade Mattermost server.
    3. Update the Mattermost ``ElasticsearchSettings.Backend`` configuration setting value from ``elasticsearch`` to ```opensearch``` manually or using :ref:`mmctl <manage/mmctl-command-line-tool:mmctl config set>`. This value cannot be changed using the System Console. See the Mattermost search :ref:`backend type <configure/environment-configuration-settings:backend type>` configuration setting documentation for additional details.
    4. Restart the Mattermost server.

Frequently asked questions (FAQ)
--------------------------------

Do I need to use Elasticsearch or AWS OpenSearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. Enterprise search engines are designed for large Enterprise deployments to run highly efficient database searches in a cluster environment. The default Mattermost database search starts to show performance degradation at around 2.5 million posts, depending on the specifications for the database server. If you expect your Mattermost server to have more than 2.5 million posts, we recommend using Elasticsearch or AWS OpenSearch for optimum search performance.

Should I install Elasticsearch or OpenSearch on the same machine as Mattermost Server?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. We strongly recommend that you install Elasticsearch or AWS OpenSearch on a dedicated machine that's separate from the Mattermost server.

What types of indexes are created?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost creates three types of indexes: users, channels, and posts. Users and channels have one index each. Posts are aggregated by date, into multiple indexes.

Can I pause an search indexing job?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. From Mattermost v6.7, the search indexing job is resumable. Stopping a server while the search indexing job is running puts the job in pending status. The job resumes when the server restarts. System admins can cancel an indexing job through the System Console.

Can an index rollover policy be defined?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The :ref:`AggregatePostsAfterDays <configure/environment-configuration-settings:aggregate search indexes>` configuration setting defines a cutoff value. All posts preceding this value are reindexed and aggregated into new and bigger indexes. The default setting is 365 days.

Are there any new search features offered with Elasticsearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The current implementation of Elasticsearch matches the search features currently available with database search. The Mattermost team is working on extending the Elasticsearch feature set with file name and content search, date filters, and operators and modifiers.

Are my files stored in Elasticsearch or OpenSearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, files and attachments are not stored.

How do I monitor system health of an Elasticsearch server?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use this Prometheus exporter to monitor `various metrics <https://github.com/justwatchcom/elasticsearch_exporter#metrics>`__ about Elasticsearch: `justwatchcom/elasticsearch_exporter <https://github.com/justwatchcom/elasticsearch_exporter>`__.

You can also refer to this `article about Elasticsearch performance monitoring <https://www.datadoghq.com/blog/monitor-elasticsearch-performance-metrics/#key-elasticsearch-performance-metrics-to-monitor>`__. It's not written specifically for Prometheus, which :doc:`Mattermost's performance monitoring </scale/deploy-prometheus-grafana-for-performance-monitoring>` system uses, but has several tips and best practices.
 
What form of data is sent to Elasticsearch or OpenSearch?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost communicates with Elasticsearch or OpenSearch through its REST API using JSON messages for indexing and querying entities.

How much data is sent to Elasticsearch or OpenSearch and when?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every time a message is published, a channel is created, or a user changes, (either because their properties change e.g.: change of the first name or because they join/leave a channel), the data associated with that event is sent to Elasticsearch or OpenSearch.

If search via Elasticsearch or OpenSearch is enabled, every search will generate a query. If autocompletion is enabled, every user or channel autocompletion associated with writing a message or user search will generate a query.

How do I know if a search job fails?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost provides the status of each Elasticsearch or OpenSearch indexing job in **System Console > Environment > Elasticsearch**. Here you can see if the job succeeded or failed, including the details of the error.

Failures are returned in the server logs. The error log begins with the string ``Failed job`` and includes a job_id key/value pair. Search job failures are identified with worker name ``EnterpriseElasticsearchAggregator`` and ``EnterpriseElasticsearchIndexer``. You can optionally create a script that programmatically queries for such failures and notifies the appropriate system.

My search indexes won't complete, what should I do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have an search indexing job that's paused, it's likely your Elasticsearch or OpenSearch server has restarted. If you restart that server, you must also restart Mattermost to ensure jobs are completed. If restarting the Mattermost server does not resolve the issue, `commercial customers can contact Mattermost Support <https://mattermost.com/support/>`__ for assistance.

Do I need to purge first then bulk index each time?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes.

Required Permissions For Mattermost Service Account
---------------------------------------------------
In "least privilege" environments you may need to further constrain the service account permissions to limit the access your Elasticsearch or AWS OpenSearch service account has. 

The following JSON provides an example of a "least privilege" permission set that allows Mattermost to operate correctly with Elasticsearch or AWS OpenSearch:

 .. code-block:: json

  {
    "cluster_permissions": [
      "cluster:monitor/*",
      "indices:admin/template/put",
      "indices:data/write/bulk"
    ],
    "index_permissions": [
      {
        "index_patterns": [
          "\<IndexPrefix\>*"
        ],
        "allowed_actions": [
          "indices:admin/get",
          "indices:admin/create",
          "indices:admin/delete",
          "indices:admin/mapping/put",
          "indices:admin/mappings/fields/get*",
          "indices:data/read*",
          "indices:data/write*"
        ]
      }
    ]
  }

A simpler, more flexible, and resilient variant of the above would be:

.. code-block:: json

  {
    "cluster_permissions": [
      "cluster:monitor/*",
      "indices:admin/template/put",
      "indices:data/write/bulk"
    ],
    "index_permissions": [
      {
        "index_patterns": [
          "\<IndexPrefix\>*"
        ],
        "allowed_actions": [
          "indices:*"
        ]
      }
    ]
  }
