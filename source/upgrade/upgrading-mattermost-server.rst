Upgrading Mattermost Server
===========================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

In most cases, you can upgrade Mattermost Server in a few minutes. However, the upgrade can take longer depending on several factors, including the size and complexity of your installation, and the version that you're upgrading from.

Preparing to upgrade to the latest version
------------------------------------------

A Mattermost server v6.0 upgrade will run significant database schema changes that can cause an extended startup time depending on the dataset size. Zero downtime won't be possible for v6.0, but depending on the efforts made during the migration process, it can be minimized to a large extent. 

Running queries prior to the upgrade can also save some downtime. However, some queries can still cause full table locking and require Mattermost to be in read-only mode for the duration of the query.

We strongly recommend that you:

- Set up a maintenance window outside of working hours to mitigate the migration impact. 
- Keep a backup of your database to ensure you can load a previous database snapshot if necessary.
- Upgrade your instance of Mattermost to the latest `Extended Support Release (ESR) <https://docs.mattermost.com/administration/extended-support-release.html>`__ first before attempting to run the Mattermost v6.0 upgrade.

.. important::

  Support for Mattermost Server v5.31 `Extended Support Release <https://docs.mattermost.com/administration/extended-support-release.html>`__ will come to the end of its life cycle on October 15, 2021. Upgrading to Mattermost Server v5.37 Extended Support Release or later is required.

Upgrading from a previous Extended Support Release to the latest Extended Support Release is supported. Upgrading from v5.31 to v5.37 should take roughly the same amount of time as upgrading from v5.31 to v5.35, then upgrading v5.35 to 5.37. However, an upgrade directly from v5.31 to v5.37 could potentially take hours due to the database schema migrations required for v5.35. Review the :doc:`important-upgrade-notes` for all intermediate versions in between to ensure you’re aware of the possible migrations that could affect your upgrade.

v6.0 Database Schema Migrations
-------------------------------

Mattermost v6.0 introduces several database schema changes to improve both database and application performance. The upgrade will run significant database schema changes that can cause an extended startup time depending on the dataset size. We've conducted extensive tests on supported database drivers including MySQL and PostgreSQL, using realistic datasets of more than 10 million posts. 

See the `Mattermost v6.0 DB Schema Migrations Analysis <https://gist.github.com/streamer45/59b3582118913d4fc5e8ff81ea78b055>`__ documentation for specifications, data size, and test results.

.. tabs::

   .. tab:: MySQL

      The following queries executed during the migration process will have a significant impact on database CPU usage and write operation restrictions for the duration of the query:

      ``ALTER TABLE Posts MODIFY Props JSON;`` (~26 minutes)

      ``ALTER TABLE Posts DROP COLUMN ParentId;`` (~26 minutes)

      ``ALTER TABLE Posts MODIFY COLUMN FileIds text;`` (~26 minutes)

      For a complete breakdown of MySQL queries, as well as their impact and duration, see the `Mattermost v6.0 DB Schema Migrations Analysis <https://gist.github.com/streamer45/59b3582118913d4fc5e8ff81ea78b055#mysql-1>`__ documentation.

      **MySQL Mitigation Strategies**

      **Run combined queries prior to the upgrade.**
      The previous queries can be combined when run prior to the upgrade as follows:

      ``ALTER TABLE Posts MODIFY COLUMN FileIds text, MODIFY COLUMN Props JSON;``

      This limits the time taken to that of a single query of that type.

      **Online migration**: An online migration that avoids locking can be attempted on MySQL installations, especially for particularly heavy queries or very big datasets (tens of millions of posts or more). This can be done through an external tool like `pt-online-schema-change <https://www.percona.com/doc/percona-toolkit/LATEST/pt-online-schema-change.html>`__. However, the online migration process can cause a significant spike in CPU usage on the database instance it runs.

      See the `Mattermost v6.0 DB Schema Migrations Analysis <https://gist.github.com/streamer45/59b3582118913d4fc5e8ff81ea78b055#online-migration-mysql>`__ documentation for a sample execution and additional caveats.

   .. tab:: PostgreSQL

      The following query executed during the migration process will have a significant impact on database CPU usage and write operation restrictions for the duration of the query:

      ``ALTER TABLE posts ALTER COLUMN props TYPE jsonb USING props::jsonb;`` (~ 11 minutes)

      For a complete breakdown of PostgreSQL queries, as well as their impact and duration, see the `Mattermost v6.0 DB Schema Migrations Analysis <https://gist.github.com/streamer45/59b3582118913d4fc5e8ff81ea78b055#postgresql-1>`__.

Upgrading from Releases Older than v5.35
----------------------------------------

Customers upgrading from a release older than Mattermost v5.35 should expect extended downtime when upgrading to v6.0 due to the introduction of backend database architecture introduced in v5.35. This upgrade path isn't recommended for large installations. We recommend upgrading to the latest `Extended Support Release (ESR) <https://docs.mattermost.com/administration/extended-support-release.html>`__ first before upgrading to Mattermost v6.0. See the `Mattermost Changelog <https://docs.mattermost.com/install/self-managed-changelog.html>`__ documentation for additional details.

