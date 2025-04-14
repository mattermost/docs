Quick Start Evaluation
======================

This guide provides instructions for quickly trying out Mattermost using either Docker or Azure Marketplace. These options are ideal for testing and evaluation purposes as they allow you to quickly get a Mattermost instance up and running for exploration and testing. However, these quick start options are not recommended for production use. They use SQLite as the database and are configured for demonstration purposes only.

Deployment options
------------------

.. tab:: Azure Marketplace

    Mattermost is available as a pre-configured virtual machine image in the Azure Marketplace. This option is preferred for customers already using Azure, as it integrates seamlessly within their existing Azure infrastructure.

    **Prerequisites:**

    * An Azure subscription
    * Basic familiarity with Azure Portal

    **Steps to deploy Mattermost on Azure:**

    1. Visit the `Mattermost, Collaboration for Mission-Critical Work (VM) <https://azuremarketplace.microsoft.com/de-de/marketplace/apps/mattermost.mattermost-all-in-one?tab=overview>`_

    2. Select **Get it now** and sign in to your Azure account.

    3. Configure the deployment:
        - Choose your subscription
        - Create or select a resource group
        - Select a region
        - Choose a VM size (recommended: at least 2 vCPUs, 4GB RAM)
        - Configure network settings
        - Set up your admin credentials

    4. Review and create the deployment.

    5. Once deployed, access your Mattermost instance using the public IP address or DNS name provided.

    .. note::
        The Azure Marketplace image comes with PostgreSQL and is more suitable for testing production-like scenarios. Remember to delete the resources when you're done to avoid unnecessary charges.

.. tab:: Docker Preview Container

    The fastest way to try Mattermost is using the official Docker preview container. This method requires minimal setup and provides a fully functional Mattermost instance.

    **Prerequisites:**

    * Docker installed on your system
    * At least 1GB of available RAM
    * At least 1GB of available disk space

    **Steps to run Mattermost using Docker:**

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
* Review the :doc:`Application architecture </deploy/application-architecture>` to understand the system better
* Consider :doc:`Server deployment </deploy/server/server-deployment-planning>` for a production deployment

For additional help or questions, visit the `Mattermost community forums <https://forum.mattermost.com/>`_ or refer to the :doc:`Deployment troubleshooting </guides/deployment-troubleshooting>` guide. 