Desktop App Deployment Guide
=============================

Mattermost desktop applications are available for Windows, Mac and Linux operating systems.

You can `download the apps directly from our download page <https://about.mattermost.com/downloads/>`_ and visit our `installation guides <https://docs.mattermost.com/install/desktop.html>`_ for help during setup and for troubleshooting tips.

This page provides a guide on how to 

 - `customize and distribute your own Mattermost Desktop App <XXX>`_
 - `distribute the official Windows Desktop App silently to end users, pre-configured with the server URL and other app settings <XXX>`_

Custom Build Configuration
---------------------------

You can customize and distribute your own Mattermost Desktop application by configuring `src/common/config/buildConfig.js <https://github.com/mattermost/desktop/blob/master/src/common/config/buildConfig.js>`_.

1. Configure the Desktop App's `buildConfig.js` file. There are multiple parameters you can configure to customize the user experience:

`defaultTeams`
~~~~~~~~~~~~~~~~

  Description
    List of server URLs and their display names added to the desktop app by default, which the user cannot modify. Users can still add servers `through the Server Management page <https://docs.mattermost.com/help/apps/desktop-guide.html#server-management>`_ unless ``enableServerManagement`` is set to false. 
    
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

`helpLink`
~~~~~~~~~~~~~~~~

  Description
    The URL of the help documentation in Help > Learn More menu bar item. If none specified, the menu option is hidden.
    
    Expects a string.

  Examples
    .. code-block:: none

      helpLink: 'https://about.mattermost.com/default-desktop-app-documentation/'
      helpLink: ''

`enableServerManagement`
~~~~~~~~~~~~~~~~~~~~~~~~~

  Description
    Controls whether users can add, edit or remove servers on the app settings page. If set to false, at least one server must be specified for ``defaultTeams`` or else users cannot interact with any servers.
    
    Expects a boolean, true or false.

  Examples
    .. code-block:: none

      enableServerManagement: true

2. To build the application, follow the `Mattermost Desktop Development Guide <https://github.com/yuya-oc/desktop/blob/master/docs/development.md>`_.

Windows App: Pre-Configuration and Silent Deployment
------------------------------------------------------

You can distribute the official Windows Desktop App silently to end users, pre-configured with the server URL and other app settings.

1. Download the latest Windows installer from the `Mattermost download page <https://about.mattermost.com/download/#mattermostApps>`_.

2. Move the executable file into a shared folder.

3. To create a batch file in Windows:

  1. Open a text editor of your choice, such as Notepad or Notepad++.
  2. Copy and paste the following commands in the text file:

    .. code-block:: none


      rem "Step 1: Install mattermost desktop into user's local disk"
      start /wait \\SERVER\shared_folder\mattermost-setup-3.7.0-win64.exe --silent

      rem "Step 2: Generate initial config.json into user's config directory"
      (
        echo {
        echo   "version": 1,
        echo   "teams": [
        echo     {
        echo       "name": "pre-release",
        echo       "url": "https://pre-release.mattermost.com/core"
        echo     }
        echo   ],
        echo   "notifications": {
        echo     "flashWindow": 1
        echo   },
        echo   "useSpellChecker": true
        echo   "showUnreadBadge": true
        echo }
      ) > %APPDATA%\Mattermost\config.json

  3. Save the text file with extension .bat. For instance, mattermost-app-install.bat.
  4. Run the batch file by double-clicking the file in File Explorer.

Once run, the desktop app is added to the user’s local directory, along with the pre-configured config.json file.
