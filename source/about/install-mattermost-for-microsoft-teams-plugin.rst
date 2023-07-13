Install the Mattermost for Microsoft Teams plugin
=================================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

To install the `Mattermost for Microsoft Teams </plugins/mattermost-for-microsoft-teams>`__ plugin in Mattermost:

1. Log in to your Mattermost workspace as a system administrator.
2. Download the `latest plugin binary release <https://github.com/mattermost/mattermost-plugin-msteams-sync/releases>`__, compatible with Mattermost v8.0.1 and later. 

  .. tip::

    If you are using an earlier version of Mattermost, `follow our documentation </upgrade/upgrading-mattermost-server.html>`__ to upgrade to Mattermost v8.0.1 or later.

4. Go to **System Console > Plugins > Plugin Management > Upload Plugin**, and upload the plugin binary you downloaded in the previous step.
5. Go to **System Console > Plugins > Plugin Management > Installed Plugins**, search for ``MS Teams Sync``, and select **Enable Plugin**.

Configure the plugin
--------------------

Additional configuration settings are available for this plugin. See the `plugin configuration settings </configure/plugins-coinfiguration-settings>`__ documentation for details.