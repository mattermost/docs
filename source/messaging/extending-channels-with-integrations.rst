Extending Channels with Integrations
====================================

Access settings for integrations from the **Product menu**. Select **Integrations** to open a page where you can view and configure incoming webhooks, outgoing webhooks, and slash commands for your team. If you can't see an **Integrations** option, then your System Admin may limit access to System Admins only.

`Visit our Marketplace <https://mattermost.com/marketplace/>`__ for dozens of open source integrations to common tools like Jira, Jenkins, GitLab, Trac, Redmine, and Bitbucket, along with interactive bot applications (Hubot, mattermost-bot), and other communication tools (Email, IRC, XMPP, Threema) that are freely available for use and customization.

Microsoft integrations
-----------------------

There are several ways to connect your Microsoft tools to Mattermost. Take a look at the tools recommended below, or visit our `Mattermost Marketplace <https://mattermost.com/marketplace/>`__ to find more.

Office 365 Calendar 
~~~~~~~~~~~~~~~~~~~

|enterprise| |professional| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The Microsoft Office 355 Calendar integration enables two-way integration between Mattermost and Office 365 Calendar, and was developed by Mattermost. This integration enables you to:

- Receive a daily summary of calendar events, and accept or decline new events.
- Reflect user status as "Do Not Disturb" when in a meeting scheduled via Outlook Calendar.

Visit the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__ to install, configure, and use this integration.

Skype for Business
~~~~~~~~~~~~~~~~~~

|all-plans| |cloud| |self-hosted|

The Skype for Business integration supports a vendor-hosted cloud solution, and enables you to:

- Start and join voice calls, video calls, and use screen-sharing with your team members. Developed by kosgrz and maintained by Mattermost.
- Select a video icon in a Mattermost channel to invite team members to join a Skype for Business call, hosted using the credentials of the user who initiated the call.

Visit the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__ to install, configure, and use this integration. See the `source code <https://github.com/mattermost/mattermost-plugin-skype4business>`__ for more information.

Office 365 SSO
~~~~~~~~~~~~~~

|enterprise| |professional| |cloud| |self-hosted|

The Office 365 SSO integration Supports Microsoft Active Directory Tenants for team creation, account creation, and Single Sign-On (SSO). This integration enables you to:

- Configure Mattermost to use your Office 365 credentials and Azure Active Directory account as a single sign-on (SSO) service, developed by Mattermost.
- Receive a daily summary of calendar events, and accept or decline new events.

Visit the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__ to install, configure, and use this integration.

CI/CD integrations
-------------------

There are several ways to connect your CI/CD tools to Mattermost. Take a look at the tools recommended below, or visit the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__ to find more.

GitHub 
~~~~~~

|all-plans| |cloud| |self-hosted|

The GitHub integration supports GitHub Enterprise, and works with Saas and Enterprise versions of GitHub. This integration enables two-way integration between Mattermost and GitHub, and was developed by Mattermost. This integration enables you to:

- Get reminders on issues and pull requests that need your attention.
- Get notifications in Mattermost about mentions, review requests, and comments.

Visit the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__ to install, configure, and use this integration. Please see the `source code <https://github.com/mattermost/mattermost-plugin-github>`__ for more information.

GitLab
~~~~~~

|all-plans| |cloud| |self-hosted|

The GitLab integration supports SaaS and on-prem versions of GitLab. This integration enables two-way integration between Mattermost and GitLab,  was developed by Romain Maneschi, and is supported by Mattermost. This integration enables you to:

- Get reminders on issues and merge requests that need your attention.
- Get notifications in Mattermost about mentions, review requests, and comments.

Visit the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__ to install, configure, and use this integration. Please see the `source code <https://github.com/mattermost/mattermost-plugin-gitlab>`__ for more information.

Atlassian integrations
-----------------------

There are several ways to connect Atlassian tools to Mattermost. Take a look at the tools recommended below, or visit the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__ to find more.

Confluence
~~~~~~~~~~

|all-plans| |cloud| |self-hosted|

The Confluence integration supports Confluence Cloud, Server, and Data Center platforms. This integration is an Atlassian Marketplace application for Confluence and Mattermost, and was developed by codefortynine. This integration enables you to:

- Send notifications about page, blogpost, question, or comment updates from your Confluence spaces to Mattermost channels.
- Configure notifications for a specific space, and also user notifications for tasks and mentions.

Download and review the documentation from the `Atlassian Marketplace <https://marketplace.atlassian.com/apps/1222417/mattermost-connector-for-confluence>`__.

Jira
~~~~

|all-plans| |cloud| |self-hosted|

The Jira integration supports Jira Core and Jira Software products for Cloud, Server, and Data Center platforms. This plugin enables two-way integration between Mattermost and Jira, and was developed by Mattermost. This integration enables you to:

- Send event notifications from your Jira projects to Mattermost channels, with full JQL filtering support.
- Create and transition Jira issues, and attach Mattermost messages to Jira in the Mattermost user interface.

Please see the `source code and documentation <https://github.com/mattermost/mattermost-plugin-jira>`__ for more information.

