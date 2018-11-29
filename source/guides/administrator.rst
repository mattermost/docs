Administrator's Guide
=====================

In-depth documentation on installation, deployment and administration of Mattermost system.

Getting Started
---------------------

.. toctree::
   :maxdepth: 2
   :glob:

   /getting-started/implementation_plan.rst
   /getting-started/welcome_email.rst


Installing Mattermost
---------------------

.. toctree::
   :maxdepth: 1
   :glob:

   /install/requirements.rst
   Installing on Ubuntu 14.04 LTS </install/install-ubuntu-1404.rst>
   Installing on Ubuntu 16.04 LTS </install/install-ubuntu-1604.rst>
   Installing on Ubuntu 18.04 LTS </install/install-ubuntu-1804.rst>
   Installing on Debian Jessie </install/install-debian-88.rst>
   Installing on RHEL 6.6 </install/install-rhel-66.rst>
   Installing on RHEL 7.1 </install/install-rhel-71.rst>
   Installing on CentOS, Oracle Linux, and Scientific Linux </install/install-centos-oracle-scientific.rst>
   /install/ee-install*
   /install/deploy-bitnami*
   /install/docker-local*
   /install/prod-docker*
   /install/docker-ebs*
   /install/deploy-cloudron*
   /install/troubleshooting*
   /install/desktop*
   /install/smtp*
   /install/config-cloudfront*
   /install/i18n*
   /install/config-apache2.rst

Deployment
----------

.. toctree::
   :maxdepth: 2
   :glob:

   /deployment/on-boarding*
   /deployment/bulk-loading.rst
   /administration/migrating.md
   /administration/hipchat-migration-guidelines*
   /administration/bulk-export.rst
   /deployment/desktop-app-deployment*
   AppConfig for EMM Solutions </deployment/mobile-appconfig.rst>
   /administration/encryption*
   /administration/image-proxy*
   /deployment/customize-mattermost.rst

Upgrading Mattermost
----------------------------

.. toctree::
   :maxdepth: 2
   :glob:
   
   /administration/upgrade.rst
   /administration/important-upgrade-notes*   
   /administration/downgrade.rst
   /administration/changelog*
   /administration/version-archive*
   /administration/extended-support-release*

Administration
----------------------------

.. toctree::
   :maxdepth: 2
   :glob:

   /administration/command*
   /administration/config*
   /deployment/client-side-data.rst
   /administration/team-settings.md
   /administration/statistics.md
   /administration/migration-announcement-email-template*
   /administration/backup*
   /administration/liveness-check*
   /administration/plugins*
   /administration/announcement-banner.rst
   /administration/branding*
   
Mobile Apps
-----------

.. toctree::
   :maxdepth: 2
   :glob:

   /mobile/mobile-overview.rst
   /mobile/mobile-appconfig.rst
   /mobile/mobile-hpns.rst
   /mobile/mobile-faq.rst
   /mobile/mobile-troubleshoot.rst

User Provisioning
----------------------------

.. toctree::
   :maxdepth: 2
   :glob:
   
   /deployment/sso-ldap*
   /deployment/auth*
   /deployment/sso-saml.rst
   /deployment/sso-gitlab*
   /deployment/sso-google*
   /deployment/sso-office*
   /deployment/ssl-client-certificate*
   /deployment/certificate-based-authentication*
   
Access Control
----------------------------

.. toctree::
   :maxdepth: 2
   :glob:
   
   /deployment/advanced*
   /deployment/permissions-backend*

Scale
----------------------------

.. toctree::
   :maxdepth: 2
   :glob:
   
   /deployment/scaling*
   /deployment/cluster*
   /deployment/elastic*
   /deployment/metrics*
   /administration/performance-alerting-guide*

Compliance
----------------------------

.. toctree::
   :maxdepth: 2
   :glob:
   
   /administration/compliance*
   /administration/compliance-export*
   /administration/data-retention*
   /administration/custom-terms-of-service*
   
Unofficial Enhancements
-----------------------

Documentation on early previews and unofficial functionality.

.. toctree::
   :maxdepth: 1
   :glob:

   /install/prod-windows-2012*
   /deployment/webrtc*
   /developer/toolkit*
