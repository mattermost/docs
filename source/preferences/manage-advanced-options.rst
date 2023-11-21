Manage advanced options
=======================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |gear-icon| image:: ../images/settings-outline_F08BB.svg
  :alt: Access settings using the gear icon.

.. |send-icon| image:: ../images/send_F048A.svg
  :alt: Select the Send icon to post your message.

To customize Mattermost display options based on your preferences, select the gear icon |gear-icon| next to your profile picture, then go to **Advanced**.

Send messages on CTRL/⌘+ENTER
------------------------------

By default, you send messages in Mattermost by composing a message in the message text box at the bottom of the Mattermost screen and selecting the **Send** |send-icon| icon or by pressing :kbd:`Enter` on Windows or Linux, or :kbd:`↵` on Mac.

And you enter new text lines by pressing :kbd:`Shift` :kbd:`Enter` on Windows or Linux, or :kbd:`⇧` :kbd:`↵` on Mac before sending the message.

You can chance this message send behavior.

.. tab:: Web/Desktop

    If you find you're accidentally sending messages too soon, you can configure Mattermost to require an extra keystroke to send all messages, or for code blocks.
    
    Select **Send Messages on CTRL/⌘ + ENTER > Edit** to configure how messages are sent in Mattermost.

    You can configure Mattermost to send messages by pressing :kbd:`Ctrl` :kbd:`Enter` on Windows or Linux, or :kbd:`⌘` :kbd:`↵` on Mac for all messages or only for code blocks that start with ```````. 

.. tab:: Mobile

    This option isn't something you can set using the mobile app.

Enable post formatting
----------------------

By default, Mattermost formats your messages with Markdown to show links, emojis, text styles, and line breaks. You can control whether your messages show the formatting or show text only.

.. tab:: Web/Desktop

    Select **Enable Post Formatting** to show your messages as raw text only that includes Markdown syntax.

.. tab:: Mobile

    This option isn't something you can set using the mobile app.

Enable join/leave messages
--------------------------

By default, Mattermost shows you system messages when users join or leave channels you're a member of. You can hide these messages if preferred.

.. tab:: Web/Desktop

    Select **Enable Join/Leave Messages** to hide the system messages when users join  or leave channels you're a member of. When users are added to or removed from a channel, a system message displays even when you've disabled this feature.

.. tab:: Mobile

    This option isn't something you can set using the mobile app.

Deactivate account
------------------

You can deactivate your account if you access Mattermost using an email address and password, and when your system admin has `enabled your ability to do so </configure/experimental-configuration-settings.html#exp-enableaccountdeactivation>`__. Deactivating your account removes your ability to access Mattermost, and disables all email and mobile notifications.

.. important::

    - If you deactive your account, you must contact your system admin to have it reactivated.
    - If you access Mattermost using another authentication method, such as AD/LDAP or SAML, or use accounts that don't have this setting available, contact your system admin to deactivate your account in the System Console.

.. tab:: Web/Desktop

    Select **Deactivate Account** to deactivate your Mattermost user account.

.. tab:: Mobile

    This option isn't applicable to the mobile app.

Performance debugging
---------------------

You can disable key Mattermost features temporarily to help isolate issues while debugging Mattermost, if your system admin `enables your ability to do so </configure/environment-configuration-settings.html#dev-enableclientdebugging>`__. We don't recommend leaving these settings enabled for an extended period of time as they can negatively impact your user experience.

.. tab:: Web/Desktop

    Select **Performance Debugging** to disable one or more of the following Mattermost features:

    - Client-side plugins
    - telemetry events sent from the client
    - "User is typing..." messages

    You may need to refresh Mattermost to see these settings take effect.

.. tab:: Mobile

    This option isn't something you can set using the mobile app.

Scroll position when viewing unread channels
--------------------------------------------

You can choose where to start viewing unread messages in all channels you're a member of.

.. tab:: Web/Desktop

    Select **Scroll position when viewing an unread channel** to choose your scroll position starting point as where you left off or at the newest message.

.. tab:: Mobile

    This option isn't something you can set using the mobile app.

Allow message drafts to sync with the server
--------------------------------------------

By default, `message drafts </send-messages.html#draft-messages>`__ are synchronized on the Mattermost server and accessible everywhere you access Mattermost using a web browser or the desktop app. You can disable server-synchronized drafts and limit drafts to your current Mattermost client, if preferred.

.. tab:: Web/Desktop

    Select **Allow message drafts to sync with the server** to disable server-synchronized drafts.

.. tab:: Mobile

    This option isn't applicable to the mobile app.

Allow Mattermost to prefetch channel posts
------------------------------------------

By default, Mattermost pre-fetches messages and user information when you start Mattermost in a browser. You can disable webapp pre-fetching so that Mattermost prefetches messages and user information as you open channels instead. Disabling prefetch is recommended for users with a high unread channel count in order to improve application performance.

.. tab:: Web/Desktop

    Select **Allow Mattermost to prefetch channel posts** to disable webapp pre-fetching on startup, and pre-fetch the data as you open channels.

.. tab:: Mobile

    This option isn't applicable to the mobile app.

Delete local files
------------------

You can delete local Mattermost files from your mobile device using the mobile app.

.. tab:: Mobile

    Access **Settings** by tapping on your profile picture. Then, tap **Advanced Settings** and **Delete local files**.

    Only data specific to the current Mattermost server is removed from your device. You'll need to repeat this process for each `Mattermost workspace you're connected to </preferences/connect-multiple-workspaces.html>`__ on the mobile app.

.. tab:: Web/Desktop

    This option isn't applicable to the web or desktop app instance of Mattermost.