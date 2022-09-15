Work with boards
================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Start by selecting the type of board you want to use. A board contains cards, which typically track tasks or topics, and views, which define how to display the cards, or a subset of them. Views can display cards in a board, table, calendar, or gallery layout, optionally filtered and grouped by a property (e.g., priority, status, etc).

Adding new boards
-----------------

To add a new board, select the **+** icon at the top of the sidebar to open the template picker, then select a template or blank board.

Board details
~~~~~~~~~~~~~

To name or rename a board, select the title area to edit it.

To display board description, hover above the board’s title and select show description to activate the show/hide toggle. Once the description field is displayed, select **Add a description** right below the board title to add or edit the description.

Boards and cards are created with random icons by default. To change or remove icons, select the icon then choose the appropriate action.

All changes you make to boards and cards are saved immediately.

Choose a board template
-----------------------

Templates provide you with a predefined structure so that you can get started quickly. Each template has a different function, but can be customized to suit your use case. When you create a new board from the template picker, select each template’s name to preview it and make sure it suits your requirements. Alternatively, you can create your own board templates.

Board templates
~~~~~~~~~~~~~~~

Standard board templates include:

- **Content Calendar**: Plan and organize your content creation and publication schedule.
- **Meeting Agenda**: Use this template for recurring meetings. Queue up items, organize discussions, and plan what to revisit later.
- **Personal Goals**: Categorize and plan your personal goals.
- **Personal Tasks**: Organize your life and track your personal tasks.
- **Project Tasks**: Stay on top of your project tasks, track progress, and set priorities.
- **Roadmap**: Plan your roadmap and manage your releases more efficiently.
- **Welcome to Boards!**: Onboarding template with guided tour points to help you quickly ramp up on Boards.

Create a blank board
~~~~~~~~~~~~~~~~~~~~

If none of the available templates suit your requirements, you can create a blank board using the **Create empty board** option from the template picker.

Create a new template
~~~~~~~~~~~~~~~~~~~~~

To create a new board template select the **+** icon at the top of the sidebar to open the template picker, then select **+ New template**.

To turn an existing board into a template, hover over the board title in the sidebar. Select the options menu **(…)**, then select **New template from board**.

Share a custom board template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From Mattermost Boards v7.2 or later
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Custom templates support permissions control, and are restricted to only the template creator by default. The template creator is an admin of the template and can make the template accessible to everyone on the team via the **Share** button on the template editor, and then setting the team role as **Viewer**. All members of the team will now be able to see and select the template from the template picker.

The admin of the template can also grant specific team members elevated permissions to the template and/or limit access to only select team members by setting the team role as **None** and adding individual members to the template. Individual team members can be assigned the following roles on a template:

<add table>

Prior to Mattermost Boards v7.2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Boards and templates are channel-specific so whichever channel you create your board or template in, is where you’ll find it. If you’d like to re-use a board as a template on another channel workspace, you can export it and then import the archive file in the channel of your choosing.

To do this, select the **…** in the toolbar at the top of the board. Then select **Export** board archive. Download the archive file. Navigate to the channel where you’d like to add the exported board. Select the gear icon next to your profile avatar, then choose Import archive. The board you created will be added to this channel.

Edit board templates
--------------------

Custom templates are fully editable, but standard templates cannot be edited or deleted. To open the template editor for a specific template, go to the template picker then hover over the custom template and click on the pencil icon. Any changes made on the template editor will be automatically saved and visible to team members who have access to the template.

From Mattermost Boards v7.2 or later
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only admins and editors of a custom template can edit the template. If you do not see the Pencil icon when hovering over the template, then you do not have the appropriate permissions to edit the template.

Prior to Mattermost Boards v7.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Any member of the channel workspace can edit a custom template in the channel. To limit access to the template, create or export the template to a private channel.
