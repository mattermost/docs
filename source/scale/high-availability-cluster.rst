High availability cluster
=========================

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

A High availability cluster enables a Mattermost system to maintain service during outages and hardware failures through the use of redundant infrastructure.

High availability in Mattermost consists of running redundant Mattermost application servers, redundant database servers, and redundant load balancers. The failure of any one of these components does not interrupt operation of the system.

Requirements for continuous operation
-------------------------------------

To enable continuous operation at all times, including during server updates and server upgrades, you must make sure that the redundant components are properly sized and that you follow the correct sequence for updating each of the system's components.

Redundancy at anticipated scale
  Upon failure of one component, the remaining application servers, database servers, and load balancers must be sized and configured to carry the full load of the system. If this requirement is not met, an outage of one component can result in an overload of the remaining components, causing a complete system outage.

Update sequence for continuous operation
  You can apply most configuration changes and dot release security updates without interrupting service, provided that you update the system components in the correct sequence. See the `upgrade guide`_ for instructions on how to do this.

  **Exception:** Changes to configuration settings that require a server restart, and server version upgrades that involve a change to the database schema, require a short period of downtime. Downtime for a server restart is around five seconds. For a database schema update, downtime can be up to 30 seconds.

Deployment guide
----------------

Deployment guide to set up and maintain high availability on your Mattermost servers. This document doesn't cover the configuration of databases in terms of disaster recovery, however, you can refer to the `frequently asked questions (FAQ)`_ section for our recommendations.

Initial setup guide for high availability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure your instance and configuration are compatible with high availability, please review the `configuration and compatibility`_ section.

.. note::
  
  Back up your Mattermost database and file storage locations before configuring high availability. For more information about backing up, see :doc:`../deploy/backup-disaster-recovery`.

1. Set up a new Mattermost server that uses an identical copy of the configuration file, ``config.json``. Verify the servers are functioning by hitting each independent server through its private IP address.
2. Modify the ``config.json`` files on both servers to add ``ClusterSettings``. See the `high availability configuration settings </configure/environment-configuration-settings.html#high-availability>`__ documentation for details.
3. Verify the configuration files are identical on both servers then restart each machine in the cluster.
4. Modify your NGINX setup so that it proxies to both servers. For more information about this, see `proxy server configuration <https://docs.mattermost.com/install/setup-nginx-proxy.html>`__ documentation for details.
5. Open **System Console > Environment > High Availability** to verify that each machine in the cluster is communicating as expected with green status indicators. If not, investigate the log files for any extra information.

Add a server to the cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Back up your Mattermost database and the file storage location. For more information about backing up, see :doc:`../deploy/backup-disaster-recovery`.
2. Set up a new Mattermost server. This server must use an identical copy of the configuration file, ``config.json``. Verify the server is functioning by hitting the private IP address.
3. Modify your NGINX setup to add the new server.
4. Open **System Console > Environment > High Availability** to verify that all the machines in the cluster are communicating as expected with green status indicators. If not, investigate the log files for any extra information.

Remove a server from the cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Back up your Mattermost database and the file storage location. For more information about backing up, see :doc:`../deploy/backup-disaster-recovery`.
2. Modify your NGINX setup to remove the server. For information about this, see `proxy server configuration <https://docs.mattermost.com/install/setup-nginx-proxy.html>`__ documentation for details..
3. Open **System Console > Environment > High Availability** to verify that all the machines remaining in the cluster are communicating as expected with green status indicators. If not, investigate the log files for any extra information.

Configuration and compatibility
-------------------------------

Details on configuring your system for High Availability.

Mattermost Server configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuration settings
^^^^^^^^^^^^^^^^^^^^^^

1. High availability is configured in the ``ClusterSettings`` section of ``config.json`` and the settings are viewable in the System Console. When high availability is enabled, the System Console is set to read-only mode to ensure all the ``config.json`` files on the Mattermost servers are always identical. However, for testing and validating a high availability setup, you can set ``ReadOnlyConfig`` to ``false``, which allows changes made in the System Console to be saved back to the configuration file.

  .. code-block:: none

    "ClusterSettings": {
            "Enable": false,
            "ClusterName": "production",
            "OverrideHostname": "",
            "UseIpAddress": true,
            "ReadOnlyConfig": true,
            "GossipPort": 8074
    }

  For more details on these settings, see the `high availability configuration settings </configure/environment-configuration-settings.html#high-availability>`__ documentation.

