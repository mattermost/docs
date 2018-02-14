.. _incoming_webhooks:

Incoming Webhooks
=================

Mattermost supports webhooks to easily integrate external applications into the server.

Use incoming webhooks to post messages to Mattermost public channels, private channels, and direct messages. Messages are sent via an HTTP POST request to a Mattermost URL generated for each application and contain a specifically formatted JSON payload in the request body.

.. image:: ../images/incoming_webhooks_sample.png
  :width: 500 px
*An example of a GitHub integration that posts updates to a Developers channel*


Use `curl <https://curl.haxx.se/>`_, a simple command line tool for sending HTTP requests in the examples that follow.

.. toctree::
   :maxdepth: 2

Simple Incoming Webhook
-----------------------------------

Let's learn how to create a simple incoming webhook that posts the following message to Mattermost.

.. image:: ../images/incoming_webhooks_create_simple.png
  :width: 400 px
  
1. First, go to **Main Menu > Integrations > Incoming Webhook**. If you don't have the **Integrations** option in your Main Menu, incoming webhooks may not be enabled on your Mattermost server or may be disabled for non-admins. Enable them from **System Console > Integrations > Custom Integrations** or ask your System Administrator to do so.
2. Click **Add Incoming Webhook** and add name and description for the webhook.
3. Select the channel to receive webhook payloads, then click **Add** to create the webhook.
4. Use a curl command from your terminal or commandline to send the following JSON payload in a HTTP POST request:

.. code-block:: text

  curl -i -X POST -H 'Content-Type: application/json' -d '{"text": "Hello, this is some text\nThis is more text. :tada:"}' http://{your-mattermost-site}/hooks/xxx-generatedkey-xxx
  # or
  curl -i -X POST --data-urlencode 'payload={"text": "Hello, this is some text\nThis is more text. :tada:"}' http://{your-mattermost-site}/hooks/xxx-generatedkey-xxx

If you're running cURL on Windows, you need to wrap the payload with double quotes (``"``) instead of single quotes (``'``). Moreover, ensure inner double quotes are escaped with a backslash and that colons have no spaces. Here's an example payload on Windows:

.. code-block:: text

  curl -i -X POST -H 'Content-Type: application/json' -d '{\"text\": "Hello, this is some text\nThis is more text. :tada:\"}' http://{your-mattermost-site}/hooks/xxx-generatedkey-xxx

Parameters and Formatting
--------------------------

The following payload gives an example webhook that uses additional parameters and formatting options.

