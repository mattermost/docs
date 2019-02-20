Upgrading Mattermost Server
===========================

In most cases you can upgrade Mattermost Server in a few minutes, but the upgrade can take longer depending on several factors, including the size and complexity of your installation, and the version that you're upgrading from.

Upgrading to the Latest Version
-------------------------------

If you are upgrading from version 3.0 or later, these instructions apply to you. If you are upgrading from a version earlier than 3.0.0, you must first `upgrade to version 3.0.3 <../administration/upgrading-to-3.0.html>`__.

If you have installed Mattermost via a package from your GNU/Linux distribution, please use your package manager or refer to the documentation specific to your distribution instead.

.. _before-you-begin:

**Before you begin**

Read these instructions carefully from start to finish. Make sure that you understand each step before starting the upgrade. If you have questions or concerns, you can ask on the Mattermost forum at https://forum.mattermost.org/.

.. important::
  Review the :doc:`important-upgrade-notes` to make sure you are aware of any actions you need to take before or after upgrading from your particular version.

You should gather the following information before starting the upgrade:

Existing install directory - *<INSTALL_PATH>*
  If you don't know where Mattermost Server is installed, use the ``whereis mattermost`` command. The output should be similar to */opt/mattermost/bin/mattermost*. The install directory is everything before the first occurrence of the string */mattermost*. In this example, the *<INSTALL_PATH>* is ``/opt``.
  If that command does not produce any results because your version is older, try ``whereis platform`` instead.
Location of your local storage directory
  The local storage directory contains all the files that users have attached to their messages. If you don't know its location, open the System Console and go to **Files > Storage** and read the value in **Local Storage Directory**. Relative paths are relative to the ``mattermost`` directory. For example, if the local storage directory is ``./data/`` then the absolute path is ``<INSTALL_PATH>/mattermost/data``.
Owner and group of the install directory - *{owner}* and *{group}*
  Use the ``ls -l <INSTALL_PATH>/mattermost/bin/mattermost`` command to get the owner and group.

**To upgrade Mattermost Server**:

.. note::
  If you are upgrading an HA cluster, `review these upgrade notes instead <https://docs.mattermost.com/deployment/cluster.html#upgrade-guide>`__.

#. Review the :doc:`important-upgrade-notes` to make sure you are aware of any actions you need to take before or after upgrading from your particular version.

**Manually**

#. Connect to the server that hosts your Mattermost instance. Connect under the username that executes Mattermost or under a privileged user authorised to restart services and change files related to Mattermost. Switch to a directory suitable to download the Mattermost package (the home directory or ``/tmp`` are good candidates. If any, delete files and directories that might still exist from a previous download.

#. Download `the latest version of Mattermost Server <https://about.mattermost.com/download/>`__ with either ``wget`` or ``curl`` (depending on your GNU/Linux distribution, one or the other or both tools might be installed). In the following command, replace ``X.X.X`` with the version that you want to download.

   *Enterprise Edition*

   .. code-block:: sh

      https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz

   *Team Edition*

   .. code-block:: sh

      https://releases.mattermost.com/X.X.X/mattermost-team-X.X.X-linux-amd64.tar.gz

#. Create a temporary directory and extract the Mattermost Server files to it. Replace ``<edition>`` and ``X.X.X`` with respectively the edition and version you choose.

   .. code-block:: sh

      # mkdir mattermost-upgrade
      # tar -xf mattermost-<edition>-X.X.X-linux-amd64.tar.gz

#. Stop Mattermost Server.

   On a GNU/Linux distribution using SysVInit as service manager (like on Ubuntu 14.04 and RHEL 6.6), use:

   .. code-block:: sh

      # service mattermost stop

   On a GNU/Linux distributionusing systemd as service manager (like on Ubuntu 16.04 and RHEL 7.1), use:

   .. code-block:: sh

      # systemctl stop mattermost

#. Back up your data and application.

   #. Back up your database using your organization’s standard procedures for backing up MySQL or PostgreSQL.

   #. Back up your application by copying into an archive folder (e.g. ``mattermost-backup-YYYY-MM-DD-HH-mm``).

      .. code-block:: sh

         # cd <INSTALL_PATH>
         # cp -ra mattermost/ mattermost-backup-$(date +'%F-%H-%M')/

