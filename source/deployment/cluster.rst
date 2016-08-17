High Availability (Beta)
===============================

*Available in Enterprise Edition E20.*

High Availability support enables a Mattermost server to scale and maintain service during outages and hardware failures through the use of redundant infrastructure. 

- Support for high availability database configurations is available in Mattermost Enterprise Edition E20 version 3.1 and higher. 
- Support for high availability configurations of the Mattermost application server is available in Mattermost Enterprise Edition E20 version 3.3 and higher. 

This documentation provides a deployment guide, configuration and compatibility details, as well as troubleshooting advice.


- `Deployment Guide <https://docs.mattermost.com/deployment/cluster.html#id1>`_ - **Instructions to set up and maintain high availability on your Mattermost servers.**
 - `Initial Setup Guide for High Availability <https://docs.mattermost.com/deployment/cluster.html#id2>`_
 - `Adding a Server to the Cluster <https://docs.mattermost.com/deployment/cluster.html#id4>`_
 - `Removing a Server from the Cluster <https://docs.mattermost.com/deployment/cluster.html#id9>`_

- `Configuration and Compatibility <https://docs.mattermost.com/deployment/cluster.html#id13>`_ - **Details on configuring your system for high availability.**
 - `Mattermost Server <https://docs.mattermost.com/deployment/cluster.html#mattermost-server-configuration>`_ - Configure the cluster settings for the Mattermost application server. 
 - `Proxy Server <https://docs.mattermost.com/deployment/cluster.html#proxy-server-configuration>`_ - Configure NGINX or another load balancer to proxy servers in the cluster.
 - `File Storage Location <https://docs.mattermost.com/deployment/cluster.html#file-storage-configuration>`_ - Configure the file storage location to be compatible with a high availability setup.
 - `Database <https://docs.mattermost.com/deployment/cluster.html#database-configuration>`_ - Size and deploy a multi-database configuration for high availability and scaling.

- `Troubleshooting <https://docs.mattermost.com/deployment/cluster.html#id14>`_ - **Advice on troubleshooting your high availability setup.**

-----


Deployment Guide
~~~~~~~~~~~~~~~~~
Deployment guide to setup and maintain high availability on your Mattermost servers.

Initial Setup Guide for High Availability
--------------------------------------------------------------
To ensure your instance and configuration are compatible with high availability, please review the `Configuration and Compatibility <https://docs.mattermost.com/deployment/cluster.html#id13>`_ section.

.. note:: Backup your `Mattermost database <https://docs.mattermost.com/deployment/cluster.html#database-configuration>`_ and `file storage locations <https://docs.mattermost.com/deployment/cluster.html#file-storage-configuration>`_ before configuring high availability.

1. Follow our `upgrade guide <https://docs.mattermost.com/administration/upgrade.html>`_ to upgrade your Mattermost server to v3.3 or later. 
2. Setup a new Mattermost server with v3.3 or later following one of our **Install Guides**. This server must use an identical copy of the configuration file, ``config.json``. Verify the servers are functioning by hitting each independent server through its private IP address.
3. Modify the ``config.json`` files on both servers to add the ``ClusterSettings`` as `described in this documentation <https://docs.mattermost.com/administration/config-settings.html#id57>`_. 
4. Verify the configuration files are identical on both servers then restart each machine in the cluster.
5. `Modify your NGINX setup <https://docs.mattermost.com/deployment/cluster.html#proxy-server-configuration>`_ so it proxies to both servers.
6. Open the **System Console** > **Advanced** > **High Availability (Beta)** to verify all the machines in the cluster are communicating as expected with green status indicators. If not, investigate the log files for any extra information.

Adding a Server to the Cluster
------------------------------------------------------------

1. Backup your `Mattermost database <https://docs.mattermost.com/deployment/cluster.html#database-configuration>`_ and `file storage location <https://docs.mattermost.com/deployment/cluster.html#file-storage-configuration>`_.
2. Setup a new Mattermost server following one of our **Install Guides**. This server must use an identical copy of the configuration file, ``config.json``. Verify the server is functioning by hitting the private IP address.
3. Modify the ``config.json`` files on all servers with the ``ClusterSettings`` as `described in this documentation <https://docs.mattermost.com/administration/config-settings.html#high-availability-beta>`_. Be sure to add the new server URL to ``InterNodeUrls``. 
4. Verify the configuration files are identical on all servers, then restart each machine in the cluster in sequence with 10 or more seconds between each restart.
5. `Modify your NGINX setup <https://docs.mattermost.com/deployment/cluster.html#proxy-server-configuration>`_ to add the new server.
6. Open the **System Console** > **Advanced** > **High Availability (Beta)** to verify all the machines in the cluster are communicating as expected with green status indicators. If not, investigate the log files for any extra information.

