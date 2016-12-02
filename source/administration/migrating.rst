Migration Guide 
---------------

Migrating the Mattermost Server  
===============================

The following instructions migrate Mattermost from one server to another by backing up and restoring the Mattermost database and ``config.json`` file. For these instructions **SOURCE** refers to the Mattermost server *from which* your system will be migrated and **DESTINATION** refers to the Mattermost server *to which* your system will be migrated. 

1. Backup your SOURCE Mattermost server 
    1. See `Backup Guide <https://docs.mattermost.com/administration/backup.html>`_
2. Upgrade your SOURCE Mattermost server to the latest major build version 
    1. See `Mattermost Upgrade Guide <upgrade.html>`_
3. Install the latest major build of Mattermost server as your DESTINATION   
    1. See docs.mattermost.com for install guides. Make sure your new instance is properly configured and tested. The database type and version of SOURCE and DESTINATION deployments need to match.  
    2. Stop the DESTINATION server using `sudo stop mattermost`, then backup the database and `config.json` file.
4. Migrate database from SOURCE to DESTINATION  
    1. Backup the database from the SOURCE Mattermost server and restore it in place of the database to which the DESTINATION server is connected
5. Migrate ``config.json`` from SOURCE to DESTINATION  
    1. Copy of ``config.json`` file from SOURCE deployment to DESTINATION 
6. Start the DESTINATION deployment  
    1. Run ``sudo start mattermost``
    2. Opening the **System Console** and saving a change will upgrade your ``config.json`` schema to the latest version using default values for any new settings added
7. Test the system is working by going to the URL of an existing team.   
    1. You may need to refresh your Mattermost browser page in order to get the latest updates from the upgrade
 
Migrating from Slack
====================

.. note:: As a proprietary SaaS service, Slack is able to change its export format quickly and without notice. If you encounter issues not mentioned in the documentation below, please alert the product team by `filing an issue <https://www.mattermost.org/filing-issues/>`_.

The Slack Import feature in Mattermost is in "Beta" and focused on supporting migration of teams of less than 100 registered users.

This feature can be accessed through the `Mattermost Web App <https://docs.mattermost.com/administration/migrating.html#migrating-from-slack-using-the-mattermost-web-app>`_ or using the `CLI <https://docs.mattermost.com/administration/migrating.html#migrating-from-slack-using-the-mattermost-cli>`_.

.. warning:: **It is highly recommended that you test Slack import before applying it to an instance intended for production.**

   If you use Docker, you can spin up a test instance in one line:

   .. code:: bash

       docker run --name mattermost-dev -d --publish 8065:80 mattermost/platform

   If you don't use Docker, there are `step-by-step instructions <https://docs.mattermost.com/install/docker-local-machine.html>`_ to install Mattermost in preview mode in less than 5 minutes.

Supported Features
++++++++++++++++++

The following key features are supported when importing from Slack:

* User accounts with an email address set

* Public channels and the text messages posted in them

* Channel topic and purpose

* Imported users added automatically to their channels

Messages with file attachments are imported as a message containing a link to Slack's servers by default. The file attachments themselves can be imported to Mattermost by using the `Slack Advanced Exporter <https://github.com/grundleborg/slack-advanced-exporter>`_ tool to add them to your archive before importing it.

Bot and Integration messages are imported by default, but if you would like them to display with the appropriate username when imported, you should ensure that `Enable Integrations to Override Usernames <https://docs.mattermost.com/administration/config-settings.html#enable-integrations-to-override-usernames>`_ is set in **System Console > Integrations > Custom Integrations** *before* doing the import.

.. note:: Slack user accounts with the same email address as existing accounts on your Mattermost server will be merged into those accounts on import.

Limitations
+++++++++++

The following limitations are present when importing from Slack:

* The Markdown subset used by Slack's Posts 2.0 feature announced on September 28, 2015 is not yet supported.

* Direct Message and Private Groups cannot be imported. Slack does not include these messages when generating the export archive.

Migrating from Slack using the Mattermost Web App
+++++++++++++++++++++++++++++++++++++++++++++++++

.. note:: For larger imports, particularly those where you have used the `slack-advanced-exporter tool` to add Slack post attachments to the archive, it is recommended to import the Slack data using the `CLI <https://docs.mattermost.com/administration/migrating.html#migrating-from-slack-using-the-mattermost-cli>`_.

1. Generate a Slack "Export" file from **Slack > Team Settings > Import/Export Data > Export > Start Export**.

2. In Mattermost go to **Team Settings > Import > Import from Slack**. Team Admin or System Admin role is required to access this menu option.

3. Click **Select file** to upload Slack export file and click **Import**.


Migrating from Slack using the Mattermost CLI
+++++++++++++++++++++++++++++++++++++++++++++

1. Generate a Slack "Export" file from **Slack > Team Settings > Import/Export Data > Export > Start Export**.

2. Run the following Mattermost CLI command, with the name of a team you have already created:

   ``$ platform -slack_import -team_name="your-team" -import_archive /path/to/your-slack-export.zip``

Using the Imported Team
+++++++++++++++++++++++

* During the import process, the emails and usernames from Slack are used to create new Mattermost accounts.

* Slack users can activate their new Mattermost accounts by using Mattermost's Password Reset screen with their email addresses from Slack to set new passwords for their Mattermost accounts.

* Once logged in, Mattermost users will have access to previous Slack messages in the public channels imported from Slack.
