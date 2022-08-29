Compliance configuration settings
=================================

Access the following configuration settings in the System Console by going to **Compliance**:

- `Data Retention Policies <#data-retention-policies>`__
- `Compliance Export <#compliance-export>`__
- `Compliance Monitoring <#compliance-monitoring>`__
- `Custom Terms of Service <#custom-terms-of-service>`__

Data Retention Policies
~~~~~~~~~~~~~~~~~~~~~~~

Changes to properties in this section require a server restart before taking effect.

.. warning:: 
   Once a message or a file is deleted, the action is irreversible. Please be careful when setting up a custom data retention policy.

Access the following configuration settings in the System Console by going to **Compliance > Data Retention Policies**.

Global Retention Policy for Messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available in legacy Enterprise Edition E20*

Set how long Mattermost keeps messages across all teams and channels. Doesn't apply to custom retention policies. Requires the `global retention policy for messages <https://docs.mattermost.com/configure/configuration-settings.html#enable-global-retention-policy-for-messages>`__ configuration setting to be set to ``true``.

By default, messages are kept forever. If **Days** or **Years** is chosen, set how many days or years messages are kept in Mattermost. Messages older than the duration you set will be deleted nightly. The minimum time is one day.

+-------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MessageRetentionDays": 365`` with numerical input. |
+-------------------------------------------------------------------------------------------------+

Global Retention Policy for Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available in legacy Enterprise Edition E20*

Set how long Mattermost keeps files across all teams and channels. Doesn't apply to custom retention policies. Requires the `global retention policy for files <https://docs.mattermost.com/configure/configuration-settings.html#enable-global-retention-policy-for-files>`__ configuration setting to be set to ``true``.

By default, messages are kept forever. If **Days** or **Years** is chosen, set how many days or years files are kept in Mattermost. Files older than the duration you set will be deleted nightly. The minimum time is one day.

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileRetentionDays": 365`` with numerical input. |
+----------------------------------------------------------------------------------------------+

Custom retention policy
^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available in legacy Enterprise Edition E20*

Set how long Mattermost keeps messages and files across specific teams and channels by specifying a name for the custom retention policy, setting a duration value, specifying the teams and channels that will follow this policy.

Data Deletion Time
^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available in legacy Enterprise Edition E20*

Set the start time of the daily scheduled data retention job. Choose a time when fewer people are using your system. Must be a 24-hour time stamp in the form ``HH:MM``.

This setting is based on the local time of the server.

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DeletionJobStartTime": "02:00"`` with 24-hour timestamp input in the form ``"HH:MM"``. |
+-------------------------------------------------------------------------------------------------------------------------------------+

Run Deletion Job Now
^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available in legacy Enterprise Edition E20*

Start a Data Retention deletion job immediately. You can monitor the status of the job in the data deletion job table within the Policy Log section.

Compliance Export
~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Compliance > Compliance Export**.

Enable Compliance Export
^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available as an add-on to legacy Enterprise Edition E20*

**True**: Mattermost will generate a compliance export file that contains all messages that were posted in the last 24 hours. The export task is scheduled to run once per day. See the `documentation to learn more <https://docs.mattermost.com/comply/compliance-export.html>`__.

**False**: Mattermost doesn't generate a compliance export file.

+----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableExport": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------+

Compliance Export Time
^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available as an add-on to legacy Enterprise Edition E20*

Set the start time of the daily scheduled compliance export job. Choose a time when fewer people are using your system. Must be a 24-hour time stamp in the form ``HH:MM``.

This setting is based on the local time of the server.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DailyRunTime": 01:00`` with 24-hour timestamp input in the form ``"HH:MM"``. |
+---------------------------------------------------------------------------------------------------------------------------+

Export File Format
^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available as an add-on to legacy Enterprise Edition E20*

File format of the compliance export. Corresponds to the system that you want to import the data into.

Currently supported formats are CSV, Actiance XML, and Global Relay EML.

If Global Relay is chosen, the following options will be presented:

Global Relay Customer Account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available as an add-on to legacy Enterprise Edition E20*

Type of Global Relay customer account your organization has, either ``A9/Type 9`` or ``A10/Type 10``.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CustomerType": "A9/Type 9"`` with options ``"A9/Type 9"`` and ``"A10/Type 10"``. |
+-------------------------------------------------------------------------------------------------------------------------------+

Global Relay SMTP Username
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available as an add-on to legacy Enterprise Edition E20*

The username for authenticating to the Global Relay SMTP server.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SmtpUsername": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Global Relay SMTP Password
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available as an add-on to legacy Enterprise Edition E20*

The password associated with the Global Relay SMTP username.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SmtpPassword": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Global Relay Email Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available as an add-on to legacy Enterprise Edition E20*

The email address your Global Relay server monitors for incoming compliance exports.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EmailAddress": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Run Compliance Export Job Now
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available as an add-on to legacy Enterprise Edition E20*

This button initiates a compliance export job immediately. You can monitor the status of the job in the compliance export job table.

Compliance Monitoring
~~~~~~~~~~~~~~~~~~~~~~

Settings used to enable and configure Mattermost compliance reports. 

Access the following configuration settings in the System Console by going to **Compliance > Compliance Monitoring**.

Enable Compliance Reporting
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available as an add-on to legacy Enterprise Edition E20*

**True**: Compliance reporting is enabled in Mattermost.

**False**: Compliance reporting is disabled.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Compliance Report Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available as an add-on to legacy Enterprise Edition E20*

Sets the directory where compliance reports are written.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Directory": "./data/"`` with string input. |
+-----------------------------------------------------------------------------------------+

Enable Daily Report
^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available as an add-on to legacy Enterprise Edition E20*

**True**: Mattermost generates a daily compliance report.

**False**: Daily reports are not generated.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableDaily": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+

Batch Size
^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available as an add-on to legacy Enterprise Edition E20*

Set the size of the batches in which posts will be read from the database to generate the compliance report. This setting is currently not available in the System Console and can only be set in ``config.json``.

+------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BatchSize": 30000`` with default value ``30000``. |
+------------------------------------------------------------------------------------------------+

Custom Terms of Service
~~~~~~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Compliance > Custom Terms of Service**.

Enable Custom Terms of Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available as an add-on to legacy Enterprise Edition E20*

.. note::
  This configuration setting can only be modified using the System Console user interface.

**True**: New users must accept the Terms of Service before accessing any Mattermost teams on desktop, web, or mobile. Existing users must accept them after login or a page refresh. To update the Terms of Service link displayed in account creation and login pages, go to **System Console > Legal and Support > Terms of Service Link**.

**False**: During account creation or login, users can review Terms of Service by accessing the link configured via **System Console > Legal and Support > Terms of Service link**.

Custom Terms of Service Text
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available as an add-on to legacy Enterprise Edition E20*

Text that will appear in your custom Terms of Service. Supports Markdown-formatted text.

Re-Acceptance Period
^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

*Available as an add-on to legacy Enterprise Edition E20*

The number of days before Terms of Service acceptance expires, and the terms must be re-accepted.

Defaults to 365 days. 0 indicates the terms do not expire.