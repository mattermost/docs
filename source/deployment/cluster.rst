High Availability Cluster (E20)
===============================

The high availability cluster feature enables a Mattermost system to maintain service during outages and hardware failures through the use of redundant infrastructure. It is available only in Enterprise Edition E20. 

High availability in Mattermost consists of running redundant Mattermost application servers, redundant database servers, and redundant load balancers. The failure of any one of these components does not interrupt operation of the system.

.. contents::
  :backlinks: top
  :local:
  
Continuous Operation During Server Updates
------------------------------------------

To ensure uninterrupted service during updates, you must make sure that the components are properly sized and that you follow the correct sequence for updating the system components.

Each application server, database, and load balancer must be sized and configured to carry the full load of the system. If this requirement is not met, an outage of one component can result in an overload of the remaining components, causing a complete system outage.

You can apply most configuration changes and dot release security updates without interrupting service, provided that you update the system components in the correct sequence. Exceptions to this rule are changes to configuration settings that require a server restart, and updates that involve a change to the database schema. Downtime for a server restart is around 5 seconds, and for a database schema update, downtime is around 30 seconds.

The following outline describes the procedure for updating a high availability system without a service interruption.

1. **Disconnect redundant servers** - Configure load balancers to consolidate requests to a single application server capable of supporting anticipated traffic during the update process. Depending on the resources available, you might choose to run updates during low traffic periods.
2. **Apply single server update** - Apply the update to a single server by updating ``config.json`` and running a command to load the new configuration into the application server, which continues to operate without down time.
3. **Apply update to redundant servers** - Apply the same updates to the redundant servers.
4. **Reconnect redundant servers** - Configure load balancers to once again balance traffic across all application servers.

For specific instructions, see the `Update Guide`_

Deployment Guide
----------------

Deployment guide to setup and maintain high availability on your Mattermost servers.

Initial Setup Guide for High Availability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure your instance and configuration are compatible with high availability, please review the `Configuration and Compatibility`_  section.

.. note:: Backup your `Mattermost database <https://docs.mattermost.com/deployment/cluster.html#database-configuration>`_ and `file storage locations <https://docs.mattermost.com/deployment/cluster.html#file-storage-configuration>`_ before configuring high availability.

1. Follow our :doc:`../administration/upgrade` to upgrade your Mattermost server to v3.3 or later. 
2. Setup a new Mattermost server with v3.3 or later following one of our **Install Guides**. This server must use an identical copy of the configuration file, ``config.json``. Verify the servers are functioning by hitting each independent server through its private IP address.
3. Modify the ``config.json`` files on both servers to add the ``ClusterSettings`` as described in the *High Availability (Beta)* section of :doc:`../administration/config-settings`.
4. Verify the configuration files are identical on both servers then restart each machine in the cluster.
5. Modify your NGINX setup  so that it proxies to both servers. For more information about this, see `Proxy Server Configuration`_
6. Open **System Console > Advanced > High Availability (Beta)** to verify all the machines in the cluster are communicating as expected with green status indicators. If not, investigate the log files for any extra information.

Adding a Server to the Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Backup your Mattermost database and the file storage location.
2. Setup a new Mattermost server. This server must use an identical copy of the configuration file, ``config.json``. Verify the server is functioning by hitting the private IP address.
3. Modify the ``config.json`` files on all servers with the ``ClusterSettings`` as described in the *High Availability (Beta)* section of :doc:`../administration/config-settings`. Be sure to add the new server URL to ``InterNodeUrls``. 
4. Verify that the configuration files are identical on all servers, then restart each machine in the cluster in sequence with 10 or more seconds between each restart.
5. Modify your NGINX setup to add the new server. For information about this, see `Proxy Server Configuration`_.
6. Open the **System Console > Advanced > High Availability (Beta)** to verify that all the machines in the cluster are communicating as expected with green status indicators. If not, investigate the log files for any extra information.

Removing a Server from the Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Backup your Mattermost database and the file storage location.
2. Modify your NGINX setup to remove the server. For information about this, see `Proxy Server Configuration`_.
3. On all servers staying active in the cluster, modify the ``ClusterSettings`` in ``config.json`` to remove the server from ``InterNodeUrls`` 
4. Verify that the configuration files are identical on all servers, then restart each machine in the cluster in sequence with 10 or more seconds between each restart.
5. Open the **System Console > Advanced > High Availability (Beta)** to verify that all the machines in the cluster are communicating as expected with green status indicators. If not, investigate the log files for any extra information.

Configuration and Compatibility
-------------------------------
Details on configuring your system for high availability.

Mattermost Server Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuration Settings
^^^^^^^^^^^^^^^^^^^^^^

