Integration questions
=====================

.. contents:: On this page
    :backlinks: top
    :depth: 2

Can I use Mattermost to add messaging functionality to my proprietary SaaS service?
------------------------------------------------------------------------------------

Mattermost is an open source, self-hosted alternative to proprietary SaaS services that lock in the data of users and customers.

While you're welcome to use the Mattermost source code under its open source license, Mattermost, Inc. does not offer support or technical advice for proprietary SaaS projects that result in customers potentially being paywalled from their data should they stop paying SaaS fees.

To learn more about why we strongly believe that users and customers should always have access to their data, please read `why we created Mattermost <https://mattermost.com/about-us/>`__.

What's the difference between incoming and outgoing webhooks?
-------------------------------------------------------------

A webhook is a way for one app to send real-time data to another app.

In Mattermost, incoming webhooks receive data from external applications and make a post in a specified channel. They're great for setting up notifications that are sent into a Mattermost channel when something happens in an external application.

Outgoing webhooks are triggered based on a rule in Mattermost and takes data (the message, and some contextual info) from Mattermost and send it to an external application. The receiving server of the outgoing webhook can then post a response back in Mattermost. They're great for listening for a specific word, and then notifying external applications when a trigger word is used.

What's a slash command?
-----------------------

A slash command is similar to an outgoing webhook, but instead of listening to a channel it is used as a command tool. This means if you type in a slash command it will not be posted to a channel, whereas an outgoing webhook is only triggered by posted messages.

What does Slack-compatible mean?
--------------------------------

Slack compatible means that Mattermost accepts integrations that have a payload in the same format as Slack's legacy "Message Attachment" payload. If you have a Slack integration, you should be able to set it up in Mattermost without changing the format of the message being sent over.   

What if I have a webhook from somewhere other than Slack?
---------------------------------------------------------

If you have an integration that outputs a payload in a different format, you need to write an intermediate application, such as N8N.io, Zapier, or Integromat, to act as a translation layer to change it to the format Mattermost uses. Since there’s currently no general standard for webhook formatting, this is unavoidable and just a part of how webhooks work.

If there's no translation layer, Mattermost won't understand the data you're sending.

What are attachments?
---------------------

When "attachments" are mentioned in Mattermost integrations documentation, it refers to Slack's message attachments functionality. These "attachments" can be optionally added as an array in the data sent by an integration, and are used to customize the formatting of the message.

Mattermost doesn't currently support the ability to attach files to a post made via webhook. You can use the API to attach files to a message if needed. 

Where can I find existing integrations?
---------------------------------------

[Visit the Mattermost Marketplace](https://mattermost.com/marketplace) to access open source integrations to common tools like Jira, Jenkins, and GitLab, along with interactive bot applications, and other communication tools that are freely available for use and customization. 

Alternatively, within Mattermost, when logged in as an Administrator, you can click on the "Marketplace" option in the main menu and easily install plugins or apps from there. 

Where should I install my integrations?
---------------------------------------

For self-hosted deployments in small setups, you might host integrations on the same server on which Mattermost is installed. For larger deployments, you can set up a separate server for integrations, or add them to the server on which the external application is hosted. For example, if you're self-hosting a Jira server you could deploy a Jira integration on the Jira server itself. When self-hosting restrictions are less strict, AWS, Heroku, and other public cloud options could also be used.

Where can I get more information about integrations?
----------------------------------------------------

Come `join our Contributors community channel <https://community.mattermost.com/core/channels/tickets>`__ on our daily build server, where you can discuss questions with community members and the Mattermost core team. 

Join our `Developers channel <https://community.mattermost.com/core/channels/developers>`__ for technical discussions, and visit our `Integrations channel <https://community.mattermost.com/core/channels/integrations>`__ for all integrations and plugins discussions.