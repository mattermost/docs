Manage your web notifications
==============================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

|chrome-badge|

|safari-badge|

|firefox-badge|

|edge-badge|

Enable notifications
--------------------

From Mattermost v9.9, Mattermost prompts you to enable notifications.

- When you select **Enable notifications**, you won't be asked again, and you'll start receiving Mattermost notifications in the web browser.
- If you dismiss the prompt, you won't receive notifications in the web browser, and you'll prompted again the next time you open Mattermost in a browser.

.. image:: ../images/enable-notifications.png
  :alt: From Mattermost v9.9, you're prompted to enable notifications.

When notifications are enabled, you're notified of all Mattermost activity by default with `badges <#badge-based-notifications>`__ and `sounds <#notification-sounds>`__. You can `customize your web-based notifications <#customize-your-notifications>`__ for Mattermost activity.

Badge-based notifications
-------------------------

Badges display in a supported browser's site tab as an asterisk (*) and includes a message count.

black vs red badges?

+-------------+-----------------+
| **Browser** | **Badge**       |
+=============+=================+
| Chrome      | |chrome-badge|  |
+-------------+-----------------+
| Safari      | |safari-badge|  |
+-------------+-----------------+
| Firefox     | |firefox-badge| |
+-------------+-----------------+
| Edge        | |edge-badge|    |
+-------------+-----------------+

Notification sounds
--------------------

By default, message notifications include audible sounds.

Customize your notifications
----------------------------

.. tip::

  Mattermost notification settings labeled as Desktop also configure your web-based notifications when using Mattermost in a web browser.

To reduce the number of notifications you receive, select **Desktop and mobile notifications > Mentions, direct messages, and group messages**, and save your changes. With limited notifications enabled, you can also choose to receive notifications about replies to threads you're following by selecting **Notify me about replies to threads I'm following**.

You can change or disable notification sounds by going to **Desktop notification sounds > Message notification sound**.

Want to hear a sound when a Mattermost call starts? If your Mattermost admin :ref:`enables this Beta feature <configure/plugins-configuration-settings:enable call ringing>`, you can choose the sound that plays when a call is started within a direct or group message you're participating in by going to **Desktop notification sounds > Incoming call sound**.

Disable all desktop notifications
-----------------------------------

Select **Desktop and mobile notifications > Nothing** to disable all web and :doc:`desktop notifications </preferences/manage-your-desktop-notifications>`. 

Clear the **Use different settings for my mobile devices** to additionally disable all Mattermost mobile notifications everywhere you use Mattermost.