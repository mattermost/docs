Manage your display options
===========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |gear-icon| image:: ../images/settings-outline_F08BB.svg
  :alt: Access settings using the gear icon.
  :class: theme-icon

To customize Mattermost display options based on your preferences, select the gear icon |gear-icon| next to your profile picture, then go to **Display**. 

Theme
-----

.. tab:: Web/Desktop

    Select **Theme** to apply a different look and feel to your Mattermost screen.

    Select **Theme Colors** to select one of 5 standard themes designed by the Mattermost team. Or, select **Custom Theme** to customize a standard theme even further.

.. tab:: Mobile

    Access **Settings** by tapping on your profile picture. Then, tap **Display** and **Theme**.

Customize a theme
-----------------

Using Mattermost in a web browser or the desktop app, you can customize any of the standard themes by selecting a standard theme and then selecting **Custom Theme** to load the standard theme into the custom theme color selectors.

Select **Custom Theme** to customize your theme colors and share them with others by copying and pasting theme vectors into the input box. Observe a live preview as you customize theme colors, then select **Save** to confirm your changes. Discard your changes by selecting **Cancel**, or by exiting the settings modal and selecting **Yes, Discard**. See the :doc:`customize your theme </preferences/customize-your-theme>` documentation to learn more about working with the custom theme color selectors.

.. tip::
  In Enterprise edition, if you are a member of multiple teams, you can optionally select the checkbox **Apply new theme to all my teams** to have the theme show up across teams. Otherwise, the changes will only apply to the current team.

Import a Slack theme
~~~~~~~~~~~~~~~~~~~~

Using Mattermost in a web browser or the desktop app, you can select **Import theme colors from Slack** to import a Slack theme. 

In Slack, go to **Preferences > Sidebar Theme** and open the custom theme option. From there, copy the theme color vector and then paste it into the **Input Slack Theme** input box in Mattermost. Any theme settings that are not customizable in Slack will default to the “Sapphire” standard theme settings.

Collapsed reply threads
-----------------------

Collapsed Reply Threads offers an enhanced experience for users communicating in threads and replying to messages. Collapsed Reply Threads are generally available in Mattermost Cloud and from self-hosted Mattermost v7.0, and are enabled by default for all new Mattermost deployments. 

Depending on how your System Admin has enabled **Collapsed Reply Threads** for your workspace, it may already be enabled for you, or you may be able to enable this feature for your account. See our :doc:`organize conversations using Collapsed Reply Threads </collaborate/organize-conversations>` documentation to learn more about working with Collapsed Reply Threads.

.. tab:: Web/Desktop

    Select **Collapsed Reply Threads > Edit** to manage this option.

.. tab:: Mobile

    Access **Settings** by tapping on your profile picture. Then, tap **Display** and **Collapsed Reply Threads**.

Clock display
-------------

You can customize how time is displayed in Mattermost.

.. tab:: Web/Desktop

    Select **Clock Display > Edit** to display time in Mattermost using a 12-hour or 24-hour convention.

.. tab:: Mobile

    Access **Settings** by tapping on your profile picture. Then, tap **Display** and **Clock Display**.

Teammate name display
---------------------

You can customize how names are displayed in Mattermost unless your system admin has :ref:`disabled your ability to do so <configure/site-configuration-settings:lock teammate name display for all users>`.

.. tab:: Web/Desktop
    
    Select **Teammate Name Display > Edit** to control how names are displayed in Mattermost. Options include: username, nickname (if it exists), or first and last name.

.. tab:: Mobile

    This option isn't something you can set using the mobile app.

Show online availability on profile images
------------------------------------------

You can show or hide :ref:`availability <preferences/set-your-status-availability:set your availability>` on profile pictures in Mattermost.

.. tab:: Web/Desktop

    Select **Show online availability on profile images > Edit** to show or hide availability in Mattermost.

.. tab:: Mobile

    This option isn't something you can set using the mobile app.

Share last active time
----------------------

By default, Mattermost shows when you were last online in your profile and in direct message channel headers, unless your system admin has :ref:`disabled this option <configure/site-configuration-settings:enable last active time>`.

