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

Find users
~~~~~~~~~~

Admins also can narrow down search results by filtering by team or user status

1. select **System Console** from the menu that appears after clicking the dot icon in the upper left corner.
2. Select the **Users** option from the **User Management** menu.
3. Enter the user name in the **Search** field and then choose the proper settings from **Team** and **User Status**.

Active or deactivate users
~~~~~~~~~~~~~~~~~~~~~~~~~~
 
 When necessary, admin can also activate or deactivate people on the channel.
 
1. Select the **User** option under the **User Management** tab.
2. Admin can choose one person from the **Mattermost User** page and then choose the **Member** option.
3. Select **Deactive** user to deactivate and **Activate** user to activate from the dropdown menu under the **Member** option.

Manage user roles
~~~~~~~~~~~~~~~~~~

Admin can change any user's role from admin to member by managing their roles.

1. Select the **Member** option in the **Mattermost User** section.
2. Select **Manage Roles** from the dropdown menu in the **Member** section.
3. Then admin can select the appropriate options

Update team membership
~~~~~~~~~~~~~~~~~~~~~~

1.
2.
3.

Reset user's password
~~~~~~~~~~~~~~~~~~~~~

1.
2.
3.

Update user's email
~~~~~~~~~~~~~~~~~~~~

1.
2.
3.

Revoke user sessions
~~~~~~~~~~~~~~~~~~~~~

1.
2.
3.



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
