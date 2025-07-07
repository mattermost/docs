Audit Log JSON Schema
==============================

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

The audit log JSON schema functions as a standardized blueprint or schematic that consistently defines how a single event should appear when being written to the audit log, including: field names, data types, objects, and structure.

An outline of the JSON audit logging schema is provided below. See the `JSON data model <#json-data-model>`__ for additional details.

.. code-block:: json

    {
        "timestamp": "",       // Event time
        "status": "",          // Success or failure of the audited event or activity
        "event_name": "",      // Logged event name
        "error": {             // Error if status = fail
            "status_code": 0,
            "description": ""
        },
        "actor": {             // The user performing the action
            "user_id": ""           // Unique identifier of the event user
            "session_id": ""        // Unique session identifier of the event user
            "client": ""            // User agent of the client/platform in use by the event user
            "ip_address": ""        // IPv4/IPv6 IP address of the event user
        },
        "event": {             // Event-specific data
            "parameters": {}        // Map containing parameters of the audited event or activity
            "prior_state": {}       // Pre-event state of the object
            "resulting_state": {}   // Post-event state of the object
            "object_type": ""       // Object targeted by the event or activity
        },
        "meta": {
            "api_path": "",         // API endpoint interacted with for event or activity
            "cluster_id": ""        // Unique identifier of the cluster in use by the event user
        }
    }


Audit log record examples
-------------------------

Update user preferences
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

    {
        "timestamp": "2022-08-17 20:37:52.846 +01:00",
        "event_name": "updatePreferences",
        "status": "success",
        "actor": {
            "user_id": "aw8ehkwaziytzry1qqxi9tsqwh",
            "session_id": "kth3jyadc3b1p84kbz6y3o75na",
            "client": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15",
            "ip_address": "192.168.0.169"
        },
        "event": {
            "parameters": {},
            "prior_state": {},
            "resulting_state": {},
            "object_type": ""
        },
        "meta": {
            "api_path": "/api/v4/users/aw8ehkwaziytzry1qqxi9tsqwh/preferences",
            "cluster_id": "8dxdbfx6fpdwtki1z6n8whtkho"
        },
        "error": {}
    }

Create post
~~~~~~~~~~~

.. code-block:: json

    {
        "timestamp": "2025-04-30 16:17:44.207 Z",
        "event_name": "createPost",
        "status": "success",
        "actor": {
            "user_id": "i764hi6h5bbz8p1955ed4ahj6y",
            "session_id": "t7894ft76igtpb788nkkej1yoy",
            "client": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            "ip_address": "172.19.0.8"
        },
        "event": {
            "parameters": {
                "post": {
                    "channel_id": "pfis7ycuy78o7m3zebajmxqeuo",
                    "user_id": "i764hi6h5bbz8p1955ed4ahj6y",
                    "message": "Sample post content"
                }
            },
            "prior_state": {},
            "resulting_state": {
                "channel_id": "pfis7ycuy78o7m3zebajmxqeuo",
                "create_at": 1746029864145,
                "id": "xpw97hf6kfncirzhqisb5sym7e",
                "user_id": "i764hi6h5bbz8p1955ed4ahj6y"
            },
            "object_type": "post"
        },
        "meta": {
            "api_path": "/api/v4/posts",
            "cluster_id": "i5twhjm3ainatcifiy3oksshae"
        },
        "error": {}
    }

System configuration change
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

    {
        "timestamp": "2025-04-30 16:18:30.803 Z",
        "event_name": "patchConfig",
        "status": "success",
        "actor": {
            "user_id": "i764hi6h5bbz8p1955ed4ahj6y",
            "session_id": "t7894ft76igtpb788nkkej1yoy",
            "client": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            "ip_address": "172.19.0.8"
        },
        "event": {
            "parameters": {},
            "prior_state": {
                "config_diffs": [
                    {
                        "actual_val": false,
                        "base_val": true,
                        "path": "MetricsSettings.EnableClientMetrics"
                    }
                ]
            },
            "resulting_state": {},
            "object_type": "config"
        },
        "meta": {
            "api_path": "/api/v4/config/patch",
            "cluster_id": "i5twhjm3ainatcifiy3oksshae"
        },
        "error": {}
    }