2. Change the process limit to 8192 and the maximum number of open files to 65536.

  Modify ``/etc/security/limits.conf`` on each machine that hosts a Mattermost server by adding the following lines:

  .. code-block:: none

    * soft nofile 65536
    * hard nofile 65536
    * soft nproc 8192
    * hard nproc 8192

3. Increase the number of WebSocket connections:

  Modify ``/etc/sysctl.conf`` on each machine that hosts a Mattermost server by adding the following lines:

  .. code-block:: none

    net.ipv4.ip_local_port_range = 1025 65000
    net.ipv4.tcp_fin_timeout = 30
    net.ipv4.tcp_tw_reuse = 1
    net.core.somaxconn = 4096
    net.ipv4.tcp_max_syn_backlog = 8192

You can do the same for the proxy server.

Cluster discovery
^^^^^^^^^^^^^^^^^

If you have non-standard (i.e. complex) network configurations, then you may need to use the `Override Hostname </configure/environment-configuration-settings.html#ha-overridehostname>`__ setting to help the cluster nodes discover each other. The cluster settings in the config are removed from the config file hash for this reason, meaning you can have ``config.json`` files that are slightly different in high availability mode. The Override Hostname is intended to be different for each clustered node in ``config.json`` if you need to force discovery.

If ``UseIpAddress`` is set to ``true``, it attempts to obtain the IP address by searching for the first non-local IP address (non-loop-back, non-localunicast, non-localmulticast network interface). It enumerates the network interfaces using the built-in go function `net.InterfaceAddrs() <https://golang.org/pkg/net/#InterfaceAddrs>`__. Otherwise it tries to get the hostname using the `os.Hostname() <https://golang.org/pkg/os/#Hostname>`__ built-in go function.

You can also run ``SELECT * FROM ClusterDiscovery`` against your database to see how it has filled in the **Hostname** field. That field will be the hostname or IP address the server will use to attempt contact with other nodes in the cluster. We attempt to make a connection to the ``url Hostname:Port`` and ``Hostname:PortGossipPort``. You must also make sure you have all the correct ports open so the cluster can gossip correctly. These ports are under ``ClusterSettings`` in your configuration.

In short, you should use:

1. IP address discovery if the first non-local address can be seen from the other machines.
2. Override Hostname on the operating system so that it's a proper discoverable name for the other nodes in the cluster.
3. Override Hostname in ``config.json`` if the above steps do not work. You can put an IP address in this field if needed. The ``config.json`` will be different for each cluster node.

Time synchronization
^^^^^^^^^^^^^^^^^^^^

Each server in the cluster must have the Network Time Protocol daemon ``ntpd`` running so that messages are posted in the correct order.

State
^^^^^

The Mattermost server is designed to have very little state to allow for horizontal scaling. The items in state considered for scaling Mattermost are listed below:

- In memory session cache for quick validation and channel access.
- In memory online/offline cache for quick response.
- System configuration file that is loaded and stored in memory.
- WebSocket connections from clients used to send messages.

When the Mattermost server is configured for high availability, the servers  use an inter-node communication protocol on a different listening address to keep the state in sync. When a state changes it is written back to the database and an inter-node message is sent to notify the other servers of the state change. The true state of the items can always be read from the database. Mattermost also uses inter-node communication to forward WebSocket messages to the other servers in the cluster for real-time messages such as “[User X] is typing.”

Proxy server configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

The proxy server exposes the cluster of Mattermost servers to the outside world. The Mattermost servers are designed for use with a proxy server such as NGINX, a hardware load balancer, or a cloud service like Amazon Elastic Load Balancer.

If you want to monitor the server with a health check you can use ``http://10.10.10.2/api/v4/system/ping`` and check the response for ``Status 200``, indicating success. Use this health check route to mark the server *in-service* or *out-of-service*.

A sample configuration for NGINX is provided below. It assumes that you have two Mattermost servers running on private IP addresses of ``10.10.10.2`` and ``10.10.10.4``.

