Deploy Mattermost
=================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Learn how to install, deploy, and scale Mattermost for teams and organizations of any size.

.. toctree::
    :maxdepth: 1
    :hidden:

    Prepare your Mattermost database </install/prepare-mattermost-database>
    Deploy on Ubuntu </install/install-ubuntu>
    Deploy using Docker </install/install-docker>
    Deploy with a tarball </install/install-tar>
    Deploy using Omnibus </install/installing-mattermost-omnibus>
    Deploy using Kubernetes </install/install-kubernetes>
    Deploy on Red Hat </install/install-rhel-8>

* :doc:`Prepare your Mattermost database </install/prepare-mattermost-database>` - Learn how to prepare and configure a database for Mattermost.
* :doc:`Deploy on Ubuntu </install/install-ubuntu>` - Signed packages direct from Mattermost featuring a single command for install and upgrades.
* `Deploy using Docker </install/install-docker.html#deploy-mattermost-on-docker-for-production-use>`__ - The fastest way to try Mattermost and a great single server installation option.
* :doc:`Deploy with a tarball </install/install-tar>` - Support for any Linux distribution.
* :doc:`Deploy using Omnibus </install/installing-mattermost-omnibus>` - An entire Mattermost installation on a single server.
* :doc:`Deploy using Kubernetes </install/install-kubernetes>` - Install using the Mattermost Helm Chart or Operator and simplified updates.
* :doc:`Deploy on Red Hat </install/install-rhel-8>` - Support for all current Red Hat Enterprise Linux platforms with a tarball.

.. tip::

  * See the `configuration settings </configure/configuration-settings.html>`__ documentation to learn more about customizing your production deployment.
  
  * Encountering issues with your deployment? See the `Deployment Troubleshooting </install/troubleshooting.html#deployment-troubleshooting>`__ or `high scale troubleshooting </deploy/high-scale-troubleshoot.html>`__ documentation for details.

Prepare for your Mattermost deployment
--------------------------------------

.. toctree::
    :maxdepth: 1
    :hidden:

    Software and hardware requirements </install/software-hardware-requirements>
    About the Mattermost Kubernetes Operator </install/mattermost-kubernetes-operator>
    Administrator tasks </getting-started/admin-onboarding-tasks>
    Architecture overview </getting-started/architecture-overview>
    Plan your Mattermost implementation </getting-started/implementation-plan>
    Enterprise roll out checklist </getting-started/enterprise-roll-out-checklist>
    Welcome email template </getting-started/welcome-email-to-end-users>

These guides will help you prepare for your Mattermost deployment.

* :doc:`Software and hardware requirements </install/software-hardware-requirements>` - Confirm software and hardware requirements for your Mattermost deployment.
* :doc:`About the Mattermost Kubernetes Operator </install/mattermost-kubernetes-operator>` - Learn more about the Mattermost Kubernetes Operator.
* :doc:`Administrator tasks </getting-started/admin-onboarding-tasks>` - Learn about the standard configurations and settings you’ll encounter.
* :doc:`Architecture overview </getting-started/architecture-overview>` - Learn the basics of user authentication, notifications, data management services, network connectivity, and high availability.
* :doc:`Plan your Mattermost implementation </getting-started/implementation-plan>` - Get a detailed breakdown of the technical requirements to deploy Mattermost for your team or organization.
* :doc:`Enterprise roll out checklist </getting-started/enterprise-roll-out-checklist>` - Learn how to roll Mattermost out to thousands of users.
* :doc:`Welcome email template </getting-started/welcome-email-to-end-users>` - Use our sample email template when you’re ready to invite users to your server.

Deployment guides
------------------

These deployment guides are for administrators who are ready to integrate Mattermost with their organization’s IT infrastructure. 

Server deployment
^^^^^^^^^^^^^^^^^
.. toctree::
    :titlesonly:
    :hidden:

    Deployment overview </deploy/deployment-overview>
    Set up a socket-based Mattermost database </install/setting-up-socket-based-mattermost-database>
    Image proxy </deploy/image-proxy>
    Backup and disaster recovery </deploy/backup-disaster-recovery>
    Encryption options </deploy/encryption-options>
    Configure transport encryption </install/transport-encryption>
    Bleve search </deploy/bleve-search>

* :doc:`Deployment overview </deploy/deployment-overview>` - Learn the basics of the Mattermost user experience, communication protocols, network access, data storage, and deployment options.
* :doc:`Set up a socket-based Mattermost database </install/setting-up-socket-based-mattermost-database>` - Connect your Mattermost server to your database service.
* :doc:`Image proxy </deploy/image-proxy>` - Setup and configure an image proxy to make loading images faster and more reliable and prevent pixel tracking.
* :doc:`Backup and disaster recovery </deploy/backup-disaster-recovery>` - Implement data backups, disaster recovery, and high availability deployment.
* :doc:`Encryption options </deploy/encryption-options>` - Setup encryption for data in transit and at rest.
* :doc:`Configure transport encryption </install/transport-encryption>` - Use transport encryption between Mattermost clusters and your proxy and database.
* :doc:`Bleve search </deploy/bleve-search>` - Use the Bleve search engine to provide Lucene-style full-text search.

