Troubleshooting high scale deployments
=======================================

This page provides troubleshooting guidance for high scale Mattermost deployments with 100 users or more.

If these steps do not resolve the issue, and you have a `paid subscription to a Mattermost offering </about/editions-and-offerings.html>`_, please reach out to our customer support team via our `online support portal <https://support.mattermost.com/hc/en-us/requests/new>`_. 

Additionally, peer-to-peer support is available for all Mattermost users in our `troubleshooting forum <https://forum.mattermost.com/c/trouble-shoot>`__ and on our `community server <https://community.mattermost.com/core/channels/peer-to-peer-help>`_. 

My system keeps hanging when I search for a message in Mattermost
---------------------------------------------------------------------

First, check how many messages have been posted on your system, including deleted posts and posts made using automations.

Go to the **System Console > Reporting > Site Statistics** and review the **Total Posts** figure reported. If this figure is above 3,000,000 posts, we recommend deploying Elasticsearch alongside your Mattermost server for improved search performance. 

How do I deploy Elasticsearch for Mattermost?
---------------------------------------------------------------------

Below are the steps to install Elasticsearch on a RHEL 8 machine. These steps include adjusting the data directory for Elasticsearch to be mounted on ``/data`` folder.

For additional guidance, see how to `deploy an Elasticsearch server </scale/elasticsearch.html>`__.

1 - Download and install the RPM

.. code-block:: bash

  wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.10.2-x86_64.rpm
  sudo rpm --install elasticsearch-7.10.2-x86_64.rpm

**Expected Output:**

.. code-block:: bash

  [elasticsearch ~]$ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.10.2-x86_64.rpm
  --2023-04-28 14:44:29--  https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.10.2-x86_64.rpm
  Resolving artifacts.elastic.co (artifacts.elastic.co)... 34.120.127.130, 2600:1901:0:1d7::
  Connecting to artifacts.elastic.co (artifacts.elastic.co)|34.120.127.130|:443... connected.
  HTTP request sent, awaiting response... 200 OK
  Length: 318859205 (304M) [application/octet-stream]
  Saving to: ‘elasticsearch-7.10.2-x86_64.rpm’

  elasticsearch-7.10.2-x86_64.rpm         100%[=============================================================================>] 304.09M  23.4MB/s    in 14s

  2023-04-28 14:44:44 (22.1 MB/s) - ‘elasticsearch-7.10.2-x86_64.rpm’ saved [318859205/318859205]

  [elasticsearch ~]$
  [elasticsearch ~]$ sudo rpm --install elasticsearch-7.10.2-x86_64.rpm
  warning: elasticsearch-7.10.2-x86_64.rpm: Header V4 RSA/SHA512 Signature, key ID d88e42b4: NOKEY
  Creating elasticsearch group... OK
  Creating elasticsearch user... OK
  ### NOT starting on installation, please execute the following statements to configure elasticsearch service to start automatically using systemd
   sudo systemctl daemon-reload
   sudo systemctl enable elasticsearch.service
  ### You can start elasticsearch service by executing
   sudo systemctl start elasticsearch.service
  Created elasticsearch keystore in /etc/elasticsearch/elasticsearch.keystore
  /usr/lib/tmpfiles.d/elasticsearch.conf:1: Line references path below legacy directory /var/run/, updating /var/run/elasticsearch → /run/elasticsearch; please update the tmpfiles.d/ drop-in file accordingly.
  [elasticsearch ~]$


2 - Setup Elastic with `systemd`

.. code-block:: bash

  sudo /bin/systemctl daemon-reload
  sudo /bin/systemctl enable elasticsearch.service
  sudo systemctl start elasticsearch.service

**Expected Output**

