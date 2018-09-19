Data Retention Policy Beta (E20)
=================================

Available in `Enterprise Edition E20 <https://about.mattermost.com/pricing/>`_.

By default, Mattermost stores all message history providing an unlimited search history to admins and end users.

In Enterprise Edition E20, you may set a custom policy for how long messages and file uploads are kept in Mattermost channels and direct messages.

.. warning:: Once a message or a file is deleted, the action is irreversible. Please be careful when setting up a custom data retention policy.

.. toctree::
    :maxdepth: 2

Set Up Guide
--------------

To set a custom data retention policy:

1. Go to **System Console > Advanced > Data Retention Policy (Beta)**
2. Set your desired retention policy for messages. Messages, including file attachments, older than the duration you set will be deleted nightly. The minimum message retention time is one day.
3. Similarly, set your desired retention policy for file uploads. File uploads older than the duration you set will be deleted nightly from your file storage system, either from your local disk or your Amazon S3 service as specified in **System Console > Files > Storage**. The minimum file retention time is one day.
4. Set the start time of the daily scheduled data retention job. Choose a time when fewer people are using your system. Must be a 24-hour time stamp in the form HH:MM.

Save the settings and restart your server. You're now all set! Data older than the duration you set are now deleted daily at the specified server time.

You may also run the deletion job manually anytime by clicking **Run Deletion Job Now** button in **System Console > Advanced > Data Retention Policy (Beta)**.

Frequently Asked Questions (FAQ)
---------------------------------

What happens when a message is deleted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The message is removed from the Mattermost user interface and deleted from the Posts table. The message is no longer searchable and cannot be retrieved in pinned posts or flagged posts lists.

Replies that did not exceed the message duration are still displayed in the user interface. However, further replies to thread are no longer permitted.

What happens when a file is deleted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The file attachment is removed from the Mattermost user interface, and deleted from the FileInfo table and from your local disk or Amazon S3 service as specified in **System Console > Files > Storage**.

Why didn't an old file get deleted after running the deletion job?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, check the data deletion was successful in the deletion job table in **System Console > Advanced > Data Retention Policy (Beta)**.

Second, if the files were uploaded prior to Mattermost v4.2, you will need to delete the files manually from your local file storage or Amazon S3 storage:

1. Wait until all files uploaded prior to Mattermost v4.2 are past the file retention policy duration.
2. Delete the ``teams/`` folder in the root of your  Mattermost storage directory.

Note that these files will still be removed from the Mattermost user interface if they were uploaded in Mattermost v3.5 or later, which contain the `FileInfo table <https://docs.mattermost.com/administration/changelog.html#database-changes-from-v3-4-to-v3-5>`_. 

Why do I see ``Pending`` in the deletion job table with no details?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This usually means another data retention job is in progress. You can verify this in the deletion job table in **System Console > Advanced > Data Retention Policy (Beta)**.

If no jobs are in progress and the job has stayed pending for more than 2 minutes, then you may not have restarted your server after enabling the data retention policy. Restart your server and try again.

How do I set a custom policy per team or channel?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Setting custom policies for each team and channel are in the roadmap but not yet supported.

If you are interested in this feature, consider upvoting the `existing feature proposal <https://mattermost.uservoice.com/forums/306457-general/suggestions/31731844-ee-data-retention-policy-for-individual-teams-and>`_ and share your feedback in the comments.

How is data retention handled in the mobile apps?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When messages or files are deleted, they are no longer searchable in the Mattermost mobile apps. 

In v1.5 and later of the iOS and Android apps, messages and files are deleted from local storage in the following cases, if they exceed the retention policy duration:

1. When the user opens the app.
2. When the user puts the app into the background.

In v1.4 and earlier of the mobile apps, messages and files are not cleared from local storage when the data retention policy is enabled.

Why is data retention feature beta?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The job to carry a data deletion has not been tested on a system with 10,000s of concurrent active users.

