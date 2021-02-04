Organizing Conversations
========================

Conversations in Mattermost are crucial to company productivity and success. Keeping information and messages organized in channels creates an efficient workplace.

1. `Channel types`_
2. `Managing channels`_

--------------
Channel types
--------------

Channels are used to organize conversations across different topics. There are three types of channels:

- Public channels
- Private channels
- Direct Messages and Group Messages

Public channels
~~~~~~~~~~~~~~~

Public channels are open to everyone on a team. New team members are automatically added to two Public channels when they sign up: ``Town Square`` and ``Off-Topic``.

Private channels
~~~~~~~~~~~~~~~~

Private channels are for sensitive topics and are only visible to select team members. In Team Edition, any member of a Private channel can add or remove other members from Private channels, but in Enterprise Edition `these permissions can be restricted to the Channel Admin and System Admin <https://docs.mattermost.com/help/getting-started/managing-members.html#user-roles>`__.

Direct Messages and Group Messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Direct Messages are conversations between two people. Group Messages are Direct Messages that have conversations among three or more people. Both are visible only to the people involved.

Use a Direct Message when you want a private conversation with one person. Use a Group Message when you want to set up a conversation with up to seven other participants. If you want to communicate with more than seven people, you must create a Private channel.

If your System Admin has allowed it, you can start a Direct Message or a Group Message with people on other teams.

.. tip :: Check the online status indicator next to names in the Direct Message list. It displays: **Online** (green checkmark indicates active browser), **Away** (orange clock indicates browser activity for 5 minutes), **Do Not Disturb** (red dash indicates disabled desktop and push notifications), and **Offline** (white circle indicates the Mattermost client is closed).

------------------
Managing channels
------------------

Channels can be created, joined, renamed, left, marked as a favorite, muted, unmuted, and archived.

Creating a channel
~~~~~~~~~~~~~~~~~~~

Create a new Public channel or Private channel by selecting the **+** symbol next to the **Public Channels*** or **Private Channels** header on the left hand navigation. To start a Direct Message thread, select the **+** symbol next to the **Direct Messages** bar or select **More** at the bottom of the list to view team members you can message.

    .. image:: ../../images/Create_private_channel.png

Anyone can create Public channels or Private channels, unless the System Admin has `restricted the permissions <https://docs.mattermost.com/administration/config-settings.html#enable-public-channel-creation-for>`__.

Joining a channel
~~~~~~~~~~~~~~~~~~

Select **More** at the bottom of the **Public Channels** list to view and search through a list of Public channels you can join. To join a Private channel you need to be added by a member of that channel.

Adding members to a channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the channel name at the top of the center pane to access the drop-down menu, then select **Add Members**. Any member of a channel can add new members by choosing **Add** next to a user's name. Users already added to the channel will not appear in this list.

    .. image:: ../../images/add_members.png

You can also add users to channels within their profile pop-over by choosing **Add to a Channel** and selecting the channel you want them to join.

    .. image:: ../../images/add_members_pop.png

Removing members from a channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the channel name at the top of the center pane to access the drop-down menu, then select **Manage Members**. Any member of a channel can remove other members by choosing **Remove** next to a user's name.

Naming a channel
~~~~~~~~~~~~~~~~~

Channels can be identified in two ways:

1. **Channel display name:** This appears in the Mattermost user interface. Click the channel name at the top of the center pane to access the drop-down menu, then choose **Rename Channel**. Anyone can rename the channels they belong to, unless the System Admin has `restricted the permissions <https://docs.mattermost.com/administration/config-settings.html#enable-public-channel-renaming-for>`__.
2. **Channel handle:** This is part of the channel URL. You may also change the channel handle when renaming a channel, but changing channel handles may break existing links.

For example, for the following channel, https://community.mattermost.com/core/channels/ux-design:

- Channel display name: ``UX Design``
- Channel handle: ``ux-design`` 

Leaving a channel
~~~~~~~~~~~~~~~~~

Select the channel name at the top of the center pane to access the drop-down menu, then select **Leave Channel**. Any team member who leaves a Private channel must be re-added by another channel member if they wish to rejoin. Team members will not receive mention notifications from channels of which they are not members.

Archiving a channel
~~~~~~~~~~~~~~~~~~~~

Select the channel name at the top of the center pane to access the drop-down menu, then select **Archive Channel**. Anyone can archive the Public channels or Private channels they belong to, unless the System Admin has `restricted the permissions <https://docs.mattermost.com/administration/config-settings.html#id2>`__.

When a channel is archived, it is removed from the user interface, but a copy exists on the server in case it is needed for audit reasons at a later stage. Because of this, the URL of a newly created channel cannot be the same URL name as an archived channel.

In addition to this, when a channel is archived, by default the contents cannot be viewed, shared, or searched. If you want to be able to view or search the channel later, either:

1. Ask your System Admin to set ``ExperimentalViewArchivedChannels`` to ``true`` in ``config.json`` to allow users to view, share, and search for content of channels that have been archived; or
2. Leave the channel open, but post a message in the channel saying it's considered archived: such as ``# This channel is archived.``

