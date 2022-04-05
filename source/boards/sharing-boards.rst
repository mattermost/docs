Sharing boards
==============

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

To share a board with others:

1. Go to **System Console > Mattermost Boards**.
2. Set **Enable Publicly-Shared Boards** to **true**.
3. Open a board in any view.
4. Select **Share board** in the top-right corner of the board.
5. The following two options are available:

   * On the **Share** tab, you can share an editable view link with users who have permissions to the board.
   * On the **Publish** tab, you can share a read-only link online with everyone.

6. Copy the link provided.

Anyone with the link will be able to view the board.

Select **Regenerate Token** if you want to invalidate all the previously shared links. Confirm the action to regenerate the token.

Import and export a board
-------------------------

If you'd like to re-use a board, you can export it as an archive file, and then import the archive file in the channel of your choosing. Exported and imported board archives include card image attachments.

To do this, select the **...** in the toolbar at the top of the board. Then select **Export board archive**. Download the archive file. Navigate to the channel where you'd like to add the exported board. Select the Gear icon next to your profile avatar, then choose **Import archive**. The board you created will be added to this channel.

From v6.4, the archive format is changing with a new ``.boardarchive`` extension and all new exports will only be in this format. 

.. note::

  The previous ``.focalboard`` format will be deprecated in a future release, but will support importing until then. Currently, the import dialog looks for ``.boardarchive``. Use **Select all files** to select ``.focalboard`` files to import.
