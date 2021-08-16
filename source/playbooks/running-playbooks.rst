Running Playbooks
=================

Use slash commands to initiate playbook runs, make announcements, and get information about a playbook run.

Slash commands
~~~~~~~~~~~~~~

The ``/playbook`` slash command allows interaction with incidents via the post textbox on desktop, browser, and mobile for:

- ``/playbook start`` - Start a playbook run.
- ``/playbook end`` - End a playbook run.
- ``/playbook update`` - Update the current playbook run's status.
- ``/playbook restart`` - Restart an ended playbook run.
- ``/playbook check [checklist item]`` - Check/uncheck the specified task.
- ``/playbook announce ~[channels]`` - Announce the current playbook run in other channels.
- ``/playbook list`` - List all your ongoing playbook runs.
- ``/playbook owner [@username]`` - Show or change the current playbook run owner.
- ``/playbook info`` - Show a summary of the current playbook's activities.

To run a playbook use the ``/playbook start`` slash command from any channel. You can also use the desktop or browser to:

 * Select the **Playbook** icon in the channel header, and select **Run playbook** from the right-hand sidebar.
 * Use the context menu of a post and select **Run playbook**.

Running a playbook opens an interactive dialog. You can create a new playbook or select an existing playbook. Provide a name for your playbook run, then select **Start run**. Only playbooks you belong to are listed in the **Playbook** drop-down menu. The creator of a playbook run is automatically added as the first member and becomes the owner. Lastly, when the playbook run is created, it's announced in the associated channel by the Playbook Bot.

Joining a playbook run
~~~~~~~~~~~~~~~~~~~~~~

Open **Main Menu > Playbooks** to see a list of runs, to which you have access. If the channel is public, you may join the channel without permission. You can also search for and join the channel via **Browse Channels**.

If the channel is private, an existing member must invite you.

Working with tasks
~~~~~~~~~~~~~~~~~~

Tasks can be part of pre-configured task templates in playbooks and they can also be added, edited, and removed as needed during an active run. Any member of the playbook run can work with tasks:

* To mark a task as completed, select the unchecked checkbox next to the task. To undo this, clear the checkbox.
* To assign a task to a member of the incident channel, select **No Assignee** (or the existing assignee's username), then select a user.
* To view any description associated with a task, select the information icon to the right of the task name.
* To execute a slash command associated with a task, select **Run** next to the listed slash command. Configured slash commands may be run as often as necessary.

.. image:: ../images/IC-ad-hoc-tasks.gif

Changing owners
~~~~~~~~~~~~~~~

To change playbook owners you can run the ``/playbook owner @username`` slash command from within the run's channel. To change the owner to a user who is not in the channel, first add the user to the channel.

Providing a status update
~~~~~~~~~~~~~~~~~~~~~~~~~

Status updates ensure that stakeholders remain informed about the playbook run's progress. To post a status update:

1. Go to **Main Menu > Playbooks**.
2. Open the run you want to update and select **Go to channel**.
3. Select **Post update**.

 * If this is the first status update and the playbook has a defined template, that template will be pre-populated here.
 * If this is a subsequent status update, the message from the last status update will be pre-populated here.

4. Select a status and add a Markdown-formatted message.
5. Optionally set a reminder to prompt for the next status update.

 * If this is the first status update and the playbook has a defined default reminder timer, that timer will be pre-selected here.
 * If this is a subsequent status update, the last reminder timer will be pre-populated here.

6. Select **Update Status** to post your status update.

 * Status updates are posted to the incident channel as a message from the user providing the status update.
 * If the playbook has a defined broadcast channel, status updates are copied to the broadcast channel as a message from the incident bot.

The most recent status post will also appear in the right-hand sidebar of the run channel. To correct or remove a status post, edit or delete the post as needed. Status updates that are broadcast to another channel will not be edited or deleted.

Ending a playbook run
~~~~~~~~~~~~~~~~~~~~~

Playbook run members can end an incident using the ``/playbook end`` slash command. Playbook runs can also be ended from the desktop or browser:

1. Select the **Playbook** icon in the channel header to open the RHS.
2. Find the playbook run you're looking for and select **Go to channel**.
3. Select **Update Status**.
4. From the **Status** drop-down menu, select **Resolved**.
5. Enter a message with additional details.
6. Select **Update Status**.

Ending a playbook run signals to all members of the channel that the playbook run is complete. Members of the team can continue to post in the channel, mark tasks as complete, and change the owner if needed.

Restarting a playbook run
~~~~~~~~~~~~~~~~~~~~~~~~~

If a playbook run was ended prematurely, it can be restarted within the channel using the ``/playbook restart`` slash command. Runs can also be restarted from the desktop or browser:

1. Select the **Playbook** icon in the channel header to open the RHS.
2. Find the playbook run you're looking for and select **Go to channel**.

Playbook dashboard
------------------

Each playbook has a dashboard with details such as how many runs using the playbook are currently in progress, total runs per week over a 12-week period, and a list of runs with details such as status, duration, owner/participants, and tasks finished.

.. image:: ../images/Playbook-dashboard.png
   :alt: View and track playbook information.
