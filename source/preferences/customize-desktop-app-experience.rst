Customize your Desktop App experience
=====================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |more-icon-vertical| image:: ../images/dots-vertical_F01D9.svg
  :alt: Use the More icon in the top left corner to access Mattermost Desktop Apps customization settings.

Additional customization options are available to you when using the Mattermost desktop app.

.. tabs::

    .. tab:: Linux

        `Install the Mattermost desktop app </collaborate/install-desktop-app.html#install-and-update-the-mattermost-desktop-app>`__ to access additional desktop app customization settings. Select **File > Settings...** from the **More** |more-icon-vertical| icon located in the top left corner of the desktop app. 

        .. image:: ../images/desktop-app-settings.jpg
            :alt: Access Desktop App customization settings by selecting More in the top left corner, then selecting File > Settings.

        +----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | **Desktop App setting**                                                    | **Description**                                                                                                                            |
        +============================================================================+============================================================================================================================================+
        | Start app on login                                                         | The Mattermost Desktop App starts up automatically when you log in to your machine.                                                        |
        |                                                                            | You can configure the Desktop App not to launch automatically when you log in to your machine.                                             |
        +----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | Launch app minimized                                                       | You can configure the Mattermost Desktop App to launch minimized in the system tray.                                                       |
        +----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | Check spelling                                                             | Misspelled words in your messages are highlighted based on the system language. You can disable spell check.                               |
        |                                                                            |                                                                                                                                            |
        |                                                                            | You can also specify additional spell check languages. You must restart the app to change this setting.                                    |
        |                                                                            | When multiple languages are configured:                                                                                                    |
        |                                                                            |                                                                                                                                            |
        |                                                                            | - All selected languages show as correct when a word matches at least one selected language.                                               |
        |                                                                            | - All selected languages show as incorrect when a word matches none of the languages.                                                      |
        +----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | Use an alternative dictionary URL                                          | You can specify an alternate dictionary for spell check as a site URL.                                                                     |
        +----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | Flash taskbar icon when a new message is received                          | Your taskbar icon flashes when a new message is received on any of your active teams and servers.                                          |
        |                                                                            | You can disable the flashing taskbar icon.                                                                                                 |
        +----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | Show icon in the notification area                                         | The Mattermost icon displays in the notification area. You can hide this icon.                                                             |
        |                                                                            | You must restart the app to change this setting.                                                                                           |
        +----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | Icon theme                                                                 | The default icon theme is based on the system preferences appearance setting.                                                              |
        |                                                                            | You can choose to display a light or dark-themed icon.                                                                                     |
        +----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | Leave app running in notification center when application window is closed | When you close the Mattermost Desktop App, you're prompted to confirm whether you want to permanently close the app.                       |
        |                                                                            | You can disable this confirmation or silence it by selecting **Don't ask again**.                                                          |
        |                                                                            | You can also configure the app to continue running after the window is closed.                                                             |
        |                                                                            | To silence the notifications, select **Don't show again**.                                                                                 |
        +----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | Use GPU hardware acceleration                                              | GPU hardware acceleration renders the Mattermost Desktop App interface more efficiently.                                                   |
        |                                                                            | If you encounter decreased stability, you can disable GPU hardware acceleration. You must restart the app to change this setting.          |
        +----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | Open app in fullscreen                                                     | You can configure the Mattermost Desktop App to open in fullscreen mode.                                                                   |
        |                                                                            | You can also toggle this setting using the following CLI command:                                                                          |
        |                                                                            |                                                                                                                                            |
        |                                                                            | ``open release/mac/Mattermost.app --args --fullscreen true`` or ``open release/mac/Mattermost.app --args -f true``                         |
        +----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | Download location                                                          | Specify where you want files to be downloaded on your machine.                                                                             |
        +----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
        | Logging level                                                              | You can adjust logging levels to isolate and troubleshoot issues.                                                                          |  
        |                                                                            | Increasing the log level increases disk space usage and can impact performance.                                                            |
        +----------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+    

    .. tab:: Mac

        When you `install the Mattermost desktop app </collaborate/install-desktop-app.html#install-and-update-the-mattermost-desktop-app>`__, you can access additional Desktop App customization settings by selecting **Mattermost > Preferences** from the menu bar.

        .. image:: ../images/mac-desktop-app-settings.png
            :alt: Access Desktop App customization settings by selecting Mattermost from the menu bar, then selecting Preferences.

        +---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
        | **Desktop App setting**                                 | **Description**                                                                                                                                          |
        +=========================================================+==========================================================================================================================================================+
        | Check spelling                                          | Misspelled words in your messages are highlighted based on the system language. You can disable spell check.                                             |
        |                                                         |                                                                                                                                                          |
        |                                                         | You can also specify additional spell check languages. You must restart the app to change this setting.                                                  |
        |                                                         | When multiple languages are configured:                                                                                                                  |
        |                                                         |                                                                                                                                                          |
        |                                                         | - All selected languages show as correct when a word matches at least one selected language.                                                             |
        |                                                         | - All selected languages show as incorrect when a word matches none of the languages.                                                                    |
        +---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Show red badge on Dock icon to indicate unread messages | A red badge on the Dock icon displays a count of unread messages and mentions.                                                                           |
        |                                                         | You can configure the Mattermost Desktop App to display a count of mentions only.                                                                        |
        +---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Bounce the Dock icon                                    | When a new message is received on any of your active teams and servers, the Dock icon bounces once or bounces until you open the Mattermost Desktop App. |
        |                                                         | You can configure the Mattermost Desktop App Dock icon to bounce more, less, or not at all.                                                              |
        +---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Show Mattermost icon in the menu bar                    | The Mattermost icon displays in the notification area.                                                                                                   |
        |                                                         | You can hide this icon. You must restart the app to change this setting.                                                                                 |
        +---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Use GPU hardware acceleration                           | GPU hardware acceleration renders the Mattermost Desktop App interface more efficiently.                                                                 |
        |                                                         | If you encounter decreased stability with this enabled, you can disable GPU hardware acceleration. You must restart the app to change this setting.      |
        +---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
        | Open app in fullscreen                                  | You can configure the Mattermost Desktop App to open in fullscreen mode.                                                                                 |
        |                                                         | You can also toggle this setting using the following CLI command:                                                                                        |
        |                                                         |                                                                                                                                                          |
        |                                                         | ``open release/mac/Mattermost.app --args --fullscreen true`` or ``open release/mac/Mattermost.app --args -f true``                                       |
        +---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

    .. tab:: Windows

        When you `install the Mattermost desktop app </collaborate/install-desktop-app.html#install-and-update-the-mattermost-desktop-app>`__, you can access additional Desktop App customization settings by selecting **File > Settings...** from the **More** |more-icon-vertical| icon located in the top left corner of the desktop app. 

        .. image:: ../images/desktop-app-settings.jpg
            :alt: Access Desktop App customization settings by selecting More in the top left corner, then selecting File > Settings.

        +--------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
        | **Desktop App setting**                                                  | **Description**                                                                                                                   |
        +==========================================================================+===================================================================================================================================+
        | Automatically check for updates                                          | Updates to the Mattermost Desktop App download automatically. You're notified when an update is ready.                            |
        |                                                                          | You can disable automatic updates through group policy (GPO) settings.                                                            |
        |                                                                          | You can also manually check for updates by selecting **Check for Updates Now**.                                                   |
        +--------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
        | Start app on login                                                       | The Mattermost Desktop App starts up automatically when you log in to your machine.                                               |
        |                                                                          | You can configure the Desktop App not to launch automatically when you log in to your machine.                                    |
        +--------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
        | Launch app minimized                                                     | You can configure the Mattermost Desktop App to launch minimized in the system tray.                                              |
        +--------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
        | Check spelling                                                           | Misspelled words in your messages are highlighted based on the system language. You can disable spell check.                      |
        |                                                                          |                                                                                                                                   |
        |                                                                          | You can also specify additional spell check languages. You must restart the app to change this setting.                           |
        |                                                                          |                                                                                                                                   |
        |                                                                          | When multiple languages are configured:                                                                                           |
        |                                                                          |                                                                                                                                   |
        |                                                                          | - All selected languages show as correct when a word matches at least one selected language.                                      |
        |                                                                          | - All selected languages show as incorrect when a word matches none of the languages.                                             |
        +--------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
        | Use an alternative dictionary URL                                        | You can specify an alternate dictionary for spell check as a site URL.                                                            |
        +--------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
        | Icon theme                                                               | The default icon theme is based on the system preferences appearance setting.                                                     |
        |                                                                          | You can choose to display a light or dark-themed icon.                                                                            |
        +--------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
        | Leave app running in notification area when application window is closed | When you close the Mattermost Desktop App, you're prompted to confirm whether you want to permanently close the app.              |
        |                                                                          | You can disable this confirmation or silence it by selecting **Don't ask again**.                                                 |
        |                                                                          | You can also configure the app to continue running after the window is closed.                                                    |
        |                                                                          | To silence the notifications, select **Don't show again**.                                                                        |
        +--------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
        | Use GPU hardware acceleration                                            | GPU hardware acceleration renders the Mattermost Desktop App interface more efficiently.                                          |
        |                                                                          | If you encounter decreased stability, you can disable GPU hardware acceleration. You must restart the app to change this setting. |
        +--------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
        | Open app in fullscreen                                                   | You can configure the Mattermost Desktop App to open in fullscreen mode.                                                          |
        |                                                                          | You can also toggle this setting using the following CLI command:                                                                 |
        |                                                                          |                                                                                                                                   |
        |                                                                          | ``open release/mac/Mattermost.app --args --fullscreen true`` or ``open release/mac/Mattermost.app --args -f true``                |
        +--------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
        | Download location                                                        | Specify where you want files to be downloaded on your machine.                                                                    |
        +--------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
        | Logging level                                                            | You can adjust logging levels to isolate and troubleshoot issues.                                                                 |
        |                                                                          | Increasing the log level increases disk space usage and can impact performance.                                                   |
        +--------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+