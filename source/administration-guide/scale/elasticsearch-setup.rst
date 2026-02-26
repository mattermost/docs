Elasticsearch server setup
===========================

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

Elasticsearch allows you to search large volumes of data quickly, in near real-time, by creating and managing an index of post data. The indexing process can be managed from the System Console after setting up and connecting an Elasticsearch server. The post index is stored on the Elasticsearch server and updated constantly after new posts are made. In order to index existing posts, a bulk index of the entire post database must be generated.

Deploying Elasticsearch includes the following steps: `setting up a single Elasticsearch node <#set-up-a-single-elasticsearch-node>`__, optionally `configuring a multi-node cluster <#set-up-an-elasticsearch-cluster>`__, and `configuring Mattermost <#configure-mattermost>`_.

Set up a single Elasticsearch node
------------------------------------

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

7. When using Elasticsearch v8, ensure you set ``action.destructive_requires_name`` to ``false`` in ``elasticsearch.yml`` to allow for wildcard operations to work.

8. Restart Elasticsearch by running the following commands:

  .. code-block:: sh

    sudo systemctl stop elasticsearch
    sudo systemctl start elasticsearch

9. Confirm the ports are listenings by running the following command:

  .. code-block:: sh

    netstat -plnt

  You should see the following ports, including  the ones listening on ports 9200 and 9300. Confirm these are listening on your server's IP address. 

10. Create an Elasticsearch directory and give it the proper permissions.

11. Install the `icu-analyzer plugin <https://www.elastic.co/guide/en/elasticsearch/plugins/current/analysis-icu.html>`__ to the ``/usr/share/elasticsearch/plugins`` directory by running the following command:

  .. code-block:: sh

    sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu

12. Test the connection from Mattermost to Elasticsearch by running the following command:

  .. code-block:: sh

    curl 172.31.80.220:9200

.. _set-up-an-elasticsearch-cluster:

Set up an Elasticsearch cluster
--------------------------------

For production environments requiring high availability and fault tolerance, deploy Elasticsearch as a multi-node cluster rather than a single node. A cluster distributes data across multiple nodes, providing redundancy and improved search performance. If one node goes down, the remaining nodes continue to serve search requests without interruption.

.. important::

  Complete the single-node setup above on your first server before proceeding with cluster configuration. The first node becomes the foundation of your cluster.

Cluster prerequisites
~~~~~~~~~~~~~~~~~~~~~~

Before configuring a cluster, ensure the following requirements are met:

- **Minimum three nodes**: Deploy an odd number of master-eligible nodes (minimum of three) to prevent split-brain scenarios, where the cluster partitions into two halves that each elect their own master node.
- **Same Elasticsearch version**: All nodes in the cluster must run the same version of Elasticsearch.
- **Network connectivity**: All nodes must be able to communicate with each other on ports ``9200`` (HTTP API) and ``9300`` (inter-node transport).
- **Hostname resolution**: Each node must be able to resolve the hostnames of all other nodes, either via DNS or the ``/etc/hosts`` file.
- **ICU Analyzer plugin**: The ``analysis-icu`` plugin must be installed on every node in the cluster, not just the first node.

Node roles
~~~~~~~~~~~

Each Elasticsearch node can serve one or more roles:

- **Master-eligible**: Manages cluster-wide operations such as creating or deleting indexes, tracking cluster membership, and deciding which data shards are allocated to which nodes.
- **Data**: Stores indexed data and handles search and aggregation requests. Data nodes consume significant CPU, memory, and I/O resources.
- **Coordinating**: Routes client requests to the appropriate data nodes and merges results. Every node acts as a coordinating node by default.

For most Mattermost deployments, a three-node cluster where every node is both master-eligible and a data node is the recommended configuration.

Configure the first node for clustering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Edit the Elasticsearch configuration file on the first node:

  .. code-block:: sh

    vi /etc/elasticsearch/elasticsearch.yml

