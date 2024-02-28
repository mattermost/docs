Communicate a channel's focus and scope
=======================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |channel-info| image:: ../images/information-outline_F02FD.svg
  :alt: Use the Channel Info icon to access additional channel management options.
  :class: theme-icon

Every channel in Mattermost serves a purpose and exists for a reason. You can communicate a channel's focus and scope in 3 ways:

- a descriptive `channel name <#channel-name>`__
- a `channel purpose <#channel-purpose>`__ description
- `channel header <#channel-header>`__ details

Channel name
------------

You're prompted to provide a channel name when `creating a new channel in Mattermost </collaborate/create-channels.html>`__. Channel names must be at least 2 characters, and can be up to 64 characters in length. See the `channel naming conventions </collaborate/channel-naming-conventions.html>`__ documentation for additional details and guidance on why channel naming is important.

.. note::
    
    `Some unicode characters <https://www.w3.org/TR/unicode-xml/#Charlist>`_ aren't supported in channel names.

Looking to rename an existing channel? See the `rename channels </collaborate/rename-channels.html>`__ documentation for details.

Channel purpose
---------------

You're prompted to provide an optional channel purpose description when `creating a new channel in Mattermost </collaborate/create-channels.html>`__ visible when you select **View Info** |channel-info| for the channel. Any member of a channel can change a channel's purpose description, unless the system admin has `disabled the ability to do so <onboard/advanced-permissions.html>`__.

A channel purpose can be up to 250 characters in length, and is often used to help users decide whether to join that channel.


.. tabs::

  .. tab:: Web/Desktop

    .. image:: ../images/channel-purpose-info.png
        :alt: Channel purpose helps users decide if they want to join the channel based on its scope or focus.

    1. Select a channel.
    2. Select the channel name and **Edit Channel Purpose** to provide or update a channel's purpose.
    3. Select **Save**.

  .. tab:: Mobile

    1. Tap the channel you want to edit.
    2. Long-press on the channel purpose.
    3. Tap **Copy purpose text**.
    4. Tap the purpose field to paste the copied text.

Channel header
--------------

A channel header refers to text that displays directly under a channel name at the top of the screen. Any channel member can change a channel header, unless the system admin has `disabled the ability to do so <onboard/advanced-permissions.html>`__

A channel header can be up to 1024 characters in length, include Markdown formatting, and is often used to summarize the channel's focus or to provide links to frequently accessed documents, tools, or websites.

.. tabs::

  .. tab:: Web/Desktop

    1. Select a channel.
    2. Select the channel name and **Edit Channel Header**. You can use the same `Markdown formatting </collaborate/format-messages.html#use-markdown>`__ in the channel header as you would when composing a message.

    .. image:: ../images/channel-header.png
        :alt: Channel headers can include links to documents, tools, or websites.

  .. tab:: Mobile

    1. Tap the channel you want to edit.
    2. Long-press on the channel header.
    3. Tap **Copy header text**.
    4. Tap the header field to paste the copied text.