High availability is configured in the ``ClusterSettings`` section of ``config.json`` and the settings are viewable in the System Console. When high availability is enabled, the System Console is set to read-only mode to ensure all the ``config.json`` files on the Mattermost servers are identical.
 
.. code-block:: none

  "ClusterSettings": {
        "Enable": false,
        "InterNodeListenAddress": ":8075",
        "InterNodeUrls": []
  }

For more details on these settings, see the **High Availability (Beta)** section of :doc:`../administration/config-settings`.

State
^^^^^

The Mattermost Server is designed to have very little state to allow for horizontal scaling. The items in state considered for scaling Mattermost are listed below:

- In memory session cache for quick validation and channel access,
- In memory online/offline cache for quick response,
- System configuration file that is loaded and stored in memory,
- WebSocket connections from clients used to send messages.

When the Mattermost Server is configured for high availability, the servers  use an inter-node communication protocol on a different listening address to keep the state in sync. When a state changes it is written back to the database and an inter-node message is sent to notify the other servers of the state change. The true state of the items can always be read from the database. Mattermost also uses inter-node communication to forward WebSocket messages to the other servers in the cluster for real-time messages such as  “[User X] is typing.”


Proxy Server Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

The proxy server exposes the cluster of Mattermost servers to the outside world. The Mattermost servers are designed for use with a proxy server such as NGINX, a hardware load balancer, or a cloud service like Amazon Elastic Load Balancer.

If you want to monitor the server with a health check you can use ``http://10.10.10.2/api/v3/general/ping`` and check the response for ``Status 200``, indicating success. Use this health check route to mark the server *in-service* or *out-of-service*.

A sample configuration for NGINX is provided below. It assumes that you have two Mattermost servers running on private IP addresses of ``10.10.10.2`` and ``10.10.10.4``.


