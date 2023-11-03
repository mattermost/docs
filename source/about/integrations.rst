Integrations overview
=====================

Mattermost provides a variety of methods to add functionality and customize the end-user experience to suit your organization’s needs, whether you want to add new user capabilities with slash commands, build an advanced chatbot, or completely change the functionality of your server.

A wide array of open source integrations are available and ready to use from Mattermost and our community. To see a list of open source integrations please see the `Mattermost Integrations Directory <https://mattermost.com/marketplace/>`__.

For self-hosted deployments in small setups, you might host integrations on the same server on which Mattermost is installed. For larger deployments, you can set up a separate server for integrations, or add them to the server on which the external application is hosted. For example, if you’re self-hosting a Jira server, you could deploy a Jira integration on the Jira server itself. When self-hosting restrictions are less strict, AWS, Heroku, and other public cloud options can also be used.

You can customize Mattermost with the following capabilities and frameworks.

Custom Apps
-----------

Apps are lightweight, interactive add-ons that can be written in any language and run on any HTTP-compatible hosting service. They enable you to connect with external services and build interactions that users can easily follow and work across the Mattermost web app, desktop app, and mobile app.   

Prebuilt apps are available on the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__, or you can `build your own custom app <https://developers.mattermost.com/integrate/apps/>`__.

API 
----

Mattermost provides complete access to `server APIs <https://api.mattermost.com/>`__, along with language-specific drivers to integrate into your own applications.  Interact with users, channels, and everything else that happens on your Mattermost server via a REST API that meets the OpenAPI specification. The API is for developers who want to build bots and other interactions that don’t rely on customizing the Mattermost user experience.

`View the Mattermost API Reference <https://api.mattermost.com/>`__.

Plugins 
-------

Plugins are the most comprehensive way to add new features and customization to self-hosted Mattermost deployments. These powerful integrations are written in Go and React and they’re ideal for customers wanting to change the behavior of the Mattermost server, desktop, and web apps without forking the core codebase to suit their organization’s needs.

Prebuilt plugins are available on the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__, or you can `build your own plugin <https://developers.mattermost.com/integrate/plugins/>`__.

.. note::
    Custom Mattermost plugins aren't available in Mattermost Cloud deployments - you are limited to the plugins that are available in the Cloud Marketplace.

Bots
-----

You can deploy interactive bots to help users with processes and tasks with Mattermost by  issuing messages to users they can respond to using buttons and dropdown menus. Bots can be used together with apps and plugins. The Hubot open source project, created by GitHub, Inc., is among the most popular of the bot options.

Prebuilt bots are available on the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__, or you can `configure your own bots <https://developers.mattermost.com/integrate/reference/bot-accounts/>`__.

Learn about `Mattermost Hubot integration (hubot-matteruser on npm) <https://www.npmjs.com/package/hubot-matteruser>`__ and `other open source community bots available <https://integrations.mattermost.com/>`__ or you can `build your own </integrations/cloud-bot-accounts.html>`__.

Custom slash commands
---------------------

A `slash command <https://developers.mattermost.com/integrate/slash-commands/>`__ is similar to an `outgoing webhooks <https://developers.mattermost.com/integrate/webhooks/outgoing/>`__, but instead of listening to a channel, it's used as a command tool in a channel.

Slash commands enable users to trigger custom actions, such as creating Jira tickets or GitHub pull requests within Mattermost channels. See the `built-in slash commands <https://developers.mattermost.com/integrate/slash-commands/built-in/>`__ and the `custom slash command <https://developers.mattermost.com/integrate/slash-commands/custom/>`__ developer documentation to learn more.

.. tip::
    The Mattermost slash command format is compatible with Slack's format, so you can easily port commands from Slack. 

Learn about `Mattermost slash commands </messaging/extending-messaging-with-integrations.html#slash-commands>`__.

Webhooks
--------

A webhook is a way for one app to send real-time data to another app. In Mattermost, `incoming webhooks <https://developers.mattermost.com/integrate/webhooks/incoming/>`__ receive data from external applications and make a post in a specified channel. They’re great for setting up notifications when something happens in an external application.

`Outgoing webhooks <https://developers.mattermost.com/integrate/webhooks/outgoing/>`__ take data from Mattermost, and send it to an external application. Then the outgoing webhook can post a response back in Mattermost. They’re great for listening in on channels, and then notifying external applications when a trigger word is used.

.. tip::

    Mattermost webhooks are "Slack-compatible”. This means that Mattermost accepts integrations that have a payload in the same format as Slack. In an application that already supports Slack webhooks, you can replace the Slack webhook URL with a Mattermost webhook URL and the integration will “just work”. 
    
    If you have an integration that outputs a payload in a different format, you need to write an intermediate application to act as a translation layer to change it to the format Mattermost uses. Since there’s currently no general standard for webhook formatting, this is unavoidable and just a part of how webhooks work.

Source code customizations
--------------------------
As an open source project, we support your ability to modify the source code for the server or web app to make changes and customizations to meet your specific needs. 

Learn about `forking our open source repositories <https://developers.mattermost.com/integrate/other-integrations/customization/>`__.
