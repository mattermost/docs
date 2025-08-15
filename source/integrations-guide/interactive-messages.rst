Interactive Messages
====================

Mattermost supports interactive message buttons and menus for incoming and outgoing webhooks, custom slash commands, and plugins via actions. They help make your integrations richer by completing common tasks inside Mattermost conversations, increasing user engagement and productivity.

.. image:: ../images/interactive-messages.png
   :alt: Example of an interactive message with buttons.

For information on interactive dialogs, see :doc:`/integrations-guide/interactive-dialogs`.

Use interactive messages to simplify complex workflows by allowing users to take quick actions directly from your integration's posts. For example, they enable your integration to:

- Mark a task as complete in your project management tracker.
- Conduct a customer survey or a poll.
- Initiate a command to merge a branch into a release.

Message Buttons
---------------

Add message buttons as ``actions`` in your integration's :doc:`message attachments </integrations-guide/message-attachments>`.

The following payload is an example that uses message buttons:

.. code-block:: json
   :linenos:

    {
      "attachments": [
        {
          "pretext": "This is the attachment pretext.",
          "text": "This is the attachment text.",
          "actions": [
            {
              "id": "message",
              "name": "Ephemeral Message",
              "integration": {
                "url": "http://127.0.0.1:7357",
                "context": {
                  "action": "do_something_ephemeral"
                }
              }
            }, {
              "id": "update",
              "name": "Update",
              "integration": {
                "url": "http://127.0.0.1:7357",
                "context": {
                  "action": "do_something_update"
                }
              }
            }
          ]
        }
      ]
    }

When a user clicks a button, your integration receives a request. In the HTTP response, your integration can choose to update the original post, and/or respond with an ephemeral message:

.. code-block:: json

    {
      "update": {
        "message": "Updated!",
        "props": {}
      },
      "ephemeral_text": "You updated the post!"
    }

.. image:: ../images/interactive_message.gif
   :alt: Animation showing an interactive message being updated.

Button actions support a ``style`` parameter to change their color. The possible values are ``good``, ``warning``, ``danger``, ``default``, ``primary``, and ``success``. Using theme variables or hex colors is discouraged as they may not be resilient to theme changes.

.. image:: ../images/interactive_button_style.png
   :alt: Examples of different button styles.

Message Menus
-------------

Similar to buttons, you can add message menus as ``actions`` in your integration's :doc:`message attachments </integrations-guide/message-attachments>`.

.. image:: ../images/message-menus.png
   :alt: Example of an interactive message menu.

The following payload is an example that uses a message menu:

.. code-block:: json
   :linenos:

    {
      "attachments": [
        {
          "pretext": "This is the attachment pretext.",
          "text": "This is the attachment text.",
          "actions": [
            {
              "id": "actionoptions",
              "name": "Select an option...",
              "integration": {
                "url": "http://127.0.0.1:7357/actionoptions",
                "context": {
                  "action": "do_something"
                }
              },
              "type": "select",
              "options": [
                {
                  "text": "Option1",
                  "value": "opt1"
                },
                {
                  "text": "Option2",
                  "value": "opt2"
                },
                {
                  "text": "Option3",
                  "value": "opt3"
                }
              ]
            }
          ]
        }
      ]
    }

The integration can respond with an update to the original post or with an ephemeral message, just like with buttons.

Message Menus for Channels
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can provide a list of public channels for users to select from. Specify ``channels`` as your action's ``data_source``:

.. code-block:: json

    {
      "type": "select",
      "data_source": "channels"
    }

Message Menus for Users
~~~~~~~~~~~~~~~~~~~~~~~

Similarly, you can provide a list of users. The user can choose any user in the system. Specify ``users`` as your action's ``data_source``:

.. code-block:: json

    {
      "type": "select",
      "data_source": "users"
    }

Parameters
----------

Each action in a message attachment is a JSON object with the following parameters:

