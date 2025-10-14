Communicate a channel's focus and scope
=======================================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Every channel in Mattermost serves a purpose and exists for a reason. You can communicate a channel's focus and scope in 3 ways:

- a descriptive `channel name <#channel-name>`__
- a `channel purpose <#channel-purpose>`__ description
- `channel header <#channel-header>`__ details

Channel name
------------

You're prompted to provide a channel name when :doc:`creating a new channel in Mattermost </end-user-guide/collaborate/create-channels>`. Channel names must be at least 2 characters, and can be up to 64 characters in length. See the :doc:`channel naming conventions </end-user-guide/collaborate/channel-naming-conventions>` documentation for additional details and guidance on why channel naming is important.

.. note::

  `Some unicode characters <https://www.w3.org/TR/unicode-xml/#Charlist>`_ aren't supported in channel names.

Looking to rename an existing channel? See the :doc:`rename channels </end-user-guide/collaborate/rename-channels>` documentation for details.

Channel purpose
---------------

You're prompted to provide an optional channel purpose description when :doc:`creating a channel </end-user-guide/collaborate/create-channels>` or :doc:`renaming a channel </end-user-guide/collaborate/rename-channels>`. A channel purpose can be up to 250 characters in length, and is often used to help users decide whether to join that channel.

A channel's purpose is visible in the right pane when you select the **View Info** |channel-info| icon for the channel. Any member of a channel can change a channel's purpose description, unless the system admin has :doc:`disabled the ability to do so </administration-guide/onboard/advanced-permissions>`.

.. tab:: Web/Desktop

  .. image:: ../../images/channel-purpose-info.png
    :alt: Channel purpose helps users decide if they want to join the channel based on its scope or focus.

  1. Select the channel name at the top of the center pane to access the drop-down menu, then select **Channel Settings**.
  2. Enter or update the channel purpose.
  3. Select **Save**.

.. tab:: Mobile

  1. Tap the channel you want to edit.

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

  4. Tap **Edit Channel**.

  .. image:: ../../images/mobile-edit-channel.jpg
    :alt: Click on Edit channel to update the purpose of the channel.
    :scale: 25
  
  5. Type the new purpose of the channel and tap on **Save** to update the purpose.

  .. image:: ../../images/mobile-update-channel-purpose.jpg
    :alt: Click on Edit channel to rename the channel.
    :scale: 30

Channel header
--------------

A channel header is text that displays directly under a channel name at the top of the channel. Any channel member can change a channel header, unless the system admin has :doc:`disabled the ability to do so </administration-guide/onboard/advanced-permissions>`

A channel header can be up to 1024 characters in length, include Markdown formatting, and is often used to summarize the channel's focus or to provide links to frequently accessed documents, tools, or websites.

.. tab:: Web/Desktop

  1. Select the channel name at the top of the center pane to access the drop-down menu, then select **Channel Settings**.
  2. Enter or change channel header details. You can use the same :ref:`Markdown formatting <end-user-guide/collaborate/format-messages:use markdown>` in the channel header as you would when composing a message.

  .. image:: ../../images/channel-header.png
    :alt: Channel headers can include links to documents, tools, or websites.

.. tab:: Mobile

  1. Tap the channel you want to edit.

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

  4. Tap **Edit Channel**.

  .. image:: ../../images/mobile-edit-channel.jpg
    :alt: Click on Edit channel to to update the header of the channel.
    :scale: 25
  
  5. Type the new header of the channel and tap on **Save** to update the header.

  .. image:: ../../images/mobile-update-channel-header.jpg
    :alt: Click on Edit channel to rename the channel.
    :scale: 30