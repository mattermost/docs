.. _incoming_webhooks:

Incoming Webhooks
=================

Mattermost supports Webhooks to integrate external applications into the platform easily. Webhooks are simple event-notifications via HTTP POST. Incoming Webhooks may post a message to a Mattermost instance into public channels, private channels, and direct messages. The HTTP POST contains a specifically formatted JSON payload and is sent to Mattermost URL generated specifically for each application.

A couple of key points:

- **The external application may be written in the programming language of your choice.** It only needs to support sending a HTTP POST in the required JSON format to the specific URL.
- **Webhooks are designed to post a message only.** It is not possible to trigger any other event, like »create new channel« with a Webhook. Use the :doc:`API <../developer/api>`_ for this task.
- **Mattermost incoming webhooks are Slack-compatible.** If you've used Slack's incoming webhooks previously, you can copy and paste that code to create Mattermost integrations. Mattermost automatically translates Slack's proprietary JSON payload format.
- **Mattermost incoming webhooks support full markdown.** Unlike in Slack a rich range of formatting is made possible through :doc:`markdown support <../help/messaging/formatting-text>` in Mattermost, including headings, formatted fonts, tables, inline images and other options supported by Mattermost Markdown.

**Example:**

Suppose you have an external application which sends notifications, and these notifications should be posted into a Mattermost channel as well. The application may publish a statistic of executed software tests once a day. The application then just needs to send a HTTP request with a defined JSON format to Mattermost.

The JSON payload for this example might be:

