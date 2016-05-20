# Upgrade Guide

This guide explains how to upgrade your Mattermost deployment across versions and editions.

### Upgrading to 3.0.x from 2.x

Mattermost 3.0 lets users maintain a single account across multiple teams on a Mattermost server. This means one set of credentials, one place to configure all account settings, and a more streamlined sign-up and team joining process.

#### Special instructions for 2.x servers with duplicate accounts

If your Mattermost server has duplicate accounts (users with multiple accounts in multiple teams with the same email address or username), you need to understand the 3.0 upgrade process in detail and take special steps to upgrade successfully.

1. Download Mattermost Team Edition 3.0.2
      1. Run `platform -version` to confirm the current version of your Mattermost server is `v2.2.0`, `v2.1.0`, or `v2.0.0`. If not, please [upgrade to `v2.0.0`](http://docs.mattermost.com/administration/upgrade.html#upgrade-guide).
      2. Run `wget https://releases.mattermost.com/X.X.X/mattermost-team-X.X.X-linux-amd64.tar.gz` to download the appropriate new version. 
2. Stop the Mattermost Server
      1. Consider posting an announcement to active teams about stopping the Mattermost server for an upgrade
      2. To stop the server run `sudo stop mattermost`
3. Backup your data
      1. Back up your `config.json` file, which contains your system configuration. This will be used to restore your current settings. after the new version is installed.
      2. Backup your database using your organization's standard procedures for backing up MySQL or PostgreSQL.
      3. If you're using local file storage, back up the location where files are stored.
      4. Verify your backups are successful.
4. Install new version
      1. Double check that your database and configuration file has been backed up, as the database upgrade to 3.x from 2.x cannot be reversed.
      2. Run `tar -xvzf mattermost-team-X.X.X-linux-amd64.tar.gz` to decompress the upgraded version and replace the current version of Mattermost on disk, where `X.X.X` is the version number to which you are upgrading.
5. Restore the state of your server
      1. Copy the backed up version of `config.json` in place of the default `config.json`.
6. Upgrade your database
      1. Run `./platform -upgrade_db_30` to upgrade your database from 2.x to 3.x
         - You may need to run with `sudo -u linux_user_account ./platform -upgrade_db_30` if you've setup Mattermost to run under a different account.  This will ensure files under `./data/` have the correct permissions.
         - You will be asked `Have you performed a database backup? (YES/NO):` 
             - If you have not backed up your database, enter `NO` and then backup your database
             - If you have verified your database has been backed up, enter `YES`
         - You will be asked to select a `primary team`.
             - If you only have one team, enter the name of the team. 
             - If you have more than one team, specify the `primary team` based on the team you use the most.
                  - If your server contains duplicate accounts (multiple accounts with either the same email addresses or the same usernames) the user account in the `primary team` will be considered the primary account and remain unchanged.
                     - When the server finds a duplicate account not in the `primary team` the email address of the account may be changed to avoid conflicts
                         - An account with a **duplicate email address** will be updated so `+[TEAM_URL_NAME]` is appended to the local part of the email address. For example: An account with a duplicate email `steve@company.com` in the team at URL `https://mattermost.company.com/marketing` becomes `steve+marketing@company.com`. The `+marketing` used in this procedure is part of the RFC5233 email specification and most email systems will properly route `steve+marketing@company.com` to `steve@company.com`. After the upgrade, if email authentication is used for sign-in, the user would need to sign-in with the new email address.
                         - An account with a **duplicate username** will be updated so `[TEAM_URL_NAME].`” is prepended to the username. For example: An account with a duplicate username `steve` in the team at URL `https://mattermost.company.com/marketing` becomes `marketing.steve`.
         - Users with accounts containing duplicate emails or usernames will receive a notification email explaining the upgrade, and instructions on how to move to a single user account ([see example](http://www.mattermost.org/upgrading-to-mattermost-3-0/#notification))
7. Start your server and address any setting changes relevant in the latest version of Mattermost
      1. Run `sudo start mattermost`.
      2. Opening the **System Console** and saving a change will upgrade your `config.json` schema to the latest version using default values for any new settings added. 
8. Test the system is working by going to the URL of an existing team.
      1. You may need to refresh your Mattermost browser page in order to get the latest updates from the upgrade.
9. After the Mattermost 3.0 upgrade users with duplicate accounts can follow instructions in the upgrade email they received to login to teams on which the duplicate accounts were created and add their primary account to the team and any private groups that are still actively used. Users can continue to access the direct message history of their duplicate accounts using their updated email addresses.

### Upgrading prior to 3.x

1. Download the **appropriate next upgrade** of your Team Edition server and note any compatibility procedures
      1. Run `platform -version` to check the current version of your Mattermost server
      2. Determine the appropriate next upgrade for your server:
          - Mattermost `v2.0.x` and `v2.1.x` can upgrade directly to Mattermost `v2.2.x`.
          - Mattermost `v1.4.x` and `v2.0.x` can upgrade directly to Mattermost `v2.1.x`.
          - Mattermost `v1.2.x` must upgrade to Mattermost `v1.3.x` before further upgrades.
          - Mattermost `v1.1.x` must upgrade to Mattermost `v1.2.x` before further upgrades.
          - Mattermost `v1.0.x` must upgrade to Mattermost `v1.1.x` before further upgrades.
      3. Use the [Version Archive table](http://docs.mattermost.com/administration/upgrade.html#version-archive) to find the `[RELEASE URL]` for your desired version and enter `wget [RELEASE URL]` to download. For example, to download `vX.X.X`, use `wget https://releases.mattermost.com/X.X.X/mattermost-team-X.X.X-linux-amd64.tar.gz`.
      4. Review **Compatibility** section in [CHANGELOG](http://docs.mattermost.com/administration/changelog.html) for the version downloaded and make sure to follow any instructions.
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

### Upgrade Team Edition to Enterprise Edition

1. Confirm you have the latest version of Mattermost Team Edition installed
   1. Run `platform -version` to check the current version of your Mattermost server and compare the version with the latest release listed on https://mattermost.org/download.
   2. If it is not the latest release, [upgrade to the latest release.](http://docs.mattermost.com/administration/upgrade.html#upgrading-mattermost-to-next-major-version)
2. Follow the standard upgrade procedure to install the [latest Mattermost Enterprise Edition build](http://docs.mattermost.com/administration/upgrade.html#mattermost-enterprise-edition) (in the format `https://releases.mattermost.com/X.X.X/mattermost-enterprise-X.X.X-linux-amd64.tar.gz`), instead of the latest Team Edition build
   1. Run `platform -version` to confirm the latest Enterprise Edition version has been successfully installed.

You will need an Enterprise Edition license key to activate the features. Follow the instructions that came with your license key to complete your upgrade.


## Version Archive

Locations of previously compiled builds.

### Mattermost Team Edition

Stable builds of open source team communication platform compiled by Mattermost, Inc, available under an MIT license.

- [Mattermost Team Edition v3.0.2](http://docs.mattermost.com/administration/changelog.html#release-v3-0-0)
  - `https://releases.mattermost.com/3.0.2/mattermost-team-3.0.2-linux-amd64.tar.gz`
- [Mattermost Team Edition v2.2.0](http://docs.mattermost.com/administration/changelog.html#release-v2-2-0)
  - `https://releases.mattermost.com/2.2.0/mattermost-team-2.2.0-linux-amd64.tar.gz`
- [Mattermost Team Edition v2.1.0](http://docs.mattermost.com/administration/changelog.html#release-v2-1-0)
  - `https://releases.mattermost.com/2.1.0/mattermost-team-2.1.0-linux-amd64.tar.gz`
- [Mattermost Team Edition v2.0.0](http://docs.mattermost.com/administration/changelog.html#release-v2-0-0)
  - `https://releases.mattermost.com/2.0.0/mattermost-team-2.0.0-linux-amd64.tar.gz`
- [Mattermost Team Edition v1.4.0](http://docs.mattermost.com/administration/changelog.html#release-v1-4-0)
  - `https://releases.mattermost.com/1.4.0/mattermost-team-1.4.0-linux-amd64.tar.gz`
- [Mattermost Team Edition v1.3.0](http://docs.mattermost.com/administration/changelog.html#release-v1-3-0)
  - `https://releases.mattermost.com/1.3.0/mattermost-team-1.3.0-linux-amd64.tar.gz`
- [Mattermost Team Edition v1.2.1](http://docs.mattermost.com/administration/changelog.html#release-v1-2-1)
  - `https://releases.mattermost.com/1.2.1/mattermost-team-1.2.1-linux-amd64.tar.gz`
- [Mattermost Team Edition v1.2.0](http://docs.mattermost.com/administration/changelog.html#release-v1-2-0)
  - Removed due to a security issue
- [Mattermost Team Edition v1.1.1](http://docs.mattermost.com/administration/changelog.html#release-v1-1-1)
   - `https://releases.mattermost.com/1.1.1/mattermost-team-1.1.1-linux-amd64.tar.gz`
- [Mattermost Team Edition v1.1.0](http://docs.mattermost.com/administration/changelog.html#release-v1-1-0)
   - `https://releases.mattermost.com/1.1.0/mattermost-team-1.1.0-linux-amd64.tar.gz`
- [Mattermost Team Edition v1.0.0](http://docs.mattermost.com/administration/changelog.html##release-v1-0-0)
   - `https://releases.mattermost.com/1.0.0/mattermost-team-1.0.0-linux-amd64.tar.gz`
- [Mattermost Team Edition v0.7.0](http://docs.mattermost.com/administration/changelog.html#release-v0-7-0-beta)
   - `https://releases.mattermost.com/0.7.0/mattermost-team-0.7.0-linux-amd64.tar.gz`
- [Mattermost Team Edition v0.6.0](http://docs.mattermost.com/administration/changelog.html#release-v0-6-0-alpha)
   - `https://releases.mattermost.com/0.6.0/mattermost-team-0.6.0-linux-amd64.tar.gz`
- [Mattermost Team Edition v0.5.0](http://docs.mattermost.com/administration/changelog.html#release-v0-5-0-preview)
  - `https://releases.mattermost.com/0.5.0/mattermost-team-0.5.0-linux-amd64.tar.gz`

### Mattermost Enterprise Edition

Commercial software for self-hosted enterprise communication compiled by Mattermost, Inc. Requires paid subscription and valid license key for use. Licenses may be purchased [here](https://about.mattermost.com/pricing/).

- [Mattermost Enterprise Edition v3.0.2](http://docs.mattermost.com/administration/changelog.html#release-v3-0-0)
  - `https://releases.mattermost.com/3.0.2/mattermost-enterprise-3.0.2-linux-amd64.tar.gz`
- [Mattermost Enterprise Edition v2.2.0](http://docs.mattermost.com/administration/changelog.html#release-v2-2-0)
  - `https://releases.mattermost.com/2.2.0/mattermost-enterprise-2.2.0-linux-amd64.tar.gz`
- [Mattermost Enterprise Edition v2.1.0](http://docs.mattermost.com/administration/changelog.html#release-v2-1-0)
  - `https://releases.mattermost.com/2.1.0/mattermost-enterprise-2.1.0-linux-amd64.tar.gz`
