Make your deployment production-ready
=====================================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

On this page, you'll learn about some of the key self-hosted workspace configuration options available for production readiness that deliver the best possible Mattermost user experience to your users.

.. tip::
    We encourage you to explore all of the settings available in the System Console. See the `configuration settings <https://docs.mattermost.com/configure/configuration-settings.html>`__ documentation for details.

Ensure Mattermost is accessible and perfomant 
----------------------------------------------

1. Go to the **System Console > Environment** page, then review the following configuration options:

    +------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Go to...                     | To...                                                                                                                                                                                               |
    +==============================+=====================================================================================================================================================================================================+
    | **Web Server**               | Ensure your workspace is accessible online. See the `web server <https://docs.mattermost.com/configure/web-server-configuration-settings.html>`__ documentation for details.                        |
    +------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **Database**                 | Ensure that data management is configured for your needs. See the `database <https://docs.mattermost.com/configure/database-configuration-settings.html>`__ documentation for details.              |
    |                              |                                                                                                                                                                                                     |
    |                              | If you have a `High Availability <https://docs.mattermost.com/scale/high-availability-cluster.html>`__  environment using PostgreSQL, we also recommend specific optimizations.                     |
    |                              | See the `High Availability cluster recommendations <https://docs.mattermost.com/scale/high-availability-cluster.html#recommended-configuration-settings>`__ documentation for details.              |
    +------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **File Storage**             | Ensure that file storage is configured for your needs. See the `file storage <https://docs.mattermost.com/configure/configuration-settings.html#file-storage>`__ documentation for details.         |
    +------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

2. Go to the **System Console > Site Configuration** page, then customize key links and enhance file sharing functionality:

    +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Go to...                       | To...                                                                                                                                                                                                 |
    +================================+=======================================================================================================================================================================================================+
    | **Customization**              | Brand and customize your Mattermost workspace by:                                                                                                                                                     |
    |                                |                                                                                                                                                                                                       |
    |                                | - Customizing the `support email <https://docs.mattermost.com/configure/configuration-settings.html#support-email>`__ for email notifications, onboarding tutorials, and support questions.           |
    |                                | - Customizing the `help link <https://docs.mattermost.com/configure/configuration-settings.html#help-link>`__ to link to your help desk ticketing system.                                             |
    +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **File Sharing and Downloads** | `File sharing <https://docs.mattermost.com/configure/configuration-settings.html#allow-file-sharing>`__ is enabled by default.                                                                        |
    |                                | You can control of the `maximum size of file attachments <https://docs.mattermost.com/configure/configuration-settings.html#maximum-image-resolution>`__.                                             |
    |                                |                                                                                                                                                                                                       |
    |                                | If your organization frequently works with SVG files, `enable previews of SVG attachments <https://docs.mattermost.com/configure/configuration-settings.html#enable-svgs>`__.                         |
    |                                |                                                                                                                                                                                                       |
    |                                | For additional security and protection with file attachments, a `ClamAV antivirus <https://mattermost.com/marketplace/antivirus-plugin/>`__                                                           |
    |                                | integration is available which scans files uploaded to Mattermost.                                                                                                                                    |
    +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Configure SMTP email
---------------------

To run in production, Mattermost requires SMTP email to be enabled for email notifications and password reset for systems using email-based authentication. See the `SMTP email setup <https://docs.mattermost.com/configure/smtp-email.html>`__ documentation for details on how to enable email by configuring an SMTP service.

What's next?
------------

Now that you've reviewed key configuration settings for production readiness, you'll want to learn how to :doc:`onboard users </getting-started/get-started-onboard-users>`, :doc:`simplify user authentication </getting-started/get-started-onboard-users.html#onboard-users-in-bulk>`, and :doc:`control product access </getting-started/get-started-onboard-users.html#control-product-access>` through user roles and permissions.