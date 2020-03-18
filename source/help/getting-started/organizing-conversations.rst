Organizing Conversations
======================================

Conversations in Mattermost are crucial to company productivity and success. Keeping information and messages organized in channels creates an efficient workplace.

1. `Channel Types`_
2. `Managing Channels`_

-------------------------------------
Channel Types
-------------------------------------

Channels are used to organize conversations across different topics. 
There are three types of channels: Public Channels, Private Channels, and Direct Messages.

Public Channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Public Channels are open to everyone on a team. New team members are automatically added to two Public Channels when they sign up: Town Square and Off-Topic.

Private Channels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Private Channels are for sensitive topics and are only visible to select team members. In Team Edition, any member of a Private channel can add or remove other members from Private channels, but in Enterprise Edition `these permissions can be restricted to the Channel Admin and System Admin <http://docs.mattermost.com/help/getting-started/managing-members.html#user-roles>`__.

Direct Messages and Group Messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Direct Messages are for conversations between two people. Group Messages are Direct Messages that have conversations among three or more people. Both are visible only to the people involved.

Use a Direct Message when you want a private conversation with one person. Use a Group Message when you want to set up a conversation with up to seven other participants. If you want to communicate with more than seven people, you must create a Private Channel.

If your System Administrator has allowed it, you can start a Direct Message or a Group Message with people on other teams.

.. tip :: Check the online status indicator next to names in the Direct Message list. It displays: online (green checkmark indicates active browser), away (orange clock indicates no browser activity for 5 minutes), do not disturb (red dash indicates disabled desktop and push notifications) and offline (white circle indicates browser is closed).

-----------------------------------------
Managing Channels
-----------------------------------------

Channels can be created, joined, renamed, left and archived.

Creating a Channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new Public Channel or Private Channel by selecting the **+** symbol next to the *Channels* or *Private Channels* header on the left hand side. To start a direct message thread, click the **+** symbol next to the *Direct Messages* bar or select **More** at the bottom of the list to view team members you can message.

    .. image:: ../../images/Create_private_channel.png

Anyone can create Public Channels or Private Channels, unless the System Administrator has `restricted the permissions <https://docs.mattermost.com/administration/config-settings.html#enable-public-channel-creation-for>`__.

Joining a Channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click **More** at the bottom of the *Channels* list to view and search through a list of Public Channels you can join. To join a Private Channel you need to be added by a member of that channel.

Adding Members to a Channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click the channel name at the top of the center pane to access the drop-down menu, then click **Add Members**. Any member of a channel can add new members by clicking **Add** next to a user's name. Users already added to the channel will not appear in this modal.

    .. image:: ../../images/add_members.png

You can also add users to channels within their profile pop-over by clicking "Add to a Channel" and selecting the channel to add them to.

    .. image:: ../../images/add_members_pop.png

Removing Members from a Channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click the channel name at the top of the center pane to access the drop-down menu, then click **Manage Members**. Any member of a channel can remove other members by clicking **Remove** next to a user's name.

Naming a Channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Channels can be identified in two ways:

1. Channel display name: This is the channel name appearing in the Mattermost user interface. Click the channel name at the top of the center pane to access the drop-down menu, then click **Rename Channel**. Anyone can rename the channels they belong to, unless the System Administrator has `restricted the permissions <https://docs.mattermost.com/administration/config-settings.html#enable-public-channel-renaming-for>`__.
2. Channel handle: This is part of the channel URL. You may also change the channel handle when renaming a channel, but changing channel handles may break existing links.

For example, for the following channel: https://community.mattermost.com/core/channels/ux-design

- Channel display name: ``UX Design``
- Channel handle: ``ux-design`` 

Leaving a Channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click the channel name at the top of the center pane to access the drop-down menu, then click **Leave Channel**. Any team member who leaves a Private Channel must be re-added by a channel member if they wish to rejoin. Team members will not receive mention notifications from channels of which they are not members.

Archiving a Channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click the channel name at the top of the center pane to access the drop-down menu, then click **Archive Channel**. Anyone can archive the Public Channels or Private Channels they belong to.  In E10 and E20, the System Administrator is able to `restricted this permissions <https://docs.mattermost.com/deployment/advanced-permissions.html#system-scheme-e10>`_.

When a channel is archived, it is removed from the user interface, but a copy exists on the server in case it is needed for audit reasons later. Because of this, the URL of a newly created channel cannot be the same URL name as an archived channel.

Moreover, when a channel is archived, the contents cannot be viewed, shared or searched by default. If you want to be able to view or search the channel later, either

1. Ask your System Administrator to set ``ExperimentalViewArchivedChannels`` to ``true`` in config.json to allow users to view, share and search for content of channels that have been archived; or
2. Leave the channel open, but post a message in the channel saying it's considered archived, such as ``# This channel is archived.``

Converting Public Channels to Private (and vice versa)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click the channel name at the top of the center pane to access the drop-down menu, then click **Convert to Private Channel**. Team and System Admins have the ability to convert public channels to private channels.  Please note that default channels such as Town Square and Off-Topic cannot be converted to private channels.

System Admins can also access this setting in **System Console > Channels > Edit (Channel Configuration)**.  Due to security concerns of sharing private channel history, only System Admins can convert private channels to public. 

When a channel is converted, history and membership are preserved. Membership in a private channel is by invitation only. Publicly shared files remain accessible to anyone with the link. 

Note that conversion of private channels to public channels can only be performed by a System Admin via the System Console or via `CLI command <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-channel-modify>`__.

Favoriting a Channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Favorite channels are a great way to organize your sidebar by choosing which Channels, Private Channels, and Direct Messages are most important to you.

To mark a channel as a favorite, simply open the channel and then:

**On desktop:** At the top of the page, click on the star next to the channel name

    .. image:: ../../images/favorite_channels_desktop.png
       :scale: 35
       
This will add the channel to a "Favorites" section in the top of the sidebar, so it's easy to access. To remove a channel from the "Favorites" section, click the star again. 

 .. image:: ../../images/favorite_channels_sidebar.png
       :scale: 35
       
**On mobile:** Open the dropdown list by the channel name, and select "Favorite".

To remove a channel from the "Favorites" section, select the "Favorite" option again.

   
