:orphan:
:nosearch:

Configure logging by going to **System Console > Environment > Logging**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

Output logs to console
~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------+---------------------------------------------------------------------+
| Configure Mattermost to output logs to the    | - System Config path: **Environment > Logging**                     |
| console.                                      | - ``config.json setting``: ``".LogSettings.EnableConsole": true",`` |
|                                               | - Environment variable: ``MM_LOGSETTINGS_ENABLECONSOLE``            |
| - **true**: **(Default)** Output log messages |                                                                     |
|   are written to the console based on the     |                                                                     |
|   `console log level <#console-log-level>`__  |                                                                     |
|   configuration. The server writes messages   |                                                                     |
|   to the standard output stream (stdout).     |                                                                     | 
| - **false**: Output log messages aren’t       |                                                                     |
|   written to the console.                     |                                                                     |
+-----------------------------------------------+---------------------------------------------------------------------+

Console log level
~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------+---------------------------------------------------------------------+
| The level of detail in log events written     | - System Config path: **Environment > Logging**                     |
| when Mattermost outputs log messages to the   | - ``config.json setting``: ``".LogSettings.ConsoleLevel": DEBUG",`` |
| console.                                      | - Environment variable: ``MM_LOGSETTINGS_CONSOLELEVEL``             |
|                                               |                                                                     |
| - **DEBUG**: **(Default)** Outputs verbose    |                                                                     |
|   detail for developers debugging issues.     |                                                                     |
| - **ERROR**: Outputs only error messages.     |                                                                     |
| - **INFO**: Outputs error messages and        |                                                                     |
|   information around startup and              |                                                                     |
|   initialization.                             |                                                                     |
+-----------------------------------------------+---------------------------------------------------------------------+

Output console logs as JSON
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------+---------------------------------------------------------------------+
| Configure Mattermost to output console logs   | - System Config path: **Environment > Logging**                     |
| as JSON.                                      | - ``config.json setting``: ``".LogSettings.ConsoleJson": true",``   |
|                                               | - Environment variable: ``MM_LOGSETTINGS_CONSOLEJSON``              |
| - **true**: **(Default)** Logged events are   |                                                                     |
|   written in a machine-readable JSON format.  |                                                                     |
|   Typically set to **true** in production.    |                                                                     |
| - **false**: Logged events are written in     |                                                                     |
|   plain text.                                 |                                                                     |
+-----------------------------------------------+---------------------------------------------------------------------+

Output logs to file
~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------+---------------------------------------------------------------------+
| Configure Mattermost to output console logs   | - System Config path: **Environment > Logging**                     |
| to a file.                                    | - ``config.json setting``: ``".LogSettings.EnableFile": true",``    |
|                                               | - Environment variable: ``MM_LOGSETTINGS_ENABLEFILE``               |
| - **true**: **(Default)** Logged events are   |                                                                     |
|   written based on the                        |                                                                     |
|   `file log level <#file-log-level>`__        |                                                                     |
|   configuration to a ``mattermost.log`` file  |                                                                     |
|   located in the directory configured via     |                                                                     |
|   file location. Typically set to **true**    |                                                                     |
|   in production.                              |                                                                     | 
| - **false**: Logged events aren’t written to  |                                                                     |
|   a file.                                     |                                                                     |
+-----------------------------------------------+---------------------------------------------------------------------+

File log level
~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------+---------------------------------------------------------------------+
| The level of detail in log events when        | - System Config path: **Environment > Logging**                     |
| Mattermost outputs log messages to a file.    | - ``config.json setting``: ``".LogSettings.FileLevel": INFO",``     |
|                                               | - Environment variable: ``MM_LOGSETTINGS_FILELEVEL``                |
| - **DEBUG**: Outputs verbose detail for       |                                                                     |
|   developers debugging issues.                |                                                                     |
| - **ERROR**: Outputs only error messages.     |                                                                     |
| - **INFO**: **(Default)** Outputs error       |                                                                     |
|   messages and information around startup     |                                                                     |
|   and initialization.                         |                                                                     |
+-----------------------------------------------+---------------------------------------------------------------------+

