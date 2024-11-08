Convert public channels to private channels
===========================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

You must be a system admin or team admin to convert public channels to private channels. When a channel is converted from public to private, its history and membership are preserved. Membership in a private channel remains as invitation only. Publicly-shared files remain accessible to anyone with the link.

.. note::
    The default channel ``Town Square`` can't be converted to a private channel.

.. tab:: Web/Desktop

  To convert a public channel to a private channel, select the public channel name at the top of the center pane to access the drop-down menu, then select **Convert to Private Channel**. 

  .. image:: ../images/convert-public-channel-to-private.png
    :alt: From the channel name, you can convert a public channel to a private channel if you're an admin.

.. tab:: Mobile

  To convert a public channel to a private channel:
  
  1. Tap the channel you want to convert.

  .. image:: ../images/mobile-select-a-channel.jpg
      :alt: Select a channel that you want to rename.
      :scale: 30

  2. Tap the **More** |more-icon-vertical| icon located in the top right corner of the app.

  .. image:: ../images/mobile-select-more-options-for-a-channel.jpg
      :alt: Tap on More options to access available options for the channel.
      :scale: 30

  3. Tap **View info**.

  .. image:: ../images/mobile-select-view-info-for-a-channel.jpg
      :alt: Tap on View info to see the basic channel info.
      :scale: 30

  4. Tap **Convert to private channel**.

  .. image:: ../images/mobile-convert-to-private-channel.jpg
      :alt: Tap on Convert to private channel to make the channel private.
      :scale: 30

  5. Tap **Yes** to confirm.

  .. image:: ../images/mobile-confirm-convert-to-private-channel.jpg
      :alt: Tap on Yes to confirm your choice.
      :scale: 30

Convert private channels to public channels
-------------------------------------------

Due to potential security concerns with sharing private channel history, only system admins can convert private channels to public channels.

1. Go to **System Console > Channels**.
2. Select **Edit** for an existing private channel. You can also filter the list of channels to private channels only.
3. Under **Channel Management > Public channel or private channel**, select **Private**. If :ref:`Sync Group channel management <manage/team-channel-members:channel management>` is enabled, private channels can't be converted to public channels.
4. Select **Save**.

.. tip::

  Alternatively, system admins can convert private channels to public channels using the :ref:`mmctl channel modify command <manage/mmctl-command-line-tool:mmctl channel modify>`.
