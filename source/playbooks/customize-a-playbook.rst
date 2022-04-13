Customize your playbook
=======================

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Playbooks are highly customizable to align with your workflow.

Edit a playbook
---------------

You can change a playbook’s configuration at any time, but changes will only be applied to future incidents. Ongoing or ended incidents previously started from that playbook remain unchanged.

1. Go to **Product menu > Playbooks**.
2. Find the playbook to be edited.

   - Only playbooks of which you are a member are listed. System Admins have unrestricted access to all playbooks on the team.

3. Select the name of the playbook.

   - To edit the playbook directly select the actions menu next to the playbook name, then select **Edit**.
   - To access the playbook dashboard, select the hyperlinked playbook name.

4. Configure the playbook the same way a playbook is created or edited.

Make checklists
----------------

1. Open Playbooks and select the **Playbooks** tab.
2. Start a **Blank Playbook**, or use the built-in template.
3. Name your playbook and provide a description.
4. Select the **Checklists** tab.

  You can start with the default checklist and edit it, or you can delete it and select **+ New checklist**.

    * Within each checklist, select **+ New task** to add tasks that are meant to be completed together.
    * Drag and drop to reorganize checklists and tasks.
    * Add task descriptions to give additional context to members of the playbook. Descriptions support a limited form of Markdown, including text styling and hyperlinks.
    * Add a slash command to the task that can be executed by members of the playbook as needed.

5. Choose **Save**.

Assign tasks and due dates
--------------------------

In some workflows, there are time constraints on tasks and others may have more flexible timeframes.

Tasks can be assigned to run members, with a due date. Select the **Toggle Run Details** icon to open the **Run Details** screen. Hover over the task you’d like to edit and select the calendar icon to assign a due date.

When a due date is assigned to a task, the user will receive reminders about the task in their Playbooks daily digest. When the task is completed, it’s removed from the daily digest reminders. 

Broadcast channels
------------------

There may be multiple active runs on any given day.

Setting up a dedicated broadcast channel is an easy way to centralize status updates, decrease noise, and remember where everything is. Configure a broadcast channel to which status updates will be copied. If you are not a member of the configured broadcast channel, **Unknown Channel** is displayed instead of the channel name.

Keywords
--------

You can use keywords to trigger a playbook. Keyword are set in the **Channel Actions** menu and are applicable to a specific channel. When you use the Keywords action any channel member who has access to the playbook and who uses one of the listed keywords will be prompted to run the associated playbook.

If you find your keywords result in too many false positives, consider refining your list and also consider that URLs used by run members may also contain monitored keywords.

Actions
-------

You can customize actions associated with your playbook to ensure a smooth start when starting a run. Select the **Actions** tab to view the automation options available.

Options include creating a channel when a run is started, inviting members to the run, sending outgoing webhooks, and automatically adding the run channel to a sidebar category.

Actions such as channel creation and adding the channel to a sidebar category are set per-playbook and applied to each run that uses that playbook.
If you’re a System Admin or Channel Admin of the run channel you can also edit these settings in the run channel, via the channel menu, in **Channel Actions**. Editing the settings in the run channel will only affect that channel and the changes aren’t applied to the playbook. 

Only Channel Admins can edit the **Channel Actions** items (such as the welcome message) but members who have access to the playbook can edit the welcome message and run behavior settings. Editing these won’t change the welcome message of a run that’s in progress - it only applies going forward.

If you want to change the behavior of all future runs associated with the playbook, edit the playbook directly in the **Actions** menu.

Webhooks
--------

- For information about the webhook payload for run start, see the PlaybookRunWebhookPayload struct. An example of the JSON payload for a run start is available here.
- For information about the webhook payload for status update, see the PlaybookRunWebhookPayload struct. An example JSON payload for a status update is available here.
