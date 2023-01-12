Product configuration settings
===============================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Self-hosted admins can access the following configuration setting in **System Console > Products**, or by editing the ``config.json`` file as described in the following table. 

Boards
------

.. config:setting:: products-enablepubliclysharedboards
  :displayname: Enable publicly-shared boards (Products > Boards)
  :systemconsole: Products > Boards
  :configjson: .ProductSettings.EnablePublicSharedBoards
  :environment: MM_PRODUCTSETTINGS_ENABLEPUBLICSHAREDBOARDS
  :description: Enable the ability to share links to boards publicly with other users.

Enable publicly-shared boards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+--------------------------------------------------------------------------------------+
| Enable or disable the ability to share               | - System Config path: **Products > Boards**                                          |
| links to Mattermost boards with other users.         | - ``config.json`` setting: ``".ProductSettings.EnablePublicSharedBoards: false”, ``  |
|                                                      | - Environment variable: ``MM_PRODUCTSETTINGS_ENABLEPUBLICSHAREDBOARDS``              |
| - **true**: Enables the ability to share links to    |                                                                                      |
|   Mattermost boards with other users.                |                                                                                      |
| - **false**: **(Default)** Mattermost boards can't   |                                                                                      |
|   be shared with other users.                        |                                                                                      |
+------------------------------------------------------+--------------------------------------------------------------------------------------+
| **Notes**:                                                                                                                                  |
|                                                                                                                                             |
| - From Mattermost v7.7, this configuration setting applies to Mattermost Boards available as an official in-product vertical. See the       |
|   `plugins configuration settings <configure/plugins-configuration-settings.html#enable-publicly-shared-boards>`__ documentation for        |
|   details on configuring the plugin-specific setting instead.                                                                               |        
| - See the `Mattermost Boards <guides/boards.html>`__ end user documentation for details on `sharing boards links with other                 |
|   users <boards/share-and-collaborate.html#share-a-board-publicly>`__.                                                                      |
| - Cloud admins can't modify this configuration setting.                                                                                     |
+------------------------------------------------------+--------------------------------------------------------------------------------------+
