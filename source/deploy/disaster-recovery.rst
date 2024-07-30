Disaster recovery 
==================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

We strongly recommend having both a :doc:`back up </deploy/back-up-mattermost-server>` and a disaster recovery plan in place for your Mattermost deployment. An appropriate disaster recovery plan weighs the benefits of mitigating specific risks against the cost and complexity of setting up disaster recovery infrastructure and automation.

Options to protect your Mattermost server from different types of failures range from :doc:`simple server backup operations </deploy/back-up-mattermost-server>` to :ref:`automated backups <deploy/back-up-mattermost-server:automated backups>`, to more sophisticated disaster recovery plans through `automated recovery <#automate-recovery-with-a-high-availability-deployment>`__.

Recovering from a failure using a backup is typically a manual process and will incur downtime. The alternative is to automate recovery using a high availability deployment.

Automate recovery with a High Availability deployment 
-------------------------------------------------------

Deploying Mattermost in :doc:`High Availability mode </scale/high-availability-cluster>` allows for fast, automated recovery from component failure, such as a specific server running out of disk space or having a hardware issue, by running on redundant servers. 

A "complete" disaster recovery solution protects against both real-time hardware failures using High Availability, data corruption failures using automation, and failures of the primary data center by offering both offsite backup and offsite redundant infrastructure. 

Options include:

- Deploying redundant Mattermost servers, to protect against failures in the Mattermost server.
- Deploying redundant databases, to protect against failures in the database.
- Deploying redundant web proxies, to protect against failures in the web proxies.
- Deploying redundant infrastructure in a separate physical data center, to protect against failures in the primary data center.

A properly deployed High Availability deployment automatically switches over to a redundant system should a single server fail. High Availability does not protect against failures such as data corruption, since errors would propagate to redundant systems.

Because the complexity of a full disaster recovery solution is high, it is common to consider trade-offs in cost and complexity relative to the anticipated risks and target recovery times.

Failover from Single Sign-On outage 
------------------------------------

When using Single Sign-on (SSO) with Mattermost Enterprise Edition, an outage to your SSO provider can cause a partial outage on your Mattermost instance.

What happens during an SSO outage?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Most people can still log in.** By default, when a user logs in to Mattermost they receive a session token lasting 30 days (the duration can be configured in the System Console). During an SSO outage, users with valid session tokens can continue to using Mattermost uninterrupted.
- **Some people can't log in.** During an SSO outage, there are two situations under which a user cannot log in:
  
  * Users whose session token expires during the outage.
  * Users trying to log in to new devices.

In each case, the user cannot reach the SSO provider, and cannot log in. In this case, there are several potential mitigations:

Configure your SSO provider for High Availability 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're using a self-hosted Single Sign-on provider, several options are available for `High Availability configurations that protect your system from unplanned outages <https://docs.microsoft.com/en-us/microsoft-identity-manager/pam/high-availability-disaster-recovery-considerations-bastion-environment>`__.

For SaaS-based authentication providers, while you still have a dependency on service uptime, you can set up redundancy in source systems from which data is being pulled. For example, with the OneLogin SaaS-based authentication service, you can set up High Availability LDAP connectivity to further reduce the chances of an outage.

Set up your own IDP to provide an automated or manual SSO failover option 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a custom Identity Provider for SAML authentication that connects to both an active and a standby authentication option, that can be manually or automatically switched in case of an outage.

In this configuration, security should be carefully reviewed to prevent the standby SSO option from weakening your authentication protocols.

Set up a manual failover plan for SSO outages 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When users are unable to reach your organization's SSO provider during an outage, an error message directing them to contact your support link (defined in your System Console settings) is displayed.

Once IT is contacted about an SSO outage issue, they can temporarily change a user's account from SSO to email-password using the System Console, and the end user can use password to claim the account, until the SSO outage is over and the account can be converted back to SSO.

When the outage is over, it's critical to switch everyone back to SSO from email-password to maintain consistency and security.