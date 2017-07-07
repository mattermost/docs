.. _incoming_webhooks:

Incoming Webhooks
=================

Mattermost supports webhooks to easily integrate external applications into the platform.

Use incoming webhooks to post messages to Mattermost public channels, private channels, and direct messages. Messages are sent via an HTTP POST request to a Mattermost URL generated for each application and contain a specifically formatted JSON payload in the request body.

.. image:: ../images/incoming_webhooks_sample.png
*An example of a GitHub integration that posts updates to a Developers channel*

Creating a simple incoming webhook
-----------------------------------

Let's learn how to create a simple incoming webhook that posts the following message to Mattermost.

.. image:: ../images/incoming_webhooks_create_simple.png
  :width: 50 px
  
1. First, go to **Main Menu > Integrations > Incoming Webhook**. If you don't have the **Integrations** option in your Main Menu, incoming webhooks may not be enabled on your Mattermost server. Enable them from **System Console > Integrations > Custom Integrations** or ask your System Administrator.
2. Click **Add Incoming Webhook** and add name and description for the webhook.
3. Select the channel to receive webhook payloads, then click **Add** to create the webhook.
4. Use a curl command from your terminal or commandline to send the following JSON payload in a HTTP POST request:

  .. code-block::

    curl -i -X POST -d 'payload={"text": "Hello, this is some text\nThis is more text. :tada:"}' http://{your-mattermost-site}/hooks/xxx-generatedkey-xxx

Parameters and formatting
--------------------------

Below are additional parameters to customize the message posted to Mattermost.

Override the channel
~~~~~~~~~~~~~~~~~~~~~

You can override the channel the webhook posts to by specifying a ``channel`` parameter in your JSON payload.

For example, if you have a webhook created for *Town Square*, you can send a message to the *Off-Topic* channel via the same webhook URL by using the following payload.

  .. code-block::

    payload={"channel": "off-topic", "text": "Hello, this is some text\nThis is more text. :tada:"}

To send a message to a direct message channel, add an "@" symbol followed by the username to the ``channel`` parameter.

  .. code-block::

    payload={"channel": "@username", "text": "Hello, this is some text\nThis is more text. :tada:"}

Override the username
~~~~~~~~~~~~~~~~~~~~~

You can override the username the messages posts as by specifying a ``username`` parameter in your JSON payload.

For example, to send the message as a `webhook-bot`, use the following payload.

  .. code-block::

    payload={"username": "webhook-bot", "text": "Hello, this is some text\nThis is more text. :tada:"}
  
.. image:: ../images/incoming_webhooks_override_username.png
  :width: 50 px

To prevent malicious users from trying to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`_ a *BOT* indicator appears next to posts coming from webhooks regardless of what username is specified.

  .. note::
    `Enable integrations to override usernames <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-usernames>`_ must be set to `true` in `config.json` to override usernames. Enable them from **System Console > Integrations > Custom Integrations** or ask your System Administrator. If not enabled, the username is set to `webhook`.

Override the profile picture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also override the profile picture the messages post with by specifying an ``icon_url`` parameter in your JSON payload.

For example, you can use the following payload to override the profile picture to use the image located at http://example.com/somecoolimage.jpg.

  .. code-block::

    payload={"icon_url": "http://example.com/somecoolimage.jpg", "text": "Hello, this is some text\nThis is more text. :tada:"}

  .. note::
    `Enable integrations to override profile picture icons <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-profile-picture-icons>`_ must be set to `true` in `config.json` to override usernames. Enable them from **System Console > Integrations > Custom Integrations** or ask your System Administrator. If not enabled, the icon of the creator of the webhook URL is used to post messages.

Mention notifications
~~~~~~~~~~~~~~~~~~~~~~

You can trigger mention notifications with your incoming webhook message. To trigger a mention, include *@username* in the `text` parameter of the JSON payload.

Channels can mentioned by including *@channel* or *<!channel>*. For example:

 .. code-block::

    payload={"text": "<!channel> this is a notification."}

Markdown formatting
~~~~~~~~~~~~~~~~~~~~

A rich range of formatting unavailable in Slack is made possible through :doc:`markdown support <../help/messaging/formatting-text>` in Mattermost, including headings, formatted fonts, tables, inline images and other options supported by Mattermost Markdown. All of these options are also supported by incoming webhooks.

For example, to create a message with a heading, and an italicized text on the next line, use the following payload. 

  .. code-block::

    payload={"text": "# This is a heading\n_This text is italicized._"}

.. image:: ../images/incoming_webhooks_markdown_formatting.png

Messages with advanced formatting can be created by including an :doc:`attachment array <message-attachments>` in the JSON payload.

Complete incoming webhook example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following payload gives an example webhook that uses the attributes mentioned above.

  .. code-block::

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
  :width: 50 px

Tips and best practices
------------------------

1. Webhooks are designed to post messages. For other actions such as channel creation, use the `Mattermost APIs <../developer/api.html>`_.

2. If the text is longer than 4000 characters, the message is split into multiple consecutive posts, each within the 4000 character limit.

3. Mattermost incoming webhooks are Slack-compatible. You can copy-and-paste code used for a Slack incoming webhook to create Mattermost integrations. Mattermost `automatically translates the Slack's proprietary JSON payload format <../developer/webhooks-incoming#translate-slacks-proprietary-data-format-to-mattermost>`_.

4. The external application may be written in any programming language as long as it supports sending an HTTP POST request in the required JSON format to a specified Mattermost URL.

5. For the HTTP request body, if `Content-Type` is specified as `application/json` in the header of the HTTP request, then the body can be direct JSON. For example,

  .. code-block::

    {"text": "Hello, this is some text."}

6. It is often best to set up your integration running on Heroku, an AWS server or a server of your own before to test sending messages to Mattermost channels.

Share your integration
-----------------------

If you've built an integration for Mattermost, please consider `sharing your work <https://www.mattermost.org/share-your-mattermost-projects/>`_ in our `app directory <https://about.mattermost.com/default-app-directory/>`_.

The `app directory <https://about.mattermost.com/default-app-directory/>`_ lists open source integrations developed by the Mattermost community and are available for download, customization and deployment to your private cloud or on-prem infrastructure.

Slack Compatibility
-------------------

Mattermost makes it easy to migrate integrations written for Slack to Mattermost. 

Translate Slack's proprietary data format to Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost automatically translates the data coming from Slack:

1. JSON payloads written for Slack that contain the following are translated to Mattermost markdown and rendered equivalently to Slack:
   
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

Known Slack Compatibility Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Using ``icon_emoji`` to override the username is not supported.
2. Referencing  channels using <#CHANNEL_ID> does not link to the channel.
3. ``<!here>``, ``<!everyone>``, and ``<!group>`` are not supported.
4. Parameters "mrkdwn", "parse", and "link_names" are not supported. Mattermost converts Markdown by default and automatically links @mentions.
5. Bold formatting as ``*bold*`` is not supported (must be done as ``**bold**``).
6. Webhooks cannot direct message the user who created the webhook.

Troubleshooting
---------------

To debug incoming webhooks, set **System Console > Logging > Enable Webhook Debugging** to ``true`` and set **System Console > Logging > Console Log Level** to ``DEBUG``.
