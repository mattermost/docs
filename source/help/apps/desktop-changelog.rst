Desktop Application Changelog
========================================

Release v4.1.2
----------------------------

This release contains a bug fix for all platforms.

- **Release date:** May 25, 2018
- **Download Binary:** `Windows 32-bit <https://releases.mattermost.com/desktop/4.1.2/mattermost-setup-4.1.2-win32.exe>`_ | `Windows 64-bit <https://releases.mattermost.com/desktop/4.1.2/mattermost-setup-4.1.2-win64.exe>`_ | `Mac <https://releases.mattermost.com/desktop/4.1.2/mattermost-desktop-4.1.2-mac.zip>`_ | `Linux 64-bit <https://releases.mattermost.com/desktop/4.1.2/mattermost-desktop-4.1.2-linux-x64.tar.gz>`_ 
- **View Source Code:** `Mattermost Desktop on GitHub <https://github.com/mattermost/desktop/tree/v4.1.2>`_

Bug Fixes
~~~~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

- Fixed an issue where the popup dialog to authenticate a user to their proxy or server didn't work.

Release v4.1.1
----------------------------

This release contains multiple bug fixes for Mac due to an incorrect build for v4.1.0. Windows and Linux apps are not affected.

- **Release date:** May 17, 2018
- **Download Binary:** `Windows 32-bit <https://releases.mattermost.com/desktop/4.1.1/mattermost-setup-4.1.1-win32.exe>`_ | `Windows 64-bit <https://releases.mattermost.com/desktop/4.1.1/mattermost-setup-4.1.1-win64.exe>`_ | `Mac <https://releases.mattermost.com/desktop/4.1.1/mattermost-desktop-4.1.1-mac.zip>`_ | `Linux 64-bit <https://releases.mattermost.com/desktop/4.1.1/mattermost-desktop-4.1.1-linux-x64.tar.gz>`_ 
- **View Source Code:** `Mattermost Desktop on GitHub <https://github.com/mattermost/desktop/tree/v4.1.1>`_

Bug Fixes
~~~~~~~~~~~~~~~

Each of the issues listed below are already fixed for Windows and Linux v4.1.0.

Mac
^^^^^^^^^^^^^

- Fixed an issue where right-clicking an image, then choosing "Save Image", did nothing.
- Fixed an issue that prevented typing in the form fields on the add server dialog when launched from the server tab bar.
- Fixed an issue that could cause an error message on the add new server dialog to be misleading.
- Fixed an issue where timestamps in message view showed no URL on hover.
- Fixed an issue where quitting and reopening the app required the user to log back in to Mattermost.
- Fixed an issue where adding a new server sometimes caused a blank page.
- Fixed deep linking via ``mattermost://`` protocol spawning a new copy of the Desktop App on the taskbar.
 
Release v4.1.0
--------------

Release date: May 16, 2018

Improvements
~~~~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

- Improved stability and performance
  - Reduced memory usage by periodically clearing cache.
  - Fixed app crashing when a server tab was drag-and-dropped to the message view.
  - Added an option to disable GPU hardware acceleration in App Settings to improve stability in some systems.
  - Fixed Windows crash issues during installation.
  - Fixed Mac and Linux crashing after toggling "Show Mattermost icon in menu bar" app setting.
- Updated design for loading animation icon.
- Improved appearance of server tabs.
- Enabled `Certificate Transparency <https://www.certificate-transparency.org/what-is-ct>`_ verification in HTTPS.

Windows
^^^^^^^^^^^^^

- [Windows 7/8] Desktop notifications now respect the duration setting set in the Control Panel.

Architectural Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Major version upgrade of Electron from v1.7.13 to v1.8.4. Electron is the underlying technology used to build the Desktop apps.
- Mac download files now use Zip packages rather than tar.gz files.
- ES6 ``import`` and ``export`` now replace the ``require`` and ``modul.export`` modules for better development.
- Storybook added to more easily develop React componets without executing the desktop app.

Bug Fixes
~~~~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

- Fixed an issue where an incorrect spellchecker language was used for non ``en-US`` locales on initial installation.
- Fixed an issue where error page appeared when U2F device was used for multi-factor authentication through single sign-on.
- Fixed an issue where right-clicking an image, then choosing "Save Image", did nothing.
- Fixed an issue that prevented typing in the form fields on the add server dialog when launched from the server tab bar.
- Fixed an issue that could cause an error message on the add new server dialog to be misleading.

Windows
^^^^^^^^^^^^^

- Fixed an issue where ``file://`` protocol was not working. Note that localhost URLs are not yet supported.

Known Issues
~~~~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

