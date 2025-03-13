Compliance export
=================

.. include:: ../_static/badges/ent-cloud-selfhosted.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

Mattermost Enterprise customers can archive history or transfer message data to third-party systems for auditing and compliance purposes with compliance exports. Supported integrations include `Actiance Vantage <#actiance-xml>`__, `Global Relay <#global-relay-eml>`__, and `Proofpoint <#proofpoint>`__. 

From Mattermost v10.5, compliance exports include performance improvements for large daily data sets with changes affecting output formats, system performance, and logic. Compliance exports provide compliance teams complete information to reconstruct the state of a channel, and to determine who had visibility on an initial message, or when the message was edited or deleted. Compliance teams can track a message by its MessageId as it is edited or deleted, and across batches and exports periods.

Overview
---------

Compliance exports are produced from the System Console, and contain all messages including:

- Messages sent in direct message channels
- File uploads
- Posts from plugins
- Posts from bots/webhooks

Exports include information on channel member history at the time the message was posted.

Set up guide
------------

Use the following guides to configure exports for `CSV <#csv>`__, `Actiance XML <#actiance-xml>`__, `Global Relay EML <#global-relay-eml>`__, or `Proofpoint <#proofpoint>`__.

.. note::

   - For self-hosted deployments, compliance exports are written to the ``exports`` subdirectory of the configured filestore in the chosen format. This will either be in the :ref:`Local Storage directory <configure/environment-configuration-settings:file storage>` or the Mattermost S3 bucket if S3 storage is configured.
   - Alternatively, you can specify an alternate filestore target and generate an S3 presigned URL for compliance exports. See the :ref:`dedicated export filestore target <configure/experimental-configuration-settings:enable dedicated export filestore target>` configuration settings documentation for details.
   - Compliance exports don't contain posts sent before the feature was enabled. For self-hosted deployments, you can export past history via the ``export`` :doc:`command line tool <../manage/command-line-tools>`. 

CSV
~~~~

1. Go to **System Console > Compliance > Compliance Export**.
2. Set **Enable Compliance Exports** to **true**.
3. Set the **Compliance Export time**. This is the start time of the daily scheduled compliance export job and must be a 24-hour time stamp in the form ``HH:MM``. Choose a time when fewer people are using your system.
4. Set the export file format to **CSV**.
5. Select **Save**.

.. tab:: From Mattermost v10.5

   You can review export job status in the System Console.

   When the daily compliance export job is finished, a parent directory is created named based on when the export was started and the ``startTimestamp`` and ``endTimestamp`` of the export, e.g, ``compliance-export-2024-08-13-05h08m-1723105062492-1723109100075``. That parent directory contains 1 zip file for each batch, named based on the batch number and the start and end timestamps of the messages in that batch, e.g, ``batch001-1723105062492-1723106622163.zip``. Each zip file contains the same information available in previous Mattermost server releases.

   Working from the same example above, the directory would look like this:

   .. code-block:: bash

      compliance-export-2024-08-13-05h08m-1723105062492-1723109100075
      ├── batch001-1723105062492-1723106622163.zip
      ├── batch002-1723106622163-1723108196005.zip
      └── batch003-1723108196005-1723109100075.zip

   And each batch would look like this:

   .. code-block:: bash

      batch001-1723105062492-1723106622163.zip
      ├── files
      ├── metadata.json
      └── actiance_export.xml

   **Updated CSV export fields**

   **Post Creation Time** is always the ``CreateAt`` for messages and attachments, or ``JoinTime`` and ``LeaveTime`` for participant join and leave events, respectively.

   - **Update Time** indicates that the message has been updated, and this is the ``updateAt`` time.
   - **Updated Type** helps differentiate what kind of update it was as one of the following:

     - **EditedNewMsg** indicates that the message has been edited, and this is the new message (post-edit) content.
     - **EditedOriginalMsg** indicates that the message has been edited, and this the original message (pre-edit) content. This message will have another field ``EditedNewMsgId``, which is the Id of the message which holds the post-edited message contents.
     - **UpdatedNoMsgChange** indicates that message's content hasn't changed, but the post was updated for some reason, such as reaction, replied-to, a reply was edited, or a reply was deleted.
     - **Deleted** indicates that this message was deleted.
     - **FileDeleted** indicates that this message is recording that a file was deleted.