.. code-block:: none

    upstream backend {
            server 10.10.10.2:8065;
            server 10.10.10.4:8065;
      }

      server {
          server_name mattermost.example.com;

          location ~ /api/v[0-9]+/(users/)?websocket$ {
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
                client_max_body_size 50M;
                proxy_set_header Host $http_host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
                proxy_set_header X-Frame-Options SAMEORIGIN;
                proxy_buffers 256 16k;
                proxy_buffer_size 16k;
                proxy_read_timeout 600s;
                proxy_http_version 1.1;
                proxy_pass http://backend;
          }

          location / {
                client_max_body_size 50M;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
                proxy_set_header Host $http_host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
                proxy_set_header X-Frame-Options SAMEORIGIN;
                proxy_pass http://backend;
          }
    }

You can use multiple proxy servers to limit a single point of failure, but that is beyond the scope of this documentation.

File storage configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

  1. File storage is assumed to be shared between all the machines that are using services such as NAS or Amazon S3.
  2. If ``"DriverName": "local"`` is used then the directory at ``"FileSettings":`` ``"Directory": "./data/"`` is expected to be a NAS location mapped as a local directory, otherwise high availability will not function correctly and may corrupt your file storage.
  3. If you’re using Amazon S3 or MinIO for file storage then no other configuration is required.

If you’re using the Compliance Reports feature in Mattermost Enterprise, you need to configure the ``"ComplianceSettings":`` ``"Directory": "./data/",`` to share between all machines or the reports will only be available from the System Console on the local Mattermost server.

Migrating to NAS or S3 from local storage is beyond the scope of this document.

Database configuration
^^^^^^^^^^^^^^^^^^^^^^

.. tip::

  Specifying configuration setting values using Mattermost environment variables ensure that they always take precedent over any other configuration settings.

For an AWS High Availability RDS cluster deployment, point the `datasource </configure/environment-configuration-settings.html#database-datasource>`__ configuration setting to the write/read endpoint at the **cluster** level to benefit from the AWS failover handling. AWS takes care of promoting different database nodes to be the writer node. Mattermost doesn't need to manage this. 

Use the `read replica </configure/environment-configuration-settings.html#database-readreplicas>`__ feature to scale the database. The Mattermost server can be set up to use one master database and one or more read replica databases. 

.. note::
  
  For an AWS High Availability RDS cluster deployment, don't hard-code the IP addresses. Point this configuration setting to the write/read endpoint at the **cluster** level. This will benefit from the AWS failover handling where AWS takes care of promoting different database nodes to be the writer node. Mattermost doesn't need to manage this. 

On large deployments, also consider using the `search replica </configure/environment-configuration-settings.html#search-replicas>`__ feature to isolate search queries onto one or more search replicas. A search replica is similar to a read replica, but is used only for handling search queries.

.. note::

  For an AWS High Availability RDS cluster deployment, don't hard-code the IP addresses. Point this configuration setting directly to the underlying read-only node endpoints within the RDS cluster. We recommend circumventing the failover/load balancing that AWS/RDS takes care of (except for the write traffic). Mattermost has its own method of balancing the read-only connections, and can also balance those queries to the DataSource/write+read connection should those nodes fail. 

Mattermost distributes queries as follows:

* All write requests, and some specific read requests, are sent to the master.
* All other read requests (excluding those specific queries that go to the master) are distributed among the available read replicas. If no read replicas are available, these are sent to the master instead.
* Search requests are distributed among the available search replicas. If no search replicas are available, these are sent to the read replicas instead (or, if no read replicas are available, to the master).

Size the databases
``````````````````

For information about sizing database servers, see :ref:`hardware-sizing-for-enterprise`.

In a master/slave environment, make sure to size the slave machine to take 100% of the load in the event that the master machine goes down and you need to fail over.

Deploy a multi-database configuration
``````````````````````````````````````

To configure a multi-database Mattermost server:

1. Update the ``DataSource`` setting in ``config.json`` with a connection string to your master database server.
2. Update the ``DataSourceReplicas`` setting in ``config.json`` with a series of connection strings to your database read replica servers in the format ``["readreplica1", "readreplica2"]``. Each connection should also be compatible with the ``DriverName`` setting.

