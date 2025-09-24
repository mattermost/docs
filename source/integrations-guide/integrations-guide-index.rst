Integrations Guide
=====================

.. toctree::
   :maxdepth: 1
   :hidden:
   :titlesonly:

   plugins
   webhook-integrations
   slash-commands
   restful-api
   no-code-automation
   faq

Mattermost provides a variety of methods to integrate with your favorite tools, automate critical workflows, and extend the capabilities of the platform. This guide provides a high-level overview of integration options and the level of technical skills required :ref:`(no-code, low-code, or pro-code) <integrations-guide/faq:what is meant by no-code, low-code, and pro-code?>`, and links to detailed documentation for each.

Choose Your Path
-----------------

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - **Skill Level**
     - **Best Options**
     - **Examples**
   * - :ref:`No-code <no-code>`
     - :doc:`Pre-built plugins </integrations-guide/popular-integrations>`, :doc:`No-code automation </integrations-guide/no-code-automation>`
     - Connect Jira, GitHub, Zoom. Run incident playbooks. Automate with Zapier.
   * - :ref:`Low-code <low-code>`
     - :doc:`Webhooks </integrations-guide/webhook-integrations>`, :ref:`custom slash commands <integrations-guide/slash-commands:custom slash commands>`
     - Send alerts from monitoring tools, trigger actions with keywords, fetch docs with ``/search``.
   * - :ref:`Pro-code <pro-code>`
     - :doc:`REST API </integrations-guide/restful-api>`, :ref:`custom plugins <integrations-guide/plugins:custom-built plugins>`
     - Build custom apps, automate provisioning, extend Mattermost core.

Integration Options
--------------------

Plugins
~~~~~~~~

Learn more about :doc:`Mattermost plugins </integrations-guide/plugins>`.

Pre-Built Plugins
^^^^^^^^^^^^^^^^^

**Technical complexity:** :ref:`No-code <no-code>`

Mattermost provides a set of pre-built plugins that require no coding to install, configure, and use. These plugins are installed and managed entirely through the System Console, where you can enable, configure, and customize settings without any development work.

.. image:: ../images/prebuilt-integrations.png
  :alt: Pre-built plugins available for no-code integration
  :width: 800

Custom-Built Plugins
^^^^^^^^^^^^^^^^^^^^

**Technical complexity:** :ref:`Pro-code <pro-code>`

Custom built plugins are the most comprehensive way to add new features and customization to self-hosted Mattermost deployments. Custom plugins are ideal for customers wanting to change the behavior of the Mattermost server, desktop, and web apps without forking the core codebase to suit their organization’s needs.

Building a custom plugin is a **software development** task, using ``Go`` for the server-side functionality and optionally ``TypeScript/React`` for UI components. 

Webhooks
~~~~~~~~

Learn more about :doc:`Mattermost webhooks </integrations-guide/webhook-integrations>`.

Incoming Webhooks
^^^^^^^^^^^^^^^^^^

**Technical complexity:** :ref:`No-code <no-code>`

:doc:`Incoming webhooks </integrations-guide/incoming-webhooks>` allow external applications to post messages into Mattermost channels and direct messages. They are a simple way to receive notifications and data from other services in real-time and require only basic setup.

Outgoing Webhooks
^^^^^^^^^^^^^^^^^^

**Technical complexity:** :ref:`Low-code <low-code>`

:doc:`Outgoing webhooks </integrations-guide/outgoing-webhooks>` allow Mattermost to send messages and trigger actions in external applications when specific keywords are typed in channels. They are a straightforward way to connect Mattermost conversations to other services and automate responses. Outgoing webhooks require no coding to configure in Mattermost. Some light coding is required to parse the request from the external service and format a JSON response payload.

Outgoing webhooks can be used to create rich, interactive experiences in Mattermost by letting external services respond with rich message attachments, such as structured fields, buttons, and menus. Additionally, these responses can trigger interactive dialog forms where users provide additional input directly in Mattermost, or interactive messages that update dynamically based on user actions. Together, these capabilities turn simple keyword triggers into powerful in-product workflows that streamline how teams interact with external systems, all with minimal coding required. 

Additionally, Mattermost webhook payloads are :ref:`fully compatible <integrations-guide/incoming-webhooks:slack compatibility>` with Slack’s webhook format to make migration easier.

Slash Commands
~~~~~~~~~~~~~~

Learn more about :doc:`Mattermost slash commands </integrations-guide/slash-commands>`.

Built-In Slash Commands
^^^^^^^^^^^^^^^^^^^^^^^^

**Technical complexity:** :ref:`No-code <no-code>`

Out-of-the-box commands enable command line interaction with users, channels, and conversations.

Custom Slash Commands
^^^^^^^^^^^^^^^^^^^^^^

**Technical complexity:** :ref:`Low-code <low-code>`

You can create custom slash commands that run preconfigured commands that can return a response, such as plain text, rich message content, interactive buttons or forms, directly into a channel.

RESTful API
~~~~~~~~~~~

Full developer control for automation, bots, and integrations. Learn more about the :doc:`Mattermost RESTful API </integrations-guide/restful-api>`.

Build and Automate Workflows
-----------------------------

**Technical complexity:** :ref:`No-code <no-code>`

In addition to direct tool integrations, Mattermost can be part of larger automated workflows across your integrated services. Automate multi-step processes across Mattermost and other systems, often with no coding required.

Mattermost Playbooks
~~~~~~~~~~~~~~~~~~~~

:doc:`Mattermost Playbooks </end-user-guide/workflow-automation>` lets you define and execute repeatable processes without any coding. Playbooks are often used for incident response, onboarding checklists, or any workflow that involves multiple steps, owners, and notifications. With Playbooks, you can automate certain actions in the process. For instance, a playbook can be configured to automatically open a dedicated channel for an incident, send template messages or task checklists to that channel, update subscribers on status changes, and so on, all through configuration.

While Playbooks primarily focus on coordinating people and tasks, they also have integration points. You can trigger a playbook run via an incoming webhook (allowing an external tool to trigger a playbook run), and within a playbook you can define steps that execute webhooks or call external APIs. Additionally, Playbooks can work in conjunction with plugins, making them a powerful no-code automation tool for orchestrating both human and system actions. It keeps the entire workflow visible in Mattermost, reducing the need to switch between apps during critical processes. Learn more about using :doc:`Playbooks </end-user-guide/workflow-automation>`.

Learn more about additional :doc:`no-code automation options </integrations-guide/no-code-automation>` available in Mattermost.

Frequently Asked Questions
--------------------------

Have questions about coding levels, Slack compatibility, or setup options? Visit the :doc:`Integrations FAQ </integrations-guide/faq>`.