Customize your channel sidebar
==============================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Conversations in Mattermost are crucial to company productivity and success. Keeping conversations organized in the sidebar creates an efficient workplace. Using a web browser or the desktop app, you can customize your own channel sidebar based on how you prefer to use Mattermost. Customizations you make are only visible to you, are visible when using the mobile app, and won't affect what your teammates see in their sidebars.

Here's how your sidebar is set up by default:

- All public and private channels you've joined are listed in the **Channels** category, sorted alphabetically.
- All your direct messages and group messages are listed in the **Direct Messages** category, sorted by recent activity.

What can you customize?
-----------------------

Using Mattermost in a web browser or the desktop app, you can customize your sidebar in the following ways:

- `Create custom categories <#create-custom-categories>`__
- `Group and order channels into your categories <#organize-channels-in-categories>`__
- `Mute and unmute entire categories <#mute-and-unmute-categories>`__
- `Mark entire categories as read <#mark-channel-categories-as-read>`__
- `Sort channels in each category <#sort-channels-in-categories>`__ manually, alphabetically, or by recent activity
- `Filter your sidebar to view unread channels only <#group-unread-channels-separately>`__, or choose to group unread messages into an **Unreads** category
- `Manage your direct messages <#manage-direct-messages>`__ by sorting them alphabetically or by recent activity, and by setting how many to display in your sidebar
- `Make channel categories work for you <#make-categories-work-for-you>`__ by prefixing category names with emojis, by collapsing and expanding categories, by reordering categories, and by adding direct message conversations to categories.

.. image:: ../images/channel_sidebar_updates.gif
   :alt: Organize your channel sidebar with channel categories.

Create custom categories
-------------------------

Create custom categories to group channels together for quicker and easier navigation. For example, you can create a category called "Design" or "Marketing".

To create categories, select the **+** symbol at the top of the sidebar. Or, select the **More options** |more-icon| icon in the sidebar on any category header, then select **Create New Category**.

Next, type a category name, select **Create**, then drag any channels or direct messages into this new category. You can also multi-select channels and direct messages to drag them together as a group by pressing :kbd:`Ctrl` or :kbd:`Shift` and selecting on Windows or Linux, or :kbd:`⌘` or :kbd:`⇧` and selecting on Mac. See the section `drag and drop selections <#drag-and-drop-selections>`__ below for details.

Your custom categories can't be shared with other Mattermost users.

Rename categories
------------------

1. Select the **Category options** icon in the sidebar, then select **Rename Category**.
2. Type a new category name, then select **Rename**.

Delete categories
------------------

1. Select the **Category options** icon in the sidebar, then select **Delete Category**.
2. Select **Delete** to confirm or select **X** to cancel.

All channels and direct message conversations in the deleted category move back to their default **Channels** and **Direct Messages** categories. Deleting a category never removes you from channels you have joined.

Organize channels in categories
-------------------------------

Once you've created categories, you can move channels around to organize your sidebar by dragging and dropping, or by moving.

Drag and drop selections
~~~~~~~~~~~~~~~~~~~~~~~~

To select multiple channels:

- Select sequential channels and/or direct messages by pressing :kbd:`Shift` while selecting on Windows or Linux, or :kbd:`⇧` while selecting  on Mac. 
- Select non-sequential channels and/or direct messages by pressing :kbd:`Ctrl` while selecting on Windows or Linux, or :kbd:`⌘` while selecting on Mac
- Press :kbd:`ESC` to clear channel or direct message selections.

Using the Mattermost web or desktop app, drag selected channels and/or direct messages between or within categories. 

.. tip::

  Multi-selected channels and direct messages move together as a group in the order they originally appeared. 

.. image:: ../images/multi-select-drag.gif
   :alt: Move a group of selected channels by dragging them to a new location in the channel sidebar.

Move selections
~~~~~~~~~~~~~~~

In addition to selecting and dragging, you can specify a category destination for selected channels and/or direct messages. To do this, select the **Channel options** icon in the sidebar and then select **Move to**.

.. image:: ../images/multi-select-move.gif
   :alt: Move a group of selected channels to a specified category destination. 

You can also specify a category destination for the current channel or conversation using the **Move to** option directly from the channel header. Channels that have been moved to a category will display a checkmark next to the category name.

.. image:: ../images/channel-heading-categories.png
  :alt: Move channels or conversations directly from the channel header.

Mute and unmute categories
---------------------------

