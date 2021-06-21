Organizing Conversations using Collapsed Reply Threads (Beta)
=============================================================

Threads are a key part of the messaging experience in Mattermost. Threads organize conversations within channels, and threads enable users to discuss topics without adding noise to channels or Direct Messages. 

Collapsed Reply Threads offers an enhanced experience for users participating in conversations by:

- Improving channel details to find, follow, and resume conversations more easily.
- Prioritizing how conversation threads are displayed in Mattermost.

.. image:: ../../images/collapsed-reply-threads.gif
  :alt: Organize conversations using Collapsed Reply Threads.

Your System Admin must enable the Collapsed Reply Threads feature in the System Console. See our `Configuration Settings <https://docs.mattermost.com/administration/config-settings.html#collapsed-reply-threads-beta>`__ documentation for details. You may additionally need to enable this feature for your Mattermost account by going to **Account Settings > Display > Collapsed Reply Threads (Beta)**.

Known Issues
------------

.. important::

    Collapsed Reply Threads is available as a beta release from Mattermost v5.37. You may experience minor issues with this beta functionality. 

You may encounter the following known issues after enabling Collapsed Reply Threads:

- You may automatically follow a large number of historical threads resulting in a large number of unread threads. To resolve this, go to  **Threads** in the channel sidebar, then select **Mark All As Read**. Older threads you’re automatically following will continue to notify you of new replies.
- You may see channels or Direct Messages with no new activity marked as unread. To resolve this, review all the unread channels, or press ALT+SHIFT+UP/DOWN to quickly navigate to all your unread channels in the sidebar and mark them as read. 
- See our `Collapsed Reply Threads board <https://mattermost.atlassian.net/secure/RapidBoard.jspa?rapidView=91&projectKey=MM&selectedIssue=MM-34895>`__ for additional details on known, in progress, and resolved issues.

Start or Reply to Threads
-------------------------

Replies are collapsed under the first message of a thread. To reply to a thread, select the **Reply** icon, or select the reply count if a thread already exists. 

.. tip:: 
    
    - Select anywhere on a message in a channel to view it, or reply to it, on the right-hand side.
    - In channels, a dot on threads indicates unread replies for threads you're following.

.. image:: ../../images/crt-new-unread-threads.png
   :alt: A dot on threads in a channel indicates unread replies.

Follow Threads and Messages
---------------------------

You can follow particular messages and threads so that any reply activity triggers notifications. Follow or unfollow any thread, at any time, by toggling the thread’s **Follow/Following** indicator, or by accessing the **More Actions** menu. On Mobile, long press to follow or unfollow threads.

.. image:: ../../images/crt-following-thread.png
   :alt: Follow threads to stay updated on replies.

You can follow messages with no replies from the **More Actions** menu to be notified if someone replies to the message later.

You'll automatically follow every thread you participate or are mentioned in. If you’re no longer interested in a or message thread, you can unfollow it to stop receiving notifications.

Viewing a thread without responding to it doesn’t automatically follow that thread.

.. image:: ../../images/crt-more-actions.png
   :alt: Follow, unfollow, and mark threads as unread from More Actions.

View All Threads
----------------

Select **Threads**  at the top of the channel sidebar to see all your followed threads on the currently selected team in the Thread View. Threads with the most recent replies display at the top of the list. 

Select **Unreads** to filter your followed threads by only those with unread replies.

.. tip::  

  - Use the **More Actions** menu or ALT+Select to mark reply posts as unread if you want to come back to them later.
  - Use UP and DOWN arrow keys to switch between threads in this list.

.. image:: ../../images/crt-thread-view.png
  :alt: Select Threads in the channel sidebar to see all thread updates in your Threads View.