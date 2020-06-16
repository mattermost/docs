High Availability Cluster (E20)
===============================

*Available in Enterprise Edition E20.*

A high availability cluster enables a Mattermost system to maintain service during outages and hardware failures through the use of redundant infrastructure.

High availability in Mattermost consists of running redundant Mattermost application servers, redundant database servers, and redundant load balancers. The failure of any one of these components does not interrupt operation of the system.

.. note::

  This document applies to Mattermost Server version 4.0 and later. For previous versions, see :doc:`cluster-310`.

.. contents::
  :backlinks: top
  :local:

Requirements for Continuous Operation
-------------------------------------

To enable continuous operation at all times, including during server updates and server upgrades, you must make sure that the redundant components are properly sized and that you follow the correct sequence for updating each of the system's components.

Redundancy at anticipated scale
  Upon failure of one component, the remaining application servers, database servers, and load balancers must be sized and configured to carry the full load of the system. If this requirement is not met, an outage of one component can result in an overload of the remaining components, causing a complete system outage.

Update sequence for continuous operation
  You can apply most configuration changes and dot release security updates without interrupting service, provided that you update the system components in the correct sequence. See the `Upgrade Guide`_ for instructions on how to do this.

  **Exception:** Changes to configuration settings that require a server restart, and server version upgrades that involve a change to the database schema require a short period of downtime. Downtime for a server restart is around 5 seconds, and for a database schema update, downtime can be up to 30 seconds.

Deployment Guide
----------------

Deployment guide to set up and maintain high availability on your Mattermost servers.

Initial Setup Guide for High Availability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure your instance and configuration are compatible with high availability, please review the `Configuration and Compatibility`_  section.

.. note::
  Backup your Mattermost database and file storage locations before configuring high availability. For more information about backing up, see :doc:`../administration/backup`.

1. Upgrade Mattermost Server to version 4.0 or later. See :doc:`../administration/upgrade`.
2. Set up a new Mattermost server with version 4.0 or later by following one of our **Install Guides**. This server must use an identical copy of the configuration file, ``config.json``. Verify the servers are functioning by hitting each independent server through its private IP address.
3. Modify the ``config.json`` files on both servers to add *ClusterSettings* as described in :ref:`high-availability`.
4. Verify the configuration files are identical on both servers then restart each machine in the cluster.
5. Modify your NGINX setup so that it proxies to both servers. For more information about this, see `Proxy Server Configuration`_.
6. Open **System Console > Advanced > High Availability** in prior versions or **System Console > Environment > High Availability** in versions after 5.12 to verify that each machine in the cluster is communicating as expected with green status indicators. If not, investigate the log files for any extra information.

Adding a Server to the Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Backup your Mattermost database and the file storage location. For more information about backing up, see :doc:`../administration/backup`.
2. Set up a new Mattermost server. This server must use an identical copy of the configuration file, ``config.json``. Verify the server is functioning by hitting the private IP address.
3. Modify your NGINX setup to add the new server. For information about this, see `Proxy Server Configuration`_.
4. Open **System Console > Advanced > High Availability** in prior versions or **System Console > Environment > High Availability** in versions after 5.12 to verify that all the machines in the cluster are communicating as expected with green status indicators. If not, investigate the log files for any extra information.

Removing a Server from the Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Backup your Mattermost database and the file storage location. For more information about backing up, see :doc:`../administration/backup`.
2. Modify your NGINX setup to remove the server. For information about this, see `Proxy Server Configuration`_.
3. Open **System Console > Advanced > High Availability** in prior versions or **System Console > Environment > High Availability** in versions after 5.12 to verify that all the machines remaining in the cluster are communicating as expected with green status indicators. If not, investigate the log files for any extra information.

Configuration and Compatibility
-------------------------------
Details on configuring your system for high availability.

Mattermost Server Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuration Settings
^^^^^^^^^^^^^^^^^^^^^^

