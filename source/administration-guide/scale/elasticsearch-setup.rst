Elasticsearch server setup
===========================

.. include:: ../../_static/badges/ent-plus.rst
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

Configure Mattermost
---------------------

Follow these steps to configure Mattermost to use your Elasticsearch server and to generate the post index:

1. Go to **System Console > Environment > Elasticsearch**.
2. Set **Enable Elasticsearch Indexing** to ``true`` to enable the other the settings on the page. Once the configuration is saved, new posts made to the database are automatically indexed on the Elasticsearch server.
3. Ensure **Backend type** is set to ``elasticsearch``.

.. include:: /administration-guide/scale/common-configure-mattermost-for-enterprise-search.rst
  :start-after: :nosearch: