Reporting configuration settings
================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

View statistics for your overall deployment and specific teams as well as access server logs by going to **System Console > Reporting**. The following reporting configuration settings are available:

- `Site statistics <#site-statistics>`__
- `Team statistics <#team-statistics>`__
- `Server logs <#server-logs>`__

----

Site statistics
---------------

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+-------------------------------------------------------------+
| View statistics on active users, teams, channels,             | - System Config path: **Reporting > Site Statistics**       |
| sessions, webhooks, and connections.                          | - ``config.json setting``: N/A                              |
|                                                               | - Environment variable: N/A                                 |
+---------------------------------------------------------------+-------------------------------------------------------------+
| **Note**: Inactive and deactivated users are not counted towards the total number of active users.                          |
+---------------------------------------------------------------+-------------------------------------------------------------+

----

Team statistics
---------------

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+---------------------------------------------------------------+
| View statistics per team on number of active users,           | - System Config path: **Reporting > Team Statistics**         |
| as well as public and private channels.                       | - ``config.json`` setting: N/A                                |
|                                                               | - Environment variable: N/A                                   |
+---------------------------------------------------------------+---------------------------------------------------------------+
| **Note**: Inactive and deactivated users are not counted towards the total number of active users.                            |
+---------------------------------------------------------------+---------------------------------------------------------------+

----

Server logs
-----------

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+---------------------------------------------------------------+
| View logging of server-side events.                           | - System Config path: **Reporting > Server Logs**             |
|                                                               | - ``config.json`` setting: N/A                                |
|                                                               | - Environment variable: N/A                                   |
+---------------------------------------------------------------+---------------------------------------------------------------+