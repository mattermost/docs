.. _interactive-message-buttons:

Interactive Message Buttons (Beta)
===================================

Mattermost supports interactive message buttons for `incoming <https://docs.mattermost.com/developer/webhooks-incoming.html>`_ and `outgoing webhooks <https://docs.mattermost.com/developer/webhooks-outgoing.html>`_, and for `custom slash commands <https://docs.mattermost.com/developer/slash-commands.html>`_ via actions. They help make your integrations richer by completing common tasks inside Mattermost conversations, increasing user engagement and productivity.

Use these buttons to simplify complex workflows by allowing users to take quick actions directly through your integration post. For example, the buttons enable your integration to:

- update sales opportunities in your CRM system from Mattermost
- conduct a customer survey or a poll
- file a report on market trends

Interactive message buttons are not yet supported on Mattermost mobile apps.

// XXX Add GIF image (AB preparing one for marketing)

.. toctree::
   :maxdepth: 2

Button Options
---------------

Add message buttons as ``actions`` in your integration `message attachments <https://docs.mattermost.com/developer/message-attachments.html>`_. Each attachment can contain up to XXX actions. // XXX @ccbrown how many?

The following payload gives an example webhook that uses message buttons.

.. code-block:: text

  {
    "attachments": [
      {
        "pretext": "This is the attachment pretext.",
        "text": "This is the attachment text.",
        "actions": [
          {
            "name": "Ephemeral Message",
            "integration": {
              "url": "http://127.0.0.1:7357",
              "context": {
                "action": "ephemeral"
              }
            }
          }, {
            "name": "Update",
            "integration": {
              "url": "http://127.0.0.1:7357",
              "context": {
                "action": "update"
              }
            }
          }
        ]
      }
    ]
  }

The integration can respond with an update to the original post, or with an ephemeral message:

.. code-block:: text

  {
    "update": {
      "message": "Updated!"
    },
    "ephemeral_text": "You updated the post!"
  }

.. image:: ../../source/images/interactive_message.gif

Below we give a brief description of each parameter to help you customize the webhook post in Mattermost. For more information on message attachments, `see our documentation <https://docs.mattermost.com/developer/message-attachments.html>`_.

Name
  Give your action a descriptive name.

URL
  The actions are backed by an integration that handles HTTP POST requests when users clicks the message button. The URL parameter determines where this action is sent to. The request contains an ``application/json`` JSON string.

Context
  The requests sent to the specified URL contain the user id and any context that was provided in the action definition. A simple example is given below:
  
  .. code-block:: text

    {
    "user_id": "rd49ehbqyjytddasoownkuqrxe",
    "context": {
      "action": "ephemeral"
      }
    }

  In most cases, your integration will do one or both of these things:
  
  1. **Identifying which action was triggered**. For example, a GitHub integration might store something like this in the context:

    .. code-block:: text

      {
      "user_id": "rd49ehbqyjytddasoownkuqrxe",
      "context": {
        "repo": "mattermost/mattermost-server"
        "pr": 1234,
        "action": "merge"
        }
      }
      
  When the message button is clicked, your integration sends a request to the specified URL with the intention to merge the pull request identified by the context.

  2. **Authenticating the server**. An important property of the context parameter is that it's kept confidential. Hence, if your integration is not behind a firewall, you could add a token to your context without users ever being able to see it:

    .. code-block:: text

      {
      "user_id": "rd49ehbqyjytddasoownkuqrxe",
      "context": {
        "repo": "mattermost/mattermost-server"
        "pr": 1234,
        "action": "merge",
        "token": "somerandomlygeneratedsecret"
        }
      }
   
  Then, when your integration receives the request, it can verify that the token matches one that you previously generated and know that the request is legitimately coming from the Mattermost server and not forged.

  Depending on the application, integrations can also perform authentication statelessly with cryptographic signatures such as:

    .. code-block:: text

      {
      "user_id": "rd49ehbqyjytddasoownkuqrxe",
      "context": {
        "repo": "mattermost/mattermost-server"
        "pr": 1234,
        "action": "merge",
        "signature": "mycryptographicsignature"
        }
      }

  It's also possible for integrations to do both of these things with a single token and use something like this as context:

    .. code-block:: text

      {
      "user_id": "rd49ehbqyjytddasoownkuqrxe",
      "context": {
        "action_id": "someunguessableactionid"
        }
      }

  Then, when the integration receives the request, it can act based on the action id.

Tips and Best Practices
------------------------

// XXX @ccbrown Do we want to clean up the polling integration demo and provide it as an example? https://github.com/ccbrown/interactive-post-demo

1. The external application may be written in any programming language. It needs to provide a URL which receives the request sent by your Mattermost server and responds with in the required JSON format.
2. Message attachments allow for rich formatting, but don't go overboard. Use the least amount of formatting and number of action buttons required for your integration post.

// XXX @ccbrown

Share Your Integration
-----------------------

If you've built an integration for Mattermost, please consider `sharing your work <https://www.mattermost.org/share-your-mattermost-projects/>`_ in our `app directory <https://about.mattermost.com/default-app-directory/>`_.

The `app directory <https://about.mattermost.com/default-app-directory/>`_ lists open source integrations developed by the Mattermost community and are available for download, customization and deployment to your private cloud or on-prem infrastructure.

Slack Compatibility
--------------------

// XXX @ccbrown, please help with how one can turn a Slack-type message button into a Mattermost one? It was just a few tweaks if I remember correctly?

Troubleshooting
--------------------

// XXX @ccbrown, any here that we should add?
