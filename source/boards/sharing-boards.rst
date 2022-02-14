Sharing Boards
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

1. Open a board in any view.
2. On the top-right of the board select the options menu **...**, then select **Share board**.
3. Set the toggle on to **Publish to web and share this board with anyone**.
4. Copy the link provided.

Anyone with the link will be able to view the board.

Select **Regenerate Token** if you want to invalidate all the previously shared links. Confirm the action to regenerate the token.

Import and export a board
-------------------------

You can share a board with other channels or teams by exporting it, sending the archived file, and having them import it. The exported and imported board archives include card image attachments.

From v6.4, the archive format is changing with a new .boardarchive extension and all new exports will only be in this format. 

Please note: The previous ``.focalboard`` format will be deprecated in a future release, but will support importing until then. Currently, the import dialog looks for ``.boardarchive``. Use **Select all files** to select ``.focalboard`` files to import.
