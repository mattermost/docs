Retrospectives
==============

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

Retrospectives help teams identify areas of improvement in workflows. Each time a playbook is run you can create and publish a retrospective for the team and stakeholders to review. Retrospective components are customized per playbook.

Configuring retrospectives before a run
----------------------------------

Open Playbooks and select the **Playbooks** tab. Select the playbook and then select **Edit**. Select **Templates** and scroll down to the **Retrospective Reminder Interval** and **Retrospective Template** fields.

You can set a reminder to fill out the retrospective, which is broadcast to the channel. The template is then pre-populated in the report. Once the report is written, it's saved and is listed in the run's detailed view.

During a run, posts made in the run channel are automatically added to the retrospective timeline and can be filtered based on all events, specific actions (such as role changes, status updates, task assignments), or activities (such as using a slash command).

.. image:: ../images/Retro.gif
   :alt: Create and publish retrospective reports.

Channel export
~~~~~~~~~~~~~~

Exporting the contents of a channel requires the channel export plugin. See the `Channel Export plugin documentation <https://mattermost.gitbook.io/channel-export-plugin>`_ for more information.
