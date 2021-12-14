Working with Boards
===================

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Adding new Boards
-----------------

Using Boards begins with selecting the type of board you want to use. A board contains cards, which typically track tasks or topics, and views, which define how to display the cards, or a subset of them. Views can display cards in a board, table, or gallery layout, optionally filtered and grouped by a property (e.g., priority, status, etc).

* To add a new board, select **+ Add Board** in the bottom left corner of the screen. 
* To rename a board, select the title area to edit it.
* To display the board description, hover over the board's name to activate the **show**/**hide** toggle.
* Boards and cards are created with random icons by default. To change or remove icons, select the icon then choose the appropriate action.

Select the headers to sort them or insert new properties.

All changes you make to boards and cards are saved immediately.

Changing views
--------------

You can change boards views to adjust how your cards are represented. To add a new view to a board, select the menu next to the current view name. Scroll down and select **+ Add view**, then select the new visualization you'd like to use.

Board view
~~~~~~~~~~

This is a vertical list view where cards are sorted by columns. The column names are editable and you can drag cards between columns. Board vie

Calendar view
~~~~~~~~~~~~~

Use Calendar View to organize your cards by date in a calendar grid view. To use this view, cards need to have the **Date** property added. If cards don't have that property, they'll be sorted and displayed by the card creation time. 

Table view
~~~~~~~~~~

Each column corresponds to a card property. You can edit cells directly or you can select **Open** to open the card editor for that row. All changes you make to boards and cards are saved immediately.

For this exercise, select the **Project Tasks** template. The first view of the new board is a table of all tasks.

* Select **By Status** in the sidebar to see a board view.
* Select **Properties** and enable **Priority** and **Date created** to add those properties to the card display.
* You can also change the **Group By**, **Filter**, and **Sort** settings of the view.

Adding cards
------------

Select **New** to add a new card to a board.

Editing cards 
-------------

Select a card to edit it. A card consists of:

* **A set of properties:** Properties are common to all cards in a board. Board views can group cards by “Select” type properties into different columns.
* **A list of comments:** Comments are useful for noting important changes or milestones.
* **A set of content:** The content of a card can consist of markdown text and images. Use this to record detailed specs or design decisions for an item for example.

Press ESC or select **X** on the top left corner of a card to close it.

Dragging cards 
--------------

Drag cards from one column to another to change their group-by property. For example, drag a card to the **Completed** column to mark it as completed. When a board is unsorted, you can drag a card to a specific row in a column.

For sorted boards, dragging a card to a column will auto-sort it using the specified sort settings.
