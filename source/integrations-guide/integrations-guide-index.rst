Integrations Guide
=====================

.. toctree::
   :maxdepth: 1
   :hidden:
   :titlesonly:

   popular-integrations
   run-slash-commands
   webhook-integrations

Mattermost provides a variety of methods to integrate with your favorite tools, automate critical workflows, and extend the capabilities of the platform. This guide provides a high-level overview of integration options and the level of technical skills required (no-code, low-code, or pro-code), and links to detailed documentation for each.


Connect your tools
__________________

Out of the box, you can connect with many popular tools without writing any code, and for deeper customization you can extend Mattermost with slash commands, webhooks, bots and API access.


Plugins
~~~~~~~


Pre-built plugins
^^^^^^^^^^^^^^^^^
**Technical complexity: No-code**

Mattermost provides a set of pre-built plugins that require no coding to install, configure and use. These plugins are installed and managed entirely through the System Console, where you can enable, configure, and customize settings without any development work, making it simple for teams to extend Mattermost with powerful integrations for project management, incident response, monitoring, and collaboration. With simple configuration steps, you can quickly connect Mattermost to widely used tools such as Jira, GitHub, GitLab, Zoom, ServiceNow and others, enabling powerful integrations that enhance collaboration and streamline workflows out of the box.

Learn more about what popular pre-built integrations are available and how to install them `here <https://developers.mattermost.com/integrate/plugins/>`_.



.. image:: ../images/prebuilt-integrations.png
  :alt: Pre-built plugins available for no-code integration
  :width: 800

.. note::
The `Mattermost Marketplace <https://mattermost.com/marketplace/>`_ offers an expanded selection of community supported integrations. 


Custom-built plugins
^^^^^^^^^^^^^^^^^^^^

**Technical complexity: Pro-code**

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:


Custom built plugins are the most comprehensive way to add new features and customization to self-hosted Mattermost deployments. Custom plugins are ideal for customers wanting to change the behavior of the Mattermost server, desktop, and web apps without forking the core codebase to suit their organization’s needs.

Building a custom plugin is a **software development** task, using ``Go`` for the server-side functionality and optionally ``TypeScript/React`` for UI components. Developers should be comfortable with Git, modern build tooling, and the `Mattermost Plugin API <https://developers.mattermost.com/integrate/reference/server/server-reference/>`_, including lifecycle hooks, KV storage, slash commands, and interactivity. Knowledge of testing, logging, and security best practices is essential for production-ready plugins, along with experience packaging and deploying plugins through the System Console or CLI. For teams without these skills, simpler options like webhooks, slash commands, or no-code workflow tools may be more practical.

Plugins can authenticate and interact with Mattermost through `bot accounts <https://developers.mattermost.com/integrate/reference/bot-accounts/>`_, utilizing the `RESTful API <https://developers.mattermost.com/api-documentation/>`_.


Learn more about building your own plugin `here <https://developers.mattermost.com/integrate/plugins/>`_.


Webhooks
~~~~~~~~

Webhooks enable Mattermost to send and receive real-time data between your workspace and external applications. Webhooks require minimal coding and are easy to set up with virtually any tool or platform because they use lightweight HTTP POST requests with JSON payloads.

Additionally, Mattermost webhook payloads are `fully compatible <https://docs.mattermost.com/integrations-guide/incoming-webhooks.html#slack-compatibility>`_ with Slack’s webhook format to make migration easier.

Incoming Webhooks
^^^^^^^^^^^^^^^^^
**Technical complexity: No-code**

Incoming webhooks allow external applications to post messages into Mattermost channels and direct messages. They are a simple way to receive notifications and data from other services in real-time.


Using incoming webhooks in Mattermost requires only basic setup. You generate a webhook URL using the Mattermost interface, then point another service to send data to that address. No coding is required if your external service triggering the events is able to send data via webhooks or HTTP POST requests, which most modern applications and platforms support. Setting this up usually involves pasting the Mattermost webhook URL into the service’s settings and selecting what type of events you want it to send. 

