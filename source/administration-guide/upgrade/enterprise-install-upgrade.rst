Upgrading Team Edition to Enterprise Edition
=============================================

.. include:: ../../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

Mattermost Enterprise Edition is free to use in "team mode" without Enterprise features enabled. Mattermost offers two subscription plans, including Enterprise and Professional. You can `compare their features online <https://mattermost.com/pricing/>`_.

Once you've downloaded and installed Mattermost, start an Enterprise trial via **Product menu > System Console > Edition and License > Start trial**. View pricing and feature information online, and talk to a `Mattermost Expert <https://mattermost.com/contact-sales/>`_ to purchase a license key.

Checking your Mattermost edition and version
---------------------------------------------

To check your edition and version from the web or desktop interface, open **Product menu > About Mattermost**.

- **Mattermost Enterprise Edition** indicates you can apply a license key to enable Enterprise features.
- **Mattermost Team Edition** indicates you're using the open source version and need to upgrade (per upgrade instructions below) before a license key can be applied.

Upgrading to Enterprise Edition from Team Edition
--------------------------------------------------

The open source Mattermost Team Edition is functionally identical to the commercial Mattermost Enterprise Edition in its free "team mode", but there is no ability to unlock Enterprise features.

To enable unlocking Enterprise features, replace the Mattermost Team Edition binary with a Mattermost Enterprise Edition binary via an :doc:`upgrade procedure </administration-guide/upgrade/upgrading-mattermost-server>`.

If you'd like to back up Mattermost prior to upgrading, :doc:`the migration guide </administration-guide/onboard/migrating-to-mattermost>` outlines the process required to back up and restore your database.

Upgrading Enterprise Edition to a newer version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upgrade a previous version of Mattermost Enterprise Edition to a later version by following the :doc:`upgrade procedure </administration-guide/upgrade/upgrading-mattermost-server>`.

Converting Team Edition to Enterprise Edition
----------------------------------------------

If you're running a Linux system with x86-64 architecture, you can convert Team Edition to Enterprise in the System Console using a built-in conversion utility. This tool is recommended if you'd like to run an Enterprise trial or want to upgrade to Enterprise or Professional on standalone servers.

.. note::

  * If you're using a modified version of Mattermost, using this tool will overwrite your changes and replace them with the official Enterprise Edition binary.
  * For versions prior to v5.27, please follow :ref:`these upgrade instructions <administration-guide/upgrade/upgrading-mattermost-server:upgrade team edition to enterprise edition>`.

Navigate to **Product menu > System Console > Edition and License** and select **Upgrade to Enterprise Edition**.

During the upgrade process, the Mattermost Enterprise Edition binary file that matches your current server version is downloaded, decompressed, and extracted. The Team Edition binary is then replaced by the Enterprise Edition version. Once this process is complete, you're prompted to restart your server.

The Mattermost version listed in **Product menu > System Console > Edition and License** will change from **Team Edition** to **Enterprise Edition**, and you can now activate an Enterprise Edition trial or upload a license.

Permissions and limitations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're using a package manager to manage your Mattermost installation the Mattermost system user won't have sufficient permissions to perform the upgrade. If this is the case, you'll need to change the file permissions manually.

Changing the permissions in this way doesn't affect your Mattermost deployment or impact any data. The permission change is done solely for the upgrade.

To change the permissions using the command line on the Mattermost server, you need access to the command line tool as *mattermost* user. 
Open the command line tool on the Mattermost server and ``cd`` to the Mattermost installation directory. Run the following commands (replacing ``<PathToBinaryFile>`` with the appropriate path - typically ``/opt/mattermost/bin/mattermost``) to change the ownership of the binary file to *mattermost* user and grant write access:

.. code-block:: sh

  chown mattermost <PathToBinaryFile>
  chmod +w <PathToBinaryFile>

In the Mattermost System Console, retry the upgrade. When the upgrade is complete, return to the command prompt on the Mattermost server and run the following command to restore the file permissions, replacing ``<OriginalFileOwner>`` with the appropriate value:

.. code-block:: sh

  chown <OriginalFileOwner> <PathToBinaryFile>
  chmod -w <PathToBinaryFile>

Troubleshooting
~~~~~~~~~~~~~~~~

Mattermost has reverted to Team Edition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you converted Team Edition to Enterprise Edition on a managed deployment and then upgraded, the upgrade will have overwritten Enterprise Edition with the latest version of Team Edition.

You can convert to Enterprise Edition again by following the steps above. If you plan to use Mattermost Enterprise Edition permanently, we recommend migrating your server to a self-hosted one.

The manual process reset my file permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you manually changed your file permissions, you can change them back.

1. Open the command line tool on the Mattermost server.
2. ``cd`` to the Mattermost installation directory (typically ``/opt/mattermost/bin/mattermost``).
3. Enter: 

.. code-block:: sh
  
  chown <OriginalFileOwner> <PathToBinaryFile>
  chmod -w <PathToBinaryFile>

File permissions error
^^^^^^^^^^^^^^^^^^^^^^^

If your Mattermost deployment is part of a managed package you may receive file permissions errors and the upgrade will fail. You can edit the permissions settings manually:

1. Open the command line tool on the Mattermost server.
2. ``cd`` to the Mattermost installation directory (typically ``/opt/mattermost/bin/mattermost``).
3. Enter: 

.. code-block:: sh

  chown <OriginalFileOwner> <PathToBinaryFile>
  chmod -w <PathToBinaryFile>

Incompatible system architecture
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This tool is currently only compatible with Linux systems using x86-64 architecture. If you're running Mattermost on a different architecture, please follow the manual upgrade process.

Can't retrieve Enterprise Edition binary file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the upgrade fails due to file retrieval failure, unavailable binary, or connectivity error, please check your proxy settings and try again. If the problem persists, follow the manual upgrade process instead.

GitLab Omnibus Integration
--------------------------

Upgrading to Enterprise Edition in GitLab Omnibus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GitLab Omnibus runs the open source Mattermost Team Edition. To upgrade to Mattermost Enterprise Edition, follow these steps:

1. Disable the built-in Mattermost instance on GitLab Omnibus:

- Go to ``/etc/gitlab/gitlab.rb`` and set the following line to false:

.. code-block:: text

   mattermost['enable'] = false

- Then run the following command to apply the updated setting:

.. code-block::
  
  sudo gitlab-ctl reconfigure

2. Install Mattermost using one of the guides above.
3. Migrate the database used by GitLab Mattermost for your new Enterprise Edition instance.
4. (Optional) Set up `GitLab slash command integration <https://docs.gitlab.com/ee/user/project/integrations/mattermost_slash_commands.html>`_ with your Mattermost instance.

If you need to migrate Team Edition prior to install, :doc:`follow the migration guide </administration-guide/onboard/migrating-to-mattermost>`.

Troubleshooting GitLab Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GitLab-specific issues when upgrading from Team Edition to Enterprise Edition can occur due to the managed nature of GitLab Omnibus installations.

.. note::

  If you're using Mattermost in GitLab Omnibus and want to start an Enterprise Edition trial, you can use the built-in conversion tool. However if you plan to upgrade permanently and scale your production environment, we strongly recommend installing a new standalone server and following the appropriate :doc:`migration process </administration-guide/onboard/migrating-to-mattermost>`.

Automated updates or actions performed by other system admins after the conversion can overwrite the changes, possibly reverting the system to Team Edition. This includes the ``run gitlab-ctl configure`` command to update Mattermost within GitLab Omnibus. If this occurs, you won't be able to use Enterprise Edition features until converting the server back, but none of your data will be affected.
