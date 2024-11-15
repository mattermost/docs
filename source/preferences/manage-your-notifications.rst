Manage your notifications
=========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |dot-badge| image:: ../images/dot-badge.png
    :alt: A dot on the badge means you have unread activity in at least one channel you're a member of.
    :width: 50px
.. |numbered-badge| image:: ../images/numbered-badge.png
    :alt: A numbered badge means you have at least 1 unread message, @mention, or one of your keywords has triggered a notification.
    :width: 50px

.. toctree::
  :maxdepth: 1
  :hidden:
  :titlesonly:

    Troubleshoot notifications </preferences/troubleshoot-notifications>
    Manage your web notifications </preferences/manage-your-web-notifications>
    Manage your desktop notifications </preferences/manage-your-desktop-notifications>
    Manage your mobile notifications </preferences/manage-your-mobile-notifications>
    Manage your thread reply notifications </preferences/manage-your-thread-reply-notifications>
    Manage your @mention & keyword notifications </preferences/manage-your-mentions-keywords-notifications>
    Manage your channel-specific notifications </preferences/manage-your-channel-specific-notifications>

Mattermost notifies you of new activity you're directly involved in. How you're notified depends on what Mattermost client you're using, the type of Mattermost activity you're being notified about, and how you prefer to be notified.

.. include:: ../_static/badges/academy-notifications.rst
  :start-after: :nosearch:

Missing notifications? Visit our :doc:`troubleshoot notifications </preferences/troubleshoot-notifications>` documentation for guidance on ensuring notification delivery.

You're in control
------------------

You are in control of how, when, and where you're notified of activity that matters to you based on how you prefer to work and collaborate. To access notification preferences:

- In a web browser or the desktop app, select the **Settings** |gear| icon located in the top right corner of the screen to manage your notification preferences.
- On mobile, tap your profile picture, then tap **Settings > Notifications**.

See the `Default notifications <#default-notifications>`__ table below for details on customizing your notification experience based on your preferred Mattermost client.

.. tip::

  From Mattermost v9.8, your desktop and mobile notification preferences have been combined together under **Notifications**. If you're using an older Mattermost release and older Mattermost clients, you'll find separate preferences for desktop and mobile.

Default notifications
------------------------

Mattermost notifies you of new activity, including unread activity, :ref:`direct <collaborate/channel-types:direct messages>` and :ref:`group <collaborate/channel-types:group messages>` messages, and :doc:`@mentions </preferences/manage-your-mentions-keywords-notifications>`, :doc:`keywords </preferences/manage-your-mentions-keywords-notifications>` you're actively watching, :doc:`thread replies </preferences/manage-your-thread-reply-notifications>`, and unread activity in :doc:`specific channels </preferences/manage-your-channel-specific-notifications>`.

The table below lists the types of notifications you can expect to see and hear in Mattermost. Select your preferred Mattermost clients to learn more about notifications for that client.

+-----------------------+---------------------------------------------------+-------------------------------------------------------------------+
| **Notification Type** | **What it Means**                                 | **Which Mattermost Clients?**                                     |
+=======================+===================================================+===================================================================+
| Icon badge (dot)      | You have unread activity in at least 1 channel    | :doc:`Web </preferences/manage-your-web-notifications>`,          |
|                       | you're a member of                                | :doc:`Desktop </preferences/manage-your-desktop-notifications>`   |
| |dot-badge|           |                                                   |                                                                   |
+-----------------------+---------------------------------------------------+-------------------------------------------------------------------+
| Icon badge (number)   | You have at least 1 unread message with an        | :doc:`Web </preferences/manage-your-web-notifications>` &         |
|                       | @mention, or a match to a keyword you're watching | :doc:`Desktop </preferences/manage-your-desktop-notifications>`   |
| |numbered-badge|      |                                                   | & :doc:`Mobile </preferences/manage-your-mobile-notifications>`   |
+-----------------------+                                                   +-------------------------------------------------------------------+
| Banner alert popups   |                                                   | :doc:`Web </preferences/manage-your-web-notifications>` &         |
|                       |                                                   | :doc:`Desktop </preferences/manage-your-desktop-notifications>`   |
+-----------------------+                                                   +-------------------------------------------------------------------+
| Push notifications    |                                                   | :doc:`Mobile </preferences/manage-your-mobile-notifications>`     |
|                       |                                                   |                                                                   |
+-----------------------+---------------------------------------------------+-------------------------------------------------------------------+
| Alert sounds          | You have at least 1 unread message with an        | :doc:`Web </preferences/manage-your-web-notifications>`,          |
|                       | @mention, a match to a keyword you're watching,   | :doc:`Desktop </preferences/manage-your-desktop-notifications>`,  |
|                       | or replies to a thread you're following           | & :doc:`Mobile </preferences/manage-your-mobile-notifications>`   |
+-----------------------+---------------------------------------------------+-------------------------------------------------------------------+

Email notifications
~~~~~~~~~~~~~~~~~~~~

By default, Mattermost notifications are sent to you via email for :doc:`@mentions </collaborate/mention-people>` and :ref:`direct messages <collaborate/channel-types:direct messages>` when you are :ref:`offline or away <preferences/set-your-status-availability:set your availability>` from Mattermost for more than 5 minutes. 

You can disable email notifications by going to **Settings > Notifications > Email notifications** and changing **Immediately** to **Never**.

.. note::

  Mattermost can group multiple email notifications together into a single email. If your Mattermost admin :ref:`enables this feature <configure/site-configuration-settings:enable email batching>`, you'll receive batches of notifications by email every 15 minutes, or as configured by your admin.

Missing notifications?
----------------------

Visit the Mattermost `notifications Knowledge Base article <https://support.mattermost.com/hc/en-us/articles/19161390661780>`__ for additional troubleshooting tips and tricks.