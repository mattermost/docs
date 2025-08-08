Message Priorities
==================

Integrations can send messages with a priority level to help users identify the importance of the message. This is done by including a ``priority`` object in the post payload when creating a message.

For more information about how this feature works for end-users, see the `message priority documentation <https://docs.mattermost.com/collaborate/message-priority.html>`_.

Priority Options
----------------

The ``priority`` object is part of the post payload and supports the following fields:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Field
     - Description
   * - ``priority``
     - (Required) A string indicating the priority level. Can be ``"urgent"`` or ``"important"``.
   * - ``requested_ack``
     - (Optional) When set to ``true``, the message will be marked as requiring an acknowledgment. This is only available for ``"urgent"`` and ``"important"`` priority messages.
   * - ``persistent_notifications``
     - (Optional) When set to ``true`` for an ``"urgent"`` message, recipients will receive a persistent notification every five minutes until they acknowledge the message.

Example: Urgent Priority
------------------------

Here is an example payload for creating a post with **Urgent** priority.

.. code-block:: json

    {
        "channel_id": "gmg7wbbcm78s7x549qg1xrmd9o",
        "message": "An urgent message that requires your immediate attention.",
        "priority": {
            "priority": "urgent"
        }
    }


This is how it renders in Mattermost:

.. image:: ../images/message-priority-urgent.jpg
   :alt: An urgent message with a red banner.

Example: Important Priority with Requested Acknowledgment
---------------------------------------------------------

Here is an example payload for creating a post with **Important** priority that requires acknowledgment.

.. code-block:: json

    {
        "channel_id": "gmg7wbbcm78s7x549qg1xrmd9o",
        "message": "An important message that requires acknowledgement.",
        "priority": {
            "priority": "important",
            "requested_ack": true
        }
    }


This is how it renders in Mattermost:

.. image:: ../images/message-priority-requested-ack.jpg
   :alt: An important message with an orange banner and an acknowledgment button.