System Admins `can archive channels in the System Console <https://docs.mattermost.com/deployment/team-channel-management.html#profile>`_ without needing to be a channel member.

Unarchiving a channel
~~~~~~~~~~~~~~~~~~~~~~

Search for the channel if required. Then, open the channel, select the channel name at the top of the center pane to access the drop-down menu, then select **Unarchive Channel**. System Admins and Team Admins can unarchive the Public channels or Private channels they belonged to when it was archived.

    .. image:: ../../images/unarchive-channel.png

When a channel is unarchived, channel membership and all its content is restored, unless messages and files have been deleted based on the :doc:`data retention policy <data-retention>`.

In addition to this, System Admins can also unarchive channels `via the CLI <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-channel-restore>`_ and Team Admins can unarchive them `via the API <https://api.mattermost.com/#tag/channels/paths/~1channels~1%7Bchannel_id%7D~1restore/post>`_.

Converting Public channels to Private channels (and vice versa)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select the channel name at the top of the center pane to access the drop-down menu, then select **Convert to Private Channel**. Team and System Admins can convert Public channels to Private channels. Please note that default channels such as ``Town Square`` and ``Off-Topic`` cannot be converted to Private channels.

System Admins can also access this setting in **System Console > Channels > Edit (Channel Configuration)**. Due to security concerns of sharing Private channel history, only System Admins can convert Private channels to Public. 

When a channel is converted, its history and membership are preserved. Membership in a Private channel is by invitation only. Publicly shared files remain accessible to anyone with the link.

Note that conversion of Private channels to Public channels can only be performed by a System Admin via the System Console or via `CLI command <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-channel-modify>`__.

Favoriting a channel
~~~~~~~~~~~~~~~~~~~~

Favorite channels are a great way to organize your sidebar by choosing which Public channels, Private channels, and Direct Messages are most important to you.

To mark a channel as a favorite, open the channel:

**On desktop:** At the top of the page, select on the star icon next to the channel name

    .. image:: ../../images/favorite_channels_desktop.png
        :alt: Mark a channel as a favorite.
        :scale: 40
       
This adds the channel to a **Favorites** list at the top of the sidebar, so it's easy to access. To remove a channel from the **Favorites** list, select the star again.

    .. image:: ../../images/favorite_channels_sidebar.png
        :alt: Favorite channels in the left-hand sidebar.
        :scale: 40
       
**On mobile:** Open the dropdown list by the channel name, and select **Favorite**. To remove a channel from the **Favorites** list, select **Favorite** again.

Muting a channel
~~~~~~~~~~~~~~~~

Select the channel name at the top of the center pane to access the drop-down menu, then select **Mute Channel**. 

Once a channel is muted:

- Email, desktop, and push notifications are disabled.
- A mute icon displays next to the channel name.
- The channel is greyed out in the left-hand sidebar, and the channel isn't marked as unread unless you're mentioned directly. 

To unmute the channel, select the channel name again to access the drop-down menu, then select **Unmute Channel**.

--------------------------------------------
Experimental: Channel Organization Features
--------------------------------------------

Join us in testing an experimental feature set offering additional functionality for managing channels in your sidebar. The features can be enabled using an opt-in config setting configured by a System Admin: `ExperimentalChannelSidebar <https://docs.mattermost.com/administration/config-settings.html#experimental-sidebar-features-experimental>`_.

When configured by the System Admin, users can enable the features in **Account Settings > Sidebar > Experimental Sidebar Features**. Features include:

**Collapsible custom categories:** Create custom categories in the sidebar to group channels together for easier navigation (e.g. “Design” or “Marketing”). Collapse categories to display only unread channels and reduce unnecessary scrolling.

**Mute and unmute custom categories**: Mute and unmute all channels in a custom category, and selectively mute or unmute select channels within categories.

**Select multiple channels at a time**: Using the Mattermost Web or Desktop App, select sequential channels by pressing and holding SHIFT. To select non-sequential channels press and hold CMD (for Mac) or CTRL (for Windows/Linux). To clear channel selections, press ESC.

**Drag and drop channels and categories:** Drag selected channels between or within categories, or drag to reorder entire categories to prioritize important conversations. Multi-selected channels move together as a group in the order they originally appeared. You can also specify a destination for selected channels using the **Move to** option under the **More options** icon. The **Move to** option is available today for Cloud deployments and will be available for self-hosted deployments in Mattermost Server v5.32 and later.

**Sort Direct Messages by recent conversations**: Choose to sort Direct Messages alphabetically or by recent conversations first. 

**Unread filter**: Catch up on all your unread channels with a one-click unreads filter. When enabled, you'll see only unread channels in the sidebar.

**History arrows**: Navigate recently viewed channels more easily with arrows to move back and forth through channel history. Available in the Desktop app only.

`Learn more about upcoming additions to this feature set and give us feedback here <https://about.mattermost.com/default-sidebar/>`_.

 .. image:: ../../images/sidebar-phase-2.gif
