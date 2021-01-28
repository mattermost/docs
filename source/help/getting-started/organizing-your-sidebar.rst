Organizing Your Sidebar
=======================

You can organize your sidebar based on how you use Mattermost. Customizations you make to your sidebar only changes your Mattermost sidebar.

Here's how your sidebar is set up by default:

- All of the channels you've joined display in a **Channels** category. 
- All channels are sorted in alphabetical order.
- All Direct Messages display in a **Direct Messages** category below channels.
- All Direct Messages are sorted by recent activity.

What can you customize?
-----------------------

You can customize your sidebar in the following ways:

- Group and order channels into categories customized just for you.
- Mute and unmute entire categories.
- Sort category channels manually, alphabetically, or by recent activity.
- Group unread messages into an **Unreads** category.
- Sort Direct Messages alphabetically or by recent activity.
- Control how many Direct Message conversations to display.

Creating custom categories
--------------------------

Create custom categories to group channels together for quicker and easier navigation (e.g. “Design” or “Marketing”).

Categories can be created in two ways:

- Select the **+** symbol to the right of the **History** arrows at the top of the sidebar.
- Select the **Channel options** icon in the sidebar, then select **Create New Category**.

Next, type a category name, select **Create**, then drag any channels or Direct Messages into this new category. You can also multi-select channels and Direct Messages to drag them together as a group.

Making categories work for you
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Categories are collapsible**

- When collapsed, only unread channels display to reduce unnecessary scrolling.
- When expanded, all channels in the category display, including channels with unread messages.

**You can reorder categories.**

- Drag to reorder entire categories to prioritize important conversations. 

**Categories can contain Direct Message conversations**

- Click and drag Direct Messages into any category. You can also multi-select Direct Messages to drag them together as a group.

    .. image:: ../../images/sidebar_ga.gif

Renaming categories
^^^^^^^^^^^^^^^^^^^

1. Select the **Category options** icon in the sidebar, then select **Rename Category**.
2. Type a new category name, then select **Rename**.

Deleting categories
^^^^^^^^^^^^^^^^^^^

1. Select the **Category options** icon in the sidebar, then select **Delete Category**.
2. Select **Delete** to confirm or select **X** to cancel.

All channels and Direct Message conversations in the deleted category move back to their default **Channels** and **Direct Messages** categories. Deleting a category never removes you from channels you have joined. 

Organizing channels in categories
---------------------------------

Once you have categories, you can move channels into your categories to organize your sidebar.

Multi-selecting channels and Direct Messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the Mattermost Web or Desktop App:

- Select sequential channels and/or Direct Messages by pressing and holding SHIFT. 
- Select non-sequential channels and/or Direct Messages by pressing and holding CMD (for Mac) or CTRL (for Windows/Linux). 
- Press ESC to clear channel or Direct Message selections.

Multi-selected channels and Direct Messages move together as a group in the order they originally appeared.

Dragging and dropping selections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the Mattermost Web or Desktop App, drag selected channels and/or Direct Messages between or within categories. 

    .. image:: ../../images/multi-select-drag.gif

Moving selections
^^^^^^^^^^^^^^^^^

In addition to selecting and dragging, you can also specify a destination for selected channels and/or Direct Messages using the **Move to** option under the **Channel options** icon in the sidebar.  

    .. image:: ../../images/multi-select-move.gif

Muting and unmuting categories
------------------------------

When you mute or unmute a category, all channels within that category are also muted or unmuted. 

Select the **Category options** icon in the sidebar, then select **Mute Category**.

Once a category is muted:

- Email, desktop, and push notifications are disabled for all channels in the category.
- A mute icon displays next to each channel name in the category.
- The category and all of its channels are greyed out in the left-hand sidebar. Channels in the category aren't marked as unread unless you’re mentioned directly.
- You can selectively unmute specific channels within the category.

To unmute the category, select the **Category options** icon in the sidebar, then select **Unmute Category**.

    .. image:: ../../images/mute-categories.gif

Sorting category channels
-------------------------

Using the Mattermost Web or Desktop App, you can control how channels are sorted for each category. Sort category channels manually (by dragging and dropping), alphabetically, or by recent conversations first.

Select the **Category options** icon in the sidebar, then select **Sort** and choose from **Alphabetically**, **Recent Activity**, or **Manually**.

    .. image:: ../../images/sort-categories.gif

Grouping unread messages
------------------------

Catch up on all your unread channels in one place at the top of your sidebar with a one-click **Unreads** category.

Go to **Main Menu > Account Settings > Sidebar**, set **Group unread channels separately** to **On**, then select **Save**.

- When this setting is enabled, all unread messages appear only in the **Unreads** category.
- When this setting is disabled, all unread messages appear within their respective categories and channels.

When enabled, the **Unreads** category is organized as follows:

- Unread messages that contain mentions are sorted to the top by most recent activity.
- Unread messages that do not contain mentions are sorted by most recent and appear directly below unread messages containing mentions.
- Muted channels that contain mentions are sorted by most recent and appear directly below unread messages without mentions.

    .. image:: ../../images/unreads.gif

.. tip::
  If you prefer to see a decicated unread-only view in your sidebar, collapse all custom categories to show only unread messages, then disable **Grouping unread messages** under **Account Settings > Sidebar**.

Sorting your Direct Messages
----------------------------

Sort your Direct Messages alphabetically or by recent conversations first.

Select the **Channel options** icon in the sidebar, then select **Sort** and choose from **Alphabetically** or **Recent Activity**.

How many Direct Messages to display?
------------------------------------

Control how many Direct Message conversations display in the **Direct Messages** category to keep your conversations manageable. You can choose to show all messages or a fixed number of messages.

You have two ways to configure the number of Direct Messages to display:

- Go to **Main Menu > Account Settings > Sidebar**, then set **Number of direct messages to show**.

or
- Select the **Channel options** icon in the sidebar, then select **Show**

Choose from **All direct messages**, or choose to show **10**, **15**, **20**, or **40** messages.

Once you exceed the number of Direct Messages configured, older messages are hidden from the **Direct Messages** category. You can increase the number of conversations displayed to see older Direct Messages.

.. note::
  Direct Message conversations that you add to custom categories don't count against the maximum number of conversations shown in the **Direct Messages** category.

Mobile support for this feature is coming in a future release.

    .. image:: ../../images/dm-display.gif
