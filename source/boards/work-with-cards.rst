Work with Cards
===============

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

Cards can have different configuration fields, depending on the type of board you've selected. For example, in a Roadmap board you'll find the cards include an option for **Type** where you can add categories such as Bug, Triage, etc. A Task board doesn't include a Type field, but includes **Status** and **Priority**. All cards have a **New Property** field. For this field, you can select the type from the drop-down menu. It'll then be added to your card.

The default name for a new property is **New Property**. Ensure that you name your property as it's added to the filter list at the top of the board and having all your filters named **New Property** makes it difficult to work out what you're filtering. To rename a property field, open up a card and select **New Property**. Enter the new name in the field provided. The change is saved immediately and applied across all cards.

Mention people
--------------

You can include a team member on a card by `mentioning them on a card <https://docs.mattermost.com/messaging/mentioning-teammates.html>`__ the same way you would in Channels. The team member you mention will receive a Direct Message notification from the Boards bot with a link to the card you mentioned them on. To mention multiple team members, separate each name with a comma.

Share card previews
-------------------

When you share a link to a card within Mattermost, the card details are automatically displayed in a preview. This preview highlights what the card is about at a glance without having to navigate to it.

Customize card properties
-------------------------

Cards can contain different data fields depending on the purpose of the board. For example, in a Roadmap board, cards include a Type field where you can add categories such as Bug, Triage, etc. In a Task board, cards include Status and Priority fields instead.

Add and manage properties
-------------------------

To create a new a new property field open a card and select **Add a property**. Then select the type of property from the drop-down menu. The property type specifies the type of data you plan to capture within that field. When you create new card properties, they are added to all new and all existing cards on the current board.

Properties are automatically added to the board filter list at the top of the page, so ensure you customize all property names to make it easy to filter your board by specific properties later. You can rename a property at any time by opening a card, then selecting **New Property**. Your changes are saved immediately, and applied across all cards on the current board.

To delete properties you no longer need, select the property, then choose Delete. You'll be asked to confirm that you want to removes that property from every card on the current board.

Once you have card properties defined, you have full control over which properties are visible on the board. Select **Properties** at the top of the board, then enable all properties you want to see at a glance, and hide all properties you don't want to see.

Work with property types
~~~~~~~~~~~~~~~~~~~~~~~~

* **Checkboxes** are useful for agenda items that are regularly revisited in weekly sprint or grooming meetings.
* **Multi-select** allows you to create badges to indicate things like status.
* **Numbers** are useful to capture metrics such as task sizing or effort estimates.
* **Person** provides a quick way to capture user assignments.
* **URL** can be used to provide a link to a pull request or relevant website.
* **Created time/Created by/Last updated time/Last updated by** are good ways order tasks in order of recency.

Calculations
------------

When you view a board in table view, you can use calculations to answer basic metric questions without needing to create complex reports. Hover over the bottom of a column to display the **Calculate** feature, then select the arrow to open the menu options.

You can use calculations to quickly see:

- How many story points are planned for a release.
- How many tasks have been assigned or not assigned.
- How long has the oldest bug been sitting in the backlog.
- The count of cards where particular properties are empty (useful to make sure important info isn’t missing)
- The sum of estimated developer days for features (to make sure your team isn’t overloaded), and
- The range of estimated dates (to make sure your milestones all line up)

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
