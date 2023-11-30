Migrate from Slack
==================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Migrating from Slack to Mattermost involves the following steps:

1. `Prepare your Mattermost server <#prepare-your-mattermost-server>`__
2. `Generate a Slack import <#generate-a-slack-import>`__
3. `Download file attachments and email addresses <#download-file-attachments-and-email-addresses>`__
4. `Convert the Slack import to Mattermost's format <#convert-slack-import-to-mattermost-s-bulk-export-format>`__
5. `Import data into Mattermost <#import-data-into-mattermost>`__

.. note::

  If you are migrating to a self-hosted deployment of Mattermost, we recommend configuring your Mattermost server to use an S3 filestore before migration, as opposed to using the local filesystem filestore. If you are testing this in a development environment, you can use the ``minio`` docker image to simulate using an S3 bucket.

1. Prepare your Mattermost server
---------------------------------

We recommend you create a separate team in Mattermost for each of your Slack workspaces.

You can import two workspaces into the same team, but you'll need to ensure there are no channel name collisions first. Make sure that all users in Mattermost have the same username as in Slack, otherwise the import will fail.

Also, system administrator roles will be overwritten if the usernames match and the user isn't an admin on the Slack workspace.

2. Generate a Slack import
--------------------------

Slack offers two ways to `export your data from their product <https://get.slack.help/hc/en-us/articles/201658943-Export-your-workspace-data>`_.

1. Regular export - Contains only public channel posts. This does not include private channels, DMs, or group conversations. This can be generated from **Slack > Administration > Workspace settings > Import/Export Data > Export > Start Export**.
2. Corporate export - Contains all posts. This includes public channels, private channels, DMs and group messages. You must `request this export type from Slack directly <https://slack.com/help/articles/1500001548241-Request-to-export-all-conversations>`__.

You will receive a zip file containing the following contents:

- Channels (``channels.json``)
- Users (``users.json``)
- Direct messages (``dms.json``) (Corporate export)
- Private channels (``groups.json``) (Corporate export)
- Group direct messages (``mpims.json``) (Corporate export)
- App activity logs (``integration_logs.json``)
- Folders containing posts for every public channel
- Folders containing posts for every private channel (Corporate exports)

.. note::

  - Refer to the `Slack help article <https://slack.com/help/articles/220556107-How-to-read-Slack-data-exports>`__ for additioanl details on zip file contents.
  - As a proprietary SaaS service, Slack is able to change its export format quickly and without notice. If you encounter issues not mentioned in the following documentation, please let the Mattermost Product Team know by `filing an issue <https://handbook.mattermost.com/contributors/contributors/ways-to-contribute>`__.

3. Download file attachments and email addresses
------------------------------------------------

When you download your Slack export zip file, some data will be missing from the zip file:
- User emails
- Uploaded attachment contents

We need to create a Slack app in order to gather these contents. Follow these steps to create a Slack app:

1. Go to https://api.slack.com/apps.
2. Select **Create New App**.
3. Select **From scratch**.
4. Name the app **Slack Advanced Exporter** and select the workspace. You'll have to do this for every workspace. Then select **Create App**.
5. Select **OAuth & Permissions** on the left-hand side of the screen. Then scroll down to **Scopes**.
6. Under **Bot Token Scopes** type in and select the following scopes:
  - ``users:read``
  - ``users:read.email``

7. Scroll up and select **Install to Workspace**.
8. Grant the app permissions when prompted.
9. Copy the **Bot User OAuth Token** and save it somewhere convenient.

We'll now use **Bot User OAuth Token** with the ``slack-advanced-exporter`` tool to download emails and attachments. Download the latest release of ``slack-advanced-exporter`` for your OS and architecture `here <https://github.com/grundleborg/slack-advanced-exporter/releases/>`__ and extract the executable from the download.

Once you have the program downloaded locally, run the commands below to fetch the emails, and then fetch file attachments. Replace ``<SLACK TOKEN>`` with the Slack token you generated earlier and ``<SLACK EXPORT FILE>`` with the `path <https://www.geeksforgeeks.org/absolute-relative-pathnames-unix/>`__ to your export file.

.. code:: bash

  ./slack-advanced-exporter --input-archive <SLACK EXPORT FILE> --output-archive export-with-emails.zip fetch-emails --api-token <SLACK TOKEN>
  ./slack-advanced-exporter --input-archive export-with-emails.zip --output-archive export-with-emails-and-attachments.zip fetch-attachments --api-token <SLACK TOKEN>

.. note::

  - The first command collects all of the user emails and creates the file ``export-with-emails.zip``. The second command fetches attachments and creates the file ``export-with-emails-and-attachments.zip``, which we will use going forward.
  - The second command can take a long time if you have a large number of file uploads. If it's interrupted, delete the file generated (if any), and start again.

The file ``export-with-emails-and-attachments.zip`` now contains all the information necessary to be imported into Mattermost.

From the slack advanced exporter repo:
Due to archive/zip limitations, these actions cannot modify archive in place. It's preferable to fetch e-mails first to avoid copying large attachments around.

