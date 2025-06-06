# Desktop App Changelog

```{include} ../_static/badges/allplans-cloud-selfhosted.md
```

This changelog summarizes updates to Mattermost desktop app releases for [Mattermost](https://mattermost.com).

```{Important}
```{include} common-esr-support.md
```

(release-v5-12)=
## Release v5.12

- **v5.12.1, released 2025-05-31**

  - Fixed an issue where focus was lost when tabbing to an external URL on Windows/Linux [MM-62005](https://mattermost.atlassian.net/browse/MM-62005).
  - Disabled server management in the **Settings** modal when disabled via group policy [MM-64355](https://mattermost.atlassian.net/browse/MM-64355).

- **v5.12.0, released 2025-05-16**

  - Original v5.12.0 release

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/latest)

```{Note}
Mattermost Desktop App v5.12.0 contains a medium severity level security fix. Upgrading is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
```

### Compatibility

- Desktop App is supported on any currently supported [Mattermost server version](https://docs.mattermost.com/about/mattermost-desktop-releases.html#latest-releases).
- Updated Chromium minimum supported version to 134+.

### Improvements

#### All Platforms

- Refreshed the **Settings** modal designs.
- Refreshed all built-in dialogs with new designs. 
- Added a changelog link for when the app auto-updates. 
- Updated the certificate error message. 
- Removed bootstrap and dependencies.

### Architectural Changes

- Major version upgrade of Electron to 35.2.0. Electron is the underlying technology used to build the Desktop App.

### Bug Fixes

#### All Platforms

- Fixed an issue where server loading was blocked on contact with each configured server.

### Open Source Components

- Added ``@floating-ui/react`` to https://github.com/mattermost/desktop.

### Known Issues

- Sometimes the app will not restart after an auto-update. This is normal, and if this occurs the app can be safely launched manually.
- Sometimes during installation you may see this message: ``Warning 1946. Property 'System.AppUserModel.ID' for shortcut 'Mattermost.Ink' could not be set``. This message can be safely ignored.
- Users seeing an endless "Loading..." screen when attempting to log in to the app may need to manually delete their cache directory. For macOS it is located in `/Users/<username>/Library/Containers/Mattermost/Data/Library/Application Support/Mattermost`, for Windows in `Users/<username>/AppData/Roaming/Mattermost` and for Linux in `~/config/Mattermost` (where `~` is the home directory).
- On Linux, a left-click on the Mattermost tray icon doesn't open the app window but opens the tray menu.
- Crashes might be be experienced in some Linux desktop clients due to an upstream bug in the `libnotifyapp` library. A recommended workaround is to disable the Mattermost system tray icon via Desktop Settings.
- On apps using GPO configurations, when adding a second server tab, it's possible to drag and drop tabs, but they'll jump back to the original position when releasing the mouse.

### Contributors

- [devinbinnie](https://github.com/devinbinnie), [j0794](https://github.com/j0794).

(release-v5-11)=
## Release v5.11 (Extended Support Release)

- **v5.11.3, released 2025-05-23**

  - Fixed an issue where focus was lost when tabbing to an external URL on Windows/Linux [MM-62005](https://mattermost.atlassian.net/browse/MM-62005).
  - Fixed an issue where server loading was blocked on contact with each configured server [MM-63899](https://mattermost.atlassian.net/browse/MM-63899).

- **v5.11.2, released 2025-03-12**

  - Fixed an issue where the incompatible server screen showed by default when the server info was not present.

- **v5.11.1, released 2025-03-01**

  - Mattermost Desktop App v5.11.1 contains a high severity level security fix. Upgrading is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Added a server incompatible version screen [MM-63224](https://mattermost.atlassian.net/browse/MM-63224). Users with servers running Mattermost v9.3 and earlier versions are not supported by this upgrade. Mattermost v9.4 or later is required.
  - Fixed an issue where the server drop-down wouldn't render properly on first load [MM-62781](https://mattermost.atlassian.net/browse/MM-62781).
  - Updated the error page with new visuals [MM-62724](https://mattermost.atlassian.net/browse/MM-62724).

- **v5.11.0, released 2025-02-14**

  - Original v5.11.0 release

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/v5.11.3)

```{Note}
Mattermost Desktop App v5.11.0 contains a low severity level security fix. Upgrading is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
```

### Compatibility

- Desktop App is supported on any currently supported [Mattermost server version](https://docs.mattermost.com/about/mattermost-desktop-releases.html#latest-releases).
- Updated Chromium minimum supported version to 132+.

### Improvements

#### Linux

- Modified rpm-digest to utilize sha256 instead of md5 to all for rpm installation on FIPS mode enabled Enterprise Linux systems.

#### All Platforms

- Added two menu items to help users forcibly clear out cache and session data.
- Improved the help options in the **Help** menu.
- Updated the styling of the **Downloads** menu to improve text fitting and to prevent text overlap.
- Refreshed loading and welcome screens.
- Server URLs are now auto-filled when deep-linking into the Desktop App if the server isn't configured.
- Removed legacy code for older unsupported Mattermost servers.
- Calls: while the popout window is open, the widget window's visibility will change so that it is not always on top of other windows.

### Architectural Changes

- Major version upgrade of Electron to 34.0.1. Electron is the underlying technology used to build the Desktop App.

### Bug Fixes

#### macOS

- Fixed an issue where the MAS migration from DMG would always fail, fixed a potential crash case.

#### Windows

- Fixed an issue with per-server permission checks for GPO-configured servers on Windows.
- Fixed an issue where the app could crash loading a thumbnail on Windows.

#### Linux

- Fixed an issue for Linux users where the app could crash when trying to add the first server.

#### All Platforms

- Fixed an issue where autocompleting did not stop while the user was typing `https://`.
- Fixed an issue preventing the screen sharing selection modal to show when the app was focused on a different tab (e.g. Playbooks, Boards).
- Fixed an issue trying to download images using right-click > **Save As...**.
- Fixed an issue where the URL view would trap focus when tabbing over a link.

### Known Issues

- Users with servers running Mattermost v9.3 and earlier versions are not supported by this upgrade. Mattermost v9.4 or later is required.
- Boards is not using the new Desktop API, causing issues in v5.11+ [MM-61745](https://mattermost.atlassian.net/browse/MM-61745). Users of v5.11 will need to upgrade their Boards plugin version to v9.1.0+ avoid the issue.
- Sometimes the app will not restart after an auto-update. This is normal, and if this occurs the app can be safely launched manually.
- Sometimes during installation you may see this message: ``Warning 1946. Property 'System.AppUserModel.ID' for shortcut 'Mattermost.Ink' could not be set``. This message can be safely ignored.
- Users seeing an endless "Loading..." screen when attempting to log in to the app may need to manually delete their cache directory. For macOS it is located in `/Users/<username>/Library/Containers/Mattermost/Data/Library/Application Support/Mattermost`, for Windows in `Users/<username>/AppData/Roaming/Mattermost` and for Linux in `~/config/Mattermost` (where `~` is the home directory).
- On Linux, a left-click on the Mattermost tray icon doesn't open the app window but opens the tray menu.
- Crashes might be be experienced in some Linux desktop clients due to an upstream bug in the `libnotifyapp` library. A recommended workaround is to disable the Mattermost system tray icon via Desktop Settings.
- On apps using GPO configurations, when adding a second server tab, it's possible to drag and drop tabs, but they'll jump back to the original position when releasing the mouse.

### Contributors

- [andr-sokolov](https://github.com/andr-sokolov), [devinbinnie](https://github.com/devinbinnie), [jonathan-dove](https://github.com/jonathan-dove), [pvev](https://github.com/pvev), [s1Sharp](https://github.com/s1Sharp), [streamer45](https://github.com/streamer45).

(release-v5-10)=
## Release v5.10

- **v5.10.2, released 2024-12-17**

  - Fixed an issue where the new MSI installer would not uninstall versions before v5.9 installed via MSI [MM-61994](https://mattermost.atlassian.net/browse/MM-61994).
  - Fixed an issue where the MSI kept auto-update on for per-machine installation [MM-62029](https://mattermost.atlassian.net/browse/MM-62029).
  - Fixed a potential error thrown by the MSI when trying to uninstall the EXE [MM-60416](https://mattermost.atlassian.net/browse/MM-60416).
  - Fixed an issue where minimizing on Linux would cause the window to re-appear immediately [MM-60233](https://mattermost.atlassian.net/browse/MM-60233).
  - Added support for downgrading using the MSI installer [MM-62196](https://mattermost.atlassian.net/browse/MM-62196).
  - Fixed an issue where the application would not focus the browser window when opening an external link [MM-61406](https://mattermost.atlassian.net/browse/MM-61406).
  - Upgraded to Electron v33.2.0.

- **v5.10.1, released 2024-11-20**

  - Fixed an issue where the app would not restore when opened again from cold [MM-61864](https://mattermost.atlassian.net/browse/MM-61864).
  - Fixed an issue where deep linking from cold didn't work on Linux.

- **v5.10.0, released 2024-11-15**

  - Original v5.10.0 release

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/v5.10.2)

```{Note}
Mattermost Desktop App v5.10.0 contains a low severity level security fix. Upgrading is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
```

### Compatibility

- Desktop App is supported on any currently supported [Mattermost server version](https://docs.mattermost.com/about/mattermost-desktop-releases.html#latest-releases).
- Updated Chromium minimum supported version to 130+.

### Improvements

#### Windows

- Started using ``titleBarOverlay`` for Windows instead of the buttons that were baked-in to the app.

#### Linux

- Full screen mode is now disabled on Linux. This decision was made for a number of reasons outlined at https://github.com/mattermost/desktop/pull/3151#issue-2539440389.

#### All Platforms

- Implemented a ``performanceMonitor`` to collect and send anonymous usage data to server dashboards.
- Plugins are now allowed to open ``about:blank`` popup windows using ``window.open()``.
- Added support for plugins to ask for desktop source for screen sharing through the ``desktopAPI.getDesktopSources`` call.
- Added ``Developer Mode`` settings to help debug performance issues.
- Upgraded ``electron-log`` and turned on async logging.

### Architectural Changes

- Major version upgrade of Electron to 33.0.2. Electron is the underlying technology used to build the Desktop App.

### Bug Fixes

#### macOS

- Fixed an issue with resizing the app when the welcome screen was open on macOS, and forced the button to always appear on the welcome screen.

#### Linux

- Fixed a crash in Linux when trying to create a thumbnail from an image.

#### All Platforms

- Fixed a potential crash where the app menu could regenerate when ``currentServerId`` wasn't set.
- Fixed an issue with dark-mode style for download location in settings.
- Fixed an issue where logging out from the Boards/Playbooks tabs and trying to navigate after logging back in would force an unexpected logout.
- Fixed an issue with the Download button being hidden on Windows/Linux.
- Fixed an issue where pre-defined servers couldn't edit permissions, and the dropdown would not show badges.
- Fixed issues with loading the app from cold when deep linking.

### Open Source Components

- Added ``@emotion/react`` to https://github.com/mattermost/desktop.

### Known Issues

- Clicking on links does not put the Desktop app in the background to show the external browser [MM-61406](https://mattermost.atlassian.net/browse/MM-61406).
- Sometimes the app will not restart after an auto-update. This is normal, and if this occurs the app can be safely launched manually.
- Sometimes during installation you may see this message: ``Warning 1946. Property 'System.AppUserModel.ID' for shortcut 'Mattermost.Ink' could not be set``. This message can be safely ignored.
- Users seeing an endless "Loading..." screen when attempting to log in to the app may need to manually delete their cache directory. For macOS it is located in `/Users/<username>/Library/Containers/Mattermost/Data/Library/Application Support/Mattermost`, for Windows in `Users/<username>/AppData/Roaming/Mattermost` and for Linux in `~/config/Mattermost` (where `~` is the home directory).
- On Linux, a left-click on the Mattermost tray icon doesn't open the app window but opens the tray menu.
- Crashes might be be experienced in some Linux desktop clients due to an upstream bug in the `libnotifyapp` library. A recommended workaround is to disable the Mattermost system tray icon via Desktop Settings.
- On apps using GPO configurations, when adding a second server tab, it's possible to drag and drop tabs, but they'll jump back to the original position when releasing the mouse.

### Contributors

- [devinbinnie](https://github.com/devinbinnie), [streamer45](https://github.com/streamer45), [theaino](https://github.com/theaino).

(release-v5-9)=
## Release v5.9 (Extended Support Release)

- **v5.9.2, released 2024-12-17**

  - Fixed an issue where the new MSI installer would not uninstall versions before v5.9 installed via MSI [MM-61994](https://mattermost.atlassian.net/browse/MM-61994).
  - Fixed an issue where the MSI kept auto-update on for per-machine installation [MM-62029](https://mattermost.atlassian.net/browse/MM-62029).
  - Fixed a potential error thrown by the MSI when trying to uninstall the EXE [MM-60416](https://mattermost.atlassian.net/browse/MM-60416).
  - Fixed an issue where minimizing on Linux would cause the window to re-appear immediately [MM-60233](https://mattermost.atlassian.net/browse/MM-60233).
  - Added support for downgrading using the MSI installer [MM-62196](https://mattermost.atlassian.net/browse/MM-62196).

- **v5.9.1, released 2024-11-20**

  - Fixed a crash in Linux when trying to create a thumbnail from an image [MM-60232](https://mattermost.atlassian.net/browse/MM-60232).
  - Fixed an issue with the **Download** button being hidden on Windows/Linux [MM-60605](https://mattermost.atlassian.net/browse/MM-60605).

- **v5.9.0, released 2024-08-16**

  - Original v5.9.0 release

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/v5.9.2)

```{Note}
Mattermost v5.9.0 contains low to medium severity level security fixes. Upgrading is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
```

```{Note}
v5.9.0 is the first Extended Support Release for the Desktop App. See more details in [this documentation](https://docs.mattermost.com/about/release-policy.html#extended-support-releases).
```

### Compatibility

- Desktop App is supported on any currently supported [Mattermost server version](https://docs.mattermost.com/about/mattermost-desktop-releases.html#latest-releases).
- Updated Chromium minimum supported version to 126+.

### Improvements

#### Linux

- Changed the window buttons on the Linux client to use the native ones provided by Electron, removed the frame.

#### All Platforms

- Dropped support for 32-bit Windows and added support for ARM64 (beta).
- Dropped support for the EXE/NSIS installer, shipping only the MSI.
- Added a permissions manager user interface in the **Edit Server** modal, and improved permission checks to be less missable.

### Architectural Changes

- Major version upgrade of Electron to 31.2.1. Electron is the underlying technology used to build the Desktop App.

### Bug Fixes

#### Windows

- Fixed an issue where the window size would get smaller on Windows after a restart if the primary monitor was used and was scaled.
- Fixed an issue where snapping the window on Windows would sometimes cause the inner ``BrowserView`` not to resize.

#### All Platforms

- Fixed an issue where reloading the webapp would not always take the user back to the same URL.
- Fixed an issue with a missing context menu upon right-clicking in the calls popout window.
- Fixed an issue where the window could be rendered off-screen in multi-monitor setups.

### Open Source Components

- Removed ``@aws-sdk/client-s3``, ``@aws-sdk/lib-storage``, ``@electron/rebuild``, ``axios``, ``chai``, ``electron-mocha``, ``mochawesome``, ``nan``, ``node-abi``, ``node-gyp``, ``playwright``, ``ps-node``, ``recursive-readdir`` and ``robotjs`` from https://github.com/mattermost/desktop.

### Known Issues

- Sometimes the app will not restart after an auto-update. This is normal, and if this occurs the app can be safely launched manually.
- Sometimes during installation you may see this message: ``Warning 1946. Property 'System.AppUserModel.ID' for shortcut 'Mattermost.Ink' could not be set``. This message can be safely ignored.
- Users seeing an endless "Loading..." screen when attempting to log in to the app may need to manually delete their cache directory. For macOS it is located in `/Users/<username>/Library/Containers/Mattermost/Data/Library/Application Support/Mattermost`, for Windows in `Users/<username>/AppData/Roaming/Mattermost` and for Linux in `~/config/Mattermost` (where `~` is the home directory).
- On Linux, a left-click on the Mattermost tray icon doesn't open the app window but opens the tray menu.
- Crashes might be be experienced in some Linux desktop clients due to an upstream bug in the `libnotifyapp` library. A recommended workaround is to disable the Mattermost system tray icon via Desktop Settings.
- On apps using GPO configurations, when adding a second server tab, it's possible to drag and drop tabs, but they'll jump back to the original position when releasing the mouse.

### Contributors

- [enzowritescode](https://github.com/enzowritescode), [devinbinnie](https://github.com/devinbinnie), [mvitale1989](https://github.com/mvitale1989), [Rajat-Dabade](https://github.com/Rajat-Dabade), [streamer45](https://github.com/streamer45), [tnir](https://github.com/tnir), [toninis](https://github.com/toninis), [yasserfaraazkhan](https://github.com/yasserfaraazkhan).

(release-v5-8)=
## Release v5.8

- **v5.8.1, released 2024-06-13**

  - Fixed an issue where notifications would not show on macOS in certain cases.
  - Fixed an issue where clicking a notification would clear unreads for the wrong channel.
  - Fixed an issue where scaled monitors in multi-monitor setups may have caused the window to be opened across two screens.
  - Fixed an issue with Do Not Disturb mode on Windows.

- **v5.8.0, released 2024-05-16**

  - Original v5.8.0 release

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/v5.8.1)

```{Note}
Mattermost v5.8.0 contains low to medium severity level security fixes. Upgrading is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
```

### Compatibility

- Desktop App is supported on any currently supported [Mattermost server version](https://docs.mattermost.com/about/mattermost-desktop-releases.html#latest-releases).
- Updated Chromium minimum supported version to 122+.

### Improvements

#### All Platforms

- Moved the **Settings** window into a new modal.
- Disabled the `--inspect` tag.

### Architectural Changes

- Minor version upgrade of Electron to 29.3.0. Electron is the underlying technology used to build the Desktop App.

### Bug Fixes

#### macOS

- Fixed an issue for macOS 13+ users on the Mac App Store build where the OS-level **Do Not Disturb** user status was not respected.
- Fixed the settings window disappearing on macOS when dragged to another monitor.

#### All Platforms

- Fixed an issue where removing a server did not clear mentions.
- Fixed an issue where right-clicking on **Save Image** crashed the app.
- Fixed an issue where typing in the local server followed by a port would trip up the URL validation.
- Fixed an issue where restoring the window from the tray icon could cause a strange state if the window was previously maximized.
- Fixed the permission prompt to **Deny** on closing the dialog.

### Open Source Components

- Added and removed several open source components at https://github.com/mattermost/desktop.

### Known Issues

- Desktop App Windows 10: The taskbar might not flash on receipt of a new message when the setting is enabled [MM-58087](https://mattermost.atlassian.net/browse/MM-58087).
- Users seeing an endless "Loading..." screen when attempting to log in to the app may need to manually delete their cache directory. For macOS it is located in `/Users/<username>/Library/Containers/Mattermost/Data/Library/Application Support/Mattermost`, for Windows in `Users/<username>/AppData/Roaming/Mattermost` and for Linux in `~/config/Mattermost` (where `~` is the home directory).
- On Linux, a left-click on the Mattermost tray icon doesn't open the app window but opens the tray menu.
- Crashes might be be experienced in some Linux desktop clients due to an upstream bug in the `libnotifyapp` library. A recommended workaround is to disable the Mattermost system tray icon via Desktop Settings.
- On apps using GPO configurations, when adding a second server tab, it's possible to drag and drop tabs, but they'll jump back to the original position when releasing the mouse.

### Contributors

- [devinbinnie](https://github.com/devinbinnie), [toninis](https://github.com/toninis), [yasserfaraazkhan](https://github.com/yasserfaraazkhan).

----

(release-v5-7)=
## Release v5.7

**Release Date: March 15, 2024**

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/v5.7.0)

### Compatibility

- Desktop App is supported on any currently supported [Mattermost server version](https://docs.mattermost.com/about/mattermost-desktop-releases.html#latest-releases).
- Updated Chromium minimum supported version to 120+.

### Improvements

#### All Platforms

- Added a new **View > Developer Tools** submenu that contains items to access the developer tools for all desktop created windows.
- Added a new menu item to open the developers tools for the Call widget window.
- Reworked and updated the preload script to use an updated and more robust wep app API.
- Promoted Simplified Chinese language to Beta.

### Architectural Changes

- Major version upgrade of Electron to 28.2.2. Electron is the underlying technology used to build the Desktop App.

### Bug Fixes

#### All Platforms

- Fixed an issue where the user's URL would be cleared after being entered in the **Add Server** modal.
- Fixed an issue where users couldn't add a second server with a similar subpath as the configured server.
- Fixed a potential crash in diagnostics.

### Open Source Components

- Added `@aws-sdk/client-s3`, `@aws-sdk/lib-storage` and `@mattermost/desktop-api`, and removed `aws-sdk` from https://github.com/mattermost/desktop.

### Known Issues

- Error might be experienced when quitting v5.7 desktop app on macOS Ventura [MM-57146](https://mattermost.atlassian.net/browse/MM-57146).
- In the **Settings** modal, the search text in the **Check spelling** dropdown is not visible [MM-57089](https://mattermost.atlassian.net/browse/MM-57089).
- Users seeing an endless "Loading..." screen when attempting to log in to the app may need to manually delete their cache directory. For macOS it is located in `/Users/<username>/Library/Containers/Mattermost/Data/Library/Application Support/Mattermost`, for Windows in `Users/<username>/AppData/Roaming/Mattermost` and for Linux in `~/config/Mattermost` (where `~` is the home directory).
- On Linux, a left-click on the Mattermost tray icon doesn't open the app window but opens the tray menu.
- Crashes might be be experienced in some Linux desktop clients due to an upstream bug in the `libnotifyapp` library. A recommended workaround is to disable the Mattermost system tray icon via Desktop Settings.
- On apps using GPO configurations, when adding a second server tab, it's possible to drag and drop tabs, but they'll jump back to the original position when releasing the mouse.

### Contributors

- [ctlaltdieliet](https://github.com/ctlaltdieliet), [devinbinnie](https://github.com/devinbinnie), [hasancankucuk](https://github.com/hasancankucuk), [streamer45](https://github.com/streamer45), [trivikr](https://github.com/trivikr), [wiebel](https://github.com/wiebel).

----

(release-v5-6)=
## Release v5.6

**Release Date: December 15, 2023**

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/tag/v5.6.0)

### Compatibility

- Desktop App is supported on any currently supported [Mattermost server version](https://docs.mattermost.com/about/mattermost-desktop-releases.html#latest-releases).
- Updated Chromium minimum supported version to 118+.

### Improvements

#### All Platforms

- Added Vietnamese as a new language (Beta).
- Removed `gconf` dependency for Debian/Ubuntu.
- Stopped auto-opening Boards/Playbooks tabs.

### Architectural Changes

- Major version upgrade of Electron to v27.0.2. Electron is the underlying technology used to build the Desktop App.

### Bug Fixes

#### All Platforms

- Fixed an issue where some notifications did not navigate to the channel.
- Set the category for the main menu correctly for installations with Debian package.
- Fixed an issue where servers on a subpath could not grant the `media` permission.
- Fixed an issue where users could not fullscreen embedded videos.
- Fixed a deep linking issue for servers with subpaths.
- Fixed an issue where the "session expired" badge wasn't displayed.

#### macOS

- Fixed an issue where clicking on a link to an unregistered protocol on macOS would cause the app to crash.

### Open Source Components

- Added `electron-extension-installer` and `node-gyp` to https://github.com/mattermost/desktop.

### Known Issues

- Users seeing an endless "Loading..." screen when attempting to log in to the app may need to manually delete their cache directory. For macOS it is located in `/Users/<username>/Library/Containers/Mattermost/Data/Library/Application Support/Mattermost`, for Windows in `Users/<username>/AppData/Roaming/Mattermost` and for Linux in `~/config/Mattermost` (where `~` is the home directory).
- On Linux, a left-click on the Mattermost tray icon doesn't open the app window but opens the tray menu.
- Crashes might be be experienced in some Linux desktop clients due to an upstream bug in the `libnotifyapp` library. A recommended workaround is to disable the Mattermost system tray icon via Desktop Settings.
- On apps using GPO configurations, when adding a second server tab, it's possible to drag and drop tabs, but they'll jump back to the original position when releasing the mouse.

### Contributors

- [BaumiCoder](https://github.com/BaumiCoder), [ctlaltdieliet](https://github.com/ctlaltdieliet), [devinbinnie](https://github.com/devinbinnie), [larkox](https://github.com/larkox).

----

(release-v5-5)=
## Release v5.5

- **v5.5.1, released 2023-10-03**
  - Mattermost v5.5.1 contains low severity level security fixes. Upgrading is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Upgraded to Electron v26.2.1, which mitigates `CVE-2023-4863` of the third-party library libwebp.
  - Fixed an issue where logging was stuck to `info` level.
  - Fixed an issue where the downloads dropdown would not open on auto-update notification.

- **v5.5.0, released 2023-09-15**

  - Original v5.5.0 release

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/tag/v5.5.1)

```{Note}
Mattermost v5.5.0 contains a medium severity level security fix. Upgrading is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
```

### Compatibility

- Desktop App is supported on any currently supported [Mattermost server version](https://docs.mattermost.com/about/mattermost-desktop-releases.html#latest-releases).
- Updated Chromium minimum supported version to 116+.

### Improvements

#### All Platforms

- Set the minimum window width to 600px.

### Architectural Changes

- Major version upgrade of Electron to v26.1.0. Electron is the underlying technology used to build the Desktop App.

### Bug Fixes

#### All Platforms

- Fixed a crash in diagnostics when the server was unreachable.
- Fixed bad user feedback on the server URL validation when plugins were disabled.
- Fixed an issue where auto-updating the app wouldn't be properly disabled.
- Fixed an issue where changes in the OS dark/light mode did not reflect immediately in the window top bar.

### Known Issues

- Users are unable to login to Desktop app v5.5 on servers with subpaths.
- Users seeing an endless "Loading..." screen when attempting to log in to the app may need to manually delete their cache directory. For macOS it is located in `/Users/<username>/Library/Containers/Mattermost/Data/Library/Application Support/Mattermost`, for Windows in `Users/<username>/AppData/Roaming/Mattermost` and for Linux in `~/config/Mattermost` (where `~` is the home directory).
- On Linux, a left-click on the Mattermost tray icon doesn't open the app window but opens the tray menu.
- Crashes might be be experienced in some Linux desktop clients due to an upstream bug in the `libnotifyapp` library. A recommended workaround is to disable the Mattermost system tray icon via Desktop Settings.
- On apps using GPO configurations, when adding a second server tab, it's possible to drag and drop tabs, but they'll jump back to the original position when releasing the mouse.

### Contributors

- [apollo13](https://github.com/apollo13), [cpoile](https://github.com/cpoile), [devinbinnie](https://github.com/devinbinnie), [Partizann](https://github.com/Partizann).

----

(release-v5-4)=
## Release v5.4

**Release Day: June 19, 2023**

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/tag/v5.4.0)

### Compatibility

- Desktop App is supported on any supported Extended Support Release or a newer Mattermost server version.
- Updated Chromium minimum supported version to 112+.

### Improvements

#### All Platforms

- Improved URL validation and the add/edit server experience.
- Made `ExtraBar` dark when using dark mode.
- Improved the tray icon click behaviour across operating systems.

### Architectural Changes

- Major version upgrade of Electron to v24.3.1. Electron is the underlying technology used to build the Desktop App.

### Bug Fixes

#### All Platforms

- Calls: Fixed duplicate desktop notifications when calls popout was open.
- Fixed an issue where YubiKeys did not work on the MAS build.
- Fixed an issue where servers on subpaths would not properly navigate to external URLs on the same domain.
- Fixed an issue where spellcheck highlighting would persist after text was deleted.
- Fixed an issue for the MAS build where the default downloads directory would be invalid after upgrade.
- Fixed an issue where the default download location did not respect `XDG_DOWNLOAD_DIR` where it was set.
- Fixed an issue where the popup window was not refocused if it already existed.

### Known Issues

- Mattermost is not detected in the **Add Server** screen if the server has plugins disabled [MM-53294](https://mattermost.atlassian.net/browse/MM-53294).
- When running "Run Diagnostics" from the **Help** menu, the app crashes [MM-53295](https://mattermost.atlassian.net/browse/MM-53295).
- Users seeing an endless "Loading..." screen when attempting to log in to the app may need to manually remove their cache directory. For macOS it is located in `/Users/<username>/Library/Containers/Mattermost/Data/Library/Application Support/Mattermost` and for Windows it is located in `Users/<username>/AppData/Roaming/Mattermost`.
- On Linux, a left-click on the Mattermost tray icon doesn't open the app window but opens the tray menu.
- Crashes might be be experienced in some Linux desktop clients due to an upstream bug in the `libnotifyapp` library. A recommended workaround is to disable the Mattermost system tray icon via Desktop Settings.
- On apps using GPO configurations, when adding a second server tab, it's possible to drag and drop tabs, but they'll jump back to the original position when releasing the mouse.

### Contributors

- [cpoile](https://github.com/cpoile), [devinbinnie](https://github.com/devinbinnie), [jnsgruk](https://github.com/jnsgruk), [streamer45](https://github.com/streamer45), [zoltan-ofir](https://github.com/zoltan-ofir).

----

(release-v5-3)=
## Release v5.3

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/tag/v5.3.1)

- **v5.3.1, released 2023-04-04**

  - Calls: fixed an issue where, after opening the calls popout then closing it (without leaving the call), subsequent clicks would cause a crash.

- **v5.3.0, released 2023-03-30**

  - Original v5.3.0 release

```{Note}
Mattermost v5.3.0 contains a medium severity level security fix. Upgrading is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
```

### Compatibility

- Desktop App is supported on any supported Extended Support Release or a newer Mattermost server version.
- Support for Windows v8 and v8.1 have been dropped. Minimum supported Windows version was updated to 10+.
- Updated Chromium minimum supported version to 110+.

### Highlights

- Added application diagnostics.
- Implemented a global calls widget window.

### Improvements

#### All Platforms

- Added support for starting a call from an existing thread through the `/call start` slash command.
- Added support for Gnome's "do-not-disturb" status.
- Added a menu item for showing the logs folder.
- Improved performance by reducing the number of calls for URL detection.
- Changed the tray behavior on left-click. Left-clicking on the system tray Mattermost icon now hides the application to system tray if it's already visible.
- Defaulted to opening a file when it's selected from the download list.

### Architectural Changes

- Major version upgrade of Electron to v23.1.2. Electron is the underlying technology used to build the Desktop App.

### Bug Fixes

#### All Platforms

- Fixed an issue where a user could open a blank Electron window using the main window.
- Fixed an issue where image thumbnails did not always display in the downloads for MAS builds.
- Fixed an issue where the Boards/Playbooks tabs sometimes didn't appear automatically when a server was added.
- Fixed an issue where RPM conflicted with other Electron-based applications.
- Fixed an issue where a custom certificate wasn't applied to the WebSocket connection along with the HTTP connection.
- Fixed an issue where opening the app with a deeplink could cause the app not to redirect to the correct URL.
- Fixed an issue with closing the Downloads drop-down menu when selecting **Show in folder**.
- Fixed an issue with maximizing the main window when a monitor is removed.
- Fixed an issue where special characters in the server name caused the top bar of the Desktop App to disappear.
- Fixed an issue where OneLogin users wouldn't have their credentials remembered.
- Fixed an issue with plugin navigation displaying a white empty bar between the plugin UI and the Desktop Apps Bar.

### Known Issues

- Users seeing an endless "Loading..." screen when attempting to log in to the app may need to manually remove their cache directory. For macOS it is located in `/Users/<username>/Library/Containers/Mattermost/Data/Library/Application Support/Mattermost` and for Windows it is located in `Users/<username>/AppData/Roaming/Mattermost`.
- On Linux, a left-click on the Mattermost tray icon doesn't open the app window but opens the tray menu.
- Crashes might be be experienced in some Linux desktop clients due to an upstream bug in the `libnotifyapp` library. A recommended workaround is to disable the Mattermost system tray icon via Desktop Settings.
- On apps using GPO configurations, when adding a second server tab, it's possible to drag and drop tabs, but they'll jump back to the original position when releasing the mouse.

### Contributors

- [cpoile](https://github.com/cpoile), [cs4p](https://github.com/cs4p), [devinbinnie](https://github.com/devinbinnie), [JtheBAB](https://github.com/JtheBAB), [kevfocke](https://github.com/kevfocke), [kyeongsoosoo](https://github.com/kyeongsoosoo), [m1lt0n](https://github.com/m1lt0n), [streamer45](https://github.com/streamer45), [tboul shootis](https://github.com/tboulis).

----

(release-v5-2)=
## Release v5.2

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/tag/v5.2.2)

- **v5.2.2, released 2022-12-06**

  - Added ARM64 build (beta) for Windows/Linux.
  - Fixed an issue on Windows installers where the onboarding screen was displayed even when there was a preconfigured server list [MM-48079](https://mattermost.atlassian.net/browse/MM-48079).
  - Fixed an issue where a crash could occur when a download list included corrupt data [MM-48483](https://mattermost.atlassian.net/browse/MM-48483).
  - Fixed an issue where `AppImageLauncher` still created a bad shortcut that caused the app not to launch [MM-48557](https://mattermost.atlassian.net/browse/MM-48557).
  - Fixed an issue where notifications were not displayed on Windows v8 and v8.1 [MM-48397](https://mattermost.atlassian.net/browse/MM-48397).
  - Fixed an issue where users could get stuck after finished the Getting Started flow [MM-48682](https://mattermost.atlassian.net/browse/MM-48682).
  - Fixed an issue where the window resize did not work on some Windows machines [MM-48574](https://mattermost.atlassian.net/browse/MM-48574).
  - Fixed an issue on Windows where the three-dot menu remained focused after clicking elsewhere [MM-46424](https://mattermost.atlassian.net/browse/MM-46424).

- **v5.2.1, released 2022-11-15**

  - Fixed an issue on `.exe` installers where the onboarding screen was still displayed even when there was a preconfigured server list [MM-48079](https://mattermost.atlassian.net/browse/MM-48079).
  - Fixed an issue where the default downloads location was not set on macOS [MM-48167](https://mattermost.atlassian.net/browse/MM-48167).
  - Fixed an issue where users were able to edit or remove a pre-configured server provided by GPO on Windows [MM-48184](https://mattermost.atlassian.net/browse/MM-48184).
  - Fixed an issue where the tray icon colour on Windows didn't obey the setting [MM-48080](https://mattermost.atlassian.net/browse/MM-48080).

- **v5.2.0, released 2022-10-31**

  - Original v5.2.0 release

### Compatibility

- Desktop App is supported on any supported Extended Support Release up to v8.1 ESR.
- Desktop App v5.2 is incompatible with server versions v9.1 and later.

### Highlights

- Onboarding screen improvements: Added new **Configure Server** and first user onboarding screens when starting the app without servers configured.
- Added a Downloads dropdown menu that displays file upload progress and recently downloaded files.

### Improvements

#### Linux

- Dropped support for Linux IA32 (Linux 32-bit builds).

#### All Platforms

- The Desktop App configured URL is now forced to be changed to the SiteURL configured by the system adminstrator.
- Added localization support to the Desktop App (Beta).
- Zoom in/out now works when `CTRL/CMD+SHIFT+=` is pressed.
- Changed the order of fields in the Add Server modal so that the server URL is filled in first and the display name after.
- The app window now reloads only when the URL changes, not when a server's name changes.
- Updated the default window size to 1280x800, so that users can now see other login options as well on first load.
- Swapped the dark and light theme tray icons on Linux and Windows to the expected behavior.
- Disabled the auto-update functionality explicitly for all MSI installers except the Windows EXE installer and the Linux AppImage.
- Dropped support for asterisk-based unreads in Mattermost Self-Hosted versions older than v5.28.
- Improved the performance of window resizing.

### Architectural Changes

- Major version upgrade of Electron to v21.2.0. Electron is the underlying technology used to build the Desktop App.

### Bug Fixes

#### Linux

- To fix notification issues for Linux users, the configuration setting `notifications.flashWindow` default value was changed to `0` for Linux.

#### All Platforms

- Fixed an issue where an Operating System could register Mattermost as the default web browser / mail app.
- Fixed an issue where the download notification showed the wrong file name.
- Fixed an issue where it was possible to drag the Minimize/Close buttons.
- Fixed an issue where a misleading error message from a remote certificate would imply that the Mattermost server had an issue.
- Fixed an issue where users still received notifications when their status was set to **Do Not Disturb**.
- Fixed an issue where users could not replace files in the **Downloads** folder.
- Fixed improper reporting of app version when the `--version` or `-v` command-line flags were passed.
- Fixed an issue where MAS users couldn't easily replace files.

### Open Source Components

- Added `macos-notification-state`, `windows-focus-assist`, and `react-intl` to https://github.com/mattermost/desktop.

### Known Issues

- Users seeing an endless "Loading..." screen when attempting to log in to the app may need to manually remove their cache directory. For macOS it is located in `/Users/<username>/Library/Containers/Mattermost/Data/Library/Application Support/Mattermost` and for Windows it is located in `Users/<username>/AppData/Roaming/Mattermost`.
- On Linux, a left click on the tray icon doesn't open the app window but opens the tray menu.
- Crashes might be be experienced in some Linux desktop clients. This is an upstream bug in the `libnotifyapp` library. A recommended workaround is to disable the system tray icon in the Desktop settings.
- On apps using GPO configurations, when adding a second server tab, it's possible to drag and drop tabs, but they'll jump back to the original position when releasing the mouse.

### Contributors

- [devinbinnie](https://github.com/devinbinnie), [julmondragon](https://github.com/julmondragon), [m1lt0n](https://github.com/m1lt0n), [saturninoabril](https://github.com/saturninoabril), [tboulis](https://github.com/tboulis), [vaaas](https://github.com/vaaas).

----

(release-v5-1)=
## Release v5.1

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/tag/v5.1.1)

- **v5.1.1, released 2022-06-27**

  - Upgraded to Electron v18.3.0.
  - Fixed an issue where a channel name matching the server subpath would not be navigable.
  - Fixed an issue where the `hideOnStart` setting didn't work.
  - Fixed an issue where the certificate error dialog box would reappear infinitely.
  - Fixed an issue where the first client certificate could not be selected.
  - Restored Windows ZIP builds.

- **v5.1.0, released 2022-05-16**

  - Original v5.1.0 release

```{Note}
Mattermost v5.1.0 contains a low severity level security fix. Upgrading is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
```

### Compatibility

- Desktop App is supported on any supported Extended Support Release up to v8.1 ESR.
- Desktop App v5.1 is incompatible with server versions v9.1 and later.

### Highlights

- Added [a Desktop App auto-updater](https://docs.mattermost.com/collaborate/install-desktop-app.html). The app now automatically checks for new updates on app start up. Note that the Mac builds provided on GitHub do not support auto-updates.

### Improvements

#### macOS

- Mattermost can now be installed on the [Mac App Store](https://apps.apple.com/us/app/mattermost-desktop/id1614666244?mt=12). Even if you’re already using Mattermost desktop on Mac, you can download and install it via the Mac App Store to access future automatic updates.

#### Linux

- Updated the Linux closing behaviour to allow the app to close complely when pressing `X`.
- Changed the default setting for **Leave app running in notification area when application window is closed** on Linux to `false` by default.

#### All Platforms

- Added the ability in Calls to select which window to share when screensharing.
- Added a new config setting "Launch app minimized" to be able to auto-launch the app minimized when the application is launched on startup.
- When the **Add Server** modal pops up for the first time when the app is launched, the modal now stays open instead of closes on mouse click until the first server has been added.
- Added a new setting/preference to always open the Desktop App in full screen.
- The app now uses `ctrl+=` and `cmd+=` to zoom in to match the behavior of Chrome and Firefox.
- Changed the wording in the **File > View** menu from `Tab` to `Server` to reflect recent changes in the user interface.
- Added the ability to copy the version string into clipboard from **Menu > Help > Version**.
- Added a menu item **Window > Show Servers** to show a list of servers.
- Removed the reference to the flashing window on the Settings page to avoid confusion when the window doesn't flash.

### Architectural Changes

- Major version upgrade of Electron to v18.0.3. Electron is the underlying technology used to build the Desktop app.

### Bug Fixes

#### Linux

- Fixed an issue where the app window and taskbar did not flash when notifications were received.

#### All Platforms

- Fixed an issue where customized URIs were not supported on the desktop app.
- Fixed an issue where parsed, but technically invalid URIs could not be opened in the browser.
- Fixed an issue where a channel name with an asterisk at the front would cause unreads to return a false positive.
- Fixed an issue where opening a new tab view caused the original view to go to the requested link as well.
- Fixed an issue where users could add the same server name or URL twice.
- Fixed an issue where the URL view prevented users from clicking a button directly above it.
- Fixed an issue where the tray icon theme toggle was not hidden when the icon itself wasn't enabled.
- Fixed an issue where a redundant icon was present in Windows 10+ notifications.
- Fixed an issue where unreads on a different team wouldn't trigger an unread badge in the Desktop App.
- Fixed an issue where retrying to load tabs indefinitely instead of stopping after a few tries was not supported.
- Fixed issues with the loading screen to make it more reliable.
- Fixed an issue where `Shift+Alt` moved the focus to the top menu.
- Fixed an issue where external links at the bottom of the page were not clickable.
- Fixed an issue where mentions/unreads did not take precedence when setting the badge/tray icon.
- Fixed an issue where the macOS dock would stay open after clicking the tray icon.
- Fixed an issue where the URL view would persist once the user had moved their mouse off of an external URL.

### Known Issues

- On Linux, a left click on the tray icon doesn't open the app window but opens the tray menu.
- Mattermost Desktop App v5.1.0 cannot be launched twice on Windows servers with the role "Remote Desktop Session Host".
- Desktop App may become unresponsive and crash when initiating a screen reader [MM-44058](https://mattermost.atlassian.net/browse/MM-44058).
- Crashes might be experienced in some Linux desktop clients. This is an upstream bug in the `libnotifyapp` library. A recommended workaround is to disable the system tray icon in the Desktop settings.
- On apps using GPO configurations, when adding a second server tab, it is possible to drag and drop tabs but they will jump back to the original position when releasing the mouse.

### Contributors

- [ChristophKaser](https://github.com/ChristophKaser), [coltoneshaw](https://github.com/coltoneshaw), [devinbinnie](https://github.com/devinbinnie), [JulienTant](https://github.com/JulienTant), [oh6hay](https://github.com/oh6hay), [Profesor08](https://github.com/Profesor08), [shadowshot-x](https://github.com/shadowshot-x), [streamer45](https://github.com/streamer45), [svelle](https://github.com/svelle), [Willyfrog](https://github.com/Willyfrog).

----

(release-v5-0)=
## Release v5.0

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/tag/v5.0.4)

- **v5.0.4, release 2022-02-04**

  - Fixed an issue where Desktop App toast notifications didn't work in v5.0.3.
  - Restored **Minimize to tray** option for Windows, and added the ability to override the tray icon color.

- **v5.0.3, released 2022-02-01**

  - Fixed an issue where a user might get an erroneous "Your session has expired" error and be unable to login.
  - Fixed an issue where the app could crash while trying to reload a page that is currently loading.
  - Fixed an issue where OS-level shortcuts could cause an unexpected focus behavior in the app.
  - Fixed an issue where Linux users might not see the **Add Server** modal.
  - Fixed an issue that prevented the export channel log from being downloaded from Playbooks.

- **v5.0.2, released 2021-11-15**

  - Fixed an issue where the Desktop app crashed intermittently when switching between tabs while a tab was loading.
  - Fixed an issue where the app didn't raise the window from the tray icon when clicking on the taskbar icon.

- **v5.0.1, released 2021-10-22**

  - Fixed issue with desktop notification sounds not working correctly.
  - Fixed an issue where using a proxy server with the Desktop app caused the app to crash.
  - Fixed the new server modal not being accessible on Linux when no other servers existed.
  - Fixed an issue where switching from Boards/Playbooks to Channels caused a reload in the Channels view.
  - Fixed an issue with GPO and built-in servers not working correctly with Boards/Playbooks tabs.
  - Fixed an issue where the top bar buttons on Windows 8 were missing.
  - Reduced the size of some builds by removing unnecessary files.

- **v5.0.0, released 2021-10-13**

 - Original v5.0.0 release

```{Note}
Mattermost v5.0.0 contains a low level security fix. Upgrading is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
```

### Compatibility

- Desktop App is supported on any supported Extended Support Release up to v8.1 ESR.
- Desktop App v5.0 is incompatible with server versions v9.1 and later.

### Breaking Changes / Upgrade Notes

- Some keyboard shortcuts and menu items were updated to work with the new Desktop App layout. `Ctrl+#` is used for changing tabs and `Ctrl+Shft+#` is used for changing servers.

### Highlights

- Redesigned title bar allows users to seamlessly work in Channels, Playbooks, and Boards across multiple servers with minimal context switching.

### Improvements

### macOS

- Made the window menu on macOS more consistent with system standards.

#### All Platforms

- Added support for multiple languages to be used by the spellchecker. This can be configured in the desktop preferences.
- Updated loading screen visuals.
- Added a dark mode for settings and modals.
- Changed the server selection to use a dropdown instead of tabs.
- Added support for dragging and dropping of the server dropdown items to re-order servers.
- Converted the tabs interface to support multiple configurable tabs based on the added server to easily access Boards and Playbooks via tabs in the window header.
- Removed the **Server Management** screen from **Settings**, and added Edit/Delete buttons to the new dropdown, as users can now configure and edit their servers from the server dropdown menu.
- Added a checkbox to certificate error modal that allows users to permanently distrust a certificate.

### Architectural Changes

- Major version upgrade of Electron to v14.1. Electron is the underlying technology used to build the Desktop app.
- Added a RPM build option to the Electron builder.
- Added Universal binaries for macOS users.
- Migrated to Bootstrap v4 and refreshed the interface. Migrated to `react-beautiful-dnd` instead of `react-smooth-dnd` for a cleaner experience.

### Bug Fixes

#### Linux

- Fixed the tray icon size on Linux.
- Fixed an issue where pressing `Alt+<somekey>` could cause the menu bar to disable and overlap the top bar on Linux.

#### All Platforms

- Fixed an issue where resizing the app while in the System Console caused a white bar to appear at the top.
- Fixed an issue where the right-click menu was missing from the `jira connect` modal.
- Fixed an issue where the app would render off screen and the user would have trouble getting the window in view.

### Known Issues

- Unread messages icon may be missing from the taskbar on Windows following 4.7.0 upgrade [MM-37807](https://mattermost.atlassian.net/browse/MM-37807).
- Crashes might be be experienced in some Linux desktop clients. This is an upstream bug in the `libnotifyapp` library. A recommended workaround is to disable the system tray icon in the Desktop settings.
- On some Linux distros, a sandbox setting is preventing apps from opening links in the browser (see https://github.com/electron/electron/issues/17972#issuecomment-486927073). While this is fixed for most installers, it is not on the tgz. In this case manual intervention is required via `$ chmod 4755 <installpath>/chrome-sandbox`.
- Pressing Enter multiple times during Basic Authentication causes a crash.
- On apps using GPO configurations, when adding a second server tab, it is possible to drag and drop tabs but they will jump back to the original position when releasing the mouse.

### Contributors

- [devinbinnie](https://github.com/devinbinnie), [elsiehupp](https://github.com/elsiehupp), [jtwillis92](https://github.com/jtwillis92), [koox00](https://github.com/koox00), [svelle](https://github.com/svelle), [Westacular](https://github.com/Westacular), [Willyfrog](https://github.com/Willyfrog).

----

(release-v4-7)=
## Release v4.7

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/tag/v4.7.2)

- **v4.7.2, released 2021-09-13**

  - Upgraded to Electron v12.0.16.
  - Fixed an issue where the **Add Server** screen appeared on each startup on servers with GPO.
  - Fixed an issue where the window would flash on Windows and Linux when a new mention arrived regardless of the setting to turn it on/off.
  - Added desktop notifications for followed threads.

- **v4.7.1, released 2021-08-03**

- Mattermost v4.7.1 contains a medium level security fix. Upgrading is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
  - Added support to allow users to specify a different download location for Hunspell dictionaries.
  - Fixed an issue where the notification badge did not get cleared when reading a channel with unread messages until navigating away from the channel.
  - Fixed an issue where the top bar menu, and the minimize, maximize and close icons did not work on 4.7.0 on Windows 10 if GPU acceleration was disabled.
  - Reverted to Electron v12.0.1 to fix an issue where clicking in the searchbox to highlight search terms dragged the desktop window.
  - Fixed an issue to prevent a crash on malformed default download locations.

- **v4.7.0, released 2021-06-23**

  - Original v4.7.0 release

```{Note}
Mattermost v4.7.0 contains low to medium level security fixes. Upgrading is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
```

### Compatibility

- Desktop Apps is supported on any supported Extended Support Release or a newer Mattermost server version.

### Highlights

- Added support for Electron BrowserView, an underlying architecture change that improves performance and offers snappier interactions (i.e., less lag), lower CPU usage, and faster launch times.

### Improvements

#### Windows

- Windows desktop now automatically switches between light and dark themes based on the operating system settings.

#### All Platforms

- Added a setting to specify the default desktop app download location.
- Improved the launch screen and loading indicator.
- Restored deeplinking.
- Improved the spell check dictionary to provide more accurate spelling suggestions in more languages. The spell check language is now automatically based on the operating system setting.
- Added improvements to be consistent with the use of URL and URL libraries.
- Ctrl/CMD + F functionality has been replaced with in-channel search (requires Mattermost server v5.36+).
- Updated the Content Security Policy for Desktop App to avoid warnings in the dev tools.
- On Linux and Windows, each settings menu is now in a separate window.
- Shortened the maximum length (width) for server tab names to 224px.
- Updated the menu bar and system tray icons for improved contrast.
- Removed `libappnotify1` as a dependency requirement in Debian installers as it's no longer shipped in Debian's Bullseye. It's still recommended to install where available.

### Architectural Changes

- Major version upgrade of Electron to v12.0.10. Electron is the underlying technology used to build the Desktop app.
- Added support for Electron BrowserView.
- Added support for M1 architecture (beta) in the build pipeline.

### Bug Fixes

#### Windows

- Fixed an issue where Windows desktop notifications did not auto-dismiss when another notification arrived.
- Fixed an issue on Windows where the **Pin to Taskbar** icon got lost during an upgrade.
- Fixed an issue with the MSI build that caused notifications to not open the application and navigate to the correct channel.

#### macOS

- Fixed an issue where changing the theme from the **System Preferences** changed the tray icon, but the red/blue dot indicating unreads got removed.
- Fixed an issue where there was an invisible Mattermost icon in the top menu bar.

#### Linux

- Fixed an issue where Shift+Alt moved the focus to the main menu instead of changing keyboard layout.

#### All Platforms

- Fixed an issue where special characters were not shown for server names using GPO.
- Fixed an issue where the close/back button in permanent link media previews was missing.
- Fixed an issue where the text input focus was lost when closing the **Settings** window.
- Fixed an issue where saving the desktop app settings didn't remove the **saving** indicator in the settings window.
- Fixed an issue where the jewel indicating the number of mentions was not shown in the tab.
- Fixed an issue where the desktop linting didn't match the webapp linting.
- Fixed an issue where clicking on a notification did nothing when the wrong server tab was selected.
- Fixed an issue where users were unable to copy text from desktop **About** window.

### Known Issues

- The new spellchecker connects to Google servers for downloading updated dictionaries.
- Unread messages icon may be missing from the taskbar on Windows following 4.7.0 upgrade [MM-37807](https://mattermost.atlassian.net/browse/MM-37807).
- Clicking on **View > Find** doesn't work [MM-36606](https://mattermost.atlassian.net/browse/MM-36606).
- Right click menu is missing from the `jira connect` modal [MM-36032](https://mattermost.atlassian.net/browse/MM-36032).
- Search field is focused on first start of the app [MM-35249](https://mattermost.atlassian.net/browse/MM-35249).
- The `create_desktop_file.sh` script is removed from the .tar.gz release. As a workaround, it can be downloaded from [GitHub here](https://github.com/mattermost/desktop/blob/master/src/assets/linux/create_desktop_file.sh).
- An error may occur when installing the MSI Installer on any Windows version.
- Crashes might be be experienced in some Linux desktop clients. This is an upstream bug in the `libnotifyapp` library. A recommended workaround is to disable the system tray icon in the Desktop settings.
- On some Linux distros, a sandbox setting is preventing apps from opening links in the browser (see https://github.com/electron/electron/issues/17972#issuecomment-486927073). While this is fixed for most installers, it is not on the tgz. In this case manual intervention is required via `$ chmod 4755 <installpath>/chrome-sandbox`.
- Pressing Enter multiple times during Basic Authentication causes a crash.
- On apps using GPO configurations, when adding a second server tab, it is possible to drag and drop tabs but they will jump back to the original position when releasing the mouse.

### Contributors

- [devinbinnie](https://github.com/devinbinnie), [FalseHonesty](https://github.com/FalseHonesty), [nevyangelova](https://github.com/nevyangelova), [petermcj](https://github.com/petermcj), [wget](https://github.com/wget), [Willyfrog](https://github.com/Willyfrog).

----

(release-v4-6)=
## Release v4.6

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/tag/v4.6.2)

- **v4.6.2, released 2021-01-25**

  - Fixed an issue where logging in to `gitlab.com` did not work on the Desktop App. [MM-31626](https://mattermost.atlassian.net/browse/MM-31626)
  - Fixed an issue where macOS entitlements had not been enabled for using camera and microphone on the Desktop App for third-party plugins such as Jitsi. [MM-31987](https://mattermost.atlassian.net/browse/MM-31987)

- **v4.6.1, released 2020-10-26**

  - Fixed an issue where desktop app notification sounds did not work on Desktop App v4.6.0. [MM-29921](https://mattermost.atlassian.net/browse/MM-29921)

- **v4.6.0, released 2020-10-16**

  - Original v4.6.0 release

### Improvements

#### All Platforms

- Added a setting to be able to select different desktop notification sounds (Requires Mattermost server v5.28+).
- `Show Mattermost icon in the menu bar` setting is now enabled by default for new installs on Mac, and `Show icon in the notification area` and `Leave app running in the notification area when application window is closed` settings are are now enabled by default for new installs on Ubuntu.
- The default window frame and server tabs are now used on older Windows and Linux OS versions.
- Added Russian and Ukrainian language spellcheckers.
- Added support for allowing access to managed resources.
- The same default protocols as in the server are now used in the autolink plugin.

### Bug Fixes

#### All Platforms

- Fixed an issue where the app window started as maximized when the "Start app on login" setting was enabled. The Desktop App no longer shows in the system tray and the parameter `--hidden` was removed. This setting is not respected when AppImage file (Unofficial) is used.
- Fixed an issue where the **Add server** modal fields were missing the right-click menu.
- Fixed an issue where users did not see the right-click menu with Copy and Paste options on the login page when using the desktop app to login to an external application.
- Fixed an issue where the URL bar was shown in the bottom left corner when hovering over a timestamp or internal links.
- Fixed an issue where a Javascript error occurred when a separate OAuth window was open.
- Fixed an issue where users were unable to resize the desktop app vertically from the top tab bar.
- Fixed an issue where some links pointing to the System Console did not work on the desktop app.

### Known Issues

- Unlocking the Desktop App on macOS marks the currently viewed channel as read. [MM-31429](https://mattermost.atlassian.net/browse/MM-31429)
- On Ubuntu, auto-focus is lost when using ALT+TAB to switch between windows. [MM-29705](https://mattermost.atlassian.net/browse/MM-29705)
- Crashes might be be experienced in some Linux desktop clients. This is an upstream bug in the `libnotifyapp` library and a recommended workaround is to disable the system tray icon in the Desktop settings.
- On some Linux distros, a sandbox setting is preventing apps from opening links in the browser (see https://github.com/electron/electron/issues/17972#issuecomment-486927073). While this is fixed for most installers, it is not on the tgz. In this case manual intervention is required via `$ chmod 4755 <installpath>/chrome-sandbox`.
- Pressing Enter multiple times during Basic Authentication causes a crash.
- On apps using GPO configurations, when adding a second server tab, it is possible to drag and drop tabs but they will jump back to the original position when releasing the mouse.

### Contributors

Many thanks to all our contributors. In alphabetical order:

- [devinbinnie](https://github.com/devinbinnie), [dpanic](https://github.com/dpanic), [jekill](https://github.com/jekill), [jupenur](https://github.com/jupenur), [M-ZubairAhmed](https://github.com/M-ZubairAhmed), [nevyangelova](https://github.com/nevyangelova), [rvillablanca](https://github.com/rvillablanca), [wget](https://github.com/wget), [Willyfrog](https://github.com/Willyfrog).

----

(release-v4-5)=
## Release v4.5

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/tag/v4.5.4)

- **v4.5.4, released 2020-09-11**

  - Fixed an issue where Help and Report a Problem website links configured to point to Mattermost channels didn't work. [MM-28595](https://mattermost.atlassian.net/browse/MM-28595)

- **v4.5.3, released 2020-08-25**

  - Fixed an issue where users were unable to log in to the desktop app when users had to select a certificate for authentication that requires a pin even when there was only one option to manage a certificate login. [MM-27331](https://mattermost.atlassian.net/browse/MM-27331)

- **v4.5.2, released 2020-07-20**

  - Fixed an issue on Linux app started as a blank screen when both “Show icon in the notification area" and "Start app on login" were enabled. [MM-26832](https://mattermost.atlassian.net/browse/MM-26832)

- **v4.5.1, released 2020-07-13**

  - Mattermost v4.5.1 contains a high level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

- **v4.5.0, released 2020-06-16**

  - Original v4.5.0 release

### Improvements

#### All Platforms

- Added a spell checker for Polish language. 
- Added support for triggering a desktop notification when a file download is complete.
- Added support for the cursor focus to be on the Server Name field when clicking on the `+` tab to add a new server.
- Defaulted "Flash app window and taskbar icon when a new message is received" setting to `True`.

#### macOS

- On Mac, a closed window now reopens with `CMD+Tab` keyboard shortcut.

### Architectural Changes

- Major version upgrade of Electron to v7.0.0. Electron is the underlying technology used to build the Desktop apps.

### Bug Fixes

#### All Platforms

- Fixed an issue where the Desktop app could not authenticate with SAML with an IdP relay.
- Fixed an issue where a moved server tab did not stay in focus.
- Fixed an issue where right-clicking and then clicking "Save Image" didn't work.
- Fixed an issue where trusting self-signed certificates kept asking for trust.
- Fixed an issue where a link to the root of a server caused a "Channel not Found" error if the URL didn't end with a `/`.
- Fixed an issue where using ESC or Cancel to close the Add Server modal did not return focus to previously selected text input.
- Fixed an issue where OneLogin links opened up in the app itself making it impossible to go back to the app.
- Fixed an issue where links on "Cannot connect to Mattermost" error didn't work.

#### Windows

- Fixed an issue where Windows Desktop notifications were delayed compared to other notification channels.
- Fixed an issue where Windows Desktop Menu option was read as "Unlabel 0 button".
- Fixed an issue where a white bar was present on the right-hand side of the Settings screen when Add Server modal was open.

#### macOS

- Fixed an issue where double clicking the top bar no longer minimized or maximized the window.
- Fixed an issue where users were unable to reposition the app by using click, hold and drag on the left side of the header.
- Fixed an issue where server display name field lost focus when using `CMD+Tab` to navigate away and back to the app.
- Fixed an issue where a long server address didn't wrap correctly in the new server settings page.
- Fixed an issue where copy and pasting into Atlassian login fields pasted text in the wrong place.

### Known Issues

- A visible cursor focus is missing on the login screen directly after adding a new server via "+" to the right of the server tabs. [MM-25984](https://mattermost.atlassian.net/browse/MM-25984)
- Right-click menu is missing on "Add server" modal fields. [MM-26017](https://mattermost.atlassian.net/browse/MM-26017)
- Double notifications are received on Ubuntu for at-mentions. [MM-26012](https://mattermost.atlassian.net/browse/MM-26012)
- The current window frame and server tabs are not styled consistently with the rest of the OS in Windows 7 or Linux. [MM-22751](https://mattermost.atlassian.net/browse/MM-22751)
- Crashes might be be experienced in some linux desktop clients. This is an upstream bug in the `libnotifyapp` library and a recommended workaround is to disable the system tray icon in the Desktop settings.
- On some Linux distros, a sandbox setting is preventing apps from opening links in the browser (see https://github.com/electron/electron/issues/17972#issuecomment-486927073). While this is fixed for most installers, it is not on the tgz. In this case manual intervention is required via `$ chmod 4755 <installpath>/chrome-sandbox`.
- Pressing Enter multiple times during Basic Authentication causes a crash.
- On apps using GPO configurations, when adding a second server tab, it is possible to drag and drop tabs but they will jump back to the original position when releasing the mouse.

### Contributors

Many thanks to all our contributors. In alphabetical order:

- [deanwhillier](https://github.com/deanwhillier), [devinbinnie](https://github.com/devinbinnie), [hanzei](https://github.com/hanzei), [hunterlester](https://github.com/hunterlester), [JtheBAB](https://github.com/JtheBAB), [jupenur](https://github.com/jupenur), [justledbetter](https://github.com/justledbetter), [nevyangelova](https://github.com/nevyangelova), [wget](https://github.com/wget), [Willyfrog](https://github.com/Willyfrog).

----

(release-v4-4)=
## Release v4.4

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/tag/v4.4.2)

- **v4.4.2, released 2020-05-11**

  - Fixed an issue on Windows where a channel was marked as read if the app was closed on a channel where the message was posted. [MM-23215](https://mattermost.atlassian.net/browse/MM-23215)

- **v4.4.1, released 2020-04-22**

  - Fixed an issue where the Desktop client opened to a blank white Window when using GPO-set teams. [MM-23082](https://mattermost.atlassian.net/browse/MM-23082)
  - Fixed an issue where Google oAuth with Gmail addresses did not work on the Desktop app for plugins. [MM-23057](https://mattermost.atlassian.net/browse/MM-23057)
  - Fixed an issue where Windows Desktop notifications were delayed. [MM-22552](https://mattermost.atlassian.net/browse/MM-22552)
  - Fixed an issue where the app sometimes didn't restore to the right position but "jumped" to a different place in the display when minimizing the app and then maximizing it. [MM-23195](https://mattermost.atlassian.net/browse/MM-23195)
  - Fixed an issue where users were not able to paste text into the login screen. [MM-23784](https://mattermost.atlassian.net/browse/MM-23784)
  - Fixed an issue where back/forward navigation on the OAuth window caused the app to crash. [MM-23153](https://mattermost.atlassian.net/browse/MM-23153)

- **v4.4.0, released 2020-02-16**

  - Original v4.4.0 release

```{Note}
Mattermost v4.4.0 contains low to medium level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
```

### Breaking Changes

- Due to moving to a new configuration version to support the new tabbar for the ability to rearrange the server tab order, it is recommended to do a backup of previous config if you want to downgrade your Desktop App version afterwards.

### Improvements

#### All Platforms

- Added support for Certificate Authentication, including PIV Card authentication.
- Improved server tab organization and visuals with the ability to reorder server tabs via drag-and-drop, notification updates that make it easier to tell when new messages or mentions come in, and a new dark theme.
- Added a spell checker for Italian language.
- Added auto focus on Server Display Name input field.

### Architectural Changes

- Major version upgrade of Electron to v6.0.0. Electron is the underlying technology used to build the Desktop apps.

### Bug Fixes

#### All Platforms

- Fixed an issue where downgrading the app caused login issues.
- Fixed an issue where Ctrl+C or Ctrl+V didn't work on Electron modals or developer tools.
- Fixed an issue where navigation with Ctrl/Cmd+Tab stopped on disconnected server.
- Fixed an issue where a new desktop window was created after clicking on a permalink to a channel on a different server.
- Fixed an issue where changing the spellchecker on the app did not suggest words in that language.
- Fixed an issue where the app window didn't save "floating" app position.
- Fixed an issue where copying and pasting into Atlassian login fields pasted text in the wrong place.

#### Windows

- Fixed an issue where installing v4.3.1 MSI installer did not remove the previous desktop app version.
- Fixed an issue where an attachment name would lose its extension if it was edited during download.
- Fixed an issue where the unread mention badge broke with more than 100 mentions.

#### macOS

- Fixed an issue where the DMG install window user interface was missing styling.
- Updated the look of Add New Server icon on the Settings page.
- Fixed an issue where the app could not recover from a connection error after leaving a computer to sleep for a few days.

### Known Issues

- The current window frame and server tabs are not styled consistently with the rest of the OS in Windows 7 or Linux. [MM-22751](https://mattermost.atlassian.net/browse/MM-22751)
- No notification on Windows if the app is closed on the channel where the message is posted. [MM-23215](https://mattermost.atlassian.net/browse/MM-23215)
- Crashes might be be experienced in some linux desktop clients. This is an upstream bug in the `libnotifyapp` library and a recommended workaround is to disable the system tray icon in the Desktop settings.
- On some Linux distros, a sandbox setting is preventing apps from opening links in the browser (see https://github.com/electron/electron/issues/17972#issuecomment-486927073). While this is fixed for most installers, it is not on the tgz. In this case manual intervention is required via `$ chmod 4755 <installpath>/chrome-sandbox`.
- Pressing Enter multiple times during Basic Authentication causes a crash.
- The confirmation dialog from UAC names MSI installers with random numbers.
- On apps using GPO configurations, when adding a second server tab, it is possible to drag and drop tabs but they will jump back to the original position when releasing the mouse.

### Contributors

Many thanks to all our contributors. In alphabetical order:

- [allenlai18](https://github.com/allenlai18), [cpanato](https://github.com/cpanato), [deanwhillier](https://github.com/deanwhillier), [devinbinnie](https://github.com/devinbinnie), [hunterlester](https://github.com/hunterlester), [JtheBAB](https://github.com/JtheBAB), [jupenur](https://github.com/jupenur), [kethinov](https://github.com/kethinov), [rascasoft](https://github.com/rascasoft), [Willyfrog](https://github.com/Willyfrog), [xalkan](https://github.com/xalkan).

----

(release-v4-3)=
## Release v4.3

**Download Binaries:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/tag/4.3.2)

- **v4.3.2, released 2019-11-29**

- Mattermost v4.3.0 contains a low level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
- Fixed an issue where the app started into white screen after a system reboot on Windows. [MM-19649](https://mattermost.atlassian.net/browse/MM-19649)
- Fixed an issue where `CMD+Z` didn't undo on the Mac desktop app. [MM-19198](https://mattermost.atlassian.net/browse/MM-19198)
- Fixed an issue where users were unable to zoom in/out except on the first server tab. [MM-19032](https://mattermost.atlassian.net/browse/MM-19032)
- Fixed an issue where right-click + "Copy" did not work in some instances. [MM-19324](https://mattermost.atlassian.net/browse/MM-19324)
- Fixed an issue where email links in profile popovers didn't work. [MM-19596](https://mattermost.atlassian.net/browse/MM-19596)

- **v4.3.1, released 2019-10-22**

  - Fixed an issue where Mac desktop app was not notarized correctly for installing on macOS Catalina. [MM-19555](https://mattermost.atlassian.net/browse/MM-19555)

- **v4.3.0, released 2019-10-17**

  - Original v4.3.0 release

```{Note}
Mattermost v4.3.0 contains medium level security fixes. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
```

### Breaking Change

The Mattermost Desktop v4.3.0 release includes a change to how desktop notifications are sent from non-secure URLs (http://). Organizations using non-secure Mattermost Servers (http://) will need to update to Mattermost Server versions 5.16.0+, 5.15.1, 5.14.4 or 5.9.5 (ESR) to continue receiving desktop notifications when using Mattermost Desktop v4.3.0 or later.

### Improvements

#### All Platforms

- Added support for maintaining a user's online status while the desktop app is in the background but the user is interacting with their computer. Requires Mattermost Server v5.16.0, v5.15.1, v5.14.4 or later.
- Updated spellchecker dictionaries for English.
- Added support for exposing Webview Developer Tools via View Menu.
- Improved the styling of the session expiry mention badge in the tab bar.
- Improved the wording of the invalid certificate dialog.
- Improved accessibility support for the menu bar items.

#### Windows

- Added support for MSI installer (Beta) to allow deploying Mattermost desktop app to the computer program files (accessible by any user accounts rather than a specific user account on the machine).
- Added support for Group Policies (GPO) to allow admins to set default servers and enable/disable the ability to add/remove servers.

#### macOS

- Added a flag to enable macOS dark mode title bar.

### Architectural Changes

- Major version upgrade of Electron to v5.0.0. Electron is the underlying technology used to build the Desktop apps.

### Bug Fixes

#### All Platforms

- Fixed an issue where opening the emoji picker froze the desktop app.
- Fixed an issue where jumbo emoji didn't render for unsupported unicode emojis.
- Fixed an issue where username and password were not being passed for HTTP basic authentication.
- Fixed an issue where switching server tabs on app load caused a visual size glitch.
- Fixed various desktop app notification issues.
- Fixed an issue where the unread count changed after opening the quick switcher.
- Fixed an issue where clicking on some links in System Console opened the links on the app itself.
- Fixed an issue where the "Help" button opened in a new browser tab instead of below the textbox in the default system browser.
- Fixed an issue where Mattermost opened both on fullscreen and on a smaller window when closing the app in fullscreen.
- Fixed an issue to prevent the app from restarting in full-screen mode.
- Fixed an issue where the dot and mention counts in server tab jewels were not centered.
- Fixed an issue where the dot in notification badges was off centre.

#### Windows

- Fixed an issue where Ctrl+M shortcut minimized the Windows app and sent a message.
- Fixed an issue where clicking the tooltip button dismissed the tooltip.

#### macOS

- Fixed an issue where using the red Close button to close the window caused a blank screen when the window was maximized.
- Fixed an issue where `Cmd + Option + Shift + v` and `Cmd + Shift + v` didn't work on macOS desktop app.
- Fixed an issue where the timezones were incorrect in OSX High Sierra.

### Known Issues

- Users are unable to zoom in/out on the desktop app. This bug will be fixed after a major version upgrade of Electron to v6.0.0.
- `CMD+Z` doesn't undo on the Mac desktop app.
- Unable to exit full screen YouTube videos.
- "RIght-click + Copy" does not work.
- Notifications appear in sequence rather than stacking on Windows.
- Clicking on notifications when using the MSI installer(s) doesn't focus the app or the channel that triggered the notification.

### Contributors

Many thanks to all our contributors. In alphabetical order:

- [asaadmahmood](https://github.com/asaadmahmood), [aswathkk](https://github.com/aswathkk), [crspeller](https://github.com/crspeller), [deanwhillier](https://github.com/deanwhillier), [devinbinnie](https://github.com/devinbinnie), [esethna](https://github.com/esethna), [jespino](https://github.com/jespino), [JtheBAB](https://github.com/JtheBAB), [manland](https://github.com/manland), [mickmister](https://github.com/mickmister), [MikeNicholls](https://github.com/MikeNicholls), [PeterDaveHello](https://github.com/PeterDaveHello), [sethitow](https://github.com/sethitow), [steevsachs](https://github.com/steevsachs), [svelle](https://github.com/svelle), [wget](https://github.com/wget), [Willyfrog](https://github.com/Willyfrog), [yuya-oc](https://github.com/yuya-oc).

----

(release-v4-2-3)=
## Release v4.2.3

This release contains a bug fix for all platforms.

- **Release date:** August 9, 2019
**Download Binary:** [Windows 32-bit](https://releases.mattermost.com/desktop/4.2.3/mattermost-setup-4.2.3-win32.exe) | [Windows 64-bit](https://releases.mattermost.com/desktop/4.2.3/mattermost-setup-4.2.3-win64.exe) | [Mac](https://releases.mattermost.com/desktop/4.2.3/mattermost-desktop-4.2.3-mac.dmg) | [Linux 64-bit](https://releases.mattermost.com/desktop/4.2.3/mattermost-desktop-4.2.3-linux-x64.tar.gz)
- **View Source Code:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/tag/v4.2.3)

### Bug Fixes

#### All Platforms

- Fixed an issue where the server URL entry prior to v4.2.2 could include malformed URLs that failed in v4.2.2 and later due to stricter validation. https://github.com/mattermost/desktop/pull/1015

----

(release-v4-2-2)=
## Release v4.2.2

This release contains a bug fix for all platforms.

- **Release date:** August 7, 2019

### Bug Fixes

#### All Platforms

- Mattermost v4.2.2 contains high level security fixes. [Upgrading](https://mattermost.com/apps) is recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).

----

(release-v4-2-1)=
## Release v4.2.1

This release contains a bug fix for all platforms.

- **Release date:** March 20, 2019
**Download Binary:** [Windows 32-bit](https://releases.mattermost.com/desktop/4.2.1/mattermost-setup-4.2.1-win32.exe) | [Windows 64-bit](https://releases.mattermost.com/desktop/4.2.1/mattermost-setup-4.2.1-win64.exe) | [Mac](https://releases.mattermost.com/desktop/4.2.1/mattermost-desktop-4.2.1-mac.dmg) | [Linux 64-bit](https://releases.mattermost.com/desktop/4.2.1/mattermost-desktop-4.2.1-linux-x64.tar.gz)
- **View Source Code:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/tag/v4.2.1)

### Bug Fixes

#### All Platforms

- Fixed an issue where some links opened in a smaller window in the Mattermost app. This issue only affected installations with a [Site URL](https://docs.mattermost.com/configure/environment-configuration-settings.html#web-siteurl) configured to use a subpath.

----

(release-v4-2-0)=
## Release v4.2.0

- **Release date:** November 27, 2018
**Download Binary:** [Windows 32-bit](https://releases.mattermost.com/desktop/4.2.0/mattermost-setup-4.2.0-win32.exe) | [Windows 64-bit](https://releases.mattermost.com/desktop/4.2.0/mattermost-setup-4.2.0-win64.exe) | [Mac](https://releases.mattermost.com/desktop/4.2.0/mattermost-desktop-4.2.0-mac.dmg) | [Linux 64-bit](https://releases.mattermost.com/desktop/4.2.0/mattermost-desktop-4.2.0-linux-x64.tar.gz)
- **View Source Code:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/releases/tag/v4.2.0)

```{Note}
Mattermost v4.2.0 contains a high level security fix. [Upgrading](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html) is highly recommended. Details will be posted on our [security updates page](https://mattermost.com/security-updates/) 30 days after release as per the [Mattermost Responsible Disclosure Policy](https://mattermost.com/security-vulnerability-report/).
```

### Improvements

#### All Platforms

- Added English (UK), Portuguese (BR), Spanish (ES) and Spanish (MX) to the spell checker.
- Added `Ctrl/Cmd+F` shortcut to work as browser-like search.
- Preserved case of first letter in spellcheck.
- Added support for session expiry notification.

#### Windows

- Set "app start on login" preference as enabled by default and synchronized its state with config.json.

#### Mac

- Added **.dmg** package to support installation.
- Added "Hide" option to Login Items in Preferences.

#### Linux

- [tar.gz] Added support for using SVG icons for Linux application menus in place of PNG icons.
- Updated categories in order to be listed under the appropriate submenu of the application starter.
- Set "app start on login" preference as enabled by default and synchronized its state with config.json.
- Added AppImage packages as an unofficial build.

### Architectural Changes

- Major version upgrade of Electron to v2.0.12. Electron is the underlying technology used to build the Desktop apps.
- Artifact names are now configured via `electron-builder.json`.

### Contributors

Many thanks to all our contributors. In alphabetical order:

- [danmaas](https://github.com/danmaas), [hmhealey](https://github.com/hmhealey), [j1mc](https://github.com/j1mc), [jasonblais](https://github.com/jasonblais), [lieut-data](https://github.com/lieut-data), [rodcorsi](https://github.com/rodcorsi), [scherno2](https://github.com/scherno2), [sudheerDev](https://github.com/sudheerDev), [svelle](https://github.com/svelle), [torlenor](https://github.com/torlenor), [yuya-oc](https://github.com/yuya-oc).

----

(release-v4-1-2)=
## Release v4.1.2

This release contains a bug fix for all platforms.

- **Release date:** May 25, 2018
**Download Binary:** [Windows 32-bit](https://releases.mattermost.com/desktop/4.1.2/mattermost-setup-4.1.2-win32.exe) | [Windows 64-bit](https://releases.mattermost.com/desktop/4.1.2/mattermost-setup-4.1.2-win64.exe) | [Mac](https://releases.mattermost.com/desktop/4.1.2/mattermost-desktop-4.1.2-mac.zip) | [Linux 64-bit](https://releases.mattermost.com/desktop/4.1.2/mattermost-desktop-4.1.2-linux-x64.tar.gz)
- **View Source Code:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/tree/v4.1.2)

### Bug Fixes

#### All Platforms

- Fixed an issue where the popup dialog to authenticate a user to their proxy or server didn't work.

----

(release-v4-1-1)=
## Release v4.1.1

This release contains multiple bug fixes for Mac due to an incorrect build for v4.1.0. Windows and Linux apps are not affected.

- **Release date:** May 17, 2018
**Download Binary:** [Windows 32-bit](https://releases.mattermost.com/desktop/4.1.1/mattermost-setup-4.1.1-win32.exe) | [Windows 64-bit](https://releases.mattermost.com/desktop/4.1.1/mattermost-setup-4.1.1-win64.exe) | [Mac](https://releases.mattermost.com/desktop/4.1.1/mattermost-desktop-4.1.1-mac.zip) | [Linux 64-bit](https://releases.mattermost.com/desktop/4.1.1/mattermost-desktop-4.1.1-linux-x64.tar.gz)
- **View Source Code:** [Mattermost Desktop on GitHub](https://github.com/mattermost/desktop/tree/v4.1.1)

### Bug Fixes

Each of the issues listed below are already fixed for Windows and Linux v4.1.0.

#### macOS

- Fixed an issue where right-clicking an image, then choosing "Save Image", did nothing.
- Fixed an issue that prevented typing in the form fields on the add server dialog when launched from the server tab bar.
- Fixed an issue that could cause an error message on the add new server dialog to be misleading.
- Fixed an issue where timestamps in message view showed no URL on hover.
- Fixed an issue where quitting and reopening the app required the user to log back in to Mattermost.
- Fixed an issue where adding a new server sometimes caused a blank page.
- Fixed deep linking via `mattermost://` protocol spawning a new copy of the Desktop App on the taskbar.

----

(release-v4-1-0)=
## Release v4.1.0

Release date: May 16, 2018

### Improvements

### All Platforms

- Improved stability and performance

  - Reduced memory usage by periodically clearing cache.
  - Fixed app crashing when a server tab was drag-and-dropped to the message view.
  - Added an option to disable GPU hardware acceleration in App Settings to improve stability in some systems.
  - Fixed Windows crash issues during installation.
  - Fixed Mac and Linux crashing after toggling "Show Mattermost icon in menu bar" app setting.

- Updated design for loading animation icon.
- Improved appearance of server tabs.
- Enabled [Certificate Transparency](https://certificate.transparency.dev/) verification in HTTPS.

#### Windows

- [Windows 7/8] Desktop notifications now respect the duration setting set in the Control Panel.

### Architectural Changes

- Major version upgrade of Electron from v1.7.13 to v1.8.4. Electron is the underlying technology used to build the Desktop apps.
- Mac download files now use Zip packages rather than tar.gz files.
- ES6 `import` and `export` now replace the `require` and `modul.export` modules for better development.
- Storybook added to more easily develop React componets without executing the desktop app.

### Bug Fixes

#### All Platforms

- Fixed an issue where an incorrect spellchecker language was used for non `en-US` locales on initial installation.
- Fixed an issue where error page appeared when U2F device was used for multi-factor authentication through single sign-on.
- Fixed an issue where right-clicking an image, then choosing "Save Image", did nothing.
- Fixed an issue that prevented typing in the form fields on the add server dialog when launched from the server tab bar.
- Fixed an issue that could cause an error message on the add new server dialog to be misleading.

#### Windows

- Fixed an issue where `file://` protocol was not working. Note that localhost URLs are not yet supported.

### Known Issues

#### All Platforms

- Clicking on a video preview opens another Mattermost window in addition to downloading the file.
- Insecure connection produces hundreds of log messages.

#### Windows

- App window doesn't save "floating" app position.
- [Windows 7] Sometimes app tries to render a page inside the app instead of in a new browser tab when clicking links].
- [Windows 10] Incorrect task name in Windows 10 startup list.
- Mattermost UI sometimes bleeds over a file explorer.
- When auto-starting the desktop app, the application window is included in Windows tab list.

#### macOS

- The application crashes when a file upload dialog is canceled without closing Quick Look.
- When the app auto-starts, app page opens on screen instead of being minimized to Dock.

#### Linux (Beta)

- [Ubuntu - 64 bit] Right clicking taskbar icon and choosing **Quit** only minimizes the app.
- [Ubuntu - 64 bit] Direct message notification sometimes comes as a streak of line instead of a pop up.

### Contributors

Many thanks to all our contributors. In alphabetical order:

- [Autre31415](https://github.com/Autre31415), [dmeza](https://github.com/dmeza), [hmhealey](https://github.com/hmhealey), [jasonblais](https://github.com/jasonblais), [kethinov](https://github.com/kethinov), [lieut-data](https://github.com/lieut-data), [lip-d](https://github.com/lip-d), [mkraft](https://github.com/mkraft), [yuya-oc](https://github.com/yuya-oc).

----

(release-v4-0-1)=
## Release v4.0.1

Release date: March 28, 2018

This release contains multiple security updates for Windows, Mac and Linux, and it is highly recommended that users upgrade to this version.

### Architectural Changes

- Minor version upgrade of Electron from v1.7.11 to v1.7.13. Electron is the underlying technology used to build the Desktop apps.

### Bug Fixes

#### All Platforms

- Disabled Certificate Transparency verification that produced unnecessary certificate errors.

----

(release-v4-0-0)=
## Release 4.0.0

Release date: January 29, 2018

This release contains multiple security updates for Windows, Mac and Linux, and it is highly recommended that users upgrade to this version.

### Improvements

#### All Platforms

- Added a dialog to allow the user to reopen the desktop app if it quits unexpectedly.
- Mattermost animation icon is now displayed when loading a page, instead of a blank screen.
- Added a dialog to request permissions to show desktop notifications or to use microphone and video for video calls from untrusted origins.
- The "Saved" indicator now appears for both Server Management and App Options on the Settings page.
- Close button on the Settings page now has a hover effect.
- Added new admin configuration settings for:

  - Disabling server management where the user cannot add or edit the server URL.
  - Setting one or more pre-configured server URLs for the end user.
  - Customizing the link in **Help > Learn More..**.

#### Windows

- Added support for protocol deep linking where the desktop app opens via `mattermost://` link if app is already installed.
- Added the ability to more easily white-label the Mattermost taskbar icon on custom builds.

#### macOS

- Added support for protocol deep linking where the desktop app opens via `mattermost://` link if app is already installed.
- Added `Ctrl+Tab` and `Ctrl+Shift+Tab` shortcuts to switch between server tabs.
- Added the option to bounce the Dock icon when receiving a notification.

### Architectural Changes

- Major version upgrade of Electron from v1.6.11 to v1.7.11. Electron is the underlying technology used to build the Desktop apps.
- The app now uses CSS to style the user interface. Styles are also divided into React's inline `style` and CSS.
- Yarn is now used to manage dependencies across Windows, Mac and Linux builds.
- Build is now run automatically before packaging the apps with `npm run package`.
- Removed hardcoded product name references.
- Added an `rm` command to `npm`, which removes all dynamically generated files to make it easy to reset the app between builds and branches.

### Bug Fixes

#### All Platforms

- Fixed the close button of the Settings page not working on first installation.
- Fixed the app publisher referring to Yuya Ochiai instead of Mattermost, Inc.
- Fixed font size not always persisting across app restarts.
- Fixed an automatic reloading of the app when a DNS or network error page is manually reloaded with CTRL/CMD+R.
- Fixed an issue where changing font size caused rendering issues on next restart.
- Fixed an issue where after adding a server on the Settings page, focus remained on the "Add new server" link.
- Fixed an issue where SAML certificate file couldn't be uploaded from the file upload dialog.

#### Windows

- Fixed desktop notifications not working when the window was minimized from an inactive state.
- Fixed the uninstaller not removing all files correctly.

#### macOS

- Fixed an issue where after uploading a file, focus wasn't put back to the text box.
- Fixed a mis-aligned `+` button in the server tab bar.

#### Linux (Beta)

- Fixed the main window not being minimized when the app is launched via "Start app on Login" option.

### Known Issues

#### All Platforms

- Insecure connection produces hundreds of log messages.

#### Windows

- App window doesn't save "floating" app position.
- Windows 7: Sometimes the app tries to render the page inside the app instead of in a new browser tab when clicking links.
- Windows 10: Incorrect task name in Windows 10 start-up list.

#### Mac

- The application crashes when a file upload dialog is canceled without closing Quick Look.
- When the app auto-starts, app page opens on screen instead of being minimized to Dock.
- You have to click twice when a window is out of focus to have actions performed.

#### Linux (Beta)

- Ubuntu - 64 bit: Right clicking taskbar icon and choosing **Quit** only minimizes the app.
- Ubuntu - 64 bit: Direct message notification sometimes renders as a streak or line instead of a pop up.

### Contributors

Many thanks to all our contributors. In alphabetical order:

- [csduarte](https://github.com/csduarte), [dmeza](https://github.com/dmeza), [jasonblais](https://github.com/jasonblais), [jarredwitt](https://github.com/jarredwitt), [wvds](https://github.com/wvds), [yuya-oc](https://github.com/yuya-oc).

----

(release-v3-7-1)=
## Release 3.7.1

Release date: August 30, 2017

This release contains a security update for Windows, Mac and Linux, and it is highly recommended that users upgrade to this version.

### Improvements and Bug Fixes

#### Windows

- Client no longer freezes intermittently, such as when receiving desktop notifications.
- [Windows 8.1/10] Added support for running the desktop app across monitors of different DPI.
- [Windows 7/8] Clicking on a desktop notification now opens the message.

----

(release-v3-7-0)=
Release 3.7.0
--------------

Release date: May 9th, 2017

### Improvements

#### All Platforms

- Added an inline spell checker for English, French, German, Spanish, and Dutch.
- Removed an obsolete "Display secure content only" option, following an [upgrade of the Electron app to Chrome v56](https://github.com/electron/electron/commit/2e0780308c7ef2258422efd34c968091d7cd5b65)
- Reset app window position when restoring it off-screen from a minimized state.
- Improved page loading and app view rendering.

#### Windows

- [Windows 7/8] Added support for sound when a desktop notification is received.
- Removed obsolete support for Japanese fonts.
- The application window now respects 125% display resolution.

### Bug Fixes

#### All Platforms

- An extra row is no longer added after switching channels with CTRL/CMD+K shortcut.
- Fixed an issue where an unexpected extra app window opened after clicking a public link of an uploaded file.
- Fixed JavaScript errors when refreshing the page.
- Fixed vertical alignment of the Add Server "+" button in the server tab bar.

#### Windows

- Focus is now set to the next top-level window after closing the main app window.
- Fixed an issue where the app remained in the ["classic" ALT+TAB window switcher](https://www.askvg.com/how-to-get-windows-xp-styled-classic-alttab-screen-in-windows-vista-and-7/) after closing the main app window.

#### macOS

- Fixed an issue where the application was not available on the Dock after a computer reboot.
- Fixed an issue where Quick Look couldn't be closed after opening the file upload dialog.

#### Linux (Beta)

- Fixed an issue where the setting was not saved after changing the tray icon theme.

### Known Issues

#### All Platforms

- [If you click twice on the tab bar, and then attempt to use the "Zoom in/out" to change font size, the app window doesn't render properly](https://github.com/mattermost/desktop/issues/334)
- [Holding down CTRL, SHIFT, or ALT buttons and clicking a channel opens a new application window](https://github.com/mattermost/desktop/issues/406)
- [Unable to upload a SAML certificate file from the file upload dialog](https://github.com/mattermost/desktop/issues/497)

#### Windows

- [Windows 7] [Sometimes the app tries to render the page inside the app instead of in a new browser tab when clicking links](https://github.com/mattermost/desktop/issues/369)

#### macOS

- [After uploading a file with a keyboard shortcut, focus isn't set back to the message box](https://github.com/mattermost/desktop/issues/341)
- The application crashes when a file upload dialog is canceled without closing Quick Look.

#### Linux (Beta)

- [Ubuntu - 64 bit] [Right clicking taskbar icon and choosing **Quit** only minimizes the app](https://github.com/mattermost/desktop/issues/90#issuecomment-233712183)
- [Ubuntu - 64 bit] [Direct message notification comes as a streak of line instead of a pop up](https://github.com/mattermost/mattermost-server/issues/3589)

### Contributors

Many thanks to all our contributors. In alphabetical order:

- [jasonblais](https://github.com/jasonblais), [jnugh](https://github.com/jnugh), [yuya-oc](https://github.com/yuya-oc).

Thanks also to those who reported bugs that benefited the release, in alphabetical order:

- [esethna](https://github.com/esethna) ([#524](https://github.com/mattermost/desktop/issues/524)), [hanzei](https://github.com/hanzei) ([#523](https://github.com/mattermost/desktop/issues/523))

----

(release-v3-6-0)=
## Release 3.6.0

Release date: February 28, 2017

Upgrading to Mattermost server 3.6 or later is recommended, as new features for the desktop app have been added following the release of the team sidebar.

### Improvements

- Added support for unread indicators following the release of team sidebar in Mattermost server 3.6
- Removed a confusing CTRL/CMD+S shortcut for searching within a Mattermost team
- Added support for SAML OneLogin and Google authentication for Enterprise users
- Switching to a server from the system tray icon, from "Window" menu bar item, or through CTRL/CMD+{n} shortcut now works while viewing the Settings page
- Streamlined desktop server management:

  - "Team Management" changed to "Server Management" following the release of team sidebar in Mattermost server 3.6
  - Added a "+" icon to the desktop server tab bar to more easily sign into a new Mattermost server
  - Added an option to sign in to another Mattermost server from **File > Sign in to Another Server**
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

### Bug Fixes

#### All Platforms

- Mattermost window no longer opens on a display screen that has been disconnected
- Mention badges no longer persist after logging out of a Mattermost server
- After right-clicking an image or a link, the "Copy Link" option no longer moves around when clicking different places afterwards
- Fixed an issue where minimum window size is not set
- Changed target resolution size to 1000x700 to prevent unintended issues on the user interface
- Fixed an issue where the application menu is not updated when the config file is saved in the Settings page
- Fixed login issues with local development environment
- Removed a white screen which was momentarily displayed on startup

#### Windows

- Fixed an issue where an unexpected window appears while installing or uninstalling
- Fixed an issue where the maximized state of the application window was not restored on re-launch if "Start app on Login" setting is enabled

#### Linux (Beta)

- Fixed an issue where tray icon wasn't shown by default even when "Show icon in the notification area" setting is enabled
- Fixed an issue where the maximized state of the application window was not restored on re-launch if "Start app on login" setting is enabled

### Known Issues

#### All Platforms

- [If you click twice on the tab bar, and then attempt to use the "Zoom in/out" to change font size, the app window doesn't render properly](https://github.com/mattermost/desktop/issues/334)
- [After using CTRL+K, an added row appears in the message box](https://github.com/mattermost/desktop/issues/426)
- [Holding down CTRL, SHIFT or ALT buttons and clicking a channel opens a new application window](https://github.com/mattermost/desktop/issues/406)

#### Windows

- [Windows 7] [Sometimes the app tries to render the page inside the app instead of in a new browser tab when clicking links](https://github.com/mattermost/desktop/issues/369)

#### macOS

- [After uploading a file with a keyboard shortcut, focus isn't set back to the message box](https://github.com/mattermost/desktop/issues/341)

#### Linux (Beta)

- [Ubuntu - 64 bit] [Right clicking taskbar icon and choosing **Quit** only minimizes the app](https://github.com/mattermost/desktop/issues/90#issuecomment-233712183)
- [Ubuntu - 64 bit] [Direct message notification comes as a streak of line instead of a pop up](https://github.com/mattermost/mattermost-server/issues/3589)

### Contributors

Many thanks to all our contributors. In alphabetical order:

- [asaadmahmood](https://github.com/asaadmahmood), [jasonblais](https://github.com/jasonblais), [jnugh](https://github.com/jnugh), [yuya-oc](https://github.com/yuya-oc).

----

(release-v3-5-0)=
## Release v3.5.0

Release date: December 14, 2016

### Improvements

#### All Platforms

- URL address is shown when hovering over links with a mouse
- Added CTRL+SHIFT+MINUS as a shortcut for decreasing font size (zooming out)
- Reduce upgrade issues by properly clearing cache when updating the desktop app to a new version (the application cache will be purged whenever the desktop app version changes)
- When launching the app from the command line interface, unnecessary warning messages are no longer sent if connecting to a trusted https connection without a `certificate.json` file

#### Windows

- Link addresses can now be copied and pasted inside the app

### Bug Fixes

#### All Platforms

- YouTube previews now work, even if mixed content is allowed
- Fixed an incorrect cursor mode for "Edit" and "Remove" buttons on the Settings page
- Fixed an issue where "Zoom in/out" settings did not properly work
- When disconnected from Mattermost, the "Cannot connect to Mattermost" page is now properly aligned at the top of the window

#### Windows

- The menu bar option for "Redo" is now properly shown as CTRL+Y

#### macOS

- Fixed an issue where the default download folder was `Macintosh HD`
- Removed an unexpected "Show Tab Bar" menu item on macOS 10.12

#### Linux (Beta)

- Fixed an issue where the option "Leave app running in notification area when the window is closed" was never enabled.

### Known Issues

#### All Platforms

- [If you click twice on the tab bar, and then attempt to use the "Zoom in/out" to change font size, the app window doesn't render properly](https://github.com/mattermost/desktop/issues/334)
- [Direct messages cause notification icons to appear on all team tabs, which don't clear until you click on each team](https://github.com/mattermost/desktop/issues/160)
- [After right-clicking an image or a link, the "Copy Link" option sometimes moves around when clicking different places afterwards](https://github.com/mattermost/desktop/issues/340)

#### Windows

- [Windows 7] [Sometimes the app tries to render clicked linked inside the app, instead of in a new browser tab](https://github.com/mattermost/desktop/issues/369>)

#### macOS

- [After uploading a file with a keyboard shortcut, focus isn't set back to the message box](https://github.com/mattermost/desktop/issues/341)

#### Linux (Beta)

- [Ubuntu - 64 bit] [Right clicking taskbar icon and choosing Quit only minimizes the app](https://github.com/mattermost/desktop/issues/90#issuecomment-233712183)
- [Ubuntu - 64 bit] [Direct message notification pop ups do not properly render](https://github.com/mattermost/mattermost-server/issues/3589)

### Contributors

Many thanks to all our contributors. In alphabetical order:

- [itsmartin](https://github.com/itsmartin),
- [jasonblais](https://github.com/jasonblais),
- [jcomack](https://github.com/jcomack),
- [jnugh](https://github.com/jnugh),
- [kytwb](https://github.com/kytwb),
- [magicmonty](https://github.com/magicmonty),
- [Razzeee](https://github.com/Razzeee),
- [yuya-oc](https://github.com/yuya-oc).

Thanks also to those who reported bugs that benefited the release, in alphabetical order:

- ellisd ([#383](https://github.com/mattermost/desktop/issues/383)), [it33](https://github.com/it33) ([#384](https://github.com/mattermost/desktop/issues/384)), [jnugh](https://github.com/jnugh) ([#392](https://github.com/mattermost/desktop/issues/392)), [lfbrock](https://github.com/lfbrock) ([#382](https://github.com/mattermost/desktop/issues/382)), [yuya-oc](https://github.com/yuya-oc) ([#391](https://github.com/mattermost/desktop/issues/391)).

----

(release-v3-4-1)=
## Release v3.4.1

Release date: September 30, 2016

This release contains a security update and it is highly recommended that users upgrade to this version.

Version number updated to 3.4 to make numbering consistent with Mattermost server and mobile app releases. This change will not imply monthly releases.

- v3.4.1, released 2016-09-30

 - (Mac) Fixed an issue where the app window pops up second to foreground when a new message is received

- v3.4.0, released 2016-09-22

   - Original v3.4 release

### Improvements

#### All Platforms

- Current team and channel name shown in window title bar
- Team tab is bolded for unread messages and has a red dot with a count of unread mentions
- Added new shortcuts:

  - CTRL+S; CMD+S on Mac: sets focus on the Mattermost search box
  - ALT+Left Arrow; CMD+[ on Mac: go to previous page in history
  - ALT+Right Arrow; CMD+] on Mac: go to next page in history

- Upgraded the Settings page user interface
- The app now tries to reconnect periodically if a page fails to load
- Added validation for name and URL when adding a new team on the Settings page

#### Windows

- Added access to the settings menu from the system tray icon
- Only one instance of the desktop application will now load at a time
- Added an option to configure whether a red badge is shown on taskbar icon for unread messages

#### macOS

- Added an option to configure whether a red badge is shown on taskbar icon for unread messages

#### Linux (Beta)

- Added an option to flash taskbar icon when a new message is received
- Added a badge to count mentions on the taskbar icon (for Unity)
- Added a script, `create_desktop_file.sh` to create `Mattermost.desktop` desktop entry to help [integrate the application into a desktop environment](https://wiki.archlinux.org/title/Desktop_entries) more easily
- Added access to the settings menu from the system tray icon
- Only one instance of the desktop application will now load at a time

### Bug Fixes

#### All Platforms

- Cut, copy and paste are shown in the user interface only when the commands are available
- Copying link addresses now work properly
- Saving images by right-clicking the image preview now works
- Refreshing the app page no longer takes you to the team selection page, but keeps you on the current channel
- Fixed an issue where the maximized state of the app window was lost in some cases
- Fixed an issue where shortcuts didn't work when switching applications or tabs in some cases

#### Windows

- Removed misleading shortcuts from the system tray menu
- Removed unclear desktop notifications when the application page fails to load
- Fixed the Mattermost icon for desktop notifications in Windows 10
- Fixed an issue where application icon at the top left of the window was pixelated
- Fixed an issue where the application kept focus after closing the app window

#### Linux (Beta)

- Removed misleading shortcuts from the system tray menu
- Removed unclear desktop notifications when the application page fails to load

### Known Issues

#### All Platforms

- YouTube videos do not work if mixed content is enabled from app settings

#### Windows

- Copying a link address and pasting it inside the app doesn't work

#### Linux (Beta)

- [Ubuntu - 64 bit] Right clicking taskbar icon and choosing **Quit** only minimizes the app
- [Ubuntu - 64 bit] [Direct message notification comes as a streak of line instead of a pop up](https://github.com/mattermost/mattermost-server/issues/3589)

### Contributors

Many thanks to all our contributors. In alphabetical order:

- [akashnimare](https://github.com/akashnimare),
- [asaadmahmood](https://github.com/asaadmahmood),
- [jasonblais](https://github.com/jasonblais),
- [jgis](https://github.com/jgis),
- [jnugh](https://github.com/jnugh),
- [Razzeee](https://github.com/Razzeee),
- [St-Ex](https://github.com/St-Ex),
- [timroes](https://github.com/timroes),
- [yuya-oc](https://github.com/yuya-oc).

--------------

(release-v1-3-0)=
## Release v1.3.0

Release date: 2016-07-18

[Download the latest version here](https://mattermost.com/apps)

### Improvements

#### All Platforms

- Added auto-reloading when tab fails to load the team.
- Added the ability to access all of your teams by right clicking the system tray icon.

##### Menu Bar

- New Keyboard Shortcuts

  - Adjust text size

   - CTRL+0 (Menu Bar -> View -> Actual Size): Reset the zoom level.
   - CTRL+PLUS (Menu Bar -> View -> Zoom In): Increase text size
   - CTRL+MINUS (Menu Bar -> View -> Zoom Out): Decrease text size

  - Control window

   - CTRL+W (Menu Bar -> Window -> Close): On Linux, this minimizes the main window.
   - CTRL+M (Menu Bar -> Window -> Minimize)

  - Switch teams (these shotcuts also reopen the main window)

   - CTRL+{1-9} (Menu Bar -> Window -> [Team name]): Open the *n*-th tab.
   - CTRL+TAB or ALT+CMD+Right (Menu Bar -> Window -> Select Next Team): Switch to the next window.
   - CTRL+SHIFT+TAB or ALT+CMD+Left (Menu Bar -> Window -> Select Previous Team): Switch to the previous window.
   - Right click on the tray item, to see an overview of all your teams. You can also select one and jump right into it.

  - Added **Help** to the Menu Bar, which includes

   - Link to [Mattermost Docs](https://docs.mattermost.com)
   - Field to indicate the application version number.

##### Settings Page

- Added a "+" button next to the **Teams** label, which allows you to add more teams.
- Added the ability to edit team information by clicking on the pencil icon to the right of the team name.

#### Windows

- Added an installer for better install experience.
- The app now minimizes to the system tray when application window is closed.
- Added an option to launch application on login.
- Added an option to blink the taskbar icon when a new message has arrived.
- Added tooltip text for the system tray icon in order to show count of unread channels/mentions.
- Added an option to toggle the app to minimize/restore when clicking on the system tray icon.

#### macOS

- Added colored badges to the menu icon when there are unread channels/mentions.
- Added an option to minimize the app to the system tray when application window is closed.

#### Linux (Beta)

- Added an option to show the icon on menu bar (requires libappindicator1 on Ubuntu).
- Added an option to launch application on login.
- Added an option to minimize the app to the system tray when application window is closed.

### Other Changes

- Application license changed from MIT License to Apache License, Version 2.0.

### Bug Fixes

#### All platforms

- Fixed authentication dialog not working for proxy.

#### Windows

- Fixed the blurred system tray icon.
- Fixed a redundant description appearing in the pinned start menu on Windows 7.

#### macOS

- Fixed two icons appearing on a notification.

### Known Issues

#### Linux (Beta)

- [Ubuntu - 64 bit] Right clicking taskbar icon and choosing **Quit** only minimizes the app
- [Ubuntu - 64 bit] [Direct message notification comes as a streak of line instead of a pop up](https://github.com/mattermost/mattermost-server/issues/3589)

### Contributors

Many thanks to all our contributors. In alphabetical order:

- [CarmDam](https://github.com/CarmDam),
- [it33](https://github.com/it33),
- [jasonblais](https://github.com/jasonblais),
- [jnugh](https://github.com/jnugh),
- [magicmonty](https://github.com/magicmonty),
- [MetalCar](https://github.com/MetalCar),
- [Razzeee](https://github.com/Razzeee),
- [yuya-oc](https://github.com/yuya-oc).

--------------

(release-v1-2-1-Beta)=
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

#### All Platforms

- Improved the style for tab badges.
- Added **Allow mixed content** option to render images with `http://`.
- Added the login dialog for `http` authentication.

#### macOS

- Added an option to show a black dot indicating unread messages on the team tab bar.

#### Linux

- Added **.deb** packages to support installation.

### Bug Fixes

#### All Platforms

- Node.js environment is enabled in the new window.
- The link other than `http://` and `https://` is opened by clicking.

#### Linux

- Desktop notification is shown as a dialog on Ubuntu 16.04.

### Known issues

- The shortcuts can't switch teams twice in a row.
- The team pages are not correctly rendered until the window is resized when the zoom level is changed.

### Contributors

Many thanks to all our contributors. In alphabetical order:

- [asaadmahmood](https://github.com/asaadmahmood),
- [jeremycook](https://github.com/jeremycook),
- [jnugh](https://github.com/jnugh),
- [jwilander](https://github.com/jwilander),
- [mgielda](https://github.com/mgielda),
- [lloeki](https://github.com/lloeki),
- [yuya-oc](https://github.com/yuya-oc).

(release-v1-1-1-Beta)=
## Release v1.1.1 (Beta)

Release date: 2016-04-13

This release contains a security update and it is highly recommended that users upgrade to this version.

- v1.1.1, released 2016-04-13

  - If the specified team URL on the **Settings** page contains an additional space, the app now properly redirects to the team page
  - ALT+SHIFT now opens the menu on Cinnamon desktop environment.

- v1.1.0, released 2016-03-30

  - Original v1.1 release

The `electron-mattermost` project is now the official desktop application for the Mattermost open source project.

### Changes

#### All platforms

- Rename project from `electron-mattermost` to `desktop`
- Rename the executable file from `electron-mattermost` to `Mattermost`
- The configuration directory is also different from previous versions.
- Should execute following command to take over `config.json`.

  - Windows:
      `mkdir %APPDATA%\Mattermost and copy %APPDATA%\electron-mattermost\config.json %APPDATA%\Mattermost\config.json`
  - OS X:
      `ditto ~/Library/Application\ Support/electron-mattermost/config.json ~/Library/Application\ Support/Mattermost/config.json`
  - Linux:
      `mkdir -p ~/.config/Mattermost && cp ~/.config/electron-mattermost/config.json ~/.config/Mattermost/config.json`

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
- Some keyboard shortcuts are missing (e.g. CTRL+W, CMD+PLUS).

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

[Release v0.2.0 (Unofficial) 2015-10-14](https://github.com/mattermost/desktop/releases/tag/v0.2.0)

[Release v0.1.0 (Unofficial) 2015-10-10](https://github.com/mattermost/desktop/releases/tag/v0.1.0)
