Work with cards
===============

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/sign-up
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Our templates provide some default card properties that can be customized or removed. In the Roadmap template, we include **Type** property, whereas in the Project Tasks template, we include an **Estimated Hours** property. These properties are not exclusive to any template and can be easily re-created in any of the templates provided.

Card descriptions
-----------------

Card descriptions can include text with Markdown formatting, checkboxes, and visual elements such as images or GIFs. These images and GIFs are also included in card import and export data.

Customize card properties
-------------------------

Cards can contain different data fields depending on the purpose of the board. For example, in a **Roadmap** board, cards include a **Type** field where you can add categories such as **Bug**, **Triage**, etc. In a **Task** board, cards include the **Estimated Hours** field instead.

Add and manage properties
-------------------------

To create a new property field open a card and select **Add a property**. Then select the type of property from the drop-down menu. The property type specifies the type of data you plan to capture within that field. When you create new card properties, they are added to all new and all existing cards on the current board.

Properties are automatically added to the board filter list at the top of the page, so ensure you customize all property names to make it easy to filter your board by specific properties later. To rename a property, open a card and select the property name to open an editable field. Your changes are saved immediately, and applied across all cards on the current board.

To delete properties you no longer need, select the property, then choose **Delete**. You'll be asked to confirm that you want to remove that property from every card on the current board.

Once you have card properties defined, you have full control over which properties are visible on the board. Select **Properties** at the top of the board, then enable all properties you want to see at a glance, and hide all properties you don't want to see.

Work with property types
~~~~~~~~~~~~~~~~~~~~~~~~

* **Checkboxes** are useful for agenda items that are regularly revisited in weekly sprint or grooming meetings.
* **Multi-select** allows you to create badges to indicate things like status.
* **Numbers** are useful to capture metrics such as task sizing or effort estimates.
* **Person** provides a quick way to capture user assignments. Note that this is not available in Personal Desktop.
* **URL** can be used to provide a link to a pull request or relevant website.
* **Created time/Created by/Last updated time/Last updated by** are good ways order tasks in order of recency.

Card badges
-----------

Card badges are a quick way to view card details without opening up a card. To add them, select **Properties > Comments and Description**. Icons related to the card description, comments, and checkboxes will be displayed on cards with the respective content. Open the card to view the details.

- The description icon indicates that a card has a text description.
- The comment icon displays a number indicating how many comments have been added to a card. When a new comment is added, that number is updated.
- The checkbox icon displays the number of items checked off relative to the total number of checkboxes within the card. When an item is checked off, the icon is automatically updated.

Rename a card property
----------------------

The default name for a new property is the name of the property type (e.g. **Date**, **URL**) and properties are automatically added to the filter list at the top of the board. You can use this to toggle which properties you see displayed on each card preview.

To rename a property field, open up a card and select the property name. Enter the new name in the field provided. The change is saved immediately and applied across all cards.

Mention people
--------------

You can include a team member on a card by `mentioning them on a card <https://docs.mattermost.com/channels/mention-people.html>`__ the same way you would in Channels. The team member you mention will receive a Direct Message notification from the Boards bot with a link to the card you mentioned them on. To mention multiple team members, separate each name with a comma.

Share card previews
-------------------

When you share a link to a card within Mattermost, the card details are automatically displayed in a preview. This preview highlights what the card is about at a glance without having to navigate to it.

Receive updates
---------------

When you create a card, you automatically follow it. You can @mention someone on a card to add them as a follower. This can be a card you've created or someone else's card. Lastly, you can also follow cards manually using the **Follow** option on the top-right corner of a card. To unfollow a card, select **Following**.

When updates are made to a card you're following, you'll receive a Direct Message from the boards bot with a summary of the change (e.g. Bob changed status from **In progress** to **Done**) and a link to the card for more detailed information.

.. note::

  You won't get a notification of your own changes made to a card, even if you're following that card.

Calculations
------------

When you view a board in table, Kanban, or Board view, you can use calculations to answer basic metric questions without needing to create complex reports. Hover over the bottom of a column to display the **Calculate** feature, then select the arrow to open the menu options.

You can use calculations to quickly see:

- How many story points are planned for a release.
- How many tasks have been assigned or not assigned.
- How long has the oldest bug been sitting in the backlog.
- The count of cards where particular properties are empty (useful to make sure important info isn’t missing).
- The sum of estimated developer days for features (to make sure your team isn’t overloaded).
- The range of estimated dates (to make sure your milestones all line up).

The calculation options are detailed below:

* **Count**: Counts the total number of rows in Table view or total number of cards in a column in Board view. Applies to any property type.
* **Count Empty**: Applies to any property type.
  
  - Table View: Counts the total number of empty rows per column selected.
  - Board View: Counts the total number of empty values per property specified within the same column.

* **Count Not Empty**: Applies to any property type.
 
  - Table View: Counts the total number of rows with non-empty cells per column selected.
  - Board View: Counts the total number of non-empty values per property specified within the same column.

* **Percent Empty**: Applies to any property type.

  - Table View: Percentage of empty rows per column selected.
  - Board View: Percentage of empty values per property specified within the same column.

* **Percent Not Empty**: Applies to any property type.

  - Table View: Percentage of rows with non-empty cells per column selected.
  - Board View: Percentage of non-empty values per property specified within the same column.

* **Count Value**: Applies to any property type.

  - Table View: Counts the total number of values within the column (helpful for multi-select properties).
  - Board View: Counts the total number of values per property specified within the same column.

* **Count Unique Values**: Applies to any property type.

  - Table View: Counts the total number of rows with unique values within the column, omitting any duplicates from the count.
  - Board View: Counts the total number of unique values per property specified within the same column, omitting any duplicates from the count.

* **Sum**: The sum of any specified number property within the same column.
* **Average**: The average of any specified number property within the same column.
* **Median**: The median of any specified number property within the same column.
* **Min**: The lowest number of any specified number property within the same column.
* **Max**: The highest number of any specified number property within the same column.
* **Range**: Displays the lowest and highest number. Requires a number property.
* **Earliest Date**: Displays the oldest date. Requires any custom date property or the included "Created time" or "Last updated time".
* **Latest Date**: Displays the most recent date. Requires any custom date property or the included "Created time" or "Last updated time".
* **Date Range**: The difference between the most recent date and oldest date within the same column. In Table View, it is labeled simply as "Range" for any date property/column. Requires any custom date property or the included "Created time" or "Last updated time".
