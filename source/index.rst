.. Mattermost documentation master file, created by
   sphinx-quickstart on Thu Nov 19 13:21:53 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Mattermost Overview 
-------------------
Mattermost is modern communication behind your firewall. 

The platform lets users share messages and files across PCs, phones and tablets with continuous archiving and instant search, and supports notifications and integrations with your existing tools. 

**Mattermost Team Edition** is an open source, self-hosted application offering "All your team communication in one place, easy-to-use, searchable, and accessible anywhere". New releases available monthly under an MIT license from `mattermost.org/download`_.

**Mattermost Enterprise Edition** is a pre-released commercial version of Mattermost offering additional features for enterprise communication and compliance available by `contacting Mattermost, Inc.`_

This site offers documentation on User Help, Installation, Deployment, Administration, Development and Integrations.

-----

.. _`mattermost.org/download`: http://www.mattermost.org/download/
.. _contacting Mattermost, Inc.: https://about.mattermost.com/contact/
.. toctree::
   :maxdepth: 1
   :caption: Getting Started
   
   help/getting-started/signing-in.md
   help/getting-started/messaging-basics.md
   help/getting-started/configuring-notifications.md
   help/getting-started/organizing-conversations.md
   help/getting-started/searching.md
   help/getting-started/creating-teams.md
   
.. toctree::
   :maxdepth: 1
   :caption: Messaging
   
   help/messaging/sending-messages.md
   help/messaging/reading-messages.md
   help/messaging/mentioning-teammates.md
   help/messaging/formatting-text.md
   help/messaging/attaching-files.md
 
.. toctree::
   :maxdepth: 1
   :caption: Settings
   
   help/settings/account-settings.md
   help/settings/theme-colors.md
   help/settings/channel-settings.md
   
.. toctree::
   :maxdepth: 1
   :caption: Install Guides
   :glob:
   
   install/requirements*
   install/*
   
.. toctree::
   :maxdepth: 1
   :caption: Deployment 
   :glob:
   
   deployment/sso*
   deployment/*

.. toctree::
   :maxdepth: 1
   :caption: Administration
   :glob:
   
   administration/overview*
   administration/command*
   administration/config*
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
   developer/developer*
   developer/contribution*
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


