Deploy Mattermost
=================

Learn how to install, deploy, and scale Mattermost for teams and organizations of any size.

Get Started
-----------
.. toctree::
    :maxdepth: 1
    :hidden:

    Quick Install Guide </getting-started/light-install>
    Run Mattermost via Docker </install/setting-up-local-machine-using-docker>
    Administrator Tasks </getting-started/admin-onboarding-tasks>
    Architecture </getting-started/architecture-overview>
    Implement Mattermost </getting-started/implementation-plan>
    Enterprise Roll Out Checklist </getting-started/enterprise-roll-out-checklist>
    Welcome Email Template </getting-started/welcome-email-to-end-users>

These guides will get you up and running with Mattermost in minutes.

* :doc:`Quick Install Guide </getting-started/light-install>` - Deploy in minutes via Mattermost Omnibus on Ubuntu.
* :doc:`Run Mattermost via Docker </install/setting-up-local-machine-using-docker>` - Launch a Mattermost server instantly to test functionality and build integrations.
* :doc:`Administrator Tasks </getting-started/admin-onboarding-tasks>` - Learn about the standard configurations and settings you’ll encounter.
* :doc:`Architecture </getting-started/architecture-overview>` - Learn the basics of user authentication, notifications, data management services, network connectivity, and high availability.
* :doc:`Implement Mattermost </getting-started/implementation-plan>` - Get a detailed breakdown of the technical requirements to deploy Mattermost for your team or organization.
* :doc:`Enterprise Roll Out Checklist </getting-started/enterprise-roll-out-checklist>` - Learn how to roll Mattermost out to thousands of users.
* :doc:`Welcome Email Template </getting-started/welcome-email-to-end-users>` - Use our sample email template when you’re ready to invite users to your server.

Install Guides
--------------

The Mattermost server and client apps can run on all of the most popular platforms. Here’s a list of the most popular installation methods.

Server Installation
^^^^^^^^^^^^^^^^^^^
.. toctree::
    :maxdepth: 1
    :hidden:

    Software and Hardware Requirements </install/software-hardware-requirements>
    Local Docker Setup </install/setting-up-local-machine-using-docker>
    Mattermost Omnibus </install/installing-mattermost-omnibus>
    Ubuntu 20.04 LTS </install/installing-ubuntu-2004-LTS>
    Kubernetes </install/install-kubernetes>
    Helm </install/install-kubernetes.html#installing-the-operators-via-helm>
    Debian Buster </install/install-debian>
    RHEL 8 </install/install-rhel-8>
    CentOS, Oracle Linux, and Scientific Linux </install/install-centos-oracle-scientific>


* :doc:`Software and Hardware Requirements </install/software-hardware-requirements>`
* :doc:`Local Docker Setup </install/setting-up-local-machine-using-docker>`
* :doc:`Mattermost Omnibus </install/installing-mattermost-omnibus>`
* :doc:`Ubuntu 20.04 LTS </install/installing-ubuntu-2004-LTS>`
* :doc:`Kubernetes </install/install-kubernetes>`
* `Helm <https://docs.mattermost.com/install/install-kubernetes.html#installing-the-operators-via-helm>`__
* :doc:`Debian Buster </install/install-debian>`
* :doc:`RHEL 8 </install/install-rhel-8>`
* :doc:`CentOS, Oracle Linux, and Scientific Linux </install/install-centos-oracle-scientific>`
* `More server install guides <https://docs.mattermost.com/guides/deployment.html#other-resources>`__

Desktop/Mobile App Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. toctree::
    :maxdepth: 1
    :hidden:

    Install the Mattermost Desktop App </install/installing-mattermost-desktop-app>
    Desktop Application Install Guides </install/desktop-app-install>
    iOS Setup </install/install-ios-app>
    Android Setup </install/install-android-app>
    Testing Push Notifications </deploy/mobile-testing-notifications>

* :doc:`Install the Mattermost Desktop App </install/installing-mattermost-desktop-app>`
* :doc:`Desktop Application Install Guides </install/desktop-app-install>`
* :doc:`iOS Setup </install/install-ios-app>`
* :doc:`Android Setup </install/install-android-app>`
* :doc:`Testing Push Notifications </deploy/mobile-testing-notifications>`

Deployment Guide
----------------
The deployment guide is for administrators who are ready to integrate Mattermost with their organization’s IT infrastructure. 

Server Deployment
^^^^^^^^^^^^^^^^^
.. toctree::
    :titlesonly:
    :hidden:

    Deployment Overview </deploy/deployment-overview>
    Set Up a Socket-based Mattermost Database </install/setting-up-socket-based-mattermost-database>
    Image Proxy </deploy/image-proxy>
    Backup and Disaster Recovery </deploy/backup-disaster-recovery>
    Encryption Options </deploy/encryption-options>
    Configure Transport Encryption </install/transport-encryption>
    Bleve Search (Experimental) </deploy/bleve-search>

