Notifications and updates
=========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:
  
.. |vertical-3-dots| image:: ../images/dots-vertical_F01D9.svg
  :alt: Select the More icon to access additional channel management options.
  :class: theme-icon

There are multiple ways to receive updates and notifications.

Status updates
--------------

Status updates ensure that stakeholders remain informed about the playbook run’s progress. 

You can post a status update from the run channel and you can also configure the playbook to send a reminder to post a status update.

To post a status update, open the playbooks tab in Mattermost. Select the run you want to post the update for. In the run details page, select **Post update**.

   - If this is the first status update and the playbook has a defined template, that template will be pre-populated here.
   - If this is a subsequent status update, the message from the last status update will be pre-populated here.

3. Optionally set a reminder to prompt for the next status update.

   - If this is the first status update and the playbook has a defined default reminder timer, that timer will be pre-selected here.
   - If this is a subsequent status update, the last reminder timer will be pre-populated here.

4. Select **Post update** to post your status update.

If the playbook has a defined broadcast channel, status updates are copied to the broadcast channel as a message from the Playbooks bot.

The most recent status post will also appear in the right-hand sidebar of the run channel and in the timeline. To correct or remove a status post, edit or delete the post as needed. Note that status updates that are broadcast to another channel won’t be updated or removed if the original post is edited or deleted.

Request an update
-----------------

To request a status update, open the playbooks tab in Mattermost. Select the run you want an update for. In the run details page, select the |vertical-3-dots| menu next to **Post update** and select **Request update**.

Follow runs and playbooks
-------------------------

Follow specific playbooks to receive updates on important events such as when a run is started and finished, as well as status and retrospective updates every time that playbook is run. This is a good option if you’re interested in all instances of a specific workflow, such as an outage resolution playbook.

As a stakeholder, you can also choose to follow only a specific run. This means that while you don’t have to participate in the run, you’ll receive updates and can decide what, if any, actions to take. This is a good option if you’re only interested in a single instance of a procedure. For example, you may want to only follow customer onboarding for one specific customer instead of all onboarding runs.

Daily digest
------------

To help you keep track of your runs, tasks, and statuses, a daily digest is sent via direct message in Mattermost.

Running playbooks in multiple channels can be overwhelming. The daily digest is sent once a day, in the morning. It lists the actionable items for each run, as well as any outstanding tasks or status updates required. Select the run name to move to that channel.

The digest is on by default. To turn it off, use the slash command ``/playbook settings digest off``.

Playbook to do
--------------

As you complete tasks and finish runs, you can update the details in the digest using the slash command ``/playbook todo``. This slash command can be run in any channel, direct message, or group message. Once run, it delivers an updated digest which includes a list of active runs you belong to.
