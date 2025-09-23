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
   workflow-orchestration-platforms
   faq

Mattermost provides a variety of methods to integrate with your favorite tools, automate critical workflows, and extend the capabilities of the platform. This guide provides a high-level overview of integration options and the level of technical skills required :ref:`(no-code, low-code, or pro-code) <integrations-guide/faq:what is meant by no-code, low-code, and pro-code?>`, and links to detailed documentation for each.

Choose your path
-----------------

.. list-table::
   :header-rows: 1
   :widths: 20 40 40

   * - **Skill Level**
     - **Best Options**
     - **Examples**
   * - **No-code**
     - :doc:`Pre-built plugins </integrations-guide/popular-integrations>`, :doc:`Playbooks </end-user-guide/workflow-automation>`, :doc:`Workflow orchestration platforms </integrations-guide/workflow-orchestration-platforms>`
     - Connect Jira, GitHub, Zoom. Run incident playbooks. Automate with Zapier.
   * - **Low-code**
     - :doc:`Webhooks </integrations-guide/webhook-integrations>`, :ref:`custom slash commands <integrations-guide/slash-commands:custom slash commands>`
     - Send alerts from monitoring tools, trigger actions with keywords, fetch docs with ``/search``.
   * - **Pro-code**
     - :doc:`REST API </integrations-guide/restful-api>`, :doc:`custom plugins </integrations-guide/plugins>`
     - Build custom apps, automate provisioning, extend Mattermost core.

Integration options
--------------------

Plugins
~~~~~~~~

Install pre-built plugins or create your own for deeper customization. Learn more about :doc:`Mattermost plugins </integrations-guide/plugins>`.

Webhooks
~~~~~~~~

Send or receive real-time data from external tools. Webhooks require minimal coding and are easy to set up with virtually any tool or platform because they use lightweight HTTP POST requests with JSON payloads.

- :doc:`Incoming webhooks </integrations-guide/incoming-webhooks>` push alerts and notifications into channels.
- :doc:`Outgoing webhooks </integrations-guide/outgoing-webhooks>` trigger actions when keywords are typed.

Additionally, Mattermost webhook payloads are :ref:`fully compatible <integrations-guide/incoming-webhooks:slack compatibility>` with Slack’s webhook format to make migration easier.

Learn more about :doc:`Mattermost webhooks </integrations-guide/webhook-integrations>`.

Slash Commands
~~~~~~~~~~~~~~

Execute actions with simple commands inside Mattermost. Learn more about :doc:`Mattermost slash commands </integrations-guide/slash-commands>`.

RESTful API
~~~~~~~~~~~

Full developer control for automation, bots, and integrations. Learn more about the :doc:`Mattermost RESTful API </integrations-guide/restful-api>`.

Mattermost Playbooks
~~~~~~~~~~~~~~~~~~~~

**Technical complexity: No-code**

:doc:`Mattermost Playbooks </end-user-guide/workflow-automation>` lets you define and execute repeatable processes without any coding. Playbooks are often used for incident response, onboarding checklists, or any workflow that involves multiple steps, owners, and notifications. With Playbooks, you can automate certain actions in the process. For instance, a playbook can be configured to automatically open a dedicated channel for an incident, send template messages or task checklists to that channel, update subscribers on status changes, and so on, all through configuration.

While Playbooks primarily focus on coordinating people and tasks, they also have integration points. You can trigger a playbook run via an incoming webhook (allowing an external tool to trigger a playbook run), and within a playbook you can define steps that execute webhooks or call external APIs. Additionally, Playbooks can work in conjunction with plugins, making them a powerful no-code automation tool for orchestrating both human and system actions. It keeps the entire workflow visible in Mattermost, reducing the need to switch between apps during critical processes.

Learn more about using :doc:`Playbooks </end-user-guide/workflow-automation>`.

Build and automate workflows
-----------------------------

In addition to direct tool integrations, Mattermost can be part of larger automated workflows across your integrated services. The options below let you automate multi-step processes across Mattermost and other systems, often with no coding required.

Learn more about :doc:`workflow orchestration platforms for Mattermost </integrations-guide/workflow-orchestration-platforms>`.

Frequently asked questions
--------------------------

Have questions about coding levels, Slack compatibility, or setup options? Visit the :doc:`Integrations FAQ </integrations-guide/faq>`.