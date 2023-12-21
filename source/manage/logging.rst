Mattermost logging
===================

.. include:: ../_static/badges/allplans-cloud-selfhosted.rst
  :start-after: :nosearch:

.. contents:: On this page
    :depth: 2

By default, Mattermost writes logs to both the console and to the ``mattermost.log`` file in a machine-readable JSON format. 

You can customize the following logging options based on your business practices and needs by going to **System Console > Environment > Logging** or by editing the ``config.json`` file directly: 


Console logs
------------

Console logs feature verbose debug level log messages written to the console using the standard output stream (stdout). 

Customize the following console logs by going to **System Console > Environment > Logging** or by editing the ``config.json`` file directly:

- `Stop outputting console logs </configure/environment-configuration-settings.html#output-logs-to-console>`__
- `Adjust console log level </configure/environment-configuration-settings.html#console-log-level>`__ 
- `Output console logs as plain text </configure/environment-configuration-settings.html#output-console-logs-as-json>`__ & `colorize plain text log level details </configure/environment-configuration-settings.html#colorize-plain-text-console-logs>`__
- `Omit webhook debug messages </configure/environment-configuration-settings.html#enable-webhook-debugging>`__

File logs
---------

File logs feature info level log messages including errors and information around startup and initialization and webhook debug messages. The file is stored in ``./logs/mattermost.log``, rotated at 100 MB, and archived to a separate file in the same directory.

Customize the following file logs by going to **System Console > Environment > Logging** or by editing the ``config.json`` file directly:

- `Stop outputting file logs <https://docs.mattermost.com/configure/environment-configuration-settings.html#output-logs-to-file>`__
- `Adjust file log level <https://docs.mattermost.com/configure/environment-configuration-settings.html#file-log-level>`__ 
- `Output file logs as plain text <https://docs.mattermost.com/configure/environment-configuration-settings.html#output-file-logs-as-json>`__
- `Change where the file is stored <https://docs.mattermost.com/configure/environment-configuration-settings.html#file-log-directory>`__

You can optionally output log records to any combination of `console <#console-target-configuration-options>`__, `local file <#file-target-configuration-options>`__, `syslog <#syslog-target-configuration-options>`__, and `TCP socket <#tcp-target-configuration-options>`__ targets, each featuring additional customization. See `Advanced Logging <#advanced-logging>`__ for details.

Define logging output
---------------------

Define logging output in JSON format in the System Console by going to **Environment > Logging > Advanced Logging** or by editing the ``config.json`` file directly. You can use the sample JSON below as a starting point.

.. code-block:: JSON

    {
        "console1": {
            "Type": "console",
            "Format": "json",
            "Levels": [
                {"ID": 5, "Name": "debug", "Stacktrace": false},
                {"ID": 4, "Name": "info", "Stacktrace": false, "color": 36},
                {"ID": 3, "Name": "warn", "Stacktrace": false},
                {"ID": 2, "Name": "error", "Stacktrace": true, "color": 31},
                {"ID": 1, "Name": "fatal", "Stacktrace": true, "color": 31},
                {"ID": 0, "Name": "panic", "Stacktrace": true, "color": 31},
                {"ID": 10, "Name": "stdlog", "Stacktrace": false}
            ],
            "Options": {
                "Out": "stdout"
            },
            "MaxQueueSize": 1000
        },
        "file1": {
            "Type": "file",
            "Format": "json",
            "Levels": [
                {"ID": 5, "Name": "debug", "Stacktrace": false},
                {"ID": 4, "Name": "info", "Stacktrace": false},
                {"ID": 3, "Name": "warn", "Stacktrace": false},
                {"ID": 2, "Name": "error", "Stacktrace": true},
                {"ID": 1, "Name": "fatal", "Stacktrace": true},
                {"ID": 0, "Name": "panic", "Stacktrace": true}
            ],
            "Options": {
                "Compress": true,
                "Filename": "mattermost_logging.log",
                "MaxAgeDays": 1,
                "MaxBackups": 10,
                "MaxSizeMB": 100 
            },
            "MaxQueueSize": 1000
        },
        "file2": {
            "Type": "file",
            "Format": "json",
            "Levels": [
                {"ID": 2, "Name": "error", "Stacktrace": true},
                {"ID": 1, "Name": "fatal", "Stacktrace": true},
                {"ID": 0, "Name": "panic", "Stacktrace": true}
            ],
            "Options": {
                "Compress": true,
                "Filename": "mattermost_logging_errors.log", 
                "MaxAgeDays": 30,
                "MaxBackups": 10,
                "MaxSizeMB": 100
            },
            "MaxQueueSize": 1000
        }
    }

----

Audit logging (Beta)
-----------------------------

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

By default, Mattermost doesn’t write audit logs locally to a file on the server. You can enable and customize experimental audit logging in Mattermost to record activities and events performed within a Mattermost workspace, such as access to the Mattermost REST API or mmctl. 

