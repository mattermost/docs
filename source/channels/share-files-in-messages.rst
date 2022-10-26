Share files in messages
=======================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. |attachment-icon| image:: ../images/attachment-icon.png
  :alt: Use the Attachment icon to share files with messages.

.. |download-icon| image:: ../images/download-outline_F0B8F.svg
  :alt: Use the Download icon to download an attached file to your local system.

With file attachments, you can share additional information that helps your team to visually understand your ideas. Sharing videos, voice recordings, screenshots, and photos can make your messages more effective and clear.

You can share files with other Mattermost users or entire channels by:

- dragging and dropping files into Channels.
- selecting the **Attachment** |attachment-icon| icon in the message input box.
- pasting from the clipboard.

Attachment limits and sizes
---------------------------

Up to 10 files can be attached per post. The default maximum file size is 100 MB, but this can be changed by the System Admin. See our `Configuration Settings </configure/configuration-settings.html#maximum-file-size>`__ product documentation for details.

Image files can be a maximum size of 7680 pixels x 4320 pixels, with a maximum image resolution of 33 MP (mega pixels) or 8K resolution, and a maximum raw image file size of approximately 253 MB. System Admins can customize the maximum image resolution size within the ``config.json`` file. See our `Configuration Settings </configure/configuration-settings.html#maximum-image-resolution>`__ product documentation for details.

Preview file attachments
------------------------

Mattermost has a built-in file previewer that you can use to:

-  Download files
-  Share public links
-  View media

Select the thumbnail of an attached file to open it in the file previewer.

View media
^^^^^^^^^^

The following media formats are supported on most browsers:

-  Images: BMP, GIF, JPG, JPEG, PNG, SVG
-  Video: MP4
-  Audio: MP3, M4A
-  Files: PDF, TXT

Other document previews (such as Word, Excel, or PPT) are not yet supported.

Share public links
------------------

Public links allow you to share message attachments with anyone outside your Mattermost workspace. To share an attachment, select the thumbnail of an attachment, then select **Get Public Link**.

.. tip::
  
  If **Get Public Link** is not visible in the file previewer, ask your System Admin to enable the feature from the System Console under **Site Configuration > Public Links**.

Download files
--------------

You can download an attached file by selecting the **Download** |download-icon| icon next to the file thumbnail.