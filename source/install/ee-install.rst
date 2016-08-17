..  _ee-install:

Enterprise Edition Installation and Upgrade
===========================================

Enterprise Edition and Team Edition are nearly identical in installation and upgrade, except for two differences: 

1. Enterprise Edition offers enterprise features when unlocked with a license key. 

   A list of `enterprise features <https://about.mattermost.com/pricing/>`_ available with subscription can be found online. 

2. The Enterprise Edition and Team Edition are different binary files. 

   Follow the instructions below to install or upgrade to the correct edition. 
   
Enterprise Edition without a license key is largely identical to Team Editon. If you think you might want to use Enterprise Edition at some point, whether via `trial license <https://about.mattermost.com/trial/>`_ or with `a subscription <https://about.mattermost.com/pricing/>`_, it's easiest to install the Enterprise Edition. Should you decide not to purchase, you can continue using Enteprise Edition without enterprise features for free. 

Installing Enterprise Edition 
---------------

To install Mattermost Enterprise Edition directly please use one of the following guides: 

1. `Production Enterprise Edition on Ubunutu 14 <http://docs.mattermost.com/install/ee-prod-ubuntu.html>`_
2. `Production Enterprise Edition on RHEL 7.1 <http://docs.mattermost.com/install/ee-prod-rhel-7.html>`_
3. `Production Enterprise Edition on RHEL 6.6 <http://docs.mattermost.com/install/ee-prod-rhel-6.html>`_

Upgrading Enterprise Edition to a newer version
---------------

1. Follow the procedure to `upgrade Enterprise Edition to a newer version. <https://docs.mattermost.com/administration/upgrade.html#upgrade-enterprise-edition>`_

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

