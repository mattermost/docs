Mattermost administration
==========================

Getting started with Mattermost
-------------------------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

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

Configure your deployment
-------------------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. toctree::
    :maxdepth: 1
    :hidden:

    Optimize your workspace </configure/optimize-your-workspace>
    Mattermost configuration settings </configure/configuration-settings>
    Self-hosted edition and license </configure/self-hosted-account-settings>
    Reporting configuration settings </configure/reporting-configuration-settings>
    User management configuration settings </configure/user-management-configuration-settings>
    Environment configuration settings </configure/environment-configuration-settings>
    Site configuration settings </configure/site-configuration-settings>
    Authentication configuration settings </configure/authentication-configuration-settings>
    Plugins configuration settings </configure/plugins-configuration-settings>
    Integrations configuration settings </configure/integrations-configuration-settings>
    Compliance configuration settings </configure/compliance-configuration-settings>
    Experimental configuration settings </configure/experimental-configuration-settings>
    Deprecated configuration settings </configure/deprecated-configuration-settings>

The following documentation applies to both self-hosted and Cloud-based Mattermost deployments. 

* :doc:`Optimize your workspace </configure/optimize-your-workspace>` - Review health and growth scores for your workspace, and take necessary action.
* **Configure your workspace** - Mattermost offers extensive configuration options for both `self-hosted Mattermost servers and Mattermost Cloud workspaces </configure/configuration-settings.html>`__, and provides a list of :doc:`deprecated configuration settings </configure/deprecated-configuration-settings>` no longer supported.

User management
---------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. toctree::
    :maxdepth: 1
    :hidden:

    System admin roles </onboard/system-admin-roles>
    Manage team and channel members </manage/team-channel-members>
    Advanced permissions </onboard/advanced-permissions>
    Advanced permissions infrastructure </onboard/advanced-permissions-backend-infrastructure>
    Provisioning workflows </onboard/user-provisioning-workflows>
    Multi-factor authentication </onboard/multi-factor-authentication>
    Active Directory/LDAP </onboard/ad-ldap>
    AD/LDAP groups </onboard/ad-ldap-groups-synchronization>
    Use AD/LDAP synchronized groups to manage team or private channel membership </onboard/managing-team-channel-membership-using-ad-ldap-sync-groups>
    GitLab SSO </onboard/sso-gitlab>
    OpenID SSO </onboard/sso-openidconnect>
    Google SSO </onboard/sso-google>
    Office 365 SSO </onboard/sso-office>
    SAML SSO </onboard/sso-saml>
    SAML SSO: technical documentation </onboard/sso-saml-technical>
    Guest accounts </onboard/guest-accounts>

The following documentation applies to both self-hosted and Cloud-based Mattermost deployments. 

* :doc:`System Admin roles </onboard/system-admin-roles>` - Grant admins from your organization access to specific areas of the Mattermost System Console.
* :doc:`Manage team and channel members </manage/team-channel-members>` synchronization, moderation, and membership settings.
* **User permissions** - All versions of Mattermost offer standard user permissions control. Professional and Enterprise versions also include :doc:`advanced permissions control </onboard/advanced-permissions>` to customize which users can perform specific actions, 
* :doc:`Provisioning workflows </onboard/user-provisioning-workflows>` Learn how to provision and de-provision user accounts.
* **User authentication** - All versions of Mattermost provide basic authentication and offer :doc:`multi-factor authentication </onboard/multi-factor-authentication>` out of the box. Professional and Enterprise versions of Mattermost also include :doc:`Active Directory/LDAP </onboard/ad-ldap>` and SSO for :doc:`GitLab SSO </onboard/sso-gitlab>`, :doc:`OpenID </onboard/sso-openidconnect>`, :doc:`Google </onboard/sso-google>`, and :doc:`Office365 </onboard/sso-office>`.
* :doc:`AD/LDAP groups </onboard/ad-ldap-groups-synchronization>` - Sync AD/LDAP groups with Mattermost roles and teams.
* :doc:`Use AD/LDAP synchronized groups to manage team or private channel membership </onboard/managing-team-channel-membership-using-ad-ldap-sync-groups>` - Synchronize your AD/LDAP group with private Mattermost channels and teams.
* :doc:`SAML SSO </onboard/sso-saml>` - Configure Mattermost to be a SAML 2.0 service provider.
* :doc:`SAML SSO: technical documentation </onboard/sso-saml-technical>` - SAML 2.0 reference documentation for Mattermost.
* :doc:`Guest accounts </onboard/guest-accounts>` - Create guest accounts to collaborate with individuals outside your organization.