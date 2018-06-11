Advanced Permissions (E10/E20)
===============================

Advanced permissions offers Admins a way to restrict actions in Mattermost to authorized users only. The Mattermost permission system is based on a modified RBAC (role-based access control) architecture and will be rolled out over a number of Mattermost server releases, starting with v5.0. 

.. note::

  This document applies to Mattermost Server version 5.0 and later. For previous versions, see `permission settings  available in the System Console > Policy page <https://docs.mattermost.com/administration/config-settings.html#policy>`_.


.. contents::
  :backlinks: top
  :local:
  
  
Permissions Structure
----------------------


  

System Scheme (E10)
~~~~~~~~~~~~~~~~~~~

*Available in Enterprise Edition E10 and higher.*


Team Override Scheme (E20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in Enterprise Edition E20*

Channel Permissions (E20)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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






