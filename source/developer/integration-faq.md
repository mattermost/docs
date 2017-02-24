# Integrations FAQ
---

## What's the difference between incoming and outgoing webhooks? 

A webhook is a way for one app to send real-time data to another app. 

In Mattermost, incoming webhooks receive data from external applications and make a post in a specified channel. They're great for setting up notifications when something happens in an external application. 

Outgoing webhooks take data from Mattermost, and send it to an external application. Then the outgoing webhook can post a response back in Mattermost. They're great for listening in on channels, and then notifying external applications when a trigger word is said. 

## What is a slash command? 

A slash command is similar to an outgoing webhook, but instead of listening to a channel it is used as a command tool. This means if you type in a slash command it will not be posted to a channel, whereas an outgoing webhook is only triggered by posted messages. 

## What does Slack-compatible mean?

Slack compatible means that Mattermost accepts integrations that have a payload in the same format as Slack.  

If you have a Slack integration, you should be able to set it up in Mattermost without changing the format.   

## What if I have a webhook from somewhere other than Slack? 

If you have an integration that outputs a payload in a different format you need to write an intermediate application to act as a translation layer to change it to the format Mattermost uses. Since there’s currently no general standard for webhook formatting, this is unavoidable and just a part of how webhooks work. 

If there's no translation layer, Mattermost won't understand the data you're sending. 

## What are attachments? 

When "attachments" are mentioned in the integrations documentation, it refers to Slack's Message Attachments. These "attachments" can be optionally added as an array in the data sent by an integration, and are used to customize the formatting of the message.

We currently don't support the ability to attach files to a post made by an integration. 

## What do I do if my webhook post is too long?

We recommend breaking up the information into separate posts. 

If you're interested in Mattermost automatically splitting up integration posts that are too long, please [upvote this feature idea](https://mattermost.uservoice.com/forums/306457-general/suggestions/13878750-automatically-break-long-responses-from-integratio), or comment if it's something you would be interested in working on. 

If you would like to suggest alternative solutions, please [discuss here](https://forum.mattermost.org/t/recommendations-for-handling-automation-that-wants-to-post-messages-longer-than-4000-characters-per-message/1393).

## Where should I install my integrations? 

For self-hosted deployments in small setups you might host integrations on the same server on which Mattermost is installed. For larger deployments you can setup a separate server for integrations, or add them to the server on which the external application is hosted--for example, if you're self-hosting a Jira server you could deploy a Jira integration on the Jira server itself. 

When self-hosting restrictions are less strict, AWS, Heroku and other public cloud options could also be used. 

## How should I automate the install and upgrade of Mattermost when included in another application? 

Automating Mattermost installation within another application: 

1. Review the [Mattermost installation guides](https://docs.mattermost.com/guides/administrator.html#installing-mattermost) to understand configuration steps of the production deployment 
2. Install Mattermost files to a dedicated `/opt/mattermost` directory by decompressing the `tar.gz` file of the latest release for your target platform (for example `linux-amd64`). 
3. Review [Configuration Settings](http://docs.mattermost.com/administration/config-settings.html) in `config.json` and set your automation to customize your Mattermost deployment based on your requirements. 
4. For directory locations defined in `config.json`, such as the location of the local file storage directory (`./data/`) or logs directory (`./logs`), you can redefine those locations in your `config.json` settings and move the directories.
   - All other directories should remain as they are in `/mattermost` 
5. Test that your Mattermost server is running with your new configuration.
6. Also, from the commandline run `./bin/platform -version` to test that the commandline interface is functioning properly.

Automating Mattermost upgrade within another application: 

1. Review the [upgrade guide](http://docs.mattermost.com/administration/upgrade.html) for an overview of the upgrade procedure. 
2. Create automation to upgrade to the next Mattermost versions: 
    - backup the `config.json` file to preserve any settings a user may have made.
    - backup the `./data` directory if local storage is used for files.
    - replace the contents of `/mattermost` directory with the decompressed contents of the latest release.
    - restore `config.json` and `./data` to their previous locations (which may have been overwritten).
    - if you need to overwrite any `config.json` parameters use a [`sed` command](http://stackoverflow.com/questions/20568515/how-to-use-sed-to-replace-a-config-files-variable) or similar tool to update `config.json`
    - starting the Mattermost server to upgrade the database, `config.json` file, and `./data` as necessary. 
3. Optionally the upgrade procedure can be chained so users can upgrade across an arbitrary number of Mattermost versions rather than to just the latest release. 
