Manage your notifications
=========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

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

Mattermost notifies you of new activity. How you're notified depends on what Mattermost client you're using, the type of Mattermost activity you're being notified about, and how you prefer to be notified.

You're in control
------------------

By default Mattermost alerts you about all Mattermost activity all of the time.

.. include:: ../_static/badges/academy-notifications.rst
  :start-after: :nosearch:

You are in complete control of how, when, and where you're notified based on how you prefer to work and collaborate. To access notification preferences:

- In a web browser or the desktop app, select the **Settings** |gear| icon located in the top right corner of the screen to manage your notification preferences.
- On mobile, tap your profile picture, then tap **Settings**, and **Notifications**.

See the `Mattermost notifications <#default-notifications>`__ table below for details on customizing your notification experience based on your preferred Mattermost client.

.. tip::

  From Mattermost v9.8, your desktop and mobile notification preferences have been combined together under **Settings > Notifications**. If you're using an older Mattermost release, you'll find these settings split out as desktop settings and mobile settings instead.

Default notifications
------------------------

Mattermost notifies you of new activity, including unread activity, :ref:`direct <collaborate/channel-types:direct messages>` and :ref:`group <collaborate/channel-types:group messages>` messages, and :doc:`@mentions </preferences/manage-your-mentions-keyword-notifications>`, :doc:`keywords </preferences/manage-your-mentions-keywords-notifications>` you're actively watching, :doc:`thread replies </preferences/manage-your-thread-reply-notifications>`, and unread activity in :doc:`specific channels </preferences/manage-your-channel-specific-notifications>`.

The table below lists the types of notifications you can expect to receive in Mattermost. Select your preferred Mattermost clients to learn more about client-specific notifications.

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
| Banner alerts         | Example screenshot                                | :doc:`Web </preferences/manage-your-web-notifications>` &         |
|                       |                                                   | :doc:`Desktop </preferences/manage-your-desktop-notifications>`   |
+-----------------------+---------------------------------------------------+-------------------------------------------------------------------+
| Push notifications    | example screenshot                                | :doc:`Mobile </preferences/manage-your-mobile-notifications>`     |
+-----------------------+---------------------------------------------------+-------------------------------------------------------------------+
| Alert sounds          |                                                   | :doc:`Web </preferences/manage-your-web-notifications>`,          |
|                       |                                                   | :doc:`Desktop </preferences/manage-your-desktop-notifications>`,  |
|                       |                                                   | & :doc:`Mobile </preferences/manage-your-mobile-notifications>`   |
+-----------------------+---------------------------------------------------+-------------------------------------------------------------------+

Email notifications
~~~~~~~~~~~~~~~~~~~~

Mattermost notifications are also sent via email by default for :doc:`@mentions </collaborate/mention-people>` and :ref:`direct messages <collaborate/channel-types:direct messages>` when you are :ref:`offline or away <preferences/set-your-status-availability:set your availability>` from Mattermost for more than 5 minutes. You can disable email notifications by going to **Settings > Notifications > Email notifications** and changing **Immediately** to **Never**.

.. note::

  Mattermost can group multiple email notifications together into a single email. If your Mattermost admin :ref:`enables this feature <configure/site-configuration-settings:enable email batching>`, you'll receive batches of notifications by email every 15 minutes, or as configured by your admin.

Missing notifications?
----------------------

Visit the Mattermost `notifications Knowledge Base article <https://support.mattermost.com/hc/en-us/articles/19161390661780>`__ for additional troubleshooting tips and tricks.