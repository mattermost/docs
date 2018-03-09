
Integrations Overview 
=====================

  .. note::
    To see a list of open source integrations please see the `Mattermost Integrations Directory <https://about.mattermost.com/community-applications/>`_ 

Mattermost offers a host of options for connecting to systems on your private network as well as services hosted on hybrid and public clouds. 

**Pre-configured integrations options include:**

1. `Open source, self-hosted integrations (private and public cloud)`_
2. `Slack-compatible webhooks (private and public cloud)`_ 
3. `700 app integrations using Zapier (public cloud only)`_
4. `Self-hosted bots interfacing to other systems (private and public cloud)`_ 

**Custom integrations options include:** 

1. `Command line interface (private and public cloud)`_
2. `Custom applications using APIs and Drivers (private and public cloud)`_
3. `Slack-compatible Slash Commands (private and public cloud)`_

Pre-Configured Integrations 
---------------------------

Open Source, Self-hosted Integrations (Private and Public Cloud)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A wide selection of self-hosted open source integrations are available from the community applications directory. 

Many of these use Mattermost incoming webhooks to deliver data into Mattermost from on-premises systems like Jira, Jenkins, GitLab and other popular products. 

- Learn about `Mattermost open source apps and integrations <https://about.mattermost.com/default-app-directory/>`_

Slack-compatible Webhooks (Private and Public Cloud)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost webhooks are *Slack-compatible*, not *Slack limited*. Applications supporting Slack webhooks can replace the Slack webhook URL with a Mattermost webhook URL and the integration functions. 

- Learn about `incoming Webhooks <https://docs.mattermost.com/developer/webhooks-incoming.html>`_
- Learn about `Outgoing Webhooks <https://docs.mattermost.com/developer/webhooks-outgoing.html>`_ 

Seven hundred Application Integrations Using Zapier (Public Cloud Only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost's Zapier support enables you to connect to over 700 public cloud services, like Email, Gmail, GitHub, Jira, BitBucket and Confluence. 

- Learn about `Mattermost-Zapier integration <https://docs.mattermost.com/integrations/zapier.html>`_

Self-hosted Bots Interfacing to Other Systems (Private and Public Cloud)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Interactive bots can be deployed with Mattermost to issue commands and receive responses through a centralized interface. The Hubot open source project, created by GitHub, Inc., is among the most popular of the bot options. 

- Learn about `Mattermost Hubot integration (hubot-matteruser on npm) <https://www.npmjs.com/package/hubot-matteruser>`_
- Learn about `all the open source community bots available <https://about.mattermost.com/default-app-directory/>`_

Custom Integrations 
---------------------------------------------------------

Command Line Interface (Private and Public Cloud)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's possible to send data into Mattermost in real-time with command line tools by posting HTTP requests with JSON payloads into a Mattermost webhook. You can do this using `curl` or an open source tool like `mattersend <https://github.com/mtorromeo/mattersend>`_, to create an integration. 

- Learn about `incoming Webhooks <https://docs.mattermost.com/developer/webhooks-incoming.html>`_
- Learn about the `mattersend CLI integration in Python <https://github.com/mtorromeo/mattersend>`_

Custom Applications Using APIs and Drivers (Private and Public Cloud)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost provides complete access to `server APIs <https://api.mattermost.com/>`_, along with language specific drivers to integrate into your own applications. You can also draw from dozens of open source applications to build your own. Go in-depth and learn about Mattermost:

- `REST APIs <https://api.mattermost.com/>`_
- `drivers, webhooks and slash commands <https://docs.mattermost.com/developer/api.html>`_
- `open source apps and integrations <https://about.mattermost.com/default-app-directory/>`_
- `Golang Bot Sample <https://github.com/mattermost/mattermost-bot-sample-golang>`_

Slack-compatible Slash Commands (Private and Public Cloud)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost lets you add your own slash commands to execute commands and actions from the Mattermost user interface. The Mattermost slash command format is compatible with Slack's format, so you can re-create functionality your team had in Slack. 

- Learn about `Mattermost Slash Commands <https://docs.mattermost.com/developer/slash-commands.html>`_