* :doc:`Deployment Overview </deploy/deployment-overview>` - Learn the basics of the Mattermost user experience, communication protocols, network access, data storage, and deployment options.
* :doc:`Set Up a Socket-based Mattermost Database </install/setting-up-socket-based-mattermost-database>` - Connect your Mattermost server to your database service.
* :doc:`Image Proxy </deploy/image-proxy>` - Setup and configure an image proxy to make loading images faster and more reliable and prevent pixel tracking.
* :doc:`Backup and Disaster Recovery </deploy/backup-disaster-recovery>` - Implement data backups, disaster recovery, and high availability deployment.
* :doc:`Encryption Options </deploy/encryption-options>` - Setup encryption for data in transit and at rest.
* :doc:`Configure Transport Encryption </install/transport-encryption>` - Use transport encryption between Mattermost clusters and your proxy and database.
* :doc:`Bleve Search (Experimental) </deploy/bleve-search>` - Use the Bleve search engine to provide Lucene-style full-text search.

Desktop & Mobile App Deployment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. toctree::
    :maxdepth: 1
    :hidden:

    Desktop App Deployment Guide </deploy/desktop-app>
    Desktop MSI Installer and Group Policy Installation Guides (Beta) </install/desktop-msi-installer-and-group-policy-install>
    Desktop App Custom Dictionaries </install/desktop-custom-dictionaries>
    Desktop Managed Resources </install/desktop-app-managed-resources>
    Using Mattermost’s Pre-Built Mobile Apps </deploy/use-prebuilt-mobile-apps>
    Deploy Mattermost Mobile Apps </deploy/mobile-overview>
    Mobile Push Notifications </deploy/mobile-hpns>
    Building and Distributing Your Own Custom Mattermost Mobile Apps </deploy/build-custom-mobile-apps>
    Deploying Mobile Apps Using an EMM Provider </deploy/deploy-mobile-apps-using-emm-provider>
    Mobile VPN Options </deploy/consider-mobile-vpn-options>
    Mobile Apps FAQ </deploy/mobile-faq>
    Client-side Data Storage FAQ </deploy/client-side-data>

Customize the Mattermost desktop and mobile apps to meet any deployment needs.

**Desktop Apps**

* :doc:`Desktop App Deployment Guide </deploy/desktop-app>` - Customize and distribute the Mattermost desktop app with pre-configured settings.
* :doc:`Desktop MSI Installer and Group Policy Installation Guides (Beta) </install/desktop-msi-installer-and-group-policy-install>` - Use the Mattermost MSI installer and Group Policy definitions for Windows deployment.
* :doc:`Desktop App Custom Dictionaries </install/desktop-custom-dictionaries>` - Create custom dictionaries for Mattermost spellcheck.
* :doc:`Desktop Managed Resources </install/desktop-app-managed-resources>` - Configure resource management for services running on the same domain as your Mattermost instance.

**Mobile Apps**

* :doc:`Using Mattermost’s Pre-Built Mobile Apps </deploy/use-prebuilt-mobile-apps>` - Connect users to your Mattermost server with our prebuilt apps for Android and iOS.
* :doc:`Deploy Mattermost Mobile Apps </deploy/mobile-overview>` - Learn the basics of how to customize and deploy Mattermost to the Enterprise.
* :doc:`Mobile Push Notifications </deploy/mobile-hpns>` - Set up mobile push notifications. 
* :doc:`Building and Distributing Your Own Custom Mattermost Mobile Apps </deploy/build-custom-mobile-apps>` - Build custom mobile Mattermost apps.
* :doc:`Deploying Mobile Apps Using an EMM Provider </deploy/deploy-mobile-apps-using-emm-provider>` - Deploy with Enterprise Mobile Management software to enforce security policies and enforce specific versions of the Mattermost mobile apps.
* :doc:`Mobile VPN Options </deploy/consider-mobile-vpn-options>` - Learn how to use the Mattermost mobile apps with Mobile VPNs.
* :doc:`Mobile Apps FAQ </deploy/mobile-faq>`
* :doc:`Client-side Data Storage FAQ </deploy/client-side-data>`

Upgrade Mattermost
------------------
.. toctree::
    :maxdepth: 1
    :hidden:

    Upgrade Mattermost Server </upgrade/upgrading-mattermost-server>
    Enterprise Install and Upgrade </install/enterprise-install-upgrade>
    Install a License Key </upgrade/installing-license-key>
    Release Definitions </upgrade/release-definitions>
    Important Upgrade Notes </upgrade/important-upgrade-notes>
    Release Lifecycle </upgrade/release-lifecycle>
    Extended Support Release </upgrade/extended-support-release>
    Downgrade Mattermost Server </upgrade/downgrading-mattermost-server>
    Version Archive </upgrade/version-archive>


