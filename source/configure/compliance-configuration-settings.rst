Compliance configuration settings
=================================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Both self-hosted and Cloud admins can access the following configuration settings in **System Console > Compliance**. Self-hosted admins can also edit the ``config.json`` file as described in the following tables. 

- `Data Retention Policies <#data-retention-policies>`__
- `Compliance Export <#compliance-export>`__
- `Compliance Monitoring <#compliance-monitoring>`__
- `Custom Terms of Service <#custom-terms-of-service>`__

----

Data retention policies
-----------------------

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Changes to properties in this section require a server restart before taking effect.

.. warning::

  - Once a message or a file is deleted, the action is irreversible. Please be careful when setting up a custom data retention policy.
  - From Mattermost v9.5, data retention removes Elasticsearch indexes based on the day of the retention cut-off time.

Access the following configuration settings in the System Console by going to **Compliance > Data Retention Policies**.

.. config:setting:: dataretention-globalmessagepolicy
  :displayname: Global retention policy for messages (Data Retention)
  :systemconsole: Compliance > Data Retention Policies
  :configjson: .DataRetentionSettings.MessageRetentionDays
  :environment: MM_DATARETENTIONSETTINGS_MESSAGERETENTIONDAYS
  :description: Set how long Mattermost keeps messages across all teams and channels. Doesn't apply to custom retention policies. The minimum time is 1 hour.

Global retention policy for messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

Set how long Mattermost keeps messages across all teams and channels. Doesn't apply to custom retention policies. Requires the `global retention policy for messages <https://docs.mattermost.com/configure/configuration-settings.html#enable-global-retention-policy-for-messages>`__ configuration setting to be set to ``true``.

By default, messages are kept forever. If **Hours**, **Days**, or **Years** is chosen, set how many hours, days, or years messages are kept in Mattermost. Messages older than the duration you set will be deleted nightly. The minimum message retention time is one hour.

+--------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MessageRetentionHours": 1`` or ``"MessageRetentionDays"`` with numerical input.   |
+--------------------------------------------------------------------------------------------------------------------------------+

.. note::

  From Mattermost v9.5, when a ``MessageRetentionHours`` value is configured, the ``MessageRetentionDays`` value must be 0 in the ``config.json`` file.  Conversely, when a ``MessageRetentionDays`` value is configured, the ``MessageRetentionHours`` value must be ``0``.

.. config:setting:: dataretention-globalfilepolicy
  :displayname: Global retention policy for files (Data Retention)
  :systemconsole: Compliance > Data Retention Policies
  :configjson: .DataRetentionSettings.FileRetentionDays
  :environment: MM_DATARETENTIONSETTINGS_FILERETENTIONDAYS
  :description: Set how long Mattermost keeps files across all teams and channels. Doesn't apply to custom retention policies. The minimum time is 1 hour.

Global retention policy for files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

Set how long Mattermost keeps files across all teams and channels. Doesn't apply to custom retention policies. Requires the `global retention policy for files <https://docs.mattermost.com/configure/configuration-settings.html#enable-global-retention-policy-for-files>`__ configuration setting to be set to ``true``.

By default, files are kept forever. If **Hours**, **Days**, or **Years** is chosen, set how many hours, days, or years files are kept in Mattermost. Files older than the duration you set will be deleted nightly. The minimum file retention time is one hour.

+--------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileRetentionHours": ``1`` or ``"FileRetentionDays"`` with numerical input. |
+--------------------------------------------------------------------------------------------------------------------------+

.. note::

  From Mattermost v9.5, when a ``FileRetentionHours`` value is configured, the ``FileRetentionDays`` value must be 0 in the ``config.json`` file.  Conversely, when a ``FileRetentionDays`` value is configured, the ``FileRetentionHours`` value must be ``0``.

.. config:setting:: dataretention-customretentionpolicy
  :displayname: Custom retention policy (Data Retention)
  :systemconsole: Compliance > Data Retention Policies
  :configjson: .DataRetentionSettings.DeletionJobStartTime
  :environment: MM_DATARETENTIONSETTINGS_DELETIONJOBSTARTTIME
  :description: Set the start time of the daily scheduled data retention job. Must be a 24-hour time stamp in the form ``HH:MM``. This setting is based on the local time of the server.

