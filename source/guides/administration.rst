Mattermost administration guide
===============================

This guide is for people who administer an existing Mattermost server. It’s divided into three parts:

* `The basics <https://docs.mattermost.com/guides/administration.html#the-basics>`__ - An overview of standard configurations and features.
* `Cloud admin <https://docs.mattermost.com/guides/administration.html#cloud-admin>`__ - Detailed information about admin capabilities of Mattermost Cloud workspaces.
* `Self-Hosted admin <https://docs.mattermost.com/guides/administration.html#self-hosted-admin>`__ - Detailed information about admin capabilities of self-hosted Mattermost servers.

If you’re looking for resources to help you install, deploy, and scale your self-hosted Mattermost server, refer to the :doc:`Mattermost Deployment Guide </guides/deployment>`.

The basics
----------
.. toctree::
    :maxdepth: 1
    :hidden:

    Optimize your workspace </configure/optimize-your-workspace>
    Mattermost configuration settings </configure/configuration-settings>
    Mattermost deprecated configuration settings </configure/deprecated-configuration-settings>
    Workspace configuration for Cloud deployments </configure/cloud-site-configuration>
    Advanced permissions </onboard/advanced-permissions>
    Guest accounts </onboard/guest-accounts>
    System Admin roles </onboard/system-admin-roles>
    OpenID </onboard/sso-openidconnect>
    Google SSO </onboard/sso-google>
    Office 365 SSO </onboard/sso-office>
    GitLab SSO </onboard/sso-gitlab>
    Multi-factor authentication </onboard/multi-factor-authentication>
    Active Directory/LDAP </onboard/ad-ldap>

These resources will help you get started with your Mattermost workspace.

* Visit the :doc:`Workspace optimization </configure/optimize-your-workspace>` page in the System Console to review health and growth scores for your Mattermost workspace and take recommended actions.
* **Configuration overview** - Mattermost offers extensive configuration options for both :doc:`self-hosted Mattermost servers </configure/configuration-settings>` and :doc:`Mattermost cloud workspaces </configure/cloud-site-configuration>`.
* **Authentication** - All versions of Mattermost provide basic authentication, :doc:`multi-factor authentication </onboard/multi-factor-authentication>`, and :doc:`Gitlab SSO </onboard/sso-gitlab>` out of the box. Professional and Enterprise versions of Mattermost also include :doc:`Active Directory / LDAP </onboard/ad-ldap>` and SSO for :doc:`OpenID </onboard/sso-openidconnect>`, :doc:`Google </onboard/sso-google>`, and :doc:`Office365 </onboard/sso-office>`.
* **User permissions** - All versions of Mattermost offer standard user permissions control. Professional and Enterprise versions also include :doc:`advanced permissions control </onboard/advanced-permissions>` to customize which users can perform specific actions, and :doc:`system admin roles </onboard/system-admin-roles>` to grant admins from your organization access to specific areas of the Mattermost System Console.

Cloud admin
-----------

This section of the guide is for admins of Mattermost Cloud workspaces. If you're the admin for a self-hosted Mattermost server, please refer to the self-hosted section.

Workspace setup and configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. toctree::
    :maxdepth: 1
    :hidden:

    Site configuration </configure/cloud-site-configuration>
    SAML Single Sign-On </onboard/cloud-sso-saml>
    SAML SSO technical documentation </onboard/cloud-sso-saml-technical>
    AD/LDAP groups </onboard/cloud-groups>
    Shared channels </onboard/shared-channels>

* :doc:`Site configuration </configure/cloud-site-configuration>` - Set up and configure your Mattermost Cloud workspace.
* :doc:`SAML Single Sign-On </onboard/cloud-sso-saml>` - Configure Mattermost to be a SAML 2.0 service provider. Refer to the :doc:`SAML reference documentation </onboard/cloud-sso-saml-technical>` for technical implementation details.
* :doc:`AD/LDAP groups </onboard/cloud-groups>` - Sync AD/LDAP groups with Mattermost roles and teams.
* :doc:`Shared channels </onboard/shared-channels>` - Connect channels from multiple Mattermost servers in a federated architecture.

Workspace management
^^^^^^^^^^^^^^^^^^^^
.. toctree::
    :maxdepth: 1
    :hidden:

    Mattermost Cloud billing </manage/cloud-billing>
    Statistics </manage/cloud-reporting>
    User Satisfaction surveys </manage/cloud-user-satisfaction-surveys>
    Managing team and channel members </manage/cloud-team-and-channel>
    Workspace migration </manage/cloud-data-export>
    Cloud data residency </manage/cloud-data-residency>

