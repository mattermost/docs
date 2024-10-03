:orphan:
:nosearch:

Elasticsearch provides enterprise-scale deployments with optimized search performance and prevents performance degradation and timeouts. Learn more about :doc:`Elasticsearch </scale/elasticsearch>` in our product documentation.

You can configure the Elasticsearch environment in which Mattermost is deployed in **System Console > Environment > Elasticsearch**. You can also edit the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: elastic-enableindexing
  :displayname: Enable Elasticsearch indexing (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.EnableIndexing
  :environment: MM_ELASTICSEARCHSETTINGS_ENABLEINDEXING
  :description: Configure Mattermost to index new posts automatically.

  - **true**: Indexing of new posts occurs automatically.
  - **false**: **(Default)** Elasticsearch indexing is disabled and new messages aren't indexed.

Enable Elasticsearch indexing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------------+
| Configure Mattermost to index new posts automatically.        | - System Config path: **Environment > Elasticsearch**                          |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.EnableIndexing: false",`` |
| - **true**: Indexing of new messages occurs automatically.    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_ENABLEINDEXING``            |
| - **false**: **(Default)** Elasticsearch indexing is disabled |                                                                                |
|   and new messages aren't indexed.                            |                                                                                |
+---------------------------------------------------------------+--------------------------------------------------------------------------------+
| **Notes**:                                                                                                                                     |
|                                                                                                                                                |
| - Core search happens in a relational database and is intended for deployments under about 2-3 million posts and file entries. Beyond that     |
|   scale, `enabling Elasticsearch for search queries <#enable-elasticsearch-for-search-queries>`__ is highly recommended                        |
| - If you anticipate your Mattermost server reaching more than 2.5 million posts and file entries, we recommend enabling Elasticsearch for      |
|   optimum search performance **before** reaching 3 million posts.                                                                              |
| - For deployments with over 3 million posts, Elasticsearch is required to avoid significant performance issues, such as timeouts, with         |
|   :doc:`message searches </collaborate/search-for-messages>` and :doc:`@mentions </collaborate/mention-people>`.                               |
| - If indexing is disabled and then re-enabled after an index is created, purge and rebuild the index to ensure complete search results.        |
+---------------------------------------------------------------+--------------------------------------------------------------------------------+

.. config:setting:: elastic-backendtype
  :displayname: Elasticsearch backend type (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.Backend
  :environment: MM_ELASTICSEARCHSETTINGS_BACKEND
  :description: Set the type of search backend as either Elasticsearch or Opensearch.

Backend type
~~~~~~~~~~~~~

+----------------------------------------------------+-----------------------------------------------------------------------------------+
| The type of search backend.                        | - System Config path: **Environment > Elasticsearch**                             |
|                                                    | - ``config.json`` setting: ``".Elasticsearchsettings.Backend: elasticsearch",``   |
| - ``elasticsearch`` - (**Default**)                | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_BACKEND``                      |
| - ``opensearch``                                   |                                                                                   |
+----------------------------------------------------+-----------------------------------------------------------------------------------+

.. important::

  Mattermost v9.11 introduces support for `Elasticsearch v8 <https://www.elastic.co/guide/en/elasticsearch/reference/current/elasticsearch-intro.html>`_ and `OpenSearch <https://opensearch.org/>`_ (Beta).

  **Elasticsearch**
  
  - Mattermost supports Elasticsearch v7.17+. We recommend upgrading your Elasticsearch v7 instance to v8.x. See the `Elasticsearch upgrade <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ documentation for details.
  - The official AWS Elasticsearch v8 client only works from Elasticsearch v7.11 and later. This is a breaking change for customers using AWS Elasticsearch v7.10.x. We recommend customers upgrade to `AWS Opensearch <https://aws.amazon.com/opensearch-service/>`_ for future compatibility. See the `AWS Amazon Opensearch upgrade <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/version-migration.html>`_ documentation for details.
  - Customers using Elasticsearch v8 must set ``action.destructive_requires_name`` to ``false`` in ``elasticsearch.yml`` to enable wildcard operations.

  **Opensearch (Beta)**

  - Customers using OpenSearch as their search backend must change the default configuration value to ``opensearch`` using :ref:`mmctl config set <manage/mmctl-command-line-tool:mmctl config set>`, or by editing the ``config.json`` file manually, and then restarting the Mattermost server. This configuration setting value can't be changed dynamically while the Mattermost server is running using the System Console.
  - Additionally, we recommend that ``compatibility mode`` isn't enabled because it reports the incorrect version.

.. config:setting:: elastic-serverconnectionaddress
  :displayname: Server connection address (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.ConnectionUrl
  :environment: MM_ELASTICSEARCHSETTINGS_CONNECTIONURL
  :description: The address of the Elasticsearch server.

Server connection address
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------+--------------------------------------------------------------------------+
| The address of the Elasticsearch server.           | - System Config path: **Environment > Elasticsearch**                    |
|                                                    | - ``config.json`` setting: ``".Elasticsearchsettings.ConnectionUrl",``   |
|                                                    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CONNECTIONURL``       |
+----------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-CApath
  :displayname: CA path (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.CA
  :environment: MM_ELASTICSEARCHSETTINGS_CA
  :description: Optional path to the Custom Certificate Authority certificates for the Elasticsearch server.

CA path
~~~~~~~

+----------------------------------------------------+--------------------------------------------------------------------------+
| Optional path to the Custom Certificate Authority  | - System Config path: **Environment > Elasticsearch**                    |
| certificates for the Elasticsearch server.         | - ``config.json`` setting: ``".Elasticsearchsettings.CA",``              |
|                                                    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CA``                  |
+----------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: Available from Mattermost v7.8. Can be used in conjunction with basic auth credentials or to replace them.          |
| Leave this setting blank to use the default Certificate Authority certificates for the operating system.                      |
+----------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-clientcertificatepath
  :displayname: Client certificate path (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.ClientCert
  :environment: MM_ELASTICSEARCHSETTINGS_CLIENTCERT
  :description: Optional client certificate for the connection to the Elasticsearch server in PEM format.

Client certificate path
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+--------------------------------------------------------------------------+
| Optional client certificate for the connection to  | - System Config path: **Environment > Elasticsearch**                    |
| the Elasticsearch server in the PEM format.        | - ``config.json`` setting: ``".Elasticsearchsettings.ClientCert",``      |
|                                                    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CLIENTCERT``          |
+----------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: Available from Mattermost v7.8. Can be used in conjunction with basic auth credentials or to replace them.          |
+----------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-clientcertificatekeypath
  :displayname: Client certificate key path (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.ClientKey
  :environment: MM_ELASTICSEARCHSETTINGS_CLIENTKEY
  :description: Optional key for the client certificate in PEM format.

Client certificate key path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+--------------------------------------------------------------------------+
| Optional key for the client certificate in the PEM | - System Config path: **Environment > Elasticsearch**                    |
| format.                                            | - ``config.json`` setting: ``".Elasticsearchsettings.ClientKey",``       |
|                                                    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CLIENTKEY``           |
+----------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: Available from Mattermost v7.8. Can be used in conjunction with basic auth credentials or to replace them.          |
+----------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-skiptlsverification
  :displayname: Skip TLS verification (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.SkipTLSVerification
  :environment: MM_ELASTICSEARCHSETTINGS_SKIPTLSVERIFICATION
  :description: The certificate step for TLS connections can be skipped.

  - **true**: Skips the certificate verification step for TLS connections.
  - **false**: **(Default)** Mattermost does not skip certificate verification.

Skip TLS verification
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------------------------------+
| The certificate step for TLS connections can be skipped.      | - System Config path: **Environment > Elasticsearch**                               |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.SkipTLSVerification: false",`` |
| - **true**: Skips the certificate verification step for       | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_SKIPTLSVERIFICATION``            |
|   TLS connections.                                            |                                                                                     |
| - **false**: **(Default)** Mattermost does not skip           |                                                                                     |
|   certificate verification.                                   |                                                                                     |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------+

.. config:setting:: elastic-serverusername
  :displayname: Server username (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.UserName
  :environment: MM_ELASTICSEARCHSETTINGS_USERNAME
  :description: (Optional) The username to authenticate to the Elasticsearch server.

Server username
~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| (Optional) The username to authenticate to the                | - System Config path: **Environment > Elasticsearch**                    |
| Elasticsearch server.                                         | - ``config.json`` setting: ``".Elasticsearchsettings.UserName",``        |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_USERNAME``            |
| String input.                                                 |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-serverpassword
  :displayname: Server password (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.Password
  :environment: MM_ELASTICSEARCHSETTINGS_PASSWORD
  :description: (Optional) The password to authenticate to the Elasticsearch server.

Server password
~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| (Optional) The password to authenticate to the                | - System Config path: **Environment > Elasticsearch**                    |
| Elasticsearch server.                                         | - ``config.json`` setting: ``".Elasticsearchsettings.Password",``        |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_PASSWORD``            |
| String input.                                                 |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-enablesniffing
  :displayname: Enable cluster sniffing (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.Sniff
  :environment: MM_ELASTICSEARCHSETTINGS_SNIFF
  :description: Configure Mattermost to automatically find and connect to all data nodes in a cluster.

  - **true**: Sniffing finds and connects to all data nodes in your cluster automatically.
  - **false**: **(Default)** Cluster sniffing is disabled.

Enable cluster sniffing
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------+--------------------------------------------------------------------------+
| Configure Mattermost to automatically find and connect to      | - System Config path: **Environment > Elasticsearch**                    |
| all data nodes in a cluster.                                   | - ``config.json`` setting: ``".Elasticsearchsettings.Sniff: false",``    |
|                                                                | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_SNIFF``               |
| - **true**: Sniffing finds and connects to all data nodes      |                                                                          |
|   in your cluster automatically.                               |                                                                          |
| - **false**: **(Default)** Cluster sniffing is disabled.       |                                                                          |
+----------------------------------------------------------------+--------------------------------------------------------------------------+
| Select the **Test Connection** button in the System Console to validate the connection between Mattermost and the Elasticsearch server.   |
+----------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-bulkindexing
  :displayname: Bulk indexing (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: N/A
  :environment: N/A
  :description: Configure Mattermost to start a bulk index of all existing posts in the database by selecting Index Now.

Bulk indexing
~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Configure Mattermost to start a bulk index of all existing    | - System Config path: **Environment > Elasticsearch**                    |
| posts in the database, from oldest to newest.                 | - ``config.json`` setting: N/A                                           |
|                                                               | - Environment variable: N/A                                              |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **Notes**:                                                                                                                               |
|                                                                                                                                          |
| - Always `purge indexes <#purge-indexes>`__ before bulk indexing.                                                                        |
| - Select the **Index Now** button in the System Console to start a bulk index of all posts, and review all index jobs in progress.       |
| - Elasticsearch is available during indexing, but search results may be incomplete until the indexing job is complete.                   |
| - If an in-progress indexing job is canceled, the index and search results will be incomplete.                                           |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-rebuildchannelsindex
  :displayname: Rebuild channels index (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: N/A
  :environment: N/A
  :description: Purge the channels index adn re-index all channels in the database, from oldest to newest.

Rebuild channels index
~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------+
| Purge the channels index adn re-index all channels in the     | - System Config path: **Environment > Elasticsearch**         |
| database, from oldest to newest.                              | - ``config.json`` setting: N/A                                |
|                                                               | - Environment variable: N/A                                   |
+---------------------------------------------------------------+---------------------------------------------------------------+
| Select the **Rebuild Channels Index** button in the System Console to purge the channels index.                               |
| Ensure no other indexing jobs are in progress via the **Bulk Indexing** table before starting this process.                   |
| During indexing, channel auto-complete is available, but search results may be incomplete until the indexing job is complete. |
+---------------------------------------------------------------+---------------------------------------------------------------+

.. config:setting:: elastic-purgeindexes
  :displayname: Purge indexes (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: N/A
  :environment: N/A
  :description: Purge the entire Elasticsearch index by selecting Purge Indexes before creating a new index.

Purge indexes
~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-------------------------------------------+-------------------------------------------------------------+
| Purge the entire Elasticsearch index.     | - System Config path: **Environment > Elasticsearch**       |
|                                           | - ``config.json`` setting: N/A                              |
|                                           | - Environment variable: N/A                                 |
+-------------------------------------------+-------------------------------------------------------------+
| Select the **Purge Indexes** button in the System Console to purge the index.                           |
| After purging the index, create a new index by selecting the **Index Now** button.                      |
+-------------------------------------------+-------------------------------------------------------------+

.. config:setting:: elastic-indexestoskipwhilepurging
  :displayname: Indexes to skip while purging (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.IgnoredPurgeIndexes
  :environment: MM_ELASTICSEARCHSETTINGS_IGNOREDPURGEINDEXES
  :description: Specify index names to ignore while purging indexes, separated by commas.

Indexes to skip while purging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------------------+
| Specify index names to ignore while purging indexes.          | - System Config path: **Environment > Elasticsearch**                     |
| Separate multiple index names with commas.                    | - ``config.json`` setting: ``ElasticsearchSettings.IgnoredPurgeIndexes``  |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_IGNOREDPURGEINDEXES``  |
| Use an asterisk (*) to match a sequence of index name         |                                                                           |
| characters.                                                   |                                                                           |
+---------------------------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: elastic-enablesearch
  :displayname: Enable Elasticsearch for search queries (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.EnableSearching
  :environment: MM_ELASTICSEARCHSETTINGS_ENABLESEARCHING
  :description: Configure Mattermost to use Elasticsearch for all search queries using the latest index.

  - **true**: Elasticsearch is used for all search queries using the latest index. Search results may be incomplete until a bulk index of the existing message database is completed.
  - **false**: **(Default)** Relational database search is used for search queries.

Enable Elasticsearch for search queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

.. important::

  - Core search happens in a relational database and is intended for deployments under about 2-3 million posts and file entries. Beyond that scale, enabling Elasticsearch for search queries is highly recommended.
  - If you anticipate your Mattermost server reaching more than 2.5 million posts and file entries, we recommend enabling Elasticsearch for optimum search performance **before** reaching 3 million posts.
  - For deployments with over 3 million posts, Elasticsearch with :ref:`dedicated indexing <configure/environment-configuration-settings:enable elasticsearch indexing>` and scaled usage resourcing through :doc:`cluster support </scale/high-availability-cluster-based-deployment>` is required to avoid significant performance issues, such as timeouts, with :doc:`message searches </collaborate/search-for-messages>` and :doc:`@mentions </collaborate/mention-people>`.

+---------------------------------------------------------------+---------------------------------------------------------------------------------+
| Configure Mattermost to use Elasticsearch for all search      | - System Config path: **Environment > Elasticsearch**                           |
| queries using the latest index.                               | - ``config.json`` setting: ``".Elasticsearchsettings.EnableSearching: false",`` |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_ENABLESEARCHING``            |
| - **true**: Elasticsearch is used for all search queries      |                                                                                 |
|   using the latest index. Search results may be incomplete    |                                                                                 |
|   until a bulk index of the existing message database is      |                                                                                 |
|   completed.                                                  |                                                                                 |
| - **false**: **(Default)** Database search is used for        |                                                                                 |
|   search queries.                                             |                                                                                 |
+---------------------------------------------------------------+---------------------------------------------------------------------------------+
| **Note**: If indexing is disabled and then re-enabled after an index is created, purge and rebuild the index to ensure complete search results. |
+---------------------------------------------------------------+---------------------------------------------------------------------------------+

.. config:setting:: elastic-enableautocomplete
  :displayname: Enable Elasticsearch for autocomplete queries (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.EnableAutocomplete
  :environment: MM_ELASTICSEARCHSETTINGS_ENABLEAUTOCOMPLETE
  :description: Configure Mattermost to use Elasticsearch for all autocompletion queries on users and channels using the latest index.

  - **true**: Elasticsearch will be used for all autocompletion queries on users and channels using the latest index.
  - **false**: **(Default)** Database autocomplete is used.

Enable Elasticsearch for autocomplete queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+------------------------------------------------------------------------------------+
| Configure Mattermost to use Elasticsearch for all             | - System Config path: **Environment > Elasticsearch**                              |
| autocompletion queries on users and channels using the        | - ``config.json`` setting: ``".Elasticsearchsettings.EnableAutocomplete: false",`` |
| latest index.                                                 | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_ENABLEAUTOCOMPLETE``            |
|                                                               |                                                                                    |
| - **true**: Elasticsearch will be used for all autocompletion |                                                                                    |
|   queries on users and channels using the latest index.       |                                                                                    |
| - **false**: **(Default)** Database autocomplete is used.     |                                                                                    |
+---------------------------------------------------------------+------------------------------------------------------------------------------------+
| **Note**: Autocompletion results may be incomplete until a bulk index of the existing users and channels database is finished.                     |
+---------------------------------------------------------------+------------------------------------------------------------------------------------+

.. config:setting:: elastic-postindexreplicas
  :displayname: Post index replicas (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.PostIndexReplicas
  :environment: MM_ELASTICSEARCHSETTINGS_POSTINDEXREPLICAS
  :description: The number of replicas to use for each post index. Default is **1**.

Post index replicas
~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The number of replicas to use for each post index.            | - System Config path: N/A                                                     |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.PostIndexReplicas: 1",`` |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_POSTINDEXREPLICAS``        |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Important notes**:                                                                                                                          |
|                                                                                                                                               |
| - If this setting is changed, the changed configuration only applies to newly-created indexes. To apply the change to existing indexes,       |
|   purge and rebuild the index after changing this setting.                                                                                    |
| - If there are ``n`` data nodes, the number of replicas per shard for each index should be ``n-1``.                                           |
| - If the number of nodes in an Elasticsearch cluster changes, this configuration setting, as well as                                          |
|   `Channel Index Replicas <#channel-index-replicas>`__ and `User Index Replicas <#user-index-replicas>`__ must also be updated accordingly.   |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

.. config:setting:: elastic-postindexshards
  :displayname: Post index shards (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.PostIndexShards
  :environment: MM_ELASTICSEARCHSETTINGS_POSTINDEXSHARDS
  :description: The number of shards to use for each post index. Default is **1**.

Post index shards
~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The number of shards to use for each post index.              | - System Config path: N/A                                                     |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.PostIndexShards: 1",``   |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_POSTINDEXSHARDS``          |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Important note**: If this configuration setting is changed, the changed configuration only applies to newly-created indexes.                |
| To apply the change to existing indexes, purge and rebuild the index after changing this setting.                                             |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+


.. config:setting:: elastic-channelindexreplicas
  :displayname: Channel index replicas (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.ChannelIndexReplicas
  :environment: MM_ELASTICSEARCHSETTINGS_CHANNELINDEXREPLICAS
  :description: The number of replicas to use for each channel index. Default is **1**.

Channel index replicas
~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+----------------------------------------------------------------------------------+
| The number of replicas to use for each channel index.         | - System Config path: N/A                                                        |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.ChannelIndexReplicas: 1",`` |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CHANNELINDEXREPLICAS``        |
+---------------------------------------------------------------+----------------------------------------------------------------------------------+
| **Note**: If there are ``n`` data nodes, the number of replicas per shard for each index should be ``n-1``. If the number of nodes in an         |
| Elasticsearch cluster changes, this configuration setting, as well as `Post Index Replicas <#post-index-shards>`__ and                           |
| `User Index Replicas <#user-index-replicas>`__ must also be updated accordingly.                                                                 |
+---------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: elastic-channelindexshards
  :displayname: Channel index shards (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.ChannelIndexShards
  :environment: MM_ELASTICSEARCHSETTINGS_CHANNELINDEXSHARDS
  :description: The number of shards to use for each channel index. Default is **1**.

Channel index shards
~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+----------------------------------------------------------------------------------+
| The number of shards to use for each channel index.           | - System Config path: N/A                                                        |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.ChannelIndexShards: 1",``   |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CHANNELINDEXSHARDS``          |
+---------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: elastic-userindexreplicas
  :displayname: User index replicas (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.UserIndexReplicas
  :environment: MM_ELASTICSEARCHSETTINGS_USERINDEXREPLICAS
  :description: The number of replicas to use for each user index. Default is **1**.

User index replicas
~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The number of replicas to use for each user index.            | - System Config path: N/A                                                     |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.UserIndexReplicas: 1",`` |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_USERINDEXREPLICAS``        |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Note**: If there are ``n`` data nodes, the number of replicas per shard for each index should be ``n-1``. If the number of nodes in an      |
| Elasticsearch cluster changes, this configuration setting, as well as `Post Index Replicas <#post-index-replicas>`__ and                      |
| `Channel Index Replicas <#channel-index-replicas>`__ must also be updated accordingly.                                                        |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

.. config:setting:: elastic-userindexshards
  :displayname: User index shards (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.UserIndexShards
  :environment: MM_ELASTICSEARCHSETTINGS_USERINDEXSHARDS
  :description: The number of shards to use for each user index. Default is **1**.

User index shards
~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+----------------------------------------------------------------------------------+
| The number of shards to use for each user index.              | - System Config path: N/A                                                        |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.UserIndexShards: 1",``      |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_USERINDEXSHARDS``             |
+---------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: elastic-aggregatesearchindexes
  :displayname: Aggregate search indexes (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.AggregatePostsAfterDays
  :environment: MM_ELASTICSEARCHSETTINGS_AGGREGATEPOSTSAFTERDAYS
  :description: Elasticsearch indexes older than the age specified by this setting, in days, will be aggregated during the daily scheduled job. Default is **365** days.

Aggregate search indexes
~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Elasticsearch indexes older than the age specified by this    | - System Config path: N/A                                                              |
| setting, in days, will be aggregated during the daily         | - ``config.json`` setting: ``".Elasticsearchsettings.AggregatePostsAfterDays: 365",``  |
| scheduled job.                                                | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_AGGREGATEPOSTSAFTERDAYS``           |
|                                                               |                                                                                        |
| Numerical input. Default is **365** days.                     |                                                                                        |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
| **Note**: If you’re using :doc:`data retention </comply/data-retention-policy>` and                                                                    |
| :doc:`Elasticsearch </scale/elasticsearch>`, configure this with a value greater than your data retention policy.                                      |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------+

.. config:setting:: elastic-postaggregatorstarttime
  :displayname: Post aggregator start time (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.PostsAggregatorJobStartTime
  :environment: MM_ELASTICSEARCHSETTINGS_POSTSAGGREGATORJOBSTARTTIME
  :description: The start time of the daily scheduled aggregator job. Must be a 24-hour time stamp in the form ``HH:MM`` based on the local time of the server. Default is **03:00** (3 AM).

Post aggregator start time
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| The start time of the daily scheduled aggregator job.         | - System Config path: N/A                                                                   |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.PostsAggregatorJobStartTime: 03:00",`` |
| Must be a 24-hour time stamp in the form ``HH:MM`` based on   | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_POSTSAGGREGATORJOBSTARTTIME``            |
| the local time of the server.                                 |                                                                                             |
|                                                               |                                                                                             |
| Default is **03:00** (3 AM)                                   |                                                                                             |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+

.. config:setting:: elastic-indexprefix
  :displayname: Index prefix (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.IndexPrefix
  :environment: MM_ELASTICSEARCHSETTINGS_INDEXPREFIX
  :description: The prefix added to the Elasticsearch index name.

Index prefix
~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The prefix added to the Elasticsearch index name.             | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.IndexPrefix",``     |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_INDEXPREFIX``         |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: When this setting is used, all Elasticsearch indexes created by Mattermost are given this prefix. You can set different        |
| prefixes so that multiple Mattermost deployments can share an Elasticsearch cluster without the index names colliding.                   |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-liveindexingbatchsize
  :displayname: Live indexing batch size (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.LiveIndexingBatchSize
  :environment: MM_ELASTICSEARCHSETTINGS_LIVEINDEXINGBATCHSIZE
  :description: The number of new posts batched together before they're added to the Elasticsearch index. Default is **1**.

Live indexing batch size
~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-----------------------------------------------------------------------------------+
| The number of new posts needed before those posts are added   | - System Config path: N/A                                                         |
| to the Elasticsearch index. Once added to the Index,          | - ``config.json`` setting: ``".Elasticsearchsettings.LiveIndexingBatchSize: 1",`` |
| the post becomes searchable.                                  | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_LIVEINDEXINGBATCHSIZE``        |
|                                                               |                                                                                   |
| On servers with more than 1 post per second, we suggest       |                                                                                   |
| setting this value to the average number of  posts over a     |                                                                                   |
| 20 second period of time.                                     |                                                                                   |
|                                                               |                                                                                   |
| Numerical input. Default is **1**. Every post is indexed      |                                                                                   |
| synchronously as they are created.                            |                                                                                   |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------+
| **Note**: It may be necessary to increase this value to avoid hitting the rate limit or resource limit of your Elasticsearch cluster              |
| on installs handling more than 1 post per second.                                                                                                 |
|                                                                                                                                                   |
| **What exactly happens when I increase this value?**                                                                                              |
| The primary impact is that a post will be indexed into Elasticsearch after the threshold of posts is met which then makes the posts searchable    |
| within Mattermost. So, if you set this based on our recommendations for larger servers, and you make a post, you cannot find it via search        | 
| for ~ 10-20 seconds, on average. Realistically, no users should see or feel this impact due to the limited amount of users who are actively       |
| **searching** for a post this quickly. You can set this value to a lower average or higher average as well, depending on your Elasticsearch       |
| server specifications.                                                                                                                            |
|                                                                                                                                                   |
| During busy periods, this delay will be faster as more traffic is happening, causing more posts and a quicker time to hit the index number.       |
| During slow times, expect the reverse.                                                                                                            |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------+

**How to find the right number for your server**

1. You must understand how many posts your server makes every minute. Run the query below to calculate your server's average posts per minute.

    Note that this query can be heavy, so we recommend that you run it during non-peak hours.
    Additionally, you can adjust the ``WHERE`` clause to see the posts per minute over a different time period. Right now ``31536000000`` represents the number of milliseconds in a year. 

    .. code-block:: SQL

      SELECT
        AVG(postsPerMinute) as averagePostsPerMinute
      FROM (
        SELECT 
          count(*) as postsPerMinute, 
          date_trunc('minute', to_timestamp(createat/1000))
        FROM posts
        WHERE createAt > ( (extract(epoch from now()) * 1000 )  - 31536000000)
        GROUP BY date_trunc('minute', to_timestamp(createat/1000))
      ) as ppm;

2. Decide the acceptable index window for your environment, and divide your average posts per minute by that. We suggest 10-20 seconds. Assuming you have ``600`` posts per minute on average, and you want to index every 20 seconds (``60 seconds / 20 seconds = 3```) you would calculate ``600 / 3`` to come to the number ``200``. After 200 posts, Mattermost will index the posts into Elasticsearch. So, on average, there would be a 20-second delay in searchability.

3. Edit the ``config.json`` or run mmctl to modify the ``LiveIndexingBatchSize`` setting

    **In the ``config.json``**

    .. code-block:: JSON

      {
        "ElasticsearchSettings": {
          "LiveIndexingBatchSize": 200
        }
      }

    **Via mmctl**

    .. code-block:: sh

      mmctl config set ElasticsearchSettings.LiveIndexingBatchSize 200

    **Via an environment variable**

    .. code-block:: sh

      MM_ELASTICSEARCHSETTINGS_LIVEINDEXINGBATCHSIZE = 200

4. Restart the Mattermost server.

.. config:setting:: elastic-batchsize
  :displayname: Batch size (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.BatchSize
  :environment: MM_ELASTICSEARCHSETTINGS_BATCHSIZE
  :description: The number of posts for a single batch during a bulk indexing job. Default is **10000**.

Batch size
~~~~~~~~~~~

+-------------------------------------------+---------------------------------------------------------------------------+
| The number of posts for a single batch    | - System Config path: N/A                                                 |
| during a bulk indexing job.               | - ``config.json`` setting: ``".Elasticsearchsettings.BatchSize :10000",`` |
|                                           | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_BATCHSIZE``            |
| Numerical input. Default is **10000**.    |                                                                           |
+-------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: elastic-requesttimeout
  :displayname: Request timeout (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.RequestTimeoutSeconds
  :environment: MM_ELASTICSEARCHSETTINGS_REQUESTTIMEOUTSECONDS
  :description: The timeout, in seconds, for Elasticsearch calls. Default is **30** seconds.

Request timeout
~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+------------------------------------------------------------------------------------+
| The timeout, in seconds, for Elasticsearch calls.             | - System Config path: N/A                                                          |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.RequestTimeoutSeconds :30",`` |
| Numerical input in seconds. Default is **30** seconds.        | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_REQUESTTIMEOUTSECONDS``         |
+---------------------------------------------------------------+------------------------------------------------------------------------------------+

.. config:setting:: elastic-trace
  :displayname: Trace (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.Trace
  :environment: MM_ELASTICSEARCHSETTINGS_TRACE
  :description: Options for printing Elasticsearch trace errors.

  - **error**: Creates the error trace when initializing the Elasticsearch client and prints any template creation or search query that returns an error as part of the error message.
  - **all**: Creates the three traces (error, trace and info) for the driver and doesn’t print the queries because they will be part of the trace log level of the driver.
  - **not specified**: **(Default)** No error trace is created.

Trace
~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Options for printing Elasticsearch trace errors.              | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.Trace",``           |
| - **error**: Creates the error trace when initializing        | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_TRACE``               |
|   the Elasticsearch client and prints any template creation   |                                                                          |
|   or search query that returns an error as part of the        |                                                                          |
|   error message.                                              |                                                                          |
| - **all**: Creates the three traces (error, trace and info)   |                                                                          |
|   for the driver and doesn’t print the queries because they   |                                                                          |
|   will be part of the trace log level of the driver.          |                                                                          |
| - **not specified**: **(Default)** No error trace is created. |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
