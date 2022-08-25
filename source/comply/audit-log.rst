Audit logging (beta)
====================

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Mattermost Enterprise Edition E20*

Audit logging provides System Admins, including Security, IT/SRE, Compliance, and HR/PeopleOps teams, with a method of recording activities and events performed within a Mattermost workspace, such as access to the REST API or mmctl. Mattermost audit logging offers you control over where the audit logs are generated and stored, and applies a standard `JSON schema <#json-data-model>`__ to log output. 

.. note:: 

  - Logs are recorded asynchronously to reduce latency to the caller, and are stored separately from general logging.
  - During short spans of inability to write to targets, the audit records buffer in memory with a configurable maximum size cap. Based on typical audit record volumes, it could take many minutes to fill the buffer. After that, the records are dropped, and the record drop event is logged.
  - When using syslog remotely, we recommend writing to a local file so no records are lost. Records won’t be taken from the local file and sent back to syslog when syslog becomes available again.

Configure audit logging
-----------------------

Configuring Mattermost to enable audit logging requires editing the ``config.json`` file directly. Audit logging can’t be managed using the System Console.

In the ``config.json`` file, go to the ``ExperimentalAuditSettings`` section. Within the ``AdvancedLoggingConfig`` setting, you can specify an absolute or relative filespec to another configuration file, a database DSN, or a JSON object. The process of configuring audit logging includes specifying destination targets, event names to include, and the verbosity of the audit log output.

The example below specifies two log targets: one outputs to the console using a plain text format with pipes delimiting fields, and the other outputs to a file using XXX. The standard `log levels <#log-level-configuration-options>`__ are listed, with only error and lower outputting a stack trace. The error level will be output and displayed in the color red for log targets and formatters that support `color output <#log-level-configuration-options>`__.

.. code-block:: json

  {
    "sample-console": {
      "type": "console",
      "options": {
        "out": "stdout"
      },
      "format": "plain",
      "format_options": {
        "delim": " | "
      },
      "levels": [
        {"id": 5, "name": "debug"},
        {"id": 4, "name": "info"},
        {"id": 3, "name": "warn"},
        {"id": 2, "name": "error", "stacktrace": true, "color": 31},
        {"id": 1, "name": "fatal", "stacktrace": true},
        {"id": 0, "name": "panic", "stacktrace": true}
      ],
      "maxqueuesize": 1000
    }
  }

Configure audit logging in Mattermost Boards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `Boards configuration file <https://github.com/mattermost/focalboard/blob/main/config.json>`_ ``config.json`` is used to configure logging.

``logging_cfg_file`` is used to specify the path to a file containing the logging configuration in JSON format.

``logging_cfg_json`` is used to provide logging configuration directly as embedded JSON. Typically this is overridden using the corresponding environment variable ``FOCALBOARD_LOGGING_CFG_JSON``.

Both configuration methods can be used, but care must be taken to avoid multiple log targets writing to the same file.

The logging configuration JSON is an object (unordered collection) containing names and log target values. Each log target contains a type, options specific to the type, format, and levels.

Boards uses discrete log levels, meaning each level to be output must be listed. This allows for log targets to output specific log levels, and custom log levels to be created. See ``server/mlog/levels.go`` for a list of available log levels. 

Multiple file and target support
--------------------------------

System Admins can define multiple log targets to:

- Mirror log output to files and log aggregators for redundancy.
- Log certain entries to specific destinations. For example, all errors could be routed to a specific destination for review.

Admins can also temporarily disable log targets by setting its type to ``none``.

Any combination of console, local file, syslog, and TCP socket targets can send log records to multiple targets. Log targets have been chosen based on support for the vast majority of log aggregators and other log analysis tools, without needing additional software installed.

- Console targets can be either ``stdout`` or ``stderr``.
- File targets support rotation and compression triggered by size and/or duration. See the `file target configuration <#file-target-configuration-options>`__ documentation for supported options.
- Syslog targets support local and remote syslog servers, with or without TLS transport. See the `syslog target configuration <#syslog-target-configuration-options>`__ documentation for supported options.
- The TCP socket target can be configured with an IP address or domain name, port, and optional TLS certificate. See the `TCP target configuration <#tcp-target-configuration-options>`__ documentation for supported options.

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
| compress    | bool     | Compress rotated log files using `gzip <https://www.gnu.org/software/gzip/>`__. Default is ``false``.               |
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

JSON data model
---------------

Record
~~~~~~

+-------------------+---------------+-------------------------------------------------------------------+
| **Field name**    | **Data type** | **Description**                                                   |
+-------------------+---------------+-------------------------------------------------------------------+
| event_name        | string        | Unique event type identifier (e.g. ``getLogs``                    |
|                   |               | ``requestRenewalLink``, ``createTeam``, ``createChannel``,        |
|                   |               | ``deleteChannel``, or ``extendSessionExpiry``)                    |
+-------------------+---------------+-------------------------------------------------------------------+
| status            | string        | Success or failure of the audited event.                          |
+-------------------+---------------+-------------------------------------------------------------------+
| event             | EventData     | Contains all event-specific data about the modified entity.       |
+-------------------+---------------+-------------------------------------------------------------------+
| actor             | EventActor    | User involved with the audited event.                             |
+-------------------+---------------+-------------------------------------------------------------------+
| meta              | map           | A key/value store that contains related event information that    |
|                   |               | isn't directly related to the modified entity, such as            |
|                   |               | ``api_path`` and ``cluster_id``                                   |
+-------------------+---------------+-------------------------------------------------------------------+
| error             | EventError    | (Optional) Error information in case of event failure.            |
+-------------------+---------------+-------------------------------------------------------------------+

EventData
^^^^^^^^^

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
| object_type       | string        | String representation of the entity type (e.g post)               |
+-------------------+---------------+-------------------------------------------------------------------+

EventActor
^^^^^^^^^^

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

EventError
^^^^^^^^^^

+-------------------+---------------+-------------------------------------------------------------------+
| **Field name**    | **Data type** | **Description**                                                   |
+-------------------+---------------+-------------------------------------------------------------------+
| description       | string        | (Optional) Error description.                                     |
+-------------------+---------------+-------------------------------------------------------------------+
| status_code       | integer       | (Optional) TBD                                                    |
+-------------------+---------------+-------------------------------------------------------------------+

Audit log record examples
~~~~~~~~~~~~~~~~~~~~~~~~~

Create a team
^^^^^^^^^^^^^^

[code here]

Create a channel
^^^^^^^^^^^^^^^^

[code here]

Delete a channel
^^^^^^^^^^^^^^^^

[code here]

Extend session expiry
^^^^^^^^^^^^^^^^^^^^^

[code here]

Update user preferences
^^^^^^^^^^^^^^^^^^^^^^^

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