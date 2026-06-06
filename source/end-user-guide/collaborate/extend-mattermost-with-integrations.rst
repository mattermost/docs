Extend Mattermost with integrations
===================================

Ensure your teams are are always informed about important events, status changes, deadlines, or priorities with Mattermost operational and DevOps integrations. Enhance communication, streamline Mattermost with external workflows, ensure security and compliance, and foster a more efficient and collaborative work environment with major communication tools and services featuring real-time alerts, updates, and notifications directly within channels. 

Interoperability with pre-built integrations
----------------------------------------------

Your system admin can install the following pre-packaged integrations through the Mattermost Marketplace, and enable and configure them in the Mattermost System Console.

Mattermost features
~~~~~~~~~~~~~~~~~~~~

- :ref:`AI Agents <end-user-guide/agents:access ai features>`
- :ref:`Export Mattermost channel data <administration-guide/comply/export-mattermost-channel-data:usage>`
- :ref:`Monitor performance metrics <administration-guide/scale/collect-performance-metrics:usage>`
- :doc:`Perform legal holds </administration-guide/comply/legal-hold>`

Mattermost interoperability
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- :ref:`GitHub <integrations-guide/github:use>`
- :ref:`GitLab <integrations-guide/gitlab:use>`
- :ref:`Jira <integrations-guide/jira:use>`
- :ref:`Microsoft Teams <integrations-guide/microsoft-teams-sync:use>`
- :ref:`ServiceNow <integrations-guide/servicenow:use>`
- :ref:`Zoom <integrations-guide/zoom:use>`

Interact with integration messages
----------------------------------

Many integrations post rich, actionable content into channels using **MM Blocks**—a structured layout format for text, images, buttons, menus, and grouped content. You may also see the same presentation for older integrations that use message attachments; Mattermost translates those into the MM Blocks layout automatically.

What you may see in a channel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Integration posts can include:

- **Text and images** formatted with headings, emphasis, and links.
- **Grouped content** in bordered or shaded containers, sometimes arranged in columns.
- **Buttons** labeled with actions such as *Acknowledge*, *Approve*, or *View details*.
- **Menus** (static selects) that let you choose from a list of options.
- **Collapsible sections** with a header you can tap to show or hide additional details.

Using buttons and menus
~~~~~~~~~~~~~~~~~~~~~~~

1. **Buttons:** Select a button to send your choice to the integration. The integration may update the post in place or send you a private follow-up message visible only to you.
2. **Menus:** Select the menu to open the list of options, then choose one. Mattermost sends the selected value to the integration, similar to pressing a button.
3. **Disabled controls:** Some buttons or menus appear grayed out and cannot be selected until the integration enables them.

If nothing happens after you select a button or menu option, wait a moment in case the integration is still processing. Contact your system admin if actions consistently fail.

Expandable and scrollable content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some integration posts clip long content to keep the channel readable.

- **Collapsible sections:** Select the section header to expand or collapse the content beneath it.
- **Web and desktop:** When a content region has a height limit, scroll inside the post to read the full content.
- **Mobile:** When content is clipped, a fade appears at the bottom of the region and an expand control is shown in the bottom-right corner. Select that control to open a full-screen **Scrollable content** view. Scroll through the complete content, then use the back gesture or navigation control to return to the channel.

.. tip::

   Integration developers can learn how to build MM Blocks payloads in the :doc:`MM Blocks </integrations-guide/mm-blocks>` documentation. If content does not render or respond as expected, see :doc:`Troubleshoot MM Blocks </get-help/mm-blocks-troubleshooting>`.

.. tip::

   - `Visit the Mattermost Marketplace <https://mattermost.com/marketplace/>`__ to find open source, community-supported integrations to common developer tools like `CircleCI <https://mattermost.com/marketplace/circleci/>`__, `Opsgenie <https://mattermost.com/marketplace/opsgenie/>`__, `PagerDuty Notifier <https://mattermost.com/marketplace/pagerduty/>`__; productivity tools like `Autolink <https://mattermost.com/marketplace/autolink-plugin/>`__, `ToDo <https://mattermost.com/marketplace/todo/>`__, and `WelcomeBot <https://mattermost.com/marketplace/welcomebot-plugin/>`__; as well as social tools like `Memes <https://mattermost.com/marketplace/memes-plugin/>`__ and `GIFs <https://mattermost.com/marketplace/giphy-plugin/>`__ that are freely available for use and customization.
   - Looking for a way to get notifications of new Mattermost Marketplace integrations in your Mattermost channels? See the :doc:`integrations FAQ </integrations-guide/faq>` documentation for details.
