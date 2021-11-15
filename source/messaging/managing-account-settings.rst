Account Settings
================

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

Account Settings is where you can configure your profile settings, notification preferences, integrations, theme settings, and display options.

.. tabs::

  .. tab:: Mattermost v6.0 onwards

      In Mattermost v6.0, **Account Settings** have moved.

      - Access **Profile** and **Security** settings from your avatar in the Global Header.
      - Access **Notifications**, **Display**, **Sidebar**, and **Advanced Settings** by selecting the **Gear** icon in the Global Header.

  .. tab:: Mattermost v5.39 and earlier

      In Mattermost versions up to 5.39, access **Account Settings** from the **Main Menu** by selecting the three horizontal lines (also known as a hambuger menu) at the top of the channel sidebar.
  
Profile
-------

Settings to configure name, username, nickname, email, and profile picture.

.. tabs::

  .. tab:: Mattermost v6.0 onwards

      In Mattermost v6.0, **Account Settings** have moved.

      - Access **Profile** and **Security** settings from your avatar in the Global Header.
      - Access **Notifications**, **Display**, **Sidebar**, and **Advanced Settings** by selecting the **Gear** icon in the Global Header.
      
  .. tab:: Mattermost v5.39 and earlier

      In Mattermost versions up to 5.39, access **Account Settings** from the **Main Menu** by selecting the three horizontal lines (also known as a hambuger menu) at the top of the channel sidebar.

Full Name
~~~~~~~~~

Full names appear in the Direct Messages member list and team management modal. By default, you will receive mention notifications when someone types your first name. Entering a full name is optional. 

Username
~~~~~~~~

Usernames are unique identifiers appearing next to all posts. Pick something easy for teammates to recognize and recall. By default, you will receive mention notifications when someone types your username. In order to maintain message integrity, changing your username does not update @mentions in messages already posted. Username must begin with a letter, and contain between 3 to 22 lowercase characters made up of numbers, letters, and the symbols '.', '-', and '_'. 

Nickname
~~~~~~~~

Nicknames appear in the Direct Messages member list and team management modal. You will not receive mention notifications when someone types your nickname unless you add it to the *Words That Trigger Mentions* notifications list in **Notifications**.

Position
~~~~~~~~~

Position can be used to describe your role or job title. It appears in the profile popup that shows up when you select a user's name in the center channel or right-hand sidebar.

Email
~~~~~

Email is used for signing in, notifications, and password reset. Email requires verification if changed. If you are signing in using a single sign-on service, the email field is not editable and you will receive email notifications to the email you used to sign up to your SSO service.

Profile Picture
~~~~~~~~~~~~~~~

Profile pictures appear next to all posts and at the top of the channel sidebar next to your name. 

.. tabs::

  .. tab:: Mattermost v6.0 onwards

      In Mattermost v6.0, **Account Settings** have moved.

      - Access **Profile** and **Security** settings from your avatar in the Global Header.
      - Access **Notifications**, **Display**, **Sidebar**, and **Advanced Settings** by selecting the **Gear** icon in the Global Header.
      
  .. tab:: Mattermost v5.39 and earlier

      In Mattermost versions up to 5.39, access **Account Settings** from the **Main Menu** by selecting the three horizontal lines (also known as a hambuger menu) at the top of the channel sidebar.

To change your profile picture, choose **Select**, then choose an image. For best results, choose an image that's at least 128 x 128 pixels in size. Supported image formats include: BMP, JPG, JPEG, and PNG. The GIF file format is not supported.

Security
--------

Settings to configure your password, view access history, and view or logout of active sessions.

.. tabs::

  .. tab:: Mattermost v6.0 onwards

      In Mattermost v6.0, **Account Settings** have moved.

      - Access **Profile** and **Security** settings from your avatar in the Global Header.
      - Access **Notifications**, **Display**, **Sidebar**, and **Advanced Settings** by selecting the **Gear** icon in the Global Header.

  .. tab:: Mattermost v5.39 and earlier

      In Mattermost versions up to 5.39, access **Account Settings** from the **Main Menu** by selecting the three horizontal lines (also known as a hambuger menu) at the top of the channel sidebar.

Password
~~~~~~~~

You may change your password if you’ve logged in by email. If you are signing in using a single sign-on service, the password field is not editable, and you must access your SSO service’s account settings to update your password.

