Incoming Webhooks
=================

Incoming webhooks allow external applications to post messages into Mattermost channels and direct messages. They are a simple way to receive notifications and data from other services in real-time.

All webhook posts will display a ``BOT`` indicator next to the username in Mattermost clients to help prevent against phishing attacks.

Create an Incoming Webhook
--------------------------

1.  In Mattermost, go to **Product Menu > Integrations > Incoming Webhooks**.

    .. note::
       If you don't have the **Integrations** option, incoming webhooks may not be enabled on your Mattermost server or may be disabled for non-admins. A System Admin can enable them from **System Console > Integrations > Integration Management**.

2.  Select **Add Incoming Webhook** and add a name and description for the webhook.
3.  Select the channel to receive webhook payloads, then select **Add** to create the webhook.

This will generate a unique webhook URL, which will look something like this:
``https://your-mattermost-server.com/hooks/xxx-generatedkey-xxx``

.. warning::
   Treat this URL as a secret. Anyone who has it will be able to post messages to your Mattermost instance.

Here's an example of a simple message created with an incoming webhook:

.. image:: ../images/incoming_webhooks_create_simple.png
   :alt: An incoming webhook message saying "Hello, this is some text. This is some more text."

Use an Incoming Webhook
------------------------

To post a message, your application needs to send an HTTP POST request to the webhook URL with a JSON payload in the request body.

.. code-block:: bash

    curl -i -X POST -H 'Content-Type: application/json' -d '{"text": "Hello, this is some text\nThis is more text. :tada:"}' https://your-mattermost-server.com/hooks/xxx-generatedkey-xxx

A successful request will receive an HTTP 200 response with `ok` in the response body.

For compatibility with Slack incoming webhooks, if no ``Content-Type`` header is set, the request body must be prefixed with ``payload=``.

Parameters
----------

The JSON payload can contain the following parameters:

.. list-table::
   :widths: 20 15 65
   :header-rows: 1

   * - Parameter
     - Required
     - Description
   * - ``text``
     - Yes (if ``attachments`` is not set)
     - `Markdown-formatted <https://docs.mattermost.com/messaging/formatting-text.html>`_ message. Use ``@<username>``, ``@channel``, and ``@here`` for notifications.
   * - ``channel``
     - No
     - Overrides the default channel. Use the channel's name (e.g., ``town-square``), not the display name. Use ``@<username>`` to send a Direct Message. The webhook can post to any public channel, and any private channel the creator is a member of.
   * - ``username``
     - No
     - Overrides the default username. The `Enable integrations to override usernames <https://docs.mattermost.com/configure/configuration-settings.html#enable-integrations-to-override-usernames>`_ setting must be enabled.
   * - ``icon_url``
     - No
     - Overrides the default profile picture URL. The `Enable integrations to override profile picture icons <https://docs.mattermost.com/configure/configuration-settings.html#enable-integrations-to-override-profile-picture-icons>`_ setting must be enabled.
   * - ``icon_emoji``
     - No
     - Overrides the ``icon_url`` with an emoji. Use the emoji name (e.g., ``:tada:``). The `Enable integrations to override profile picture icons <https://docs.mattermost.com/configure/configuration-settings.html#enable-integrations-to-override-profile-picture-icons>`_ setting must be enabled.
   * - ``attachments``
     - Yes (if ``text`` is not set)
     - An array of :doc:`message attachment </integrations-guide/message-attachments>` objects for richer formatting.
   * - ``type``
     - No
     - Sets the post type, mainly for use by plugins. If set, must begin with ``custom_``.
   * - ``props``
     - No
     - A JSON object for storing metadata. The ``card`` property can be used to display extra Markdown-formatted text in the post's info panel (RHS). This is available in Mattermost v5.14 and later, and is not yet supported on mobile.
   * - ``priority``
     - No
     - Sets the priority of the message. See :doc:`message priorities </integrations-guide/message-priorities>`.

Example with Parameters
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

    {
      "channel": "town-square",
      "username": "test-automation",
      "icon_url": "https://mattermost.com/wp-content/uploads/2022/02/icon.png",
      "text": "#### Test results for July 27th, 2017\n@channel please review failed tests.\n\n| Component  | Tests Run   | Tests Failed                                   |\n|:-----------|:-----------:|:-----------------------------------------------|\n| Server     | 948         | :white_check_mark: 0                           |\n| Web Client | 123         | :warning: 2 [(see details)](https://linktologs) |\n| iOS Client | 78          | :warning: 3 [(see details)](https://linktologs) |"
    }

This renders as:

.. image:: ../images/incoming_webhooks_full_example.png
   :alt: Example of a webhook post with a custom username, icon, and formatted text.

Example with Card Prop
~~~~~~~~~~~~~~~~~~~~~~

Using the ``card`` property inside ``props`` will display an info icon on the post. Clicking the icon opens the right-hand sidebar to display the content.

.. code-block:: json

    {
      "channel": "town-square",
      "username": "Winning-bot",
      "text": "#### We won a new deal!",
      "props": {
        "card": "Salesforce Opportunity Information:\n\n [Opportunity Name](https://salesforce.com/OPPORTUNITY_ID)\n\n-Salesperson: **Bob McKnight** \n\n Amount: **$300,020.00**"
      }
    }

.. image:: ../images/card-prop-example.png
   :alt: Example of a post with a card property displaying more information in the sidebar.

Slack Compatibility
-------------------

Mattermost provides compatibility with Slack's webhook format to make migration easier.

Translating Slack's Data Format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost automatically translates JSON payloads from Slack format:
- ``<https://mattermost.com/>`` is rendered as a link.
- ``<https://mattermost.com/|Click here>`` is rendered as linked text.
- ``<userid>`` triggers a user mention.
- ``<!channel>``, ``<!here>``, or ``<!all>`` trigger channel-wide mentions.

You can also send a direct message by overriding the channel name with ``@username``, e.g., ``"channel": "@jim"``.

Using Mattermost Webhooks in GitLab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use GitLab's built-in Slack integration to send notifications to Mattermost:
1. In GitLab, go to **Settings > Services** and select **Slack**.
2. Paste the Mattermost incoming webhook URL.
3. Optionally, set a **Username**. Leave the **Channel** field blank.
4. Select **Save** and test the integration.

Known Slack Compatibility Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Referencing channels using ``<#CHANNEL_ID>`` is not supported.
- ``<!everyone>`` and ``<!group>`` are not supported.
- ``*bold*`` formatting is not supported; use ``**bold**`` instead.
- Webhooks cannot send a direct message to the user who created the webhook.

Troubleshooting
---------------

To debug incoming webhooks, a System Admin can enable **Webhook Debugging** and set the **Console Log Level** to **DEBUG** in **System Console > Logging**.

Common error messages include:
- **Couldn't find the channel**: The channel specified in the ``channel`` parameter does not exist.
- **Couldn't find the user**: The user specified does not exist.
- **Unable to parse incoming data**: The JSON payload is malformed.

If your integration posts the JSON payload as plain text instead of a rendered message, ensure the request includes the ``Content-Type: application/json`` header.
