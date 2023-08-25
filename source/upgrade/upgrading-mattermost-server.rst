Upgrade Mattermost Server
=========================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

In most cases, you can upgrade Mattermost Server in a few minutes. However, the upgrade can take longer depending on several factors, including the size and complexity of your installation, and the version that you're upgrading from.

.. _before-you-begin:

Before you begin
----------------

**Read these instructions carefully from start to finish.** 

Make sure that you understand how to `prepare for your upgrade </upgrade/prepare-to-upgrade-mattermost.html>`__, familiarize yourself with all `software and hardware requirements </install/software-hardware-requirements.html>`__, read the `important upgrade notes </upgrade/important-upgrade-notes.html>`__ and that you understand each step of the upgrade process documented below before starting a Mattermost upgrade. If you have questions or concerns, you can ask on the Mattermost forum at https://forum.mattermost.com/.

**Gather the following information before starting the upgrade:**

- **Existing install directory - {install-path}**: If you don't know where Mattermost Server is installed, use the ``whereis mattermost`` command to find standard binary places and $PATH. 

  - This command won't won't return anything if ``/opt/mattermost/bin`` wasn't added to the PATH. 
  - Alternatively, you can use the ``find / -executable -type f -iname mattermost 2> /dev/null`` command to find the ``mattermost`` binary. 
  - The output should be similar to ``/opt/mattermost/bin/mattermost``. 
  - The install directory is everything before the first occurrence of the string ``/mattermost``. In this example, the ``{install-path}`` is ``/opt``. 
  - If that command doesn't produce any results, it's likely because your version is older; try ``whereis platform`` instead.
- **Location and size of your local storage directory**: The local storage directory contains all the files that users have attached to their messages.

  - If you don't know its location, open the System Console and go to **Environment > File Storage**, then read the value in **Local Storage Directory**. 
  - Paths are relative to the ``mattermost`` directory. For example, if the local storage directory is ``./data/`` then the absolute path is ``{install-path}/mattermost/data``.
- **Database disk space**: If you're upgrading a Mattermost deployment on the same server as your database, we recommend that you have sufficient disk space available. Double your database size should be sufficient, but more is always better.

Upgrade Mattermost Server
--------------------------

1. In a terminal window on the server that hosts Mattermost, change to your home directory. Delete any files and directories that might still exist from a previous download.

   .. code-block:: sh

     cd /tmp

2. Download `the latest version of Mattermost Server <https://mattermost.com/deploy/>`__. In the following command, replace ``X.X.X`` with the version that you want to download:

   .. code-block:: sh

     # Enterprise Edition
     wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz

     # Team Edition
     wget https://releases.mattermost.com/X.X.X/mattermost-team-X.X.X-linux-amd64.tar.gz

3. Confirm no other Mattermost zip folders exist in your ``/tmp`` directory. If another version's zip file does exist, delete or rename the file.

   .. code-block:: sh

     ls -- mattermost*.gz

   If anything except the new release is returned above, rename this file or delete it completely.

4. Extract the Mattermost Server files.

   .. code-block:: sh

     tar -xf mattermost*.gz --transform='s,^[^/]\+,\0-upgrade,'

   The ``transform`` option adds a suffix to the topmost extracted directory so it does not conflict with the usual install directory.

5. Stop your Mattermost server.

   .. code-block:: sh

     sudo systemctl stop mattermost

6. Back up your data and application. Make sure you've properly backed up your database before continuing with the upgrade. In case of an unexpected failure, you should be in a position to load a previous database snapshot.

   a. Back up your database using your organization’s standard procedures for backing up the database.

   b. Back up your application by copying into an archive folder (e.g. ``mattermost-back-YYYY-MM-DD-HH-mm``).

      .. code-block:: sh

        cd {install-path}
        sudo cp -ra mattermost/ mattermost-back-$(date +'%F-%H-%M')/

