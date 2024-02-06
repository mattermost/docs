Audit Log JSON Schema
==============================

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

*Also available in legacy Mattermost Enterprise Edition E20*

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

JSON data model
---------------

+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| **Name**   | **Type**                     | **Description**                                                                                                                     |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| timestamp  | int64                        | Date/time when event or activity has taken place.                                                                                   |
|            |                              |                                                                                                                                     |
|            |                              | Mattermost currently supports three log formats: plain, JSON, and `GELF <https://docs.graylog.org/docs/gelf>`__.                    |
|            |                              |                                                                                                                                     |
|            |                              | - Plain log format uses `RFC3339 <https://www.rfc-editor.org/rfc/rfc3339>`__ by default.                                            |
|            |                              |   See the `plain log format configuration </manage/logging.html#plain-log-format-configuration-options>`__ documentation for        |
|            |                              |   supported options.                                                                                                                |
|            |                              | - JSON log format uses `RFC3339 <https://www.rfc-editor.org/rfc/rfc3339>`__ by default.                                             |
|            |                              |   See the `JSON log format configuration </manage/logging.html#json-log-format-configuration-options>`__ documentation for          |
|            |                              |   supported options.                                                                                                                |
|            |                              | - GELF log format uses `unixtime <https://www.unixtimestamp.com/>`__.                                                               |
|            |                              |   See the `GELF log format configuration </manage/logging.html#gelf-log-format-configuration-options>`__ documentation for          |
|            |                              |   supported options.                                                                                                                |
+------------+------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| event_name | string                       | Unique name and identifier of the event type taking place (e.g. ``getLogs`` ``requestRenewalLink``,                                 |
|            |                              | ``createTeam``, ``createChannel``, ``deleteChannel``, or ``extendSessionExpiry``).                                                  |
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
