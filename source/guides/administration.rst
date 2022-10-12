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

* **Optimize your workspace** - Review health and growth scores for your Mattermost workspace, and take necessary action using the :doc:`workspace optimization </configure/optimize-your-workspace>` page in the System Console.
* **Configure your workspace** - Mattermost offers extensive configuration options for both :doc:`self-hosted Mattermost servers and Mattermost Cloud workspaces </configure/configuration-settings>`, and provides a list of :doc:`deprecated configuration settings </configure/deprecated-configuration-settings>` no longer supported.
* **Environment variables** - Learn how to use :doc:`environment variables </configure/environment-variables>` to manage configuration for self-hosted deployments.
* :doc:`Shared channels </onboard/shared-channels>` - Connect channels from multiple Mattermost servers in a federated architecture.
* **Statistics** - Review :doc:`statistics </manage/statistics>` about your Mattermost server usage.
* **In-product notices** - Notify users about Mattermost updates using :doc:`in-product notices </manage/in-product-notices>`.
* **User satisfaction surveys**  - Learn how to gather user feedback using :doc:`Mattermost user satisfaction surveys </manage/user-satisfaction-surveys>`.
* **Announcement banner**  - Display notices to your users via a dismissable :doc:`announcement banner </manage/announcement-banner>`.

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

* **Mattermost Cloud billing** - Set up and :doc:`manage billing </manage/cloud-billing>` for your Mattermost Cloud workspace.
* **Workspace limits** - Understand the :doc:`data and workspace limits </onboard/mattermost-limits>` of your plan.
* **Workspace usage** - Learn about :doc:`workspace usage </manage/workspace-usage>` and how to keep your workspace active.
* **Cloud data residency** - Learn about :doc:`how your data is stored in the Cloud </manage/cloud-data-residency>`.

Self-hosted workspace management
--------------------------------

If you're the admin for a Mattermost Cloud workspace, please refer to the `Cloud workspace management <https://docs.mattermost.com/guides/administration.html#cloud-workspace-management>`__ section on this page.

.. toctree::
    :maxdepth: 1
    :hidden:

    Mattermost configuration in the database </configure/configuation-in-mattermost-database>
    Deploy Mattermost calls </configure/calls-deployment>
    Configure health checks probes </manage/health-checks>
    Configure Mattermost Omnibus </install/configure-mattermost-omnibus>
    Kubernetes FAQ </install/faq-kubernetes>

* **Move Mattermost configuration to the database** - Learn how to :doc:`store Mattermost configuration information in your database </configure/configuation-in-mattermost-database>` rather than as a JSON file. Recommended this for High Availability environments.
* **Deploy Mattermost Calls** - Learn about the different ways you can :doc:`deploy Mattermost Calls </configure/calls-deployment>`.
* **Health check** - Configure :doc:`health check probes </manage/health-checks>` for your Mattermost server.
* **Configure Mattermost Omnibus** - Learn how to :doc:`configure </install/configure-mattermost-omnibus>`, backup, restore, and remove Mattermost Omnibus, as well as use a custom NIGINX template.
* **Kubernetes FAQ** - See :doc:`answers to common questions </install/faq-kubernetes>` about working with Kubernetes clusters.

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

* **Migrate from Cloud to self-hosted** - Learn how to :doc:`migrate from Mattermost Cloud to a self-hosted deployment </manage/cloud-data-export>`.
* **Migrate from other chat products** - Learn how to :doc:`migrate from other chat services </onboard/migrating-to-mattermost>` to Mattermost.
* **Migration announcement email** - An :doc:`email template </onboard/migration-announcement-email>` is available to help you notify your users about migrating to Mattermost.
* **Bulk load data** - Learn how to :doc:`import bulk data </onboard/bulk-loading-data>` into Mattermost for teams, channels, users, post content, and more.
* **Bulk export data** - Learn how to :doc:`export user, team, channel, and post data </manage/bulk-export-tool>` from Mattermost.

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
* **Convert OAuth 2.0 service providers to OpenID Connect** - Learn how to :doc:`migrate from OAuth 2.0 to OpenID Connect </onboard/convert-oauth20-service-providers-to-openidconnect>`.

User permissions
-----------------

.. toctree::
    :maxdepth: 1
    :hidden:

	Advanced permissions </onboard/advanced-permissions>
    Permissions backend infrastructure </onboard/advanced-permissions-backend-infrastructure>
	System Admin roles </onboard/system-admin-roles>

* **User permissions** - All versions of Mattermost offer standard user permissions control. Professional and Enterprise versions also include :doc:`advanced permissions control </onboard/advanced-permissions>` to customize which users can perform specific actions, and :doc:`System Admin roles </onboard/system-admin-roles>` to grant admins from your organization access to specific areas of the Mattermost System Console.
* **Advanced permissions: backend infrastructure** - Read our technical guide on :doc:`modifying self-hosted Mattermost permissions </onboard/advanced-permissions-backend-infrastructure>` to create custom permissions schemes.

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
* **AD/LDAP groups** - Sync :doc:`AD/LDAP groups </onboard/ad-ldap-groups-synchronization>` with Mattermost roles and teams.
* **Manage team or private channel membership with AD/LDAP synchronized groups** - :doc:`Synchronize your AD/LDAP groups </onboard/managing-team-channel-membership-using-ad-ldap-sync-groups>` with Mattermost private channels and teams.
* **Guest accounts** - Create :doc:`guest accounts </onboard/guest-accounts>` to collaborate with individuals outside your organization.
* **SAML SSO** - Configure Mattermost to be a :doc:`SAML 2.0 service provider </onboard/sso-saml>`.
* **SAML SSO technical documentation** - See the :doc:`SAML 2.0 reference documentation </onboard/sso-saml-technical>` for Mattermost.

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

Other resources
---------------

.. toctree::
    :maxdepth: 1
    :hidden:

    mmctl command line tool </manage/mmctl-command-line-tool>
    Command line tools </manage/command-line-tools>

* **mmctl command line tool** - Use :doc:`mmctl </manage/mmctl-command-line-tool>` to manage Mattermost workspaces from the command line.
* **Command line tools** - Learn how to use :doc:`command line tools </manage/command-line-tools>` to manage self-hosted Mattermost workspaces running releases prior to v6.0. 