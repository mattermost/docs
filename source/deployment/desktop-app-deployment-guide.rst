Desktop App Deployment Guide
=========================

Mattermost desktop applications are available for Windows, Mac and Linux operating systems.

You can `download the apps directly from our download page <https://about.mattermost.com/downloads/>`_ and visit our `installation guides <https://docs.mattermost.com/install/desktop.html>`_ for help during setup and for troubleshooting tips.

This page provides a guide on how to distribute the desktop app to users pre-configured with the server URL and other app settings.

Windows
-------------

1. Download the latest Windows installer from the `Mattermost download page <https://about.mattermost.com/download/#mattermostApps>`_.

2. Move the executable file into a shared folder.

// XXX Is this correct?

3. Create a batch file in Windows

  1. Open a text editor of your choice, such as Notepad or Notepad++.
  2. Copy and paste the following commands in the text file

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

// XXX Some admins might not be comfortable giving execute permissions to every user for a shared folder. Might be better to copy the exe to the local computer before running it. That way, the shared folder only needs read-only permissions.
// XXX This means that each user must run the batch file on their local computer, which means you need a step that tells the admin to distribute the batch file.

// XXX The first step installs the Mattermost Desktop App into the user’s local directory. TheUse the ``--silent`` parameter to not automatically launch the app after the installation is completed.
// XXX Step 2 let’s you pre-configure the server URLs, and the app settings. See the `Desktop App User Guide <https://docs.mattermost.com/help/apps/desktop-guide.html#app-options>`_ for more information on the app settings

  3. Save the text file with extension .bat. For instance, mattermost-app-install.bat.
  4. Run the batch file by double-clicking the file in File Explorer.

// XXX You should make it clear that each user has to download and run the batch file themselves. At least, that's the way it's set up here... it can't be used to push the install to multiple users.
// XXX Yes, but I had thought that admin's deployment system should trigger the process...To install the app for other users, zip version of the app should be used. https://forum.mattermost.org/t/mattermost-client-package/2139/2

Once run, the desktop app is added to the user’s local directory, along with the pre-configured config.json file.

// XXX How can the user open the app? By going to the local directory? -- The installer creates a shortcut into user's start menu. If zip version is used, admin needs to create a shortcut manually.
// XXX Will this be added to everyone in that shared folder? -- Sorry, I'm not sure what you mean. What I can say is only that the installer install the app into the user's (who executed the installer) local directory.
