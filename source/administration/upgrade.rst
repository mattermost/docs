Upgrading Mattermost Server
===========================

In most cases you can upgrade Mattermost Server in a few minutes, but the upgrade can take longer depending on several factors, including the size and complexity of your installation, and the version that you're upgrading from.

Upgrading to the Latest Version
-------------------------------

If you are upgrading from version 3.0 or later, these instructions apply to you. If you are upgrading from a version earlier than 3.0.0, you must first `upgrade to version 3.0.3 <../administration/upgrading-to-3.0.html>`_.

.. _before-you-begin:

**Before you begin**

Read these instructions carefully from start to finish. Make sure that you understand each step before starting the upgrade. If you have questions or concerns, you can ask on the Mattermost forum at https://forum.mattermost.org/.

.. important::
  Review the :doc:`important-upgrade-notes` to make sure you are aware of any actions you need to take before or after upgrading from your particular version.

You should gather the following information before starting the upgrade:

Existing install directory - *{install-path}*
  If you don't know where Mattermost Server is installed, use the ``whereis platform`` command. The output should be similar to */opt/mattermost/bin/platform*. The install directory is everything before the last occurrence of the string */mattermost*. In this example, the *{install-path}* is ``/opt``.
Location of your local storage directory
  The local storage directory contains all the files that users have attached to their messages. If you don't know its location, open the System Console and go to **Files > Storage** and read the value in **Local Storage Directory**. Relative paths are relative to the ``mattermost`` directory. For example, if the local storage directory is ``./data/`` then the absolute path is ``{install-path}/mattermost/data``.
Owner and group of the install directory - *{owner}* and *{group}*
  Use the ``ls -l {install-path}/mattermost/bin/platform`` command to get the owner and group.

**To upgrade Mattermost Server**:

.. note::
  If you are upgrading an HA cluster, `review these upgrade notes instead <https://docs.mattermost.com/deployment/cluster.html#upgrade-guide>`_.

1. Review the :doc:`important-upgrade-notes` to make sure you are aware of any actions you need to take before or after upgrading from your particular version.

2. In a terminal window on the server that hosts Mattermost Server, change to your home directory. If any, delete files and directories that might still exist from a previous download.

  ``cd ~``

3. Download `the latest version of Mattermost Server <https://about.mattermost.com/download/>`_. In the following command, replace ``X.X.X`` with the version that you want to download:

  Enterprise Edition
    ``wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz``
  Team Edition
    ``wget https://releases.mattermost.com/X.X.X/mattermost-team-X.X.X-linux-amd64.tar.gz``

4. Extract the Mattermost Server files.

  ``tar -xzf mattermost*.gz``

5. Stop Mattermost Server.

  On Ubuntu 14.04 and RHEL 6.6: ``sudo service mattermost stop``

  On Ubuntu 16.04 and RHEL 7.1: ``sudo systemctl stop mattermost``

6. Back up your data and application.
  a. Back up your database using your organization’s standard procedures for backing up MySQL or PostgreSQL.
  b. Back up your application by moving into your archive folder (e.g. ``mattermost-back-YYYY-MM-DD``).

    ``mv {install-path}/mattermost {install-path}/{mattermost-back-YYYY-MM-DD}``

7. Copy the files that you extracted earlier to the install directory.

  ``sudo cp -r mattermost {install-path}``

8. Restore your configuration, local file storage and logs.

  .. code-block:: text

    sudo cp -r {install-path}/{mattermost-back-YYYY-MM-DD}/config {install-path}/mattermost
    sudo cp -r {install-path}/{mattermost-back-YYYY-MM-DD}/data {install-path}/mattermost
    sudo cp -r {install-path}/{mattermost-back-YYYY-MM-DD}/logs {install-path}/mattermost

9. Change ownership of the new files.

  ``sudo chown -R {owner}:{group} {install-path}/mattermost``

10. Start Mattermost server.

  On Ubuntu 14.04 and RHEL 6.6: ``sudo service mattermost start``

  On Ubuntu 16.04 and RHEL 7.1: ``sudo systemctl start mattermost``

11. If you have TLS set up on your Mattermost server, you must activate the CAP_NET_BIND_SERVICE capability to allow the new Mattermost binary to bind to low ports.

  .. code-block:: text

    cd {install-path}/mattermost
    sudo setcap cap_net_bind_service=+ep ./bin/platform

12. Upgrade your ``config.json`` schema:

  a. Open the System Console and change a setting, then revert it. This should enable the Save button for that page.
  b. Click **Save**.
  c. Refresh the page.

  Your current settings are preserved, and new settings are added with default values.

After the server is upgraded, users might need to refresh their browsers to experience any new features.

Upgrading Team Edition to Enterprise Edition
--------------------------------------------

To upgrade from the Team Edition to the Enterprise Edition, follow the normal upgrade instructions above, but make sure that you download the Enterprise Edition in Step 3.

After the Enterprise Edition is running, open the *System Console* and go to **OTHER > Edition and License > License Key** and upload your license key file.
