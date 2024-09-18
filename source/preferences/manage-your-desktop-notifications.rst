Manage your desktop notifications
=================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |dot-badge| image:: ../images/dot-badge.png
  :alt: A dot on the badge means you have unread activity in at least one channel you're a member of.
  :width: 50px

.. |numbered-badge| image:: ../images/numbered-badge.png
  :alt: A numbered badge means you have at least 1 unread message, @mention, or one of your keywords has triggered a notification.
  :width: 50px

Enable notifications
--------------------

From Mattermost v9.9, Mattermost prompts you to enable notifications in the desktop app.

.. image:: ../images/enable-notifications.png
  :alt: From Mattermost v9.9, you're prompted to enable notifications.

- When you select **Enable notifications**, you won't be asked again. You'll start receiving notifications for all Mattermost activity with `badges <#badge-based-notifications>`__, `banner alerts <#banner-alerts>`__ and `sounds <#notification-sounds>`__. See the section below on `customizing your notifications <#customize-your-notifications>`__ based on how you prefer to be notified about Mattermost activity in the desktop app.
- If you dismiss this prompt, you won't receive Mattermost notifications in the web browser, and you'll prompted again the next time you open Mattermost in a web browser.

Badge-based notifications
-------------------------

Mattermost desktop app icons display the following types of badges:

- A numbered badge for unread :ref:`direct <collaborate/channel-types:direct messages>` and :ref:`group <collaborate/channel-types:group messages>` messages, and :doc:`@mentions </preferences/manage-your-mentions-keywords-notifications>`, :doc:`keywords </preferences/manage-your-mentions-keywords-notifications>` you're actively watching. |numbered-badge|
- A dot badge for unread activity. |dot-badge|


Banner alerts
-------------

Banner alerts in the desktop app are popup windows that display for a limited time in the top right corner of your screen that summarizes the new activity.

Notification sounds
--------------------

By default, desktop app notifications include audible sounds.

Customize your notifications
----------------------------

.. tip::

  Mattermost notification settings labeled as Desktop also configure your web-based notifications when using Mattermost in a web browser.

Reduce desktop notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To reduce the number of notifications you receive, select **Desktop and mobile notifications > Mentions, direct messages, and group messages**, and save your changes. 

With limited notifications enabled, you can also choose to receive notifications about replies to threads you're following by selecting **Notify me about replies to threads I'm following**.

Notification sounds
~~~~~~~~~~~~~~~~~~~~

You can change or disable notification sounds by going to **Desktop notification sounds > Message notification sound**.

Incoming Call notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Want to hear a sound when a Mattermost call starts? If your Mattermost admin :ref:`enables this Beta feature <configure/plugins-configuration-settings:enable call ringing>`, you can choose the sound that plays when a call is started within a direct or group message by going to **Desktop notification sounds > Incoming call sound**.

Disable all desktop notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select **Desktop and mobile notifications > Nothing** to disable all desktop and :doc:`web notifications </preferences/manage-your-web-notifications>`.

Clear the **Use different settings for my mobile devices** to additionally disable all Mattermost mobile notifications everywhere you use Mattermost.

Frequently asked questions
---------------------------

Why am I prompted repeatedly enable notifications I don't want?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost will continue to prompt you to enable notifications in the desktop app until you respond to the prompt. If you want to disable all Mattermost notifications, select **Enable notifications** when prompted, and then `disable all Mattermost desktop notifications <#disable-all-desktop-notifications>`__.