Advanced server administration
==============================

This documentation is for system admins who manage an existing Mattermost instance. It’s divided into the following sections:

* `Advanced Mattermost tools <#advanced-mattermost-tools>`__
* `Self-hosted server resources <#self-hosted-server-resources>`__
* `Additional resources <#additional-resources>`__

If you’re looking for resources to help you install, configure, upgrade, and scale your self-hosted Mattermost server, see the :doc:`Mattermost Deployment Guide </guides/deployment>`.

Advanced Mattermost tools
-------------------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

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
    Whitelabel Mattermost </configure/custom-branding-tools>
    eDiscovery </comply/electronic-discovery>
    Compliance monitoring </comply/compliance-monitoring>
    Compliance export </comply/compliance-export>
    Data retention tools </comply/data-retention-policy>
    Custom terms of service </comply/custom-terms-of-service>
    Notify Admin </upgrade/notify-admin>

* :doc:`Shared channels </onboard/shared-channels>` - Connect channels from multiple Mattermost servers in a federated architecture.
* :doc:`Statistics </manage/statistics>` - Get statistics about your Mattermost server usage.
* :doc:`In-product notices </manage/in-product-notices>` - Get notified about Mattermost updates via in-app notices.
* :doc:`User satisfaction surveys </manage/user-satisfaction-surveys>` - Learn about Mattermost user satisfaction surveys and how to configure their operation.
* :doc:`Health check </manage/health-checks>` - Configure health probes for your Mattermost server.
* :doc:`Announcement banner </manage/announcement-banner>` - Display notices to your users via an announcement banner.
* :doc:`Bulk export tool </manage/bulk-export-tool>` - Export user, team, channel, and post data from Mattermost.
* :doc:`Whitelabel Mattermost </configure/custom-branding-tools>` - Change your site name and and description.
* **Compliance tools** - Extract data from Mattermost for :doc:`eDiscovery </comply/electronic-discovery>` use in legal cases, create :doc:`Compliance monitoring </comply/compliance-monitoring>` reports for query and download actions, or :doc:`Compliance export </comply/compliance-export>` reports for channel history actions, set custom :doc:`data retention policies </comply/data-retention-policy>`, and set :doc:`custom terms of service </comply/custom-terms-of-service>` for team members.
* :doc:`Notify admin </upgrade/notify-admin>` - Keep track of your users' feature requirement needs.

Self-hosted server resources
-----------------------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

This section of the guide is for system admins mangaging self-hosted Mattermost servers. If you're the admin for a Mattermost Cloud workspace, see the `Cloud workspace administration </guides/cloud-administration>`__ documentation. 

.. toctree::
    :maxdepth: 1
    :hidden:

    Environment variables </configure/environment-variables>
    Bulk loading data </onboard/bulk-loading-data>
    Email templates </configure/email-templates>
    Calls deployment </configure/calls-deployment>
    Configure CloudFront to host static assets </configure/configuring-cloudfront-to-host-mattermost-static-assets>
    Use an outbound proxy </configure/using-outbound-proxy>
    Migration guide </onboard/migrating-to-mattermost>
    Chinese, Japanese, and Korean search </configure/enabling-chinese-japanese-korean-search>
    Whitelabel Mattermost </configure/customizing-mattermost>
    Audit logging </comply/audit-log>
    JSON audit log schema </comply/embedded-json-audit-log-schema>
    Certificate-based authentication </onboard/certificate-based-authentication>
    Manage telemetry </manage/telemetry>

* :doc:`Environment variables </configure/environment-variables>` Learn how to manage configuration using environment variables.
* :doc:`Bulk loading data </onboard/bulk-loading-data>` - Import bulk data into Mattermost for teams, channels, users, post content, and more.
* :doc:`Email templates </configure/email-templates>` - Alter the transactional emails Mattermost sends to your users.
* :doc:`Calls deployment </configure/calls-deployment>` - Learn about the different calls deployment types.
* :doc:`Configure CloudFront to host Mattermost static assets </configure/configuring-cloudfront-to-host-mattermost-static-assets>` - Improve caching performance to reduce content load times.
* :doc:`Use an outbound proxy </configure/using-outbound-proxy>` - Monitor outbound traffic and control the websites that can appear in embedded content.
* :doc:`Migration guide </onboard/migrating-to-mattermost>` - Learn how to migrate from other chat services to Mattermost.
* :doc:`Chinese, Japanese, and Korean search </configure/enabling-chinese-japanese-korean-search>` - Set up search capabilities for teams communicating via Chinese, Japanese, or Korean.
* :doc:`Whitelabel Mattermost </configure/customizing-mattermost>` - Whitelabel the Mattermost server and apps.
* :doc:`Audit logging </comply/audit-log>` - Learn how Mattermost records activities and events performed within a Mattermost workspace.
* :doc:`JSON audit log schema </comply/embedded-json-audit-log-schema>` - Learn how to configure Mattermost audit logging using a JSON object.
* :doc:`Certificate-Based Authentication </onboard/certificate-based-authentication>` - Set up certificate-based authentication for Mattermost.
* :doc:`Manage telemetry </manage/telemetry>` - Self-hosted system admins can opt out of sharing telemetry data with Mattermost.

Additional resources
--------------------

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. toctree::
    :maxdepth: 1
    :hidden:

    Convert OAuth 2.0 providers to OpenID Connect </onboard/convert-oauth20-service-providers-to-openidconnect>
    Generate a support packet </manage/generating-support-packet>
    mmctl command line tool </manage/mmctl-command-line-tool>
    Migration announcement email template </onboard/migration-announcement-email>
    Command line tools </manage/command-line-tools>

If the information above doesn’t solve your problem, look at these other resources to find something that meets your needs. Alternatively, you can also :doc:`get help </guides/get-help>` from our community or via premium support services.

* :doc:`Convert OAuth 2.0 service providers to OpenID Connect </onboard/convert-oauth20-service-providers-to-openidconnect>` - Migrate from OAuth 2.0 to OpenID Connect.
* :doc:`Generate a support packet </manage/generating-support-packet>` - Generate configuration information, logs, plugin details, and data dependencies to provide when contacting Mattermost support.
* :doc:`mmctl command line tool </manage/mmctl-command-line-tool>` - Use mmctl to manage self-hosted Mattermost servers from the command line.
* :doc:`Migration announcement email template </onboard/migration-announcement-email>` - Use this email template to notify your users about migrating to Mattermost.
* :doc:`Command line tools </manage/command-line-tools>` - Learn how to use the command line to manage self-hosted Mattermost servers.