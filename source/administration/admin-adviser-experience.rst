Admin Adviser Experience (AAE)
===============================

.. note::
  Mattermost AAE Message Codes were introduced in version 5.26. They are added retroactively to existing System Admin messages. 

Administrator Adviser Experience ("AAE") is a set of notifications and workflows to guide System Admins through the proper activation and configuration of system capabilities as the needs of their user base evolves. 

AAE includes: 

- Bot notifications to System Admins
- Notification alerts in the channel header (only visible to System Admins)
- A coding system to look up more information on errors and warnings

AAE Message Code System 
-------------------------------

Since Mattermost may be deployed in air-gapped networks where links to documentation aren’t always available, AAE uses human-readable message codes to uniquely identify errors, warnings and recommendations. These codes can be manually referenced in downloaded documentation, or through web search on a separate internet-connected device. 

Example: Please check connection, Mattermost unreachable. If issue persists, ask administrator to check WebSocket port. AAE-000-0010

The "AAE-010-0010" message code represents an entry within a directory of message codes that can be downloaded locally and used to troubleshoot common issues.

AAE Message Code Syntax
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AAE Message Codes consists of 12 characters, with the first four characters starting with "AAE-" followed by a three digit "Category & Subcategory" code, a hyphen, then a "Message ID" code. The format specifically is: 

"AAE-" & [Category & Subcategory] & "-" & [Message ID]

AAE Category & Subcategory 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AAE Message Codes are categorized as follows:

.. csv-table::
    :header: "Category", "Subcategory", "Category & Subcategory Code"

    "System Administration", "Common Issues", "010"

The classification of AAE codes is an iterative work in progress. We will use the AAE-010-XXX0 name space for the first few hundred issues, then analyze, categorize and subcategorize the AAE Categories and Subcategories, migrate to new codes, and deprecate the original AAE-010-XXX0, with information preserved for legacy deployments. 

AAE Message Code Registry 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following section lists out AAE codes with links to troubleshooting documentation.

.. csv-table::
    :header: "AAE Code", "Initial Release Version", "Message", "More Information"

    "AAE-010-0010", "5.26", "Please check connection, Mattermost unreachable. If issue persists, ask administrator to check WebSocket port. AAE-000-0010", "Potential proxy configuration issue. See `troubleshooting guide <https://docs.mattermost.com/install/troubleshooting.html#please-check-connection-mattermost-unreachable-if-issue-persists-ask-administrator-to-check-websocket-port>`_ to diagnose network connection."
    "AAE-010-0011", "5.26", "Preview Mode: Email notifications have not been configured. AAE-000-0011", "To run in production with email-based authentication, Mattermost requires SMTP to be configured for email notifications and password reset. See `SMTP setup guide <https://docs.mattermost.com/install/smtp-email-setup.html>`_ to configure email notifications."
    "AAE-010-0012", "5.26", "Please configure your site URL on the System Console. AAE-010-0012", "Site URL is required for email notifications, authentication and plugins to operate properly. See `configuration settings docs <https://docs.mattermost.com/administration/config-settings.html#site-url>`_ to configure your site URL."
    "AAE-010-0013", "5.26", "Please configure your site URL either on the System Console or, if you're using GitLab Mattermost, in gitlab.rb. AAE-010-0013", "Site URL is required for email notifications, authentication and plugins to operate properly. See `configuration settings docs <https://docs.mattermost.com/administration/config-settings.html#site-url>`_ to configure your site URL. If you’re using GitLab Mattermost, refer to `GitLab configuration docs <https://docs.gitlab.com/omnibus/gitlab-mattermost/#getting-started>`_."
    "AAE-010-0014", "5.26", "Enterprise license expires on {date}. Please renew. AAE-010-0014", "Enterprise features are disabled after your Enterprise license expires. `Renew your Enterprise Edition subscription. <https://mattermost.com/renew/>`_"
    "AAE-010-1010", "5.26", "Team exceeds {number of} users. Consider activating user management access controls to ensure compliance. AAE-010-1010", "Mattermost Team Edition scales to dozens of users. For larger systems, consider activating `user management access controls <https://docs.mattermost.com/deployment/advanced-permissions.html>`_. Learn more about `Mattermost Editions <https://docs.mattermost.com/overview/product.html#mattermost-editions>`_."
    "AAE-010-1011", "5.26", "Warning: More than {number of} messages sent through test push proxy service today. Consider switching to a production-grade hosted push notification service to ensure reliability. AAE-010-1011", "Mattermost test push proxy service is offered for testing setups. For production systems, consider using the `Hosted Push Notification Service (HPNS) <https://docs.mattermost.com/mobile/mobile-hpns.html>`_ to ensure production-level uptime."
    "AAE-010-1012", "5.26", "Messages exceed {number of}. Consider activating system monitoring and elasticsearch to avoid degraded performance. AAE-010-1012", "Mattermost Team Edition scales to 10,000s of messages. For larger systems, consider activating system monitoring and elasticsearch. Learn more about `Mattermost Editions <https://docs.mattermost.com/overview/product.html#mattermost-editions>`_."

Frequently Asked Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What happens when I click "Contact Support"?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you choose to contact support from the Mattermost system, an email is sent to support[at]mattermost.com with the Administrative Adviser Experience (AAE) message code summarizing your issue.

The email also includes the name and email address of the System Admin requesting support, along with site URL, user count and diagnostic ID to help the support team diagnose your issue.
