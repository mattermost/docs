Compliance configuration settings
=================================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Review and manage the following compliance configuration options in the System Console by selecting the **Product** |product-list| menu, selecting **System Console**, and then selecting **Compliance**:

- `Data Retention Policies <#data-retention-policies>`__
- `Compliance Export <#compliance-export>`__
- `Compliance Monitoring <#compliance-monitoring>`__
- `Custom Terms of Service <#custom-terms-of-service>`__

.. tip::

  System admins managing a self-hosted Mattermost deployment can edit the ``config.json`` file as described in the following tables. Each configuration value below includes a JSON path to access the value programmatically in the ``config.json`` file using a JSON-aware tool. For example, the ``MessageRetentionHours`` value is under ``DataRetentionSettings``.

  - If using a tool such as `jq <https://stedolan.github.io/jq/>`__, you'd enter: ``cat config/config.json | jq '.DataRetentionSettings.MessageRetentionHours'``
  - When working with the ``config.json`` file manually, look for an object such as ``DataRetentionSettings``, then within that object, find the key ``MessageRetentionHours``.

----

Data retention policies
-----------------------

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Changes to properties in this section require a server restart before taking effect.

.. warning::

  - Once a message or a file is deleted, the action is irreversible. Please set up a custom data retention policy with care.
  - From Mattermost v9.5, data retention removes Elasticsearch indexes based on the day of the retention cut-off time.

Access the following configuration settings in the System Console by going to **Compliance > Data Retention Policies**.

.. config:setting:: global-retention-policy-for-messages
  :displayname: Global retention policy for messages (Data Retention)
  :systemconsole: Compliance > Data Retention Policies
  :configjson: .DataRetentionSettings.MessageRetentionHours
  :environment: MM_DATARETENTIONSETTINGS_MESSAGERETENTIONHOURS
  :description: Set how long Mattermost keeps messages across all teams and channels. Doesn't apply to custom retention policies. Default is **O** and the minimum time is 1 hour.

Global retention policy for messages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Set how long Mattermost keeps messages across all teams and    | - System Config path: **Compliance > Data Retention Policies**                           |
| channels. This setting doesn't apply to custom retention       | - ``config.json`` setting: ``DataRetentionSettings`` > ``MessageRetentionHours`` > ``0`` |
| policies.                                                      | - Environment variable: ``MM_DATARETENTIONSETTINGS_MESSAGERETENTIONHOURS``               |
|                                                                |                                                                                          |
| By default, messages are kept forever. If **Hours**, **Days**, |                                                                                          |
| or **Years** is chosen, set how many hours, days, or years     |                                                                                          |
| messages are kept in Mattermost. Messages older than the       |                                                                                          |
| duration you set will be deleted nightly.                      |                                                                                          |
|                                                                |                                                                                          |
| The default  is **0** (messages are kept forever).             |                                                                                          |
| The minimum message retention is 1 hour.                       |                                                                                          |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------+

.. note::

  From Mattermost v9.5, ``MessageRetentionDays`` has been deprecated in favor of ``MessageRetentionHours``. See :ref:`deprecated configuration settings <configure/deprecated-configuration-settings:Message Retention (Days)>` for details.

.. config:setting:: global-retention-policy-for-files
  :displayname: Global retention policy for files (Data Retention)
  :systemconsole: Compliance > Data Retention Policies
  :configjson: .DataRetentionSettings.FileRetentionHours
  :environment: MM_DATARETENTIONSETTINGS_FILERETENTIONHOURS
  :description: Set how long Mattermost keeps files across all teams and channels. Doesn't apply to custom retention policies. Default is **0** and the minimum time is 1 hour.

Global retention policy for files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Set how long Mattermost keeps files across all teams and      | - System Config path: **Compliance > Data Retention Policies**                        |
| channels. This setting doesn't apply to custom retention      | - ``config.json`` setting: ``DataRetentionSettings`` > ``FileRetentionHours`` > ``0`` |
| policies.                                                     | - Environment variable: ``MM_DATARETENTIONSETTINGS_FILERETENTIONHOURS``               |
|                                                               |                                                                                       |
| By default, files are kept forever. If **Hours**, **Days**,   |                                                                                       |
| or **Years** is chosen, set how many hours, days, or years    |                                                                                       |
| files are kept in Mattermost. Files older than the duration   |                                                                                       |
| you set will be deleted nightly.                              |                                                                                       |
|                                                               |                                                                                       |
| The default is **0** (files kept forever).                    |                                                                                       |
| The minimum file retention time is 1 hour.                    |                                                                                       |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------+