Here's an example ``SqlSettings`` block for one master and two read replicas:

.. code-block:: none

  "SqlSettings": {
        "DriverName": "mysql",
        "DataSource": "master_user:master_password@tcp(master.server)/mattermost?charset=utf8mb4,utf8\u0026readTimeout=30s\u0026writeTimeout=30s",
        "DataSourceReplicas": ["slave_user:slave_password@tcp(replica1.server)/mattermost?charset=utf8mb4,utf8\u0026readTimeout=30s\u0026writeTimeout=30s","slave_user:slave_password@tcp(replica2.server)/mattermost?charset=utf8mb4,utf8\u0026readTimeout=30s\u0026writeTimeout=30s"],
        "DataSourceSearchReplicas": [],
        "MaxIdleConns": 20,
        "MaxOpenConns": 300,
        "Trace": false,
        "AtRestEncryptKey": "",
        "QueryTimeout": 30
    }  

The new settings can be applied by either stopping and starting the server, or by loading the configuration settings as described in the next section.

Once loaded, database write requests are sent to the master database and read requests are distributed among the other databases in the list.

Load a multi-database configuration onto an active server
`````````````````````````````````````````````````````````

After a multi-database configuration has been defined in ``config.json``, the following procedure can be used to apply the settings without shutting down the Mattermost server:

1. Go to **System Console > Environment > Web Server**, then select **Reload Configuration from Disk** to reload configuration settings for the Mattermost server from ``config.json``.
2. Go to **System Console > Environment > Database**, then select **Recycle Database Connections** to take down existing database connections and set up new connections in the multi-database configuration.

While the connection settings are changing, there might be a brief moment when writes to the master database are unsuccessful. The process waits for all existing connections to finish and starts serving new requests with the new connections. End users attempting to send messages while the switch is happening will have an experience similar to losing connection to the Mattermost server.

Manual failover for master database
```````````````````````````````````

If the need arises to switch from the current master database - for example, if it is running out of disk space, or requires maintenance updates, or for other reasons - you can switch Mattermost server to use one of its read replicas as a master database by updating ``DataSource`` in ``config.json``.

To apply the settings without shutting down the Mattermost server:

1. Go to **System Console > Environment > Web Server**, then select **Reload Configuration from Disk** to reload configuration settings for the Mattermost server from ``config.json``.
2. Go to **System Console > Environment > Database**, then select **Recycle Database Connections** to take down existing database connections and set up new connections in the multi-database configuration.

While the connection settings are changing, there might be a brief moment when writes to the master database are unsuccessful. The process waits for all existing connections to finish and starts serving new requests with the new connections. End users attempting to send messages while the switch is happening can have an experience similar to losing connection to the Mattermost server.

Transparent failover
````````````````````

The database can be configured for high availability and transparent failover use the existing database technologies. We recommend PostgreSQL Clustering or Amazon Aurora. Database transparent failover is beyond the scope of this documentation.

Recommended configuration settings for PostgreSQL
``````````````````````````````````````````````````

If you're using PostgreSQL as the choice of database, we recommend the following configuration optimizations on your Mattermost server. These configurations were tested on an AWS Aurora r5.xlarge instance of PostgreSQL 11.7. There are also some general optimizations mentioned which requires servers with higher specifications.

**Config for Postgres Primary or Writer node**

.. code-block:: bash

  # If the instance is lower capacity than r5.xlarge, then set it to a lower number. 
  # Also tune the "MaxOpenConns" setting under the "SqlSettings" of the Mattermost app accordingly. 
  # Note that "MaxOpenConns" on Mattermost is per data source name.
  max_connections = 1024

  # Set it to 1.1, unless the DB is using spinning disks.
  random_page_cost = 1.1

  # This should be 32MB if using read replicas, or 16MB if using a single PostgreSQL instance. 
  # If the instance is of a lower capacity than r5.xlarge, then set it to a lower number.
  work_mem = 32MB

  # Set both of the below settings to 65% of total memory. For a 32 GB instance, it should be 21 GB.
  # If on a smaller server, set this to 20% or less total RAM.
  # ex: 512MB would work for a 4GB RAM server
  effective_cache_size = 21GB
  shared_buffers = 21GB

  # If you are using pgbouncer, or any similar connection pooling proxy, 
  # in front of your DB, then apply the keepalive settings to the proxy instead, 
  # and revert the keepalive settings for the DB back to defaults.
  tcp_keepalives_idle = 5
  tcp_keepalives_interval = 1
  tcp_keepalives_count = 5

  # 1GB (reduce this to 512MB if your server has less than 32GB of RAM)
  maintenance_work_mem = 512MB
  
  autovacuum_max_workers = 4
  autovacuum_vacuum_cost_limit = 500


  # If you have more than 32 CPUs on your database server, please set the following options to utilize more CPU for your server:
  max_worker_processes = 12
  max_parallel_workers_per_gather = 4
  max_parallel_workers = 12
  max_parallel_maintenance_workers = 4

