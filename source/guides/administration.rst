Mattermost Administration Guide
===============================

This guide is for people who administer an existing Mattermost server. It’s divided into three parts:


* `The Basics <https://docs.mattermost.com/guides/administration.html#the-basics>`__ - An overview of standard configurations and features.
* `Cloud Admin <https://docs.mattermost.com/guides/administration.html#cloud-admin>`__ - Detailed information about admin capabilities of Mattermost cloud workspaces.
* `Self-Hosted Admin <https://docs.mattermost.com/guides/administration.html#self-hosted-admin>`__ - Detailed information about admin capabilities of self-hosted Mattermost servers.

If you’re looking for resources to help you install, deploy, and scale your self-hosted Mattermost server, refer to the :doc:`Mattermost Deployment Guide </guides/deployment>`.


The Basics
----------
.. toctree::
    :maxdepth: 1
    :hidden:

    Self-Hosted Configuration </configure/configuration-settings>
    Cloud Workspace Configuration </configure/cloud-site-configuration>
    Advanced Permissions </onboard/advanced-permissions>
    System Admin Roles </onboard/system-admin-roles>
    OpenID </onboard/sso-openidconnect>
    Google SSO </onboard/sso-google>
    Office 365 SSO </onboard/sso-office>
    Gitlab SSO </onboard/sso-gitlab>
    Multi-factor Authentication </onboard/multi-factor-authentication>
    Active Directory / LDAP </onboard/ad-ldap.md>


These resources will help you get started with your Mattermost server.



* **Configuration Overview** - Mattermost offers extensive configuration options for both :doc:`self-hosted Mattermost servers </configure/configuration-settings>` and :doc:`Mattermost cloud workspaces </configure/cloud-site-configuration>`.
* **Authentication** - All versions of Mattermost provide basic authentication, :doc:`multi-factor authentication </onboard/multi-factor-authentication>`, and :doc:`Gitlab SSO </onboard/sso-gitlab>` out of the box. Professional and Enterprise versions of Mattermost also include :doc:`Active Directory / LDAP </onboard/ad-ldap.md>` and SSO for :doc:`OpenID </onboard/sso-openidconnect>`, :doc:`Google </onboard/sso-google>`, and :doc:`Office365 </onboard/sso-office>`.
* **User Permissions** - All versions of Mattermost offer standard user permissions control. Professional and Enterprise versions also include :doc:`advanced permissions control </onboard/advanced-permissions>` to customize which users can perform specific actions, and :doc:`system admin roles </onboard/system-admin-roles>` to grant admins from your organization access to specific areas of the Mattermost System Console.


Cloud Admin
-----------


This section of the guide is for administrators of Mattermost cloud workspaces. If you are the administrator for a self-hosted Mattermost server, please refer to the self-hosted section.


Workspace Setup and Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. toctree::
    :maxdepth: 1
    :hidden:

    Site Configuration </configure/cloud-site-configuration>
    SAML Single Sign-On </onboard/cloud-sso-saml>
    AD/LDAP Groups </onboard/cloud-groups>
    Guest Accounts </onboard/cloud-guest-accounts>
    Shared Channels </onboard/shared-channels>

* :doc:`Site Configuration </configure/cloud-site-configuration>` - Setup and configure your Mattermost cloud workspace.
* :doc:`SAML Single Sign-On </onboard/cloud-sso-saml>` - Configure Mattermost to be a SAML 2.0 service provider. Refer to the :doc:`SAML reference documentation </onboard/cloud-sso-saml-technical>` for technical implementation details.
* :doc:`AD/LDAP Groups </onboard/cloud-groups>` - Sync AD/LDAP groups with Mattermost roles and teams.
* :doc:`Guest Accounts </onboard/cloud-guest-accounts>` - Create guest accounts to collaborate with individuals outside your organization.
* :doc:`Shared Channels </onboard/shared-channels>` - Connect channels from multiple Mattermost servers in a federated architecture.


Workspace Management
^^^^^^^^^^^^^^^^^^^^
.. toctree::
    :maxdepth: 1
    :hidden:

    Mattermost Cloud Billing </manage/cloud-billing>
    Statistics </manage/cloud-reporting>
    User Satisfaction Surveys </manage/cloud-user-satisfaction-surveys>
    Managing Team and Channel Members </manage/cloud-team-and-channel>


* :doc:`Mattermost Cloud Billing </manage/cloud-billing>` - Set up and manage billing for your Mattermost cloud workspace.
* :doc:`Statistics </manage/cloud-reporting>` - Get statistics about Mattermost usage.
* :doc:`User Satisfaction Surveys </manage/cloud-user-satisfaction-surveys>` - Learn about Mattermost user satisfaction surveys and how to configure their operation.
* :doc:`Managing Team and Channel Members </manage/cloud-team-and-channel>` - Manage synchronization, moderation, and membership settings.


Workspace Compliance
^^^^^^^^^^^^^^^^^^^^
.. toctree::
    :maxdepth: 1
    :hidden:

    Compliance Export </comply/cloud-compliance-export>
    Data Retention Policy </comply/cloud-data-retention-policy>
    Custom Terms of Service </comply/cloud-custom-terms-of-service>