- Clicking on a video preview opens another Mattermost window in addition to downloading the file.
- Insecure connection produces hundreds of log messages.

Windows
^^^^^^^^^^^^^

- App window doesn't save "floating" app position.
- [Windows 7] Sometimes app tries to render a page inside the app instead of in a new browser tab when clicking links].
- [Windows 10] Incorrect task name in Windows 10 startup list.
- Mattermost UI sometimes bleeds over a file explorer.
- When auto-starting the desktop app, the application window is included in Windows tab list.

Mac
^^^^^^^^^^^^^

- The application crashes when a file upload dialog is canceled without closing Quick Look.
- When the app auto-starts, app page opens on screen instead of being minimized to Dock.

Linux (Beta)
^^^^^^^^^^^^^

- [Ubuntu - 64 bit] Right clicking taskbar icon and choosing **Quit** only minimizes the app.
- [Ubuntu - 64 bit] Direct message notification sometimes comes as a streak of line instead of a pop up.

Contributors
~~~~~~~~~~~~~~~

Many thanks to all our contributors. In alphabetical order:

- `Autre31415 <https://github.com/Autre31415>`_, `dmeza <https://github.com/dmeza>`_, `hmhealey <https://github.com/hmhealey>`_, `jasonblais <https://github.com/jasonblais>`_, `kethinov <https://github.com/kethinov>`_, `lieut-data <https://github.com/lieut-data>`_, `lip-d <https://github.com/lip-d>`_, `mkraft <https://github.com/mkraft>`_, `yuya-oc <https://github.com/yuya-oc>`_

Release v4.0.1
--------------

Release date: March 28, 2018

This release contains multiple security updates for Windows, Mac and Linux, and it is highly recommended that users upgrade to this version.

Architectural Changes
~~~~~~~~~~~~~~~

- Minor version upgrade of Electron from v1.7.11 to v1.7.13. Electron is the underlying technology used to build the Desktop apps.

Bug Fixes
~~~~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

- Disabled Certificate Transparency verification that produced unnecessary certificate errors.

Release 4.0.0
--------------

Release date: January 29, 2018

This release contains multiple security updates for Windows, Mac and Linux, and it is highly recommended that users upgrade to this version.

Improvements
~~~~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

- Added a dialog to allow the user to reopen the desktop app if it quits unexpectedly.
- Mattermost animation icon is now displayed when loading a page, instead of a blank screen.
- Added a dialog to request permissions to show desktop notifications or to use microphone and video for video calls from untrusted origins.
- The "Saved" indicator now appears for both Server Management and App Options on the Settings page.
- Close button on the Settings page now has a hover effect.
- Added new admin configuration settings for:

   - Disabling server management where the user cannot add or edit the server URL.
   - Setting one or more pre-configured server URLs for the end user.
   - Customizing the link in **Help > Learn More..**.

Windows
^^^^^^^^^^^^^

- Added support for protocol deep linking where the desktop app opens via `mattermost://` link if app is already installed.
- Added the ability to more easily white-label the Mattermost taskbar icon on custom builds.

Mac
^^^^^^^^^^^^^

- Added support for protocol deep linking where the desktop app opens via `mattermost://` link if app is already installed.
- Added `Ctrl+Tab` and `Ctrl+Shift+Tab` shortcuts to switch between server tabs.
- Added the option to bounce the Dock icon when receiving a notification.

Architectural Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Major version upgrade of Electron from v1.6.11 to v1.7.11. Electron is the underlying technology used to build the Desktop apps.
- The app now uses CSS to style the user interface. Styles are also divided into React's inline `style` and CSS.
- Yarn is now used to manage dependencies across Windows, Mac and Linux builds.
- Build is now run automatically before packaging the apps with `npm run package`.
- Removed hardcoded product name references.
- Added an `rm` command to `npm`, which removes all dynamically generated files to make it easy to reset the app between builds and branches.

Bug Fixes
~~~~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

- Fixed the close button of the Settings page not working on first installation.
- Fixed the app publisher referring to Yuya Ochiai instead of Mattermost, Inc.
- Fixed font size not always persisting across app restarts.
- Fixed an automatic reloading of the app when a DNS or network error page is manually reloaded with CTRL/CMD+R.
- Fixed an issue where changing font size caused rendering issues on next restart.
- Fixed an issue where after adding a server on the Settings page, focus remained on the "Add new server" link.
- Fixed an issue where SAML certificate file couldn't be uploaded from the file upload dialog.

Windows
^^^^^^^^^^^^^

- Fixed desktop notifications not working when the window was minimized from an inactive state.
- Fixed the uninstaller not removing all files correctly.

