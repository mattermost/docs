=====================
DevOps Command Center
=====================


.. contents:: Contents
  :backlinks: top
  :local:
  :depth: 2

Overview
^^^^^^^

Workplace messaging is often process-driven rather than completely ad-hoc, and these processes could be organizationally critical in crisis situations. Help
teams collaborate to solve problems that are time-sensitive, recurring, situational.

Incident Response is a Mattermost plugin designed to help organizations monitor, coordinate,
and measure their incident response processes, increasing transparency, maximizing effectiveness, and ultimately saving costs by cutting down time taken to respond and resolve incidents.


User's Guide
^^^^^^^^^^^^^

Incidents are events within Mattermost that are initiated to manage a specific situation/response in real-time. When the situation/response is complete, the incident is ended.
Incident details are stored as logs, and events that occurred within the incident can be reused in future incidents as Playbooks and checklists.

Starting incidents
~~~~~~~~~~~~~~~~~~

The incident channel is the central place for discussion related to the incident. You can start an incident in one of three ways:

- Use the slash command */incident start* from any channel.
- Use the message actions dropdown menu and select **Start incident**.
- Use the context menu of a post and select **Start incident**.

When you create an incident, the name provided is applied to the new incident channel that is created. You can also select an optional Playbook. The channel name can be used to
search for the channel, and is also the name appended to the archived logs. If a Playbook is selected,
the corresponding checklist is used as a template to start the incident. If no Playbook is selected, the incident starts with an empty checklist.

The creator of an incident automatically becomes the incident Commander, responsible for managing the incident.

The Commander of the incident can:

- Select Playbooks
- Create checklists
- Invite people to the channel
- Hand over the Commander role to another channel member

The Commander of the channel must be a team/channel admin, and if the role is handed to another member they must also be a team/channel admin. To change Commanders,
select the current Commander’s name and use the search bar to locate the username of the new Commander. Only members of the channel may be selected as commanders. To assign a
Commander not in the channel, that user must first be invited to the channel using the existing Mattermost user interface (**Manage Members** in the channel header, or the /invite slash command).
Changing the Commander takes effect immediately, and members are notified of the change in the channel.

Active incidents
~~~~~~~~~~~~~~~~

To view details about active incidents, click the **!** icon in the channel header to bring up the right-hand side (RHS) panel that shows a list of current
active incidents. Select an incident to see its Commander, channel, and checklist.

When an incident has started and the incident channel is created, the channel header is updated to reflect its origin and
a message from the incident bot is also posted to the incident channel naming the creator of the incident. If an incident is started
from the context of a post, the channel header includes a link to the post and the text of the post is also posted to the channel alongside a permalink.

Incidents are displayed in the RHS and visible to all members of the relevant team, even if they are not a member of the corresponding incident channel. It
is not possible to view incidents from teams other than the currently selected team.

Using Playbooks
~~~~~~~~~~~~~~~~

Playbooks are templates which are applied to an incident and define a set of steps to be followed in order to resolve the incident. Playbooks can be
refined over a period of time to match the changing parameters of related incidents.

The set of steps contained within a Playbook is called a checklist.

Viewing and creating Playbooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the Playbooks icon **()** in the RHS to open the Playbooks backstage and list all Playbooks associated with the current team.
Select **+ New Playbook** to start a new Playbook and checklist. Enter a Playbook name and choose **Save Playbook**.

Creating checklists
~~~~~~~~~~~~~~~~~~~

Checklists are created within a Playbook and provide steps to follow during an incident. Checklists can be created ahead of time as part of a Playbook, or during an incident.


Editing checklists
~~~~~~~~~~~~~~~~~~~

Checklists can be edited during an incident as well as when not associated with an active incident.

To edit a checklist, choose **Edit**.
- Hover over an input box and select the **X** to remove the checklist item.
- Drag the hamburger menu to rearrange the checklist items.

Choose **Done** to save the changes.


Ending incidents
~~~~~~~~~~~~~~~~

There are two ways to end an incident:

- Using slash command */incident end* from within the incident channel.
- Using the **End Incident** button in the RHS panel while in the incident channel.

The incident will become inactive, be removed from the list of active incidents, and the associated channel is archived.


Administrator's Guide
^^^^^^^^^^^^^^^^^^^^^^

Permissions
~~~~~~~~~~~~~~~~~~~~~

