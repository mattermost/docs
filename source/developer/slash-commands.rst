.. _slash-commands:

Slash Commands
==============

.. note::

  This is the admin documentation for slash commands. If you're a developer looking to build an integration, see `our developer documentation <https://developers.mattermost.com/integrate/getting-started/>`__.

Mattermost supports slash commands to easily integrate external applications into the server. They function similarly to :doc:`outgoing webhooks <../developer/webhooks-outgoing/>`, except they can be used in any channel - including Private channels and Direct Messages.

Messages that begin with ``/`` are interpreted as slash commands. The commands will send an HTTP POST request to a web service, and process a response back to Mattermost. Mattermost supports both `built-in <https://docs.mattermost.com/developer/slash-commands.html#built-in-commands>`__ and `custom slash commands <https://docs.mattermost.com/developer/slash-commands.html#custom-slash-command>`__.

.. note::
  
  To prevent malicious users from trying to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`__, a *BOT* indicator appears next to posts coming from webhooks regardless of what username is specified.

.. toctree::
   :maxdepth: 2

Built-in Commands
-----------------

Each Mattermost installation comes with some built-in slash commands that are ready to use. These commands are available in the `latest Mattermost release <https://mattermost.com/download>`__:

.. csv-table::
    :header: "Command", "Description", "Example"

    "/away", "Set your availablity to away", "/away"
    "/offline", "Set your availablity to offline", "/offline"
    "/online", "Set your availablity to online", "/online"
    "/dnd", "Set your availablity to Do Not Disturb", "/dnd"
    "/code *{text}*", "Display text as a code block", "/code File bugs"
    "/collapse", "Turn on auto-collapsing of image previews", "/collapse"
    "/expand", "Turn off auto-collapsing of image previews", "/expand"
    "/echo *{message}* *{delay in seconds}*", "Echo back text from your account", "/echo Hello World 5"
    "/header *{text}*", "Edit the channel header", "/header File bugs here"
    "/invite *@{user}* *~{channel-name}*", "Invite user to the channel","/invite @john ~sampleChannel"
    "/purpose *{text}*", "Edit the channel purpose", "/purpose A channel to discuss bugs"
    "/rename *{text}*", "Rename the channel", "/rename Developers"
    "/help", "Open the Mattermost help page", "/help"
    "/invite *@{user}* *~{channel-name}*", "Invite user to the channel","/invite @john ~sampleChannel"
    "/invite_people *{name@domain.com ...}*", "Send an email invite to your Mattermost team","/invite_people john@example.com"
    "/kick (or /remove) *{@username}*", "Remove a member from a public or private channel", "/kick @alice"
    "/join (or /open) *{channel-name}*", "Join the given channel", "/join off-topic"
    "/leave", "Leave the current channel", "/leave"
    "/mute", "Turns off desktop, email and push notifications for the current channel or the [channel] specified", "/mute ~[channel]"
    "/logout", "Log out of Mattermost", "/logout"
    "/me *{message}*", "Do an action", "/me Hello World"
    "/msg *{@username}* *{message}*", "Send a Direct Message to a user", "/msg @alice hello"
    "/groupmsg *{@username1, @username2, ...}* *{message}*", "Sends a Group Message to the specified users", "/groupmsg @alice, @bob hello"
    "/search *{text}*", "Search text in messages", "/search meeting"
    "/settings", "Open the Account Settings dialog", "/settings"
    "/shortcuts", "Display a list of keyboard shortcuts", "/shortcuts"
    "/shrug *{message}*", "Add ``¯\_(ツ)_/¯`` to your message", "/shrug oh well"
    "/status *{emoji_name}* *{descriptive status_message}*", "Set a custom status that includes an optional emoji and a descriptive status message", "/status sick Feeling unwell and taking time off to recover"
    "/status clear", Clear the current status, "/status clear"

.. note::

  ``/status`` and ``/status clear`` slash commands listed above will be available in the Mattermost Mobile App in a future release.

Custom Slash Command
--------------------

Suppose you want to write an external application that is able to check the weather for certain cities. By creating a custom slash command, and setting up the application to handle the HTTP POST or GET from the command, you can let your users check the weather in their city using your command, say ``/weather toronto week``.

You can follow these general guidelines to set up a custom Mattermost slash command for your application.

1. Open **Main Menu > Integrations > Slash Commands**. If you don't have the **Integrations** option in your Main Menu, slash commands may not be enabled on your Mattermost server or may be disabled for non-admins. Enable them from **System Console > Integrations > Integration Management** or ask your Mattermost System Admin to do so.

