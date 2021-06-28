Data Retention Policy
=====================

By default, Mattermost stores all message history providing an unlimited search history to admins and end users.

With a data retention policy, you can set a custom policy to manage how long messages and file uploads are kept in Mattermost channels and direct messages.

.. warning:: Once a message or a file is deleted, the action is irreversible. Please be careful when setting up a custom data retention policy.

.. toctree::
    :maxdepth: 2

Configuring a Data Retention Policy
-----------------------------------

To set a custom data retention policy:

1. Go to **System Console > Compliance > Data Retention Policy**.
2. Select a **Message Retention** option. When a time is specified, messages, including file attachments, older than the duration you set will be deleted at the specified time. The minimum retention period is one day.
3. Select a **File Retention** option. When a time is specified uploaded files which are older than the duration you set will be deleted will be deleted at the specified time. The minimum retention period is one day.
4. Set the start time of the daily scheduled data retention job. Choose a time when fewer people are using your system. Must be a 24-hour time stamp in the form HH:MM.

Save the settings. Messages and files older than the duration you set will be deleted at the specified server time, if applicable.

You can also run the deletion job manually at any time by selecting **Run Deletion Job Now** in **System Console > Compliance > Data Retention Policy**.

Frequently Asked Questions (FAQs)
---------------------------------

What happens when a message is deleted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The message is removed from the Mattermost user interface and permanently deleted from the database. The message is no longer searchable and cannot be retrieved in pinned posts or saved posts lists.

Replies that did not exceed the message duration are still displayed in the user interface. However, further replies are no longer possible.

What happens when a file is deleted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The file attachment is removed from the Mattermost user interface and permanently deleted.

Why didn't an old file get deleted after running the deletion job?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, check the data deletion was successful in the deletion job table in **System Console > Compliance > Data Retention Policy**.

Why do I see ``Pending`` in the deletion job table with no details?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This usually means another data retention job is in progress. You can verify this in the deletion job table in  **System Console > Compliance > Data Retention Policy**.

If no jobs are in progress and the job has stayed ``Pending`` for more than an hour, please contact support

How do I set a custom policy per team or channel?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setting custom policies for each team and channel are in the roadmap but not yet supported.

If you are interested in this feature, consider upvoting the `existing feature proposal <https://mattermost.uservoice.com/forums/306457-general/suggestions/31731844-ee-data-retention-policy-for-individual-teams-and>`__ and share your feedback in the comments.

How is data retention handled in the mobile apps?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When messages or files are deleted, they are no longer searchable in the Mattermost mobile apps.

How do I know if a data retention job fails?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost provides the status of each data retention job in **System Console** > **Compliance** > **Data Retention Policy**. Here, you can see if the job succeeded or failed, including the details of the error.

What happens when the data retention period is changed?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data retention runs once a day at the time specified in the settings. Changing the retention period does not automatically schedule any additional run of the data retention job - it only updates how long data is kept in Mattermost.

Does the System Administrator get any notification when the data retention period is changed?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No, the setting is updated, but the System Admin does not receive any feedback on what the effects will be (e.g. reporting of how many messages are to be deleted).

Does the data retention job include archived channels? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Posts and attachments in archived channels are affected by the data retention job. If a post exceeds the age configured for the data retention job it will be deleted from the database.

How long does it take to run a deletion query and does it affect server performance?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data retention runs the actual deletion query in batches, deleting data in blocks of 1,000 records per query. This is so the database won’t be locked up for extended periods of time with long-running queries. Keeping to this limit keeps the query down to a few milliseconds' execution time on the database itself.

Each batch of data is deleted based on indexes - making the queries quick to execute on small batches. This helps the server remain fully responsive while the process is running.
