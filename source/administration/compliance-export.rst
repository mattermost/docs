Compliance Export Beta (E20)
=====================================

Available in `Enterprise Edition E20 <https://about.mattermost.com/pricing/>`_.

This feature enables compliance exports to be produced from the System Console, containing all messages including those made in direct message channels, as well as file uploads. The exports also include information on channel member history at the time of the message was posted.

By default, Mattermost stores all message history providing an unlimited search history to admins and end users. In Enterprise Edition E20, you may set a `custom data retention policy <https://docs.mattermost.com/administration/data-retention.html>`_ for how long messages and file uploads are kept in Mattermost channels and direct messages.

Those Enterprise deployments who want to archive history beyond the data retention period can enable this add-on to export compliance reports to third-party systems. Integration with Actiance Vantage and Global Relay are currently supported, with integrations with other systems in the roadmap.

.. note::
  This feature will replace the existing :doc:`Compliance feature <compliance>` in a future release. Compliance exports to CSV will continue to be available in Enterprise Edition E20.

.. toctree::
    :maxdepth: 2

Set Up Guide
----------------------------

Use the following guides to configure exports for CSV, Actiance XML or Global Relay EML. Compliance exports are written to the ``exports`` subdirectory of the configured `Local Storage directory <https://docs.mattermost.com/administration/config-settings.html#storage>`_ in the chosen format.

.. note::
  The compliance exports do not contain posts sent before the feature was enabled, but you can export past history via the ``export`` :doc:`command line tool <command-line-tools>`. Posts made prior to upgrading to Mattermost v4.5 will have less accurate channel member history information.

CSV
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to **System Console > Advanced > Compliance Export (Beta)**.
2. Enable compliance exports, then set the start time of the daily scheduled compliance export job. Choose a time when fewer people are using your system. Must be a 24-hour time stamp in the form HH:MM.
3. Set the export file format to CSV.
4. Save the settings. You’re now all set!

You can use the CSV format to easily transform exports in a desired format for your third-party archive system.

For a sample CSV output, `download a CSV export file here <https://github.com/mattermost/docs/blob/master/source/samples/csv_export.zip>`_.

Actiance XML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to **System Console > Advanced > Compliance Export (Beta)**.
2. Enable compliance exports, then set the start time of the daily scheduled compliance export job. Choose a time when fewer people are using your system. Must be a 24-hour time stamp in the form HH:MM.
3. Set the export file format to Actiance XML.
4. Save the settings. You’re now all set!

If you have chosen your file format to be Actiance XML, you can set up an integration with Actiance Vantage archive system. For more information, see `their homepage <https://www.actiance.com/products/vantage/>`_.

For a sample Actiance outpout, `download an Actiance XML export file here <https://github.com/mattermost/docs/blob/master/source/samples/actiance_export.xml>`_.

.. note::
  In Actiance XML exports, channel type is prepended to the channel names.

Global Relay EML
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to **System Console > Advanced > Compliance Export (Beta)**.
2. Enable compliance exports, then set the start time of the daily scheduled compliance export job. Choose a time when fewer people are using your system. Must be a 24-hour time stamp in the form HH:MM.
3. Set the export file format to GlobalRelay EML.
4. Set the Global Relay Customer Account, either `A9/Type 9` or `A10/Type 10`. This is the type of Global Relay customer account your organization has.
5. Set the Global Relay SMTP username, password and email address as provided by Global Relay.
6. Save the settings. You’re now all set!

If you have chosen your file format to be Global Relay EML, you can set up an integration with Global Relay archive system. For more information, see `their homepage <https://www.globalrelay.com/gr-services/archive>`_.

.. note::
  Messages larger than 250MB will have their attachments removed because they are too large to send to Global Relay. An error is added to the server logs with id ``global_relay_attachments_removed``. It includes the post ID the attachments were removed from, as well as the attachment IDs. A `ticket is queued to better handle large messages <https://mattermost.atlassian.net/browse/MM-10038>`_.

For more information on Global Relay archive system, see `their homepage <https://www.globalrelay.com/>`_

Frequently Asked Questions (FAQ)
---------------------------------

How do I export past history?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the ``export`` :doc:`command line tool <command-line-tools>`. You can specify an `exportFrom` option to export data from a specified timestamp. All posts that were made after this timestamp will be exported.

What happens if I export data manually?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the compliance export job is run automatically, manually via the System Console, or manually via the CLI (without the ``--exportFrom`` option), it exports all posts that were made since the last post that the previous execution of the job exported. If this is the first time that the job has ever run, all posts that were made since the feature was enabled will be exported.  

If the ``--exportFrom`` option is specified with the CLI command, all posts that have been made since the supplied timestamp will be exported.

When run manually via the System Console, CSV and Actiance XML files are written to the `exports` subdirectory of the configured `Local Storage Directory <https://docs.mattermost.com/administration/config-settings.html?#local-storage-directory>`_.  Files will be written to a folder with names based on an epoch time range.  Global Relay EML export format will be mailed to the configured email address when run manually. 

Why are compliance exports beta?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature is labelled as beta for the following reasons:

1. The job to carry out a compliance export has not been tested on a system with 10,000s of concurrent active users.
2. Exports do not yet include messages with special types, namely system messages, webhook message attachments and custom plugin messages.
3. There isn't yet a way to distinguish who edited or deleted a message, nor which message is a reply or an edit of another message.