Custom retention policy
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

Set how long Mattermost keeps messages and files across specific teams and channels by specifying a name for the custom retention policy, setting a duration value in days or years, and specifying the teams and channels that will follow this policy.

.. config:setting:: dataretention-deletiontime
  :displayname: Data deletion time (Data Retention)
  :systemconsole: Compliance > Data Retention Policies
  :configjson: .DataRetentionSettings.DeletionJobStartTime
  :environment: MM_DATARETENTIONSETTINGS_DELETIONJOBSTARTTIME
  :description: Set the start time of the daily scheduled data retention job. Must be a 24-hour time stamp in the form ``HH:MM``. This setting is based on the local time of the server.

Data deletion time
~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

Set the start time of the daily scheduled data retention job. Choose a time when fewer people are using your system. Must be a 24-hour time stamp in the form ``HH:MM``.

This setting is based on the local time of the server.

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DeletionJobStartTime": "02:00"`` with 24-hour timestamp input in the form ``"HH:MM"``. |
+-------------------------------------------------------------------------------------------------------------------------------------+

Run deletion job now
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

Start a Data Retention deletion job immediately. You can monitor the status of the job in the data deletion job table within the Policy Log section.

----

Compliance export
-----------------

Access the following configuration settings in the System Console by going to **Compliance > Compliance Export**.

.. config:setting:: compliance-exportenable
  :displayname: Enable compliance export (Compliance Export)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.EnableExport
  :environment: MM_MESSAGEEXPORTSETTINGS_ENABLEEXPORT

  - **true**: Mattermost will generate a compliance export file that contains all messages that were posted in the last 24 hours.
  - **false**: **(Default)** Mattermost doesn't generate a compliance export file.

Enable compliance export
~~~~~~~~~~~~~~~~~~~~~~~~

*Available as an add-on to legacy Enterprise Edition E20*

**True**: Mattermost will generate a compliance export file that contains all messages that were posted in the last 24 hours. The export task is scheduled to run once per day. See the `documentation to learn more <https://docs.mattermost.com/comply/compliance-export.html>`__.

**False**: Mattermost doesn't generate a compliance export file.

+----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableExport": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------+

.. config:setting:: compliance-exporttime
  :displayname: Compliance export time (Compliance Export)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.DailyRunTime
  :environment: MM_MESSAGEEXPORTSETTINGS_DAILYRUNTIME
  :description: Set the start time of the daily scheduled compliance export job. Must be a 24-hour time stamp in the form ``HH:MM``. This setting is based on the local time of the server.

Compliance export time
~~~~~~~~~~~~~~~~~~~~~~~

*Available as an add-on to legacy Enterprise Edition E20*

Set the start time of the daily scheduled compliance export job. Choose a time when fewer people are using your system. Must be a 24-hour time stamp in the form ``HH:MM``.

This setting is based on the local time of the server.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DailyRunTime": 01:00`` with 24-hour timestamp input in the form ``"HH:MM"``. |
+---------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: compliance-exportformat
  :displayname: Export file format (Compliance Export)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.ExportFormat
  :environment: MM_MESSAGEEXPORTSETTINGS_EXPORTFORMAT
  :description: File format of the compliance export. Currently supported formats are CSV, Actiance XML, and Global Relay EML.

Export file format
~~~~~~~~~~~~~~~~~~~

*Available as an add-on to legacy Enterprise Edition E20*

File format of the compliance export. Corresponds to the system that you want to import the data into.

Currently supported formats are CSV, Actiance XML, and Global Relay EML.

If Global Relay is chosen, the following options will be presented:

.. config:setting:: compliance-exportglobalrelaycustomertype
  :displayname: Global Relay customer account (Compliance Export - Global Relay EML)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.GlobalRelaySettings.CustomerType
  :environment: MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_CUSTOMERTYPE
  :description: Type of Global Relay customer account your organization has. Can be ``A9/Type 9``, ``A10/Type 10``, or ``Custom``.

Global Relay customer account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available as an add-on to legacy Enterprise Edition E20*