Multi-factor Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When this option is available, you can require a phone-based passcode in addition to your password when signing in.

To enable, download Google Authenticator from `iTunes <https://itunes.apple.com/us/app/google-authenticator/id388497605?mt=8>`__ or `Google Play <https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=en>`__ for your phone, then:

1. Select the **Add MFA to your account** button.
2. Use Google Authenticator to scan the QR code that appears.
3. Enter the token generated by Google Authenticator, then select **Save**.

In future, you will be asked to enter a passcode from Google Authenticator in addition to your password on login.

If you are unable to scan the QR code, you can:

1. Select the **Add MFA to your account** button. You should see a ``Secret Key`` below the QR code.
2. Open Google Authenticator.
3. Select the **+** button, then select **Manual Entry**.
4. Enter an account name.
5. Enter the ``Secret Key`` from Mattermost into the ``Key`` field in Google Authenticator, then select **Save**.
6. In Mattermost, enter the token generated by Google Authenticator, then select **Save**.

Sign-in Method
~~~~~~~~~~~~~~

This option allows you to switch your sign-in method from email/password to a single sign-on option, and back again.

For example, if AD/LDAP single sign-on is enabled, users can select a "Switch to using AD/LDAP" button and the enter their AD/LDAP credentials to switch sign-in over to AD/LDAP. They also need to enter the password for their email account to verify their existing credentials. Following the change, users receive an email to confirm the action.

View Access History
~~~~~~~~~~~~~~~~~~~

Access History displays a chronological list of the last 20 login and logout attempts, channel creations and deletions, account settings changes, or channel setting modifications made on your account. The details of the Session ID (unique identifier for each Mattermost browser session) and IP Address of the action is recorded for audit log purposes.

View and Logout of Active Sessions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sessions are created when you log in with your email and password to a new browser on a device. Sessions let you use Mattermost for up to 30 days without having to log in again. Select **Logout** on an active session if you want to revoke automatic login privileges for a specific browser or device. Select **More Info** to view details on browser and operating system.

Notifications
-------------

Settings to configure desktop notifications, desktop notification sounds, email notifications, mobile push notifications, and words that trigger mentions.

.. tabs::

  .. tab:: Mattermost v6.0 onwards

      In Mattermost v6.0, **Account Settings** have moved.

      - Access **Profile** and **Security** settings from your avatar in the Global Header.
      - Access **Notifications**, **Display**, **Sidebar**, and **Advanced Settings** by selecting the **Gear** icon in the Global Header.
      
  .. tab:: Mattermost v5.39 and earlier

      In Mattermost versions up to 5.39, access **Account Settings** from the **Main Menu** by selecting the three horizontal lines (also known as a hambuger menu) at the top of the channel sidebar. 

Desktop Notifications
~~~~~~~~~~~~~~~~~~~~~

Desktop notifications appear in the top corner of your main monitor when there is activity in Mattermost.

Send Desktop Notifications
^^^^^^^^^^^^^^^^^^^^^^^^^^

Choose what activity triggers a desktop notification. This setting applies globally, but this preference is customizable for each channel from the channel name drop-down menu. Desktop notifications are available on Chrome, Edge, Firefox, and Safari.

When `Desktop App <https://mattermost.com/download/#mattermostApps>`__ notifications are set to "Only for mentions and direct messages":

- An empty red circle is displayed over the upper right corner of the Mattermost dock icon when any message without an at-mention is received. 
- A solid red circle with a post count is displayed when a message with an at-mention is received.
- And when `Collapsed Reply Threads (Beta) <https://docs.mattermost.com/messaging/managing-account-settings.html#collapsed-reply-threads-beta>`__ is enabled, you can choose to receive desktop notifications about `threads you're following <https://docs.mattermost.com/messaging/organizing-conversations.html#start-or-reply-to-threads>`__.

Notification Sound
^^^^^^^^^^^^^^^^^^

Notification sounds fire for any activity that would trigger a desktop notification. Notification sounds are available on Chrome, Edge, Firefox, and Safari in addition to the Mattermost Desktop App.

Notification Duration
^^^^^^^^^^^^^^^^^^^^^

*Removed in June 16th, 2018 release*

In Mattermost v5.0 and later, desktop notifications will stay onscreen for five seconds when supported by the browser and operating system.