Mac
^^^^^^^^^^^^^

- Fixed an issue where after uploading a file, focus wasn't put back to the text box.
- Fixed a mis-aligned `+` button in the server tab bar.

Linux
^^^^^^^^^^^^^

- Fixed the main window not being minimized when the app is launched via "Start app on Login" option.

Known Issues
~~~~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

- Insecure connection produces hundreds of log messages.

Windows
^^^^^^^^^^^^^

- App window doesn't save "floating" app position.
- Windows 7: Sometimes the app tries to render the page inside the app instead of in a new browser tab when clicking links.
- Windows 10: Incorrect task name in Windows 10 start-up list.

Mac
^^^^^^^^^^^^^

- The application crashes when a file upload dialog is canceled without closing Quick Look.
- When the app auto-starts, app page opens on screen instead of being minimized to Dock.
- You have to click twice when a window is out of focus to have actions performed.

Linux (Beta)
^^^^^^^^^^^^^

- Ubuntu - 64 bit: Right clicking taskbar icon and choosing **Quit** only minimizes the app.
- Ubuntu - 64 bit: Direct message notification sometimes renders as a streak or line instead of a pop up.

Contributors
~~~~~~~~~~~~~~~

Many thanks to all our contributors. In alphabetical order:

 - `csduarte <https://github.com/csduarte>`_, `dmeza <https://github.com/dmeza>`_, `jasonblais <https://github.com/jasonblais>`_, `jarredwitt <https://github.com/jarredwitt>`_, `wvds <https://github.com/wvds>`_, `yuya-oc <https://github.com/yuya-oc>`_

----

Release 3.7.1
--------------

Release date: August 30, 2017

This release contains a security update for Windows, Mac and Linux, and it is highly recommended that users upgrade to this version.

Improvements and Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Windows
^^^^^^^^^^^^^

 - Client no longer freezes intermittently, such as when receiving desktop notifications.
 - [Windows 8.1/10] Added support for running the desktop app across monitors of different DPI.
 - [Windows 7/8] Clicking on a desktop notification now opens the message.

Release 3.7.0
--------------

Release date: May 9th, 2017

Improvements
~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

- Added an inline spell checker for English, French, German, Spanish, and Dutch.
- Removed an obsolete "Display secure content only" option, following an `upgrade of the Electron app to Chrome v56 <https://github.com/electron/electron/commit/2e0780308c7ef2258422efd34c968091d7cd5b65>`_.
- Reset app window position when restoring it off-screen from a minimized state.
- Improved page loading and app view rendering.

Windows
^^^^^^^^^^^^^

- [Windows 7/8] Added support for sound when a desktop notification is received.
- Removed obsolete support for Japanese fonts.
- The application window now respects 125% display resolution.

Bug Fixes
~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

- An extra row is no longer added after switching channels with CTRL/CMD+K shortcut.
- Fixed an issue where an unexpected extra app window opened after clicking a public link of an uploaded file.
- Fixed JavaScript errors when refreshing the page.
- Fixed vertical alignment of the Add Server "+" button in the server tab bar.

Windows
^^^^^^^^^^^^^

- Focus is now set to the next top-level window after closing the main app window.
- Fixed an issue where the app remained in the `"classic" ALT+TAB window switcher <https://www.askvg.com/how-to-get-windows-xp-styled-classic-alttab-screen-in-windows-vista-and-7/>`_ after closing the main app window.

Mac
^^^^^^^^^^^^^

- Fixed an issue where the application was not available on the Dock after a computer reboot.
- Fixed an issue where Quick Look couldn't be closed after opening the file upload dialog.

Linux (Beta)
^^^^^^^^^^^^^

- Fixed an issue where the setting was not saved after changing the tray icon theme.

Known Issues
~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

- `If you click twice on the tab bar, and then attempt to use the "Zoom in/out" to change font size, the app window doesn't render properly <https://github.com/mattermost/desktop/issues/334>`__
- `Holding down CTRL, SHIFT or ALT buttons and clicking a channel opens a new application window <https://github.com/mattermost/desktop/issues/406>`_
- `Unable to upload a SAML certificate file from the file upload dialog <https://github.com/mattermost/desktop/issues/497>`_

Windows
^^^^^^^^^^^^^

- [Windows 7] `Sometimes the app tries to render the page inside the app instead of in a new browser tab when clicking links <https://github.com/mattermost/desktop/issues/369>`_

Mac
^^^^^^^^^^^^^

- `After uploading a file with a keyboard shortcut, focus isn't set back to the message box <https://github.com/mattermost/desktop/issues/341>`_
- The application crashes when a file upload dialog is canceled without closing Quick Look.

