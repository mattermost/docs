Launch Mattermost at your organization
======================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Launching Mattermost at your organization involves the following steps:

- :doc:`Deploy Mattermost </guides/deployment>`
- :doc:`Install a database </deploy/install-database>`
- :doc:`Install a proxy server </deploy/install-nginx-server>`
- :doc:`Set up and customize the Mattermost server </guides/configure-mattermost-server>`

.. note::

   See our :doc:`software and hardware requirements </install/software-hardware-requirements>` documentation for details on the minimum requirements to launch Mattermost.

.. toctree::
   :maxdepth: 1
   :hidden:

      Deploy Mattermost </guides/deployment>
      Install a database </deploy/install-database>
      Use sockets for the database </install/setting-up-socket-based-mattermost-database>
      Install a proxy server </deploy/install-nginx-server>
      Software and hardware requirements </install/software-hardware-requirements>
      Configure Mattermost server </guides/configure-mattermost-server>
      Components of a Mattermost deployment </deploy/deployment-overview>
      Mattermost architecture </getting-started/architecture-overview>
      Administrator onboarding tasks </getting-started/admin-onboarding-tasks>
      Implementation plan </getting-started/implementation-plan>
      Enterprise roll out checklist </getting-started/enterprise-roll-out-checklist>
      Preview Mattermost using Docker </install/common-local-deploy-docker>
      Preview Mattermost using AWS Elastic Beanstalk Docker </install/setting-up-aws-elastic-beanstalk-docker>

See the following resources to plan your Mattermost launch:

* **Components of a Mattermost deployment** - Learn about the :doc:`components of a Mattermost deployment </deploy/deployment-overview>`, including communication protocols, network access, data storage, and deployment options.
* **Mattermost architecture** - Get an :doc:`overview of Mattermost architecture </getting-started/architecture-overview>` including the basics of user authentication, notifications, data management services, network connectivity, and high availability.
* **Administrator onboarding tasks** - Learn about the standard configurations and settings you’ll encounter :doc:`onboarding new users </getting-started/admin-onboarding-tasks>`.
* **Implementation plan** - See a detailed technical :doc:`implementation plan </getting-started/implementation-plan>` breakdown to deploy Mattermost for your team or organization.
* **Rollout checklist for enterprise deployments** - Learn how to :doc:`roll out Mattermost </getting-started/enterprise-roll-out-checklist>` to thousands of users.
* **Preview Mattermost** - Learn how to :doc:`install Mattermost server in a preview mode using Docker </install/common-local-deploy-docker>` or using :doc:`AWS Elastic Beanstalk Docker </install/setting-up-aws-elastic-beanstalk-docker>` to explore product functionality on a single local machine. Not recommended for production environments.