.. note::

  From Mattermost v9.5, ``FileRetentionDays`` has been deprecated in favor of ``FileRetentionHours``. See :ref:`deprecated configuration settings <configure/deprecated-configuration-settings:File Retention (Days)>` for details.

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

  - This global configuration setting must be enabled with mmctl using the :ref:`mmctl config set <manage/mmctl-command-line-tool:mmctl config set>` command.
  - This configuration setting applies to team and channel policies as well as data retention, and can't be overridden in those more granular team or channel policies.
  - Files attached to the pinned message aren't preserved.
  - Only the pinned post is preserved. If it's attached to a thread or if it's the root post of a thread, the other threaded messages aren't preserved.

.. config:setting:: custom-retention-policy
  :displayname: Custom retention policy (Data Retention)
  :systemconsole: Compliance > Data Retention Policies
  :configjson: N/A
  :environment: N/A
  :description: Define a custom retention policy to override the global retention policy for messages and files. Custom policies can be set for specific teams, channels, or users.

Custom retention policy
~~~~~~~~~~~~~~~~~~~~~~~

Select **Add Policy** to define a custom retention policy. See the :doc:`custom data retention policy </comply/data-retention-policy>` documentation for details.

.. config:setting:: data-deletion-time
  :displayname: Data deletion time (Data Retention)
  :systemconsole: Compliance > Data Retention Policies
  :configjson: .DataRetentionSettings.DeletionJobStartTime
  :environment: MM_DATARETENTIONSETTINGS_DELETIONJOBSTARTTIME
  :description: Set the start time of the daily scheduled data retention job. Must be a 24-hour time stamp in the form ``HH:MM``. Default is **02:00** and this setting is based on the local time of the server.

Data deletion time
~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Set the start time of the daily scheduled data retention job. | - System Config path: **Compliance > Data Retention Policies**                                |
| Choose a time when fewer people are using your system. Must   | - ``config.json`` setting: ``DataRetentionSettings`` > ``DeletionJobStartTime`` > ``"02:00"`` |
| be a 24-hour time stamp in the form ``HH:MM``.                | - Environment variable: ``MM_DATARETENTIONSETTINGS_DELETIONJOBSTARTTIME``                     |
|                                                               |                                                                                               |
| This setting is based on the local time of the server.        |                                                                                               |
|                                                               |                                                                                               |
| Default is **02:00**.                                         |                                                                                               |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------+

.. config:setting:: run-deletion-job-now
  :displayname: Run deletion job now (Data Retention)
  :systemconsole: Compliance > Data Retention Policies
  :configjson: N/A
  :environment: N/A
  :description: Start a data retention deletion job immediately. Monitor the status of the job in the data deletion job table within the Policy Log section. 

Run deletion job now
~~~~~~~~~~~~~~~~~~~~~

Select **Run Deletion Job Now** to start a Data Retention deletion job immediately. Monitor the status of the job in the data deletion job table within the Policy Log section.

----

Compliance export
-----------------

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Compliance > Compliance Export**.

.. config:setting:: enable-compliance-export
  :displayname: Enable compliance export (Compliance Export)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.EnableExport
  :environment: MM_MESSAGEEXPORTSETTINGS_ENABLEEXPORT

  - **true**: Mattermost will generate a compliance export file that contains all messages that were posted in the last 24 hours.
  - **false**: **(Default)** Mattermost doesn't generate a compliance export file.

