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

Additional configuration settings are available for this plugin. See the `MS Teams Sync plugin configuration settings </configure/plugins-configuration-settings.html#ms-teams-sync>`__ documentation for details.

Demonstration
--------------

Check out this `YouTube demo <https://youtu.be/Mg-stF7_Bjk>`__, from Doug Lauder, Senior Software Design Engineer at Mattermost, to learn how to embed Mattermost in Microsoft Teams:

.. raw:: html
  
   <iframe width="560" height="315" src="https://www.youtube.com/embed/Mg-stF7_Bjk" alt="Install Matterrmost for Microsoft Teams plugin" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

