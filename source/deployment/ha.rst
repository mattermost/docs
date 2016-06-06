High Availability 
----

*Available in Enterprise Edition E20 version 3.1 and higher.*

High Availability support enables a Mattermost server to maintain service during outages and hardware failures of underlying services and hardware through the use of redundant infrastructure. 

- Support for high availability database configurations is available in Mattermost Enterprise Edition E20 version 3.1 and higher. 
- Support for high availability configurations of the Mattermost application server is planned for release in Mattermost Enterprise Edition E20 during summer 2016. 

Setting up an active-passive redundant database configuration
====

The Mattermost server can set up to use one "master" database and up to 8 read replica databases. Mattermost distributes read requests across all databases, and sends write requests to the master database, and those changes are then sent to update the read replicas. 

Sizing databases
^^^^

Please see `documentation on sizing database servers <http://docs.mattermost.com/install/requirements.html#hardware-requirements>`_ for guidance to determine appropriate hardware. 

It's highly recommended that at least one read replica have a minimum of **three times the disk space** of the master database. This way, if the master database signals a "low disk space" warning the administrator can switch over to the read replica with a larger disk and continue operation, while also having room to locally duplicate and manipulate the production database. 


Deploying a multi-database configuration 
^^^^

To configure a multi-database Mattermost server edit the `DataSource` setting `config.json` with a list of comma-separated database connection strings, with the first entry being the connection to the master database.

All connection strings must be compatible with the database type set in `DriverName`, which would be either `postgres` or `mysql`. 

Database write requests will be sent to the master database and read requests will be distributed among the other databases in the list. 
Loading a multi-database configuration onto an active server
^^^^

After a multi-database configuration has been defined in `config.json` the following procedure can be used to apply the settings without shutting down the Mattermost server: 

1. Go to **System Console** > **Configuration** and press *Reload Configuration from Disk** to reload configuration settings for the Mattermost server from `config.json`. 
2. Go to **System Console** > **Database** and press **Recycle Database Connections** to takedown existing database connections and set up new connections in the multi-database configuration. 

While connection settings are changing there may be a brief moment when writes to the master database will be unsuccessful. The process waits for all existing connections to finish and starts serving new requests with the new connections. End users attempting to send messages while the switch is happening will have an experience similar to losing connection to the Mattermost server.

Automatic read replica failover 
^^^^

The Mattermost server can be connected to a database cluster to enable automatic failover from read replicas that are disabled from exceeding disk space, having a hardware failure, a network disconnection, or for other reasons. 

Manual failover for master database  
^^^^

If the need arises to switch from the current master database--for example, if it is running out of disk space, or requires maintenance updates, or for other reasons--the Mattermost server can switch to using one of its read replicas as a master database by updating `DataSource` in `config.json` the following procedure can be used to apply the settings without shutting down the Mattermost server: 

1. Go to **System Console** > **Configuration** and press *Reload Configuration from Disk** to reload configuration settings for the Mattermost server from `config.json`. 
2. Go to **System Console** > **Database** and press **Recycle Database Connections** to takedown existing database connections and set up new connections in the multi-database configuration. 

While connection settings are changing there may be a brief moment when writes to the master database will be unsuccessful. The process waits for all existing connections to finish and starts serving new requests with the new connections. End users attempting to send messages while the switch is happening will have an experience similar to losing connection to the Mattermost server.
