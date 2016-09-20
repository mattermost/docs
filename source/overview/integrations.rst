=====================
Integrations Overview 
=====================

Mattermost offers a host of options for connecting to systems on your private network as well as services hosted on hybrid and public clouds. 

**Pre-configured integrations options include:**

1. Deploy open source, self-hosted integrations to popular systems (private & public cloud) 
2. Use webhook integrations built for Slack to send data to Mattermost (private & public cloud) 
3. Bring in data from over 600 public cloud applications using Zapier (public cloud only) 
4. Deploy a self-hosted bot as an interface to other systems

**Custom integrations options include:** 

1. Write command line integrations (private & public cloud) 
2. Build and deploy custom apps (private & public cloud) 
3. Create Slack-compatible Slash Commands (private & public cloud) 

Pre-configured integrations 
---------------------------------------------------------

Open source, self-hosted integrations 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A wide array of open source self-hosted integrations are available from the community applications directory. 

Many of these use Mattermost incoming webhooks to deliver data into Mattermost from on-premises systems like Jira, Jenkins, GitLab and other popular products. 

- Learn about `Mattermost open source apps and integrations <https://www.mattermost.org/community-applications/>`_

Slack-compatible webhooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost webhooks are "Slack-compatible, not Slack limited". In applications supporting Slack webhooks you can replace the Slack webhook URL with a Mattermost webhook URL and the integration will work. 

- Learn about `incoming Webhooks <https://docs.mattermost.com/developer/webhooks-incoming.html>`_
- Learn about `Outgoing Webhooks <https://docs.mattermost.com/developer/webhooks-outgoing.html>`_ 

Zapier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost's Zapier support enablees you to connect to over 500 public cloud services, like GitHub, Jira, BitBucket and Confluence. 

- Learn about `Mattermost-Zapier integration <https://docs.mattermost.com/integrations/zapier.html>`_

Self-hosted Bots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can deploy interactive bots with Mattermost to issue commands and receive responses through a centralized interface. The Hubot open source project, created by GitHub, Inc., is among the most popular of the bot options. 

- Learn about `Mattermost Hubot integration (hubot-matteruser on npm) <https://www.npmjs.com/package/hubot-matteruser>`_
- Learn about `all the open source community bots available <https://www.mattermost.org/community-applications/#bots>`_

Custom Integrations 
---------------------------------------------------------

Commandline integrations 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can send data into Mattermost real-time using command line tools by posting HTTP requests with JSON payloads into a Mattermost webhook. You can do this using `curl` or use an open source tool, like `mattersend <https://github.com/mtorromeo/mattersend>`_, to create an integration. 

- Learn about `incoming Webhooks <https://docs.mattermost.com/developer/webhooks-incoming.html>`_
- Learn about the `mattersend CLI integration in Python <https://github.com/mtorromeo/mattersend>`_

Custom applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost provides complete access to server APIs, along with language specific drivers to integrate into your own applications. You can also draw from dozens of open source applications to build your own. 

- Learn about `Mattermost APIs, drivers, webhooks and slash commands <https://docs.mattermost.com/developer/api.html>`_
- Learn about `Mattermost open source apps and integrations <https://www.mattermost.org/community-applications/>`_
- Learn about the `Mattermost Golang Bot Sample <https://github.com/mattermost/mattermost-bot-sample-golang>`_

Mattermost Slash Commands 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to built-in slash commands, Mattermost lets you add your own to execute commands and actions from the Mattermost user interface. The Mattermost slash command format is compatible with Slack's format, so you can re-create functionality your team had in Slack. 

- Learn about `Mattermost Slash Commands <https://docs.mattermost.com/developer/slash-commands.html>`_
