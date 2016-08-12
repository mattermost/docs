Migration Guide 
---- 

Migrating the Mattermost Server  
==== 

The following instructions migrate Mattermost from one server to another by backing up and restoring the Mattermost database and `config.json` file. For these instructions **SOURCE** refers to the Mattermost server *from which* your system will be migrated and **DESTINATION** refers to the Mattermost server *to which* your system will be migrated. 

1. Upgrade your SOURCE Mattermost server to the latest major build version 
    1. See `Mattermost Upgrade Guide <upgrade.html>`_
2. Install the latest major build of Mattermost server as your DESTINATION   
    1. See docs.mattermost.com for install guides. Make sure your new instance is properly configured and tested. The database type and version of SOURCE and DESTINATION deployments need to match.  
    2. Stop the DESTINATION server using `sudo stop mattermost`, then backup the database and `config.json` file.
3. Migrate database from SOURCE to DESTINATION  
    1. Backup the database from the SOURCE Mattermost server and restore it in place of the database to which the DESTINATION server is connected
4. Migrate `config.json` from SOURCE to DESTINATION  
    1. Copy of `config.json` file from SOURCE deployment to DESTINATION 
5. Start the DESTINATION deployment  
    1. Run `sudo start mattermost`
    2. Opening the **System Console** and saving a change will upgrade your `config.json` schema to the latest version using default values for any new settings added
6. Test the system is working by going to the URL of an existing team.   
    1. You may need to refresh your Mattermost browser page in order to get the latest updates from the upgrade
 
Migrating from Slack
==== 

You can import channels and users from Slack into Mattermost from Team Settings > Import. Please review our documentation on `Slack Import <https://docs.mattermost.com/help/settings/team-settings.html#import-from-slack-beta>`_ for more details.
