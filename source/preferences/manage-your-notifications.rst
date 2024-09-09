Manage your notifications
=========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |gear| image:: ../images/settings-outline_F08BB.svg
  :alt: Use the Settings icon to customize your Mattermost user experience.
  :class: theme-icon

.. |channel-info| image:: ../images/information-outline_F02FD.svg
  :alt: Use the Channel Info icon to access additional channel management options.
  :class: theme-icon

.. |more-icon| image:: ../images/dots-horizontal_F01D8.svg
  :alt: Use the More icon to access additional message options.
  :class: theme-icon

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

    Manage your web notifications </preferences/manage-your-web-notifications>
    Manage your desktop notifications </preferences/manage-your-desktop-notifications>
    Manage your mobile notifications </preferences/manage-your-mobile-notifications>
    Manage your thread reply notifications </preferences/manage-your-thread-reply-notifications>
    Manage your @mention & keyword notifications </preferences/manage-your-mentions-keywords-notifications>
    Manage your channel-specific notifications </preferences/manage-your-channel-specific-notifications>

Mattermost notifies you of new activity. How you're notified depends on what Mattermost client you're using, and the type of Mattermost activity you're being notified about.

You're in control
------------------

By default Mattermost alerts you about all Mattermost activity all of the time.

.. include:: ../_static/badges/academy-notifications.rst
  :start-after: :nosearch:

You are in complete control of how, when, and where you're notified based on how you prefer to work and collaborate. To access notification preferences:

- In a web browser or the desktop app, select the **Settings** |gear| icon located in the top right corner of the screen to manage your notification preferences.
- On mobile, tap your profile picture, then tap **Settings**, and **Notifications**.

See the table below on `Mattermost notifications <#mattermost-notifications>`__ for details on customizing your notification experience based on your preferred Mattermost client.

.. tip::

  - From Mattermost v9.8, your desktop and mobile notification preferences have been combined together under **Settings > Notifications**. If you're using an older Mattermost release, you'll find these settings split out as desktop settings and mobile settings instead.

Mattermost notifications
------------------------

Mattermost notifies you of new activity, including unread activity, messages, and :doc:`@mentions </preferences/manage-your-mentions-keyword-notifications>`, :doc:`keywords </preferences/manage-your-mentions-keywords-notifications>` you're actively watching, :doc:`thread replies </preferences/manage-your-thread-reply-notifications>`, and unread activity in :doc:`specific channels </preferences/manage-your-channel-specific-notifications>`. 

The table below lists the types of notifications available in Mattermost. Select the Mattermost clients you use to access Mattermost to learn more about notifications specific to that client.

+-----------------------+---------------------------------------------------+-------------------------------------------------------------------+
| **Notification Type** | **Description**                                   | **Client Support**                                                |
+=======================+===================================================+===================================================================+
| Icon badge (dot)      | You have unread activity in at least              | :doc:`Web </preferences/manage-your-web-notifications>`,          |
|                       | one channel you're a member of                    | :doc:`Desktop </preferences/manage-your-desktop-notifications>`   |
| |dot-badge|           |                                                   |                                                                   |
+-----------------------+---------------------------------------------------+-------------------------------------------------------------------+
| Icon badge (number)   | You have at least one unread message,             | :doc:`Web </preferences/manage-your-web-notifications>` &         |
|                       | @mention, or a match to a keyword you're watching | :doc:`Desktop </preferences/manage-your-desktop-notifications>`   |
| |numbered-badge|      |                                                   | & :doc:`Mobile </preferences/manage-your-mobile-notifications>`   |
+-----------------------+---------------------------------------------------+-------------------------------------------------------------------+
| Popup banner alerts   | Example screenshots:                              | :doc:`Web </preferences/manage-your-web-notifications>` &         |
|                       |                                                   | :doc:`Desktop </preferences/manage-your-desktop-notifications>`   |
|                       | - web                                             |                                                                   |
|                       | - desktop                                         |                                                                   |
+-----------------------+---------------------------------------------------+-------------------------------------------------------------------+
| Push notifications    | example screenshot                                | :doc:`Mobile </preferences/manage-your-mobile-notifications>`     |
+-----------------------+---------------------------------------------------+-------------------------------------------------------------------+
| Alert sounds          | example screenshot                                | :doc:`Web </preferences/manage-your-web-notifications>`,          |
|                       | showing available sounds                          | :doc:`Desktop </preferences/manage-your-desktop-notifications>`,  |
|                       |                                                   | & :doc:`Mobile </preferences/manage-your-mobile-notifications>`   |
+-----------------------+---------------------------------------------------+-------------------------------------------------------------------+

Email notifications
~~~~~~~~~~~~~~~~~~~~

Mattermost notifications are also sent via email by default for :doc:`@mentions </collaborate/mention-people>` and :ref:`direct messages <collaborate/channel-types:direct messages>` when you are :ref:`offline or away <preferences/set-your-status-availability:set your availability>` from Mattermost for more than 5 minutes. You can disable email notifications by going to **Settings > Notifications > Email notifications** and changing **Immediately** to **Never**.

.. note::

  Mattermost also supports the ability to group multiple email notifications together into a single email. If your Mattermost admin :ref:`enables this feature <configure/site-configuration-settings:enable email batching>`, you'll receive batches of notifications by email every 15 minutes, or as configured by your admin.

Missing notifications?
----------------------

Visit the Mattermost `notifications Knowledge Base article <https://support.mattermost.com/hc/en-us/articles/19161390661780>`__ for additional troubleshooting tips and tricks.