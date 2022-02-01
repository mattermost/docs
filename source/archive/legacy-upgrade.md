# Upgrading from an Unsupported Version

These instructions apply only if you're upgrading from an unsupported version of Mattermost to the latest version. Only the current released version and the two previous versions are supported.

If you're upgrading a server that's already running a supported version, See [Upgrading Mattermost Server](../../administration/upgrade.html).

## Upgrade Team Edition from 3.0.0 and later

### Important Notices

1. Security-related changes were made in 3.9.0 that cause any previously created team invite links, password reset links, and email verification links to no longer work. You must update any place where you have published these links.

2. Security-related changes were made in 3.6.7, 3.7.5, and 3.8.0 that require you to verify settings in the System Console before upgrading.

    - Go to **System Console > Environment > Web Server**, then select **Configuration** and make sure that the **Site URL** is specified. It must not be empty. For more information about SiteURL, see [Configuration Settings](../../administration/config-settings.html#site-url).
    - Go to **System Console > Environment > Logging**, then select **Logging** and make sure that the **File Log Directory** field is either empty or has a directory path only. It must not have a filename as part of the path.

3. Changes were made in 3.8.0 that require a change in the proxy configuration. If you're using NGINX:
    1. Open the NGINX configuration file as *root*. The file is usually ``/etc/nginx/sites-available/mattermost`` but might be different on your system.
    2. Locate the following line:
     `location /api/v3/users/websocket {`
    3. Replace the  line with ``location ~ /api/v[0-9]+/(users/)?websocket$ {``.

    If you're using a proxy other than NGINX, make the equivalent change to that proxy's configuration.

4. RHEL6 and Ubuntu installations must verify the line `limit nofile 50000 50000` is included in `/etc/init/mattermost.conf` file. See the [installation guide](../../guides/administrator.html#install-guides) for your operating system for more details.

5. RHEL7 and Ubuntu installations must verify the line `LimitNOFILE=49152` is included in the `/etc/systemd/system/mattermost.service` file. See the [installation guide](../../guides/administrator.html#install-guides) for your operating system for more details.

**Upgrading from 3.0.0 and later**

1. Download the latest version of Team Edition server and note any compatibility procedures:
      1. Review past and upcoming deprecation notices [listed on our website](https://about.mattermost.com/deprecated-features/).
      2. Download [the latest version of the Mattermost Server](https://mattermost.com/deploy/). In the following command, replace `X.X.X` with the version that you want to download:
          - **Team Edition**: `wget https://releases.mattermost.com/X.X.X/mattermost-team-X.X.X-linux-amd64.tar.gz`
2. Stop the Mattermost server
      1. Consider posting an announcement to active teams about stopping the Mattermost server for an upgrade.
      2. To stop the server run `sudo stop mattermost`.
3. Back up your data
      1. Back up your `config.json` file, which contains your system configuration. This will be used to restore your current settings after the new version is installed.
      2. Back up your database using your organization's standard procedures for backing up MySQL or PostgreSQL.
      3. If you're using local file storage, back up the location where files are stored.
4. Install the new version
      1. Run `tar -xvzf mattermost-team-X.X.X-linux-amd64.tar.gz` to decompress the upgraded version and replace the current version of Mattermost on disk, where `X.X.X` is the version number to which you are upgrading.
5. Restore the state of your server
      1. Copy the backed up version of `config.json` in place of the default `config.json`.
6. Start your server and address any setting changes relevant in the latest version of Mattermost
      1. Run `sudo start mattermost`.
      2. Open the System Console and save a change to upgrade your `config.json` schema to the latest version using default values for any new settings added.
7. If you have TLS set up on your Mattermost server, you must activate the CAP_NET_BIND_SERVICE capability to allow the new Mattermost binary to bind to low ports
      1. `cd {install-path}`
      2. `sudo setcap cap_net_bind_service=+ep ./bin/mattermost`

After the server is upgraded, users might need to refresh their browsers to experience any new features.

## Upgrade Enterprise Edition from 3.0.0 and later

### Important Notices

1. Security-related changes were made in 3.9.0 that cause any previously created team invite links, password reset links, and email verification links to no longer work. You must update any place where you have published these links.

2. Security-related changes were made in 3.6.7, 3.7.5, and 3.8.0 that require you to verify settings in the System Console before upgrading from version 3.5.3 and earlier to any version greater than 3.6.7.
    1. Go to **System Console > Environment > Web Server**, then select **Configuration** and make sure that the **Site URL** is specified. It must not be empty. For more information about SiteURL, see [Configuration Settings](../../administration/config-settings.html#site-url).
    2. Go to **System Console > Environment > Logging**, then select **Logging** and make sure that the **File Log Directory** field is either empty or has a directory path only. It must not have a filename as part of the path.

3. Changes were made in 3.8.0 that require a change in the proxy configuration. If you're using NGINX:
    1. Open the NGINX configuration file as root. The file is usually ``/etc/nginx/sites-available/mattermost`` but might be different on your system.
    2. Locate the following line:
     `location /api/v3/users/websocket {`
    3. Replace the  line with ``location ~ /api/v[0-9]+/(users/)?websocket$ {``.

    If you're using a proxy other than NGINX, make the equivalent change to that proxy's configuration.
    
4. If there are config settings set for `"RestrictPublicChannelManagement"` and `"RestrictPrivateChannelManagement"`, they will be used as the default values for `"RestrictPublicChannelCreation"`, `"RestrictPrivateChannelCreation"`, `"RestrictPublicChannelDeletion"`, and `"RestrictPrivateChannelDeletion"` after upgrade.

5. If public links are enabled, upgrading from `v3.3.x` and earlier to `v3.4.x` and later will invalidate existing public links due to a security upgrade allowing admins to invalidate links by resetting a public link salt from the System Console.

6. RHEL6 and Ubuntu installations must verify the line `limit nofile 50000 50000` is included in `/etc/init/mattermost.conf` file. See the [installation guide](https://docs.mattermost.com/guides/administrator.html#install-guides) for your operating system for more details.
7. RHEL7 and Ubuntu installations must verify the line `LimitNOFILE=49152` is included in the `/etc/systemd/system/mattermost.service` file. See the [installation guide](https://docs.mattermost.com/guides/administrator.html#install-guides) for your operating system for more details.

**Upgrading from 3.0.0 and later**

1. Download the latest version of Enterprise Edition server and note any compatibility procedures:
      1. Review past and upcoming deprecation notices [listed on our website](https://about.mattermost.com/deprecated-features/).
      2. Download [the latest version of the Mattermost Server](https://mattermost.com/download/). In the following command, replace `X.X.X` with the version that you want to download:
          - **Enterprise Edition:** `wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz`
2. Stop the Mattermost server
      1. Consider posting an announcement to active teams about stopping the Mattermost server for an upgrade.
      2. To stop the server run `sudo stop mattermost`.
3. Back up your data
      1. Back up your `config.json` file, which contains your system configuration. This will be used to restore your current settings after the new version is installed.
      2. Back up your database using your organization's standard procedures for backing up MySQL or PostgreSQL.
      3. If you're using local file storage, back up the location where files are stored.
4. Install the new version
      1. Run `tar -xvzf mattermost-X.X.X-linux-amd64.tar.gz` to decompress the upgraded version and replace the current version of Mattermost on disk, where `X.X.X` is the version number to which you are upgrading.  
5. Restore the state of your server
      1. Copy the backed up version of `config.json` in place of the default `config.json`.
6. Start your server and address any setting changes relevant in the latest version of Mattermost
      1. Run `sudo start mattermost`.
      2. Open the System Console and save a change to upgrade your `config.json` schema to the latest version using default values for any new settings added.
7. If you have TLS set up on your Mattermost server, you must activate the CAP_NET_BIND_SERVICE capability to allow the new Mattermost binary to bind to low ports

      1. ``cd {install-path}``
      2. ``sudo setcap cap_net_bind_service=+ep ./bin/platform``

After the server is upgraded, users might need to refresh their browsers to experience any new features.

## Upgrade Team Edition to 3.0.3

In Mattermost 3.0 users can maintain a single account across multiple teams on a Mattermost server. This means one set of credentials, one place to configure all account settings, and a more streamlined sign-up and team joining process.

If your Mattermost server has duplicate accounts (users with multiple accounts in multiple teams with the same email address or username), you need to understand the 3.0 upgrade process in detail and take special steps to upgrade successfully.

1. Download Mattermost Team Edition 3.0.3:
      1. Run `platform -version` to confirm the current version of your Mattermost server is `v2.2.0`, `v2.1.0`, or `v2.0.0`. If not, please [upgrade to `v2.0.0`](https://docs.mattermost.com/administration/legacy-upgrade.html#upgrade-team-edition-to-2-2-x-and-earlier).
      2. Run `wget https://releases.mattermost.com/X.X.X/mattermost-team-X.X.X-linux-amd64.tar.gz` to download the appropriate new version.
2. Stop the Mattermost server
      1. Consider posting an announcement to active teams about stopping the Mattermost server for an upgrade
      2. To stop the server run `sudo stop mattermost`
3. Back up your data
      1. Back up your `config.json` file, which contains your system configuration. This will be used to restore your current settings after the new version is installed.
      2. Back up your database using your organization's standard procedures for backing up MySQL or PostgreSQL.
      3. If you're using local file storage, back up the location where files are stored. This location is specified in the `config.json` file under `FileSettings` > `Directory`.
      4. Verify your backups are successful.
4. Install the new version
      1. Double check that your database and configuration file has been backed up, as the database upgrade to 3.x from 2.x cannot be reversed.
      2. Run `tar -xvzf mattermost-team-X.X.X-linux-amd64.tar.gz` to decompress the upgraded version and replace the current version of Mattermost on disk, where `X.X.X` is the version number to which you are upgrading.
5. Restore the state of your server
      1. Copy the backed up version of `config.json` in place of the default `config.json`.
      2. If you're using local file storage, restore the data you backed up before running the server. Keep the backup until you're sure the upgrade has succeeded.
6. Upgrade your database
      1. Run `./platform -upgrade_db_30` to upgrade your database from 2.x to 3.x
         - You may need to run with `sudo -u linux_user_account ./platform -upgrade_db_30` if you've setup Mattermost to run under a different account.  This will ensure files under `./data/` have the correct permissions.
         - You will be asked `Have you performed a database backup? (YES/NO):`
             - If you have not backed up your database, enter `NO` and then back up your database.
             - If you have verified your database has been backed up, enter `YES`.
         - You will be asked to select a `primary team`.
             - If you only have one team, enter the name of the team.
             - If you have more than one team, specify the `primary team` based on the team you use the most.
                  - If your server contains duplicate accounts (multiple accounts with either the same email addresses or the same usernames) the user account in the `primary team` will be considered the primary account and remain unchanged.
                     - When the server finds a duplicate account not in the `primary team` the email address of the account may be changed to avoid conflicts.
                         - An account with a **duplicate email address** will be updated so `+[TEAM_URL_NAME]` is appended to the local part of the email address. For example: An account with a duplicate email `steve@company.com` in the team at URL `https://mattermost.company.com/marketing` becomes `steve+marketing@company.com`. The `+marketing` used in this procedure is part of the RFC5233 email specification and most email systems will properly route `steve+marketing@company.com` to `steve@company.com`. After the upgrade, if email authentication is used for sign-in, the user would need to sign-in with the new email address.
                         - An account with a **duplicate username** will be updated so `[TEAM_URL_NAME].`” is prepended to the username. For example: An account with a duplicate username `steve` in the team at URL `https://mattermost.company.com/marketing` becomes `marketing.steve`.
         - Users with accounts containing duplicate emails or usernames will receive a notification email explaining the upgrade, and instructions on how to move to a single user account ([see example](https://mattermost.org/upgrade-to-3-0/)).
7. Start your server and address any setting changes relevant in the latest version of Mattermost
      1. Run `sudo start mattermost`.
      2. Open the System Console and save a change to upgrade your `config.json` schema to the latest version using default values for any new settings added.
8. If you have TLS set up on your Mattermost server, run `sudo setcap cap_net_bind_service=+ep ./bin/platform` in your Mattermost directory to allow Mattermost to bind to low ports
9. Test the system is working by going to the URL of the server with an `https://` prefix
      1. You may need to refresh your Mattermost browser page in order to get the latest updates from the upgrade.
10. After the Mattermost 3.0 upgrade, users with duplicate accounts must follow the instructions in the upgrade email to:
      1. Log in to teams on which duplicate accounts were created.
      2. Add their primary account to the team and any private channels that are still actively used.

   Users can continue to access the direct message history of their duplicate accounts using their updated email addresses.

## Upgrade Team Edition to 2.2.0 and earlier

1. Download the **appropriate next upgrade** of your Team Edition server and note any compatibility procedures:
      1. Run `platform -version` to check the current version of your Mattermost server
      2. Determine the appropriate next upgrade for your server:
          - Mattermost `v2.0.x` and `v2.1.x` can upgrade directly to Mattermost `v2.2.x`.
          - Mattermost `v1.4.x` and `v2.0.x` can upgrade directly to Mattermost `v2.1.x`.
          - Mattermost `v1.2.x` must upgrade to Mattermost `v1.3.x` before further upgrades.
          - Mattermost `v1.1.x` must upgrade to Mattermost `v1.2.x` before further upgrades.
          - Mattermost `v1.0.x` must upgrade to Mattermost `v1.1.x` before further upgrades.
      3. Use the [Version Archive List](https://docs.mattermost.com/administration/upgrade.html#version-archive) to find the `[RELEASE URL]` for your desired version and enter `wget {RELEASE URL}` to download. For example, to download `vX.X.X`, use `wget https://releases.mattermost.com/X.X.X/mattermost-team-X.X.X-linux-amd64.tar.gz`.
      4. Review the **Compatibility** section in [CHANGELOG](https://docs.mattermost.com/administration/changelog.html) for the version downloaded and make sure to follow any instructions.
2. Stop the Mattermost server
      1. Consider posting an announcement to active teams about stopping the Mattermost server for an upgrade.
      2. To stop the server run `sudo stop mattermost`.
3. Back up your data
      1. Back up your `config.json` file, which contains your system configuration. This will be used to restore your current settings after the new version is installed.
      2. Back up your database using your organization's standard procedures for backing up MySQL or PostgreSQL.
      3. If you're using local file storage, back up the location where files are stored.
5. Install the new version
      1. Run `tar -xvzf mattermost-team-X.X.X-linux-amd64.tar.gz` to decompress the upgraded version and replace the current version of Mattermost on disk, where `X.X.X` is the version number to which you are upgrading.  
6. Restore the state of your server
      1. Copy the backed up version of `config.json` in place of the default `config.json`.
7. Start your server and address any setting changes relevant in the latest version of Mattermost
      1. Run `sudo start mattermost`.
      2. Open the System Console and save a change to upgrade your `config.json` schema to the latest version using default values for any new settings added.
8. If you have TLS set up on your Mattermost server, run `sudo setcap cap_net_bind_service=+ep ./bin/platform` in your Mattermost directory to allow Mattermost to bind to low ports
9. Test the system is working by going to the URL of the server with an `https://` prefix
      1. You may need to refresh your Mattermost browser page in order to get the latest updates from the upgrade.

## Upgrade Enterprise Edition to 3.0.3

In Mattermost 3.0 users can maintain a single account across multiple teams on a Mattermost server. This means one set of credentials, one place to configure all account settings, and a more streamlined sign up and team joining process.

If your Mattermost server has duplicate accounts (users with multiple accounts in multiple teams with the same email address or username), you need to understand the 3.0 upgrade process in detail and take special steps to upgrade successfully.

1. Download Mattermost Enterprise Edition 3.0.3
      1. Run `platform -version` to confirm the current version of your Mattermost server is `v2.2.0`, `v2.1.1`, or `v2.0.0` of either Mattermost Enterprise Edition or Mattermost Team Edition. If not, please [upgrade to at least Mattermost Enterprise Edition `v2.0.0`](https://docs.mattermost.com/administration/legacy-upgrade.html#upgrade-enterprise-edition-to-2-2-x-and-earlier).
      2. Run `wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz` to download the appropriate new version.
2. Stop the Mattermost server
      1. Consider posting an announcement to active teams about stopping the Mattermost server for an upgrade.
      2. To stop the server run `sudo stop mattermost`.
3. Back up your data
      1. Back up your `config.json` file, which contains your system configuration. This will be used to restore your current settings. after the new version is installed.
      2. Back up your database using your organization's standard procedures for backing up MySQL or PostgreSQL.
      3. If you're using local file storage, back up the location where files are stored.
      4. Verify your backups are successful.
4. Install the new version
      1. Double check that your database and configuration file has been backed up, as the database upgrade to 3.x from 2.x cannot be reversed.
      2. Run `tar -xvzf mattermost-X.X.X-linux-amd64.tar.gz` to decompress the upgraded version and replace the current version of Mattermost on disk, where `X.X.X` is the version number to which you are upgrading.
5. Restore the state of your server
      1. Copy the backed up version of `config.json` in place of the default `config.json`.
6. Upgrade your database
      1. Run `./platform -upgrade_db_30` to upgrade your database from 2.x to 3.x.
         - You may need to run with `sudo -u linux_user_account ./platform -upgrade_db_30` if you've setup Mattermost to run under a different account.  This will ensure files under `./data/` have the correct permissions.
         - You will be asked `Have you performed a database backup? (YES/NO):`
             - If you have not backed up your database, enter `NO` and then back up your database.
             - If you have verified your database has been backed up, enter `YES`.
         - You will be asked to select a `primary team`.
             - If you only have one team, enter the name of the team.
             - If you have more than one team, specify the `primary team` based on the team you use the most.
                  - If your server contains duplicate accounts (multiple accounts with either the same email addresses or the same usernames) the user account in the `primary team` will be considered the primary account and remain unchanged.
                     - When the server finds a duplicate account not in the `primary team` the email address of the account may be changed to avoid conflicts
                         - An account with a **duplicate email address** will be updated so `+[TEAM_URL_NAME]` is appended to the local part of the email address. For example: An account with a duplicate email `steve@company.com` in the team at URL `https://mattermost.company.com/marketing` becomes `steve+marketing@company.com`. The `+marketing` used in this procedure is part of the RFC5233 email specification and most email systems will properly route `steve+marketing@company.com` to `steve@company.com`. After the upgrade, if email authentication is used for sign-in, the user would need to sign-in with the new email address.
                         - An account with a **duplicate username** will be updated so `[TEAM_URL_NAME].`” is prepended to the username. For example: An account with a duplicate username `steve` in the team at URL `https://mattermost.company.com/marketing` becomes `marketing.steve`.
         - Users with accounts containing duplicate emails or usernames will receive a notification email explaining the upgrade, and instructions on how to move to a single user account ([see example](https://mattermost.org/upgrading-to-mattermost-3-0/#notification))
7. Start your server and address any setting changes relevant in the latest version of Mattermost
      1. Run `sudo start mattermost`.
      2. Open the System Console and save a change to upgrade your `config.json` schema to the latest version using default values for any new settings added.
8. If you have TLS set up on your Mattermost server, run `sudo setcap cap_net_bind_service=+ep ./bin/platform` in your Mattermost directory to allow Mattermost to bind to low ports
9. Test the system is working by going to the URL of the server with an `https://` prefix
      1. You may need to refresh your Mattermost browser page in order to get the latest updates from the upgrade.
10. After the Mattermost 3.0 upgrade, users with duplicate accounts must follow the instructions in the upgrade email to:
      1. Log in to teams on which duplicate accounts were created.
      2. Add their primary account to the team and any private channels that are still actively used.

   Users can continue to access the direct message history of their duplicate accounts using their updated email addresses.

For any issues, Mattermost Enterprise Edition subscribers and trial license users can email support@mattermost.com.

## Upgrade Enterprise Edition to 2.2.0 and earlier

1. Download the **appropriate next upgrade** of your Enterprise Edition server and note any compatibility procedures.
      1. Run `platform -version` to check the current version of your Mattermost server.
      2. Determine the appropriate next upgrade for your server:
          - Mattermost `v2.0.x` and `v2.1.x` can upgrade directly to Mattermost `v2.2.0`.
          - Mattermost `v1.4.x` and `v2.0.x` can upgrade directly to Mattermost `v2.1.0`.
          - Mattermost `v1.2.x` must upgrade to Mattermost `v1.3.x` before further upgrades.
          - Mattermost `v1.1.x` must upgrade to Mattermost `v1.2.x` before further upgrades.
          - Mattermost `v1.0.x` must upgrade to Mattermost `v1.1.x` before further upgrades.
      3. Use the [Version Archive List](https://docs.mattermost.com/administration/upgrade.html#version-archive) to find the `[RELEASE URL]` for your desired version and enter `wget {RELEASE URL}` to download. For example, to download `vX.X.X`, use `wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz`.
      4. Review the **Compatibility** section in [CHANGELOG](https://docs.mattermost.com/administration/changelog.html) for the version downloaded and make sure to follow any instructions.
2. Stop the Mattermost server
      1. Consider posting an announcement to active teams about stopping the Mattermost server for an upgrade.
      2. To stop the server run `sudo stop mattermost`.
3. Back up your data
      1. Back up your `config.json` file, which contains your system configuration. This will be used to restore your current settings after the new version is installed.
      2. Back up your database using your organization's standard procedures for backing up MySQL or PostgreSQL.
      3. If you're using local file storage, back up the location where files are stored.
5. Install the new version
      1. Run `tar -xvzf mattermost-X.X.X-linux-amd64.tar.gz` to decompress the upgraded version and replace the current version of Mattermost on disk, where `X.X.X` is the version number to which you are upgrading.  
6. Restore the state of your server
      1. Copy the backed up version of `config.json` in place of the default `config.json`.
7. Start your server and address any setting changes relevant in the latest version of Mattermost
      1. Run `sudo start mattermost`.
      2. Open the System Console and save a change to upgrade your `config.json` schema to the latest version using default values for any new settings added.
8. If you have TLS set up on your Mattermost server, run `sudo setcap cap_net_bind_service=+ep ./bin/platform` in your Mattermost directory to allow Mattermost to bind to low ports
9. Test the system is working by going to the URL of the server with an `https://` prefix
      1. You may need to refresh your Mattermost browser page in order to get the latest updates from the upgrade.

For any issues, Mattermost Enterprise Edition subscribers and trial license users can email support@mattermost.com.
