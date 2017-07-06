.. _incoming_webhooks:

Incoming Webhooks
=================

Incoming webhooks are a simple way to post messages from external applications into Mattermost public channels, private channels, and direct messages. They use a JSON payload that contains the message and send it via HTTP POST request to a Mattermost URL generated for each application.

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

Additional options and formatting
----------------------------------

Below are additional options to customize the message posted to Mattermost.

Override the channel
~~~~~~~~~~~~~~~~~~~~~

You can override the channel the webhook posts to by specifying a `channel` parameter in your JSON payload.

For example, if you have a webhook created for *Town Square*, you can send a message to the *Off-Topic* channel via the same webhook URL by using the following payload.

  .. code-block::

    payload={"channel": "off-topic", "text": "Hello, this is some text\nThis is more text. :tada:"}

To send a message to a direct message channel, add an "@" symbol followed by the username to the `channel` parameter.

  .. code-block::

    payload={"channel": "@username", "text": "Hello, this is some text\nThis is more text. :tada:"}

Override the username
~~~~~~~~~~~~~~~~~~~~~

You can override the username the messages posts as by specifying a `username` parameter in your JSON payload.

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

You can also override the profile picture the messages post with by specifying an `icon_url` parameter in your JSON payload.

For example, you can use the following payload to override the profile picture to use the image located at http://example.com/somecoolimage.jpg.

  .. code-block::

    payload={"icon_url": "http://example.com/somecoolimage.jpg", "text": "Hello, this is some text\nThis is more text. :tada:"}

  .. note::
    `Enableintegrations to override profile picture icons <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-profile-picture-icons>`_ must be set to `true` in `config.json` to override usernames. Enable them from **System Console > Integrations > Custom Integrations** or ask your System Administrator. If not enabled, the icon of the creator of the webhook URL is used to post messages.

Format the webhook message
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can apply :doc:`Markdown formatting <../help/messaging/formatting-text>` to create richly formatted payloads.

For example, to create a message with a heading, and an italicized text on the next line, use the following payload. 

  .. code-block::

    payload={"text": "# This is a heading\n_This text is italicized._"}

.. image:: ../images/incoming_webhooks_markdown_formatting.png

Messages with advanced formatting can be created by including an :doc:`attachment array <message-attachments>` in the JSON payload.



Full example / best practices?
-------------------

Built-in stuff
-------------------

Share your integration
-------------------











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

















A couple key points:

- **Mattermost incoming webhooks are Slack-compatible.** If you've used Slack's incoming webhooks to create integrations, you can copy and paste that code to create Mattermost integrations. Mattermost automatically translates Slack's proprietary JSON payload format into markdown to render in Mattermost messages
- **Mattermost incoming webhooks support full markdown.** A rich range of formatting unavailable in Slack is made possible through :doc:`markdown support <../help/messaging/formatting-text>` in Mattermost, including headings, formatted fonts, tables, inline images and other options supported by Mattermost Markdown.

Setting Up Existing Integrations
--------------------------------

If you've already found or built an integration and are just looking to hook it up, then you should just need to follow the specific instructions of that integration. If the integration is using Mattermost incoming webhooks, then at some point in the instructions it will ask for a webhook URL. You can get this URL by following the first step in the next section.

Creating Integrations using Incoming Webhooks
---------------------------------------------

You can create a webhook integration to post into any Mattermost public channels and into private channels you have permission to by using these steps:

2. Build your integration in the programming language of your choice.
  a. Most integrations will be used to translate some sort of output from another system to an appropriately formatted input that will be passed into the Mattermost webhook URL. For example, an integration could take events generated by `GitLab outgoing webhooks <http://doc.gitlab.com/ee/web_hooks/web_hooks.html>`_ and parse them into a JSON body to post into Mattermost.
  b. To get the message posted into Mattermost, your integration will need to create an HTTP POST request that will submit to the incoming webhook URL you created before. The body of the request must have a *payload* that contains a JSON object that specifies a *text* parameter. For example, ``payload={"text": "Hello, this is some text."}``` is a valid body for a request.
  c. Set up your integration running on Heroku, an AWS server or a server of your own to start sending real-time updates to Mattermost channels.

**Additional Notes:**

1. For the HTTP request body, if `Content-Type` is specified as `application/json` in the headers of the HTTP request then the body of the request can be direct JSON. For example, ``{"text": "Hello, this is some text."}``

6. Including *@username* in the JSON payload will trigger a mention notification for the person with the specified username. Channels can be mentioned by including *@channel* or *<!channel>*. For example:  ``payload={"text": "<!channel> this is a notification""}`` would create a message that mentions *@channel*.

7. If the text is longer than 4000 characters, the message is split into multiple consecutive posts, each within the 4000 character limit.
