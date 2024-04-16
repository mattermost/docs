Integrate Zoom into Mattermost
==============================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Reduce friction and time lost to coordinating meetings and switching between apps by integrating Zoom with Mattermost. Make it easy for your teams to start both spontaneous and scheduled video calls directly from Mattermost channels.

Setup
------

The following integration configuration steps are required.



Register an OAuth app in GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every Mattermost user who wants GitHub interoperabilty must perform the following steps while logged in to GitHub.

Create a webhook in GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~

A Mattermost system admin must perform the following steps in Mattermost. Create a Mattermost webhook for each GitHub organization you want to set up.

Configure the GitHub account in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Mattermost system admin must perform the following steps in Mattermost.

Enable
------

Once all setup and configuration is complete, go to **System Console > Plugins > GitHub** to enable GitHub interoperability.

Notify your team so they can connect their GitHub account to Mattermost and get started.

Upgrade
--------

We recommend updating this functionality when new versions are released. Generally, updates are seamless and don't interrupt the user experience in Mattermost.

Usage
-----

In Mattermost, run the ``/github connect`` slash command in any Mattermost channel to link your Mattermost account with your GitHub account. 

Frequently asked questions
---------------------------

Get help
--------

Mattermost customers can open a `Mattermost support case <https://mattermost.zendesk.com/hc/en-us/requests/new>`_. To report a bug, please open a GitHub issue against the `Mattermost GitHub repository <https://github.com/mattermost/mattermost-plugin-github>`_.

For questions, feedback, and assistance, join our pubic `Integrations and Apps channel <https://community.mattermost.com/core/channels/integrations>`_ on the `Mattermost Community Server <https://community.mattermost.com/>`_ for assistance, or join us on the  `Mattermost Discussion Forum <https://forum.mattermost.org/c/plugins>`_.

Customize this plugin
---------------------

This plugin contains both a server and web app portion. See the `Channel Export plugin README documentation <https://github.com/mattermost/mattermost-plugin-channel-export?tab=readme-ov-file#development>`_ on GitHub for details. Visit the `Mattermost Developer Workflow <https://developers.mattermost.com/extend/plugins/developer-workflow/>`__ and `Mattermost Developer environment setup <https://developers.mattermost.com/extend/plugins/developer-setup/>`_ for information about developing, customizing, and extending Mattermost functionality.

In order to get your environment set up to run Playwright tests, please see the setup guide at `e2e/playwright <https://github.com/mattermost/mattermost-plugin-github/blob/master/e2e/playwright#readme>`_.