Compliance configuration settings
=================================

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

Review and manage the following compliance configuration options in the System Console by selecting the **Product** |product-list| menu, selecting **System Console**, and then selecting **Compliance**:

- `Data Retention Policies <#data-retention-policies>`__
- `Compliance Export <#administration-guide/comply/compliance-export>`__
- `Compliance Monitoring <#compliance-monitoring>`__
- `Custom Terms of Service <#custom-terms-of-service>`__

.. tip::

  System admins managing a self-hosted Mattermost deployment can edit the ``config.json`` file as described in the following tables. Each configuration value below includes a JSON path to access the value programmatically in the ``config.json`` file using a JSON-aware tool. For example, the ``MessageRetentionHours`` value is under ``DataRetentionSettings``.

  - If using a tool such as `jq <https://stedolan.github.io/jq/>`__, you'd enter: ``cat config/config.json | jq '.DataRetentionSettings.MessageRetentionHours'``
  - When working with the ``config.json`` file manually, look for an object such as ``DataRetentionSettings``, then within that object, find the key ``MessageRetentionHours``.

----

Data retention policies
-----------------------

Changes to properties in this section require a server restart before taking effect.

.. warning::

  - Once a message or a file is deleted, the action is irreversible. Please be careful when setting up a custom data retention policy.
  - From Mattermost v9.5, data retention removes Elasticsearch indexes based on the day of the retention cut-off time.

Access the following configuration settings in the System Console by going to **Compliance > Data Retention Policies**.

.. config:setting:: global-retention-policy-for-messages
  :displayname: Global retention policy for messages (Data Retention)
  :systemconsole: Compliance > Data Retention Policies
  :configjson: .DataRetentionSettings.MessageRetentionHours
  :environment: MM_DATARETENTIONSETTINGS_MESSAGERETENTIONHOURS
  :description: Set how long Mattermost keeps messages across all teams and channels. Doesn't apply to custom retention policies. The minimum time is 1 hour.

Global retention policy for messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set how long Mattermost keeps messages across all teams and channels. This value is not used for any teams and channels that have a custom retention policy applied . Requires the :ref:`global retention policy for messages <administration-guide/configure/compliance-configuration-settings:global retention policy for messages>` configuration setting to be set to ``true``.

By default, messages are kept forever. If **Hours**, **Days**, or **Years** is chosen, set how many hours, days, or years messages are kept in Mattermost. Messages older than the duration you set will be deleted nightly. The minimum message retention time is one hour.

The global retention time for messages can be superseded on a team or channel level by creating custom policies with unique post retention times See the `Custom retention policy <#custom-retention-policy>`__ section below for details. 

+--------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MessageRetentionHours": 1`` with numerical input.                           |
+--------------------------------------------------------------------------------------------------------------------------+

.. note::

  From Mattermost v9.5, ``MessageRetentionDays`` has been deprecated in favor of ``MessageRetentionHours``. See :doc:`deprecated configuration settings </administration-guide/configure/deprecated-configuration-settings>` for details.

.. config:setting:: global-retention-policy-for-files
  :displayname: Global retention policy for files (Data Retention)
  :systemconsole: Compliance > Data Retention Policies
  :configjson: .DataRetentionSettings.FileRetentionHours
  :environment: MM_DATARETENTIONSETTINGS_FILERETENTIONHOURS
  :description: Set how long Mattermost keeps files across all teams and channels. Doesn't apply to custom retention policies. The minimum time is 1 hour.

Global retention policy for files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set how long Mattermost keeps files across all teams and channels. Custom policies on team and channel level don't apply to file attachments. The global retention time for files will be used even if a custom policy for messages is in place. Requires the :ref:`global retention policy for files <administration-guide/configure/compliance-configuration-settings:global retention policy for files>` configuration setting to be set to ``true``.

By default, files are kept forever. If **Hours**, **Days**, or **Years** is chosen, set how many hours, days, or years files are kept in Mattermost. Files older than the duration you set will be deleted nightly. The minimum file retention time is one hour.

+--------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileRetentionHours": 1`` with numerical input.                              |
+--------------------------------------------------------------------------------------------------------------------------+

.. note::

  From Mattermost v9.5, ``FileRetentionDays`` has been deprecated in favor of ``FileRetentionHours``. See :doc:`deprecated configuration settings </administration-guide/configure/deprecated-configuration-settings>` for details.

.. config:setting:: preserve-pinned-posts
  :displayname: Preserve pinned posts (Data Retention)
  :systemconsole: Compliance > Data Retention Policies
  :configjson: .DataRetentionSettings.PreservePinnedPosts
  :environment: MM_DATARETENTIONSETTINGS_PRESERVEPINNEDPOSTS
  :description: Controls whether pinned posts are preserved when data retention policies delete messages.