Learn more about incoming webhooks `here <https://docs.mattermost.com/integrations-guide/incoming-webhooks.html>`_.


**Examples**

Here are some example use cases for incoming webhooks in Mattermost:

- **Monitoring alerts**  
   Send real-time alerts from monitoring systems (such as Prometheus or Datadog) into a dedicated Mattermost channel so your team is immediately notified about system issues or downtime.

- **Build and deployment notifications**  
   Post automated updates from CI/CD pipelines (such as Jenkins or GitLab CI) to a channel, keeping developers informed of build status, test results, and deployment progress.

- **Customer support updates**  
   Forward new support ticket notifications from systems like Zendesk or ServiceNow into a support channel, ensuring the team can respond quickly to incoming requests.



Outgoing Webhooks
^^^^^^^^^^^^^^^^^
**Technical complexity: Low-code**


Outgoing webhooks allow Mattermost to send messages and trigger actions in external applications when specific keywords are typed in channels. They are a straightforward way to connect Mattermost conversations to other services and automate responses.


Outgoing webhooks require no coding to configure on in Mattermost, however the external service that receives the HTTP POST request needs to process the data, and then format and send a respond with a message back to Mattermost. This usually requires light coding to parse the request and format a JSON response payload, though many `automation platforms <https://docs.mattermost.com/integrations-guide/integrations-guide-index.html#build-and-automate-workflows>`_ handle this without writing custom code.

Outgoing webhooks can be used to create rich, interactive experiences in Mattermost by letting external services respond with rich message attachments, such as structured fields, buttons, and menus. Additionally, these responses can trigger interactive dialog forms where users provide additional input directly in Mattermost, or interactive messages that update dynamically based on user actions. Together, these capabilities turn simple keyword triggers into powerful in-product workflows that streamline how teams interact with external systems - all with minimal coding required. 


Learn more about outgoing webhooks `here <https://docs.mattermost.com/integrations-guide/outgoing-webhooks.html>`_.


**Examples**

Here are some example use cases for outgoing webhooks in Mattermost:

- **Issue tracking integration**  
   When a user types ``bug`` in a channel, an outgoing webhook sends the message to an external service that parses the details and responds with an interactive dialog in Mattermost. The user can enter fields like priority, description, and assignee, and submitting the dialog automatically creates a ticket in your ticketing software.

- **Knowledge base lookup**  
   A keyword like ``docs`` triggers an outgoing webhook that queries a documentation service and returns a rich interactive message with a list of suggested articles, each with clickable buttons or menus. Users can refine their search or open links without leaving Mattermost.

- **Security incident enrichment**  
   Typing a keyword like ``ioc`` (indicator of compromise) in a security channel can trigger an outgoing webhook that queries a threat intelligence platform. The response can return a formatted message attachment with reputation scores, related incidents, and quick-action buttons for escalating, investigating, or dismissing the alert.



Slash Commands
~~~~~~~~~~~~~~
Slash commands in Mattermost let users trigger actions or retrieve information from external systems by typing simple commands directly into the message input box, making it easy to extend workflows without leaving the conversation. Mattermost offers a selection of pre-build slash commands for common actions within the platform, as well as the ability to create custom slash commands that trigger actions and responses in external services. 


Pre-built slash commands
^^^^^^^^^^^^^^^^^^^^^^^^
**Technical complexity: No-code**

These out-of-the-box commands enable command line interaction with users, channels, and conversations. Examples include Examples of pre-built slash commands include ``/invite`` to add teammates to a channel, ``/header`` to set a channel description, or ``/call`` to start or join a call in a channel.

Learn more about pre-built slash commands `here <https://docs.mattermost.com/integrations-guide/built-in-slash-commands.html>`_.


Custom slash commands
^^^^^^^^^^^^^^^^^^^^^
**Technical complexity: Low-code**


Slash commands are similar to an outgoing webhooks, but instead of listening for keywords in a channel they are triggered by users explicitly typing a preconfigured command. Using slash commands is similar to using a command line within a channel - this means if you type in a slash command it will execute without posting a message, whereas an outgoing webhook is only triggered by posted messages. The external service then processes the request and can return a response, such as plain text, rich message content, interactive buttons or forms, directly into the channel.

