Built-In Slash Commands
============================

.. include:: ../_static/badges/all-commercial.rst
  :start-after: :nosearch:

The following built-in slash comamnds are available in your Mattermost :doc:`workspace </end-user-guide/end-user-guide-index>`. 

.. tip::

    Looking for more slash commands? See the `custom slash commands <https://developers.mattermost.com/integrate/slash-commands/custom/>`__ developer documentation for details on creating custom commands.

Invite people
~~~~~~~~~~~~~

- Invite one person using ``/invite user1`` or ``/invite @user1``.
- Invite a custom user group using ``/invite @usergroup``.
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

Start or join a call
~~~~~~~~~~~~~~~~~~~~

- Start a call in a channe or thread using ``/call start``
- Join a call in a channel or thread using ``/call join``

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

- Set :ref:`your availability <end-user-guide/preferences/set-your-status-availability:set your availability>` using ``/away``, ``/offline``, ``/online``, or ``/dnd``
- Set :ref:`a custom status <end-user-guide/preferences/set-your-status-availability:set a custom status>` using ``/status {emoji_name} {descriptive status_message}``, such as ``/status sick Feeling unwell and taking time off to recover``. Clear your current status using ``/status clear``.

Manage channels
~~~~~~~~~~~~~~~

- Edit the channel header using ``/header {text}`` or the channel purpose using ``/purpose {text}``.
- Rename a channel using ``/rename {text}``.

Manage mobile app log attachments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``/mobile-logs`` to enable an attachment option in the Mattermost mobile client that lets users attach their mobile app logs as a file to any message they send. This helps administrators and support engineers debug mobile-specific issues by providing device-side context that isn't available from server logs alone. The command updates the ``attach_app_logs`` advanced preference and always responds with an ephemeral message visible only to the invoking user.

.. note::

    This command requires Mattermost mobile app v2.38 or later. On earlier versions the preference can still be set, but the attachment option won't appear in the mobile client.

- Enable log attachment for yourself using ``/mobile-logs on``.
- Disable log attachment for yourself using ``/mobile-logs off``.
- Check your current setting using ``/mobile-logs status``.
- System admins can manage the setting for another user by appending a username, such as ``/mobile-logs on @username``, ``/mobile-logs off @username``, or ``/mobile-logs status @username``.

.. important::

    Non-admin users can only manage their own preference. Attempts to target another account return a neutral **Unable to change mobile log settings for that user** message to avoid username enumeration. Preference changes made through this command are recorded in the audit log.

More useful slash commands
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Open the Mattermost product documentation using ``/help``.
- Open the in-product Marketplace using ``/marketplace``.
- Display a list of keyboard shortcuts using ``/shortcuts``.
- Open the **Settings** screen using ``/settings``.
- Log out of Mattermost using ``/logout``.