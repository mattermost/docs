Mattermost administration guide
===============================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

This guide is for people who administer an existing Mattermost server. It’s divided into four parts:

* `Get started </guides/administration.html#get-started>`__ - An overview of standard configurations and features for both self-hosted and Cloud workspaces.
* `Cloud workspace management </guides/administration.html#workspace-management>`__ - Detailed information about admin capabilities of Mattermost Cloud workspaces.
* `Self-hosted administration </guides/administration.html#self-hosted-admin>`__ - Detailed information about admin capabilities of self-hosted Mattermost servers.
* `Other resources </guides/administration.html#other-resources>`__ - Additional migration, conversion, and troubleshooting resources.

If you’re looking for resources to help you install, deploy, and scale your self-hosted Mattermost server, see the :doc:`Mattermost Deployment Guide </guides/deployment>`.

Get started
------------
.. toctree::
    :maxdepth: 1
    :hidden:

    Optimize your workspace </configure/optimize-your-workspace>
    Mattermost configuration settings </configure/configuration-settings>
    Self-hosted edition and license </configure/self-hosted-account-settings>
    Cloud subscription, billing, and account </configure/cloud-billing-account-settings>
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
    Environment variables </configure/environment-variables>
    Provisioning workflows </onboard/user-provisioning-workflows>
    Multi-factor authentication </onboard/multi-factor-authentication>
    Active Directory/LDAP </onboard/ad-ldap>
    GitLab SSO </onboard/sso-gitlab>
    OpenID SSO </onboard/sso-openidconnect>
    Google SSO </onboard/sso-google>
    Office 365 SSO </onboard/sso-office>
    Advanced permissions </onboard/advanced-permissions>
    System admin roles </onboard/system-admin-roles>
    Manage team and channel members </manage/team-channel-members>
    Custom branding tools </configure/custom-branding-tools>
    eDiscovery </comply/electronic-discovery>
    Compliance monitoring </comply/compliance-monitoring>
    Compliance export </comply/compliance-export>
    Data retention tools </comply/data-retention-policy>
    Custom terms of service </comply/custom-terms-of-service>
    Notify Admin </upgrade/notify-admin>

These resources will help you get started with your Mattermost self-hosted or Cloud workspace.

* **Optimize your workspace** - Review health and growth scores for your Mattermost workspace, and take necessary action using the :doc:`workspace optimization </configure/optimize-your-workspace>` page in the System Console.
* **Configure your workspace** - Mattermost offers extensive configuration options for both `self-hosted Mattermost servers and Mattermost Cloud workspaces </configure/configuration-settings.html>`__, and provides a list of :doc:`deprecated configuration settings </configure/deprecated-configuration-settings>` no longer supported.
* **Environment variables** - Learn how to use :doc:`environment variables </configure/environment-variables>` to manage configuration for a self-hosted deployment.
* **Provisioning workflows** - Learn how to :doc:`provision </onboard/user-provisioning-workflows>` and de-provision user accounts.
* **User authentication** - All versions of Mattermost provide basic authentication and offer :doc:`multi-factor authentication </onboard/multi-factor-authentication>` out of the box. Professional and Enterprise versions of Mattermost also include :doc:`Active Directory/LDAP </onboard/ad-ldap>` and SSO for :doc:`GitLab SSO </onboard/sso-gitlab>`, :doc:`OpenID </onboard/sso-openidconnect>`, :doc:`Google </onboard/sso-google>`, and :doc:`Office365 </onboard/sso-office>`.
* **User permissions** - All versions of Mattermost offer standard user permissions control. Professional and Enterprise versions also include :doc:`advanced permissions control </onboard/advanced-permissions>` to customize which users can perform specific actions, and :doc:`System Admin roles </onboard/system-admin-roles>` to grant admins from your organization access to specific areas of the Mattermost System Console.
* **Manage team and channel members** - :doc:`Manage team and channel members </manage/team-channel-members>` synchronization, moderation, and membership settings.
* **Customize branding** - Change Mattermost branding, site name, and description with :doc:`custom branding tools </configure/custom-branding-tools>`.
* **Compliance tools** - Extract data from Mattermost for :doc:`eDiscovery </comply/electronic-discovery>` use in legal cases, create :doc:`Compliance monitoring </comply/compliance-monitoring>` reports for query and download actions, or :doc:`Compliance export </comply/compliance-export>` reports for channel history actions, set custom :doc:`data retention policies </comply/data-retention-policy>`, and set :doc:`custom terms of service </comply/custom-terms-of-service>` for team members.
* **Notify admin** - Keep track of your users' :doc:`feature requirement needs </upgrade/notify-admin>`.

