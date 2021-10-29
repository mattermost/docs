
Desktop Application Install Guides
==================================

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Mattermost desktop applications are available for Windows, Mac, and Linux operating systems. They support all the features of the web experience, plus:

- Connect to multiple Mattermost servers from a single interface, and switch with shortcut keys.
- Auto-start Mattermost when a user logs into their machine.
- (Windows) Add Mattermost to Start menu, Taskbar, and System Tray.
- (Windows/Mac) Deep link to the desktop app via ``mattermost://`` protocol if app is already installed.
- (Mac) Add Mattermost to the Dock.
- (Linux) ``Desktop Entry`` for the application to more easily `integrate into a desktop environment <https://wiki.archlinux.org/index.php/Desktop_entries>`__.

Below is a list of additional resources:

- `Guide for configuring your desktop app experience <https://docs.mattermost.com/help/apps/desktop-guide.html>`__
- `Changelog <https://docs.mattermost.com/help/apps/desktop-changelog.html>`__
- `Source code <https://github.com/mattermost/desktop>`__
- Contributor’s guide (coming soon)

You can `download the Mobile Apps directly from our Downloads page <https://mattermost.com/download/#mattermostApps>`__. You may also use the following installation guides for Windows, Mac, and Linux.

.. include:: ../upgrade/upgrading-to-v60.rst

.. contents::
    :backlinks: top

Windows 10+, Windows 8.1+
-------------------------

1. Download the latest version of the Mattermost desktop app:

  - `32/64-bit version of Windows <https://releases.mattermost.com/desktop/5.0.1/mattermost-desktop-setup-5.0.1-win.exe>`__

2. From the **\Downloads** folder right-click on the file ``mattermost-desktop-setup-5.0.1-win.exe`` and select **Open**.

This will start an installer for the app. Once finished, the Mattermost desktop app will open automatically.

MSI Installer and Group Policies (Beta)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the latest version of the Mattermost desktop app MSI installer (Beta):

- MSI for `64-bit version of Windows <https://releases.mattermost.com/desktop/5.0.1/mattermost-desktop-5.0.1-x64.msi>`__
- MSI for `32-bit version of Windows <https://releases.mattermost.com/desktop/5.0.1/mattermost-desktop-5.0.1-x86.msi>`__

`See here <https://docs.mattermost.com/install/desktop-msi-gpo.html>`__ for instructions on installing the Mattermost desktop app via an MSI installer and configuring supported Group Policies.

The following Group Policies are available:

+----------------------------+-----------------------------------------------------------------------------+----------------------+
| Group Policy               | Description                                                                 | Required Version     |
+============================+=============================================================================+======================+
| Enable Server Management   | If disabled, management of servers in the app settings are disabled.        | 4.3 or later         |
+----------------------------+-----------------------------------------------------------------------------+----------------------+
| Default Server List        | Define one or more default, permanent servers.                              | 4.3 or later         |
+----------------------------+-----------------------------------------------------------------------------+----------------------+

macOS 10.9+
-----------

1. Download the latest version of the Mattermost desktop app:
  - `Intel systems <https://releases.mattermost.com/desktop/5.0.1/mattermost-desktop-5.0.1-mac-x64.dmg>`__
  - `M1 systems <https://releases.mattermost.com/desktop/5.0.1/mattermost-desktop-5.0.1-mac-m1.dmg>`__ (Beta)

2. Double-click the download to open the disk image.

3. Drag the Mattermost application to the **Applications** folder.

`Homebrew <https://brew.sh>`__ users can install with ``brew install --cask mattermost``.

Linux
-----

Generic Linux package
~~~~~~~~~~~~~~~~~~~~~

1. Download the latest version of the Mattermost desktop app:

 - 64-bit systems: `mattermost-desktop-5.0.1-linux-x64.tar.gz <https://releases.mattermost.com/desktop/5.0.1/mattermost-desktop-5.0.1-linux-x64.tar.gz>`__
 - 32-bit systems: `mattermost-desktop-5.0.1-linux-ia32.tar.gz <https://releases.mattermost.com/desktop/5.0.1/mattermost-desktop-5.0.1-linux-ia32.tar.gz>`__