* :doc:`Compliance Export </comply/cloud-compliance-export>` - Create compliance reports from the Mattermost System Console. 
* :doc:`Data Retention Policy </comply/cloud-data-retention-policy>` - Set custom data retention policies to manage how long Mattermost retains messages and file uploads.
* :doc:`Custom Terms of Service </comply/cloud-custom-terms-of-service>` - Define custom terms of service for users to accept before joining your Mattermost server.


Self-Hosted Admin
-----------------

This section of the guide is for administrators of self-hosted Mattermost servers. If you are the administrator for a Mattermost cloud workspace, please refer to the cloud section of this page.


Self-Hosted Setup & Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Initial Setup
"""""""""""""
.. toctree::
    :maxdepth: 1
    :hidden:

    Configuration Overview </configure/configuration-settings>
    Custom Branding Tools </configure/custom-branding-tools>
    Customize Mattermost </configure/customizing-mattermost>
    SMTP Email Setup </configure/smtp-email>


* :doc:`Configuration Overview </configure/configuration-settings>` - Setup and configure your Mattermost cloud workspace.
* :doc:`Custom Branding Tools </configure/custom-branding-tools>` - Change Mattermost branding, site name, and description. 
* :doc:`Customize Mattermost </configure/customizing-mattermost>` - Whitelabel the Mattermost server and apps.
* :doc:`SMTP Email Setup </configure/smtp-email>` - Connect to an email server to send emails for password resets and system notifications.

Advanced Configurations
"""""""""""""""""""""""
.. toctree::
    :maxdepth: 1
    :hidden:

    Shared Channels </onboard/shared-channels>
    Store Mattermost Configuration in the Database </configure/configuation-in-mattermost-database>
    Email Templates </configure/email-templates>
    Configuring CloudFront to host Mattermost static assets </configure/configuring-cloudfront-to-host-mattermost-static-assets>
    Use an Outbound Proxy </configure/using-outbound-proxy>
    Chinese, Japanese, and Korean Search </configure/enabling-chinese-japanese-korean-search>


* :doc:`Shared Channels </onboard/shared-channels>` - Connect channels from multiple Mattermost servers in a federated architecture.
* :doc:`Include Configuration in the Mattermost Database </configure/configuation-in-mattermost-database>` - Store Mattermost configuration information in your database rather than as a JSON file. We recommend this for high-availability environments.
* :doc:`Email Templates </configure/email-templates>` - Alter the transactional emails Mattermost sends to your users.
* :doc:`Configuring CloudFront to host Mattermost static assets </configure/configuring-cloudfront-to-host-mattermost-static-assets>` - Improve caching performance to reduce content load times.
* :doc:`Using an Outbound Proxy </configure/using-outbound-proxy>` - Monitor outbound traffic and control the websites that can appear in embedded content.
* :doc:`Chinese, Japanese, and Korean Search </configure/enabling-chinese-japanese-korean-search>` - Set up search capabilities for teams communicating via Chinese, Japanese, or Korean.

User Onboarding
"""""""""""""""
.. toctree::
    :maxdepth: 1
    :hidden:

    Provisioning Workflows </onboard/user-provisioning-workflows>
    Bulk Loading Data </onboard/bulk-loading-data>
    Migration Guide </onboard/migrating-to-mattermost>


* :doc:`Provisioning Workflows </onboard/user-provisioning-workflows>` - Learn how to provision and de-provision user accounts.
* :doc:`Bulk Loading Data </onboard/bulk-loading-data>` - Import bulk data into Mattermost for teams, channels, users, post content, and more.
* :doc:`Migration Guide </onboard/migrating-to-mattermost>` - Learn how to migrate from other chat services to Mattermost.

