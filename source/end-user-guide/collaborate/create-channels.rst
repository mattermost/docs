Create channels
===============

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Anyone can create public channels, private channels, direct messages, and group messages unless the system admin has :doc:`restricted permissions to do so using advanced permissions </administration-guide/onboard/advanced-permissions>`. Enterprise system administrators can also configure channels as :ref:`read-only <administration-guide/onboard/advanced-permissions:read-only channels>`.

.. tab:: Web/Desktop
  :parse-titles:

  Create a public or private channel
  -----------------------------------

  1. Select the **Add channels** button in the channel sidebar, then select **Create New Channel**. Alternatively, you can select |plus| at the top of the channel sidebar, then select **Create New Channel**.

    .. image:: ../../images/add-channels-button.png
      :alt: You can create a channel using the Add channels button
      :width: 400

  2. Enter a channel name.
  3. Choose whether this is a public or private channel. See the :doc:`channel types </end-user-guide/collaborate/channel-types>` documentation to learn more about public and private channels.
  4. (Optional) Describe the channel's focus or purpose. This text is visible to all channel members in the channel header.
  5. (Optional) Assign the channel to a category. If your system admin has enabled :ref:`channel category sorting <administration-guide/configure/experimental-configuration-settings:enable channel category sorting>`, you can assign the new channel to a new or existing channel category. If this option isn't available, you can `customize your channel sidebar </end-user-guide/preferences/customize-your-channel-sidebar>`.

  Start a direct or group message
  --------------------------------

  1. Select the |plus| next to the **Direct Messages** category in the channel sidebar.

    .. image:: ../../images/write-dm.png
      :alt: Access recent direct messages and group messages.

  2. Select up to seven users by searching or browsing. If your organization uses :doc:`connected workspaces </administration-guide/onboard/connected-workspaces>`, you can also select remote users from shared channels for direct and group messages.

  .. tip::

    - Alternatively, select |plus| at the top of the channel sidebar, then select **Open a Direct Message**. In the **Direct Messages** list, you'll see your most recent conversations.
    - To add more people to the conversation select the channel name, then select **Add Members**. Adding members to a group message creates a new channel and starts a new conversation.
    - You can't remove members of a group message; however, you can start a new group channel and conversation with different members.
    - If you want to add more than 7 users to a group message, create a private channel instead.

.. tab:: Mobile
  :parse-titles:

  Create a public or private channel
  -----------------------------------

  Tap |plus| in the top right corner of the app, then select **Create New Channel**. Channels are created as public by default. If you want to create a private channel, tap the **Make Private** option.


    .. image:: ../../images/create-channel-or-open-direct-message-on-mobile.jpg
      :alt: You can create a new channel by tapping the plus in the top right corner.
      :scale: 30
    
    .. image:: ../../images/private-channel-create.jpg
      :alt: You can make a channel private by tapping the Make Private option.
      :scale: 30

  Start a direct or group message
  --------------------------------

  Tap |plus| in the top right corner of the app, then select **Open a Direct Message**. You can select one person for a direct message or up to seven people for a group message. If your organization uses :doc:`connected workspaces </administration-guide/onboard/connected-workspaces>`, remote users from shared channels are also available to select. Tap **Start** to start the conversation.

    .. image:: ../../images/create-channel-or-open-direct-message-on-mobile.jpg
      :alt: You can start a direct or group message by tapping the plus in the top right corner.
      :scale: 30
    
    .. image:: ../../images/start-group-conversation.jpg
      :alt: You can stat a group conversation by selecting up to 7 members.
      :scale: 30

Automate with channel actions
-----------------------------

The person who creates a channel automatically becomes the channel admin. Channel admins using Mattermost in a web browser or the desktop app can access **Channel Actions** from the channel name drop-down menu in the center pane to set up automatic actions when users :ref:`join the channel <end-user-guide/collaborate/join-leave-channels:join a channel>` or :doc:`post a message </end-user-guide/collaborate/send-messages>` to the channel.

Automatic actions include:

- Displaying a temporary welcome message for new channel members.
- Automatically adding the channel to a :doc:`category in the user's channel sidebar </end-user-guide/preferences/customize-your-channel-sidebar>`.
- Prompting to run a playbook based on the contents of a message.

The :ref:`collaborative playbooks must be enabled <administration-guide/configure/plugins-configuration-settings:collaborative playbooks>` for channel admins to use channel actions.