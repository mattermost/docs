Archive and unarchive channels
==============================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Archive a channel
-----------------

Delete :ref:`public channels <end-user-guide/collaborate/channel-types:public channels>` and :ref:`private channels <end-user-guide/collaborate/channel-types:private channels>` when they're no longer needed by archiving them. Archiving channels removes them from the channel sidebar and marks them as read-only. Anyone can archive a public or private channel they're a member of, unless your system admin has :doc:`disabled </administration-guide/onboard/advanced-permissions>` your ability to do so.

.. tip::

  You can continue to access archived channels, unless your system admin has :ref:`disabled <administration-guide/configure/site-configuration-settings:allow users to view archived channels>` your ability to do so.

.. tab:: Web/Desktop

  To archive a channel, select the channel name at the top of the center pane to access the drop-down menu, then select **Archive Channel**.

.. tab:: Mobile

  To archive a channel:
  
  1. Tap the channel you want to delete.

  .. image:: ../../images/mobile-select-a-channel.jpg
    :alt: Select a channel that you want to edit.
    :scale: 30

  2. Tap the **More** |more-icon-vertical| icon located in the top right corner of the app.

  .. image:: ../../images/mobile-select-more-options-for-a-channel.jpg
    :alt: Tap on More options to access available options for the channel.
    :scale: 30

  3. Tap **View info**.

  .. image:: ../../images/mobile-select-view-info-for-a-channel.jpg
    :alt: Tap on View info to see the basic channel info.
    :scale: 30

  4. Tap **Archive Channel**.

  .. image:: ../../images/mobile-edit-channel.jpg
    :alt: Tap on Archive channel to archive the current channel.
    :scale: 30

  5. Tap **Yes** to confirm.

  .. image:: ../../images/mobile-confirm-archive-a-channel.jpg
    :alt: Tap on Yes to confirm your choice.
    :scale: 30

.. note::

  - When a Mattermost user is deactivated in the system, your :ref:`direct message channel <end-user-guide/collaborate/channel-types:direct message channels>` with that user are archived and marked as read-only. An **Archived** icon |file-box| displays next to archived channels.
  - :ref:`Group message channels <end-user-guide/collaborate/channel-types:group message channels>` can't be archived, but they can be closed to hide them from the channel sidebar.
  - The default **Town Square** channel can't be archived.
  - System admins can archive channels without needing to be a channel member by using the System Console.
  - Because a copy of the channel exists on the server, you can't reuse the URL of an archived channel when :doc:`creating a new channel </end-user-guide/collaborate/create-channels>`.

Unarchive a channel
-------------------

System admins and Team admins can restore archived channels. When a channel is unarchived, channel membership and all its content is restored, unless messages and files have been deleted based on a :ref:`data retention policy <administration-guide/configure/compliance-configuration-settings:data retention policies>`.

.. tab:: Web/Desktop

  Search for the channel if required. Then, open the channel, select the channel name at the top of the center pane to access the drop-down menu and select **Unarchive Channel**. 

  .. image:: ../../images/unarchive-channel.png
    :alt: Unarchive a channel.

.. tab:: Mobile

  To unarchive a channel:
  
  1. Tap the channel you want to unarchive.

  .. image:: ../../images/mobile-select-a-channel.jpg
    :alt: Select a channel that you want to edit.
    :scale: 30

  2. Tap the **More** |more-icon-vertical| icon located in the top right corner of the app.

  .. image:: ../../images/mobile-select-more-options-for-a-channel.jpg
    :alt: Tap on More options to access available options for the channel.
    :scale: 30

  3. Tap **View info**.

  .. image:: ../../images/mobile-select-view-info-for-a-channel.jpg
    :alt: Tap on View info to see the basic channel info.
    :scale: 30

  4. Tap **Unarchive Channel**.

  .. image:: ../../images/mobile-unarchive-a-channel.jpg
    :alt: Tap on Unarchive channel to unarchive the current channel.
    :scale: 30

  5. Tap **Yes** to confirm.

  .. image:: ../../images/mobile-confirm-unarchive-a-channel.jpg
    :alt: Tap on Yes to confirm your choice.
    :scale: 30

.. tip::

  Alternatively, system admins can unarchive channels :ref:`via the mmctl <administration-guide/manage/mmctl-command-line-tool:mmctl channel unarchive>`, and Team admins can unarchive channels `via the API <https://api.mattermost.com/#operation/RestoreChannel>`__.
