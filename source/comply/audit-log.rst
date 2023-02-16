Audit logging (beta)
====================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Mattermost Enterprise Edition E20*

.. warning::

  - Audit logging beta from Mattermost v7.2 is a **breaking change** from previous releases.
  - The format and content of an audit log record has changed to become standardized for all events.
  - Existing tools which ingest or parse audit log records may need to be modified.

Audit logging provides System Admins, including Security, IT/SRE, Compliance, and HR/PeopleOps teams, with a method of recording activities and events performed within a Mattermost workspace, such as access to the REST API or mmctl. Mattermost audit logging offers you control over where the audit logs are generated and stored, and applies a standard :doc:`JSON schema </comply/embedded-json-audit-log-schema>` to log output.

.. note::

  - Logs are recorded asynchronously to reduce latency to the caller, and are stored separately from general logging.
  - During short spans of inability to write to targets, the audit records buffer in memory with a configurable maximum record cap. Based on typical audit record volumes, it could take many minutes to fill the buffer. After that, the records are dropped, and the record drop event is logged.

Configure audit logging
-----------------------

Configuring Mattermost to enable audit logging requires editing the ``config.json`` file directly. Audit logging can’t be managed using the System Console.

In the ``config.json`` file, go to the ``ExperimentalAuditSettings`` section. Within the ``AdvancedLoggingConfig`` setting, you can specify an absolute or relative filespec to another configuration file or a JSON string. The process of configuring audit logging includes specifying destination targets, event names to include, and the verbosity of the audit log output.

The example JSON configuration specifies two log targets: one outputs to the console using a plain text format with pipes delimiting fields, and the other outputs to a file using a JSON format with log file rotation. All audit log levels are enabled.

.. code-block:: json

    {
      "sample-console": {
        "type": "console",
        "format": "plain",
        "format_options": {
            "delim": " | "
        },
        "levels": [
          { "id": 100, "name": "audit-api" },
          { "id": 101, "name": "audit-content" },
          { "id": 102, "name": "audit-permissions" },
          { "id": 103, "name": "audit-cli" }
        ],
        "options": {
          "out": "stdout"
        },
        "maxqueuesize": 1000
      },
      "sample-file": {
        "type": "file",
        "format": "json",
        "levels": [
          { "id": 100, "name": "audit-api" },
          { "id": 101, "name": "audit-content" },
          { "id": 102, "name": "audit-permissions" },
          { "id": 103, "name": "audit-cli" }
        ],
        "options": {
          "compress": true,
          "filename": "audit.log",
          "max_age": 1,
          "max_backups": 10,
          "max_size": 500
        },
        "maxqueuesize": 1000
      }
    }

Examples of values for the ``AdvancedLoggingConfig`` setting are:

1. Filespec to another configuration file; this file will contain a JSON object

  ``"AdvancedLoggingConfig": "/path/to/audit_log_config.json"``

2. JSON string

  ``"AdvancedLoggingConfig": "{\"sample-console\":{\"type\":\"console\",\"format\":\"plain\",\"format_options\":{\"delim\":\" | \"},\"levels\":[{\"id\":100,\"name\":\"audit-api\"},{\"id\":101,\"name\":\"audit-content\"},{\"id\":102,\"name\":\"audit-permissions\"},{\"id\":103,\"name\":\"audit-cli\"}],\"options\":{\"out\":\"stdout\"},\"maxqueuesize\":1000},\"sample-file\":{\"type\":\"file\",\"format\":\"json\",\"levels\":[{\"id\":100,\"name\":\"audit-api\"},{\"id\":101,\"name\":\"audit-content\"},{\"id\":102,\"name\":\"audit-permissions\"},{\"id\":103,\"name\":\"audit-cli\"}],\"options\":{\"compress\":true,\"filename\":\"audit.log\",\"max_age\":1,\"max_backups\":10,\"max_size\":500},\"maxqueuesize\":1000}}"``

