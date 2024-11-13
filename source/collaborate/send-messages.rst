Send messages
=============

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. tab:: Web/Desktop

  Enter a message in the text field, then select **Send** |send-icon| to send the message. You can include images and file attachments to your messages by:

  - copying and pasting images.
  - dragging-and-drop image files into the text field.
  - selecting the **Attachment** |attachments-icon| icon.

  Compose a message by typing into the text box at the bottom of the Mattermost screen, then select the **Send** |send-icon| icon.

  You can also use a keyboard to send messages:
  
  - Press :kbd:`Enter` on Windows or Linux, or :kbd:`↵` on Mac. 
  - To create new text lines, press :kbd:`Shift` :kbd:`Enter` on Windows or Linux, or press :kbd:`⇧` :kbd:`↵` on Mac. 

  .. tip::

    - From Mattermost v10, when sending a direct message, Mattermost warns you that the recipient's availability is set to :ref:`Do Not Disturb <preferences/set-your-status-availability:set your availability>`, and when the recipient's local time is outside of regular business hours (between 10PM and 6AM). This warning displays directly above the message text field.
    - If you find you're accidentally sending messages too soon, you can configure Mattermost to require :kbd:`Shift` :kbd:`Enter` on Windows or Linux, or press :kbd:`⇧` :kbd:`↵` on Mac to send all messages. Select the **gear** |gear| icon to go to **Settings**, then select **Advanced > Send messages on CTRL+ENTER**.

.. tab:: Mobile

  1. In a channel, tap on the text field at the bottom of the Mattermost app to type a message.

  .. image:: ../images/mobile-type-a-message-in-a-channel.jpg
    :alt: Type a message in the text box at the bottom of the mobile app.
    :scale: 30

  2. Tap on **Send** |send-icon| icon to send it in the channel.

  .. image:: ../images/mobile-sending-a-message.gif
    :alt: Tapp on the send icon to send the message in the channel.
    :scale: 50


.. tip::

  - When you send messages in a channel, depending on the :doc:`channel actions configured </collaborate/create-channels>`, specific words in the post can trigger a prompt to run a playbook. Access **Channel Actions** from the channel name drop-down menu in the center pane to see what automatic actions have been configured for the current channel.
  - Using a RTL plugin, Mattermost can automatically detect and display messages written using right-to-left scripts, such as Arabic, Hebrew, or Persian. Your system admin must install the `RTL Plugin <https://github.com/QueraTeam/mattermost-rtl>`__ to enable this functionality.
  - `Mattermost Enterprise or Professional <https://mattermost.com/pricing>`__ customers can `edit or delete messages <#edit-or-delete-messages>`__ after sending them if the system admin hasn't restricted the ability to do so using :doc:`advanced permissions </onboard/advanced-permissions>`.
  
Draft messages
--------------

.. tab:: Web/Desktop

  From Mattermost v7.7, when composing new messages, it's easy to return to a message in progress later. Draft messages are added to a **Drafts** view available at the top of the channel sidebar 

  .. image:: ../images/Global-Drafts-Animated-GIF.gif
    :width: 700
    :alt: Global drafts makes it easy for you to find all messages in progress.

  By default, message drafts are synchronized on the Mattermost server and are accessible everywhere you access Mattermost, including a web browser or the desktop app. 

  .. Tip::
  
    You can disable server-synchronized drafts and limit drafts to your current Mattermost client only by going to **Settings > Advanced > Allow message drafts to sync with the server**.

.. tab:: Mobile

  When composing a message, you can simply opt to complete it later by exiting the channel. 
  
  The partially composed message is retained in the text field and you can see a |edit-icon| before the channel name on the app.

  .. image:: ../images/mobile-draft-a-message.gif
    :alt: You can sync a daft message by exiting the channel mid-way while composing the message.
    :scale: 50


.. note::

  System admins can disable global drafts by disabling the :ref:`message draft server sychronization configuration setting <configure/site-configuration-settings:enable server syncing of message drafts>` in the System Console.

Edit messages
--------------

.. tab:: Web/Desktop

  All users can edit their own sent messages, unless the system admin has :doc:`restricted the ability to do so </onboard/advanced-permissions>`.

  1. Using Mattermost in a web browser or the desktop app, select the **More** |more-icon| icon next to a message that you've sent.

    .. image:: ../images/more-actions.png
      :alt: Select the More option to edit or delete a sent message.

  2. Select **Edit** to edit your own messages. Editing a message won't trigger new :doc:`@mention notifications </collaborate/mention-people>`, or :doc:`desktop notifications </preferences/manage-your-notifications>`.

.. tab:: Mobile

  1. Long press on the message that you want to edit and tap on **Edit**.

  .. image:: ../images/mobile-edit-a-message.gif
    :alt: Tap and hold on a message that you want to edit.
    :scale: 50

  2. Type the updated message and tap on **Save**.

  .. image:: ../images/mobile-editing-a-message.jpg
    :alt: Type the updated message and tap save to save the edited message.
    :scale: 30


Delete messages
----------------

.. tab:: Web/Desktop

  All users can delete their own sent messages, unless the system admin has :doc:`restricted the ability to do so </onboard/advanced-permissions>`.

  1. Using Mattermost in a web browser or the desktop app, select the **More** |more-icon| icon next to a message that you want to delete.
  2. Select **Delete** to delete your own messages. Select **Delete** again to confirm.

.. tab:: Mobile

  1. Long Press on the message you want to delete and tap on **Delete**.

  .. image:: ../images/mobile-delete-a-message.gif
    :alt: Tap and hold on the message that you want to delete.
    :scale: 50

  2. Tap on **Delete** again to confirm your choice.

  .. image:: ../images/mobile-confirm-delete-a-message.jpg
    :alt: Confirm your choice to delete the message.
    :scale: 30

Restore a previous version of an edited message
-----------------------------------------------

From Mattermost v7.9, you can view the edit history of your edited messages, and restore a previous version of an edited message. Message recipients can't see your message edit history, and restoring a previous message version won't trigger new :doc:`@mention notifications </collaborate/mention-people>`.

1. Select the word *Edited* next to your message. 
2. In the right pane, you'll see all previous versions of the message.
3. Select the **Restore** |restore-edit| icon next to the version you want to restore.
4. Select **Confirm**.

.. image:: ../images/restore-previous-edited-message.gif
  :alt: Select Edited next to an edited message, and then select the version you want to restore.

.. note::
  
  Restoring a previous version of the message is available in the Mattermost desktop app or a web browser. The ability to restore using the mobile app isn't supported.

Do more with your messages
--------------------------

Express yourself your way using the following message features:

- :doc:`Set message priority </collaborate/message-priority>`
- :doc:`Format messages </collaborate/format-messages>`
- :doc:`Mention people </collaborate/mention-people>`
- :doc:`Share files </collaborate/share-files-in-messages>`
- :doc:`Share links to channels and messages </collaborate/share-links>`
