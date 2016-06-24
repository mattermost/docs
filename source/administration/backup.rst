Backup 
======

To backup your Mattermost server: 

1. Backup your Mattermost database using standard MySQL or PostgreSQL procedures depending on your database version.

      - `MySQL backup documentation <https://dev.mysql.com/doc/refman/5.6/en/backup-types.html>`_ is available online. Use the selector on the page to choose your MySQL version. 
      - `PostgreSQL backup documentation <https://www.postgresql.org/docs/9.5/static/backup-dump.html>`_ is available online. Use the navigation at the top of the page to select your PostgreSQL version. 
     
2. Backup your server settings stored in ``config/config.json``.

3. Backup files stored by your users with one of the following options: 

     - If you use local storage using the default ``./data`` directory back up this directory.
     - If you use local storage using a non-default directory specified in the ``Directory`` setting in ``config.json``, back up files in that location.
     - If you store your files in S3, you can typically keep the files where they are located without backup.
     
To restore a Mattermost instance from backup, restore your database, ``config.json`` file and optionally locally stored user files into the locations from which they were backed up. 
