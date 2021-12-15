Configuring Notifications
=========================

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

.. |gear-icon| image:: ../images/gear-icon.png
  :alt: Select the Gear icon to access your user preferences.

Notifications in Mattermost alert you to unread messages and mentions. Desktop, email, and mobile push notifications notify you of activity in Mattermost. 

You can configure your Mattermost account for how and when you want to be notified of Mattermost activity. When you join a team, Mattermost will notify you of messages directed at you, including when someone:

- Mentions you specifically with ``@username``
- Sends you a Direct Message
- Mentions your username or first name in a channel
- Notifies a channel you're in using ``@channel``, ``@all``, or ``@here``
- Responds to a thread you're following
- Uses any `keywords you've configured <https://docs.mattermost.com/messaging/managing-account-settings.html#words-that-trigger-mentions>`__ 

.. tip::

  Not getting a notification? See our `FAQ to view the notification flow chart <https://docs.mattermost.com/about/faq-notifications.html>`__ to see what other factors can influence whether a notification gets triggered.

Desktop notifications
----------------------

Desktop notifications are pop-ups that appear in the corner of your main monitor when using Chrome, Edge, Firefox, and Safari, or the `Mattermost Desktop Apps <https://mattermost.com/download/#mattermostApps>`__. You can change the default preference to trigger desktop notifications for all messages sent in channels you're a member of, or turn them off entirely. You can also choose what sound plays when a desktop notification is triggered on supported browsers and the Mattermost Desktop App.

.. image:: ../images/desktop_notification.png

.. tabs::

  .. tab:: Mattermost v6.0 onwards

    From Mattermost v6.0, **Desktop Notifications** have moved. Access **Notifications** by selecting the **Gear** |gear-icon| icon in the Global Header.
      
    Configure desktop notifications in **Settings > Notifications > Desktop Notifications**. 
    
    +---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **Notification option**   | **You'll receive...**                                                                                                                                                                                                                            |
    +===========================+==================================================================================================================================================================================================================================================+
    | **For all activity**      | Desktop notifications for all channel activity.                                                                                                                                                                                                  |
    +---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **Only for mentions**     | - Desktop notifications for @mentions and Direct Messages/Group Messages only.                                                                                                                                                                   |
    |                           | - When you've `enabled Collapsed Reply Threads <https://docs.mattermost.com/messaging/manage-channels-settings.html#collapsed-reply-threads-beta>`__, receive reply thread notifications by enabling **Notify me about threads I'm following**.  |
    |                           | - Choose your notification sound preference.                                                                                                                                                                                                     |
    +---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **Never**                 | No desktop notifications.                                                                                                                                                                                                                        |
    +---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    By default, this setting becomes your global setting applied to all channels you're a member of.

  .. tab:: Mattermost v5.39 and earlier

    In Mattermost versions up to 5.39, access **Account Settings** from the **Main Menu** by selecting the three horizontal lines (also known as a hambuger menu) at the top of the channel sidebar.
      
    - Configure desktop notifications in **Account Settings > Notifications > Desktop Notifications > Send desktop notifications**, then choose your sound preference.
    - By default, all channels use the global setting configured in **Account Settings**.
  
    Configure desktop notifications in specific channels in the channel menu via **Notification Preferences > Send desktop notifications**.

Email notifications
-------------------

By default, you'll get email notifications if you're not actively using Mattermost. You can turn off email notifications.

.. image:: ../images/email_notification.png

Open messages from email notifications in the Mattermost Desktop App, Mobile App, or in your browser.

.. image:: ../images/deep_linking.png

.. tabs::

  .. tab:: Mattermost v6.0 onwards

    From Mattermost v6.0, **Email Notifications** have moved. Access **Notifications** by selecting the **Gear** |gear-icon| icon in the global header.
      
    Configure email notifications in **Settings > Notifications > Email Notifications**.

    +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **Notification Option**   | **You'll receive...**                                                                                                                                                                                                                           |
    +===========================+=================================================================================================================================================================================================================================================+
    | **Immediately**           | - Email notifications for @mentions and direct messages/group messages when you're                                                                                                                                                              |
    |                           |   offline or away for more than five minutes.                                                                                                                                                                                                   |
    |                           | - When you've `enabled Collapsed Reply Threads <https://docs.mattermost.com/messaging/manage-channels-settings.html#collapsed-reply-threads-beta>`__, receive reply thread notifications by enabling **Notify me about threads I'm following**. |
    +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **Never**                 | No email notifications.                                                                                                                                                                                                                         |
    +---------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    This setting becomes your global setting applied to all channels you're a member of.

  .. tab:: Mattermost v5.39 and earlier

    In Mattermost versions up to 5.39: 
      
    -  Configure email notifications in **Account Settings > Notifications > Email notifications**.
    -  Configure the email address where notifications are sent in **Account Settings > General > Email**.

