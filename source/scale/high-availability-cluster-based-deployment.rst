High availability cluster-based deployment
===========================================

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

A high availability cluster-based deployment ensures that Mattermost stays up and running during outages or hardware failures by using redundant infrastructure. This setup includes multiple Mattermost application servers, database servers, and load balancers. If one component fails, the system continues to operate without interruption.

Follow the guidance on this page to `deploy <high-availability-deployment-guide>`__ and `upgrade <#high-availability-upgrade-guide>`__ your Mattermost server for high availability. Ensure all `<#high-availability-prerequisites-&-requirements>`__ are in place before starting.

.. important::

   Mattermost doesn't support high availability deployments spanning multiple datacenters. All nodes in a high availability cluster must reside within the same datacenter to ensure proper functionality and performance.

High availability prerequisites & requirements
----------------------------------------------

You'll need familiarity with the following:

- Basic database management (e.g., PostgreSQL replication and failover).
- Reverse proxy configuration (e.g., NGINX, AWS ELB).
- Linux system administration (e.g., managing file descriptors, system limits, and logs).

See the following sections for additional prerequisites and requirements.

Infrastructure
~~~~~~~~~~~~~~~

- **Multiple nodes**: At least 2 Mattermost application nodes (e.g., in AWS EC2, on-prem servers, or containers) must be deployed and networked.
- **Load balancer/Reverse proxy**: A load balancer (e.g., AWS ELB, NGINX) must be set up to distribute traffic across the Mattermost nodes. It should handle session persistence and support failover.
- **Shared storage**: File storage must be shared across all nodes:

  - **Recommended**: Amazon S3 or other S3-compatible services (e.g., MinIO).
  - **Alternatively**: A shared network-attached storage (NAS) mounted on all nodes.

- Database Setup:

  - Deploy a master PostgreSQL database with one or more read replicas configured.
  - For AWS deployments, use an RDS cluster with a cluster-level endpoint for master/failover handling.
  - Database sizing:

    - Ensure the master database can handle both write and read traffic if no replicas are temporarily available.
    - Read replicas must be correctly sized to offload queries, such as search queries.
    - A read replica for your database could be of additional benefit.

.. tip::

  **Transitioning from a single-node to a multi-node high availability setup?**

  If you have an instance deployed in AWS as a single EC2, and want to ensure a supported high availability deployment, create a second EC2 node like your existing one. Both should incorporate the settings and configurations required, with a load balancer or reverse proxy in front which can handle a session switch-over. 

Network and connectivity
~~~~~~~~~~~~~~~~~~~~~~~~~

- **Internal networking**:

  - All nodes must be able to communicate via private networking (ensure proper firewall rules or subnet configurations).
  - Ports for inter-node communication (default: ``8074`` for Mattermost gossip) must be open.

- **Outbound internet access** (if applicable):

  - For outbound traffic (e.g., Elasticsearch or AWS services), ensure nodes can reach necessary external endpoints.

Time synchronization
~~~~~~~~~~~~~~~~~~~~~

Ensure all nodes are synchronized using Network Time Protocol, ntpd, or Chrony. Accurate timestamps are critical for database replication, cluster communication, and log consistency. Ensuring all servers have synchronized clocks is a foundational step, as it impacts every subsequent configuration. Without correct time synchronization, cluster operations and state coordination could fail or behave unpredictably.

Ensure ``ntpd`` is running on all servers by running ``sudo service ntpd start``.

Database
~~~~~~~~~

- Compatibility: Use :ref:`supported database versions <install/software-hardware-requirements:database software>`
- Database sizing:

  - Ensure the master database can handle both write and read traffic if no replicas are temporarily available.
  - Read replicas must be correctly sized to offload queries, such as search queries.

File descriptor/process limits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Update limits on all nodes to handle high traffic:

  - Set file descriptors: ``nofile`` (e.g., ``65,536`` or higher).
  - Set process limits: ``nproc`` (e.g., ``8192`` or higher).

Proxy server configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **WebSocket Support**: Ensure your load balancer or reverse proxy is configured to support WebSocket connections (e.g., for real-time messaging events).
- **Health Checks**: Use ``http://<server>:8065/api/v4/system/ping`` for load balancer health probes.
- **SSL Termination**: If applicable, configure SSL for secure access.
- Cluster-specific configuration

  - Each node must use unique node identifiers, use the same cluster name, and :ref:`enable clustering <configure/environment-configuration-settings:enable high availability mode>`.

Use-case specific
~~~~~~~~~~~~~~~~~~

Depending on your use case, the following prerequisites may also be required:

