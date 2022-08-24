Embedded JSON audit log schema
==============================

The JSON schema functions as a standardized blueprint or schematic that consistently defines how a single event should appear when being written to the audit log, including: field names, data types, objects, and structure.

The logging configuration JSON is an object (unordered collection) containing names and log target values. Each log target contains a type, options specific to the target type, format, and levels.

An outline of the JSON audit logging schema is provided below. See the `JSON data model <#json-data-model>` for additional details.

.. code-block:: json

    {
        "timestamp": "",       // Event time; RFC3339
        "level": "",           // Audit log level
        "status": "",          // Success or failure of the audited event or activity
        "error": "",           // Error if status = fail
        "actor": {,            // The user performing the action
            "user_id":              // Unique identifier of the event user
            "session_id":           // Unique session identifier of the event user
            "client":               // User agent of the client/platform in use by the event user
            "ip_address":           // IPv4/IPv6 IP address of the event user
        }
        "event_name": "",      // Logged event name
        "event": {             // Metadata of event
            "parameters": {}        // Map containing parameters of the audited event or activity
            "prior_state": {}       // Pre-event state of the object
            "resulting_state": {}   // Post-event state of the object
            "object_type":          // Object targeted by the event or activity
        }
        "meta": {             // 
            "api_path": "",         // API endpoint interacted with for event or activity
            "cluster_id": "",       // Unique identifier of the cluster in use by the event user
        }
    }

Example output
---------------

[TBD]

Create a team
~~~~~~~~~~~~~



Create a channel
~~~~~~~~~~~~~~~~



Delete a channel
~~~~~~~~~~~~~~~~


Extend session expiry
~~~~~~~~~~~~~~~~~~~~~



Update preferences
~~~~~~~~~~~~~~~~~~~



JSON data model
---------------

+------------+----------+--------------------------------------------------------------------------------------------------------------------+
| **Name**   | **Type** | **Description**                                                                                                    |
+------------+----------+--------------------------------------------------------------------------------------------------------------------+
| timestamp  | int64    | Date/time when event or activity has taken place.                                                                  |
|            |          |                                                                                                                    |
|            |          | Mattermost currently supports three log formats: plain, JSON, and `GELF <https://docs.graylog.org/docs/gelf>`__.   |
|            |          |                                                                                                                    |
|            |          | - Plain log format uses `RFC3339 <https://www.rfc-editor.org/rfc/rfc3339>`__ by default.                           |
|            |          |   See the `plain log format configuration <#plain-log-format-configuration-options>`__ documentation for           |
|            |          |   supported options.                                                                                               |
|            |          | - JSON log format uses `RFC3339 <https://www.rfc-editor.org/rfc/rfc3339>`__ by default.                            |
|            |          |   See the `JSON log format configuration <#plain-log-format-configuration-options>`__ documentation for            |
|            |          |   supported options.                                                                                               |  
|            |          | - GELF log format uses `unixtime <https://www.unixtimestamp.com/>`__.                                              |
|            |          |   See the `GELF log format configuration <#gelf-log-format-format-configuration-options>`__ documentation for      |
|            |          |   supported options.                                                                                               |    
+------------+----------+--------------------------------------------------------------------------------------------------------------------+
| level      | string   | Audit log level as described in configuration heading.                                                             |
|            |          |                                                                                                                    |
|            |          | - ``audit-api``: Enables output of REST API calls.                                                                 |
|            |          | - ``audit-content``: Enables output of API calls that generate content (e.g. create post, create reaction).        |
|            |          | - ``audit-permissions``: Enables output of all permissions failures.                                               |
|            |          | - ``audit-cli``: Enables output of legacy CLI calls.                                                               |
|            |          |                                                                                                                    |
|            |          | See the `log level configuration <#log-level-configuration-options>`__ documentation for details on supported      |
|            |          | options.                                                                                                           |
+------------+----------+--------------------------------------------------------------------------------------------------------------------+
| api_path   | string   | API REST endpoint used for the event or activity.                                                                  |
+------------+----------+--------------------------------------------------------------------------------------------------------------------+
| status     | string   | Success or failure of the audited event.                                                                           |
+------------+----------+--------------------------------------------------------------------------------------------------------------------+
| error      | string   | The resulting error if the status is in a failed state.                                                            |
+------------+----------+--------------------------------------------------------------------------------------------------------------------+
| actor      |          | User involved with the event.                                                                                      |
+------------+----------+--------------------------------------------------------------------------------------------------------------------+
| event-name | string   | Unique name and identifier of the event type taking place (e.g. ``getLogs`` ``requestRenewalLink``,                |
|            |          | ``createTeam``, ``createChannel``, ``deleteChannel``, or ``extendSessionExpiry``)                                  |
+------------+----------+--------------------------------------------------------------------------------------------------------------------+
| event      |          |                                       
+------------+----------+--------------------------------------------------------------------------------------------------------------------+
| meta       |          | 