Enable compliance export
~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-------------------------------------------------------------------------------------+
| - **True**: Mattermost will generate a compliance export file   | - System Config path: **Compliance > Compliance Export**                            |
|   that contains all messages that were posted in the last 24    | - ``config.json`` setting: ``MessageExportSettings`` > ``EnableExport`` > ``false`` |
|   hours. The export task is scheduled to run once per day.      | - Environment variable: ``MM_MESSAGEEXPORTSETTINGS_ENABLEEXPORT``                   |
|   See the :doc:`compliance export documentation                 |                                                                                     |
|   </comply/compliance-export>`  to learn more.                  |                                                                                     |
|                                                                 |                                                                                     |
| - **False**: **(Default)** Mattermost doesn't generate a        |                                                                                     |
|   compliance export file.                                       |                                                                                     |
+-----------------------------------------------------------------+-------------------------------------------------------------------------------------+

.. config:setting:: compliance-export-time
  :displayname: Compliance export time (Compliance Export)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.DailyRunTime
  :environment: MM_MESSAGEEXPORTSETTINGS_DAILYRUNTIME
  :description: Set the start time of the daily scheduled compliance export job. Must be a 24-hour time stamp in the form ``HH:MM``. Default is **01:00** and this setting is based on the local time of the server.

Compliance export time
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Set the start time of the daily scheduled compliance export   | - System Config path: **Compliance > Compliance Export**                              |
| job. Choose a time when fewer people are using your system.   | - ``config.json`` setting: ``MessageExportSettings`` > ``DailyRunTime`` > ``"01:00"`` |
| Must be a 24-hour time stamp in the form ``HH:MM``.           | - Environment variable: ``MM_MESSAGEEXPORTSETTINGS_DAILYRUNTIME``                     |
|                                                               |                                                                                       |
| This setting is based on the local time of the server.        |                                                                                       |
|                                                               |                                                                                       |
| Default is **01:00**.                                         |                                                                                       |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------+

.. config:setting:: export-file-format
  :displayname: Export file format (Compliance Export)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.ExportFormat
  :environment: MM_MESSAGEEXPORTSETTINGS_EXPORTFORMAT
  :description: File format of the compliance export. Currently supported formats are CSV, Actiance XML, and Global Relay EML.

Export file format
~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-------------------------------------------------------------------------------------+
| File format of the compliance export. Corresponds to the      | - System Config path: **Compliance > Compliance Export**                            |
| system that you want to import the data into.                 | - ``config.json`` setting: ``MessageExportSettings`` > ``ExportFormat`` > ``"csv"`` |
|                                                               | - Environment variable: ``MM_MESSAGEEXPORTSETTINGS_EXPORTFORMAT``                   |
| Currently supported formats are **CSV**, **Actiance XML**,    |                                                                                     |
| and **Global Relay EML**.                                     |                                                                                     |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------+

.. config:setting:: global-relay-customer-account
  :displayname: Global Relay customer account (Compliance Export - Global Relay EML)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.GlobalRelaySettings.CustomerType
  :environment: MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_CUSTOMERTYPE
  :description: Type of Global Relay customer account your organization has. Can be ``A9/Type 9``, ``A10/Type 10``, or ``Custom``.

Global Relay customer account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| Type of Global Relay customer account your organization has.  | - System Config path: **Compliance > Compliance Export**                                                     |
| Can be one of: **A9/Type 9**, **A10/Type 10**, or **Custom**. | - ``config.json`` setting: ``MessageExportSettings`` > ``GlobalRelaySettings`` > ``CustomerType`` > ``"A9"`` |
|                                                               | - Environment variable: ``MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_CUSTOMERTYPE``                        |
| Default is **A9**.                                            |                                                                                                              |
+---------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+

.. config:setting:: global-relay-smtp-username
  :displayname: Global Relay SMTP username (Compliance Export - Global Relay EML)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.GlobalRelaySettings.SmtpUsername
  :environment: MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_SMTPUSERNAME
  :description: The username for authenticating to the Global Relay SMTP server.

Global Relay SMTP username
~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| The username for authenticating to the Global Relay SMTP      | - System Config path: **Compliance > Compliance Export**                                                   |
| server.                                                       | - ``config.json`` setting: ``MessageExportSettings`` > ``GlobalRelaySettings`` > ``SmtpUsername`` > ``""`` |
|                                                               | - Environment variable: ``MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_SMTPUSERNAME``                      |
| String input. Default is an empty string.                     |                                                                                                            |
+---------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

