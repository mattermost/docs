Setting Up Playbooks
====================

A playbook must be defined before starting an incident.

Adding tasks
~~~~~~~~~~~~~

1. Go to **Main Menu > Incident Collaboration**.
2. Select **Playbooks**.
3. Start a **Blank Playbook**, or use the built-in **Incident Collaboration Playbook** as a template.
4. Name your playbook and provide a description.
5. Select the **Tasks** tab.
6. Within the **Tasks** tab, customize the checklists and tasks:
  * Create and name new tasks to capture actions your team should take to resolve the incident.
  * Create new checklists to group tasks meant to be completed together.
  * Drag and drop to reorganize checklists and tasks.
  * Optionally add task descriptions to give additional context to members of the incident channel. Descriptions support a limited form of Markdown, including text styling and hyperlinks.
  * Optionally add a slash command to the task that can be executed by members of the incident channel as needed.
  
Setting preferences
~~~~~~~~~~~~~~~~~~~

1. Select the **Preferences** tab.
2. Within the **Preferences** tab, customize how status updates are communicated:
  * Optionally configure a broadcast channel to which status updates will be copied. If you are not a member of the configured broadcast channel, **Unknown Channel** is displayed instead of the channel name.
  * Optionally configure the default reminder timer used to prompt for regular updates. The reminder timer may be changed when a status update is written.
  * Optionally configure a template to use for the first status update. Subsequent status updates will start with the text of the most recent update.
  
Setting automation
~~~~~~~~~~~~~~~~~~

1. Select the **Automation** tab.
2. Within the **Automation** tab, customize automatically triggered tasks:
  * Optionally enable the **Invite members** toggle and select a set of members. This set of members are automatically invited to the incident channel when the incident starts.
  * Optionally enable the **Assign commander** toggle and select a member. This member is automatically assigned as commander of the incident when the incident starts.
  * Optionally enable the **Announce it in another channel** toggle and select a channel. When the incident is started, an announcement is made in the selected channel.
  * Optionally enable the **Send a webhook** toggle and enter the webhook you want to use.
3. On the right-hand side of the screen, configure the permissions:
  * Decide whether the automatically-created incident channel should be Public or Private within the team.
  * Share this playbook with other members of the team to allow them to use the playbook to start an incident, as well as edit the playbook.

Editing a playbook
~~~~~~~~~~~~~~~~~~~

You can change a playbook's configuration at any time, but changes will only be applied to future incidents. Ongoing or ended incidents previously started from that playbook remain unchanged.

1. Go to **Main Menu > Incident Collaboration**.
2. Select **Playbooks**.
3. Find the playbook to be edited.
 * Only playbooks of which you are a member are listed. System Admins have unrestricted access to all playbooks on the team.
4. Select the name of the playbook, or select the **Actions** menu next to the playbook name, then select **Edit**.
5. Configure the playbook the same way a playbook is created or edited.
