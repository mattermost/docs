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

+----------------------------------------------------------------+---------------------------------------------------------------------+
| View statistics on a wide variety of activities in Mattermost, | - System Config path: **Reporting > Site Statistics**               |
| including: users, seats, teams, channels, posts, calls,        | - ``config.json setting``: N/A                                      |
| sessions, commands, webhooks, websocket and database           | - Environment variable: N/A                                         |
| connections, and collaborative playbooks,                      |                                                                     |
+----------------------------------------------------------------+---------------------------------------------------------------------+
| **Notes**:                                                                                                                           |
|                                                                                                                                      |
| - Bots, deactivated users, and synthetic users in                                                                                    |
|   :doc:`Microsoft Teams integrations </collaborate/collaborate-within-connected-microsoft-teams>`                                    |
|   and :doc:`connected workspaces </onboard/connected-workspaces>` users aren't counted towards the total number of activated users.  |
| - For billing purposes, activated guest accounts do consume a licensed seat, which is returned when the guest account is             |
|   deactivated. This means that guest accounts count as a paid user in your Mattermost                                                |
|   :doc:`workspace </guides/use-mattermost>`.                                                                                         |
+---------------------------------------------------------------+----------------------------------------------------------------------+

----

Team statistics
---------------

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+----------------------------------------------------------------+
| View statistics per team on number of activated users,        | - System Config path: **Reporting > Team Statistics**          |
| number of public and private channels, total post count, and  | - ``config.json`` setting: N/A                                 |
| count of paid users (self-hosted only).                       | - Environment variable: N/A                                    |
+---------------------------------------------------------------+----------------------------------------------------------------+
| **Note**: Bots, deactivated users, and synthetic users in                                                                      |
| :doc:`Microsoft Teams integrations </collaborate/collaborate-within-connected-microsoft-teams>`                                |
| and :doc:`connected workspaces </onboard/connected-workspaces>` users aren't counted towards the total number of active users. |
+---------------------------------------------------------------+----------------------------------------------------------------+

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
| Reload data, download the ``mattermost.log`` file locally,    | - Environment variable: N/A                                   |
| and view full log event details for any log entry.            |                                                               |
+---------------------------------------------------------------+---------------------------------------------------------------+