Removing a Server from the Cluster
-----------------------------------------------------------------

1. Backup your `Mattermost database <https://docs.mattermost.com/deployment/cluster.html#database-configuration>`_ and `file storage location <https://docs.mattermost.com/deployment/cluster.html#file-storage-configuration>`_.
2. `Modify your NGINX setup <https://docs.mattermost.com/deployment/cluster.html#proxy-server-configuration>`_ to remove the server.
3. On all servers staying active in the cluster, modify the ``ClusterSettings`` in ``config.json`` to remove the server from ``InterNodeUrls`` 
4. Verify the configuration files are identical on all servers, then restart each machine in the cluster in sequence with 10 or more seconds between each restart.
5. Open the **System Console** > **Advanced** > **High Availability (Beta)** to verify all the machines in the cluster are communicating as expected with green status indicators. If not, investigate the log files for any extra information.


-----

Configuration and Compatibility
~~~~~~~~~~~~~~~~~~~~~~~~
Details on configuring your system for high availability.    

Mattermost Server Configuration
------------------------------------------------

Configuration Settings
````````````````````````````````````
High availability is configured in the ``ClusterSettings`` section of ``config.json`` and the settings are viewable in the System Console. When high availability is enabled, the System Console is set to read-only mode to ensure all the ``config.json`` files on the Mattermost servers are identical.
 
.. code::

  "ClusterSettings": {
        "Enable": false,
        "InterNodeListenAddress": ":8075",
        "InterNodeUrls": []
  }


Please refer to our `Configuration Settings documentation <https://docs.mattermost.com/administration/config-settings.html#high-availability-beta>`_ for more details on these settings.

State
``````````````````
The Mattermost Server is designed to have very little state to allow for horizontal scaling.  The items in state considered for scaling Mattermost are listed below:

- In memory session cache for quick validation and channel access,
- In memory online/offline cache for quick response,
- System configuration file that is loaded and stored in memory,
- WebSocket connections from clients used to send messages.

When the Mattermost Server is configured for high availability, the servers will use an inter-node communication protocol on a different listening address to keep the state in sync.  When a state changes it is written back to the database and an inter-node message is sent to notify the other servers of the state change.  The true state of the items can always be read from the database.  Mattermost also uses inter-node communication to forward WebSocket messages to the other servers in the cluster for real-time messages like “[User X] is typing.”


Proxy Server Configuration
-----------------------------------------

The proxy server will expose the cluster of Mattermost servers to the outside world.  The Mattermost servers are designed for use with a proxy server like NGINX, hardware load balancer, or a cloud service like Amazon Elastic Load Balancer.

If you wish to monitor the server with a health check you can use ``http://10.10.10.2/api/v3/general/ping`` and check the response for ``Status 200``, indicating success.  Use this health check route to mark the server in-service or out-of-service.

A sample configuration for NGINX is provided below.  It assumes you have two Mattermost servers running on private IP addresses of ``10.10.10.2`` and ``10.10.10.4``.


.. code::

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


A setup with multiple proxy servers can be utilized to limit a single point of failure, but is beyond the scope of this documentation.


File Storage Configuration
----------------------------------------

.. note:: File storage is assumed to be shared between all the machines utilizing services such as NAS or Amazon S3. If ``"DriverName": "local"`` is used then the directory at ``"FileSettings":`` ``"Directory": "./data/"`` is expected to be a NAS location mapped as a local directory, otherwise high availability will not function correctly and may corrupt your file storage. If you’re using Amazon S3 for file storage then no other configuration is required.

If you’re using the Compliance Reports feature in Enterprise Edition E20, you will need to configure the  ``"ComplianceSettings":`` ``"Directory": "./data/",`` to share between all machines or the reports will only be available from the System Console on the local Mattermost server.

Migrating to NAS or S3 from local storage is beyond the scope of this document.

Database Configuration
------------------------------------
Scaling the database can be accomplished by utilizing the read-replica feature. The Mattermost server can be set up to use one "master" database and up to 8 read replica databases. Mattermost distributes read requests across all databases, and sends write requests to the master database, and those changes are then sent to update the read replicas. 