* :doc:`Mattermost Cloud billing </manage/cloud-billing>` - Set up and manage billing for your Mattermost Cloud workspace.
* :doc:`Statistics </manage/cloud-reporting>` - Get statistics about Mattermost usage.
* :doc:`User Satisfaction surveys </manage/cloud-user-satisfaction-surveys>` - Learn about Mattermost user satisfaction surveys and how to configure their operation.
* :doc:`Managing team and channel members </manage/cloud-team-and-channel>` - Manage synchronization, moderation, and membership settings.
* :doc:`Workspace migration </manage/cloud-data-export>` - Migrate your workspace using the mmctl tool.
* :doc:`Cloud data residency </manage/cloud-data-residency>` - Find information about your data in the Cloud.

Workspace compliance
^^^^^^^^^^^^^^^^^^^^
.. toctree::
    :maxdepth: 1
    :hidden:

    Data retention policy </comply/cloud-data-retention-policy>

* :doc:`Data retention policy </comply/cloud-data-retention-policy>` - Set custom data retention policies to manage how long Mattermost retains messages and file uploads.

Self-hosted admin
-----------------

This section of the guide is for admins of self-hosted Mattermost servers. If you're the admin for a Mattermost Cloud workspace, please refer to the Cloud section of this page.

Self-hosted setup and configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Initial setup
"""""""""""""
.. toctree::
    :maxdepth: 1
    :hidden:

    Configuration overview </configure/configuration-settings>
    Custom branding tools </configure/custom-branding-tools>
    Customize Mattermost </configure/customizing-mattermost>
    SMTP email setup </configure/smtp-email>

* :doc:`Configuration overview </configure/configuration-settings>` - Set up and configure your Mattermost Cloud workspace.
* :doc:`Custom branding tools </configure/custom-branding-tools>` - Change Mattermost branding, site name, and description. 
* :doc:`Customize Mattermost </configure/customizing-mattermost>` - Whitelabel the Mattermost server and apps.
* :doc:`SMTP email setup </configure/smtp-email>` - Connect to an email server to send emails for password resets and system notifications.

Advanced configurations
"""""""""""""""""""""""
.. toctree::
    :maxdepth: 1
    :hidden:

    Shared channels </onboard/shared-channels>
    Store Mattermost configuration in the database </configure/configuation-in-mattermost-database>
    Email templates </configure/email-templates>
    Configuring CloudFront to host Mattermost static assets </configure/configuring-cloudfront-to-host-mattermost-static-assets>
    Use an outbound proxy </configure/using-outbound-proxy>
    Chinese, Japanese, and Korean search </configure/enabling-chinese-japanese-korean-search>

* :doc:`Shared channels </onboard/shared-channels>` - Connect channels from multiple Mattermost servers in a federated architecture.
* :doc:`Include configuration in the Mattermost database </configure/configuation-in-mattermost-database>` - Store Mattermost configuration information in your database rather than as a JSON file. We recommend this for High Availability environments.
* :doc:`Email templates </configure/email-templates>` - Alter the transactional emails Mattermost sends to your users.
* :doc:`Configuring CloudFront to host Mattermost static assets </configure/configuring-cloudfront-to-host-mattermost-static-assets>` - Improve caching performance to reduce content load times.
* :doc:`Using an outbound proxy </configure/using-outbound-proxy>` - Monitor outbound traffic and control the websites that can appear in embedded content.
* :doc:`Chinese, Japanese, and Korean search </configure/enabling-chinese-japanese-korean-search>` - Set up search capabilities for teams communicating via Chinese, Japanese, or Korean.

User onboarding
"""""""""""""""
.. toctree::
    :maxdepth: 1
    :hidden:

    Provisioning Workflows </onboard/user-provisioning-workflows>
    Bulk loading data </onboard/bulk-loading-data>
    Migration guide </onboard/migrating-to-mattermost>

* :doc:`Provisioning workflows </onboard/user-provisioning-workflows>` - Learn how to provision and de-provision user accounts.
* :doc:`Bulk loading data </onboard/bulk-loading-data>` - Import bulk data into Mattermost for teams, channels, users, post content, and more.
* :doc:`Migration guide </onboard/migrating-to-mattermost>` - Learn how to migrate from other chat services to Mattermost.

