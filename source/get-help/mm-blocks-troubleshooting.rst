Troubleshoot MM Blocks
======================

.. include:: ../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Integration posts that use :doc:`MM Blocks </integrations-guide/mm-blocks>` show structured content—text, images, buttons, menus, and layouts—directly in a channel. This page covers common issues when MM Blocks do not render or respond as expected, with emphasis on mobile clients.

MM Blocks content does not appear
---------------------------------

**Symptoms:** A post shows only plain text (or no content) and the expected buttons, images, or layout blocks are missing.

**Try the following:**

1. **Update your client.** MM Blocks require a current Mattermost web, desktop, or mobile app. See :doc:`client availability </end-user-guide/access/client-availability>` for platform support.
2. **Confirm the integration payload.** The post must include a non-empty ``props.mm_blocks`` array (or a legacy format such as message attachments that the client translates). Ask your integration owner or system admin to verify the webhook or bot payload.
3. **Check the feature flag (system admins).** Self-hosted deployments can disable MM Blocks with the ``MmBlocksEnabled`` feature flag. When disabled, native MM Blocks payloads are not rendered and their actions are rejected. See :doc:`MM Blocks </integrations-guide/mm-blocks>` for details.
4. **Reload the channel.** Pull to refresh on mobile, or switch channels and return, to fetch the latest post data.

Buttons or menus do not respond
-------------------------------

**Symptoms:** Buttons appear disabled, or tapping a button or menu option has no effect.

**Try the following:**

1. **Wait for the action to finish.** Some integrations show a loading state while Mattermost calls an external service. Slow integrations may time out based on your server's :ref:`integration request timeout <administration-guide/configure/integrations-configuration-settings:integration request timeout>` setting.
2. **Check whether the control is disabled.** Integrations can send buttons and menus in a disabled state. Disabled controls cannot be activated.
3. **Verify network connectivity.** External actions require Mattermost to reach the integration URL configured by the post author. Connectivity issues on the server or integration host can prevent responses.
4. **Look for follow-up messages.** Successful actions may update the original post or return an ephemeral reply visible only to you. Check the thread panel if the post is part of a thread.

Scrollable content issues on mobile
-----------------------------------

**Symptoms:** Clipped integration content cannot be expanded, or the **Scrollable content** screen is empty.

Some integration posts limit the height of a content region. When content overflows, Mattermost mobile shows a clipped preview with an expand control in the corner of the region.

**To view the full content on mobile:**

1. Locate the clipped region in the post (a fade at the bottom indicates more content below).
2. Select the expand control in the bottom-right corner of the clipped area.
3. Mattermost opens a full-screen **Scrollable content** view where you can scroll through the complete block content.
4. Use the back gesture or navigation control to return to the channel.

**If the Scrollable content screen shows "Cannot display content":**

- Return to the channel and open the expand control again. This screen appears when the expanded payload is no longer available (for example, after navigating away before the view loaded).
- Update to the latest mobile app build if the issue persists across multiple posts.

On web and desktop, the same clipped regions scroll inside the post; a separate full-screen view is not used.

Collapsible sections or images look wrong
-----------------------------------------

**Symptoms:** A section will not expand, an image fails to load, or part of the layout is missing.

**Try the following:**

1. **Collapsible sections:** Select the section header to toggle between expanded and collapsed states. If the header is missing or empty, the integration payload may be incomplete.
2. **Images:** External images require a valid URL and may be blocked by your server's image proxy or SVG settings. Contact your system admin if images from other integrations load but MM Blocks images do not.
3. **Partial content:** Clients skip individual malformed blocks and still render valid ones in the same post. If only some elements are missing, the integration payload likely contains invalid block entries.

Legacy message attachments
--------------------------

Older integrations that use `message attachments <https://developers.mattermost.com/integrate/reference/message-attachments/>`_ are translated into the MM Blocks UI at render time. Button and menu behavior should match native MM Blocks posts. If an attachment-based post behaves differently from a native MM Blocks post, report the payload to your integration owner.

Get more help
-------------

- **End users:** See :doc:`Extend Mattermost with integrations </end-user-guide/collaborate/extend-mattermost-with-integrations>` for how to use buttons, menus, and expandable content in channels.
- **Developers:** See :doc:`MM Blocks </integrations-guide/mm-blocks>` for payload format, action APIs, and migration guidance.
- **Mobile deployment issues:** See :doc:`Mobile deployment troubleshooting </deployment-guide/mobile/mobile-troubleshooting>` for connectivity, push notification, and app install problems unrelated to MM Blocks content.

If you continue to experience issues, visit the `Mattermost Troubleshooting forum <https://forum.mattermost.com/c/trouble-shoot/16>`_ or contact your system administrator.