Desktop and Mobile App deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. toctree::
    :maxdepth: 1
    :hidden:

    Desktop app deployment guide </deploy/desktop-app>
    Desktop MSI installer and group policy installation guides (beta) </install/desktop-msi-installer-and-group-policy-install>
    Desktop App custom dictionaries </install/desktop-custom-dictionaries>
    Desktop managed resources </install/desktop-app-managed-resources>
    Using Mattermost’s pre-built mobile apps </deploy/use-prebuilt-mobile-apps>
    Testing push notifications </deploy/mobile-testing-notifications>
    Deploy Mattermost mobile apps </deploy/mobile-overview>
    Mobile push notifications </deploy/mobile-hpns>
    Building and distributing your own custom Mattermost mobile apps </deploy/build-custom-mobile-apps>
    Deploying mobile apps using an EMM provider </deploy/deploy-mobile-apps-using-emm-provider>
    AppConfig for EMM solutions with Mattermost Mobile Apps </deploy/mobile-appconfig> 
    Mobile VPN options </deploy/consider-mobile-vpn-options>
    Mobile apps FAQ </deploy/mobile-faq>
    Client-side data storage FAQ </deploy/client-side-data>

Customize the Mattermost desktop and mobile apps to meet any deployment needs.

**Desktop Apps**

* :doc:`Desktop app deployment guide </deploy/desktop-app>` - Customize and distribute the Mattermost desktop app with pre-configured settings.
* :doc:`Desktop MSI installer and group policy installation guides (beta) </install/desktop-msi-installer-and-group-policy-install>` - Use the Mattermost MSI installer and Group Policy definitions for Windows deployment.
* :doc:`Desktop app custom dictionaries </install/desktop-custom-dictionaries>` - Create custom dictionaries for Mattermost spellcheck.
* :doc:`Desktop managed resources </install/desktop-app-managed-resources>` - Configure resource management for services running on the same domain as your Mattermost instance.

**Mobile Apps**

* :doc:`Using Mattermost’s pre-built mobile apps </deploy/use-prebuilt-mobile-apps>` - Connect users to your Mattermost server with our prebuilt apps for Android and iOS.
* :doc:`Testing push notifications </deploy/mobile-testing-notifications>` - Learn how to test mobile push notifications.
* :doc:`Deploy Mattermost mobile apps </deploy/mobile-overview>` - Learn the basics of how to customize and deploy Mattermost to the Enterprise.
* :doc:`Mobile push notifications </deploy/mobile-hpns>` - Set up mobile push notifications. 
* :doc:`Building and distributing your own custom Mattermost mobile apps </deploy/build-custom-mobile-apps>` - Build custom mobile Mattermost apps.
* :doc:`Deploying mobile apps using an EMM provider </deploy/deploy-mobile-apps-using-emm-provider>` - Deploy with Enterprise Mobile Management software to enforce security policies and enforce specific versions of the Mattermost mobile apps.
* :doc:`AppConfig for EMM solutions with Mattermost mobile apps </deploy/mobile-appconfig>` - Learn how AppConfig provides an easy way to configure enterprise mobile applications.
* :doc:`Mobile VPN options </deploy/consider-mobile-vpn-options>` - Learn how to use the Mattermost mobile apps with Mobile VPNs.
* :doc:`Mobile apps frequently asked questions </deploy/mobile-faq>`
* :doc:`Client-side data storage frequently asked questions </deploy/client-side-data>`

Upgrade Mattermost
------------------
.. toctree::
    :maxdepth: 1
    :hidden:

    Prepare to upgrade Mattermost </upgrade/prepare-to-upgrade-mattermost>
    Upgrade Mattermost Server </upgrade/upgrading-mattermost-server>
    Enterprise install and upgrade </install/enterprise-install-upgrade>
    Install a license key </upgrade/installing-license-key>
    Release definitions </upgrade/release-definitions>
    Important upgrade notes </upgrade/important-upgrade-notes>
    Release lifecycle </upgrade/release-lifecycle>
    Extended Support Release </upgrade/extended-support-release>
    Downgrade Mattermost Server </upgrade/downgrading-mattermost-server>
    Version archive </upgrade/version-archive>

Stay up to date with the latest features and improvements.