7. Remove all files **except** data and custom directories from within the current ``mattermost`` directory. We strongly recommend reading the important note below before executing the following command.

   .. code-block:: sh

     sudo find mattermost/ mattermost/client/ -mindepth 1 -maxdepth 1 \! \( -type d \( -path mattermost/client -o -path mattermost/client/plugins -o -path mattermost/config -o -path mattermost/logs -o -path mattermost/plugins -o -path mattermost/data \) -prune \) | sort | sudo xargs rm -r

   .. important::

     By default, the following subdirectories will be preserved on upgrade:``config``, ``logs``, ``plugins``, ``client/plugins``, and ``data``. Custom directories and ANY other directories that you've added to Mattermost are NOT preserved by default. Generally, these are TLS keys or other custom information, but can also include a different directories configured for local storage other than ``data``, as well as custom directories used to store attachments.

     Before continuing with your upgrade, we strongly recommend that you:

     a. Run ``ls`` on your Mattermost install directory to identify all default folders that exist prior to upgrading.

        A default Mattermost installation has the following files and directories:

        .. code-block:: sh

          $ ls /opt/mattermost
          ENTERPRISE-EDITION-LICENSE.txt README.md  client  data   i18n  manifest.txt  prepackaged_plugins
          NOTICE.txt                      bin        config  fonts  logs  plugins       templates

     b. Perform a dry run of deleting the contents of the ``mattermost`` folder and preserving only the specified directories and their contents by running the following command. It's the same command listed above, but it omits ``sudo xargs rm -r``:

        .. code-block:: sh

          sudo find mattermost/ mattermost/client/ -mindepth 1 -maxdepth 1 \! \( -type d \( -path mattermost/client -o -path mattermost/client/plugins -o -path mattermost/config -o -path mattermost/logs -o -path mattermost/plugins -o -path mattermost/data \) -prune \) | sort

     c. If you store TLSCert/TLSKey files or other information within your ``/opt/mattermost`` folder, you need to append ``-o -path mattermost/yourFolderHere`` to the command above to avoid having to manually copy the TLSCert/TLSKey files from the backup into the new install.

        .. code-block:: sh

          sudo find mattermost/ mattermost/client/ -mindepth 1 -maxdepth 1 \! \( -type d \( -path mattermost/client -o -path mattermost/client/plugins -o -path mattermost/config -o -path mattermost/logs -o -path mattermost/plugins -o -path mattermost/data -o -path  mattermost/yourFolderHere \) -prune \) | sort

     d. If you're using `Bleve search </deploy/bleve-search.html>`__, and the directory exists *within* the ``mattermost`` directory, the index directory path won't be preserved using the command above. 

        - You can either move the bleve index directory out from the ``mattermost`` directory before upgrading or, following an upgrade, you can copy the contents of the bleve index directory from the ``backup`` directory. 
        - You can then store that directory or re-index as preferred. 
        - The bleve indexes can be migrated without reindexing between Mattermost versions. See our `Configuration Settings </configure/configuration-settings.html#bleve-settings-experimental>`__ documentation for details on configuring the bleve index directory.

     Once you've completed all of the steps above (where applicable), you're ready to execute the full command that includes ``xargs rm -r`` to delete the files. Note that the following example includes ``-o -path mattermost/yourFolderHere``:

     .. code-block:: sh

       sudo find mattermost/ mattermost/client/ -mindepth 1 -maxdepth 1 \! \( -type d \( -path mattermost/client -o -path mattermost/client/plugins -o -path mattermost/config -o -path mattermost/logs -o -path mattermost/plugins -o -path mattermost/data -o -path  mattermost/yourFolderHere \) -prune \) | sort | sudo xargs rm -r

8. Copy the new files to your install directory.

   .. code-block:: sh

     sudo cp -an /tmp/mattermost-upgrade/. mattermost/

   .. note::

     The ``n`` (no-clobber) flag and trailing ``.`` on source are very important. The ``n`` (no-clobber) flag preserves existing configurations and logs in your installation path. The trailing ``.`` on source ensures all installation files are copied.

9. Change ownership of the new files after copying them. For example:

   .. code-block:: sh

     sudo chown -R mattermost:mattermost mattermost

   .. note::

     - If you didn't use ``mattermost`` as the owner and group of the install directory, run ``sudo chown -hR {owner}:{group} {install-path}/mattermost``.
     - If you're uncertain what owner or group was defined, use the ``ls -l {install-path}/mattermost/bin/mattermost`` command to obtain them.

10. If you want to use port 80 or 443 to serve your server, and/or if you have TLS set up on your Mattermost server, you **must** activate the ``CAP_NET_BIND_SERVICE`` capability to allow the new Mattermost binary to bind to ports lower than 1024. For example:

    .. code-block:: sh

      sudo setcap cap_net_bind_service=+ep ./mattermost/bin/mattermost

11. Start your Mattermost server.

    .. code-block:: sh

      sudo systemctl start mattermost

12. Remove the temporary files.

    .. code-block:: sh

      sudo rm -r /tmp/mattermost-upgrade/
      sudo rm -i /tmp/mattermost*.gz

13. If you're using a `high availability </scale/high-availability-cluster.html>`__ deployment, you need to apply the steps above on every node in your cluster. Once complete, the **Config File MD5** columns in the high availability section of the System Console should be green. If they're yellow, please ensure that all nodes have the same server version and the same configuration.

    If they continue to display as yellow, trigger a configuration propagation across the cluster by opening the System Console, changing a setting, and reverting it. This will enable the **Save** button for that page. Then, select **Save**. This will not change any configuration, but sends the existing configuration to all nodes in the cluster. 

After the server is upgraded, users might need to refresh their browsers to experience any new features.

Upgrade Team Edition to Enterprise Edition
--------------------------------------------

To upgrade from the Team Edition to the Enterprise Edition, follow the normal upgrade instructions provided above, making sure that you download the Enterprise Edition of Mattermost Server in Step 2.

Upload a license key
---------------------

When Enterprise Edition is running, open **System Console > About > Editions and License** and upload your license key.