- **Search Setup**: If using Elasticsearch for enterprise search, an Elasticsearch cluster must be deployed before enabling it in Mattermost.
- **Plugins**: For plugin usage, ensure shared file storage is properly configured (NAS/S3) to propagate plugins across all nodes.
- **Compliance & data retention**: Enable any required compliance features (e.g., audit logging, compliance exports) and configure shared directories or destinations.

Continuous operation
~~~~~~~~~~~~~~~~~~~~~

To ensure uninterrupted operation during server updates and upgrades:  

- **Proper Redundancy**: Ensure all components, including application servers, database servers, and load balancers, are correctly sized and configured to handle full system load in case of a failure. Lack of proper sizing can lead to system-wide outages. See the :doc:`scaling for Enterprise </scale/scaling-for-enterprise>` for details.
- **Correct Update Sequence**: Most configuration changes and dot release updates can be applied without service interruption if components are updated in the proper sequence. Minimal downtime of approximately 5 seconds for server restarts and up to 30 seconds for schema updates is expected. Learn more about `upgrading a highly available deployment <#upgrade-guide>`__.

High Availability deployment guide
-----------------------------------

Get started checklist
~~~~~~~~~~~~~~~~~~~~~

Now that you're aware of the prerequisites, ensure you meet all of the following:

- Multiple servers deployed (EC2/VM/containers).
- Database properly configured with master/replicas.
- File storage shared and accessible.
- Load balancer or reverse proxy in place.
- Time synchronization enabled on all nodes.
- Necessary ports open and network connectivity verified.
- System configurations (e.g., file descriptors and process limits) updated.

Once these prerequisites are satisfied, proceed with the deployment!

.. important::

  Back up your Mattermost database and file storage locations before configuring high availability. For more information about backing up, see :doc:`../deploy/backup-disaster-recovery`.

Database configuration
~~~~~~~~~~~~~~~~~~~~~~~

The database is the core of Mattermost's functionality. Setting up master/replica configurations and ensuring database performance and failover capabilities come before the application layer configuration.

Key recommendations:

- Use :doc:`environment variables </configure/environment-variables>`: Prioritize environment variables for database configuration to ensure they take precedence over ``config.json``.
- Leverage AWS Failover Features: For AWS RDS clusters, point the :ref:`DataSource <configure/environment-configuration-settings:database datasource>` to the cluster-level endpoint for automatic handling of writer node promotion during failover.
- Scale with :ref:`Read Replicas <configure/environment-configuration-settings:read replicas>` to distribute read queries, and use :ref:`Search Replicas <configure/environment-configuration-settings:search replicas>` to isolate search-related queries.

Master and replica configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Cluster-Level DataSource example
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Define your SqlSettings in config.json for master and replicas:

.. code-block:: sql

  NEED PG-SPECIFIC DETAILS HERE
  "SqlSettings": {
    "DriverName": "mysql",
    "DataSource": "master_user:master_password@tcp(master.server)/mattermost?charset=utf8mb4,utf8&readTimeout=30s&writeTimeout=30s",
    "DataSourceReplicas": [
      "replica_user:replica_password@tcp(replica1.server)/mattermost?charset=utf8mb4,utf8&readTimeout=30s&writeTimeout=30s",
      "replica_user:replica_password@tcp(replica2.server)/mattermost?charset=utf8mb4,utf8&readTimeout=30s&writeTimeout=30s"
    ],
    "DataSourceSearchReplicas": [],
    "MaxIdleConns": 20,
    "MaxOpenConns": 300
  }

.. note::

  - No Hard-Coded IPs: Use cluster-level endpoints for AWS RDS to avoid manual management during failover.
  - Writes go to the master (or failover replica once promoted).
  - Reads are distributed among available read replicas by Mattermost.
 
Multi-database setup
^^^^^^^^^^^^^^^^^^^^

1.	Update ``DataSource`` and ``DataSourceReplicas``.
2.	Apply the new database configuration:

  - Reload the Configuration: Navigate to **System Console > Environment > Web Server** and select **Reload Configuration from Disk**.
  - Recycle Connections: Go to **System Console > Environment > Database** and select **Recycle Database Connections**.

A brief downtime may occur during reconfiguration, similar to a temporary connection loss for end users.
 
Manage failovers
^^^^^^^^^^^^^^^^^^

Manual failover: Update ``DataSource`` to point to a new master, and reload and recycle settings via the System Console as outlined above.

Transparent failover: Transparent failover setups are beyond the scope of this document. 

