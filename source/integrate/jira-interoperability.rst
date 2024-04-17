Connect Jira to Mattermost
===============================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Minimize distractions, reduce context switching between your project management tool and your communication platform integrating Jira with Mattermost. Create Jira issues directly from Mattermost conversations, attach messages to Jira issues, transition and assign Jira issues, and follow up on action items in real-time, directly from Mattermost channel subscriptions.

.. note::

  - You can control which events trigger notifications including issue creation, field-specific issue updates, reopened, resolved, or deleted issues, as well as new, updated, or deleted issue comments.
  - Jira Core and Jira Software products, for Server, Data Center, and Cloud platforms are supported, and tested with versions 7 and 8.
  - From Jira v3.0, support for multiple Jira instances is supported with Mattermost Professional and Enterprise plans, configured using Administrator Slash Commands.


Setup
------

Setup starts in Mattermost, moves to Jira, and finishes in Mattermost.

Configure Mattermost
~~~~~~~~~~~~~~~~~~~~

A Mattermost system admin must perform the following steps in Mattermost.

1. Go to **System Console > Plugins > Jira** to enable Jira interoperability.
2. Generate a **Webhook Secret** by selecting **Regenerate**.
3. Configure Jira interoperabiilty preferences, then select **Save**.

  - Enable or disable the user's ability to attach and create Jira issues in Mattermost. When enabled, you must also `install this Jira integration in your Jira instance <#install-integration-as-Jira-app>`__.
  - Specify the Mattermost roles that can edit Jira subscriptions to control which Mattermost users can subscribe channels to Jira tickets.
  - (Older Jira v2.4 or earlier deployments only) Specify the Jira groups allowed to edit Jira subscriptions as a comma-separated list of user group names. Leave blank to allow any Jira user the ability to create subscriptions. The user editing a subscription only needs to be a member of one of the listed groups.
  - Enable or disable default subscription security level. When enabled, subscriptions only include issues that have a security level assigned when a security level has been included as a filter.
  - Define any additional help text to display when users run the ``/jira help`` slash command.
  - Show or hide issue descriptions and comments from subscription and webhook messages.
  - Enable or disble slash command autocompletion to guide users through available ``/jira`` slash commands.
  - Show or hide subscription name in notification messages posted to a channel.

Install Jira integration in your Jira instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To enable your users to create and manage Jira issues across Mattermost channels, you must install this Jira integration, as an application, in your Jira instance. 

- For Jira Server or Data Center instances, run the ``/jira instance install server <YOUR-JIRA-URL>`` slash command in a Mattermost channel as a Mattermost system admin, then follow the steps posted to the channel, replacing ``YOUR-JIRA-URL`` with your Jira URL. This value must match the Jira server URL you use to log in. Run the ``/jira instance uninstall server <YOUR-JIRA-URL>`` slash command to disconnect Mattermost from your Jira Server or Data Center instance.
- For Jira Cloud, run the  ``/jira instance install cloud <YOUR-JIRA-URL>`` slash command. Run the ``/jira instance uninstall cloud <YOUR-JIRA-URL>`` slash command to disconnect Mattermost from your Jira Cloud instance.

Configure webhooks in Jira
~~~~~~~~~~~~~~~~~~~~~~~~~~

A Mattermost system admin and a Jira system admin must perform the following steps to configure a single webhook for all possible event triggers, called a firehose, that you would like to be pushed into Mattermost. Mattermost gets sent a stream of events from the Jira server via a configured webhook. A channel subscription processes the firehose of data and then routes the events to channels based on your subscriptions.

1. In Mattermost, run the  ``/jira webhook <YOUR-JIRA-URL>`` slash command in a Mattermost channel to get the appropriate webhook URL, replacing ``YOUR-JIRA-URL`` with your Jira URL.
2. In Jira, go to **Jira Settings > System > WebHooks**. (For older versions of Jira, select the gear icon in bottom left corner, then go to **Advanced > WebHooks**.)
3. Select **Create a WebHook**.
4. Enter a **Name** for the webhook and add the Jira webhook URL you retrieved above in Mattermost as the URL.
5. Specify the issue events that will be sent to Mattermost channels by selecting all of the following: 

  - Comments: created, updated, and deleted.
  - Issues: created, updated, and deleted.

