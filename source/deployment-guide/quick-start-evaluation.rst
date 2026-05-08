Quick Start Evaluation
======================

This guide provides instructions for quickly trying out Mattermost using either Docker or Azure Marketplace. These options are ideal for testing and evaluation purposes as they allow you to quickly get a Mattermost instance up and running for exploration and testing. However, these quick start options are not recommended for production use. They are configured for demonstration purposes only.

Deployment options
------------------

.. tab:: Azure Marketplace
  :parse-titles:

  .. include:: csp-marketplaces/azure/quick-start-evaluation.rst
    :start-after: :nosearch:

.. tab:: Docker Preview Container
  :parse-titles:

  The fastest way to try Mattermost is using the official Docker preview container. This method requires minimal setup and provides a fully functional Mattermost instance.

  Docker Preview Prerequisites
  ----------------------------

  * Docker installed on your system
  * At least 1GB of available RAM
  * At least 1GB of available disk space

  Run Mattermost using Docker
  ---------------------------

  1. Pull and run the Mattermost preview container:

    .. code-block:: bash

      docker run --name mattermost-preview -d --publish 8065:8065 mattermost/mattermost-preview

  2. Access Mattermost at ``http://localhost:8065``

  3. Create your first admin account when prompted.

Next steps
----------

After setting up your Mattermost instance using either method:

* Create your first team and channels
* Invite users to join your workspace
* Explore Mattermost features and integrations
* Review the :doc:`Application architecture </deployment-guide/reference-architecture/application-architecture>` to understand the system better
* Consider :doc:`Server deployment </deployment-guide/server/server-deployment-planning>` for a production deployment

For additional help or questions, visit the `Mattermost community forums <https://forum.mattermost.com/>`_ or refer to the :doc:`Deployment troubleshooting </deployment-guide/deployment-troubleshooting>` guide.

`Book a live demo <https://mattermost.com/request-demo/>`_  or `talk to a Mattermost expert <https://mattermost.com/contact-sales/>`_ to explore tailored solutions for your organization's secure collaboration needs. Or try Mattermost yourself with a `1-hour preview <https://mattermost.com/sign-up/>`_ for instant access to a live sandbox environment. 
