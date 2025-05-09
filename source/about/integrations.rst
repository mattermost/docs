Integrations Guide
=====================

.. toctree::
   :maxdepth: 1
   :hidden:
   :titlesonly:

   /guides/pre-built-integrations.rst
   /guides/microsoft-integrations.rst

Mattermost provides a variety of methods to add functionality and customize the end-user experience to suit your organization’s needs, whether you want to add new user capabilities with slash commands, build an advanced chatbot, or completely change the functionality of your server.

Learn about the :doc:`pre-built integrations </guides/pre-built-integrations>` that come with your Mattermost deployment and :doc:`integrations specific to the Microsoft ecosystem </guides/microsoft-integrations>`.

In addition, a wide array of open source integrations are available and ready to use from Mattermost and our community. To see a list of open source integrations available, please see the `Mattermost Marketplace <https://mattermost.com/marketplace/>`_.

For self-hosted deployments in small setups, you might host integrations on the same server on which Mattermost is installed. For larger deployments, you can set up a separate server for integrations, or add them to the server on which the external application is hosted. For example, if you’re self-hosting a Jira server, you could deploy a Jira integration on the Jira server itself. When self-hosting restrictions are less strict, AWS, Heroku, and other public cloud options can also be used.

You can customize Mattermost with the following capabilities and frameworks.

Webhooks
--------

A webhook is a way for one app to send real-time data to another app. In Mattermost, `incoming webhooks <https://developers.mattermost.com/integrate/webhooks/incoming/>`_ receive data from external applications and make a post in a specified channel. They’re great for setting up notifications when something happens in an external application.

`Outgoing webhooks <https://developers.mattermost.com/integrate/webhooks/outgoing/>`_ take data from Mattermost, and send it to an external application. Then the outgoing webhook can post a response back in Mattermost. They’re great for listening in on channels, and then notifying external applications when a trigger word is used.

.. tip::

    Mattermost webhooks are "Slack-compatible”. This means that Mattermost accepts integrations that have a payload in the same format as Slack. In an application that already supports Slack webhooks, you can replace the Slack webhook URL with a Mattermost webhook URL and the integration will “just work”. 
    
    If you have an integration that outputs a payload in a different format, you need to write an intermediate application to act as a translation layer to change it to the format Mattermost uses. Since there’s currently no general standard for webhook formatting, this is unavoidable and just a part of how webhooks work.

Custom slash commands
---------------------

A :doc:`slash command </collaborate/run-slash-commands>` is similar to an `outgoing webhooks <https://developers.mattermost.com/integrate/webhooks/outgoing/>`_, but instead of listening to a channel, it's used as a command tool in a channel.

Slash commands enable users to trigger custom actions, such as creating Jira tickets or GitHub pull requests within Mattermost channels. See the :doc:`built-in slash commands </collaborate/built-in-slash-commands>` product documentation and the `custom slash command <https://developers.mattermost.com/integrate/slash-commands/custom/>`_ developer documentation to learn more.

.. tip::
    The Mattermost slash command format is compatible with Slack's format, so you can easily port commands from Slack. 

Bots
-----

You can deploy interactive bots to help users with processes and tasks with Mattermost by  issuing messages to users they can respond to using buttons and dropdown menus. Bots can be used together with apps and plugins. The Hubot open source project, created by GitHub, Inc., is among the most popular of the bot options.

Pre-built bots are available on the `Mattermost Marketplace <https://mattermost.com/marketplace/>`_, or you can `configure your own bots <https://developers.mattermost.com/integrate/reference/bot-accounts/>`_.

Learn about `Mattermost Hubot integration (hubot-matteruser on npm) <https://www.npmjs.com/package/hubot-matteruser>`_ and `other open source community bots available <https://mattermost.com/marketplace/>`_ or you can `build your own <https://developers.mattermost.com/integrate/reference/bot-accounts/>`_.

API 
----

Mattermost provides complete access to `server APIs via the Mattermost API Reference <https://api.mattermost.com/>`_, along with language-specific drivers to integrate into your own applications.  Interact with users, channels, and everything else that happens on your Mattermost server via a REST API that meets the OpenAPI specification. The API is for developers who want to build bots and other interactions that don’t rely on customizing the Mattermost user experience.

Plugins 
-------

Plugins are the most comprehensive way to add new features and customization to self-hosted Mattermost deployments. These powerful integrations are written in Go and React and they’re ideal for customers wanting to change the behavior of the Mattermost server, desktop, and web apps without forking the core codebase to suit their organization’s needs.

Pre-built plugins are available on the `Mattermost Marketplace <https://mattermost.com/marketplace/>`_, or you can `build your own plugin <https://developers.mattermost.com/integrate/plugins/>`_.

.. note::

  - :doc:`Mattermost Cloud Dedicated </about/cloud-dedicated>` customers supports custom Mattermost plugin uploads.
  - Custom Mattermost plugins aren't available in :doc:`Mattermost Cloud Shared </about/cloud-shared>` deployments. You're limited to the plugins available in the Cloud Marketplace, including:

    .. include:: ./cloud-supported-integrations.rst
       :start-after: :nosearch:

Source code customizations
--------------------------

As an open source project, we support your ability to modify the source code for the server or web app to make changes and customizations to meet your specific needs. 

Learn about `forking our open source repositories <https://developers.mattermost.com/integrate/other-integrations/customization/>`_ and `customizing the Mattermost source code <https://developers.mattermost.com/integrate/customization/customization/>`__ for your specific operational needs.