Type of Global Relay customer account your organization has. Can be one of: ``A9/Type 9``, ``A10/Type 10``, or ``Custom``.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CustomerType": "A9"`` with options ``"A9``, ``"A10"``, and ``CUSTOM``. |
+---------------------------------------------------------------------------------------------------------------------+

.. config:setting:: compliance-exportglobalrelaysmtpuser
  :displayname: Global Relay SMTP username (Compliance Export - Global Relay EML)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.GlobalRelaySettings.SmtpUsername
  :environment: MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_SMTPUSERNAME
  :description: The username for authenticating to the Global Relay SMTP server.

Global Relay SMTP username
~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available as an add-on to legacy Enterprise Edition E20*

The username for authenticating to the Global Relay SMTP server.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SmtpUsername": ""`` with string input. |
+-------------------------------------------------------------------------------------+

.. config:setting:: compliance-exportglobalrelaysmtppassword
  :displayname: Global Relay SMTP password (Compliance Export - Global Relay EML)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.GlobalRelaySettings.SMTPPassword
  :environment: MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_SMTPPASSWORD
  :description: The password associated with the Global Relay SMTP username.

Global Relay SMTP password
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available as an add-on to legacy Enterprise Edition E20*

The password associated with the Global Relay SMTP username.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SmtpPassword": ""`` with string input. |
+-------------------------------------------------------------------------------------+

.. config:setting:: compliance-exportglobalrelayemail
  :displayname: Global Relay email address (Compliance Export - Global Relay EML)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.GlobalRelaySettings.EmailAddress
  :environment: MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_EMAILADDRESS
  :description: The email address your Global Relay server monitors for incoming compliance exports.

Global Relay email address
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available as an add-on to legacy Enterprise Edition E20*

The email address your Global Relay server monitors for incoming compliance exports.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EmailAddress": ""`` with string input. |
+-------------------------------------------------------------------------------------+

.. config:setting:: compliance-exportglobalrelaysmtpserver
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

.. config:setting:: compliance-exportglobalrelaysmtpport
  :displayname: SMTP server port (Compliance Export - Global Relay EML)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.GlobalRelaySettings.CustomSMTPPort
  :environment: MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_CUSTOMSMPTPORT
  :description: The SMTP server port that will receive your Global Relay EML file when a custom customer account type is configured. Default is 25.

SMTP server port
~~~~~~~~~~~~~~~~

The SMTP server port that will receive your Global Relay EML file when a `custom customer account type <#global-relay-customer-account>`__ is configured. Default is 25.

+----------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``".MessageExportSettings.GlobalRelaySettings.CustomSMTPPort": 25`` with string input. |
+----------------------------------------------------------------------------------------------------------------------------------+

Run compliance export job now
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available as an add-on to legacy Enterprise Edition E20*

This button initiates a compliance export job immediately. You can monitor the status of the job in the compliance export job table.

----

Compliance monitoring
----------------------

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Settings used to enable and configure Mattermost compliance reports.

Access the following configuration settings in the System Console by going to **Compliance > Compliance Monitoring**.

.. config:setting:: compliance-monitorenable
  :displayname: Enable compliance reporting (Compliance Monitoring)
  :systemconsole: Compliance > Compliance Monitoring
  :configjson: .ComplianceSettings.Enable
  :environment: MM_COMPLIANCESETTINGS_ENABLE

  - **true**: Compliance reporting is enabled in Mattermost.
  - **false**: **(Default)** Compliance reporting is disabled.

Enable compliance reporting
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available as an add-on to legacy Enterprise Edition E20*

**True**: Compliance reporting is enabled in Mattermost.

**False**: Compliance reporting is disabled.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

.. config:setting:: compliance-monitordirectory
  :displayname: Compliance report directory (Compliance Monitoring)
  :systemconsole: Compliance > Compliance Monitoring
  :configjson: .ComplianceSettings.Directory
  :environment: MM_COMPLIANCESETTINGS_DIRECTORY
  :description: Sets the directory where compliance reports are written. The default value is ``./data/``.

Compliance report directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available as an add-on to legacy Enterprise Edition E20*

