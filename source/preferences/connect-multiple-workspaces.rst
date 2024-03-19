Connect to multiple Mattermost workspaces
=========================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |servers-icon| image:: ../images/server-variant_E81F.svg
  :alt: Access server connection options using the Servers icon.
  :class: theme-icon

Using the Mattermost desktop or mobile app, you can connect to multiple Mattermost instances from a single interface. 

.. note::

  The ability to create and manage multiple server connections isn't available when using Mattermost in a web browser.

.. tab:: Web/Desktop

  .. note::

    If you're using the desktop app prior to release v5.0, individual servers display as separate tabs at the top of the window instead of the top left corner of the window as a list, and servers are managed by going to **… > File > Settings** on Windows and **Mattermost > Preferences** on Mac.

  The **Server** list is located in the top left corner of the window and displays all servers available. Drag to reorder the servers in the list. You can also navigate the server options using :doc:`keyboard shortcuts </collaborate/keyboard-shortcuts>`. From the **Server** list, you can add, edit, and remove servers.
  
  **Add a server**
  
  1. Select **Add a server**.

    .. image:: ../images/desktop-server-add.png
      :alt: Connect the desktop app to a Mattermost Server using options located in the top left corner of the Mattermost screen.

  2. Enter the server URL. Server URLs must begin with either ``http://`` or ``https://``.
  3. Enter the server's Display Name.

    .. tip::

      Can't find your Mattermost server URL? Ask your company’s IT department or your Mattermost system admin for your organization’s **Mattermost Site URL**. It’ll look something like ``https://example.com/company/mattermost``, ``mattermost.yourcompanydomain.com``, or ``chat.yourcompanydomain.com``. These URLs could also end in ``.net``.

  4. Select **Add**.
  
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
  
.. tab:: Mobile

  Tap the **Servers** |servers-icon| icon located in the top left corner of the window to access all available servers and to add new servers.

  **Add a server**
      
  1. Tap **Add a server**.
  2. Enter the server URL. Server URLs must begin with either ``http://`` or ``https://``.
  3. Enter the server's Display Name.
  4. Tap **Done**.

  .. tip::

      Can't find your Mattermost server URL? Ask your company’s IT department or your Mattermost system admin for your organization’s **Mattermost Site URL**. It’ll look something like ``https://example.com/company/mattermost``, ``mattermost.yourcompanydomain.com``, or ``chat.yourcompanydomain.com``. These URLs could also end in ``.net``.

  **Remove a server**

  Swipe left on an existing server entry to reveal additional options. Tap **Remove**.

  .. image:: ../images/swipe-left-to-remove.png
    :width: 400px
    :alt: In the Mattermost mobile app, swipe left on an existing server connection entry to delete the connection.

  .. note::

      Removing a server from your mobile app doesn't delete its data. You can add the server back any time.
