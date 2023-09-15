Customize your Mattermost experience
==================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

You can customize your Mattermost experience in the following ways in **Settings**:

- `Notifications <#notifications>`__
- `Display <#display>`__
- `Sidebar <#sidebar>`__
- `Advanced <#advanced>`__

.. tip::
  
  How you access settings depends on the version of Mattermost you’re using. See the `what’s changed in Mattermost v6.0 </welcome/what-changed-in-v60.html#account-settings>`__ documentation for details.

Notifications
-------------

Settings to configure desktop notifications and sounds, email notifications, mobile push notifications, words that trigger mentions, and automatic direct message replies.

Desktop notifications
~~~~~~~~~~~~~~~~~~~~~

Desktop notifications appear in the top corner of your main monitor when there is activity in Mattermost.

Send desktop notifications
^^^^^^^^^^^^^^^^^^^^^^^^^^

Choose what activity triggers a desktop notification. This setting applies globally, but this preference is customizable for each channel from the channel name drop-down menu. Desktop notifications are available on Chrome, Edge, Firefox, and Safari.

When `desktop app <https://mattermost.com/apps>`__ notifications are set to **Only for mentions and direct messages**, notifications trigger as follows:

- An empty red circle is displayed over the upper right corner of the Mattermost dock icon when any message without an at-mention is received. 
- A solid red circle with a post count is displayed when a message with an at-mention is received.
- And when `Collapsed Reply Threads </channels/organize-conversations.html>`__ is enabled, you can choose to receive desktop notifications about `threads you're following </channels/organize-conversations.html#start-or-reply-to-threads>`__.

Notification sound
^^^^^^^^^^^^^^^^^^

When desktop app notifications are set to **For all activity** or **Only for mentions and direct messages**, you can configure Mattermost to notify you using a sound. Chooose from one of 6 preset notification sounds. Notification sounds are available on Chrome, Edge, Firefox, and Safari in addition to the Mattermost Desktop App.

Notification sound for incoming calls (Beta)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

From Mattermost v8.0 and Calls v0.17.0, when desktop app notifications are set to **For all activity** or **Only for mentions and direct messages**, you can configure Mattermost to alert you to incoming calls through direct or group messages with a specific ring tone and a desktop notification, unless the system admin has `disabled your ability to do so </configure/plugins-configuration-settings.html#enable-call-ringing-beta>`__.

When incoming call notification sounds are enabled, choose the ring tone to play, then select **Save**.

Email notifications
~~~~~~~~~~~~~~~~~~~

Email notifications are sent for mentions and direct messages after you’ve been offline for more than 60 seconds or away from Mattermost for more than five minutes. Using Mattermost in a web browser or the desktop app, you can change the email address where notifications are sent by selecting **Profile > Profile Settings > Email**.

If your System Admin has enabled `email batching </configure/configuration-settings.html#enable-email-batching>`__, you'll have additional options under this settings to select how often email notifications will be sent. All notifications received over this time period are combined and sent in a single email.

.. note::

  In Mattermost mobile, access **Settings** by tapping on your profile picture.

  1. Tap **Notifications**.
  2. Tap **Email Notifications**.

Mobile push notifications
~~~~~~~~~~~~~~~~~~~~~~~~~

Push notifications can be sent to your mobile device if you have the Android or iOS app installed. You can choose the type of activity that will send a notification.

By default, push notifications are sent **For mentions and direct messages**. If push notifications are sent **Never**, the Mattermost setting to trigger push notifications depending on your `Mattermost availability </welcome/set-your-status-availability.html>`__ is hidden. If your System Admin hasn't set up push notifications, this setting will be disabled.

.. note::

  In Mattermost mobile, access **Settings** by tapping on your profile picture.

  1. Tap **Notifications**.
  2. Tap **Push Notifications**.

If you're actively viewing a channel (public or private), direct message, or group message using the Desktop App or a browser, no push notifications will be sent for that channel. If a notification is viewed using the Desktop App or a browser, the lockscreen notification will clear on Android, and on iOS the badge on the Mattermost app icon will count down accordingly.

Browser tab notifications
~~~~~~~~~~~~~~~~~~~~~~~~~

If Mattermost is open in a browser tab, the favicon updates to notify you of unread messages (\*) and a count of mentions or direct messages. Browser tab notifications are available on Chrome, Edge, Firefox, and Safari.

.. image:: ../images/browser_notification.png

Trigger mobile push notifications when
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also choose when to send push notifications depending on your Mattermost availability. By default, push notifications are sent if your availability is **Away** or **Offline**. If **Send Mobile Push Notifications** is set as **Never**, this setting is hidden. If your System Admin has not set up push notifications, this setting will be disabled.

Words that trigger mentions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, you receive notifications when someone posts a message that contains your non-case sensitive username or @username. You also receive notifications when someone uses the @channel, @all, and @here mentions. You can customize the words that trigger mentions by typing them into the input box. This is useful if you want to be notified of all posts on a certain topic, for example, "marketing".

.. note::

  In Mattermost mobile, access **Settings** by tapping on your profile picture.

  1. Tap **Notifications**.
  2. Tap **Mentions**.

Reply notifications
~~~~~~~~~~~~~~~~~~~

When `Collapsed Reply Threads </channels/organize-conversations.html>`__ is disabled, you can choose to receive mention notifications when someone replies to a thread you have started or have participated in.

- You're considered to start a thread when you post a message to which other members of your team reply.
- You're considered to be a participant in a thread when you post a message using the `reply button </channels/reply-to-messages.html>`__ in an pre-existing thread.

.. note::
  This setting is hidden when Collapsed Reply Threads is enabled.

Automatic direct message replies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set an automated custom message that will be sent once per day in response to direct messages. Mentions in public and private channels won't trigger the automated reply. Enabling Automatic Replies sets your availability to **Out of Office** and disables desktop, email, and push notifications. This setting is experimental and `must be enabled by your System Admin </configure/configuration-settings.html#enable-automatic-replies>`__.

.. note::

  In Mattermost mobile, access **Settings** by tapping on your profile picture.

  1. Tap **Notifications**.
  2. Tap **Automatic replies**.




