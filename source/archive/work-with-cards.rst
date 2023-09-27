:nosearch:
:orphan:

Work with cards
===============

.. |options-icon| image:: ../images/dots-horizontal_F01D8.svg
  :alt: Access additional message actions using the More actions icon.

.. |vertical-3-dots| image:: ../images/dots-vertical_F01D9.svg
  :alt: Select the More icon to access additional channel management options.

A card consists of:

- **A set of properties**: Properties are common to all cards in a board. Board views can group cards by “Select” type properties into different columns.
- **A list of comments**: Comments are useful for noting important changes or milestones.
- **A set of content**: The content of a card can consist of Markdown text, checkboxes, and images. Use this to record detailed specs or design decisions for an item for example.

Drag cards from one column to another to change their group-by property. For example, if cards are grouped by “Status” on board view, drag a card to the **Completed** column to mark it as completed. When a board is unsorted, you can drag a card up and down within a column to custom sort your cards.

For sorted boards, dragging a card to a column will auto-sort it using the specified sort settings.

.. note::

  It's not currently possible to move cards between boards. This functionality will be supported in a future release.

Our standard board templates provide some default card properties that can be customized or removed. In the Roadmap template, we include **Type** property, whereas in the Project Tasks template, we include an **Estimated Hours** property. These properties are not exclusive to any template and can be easily re-created in any of the templates provided.

Card descriptions
-----------------

Card descriptions can include text with Markdown formatting, checkboxes, and visual elements such as images or GIFs, and can be separated into blocks of content. To add a description, open a card, select **Add a description** below the **Comments** section, and start typing in your content.

To add a new content block in the description section, hover over the section and select **Add content**. Then choose from any of the following options:

- **Text**: Adds a new text block that can be formatted with Markdown.
- **Image**: Select and embed an image file into the content block. The following image formats are currently supported: GIF, JPEG, and PNG.
- **Divider**: Adds a divider content block below the previous block.
- **Checkbox**: Adds a checkbox content block. Press Enter/Return after typing in content for your checkbox to add another checkbox within the same block. Please note, Markdown formatting isn't supported within the **Checkbox** content block.

To manage the description content blocks on a card, hover over any existing block and select the options menu |options-icon| to move the block up or down, insert a new block above, or delete the current block. Alternatively, you can hover over any existing block, then select and hold the grid button to drag and drop it to a new position within the description section.

Card properties
---------------

Cards can contain different data fields depending on the purpose of the board. Using card properties, you can customize these data fields to fit your needs and track the information most important to you. For example, in a **Roadmap** board, cards include a **Type** field where you can add categories such as **Bug**, **Epic**, etc. In a **Project Task** board, cards include the **Estimated Hours** field instead.

Add properties
--------------

To create a new property field open a card and select **Add a property**. Then select the type of property from the drop-down menu. The property type specifies the type of data you plan to capture within that field. When you create new card properties, they're added to all new and all existing cards on the current board.

Properties are automatically added to the board filter list at the top of the page, so ensure you customize all property names to make it easy to filter your board by specific properties later.

Work with property types
~~~~~~~~~~~~~~~~~~~~~~~~

Boards supports a wide range of fully customizable property types:

- **Text** can be used to add short notes to a card. An advantage of the text property over card descriptions is that it can be `shown on the board <https://docs.mattermost.com/boards/work-with-cards.html#toggle-properties-shown-on-a-board>`_ without needing to open the card.
- **Numbers** are useful to capture metrics such as task sizing or effort estimates. Use in conjunction with calculations to get the most out of the number property type.  
- **Email** and **Phone** can be used to record contact information.
- **URL** can be used to provide a link to a pull request or relevant website. Clicking on the box of a URL property will automatically open the link in a new tab on your browser. Hover over the box to surface options to copy or edit the URL.
- **Select** and **Multi-select** allows you to create a predefined list of options that can be color-coded and displayed as badges on the card to indicate things like status and priority.
- **Dates** are useful to set and track due dates or milestones. Use the date property to make a card appear on the `Calendar view <https://docs.mattermost.com/boards/work-with-views.html#calendar-view>`_. Set a single date or toggle on the **End date** to set a date range.
- **Person** and **Multi-person** provides a quick way to capture user assignments. Note that this is not available in Personal Desktop.
- **Checkbox** is a toggle property that can be used for assigning simple binary options on a card such as True/False or Yes/No.
- **Created time/Created by/Last updated time/Last updated by** are predefined system properties to help you audit changes on a card. The names of these properties are customizable, but the values are not.

Rename a property
-----------------

The default name for a new property is the name of the property type (e.g. **Date**, **URL**).
To rename a property field, open up a card and select the property name to open an editable field. Enter the new name in the field provided. The change is saved immediately and applied across all cards on the current board.

Change a property type
----------------------

To change a property type, select the property then open the **Type** menu and choose a new property type. You’ll be asked to confirm the change from every card on the current board. Changing the type for an existing property will affect values across all cards on the board and may result in data loss.

Delete a property
-----------------

To delete properties you no longer need, select the property, then choose **Delete**. You’ll be asked to confirm that you want to remove that property from every card on the current board.

.. note:: 
  
  Properties are displayed in the order they were created and cannot be re-ordered at this time.

