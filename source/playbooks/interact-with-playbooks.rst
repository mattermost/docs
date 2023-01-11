Interact with playbooks
=======================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Slash commands
--------------

Slash commands are available for playbooks. The ``/playbook`` slash command allows interaction with incidents via the post textbox on desktop, browser, and mobile. To run a playbook use the ``/playbook run`` slash command from any channel.

Available slash commands include:

- ``/playbook run`` - Start a playbook run.
- ``/playbook end`` - End a playbook run.
- ``/playbook update`` - Update the current playbook run's status.
- ``/playbook restart`` - Restart an ended playbook run.
- ``/playbook check [checklist item]`` - Check/uncheck the specified task.
- ``/playbook announce ~[channels]`` - Announce the current playbook run in other channels.
- ``/playbook list`` - List all your ongoing playbook runs.
- ``/playbook owner [@username]`` - Show or change the current playbook run owner.
- ``/playbook info`` - Show a summary of the current playbook's activities.

API documentation
-----------------

To interact with the data model programmatically, consult the `REST API specification <https://github.com/mattermost/mattermost-plugin-incident-collaboration/blob/master/server/api/api.yaml>`_.

Playbooks help streamline and manage complex processes while decreasing the risk of forgotten steps or tasks. They also support tool integration, status updates in a dedicated channel, and can be edited on the fly. When a playbook run is finished, you can review the entire run to assess any areas of improvement for the next run.