.. config:setting:: global-relay-smtp-password
  :displayname: Global Relay SMTP password (Compliance Export - Global Relay EML)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.GlobalRelaySettings.SMTPPassword
  :environment: MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_SMTPPASSWORD
  :description: The password associated with the Global Relay SMTP username.

Global Relay SMTP password
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| The password associated with the Global Relay SMTP username.  | - System Config path: **Compliance > Compliance Export**                                                   |
|                                                               | - ``config.json`` setting: ``MessageExportSettings`` > ``GlobalRelaySettings`` > ``SMTPPassword`` > ``""`` |
| String input. Default is an empty string.                     | - Environment variable: ``MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_SMTPPASSWORD``                      |
+---------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

.. config:setting:: global-relay-email-address
  :displayname: Global Relay email address (Compliance Export - Global Relay EML)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.GlobalRelaySettings.EmailAddress
  :environment: MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_EMAILADDRESS
  :description: The email address your Global Relay server monitors for incoming compliance exports.

Global Relay email address
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| The email address your Global Relay server monitors for       | - System Config path: **Compliance > Compliance Export**                                                   |
| incoming compliance exports.                                  | - ``config.json`` setting: ``MessageExportSettings`` > ``GlobalRelaySettings`` > ``EmailAddress`` > ``""`` |
|                                                               | - Environment variable: ``MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_EMAILADDRESS``                      |
| String input. Default is an empty string.                     |                                                                                                            |
+---------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

.. config:setting:: smtp-server-name
  :displayname: SMTP server name (Compliance Export - Global Relay EML)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.GlobalRelaySettings.CustomSMTPServerName
  :environment: MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_CUSTOMSMTPSERVERNAME
  :description: The SMTP server name URL that will receive your Global Relay EML file when a custom customer account type is configured.

SMTP server name
~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| The SMTP server name URL that will receive your Global Relay       | - System Config path: **Compliance > Compliance Export**                                                           |
| EML file when a                                                    | - ``config.json`` setting: ``MessageExportSettings`` > ``GlobalRelaySettings`` > ``CustomSMTPServerName`` > ``""`` |
| `custom account type <#global-relay-customer-account>`__           | - Environment variable: ``MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_CUSTOMSMTPSERVERNAME``                      |
| is configured.                                                     |                                                                                                                    |
|                                                                    |                                                                                                                    |
| String input. Default is an empty string.                          |                                                                                                                    |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

.. config:setting:: smtp-server-port
  :displayname: SMTP server port (Compliance Export - Global Relay EML)
  :systemconsole: Compliance > Compliance Export
  :configjson: .MessageExportSettings.GlobalRelaySettings.CustomSMTPPort
  :environment: MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_CUSTOMSMPTPORT
  :description: The SMTP server port that will receive your Global Relay EML file when a custom customer account type is configured. Default is 25.

SMTP server port
~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| The SMTP server port that will receive your Global Relay EML        | - System Config path: **Compliance > Compliance Export**                                                     |
| file when a                                                         | - ``config.json`` setting: ``MessageExportSettings`` > ``GlobalRelaySettings`` > ``CustomSMTPPort`` > ``25`` |
| `custom account type <#global-relay-customer-account>`__            | - Environment variable: ``MM_MESSAGEEXPORTSETTINGS_GLOBALRELAYSETTINGS_CUSTOMSMPTPORT``                      |
| is configured.                                                      |                                                                                                              |
|                                                                     |                                                                                                              |
| Numerical input. Default is **25**.                                 |                                                                                                              |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+

.. config:setting:: message-export-batch-size
  :displayname: Message export batch size (Compliance Export)
  :systemconsole: N/A
  :configjson: .MessageExportSettings.BatchSize
  :environment: MM_MESSAGEEXPORTSETTINGS_BATCHSIZE
  :description: Determines how many new messages are batched together to a compliance export file. Default is **10000** messages.

Message export batch size
~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

