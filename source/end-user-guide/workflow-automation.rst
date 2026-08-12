Workflow Automation
=====================

.. include:: ../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Mattermost Playbooks provides structure, monitoring and automation for repeatable, team-based processes integrated with the Mattermost platform. Playbooks are :doc:`configurable checklists </end-user-guide/workflow-automation/work-with-tasks>` for teams to achieve :doc:`specific and predictable outcomes </end-user-guide/workflow-automation/metrics-and-goals>`, such as incident response, software release management, and logistical operations. 

From Mattermost v11.1, Entry, Enterprise, and Enterprise Advanced customers can enable adaptive, conditional workflows responding in real time to changing mission or operational context. Admins can define attributes such as severity, category, or linked ticket ID, and use those attributes to hide or show tasks depending on the values of these attributes which can be seen and modified during a playbook run. Learn more about :ref:`playbook attributes <end-user-guide/workflow-automation/work-with-playbooks:playbook attributes>` and :ref:`conditional playbook tasks <end-user-guide/workflow-automation/work-with-tasks:conditional tasks>`.

While Playbooks primarily focus on coordinating people and tasks, they also have integration points. You can trigger a playbook run via an incoming webhook, allowing an external tool to trigger a playbook run. Within a playbook, you can define steps that execute webhooks or call external APIs. Additionally, playbooks can work in conjunction with plugins, keeping the entire workflow visible in Mattermost, and reducing the need to switch between apps during critical processes.

.. toctree::
   :maxdepth: 1
   :hidden:
   :titlesonly:

   Learn about collaborative playbooks </end-user-guide/workflow-automation/learn-about-playbooks>
   Work with collaborative playbooks </end-user-guide/workflow-automation/work-with-playbooks>
   Work with runs </end-user-guide/workflow-automation/work-with-runs>
   Work with tasks </end-user-guide/workflow-automation/work-with-tasks>
   Work with notifications and updates </end-user-guide/workflow-automation/notifications-and-updates>
   Work with metrics and goals </end-user-guide/workflow-automation/metrics-and-goals>
   Share and collaborate </end-user-guide/workflow-automation/share-and-collaborate>
   Interact with collaborative playbooks </end-user-guide/workflow-automation/interact-with-playbooks>

Playbooks monitor channels for keywords or user actions to trigger a structured process, which brings up a set of individual or shared tasks, each associated with manual or automated actions. As playbooks are executed, some may have requirements for :doc:`broadcasting status updates to stakeholders </end-user-guide/workflow-automation/notifications-and-updates>` at regular intervals, to populate workflow dashboards by conducting :ref:`retrospectives <end-user-guide/workflow-automation/metrics-and-goals:configure retrospectives before a run>` after the core process is complete, or other customer requirements as exit criteria for a :doc:`playbook “run” </end-user-guide/workflow-automation/work-with-runs>`. 

:doc:`Advanced permissions </end-user-guide/workflow-automation/share-and-collaborate>` are also available to delegate and manage playbook controls in larger organizations.

.. image:: ../images/Playbooks_Hero.png
   :alt: An example of the collaborative playbooks screen that includes active run details in the right-hand pane.

Configuration
--------------

Playbooks comes pre-packaged, installed, and enabled with Mattermost server.

Access
------

.. tab:: Web and Desktop

   Access playbooks using a web browser or the desktop app by selecting the product menu located in the top-left corner of the Mattermost interface and then selecting **Playbooks**.

.. tab:: Mobile

   From Mattermost v11.0 and mobile app v2.34.0, mobile users can:

   - **Post status updates directly from mobile**: When you open a playbook run on mobile, a new status update button allows you to post progress updates and share status with your team while on the move or in the field.
   - **Create and manage playbook runs** for operational command at the edge.

   From Mattermost v11 and mobile app v2.32.0, mobile users can access playbooks from the mobile app to :ref:`interact with playbook tasks <end-user-guide/workflow-automation/work-with-tasks:interact with playbook tasks>` and :ref:`update tasks <end-user-guide/workflow-automation/work-with-tasks:update tasks>`.

   From Mattermost v10.11 and mobile app v2.31.0, mobile users can access playbooks from the mobile app in read-only mode. :ref:`Playbooks slash commands <end-user-guide/workflow-automation/interact-with-playbooks:slash commands>` are supported in the mobile app, but actions like starting runs or updating checklists aren't available through the mobile interface.

Usage
-----

Use collaborative playbooks to orchestrate prescribed workflows and define, streamline, and document complex, recurring operations, and help your organization stay in command with integrated communication, collaboration, and status dashboards managing your workflow life cycles.

Try it yourself!
~~~~~~~~~~~~~~~~

Walk through our `Incident Response playbook demonstration <https://mattermost.com/demo/playbooks-incident-response/>`__ to see what you can do with playbooks.

Learn more
----------

This end user documentation is for anyone who wants guidance on building repeatable processes in Mattermost.

- :doc:`Overview </end-user-guide/workflow-automation/learn-about-playbooks>` - Learn what collaborative playbooks are and how they're used.
- :doc:`Work with collaborative playbooks </end-user-guide/workflow-automation/work-with-playbooks>` - Customize a playbook for successful runs.
- :doc:`Work with runs </end-user-guide/workflow-automation/work-with-runs>` - Edit triggers and actions in an active run.
- :doc:`Work with tasks </end-user-guide/workflow-automation/work-with-tasks>` - Work with tasks and the task inbox.
- :doc:`Work with notifications and updates </end-user-guide/workflow-automation/notifications-and-updates>` - Keep track of all your active runs and tasks.
- :doc:`Work with metrics and goals </end-user-guide/workflow-automation/metrics-and-goals>` - Unlock insights about the performance of collaborative workflows across organizations with workflow dashboards.
- :doc:`Share and collaborate </end-user-guide/workflow-automation/share-and-collaborate>` - Reuse and share collaborative playbooks with your organization.
- :doc:`Interact with collaborative playbooks </end-user-guide/workflow-automation/interact-with-playbooks>` - Interact with collaborative playbooks using slash commands and the REST API. 