If you're upgrading from a version prior to Mattermost v5.0, you can't upgrade directly to v6.0. Instead, we strongly recommend approaching the upgrade in phases, starting with an upgrade to the latest ESR first, followed by the upgrade to v6.0. During the first phase of updates, you must also modify your service file to work with the binary changes introduced with the v5.0 release. Your execution directory should point to the Mattermost base directory (i.e. ``/opt/mattermost``), and your binary should point to the ``mattermost`` binary (i.e. ``/opt/mattermost/bin/mattermost``). 

Ensure you review the :doc:`important-upgrade-notes` for all intermediate release versions in between to ensure you’re aware of the possible migrations that could affect your upgrade.

Upgrading High Availability Deployments
---------------------------------------

In `High Availability <https://docs.mattermost.com/scale/high-availability-cluster.html>`__ environments, you should expect to schedule downtime for the upgrade to v6.0. Based on your database size and setup, the migration to v6.0 can take a significant amount of time, and may even lock the tables for posts which will prevent your users from posting or receiving messages until the migration is complete.

Ensure you review the `High Availability Cluster Upgrade Guide <https://docs.mattermost.com/scale/high-availability-cluster.html#upgrade-guide>`__, as well as the :doc:`important-upgrade-notes` to make sure you're aware of any actions you need to take before or after upgrading from your particular version.

.. important::

  We only support one minor version difference between server versions when performing a rolling upgrade. For example v5.27.1 + v5.27.2 or v5.26.4 + v5.27.1 is supported, whereas v5.25.5 + v5.27.0 is not supported. 

  Running two different versions of Mattermost in your cluster should not be done outside of an upgrade scenario. Due to a fundamental change to the clustering code in v6.0, nodes from different versions cannot be run, as noted in the :doc:`important-upgrade-notes` product documentation.

  The release of v6.0 also introduces database schema changes and longer migration times should be expected, especially on MySQL installations. 

.. _before-you-begin:

Before you begin
----------------

**Read these instructions carefully from start to finish.** 

Make sure that you understand each step before starting the upgrade. If you have questions or concerns, you can ask on the Mattermost forum at https://forum.mattermost.org/.

**Gather the following information before starting the upgrade**

- **Existing install directory - {install-path}**: If you don't know where Mattermost Server is installed, use the ``whereis mattermost`` command to find standard binary places and $PATH (which won't return anything if ``/opt/mattermost/bin`` wasn't added to the PATH), or use the ``find / -executable -type f -iname mattermost 2> /dev/null`` command to find the ``mattermost`` binary. The output should be similar to ``/opt/mattermost/bin/mattermost``. The install directory is everything before the first occurrence of the string ``/mattermost``. In this example, the ``{install-path}`` is ``/opt``. If that command doesn't produce any results, it's likely because your version is older; try ``whereis platform`` instead.
- **Location of your local storage directory**: The local storage directory contains all the files that users have attached to their messages. If you don't know its location, open the System Console and go to **Environment > File Storage**, then read the value in **Local Storage Directory**. Paths are relative to the ``mattermost`` directory. For example, if the local storage directory is ``./data/`` then the absolute path is ``{install-path}/mattermost/data``.

Upgrading Mattermost Server
----------------------------

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

6. Back up your data and application. Make sure you've properly backed up your database before continuing with the upgrade. In case of an unexpected failure, you should be in a position to load a previous database snapshot.

   a. Back up your database using your organization’s standard procedures for backing up MySQL or PostgreSQL.

   b. Back up your application by copying into an archive folder (e.g. ``mattermost-back-YYYY-MM-DD-HH-mm``).

      .. code-block:: sh

        cd {install-path}
        sudo cp -ra mattermost/ mattermost-back-$(date +'%F-%H-%M')/

