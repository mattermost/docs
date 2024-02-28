Share links to channels and messages
====================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |copy-link-icon| image:: ../images/link-variant_F0339.svg
  :alt: Use the Copy Link icon to copy the public URL link for an image in a message.
  :class: theme-icon

.. |more-icon| image:: ../images/dots-horizontal_F01D8.svg
  :alt: Use the More icon to access additional message options.
  :class: theme-icon

.. |channel-info| image:: ../images/information-outline_F02FD.svg
  :alt: Use the Channel Info icon to access additional channel management options.
  :class: theme-icon

You can share links to Mattermost `channels <#share-channel-links>`__ and `messages <#share-message-links>`__ with other Mattermost users. 

Share channel links
-------------------

Sharing channel links makes it easy for others to find and join channels. To share a link to a channel, type ``~`` into the message text box, then select the channel you want to link to. If you're a member of multiple teams, only channels for the current team are listed.

.. tip::

  Alternatively, you can select the **View info** |channel-info| icon in the top right corner of the screen to access additional channel management options, including a **Copy Link** option you can share with others.

Share message links
-------------------

.. tab:: Web/Desktop

  Sharing message links displays a preview of the message in the post. To share links to messages in Mattermost, select the **More** |more-icon| icon next to a message, then select **Copy Link**. 

  .. image:: ../images/message-more.png
    :alt: When you hover over messages, you can access more message options from the More icon.

  .. image:: ../images/copy-link.png
    :alt: You can share links to messages with others using the More option.

  Paste the link into a message to share the image link with others. Sharing links to messages generates a preview of the message.

  .. image:: ../images/permalink-previews.png
    :alt: Mattermost generates previews of links shared in Channels.

  .. tip::

    - You can also hover over an image and select the |copy-link-icon| icon in the top right corner. 
    - The timestamp next to the username of any message is also a permanent link to that conversation.

.. tab:: Mobile

  Long press a message, and then tap **Copy Link** to copy the link to the clipboard. Long press to paste the link as a message or reply. Sharing links to messages generates a preview of the message.

.. note::

  - Message previews respect channel membership permissions, so they’re only visible to users who have access to the original message. If the link is to a message in a public channel, any member of the team can see the message preview. If the link is to a message in a private channel or direct message, only members in that channel can see the message preview.
  - If you're unable to share links, contact your Mattermost system admin for assistance. An `SSL certificate (or a self-signed certificate) </onboard/ssl-client-certificate.html>`__ may be required for this functioanlity to work.