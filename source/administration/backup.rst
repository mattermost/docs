Backup and Disaster Recovery 
=============================

Options to protect your Mattermost server from different types of failures range from simple backup to sophisticated disaster recovery deployments and automation.

Backup
------

The state of your Mattermost server is contained in multiple data stores that need to be separately backed up and restored to fully recover your system from failure. 

To back up your Mattermost server:

1. Back up your Mattermost database using standard MySQL or PostgreSQL procedures depending on your database version.

      - `MySQL backup documentation <https://dev.mysql.com/doc/refman/5.6/en/backup-types.html>`__ is available online. Use the selector on the page to choose your MySQL version.
      - `PostgreSQL SQL Dump backup documentation <https://www.postgresql.org/docs/10/backup-dump.html>`__ is available online. Use the navigation at the top of the page to select your PostgreSQL version.
     
2. Back up your server settings stored in ``config/config.json``.

      - If you are using SAML configuration for Mattermost, your SAML certificate files will be saved in the ``config`` directory. Therefore, it is recommended to back up the entire directory.
   
3. Back up files stored by your users with one of the following options: 

     - If you use local storage using the default ``./data`` directory back up this directory.
     - If you use local storage using a non-default directory specified in the ``Directory`` setting in ``config.json``, back up files in that location.
     - If you store your files in S3, you can typically keep the files where they are located without backup.
     
Please note that to make a 'clean' backup you need to stop Mattermost during the duration of the backup otherwise the database and files may become out of sync.

To restore a Mattermost instance from backup, restore your database, ``config.json`` file, and optionally locally stored user files into the locations from which they were backed up.

Disaster Recovery 
-----------------

An appropriate disaster recovery plan weighs the benefits of mitigating specific risks against the cost and complexity of setting up disaster recovery infrastructure and automation.

There are two common approaches: 

Automated backup
~~~~~~~~~~~~~~~~

Automating backups for a Mattermost server provides a copy of the server's state at a particular point in time, which can be restored if a failure in the future leads to loss of data. Options include:

- Automation to periodically back up the Mattermost server, which may include all the components listed above or a subset depending on what you choose to protect.
- Automation to restore a server from backup, or deploy a new server, to reduce recovery time.
- Automation to verify a backup has been successfully produced to protect against backup automation failures.
- Storing backups off-site, to protect against physical loss of onsite systems.

Recovering from a failure using a backup is typically a manual process and will incur downtime. The alternative is to automate recovery using a high availability deployment.

High Availability deployment 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deploying Mattermost in `High Availability mode <https://docs.mattermost.com/deployment/cluster.html>`__ allows for fast, automated recovery from component failure, such as a specific server running out of disk space or having a hardware issue, by running on redundant servers. Options include:

- Deploying redundant Mattermost servers, to protect against failures in the Mattermost server.
- Deploying redundant databases, to protect against failures in the database.
- Deploying redundant web proxies, to protect against failures in the web proxies.
- Deploying redundant infrastructure in a separate physical data center, to protect against failures in the primary data center.

A properly deployed High Availability deployment automatically switches over to a redundant system should a single server fail. High Availability does not protect against failures such as data corruption, since errors would propagate to redundant systems.

A "complete" disaster recovery solution would protect against both real-time hardware failures using High Availability, data corruption failures using automation, and failures of the primary data center by offering both offsite backup and offsite redundant infrastructure. Because the complexity of a full disaster recovery solution is high, it is common for customers to consider trade-offs in cost and complexity relative to the anticipated risks and target recovery times.

Failover from Single Sign-On outage 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When using Single Sign-on with Mattermost Enterprise Edition an outage to your SSO provider can cause a partial outage on your Mattermost instance.

**What happens during an SSO outage?**

- **Most people can still log in.** By default, when a user logs in to Mattermost they receive a session token lasting 30 days (the duration can be configured in the System Console). During an SSO outage, users with valid session tokens can continue to using Mattermost uninterrupted.
- **Some people can't log in.** During an SSO outage, there are two situations under which a user cannot log in:
  
  * Users whose session token expires during the outage.
  * Users trying to log in to new devices.

In each case, the user cannot reach the SSO provider, and cannot log in. In this case, there are several potential mitigations:

Configure your SSO provider for High Availability 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you're using a self-hosted Single Sign-on provider, several options are available for `High Availability configurations that protect your system from unplanned outages <https://docs.microsoft.com/en-us/microsoft-identity-manager/pam/high-availability-disaster-recovery-considerations-bastion-environment>`__.

For SaaS-based authentication providers, while you still have a dependency on service uptime, you can set up redundancy in source systems from which data is being pulled. For example, with the OneLogin SaaS-based authentication service, you can set up `High Availability LDAP connectivity <https://support.onelogin.com/hc/en-us/articles/204262680-High-Availability-for-LDAP>`__ to further reduce the chances of an outage.

Set up your own IDP to provide an automated or manual SSO failover option 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a custom Identity Provider for SAML authentication that connects to both an active and a standby authentication option, that can be manually or automatically switched in case of an outage.

In this configuration, security should be carefully reviewed to prevent the standby SSO option from weakening your authentication protocols.

Set up a manual failover plan for SSO outages 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When users are unable to reach your organization's SSO provider during an outage, an error message directing them to contact your support link (defined in your System Console settings) is displayed.

Once IT is contacted about an SSO outage issue, they can temporarily change a user's account from SSO to email-password using the System Console, and the end user can use password to claim the account, until the SSO outage is over and the account can be converted back to SSO.

If the System Admin is unable to log into the System Console because of the SSO outage, they can switch their authentication method to email-password to gain access using the `command line tool <https://docs.mattermost.com/administration/command-line-tools.html>`__.

When the outage is over, it's critical to switch everyone back to SSO from email-password to maintain consistency and security.
