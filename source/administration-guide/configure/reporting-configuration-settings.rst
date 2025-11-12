Reporting configuration settings
================================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

View the following statistics for your overall deployment and specific teams, as well as access server logs, in the System Console by selecting the **Product** |product-list| menu, selecting **System Console**, and then selecting **Reporting**:

- `Site statistics <#site-statistics>`__
- `Team statistics <#team-statistics>`__
- `Server logs <#server-logs>`__
- `Statistics configuration settings <#statistics-configuration-settings>`__

----

Site statistics
---------------

+----------------------------------------------------------------+---------------------------------------------------------------------+
| View statistics on a wide variety of activities in Mattermost, | - System Config path: **Reporting > Site Statistics**               |
| including: users, seats, teams, channels, posts, calls,        | - ``config.json setting``: N/A                                      |
| sessions, commands, webhooks, websocket and database           | - Environment variable: N/A                                         |
| connections, and collaborative playbooks.                      |                                                                     |
+----------------------------------------------------------------+---------------------------------------------------------------------+

.. note::

  - Bots, deactivated users, and synthetic users in :doc:`Microsoft Teams integrations </end-user-guide/collaborate/collaborate-within-connected-microsoft-teams>` and :doc:`connected workspaces </administration-guide/onboard/connected-workspaces>` users aren't counted towards the total number of activated users. 
  - For billing purposes, activated guest accounts do consume a licensed seat, which is returned when the guest account is deactivated. This means that guest accounts count as a paid user in your Mattermost :doc:`workspace </end-user-guide/end-user-guide-index>`

----

Team statistics
---------------

+---------------------------------------------------------------+----------------------------------------------------------------+
| View statistics per team on number of activated users,        | - System Config path: **Reporting > Team Statistics**          |
| number of public and private channels, total post count, and  | - ``config.json`` setting: N/A                                 |
| count of paid users (self-hosted only).                       | - Environment variable: N/A                                    |
+---------------------------------------------------------------+----------------------------------------------------------------+

.. note::

  Bots, deactivated users, and synthetic users in :doc:`Microsoft Teams integrations </end-user-guide/collaborate/collaborate-within-connected-microsoft-teams>` and :doc:`connected workspaces </administration-guide/onboard/connected-workspaces>` users aren't counted towards the total number of active users.

----

Server logs
-----------

+---------------------------------------------------------------+---------------------------------------------------------------+
| View logging of server-side events.                           | - System Config path: **Reporting > Server Logs**             |
|                                                               | - ``config.json`` setting: N/A                                |
| Reload data, download the ``mattermost.log`` file locally,    | - Environment variable: N/A                                   |
| and view full log event details for any log entry.            |                                                               |
+---------------------------------------------------------------+---------------------------------------------------------------+

.. note::

  - This setting is applicable to self-hosted deployments only.
  - From Mattermost v10.9, you can toggle between JSON and plain text server logs in the System Console when console log output is configured as :ref:`JSON <administration-guide/configure/environment-configuration-settings:output console logs as json>` by specifying the log format as **JSON** or **Plain text**. This option is located in the top right corner of the page **Server logs** page.

----

Statistics configuration settings
---------------------------------

The following self-hosted deployment configuration setting controls statistics collection behavior. This setting is not available in the System Console and can only be set in the ``config.json`` file.

.. config:setting:: maximum-users-for-statistics
  :displayname: Maximum users for statistics (Reporting)
  :systemconsole: N/A
  :configjson: MaxUsersForStatistics
  :environment: N/A
  :description: Sets the maximum number of users on the server before statistics for total messages, total hashtag messages, total file messages, messages per day, and activated users with messages per day are disabled. Default is **2500** users.

Maximum users for statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting is used to maximize performance for large Enterprise deployments and isn't available in the System Console and can only be set in ``config.json``.

+---------------------------------------------------------------+--------------------------------------------------------------------------------+
| Set the maximum number of users on the server before          | - System Config path: N/A                                                      |
| statistics for total messages, total hashtag messages, total  | - ``config.json`` setting: ``"AnalyticsSettings.MaxUsersForStatistics": 2500`` |
| file messages, messages per day, and activated users with     | - Environment variable: N/A                                                    |
| messages per day are disabled.                                |                                                                                |
|                                                               |                                                                                |
| Numerical input. Default is **2500** users.                   |                                                                                |
+---------------------------------------------------------------+--------------------------------------------------------------------------------+