.. code-block:: bash

  [elasticsearch ~]$ sudo /bin/systemctl daemon-reload
  sudo /bin/systemctl enable elasticsearch.service
  sudo systemctl start elasticsearch.service
  Synchronizing state of elasticsearch.service with SysV service script with /usr/lib/systemd/systemd-sysv-install.
  Executing: /usr/lib/systemd/systemd-sysv-install enable elasticsearch
  Created symlink /etc/systemd/system/multi-user.target.wants/elasticsearch.service → /usr/lib/systemd/system/elasticsearch.service.
  [elasticsearch ~]$

3 - Confirm Elasticsearch is working on the Elastic server

.. code-block:: bash
  curl localhost:9200

**Expected Output**

.. code-block:: bash

  [elasticsearch ~]$ curl localhost:9200
  {
    "name" : "ip-172-31-80-220.ec2.internal",
    "cluster_name" : "elasticsearch",
    "cluster_uuid" : "dq-SHv0vS023zi1ZhTd_Hw",
    "version" : {
      "number" : "7.10.2",
      "build_flavor" : "default",
      "build_type" : "rpm",
      "build_hash" : "747e1cc71def077253878a59143c1f785afa92b9",
      "build_date" : "2021-01-13T00:42:12.435326Z",
      "build_snapshot" : false,
      "lucene_version" : "8.7.0",
      "minimum_wire_compatibility_version" : "6.8.0",
      "minimum_index_compatibility_version" : "6.0.0-beta1"
    },
    "tagline" : "You Know, for Search"
  }
  [elasticsearch ~]$

4 - Get your network interface name

.. code-block:: bash
  ip addr

**Expected Output**

Look for the public interface name, in the below example it's the ``eth0`` interface. This interface will be the one that is bound to your public IP address. Copy your interface name and use it in the next step.

.. code-block:: bash

  [elasticsearch etc]$ ip addr
  1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
      link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
      inet 127.0.0.1/8 scope host lo
         valid_lft forever preferred_lft forever
      inet6 ::1/128 scope host
         valid_lft forever preferred_lft forever
  2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc mq state UP group default qlen 1000
      link/ether 12:52:a0:a2:8d:55 brd ff:ff:ff:ff:ff:ff
      altname enX0
      inet 172.31.80.220/20 brd 172.31.95.255 scope global dynamic noprefixroute eth0
         valid_lft 2786sec preferred_lft 2786sec
      inet6 fe80::1052:a0ff:fea2:8d55/64 scope link
         valid_lft forever preferred_lft forever
  [elasticsearch etc]$

5 - Edit the Elastic config

.. code-block:: bash

  vi /etc/elasticsearch/elasticsearch.yml

**New Config**

Replace ``_eth0_`` with your interface name from step 4.

.. code-block:: diff

  # ---------------------------------- Network -----------------------------------
  #
  # Set the bind address to a specific IP (IPv4 or IPv6):
  #
  # 
  + network.host: _eth0_
  - #network.host: 192.168.0.1
  #
  # Set a custom port for HTTP:
  #
  # http.port: 9200
  #
  # For more information, consult the network module documentation.
  #
  # --------------------------------- Discovery ----------------------------------
  #
  # Pass an initial list of hosts to perform discovery when this node is started:
  # The default list of hosts is ["127.0.0.1", "[::1]"]
  #
  + discovery.type: single-node
  # discovery.seed_hosts: ["host1", "host2"]
  #
  # Bootstrap the cluster using an initial set of master-eligible nodes:
  #
  # cluster.initial_master_nodes: ["node-1", "node-2"]
  #
  # For more information, consult the discovery and cluster formation module documentation.
  #

6 - Restart Elasticsearch

.. code-block:: bash

  sudo systemctl stop elasticsearch
  sudo systemctl start elasticsearch

7 - Check the ports are listening

.. code-block:: bash

  netstat -plnt

You should see the below ports. The ones we are interested in are the ones listening on `9200` / `9300`. Confirm these are listening on your server's IP address. It should look similar to the below. 

