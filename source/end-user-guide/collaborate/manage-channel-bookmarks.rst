Manage channel bookmarks
=========================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

From Mattermost v10.1, you can bookmark up to 50 links or files to the top of channels for quick and easy access, unless your system admin has disabled your ability to do so. Bookmarks display directly under channel headers. Files added as channel bookmarks are also :doc:`searchable </end-user-guide/collaborate/search-for-messages>` in Mattermost.

Open a bookmark
---------------

Opening a channel bookmark works the same way as selecting a file link or attachment in a message. Select or tap a bookmark to view the file or link.

From Mattermost v10.11, bookmarks containing ``mattermost://`` links open directly in the desktop app using deep linking. This turns bookmarks into one-click shortcuts to channels, threads, or messages, letting you jump straight to key assets in Mattermost quickly and easily.

Add a bookmark
--------------

.. tab:: Web/Desktop

    1. From Mattermost v10.5, select the channel name at the top of the center pane to access the drop-down menu, and select **Bookmarks Bar** to add a link or attach a file. In Mattermost versions prior to v10.5, select **Add a bookmark** in the bookmarks bar instead.
    
     - Select **Add a link** to specify the link URL, specify bookmark text, and an optional bookmark icon.
     - Select **Attach a file** to select a file, specify bookmark text, and an optional bookmark icon.

.. tab:: Mobile

    The bookmarks bar is hidden when a channel has no bookmarks.
    
    1. In a channel, select the **More** |more-icon-vertical| icon.

    .. image:: ../../images/mobile-select-more-options-for-a-channel.jpg
      :alt: Tap on More options to access available options for the channel.
      :scale: 30
    
    2. Select **View info**.

    .. image:: ../../images/mobile-select-view-info-for-a-channel.jpg
      :alt: Tap on View info to view additional information about the channel.
      :scale: 30
    
    3. Tap on **Add a bookmark** to add the first bookmark.

    .. image:: ../../images/mobile-add-first-channel-bookmark.jpg
        :alt: Tap on Add a bookmark to add the first bookmark.
        :scale: 30
         
    For subsequent bookmarks, select the **Plus** |plus| icon in the bookmarks bar.
    
    .. image:: ../../images/mobile-add-subsequent-channel-bookmarks.jpg
        :alt: Tap on the Plus icon to add more bookmarks to the channel.
        :scale: 30

    4. You can either select **Add a link** to specify the link URL, specify bookmark text, and an optional bookmark icon. 

    .. image:: ../../images/mobile-attach-a-channel-bookmark-link.jpg
        :alt: Tap on Add a link to add a Bookmark link.
        :scale: 30
     
    Or you can select **Add a file** to select a file, specify bookmark text, and an optional bookmark icon.

    .. image:: ../../images/mobile-attach-a-channel-bookmark-file.jpg
        :alt: Tap on Add a file to add a file as Bookmark.
        :scale: 30

    5. Tap on **Save**.

Manage bookmarks
----------------

You can `edit <#edit-bookmarks>`__ and `delete <#delete-bookmarks>`__ bookmarks, as well as `copy bookmark links <#copy-bookmark-links>`__. Additionally, web and desktop users can `reorder bookmarks <#reorder-bookmarks>`__, and mobile users can `share bookmarks <#share-bookmarks>`__. Changes to bookmarks are visible to all channel members.

Reorder bookmarks
^^^^^^^^^^^^^^^^^

Using Mattermost in a web browser or the desktop app, drag bookmarks to reorder them in the bookmarks bar. Reordering channel bookmarks changes the display order for all channel members.

.. note::

    You can't reorder channel bookmarks using the mobile app.

Edit bookmarks
^^^^^^^^^^^^^^^

You can make changes to the bookmark link or file, the bookmark title, or the optional bookmark icon. Editing a bookmark changes the bookmark for all channel members.

.. tab:: Web/Desktop

    Select the **More** |more-icon| icon next to a bookmark and select **Edit**. 

.. tab:: Mobile

    Long-press on a bookmark and select **Edit**.

    .. image:: ../../images/mobile-edit-a-channel-bookmark.gif
        :alt: Tap and hold a bookmark name to explore more options.
        :scale: 50

Share bookmarks
^^^^^^^^^^^^^^^^

Using the mobile app, long-press on a bookmark and select **Share**.

Copy bookmark links
^^^^^^^^^^^^^^^^^^^^

You can copy bookmark links when your system admin has :ref:`enabled your ability to do so <administration-guide/configure/site-configuration-settings:enable public file links>`.

.. tab:: Web/Desktop

    Select the **More** |more-icon| icon next to a bookmark and select **Copy link**.

.. tab:: Mobile

    Long-press on a bookmark and select **Copy link**.

    .. image:: ../../images/mobile-copy-a-channel-bookmark-link.gif
        :alt: Tap and hold a bookmark name to explore more options.
        :scale: 50

Delete bookmarks
^^^^^^^^^^^^^^^^^

Deleting a channel bookmark deletes it for all channel members.

.. tab:: Web/Mobile

    Select the **More** |more-icon| icon next to a bookmark and select **Delete**.

.. tab:: Mobile

    Long-press on a bookmark and select **Delete**.

    .. image:: ../../images/mobile-delete-a-channel-bookmark.gif
        :alt: Tap and hold a bookmark name to explore more options.
        :scale: 50

