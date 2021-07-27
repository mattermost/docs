Install, Deploy, Upgrade, and Scale Mattermost
==============================================

Install, host, and grow with Mattermost.

Getting Started
---------------

.. toctree::
   :maxdepth: 1

   /getting-started/architecture-overview.rst
   /getting-started/light-install.rst
   /getting-started/enterprise-roll-out-checklist.rst
   /getting-started/admin-onboarding-tasks.rst
   /getting-started/implementation-plan.rst
   /getting-started/welcome-email-to-end-users.rst

Install Mattermost
------------------

Mattermost Server
^^^^^^^^^^^^^^^^^
   
.. toctree::
   :maxdepth: 1
    
   /install/software-hardware-requirements.rst
   Installing on Ubuntu 20.04 LTS </install/installing-ubuntu-2004-LTS.rst>
   Installing on Ubuntu 18.04 LTS </install/installing-ubuntu-1804-LTS.rst>
   Installing Mattermost Omnibus </install/installing-mattermost-omnibus.rst>
   Installing on Kubernetes </install/install-kubernetes.rst>
   Installing on Debian Buster </install/install-debian.rst>
   Installing on RHEL 8 </install/install-rhel-8.rst>
   Installing on RHEL 7 </install/install-rhel-7.rst>
   Installing on CentOS, Oracle Linux, and Scientific Linux </install/install-centos-oracle-scientific.rst>
   Instructions On Setting Up a Socket-based Mattermost Database </install/setting-up-socket-based-mattermost-database.rst>
   /install/trouble_mysql.rst
   /install/enterprise-install-upgrade.rst
   /install/transport-encryption.rst
   /install/proxy-to-mattermost-transport-encryption.rst
   /install/database-transport-encryption.rst
   /install/cluster-transport-encryption.rst
   /install/deploying-team-edition-on-bitnami.rst
   /install/setting-up-local-machine-using-docker.rst
   /install/setting-up-aws-elastic-beanstalk-docker.rst
   Installing Mattermost Team Edition in GitLab Helm Chart </install/installing-team-edition-helm-chart.rst>
   /install/troubleshooting.rst
   /install/self-managed-changelog.md
   /install/cloud-changelog.md


Desktop App
^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   /install/installing-mattermost-desktop-app.rst
   /install/desktop-app-install.rst
   /install/desktop-app-managed-resources.rst
   /install/desktop-msi-installer-and-group-policy-install.rst
   /install/desktop-app-changelog.rst

Mobile App
^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   /install/install-ios-app.rst
   /install/install-android-app.rst
   /deploy/mobile-app-changelog.md 

Deploy Mattermost
-----------------

Mattermost Server
^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   /deploy/deployment-overview.md
   /deploy/image-proxy.rst
   /deploy/encryption-options.rst
   /deploy/backup-disaster-recovery.rst
   /deploy/bleve-search.rst

Desktop App
^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   /deploy/desktop-app.rst

Mobile Apps
^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   /deploy/mobile-overview.rst
   /deploy/use-prebuilt-mobile-apps.rst
   /deploy/build-custom-mobile-apps.rst
   /deploy/deploy-mobile-apps-using-emm-provider.rst
   /deploy/mobile-appconfig.rst
   /deploy/consider-mobile-vpn-options.rst
   /deploy/mobile-hpns.rst
   /deploy/mobile-faq.rst
   /deploy/mobile-troubleshoot.rst
   /deploy/client-side-data.rst

Upgrade Mattermost
------------------

.. toctree::
   :maxdepth: 1

   /upgrade/upgrading-mattermost-server.rst
   /upgrade/important-upgrade-notes.rst
   /upgrade/version-archive.rst
   /upgrade/extended-support-release.rst
   /upgrade//release-lifecycle.rst
   /upgrade/downgrading-mattermost-server.rst
   /upgrade/open-source-components.rst
   /upgrade/release-definitions.rst

Scale Mattermost
----------------
   
.. toctree::
   :maxdepth: 1

   /scale/scaling-for-enterprise.rst
   /scale/high-availability-cluster.rst
   /scale/elasticsearch.rst
   /scale/performance-monitoring.rst
   /scale/peformance-alerting.rst
