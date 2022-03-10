Retrospectives
==============

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Retrospectives help teams identify areas of improvement in workflows. Each time a playbook is run you can create and publish a retrospective for the team and stakeholders to review. Retrospective components are customized per playbook.

Configuring retrospectives before a run
----------------------------------------

Open Playbooks and select the **Playbooks** tab. Select the playbook and then select **Edit**. Select **Retrospective**. Move the toggle to **Enable Retrospective**.

You can set a reminder to fill out the retrospective after a run is finished. The configured template is pre-populated in the run's retrospective.

Use the run timeline to help write an accurate retrospective. Events such as owner changes, status updates, and task assignments appear automatically. Selected posts may also be added to the timeline by using the post context menu.

.. image:: ../images/Retro.gif
   :alt: Create and publish retrospective reports.

Metrics
~~~~~~~

Use metrics to identify key areas where you want to extract valuable insights by measuring performance and improvement. 

These metrics can be anything that's of interest to you and your team. For example, for a software release playbook you might want to have a metric tracking how many bugs were detected during a run. The output of the metrics you've added is provided in the retrospective and, over time, you can use the data to examine anomalies and refine goals.

Another example is a support incident playbook. A metric such as time to resolution can be applied and used to identify areas that need more refinement such as tasks that might work better if they're split up so the goal is reached faster.

Metrics are enabled when you enable retrospectives. Calibrate the type of metric you want to measure, and once a run is finished you can view the output in the retrospective. You can have multiple metrics configured per playbook and you can edit them at any time.

Channel export
~~~~~~~~~~~~~~

Exporting the contents of a channel requires the channel export plugin. See the `Channel Export plugin documentation <https://mattermost.gitbook.io/channel-export-plugin>`_ for more information.