.. tab:: Web/Desktop

    Select **Share last active time > Edit** to show or hide when you were last online in Mattermost.

.. tab:: Mobile

    This option isn't something you can set using the mobile app.

Timezone
--------

You can customize the timezone used for timestamps in Mattermost and in email notifications.

.. tab:: Web/Desktop

    Select **Timezone > Edit** to select your timezone.

.. tab:: Mobile

    Access **Settings** by tapping on your profile picture. Then, tap **Display** and **Timezone**.

Website link previews
---------------------

You can control whether website link previews in Mattermost show a preview of the website content directly below the message.

.. note::

    Your system admin must :ref:`enable this feature <configure/site-configuration-settings:enable message link previews>`. It's disabled by default. Once enabled, only the first web link in a message creates a preview of the website.

.. tab:: Web/Desktop

    Select **Website Link Previews > Edit** to show or hide website previews in messages.

.. tab:: Mobile

    This option isn't something you can set using the mobile app.

Default appearance of image previews
------------------------------------

When messages in Mattermost include images, you can control whether an image preview displays directly below the message for image attachments, image link previews, and :ref:`in-line images <collaborate/format-messages:in-line images>` over 100px in height.

.. tab:: Web/Desktop

    Select **Default Appearance of Image Previews > Edit** to expand or collapse all image links and image attachments.

    .. tip::
        This setting can also be controlled using the :doc:`slash commands </collaborate/run-slash-commands>` ``/expand`` and ``/collapse``.

.. tab:: Mobile

    This option isn't something you can set using the mobile app.

Message display
----------------

You can control how messages in a channel are displayed.

.. tab:: Web/Desktop

    Select **Message Display > Edit** to display standard or compact messages.

    .. tip::

        **Compact** mode fits more messages on the screen by decreasing the spacing around posts, collapsing link previews, and hiding thumbnails so that only file names are shown. Some formatting types, such as block quotes and headings, are also reduced in size.

        When you select **Compact**, usernames are colorized by default, and username colors are consistent for all users. Disable the **Colorize usernames** option to display all usernames in a single color instead.

.. tab:: Mobile

    This option isn't something you can set using the mobile app.


Click to open threads
----------------------

By default, Mattermost opens reply threads in the right pane when you select any part of a message. You can change this default behavior.

.. tab:: Web/Desktop

    Select **Click to open threads > Edit** to disable the default behavior of opening reply threads in the right pane automatically. You'll need to select the replies count to open a reply thread.

.. tab:: Mobile

    This option isn't something you can set using the mobile app.

Channel display
----------------

You can control the width of the center channel area in Matermost.

.. tab:: Web/Desktop

    Select **Channel Display  > Edit** to specify the center channel as fixed width and centered, or full width.

.. tab:: Mobile

    This option isn't something you can set using the mobile app.

Quick reactions on messages
---------------------------

By default, you can hover over messages to react using recently-used emojis. You can hide your recently-used emojis instead if preferred.

.. tab:: Web/Desktop

    Select **Quick reactions on messages > Edit** to hide your recently-used emojis.

.. tab:: Mobile

    This option isn't something you can set using the mobile app.

Language
--------

You can control what language Mattermost displays in. Options include:

- Deutsch - German
- English (U.S.)
- English Australian
- Español - Spanish
- Français - French
- Italiano - Italian
- Magyar - Hungarian
- Nederlands - Dutch
- Polski - Polish
- Português (Brasil) - Portuguese
- Română - Romanian
- Svenska - Swedish
- Tiếng Việt - Vietnamese
- Türkçe - Turkish
- български - Bulgarian
- Pусский - Russian
- Yкраїнська - Ukrainian
- فارسی - Persian
- 한국어 - Korean
- 中文 (简体) - Simplified Chinese
- 中文 (繁體) - Traditional Chinese
- 日本語 - Japanese

.. tab:: Web/Desktop

    Select **Language > Edit** to set the display language in Mattermost.

.. tab:: Mobile

    This option isn't something you can set using the mobile app. However, when you change the display language using a web browser or the desktop app, that language selection is also applied to the mobile app.