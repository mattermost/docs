.. Mattermost documentation master file, created by
   sphinx-quickstart on Thu Nov 19 13:21:53 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Mattermost Overview
-------------------
Mattermost is modern communication behind your firewall.

The platform lets users share messages and files across PCs, phones and tablets with continuous archiving and instant search, and supports notifications and integrations with your existing tools.

**Mattermost Team Edition** is an open source, self-hosted alternative to propretiary SaaS messaging. Mattermost brings all your team communication into one place, making it searchable and accessible anywhere. Deploys as single Linux binary on MySQL or PostgreSQL under an MIT license from `mattermost.org/download`_.

**Mattermost Enterprise Edition** is a commercial enteprise messaging solution offering advanced features including integration with corporate directories, compliance and auditing support, and sophisticated configurations for horizontal and multi-region scaling. More information is available by `contacting Mattermost, Inc.`_

This site offers documentation on User Help, Installation, Deployment, Administration, Development and Integrations.

-----

.. _`mattermost.org/download`: http://www.mattermost.org/download/
.. _contacting Mattermost, Inc.: https://about.mattermost.com/contact/
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
   help/getting-started/*

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

.. toctree::
   :maxdepth: 1
   :caption: Install Guides
   :glob:

   install/requirements*
   install/docker*
   install/prod*
   install/smtp*
   install/troubleshooting*
   install/i18n*

.. toctree::
   :maxdepth: 1
   :caption: Deployment
   :glob:

   deployment/sso*
   deployment/deployment*
   deployment/*

.. toctree::
   :maxdepth: 1
   :caption: Administration
   :glob:

   administration/overview*
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
   developer/*

.. toctree::
   :maxdepth: 1
   :caption: Development Process
   :glob:

   process/release-process*
   process/*

.. toctree::
   :maxdepth: 1
   :caption: Integrations
   :glob:

   integrations/*


