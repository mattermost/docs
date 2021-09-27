Audit Log v2 (Experimental) (E20)
=================================

*Available in Mattermost Enterprise Edition E20*

System Admins can review a comprehensive listing of events for more in-depth analysis and advanced logging capabilities. Additionally, the new audit log provides more control over where the logs are generated and stored. 

.. note::
   Mattermost v6.0 introduced a change to the logging engine library which changes how the logger is configured. Please see this `sample file <>`_. 

Configure audit log in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuring the Mattermost server to use the new audit log requires editing the ``config.json`` file directly. The audit settings output audit records to allow any combination of local file, syslog, and TCP socket targets.

File target supports rotation and compression triggered by size and/or duration. Syslog target supports local and remote syslog servers, with or without TLS transport. TCP socket target can be configured with an IP address or domain name, port, and optional TLS certificate.

**Accessing configuration options for audit log**

Open ``config.json`` and navigate to the audit settings under ``ExperimentalAuditSettings``. Within the setting ``AdvancedLoggingConfig`` you are able to specifiy a filespec to another config file, a database DSN, or JSON. 

The logging configuration JSON is an object (unordered collection) containing names and log target values. Each log target contains a type, options specific to the target type, format, and levels.

The example below specifies one log target that outputs to the console using a plain text format with pipes delimiting fields. The standard log levels are listed, with only `error` and lower outputing a stack trace. The `error` level will output in red for log targets and formatters that support color output.

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

Log Target Types
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
       "insecure", "bool", "false", "When true, Focalbaord will accept any certificate presented by the server and any host name in that certificate. Should be used only in testing environments."
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
       "insecure", "bool", "false", "When true, Mattermost will accept any certificate presented by the server and any host name in that certificate. Should be used only in testing environments."

    
To temporarily disable a log target its type can be set to "none".

Log Formatters
~~~~~~~~~~~~~~~~~~~
Mattermost currently supports three log formats: plain, json, and `GELF <https://docs.graylog.org/en/4.0/pages/gelf.html>`_.

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

**Json configuration options:**

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

Log Levels 
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


Supported logging events
~~~~~~~~~~~~~~~~~~~~~~~~~

- Events evoked from the Mattermost API
- Events evoked from mmctl 
- Events evoked from the legacy Mattermost CLI
- Events evoked from the Focalboard plugin

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

Configure audit log in Focalboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The `Focalboard configuration file <https://github.com/mattermost/focalboard/blob/main/config.json>`_ ``config.json`` is used to configure logging.

``logging_cfg_file`` is used to specify the path to a file containing the logging configuration in JSON format.

``logging_cfg_json`` is used to provide logging configuration directly as embedded JSON. Typically this is overridden using the corresponding environment variable ``FOCALBOARD_LOGGING_CFG_JSON``.

Both configuration methods can be used, but care must be taken to avoid mutiple log targets writing to the same file.

The logging configuration JSON is an object (unordered collection) containing names and log target values. Each log target contains a type, options specific to the type, format, and levels.

Focalboard uses discrete log levels, meaning each level to be output must be listed. This allows for log targets to output specific log levels, and custom log levels to be created. See ``server/mlog/levels.go`` for a list of available log levels. 

Planned enhancements to the audit log
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure audit logs cannot be unknowingly corrupted or tampered with, make it possible to configure the logging engine to sign log files for specific targets. When an audit store cannot be made secure, audit logs could be stored in multiple places (e.g. file and database) so they can be reconciled if needed.

Planned enhancements to logging in general
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Allow discrete logging levels. Currently, an application-wide logging level is configured and any log records matching that level or lower will be emitted. These logging levels will remain, but support for zero or more discrete logging levels will be added, meaning only records matching the current log level or one of the discrete levels are emitted. Within the logging engine, any level below 10 (``trace`` through ``critical``/``fatal``, plus ``reserved``) will behave as it does currently, but any level above 10 will be considered discrete. Audit records will have a level above 10.

- Allow logging levels and discrete levels to different targets (files, databases, etc) via configuration.

See the `logging enhancements <https://docs.google.com/document/d/1DSE-SKfqwcpUIXKUokWFIh_uAp3nzw-5UkKBUt90ZqE/edit?usp=sharing>`_ proposal for more details.