.. code-block:: text

  {"text": "
  | Component  | Tests Run   | Tests Failed                                   |
  |:-----------|:------------|:-----------------------------------------------|
  | Server     | 948         | :white_check_mark: 0                           |
  | Web Client | 123         | :warning: [2 (see details)](http://linktologs) |
  | iOS Client | 78          | :warning: [3 (see details)](http://linktologs) |
  "}

Which would render in a Mattermost message as follows:

.. image:: ../images/webhooksTable.PNG
  :alt: Shows what the output of the JSON payload renders as in Mattermost

Enabling Incoming Webhooks
--------------------------

Incoming webhooks should be enabled on your Mattermost instance by default, but if they are not you'll need to get your system administrator to enable them. If you are the system administrator you can enable them by doing the following:

1. Login to your Mattermost team account that has the system administrator role.
2. Enable incoming webhooks from **System Console > Integrations > Custom Integrations**.
3. (Optional) Configure the **Enable integrations to override usernames** option to allow external applications to post messages under any name. If not enabled, the username is set to "webhook".
4. (Optional) Configure the **Enable integrations to override profile picture icons** option to allow external applications to change the icon of the account posting messages. If not enabled, the icon of the creator of the webhook URL is used to post messages.

Setting Up Existing Integrations
--------------------------------

If you've already found or built an integration and are just looking to hook it up, then you should just need to follow the specific instructions of that integration. If the integration is using Mattermost incoming webhooks, then at some point in the instructions it will ask for a webhook URL. You can get this URL by following the first step in the next section.

Creating Integrations using Incoming Webhooks
---------------------------------------------

You can create a webhook integration to post into any Mattermost public channels and into private channels you have permission to by using these steps:

.. Note::
  Incoming webhooks must be enabled. Only your Mattermost system administrator can enable incoming webhooks if they are currently disabled.

1. Create a Mattermost Incoming Webhook URL.
  a. Login to your Mattermost team site and go to **Main Menu > Integrations > Incoming Webhooks**.
  b. Click **Add incoming webhook**.
  c. Select the channel to receive webhook payloads, then click **Add** to create the webhook.
  d. To see your new webhook in action, try a curl command from your terminal or command-line to send a JSON string as the `payload` parameter in a HTTP POST request. For example:

  .. code-block:: text

    curl -i -X POST -d 'payload={"text": "Hello, this is some text.\nThis is more text."}' http://{your-mattermost-site}/hooks/xxx-generatedkey-xxx

2. Build your integration in the programming language of your choice.
  a. Most integrations will be used to translate some sort of output from another system to an appropriately formatted input that will be passed into the Mattermost webhook URL. For example, an integration could take events generated by `GitLab outgoing webhooks <http://doc.gitlab.com/ee/web_hooks/web_hooks.html>`_ and parse them into a JSON body to post into Mattermost.
  b. To get the message posted into Mattermost, your integration will need to create an HTTP POST request that will submit to the incoming webhook URL you created before. The body of the request must have a *payload* that contains a JSON object that specifies a *text* parameter. For example, ``payload={"text": "Hello, this is some text."}``` is a valid body for a request.
  c. Set up your integration running on Heroku, an AWS server or a server of your own to start sending real-time updates to Mattermost channels.

**Additional Notes:**

1. For the HTTP request body, if `Content-Type` is specified as `application/json` in the headers of the HTTP request then the body of the request can be direct JSON. For example, ``{"text": "Hello, this is some text."}``

2. You can override the channel specified in the webhook definition by specifying a `channel` parameter in your payload. For example, you might have a single webhook created for *Town Square*, but you can use ``payload={"channel": "off-topic", "text": "Hello, this is some text."}`` to send a message to the *Off-Topic* channel using the same webhook URL. If an *@* symbol followed by a username is specified, then the message will be sent to that user's direct message channel.

3. In addition, with **Enable integrations to override usernames** turned on,  you can also override the username the message posts as by providing a *username* parameter in your JSON payload. For example, you might want your message looking like it came from a robot so you can use ``payload={"username": "robot", "text": "Hello, this is some text."}`` to change the username of the post to "robot". Note, to combat any malicious users from trying to use this to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`_ a *BOT* indicator appears next to posts coming from webhooks.

4. With **Enable integrations to override profile picture icons** turned on, you can similarly change the icon the message posts with by providing a link to an image in the *icon_url* parameter of your payload. For example, ``payload={"icon_url": "http://example.com/somecoolimage.jpg", "text": "Hello, this is some text."}`` will post using whatever image is located at *http://example.com/somecoolimage.jpg* as the icon for the post.

5. Also, as mentioned previously, :doc:`markdown <../help/messaging/formatting-text>` can be used to create richly formatted payloads, for example: ``payload={"text": "# A Header\nThe _text_ below **the** header."}`` creates a message with a header, a carriage return, and bold text for "the".

6. Including *@username* in the JSON payload will trigger a mention notification for the person with the specified username. Channels can be mentioned by including *@channel* or *<!channel>*. For example:  ``payload={"text": "<!channel> this is a notification""}`` would create a message that mentions *@channel*.

7. If the text is longer than 4000 characters, the message is split into multiple consecutive posts, each within the 4000 character limit.

8. Posts with advanced formatting can be created by including an :doc:`attachment array <message-attachments>` in the JSON payload.

Slack Compatibility
-------------------

Mattermost makes it easy to take integrations written for Slack's proprietary JSON payload format and repurpose them to become Mattermost integrations. For example:

Connecting Mattermost to GitLab using Slack UI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GitLab is the leading open-source alternative to GitHub and offers built-in integrations with Slack. Rather than having to change code to support Mattermost, users can add Mattermost webhooks directly into the interface for Slack.

1. In GitLab, go to **Settings > Services** and select **Slack**.
2. Paste in the incoming webhook URL provided by Mattermost from under **Main Menu > Integration > Incoming Webhooks**.
3. Optionally set the **Username** you'd like displayed when the notification is made. Leave the **Channel** field blank.
4. Click **Save** then test the settings to confirm posts will be made to Mattermost.

Translating Slack's proprietary data format to Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following describes the automatic translations Mattermost performance to process data coming from Slack:

1. Payloads designed for Slack using *<>* to note the need to hyperlink a URL, such as ``payload={"text": "<http://www.mattermost.com/>"}``, are translated to the equivalent markdown in Mattermost and rendered the same as you would see in Slack.
2. Similiarly, payloads designed for Slack using *|* within a *<>* to define linked text, such as ``payload={"text": "Click <http://www.mattermost.com/|here> for a link."}``, are also translated to the equivalent markdown in Mattermost and rendered the same as you would see in Slack.
3. Like Slack, by overriding the channel name with a *@username*, such as ```payload={"text": "Hi", channel: "@jim"}``, you can send the message to a user through your direct message chat.
4. Channel names can be prepended with a *#*, like they are in Slack incoming webhooks, and the message will still be sent to the correct channel.

To see samples and community contributions, please visit `our app directory <https://about.mattermost.com/default-app-directory/>`_.

Known Slack Compatibility Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Using icon_emoji to override the username is not supported.
2. Referencing  channels using <#CHANNEL_ID> does not link to the channel.
3. ``<!here>``, ``<!everyone>``, and ``<!group>`` are not supported.
4. Parameters "mrkdwn", "parse", and "link_names" are not supported (Mattermost always converts markdown and automatically links @mentions).
5. Bold formatting as ``*bold*`` is not supported (must be done as ``**bold**``).
6. Webhooks cannot direct message the user who created the webhook.

Troubleshooting
---------------

Debugging Incoming Webhooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~
To debug, set **System Console > Logging > Enable Webhook Debugging** to ``true`` and set **System Console > Logging > Console Log Level** to ``DEBUG``.
