Install the Mattermost for Microsoft Teams plugin
=================================================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

To install the `Mattermost for Microsoft Teams </plugins/mattermost-for-microsoft-teams>`__ plugin in Mattermost:

1. Log in to your Mattermost workspace as a system administrator.
2. Download the `latest plugin binary release <https://github.com/mattermost/mattermost-plugin-msteams-sync/releases>`__, compatible with Mattermost v8.0.1 and later. 

  .. tip::

    If you are using an earlier version of Mattermost, `follow our documentation </upgrade/upgrading-mattermost-server.html>`__ to upgrade to Mattermost v8.0.1 or later.

3. Go to **System Console > Plugins > Plugin Management > Upload Plugin**, and upload the plugin binary you downloaded in the previous step.
4. Go to **System Console > Plugins > Plugin Management**. In the **Installed Plugins** section, scroll to **MS Teams Sync**, and select **Enable Plugin**.

Configure how users will connect accounts
------------------------------------------

Mattermost admins can configure Mattermost to automatically prompt users to connect their Mattermost user account to their Microsoft Teams user account on login.

1. Go to **System Console > Plugins > MS Teams Sync**.
2. Enable **Enforce connected accounts** to prompt users to connect if they haven't done so.
3. (Optional) Enable **Allow to temporarily skip connect user** to allow users to skip the connection prompt temporarily. Users are prompted on refresh and login.

Configure the plugin
--------------------

Additional configuration settings are available for this plugin. See the `MS Teams Sync plugin configuration settings </configure/plugins-configuration-settings.html#ms-teams-sync>`__ documentation for details.

Get started with the plugin
---------------------------

See our `collaborate using Mattermost for MS Teams </channels/collaborate-using-mattermost-for-microsoft-teams>`__ documentation for details on how to collaborate across both Mattermost and Microsoft Teams at the same time.

Troubleshooting
---------------

If you encounter issues when connecting user accounts or linking channels, we recommend restarting the plugin as a Mattermost system admin. 

1. Go to **System Console > Plugins > Plugin Management**.
2. Under **Installed Plugins**, scroll to the **MSTeams Sync** section, select **Disable** then wait for the State to change to **Not running**.
3. Select **Enable** and wait for the State to change to **Running**.

Get help
---------

If you face any issues while installing the Mattermost for Microsoft Teams sync plugin, you can either:

- Open a new issue in the `Mattermost for Microsoft Teams GitHub repository <https://github.com/mattermost/mattermost-plugin-msteams-sync/issues/new>`__. 
- Or, create a new topic in our `peer-to-peer troubleshooting forum <https://forum.mattermost.com/c/trouble-shoot/16>`__.