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
| Manage active and inactive users, revoke all user sessions,   | - System Config path: **User Management > Users**           |
| access individual users to view their User ID, add users      | - ``config.json setting``: N/A                              |
| to other teams, and view the teams they are on and what       | - Environment variable: N/A                                 |
| their role is on a team.                                      |                                                             |
+---------------------------------------------------------------+-------------------------------------------------------------+

There are a lot of things that an Admin can do.

Find users
~~~~~~~~~~

admins also can narrow down search results by filtering by team or user status
by selecting System Console > User Management > User, system administrators can access the User option and search for any user or team member by choosing the required parameters.


----

Groups
------

*Available in legacy Enterprise Edition E20*

+---------------------------------------------------------------+-------------------------------------------------------------+
| Manage default teams and channels by linking AD/LDAP groups   | - System Config path: **User Management > Groups**          |
| to Mattermost groups.                                         | - ``config.json setting``: N/A                              |
|                                                               | - Environment variable: N/A                                 |
+---------------------------------------------------------------+-------------------------------------------------------------+
| See the `AD/LDAP groups </onboard/ad-ldap-groups-synchronization.html>`__ documentation for                                 |
| details.                                                                                                                    |
+---------------------------------------------------------------+-------------------------------------------------------------+

----

Teams
-----

*Available in legacy Enterprise Edition E20*

+---------------------------------------------------------------+-------------------------------------------------------------+
| Manage team settings, including group synchronization for     | - System Config path: **User Management > Teams**           |
| teams.                                                        | - ``config.json setting``: N/A                              |
|                                                               | - Environment variable: N/A                                 |
+---------------------------------------------------------------+-------------------------------------------------------------+
| See the `using AD/LDAP synchronized groups to manage team or private channel membership                                     |
| </onboard/cloud-groups.html#using-ad-ldap-group-synchronization>`__ documentation for details.                              |
+---------------------------------------------------------------+-------------------------------------------------------------+

----

Channels
--------

*Available in legacy Enterprise Edition E20*

+-------------------------------------------------------------------------+-------------------------------------------------------------+
| Manage channel settings, including group synchronization on channels.   | - System Config path: **User Management > Channels**        |
|                                                                         | - ``config.json setting``: N/A                              |
|                                                                         | - Environment variable: N/A                                 |
+-------------------------------------------------------------------------+-------------------------------------------------------------+
| Channels can be deleted with all content, including posts in the database, using the `mmctl channel delete                            |
| </manage/mmctl-command-line-tool.html#mmctl-channel-delete>`__ tool.                                                                  |
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
| Restrict actions in Mattermost to authorized users only.            | - System Config path: **User Management > Permissions**     |
|                                                                     | - ``config.json setting``: N/A                              |
|                                                                     | - Environment variable: N/A                                 |
+---------------------------------------------------------------------+-------------------------------------------------------------+
| See `advanced permissions </onboard/advanced-permissions.html>`__ documentation for details                                       |
+---------------------------------------------------------------------+-------------------------------------------------------------+

----

System roles
------------

*Available in legacy Enterprise Edition E10/E20*

+----------------------------------------------------------------------+------------------------------------------------------------+
| Restrict System Console access to authorized users only.             | - System Config path: **User Management > System Roles**   |
|                                                                      | - ``config.json setting``: N/A                             |
|                                                                      | - Environment variable: N/A                                |
+----------------------------------------------------------------------+------------------------------------------------------------+
| See `additional system admin roles </onboard/system-admin-roles.html>`__ documentation for details                                |
+----------------------------------------------------------------------+------------------------------------------------------------+