Linux (Beta)
^^^^^^^^^^^^^

- [Ubuntu - 64 bit] `Right clicking taskbar icon and choosing **Quit** only minimizes the app <https://github.com/mattermost/desktop/issues/90#issuecomment-233712183>`_
- [Ubuntu - 64 bit] `Direct message notification comes as a streak of line instead of a pop up <https://github.com/mattermost/mattermost-server/issues/3589>`_

Contributors
~~~~~~~~~~~~

Many thanks to all our contributors. In alphabetical order:

- `jasonblais <https://github.com/jasonblais>`_, `jnugh <https://github.com/jnugh>`_, `yuya-oc <https://github.com/yuya-oc>`_

Thanks also to those who reported bugs that benefited the release, in alphabetical order:

- `esethna <https://github.com/esethna>`_ (`#524 <https://github.com/mattermost/desktop/issues/524>`_), `hanzei <https://github.com/hanzei>`_ (`#523 <https://github.com/mattermost/desktop/issues/523>`_)

----

Release 3.6.0
--------------

Release date: February 28, 2017

Upgrading to Mattermost server 3.6 or later is recommended, as new features for the desktop app have been added following the release of the team sidebar.

Improvements
~~~~~~~~~~~~

 - Added support for unread indicators following the release of team sidebar in Mattermost server 3.6
 - Removed a confusing CTRL/CMD+S shortcut for searching within a Mattermost team
 - Added support for SAML OneLogin and Google authentication for Enterprise users
 - Switching to a server from the system tray icon, from "Window" menu bar item, or through CTRL/CMD+{n} shortcut now works while viewing the Settings page
 - Streamlined desktop server management:

   - "Team Management" changed to "Server Management" following the release of team sidebar in Mattermost server 3.6
   - Added a "+" icon to the desktop server tab bar to more easily sign into a new Mattermost server
   - Added an option to sign into another Mattermost server from **File > Sign in to Another Server**
   - Clicking "Add new server" on the Settings page opens a dialog instead of a new row
   - Clicking "Remove" next to a server now requires a confirmation to prevent a user from removing the server by accident
   - Clicking "Edit" next to a server on the Settings page opens a dialog
   - Clicking on a server on the Settings page opens the corresponding server tab

 - Simplified desktop app options:

   - App options now auto-save when changed
   - Added supporting help text for each option
   - Removed "Leave app running in menu bar when application window is closed" setting for Mac, which is not applicable for that platform
   - Removed "Toggle window visibility when clicking on the tray icon" setting for Windows, given the behavior is inconsistent with typical Windows app behavior
   - Removed "Hide menu bar" setting to avoid users not being able to use the menu bar and the Settings page

Bug Fixes
~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

- Mattermost window no longer opens on a display screen that has been disconnected
- Mention badges no longer persist after logging out of a Mattermost server
- After right-clicking an image or a link, the "Copy Link" option no longer moves around when clicking different places afterwards
- Fixed an issue where minimum window size is not set
- Changed target resolution size to 1000x700 to prevent unintended issues on the user interface
- Fixed an issue where the application menu is not updated when the config file is saved in the Settings page
- Fixed login issues with local development environment
- Removed a white screen which was momentarily displayed on startup

Windows
^^^^^^^^^^^^^

- Fixed an issue where an unexpected window appears while installing or uninstalling
- Fixed an issue where the maximized state of the application window was not restored on re-launch if "Start app on Login" setting is enabled

Linux (Beta)
^^^^^^^^^^^^^

- Fixed an issue where tray icon wasn't shown by default even when "Show icon in the notification area" setting is enabled
- Fixed an issue where the maximized state of the application window was not restored on re-launch if "Start app on login" setting is enabled

Known Issues
~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

 - `If you click twice on the tab bar, and then attempt to use the "Zoom in/out" to change font size, the app window doesn't render properly <https://github.com/mattermost/desktop/issues/334>`_
 - `After using CTRL+K, an added row appears in the message box <https://github.com/mattermost/desktop/issues/426>`_
 - `Holding down CTRL, SHIFT or ALT buttons and clicking a channel opens a new application window <https://github.com/mattermost/desktop/issues/406>`_

Windows
^^^^^^^^^^^^^

 - [Windows 7] `Sometimes the app tries to render the page inside the app instead of in a new browser tab when clicking links <https://github.com/mattermost/desktop/issues/369>`_

Mac
^^^^^^^^^^^^^

 - `After uploading a file with a keyboard shortcut, focus isn't set back to the message box <https://github.com/mattermost/desktop/issues/341>`_

