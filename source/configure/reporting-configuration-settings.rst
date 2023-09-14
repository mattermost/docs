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
| View statistics on activated users, teams, channels, posts,   | - System Config path: **Reporting > Site Statistics**       |
| sessions, commands, webhooks, active users, connections,      | - ``config.json setting``: N/A                              |
| and playbooks.                                                | - Environment variable: N/A                                 |
+---------------------------------------------------------------+-------------------------------------------------------------+
| **Note**: Inactive and deactivated users, as well as remote users in                                                        |
| `Microsoft Teams integrations </channels/collaborate-using-mattermost-for-microsoft-teams.html>`__                          |
| and `shared channels users </onboard/shared-channels.html>`__, aren't counted towards the total number of active users.     |
+---------------------------------------------------------------+-------------------------------------------------------------+

----

Team statistics
---------------

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+---------------------------------------------------------------+
| View statistics per team on number of activated users,        | - System Config path: **Reporting > Team Statistics**         |
| number of public and private channels, total post count, and  | - ``config.json`` setting: N/A                                |
| count of paid users (self-hosted only).                       | - Environment variable: N/A                                   |
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
