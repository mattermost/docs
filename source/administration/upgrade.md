# Upgrade Guide

This guide explains how to upgrade your Mattermost deployment across versions and editions.

To start, select one of the following guides: 

- [Upgrade Team Edition](https://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition)
  - [Upgrade Team Edition to 3.1.x and later](https://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-to-3-1-x-and-later)
  - [Upgrade Team Edition to 3.0.x](https://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-to-3-0-x)
- [Upgrade Enterprise Edition](https://docs.mattermost.com/administration/upgrade.html#upgrade-enterprise-edition)
  - [Upgrade Enterprise Edition to 3.1.x and later](https://docs.mattermost.com/administration/upgrade.html#upgrade-enterprise-edition-to-3-1-x-and-later)
  - [Upgrade to Enterprise Edition 3.0.x](https://docs.mattermost.com/administration/upgrade.html#upgrade-to-enterprise-edition-3-0-x)
- [Upgrade Team Edition to Enterprise Edition](https://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-to-enterprise-edition)  

### Upgrade Team Edition 

#### Upgrade Team Edition to 3.1.x and later

1. Download the **appropriate next upgrade** of your Team Edition server and note any compatibility procedures
      1. Run `platform -version` to check the current version of your Mattermost server
      2. Determine the appropriate next upgrade for your server:
          - Mattermost `v3.0.x` and later can upgrade directly to Mattermost `v3.6.x`
              - Note: If public links are enabled, upgrading from `v3.3.x` and earlier to `v3.4.x` and later will invalidate existing public links due to a security upgrade allowing admins to invalidate links by resetting a public link salt from the System Console.
              - Note: RHEL6 and Ubuntu installations must verify the line `limit nofile 50000 50000` is included in `/etc/init/mattermost.conf` file. See the [installation guide](https://docs.mattermost.com/guides/administrator.html#install-guides) for your operating system for more details.
              - Note: RHEL7 and Debian installations must verify the line `LimitNOFILE=49152` is included in the `/etc/systemd/system/mattermost.service` file. See the [installation guide](https://docs.mattermost.com/guides/administrator.html#install-guides) for your operating system for more details.
          - Mattermost `v2.2.x` can upgrade directly to `v3.1.x` or `v3.2.x` but must follow the [extended upgrade guide for `v3.0.x`](https://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-to-3-0-x)   
          - Mattermost `v2.1.x` and below must follow the process to [upgrade to `v3.0.x`](https://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-to-3-0-x) before upgrading further
      3. Use the [Version Archive table](https://docs.mattermost.com/administration/upgrade.html#version-archive) to find the `[RELEASE URL]` for your desired version and enter `wget [RELEASE URL]` to download. For example, to download `vX.X.X`, use `wget https://releases.mattermost.com/X.X.X/mattermost-team-X.X.X-linux-amd64.tar.gz`.
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

#### Upgrade Team Edition to 3.0.x 

Mattermost 3.0 lets users maintain a single account across multiple teams on a Mattermost server. This means one set of credentials, one place to configure all account settings, and a more streamlined sign-up and team joining process.

##### Special instructions for 2.x servers with duplicate accounts

If your Mattermost server has duplicate accounts (users with multiple accounts in multiple teams with the same email address or username), you need to understand the 3.0 upgrade process in detail and take special steps to upgrade successfully.

1. Download Mattermost Team Edition 3.0.3
      1. Run `platform -version` to confirm the current version of your Mattermost server is `v2.2.0`, `v2.1.0`, or `v2.0.0`. If not, please [upgrade to `v2.0.0`](https://docs.mattermost.com/administration/2-x-upgrade.html).
      2. Run `wget https://releases.mattermost.com/X.X.X/mattermost-team-X.X.X-linux-amd64.tar.gz` to download the appropriate new version. 
2. Stop the Mattermost Server
      1. Consider posting an announcement to active teams about stopping the Mattermost server for an upgrade
      2. To stop the server run `sudo stop mattermost`
3. Backup your data
      1. Back up your `config.json` file, which contains your system configuration. This will be used to restore your current settings after the new version is installed.
      2. Backup your database using your organization's standard procedures for backing up MySQL or PostgreSQL.
      3. If you're using local file storage, back up the location where files are stored. This location is specified in the `config.json` file under `FileSettings` > `Directory`.
      4. Verify your backups are successful.
4. Install new version
      1. Double check that your database and configuration file has been backed up, as the database upgrade to 3.x from 2.x cannot be reversed.
      2. Run `tar -xvzf mattermost-team-X.X.X-linux-amd64.tar.gz` to decompress the upgraded version and replace the current version of Mattermost on disk, where `X.X.X` is the version number to which you are upgrading.
5. Restore the state of your server
      1. Copy the backed up version of `config.json` in place of the default `config.json`.
      2. If you're using local file storage, restore the data you backed up before running the server. Keep the backup until you're sure the upgrade has succeeded.
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
         - Users with accounts containing duplicate emails or usernames will receive a notification email explaining the upgrade, and instructions on how to move to a single user account ([see example](https://www.mattermost.org/upgrade-to-3-0/))
7. Start your server and address any setting changes relevant in the latest version of Mattermost
      1. Run `sudo start mattermost`.
      2. Opening the **System Console** and saving a change will upgrade your `config.json` schema to the latest version using default values for any new settings added. 
8. Test the system is working by going to the URL of an existing team.
      1. You may need to refresh your Mattermost browser page in order to get the latest updates from the upgrade.
9. After the Mattermost 3.0 upgrade users with duplicate accounts can follow instructions in the upgrade email they received to login to teams on which the duplicate accounts were created and add their primary account to the team and any private groups that are still actively used. Users can continue to access the direct message history of their duplicate accounts using their updated email addresses.



### Upgrade Team Edition to Enterprise Edition

1. Confirm you have the latest version of Mattermost Team Edition installed
   1. Run `platform -version` to check the current version of your Mattermost server and compare the version with the latest release listed on https://mattermost.org/download.
   2. If it is not the latest release, [upgrade to the latest release.](https://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-to-3-1-x-and-later)
2. Follow the [Enterprise Edition upgrade procedure](https://docs.mattermost.com/administration/upgrade.html#upgrade-enterprise-edition) to replace the Team Edition binary with the [latest Mattermost Enterprise Edition build](https://docs.mattermost.com/administration/upgrade.html#mattermost-enterprise-edition) (in the format `https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz`). 
3. Run `platform -version` to confirm the latest Enterprise Edition version has been successfully installed.
4. In the **System Console**, go to **OTHER** > **Edition and License** > **License Key** and upload the license key file you received via email. 
5. Reset the Mattermost account as the directory owner by typing:
 - `sudo chown -R mattermost:mattermost <path-to-your-mattermost-folder>`
 - `sudo chmod -R g+w <path-to-your-mattermost-folder>`
6. To ensure client applications don't encounter issues with out-of-sync caches, you can force clients to refresh after a server upgrade by changing any setting in the System Console. For example, go to **System Console** > **General** > **Configuration**, and copy the Listen Address. Then paste the Listen Address back into the field, and press **Save**.

The **Edition** and **License** sections on the page should update to confirm your system has been updated to the Enterprise Edition.

For any issues, Mattermost Enterprise Edition subscribers and trial license users can email support@mattermost.com 

### Upgrade Enterprise Edition 

#### Upgrade Enterprise Edition to 3.1.x and later

1. Download the **appropriate next upgrade** of your Team Edition server and note any compatibility procedures
      1. Run `platform -version` to check the current version of your Mattermost server
      2. Determine the appropriate next upgrade for your server:
          - Mattermost `v3.0.x` and later can upgrade directly to Mattermost `v3.6.x`
              - Note: If there is are config settings set for `"RestrictPublicChannelManagement"` and `"RestrictPrivateChannelManagement"`, they will be used as the default values for `"RestrictPublicChannelCreation"`, `"RestrictPrivateChannelCreation"`, `"RestrictPublicChannelDeletion"`, and `"RestrictPrivateChannelDeletion"` after upgrade
              - Note: If public links are enabled, upgrading from `v3.3.x` and earlier to `v3.4.x` and later will invalidate existing public links due to a security upgrade allowing admins to invalidate links by resetting a public link salt from the System Console.
              - Note: RHEL6 and Ubuntu installations must verify the line `limit nofile 50000 50000` is included in `/etc/init/mattermost.conf` file. See the [installation guide](https://docs.mattermost.com/guides/administrator.html#install-guides) for your operating system for more details.
              - Note: RHEL7 and Debian installations must verify the line `LimitNOFILE=49152` is included in the `/etc/systemd/system/mattermost.service` file. See the [installation guide](https://docs.mattermost.com/guides/administrator.html#install-guides) for your operating system for more details.
          - Mattermost `v2.2.x` can upgrade directly to `v3.1` or `v3.2` but must follow the [extended upgrade guide for `v3.0.x`](https://docs.mattermost.com/administration/upgrade.html#upgrade-to-enterprise-edition-3-0-x)   
            - Note: For `v3.2.x` only, `"BindUsername"`, and `"BindPassword"` under `LdapSettings` are required fields with anonymous bind not supported. For `v3.2.x` and `v3.3.x` only, `"FirstNameAttribute"` and `"LastNameAttribute"` under `LdapSettings` are required fields.
          - Mattermost `v2.1.x` and below must follow the process to [upgrade to `v3.0.x`](https://docs.mattermost.com/administration/upgrade.html#upgrade-to-enterprise-edition-3-0-x) before upgrading further
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

#### Upgrade to Enterprise Edition 3.0.x 

Mattermost 3.0 lets users maintain a single account across multiple teams on a Mattermost server. This means one set of credentials, one place to configure all account settings, and a more streamlined sign-up and team joining process.

##### Special instructions for 2.x servers with duplicate accounts

If your Mattermost server has duplicate accounts (users with multiple accounts in multiple teams with the same email address or username), you need to understand the 3.0 upgrade process in detail and take special steps to upgrade successfully.

1. Download Mattermost Enterprise Edition 3.0.3
      1. Run `platform -version` to confirm the current version of your Mattermost server is `v2.2.0`, `v2.1.1`, or `v2.0.0` of either Mattermost Enteprrise Edition or Mattermost Team Edition. If not, please [upgrade to at least Mattermost Enterprise Edition `v2.0.0`]((https://docs.mattermost.com/administration/2-x-upgrade.html)).
      2. Run `wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz` to download the appropriate new version. 
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
      2. Run `tar -xvzf mattermost-X.X.X-linux-amd64.tar.gz` to decompress the upgraded version and replace the current version of Mattermost on disk, where `X.X.X` is the version number to which you are upgrading.
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
         - Users with accounts containing duplicate emails or usernames will receive a notification email explaining the upgrade, and instructions on how to move to a single user account ([see example](https://www.mattermost.org/upgrading-to-mattermost-3-0/#notification))
7. Start your server and address any setting changes relevant in the latest version of Mattermost
      1. Run `sudo start mattermost`.
      2. Opening the **System Console** and saving a change will upgrade your `config.json` schema to the latest version using default values for any new settings added. 
8. Test the system is working by going to the URL of an existing team.
      1. You may need to refresh your Mattermost browser page in order to get the latest updates from the upgrade.
9. After the Mattermost 3.0 upgrade users with duplicate accounts can follow instructions in the upgrade email they received to login to teams on which the duplicate accounts were created and add their primary account to the team and any private groups that are still actively used. Users can continue to access the direct message history of their duplicate accounts using their updated email addresses.

For any issues, Mattermost Enterprise Edition subscribers and trial license users can email support@mattermost.com 

## Version Archive

### Mattermost Enterprise Edition Server

Private cloud enterprise communications server. 

- Free to use in "team mode" with same features as open source version.
- Enterprise features unlock with a license key and purchase of a subscription. [See feature list and pricing](https://about.mattermost.com/pricing/) (including academic and non-profit options).

-------

- Mattermost Enterprise Edition v3.6.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v3-6-0) - [Download](https://releases.mattermost.com/3.6.0/mattermost-3.6.0-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/3.6.0/mattermost-3.6.0-linux-amd64.tar.gz`
  - Checksum: `c58110460c33dbe3d365eaea25ae0cf2e4c529fd81c70b969f8c5611d467bff6`
- Mattermost Enterprise Edition v3.5.1 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v3-5-1) - [Download](https://releases.mattermost.com/3.5.1/mattermost-3.5.1-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/3.5.1/mattermost-3.5.1-linux-amd64.tar.gz`
  - Checksum: `b972ac6f38f8b4c4f364e40a7c0e7819511315a81cb38c8a51c0622d7c5b14a1`
- Mattermost Enterprise Edition v3.4.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v3-4-0) - [Download](https://releases.mattermost.com/3.4.0/mattermost-3.4.0-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/3.4.0/mattermost-3.4.0-linux-amd64.tar.gz`
  - Checksum: `3329fe3ef4d6bd7bd156eec86903b5d9db30d8c62545e4f5ca63633a64559f16`
- Mattermost Enterprise Edition v3.3.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v3-3-0) - [Download](https://releases.mattermost.com/3.3.0/mattermost-3.3.0-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/3.3.0/mattermost-3.3.0-linux-amd64.tar.gz`
  - Checksum: `d12d567c270a0c163e07b38ff41ea1d7839991d31f7c10b6ad1b4ef0f05f4e14`
- Mattermost Enterprise Edition v3.2.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v3-2-0) - [Download](https://releases.mattermost.com/3.2.0/mattermost-3.2.0-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/3.2.0/mattermost-3.2.0-linux-amd64.tar.gz`
  - Checksum: `f66597ad2fa94d3f75f06135129aa91cddd35dd8b94acab4aa15dfa225596422`
- Mattermost Enterprise Edition v3.1.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v3-1-0) - [Download](https://releases.mattermost.com/3.1.0/mattermost-3.1.0-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/3.1.0/mattermost-3.1.0-linux-amd64.tar.gz`
  - Checksum: `9e29525199e25eca6b7fe6422b415f6371d21e22c344ca6febc5e64f69ec670b`
- Mattermost Enterprise Edition v3.0.3 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v3-0-3) - [Download](https://releases.mattermost.com/3.0.3/mattermost-enterprise-3.0.3-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/3.0.3/mattermost-enterprise-3.0.3-linux-amd64.tar.gz`
  - Checksum: `3c692f8532b1858aefd2f0c2c22721e6b18734580a84a8ae5d6ce891f0e16f07`
- Mattermost Enterprise Edition v2.2.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v2-2-0) - [Download](https://releases.mattermost.com/2.2.0/mattermost-enterprise-2.2.0-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/2.2.0/mattermost-enterprise-2.2.0-linux-amd64.tar.gz`
  - Checksum: `a7e997526d9204eab70c74a31d51eea693cca0d4bf0f0f71760f14f797fa5477`
- Mattermost Enterprise Edition v2.1.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v2-1-0) - [Download](https://releases.mattermost.com/2.1.0/mattermost-enterprise-2.1.0-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/2.1.0/mattermost-enterprise-2.1.0-linux-amd64.tar.gz`
  - Checksum: `9454c3daacae602025b03950590e3f1ecd540b85a4bb7ad73bdca212ba85cf7a`


### Mattermost Team Edition Server

Open source self-hosted team communication server compiled by Mattermost, Inc, available under an MIT license. 

- Identical feature set to free version of Mattermost Enterprise Edition, but cannot be unlocked with a license key.

-------

- Mattermost Team Edition v3.6.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v3-6-0) - [Download](https://releases.mattermost.com/3.6.0/mattermost-team-3.6.0-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/3.6.0/mattermost-team-3.6.0-linux-amd64.tar.gz`
  - Checksum: `527acc2af67d7a47990cf177c17d60d23b43c7cc5a06d143194ad94eb2699bda`
- Mattermost Team Edition v3.5.1 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v3-5-1) - [Download](https://releases.mattermost.com/3.5.1/mattermost-team-3.5.1-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/3.5.1/mattermost-team-3.5.1-linux-amd64.tar.gz`
  - Checksum: `2c6bc8b1c25e48d1ac887cd6cbef77df1f80542127b4d98c4d7c0dfbfade04d5`
- Mattermost Team Edition v3.4.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v3-4-0) - [Download](https://releases.mattermost.com/3.4.0/mattermost-team-3.4.0-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/3.4.0/mattermost-team-3.4.0-linux-amd64.tar.gz`
  - Checksum: `c352f6c15466c35787bdb5207a6efe6b471513ccdd5b1f64a91a8bd09c3365da`
- Mattermost Team Edition v3.3.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v3-3-0) - [Download](https://releases.mattermost.com/3.3.0/mattermost-team-3.3.0-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/3.3.0/mattermost-team-3.3.0-linux-amd64.tar.gz`
  - Checksum: `09948edb32ebb940708e30a05c269e69568dfd2e0c05495392f353b26139b79a`
- Mattermost Team Edition v3.2.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v3-2-0) - [Download](https://releases.mattermost.com/3.2.0/mattermost-team-3.2.0-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/3.2.0/mattermost-team-3.2.0-linux-amd64.tar.gz`
  - Checksum: `14e5c1460a991791ef3dccd6b5aeab40ce903090c5f6c15e7974eb5e4571417a`
- Mattermost Team Edition v3.1.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v3-1-0) - [Download](https://releases.mattermost.com/3.1.0/mattermost-team-3.1.0-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/3.1.0/mattermost-team-3.1.0-linux-amd64.tar.gz`
  - Checksum: `dad164d2382428c36623b6d50e3290336a3be01bae278a465e0d8d94b701e3ff`
- Mattermost Team Edition v3.0.3 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v3-0-3) - [Download](https://releases.mattermost.com/3.0.3/mattermost-team-3.0.3-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/3.0.3/mattermost-team-3.0.3-linux-amd64.tar.gz`
  - Checksum: `b60d26a13927b614e3245384559869ae31250c19790b1218a193d52599c09834`
- Mattermost Team Edition v2.2.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v2-2-0) - [Download](https://releases.mattermost.com/2.2.0/mattermost-team-2.2.0-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/2.2.0/mattermost-team-2.2.0-linux-amd64.tar.gz`
  - Checksum: `d723fe9bf18d2d2a419a8d2aa6ad94fc99f251f8382c4342f08a48813501ca06`
- Mattermost Team Edition v2.1.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v2-1-0) - [Download](https://releases.mattermost.com/2.1.0/mattermost-team-2.1.0-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/2.1.0/mattermost-team-2.1.0-linux-amd64.tar.gz`
  - Checksum: `2825434aad23db1181e03b036bd826e66d6d4f21d337d209679a095a3ed9a4d2`
- Mattermost Team Edition v2.0.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v2-0-0) - [Download](https://releases.mattermost.com/2.0.0/mattermost-team-2.0.0-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/2.0.0/mattermost-team-2.0.0-linux-amd64.tar.gz`
  - Checksum: `005687c6a8128e1e40d01933f09d7da1a1b70b149a6bef96d923166bc1e7ce8f`
- Mattermost Team Edition v1.4.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v1-4-0) - [Download](https://releases.mattermost.com/1.4.0/mattermost-team-1.4.0-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/1.4.0/mattermost-team-1.4.0-linux-amd64.tar.gz`
  - Checksum: `0874dad79415066466c22ac584e599897124106417e774818cf40864d202dbb0`
- Mattermost Team Edition v1.3.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v1-3-0) - [Download](https://releases.mattermost.com/1.3.0/mattermost-team-1.3.0-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/1.3.0/mattermost-team-1.3.0-linux-amd64.tar.gz`
  - Checksum: `57af87ae8a98743b5379ed70f93a923654f7b8547f89b7f99ef9a718f472364d`
- Mattermost Team Edition v1.2.1 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v1-2-1) - [Download](https://releases.mattermost.com/1.2.1/mattermost-team-1.2.1-linux-amd64.tar.gz)
  - `https://releases.mattermost.com/1.2.1/mattermost-team-1.2.1-linux-amd64.tar.gz`
  - Checksum: `f4cc5b0e1026026ff0cea4cc915b92967f9dfdf497c249731dc804a9a2ff156d`
- Mattermost Team Edition v1.1.1 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v1-1-1) - [Download](https://releases.mattermost.com/1.1.1/mattermost-team-1.1.1-linux-amd64.tar.gz)
   - `https://releases.mattermost.com/1.1.1/mattermost-team-1.1.1-linux-amd64.tar.gz`
   - Checksum: `e6687b9d7f94538e1f4a9f93a0bcb8a66e293e2260433ed648964baa53c3e561`
- Mattermost Team Edition v1.0.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html##release-v1-0-0) - [Download](https://releases.mattermost.com/1.0.0/mattermost-team-1.0.0-linux-amd64.tar.gz)
   - `https://releases.mattermost.com/1.0.0/mattermost-team-1.0.0-linux-amd64.tar.gz`
   - Checksum: `208b429cc29119b3d3c686b8973d6100eb02845b1da2f18744195f055521cbc8`
- Mattermost Team Edition v0.7.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v0-7-0-beta) - [Download](https://releases.mattermost.com/0.7.0/mattermost-team-0.7.0-linux-amd64.tar.gz)
   - `https://releases.mattermost.com/0.7.0/mattermost-team-0.7.0-linux-amd64.tar.gz`
   - Checksum: `f0a0e5b5fab3aeb5dc638ab3059b3ea5bf7bc1ec5123db1199aa10db41bfffb1`
- Mattermost Team Edition v0.6.0 - [View Changelog](https://docs.mattermost.com/administration/changelog.html#release-v0-6-0-alpha) - [Download](https://releases.mattermost.com/0.6.0/mattermost-team-0.6.0-linux-amd64.tar.gz)
   - `https://releases.mattermost.com/0.6.0/mattermost-team-0.6.0-linux-amd64.tar.gz`
   - Checksum: `9eb364f7f963af32d4a9efe3bbb5abb2a21ca5d1a213b50ca461dab047a123b6`
