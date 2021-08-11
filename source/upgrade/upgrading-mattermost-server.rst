Upgrading Mattermost Server
===========================

In most cases you can upgrade Mattermost Server in a few minutes, but the upgrade can take longer depending on several factors, including the size and complexity of your installation, and the version that you're upgrading from.

.. important::

  Support for Mattermost Server v5.31 `Extended Support Release <https://docs.mattermost.com/administration/extended-support-release.html>`_ will come to the end of its life cycle on October 15, 2021. Upgrading to Mattermost Server v5.37 `Extended Support Release <https://docs.mattermost.com/administration/extended-support-release.html>`_ or later is required.

Upgrading to the Latest Version
-------------------------------

If you are upgrading from version 3.0 or later, these instructions apply to you. If you are upgrading from a version prior to 3.0.0, you must first upgrade to version 3.0.3.

Upgrading from a previous Extended Support Release to the latest Extended Support Release is supported. However, we strongly recommend that you review the :doc:`important-upgrade-notes` for all intermediate versions in between to ensure you're aware of the possible migrations that could affect your upgrade.

For `High Availability <https://docs.mattermost.com/scale/high-availability-cluster.html>`__ deployments, we only support one minor version difference between  server versions when performing a rolling upgrade. For example v5.27.1 + v5.27.2 or v5.26.4 + v5.27.1 is supported, whereas v5.25.5 + v5.27.0 is not supported. Running two different versions of Mattermost in your cluster should not be done outside of an upgrade scenario. In some upgrade scenarios, it won't be possible to run different versions, and such cases are clearly noted in the :doc:`important-upgrade-notes` product documentation.

.. _before-you-begin:

Before you Begin
----------------

Read these instructions carefully from start to finish. Make sure that you understand each step before starting the upgrade. If you have questions or concerns, you can ask on the Mattermost forum at https://forum.mattermost.org/.

.. important::

  - Review the :doc:`important-upgrade-notes` to make sure you are aware of any actions you need to take before or after upgrading from your particular version.
  - If you're upgrading from a version prior to v5.0 be sure to also modify your service file to work with the binary changes introduced with 5.0. Your execution directory should point to the Mattermost base directory (i.e. ``/opt/mattermost``) and your binary should point to the ``mattermost`` binary (i.e. ``/opt/mattermost/bin/mattermost``).
  - Gather the following information before starting the upgrade:
      - **Existing install directory - {install-path}**: If you don't know where Mattermost Server is installed, use the ``whereis mattermost`` command to find standard binary places and $PATH (which won't return anything if ``/opt/mattermost/bin`` wasn't added to the PATH), or use the ``find / -executable -type f -iname mattermost 2> /dev/null`` command to find the mattermost binary. The output should be similar to ``/opt/mattermost/bin/mattermost``. The install directory is everything before the first occurrence of the string ``/mattermost``. In this example, the ``{install-path}`` is ``/opt``. If that command does not produce any results, it's likely because your version is older; try ``whereis platform`` instead.
      - **Location of your local storage directory**: The local storage directory contains all the files that users have attached to their messages. If you don't know its location, open the System Console and go to **Environment > File Storage**, then read the value in **Local Storage Directory**. Paths are relative to the ``mattermost`` directory. For example, if the local storage directory is ``./data/`` then the absolute path is ``{install-path}/mattermost/data``.

Upgrading Mattermost Server
----------------------------

.. note::

  - If you're upgrading a High Availability cluster, `review these upgrade notes instead <https://docs.mattermost.com/deployment/cluster.html#upgrade-guide>`__.
  - Review the :doc:`important-upgrade-notes` to make sure you're aware of any actions you need to take before or after upgrading from your particular version.

1. In a terminal window on the server that hosts Mattermost, change to your home directory. Delete any files and directories that might still exist from a previous download.

   .. code-block:: sh

     cd /tmp

2. Download `the latest version of Mattermost Server <https://mattermost.com/download/>`__. In the following command, replace ``X.X.X`` with the version that you want to download:

   .. code-block:: sh

     wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz

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

6. Back up your data and application.

   a. Back up your database using your organization’s standard procedures for backing up MySQL or PostgreSQL.

   b. Back up your application by copying into an archive folder (e.g. ``mattermost-back-YYYY-MM-DD-HH-mm``).

      .. code-block:: sh

        cd {install-path}
        sudo cp -ra mattermost/ mattermost-back-$(date +'%F-%H-%M')/

