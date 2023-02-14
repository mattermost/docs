Work with playbooks
===================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

A playbook is a checklist of the tasks that make up your processes. Playbooks allow you to take codified knowledge and processes and make them accessible and editable by your organization and team.

Playbook configuration applies both to the execution of the playbook as well as to its management and improvement.

When you're setting up your playbook, you'll be able to break tasks down, and assign actions to them - such as using a slash command to start a Zoom call. You can also decide whether to use the same channel every time your playbook is run, or a new one.

There are other parts of a playbook, such as automation settings, and metrics. But the very first thing you’ll want to set up is a checklist.

Each time you use the process you’ve documented, such as onboarding a new customer, the playbook is used to start a run - a discrete single use of the process - and that run is captured in a channel (either a dedicated one or a new one every time you run the playbook). 

Setting up a playbook includes configuring how the playbook manages the creation of its channel as well as how stakeholders are notified.

To open a playbook and view its statistics, select the playbook name. To begin a run using a specific playbook, select **Run** beside that playbook’s name.

Templates
----------

Creating a playbook from scratch can be daunting, even if you have the process mapped out. One way to get started quickly is to use one of the pre-configured templates available. These templates are populated with content and settings to provide guidance and are customizable.

Playbook templates are basic workflows that you can use to get started quickly. As you learn more about your workflows, you can customize them into specific playbooks.

Choose a template
~~~~~~~~~~~~~~~~~

The first step is to choose the right template for your use case. There are pre-configured templates for specific scenarios. The checklists, actions, status updates, and retrospective settings for these templates may already be filled in and, where appropriate, enabled. You can always edit and adjust these settings - they're there to guide you - removing them doesn't negatively affect the playbook run.

.. tip:: 

    Take a look at the **Learn how to use playbooks** template. This template breaks down the components of a playbook and you can also start a test run to see how everything fits together. If you're taking this option, you can stop reading here and enjoy the test run. You can also choose a blank template and start from scratch - this is a good option if your use case is unique.

In the incident response template, the template contains items that are relevant to incident resolution. These are general items to help you get started.

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

1. In channels, select **Toggle Playbook List** from the apps bar.
2. Select an exiStart a **Blank Playbook**, or use the built-in template.
3. Name your playbook and provide a description.
4. Select the **Checklists** tab.

  You can start with the default checklist and edit it, or you can delete it and select **+ New checklist**.

    * Within each checklist, select **+ New task** to add tasks that are meant to be completed together.
    * Drag and drop to reorganize checklists and tasks.
    * Add task descriptions to give additional context to members of the playbook. Descriptions support a limited form of Markdown, including text styling and hyperlinks.
    * Add a slash command to the task that can be executed by members of the playbook as needed.

5. Choose **Save**.

Multiple runs in a channel
--------------------------

From Mattermost v7.7, you can choose to start each run in a new channel or re-use an already existing channel.

Here are some scenarios why you might want to start each run in the same channel:

- Short, frequently-used processes benefit from being in the same channel - it keeps the process streamlined.
- Teams with multiple independent workflows, such as release teams, benefit from having them in one place.
- Cutting down on the number of new channels created makes it easier to find run channels again.
- The run name isn't linked to the the channel's name so you can tell multiple workflows apart.

When you're configuring your playbook:

- You can link it to an existing channel so that each run starts in that channel.
- You can choose that each time the playbook is run, it creates a new channel.

To access this setting, open the playbooks tab. Select the playbook you want to edit, then select the **Outline** tab. Select **Actions** in the left-hand menu and make your selection under the **When a run starts** heading.

When you start a run, your selection is the default but can be changed for each run. Additionally, it's also possible to move a started run to another channel, so you're not locked into whichever option you select.

Status updates
--------------

There may be multiple active runs on any given day.

Configuring an update cadence is an easy way to centralize status updates, decrease noise, and remember where everything is. You can do this when you're setting up your playbook. Navigate to the **Usage** section and set the parameters based on expected update cycles and where the updates should be published.

Keywords
--------

You can use keywords to trigger a playbook. Keywords are set in the **Channel Actions** menu and are applicable to a specific channel. When you use the Keywords action any channel member who has access to the playbook and who uses one of the listed keywords will be prompted to run the associated playbook.

If you find your keywords result in too many false positives, consider refining your list and also consider that URLs used by run members may also contain monitored keywords.

Actions
-------

You can customize actions associated with your playbook to ensure a smooth start when starting a run. Select the **Actions** tab to view the automation options available.

Options include: 

- Create a channel when a run is started
- Invite members to the run
- Send outgoing webhooks
- Automatically add the run channel to a sidebar category

Actions such as channel creation and adding the channel to a sidebar category are set per-playbook and applied to each run that uses that playbook.

If you’re a system admin or channel admin of the run channel you can also edit these settings in the run channel, via the channel menu, in **Channel Actions**. Editing the settings in the run channel will only affect that channel and the changes aren’t applied to the playbook. Only channel admins can edit the **Channel Actions** items (such as the welcome message) but members who have access to the playbook can edit the welcome message and run behavior settings. Editing these won’t change the welcome message of a run that’s in progress - it only applies going forward.

If you want to change the behavior of all future runs associated with the playbook, edit the playbook directly in the **Actions** menu.

Run metrics
-----------

The **Usage** tab in the playbooks dashboard provides run metrics for that playbook. These metrics are available to all viewers. It's not possible to edit or add to these metrics.

Webhooks
--------

- For information about the webhook payload for ``run start``, see the `PlaybookRunWebhookPayload <https://github.com/mattermost/mattermost-plugin-playbooks/blob/b4c8058d8660efe35050bc7eb080e3819c7ab09c/server/app/playbook_run_service.go#L176-L185>`_ struct. An example of the JSON payload for a run start is available `here <https://gist.github.com/icelander/b68f2bf2b4ffefec93400cb050211cf1>`_.
- For information about the webhook payload for ``status update``, see the `PlaybookRunWebhookPayload <https://github.com/mattermost/mattermost-plugin-playbooks/blob/b4c8058d8660efe35050bc7eb080e3819c7ab09c/server/app/playbook_run_service.go#L176-L185>`_ struct. An example JSON payload for a status update is available `here <https://gist.github.com/icelander/2f9938ad68d1e0aa656f97969895d080>`_.