Advanced user management
~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
    :maxdepth: 1
    :hidden:

    AD/LDAP groups </onboard/ad-ldap-groups-synchronization>
    Use AD/LDAP synchronized groups to manage team or private channel membership </onboard/managing-team-channel-membership-using-ad-ldap-sync-groups>
    Guest accounts </onboard/guest-accounts>
    SAML Single Sign-On </onboard/sso-saml>
    SAML Single-Sign-On: technical documentation </onboard/sso-saml-technical>

* :doc:`AD/LDAP groups </onboard/ad-ldap-groups-synchronization>` - Sync AD/LDAP groups with Mattermost roles and teams.
* :doc:`Use AD/LDAP synchronized groups to manage team or private channel membership </onboard/managing-team-channel-membership-using-ad-ldap-sync-groups>` - Synchronize your AD/LDAP group with private Mattermost channels and teams.
* :doc:`Guest accounts </onboard/guest-accounts>` - Create guest accounts to collaborate with individuals outside your organization.
* :doc:`SAML Single Sign-On </onboard/sso-saml>` - Configure Mattermost to be a SAML 2.0 service provider.
* :doc:`SAML Single Sign-On: technical documentation </onboard/sso-saml-technical>` - SAML 2.0 reference documentation for Mattermost.

Advanced workspace management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
    :maxdepth: 1
    :hidden:

    Shared channels </onboard/shared-channels>
    Statistics </manage/statistics>
    In-product notices </manage/in-product-notices>
    User satisfaction surveys </manage/user-satisfaction-surveys>
    Health check </manage/health-checks>
    Announcement banner </manage/announcement-banner>
    Bulk export tool </manage/bulk-export-tool>

* :doc:`Shared channels </onboard/shared-channels>` - Connect channels from multiple Mattermost servers in a federated architecture.
* :doc:`Statistics </manage/statistics>` - Get statistics about your Mattermost server usage.
* :doc:`In-product notices </manage/in-product-notices>` - Get notified about Mattermost updates via in-app notices.
* :doc:`User satisfaction surveys </manage/user-satisfaction-surveys>` - Learn about Mattermost user satisfaction surveys and how to configure their operation.
* :doc:`Health check </manage/health-checks>` - Configure health probes for your Mattermost server.
* :doc:`Announcement banner </manage/announcement-banner>` - Display notices to your users via an announcement banner.
* :doc:`Bulk export tool </manage/bulk-export-tool>` - Export user, team, channel, and post data from Mattermost.

Cloud workspace management
--------------------------

.. toctree::
    :maxdepth: 1
    :hidden:

    Mattermost Cloud billing </manage/cloud-billing>
    Workspace usage </manage/workspace-usage>
    Workspace migration </manage/cloud-data-export>
    Cloud data residency </manage/cloud-data-residency>

* :doc:`Mattermost Cloud billing </manage/cloud-billing>` - Set up and manage billing for your Mattermost Cloud workspace.
* :doc:`Workspace usage </manage/workspace-usage>` - Keep your workspace active.
* :doc:`Workspace migration </manage/cloud-data-export>` - Migrate your workspace using the mmctl tool.
* :doc:`Cloud data residency </manage/cloud-data-residency>` - Find information about your data in the Cloud.

Self-hosted administration
--------------------------

This section of the guide is for system admins of self-hosted Mattermost servers. If you're the admin for a Mattermost Cloud workspace, please refer to the `Cloud workspace management </guides/administration.html#cloud-workspace-management>`__ section on this page.

.. toctree::
    :maxdepth: 1
    :hidden:

    Mattermost self-hosted billing </manage/self-hosted-billing>
    Store configuration in the database </configure/configuation-in-a-database>
    Bulk loading data </onboard/bulk-loading-data>
    SMTP email setup </configure/smtp-email>
    Email templates </configure/email-templates>
    Calls deployment </configure/calls-deployment>
    Configure CloudFront to host static assets </configure/configuring-cloudfront-to-host-mattermost-static-assets>
    Use an outbound proxy </configure/using-outbound-proxy>
    Migration guide </onboard/migrating-to-mattermost>
    Chinese, Japanese, and Korean search </configure/enabling-chinese-japanese-korean-search>
    Customize Mattermost </configure/customizing-mattermost>
    Audit logging </comply/audit-log>
    JSON audit log schema </comply/embedded-json-audit-log-schema>
    SSL client certificate setup </onboard/ssl-client-certificate>
    Certificate-based authentication </onboard/certificate-based-authentication>
    Manage telemetry </manage/telemetry>

