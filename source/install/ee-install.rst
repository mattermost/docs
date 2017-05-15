..  _ee-install:

===========================================
Enterprise Install and Upgrade
===========================================

Mattermost Enterprise Edition is free to use in "team mode" without enterprise features enabled. Enable enteprise features using a `trial license <https://about.mattermost.com/trial/>`_ or by `purchasing a license key <https://about.mattermost.com/pricing/>`_. There are two variants of Enterprise Edition, E10 and E20, and you can `compare their features online <https://about.mattermost.com/features/>`_.

Installing Enterprise Edition
-----------------------------

To install Mattermost Enterprise Edition directly please use one of the following guides:

1. `Production Enterprise Edition on Ubuntu 14.04 <http://docs.mattermost.com/install/ee-prod-ubuntu.html>`_
2. `Production Enterprise Edition on Ubuntu 16.04 <https://docs.mattermost.com/install/ee-prod-ubuntu-1604.html>`_
3. `Production Enterprise Edition on RHEL 7.1 <http://docs.mattermost.com/install/ee-prod-rhel-7.html>`_
4. `Production Enterprise Edition on RHEL 6.6 <http://docs.mattermost.com/install/ee-prod-rhel-6.html>`_
5. `Production Enterprise Edition on Docker using Docker Compose <https://docs.mattermost.com/install/prod-docker.html#production-docker-on-ubuntu-with-enterprise-edition>`_

Upgrading to Mattermost Enterprise Edition
-------------------------------------------------

Checking your Mattermost Edition and Version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you're already running Mattermost, to check your Mattermost edition and version from the server run:

  `platform version`

To check your edition and version from the web interface, go to the main menu and open the "About Mattermost" dialog.

- "Mattermost Enterprise Edition" indicates your system is ready to receive a license key to enable enterprise features.
- "Mattermost Team Edition" indicates you're using the open source version and need to upgrade (per upgrade instructions below) before a license key can be applied.

Upgrading to Enterprise Edition from Mattermost Team Edition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- The open source Mattermost Team Edition is functionally identical to the commercial Mattermost Enterprise Edition in its free "team mode", but there is no ability to unlock enterprise features.
- To enable the unlocking of enterprise features, replace the Mattermost Team Edition binary with a Mattermost Enterprise Edition binary via an `upgrade procedure <http://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-to-enterprise-edition>`_.

If you need to migrate Team Edition prior to install, `please follow the migration guide. <http://docs.mattermost.com/administration/migrating.html>`_

Upgrading Enterprise Edition to a newer version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Upgrade previous version of Mattermost Enterprise Edition to later versions by following the `upgrade procedure. <https://docs.mattermost.com/administration/upgrade.html#upgrade-enterprise-edition>`_

Changing a License Key
----------------------

Make sure that the new license is for a number of users that is greater than or equal to the current total number of users on your system. To find the total number of users, go to the REPORTING section of the System Console and click **Site Statistics**. The total number of users is in the **Total Users** field. The license is rejected if this value is greater than allowed by the key.

**To install a new license key**:

1. In the OTHER section of the System Console, click **Edition and License**. The *Edition and License* page opens.
2. Click **Remove Enterprise License and Downgrade Server**. This clears the license from the server and refreshes the System Console.
3. Upload the new license key file.

After the key is uploaded and installed, the **Edition** and **License** sections on the page show the capabilities of your new license key.
