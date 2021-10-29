
Integrations Overview
=====================

Mattermost provides a variety of methods to add functionality and customize the end-user experience to suit your organization’s needs, whether you want to add new user capabilities with slash commands, build an advanced chatbot, or completely change the functionality of your server.

A wide array of open source integrations are available and ready to use from Mattermost and our community. To see a list of open source integrations please see the `Mattermost Integrations Directory <https://mattermost.com/marketplace/>`__.

You can customize Mattermost with the following capabilities and frameworks.

Custom Apps
-----------

Apps are lightweight, interactive add-ons that can be written in any language and run on any HTTP-compatible hosting service. They enable you to connect with external services and build interactions that users can easily follow and work across the Mattermost web app, desktop app, and mobile app.   

Prebuilt apps are available in our `Mattermost Integrations Marketplace <https://mattermost.com/marketplace/>`__, or you can `build your own custom app <https://developers.mattermost.com/integrate/apps/>`_.

API 
----

Mattermost provides complete access to `server APIs <https://api.mattermost.com/>`__, along with language-specific drivers to integrate into your own applications.  Interact with users, channels, and everything else that happens on your Mattermost server via a REST API that meets the OpenAPI specification. The API is for developers who want to build bots and other interactions that don’t rely on customizing the Mattermost user experience.

`View the Mattermost API Reference <https://api.mattermost.com/>`__.

Plugins 
-------

Plugins are the most comprehensive way to add new features and customization to Mattermost.  These powerful integrations are written in Go and React and they’re ideal for customers wanting to change the behavior of the server, desktop, and web apps without forking the core codebase to suit their organization’s needs.  

Prebuilt plugins are available in our `Mattermost Integrations Marketplace <https://mattermost.com/marketplace/>`__, or you can `build your own plugin <https://developers.mattermost.com/integrate/plugins/>`_.

Bots
-----

You can deploy interactive bots to help users with processes and tasks with Mattermost by  issuing messages to users they can respond to using buttons and dropdown menus. Bots can be used together with apps and plugins. The Hubot open source project, created by GitHub, Inc., is among the most popular of the bot options.

Learn about `Mattermost Hubot integration (hubot-matteruser on npm) <https://www.npmjs.com/package/hubot-matteruser>`__ and `other open source community bots available <https://integrations.mattermost.com/>`__ or you can `build your own <https://docs.mattermost.com/integrations/cloud-bot-accounts.html>`_.

Custom Slash Commands
---------------------

Slash commands bring the power of developer command-line tools, to channels in Mattermost. Enable your users to trigger custom actions such as creating a Jira ticket or GitHub PR directly from within Mattermost.  . The Mattermost slash command format is compatible with Slack's format, so you can easily port commands from Slack.

Learn about `Mattermost slash commands <https://docs.mattermost.com/messaging/extending-messaging-with-integrations.html#slash-commands>`__.

Webhooks
--------

Easily integrate events from external systems with a webhook that will post messages within a channel, or listen for new messages containing specific words to trigger an  outgoing webhook. Mattermost webhooks are "Slack-compatible” meaning that with applications that already support Slack webhooks, you can replace the Slack webhook URL with a Mattermost webhook URL and the integration will “just work”. 

Learn about `incoming webhooks <https://docs.mattermost.com/messaging/extending-messaging-with-integrations.html#incoming-webhooks>`__ and `outgoing webhooks <https://docs.mattermost.com/messaging/extending-messaging-with-integrations.html#outgoing-webhooks>`__.

Interactive Messages
--------------------

Mattermost supports interactive message buttons and menus for incoming and outgoing webhooks, custom slash commands, and plugins via actions. They help make your integrations richer by completing common tasks inside Mattermost conversations, increasing user engagement and productivity. Interactive messages can be used together with slash commands, custom apps, and plugins. 

Learn about `interactive messages and buttons <https://developers.mattermost.com/integrate/admin-guide/admin-interactive-messages/>`_ and `interactive dialogs <https://developers.mattermost.com/integrate/admin-guide/admin-interactive-dialogs/>`__. 

CLI
----
You can send data into Mattermost real-time using command line tools by posting HTTP requests with JSON payloads into a Mattermost webhook. You can do this using `curl` or use an open source tool, like `mattersend <https://github.com/mtorromeo/mattersend>`__ to create an integration.

Zapier
--------- 
Mattermost's Zap connector enables you to connect to over 2,000 public cloud services, like Email, Gmail, GitHub, Jira, BitBucket, and Confluence.

Learn about `Mattermost-Zapier integration <https://docs.mattermost.com/integrations/zapier.html>`__.

Source Code Customizations
--------------------------
As an open source project, we support your ability to modify the source code for the server or web app to make changes and customizations to meet your specific needs. 

Learn about `forking our open source repositories <https://developers.mattermost.com/integrate/other-integrations/customization/>`__.

