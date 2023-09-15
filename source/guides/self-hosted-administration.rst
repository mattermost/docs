Self-hosted administration
==========================

This section of the guide is for system admins of self-hosted Mattermost servers. If you're the admin for a Mattermost Cloud workspace, please refer to the `Cloud workspace management </guides/administration.html#cloud-workspace-management>`__ section on this page.

.. toctree::
    :maxdepth: 1
    :hidden:
    :titlesonly:

    Mattermost self-hosted billing </manage/self-hosted-billing>
    Store configuration in the database </configure/configuation-in-a-database>
    Bulk loading data </onboard/bulk-loading-data>
    SMTP email setup </configure/smtp-email>
    Email templates </configure/email-templates>
    Calls deployment </configure/calls-deployment>
    Configure CloudFront to host static assets </configure/configuring-cloudfront-to-host-mattermost-static-assets>
    Use an outbound proxy </configure/using-outbound-proxy>
    Migration guide </onboard/migrating-to-mattermost>
    Migration from MySQL to PostgreSQL </deploy/postgres-migration>
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
* :doc:`Migration guidelines from MySQL to PostgreSQL </deploy/postgres-migration>` - Learn how to migrate the Mattermost database from MySQL to PostgreSQL.
* :doc:`Chinese, Japanese, and Korean search </configure/enabling-chinese-japanese-korean-search>` - Set up search capabilities for teams communicating via Chinese, Japanese, or Korean.
* :doc:`Whitelabel Mattermost </configure/customizing-mattermost>` - Whitelabel the Mattermost server and apps.
* :doc:`Audit logging </comply/audit-log>` - Learn how Mattermost records activities and events performed within a Mattermost workspace.
* :doc:`JSON audit log schema </comply/embedded-json-audit-log-schema>` - Learn how to configure Mattermost audit logging using a JSON object.
* :doc:`SSL client certificate setup </onboard/ssl-client-certificate>` - Configure SSL client certificates for Mattermost Desktop and Web Apps.
* :doc:`Certificate-Based Authentication </onboard/certificate-based-authentication>` - Set up certificate-based authentication for Mattermost.
* :doc:`Manage telemetry </manage/telemetry>` - Self-hosted system admins can opt out of sharing telemetry data with Mattermost.