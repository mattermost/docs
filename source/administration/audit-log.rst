Audit Log v2 (Experimental) (E20)
=================================

*Available in Mattermost Enterprise Edition E20*

System Admins can review a comprehensive listing of events for more in-depth analysis. Additionally, the new audit log provides more control over where the logs are generated and stored.

Configure audit log in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuring the Mattermost server to use the new audit log requires editing the ``config.json`` file directly. The audit settings output audit records to syslog (local or remote server via TLS) as well as to a local file. Syslog and local file storage can be enabled simultaneously. Both are disabled by default.

**Accessing configuration options for audit log**

Open ``config.json`` and navigate to the audit settings. The following `configuration options <https://docs.mattermost.com/administration/config-settings.html#audit-settings>`_ are available:

- Syslog configuration options:

    - Enable settings to write audit records to a local or remote syslog
    - Specify the IP
    - Specify port
    - Add user-generated fields
    - Configure certificate settings

- File configuration options:

    - Enable settings to write audit files locally
    - Specify file size
    - Specify backup interval
    - Add compression
    - Set maximum age to manage file rotation

Supported logging events
~~~~~~~~~~~~~~~~~~~~~~~~~

- Events evoked from the Mattermost API
- Events evoked from mmctl 
- Events evoked from the legacy Mattermost CLI

Data model
~~~~~~~~~~~~

A single audit record is emitted for each event (``add``, ``delete``, ``login``, ``...``). Multiple auditable events may be emitted for a single API call.

.. csv-table::
    :header: "Name", "Type", "Description"

    "ID.", "string", "audit record ID."
    "CreateAt", "int64", "timestamp of record creation, UTC."
    "Level", "string", "e.g. ``audit-rest``, ``audit-app``, ``audit-model``"
    "APIPath", "string", "rest endpoint"
    "Event", "string", "e.g. ``add``, ``delete``, ``login``, ``...``"
    "Status", "string", "e.g. ``attempt``, ``success``, ``fail``, ``...``"
    "UserId", "string", "ID of user calling the API"
    "SessionId". "string", "ID of session used to call the API"
    "Client", "string", "e.g. webapp, mmctl, user-agent"
    "IPAddress", "string", "IP address of client"
    "Meta", "map[string]interface{}", "API-specific info (e.g. user id being deleted)"

Log storage
~~~~~~~~~~~

Audit records are stored separately from general logging. The general log storage location is configurable via ``LogSettings`` in the ``config.json`` file.

During short spans of inability to write to targets, the audit records buffer in memory with a cap. Based on typical audit record volumes it could take many minutes to fill the buffer. After that, the records are dropped and the record drop event is logged.

When using remote syslog, the current best practice is to also write to local file so no records are lost. Note that this does not automatically take records from local file and send it to syslog when syslog becomes available again.

Planned enhancements to the audit log
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure audit logs cannot be unknowingly corrupted or tampered with, make it possible to configure the logging engine to sign log files for specific targets. When an audit store cannot be made secure, audit logs could be stored in multiple places (e.g. file and database) so they can be reconciled if needed.

Planned enhancements to logging in general
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Allow discrete logging levels. Currently, an application-wide logging level is configured and any log records matching that level or lower will be emitted. These logging levels will remain, but support for zero or more discrete logging levels will be added, meaning only records matching the current log level or one of the discrete levels are emitted. Within the logging engine, any level below 10 (``trace`` through ``critical``/``fatal``, plus ``reserved``) will behave as it does currently, but any level above 10 will be considered discrete. Audit records will have a level above 10.

- Make logging engine enhancements implemented via the ``mlog`` package and will be compatible with existing usage.

- Allow logging levels and discrete levels to different targets (files, databases, etc) via configuration.

See the `logging enhancements <https://docs.google.com/document/d/1DSE-SKfqwcpUIXKUokWFIh_uAp3nzw-5UkKBUt90ZqE/edit?usp=sharing>`_ proposal for more details.
