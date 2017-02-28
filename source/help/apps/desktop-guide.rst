Using Mattermost Desktop App
============================

Mattermost desktop applications are available for Windows, Mac and Linux operating systems.

You can `download the apps directly from our download page <https://about.mattermost.com/downloads/>`_ and visit our `installation guides <https://docs.mattermost.com/install/desktop.html>`_ for help during setup and for troubleshooting tips.

To view the latest updates, please see our `changelog <https://docs.mattermost.com/help/apps/desktop-changelog.html>`_.

Below are a few tips to get you started and to configure your experience on the desktop app:

.. contents::
    :backlinks: top
    :local:

Server Management
-----------------

You can connect to multiple Mattermost servers from a single interface on the desktop app. Servers appear as separate tabs while you are using the app.

The Server Management section allows you to add, edit, and remove servers. 

Adding Servers
~~~~~~~~~~~~~~

To access a new server from your desktop app environment:

1. On the menu bar, go to **File > Settings**.
2. In the *Server Management* section, click **Add new server**.
3. In the **Name** field, enter the name that you want for the tab.
4. In the **URL** field, enter the complete URL of the server that you want to connect to. Must begin with either ``http://`` or ``https://``.
5. Click **Add**.

Editing Servers
~~~~~~~~~~~~~~~

To edit a server in your desktop app environment:

1. On the menu bar, go to **File > Settings**.
2. Next to the server you want to update, click **Edit**.
3. Edit **Name** and/or **URL**.
4. Click **Save**.

Removing Servers
~~~~~~~~~~~~~~~~

To remove a server from your desktop app environment:

1. On the menu bar, go to **File > Settings**.
2. Next to the server or team that you want to remove, click **Remove**.
3. Click **Remove**.

App Options
-----------

In addition to `Mattermost Account Settings <https://docs.mattermost.com/help/settings/account-settings.html>`_ , the desktop app provides additional options to customize your experience.

The options appear in the Settings page, available from the **File > Settings** or by CTRL/CMD+COMMA.

Start app on login (Windows, Linux only)
    When enabled, Mattermost application starts when you log in to your machine.

    This setting is enabled by default.

Display secure content
    If your server is hosted on ``https://``, insecure content, images and scripts with ``http://`` are not rendered by default. This option allows such content to be rendered. If you disable it, please be mindful of potential security risks shared over ``http://`` protocols.

    This setting is enabled by default.

Show red badge on taskbar icon to indicate unread messages (Windows, Mac only)
    When enabled, a red badge is shown on the taskbar icon for unread messages with a number count indicating unread mentions or direct messages. If disabled, a red badge is only shown for unread mentions (with a number count).

    This setting is enabled by default.

Flash taskbar icon when a new message is received (Windows, Linux only)
    Configure whether the taskbar icon flashes for a few messages when a new message is received on any of your active teams and servers.

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