Advanced User Management Configurations
"""""""""""""""""""""""""""""""""""""""
.. toctree::
    :maxdepth: 1
    :hidden:

    AD/LDAP Groups </onboard/ad-ldap-groups-synchronization>
    Guest Accounts </onboard/guest-accounts>
    Using AD/LDAP Synchronized Groups to Manage Team or Private Channel Membership </onboard/managing-team-channel-membership-using-ad-ldap-sync-groups>
    SAML Single Sign-On </onboard/sso-saml>
    SAML Single-Sign-On: Technical Documentation </onboard/sso-saml-technical>
    SSL Client Certificate Setup </onboard/ssl-client-certificate>
    Certificate-Based Authentication </onboard/certificate-based-authentication>


* :doc:`AD/LDAP Groups </onboard/ad-ldap-groups-synchronization>` - Sync AD/LDAP groups with Mattermost roles and teams.
* :doc:`Guest Accounts </onboard/guest-accounts>` - Create guest accounts to collaborate with individuals outside your organization.
* :doc:`Using AD/LDAP Synchronized Groups to Manage Team or Private Channel Membership </onboard/managing-team-channel-membership-using-ad-ldap-sync-groups>` - Synchronize your AD/LDAP group with private Mattermost channels and teams.
* :doc:`SAML Single Sign-On </onboard/sso-saml>` - Configure Mattermost to be a SAML 2.0 service provider.
* :doc:`SAML Single-Sign-On: Technical Documentation </onboard/sso-saml-technical>` - SAML 2.0 reference documentation for Mattermost.
* :doc:`SSL Client Certificate Setup </onboard/ssl-client-certificate>` - Configure SSL client certificates for Mattermost Desktop and Web Apps.
* :doc:`Certificate-Based Authentication </onboard/certificate-based-authentication>` - Set up certificate-based authentication for Mattermost.


Self-Hosted Server Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. toctree::
    :maxdepth: 1
    :hidden:

    Managing Team and Channel Members </manage/team-channel-members>
    Statistics </manage/statistics>
    In-Product Notices </manage/in-product-notices>
    User Satisfaction Surveys </manage/user-satisfaction-surveys>
    Health Check </manage/health-checks>
    Announcement Banner </manage/announcement-banner>
    Bulk Export Tool </manage/bulk-export-tool>


* :doc:`Managing Team and Channel Members </manage/team-channel-members>` - Manage synchronization, moderation, and membership settings.
* :doc:`Statistics </manage/statistics>` - Get statistics about your Mattermost server usage.
* :doc:`In-Product Notices </manage/in-product-notices>` - Get notified about Mattermost updates via in-app notices.
* :doc:`User Satisfaction Surveys </manage/user-satisfaction-surveys>` - Learn about Mattermost user satisfaction surveys and how to configure their operation.
* :doc:`Health Check </manage/health-checks>` - Configure health probes for your Mattermost server.
* :doc:`Announcement Banner </manage/announcement-banner>` - Display notices to your users via an announcement banner.
* :doc:`Bulk Export Tool </manage/bulk-export-tool>` - Export user, team, channel, and post data from Mattermost.


Self-Hosted Compliance
^^^^^^^^^^^^^^^^^^^^^^
.. toctree::
    :maxdepth: 1
    :hidden:

    Electronic Discovery </comply/electronic-discovery>
    Compliance Export Beta </comply/compliance-export>
    Audit Log v2 (Experimental) </comply/audit-log>
    Data Retention Policy </comply/data-retention-policy>
    Custom Terms of Service (Beta) </comply/custom-terms-of-service>

* :doc:`Electronic Discovery </comply/electronic-discovery>` - Extract data from Mattermost for eDiscovery use in legal cases.
* :doc:`Compliance Export Beta </comply/compliance-export>` - Create compliance reports from the Mattermost System Console. 
* :doc:`Audit Log v2 (Experimental) </comply/audit-log>` - Review a comprehensive list of events that occur on your Mattermost Server
* :doc:`Data Retention Policy </comply/data-retention-policy>` - Set custom data retention policies to manage how long Mattermost retains messages and file uploads.
* :doc:`Custom Terms of Service (Beta) </comply/custom-terms-of-service>` - Define custom terms of service for users to accept before joining your Mattermost server.


Other Resources
---------------
.. toctree::
    :maxdepth: 1
    :hidden:

    Converting OAuth 2.0 Service Providers to OpenID Connect </onboard/convert-oauth20-service-providers-to-openidconnect>
    Generate a Support Packet </manage/generating-support-packet>
    mmctl Command Line Tool (Beta) </manage/mmctl-command-line-tool>
    Migration Announcement Email Template </onboard/migration-announcement-email>
    Configuring Apache2 (Unofficial) </configure/configuring-apache2>
    Advanced Permissions: Backend Infrastructure </onboard/advanced-permissions-backend-infrastructure>
    Command Line Tools </manage/command-line-tools>
    Scripts </manage/scripts>


If the information above doesn’t solve your problem, look at these other resources to find something that meets your needs. Alternatively, you can also :doc:`get help </guides/get-help>` from our community or via premium support services.



* :doc:`Converting OAuth 2.0 Service Providers to OpenID Connect </onboard/convert-oauth20-service-providers-to-openidconnect>` - Migrate from OAuth 2.0 to OpenID Connect.
* :doc:`Generate a Support Packet </manage/generating-support-packet>` - Generate configuration information, logs, plugin details, and data dependencies to provide when contacting Mattermost support.
* :doc:`mmctl Command Line Tool (Beta) </manage/mmctl-command-line-tool>` - Use mmctl to manage self-hosted Mattermost servers from the command line.
* :doc:`Migration Announcement Email Template </onboard/migration-announcement-email>` - Use this email template to notify your users about migrating to Mattermost.
* :doc:`Configuring Apache2 (Unofficial) </configure/configuring-apache2>` - Replace the default NGINX proxy with Apache2 for self-hosted Mattermost servers.
* :doc:`Advanced Permissions: Backend Infrastructure </onboard/advanced-permissions-backend-infrastructure>` - Read our technical guide on modifying self-hosted Mattermost installations to create custom permissions schemes.
* :doc:`Command Line Tools </manage/command-line-tools>` - Learn how to use the command line to manage self-hosted Mattermost servers.
* :doc:`Scripts </manage/scripts>` - Explore a selection of example scripts you can use to manage self-hosted Mattermost servers.