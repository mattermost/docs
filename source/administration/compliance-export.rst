Compliance Export Beta (E20 Add-On)
=====================================

Available as an `add-on to Enterprise Edition E20 <https://about.mattermost.com/pricing/>`_.

This feature enables compliance exports to be produced from the System Console, with all query and download actions logged in an audit history to enable oversight and prevent unauthorized queries.

By default, Mattermost stores all message history providing an unlimited search history to admins and end users. In Enterprise Edition E20, you may set a `custom data retention policy <https://docs.mattermost.com/administration/data-retention.html>`_ for how long messages and file uploads are kept in Mattermost channels and direct messages.

Those Enterprise deployments who want to archive history beyond the data retention period can enable this add-on to export compliance reports to third-party systems. Integration with Actiance Vantage is currently supported, with integrations with other systems such as GlobalRelay in the roadmap.

.. note::
  This feature will replace the existing `Compliance feature <https://docs.mattermost.com/administration/compliance.html>`_. Compliance exports to CSV will continue to be available in Enterprise Edition E20.

.. toctree::
    :maxdepth: 2

// XXXX JB: Add to TOC

Set Up Guide
--------------

1. Go to **System Console > Advanced > Compliance Export (Beta)**.
2. Enable compliance exports, then set the start time of the daily scheduled compliance export job. Choose a time when fewer people are using your system. Must be a 24-hour time stamp in the form HH:MM.
3. Set the export file format. Currently, export format to Actiance XML is supported, but support for the GlobalRelay EML format and the Mattermost CSV format are scheduled for a future release.
4. Set the export directory to write compliance export files to. Must be a subdirectory of the Local Storage Directory. Mattermost must have write access to this directory, and the path that you set must not include a filename.

Save the settings. You’re now all set!

// XXX JF: Any info on query output like in https://docs.mattermost.com/administration/compliance.html#compliance-query-definition-stored-in-meta-json-file that we should consider including?

Actiance Vantage Integration
---------------------------------

// XXX JF: Is there a link to Actiance docs we can share?

Frequently Asked Questions (FAQ)
---------------------------------

// XXX JF: can you help with the following. Also happy to add more questions that you feel admins may ask about.

1) How to export past history (via the CLI)?
2) What happens when you archive manually --> i.e. what's exported on the next scheduled run? Is it messages between the last time the export was run to the time of the next scheduled run? If so, what happens if you run the export manually right before the scheduled run?
