Slash Commands
===============

.. include:: ../_static/badges/all-commercial.rst
  :start-after: :nosearch:

.. toctree::
   :maxdepth: 1
   :hidden:
   :titlesonly:

   built-in-slash-commands
   run-slash-commands

Execute actions with simple commands inside Mattermost. Learn how to :doc:`run Mattermost slash commands </integrations-guide/run-slash-commands>`.

Built-in slash commands
------------------------

**Technical complexity:** :ref:`No-code <no-code>`

These out-of-the-box commands enable command line interaction with users, channels, and conversations. Examples of pre-built slash commands include ``/invite`` to add teammates to a channel, ``/header`` to set a channel description, or ``/call`` to start or join a call in a channel.

Additionally, you can interact with the data model programmatically using `API endpoints <https://api.mattermost.com/>`__. Responses are posted as the user who invoked the command, with possible username/icon overrides.

Learn more about :doc:`built-in slash commands </integrations-guide/built-in-slash-commands>` available in Mattermost.

Custom slash commands
----------------------

**Technical complexity:** :ref:`Low-code <low-code>`

Slash commands are similar to an outgoing webhooks, but instead of listening for keywords in a channel they are triggered by users explicitly typing a preconfigured command. Using slash commands is similar to using a command line within a channel. This means if you type in a slash command it will execute without posting a message, whereas an outgoing webhook is only triggered by posted messages. The external service then processes the request and can return a response, such as plain text, rich message content, interactive buttons or forms, directly into the channel.

Mattermost's slash command format is Slack compatible, so you can easily migrate your commands from Slack.

Learn more about `building custom slash commands <https://developers.mattermost.com/integrate/slash-commands/custom/>`_.

Example Use Cases
~~~~~~~~~~~~~~~~~~

Here are some example use cases for slash commands in Mattermost:

**Project management**  

Typing ``/jira create`` opens an interactive dialog where you can file a new Jira issue directly from Mattermost, including fields like summary, description, and priority.

**Incident response**  

Using ``/pagerduty trigger`` can open a form to start a new incident, notify on-call responders, and post details back into the channel so the team can coordinate.

**Knowledge retrieval**  

A command like ``/docs search authentication`` queries your documentation system and returns a list of relevant articles as interactive message attachments with links.