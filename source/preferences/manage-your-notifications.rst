Manage your notifications
=========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |gear| image:: ../images/settings-outline_F08BB.svg
  :alt: Use the Settings icon to customize your Mattermost user experience.

Mattermost notifies you of new activity in the following ways:

- **Badges**: In Mattermost, badges show you when you have unread messages and threads.
- **Banner alerts**: Pop-ups alert you to new activity.
- **Push notifications**: Mobile app alert you to new activity when you're on the go.
- **Sounds**: Audible sounds alert you to new activity.

You can configure Mattermost to receive increase or decrease the number of notifications based on your preferences.

Get notified
-------------

In Mattermost, select the **Settings** |gear| icon located in the top right corner of the screen to manage your notification preferences.

this section is missing mobile app-specific actions; either find a clean way to display in tabs OR break out into sections with tabs for app type
----------------------


.. tabs::
    
    .. tab:: Web/Desktop
        
        By default, you're notified of all Mattermost activity in both a web browser and the desktop app with badges, banner alerts, and sounds.

        In a supported web browser, the tab's favicon also notifies you of unread messages with an asterisk (*) and a count.
            
        **Too many notifications!**

        If that's too many notifications, you can configure Mattermost to notify you for only mentions and direct messages. Select **Desktop Notifications > Only for mentions and direct messages**. 

        Disable web and desktop notifications altogether by selecting **Desktop Notifications > Never**.

        **Too loud**

        You can change or disable the audible sound for notifications. Go to **Desktop notifications > Notification sound**, and choose a different sound or turn the sound off.

        **Incoming call sounds**

        Want to hear a sound when a Mattermost call starts? If your Mattermost admin `enables this beta feature </configure/plugins-configuration-settings.html#enable-call-ringing-beta>`__, you can choose the sound that plays when a call is started within a direct or group message you're participating in by going to **Desktop notifications > Notification sound for incoming calls**.
        
        You can disable incoming call sounds altogether if preferred.

    .. tab:: Email 
        
        By default, you're notified of all Mattermost activity by email right away when you're offline or away from Mattermost for more than 5 minutes.

        **Too many notifications!**

        Turn off email notifications altogether by selecting **Email Notifications > Never**.

        **Group email notifications in batches**

        Mattermost also supports the ability to group multiple email notifications together into a single email. If your Mattermost admin `enables this feature </configure/site-configuration-settings.html#notification-enableemailbatching>`__, you'll receive batches of notifications by email every 15 minutes, or as configured by your admin.

    .. tab:: Mobile app

        By default, you're notified of all Mattermost activity in the mobile app when you're away or offline for more than 5 minutes.

        **Too many notifications!**

        If that's too many notifications, you can configure Mattermost to notify you for only mentions and direct messages. Select **Mobile Push Notifications > Only for mentions and direct messages**.

        If you prefer to be notified only when you're offline, select **Mobile Push Notifications > Trigger push notifications when > Offline**.

        Turn off mobile notifications altogether by selecting **Mobile Push Notifications > Never**.

        **Not enough notifications**

        If you prefer to always be notified, regardless of your user status, select **Mobile Push Notifications > Trigger push notifications when > Online, away or offline**.

    .. tab:: @mentions/keywords

        By default, you’re notified when you’re @mentioned in a message or a thread by your username or first name, or when a thread you’re following has a new response. For all other messages, the channel is highlighted to indicate unread messages.

        You're also notified when someone uses channel-wide mentions including @channel, @all, and @here. 

        **Customize notification keywords**

        You can customize any additional keywords to receive notifications. For example, you can receive notifications for all messages and threads related to a specific topic, project name, or customer. Separate multiple keywords using commas.

    .. tab:: Replies

        If `Collapsed Reply Threads </collaborate/organize-conversations.html>`__ is disabled, you won't be notified in reply threads unless you're @mentioned. However, you can configure Mattermost to notify you when someone replies to a thread you started, or started or have participated in. Select **Reply notifications** to choose the option that works best for you.

        **Automatic replies**

        Mattermost also supports the ability to automatically send custom replies to direct messages. If your Mattermost admin enables this experimental feature, you can go to **Automatic Direct Message Replies** to select **Enable** this feature and compose your message.
        
        Enabling this feature also sets your status to **Out of Office** and disables all email and push notifications until you disable it. 

    .. tab:: Per channel/category

        https://docs.mattermost.com/channels/set-channel-preferences.html

        mute channel

        ignore mentions for @channel, @here, and @all

        desktop notifications

        mobile push notifications



By default, you will only be notified in threads that you are following. See the organize conversations using collapsed reply threads documentation for details. If you’d like to be notified for all new posts in a channel, you can automatically follow all new threads in a channel by configuring channel notifications. (available by selecting the channel drop-down, selecting Notification Preferences, then enabling the Auto-follow all new threads in this channel option). 


Automatically follow all new threads in this channel

By default, you don’t automatically follow new conversation threads unless you start a thread or reply to a thread, follow a thread, or are @mentioned in a thread.

You can configure Mattermost to automatically follow every thread in a channel. When enabled, you can access all threads in the Threads view, and unfollow specific threads as you prefer.



