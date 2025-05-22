Customize your Desktop App experience
=====================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

You can customize your desktop app further with additional settings. Select the tab below that matches your operating system to learn more about what's available.

.. tab:: macOS

    With the Mattermost desktop app in focus, select **Mattermost > Settings...**

    .. image:: ../images/mac-desktop-app-settings.png
      :alt: Access Desktop App customization settings by selecting Mattermost from the menu bar, then selecting Preferences.

    **General**

    - **Download Location**: Specify where on your machine you want files to be downloaded from the desktop app.
    - **Show icon in the notification area**: The Mattermost icon displays in the notification area. You can hide this icon if preferred. Restart the desktop app to apply changes to this setting.
    - **Open app in full screen**: Configure the desktop app to open in fullscreen. You can also toggle this setting using the following CLI command: ``open release/mac/Mattermost.app --args --fullscreen true or open release/mac/Mattermost.app --args -f true``

    **Notifications**

    - **Show red badge on Dock icon to indicate unread messages**: A red badge on the Dock icon displays a count of unread messages and mentions. You can configure the desktop app to display a count of mentions only, if preferred.
    - **Bounce the Dock icon**: When a new message is received on any of your active teams and servers, the Dock icon bounces once or bounces until you open the desktop app. You can configure the Mattermost Desktop App Dock icon to bounce more, less, or not at all.

    **Language**

    - **App Language**: Specify your preferred language for the desktop app.
    - **Check spelling**: Misspelled words detected in your messages are highlighted based on your app language preference. You can disable spell check if preferred.

    - **Spell Checker Languages**: Specify additional spell check languages if needed. Restart the desktop app to change this setting. When multiple languages are configured:

        - All selected languages show as spelled correctly when a word matches at least one selected language
        - All selected languages show as spelled incorrectly when a word matches none of the selected languages.

    - **Use an alternative dictionary URL**: Specify an alternate dictionary for spell check as a site URL.

    **Servers**

    - **Add and manage server connections**: :doc:`Learn more </preferences/connect-multiple-workspaces>` about connecting your desktop app to multiple Mattermost workspaces.

    **Advanced**

    - **Logging level**: Adjust logging levels to isolate and troubleshoot issues. Increasing the log level increases disk space usage and can impact performance.
    - **Send anonymous usage data to your configured servers**: Send desktop app usage and performance data to your configured Mattermost servers set up to accept it.
    - **Use GPU hardware acceleration**: GPU hardware acceleration renders the desktop app interface more efficiently. If you encounter decreased stability, disable GPU hardware acceleration. Restart the desktop app to apply changes to this setting.

.. tab:: Windows/Linux

    With the Mattermost desktop app in focus, select the **More** |more-icon-vertical| icon in the top left of the menu bar and select **File > Settings...**

    .. image:: ../images/desktop-app-settings.jpg
      :alt: Access Desktop App customization settings by selecting More in the top left corner, then selecting File > Settings.

    **General**

    - **Download Location**: Specify where on your machine you want files to be downloaded from the desktop app.
    - **Start app on login**: The desktop app starts up automatically when you log in to your machine. You can disable this if preferred.
    - **Launch app minimized**: Configure the desktop app to launch minimized in the system tray.
    - **Icon color**: Display a light, dark, or system default-driven Mattermost icon.
    - **Leave app running in notification area when application window is closed**: When closing the desktop app, you’re prompted to confirm whether you want to permanently close the app. Disable this confirmation by selecting **Don’t ask again**.Silence these notifications by selecting **Don’t show again**.  Restart the desktop app to apply changes to this setting.
    - **Open app in full screen**:

    **Notifications**

    - **Show red badge on taskbar icon to indicate unread messages**:
    - **Flash taskbar icon when a new message is received**: Your desktop app taskbar icon flashes when a new message is received on any of your active teams and servers. You can disable the flashing taskbar icon if preferred.

    **Language**

    - **App Language**: Specify your preferred language for the desktop app.
    - **Check spelling**: Misspelled words detected in your messages are highlighted based on your app language preference. You can disable spell check if preferred.
    - **Spell Checker Languages**: Specify additional spell check languages if needed. Restart the desktop app to apply changes to this setting. When multiple languages are configured:

        - All selected languages show as spelled correctly when a word matches at least one selected language
        - All selected languages show as spelled incorrectly when a word matches none of the selected languages.

    - **Use an alternative dictionary URL**: Specify an alternate dictionary for spell check as a site URL.

    **Servers**

    - **Add and manage server connections**: :doc:`Learn more </preferences/connect-multiple-workspaces>` about connecting your desktop app to multiple Mattermost workspaces.

    **Advanced**

    - **Logging level**: Adjust logging levels to isolate and troubleshoot issues. Increasing the log level increases disk space usage and can impact performance.
    - **Send anonymous usage data to your configured servers**: Send desktop app usage and performance data to your configured Mattermost servers set up to accept it.
    - **Use GPU hardware acceleration**: GPU hardware acceleration renders the desktop app interface more efficiently. If you encounter decreased stability, disable GPU hardware acceleration. Restart the desktop app to apply changes to this setting.