Sets the directory where compliance reports are written.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Directory": "./data/"`` with string input. |
+-----------------------------------------------------------------------------------------+

.. config:setting:: compliance-monitorenabledaily
  :displayname: Enable daily report (Compliance Monitoring)
  :systemconsole: Compliance > Compliance Monitoring
  :configjson: .ComplianceSettings.EnableDaily
  :environment: MM_COMPLIANCESETTINGS_ENABLEDAILY

  - **true**: Mattermost generates a daily compliance report.
  - **false**: **(Default)** Daily reports are not generated.

Enable daily report
~~~~~~~~~~~~~~~~~~~~

*Available as an add-on to legacy Enterprise Edition E20*

**True**: Mattermost generates a daily compliance report.

**False**: Daily reports are not generated.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableDaily": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+

.. config:setting:: compliance-monitorbatchsize
  :displayname: Batch size (Compliance Monitoring)
  :systemconsole: Compliance > Compliance Monitoring
  :configjson: .ComplianceSettings.BatchSize
  :environment: MM_COMPLIANCESETTINGS_BATCHSIZE
  :description: Set the size of the batches in which posts will be read from the database to generate the compliance report. The default value is **30000**.

Batch size
~~~~~~~~~~

*Available as an add-on to legacy Enterprise Edition E20*

Set the size of the batches in which posts will be read from the database to generate the compliance report. This setting is currently not available in the System Console and can only be set in ``config.json``.

+------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BatchSize": 30000`` with default value ``30000``. |
+------------------------------------------------------------------------------------------------+

----

Custom terms of service
-----------------------

Access the following configuration settings in the System Console by going to **Compliance > Custom Terms of Service**.

.. config:setting:: compliance-ctosenable
  :displayname: Enable custom terms of service (Custom Terms of Service)
  :systemconsole: Compliance > Custom Terms of Service
  :configjson: .SupportSettings.CustomTermsOfServiceEnabled
  :environment: MM_SUPPORTSETTINGS_CUSTOMTERMSOFSERVICEENABLED

  - **True**: New users must accept the Terms of Service before accessing any Mattermost teams on desktop, web, or mobile. Existing users must accept them after login or a page refresh.
  - **False**: During account creation or login, users can review Terms of Service by accessing the link configured via **System Console > Legal and Support > Terms of Service link**.

Enable custom terms of service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available as an add-on to legacy Enterprise Edition E20*

.. note::
  This configuration setting can only be modified using the System Console user interface.

**True**: New users must accept the Terms of Service before accessing any Mattermost teams on desktop, web, or mobile. Existing users must accept them after login or a page refresh. To update the Terms of Service link displayed in account creation and login pages, go to **System Console > Legal and Support > Terms of Service Link**.

**False**: During account creation or login, users can review Terms of Service by accessing the link configured via **System Console > Legal and Support > Terms of Service link**.

.. config:setting:: compliance-ctostext
  :displayname: Custom terms of service text (Custom Terms of Service)
  :systemconsole: Compliance > Custom Terms of Service
  :configjson: N/A
  :environment: N/A
  :description: Text that will appear in your custom Terms of Service. Supports Markdown-formatted text.

Custom terms of service text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available as an add-on to legacy Enterprise Edition E20*

Text that will appear in your custom Terms of Service. Supports Markdown-formatted text.

.. config:setting:: compliance-ctosreacceptanceperiod
  :displayname: Re-acceptance period (Custom Terms of Service)
  :systemconsole: Compliance > Custom Terms of Service
  :configjson: .SupportSettings.CustomTermsOfServiceReAcceptancePeriod
  :environment: MM_SUPPORTSETTINGS_CUSTOMTERMSOFSERVICEREACCEPTANCEPERIOD
  :description: The number of days before Terms of Service acceptance expires, and the terms must be re-accepted. The default value is **365**. A value of **0** indicates the terms do not expire.

Re-acceptance period
~~~~~~~~~~~~~~~~~~~~

*Available as an add-on to legacy Enterprise Edition E20*

The number of days before Terms of Service acceptance expires, and the terms must be re-accepted.

Defaults to 365 days. 0 indicates the terms do not expire.