Email Notifications
~~~~~~~~~~~~~~~~~~~

Email notifications are sent for mentions and direct messages after you’ve been offline for more than 60 seconds or away from Mattermost for more than five minutes. Change the email where notifications are sent in **Account Settings > General > Email**.

If your System Admin has enabled `Email Batching <https://docs.mattermost.com/configure/configuration-settings.html#enable-email-batching>`__, you'll have additional options under this settings to select how often email notifications will be sent. All notifications received over this time period are combined and sent in a single email.

Mobile Push Notifications
~~~~~~~~~~~~~~~~~~~~~~~~~

Push notifications can be sent to your mobile device if you have the Android or iOS app installed. You can choose the type of activity that will send a notification. 

By default, push notifications are sent "For mentions and direct messages". If push notifications are sent "Never", the Mattermost setting to trigger push notifications depending on your `Mattermost availability <https://docs.mattermost.com/messaging/setting-your-status-availability.html>`__ is hidden. If your System Admin has not set up push notifications, this setting will be disabled.

If you're actively viewing a channel (Public or Private), Direct Message, or Group Message using the Desktop App or a browser, no push notifications will be sent for that channel. If a notification is viewed using the Desktop App or a browser, the lockscreen notification will clear on Android, and on iOS the badge on the Mattermost app icon will count down accordingly.

Trigger Mobile Push Notifications When
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also choose when to send push notifications depending on your Mattermost availability. By default, push notifications are sent if your availability is **Away** or **Offline**. If **Send Mobile Push Notifications** is set as **Never**, this setting is hidden. If your System Admin has not set up push notifications, this setting will be disabled.

Words That Trigger Mentions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, you receive notifications when someone posts a message that contains your non-case sensitive username or @username. You also receive notifications when someone uses the @channel, @all, and @here mentions. You can customize the words that trigger mentions by typing them into the input box. This is useful if you want to be notified of all posts on a certain topic, for example, "marketing".

Reply Notifications
~~~~~~~~~~~~~~~~~~~

When `Collapsed Reply Threads (Beta) <https://docs.mattermost.com/messaging/managing-account-settings.html#collapsed-reply-threads-beta>`__ is disabled, you can choose to receive mention notifications when someone replies to a thread you have started or have participated in. 

- You are considered to start a thread when you post a message to which other members of your team reply. 
- You are considered to participate in a thread when you post a message using the `Reply button <https://docs.mattermost.com/messaging/messaging-basics.html>`__ in an pre-existing thread.

.. note::
  This setting is hidden when Collapsed Reply Threads (Beta) is enabled.

Automatic Direct Message Replies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set an automated custom message that will be sent once per day in response to Direct Messages. Mentions in Public and Private Channels won't trigger the automated reply. Enabling Automatic Replies sets your availability to **Out of Office** and disables desktop, email, and push notifications. This setting is experimental and `must be enabled by your System Admin <https://docs.mattermost.com/configure/configuration-settings.html#enable-automatic-replies-experimental>`__.

Display
-------

Settings to configure clock and teammate name display preferences.

.. tabs::

  .. tab:: Mattermost v6.0 onwards

      In Mattermost v6.0, **Account Settings** have moved.

      - Access **Profile** and **Security** settings from your avatar in the Global Header.
      - Access **Notifications**, **Display**, **Sidebar**, and **Advanced Settings** by selecting the **Gear** icon in the Global Header.

  .. tab:: Mattermost v5.39 and earlier

      In Mattermost versions up to 5.39, access **Account Settings** from the **Main Menu** by selecting the three horizontal lines (also known as a hambuger menu) at the top of the channel sidebar.

Theme
~~~~~

Select **Theme Colors** to select from four standard themes designed by the Mattermost team. To make custom adjustments on the four standard theme colours, select a standard theme and then select **Custom Theme** to load the standard theme into the custom theme color selectors.

Select **Custom Theme** to customize your theme colors and share them with others by copying and pasting theme vectors into the input box. Observe a live preview as you customize theme colors, then select **Save** to confirm your changes. Discard your changes by selecting **Cancel**, or by exiting the settings modal and selecting **Yes, Discard**.

In Enterprise Edition, if you belong to multiple teams, you can optionally select the checkbox "Apply new theme to all my teams" to have the theme show up across teams. Otherwise, the changes will only apply to the current team.

