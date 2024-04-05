Archive and unarchive channels
==============================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |more-icon| image:: ../images/dots-horizontal_F01D8.svg
    :alt: Use the More icon to access additional message options.
    :class: theme-icon

Archive a channel
-----------------

You can delete a channel in Mattermost when it's no longer useful by archiving it. Anyone using Mattermost can archive the public channels or private channels they're a member of, unless the system admin has restricted the permissions to do so. 

When a channel is archived, it's deleted from the user interface, but a copy exists on the server in case it's needed for audit reasons in the future, or in case you decide to restore the channel by `unarchiving it <#unarchive-a-channel>`__. 

.. notes::
  - All users are added to the **Off-Topic** and **Town Square** channels automatically. Users can't archive, `unarchive <#unarchive-a-channel>`__, or :ref:`leave <collaborate/join-leave-channels:leave a channel>` these channels.
  - System admins can archive channels in the System Console without needing to be a channel member.
  - Because a copy of the channel exists on the server, you can't reuse the URL of an archived channel when :doc:`creating a new channel </collaborate/create-channels>`.
  - Instead of archiving the channel, you can also leave it open and post a message in the channel saying it's considered archived, such as: ``# This channel is archived.``

.. tab:: Web/Desktop

  To archive a channel, select the channel name at the top of the center pane to access the drop-down menu, then select **Archive Channel**. 

.. tab:: Mobile

  To archive a channel:
  
  1. Tap the channel you want to delete.
  2. Tap the **More** |more-icon| icon located in the top right corner of the app.
  3. Tap **View info**.
  4. Tap **Archive Channel**.
  5. Tap **Yes** to confirm.

Unarchive a channel
-------------------

System admins and Team admins can restore archived channels be unarchiving them. When a channel is unarchived, channel membership and all its content is restored, unless messages and files have been deleted based on the :ref:`data retention policy <configure/compliance-configuration-settings:data retention policies>`.

.. note::

  - All users are added to the **Off-Topic** and **Town Square** channels automatically. Users can't `archive <#archive-a-channel>`__, unarchive, or :ref:`leave <collaborate/join-leave-channels:leave a channel>` these channels.

.. tab:: Web/Desktop

  Search for the channel if required. Then, open the channel, select the channel name at the top of the center pane to access the drop-down menu and select **Unarchive Channel**. 

  .. image:: ../images/unarchive-channel.png
    :alt: Unarchive a channel.

.. tab:: Mobile

  To unarchive a channel:
  
  1. Tap the channel you want to unarchive.
  2. Tap the **More** |more-icon| icon located in the top right corner of the app.
  3. Tap **View info**.
  4. Tap **Unarchive Channel**.
  5. Tap **Yes** to confirm.

.. tip::

  Alternatively, system admins can unarchive channels :ref:`via the mmctl <manage/mmctl-command-line-tool:mmctl channel unarchive>`, and Team admins can unarchive channels `via the API <https://api.mattermost.com/#operation/RestoreChannel>`__.
