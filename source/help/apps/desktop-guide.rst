===================================
Desktop Guide
===================================

Mattermost desktop applications are available for Windows, Mac and Linux operation systems. 

You can `download the apps directly from our download page <https://about.mattermost.com/downloads/>`_ and you can visit our `installation guides <https://docs.mattermost.com/install/desktop.html>`_ for help during set up.

Below are a few tips to get you started and configuring your experience on the desktop app:

 - `Team Management <https://docs.mattermost.com/help/apps/desktop-guide.html#team-management>`_
 - `Settings <https://docs.mattermost.com/help/apps/desktop-guide.html#settings>`_
 - `Menu Bar <https://docs.mattermost.com/help/apps/desktop-guide.html#menu-bar>`_

Team management
---------------------------------------------------------------------

You can connect to multiple Mattermost servers from a single interface on the desktop app.

**Adding servers and teams**

To add a new server on the Mattermost instance, 

1. Click **Add new team** next to the right of Team Management section.
2. Enter **Name** and a valid **URL**, which begins with either ``http://`` or ``https://``.
3. Click **Add**.

You can now access all teams you have joined in the server once you have saved the settings, and each will appear as a separate tab in the app. 

You may also add a separate instance for each team, if you'd like.

**Editing servers and teams**

To edit a server, 

1. To the right of the team or server you want update, click **Edit**.
2. Edit **Name** and/or **URL**.
3. Click **Save**.

**Removing servers and teams**

To remove a server from your desktop app environment, click on **Remove** next to the server or a team you want removed. Note that this action cannot be undone.

Settings
---------------------------------------------------------------------

In addition to `Mattermost Account Settings <https://docs.mattermost.com/help/settings/account-settings.html>`_ , the desktop app provides additional options to customize your experience. 

The Settings Page is available from the `File` menu under `Settings`, and can be accessed with `CTRL + COMMA` on Windows and Linux, and with `CMD + COMMA` on Mac.

Description of each setting is included below this table.

+-------------------------------------------------------------------------------+---------------------------+---------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting                                                                       | On Windows                | On OS X                   | On Linux                  | Contributors                                                                                                                                           | 
+===============================================================================+===========================+===========================+===========================+========================================================================================================================================================+
| Hide menu bar                                                                 | v0.5.0 +                  | v0.5.0 +                  | v1.0.3 +                  | `yuya-oc <https://github.com/yuya-oc>`_ (Windows, OS X); `alerque <https://github.com/alerque>`_ (Linux)                                               |
+-------------------------------------------------------------------------------+---------------------------+---------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| Allow mixed content                                                           | v1.2.0 +                  | v1.2.0 +                  | v1.2.0 +                  | `yuya-oc <https://github.com/yuya-oc>`_                                                                                                                |
+-------------------------------------------------------------------------------+---------------------------+---------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| Start app on login                                                            | v1.3.0 +                  | v1.3.0 +                  | v1.3.0 +                  | `Razzeee <https://github.com/Razzeee>`_                                                                                                                |
+-------------------------------------------------------------------------------+---------------------------+---------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| Toggle window visibility when clicking on the tray icon                       | v1.3.0 +                  | N/A                       | N/A                       | `magicmonty <https://github.com/magicmonty>`_                                                                                                          |
+-------------------------------------------------------------------------------+---------------------------+---------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| Leave app running in notification center when application window is closed    | N/A                       | v1.3.0 +                  | v1.3.0 +                  | `magicmonty <https://github.com/magicmonty>`_ (OS X); `yuya-oc <https://github.com/yuya-oc>`_ (Linux)                                                  |
+-------------------------------------------------------------------------------+---------------------------+---------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| Show red badge on taskbar icon to indicate unread messages                    | v1.4.0 +                  | v1.4.0 +                  | N/A                       | `Razzeee <https://github.com/Razzeee>`_                                                                                                                |
+-------------------------------------------------------------------------------+---------------------------+---------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| Flash taskbar icon when a new message is received                             | v1.3.0 +                  | N/A                       | v1.4.0 +                  | `MetalCar <https://github.com/metalcar>`_ (Windows); `jnugh <https://github.com/jnugh>`_ (Linux)                                                       |
+-------------------------------------------------------------------------------+---------------------------+---------------------------+---------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+


**Hide menu bar**