Linux (Beta)
^^^^^^^^^^^^^

 - [Ubuntu - 64 bit] `Right clicking taskbar icon and choosing **Quit** only minimizes the app <https://github.com/mattermost/desktop/issues/90#issuecomment-233712183>`_
 - [Ubuntu - 64 bit] `Direct message notification comes as a streak of line instead of a pop up <https://github.com/mattermost/mattermost-server/issues/3589>`_

Contributors
~~~~~~~~~~~~

Many thanks to all our contributors. In alphabetical order:

 - `asaadmahmood <https://github.com/asaadmahmood>`_, `jasonblais <https://github.com/jasonblais>`_, `jnugh <https://github.com/jnugh>`_, `yuya-oc <https://github.com/yuya-oc>`_

----

Release v3.5.0
--------------

Release date: December 14, 2016

Improvements
~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

-  URL address is shown when hovering over links with a mouse
-  Added CTRL+SHIFT+MINUS as a shortcut for decreasing font size (zooming out)
-  Reduce upgrade issues by properly clearing cache when updating the desktop app to a new version (the application cache will be purged whenever the desktop app version changes)
-  When launching the app from the command line interface, unnecessary warning messages are no longer sent if connecting to a trusted https connection without a ``certificate.json`` file

Windows
^^^^^^^

-  Link addresses can now be copied and pasted inside the app

Bug Fixes
~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

-  YouTube previews now work, even if mixed content is allowed
-  Fixed an incorrect cursor mode for "Edit" and "Remove" buttons on the Settings page
-  Fixed an issue where "Zoom in/out" settings did not properly work
-  When disconnected from Mattermost, the "Cannot connect to Mattermost" page is now properly aligned at the top of the window

Windows
^^^^^^^

-  The menu bar option for "Redo" is now properly shown as CTRL+Y

Mac
^^^

-  Fixed an issue where the default download folder was ``Macintosh HD``
-  Removed an unexpected "Show Tab Bar" menu item on macOS 10.12

Linux (Beta)
^^^^^^^^^^^^

-  Fixed an issue where the option "Leave app running in notification area when the window is closed" was never enabled.

Known Issues
~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

-  `If you click twice on the tab bar, and then attempt to use the "Zoom in/out" to change font size, the app window doesn't render properly <https://github.com/mattermost/desktop/issues/334>`__
-  `Direct messages cause notification icons to appear on all team tabs, which don't clear until you click on each team <https://github.com/mattermost/desktop/issues/160>`__
-  `After right-clicking an image or a link, the "Copy Link" option sometimes moves around when clicking different places afterwards <https://github.com/mattermost/desktop/issues/340>`__

Windows
^^^^^^^

-  [Windows 7] `Sometimes the app tries to render clicked linked inside the app, instead of in a new browser tab <https://github.com/mattermost/desktop/issues/369>`_

Mac
^^^

-  `After uploading a file with a keyboard shortcut, focus isn't set back to the message box <https://github.com/mattermost/desktop/issues/341>`__

Linux (Beta)
^^^^^^^^^^^^

-  [Ubuntu - 64 bit] `Right clicking taskbar icon and choosing Quit only minimizes the
   app <https://github.com/mattermost/desktop/issues/90#issuecomment-233712183>`_
-  [Ubuntu - 64 bit] `Direct message notification pop ups do not properly render <https://github.com/mattermost/mattermost-server/issues/3589>`_

Contributors
~~~~~~~~~~~~

Many thanks to all our contributors. In alphabetical order:

-  `itsmartin <https://github.com/itsmartin>`__,
   `jasonblais <https://github.com/jasonblais>`__,
   `jcomack <https://github.com/jcomack>`__,
   `jnugh <https://github.com/jnugh>`__,
   `kytwb <https://github.com/kytwb>`__,
   `magicmonty <https://github.com/magicmonty>`__,
   `Razzeee <https://github.com/Razzeee>`__,
   `yuya-oc <https://github.com/yuya-oc>`__

Thanks also to those who reported bugs that benefited the release, in alphabetical order:

- ellisd (`#383 <https://github.com/mattermost/desktop/issues/383>`_), `it33 <https://github.com/it33>`_ (`#384 <https://github.com/mattermost/desktop/issues/384>`_), `jnugh <https://github.com/jnugh>`_ (`#392 <https://github.com/mattermost/desktop/issues/392>`_), `lfbrock <https://github.com/lfbrock>`_ (`#382 <https://github.com/mattermost/desktop/issues/382>`_), `yuya-oc <https://github.com/yuya-oc>`_ (`#391 <https://github.com/mattermost/desktop/issues/391>`_)

