Desktop App Deployment Guide
=============================

Mattermost desktop applications are available for Windows, macOS, and Linux operating systems.

You can `download the apps directly from our download page <https://mattermost.com/download/#mattermostApps>`__ and visit our `installation guides <https://docs.mattermost.com/install/desktop.html>`__ for help during setup and for troubleshooting tips.

This page provides a guide on how to customize and distribute your own Mattermost Desktop App, and how to distribute the official Windows Desktop App silently to end users, pre-configured with the server URL and other app settings.

.. contents::
  :depth: 1
  :local:
  :backlinks: entry

Custom Build Configuration
--------------------------

You can customize and distribute your own Mattermost Desktop application by configuring `src/common/config/buildConfig.js <https://github.com/mattermost/desktop/blob/master/src/common/config/buildConfig.js>`__.

1. Configure the Desktop App's ``buildConfig.js`` file. There are multiple parameters you can configure to customize the user experience:

``defaultTeams``
~~~~~~~~~~~~~~~~

  Description
    List of server URLs and their display names added to the desktop app by default, which the user cannot modify. Users can still add servers `through the Server Management page <https://docs.mattermost.com/deploy/desktop-app.html#enableservermanagement>`__ unless ``enableServerManagement`` is set to ``false``. 
    
    Expects an array of key-value pairs.

  Example
  
.. code-block:: none

      defaultTeams: [
        {
          name: 'example',
          url: 'https://example.com'
        },
        {
          name: 'mattermost',
          url: 'https://www.mattermost.com'
        }
      ]

``helpLink``
~~~~~~~~~~~~

  Description
    The URL of the help documentation in **Help > Learn More** menu bar item. If none is specified, the menu option is hidden.
    
    Expects a string.

  Examples

.. code-block:: none

      helpLink: 'https://about.mattermost.com/default-desktop-app-documentation/'
      helpLink: ''

``enableServerManagement``
~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Controls whether users can add, edit, or remove servers on the app settings page. If set to false, at least one server must be specified for ``defaultTeams`` or else users cannot interact with any servers.
    
    Expects a boolean, true or false.

  Examples

.. code-block:: none

      enableServerManagement: true

2. To build the application, follow the `Mattermost Desktop Development Guide <https://github.com/mattermost/desktop/blob/master/docs/development.md>`__.

Windows App: Pre-Configuration and Silent Deployment
-----------------------------------------------------

You can distribute the official Windows Desktop App silently to end users, pre-configured with the server URL. You can also set all the `app settings <https://docs.mattermost.com/messaging/managing-desktop-app-options.html>`__ except for the **Start app on login** option.

1. Download the latest Windows installer from the `Mattermost download page <https://mattermost.com/download/#mattermostApps>`__.

2. Move the executable file into a shared place such as a file server.

3. To create a batch file in Windows:

  - Open a text editor of your choice, such as Notepad or Notepad++.
  - Copy and paste the following commands in the text file:

.. code-block:: none

      rem "Step 1: Install Mattermost Desktop App silently into user's local disk"
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

.. note::

  Instead of using this command to install the Desktop App into a shared folder, you can also copy the executable to the folder before running it. This allows the shared folder to only require read-only permissions.

4. Save the text file with the extension ``.bat``. For instance, ``mattermost-app-install.bat``.
5. Use standard software asset management tools to distribute and deploy the batch file to each user.

Once run, the Desktop App is added to the user’s local directory, along with the pre-configured ``config.json`` file. The installer creates a shortcut for the Desktop App in the user's start menu; if a zip version is used, you need to create the shortcut manually.

Windows App: Silently Removing the App
---------------------------------------

To remove the app silently from a user's computer, you can run the following command:

.. code-block:: none
  
  %userprofile%\AppData\local\Programs\mattermost-desktop\Uninstall Mattermost.exe /currentuser /S
    
.. note::
   The .exe needs to be closed when this command is run
 
