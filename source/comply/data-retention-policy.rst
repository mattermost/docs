Data Retention Policy (E20)
===========================

*Available in Mattermost Enterprise Edition E20*

By default, Mattermost stores all message history providing an unlimited search history to admins and end users.

In Mattermost Enterprise E20, you can set a custom policy to manage how long messages and file uploads are kept in Mattermost channels and direct messages.

.. warning:: 
  Once a message or a file is deleted, the action is irreversible. Please use caution when setting up a custom data retention policy.

Configuring a Global Data Retention Policy
-------------------------------------------

To set a global data retention policy:

1. Go to **System Console > Compliance > Data Retention Policies**.
2. Select edit from the menu presented to the right of the **Global retention policy** table. 
3. Select a **Channel & direct message retention** option from the dropdown. Specify the number of days or years to keep channel and direct messages. When a time is specified, messages, including file attachments, older than the duration you set will be deleted at the specified time. The minimum retention period is one day.
3. Select a **File retention** option from the dropdown. Specify the number of days or ears to keep files. When a time is specified uploaded files which are older than the duration you set will be deleted from your file storage system (either from your local disk or your Amazon S3 service as specified in **System Console > Environment > File Storage** at the specified time. The minimum retention period is one day.
4. Set the start time of the daily scheduled data retention job under the **Policy log** section. Choose a time when fewer people are using your system. 

Save the settings. Messages and files older than the duration you set will be deleted at the specified server time, if applicable.

Configuring a Custom Data Retention Policy
-------------------------------------------

To set a custom data retention policy in Mattermost versions 5.38+:

1. Go to **System Console > Compliance > Data Retention Policy**.
2. Select **Add policy** from the menu presented to the right of the **Custom retention policy** table. 
3. Create a name for your policy. 
4. Select a **Channel & direct message retention** option from the dropdown. Specify the number of days or years to keep channel and direct messages. When a time is specified, messages, including file attachments, older than the duration you set will be deleted at the specified time. The minimum retention period is one day.
5. Assign teams and channels to this policy by selecting **Add teams** and searching for a specific team, or by selecting **Add channels** and searching for a specific channel. If only teams are specified, all channels for selected teams will be included in the a policy. 
6. Under the **Policy log** section, select **Edit** to specify the start time of the daily scheduled data retention job. Choose a time when fewer people are using your system. If a time is already set for a global retention policy, then the same time applies to custom data retention policies. 

Save the settings. Messages and files older than the duration you set will be deleted at the specified server time, if applicable.

Running a Deletion Job Manually
--------------------------------
You can also run the deletion job manually at any time by selecting **Run Deletion Job Now** in **System Console > Compliance > Data Retention Policy**.

.. note::
  If using data retention and `ElasticSearch <https://docs.mattermost.com/deployment/elasticsearch.html>`_, ensure the `ElasticSearch aggregate search indexes <https://docs.mattermost.com/administration/config-settings.html#aggregate-search-indexes>`_ setting is set to a value that is greater than your data retention policy in days.

Frequently Asked Questions (FAQs)
---------------------------------

What happens when a message is deleted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The message is removed from the Mattermost user interface and deleted from the ``Posts`` table. The message is no longer searchable and cannot be retrieved in pinned posts or saved posts lists. 

Replies that did not exceed the message duration are still displayed in the user interface. However, further replies are no longer possible.

If there was a file attached to the message, it will be removed from the user interface only.  

What happens when a file is deleted by the file retention policy?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The file attachment is removed from the Mattermost user interface, deleted from the ``FileInfo`` table, and from your local disk or Amazon S3 service as specified in **System Console > Environment > File Storage**.

Why didn't an old file get deleted after running the deletion job?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, check the data deletion was successful in the deletion job table in **System Console > Compliance > Data Retention Policy**.

If the files were uploaded prior to Mattermost v4.2, you will need to delete the files manually from your local file storage or Amazon S3 storage:

1. Wait until all files uploaded prior to Mattermost v4.2 are past the file retention policy duration.
2. Delete the ``teams/`` folder in the root of your  Mattermost storage directory.

Note that these files will still be removed from the Mattermost user interface if they were uploaded in Mattermost v3.5 or later, which contain the `FileInfo table <https://docs.mattermost.com/administration/changelog.html#database-changes-from-v3-4-to-v3-5>`__. 

Why do I see ``Pending`` in the deletion job table with no details?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This usually means another data retention job is in progress. You can verify this in the deletion job table in  **System Console > Compliance > Data Retention Policy**.

If no jobs are in progress and the job has stayed ``Pending`` for more than 2 minutes, then you may not have restarted your server after enabling the data retention policy. Restart your server and try again.


How is data retention handled in the mobile apps?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When messages or files are deleted, they are no longer searchable in the Mattermost mobile apps. 

In v1.5 and later of the iOS and Android apps, messages and files are deleted from local storage in the following cases, if they exceed the retention policy duration:

1. When the user opens the app.
2. When the user puts the app into the background.

In v1.4 and earlier of the mobile apps, messages and files are not cleared from local storage when the data retention policy is enabled.

How do I know if a data retention job fails?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost provides the status of each data retention job in **System Console** > **Compliance** > **Data Retention Policy**. Here, you can see if the job succeeded or failed, including the details of the error.

Additionally, any failures are returned in the server logs. The error log begins with the string ``Failed job`` and includes a job_id key/value pair. Data retention job failures are identified with worker name ``EnterpriseDataRetention``. You can optionally create a script that programmatically queries for such failures and notifies the appropriate system.

What happens when the data retention period is changed?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data retention runs once a day at the time specified in the ``config.json`` file. Changing the retention period does not automatically schedule any additional run of the data retention job - it only updates how long data is kept in Mattermost.

Does the System Administrator get any notification when the data retention period is changed?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, the new config is updated, but the System Admin does not receive any feedback on what the effects will be (e.g. reporting of how many messages are to be deleted).

Does the data retention job affect the audits table? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prior to v5.20, data retention would delete all user activity corresponding to the data retention time configuration. From v5.20, the audit table will retain the user activity corresponding to the data retention time configuration. 

Does the data retention job include archived channels? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Posts and attachments in archived channels are affected by the data retention job. If a post exceeds the age configured for the data retention job it will be deleted from the database.

How long does it take to run a deletion query and does it affect server performance?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data retention runs the actual deletion query in batches, deleting data in blocks of 1000 records per query. This is so the database won’t be locked up for extended periods of time with long-running queries. Keeping to this limit keeps the query down to a few milliseconds' execution time on the database itself.

Each batch of data is deleted based on indexes - making the queries quick to execute on small batches. This helps the server remain fully responsive while the process is running.

How do I know whether the data retention job is running/scheduled?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The job scheduler runs the data retention job based on the time specified in the configuration settings. At this time a ``DEBUG``-level log line is printed: ``Scheduling data retention job``.

When a job server picks up that scheduled job for execution, a ``DEBUG``-level log line is generated: ``Worker EnterpriseDataRetention: Received a new candidate job``.

When the job is complete, an ``INFO``-level log line is generated: ``Worker EnterpriseDataRetention: Job is complete``. 
