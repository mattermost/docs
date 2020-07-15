..  _ee-install:

===========================================
Enterprise Install and Upgrade
===========================================

Mattermost Enterprise Edition is free to use in "team mode" without enterprise features enabled. There are two variants of Enterprise Edition, E10 and E20, and you can `compare their features online <https://mattermost.com/pricing-feature-comparison/>`__.

Once you've downloaded and installed Mattermost, start an Enterprise E20 trial via **Main Menu > System Console > Edition and License > Start trial**. You can view `pricing and feature information <https://mattermost.com/pricing/>`__ and purchase a `license key online <https://customers.mattermost.com/login/>`__.

Installing Enterprise Edition
-----------------------------

To install Mattermost Enterprise Edition directly please use one of the following guides:

* `Production Kubernetes Deployment <https://docs.mattermost.com/install/install-kubernetes.html>`__
* `Production Enterprise Edition on Ubuntu 16.04 <https://docs.mattermost.com/install/install-ubuntu-1604.html>`__
* `Production Enterprise Edition on Ubuntu 18.04 <https://docs.mattermost.com/install/install-ubuntu-1804.html>`__
* `Production Enterprise Edition on RHEL 7 <https://docs.mattermost.com/install/install-rhel-7.html>`__
* `Production Enterprise Edition on RHEL 6 <https://docs.mattermost.com/install/install-rhel-6.html>`__
* `Production Enterprise Edition on Debian Stretch <https://docs.mattermost.com/install/install-debian.html>`__
* `Production Docker Deployment using Docker Compose <https://docs.mattermost.com/install/prod-docker.html>`__

Upgrading to Mattermost Enterprise Edition
-------------------------------------------------

Checking your Mattermost Edition and Version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're already running Mattermost, you can check the Mattermost edition and version from the command line using:

  `mattermost version`

To check your edition and version from the web interface, open **Main Menu > About Mattermost**.

- **Mattermost Enterprise Edition** indicates you can apply a license key to enable enterprise features.
- **Mattermost Team Edition** indicates you're using the open source version and need to upgrade (per upgrade instructions below) before a license key can be applied.

Upgrading to Enterprise Edition from Mattermost Team Edition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The open source Mattermost Team Edition is functionally identical to the commercial Mattermost Enterprise Edition in its free "team mode", but there is no ability to unlock enterprise features.

To enable unlocking enterprise features, replace the Mattermost Team Edition binary with a Mattermost Enterprise Edition binary via an `upgrade procedure <http://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-to-enterprise-edition>`__.

If you'd like to back up Mattermost prior to upgrading, `the migration guide <https://docs.mattermost.com/administration/migrating.html#migrating-the-mattermost-server>`__  outlines the process required to back up and restore your database.

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

Upgrading Enterprise Edition to a Newer Version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Upgrade a previous version of Mattermost Enterprise Edition to a later version by following the `upgrade procedure <https://docs.mattermost.com/administration/upgrade.html#upgrade-enterprise-edition>`__.

Changing a License Key
----------------------

Make sure that the new license is for a number of users that is greater than or equal to the current total number of users on your system. To find the total number of users, go to **System Console > Reporting > Site Statistics**. The total number of users is in the **Total Active Users** field. The license is rejected if this value is greater than the value allowed by the key.

Installing a New License Key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Using the command line interface (CLI)**

Use this command to upload a new license or to replace an existing license with a new one.

.. code-block:: none

  mattermost license upload {license}

.. note::
  If you upload the license via the CLI using  `mattermost license upload`, you need to restart the Mattermost server after uploading. Additionally, if you're running a cluster, the license file needs to be uploaded to every node. See `our documentation for more information on the command line tools <https://docs.mattermost.com/administration/command-line-tools.html#mattermost-license-upload>`__.

**Using the System Console**

1. Open **System Console > About > Edition and License** (or **System Console > OTHER > Edition and License** in versions prior to 5.12).
2. Click **Remove Enterprise License and Downgrade Server**. This clears the license from the server and refreshes the System Console.
3. Upload the new license key file.

After the key is uploaded and installed, the details of your license are displayed.
