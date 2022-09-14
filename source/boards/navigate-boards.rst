Navigate boards
===============

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:
  
If you're using Mattermost 7.0, open boards using the App Bar. If you don't see the Apps Bar to the right of your screen, you can access boards using the product menu in the top left corner of Mattermost.

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

Sidebar categories
------------------

From Mattermost Boards v7.2, you can organize your boards on the left hand sidebar using custom categories. By default, all boards will appear under the **Boards** category.

To manage your categories, open the options menu **(...)** next to the category to create, delete, or rename a category. With the exception to the default **Boards** category, all other categories can be renamed or deleted.

After creating categories, you can move your boards to those categories by opening the options menu **(...)** next to the board and selecting **Move To…** to select the category where you want the board to be moved.

If you delete a category with boards in it, then those boards will return to the default **Boards** category.

Categories are organized per-user, so you can arrange your boards under categories that make sense to you without impacting boards or categories for other users. If a board is moved to a custom category, then the board will appear under that category for you only. Other users who are members of the board will continue to see the board in their own categories.

.. note::

  For users upgrading to Mattermost Boards v7.2 onwards:If you belonged to a workspace prior to v7.2, then you’ll see that the workspaces have been migrated to custom categories in the sidebar. All boards from a workspace are listed under a category of the same name. Boards from direct messages and group messages appear under the default **Boards** category.
  Categories are per-user, and can be renamed or deleted by each user after migration. New users won’t have default categories, and boards they join will appear under the default **Boards** category.

Boards that you create after the migration won’t be linked to a workspace and will always appear under the default **Boards** category unless you move or hide the boards.

Manage boards on the sidebar
----------------------------

In addition to moving boards to other categories, from the  options menu **(...)** next to each board name you can perform the following actions:

- **Delete board**: If you are an admin of the board, you will see an option to delete the board. Deleting the board permanently removes the board from the sidebar of all board members.
- **Duplicate board**: Creates a copy of the board and all the cards on the board. The duplicated board will appear under the same category as the original board. Board members from the original board are not migrated to the new board.
- **New template from board**: Creates a custom board template of the board and all the cards on the board.
- **Hide board**: Hides the board from your sidebar only. The board will still remain visible on the sidebar for other board members. You can add the board back to your sidebar using the search box (CMD+K/CTRL+K).

Find a board
------------

From the top of the boards left hand sidebar, select the **Find Boards** field (CMD+K/CTRL+K) to open the board switcher, and start typing the name of the board you’re looking for.

Team sidebar
------------

If you’re a member of multiple teams, the team sidebar will appear on the left hand side of Boards. To switch teams, select any of the team icons from the team sidebar.

Set language
------------

To set your language on boards, select the gear icon next to your profile avatar, then go to **Set language** to apply your language settings. Please note: language settings in Boards are independent from language settings in Channels.

Emoji icons
-----------

To enable or disable random emoji icons for your board and cards, select the gear icon next to your profile avatar, then toggle **Random icons on or off**.

Product tour
------------

If you skipped the product tour or want a refresher on Boards, you can restart the product tour by going to the gear icon next to your profile avatar and selecting **Product tour**. This will add a new **Welcome to Boards** template to your sidebar and kick-off the guided onboarding tour.
