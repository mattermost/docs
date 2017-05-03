
Desktop Application Install Guides
===================================

Mattermost desktop applications are available for Windows, Mac and Linux operating systems. They support all the features of the web experience, plus:

 - Connect to multiple Mattermost servers from a single interface, and switch with shortcut keys.
 - Auto-start Mattermost when a user logs into their machine
 - (Windows) Add Mattermost to Start menu, taskbar and system tray
 - (Mac) Add Mattermost to the applications Dock
 - (Linux) ``Desktop Entry`` for the application to more easily `integrate into a desktop environment <https://wiki.archlinux.org/index.php/Desktop_entries>`_

Below is a list of additional resources:

 - `Guide for configuring your desktop app experience <https://docs.mattermost.com/help/apps/desktop-guide.html>`_
 - `Changelog <https://docs.mattermost.com/help/apps/desktop-changelog.html>`_
 - Contributor’s guide (coming soon)
 - `Source code <https://github.com/mattermost/desktop>`_

You can `download the apps directly from our downloads page <https://about.mattermost.com/downloads/>`_. You may also use the following installation guides for Windows, Mac and Linux.

.. contents::
    :backlinks: top

Windows 10+, Windows 8.1+, Windows 7+
--------------------------------------------------

1. Download latest version of the Mattermost desktop app:

   - `64-bit version of Windows <https://releases.mattermost.com/desktop/3.6.0/mattermost-setup-3.6.0-win64.exe>`_
   - `32-bit version of Windows <https://releases.mattermost.com/desktop/3.6.0/mattermost-setup-3.6.0-win32.exe>`_

2. From the ``\Downloads`` directory right-click on the file ``mattermost-setup-3.6.0...`` and select **Open**.

This will start an installer for the app. Once finished, the Mattermost desktop app will open automatically.

Mac OS X 10.9+
--------------------------------------------------

1. Download `latest version of the Mattermost desktop app <https://releases.mattermost.com/desktop/3.6.0/mattermost-desktop-3.6.0-osx.tar.gz>`_

2. From the ``/Downloads`` directory, find ``/mattermost-desktop...`` folder.

   - If one doesn’t exist, from the ``/Downloads`` directory, find a file ending in ``-osx.tar.gz`` and double-click on the file. The ``/mattermost-desktop...`` folder should now be created.

3. From the ``/mattermost-desktop...`` folder, right-click on ``Mattermost`` package and select **Open**. If you see a dialog to confirm the application, choose **Open**.

The Mattermost desktop should open automatically.

Linux (Beta)
--------------------------------------------------

Generic Linux package
~~~~~~~~~~~~~~~~~~~~~

1. Download latest version of the Mattermost desktop app:

  64-bit systems:
   `mattermost-desktop-3.6.0-linux-x64.tar.gz <https://releases.mattermost.com/desktop/3.6.0/mattermost-desktop-3.6.0-linux-x64.tar.gz>`_
  32-bit systems:
   `mattermost-desktop-3.6.0-linux-ia32.tar.gz <https://releases.mattermost.com/desktop/3.6.0/mattermost-desktop-3.6.0-linux-ia32.tar.gz>`_

2. Extract the archive to a convenient location. You can then execute ``mattermost-desktop``, which is located inside the extracted directory.

3. To create a Desktop launcher, open the file ``README.md`` and follow the instructions in the *Desktop launcher* section.

Ubuntu and Debian-based systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unofficial, community-driven .deb packages are available.

1. Download the latest version of the Mattermost desktop app:

    64-bit systems
     `mattermost-desktop-3.6.0-linux-amd64.deb <https://releases.mattermost.com/desktop/3.6.0/mattermost-desktop-3.6.0-linux-amd64.deb>`_
    32-bit systems
     `mattermost-desktop-3.6.0-linux-i386.deb <https://releases.mattermost.com/desktop/3.6.0/mattermost-desktop-3.6.0-linux-i386.deb>`_

2. At the command line, execute one of the following commands depending on the package that you downloaded:

    64-bit systems
      ``sudo dpkg -i mattermost-desktop-3.6.0-linux-amd64.deb``
    32-bit systems
      ``sudo dpkg -i mattermost-desktop-3.6.0-linux-i386.deb``

3. To run Mattermost, open **Dash** (located at top left corner) and input ``mattermost``, then click the Mattermost icon.

Snapcraft package
~~~~~~~~~~~~~~~~~

A snap is available for systems that have Snapcraft installed. Snapcraft is installed by default on Ubuntu 16.04 and later, but for most other Linux distributions you can install it manually. To install Snapcraft, see `Install snapd <https://snapcraft.io/docs/core/install>`_ on the Snapcraft website.

1. At the command line, execute the following command:

  ``sudo snap install mattermost-desktop --beta``

2. To run Mattermost, open **Dash** (located at top left corner) and input ``mattermost``, then click the Mattermost icon.

Troubleshooting
--------------------------------------------------

Possible solutions to issues encountered when using the Desktop App.

"Installation has failed" dialog
    The app data might be corrupted - remove all the files in `C:\Users...\AppData\Local\mattermost`, then try re-installing the app.

Desktop App window is black and doesn't load the page
    - First try to clear cache and reload the app from **View** > **Clear Cache and Reload** or by pressing CTRL/CMD+SHIFT+R.
    - Next, quit the app and restart it to see if the issue clears.
    - If neither of the above works and you are using a special video driver such as Optimus, try disabling it to see if the problem is resolved.
    - Finally, try disabling GPU hardware acceleration by using the `--disable-gpu <http://peter.sh/experiments/chromium-command-line-switches/#disable-gpu>`_ Chromium command line switch.

    If none of the above steps resolve the issue, please open a new ticket in the `Mattermost Troubleshooting Forum <https://forum.mattermost.org/t/how-to-use-the-troubleshooting-forum/150>`_.

Desktop App is not visible, but you can see the Mattermost icon in the Task Bar
  This issue can occur on Windows in a multiple-monitor setup. When you disconnect the monitor that Mattermost is displayed on, Mattermost continues to display at screen coordinates that no longer exist.

  To resolve this issue, you can reset the Desktop App screen location by deleting the screen location file. When the file is not present, the Desktop App displays on the primary monitor by default.

  **To reset the Desktop App screen location**:
    1. If the Desktop App is running, right-click the Mattermost icon in the task bar and click **Close Window**.
    2. Open Windows File Explorer, and navigate to the ``%USERPROFILE%\AppData\Roaming\Mattermost`` folder.
    3. Delete the file ``bounds-info.json``

For additional troubleshooting tips, see the `troubleshooting guide <https://www.mattermost.org/troubleshoot/>`_.

To submit an improvement or correction, click  **Edit** at the top of this page.
