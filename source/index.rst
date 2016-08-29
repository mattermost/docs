.. Mattermost documentation master file, created by
   sphinx-quickstart on Thu Nov 19 13:21:53 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Mattermost Documentation 
-------------------
Mattermost is modern communication behind your firewall.

-----

.. _`mattermost.org/download`: http://www.mattermost.org/download/
.. _contacting Mattermost, Inc.: https://about.mattermost.com/contact/
.. _download and try it today.: https://docs.mattermost.com/install/ee-install.html


.. toctree::
   :maxdepth: 1
   :caption: Overview
   :glob:

   administration/overview-tech*
   overview/security*
   deployment/deployment*
   integrations/overview*
   
.. toctree::
   :maxdepth: 1
   :caption: Install Guides
   :glob:

   install/requirements*
   install/docker-local*
   install/docker-ebs*
   install/prod*
   install/smtp*
   install/troubleshooting*
   install/ee-install*
   install/i18n*

.. toctree::
   :maxdepth: 1
   :caption: Deployment
   :glob:

   deployment/deployment*
   deployment/on-boarding*
   deployment/sso-gitlab*
   deployment/sso-google*
   deployment/sso-office*
   deployment/sso-ldap*
   deployment/sso-saml.md
   deployment/auth*
   deployment/push*
   deployment/scaling*
   deployment/cluster*


.. toctree::
   :maxdepth: 1
   :caption: Administration
   :glob:

   administration/overview*
   overview/security*
   administration/command*
   administration/config*
   administration/team-settings.md
   administration/statistics.md
   administration/upgrade.md
   administration/migrating.md
   administration/*

.. toctree::
   :maxdepth: 1
   :caption: Developer Guide
   :glob:

   developer/api*
   developer/web-service*
   developer/webhooks*
   developer/slash*
   developer/developer*
   developer/contribution*
   developer/fx*
   developer/style*
   developer/integration*
   developer/localization-process.rst
   developer/message-attachments*
   developer/running-mattermost*

.. toctree::
   :maxdepth: 1
   :caption: Team Handbook
   :glob:

   process/overview*
   process/release-process*
   process/*

.. toctree::
   :maxdepth: 1
   :caption: Integrations
   :glob:

   integrations/*

.. toctree::
   :maxdepth: 1
   :caption: Getting Started
   :glob:

   help/getting-started/signing-in.md
   help/getting-started/messaging-basics.md
   help/getting-started/configuring-notifications.md
   help/getting-started/organizing-conversations.md
   help/getting-started/searching.md
   help/getting-started/creating-teams.md
   help/getting-started/managing-members.md

.. toctree::
   :maxdepth: 1
   :caption: Messaging
   :glob:

   help/messaging/sending-messages.md
   help/messaging/reading-messages.md
   help/messaging/mentioning-teammates.md
   help/messaging/formatting-text.md
   help/messaging/attaching-files.md
   help/messaging/executing-commands.md
   help/messaging/*

.. toctree::
   :maxdepth: 1
   :caption: Settings
   :glob:

   help/settings/account-settings.md
   help/settings/theme-colors.md
   help/settings/channel-settings.md
   help/settings/team-settings.md
   help/settings/*
