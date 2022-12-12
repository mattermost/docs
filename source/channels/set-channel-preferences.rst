Set channel preferences
=======================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |channel-info| image:: ../images/information-outline_F02FD.svg
  :alt: Use the Channel Info icon to access additional channel management options.

.. |vertical-3-dots| image:: ../images/dots-vertical_F01D9.svg
  :alt: Select the More icon to access additional channel management options.

For each channel you're a member of, you can set notification preferences as well as the channel's header, purpose, and name. See the documentation for details on :doc:`renaming channels </channels/rename-channels>` and :doc:`channel naming convention recommendations </channels/channel-naming-conventions>`.

.. image:: ../images/channel-preferences.png
    :alt: Select the channel name at the top of the screen to set preferences for each channel you belong to.

Channel notification preferences
--------------------------------

To manage channel notification preferences, select the channel name at the top of the screen to access channel-specific settings, then select **Notification Preferences**.

.. tip::

  Alternatively, to manage channel notification preferences select the channel name, select the **View Info** |channel-info| icon, then select **Notification Preferences** in the right pane.

Mute channel
~~~~~~~~~~~~~

Muting turns off desktop, email, and push notifications for a channel, and the channel will only be marked as unread in the channel sidebar if you're mentioned. By default, all channels are unmuted.

To mute the current channel and disable notifications, select **Mute Channel** from the channel name at the top of the screen.

Once a channel is muted:

- Email, desktop, and push notifications are disabled.
- A mute icon displays next to the channel name.
- The channel appears at reduced opacity in the channel sidebar, and the channel isn't marked as unread unless you're mentioned directly.

To unmute the channel, select the channel name again to access the drop-down menu, then select **Unmute Channel**.

.. tip::

  You can also quickly mute or unmute any channel any time:
  
  - Select the channel name, then select **Mute Channel** or **Unmute Channel** from the list of options.
  - Select the **More Options** |vertical-3-dots| icon for a channel in the channel sidebar.
  - Select the **View Info** |channel-info| icon, then select **Mute** or **Muted** in the right pane. 

Ignore mentions for @channel, @here, and @all
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, you'll receive mention notifications every time someone on your team `mentions an entire channel </channels/mention-people.html>`__ using ``@channel``, ``@all``, or ``@here``.

To stop receiving mention notifications, enable the **Ignore mentions for @channel, @here and @all** option, then select **Save**. When enabled, mention notifications for channel-wide mentions are ignored, but the channel is marked as unread unless the channel is muted.

Send desktop notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, your `desktop notification preferences </channels/channels-settings.html#notifications>`__ configured in **Settings** apply to all channels. Desktop notifications are available on Edge, Firefox, Safari, Chrome, and `Mattermost desktop apps <https://mattermost.com/apps>`__.

To customize desktop notifications per channel, edit **Send desktop notifications**, choose one of the following options, then select **Save**:

+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Notification option**   | **You'll receive...**                                                                                                                                                                                                                            |
+===========================+==================================================================================================================================================================================================================================================+
| **Global default (None)** | Desktop notifications based on your `Settings </channels/channels-settings.html>`__ configuration.                                                                                                                                               |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **For all activity**      | Desktop notifications for every new message.                                                                                                                                                                                                     |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Only for mentions**     | - Desktop notifications for @mentions only.                                                                                                                                                                                                      |
|                           | - When you've `enabled Collapsed Reply Threads </channels/channels-settings.html#collapsed-reply-threads>`__, receive reply thread notifications by enabling **Notify me about threads I'm following**.                                          |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Never**                 | No desktop notifications.                                                                                                                                                                                                                        |
+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Send mobile push notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost push notifications `must be enabled </configure/configuration-settings.html#enable-push-notifications>`__ by a System Admin. Once enabled, your `mobile push notification preferences </messaging/manage-channels-settings.html#mobile-push-notifications>`__ configured in **Settings** apply to all channels by default.

To customize mobile push notifications per channel, edit **Send mobile push notifications**, choose one of the following options, then select **Save**:

+------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Notification option**      | **You'll receive...**                                                                                                                                                                                                                            |
+==============================+==================================================================================================================================================================================================================================================+
| **Global default (Mention)** | Mobile notifications based on your `Settings </channels/channels-settings.html>`__ configuration.                                                                                                                                                |
+------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **For all activity**         | Mobile notifications for every new message.                                                                                                                                                                                                      |
+------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Only for mentions**        | - Mobile notifications for @mentions only.                                                                                                                                                                                                       |
|                              | - When you've `enabled Collapsed Reply Threads </channels/channels-settings.html#collapsed-reply-threads>`__, receive reply thread notifications by enabling **Notify me about threads I'm following**.                                          |
+------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Never**                    | No desktop notifications.                                                                                                                                                                                                                        |
+------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Channel header
--------------

A channel header refers to text that displays under a channel name at the top of the screen. A channel header can be up to 1024 characters in length and is often used to summarize the channel's focus or to provide links to frequently accessed documents, tools, or websites.

Change the channel header by selecting **Edit Channel Header**. You can use Markdown to `format channel header text </messaging/formatting-text.html>`__ using the same Markdown for messages. Any channel member can change a channel header, unless the System Admin has `restricted permissions to do so </configure/configuration-settings.html#enable-public-channel-renaming-for>`__.

.. image:: ../images/channel-header.png
    :alt: Channel headers can include links to documents, tools, or websites.

.. tip::

  Alternatively, to provide or update a channel header, select the channel name, then select **Edit Channel Header** from the list of options.

Channel purpose
---------------

A channel purpose refers to text that displays when users select **View Info** for a channel. A channel purpose can be up to 250 characters in length and is often used to help users decide whether to join the channel.

To add a channel purpose, select **Edit Channel Purpose**. Any channel member can change a channel purpose, unless the System Admin has `restricted permissions to do so using advanced permissions </onboard/advanced-permissions.html>`__.

.. image:: ../images/channel-purpose.png
    :alt: Channel purpose helps users decide if they want to join the channel based on its scope or focus.

.. tip::

  Alternatively, to provide or update a channel purpose, select the channel name, then select **Edit Channel Purpose** from the list of options.

Channel name
------------

A channel name must be at least two characters, and can be up to 64 characters in length. `Some unicode characters <https://www.w3.org/TR/unicode-xml/#Charlist>`_ aren't supported.

To change the channel name, select **Rename Channel**. Changing the name of the channel also changes the channel URL. Any channel member can change a channel name, unless the System Admin has `restricted permissions to do so using advanced permissions </onboard/advanced-permissions.html>`__.

.. tip::

  Alternatively, to provide or update a channel name, select the channel name, then select **Rename Channel** from the list of options.