Incidents and Playbooks are associated with teams in Mattermost, and permissions are assigned based on the Permission scheme used in Mattermost. Incidents
are directly tied to a specific team and channel.

Public incidents
~~~~~~~~~~~~~~~~~~~~~

Public incidents are incidents where anyone with access to the team the incident channel is created on can join the incident as a participant by joining the channel
the incident is in. Anyone on the team can join the primary channel and become an incident participant. Just like public channels, public incidents appear for everyone
in the team they are created in.

Private incidents
~~~~~~~~~~~~~~~~~~~~~

Private incidents are invite-only. Participants can be added by inviting them to the incident's primary channel. Like private channels, private incidents do not appear on
the incident list of users who are not participants.

To view incidents associated with your Mattermost team, select the **Incidents** icon in the channel header to open the RHS menu. If there are no active incidents, you can
start one or you can view incident logs.

Incidents Backstage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To open the Incidents backstage Select **Incidents & Playbooks** from the Main Menu , which lists all incidents associated with the current team. This main menu item is available to all Mattermost users.

All incidents for the current team are listed for review with the following details for each incident:

- Name
- Status (**Ongoing** or **Ended**)
- Start Date
- End Date, if ended, otherwise **--**
- Commander

All dates are rendered as per the locale and timezone of the active user.

Viewing incident details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To view details of active incidents, select **Incidents** from the plugin menu to open the RHS panel.

Listed incidents include the following information:

- The current Commander’s profile picture and username
- Zero or more checklist items
- The channels associated with the incident
- A button to end the incident

If the incident is active, but in a private channel, you won't be able to see the incident channel name or select **End Incident**. However, the Commander name and incident
checlist will be visible. If you're a participant in an incident channel, you can modify incident details from within that channel.

You can view all incidents in the incident Backstage via **Main Menu > Incidents & Playbooks**.

Select an incident to view:

- Incident name
- A link icon to open the corresponding incident channel
- Status (**Ongoing** or **Ended**)
- The Commander, including profile picture and username
- A prompt to export the incident channel
- The total duration
- The number of members involved in the incident
- The number of messages posted to the channel, including another prompt to open the corresponding incident channel