Automatic failover: use database technologies such as PostgreSQL Clustering or Amazon Aurora.

 
PostgreSQL optimization (Optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For improved performance, apply the following recommendations:

Primary Node:

- ``max_connections = 1024``
- ``random_page_cost = 1.1``
- ``effective_cache_size = 21GB``
- ``shared_buffers = 21GB``
- ``tcp_keepalives_idle = 5``
- ``tcp_keepalives_interval = 1``
- ``tcp_keepalives_count = 5``
- ``maintenance_work_mem = 512MB``
- ``autovacuum_max_workers = 4``
- ``autovacuum_vacuum_cost_limit = 500``
- ``max_worker_processes = 12``
- ``max_parallel_workers_per_gather = 4``
- ``max_parallel_workers = 12``
- ``max_parallel_maintenance_workers = 4``

Replica Node (in addition to the primary node settings above):

- ``work_mem = 16MB``
- ``hot_standby = on``
- ``hot_standby_feedback = on``

File storage
~~~~~~~~~~~~

Proper shared storage setup for files (e.g., NAS/S3) is another fundamental requirement before progressing to configuring the application.

For shared storage:

- Use NAS or S3 for ``DriverName``: ``local``. Migrating to NAS or S3 from local storage is beyond the scope of this document.
- Ensure ``Directory``: ``./data/`` is accessible by all cluster nodes.

For compliance reports, share the location assigned to ``ComplianceSettings":"Directory``.

Mattermost server configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once the database and file storage are in place, focus on configuring the Mattermost server (e.g., cluster settings, ports, etc.)

Cluster settings
^^^^^^^^^^^^^^^^

Update the following ClusterSettings configuration settings:

+---------------------------------------------------------------------------------------------+---------------+-----------------------------------------------------------------+
| **Setting**                                                                                 | **Default**   | **Description**                                                 |
+=============================================================================================+===============+=================================================================+
| :ref:`Enable <configure/environment-configuration-settings:enable high availability mode>`  | false         | Enable high availability.                                       |
+---------------------------------------------------------------------------------------------+---------------+-----------------------------------------------------------------+
| :ref:`ClusterName <configure/environment-configuration-settings:cluster name>`              | "production"  | Name of your cluster.                                           |
+------------------+---------------+----------------------------------------------------------+---------------+-----------------------------------------------------------------+
| :ref:`ReadOnlyConfig <configure/environment-configuration-settings:read only config>`       | ``true``      | Set to ``false`` for testing. Not recommended in production.    |
+---------------------------------------------------------------------------------------------+---------------+-----------------------------------------------------------------+
| :ref:`GossipPort <configure/environment-configuration-settings:gossip port>`                | ``8074``      | Port for inter-node communication.                              |
+------------------+---------------+----------------------------------------------------------+---------------+-----------------------------------------------------------------+


.. code-block:: bash

  "ClusterSettings": {
      "Enable": true,
      "ClusterName": "production",
      "OverrideHostname": "",
      "UseIpAddress": true,
      "ReadOnlyConfig": true,
      "GossipPort": 8074
  }

For advanced settings, see the :ref:`high availability configuration settings <configure/environment-configuration-settings:high availability>` documentation.

File descriptors and process limits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update file/process limits in ``/etc/security/limits.conf``:

- ``soft nofile 65536``
- ``hard nofile 65536``
- ``soft nproc 8192``
- ``hard nproc 8192``

Network settings
^^^^^^^^^^^^^^^^

Optimize network configurations in ``/etc/sysctl.conf`` on each machine that hosts a Mattermost server:

.. code-block:: bash

  net.ipv4.ip_local_port_range = 1025 65000
  net.ipv4.tcp_fin_timeout = 30
  net.ipv4.tcp_tw_reuse = 1
  net.core.somaxconn = 4096
  net.ipv4.tcp_max_syn_backlog = 8192
  vm.min_free_kbytes = 167772
  net.ipv4.tcp_congestion_control = bbr
  net.core.default_qdisc = fq
  net.ipv4.tcp_mem = 1638400 1638400 1638400

Apply similar optimizations to your proxy server.

Cluster discovery
~~~~~~~~~~~~~~~~~

After the basic server configuration, enable node discovery to ensure servers in the cluster can find and communicate with each other.

If using custom network configurations:

- Use :ref:`OverrideHostname <configure/environment-configuration-settings:override hostname>` for per-server configurations.
- Ensure :ref:`UseIpAddress <configure/environment-configuration-settings:use ip address>` is set to ``true`` for automatic discovery of the first non-local IP.

Verify discovery settings via the database: ``SELECT * FROM ClusterDiscovery;``

Ensure necessary ports are open for inter-node communication.

State synchronization
~~~~~~~~~~~~~~~~~~~~~

Once nodes can communicate, synchronize session data and WebSocket messages across nodes through inter-node communication.

High availability depends on real-time synchronization:

- In-memory session cache
- WebSocket connections for real-time communication
- Shared configuration state (synchronized via the database)

Proxy server configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

With the cluster set up, configure a load balancer or proxy server (e.g., NGINX) to distribute traffic across the nodes.

Example configuration for NGINX:

.. code-block:: bash

  upstream backend {
      server 10.10.10.2:8065;
      server 10.10.10.4:8065;
      keepalive 256;
  }

  server {
      listen 80;
      server_name mattermost.example.com;

      location / {
          proxy_pass http://backend;
          proxy_cache mattermost_cache;
          client_max_body_size 100M;
      }

      location ~ /api/v[0-9]+/(users/)?websocket$ {
          proxy_pass http://backend;
          proxy_set_header Connection "upgrade";
      }
  }

Leader election
~~~~~~~~~~~~~~~~

Configure the leader election process to handle tasks like LDAP synchronization, ensuring only one node executes scheduled tasks at a time.

- **Purpose**: Assigns scheduled tasks (e.g., LDAP sync) to a single node in a multi-node cluster.
- **Mechanism**: Uses the bully algorithm : https://en.wikipedia.org/wiki/Bully_algorithm to elect a leader. The node with the lowest ID among non-failed processes becomes the leader.
 
Job server
~~~~~~~~~~~

After leader election, configure periodic tasks, such as :doc:`compliance exports </comply/compliance-export>`, :ref:`synchronize LDAP <configure/authentication-configuration-settings:ad/ldap synchronize now>`, :doc:`data retention </comply/data-retention-policy>`, or :ref:`Elasticsearch indexing <configure/environment-configuration-settings:enable elasticsearch indexing>`, to use the job server for execution.

:ref:`Enable RunScheduler <configure/experimental-configuration-settings:run scheduler>` for all servers in the cluster. This setting should remain ``true``. Changing it prevents the leader from scheduling recurring jobs.
 
Plugins
~~~~~~~~

Now that the cluster is fully operational, ensure Mattermost plugins are properly deployed and functioning across all nodes.

- Automatic plugin propagation: When adding or upgrading plugins, they are automatically distributed across cluster nodes if shared file storage (e.g., NAS, S3) is in use.
- File storage: Ensure the :ref:`FileSettings.Directory <configure/environment-configuration-settings:local storage directory>` is a shared NAS location (``./data/``). Failure to do so could corrupt storage or disrupt high availability functionality.
- Plugin State on reinstallation:

  - v5.14 and earlier: Retains previous Enabled/Disabled state.
  - v5.15 and later: Starts in a Disabled state by default.

mmctl
~~~~~~

We recommend using :doc:`mmctl commands </manage/mmctl-command-line-tool>` to make changes in a high availability environment because mmctl commands interact through the API layer to notify all nodes of changes, and no server restarts are required.

Review cluster status
---------------------

Once you've set up new Mattermost servers with identical copies of the configuration, Verify the servers are functioning by hitting each independent server through its private IP address. Restart each machine in the cluster.

Open **System Console > Environment > High Availability** to verify that each machine in the cluster is communicating as expected with green status indicators. If not, investigate the log files for any extra information.

Add a server to the cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Back up your Mattermost database and the file storage location. For more information about backing up, see :doc:`../deploy/backup-disaster-recovery`.
2. Set up a new Mattermost server. This server must use an identical copy of the configuration file, ``config.json``. Verify the server is functioning by hitting the private IP address.
3. Modify your NGINX setup to add the new server.
4. Open **System Console > Environment > High Availability** to verify that all the machines in the cluster are communicating as expected with green status indicators. If not, investigate the log files for any extra information.

Remove a server from the cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Back up your Mattermost database and the file storage location. For more information about backing up, see :doc:` the documentation </deploy/backup-disaster-recovery>`.
2. Modify your NGINX setup to remove the server. For information about this, see :ref:`proxy server configuration <install/setup-nginx-proxy:manage the nginx process>` documentation for details.
3. Open **System Console > Environment > High Availability** to verify that all the machines remaining in the cluster are communicating as expected with green status indicators. If not, investigate the log files for any extra information.

High Availability upgrade guide
--------------------------------

An update is an incremental change to Mattermost server that fixes bugs or performance issues. An upgrade adds new or improved functionality to the server.

Update configuration changes while operating continuously
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A service interruption is not required for most configuration updates. See the section below for details on upgrades requiring service interruption. You can apply updates during a period of low load, but if your high availability cluster-based deployment is sized correctly, you can do it at any time. The system downtime is brief, and depends on the number of Mattermost servers in your cluster. Note that you are not restarting the machines, only the Mattermost server applications. A Mattermost server restart generally takes about five seconds.

.. note::

  Don't modify configuration settings through the System Console, otherwise you'll have two servers with different ``config.json`` files in a high availability cluster-based deployment causing a refresh every time a user connects to a different app server.

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

All cluster nodes must use a single protocol
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All cluster traffic uses the gossip protocol. :ref:`Gossip clustering can no longer be disabled <configure/deprecated-configuration-settings:use gossip>`.

When upgrading a high availability cluster-based deployment, you can't upgrade other nodes in the cluster when one node isn't using the gossip protocol. You must use gossip to complete this type of upgrade. Alternatively you can shut down all nodes and bring them all up individually following an upgrade.

Frequently asked questions (FAQ)
---------------------------------

Does Mattermost support multi-region high availability cluster-based deployment?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. Although not officially tested, you can set up a cluster across AWS regions, for example, and it should work without issues.

What does Mattermost recommend for disaster recovery of the databases?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When deploying Mattermost in a high availability configuration, we recommend using a database load balancer between Mattermost and your database. Depending on your deployment this needs more or less consideration.

For example, if you're deploying Mattermost on AWS with Amazon Aurora we recommend utilizing multiple Availability Zones. If you're deploying Mattermost on your own cluster please consult with your IT team for a solution best suited for your existing architecture.

How to find the hostname of the connected websocket?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From Mattermost v10.4, Enterprise customers running self-hosted deployments can go to the **Product** menu |product-list| and select **About Mattermost** to see the hostname of the node in the cluster running Mattermost.


Troubleshooting
----------------

Capture high availability troubleshooting data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When deploying Mattermost in a high availability configuration, we recommend that you keep Prometheus and Grafana metrics as well as cluster server logs for as long as possible - and at minimum two weeks. 

You may be asked to provide this data to Mattermost for analysis and troubleshooting purposes.

.. note::

  - Ensure that server log files are being created. You can find more on working with Mattermost logs :ref:`here <install/troubleshooting:review mattermost logs>`.
  - When investigating and replicating issues, we recommend opening **System Console > Environment > Logging** and setting **File Log Level** to **DEBUG** for more complete logs. Make sure to revert to **INFO** after troubleshooting to save disk space. 
  - Each server has its own server log file, so make sure to provide server logs for all servers in your High Availability cluster-based deployment.

Red server status
~~~~~~~~~~~~~~~~~

When high availability mode is enabled, the System Console displays the server status as red or green, indicating if the servers are communicating correctly with the cluster. The servers use inter-node communication to ping the other machines in the cluster, and once a ping is established the servers exchange information, such as server version and configuration files.

A server status of red can occur for the following reasons:

- **Configuration file mismatch:** Mattermost will still attempt the inter-node communication, but the System Console will show a red status for the server since the high availability mode feature assumes the same configuration file to function properly.
- **Server version mismatch:** Mattermost will still attempt the inter-node communication, but the System Console will show a red status for the server since the high availability mode feature assumes the same version of Mattermost is installed on each server in the cluster. It is recommended to use the `latest version of Mattermost <https://mattermost.com/download/>`__ on all servers. Follow the upgrade procedure in :doc:`../upgrade/upgrading-mattermost-server` for any server that needs to be upgraded.
- **Server is down:** If an inter-node communication fails to send a message it makes another attempt in 15 seconds. If the second attempt fails, the server is assumed to be down. An error message is written to the logs and the System Console shows a status of red for that server. The inter-node communication continues to ping the down server in 15 second intervals. When the server comes back up, any new messages are sent to it.

WebSocket disconnect
~~~~~~~~~~~~~~~~~~~~

When a client WebSocket receives a disconnect it will automatically attempt to re-establish a connection every three seconds with a backoff. After the connection is established, the client attempts to receive any messages that were sent while it was disconnected.

App refreshes continuously
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When configuration settings are modified through the System Console, the client refreshes every time a user connects to a different app server. This occurs because the servers have different ``config.json`` files in a high availability cluster-based deployment.

Modify configuration settings directly through ``config.json`` :ref:`following these steps <scale/high-availability-cluster-based-deployment:update configuration changes while operating continuously>`.

Messages do not post until after reloading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When running in high availability mode, make sure all Mattermost application servers are running the same version of Mattermost. If they are running different versions, it can lead to a state where the lower version app server cannot handle a request and the request will not be sent until the frontend application is refreshed and sent to a server with a valid Mattermost version. Symptoms to look for include requests failing seemingly at random or a single application server having a drastic rise in goroutines and API errors.
