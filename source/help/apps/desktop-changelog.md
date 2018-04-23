# Desktop Application Changelog

## Release v3.4.1

Release date: September 30, 2016

This release contains a security update and it is highly recommended that users upgrade to this version.

Version number updated to 3.4 to make numbering consistent with Mattermost server and mobile app releases. This change will not imply bi-monthly releases.

 - v3.4.1, released 2016-09-30
     - (OS X) Fixed an issue where the app window pops up second to foreground when a new message is received
 - v3.4.0, released 2016-09-22
     - Original v3.4 release

### Improvements

#### Windows
 - Current team and channel name shown in window title bar
 - Team tab is bolded for unread messages and has a red dot with a count of unread mentions
 - Added an option to configure whether a red badge is shown on taskbar icon for unread messages
 - Added new shortcuts:
     - `CTRL + S`: sets focus on the Mattermost search box
     - `ALT + Left Arrow`: go to previous page in history
     - `ALT + Right Arrow`: go to next page in history
 - Upgraded the Settings page user interface
 - Added access to the settings menu from the system tray icon
 - Added validation for name and URL when adding a new team on the Settings page
 - The app now tries to reconnect periodically if a page fails to load
 - Only one instance of the desktop application will now load at a time

#### OS X
 - Current team and channel name shown in window title bar
 - Team tab is bolded for unread messages and has a red dot with a count of unread mentions
 - Added an option to configure whether a red badge is shown on taskbar icon for unread messages
 - Added new shortcuts:
     - `CMD + S`: sets focus on the Mattermost search box
     - `CMD + [`: go to previous page in history
     - `CMD + ]`: go to next page in history
 - Upgraded the Settings page user interface
 - The app now tries to reconnect periodically if a page fails to load
 - Added validation for name and URL when adding a new team on the Settings page

