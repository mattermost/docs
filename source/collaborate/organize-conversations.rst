Organize conversations using threaded discussions
====================================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Threads are a key part of the messaging experience in Mattermost. They're used to organize conversations and enable users to discuss topics without adding noise to channels or direct messages.

Threaded discussions offers an enhanced experience for users communicating in threads and replying to messages that includes a unified threads inbox to read all conversations in one view. Threads improve the ability to process channel content, find, follow, and resume conversations more easily, and keep threaded conversations focused.

From Mattermost v7.0, threaded discussions are enabled by default for all new Mattermost deployments. All Mattermost users can create new threads, unless the system admin has :ref:`disabled the ability to do so <configure/site-configuration-settings:threaded discussions>`.

.. note::

  System admins can :ref:`configure default availability and user opt-in <configure/site-configuration-settings:threaded discussions>` of threaded discussions.

.. image:: ../images/collapsed-reply-threads.gif
  :alt: Organize conversations using threaded discussions.

Start or reply to threads
-------------------------

:doc:`Replies to messages </collaborate/reply-to-messages>` are collapsed under the first message of a thread. 

.. tip:: 
    
    - When replying to a thread in a web browser or the desktop app, you can also select the reply count if a thread already exists, and you can select anywhere on a message in a channel in the center pane to view it or reply to it.
    - In channels, a dot next to the thread participants indicates there are unread replies. You'll only see unreads for threads you're following.

.. image:: ../images/crt-new-unread-threads.jpg
   :alt: A dot on threads in a channel indicates unread replies.

Follow threads and messages
---------------------------

You'll automatically follow every thread you participate or are mentioned in. You can manually follow particular messages and threads so that any reply activity triggers :doc:`notifications </preferences/manage-your-notifications>`. Follow or unfollow any thread, at any time.

.. image:: ../images/crt-following-thread.png
   :alt: Follow threads to stay updated on replies to messages.

.. tab:: Web/Desktop

  Toggle the thread’s **Follow/Following** indicator, or select **Follow thread** from the **More Actions** |more-icon| icon.
  
  **Unfollow threads**
  
  If you’re no longer interested in a or message thread, unfollow it to stop receiving notifications. Viewing a thread without responding to it doesn’t automatically follow that thread.

  .. image:: ../images/crt-following-thread.jpg
    :alt: Follow, unfollow, and mark threads as unread from the More Actions icon.

.. tab:: Mobile

  Long-press on a message to access message options, then tap **Follow Thread**. 
  
  **Unfollow threads**
  
  If you’re no longer interested in a or message thread, unfollow it to stop receiving notifications. Viewing a thread without responding to it doesn’t automatically follow that thread.

.. tip::
  - Follow messages with no replies from the **More Actions** |more-icon| icon to be notified if someone replies to the message later based on your notification preferences.
  - You can also use keyboard arrow keys to navigate threads in the **Threads** view.

View all threads
----------------

Select **Threads** at the top of the channel sidebar to see all your followed threads on the currently selected team. Threads with the most recent replies display at the top of the list. 

Select **Unreads** to filter your followed threads by only those with unread replies.

.. image:: ../images/crt-thread-view.jpg
  :alt: Select Threads in the channel sidebar to see all thread updates in your Threads View.

Tutorial video
---------------

.. raw:: html

  <script src="https://fast.wistia.com/embed/medias/5gjgi10rr0.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_5gjgi10rr0 videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/5gjgi10rr0/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>
  <br>

Known issues
------------

Threaded discussions were released as generally available in Mattermost v7.0, including significant server performance improvements and more flexible configuration options for system admins to enable the feature by default. We highly recommended :doc:`upgrading Mattermost </upgrade/upgrading-mattermost-server>` to take advantage of configuration and performance enhancements.
