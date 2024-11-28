Archive and unarchive channels
==============================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Archive a channel
-----------------

You can delete a channel in Mattermost when it's no longer useful by archiving it. Anyone using Mattermost can archive the public channels or private channels they're a member of, unless the system admin has restricted the permissions to do so. 

When a channel is archived, it's deleted from the user interface, but a copy exists on the server in case it's needed for audit reasons in the future, or in case you decide to restore the channel by `unarchiving it <#unarchive-a-channel>`__. 

.. note::

  - All users are added to the **Off-Topic** and **Town Square** channels automatically. Town Square can't be archived.
  - System admins can archive channels in the System Console without needing to be a channel member.
  - Because a copy of the channel exists on the server, you can't reuse the URL of an archived channel when :doc:`creating a new channel </collaborate/create-channels>`.
  - Instead of archiving the channel, you can also leave it open and post a message in the channel saying it's considered archived, such as: ``# This channel is archived.``

.. tab:: Web/Desktop

  To archive a channel, select the channel name at the top of the center pane to access the drop-down menu, then select **Archive Channel**. 

.. tab:: Mobile

  To archive a channel:
  
  1. Tap the channel you want to delete.

  .. image:: ../images/mobile-select-a-channel.jpg
    :alt: Select a channel that you want to edit.
    :scale: 30

  2. Tap the **More** |more-icon-vertical| icon located in the top right corner of the app.

  .. image:: ../images/mobile-select-more-options-for-a-channel.jpg
    :alt: Tap on More options to access available options for the channel.
    :scale: 30

  3. Tap **View info**.

  .. image:: ../images/mobile-select-view-info-for-a-channel.jpg
    :alt: Tap on View info to see the basic channel info.
    :scale: 30

  4. Tap **Archive Channel**.

  .. image:: ../images/mobile-edit-channel.jpg
    :alt: Tap on Archive channel to archive the current channel.
    :scale: 30

  5. Tap **Yes** to confirm.

  .. image:: ../images/mobile-confirm-archive-a-channel.jpg
    :alt: Tap on Yes to confirm your choice.
    :scale: 30

Unarchive a channel
-------------------

System admins and Team admins can restore archived channels. When a channel is unarchived, channel membership and all its content is restored, unless messages and files have been deleted based on the :ref:`data retention policy <configure/compliance-configuration-settings:data retention policies>`.

.. tab:: Web/Desktop

  Search for the channel if required. Then, open the channel, select the channel name at the top of the center pane to access the drop-down menu and select **Unarchive Channel**. 

  .. image:: ../images/unarchive-channel.png
    :alt: Unarchive a channel.

.. tab:: Mobile

  To unarchive a channel:
  
  1. Tap the channel you want to unarchive.

  .. image:: ../images/mobile-select-a-channel.jpg
    :alt: Select a channel that you want to edit.
    :scale: 30

  2. Tap the **More** |more-icon-vertical| icon located in the top right corner of the app.

  .. image:: ../images/mobile-select-more-options-for-a-channel.jpg
    :alt: Tap on More options to access available options for the channel.
    :scale: 30

  3. Tap **View info**.

  .. image:: ../images/mobile-select-view-info-for-a-channel.jpg
    :alt: Tap on View info to see the basic channel info.
    :scale: 30

  4. Tap **Unarchive Channel**.

  .. image:: ../images/mobile-unarchive-a-channel.jpg
    :alt: Tap on Unarchive channel to unarchive the current channel.
    :scale: 30

  5. Tap **Yes** to confirm.

  .. image:: ../images/mobile-confirm-unarchive-a-channel.jpg
    :alt: Tap on Yes to confirm your choice.
    :scale: 30

.. tip::

  Alternatively, system admins can unarchive channels :ref:`via the mmctl <manage/mmctl-command-line-tool:mmctl channel unarchive>`, and Team admins can unarchive channels `via the API <https://api.mattermost.com/#operation/RestoreChannel>`__.
