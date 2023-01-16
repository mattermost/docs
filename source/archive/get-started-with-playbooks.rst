Get started with Mattermost Playbooks
=====================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Using a web browser or the desktop app, you can access Mattermost Playbooks by selecting **Playbooks** from the **product menu** |product-list|.

.. |product-list| image:: ../images/products_E82F.svg
  :height: 24px
  :width: 24px
  :alt: Navigate between Channels, Playbooks, and Boards using the Product list icon.

Playbooks are workflows that can be repeated and refined over time. They can be applied to a range of situations and give stakeholders visibility into progress, process, and metrics. Playbooks are configurable and editable. You can add tasks to checklists, include automation behaviors, and provide insights into your processes in the form of metrics.

When you get started with Playbooks, it helps to have a repeatable process in mind up front. As a working example, we'll refer to an incident response playbook and discuss its moving parts.

Visit the `Mattermost Playbooks documentation </playbooks/setting-up-playbooks.html>`_ to learn more.

Choose a template
-----------------

The first step is to choose the right template for your use case. There are pre-configured templates for specific scenarios. The checklists, actions, status updates, and retrospective settings for these templates may already be filled in and, where appropriate, enabled. You can always edit and adjust these settings - they're there to guide you - removing them doesn't negatively affect the playbook run.

.. tip:: 

    Take a look at the **Learn how to use playbooks** template. This template breaks down the components of a playbook and you can also start a test run to see how everything fits together. If you're taking this option, you can stop reading here and enjoy the test run. You can also choose a blank template and start from scratch - this is a good option if your use case is unique.

In the incident response template, the template contains items that are relevant to incident resolution. These are general items to help you get started.

Keywords
--------

It's important to make it easy to start a run. One way to do this is by setting up keywords. These keywords prompt a user to start the run when they're used. In the incident response playbook, the keywords are specific to critical incidents, for example ``sev-1`` and ``#incident``. It's unlikely that someone would use those terms in general conversation and, even if they do, they can elect not to start the playbook run when prompted.

Welcome message
---------------

Create a welcome message so that when members join your run, it's easy for them to see where they're needed and where to find the relevant information. This is especially important during a time-sensitive incident to eliminate confusion and help members ramp up quickly.

Tasks and checklists
--------------------

Tasks and checklists are the foundation of a template and a workflow. In an incident, it's critical to get stakeholders together as soon as possible, so one of the first tasks is to add the on-call engineer to the channel, followed by starting a bridge call. When you're setting up these tasks, you can add slash commands, at-mentions, and integrations with tools such as Zoom to make the initiation as seamless as possible.

Status updates
--------------

Regular updates are important communication tools, especially in the middle of an incident like an outage. Channels can get very busy and overwhelming, and if you have more than one incident at a time, it's often too noisy for stakeholders to keep track of everything.

Use the **Broadcast update to other channels** option to cut through the noise and share critical information with both channel members and other users in a dedicated channel.

Additionally, set a timer that issues a reminder for updates to be shared.

Retrospective
-------------

When an incident is over, create a retrospective that captures the impact of the event. You can also add metrics, such as how long it took to resolve the incident, which you can apply to other, similar incidents to see where you can improve and refine your workflows.
