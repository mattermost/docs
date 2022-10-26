Send messages
=============

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |gear-icon| image:: ../images/settings-outline_F08BB.svg
  :alt: Select the Gear icon to open the Settings dialog.

.. |more-icon| image:: ../images/dots-horizontal_F01D8.svg
  :alt: Select the More icon to access additional message actions.

Compose a message by typing into the text box at the bottom of Mattermost. Press :kbd:`Enter` on Windows or Linux, or :kbd:`↵` on Mac, to send the message. To create a new line without sending the message, press :kbd:`Shift` :kbd:`Enter` on Windows or Linux, or press :kbd:`⇧` :kbd:`↵` on Mac. 

`Mattermost Professional or Enterprise <https://mattermost.com/pricing>`__ customers can `edit or delete messages <#edit-or-delete-messages>`__ after sending them if the System Admin hasn't restricted the ability to do so using `advanced permissions </onboard/advanced-permissions.html>`__.

.. tip::
  
  - When you send messages in a channel, depending on the `channel actions configured </channels/create-channels.html>`__, specific words in the post can trigger a prompt to run a playbook. Access **Channel Actions** from the channel name drop-down menu in the center pane to see what automatic actions have been configured.
  - Using a RTL plugin, Mattermost can automatically detect and display messages written using right-to-left scripts, such as Arabic, Hebrew, or Persian. Your System Admin must install the `RTL Plugin <https://github.com/QueraTeam/mattermost-rtl>`__ to enable this functionality.

.. tabs::

  .. tab:: Mattermost v6.0 onwards

      If you prefer to press :kbd:`Enter` on Windows or Linux, or :kbd:`↵` on Mac to insert new lines, and press :kbd:`Ctrl` :kbd:`Enter` on Windows or Linux, or :kbd:`⌘` :kbd:`↵` on Mac to send messages instead, select the **gear** |gear-icon| icon to go to **Settings**, then select **Advanced > Send messages on CTRL+ENTER**.

  .. tab:: Mattermost v5.39 and earlier

      In Mattermost versions up to v5.39, you can configure Mattermost to press :kbd:`Enter` on Windows or Linux, or :kbd:`↵` on Mac to insert new lines, and press :kbd:`Ctrl` :kbd:`Enter` on Windows or Linux, or :kbd:`⌘` :kbd:`↵` on Mac to send messages instead. Select the three horizontal lines at the top of the channel sidebar (also known as a hamburger menu) to go to **Account Settings**, then select **Advanced > Send messages on CTRL+ENTER**.
  
Edit or delete messages
-----------------------

Select the **More** |more-icon| icon next to a message that you've sent.

.. image:: ../images/more-actions.png
   :alt: Select the More option to edit or delete a sent message.

Select **Edit** to edit your own messages. Editing a message won't trigger new @mention notifications, desktop notifications, or notification sounds.

Select **Delete** to delete your own messages. Select **Delete** again to confirm.
