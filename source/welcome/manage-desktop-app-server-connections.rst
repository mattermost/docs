Manage Desktop App server connections
=====================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Using the Mattermost desktop app, you can connect to multiple Mattermost servers from a single interface. 

.. tabs::

  .. tab:: Mattermost desktop app v5.0 onwards
  
    The **Server** list is located in the top left corner of the window and displays all servers available in your desktop app environment. Drag to reorder the servers in the list. You can also navigate the server options using `keyboard shortcuts </welcome/keyboard-shortcuts.html>`__. From the **Server** list, you can add, edit, and remove servers.
    
    **Add a server**
    
    1. Select **Add a server**.

      .. image:: ../images/desktop-server-add.png
        :alt: Connect the desktop app to a Mattermost Server using options located in the top left corner of the Mattermost screen.

    2. Enter the server name as it will appear in the desktop app.
    3. Enter the server URL. Server URLs must begin with either ``http://`` or ``https://``.

       .. tip::

        Can't find your Mattermost server URL? Ask your company’s IT department or your Mattermost System Admin for your organization’s **Mattermost Site URL**. It’ll look something like ``https://example.com/company/mattermost``, ``mattermost.yourcompanydomain.com``, or ``chat.yourcompanydomain.com``. These URLs could also end in ``.net``.

    4. Select **Add**.

      .. image:: ../images/desktop-server-add2.png
          :alt: Connect the desktop app to another Mattermost Server using options located in the top left corner of the Mattermost screen.
    
    **Edit a server**
    
    1. Hover over a server and select the **Edit** icon.

       .. image:: ../images/desktop-edit-server.png
         :alt: Edit an existing Mattermost server connection using options located in the top right corner of the Mattermost screen.

    2. Modify the server's display name or URL, then select **Save**.
    
    **Remove a server**
    
    Removing a server from your desktop app doesn't delete its data. You can add the server back any time.
    
    1. Hover over a server and select **Remove**.

       .. image:: ../images/desktop-remove-server.png
         :alt: Remove a Mattermost server connection using options located in the top right corner of the Mattermost screen.

    2. Select **Remove** when prompted to confirm.
    
  .. tab:: Mattermost desktop app v4.7 and earlier
  
    Each server appears as a separate tab at the top of the window. Drag to reorder the server tabs. From the Server Management section, you can add, edit, and remove servers. 

    **Add a server**

    To add a new server to your desktop app environment:

    1. Select the **+** button in the desktop window bar at the top of the screen.
    2. In the **Name** field, enter the name that you want for the tab.
    3. In the **URL** field, enter the complete URL of the server that you want to connect to. Must begin with either ``http://`` or ``https://``.
    4. Select **Add**.

    **Edit a server**

    To edit a server in your desktop app environment:

    1. On Windows and Linux, go to **... > File > Settings**. On Mac, go to **Mattermost > Preferences**.
    2. Next to the server you want to update, select **Edit**.
    3. Edit **Name** and/or **URL**.
    4. Select **Save**.

    **Remove a server**

    To remove a server from your desktop app environment:

    1. On Windows and Linux, go to **... > File > Settings**. On Mac, go to **Mattermost > Preferences**.
    2. Next to the server or team that you want to remove, select **Remove**.