.. tip::
    From Mattermost v9.3, you can enable and customize advanced logging for AD/LDAP events separately from other logging.

- Logs are recorded asynchronously to reduce latency to the caller, and are stored separately from general logging.
- During short spans of inability to write to targets, the audit records buffer in memory with a configurable maximum record cap. Based on typical audit record volumes, it could take many minutes to fill the buffer. After that, the records are dropped, and the record drop event is logged.

You can define `whether audit events are output to file </configure/experimental-configuration-settings.html#write-audit-files-locally>`__, `the name and path of the audit logging file </configure/experimental-configuration-settings.html#file-name>`__, the `maximum size of each file </configure/experimental-configuration-settings.html#file-max-size-mb>`__, the `maximum number of days before triggering a rotation </configure/experimental-configuration-settings.html#file-max-age-days>`__, the `maximum number of rotated files to keep </configure/experimental-configuration-settings.html#file-max-backups>`__, `whether files are compressed using GZIP </configure/experimental-configuration-settings.html#file-compress>`__, and `how many audit records can be queued/buffered </configure/experimental-configuration-settings.html#file-max-queue-size>`__ at any point in time when writing to a file.

In addition, you can output audit log records to any combination of `console <#console-target-configuration-options>`__, `local file <#file-target-configuration-options>`__, `syslog <#syslog-target-configuration-options>`__, and `TCP socket <#tcp-target-configuration-options>`__ targets, each featuring additional customization. See `Advanced Logging <#advanced-logging>`__ for details.  

.. warning::
    
    - From Mattermost v7.2, experimental audit logging beta is a breaking change from previous releases in cases where customers looking to parse previous audit logs with the new format.
    - The format and content of an audit log record has changed to become standardized for all events using a `standard JSON schema </comply/embedded-json-audit-log-schema.html>`__.
    - Existing tools which ingest or parse audit log records may need to be modified.

----

Advanced logging
-----------------

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

System admins can output log and audit records to any combination of `console <#console-target-configuration-options>`__, `local file <#file-target-configuration-options>`__, `syslog <#syslog-target-configuration-options>`__, and `TCP socket <#tcp-target-configuration-options>`__ targets. Each output target features additional configuration options you can customize for your Mattermost deployment.

.. tip::
    
    - From Mattermost v9.3, system admins can configure advanced logging options in the System Console using multi-line JSON by going to **Environment > Logging**.
    - Alternatively, admins can configure advanced logging within the ``AdvancedLoggingJSON`` section of the ``config.json`` file using multi-line JSON or escaped JSON as a string.
    - Mattermost Team Edition customers can output audit log records to the console or a file.

Advanced logging options can be configured to:

- Enable trace logging for AD/LDAP to troubleshoot authentication issues.
- Capture errors and panics in a separate, monitored file that triggers alerts.
- Capture production debug and error logs in a separate file with log file rotation to reproduce issues, while enforcing a cap on the amount of disk space the debug logs are allowed to use.
- Audit every API endpoint accessed during a user workflow.

Configuring advanced logging includes the following steps:

- `Define log output <#define-audit-log-output>`__ as multi-line JSON or a filespec to another configuration file.
- `Specify destination targets <#specify-destination-targets>`__, including any combination of `console <#console-target-configuration-options>`__, `local file <#file-target-configuration-options>`__, `syslog <#syslog-target-configuration-options>`__, and `TCP socket <#tcp-target-configuration-options>`__ targets.
- `Configure format preferences <#specify-destination-targets>`__ for `plain <#plain-log-format-configuration-options>`__, `JSON <#json-log-format-configuration-options>`__, or `GELF <#gelf-log-format-configuration-options>`__ output.
- `Configure log levels & events <#configure-log-levels-and-events>`__
- `Configure target-specific settings <#configure-target-specific-settings>`__

Define advanced log output
~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

    .. tab:: Multi-line JSON

        In the example below, file output is written to ``./logs/audit.log`` in plain text and includes all audit log levels & events. Older logs are kept for 1 day, and up to a total of 10 backup log files are kept at a time. Logs are rotated using gzip when the maximum size of the log file reaches 500 MB. A maximum of 1000 audit records can be queued/buffered while writing to the file.

        .. code-block:: JSON

            "AdvancedLoggingJSON": {
                "file_1": {
                    "Type": "file",
                    "Format": "plain",
                    "Levels": [
                    { "id": 100, "name": "audit-api" },
                    { "id": 101, "name": "audit-content" },
                    { "id": 102, "name": "audit-permissions" },
                    { "id": 103, "name": "audit-cli" }
                    ],
                    "Options": {
                        "Compress": true,
                        "Filename": "./logs/audit.log",
                        "MaxAgeDays": 1,
                        "MaxBackups": 10,
                        "MaxSizeMB": 500
                    },
                    "MaxQueueSize": 1000
                }
            }

    .. tab:: Filespec

        Advanced logging configuration can be pointed to a filespec to another configuration file, rather than multi-line JSON, to keep the config.json file tidy:

        .. code:: JSON

            "AdvancedLoggingJSON": "/path/to/audit_log_config.json"

        The separate configuration file includes the multi-line JSON instead.

        In the example below, the first output is written to the console in plain text and includes all audit log levels, events, and command outputs. A pipe ``|`` delimiter is placed between fields. 

        A second output is written to ``./logs/audit.log`` in plain text in a machine-readable JSON format and includes all audit log levels, events, and command outputs. Older logs are kept for 1 day, and up to a total of 10 backup log files are kept at a time. Logs are rotated using GZIP when the maximum size of the log file reaches 500 MB. A maximum of 1000 audit records can be queued/buffered while writing to the file.

        Contents of ``audit_log_config.json`` file:

        .. code-block:: JSON

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
                "filename": "./logs/audit.log",
                "max_age": 1,
                "max_backups": 10,
                "max_size": 500
                },
                "maxqueuesize": 1000
            }
            }