Mattermost's slash command format is Slack compatible, so you can easily migrate your commands from Slack.


Learn more about building custom slash commands `here <https://developers.mattermost.com/integrate/slash-commands/custom/>`_.


**Examples**

Here are some example use cases for slash commands in Mattermost:

- **Project management**  
   Typing ``/jira create`` opens an interactive dialog where you can file a new Jira issue directly from Mattermost, including fields like summary, description, and priority.

- **Incident response**  
   Using ``/pagerduty trigger`` can open a form to start a new incident, notify on-call responders, and post details back into the channel so the team can coordinate.

- **Knowledge retrieval**  
   A command like ``/docs search authentication`` queries your documentation system and returns a list of relevant articles as interactive message attachments with links.



RESTful API
~~~~~~~~~~~

**Technical complexity: Pro-code**

The `Mattermost API <https://developers.mattermost.com/api-documentation/>`_ provides a comprehensive set of endpoints that let you programmatically interact with your Mattermost workspace. With the API, you can manage users, teams, channels, posts, and more, making it possible to automate administrative tasks, integrate external systems, and build custom applications that extend Mattermost functionality. Whether you’re writing lightweight scripts or developing full-scale integrations, the API offers flexible building blocks to tailor Mattermost to your workflows.

Using the API is a pro-code approach meant for developers who want to write scripts to automate specific workflows or build deeply customized integrations using the plugin framework to connect external systems. 

The API is often used in combination with `bot accounts <https://developers.mattermost.com/integrate/reference/bot-accounts/>`_ to authenticate and interact with Mattermost.

**Examples**

Here are some example use cases for API integration in Mattermost:

- **User provisioning**  
   Write a script to automatically create and manage user accounts in Mattermost, ensuring that new team members are added to the right teams and channels as part of your onboarding process.

- **Channel management**  
   Use the API to programmatically create, archive, or update channels, making it easy to align collaboration spaces with your project lifecycle or organizational changes.

- **Message automation**  
   Build a script or integration that posts messages or reminders into specific channels on a schedule, such as daily stand-up prompts, release announcements, or security notifications.


Learn more about using the API and available endpoints `here <https://developers.mattermost.com/api-documentation/>`_.





Build and automate workflows
____________________________


In addition to direct tool integrations, Mattermost can be part of larger automated workflows across your integrated services. The options below let you automate multi-step processes across Mattermost and other systems, often with no coding required.


Workflow orchestration platforms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Technical complexity: No-code**

Platforms like n8n, Zapier, or Make provide powerful visual editors that support wthousands of connected tools, with triggers and actions that integrate Mattermost to external services, enabling teams to build complex workflows without writing code. Admins migrating from tools like Slack Workflow Builder can recreate familiar automations in Mattermost using these platforms.

When used in comination with outgoing webhooks or custom slash commands, users can trigger complex workflows and automations without leaving Mattermost. By pointing a webhook or slash command at the unique URL these automation tools provide, any message or keyword in Mattermost can initiate a workflow. This allows you to capture context from conversations and pass it into external systems — for example, creating tickets, updating records, or starting multi-step automations.

Choosing the best platform for your team depends on your specific integration requirements, hosting preferences, and technical capabilities. Learn more about the capabilities of each platform below:  


