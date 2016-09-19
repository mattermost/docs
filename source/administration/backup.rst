Backup & Disaster Recovery 
==========================

Options to protect your Mattermost server from different types of failures range from simple backup to sophisticated disaster recovery deployments and automation. 

Backup
------

The state of your Mattermost server is contained in multiple data stores that need to be separately backed-up and restored to fully recover your system from a failure. 

To backup your Mattermost server: 

1. Backup your Mattermost database using standard MySQL or PostgreSQL procedures depending on your database version.

      - `MySQL backup documentation <https://dev.mysql.com/doc/refman/5.6/en/backup-types.html>`_ is available online. Use the selector on the page to choose your MySQL version. 
      - `PostgreSQL backup documentation <https://www.postgresql.org/docs/9.5/static/backup-dump.html>`_ is available online. Use the navigation at the top of the page to select your PostgreSQL version. 
     
2. Backup your server settings stored in ``config/config.json``.

      - If you are using SAML configuration for Mattermost, your SAML certificate files will be saved in the ``config`` directory. Therefore, it is recommended to backup the entire directory.
   
3. Backup files stored by your users with one of the following options: 

     - If you use local storage using the default ``./data`` directory back up this directory.
     - If you use local storage using a non-default directory specified in the ``Directory`` setting in ``config.json``, back up files in that location.
     - If you store your files in S3, you can typically keep the files where they are located without backup.
     
To restore a Mattermost instance from backup, restore your database, ``config.json`` file and optionally locally stored user files into the locations from which they were backed up. 

Disaster Recovery 
-----------------

An appropriate disaster recovery plan weighs the benefits of mitigating specific risks against the cost and complexity of setting up disaster recovery infrastructure and automation. 

There are two common approaches: 

Automated backup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Automating backup up a Mattermost server provides a copy of the server's state at a particular point in time, which can be restored if a failure in future leads to loss of data. Options include: 

- Automation to periodically backup the Mattermost server, which may include all the components listed above or a subset depending on what you choose to protect.
- Automation to restore a server from backup, or deploy a new server, to reduce recovery time.
- Automation to verify a backup has been successfully produced to protect against backup automation failures.
- Storing backups off-site, to protect against physical loss of onsite systems.

Recoverying from a failure using a backup is typically a manual process and will incur downtime. The alternative is to automate recovery using a high availability deployment. 

High availability deployment 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Deploying Mattermost in `high availability mode <https://docs.mattermost.com/deployment/cluster.html>`_ allows for fast, automated recovery from a component failure, such as a specific server running out of disk space or having a hardware issue, by running on redundant servers. Options include: 

- Deploying redundant Mattermost servers, to protect against failures in the Mattermost server.
- Deploying redundant databases, to protect against failures in the database.
- Deploying redundant web proxies, to protect against failures in the web proxies.
- Deploying redundant infrastructure in a separate physical data center, to protect against failures in the primary data center.

A properly deployed high availability setup automatically switches over to a redundant system should a single server fail. High availability does not protect against failures such as data corruption, since errors would propagate to redundant systems.

A "complete" disaster recovery solution would protect against both real-time hardware failures using high availability, data corruption failures using automated, and failures of the primary data center by offering both offsite backup and offsite redundant infrastructure. Because the complexity of a full disaster recovery solution is high, it is common for customers to consider trade-offs in cost and complexity relative to the anticipated risks and target recovery times.

