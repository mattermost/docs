Getting Started 
===============

Mattermost Playbooks is included in the Mattermost Cloud workspace, enabled by default, and upgraded automatically.

*For self-managed deployments*

Mattermost Playbooks is available in the Plugin Marketplace:

1. As a System Admin, go to **Main Menu > Plugin Marketplace**.
2. Search for **Playbooks**.
3. Select **Install** if not yet installed, then select **Configure** to enable.
4. From the plugin configuration page, set **Enable Plugin** to **true**.
5. Select **Save** to enable the plugin.

To access playbooks:

* From the Main Menu, select **Playbooks** to view stats, review incidents of which you are a member, and configure playbooks. System Admins have unrestricted access.
* From the channel header, select the **Playbook** icon to open the right-hand sidebar. From there, you can start a new playbook run or view runs you belong to.

Navigating playbooks
--------------------

Active runs 
~~~~~~~~~~~

When you're in a channel with an active run, the channel right-hand sidebar enables teams to have their conversation and procedure checklist side-by-side to effectively work towards the desired outcome. We’ve simplified the experience to help teams run playbooks faster, and focus better on the process at hand.

When opening the right-hand sidebar from a channel that is not running a playbook, it will now show the list of playbooks for that team that can be run with one-click.

Alternatively, if the current channel is already running a playbook, the right-hand sidebar will instead show the run details. Information such as run name and description can be edited in-line, and the checklists can be collapsed and filtered based on their status. 

Playbooks 
~~~~~~~~~

Playbooks are accessed via **Main Menu > Playbooks** in Mattermost, where you can also view a list of templates.

API Documentation
~~~~~~~~~~~~~~~~~~

To interact with the data model programmatically, consult the `REST API specification <https://github.com/mattermost/mattermost-plugin-incident-collaboration/blob/master/server/api/api.yaml>`_.