.. code-block:: none

    upstream backend {
            server 10.10.10.2:8065;
            server 10.10.10.4:8065;
      }

      server {
          server_name mattermost.example.com;

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
  3. If you’re using Amazon S3 for file storage then no other configuration is required.

If you’re using the Compliance Reports feature in Enterprise Edition E20, you need to configure the  ``"ComplianceSettings":`` ``"Directory": "./data/",`` to share between all machines or the reports will only be available from the System Console on the local Mattermost server.

Migrating to NAS or S3 from local storage is beyond the scope of this document.

Database Configuration
^^^^^^^^^^^^^^^^^^^^^^

Use the read-replica feature to scale the database. The Mattermost server can be set up to use one "master" database and up to 8 read replica databases. Mattermost distributes read requests across all databases, and sends write requests to the master database, and those changes are then sent to update the read replicas. 

Sizing databases
````````````````

For information about sizing database servers, see the *Hardware Sizing for Enterprise Deployments (Multi-Server)* section of :doc:`../install/requirements`.

In a master/slave environment, make sure to size the slave machine to take 100% of the load in the event that the master machine goes down and you need to fail over.

Deploying a multi-database configuration
````````````````````````````````````````

To configure a multi-database Mattermost server: 

1. Update the ``DataSource`` setting in ``config.json`` with a connection string to your master database server. The connection string is based on the database type set in ``DriverName``, either ``postgres`` or ``mysql``.
2. Update the ``DataSourceReplicas`` setting in ``config.json`` with a series of connection strings to your database read replica servers in the format ``["readreplica1", "readreplica2"]``. Each connection should also be compatible with the ``DriverName`` setting.

The new settings can be applied by either stopping and starting the server, or by loading the configuration settings as described in the next section. 

Once loaded, database write requests are sent to the master database and read requests are distributed among the other databases in the list.

Loading a multi-database configuration onto an active server
````````````````````````````````````````````````````````````

After a multi-database configuration has been defined in ``config.json``, the following procedure can be used to apply the settings without shutting down the Mattermost server: 

1. Go to **System Console > Configuration** and click **Reload Configuration from Disk** to reload configuration settings for the Mattermost server from ``config.json``. 
2. Go to **System Console > Database** and click **Recycle Database Connections** to take down existing database connections and set up new connections in the multi-database configuration.

While the connection settings are changing, there might be a brief moment when writes to the master database are unsuccessful. The process waits for all existing connections to finish and starts serving new requests with the new connections. End users attempting to send messages while the switch is happening will have an experience similar to losing connection to the Mattermost server.

Manual failover for master database
```````````````````````````````````

If the need arises to switch from the current master database--for example, if it is running out of disk space, or requires maintenance updates, or for other reasons--you can switch Mattermost server to use one of its read replicas as a master database by updating ``DataSource`` in ``config.json``. 

To apply the settings without shutting down the Mattermost server: 

1. Go to **System Console > Configuration** and click **Reload Configuration from Disk** to reload configuration settings for the Mattermost server from ``config.json``. 
2. Go to **System Console > Database** and click **Recycle Database Connections** to take down existing database connections and set up new connections in the multi-database configuration. 

While the connection settings are changing, there might be a brief moment when writes to the master database are unsuccessful. The process waits for all existing connections to finish and starts serving new requests with the new connections. End users attempting to send messages while the switch is happening will have an experience similar to losing connection to the Mattermost server.

Transparent Failover
````````````````````

The database can be configured for high availability and transparent failover use the existing database technologies. We recommend MySQL Clustering, Postgres Clustering, or Amazon Aoura. Database transparent failover is beyond the scope of this documentation.

Update Guide
------------

Updating configuration without service interruption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A service interruption is not required for most configuration updates. See `Updating server with service interruption`_ for a list of configuration updates that require a service interruption.

You can apply updates during a period of low load, but if your HA cluster is sized correctly, you can do it at any time. The system downtime is brief, and depends on the number of Mattermost servers in your cluster. Note that you are not restarting the machines, only the Mattermost server applications. A Mattermost server restart generally takes about 5 seconds.

1. Make a backup of your existing ``config.json`` file.
2. For one of the Mattermost servers, make the configuration changes to ``config.json`` and save the file. Do not reload the file yet.
3. Copy the ``config.json`` file to the other servers.
4. Shut down Mattermost on all but one server.
5. Reload the configuration file on the server that is still running. Go to **System Console > Configuration** and click **Reload Configuration from Disk**
6. Start the other servers. 

Updating server without service interruption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A service interruption is not required for security patch dot releases of the Mattermost server.

You can apply updates during a period of low load, but if your HA cluster is sized correctly, you can do it at any time. The system downtime is brief, and depends on the number of Mattermost servers in your cluster. Note that you are not restarting the machines, only the Mattermost server applications. A Mattermost server restart generally takes about 5 seconds.

1. Review the upgrade procedure in the *Upgrade Enterprise Edition* section of :doc:`../administration/upgrade`.
2. Make a backup of your existing ``config.json`` file.
3. Set your proxy to move all new requests to a single server. If you are using NGINX and it's configured with an upstream backend section in ``/etc/nginx/sites-available/mattermost`` then comment out all but the one server that you intend to update first, and reload NGINX.
4. Shut down Mattermost on each server except the one that you are updating first.
5. Upgrade each Mattermost instance that is shut down.
6. On each server, replace the new ``config.json`` file with your backed-up copy.
7. Start the Mattermost servers.
8. Repeat the upgrade procedure for the server that was left running.

Updating server with service interruption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A service interruption is required when the update includes a change to the database schema or when a change to ``config.json`` requires a server restart, such as when making the following changes:

  * Default Server Language
  * Rate Limiting
  * Webserver Wode
  * Database
  * High Availability

If the update includes a change to the database schema, the database is upgraded by the first server that starts.

Apply updates during a period of low load. The system downtime is brief, and depends on the number of Mattermost servers in your cluster. Note that you are not restarting the machines, only the Mattermost server applications.

1. Review the upgrade procedure in the *Upgrade Enterprise Edition* section of :doc:`../administration/upgrade`.
2. Make a backup of your existing ``config.json`` file.
3. Stop NGINX.
4. Upgrade each Mattermost instance.
5. On each server, replace the new ``config.json`` file with your backed-up copy.
6. Start one of the Mattermost servers.
7. When the server is running, start the other servers.
8. Restart NGINX.

Troubleshooting
---------------

Red Server Status
~~~~~~~~~~~~~~~~~

When high availability is enabled, the System Console displays the server status as red or green, indicating if the servers are communicating correctly with the cluster. The servers use inter-node communication to ping the other machines in the cluster, and once a ping is established the servers exchange information, such as server version and configuration files.

A server status of red can occur for the following reasons:

- **Configuration file mismatch**: Mattermost will still attempt the inter-node communication, but the System Console will show a red status for the server since the high availability feature assumes the same configuration file to function properly.
- **Server version mismatch**: Mattermost will still attempt the inter-node communication, but the System Console will show a red status for the server since the high availability feature assumes the same version of Mattermost is installed on each server in the cluster. It is recommended to use the `latest version of Mattermost <https://www.mattermost.org/download/>`_ on all servers. Follow the upgrade procedure in :doc:`../administration/upgrade` for any server that needs to be upgraded.
- **Server is down**: If an inter-node communication fails to send a message it will attempt again in 15 seconds. If the second attempt fails, the server is assumed to be down. An error message is written to the logs and the System Console will show a status of red for that server.

WebSocket Disconnect
~~~~~~~~~~~~~~~~~~~~

When a client WebSocket receives a disconnect it will automatically attempt to re-establish a connection every three seconds with a backoff. After the connection is established, the client attempts to receive any messages that were sent while it was disconnected.
