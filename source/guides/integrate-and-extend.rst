Integrate and extend Mattermost
================================

.. toctree::
  :maxdepth: 1
  :hidden:
  :titlesonly:

    GitHub interoperability </integrate/github-interoperability>
    GitLab interoperability </integrate/gitlab-interoperability>
    Jira interoperability </integrate/jira-interoperability>
    Community for Mattermost for Microsoft 365 </integrate/community-for-mattermost-for-microsoft-teams>
    Mattermost Playbooks for Microsoft Teams </integrate/playbooks-for-microsoft-teams>
    Microsoft Calendar interoperability </integrate/microsoft-calendar-interoperability>
    Microsoft Teams interoperability </integrate/microsoft-teams-interoperability>
    Microsoft Teams Meetings interoperability </integrate/microsoft-teams-meetings-interoperability>
    ServiceNow interoperability </integrate/servicenow-interoperability>
    Zoom interoperability </integrate/zoom-interoperability>

Accelerate operational and technical workflows by connecting Mattermost operational and DevOps integrations to your mission-critical tools.

Interoperability with pre-packaged integrations
-----------------------------------------------

Your Mattermost deployment comes with the following integrations you can configure and use:

* :doc:`GitHub interoperability </integrate/github-interoperability>` - Connect your GitHub instance to your Mattermost instance to subscribe to repositiories, and to stay current with reviews, assignments, and more.
* :doc:`GitLab interoperability </integrate/gitlab-interoperability>` - Connect your GitLab instance to your Mattermost instance to subscribe to repositories, use GitLab events as Mattermost action triggers, and more.
* :doc:`Jira interoperability </integrate/jira-interoperability>` - Connect your Jira instance to your Mattermost instance to create Jira tickets from messages in Mattermost, and to get notified of important Jira updates in Mattermost.
* :doc:`Community for Mattermost for Microsoft 365 </integrate/community-for-mattermost-for-microsoft-teams>` - Access the Mattermost Community directly from a tab in Microsoft 365 without switching applications or opening a browser.
* :doc:`Mattermost Playbooks for Microsoft Teams </integrate/playbooks-for-microsoft-teams>` - Improve cross-organizational alignment and awareness by enabling access to your active, repeatable processes and status updates in Mattermost directly in Microsoft Teams.
* :doc:`Microsoft Calendar interoperability </integrate/microsoft-calendar-interoperability>` - Connect your Microsoft O365 Calendar to your Mattermost instance to receive daily sumamryies of calendar events, synchronize your Microsoft O365 status in Mattermost, and accept or decline calendar invites without leaving Mattermost.
* :doc:`Microsoft Teams interoperability </integrate/microsoft-teams-interoperability>` - Connect your Microsoft Teams instance to your Mattermost instance to forward real-time chat notifications from Teams to Mattermost.
* :doc:`Microsoft Teams Meetings interoperability </integrate/microsoft-teams-meetings-interoperability>` - Connect your Microsoft Teams Meetings instance to your Mattermost instance to start and join voice calls, video calls, and use screen sharing without leaving Mattermost.
* :doc:`ServiceNow interoperability </integrate/servicenow-interoperability>` - Connect your ServiceNow instance to your Mattermost instance to subscribe to record changes in ServiceNow and manage them in Mattermost.
* :doc:`Zoom interoperability </integrate/zoom-interoperability>` - Connect your Zoom instance to your Mattermost instance to start Zoom audio and video conferencing calls in Mattermost with a single click.

.. tip::

    Visit the `Mattermost Developer Documentation <https://developers.mattermost.com/integrate/getting-started/>`__ for details on developing `webhooks <https://developers.mattermost.com/integrate/webhooks>`__, developing `custom slash commands <https://developers.mattermost.com/integrate/slash-commands/custom/>`_, `custom plugins <https://developers.mattermost.com/integrate/plugins/>`__, building advanced bots and integrations using the `Mattermost REST API <https://api.mattermost.com/>`__, `embedding Mattermost <https://developers.mattermost.com/integrate/customization/embedding/>`__ into web browsers and web apps, `customizing the Mattermost source code <https://developers.mattermost.com/integrate/customization/customization/>`__, and developing `interactive messages <https://developers.mattermost.com/integrate/plugins/interactive-messages/>`__ on the Mattermost platform.

Mattermost Marketplace integrations
-----------------------------------

Additional Mattermost integrations are available on the `Mattermost Marketplace <https://mattermost.com/marketplace/>`_. You can install these integrations directly from the Marketplace, by uploading them in the System Console, or by using the REST API.

.. important::

  Installed plugins are persisted to the configured file store and unpacked on server startup. It's imperative that your file store be accessible to the server immediately on startup. If using a shared filesystem, ensure the mount completes successfully before starting the server. We also strongly recommend testing integration updates in a staging environment before deploying to production, and regularly backing up integrations.
