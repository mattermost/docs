Mattermost Incident Management
==============================

*Available in Mattermost Enterprise Edition E20, Mattermost Cloud Professional, and Mattermost Cloud Enterprise.*

Better response to an incident is one of three ways that Mattermost Incident Management helps you provide more reliable services, in addition to gaining insights with incident reports and incorporating learnings with playbooks.

Mattermost Incident Management allows your team to coordinate, manage, and resolve incidents from within Mattermost. 

Incidents are situations which require an immediate response and benefit from a clearly defined process guiding towards resolution. Incident Management allows your team to coordinate, manage, and resolve incidents from within Mattermost. You can:

- Automatically create a new channel that can be organized in the left-hand sidebar using custom categories.
- Use [playbooks](/playbooks/creating-and-managing-playbooks.md) to perform automated actions such as create a Jira ticket, start a Zoom call, or find out who is on-call in Opsgenie.
- Iterate on and refine processes after each incident.

When incidents are monitored, coordinated, and measured effectively, you can add transparency, maximize effectiveness, and save costs by cutting down time taken to respond to and resolve incidents.

![Mattermost Incident Management screenshot](../docs/assets/incident_response_landing.png)

.. contents::
  :depth: 2
  :local:
  :backlinks: entry
  

Installing Mattermost Incident Management for Self-Managed Deployments
----------------------------------------------------------------------

Mattermost Incident Management is available in the Plugin Marketplace. You can download and install the plugin from Mattermost.

1. Open **System Console > Plugin Management**.
2. Search for **Incident Response** using the search bar or scroll through the list manually.
3. Select **Install**.
4. Next, select **Configure**.
5. Select **true** to enable the plugin.
6. Select **Save**.

When you open the Main Menu, **Playbooks & Incidents** is available as a menu item.

Activating Mattermost Incident Management for Cloud Deployments
---------------------------------------------------------------

Mattermost Incident Management is included in the Mattermost Cloud workspace and is enabled by default.

Using slash commands
--------------------

Slash commands are shortcuts used to perform actions in Mattermost. To view the available slash commands in Mattermost begin by typing `/` and a list of slash command options appears above the text input box. The autocomplete suggestions help by providing a format example in black text and a short description of the slash command in grey text.

Mattermost Incident Management includes built-in slash commands:

- `/incident start` - Start a new incident.
- `/incident end` - Close the incident of that channel.
- `/incident restart` - Restart a closed incident.
- `/incident check [checklist #] [item #]` - Check/uncheck the checklist item.
- `/incident announce ~[channels]` - Announce the current incident in other channels.
- `/incident list` - List all your incidents.
- `/incident commander [@username]` - Show or change the current commander.
- `/incident info` - Show a summary of the current incident.
- `/incident stage [next/prev]` - Move to the next or previous stage.

Adding slash commands to tasks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Slash commands can be added to tasks to initiate actions as part of your incident response playbook.

Here are some examples:

- Add a task called **Sync up** with the slash command `/zoom hello`. Running that slash command initiates a Zoom call in the incident channel. If you've installed Jitsi, you could use `/jitsi hello`. 

![Tasks and slash commands](../assets/stage_task_slashcommand.png)

- One of your tasks may require the header to be changed to reflect a new status. Create a task called **Change header** with the slash command `/header new header`.

![Tasks and slash commands](../assets/stage_task_header.png)