--------------

Release v3.4.1
--------------

Release date: September 30, 2016

This release contains a security update and it is highly recommended that users upgrade to this version.

Version number updated to 3.4 to make numbering consistent with Mattermost server and mobile app releases. This change will not imply monthly releases.

-  v3.4.1, released 2016-09-30

   -  (Mac) Fixed an issue where the app window pops up second to foreground when a new message is received

-  v3.4.0, released 2016-09-22

   -  Original v3.4 release

Improvements
~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

-  Current team and channel name shown in window title bar
-  Team tab is bolded for unread messages and has a red dot with a count of unread mentions
-  Added new shortcuts:

   -  CTRL+S; CMD+S on Mac: sets focus on the Mattermost search box
   -  ALT+Left Arrow; CMD+[ on Mac: go to previous page in history
   -  ALT+Right Arrow; CMD+] on Mac: go to next page in history

-  Upgraded the Settings page user interface
-  The app now tries to reconnect periodically if a page fails to load
-  Added validation for name and URL when adding a new team on the Settings page

Windows
^^^^^^^

-  Added access to the settings menu from the system tray icon
-  Only one instance of the desktop application will now load at a time
-  Added an option to configure whether a red badge is shown on taskbar icon for unread messages

Mac
^^^

-  Added an option to configure whether a red badge is shown on taskbar icon for unread messages

Linux (Beta)
^^^^^^^^^^^^

-  Added an option to flash taskbar icon when a new message is received
-  Added a badge to count mentions on the taskbar icon (for Unity)
-  Added a script, ``create_desktop_file.sh`` to create ``Mattermost.desktop`` desktop entry to help `integrate the application into a desktop environment <https://wiki.archlinux.org/index.php/Desktop_entries>`__ more easily
-  Added access to the settings menu from the system tray icon
-  Only one instance of the desktop application will now load at a time

Bug Fixes
~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

-  Cut, copy and paste are shown in the user interface only when the commands are available
-  Copying link addresses now work properly
-  Saving images by right-clicking the image preview now works
-  Refreshing the app page no longer takes you to the team selection page, but keeps you on the current channel
-  Fixed an issue where the maximized state of the app window was lost in some cases
-  Fixed an issue where shortcuts didn't work when switching applications or tabs in some cases

Windows
^^^^^^^

-  Removed misleading shortcuts from the system tray menu
-  Removed unclear desktop notifications when the application page fails to load
-  Fixed the Mattermost icon for desktop notifications in Windows 10
-  Fixed an issue where application icon at the top left of the window was pixelated
-  Fixed an issue where the application kept focus after closing the app window

Linux (Beta)
^^^^^^^^^^^^

-  Removed misleading shortcuts from the system tray menu
-  Removed unclear desktop notifications when the application page fails to load

Known Issues
~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

-  YouTube videos do not work if mixed content is enabled from app settings

Windows
^^^^^^^

-  Copying a link address and pasting it inside the app doesn't work

Linux (Beta)
^^^^^^^^^^^^

-  [Ubuntu - 64 bit] Right clicking taskbar icon and choosing **Quit** only minimizes the app
-  [Ubuntu - 64 bit] `Direct message notification comes as a streak of line instead of a pop up <https://github.com/mattermost/mattermost-server/issues/3589>`_

Contributors
~~~~~~~~~~~~

Many thanks to all our contributors. In alphabetical order:

-  `akashnimare <https://github.com/akashnimare>`__,
   `asaadmahmood <https://github.com/asaadmahmood>`__,
   `jasonblais <https://github.com/jasonblais>`__,
   `jgis <https://github.com/jgis>`__,
   `jnugh <https://github.com/jnugh>`__,
   `Razzeee <https://github.com/Razzeee>`__,
   `St-Ex <https://github.com/St-Ex>`__,
   `timroes <https://github.com/timroes>`__,
   `yuya-oc <https://github.com/yuya-oc>`__

--------------

Release v1.3.0
--------------

Release date: 2016-07-18

`Download the latest version here <https://about.mattermost.com/downloads/>`__.

Improvements
~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^

-  Added auto-reloading when tab fails to load the team.
-  Added the ability to access all of your teams by right clicking the system tray icon.

Menu Bar
''''''''