6. Select **Save**.

Legacy Jira webhooks
^^^^^^^^^^^^^^^^^^^^

If your organization's infrastructure is set up in such a way that your Mattermost instance can't connect to your Jira instance, you won't be able to subscribe Mattermost channels. You'll need to use legacy webhooks instead.

1. To generate the webhook URL for a specific channel, run the  ``/jira webhook`` slash command, and use the URL output in the **Legacy Webhooks** section of the output.

2. As a Jira system admin, go to **Jira Settings > System > WebHooks**. (For older versions of Jira, select the gear icon in bottom left corner, then go to **Advanced > WebHooks**.)

3. Select **Create a WebHook** to create a new webhook. Enter a **Name** for the webhook, and add the Jira webhook URL ``https://MATTERMOST-SITE-URL/plugins/jira/webhook?secret=MATTERMOST-WEBHOOK-SECRET&team=MATTERMOST-TEAM-URL&channel=MATTERMOST-CHANNEL-URL`` (for Jira 2.1) as the URL.

- Replace ``MATTERMOST-TEAM-URL`` and ``MATTERMOST-CHANNEL-URL`` with the Mattermost team URL and channel URL you want the Jira events to post to using lowercase characters.
- Replace ``MATTERMOST-SITE-URL`` with the site URL of your Mattermost instance.
- Replace ``MATTERMOST-WEBHOOK-SECRET`` with the secret generated in Mattermost by going to **System Console > Plugins > Jira**.

For example, if the team URL is ``contributors``, channel URL is ``town-square``, site URL is ``https://community.mattermost.com``, and the generated webhook secret is ``MYSECRET``, the final webhook URL would be: ``https://community.mattermost.com/plugins/jira/webhook?secret=MYSECRET&team=contributors&channel=town-square``.

4. (Optional) Set a description and a custom JQL query to determine which tickets trigger events. For information on JQL queries, see the `Atlassian help documentation <https://confluence.atlassian.com/jirasoftwarecloud/advanced-searching-764478330.html>`__.

5. Set which issue events send messages to Mattermost channels, then select **Save**. The following issue events are supported: issues created, issues deleted, and issues updated (including reopened or resolved when the assignee changes).

By default, the legacy webhook integration publishes notifications for issue created, resolve, unresolve, reopen, and assign events. To post more events, use the following extra &-separated parameters:

- ``updated_all=1``: all events
- ``updated_comments=1``: all comment events
- ``updated_description=1``: updated issue description
- ``updated_labels=1``: updated issue labels
- ``updated_prioity=1``: updated issue priority
- ``updated_rank=1``: ranked issue higher or lower
- ``updated_sprint=1``: assigned issue to a different sprint
- ``updated_status=1``: transitioned issed to a different status, such as Done or In Progress
- ``updated_summary=1``: renamed issue

Here's an example of a webhook configured to create a post for comment events: ``https://community.mattermost.com/plugins/jira/webhook?secret=MYSECRET&team=contributors&channel=town-square&updated_comments=1``

.. tip::
  
  Any previously configured webhooks set up in Jira that point to specific channels are supported and will continue to work.

Manage channel subscriptions in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As a Mattermost system admin, create or manage a channel subscription by running the ``/jira subscribe`` slash command. You can configure the following options with this command:

- Configure what Jira notifications are sent to the current channel.
- Specify filters including: affects versions, epic link, fix versions, labels, and priority.
- Specify custom fields including: checkboxes, labels, radio buttons, and select list (single or multiple choice). 
- Review the approximate JQL output generated. This is not guaranteed to be valid JQL and is only shown as a reference to what the query may look like if converted to JQL.

Run the ``/jira subscribe list`` slash command to display all subscription rules set up across all channels and teams on your Mattermost instance.

Do more with Jira
~~~~~~~~~~~~~~~~~

Do more with Jira interoperabiilty as a Mattermost system admin by using the following slash commands:

- ``/jira instance alias [URL] [ALIAS-NAME]`` - Assign an alias to an instance.
- ``/jira instance unalias [ALIAS-NAME]`` - Remove an alias from an instance.
- ``/jira instance list`` - List all installed Jira instances.
- ``/jira instance v2 <YOUR-JIRA-URL>`` - Set the Jira instance to process legacy "v2" webhooks and subscriptions (which aren't prefixed with the instance ID).
- ``/jira stats`` - Display usage statistics.
- ``/jira webhook [--instance=<YOUR-JIRA-URL>]`` - Display the Mattermost webhook that receive JQL queries.
- ``/jira v2revert`` - Revert to the legacy V2 jira plugin data model.

Manage notifications
~~~~~~~~~~~~~~~~~~~~

Jira notifications are messages sent to a Mattermost channel when a particular event occurs in Jira. They can managed as `channel subscriptions <#manage-channel-subscriptions>`__ in Mattermost, or managed as `webhooks <#configure-webhooks-in-Jira>`__ in Jira. 

.. note::
  
  The notifications and metadata shown in a channel are not protected by Jira permissions. Anyone in the channel can see what's posted to the channel. However, if they don't have the appropriate permission, they won't be able to see further details of the issue if they try to access it in Jira.

Enable
------

Notify your teams that they can connect their Jira accounts to Mattermost.

Upgrade
~~~~~~~

We recommend updating this integration as new versions are released. Generally, updates are seamless and don't interrupt the user experience in Mattermost.
Visit the `Releases page <https://github.com/mattermost/mattermost-plugin-jira/releases>`__ for the latest release, available releases, and compatibiilty considerations.

Usage
-----


To get started with the Jira/Mattermost connector is easy. You'll first need to connect your Jira account with your Mattermost account so the system can perform actions such as searching, viewing and creating Jira issues on your behalf. 
    You must be signed into Mattermost on the same browser you are using to sign into Jira during connect. end-user to authenticate with Jira and allow access to their Jira account. All create, view, assign, and transition operations are done using the logged-in user's Jira access token.

    Go into any channel within Mattermost, and type /jira connect.
    Follow the link that gets presented to you - it will bring you to your Jira server.
    Select Allow.

/jira disconnect commands to manage the connection between your Mattermost account and Jira account.

slash commands available

The available commands are listed below.

    /jira help - Launch the Jira plugin command line help syntax
    /jira info - Display information about the current user and the Jira plugin
    /jira connect [jiraURL] - Connect your Mattermost account to your Jira account
    /jira disconnect [jiraURL] - Disconnect your Mattermost account from your Jira account
    /jira issue assign [issue-key] [assignee] - Change the assignee of a Jira issue
    /jira issue create [text] - Create a new Issue with 'text' inserted into the description field
    /jira issue transition [issue-key] [state] - Change the state of a Jira issue
    /jira issue unassign [issue-key] - Unassign the Jira issue
    /jira issue view [issue-key] - View the details of a specific Jira issue
    /jira instance settings - View your user settings
    /jira instance settings [setting] [value] - Update your user settings

Note: For the /jira instance settings command, [setting] can be notifications and [value] can be on or off


Create a Jira issue

Use the /jira issue create command to create a Jira issue within Mattermost. A form will show that will allow you to fill out the issue. You can prepopulate the issue's summary using the command:

/jira issue create This is my issue's summary
Transition Jira issues

Transition issues without the need to switch to your Jira project. To transition an issue, use the /jira transition <issue-key> <state> command.

For instance, /jira transition EXT-20 done transitions the issue key EXT-20 to Done.

Note:

    States and issue transitions are based on your Jira project workflow configuration. If an invalid state is entered, an ephemeral message is returned mentioning that the state couldn't be found.
    Partial matches work. For example, typing /jira transition EXT-20 in will transition to In Progress. However, if there are states of In Review, In Progress, the plugin bot will ask you to be more specific and display the partial matches.

Assign Jira issues

Assign issues to other Jira users without the need to switch to your Jira project. To assign an issue, use the /jira assign command. For instance, /jira assign EXT-20 john transitions the issue key EXT-20 to John.

Note: Partial Matches work with Usernames and Firstname/Lastname.




Frequenly asked questions
--------------------------

Can I restrict users from creating or attaching Mattermost messages to Jira issues?

Yes, there is a plugin setting to disable that functionality.
How does Mattermost know which issues a user can see?

Mattermost only displays static messages in the channel and does not enforce Jira permissions on viewers in a channel.

Any messages in a channel can be seen by all users of that channel. Subscriptions to Jira issues should be made carefully to avoid unwittingly exposing sensitive Jira issues in a public channel for example. Exposure is limited to the information posted to the channel. To transition an issue, or re-assign it the user needs to have the appropriate permissions in Jira.
Why does each user need to authenticate with Jira?
The authentication with Jira lets the JiraBot provide personal notifications for each Mattermost/Jira user whenever they are mentioned on an issue, comment on an issue, or have an issue assigned to them. Additionally, the plugin uses their authentication information to perform actions on their behalf. Tasks such as searching, viewing, creating, assigning, and transitioning issues all abide by the permissions granted to the user within Jira.

If you experience problems with Jira-related user interactions in Mattermost such as creating issues, disable these features by setting Allow users to connect their Mattermost accounts to Jira to false in System Console > Plugins > Jira. This setting does not affect Jira webhook notifications. Then re-enable this plugin in System Console > Plugins > Plugin Management to reset the plugin state for all users.

Sometimes the plugin may crash unexpectedly and you may notice a response in red text below the chat window displaying slash command with trigger of  '/(name)' not found,. If you check your log file, look for messages that refer to plugins and health check fail, ExecuteCommand etc.

If you encounter these types of issues you can set LogSettings.FileLevel to DEBUG in your config.json settings. This will enable debug logging and give more verbose error events in the system log. Then try re-enabling the plugin in the system-console. These log results may be requested by others in the forum or by our support team.

Note: If you have a site with high volumes of activity, this setting can cause Log files to expand substantially and may adversely impact the server performance. Keep an eye on your server logs, or only enable it in development environments.


FAQ: users may notice that when you type / a menu pops up - these are called slash commands and bring the functionality of Jira (and other integrations) to your fingertips.


FAQ? If connecting to a Jira cloud instance, you will need to temporarily enable third-party cookies in your browser during the Jira authentication process. If you are using Google Chrome, this can be done by going to the browser's cookie settings and selecting "Allow all cookies". You can paste chrome://settings/cookies into your address bar to access these settings. After your Jira account is connected, feel free to disable the third-party cookies setting in your browser.


FAQ: A user must meet the criteria of both the Mattermost user settings and Jira group settings in order to edit subscriptions.

If you can subscribe channels to Jira events, you can also set up rules that define when a particular event with certain criteria are met in Jira that trigger a notification is sent to a particular channel. These subscription rules can specify the Jira Project, Event Type, Issue Type, and can filter out issues with certain values. When a user is setting up a notification subscription they'll only see the projects and issue types they have access to within Jira. If they can't see a project in Jira it won't be displayed as an option for that particular user when they are trying to set up a subscription in Mattermost.

FAQ: An approximate JQL query is output as well. This is not guaranteed to be valid JQL and is only shown as a reference to what the query may look like if converted to JQL.
When any webhook event is received from Jira, and it matches a notification rule, it posts a notification to the channel. If there are no subscription matches, the webhook event is discarded.