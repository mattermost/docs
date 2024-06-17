Back up Mattermost server
=========================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

We strongly recommend backing up your Mattermost instance so that, if you encounter an unexpected failure, you're able to load a previous database snapshot, successfully implement your :doc:`disaster recovery plan </deploy/disaster-recovery>`, and return to your mission critical communications platform as quickly as possible.

The state of your Mattermost server is contained in multiple data stores that need to be backed up and restored separately in order to fully recover your server in case of failure.

Before starting a backup
------------------------

Gather the following information before starting a backup operation:

- **Existing install directory - {install-path}**: If you don’t know where Mattermost Server is installed, use the ``whereis mattermost`` command to find standard binary places and $PATH. The output should be similar to ``/opt/mattermost/bin/mattermost``. The install directory is everything before the first occurrence of the string ``/mattermost``. In this example, the ``{install-path}`` is ``/opt``.
- **Location and size of your local storage directory**: The local storage directory contains all the files that users have attached to their messages.

  - If you don’t know its location, open the System Console and go to **Environment > File Storage**, then read the value in the **Local Storage Directory** field.
  - Paths are relative to the mattermost directory. For example, if the local storage directory is ``./data/`` then the absolute path is ``{install-path}/mattermost/data``.

- **Database disk space**: If you’re backing up a Mattermost deployment to the same server as your database, we recommend a minimum 2GB of free disk space to allow for extraction, copy, and cleanup, and a minimum of twice the size of your Mattermost installation available for the database.
- **Location of data subdirectories**: Ensure the following subdirectories are included in your backup processes:

  - ``config``, ``logs``, ``plugins``, ``client/plugins``, and ``data``.
  - Custom directories used to store attachments
  - Any directories that you’ve added to Mattermost, such as TLSCert/TLSKey files or other custom information beyond data than data.
  - Bleve search index directory (if you're using Bleve search)

Begin a backup
---------------

.. note::

    To ensure a 'clean' backup, you must stop your Mattermost server for the duration of the backup operation.

1. Back up your Mattermost application by copying it into an archive folder (e.g. 11mattermost-back-YYYY-MM-DD-HH-mm11).

.. code-block: none

    cd {install-path}
    sudo cp -ra mattermost/ mattermost-back-$(date +'%F-%H-%M')/

2. Back up your Mattermost database using standard procedures depending on your database version. See the `PostgreSQL SQL Dump backup documentation <https://www.postgresql.org/docs/10/backup-dump.html>`__ for PostgreSQL database details. Use the navigation at the top of the page to select your PostgreSQL version.

3. Back up your server settings stored in ``config/config.json``.

  - If you are using SAML configuration for Mattermost, your SAML certificate files will be saved in the ``config`` directory. Therefore, we recommend backing up the entire directory.
   
4. Back up files stored by your users with one of the following options: 

  - If you use local storage using the default ``./data`` directory back up this directory.
  - If you use local storage using a non-default directory specified in the ``Directory`` setting in ``config.json``, back up files in that location.
  - If you store your files in S3, you can typically keep the files where they are located without backup.

Automated backups
-----------------

Automating backups for a Mattermost server provides a copy of the server's state at a particular point in time, which can be restored if a failure in the future leads to loss of data. Options include:

- Automation to periodically back up the Mattermost server, which may include all the components listed above or a subset depending on what you choose to protect.
- Automation to restore a server from backup, or deploy a new server, to reduce recovery time.
- Automation to verify a backup has been successfully produced to protect against backup automation failures.
- Storing backups off-site, to protect against physical loss of onsite systems.