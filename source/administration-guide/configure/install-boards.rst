Install Mattermost Boards
==========================

.. include:: ../../_static/badges/ent-cloud-selfhosted.rst
   :start-after: :nosearch:

Mattermost Boards is not enabled by default for new Mattermost Enterprise instances. If the Mattermost Boards plugin isn't enabled for your Mattermost workspace, self-hosted Enterprise customers can install this plugin by manually uploading the binary release file into the System Console and enabling it.

Mattermost Cloud Enterprise customers can request the Boards plugins be enabled by contacting their Mattermost Account Manager or by `creating a support ticket <https://support.mattermost.com/hc/en-us/requests/new?ticket_form_id=11184911962004>`_ request.

.. note::

    The Mattermost Boards plugin is currently in maintenance mode. While adoption of this plugin is still supported for Enterprise customers, we recommend system admins proceed at their own risk. Mattermost is no longer actively developing new features or future improvements for the Boards plugin, beyond addressing bug fixes reported by Enterprise customers and any necessary security patches. 

    In the future, Mattermost plans to deliver a core Boards feature as part of the platform. Migration from the Boards plugin to this upcoming feature will be required, which could potentially involve downtime or data migration complexities. Keep this in mind when deploying the Boards plugin in production environments.

Install the plugin
-------------------

A Mattermost system admin must perform the following steps in Mattermost.

1. Download the latest Mattermost Boards plugin binary file from the `Mattermost Boards Releases <https://github.com/mattermost/mattermost-plugin-end-user-guide/project-management/releases>`_ page.
2. Log in to your Mattermost System Console as a system admin.
3. Go to **Plugins > Plugin Management**.
4. Select **Upload Plugin** to upload the Boards plugin binary file you downloaded from the Mattermost Releases page.

Mattermost configuration
------------------------

1. Go to **Plugins > Mattermost Boards**.
2. Select **Enable Plugin** to enable the plugin.
3. You can optionally enable **Enable Publicly-Shared Boards** so that board editors can share boards with people outside of your Mattermost instance, who can view the board without needing a Mattermost account.
4. Select **Save** to save your changes.

Access
-------

See the :doc:`navigate boards </end-user-guide/project-management/navigate-boards>` documentation to learn how to create and access boards.

Work with boards
-----------------

See the :doc:`project and task management </end-user-guide/project-task-management>` end user documentation to learn how to align, define, organize, track, and manage work across teams.