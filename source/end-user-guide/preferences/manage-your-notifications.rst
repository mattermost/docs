Manage your notifications
=========================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

.. |dot-badge| image:: ../../images/dot-badge.png
    :alt: A dot on the badge means you have unread activity in at least one channel you're a member of.
    :width: 50px
.. |numbered-badge| image:: ../../images/numbered-badge.png
    :alt: A numbered badge means you have at least 1 unread message, @mention, or one of your keywords has triggered a notification.
    :width: 50px

.. toctree::
  :maxdepth: 1
  :hidden:
  :titlesonly:

    Troubleshoot notifications </end-user-guide/preferences/troubleshoot-notifications>
    Manage your web notifications </end-user-guide/preferences/manage-your-web-notifications>
    Manage your desktop notifications </end-user-guide/preferences/manage-your-desktop-notifications>
    Manage your mobile notifications </end-user-guide/preferences/manage-your-mobile-notifications>
    Manage your thread reply notifications </end-user-guide/preferences/manage-your-thread-reply-notifications>
    Manage your @mention & keyword notifications </end-user-guide/preferences/manage-your-mentions-keywords-notifications>
    Manage your channel-specific notifications </end-user-guide/preferences/manage-your-channel-specific-notifications>

Mattermost notifies you of new activity you're directly involved in. How you're notified depends on what Mattermost client you're using, the type of Mattermost activity you're being notified about, and how you prefer to be notified.

.. tip::

  **Missing notifications?**

  - Your mobile device may have Mattermost notifications disabled. See the :ref:`manage your mobile notifications <end-user-guide/preferences/manage-your-mobile-notifications:enable notifications>` for details.
  - You may need to grant permissions in the Mattermost :ref:`desktop app <end-user-guide/preferences/manage-your-desktop-notifications:enable notifications>` or :ref:`web browser <end-user-guide/preferences/manage-your-web-notifications:enable notifications>` to show notifications.
  - Visit our :doc:`troubleshoot notifications </end-user-guide/preferences/troubleshoot-notifications>` documentation for guidance on ensuring you receive Mattermost notifications.

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

Mattermost notifies you of new activity, including unread activity, :ref:`direct <end-user-guide/collaborate/channel-types:direct message channels>` and :ref:`group <end-user-guide/collaborate/channel-types:group message channels>` messages, and :doc:`@mentions </end-user-guide/preferences/manage-your-mentions-keywords-notifications>`, :doc:`keywords </end-user-guide/preferences/manage-your-mentions-keywords-notifications>` you're actively watching, :doc:`thread replies </end-user-guide/preferences/manage-your-thread-reply-notifications>`, and unread activity in :doc:`specific channels </end-user-guide/preferences/manage-your-channel-specific-notifications>`.

The table below lists the types of notifications you can expect to see and hear in Mattermost. Select your preferred Mattermost clients to learn more about notifications for that client.

+-----------------------+---------------------------------------------------+----------------------------------------------------------------------------------+
| **Notification Type** | **What it Means**                                 | **Which Mattermost Clients?**                                                    |
+=======================+===================================================+==================================================================================+
| Icon badge (dot)      | You have unread activity in at least 1 channel    | :doc:`Web </end-user-guide/preferences/manage-your-web-notifications>`,          |
|                       | you're a member of                                | :doc:`Desktop </end-user-guide/preferences/manage-your-desktop-notifications>`   |
| |dot-badge|           |                                                   |                                                                                  |
+-----------------------+---------------------------------------------------+----------------------------------------------------------------------------------+
| Icon badge (number)   | You have at least 1 unread message with an        | :doc:`Web </end-user-guide/preferences/manage-your-web-notifications>` &         |
|                       | @mention, or a match to a keyword you're watching | :doc:`Desktop </end-user-guide/preferences/manage-your-desktop-notifications>`   |
| |numbered-badge|      |                                                   | & :doc:`Mobile </end-user-guide/preferences/manage-your-mobile-notifications>`   |
+-----------------------+                                                   +----------------------------------------------------------------------------------+
| Banner alert popups   |                                                   | :doc:`Web </end-user-guide/preferences/manage-your-web-notifications>` &         |
|                       |                                                   | :doc:`Desktop </end-user-guide/preferences/manage-your-desktop-notifications>`   |
+-----------------------+                                                   +----------------------------------------------------------------------------------+
| Push notifications    |                                                   | :doc:`Mobile </end-user-guide/preferences/manage-your-mobile-notifications>`     |
|                       |                                                   |                                                                                  |
+-----------------------+---------------------------------------------------+----------------------------------------------------------------------------------+
| Alert sounds          | You have at least 1 unread message with an        | :doc:`Web </end-user-guide/preferences/manage-your-web-notifications>`,          |
|                       | @mention, a match to a keyword you're watching,   | :doc:`Desktop </end-user-guide/preferences/manage-your-desktop-notifications>`,  |
|                       | or replies to a thread you're following           | & :doc:`Mobile </end-user-guide/preferences/manage-your-mobile-notifications>`   |
+-----------------------+---------------------------------------------------+----------------------------------------------------------------------------------+

Email notifications
~~~~~~~~~~~~~~~~~~~~

When your admin :ref:`enables email notifications <administration-guide/configure/site-configuration-settings:enable email notifications>`, Mattermost notifications are sent to you via email for :doc:`@mentions </end-user-guide/collaborate/mention-people>` and :ref:`direct messages <end-user-guide/collaborate/channel-types:direct message channels>` as soon as you're away from Mattermost for 5 minutes.

You can also opt in to be notified by email about thread replies you're following.

Additionally, if your admin :ref:`enables email batching <administration-guide/configure/site-configuration-settings:enable email batching>`, email-based notifications are batched, and you can customize how frequenly you receive batched notifications by going to **Settings > Notifications > Email notifications**. The default frequency is 15 minutes. Choosing every 15 minutes or every hour will reduce the number of emails you receive.

Disable email notifications by going to **Settings > Notifications > Email notifications** and changing **On** to **Off**.

Missing notifications?
----------------------

Visit the Mattermost `notifications Knowledge Base article <https://support.mattermost.com/hc/en-us/articles/19161390661780-Troubleshooting-Mattermost-Notifications>`_ for additional troubleshooting tips and tricks.