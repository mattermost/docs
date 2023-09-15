:nosearch:
:orphan:

Navigate boards
===============
  
.. |options-icon| image:: ../images/dots-horizontal_F01D8.svg
  :alt: Access additional message actions using the More actions icon.
  
If you've already created a board, you can open the Focalboard plugin using the Apps Bar. If you don't see the Apps Bar to the right of your screen, you can access boards using the product menu in the top left corner of Mattermost.

Link a board to a channel
-------------------------

From Mattermost Boards v7.2, boards can be linked to channels and accessed from the channel Apps Bar. Select the Boards icon from the Apps Bar in a channel to open a right-hand sidebar (RHS) where channel members can search for and link boards to the channel. To link a board to the channel, select **Add** button to open the link boards dialog and search for a board to link. Channel members can only search and link boards within the team where they are also board admins.

.. note:: 
 
  A channel can be linked to multiple boards, but each individual board can only be linked to one channel at a time. Linking the same board to another channel will automatically remove the link from the previous channel.

Open the Boards Apps Bar icon, and select **Create a Board** to create a new board linked to the current channel. Once a board is linked to a channel, it's listed in the right-hand side of the Boards Apps Bar. Linking a board to a channel automatically grants all channel members access to the board, with the exception of guest accounts. Select a linked board to navigate directly to the board.

.. note:: 
  
  If you're upgrading to Mattermost Boards v7.2 or later, all the boards previously associated with the workspace will automatically appear on the right-hand side panel post-migration.

Unlink a board from a channel
-----------------------------

If you're a board admin and want to unlink a board from a channel you're in, open the Boards Apps Bar, select the |options-icon| menu and select **Unlink**. Alternatively, you can open the **Share** dialog on the board, open the **Role** drop-down menu next to the channel's name and select **Unlink**.

Sidebar categories
------------------

From Mattermost Boards v7.2, you can organize your boards in the left-hand sidebar using custom categories. By default, all boards will appear under the **Boards** category. To manage your categories, open the |options-icon| menu next to the category to create, delete, or rename a category. With the exception to the default **Boards** category, all other categories can be renamed or deleted.

After creating categories, you can move your boards to those categories by opening the |options-icon| menu next to the board and selecting **Move To…** to select the category where you want the board to be moved.

If you delete a category with boards in it, then those boards will return to the default **Boards** category.

Categories are organized per-user, so you can arrange your boards under categories that make sense to you without impacting boards or categories for other users. If a board is moved to a custom category, then the board will appear under that category for you only. Other users who are members of the board will continue to see the board in their own categories.

.. note::

  Upgrading to Mattermost Boards v7.2 onwards: If you belonged to a workspace prior to v7.2, you’ll see that the workspaces have been migrated to custom categories in the sidebar. All boards from a workspace are listed under a category of the same name. Boards from direct messages and group messages appear under the default **Boards** category.
  
  Categories are per-user, and can be renamed or deleted by each user after migration. New users won’t have default categories, and boards they join will appear under the default **Boards** category.

  Boards that you create after the migration won’t be linked to a workspace and will always appear under the default **Boards** category unless you move or hide the boards.
  
Drag and drop
-------------

You can move both sidebar categories and boards and change the order of both to suit your preference. You can:

- Set the position of a board within a category.
- Drag a board out of one category and drop it into another category.

To do this, select and hold the cursor over the category or board name. Then move the category or board around as needed. Boards moved into a category are sorted to the top of the category by default unless you specifically position the board before releasing the cursor.

Manage boards on the sidebar
----------------------------

In addition to moving boards to other categories, from the |options-icon| menu next to each board name you can perform the following actions:

- **Delete board**: If you're an admin of the board, you will see an option to delete the board. Deleting the board permanently removes the board from the sidebar of all board members.
- **Duplicate board**: Creates a copy of the board and all the cards on the board. The duplicated board will appear under the same category as the original board. Board members and comments from the original board aren't migrated to the new board.
- **New template from board**: Creates a custom board template of the board and all the cards on the board.
- **Hide board**: Hides the board from your sidebar only. The board will still remain visible on the sidebar for other board members. You can add the board back to your sidebar using the search box (CMD+K/CTRL+K).

Find a board
------------

From the top of the boards left hand sidebar, select the **Find Boards** field (CMD+K/CTRL+K) to open the board switcher, and start typing the name of the board you’re looking for.

Team sidebar
------------

If you’re a member of multiple teams, the team sidebar will appear on the left hand side of Boards. To switch teams, select any of the team icons from the team sidebar.
