Using Mattermost Desktop App
============================

Mattermost desktop applications are available for Windows, Mac and Linux operating systems.

.. image:: ../../images/desktop.png

You can `download the apps directly from our download page <https://about.mattermost.com/downloads/>`__ and visit our `installation guides <https://docs.mattermost.com/install/desktop.html>`__ for help during setup and for troubleshooting tips.

To view the latest updates, please see our `changelog <https://docs.mattermost.com/help/apps/desktop-changelog.html>`__.

Below are a few tips to get you started and to configure your experience on the desktop app:

.. contents::
    :backlinks: top
    :local:

Server Management
-----------------

You can connect to multiple Mattermost servers from a single interface on the desktop app. Servers appear as separate tabs at the top of the desktop window and can be reordered by dragging.

The Server Management section allows you to add, edit, and remove servers. 

Adding Servers
~~~~~~~~~~~~~~

To add a new server to your desktop app environment:

1. Click the **+** button in the desktop window bar at the top of the screen.
2. In the **Name** field, enter the name that you want for the tab.
3. In the **URL** field, enter the complete URL of the server that you want to connect to. Must begin with either ``http://`` or ``https://``.
4. Click **Add**.

Editing Servers
~~~~~~~~~~~~~~~

To edit a server in your desktop app environment:

1. On Windows, go to **... > File > Settings**. On Mac, go to **Mattermost > Preferences**.
2. Next to the server you want to update, click **Edit**.
3. Edit **Name** and/or **URL**.
4. Click **Save**.

Removing Servers
~~~~~~~~~~~~~~~~

To remove a server from your desktop app environment:

1. On Windows, go to **... > File > Settings**. On Mac, go to **Mattermost > Preferences**.
2. Next to the server or team that you want to remove, click **Remove**.
3. Click **Remove**.

App Options
-----------

In addition to `Mattermost Account Settings <https://docs.mattermost.com/help/settings/account-settings.html>`__ , the desktop app provides additional options to customize your experience.

The options appear in the Settings page, available on Windows from **... > File > Settings**, or on Mac from **Mattermost > Preferences**.

Start app on login (Windows, Linux only)
    When enabled, Mattermost application starts when you log in to your machine.

    This setting is enabled by default.

Check spelling
    Highlight misspelled words in your messages. Available for English, French, German, Spanish, and Dutch. To change the spelling language, right-click inside a message box and navigate to **Spelling Languages** in the context menu.

    This setting is enabled by default.

Show red badge on taskbar icon to indicate unread messages (Windows, Mac only)
    When enabled, a red badge is shown on the taskbar icon for unread messages with a number count indicating unread mentions or direct messages. If disabled, a red badge is only shown for unread mentions (with a number count).

    This setting is enabled by default.

Flash taskbar icon when a new message is received (Windows, Linux only)
    Configure whether the taskbar icon flashes for a few messages when a new message is received on any of your active teams and servers.

    This setting is disabled by default.
    
Bounce the Dock icon when receiving a notification (Mac only)
    When enabled, the Dock icon will either bounce once or bounce until the user opens the app when receiving a notification.
    
    This setting is disabled by default.

Show Mattermost icon in the menu bar (Mac only)
    When enabled, Mattermost icon is added to the Mac menu bar.

    This setting is disabled by default.

Show icon in the notification area (Linux only)
    When enabled, Mattermost icon is added to the Linux notification area.

    This setting is disabled by default.

Leave app running in notification center when application window is closed (Linux only)
    When enabled, closing the application window will leave the Mattermost desktop app running in your notification center. This can be useful if you want to check for unread mentions while away from the app.

    This setting is disabled by default.
    
Use GPU hardware acceleration
    If enabled, Mattermost UI is rendered more efficiently but can lead to decreased stability for some systems. Setting takes effect after restarting the app.

    This setting is disabled by default.

Dark Theme
~~~~~~~~~~~~~~~~
On macOS, the Mattermost desktop app respects the System Preferences appearance setting of the operating system to set the theme of the title bar. On Windows, you can toggle the theme of the Mattermost desktop app title bar in **... > View > Toggle Dark Mode**.  

.. image:: ../../images/dark_theme.png