2. Select **Add Slash Command** and add a name and description for the command.

3. Set the **Command Trigger Word**. The trigger word must be unique and cannot begin with a slash or contain any spaces. It also cannot be one of the `built-in commands <https://docs.mattermost.com/help/messaging/executing-commands.html#built-in-commands>`__.

4. Set the **Request URL** and **Request Method**. The request URL is the endpoint that Mattermost hits to reach your application, and the request method is either POST or GET and specifies the type of request sent to the request URL.

5. (Optional) Set the response username and icon the command will post messages as in Mattermost. If not set, the command will use your username and profile picture.

.. note::
  
    `Enable integrations to override usernames <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-usernames>`__ must be set to ``true`` in ``config.json`` to override usernames, and `similarly for profile picture icons <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-profile-picture-icons>`__. Enable them from **System Console > Integrations > Integration Management** or ask your Mattermost System Admin.

6. (Optional) Include the slash command in the command autocomplete list, displayed when typing ``/`` in an empty input box. Use it to make your command easier to discover by your teammates. You can also provide a hint listing the arguments of your command and a short description displayed in the autocomplete list.

7. Select **Save**. On the next page, copy the **Token** value. This will be used in a later step.

.. image:: ../images/slash_commands_token.png
  :width: 500 px

8. Next, write your external application. Include a function which receives HTTP POST or HTTP GET requests from Mattermost. The request will look something like this:

.. code-block:: text

  POST /slash-command HTTP/1.1
  Host: example.com
  User-Agent: Go-http-client/1.1
  Content-Length: 313
  Accept: application/json
  Authorization: Token okwexkjpe7ygb8eq1ww58t483w
  Content-Type: application/x-www-form-urlencoded
  Accept-Encoding: gzip

  channel_id=jux16pkewjrkfj3ehep1psxyxc&
  channel_name=town-square&
  command=%2Ftest&
  response_url=http%3A%2F%2Flocalhost%3A8065%2Fhooks%2Fcommands%2Fxbrkb8p393gjpq5cawei7npije&
  team_domain=test&
  team_id=carya1qs77bemjup96ff538snh&
  text=asd&
  token=okwexkjpe7ygb8eq1ww58t483w&
  user_id=aoa1agao6t8fmx3ikt1j9w5ybw&
  user_name=somename
  channel_mentions=["saepe-5", "aut-8"]
  channel_mentions_ids=["r3j6sby343fpfdxcbwqg95rfsa", "ehjj46yk7ifptr5bpfb966s6mc"]
  user_mentions=["aaron.peterson", "aaron.medina"]
  user_mentions_ids=["q5s3b7xzgprp5eid8h66j9epsy", "czwmumrmw7dfxecww7qibkkoor"]

If your integration sends back a JSON response, make sure it returns the ``application/json`` content-type.

9. Add a configurable *MATTERMOST_TOKEN* variable to your application and set it to the **Token** value from step 7. This value will be used by your application to confirm the HTTP POST or GET request came from Mattermost.

10. To have your application post a message back to ``town-square``, it can respond to the HTTP POST request with a JSON response such as:

