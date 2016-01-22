# GitLab

## GitLab Mattermost Administration 

GitLab Mattermost is a special version of Mattermost bundled with GitLab omnibus. Here we consolidate administrative instructions, guides and troubleshooting guidance.

### Installing GitLab Mattermost

Please follow the [GitLab Omnibus documentation for installing GitLab Mattermost](http://doc.gitlab.com/omnibus/gitlab-mattermost/).

### Community Support Resources

For help and support around your GitLab Mattermost deployment please see:

- [Troubleshooting Forum](https://forum.mattermost.org/t/about-the-trouble-shooting-category/150/1)
- [GitLab Mattermost issue tracker on GitLab.com](https://gitlab.com/gitlab-org/gitlab-mattermost/issues)

___

### GitLab notifications in Mattermost

There are multiple ways to send notifications depending on how much control you'd like over the messages. 

#### Setting up Mattermost as a Slack project service integration:

Mattermost is "Slack-compatible, not Slack-limited" so if you like Slack's default formatting you can use their project service option to set up Mattermost integration: 

1. In Mattermost go to **Account Settings** > **Integrations** > **Incoming Webhooks** 
2. Select a channel and click **Add* and copy the `Webhook URL`
3. In GitLab, go to **Settings** > **Project Services** > **Slack** and paste in the `Webhook URL` into **Webhook** 
4. Enter **Username** for how you would like to name the account that posts the notifications
4. Select **Triggers** for GitLab events on which you'd like to receive notifications
6. Click **Save changes** then **Test settings** to make sure everything is working

Any issues, please see the [Mattermost Troubleshooting Forum](https://forum.mattermost.org/t/how-to-use-the-troubleshooting-forum/150).

#### Setting up GitLab integration service for Mattermost 

You can also set up the [open source integration service](https://github.com/NotSqrt/mattermost-integration-gitlab) to let you configure notifications on GitLab issues, pushes, build events, merge requests and comments to be delivered to selected Mattermost channels. 

This integration lets you completely control how notifications are formatted and, unlike Slack, offers full markdown support. 

The source code can be modified to support not only GitLab, but any in-house applications you may have that support webhooks. Also see: 
- [Mattermost incoming webhook documentation](http://docs.mattermost.com/developer/webhooks-incoming.html)
- [GitLab webhook documentation](http://doc.gitlab.com/ce/web_hooks/web_hooks.html)

![webhooks](https://gitlab.com/gitlab-org/omnibus-gitlab/uploads/677b0aa055693c4dcabad0ee580c61b8/730_gitlab_feature_request.png)



### Upgrading GitLab Mattermost manually

If you choose to upgrade Mattermost outside of GitLab's omnibus automation, please [follow this guide](https://github.com/mattermost/platform/blob/master/doc/install/Upgrade-Guide.md#upgrading-mattermost-to-next-major-release).

### Upgrading GitLab Mattermost from GitLab 8.0 (containing Mattermost 0.7.1-beta)

To upgrade GitLab Mattermost from the 0.7.1-beta release of Mattermost in GitLab 8.0, please [follow this guide](https://github.com/mattermost/platform/blob/master/doc/install/Upgrade-Guide.md#upgrading-mattermost-in-gitlab-80-to-gitlab-81-with-omnibus).

### Troubleshooting GitLab Mattermost

- If you're having issues installing GitLab Mattermost with GitLab Omnibus, as a first step please turn on logging by updating the [log settings](https://github.com/mattermost/platform/blob/master/doc/install/Configuration-Settings.md#log-file-settings) section in your `config.json` file installed by omnibus, and they try a general web search for the error message you receive. 

#### GitLab Mattermost Error Messages

###### `We received an unexpected status code from the server (200)`

- If you have upgraded from a pre-released version of GitLab Mattermost or if an unforseen issue has arrisen during the [upgrade procedure](https://github.com/mattermost/platform/blob/master/doc/install/Upgrade-Guide.md), you may be able to restore Mattermost using the following procedure: 
  - `sudo stop mattermost`, so DB can be dropped 
  - `sudo gitlab-ctl reconfigure`
  - `sudo -u gitlab-psql /opt/gitlab/embedded/bin/dropdb -h /var/opt/gitlab/postgresql mattermost_production`
  - `sudo start mattermost`
  - `sudo gitlab-ctl reconfigure`
  - [Manually set up GitLab SSO](https://github.com/mattermost/platform/blob/master/doc/integrations/Single-Sign-On/Gitlab.md) by copying Secret and ID into `/var/opt/gitlab/mattermost/config.json` 
  - `sudo gitlab-ctl restart`

###### `Token request failed`
 - This error can appear in the web browser after attempting to create a new team with GitLab SSO enabled
 - **Solutions:** 
   1. Check that your SSL settings for the SSO provider match the `http://` or `https://` choice selected in `config.json` under `GitLabSettings`
   2. Follow steps 1 to 3 of the manual [GitLab SSO configuration procedure](https://github.com/mattermost/platform/blob/master/doc/integrations/Single-Sign-On/Gitlab.md) to confirm your `Secret` and `Id` settings in `config.json` match your GitLab settings, and if they don't, manually update `config.json` to the correct settings and see if this clears the issue. 

###### `"The redirect URI included is not valid.`
  - This error may be related to SSL configurations in your proxy after a GitLab omnibus upgrade from 8.0, which contained the Mattermost beta version.
  - **Solution:** 
    - Please check that each step of [the procedure for upgrading Mattermost in GitLab 8.0 to GitLab 8.1 was completed](https://github.com/mattermost/platform/blob/master/doc/install/Upgrade-Guide.md#upgrading-mattermost-in-gitlab-80-to-gitlab-81-with-omnibus). Then check upgrades to successive major versions were completed using the procedure in the [Upgrade Guide](https://github.com/mattermost/platform/blob/master/doc/install/Upgrade-Guide.md#upgrading-mattermost-to-next-major-release).


###### `We couldn't find the existing account ...`
  - This error appears when a user attempts to sign in using a single-sign-on option with an account that was not created using that single-sign-on option. For example, if a user creates Account A using email sign-up, then attempts to sign-in using GitLab SSO, the error appears since Account A was not created using GitLab SSO. 
  - **Solution:** 
    - If you're switching from email auth to GitLab SSO, and you're getting this issue on an admin account, consider deactivating your email-based account, then creating a new account with System Admin privileges using GitLab SSO. Specifically: 
       1. Deactivate your email-based System Admin account (note: this process is [scheduled to improve](https://mattermost.atlassian.net/browse/PLT-975))
         1. Temporarily turn off email verification (**System Console** > **Email Settings** > **Require Email Verification** > **false**, or set `"RequireEmailVerification": false` in `config.json`).
         2. Change email for account to random address so you can create a new GitLab SSO account using your regular address.
       2. Create a new Mattermost account using GitLab SSO
         1. With GitLab SSO enabled, go to `https://domain.com/teamname` and sign-up for a new Mattermost account using your GitLab SSO account with preferred email address.
         2. [Upgrade the new account to System Admin privileges](https://github.com/mattermost/platform/blob/master/doc/install/Troubleshooting.md#lost-system-administrator-account).
       3. Deactivate the previous System Admin account that used email authentication.
         1. Using the new GitLab SSO System Admin account go to **System Console** > **[TEAMNAME]** > **Users**, find the previous account and set it to "Inactive"
