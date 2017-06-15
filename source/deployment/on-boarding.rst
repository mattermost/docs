Administrator Tasks
===================

This document provides instructions for common administrator tasks.

DO NOT manipulate the Mattermost database
-----------------------------------------

  - In particular, DO NOT manually delete data from the database directly. Mattermost is designed as a continuous archive and cannot be supported after manual manipulation.
  - If you need to permanently delete a team or user, use the `Command Line Tool <../administration/command-line-tools.html>`_.

Migrating to AD/LDAP or SAML from email-based authentication
------------------------------------------------------------

If you have Enterprise Edition, you can migrate from email authentication to Active Directory/LDAP or to SAML Single Sign-on. To set up Active Directory/LDAP, see :doc:`sso-ldap`. To set up SAML Single Sign-on, see :doc:`sso-saml`.

After the new authentication method is enabled, existing users cannot use the new method until they go to **Account Settings > Security > Sign-in method** and click **Switch to using AD/LDAP** or **Switch to using SAML Single Sign-on**. After they have switched, they can no longer use their email and password to sign in.

Common Tasks
------------

Creating System Admin account from the command line
  - If the System Admin leaves the organization or is otherwise unavailable, you can use the command line interface to assign the *system_admin* role to an existing user. In the ``mattermost/bin`` directory, type ``sudo ./platform roles system_admin {user-name}``, where *{user-name}* is the username of the person with the new role. For more information about using the command line interface, see :doc:`../administration/command-line-tools`.
  - The user needs to log out and log back in before the *system_admin* role is applied.

Deactivating a user
  - System Admins can go to **System Console > Users** for a list of all users on the server. The list can be searched and filtered to make finding the user easier. Click the user's role and in the menu that opens, click **Deactivate**.
  - To preserve audit history, users are never deleted from the system. It is highly recommended that System Admins do not attempt to delete users manually from the database, as this may compromise system integrity and the ability to upgrade in the future.

Checking for a valid license in Enterprise Edition without logging in
  - Open the log file ``mattermost.log``. It's usually in the ``mattermost/logs/`` directory but might be elsewhere on your system. Find the last occurrence of a log entry that starts with the text ``[INFO] License key``. If the license key is valid, the complete line should be similar to the following example:

    .. code-block:: text

      [2017/05/19 16:51:40 UTC] [INFO] License key valid unlocking enterprise features.
