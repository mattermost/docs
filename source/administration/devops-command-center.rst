=====================
DevOps Command Center
=====================


.. contents:: Contents
  :backlinks: top
  :local:
  :depth: 2

Overview
^^^^^^^

Incident Response is a Mattermost plugin designed to help organizations monitor, coordinate, and measure their incident response processes, increasing transparency, maximizing effectiveness, and ultimately saving costs by cutting down time taken to respond and resolve incidents.

User's Guide
^^^^^^^^^^^^^

Incidents are events within Mattermost that are initiated to manage a specific situation/response in real-time. When the situation/response is complete, the incident is ended. Events that occurred within the incident can be reused in future incidents as playbooks and checklists.

Starting incidents
~~~~~~~~~~~~~~~~~~

The incident channel is the central place for discussion related to the incident. You can start an incident in one of three ways:

- Use the slash command */incident start* from any channel.
- Select **!** from the channel header.
- Use the context menu of a post and select **Start incident**.

When you create an incident, the name provided is applied to the new incident channel that is created. You can also select an optional playbook.

- If a playbook is selected, a corresponding checklist is used as a template to start the incident.
- If no playbook is selected, the incident starts with an empty checklist.

The creator of an incident automatically becomes the incident commander, responsible for managing the incident.

The commander of the incident can:

- Select a playbook when starting an incident.
- Create checklists.
- Invite people to the channel.
- Hand over the commander role to another channel member.

To change commanders, select the current commander’s name and use the search bar to locate the username of the new commander. Only members of the channel may be selected as commanders. To assign a commander who is not in the channel, that user must first be invited to the channel using the existing Mattermost user interface (**Manage Members** in the channel header, or the */invite* slash command). Changing the commander takes effect immediately, and members are notified of the change in the channel.

Active incidents
~~~~~~~~~~~~~~~~

To view details about active incidents select **!** in the channel header, to open the right-hand side (RHS) panel and list of current active incidents. Select an incident to see its commander, channel, and checklist.

When an incident has started and the incident channel is created, a message from the incident bot is posted to the incident channel naming the creator of the incident. If an incident is started from the context of a post, the text of the post is posted to the channel along with a permalink.

Incidents that are displayed in the RHS are visible to all members of the relevant team, even if they are not a member of the corresponding incident channel. It is not possible to view incidents from teams other than the currently selected team.

Using playbooks
~~~~~~~~~~~~~~~~

Playbooks are templates which are applied to an incident and define a set of steps to be followed in order to resolve the incident. Playbooks can be refined over a period of time to match the changing parameters of future related incidents.

The set of steps contained within a playbook is called a checklist.

Viewing and creating playbooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select **!** in the channel header to open the RHS panel. Select the **Playbooks** icon to open the playbooks backstage and list all playbooks associated with the current team. Select **+ New Playbook** to start a new playbook and checklist. Enter a playbook name and choose **Save Playbook**.

Public and private incidents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Incidents can be:

**Public:** Anyone in the team can view the incident details and join the incident channel.
**Private:** Only incident members who were in the incident when it was started have access to the ongoing incident and view incident details after the incident has ended.

**Creating a public incident channel**

1. Navigate to **Main Menu > Incidents & Playbooks > Playbooks**
2. Select **+ New Playbook**.
3. Enter a name for the playbook.
4. Move the toggle to the right to **Create Public Incident**.
5. Add a few checklist items.
6. Select **Save**
7. Switch to the main channel view.
8. Create an incident by selecting the playbook you just created.

**Creating a private incident channel**

1. Navigate to **Main Menu > Incidents & Playbooks > Playbooks**.
2. Select **+ New Playbook**.
3. Enter a name for the playbook.
4. Keep the **Create Public Incident** option disabled.
5. Add a few checklist items.
6. Select **Save**
7. Switch to the main channel view.
8. Create an incident by selecting the playbook you just created.

Private incidents are invisible to non-participants: they do not appear in the RHS when active, nor anywhere in the backstage. Private incidents cannot be made public once they've been started. If an incident was public and changed to private, it can't be accessed by non-participants thereafter, and the contents of the channel won't show up in a search query.

Editing checklists
~~~~~~~~~~~~~~~~~~~

You can edit checklist items and their position in the checklist during an active incident as well as checklist items in playbooks not currently being used in active incidents.

1. Select **!** in the channel header of an active incident.
2. Choose **Edit**.
   - To edit: Select the text field to edit details.
   - To delete: Hover over an input box and select the **X** to remove the checklist item.
   - To move: Drag the hamburger menu to rearrange the checklist items.
3. Choose **Done** to save the changes.

Ending incidents
~~~~~~~~~~~~~~~~

There are two ways to end an incident:

- Using the slash command */incident end* from within the incident channel.
- Using the **End Incident** button in the RHS panel while in the incident channel.

The incident will become inactive, is removed from the list of active incidents, and the associated channel is archived.

Administrator's Guide
^^^^^^^^^^^^^^^^^^^^^^

Incidents and playbooks are associated with teams in Mattermost. Participants can be added to an incident by other incident members inviting them to the incident's channel. By default, all incidents are public (available to all members of a team). An incident can be made private during creation, or it can be made private after it has been created. 

