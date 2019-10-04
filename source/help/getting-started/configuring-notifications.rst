Configuring Notifications
=========================

Desktop, email and mobile push notifications notify you of activity in Mattermost. When you join a team, Mattermost will notify you of messages directed at you, including when someone:

- Direct Messages you
- Mentions your username or first name in a channel
- Notifies a channel you're in using @channel or @all
- Uses any `keywords you've configured<https://docs.mattermost.com/help/settings/account-settings.html#words-that-trigger-mentions>`_ 

Desktop Notifications
-------------------------------------

Desktop notifications are pop-ups that appear in the corner of your main monitor when using Chrome, Firefox, Edge, Safari or the `Mattermost Desktop app <https://mattermost.com/download/#mattermostApps>`_. You can change the default preference to trigger desktop notifications for all messages sent in channels you're a member of, or turn them off entirely.

.. image:: ../../images/desktop_notification.png
  :width: 239px
  :height: 232px

-  Configure desktop notifications in **Account
   Settings** > **Notifications** > **Desktop Notifications** > **Send
   Desktop Notifications**.
-  Configure desktop notifications in specific channels in **Channel
   Menu** > **Notification Preferences** > **Send Desktop
   Notifications**. 
  - By default, all channels use the global setting configured in *Account Settings*.
   
**Not getting a desktop notification?** See our `FAQ to view the desktop notification flow chart <https://docs.mattermost.com/overview/faq.html?#what-determines-if-a-desktop-notification-should-be-triggered>`_ and see what other factors influence if a notification should be triggered.

.. tip :: Configure desktop notification sounds in **Account Settings** >
   **Notifications** > **Desktop Notifications** > **Desktop Notification Sounds**.

Email Notifications
-------------------------------------

By default, you'll get email notifications if you're not actively using Mattermost. You can change the default preference for email notifications to turn them off entirely.

.. image:: ../../images/email_notification.png
  :width: 239px
  :height: 232px


-  Configure email notifications in **Account Settings** >
   **Notifications** > **Email Notifications**.
-  Configure the email address where notifications are sent in **Account
   Settings** > **General** > **Email**.

**Not getting an email notification?** See our `FAQ to view the email notification flow chart <https://docs.mattermost.com/overview/faq.html?#what-determines-if-an-email-notification-should-be-triggered>`_ and see what other factors influence if a notification should be triggered.

Mobile Push Notifications
--------------------------------------------

Mobile push notifications appear on the lock screen of your mobile device if the Mattermost Android or iOS app is installed. By default, these notifications are triggered when you're not actively using Mattermost, but this is configurable. You can also change the default preference to trigger push notifications for all messages sent in channels you're a member of, or turn them off entirely.

.. image:: ../../images/push_notification.png
  :width: 239px
  :height: 232px

-  Configure push notifications in **Account Settings**
   > **Notifications** > **Mobile Push Notifications** > **Send mobile
   push notifications**.
-  Configure when push notifications are sent depending on your status
   in **Account Settings** > **Notifications** > **Mobile Push
   Notifications** > **Trigger push notifications when**.
   
**Not getting a push notification?** See our `FAQ to view the email notification flow chart <https://docs.mattermost.com/overview/faq.html?#what-determines-if-a-mobile-push-notification-should-be-triggered>`_ and see what other factors influence if a notification should be triggered.   

.. tip :: Your status switches from "online" to "away" when no activity is detected in Mattermost for five or more minutes. Your status switches to offline if you log out or close the mobile or desktop clients.

Browser Tab Notifications
----------------------------------------

If Mattermost is open in a browser tab, the favicon updates to notify you of unread messages (\*) and
a count of mentions or Direct Messages. Browser tab notifications are available on Firefox and Chrome.

.. image:: ../../images/browser_notification.png
  :width: 239px
  :height: 232px


Muting a Channel
----------------------------------------

Channels in the sidebar are **bold** when there are unread messages in the channel and show a badge count if you are mentioned specifically. To mute a channel so it does not appear unread and you do not recieve notifications, click the channel name at the top of the page to access the **Channel Menu** > **Notification Preferences > Mute channel**.

.. tip :: Mentions are triggered by `selected keywords <https://docs.mattermost.com/help/settings/account-settings.html#words-that-trigger-mentions>`_, learn more about `mentioning teammates <http://docs.mattermost.com/help/messaging/mentioning-teammates.html>`__.
