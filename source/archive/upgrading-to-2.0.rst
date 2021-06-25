Upgrading to version 2.0
========================

To upgrade an early edition of Mattermost to the latest edition, you must first upgrade in a specific sequence until you get to version 2.0.0. After that, you must upgrade to version 3.0.3, and from there you can upgrade directly to the latest Mattermost version.

Read these instructions carefully from start to finish. Make sure that you understand each step before starting the upgrade. If you have questions or concerns, you can ask on the Mattermost forum at https://forum.mattermost.org/.

You should gather the following information before starting the upgrade:

Existing install directory - *{install-path}*
  If you don't know where Mattermost Server is installed, use the ``whereis platform`` command. The output should be similar to */opt/mattermost/bin/platform*. The install directory is everything before the last occurrence of the string */mattermost*. In this example, the *{install-path}* is ``/opt``.
Location of your local storage directory
  The local storage directory contains all the files that users have attached to their messages. If you don't know its location, open the System Console and go to **Files > Storage** and read the value in **Local Storage Directory**. Relative paths are relative to the ``mattermost`` directory. For example, if the local storage directory is ``./data/`` then the absolute path is ``{install-path}/mattermost/data``.
Owner and group of the install directory - *{owner}* and *{group}*
  Use the ``ls -l {install-path}/mattermost/bin/platform`` command to get the owner and group.

**To upgrade to version 2.0**:

1. In a terminal window on the server that hosts Mattermost Server, change to your home directory. If any, delete files and directories that might still exist from a previous download.

  ``cd ~``

2. Download the appropriate version for the upgrade:
  a. Run ``sudo ./platform -version`` to check the current version.
  b. Use the following table to determine the appropriate version to download:
    .. csv-table::
      :header: "From", "To", "Download command"
      :widths: auto

      "1.4.0", "2.0.0", "wget https://releases.mattermost.com/2.0.0/mattermost-team-2.0.0-linux-amd64.tar.gz"
      "1.3.0", "1.4.0", "wget https://releases.mattermost.com/1.4.0/mattermost-team-1.4.0-linux-amd64.tar.gz"
      "1.2.1", "1.3.0", "wget https://releases.mattermost.com/1.3.0/mattermost-team-1.3.0-linux-amd64.tar.gz"
      "1.2.0", "1.3.0", "wget https://releases.mattermost.com/1.3.0/mattermost-team-1.3.0-linux-amd64.tar.gz"
      "1.1.1", "1.2.1", "wget https://releases.mattermost.com/1.2.1/mattermost-team-1.2.1-linux-amd64.tar.gz"
      "1.1.0", "1.2.1", "wget https://releases.mattermost.com/1.2.1/mattermost-team-1.2.1-linux-amd64.tar.gz"
      "1.0.0", "1.2.1", "wget https://releases.mattermost.com/1.2.1/mattermost-team-1.2.1-linux-amd64.tar.gz"

3. When the download is complete, extract the Mattermost Server files.

  ``tar -xzf mattermost*.gz``

4. Stop Mattermost Server.

  On Ubuntu 14.04 and RHEL 6: ``sudo service mattermost stop``

  On Ubuntu 16.04 and RHEL 7: ``sudo systemctl stop mattermost``

5. Back up your data and application.
  a. Back up your database using your organization’s standard procedures for backing up MySQL or PostgreSQL.
  b. Back up your application by moving into your archive folder (e.g. ``mattermost-back-YYYY-MM-DD``).

    ``mv {install-path}/mattermost {install-path}/{mattermost-back-YYYY-MM-DD}``

6. Copy the files that you extracted earlier to the install directory.

  ``sudo cp -r mattermost {install-path}``

7. Restore your configuration, local file storage and logs.

  .. code-block:: text

    sudo cp -r {install-path}/{mattermost-back-YYYY-MM-DD}/config {install-path}/mattermost
    sudo cp -r {install-path}/{mattermost-back-YYYY-MM-DD}/data {install-path}/mattermost
    sudo cp -r {install-path}/{mattermost-back-YYYY-MM-DD}/logs {install-path}/mattermost

8. Change ownership of the new files.

  ``sudo chown -R {owner}:{group} {install-path}/mattermost``

9. Upgrade your ``config.json`` schema: Open the System Console and make a change and then save the change. Your current settings are preserved, and new settings are added with default values.

10. If you have TLS set up on your Mattermost server, you must activate the CAP_NET_BIND_SERVICE capability to allow the new Mattermost binary to bind to low ports.

  .. code-block:: text

    cd {install-path}
    sudo setcap cap_net_bind_service=+ep ./bin/platform

11. Make sure the system is working, then repeat the steps 1 to 10 until version 2.0 is installed and running.
