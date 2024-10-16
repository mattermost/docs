Share links to channels and messages
====================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

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
  - If you're unable to share links, contact your Mattermost system admin for assistance. An :doc:`SSL certificate (or a self-signed certificate) </onboard/ssl-client-certificate>` may be required for this functionality to work.

Deep links
--------------
A Mattermost deep link is a URL that directs users to a specific location within Mattermost. Typically, these links are used to go to specific teams, channels, messages, or threads. 

.. tip::

  Deep links can also be used, in combination with bots, scripts, and integrations, to trigger specific actions within Mattermost.
  
To customize the Mattermost deep link for suitability:
-----------------
Take the link you have copied from the three dots around your message or the channels that you are working on and will find at the dropdown menu e.g., https://your-mattermost-domain.com/team-name/channels/channel-name. 

For Mobile deep linking; which represents the structuring link in such a way that it can open your Mattermost mobile application. 
1. Starting with the URL structure; let's assume you have mattermost://team-id/messages/message-id. 

Configure the link by modifying the team id in the URL by replacing the teamid with the name of your choice.

Also replace the messageid with a name that is unique to you for proper identification in your channels. 
 
For web deep linking
Which takes users directly to the content you have for them directly from your browser, follow the guidelines given to you from the previous section, which comprises: 
Locate the permalink to the file. 
Copying the URL 
And distributing in any part of your message. 

Furthermore, you can customize the link by building a button for it, thereby making it more attractive and interactive for your users or team. 

Before you launch your link with assurance, test the link by yourself in your browser or mobile app to ascertain that it is readily available upon demand and compatible with the Mattermost functionary packages. 

You are now acquainted with the techniques you can deploy to enhance the experience of your team in Mattermost collaborative application, by issuing straightforward reference within your content with deep links. Go ahead and add a deep link to your message.  
