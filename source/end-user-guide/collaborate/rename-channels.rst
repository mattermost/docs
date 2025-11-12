Rename channels
===============

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Anyone can rename the channels they belong to, unless the system admin has :doc:`restricted the permissions to do so using advanced permissions </administration-guide/onboard/advanced-permissions>`.

.. tab:: Web/Desktop

  Select the channel name at the top of the center pane to access the drop-down menu, then select **Channel Settings**. You'll be prompted to provide two pieces of information:

  - **Channel name:** The channel name that displays in the Mattermost user interface for all users. Enter a different channel name if needed or preferred.
  - **Channel URL:** The web URL used to access the channel in a web browser. Select **Edit** to change the URL, and select **Done** to save your changes.

  If your system admin has enabled :ref:`channel category sorting <administration-guide/configure/experimental-configuration-settings:enable channel category sorting>`, you can assign the renamed channel to a new or existing channel category. 

  For example, a channel could be named ``UX Design`` and have a URL of ``https://community.mattermost.com/core/channels/ux-design``.

.. tab:: Mobile

  1. Tap the channel you want to rename.

    .. image:: ../../images/mobile-select-a-channel.jpg
      :alt: Select a channel that you want to rename.
      :scale: 30

  2. Tap the **More** |more-icon-vertical| icon located in the top right corner of the app.

    .. image:: ../../images/mobile-select-more-options-for-a-channel.jpg
      :alt: Tap on More options to access available options for the channel.
      :scale: 30

  3. Tap **View info**.

    .. image:: ../../images/mobile-select-view-info-for-a-channel.jpg
      :alt: Tap on View info to see the basic channel info.
      :scale: 30

  4. Tap **Edit Channel**.

    .. image:: ../../images/mobile-edit-channel.jpg
      :alt: Click on Edit channel to rename the channel.
      :scale: 25

  5. You're prompted to provide three pieces of information:

    - **Name:** This appears in the Mattermost user interface.
    - **Purpose:** (Optional) Used to describe the channel's function or goal.
    - **Header:** (Optional) Used to include information relevant to the channel, such as key contacts or document links.


    Tap on **Save** to save the new channel name.

    .. image:: ../../images/mobile-rename-channel-name-and-save.jpg
      :alt: Type the new channel name and click on Save to rename the channel.
      :scale: 30