Specify destination targets
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Log records can be sent to any combination of `console <#console-target-configuration-options>`__, `local file <#file-target-configuration-options>`__, `syslog <#syslog-target-configuration-options>`__, and `TCP socket <#tcp-target-configuration-options>`__ targets. Log targets have been chosen based on support for the vast majority of log aggregators and other log analysis tools, without needing additional software installed.

System Admins can define multiple log targets to:

- Mirror log output to files and log aggregators for redundancy.
- Log certain entries to specific destinations. For example, all ``audit-content`` records can be routed to a different destination than the other levels.
- Admins can also temporarily disable log targets by setting its ``type`` to ``none``.

Configure format preferences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

System admins can control log formatting per target.

Plain log format configuration options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------+----------+----------------------------------------------------------+
| **Key**  | **Type** | **Description**                                          |
+----------+----------+----------------------------------------------------------+
| hostname | string   | Outputs a custom hostname in log records.                |
|          |          | If omitted, hostname is taken from the operating system. |
+----------+----------+----------------------------------------------------------+

Configure log levels and events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Log levels
^^^^^^^^^^

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
| 140    | ``LDAPError``         | AD/LDAP authentication errors                                            |
+--------+-----------------------+--------------------------------------------------------------------------+
| 141    | ``LDAPWarn``          | AD/LDAP authentication warnings                                          |
+--------+-----------------------+--------------------------------------------------------------------------+
| 142    | ``LDAPInfo``          | AD/LDAP authentication information logs                                  |
+--------+-----------------------+--------------------------------------------------------------------------+
| 143    | ``LDAPDebug``         | AD/LDAP authentication debug logs                                        |
+--------+-----------------------+--------------------------------------------------------------------------+
| 144    | ``LDAPTrace``         | AD/LDAP authentication trace logs. Replaces ``LdapSetings.trace`` from   |
|        |                       | Mattermost v9.3.                                                         |
+--------+-----------------------+--------------------------------------------------------------------------+

Configure target-specific settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Console target configuration options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Console targets can be either ``stdout`` or ``stderr``.

- The standard output stream, ``stout``, is typically used for command output that prints the results of a command to the user. 
- The standard error stream, ``sterr``, is typically used to print any errors that occur when a program is running.

File target configuration options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

File targets support rotation and compression triggered by size and/or duration.

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

Syslog targets support local and remote syslog servers, with or without TLS transport. Syslog target support requires Mattermost Enterprise.

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

The TCP socket targets can be configured with an IP address or domain name, port, and optional TLS certificate. TCP socket target support requires Mattermost Enterprise.

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

---- 

Frequently asked questions
--------------------------

Does Mattermost have an audit log besides the system ``auditd``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. See the `audit logging <#audit-logging-experimental-beta>`__ documentation for details.

When syslog is configured as the target, does it contain the IP address of the emitter of the data (i.e., the Mattermost app node)?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. That is a function of the syslog daemon (receiver). Typically, all the log lines are prefixed with a timestamp and the hostname of the node sending the data. For example, a log line starts with: ``Nov 28 10:56:59 tower kernel: [1072437.431123]  ....``, where ``tower`` is the hostname of the server that generated the log line.

Once audit logs are enabled, can audit logging track events where an admin disables or modifies the audit log settings?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes, though it depends on how audit logs are configured. Audit log config can be specified via REST API, mmctl, System Console, file on disk, and using environment variables. When changes are made via the REST API or System Console, there is an audit record. However, the Mattermost server can't capture changes to a configuration file or via environment variables.

Do server logs show any information about a service or similar stopping/updating when auditing would be disabled? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yes. When updating the audit log configuration via REST API, mmctl, or System Console, the last event of the audit log should be about the admin user updating the config of the server, which helps your security team identify which actions took place in the system and by whom.

How do I omit incoming webhook details from the logs?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See `enable-webhook-debugging </configure/environment-configuration-settings.html#enable-webhook-debugging>`__

How do I adjust the maximum log field size?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See `maximum-field-size </configure/environment-configuration-settings.html#maximum-field-size>`__