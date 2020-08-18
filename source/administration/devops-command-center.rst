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

Using playbooks
~~~~~~~~~~~~~~~~

Playbooks are templates which are applied to an incident and define a group of tasks (stages) and steps to be followed in order to resolve the incident. Playbooks can be refined over a period of time to match the changing parameters of future related incidents. Incidents can only be started once they're associated with a playbook. It's not possible to start an incident from within the playbook backstage but you can create a playbook for use with a future incident.

When you start an incident, you need to either create a playbook or select an existing one.

**Creating a new playbook**

The creator of a playbook is automatically added as the first member and can remove themselves once other members have been added. Only playbook members can use the playbook to start an incident - System Admins must be added to the member list to have access to a playbook.

You can also create a new playbook outside of an incident. Select **+ New Playbook** to start a new playbook using either the blank template, or the **Incident Response Playbook** template provided.

**Selecting an existing playbook**

You can select any existing playbook that you have access to, from the drop-down list provided, when starting an incident.

**Viewing playbooks**

Open **Main Menu > Incidents & Playbooks > Playbooks** to view the playbooks associated with the current team and create a new one.

Stages and steps
~~~~~~~~~~~~~~~~~~

When you create a playbook you can group your tasks into stages which have accompanying steps. Each step can be assigned a slash command. The steps within each stage must be completed in the order they're listed.

Stages and steps are optional, and can be left empty by default. You can add stages and steps to a playbook that's being used in an active incident, but they won't be applied to the active incident.

Starting incidents
~~~~~~~~~~~~~~~~~~

When you start an incident, a channel is created. You can start an incident in one of three ways:

- Use the slash command */incident start* from any channel.
- Select **!** from the channel header.
- Use the context menu of a post and select **Start incident**.

The incident channel is the central place for discussion related to the incident.  When you create an incident, the name provided is applied to the new incident channel that is created. You can also select an optional playbook.

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

When an incident has started and the incident channel is created, a message from the incident bot is posted to the incident channel naming the creator of the incident. If an incident is started from the context of a post, the text of the post is posted to the channel along with a permalink.

It is not possible to view incidents from teams other than the currently selected team.

To view details about active incidents select **Main Menu > Incidents & Playbooks**. Select an incident to see its duration, members, and messages.

Public and private incidents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Incident channels can be public or private, based on the incident's playbook.

- **Public:** Anyone in the team can view the incident details and join the incident channel. The incident details are visible to all team members during the active incident and after the incident has ended.
 - **Private:** Only incident members who are members of the incident channel have access to the ongoing incident and incident details after the incident has ended. Private incidents can't be made public once they've been started.

**Creating a public playbook and incident**

1. Navigate to **Main Menu > Incidents & Playbooks > Playbooks**.
2. Select **+ New Playbook**.
3. Replace **Untitled Playbook** with the name of the playbook.
4. Under **Settings** select **Public**.
5. Select **Save**.
6. Return to the channel view using the **<**.
7. Select **!** in the channel header and then **+ Start Incident**.

**Creating a private playbook and incident**

1. Navigate to **Main Menu > Incidents & Playbooks > Playbooks**.
2. Select **+ New Playbook**.
3. Replace **Untitled Playbook** with the name of the playbook.
4. Under **Settings** select **Private**.
5. Select **Save**.
6. Return to the channel view using the **<**.
7. Select **!** in the channel header and then **+ Start Incident**.

Ending incidents
~~~~~~~~~~~~~~~~

To end an active incident:

- Use the slash command */incident end* from within the incident channel.
- Use the **End Incident** button in the RHS panel while in the incident channel.

Administrator's Guide
^^^^^^^^^^^^^^^^^^^^^^

Incidents and playbooks are associated with teams in Mattermost. Incident channels are created based on playbooks, and are public or private depending on the playbook's settings. Read more about `public and private channels <https://docs.mattermost.com/help/getting-started/organizing-conversations.html>`_.

Permissions
~~~~~~~~~~~~

Membership of playbooks and incidents is independent. System Admins can edit the visibility of, and access to, playbooks and incidents so that:

- Incident members can't have access to playbooks removed by other members of the team.
- Team members can't be removed from an incident by other members of the team.
- Incident members can invite other team members to manage private playbooks.

Managing incident channel visibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System Admins can manage the visibility of public incident channels by converting them into private incident channels. These steps are only applicable if the incident's playbook is **Public**.

**Creating a private incident channel**

1. Create an incident via **! > + Start Incident**, select or create a playbook, and choose **Start Incident**.
2. From the channel header, click the dropdown and select **Convert to Private Channel**.
3. In the confirmation box, select “Yes.”
4. Open the incident backstage, select the incident, and confirm that it is listed as **Private**.

**Converting a public incident channel into a private incident channel as a participant**

1. Join an active incident channel.
2. From the channel header, click the dropdown and select **Convert to Private Channel**.
3. In the confirmation box, select “Yes.”
4. Open the incident backstage, select the incident, and confirm that it is listed as **Private**.

Managing playbooks
~~~~~~~~~~~~~~~~~~~

Any member of a playbook as well as all System Admins can modify playbook editing permissions and visibility.

**Adding a playbook editor**

1. Navigate to **Main Menu > Incidents & Playbooks > Playbooks**.
2. Search for the playbook you want to edit.
3. Select **Edit**.
4. Invite a team member to edit the playbook.
5. Select **Save Playbook**.

**Removing a playbook member**

1. Navigate to **Main Menu > Incidents & Playbooks > Playbooks**.
2. Search for the playbook you want to edit.
3. Select **Edit**.
4. Search for the user in the list provided.
5. Remove the user from the playbook.
6. Select **Save Playbook**.

Incidents backstage
~~~~~~~~~~~~~~~~~~~~

To open the incidents backstage, which lists all incidents associated with the current team, select **Main Menu > Incidents & Playbooks**. All incidents for the current team are listed for review with the following details for each incident:

- Name
- Status (**Ongoing** or **Ended**)
- Start Date
- End Date, if ended, otherwise **--**
- Commander

Viewing incident details
~~~~~~~~~~~~~~~~~~~~~~~~

To view details of ongoing and ended incidents associated with your Mattermost team, open **Main Menu > Incidents & Playbooks**. Select an incident's name to view its details.

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
- A prompt to `Export the Incident Channel <#exporting-channels>`_.
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
