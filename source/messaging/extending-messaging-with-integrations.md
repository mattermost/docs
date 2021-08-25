## Integrations

Settings for integrations are accessible from the **Main Menu**. Select **Integrations** to open a page where you can view and configure incoming webhooks, outgoing webhooks, and slash commands for your team. If you can't see an **Integrations** option, then your System Admin may have only given Admins access.

[Visit our app directory](https://about.mattermost.com/default-app-directory/) for dozens of open source integrations to common tools like Jira, Jenkins, GitLab, Trac, Redmine, and Bitbucket, along with interactive bot applications (Hubot, mattermost-bot), and other communication tools (Email, IRC, XMPP, Threema) that are freely available for use and customization.

### Microsoft integrations

There are several ways to connect your Microsoft tools to Mattermost. Take a look at the tools recommended below, or visit the Marketplace to find others.

#### Office 365 Calendar (E20)

- Two-way integration between Mattermost and Office 365 Calendar, developed by Mattermost.
- Receive a daily summary of calendar events, and accept or decline new events.
- Reflect user status as "Do Not Disturb" when in a meeting scheduled via Outlook Calendar.
- Visit the Marketplace to install, configure, and use this integration.

#### Skype for Business

- Start and join voice calls, video calls, and use screen-sharing with your team members. Developed by kosgrz and maintained by Mattermost.
- Selecting a video icon in a Mattermost channel invites team members to join a Skype for Business call, hosted using the credentials of the user who initiated the call.
- Supports a vendor-hosted cloud solution.
- Visit the Marketplace to install, configure, and use this integration.
- Source code: https://github.com/mattermost/mattermost-plugin-skype4business

#### Office 365 SSO (E20)

- Configure Mattermost to use your Office 365 credentials and Azure Active Directory account as a single sign-on (SSO) service, developed by Mattermost.
- Supports Microsoft Active Directory Tenants for team creation, account creation, and Single Sign-On (SSO).
- Receive a daily summary of calendar events, and accept or decline new events.
- Visit the Marketplace to install, configure, and use this integration.

### CI/CD integrations

There are several ways to connect your CI/CD tools to Mattermost. Take a look at the tools recommended below, or visit the Marketplace to find others.

#### GitHub

 - Two-way integration between Mattermost and GitHub, developed by Mattermost.
 - Get reminders on issues and pull requests that need your attention.
 - Get notifications in Mattermost about mentions, review requests, and comments.
 - Supports GitHub Enterprise, works with SaaS and Enterprise versions of GitHub.
 - Visit the Marketplace to install, configure, and use this integration.
 - Source code: https://github.com/mattermost/mattermost-plugin-github

#### GitLab

 - Two-way integration between Mattermost and GitLab, developed by Romain Maneschi, supported by Mattermost.
 - Get reminders on issues and merge requests that need your attention.
 - Get notifications in Mattermost about mentions, review requests, and comments.
 - Supports SaaS and on-prem versions of GitLab.
 - Visit the Marketplace to install, configure, and use this integration.
 - Source code: https://github.com/mattermost/mattermost-plugin-gitlab

### Atlassian integrations

There are several ways to connect Atlassian tools to Mattermost. Take a look at the tools recommended below, or visit the Marketplace to find others.

#### Confluence

- Atlassian Marketplace application for Confluence and Mattermost, developed by codefortynine.
- Send notifications about page, blogpost, question, or comment updates from your Confluence spaces to Mattermost channels.
- Configure notifications for a specific space, and also user notifications for tasks and mentions.
- Supports Confluence Cloud, Server and Data Center platforms.
- Marketplace download + docs: https://marketplace.atlassian.com/apps/1215055/slack-for-confluence

#### Jira Plugin

- Two-way integration between Mattermost and Jira, developed by Mattermost.
- Send event notifications from your Jira projects to Mattermost channels, with full JQL filtering support.
- Create and transition Jira issues, and attach Mattermost messages to Jira in the Mattermost user interface.
- Supports Jira Core and Jira Software products, for Cloud, Server and Data Center platforms.
- Source code + docs: https://github.com/mattermost/mattermost-plugin-jira

### Productivity integrations

There are several ways to connect your productivity tools to Mattermost. Take a look at the tools recommended below, or visit the Marketplace to find others.

#### Google Calendar

 - Time management tool for Google Calendar, developed by Wasim Thabraze.
 - Get reminders about appointments and meetings from a configured Google Calendar to any Mattermost channel.
 - Source code + docs: https://github.com/waseem18/mattermost-plugin-google-calendar

#### Remind Plugin

 - A Mattermost plugin that sets reminders for users and channels, developed by Scott Lee Davis.
 - Set reminders for one-time or recurring events and tasks in any Mattermost channel.
 - Source code + docs: https://github.com/scottleedavis/mattermost-plugin-remind

### Voice, video, and screensharing integrations

There are several ways to work with voice, video, and screensharing in Mattermost. Take a look at the tools recommended below, or visit the Marketplace to find others.

#### Zoom

- Start and join voice calls, video calls, and use screensharing with your team members, developed by Mattermost.
- Click a video icon in a Mattermost channel to invite team members to join a Zoom call, hosted using the credentials of the user who initiated the call.
- Requires one paid `Zoom Pro, Business, Education, or API plan, <https://zoom.us/pricing>`_ to generate an API key and secret.
- Supports a self-hosted cloud solution and a vendor-hosted cloud solution.
- Docs available at: https://docs.mattermost.com/integrations/zoom.html.
- Source code available at: https://github.com/mattermost/mattermost-plugin-zoom.

#### Microsoft Teams Meetings

- Start and join voice calls, video calls, and use screensharing with your team members, developed by Mattermost.
- Click a video icon in a Mattermost channel to invite team members to join a Microsoft Teams Meeting, hosted using the credentials of the user who initiated the call.
- Requires a Microsoft Teams account.
- Requires Mattermost Enterprise Edition E20.
- Source code and docs available at: https://github.com/mattermost/mattermost-plugin-msteams-meetings.

## Incoming Webhooks

Incoming webhooks from external integrations can post messages to Mattermost in Public and Private channels. Learn more about setting up incoming webhooks in our [documentation](https://developers.mattermost.com/integrate/admin-guide/admin-webhooks-incoming/).

## Outgoing Webhooks

Outgoing webhooks use trigger words to fire new message events to external integrations. For security reasons, outgoing webhooks are only available in public channels. Learn more about setting up outgoing webhooks on our [documentation page](https://docs.mattermost.com/developer/webhooks-outgoing.html).

## Slash Commands

Slash commands allow users to interact with external applications by typing `/` followed by a command. See [executing slash commands](https://docs.mattermost.com/help/messaging/executing-commands.html) for a list of built-in commands. Learn more about setting up custom slash commands on our [documentation page](https://docs.mattermost.com/developer/slash-commands.html).
