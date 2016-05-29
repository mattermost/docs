..  _ee-install:

Enterprise Edition Installation
===============================

Enterprise Edition can be installed either directly or via upgrade from Team Editon.

Installing Enterprise Edition 
---------------

To install Mattermost Enterprise Edition directly please use one of the following guides: 

1. `Production Enterprise Edition on Ubunutu 14 <http://docs.mattermost.com/install/ee-prod-ubuntu.html>`_
2. `Production Enterprise Edition on RHEL 7.1 <http://docs.mattermost.com/install/ee-prod-rhel-7.html>`_
3. `Production Enterprise Edition on RHEL 6.6 <http://docs.mattermost.com/install/ee-prod-rhel-6.html>`_

Upgrading to Enterprise Edition from Mattermost Team Edition 
---------------

1. Follow the procedure to `upgrade Team Edition to Enterprise Edition. <http://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-to-enterprise-edition>`_

If you need to migrate Team Edition prior to install, `please follow the migration guide. <http://docs.mattermost.com/administration/migrating.html>`_

Changing a License Key
----------------------

To change an existing license key on an Enterprise Edition server to a new license key:

1. In the **System Console**, go to **OTHER** > **Edition and License** > **License Key** and click "Remove Enterprise License and Downgrade Server". This clears the license from the server and refreshes the System Console. 
2. In the **System Console**, go to **OTHER** > **Edition and License** > **License Key** and upload the new license key file.
   
The **Edition** and **License** sections on the page should update to show the capabilities of your new license key. 

