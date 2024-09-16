Manage your desktop notifications
=================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

Enable notifications
--------------------

From Mattermost v9.9, Mattermost prompts you to enable notifications in the desktop app.

- When you select **Enable notifications**, you won't be asked again, and you'll start receiving Mattermost notifications in the web browser.
- If you dismiss the prompt, you won't receive notifications in the web browser, and you'll prompted again the next time you open Mattermost in a browser.

.. image:: ../images/enable-notifications.png
  :alt: From Mattermost v9.9, you're prompted to enable notifications.

When notifications are enabled, you're notified of all Mattermost activity by default with `badges <#badge-based-notifications>`__, `banner alerts <#banner-alerts>`__ and `sounds <#notification-sounds>`__. You can `customize your desktop-based notifications <#customize-your-notifications>`__ for Mattermost activity.

Badge-based notifications
-------------------------

Mattermost desktop app icons display the following types of badges:

- A dot badge indicates unread activity. |dot-badge|
- A number badge indicates unread messages, @mentions, or keywords. |numbered-badge|

Banner alerts
-------------

Banner alerts in the desktop app are popup windows that appear in the top right corner of the screen for a limited time that include activity details.

Notification sounds
--------------------

By default, message notifications include audible sounds.

Customize your notifications
----------------------------

Reduce notifications
~~~~~~~~~~~~~~~~~~~~

To reduce the number of notifications you receive, select **Desktop and mobile notifications > Mentions, direct messages, and group messages**, and save your changes. With limited notifications enabled, you can also choose to receive notifications about replies to threads you're following by selecting **Notify me about replies to threads I'm following**.

Notification sounds
~~~~~~~~~~~~~~~~~~~~

You can change or disable notification sounds by going to **Desktop notification sounds > Message notification sound**.

Incoming Call notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Want to hear a sound when a Mattermost call starts? If your Mattermost admin :ref:`enables this Beta feature <configure/plugins-configuration-settings:enable call ringing>`, you can choose the sound that plays when a call is started within a direct or group message you're participating in by going to **Desktop notification sounds > Incoming call sound**.

Disable all desktop notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select **Desktop and mobile notifications > Nothing** to disable all desktop and :doc:`web notifications </preferences/manage-your-web-notifications>`.

Clear the **Use different settings for my mobile devices** to additionally disable all Mattermost mobile notifications everywhere you use Mattermost.

Frequently asked questions
---------------------------

Why am I prompted repeatedly enable notifications I don't want?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost will continue to prompt you to enable notifications in the desktop app until you respond to the prompt. If you want to disable all Mattermost notifications, select **Enable notifications** when prompted, and then `disable all Mattermost desktop notifications <#disable-all-desktop-notifications>`__.