Learn more about the custom theme color selectors `here <https://docs.mattermost.com/messaging/customizing-theme-colors.html>`__.

Select **Import theme colors from Slack** to import a Slack theme. In Slack, go to **Preferences > Sidebar Theme** and open the custom theme option. From there, copy the theme color vector and then paste it into the *Input Slack Theme* input box in Mattermost. Any theme settings that are not customizable in Slack will default to the “Sapphire” standard theme settings.

Display Font
~~~~~~~~~~~~

*Removed in July 16th, 2017 release*

Select what font is used.

Clock Display
~~~~~~~~~~~~~

Choose a 12-hour or 24-hour time preference that appears on the time stamp for all posts.

Teammate Name Display
~~~~~~~~~~~~~~~~~~~~~

Configure how names are displayed in the user interface: nickname, username or full name. The default for this setting is dependent on the `configuration set by the System Admin <https://docs.mattermost.com/configure/configuration-settings.html#teammate-name-display>`__.

Show online availability on profile images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Online availability icons display on user profile avatars in the center channel by default. Disable this setting to hide online availability icons within the center channel.

Timezone
~~~~~~~~~

Select the timezone used for timestamps in the user interface and for email notifications. 

.. note::
  
  In Mattermost v5.38 or earlier, timezone functionality `must first be enabled by the System Admin <https://docs.mattermost.com/configure/configuration-settings.html#timezone>`__ by replacing ``false`` with ``true`` in ``config.json``. Timezone is enabled by default from Mattermost v6.0.

Website Link Previews
~~~~~~~~~~~~~~~~~~~~~

When available, the first web link in a message will show a preview of the website content below the message. This `setting must be enabled by your System Admin <https://docs.mattermost.com/configure/configuration-settings.html#enable-link-previews>`__.

Default Appearance of Image Previews
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When messages in Mattermost include images, an image preview can display directly below the message for image attachments, image link previews, and `in-line images <https://docs.mattermost.com/messaging/formatting-text.html#in-line-images>`__ over 100px in height. You can set this preference to **Expanded** or **Collapsed**.

.. tip::
  This setting can also be controlled using the slash commands ``/expand`` and ``/collapse``.

Message Display
~~~~~~~~~~~~~~~

Select the formatting for messages in the center channel. "Compact" mode decreases the spacing around posts, collapses link previews, and hides thumbnails so only file names are shown. Some formatting types, such as block quotes and headings, are also reduced in size.

Collapsed Reply Threads (Beta)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Collapsed Reply Threads (Beta) offers an enhanced experience for users communicating in threads and replying to messages. Collapsed Reply Threads are available in Mattermost Cloud and from self-hosted Mattermost v5.37 as an early access beta, and are disabled by default. If your System Admin has enabled **Collapsed Reply Threads** for your workspace, you can enable them in your Mattermost instance to start being notified about threads you're following in a new **Threads** option at the top of the channel sidebar.

See our `Organizing Conversations using Collapsed Reply Threads (Beta) <https://docs.mattermost.com/messaging/organizing-conversations.html>`__ documentation to learn more about this feature.

Channel Display
~~~~~~~~~~~~~~~

Select if the text in the center channel is fixed width and centered, or full width.

Language
~~~~~~~~

Select what language Mattermost displays in the user interface. Options include:

- Deutsch - German
- English (U.S.)
- English Australian
- Español - Spanish
- Français - French
- Italiano - Italian
- Magyar - Hungarian
- Nederlands - Dutch
- Polski - Polish
- Português (Brasil) - Portuguese
- Română - Romanian
- Svenska - Swedish
- Türkçe - Turkish
- български - Bulgarian
- Pусский - Russian
- Yкраїнська - Ukrainian
- 한국어 - Korean
- 中文 (简体) - Simplified Chinese
- 中文 (繁體) - Traditional Chinese
- 日本語 - Japanese

Sidebar
-------

The channel sidebar includes `enhanced sidebar features <https://docs.mattermost.com/messaging/organizing-your-sidebar.html>`__, including custom, collapsible channel categories, drag and drop, unread filtering, channel sorting options, and more.