Preserve pinned posts
~~~~~~~~~~~~~~~~~~~~~

From Mattermost v10.10, controls whether pinned posts are preserved when data retention policies delete messages. When enabled, pinned posts won't be deleted by data retention policies, even if they exceed the configured retention period.

**True**: Pinned posts are preserved and won't be deleted by data retention policies.

**False**: **(Default)** Pinned posts are deleted according to the configured data retention policy.

+---------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DataRetentionSettings.PreservePinnedPosts": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------------------------------+

.. note::

  - This global configuration setting must be enabled with mmctl using the :ref:`mmctl config set <administration-guide/manage/mmctl-command-line-tool:mmctl config set>` command.
  - This configuration setting applies to team and channel policies as well as data retention, and can't be overridden in those more granular team or channel policies.
  - Files attached to the pinned message aren't preserved.
  - Only the pinned post is preserved. If it's attached to a thread or if it's the root post of a thread, the other threaded messages aren't preserved.

.. config:setting:: custom-retention-policy
  :displayname: Custom retention policy (Data Retention)
  :systemconsole: Compliance > Data Retention Policies
  :configjson: .DataRetentionSettings.DeletionJobStartTime
  :environment: MM_DATARETENTIONSETTINGS_DELETIONJOBSTARTTIME
  :description: Set the start time of the daily scheduled data retention job. Must be a 24-hour time stamp in the form ``HH:MM``. This setting is based on the local time of the server.

Custom retention policy
~~~~~~~~~~~~~~~~~~~~~~~

Set how long Mattermost keeps messages across specific teams and channels by specifying a name for the custom retention policy, setting a duration value in days or years, and specifying the teams and channels that will follow this policy. The attachment retention time cannot be set on custom policy levels and the global retention time for attachments is always applied.

.. config:setting:: data-deletion-time
  :displayname: Data deletion time (Data Retention)
  :systemconsole: Compliance > Data Retention Policies
  :configjson: .DataRetentionSettings.DeletionJobStartTime
  :environment: MM_DATARETENTIONSETTINGS_DELETIONJOBSTARTTIME
  :description: Set the start time of the daily scheduled data retention job. Must be a 24-hour time stamp in the form ``HH:MM``. This setting is based on the local time of the server.

Data deletion time
~~~~~~~~~~~~~~~~~~

Set the start time of the daily scheduled data retention job. Choose a time when fewer people are using your system. Must be a 24-hour time stamp in the form ``HH:MM``.

This setting is based on the local time of the server.

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DeletionJobStartTime": "02:00"`` with 24-hour timestamp input in the form ``"HH:MM"``. |
+-------------------------------------------------------------------------------------------------------------------------------------+

Run deletion job now
~~~~~~~~~~~~~~~~~~~~~

Start a Data Retention deletion job immediately. You can monitor the status of the job in the data deletion job table within the Policy Log section.

----

Compliance export
-----------------

Access the following configuration settings in the System Console by going to **Compliance > Compliance Export**.

.. config:setting:: enable-administration-guide/comply/compliance-export
  :displayname: Enable compliance export (Compliance Export)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.EnableExport
  :environment: MM_MESSAGEEXPORTSETTINGS_ENABLEEXPORT

  - **true**: Mattermost will generate a compliance export file that contains all messages that were posted in the last 24 hours.
  - **false**: **(Default)** Mattermost doesn't generate a compliance export file.

Enable compliance export
~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Mattermost will generate a compliance export file that contains all messages that were posted in the last 24 hours. The export task is scheduled to run once per day. See the :doc:`documentation to learn more </administration-guide/comply/compliance-export>`.

**False**: Mattermost doesn't generate a compliance export file.

+----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableExport": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------+

.. config:setting:: administration-guide/comply/compliance-export-time
  :displayname: Compliance export time (Compliance Export)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.DailyRunTime
  :environment: MM_MESSAGEEXPORTSETTINGS_DAILYRUNTIME
  :description: Set the start time of the daily scheduled compliance export job. Must be a 24-hour time stamp in the form ``HH:MM``. This setting is based on the local time of the server.

Compliance export time
~~~~~~~~~~~~~~~~~~~~~~~

Set the start time of the daily scheduled compliance export job. Choose a time when fewer people are using your system. Must be a 24-hour time stamp in the form ``HH:MM``.

This setting is based on the local time of the server.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DailyRunTime": 01:00`` with 24-hour timestamp input in the form ``"HH:MM"``. |
+---------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: export-file-format
  :displayname: Export file format (Compliance Export)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.ExportFormat
  :environment: MM_MESSAGEEXPORTSETTINGS_EXPORTFORMAT
  :description: File format of the compliance export. Currently supported formats are CSV, Actiance XML, and Global Relay EML.

