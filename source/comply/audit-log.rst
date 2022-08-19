Audit log v2 (experimental)
===========================

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Mattermost Enterprise Edition E20*

Audit log v2 is an experimental feature that provides System Admins with a comprehensive listing of events for more in-depth analysis. Additionally, the new audit log provides more control over where the logs are generated and stored. 

The advanced logging capabilities of the Audit Log V2 allow any combination of console, local file, syslog, and TCP socket targets, and can send log records to multiple targets. These targets have been chosen as they support the vast majority of log aggregators, and other log analysis tools, without needing additional software installed.

System Admins can define multiple log targets to:

- Mirror log output to files and log aggregators for redundancy.
- Log certain entries to specific destinations. For example, all errors could be routed to a specific destination for review.

All access to the REST API or CLI is audited. When using Advanced Logging for auditing, System Admins can capture the following auditing in the target configuration in addition to discrete log levels:

.. code-block:: none

   "Levels": [
      {"ID": 100, "Name": "audit-api"},
      {"ID": 101, "Name": "audit-content"},
      {"ID": 102, "Name": "audit-permissions"},
      {"ID": 103, "Name": "audit-cli"},
   ],

where:

- ``audit-api``: Enables output of REST API calls.
- ``audit-content``: Enables output of API calls that generate content (e.g. ``create post``, ``create reaction``).
- ``audit-permissions``: Enables output of all permissions failures.
- ``audit-cli``: Enables output of legacy CLI calls.

All levels can be viewed at ``mattermost-server/shared/mlog/levels.go``.

.. Note::
  - Logs are recorded asynchronously to reduce latency to the caller. 
  - In version 5.x advanced logging supports hot-reloading of logger configuration. In versions 6.0 and greater, hot-reloading of configuration as been removed. 

Configure audit log in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuring the Mattermost server to use the new audit log requires editing the ``config.json`` file directly. The audit settings output audit records to allow any combination of local file, syslog, and TCP socket targets.

File target supports rotation and compression triggered by size and/or duration. Syslog target supports local and remote syslog servers, with or without TLS transport. TCP socket target can be configured with an IP address or domain name, port, and optional TLS certificate.

.. note::
   Mattermost v6.0 introduced a change to the logging engine library which changes how the logger is configured in Mattermost 5.x versions. Please refer to :download:`Advanced Logging sample file <../samples/sample-logger-config.json>` for a sample configuration file supported from v6.0. 

   
**Accessing configuration options for audit log**

Open ``config.json`` and navigate to the audit settings under ``ExperimentalAuditSettings``. Within the setting ``AdvancedLoggingConfig`` you are able to specifiy a filespec to another config file, a database DSN, or JSON. 

The logging configuration JSON is an object (unordered collection) containing names and log target values. Each log target contains a type, options specific to the target type, format, and levels.

The example below specifies one log target that outputs to the console using a plain text format with pipes delimiting fields. The standard log levels are listed, with only `error` and lower outputting a stack trace. The `error` level will output in red for log targets and formatters that support color output.

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
    
.. note::
    Filenames for ``AdvancedLoggingConfig`` can contain an absolute filename, a relative filename, or embedded JSON.

Sample configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~

Download the :download:`advanced logging options sample JSON ZIP file <../samples/advanced-logging-options-sample-json.zip>` for a sample configuration file. Options outlined in ``Log.Settings.Options.txt`` file within the downloaded ZIP file are described in the following table.

