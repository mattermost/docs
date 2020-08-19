=====================
DevOps Command Center
=====================


.. contents:: Contents
  :backlinks: top
  :local:
  :depth: 2

Overview
^^^^^^^^

Incident Response is a Mattermost plugin designed to help organizations monitor, coordinate, and measure their incident response processes, increasing transparency, maximizing effectiveness, and ultimately saving costs by cutting down time taken to respond and resolve incidents.

User's Guide
^^^^^^^^^^^^

Incidents are situations which require an immediate response and benefit from a clearly defined process guiding towards resolution. A playbook defines this process, initializing a dedicated channel for the incident with steps grouped into stages for members of the incident to follow. When the situation is resolved, the incident is ended, and the playbook can be updated to improve the response to similar incidents in the future.

Playbooks and incidents are scoped by teams, and cannot be shared between teams.

Creating a playbook
~~~~~~~~~~~~~~~~~~~

A playbook must be defined before starting an incident.

1. Navigate to **Main Menu > Incidents & Playbooks**.
2. Click **Playbooks** in the top menu.
3. Select a template, or click **+ New Playbook** to start a new playbook from scratch.
4. Name your playbook.
5. Rename the **Default Stage**, defining one or more steps to be taken by members of the incident.
6. Optionally use descriptions on steps to add additional context for members of the incident. Descriptions support a limited form of markdown, including text styling and hyperlinks.
7. Optionally define a slash command with the step, simplifying the completion of steps in the incident.
8. Configure whether the incident channel should be public or private within the team.
9. Optionally share this playbook with other members of the team to allow them to use the playbook to start an incident, as well as edit the stages, steps and configuration.

Starting an incident
~~~~~~~~~~~~~~~~~~~~

To start an incident, use one of the following steps:

- Use the slash command */incident start* from any channel.
- Select the shield icon in the channel header, and click **+ Start Incident**
- Use the context menu of a post and select **Start incident**.

An interactive dialog appears prompting the selection of a playbook and channel name. Click **Start Incident** to create an incident with the selected playbook. Only playbook members can use the playbook to start an incident.

The newly-created incident channel is the central place for discussion related to the incident. The incident bot announces the creator of the incident with a post in the channel. If an incident is started from the context menu of a post, the text of that post is included in the announcement message.

The creator of a playbook is automatically added as the first member and becomes the commander. The commander is responsible for adding other members to the incident as needed, and may assign a new commander once a member is added to the channel. To change commanders, click the current commander's name in the RHS and select the new commander. Only members of the channel may be selected as commanders. To change commander to a user who is not in the channel, first add the user to the channel. 

Interacting with an incident
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Browsing to an incident channel automatically opens the RHS showing the current commander, duration, active stage and corresponding steps. Any member of the user is free to change the commander, view other stages, mark a new stage as active, or mark a step as completed.

Some steps may be assigned slash commands which can be run at any time by clicking **(Run)** next to the slash command. Use slash commands to expedite the completion of a step, such as inviting a user to the channel or triggering some third-party integration.

Ending incidents
~~~~~~~~~~~~~~~~

To end an active incident, browse to the incident channel and use one of the following steps:

- Use the slash command */incident end*.
- The **End Incident** button in the RHS.

Browsing incidents
~~~~~~~~~~~~~~~~~~

1. Navigate to **Main Menu > Incidents & Playbooks**.
2. With **Incidents** selected in the top menu, view the incidents in the current team.

Only public incidents and incidents in which the active user is a member are displayed. System administrators have access to all incidents, whether or not they are members.

Click on an incident to view additional metadata such as duration, number of involved members, number of messages posted to the channel, and a timeline of when steps were resolved. Optionally filter the list of incidents to show only ongoing incidents, or incidents for whom a given user is the commander.

Exporting channels
^^^^^^^^^^^^^^^^^^

If your server is licensed for E20, and the channel export plugin is installed and active, navigate to **Main Menu > Incidents & Playbooks**, select an incident, then choose **Export Incident Channel** in the top-right corner to download the contents of the incident channel as a CSV. The file excludes attachments, but includes system messages.

If you have an E20 license but the channel export plugin is not installed, or the plugin is installed but not enabled, it’s not possible to select **Export Incident Channel**.

Permissions
~~~~~~~~~~~

Incidents and playbooks are associated with teams in Mattermost. Incident channels are created based on playbooks, which define whether an incident channel is public or private. Read more about `public and private channels <https://docs.mattermost.com/help/getting-started/organizing-conversations.html>`_.

Only members of the team in which the playbook or incident is defined have access. Furthermore, membership of playbook is independent of membership in incidents:

- Members of a playbook may start an incident using that playbook, or edit the playbook's stages and steps. Non-members do not have access to the playbook at all.
- Members of an incident may modify the current state of the incident, and invite new members to the incident channel.

Telemetry
^^^^^^^^^^

We only track the events that create, delete, or update items. We never track the specific content of the items. In particular, we do not collect the name of the incidents or the contents of the stages and steps.

Every event we track is accompanied with metadata that help us identify each event and isolate it from the rest of the servers. We can group all events that are coming from a single server, and if that server is licensed, we are able to identify the buyer of the license. The following list details the metadata that accompanies every event:

