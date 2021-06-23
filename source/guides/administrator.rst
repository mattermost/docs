
Self-Managed Administrator's Guide
==================================

In-depth documentation on installation, deployment, and administration of Mattermost.

.. toctree::
   :maxdepth: 2
   :glob:
   
   /overview/architecture*
   /deployment/deployment*
      /deployment/enterprise-deployment-guide*
      /deployment/mobile-app-deployment*

Getting Started
----------------

Use the following materials as a template to help you plan and document the implementation of Mattermost at your organization.

.. toctree::
   :maxdepth: 2
   :glob:

   /help/getting-started/light-install.rst
   /getting-started/enterprise-roll-out-checklist.rst
   /deployment/on-boarding.rst
   /getting-started/implementation_plan.rst
   /getting-started/welcome_email.rst

Installing Mattermost
---------------------

Learn how to get Mattermost running on your environment.

.. toctree::
   :maxdepth: 1
   :glob:

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
   /install/ee-install*
   /install/transport-encryption/config.rst
   /install/deploy-bitnami*
   /install/docker-local*
   /install/docker-ebs*
   Installing Mattermost Team Edition in GitLab Helm Chart </install/install-mmte-helm-gitlab-helm.rst>
   /install/desktop*
   /install/desktop-managed-resources*
   /install/desktop-msi-gpo*
 
Deployment
-----------

Learn how to host Mattermost to meet your networking requirements.

.. toctree::
   :maxdepth: 2
   :glob:

   /deployment/deployment.md
   /deployment/desktop-app-deployment*
   /mobile/mobile-appconfig.rst
   /administration/image-proxy*
   /administration/encryption*
   /deployment/client-side-data.rst
   /administration/backup*
   /deployment/bleve*

Configure Mattermost
---------------------

Learn how to configure settings to meet your unique requirements.

.. toctree::
   :maxdepth: 2
   :glob:

   /administration/config-settings.rst
   /administration/config-in-database.rst
   /administration/prev-config-settings.rst
   /deployment/customize-mattermost.rst
   /deployment/customize-email.rst
   /administration/branding.rst
   /install/smtp*
   /install/config-cloudfront*
   /install/outbound-proxy.rst
   /install/i18n*
   /install/config-apache2.rst
   
Incident Collaboration
----------------------

.. toctree::
   :maxdepth: 1
   :glob:

   /administration/devops-command-center.rst

Mobile Apps
-----------

Learn how to configure and administer Mattermost apps.

.. toctree::
   :maxdepth: 2
   :glob:

   /mobile/mobile-overview.rst
   /mobile/use-prebuilt-mobile-apps.rst
   /mobile/build-custom-mobile-apps.rst
   /mobile/deploy-mobile-apps-using-emm-provider.rst
   /mobile/consider-mobile-vpn-options.rst
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
   /deployment/admin-roles*
   /deployment/sso-ldap.md
   /deployment/auth*
   /deployment/ldap-group-sync.rst
   /deployment/ldap-group-constrained-team-channel.rst
   /deployment/sso-saml.rst
   /deployment/sso-saml-technical*
   /deployment/sso-openidconnect.rst
   /deployment/sso-gitlab.rst
   /deployment/sso-google.rst
   /deployment/sso-office.rst
   /deployment/converting-oauth20-service-providers-to-openidconnect.rst
   /deployment/ssl-client-certificate*
   /deployment/certificate-based-authentication*
   /deployment/team-channel-management*
   /deployment/advanced*
   /deployment/permissions-backend*
   /deployment/guest-accounts*

Administration
--------------

Learn how to maintain your Mattermost system.

.. toctree::
   :maxdepth: 2
   :glob:

   /administration/command*
   /administration/mmctl-cli-tool.rst
   /administration/scripts*
   /administration/statistics.md
   /integrations/net-promoter-score*
   /administration/notices* 
   /administration/health-check*
   /administration/announcement-banner.rst
   /administration/bulk-export.rst
   /administration/generating-support-packet.rst

Troubleshooting
----------------

Understand potential issues and how to address them.

.. toctree::
   :maxdepth: 1
   :glob:

   /install/troubleshooting.rst
   /install/trouble_mysql.rst
 
Upgrade Mattermost
------------------

Learn how to keep Mattermost current with fixes and new features.

.. toctree::
   :maxdepth: 2
   :glob:
   
   /administration/upgrade.rst
   /administration/important-upgrade-notes*
   /administration/changelog*
   /help/apps/desktop-changelog*
   /administration/mobile-changelog*
   /administration/version-archive*
   /administration/extended-support-release*
   /administration/release-lifecycle*
   /administration/downgrade.rst
   /administration/open-source-components*
   /administration/release-definitions*

Mattermost Integrations
-----------------------

Learn how to extend Mattermost by integrating your workflows.

.. toctree::
   :maxdepth: 2
   :glob:

   /developer/toolkit*
   /deployment/atlassian-integrations*
   /deployment/microsoft-integrations*
   /deployment/ci-cd-tools*
   /deployment/incident-response-and-monitoring*
   /deployment/bots*
   /deployment/video-and-audio-calling*
   /deployment/productivity-tools*

Mattermost Compliance
---------------------

Learn how to adhere to your security and regulations.

.. toctree::
   :maxdepth: 2
   :glob:

   /administration/ediscovery*
   /administration/compliance*
   /administration/audit-log*
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

Community-Managed Documentation
-------------------------------

Documentation on early previews and unofficial functionality.

.. toctree::
   :maxdepth: 1
   :glob:

   /install/prod-windows-2012*
   /install/prod-docker*
   /install/deploy-cloudron*
   /administration/upgrade-script*
   /administration/light-install-hindi.rst
   