.. tabs::

  .. tab:: Mattermost v6.0 onwards

      In Mattermost v6.0, **Account Settings** have moved.

      - Access **Profile** and **Security** settings from your avatar in the Global Header.
      - Access **Notifications**, **Display**, **Sidebar**, and **Advanced Settings** by selecting the **Gear** icon in the Global Header.
      
  .. tab:: Mattermost v5.39 and earlier

      In Mattermost versions up to 5.39, access **Account Settings** from the **Main Menu** by selecting the three horizontal lines (also known as a hambuger menu) at the top of the channel sidebar.

The following sidebar settings apply to your current sidebar only:

**Group unread channels separately**

This feature groups unread channels at the top of the channel sidebar in an **Unreads** category. System Admins can `set the default of this setting <https://docs.mattermost.com/configure/configuration-settings.html#group-unread-channels-experimental>`__ for you. 

Legacy sidebar settings
~~~~~~~~~~~~~~~~~~~~~~~

The legacy sidebar `must be enabled by your System Admin <https://docs.mattermost.com/configure/configuration-settings.html#enable-legacy-sidebar>`__. The following sidebar settings apply only to the legacy sidebar:

Channel grouping
^^^^^^^^^^^^^^^^

Channels can be grouped by type (Public, Private, or Direct Message), or all channel types can be grouped in a single list. 

Channel sorting
^^^^^^^^^^^^^^^

Channels can be sorted within their channel sidebar sections alphabetically (default) or by most recent message.

Channel switcher
^^^^^^^^^^^^^^^^

Hide the channel switcher used to jump between channels quickly. The channel switcher can also be accessed using CTRL/CMD+K.

Autoclose Direct Messages
^^^^^^^^^^^^^^^^^^^^^^^^^

Hide Direct Message conversations with no activity for seven days. These conversations can be reopened with the **+** button in the channel sidebar, or by using the Channel Switcher (CTRL+K). This setting is experimental and `must be enabled by your System Admin <https://docs.mattermost.com/configure/configuration-settings.html#autoclose-direct-messages-in-sidebar-experimental>`__.

Advanced
--------

Settings to configure when messages are sent.

.. tabs::

  .. tab:: Mattermost v6.0 onwards

      In Mattermost v6.0, **Account Settings** have moved.

      - Access **Profile** and **Security** settings from your avatar in the Global Header.
      - Access **Notifications**, **Display**, **Sidebar**, and **Advanced Settings** by selecting the **Gear** icon in the Global Header.
      
  .. tab:: Mattermost v5.39 and earlier

      In Mattermost versions up to 5.39, access **Account Settings** from the **Main Menu** by selecting the three horizontal lines (also known as a hambuger menu) at the top of the channel sidebar.

Send messages on CTRL+ENTER
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If "On for all messages" is enabled, ENTER inserts a new line and CTRL+ENTER posts a message. If "On only for code blacks starting with ```" is enabled, ENTER inserts a new line inside an open code block and CTRL+ENTER automatically closes the code block and posts the message. If disabled, SHIFT+ENTER inserts a new line and ENTER posts the message.

Enable Post Formatting
~~~~~~~~~~~~~~~~~~~~~~

This setting controls whether post formatting is rendered. When "On", posts will be rendered with `markdown formatting <https://docs.mattermost.com/messaging/formatting-text.html>`__, emoji, autolinked URLs, and line breaks. When "Off", the raw text will be shown.

Enable Join/Leave Messages
~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting controls whether system messages about users joining or leaving a channel are visible. When **On** these messages will appear. When **Off**, these messages will be hidden. If any users are added to or removed from a channel, a system message will still be shown even if this setting is **Off**.

Preview pre-release features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Turn on preview features to view them early, ahead of their official release:

- **Show markdown preview option in message input box** Turning this on will show a "Preview" option when typing in the text input box. Pressing "Preview" shows what the Markdown formatting in the message looks like before the message is sent.

Deactivate Account
~~~~~~~~~~~~~~~~~~

Use this setting to deactivate your account. After deactivating, an email notification is sent confirming the deactivation was successful.

Deactivating your account removes your ability to log in to the Mattermost server and disables all email and mobile notifications. To reactivate your account, contact your System Admin.

Only available for accounts with email login, and if your System Admin has set ``EnableUserDeactivation`` to ``true`` in ``config.json``.

For accounts with other authentication methods such as AD/LDAP or SAML, or for accounts that do not have this setting available, contact your System Admin to deactivate your account.
