# Upgrade Guide

This guide explains how to upgrade your Mattermost deployment across versions and editions. 

### Upgrading Team Edition 

1. Download the **appropriate next upgrade** of your server and note any compatibility procedures 
      1. Run `platform -version` to check the current version of your Mattermost server
      2. Determine the appropriate next upgrade for your server: 
          - Mattermost `v2.0.x` and `v2.1.x` can upgrade directly to Mattermost `v2.2.x`.
          - Mattermost `v1.4.x` and `v2.0.x` can upgrade directly to Mattermost `v2.1.x`.
          - Mattermost `v1.2.x` must upgrade to Mattermost `v1.3.x` before further upgrades.
          - Mattermost `v1.1.x` must upgrade to Mattermost `v1.2.x` before further upgrades.
          - Mattermost `v1.0.x` must upgrade to Mattermost `v1.1.x` before further upgrades.
      3. Use the [Version Archive table](http://docs.mattermost.com/administration/upgrade.html#version-archive) to find the `[RELEASE URL]` for your desired version and enter `wget [RELEASE URL]` to download. For example, to download `vX.X.X`, use `wget https://releases.mattermost.com/X.X.X/mattermost-team-X.X.X-linux-amd64.tar.gz`
      4. Review **Compatibility** section in [CHANGELOG](http://docs.mattermost.com/administration/changelog.html) for the version downloaded and make sure to follow any instructions
2. Stop the Mattermost Server
      1. Consider posting an announcement to active teams about stopping the Mattermost server for an upgrade
      2. To stop the server run `sudo stop mattermost`
3. Backup your data
      1. Back up your `config.json` file, which contains your system configuration. This will be used to restore your current settings after the new version is installed
      2. Backup your database using your organization's standard procedures for backing up MySQL or PostgreSQL
      3. If you're using local file storage, back up the location where files are stored
5. Install new version 
      1. Run `tar -xvzf mattermost-team-X.X.X-linux-amd64.tar.gz` to decompress the upgraded version and replace the current version of Mattermost on disk, where `X.X.X` is the version number to which you are upgrading.  
6. Restore the state of your server 
      1. Copy the backed up version of `config.json` in place of the default `config.json` 
7. Start your server and address any setting changes relevant in the latest version of Mattermost
      1. Run `sudo start mattermost`
      2. Opening the **System Console** and saving a change will upgrade your `config.json` schema to the latest version using default values for any new settings added
8. Test the system is working by going to the URL of an existing team. 
      You may need to refresh your Mattermost browser page in order to get the latest updates from the upgrade

### Upgrade Team Edition to Enterprise Edition 

1. Confirm you have the latest version of Mattermost Team Edition installed
   1. Run `platform -version` to check the current version of your Mattermost server and compare the version with the latest release listed on https://mattermost.org/download
   2. If it is not the latest release, [upgrade to the latest release.](http://docs.mattermost.com/administration/upgrade.html#upgrading-mattermost-to-next-major-version)
2. Follow the standard upgrade procedure to install the [latest Mattermost Enterprise Edition build](http://docs.mattermost.com/administration/upgrade.html#mattermost-team-edition-t0), instead of the latest Team Edition build
   1. Run `platform -version` to confirm the latest version has been successfully installed. 
   
You will need an Enterprise Edition license key to activate the features. Follow the instructions that came with your license key to complete your upgrade.   
   
## Version Archive 

Locations of previously compiled builds. 

### Mattermost Team Edition

Stable builds of open source team communication platform compiled by Mattermost, Inc, available under an MIT license.

- [v2.2.0](http://docs.mattermost.com/administration/changelog.html#release-v2-2-0) 
  - `https://releases.mattermost.com/2.2.0/mattermost-team-2.2.0-linux-amd64.tar.gz`
- [v2.1.0](http://docs.mattermost.com/administration/changelog.html#release-v2-1-0) 
  - `https://releases.mattermost.com/2.1.0/mattermost-team-2.1.0-linux-amd64.tar.gz` 
- [v2.0.0](http://docs.mattermost.com/administration/changelog.html#release-v2-0-0) 
  - `https://releases.mattermost.com/2.0.0/mattermost-team-2.0.0-linux-amd64.tar.gz` 
- [v1.4.0](http://docs.mattermost.com/administration/changelog.html#release-v1-4-0)
  - `https://releases.mattermost.com/1.4.0/mattermost-team-1.4.0-linux-amd64.tar.gz` 
- [v1.3.0](http://docs.mattermost.com/administration/changelog.html#release-v1-3-0)
  - `https://releases.mattermost.com/1.3.0/mattermost-team-1.3.0-linux-amd64.tar.gz` 
- [v1.2.1](http://docs.mattermost.com/administration/changelog.html#release-v1-2-1)
  - `https://releases.mattermost.com/1.2.1/mattermost-team-1.2.1-linux-amd64.tar.gz` 
- [v1.2.0](http://docs.mattermost.com/administration/changelog.html#release-v1-2-0)
  - Removed due to a security issue
- [v1.1.1](http://docs.mattermost.com/administration/changelog.html#release-v1-1-1)     
   - `https://releases.mattermost.com/1.1.1/mattermost-team-1.1.1-linux-amd64.tar.gz` 
- [v1.1.0](http://docs.mattermost.com/administration/changelog.html#release-v1-1-0)
   - `https://releases.mattermost.com/1.1.0/mattermost-team-1.1.0-linux-amd64.tar.gz` 
- [v1.0.0](http://docs.mattermost.com/administration/changelog.html##release-v1-0-0)
   - `https://releases.mattermost.com/1.0.0/mattermost-team-1.0.0-linux-amd64.tar.gz` 
- [v0.7.0](http://docs.mattermost.com/administration/changelog.html#release-v0-7-0-beta)
   - `https://releases.mattermost.com/0.7.0/mattermost-team-0.7.0-linux-amd64.tar.gz` 
- [v0.6.0](http://docs.mattermost.com/administration/changelog.html#release-v0-6-0-alpha)
   - `https://releases.mattermost.com/0.6.0/mattermost-team-0.6.0-linux-amd64.tar.gz`
- [v0.5.0](http://docs.mattermost.com/administration/changelog.html#release-v0-5-0-preview) 
  - `https://releases.mattermost.com/0.5.0/mattermost-team-0.5.0-linux-amd64.tar.gz` 

### Mattermost Enterprise Edition

Stable builds of commercial software for enterprise communication compiled by Mattermost, Inc. Requires paid subscription and valid license key for use. 

- [mattermost-enterprise-2.2.0-linux-amd64](http://docs.mattermost.com/administration/changelog.html#release-v2-2-0) 
  - `https://releases.mattermost.com/2.2.0/mattermost-enterprise-2.2.0-linux-amd64.tar.gz` 
- [mattermost-enterprise-2.1.0-linux-amd64](http://docs.mattermost.com/administration/changelog.html#release-v2-1-0) 
  - `https://releases.mattermost.com/2.1.0/mattermost-enterprise-2.1.0-linux-amd64.tar.gz` 

