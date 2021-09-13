Planning a Playbook
====================

Playbooks are made up of:

- **Checklists:** The list of tasks to be completed for the run.
- **Templates:** Templates for frequently-used actions such as updates and reminders. 
- **Actions:** Automation options for inviting members, webhooks, welcome messages, channel export settings, and more.
- **Permissions:** Manage permissions at a channel and a playbook level.

Creating checklists
-------------------

1. Go to **Main Menu > Playbooks**.
2. Start a **Blank Playbook**, or use the built-in template.
3. Name your playbook and provide a description.
4. Select the **Checklists** tab.

  You can start with the default checklist and edit it or you can delete it and select **+ New checklist**.

    * Within each checklist, select **+ New task** to add tasks that are meant to be completed together.
    * Drag and drop to reorganize checklists and tasks.
    * Optionally add task descriptions to give additional context to members of the playbook. Descriptions support a limited form of Markdown, including text styling and hyperlinks.
    * Optionally add a slash command to the task that can be executed by members of the playbook as needed.

5. Choose **Save**.
  
Configuring templates
---------------------

Templates are standardized sets of content that are used for communicating reminders and updates.

1. Go to **Main Menu > Playbooks**.
2. Select the **Templates** tab.

  * Optionally configure a broadcast channel to which status updates will be copied. If you are not a member of the configured broadcast channel, **Unknown Channel** is displayed instead of the channel name.
  * Optionally configure the default reminder timer used to prompt for regular updates. The reminder timer may be changed when a status update is written.
  * Optionally configure a template to use for the first status update. Subsequent status updates will start with the text of the most recent update.

Defining actions
----------------

You can customize actions associated with your playbook by setting up keyword triggers, automate member invites, and add a welcome message for new members.

Select the **Actions** tab.

Prompt to run the playbook when a user posts a message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  * **Keywords**: Enable the toggle, and enter comma-separated keywords that, when included in a message, will prompt the posting user to run the playbook.

.. image:: ../images/Playbook-keyword-monitoring.png
   :alt: Keyword notification.

When a run starts
~~~~~~~~~~~~~~~~~

  * **Invite members**: Enable the toggle, and select members who will automatically be invited to the channel when the playbook run starts.
  * **Assign the owner role**: Enable the toggle and select a member. This member is automatically assigned as the owner of the playbook run.
  * **Announce in another channel**: Enable the toggle and select a channel. When the playbook run is started, an announcement is made in the selected channel.
  * **Send outgoing webhook**: Enable the toggle and enter the webhook you want to use for when the run starts. For information about the webhook payload, see the `PlaybookRunWebhookPayload struct <https://github.com/mattermost/mattermost-plugin-playbooks/blob/b4c8058d8660efe35050bc7eb080e3819c7ab09c/server/app/playbook_run_service.go#L176-L185>`_. An example of the JSON payload for a run start `is available here <https://gist.github.com/icelander/b68f2bf2b4ffefec93400cb050211cf1>`_.

When a status update is posted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  * **Send outgoing webhook**: Enable the toggle and enter the webhook you want to use for status updates. For information about the webhook payload, see the `PlaybookRunWebhookPayload struct <https://github.com/mattermost/mattermost-plugin-playbooks/blob/b4c8058d8660efe35050bc7eb080e3819c7ab09c/server/app/playbook_run_service.go#L176-L185>`_. An example JSON payload for a status update `is available here <https://gist.github.com/icelander/2f9938ad68d1e0aa656f97969895d080>`_.
  
When a new member joins the channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 * **Send a welcome message**: Enable the toggle and enter text that new channel members will see when they join the channel.
 * **Add the channel to a sidebar category**: Enable the toggle so that the channel will be automatically categorized and listed under **Playbook runs** in the left-hand sidebar.
 
When a run is archived
~~~~~~~~~~~~~~~~~~~~~~

 * **Export channel**: (E20 and Cloud only) When a run finishes, this triggers the playbook to automatically save a copy of all channel messages in CSV format. This provides a record of the discussion for future reference or other use such as audits.

Setting permissions
-------------------

1. Go to **Main Menu > Playbooks**, and then select **Permissions**.

 * **Channel access**: Decide whether the automatically-created channel should be Public or Private within the team.
 * **Playbook access**: Share this playbook with other members of the team to allow them to use the playbook to start a run, as well as edit the playbook.

Editing a playbook
------------------

You can change a playbook's configuration at any time, but changes will only be applied to future incidents. Ongoing or ended incidents previously started from that playbook remain unchanged.

1. Go to **Main Menu > Playbooks**.
2. Find the playbook to be edited.

 * Only playbooks of which you are a member are listed. System Admins have unrestricted access to all playbooks on the team.

3. Select the name of the playbook.

 * To edit the playbook directly select the **Actions** menu next to the playbook name, then select **Edit**.
 * To access the playbook dashboard, select the hyperlinked playbook name.

4. Configure the playbook the same way a playbook is created or edited.