.. tab:: n8n
  :parse-titles:

  
  `n8n <https://n8n.io/>`_ is ideal for organizations prioritizing data residency and security, since it is self-hosted and can be supported in air-gapped environments where cloud solutions like Zapier and Make might not be feasible. 

  Additonally, n8n supports both no-code and low-code approaches, making it flexible for technical and semi-technical users. Being open source means there’s a large community of people sharing their custom workflows and automations that can either be used directly or iterated on to meet your specific requirements.


  **Supported Triggers**

  - MattermostTrigger (community node): Listens for Mattermost events via WebSocket events, such as new post and users added.

  You can also use outgoing webhooks or slash commands in Mattermost as triggers using the `Webhook node <https://n8n.io/integrations/webhook/>`_.
 

  **Supported Actions**

  - Channels
    - Add a user to a channel
    - Create a new channel
    - Soft delete a channel

    - Restore a soft deleted channel
    - Get statistics for a channel

  - Messages
    - Post a message into a channel
    - Post an ephemeral message into a channel
    - Soft delete a post

  - Reactionss
    - Add a reaction to a post
    - Remove a reaction from a post
    - Get all reactions to one or more posts

  - Users
    - Create a new user
    - Deactivate a user (archive, revoke sessions)
    - Invite user to a team

  **Supported Searches**

  - Search for a channel 
  - Get a user by email  
  - Get a user by ID
  - Retrieve all users
  - Retrieve members of a channel


  Explore building workflows with the `Mattermost n8n integration <https://n8n.io/integrations/mattermost/>`_.


.. tab:: Make
  :parse-titles:

  Make offers a more visual and flexible approach to automation, allowing you to build complex workflows with advanced logic and data manipulation. Make offers one of the most expansive sets of out-of-the-box triggers and actions for Mattermost. 

  Make is hosted in the cloud, and excels at more complex multi-step workflows while still keeping the configuration non-technical.


  **Supported Triggers**

  - Watch New Posts: Fires when a new post is added.
  - Watch New Posts Pinned for a Channel: Fires when a post is pinned in a channel.
  - Watch New Users: Fires when a new user is added.

  **Supported Actions**

  - Add a User to a Team: Add a user into a specific team.
  - Check if the Team Exists: Verify whether a team exists by name.
  - Create a Command: Add a custom command within a team.
  - Create a New User: Create a user account on the Mattermost system.
  - Create a Post: Post a message in a channel.
  - Deactivate a User Account: Archive or disable a user account.
  - Delete a Command: Remove a command by its ID.
  - Delete a Post: Remove a post.
  - Execute a Command: Run or trigger an existing command.

  You can also use outgoing webhooks or slash commands in Mattermost as triggers using the `Webhook app <https://www.make.com/en/integrations/gateway>`_.

  **Supported Searches**

  - Get a Channel: Retrieve a channel by its ID.
  - Get a Post: Retrieve a post by its ID.
  - Get a File: Retrieve an uploaded file by its ID.
  - Get a User: Retrieve a user by their user ID.
  - Get a Team by Name: Retrieve team information by team name.


  Explore building workflows with the `Mattermost Make integration <https://www.make.com/en/integrations/mattermost>`_.


.. tab:: Zapier
  :parse-titles:

  Zapier is ideal for non-technical users who want the fastest path to connect Mattermost with over 7000+ SaaS apps. It’s hosted in the cloud, easy to set up, and best for common business workflows.

  Zapier’s strength is the breadth of integrations. Without coding, you can integrate Mattermost with everything from CRMs to social media. This is perfect for non-technical users who want to automate notifications or routine tasks, such as posting daily reports or sending Mattermost channel messages when forms are submitted. Zapier provides a user-friendly wizard and template library to get started quickly.

  **Supported Triggers**
  - Zapier does not natively support triggers in Mattermost. If you want Mattermost to trigger a Zapier workflow, you can use outgoing webhooks or slash commands in combination with `Zapier’s Webhooks trigger <https://zapier.com/apps/webhook/integrations> _. For example, you could configure an outgoing webhook in Mattermost to hit Zapier when a certain keyword is posted, which Zapier treats as a trigger to then perform actions in other apps.

  **Supported Actions**
  - Compared with the wide range of triggers and actions supported by n8n or Make, Zapier supports only one action - posting a message. 


  Explore building workflows with the `Mattermost Zapier integration <https://n8n.io/integrations/mattermost/>`_.


Mattermost Playbooks
~~~~~~~~~~~~~~~~~~~~
**Technical complexity: No-code**