1. High availability is configured in the ``ClusterSettings`` section of ``config.json`` and the settings are viewable in the System Console. When high availability is enabled, the System Console is set to read-only mode to ensure all the ``config.json`` files on the Mattermost servers are always identical. However, for testing and validating a High Availability setup, you can set *ReadOnlyConfig* to ``false``, which allows changes made in the System Console to be saved back to the configuration file.

  .. code-block:: none

    "ClusterSettings": {
            "Enable": false,
            "ClusterName": "production",
            "OverrideHostname": "",
            "UseIpAddress": true,
            "UseExperimentalGossip": false,
            "ReadOnlyConfig": true,
            "GossipPort": 8074,
            "StreamingPort": 8075
    }

  For more details on these settings, see :ref:`high-availability`.

2. Change the process limit to 8192 and the maximum number of open files to 65536.

  Modify ``/etc/security/limits.conf`` on each machine that hosts a Mattermost server by adding the following lines:

  .. code-block:: none

    * soft nofile 65536
    * hard nofile 65536
    * soft nproc 8192
    * hard nproc 8192

3. Increase the number of websocket connections

  Modify ``/etc/sysctl.conf`` on each machine that hosts a Mattermost server by adding the following lines:

  .. code-block:: none

    net.ipv4.ip_local_port_range = 1025 65000
    net.ipv4.tcp_fin_timeout = 30
    net.ipv4.tcp_tw_reuse = 1
    net.core.somaxconn = 4096
    net.ipv4.tcp_max_syn_backlog = 8192

You can do the same for the proxy server too.

Cluster Discovery
^^^^^^^^^^^^^^^^^

If you have non-standard (i.e. not simple) network configurations, then you may need to use the `Override Hostname <https://docs.mattermost.com/administration/config-settings.html#override-hostname>`_ setting to help the cluster nodes discover each other. The cluster settings in the config are removed from the config file hash for this reason, meaning you can have ``config.json`` files that are slightly different in High Availability mode. The `Override Hostname <https://docs.mattermost.com/administration/config-settings.html#override-hostname>`_ is intended to be different for each clustered node in ``config.json`` if you need to force discovery.

If ``UseIpAddress`` is set to ``true``, it attempts to obtain the IP address by searching for the first non-local IP address (non-loop-back, non-localunicast, non-localmulticast network interface). It enumerates the network interfaces using the built-in go function `net.InterfaceAddrs() <https://golang.org/pkg/net/#InterfaceAddrs>`_. Otherwise it tries to get the hostname using the `os.Hostname() <https://golang.org/pkg/os/#Hostname>`_ built-in go function.

You can also run ``SELECT * FROM ClusterDiscovery`` against your database to see how it has filled in the Hostname field. That field will be the hostname or IP address the server will use to attempt contact with other nodes in the cluster. We attempt to make a connection to the ``url Hostname:Port`` and ``Hostname:PortGossipPort``. You must also make sure you have all the correct ports open so the cluster can gossip correctly. These ports are under ``ClusterSettings`` in your configuration.

In short, you should use:

 1. IpAddress discovery if the first non-local address can be seen from the other machines.
 2. Override Hostname on the operating system so that it's a proper discoverable name for the other nodes in the cluster.
 3. Override Hostname in ``config.json`` if the above steps do not work. You can put an IpAddress in this field if needed. The ``config.json`` will be different for each cluster node.

Time Synchronization
^^^^^^^^^^^^^^^^^^^^

Each server in the cluster must have the Network Time Protocol daemon ``ntpd`` running so that messages are posted in the correct order.

State
^^^^^

The Mattermost Server is designed to have very little state to allow for horizontal scaling. The items in state considered for scaling Mattermost are listed below:

- In memory session cache for quick validation and channel access
- In memory online/offline cache for quick response
- System configuration file that is loaded and stored in memory
- WebSocket connections from clients used to send messages

When the Mattermost Server is configured for high availability, the servers  use an inter-node communication protocol on a different listening address to keep the state in sync. When a state changes it is written back to the database and an inter-node message is sent to notify the other servers of the state change. The true state of the items can always be read from the database. Mattermost also uses inter-node communication to forward WebSocket messages to the other servers in the cluster for real-time messages such as  “[User X] is typing.”

Proxy Server Configuration
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

