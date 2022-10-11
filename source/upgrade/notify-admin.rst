Notify admin
============

In some cases there are Mattermost features that are limited to specific plans. When using Mattermost, users who come across these unavailable features can send a notification to System Admins indicating that they'd like access to this feature.

If access to a feature requires a plan upgrade, System Admins receive notifications of these requests in order to collect data before upgrading. For example, if only one end-user requests access to AD/LDAP, it probably isn't necessary to upgrade. However, if 20 users, including Team and Channel Admins request it, you may want to consider upgrading to support this need.

This feature is designed for informational purposes only, and no action is required unless you want to take action. Your Mattermost instance's functionality is not affected if you choose not to upgrade.

Notifications
-------------

Notifications are triggered by users. The very first user trigger results in a bot message to all System Admins, indicating the feature or functionality the user has requested. This bot message is listed in the direct message section of the channel sidebar.

Any requests that happen after this first request are sent 14 days later, in a summary format.

Take action
-----------

You can take action on any of the requests sent using the options provided in the message.

Dismiss notifications
---------------------

You're not obligated to upgrade or change your plan. Once you've read the notification, it's marked as read and is filed in your list of direct messages. You can find the message at any time using the search bar. None of your existing Mattermost features and functions are affected negatively if you don't upgrade.