* :doc:`Prepare to upgrade Mattermost </upgrade/prepare-to-upgrade-mattermost>` - Learn how to prepare for a Mattermost upgrade.
* :doc:`Upgrade Mattermost Server </upgrade/upgrading-mattermost-server>` - Learn the basics of upgrading your Mattermost server to the latest version.
* :doc:`Enterprise install and upgrade </install/enterprise-install-upgrade>` - Learn how to upgrade your Mattermost server to premium versions.
* :doc:`Install a license key </upgrade/installing-license-key>` - Learn how to add or change a Mattermost license key.
* :doc:`Release definitions </upgrade/release-definitions>` - Get details on the Mattermost release schedule and the types of releases.
* :doc:`Important upgrade notes </upgrade/important-upgrade-notes>` - Find version-specific upgrade considerations.
* :doc:`Release lifecycle </upgrade/release-lifecycle>` - See critical release lifecycle dates.
* :doc:`Extended Support Release </upgrade/extended-support-release>` - Get information about releases that have extended release support.
* :doc:`Downgrade Mattermost Server </upgrade/downgrading-mattermost-server>` - Find out how to roll back to older versions of Mattermost.
* :doc:`Version archive </upgrade/version-archive>` - Download binaries for every release.

Scale Mattermost
----------------
.. toctree::
    :maxdepth: 1
    :hidden:

    Scale for Enterprise </scale/scaling-for-enterprise>
    High availability cluster </scale/high-availability-cluster>
    Elasticsearch </scale/elasticsearch>
    Performance monitoring </scale/performance-monitoring>
    Mattermost performance alerting guide </scale/performance-alerting>

Scale and monitor your Mattermost deployment.

* :doc:`Scale for Enterprise </scale/scaling-for-enterprise>` - Scale Mattermost to tens of thousands of users and beyond.
* :doc:`High availability cluster </scale/high-availability-cluster>` - Maintain Mattermost service during outages and hardware failures with redundant infrastructure.
* :doc:`Elasticsearch </scale/elasticsearch>` - Enhance search performance with Elasticsearch.
* :doc:`Performance monitoring </scale/performance-monitoring>` - Use Prometheus and Grafana to monitor the health and performance of your Mattermost cluster.
* :doc:`Mattermost performance alerting guide </scale/performance-alerting>` - Learn strategies and best practices for monitoring your Mattermost cluster. 

Troubleshooting guides
----------------------
.. toctree::
    :maxdepth: 1
    :hidden:

    General troubleshooting </install/troubleshooting>
    Troubleshooting your high scale deployment </deploy/high-scale-troubleshoot> 
    Troubleshooting mobile applications </deploy/mobile-troubleshoot>
    PostgreSQL installation troubleshooting </install/trouble-postgres>
    MySQL installation troubleshooting </install/trouble_mysql>

* :doc:`General deployment troubleshooting </install/troubleshooting>`
* :doc:`High scale troubleshooting </deploy/high-scale-troubleshoot>`
* :doc:`Mobile applications troubleshooting </deploy/mobile-troubleshoot>`
* :doc:`PostgreSQL installation troubleshooting </install/trouble-postgres>`
* :doc:`MySQL installation troubleshooting </install/trouble_mysql>`

Changelogs
----------
.. toctree::
    :maxdepth: 1
    :hidden:

    Mattermost self-hosted </install/self-managed-changelog>
    Mattermost legacy self-hosted </install/legacy-self-hosted-changelog>
    Mattermost Cloud </install/cloud-changelog>
    Mobile apps </deploy/mobile-app-changelog>
    Desktop apps </install/desktop-app-changelog>
    Deprecated features </install/deprecated-features>

* :doc:`Mattermost self-hosted </install/self-managed-changelog>`
* :doc:`Mattermost legacy self-hosted </install/legacy-self-hosted-changelog>`
* :doc:`Mattermost Cloud </install/cloud-changelog>`
* :doc:`Mobile apps </deploy/mobile-app-changelog>`
* :doc:`Desktop apps </install/desktop-app-changelog>`
* :doc:`Deprecated features </install/deprecated-features>`

Additional server install guides
--------------------------------
.. toctree::
    :maxdepth: 1
    :hidden:

    Deploy Mattermost on Bitnami </install/deploying-team-edition-on-bitnami>
    AWS Elastic Beanstalk Docker setup </install/setting-up-aws-elastic-beanstalk-docker>
    Install Mattermost Team Edition in GitLab Helm Chart </install/installing-team-edition-helm-chart>
    Open source components </upgrade/open-source-components>

* :doc:`Deploy Mattermost on Bitnami </install/deploying-team-edition-on-bitnami>`
* :doc:`AWS Elastic Beanstalk Docker setup </install/setting-up-aws-elastic-beanstalk-docker>`
* :doc:`Install on GitLab Helm Chart </install/installing-team-edition-helm-chart>`
* :doc:`Open source components </upgrade/open-source-components>`