2. Extract the archive to a convenient location. You can then execute ``mattermost-desktop``, which is located inside the extracted directory.

3. To create a Desktop launcher, open the file **README.md** and follow the instructions in the **Desktop launcher** section.

Ubuntu and Debian-based systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unofficial, community-driven ``.deb`` packages are available.

1. Download the latest version of the Mattermost Desktop App:

- 64-bit systems
  `mattermost-desktop-5.0.1-linux-amd64.deb <https://releases.mattermost.com/desktop/5.0.1/mattermost-desktop-5.0.1-linux-amd64.deb>`__
- 32-bit systems
  `mattermost-desktop-5.0.1-linux-i386.deb <https://releases.mattermost.com/desktop/5.0.1/mattermost-desktop-5.0.1-linux-i386.deb>`__

2. At the command line, execute one of the following commands depending on the package that you downloaded:

- 64-bit systems
  ``sudo dpkg -i mattermost-desktop-5.0.1-linux-amd64.deb``
- 32-bit systems
  ``sudo dpkg -i mattermost-desktop-5.0.1-linux-i386.deb``

3. To run Mattermost, open **Dash** (located at the top left corner), enter **mattermost**, then click the Mattermost icon.

Linux rpm files (Beta)
~~~~~~~~~~~~~~~~~~~~~~

Unofficial, community-driven ``.rpm`` packages are available.

1. Download the latest version of the Mattermost Desktop App:

- 32-bit systems
  `mattermost-desktop-5.0.1-linux-i686.rpm <https://releases.mattermost.com/desktop/5.0.1/mattermost-desktop-5.0.1-linux-i686.rpm>`__
- 64-bit systems
  `mattermost-desktop-5.0.1-linux-x86_64.rpm <https://releases.mattermost.com/desktop/5.0.1/mattermost-desktop-5.0.1-linux-x86_64.rpm>`__

2. At the command line, execute one of the following commands depending on the package that you downloaded:

- 32-bit systems
  ``sudo rpm -i mattermost-desktop-5.0.1-linux-i686.rpm``
- 64-bit systems
  ``sudo rpm -i mattermost-desktop-5.0.1-linux-x86_64.rpm``

3. To run Mattermost, open **Dash** (located at the top left corner), enter **mattermost**, then click the Mattermost icon.

Arch Linux-based systems
~~~~~~~~~~~~~~~~~~~~~~~~

To install the Desktop client on Arch Linux, see the `Mattermost page <https://wiki.archlinux.org/index.php/Mattermost>`__ on the Arch Linux wiki.

Snapcraft package
~~~~~~~~~~~~~~~~~

A snap is available for systems that have Snapcraft installed. Snapcraft is installed by default on Ubuntu 16.04 and later, but for most other Linux distributions you can install it manually. To install Snapcraft, see `Install snapd <https://snapcraft.io/docs/core/install>`__ on the Snapcraft website.

1. At the command line, execute the following command:

  ``sudo snap install mattermost-desktop --beta``

2. To run Mattermost, open **Dash** (located at the top left corner), enter **mattermost**, then click the Mattermost icon.

Troubleshooting
---------------

"Installation has failed" dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The app data might be corrupted. Remove all the files in ``%LOCALAPPDATA%\mattermost``, then try reinstalling the app.
    
"The application "Mattermost" can't be opened" dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On macOS Catalina, this dialog can be triggered if the Mac Archive Utility is the default method for decompressing files. In this case using a third-party tool such as `Keka <https://www.keka.io>`__ or `Unarchiver <https://macpaw.com/the-unarchiver>`__ may resolve the problem.

Desktop App window is black and doesn't load the page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. First, make sure you have installed the latest desktop app version `from our website <https://mattermost.com/download/#mattermostApps>`__. Check your app version from **Help > Version**.
2. Try to clear cache and reload the app from **View > Clear Cache and Reload** or use CTRL/CMD+SHIFT+R.
3. Quit the app and restart it to see if the issue clears.
4. Disable GPU hardware acceleration from **File > Settings** on Windows and Linux or **Mattermost > Settings** on macOS, and unselect **Use GPU hardware acceleration**.
5. If you are using a special video driver, such as Optimus, try disabling it to see if the problem is resolved.

