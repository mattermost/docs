Configuring Notifications
=========================

Notifications in Mattermost alert you to unread messages and mentions.

Unreads and Mentions
----------------------------------------

Unread Messages Indicator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The name of a channel in the left-hand sidebar is **bold** when
there are unread messages in the channel. Clicking on the channel
removes the bold indicator, and brings you to the most recent unread
message in the channel.

You can choose not to show unread indicators in a channel by clicking
**Channel Menu** > **Notification Preferences** > **Mark Channel
Unread** and selecting **Only for mentions**. This will only notify you if your name is mentioned or a
keyword for which you're listening is entered.

Mentions Indicator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mentions are triggered by `selected
keywords <https://docs.mattermost.com/help/settings/account-settings.html#words-that-trigger-mentions>`__
in a channel. Unread mentions are indicated by bold text and a mention counter next to
the channel name in the left-hand sidebar.

Clicking the channel name removes the bolding and mention count. You can
review your recent mentions by clicking **@** next to the search box
at the top of the screen.

Learn more about `mentioning
teammates <http://docs.mattermost.com/help/messaging/mentioning-teammates.html>`__.

Muting a Channel
~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, channel muting is turned off for all channels. 
To mute or unmute a channel, click the channel
name at the top of the page to access the channel menu, then click
**Notification Preferences > Mute channel**.

Once this is completed, you will no longer receive unread notifications from the specified channel.

Email Notifications
-------------------------------------

If you have Mattermost closed or have not had any browser activity for a short time, an email will be sent to your inbox for any mentions you received while you were away.

-  Turn email notifications On or Off in **Account Settings** >
   **Notifications** > **Email Notifications**.
-  Configure the email address where notifications are sent in **Account
   Settings** > **General** > **Email**.

Desktop Notifications
-------------------------------------

Desktop notifications are browser notifications that appear in the corner of your main monitor for activity in channels you are not actively viewing. By default, these notifications are sent for any mentions or `selected
keywords <https://docs.mattermost.com/help/settings/account-settings.html#words-that-trigger-mentions>`__. Desktop notifications are available on Edge, Firefox, Safari, Chrome and `Mattermost Desktop Apps <https://about.mattermost.com/download/#mattermostApps>`__.

-  Configure when desktop notifications are sent in **Account
   Settings** > **Notifications** > **Desktop Notifications** > **Send
   Desktop Notifications**.
-  Configure channel-specific desktop notifications in **Channel
   Menu** > **Notification Preferences** > **Send Desktop
   Notifications**. By default, all channels use the global setting
   configured in *Account Settings*.
   
When `Desktop App <https://about.mattermost.com/download/#mattermostApps>`__ notifications are set to "Only for mentions and direct messages," an empty red circle is displayed over the upper right corner of the Mattermost dock icon when any message without an at-mention is received. A solid red circle with a post count is displayed when a message with an at-mention is received.
   
Notification Sounds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A notification sound plays for all activity that would cause a desktop
notification. Notification sounds are available on IE11, Edge, Safari, Chrome and
`Mattermost Desktop Apps <https://about.mattermost.com/download/#mattermostApps>`__.

-  Turn notification sounds On or Off in **Account Settings** >
   **Notifications** > **Desktop Notification Sounds**.
-  Configure desktop notification triggers and sounds in
   **Account Settings** > **Notifications** > **Desktop Notifications**.
-  Configure channel specific desktop notifications in **Channel
   Menu** > **Notification Preferences** > **Send Desktop
   Notifications**. By default, all channels use the global setting
   configured in *Account Settings*.

Mobile Push Notifications
--------------------------------------------

If the Mattermost Android or iOS app is installed, push notifications
can be sent to your mobile device. By default, these notifications are
sent when you are away or offline and are mentioned in any channel that is not being viewed on desktop.

.. tip :: Your status switches from "online" to "away" when no activity is detected in Mattermost for five or more minutes. Clicking or typing anywhere in Mattermost changes your status to online.

   Moreover, your status switches to offline if you log out, or close your mobile and desktop clients.

-  Configure when push notifications are sent in **Account Settings**
   > **Notifications** > **Mobile Push Notifications** > **Send mobile
   push notifications**.
-  Configure when push notifications are sent depending on your status
   in **Account Settings** > **Notifications** > **Mobile Push
   Notifications** > **Trigger push notifications when**.

Team Sidebar Notifications
----------------------------------------

If you belong to more than one team, a team sidebar appears to the left of your channel list. It will inform you of unread messages and mentions across teams.

- Unread messages are denoted by a small dot to the left of the team icon.
- Unread mentions are displayed with a mention counter that appears on the top right corner of the team icon.

.. image:: ../../images/team-sidebar-notifications.png

Browser Tab Notifications
----------------------------------------

If Mattermost is open in a browser tab, the favicon updates to inform you of unread messages and
mentions. Browser tab notifications are available on Firefox and Chrome.

- Unread messages are denoted by an asterisk (\*) next to the Mattermost icon.
- Unread mentions are counted in brackets and incorporate mentions and direct messages from all of your teams.
