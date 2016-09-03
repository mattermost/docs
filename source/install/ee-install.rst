..  _ee-install:

Enterprise Install and Upgrade 
===========================================

Mattermost Enterprise Edition is free to use in "team mode" without enterprise features enabled. Enable enteprise features using a `trial license <https://about.mattermost.com/trial/>`_ or by `purchasing a license key <https://about.mattermost.com/pricing/>`_. 

- `Compare Mattermost Enterprise Edition features <https://about.mattermost.com/features/>`_
- `Request a trial license <https://about.mattermost.com/trial/>`_
- `Purchase a license key <https://about.mattermost.com/pricing/>`_

Installing Enterprise Edition 
---------------

To install Mattermost Enterprise Edition directly please use one of the following guides: 

1. `Production Enterprise Edition on Ubunutu 14 <http://docs.mattermost.com/install/ee-prod-ubuntu.html>`_
2. `Production Enterprise Edition on RHEL 7.1 <http://docs.mattermost.com/install/ee-prod-rhel-7.html>`_
3. `Production Enterprise Edition on RHEL 6.6 <http://docs.mattermost.com/install/ee-prod-rhel-6.html>`_
4. `Production Enterprise Edition on Docker using Docker Compose <https://docs.mattermost.com/install/prod-docker.html#production-docker-on-ubuntu-with-enterprise-edition>`_


Upgrading Enterprise Edition to a newer version
---------------

- Upgrade previous version of Mattermost Enterprise Edition to later versions by following the `upgrade procedure. <https://docs.mattermost.com/administration/upgrade.html#upgrade-enterprise-edition>`_

Upgrading to Enterprise Edition from Mattermost Team Edition 
---------------

- The open source Mattermost Team Edition is functionally identical to the commercial Mattermost Enterprise Edition in its free "team mode", but there is no ability to unlock enterprise features.
- To enable the unlocking of enterprise features, replace the Mattermost Team Edition binary with a Mattermost Enterprise Edition binary via an `upgrade procedure <http://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-to-enterprise-edition>`_.

If you need to migrate Team Edition prior to install, `please follow the migration guide. <http://docs.mattermost.com/administration/migrating.html>`_

Changing a License Key
----------------------

To change an existing license key on an Enterprise Edition server to a new license key:

1. In the **System Console**, go to **OTHER** > **Edition and License** > **License Key** and click "Remove Enterprise License and Downgrade Server". This clears the license from the server and refreshes the System Console. 
2. In the **System Console**, go to **OTHER** > **Edition and License** > **License Key** and upload the new license key file.
   
The **Edition** and **License** sections on the page should update to show the capabilities of your new license key. 