+---------------------------------------------------------------+----------------------------------------------------------------------------------+
| Determines how many new messages are batched together to a    | - System Config path: N/A                                                        |
| compliance export file.                                       | - ``config.json`` setting: ``MessageExportSettings`` > ``BatchSize`` > ``10000`` |
|                                                               | - Environment variable: ``MM_MESSAGEEXPORTSETTINGS_BATCHSIZE``                   |
| Numerical input. Default is **10000** messages.               |                                                                                  |
+---------------------------------------------------------------+----------------------------------------------------------------------------------+

.. note::
  This setting isn't available in the System Console and can only be set in ``config.json``.

.. config:setting:: run-compliance-export-job-now
  :displayname: Run compliance export job now (Compliance Export)
  :systemconsole: Compliance > Compliance Export
  :configjson: N/A
  :environment: N/A
  :description: Start a compliance export job immediately. Monitor the status of the job in the compliance export job table. 

Run compliance export job now
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Select **Run Compliance Export Job Now** to start a compliance export job immediately. Monitor the status of the job in the compliance export job table.

----

Compliance monitoring
----------------------

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Settings to enable and configure Mattermost compliance reports. Access the following configuration settings in the System Console by going to **Compliance > Compliance Monitoring**.

.. config:setting:: enable-compliance-reporting
  :displayname: Enable compliance reporting (Compliance Monitoring)
  :systemconsole: Compliance > Compliance Monitoring
  :configjson: .ComplianceSettings.Enable
  :environment: MM_COMPLIANCESETTINGS_ENABLE

  - **true**: Compliance reporting is enabled in Mattermost.
  - **false**: **(Default)** Compliance reporting is disabled.

Enable compliance reporting
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| - **True**: Compliance reporting is enabled in Mattermost.      | - System Config path: **Compliance > Compliance Monitoring**               |
|                                                                 | - ``config.json`` setting: ``ComplianceSettings`` > ``Enable`` > ``false`` |
| - **False**: **(Default)** Compliance reporting is disabled.    | - Environment variable: ``MM_COMPLIANCESETTINGS_ENABLE``                   |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+

.. config:setting:: compliance-report-directory
  :displayname: Compliance report directory (Compliance Monitoring)
  :systemconsole: Compliance > Compliance Monitoring
  :configjson: .ComplianceSettings.Directory
  :environment: MM_COMPLIANCESETTINGS_DIRECTORY
  :description: Sets the directory where compliance reports are written. The default value is ``./data/``.

