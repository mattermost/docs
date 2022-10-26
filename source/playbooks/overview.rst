Overview
========

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Mattermost Playbooks is a collaboration tool that defines a repeatable process to enable teams to achieve specific and predictable outcomes. With playbooks, development teams can orchestrate prescribed workflows and define, streamline, and document complex, recurring operations.

Mattermost Playbooks is included in Mattermost self-hosted and Mattermost Cloud workspace. You can access Playbooks via the product menu in the top-left corner of Mattermost.

To find all playbook runs, open **Product menu > Playbooks**, and then select any playbook name. Next, select **Runs** from the navigation bar, then choose a run to view its overview. Select **Go to channel** to open the run’s channel.

Each playbook represents a recurring outcome or specific goal that your teams collaborate on to achieve, such as service outage recovery or customer onboarding. 

Playbooks are made up of:

- **Checklists**: The list of tasks to be completed for the run. `Checklists </playbooks/customize-a-playbook.html#make-checklists>`_ can be edited ad-hoc during a run.
- **Templates**: `Templates </playbooks/overview.html#templates>`_ for frequently-used actions such as updates and reminders. You can create your own templates or use default ones.
- **Actions**: `Automation options </playbooks/customize-a-playbook.html#actions>`_ for inviting members, creating webhooks, editing welcome messages, and more.
- **Permissions**: Manage :doc:`permissions </playbooks/playbook-permissions>` at a channel and a playbook level.

Teams run a playbook every time they want to orchestrate people, tools, and data to achieve that outcome as quickly as possible while providing visibility to stakeholders. 

For participants, it prescribes processes such as task checklists, status updates, and retrospective reports. For integrated tools, it configures the triggers to perform automated actions. And for stakeholders, it provides a single pane of glass for visibility into each run as well as aggregate insights over time.

Playbooks also allow teams to incorporate learnings from the retrospective to tweak and improve the playbook with every iteration.

What’s a playbook?
^^^^^^^^^^^^^^^^^^

A playbook is a checklist of the tasks that make up your processes. These tasks can range from at-mentioning a team member, to using a slash command to start a Zoom call. Tasks can be assigned to users, they can be given due dates.

There are other parts of a playbook, such as automation settings, and metrics. But the very first thing you’ll want to set up is a checklist.

Each time you use the process you’ve documented, such as onboarding a new customer, the playbook is used to start a run - a discrete single use of the process - and that run is captured in a dedicated channel. 

Setting up a playbook includes configuring how the playbook manages the creation of its channel as well as how stakeholders are notified.
To open a playbook and view its statistics, select the playbook name. To begin a run using a specific playbook, select **Run** beside that playbook’s name.

Templates
~~~~~~~~~

Creating a playbook from scratch can be daunting, even if you have the process mapped out. One way to get started quickly is to use one of the pre-configured templates available. These templates are populated with content and settings to provide guidance and are customizable.

Playbook templates are basic workflows that you can use to get started quickly. As you learn more about your workflows, you can customize them into specific playbooks.

What’s a run?
^^^^^^^^^^^^^

To access runs, select the product menu in the top-left corner of Mattermost, then select **Playbooks**. In the runs list, you can select a run to view more details, such as the overview and retrospective. This is an easy way to assess all the active runs to which you have access.

View run details
~~~~~~~~~~~~~~~~

When you’re in a channel with an active run, select the **Toggle Run Details** icon in the channel header to open the right-hand pane to view the run details. Information such as run name and description can be edited in-line, and the checklists can be collapsed and filtered based on their status.