2. Configure the following cluster settings, replacing the example IP addresses with the actual addresses of your servers:

  .. code-block:: sh

    # Give your cluster a descriptive name
    cluster.name: mattermost-es-cluster

    # Set a unique name for this node
    node.name: es-node-01

    # Bind to this server's network interface
    network.host: 192.168.1.10

    # List the addresses of all nodes for discovery
    discovery.seed_hosts: ["192.168.1.10", "192.168.1.11", "192.168.1.12"]

    # Define the initial set of master-eligible nodes (first bootstrap only)
    cluster.initial_master_nodes: ["es-node-01", "es-node-02", "es-node-03"]

3. Restart Elasticsearch:

  .. code-block:: sh

    sudo systemctl stop elasticsearch
    sudo systemctl start elasticsearch

.. note::

  The ``cluster.initial_master_nodes`` setting is only used during the very first bootstrap of the cluster. Once the cluster is formed, this setting is ignored. Some administrators choose to remove it after initial cluster formation to prevent accidental re-bootstrapping.

Add nodes to the cluster (Elasticsearch 8.x)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Elasticsearch 8.x simplifies adding new nodes to a cluster using enrollment tokens. This approach automatically handles TLS certificate distribution between nodes.

1. On the **first node**, generate an enrollment token:

  .. code-block:: sh

    sudo /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s node

  This token is valid for 30 minutes. If it expires, generate a new one by running the same command again.

2. On each **additional node**, install Elasticsearch (the same version as the first node) and install the ICU Analyzer plugin:

  .. code-block:: sh

    sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu

3. Before starting Elasticsearch on the additional node, run the reconfigure command with the enrollment token from step 1:

  .. code-block:: sh

    sudo /usr/share/elasticsearch/bin/elasticsearch-reconfigure-node --enrollment-token <token-from-step-1>

  This configures the node to join the existing cluster and copies the necessary TLS certificates from the first node.

4. Edit the Elasticsearch configuration file on the additional node:

  .. code-block:: sh

    vi /etc/elasticsearch/elasticsearch.yml

5. Configure the cluster settings. The ``cluster.name``, ``discovery.seed_hosts``, and ``cluster.initial_master_nodes`` values must match the first node. Set a unique ``node.name`` and ``network.host`` for each node:

  .. code-block:: sh

    # Must match the first node's cluster name
    cluster.name: mattermost-es-cluster

    # Set a unique name for this node
    node.name: es-node-02

    # Bind to this server's network interface
    network.host: 192.168.1.11

    # Same discovery settings as the first node
    discovery.seed_hosts: ["192.168.1.10", "192.168.1.11", "192.168.1.12"]
    cluster.initial_master_nodes: ["es-node-01", "es-node-02", "es-node-03"]

6. When using Elasticsearch v8, ensure you set ``action.destructive_requires_name`` to ``false`` in ``elasticsearch.yml`` to allow for wildcard operations to work.

7. Start Elasticsearch on the additional node:

  .. code-block:: sh

    sudo /bin/systemctl daemon-reload
    sudo /bin/systemctl enable elasticsearch.service
    sudo systemctl start elasticsearch.service

8. Repeat steps 2 through 7 for each additional node, adjusting ``node.name`` and ``network.host`` for each server.

Add nodes to the cluster (Elasticsearch 7.x)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For Elasticsearch 7.x, enrollment tokens are not available. Instead, configure each additional node manually.

1. On each **additional node**, install Elasticsearch (the same version as the first node) and install the ICU Analyzer plugin:

  .. code-block:: sh

    sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu

2. Edit the Elasticsearch configuration file on the additional node:

  .. code-block:: sh

    vi /etc/elasticsearch/elasticsearch.yml

3. Configure the cluster settings as described above for the first node, ensuring ``cluster.name``, ``discovery.seed_hosts``, and ``cluster.initial_master_nodes`` match the first node, whilst setting a unique ``node.name`` and ``network.host`` for each additional node.

4. If TLS is enabled, you must manually copy the TLS certificates from the first node to each additional node. See the `Elasticsearch security documentation <https://www.elastic.co/guide/en/elasticsearch/reference/7.17/security-basic-setup.html>`__ for details.

5. Start Elasticsearch on the additional node:

  .. code-block:: sh

    sudo /bin/systemctl daemon-reload
    sudo /bin/systemctl enable elasticsearch.service
    sudo systemctl start elasticsearch.service

6. Repeat steps 1 through 5 for each additional node.

Disable memory swapping
~~~~~~~~~~~~~~~~~~~~~~~~~

