React with emojis and GIFs
===========================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |smile-icon| image:: ../images/smile-icon.png
  :alt: Smile icon

Emojis and GIFs are small, digital images, animated images, or icons you can use to communicate or express concepts such as emotions, humor, and physical gestures in your messages. 

Quick emoji reactions
-----------------------

Hover over a message to react quickly using your most recent emojis. You can react with up to 50 emojis per message.

    .. image:: ../images/recent-emojis.png
      :alt: React to messages quickly by selecting one of your most recently used emojis.

Recently used emojis are sorted based on how often you've used them.

.. tip::
  
  If you don't see your most recently used emojis, enable quick reactions by selecting **Settings > Display > Quick reactions on messages**.

Include emojis and GIFs in messages
-----------------------------------

.. tab:: Web/desktop

  Select the **Smile** icon |smile-icon| inside the Mattermost message input box to open the emoji and GIF picker. 

  Select an emoji from the **Emojis** tab, or switch to the **GIFs** tab to search for a GIF.

  You can also specify emojis based on their name. Type ``:`` followed by at least two characters of the word describing the emoji. This opens an emoji autocomplete. Descriptions include skin tone details for people-based emojis, where supported.

  .. image:: ../images/emojiautocomplete.png
    :alt: Emoji autocomplete

  .. tip::

    Can't find the perfect emoji? You can `upload your own custom emoji <#upload-custom-emojis>`__ if your system admin has `enabled you to do so </configure/site-configuration-settings.html#emoji-enablecustom>`__.

.. tab:: Mobile

  Long press on a message, and then select a recently used emoji, or select the |smile-icon| to add a different reaction. Mattermost accesses the emojis and GIFs available on your mobile device.

Manage emojis
-------------

Using Mattermost in a web browser or the desktop app, you can select recently used emojis, select a default skin tone for people-based emojis, as well as manage custom emojis.

Select default skin tone
~~~~~~~~~~~~~~~~~~~~~~~~

Select the **Skin tone** icon in the top right corner of the emoji picker to specify the skin tone you prefer to use for people-based emojis by default. You can select an alternate skin tone at any time.

.. image:: ../images/emoji-skin-tone.png
  :alt: Select a default skin tone preference for people-based emojis.

Upload custom emojis
~~~~~~~~~~~~~~~~~~~~

Using Mattermost in a web browser or the desktop app, you can upload new emojis that everyone in your Mattermost workspace can access to react to messages. From the emoji picker, select **Custom Emoji**. Small, square pictures work best when selecting an image to upload. The file can be any JPG, GIF, or PNG that's up to 512 KiB in size.

1. Enter a name for your custom emoji. This is the name that shows up in the emoji autocomplete.
2. Choose **Select**, then select the image to use for the emoji.
3. Select **Save**. Once saved, your emoji is added to the list of custom emoji.

.. image:: ../images/add_custom_emoji.png
  :alt: You can upload custom emojis to Mattermost.

4. To use your custom emoji in a message, select it from the emoji picker, or type ``:`` followed by your emoji name to bring it up in the emoji autocomplete.

.. note::

  If you can't see the **Custom Emoji** option, your Mattermost system admin may have restricted access to upload custom emoji. Contact your Mattermost system admin for assistance.
  
Remove custom emojis
~~~~~~~~~~~~~~~~~~~~

Using Mattermost in a web browser or the desktop app, you can remove custom emojis that you uploaded to Mattermost.

1. Open the emoji picker.
2. Select **Custom Emoji**.
3. If required, use the Search bar to find your custom emoji in the list.
4. Under **Actions** select **Delete**.
5. Choose **Delete** to confirm.

.. image:: ../images/delete_custom_emoji.png
  :alt: Remove custom emoji
