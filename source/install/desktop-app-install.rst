Desktop application install guides
==================================

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

.. |more-icon-vertical| image:: ../images/dots-vertical_F01D9.svg
  :alt: Use the More icon in the top left corner to access Mattermost Desktop Apps customization settings.

The Mattermost Desktop App is available for Windows, Mac, and Linux operating systems. The Desktop App supports all the features of the web experience, plus the following features:

- `Connect to multiple Mattermost servers <https://docs.mattermost.com/welcome/manage-desktop-app-server-connections.html>`__ from a single interface, and navigate between servers using keyboard shortcuts.
- `Auto-start Mattermost <https://docs.mattermost.com/welcome/customize-desktop-app-experience.html>`__ when a user logs into their machine.
- `Add Mattermost <https://docs.mattermost.com/welcome/customize-desktop-app-experience.html>`__ to the Windows Start menu, the Taskbar, the Dock, or the System Tray.
- (Windows/Mac) `Deep link to the Desktop App <https://docs.mattermost.com/welcome/customize-desktop-app-experience.html>`__ via the ``mattermost://`` protocol if the app is already installed.
- (Linux) `Set up Desktop Entry <https://docs.mattermost.com/welcome/customize-desktop-app-experience.html>`__ for the application to more easily `integrate into a desktop environment <https://wiki.archlinux.org/index.php/Desktop_entries>`__.

The following additional documentation resources are also available:

- `Desktop App changelog <https://docs.mattermost.com/install/desktop-app-changelog.html>`__
- `Minimum software requirements <https://docs.mattermost.com/install/software-hardware-requirements.html#desktop-apps>`__
- `Configure your Desktop App experience <https://docs.mattermost.com/welcome/customize-desktop-app-experience.html>`__
- `Source code <https://github.com/mattermost/desktop>`__
- `Contributor’s guide <https://developers.mattermost.com/contribute/desktop>`__

Install the Mattermost Desktop App
----------------------------------

You can `download the Desktop App directly from our Downloads page <https://mattermost.com/download/>`__. You may also use the following installation guides for Linux, Mac, and Windows.

.. include:: ../upgrade/upgrading-to-v60.rst
  :start-after: :nosearch:

.. tabs::

  .. tab:: Linux

    **Generic Linux package** 

    1. Download the latest version of the Mattermost desktop app:

      - 64-bit systems: `mattermost-desktop-5.0.4-linux-x64.tar.gz <https://releases.mattermost.com/desktop/5.0.4/mattermost-desktop-5.0.4-linux-x64.tar.gz>`__
      - 32-bit systems: `mattermost-desktop-5.0.4-linux-ia32.tar.gz <https://releases.mattermost.com/desktop/5.0.4/mattermost-desktop-5.0.4-linux-ia32.tar.gz>`__

    2. Extract the archive to a convenient location, then execute ``mattermost-desktop`` located inside the extracted directory.

    3. To create a Desktop launcher, open the file **README.md** and follow the instructions in the **Desktop launcher** section.

    **Ubuntu and Debian-based systems**

    Unofficial, community-driven ``.deb`` packages are available.

    1. Download the latest version of the Mattermost Desktop App:

      - 64-bit systems `mattermost-desktop-5.0.4-linux-amd64.deb <https://releases.mattermost.com/desktop/5.0.4/mattermost-desktop-5.0.4-linux-amd64.deb>`__
      - 32-bit systems `mattermost-desktop-5.0.4-linux-i386.deb <https://releases.mattermost.com/desktop/5.0.4/mattermost-desktop-5.0.4-linux-i386.deb>`__

    2. At the command line, execute one of the following commands depending on the package that you downloaded:

      - 64-bit systems ``sudo dpkg -i mattermost-desktop-5.0.4-linux-amd64.deb``
      - 32-bit systems ``sudo dpkg -i mattermost-desktop-5.0.4-linux-i386.deb``

    3. Run Mattermost as a desktop app.

    **Linux rpm files (Beta)**

    Unofficial, community-driven ``.rpm`` packages are available.

    1. Download the latest version of the Mattermost Desktop App:

      - 32-bit systems `mattermost-desktop-5.0.4-linux-i686.rpm <https://releases.mattermost.com/desktop/5.0.4/mattermost-desktop-5.0.4-linux-i686.rpm>`__
      - 64-bit systems `mattermost-desktop-5.0.4-linux-x86_64.rpm <https://releases.mattermost.com/desktop/5.0.4/mattermost-desktop-5.0.4-linux-x86_64.rpm>`__

    2. At the command line, execute one of the following commands based on the package you downloaded:

      - 32-bit systems ``sudo rpm -i mattermost-desktop-5.0.4-linux-i686.rpm``
      - 64-bit systems ``sudo rpm -i mattermost-desktop-5.0.4-linux-x86_64.rpm``

    3. Run Mattermost as a desktop app.

    **Arch Linux-based systems**

    To install the Desktop client on Arch Linux, see the `Mattermost page <https://wiki.archlinux.org/index.php/Mattermost>`__ on the Arch Linux wiki.

    **Snapcraft package**

    A snap is available for systems that have Snapcraft installed. Snapcraft is installed by default on Ubuntu 16.04 and later, but for most other Linux distributions you can install it manually. To install Snapcraft, see `Install snapd <https://snapcraft.io/docs/core/install>`__ on the Snapcraft website.

    1. At the command line, execute the following command: ``sudo snap install mattermost-desktop --beta``

    2. Run Mattermost as a desktop app.

  .. tab:: Mac 10.9+

    1. Download the latest version of the Mattermost desktop app:
      
      - `Intel systems <https://releases.mattermost.com/desktop/5.0.4/mattermost-desktop-5.0.4-mac-x64.dmg>`__
      - `M1 systems <https://releases.mattermost.com/desktop/5.0.4/mattermost-desktop-5.0.4-mac-m1.dmg>`__ (Beta)

    2. Double-click the download to open the disk image.

    3. Drag the Mattermost application to the **Applications** folder.

    .. tip::
      
      `Homebrew <https://brew.sh>`__ users can install with ``brew install --cask mattermost``.

  .. tab:: Windows 8.1+

    1. Download the latest version of the Mattermost desktop app: `32/64-bit version of Windows <https://releases.mattermost.com/desktop/5.0.4/mattermost-desktop-setup-5.0.4-win.exe>`__

    2. From the **\Downloads** folder, right-click on the file ``mattermost-desktop-setup-5.0.4-win.exe`` and select **Open** to start an installer for the app. Once finished, the Mattermost desktop app opens automatically.

    **MSI Installer and Group Policies (Beta)**

    You can download the latest version of the Mattermost Desktop App MSI installer (Beta):

    - MSI for `64-bit version of Windows <https://releases.mattermost.com/desktop/5.0.4/mattermost-desktop-5.0.4-x64.msi>`__
    - MSI for `32-bit version of Windows <https://releases.mattermost.com/desktop/5.0.4/mattermost-desktop-5.0.4-x86.msi>`__

    See the `MSI installer and group policy documentation <https://docs.mattermost.com/install/desktop-msi-gpo.html>`__ for instructions on installing the Mattermost Desktop App via an MSI installer and configuring supported group policies. Changes to group policies require you to restart Mattermost for those changes to take effect.

    The following group policies are available:

    +----------------------------+-----------------------------------------------------------------------------+---------------------------------+
    | Group policy               | Description                                                                 | Required Mattermost version     |
    +============================+=============================================================================+=================================+
    | Enable Server Management   | If disabled, management of servers in the app settings are disabled.        | 4.3 or later                    |
    +----------------------------+-----------------------------------------------------------------------------+---------------------------------+
    | Default Server List        | Define one or more default, permanent servers.                              | 4.3 or later                    |
    +----------------------------+-----------------------------------------------------------------------------+---------------------------------+

Update the Mattermost Desktop App
---------------------------------

For the best experience, we recommend keeping your Desktop App updated to the latest release. 

.. tabs::

  .. tab:: Linux

    Depending on the distribution you're using, your Desktop App updates automatically when a new release is available.

    - Ubuntu: A Debian repository is available to configure and install. TBD
    - RedHat: An RPM repo is in progress. TBD
    - All others: An unofficial AppImage distribution supports automatic updates.

    **Check your Desktop App version**

    Select the **More** |more-icon-vertical| icon located in the top left corner of the Mattermost window, then select **Help > Version...**.

    **Manually check for updates**

    1. Select the **More** |more-icon-vertical| icon located in the top left corner of the Mattermost window, then select **File > Settings...**.
    2. Select **Check for updates**.

    If a newer release of the Desktop App is available, you're prompted to install it.

  .. tab:: Mac 10.9+

    You have two ways to install the Desktop App, and how you install the app determines whether it updates automatically.
    
    - You can install the Desktop App from the `App Store <https://apps.apple.com/us/app/mattermost/id1257222717>`__. When you install through the App Store, your Desktop App updates automatically when a new release is available.
    - You can `download the Desktop App directly from our GitHub release page <https://github.com/mattermost/desktop/releases>`__. However, when you install the Desktop App this way, you can't manually check for updates, and updates won't be installed automatically.

    **Check your Desktop App version**

    Select **Mattermost > About Mattermost** from the menu bar. This dialog indicates when you've downloaded the app from the App Store.

  .. tab:: Windows 8.1+

    Your Desktop App updates automatically when a new release is available. You can check for updates manually any time.

    **Manually check for updates**

    1. Select the **More** |more-icon-vertical| icon located in the top left corner of the Mattermost window, then select **File > Settings...**.
    2. Select **Check for updates**.
    
    If a newer release of the Desktop App is available, you're prompted to install it.






Troubleshooting your Desktop App installation
----------------------------------------------

"Installation has failed" dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The app data might be corrupted. Remove all the files in ``%LOCALAPPDATA%\mattermost``, then try reinstalling the app.
    
