Getting Started 
===============

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Mattermost Playbooks is included in the Mattermost Cloud workspace, enabled by default, and upgraded automatically.

*For self-hosted deployments*

Mattermost Playbooks is available in the Plugin Marketplace:

1. As a System Admin, go to **Main Menu > Plugin Marketplace**.
2. Search for **Playbooks**.
3. Select **Install** if not yet installed, then select **Configure** to enable.
4. From the plugin configuration page, set **Enable Plugin** to **true**.
5. Select **Save** to enable the plugin.

Accessing and Navigating Playbooks
----------------------------------

* From the Main Menu, select **Playbooks** to view runs, configure playbooks, and modify settings. System Admins have unrestricted access.
* From the channel header, select the **Playbook** icon in the channel header to open the right-hand sidebar. From there, you can start a new playbook run using a playbook or a playbook template.

Finding playbook runs
~~~~~~~~~~~~~~~~~~~~~

When you're in a channel with an active run, select the **Playbook** icon in the channel header to open the right-hand sidebar to view the run details. Information such as run name and description can be edited in-line, and the checklists can be collapsed and filtered based on their status.

To find all playbook runs, select **Main Menu > Playbooks**. Select a run to view its overview. Select **Go to channel** to open the run's channel.

Viewing playbooks 
~~~~~~~~~~~~~~~~~

Playbooks are accessed via **Main Menu > Playbooks** in Mattermost, where you can also view a list of templates.

When you're in a channel that's not running a playbook, select the **Playbook** icon in the channel header to open the right-hand sidebar and view the list of playbooks and templates available for your team.

API Documentation
~~~~~~~~~~~~~~~~~~

To interact with the data model programmatically, consult the `REST API specification <https://github.com/mattermost/mattermost-plugin-incident-collaboration/blob/master/server/api/api.yaml>`_.