`Mattermost Playbooks <https://docs.mattermost.com/end-user-guide/workflow-automation.html>`_ is a pre-built plugin in Mattermost that lets you define and execute repeatable processes without any coding. Playbooks are often used for incident response, onboarding checklists, or any workflow that involves multiple steps, owners, and notifications. With Playbooks, you can automate certain actions in the process. For instance, a playbook can be configured to automatically open a dedicated channel for an incident, send template messages or task checklists to that channel, update subscribers on status changes, and so on, all through configuration.

While Playbooks primarily focus on coordinating people and tasks, they also have integration points. You can trigger a playbook run via an incoming webhook (allowing an external tool to trigger a playbook run), and within a playbook you can define steps that execute webhooks or call external APIs. Additionally, Playbooks can work in conjunction with plugins, making them a powerful no-code automation tool for orchestrating both human and system actions. It keeps the entire workflow visible in Mattermost, reducing the need to switch between apps during critical processes.

Learn more about using Playbooks `here <https://docs.mattermost.com/end-user-guide/workflow-automation.html>`_.


Frequently Asked Questions
__________________________

What is meant by **no-code**, **low-code**, and **pro-code**?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **No-code**: Integration or automation can be achieved without writing any code. All configuration is done via user-friendly interfaces or by installing pre-made components. This is ideal for non-technical users or admins – for example, installing a plugin from the marketplace or using a drag-and-drop automation tool would be considered no-code. The heavy lifting is pre-built and you just need to configure it.

- **Low-code**: Minimal coding or scripting is needed to implement the integration. Low-code solutions might require writing a few lines of script or simple configuration in code-like logic, but not building a full software application. In Mattermost’s context, something like setting up a webhook with a small custom script, or tweaking an automation template would be considered low-code. It typically assumes some technical knowledge, but far less than full-scale development. Utilizing templates or online AI tooling can likely meet the need for most low-code integration requirements.

- **Pro-code**: These kinds of integrations require a professional software developer to write code and sometimes build underlying infrastructure. These integrations offer maximum flexibility at the cost of technical complexity, for example building a custom Mattermost plugin or writing a complex bot program using the Mattermost API in a custom application. Pro-code integrations are essentially software projects – you’ll use developer tools, work with source code, and follow software development practices to build and maintain them.


What does Slack-compatible mean?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Slack compatible means that Mattermost accepts integrations that have a payload in the same format as Slack's legacy "Message Attachment" payload. If you have a Slack integration, you should be able to set it up in Mattermost without changing the format of the message being sent over.   

What if I have a webhook from somewhere other than Slack?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have an integration that outputs a payload in a different format, you need to write an intermediate application, such as N8N.io, Zapier, or Make, to act as a translation layer to change it to the format Mattermost uses. Since there’s currently no general standard for webhook formatting, this is unavoidable and just a part of how webhooks work.

If there's no translation layer, Mattermost won't understand the data you're sending.

What are attachments?
~~~~~~~~~~~~~~~~~~~~~

When "attachments" are mentioned in Mattermost integrations documentation, it refers to Slack's message attachments functionality. These "attachments" can be optionally added as an array in the data sent by an integration, and are used to customize the formatting of the message.

Mattermost doesn't currently support the ability to attach files to a post made via webhook. You can use the API to attach files to a message if needed. 

Where can I find existing integrations?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


Can I use Mattermost to add messaging functionality to my proprietary SaaS service?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost is an open source, self-hosted alternative to proprietary SaaS services that lock in the data of users and customers.

While you're welcome to use the Mattermost source code under its open source license, Mattermost, Inc. does not offer support or technical advice for proprietary SaaS projects that result in customers potentially being paywalled from their data should they stop paying SaaS fees.

To learn more about why we strongly believe that users and customers should always have access to their data, please read `why we created Mattermost <https://mattermost.com/about-us/>`_.


Source Code Customizations
--------------------------

As an open source project, we support your ability to modify the source code for the server or web app to make changes and customizations to meet your specific needs. 

Learn about `forking our open source repositories <https://developers.mattermost.com/integrate/other-integrations/customization/>`_ and `customizing the Mattermost source code <https://developers.mattermost.com/integrate/customization/customization/>`__ for your specific operational needs.