Memory swapping can cause Elasticsearch nodes to respond slowly or disconnect from the cluster entirely. It is strongly recommended to disable swapping on all cluster nodes.

To enable memory locking, add or uncomment the following line in ``elasticsearch.yml`` on each node:

.. code-block:: sh

  bootstrap.memory_lock: true

Then configure the systemd service to permit memory locking. Create or edit the systemd override file:

.. code-block:: sh

  sudo systemctl edit elasticsearch

Add the following content:

.. code-block:: sh

  [Service]
  LimitMEMLOCK=infinity

Reload systemd and restart Elasticsearch:

.. code-block:: sh

  sudo systemctl daemon-reload
  sudo systemctl restart elasticsearch

Verify that memory locking is active by running:

.. code-block:: sh

  curl -X GET "localhost:9200/_nodes?filter_path=**.mlockall"

The response should show ``"mlockall": true`` for each node.

Verify cluster health
~~~~~~~~~~~~~~~~~~~~~~

After all nodes have joined the cluster, verify that the cluster is healthy:

.. code-block:: sh

  curl -X GET "localhost:9200/_cluster/health?pretty"

A healthy cluster returns a ``status`` of ``green``, indicating that all primary and replica shards are allocated. A ``yellow`` status means all primary shards are allocated but some replicas are not yet assigned — this may occur temporarily while the cluster rebalances after a new node joins.

To list all nodes in the cluster:

.. code-block:: sh

  curl -X GET "localhost:9200/_cat/nodes?v"

This should list all nodes with their names, roles, heap usage, and other details. Confirm that the expected number of nodes appears in the output.

Configure Mattermost
---------------------

Follow these steps to configure Mattermost to use your Elasticsearch server and to generate the post index:

1. Go to **System Console > Environment > Elasticsearch**.
2. Set **Enable Elasticsearch Indexing** to ``true`` to enable the other the settings on the page. Once the configuration is saved, new posts made to the database are automatically indexed on the Elasticsearch server.
3. Ensure **Backend type** is set to ``elasticsearch``.

Configure Mattermost for an Elasticsearch cluster
---------------------------------------------------

When connecting Mattermost to an Elasticsearch cluster rather than a single node, the following additional configuration is recommended.

Enable cluster sniffing
~~~~~~~~~~~~~~~~~~~~~~~~

Set **Enable Cluster Sniffing** to ``true`` in **System Console > Environment > Elasticsearch**. Sniffing allows Mattermost to automatically discover and connect to all data nodes in the cluster. With sniffing enabled, you only need to provide the address of one node in the **Server Connection Address** field — Mattermost will find the rest.

This also means that if nodes are added to or removed from the cluster, Mattermost adapts automatically without requiring a configuration change.

Configure index replicas
~~~~~~~~~~~~~~~~~~~~~~~~~

In a cluster, Elasticsearch stores copies of each data shard (called replicas) on different nodes. This provides redundancy — if a node goes down, the data is still available on another node.

Mattermost provides three settings to control the number of replicas for each type of index. For a cluster with *n* data nodes, set the number of replicas for each index to *n-1*:

- **Channel Index Replicas** (``ElasticsearchSettings.ChannelIndexReplicas``)
- **Post Index Replicas** (``ElasticsearchSettings.PostIndexReplicas``)
- **User Index Replicas** (``ElasticsearchSettings.UserIndexReplicas``)

For example, in a three-node cluster, set all three values to ``2``.

These settings can be configured in the ``config.json`` file or via the System Console. See the `enterprise search configuration settings </administration-guide/configure/environment-configuration-settings.html#enterprise-search>`__ documentation for details.

.. important::

  If the number of data nodes in the cluster changes, these replica settings must be updated accordingly. After changing replica settings, purge and rebuild all indexes to apply the new configuration to existing indexes.

Use an index prefix for shared clusters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If multiple Mattermost deployments share a single Elasticsearch cluster, configure a unique **Index Prefix** (``ElasticsearchSettings.IndexPrefix``) for each deployment. This prevents index name collisions between deployments.

.. include:: /administration-guide/scale/common-configure-mattermost-for-enterprise-search.rst
  :start-after: :nosearch:
