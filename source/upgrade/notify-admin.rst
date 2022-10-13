Notify admin
============

Some Mattermost features are limited to specific plans. Users who want to access these unavailable features can request access through their System Admin by sending a notification.

If access to a feature requires a plan upgrade, System Admins receive notifications of these requests in order to collect data before upgrading. For example, if only one end-user requests access to AD/LDAP, it probably isn't necessary to upgrade. However, if 20 users, including Team and Channel Admins request it, you may want to consider upgrading to support this need.

This feature is designed for informational purposes only, and no action is required unless you want to take action. Your Mattermost instance's functionality is not affected if you choose not to upgrade.

Notifications
-------------

Notifications are triggered by users. The very first time a user sends a request to upgrade or start a trial, a bot message is sent to all System Admins indicating the feature or functionality the user has requested that requires an upgrade or trial. This bot message is listed in the **Direct Messages** section of the channel sidebar.

Subsequent request notifications are received by System Admins at most every 14 days. When a notification is received by a System Admin, a 14-day cool-off period begins. Any requests generated in the middle of the cool-off period will be held off until 14 days later, and then provided in a summarized format.

Take action
-----------

You can take action on any of the requests sent using the options provided in the message.

Dismiss notifications
---------------------

You're not obligated to upgrade or change your plan. Once you've read the notification, it's marked as read and is filed in your list of direct messages. You can find the message at any time using the search bar. None of your existing Mattermost features and functions are affected negatively if you don't upgrade.
