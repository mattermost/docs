Set up your Mattermost server
==============================

The following resources will help you get your Mattermost self-hosted server or Cloud-based workspace up and running:

.. toctree::
   :maxdepth: 1
   :hidden:

    Configure TLS on Mattermost server </deploy/configure-tls>
    Install NGINX server </deploy/install-nginx-server>
    SSL client certificate setup </onboard/ssl-client-certificate>
    Certificate-based authentication </onboard/certificate-based-authentication>
    Set up SMTP email </configure/smtp-email>
    Configure CloudFront </configure/configuring-cloudfront-to-host-mattermost-static-assets>
    Use an outbound proxy </configure/using-outbound-proxy>
    Use an image proxy </deploy/image-proxy>
    Backup and disaster recovery </deploy/backup-disaster-recovery>
    Encryption options </deploy/encryption-options>
    Configure transport encryption </install/transport-encryption>
    Configure Bleve search </deploy/bleve-search>
    Audit logging </comply/audit-log>
    
* :doc:`Configure TLS on your Mattermost server </deploy/configure-tls>` - Configure Mattermost so that your users can connect with HTTPS.
* :doc:`Install NGINX server </deploy/install-nginx-server>`- Use NGINX as a proxy server for greater security and performance of Mattermost.
* :doc:`SSL client certificate setup </onboard/ssl-client-certificate>` - Configure SSL client certificates for Mattermost Desktop and Web Apps.
* :doc:`Certificate-based authentication </onboard/certificate-based-authentication>` - Set up certificate-based authentication for Mattermost.
* :doc:`Set up SMTP email </configure/smtp-email>` - Configure Mattermost to send outgoing emails.
* :doc:`Configure CloudFront </configure/configuring-cloudfront-to-host-mattermost-static-assets>` - Configure CloudFront to host Mattermost static assets.
* :doc:`Use an outbound proxy </configure/using-outbound-proxy>` - Use Mattermost behind a proxy.
* :doc:`Use an image proxy </deploy/image-proxy>` - Set up an image proxy to make loading images faster and more reliable and prevent pixel tracking.
* :doc:`Backup and disaster recovery </deploy/backup-disaster-recovery>` - Implement data backups, disaster recovery, and high availability deployment.
* :doc:`Encryption options </deploy/encryption-options>`  - Set up encryption for data in transit and at rest.
* :doc:`Configure transport encryption </install/transport-encryption>` - Use transport encryption between Mattermost clusters and your proxy and database.
* :doc:`Configure Bleve search </deploy/bleve-search>` - Use the Bleve search engine to provide Lucene-style full-text search.
* :doc:`Audit logging </comply/audit-log>` - Set up audit logging to record activities and events performed within a Mattermost workspace.

----

Once your Mattermost workspace is operational, use the following resources to customize your workspace for your organization:

.. toctree::
   :maxdepth: 2
   :hidden:

    Customize email templates </configure/email-templates>
    Whitelabel Mattermost </configure/customizing-mattermost>
    Custom branding </configure/custom-branding-tools>
    Custom terms of service </comply/custom-terms-of-service>
    Enable Chinese, Japanese, and Korean search </configure/enabling-chinese-japanese-korean-search>

* :doc:`Customize email templates </configure/email-templates>` - Customize emails sent from Mattermost.
* :doc:`Whitelabel Mattermost </configure/customizing-mattermost>` - Brand your Mattermost workspace.
* :doc:`Custom branding </configure/custom-branding-tools>` - Use Mattermost branding tools to customize your Mattemrost login screen.
* :doc:`Custom terms of service </comply/custom-terms-of-service>` - Customize the terms of service your team members accept to use your Mattermost workspace.
* :doc:`Enable Chinese, Japanese, and Korean search </configure/enabling-chinese-japanese-korean-search>` - Enable your users to search Mattermost in Chinese, Japanese, and Korean.