-  New Keyboard Shortcuts

   -  Adjust text size

      -  CTRL+0 (Menu Bar -> View -> Actual Size): Reset the zoom level.
      -  CTRL+PLUS (Menu Bar -> View -> Zoom In): Increase text size
      -  CTRL+MINUS (Menu Bar -> View -> Zoom Out): Decrease text size

   -  Control window

      -  CTRL+W (Menu Bar -> Window -> Close): On Linux, this minimizes the main window.
      -  CTRL+M (Menu Bar -> Window -> Minimize)

   -  Switch teams (these shotcuts also reopen the main window)

      -  CTRL+{1-9} (Menu Bar -> Window -> [Team name]): Open the *n*-th tab.
      -  CTRL+TAB or ALT+CMD+Right (Menu Bar -> Window -> Select Next Team): Switch to the next window.
      -  CTRL+SHIFT+TAB or ALT+CMD+Left (Menu Bar -> Window -> Select Previous Team): Switch to the previous window.
      -  Right click on the tray item, to see an overview of all your teams. You can also select one and jump right into it.

   -  Added **Help** to the Menu Bar, which includes

      -  Link to `Mattermost Docs <https://docs.mattermost.com>`__
      -  Field to indicate the application version number.

Settings Page
'''''''''''''

-  Added a "+" button next to the **Teams** label, which allows you to add more teams.
-  Added the ability to edit team information by clicking on the pencil icon to the right of the team name.

Windows
^^^^^^^

-  Added an installer for better install experience.
-  The app now minimizes to the system tray when application window is closed.
-  Added an option to launch application on login.
-  Added an option to blink the taskbar icon when a new message has arrived.
-  Added tooltip text for the system tray icon in order to show count of unread channels/mentions.
-  Added an option to toggle the app to minimize/restore when clicking on the system tray icon.

Mac
^^^

-  Added colored badges to the menu icon when there are unread channels/mentions.
-  Added an option to minimize the app to the system tray when application window is closed.

Linux (Beta)
^^^^^^^^^^^^

-  Added an option to show the icon on menu bar (requires libappindicator1 on Ubuntu).
-  Added an option to launch application on login.
-  Added an option to minimize the app to the system tray when application window is closed.

Other Changes
~~~~~~~~~~~~~

-  Application license changed from MIT License to Apache License, Version 2.0.

Bug Fixes
~~~~~~~~~

All platforms
^^^^^^^^^^^^^

-  Fixed authentication dialog not working for proxy.

Windows
^^^^^^^

-  Fixed the blurred system tray icon.
-  Fixed a redundant description appearing in the pinned start menu on Windows 7.

Mac
^^^

-  Fixed two icons appearing on a notification.

Known Issues
~~~~~~~~~~~~

Linux (Beta)
^^^^^^^^^^^^^

-  [Ubuntu - 64 bit] Right clicking taskbar icon and choosing **Quit** only minimizes the app
-  [Ubuntu - 64 bit] `Direct message notification comes as a streak of line instead of a pop up <https://github.com/mattermost/mattermost-server/issues/3589>`_

Contributors
~~~~~~~~~~~~

Many thanks to all our contributors. In alphabetical order:

-  `CarmDam <https://github.com/CarmDam>`__,
   `it33 <https://github.com/it33>`__,
   `jasonblais <https://github.com/jasonblais>`__,
   `jnugh <https://github.com/jnugh>`__,
   `magicmonty <https://github.com/magicmonty>`__,
   `MetalCar <https://github.com/MetalCar>`__,
   `Razzeee <https://github.com/Razzeee>`__,
   `yuya-oc <https://github.com/yuya-oc>`__

--------------

Release v1.2.1 (Beta)
-----------------------------

Release date: 2016-05-24

This release contains a security update and it is highly recommended that users upgrade to this version.

-  v1.2.1, released 2016-05-24

   -  Fixed an issue where "Electron" appeared in the title bar on startup.
   -  Added a dialog to confirm use of non-http(s) protocols prior to opening links. For example, clicking on a link to ``file://test`` will open a dialog to confirm the user intended to open a file.
   -  (Windows and OS X) Added a right-click menu option for tray icon to open the Desktop application.

-  v1.2.0, released 2016-05-13

   -  Original v1.2 release

Improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Improved the style for tab badges.
-  Added **Allow mixed content** option to render images with ``http://``.
-  Added the login dialog for ``http`` authentication.

Mac
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Added an option to show a black dot indicating unread messages on the team tab bar.

Linux
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Added **.deb** packages to support installation.

Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All Platforms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Node.js environment is enabled in the new window.
-  The link other than ``http://`` and ``https://`` is opened by clicking.

Linux
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Desktop notification is shown as a dialog on Ubuntu 16.04.

Known issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  The shortcuts can't switch teams twice in a row.
-  The team pages are not correctly rendered until the window is resized when the zoom level is changed.

Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many thanks to all our contributors. In alphabetical order:

