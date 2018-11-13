.. _slash-commands:

Slash Commands
==============

.. note::
  This is the admin documentation for slash commands. If you're a developer looking to build an integration, see `our developer documentation <https://developers.mattermost.com/integrate>`_.

Mattermost supports slash commands to easily integrate external applications into the server. They function similarly to :doc:`outgoing webhooks <../developer/webhooks-outgoing/>`, except they can be used in any channel, including private channels and direct messages.

Messages that begin with ``/`` are interpreted as slash commands. The commands will send an HTTP POST request to a web service, and process a response back to Mattermost. Mattermost supports both `built-in <https://docs.mattermost.com/developer/slash-commands.html#built-in-commands>`_ and `custom slash commands <https://docs.mattermost.com/developer/slash-commands.html#custom-slash-command>`_.

.. note::
  To prevent malicious users from trying to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`_, a *BOT* indicator appears next to posts coming from webhooks regardless of what username is specified.

.. toctree::
   :maxdepth: 2

Built-in Commands
------------------------

Each Mattermost installation comes with some built-in slash commands that are ready to use. These commands are available in the `latest Mattermost release <https://about.mattermost.com/download/>`_:

.. csv-table::
    :header: "Command", "Description", "Example"

    "/away", "Set your status away", "/away"
    "/offline", "Set your status offline", "/offline"
    "/online", "Set your status online", "/online"
    "/dnd", "Set your status to Do Not Disturb", "/dnd"
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
    "/kick *{@username}*", "Remove a member from a public or private channel", "/kick @alice"
    "/remove *{@username}*", "Remove a member from a public or private channel", "/remove @alice"
    "/join *{channel-name}*", "Join the open channel", "/join off-topic"
    "/open *{channel-name}*", "Join the open channel", "/open off-topic"
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

Custom Slash Command
------------------------------

Suppose you want to write an external application that is able to check the weather for certain cities. By creating a custom slash command, and setting up the application to handle the HTTP POST or GET from the command, you can let your users check the weather in their city using your command, say ``/weather toronto week``.

You can follow these general guidelines to set up a custom Mattermost slash command for your application.

1 - First, go to **Main Menu > Integrations > Slash Commands**. If you don't have the **Integrations** option in your Main Menu, slash commands may not be enabled on your Mattermost server or may be disabled for non-admins. Enable them from **System Console > Integrations > Custom Integrations** or ask your System Administrator to do so.

2 - Click **Add Slash Command** and add name and description for the command.

3 - Set the **Command Trigger Word**. The trigger word must be unique and cannot begin with a slash or contain any spaces. It also cannot be one of the `built-in commands <https://docs.mattermost.com/help/messaging/executing-commands.html#built-in-commands>`_.

4 - Set the **Request URL** and **Request Method**. The request URL is the endpoint that Mattermost hits to reach your application, and the request method is either POST or GET and specifies the type of request sent to the request URL.

5 - (Optional) Set the response username and icon the command will post messages as in Mattermost. If not set, the command will use your username and profile picture.

  .. note::
    `Enable integrations to override usernames <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-usernames>`_ must be set to `true` in `config.json` to override usernames, and `similarly for profile picture icons <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-profile-picture-icons>`_. Enable them from **System Console > Integrations > Custom Integrations** or ask your System Administrator.

6 - (Optional) Include the slash command in the command autocomplete list, displayed when typing ``/`` in an empty input box. Use it to make your command easier to discover by your teammates. You can also provide a hint listing the arguments of your command and a short description displayed in the autocomplete list.

7 - Hit **Save**. On the next page, copy the **Token** value. This will be used in a later step.

.. image:: ../images/slash_commands_token.png
  :width: 500 px

8 - Next, write your external application. Include a function which receives HTTP POST or HTTP GET requests from Mattermost. The request will look something like this:

