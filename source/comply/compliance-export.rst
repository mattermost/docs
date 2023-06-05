Compliance export
=================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

*Available in legacy Mattermost Enterprise Edition E20*

This feature enables compliance exports to be produced from the System Console, containing all messages including:

- Messages sent in direct message channels
- File uploads
- Posts from plugins
- Posts from bots/webhooks

The exports include information on channel member history at the time the message was posted. Entries for deleted messages and files are included in CSV and Actiance reports. The deleted content is included in the compliance export. Global Relay reports include file deletion entries but message deletion entries are excluded.

By default, Mattermost stores all message history providing an unlimited search history to admins and end users. In Mattermost Enterprise, you may set a `custom data retention policy </comply/data-retention-policy.html>`__ for how long messages and file uploads are kept in Mattermost channels and direct messages.

Enterprise deployments with a requirement to archive history beyond the data retention period can enable this add-on to export compliance reports to third-party systems. Integration with Actiance Vantage and Global Relay are currently supported, with integrations with other systems in the roadmap.

.. note::
  
   This feature replaces legacy Compliance Reporting Oversight functionality. We recommend migrating to the new system. For a sample CSV output of the new compliance export system, `download a CSV export file here <https://github.com/mattermost/docs/blob/master/source/samples/csv_export.zip>`__.
   
Set up guide
------------

Use the following guides to configure exports for CSV, Actiance XML, or Global Relay EML. \

For self-hosted deployments, compliance exports are written to the ``exports`` subdirectory of the configured `Local Storage directory </configure/configuration-settings.html>`__ in the chosen format. If you've configured Mattermost to use S3 storage, the exports are written to the ``exports`` directory in the Mattermost bucket.

.. note::
   
   The compliance exports do not contain posts sent before the feature was enabled. For self-hosted deployments, you can export past history via the ``export`` :doc:`command line tool <../manage/command-line-tools>`. 

CSV
~~~~

1. Go to **System Console > Compliance > Compliance Export**.
2. Set **Enable Compliance Exports** to **true**.
3. Set the **Compliance Export time**. This is the start time of the daily scheduled compliance export job and must be a 24-hour time stamp in the form HH:MM. Choose a time when fewer people are using your system.
4. Set the export file format to **CSV**.
5. Select **Save**.

The daily compliance export job creates a zip file with a unique job identifier of all messages posted in the last 24 hours. You can unzip the file to easily transform the default ``.csv`` format into a desired format for your third-party archive system.

For a sample CSV output, `download a CSV export file here <https://github.com/mattermost/docs/blob/master/source/samples/csv_export.zip>`__.

Actiance XML
~~~~~~~~~~~~

1. Go to **System Console > Compliance > Compliance Export**.
2. Set **Enable Compliance Exports** to **true**.  
3. Set the **Compliance Export time**. This is the start time of the daily scheduled compliance export job and must be a 24-hour time stamp in the form HH:MM. Choose a time when fewer people are using your system.
4. Set the export file format to **Actiance XML**.
5. Select **Save**.

The daily compliance export job creates a ``.zip`` file with a unique job identifier of all messages posted in the last 24 hours. Once you've selected Actiance XML as your file format, you can set up an integration with Actiance Vantage archive system. For more information, see `their homepage <https://www.actianceworks.com/Vantage.asp>`__. For a sample Actiance output, `download an Actiance XML export file here <https://github.com/mattermost/docs/blob/master/source/samples/actiance_export.xml>`__.

.. note::
  
   In Actiance XML exports, channel type is prepended to the channel names.

Global Relay EML
~~~~~~~~~~~~~~~~

1. Go to **System Console > Compliance > Compliance Export**.
2. Set **Enable Compliance Exports** to **true**.
3. Set the **Compliance Export time**. This is the start time of the daily scheduled compliance export job and must be a 24-hour time stamp in the form HH:MM. Choose a time when fewer people are using your system.
4. Set the export file format to **GlobalRelay EML**.
5. Select `A9/Type 9` or `A10/Type 10` for the **Global Relay Customer Account**. This is the type of Global Relay customer account your organization has.
6. Set the **Global Relay SMTP username**, **Global Relay SMTP password**, and **Global Relay SMTP email address**, provided by Global Relay.
7. Select **Save**.

Once you've selected Global Relay EML as your file format, you can set up an integration with Global Relay archive system. For more information, see `Global Relay Archive <https://www.globalrelay.com/gr-services/archive>`__.

.. note::
  
   Messages larger than 250 MB will have their attachments removed because they are too large to send to Global Relay. An error is added to the server logs with id ``global_relay_attachments_removed``. It includes the post ID the attachments were removed from, as well as the attachment IDs. A `ticket is queued to better handle large messages <https://mattermost.atlassian.net/browse/MM-10038>`__.

For more information on Global Relay archive system, see `their homepage <https://www.globalrelay.com/>`__.

Frequently Asked Questions (FAQ)
--------------------------------

How do I export past history?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the ``export`` :doc:`command line tool <../manage/command-line-tools>`. You can specify an ``exportFrom`` option to export data from a specified timestamp. All posts that were made after this timestamp will be exported.

What happens if I export data manually?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the compliance export job is run automatically, manually via the System Console, or manually via the CLI (without the ``--exportFrom`` option), it exports all posts that were made since the last post that the previous execution of the job exported. If this is the first time that the job has ever run, all posts that were made since the feature was enabled will be exported.

If the ``--exportFrom`` option is specified with the CLI command, all posts that have been made since the supplied timestamp will be exported.

When run manually via the System Console, ``.csv`` and Actiance XML files are written to the ``exports`` subdirectory of the configured `Local Storage Directory </configure/configuration-settings.html#local-storage-directory>`__.  Files will be written to a folder with names based on an epoch time range. Global Relay EML export format files will be mailed to the configured email address when run manually.

Is there a maximum row limit for CSV files?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. There's no limit to the number of rows within Compliance Monitoring CSV files.

How do I know if a compliance export job fails?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost provides the status of each compliance export job in **System Console > Compliance > Compliance Export**. Here, you can see if the job succeeded or failed, including the number of messages and files exported.

In addition, any failures are returned in the server logs for self-hosted deployments. The error log begins with the string ``Failed job`` and includes a ``job_id key/value`` pair. Compliance export job failures are identified with worker name ``MessageExportWorker``. You can optionally create a script that programmatically queries for such failures and notifies the appropriate system.
