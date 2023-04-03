Mattermost administration
==========================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

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
    SSO </onboard/sso>

* :doc:`Optimize your workspace </configure/optimize-your-workspace>` - Review health and growth scores for your workspace, and take necessary action.
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
* :doc:`SSO </onboard/sso>` - text here

other stuff
-----------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. toctree::
    :maxdepth: 1
    :hidden:

    Optimize your workspace </configure/optimize-your-workspace>
    System admin roles </onboard/system-admin-roles>
    Manage team and channel members </manage/team-channel-members>
    Advanced permissions </onboard/advanced-permissions>
    Provisioning workflows </onboard/user-provisioning-workflows>
    Multi-factor authentication </onboard/multi-factor-authentication>
    Active Directory/LDAP </onboard/ad-ldap>
    AD/LDAP groups </onboard/ad-ldap-groups-synchronization>
    Guest accounts </onboard/guest-accounts>
    Welcome email template </getting-started/welcome-email-to-end-users>
    Enterprise roll out checklist </getting-started/enterprise-roll-out-checklist>

The following documentation applies to both self-hosted and Cloud-based Mattermost deployments. 

* :doc:`System Admin roles </onboard/system-admin-roles>` - Grant admins from your organization access to specific areas of the Mattermost System Console.
* :doc:`Manage team and channel members </manage/team-channel-members>` synchronization, moderation, and membership settings.
* **User permissions** - All versions of Mattermost offer standard user permissions control. 
* :doc:`Provisioning workflows </onboard/user-provisioning-workflows>` Learn how to provision and de-provision user accounts.
* **User authentication** - All versions of Mattermost provide basic authentication and offer :doc:`multi-factor authentication </onboard/multi-factor-authentication>` out of the box. Professional and Enterprise versions of Mattermost also include :doc:`Active Directory/LDAP </onboard/ad-ldap>` and SSO for :doc:`GitLab SSO </onboard/sso-gitlab>`, :doc:`OpenID </onboard/sso-openidconnect>`, :doc:`Google </onboard/sso-google>`, and :doc:`Office365 </onboard/sso-office>`.
* :doc:`AD/LDAP groups </onboard/ad-ldap-groups-synchronization>` - Sync AD/LDAP groups with Mattermost roles and teams.
* :doc:`SAML SSO </onboard/sso-saml>` - Configure Mattermost to be a SAML 2.0 service provider.
* :doc:`Guest accounts </onboard/guest-accounts>` - Create guest accounts to collaborate with individuals outside your organization.
* :doc:`Welcome email template </getting-started/welcome-email-to-end-users>` - Use our sample email template when you’re ready to invite users to your server.
* :doc:`Enterprise roll out checklist </getting-started/enterprise-roll-out-checklist>` - Learn how to roll Mattermost out to thousands of users.