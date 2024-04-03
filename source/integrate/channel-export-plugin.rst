Channel Export plugin
=====================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

The Mattermost Channel Export plugin enables system administrators to archive, back up, or submit the contents of a channel into other systems to fulfill reporting and auditability requirements as needed.

Enable
------

Mattermost Cloud deployments enable the Channel Export plugin by default. For self-hosted deployments, a system admin must enable the Channel Export plugin in the System Console.

1. Go to **System Console > Plugins > Plugin Management**.
2. Under **Installed Plugins**, scroll to the Channel Export plugin, and select **Enable**.

Once the plugin is enabled, the Channel Export plugin has its own page of configuration settings in the System Console under **Plugins**.

Configure
---------

Go to **System Console > Plugins > Plugin Management > Channel Export** to manage configuration settings for this plugin. 

.. tip::

    You can also reach the plugin's configuration page from **System Console > Plugins > Plugin Management** by selecting **Settings**.

Outstanding Engineering question: Does the experimental `Export output directory <https://docs.mattermost.com/configure/experimental-configuration-settings.html#export-output-directory>`__ and `Export retention days <https://docs.mattermost.com/configure/experimental-configuration-settings.html#export-retention-days>`__ config settings apply to this plugin?

Upgrade
--------

When a new version of the plugin is released, Mattermost prompts you to update your current version of the plugin to the newest one. There may be a warning shown if there is a major version change that may affect the installation. Generally, updates are seamless and don't interrupt the user experience in Mattermost.

^ is this true for the Channel Export plugin?

Usage
------

Use the ``/export`` slash command in a channel to export the current channel's message data into a CSV-formatted file.

Engineering questions: who can run this slash command -- admins only? what data is/isn't included? Is the admin prompted to download the CSV file?

Frequently asked questions
---------------------------

TBD

Get help
--------

For Mattermost customers: Please open a `Mattermost support case <https://mattermost.zendesk.com/hc/en-us/requests/new>`__ to ensure your issue is tracked properly.

For questions, feedback, and assistance: Please join us on the `Mattermost Discussion Forum <https://forum.mattermost.org/c/plugins>`__. 

Alternatively, join our pubic `Mattermost Community Server <https://community.mattermost.com/>`__ and the `Integrations and Apps channel <https://community.mattermost.com/core/channels/integrations>`__ for assistance.

To report a bug, please open a GitHub issue against the `Mattermost Channel Export plugin GitHub repository <https://github.com/mattermost/mattermost-plugin-channel-export>`__.

Customize this plugin
---------------------

This plugin contains both a server and web app portion. See the `Channel Export plugin README documentation <https://github.com/mattermost/mattermost-plugin-channel-export?tab=readme-ov-file#development>`__ on GitHub for details on developing and deploying this plugin.

Read our documentation about the `Mattermost Developer Workflow <https://developers.mattermost.com/extend/plugins/developer-workflow/>`__ and `Mattermost Developer environment setup <https://developers.mattermost.com/extend/plugins/developer-setup/>`__ for information about developing, customizing, and extending Mattermost plugins.


