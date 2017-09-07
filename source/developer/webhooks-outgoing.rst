.. _outgoing-webhooks:

Outgoing Webhooks
=================

Mattermost supports webhooks to easily integrate external applications into the server.

Use outgoing webhooks to post automated responses to posts made by your users. Outgoing webhooks will send an HTTP POST request to a web service, and process a response back to Mattermost, when a message matches one or both of the following conditions:

 - It is posted in a specified channel
 - The first word matches or starts with one of the defined trigger words, such as ``gif``

  .. note::
    Outgoing webhooks are supported in public channels only. If you need a trigger that works in a private channel or a direct message, consider using a `slash command <https://docs.mattermost.com/developer/slash-commands.html>`_ instead.

.. toctree::
   :maxdepth: 2

Create an Outgoing Webhook
----------------------------

Suppose you want to write an external application, which executes software tests after someone posts a message starting with the word ``#build`` in the ``town-square`` channel.

You can follow these general guidelines to set up a Mattermost outgoing webhook for your application.

1 - First, go to **Main Menu > Integrations > Outgoing Webhook**. If you don't have the **Integrations** option in your Main Menu, outgoing webhooks may not be enabled on your Mattermost server or may be disabled for non-admins. Enable them from **System Console > Integrations > Custom Integrations** or ask your System Administrator to do so.

2 - Click **Add Outgoing Webhook** and add name and description for the webhook.

3 - Choose the content type by which the response will be sent.

 - If ``application/x-www-form-urlencoded`` is chosen, the Mattermost server assumes you will be encoding the parameters in a URL format.
 - If ``application/json`` is chosen, the Mattermost server assumes you will posting JSON data.

4 - Select the public channel to receive webhook payloads, or specify one or more trigger words that send an HTTP POST request to your application. You may configure either the channel or the trigger words for the outgoing webhook, or both. If both are specified, then the message must match both values.

In our example, we would set the channel to ``town-square`` and specify ``#build`` as the trigger word.

  .. note::
    If you leave the channel field blank, the webhook will respond to trigger words in all public channels of your team.
    
    Similarly, if you don't specify trigger words, then the webhook will respond to all messages in the selected public channel.

5 - If you specified one or more trigger words on the previous step, choose when to trigger the outgoing webhook.

 - If the first word of a message matches one of the trigger words exactly, or
 - If the first word of a message starts with one of the trigger words.

6 - Finally, set one or more callback URLs that HTTP POST requests will be sent to, and hit **Save**.

7 - On the next page, copy the **Token** value. This will be used in a later step.

.. image:: ../images/outgoing_webhooks_token.png
  :width: 500 px

8 - Next, write your external application. Include a function, which receives HTTP POST requests from Mattermost. The function should look something like this:

    .. code-block:: text

      Content-Length: 244
      User-Agent: Go 1.1 package http
      Host: localhost:5000
      Accept: application/json
      Content-Type: application/x-www-form-urlencoded

      channel_id=hawos4dqtby53pd64o4a4cmeoo&
      channel_name=town-square&
      team_domain=someteam&
      team_id=kwoknj9nwpypzgzy78wkw516qe&
      post_id=axdygg1957njfe5pu38saikdho&
      text=some+text+here&
      timestamp=1445532266&
      token=zmigewsanbbsdf59xnmduzypjc&
      trigger_word=some&
      user_id=rnina9994bde8mua79zqcg5hmo&
      user_name=somename

9 - Add a configurable *MATTERMOST_TOKEN* variable to your application and set it to the **Token** value from step 7. This value will be used by your application to confirm the HTTP POST request came from Mattermost.

10 - To have your application post a message back to ``town-square``, it can respond to the HTTP POST request with a JSON response payload such as:

