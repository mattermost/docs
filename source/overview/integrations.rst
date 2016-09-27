=====================
Integrations Overview 
=====================

Mattermost offers a host of options for connecting to systems on your private network as well as services hosted on hybrid and public clouds. 

**Pre-configured integrations options include:**

1. `Open source, self-hosted integrations (private and public cloud) <https://docs.mattermost.com/overview/integrations.html#open-source-self-hosted-integrations-private-public-cloud>`_
2. `Slack-compatible webhooks (private and public cloud) <https://docs.mattermost.com/overview/integrations.html#slack-compatible-webhooks-private-public-cloud>`_ 
3. `700 app integrations using Zapier (public cloud only) <https://docs.mattermost.com/overview/integrations.html#app-integrations-using-zapier-public-cloud-only>`_
4. `Self-hosted bots interfacing to other systems (private and public cloud) <https://docs.mattermost.com/overview/integrations.html#self-hosted-bots-interfacing-to-other-systems-private-public-cloud>`_ 

**Custom integrations options include:** 

1. `Command line interface (private and public cloud) <https://docs.mattermost.com/overview/integrations.html#command-line-interface-private-public-cloud>`_
2. `Custom applications (private and public cloud) <https://docs.mattermost.com/overview/integrations.html#custom-applications-private-public-cloud>`_
3. `Slack-compatible Slash Commands (private and public cloud) <https://docs.mattermost.com/overview/integrations.html#slack-compatible-slash-commands-private-public-cloud>`_

Pre-configured integrations 
---------------------------------------------------------

Open source, self-hosted integrations (private and public cloud) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A wide array of open source self-hosted integrations are available from the community applications directory. 

Many of these use Mattermost incoming webhooks to deliver data into Mattermost from on-premises systems like Jira, Jenkins, GitLab and other popular products. 

- Learn about `Mattermost open source apps and integrations <https://www.mattermost.org/community-applications/>`_

Slack-compatible webhooks (private and public cloud) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost webhooks are "Slack-compatible, not Slack limited". In applications supporting Slack webhooks you can replace the Slack webhook URL with a Mattermost webhook URL and the integration will work. 

- Learn about `incoming Webhooks <https://docs.mattermost.com/developer/webhooks-incoming.html>`_
- Learn about `Outgoing Webhooks <https://docs.mattermost.com/developer/webhooks-outgoing.html>`_ 

700 app integrations using Zapier (public cloud only) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost's Zapier support enablees you to connect to over 700 public cloud services, like Email, Gmail, GitHub, Jira, BitBucket and Confluence. 

- Learn about `Mattermost-Zapier integration <https://docs.mattermost.com/integrations/zapier.html>`_

Self-hosted bots interfacing to other systems (private and public cloud) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can deploy interactive bots with Mattermost to issue commands and receive responses through a centralized interface. The Hubot open source project, created by GitHub, Inc., is among the most popular of the bot options. 

- Learn about `Mattermost Hubot integration (hubot-matteruser on npm) <https://www.npmjs.com/package/hubot-matteruser>`_
- Learn about `all the open source community bots available <https://www.mattermost.org/community-applications/#bots>`_

Custom Integrations 
---------------------------------------------------------

Command line interface (private and public cloud) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can send data into Mattermost real-time using command line tools by posting HTTP requests with JSON payloads into a Mattermost webhook. You can do this using `curl` or use an open source tool, like `mattersend <https://github.com/mtorromeo/mattersend>`_, to create an integration. 

- Learn about `incoming Webhooks <https://docs.mattermost.com/developer/webhooks-incoming.html>`_
- Learn about the `mattersend CLI integration in Python <https://github.com/mtorromeo/mattersend>`_

Custom applications (private and public cloud) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost provides complete access to server APIs, along with language specific drivers to integrate into your own applications. You can also draw from dozens of open source applications to build your own. 

- Learn about `Mattermost APIs, drivers, webhooks and slash commands <https://docs.mattermost.com/developer/api.html>`_
- Learn about `Mattermost open source apps and integrations <https://www.mattermost.org/community-applications/>`_
- Learn about the `Mattermost Golang Bot Sample <https://github.com/mattermost/mattermost-bot-sample-golang>`_

Slack-compatible Slash Commands (private and public cloud) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to built-in slash commands, Mattermost lets you add your own to execute commands and actions from the Mattermost user interface. The Mattermost slash command format is compatible with Slack's format, so you can re-create functionality your team had in Slack. 

- Learn about `Mattermost Slash Commands <https://docs.mattermost.com/developer/slash-commands.html>`_