**Config for Postgres Replica node**

Copy all the above settings to the read replica, and modify or add only the below. 

.. code-block:: bash
  
  # If the instance is lower capacity than r5.xlarge, then set it to a lower number. 
  # Also tune the "MaxOpenConns" setting under the "SqlSettings" of the Mattermost app accordingly. 
  # Note that "MaxOpenConns" on Mattermost is per data source name.
  max_connections = 1024

  # This setting should be 16MB on read nodes, and 32MB on writer nodes
  work_mem = 16MB

  # The below settings allow the reader to return query results even when the primary has a write process running, a query conflict. 
  # This is set to on because of the high volume of write traffic that can prevent the reader from returning query results within the timeout. 
  # https://www.postgresql.org/docs/current/hot-standby.html#HOT-STANDBY-CONFLICT
  hot_standby = on
  hot_standby_feedback = on

Leader election
^^^^^^^^^^^^^^^^

A cluster leader election process assigns any scheduled task such as LDAP sync to run on a single node in a multi-node cluster environment.

The process is based on a widely used `bully leader election algorithm <https://en.wikipedia.org/wiki/Bully_algorithm>`__ where the process with the lowest node ID number from amongst the non-failed processes is selected as the leader.

Job server
^^^^^^^^^^^

Mattermost runs periodic tasks via the `job server </configure/configuration-settings.html#jobs>`__. These tasks include:

- LDAP sync
- Data retention
- Compliance exports
- Elasticsearch indexing

Make sure you have set ``JobSettings.RunScheduler`` to ``true`` in ``config.json`` for all app and job servers in the cluster. The cluster leader will then be responsible for scheduling recurring jobs.

.. note::

  It is strongly recommended not to change this setting from the default setting of ``true`` as this prevents the ``ClusterLeader`` from being able to run the scheduler. As a result, recurring jobs such as LDAP sync, Compliance Export, and data retention will no longer be scheduled.

In previous Mattermost Server versions, and this documentation, the instructions stated to run the Job Server with ``RunScheduler: false``. The cluster design has evolved and this is no longer the case.

Plugins and High Availability
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you install or upgrade a plugin, it's propagated across the servers in the cluster automatically. File storage is assumed to be shared between all the servers, using services such as NAS or Amazon S3.

If ``"DriverName": "local"`` is used then the directory at ``"FileSettings":`` ``"Directory": "./data/"`` is expected to be a NAS location mapped as a local directory. If this is not the case High Availability will not function correctly and may corrupt your file storage.

When you reinstall a plugin in v5.14, the previous **Enabled** or **Disabled** state is retained. As of v5.15, a reinstalled plugin's initial state is **Disabled**.

CLI and High Availability
^^^^^^^^^^^^^^^^^^^^^^^^^

The CLI is run in a single node which bypasses the mechanisms that a `high availability environment </scale/high-availability-cluster.html>`__ uses to perform actions across all nodes in the cluster. As a result, when running `CLI commands </manage/command-line-tools.html>`__ in a High Availability environment, tasks such as updating and deleting users or changing configuration settings require a server restart.

We recommend using `mmctl </manage/mmctl-command-line-tool.html>`__ in a high availability environment instead since a server restart is not required. These changes are made through the API layer, so the node receiving the change request notifies all other nodes in the cluster.

Upgrade guide
-------------

An update is an incremental change to Mattermost server that fixes bugs or performance issues. An upgrade adds new or improved functionality to the server.