"The application "Mattermost" can't be opened" dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On macOS Catalina, this dialog can be triggered if the Mac Archive Utility is the default method for decompressing files. In this case using a third-party tool such as `Keka <https://www.keka.io>`__ or `Unarchiver <https://macpaw.com/the-unarchiver>`__ may resolve the problem.

Desktop App window is black and doesn't load the page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. First, make sure you have installed the latest desktop app version.
2. Clear your cache and reload the app from **View > Clear Cache and Reload** or use CTRL/CMD+SHIFT+R.
3. Quit the app and restart it to see if the issue clears.
4. Disable GPU hardware acceleration from **File > Settings** on Windows and Linux or **Mattermost > Settings** on macOS, and unselect **Use GPU hardware acceleration**.
5. If you are using a special video driver, such as Optimus, try disabling it to see if the problem is resolved.

If none of the above steps resolve the issue, please open a new ticket in the `Mattermost Troubleshooting Forum <https://forum.mattermost.com/t/how-to-use-the-troubleshooting-forum/150>`__.

Desktop App is not visible, but the Mattermost icon is in the Task Bar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This issue can occur on Windows in a multiple-monitor setup. When you disconnect the monitor that Mattermost is displayed on, Mattermost continues to display at screen coordinates that no longer exist.

To resolve this issue, you can reset the desktop app screen location by deleting the screen location file. When the file is not present, the desktop app displays on the primary monitor by default.

To reset the desktop app screen location:

1. If the desktop app is running, right-click the Mattermost icon in the task bar, then select **Close Window**.
2. Open Windows File Explorer, and go to the ``%APPDATA%\\Mattermost`` folder.
3. Delete the file ``bounds-info.json``.

Desktop App constantly refreshes the page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This issue can occur when ``localStorage`` has an unexpected state. To resolve the issue:

- Windows: Open Windows File Explorer, go to the ``%APPDATA%\Mattermost`` folder, then delete the ``Local Storage`` folder.
- Mac: Open Finder, go to the ``~/Library/Application Support/Mattermost`` folder, then delete the ``Local Storage`` folder.
- Linux: Open the File Manager, go to the ``~/.config/Mattermost`` folder, then delete the ``Local Storage`` folder. Linux file managers may hide folders starting with a period by default. You can delete them from the terminal using ``rm -rf ~/.config/Mattermost``.
      
Desktop App constantly asks to log in to Mattermost server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This issue can occur after a crash or unexpected shutdown of the desktop app that causes the app data to be corrupted. To resolve the issue:

- Windows: Open Windows File Explorer, go to the ``%APPDATA%\\Mattermost`` folder, then delete the ``IndexedDB`` folder and the ``Cookies`` and ``Cookies-journal`` files.
- Mac: Open Finder, go to the ``~/Library/Application Support/Mattermost`` folder, then delete the ``IndexedDB`` folder and the ``Cookies`` and ``Cookies-journal`` files.
- Linux: Open the file manager, go to the ``~/.config/Mattermost`` folder, then delete the ``IndexedDB`` folder and the ``Cookies`` and ``Cookies-journal`` files. Linux file managers may hide folders starting with a period by default. You can delete them from the terminal using ``rm -rf ~/.config/Mattermost``.

"Internal error: BrowserWindow 'unresponsive' event has been emitted"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Selecting **Show Details** on the dialog provides logs. Ways to resolve the issue:

1. Clear the cache via **View > Clear Cache and Reload** or CTRL+SHIFT+R.
2. Go to App Settings via **File > Settings** or CTRL+COMMA  and unselect hardware acceleration.
  
Desktop app not responsive within Citrix Virtual Apps or Desktop Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Append ``Mattermost.exe;`` to the Registry Key ``HKLM\SYSTEM\CurrentControlSet\Services\CtxUvi\UviProcessExcludes`` and reboot the system.

For further assistance, review the `Troubleshooting forum <https://forum.mattermost.com/c/trouble-shoot>`__ for previously reported errors, or `join the Mattermost user community for troubleshooting help <https://mattermost.com/pl/default-ask-mattermost-community/>`__.

Report Desktop App Issues
-------------------------

When reporting issues found in the Mattermost Desktop App, it's helpful to include the contents of the Developer Tools Console along with `the information on this page <https://support.mattermost.com/hc/en-us/articles/360060662492-Opening-a-Support-Ticket-for-Self-Managed-Deployments>`__. 

To access the Developer Tools Console:

1. In the menu bar, go to **View > Developer Tools for Current Tab**.
2. Select the **Console** tab.
3. Right-click the log entry, then select **Save As**.
4. Save the file, then send it along with a description of your issue.
5. Close the console to disable the Developer Tools.

You can open an additional set of developer tools for each server you have added to the desktop app. The tools can be opened by pasting this command in the Developer Tools Console you opened with the steps described above:

``document.getElementsByTagName("webview")[0].openDevTools();`` 

Windows
~~~~~~~

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/jnutU-g2QA8" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

macOS
~~~~~

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/avKDRodDS3s" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

To submit an improvement or correction to this documentation, select **Edit** at the top of this page.