.. code-block:: text

  {"text": "
  | Component  | Tests Run   | Tests Failed                                   |
  |:-----------|:------------|:-----------------------------------------------|
  | Server     | 948         | :white_check_mark: 0                           |
  | Web Client | 123         | :warning: [2 (see details)](http://linktologs) |
  | iOS Client | 78          | :warning: [3 (see details)](http://linktologs) |
  "}

which would render in Mattermost as:

.. image:: ../images/webhooksTable.PNG

11 - You're all set! See below for message formatting options for the JSON payload, as well as tips and best practices for setting up your outgoing webhook.

Parameters and Formatting
--------------------------

Below we give a brief description of additional parameters that help you customize the webhook post in Mattermost.

Override the username
~~~~~~~~~~~~~~~~~~~~~

You can override the username the messages posts as by specifying a ``username`` parameter in your JSON payload.

For example, to send the message as a ``webhook-bot``, use the following payload.

.. code-block:: text

  payload={"username": "webhook-bot", "text": "Hello, this is some text\nThis is more text. :tada:"}
  
.. image:: ../images/incoming_webhooks_override_username.png
  :width: 400 px

To prevent malicious users from trying to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`_ a *BOT* indicator appears next to posts coming from webhooks regardless of what username is specified.

.. note::
  `Enable integrations to override usernames <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-usernames>`_ must be set to `true` in `config.json` to override usernames. Enable them from **System Console > Integrations > Custom Integrations** or ask your System Administrator. If not enabled, the username is set to `webhook`.

Override the profile picture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also override the profile picture the messages post with by specifying an ``icon_url`` parameter in your JSON payload.

For example, you can use the following payload to override the profile picture to use the image located at http://example.com/somecoolimage.jpg.

.. code-block:: text

  payload={"icon_url": "http://example.com/somecoolimage.jpg", "text": "Hello, this is some text\nThis is more text. :tada:"}

.. note::
  `Enable integrations to override profile picture icons <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-profile-picture-icons>`_ must be set to `true` in `config.json` to override usernames. Enable them from **System Console > Integrations > Custom Integrations** or ask your System Administrator. If not enabled, the icon of the creator of the webhook URL is used to post messages.

Mention notifications
~~~~~~~~~~~~~~~~~~~~~~

You can trigger mention notifications with your outgoing webhook message. To trigger a mention, include *@username* in the `text` parameter of the JSON payload.

Channels can be mentioned by including *@channel* or *<!channel>*. For example:

.. code-block:: text

  payload={"text": "<!channel> this is a notification."}

Markdown formatting
~~~~~~~~~~~~~~~~~~~~

A rich range of formatting unavailable in Slack is made possible through :doc:`markdown support <../help/messaging/formatting-text>` in Mattermost, including headings, formatted fonts, tables, inline images and other options supported by Mattermost Markdown. All of these options are also supported by outgoing webhooks.

For example, to create a message with a heading, and an italicized text on the next line, use the following payload. 

.. code-block:: text

  payload={"text": "# This is a heading\n_This text is italicized._"}

.. image:: ../images/incoming_webhooks_markdown_formatting.png
  :width: 300 px

Messages with advanced formatting can be created by including an :doc:`attachment array <message-attachments>` in the JSON payload.

Tips and Best Practices
------------------------

1. Webhooks are designed to easily allow you to post messages. For other actions such as channel creation, you must also use the `Mattermost APIs <../developer/api.html>`_.

2. If the text in the JSON payload is longer than 4000 characters, the message is split into multiple consecutive posts, each within the 4000 character limit.

3. Outgoing webhooks are supported in public channels only. If you need a trigger that works in a private channel or a direct message, consider using a `slash command <https://docs.mattermost.com/developer/slash-commands.html>`_ instead.

4. You can restrict who can create outgoing webhooks in `System Console > Integrations > Custom Integrations <https://docs.mattermost.com/administration/config-settings.html#restrict-managing-integrations-to-admins>`_.

5. Mattermost outgoing webhooks are Slack-compatible. You can copy-and-paste code used for a Slack outgoing webhook to create Mattermost integrations. Mattermost `automatically translates the Slack's proprietary JSON payload format <../developer/webhooks-outgoing#translate-slacks-proprietary-data-format-to-mattermost>`_.

6. The external application may be written in any programming language. It needs to provide a URL which reacts to the request sent by your Mattermost server, and send an HTTP POST in the required JSON format as a response.
 
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

2. The HTTP POST request body sent to a web service is formatted the same as Slack's. This means your Slack integration's receiving function does not need change to be compatible with Mattermost.
  
Known Slack compatibility issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Using ``icon_emoji`` to override the username is not supported.
2. Referencing  channels using ``<#CHANNEL_ID>`` does not link to the channel.
3. ``<!here>``, ``<!everyone>``, and ``<!group>`` are not supported.
4. Parameters "mrkdwn", "parse", and "link_names" are not supported (Mattermost always converts markdown and automatically links @mentions).
5. Bold formatting supplied as ``*bold*`` is not supported (must be done as ``**bold**``).
6. Advanced formatting using :doc:`attachments <message-attachments>` is not yet supported.

Troubleshooting
---------------

To debug outgoing webhooks in **System Console > Logs**, set **System Console > Logging > Enable Webhook Debugging** to ``true`` and set **System Console > Logging > Console Log Level** to ``DEBUG``.
