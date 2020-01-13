Advanced Permissions (E10/E20)
===============================

Advanced permissions offers Admins a way to restrict actions in Mattermost to authorized users only. The Mattermost permission system is based on a modified RBAC (role-based access control) architecture and will be rolled out over a number of server releases, starting with Mattermost server v5.0. The permissions interface can be accessed in **System Console** > **User Management** > **Permissions** (or **System Console** > **Advanced Permissions** in versions prior to 5.12).

.. note::

  This document applies to Mattermost Server version 5.0 and later. For previous versions, see `permission settings available in the System Console > Policy page <https://docs.mattermost.com/administration/config-settings.html#policy>`__.


.. contents::
  :backlinks: top
  :local:
  
  
Permissions Structure
----------------------

The Mattermost System Console user interface provides a number of elements for Admins to control the permissions in their system.
  

System Scheme (E10)
~~~~~~~~~~~~~~~~~~~~~

*Available in Enterprise Edition E10 and higher*

You can set the default permissions granted to System Admins, Team Admins, Channel Admins, and all other members. The permissions granted in the System Scheme apply system-wide, meaning:

- **All Members:** Permissions apply to all members, including Admins, in all channels, in all teams. 
- **Channel Administrators:** Permissions apply to all Channel Admins in all channels, in all teams.
- **Team Administrators:** Permissions apply to all Team Admins, in all teams.
- **Guests:** Permissions granted to users with the Guest role, in all channels and teams. 

To override the System Scheme default permissions in a specific team, you must set up a Team Override Scheme.

**System Scheme Interface** 

The interface for editing permissions in the System Scheme, with panels for Guests, All Members, Channel Administrators, Team Administrators, and System Administrators is available in **System Console > User Management > Permissions > System Scheme** (or **System Console > Advanced Permissions > System Scheme** in versions prior to 5.12).

.. image:: ../images/system-scheme.png

