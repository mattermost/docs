Additional desktop app installations
====================================

This page describes additional ways to install the Mattermost desktop app.

.. tab:: Windows

  Windows 10+ is required. Automatic app updates are supported and enabled. When a new version of the desktop app is released, your app updates automatically.

  **Install the Mattermost Desktop App**

    1. Download the latest version of the Mattermost desktop app for the `64-bit version of Windows <https://releases.mattermost.com/desktop/5.11.2/mattermost-desktop-5.11.2-win-x64.msi>`_
    2. From the **\Downloads** folder, right-click on the file ``mattermost-desktop-setup-5.11.2-win.exe``, then select **Open** to start an installer for the app. Once finished, the Mattermost desktop app opens automatically.

  .. warning:: 
    Mattermost Desktop should always be installed on a local drive. Network Shares are not supported as installation locations.

  **MSI Installer and group policies**

  The following group policies are available supporting a state option of Not Configured, Enabled, or Disabled:

  +--------------------------+------------------------------------------------------------+----------------------+----------------------------+
  | Group policy             | Description                                                | Mattermost release   | Setting                    |
  +==========================+============================================================+======================+============================+
  | Enable Server Management | If disabled, management of servers in the                  | v4.3 or later        | ``EnableServerManagement`` |
  |                          | app settings are disabled.                                 |                      |                            |
  +--------------------------+------------------------------------------------------------+----------------------+----------------------------+
  | Default Server List      | Define one or more default, permanent servers.             | v4.3 or later        | ``DefaultServerList``      |
  +--------------------------+------------------------------------------------------------+----------------------+----------------------------+
  | Automatic Updates        | If disabled, automatic desktop app updates are disabled.   | v5.1 or later        | ``EnableAutoUpdates``      |
  +--------------------------+------------------------------------------------------------+----------------------+----------------------------+

  **Disable automatic updates**
  
  Automatic desktop app updates can be disabled by configuring the supported group policy. See the :doc:`MSI installer and group policy documentation </install/desktop-msi-installer-and-group-policy-install>` for instructions on installing the Mattermost Desktop App via an MSI installer, configuring supported group policies, and performing silent MSI installations. Changes to group policies require you to restart Mattermost for those changes to take effect.

.. tab:: macOS

  MacOS 11+ is required. You have two ways to install the desktop app, and how you install the app determines whether it updates automatically.

  **Install from the App Store**

  We recommend that you install the desktop app from the `App Store <https://apps.apple.com/us/app/mattermost-desktop/id1614666244?mt=12>`_. When you install through the App Store, your desktop app updates automatically when a new release is available.

  **Download the Desktop App from GitHub**

  You can download the `desktop app <https://mattermost.com/apps/>`_ directly from the Downloads page. However, when you install the desktop app this way, you can't manually check for updates, and updates won't be installed automatically.
  
  1. Download the latest version of the Mattermost desktop app:
          
     - `Intel systems <https://releases.mattermost.com/desktop/5.11.2/mattermost-desktop-5.11.2-mac-x64.dmg>`_
     - `M1 systems <https://releases.mattermost.com/desktop/5.11.2/mattermost-desktop-5.11.2-mac-m1.dmg>`_ (Beta)

  2. Double-click the download to open the disk image.

  3. Drag the Mattermost application to the **Applications** folder.

  .. tip:: 
    You can review the current version of your desktop app by selecting **Mattermost > About Mattermost** from the macOS menu bar. 

.. tab:: Ubuntu/Debian

  Both a ``.deb`` package (Beta), and an official APT repository is available for Debian 9 and for Ubuntu releases 20.04 LTS or later. Automatic app updates are supported and enabled. When a new version of the desktop app is released, your app updates automatically.

  .. important::

    The GPG public key has changed. If you had previously set up the repository on your system, you'll need to download the new key. You can set the ``UPDATE_GPG_KEY=yes`` environment variable when running the setup script to configure it to overwrite the previous key on your system with the new one. The first step of installation then becomes: ``curl -fsS -o- https://deb.packages.mattermost.com/setup-repo.sh | sudo UPDATE_GPG_KEY=yes bash``. Depending on your setup, additional steps may also be required, particularly for installations that don't rely on the repository setup script.

  1. At the command line, set up the Mattermost repository on your system: 

    .. code-block:: sh

      curl -fsS -o- https://deb.packages.mattermost.com/setup-repo.sh | sudo bash

  2. Install the Mattermost desktop app: 
  
    .. code-block:: sh

      sudo apt install mattermost-desktop

  3. Update the Mattermost desktop app: 
  
    .. code-block:: sh

      sudo apt upgrade mattermost-desktop

  **Snapcraft package**

  A snap is available for systems that have Snapcraft installed. Snapcraft is installed by default on Ubuntu 16.04 and later, but for most other Linux distributions you can install it manually. To install Snapcraft, see `Install snapd <https://snapcraft.io/docs/installing-snapd>`_ on the Snapcraft website for details.

  1. At the command line, execute the following command: 
  
    .. code-block:: sh

      sudo snap install mattermost-desktop --beta

  2. Run Mattermost as a desktop app.

  .. tip:: 
    You can review the current version of your desktop app by selecting the **More** |more-icon-vertical| icon located in the top left corner of the desktop app, then selecting **Help > Version...**.

.. tab:: CentOS/RHEL

  Beta ``.rpm`` packages are available for CentOS and RHEL 7 and 8. Automatic app updates aren't supported. You must update your app manually.

  **Install the Mattermost Desktop App**

  1. Download the latest version of the Mattermost desktop app for 64-bit systems: `mattermost-desktop-5.11.2-linux-x86_64.rpm <https://releases.mattermost.com/desktop/5.11.2/mattermost-desktop-5.11.2-linux-x86_64.rpm>`_

  2. At the command line, execute the following command:
    
    .. code-block:: sh

      sudo rpm -i mattermost-desktop-5.11.2-linux-x86_64.rpm

  3. Run Mattermost as a desktop app.

  To manually update the desktop app, run the following command:
  
    .. code-block:: sh

      sudo rpm -u mattermost-desktop-5.11.2-linux-x86_64.rpm

  .. tip:: 
    You can review the current version of your desktop app by selecting the **More** |more-icon-vertical| icon located in the top left corner of the desktop app, then selecting **Help > Version...**.

.. tab:: Generic Linux

  The Desktop app is available in two formats which are usable on most Linux distributions: a compressed tarball, and an AppImage binary. Both can be downloaded from the `Desktop App's Github releases page <https://github.com/mattermost/desktop/releases>`_. Automatic app updates are supported and enabled on AppImage binary builds. When a new version of the desktop app is released, your app updates automatically.

  For instructions on how to use the AppImage binary, please refer to the  `AppImage Quickstart documentation page <https://docs.appimage.org/introduction/quickstart.html>`_.

  **Install the Desktop App's compressed tarball**

  1. Download the latest version of the Mattermost desktop app for 64-bit systems: `mattermost-desktop-5.11.2-linux-x64.tar.gz <https://releases.mattermost.com/desktop/5.11.2/mattermost-desktop-5.11.2-linux-x64.tar.gz>`_

  2. Extract the archive to a convenient location, then give ``chrome-sandbox`` in the extracted directory the required ownership and permissions: ``sudo chown root:root chrome-sandbox && sudo chmod 4755 chrome-sandbox``

  3. Execute ``mattermost-desktop`` located inside the extracted directory.

  4. To create a Desktop launcher, open the file ``README.md``, and follow the instructions in the **Desktop launcher** section.