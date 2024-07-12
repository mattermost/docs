Manage your notifications
=========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |gear| image:: ../images/settings-outline_F08BB.svg
  :alt: Use the Settings icon to customize your Mattermost user experience.
  :class: theme-icon

.. |channel-info| image:: ../images/information-outline_F02FD.svg
  :alt: Use the Channel Info icon to access additional channel management options.
  :class: theme-icon

.. |more-icon| image:: ../images/dots-horizontal_F01D8.svg
  :alt: Use the More icon to access additional message options.
  :class: theme-icon

.. |dot-badge| image:: ../images/dot-badge.png
  :alt: A dot on the badge means you have unread activity in at least one channel you're a member of.
  :width: 50px

.. |numbered-badge| image:: ../images/numbered-badge.png
  :alt: A numbered badge means you have at least 1 unread message, @mention, or one of your keywords has triggered a notification.
  :width: 50px

Mattermost notifies you of new activity in the following ways:

**Badges**: In Mattermost, badges show you when you have unread messages and threads.

 |dot-badge| You have unread activity in at least one channel you're a member of.

 |numbered-badge| You have at least one unread :ref:`direct message <collaborate/channel-types:direct messages>`, :ref:`group message <collaborate/channel-types:group messages>`, :doc:`@mention </collaborate/mention-people>`, or a keyword triggered a notification.

**Banner alerts**: Pop-ups alert you to new activity.

**Push notifications**: Mobile app alert you to new activity when you're on the go.

**Sounds**: Audible sounds alert you to new activity.

.. include:: ../_static/badges/academy-notifications.rst
  :start-after: :nosearch:

Get notified
-------------

You can configure Mattermost to receive increase or decrease the number of notifications based on your preferences.

In a web browser or the desktop app, select the **Settings** |gear| icon located in the top right corner of the screen to manage your notification preferences.

On mobile, select the **Settings** |gear| icon and tap **Notifications**.

.. tip::

  - From Mattermost v9.8, your desktop and mobile notification preferences have been combined together under **Settings > Notifications**. If you're using an older Mattermost release, you'll find these settings split out as desktop settings and mobile settings instead.
  - Missing notifications? Visit our `notifications knowledge base article <https://support.mattermost.com/hc/en-us/articles/19161390661780>`__ for additional troubleshooting tips and tricks.

.. tab:: Web/Desktop/Mobile

  By default, you're notified of all Mattermost activity in Mattermost with badges, banner alerts, and sounds, regardless of how you access Mattermost, and your current :ref:`Mattermost availability <preferences/set-your-status-availability:set your availability>`.

  When accessing Mattermost using a supported web browser, the browser tab's favicon notifies you of unread messages with an asterisk (*) and a message count. From Mattermost v9.9, you're prompted to give Mattermost permission to send you notifications in the announcement bar.

    - When you select **Enable notifications**, you won't be asked again, and you'll start receiving Mattermost notifications in the web browser. 
    - If you dismiss the prompt, you won't receive notifications in the web browser, and you'll prompted again the next time you open Mattermost in a browser.

  **Want different notifications on mobile?**

  To personalize your notification preferences for the mobile app, select **Desktop and mobile notifications**, and then select **Use different settings for my mobile devices** to define how mobile notifications are triggered, when they're triggered based on you being online, away, or offline, and whether they include replies to threads you're following.

  **Getting too many notifications?**

  If you're receiving too many notifications, you can configure Mattermost to notify you for select messages only. Select **Desktop and mobile notifications > Mentions, direct messages, and group messages** to receive notifications for mentions, direct messages, and group messages only. This option also enables you to receive notifications about replies to threads you're following by selecting **Notify me about replies to threads I'm following**.

  Disable web, desktop, and mobile notifications altogether by selecting **Desktop and mobile notifications > Nothing**.

.. tab:: Notification sounds

  By default, desktop message notifications include audible sounds. You can change or disable these sounds if preferred. Go to **Desktop notification sounds > Message notification sound** to choose a different sound, or disable this option to turn off desktop notification sounds, if preferred.

  **Want incoming call sounds?**

  Want to hear a sound when a Mattermost call starts? If your Mattermost admin :ref:`enables this Beta feature <configure/plugins-configuration-settings:enable call ringing (beta)>`, you can choose the sound that plays when a call is started within a direct or group message you're participating in by going to **Desktop notifications > Notification sound for incoming calls**.

  From Mattermost mobile app v2.19, incoming call sounds on mobile include sounds and vibration, and vibration only when your device is in silent mode. You can set one **Incoming call sound** for web or desktop, and a different one for mobile. When you select an **Incoming call sound** on mobile, your changes apply only to mobile.

.. tab:: Email 

  By default, you're notified of all Mattermost activity by email right away when you're offline or away from Mattermost for more than 5 minutes.

  **Too many notifications?**

  Turn off email notifications altogether by selecting **Email Notifications > Never**.

  **Group email notifications in batches**

  Mattermost also supports the ability to group multiple email notifications together into a single email. If your Mattermost admin :ref:`enables this feature <configure/site-configuration-settings:enable email batching>`, you'll receive batches of notifications by email every 15 minutes, or as configured by your admin.

