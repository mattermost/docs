Important Upgrade Notes
=======================

.. important::
   API version 3 is scheduled for removal on January 16th, 2018. See `api.mattermost.com <https://api.mattermost.com/#tag/APIv3-Deprecation>`_ to learn more.

+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| If you’re upgrading from a version earlier than... | Then...                                                                                                                                                      |
+====================================================+==============================================================================================================================================================+
| v4.0.0                                             | (High Availability Only)                                                                                                                                     |
|                                                    |                                                                                                                                                              |
|                                                    | You must manually add new items to the *ClusterSettings* section of your existing ``config.json``.                                                           |
|                                                    | See the *Upgrading to Version 4.0 and Later* section of :doc:`../deployment/cluster` for details.                                                            |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v3.9.0                                             | Old email invitation links, password reset links, and email verification links will no longer work due to a security change.                                 |
|                                                    | Team invite links copied from the Team Invite Link dialog are not affected and are still valid.                                                              |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v3.8.0                                             | A change is required in the proxy configuration.                                                                                                             |
|                                                    | If you’re using NGINX:                                                                                                                                       |
|                                                    |   1. Open the NGINX configuration file as root. The file is usually ``/etc/nginx/sites-available/mattermost`` but might be different on your system.         |
|                                                    |   2. Locate the line: ``location /api/v3/users/websocket {``                                                                                                 |
|                                                    |   3. Replace the line with ``location ~ /api/v[0-9]+/(users/)?websocket$ {``                                                                                 |
|                                                    | If you are using a proxy other than NGINX, make the equivalent change to that proxy's configuration.                                                         |
|                                                    +--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                    | You need to verify settings in the System Console due to a security-related change.                                                                          |
|                                                    |                                                                                                                                                              |
|                                                    |   1. Go to the the GENERAL section of the System Console                                                                                                     |
|                                                    |   2. Click **Logging**                                                                                                                                       |
|                                                    |   3. Make sure that the **File Log Directory** field is either empty or has a directory path only.It must not have a filename as part of the path.           |
|                                                    +--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                    | Backwards compatibility with the old CLI tool was removed. If you have any scripts that rely on the old CLI, they must be revised to use the                 |
|                                                    | `new CLI  <../administration/command-line-tools.html>`_.                                                                                                     |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v3.6.0                                             | Update the maximum number of files that can be open.                                                                                                         |
|                                                    |                                                                                                                                                              |
|                                                    | On RHEL6 and Ubuntu 14.04:                                                                                                                                   |
|                                                    |   - Verify that the line ``limit nofile 50000 50000`` is included in the ``/etc/init/mattermost.conf`` file.                                                 |
|                                                    | On RHEL7 and Ubuntu 16.04:                                                                                                                                   |
|                                                    |   - Verify that the line ``LimitNOFILE=49152`` is included in the ``/etc/systemd/system/mattermost.service`` file.                                           |
|                                                    +--------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                    | (Enterprise Only)                                                                                                                                            |
|                                                    |                                                                                                                                                              |
|                                                    | Previous ``config.json`` values for restricting public and private channel management will be used as the default values for new settings for restricting    |
|                                                    | private and public channel creation and deletion.                                                                                                            |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| v3.4.0                                             | If public links are enabled, existing public links will no longer be valid. This is because in earlier versions, existing public links were not invalidated  |
|                                                    | when the Public Link Salt was regenerated. You must update any place where you have published these links.                                                   |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