If none of the above steps resolve the issue, please open a new ticket in the `Mattermost Troubleshooting Forum <https://forum.mattermost.org/t/how-to-use-the-troubleshooting-forum/150>`__.

Desktop App is not visible, but the Mattermost icon is in the Task Bar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This issue can occur on Windows in a multiple-monitor setup. When you disconnect the monitor that Mattermost is displayed on, Mattermost continues to display at screen coordinates that no longer exist.

To resolve this issue, you can reset the desktop app screen location by deleting the screen location file. When the file is not present, the desktop app displays on the primary monitor by default.

**To reset the desktop app screen location**

1. If the desktop app is running, right-click the Mattermost icon in the task bar and click **Close Window**.
2. Open Windows File Explorer, and navigate to the ``%APPDATA%\\Mattermost`` folder.
3. Delete the file ``bounds-info.json``.

Desktop App constantly refreshes the page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This issue can occur when ``localStorage`` has an unexpected state. To resolve the issue:

- Windows: Open Windows File Explorer, navigate to the ``%APPDATA%\Mattermost`` folder, then delete the ``Local Storage`` folder.
- Mac: Open Finder, navigate to the ``~/Library/Application Support/Mattermost`` folder, then delete the ``Local Storage`` folder.
- Linux: Open the File Manager, navigate to the ``~/.config/Mattermost`` folder, then delete the ``Local Storage`` folder.
      
Desktop App constantly asks to log in to Mattermost server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This issue can occur after a crash or unexpected shutdown of the desktop app that causes the app data to be corrupted. To resolve the issue:

- Windows: Open Windows File Explorer, navigate to the ``%APPDATA%\\Mattermost`` folder, then delete the ``IndexedDB`` folder and the ``Cookies`` and ``Cookies-journal`` files.
- Mac: Open Finder, navigate to the ``~/Library/Application Support/Mattermost`` folder, then delete the ``IndexedDB`` folder and the ``Cookies`` and ``Cookies-journal`` files.
- Linux: Open the file manager, navigate to the ``~/.config/Mattermost`` folder, then delete the ``IndexedDB`` folder and the ``Cookies`` and ``Cookies-journal`` files.

"Internal error: BrowserWindow 'unresponsive' event has been emitted"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clicking **Show Details** on the dialog provides logs. Ways to resolve the issue:

1. Clear the cache via **View > Clear Cache and Reload** or CTRL+SHIFT+R.
2. Go to App Settings via **File > Settings** or CTRL+COMMA  and unselect hardware acceleration.
  
Desktop app not responsive within Citrix Virtual Apps or Desktop Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Append ``Mattermost.exe;`` to the Registry Key ``HKLM\SYSTEM\CurrentControlSet\Services\CtxUvi\UviProcessExcludes`` and reboot the system.

For further assistance, review the `Troubleshooting forum <https://forum.mattermost.org/c/trouble-shoot>`__ for previously reported errors, or `join the Mattermost user community for troubleshooting help <https://mattermost.com/pl/default-ask-mattermost-community/>`__.

Reporting Issues
----------------

When reporting bugs found in the Mattermost desktop app, it is helpful to include the contents of the Developer Tools Console along with `the information on this page <https://docs.mattermost.com/process/support.html#general-questions-for-any-issues>`__. To access the Developer Tools Console, follow these instructions:

1. In the menu bar, go to **View > Toggle Developer Tools**.
2. Select the **Console** tab.
3. Right-click the log window and select **Save As**.
4. Save the file and then send it along with a description of your issue.
5. Go to **View > Toggle Developer Tools** to disable the Developer Tools.

You can open an additional set of developer tools for each server you have added to the desktop app. The tools can be opened by pasting this command in the Developer Tools Console you opened with the steps described above:

``document.getElementsByTagName("webview")[0].openDevTools();`` 

Note that if you have more than one server added to the desktop client, you need to change the 0 to the number corresponding to the server you want to open in the Developer Tools Console, starting with 0 from the left.

Windows
~~~~~~~

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/jnutU-g2QA8" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

macOS
~~~~~

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/avKDRodDS3s" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

To submit an improvement or correction to this documentation, click **Edit** at the top of this page.