Output file logs as JSON
~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------+---------------------------------------------------------------------+
| Configure Mattermost to output file logs as   | - System Config path: **Environment > Logging**                     |
| JSON.                                         | - ``config.json setting``: ``".LogSettings.FileJson": true",``      |
|                                               | - Environment variable: ``MM_LOGSETTINGS_FILEJSON``                 |
| - **true**: **(Default)** Logged events are   |                                                                     |
|   written in a machine-readable JSON format.  |                                                                     |
|   Typically set to **true** in production.    |                                                                     |  
| - **false**: Logged events are written in     |                                                                     |
|   plain text.                                 |                                                                     |
+-----------------------------------------------+---------------------------------------------------------------------+

File log directory
~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------+---------------------------------------------------------------------+
| The location of the log files.                | - System Config path: **Environment > Logging**                     |
|                                               | - ``config.json setting``: ``".LogSettings.FileLocation": "",``     |
| String input. If left blank, log files are    | - Environment variable: ``MM_LOGSETTINGS_FILELOCATION``             |
| stored in the ``./logs`` directory.           |                                                                     |
+-----------------------------------------------+---------------------------------------------------------------------+
| **Note**: The path you configure must exist, and Mattermost must have write permissions for this directory.         |
+-----------------------------------------------+---------------------------------------------------------------------+

Enable webhook debugging
~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------+------------------------------------------------------------------------------+
| Configure Mattermost to capture the contents  | - System Config path: **Environment > Logging**                              |
| of incoming webhooks to log files for         | - ``config.json setting``: ``".LogSettings.EnableWebhookDebugging": true",`` |
| debugging.                                    | - Environment variable: ``MM_LOGSETTINGS_ENABLEWEBHOOKDEBUGGING``            |
|                                               |                                                                              |
| - **true**: **(Default)** The contents of     |                                                                              |
|   incoming webhooks are printed to log files  |                                                                              |
|   for debugging.                              |                                                                              |     
| - **false**: The contents of incoming         |                                                                              |
|   webhooks aren’t printed to log files.       |                                                                              |
+-----------------------------------------------+------------------------------------------------------------------------------+

Enable diagnostics and error reporting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------+---------------------------------------------------------------------------+
| Configure Mattermost to allow any combination | - System Config path: **Environment > Logging**                           |
| of console, local file, syslog, and TCP       | - ``config.json setting``: ``".LogSettings.AdvancedLoggingConfig": "",``  |
| socket targets, and send log records to       | - Environment variable: ``MM_LOGSETTINGS_ADVANCEDLOGGINGCONFIG``          |
| multiple targets.                             |                                                                           |
|                                               |                                                                           |
+-----------------------------------------------+---------------------------------------------------------------------------+

Output logs to multiple targets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------+---------------------------------------------------------------------------+
| Configure Mattermost to allow any combination | - System Config path: **Environment > Logging**                           |
| of console, local file, syslog, and TCP       | - ``config.json setting``: ``".LogSettings.AdvancedLoggingConfig": "",``  |
| socket targets, and send log records to       | - Environment variable: ``MM_LOGSETTINGS_ADVANCEDLOGGINGCONFIG``          |
| multiple targets.                             |                                                                           |
|                                               |                                                                           |
| String input can contain a filespec to        |                                                                           |
| another configuration file, a database DSN,   |                                                                           |
| or JSON.                                      |                                                                           |
+-----------------------------------------------+---------------------------------------------------------------------------+
| **Notes**:                                                                                                                |
|                                                                                                                           |
| - These targets have been chosen as they support the vast majority of log aggregators, and other log analysis tools,      |
|   without needing additional software installed.                                                                          |
| - Logs are recorded asynchronously to reduce latency to the caller.                                                       |
| - Advanced logging supports hot-reloading of logger configuration.                                                        |
+-----------------------------------------------+---------------------------------------------------------------------------+   
| See the :doc:`audit log v2 </comply/audit-log>` documentation for additional information.                                 |
+-----------------------------------------------+---------------------------------------------------------------------------+

Teammate name display
~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Control Teammate Name Display at the system level. 

**True**: Allows System Admins to control Teammate Name Display at the system level.

**False**: System Admins cannot control Teammate Name Display at the system level.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LockTeammateNameDisplay": []`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

Colorize plain text console logs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: When logged events are output to the console as plain text, colorize log levels details.

**False**: Plain text log details aren't colorized in the console.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableColor": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+
