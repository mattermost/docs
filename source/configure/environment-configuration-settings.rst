Environment configuration settings
==================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: common-config-settings-notation.rst
    :start-after: :nosearch:

Both self-hosted and Cloud admins can access the following configuration settings in **System Console > Environment**. Self-hosted admins can also edit the ``config.json`` file as described in the following tables. 

Web server
----------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: web-server-configuration-settings.rst
    :start-after: :nosearch:

----

Database
--------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: database-configuration-settings.rst
    :start-after: :nosearch:

----

Elasticsearch
-------------

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

.. include:: elasticsearch-configuration-settings.rst
    :start-after: :nosearch:

----

File storage
------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: file-storage-configuration-settings.rst
    :start-after: :nosearch:

----

Image proxy
-----------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: image-proxy-configuration-settings.rst
    :start-after: :nosearch:

----

SMTP
----

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: smtp-configuration-settings.rst
    :start-after: :nosearch:

----

Push notification server
------------------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: push-notification-server-configuration-settings.rst
    :start-after: :nosearch:

----

High availability
-----------------

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

.. include:: high-availability-configuration-settings.rst
    :start-after: :nosearch:

----

Rate limiting
-------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: rate-limiting-configuration-settings.rst
    :start-after: :nosearch:

----

Logging
--------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: logging-configuration-settings.rst
    :start-after: :nosearch:

----

Session lengths
---------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: session-lengths-configuration-settings.rst
    :start-after: :nosearch:

----

Performance monitoring
----------------------

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

.. include:: performance-monitoring-configuration-settings.rst
    :start-after: :nosearch:

----

Developer
---------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: developer-mode-configuration-settings.rst
    :start-after: :nosearch:

config.json-only settings
-------------------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. config:setting:: disable-customer-portal-requests
  :displayname: Disable customer portal requests
  :systemconsole: N/A
  :configjson: .CloudSettings.Disable
  :environment: MM_CLOUDSETTINGS_DISABLE
  :description: Enable or disable server requests to the Mattermost Customer Portal.

    - **true**: **(Default)** Server-side requests made to the customer portal are disabled.
    - **false**: Server-side requests made to the customer portal are enabled, but will always fail in air-gapped and restricted environments.

Disable Customer Portal requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------+---------------------------------------------------------------------------+
| Enable or disable customer portal requests.   | - System Config path: **N/A**                                             |
|                                               | - ``config.json setting``: ``CloudSettings`` > ``Disable`` > ``false,``   |
|                                               | - Environment variable: ``MM_CLOUDSETTINGS_DISABLE``                      |
| - **true**: **(Default)** Server-side         |                                                                           |
|   requests made to the customer portal are    |                                                                           |
|   disabled.                                   |                                                                           |
| - **false**: Server-side requests made to the |                                                                           |
|   Mattermost Customer Portal are enabled,     |                                                                           |
|   but will always fail in air-gapped and      |                                                                           |
|   restricted deployment environments.         |                                                                           |
+-----------------------------------------------+---------------------------------------------------------------------------+

.. note::
  Cloud admins can’t modify this configuration setting. 

.. config:setting:: exp-enableapiteamdeletion
  :displayname: Enable API team deletion (ServiceSettings)
  :systemconsole: N/A
  :configjson: EnableAPITeamDeletion
  :environment: N/A

  - **true**: The ``api/v4/teams/{teamid}?permanent=true`` API endpoint can be called by team admins and system admins (or users with appropriate permissions), or by running the mmctl team delete command, to permanently delete a team.
  - **false**: **(Default)** The API endpoint cannot be called, but ``api/v4/teams/{teamid}`` can still be used to soft delete a team.

Enable API team deletion
~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: The ``api/v4/teams/{teamid}?permanent=true`` API endpoint can be called by team admins and system admins (or users with appropriate permissions), or by running the :ref:`mmctl team delete <manage/mmctl-command-line-tool:mmctl team delete>` command to permanently delete a team.

**False**: The API endpoint cannot be called. Note that ``api/v4/teams/{teamid}`` can still be used to soft delete a team.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAPITeamDeletion": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enableapiuserdeletion
  :displayname: Enable API user deletion (ServiceSettings)
  :systemconsole: N/A
  :configjson: EnableAPIUserDeletion
  :environment: N/A

  - **true**: The ``api/v4/users/{userid}?permanent=true`` API endpoint can be called by system admins (or users with appropriate permissions), or by running the mmctl user delete command, to permanently delete a user.
  - **false**: **(Default)** The API endpoint cannot be called, but ``api/v4/users/{userid}`` can still be used to soft delete a user.

Enable API user deletion
~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: The ``api/v4/users/{userid}?permanent=true`` API endpoint can be called by system admins (or users with appropriate permissions), or by running the :ref:`mmctl user delete <manage/mmctl-command-line-tool:mmctl user delete>` command, to permanently delete a user.

**False**: The API endpoint cannot be called. Note that ``api/v4/users/{userid}`` can still be used to soft delete a user.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAPIUserDeletion": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enableapichanneldeletion
  :displayname: Enable API channel deletion (ServiceSettings)
  :systemconsole: N/A
  :configjson: EnableAPIChannelDeletion
  :environment: N/A

  - **true**: The ``api/v4/channels/{channelid}?permanent=true`` API endpoint can be called by system admins (or users with appropriate permissions), or by running the mmctl channel delete command, to permanently delete a channel.
  - **false**: **(Default)** The API endpoint cannot be called, but ``api/v4/channels/{channelid}`` can still be used to soft delete a channel.

Enable API channel deletion
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: The ``api/v4/channels/{channelid}?permanent=true`` API endpoint can be called by system admins (or users with appropriate permissions), or by running the :ref:`mmctl channel delete <manage/mmctl-command-line-tool:mmctl channel delete>` command, to permanently delete a channel.

**False**: The API endpoint cannot be called. Note that ``api/v4/channels/{channelid}`` can still be used to soft delete a channel.

+----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAPIChannelDeletion": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------+