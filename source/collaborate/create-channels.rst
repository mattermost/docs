Create channels
===============

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |plus-icon| image:: ../images/plus_F0415.svg
  :alt: Open menus using the plus icon.
  :class: theme-icon

Anyone can create public channels, private channels, direct messages, and group messages unless the system admin has :doc:`restricted permissions to do so using advanced permissions </onboard/advanced-permissions>`.

.. tab:: Web/Desktop

  **To create a public or private channel**

  1. Select the **Add channels** button in the channel sidebar, then select **Create New Channel**. Alternatively, you can select |plus-icon| at the top of the channel sidebar, then select **Create New Channel**.

    .. image:: ../images/add-channels-button.png
      :alt: You can create a channel using the Add channels button
      :width: 400

  2. Enter a channel name.
  3. Choose whether this is a public or private channel. See the :doc:`channel types </collaborate/channel-types>` documentation to learn more about public and private channels.
  4. (Optional) Describe the channel's focus or purpose. This text is visible to all channel members in the channel header.

  **To start a direct or group message**

  1. Select the |plus-icon| next to the **Direct Messages** category in the channel sidebar.

    .. image:: ../images/write-dm.png
      :alt: Access recent direct messages and group messages.

  2. Select up to seven users by searching or browsing.

  .. tip::

    - Alternatively, select |plus-icon| at the top of the channel sidebar, then select **Open a Direct Message**. In the **Direct Messages** list, you'll see your most recent conversations.
    - To add more people to the conversation select the channel name, then select **Add Members**. Adding members to a group message creates a new channel and starts a new conversation.
    - You can't remove members of a group message; however, you can start a new group channel and conversation with different members.
    - If you want to add more than 7 users to a group message, create a private channel instead.

.. tab:: Mobile

  **To create a public or private channel**

  Tap |plus-icon| in the top right corner of the app, then select **Create New Channel**. Channels are created as public by default. If you want to create a private channel, tap the **Make Private** option.

  **To start a direct or group message**

  Tap |plus-icon| in the top right corner of the app, then select **Open a Direct Message**. You can select one person for a direct message or up to seven people for a group message. Tap **Start** to start the conversation.

Automate with channel actions
-----------------------------

The person who creates a channel automatically becomes the channel admin. Channel admins using Mattermost in a web browser or the desktop app can access **Channel Actions** from the channel name drop-down menu in the center pane to set up automatic actions when users :ref:`join the channel <collaborate/join-leave-channels:join a channel>` or :doc:`post a message </collaborate/send-messages>` to the channel.

Automatic actions include:

- Displaying a temporary welcome message for new channel members.
- Automatically adding the channel to a :doc:`category in the user's channel sidebar </preferences/customize-your-channel-sidebar>`.
- Prompting to run a playbook based on the contents of a message.

The :ref:`playbooks must be enabled <configure/plugins-configuration-settings:mattermost playbooks>` for channel admins to use channel actions.