Mobile push notifications
-------------------------

Mobile push notifications appear on the lock screen of your mobile device if the Mattermost Android or iOS app is installed. By default, these notifications are triggered when you're not actively using Mattermost, but this is configurable. You can also change the default preference to trigger push notifications for all messages sent in channels you're a member of, or turn them off entirely.

.. image:: ../images/push_notification.png

.. tabs::

  .. tab:: Mattermost v6.0 onwards

      From Mattermost v6.0, **Mobile Push Notifications** have moved. Access **Notifications** by selecting the **Gear** |gear-icon| icon in the Global Header.
      
      Configure the activities that trigger mobile push notifications in **Settings > Notifications > Mobile Push Notifications > Send mobile push notifications**.

      +----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | **Notification option**                | **You'll receive...**                                                                                                                                                                                                                            |
      +========================================+==================================================================================================================================================================================================================================================+
      | **For all activity**                   | - Mobile notifications for all activity.                                                                                                                                                                                                         |
      +----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | **For mentions and Direct Messages**   | - Mobile notifications for @mentions and Direct Messages/Group Messages only.                                                                                                                                                                    |
      |                                        | - When you've `enabled Collapsed Reply Threads <https://docs.mattermost.com/messaging/manage-channels-settings.html#collapsed-reply-threads-beta>`__, receive reply thread notifications by enabling **Notify me about threads I'm following**.  |
      +----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | **Never**                              | No mobile notifications.                                                                                                                                                                                                                         |
      +----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

      Configure when mobile push notifications are triggered in **Settings > Notifications > Mobile Push Notifications > Trigger push notifications when**.

      +---------------------------------+-----------------------------------------------------------------------------------+
      | **Notification option**         | **You'll receive...**                                                             |
      +=================================+===================================================================================+
      | **Online, away or offline**     | Mobile notifications at all times, regardless of your current Mattermost status.  |
      +---------------------------------+-----------------------------------------------------------------------------------+
      | **Away or offline**             | Mobile notifications when you're away or offline only.                            |
      +---------------------------------+-----------------------------------------------------------------------------------+
      | **Offline**                     | No mobile notifications.                                                          |
      +---------------------------------+-----------------------------------------------------------------------------------+
      
  .. tab:: Mattermost v5.39 and earlier

      In Mattermost versions up to 5.39: 
      
      -  Configure push notifications in **Account Settings > Notifications > Mobile Push Notifications > Send mobile push notifications**.
      -  Configure when push notifications are sent depending on your availability in **Account Settings > Notifications > Mobile push notifications > Trigger push notifications when**.
  
.. tip::

  Learn more about how Mattermost detects your `availability <https://docs.mattermost.com/help/getting-started/setting-your-status-availability.html>`__ as **Online**, **Away** or **Offline**.

Browser tab notifications
-------------------------

If Mattermost is open in a browser tab, the favicon updates to notify you of unread messages (\*) and a count of mentions or Direct Messages. Browser tab notifications are available on Chrome, Edge, Firefox, and Safari.

.. image:: ../images/browser_notification.png

Muting a channel
----------------

Channels in the sidebar appear **bolded** when there are unread messages in the channel and include a badge count if you are mentioned specifically. 

When you mute a channel, you do not receive any notifications (desktop, email, or push) for any mentions (whether they are channel-wide or directed at you). However, if you are mentioned while the channel is muted, the mention badge will be displayed in the sidebar with the channel displaying at reduced opacity.

To mute a channel, select the channel name and select **Mute Channel**. To unmute it, select the channel name and select **Unmute Channel**.

.. tip:: 

  Mentions are triggered by `selected keywords <https://docs.mattermost.com/help/settings/account-settings.html#words-that-trigger-mentions>`__. Learn more about `mentioning teammates <https://docs.mattermost.com/help/messaging/mentioning-teammates.html>`__.

Ignoring mentions
-----------------

To turn off notifications for channel-wide mentions for @channel, @here, and @all, navigate to:

**Notification Preferences > Ignore mentions for @channel, @here and @all**. Choose **Edit**, select **On**, and then select **Save**. 

When this setting is on you will still receive notifications for direct mentions. 

.. note::
  
If you've muted a channel and enabled **Ignore mentions for @channel, @here and @all**, then you won't receive notifications (whether they're direct or channel-wide). However, if you're directly mentioned in the muted channel, a badge counter is displayed in the sidebar.