.. tab:: Prior to Mattermost v10.5

   The daily compliance export job creates a ``.zip`` file with a unique job identifier of all messages posted in the last 24 hours. You can unzip the file to easily transform the default ``.csv`` format into a desired format for your third-party archive system.

   For a sample CSV output, `download a CSV export file here <https://github.com/mattermost/docs/blob/master/source/samples/csv_export.zip>`__.

Actiance XML
~~~~~~~~~~~~

1. Go to **System Console > Compliance > Compliance Export**.
2. Set **Enable Compliance Exports** to **true**.  
3. Set the **Compliance Export time**. This is the start time of the daily scheduled compliance export job and must be a 24-hour time stamp in the form HH:MM. Choose a time when fewer people are using your system.
4. Set the export file format to **Actiance XML**.
5. Select **Save**.

.. note::

   In Actiance XML exports, channel type is prepended to the channel names.

.. tab:: From Mattermost v10.5

   You can review export job status in the System Console. Once you've selected Actiance XML as your file format, you can set up an integration with Actiance Vantage archive system. 

   When the daily compliance export job is finished, a parent directory is created named based on when the export was started and the ``startTimestamp`` and ``endTimestamp`` of the export, e.g, ``compliance-export-2024-08-13-05h08m-1723105062492-1723109100075``. That parent directory contains 1 zip file for each batch, named based on the batch number and the start and end timestamps of the messages in that batch, e.g, ``batch001-1723105062492-1723106622163.zip``. Each zip file contains the same information available in previous Mattermost server releases.

   Working from the same example above, the directory would look like this:

   .. code-block:: bash

      compliance-export-2024-08-13-05h08m-1723105062492-1723109100075
      ├── batch001-1723105062492-1723106622163.zip
      ├── batch002-1723106622163-1723108196005.zip
      └── batch003-1723108196005-1723109100075.zip

   And each batch would look like this:

   .. code-block:: bash

      batch001-1723105062492-1723106622163.zip
      ├── 20240808
      └── actiance_export.xml

   **Updated Actiance XML export fields**

   If an XML field is empty, it won't be exported. This is a change from previous Mattermost releases, where empty XML nodes were exported.

   - ``MessageId`` is the unique ``messageId``.
   - ``DateTimeUTC`` is always the post's ``CreateAt`` time.
   - ``UpdatedDateTimeUTC`` indicates that the message has been updated, and this is the ``updateAt`` time.
   - ``UpdatedType`` helps differentiate what kind of update it was, including:

     - ``EditedNewMsg`` indicates that this message has been edited, and this is the new message (post-edit) content.
     - ``EditedOriginalMsg`` indicates that this message has been edited, and this the original message (pre-edit) content. This message will have another field ``EditedNewMsgId``, which is the Id of the message which holds the post-edited message contents.
     - ``UpdatedNoMsgChange`` indicates that this message's content hasn't changed, but the post was updated for some reason, such as a reaction, replied-to, a reply was edited, or a reply was deleted.
     - ``Deleted`` indicates that the message was deleted.
     - ``FileDeleted`` indicates that the message is recording that a file was deleted.

.. tab:: Prior to Mattermost v10.5

   The daily compliance export job creates a ``.zip`` file with a unique job identifier of all messages posted in the last 24 hours. Once you've selected Actiance XML as your file format, you can set up an integration with Actiance Vantage archive system. For a sample Actiance output, `download an Actiance XML export file here <https://github.com/mattermost/docs/blob/master/source/samples/actiance_export.xml>`__.

Global Relay EML
~~~~~~~~~~~~~~~~

For more information on Global Relay archive system, visit `their website <https://www.globalrelay.com/>`_.