.. list-table::
   :widths: 15 85
   :header-rows: 1

   * - Parameter
     - Description
   * - ``id``
     - A unique identifier for the action. Must consist of only letters and numbers.
   * - ``name``
     - A descriptive name for the action, which is used as the button text or the menu placeholder.
   * - ``type``
     - The type of action. Can be ``button`` or ``select``.
   * - ``style``
     - (For buttons) Changes the color of the button. Options are ``good``, ``warning``, ``danger``, ``default``, ``primary``, ``success``.
   * - ``options``
     - (For menus) An array of ``{"text": "display text", "value": "option_value"}`` objects.
   * - ``data_source``
     - (For menus) Set to ``channels`` or ``users`` to populate the menu dynamically.
   * - ``integration``
     - An object containing the ``url`` and ``context`` for the action.

The ``integration`` object has two fields:

- **URL**: The endpoint where the action payload is sent via an HTTP POST request. As of Mattermost v5.14, relative URLs are accepted.
- **Context**: A JSON object that is sent back to your integration. It allows your integration to track the state and verify the authenticity of the request.

Request and Response Flow
-------------------------

When a user interacts with a button or menu, Mattermost sends a request to the URL specified in the action's ``integration`` object.

Request Payload
~~~~~~~~~~~~~~~

The request from Mattermost to your integration will contain a JSON body similar to this:

.. code-block:: json

    {
        "user_id": "rd49ehbqyjytddasoownkuqrxe",
        "post_id": "gqrnh3675jfxzftnjyjfe4udeh",
        "channel_id": "j6j53p28k6urx15fpcgsr20psq",
        "team_id": "5xxzt146eax4tul69409opqjlf",
        "context": {
            "action": "do_something"
        }
    }

If the action was a menu selection, the context will also contain a ``selected_option`` field with the value of the chosen option.

The ``context`` is crucial for two main reasons:
1.  **Identifying the action**: Store information like a repository name or a pull request ID to know what action to perform.
2.  **Authenticating the request**: Include a secret token or a cryptographic signature in the context. Your integration can then verify this token to ensure the request is from Mattermost and not forged.

Response Payload
~~~~~~~~~~~~~~~~

Your integration should respond to the request with a JSON object. You can either update the original message or send an ephemeral message to the user who initiated the action.

.. code-block:: json

    {
      "update": {
        "message": "This message has been updated.",
        "props": {}
      },
      "ephemeral_text": "This is a temporary confirmation message."
    }

- **update**: An object containing a new ``message`` and/or ``props`` to replace the content of the original post.
- **ephemeral_text**: A string that will be displayed as a temporary message visible only to the user who triggered the action.

Slack Compatibility
-------------------

The schema for interactive messages is similar to Slack's. However, Mattermost allows an integration to create an interactive message without the pre-configuration that Slack requires.

If your ``ephemeral_text`` is not handled correctly by the Slack-compatibility logic, you can bypass it by sending ``"skip_slack_parsing": true`` in your response.

Frequently Asked Questions
--------------------------

**Are message buttons and menus supported in ephemeral messages?**

Yes, they are supported in ephemeral messages in Mattermost v5.10 and later on browsers and desktop apps.

**Why does an interactive button or menu return a 400 error?**

This is likely for one of three reasons:
1.  Mattermost could not connect to the integration. If the integration is on an internal network, the URL may need to be whitelisted in ``System Console > Environment > Web Server``.
2.  The integration did not return an HTTP 200 status code.
3.  The integration did not return a valid JSON response.

Check the Mattermost server logs for detailed error messages.

**How do I manage the properties of an interactive message?**

When responding with an ``update``, you can use ``update.props`` to modify the properties of the original message post:
- ``update.props == nil`` (not included): The ``props`` of the original message are not changed.
- ``update.props == {}`` (empty object): All properties are cleared from the original message, except for username, icon, pinned status, and emoji reactions.
- ``update.props == {"some": "props"}``: The original message's props are replaced with the new ones.

Share Your Integration
----------------------

If you've built an integration for Mattermost, please consider sharing your work in our `App Directory <https://mattermost.com/marketplace/>`_.
