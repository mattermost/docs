MM Blocks
==========

.. include:: ../_static/badges/all-commercial.rst
  :start-after: :nosearch:

**Technical complexity:** :ref:`Low-code <low-code>`

MM Blocks are Mattermost's structured format for rich, interactive integration posts. Integrations can extend messages with text, images, buttons, menus, collapsible sections, and different layout options.

MM Blocks are the recommended way to create interactive messages for integrations such as :doc:`incoming webhooks </integrations-guide/incoming-webhooks>`, plugins, and bot accounts. Legacy `message attachments <https://developers.mattermost.com/integrate/reference/message-attachments/>`_ continue to work; clients translate them into the MM Blocks format at render time.

For payload structure, block types, action handling, and migration guidance, see the `MM Blocks reference <https://developers.mattermost.com/integrate/reference/mm-blocks/>`_ in the developer documentation.

If content does not render or respond as expected, see :doc:`Troubleshoot MM Blocks </get-help/mm-blocks-troubleshooting>`.