-  `asaadmahmood <https://github.com/asaadmahmood>`__,
   `jeremycook <https://github.com/jeremycook>`__,
   `jnugh <https://github.com/jnugh>`__,
   `jwilander <https://github.com/jwilander>`__,
   `mgielda <https://github.com/mgielda>`__,
   `lloeki <https://github.com/lloeki>`__,
   `yuya-oc <https://github.com/yuya-oc>`__

Release v1.1.1 (Beta)
-----------------------------

Release date: 2016-04-13

This release contains a security update and it is highly recommended that users upgrade to this version.

-  v1.1.1, released 2016-04-13

   -  If the specified team URL on the **Settings** page contains an additional space, the app now properly redirects to the team page
   -  ALT+SHIFT now opens the menu on Cinnamon desktop environment.

-  v1.1.0, released 2016-03-30

   -  Original v1.1 release

The ``electron-mattermost`` project is now the official desktop application for the Mattermost open source project.

Changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All platforms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Rename project from ``electron-mattermost`` to ``desktop``
-  Rename the executable file from ``electron-mattermost`` to ``Mattermost``
-  The configuration directory is also different from previous versions.
-  Should execute following command to take over ``config.json``.

   -  Windows:
      ``mkdir %APPDATA%\Mattermost & copy %APPDATA%\electron-mattermost\config.json %APPDATA%\Mattermost\config.json``
   -  OS X:
      ``ditto ~/Library/Application\ Support/electron-mattermost/config.json ~/Library/Application\ Support/Mattermost/config.json``
   -  Linux:
      ``mkdir -p ~/.config/Mattermost && cp ~/.config/electron-mattermost/config.json ~/.config/Mattermost/config.json``

Improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All platforms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Refined the application icon.
-  Show error messages when the application fails to load the Mattermost server.
-  Show confirmation dialog to continue connection when there is a certificate error.
-  Added validation to check whether **Name** or **URL** are blank when adding or editing a team on the **Settings** page.
-  Added simple basic HTTP authentication (requires a command line).

Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Show a small circle on the tray icon when there are new messages.

Bug Fixes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  **File** > **About** now shows the version number dialog.

Linux
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  **File** > **About** now shows the version number dialog.
-  Ubuntu: Notifications now work properly.
-  The view mp longer crashes when freetype 2.6.3 is used on the system.

Known issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All platforms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Basic authentication is not working and requires a command line.
-  Some keyboard shortcuts are missing (e.g. CTRL+W, CMD+PLUS).

Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Application does not appear properly in Windows volume mixer.

**List of releases before the project was promoted as the official
desktop application for Mattermost.**

`Release v1.0.7 (Unofficial) -
2016-02-20 <https://github.com/mattermost/desktop/releases/tag/v1.0.7>`__

`Release v1.0.6 (Unofficial) -
2016-02-16 <https://github.com/mattermost/desktop/releases/tag/v1.0.6>`__

`Release v1.0.5 (Unofficial) -
2016-02-13 <https://github.com/mattermost/desktop/releases/tag/v1.0.5>`__

`Release v1.0.4 (Unofficial) -
2016-02-12 <https://github.com/mattermost/desktop/releases/tag/v1.0.4>`__

`Release v1.0.3 (Unofficial) -
2016-02-03 <https://github.com/mattermost/desktop/releases/tag/v1.0.3>`__

`Release v1.0.2 (Unofficial) -
2016-01-16 <https://github.com/mattermost/desktop/releases/tag/v1.0.2>`__

`Release v1.0.1 (Unofficial) -
2016-01-06 <https://github.com/mattermost/desktop/releases/tag/v1.0.1>`__

`Release v1.0.0 (Unofficial) -
2015-12-27 <https://github.com/mattermost/desktop/releases/tag/v1.0.0>`__

`Release v0.5.1 (Unofficial) -
2015-12-12 <https://github.com/mattermost/desktop/releases/tag/v0.5.1>`__

`Release v0.5.0 (Unofficial) -
2015-12-06 <https://github.com/mattermost/desktop/releases/tag/v0.5.0>`__

`Release v0.4.0 (Unofficial) -
2015-11-03 <https://github.com/mattermost/desktop/releases/tag/v0.4.0>`__

`Release v0.3.0 (Unofficial) -
2015-10-24 <https://github.com/mattermost/desktop/releases/tag/v0.3.0>`__

`Release v0.2.0 (Unofficial) -
2015-10-14 <https://github.com/mattermost/desktop/releases/tag/v0.2.0>`__

`Release v0.1.0 (Unofficial) -
2015-10-10 <https://github.com/mattermost/desktop/releases/tag/v0.1.0>`__