.. code-block:: text

   Content-Length: 244
   User-Agent: Go 1.1 package http
   Host: localhost:5000
   Accept: application/json
   Content-Type: application/x-www-form-urlencoded

   channel_id=cniah6qa73bjjjan6mzn11f4ie&
   channel_name=town-square&
   command=/somecommand&
   response_url=not+supported+yet&
   team_domain=someteam&
   team_id=rdc9bgriktyx9p4kowh3dmgqyc&
   text=hello+world&
   token=xr3j5x3p4pfk7kk6ck7b4e6ghh&
   user_id=c3a4cqe3dfy6dgopqt8ai3hydh&
   user_name=somename

If your integration sends back a JSON response, make sure it returns the ``application/json`` content-type.

9 - Add a configurable *MATTERMOST_TOKEN* variable to your application and set it to the **Token** value from step 7. This value will be used by your application to confirm the HTTP POST or GET request came from Mattermost.

10 - To have your application post a message back to ``town-square``, it can respond to the HTTP POST request with a JSON response such as:

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

which would render in Mattermost as

.. image:: ../images/weatherBot.PNG
  :alt: Shows what the JSON response renders as in Mattermost

11 - You're all set! See `developer documentation <https://developers.mattermost.com/integrate/slash-commands>`_ for details on what parameters are supported by slash commands. For instance, you can override the username and profile picture the messages post as, or specify a custom post type when sending a webhook message for use by `plugins <https://about.mattermost.com/default-plugins>`_.

Messages with advanced formatting can be created by including an :doc:`attachment array <message-attachments>` and :doc:`interactive message buttons <interactive-messages>` in the JSON payload.

.. note::
  `Enable integrations to override usernames <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-usernames>`_ must be set to `true` in `config.json` to override usernames. Enable them from **System Console > Integrations > Custom Integrations** or ask your System Administrator. If not enabled, the username is set to `webhook`.
  
  Similarly, `Enable integrations to override profile picture icons <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-profile-picture-icons>`_ must be set to `true` in `config.json` to override usernames. Enable them from **System Console > Integrations > Custom Integrations** or ask your System Administrator. If not enabled, the icon of the creator of the webhook URL is used to post messages.

Tips and Best Practices
------------------------

1. Slash commands are designed to easily allow you to post messages. For other actions such as channel creation, you must also use the `Mattermost APIs <https://api.mattermost.com>`_.

2. If the text is longer than the allowable character limit per post, the message is split into multiple consecutive posts, each within the character limit. Servers running Mattermost Server v5.0 or later `can support posts up to 16383 characters <https://docs.mattermost.com/administration/important-upgrade-notes.html>`_.

3. You can restrict who can create slash commands in `System Console > Integrations > Custom Integrations <https://docs.mattermost.com/administration/config-settings.html#restrict-managing-integrations-to-admins>`_.

4. Mattermost outgoing webhooks are Slack-compatible. You can copy-and-paste code used for a Slack outgoing webhook to create Mattermost integrations. Mattermost `automatically translates Slack's JSON format <https://docs.mattermost.com/developer/slash-commands.html?highlight=translate%20slack%20data%20format%20mattermost#translate-slack-s-data-format-to-mattermost>`_.

5. The external application may be written in any programming language. It needs to provide a URL which receives the request sent by your Mattermost server and responds with in the required JSON format.

Share Your Integration
-----------------------

If you've built an integration for Mattermost, please consider `sharing your work <https://www.mattermost.org/share-your-mattermost-projects/>`_ in our `app directory <https://about.mattermost.com/default-app-directory/>`_.

The `app directory <https://about.mattermost.com/default-app-directory/>`_ lists open source integrations developed by the Mattermost community and are available for download, customization and deployment to your private cloud or on-prem infrastructure.

Slack Compatibility
-------------------

Mattermost makes it easy to migrate integrations written for Slack to Mattermost. 

Translate Slack's data format to Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost automatically translates the data coming from Slack:

1. JSON responses written for Slack, that contain the following, are translated to Mattermost Markdown and rendered equivalently to Slack:
   
   - ``<>`` to denote a URL link, such as ``{"text": "<http://www.mattermost.com/>"}``
   - ``|`` within a ``<>`` to define linked text, such as ``{"text": "Click <http://www.mattermost.com/|here> for a link."}``
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

See `developer documentation <https://developers.mattermost.com/integrate/slash-commands>`_ for troubleshooting help.
