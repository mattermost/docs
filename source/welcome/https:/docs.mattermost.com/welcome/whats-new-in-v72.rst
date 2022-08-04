What’s new in Mattermost Boards v7.2
=====================================

Mattermost Boards v7.2 will be released in the week of August 15th, and all Cloud plans will be automatically upgraded to the latest version during this time.

Boards is moving from a channel-based to a role-based permissions system. This means that access to individual boards can be controlled on a channel level or a board level, depending on whether a board is linked to a channel or not.

TL;DR
------

1. All the boards you're currently a member of from your current team will appear on the sidebar without needing to switch workspaces.
2. Organize boards on the sidebar with custom categories. 
3. Press Ctrl+K / Cmd+K to find additional boards.
4. Navigate between teams in Boards with the new team switcher.
5. Set board and template permissions in the new **Share** dialog.
6. Link boards to channels to automatically grant board permissions to channel members.

Navigation
----------

Sidebar categories
~~~~~~~~~~~~~~~~~~~

Navigation is simplified, and now works similarly to channels. No more switching between workspaces - and the dashboard page has been removed. All the boards you're currently a member of from your current team will appear on the sidebar without needing to switch workspaces. Use the search box (Ctrl+K / Cmd+K) to find additional boards.

Boards can be organized under custom categories on a per-user level. So, users can organize their boards under categories that make sense to them without impacting the boards or categories for other users. Select the “...” options menu next to a custom category to manage your categories.

Team sidebar
~~~~~~~~~~~~

Boards now supports a team sidebar so you can easily navigate between boards on different teams. If you’re a member of multiple teams, the team sidebar will appear on the left hand side. To switch teams, select any of the team icons from the team sidebar.

Linking boards to channels
--------------------------

The channel header’s board icon is now located on the channel `Apps Bar <https://docs.mattermost.com/configure/configuration-settings.html#enable-apps-bar>`_. When you select the **Boards** icon, you’ll open a new right-hand sidebar (RHS) where channel admins can search and link boards to the channel. To maintain the same organization, all the boards previously associated with the workspace will automatically appear on the RHS post-migration. Select a linked board to navigate directly to the board.

Channel members can search and link boards within the team where they are also board admins. Linking a board to a channel automatically grants all channel members Editor access to the board (see Sharing section below for more details).

.. note:: 
  
  A channel can be linked to multiple boards, but each individual board can only be linked to one channel at a time. Linking the same board to another channel will automatically remove the link from the previous channel.

Channel members can also create a new board from the RHS. Doing so will automatically link the new board to the channel and grant channel members permissions to the board.

Sharing
-------

Select **Share** to view and edit permissions to a board.

Team access
~~~~~~~~~~~

Boards belong to teams, and only members of that team can eithercan be either be granted editor access or no access to the board by default.members of the board (similar to channels).

Roles
~~~~~

In v7.2, there will only be two roles:

- **Admin**: Can modify the board, its contents, and its permissions
- **Editor**: Can modify the board and its contents

In the future, there will be additional roles:

- **Commenter**: Can add comments
- **Viewer**: Can view the board and its contents
Channel role groups
Board Admins can add a channel to a board to grant its members Editor access. To do this, open the Share option, search for the channel, and add it to the board as a user. The default role is Editor. Doing so also links the board back to the channel, where the board will appear on the channel RHS.
CUSTOM TEMPLATES
Custom templates also support permissions control, and are restricted to only the template creatorprivate by default. The template creator is an admin of the template and can make it public so it will be accessible to everyone on the team via the Share button on the template editor, and then setting the team role as Editorvia the template picker.
AUTOMATIC MIGRATION
Instead of being tied to a particular channel, each board has been automatically migrated to use its own access control list. The creator of the original board is set as an admin on the board, with the ability to change the board’s permissions. Other members are granted the new Editor role.
Public channels
If a board or custom template was previously attached to a public channel: It’s now searchable by, and accessible to, any member of that channel’s team, including future members.
Private channels
If a board or custom template was previously attached to a private channel: It will be searchable by, and accessible to, any member of that channel at the time of migration. Future members will need to be added by the admin.
Direct messages (DMs) and group messages (GMs)
If a board or custom template was previously attached to a direct message or group message: It will be searchable by, and accessible to, any member of that channel at the time of migration. Future members will need to be added by the admin. 
For boards previously attached to DMs and GMs whose members are associated with more than one team:
The board will be moved to the first team on the team sidebar where all the board members are current team members.
In the case where some members do not belong to the same team, we will associate the board to the first team where the creator (board admin) has access and where most other board members are current team members.
Please note: These boards may not appear in your search results when switching teams.
Workspaces to categories 
If you belonged to a workspace at the time of migration you’ll see that they’ve been migrated to custom categories in the sidebar. All boards from a workspace are listed under a category of the same name. Boards from direct messages and group messages appear under the default “Boards” category.
Categories are per-user, and can be renamed or deleted by each user after migration. New users won’t have default categories, and boards they join will appear under the default “Boards” category.
Boards that you create after the migration won’t be linked to a workspace. and will always appear under the default "Boards" category unless you move or hide the boards.
Boards linked to channels post-migration will also not appear under their respective workspace categories.



