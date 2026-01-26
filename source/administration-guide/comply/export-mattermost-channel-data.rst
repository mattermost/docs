Export channel data
===================

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

Ensure important data isn't trapped in silos by migrating data between systems or backing data up for operational continuity. Once exported, channel data can be analyzed using various tools for insights into team dynamics, productivity, and communication patterns, and to fulfill reporting and auditability requirements.

Enable
------

.. note::

  For Mattermost Cloud deployments, no setup is required. See the `usage <#usage>`__ section below for details on exporting channel data.

For self-hosted deployments, a Mattermost system admin must install the Channel Export integration from the in-product App Marketplace:

1. In Mattermost, from the Product menu |product-list|, select **App Marketplace**.
2. Search for or scroll to **Channel Export**, and select **Install**.
3. Once installed, select **Configure**. You're taken to the System Console.
4. On the **Channel Export** configuration page, enable and configure the plugin, and then select **Save**. You can restrict the ability to export channels to system, team, and channel admins only, and you can configure a maximum file size for channel export files.

Upgrade
-------

We recommend upgrading this feature as new versions are released. Generally, updates are seamless and don't interrupt the user experience in Mattermost. Visit the `Releases page <https://github.com/mattermost/mattermost-plugin-channel-export/releases>`__ for the latest release, available releases, and compatibiilty considerations.

Usage
------

You need to be a Mattermost system admin to export channel data.

Use the ``/export`` slash command in a channel to export the current channel's message data into a CSV-formatted file.

Get help
--------

Mattermost customers can open a `Mattermost support case <https://support.mattermost.com/hc/en-us/requests/new>`_. To report a bug, please open a GitHub issue against the `Mattermost Channel Export plugin GitHub repository <https://github.com/mattermost/mattermost-plugin-channel-export>`_.

For questions, feedback, and assistance, join our pubic `Integrations and Apps channel <https://community.mattermost.com/core/channels/integrations>`_ on the `Mattermost Community Server <https://community.mattermost.com/>`_ for assistance.

Customize this integration
--------------------------

This plugin contains both a server and web app portion. See the `Channel Export plugin README documentation <https://github.com/mattermost/mattermost-plugin-channel-export?tab=readme-ov-file#development>`_ on GitHub for details. Visit the `Mattermost Developer Workflow <https://developers.mattermost.com/extend/plugins/developer-workflow/>`_ and `Mattermost Developer environment setup <https://developers.mattermost.com/extend/plugins/developer-setup/>`_ for information about developing, customizing, and extending Mattermost functionality.
