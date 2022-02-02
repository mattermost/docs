Hide emojis from the Emoji Picker
=================================

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Emojis are small, digital images or icons used to communicate or express concepts such as emotions and physical gestures in messages. In addition to the default set of emojis that ship with Mattermost, users can supplement Mattermost standard emojis with by `uploading custom emojis <https://docs.mattermost.com/messaging/using-emoji.html#creating-custom-emojis>`__. 

To hide a standard emoji in Mattermost, a System Admin must identify each emoji offending by name, and then rebuild their self-hosted instance of the Mattermost webapp to hide the emojis.

.. note:: 

    - The ability to remove default emojis from Cloud deployments is not supported.
    - Removing a standard emoji from the Mattermost web app also removes it from all Mattermost clients, including the Desktop App and mobile apps. However, a hidden emoji doesn't stop users from using unicode characters to apply a hidden emoji visible to other Mattermost users.
    - Customers who upgrade Mattermost `using the standard upgrade process <https://docs.mattermost.com/guides/deployment.html#upgrade-mattermost>`__ will see the offending emoji return following the upgrade. This is because the standard upgrade process retains only plugin data in ``mattermost/client/plugins``, and doesn't retain emoji data.

To remove a standard emoji from the Mattermost Emoji Picker:

1. Clone the `mattermost-webapp <https://github.com/mattermost/mattermost-webapp>`__ repository by running: ``git clone --depth=1 https://github.com/mattermost/mattermost-webapp``
2. In Mattermost Channels, identify the names of the emojis to remove by hovering over over an emoji in the Emoji Picker, and noting its name in the format ``:name:``. For example: ``:smile:``.
3. Create a ``TXT`` file, such as ``excludedemojis.txt`` that contains a list of the emojis to remove. Add each emoji name as a separate line.
4. Navigate to the ``mattermost-webapp`` directory from step 1 by running: ``cd mattermost-webapp``.
5. Install ``nvm`` by following `these instructions <https://github.com/nvm-sh/nvm#installing-and-updating>`__.
6. Install the correct node version for the webapp by running ``nvm i``.
7. Download the node packages in the webapp by running ``npm i``.
8. Use ``npm`` to invoke the script ``emoji_gen.mjs``. For example: ``npm run make-emojis -- --excluded-emoji-file .path-to-file/excludedemojis.txt``
9. Build and package the modified mattermost-webapp by running ``make package``.
10. Remove the existing client directory within the Mattermost install directory by running ``rm -r /opt/mattermost/client``.
11. Extract the generated tar into the Mattermost install directory by running ``tar -xvf mattermost-webapp.tar.gz /opt/mattermost``.
12. Ensure the files are owned by the Mattermost service account by running ``sudo chown mattermost:mattermost /opt/mattermost``.
13. Restart Mattermost. The offending emoji are hidden from the Mattermost Emoji Picker.