File Storage Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
  1. File storage is assumed to be shared between all the machines that are using services such as NAS or Amazon S3.
  2. If ``"DriverName": "local"`` is used then the directory at ``"FileSettings":`` ``"Directory": "./data/"`` is expected to be a NAS location mapped as a local directory, otherwise high availability will not function correctly and may corrupt your file storage.
  3. If you’re using Amazon S3 or Minio for file storage then no other configuration is required.

If you’re using the Compliance Reports feature in Enterprise Edition E20, you need to configure the ``"ComplianceSettings":`` ``"Directory": "./data/",`` to share between all machines or the reports will only be available from the System Console on the local Mattermost server.

Migrating to NAS or S3 from local storage is beyond the scope of this document.

Database Configuration
^^^^^^^^^^^^^^^^^^^^^^

Use the read replica feature to scale the database. The Mattermost server can be set up to use one "master" database and multiple read replica databases. Mattermost distributes read requests across all databases, and sends write requests to the master database, and those changes are then sent to update the read replicas.

On large deployments, consider using the search replica feature to isolate search queries onto one or more database servers. A search replica is similar to a read replica, but is used only for handling search queries.

If there are no search replicas, the server uses the read replicas instead. Similarly, if there are no read replicas, the server falls back to master.

Sizing Databases
````````````````

For information about sizing database servers, see :ref:`hardware-sizing-for-enterprise`.

In a master/slave environment, make sure to size the slave machine to take 100% of the load in the event that the master machine goes down and you need to fail over.

Deploying a Multi-database Configuration
````````````````````````````````````````

To configure a multi-database Mattermost server:

1. Update the ``DataSource`` setting in ``config.json`` with a connection string to your master database server. The connection string is based on the database type set in ``DriverName``, either ``postgres`` or ``mysql``.
2. Update the ``DataSourceReplicas`` setting in ``config.json`` with a series of connection strings to your database read replica servers in the format ``["readreplica1", "readreplica2"]``. Each connection should also be compatible with the ``DriverName`` setting.

Here's an example SqlSettings block for one master and two read replicas:

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

Loading a Multi-database Configuration onto an Active Server
````````````````````````````````````````````````````````````

After a multi-database configuration has been defined in ``config.json``, the following procedure can be used to apply the settings without shutting down the Mattermost server:

1. Go to **System Console > Configuration** in prior versions or **System Console > Environment > Web Server**  and click **Reload Configuration from Disk** in versions after 5.12 to reload configuration settings for the Mattermost server from ``config.json``.
2. Go to **System Console > Database** in prior versions or **System Console > Environment > Database** and click **Recycle Database Connections** in versions after 5.12 to take down existing database connections and set up new connections in the multi-database configuration.

While the connection settings are changing, there might be a brief moment when writes to the master database are unsuccessful. The process waits for all existing connections to finish and starts serving new requests with the new connections. End users attempting to send messages while the switch is happening will have an experience similar to losing connection to the Mattermost server.

Manual Failover for Master Database
```````````````````````````````````

If the need arises to switch from the current master database--for example, if it is running out of disk space, or requires maintenance updates, or for other reasons--you can switch Mattermost server to use one of its read replicas as a master database by updating ``DataSource`` in ``config.json``.

To apply the settings without shutting down the Mattermost server:

1. Go to **System Console > Configuration** in prior versions or **System Console > Environment > Web Server** and click **Reload Configuration from Disk** in versions after 5.12 to reload configuration settings for the Mattermost server from ``config.json``.
2. Go to **System Console > Database** in prior versions or **System Console > Environment > Database** and click **Recycle Database Connections** in versions after 5.12 to take down existing database connections and set up new connections in the multi-database configuration.

While the connection settings are changing, there might be a brief moment when writes to the master database are unsuccessful. The process waits for all existing connections to finish and starts serving new requests with the new connections. End users attempting to send messages while the switch is happening can have an experience similar to losing connection to the Mattermost server.

Transparent Failover
````````````````````

The database can be configured for high availability and transparent failover use the existing database technologies. We recommend MySQL Clustering, Postgres Clustering, or Amazon Aurora. Database transparent failover is beyond the scope of this documentation.

Leader Election
^^^^^^^^^^^^^^^^

In Mattermost v4.2 and later, a cluster leader election process assigns any scheduled task such as LDAP sync to run on a single node in a multi-node cluster environment.

The process is based on a widely used `bully leader election algorithm <https://en.wikipedia.org/wiki/Bully_algorithm>`__ where the process with the lowest node ID number from amongst the non-failed processes is selected as the "leader". 

