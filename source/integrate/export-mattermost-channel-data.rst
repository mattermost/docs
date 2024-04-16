Export channel data
===================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Ensure important data isn't trapped in silos by migrating data between systems or backing data up for operational continuity. Once exported, channel data can be analyzed using various tools for insights into team dynamics, productivity, and communication patterns. This analysis can inform strategies to improve team collaboration, streamline workflows, and enhance overall efficiency, as well as fulfill reporting and auditability requirements.

Enable
------

You need to be a Mattermost system admin to export channel data.

.. tab:: self-hosted

  Enable channel exports in the System Console.

  1. Go to **System Console > Plugins > Plugin Management**.
  2. Under **Installed Plugins**, scroll to Channel Export, and select **Enable**.

  Once enabled, Channel Export has its own page of configuration settings in the System Console under **Plugins**.

.. tab:: Cloud

  No setup is required. See the `usage <#usage>`__ section below for details on exporting channel data.

Configure
---------

Go to **System Console > Plugins > Plugin Management > Channel Export** to manage configuration settings for this plugin.

.. Outstanding Engineering question: Does the following experimental config settings apply to this plugin?
  - `Export output directory <https://docs.mattermost.com/configure/experimental-configuration-settings.html#export-output-directory>`__  
  - `Export retention days <https://docs.mattermost.com/configure/experimental-configuration-settings.html#export-retention-days>`__ config settings apply to this plugin?

Upgrade
--------

We recommend updating this functionality when new versions are released. Generally, updates are seamless and don't interrupt the user experience in Mattermost.

Usage
------

Use the ``/export`` slash command in a channel to export the current channel's message data into a CSV-formatted file.

.. Engineering questions: who can run this slash command -- admins only? what data is/isn't included? Is the admin prompted to download the CSV file?

Frequently asked questions
---------------------------

TBD

Get help
--------

Mattermost customers can open a `Mattermost support case <https://mattermost.zendesk.com/hc/en-us/requests/new>`_. To report a bug, please open a GitHub issue against the `Mattermost Channel Export plugin GitHub repository <https://github.com/mattermost/mattermost-plugin-channel-export>`_.

For questions, feedback, and assistance, join our pubic `Integrations and Apps channel <https://community.mattermost.com/core/channels/integrations>`_ on the `Mattermost Community Server <https://community.mattermost.com/>`_ for assistance, or join us on the  `Mattermost Discussion Forum <https://forum.mattermost.org/c/plugins>`_.

Customize this plugin
---------------------

This plugin contains both a server and web app portion. See the `Channel Export plugin README documentation <https://github.com/mattermost/mattermost-plugin-channel-export?tab=readme-ov-file#development>`_ on GitHub for details. Visit the `Mattermost Developer Workflow <https://developers.mattermost.com/extend/plugins/developer-workflow/>`_ and `Mattermost Developer environment setup <https://developers.mattermost.com/extend/plugins/developer-setup/>`_ for information about developing, customizing, and extending Mattermost functionality.