Audit event types
-----------------

The following table lists the audit event types (``event_name`` values) that are captured in Mattermost audit logs:

User Management Events
~~~~~~~~~~~~~~~~~~~~~~

+-------------------------+-------------------------------------------------------------------+
| **Event Name**          | **Description**                                                   |
+=========================+===================================================================+
| ``updatePreferences``   | User preference changes (themes, notifications, etc.)            |
+-------------------------+-------------------------------------------------------------------+
| ``extendSessionExpiry`` | User session extension activities                                 |
+-------------------------+-------------------------------------------------------------------+

Content and Communication Events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------+-------------------------------------------------------------------+
| **Event Name**          | **Description**                                                   |
+=========================+===================================================================+
| ``createPost``          | Post creation in channels                                         |
+-------------------------+-------------------------------------------------------------------+
| ``updatePost``          | Post editing and modifications                                    |
+-------------------------+-------------------------------------------------------------------+
| ``deletePost``          | Post deletion activities                                          |
+-------------------------+-------------------------------------------------------------------+

Channel Management Events
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------+-------------------------------------------------------------------+
| **Event Name**          | **Description**                                                   |
+=========================+===================================================================+
| ``createChannel``       | Channel creation activities                                       |
+-------------------------+-------------------------------------------------------------------+
| ``deleteChannel``       | Channel deletion activities                                       |
+-------------------------+-------------------------------------------------------------------+
| ``updateChannel``       | Channel setting modifications                                     |
+-------------------------+-------------------------------------------------------------------+

Team Management Events
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------+-------------------------------------------------------------------+
| **Event Name**          | **Description**                                                   |
+=========================+===================================================================+
| ``createTeam``          | Team creation activities                                          |
+-------------------------+-------------------------------------------------------------------+
| ``deleteTeam``          | Team deletion activities                                          |
+-------------------------+-------------------------------------------------------------------+
| ``updateTeam``          | Team setting modifications                                        |
+-------------------------+-------------------------------------------------------------------+

System Configuration Events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------+-------------------------------------------------------------------+
| **Event Name**          | **Description**                                                   |
+=========================+===================================================================+
| ``getConfig``           | System configuration retrieval                                    |
+-------------------------+-------------------------------------------------------------------+
| ``patchConfig``         | System configuration changes                                      |
+-------------------------+-------------------------------------------------------------------+
| ``updateConfig``        | System configuration updates                                      |
+-------------------------+-------------------------------------------------------------------+

Administrative Events
~~~~~~~~~~~~~~~~~~~~~~

+-------------------------+-------------------------------------------------------------------+
| **Event Name**          | **Description**                                                   |
+=========================+===================================================================+
| ``getLogs``             | System log retrieval activities                                   |
+-------------------------+-------------------------------------------------------------------+
| ``requestRenewalLink``  | License renewal link requests                                     |
+-------------------------+-------------------------------------------------------------------+

.. note::
   This list includes the most commonly audited events in Mattermost. Additional events may be logged depending on your Mattermost version, enabled features, and configuration settings. Enterprise features may generate additional audit events not listed here.

JSON data model
---------------