Permissions
~~~~~~~~~~~~~~~~~~~~~

System Admins and Team Admins can edit the visibility of, and access to, playbooks and incidents so that:

- Users who are removed from an incident channel by a System Admin can no longer access the incident's playbook.
- Team members who aren't System or Team Admins can't invite other team members to manage private playbooks.
- Team members who aren't System or Team Admins can't be removed from an incident by other members of the team.
- Team members who aren't System or Team Admins can't have access to playbooks removed by other members of the team.

In addition, System and Team Admins can allow:

- Public playbooks to be deleted by team members whether they're participants in an incident channel or not.

Managing incident channel visibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System Admins can manage the visibility of channels by converting them into private incident channels. When a public incident is converted to a private incident, it can't be accessed by members who weren't in the channel at the time of the conversion. In addition, the contents of the channel won't show up in a search query or in the incident list in the incident backstage. 

Once a public incident is converted to a private incident the change cannot be reversed. Non-participants who are in the same team can be added to the channel by an admin.

**Creating a private incident channel**

1. Create an incident via **! > Create Incident**.
2. From the channel header, click the dropdown and select **Convert to Private Channel**.
3. In the confirmation box, select “Yes..”
4. Open the incident backstage, select the incident, and confirm that it is listed as **Private**.

**Converting a public incident channel into a private incident channel as a participant**

1. Join an active incident channel.
2. From the channel header, click the dropdown and select **Convert to Private Channel**.
3. In the confirmation box, select “Yes..”
4. Open the incident backstage, select the incident, and confirm that it is listed as **Private**.

Managing playbooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System and Team Admins can modify playbook editing permissions and visibility.

**Adding a user as a playbook editor**

1. Navigate to **Main Menu > Incidents & Playbooks > Playbooks**.
2. Search for the playbook you want to edit.
3. Select **Edit**.
4. Invite a team member to edit the playbook.
5. Select **Save Playbook**.

**Removing a user from a playbook**

1. Navigate to **Main Menu > Incidents & Playbooks > Playbooks**
2. Search for the playbook you want to edit.
3. Select **Edit**.
4. Search for the user in the list provided.
5. Remove the user from the playbook.
6. Select **Save Playbook**.

Incidents backstage
~~~~~~~~~~~~~~~~~~~~

To open the incidents backstage, which lists all incidents associated with the current team, select **Incidents & Playbooks** from the Main Menu. All incidents for the current team are listed for review with the following details for each incident:

- Name
- Status (**Ongoing** or **Ended**)
- Start Date
- End Date, if ended, otherwise **--**
- Commander

Viewing incident details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To view details of active incidents associated with your Mattermost team, select **!** in the channel header to open the RHS panel. If there are no active incidents, you can view details of incidents that have ended. If an incident is public you can view details. If an incident is private you will not be able to view the details.

Incident details include the following information:

- The current commander’s profile picture and username.
- Zero or more checklist items.
- The channels associated with the incident.
- A button to end the incident.

If the incident is active, but in a private channel, you won't be able to see the incident channel name or select **End Incident**. However, the commander name and incident checklist are displayed. If you're a participant in an incident channel, you can modify incident details from within that channel.

You can view all incidents in the incident Backstage via **Main Menu > Incidents & Playbooks** and then select an incident to view the following details:

- Incident name
- A link icon to open the corresponding incident channel
- Status (**Ongoing** or **Ended**)
- The commander, including profile picture and username
- A prompt to `Export the Incident Channel <#exporting-channels>`_
- The **Duration** widget displays the duration of the incident. While the incident is ongoing, the end time is displayed as **Ongoing**. When the incident has ended, it shows the end time (in the user's timezone).
- The **Members Involved** widget indicates the total number of users that participated in the channel, either by posting a message, being assigned as commander, or interacting with a checklist. This number is not affected by users leaving the channel, or users joining the channel but not participating.
- The total number of messages displayed includes messages posted by both users and bots (including the incident response bot). It does not include system or ephemeral messages.
- A graph depicting when each checklist item was completed.

**Filtering incidents**

Incidents can be filtered by incident name, commander, and incident status.

**Browsing related channels**

Incident participants see a link to the incident channel at the bottom of the incident details. Clicking the channel name navigates to the incident channel. This section is not displayed when the active user is not an incident participant.

Exporting channels
^^^^^^^^^^^^^^^^^

If your server is licensed for E20, and the channel export plugin is installed and active, navigate to **Main Menu > Incidents & Playbooks**, select an incident, then choose **Export Incident Channel** in the top-right corner to download the contents of the incident channel as a CSV. The file excludes attachments, but includes system messages.

If you have an E20 license but the channel export plugin is not installed, or the plugin is installed but not enabled, it’s not possible to select **Export Incident Channel**.

You can install and activate the plugin via the `Plugin Marketplace <https://docs.mattermost.com/administration/plugins.html#plugin-marketplace>`_.

Telemetry
^^^^^^^^^^

During beta early access, events for the Incident Response plugin are collected regardless of the server telemetry configuration. In other words, even if telemetry is disabled in your Mattermost server, the information described on this page is still collected.

We only track the events that create, delete, or update items. We never track the specific content of the items. In particular, we do not collect the name of the incidents or the contents of the checklist items.

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