- ``diagnosticID``: Unique identifier of the server the plugin is running on.
- ``serverVersion``: Version of the server the plugin is running on.
- ``pluginVersion``: Version of the plugin.
- Fields automatically generated by Rudder:

  - ``eventTimeStamp``: Timestamp indicating when the event was queued to send to the server.
  - ``createdAt``: Timestamp indicating when the event was sent to the server.
  - ``id``: Unique identifier of the event.
  - ``event integrations``: Unused field. It always contains the value null.
  - ``event originalTimestamp``: Timestamp indicating when the event actually happened. It always equals ``eventTimeStamp``.
  - ``type``: Type of the event. It always contains the string ``track``.

**Events data**

.. csv-table::
    :header: "Event", "Triggers", "Information collected"

    "Incident created", "- Any user sends the ``/incident start`` command and creates an incident.
    - Any user clicks on the ``+`` button on the **Incident List** view, in the RHS and creates an incident.
    - Any user clicks on the drop-down menu of any post, clicks on the **Start incident** option, and creates an incident.", "
    - ``ID``: Unique identifier of the incident.
    - ``IsActive``: Boolean  value indicating if the incident is active. It always equals ``true``.
    - ``CommanderUserID``: Unique identifier of the commander of the incident. It equals the identifier of the user that created the incident.
    - ``TeamID``: Unique identifier of the team where the incident channel is created.
    - ``CreatedAt``: Timestamp of the incident creation.
    - ``ChannelIDs``: A list containing a single element, the channel created along with the incident.
    - ``PostID``: Unique identifier of the post.
    - ``NumChecklists``: Number of checklists. It always equals 1.
    - ``TotalChecklistItems``: Number of checklist items this incident starts with. It always equals 0."
    "Incident finished", "- Any user sends the ``/incident end`` command.
    - Any user clicks on the **End Incident** button through the incident details view, in the RHS.", "
    - ``ID``: Unique identifier of the incident.
    - ``IsActive``: Boolean  value indicating if the incident is active. It always equals ``false``.
    - ``CommanderUserID``: Unique identifier of the commander of the incident. It equals the identifier of the user that created the incident.
    - ``UserID``: Unique identifier of user that ended the incident.
    - ``TeamID``: Unique identifier of the team where the incident channel is created.
    - ``CreatedAt``: Timestamp of the incident creation.
    - ``ChannelIDs``: A list containing a single element, the channel created along with the incident.
    - ``PostID``: Unique identifier of the post.
    - ``NumChecklists``: Number of checklists. It always equals 1.
    - ``TotalChecklistItems``: Number of checklist items this incident starts with. It always equals 0."
    "Checklist item created", "- Any user creates a new checklist item through the incident details view, in the RHS.", "
    - ``IncidentID``: Unique identifier of the incident where the item was created.
    - ``UserID``: Unique identifier of the user that created the item."
    "Checklist item removed", "- Any user deletes a checklist item through the incident details view, in the RHS.", "
    - ``IncidentID``: Unique identifier of the incident where the item was.
    - ``UserID``: Unique identifier of the user that removed the item."
    "Checklist item renamed.", "- Any user edit the contents of a checklist item through the incident details view, in the RHS.", "
    - ``IncidentID``: Unique identifier of the incident where the item was.
    - ``UserID``: Unique identifier of the user that removed the item."
    "Checklist item moved", "- Any user moves the position of a checklist item in the list through the incident details view, in the RHS.", "
    - ``IncidentID``: Unique identifier of the incident where the item is.
    - ``UserID``: Unique identifier of the user that edited the item."
    "Unchecked checklist item checked", "- Any user checks an unchecked checklist item through the incident details view, in the RHS.", "
    - ``IncidentID``: Unique identifier of the incident where the item is.
    - ``UserID``: Unique identifier of the user that checked the item."
    "Checked checklist item unchecked", "- Any user unchecks a checked checklist item through the incident details view, in the RHS.", "
    - ``IncidentID``: Unique identifier of the incident where the item is.
    - ``UserID``: Unique identifier of the user that unchecked the item."
     "Playbook created", "- Any user clicks on the **+ New Playbook** button on the backstage and saves it.", "
    - ``PlaybookID``: Unique identifier of the playbook.
    - ``TeamID``: Unique identifier of the team where the playbook is created.
    - ``NumChecklists``: Number of checklists this playbook has after the update.
    - ``TotalChecklistItems``: Number of checklist items, among all checklists, this playbook has after the update."
     "Playbook deleted", "- Any user clicks on the **Delete** button next to a playbook on the backstage and confirms.", "
    - ``PlaybookID``: Unique identifier of the playbook.
    - ``TeamID``: Unique identifier of the team where the playbook was located.
    - ``NumChecklists``: Number of checklists this playbook had immediately prior to deletion.
    - ``TotalChecklistItems``: Number of checklist items, among all checklists, this playbook had immediately prior to deletion."

Glossary
^^^^^^^^

* **Incident:** An event requiring the coordinated actions of one or more Mattermost users. An incident is either ongoing or closed.
* **Playbook:** A set of steps to execute as part of resolving an incident. It consists of one or more checklists, with each checklist item representing a single step.
* **Commander:** The Mattermost user currently responsible for transitioning an incident from ongoing to closed.
* **Incident channel:** A Mattermost channel dedicated to real-time conversation about the incident.
* **Incident participant:** A Mattermost user with access to the corresponding incident channel.
* **The RHS:** The incident list and incident details displayed on the right hand side of the webapp. Clicking an incident from the list in the RHS surfaces details of the selected incident. It is not available on mobile.
* **Incident backstage:** The full-screen analytics and configuration screens accessible from the webapp. It is not available on mobile.
* **Active incident:** An incident that has not been ended.
