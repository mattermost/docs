Forward messages
================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |more-icon| image:: ../images/dots-horizontal_F01D8.svg
  :alt: When you hover over messages, you can access more message options from the More icon.

From Mattermost v7.2, using a web browser or the desktop app, you can forward messages in public channels to other public channels. From Mattermost v7.5, you can also forward messages from bots and webhooks. 

.. note::
  
  Private channels, direct messages, and group messages intended for specific people can't be forwarded.

To forward a message:

1. Select the **More** |more-icon| icon next to a message, then select **Forward**. 

  .. image:: ../images/forward-message.png
    :alt: You can forward messages to others using the More option.

2. Specify where you want to forward the message, and include an optional comment. 

Forwarding a message also generates a preview of the message.

.. image:: ../images/permalink-previews.png
   :alt: Mattermost generates previews of links shared in Channels.

.. note::
  
  Previews respect channel membership permissions, so they’re only visible to users who have access to the original message. If the link is to a message in a public channel, any member of the team can see the message preview. If the link is to a message in a private channel or direct message, only members in that channel can see the message preview.
