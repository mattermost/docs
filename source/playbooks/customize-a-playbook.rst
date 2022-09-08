Customize your playbook
=======================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Playbooks are highly customizable to align with your workflow.

Edit a playbook
---------------

You can change a playbook’s configuration at any time, but changes will only be applied to future incidents. Ongoing or ended incidents previously started from that playbook remain unchanged.

1. Go to **product menu > Playbooks**.
2. Find the playbook you want to edit.

   - Only public playbooks and private playbooks of which you are a member are listed. System Admins have unrestricted access to all playbooks on the team.

3. Select the name of the playbook.

   - To edit the playbook directly select the actions menu next to the playbook name, then select **Edit**.
   - To access the playbook dashboard, select the hyperlinked playbook name.

4. Select the **Outline** tab. 
5. Edit the text portions of the playbook inline. Use the left-hand menu to navigate to other parts of the playbook that you may want to edit.

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

In some workflows, there are time constraints on tasks and others may have more flexible timeframes. Associating tasks with deliverable dates provides visibility into workloads and helps everyone stay accountable during the run.

To assign a due date to a task, select the **Toggle Run Details** icon to open the **Run Details** screen. Hover over the task you’d like to edit and select the calendar icon to assign a due date. Due dates can be used to sort tasks in the run overview.

When a due date is assigned to a task, and the task is overdue or due today, a reminder is added to the Playbooks daily digest along with tasks that don't have an assigned due date. As tasks are completed, they're removed from the daily digest reminders. You can refresh the list of assigned tasks at any time using the ``/playbooks to-do`` slash command.

Due dates can be entered in text (e.g., "two minutes ago") or numerically (e.g., "15 March 2023").

Broadcast channels
------------------

There may be multiple active runs on any given day.

Setting up a dedicated broadcast channel is an easy way to centralize status updates, decrease noise, and remember where everything is. Configure a broadcast channel to which status updates will be copied. If you're not a member of the configured broadcast channel, **Unknown Channel** is displayed instead of the channel name.

Keywords
--------

You can use keywords to trigger a playbook. Keywords are set in the **Channel Actions** menu and are applicable to a specific channel. When you use the Keywords action any channel member who has access to the playbook and who uses one of the listed keywords will be prompted to run the associated playbook.

If you find your keywords result in too many false positives, consider refining your list and also consider that URLs used by run members may also contain monitored keywords.

Actions
-------

You can customize actions associated with your playbook to ensure a smooth start when starting a run. Select the **Actions** tab to view the automation options available.

Options include: Creating a channel when a run is started, inviting members to the run, sending outgoing webhooks, and automatically adding the run channel to a sidebar category.

Actions such as channel creation and adding the channel to a sidebar category are set per-playbook and applied to each run that uses that playbook.
If you’re a System Admin or Channel Admin of the run channel you can also edit these settings in the run channel, via the channel menu, in **Channel Actions**. Editing the settings in the run channel will only affect that channel and the changes aren’t applied to the playbook.

Only Channel Admins can edit the **Channel Actions** items (such as the welcome message) but members who have access to the playbook can edit the welcome message and run behavior settings. Editing these won’t change the welcome message of a run that’s in progress - it only applies going forward.

If you want to change the behavior of all future runs associated with the playbook, edit the playbook directly in the **Actions** menu.

Run metrics
-----------

The **Usage** tab in the playbooks dashboard provides run metrics for that playbook. These metrics are available to all viewers. It's not possible to edit or add to these metrics.

Webhooks
--------

- For information about the webhook payload for ``run start``, see the `PlaybookRunWebhookPayload <https://github.com/mattermost/mattermost-plugin-playbooks/blob/b4c8058d8660efe35050bc7eb080e3819c7ab09c/server/app/playbook_run_service.go#L176-L185>`_ struct. An example of the JSON payload for a run start is available `here <https://gist.github.com/icelander/b68f2bf2b4ffefec93400cb050211cf1>`_.
- For information about the webhook payload for ``status update``, see the `PlaybookRunWebhookPayload <https://github.com/mattermost/mattermost-plugin-playbooks/blob/b4c8058d8660efe35050bc7eb080e3819c7ab09c/server/app/playbook_run_service.go#L176-L185>`_ struct. An example JSON payload for a status update is available `here <https://gist.github.com/icelander/2f9938ad68d1e0aa656f97969895d080>`_.
