Archive and unarchive channels
==============================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |more-icon| image:: ../images/dots-horizontal_F01D8.svg
    :alt: Use the More icon to access additional message options.

Archive a channel
-----------------

Anyone using Mattermost can archive the public channels or private channels they belong to, unless the system admin has restricted the permissions to do so. system admins can archive channels in the System Console without needing to be a channel member. When a channel is archived, it's removed from the user interface, but a copy exists on the server in case it's needed for audit reasons at a later stage. 

.. note:: 
  
  From Mattermost v5.28, users can view, share, and search for archived channel content. Because a copy of the channel exists on the server, you can't reuse the URL of an archived channel when creating a new channel.

.. tabs::

  .. tab:: Desktop

    To archive a channel, select the channel name at the top of the center pane to access the drop-down menu, then select **Archive Channel**. 

  .. tab:: Mobile

    To archive a channel:
    
    1. Tap the channel you want to archive.
    2. Tap the **More** |more-icon| icon located in the top right corner of the app.
    3. Tap **View info**.
    4. Tap **Archive Channel**.
    5. Tap **Yes** to confirm.

.. tip::

  Instead of archiving, you can also leave the channel open and post a message in the channel saying it's considered archived, such as: ``# This channel is archived.``

Unarchive a channel
-------------------

System admins and Team admins can unarchive public channels or private channels they belonged to before they were archived. When a channel is unarchived, channel membership and all its content is restored, unless messages and files have been deleted based on the `data retention policy </configure/configuration-settings.html#data-retention-policies>`__.

.. tabs::

  .. tab:: Desktop

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

  Alternatively, system admins can unarchive channels `via the CLI </manage/command-line-tools.html#mattermost-channel-restore>`__, or via the `mmctl </manage/mmctl-command-line-tool.html#mmctl-channel-unarchive>`__. Team admins can unarchive channels `via the API <https://api.mattermost.com/#operation/RestoreChannel>`__.
