Compliance Export Beta (E20 Add-On)
=====================================

Available as an `add-on to Enterprise Edition E20 <https://about.mattermost.com/pricing/>`_.

This feature enables compliance exports to be produced from the System Console, containing all messages including those made in direct message channels, as well as file uploads. The exports also include information on channel member history at the time of the message was posted.

By default, Mattermost stores all message history providing an unlimited search history to admins and end users. In Enterprise Edition E20, you may set a `custom data retention policy <https://docs.mattermost.com/administration/data-retention.html>`_ for how long messages and file uploads are kept in Mattermost channels and direct messages.

Those Enterprise deployments who want to archive history beyond the data retention period can enable this add-on to export compliance reports to third-party systems. Integration with Actiance Vantage and GlobalRelay are currently supported, with integrations with other systems in the roadmap.

.. note::
  This feature will replace the existing :doc:`Compliance feature <compliance>` in a future release. Compliance exports to CSV will continue to be available in Enterprise Edition E20.

.. toctree::
    :maxdepth: 2

Set Up Guide
--------------

1. Go to **System Console > Advanced > Compliance Export (Beta)**.
2. Enable compliance exports, then set the start time of the daily scheduled compliance export job. Choose a time when fewer people are using your system. Must be a 24-hour time stamp in the form HH:MM.
3. Set the export file format. Currently, export format to Actiance XML and GlobalRelay EML are supported, but support for the Mattermost CSV format is scheduled for a future release.
4. Save the settings. You’re now all set!

The compliance exports do not contain posts sent before the feature was enabled, but you can export past history via the ``export`` :doc:`command line tool <command-line-tools>`. Posts made prior to upgrading to Mattermost v4.5 will have less accurate channel member history information.

The compliance exports are written to the `exports` subdirectory of the configured `Local Storage directory <https://docs.mattermost.com/administration/config-settings.html#storage>`_, in the format you chose in step 3.

Actiance Vantage Integration
---------------------------------

If you have chosen your file format to be Actiance XML, you can set up an integration with Actiance Vantage.

Channel names will now be exported in the Actiance XML file with the channel type prepended.

For more information on Actiance Vantage archive system, see `their homepage <https://www.actiance.com/products/vantage/>`_.

GlobalRelay Integration
---------------------------------

If you have chosen your file format to be GlobalRelay EML, you can set up an integration with GlobalRelay.

Users must configure the email settings as provided by Global Relay.

Global Relay exports with channel data totalling more than 100MB may fail.

For more information on GlobalRelay archive system, see `their homepage <https://www.globalrelay.com/>`_

Frequently Asked Questions (FAQ)
---------------------------------

How do I export past history?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the ``export`` :doc:`command line tool <command-line-tools>`. You can specify an `exportFrom` option to export data from a specified timestamp. All posts that were made after this timestamp will be exported.

What happens if I export data manually?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the compliance export job is run automatically, manually via the System Console, or manually via the CLI (without the ``--exportFrom`` option), it exports all posts that were made since the last post that the previous execution of the job exported. If this is the first time that the job has ever run, all posts that were made since the feature was enabled will be exported.

If the ``--exportFrom`` option is specified with the CLI command, all posts that have been made since the supplied timestamp will be exported.
