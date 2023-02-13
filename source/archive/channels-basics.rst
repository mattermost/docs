:nosearch:

Channels Basics
================

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Write messages
--------------

Write messages using the text input box at the bottom of Mattermost. Press :kbd:`Enter` to send a message. Press :kbd:`Shift` :kbd:`Enter` on Windows or Linux, or press :kbd:`⇧` :kbd:`↵` on Mac, to create a new line without sending a message. 

.. tabs::

  .. tab:: Mattermost v6.0 onwards

      You can press :kbd:`Enter` to insert new lines, and press :kbd:`Ctrl` :kbd:`Enter` on Windows or Linux, or :kbd:`⌘` :kbd:`↵` on Mac, to send messages instead. Select the |gear-icon| to go to **Settings**, then select **Advanced > Send messages on CTRL+ENTER**.

      .. |gear-icon| image:: ../images/settings-outline_F08BB.svg
        :alt: Select the Gear icon to open the Settings dialog.

  .. tab:: Mattermost v5.39 and earlier

      In Mattermost versions up to v5.39, you can press :kbd:`Enter` to insert new lines, and :kbd:`Ctrl` :kbd:`Enter` on Windows or Linux, or :kbd:`⌘` :kbd:`↵` on Mac, to send messages instead. Select the three horizontal lines at the top of the channel sidebar (also known as a hamburger menu) to go to **Account Settings**, then select **Advanced > Send messages on CTRL+ENTER**.
      
Reply to messages
------------------

Reply to messages by selecting the |reply-arrow| icon next to the message text.

.. |reply-arrow| image:: ../images/reply-arrow.png
  :alt: Reply icon.

Notify teammates
----------------

Let teammates know when they're needed by typing ``@username``.

Link to channels
----------------

Create a link to a Public Channel in a message by typing ``~`` followed by the channel name (e.g. ``~roadmap``). From Mattermost v6.2, channel members also see Private Channel names returned.

Format your messages
--------------------

Format your messages using Markdown that supports text styling, headings, links, emojis, code blocks, block quotes, tables, lists, and in-line images.

You can use either ``_`` or ``*`` for italics and bold text. 

.. image:: ../images/messagesTable1.png
   :alt: Formatting markdown controls the look and feel of text messages.

See our `Formatting Text </messaging/formatting-text.html>`__ documentation for more details and examples.

React to messages
-----------------

React to messages quickly by selecting the |smile-icon| icon inside the Mattermost message input box to open the Emoji Picker.

.. |smile-icon| image:: ../images/smile-icon.png
  :alt: Smile icon.

Or, react to messages by typing ":" followed by two characters, which will open an emoji autocomplete. If the existing emojis don't cover what you want to express, you can also create your own `Custom Emoji </messaging/using-emoji.html#creating-custom-emojis>`__.

Share files
-----------

Share files by dragging and dropping them into Channels, or by selecting the |attachment-icon| icon within the message input box.

.. |attachment-icon| image:: ../images/attachment-icon.png
  :alt: Attachment icon.

Save messages for follow up
---------------------------

Save messages for later follow up by selecting the |save-icon| icon next to the message.

.. |save-icon| image:: ../images/save-icon.png
  :alt: Save icon.

.. image:: ../images/save-message.png
   :alt: Save messages for later follow up.

Learn more about:

* `Composing Messages and Replies </messaging/sending-receiving-messages.html>`__
* `Mentioning Teammates </messaging/mentioning-teammates.html>`__
* `Formatting Messages using Markdown </messaging/formatting-text.html>`__
* `Sharing Files </messaging/sharing-files.html>`__
* `Executing Commands </messaging/executing-slash-commands.html>`__
