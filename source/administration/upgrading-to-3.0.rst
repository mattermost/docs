Upgrading to version 3.0
========================

Use these instructions if you are upgrading from 2.0.0, 2.1.0, or 2.2.0. If you are upgrading from a version earlier than 2.0.0, you must first `upgrade to version 2.0 <../administration/upgrading-to-2.0.html>`__. 

You must upgrade to 3.0 before upgrading to the latest version of Mattermost.

Introduction
------------

If your Mattermost server contains more than one team, you need to understand the 3.0 upgrade process in detail and take special steps to upgrade successfully.

Before version 3.0, users needed a separate account for each team that they joined. Starting in version 3.0, users can have only one account, and that account is used across all teams.

This means that you must decide which of the teams on the server will be the **primary team**, and your users must take steps after the upgrade to consolidate their various accounts into one.

Username and email address changes
  During the upgrade, the database is migrated to the new design. The primary team is migrated first, and then the other teams are migrated. When a duplicate account is found, it is modified to ensure that all accounts in the system are unique. A duplicate account is an account that has either the same username or the same email address as an account in the primary team.

Duplicate usernames
  An account with a duplicate username is changed by prepending a string based on the team name to the username. For example, the user *steve* on the *Marketing* team becomes *marketing.steve*.

Duplicate email addresses
  An account with a duplicate email address is changed by adding a string based on the team name to the local part of the email address. For example, the email address of *steve@example.com* on the *Marketing* team becomes *steve+marketing@example.com*.

Users with accounts containing duplicate emails or usernames will receive a notification email explaining the upgrade, and instructions on how to move to a single user account.

**Before you begin**

Read these instructions carefully from start to finish. Make sure that you understand each step before starting the upgrade. If you have questions or concerns, you can ask on the Mattermost forum at https://forum.mattermost.org/.

You should gather the following information before starting the upgrade:

Existing install directory - *{install-path}*
  If you don't know where Mattermost Server is installed, use the ``whereis platform`` command. The output should be similar to */opt/mattermost/bin/platform*. The install directory is everything before the last occurrence of the string */mattermost*. In this example, the *{install-path}* is ``/opt``.
Location of your local storage directory
  The local storage directory contains all the files that users have attached to their messages. If you don't know its location, open the System Console and go to **Files > Storage** and read the value in **Local Storage Directory**. Relative paths are relative to the ``mattermost`` directory. For example, if the local storage directory is ``./data/`` then the absolute path is ``{install-path}/mattermost/data``.
Owner and group of the install directory - *{owner}* and *{group}*
  Use the ``ls -l {install-path}/mattermost/bin/platform`` command to get the owner and group.

**Upgrading to version 3.0**

1. Read the following post in the Mattermost forum which describes the steps that were taken to ensure success when upgrading to version 3.0. `Mattermost 3.0 upgrade example <https://forum.mattermost.org/t/mattermost-3-0-upgrade-example/1541>`__

2. In a terminal window on the server that hosts Mattermost Server, change to your home directory. If any, delete files and directories that might still exist from a previous download.

  ``cd ~``

3. Download version 3.0.3.

  ``wget https://releases.mattermost.com/3.0.3/mattermost-enterprise-3.0.3-linux-amd64.tar.gz``

4. Extract the Mattermost Server files.

  ``tar -xzf mattermost*.gz``

5. Stop Mattermost Server.

  On Ubuntu 14.04 and RHEL 6: ``sudo service mattermost stop``

  On Ubuntu 16.04 and RHEL 7: ``sudo systemctl stop mattermost``

6. Back up your data and application.
  a. Back up your database using your organization’s standard procedures for backing up MySQL or PostgreSQL.
  b. Back up your application by moving into your archive folder (e.g. ``mattermost-back-YYYY-MM-DD``).

    ``mv {install-path}/mattermost {install-path}/{mattermost-back-YYYY-MM-DD}``

7. Copy the files that you extracted earlier to the install directory.

  ``sudo cp -r mattermost {install-path}``

8. Restore your configuration, local file storage and logs.

  .. code-block:: text

    sudo cp -r {install-path}/{mattermost-back-YYYY-MM-DD}/config {install-path}/mattermost
    sudo cp -r {install-path}/{mattermost-back-YYYY-MM-DD}/data {install-path}/mattermost
    sudo cp -r {install-path}/{mattermost-back-YYYY-MM-DD}/logs {install-path}/mattermost

9. Change ownership of the new files.

  ``sudo chown -R {owner}:{group} {install-path}/mattermost``

10. Upgrade the database.
  a. Change to the Mattermost bin directory

    ``cd {install-path}/mattermost/bin``

  b. Run the database upgrade script

    ``sudo -u {owner} ./platform -upgrade_db_30``

  c. When prompted, enter the name of the team that you want to use as the primary team.

11. Start Mattermost server.

  On Ubuntu 14.04 and RHEL 6: ``sudo service mattermost start``

  On Ubuntu 16.04 and RHEL 7: ``sudo systemctl start mattermost``

12. Upgrade your ``config.json`` schema: Open the System Console and make a change and then save the change. Your current settings are preserved, and new settings are added with default values.

13. If you have TLS set up on your Mattermost server, you must activate the CAP_NET_BIND_SERVICE capability to allow the new Mattermost binary to bind to low ports.

  .. code-block:: text

    cd {install-path}
    sudo setcap cap_net_bind_service=+ep ./bin/platform
