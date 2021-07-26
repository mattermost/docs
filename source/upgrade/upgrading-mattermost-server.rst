Upgrading Mattermost Server
===========================

In most cases you can upgrade Mattermost Server in a few minutes, but the upgrade can take longer depending on several factors, including the size and complexity of your installation, and the version that you're upgrading from.

.. important::

  Support for Mattermost Server v5.31 `Extended Support Release <https://docs.mattermost.com/administration/extended-support-release.html>`_ will come to the end of its life cycle on October 15, 2021. Upgrading to Mattermost Server v5.37 `Extended Support Release <https://docs.mattermost.com/administration/extended-support-release.html>`_ or later is required.

Upgrading to the Latest Version
-------------------------------

If you are upgrading from version 3.0 or later, these instructions apply to you. If you are upgrading from a version prior to 3.0.0, you must first upgrade to version 3.0.3.

.. _before-you-begin:

**Before you begin**

Read these instructions carefully from start to finish. Make sure that you understand each step before starting the upgrade. If you have questions or concerns, you can ask on the Mattermost forum at https://forum.mattermost.org/.

.. important::

  Review the :doc:`important-upgrade-notes` to make sure you are aware of any actions you need to take before or after upgrading from your particular version.
  
.. important::

  If you're upgrading from a version prior to v5.0 be sure to also modify your service file to work with the binary changes introduced with 5.0. Your execution directory should point to the Mattermost base directory (i.e. ``/opt/mattermost``) and your binary should point to the ``mattermost`` binary (i.e. ``/opt/mattermost/bin/mattermost``).

You should gather the following information before starting the upgrade:

Existing install directory - *{install-path}*
  If you don't know where Mattermost Server is installed, use the ``whereis mattermost`` command. The output should be similar to */opt/mattermost/bin/mattermost*. The install directory is everything before the first occurrence of the string */mattermost*. In this example, the *{install-path}* is ``/opt``.
  If that command does not produce any results because your version is older, try ``whereis platform`` instead.
Location of your local storage directory
  The local storage directory contains all the files that users have attached to their messages. If you don't know its location, open the System Console and go to **Environment > File Storage**, then read the value in **Local Storage Directory**. Relative paths are relative to the ``mattermost`` directory. For example, if the local storage directory is ``./data/`` then the absolute path is ``{install-path}/mattermost/data``.

**To upgrade Mattermost Server**

.. note::

  If you're upgrading a High Availability cluster, `review these upgrade notes instead <https://docs.mattermost.com/deployment/cluster.html#upgrade-guide>`__.

#. Review the :doc:`important-upgrade-notes` to make sure you are aware of any actions you need to take before or after upgrading from your particular version.

#. In a terminal window on the server that hosts Mattermost, change to your home directory. If any, delete files and directories that might still exist from a previous download.

   .. code-block:: sh

     cd /tmp

#. Download `the latest version of Mattermost Server <https://mattermost.com/download/>`__. In the following command, replace ``X.X.X`` with the version that you want to download:

   .. code-block:: sh

     wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz

#. Confirm no other Mattermost zip folders exist in your ``/tmp`` directory. If another version's zip file does exist, delete or rename the file.

   .. code-block:: sh
     
     ls -- mattermost*.gz
  
   If anything except the new release is returned above, rename this file or delete it completely.

#. Extract the Mattermost Server files.

   .. code-block:: sh
     
     tar -xf mattermost*.gz --transform='s,^[^/]\+,\0-upgrade,'
  
   The ``transform`` option adds a suffix to the topmost extracted directory so it does not conflict with the usual install directory.

#. Stop your Mattermost server.

   .. code-block:: sh

     sudo systemctl stop mattermost

#. Back up your data and application.

   #. Back up your database using your organization’s standard procedures for backing up MySQL or PostgreSQL.

   #. Back up your application by copying into an archive folder (e.g. ``mattermost-back-YYYY-MM-DD-HH-mm``).

      .. code-block:: sh

        cd {install-path}
        sudo cp -ra mattermost/ mattermost-back-$(date +'%F-%H-%M')/

