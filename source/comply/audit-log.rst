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

Audit logging provides System Admins, including Security, IT/SRE, Compliance, and HR/PeopleOps teams, with a method of recording activities and events performed within a Mattermost workspace, such as access to the REST API or mmctl. Mattermost audit logging offers you control over where the audit logs are generated and stored. 

.. note:: 

  - Logs are recorded asynchronously to reduce latency to the caller, and are stored separately from general logging.
  - During short spans of inability to write to targets, the audit records buffer in memory with a configurable maximum size cap. Based on typical audit record volumes, it could take many minutes to fill the buffer. After that, the records are dropped, and the record drop event is logged.
  - When using syslog remotely, we recommend writing to a local file so no records are lost. Records won’t be taken from the local file and sent back to syslog when syslog becomes available again.

Multiple file and target support
--------------------------------

System Admins can define multiple log targets to:

- Mirror log output to files and log aggregators for redundancy.
- Log certain entries to specific destinations. For example, all errors could be routed to a specific destination for review.

You can also temporarily disable log targets by setting its type to ``none``.

Any combination of console, local file, syslog, and TCP socket targets can send log records to multiple targets. Log targets have been chosen based on support for the vast majority of log aggregators and other log analysis tools, without needing additional software installed.

- Console targets can be either ``stdout`` or ``stderr``.
- File targets support rotation and compression triggered by size and/or duration. See the `file target configuration <https://docs.mattermost.com/comply/embedded-json-audit-log-schema.html#file-target-configuration-options>`__ documentation for supported options.
- Syslog targets support local and remote syslog servers, with or without TLS transport. See the `syslog target configuration <https://docs.mattermost.com/comply/embedded-json-audit-log-schema.html#syslog-target-configuration-options>`__ documentation for supported options.
- The TCP socket target can be configured with an IP address or domain name, port, and optional TLS certificate. See the `TCP target configuration <https://docs.mattermost.com/comply/embedded-json-audit-log-schema.html#tcp-target-configuration-options>`__ documentation for supported options.

Configure audit logging
-----------------------

Configuring Mattermost to enable audit logging requires editing the ``config.json`` file directly. Audit logging can’t be managed using the System Console.

In the ``config.json`` file, navigate to the ``ExperimentalAuditSettings`` section. Within the ``AdvancedLoggingConfig`` setting, you can specify an absolute or relative filespec to another configuration file, a database DSN, or a JSON object.

1. Specify the destination targets for the audit log output as console, file, syslog, and/or TCP socket.
2. Specify the event names to include and identify the event names exclude from being written out.
3. Specify the verbosity of audit log output.

Configure audit logging in Mattermost Boards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `Boards configuration file <https://github.com/mattermost/focalboard/blob/main/config.json>`_ ``config.json`` is used to configure logging.

``logging_cfg_file`` is used to specify the path to a file containing the logging configuration in JSON format.

``logging_cfg_json`` is used to provide logging configuration directly as embedded JSON. Typically this is overridden using the corresponding environment variable ``FOCALBOARD_LOGGING_CFG_JSON``.

Both configuration methods can be used, but care must be taken to avoid multiple log targets writing to the same file.

The logging configuration JSON is an object (unordered collection) containing names and log target values. Each log target contains a type, options specific to the type, format, and levels.

Boards uses discrete log levels, meaning each level to be output must be listed. This allows for log targets to output specific log levels, and custom log levels to be created. See ``server/mlog/levels.go`` for a list of available log levels. 