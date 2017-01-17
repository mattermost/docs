# Upgrade Guide for v2.2.x and Earlier

#### Upgrade Team Edition for 2.2.x and earlier 

1. Download the **appropriate next upgrade** of your Team Edition server and note any compatibility procedures
      1. Run `platform -version` to check the current version of your Mattermost server
      2. Determine the appropriate next upgrade for your server:
          - Mattermost `v2.0.x` and `v2.1.x` can upgrade directly to Mattermost `v2.2.x`.
          - Mattermost `v1.4.x` and `v2.0.x` can upgrade directly to Mattermost `v2.1.x`.
          - Mattermost `v1.2.x` must upgrade to Mattermost `v1.3.x` before further upgrades.
          - Mattermost `v1.1.x` must upgrade to Mattermost `v1.2.x` before further upgrades.
          - Mattermost `v1.0.x` must upgrade to Mattermost `v1.1.x` before further upgrades.
      3. Use the [Version Archive List](https://docs.mattermost.com/administration/upgrade.html#version-archive) to find the `[RELEASE URL]` for your desired version and enter `wget [RELEASE URL]` to download. For example, to download `vX.X.X`, use `wget https://releases.mattermost.com/X.X.X/mattermost-team-X.X.X-linux-amd64.tar.gz`.
      4. Review **Compatibility** section in [CHANGELOG](https://docs.mattermost.com/administration/changelog.html) for the version downloaded and make sure to follow any instructions.
2. Stop the Mattermost Server
      1. Consider posting an announcement to active teams about stopping the Mattermost server for an upgrade.
      2. To stop the server run `sudo stop mattermost`.
3. Backup your data
      1. Back up your `config.json` file, which contains your system configuration. This will be used to restore your current settings after the new version is installed.
      2. Backup your database using your organization's standard procedures for backing up MySQL or PostgreSQL.
      3. If you're using local file storage, back up the location where files are stored.
5. Install new version
      1. Run `tar -xvzf mattermost-team-X.X.X-linux-amd64.tar.gz` to decompress the upgraded version and replace the current version of Mattermost on disk, where `X.X.X` is the version number to which you are upgrading.  
6. Restore the state of your server
      1. Copy the backed up version of `config.json` in place of the default `config.json`.
7. Start your server and address any setting changes relevant in the latest version of Mattermost
      1. Run `sudo start mattermost`.
      2. Opening the **System Console** and saving a change will upgrade your `config.json` schema to the latest version using default values for any new settings added.
8. Test the system is working by going to the URL of an existing team.
      You may need to refresh your Mattermost browser page in order to get the latest updates from the upgrade.
      
#### Upgrade Enterprise Edition to 2.2.x and earlier

1. Download the **appropriate next upgrade** of your Enterprise Edition server and note any compatibility procedures
      1. Run `platform -version` to check the current version of your Mattermost server
      2. Determine the appropriate next upgrade for your server:
          - Mattermost `v2.0.x` and `v2.1.x` can upgrade directly to Mattermost `v2.2.x`.
          - Mattermost `v1.4.x` and `v2.0.x` can upgrade directly to Mattermost `v2.1.x`.
          - Mattermost `v1.2.x` must upgrade to Mattermost `v1.3.x` before further upgrades.
          - Mattermost `v1.1.x` must upgrade to Mattermost `v1.2.x` before further upgrades.
          - Mattermost `v1.0.x` must upgrade to Mattermost `v1.1.x` before further upgrades.
      3. Use the [Version Archive List](https://docs.mattermost.com/administration/upgrade.html#version-archive) to find the `[RELEASE URL]` for your desired version and enter `wget [RELEASE URL]` to download. For example, to download `vX.X.X`, use `wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz`.
      4. Review **Compatibility** section in [CHANGELOG](https://docs.mattermost.com/administration/changelog.html) for the version downloaded and make sure to follow any instructions.
2. Stop the Mattermost Server
      1. Consider posting an announcement to active teams about stopping the Mattermost server for an upgrade.
      2. To stop the server run `sudo stop mattermost`.
3. Backup your data
      1. Back up your `config.json` file, which contains your system configuration. This will be used to restore your current settings after the new version is installed.
      2. Backup your database using your organization's standard procedures for backing up MySQL or PostgreSQL.
      3. If you're using local file storage, back up the location where files are stored.
5. Install new version
      1. Run `tar -xvzf mattermost-X.X.X-linux-amd64.tar.gz` to decompress the upgraded version and replace the current version of Mattermost on disk, where `X.X.X` is the version number to which you are upgrading.  
6. Restore the state of your server
      1. Copy the backed up version of `config.json` in place of the default `config.json`.
7. Start your server and address any setting changes relevant in the latest version of Mattermost
      1. Run `sudo start mattermost`.
      2. Opening the **System Console** and saving a change will upgrade your `config.json` schema to the latest version using default values for any new settings added.
8. Test the system is working by going to the URL of an existing team.
      You may need to refresh your Mattermost browser page in order to get the latest updates from the upgrade.

For any issues, Mattermost Enterprise Edition subscribers and trial license users can email support@mattermost.com 
