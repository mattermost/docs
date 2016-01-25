# Upgrade and Migration Guide

### Upgrading Mattermost to Next Major Release 

The following instructions upgrade Mattermost to the next major build release (for example, from 1.3.x to 1.4.x). If you're upgrading across multiple releases (for example from 1.2.x to 1.4.x) please run the following procedure once for each incremental upgrade. 

1. Download the **next major build release** of your server and note any compatibility procedures 
     1. Run `platform -version` to check the current version of your Mattermost server
     2. Review the [Mattermost CHANGELOG](https://github.com/mattermost/platform/blob/master/CHANGELOG.md) to determine the next major build to download to your server using `wget https://github.com/mattermost/platform/releases/download/v1.x.x/mattermost.tar.gz`
     3. Review **Compatibility** section in CHANGELOG for the version downloaded and make sure to follow any instructions
2. Stop the Mattermost Server
     1. Consider posting an announcement to active teams about stopping the Mattermost server for an upgrade
     2. To stop the server run `sudo stop mattermost`
3. Backup your data
     1. Back up your `config.json` file, which contains your system configuration. This will be used to restore your current settings after the new version is installed
     2. Backup your database using your organization's standard procedures for backing up MySQL or PostgreSQL
     3. If you're using local file storage, back up the location where files are stored
5. Install new version 
     1. Run `tar -xvzf mattermost.tar.gz` to decompress the upgraded version and replace the current version of Mattermost on disk
6. Restore the state of your server 
     1. Copy the backed up version of `config.json` in place of the default `config.json` 
7. Start your server and address any setting changes relevant in the latest version of Mattermost
     1. Run `sudo start mattermost`
     2. Opening the **System Console** and saving a change will upgrade your `config.json` schema to the latest version using default values for any new settings added
8. Test the system is working by going to the URL of an existing team. 
     You may need to refresh your Mattermost browser page in order to get the latest updates from the upgrade

### Migrating Mattermost 

The following instructions migrate Mattermost from one server to another by backing up and restoring the Mattermost database and `config.json` file. For these instructions **SOURCE** refers to the Mattermost server _from which_ your system will be migrated and **DESTINATION** refers to the Mattermost server _to which_ your system will be migrated. 

1. Upgrade your SOURCE Mattermost server to the latest major build version
      1. See instructions above. 
2. Install the latest major build of Mattermost server as your DESTINATION 
      2. See docs.mattermost.com for install guides. Make sure your new instance is properly configured and tested. The database type and version of SOURCE and DESTINATION deployments need to match.
      3. Stop the DESTINATION server using `sudo stop mattermost`, then backup the database and `config.json` file.
3. Migrate database from SOURCE to DESTINATION 
      1. Backup the database from the SOURCE Mattermost server and restore it in place of the database to which the DESTINATION server is connected
4. Migrate `config.json` from SOURCE to DESTINATION 
      1. Create a copy of `config.json` file from SOURCE deployment and replace `DataSource` and `ListenAddress` with settings from `config.json` file in DESTINATION deployment
      2. Use this file to replace `config.json` file in DESTINATION deployment
5. Start the DESTINATION deployment 
      1. Run `sudo start mattermost`
      2. Opening the **System Console** and saving a change will upgrade your `config.json` schema to the latest version using default values for any new settings added
6. Test the system is working by going to the URL of an existing team. 
     You may need to refresh your Mattermost browser page in order to get the latest updates from the upgrade
 