#. Remove all files *except special directories* from within the current mattermost directory.

   The special directories within mattermost are ``config``, ``logs``, ``plugins``, and ``data`` (unless you have a different value configured for local storage, as per *Before you begin*). The following command clears the contents of mattermost, preserving only those directories and their contents.
   It is recommandded to modify the second part of the command from ``--delete`` to ``--print`` in order to check which files will be effecively removed.

   .. code-block:: sh

      # find "$mattermostdir" -mindepth 1 -maxdepth 1 -not \( -path "$mattermostdir/config" -o -path "$mattermostdir/logs" -o -path "$mattermostdir/plugins" -o -path "$mattermostdir/data" \) -delete

#. Rename the ``plugins`` directory so they do not interfere with the upgrade.

   .. code-block:: sh

      # mv mattermost/plugins/ mattermost/plugins~

#. Change ownership of the new files before copying them.

   .. code-block:: sh

      # chown -hR {owner}:{group} {path-to}/mattermost-upgrade/

#. Copy the new files to your install directory and remove the temporary files.

   Note that the ``n`` (no-clobber) flag and trailing ``.`` on source are very important.

   .. code-block:: sh

      # cp -an {path-to}/mattermost-upgrade/. mattermost/
      # rm -rf {path-to}/mattermost-upgrade/

#. If your server listens on a port in the range 0 to 1023 (port also called well-known port, system port or privileged port) and your Mattermost instance is not being run as root, you must activate the CAP_NET_BIND_SERVICE Linux namespace capability to allow the new Mattermost binary to bind to that low port.

   .. code-block:: sh

      # cd <INSTALL_PATH>/mattermost
      # setcap cap_net_bind_service=+ep ./bin/mattermost

#. Start Mattermost server.

   On Ubuntu 14.04 and RHEL 6.6:

   .. code-block:: sh

      # service mattermost start

   On a GNU/Linux distributionusing systemd as service manager (like on Ubuntu 16.04 and RHEL 7.1), use:

   .. code-block:: sh

      # systemctl start mattermost

#. Upgrade your ``config.json`` schema:

   #. Open the System Console and change a setting, then revert it. This should enable the Save button for that page.
   #. Click **Save**.
   #. Refresh the page.

   Your current settings are preserved, and new settings are added with default values.

   After the server is upgraded, users might need to refresh their browsers to experience any new features.

#. Reinstate the ``plugins`` directory, then restart the mattermost service.

.. code-block:: sh

   # cd <INSTALL_PATH>/mattermost
   # mv plugins~/ plugins

**With a script**

The tasks described in the manual way described above can be somewhat automated with a simple script. Use it cautiously and don't forget to adapt the parameters described in the first section.

*Preparing the script*

`Save the script <https://docs.mattermost.com/administration/update_mattermost.sh>`__ to your mattermost server.

Make it executable.

.. code-block:: sh

   # chmod +x ./update_mattermost.sh

Please adjust the parameters at the beginning of the script according to your environment.

*Start the script*

To start the update process, start the script and add the desired version number as an argument.

.. code-block:: sh

   # ./update_mattermost.sh <VERSION>

Example:

.. code-block:: sh

   # ./update_mattermost.sh 5.7.1

After the update, the following additional steps are required:

#. Upgrade your ``config.json`` schema:

   #. Open the System Console and change a setting, then revert it. This should enable the Save button for that page.
   #. Click **Save**.
   #. Refresh the page.

   Your current settings are preserved and new settings are added with default values.

After the server is upgraded, users might need to refresh their browsers to experience any new features.

#. If needed, reinstate the ``plugins`` directory and restart the mattermost service.

.. code-block:: sh

   # cd <INSTALL_PATH>/mattermost
   # sudo mv plugins~/ plugins


Upgrading Team Edition to Enterprise Edition
--------------------------------------------

To upgrade from the Team Edition to the Enterprise Edition, follow the normal upgrade instructions above, but make sure that you download the Enterprise Edition in Step 3.

After the Enterprise Edition is running, open the *System Console* and go to **OTHER > Edition and License > License Key** and upload your license key file.
