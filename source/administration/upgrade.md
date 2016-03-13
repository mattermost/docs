# Upgrade Guide

This guide explains how to upgrade your Mattermost deployment across versions and editions. 

### Upgrading Mattermost to next major version

The following instructions upgrade Mattermost to the next major build release (for example, from 1.4.x to 2.0.0). You can upgrade to v2.0.0 directly from v1.3.x. or v1.4.x. If you're upgrading across more releases (for example from 1.2.x to 2.0.0) please run the following procedure once for each incremental upgrade up to v1.3.x, then again for v1.3.x to v2.0.0.  

1. Download the **next major build release** of your server and note any compatibility procedures 
      1. Run `platform -version` to check the current version of your Mattermost server
      2. Review the [Mattermost CHANGELOG](http://docs.mattermost.com/administration/changelog.html) to determine the next major build to download to your server. 
      3. Check the [Version Archive table](upgrade.html#version-archive) to find the `[RELEASE URL]` for your desired version and enter `wget [RELEASE URL]` to download. For example, to download v2.0.0, use `wget https://github.com/mattermost/platform/releases/download/v2.0.0/mattermost.tar.gz`
      4. Review **Compatibility** section in CHANGELOG for the version downloaded and make sure to follow any instructions
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

## Version Archive 

### Mattermost Team Edition T0

| Version | Release URL | 
|:--- |:--- |:--- |
| [t0-v2.1.0](http://docs.mattermost.com/administration/changelog.html#release-v2-1-0) | `https://github.com/mattermost/platform/releases/download/v2.0.0/mattermost.tar.gz` | 
| [t0-v2.0.0](http://docs.mattermost.com/administration/changelog.html#release-v2-0-0) | `https://github.com/mattermost/platform/releases/download/v2.0.0/mattermost.tar.gz` | 
| [t0-v1.4.0](http://docs.mattermost.com/administration/changelog.html#release-v1-4-0) | `https://github.com/mattermost/platform/releases/download/v1.4.0/mattermost.tar.gz` | 
| [t0-v1.3.0](http://docs.mattermost.com/administration/changelog.html#release-v1-3-0) | `https://github.com/mattermost/platform/releases/download/v1.3.0/mattermost.tar.gz` | 
| [t0-v1.2.1](http://docs.mattermost.com/administration/changelog.html#release-v1-2-1) | `https://github.com/mattermost/platform/releases/download/v1.2.1/mattermost.tar.gz` | 
| [t0-v1.2.0](http://docs.mattermost.com/administration/changelog.html#release-v1-2-0) | Redacted due to security issue | 
| [t0-v1.1.1](http://docs.mattermost.com/administration/changelog.html#release-v1-1-1) | `https://github.com/mattermost/platform/releases/download/v1.1.1/mattermost.tar.gz` | 
| [t0-v1.1.0](http://docs.mattermost.com/administration/changelog.html#release-v1-1-0) | `https://github.com/mattermost/platform/releases/download/v1.1.0/mattermost.tar.gz` | 
| [t0-v1.0.0](http://docs.mattermost.com/administration/changelog.html##release-v1-0-0) | `https://github.com/mattermost/platform/releases/download/v1.0.0/mattermost.tar.gz` | 
| [t0-v0.7.0](http://docs.mattermost.com/administration/changelog.html#release-v0-7-0-beta) | `https://github.com/mattermost/platform/releases/download/v0.7.0/mattermost.tar.gz` | 
| [t0-v0.6.0](http://docs.mattermost.com/administration/changelog.html#release-v0-6-0-alpha) | `https://github.com/mattermost/platform/releases/download/v0.6.0/mattermost.tar.gz` | 
| [t0-v0.5.0](http://docs.mattermost.com/administration/changelog.html#release-v0-5-0-preview) | `https://github.com/mattermost/platform/releases/download/v0.5.0/mattermost.tar.gz` | 
