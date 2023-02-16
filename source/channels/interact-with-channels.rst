Interact with channels
======================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

You can interact with Mattermost users, channels, conversations, and more using `built-in slash commands <#slash-commands>`_, or interact with the data model programmatically using `API endpoints <https://api.mattermost.com/>`__.

Slash commands
--------------

The following built-in slash comamnds are available in your Mattermost workspace. 

.. tip::

    Looking for more slash commands? See the `custom slash commands <https://developers.mattermost.com/integrate/slash-commands/custom/>`__ developer documentation for details on creating custom commands.

Invite people
~~~~~~~~~~~~~

- Invite one person using ``/invite user1`` or ``/invite @user1``
- Invite multiple people using ``/invite @user1 @user2``.
- Invite one person to a specific channel using ``/invite @user1 ~channel1``, or ``/invite @user1 channel1``.
- Invite multiple people to multiple channels using ``/invite @user1 @user2 ~channel1 ~channel2``.
- Invite people by email using ``/invite_people {name@domain.com, ...}``.

Join, leave, or mute channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Join a specific channel using ``/join {channel-name}`` or ``/open {channel-name}``.
- Leave a channel using ``/leave``.
- Mute a channel using ``/mute`` or ``/mute {channel-name}`` to turn off desktop, email, and push notifications for the current or specified channel.
- Remove someone from a channel using ``/kick {@username}`` or ``/remove {@username}``.

Manage conversations
~~~~~~~~~~~~~~~~~~~~

- Send a direct message to someone using ``/msg {@username} {message}``, or send a group message to multiple people using ``/groupmsg {@username1, @username2, @username3,...} {message}``.
- Display text as a code block using ``/code {text}``.
- Automatically collapse image previews using ``/collapse``, and automatially expand them using ``/expand``.
- Echo text back to yourself using ``/echo {message} {delay in seconds}`` or ``/me {message}``.
- Respond with a shrug using ``/shrug {message}``.
- Search message text using ``search {text}``.

Set your availability and status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Set `your availability </welcome/set-your-status-availability.html#set-your-availability>`__ using ``/away``, ``/offline``, ``/online``, or ``/dnd``
- Set `a custom status </welcome/set-your-status-availability.html#set-a-custom-status>`__ using ``/status {emoji_name} {descriptive status_message}``, such as ``/status sick Feeling unwell and taking time off to recover``. Clear your current status using ``/status clear``.

Manage channels
~~~~~~~~~~~~~~~

- Edit the channel header using ``/header {text}`` or the channel purpose using ``/purpose {text}``.
- Rename a channel using ``/rename {text}``.

More useful slash commands
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Open the Mattermost product documentation using ``/help``.
- Open the in-product Marketplace using ``/marketplace``.
- Display a list of keyboard shortcuts using ``/shortcuts``.
- Open the **Settings** screen using ``/settings``.
- Log out of Mattermost using ``/logout``.

