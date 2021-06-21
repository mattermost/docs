Install, Deploy, Upgrade, and Scale Mattermost
==============================================

Install, host, and grow with Mattermost.

Before You Begin
----------------

.. toctree::
   :maxdepth: 1

   /overview/architecture.rst
   /help/getting-started/light-install.rst
   /getting-started/enterprise-roll-out-checklist.rst
   /deployment/on-boarding.rst
   /getting-started/implementation_plan.rst
   /getting-started/welcome_email.rst

Install Mattermost
------------------

Mattermost Server
^^^^^^^^^^^^^^^^^
   
.. toctree::
   :maxdepth: 1
    
   /install/requirements.rst
   Installing on Ubuntu 20.04 LTS </install/install-ubuntu-2004.rst>
   Installing on Ubuntu 18.04 LTS </install/install-ubuntu-1804.rst>
   Installing Mattermost Omnibus </install/mattermost-omnibus.rst>
   Installing on Kubernetes </install/install-kubernetes.rst>
   Installing on Debian Buster </install/install-debian.rst>
   Installing on RHEL 7 </install/install-rhel-7.rst>
   Installing on RHEL 8 </install/install-rhel-8.rst>
   Installing on CentOS, Oracle Linux, and Scientific Linux </install/install-centos-oracle-scientific.rst>
   Instructions On Setting Up a Socket-based Mattermost Database </install/sockets-db.rst>
   /install/ee-install.rst
   /install/transport-encryption/config.rst
   /install/deploy-bitnami.rst
   /install/docker-local-machine.rst
   /install/docker-ebs.rst
   Installing Mattermost Team Edition in GitLab Helm Chart </install/install-mmte-helm-gitlab-helm.rst>
   /administration/changelog.md

Desktop App
^^^^^^^^^^^

.. toctree::
   :maxdepth: 3

   /help/getting-started/install-desktop-app.rst
   /install/desktop.rst
   /install/desktop-managed-resources.rst
   /install/desktop-msi-gpo.rst
   /help/apps/desktop-changelog.rst

Mobile App
^^^^^^^^^^

.. toctree::
   :maxdepth: 3

   /help/getting-started/install-ios-app.rst
   /help/getting-started/install-android-app.rst
   /administration/mobile-changelog.md 

Deploy Mattermost
-----------------

Mattermost Server
^^^^^^^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   /deployment/deployment.md
   /administration/image-proxy.rst
   /administration/encryption.rst
   /administration/backup.rst
   /deployment/bleve.rst

Desktop App
^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   /deployment/desktop-app-deployment.rst

Mobile Apps
^^^^^^^^^^^

.. toctree::
   :maxdepth: 1

   /mobile/mobile-overview.rst
   /mobile/mobile-appconfig.rst
   /mobile/mobile-hpns.rst
   /mobile/mobile-faq.rst
   /mobile/mobile-troubleshoot.rst
   /deployment/client-side-data.rst

Upgrade Mattermost
------------------

.. toctree::
   :maxdepth: 1

   /administration/upgrade.rst
   /administration/important-upgrade-notes.rst
   /administration/version-archive.rst
   /administration/extended-support-release.rst
   /administration//release-lifecycle.rst
   /administration/downgrade.rst
   /administration/open-source-components.rst
   /administration/release-definitions.rst

Scale Mattermost
----------------
   
.. toctree::
   :maxdepth: 1

   /deployment/scaling.rst
   /deployment/cluster.rst
   /deployment/elasticsearch.rst
   /deployment/metrics.rst
   /administration/performance-alerting-guide.rst
