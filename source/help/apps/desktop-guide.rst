===================================
Using Mattermost Desktop App
===================================

Mattermost desktop applications are available for Windows, Mac and Linux operating systems. 

You can `download the apps directly from our download page <https://about.mattermost.com/downloads/>`_ and visit our `installation guides <https://docs.mattermost.com/install/desktop.html>`_ for help during set up and for troubleshooting tips.

To view the latest updates, please see our `changelog <https://docs.mattermost.com/help/apps/desktop-changelog.html>`_.

Below are a few tips to get you started and to configure your experience on the desktop app:

 - `Team Management <https://docs.mattermost.com/help/apps/desktop-guide.html#id1>`_
 - `App Options <https://docs.mattermost.com/help/apps/desktop-guide.html#id2>`_
 - `Menu Bar <https://docs.mattermost.com/help/apps/desktop-guide.html#id3>`_

Team Management
---------------------------------------------------------------------

You can connect to multiple Mattermost servers from a single interface on the desktop app.

The Team Management section allows you to add, edit and remove servers and teams.

Adding servers and teams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To add a new server on the Mattermost instance, 

1. On the menu bar, go to **File** > **Settings** or press CTRL/CMD+COMMA
2. Click **Add new team** in the Team Management section.
3. In the **Name** field, enter the name that you want for the tab. 
4. In the **URL** field, enter the complete URL of the server that you want to connect to. Must begin with either ``http://`` or ``https://``.
5. Click **Add**.
6. Click **Save**.

You can now access all teams you have joined in the server once you have saved the settings, and each will appear as a separate tab in the app. 

You may also add each team separately, if you'd like.

Editing servers and teams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To edit a server, 

1. On the menu bar, go to **File** > **Settings** or press CTRL/CMD+COMMA
2. Next to the team or server you want update, click **Edit**.
3. Edit **Name** and/or **URL**.
4. Click **Save**.

Removing servers and teams
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To remove a server from your desktop app environment, 

1. On the menu bar, go to **File** > **Settings** or press CTRL/CMD+COMMA
2. Click on **Remove** next to the server or a team you want removed.
3. Click **Save**.

App Options
---------------------------------------------------------------------

In addition to `Mattermost Account Settings <https://docs.mattermost.com/help/settings/account-settings.html>`_ , the desktop app provides additional options to customize your experience. 

The options appear in the Settings page, available from the **File** > **Settings** or by CTRL/CMD+COMMA.

Allow mixed content
    If your server is hosted on ``https://``, insecure content, images and scripts with ``http://`` are not rendered by default. This option allows such content to be rendered. If you do enable it, please be mindful of potential security risks shared over ``http://`` protocols.
    
    This setting is enabled by default.

Show red badge on taskbar icon to indicate unread messages (Windows, Mac only)
    When enabled, a red badge is shown on the taskbar icon for unread messages with a number count indicating unread mentions. If disabled, a red badge is only shown for unread mentions (with a number count).

    This setting is enabled by default.

Flash taskbar icon when a new message is received (Windows, Linux only)
    Configure whether the taskbar icon flashes when a new message is received on any of your active teams and servers.

    This setting is disabled by default.

Start app on login (Windows, Linux only)
    When enabled, Mattermost application starts when you log in to your machine.

    This setting is enabled by default.

Hide menu bar (Windows, Linux only)
    Hides the menu bar. When enabled, pressing ALT will toggle whether the menu bar is shown or hidden.

    This setting is disabled by default.

Toggle window visibility when clicking on the tray icon (Windows only)
    When enabled, clicking on the system tray icon allows you to toggle the window open and minimized.

    This setting is disabled by default.

Show icon on Menu Bar (Mac, Linux only)
    When enabled, a red dot with a count of unread mentions is displayed on the team tab bar.

    This setting is disabled by default.

Leave app running in notification center when application window is closed (Mac, Linux only)
    When enabled, closing the application window will leave the Mattermost desktop app running in your notification center. This can be useful if you’d like to check for unread mentions while away from the app.

    This setting is disabled by default.