.. code-block:: bash

  (Not all processes could be identified, non-owned process info
   will not be shown, you would have to be root to see it all.)
  Active Internet connections (only servers)
  Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
  tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      -
  tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
  tcp6       0      0 :::111                  :::*                    LISTEN      -
  tcp6       0      0 fe80::1052:a0ff:fe:9200 :::*                    LISTEN      -
  tcp6       0      0 172.31.80.220:9200      :::*                    LISTEN      -
  tcp6       0      0 fe80::1052:a0ff:fe:9300 :::*                    LISTEN      -
  tcp6       0      0 172.31.80.220:9300      :::*                    LISTEN      -
  tcp6       0      0 :::22                   :::*                    LISTEN      -

8 - Adjust the Elasticsearch default directories

Below, you are creating an Elasticsearch directory within the `/data` mount and giving it the proper permissions.

.. code-block:: bash

  cd /data
  mkdir -p ./elasticsearch/{data,logs}
  sudo chown -R root:elasticsearch ./elasticsearch
  sudo chmod -R g+w ./elasticsearch
  vi /etc/elasticsearch/elasticsearch.yml

.. code-block:: diff

  # ----------------------------------- Paths ------------------------------------
  #
  # Path to directory where to store the data (separate multiple locations by comma):
  #
  + path.data: /data/elasticsearch/data
  - path.data: /var/lib/elasticsearch
  #
  # Path to log files:
  #
  + path.logs: /data/elasticsearch/logs
  - path.logs: /var/log/elasticsearch
  #

9 - Install the `icu-analyzer` plugin

Plugins will always be installed to `/usr/share/elasticsearch/plugins` per Elasticsearch.

.. code-block:: bash
  sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu

**Expected Output**

.. code-block:: bash

  [elasticsearch bin]$ sudo /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu
  -> Installing analysis-icu
  -> Downloading analysis-icu from elastic
  [=================================================] 100%
  -> Installed analysis-icu
  [elasticsearch bin]$

10 - Test the connection from Mattermost to Elasticsearch

Open a terminal session to the Mattermost server

If this completes successfully, your Elasticsearch is fully configured.

.. code-block:: bash
  curl 172.31.80.220:9200

**Expected Output**

.. code-block:: bash

  [mattermost ]$ curl 172.31.80.220:9200
  {
    "name" : "ip-172-31-80-220.ec2.internal",
    "cluster_name" : "elasticsearch",
    "cluster_uuid" : "dq-SHv0vS023zi1ZhTd_Hw",
    "version" : {
      "number" : "7.10.2",
      "build_flavor" : "default",
      "build_type" : "rpm",
      "build_hash" : "747e1cc71def077253878a59143c1f785afa92b9",
      "build_date" : "2021-01-13T00:42:12.435326Z",
      "build_snapshot" : false,
      "lucene_version" : "8.7.0",
      "minimum_wire_compatibility_version" : "6.8.0",
      "minimum_index_compatibility_version" : "6.0.0-beta1"
    },
    "tagline" : "You Know, for Search"
  }
  [mattermost]$

11 - Set up Elasticsearch within Mattermost

Open your web browser to the system console of the production Mattermost server.

  1. Navigate to `System Console > Environment > Elasticsearch`
  2. Set `Enable Elasticsearch Indexing` to `true`
  3. Adjust the `Server Connection Address` to be your Elasticsearch IP and port
    - example: `http://ipAddress:9200`
  4. Click `Test Connection`
  5. Save the config

12 - Index your posts

On the same page as step 11, click the `Build Index` button. This will take a few hours to complete fully.

13 - Enable Elasticsearch

Once the index above is fully done, you'll want to enable ES to be used for queries or autocomplete.

  1. Navigate to `System Console > Environment > Elasticsearch`
  2. Set `Enable Elasticsearch for search queries` to `true`
  3. Set `Enable Elasticsearch for autocomplete` to `true`
  4. Save the config
  5. Make a search, confirm it works.
