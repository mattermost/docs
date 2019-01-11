Administrator's Guide
=====================

In-depth documentation on installation, deployment and administration of Mattermost system.

Getting Started
---------------------

Use the following materials as a template to help you plan and document the implementation of Mattermost at your organization. 

.. toctree::
   :maxdepth: 2
   :glob:

   /getting-started/implementation_plan.rst
   /getting-started/welcome_email.rst

Installing Mattermost
---------------------

Learn how to get Mattermost running on your environment.

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
   Installing Mattermost Team Edition in GitLab Helm Chart </install/install-mmte-helm-gitlab-helm.rst>
   /install/troubleshooting*
   /install/desktop*
   /install/smtp*
   /install/config-cloudfront*
   /install/outbound-proxy.rst
   /install/i18n*
   /install/config-apache2.rst

Deployment
-----------------

Learn how to host Mattermost to meet your networking requirements.

.. toctree::
   :maxdepth: 2
   :glob:

   /deployment/deployment.md 
   /deployment/desktop-app-deployment*
   AppConfig for EMM Solutions </deployment/mobile-appconfig.rst>
   /administration/image-proxy*
   /administration/encryption*  
   /deployment/client-side-data.rst
   /administration/backup*

Configure Mattermost
---------------------

Learn how to configure settings to meet your unique requirements.

.. toctree::
   :maxdepth: 2
   :glob:

   /deployment/on-boarding.rst  
   /administration/config-settings.rst
   /deployment/customize-mattermost.rst 
   /administration/branding.rst

Mobile Apps
------------------

Learn how to configure and administer Mattermost apps.

.. toctree::
   :maxdepth: 2
   :glob:

   /mobile/mobile-overview.rst
   /mobile/mobile-appconfig.rst
   /mobile/mobile-hpns.rst
   /mobile/mobile-faq.rst
   /mobile/mobile-troubleshoot.rst

Onboard Users
--------------

Learn how to get your users into and comfortable using Mattermost.

.. toctree::
   :maxdepth: 2
   :glob:

   /deployment/bulk-loading.rst
   /administration/migrating.md
   /administration/hipchat-migration-guidelines*
   /administration/migration-announcement-email-template*
   /administration/user-provisioning*
   /deployment/sso-ldap*
   /deployment/auth*
   /deployment/ldap-group-sync.rst
   /deployment/sso-saml.rst
   /deployment/sso-gitlab*
   /deployment/sso-google*
   /deployment/sso-office*
   /deployment/ssl-client-certificate*
   /deployment/certificate-based-authentication*
   /deployment/advanced*
   /deployment/permissions-backend*

Administration
----------------------------

Learn how to maintain your Mattermost system.

.. toctree::
   :maxdepth: 2
   :glob:

   /administration/command*
   /administration/team-settings.md
   /administration/statistics.md
   /administration/liveness-check*
   /administration/announcement-banner.rst
   /administration/bulk-export.rst
 
Upgrade Mattermost
----------------------------

Learn how to keep Mattermost current with fixes and new features.

.. toctree::
   :maxdepth: 2
   :glob:
   
   /administration/upgrade.rst
   /administration/important-upgrade-notes*   
   /administration/changelog*
   /administration/version-archive*
   /administration/extended-support-release*  
   /administration/downgrade.rst

Mattermost Integrations
----------------------------

Learn how to extend Mattermost by integrating your workflows.

.. toctree::
   :maxdepth: 2
   :glob:

   /administration/plugins*

Mattermost Compliance
----------------------------

Learn how to adhere to your security and regulations.

.. toctree::
   :maxdepth: 2
   :glob:

   /administration/ediscovery*
   /administration/compliance*
   /administration/compliance-export*
   /administration/data-retention*
   /administration/custom-terms-of-service*

Scaling Mattermost
------------------

Learn how to support growth within Mattermost.

.. toctree::
   :maxdepth: 2
   :glob:
   
   /deployment/scaling*
   /deployment/cluster*
   /deployment/elastic*
   /deployment/metrics*
   /administration/performance-alerting-guide*

Unofficial Enhancements
-----------------------

Documentation on early previews and unofficial functionality.

.. toctree::
   :maxdepth: 1
   :glob:

   /install/prod-windows-2012*
   /developer/toolkit*
   /deployment/video-and-audio-calling*
