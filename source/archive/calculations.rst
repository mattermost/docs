:nosearch:
:orphan:

Work with calculations
======================

When you view a board in table or board view, you can use calculations to answer basic metric questions without needing to create complex reports. Hover over the bottom of a column to display the **Calculate** feature, then select the arrow to open the menu options.

You can use calculations to quickly see:

- How many story points are planned for a release.
- How many tasks have been assigned or not assigned.
- How long has the oldest bug been sitting in the backlog.
- The count of cards where particular properties are empty (useful to make sure important info isn’t missing).
- The sum of estimated developer days for features (to make sure your team isn’t overloaded).
- The range of estimated dates (to make sure your milestones all line up).

The calculation options are:

* **Count**: Counts the total number of rows in table view or total number of cards in a column in Board view. Applies to any property type.
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
* **Date Range**: The difference between the most recent date and oldest date within the same column. In Table View, it's labeled simply as "Range" for any date property/column. Requires any custom date property or the included "Created time" or "Last updated time".
