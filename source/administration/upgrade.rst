Upgrading Mattermost Server
===========================

In most cases you can upgrade Mattermost Server in a few minutes, but the upgrade can take longer depending on several factors, including the size and complexity of your installation, and the version that you're upgrading from.

Upgrading to the Latest Version
-------------------------------

If you are upgrading from version 3.0 or later, these instructions apply to you. If you are upgrading from a version earlier than 3.0.0, you must first `upgrade to version 3.0.3 <../administration/upgrading-to-3.0.html>`__.

.. _before-you-begin:

**Before you begin**

Read these instructions carefully from start to finish. Make sure that you understand each step before starting the upgrade. If you have questions or concerns, you can ask on the Mattermost forum at https://forum.mattermost.org/.

.. important::
  Review the :doc:`important-upgrade-notes` to make sure you are aware of any actions you need to take before or after upgrading from your particular version.

You should gather the following information before starting the upgrade:

Existing install directory - *{install-path}*
  If you don't know where Mattermost Server is installed, use the ``whereis mattermost`` command. The output should be similar to */opt/mattermost/bin/mattermost*. The install directory is everything before the first occurrence of the string */mattermost*. In this example, the *{install-path}* is ``/opt``.
  If that command does not produce any results because your version is older, try ``whereis platform`` instead.
Location of your local storage directory
  The local storage directory contains all the files that users have attached to their messages. If you don't know its location, open the System Console and go to **Files > Storage** and read the value in **Local Storage Directory**. Relative paths are relative to the ``mattermost`` directory. For example, if the local storage directory is ``./data/`` then the absolute path is ``{install-path}/mattermost/data``.
Owner and group of the install directory - *{owner}* and *{group}*
  Use the ``ls -l {install-path}/mattermost/bin/mattermost`` command to get the owner and group.

**To upgrade Mattermost Server**:

.. note::
  If you are upgrading an HA cluster, `review these upgrade notes instead <https://docs.mattermost.com/deployment/cluster.html#upgrade-guide>`__.

#. Review the :doc:`important-upgrade-notes` to make sure you are aware of any actions you need to take before or after upgrading from your particular version.

#. In a terminal window on the server that hosts Mattermost Server, change to your home directory. If any, delete files and directories that might still exist from a previous download.

   .. code-block:: sh

     cd ~

#. Download `the latest version of Mattermost Server <https://about.mattermost.com/download/>`__. In the following command, replace ``X.X.X`` with the version that you want to download:

   *Enterprise Edition*

   .. code-block:: sh

     wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz

   *Team Edition*

   .. code-block:: sh

    wget https://releases.mattermost.com/X.X.X/mattermost-team-X.X.X-linux-amd64.tar.gz

#. Extract the Mattermost Server files.

   .. code-block:: sh

     tar -x --transform='s,^[^/]\+,\0-upgrade,' -f mattermost*.gz
  
   The ``transform`` option adds a suffix to the topmost extracted directory so it does not conflict with the usual install directory.

#. Stop Mattermost Server.

   On Ubuntu 14.04 and RHEL 6.6:

   .. code-block:: sh

     sudo service mattermost stop

   On Ubuntu 16.04 and RHEL 7.1:

   .. code-block:: sh

     sudo systemctl stop mattermost

#. Back up your data and application.

   #. Back up your database using your organization’s standard procedures for backing up MySQL or PostgreSQL.

   #. Back up your application by copying into an archive folder (e.g. ``mattermost-back-YYYY-MM-DD-HH-mm``).

      .. code-block:: sh

        cd {install-path}
        sudo cp -ra mattermost/ mattermost-back-$(date +'%F-%H-%M')/

#. Remove all files *except special directories* from within the current mattermost directory.

   The special directories within mattermost are ``config``, ``logs``, ``plugins``, and ``data`` (unless you have a different value configured for local storage, as per *Before you begin*). The following command clears the contents of mattermost, preserving only those directories and their contents.
   You should first modify the second part of the command to ``xargs echo rm -r`` to verify what will be executed.

   .. code-block:: sh

     sudo find mattermost/ -mindepth 1 -maxdepth 1 \! \( -type d \( -path mattermost/config -o -path mattermost/logs -o -path mattermost/plugins -o -path mattermost/data \) -prune \) | sudo xargs rm -r
    
#. Rename the ``plugins`` directory so they do not interfere with the upgrade.

   .. code-block:: sh

     sudo mv mattermost/plugins/ mattermost/plugins~
    
#. Change ownership of the new files before copying them.

   .. code-block:: sh

     sudo chown -hR {owner}:{group} {path-to}/mattermost-upgrade/

#. Copy the new files to your install directory and remove the temporary files.

   Note that the ``n`` (no-clobber) flag and trailing ``.`` on source are very important.

   .. code-block:: sh

     sudo cp -an {path-to}/mattermost-upgrade/. mattermost/
     sudo rm -rf {path-to}/mattermost-upgrade/

#. Start Mattermost server.

   On Ubuntu 14.04 and RHEL 6.6:

   .. code-block:: sh

     sudo service mattermost start

   On Ubuntu 16.04 and RHEL 7.1:

   .. code-block:: sh

     sudo systemctl start mattermost

#. If you have TLS set up on your Mattermost server, you must activate the CAP_NET_BIND_SERVICE capability to allow the new Mattermost binary to bind to low ports.

   .. code-block:: sh

     cd {install-path}/mattermost
     sudo setcap cap_net_bind_service=+ep ./bin/mattermost

#. Upgrade your ``config.json`` schema:

   #. Open the System Console and change a setting, then revert it. This should enable the Save button for that page.
   #. Click **Save**.
   #. Refresh the page.

   Your current settings are preserved, and new settings are added with default values.

After the server is upgraded, users might need to refresh their browsers to experience any new features.

14. Re-instate the ``plugins`` directory, then restart the mattermost service.

    .. code-block:: sh

      cd {install-path}/mattermost
      sudo mv plugins~/ plugins

Upgrading Team Edition to Enterprise Edition
--------------------------------------------

To upgrade from the Team Edition to the Enterprise Edition, follow the normal upgrade instructions above, but make sure that you download the Enterprise Edition in Step 3.

After the Enterprise Edition is running, open the *System Console* and go to **OTHER > Edition and License > License Key** and upload your license key file.