Sizing databases
```````````````````````````````````````
Please see `documentation on sizing database servers <http://docs.mattermost.com/install/requirements.html#hardware-requirements>`_ for guidance to determine appropriate hardware. 

In a master/slave environment, make sure to size the slave machine to take 100% of the load in the event that the master machine goes down and you need to fail over.


Deploying a multi-database configuration 
````````````````````````````````````````````````````````````````````````
To configure a multi-database Mattermost server: 

1. Update the ``DataSource`` setting in ``config.json`` with a connection string to your master database server. The connection string is based on the database type set in ``DriverName``, either ``postgres`` or ``mysql``. 
2. Update the ``DataSourceReplicas`` setting in ``config.json`` with a series of connection strings to your database read replica servers in the format ``["readreplica1", "readreplica2"]``. Each connection should also be compatible with the ``DriverName`` setting.

The new settings can be applied by either stopping and starting the server, or by loading the configuration settings as described in the next section. 

Once loaded, database write requests will be sent to the master database and read requests will be distributed among the other databases in the list.

Loading a multi-database configuration onto an active server
``````````````````````````````````````````````````````````````````````````````````````````````````
After a multi-database configuration has been defined in ``config.json`` the following procedure can be used to apply the settings without shutting down the Mattermost server: 

1. Go to **System Console** > **Configuration** and press **Reload Configuration from Disk** to reload configuration settings for the Mattermost server from ``config.json``. 
2. Go to **System Console** > **Database** and press **Recycle Database Connections** to takedown existing database connections and set up new connections in the multi-database configuration. 

While connection settings are changing there may be a brief moment when writes to the master database will be unsuccessful. The process waits for all existing connections to finish and starts serving new requests with the new connections. End users attempting to send messages while the switch is happening will have an experience similar to losing connection to the Mattermost server.

Manual failover for master database  
`````````````````````````````````````````````````````````````````
If the need arises to switch from the current master database--for example, if it is running out of disk space, or requires maintenance updates, or for other reasons--the Mattermost server can switch to using one of its read replicas as a master database by updating ``DataSource`` in ``config.json``. The following procedure can be used to apply the settings without shutting down the Mattermost server: 

1. Go to **System Console** > **Configuration** and press **Reload Configuration from Disk** to reload configuration settings for the Mattermost server from ``config.json``. 
2. Go to **System Console** > **Database** and press **Recycle Database Connections** to takedown existing database connections and set up new connections in the multi-database configuration. 

While connection settings are changing there may be a brief moment when writes to the master database will be unsuccessful. The process waits for all existing connections to finish and starts serving new requests with the new connections. End users attempting to send messages while the switch is happening will have an experience similar to losing connection to the Mattermost server.

Transparent Failover
````````````````````````````````````
The database can be configured for high availability and transparent failover utilizing the existing database technologies.  We recommend MySQL Clustering, Postgres Clustering, or Amazon Aoura.  Database transparent failover is beyond the scope of this documentation.

-----

Troubleshooting
~~~~~~~~~~~~~~~~~~~~~~~

Red Server Status
---------------------------
When high availability is enabled, the System Console displays the server status as red or green, indicating if the servers are communicating correctly with the cluster. The servers use inter-node communication to ping the other machines in the cluster, and once a ping is established the servers exchange information, such as server version and configuration files. Red server status may display for the following reasons:

- **Configuration file mismatch**: Mattermost will still attempt the inter-node communication, but the System Console will show a red status for the server since the high availability feature assumes the same configuration file to function properly.
- **Server version mismatch**: Mattermost will still attempt the inter-node communication, but the System Console will show a red status for the server since the high availability feature assumes the same version of Mattermost is installed on each server in the cluster. It is recommended to use the `latest version of Mattermost <https://www.mattermost.org/download/>`_ on all servers. Follow the `upgrade procedure <https://docs.mattermost.com/administration/upgrade.html>`_ for any server that needs to be upgraded.
- **Server is down**: If an inter-node communication fails to send a message it will attempt again in 15 seconds.  If the second attempt fails, the server is assumed to be down. An error message is written to the logs and the System Console will show a status of red for that server.

WebSocket Disconnect
----------------------------------------
When a client WebSocket receives a disconnect it will automatically attempt to re-establish a connection every three seconds with a backoff.  Once the connection is established the client will attempt to receive any missing messages since it was disconnected.