Hides the menu bar. When enabled, pressing ``ALT`` will toggle whether the menu bar is shown or hidden.

This setting is off by default.

**Allow mixed content**

If your server is hosted on `https://`, insecure content, images and scripts with `http://` are not rendered by default. This option allows such content to be rendered. If you do enable it, please be mindful of potential security risks shared over `http://` protocols.

This setting is on by default.

Note: Enabling both secure and insecure content will break YouTube videos. An open issue for ``electron`` on which the app is built is under investigation: https://github.com/electron/electron/issues/2749

**Start app on login**

When enabled, Mattermost application starts when you login to your machine.

This setting is on by default.

**Toggle window visibility when clicking on the tray icon** (Windows)

When enabled, clicking on the system tray icon allows you to toggle the window open and minimized.

This setting is off by default.

**Leave app running in notification center when application window is closed.** (OS X, Linux)

When enabled, closing the application window will leave the Mattermost desktop app running in your notification center. This can be useful if you’d like to check for unread mentions while away from the app.

This setting is off by default.

**Show red badge on taskbar icon to indicate unread messages** (Windows, OS X)

If you have multiple active teams (either on a single or multiple servers), having a red badge for unread messages may be annoying as it would likely be displayed most of the time. You may use this setting to configure when the red badge is shown on the taskbar icon. 
If enabled, a red badge is shown for unread messages with a number count indicating unread mentions. If disabled, a red badge is only shown for unread mentions (with a number count).

This setting is on by default.

**Flash taskbar icon when a new message is received** (Windows, Linux)

Configure whether the taskbar icon flashes when a new message is received on any of your active teams and servers.

This setting is off by default.

Menu Bar
---------------------------------------------------------------------

The desktop app contains a menu bar with additional features and shortcuts to streamline your experience. 

If the menu bar is hidden, you may use the ``ALT`` key to display the menu. To have the menu displayed at all times, go to the Settings page and uncheck the **Hide menu bar** setting.

Below is a list of menu options with the corresponding keyboard shortcuts. For Mac OS X, replace `CTRL` by `CMD` unless otherwise specified.

**File**

 - Settings (CTRL + COMMA): Opens app settings where you can manage your servers and configure desktop app settings
 - Exit (CTRL + Q): Closes the application. Labeled `Quit` on Mac OS X

**Edit**

 - Undo (CTRL + Z): Reverses previous action
 - Redo (CTRL + SHIFT + Z; CTRL + Y): Redoes the most recent action
 - Cut (CTRL + X): Cuts selected text
 - Copy (CTRL + C): Copies selected text
 - Paste (CTRL + V): Pastes text from the clipboard
 - Select All (CTRL + A): Selects all text in input box
 - Search in Team (CTRL + S): Sets focus on the Mattermost search box
 - Search in Channel (CTRL + SHIFT + S): Sets focus on the Mattermost search box and adds `in:[Channel]` to search in current channel

**View**

 - Reload (CTRL + R): Reloads the current page
 - Clear Cache and Reload (CTRL + SHIFT + R): Clears cached content in application and reloads the current page
 - Toggle Full Screen (F11): Toggles the application window full screen mode
 - Actual Size (CTRL + 0) - Resets zoom level to default
 - Zoom In (CTRL + =; CTRL + SHIFT + =) - Increase font size (zoom in)
 - Zoom In (CTRL + MINUS) - Decrease font size (zoom out)
 - Toggle Developer Tools (CTRL + SHIFT + I): Toggles sidebar showing developer tools

**History**

 - Back (ALT + Left Arrow; CMD + [ on OS X): Go to previous page in history
 - Forward (ALT + Right Arrow; CMD + [ on OS X): Go to next page in history

**Window**

 - Close (CTRL + W) - Closes the application window
 - Minimize (CTRL + M) - Minimizes the application window to the taskbar
 - Team Name (CTRL + {1-9}) - Opens the n-th tab
 - Select Next Team (CTRL + TAB; ALT + CMD + Right Arrow on OS X) - Opens the next tab
 - Select Previous Team (CTRL+ SHIFT + TAB; ALT + CMD + Left Arrow on OS X) - Open the previous tab

**Help**

 - Mattermost Docs - Links to a parent page for `Desktop applications documentation <https://docs.mattermost.com/install/desktop.html>`_ .
 - Version - Indicates the desktop application version in use