.. note::
  When using a JSON string as the value of ``AdvancedLoggingConfig``, ensure you escape double quotes (``"``) in the string using a backslash (``\``). You can also use a free online tool, such as `Free Online JSON Escape <https://www.freeformatter.com/json-escape.html>`__ to format the value correctly.

Log level configuration options
-------------------------------

+------------+----------+--------------------------------------------------------------+
| **Key**    | **Type** | **Description**                                              |
+------------+----------+--------------------------------------------------------------+
| id         | number   | Unique identifier of the log level.                          |
+------------+----------+--------------------------------------------------------------+
| name       | string   | Name of the log level.                                       |
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

Audit log levels
~~~~~~~~~~~~~~~~

The following audit log levels are available:

+--------+-----------------------+--------------------------------------------------------------------------+
| **ID** | **Name**              | **Description**                                                          |
+--------+-----------------------+--------------------------------------------------------------------------+
| 100    | ``audit-api``         | API events                                                               |
+--------+-----------------------+--------------------------------------------------------------------------+
| 101    | ``audit-content``     | Content changes. This log level can generate considerably more records   |
|        |                       | than the other audit log levels.                                         |
+--------+-----------------------+--------------------------------------------------------------------------+
| 102    | ``audit-permissions`` | Permission changes                                                       |
+--------+-----------------------+--------------------------------------------------------------------------+
| 103    | ``audit-cli``         | CLI operations                                                           |
+--------+-----------------------+--------------------------------------------------------------------------+

Multiple file and target support
--------------------------------

System Admins can define multiple log targets to:

- Mirror log output to files and log aggregators for redundancy.
- Log certain entries to specific destinations. For example, all ``audit-content`` records can be routed to a different destination than the other levels.

Admins can also temporarily disable log targets by setting its type to ``none``.

Log records can be sent to any combination of console, local file, syslog, and TCP socket targets. Log targets have been chosen based on support for the vast majority of log aggregators and other log analysis tools, without needing additional software installed.

- Console targets can be either ``stdout`` or ``stderr``.
- File targets support rotation and compression triggered by size and/or duration. See the `file target configuration <#file-target-configuration-options>`__ documentation for supported options.
- Syslog targets support local and remote syslog servers, with or without TLS transport. Syslog target support is available with Mattermost Enterprise. See the `syslog target configuration <#syslog-target-configuration-options>`__ documentation for supported options.
- The TCP socket targets can be configured with an IP address or domain name, port, and optional TLS certificate. TCP socket target support is available with Mattermost Enterprise. See the `TCP target configuration <#tcp-target-configuration-options>`__ documentation for supported options.


Console target configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------+----------+---------------------------------------------------------------------------+
| **Key** | **Type** | **Description**                                                           |
+---------+----------+---------------------------------------------------------------------------+
| out     | string   | Console output pipe name: ``stdout`` for STDOUT or ``stderr`` for STDERR. |
+---------+----------+---------------------------------------------------------------------------+

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

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

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
| insecure | bool     | Mattermost accepts any certificate presented by the server, and any host name in that certificate. Default is ``false``.        |
|          |          | **Note**: Should only be used in testing environments, and shouldn’t be used in production environments.                        |
+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+

TCP target configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

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
| insecure | bool     | Mattermost accepts any certificate presented by the server, and any host name in that certificate. Default is ``false``.        |
|          |          | **Note**: Should only be used in testing environments, and shouldn’t be used in production environments.                        |
+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+
| tag      | string   | Syslog tag field.                                                                                                               |
+----------+----------+---------------------------------------------------------------------------------------------------------------------------------+

Format configuration options
----------------------------

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

GELF log format configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------+----------+----------------------------------------------------------+
| **Key**  | **Type** | **Description**                                          |
+----------+----------+----------------------------------------------------------+
| hostname | string   | Outputs a custom hostname in log records.                |
|          |          | If omitted, hostname is taken from the operating system. |
+----------+----------+----------------------------------------------------------+
