User management configuration settings
======================================

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 25
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 25
  :target: https://mattermost.com/sign-up
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 25
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Manage your Mattermost users including their access permissions, groups, teams, channels, as well as their access to the System Console. Configure this feature by going to **System Console > User Management**.

.. include:: common-config-settings-notation.rst
    :start-after: :nosearch:

Users
-----

*Available in legacy Enterprise Edition E10/E20*

|all-plans| |cloud| |self-hosted|

+---------------------------------------------------------------+-------------------------------------------------------------+
| View statistics on active users, teams, channels,             | - System Config path: **User Management > Users**           |
| sessions, webhooks, and connections.                          | - ``config.json setting``: N/A                              |
|                                                               | - Environment variable: N/A                                 |
+---------------------------------------------------------------+-------------------------------------------------------------+

Groups
------

|enterprise| |cloud| |self-hosted|

*Available in legacy Enterprise Edition E20*

+---------------------------------------------------------------+-------------------------------------------------------------+
| View statistics on active users, teams, channels,             | - System Config path: **User Management > Groups**          |
| sessions, webhooks, and connections.                          | - ``config.json setting``: N/A                              |
|                                                               | - Environment variable: N/A                                 |
+---------------------------------------------------------------+-------------------------------------------------------------+

Teams
-----

|enterprise| |cloud| |self-hosted|

*Available in legacy Enterprise Edition E20*

+---------------------------------------------------------------+-------------------------------------------------------------+
| View statistics on active users, teams, channels,             | - System Config path: **User Management > Teams**           |
| sessions, webhooks, and connections.                          | - ``config.json setting``: N/A                              |
|                                                               | - Environment variable: N/A                                 |
+---------------------------------------------------------------+-------------------------------------------------------------+

Channels
--------

|enterprise| |cloud| |self-hosted|

*Available in legacy Enterprise Edition E20*

+-------------------------------------------------------------------------+-------------------------------------------------------------+
| Manage active and inactive users, revoke all user sessions,             | - System Config path: **User Management > Channels**        |
| access individual users to view their User ID, add users to other       | - ``config.json setting``: N/A                              |
| teams, and view the teams they are on and what their role is on a team. | - Environment variable: N/A                                 |
+-------------------------------------------------------------------------+-------------------------------------------------------------+
| **Note**: You can search for channels by channel name or by channel ID.                                                               |
+-------------------------------------------------------------------------+-------------------------------------------------------------+

Permissions
-----------

|enterprise| |professional| |cloud| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------------+-------------------------------------------------------------+
| Manage default teams and channels by linking AD/LDAP groups         | - System Config path: **User Management > Permissions**     |
| to Mattermost groups.                                               | - ``config.json setting``: N/A                              |
|                                                                     | - Environment variable: N/A                                 |
+---------------------------------------------------------------------+-------------------------------------------------------------+
| See `AD/LDAP groups documentation <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`__ documentation      |
| for more details.                                                                                                                 |
+---------------------------------------------------------------------+-------------------------------------------------------------+

System roles
------------

|all-plans| |cloud| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+----------------------------------------------------------------------+------------------------------------------------------------+
| Manage team settings, including group synchronization for teams.     | - System Config path: **User Management > System Roles**   |
|                                                                      | - ``config.json setting``: N/A                             |
|                                                                      | - Environment variable: N/A                                |
+----------------------------------------------------------------------+------------------------------------------------------------+
| See `AD/LDAP groups documentation <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`__ documentation      |
| for more details.                                                                                                                 |
+----------------------------------------------------------------------+------------------------------------------------------------+