+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| **Key**       | **Definition**                                                                                                                                         | **Type**    |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| **Levels**    |                                                                                                                                                        |             |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| ID            | Unique log level identifier. Must be registered in ``mattermost/mattermost-server/shared/mlog/levels.go``.                                             | int         |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Name          | Human-readable name for the log level identifier.                                                                                                      | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Stacktrace    | Set to ``true`` to generate a stacktrace. Set to ``false`` to prevent a stacktrace from being generated.                                               | bool        |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| **Targets**   |                                                                                                                                                        |             |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Type          | Can be one of: ``console``, ``file``, ``syslog``, or ``tcp``.                                                                                          | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Format        | Can be either ``json`` or ``plain``.                                                                                                                   | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Levels        | Array of log levels.                                                                                                                                   | []          |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Options       | Map of options specific to the target type.                                                                                                            | {}          |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| MaxQueueSize  | The number of audit records that can be queued/buffered at any point in time when writing to syslog. Default is 1000.                                  | int         |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| **Console**   |                                                                                                                                                        |             |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Out           | Can be either ``stdout`` or ``stderr``.                                                                                                                | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| **File**      |                                                                                                                                                        |             |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Filename      | Path and filename for logs.                                                                                                                            | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| MaxAgeDays    | Number of days until a rotation is triggered. Set to ``0`` to not rotate based on age.                                                                 | int         |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| MaxBackups    | Maximum number of rotated files to keep where the oldest are deleted. Set to ``0`` to discard rotated files.                                           | int         |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| MaxSizeMB     | Maximum file size before a rotation is triggered. Set to ``0`` to prevent rotation based on file size.                                                 | int         |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Compress      | Set to ``true`` to compress files after rotation. Set to ``false`` to not compress files after rotation.                                               | bool        |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| **SysLog**    |                                                                                                                                                        |             |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| IP            | IP address or domain of the syslog server.                                                                                                             | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Port          | Listening port of syslog server.                                                                                                                       | int         |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Tag           | Typically the program name, machine name, or node name.                                                                                                | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| TLS           | Set to ``true`` to connect via TLS. Set to ``false`` to prevent connecting via TLS.                                                                    | bool        |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Cert          | For TLS connections where TLS is set to ``true``, the filename of client certificate or base64-encoded certificate.                                    | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Insecure      | Used for testing purposes only. Set to ``true`` to prevent a certificate check from being performed. Set to ``false`` to perform a certificate check.  | bool        |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| **TCP**       |                                                                                                                                                        |             |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| IP            | IP address or domain of the socket server.                                                                                                             | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Port          | Listening port of the socket server.                                                                                                                   | int         |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| TLS           | Set to ``true`` to connect via TLS. Set to ``false`` to prevent connecting via TLS.                                                                    | bool        |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Cert          | For TLS connections where TLS is set to ``true``, the filename of client certificate or base64-encoded certificate.                                    | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Insecure      | Used for testing purposes only. Set to ``true`` to prevent a certificate check from being performed. Set to ``false`` to perform a certificate check.  | bool        |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+

.. note::

    Filenames for ``AdvancedLoggingConfig`` can contain an absolute filename, a relative filename, or embedded JSON.

Log target types
~~~~~~~~~~~~~~~~

Log target types include Console, Syslog, File, or TCP. 

**Console configuration options:**

.. csv-table::
    :header: "Key", "Type", "Default", "Description"
       
       "out", "string", " ", "One of `stdout` or `stderr`. "

**Syslog configuration options:**

.. csv-table::
    :header: "Key", "Type", "Default", "Description"
       
       "host", "string", " ", "IP or domain name of server to receive log records."
       "port", "number", "", "Port number for server receiving log records."
       "tls", "bool", "false", "When true, a TLS connection will be created."
       "cert", "string", "  ", "Path to a cert file (.pem) to be used when establishing a TLS connection."
       "insecure", "bool", "false", "When true, Boards will accept any certificate presented by the server and any host name in that certificate. Should be used only in testing environments."
       "tag", "string", " ", "Syslog tag field."


**File configuration options:**

.. csv-table::
    :header: "Key", "Type", "Default", "Description"

       "filename", "string", "  ", "Full path to output file."
       "max_size", "number", "100", "Maximum size in megabytes the log file can grow before it gets rotated."
       "max_age", "number", "0", "Maximum number of days to retain old log files based on the timestamp encoded in their filename. 0 means do not remove old log files based on age."
       "max_backups", "number", "0", "Maximum number of old log files to retain.  0 means retain all old log files (though max_age may still cause them to get deleted.)"
       "compress", "bool", "false", "When true, the rotated log files will be compressed using gzip."

    
**TCP configuration options:** 

.. csv-table::
    :header: "Key", "Type", "Default", "Description"
       
       "host", "string", "  ", "IP or domain name of server to receive log records."
       "port", "number", " ", "Port number for server receiving log records."
       "tls", "bool", "false", "When true, a TLS connection will be created."
       "cert", "string", "  ", "Path to a cert file (.pem) to be used when establishing a TLS connection."
       "insecure", "bool", "false", "When true, any certificate will be accepted and any host name in that certificate. Should be used only in testing environments."

    
To temporarily disable a log target its type can be set to "none".

Log formatters
~~~~~~~~~~~~~~~

Mattermost currently supports three log formats: plain, JSON, and `GELF <https://docs.graylog.org/en/4.0/pages/gelf.html>`__.

**Plain configuration options:**

.. csv-table::
    :header: "Key", "Type", "Default", "Description"
 
       "disable_timestamp", "bool", "alse", "Disables output of the timestamp."
       "disable_level", "bool", "false", "Disables output of the level name."
       "disable_msg", "bool", "false", "Disables output of the message text."
       "disable_fields", "bool", "false", "Disables output of all fields."
       "disable_stacktrace", "bool", "false", "Disables output of stack traces."
       "delim", "string", "single space", "Delimiter placed between fields."
       "min_level_len", "number", "0", "Minimum level name length. If the level name is less than the minimum it will be padded with spaces."
       "min_msg_len", "number", "0", "Minimum msg length. If the msg text is less than the minimum it will be padded with spaces."
       "timestamp_format", "string", "2006-01-02 15:04:05.000 Z07:00", "Format for timestamps. See `format <https://golang.org/pkg/time/#Time.Format>`_ for format details."
       "line_end", "string", "\n ", "Alternative end of line character(s)."
       "enable_color", "bool", "false", "Enables color for targets that support color output."

