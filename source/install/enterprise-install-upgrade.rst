..  _ee-install:

Enterprise Install and Upgrade
===============================

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Mattermost Enterprise Edition is free to use in "team mode" without Enterprise features enabled. Mattermost offers two subscription plans, including Professional and Enterprise. You can `compare their features online <https://mattermost.com/pricing-feature-comparison/>`__.

Once you've downloaded and installed Mattermost, start an Enterprise trial via **Main Menu > System Console > Edition and License > Start trial**. You can view `pricing and feature information <https://mattermost.com/pricing/>`__ and purchase a `license key online <https://customers.mattermost.com/login/>`__.

Installing Enterprise Edition
-----------------------------

To install Mattermost Enterprise Edition directly please use one of the following guides:

* `Production Kubernetes Deployment <https://docs.mattermost.com/install/install-kubernetes.html>`__
* `Production Enterprise Edition on Ubuntu 18.04 <https://docs.mattermost.com/install/install-ubuntu-1804.html>`__
* `Production Enterprise Edition on RHEL 7 <https://docs.mattermost.com/install/install-rhel-7.html>`__
* `Production Enterprise Edition on RHEL 8 <https://docs.mattermost.com/install/install-rhel-8.html>`__
* `Production Enterprise Edition on Debian Stretch <https://docs.mattermost.com/install/install-debian.html>`__
* `Production Enterprise Edition using Docker and Docker Compose <https://github.com/mattermost/docker>`__

Upgrading to Mattermost Enterprise Edition
--------------------------------------------

Checking your Mattermost Edition and Version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're already running Mattermost v5.39 or earlier, you can check the Mattermost edition and version from the command line using:

`mattermost version`

To check your edition and version from the web or desktop interface, open **Main Menu > About Mattermost**.

- **Mattermost Enterprise Edition** indicates you can apply a license key to enable Enterprise features.
- **Mattermost Team Edition** indicates you're using the open source version and need to upgrade (per upgrade instructions below) before a license key can be applied.

Upgrading to Enterprise Edition from Mattermost Team Edition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The open source Mattermost Team Edition is functionally identical to the commercial Mattermost Enterprise Edition in its free "team mode", but there is no ability to unlock Enterprise features.

To enable unlocking Enterprise features, replace the Mattermost Team Edition binary with a Mattermost Enterprise Edition binary via an `upgrade procedure <https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html>`__.

If you'd like to back up Mattermost prior to upgrading, `the migration guide <https://docs.mattermost.com/onboard/migrating-to-mattermost.html>`__  outlines the process required to back up and restore your database.

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

2. Install Mattermost using `one of the guides above <https://docs.mattermost.com/install/ee-install.html#installing-enterprise-edition>`__.
3. Migrate the database used by GitLab Mattermost for your new Enterprise Edition instance.
4. (Optional) Set up `GitLab slash command integration <https://docs.gitlab.com/ee/user/project/integrations/mattermost_slash_commands.html>`__ with your Mattermost instance.

If you need to migrate Team Edition prior to install, `please follow the migration guide <https://docs.mattermost.com/onboard/migrating-to-mattermost.html>`__.

Upgrading Enterprise Edition to a Newer Version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upgrade a previous version of Mattermost Enterprise Edition to a later version by following the `upgrade procedure <https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html>`__.

Converting Team Edition to Enterprise Edition
----------------------------------------------

From Mattermost v5.27 on, if you're running a Linux system with x86-64 architecture, you can convert Team Edition to Enterprise in the System Console using a built-in conversion utility. This tool is recommended if you'd like to run an Enterprise trial or want to upgrade to Enterprise or Professional on standalone servers.

.. note::

  * If you're using Mattermost in a managed environment, such as GitLab Omnibus, and want to start an Enterprise Edition trial, you can use this tool. However if you plan to upgrade permanently and scale your production environment, we strongly recommend installing a new standalone server and following the appropriate `migration process <https://docs.mattermost.com/onboard/migrating-to-mattermost.html>`_.
  * If you're using a modified version of Mattermost, using this tool will overwrite your changes and replace them with the official Enterprise Edition binary.
  * For versions prior to v5.27, please follow `these upgrade instructions <https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html#upgrading-team-edition-to-enterprise-edition>`_.

Navigate to **System Console > Edition and License** and select **Upgrade to Enterprise Edition**.

During the upgrade process, the Mattermost Enterprise Edition binary file that matches your current server version is downloaded, decompressed, and extracted. The Team Edition binary is then replaced by the Enterprise Edition version. Once this process is complete, you're prompted to restart your server.

The Mattermost version listed in **System Console > Edition and License** will change from **Team Edition** to **Enterprise Edition**, and you can now activate an Enterprise Edition trial or upload a license.

Permissions and Limitations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're using a package manager, such as GitLab Omnibus, to manage your Mattermost installation the Mattermost system user won't have sufficient permissions to perform the upgrade. If this is the case, you'll need to change the file permissions manually.

Changing the permissions in this way doesn't affect your Mattermost deployment or impact any data. The permission change is done solely for the upgrade.

To change the permissions using the command line on the Mattermost server, you need access to the command line tool as *mattermost* user. 
Open the command line tool on the Mattermost server and ``cd`` to the Mattermost installation directory. Run the following commands (replacing ``<PathToBinaryFile>`` with the appropriate path - typically ``/opt/mattermost/bin/mattermost``) to change the ownership of the binary file to *mattermost* user and grant write access:

.. code-block:: none

  chown mattermost <PathToBinaryFile>
  chmod +w <PathToBinaryFile>

In the Mattermost System Console, retry the upgrade. When the upgrade is complete, return to the command prompt on the Mattermost server and run the following command to restore the file permissions, replacing ``<OriginalFileOwner>`` with the appropriate value:

.. code-block:: none

  chown <OriginalFileOwner> <PathToBinaryFile>
  chmod -w <PathToBinaryFile>

Note that automated updates or actions performed by other System Admins after the conversion can overwrite the changes, possibly reverting the system to Team Edition. This includes the ``run gitlab-ctl configure`` command to update Mattermost within GitLab Omnibus. If this occurs, you won't be able to use Enterprise Edition features until converting the server back, but none of your data will be affected.

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

.. code-block:: none
  
  chown <OriginalFileOwner> <PathToBinaryFile>
  chmod -w <PathToBinaryFile>

File permissions error
^^^^^^^^^^^^^^^^^^^^^^^

If your Mattermost deployment is part of a managed package you may receive file permissions errors and the upgrade will fail. You can edit the permissions settings manually:

1. Open the command line tool on the Mattermost server.
2. ``cd`` to the Mattermost installation directory (typically ``/opt/mattermost/bin/mattermost``).
3. Enter: 

.. code-block:: none

  chown <OriginalFileOwner> <PathToBinaryFile>
  chmod -w <PathToBinaryFile>

Incompatible system architecture
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This tool is currently only compatible with Linux systems using x86-64 architecture. If you’re running Mattermost on a different architecture, please follow the manual upgrade process.

Can’t retrieve Enterprise Edition binary file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the upgrade fails due to file retrieval failure, unavailable binary, or connectivity error, please check your proxy settings and try again. If the problem persists, follow the manual upgrade process instead.