Job Server
^^^^^^^^^^^^^^^^

Mattermost runs periodic tasks via the `job server <https://docs.mattermost.com/administration/config-settings.html#jobs>`__. These tasks include:

 - LDAP sync
 - Data retention
 - Compliance exports
 - Elasticsearch indexing

Make sure you have set ``JobSettings.RunScheduler`` to ``true`` in config.json for all app and job servers in the cluster. The cluster leader will then be responsible for scheduling recurring jobs.

Plugins and High Availability
^^^^^^^^^^^^^^^^

As of Mattermost 5.14, when you install or upgrade a plugin, it is propagated across the servers in the cluster automatically.

File storage is assumed to be shared between all the machines that are using services such as NAS or Amazon S3.

If ``"DriverName": "local"`` is used then the directory at ``"FileSettings":`` ``"Directory": "./data/"`` is expected to be a NAS location mapped as a local directory. If this is not the case high availability will not function correctly and may corrupt your file storage.

Note a slight behavior change in 5.15:
When you reinstall a plugin in 5.14, the previous **Enabled** or **Disabled** state is retained. As of 5.15, a reinstalled plugin's initial state is **Disabled**.

Upgrade Guide
-------------

An update is an incremental change to Mattermost server that fixes bugs or performance issues. An upgrade adds new or improved functionality to the server.

Updating Configuration Changes While Operating Continuously
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A service interruption is not required for most configuration updates. See `Server Upgrades Requiring Service Interruption`_ for a list of configuration updates that require a service interruption.

You can apply updates during a period of low load, but if your HA cluster is sized correctly, you can do it at any time. The system downtime is brief, and depends on the number of Mattermost servers in your cluster. Note that you are not restarting the machines, only the Mattermost server applications. A Mattermost server restart generally takes about 5 seconds.

.. note::

  Do not modify configuration settings through the System Console. Otherwise you will have two servers with different `config.json` files in an HA cluster causing a refresh every time a user connects to a different app server.

1. Make a backup of your existing ``config.json`` file.
2. For one of the Mattermost servers, make the configuration changes to ``config.json`` and save the file. Do not reload the file yet.
3. Copy the ``config.json`` file to the other servers.
4. Shut down Mattermost on all but one server.
5. Reload the configuration file on the server that is still running. Go to **System Console > Configuration** in prior versions or **System Console > Environment > Web Server** in versions after 5.12 and click **Reload Configuration from Disk**
6. Start the other servers.

Updating Server Version While Operating Continuously
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A service interruption is not required for security patch dot releases of the Mattermost server.

You can apply updates during a period when the anticipated load is small enough that one server can carry the full load of the system during the update.

Note that you are not restarting the machines, only the Mattermost server applications. A Mattermost server restart generally takes about 5 seconds.

1. Review the upgrade procedure in the *Upgrade Enterprise Edition* section of :doc:`../administration/upgrade`.
2. Make a backup of your existing ``config.json`` file.
3. Set your proxy to move all new requests to a single server. If you are using NGINX and it's configured with an upstream backend section in ``/etc/nginx/sites-available/mattermost`` then comment out all but the one server that you intend to update first, and reload NGINX.
4. Shut down Mattermost on each server except the one that you are updating first.
5. Update each Mattermost instance that is shut down.
6. On each server, replace the new ``config.json`` file with your backed-up copy.
7. Start the Mattermost servers.
8. Repeat the update procedure for the server that was left running.

Server Upgrades Requiring Service Interruption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A service interruption is required when the upgrade includes a change to the database schema or when a change to ``config.json`` requires a server restart, such as when making the following changes:

  * Default Server Language
  * Rate Limiting
  * Webserver Mode
  * Database
  * High Availability

If the upgrade includes a change to the database schema, the database is upgraded by the first server that starts.

Apply upgrades during a period of low load. The system downtime is brief, and depends on the number of Mattermost servers in your cluster. Note that you are not restarting the machines, only the Mattermost server applications.