* :doc:`Mattermost self-hosted billing </manage/self-hosted-billing>` - Manage your Mattermost subscription.
* :doc:`Include configuration in the Mattermost database </configure/configuation-in-a-database>` - Store Mattermost configuration information in your database rather than as a JSON file. We recommend this for High Availability environments.
* :doc:`Bulk loading data </onboard/bulk-loading-data>` - Import bulk data into Mattermost for teams, channels, users, post content, and more.
* :doc:`SMTP email setup </configure/smtp-email>` - Connect to an email server to send emails for password resets and system notifications.
* :doc:`Email templates </configure/email-templates>` - Alter the transactional emails Mattermost sends to your users.
* :doc:`Calls deployment </configure/calls-deployment>` - Learn about the different calls deployment types.
* :doc:`Configure CloudFront to host Mattermost static assets </configure/configuring-cloudfront-to-host-mattermost-static-assets>` - Improve caching performance to reduce content load times.
* :doc:`Use an outbound proxy </configure/using-outbound-proxy>` - Monitor outbound traffic and control the websites that can appear in embedded content.
* :doc:`Migration guide </onboard/migrating-to-mattermost>` - Learn how to migrate from other chat services to Mattermost.
* :doc:`Chinese, Japanese, and Korean search </configure/enabling-chinese-japanese-korean-search>` - Set up search capabilities for teams communicating via Chinese, Japanese, or Korean.
* :doc:`Whitelabel Mattermost </configure/customizing-mattermost>` - Whitelabel the Mattermost server and apps.
* :doc:`Audit logging </comply/audit-log>` - Learn how Mattermost records activities and events performed within a Mattermost workspace.
* :doc:`JSON audit log schema </comply/embedded-json-audit-log-schema>` - Learn how to configure Mattermost audit logging using a JSON object.
* :doc:`SSL client certificate setup </onboard/ssl-client-certificate>` - Configure SSL client certificates for Mattermost Desktop and Web Apps.
* :doc:`Certificate-Based Authentication </onboard/certificate-based-authentication>` - Set up certificate-based authentication for Mattermost.
* :doc:`Manage telemetry </manage/telemetry>` - Self-hosted system admins can opt out of sharing telemetry data with Mattermost.

Other resources
---------------
.. toctree::
    :maxdepth: 1
    :hidden:

    Convert OAuth 2.0 providers to OpenID Connect </onboard/convert-oauth20-service-providers-to-openidconnect>
    Generate a support packet </manage/generating-support-packet>
    mmctl command line tool </manage/mmctl-command-line-tool>
    Migration announcement email template </onboard/migration-announcement-email>
    Advanced permissions infrastructure </onboard/advanced-permissions-backend-infrastructure>
    Command line tools </manage/command-line-tools>

If the information above doesn’t solve your problem, look at these other resources to find something that meets your needs. Alternatively, you can also :doc:`get help </guides/get-help>` from our community or via premium support services.

* :doc:`Convert OAuth 2.0 service providers to OpenID Connect </onboard/convert-oauth20-service-providers-to-openidconnect>` - Migrate from OAuth 2.0 to OpenID Connect.
* :doc:`Generate a support packet </manage/generating-support-packet>` - Generate configuration information, logs, plugin details, and data dependencies to provide when contacting Mattermost support.
* :doc:`mmctl command line tool </manage/mmctl-command-line-tool>` - Use mmctl to manage self-hosted Mattermost servers from the command line.
* :doc:`Migration announcement email template </onboard/migration-announcement-email>` - Use this email template to notify your users about migrating to Mattermost.
* :doc:`Advanced permissions: backend infrastructure </onboard/advanced-permissions-backend-infrastructure>` - Read our technical guide on modifying self-hosted Mattermost installations to create custom permissions schemes.
* :doc:`Command line tools </manage/command-line-tools>` - Learn how to use the command line to manage self-hosted Mattermost servers.
