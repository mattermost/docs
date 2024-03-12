.. _user-provisoning:

Provisioning workflows
======================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

This document provides an overview of user provisioning and deprovisioning workflows in Mattermost.

User Provisioning
--------------------

There are currently three recommended user provisioning workflows in Mattermost:

1. **On demand:** If user accounts are not pre-provisioned using one of the methods described below, then a new user account will be provisioned when the user first logs in. When the user logs in, they are asked to select a public team to join (all users must belong to at least one team) and then they are added automatically to Town Square and Off-Topic channels. Mattermost also has a default channel setting that allows everyone to be added to additional channels specified by the organization.
2. **Pre-provisioned via bulk import:** Mattermost features a :doc:`bulk data loading tool </onboard/bulk-loading-data>` that can be used for pre-provisioning new users by adding them to teams and channels before their first login to Mattermost. This tool automates the creation of Teams, Channels, Users, and Posts (with file attachments). It can also be used to migrate users and content from an existing system.
3. **Mattermost API:** The Mattermost `RESTful API <https://api.mattermost.com>`__ can be used to pre-provision new user accounts as well as add and remove them from teams and channels. This model is commonly used by enterprises that have central account provisioning applications.

.. note::

  Mattermost plans to release a new feature in early 2019 that will enable organizations to synchronize users to teams and channels based on group membership.

Mattermost user identifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The user identifier used to uniquely identify users in Mattermost depends on the method of authentication:

- **Email/password**: Email address or username. Created by the user or previously described account pre-provisioning process.
- **AD/LDAP**: Configure a unique and unchanging ID Attribute from the AD/LDAP server to be used in Mattermost. If a user's ID Attribute changes, it will create a new Mattermost account unassociated with their old one.
- **SAML 2.0**: Selected during configuration. You may use an Id Attribute instead of email to bind the user. We recommend choosing an ID that is unique and will not change over time.

User deprovisioning
--------------------

Users in Mattermost can be deactivated in the following ways:

- **AD/LDAP Synchronization**: AD/LDAP users can be deactivated in Mattermost based on their status in the directory server via synchronization. Learn more in :ref:`AD/LDAP documentation <onboard/ad-ldap:how do i deactivate users?>`.
- **System Console**: User management screen in **System Console > Users** allows administrators to deactiveate users with email/password login.
- **RESTful API** The Mattermost API can be used to deactivate users. See `API documentation to learn more <https://api.mattermost.com/#operation/DeleteUser>`__.
- **Command Line Interface**: You can use the Mattermost :ref:`mmctl user deactivate <manage/mmctl-command-line-tool:mmctl user deactivate>` command to deactivate users.

Once deactivated, users still exist in the Mattermost database and their messages can still be viewed in Mattermost. You can use the :ref:`mmctl <manage/mmctl-command-line-tool:mmctl user delete>` tools to delete a user and all of their content.

.. note::

   As long as the ID attribute selected via AD/LDAP or SAML 2.0 is a unique identifier, the user’s email address or name (along with other attributes) can be updated without breaking the user’s account.
