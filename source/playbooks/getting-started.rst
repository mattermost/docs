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
  
Mattermost Playbooks is included in Mattermost self-hosted and Mattermost Cloud workspace. You can access Playbooks via the Product menu in the top-left corner of Mattermost.

Access playbooks and runs
-------------------------

You can access Playbooks within Channels using the **Toggle Playbook List** icon in the channel header to open the right-hand sidebar (RHS). In the RHS, you'll find playbooks you can run as well as templates.

* Playbooks are preconfigured workflows, applied to a specific situation or event, that are refined over time with steps and processes that your team agree on.
* Playbook Templates are basic workflows that you can use to get started quickly. As you learn more about your workflows, you can customize them into specific playbooks.

To open a playbook and view its statistics, select the playbook name. To begin a run using a specific playbook, select **Run** next to that playbook's name.

To access runs, select the Product menu in the top-left corner of Mattermost, then select **Playbooks**. In the runs list, you can select a run to view more details, such as the overview and retrospective. This is an easy way to assess all the active instead of joining each run's channel to keep up.

View run details
~~~~~~~~~~~~~~~~

When you're in a channel with an active run, select the **Toggle Run Details** icon in the channel header to open the RHS to view the run details. Information such as run name and description can be edited in-line, and the checklists can be collapsed and filtered based on their status.

To find all playbook runs, select any playbook name. Then, select **Runs** from the navigation bar. Select a run to view its overview. Select **Go to channel** to open the run's channel.

API Documentation
~~~~~~~~~~~~~~~~~~

To interact with the data model programmatically, consult the `REST API specification <https://github.com/mattermost/mattermost-plugin-incident-collaboration/blob/master/server/api/api.yaml>`_.
