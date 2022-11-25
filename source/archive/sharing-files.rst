:nosearch:

Sharing Files
===============

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

With file attachments, you can share additional information that will help your team to visually understand your ideas. Sharing videos, voice recordings, screenshots, and photos will make your messages more effective and clear.

Attach Files to Messages
------------------------

You can attach files to messages in the following ways:

-  Use the attachment icon inside the message input box
-  Drag and drop
-  Paste from the clipboard

Preview File Attachments
------------------------

Mattermost has a built-in file previewer that you can use to:

-  Download files
-  Share public links
-  View media

Select the thumbnail of an attached file to open it in the file previewer.

Downloading Files
~~~~~~~~~~~~~~~~~

You can download an attached file by selecting the download icon next to the file thumbnail.

Sharing Public Links
~~~~~~~~~~~~~~~~~~~~

Public URLs allow you to share attachments with anyone outside the Mattermost system. To share an attachment, select the thumbnail of an attachment, then select **Get Public Link**.

.. tip::
  
  If **Get Public Link** is not visible in the file previewer, and you prefer that the feature is enabled, you can request your System Admin to enable the feature from the System Console under **Site Configuration > Public Links**.

Viewing Media
~~~~~~~~~~~~~~

The following media formats are supported on most browsers:

-  Images: BMP, GIF, JPG, JPEG, PNG, SVG
-  Video: MP4
-  Audio: MP3, M4A
-  Files: PDF, TXT

Other document previews (such as Word, Excel, or PPT) are not yet supported.

Attachment Limits and Sizes
---------------------------

Up to 10 files can be attached per post. The default maximum file size is 100 MB, but this can be changed by the System Admin. See our `Configuration Settings </configure/configuration-settings.html#maximum-file-size>`__ product documentation for details.

Image files can be a maximum size of 7680 pixels x 4320 pixels, with a maximum image resolution of 33 MP (mega pixels) or 8K resolution, and a maximum raw image file size of approximately 253 MB. System Admins can customize the maximum image resolution size within the ``config.json`` file. See our `Configuration Settings </configure/configuration-settings.html#maximum-image-resolution>`__ product documentation for details.
