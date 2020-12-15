Mattermost Incident Management
==============================

*Available in Mattermost Enterprise Edition E20, Mattermost Cloud Professional, and Mattermost Cloud Enterprise.*

Incidents are situations which require an immediate response and benefit from a clearly defined process guiding towards resolution. Mattermost Incident Management allows your team to coordinate, manage, and resolve incidents from within Mattermost. 

Better response to an incident helps you provide more reliable services, in addition to gaining insights with incident reports and incorporating learnings with playbooks.

- Automatically create a new channel that can be organized in the left-hand sidebar using custom categories.
- Use playbooks to perform automated actions such as create a Jira ticket, start a Zoom call, or find out who is on-call in Opsgenie.
- Iterate on and refine processes after each incident.

When incidents are monitored, coordinated, and measured effectively, you can add transparency, maximize effectiveness, and save costs by cutting down time taken to respond to and resolve incidents.

.. contents::
  :depth: 1
  :local:
  :backlinks: entry
  
API Documentation
-----------------

The Mattermost Incident Management API specification is available `here <https://github.com/mattermost/mattermost-plugin-incident-management/blob/master/server/api/api.yaml>`_.

Installing Mattermost Incident Management
-----------------------------------------

*For self-managed deployments*

Mattermost Incident Management is available in the Plugin Marketplace. You can download and install the plugin from Mattermost.

1. Open **System Console > Plugin Management**.
2. Search for **Incident Response** using the search bar or scroll through the list manually.
3. Select **Install**.
4. Next, select **Configure**.
5. Select **true** to enable the plugin.
6. Select **Save**.

When you open the Main Menu, **Playbooks & Incidents** is available as a menu item.

*For Cloud deployments*

Mattermost Incident Management is included in the Mattermost Cloud workspace and is enabled by default.

Getting Started with Incident Management
----------------------------------------

Mattermost Incident Management has the following components:

* **Slash commands:** Used to perform actions and manage incidents.
* **Playbooks:** A playbook is a recipe that defines how an incident is started and resolved, as well as the retrospective process. Playbooks also include configuration options such as reminders.
- **Stages:** A set of tasks grouped together to achieve a specific goal of the workflow, which generally need to be completed before proceeding to the next stage of the incident resolution process.
- **Tasks:** The individual steps required to complete the stages of an incident. Tasks can optionally be assigned to specific incident participants into stages.
* **Incidents:** Incidents are events that require quick and effective collaboration and resolution. How an incident is handled depends on its playbook configuration.

Using slash commands
--------------------

Slash commands are shortcuts used to perform actions in Mattermost. To view the available slash commands in Mattermost begin by typing ``/`` and a list of slash command options appears above the text input box. The autocomplete suggestions help by providing a format example in black text and a short description of the slash command in grey text.

Mattermost Incident Management includes built-in slash commands:

- ``/incident start`` - Start a new incident.
- ``/incident end`` - End an ongoing incident.
- ``/incident restart`` - Restart an ended incident.
- ``/incident check [checklist #] [item #]`` - Check/uncheck the checklist item.
- ``/incident announce ~[channels]`` - Announce the current incident in other channels.
- ``/incident list`` - List all your incidents.
- ``/incident commander [@username]`` - Show or change the current commander.
- ``/incident info`` - Show a summary of the current incident.
- ``/incident stage [next/prev]`` - Move to the next or previous stage.

Adding slash commands to tasks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Slash commands can be added to tasks to initiate actions as part of your playbook.

Here are some examples:

- Add a communication task called **Sync up** with the slash command ``/zoom hello``. Running that slash command initiates a Zoom call in the incident channel. If you've installed Jitsi, you could use ``/jitsi hello``. 
- One of your tasks may require the channel header to be changed to reflect a new status. Create a task called **Change header** with the slash command ``/header new header``.

Generating test data
^^^^^^^^^^^^^^^^^^^^

You can use the test commands to create incidents that are populated with random data. These incidents are listed in the incident insight page.

- ``/incident test create-incident``: This command accepts a playbook ID (that can be chosen from the playbooks the user is a member of, using the autocomplete system), a timestamp, and an incident name. It creates an ongoing incident with the creation date set to the specified timestamp. An example command looks like this: ``/incident test create-incident 6utgh6qg7p8ndeef9edc583cpc 2020-11-23 PR-Testing``.

- ``/incident test bulk-data``: This command accepts a number of ongoing incidents, a number of ended incidents, a beginning and an end date, and an optional seed. It creates as many ongoing and ended incidents as specified, all of them with their creation date randomly picked between the beginning and end dates. The seed, if available, is used to get reproducible results. The names of the incidents are randomly chosen from a list of incident names and a list of fake company names which are defined in the code. An example command is: ``/incident test bulk-data 10 3 2020-01-31 2020-11-22 2``.

Playbooks and Incidents
-----------------------

Playbooks and incidents are associated with teams in Mattermost. Incident channels are created based on playbooks, which define whether an incident channel is public or private. Read more about `public and private channels <https://docs.mattermost.com/help/getting-started/organizing-conversations.html>`_.

Only members of the team in which the playbook or incident is defined have access. Playbook membership is independent of incident membership.

- Members of a playbook may start an incident using that playbook, and edit the playbook's stages and steps.
- Members of an incident may modify the current state of the incident, and invite new members to the incident channel.

During an active incident, you want to focus on triaging and solving the problem as soon as possible. Planning your incident support strategy ahead of time with playbooks is the best way to ensure incidents run smoothly. A playbook is a recipe for dealing with and resolving an incident. In a playbook, you can plan ahead so that during an incident responders know exactly what to do.

Within each playbook, you can create stages and tasks to ensure that items are addressed and completed in sequential order. The tasks can optionally be associated with slash commands and assigned to individual team members. Playbooks also include status update settings, including a reminder feature, so regular updates can be shared to selected channels at set intervals. Make sure to schedule a retrospective analysis to iterate on the design of your playbooks after the incident finishes.

Once complete, incident channels can be exported using the channel export option for analysis. Teams can identify bottlenecks in the incident by seeing time gaps between when checklist items are completed and incorporating necessary changes into the playbook for next incident.

Playbooks
^^^^^^^^^

.. contents::
  :backlinks: top
  :local:

Creating a playbook
~~~~~~~~~~~~~~~~~~~

A playbook must be defined before starting an incident.

1. Navigate to **Main Menu > Playbooks & Incidents**.
2. Select a template, or **+ Create a Playbook** to start a new playbook from scratch.
4. Name your playbook.
5. Edit the **Default Stage**, defining one or more steps to be taken by members of the incident.
   * Optionally use descriptions on steps to add additional context for members of the incident. Descriptions support a limited form of markdown, including text styling and hyperlinks.
   * Optionally define a slash command with the step, simplifying the completion of steps in the incident.
6. Configure whether the incident channel should be public or private within the team.
7. Share this playbook with other members of the team to allow them to use the playbook to start an incident, as well as edit the contents.

Configuring a playbook
~~~~~~~~~~~~~~~~~~~~~~

You can change a playbook's configuration at any time. However, the changes will only be applied to future incidents - not the active incidents, or incidents that previously used that playbook.

Navigate to **Main Menu > Playbooks & Incidents** and select the playbook you'd like to edit.

**Permissions:**

- Change the channel type created with this playbook.
- Share the playbook.

**Stages and tasks:**

- Delete a stage and its associated tasks.
- Add new tasks to an existing stage.
- Edit tasks in an existing stage.
- Edit the slash commands in existing tasks.
- Add new stages and tasks.

**Preferences:**

- Select a broadcast channel where status updates will be automatically posted.
- Set a timer to reminder the incident commander to provide a status update.
- Add a message template with the reminder text.

Deleting a playbook
~~~~~~~~~~~~~~~~~~~

You can delete a playbook provided it's not currently being used in an active incident.

1. Navigate to **Main Menu > Playbooks & Incidents**.
2. Select the **Action** menu next to the playbook name.
3. Select **Delete**.
4. Confirm that you want to **Delete Playbook**.

Incidents
^^^^^^^^^

.. contents::
  :backlinks: top
  :local:

Starting an incident
~~~~~~~~~~~~~~~~~~~~~

To start an incident, use one of the following steps:

- Use the slash command */incident start* from any channel.
- Select the shield icon in the channel header, and select **+ Start Incident**.
- Use the context menu of a post and select **Start incident**.

You need to select a playbook and name your incident before you can select **Start Incident**. The incident description is optional. Only playbooks that you're a member of are listed in the **Playbook** drop-down menu.

The creator of an incident is automatically added as the first member and becomes the commander. To change commanders, click the current commander's name in the RHS and select the new commander. Only members of the channel may be selected as commanders. To change commander to a user who is not in the channel, first add the user to the channel.

Joining an incident
~~~~~~~~~~~~~~~~~~~

When an incident has been started, it's added to the list of channels in the Mattermost team.

If an incident channel is private new participants can only be added to an incident channel by a channel member. If the incident is public, no invitation is needed - search for, and join, the channel via **Browse Channels** in Mattermost.

Ending an incident
~~~~~~~~~~~~~~~~~~~

Incident members can end an incident using the slash command ``/incident end`` from within the incident channel. Ending an incident signals to all participants that the issue has been resolved.

Restarting an incident
~~~~~~~~~~~~~~~~~~~~~~~

An ended incident can be restarted at any time using ``/incident restart`` from within the incident channel or via **Restart Incident** in the RHS. Some playbooks may define stages and tasks to complete after an incident has been resolved, such as scheduling and completing a post-mortem.

Incident information
--------------------

To view information about ongoing incidents, select the **Incidents** icon in the header of any channel to open the RHS where all ongoing incidents in your team are listed. Select **Go to Incident Channel** to open the relevant channel and see:

- The incident summary tab shows:
  - The incident commander
  - The incident duration
  - The current stage
  - The most recent update

Select **Update Status** to send out a status update to your selected channel. 

The tasks list tab shows:
  - The current stage
  - The remaining tasks in the stage
  - The finished tasks in the stage
  
Note that you can advance to the next stage in the incident even if none of the tasks are marked as completed. To return to the previous stage, select the three-dot menu and then choose **Previous Stage**.

You can also:

- Assign a step to yourself or another incident member.
- Mark a step as **Complete** or **Incomplete**.
- Start an automated action.
- Invite new members to the channel.

To view all incidents in your team (ongoing and closed) select **Main Menu > Playbooks & Incidents**. Select the **Incident** tab and then select the incident name to view a summary of the incident, jump to the channel, or export the channel.

Channel Export
--------------

Please see the `Channel Export plugin documentation <https://mattermost.gitbook.io/channel-export-plugin>`_ for more information.

Glossary
--------

- **Commander:** The Mattermost user currently responsible for transitioning an incident from ongoing to ended.
- **Incident channel:** A Mattermost channel dedicated to real-time conversation about the incident.
- **Incident insight page:** The incident details and analytics page, which also provides the channel export download link. It is not available on mobile.
- **Incident member:** A Mattermost user with access to the corresponding incident channel.
- **Playbook configuration page:** The playbook configuration and editing page. It is not available on mobile.
- **The RHS:** The incident list and incident details displayed on the right hand side (RHS) of the web app. It is not available on mobile.
