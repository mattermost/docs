Silent Windows desktop distribution
=====================================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

You can distribute the official Windows desktop app silently to end users, pre-configured with the server URL. Additionally, you can customize all of the :doc:`desktop app settings </end-user-guide/preferences/customize-desktop-app-experience>`, except the **Start app on login** option.

.. tip::

  Want to :ref:`perform a silent installation of the desktop app MSI <deployment-guide/desktop/desktop-msi-installer-and-group-policy-install:silent installation>` instead? 

1. Download the latest Windows installer from the `Mattermost download page <https://mattermost.com/apps>`__.

2. Move the executable file into a shared place such as a file server.

3. To create a batch file in Windows:

  - Open a text editor of your choice, such as Notepad or Notepad++.
  - Copy and paste the following commands in the text file:

    .. code-block:: text

          rem "Step 1: Install Mattermost desktop app silently into user's local disk"
          start \\SERVER\shared_folder\mattermost-setup-4.6.2-win.exe --silent

          if not exist "%APPDATA%\Mattermost" mkdir %APPDATA%\Mattermost

          rem "Step 2: Generate initial config.json into user's config directory"
          (
            echo {
            echo   "version": 2,
            echo   "teams": [
            echo     {
            echo       "name": "core",
            echo       "url": "https://community.mattermost.com",
            echo       "order": 0
            echo     },
            echo     {
            echo       "name": "hq",
            echo       "url": "https://hq.example.com",
            echo       "order": 1
            echo     }
            echo   ],
            echo   "showTrayIcon": true,
            echo   "trayIconTheme": "light",
            echo   "minimizeToTray": true,
            echo   "notifications": {
            echo     "flashWindow": 2,
            echo     "bounceIcon": true,
            echo     "bounceIconType": "informational"
            echo   },
            echo   "showUnreadBadge": true,
            echo   "useSpellChecker": true,
            echo   "enableHardwareAcceleration": true,
            echo   "autostart": true,
            echo   "spellCheckerLocale": "en-US",
            echo   "darkMode": false
            echo }
          ) > %APPDATA%\Mattermost\config.json

4. Save the text file with the extension ``.bat``. For instance, ``mattermost-app-install.bat``.
5. Use standard software asset management tools to distribute and deploy the batch file to each user.

Once run, the desktop app is added to the user’s local directory, along with the pre-configured ``config.json`` file. The installer creates a shortcut for the desktop app in the user's start menu; if a zip version is used, you need to create the shortcut manually.

.. tip::

  You can copy the executable to the folder before running it instead of using this command to install the desktop app into a shared folder. This allows the shared folder to only require read-only permissions.

Windows App: Silently removing the app
---------------------------------------

To remove the app silently from a user's computer, you can run the following command with the .exe file closed:

.. code-block:: text

  %userprofile%\AppData\local\Programs\mattermost-desktop\Uninstall Mattermost.exe /currentuser /S