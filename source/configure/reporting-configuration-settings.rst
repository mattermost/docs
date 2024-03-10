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

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------+
| View statistics on activated users, teams, channels, posts,   | - System Config path: **Reporting > Site Statistics**       |
| sessions, commands, webhooks, activated users, connections,   | - ``config.json setting``: N/A                              |
| and playbooks.                                                | - Environment variable: N/A                                 |
+---------------------------------------------------------------+-------------------------------------------------------------+
| **Note**: Bots, deactivated users, and synthetic users in                                                                   |
| :doc:`Microsoft Teams integrations </collaborate/collaborate-within-connected-microsoft-teams>`                       |
| and :doc:`shared channels users </onboard/shared-channels>`, aren't counted towards the total number of activated users.  |
+---------------------------------------------------------------+-------------------------------------------------------------+

----

Team statistics
---------------

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+---------------------------------------------------------------+
| View statistics per team on number of activated users,        | - System Config path: **Reporting > Team Statistics**         |
| number of public and private channels, total post count, and  | - ``config.json`` setting: N/A                                |
| count of paid users (self-hosted only).                       | - Environment variable: N/A                                   |
+---------------------------------------------------------------+---------------------------------------------------------------+
| **Note**: Bots, deactivated users, and synthetic users in                                                                     |
| :doc:`Microsoft Teams integrations </collaborate/collaborate-within-connected-microsoft-teams>`                         |
| and :doc:`shared channels users </onboard/shared-channels>`, aren't counted towards the total number of active users.       |
+---------------------------------------------------------------+---------------------------------------------------------------+

----

Server logs
-----------

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+---------------------------------------------------------------+
| View logging of server-side events.                           | - System Config path: **Reporting > Server Logs**             |
|                                                               | - ``config.json`` setting: N/A                                |
|                                                               | - Environment variable: N/A                                   |
+---------------------------------------------------------------+---------------------------------------------------------------+
