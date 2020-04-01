..  _ee-install:

===========================================
Enterprise Install and Upgrade
===========================================

Mattermost Enterprise Edition is free to use in "team mode" without enterprise features enabled. Enable enterprise features using a `trial license <https://about.mattermost.com/trial/>`__ or by `purchasing a license key <https://about.mattermost.com/pricing/>`__. There are two variants of Enterprise Edition, E10 and E20, and you can `compare their features online <https://mattermost.com/pricing-feature-comparison/>`__.

Installing Enterprise Edition
-----------------------------

To install Mattermost Enterprise Edition directly please use one of the following guides:

1. `Production Enterprise Edition on Ubuntu 16.04 <https://docs.mattermost.com/install/install-ubuntu-1604.html>`__
2. `Production Enterprise Edition on Ubuntu 18.04 <https://docs.mattermost.com/install/install-ubuntu-1804.html>`__
3. `Production Kubernetes Deployment <https://docs.mattermost.com/install/install-kubernetes.html>`__
4. `Production Enterprise Edition on RHEL 7 <https://docs.mattermost.com/install/install-rhel-7.html>`__
5. `Production Enterprise Edition on RHEL 6 <https://docs.mattermost.com/install/install-rhel-6.html>`__
6. `Production Enterprise Edition on Debian Stretch <https://docs.mattermost.com/install/install-debian.html>`__
7. `Production Docker Deployment using Docker Compose <https://docs.mattermost.com/install/prod-docker.html>`__

Upgrading to Mattermost Enterprise Edition
-------------------------------------------------

Checking your Mattermost Edition and Version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're already running Mattermost, to check your Mattermost edition and version from the server run:

  `mattermost version`

To check your edition and version from the web interface, go to the main menu and open the "About Mattermost" dialog.

- "Mattermost Enterprise Edition" indicates your system is ready to receive a license key to enable enterprise features.
- "Mattermost Team Edition" indicates you're using the open source version and need to upgrade (per upgrade instructions below) before a license key can be applied.

Upgrading to Enterprise Edition from Mattermost Team Edition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- The open source Mattermost Team Edition is functionally identical to the commercial Mattermost Enterprise Edition in its free "team mode", but there is no ability to unlock enterprise features.
- To enable the unlocking of enterprise features, replace the Mattermost Team Edition binary with a Mattermost Enterprise Edition binary via an `upgrade procedure <http://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-to-enterprise-edition>`__.

If you need to migrate Team Edition prior to install, `please follow the migration guide. <http://docs.mattermost.com/administration/migrating.html>`__

Upgrading to Enterprise Edition in GitLab Omnibus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GitLab Omnibus runs the open source Mattermost Team Edition. To upgrade to Mattermost Enterprise Edition, follow these steps:

1. Disable the built-in Mattermost instance on GitLab Omnibus:

 - Go to ``/etc/gitlab/gitlab.rb`` and set the following line to false

   .. code-block:: text

    mattermost['enable'] = false

 - Run `sudo gitlab-ctl reconfigure` to apply the updated setting

2. Install Mattermost using `one of the guides above <https://docs.mattermost.com/install/ee-install.html#installing-enterprise-edition>`__.
3. Migrate the database used by GitLab Mattermost for your new Enterprise Edition instance.
4. (Optional) Set up `GitLab slash command integration <https://docs.gitlab.com/ee/user/project/integrations/mattermost_slash_commands.html>`__ with your Mattermost instance.

If you need to migrate Team Edition prior to install, `please follow the migration guide. <http://docs.mattermost.com/administration/migrating.html>`__

Upgrading Enterprise Edition to a newer version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Upgrade previous version of Mattermost Enterprise Edition to later versions by following the `upgrade procedure. <https://docs.mattermost.com/administration/upgrade.html#upgrade-enterprise-edition>`__

Changing a License Key
----------------------

Make sure that the new license is for a number of users that is greater than or equal to the current total number of users on your system. To find the total number of users, go to the REPORTING section of the System Console and click **Site Statistics**. The total number of users is in the **Total Active Users** field. The license is rejected if this value is greater than allowed by the key.

To install a new license key:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Through the command line interface (CLI):**

Use this command to upload a new license or to replace an existing license with a new one.

.. code-block:: none

  mattermost license upload {license}

.. note::
  If you upload the license via `mattermost license upload` CLI, you need to restart the Mattermost server after uploading. Also, if you're running a cluster setup, the license file needs to be uploaded to every node.


See `documentation for more information on the command line tools <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-license-upload>`__.

**Through the System Console:**

1. In the OTHER section of the System Console, click **Edition and License** in prior versions or **System Console** > **About** > **Edition and License** in versions after 5.12.
2. Click **Remove Enterprise License and Downgrade Server**. This clears the license from the server and refreshes the System Console.
3. Upload the new license key file.

After the key is uploaded and installed, the **Edition** and **License** sections on the page show the capabilities of your new license key.