7. Remove all files **except** data and custom directories from within the current ``mattermost`` directory. 

  **What's preserved?**
  
  By default, your data directories will be preserved with the following commands:``config``, ``logs``, ``plugins``, ``client/plugins``, and ``data`` (unless you have a different value configured for local storage). Custom directories are any directories that you've added to Mattermost and are not preserved by default. Generally, these are TLS keys or other custom information.

  Run ``ls`` on your Mattermost install directory to identify what default folders exist. If your folders match the structure specified in the following note, you can jump to step 8 below.
      
  **A default Mattermost installation has the following files and directories**:

  .. code-block:: sh

    $ ls /opt/mattermost
    ENTERPRISE-EDITION-LICENSE.txt README.md  client  data   i18n  manifest.txt  prepackaged_plugins
    NOTICE.txt                      bin        config  fonts  logs  plugins       templates

  **Clear Mattermost contents**

  The following command clears the contents of the ``mattermost`` folder, preserving only the specified directories and their contents: 
  
  .. code-block:: sh
    
    sudo find mattermost/ mattermost/client/ -mindepth 1 -maxdepth 1 \! \( -type d \( -path mattermost/client -o -path mattermost/client/plugins -o -path mattermost/config -o -path mattermost/logs -o -path mattermost/plugins -o -path mattermost/data \) -prune \)
  
  We recommend that you append ``xargs echo rm -r`` to the command above to verify what will be executed first.

  Also, if you store TLSCert/TLSKey files or other information within your ``/opt/mattermost`` folder, you should append ``-o -path mattermost/{yourFolderHere}`` to the command above, or you'll have to manually copy the TLSCert/TLSKey files from the backup into the new install.
  
  **Using Bleve Search**

  If using `Bleve Search <https://docs.mattermost.com/deploy/bleve-search.html>`__, and the directory exists *within* the ``mattermost`` directory, the index directory path won't be preserved using the command above. 
  
  - You can either move the bleve index directory out from the ``mattermost`` directory before upgrading or, following an upgrade, you can copy the contents of the bleve index directory from the ``backup`` directory. 
  - You can then store that directory or re-index as preferred. 
  - The bleve indexes can be migrated without reindexing between Mattermost versions. See our `Configuration Settings <https://docs.mattermost.com/configure/configuration-settings.html#bleve-settings-experimental>`__ documentation for details on configuring the bleve index directory.

8. Copy the new files to your install directory and remove the temporary files.

  .. code-block:: sh

   sudo cp -an /tmp/mattermost-upgrade/. mattermost/
   sudo rm -r /tmp/mattermost-upgrade/
   sudo rm -i /tmp/mattermost*.gz

  .. note::
    
    The ``n`` (no-clobber) flag and trailing ``.`` on source are very important. The ``n`` (no-clobber) flag preserves existing configurations and logs in your installation path. The trailing ``.`` on source ensures all installation files are copied.

9. If you want to use port 80 or 443 to serve your server, and/or if you have TLS set up on your Mattermost server, you **must** activate the CAP_NET_BIND_SERVICE capability to allow the new Mattermost binary to bind to ports lower than 1024. For example:

  .. code-block:: sh

    cd {install-path}/mattermost
    sudo setcap cap_net_bind_service=+ep ./bin/mattermost

10. Change ownership of the new files before copying them. For example:

  .. code-block:: sh
         
    sudo chown -R mattermost:mattermost {install-path}
     
.. note::
    
  - If you didn't use ``mattermost`` as the owner and group of the install directory, run ``sudo chown -hR {owner}:{group} tmp/mattermost-upgrade/``.
  - If you're uncertain what owner or group was defined, use the ``ls -l {install-path}/mattermost/bin/mattermost`` command to obtain them.

11. Start your Mattermost server.

  .. code-block:: sh

    sudo systemctl start mattermost

12. If you're using a `High Availability <https://docs.mattermost.com/scale/high-availability-cluster.html>`__ deployment, you need to apply the steps above on every node in your cluster. Once complete, the **Config File MD5** columns in the High Availability section of the System Console should be green. If they're yellow, please ensure that all nodes have the same server version and the same configuration.

    If they continue to display as yellow, trigger a configuration propagation across the cluster by opening the System Console, changing a setting, and reverting it. This will enable the **Save** button for that page. Then, select **Save**. This will not change any configuration, but sends the existing configuration to all nodes in the cluster. 

After the server is upgraded, users might need to refresh their browsers to experience any new features.

Upgrading Team Edition to Enterprise Edition
--------------------------------------------

To upgrade from the Team Edition to the Enterprise Edition, follow the normal upgrade instructions provided above, making sure that you download the Enterprise Edition of Mattermost Server in Step 2.

Uploading a License Key
-----------------------

When Enterprise Edition is running, open **System Console > About > Editions and License** and upload your license key.
