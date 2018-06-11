Advanced Permissions (E10/E20)
===============================

Advanced permissions offers Admins a way to restrict actions in Mattermost to authorized users only. The Mattermost permission system is based on a modified RBAC (role-based access control) architecture and will be rolled out over a number of server releases, starting with Mattermost server v5.0. 

.. note::

  This document applies to Mattermost Server version 5.0 and later. For previous versions, see `permission settings  available in the System Console > Policy page <https://docs.mattermost.com/administration/config-settings.html#policy>`_.


.. contents::
  :backlinks: top
  :local:
  
  
Permissions Structure
----------------------

Mattermost user interface surfaces a number of elements for Admins to control the permissions in their system.
  

System Scheme (E10)
~~~~~~~~~~~~~~~~~~~~~

*Available in Enterprise Edition E10 and higher.*

Set the default permissions granted to System Admins, Team Admins, Channel Admins and all other members. The permissions granted in the System Scheme apply system-wide, meaning:

- Team Admins: permissions granted apply to all Team Admins, in all teams.
- Channel Admins: permissions granted apply to all Channel Admins in all channels, in all teams.
- All members: permissions granted apply to all members, including Admins, in all channels, in all teams. 

To override the System Scheme default permissions in a specific team, you must set up a Team Override Scheme.

.. image:: ../images/system-scheme.png

Team Override Scheme (E20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in Enterprise Edition E20*

Channel Override Permissions (E20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
*Available in a future release of Enterprise Edition E20*

Allow Admins to restrict permissions within specific channels. Permissions under consideration for this phase include:

- **Read-only Channels:** The ability for Admins to turn off posting in specified channels.
- **Restrict Channel Mentions:** Turn off the ability for users to post channel wide mentions (@-all/channel/here) in specified channels.
- **Channel member management:** Restricting adding and removing channel members to Admins only in specified channels.

Supplementary Roles (E20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
*Available in a future release of Enterprise Edition E20*

Allow Admins to grant additional permissions to specific users or to a group of users based on AD/LDAP group membership. Permissions can be granted within the scope of channels, teams or system level.

Recipes
--------

Glossary
----------

- Inherited: 
- Permission: The ability to execute certain actions. Permissions are granted to roles.
- Roles: A set of permissions. Users or groups are assigned to roles.
- Default Roles: System Admin, Team Admin, Channel Admin, Member.
- System Scheme: A set of default roles that apply system wide
- Team Scheme: A set of default roles that apply only in the team specified. The permissions granted to the roles in a team scheme override role permissions of a system scheme.
- System Wide: Applies across the entire system, including all teams of which the user is a member.
- Team Wide: Applies in a specific team only.
- Group: A set of users, usually synced from AD/LDAP. Groups are assigned to roles.








