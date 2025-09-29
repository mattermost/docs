Popular Pre-Built Integrations
===============================

.. toctree::
  :maxdepth: 1
  :hidden:
  :titlesonly:

    Mattermost Channel Export </administration-guide/comply/export-mattermost-channel-data>
    Mattermost Legal Hold </administration-guide/comply/legal-hold>
    Mattermost Metrics </administration-guide/scale/collect-performance-metrics>
    Mattermost User Survey </administration-guide/configure/manage-user-surveys>
    Mattermost Embedded for M365, Teams, and Outlook </integrations-guide/mattermost-mission-collaboration-for-m365>
    Microsoft Calendar </integrations-guide/microsoft-calendar>
    Microsoft Teams Meetings </integrations-guide/microsoft-teams-meetings>
    Microsoft Teams Sync </integrations-guide/microsoft-teams-sync>
    GitHub </integrations-guide/github>
    GitLab </integrations-guide/gitlab>
    Jira </integrations-guide/jira>
    ServiceNow </integrations-guide/servicenow>
    Zoom </integrations-guide/zoom>

Accelerate your operational and technical workflows by connecting Mattermost with your mission-critical tools through pre-built integrations.

Mattermost Integrations
------------------------

Designed for teams that need reliability, auditability, and ownership of their collaboration stack, the following Mattermost collaboration integrations keep your data all inside your secure Mattermost ecosystem. Reduce tool sprawl, strengthen security, improve compliance posture, all with a seamless user experience.

+------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| **Mattermost Integration**                                                                     | **How to Get It**                                                 | **What It Does**                                                                                           |
+================================================================================================+===================================================================+============================================================================================================+
| :doc:`Mattermost Channel Export </administration-guide/comply/export-mattermost-channel-data>` | |product-list| > **App Marketplace**                              | Exports channel history and data for compliance purposes.                                                  |
+------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| :doc:`Mattermost Legal Hold </administration-guide/comply/legal-hold>`                         | Manual Upload                                                     | Keeps a copy of messages and files so they cannot be deleted for legal or compliance needs.                |
+------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| :doc:`Mattermost Metrics </administration-guide/scale/collect-performance-metrics>`            | |product-list| > **App Marketplace**                              | Shows numbers about system performance when people use Mattermost.                                         |
+------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| :doc:`Mattermost User Survey </administration-guide/configure/manage-user-surveys>`            | |product-list| > **App Marketplace**                              | Collects feedback by asking questions directly in Mattermost channels.                                     |
+------------------------------------------------------------------------------------------------+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

Microsoft Integrations
------------------------

If your organization relies on Microsoft tools, Mattermost offers deep integrations with M365, Teams, Outlook, and Calendar to keep collaboration seamless and secure. These integrations allow you to enhance and extend Microsoft tools while maintaining Mattermost as your central hub. By connecting Mattermost with Microsoft apps, you reduce context switching, strengthen reliability through secure fallback options, and ensure your workflows stay efficient across both platforms.

+----------------------------------------------------------------------------------+--------------------------------------+-----------------------------------------------------------------------------------------------+
| **Microsoft Integration**                                                        | **Where to Get It**                  | **What It Does**                                                                              |
+==================================================================================+======================================+===============================================================================================+
| :doc:`Mattermost Embedded for M365, Teams, and                                   | Manual Upload                        | Embed Mattermost in Microsoft apps.                                                           |
| Outlook </integrations-guide/mattermost-mission-collaboration-for-m365>`         |                                      | Use Outlook and Teams together with Mattermost for secure backup and extra features.          |
+----------------------------------------------------------------------------------+--------------------------------------+-----------------------------------------------------------------------------------------------+
| :doc:`Microsoft Calendar </integrations-guide/microsoft-calendar>`               | |product-list| > **App Marketplace** | Sends your Microsoft Calendar reminders into Mattermost so you don’t miss events.             |
+----------------------------------------------------------------------------------+--------------------------------------+-----------------------------------------------------------------------------------------------+
| :doc:`Microsoft Teams Meetings </integrations-guide/microsoft-teams-meetings>`   | |product-list| > **App Marketplace** | Lets you start or join Microsoft Teams meetings directly from Mattermost.                     |
+----------------------------------------------------------------------------------+--------------------------------------+-----------------------------------------------------------------------------------------------+
| :doc:`Microsoft Teams Sync </integrations-guide/microsoft-teams-sync>`           | |product-list| > **App Marketplace** | Copies messages from Microsoft Teams into Mattermost (one-way) to keep conversations in sync. |
+----------------------------------------------------------------------------------+--------------------------------------+-----------------------------------------------------------------------------------------------+

The following integrations bring key external tools (DevOps, ITSM, monitoring, and meetings) into Mattermost, so teams can see updates, take action, and collaborate faster without leaving their secure chat environment.

+-------------------------------------------------------------------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| **Third-Party Integration**                                             | **Where to Get It**                                               | **What It Does**                                                                                                        |
+=========================================================================+===================================================================+=========================================================================================================================+
| :doc:`GitHub </integrations-guide/github>`                              | |product-list| > **App Marketplace**                              | Shows GitHub updates, like new pull requests, commits, or issues, in Mattermost channels.                               |
+-------------------------------------------------------------------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| :doc:`GitLab </integrations-guide/gitlab>`                              | |product-list| > **App Marketplace**                              | Sends GitLab activity (code pushes, merge requests, CI/CD pipeline updates) into Mattermost channels.                   |
+-------------------------------------------------------------------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| :doc:`Jira </integrations-guide/jira>`                                  | |product-list| > **App Marketplace**                              | Lets you see, create, and update Jira issues inside Mattermost.                                                         |
+-------------------------------------------------------------------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| `Pexip <https://mattermost.com/marketplace/pexip-video-connect/>`_      | `Mattermost Marketplace <https://mattermost.com/marketplace/>`_   | Lets you start and join Pexip video meetings from Mattermost.                                                           |
+-------------------------------------------------------------------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| :doc:`ServiceNow </integrations-guide/servicenow>`                      | |product-list| > **App Marketplace**                              | Sends ServiceNow updates (like tickets or incidents) into Mattermost and lets you take action from chat.                |
+-------------------------------------------------------------------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| `Splunk <https://mattermost.com/marketplace/splunk-2/>`_                | `Mattermost Marketplace <https://mattermost.com/marketplace/>`_   | Sends Splunk alerts and search results directly into Mattermost channels.                                               |
+-------------------------------------------------------------------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+
| :doc:`Zoom </integrations-guide/zoom>`                                  | |product-list| > **App Marketplace**                              | Lets you start and join Zoom meetings from inside Mattermost.                                                           |
+-------------------------------------------------------------------------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------+

More on Marketplace
--------------------

More integrations are available on the `Mattermost Marketplace <https://mattermost.com/marketplace/>`_. You can install these integrations directly from the Marketplace, by uploading them in the System Console, or by using the REST API.

.. important::

  - Installed plugins are persisted to the configured file store and unpacked on server startup. It's imperative that your file store be accessible to the server immediately on startup. If using a shared filesystem, ensure the mount completes successfully before starting the server. 
  - We strongly recommend testing integration updates in a staging environment before deploying to production, and regularly backing up integrations.