Stay up to date with the latest features and improvements.

* :doc:`Upgrade Mattermost Server </upgrade/upgrading-mattermost-server>` - Learn the basics of upgrading your Mattermost server to the latest version.
* :doc:`Enterprise Install and Upgrade </install/enterprise-install-upgrade>` - Learn how to upgrade your Mattermost server to premium versions.
* :doc:`Install a License Key </upgrade/installing-license-key>` - Learn how to add or change a Mattermost license key.
* :doc:`Release Definitions </upgrade/release-definitions>` - Get details on the Mattermost release schedule and the types of releases.
* :doc:`Important Upgrade Notes </upgrade/important-upgrade-notes>` - Find version-specific upgrade considerations.
* :doc:`Release Lifecycle </upgrade/release-lifecycle>` - See critical release lifecycle dates.
* :doc:`Extended Support Release </upgrade/extended-support-release>` - Get information about releases that have extended release support.
* :doc:`Downgrade Mattermost Server </upgrade/downgrading-mattermost-server>` - Find out how to roll back to older versions of Mattermost.
* :doc:`Version Archive </upgrade/version-archive>` - Download binaries for every release.


Scale Mattermost
----------------
.. toctree::
    :maxdepth: 1
    :hidden:

    Scale for Enterprise </scale/scaling-for-enterprise>
    High Availability Cluster </scale/high-availability-cluster>
    Elasticsearch </scale/elasticsearch>
    Performance Monitoring </scale/performance-monitoring>
    Mattermost Performance Alerting Guide </scale/performance-alerting>

Scale and monitor your Mattermost deployment.

* :doc:`Scale for Enterprise </scale/scaling-for-enterprise>` - Scale Mattermost to tens of thousands of users and beyond.
* :doc:`High Availability Cluster </scale/high-availability-cluster>` - Maintain Mattermost service during outages and hardware failures with redundant infrastructure.
* :doc:`Elasticsearch </scale/elasticsearch>` - Enhance search performance with Elasticsearch.
* :doc:`Performance Monitoring </scale/performance-monitoring>` - Use Prometheus and Grafana to monitor the health and performance of your Mattermost cluster.
* :doc:`Mattermost Performance Alerting Guide </scale/performance-alerting>` - Learn strategies and best practices for monitoring your Mattermost cluster. 

Troubleshooting Guides
----------------------
.. toctree::
    :maxdepth: 1
    :hidden:

    General Troubleshooting </install/troubleshooting>
    Troubleshooting Mobile Applications </deploy/mobile-troubleshoot>
    MySQL Installation Troubleshooting </install/trouble_mysql>


* :doc:`General Troubleshooting </install/troubleshooting>`
* :doc:`Troubleshooting Mobile Applications </deploy/mobile-troubleshoot>`
* :doc:`MySQL Installation Troubleshooting </install/trouble_mysql>`

Changelogs
----------
.. toctree::
    :maxdepth: 1
    :hidden:

    Mattermost </install/self-managed-changelog>
    Mattermost Cloud </install/cloud-changelog>
    Mobile Apps </deploy/mobile-app-changelog>
    Desktop Apps </install/desktop-app-changelog>

* :doc:`Mattermost </install/self-managed-changelog>`
* :doc:`Mattermost Cloud </install/cloud-changelog>`
* :doc:`Mobile Apps </deploy/mobile-app-changelog>`
* :doc:`Desktop Apps </install/desktop-app-changelog>`

Other Resources
---------------
.. toctree::
    :maxdepth: 1
    :hidden:

    Install on Ubuntu 18.04 LTS </install/installing-ubuntu-1804-LTS>
    Install on RHEL 7 </install/install-rhel-7>
    Deploy Mattermost on Bitnami </install/deploying-team-edition-on-bitnami>
    AWS Elastic Beanstalk Docker Setup </install/setting-up-aws-elastic-beanstalk-docker>
    Install Mattermost Team Edition in GitLab Helm Chart </install/installing-team-edition-helm-chart>
    Open Source Components </upgrade/open-source-components>


* :doc:`Install on Ubuntu 18.04 LTS </install/installing-ubuntu-1804-LTS>`
* :doc:`Install on RHEL 7 </install/install-rhel-7>`
* :doc:`Deploy Mattermost on Bitnami </install/deploying-team-edition-on-bitnami>`
* :doc:`AWS Elastic Beanstalk Docker Setup </install/setting-up-aws-elastic-beanstalk-docker>`
* :doc:`Install on GitLab Helm Chart </install/installing-team-edition-helm-chart>`
* :doc:`Open Source Components </upgrade/open-source-components>`
