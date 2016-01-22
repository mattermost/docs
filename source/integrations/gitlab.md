# GitLab
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
