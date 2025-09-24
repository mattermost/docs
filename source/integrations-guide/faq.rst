Frequently Asked Questions
===========================

What is meant by no-code, low-code, and pro-code?
-------------------------------------------------

.. _no-code:

No-code
~~~~~~~~

Integration or automation can be achieved without writing any code. All configuration is done via user-friendly interfaces or by installing pre-made components. This is ideal for non-technical users or admins. 

For example, installing a plugin from the marketplace or using a drag-and-drop automation tool would be considered no-code. The heavy lifting is pre-built and you just need to configure it.

.. _low-code:

Low-code
~~~~~~~~

Minimal coding or scripting is needed to implement the integration. Low-code solutions might require writing a few lines of script or simple configuration in code-like logic, but not building a full software application. 

In Mattermost’s context, something like setting up a webhook with a small custom script, or tweaking an automation template would be considered low-code. It typically assumes some technical knowledge, but far less than full-scale development. Utilizing templates or online AI tooling can likely meet the need for most low-code integration requirements.

.. _pro-code:

Pro-code
~~~~~~~~

These kinds of integrations require a professional software developer to write code and sometimes build underlying infrastructure. These integrations offer maximum flexibility at the cost of technical complexity, for example building a custom Mattermost plugin or writing a complex bot program using the Mattermost API in a custom application. 

Pro-code integrations are essentially software projects – you’ll use developer tools, work with source code, and follow software development practices to build and maintain them.

What does Slack-compatible mean?
--------------------------------

Slack compatible means that Mattermost accepts integrations that have a payload in the same format as Slack's legacy "Message Attachment" payload. If you have a Slack integration, you should be able to set it up in Mattermost without changing the format of the message being sent over.   

What if I have a webhook from somewhere other than Slack?
---------------------------------------------------------

If you have an integration that outputs a payload in a different format, you need an intermediary service to act as a translation layer to change it to the format Mattermost uses. These intermediary services could be no-code or low-code integrations with n8n, Zapier, or Make, but they could also be pro-code integrations leveraging something like AWS Lambda or other hosted services. 

There’s currently no general standard for webhook communication between services, so translating your webhooks is necessary otherwise Mattermost won't understand the data you're sending.

What are attachments?
----------------------

When "attachments" are mentioned in Mattermost integrations documentation, it refers to Slack's message attachments functionality. These "attachments" can be optionally added as an array in the data sent by an integration, and are used to customize the formatting of the message.

Mattermost doesn't currently support the ability to attach files to a post made via webhook. You can use the API to attach files to a message if needed. 

Where can I find existing integrations?
---------------------------------------

Visit the `Mattermost Marketplace <https://mattermost.com/marketplace>`__ to access open source integrations to common tools like Jira, Jenkins, and GitLab, along with interactive bot applications, and other communication tools that are freely available for use and customization. 

Alternatively, within Mattermost, when logged in as an Administrator, you can click on the "Marketplace" option in the main menu and easily install plugins or apps from there. 

Where should I install my integrations?
----------------------------------------

For self-hosted deployments in small setups, you might host integrations on the same server on which Mattermost is installed. For larger deployments, you can set up a separate server for integrations, or add them to the server on which the external application is hosted. 

For example, if you're self-hosting a Jira server you could deploy a Jira integration on the Jira server itself. When self-hosting restrictions are less strict, AWS, Heroku, and other public cloud options could also be used.

Where can I get more information about integrations?
-----------------------------------------------------

Join our `Developers channel <https://community.mattermost.com/core/channels/developers>`_  on the Mattermost Community server  for technical discussions, and visit our `Integrations channel <https://community.mattermost.com/core/channels/integrations>`_ for all integrations and plugins discussions.

Can I use webhooks to be notified when new integrations are available on the Mattermost Marketplace?
-----------------------------------------------------------------------------------------------------

Yes! A `bash script <https://gist.github.com/mickmister/543a49584146af18ba5e5f82dd86ea93>`_ is available that checks for new integrations in the Mattermost Marketplace, and triggers a post through a Mattermost `incoming webhook <https://developers.mattermost.com/integrate/webhooks/incoming/>`_ request. The script downloads the latest listing, compares it with a locally stored version of the listing, and, if a new plugin is identified, a notification is pushed to a Mattermost channel.

Can I use Mattermost to add messaging functionality to my proprietary SaaS service?
------------------------------------------------------------------------------------

Mattermost is an open source, self-hosted alternative to proprietary SaaS services that lock in the data of users and customers.

While you're welcome to use the Mattermost source code under its open source license, Mattermost, Inc. does not offer support or technical advice for proprietary SaaS projects that result in customers potentially being paywalled from their data should they stop paying SaaS fees.

To learn more about why we strongly believe that users and customers should always have access to their data, please read `why we created Mattermost <https://mattermost.com/about-us/>`_.

Can I customize the source code?
--------------------------------

Yes. As an open source project, we support your ability to modify the source code for the server or web app to make changes and customizations to meet your specific needs.

Learn about `forking our open source repositories <https://developers.mattermost.com/integrate/other-integrations/customization/>`_ and `customizing the Mattermost source code <https://developers.mattermost.com/integrate/customization/customization/>`_ for your specific operational needs.