Define a "Select" or "Multi-select" property
--------------------------------------------

The options on a **Select** and **Multi-select** property type appear as color-coded tags on a card. To add and configure the options on these types:

1. Select a card to open the card view.
2. Add a new property, give it a name, and set its type to **Select** (or **Multi-Select**).
3. Select the field box for the property, and start typing the name of a new option. Press Enter to accept. Repeat this step to add additional options.

- To assign a color to or delete an option, select the value and select the options menu **(...)** next to each option name.
- To select an option on the property, select the box and choose one of the values from the menu.
- To remove an option on the property, select the box and chooose the `X` next to the option name you want to remove.

Alternatively, you can also add new options directly from a board:

1. Open a board view.
2. Group by a **Select** property.
3. Scroll to the right of the board and select **+ Add a group**.

This will add a new column, which corresponds to a new value option for the Select property.

.. note:: 
  
  Options in a **Select** or **Multi-Select** property list are sorted in the order they were created and cannot be re-ordered or renamed at this time.

Toggle properties shown on a board
----------------------------------

Once you have card properties defined, you have full control over which properties are shown on the board as a preview without having to open the card. Select **Properties** at the top of the board, then enable all properties you want to see at a glance, and hide all properties you don’t want to see.

Attach files
------------

From Mattermost v7.7 you can attach files to your cards, which other board members can download. There are no limitations to the file types that you can upload.

To upload a file to a card, select **Attach** in the top-right corner of the card. Then select the file you'd like to upload. When your file has been uploaded, you can find it in the **Attachments** section of the card. Select the **+** sign to add additional files to your card.

To delete a file, hover over it and select the |vertical-3-dots| menu. Then select **Delete**. To download the file, select the download icon.

Card badges
-----------

Card badges are a quick way to view card details without opening up a card. To add them, select **Properties > Comments and Description**. Icons related to the card description, comments, and checkboxes will be displayed on cards with the respective content. Open the card to view the details.

- The description icon indicates that a card has a text description.
- The comment icon displays a number indicating how many comments have been added to a card. When a new comment is added, that number is updated.
- The checkbox icon displays the number of items checked off relative to the total number of checkboxes within the card. When an item is checked off, the icon is automatically updated.

Comment on a card
-----------------

Comments allow you to provide feedback and ask questions relevant to the specific work item on the card.

To add a comment, select a card to open the card view, then click on **Add a comment…** to type in your comment, and press **Send** to save the comment to the card. All team members who are `following the card </boards/work-with-cards.html#receive-updates>`_ will receive a notification with a preview of your comment in Mattermost.

From Mattermost Boards v7.4, only board members with the *Commenter* role or higher can comment on a card. Board members assigned the *Viewer* role can view, but not comment on, a card.

Mention people
--------------

You can include a team member on a card by `mentioning them on a card </collaborate/mention-people.html>`__ the same way you would in a message or thread. Mentions are supported in the `Comments </boards/work-with-cards.html#comment-on-a-card>`_ and `Description </boards/work-with-cards.html#card-descriptions>`_ sections within a card. The team member you mention will receive a direct message notification from the boards bot with a link to the card you mentioned them on. To mention multiple team members, separate each name with a comma.

Receive updates
---------------

When you create a card, you automatically follow it. You can @mention someone on a card to add them as a follower. This can be a card you've created or someone else's card. Lastly, you can also follow cards manually using the **Follow** option on the top-right corner of a card. To unfollow a card, select **Following**.

When updates are made to a card you're following, you'll receive a direct message from the boards bot with a summary of the change (e.g. Bob changed status from **In progress** to **Done**) and a link to the card for more detailed information.

.. note::

  You won't get a notification of your own changes made to a card, even if you're following that card.
  
Search cards
------------

You can search through all the cards on a board to find what you’re looking for. Open the board you want to search, then select the **Search cards** field in the top-right of the board.

Card templates
--------------

Card templates can help reduce repetitive manual input for similar types of work items. Each board can have any number of card templates. To create a new card template:

1. Open the board where you want to add the card template.
2. Select the drop-down arrow next to **New**, then select **New template**.
3. Add a title to the card template.
4. Then assign values to any properties and add a description you wish to have pre-populated when a card is created from the template.
5. Close the card using the **X** in the top left corner.
6. Select the drop-down arrow next to **New**, then select the template you just created. 

Alternatively, you can turn any existing card into a template:

1. Open the card you want to use as a template.
2. Select the options menu |options-icon| in the top-right corner of the card.
3. Select **New template from card**.
4. Edit the card as needed, including a helpful name.
5. Close the card using the **X** in the top left corner.
6. Select the drop-down arrow next to **New**, then select the template you just created.

To set a default card template for all new cards created on the board:

1. Select the drop-down arrow next to **New**.
2. Open the options menu |options-icon| next to the card template of your choosing.
3. Select **Set as default**.

.. note:: 
  
  The card template is applicable only to the board in which it’s created and isn’t available in other boards in your team workspace. Comments on a template don't get populated on to new cards. Additionally, properties can't be hidden from a card template at this time. All cards on a board share the same properties, so adding or deleting a property on a template will also apply to all cards on a board.
