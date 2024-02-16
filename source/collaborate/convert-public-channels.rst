Convert public channels to private channels
===========================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |more-icon| image:: ../images/dots-horizontal_F01D8.svg
    :alt: Use the More icon to access additional message options.

You must be a system admin or team admin to convert public channels to private channels. When a channel is converted from public to private, its history and membership are preserved. Membership in a private channel remains as invitation only. Publicly-shared files remain accessible to anyone with the link.

.. note::
    Default channels such as ``Town Square`` and ``Off-Topic`` can't be converted to private channels.

.. tabs::

  .. tab:: Web/Desktop

    To convert a public channel to a private channel, select the public channel name at the top of the center pane to access the drop-down menu, then select **Convert to Private Channel**. 

    .. image:: ../images/convert-public-channel-to-private.png
      :alt: From the channel name, you can convert a public channel to a private channel if you're an admin.
  
  .. tab:: Mobile

    To convert a public channel to a private channel:
    
    1. Tap the channel you want to convert.
    2. Tap the **More** |more-icon| icon located in the top right corner of the app.
    3. Tap **View info**.
    4. Tap **Convert to private channel**.
    5. Tap **Yes** to confirm.

Convert private channels to public channels
-------------------------------------------

Due to potential security concerns with sharing private channel history, only system admins can convert private channels to public channels via **System Console > Channels > Edit (Channel Configuration)**. 

Alternatively, system admins can perform this action using the `mmctl channel modify command </manage/mmctl-command-line-tool.html#mmctl-channel-modify>`__.