Export file format
~~~~~~~~~~~~~~~~~~~

File format of the compliance export. Corresponds to the system that you want to import the data into.

Currently supported formats are CSV, Actiance XML, and Global Relay EML.

If Global Relay is chosen, the following options will be presented:

.. config:setting:: global-relay-customer-account
  :displayname: Global Relay customer account (Compliance Export - Global Relay EML)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.GlobalRelaySettings.CustomerType
  :environment: MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_CUSTOMERTYPE
  :description: Type of Global Relay customer account your organization has. Can be ``A9/Type 9``, ``A10/Type 10``, or ``Custom``.

Global Relay customer account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Type of Global Relay customer account your organization has. Can be one of: ``A9/Type 9``, ``A10/Type 10``, or ``Custom``.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CustomerType": "A9"`` with options ``"A9``, ``"A10"``, and ``CUSTOM``. |
+---------------------------------------------------------------------------------------------------------------------+

.. config:setting:: global-relay-smtp-username
  :displayname: Global Relay SMTP username (Compliance Export - Global Relay EML)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.GlobalRelaySettings.SmtpUsername
  :environment: MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_SMTPUSERNAME
  :description: The username for authenticating to the Global Relay SMTP server.

Global Relay SMTP username
~~~~~~~~~~~~~~~~~~~~~~~~~~

The username for authenticating to the Global Relay SMTP server.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SmtpUsername": ""`` with string input. |
+-------------------------------------------------------------------------------------+

.. config:setting:: global-relay-smtp-password
  :displayname: Global Relay SMTP password (Compliance Export - Global Relay EML)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.GlobalRelaySettings.SMTPPassword
  :environment: MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_SMTPPASSWORD
  :description: The password associated with the Global Relay SMTP username.

Global Relay SMTP password
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The password associated with the Global Relay SMTP username.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SmtpPassword": ""`` with string input. |
+-------------------------------------------------------------------------------------+

.. config:setting:: global-relay-email-address
  :displayname: Global Relay email address (Compliance Export - Global Relay EML)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.GlobalRelaySettings.EmailAddress
  :environment: MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_EMAILADDRESS
  :description: The email address your Global Relay server monitors for incoming compliance exports.

Global Relay email address
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The email address your Global Relay server monitors for incoming compliance exports.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EmailAddress": ""`` with string input. |
+-------------------------------------------------------------------------------------+

.. config:setting:: smtp-server-name
  :displayname: SMTP server name (Compliance Export - Global Relay EML)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.GlobalRelaySettings.CustomSMTPServerName
  :environment: MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_CUSTOMSMTPSERVERNAME
  :description: The SMTP server name URL that will receive your Global Relay EML file when a custom customer account type is configured.

SMTP server name
~~~~~~~~~~~~~~~~

The SMTP server name URL that will receive your Global Relay EML file when a `custom customer account type <#global-relay-customer-account>`__ is configured.

+----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``".MessageExportSettings.GlobalRelaySettings.CustomSMTPServerName": ""`` with string input. |
+----------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: smtp-server-port
  :displayname: SMTP server port (Compliance Export - Global Relay EML)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.GlobalRelaySettings.CustomSMTPPort
  :environment: MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_CUSTOMSMPTPORT
  :description: The SMTP server port that will receive your Global Relay EML file when a custom customer account type is configured. Default is 25.

SMTP server port
~~~~~~~~~~~~~~~~

The SMTP server port that will receive your Global Relay EML file when a `custom customer account type <#global-relay-customer-account>`__ is configured. Default is ``"25"``.

+------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``".MessageExportSettings.GlobalRelaySettings.CustomSMTPPort": "25"`` with string input. |
+------------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: message-export-batch-size
  :displayname: Message export batch size (Compliance Export)
  :systemconsole: N/A
  :configjson: .MessageExportSettings.BatchSize
  :environment: MM_MESSAGEEXPORTSETTINGS_BATCHSIZE
  :description: Determines how many new posts are batched together to a compliance export file. Default is **10000** posts.

Message export batch size
~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

Determines how many new posts are batched together to a compliance export file.

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BatchSize": 10000`` with numerical input.      |
+---------------------------------------------------------------------------------------------+

Run compliance export job now
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This button initiates a compliance export job immediately. You can monitor the status of the job in the compliance export job table.

----

Compliance monitoring
----------------------

Settings used to enable and configure Mattermost compliance reports.

Access the following configuration settings in the System Console by going to **Compliance > Compliance Monitoring**.

