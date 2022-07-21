Reporting configuration settings
================================

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

View statistics for your overall deployment and specific teams as well as access server logs by going to **System Console > Reporting**. 

.. include:: common-config-settings-notation.rst
    :start-after: :nosearch:

The following reporting configuration settings are available:

- `Site statistics <#site-statistics>`__
- `Team statistics <#team-statistics>`__
- `Server logs <#server-logs>`__

Site statistics
---------------

|all-plans| |cloud| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+-------------------------------------------------------------+
| View statistics on active users, teams, channels,             | - System Config path: **Reporting > Site Statistics**       |
| sessions, webhooks, and connections.                          | - ``config.json setting``: N/A                              |
|                                                               | - Environment variable: N/A                                 |
+---------------------------------------------------------------+-------------------------------------------------------------+

Team statistics
---------------

|all-plans| |cloud| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+---------------------------------------------------------------+
| View statistics per team on number of active users,           | - System Config path: **Reporting > Team Statistics**         |
| as well as Public and Private channels.                       | - ``config.json`` setting: N/A                                |
|                                                               | - Environment variable: N/A                                   |
+---------------------------------------------------------------+---------------------------------------------------------------+

Server logs
-----------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+---------------------------------------------------------------+
| View logging of server-side events.                           | - System Config path: **Reporting > Server Logs**             |
|                                                               | - ``config.json`` setting: N/A                                |
|                                                               | - Environment variable: N/A                                   |
+---------------------------------------------------------------+---------------------------------------------------------------+