The **Duration** widget displays the duration of the incident. While the incident is ongoing, the end time is displayed as **Ongoing**. When the incident has ended, it
shows the end time (in the user's timezone). The **Members Involved** widget indicates the total number of users that participated in the channel, either
by posting a message, being assigned as Commander, or interacting with a checklist. This number is not affected by users leaving the channel, or users joining the channel but not participating.

The total number of messages displayed includes messages posted by both users and bots (including the incident response bot). It does not include system or ephemeral messages.

**Filtering incidents**

Incidents can be filtered by incident name, Commander, and incident status.

**Browsing related channels**

Incident members see a link to the incident channel at the bottom of the incident details. Clicking the channel name navigates to the incident channel.
This section is omitted when the active user is not an incident member.

Exporting channels
^^^^^^^^^^^^^^^^^

If your server is licensed for E20, and the channel export plugin is installed and active, navigate to **Main Menu > Incidents & Playbooks**, select an incident, and
then choose **Export Incident Channel** in the top-right corner to download the contents of the incident channel as a CSV. The file excludes attachments, but includes system messages.
If you have an E20 license but the channel export plugin is not installed, or the plugin is installed but not enabled, it’s not possible to select **Export Incident Channel**.

To install and activate the plugin, navigate to the plugins menu and follow the steps provided.

Telemetry
^^^^^^^^^^

During beta early access, events for the Incident Response plugin are collected regardless of the server telemetry configuration. In other words, even if
telemetry is disabled in your Mattermost server, the information described on this page is still collected.

We only track the events that create, delete or update any items. We never track the specific content of the items. In particular, we
do not collect the name of the incidents or the contents of the checklist items.

Every event we track is accompanied with metadata that help us identify each event and isolate it from the rest of the servers. We can group all
events that are coming from a single server, but never identify that server. The following list details the metadata that accompanies every event:

- ``diagnosticID``: Unique identifier of the server the plugin is running on.
- ``serverVersion``: Version of the server the plugin is running on.
- ``pluginVersion``: Version of the plugin.
- Fields automatically generated by Rudder:
  
  - ``eventTimeStamp``: Timestamp on when the event was queued to send to the server.
  - ``createdAt``: Timestamp on when the event was sent to the server.
  - ``id``: Unique identifier of the event.
  - ``event integrations``: Unused field. It always contains the value null.
  - ``event originalTimestamp``: Timestamp on when the event actually happened. It always equals eventTimeStamp.
  - ``type``: Type of the event. It always contains the string ”track”.

**Events data**

.. csv-table::
    :header: "Event", "Triggers", "Information collected"

    "Incident created", "- Any user sends the ``/incident start`` command and creates an incident. 
    - Any user clicks on the ``+`` button on the Incident list view, in the RHS and creates an incident.
    - Any user clicks on the drop-down menu of any post, clicks on the ``Start incident`` option and creates an incident", "
    - ``ID``: Unique identifier of the incident.
    - ``IsActive``: Boolean  value indicating if the incident is active. It always equals ``true``.
    - ``CommanderUserID``: Unique identifier of the commander of the incident. It equals the identifier of the user that created the incident.
    - ``TeamID``: Unique identifier of the team where the incident channel is created.
    - ``CreatedAt``: Timestamp of the incident creation.
    - ``ChannelIDs``: A list containing a single element, the channel created along with the incident.
    - ``PostID``: Unique identifier of the post .
    - ``NumChecklists``: Number of checklists. It always equals 1.
    - ``TotalChecklistItems``: Number of checklist items this incident starts with. It always equals 0."
    "Incident finished.", "- Any user sends the ``/incident end`` command. 
    - Any user clicks on the ``End Incident`` button through the incident details view, in the RHS.", "
    - ``ID``: Unique identifier of the incident.
    - ``IsActive``: Boolean  value indicating if the incident is active. It always equals ``false``.
    - ``CommanderUserID``: Unique identifier of the commander of the incident. It equals the identifier of the user that created the incident.
    - ``UserID``: Unique identifier of user that ended the incident.
    - ``TeamID``: Unique identifier of the team where the incident channel is created.
    - ``CreatedAt``: Timestamp of the incident creation.
    - ``ChannelIDs``: A list containing a single element, the channel created along with the incident.
    - ``PostID``: Unique identifier of the post .
    - ``NumChecklists``: Number of checklists. It always equals 1.
    - ``TotalChecklistItems``: Number of checklist items this incident starts with. It always equals 0."
    "Checklist item created", "- Any user creates a new checklist item through the incident details view, in the RHS.", "
    - ``IncidentID``: Unique identifier of the incident where the item was created.
    - ``UserID``: Unique identifier of the user that created the item."
    "Checklist item removed.", "- Any user deletes a checklist item through the incident details view, in the RHS.", "
    - ``IncidentID``: Unique identifier of the incident where the item was.
    - ``UserID``: Unique identifier of the user that removed the item."
    "Checklist item renamed.", "- Any user edit the contents of a checklist item through the incident details view, in the RHS.", "
    - ``IncidentID``: Unique identifier of the incident where the item was.
    - ``UserID``: Unique identifier of the user that removed the item."
    "Checklist item moved.", "- Any user moves the position of a checklist item in the list through the incident details view, in the RHS.", "
    - ``IncidentID``: Unique identifier of the incident where the item is.
    - ``UserID``: Unique identifier of the user that edited the item."
    "Unchecked checklist item checked.", "- Any user checks an unchecked checklist item through the incident details view, in the RHS.", "
    - ``IncidentID``: Unique identifier of the incident where the item is.
    - ``UserID``: Unique identifier of the user that checked the item."
    "Checked checklist item unchecked.", "- Any user unchecks a checked checklist item through the incident details view, in the RHS.", "
    - ``IncidentID``: Unique identifier of the incident where the item is.
    - ``UserID``: Unique identifier of the user that checked the item."
    
Glossary
^^^^^^^^

* **Incident**: An event requiring the coordinated actions of one or more Mattermost users. An incident is either ongoing or closed.
* **Playbook**: A a set of steps to execute as part of resolving an incident. It consists of one or more checklists, with each checklist item representing a single step.
* **Commander**: The Mattermost user currently responsible for transitioning an incident from ongoing to closed.
* **Incident channel**: A Mattermost channel dedicated to real-time conversation about the incident.
* **Incident member**: A Mattermost user with access to the corresponding incident channel.
* **The RHS**: The incident list and incident details displayed on the right hand side of the webapp. Clicking an incident from the list in the RHS surfaces details of the
selected incident. It is not available on mobile.
* **The backstage**: The full-screen analytics and configuration screens accessible from the webapp. It is not available on mobile.
