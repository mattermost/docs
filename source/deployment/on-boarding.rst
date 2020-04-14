Administrator Tasks
===================

This document provides instructions for common administrator tasks, including some recommendations on tasks to prepare your Mattermost instance to onboard users.

Getting Started Tasks
-----------------------
1. Once you've installed and deployed Mattermost, ensure all configuration settings are appropriately set under **System Console > Environment** including: 
 - Web Server
 - Database
 - File Storage
 - SMTP
 - Push Notification Server 
  
These settings can also be set in the ``config.json`` file. Please see our `configuration settings documentation <https://docs.mattermost.com/administration/config-settings.html>`__ for a full listing of all configuration settings. 

2. Adjust settings under **System Console > Site Configuration** to brand and customize how users will interact with the site.  
Be sure to update the Support Email and Help Link in Mattermost under **System Console > Site Configuration > Customization** to provide your users a resource for password resets or questions on their Mattermost account.

 - The Support Email is used on email notifications and during tutorial for users to ask support questions.
 - The Help Link is on the Mattermost login page, sign-up pages, and Main Menu and can be used to to link to your help desk ticketing system.  
 
These settings can also be set in the ``config.json`` file.  Please see our `configuration settings documenation <https://docs.mattermost.com/administration/config-settings.html>`__ for a full listing of all configuration settings.  

3. Begin to onboard users by enabling account creation or by connecting an authentication service to assist with user provisioning.  

 - Users can be pre-provisioned with migration and bulk loading data processes based on prior collaboration systems. Please see our `migration guide <https://docs.mattermost.com/administration/migrating.html#migration-guide>`_ and `bulk loading documentation <https://docs.mattermost.com/deployment/bulk-loading.html>`_ for additional details.
 - `AD/LDAP authentication <https://docs.mattermost.com/deployment/sso-ldap.html#active-directory-ldap-setup-e10-e20>`_ and `SAML authentication <https://docs.mattermost.com/deployment/sso-saml.html>`_ are available for Enterprise Edition, providing identity management, single sign-on, and automatic account provisioning.   

4. Enable integrations and plugins to connect your team's workflows and toolsets into Mattermost. 

 - To enable integrations such as webhooks, slash commands, OAuth2.0, and bots, to go **System Console > Integrations**. More information on these integrations can be found `here <https://docs.mattermost.com/guides/integration.html>`_. 
 - To enable and manage plugins, go to **System Console > Plugins**.  Mattermost offers an `integration marketplace <https://integrations.mattermost.com/>`_ where you can see all available plugins available for upload. 

If your organization requires more structure and project management artifacts for the implementation of Mattermost, please see our `Enterprise roll out checklist <https://docs.mattermost.com/getting-started/enterprise-roll-out-checklist.html>`__.

Important Administration Notes 
------------------------------
**DO NOT manipulate the Mattermost database**

 - In particular, DO NOT manually delete data from the database directly. Mattermost is designed as a continuous archive and cannot be supported after manual manipulation.
 - If you need to permanently delete a team or user, use the `Command Line Tool <https://docs.mattermost.com/administration/command-line-tools.html>`__.

Common Tasks
------------

**Creating System Admin account from the command line**
 - If the System Admin leaves the organization or is otherwise unavailable, you can use the command line interface to assign the *system_admin* role to an existing user. In the ``/opt/mattermost`` directory, type ``sudo -u mattermost bin/mattermost roles system_admin {user-name}``, where *{user-name}* is the username of the person with the new role. For more information about using the command line interface, see `Command Line Tools <https://docs.mattermost.com/administration/command-line-tools.html>`_.
 - The user needs to log out and log back in before the *system_admin* role is applied.
  
**Migrating to AD/LDAP or SAML from email-based authentication**
 - If you have Enterprise Edition, you can migrate from email authentication to Active Directory/LDAP or to SAML Single Sign-on. To set up Active Directory/LDAP, see `Active Directory/LDAP Setup (E10/E20) <https://docs.mattermost.com/deployment/sso-ldap.html#active-directory-ldap-setup-e10-e20>`_. To set up SAML Single Sign-on, see `SAML Single-Sign-On (E20) <https://docs.mattermost.com/deployment/sso-saml.html>`_.
 - After the new authentication method is enabled, existing users cannot use the new method until they go to **Account Settings > Security > Sign-in method** and click **Switch to using AD/LDAP** or **Switch to using SAML Single Sign-on**. After they have switched, they can no longer use their email and password to sign in.  

**Deactivating a user**
 - System Admins can go to **System Console > Users** for a list of all users on the server. The list can be searched and filtered to make finding the user easier. Click the user's role and in the menu that opens, click **Deactivate**.
 - To preserve audit history, users are typically never deleted from the system. If permanently deleting a user is necessary (e.g. for the purposes of `GDPR <https://gdpr-info.eu/>`__), a `CLI tool <https://docs.mattermost.com/administration/command-line-tools.html>`_ can be used to do so.
 - Note that AD/LDAP user accounts cannot be deactivated from Mattermost; they must be deactivated from your Active Directory.

**Checking for a valid license in Enterprise Edition without logging in**
 - Open the log file ``mattermost.log``. It's usually in the ``mattermost/logs/`` directory but might be elsewhere on your system. Find the last occurrence of a log entry that starts with the text ``[INFO] License key``. If the license key is valid, the complete line should be similar to the following example:

    .. code-block:: text

      [2017/05/19 16:51:40 UTC] [INFO] License key valid unlocking enterprise features.
      
**Upgrading Mattermost**
 - Mattermost releases updates monthly to `Mattermost Team Edition <https://mattermost.com/>`_ and `Mattermost Enterprise Edition <https://about.mattermost.com/pricing/>`_. The `Mattermost Changelog <https://docs.mattermost.com/administration/changelog.html>`_ provides all information about changes in each version. We recommend servers be upgraded often to keep up with critical bug fixes and security fixes. 
 - Follow the steps outlined in the `upgrade documentation <https://docs.mattermost.com/administration/upgrade.html>`_ to perform upgrades.   
