Downgrading Mattermost Server
=============================

In most cases you can downgrade Mattermost Server using the same steps as :doc:`upgrading-mattermost-server`. The binaries can be found in the :doc:`version-archive`. We do not recommend downgrading more than one version back from your current installation.

Downgrade from 5.0 to 4.10
---------------------------

During the version 5.0 upgrade process, a migration is run to enable new features of the `advanced permissions system <https://docs.mattermost.com/onboard/advanced-permissions.html>`__. This changes the database in ways that result in it no longer being compatible with Mattermost server 4.10. If you need to downgrade from 5.0 or later to 4.10, it is necessary to follow the steps below.

You should gather the following information before starting the upgrade:

Existing install directory - *{install-path}*
  If you don't know where Mattermost Server is installed, use the ``whereis mattermost`` command. The output should be similar to */opt/mattermost/bin/mattermost*. The install directory is everything before the last occurrence of the string */mattermost*. In this example, the *{install-path}* is ``/opt``.
Location of your local storage directory
  The local storage directory contains all the files that users have attached to their messages. If you don't know its location, open the System Console and go to **Files > Storage** and read the value in **Local Storage Directory**. Relative paths are relative to the ``mattermost`` directory. For example, if the local storage directory is ``./data/`` then the absolute path is ``{install-path}/mattermost/data``.
Owner and group of the install directory - *{owner}* and *{group}*
  Use the ``ls -l {install-path}/mattermost/bin/mattermost`` command to get the owner and group.

#. In a terminal window on the server that hosts Mattermost Server, change to your home directory. If any, delete files and directories that might still exist from a previous download.

   .. code-block:: sh

     cd ~

#. Stop Mattermost server.

   On Ubuntu 14.04 and RHEL 6:

   .. code-block:: sh

     sudo service mattermost stop

   On Ubuntu 16.04 and RHEL 7:

   .. code-block:: sh

     sudo systemctl stop mattermost
     
    
#. Back up your data and application.

   a. Back up your database using your organization’s standard procedures for backing up MySQL or PostgreSQL.

   b. Back up your application by copying into an archive folder (e.g. ``mattermost-back-YYYY-MM-DD-HH-mm``).

   .. code-block:: sh
    
      cd {install-path}
      sudo cp -ra mattermost/ mattermost-back-$(date +'%F-%H-%M')/
    

#. Connect to your database CLI and run the following SQL statements to revert the changes to the database made by the migration. The commands may take up to a few minutes to run on large installations.

    .. code-block:: sh

      UPDATE Teams SET SchemeId = NULL;
      UPDATE Channels SET SchemeId = NULL;

      UPDATE TeamMembers SET Roles = CONCAT(Roles, ' team_user'), SchemeUser = NULL where SchemeUser = true;
      UPDATE TeamMembers SET Roles = CONCAT(Roles, ' team_admin'), SchemeAdmin = NULL where SchemeAdmin = true;

      UPDATE ChannelMembers SET Roles = CONCAT(Roles, ' channel_user'), SchemeUser = NULL where SchemeUser = true;
      UPDATE ChannelMembers SET Roles = CONCAT(Roles, ' channel_admin'), SchemeAdmin = NULL where SchemeAdmin = true;

      UPDATE TeamMembers SET SchemeUser = NULL, SchemeAdmin = NULL;
      UPDATE ChannelMembers SET SchemeUser = NULL, SchemeAdmin = NULL;

      DELETE from Systems WHERE Name = 'migration_advanced_permissions_phase_2';
 

#. Start Mattermost server.

   On Ubuntu 14.04 and RHEL 6:

   .. code-block:: sh

     sudo service mattermost start

   On Ubuntu 16.04 and RHEL 7:

   .. code-block:: sh

     sudo systemctl start mattermost