.. important::

  Avoid unzipping and rezipping the Slack export. Doing so can modify the directory structure of the archive which could cause issues with the import process.

4. Convert Slack import to Mattermost's bulk export format
----------------------------------------------------------

Now that you have a Slack export file with emails and attachments, let's convert this information into Mattermost's bulk import format using the import preparation tool ``mmetl``. Download the latest release of ``mmetl`` for your `OS and architecture <https://github.com/mattermost/mmetl/releases/>`__. Run ``mmetl help`` to learn more about using the tool.

Next, run the following command to create a Mattermost bulk import file. Replace ``<TEAM-NAME>`` with the name of your team in Mattermost. Note that the name needs to be one word like "my-team".

.. code:: bash

    ./mmetl transform slack --team <TEAM-NAME> --file export-with-emails-and-attachments.zip --output mattermost_import.jsonl

The tool outputs a `.jsonl <https://jsonlines.org/examples>`__ file containing all of your users, channels, and posts. It also creates a ``data`` folder that contains all of your attachments.

.. important::

  It doesn't matter what you name the ``.jsonl`` file. You can name it what you want with the `--output` flag as shown above. It just needs to be a ``.jsonl`` file.

5. Import data into Mattermost
------------------------------

We have two options to run the import process:

1. Uploading the export through Mattermost's API, via command line ``mmctl`` from the server or from another computer. This option is required for Mattermost Cloud deployments.
2. SSH into the Mattermost server's host, upload the export file to this server's file system somehow, and use the ``mattermost`` command to process the export file.

For the first option, the server will save the import in its file store before running the import (e.g. AWS S3 if you are using that are your file store), so there will be time spent uploading/downloading the file in this case. Since this is really just a one-time thing to import this file, we recommend the first option of running it on the server itself *if you have a large export zip file*.

The migration is idempotent, meaning that you can run multiple imports that contain the same posts, and there will not be duplicated created posts in Mattermost. Each post is imported with the correct user/author and ``created_at`` value from your Slack instance. Threads are kept in tact with the import.

Option 1: Upload export via ``mmctl``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure you have the Mattermost command line tool ``mmctl`` installed. This allows you to perform different tasks that communicate to Mattermost's API. You'll also want to `configure authentication </manage/mmctl-command-line-tool.html#mmctl-auth>`__ for the tool.

To prepare our files to be uploaded to the server, we need to put both the ``.jsonl`` file and ``data`` folder together into a zip file.

.. code:: bash

  zip -r mattermost-bulk-import.zip data mattermost_import.jsonl

Then we can upload the zip file to our Mattermost server:

.. code:: bash

  mmctl import upload ./mattermost-bulk-import.zip

Run this command to list the available imports:

.. code:: bash

  mmctl import list available

Run this command to process the import. Replace ``<IMPORT FILE NAME>`` with the name you got from the ``mmctl import list available`` command:

.. code:: bash

  mmctl import process <IMPORT FILE NAME>

Finally, run this command to view the status of the import process job. If the job status shows as ``pending``, then wait before running the command again. The ``--json`` flag is required to view the possible error message. Replace ``<JOB ID>`` with the id you got from the ``mmctl import list process`` command:

.. code:: bash

  mmctl import job show <JOB ID> --json

Option 2: Use the ``mattermost`` command to run the export
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First get the ``.jsonl`` file and ``data`` folder onto your server using something like ``scp``. Then you'll use the ``mattermost`` binary to process the bulk import data:

.. code:: bash

    mattermost import bulk ./mattermost_import.jsonl --import-path ./data --apply

Debug imports
^^^^^^^^^^^^^

If you choose the ``mmctl`` option above, you can use the ``mmctl import job show`` command to view any relevant errors that may have occurred. If you run into problems which the error message does not help to resolve, please try the first option of using the ``mattermost bulk import`` command. The ``mmctl`` import process does not give you any additional debugging information, even in the Mattermost server logs.

.. important::

    Note that if your logged in Mattermost user is not present in your input (neither the email nor the username matches any users in the import file), your user will not be added to any new channels in the import process.

Additional tools
^^^^^^^^^^^^^^^^

* `mm-emoji <https://github.com/maxwellpower/mm-emoji>`__ - Designed to smoothly transition emojis from a Slack instance to Mattermost.
* `mm-importjs <https://github.com/mickmister/mmimportjs>`__ - Breaks up large import files into smaller ones, as well as automatically remove null characters in post content when importing data to Mattermost.
* `slack-migrate-pinned-posts <https://github.com/svelle/slack-migrate-pinned-posts>`__ - Migrates pinned posts from Slack to Mattermost.

Use the imported team
^^^^^^^^^^^^^^^^^^^^^

* During the import process, the emails and usernames from Slack are used to create new Mattermost accounts. If emails are not present in the Slack export archive, then placeholder values will be generated and the system admin will need to update these manually.
* Slack users can activate their new Mattermost accounts by using Mattermost's **Password Reset** screen with their email addresses from Slack to set new passwords for their Mattermost accounts.
* Once logged in, Mattermost users will have access to previous Slack messages in the public channels imported from Slack.
