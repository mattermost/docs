Interact with playbooks
=======================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Slash commands
--------------

Slash commands are available for playbooks. The ``/playbook`` slash command allows interaction with incidents via the post textbox on desktop, browser, and mobile. To run a playbook use the ``/playbook run`` slash command from any channel.

Available slash commands include:

- ``/playbook run`` - Run a playbook.
- ``/playbook finish`` - Finish the playbook run in this channel.
- ``/playbook update`` - Provide a status update.
- ``/playbook check [checklist #] [item #]`` - Check/uncheck the checklist item.
- ``/playbook checkadd [checklist #] [item text]`` - Add a checklist item.
- ``/playbook checkremove [checklist #] [item #]`` - Remove a checklist item.
- ``/playbook owner [@username]`` - Show or change the current owner.
- ``/playbook info`` - Show a summary of the current playbook run.
- ``/playbook timeline`` - Show the timeline for the current playbook run.
- ``/playbook todo`` - Get a list of your assigned tasks.
- ``/playbook settings digest [on/off]`` - Turn daily digest on/off.
- ``/playbook settings weekly-digest [on/off]`` - Turn weekly digest on/off.

API documentation
-----------------

To interact with the data model programmatically, consult the `REST API specification <https://github.com/mattermost/mattermost-plugin-incident-collaboration/blob/master/server/api/api.yaml>`_.

Playbooks help streamline and manage complex processes while decreasing the risk of forgotten steps or tasks. They also support tool integration, status updates in a dedicated channel, and can be edited on the fly. When a playbook run is finished, you can review the entire run to assess any areas of improvement for the next run.