#### Linux (Beta)
 - Current team and channel name shown in window title bar
 - Team tab is bolded for unread messages and has a red dot with a count of unread mentions
 - Added an option to flash taskbar icon when a new message is received
 - Added a badge to count mentions on the taskbar icon (for Unity)
 - Added a script, `create_desktop_file.sh`, to create `Mattermost.desktop` desktop entry to help [integrate the application into a desktop environment](https://wiki.archlinux.org/index.php/Desktop_entries) more easily
 - Added new shortcuts:
     - `CTRL + S`: sets focus on the Mattermost search box
     - `ALT + Left Arrow`: go to previous page in history
     - `ALT + Right Arrow`: go to next page in history
 - Upgraded the Settings page user interface
 - Added access to the settings menu from the system tray icon
 - The app now tries to reconnect periodically if a page fails to load
 - Added validation for name and URL when adding a new team on the Settings page
 - Only one instance of the desktop application will now load at a time

### Bug Fixes

#### Windows
 - Cut, copy and paste are shown in the user interface only when the commands are available
 - Copying link addresses now work properly
 - Saving images by right-clicking the image preview now works
 - Refreshing the app page no longer takes you to the team selection page, but keeps you on the current channel
 - Removed misleading shortcuts from the system tray menu
 - Removed unclear desktop notifications when the application page fails to load
 - Fixed the Mattermost icon for desktop notifications in Windows 10
 - Fixed an issue where the maximized state of the app window was lost in some cases
 - Fixed an issue where shortcuts didn't work when switching applications or tabs in some cases
 - Fixed an issue where application icon at the top left of the window was pixelated
 - Fixed an issue where the application kept focus after closing the app window

#### OS X
 - Cut, copy and paste are shown in the user interface only when the commands are available
 - Copying link addresses now work properly
 - Saving images by right-clicking the image preview now works
 - Refreshing the app page no longer takes you to the team selection page, but keeps you on the current channel
 - Fixed an issue where the maximized state of the app window was lost in some cases
 - Fixed an issue where shortcuts didn't work when switching applications or tabs in some cases

#### Linux (Beta)
 - Cut, copy and paste are shown in the user interface only when the commands are available
 - Copying link addresses now work properly
 - Saving images by right-clicking the image preview now works
 - Refreshing the app page no longer takes you to the team selection page, but keeps you on the current channel
 - Removed misleading shortcuts from the system tray menu
 - Removed unclear desktop notifications when the application page fails to load
 - Fixed an issue where the maximized state of the app window was lost in some cases
 - Fixed an issue where shortcuts didn't work when switching applications or tabs in some cases

### Known Issues

#### Windows
 - Copying a link address and pasting it inside the app doesn't work
 - YouTube videos do not work if mixed content is enabled from app settings

#### OS X
 - YouTube videos do not work if mixed content is enabled from app settings

#### Linux
 - YouTube videos do not work if mixed content is enabled from app settings
 - [Ubuntu - 64 bit] Right clicking taskbar icon and choosing **Quit** only minimizes the app
 - [Ubuntu - 64 bit] [Direct message notification comes as a streak of line instead of a pop up](https://github.com/mattermost/platform/issues/3589)

### Contributors

Many thanks to all our contributors. In alphabetical order:

- [akashnimare](https://github.com/akashnimare), [asaadmahmood](https://github.com/asaadmahmood), [jasonblais](https://github.com/jasonblais), [jgis](https://github.com/jgis), [jnugh](https://github.com/jnugh), [Razzeee](https://github.com/Razzeee), [St-Ex](https://github.com/St-Ex), [timroes](https://github.com/timroes), [yuya-oc](https://github.com/yuya-oc)

## Release v1.3.0

Release date: 2016-07-18

[Download the latest version here](https://about.mattermost.com/downloads/).

### Improvements

#### Windows
- Added an installer for better install experience.
- The app now minimizes to the system tray when application window is closed.
- Added an option to launch application on login.
- Added an option to blink the taskbar icon when a new message has arrived.
- Added tooltip text for the system tray icon in order to show count of unread channels/mentions.
- Added an option to toggle the app to minimize/restore when clicking on the system tray icon.
- Added auto-reloading when tab fails to load the team.
- Added the ability to access all of your teams by right clicking the system tray icon.

#### OS X
- Added colored badges to the menu icon when there are unread channels/mentions.
- Added an option to minimize the app to the system tray when application window is closed.
- Added auto-reloading when tab fails to load the team.
- Added the ability to access all of your teams by right clicking the system tray icon.

#### Linux (Beta)
- Added an option to show the icon on menu bar (requires libappindicator1 on Ubuntu).
- Added an option to launch application on login.
- Added an option to minimize the app to the system tray when application window is closed.
- Added auto-reloading when tab fails to load the team.
- Added the ability to access all of your teams by right clicking the system tray icon.

#### Menu Bar
- New Keyboard Shortcuts
  - Adjust text size
    - Ctrl+0 (Menu Bar -> View -> Actual Size): Reset the zoom level.
    - Ctrl+Plus (Menu Bar -> View -> Zoom In): Increase text size
    - Ctrl+Minus (Menu Bar -> View -> Zoom Out): Decrease text size
  - Control window
    - Ctrl+W (Menu Bar -> Window -> Close): On Linux, this minimizes the main window.
    - Ctrl+M (Menu Bar -> Window -> Minimize)
  - Switch teams (these shotcuts also reopen the main window)
    - Ctrl+{1-9} (Menu Bar -> Window -> *Team name*): Open the *n*-th tab.
    - Ctrl+Tab or Alt+Command+Right (Menu Bar -> Window -> Select Next Team): Switch to the next window.
    - Ctrl+Shift+Tab or Alt+Command+Left (Menu Bar -> Window -> Select Previous Team): Switch to the previous window.
    - Right click on the tray item, to see an overview of all your teams. You can also select one and jump right into it.
- Added **Help** to the Menu Bar, which includes
    - Link to [**Mattermost Docs**](https://docs.mattermost.com/)
    - Field to indicate the application version number.

#### Settings Page
- Added a "+" button next to the **Teams** label, which allows you to add more teams.
- Added the ability to edit team information by clicking on the pencil icon to the right of the team name.

### Other Changes
- Application license changed from MIT License to Apache License, Version 2.0.

### Bug Fixes

#### All platforms
- Fixed authentication dialog not working for proxy.

#### Windows
- Fixed the blurred system tray icon.
- Fixed a redundant description appearing in the pinned start menu on Windows 7.

#### OS X
- Fixed two icons appearing on a notification.

### Known Issues

#### Linux
- [Ubuntu - 64 bit] Right clicking taskbar icon and choosing **Quit** only minimizes the app
- [Ubuntu - 64 bit] [Direct message notification comes as a streak of line instead of a pop up](https://github.com/mattermost/platform/issues/3589)

### Contributors

Many thanks to all our contributors. In alphabetical order:

- [CarmDam](https://github.com/CarmDam), [it33](https://github.com/it33), [jasonblais](https://github.com/jasonblais), [jnugh](https://github.com/jnugh), [magicmonty](https://github.com/magicmonty), [MetalCar](https://github.com/MetalCar), [Razzeee](https://github.com/Razzeee), [yuya-oc](https://github.com/yuya-oc)

## Release v1.2.1 (Beta)

Release date: 2016-05-24

This release contains a security update and it is highly recommended that users upgrade to this version.

 - v1.2.1, released 2016-05-24
     - Fixed an issue where "Electron" appeared in the title bar on startup.
     - Added a dialog to confirm use of non-http(s) protocols prior to opening links. For example, clicking on a link to `file://test` will open a dialog to confirm the user intended to open a file.
     - (Windows and OS X) Added a right-click menu option for tray icon to open the Desktop application.
 - v1.2.0, released 2016-05-13
     - Original v1.2 release

### Improvements

#### Windows
- Improved the style for tab badges.
- Added **Allow mixed content** option to render images with `http://`.
- Added the login dialog for `http` authentication.

#### OS X
- Improved the style for tab badges.
- Added **Allow mixed content** option to render images with `http://`.
- Added the login dialog for `http` authentication.
- Added an option to show a black dot indicating unread messages on the team tab bar.

#### Linux
- Improved the style for tab badges.
- Added an **Allow mixed content** option to render images with `http://`.
- Added a login dialog for `http` authentication.
- Added **.deb** packages to support installation.

### Bug Fixes

#### Windows
- Node.js environment is enabled in the new window.
- The link other than `http://` and `https://` is opened by clicking.

#### OS X
- Node.js environment is enabled in the new window.
- The link other than `http://` and `https://` is opened by clicking.

#### Linux
- Node.js environment is enabled in the new window.
- The link other than `http://` and `https://` is opened by clicking.
- Desktop notification is shown as a dialog on Ubuntu 16.04.

### Known issues
- The shortcuts can't switch teams twice in a row.
- The team pages are not correctly rendered until the window is resized when the zoom level is changed.

### Contributors

Many thanks to all our contributors. In alphabetical order:
 
- [asaadmahmoodspin](https://github.com/asaadmahmoodspin), [jeremycook](https://github.com/jeremycook), [jnugh](https://github.com/jnugh), [jwilander](https://github.com/jwilander), [mgielda](https://github.com/mgielda), [lloeki](https://github.com/lloeki), [yuya-oc](https://github.com/yuya-oc)

## Release v1.1.1 (Beta)

Release date: 2016-04-13

This release contains a security update and it is highly recommended that users upgrade to this version.

 - v1.1.1, released 2016-04-13
     - If the specified team URL on the **Settings** page contains an additional space, the app now properly redirects to the team page
     - `Alt+Shift` now opens the menu on Cinnamon desktop environment.
 - v1.1.0, released 2016-03-30
     - Original v1.1 release

The `electron-mattermost` project is now the official desktop application for the Mattermost open source project.

### Changes

#### All platforms

- Rename project from `electron-mattermost` to  `desktop`
- Rename the executable file from `electron-mattermost` to `Mattermost`
  - The configuration directory is also different from previous versions.
  - Should execute following command to take over `config.json`.
    - Windows: `mkdir %APPDATA%\Mattermost & copy %APPDATA%\electron-mattermost\config.json %APPDATA%\Mattermost\config.json`
    - OS X: `ditto ~/Library/Application\ Support/electron-mattermost/config.json ~/Library/Application\ Support/Mattermost/config.json`
    - Linux: `mkdir -p ~/.config/Mattermost && cp ~/.config/electron-mattermost/config.json ~/.config/Mattermost/config.json`

### Improvements

#### All platforms
- Refined the application icon.
- Show error messages when the application fails to load the Mattermost server.
- Show confirmation dialog to continue connection when there is a certificate error.
- Added validation to check whether **Name** or **URL** are blank when adding or editing a team on the **Settings** page.
- Added simple basic HTTP authentication (requires a command line).

#### Windows
- Show a small circle on the tray icon when there are new messages.

### Bug Fixes

#### Windows
- **File** > **About** now shows the version number dialog.

#### Linux
- **File** > **About** now shows the version number dialog.
- Ubuntu: Notifications now work properly.
- The view mp longer crashes when freetype 2.6.3 is used on the system.

### Known issues

#### All platforms
- Basic authentication is not working and requires a command line.
- Some keyboard shortcuts are missing (e.g. <kbd>Ctrl+W</kbd>, <kbd>Command+,</kbd>).

#### Windows
- Application does not appear properly in Windows volume mixer.

**List of releases before the project was promoted as the official desktop application for Mattermost.**

[Release v1.0.7 (Unofficial) - 2016-02-20](https://github.com/mattermost/desktop/releases/tag/v1.0.7)

[Release v1.0.6 (Unofficial) - 2016-02-16](https://github.com/mattermost/desktop/releases/tag/v1.0.6)

[Release v1.0.5 (Unofficial) - 2016-02-13](https://github.com/mattermost/desktop/releases/tag/v1.0.5)

[Release v1.0.4 (Unofficial) - 2016-02-12](https://github.com/mattermost/desktop/releases/tag/v1.0.4)

[Release v1.0.3 (Unofficial) - 2016-02-03](https://github.com/mattermost/desktop/releases/tag/v1.0.3)

[Release v1.0.2 (Unofficial) - 2016-01-16](https://github.com/mattermost/desktop/releases/tag/v1.0.2)

[Release v1.0.1 (Unofficial) - 2016-01-06](https://github.com/mattermost/desktop/releases/tag/v1.0.1)

[Release v1.0.0 (Unofficial) - 2015-12-27](https://github.com/mattermost/desktop/releases/tag/v1.0.0)

[Release v0.5.1 (Unofficial) - 2015-12-12](https://github.com/mattermost/desktop/releases/tag/v0.5.1)

[Release v0.5.0 (Unofficial) - 2015-12-06](https://github.com/mattermost/desktop/releases/tag/v0.5.0)

[Release v0.4.0 (Unofficial) - 2015-11-03](https://github.com/mattermost/desktop/releases/tag/v0.4.0)

[Release v0.3.0 (Unofficial) - 2015-10-24](https://github.com/mattermost/desktop/releases/tag/v0.3.0)

[Release v0.2.0 (Unofficial) - 2015-10-14](https://github.com/mattermost/desktop/releases/tag/v0.2.0)

[Release v0.1.0 (Unofficial) - 2015-10-10](https://github.com/mattermost/desktop/releases/tag/v0.1.0)