1. Review the upgrade procedure in the *Upgrade Enterprise Edition* section of :doc:`../administration/upgrade`.
2. Make a backup of your existing ``config.json`` file.
3. Stop NGINX.
4. Upgrade each Mattermost instance.
5. On each server, replace the new ``config.json`` file with your backed-up copy.
6. Start one of the Mattermost servers.
7. When the server is running, start the other servers.
8. Restart NGINX.

Upgrading to Version 4.0 and Later
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Starting with Mattermost Server version 4.0, when a server starts up it can automatically discover other servers in the same cluster. You can add and remove servers without the need to make changes to the configuration file, ``config.json``. To support this capability, new items were added to the *ClusterSettings* section of ``config.json``. When upgrading from 3.10 or earlier to 4.0 or later, you must manually add the new items to your existing ``config.json``.

1. Review the upgrade procedure in :doc:`../administration/upgrade`.
2. Make a backup of your existing ``config.json`` file.
3. Revise your existing ``config.json`` to update the *ClusterSettings* section. The following settings should work in most cases:

  .. code-block:: none

    "ClusterSettings": {
        "Enable": true,
        "ClusterName": "production",
        "OverrideHostname": "",
        "UseIpAddress": true,
        "UseExperimentalGossip": false,
        "ReadOnlyConfig": true,
        "GossipPort": 8074,
        "StreamingPort": 8075
    },

  For more information about these settings, see :ref:`high-availability`.
4. Stop NGINX.
5. Upgrade each Mattermost instance.
6. On each server, replace the new ``config.json`` file with your modified version.
7. Start one of the Mattermost servers.
8. When the server is running, start the other servers.
9. Restart NGINX.

Frequently Asked Questions (FAQ)
---------------------------------

Does Mattermost support multi-region high availability deployment?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. Although not officially tested, you can set up a cluster across AWS regions, for example, and it should work without issues.

Troubleshooting
---------------

Red Server Status
~~~~~~~~~~~~~~~~~

When high availability is enabled, the System Console displays the server status as red or green, indicating if the servers are communicating correctly with the cluster. The servers use inter-node communication to ping the other machines in the cluster, and once a ping is established the servers exchange information, such as server version and configuration files.

A server status of red can occur for the following reasons:

- **Configuration file mismatch**: Mattermost will still attempt the inter-node communication, but the System Console will show a red status for the server since the high availability feature assumes the same configuration file to function properly.
- **Server version mismatch**: Mattermost will still attempt the inter-node communication, but the System Console will show a red status for the server since the high availability feature assumes the same version of Mattermost is installed on each server in the cluster. It is recommended to use the `latest version of Mattermost <https://www.mattermost.org/download/>`__ on all servers. Follow the upgrade procedure in :doc:`../administration/upgrade` for any server that needs to be upgraded.
- **Server is down**: If an inter-node communication fails to send a message it makes another attempt in 15 seconds. If the second attempt fails, the server is assumed to be down. An error message is written to the logs and the System Console shows a status of red for that server. The inter-node communication continues to ping the down server in 15 second intervals. When the server comes back up, any new messages are sent to it.

WebSocket Disconnect
~~~~~~~~~~~~~~~~~~~~

When a client WebSocket receives a disconnect it will automatically attempt to re-establish a connection every three seconds with a backoff. After the connection is established, the client attempts to receive any messages that were sent while it was disconnected.

App Refreshes Continuously
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When configuration settings are modified through the System Console, the client refreshes every time a user connects to a different app server. This occurs because the servers have different `config.json` files in an HA cluster.

Modify configuration settings directly through ``config.json`` `following these steps <https://docs.mattermost.com/deployment/cluster.html#updating-configuration-changes-while-operating-continuously>`__.

Messages Do Not Post Until After Reloading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When running in high-availability mode, make sure all Mattermost application servers are running the same version of Mattermost. If they are running different versions, it can lead to a state where the lower version app server cannot handle a request and the request will not be sent until the frontend application is refreshed and sent to a server with a valid Mattermost version. Symptoms to look for include requests failing seemingly at random or a single application server having a drastic rise in goroutines and API errors.