.. code-block:: text

  payload={
    "channel": "town-square",
    "username": "test-automation",
    "icon_url": "https://www.mattermost.org/wp-content/uploads/2016/04/icon.png",
    "text": "#### Test results for July 27th, 2017\n<!channel> please review failed tests.\n
    | Component  | Tests Run   | Tests Failed                                   |
    |:-----------|:-----------:|:-----------------------------------------------|
    | Server     | 948         | :white_check_mark: 0                           |
    | Web Client | 123         | :warning: 2 [(see details)](http://linktologs) |
    | iOS Client | 78          | :warning: 3 [(see details)](http://linktologs) |
    "
    }

This will be displayed in the Town Square channel.

.. image:: ../images/incoming_webhooks_full_example.png
  :width: 500 px

Below we give a brief description of each parameter to help you customize the webhook post in Mattermost.

Override the channel
~~~~~~~~~~~~~~~~~~~~~

You can override the channel the webhook posts to by specifying a ``channel`` parameter in your JSON payload.

For example, if you have a webhook created for *Town Square*, you can send a message to the *Off-Topic* channel via the same webhook URL by using the following payload.

.. code-block:: text

  payload={"channel": "off-topic", "text": "Hello, this is some text\nThis is more text. :tada:"}

.. note::
  Use the channel URL, not the channel display name, when specifying the ``channel`` parameter. For instance, use ``town-square``, not ``Town Square`` when posting messages to the Town Square channel.

To send a message to a direct message channel, add an "@" symbol followed by the username to the ``channel`` parameter.

.. code-block:: text

  payload={"channel": "@username", "text": "Hello, this is some text\nThis is more text. :tada:"}

Override the username
~~~~~~~~~~~~~~~~~~~~~

You can override the username the messages post as by specifying a ``username`` parameter in your JSON payload.

For example, to send the message as a ``webhook-bot``, use the following payload.

.. code-block:: text

  payload={"username": "webhook-bot", "text": "Hello, this is some text\nThis is more text. :tada:"}
  
.. image:: ../images/incoming_webhooks_override_username.png
  :width: 400 px

To prevent malicious users from trying to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`_ a *BOT* indicator appears next to posts coming from webhooks regardless of what username is specified.

.. note::
  `Enable integrations to override usernames <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-usernames>`_ must be set to `true` in `config.json` to override usernames. Enable them from **System Console > Integrations > Custom Integrations** or ask your System Administrator to do so. If not enabled, the username is set to `webhook`.

Override the profile picture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also override the profile picture the messages post with by specifying an ``icon_url`` parameter in your JSON payload.

For example, you can use the following payload to override the profile picture to use the image located at http://example.com/somecoolimage.jpg.

.. code-block:: text

  payload={"icon_url": "http://example.com/somecoolimage.jpg", "text": "Hello, this is some text\nThis is more text. :tada:"}

.. note::
  `Enable integrations to override profile picture icons <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-profile-picture-icons>`_ must be set to `true` in `config.json` to override profile picture icons. Enable them from **System Console > Integrations > Custom Integrations** or ask your System Administrator to do so. If not enabled, the icon of the creator of the webhook URL is used to post messages.

Mention notifications
~~~~~~~~~~~~~~~~~~~~~~

You can trigger mention notifications with your incoming webhook message. To trigger a mention, include *@username* or *<userid>* in the `text` parameter of the JSON payload.

Channels can be mentioned by including *@channel* or *<!channel>*. For example:

.. code-block:: text

  payload={"text": "<!channel> this is a notification."}

Markdown formatting
~~~~~~~~~~~~~~~~~~~~

A rich range of formatting unavailable in Slack is made possible through :doc:`markdown support <../help/messaging/formatting-text>` in Mattermost, including headings, formatted fonts, tables, inline images and other options supported by Mattermost Markdown. All of these options are also supported by incoming webhooks.

For example, to create a message with a heading, and an italicized text on the next line, use the following payload. 

.. code-block:: text

  payload={"text": "# This is a heading\n_This text is italicized._"}

.. image:: ../images/incoming_webhooks_markdown_formatting.png
  :width: 300 px

Messages with advanced formatting can be created by including an :doc:`attachment array <message-attachments>` and :doc:`interactive message buttons <interactive-message-buttons>` in the JSON payload.

Custom post type
~~~~~~~~~~~~~~~~~~

You can specify a custom post type `via client plugins <about.mattermost.com/default-plugins>`_ when sending a webhook message. To set the type, use the `type` parameter on the JSON payload.

.. code-block:: text

  payload={"username": "webhook-bot", "text": "Hello, this is some text\nThis is more text. :tada:", "type": "custom_type_here"}

Tips and Best Practices
------------------------

1. Webhooks are designed to easily allow you to post messages. For other actions such as channel creation, you must also use the `Mattermost APIs <../developer/api.html>`_.

2. If the text is longer than 4000 characters, the message is split into multiple consecutive posts, each within the 4000 character limit.

3. You can restrict who can create incoming webhooks in `System Console > Integrations > Custom Integrations <https://docs.mattermost.com/administration/config-settings.html#restrict-managing-integrations-to-admins>`_.

4. Mattermost incoming webhooks are Slack-compatible. You can copy-and-paste code used for a Slack incoming webhook to create Mattermost integrations. Mattermost `automatically translates the Slack's proprietary JSON payload format <../developer/webhooks-incoming#translate-slacks-proprietary-data-format-to-mattermost>`_.

5. The external application may be written in any programming language as long as it supports sending an HTTP POST request in the required JSON format to a specified Mattermost URL.

6. For the HTTP request body, if `Content-Type` is specified as ``application/json`` in the header of the HTTP request, then the body can be direct JSON. For example,

.. code-block:: text

  {"text": "Hello, this is some text."}

Share Your Integration
-----------------------

If you've built an integration for Mattermost, please consider `sharing your work <https://www.mattermost.org/share-your-mattermost-projects/>`_ in our `app directory <https://about.mattermost.com/default-app-directory/>`_.

The `app directory <https://about.mattermost.com/default-app-directory/>`_ lists open source integrations developed by the Mattermost community and are available for download, customization and deployment to your private cloud or on-prem infrastructure.

Slack Compatibility
-------------------

Mattermost makes it easy to migrate integrations written for Slack to Mattermost. 

Translate Slack's proprietary data format to Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost automatically translates the data coming from Slack:

1. JSON payloads written for Slack, that contain the following, are translated to Mattermost markdown and rendered equivalently to Slack:
   
   - *<>* to denote a URL link, such as ``payload={"text": "<http://www.mattermost.com/>"}``
   - *|* within a *<>* to define linked text, such as ``payload={"text": "Click <http://www.mattermost.com/|here> for a link."}``

2. You can override the channel name with a *@username*, such as ```payload={"text": "Hi", channel: "@jim"}`` to send a direct message like in Slack.
3. You can prepend a channel name with *#* and the message will still be sent to the correct channel like in Slack.

Mattermost webhooks in GitLab using Slack UI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GitLab is the leading open-source alternative to GitHub and offers built-in integrations with Slack. You can use the Slack interface in GitLab to add Mattermost webhooks directly without changing code:

1. In GitLab, go to **Settings > Services** and select **Slack**.
2. Paste the incoming webhook URL provided by Mattermost from **Main Menu > Integrations > Incoming Webhooks**.
3. Optionally set the **Username** you'd like displayed when the notification is made. Leave the **Channel** field blank.
4. Click **Save** then test the settings to confirm messages are sent successfully to Mattermost.

Known Slack compatibility issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Using ``icon_emoji`` to override the username is not supported.
2. Referencing  channels using <#CHANNEL_ID> does not link to the channel.
3. ``<!everyone>`` and ``<!group>`` are not supported.
4. Parameters "mrkdwn", "parse", and "link_names" are not supported. Mattermost converts Markdown by default and automatically links @mentions.
5. Bold formatting as ``*bold*`` is not supported (must be done as ``**bold**``).
6. Webhooks cannot direct message the user who created the webhook.

Troubleshooting
---------------

To debug incoming webhooks in **System Console > Logs**, set **System Console > Logging > Enable Webhook Debugging** to ``true`` and set **System Console > Logging > Console Log Level** to ``DEBUG``.

Some common error messages include:

1. ``Couldn't find the channel``: Indicates that the channel doesn't exist or is invalid. Please modify the ``channel`` parameter before sending another request.
2. ``Couldn't find the user``: Indicates that the user doesn't exist or is invalid. Please modify the ``channel`` parameter before sending another request.
3. ``Unable to parse incoming data``: Indicates that the request received is malformed. Try reviewing that the JSON payload is in a correct format and doesn't have typos such as extra `"`.
4. ``curl: (3) [globbing] unmatched close brace/bracket in column N``: Typically an error when using cURL on Windows, when:
  1. You have space around JSON separator colons, ``payload={"Hello" : "test"}`` or  
  2. You are using single quotes to wrap the ``-d`` data, ``-d 'payload={"Hello":"test"}'``

If your integration prints the JSON payload data instead of rendering the generated message, make sure your integration is returning the ``application/json`` content-type.
