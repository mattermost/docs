Desktop app troubleshooting
============================

Where is configuration stored locally?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The location of the Mattermost desktop app configuration file depends on the platform where you're running Mattermost (and, in the case of macOS, how you've chosen to install the app):

- Windows: ``Users\<username>\AppData\Roaming\Mattermost``
- macOS installer: ``/Users/<username>/Library/Application Support/Mattermost``
- macOS App Store: ``/Users/<username>/Library/Containers/Mattermost.Desktop/Data/Library/Application Support/Mattermost`` (via Finder: ``~/Library/Application Support/Mattermost`` as the extension is hidden)
- Linux: ``~/.config/Mattermost``

.. note::

  - Local configuration data is not automatically removed when uninstalling the desktop app. If you wish to remove all data, you must manually remove the files from the applicable location noted above.
  - Prior to uninstalling, you can choose to log out of any active sessions. You can terminate active sessions from another Mattermost session in **Profile > Security > View and Logout of Active Sessions**, then select **Log Out**. Desktop app sessions are labeled as **Native Desktop App**.
  
How do I access logs?
~~~~~~~~~~~~~~~~~~~~~

From Mattermost desktop v5.3, you can access logs via **Help > Show logs**, which opens the file manager window showing the location of the log file.

How do I download app diagnostics?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From Mattermost desktop v5.3, you can download a diagnostics text file via **Help > Run diagnostics**, which can be attached to a Support ticket.

Deep links open in the wrong workspace in multi-view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you experience deep links opening in the wrong workspace, ensure all relevant workspaces are pre-provisioned via the Group Policy ``DefaultServerList``. See the :ref:`multi-view and group policies <deployment-guide/desktop/desktop-msi-installer-and-group-policy-install:multi-view and Group Policies>` documentation for details.

- Verify that workspace URLs match exactly (including protocol and subdomain) so links route to the intended workspace.
- Edit the workspace list to correct or remove stale entries, then retry the link.

High CPU or memory when multiple workspaces open
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Verify the device is powerful enough to run several workspaces concurrently. Close unused tabs and pop-out windows to reduce load.

Check the :doc:`desktop app advanced settings </end-user-guide/preferences/customize-desktop-app-experience>`. Toggle **Use GPU hardware acceleration** off on systems with unstable drivers.

Desktop App displays white screen while launching and doesn't load the page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Delete the local ``Mattermost desktop app`` configuration file. See the `Where is configuration stored locally? <#where-is-configuration-stored-locally>`__ section above for file location details.
2. Reinstall the application. 

"Installation has failed" dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The app data might be corrupted. Remove all the files in ``%LOCALAPPDATA%\mattermost``, then try reinstalling the app.
    
"The application "Mattermost" can't be opened" dialog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On macOS Catalina, this dialog can be triggered if the Mac Archive Utility is the default method for decompressing files. In this case using a third-party tool such as `Keka <https://www.keka.io>`_ or `Unarchiver <https://macpaw.com/the-unarchiver>`_ may resolve the problem.

Desktop App window is black and doesn't load the page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Ensure you have installed the latest desktop app version available.
2. Clear your cache and reload the app from **View > Clear Cache and Reload** or press :kbd:`Ctrl` :kbd:`Shift` :kbd:`R` on Windows or Linux, or :kbd:`⌘` :kbd:`⇧` :kbd:`R` on Mac.
3. Quit the app and restart it to see if the issue clears.
4. Disable GPU hardware acceleration.

  - On Windows or Linux, select **File > Settings** and clear the **Use GPU hardware acceleration** option.
  - On macOS, select **Mattermost > Settings** and clear the **Use GPU hardware acceleration** option.

5. If you are using a special video driver, such as Optimus, try disabling it to see if the problem is resolved.

Desktop App window is white and doesn't load the page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Ensure you have installed the latest desktop app version available.
2. Delete the ``%userprofile%\AppData\Roaming\Mattermost`` directory on your local machine.
3. Reinstall the desktop app.

Desktop App is not visible, but the Mattermost icon is in the Task Bar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This issue can occur on Windows in a multiple-monitor setup. When you disconnect the monitor that Mattermost is displayed on, Mattermost continues to display at screen coordinates that no longer exist.

To resolve this issue, you can reset the desktop app screen location by deleting the screen location file. When the file is not present, the desktop app displays on the primary monitor by default.

To reset the desktop app screen location:

1. If the desktop app is running, right-click the Mattermost icon in the task bar, then select **Close Window**.
2. Open Windows File Explorer, and go to the ``%APPDATA%\Mattermost`` folder.
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

- Windows: Open Windows File Explorer, go to the ``%APPDATA%\Mattermost`` folder, then delete the ``IndexedDB`` folder and the ``Cookies`` and ``Cookies-journal`` files.
- Mac: Open Finder, go to the ``~/Library/Application Support/Mattermost`` folder, then delete the ``IndexedDB`` folder and the ``Cookies`` and ``Cookies-journal`` files.
- Linux: Open the file manager, go to the ``~/.config/Mattermost`` folder, then delete the ``IndexedDB`` folder and the ``Cookies`` and ``Cookies-journal`` files. Linux file managers may hide folders starting with a period by default. You can delete them from the terminal using ``rm -rf ~/.config/Mattermost``.

"Internal error: BrowserWindow 'unresponsive' event has been emitted"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Selecting **Show Details** on the dialog provides logs. Ways to resolve the issue:

1. Clear the cache via **View > Clear Cache and Reload** or press :kbd:`Ctrl` :kbd:`Shift` :kbd:`R` on Windows or Linux, or :kbd:`⌘` :kbd:`⇧` :kbd:`R` on Mac.
2. Go to App Settings via **File > Settings** (or by pressing :kbd:`Ctrl` :kbd:`,` on Windows or Linux, or :kbd:`⌘` :kbd:`,` on Mac) and unselect hardware acceleration.
  
Desktop app not responsive within Citrix Virtual Apps or Desktop Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Append ``Mattermost.exe;`` to the Registry Key ``HKLM\SYSTEM\CurrentControlSet\Services\CtxUvi\UviProcessExcludes`` and reboot the system.

For further assistance, review the `Troubleshooting forum <https://forum.mattermost.com/c/trouble-shoot/16>`_ for previously reported errors, or `join the Mattermost user community for troubleshooting help <https://mattermost.com/community/>`_.

Can I uninstall the desktop app I installed using snap on Linux?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. Run the following command from a terminal window: ``sudo snap remove mattermost-desktop``.

Report Desktop App issues
-------------------------

When reporting issues found in the Mattermost desktop app, it's helpful to include the contents of the Developer Tools Console along with `the information on this page <https://support.mattermost.com/hc/en-us/articles/360060662492-Opening-a-Support-Ticket-for-Self-Managed-Deployments>`_. 

To access the Developer Tools Console:

1. In the menu bar, go to **View > Developer Tools > Developer Tools for Current Tab**.
2. Select the **Console** tab.
3. Right-click the log entry, then select **Save As**.
4. Save the file, then send it along with a description of your issue.
5. Close the console to disable the Developer Tools.

You can open an additional set of developer tools for each server you have added to the desktop app. The tools can be opened by pasting this command in the Developer Tools Console you opened with the steps described above:

    .. code-block:: javascript

       document.getElementsByTagName("webview")[0].openDevTools();