**JSON configuration options:**

.. csv-table::
    :header: "Key", "Type", "Default", "Description"
 
       "disable_timestamp", "bool", "false", "Disables output of the timestamp."
       "disable_level", "bool", "false", "Disables output of the level name."
       "disable_msg", "bool", "false", "Disables output of the message text."
       "disable_fields", "bool", "false", "Disables output of all fields."
       "disable_stacktrace", "bool", "false", "Disables output of stack traces."
       "timestamp_format", "string", "2006-01-02 15:04:05.000 Z07:00", "Format for timestamps. See `format <https://golang.org/pkg/time/#Time.Format>`_ for format details."

 
**GELF configuration options:**

.. csv-table::
    :header: "Key", "Type", "Default", "Description"
  
       "hostname", "string", "string", "Provides a custom hostname to be output in log records, otherwise hostname is taken from the operating system."

Log levels 
~~~~~~~~~~~

**Level configuration options:**

.. csv-table::
    :header: "Key", "Type", "Default", "Description"
    
       "id", "number", " ", "Unique id for the log level."
       "name", "string"," ", "Name to be output."
       "stacktrace", "bool", "false", "When true, a stack trace is output."
       "color", "number", " ", "ANSI color code to output parts of the log record. See color chart below."

**Colors (ANSI)**

.. csv-table::
    :header: "Name", "Value"
       
       "black", "30"
       "red", "31"
       "green", "32"
       "yellow", "33"
       "blue", "34"
       "magenta", "35"
       "cyan", "36"
       "white", "37"


Data model
~~~~~~~~~~~

A single audit record is emitted for each event (``add``, ``delete``, ``login``, ``...``). Multiple auditable events may be emitted for a single API call.

.. csv-table::
    :header: "Name", "Type", "Description"

    "ID", "string", "audit record ID."
    "CreateAt", "int64", "timestamp of record creation, UTC."
    "Level", "string", "e.g. ``audit-rest``, ``audit-app``, ``audit-model``"
    "APIPath", "string", "rest endpoint"
    "Event", "string", "e.g. ``add``, ``delete``, ``login``, ``...``"
    "Status", "string", "e.g. ``attempt``, ``success``, ``fail``, ``...``"
    "UserId", "string", "ID of user calling the API"
    "SessionId", "string", "ID of session used to call the API"
    "Client", "string", "e.g. webapp, mmctl, user-agent"
    "IPAddress", "string", "IP address of client"
    "Meta", "map[string]interface{}", "API-specific info (e.g. user id being deleted)"

Log storage
~~~~~~~~~~~

Audit records are stored separately from general logging. The general log storage location is configurable via ``LogSettings`` in the ``config.json`` file.

During short spans of inability to write to targets, the audit records buffer in memory with a cap. Based on typical audit record volumes it could take many minutes to fill the buffer. After that, the records are dropped and the record drop event is logged.

When using remote syslog, the current best practice is to also write to local file so no records are lost. Note that this does not automatically take records from local file and send it to syslog when syslog becomes available again.

Configure audit log in Boards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `Boards configuration file <https://github.com/mattermost/focalboard/blob/main/config.json>`_ ``config.json`` is used to configure logging.

``logging_cfg_file`` is used to specify the path to a file containing the logging configuration in JSON format.

``logging_cfg_json`` is used to provide logging configuration directly as embedded JSON. Typically this is overridden using the corresponding environment variable ``FOCALBOARD_LOGGING_CFG_JSON``.

Both configuration methods can be used, but care must be taken to avoid multiple log targets writing to the same file.

The logging configuration JSON is an object (unordered collection) containing names and log target values. Each log target contains a type, options specific to the type, format, and levels.

Boards uses discrete log levels, meaning each level to be output must be listed. This allows for log targets to output specific log levels, and custom log levels to be created. See ``server/mlog/levels.go`` for a list of available log levels. 


Planned enhancements to the audit log
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure audit logs cannot be unknowingly corrupted or tampered with, make it possible to configure the logging engine to sign log files for specific targets. When an audit store cannot be made secure, audit logs could be stored in multiple places (e.g. file and database) so they can be reconciled if needed.

Planned enhancements to logging in general
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the `logging enhancements <https://docs.google.com/document/d/1DSE-SKfqwcpUIXKUokWFIh_uAp3nzw-5UkKBUt90ZqE/edit?usp=sharing>`_ proposal for more details.
