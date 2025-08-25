Pre-built integrations
=======================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. toctree::
  :maxdepth: 1
  :hidden:
  :titlesonly:

    GitHub </integrations-guide/github>
    GitLab </integrations-guide/gitlab>
    Jira </integrations-guide/jira>
    ServiceNow </integrations-guide/servicenow>
    Zoom </integrations-guide/zoom>
    Mattermost Agents </administration-guide/configure/agents-admin-guide>
    Mattermost Boards </end-user-guide/project-task-management>
    Mattermost Calls </administration-guide/configure/calls-deployment>
    Mattermost Channel Export </administration-guide/comply/export-mattermost-channel-data>
    Mattermost Metrics </administration-guide/scale/collect-performance-metrics>
    Mattermost Playbooks </end-user-guide/workflow-automation>
    Mattermost User Survey </administration-guide/configure/manage-user-surveys>
    Mattermost for M365, Teams, and Outlook </integrations-guide/mattermost-mission-collaboration-for-m365>
    Microsoft Calendar </integrations-guide/microsoft-calendar>
    Microsoft Teams Sync </integrations-guide/microsoft-teams-sync>
    Microsoft Teams Meetings </integrations-guide/microsoft-teams-meetings>

Accelerate operational and technical workflows by connecting Mattermost with your mission-critical tools.

How Pre-Built Integrations Work
--------------------------------

Mattermost offers 2 types of pre-built integrations:

|checkmark| **Pre-packaged**: Already bundled with your Mattermost server. Configure and enable in the System Console.

|download-icon| **Marketplace**: Available from the `Mattermost Marketplace <https://mattermost.com/marketplace/>`_.

Pre-Packaged Integrations
~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| Integration                                                                                    | **Type**         | **What it does**                                            |
+================================================================================================+==================+=============================================================+
| :doc:`GitHub </integrations-guide/github>`                                                     | |checkmark|      | Subscribe to repos, stay updated on reviews & assignments   |
+------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| :doc:`GitLab </integrations-guide/gitlab>`                                                     | |checkmark|      | Use repo events as triggers, get updates in Mattermost      |
+------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| :doc:`Jira </integrations-guide/jira>`                                                         | |checkmark|      | Create Jira tickets from messages, receive notifications    |
+------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| :doc:`Mattermost Agents </administration-guide/configure/agents-admin-guide>`                  | |checkmark|      | Deploy and manage AI agents for workflow automation         |
+------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| :doc:`Mattermost Boards </end-user-guide/project-task-management>`                             | |checkmark|      | Manage project tasks and workflows                          |
+------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| :doc:`Mattermost Calls </administration-guide/configure/calls-deployment>`                     | |checkmark|      | Start voice/video calls with screen sharing                 |
+------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| :doc:`Mattermost Channel Export </administration-guide/comply/export-mattermost-channel-data>` | |checkmark|      | Export channel history and data for compliance              |
+------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| :doc:`Mattermost Metrics </administration-guide/scale/collect-performance-metrics>`            | |checkmark|      | Collect and analyze performance metrics                     |
+------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| :doc:`Mattermost Playbooks </end-user-guide/workflow-automation>`                              | |checkmark|      | Run structured workflows for incidents & projects           |
+------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| :doc:`Mattermost User Survey </administration-guide/configure/manage-user-surveys>`            | |checkmark|      | Collect user feedback and satisfaction data                 |
+------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| `Pexip <https://mattermost.com/marketplace/pexip-video-connect/>`_                             | |download-icon|  | Start video conferencing calls from Mattermost              |
+------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| :doc:`ServiceNow </integrations-guide/servicenow>`                                             | |checkmark|      | Subscribe to record changes, manage them in Mattermost      |
+------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| `Splunk <https://mattermost.com/marketplace/splunk-2/>`_                                       | |download-icon|  | Receive Splunk alerts directly in Mattermost channels       |
+------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| :doc:`Zoom </integrations-guide/zoom>`                                                         | |checkmark|      | Start audio/video conferences in one click                  |
+------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+

Microsoft Integrations
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| **Integration**                                                                                       | **Type**         | **What it does**                                            |
+=======================================================================================================+==================+=============================================================+
| :doc:`Mattermost for M365, Teams, and                                                                 | |download-icon|  | Secure fallback + enhance Teams & Outlook                   |
| Outlook </integrations-guide/mattermost-mission-collaboration-for-m365>`                              |                  |                                                             |
+-------------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| :doc:`Microsoft Teams Sync </integrations-guide/microsoft-teams-sync>`                                | |checkmark|      | Sync users & data between Teams and Mattermost              |
+-------------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| :doc:`Microsoft Teams Meetings </integrations-guide/microsoft-teams-meetings>`                        | |checkmark|      | Start/join Teams meetings directly from Mattermost          |
+-------------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+
| :doc:`Microsoft Calendar </integrations-guide/microsoft-calendar>`                                    | |checkmark|      | Receive calendar reminders in Mattermost                    |
+-------------------------------------------------------------------------------------------------------+------------------+-------------------------------------------------------------+

More on Mattermost Marketplace
---------------------------------

More Mattermost integrations are available on the `Mattermost Marketplace <https://mattermost.com/marketplace/>`_. You can install these integrations directly from the Marketplace, by uploading them in the System Console, or by using the REST API.

.. important::

  - Installed plugins are persisted to the configured file store and unpacked on server startup. It's imperative that your file store be accessible to the server immediately on startup. If using a shared filesystem, ensure the mount completes successfully before starting the server. 
  - We strongly recommend testing integration updates in a staging environment before deploying to production, and regularly backing up integrations.