.. config:setting:: enable-compliance-reporting
  :displayname: Enable compliance reporting (Compliance Monitoring)
  :systemconsole: Compliance > Compliance Monitoring
  :configjson: .ComplianceSettings.Enable
  :environment: MM_COMPLIANCESETTINGS_ENABLE

  - **true**: Compliance reporting is enabled in Mattermost.
  - **false**: **(Default)** Compliance reporting is disabled.

Enable compliance reporting
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**True**: Compliance reporting is enabled in Mattermost.

**False**: Compliance reporting is disabled.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

.. config:setting:: compliance-report-directory
  :displayname: Compliance report directory (Compliance Monitoring)
  :systemconsole: Compliance > Compliance Monitoring
  :configjson: .ComplianceSettings.Directory
  :environment: MM_COMPLIANCESETTINGS_DIRECTORY
  :description: Sets the directory where compliance reports are written. The default value is ``./data/``.

Compliance report directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sets the directory where compliance reports are written.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Directory": "./data/"`` with string input. |
+-----------------------------------------------------------------------------------------+

.. config:setting:: enable-compliance-reportingdaily
  :displayname: Enable daily report (Compliance Monitoring)
  :systemconsole: Compliance > Compliance Monitoring
  :configjson: .ComplianceSettings.EnableDaily
  :environment: MM_COMPLIANCESETTINGS_ENABLEDAILY

  - **true**: Mattermost generates a daily compliance report.
  - **false**: **(Default)** Daily reports are not generated.

Enable daily report
~~~~~~~~~~~~~~~~~~~~

**True**: Mattermost generates a daily compliance report.

**False**: Daily reports are not generated.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableDaily": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+

.. config:setting:: batch-size
  :displayname: Batch size (Compliance Monitoring)
  :systemconsole: Compliance > Compliance Monitoring
  :configjson: .ComplianceSettings.BatchSize
  :environment: MM_COMPLIANCESETTINGS_BATCHSIZE
  :description: Set the size of the batches in which posts will be read from the database to generate the compliance report. The default value is **30000**.

Batch size
~~~~~~~~~~

Set the size of the batches in which posts will be read from the database to generate the compliance report. This setting is currently not available in the System Console and can only be set in ``config.json``.

+------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BatchSize": 30000`` with default value ``30000``. |
+------------------------------------------------------------------------------------------------+

----

Custom terms of service
-----------------------

Access the following configuration settings in the System Console by going to **Compliance > Custom Terms of Service**.

.. config:setting:: enable-custom-terms-of-service
  :displayname: Enable custom terms of service (Custom Terms of Service)
  :systemconsole: Compliance > Custom Terms of Service
  :configjson: .SupportSettings.CustomTermsOfServiceEnabled
  :environment: MM_SUPPORTSETTINGS_CUSTOMTERMSOFSERVICEENABLED

  - **True**: New users must accept the Terms of Service before accessing any Mattermost teams on desktop, web, or mobile. Existing users must accept them after login or a page refresh.
  - **False**: During account creation or login, users can review Terms of Service by accessing the link configured via **System Console > Legal and Support > Terms of Service link**.

Enable custom terms of service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
  This configuration setting can only be modified using the System Console user interface.

**True**: New users must accept the Terms of Service before accessing any Mattermost teams on desktop, web, or mobile. Existing users must accept them after login or a page refresh. To update the Terms of Service link displayed in account creation and login pages, go to **System Console > Legal and Support > Terms of Service Link**.

**False**: During account creation or login, users can review Terms of Service by accessing the link configured via **System Console > Legal and Support > Terms of Service link**.

.. config:setting:: custom-terms-of-service-text
  :displayname: Custom terms of service text (Custom Terms of Service)
  :systemconsole: Compliance > Custom Terms of Service
  :configjson: N/A
  :environment: N/A
  :description: Text that will appear in your custom Terms of Service. Supports Markdown-formatted text.

Custom terms of service text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Text that will appear in your custom Terms of Service. Supports Markdown-formatted text.

.. config:setting:: re-acceptance-period
  :displayname: Re-acceptance period (Custom Terms of Service)
  :systemconsole: Compliance > Custom Terms of Service
  :configjson: .SupportSettings.CustomTermsOfServiceReAcceptancePeriod
  :environment: MM_SUPPORTSETTINGS_CUSTOMTERMSOFSERVICEREACCEPTANCEPERIOD
  :description: The number of days before Terms of Service acceptance expires, and the terms must be re-accepted. The default value is **365**. A value of **0** indicates the terms do not expire.

Re-acceptance period
~~~~~~~~~~~~~~~~~~~~

The number of days before Terms of Service acceptance expires, and the terms must be re-accepted.

Defaults to 365 days. 0 indicates the terms do not expire.