7. Remove all files **except** data and custom directories from within the current ``mattermost`` directory. 

   .. code-block:: sh

     sudo find mattermost/ mattermost/client/ -mindepth 1 -maxdepth 1 \! \( -type d \( -path mattermost/client -o -path mattermost/client/plugins -o -path mattermost/config -o -path mattermost/logs -o -path mattermost/plugins -o -path mattermost/data \) -prune \) | sort | sudo xargs rm -r

   **What's preserved on upgrade?**
  
   By default, the following subdirectories will be preserved:``config``, ``logs``, ``plugins``, ``client/plugins``, and ``data`` (unless you have a different directory configured for local storage). Custom directories are any directories that you've added to Mattermost and are not preserved by default. Generally, these are TLS keys or other custom information.

   Run ``ls`` on your Mattermost install directory to identify what default folders exist.
      
   **A default Mattermost installation has the following files and directories**:

   .. code-block:: sh

     $ ls /opt/mattermost
     ENTERPRISE-EDITION-LICENSE.txt README.md  client  data   i18n  manifest.txt  prepackaged_plugins
     NOTICE.txt                      bin        config  fonts  logs  plugins       templates

   **Clear the Mattermost folder**

   Dry-run the following command to delete the contents of the ``mattermost`` folder, preserving only the specified directories and their contents: 
  
   .. code-block:: sh
    
     sudo find mattermost/ mattermost/client/ -mindepth 1 -maxdepth 1 \! \( -type d \( -path mattermost/client -o -path mattermost/client/plugins -o -path mattermost/config -o -path mattermost/logs -o -path mattermost/plugins -o -path mattermost/data \) -prune \) | sort
    
   If you store TLSCert/TLSKey files or other information within your ``/opt/mattermost`` folder, you need to append ``-o -path mattermost/yourFolderHere`` to the command above to avoid having to manually copy the TLSCert/TLSKey files from the backup into the new install.
 
  .. code-block:: sh
 
    sudo find mattermost/ mattermost/client/ -mindepth 1 -maxdepth 1 \! \( -type d \( -path mattermost/client -o -path mattermost/client/plugins -o -path mattermost/config -o -path mattermost/logs -o -path mattermost/plugins -o -path mattermost/data -o -path  mattermost/yourFolderHere \) -prune \) | sort
    
  When you're ready to execute the command, append ``xargs rm -r`` to the command above to delete the files. Note that the following example includes ``-o -path mattermost/yourFolderHere``:
  
  .. code-block:: sh
  
    sudo find mattermost/ mattermost/client/ -mindepth 1 -maxdepth 1 \! \( -type d \( -path mattermost/client -o -path mattermost/client/plugins -o -path mattermost/config -o -path mattermost/logs -o -path mattermost/plugins -o -path mattermost/data -o -path  mattermost/yourFolderHere \) -prune \) | sort | sudo xargs rm -r
  
  **Using Bleve Search**

  If using `Bleve Search <https://docs.mattermost.com/deploy/bleve-search.html>`__, and the directory exists *within* the ``mattermost`` directory, the index directory path won't be preserved using the command above. 
  
  - You can either move the bleve index directory out from the ``mattermost`` directory before upgrading or, following an upgrade, you can copy the contents of the bleve index directory from the ``backup`` directory. 
  - You can then store that directory or re-index as preferred. 
  - The bleve indexes can be migrated without reindexing between Mattermost versions. See our `Configuration Settings <https://docs.mattermost.com/configure/configuration-settings.html#bleve-settings-experimental>`__ documentation for details on configuring the bleve index directory.

8. Copy the new files to your install directory.

  .. code-block:: sh

   sudo cp -an /tmp/mattermost-upgrade/. mattermost/

  .. note::
    
    The ``n`` (no-clobber) flag and trailing ``.`` on source are very important. The ``n`` (no-clobber) flag preserves existing configurations and logs in your installation path. The trailing ``.`` on source ensures all installation files are copied.


9. Change ownership of the new files after copying them. For example:

  .. code-block:: sh
         
    sudo chown -R mattermost:mattermost {install-path}/mattermost
     
.. note::
    
  - If you didn't use ``mattermost`` as the owner and group of the install directory, run ``sudo chown -hR {owner}:{group} {install-path}/mattermost``.
  - If you're uncertain what owner or group was defined, use the ``ls -l {install-path}/mattermost/bin/mattermost`` command to obtain them.
  
10. If you want to use port 80 or 443 to serve your server, and/or if you have TLS set up on your Mattermost server, you **must** activate the ``CAP_NET_BIND_SERVICE`` capability to allow the new Mattermost binary to bind to ports lower than 1024. For example:

  .. code-block:: sh

    cd {install-path}/mattermost
    sudo setcap cap_net_bind_service=+ep ./bin/mattermost

11. Start your Mattermost server.

  .. code-block:: sh

    sudo systemctl start mattermost

12. Remove the temporary files.

  .. code-block:: sh

    sudo rm -r /tmp/mattermost-upgrade/
    sudo rm -i /tmp/mattermost*.gz

13. If you're using a `High Availability <https://docs.mattermost.com/scale/high-availability-cluster.html>`__ deployment, you need to apply the steps above on every node in your cluster. Once complete, the **Config File MD5** columns in the High Availability section of the System Console should be green. If they're yellow, please ensure that all nodes have the same server version and the same configuration.

    If they continue to display as yellow, trigger a configuration propagation across the cluster by opening the System Console, changing a setting, and reverting it. This will enable the **Save** button for that page. Then, select **Save**. This will not change any configuration, but sends the existing configuration to all nodes in the cluster. 

After the server is upgraded, users might need to refresh their browsers to experience any new features.

Upgrading Team Edition to Enterprise Edition
--------------------------------------------

To upgrade from the Team Edition to the Enterprise Edition, follow the normal upgrade instructions provided above, making sure that you download the Enterprise Edition of Mattermost Server in Step 2.

Uploading a License Key
-----------------------

When Enterprise Edition is running, open **System Console > About > Editions and License** and upload your license key.