.. tab:: @mentions & keywords

  By default, you’re notified when you’re @mentioned in a message or a thread by your username or first name, or when a thread you’re following has a new response. For all other messages, the channel is highlighted to indicate unread messages.

  You're also notified when someone uses channel-wide :doc:`mentions </collaborate/mention-people>` including @channel, @all, and @here. 

  **Customize notification keywords**

  Using a web browser or the desktop app, customize any additional non case-sensitive keywords to trigger notifications. For example, you can receive notifications for all messages and threads related to a specific topic, project name, or customer. Separate multiple keywords using commas or by pressing :kbd:`Tab`, and use :kbd:`Backspace` to manage keywords.

  .. image:: ../images/keywords-trigger-mentions.gif
    :alt: A walkthrough of setting keywords that trigger mentions in Mattermost.

  **Passively track keywords (no notification)**

  .. include:: ../_static/badges/ent-pro-only.rst
    :start-after: :nosearch:
        
  From Mattermost v9.3, Mattermost Enterprise and Professional users interested calling attention to specific topics of interest across channels, at a glance, can do so without triggering notifications.
        
  Using a web browser or the desktop app, passively track key terms by specifying single or multi-words to highlight in all channels you're a member of. Keywords and phrases are automatically highlighted based on your :doc:`Mattermost theme </preferences/customize-your-theme>`.

  .. image:: ../images/keywords-highlighted.gif
    :alt: A walkthrough of setting keywords that are highlighted in Mattermost.

.. tab:: Replies

  If :doc:`Collapsed Reply Threads </collaborate/organize-conversations>` are disabled, you won't be notified in reply threads unless you're @mentioned. However, you can configure Mattermost to notify you when someone replies to a thread you started, or started or have participated in. Select **Reply notifications** to choose the option that works best for you. This setting is hidden when Collapsed Reply Threads is enabled.

  **Automatic replies**

  Mattermost also supports the ability to automatically send custom replies to direct messages. If your Mattermost admin enables this experimental feature, you can go to **Automatic Direct Message Replies** to select **Enable** this feature and compose your message.

.. tab:: Per-channel

  You can set notification preferences at the channel level, including group messages, for every channel you're a member of. You have 2 ways to access channel preferences: 
       
  Select the channel name, then select **Notification Preferences**.

  .. image:: ../images/channel-notification-settings.gif
    :alt: Select the channel name dropdown to access channel-specific notification preferences.

  Alternatively, select the channel's **View Info** |channel-info| icon, and then select **Notification Preferences** in the right pane.

  **Mute channel**

  All channels are unmuted by default. Using Mattermost in a web browser or the desktop app, mute a channel any time by selecting **Mute Channel**. Mute a direct message or group message by selecting **Mute Conversation**. You can unmute channels the same way by selecting **Unmute Channel** and **Unmute Conversation**.

  Using the mobile app:

  1. Tap the channel or conversation you want to mute.
  2. Tap the **More** |more-icon| icon located in the top right corner of the app.
  3. Tap **Mute**.
  4. Unmute the channel or conversation by tapping **Mute** again.

  Once a channel is muted:

  - Email, desktop, incoming call ring tones, and push notifications are disabled.
  - A mute icon displays next to the channel, direct message, or group message’s name.
  - The channel is dimmed in the channel sidebar, and isn’t bolded to indicate unread messages unless you’re :doc:`@mentioned </collaborate/mention-people>` directly.

  **Ignore channel-wide @mentions**

  By default, you’ll be notified every time someone on your team mentions an entire channel using @channel, @all, or @here.

  When using Mattermost in a web browser or the desktop app, stop being notified for channel-wide @mentions, by selecting the **Ignore mentions for @channel, @here and @all** option. Mention notifications for channel-wide mentions are ignored, but the channel is marked as unread unless it's muted.

  - In the desktop app, your mobile push notification preferences use the same configuration as the desktop app by default. Clear the **Use the same notification setting as desktop** option to customize your push notification preferences. You can receive notifications for all new messages; mentions, direct messages, and keywords; or no notifications within the desktop app.

  - In the mobile app, you're notified about all new messages by default. You can customize your mobile app notification preferences. You can receive notifications for all new messages, mentions only, or no notifications.

  - Select **Reset to default** to return to global defaults.

  **Desktop notifications**

    By default, your web and desktop notification preferences apply to all channels you’re a member of. You can customize notifications on a channel by channel basis if preferred by selecting **Desktop notifications**. Select **(Default**) options to revert back to your global preferences.

  **Mobile push notifications**

    By default, your mobile push notification preferences apply to all channels you’re a member of. You can customize notifications on a channel by channel basis if preferred by selecting **Mobile push notifications**. Select **(Default**) options to revert back to your global preferences.

  **Auto-follow all new threads in this channel**

  By default, you don’t automatically follow new conversation threads unless you start a thread or reply to a thread, follow a thread, or are @mentioned in a thread.

  You can configure Mattermost to automatically follow every thread in a channel. When enabled, you can access all threads in the **Threads** view, and unfollow individual threads as you prefer.

