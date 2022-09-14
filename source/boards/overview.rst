Overview
========

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Mattermost Boards provides tight integration between project management and Mattermost to align, define, organize, track, and manage work across teams, and is part of all Mattermost editions. Boards is also available as a separate single-user Personal Edition called Focalboard.

With Boards you can:

* **Manage projects and organize tasks:** A familiar kanban board structure integrated with channel-based communication.
* **Manage and collaborate on various projects:** Software releases, product launches, meetings, personal to-do’s, events, etc.
* **Stay on schedule:** Clearly-defined tasks, owners, checklists, and deadlines
* **Increase transparency and keep everybody in the loop:** Everything your team needs in one place, including documents, images, and links that are visible to every stakeholder

What's a board?
---------------

A board is a collection of cards to help you manage your projects, organize tasks, and collaborate with your team all in one place.

Boards can be displayed and filtered in different views such as kanban, table, calendar, and gallery views to help you visualize work items in the format that makes most sense to you.```

What's a card?
--------------

Cards are used on a board to track individual work items. Cards are customizable and can have a number of properties added to them, which are then used as a way to tag, sort, and filter the cards.

When working with cards, you can manage properties, add descriptions, attach images, assign them to team members, mention team members, add comments, and so on.

Access your boards
------------------

Open the Boards tab via the product menu in the top left corner of Mattermost, to view all the boards for your team. You can select the Boards icon in the Apps Bar to open the right-hand panel, and display boards linked to the channel or message that you're in.

If you don't see the Apps Bar and your boards layout looks different to what's described, you may be using an older version of Mattermost. The navigation content in this documentation will not be aligned with your navigation, but the functionality described will be applicable across versions unless otherwise noted.

Focalboard personal server and desktop
--------------------------------------

The Focalboard personal server and desktop apps have some limitations in terms of functionality. Here are some differences you will notice between them and the Boards plugin:

- You can't create private boards in the app versions. 

Link a board to a channel
-------------------------

From Mattermost Boards v7.2, boards can be linked to channels and accessed from the channel Apps Bar. Select the Boards icon from the Apps Bar in a channel to open a right-hand sidebar (RHS) where channel members can search for and link boards to the channel. To link a board to the channel, select **Add** button to open the link boards dialog and search for a board to link. Channel members can only search and link boards within the team where they are also board admins.

.. note:: 
 
  A channel can be linked to multiple boards, but each individual board can only be linked to one channel at a time. Linking the same board to another channel will automatically remove the link from the previous channel.

Open the boards App Bar icon, and select **Create a Board** to create a new board linked to the current channel. Once a board is linked to a channel, it's listed in the RHS of the Boards Apps Bar. Linking a board to a channel automatically grants all channel members access to the board. Select a linked board to navigate directly to the board.

.. note:: 
  
  For users upgrading to Mattermost Boards v7.2 or later. To maintain the same organization, all the boards previously associated with the workspace will automatically appear on the RHS post-migration.

Unlink a board from a channel
-----------------------------

If you're a board admin and want to unlink a board from a channel you're in, open the Boards Apps Bar, select the options menu **(...)** and select **Unlink**. Alternatively, you can open the **Share** dialog on the board, open the **Role** drop-down menu next to the channel's name and select **Unlink**.
