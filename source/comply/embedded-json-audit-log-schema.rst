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

File target configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+----------+---------------------------------------------------------------------------------------------------------------------+
| **Key**     | **Type** | **Description**                                                                                                     |
+-------------+----------+---------------------------------------------------------------------------------------------------------------------+
| filename    | string   | Full path to the output file.                                                                                       |
+-------------+----------+---------------------------------------------------------------------------------------------------------------------+
| max_size    | number   | Maximum size, in megabytes (MB), the log file can grow before it gets rotated. Default is ``100`` MB.               |
+-------------+----------+---------------------------------------------------------------------------------------------------------------------+
| max_age     | number   | Maximum number of days to retain old log files based on the timestamp encoded in the filename.                      |
|             |          | Default is ``0`` which disables the removal of old log files.                                                       |
+-------------+----------+---------------------------------------------------------------------------------------------------------------------+
| max_backups | number   | Maximum number of old log files to retain. Default is ``0`` which retains all old log files.                        |
|             |          | **Note**: Configuring ``max_age`` can result in old log files being deleted regardless of this configuration value. |
+-------------+----------+---------------------------------------------------------------------------------------------------------------------+
| compress    | bool     | Compress rotated log files using gzip. Default is ``false``.                                                        |
+-------------+----------+---------------------------------------------------------------------------------------------------------------------+

Syslog target configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| **Key**  | **Type** | **Description**                                                                                                                 |
+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| host     | string   | IP or domain name of the server receiving the log records.                                                                      |
+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| port     | number   | Port number for the server receiving the log records.                                                                           |
+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| tls      | bool     | Create a TLS connection to the server receiving the log records. Default is ``false``.                                          |
+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| cert     | string   | Path to a cert file (.pem) to be used when establishing a TLS connection to the server.                                         |
+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| insecure | bool     | Mattermost Boards accepts any certificate presented by the server, and any host name in that certificate. Default is ``false``. |
|          |          | **Note**: Should only be used in testing environments, and shouldn’t be used in production environments.                        |
+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+

TCP target configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| **Key**  | **Type** | **Description**                                                                                                                 |
+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| host     | string   | IP or domain name of the server receiving the log records.                                                                      |
+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| port     | number   | Port number for the server receiving the log records.                                                                           |
+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| tls      | bool     | Create a TLS connection to the server receiving the log records. Default is ``false``.                                          |
+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| cert     | string   | Path to a cert file (.pem) to be used when establishing a TLS connection to the server.                                         |
+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| insecure | bool     | Mattermost Boards accepts any certificate presented by the server, and any host name in that certificate. Default is ``false``. |
|          |          | **Note**: Should only be used in testing environments, and shouldn’t be used in production environments.                        |
+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| tag      | string   | Syslog tag field.                                                                                                               |
+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+

Plain log format configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------+----------+------------------------------------------------------------------------------------------------------------------------------+
| **Key**             | **Type** | **Description**                                                                                                              |
+---------------------+----------+------------------------------------------------------------------------------------------------------------------------------+
| disable_timestamp   | bool     | Disables output of the timestamp. Default is ``false``.                                                                      |
+---------------------+----------+------------------------------------------------------------------------------------------------------------------------------+
| disable_level       | bool     | Disables output of the level name. Default is ``false``.                                                                     |
+---------------------+----------+------------------------------------------------------------------------------------------------------------------------------+
| disable_msg         | bool     | Disables output of the message text. Default is ``false``.                                                                   |
+---------------------+----------+------------------------------------------------------------------------------------------------------------------------------+
| disable_fields      | bool     | Disables output of all fields. Default is ``false``.                                                                         |
+---------------------+----------+------------------------------------------------------------------------------------------------------------------------------+
| disables_stacktrace | bool     | Disables output of stack traces. Default is ``false``.                                                                       |
+---------------------+----------+------------------------------------------------------------------------------------------------------------------------------+
| delim               | string   | Delimiter placed between fields. Default is single space.                                                                    |
+---------------------+----------+------------------------------------------------------------------------------------------------------------------------------+
| min_level_len       | number   | Minimum level name length. When level names are less than the minimum, level names are padded with spaces. Default is ``0``. |
+---------------------+----------+------------------------------------------------------------------------------------------------------------------------------+
| min_msg_len         | number   | Minimum message length. When message text is less than the minimum, message text is padded with spaces. Default is ``0``.    |
+---------------------+----------+------------------------------------------------------------------------------------------------------------------------------+
| timestamp_format    | string   | Format for timestamps. Default is `RFC3339 <https://www.rfc-editor.org/rfc/rfc3339>`__.                                      |
+---------------------+----------+------------------------------------------------------------------------------------------------------------------------------+
| line_end            | string   | Alternative end of line character(s). Default is ``n``.                                                                      |
+---------------------+----------+------------------------------------------------------------------------------------------------------------------------------+
| enable_color        | bool     | Enables color for targets that support color output. Default is ``false``.                                                   |
+---------------------+----------+------------------------------------------------------------------------------------------------------------------------------+

JSON log format configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------+----------+-----------------------------------------------------------------------------------------+
| **Key**             | **Type** | **Description**                                                                         |
+---------------------+----------+-----------------------------------------------------------------------------------------+
| disable_timestamp   | bool     | Disables output of the timestamp. Default is ``false``.                                 |
+---------------------+----------+-----------------------------------------------------------------------------------------+
| disable_level       | bool     | Disables output of the log level display name. Default is ``false``.                    |
+---------------------+----------+-----------------------------------------------------------------------------------------+
| disable_msg         | bool     | Disables output of the message text. Default is ``false``.                              |
+---------------------+----------+-----------------------------------------------------------------------------------------+
| disable_fields      | bool     | Disables output of all fields. Default is ``false``.                                    |
+---------------------+----------+-----------------------------------------------------------------------------------------+
| disables_stacktrace | bool     | Disables output of stack traces. Default is ``false``.                                  |
+---------------------+----------+-----------------------------------------------------------------------------------------+
| timestamp_format    | string   | Format for timestamps. Default is `RFC3339 <https://www.rfc-editor.org/rfc/rfc3339>`__. |
+---------------------+----------+-----------------------------------------------------------------------------------------+

GELF log format format configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+----------------------------------------------------------+
| **Key**  | **Type** | **Description**                                          |
+----------+----------+----------------------------------------------------------+
| hostname | string   | Outputs a custom hostname in log records.                |
|          |          | If omitted, hostname is taken from the operating system. |
+----------+----------+----------------------------------------------------------+

Log level configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------+----------+--------------------------------------------------------------+
| **Key**    | **Type** | **Description**                                              |
+------------+----------+--------------------------------------------------------------+
| id         | number   | Unique identifier for the log level.                         |
+------------+----------+--------------------------------------------------------------+
| name       | string   | Display name for the log level.                              |
+------------+----------+--------------------------------------------------------------+
| stacktrace | bool     | Outputs a stack trace. Default is ``false``.                 |
+------------+----------+--------------------------------------------------------------+
| color      | number   | The ANSI color code used to output parts of the log record.  |
|            |          | Supported values include:                                    |
|            |          |                                                              |
|            |          | - Black: ``30``                                              |
|            |          | - Red: ``31``                                                |
|            |          | - Green: ``32``                                              |
|            |          | - Yellow: ``33``                                             |
|            |          | - Blue: ``34``                                               |
|            |          | - Magenta: ``35``                                            |
|            |          | - Cyan: ``36``                                               |
|            |          | - White: ``37``                                              |
+------------+----------+--------------------------------------------------------------+