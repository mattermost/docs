Planning a Playbook
====================

Playbooks are made up of:

- Checklists: The list of tasks to be completed for the run.
- Templates: Templates for frequently-used actions such as updates and reminders. 
- Actions: Automation options for inviting members, webhooks, welcome messages and more.
- Permissions: Manage permissions at a channel and a playbook level.

Creating checklists
-------------------

1. Go to **Main Menu > Incident Collaboration**.
2. Select **Playbooks**.
3. Start a **Blank Playbook**, or use the built-in template.
4. Name your playbook and provide a description.
5. Select the **Checklists** tab.

You can start with the default checklist and edit it or you can delete it and select **+ New checklist**. Each new section of a checklist is called a stage.

    * Within each stage, select **+ New task** to add tasks that are meant to be completed together.
    * Drag and drop to reorganize stages and tasks.
    * Optionally add task descriptions to give additional context to members of the playbook. Descriptions support a limited form of Markdown, including text styling and hyperlinks.
    * Optionally add a slash command to the task that can be executed by members of the playbook as needed.
6. Choose **Save**.
  
Configuring templates
---------------------

Templates are standardized sets of content that are used for communicating reminders and updates.

1. Go to **Main Menu > Incident Collaboration**.
2. Select **Playbooks**.
3. Select the **Templates** tab.

  * Optionally configure a broadcast channel to which status updates will be copied. If you are not a member of the configured broadcast channel, **Unknown Channel** is displayed instead of the channel name.
  * Optionally configure the default reminder timer used to prompt for regular updates. The reminder timer may be changed when a status update is written.
  * Optionally configure a template to use for the first status update. Subsequent status updates will start with the text of the most recent update.
  
Defining actions
----------------

You can customize actions associated with your playbook by setting up keyword triggers, automate member invites, and add a welcome message for new members.

Select the **Actions** tab.

  * **Keywords**: Enable the toggle, and enter comma-separated keywords that, when included in a message, will prompt a playbook run.
  * **Invite members**: Enable the toggle, and select members who will automatically be invited to the channel when the playbook run starts.
  * **Assign the owner role**: Enable the toggle and select a member. This member is automatically assigned as the owner of the playbook run.
  * **Announce in another channel**: Enable the toggle and select a channel. When the playbook run is started, an announcement is made in the selected channel.
  * **Send outgoing webhook**: Enable the toggle and enter the webhook you want to use for status updates.

Setting permissions
-------------------

1. Go to **Main Menu > Incident Collaboration**.
2. Select **Playbooks**.
3. Select **Permissions**.
 * **Channel access**: Decide whether the automatically-created channel should be Public or Private within the team.
 * **Playbook access**: Share this playbook with other members of the team to allow them to use the playbook to start a run, as well as edit the playbook.

Editing a playbook
------------------

You can change a playbook's configuration at any time, but changes will only be applied to future incidents. Ongoing or ended incidents previously started from that playbook remain unchanged.

1. Go to **Main Menu > Incident Collaboration**.
2. Select **Playbooks**.
3. Find the playbook to be edited.
 * Only playbooks of which you are a member are listed. System Admins have unrestricted access to all playbooks on the team.
4. Select the name of the playbook, or select the **Actions** menu next to the playbook name, then select **Edit**.
5. Configure the playbook the same way a playbook is created or edited.
