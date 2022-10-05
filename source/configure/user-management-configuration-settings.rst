User management configuration settings
======================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Manage your Mattermost users including their access permissions, groups, teams, channels, as well as their access to the System Console. Configure this feature in the System Console by going to **User Management**:

- `Users <#users>`__
- `Groups <#groups>`__
- `Teams <#teams>`__
- `Channels <#channels>`__
- `Permissions <#permissions>`__
- `System roles <#system-roles>`__

----

Users
-----

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+-------------------------------------------------------------+
| View statistics on active users, teams, channels,             | - System Config path: **User Management > Users**           |
| sessions, webhooks, and connections.                          | - ``config.json setting``: N/A                              |
|                                                               | - Environment variable: N/A                                 |
+---------------------------------------------------------------+-------------------------------------------------------------+

----

Groups
------

*Available in legacy Enterprise Edition E20*

+---------------------------------------------------------------+-------------------------------------------------------------+
| View statistics on active users, teams, channels,             | - System Config path: **User Management > Groups**          |
| sessions, webhooks, and connections.                          | - ``config.json setting``: N/A                              |
|                                                               | - Environment variable: N/A                                 |
+---------------------------------------------------------------+-------------------------------------------------------------+

----

Teams
-----

*Available in legacy Enterprise Edition E20*

+---------------------------------------------------------------+-------------------------------------------------------------+
| View statistics on active users, teams, channels,             | - System Config path: **User Management > Teams**           |
| sessions, webhooks, and connections.                          | - ``config.json setting``: N/A                              |
|                                                               | - Environment variable: N/A                                 |
+---------------------------------------------------------------+-------------------------------------------------------------+

----

Channels
--------

*Available in legacy Enterprise Edition E20*

+-------------------------------------------------------------------------+-------------------------------------------------------------+
| Manage active and inactive users, revoke all user sessions,             | - System Config path: **User Management > Channels**        |
| access individual users to view their User ID, add users to other       | - ``config.json setting``: N/A                              |
| teams, and view the teams they are on and what their role is on a team. | - Environment variable: N/A                                 |
+-------------------------------------------------------------------------+-------------------------------------------------------------+
| **Note**: You can search for channels by channel name or by channel ID.                                                               |
+-------------------------------------------------------------------------+-------------------------------------------------------------+

----

Permissions
-----------

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------------+-------------------------------------------------------------+
| Manage default teams and channels by linking AD/LDAP groups         | - System Config path: **User Management > Permissions**     |
| to Mattermost groups.                                               | - ``config.json setting``: N/A                              |
|                                                                     | - Environment variable: N/A                                 |
+---------------------------------------------------------------------+-------------------------------------------------------------+
| See `AD/LDAP groups documentation <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`__ documentation      |
| for more details.                                                                                                                 |
+---------------------------------------------------------------------+-------------------------------------------------------------+

----

System roles
------------

*Available in legacy Enterprise Edition E10/E20*

+----------------------------------------------------------------------+------------------------------------------------------------+
| Manage team settings, including group synchronization for teams.     | - System Config path: **User Management > System Roles**   |
|                                                                      | - ``config.json setting``: N/A                             |
|                                                                      | - Environment variable: N/A                                |
+----------------------------------------------------------------------+------------------------------------------------------------+
| See `additional system admin roles <https://docs.mattermost.com/onboard/system-admin-roles.html>`__ documentation and             |
| `AD/LDAP groups documentation <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`__ documentation          |
| for more details.                                                                                                                 |
+----------------------------------------------------------------------+------------------------------------------------------------+