.. code-block:: text

   {"response_type": "in_channel", "text": "
   ---
   #### Weather in Toronto, Ontario for the Week of February 16th, 2016

   | Day                 | Description                      | High   | Low    |
   |:--------------------|:---------------------------------|:-------|:-------|
   | Monday, Feb. 15     | Cloudy with a chance of flurries | 3 °C   | -12 °C |
   | Tuesday, Feb. 16    | Sunny                            | 4 °C   | -8 °C  |
   | Wednesday, Feb. 17  | Partly cloudly                   | 4 °C   | -14 °C |
   | Thursday, Feb. 18   | Cloudy with a chance of rain     | 2 °C   | -13 °C |
   | Friday, Feb. 19     | Overcast                         | 5 °C   | -7 °C  |
   | Saturday, Feb. 20   | Sunny with cloudy patches        | 7 °C   | -4 °C  |
   | Sunday, Feb. 21     | Partly cloudy                    | 6 °C   | -9 °C  |
   ---
   "}

which would render in Mattermost as:

.. image:: ../images/weatherBot.png
  :alt: Shows what the JSON response renders as in Mattermost

11. You're all set! See `developer documentation <https://developers.mattermost.com/integrate/slash-commands>`__ for details on what parameters are supported by slash commands. For instance, you can override the username and profile picture the messages post as, or specify a custom post type when sending a webhook message for use by `plugins <https://about.mattermost.com/default-plugins>`__.

Messages with advanced formatting can be created by including an :doc:`attachment array <message-attachments>` and :doc:`interactive message buttons <interactive-messages>` in the JSON payload.

.. note::
  
  `Enable integrations to override usernames <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-usernames>`__ must be set to ``true`` in ``config.json`` to override usernames. Enable them from **System Console > Integrations > Integration Management** or ask your Mattermost System Admin. If not enabled, the username is set to ``webhook``.
  
  Similarly, `Enable integrations to override profile picture icons <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-profile-picture-icons>`__ must be set to ``true`` in ``config.json`` to override usernames. Enable them from **System Console > Integrations > Integration Management** or ask your Mattermost System Admin. If not enabled, the icon of the creator of the webhook URL is used to post messages.

Tips and Best Practices
------------------------

1. Slash commands are designed to easily allow you to post messages. For other actions such as channel creation, you must also use the `Mattermost APIs <https://api.mattermost.com>`__.

2. Posts size is limited to 16393 characters for servers running `Mattermost Server v5.0 or later <https://docs.mattermost.com/administration/important-upgrade-notes.html>`__. Use the `extra_responses <https://developers.mattermost.com/integrate/slash-commands/#parameters>`__ field to reply to a triggered slash command with more than one post.

3. You can restrict who can create slash commands in `System Console > Integrations > Integration Management <https://docs.mattermost.com/administration/config-settings.html#restrict-managing-integrations-to-admins>`__.

4. Mattermost outgoing webhooks are Slack-compatible. You can copy-and-paste code used for a Slack outgoing webhook to create Mattermost integrations. Mattermost `automatically translates Slack's JSON format <https://docs.mattermost.com/developer/slash-commands.html?highlight=translate%20slack%20data%20format%20mattermost#translate-slack-s-data-format-to-mattermost>`__.

5. The external application may be written in any programming language. It needs to provide a URL which receives the request sent by your Mattermost server and responds with in the required JSON format.

Share Your Integration
----------------------

If you've built an integration for Mattermost, please consider `sharing your work <https://mattermost.org/share-your-mattermost-projects>`__ in our `app directory <https://about.mattermost.com/default-app-directory>`__.

The `app directory <https://about.mattermost.com/default-app-directory>`__ lists open source integrations developed by the Mattermost community and are available for download, customization and deployment to your private cloud or self-managed infrastructure.

Slack Compatibility
-------------------

Mattermost makes it easy to migrate integrations written for Slack to Mattermost.

Translate Slack's data format to Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost automatically translates the data coming from Slack:

1. JSON responses written for Slack, that contain the following, are translated to Mattermost Markdown and rendered equivalently to Slack:
   
   - ``<>`` to denote a URL link, such as ``{"text": "<https://mattermost.com/>"}``
   - ``|`` within a ``<>`` to define linked text, such as ``{"text": "Click <https://mattermost.com/|here> for a link."}``
   - ``<userid>``  to trigger a mention to a user, such as ``{"text": "<5fb5f7iw8tfrfcwssd1xmx3j7y> this is a notification."}``
   - ``<!channel>``, ``<!here>`` or ``<!all>`` to trigger a mention to a channel, such as ``{"text": "<!channel> this is a notification."}``

2. Both the HTTP POST and GET request bodies sent to a web service are formatted the same as Slack's. This means your Slack integration's receiving function does not need change to be compatible with Mattermost.
  
Known Slack compatibility issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Using ``icon_emoji`` to override the username is not supported.
2. Referencing  channels using ``<#CHANNEL_ID>`` does not link to the channel.
3. ``<!everyone>`` and ``<!group>`` are not supported.
4. Parameters "mrkdwn", "parse", and "link_names" are not supported (Mattermost always converts markdown and automatically links @mentions).
5. Bold formatting supplied as ``*bold*`` is not supported (must be done as ``**bold**``).
6. Slack assumes default values for some fields if they are not specified by the integration, while Mattermost does not.

Troubleshooting
---------------

See `developer documentation <https://developers.mattermost.com/integrate/slash-commands>`__ for troubleshooting, or `join the Mattermost user community for help <https://mattermost.com/pl/default-ask-mattermost-community>`_.
