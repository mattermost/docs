:nosearch:

Organizing Conversations using Collapsed Reply Threads (Beta)
=============================================================

Threads are a key part of the messaging experience in Mattermost. Threads organize conversations within channels, and threads enable users to discuss topics without adding noise to channels or Direct Messages. 

Collapsed Reply Threads (Beta) offers an enhanced experience for users communicating in threads and replying to messages. Our goal is to improve users’ ability to process channel content, find, follow, and resume conversations more easily, and keep threaded conversations focused.

.. image:: ../../images/collapsed-reply-threads.gif
  :alt: Organize conversations using Collapsed Reply Threads.

Your System Admin must enable the Collapsed Reply Threads feature in the System Console. See our `Configuration Settings </configure/configuration-settings.html#collapsed-reply-threads-beta>`__ documentation for details. You can `enable this feature for your Mattermost account </messaging/manage-channels-settings.html#collapsed-reply-threads-beta>`__ by going to **Account Settings > Display > Collapsed Reply Threads (Beta)**.

Known Issues
------------

.. important::

    Collapsed Reply Threads are available as an early beta in Mattermost Cloud and Mattermost Server v5.37 and later. It's expected that you may experience bugs as we stabilize the feature. In particular, please be aware of these known issues: 
    
    - When enabling Collapsed Reply Threads for the first time, you may see channels or threads you’ve seen before appear as unread. To resolve this,
    
      - View any unread channels or use ALT+SHIFT+UP/DOWN to switch to unread channels with the keyboard. Work in-progress ticket: `MM-35494 <https://mattermost.atlassian.net/browse/MM-35494>`__
      - Use the **Mark all as read** button in the **Threads** view to mark your threads as read. Work in-progress ticket: `MM-35345 <https://mattermost.atlassian.net/browse/MM-35345>`__
       
    - You may experience lag in your desktop or web client if you're following many threads or opening threads with many replies. Work in-progress tickets: `MM-36696 <https://mattermost.atlassian.net/browse/MM-36696>`__, `MM-36697 <https://mattermost.atlassian.net/browse/MM-36697>`__, `MM-36698 <https://mattermost.atlassian.net/browse/MM-36698>`__
    - You should expect to see more unread channels and notifications on your mobile device than you'll see on your Desktop instance of Mattermost. This is expected until mobile support is available for Collapsed Reply Threads, expected in August 2021. For early access, join our `mobile beta program <https://github.com/mattermost/mattermost-mobile#testing>`__. 
    - For a comprehensive list of known issues, and to see our work queue in priority order, check out our `Kanban board <https://mattermost.atlassian.net/secure/RapidBoard.jspa?rapidView=91&quickFilter=499>`__.

Start or Reply to Threads
-------------------------

Replies are collapsed under the first message of a thread. To reply to a thread, select the **Reply** icon, or select the reply count if a thread already exists. 

.. tip:: 
    
    - Select anywhere on a message in a channel to view it, or reply to it, on the right-hand side.
    - In channels, a dot next to the thread participants indicates there are unread replies. You'll only see unreads for threads you're following.

.. image:: ../../images/crt-new-unread-threads.png
   :alt: A dot on threads in a channel indicates unread replies.

Follow Threads and Messages
---------------------------

You can follow particular messages and threads so that any reply activity triggers notifications. Follow or unfollow any thread, at any time, by toggling the thread’s **Follow/Following** indicator, or by accessing the **More Actions** menu. 

.. image:: ../../images/crt-following-thread.png
   :alt: Follow threads to stay updated on replies.

You'll automatically follow every thread you participate or are mentioned in. If you’re no longer interested in a or message thread, you can unfollow it to stop receiving notifications. Viewing a thread without responding to it doesn’t automatically follow that thread.

.. image:: ../../images/crt-more-actions.png
   :alt: Follow, unfollow, and mark threads as unread from More Actions.
   
.. tip::
  Follow messages with no replies from the **More Actions** menu to be notified if someone replies to the message later.

View All Threads
----------------

Select **Threads** at the top of the channel sidebar to see all your followed threads on the currently selected team. Threads with the most recent replies display at the top of the list. 

Select **Unreads** to filter your followed threads by only those with unread replies.

.. image:: ../../images/crt-thread-view.png
  :alt: Select Threads in the channel sidebar to see all thread updates in your Threads View.

Tutorial Video
---------------

For additional details about working with the Beta release of Collapsed Reply Threads, see our `tutorial video on YouTube <https://www.youtube.com/watch?v=hnD0Zj-mIbs>`_. 

.. raw:: html

   <div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; height: auto;">
      <iframe src="https://www.youtube.com/embed/hnD0Zj-mIbs" alt="A video tutorial about collapsed reply threads in Mattermost" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 95%;"></iframe>
   </div>