Update configuration changes while operating continuously
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A service interruption is not required for most configuration updates. See the section below for details on upgrades requiring service interruption. You can apply updates during a period of low load, but if your high availability cluster is sized correctly, you can do it at any time. The system downtime is brief, and depends on the number of Mattermost servers in your cluster. Note that you are not restarting the machines, only the Mattermost server applications. A Mattermost server restart generally takes about five seconds.

.. note::

  Don't modify configuration settings through the System Console, otherwise you'll have two servers with different ``config.json`` files in a high availability cluster causing a refresh every time a user connects to a different app server.

1. Make a backup of your existing ``config.json`` file.
2. For one of the Mattermost servers, make the configuration changes to ``config.json`` and save the file. Do not reload the file yet.
3. Copy the ``config.json`` file to the other servers.
4. Shut down Mattermost on all but one server.
5. Reload the configuration file on the server that is still running. Go to **System Console > Environment > Web Server**, then select **Reload Configuration from Disk**.
6. Start the other servers.

Update the Server version while operating continuously
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A service interruption is not required for security patch dot releases of Mattermost Server. You can apply updates during a period when the anticipated load is small enough that one server can carry the full load of the system during the update.

.. note::

  Mattermost supports one minor version difference between the server versions when performing a rolling upgrade (for example v5.27.1 + v5.27.2 or v5.26.4 + v5.27.1 is supported, whereas v5.25.5 + v5.27.0 is not supported). Running two different versions of Mattermost in your cluster should not be done outside of an upgrade scenario.

When restarting, you aren't restarting the machines, only the Mattermost server applications. A Mattermost server restart generally takes about five seconds.

1. Review the upgrade procedure in the *Upgrade Enterprise Edition* section of :doc:`../upgrade/upgrading-mattermost-server`.
2. Make a backup of your existing ``config.json`` file.
3. Set your proxy to move all new requests to a single server. If you are using NGINX and it's configured with an upstream backend section in ``/etc/nginx/sites-available/mattermost`` then comment out all but the one server that you intend to update first, and reload NGINX.
4. Shut down Mattermost on each server except the one that you are updating first.
5. Update each Mattermost instance that is shut down.
6. On each server, replace the new ``config.json`` file with your backed up copy.
7. Start the Mattermost servers.
8. Repeat the update procedure for the server that was left running.

Server upgrades requiring service interruption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A service interruption is required when the upgrade includes a change to the database schema or when a change to ``config.json`` requires a server restart, such as when making the following changes:

- Default server language
- Rate limiting
- Webserver mode
- Database
- High availability

If the upgrade includes a change to the database schema, the database is upgraded by the first server that starts.

Apply upgrades during a period of low load. The system downtime is brief, and depends on the number of Mattermost servers in your cluster. Note that you are not restarting the machines, only the Mattermost server applications.

1. Review the upgrade procedure in the *Upgrade Enterprise Edition* section of :doc:`../upgrade/upgrading-mattermost-server`.
2. Make a backup of your existing ``config.json`` file.
3. Stop NGINX.
4. Upgrade each Mattermost instance.
5. On each server, replace the new ``config.json`` file with your backed up copy.
6. Start one of the Mattermost servers.
7. When the server is running, start the other servers.
8. Restart NGINX.

Upgrade to version 4.0 and later
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a server starts up, it can automatically discover other servers in the same cluster. You can add and remove servers without the need to make changes to the configuration file, ``config.json``. To support this capability, new items were added to the ``ClusterSettings`` section of ``config.json``. 

1. Review the upgrade procedure in :doc:`../upgrade/upgrading-mattermost-server`.
2. Make a backup of your existing ``config.json`` file.
3. Revise your existing ``config.json`` to update the ``ClusterSettings`` section. The following settings should work in most cases:

  .. code-block:: none

    "ClusterSettings": {
        "Enable": true,
        "ClusterName": "production",
        "OverrideHostname": "",
        "UseIpAddress": true,
        "ReadOnlyConfig": true,
        "GossipPort": 8074
    },

  For more information about these settings, see the `high availability configuration settings </configure/environment-configuration-settings.html#high-availability>`__ documentation.

