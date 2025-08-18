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

.. tab:: Fully Connected
    :parse-titles:

    A Mattermost system admin must perform the following steps in Mattermost.

    1. Download the latest Mattermost Boards plugin binary file from the `Mattermost Boards Releases <https://github.com/mattermost/mattermost-plugin-boards/releases>`_ page.
    2. Log in to your Mattermost System Console as a system admin.
    3. Go to **Plugins > Plugin Management**.
    4. Select **Upload Plugin** to upload the Boards plugin binary file you downloaded from the Mattermost Releases page.

.. tab:: DDIL (Restricted/Contested)
    :parse-titles:

    This workflow usually involves a 3-step process that includes an external staging machine, an approved transfer path, and a manual installation.

    Step 1. Download Outside the Air Gap
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A system admin uses a separate internet-connected workstation, such as a jump box, staging system, or unclassified host, to download the plugin package from the `Mattermost Boards Releases <https://github.com/mattermost/mattermost-plugin-boards/releases>`_ page. The admin verifies the package hash and signature against Mattermost-provided checksums for authenticity.

    The downloaded plugin package ``.tar.gz`` file contains the plugin binary, manifest, and required assets and is scanned for malware. Additional whitelisting or aproval tickets may also be required.

    Step 2. Transfer Into the Restricted Network
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    The package must be transfered into the restricted network using an approved transfer mechanism, which may include encrypted, scanned USB media, secure removable drives, burning to CD/DVD, or using approved cross-domain transfer tools.

    Step 3. Manual Install Inside the Environment
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    In the Mattermost System Console, a Mattermost system admin goes to **Plugins > Plugin Management** and uses the **Upload Plugin** option to upload the package file. Then the Mattermost system admin configures the plugin, as described below.

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