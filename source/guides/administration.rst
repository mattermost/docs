Mattermost administration guide
===============================

Getting started with Mattermost
-------------------------------

.. toctree::
    :maxdepth: 1
    :hidden:

    Deployment overview </deploy/deployment-overview>
    Architecture </getting-started/architecture-overview>
    Mattermost self-hosted billing </manage/self-hosted-billing>
    Administrator tasks </getting-started/admin-onboarding-tasks>
    Technical requirements  </getting-started/implementation-plan>
    Welcome email template </getting-started/welcome-email-to-end-users>
    Enterprise roll out checklist </getting-started/enterprise-roll-out-checklist>

* :doc:`Deployment overview </deploy/deployment-overview>` - Learn about the Mattermost user experience, communication protocols, network access, data storage, and deployment options.
* :doc:`Architecture </getting-started/architecture-overview>` - Learn about user authentication, notifications, data management services, network connectivity, and high availability.
* :doc:`Mattermost self-hosted billing </manage/self-hosted-billing>` - Manage your Mattermost subscription.
* :doc:`Administrator tasks </getting-started/admin-onboarding-tasks>` - Learn about the standard configurations and settings you’ll encounter.
* :doc:`Technical requirements </getting-started/implementation-plan>` - Get a detailed breakdown of the technical requirements to deploy Mattermost for your team or organization.
* :doc:`Welcome email template </getting-started/welcome-email-to-end-users>` - Use our sample email template when you’re ready to invite users to your server.
* :doc:`Enterprise roll out checklist </getting-started/enterprise-roll-out-checklist>` - Learn how to roll Mattermost out to thousands of users.


Self-hosted server administration
----------------------------------

.. toctree::
    :maxdepth: 1
    :hidden:

    Install a database </install/install-database>
    Set up a socket-based Mattermost database </install/setting-up-socket-based-mattermost-database>
    Include configuration in the Mattermost database </configure/configuation-in-a-database>
    Configure TLS on Mattermost Server </install/configure-tls>
    Install NGINX proxy server </install/install-nginx-proxy-server>
    SMTP email setup </configure/smtp-email>
    SSL client certificate setup </onboard/ssl-client-certificate>
    Set up an image proxy </deploy/image-proxy>
    Encryption options </deploy/encryption-options>
    Configure transport encryption </install/transport-encryption>
    Set up full-text Bleve search </deploy/bleve-search>
    Backup and disaster recovery </deploy/backup-disaster-recovery>


* :doc:`Install a database </install/install-database>` - Mattermost requires either a MySQL or PostgreSQL database.
* :doc:`Set up a socket-based Mattermost database </install/setting-up-socket-based-mattermost-database>` - Connect your Mattermost server to your database service.
* :doc:`Include configuration in the Mattermost database </configure/configuation-in-a-database>` - Store Mattermost configuration information in your database rather than as a JSON file. Recommended for High Availability environments.
* :doc:`Configure TLS on Mattermost Server </install/configure-tls>`
* :doc:`Install NGINX proxy server </install/install-nginx-proxy-server>`
* :doc:`SMTP email setup </configure/smtp-email>` - Connect to an email server to send emails for password resets and system notifications.
* :doc:`SSL client certificate setup </onboard/ssl-client-certificate>` - Configure SSL client certificates for Mattermost Desktop and Web Apps.
* :doc:`Set up an image proxy </deploy/image-proxy>` - Set up and configure an image proxy to make loading images faster and more reliable and prevent pixel tracking.
* :doc:`Encryption options </deploy/encryption-options>` - Set up encryption for data in transit and at rest.
* :doc:`Configure transport encryption </install/transport-encryption>` - Use transport encryption between Mattermost clusters and your proxy and database.
* :doc:`Set up full-text Bleve search </deploy/bleve-search>` - Use the Bleve search engine to provide Lucene-style full-text search.
* :doc:`Backup and disaster recovery </deploy/backup-disaster-recovery>` - Implement data backups, disaster recovery, and high availability deployment.































