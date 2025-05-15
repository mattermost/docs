Pre-built integrations
=======================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. toctree::
  :maxdepth: 1
  :hidden:
  :titlesonly:

    GitHub </integrate/github>
    GitLab </integrate/gitlab>
    Jira </integrate/jira>
    ServiceNow </integrate/servicenow>
    Zoom </integrate/zoom>

Accelerate operational and technical workflows by connecting Mattermost operational and DevOps integrations to your mission-critical tools.

Your Mattermost deployment comes with the following integrations pre-packaged you can configure and use:

* :doc:`GitHub </integrate/github>` - Connect GitHub to Mattermost to subscribe to repositiories, and to stay current with reviews, assignments, and more.
* :doc:`GitLab </integrate/gitlab>` - Connect GitLab to Mattermost to subscribe to repositories, use GitLab events as Mattermost action triggers, and more.
* :doc:`Jira </integrate/jira>` - Connect Jira to Mattermost to create Jira tickets from messages in Mattermost, and to get Mattermost notifications for Jira updates.
* :doc:`ServiceNow </integrate/servicenow>` - Connect ServiceNow to Mattermost to subscribe to record changes in ServiceNow and manage them in Mattermost.
* `Splunk <https://github.com/mattermost-community/mattermost-plugin-splunk#readme>`_ - Connect Splunk to Mattermost to receive alerts and notifications from Splunk in Mattermost.
* :doc:`Zoom </integrate/zoom>` - Connect Zoom to Mattermost to start audio and video conferencing calls in Mattermost with a single click.

Mattermost Marketplace integrations
-----------------------------------

.. include:: ../_static/badges/selfhosted-only.rst
  :start-after: :nosearch:

Additional integrations are available on the `Mattermost Marketplace <https://mattermost.com/marketplace/>`_. You can install these integrations directly from the Marketplace, by uploading them in the System Console, or by using the REST API.

.. important::

  Installed plugins are persisted to the configured file store and unpacked on server startup. It's imperative that your file store be accessible to the server immediately on startup. If using a shared filesystem, ensure the mount completes successfully before starting the server. We also strongly recommend testing integration updates in a staging environment before deploying to production, and regularly backing up integrations.