Compliance report directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------------+
| Sets the directory where compliance reports are written.      | - System Config path: **Compliance > Compliance Monitoring**                      |
|                                                               | - ``config.json`` setting: ``ComplianceSettings`` > ``Directory`` > ``"./data/"`` |
| String input. Default is **./data/**                          | - Environment variable: ``MM_COMPLIANCESETTINGS_DIRECTORY``                       |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------+

.. config:setting:: enable-compliance-reportingdaily
  :displayname: Enable daily report (Compliance Monitoring)
  :systemconsole: Compliance > Compliance Monitoring
  :configjson: .ComplianceSettings.EnableDaily
  :environment: MM_COMPLIANCESETTINGS_ENABLEDAILY

  - **true**: Mattermost generates a daily compliance report.
  - **false**: **(Default)** Daily reports aren't generated.

Enable daily report
~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+---------------------------------------------------------------------------------+
| - **True**: Mattermost generates a daily compliance report.     | - System Config path: **Compliance > Compliance Monitoring**                    |
|                                                                 | - ``config.json`` setting: ``ComplianceSettings`` > ``EnableDaily`` > ``false`` |
| - **False**: **(Default)** Daily reports aren't generated.      | - Environment variable: ``MM_COMPLIANCESETTINGS_ENABLEDAILY``                   |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------+

.. config:setting:: batch-size
  :displayname: Batch size (Compliance Monitoring)
  :systemconsole: Compliance > Compliance Monitoring
  :configjson: .ComplianceSettings.BatchSize
  :environment: MM_COMPLIANCESETTINGS_BATCHSIZE
  :description: Set the size of the batches in which messages will be read from the database to generate the compliance report. The default value is **30000**.

Batch size
~~~~~~~~~~

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| Set the size of the batches in which messages will be read    | - System Config path: **Compliance > Compliance Monitoring**                  |
| from the database to generate the compliance report.          | - ``config.json`` setting: ``ComplianceSettings`` > ``BatchSize`` > ``30000`` |
|                                                               | - Environment variable: ``MM_COMPLIANCESETTINGS_BATCHSIZE``                   |
| Numerical input. Default is **30000** messages.               |                                                                               |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

.. note::

  This setting isn't available in the System Console and can only be set in ``config.json``.

----

Custom terms of service
-----------------------

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

Access the following configuration settings in the System Console by going to **Compliance > Custom Terms of Service**.

.. config:setting:: enable-custom-terms-of-service
  :displayname: Enable custom terms of service (Custom Terms of Service)
  :systemconsole: Compliance > Custom Terms of Service
  :configjson: .SupportSettings.CustomTermsOfServiceEnabled
  :environment: MM_SUPPORTSETTINGS_CUSTOMTERMSOFSERVICEENABLED

  - **True**: New users must accept the Terms of Service before accessing any Mattermost teams on desktop, web, or mobile. Existing users must accept them after login or a page refresh.
  - **False**: **(Default)** During account creation or login, users can review Terms of Service by accessing the link configured via **System Console > Legal and Support > Terms of Service link**.

Enable custom terms of service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| - **True**: New users must accept the Terms of Service before     | - System Config path: **Compliance > Custom Terms of Service**                               |
|   accessing any Mattermost teams on desktop, web, or mobile.      | - ``config.json`` setting: ``SupportSettings`` > ``CustomTermsOfServiceEnabled`` > ``false`` |
|                                                                   | - Environment variable: ``MM_SUPPORTSETTINGS_CUSTOMTERMSOFSERVICEENABLED``                   |
| - **False**: **(Default)** During account creation or login,      |                                                                                              |
|   users can review Terms of Service by accessing the link         |                                                                                              |
|   configured via **System Console > Legal and Support >           |                                                                                              |
|   Terms of Service link**.                                        |                                                                                              |
+-------------------------------------------------------------------+----------------------------------------------------------------------------------------------+

.. note::

  - This configuration setting can only be managed using the System Console user interface. It can't be set in ``config.json`` or through environment variables.
  - When custom terms of service are enabled, users must accept the terms before they can access Mattermost teams after login or page refresh.
  - To update the Terms of Service link displayed in account creation and login pages, go to **System Console > Legal and Support > Terms of Service Link**.

.. config:setting:: custom-terms-of-service-text
  :displayname: Custom terms of service text (Custom Terms of Service)
  :systemconsole: Compliance > Custom Terms of Service
  :configjson: N/A
  :environment: N/A
  :description: Text that will appear in your custom Terms of Service. Supports Markdown-formatted text.

Custom terms of service text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Text that will appear in your custom Terms of Service.        | - System Config path: **Compliance > Custom Terms of Service**           |
| Supports Markdown-formatted text.                             | - ``config.json`` setting: N/A                                           |
|                                                               | - Environment variable: N/A                                              |
| Text input.                                                   |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: re-acceptance-period
  :displayname: Re-acceptance period (Custom Terms of Service)
  :systemconsole: Compliance > Custom Terms of Service
  :configjson: .SupportSettings.CustomTermsOfServiceReAcceptancePeriod
  :environment: MM_SUPPORTSETTINGS_CUSTOMTERMSOFSERVICEREACCEPTANCEPERIOD
  :description: The number of days before Terms of Service acceptance expires, and the terms must be re-accepted. The default value is **365**. A value of **0** indicates the terms do not expire.

Re-acceptance period
~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| The number of days before Terms of Service acceptance expires,  | - System Config path: **Compliance > Custom Terms of Service**                                        |
| and the terms must be re-accepted.                              | - ``config.json`` setting: ``SupportSettings`` > ``CustomTermsOfServiceReAcceptancePeriod`` > ``365`` |
|                                                                 | - Environment variable: ``MM_SUPPORTSETTINGS_CUSTOMTERMSOFSERVICEREACCEPTANCEPERIOD``                 |
| Numerical input. Default is **365** days, and **0** indicates   |                                                                                                       |
| that the terms don't expire.                                    |                                                                                                       |
+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
