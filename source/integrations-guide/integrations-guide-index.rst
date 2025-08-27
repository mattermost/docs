Integrations Guide
=====================

.. toctree::
   :maxdepth: 1
   :hidden:
   :titlesonly:

   popular-integrations
   run-slash-commands
   webhook-integrations

Mattermost provides a variety of methods to add functionality and customize the end-user experience to suit your organization's needs, whether you want to add new user capabilities with slash commands, build an advanced chatbot, or completely change the functionality of your server.

Learn about the :doc:`popluar pre-built integrations </integrations-guide/popular-integrations>` that come with your Mattermost deployment, :ref:`integrations specific to the Microsoft ecosystem <integrations-guide/popular-integrations:microsoft integrations>`, and :doc:`webhook integrations </integrations-guide/webhook-integrations>`.

In addition, a wide array of open source integrations are available and ready to use from Mattermost and our community. To see a list of open source integrations available, please see the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__.

For self-hosted deployments in small setups, you might host integrations on the same server on which Mattermost is installed. For larger deployments, you can set up a separate server for integrations, or add them to the server on which the external application is hosted. For example, if you're self-hosting a Jira server, you could deploy a Jira integration on the Jira server itself. When self-hosting restrictions are less strict, AWS, Heroku, and other public cloud options can also be used.

You can customize Mattermost with the following integration capabilities and frameworks.

Slash Commands
---------------

A :doc:`slash command </integrations-guide/run-slash-commands>` is similar to an :doc:`outgoing webhooks </integrations-guide/outgoing-webhooks/>`, but instead of listening to a channel, it's used as a command tool in a channel. The Mattermost slash command format is compatible with Slack's format, so you can easily port commands from Slack.

Slash commands enable users to trigger custom actions, such as creating Jira tickets or GitHub pull requests within Mattermost channels. See the :doc:`built-in slash commands </integrations-guide/built-in-slash-commands>` available and see the `custom slash command <https://developers.mattermost.com/integrate/slash-commands/custom/>`_ developer documentation to learn more about creating your own custom slash commands.

Webhooks
--------

Webhooks are a powerful way to integrate Mattermost with other applications and services. They allow you to send real-time data from Mattermost to external systems or receive data from those systems into Mattermost. Webhooks can be used for a variety of purposes, such as sending notifications, triggering workflows, or updating external systems based on events in Mattermost. See the :doc:`webhook integrations </integrations-guide/webhook-integrations>` documentation for details on working with :doc:`incoming </integrations-guide/incoming-webhooks>` and :doc:`outgoing webhooks </integrations-guide/outgoing-webhooks>`.

Bots
-----

You can deploy interactive bots to help users with processes and tasks with Mattermost by  issuing messages to users they can respond to using buttons and dropdown menus. Bots can be used together with apps and plugins. The Hubot open source project, created by GitHub, Inc., is among the most popular of the bot options.

Pre-built bots are available on the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__, or you can `configure your own bots <https://developers.mattermost.com/integrate/reference/bot-accounts/>`_.

Learn about `Mattermost Hubot integration (hubot-matteruser on npm) <https://www.npmjs.com/package/hubot-matteruser>`_ and `other open source community bots available <https://mattermost.com/marketplace/>`__ or you can `build your own <https://developers.mattermost.com/integrate/reference/bot-accounts/>`_.

API 
----

Mattermost provides complete access to `server APIs via the Mattermost API Reference <https://api.mattermost.com/>`_, along with language-specific drivers to integrate into your own applications.  Interact with users, channels, and everything else that happens on your Mattermost server via a REST API that meets the OpenAPI specification. The API is for developers who want to build bots and other interactions that don't rely on customizing the Mattermost user experience.

Plugins 
-------

Plugins are the most comprehensive way to add new features and customization to self-hosted Mattermost deployments. These powerful integrations are written in Go and React and they're ideal for customers wanting to change the behavior of the Mattermost server, desktop, and web apps without forking the core codebase to suit their organization's needs.

Pre-built plugins are available on the `Mattermost Marketplace <https://mattermost.com/marketplace/>`__, or you can `build your own plugin <https://developers.mattermost.com/integrate/plugins/>`_.

.. note::

  - :doc:`Mattermost Cloud Dedicated </product-overview/cloud-dedicated>` customers supports custom Mattermost plugin uploads.
  - Custom Mattermost plugins aren't available in :doc:`Mattermost Cloud Shared </product-overview/cloud-shared>` deployments. You're limited to the plugins available in the Cloud Marketplace, including:

    .. include:: /product-overview/cloud-supported-integrations.rst
       :start-after: :nosearch:

