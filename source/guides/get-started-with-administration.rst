Get started with administration
================================

.. toctree::
    :maxdepth: 1
    :hidden:
    :titlesonly:

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
    Legal hold </comply/legal-hold>
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
* **Compliance tools** - Extract data from Mattermost for :doc:`eDiscovery </comply/electronic-discovery>` use in legal cases, create :doc:`Compliance monitoring </comply/compliance-monitoring>` reports for query and download actions, or :doc:`Compliance export </comply/compliance-export>` reports for channel history actions, carry out a :doc:`legal hold </comply/legal-hold>`, set custom :doc:`data retention policies </comply/data-retention-policy>`, and set :doc:`custom terms of service </comply/custom-terms-of-service>` for team members.
* **Notify admin** - Keep track of your users' :doc:`feature requirement needs </upgrade/notify-admin>`.

Advanced user management
-------------------------

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
-----------------------------

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