Advanced user management configurations
"""""""""""""""""""""""""""""""""""""""
.. toctree::
    :maxdepth: 1
    :hidden:

    AD/LDAP Groups </onboard/ad-ldap-groups-synchronization>
    Guest Accounts </onboard/guest-accounts>
    Using AD/LDAP Synchronized Groups to manage team or private channel membership </onboard/managing-team-channel-membership-using-ad-ldap-sync-groups>
    SAML Single Sign-On </onboard/sso-saml>
    SAML Single-Sign-On: technical documentation </onboard/sso-saml-technical>
    SSL client certificate setup </onboard/ssl-client-certificate>
    Certificate-based authentication </onboard/certificate-based-authentication>

* :doc:`AD/LDAP Groups </onboard/ad-ldap-groups-synchronization>` - Sync AD/LDAP groups with Mattermost roles and teams.
* :doc:`Guest Accounts </onboard/guest-accounts>` - Create guest accounts to collaborate with individuals outside your organization.
* :doc:`Using AD/LDAP Synchronized Groups to manage team or private channel membership </onboard/managing-team-channel-membership-using-ad-ldap-sync-groups>` - Synchronize your AD/LDAP group with private Mattermost channels and teams.
* :doc:`SAML Single Sign-On </onboard/sso-saml>` - Configure Mattermost to be a SAML 2.0 service provider.
* :doc:`SAML Single-Sign-On: technical documentation </onboard/sso-saml-technical>` - SAML 2.0 reference documentation for Mattermost.
* :doc:`SSL client certificate setup </onboard/ssl-client-certificate>` - Configure SSL client certificates for Mattermost Desktop and Web Apps.
* :doc:`Certificate-Based Authentication </onboard/certificate-based-authentication>` - Set up certificate-based authentication for Mattermost.

Self-hosted server management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. toctree::
    :maxdepth: 1
    :hidden:

    Managing team and channel members </manage/team-channel-members>
    Statistics </manage/statistics>
    In-product notices </manage/in-product-notices>
    User Satisfaction surveys </manage/user-satisfaction-surveys>
    Health check </manage/health-checks>
    Announcement banner </manage/announcement-banner>
    Bulk export tool </manage/bulk-export-tool>

* :doc:`Managing team and channel members </manage/team-channel-members>` - Manage synchronization, moderation, and membership settings.
* :doc:`Statistics </manage/statistics>` - Get statistics about your Mattermost server usage.
* :doc:`In-product notices </manage/in-product-notices>` - Get notified about Mattermost updates via in-app notices.
* :doc:`User Satisfaction surveys </manage/user-satisfaction-surveys>` - Learn about Mattermost user satisfaction surveys and how to configure their operation.
* :doc:`Health check </manage/health-checks>` - Configure health probes for your Mattermost server.
* :doc:`Announcement banner </manage/announcement-banner>` - Display notices to your users via an announcement banner.
* :doc:`Bulk export tool </manage/bulk-export-tool>` - Export user, team, channel, and post data from Mattermost.

Self-hosted compliance
^^^^^^^^^^^^^^^^^^^^^^
.. toctree::
    :maxdepth: 1
    :hidden:

    Electronic discovery </comply/electronic-discovery>
    Compliance export </comply/compliance-export>
    Audit log v2 (experimental) </comply/audit-log>
    Data retention policy </comply/data-retention-policy>
    Custom terms of service </comply/custom-terms-of-service>

* :doc:`Electronic discovery </comply/electronic-discovery>` - Extract data from Mattermost for eDiscovery use in legal cases.
* :doc:`Compliance export </comply/compliance-export>` - Create compliance reports from the Mattermost System Console. 
* :doc:`Audit log v2 (experimental) </comply/audit-log>` - Review a comprehensive list of events that occur on your Mattermost server.
* :doc:`Data retention policy </comply/data-retention-policy>` - Set custom data retention policies to manage how long Mattermost retains messages and file uploads.

Other resources
---------------
.. toctree::
    :maxdepth: 1
    :hidden:

    Converting OAuth 2.0 service providers to OpenID Connect </onboard/convert-oauth20-service-providers-to-openidconnect>
    Generate a support packet </manage/generating-support-packet>
    mmctl command line tool </manage/mmctl-command-line-tool>
    Migration announcement email template </onboard/migration-announcement-email>
    Advanced permissions: Backend infrastructure </onboard/advanced-permissions-backend-infrastructure>
    Command line tools </manage/command-line-tools>
    Scripts </manage/scripts>

If the information above doesn’t solve your problem, look at these other resources to find something that meets your needs. Alternatively, you can also :doc:`get help </guides/get-help>` from our community or via premium support services.

* :doc:`Converting OAuth 2.0 service providers to OpenID Connect </onboard/convert-oauth20-service-providers-to-openidconnect>` - Migrate from OAuth 2.0 to OpenID Connect.
* :doc:`Generate a support packet </manage/generating-support-packet>` - Generate configuration information, logs, plugin details, and data dependencies to provide when contacting Mattermost support.
* :doc:`mmctl command line tool </manage/mmctl-command-line-tool>` - Use mmctl to manage self-hosted Mattermost servers from the command line.
* :doc:`Migration announcement email template </onboard/migration-announcement-email>` - Use this email template to notify your users about migrating to Mattermost.
* :doc:`Advanced permissions: Backend infrastructure </onboard/advanced-permissions-backend-infrastructure>` - Read our technical guide on modifying self-hosted Mattermost installations to create custom permissions schemes.
* :doc:`Command line tools </manage/command-line-tools>` - Learn how to use the command line to manage self-hosted Mattermost servers.
* :doc:`Scripts </manage/scripts>` - Explore a selection of example scripts you can use to manage self-hosted Mattermost servers.