Productivity integrations
--------------------------

There are several ways to connect your productivity tools to Mattermost. Take a look at the tools recommended below, or visit the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__ to find more.

Google Calendar
~~~~~~~~~~~~~~~

|all-plans| |cloud| |self-hosted|

The Google Calendar integration is a time management tool developed by Wasim Thabraze. This integration enables you to get reminders about appointments and meetings from a configured Google Calendar in any Mattermost channel.

Please see `source code and documentation <https://github.com/waseem18/mattermost-plugin-google-calendar>`__ for more information.

Remind
~~~~~~

|all-plans| |cloud| |self-hosted|

The Remind integration sets one-time or recurring events, tasks, and reminders for users in any Mattermost channel, and was developed by Scott Lee Davis.

Please see the `source code and documentation <https://github.com/scottleedavis/mattermost-plugin-remind>`__ for more information.

Voice, video, and screensharing integrations
--------------------------------------------

There are several ways to work with voice, video, and screensharing in Mattermost. Take a look at the tools recommended below, or visit the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__ to find more.

Zoom
~~~~~

|all-plans| |cloud| |self-hosted|

The Zoom integration was developed by Mattermost, and requires one paid `Zoom Pro, Business, Education, or API plan <https://zoom.us/pricing>`__ to generate an API key and secret. It supports a self-hosted cloud solution and a vendor-hosted cloud solution. This integration enables you to:

- Start and join voice calls, video calls, and use screensharing with your team members.
- Select a video icon in a Mattermost channel to invite team members to join a Zoom call, hosted using the credentials of the user who initiated the call.
 
Please see the `documentation <https://mattermost.gitbook.io/plugin-zoom/>`__ and the `source code <https://github.com/mattermost/mattermost-plugin-zoom>`__ for more information.

Microsoft Teams Meetings
~~~~~~~~~~~~~~~~~~~~~~~~

|enterprise| |professional| |cloud| |self-hosted|

The Microsoft Teams Meetings integration was developed by Mattermost, and requires a Microsoft Teams account. This integration enables you to:

- Start and join voice calls, video calls, and use screensharing with your team members.
- Select a video icon in a Mattermost channel to invite team members to join a Microsoft Teams Meeting, hosted using the credentials of the user who initiated the call.

Please see the `source code and documentation <https://github.com/mattermost/mattermost-plugin-msteams-meetings>`__ for more information.

Bot integrations
-----------------

There are several ways to connect bots with Mattermost. Take a look at the tools recommended below, or visit the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__ to find more.

WelcomeBot
~~~~~~~~~~

|all-plans| |cloud| |self-hosted|

The WelcomeBot integration welcomes users to your Mattermost instance, and was developed by Mattermost. This integration enables you to add a Welcome Bot that helps add new team members to channels to improves onboarding and HR processes.

Please see the `source code and documentation <https://github.com/mattermost/mattermost-plugin-welcomebot>`__ for more information. 

Sample Golang bot
~~~~~~~~~~~~~~~~~~

|all-plans| |cloud| |self-hosted|

The Sample Goland Bot integration is a sample bot for Go driver, and was developed by Mattermost. This integration enables you to:

- Learn how to use the Mattermost Go driver to interact with a Mattermost server, listen to events, and respond to messages.
- Use the API for simple tasks, such as logging in to your server, creating a channel, and posting a message.

Please see the `source code and documentation <https://github.com/mattermost/mattermost-bot-sample-golang>`__ for more information.

Hubot adapter
~~~~~~~~~~~~~

|all-plans| |cloud| |self-hosted|

The Hubot Adapter integration for Mattermost was written in JavaScript, uses Web API and Websockets, and was developed by Andy Lo-A-Foe. This integration enables you to:

- Use the bot to listen for commands and to execute actions based on your requests.
- Invite your bot to any Mattermost channel just like a regular user.

Please see the `source code and documentation <https://github.com/loafoe/hubot-matteruser>`__ for more information. 

Incoming webhooks
-----------------

|all-plans| |cloud| |self-hosted|

Incoming webhooks from external integrations can post messages to Mattermost in Public and Private channels. Learn more about setting up incoming webhooks in our `developer documentation  <https://developers.mattermost.com/integrate/admin-guide/admin-webhooks-incoming/>`__.

Outgoing webhooks
-----------------

|all-plans| |cloud| |self-hosted|

Outgoing webhooks use trigger words to fire new message events to external integrations. For security reasons, outgoing webhooks are only available in Public channels. Learn more about setting up outgoing webhooks in our `developer documentation <https://developers.mattermost.com/integrate/other-integrations/outgoing-webhooks/>`__.

Slash commands
---------------

|all-plans| |cloud| |self-hosted|

Slash commands allow users to interact with external applications by typing ``/`` followed by a command. See the `Executing Slash Commands <https://docs.mattermost.com/messaging/executing-slash-commands.html>`__ product documentation for a list of built-in commands. 

Learn more about setting up custom slash commands in our `developer documentation <https://developers.mattermost.com/integrate/other-integrations/slash-commands/>`__.