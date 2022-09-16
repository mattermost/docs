Manage your Mattermost workspace
================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

See the following resources to manage your Mattermost self-hosted or Cloud workspace: 

.. toctree::
    :maxdepth: 1
    :hidden:

    Optimize your workspace </configure/optimize-your-workspace>
    Configure your Mattermost workspace </configure/configuration-settings>
    Deprecated configuration settings </configure/deprecated-configuration-settings>
    Environment variables </configure/environment-variables>
    Set up shared channels </onboard/shared-channels>
	Review performance statistics </manage/statistics>
	Display in-product notices </manage/in-product-notices>
	Gather feedback with user satisfaction surveys </manage/user-satisfaction-surveys>
	Configure an announcement banner </manage/announcement-banner>
    Generate a support packet </manage/generating-support-packet>

* **Optimize your workspace** - Review health and growth scores for your Mattermost workspace, and take necessary action using the :doc:`workspace optimization </configure/optimize-your-workspace>` page in the System Console.
* **Configure your workspace** - Mattermost offers extensive configuration options for both `self-hosted Mattermost servers and Mattermost Cloud workspaces <https://docs.mattermost.com/configure/configuration-settings.html>`__, and provides a list of :doc:`deprecated configuration settings </configure/deprecated-configuration-settings>` no longer supported.
* **Environment variables** - Learn how to use :doc:`environment variables </configure/environment-variables>` to manage configuration for a self-hosted deployment.
* :doc:`Shared channels </onboard/shared-channels>` - Connect channels from multiple Mattermost servers in a federated architecture.
* :doc:`Statistics </manage/statistics>` - Get statistics about your Mattermost server usage.
* :doc:`In-product notices </manage/in-product-notices>` - Get notified about Mattermost updates via in-app notices.
* :doc:`User satisfaction surveys </manage/user-satisfaction-surveys>` - Learn about Mattermost user satisfaction surveys and how to configure their operation.
* :doc:`Announcement banner </manage/announcement-banner>` - Display notices to your users via an announcement banner.
* :doc:`Generate a support packet </manage/generating-support-packet>` - Generate configuration information, logs, plugin details, and data dependencies to provide when contacting Mattermost support.

.. note::
    
    - Looking for instructions on how to deploy Mattermost? See the :doc:`deployment </guides/deployment>` documentation for details. 
    - Some administrative functionality applies only to Cloud workspaces or self-hosted workspaces. See the sections below for details.

Cloud workspace management
--------------------------

.. toctree::
    :maxdepth: 1
    :hidden:

    Mattermost Cloud billing </manage/cloud-billing>
    Workspace limits </onboard/mattermost-limits>
    Workspace usage </manage/workspace-usage>
    Cloud data residency </manage/cloud-data-residency>

* :doc:`Mattermost Cloud billing </manage/cloud-billing>` - Set up and manage billing for your Mattermost Cloud workspace.
* :doc:`Workspace limits </onboard/mattermost-limits>` - Understand the data limits on your plan.
* :doc:`Workspace usage </manage/workspace-usage>` - Keep your workspace active.
* :doc:`Cloud data residency </manage/cloud-data-residency>` - Find information about your data in the Cloud.

Self-hosted workspace management
--------------------------------

If you're the admin for a Mattermost Cloud workspace, please refer to the `Cloud workspace management <https://docs.mattermost.com/guides/administration.html#cloud-workspace-management>`__ section on this page.

.. toctree::
    :maxdepth: 1
    :hidden:

    Mattermost configuration in the database </configure/configuation-in-mattermost-database>
    Deploy Mattermost calls </configure/calls-deployment>
    Configure health checks probes </manage/health-checks>

* :doc:`Move Mattermost configuration to the database </configure/configuation-in-mattermost-database>` - Store Mattermost configuration information in your database rather than as a JSON file. Recommended this for High Availability environments.
* :doc:`Deploy Mattermost calls </configure/calls-deployment>` - Learn about the different ways you can deploy Mattermost Calls.
* :doc:`Health check </manage/health-checks>` - Configure health probes for your Mattermost server.

Migrate your Mattermost workspace
---------------------------------

.. toctree::
    :maxdepth: 1
    :hidden:

	Cloud to Self-Hosted </manage/cloud-data-export>
    Migrate from other chat products </onboard/migrating-to-mattermost>
    Migration announcement email </onboard/migration-announcement-email>
    Bulk load data </onboard/bulk-loading-data>
    Bulk export data </manage/bulk-export-tool>

* :doc:`Migrate from  Cloud to self-hosted </manage/cloud-data-export>` - Migrate from Mattermost Cloud to a self-hosted deployment.
* :doc:`Migrate from other chat products </onboard/migrating-to-mattermost>` - Learn how to migrate from other chat services to Mattermost.
* :doc:`Migration announcement email </onboard/migration-announcement-email>` - An email template is available to help you notify your users about migrating to Mattermost.
* :doc:`Bulk load data </onboard/bulk-loading-data>` - Import bulk data into Mattermost for teams, channels, users, post content, and more.
* :doc:`Bulk export data </manage/bulk-export-tool>` - Export user, team, channel, and post data from Mattermost.

User authentication
--------------------