Team Override Schemes (E20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in Enterprise Edition E20*

Using these permissions overrides the default System Scheme permissions in specific teams for All Members, Channel Adminstrators, and Team Administrators. 

- The permissions granted in a Team Override Scheme apply only in the teams which are assigned to the scheme. 
- The System Scheme does not apply to teams that are added to a Team Override Scheme.
- Teams can only belong to one Team Override Scheme.

**Team Override Schemes Interface** 

The interface for naming, assigning teams, and editing permissions in a Team Override Scheme, with panels for All Members, Channel Administrators, and Team Administrators is available in **System Console > User Management > Permissions > Team Override Schemes** (or **System Console > Advanced Permissions > Permissions Schemes > Team Override Scheme** in versions prior to 5.12).

.. image:: ../images/team-scheme.png

Channel Override Permissions (E20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in a future release of Enterprise Edition E20*

Allows Admins to restrict permissions within specific channels. Permissions under consideration for this phase include:

- **Read-only Channels:** The ability for Admins to turn off posting in specified channels.
- **Restrict Channel Mentions:** Turn off the ability for users to post channel wide mentions (@-all/channel/here) in specified channels.
- **Channel member management:** Restricting adding and removing channel members to Admins only in specified channels.

Supplementary Roles (E20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in a future release of Enterprise Edition E20*

Allows Admins to grant additional permissions to specific users or to a group of users based on AD/LDAP group membership. Permissions can be granted within the scope of channels, teams or system level.

Recipes
--------
This section provides some examples of common permissions use cases and how to accomplish them using the **Advanced Permissions System Console interface**.

Team Management
~~~~~~~~~~~~~~~~

**Only allow Admins, in specific team, to add members**
Example: In Team A, only allow Team and System Admins to add new team members. As the default for all other teams, allow all users to add and invite new members.

1. Navigate to **System Console** > **User Management** > **Permissions** (or **System Console** > **Advanced Permissions** in versions prior to 5.12)
2. Select **Edit Scheme**.
3. In the **All Members > Teams** panel, check the box for **Add Team Members**. This sets the system default for all teams.
4. Choose **Save**. 
5. Select the back arrow to return to the **Permission Schemes** menu. 

1. Seect **New Team Override Scheme**.
  i. Name and describe the scheme. For example, ``Authorized Personnel Only`` with description ``Restrict adding team members to Team and System Admins.``
  ii. Add Team B to the **Select teams to override permissions** list.
  iii. In the **All Members** panel, uncheck the box for **Add Team Members**.
  iv. In the **Channel Administrator** and **Team Administrator** panels, check the box for **Add Team Members**. 
2. Choose **Save**. 
3. Select the back arrow to return to the **Permission Schemes** menu. 


Public and Private Channel Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Restrict who can rename channels and edit channel header and purposes**
Example: As the default for the entire system, restrict renaming channels and editing headers and purposes to Admins only.

1. Navigate to **System Console** > **User Management** > **Permissions** (or **System Console** > **Advanced Permissions** in versions prior to 5.12).
2. Select **Edit Scheme**.
3. In the **All Members** panel, uncheck the box for **Manage Public Channels > Manage Channel Settings**.
4. In the **Channel Administrator** and **Team Administrator** panels, check the box for **Manage Public Channels > Manage Channel Settings**.

.. note::

  Permissions for channel renaming, editing header, and editing purpose are currently grouped in a single permission. These will be split into separate permissions in a future release.

**Restrict who can create channels, in specific teams**
Example: In Team C, restrict public channel creation to Admins. As the default for all other teams, allow everyone to create public channels.

1. Navigate to **System Console** > **User Management** > **Permissions** (or **System Console** > **Advanced Permissions** in versions prior to 5.12).
2. Select **Edit Scheme**.
3. In the **All Members** panel, check the box for **Create Channels** in the **Manage Public Channels** section. This sets the system default to allow creation of public channels on all teams.
4. In **System Console** > **Advanced Permissions** in prior versions or **System Console** > **User Management** > **Permissions** in versions after 5.12, create a new **Team Override Scheme**.
  i. Name and describe the scheme. For example, ``Contractor Scheme`` with description ``Restrict public channel creation to Admins only``.
  ii. Add Team C to the **Select teams to override permissions** list.
  iii. In the **All Members** panel, uncheck the box for **Create Channels** in the **Manage Public Channels** section.
  iv. In the **Channel Administrator** and **Team Administrator** panels, check the box for **Create Channels** in the **Manage Public Channels** section.

Post Management
~~~~~~~~~~~~~~~~

**Restrict who can delete posts**
Example: As the default for the entire system, restrict deleting posts to only Team and System Admins.

1. Navigate to **System Console** > **User Management** > **Permissions** (or **System Console** > **Advanced Permissions** in versions prior to 5.12).
2. Select **Edit Scheme**.
3. In the **All Members** and **Channel Admin** panels, uncheck the boxes for **Delete Own Posts** and **Delete Others Posts**.
4. In the **Channel Administrator** and **Team Administrator** panels, check the box boxes for **Delete Own Posts** and **Delete Others Posts**.

**Restrict who can edit posts**
Example: As the default for the entire system, only allow users to edit their own posts for five minutes after posting.

1. Navigate to **System Console** > **User Management** > **Permissions** (or **System Console** > **Advanced Permissions** in versions prior to 5.12).
2. Select **Edit Scheme**.
3. In the **All Members**, **Channel Administrator**, and **Team Administrator** panels, check the box for **Edit Posts**.
4. From any panel, click the gear button to set the global time limit to ``300`` seconds.

.. note::

  The post edit time limit is a `global config variable <https://docs.mattermost.com/administration/config-settings.html#post-edit-time-limit>`__ ``PostEditTimeLimit``, so setting a post edit time limit applies system-wide to all teams and roles.


Integration Management
~~~~~~~~~~~~~~~~~~~~~~~

**Restrict managing webhooks and slash commands**

Example: As the default for the entire system, only allow System Admins to create, edit and delete integrations.

1. Navigate to **System Console** > **User Management** > **Permissions** (or **System Console** > **Advanced Permissions** in versions prior to 5.12).
2. Select **Edit Scheme**.
3. In the **All Members**, **Channel Administrator**, and **Team Administrator** panels uncheck the boxes for **Manage Webhooks** and **Manage Slash Commands**.

.. note::

  Permissions for creating, editing, and deleting integrations are currently grouped for each integration type. These will be split into separate permissions in a future release.

Administration Tools
--------------------

There are a number of CLI tools available for Admins to help in configuring and troubleshooting the permissions system:

1. `Reset to default permissions <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-permissions-reset>`__: Resets all permissions to the default on new installs.
2. `Export permission schemes <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-permissions-export>`__: Exports the System Scheme and any Team Override Schemes to a jsonl file.
3. `Import permission schemes <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-permissions-import>`__: Imports the System Scheme and any Team Override Schemes to your Mattermost instance from a jsonl input file in the format outputted by ``mattermost permissions export``.

Backend Infrastructure
-----------------------

Technical Admins or developers looking for a deeper understanding of the permissions backend can refer to our :doc:`permissions-backend` technical documentation.

Glossary
----------

- **Permission:** The ability to execute certain actions. Permissions are granted to roles.
- **Roles:** A set of permissions. Users or groups are assigned to roles.
- **Group:** A set of users, usually synced from AD/LDAP. Groups are assigned to roles in the context of teams, channels, or system-wide.
- **Default Roles:** All Members, Channel Administrators, Team Administrators, System Administrators.
- **System Scheme:** A set of default roles that apply system-wide.
- **Team Override Scheme:** A set of default roles that apply only in the team specified. Permissions granted to roles in a team scheme override roles in the system scheme.
- **System-wide:** Applies across the entire system, including all teams of which the user is a member.
- **Team-wide:** Applies in a specific team only.