Frequently Asked Questions
---------------------------

What integrations come pre-packaged with Mattermost Server?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the :doc:`integrations guide </integrations-guide/integrations-guide-index>` documentation for details on pre-packaged integrations available with Mattermost Server.

Can I use Mattermost to add messaging functionality to my proprietary SaaS service?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost is an open source, self-hosted alternative to proprietary SaaS services that lock in the data of users and customers.

While you're welcome to use the Mattermost source code under its open source license, Mattermost, Inc. does not offer support or technical advice for proprietary SaaS projects that result in customers potentially being paywalled from their data should they stop paying SaaS fees.

To learn more about why we strongly believe that users and customers should always have access to their data, please read `why we created Mattermost <https://mattermost.com/about-us/>`_.

What's the difference between incoming and outgoing webhooks?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A webhook is a way for one app to send real-time data to another app.

In Mattermost, incoming webhooks receive data from external applications and make a post in a specified channel. They're great for setting up notifications that are sent into a Mattermost channel when something happens in an external application.

Outgoing webhooks are triggered based on a rule in Mattermost and takes data (the message, and some contextual info) from Mattermost and send it to an external application. The receiving server of the outgoing webhook can then post a response back in Mattermost. They're great for listening for a specific word, and then notifying external applications when a trigger word is used.

What's a slash command?
~~~~~~~~~~~~~~~~~~~~~~~

A slash command is similar to an outgoing webhook, but instead of listening to a channel it is used as a command tool. This means if you type in a slash command it will not be posted to a channel, whereas an outgoing webhook is only triggered by posted messages.

What does Slack-compatible mean?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Slack compatible means that Mattermost accepts integrations that have a payload in the same format as Slack's legacy "Message Attachment" payload. If you have a Slack integration, you should be able to set it up in Mattermost without changing the format of the message being sent over.   

What if I have a webhook from somewhere other than Slack?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have an integration that outputs a payload in a different format, you need to write an intermediate application, such as N8N.io, Zapier, or Integromat, to act as a translation layer to change it to the format Mattermost uses. Since there’s currently no general standard for webhook formatting, this is unavoidable and just a part of how webhooks work.

If there's no translation layer, Mattermost won't understand the data you're sending.

What are attachments?
---------------------

When "attachments" are mentioned in Mattermost integrations documentation, it refers to Slack's message attachments functionality. These "attachments" can be optionally added as an array in the data sent by an integration, and are used to customize the formatting of the message.

Mattermost doesn't currently support the ability to attach files to a post made via webhook. You can use the API to attach files to a message if needed. 

Where can I find existing integrations?
---------------------------------------

Visit the `Mattermost Marketplace <https://mattermost.com/marketplace>`__ to access open source integrations to common tools like Jira, Jenkins, and GitLab, along with interactive bot applications, and other communication tools that are freely available for use and customization. 

Alternatively, within Mattermost, when logged in as an Administrator, you can click on the "Marketplace" option in the main menu and easily install plugins or apps from there. 

Where should I install my integrations?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For self-hosted deployments in small setups, you might host integrations on the same server on which Mattermost is installed. For larger deployments, you can set up a separate server for integrations, or add them to the server on which the external application is hosted. For example, if you're self-hosting a Jira server you could deploy a Jira integration on the Jira server itself. When self-hosting restrictions are less strict, AWS, Heroku, and other public cloud options could also be used.

Where can I get more information about integrations?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Join our `Developers channel <https://community.mattermost.com/core/channels/developers>`_ for technical discussions, and visit our `Integrations channel <https://community.mattermost.com/core/channels/integrations>`_ for all integrations and plugins discussions.

Can I use webhooks to be notified when new integrations are available on the Mattermost Marketplace?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes! A `bash script <https://gist.github.com/mickmister/543a49584146af18ba5e5f82dd86ea93>`_ is available that checks for new integrations in the Mattermost Marketplace, and triggers a post through a Mattermost `incoming webhook <https://developers.mattermost.com/integrate/webhooks/incoming/>`_ request. The script downloads the latest listing, compares it with a locally stored version of the listing, and, if a new plugin is identified, a notification is pushed to a Mattermost channel.

Source Code Customizations
--------------------------

As an open source project, we support your ability to modify the source code for the server or web app to make changes and customizations to meet your specific needs. 

Learn about `forking our open source repositories <https://developers.mattermost.com/integrate/other-integrations/customization/>`_ and `customizing the Mattermost source code <https://developers.mattermost.com/integrate/customization/customization/>`__ for your specific operational needs.