.. toctree::
    :maxdepth: 1
    :hidden:

    Enable multi-factor authentication </onboard/multi-factor-authentication>
    Set up AD/LDAP </onboard/ad-ldap>
    Set up GitLab SSO </onboard/sso-gitlab>
	Set up OpenID Connect SSO </onboard/sso-openidconnect>
	Set up Google SSO </onboard/sso-google>
	Set up Office SSO </onboard/sso-office>
    Convert OAuth 2.0 providers to OpenID Connect </onboard/convert-oauth20-service-providers-to-openidconnect>

* **User authentication** - All versions of Mattermost provide basic authentication and offer :doc:`multi-factor authentication </onboard/multi-factor-authentication>` out of the box. Professional and Enterprise versions of Mattermost also include :doc:`Active Directory/LDAP </onboard/ad-ldap>` and SSO for :doc:`GitLab SSO </onboard/sso-gitlab>`, :doc:`OpenID </onboard/sso-openidconnect>`, :doc:`Google </onboard/sso-google>`, and :doc:`Office365 </onboard/sso-office>`.
* :doc:`Convert OAuth 2.0 service providers to OpenID Connect </onboard/convert-oauth20-service-providers-to-openidconnect>` - Migrate from OAuth 2.0 to OpenID Connect.

User permissions
-----------------

.. toctree::
    :maxdepth: 1
    :hidden:

	Advanced permissions </onboard/advanced-permissions>
    Permissions backend infrastructure </onboard/advanced-permissions-backend-infrastructure>
	System Admin roles </onboard/system-admin-roles>

* **User permissions** - All versions of Mattermost offer standard user permissions control. Professional and Enterprise versions also include :doc:`advanced permissions control </onboard/advanced-permissions>` to customize which users can perform specific actions, and :doc:`System Admin roles </onboard/system-admin-roles>` to grant admins from your organization access to specific areas of the Mattermost System Console.
* :doc:`Advanced permissions: backend infrastructure </onboard/advanced-permissions-backend-infrastructure>` - Read our technical guide on modifying self-hosted Mattermost installations to create custom permissions schemes.

User management
---------------

.. toctree::
    :maxdepth: 1
    :hidden:

    Provisioning workflows </onboard/user-provisioning-workflows>
    Manage team and channel members </manage/team-channel-members>
    Sync AD/LDAP groups </onboard/ad-ldap-groups-synchronization>
    Use AD/LDAP groups to manage team or private channel membership </onboard/managing-team-channel-membership-using-ad-ldap-sync-groups>
    Guest accounts </onboard/guest-accounts>
    SAML SSO </onboard/sso-saml>
    SAML SSO technical documentation </onboard/sso-saml-technical>

* **Provisioning workflows** - Learn how to :doc:`provision </onboard/user-provisioning-workflows>` and de-provision user accounts.
* **Manage team and channel members** - :doc:`Manage team and channel members </manage/team-channel-members>` synchronization, moderation, and membership settings.
* :doc:`AD/LDAP groups </onboard/ad-ldap-groups-synchronization>` - Sync AD/LDAP groups with Mattermost roles and teams.
* :doc:`Use AD/LDAP synchronized groups to manage team or private channel membership </onboard/managing-team-channel-membership-using-ad-ldap-sync-groups>` - Synchronize your AD/LDAP group with private Mattermost channels and teams.
* :doc:`Guest accounts </onboard/guest-accounts>` - Create guest accounts to collaborate with individuals outside your organization.
* :doc:`SAML SSO </onboard/sso-saml>` - Configure Mattermost to be a SAML 2.0 service provider.
* :doc:`SAML SSO technical documentation </onboard/sso-saml-technical>` - SAML 2.0 reference documentation for Mattermost.

Compliance tools
----------------

.. toctree::
    :maxdepth: 1
    :hidden:

    eDiscovery </comply/electronic-discovery>
    Compliance monitoring </comply/compliance-monitoring>
    Compliance export </comply/compliance-export>
    Data retention tools </comply/data-retention-policy>

* **Compliance tools** - Extract data from Mattermost for :doc:`eDiscovery </comply/electronic-discovery>` use in legal cases, create :doc:`Compliance monitoring </comply/compliance-monitoring>` reports for query and download actions, create :doc:`Compliance export </comply/compliance-export>` reports for channel history actions, and set custom :doc:`data retention policies </comply/data-retention-policy>`.

Troubleshoot your Mattermost deployment
---------------------------------------

.. toctree::
    :maxdepth: 1
    :hidden:

    Troubleshoot Mattermost issues </install/troubleshooting>

* **Having trouble with your Mattermost deployment?** - See the :doc:`troubleshooting </install/troubleshooting>` documentation for details.

Other resources
---------------

.. toctree::
    :maxdepth: 1
    :hidden:

    mmctl command line tool </manage/mmctl-command-line-tool>
    Command line tools </manage/command-line-tools>

* :doc:`mmctl command line tool </manage/mmctl-command-line-tool>` - Use mmctl to manage Mattermost workspaces from the command line.
* :doc:`Command line tools </manage/command-line-tools>` - Learn how to use the command line to manage self-hosted Mattermost workspaces running releases prior to v6.0. 