1. Go to **System Console > Compliance > Compliance Export**.
2. Set **Enable Compliance Export** to **true**.
3. Set the **Compliance Export time**. This is the start time of the daily scheduled compliance export job and must be a 24-hour time stamp in the form HH:MM. Choose a time when fewer people are using your system.
4. Set the **Export Format** to **GlobalRelay EML**.
5. Select **A9/Type 9**, **A10/Type 10**, or **Custom** for the **Global Relay Customer Account**. This is the type of Global Relay customer account your organization has.
   
   - For **A9/Type 9** and **A10/Type 10** types, set the **Global Relay SMTP username**, **Global Relay SMTP password**, and **Global Relay SMTP email address**, provided by Global Relay.
   - For a **Custom** type, set the **Global Relay SMTP username**, **Global Relay SMTP password**, **Global Relay SMTP email address**, **SMTP Server Name**, and the **SMTP Server Port**, provided by Global Relay. **Custom** type can be used to integrate with Proofpoint.
6. Select **Save**.

.. note::
  
   Messages larger than 250 MB will have their attachments removed because they are too large to send to Global Relay. An error is added to the server logs with id ``global_relay_attachments_removed``. It includes the post ID the attachments were removed from, as well as the attachment IDs. A `ticket is queued to better handle large messages <https://mattermost.atlassian.net/browse/MM-10038>`__.

Once you've selected Global Relay EML as your file format, you can set up an integration with Global Relay archive system. For more information, see `Global Relay Archive <https://www.globalrelay.com/products/archive-data-compliance/>`_.

Proofpoint
~~~~~~~~~~~

1. Go to **System Console > Compliance > Compliance Export**.
2. Set **Enable Compliance Export** to **true**.
3. Set the **Compliance Export time**. This is the start time of the daily scheduled compliance export job and must be a 24-hour time stamp in the form HH:MM. Choose a time when fewer people are using your system.
4. Set the **Export Format** to **GlobalRelay EML**.
5. Select **Custom** for the **Global Relay Customer Account** to integrate with Proofpoint.
6. Set the **SMTP username**, **SMTP password**, **SMTP email address**, **SMTP Server Name**, and the **SMTP Server Port**, provided by Proofpoint. 
7. Select **Save**.

See the `Global Relay <#global-relay-eml>`__ section for details on updated Global Relay export fields. Now you can set up an integration with the Proofpoint archive system. For more information, visit the `Proofpoint Archive webiste <https://www.proofpoint.com/us/products/archiving-and-compliance/archive>`__.

Frequently Asked Questions (FAQ)
--------------------------------

How do I export past history?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the ``export`` :doc:`command line tool <../manage/command-line-tools>`. You can specify an ``exportFrom`` option to export data from a specified timestamp. All posts that were made after this timestamp will be exported.

What happens if I export data manually?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the compliance export job is run automatically, manually via the System Console, or manually via the CLI (without the ``--exportFrom`` option), it exports all posts that were made since the last post that the previous execution of the job exported. If this is the first time that the job has ever run, all posts that were made since the feature was enabled will be exported.

If the ``--exportFrom`` option is specified with the CLI command, all posts that have been made since the supplied timestamp will be exported.

When run manually via the System Console, ``.csv`` and Actiance XML files are written to the ``exports`` subdirectory of the configured :ref:`Local Storage Directory <configure/environment-configuration-settings:local storage directory>`.  Files will be written to a folder with names based on an epoch time range. Global Relay EML export format files will be mailed to the configured email address when run manually.

Is there a maximum row limit for CSV files?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No. There's no limit to the number of rows within Compliance Monitoring CSV files.

How do I know if a compliance export job fails?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost provides the status of each compliance export job in **System Console > Compliance > Compliance Export**. Here, you can see if the job succeeded or failed, including the number of messages and files exported.

In addition, any failures are returned in the server logs for self-hosted deployments. The error log begins with the string ``Failed job`` and includes a ``job_id key/value`` pair. Compliance export job failures are identified with worker name ``MessageExportWorker``. You can optionally create a script that programmatically queries for such failures and notifies the appropriate system.

.. note::
  
   This compliance export feature replaces legacy Compliance Reporting Oversight functionality. We recommend Enterprise customers migrate to the new system. For a sample CSV output of the new compliance export system, `download a CSV export file here <https://github.com/mattermost/docs/blob/master/source/samples/csv_export.zip>`__.
