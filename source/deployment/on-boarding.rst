Administrator Tasks
-------------------
This document provides instructions for common administrator tasks.

**DO NOT manipulate the Mattermost database**
=============================================
  - In particular, DO NOT manually delete data from the database directly. Mattermost is designed as a continuous archive and cannot be supported after manual manipulation.
  - If you need to permanently delete a team or user please use the `Command Line Tool <http://docs.mattermost.com/administration/command-line-tools.html>`_.

Migrating to AD/LDAP or SAML from email-based authentication
============================================================

If you've evaluated Mattermost using email authentication and decide to deploy broadly using Active Directory/LDAP or SAML Single Sign-On, you can follow this procedure:

1. `Set up Active Directory/LDAP <http://docs.mattermost.com/deployment/sso-ldap.html>`_ or `SAML Single Sign-On <http://docs.mattermost.com/deployment/sso-saml.html>`_ for all users who would optionally have access to the system.
2. Post an announcement about how the migration will work to users.
3. Users who do not yet have an account on Mattermost will have a new account created when they sign in using their AD/LDAP or SAML credentials after the authentication method is enabled.
4. Users who use email-based authentication can change their sign-in method to AD/LDAP or SAML via **Account Settings** > **Security** > **Sign-in method**.
5. If someone attempts to sign-in with AD/LDAP or SAML with an email matching that of an existing account, they'll get an error message and will need to switch sign-in methods per procedure in 4.

Common Tasks
============

Creating System Admin account from the command line
  - If the System Admin leaves the organization or is otherwise unavailable, you can use the command line interface to assign the *system_admin* role to an existing user. In the ``mattermost/bin`` directory, type ``sudo ./platform roles system_admin {user-name}``, where *{user-name}* is the username of the person with the new role. For more information about using the command line interface, see :doc:`../administration/command-line-tools` .
  - After assigning the role the user needs to log out and log back in before the *system_admin* role is applied.

Deactivating a user
  - System Admins can go to **System Console** > **Teams**, and select a team to manage. From there they can go to the **Users** page for a team and manage roles.
  - To preserve audit history, users are never deleted from the system. It is highly recommended that System Administrators do not attempt to delete users manually from the database, as this may compromise system integrity and ability to upgrade in the future.
