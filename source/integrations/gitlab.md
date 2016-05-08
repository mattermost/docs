# GitLab Mattermost Administration 

GitLab Mattermost is a special version of Mattermost bundled with GitLab omnibus. Here we consolidate administrative instructions, guides and troubleshooting guidance.

## Community Support Resources

For help and support around your GitLab Mattermost deployment please see:

- [Troubleshooting Forum](https://forum.mattermost.org/t/about-the-trouble-shooting-category/150/1) for configuration questions and issues
- [GitLab Mattermost issue tracker](https://gitlab.com/gitlab-org/gitlab-mattermost/issues) for verified bugs with repro steps

## Deploying GitLab Mattermost 

### Installing GitLab Mattermost

Please follow the [GitLab Omnibus documentation for installing GitLab Mattermost](http://doc.gitlab.com/omnibus/gitlab-mattermost/).

## Troubleshooting GitLab Mattermost

- If you're having issues installing GitLab Mattermost with GitLab Omnibus, as a first step please turn on logging by updating the [log settings](http://docs.mattermost.com/administration/config-settings.html#log-settings) section in your `config.json` file installed by omnibus, and they try a general web search for the error message you receive. 

### GitLab Mattermost Error Messages
 
###### `We received an unexpected status code from the server (200)`

- If you have upgraded from a pre-released version of GitLab Mattermost or if an unforseen issue has arrisen during the [upgrade procedure](http://docs.mattermost.com/administration/upgrade.html#upgrade-guide), you may be able to restore Mattermost using the following procedure: 
  - `sudo stop mattermost`, so DB can be dropped 
  - `sudo gitlab-ctl reconfigure`
  - `sudo -u gitlab-psql /opt/gitlab/embedded/bin/dropdb -h /var/opt/gitlab/postgresql mattermost_production`
  - `sudo start mattermost`
  - `sudo gitlab-ctl reconfigure`
  - [Manually set up GitLab SSO](http://docs.mattermost.com/deployment/sso-gitlab.html#gitlab) by copying Secret and ID into `/var/opt/gitlab/mattermost/config.json` 
  - `sudo gitlab-ctl restart`

###### `Token request failed`
 - This error can appear in the web browser after attempting to create a new team with GitLab SSO enabled
 - **Solutions:** 
   1. Check that your SSL settings for the SSO provider match the `http://` or `https://` choice selected in `config.json` under `GitLabSettings`
   2. Follow steps 1 to 3 of the manual [GitLab SSO configuration procedure](http://docs.mattermost.com/deployment/sso-gitlab.html#gitlab) to confirm your `Secret` and `Id` settings in `config.json` match your GitLab settings, and if they don't, manually update `config.json` to the correct settings and see if this clears the issue. 

###### `"The redirect URI included is not valid.`
  - This error may be related to SSL configurations in your proxy after a GitLab omnibus upgrade from 8.0, which contained the Mattermost beta version.
  - **Solution:** 
    - Please check that each step of [the procedure for upgrading Mattermost in GitLab 8.0 to GitLab 8.1 was completed]http://docs.mattermost.com/integrations/gitlab.html#upgrading-gitlab-mattermost). Then check upgrades to successive major versions were completed using the procedure in the [Upgrade Guide](http://docs.mattermost.com/administration/upgrade.html#upgrading-team-edition).


###### `We couldn't find the existing account ...`
  - This error appears when a user attempts to sign in using a single-sign-on option with an account that was not created using that single-sign-on option. For example, if a user creates Account A using email sign-up, then attempts to sign-in using GitLab SSO, the error appears since Account A was not created using GitLab SSO. 
  - **Solution:** 
    - If you're switching from email auth to GitLab SSO, and you're getting this issue on an admin account, consider deactivating your email-based account, then creating a new account with System Admin privileges using GitLab SSO. Specifically: 
       1. Deactivate your email-based System Admin account (note: this process is [scheduled to improve](https://mattermost.atlassian.net/browse/PLT-975))
         1. Temporarily turn off email verification (**System Console** > **Email Settings** > **Require Email Verification** > **false**, or set `"RequireEmailVerification": false` in `config.json`).
         2. Change email for account to random address so you can create a new GitLab SSO account using your regular address.
       2. Create a new Mattermost account using GitLab SSO
         1. With GitLab SSO enabled, go to `https://domain.com/teamname` and sign-up for a new Mattermost account using your GitLab SSO account with preferred email address.
         2. [Upgrade the new account to System Admin privileges](http://docs.mattermost.com/install/troubleshooting.html#lost-system-administrator-account).
       3. Deactivate the previous System Admin account that used email authentication.
         1. Using the new GitLab SSO System Admin account go to **System Console** > **[TEAMNAME]** > **Users**, find the previous account and set it to "Inactive"

##### `panic: The database schema version of 1.1.0 cannot be upgraded. You must not skip a version`
- This error may appear in your `/var/log/gitlab/mattermost/current` if you're attempting to skip major versions when upgrading GitLab Mattermost (e.g. running an upgrade from GitLab 8.2.x to 8.4.x, instead of running from 8.2.x to 8.3.x to 8.4.x which is required for GitLab Mattermost). To address this: 
    1. Run `platform -version` to check your version of Mattermost 
    2. If your version of the Mattermost binary doesn't match the version listed in the database error message, downgrade the version of the Mattermost binary you are using by [following the manual upgrade steps for Mattermost](http://docs.mattermost.com/administration/upgrade.html#upgrading-team-edition) and using the database schema version listed in the error messages for the version you select in Step 1) iv). 
    3. Once Mattermost is working again, you can use the same upgrade procedure to upgrade Mattermost version by version to your current GitLab version. After this is done, GitLab automation should continue to work for future upgrades, so long as you don't skip versions. 

### Upgrading from GitLab Mattermost Beta

#### Legacy: Upgrading Mattermost in GitLab 8.0

Mattermost 0.7.1-beta in GitLab 8.0 was a pre-release of Mattermost and Mattermost v1.1.1 in GitLab 8.1 was [updated significantly](http://docs.mattermost.com/administration/changelog.html#config-json-changes-from-v0-7-to-v1-0) to get to a stable, forwards-compatible platform for Mattermost. 

The Mattermost team didn't think it made sense for GitLab omnibus to attempt an automated re-configuration of Mattermost (since 0.7.1-beta was a pre-release) given the scale of change, so we're providing instructions for GitLab users who have customized their Mattermost deployments in 8.0 to move to 8.1: 

1. Follow the [Upgrading Mattermost v0.7.1-beta to v1.1.1 instructions](http://docs.mattermost.com/administration/upgrade.html#upgrading-team-edition) below to identify the settings in Mattermost's `config.json` file that differ from defaults and need to be updated from GitLab 8.0 to 8.1
2. Upgrade to GitLab 8.1 using omnibus, and allowing it overwrite `config.json` to the new Mattermost v1.1.1 format
3. Manually update `config.json` to new settings identified in Step 1

Optionally, you can use the new [System Console user interface](http://docs.mattermost.com/administration/config-settings.html#configuration-settings) to make changes to your new `config.json` file.

#### Legacy: Upgrading Mattermost v0.7.1-beta to v1.1.1

_Note: [Mattermost v1.1.1](https://github.com/mattermost/platform/releases/tag/v1.1.1) is a special release of Mattermost v1.1 that upgrades the database to Mattermost v1.1 from EITHER Mattermost v0.7 or Mattermost v1.0. The following instructions are for upgrading from Mattermost v0.7.1-beta to v1.1.1 and skipping the upgrade to Mattermost v1.0._

If you've manually changed Mattermost v0.7.1-beta configuration by updating the `config.json` file, you'll need to port those changes to Mattermost v1.1.1: 

1. Go to the `config.json` file that you manually updated and note any differences from the [default `config.json` file in Mattermost 0.7](https://github.com/mattermost/platform/blob/v0.7.0/config/config.json). 

2. For each setting that you changed, check [the changelog documentation](http://docs.mattermost.com/administration/changelog.html#config-json-changes-from-v0-7-to-v1-0) on whether the configuration setting has changed between v0.7 and v1.1.1

3. Update your new [`config.json` file in Mattermost v1.1](https://github.com/mattermost/platform/blob/v1.1.0/config/config.json), based on your preferences and the changelog documentation above

Optionally, you can use the new [System Console user interface](http://docs.mattermost.com/administration/config-settings.html#configuration-settings) to make changes to your new `config.json` file.