When you mute or unmute a category, all channels within that category are also muted or unmuted. You can selectively unmute specific channels within a muted category.

Select the **Category options** icon in the sidebar, then select **Mute Category**.

Once a category is muted:

- Email, desktop, and push notifications are disabled for all channels in the category.
- A mute icon displays next to each channel name in the category.
- The category and all of its channels appear at reduced opacity in the left-hand sidebar. Channels in the category aren't marked as unread unless you’re mentioned directly.

To unmute the category, select the **Category options** icon in the sidebar, then select **Unmute Category**.

.. image:: ../images/mute-categories.gif
   :alt: Mute or unmute a category to mute or unmute all channels within that category. You can also selectively unmute specific channels within a muted category.

Mark channel categories as read
-------------------------------

When you mark a channel category as read, all channels within that category are marked as read. You can selectively mark specific channels as unread where preferred.

Select the **Category options** icon in the sidebar, then select **Mark category as read**.

Sort channels in categories
----------------------------

Select the **Category options** icon in the sidebar, then select **Sort** and choose from **Alphabetically**, **Recent Activity**, or **Manually**.

.. image:: ../images/sort-categories.gif
   :alt: Sort channels within a category alphabetically, by recent activity, or manually.

Group unread channels separately
--------------------------------

By default, Mattermost provides a one-click **Unreads** filter to only show channels with unread activity. Alternatively, you may choose to automatically group unread channels in their own category at the top of your sidebar.

Go to **Settings > Sidebar**, set **Group unread channels separately** to **On**, then select **Save**.

- When this setting is enabled, all unread messages appear only in the **Unreads** category, sorted with mentions first.
- When this setting is disabled, all unread messages appear within their respective categories and channels. You can use the **Unread filter** to focus on only unread channels in the sidebar.

When enabled, unread channels with mentions will sort to the top of the category.

.. image:: ../images/unreads.gif
   :alt: The Unreads filter only shows channels with unread activity. You can also group unread channels into their own category at the top of the channel sidebar.

.. tip::
  
  If you prefer to see only unread channels in their respective categories, we recommend collapsing your custom categories and disabling **Group unread channels separately** under **Settings > Sidebar**.

Manage direct messages
----------------------

To sort your direct messages, select the **Channel options** icon in the sidebar, then select **Sort** and choose from **Alphabetically** or **Recent Activity**.

How many direct messages to display?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Control how many direct message conversations display in the **Direct Messages** category to keep your conversations manageable. You can choose to show all messages or a fixed number of messages.

To configure the number of direct messages to display, go to **Settings > Sidebar**, then set **Number of direct messages to show**. Or select the **Channel options** icon in the sidebar, then select **Show**.

Choose to show **10**, **15**, **20**, or **40** messages. Once you exceed the number of direct messages configured, older messages are hidden from the **Direct Messages** category. You can always increase the number of conversations displayed to see older direct messages.

.. image:: ../images/dm-display.gif
   :alt: alt: Control the number of direct message conversations to display under the Direct Messages category by showing all messages or a fixed number of messages.

.. note::
  Direct message conversations that you add to custom categories don't count against the maximum number of conversations shown in the **Direct Messages** category.

Make categories work for you
----------------------------

Prefix channel category names with emojis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Channel category names can include emojis. Specify the emoji by its name in the format ``:smile:``. We recommend prefixing channel category names with emojis for the following reasons:

- Emojis can make it easier for users to quickly identify and manage channels and channel categories, particularly in large workspaces with many channels.
- Sharing the same emoji across channels and categories related to a specific category or function helps maintain organization and consistency across the workspace.
- Making channel categories more visually distinct with emojis helps users find what they need more quickly and easily at a glance, reducing the time spent searching for the right place to take action.
- New users can quickly understand the purpose of various channels and channel categories based on their emoji prefixes without needing extensive explanations. 
- As users grasp channel structure through emojis, the time and effort needed to train new members on navigating the workspace is reduced.
- A well-organized and visually appealing workspace can encourage users to participate more actively, which can lead to more effective communication and collaboration.

Categories are collapsible
~~~~~~~~~~~~~~~~~~~~~~~~~~

When you collapse a channel category, only unread channels display to reduce unnecessary scrolling. When you expand a channel category, all channels in the category display, including channels with unread messages.

Reorder categories
~~~~~~~~~~~~~~~~~~

Drag to reorder entire categories to prioritize important conversations. 

Categories can contain direct message conversations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select and drag direct messages into any category. You can also multi-select direct messages to drag them together as a group.