#. Remove all files *except data and custom directories* from within the current mattermost directory.
   
    a. Run ``ls`` on your Mattermost install directory to identify what folders exist. If your folders match the structure below you can jump to step c.

        - By default, your data directories will be preserved with the below commands. These are ``config``, ``logs``, ``plugins``, ``client/plugins``, and ``data`` (unless you have a different value configured for local storage, as per *Before you begin*).
        - Custom directories are directories that you've added to Mattermost and are not preserved by default. Generally, these are TLS keys or other custom information.
        
        |
        .. note::
         **A default Mattermost install has the below files/directories**:

          .. code-block:: sh

            $ ls /opt/mattermost
            ENTERPRISE-EDITION-LICENSE.txt README.md  client  data   i18n  manifest.txt  prepackaged_plugins
            NOTICE.txt                      bin        config  fonts  logs  plugins       templates
          
    b. Identify if any custom directories from the above step need to be preserved. For each custom directory within the Mattermost folder that you wish to preserve add ``-o -path  mattermost/yourFolderHere`` to the below commands. See the example below where the folder ``yourFolderHere`` is preserved by adding ``-o -path  mattermost/yourFolderHere``.
    
      .. code-block:: sh

        sudo find mattermost/ mattermost/client/ -mindepth 1 -maxdepth 1 \! \( -type d \( -path mattermost/client -o -path mattermost/client/plugins -o -path mattermost/config -o -path mattermost/logs -o -path mattermost/plugins -o -path mattermost/data -o -path  mattermost/yourFolderHere \) -prune \) | sort | xargs echo rm -r
    
    c. You should first modify the last part to ``xargs echo rm -r`` to verify what will be executed. If you've added custom directories to the command in step b then add those to the below command. For example:
    
      .. code-block:: sh

        sudo find mattermost/ mattermost/client/ -mindepth 1 -maxdepth 1 \! \( -type d \( -path mattermost/client -o -path mattermost/client/plugins -o -path mattermost/config -o -path mattermost/logs -o -path mattermost/plugins -o -path mattermost/data \) -prune \) | sort | xargs echo rm -r
    
    d. Clear the contents of this directory. If you've added custom directories to the command be sure to add those to this below command. For example:

      .. code-block:: sh

        sudo find mattermost/ mattermost/client/ -mindepth 1 -maxdepth 1 \! \( -type d \( -path mattermost/client -o -path mattermost/client/plugins -o -path mattermost/config -o -path mattermost/logs -o -path mattermost/plugins -o -path mattermost/data \) -prune \) | sort | sudo xargs rm -r
      
#. Change ownership of the new files before copying them. For example:

   .. code-block:: sh

     sudo chown -hR mattermost:mattermost /tmp/mattermost-upgrade/
     
   .. note::
     If you didn't use ``mattermost`` as the owner and group of the install directory, run ``sudo chown -hR {owner}:{group} tmp/mattermost-upgrade/``.

     If you're uncertain what owner or group was defined, use the ``ls -l {install-path}/mattermost/bin/mattermost`` command to obtain them.

#. Copy the new files to your install directory and remove the temporary files.

   Note that the ``n`` (no-clobber) flag and trailing ``.`` on source are very important.

   .. code-block:: sh

     sudo cp -an /tmp/mattermost-upgrade/. mattermost/
     sudo rm -r /tmp/mattermost-upgrade/
     sudo rm -i /tmp/mattermost*.gz

#. If you want to use port 80 to serve your server, or if you have TLS set up on your Mattermost server, you *must* activate the CAP_NET_BIND_SERVICE capability to allow the new Mattermost binary to bind to low ports. For example:

   .. code-block:: sh

     cd {install-path}/mattermost
     sudo setcap cap_net_bind_service=+ep ./bin/mattermost

#. Start your Mattermost server.

   .. code-block:: sh

     sudo systemctl start mattermost

#. If you're using a High Availability deployment you need to apply the steps above on all the nodes in your cluster. Once complete, the **Config File MD5** columns in the High Availability section of the system console should be green. If they're yellow, please ensure that all nodes have the same server version and the same configuration.

If they still show yellow, then you need to trigger a config propagation across the cluster:

   #. Open the System Console and change a setting, then revert it. This will enable the **Save** button for that page.
   #. Click **Save**.

   This will not change any config, but sends the existing config to all nodes in the cluster.

After the server is upgraded, users might need to refresh their browsers to experience any new features.

.. note::

  We only support one minor version difference between the server versions when performing a rolling upgrade (for example v5.27.1 + v5.27.2 or v5.26.4 + v5.27.1 is supported, whereas v5.25.5 + v5.27.0 is not supported). Running two different versions of Mattermost in your cluster should not be done outside of an upgrade scenario.

Upgrading Team Edition to Enterprise Edition
--------------------------------------------

To upgrade from the Team Edition to the Enterprise Edition, follow the normal upgrade instructions provided above, making sure that you download the Enterprise Edition in Step 3.

Uploading a License Key
-----------------------

When Enterprise Edition is running, open **System Console > About > Editions and License** and upload your license key.
