Desktop App deployment guide
=============================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Mattermost desktop applications are available for Windows, macOS, and Linux operating systems.

You can `download the apps directly from our download page <https://mattermost.com/apps>`__ and visit our :doc:`installation guides </collaborate/install-desktop-app>` for help during setup and for troubleshooting tips.

This page provides a guide on how to customize and distribute your own Mattermost desktop app, and how to distribute the official Windows desktop app silently to end users, pre-configured with the server URL and other app settings.

Custom build configuration
--------------------------

You can customize and distribute your own Mattermost desktop application by configuring `src/common/config/buildConfig.ts <https://github.com/mattermost/desktop/blob/master/src/common/config/buildConfig.ts>`__.

1. Configure the desktop app's ``buildConfig.ts`` file. There are multiple parameters you can configure to customize the user experience:

``defaultTeams``
~~~~~~~~~~~~~~~~

  Description
    List of server URLs and their display names added to the desktop app by default, which the user cannot modify. Users can still add servers `through the Server Management page <#enableservermanagement>`_ unless ``enableServerManagement`` is set to ``false``. 
    
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

      helpLink: 'https://docs.mattermost.com/messaging/managing-desktop-app-servers.html'
      helpLink: ''

``enableServerManagement``
~~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Controls whether users can add, edit, or remove servers on the app settings page. If set to false, at least one server must be specified for ``defaultTeams`` or else users cannot interact with any servers.
    
    Expects a boolean, true or false.

  Examples

.. code-block:: none

      enableServerManagement: true

2. To build the application, follow the `Mattermost Desktop Development Guide <https://developers.mattermost.com/contribute/more-info/desktop/developer-setup/>`__.

Windows App: Pre-configuration and silent deployment
-----------------------------------------------------

You can distribute the official Windows desktop app silently to end users, pre-configured with the server URL. You can also set all the :doc:`app settings </preferences/customize-desktop-app-experience>` except for the **Start app on login** option.

1. Download the latest Windows installer from the `Mattermost download page <https://mattermost.com/apps>`__.

2. Move the executable file into a shared place such as a file server.

3. To create a batch file in Windows:

  - Open a text editor of your choice, such as Notepad or Notepad++.
  - Copy and paste the following commands in the text file:

.. code-block:: none

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

  Instead of using this command to install the desktop app into a shared folder, you can also copy the executable to the folder before running it. This allows the shared folder to only require read-only permissions.

4. Save the text file with the extension ``.bat``. For instance, ``mattermost-app-install.bat``.
5. Use standard software asset management tools to distribute and deploy the batch file to each user.

Once run, the desktop app is added to the user’s local directory, along with the pre-configured ``config.json`` file. The installer creates a shortcut for the desktop app in the user's start menu; if a zip version is used, you need to create the shortcut manually.

Windows App: Silently removing the app
---------------------------------------

To remove the app silently from a user's computer, you can run the following command:

.. code-block:: none
  
  %userprofile%\AppData\local\Programs\mattermost-desktop\Uninstall Mattermost.exe /currentuser /S
    
.. note::
   The .exe needs to be closed when this command is run
 