4. Stop NGINX.
5. Upgrade each Mattermost instance.
6. On each server, replace the new ``config.json`` file with your modified version.
7. Start one of the Mattermost servers.
8. When the server is running, start the other servers.
9. Restart NGINX.

All cluster nodes must use a single protocol
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All cluster traffic uses the gossip protocol. `Gossip clustering can no longer be disabled </configure/configuration-settings.html#use-gossip>`__.

When upgrading a high availability cluster, you can't upgrade other nodes in the cluster when one node isn't using the gossip protocol. You must use gossip to complete a high availability upgrade. Alternatively you can shut down all nodes and bring them all up individually following an upgrade.

Frequently asked questions (FAQ)
---------------------------------

Does Mattermost support multi-region high availability deployment?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. Although not officially tested, you can set up a cluster across AWS regions, for example, and it should work without issues.

What does Mattermost recommend for disaster recovery of the databases?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When deploying Mattermost in a high availability configuration, we recommend using a database load balancer between Mattermost and your database. Depending on your deployment this needs more or less consideration.

For example, if you're deploying Mattermost on AWS with Amazon Aurora we recommend utilizing multiple Availability Zones. If you're deploying Mattermost on your own cluster please consult with your IT team for a solution best suited for your existing architecture.

Troubleshooting
---------------

Capture high availability troubleshooting data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When deploying Mattermost in a high availability configuration, we recommend that you keep Prometheus and Grafana metrics as well as cluster server logs for as long as possible - and at minimum two weeks. 

You may be asked to provide this data to Mattermost for analysis and troubleshooting purposes.

.. note::

  - Ensure that server log files are being created. You can find more on working with Mattermost logs `here </install/troubleshooting.html#review-mattermost-logs>`__.
  - When investigating and replicating issues, we recommend opening **System Console > Environment > Logging** and setting **File Log Level** to **DEBUG** for more complete logs. Make sure to revert to **INFO** after troubleshooting to save disk space. 
  - Each server has its own server log file, so make sure to provide server logs for all servers in your High Availability cluster.

Red server status
~~~~~~~~~~~~~~~~~

When high availability is enabled, the System Console displays the server status as red or green, indicating if the servers are communicating correctly with the cluster. The servers use inter-node communication to ping the other machines in the cluster, and once a ping is established the servers exchange information, such as server version and configuration files.

A server status of red can occur for the following reasons:

- **Configuration file mismatch:** Mattermost will still attempt the inter-node communication, but the System Console will show a red status for the server since the high availability feature assumes the same configuration file to function properly.
- **Server version mismatch:** Mattermost will still attempt the inter-node communication, but the System Console will show a red status for the server since the high availability feature assumes the same version of Mattermost is installed on each server in the cluster. It is recommended to use the `latest version of Mattermost <https://mattermost.com/download/>`__ on all servers. Follow the upgrade procedure in :doc:`../upgrade/upgrading-mattermost-server` for any server that needs to be upgraded.
- **Server is down:** If an inter-node communication fails to send a message it makes another attempt in 15 seconds. If the second attempt fails, the server is assumed to be down. An error message is written to the logs and the System Console shows a status of red for that server. The inter-node communication continues to ping the down server in 15 second intervals. When the server comes back up, any new messages are sent to it.

WebSocket disconnect
~~~~~~~~~~~~~~~~~~~~

When a client WebSocket receives a disconnect it will automatically attempt to re-establish a connection every three seconds with a backoff. After the connection is established, the client attempts to receive any messages that were sent while it was disconnected.

App refreshes continuously
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When configuration settings are modified through the System Console, the client refreshes every time a user connects to a different app server. This occurs because the servers have different ``config.json`` files in a high availability cluster.

Modify configuration settings directly through ``config.json`` `following these steps </scale/high-availability-cluster.html#updating-configuration-changes-while-operating-continuously>`__.

Messages do not post until after reloading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When running in high availability mode, make sure all Mattermost application servers are running the same version of Mattermost. If they are running different versions, it can lead to a state where the lower version app server cannot handle a request and the request will not be sent until the frontend application is refreshed and sent to a server with a valid Mattermost version. Symptoms to look for include requests failing seemingly at random or a single application server having a drastic rise in goroutines and API errors.
