Channel Settings
================

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Notification preferences, channel header, channel purpose, and channel name are customizable for each channel. To access these settings, select
the channel name at the top of the page to access channel options.

Channel notification preferences
--------------------------------

Notification preferences can be modified for each channel you belong to.

Mute channel
~~~~~~~~~~~~~

By default, channel muting is turned off for all channels. To mute or unmute a channel, select the channel name at the top of the page to access the channel menu, then choose **Notification Preferences > Mute channel**.

Ignore mentions for @channel, @here and @all
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, you'll receive mention notifications for any uses of @channel, @all or @here in a channel. When enabled, the channel will ignore mention notifications for channel wide mentions. Any messages containing @channel, @all or @here will still mark the channel unread, unless channel mute is enabled.

Send desktop notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the desktop notification preference assigned in **Settings** is used for all channels. To customize the desktop notification preference for each channel, click the channel name at the top of the page to access the channel menu, then select **Notification Preferences > Send Desktop Notifications**.

Send mobile push notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, the mobile push notification preference assigned in **Settings** is used for all channels. To customize the mobile push notification for each channel, click the channel name at the top of the page to access the channel menu, then select **Notification Preferences > Send mobile push notifications**.

Channel header
--------------

In the channel menu, select **Edit Channel Header** to change the text that appears next to the channel name at the top of the screen. It can be used to summarize the channel topic or provide links to frequently accessed documents. Any channel member can edit this setting, unless the System Admin has `restricted the permissions <https://docs.mattermost.com/configure/configuration-settings.html#enable-public-channel-renaming-for>`__.

Adding links to the channel header
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Frequently-used links to documents, video calls, or other sites can be added to the channel header using markdown.

Example: `Google Hangout <https://plus.google.com/hangouts/_/store.com/shipping>`_

Channel purpose
---------------

In the channel menu, select **Edit Channel Purpose** to change the text that appears in the **More…** menu for channels. The channel purpose is usually a short description that helps others decide whether to join the channel. Any channel member can edit this setting, unless the System Admin has `restricted the permissions <https://docs.mattermost.com/configure/configuration-settings.html#enable-public-channel-renaming-for>`__.

Channel name
------------

In the channel menu, select **Rename Channel** to change the channel name or handle. Changing the channel handle changes the channel URL. Any channel member can edit this setting, unless the System Admin has
`restricted the permissions <https://docs.mattermost.com/configure/configuration-settings.html#enable-public-channel-renaming-for>`__. Please note that `some unicode characters <https://www.w3.org/TR/unicode-xml/#Charlist>`_ are not supported.