+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| **Name**   | **Type**                     | **Description**                                                                                                                     |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| timestamp  | int64                        | Date/time when event or activity has taken place.                                                                                   |
|            |                              |                                                                                                                                     |
|            |                              | Mattermost currently supports three log formats: plain, JSON, and                                                                   |
|            |                              | `GELF <https://go2docs.graylog.org/current/getting_in_log_data/gelf.html>`__.                                                       |
|            |                              |                                                                                                                                     |
|            |                              | - Plain log format uses `RFC3339 <https://www.rfc-editor.org/rfc/rfc3339>`__ by default.                                            |
|            |                              |   See the :ref:`plain log format configuration <manage/logging:plain log format configuration options>` documentation for           |
|            |                              |   supported options.                                                                                                                |
|            |                              | - JSON log format uses `RFC3339 <https://www.rfc-editor.org/rfc/rfc3339>`__ by default.                                             |
|            |                              |   See the :ref:`JSON log format configuration <manage/logging:json log format configuration options>` documentation for             |
|            |                              |   supported options.                                                                                                                |
|            |                              | - GELF log format uses `unixtime <https://www.unixtimestamp.com/>`__.                                                               |
|            |                              |   See the :ref:`GELF log format configuration <manage/logging:gelf log format configuration options>` documentation for             |
|            |                              |   supported options.                                                                                                                |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| event_name | string                       | Unique name and identifier of the event type taking place. See the :ref:`audit event types <audit event types>` section             |
|            |                              | for a comprehensive list of all supported event names.                                                                              |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| status     | string                       | Success or failure of the audited event.                                                                                            |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| event      | `EventData <#eventdata>`__   | Event parameters and object states.                                                                                                 |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| actor      | `EventActor <#eventactor>`__ | User involved with the event.                                                                                                       |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| meta       | `EventMeta <#eventmeta>`__   | Related event metadata.                                                                                                             |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| error      | `EventError <#eventerror>`__ | The resulting error if the status is in a failed state.                                                                             |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+

EventData
~~~~~~~~~

+-------------------+---------------+-------------------------------------------------------------------+
| **Field name**    | **Data type** | **Description**                                                   |
+-------------------+---------------+-------------------------------------------------------------------+
| parameters        | map           | Payload and parameters being processed as part of the request.    |
+-------------------+---------------+-------------------------------------------------------------------+
| prior_state       | map           | Prior state of the entity being modified. ``null`` if there was   |
|                   |               | no prior state.                                                   |
+-------------------+---------------+-------------------------------------------------------------------+
| resulting_state   | map           | Resulting entity after creating or modifying it.                  |
+-------------------+---------------+-------------------------------------------------------------------+
| object_type       | string        | String representation of the entity type (e.g. post)              |
+-------------------+---------------+-------------------------------------------------------------------+

EventActor
~~~~~~~~~~

+-------------------+---------------+-------------------------------------------------------------------+
| **Field name**    | **Data type** | **Description**                                                   |
+-------------------+---------------+-------------------------------------------------------------------+
| user_id           | string        | Unique identifier of the event actor.                             |
+-------------------+---------------+-------------------------------------------------------------------+
| session_id        | string        | Unique session identifier of the event actor.                     |
+-------------------+---------------+-------------------------------------------------------------------+
| client            | string        | User agent of the client/platform in use by the event actor.      |
+-------------------+---------------+-------------------------------------------------------------------+
| ip_address        | string        | IPv4/IPv6 IP address of the event actor.                          |
+-------------------+---------------+-------------------------------------------------------------------+

EventMeta
~~~~~~~~~

+-------------------+---------------+-------------------------------------------------------------------+
| **Field name**    | **Data type** | **Description**                                                   |
+-------------------+---------------+-------------------------------------------------------------------+
| api_path          | string        | The REST endpoint which caused the event.                         |
+-------------------+---------------+-------------------------------------------------------------------+
| cluster_id        | integer       | Cluster identifier.                                               |
+-------------------+---------------+-------------------------------------------------------------------+

EventError
~~~~~~~~~~

+-------------------+---------------+-------------------------------------------------------------------+
| **Field name**    | **Data type** | **Description**                                                   |
+-------------------+---------------+-------------------------------------------------------------------+
| description       | string        | (Optional) Error description.                                     |
+-------------------+---------------+-------------------------------------------------------------------+
| status_code       | integer       | (Optional) Error status code.                                     |
+-------------------+---------------+-------------------------------------------------------------------+
