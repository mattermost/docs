Getting Started 
===============

Mattermost Incident Collaboration is included in the Mattermost Cloud workspace, enabled by default, and upgraded automatically.

*For self-managed deployments*

Mattermost Incident Collaboration is available in the Plugin Marketplace:

1. As a System Admin, go to **Main Menu > Plugin Marketplace**.
2. Search for **Incident Collaboration**.
3. Select **Install** if not yet installed, then select **Configure** to enable.
4. From the plugin configuration page, set **Enable Plugin** to **true**.
5. Select **Save** to enable the plugin.

To access Mattermost Incident Collaboration:

* From the Main Menu, select **Incident Collaboration** to view stats, review incidents of which you are a member, and configure playbooks. System Admins have unrestricted access.
* From the channel header, select the **Incidents** icon to open the right-hand sidebar. From there, create a new incident or collaborate on active incidents of which you are a member.

Built-in slash commands
-----------------------

The ``/incident`` slash command allows interaction with incidents via the post textbox on desktop, browser, and mobile for:

- ``/incident start`` - Start a new incident.
- ``/incident end`` - End an ongoing incident.
- ``/incident update`` - Update the current incident's status.
- ``/incident restart`` - Restart an ended incident.
- ``/incident check [checklist item]`` - Check/uncheck the specified task.
- ``/incident announce ~[channels]`` - Announce the current incident in other channels.
- ``/incident list`` - List all your incidents.
- ``/incident commander [@username]`` - Show or change the current commander.
- ``/incident info`` - Show a summary of the current incident.

Channel Export
--------------

Exporting the contents of an incident channel requires the channel export plugin. See the `Channel Export plugin documentation <https://mattermost.gitbook.io/channel-export-plugin>`_ for more information.

API Documentation
-----------------

To interact with the incidents data model programmatically, consult the `REST API specification <https://github.com/mattermost/mattermost-plugin-incident-collaboration/blob/master/server/api/api.yaml>`_.
