Migrate from Slack
==================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Overview
--------

Mattermost provides a reliable migration path from Slack, enabling you to bring your organization’s collaboration history into a secure, self-hosted Mattermost environment. The migration process supports full workspaces, including users, channels and message history, direct messages, and threads so your teams can continue working without losing valuable context.

This process generally involves preparing your environment, exporting data from Slack, converting that data into a compatible format, and then importing it into Mattermost. Migrating from Slack is a multi-step process that can be complex, particularly for larger organizations or those with multiple Slack workspaces.

Additionally, please consider that Slack's data control policies or export capabilities may change at any time, or they may charge fees to customers for exporting data stored in Slack. Support for negotiating export of customer IP from Slack Enterprise can be requested by contacting a `Mattermost Expert <https://mattermost.com/contact-sales/>`_.

1. `Preparations <#preparations>`__:

   - Answer key scoping questions.
   - Gather environment and export details.
   - Validate Mattermost server capacity and configuration.
   - Back up your Mattermost environment before importing.

2. `Export Slack data <#export-slack-data>`__:

   - Generate an export from Slack in the user interface or by contacting Slack directly.
   - Download file attachments and email addresses using the ``slack_advanced_exporter``

3. `Transform the export for Mattermost <#transform-the-export-for-mattermost>`__:

   - Use the ``mmetl`` tool to parse and transform Slack exports.

4. `Import into Mattermost <#import-data-into-mattermost>`__:

   - Upload and process transformed archives with ``mmctl``.

5. Validate and test:

   - Confirm channel and user data imported correctly.
   - Run database queries to fix any unread states.

6. Go live:

   - Communicate the cutover plan to users.

Migration timeline
~~~~~~~~~~~~~~~~~~

These instructions outline a *best effort* migration path designed to preserve the majority of your messages, files, and workspace structure. Mattermost provides tools and guidance to help streamline the process, but manual adjustments during the data transformation and import steps are often required. Successful migration depends on careful planning and dedicating sufficient time, technical resources, and technical skills to the effort.

Depending on the size and complexity of your Slack environment, a full migration can take anywhere from several days to multiple weeks of dedicated effort. Larger organizations with multiple workspaces, extensive message history, and many files should expect the process to require significant iteration and testing before completion. It’s important to plan for this timeline in advance by allocating the necessary resources, scheduling time for trial imports in a development environment, and coordinating across teams. Building in extra time for adjustments during the transformation and import steps will help ensure a smoother transition and reduce disruption to your users.

Scoping the migration appropriately during the preparation step can significantly reduce processing time and allow for faster iteration. Before beginning, carefully consider what data is essential to bring over to Mattermost. Many organizations find that not every channel or file needs to be migrated, and focusing only on what is truly needed can save substantial processing time and manual effort. By setting clear boundaries early, you’ll minimize the amount of data that requires manual intervention and testing, which in turn shortens the migration timeline and helps avoid unnecessary complexity.

.. note::
  Consider `talking to a Mattermost expert <https://mattermost.com/contact-sales/>`_ if your organization needs support migrating from Slack to Mattermost.

Migrations Steps
----------------

.. _preparations:

1. Preparations
~~~~~~~~~~~~~~~

Before beginning the migration, it’s important to properly prepare your environment. Careful preparation helps reduce processing time, allows for faster iteration, and minimizes the chance of running into avoidable issues during the import.

This document assumes you already have a Mattermost Server deployed that is ready to accept your Slack data. If not, consider the recommendations in this section in conjunction with the appropriate :ref:`deployment documentation <deployment-guide/server/server-deployment-planning:deployment options>` to make informed decisions about your supporting database and file storage infrastructure.

Scope definition
^^^^^^^^^^^^^^^^

Start by defining the scope of your migration:

- **Slack edition**: Migrating from Slack Enterprise Grid involves additional `steps and planning <#faq>`_.
- **Data history**: Decide how much history is necesary to import. Importing a smaller time window (e.g., the last six months) can significantly reduce complexity and processing time.
- **Export size**: Consider the size of your Slack export file as you progress through this guide. File size directly impacts how long the import will take - for example, files under ~25 GB often complete within a day, while exports over 100 GB can take several days, significantly lengthening the time between iterations and the overall timeline to complete the migration.
- **File attachments**: Consider whether you can exclude very large or non-critical attachments (for example, public software download packages, videos, or outdated media assets) to reduce import size and speed up processing.

Infrastructure considerations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The environment where you run the import can significantly affect performance:

- **Test environment**: Always run the migration in a development or staging environment first. Most migrations require multiple iterations before a production import is successful.
- **Operating system**: The ``mmetl`` and ``slack_advanced_exporter`` tools are supported on Linux and macOS. Windows is not supported, and we do not recommend using Windows Subsystem for Linux (WSL) since the file system is not performant enought for the heavier processes involved in migration.
- **Storage requirements**: Ensure your server can store both the Slack export archive and the fully unpacked data. As a best practice, plan for at least three times the size of your Slack export in available server storage.
- **File Storage**: Imports into S3 file storage typically complete faster than imports into local storage or NFS. For large imports, we recommend using AWS S3 or another S3-compatible storage service for best performance.

Mattermost server considerations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Carefully preparing your environment and making these adjustments up front will help ensure the migration proceeds smoothly and reduces the need for repeated trial-and-error.

- **Fresh server**: The most reliable imports happen on a fresh Mattermost installation. If importing into an existing server, never import over an existing team.

- **Server version**: Make sure you are running the latest supported version of :doc:`Mattermost </product-overview/mattermost-server-releases>` to benefit from the most up-to-date functionality and fixes.

- **Backups**: When importing into an already existing Mattermost environment, back up both the Mattermost database and the data directory before starting. If an import fails, you’ll need to roll back or reset.

  - If merging multiple Slack workspaces into a single team is the desired end-result, we recommend completing the import to separate teams, validating the results, then using :ref:`mmctl <administration-guide/manage/mmctl-command-line-tool:mmctl channel move>` to move channels between teams.

- **Configuration settings**: Adjust the following settings before starting the import:

  - ``TeamSettings.MaxChannelsPerTeam``: Set to this to a number much higher than the number of users you are migrating.
  - ``TeamSettings.MaxUsersPerTeam``: Set to this to a number much higher than the number of users you are migrating.
  - **Team Settings > Allow any user with an account on this server to join this team**: Ensure this is enabled for the team receiving the import.
  - ``EmailSettings.EnableSignUpWithEmail`` and ``EmailSettings.EnableSignInWithEmail``: Both must be set to ``true``
  - ``FileSettings.MaxFileSize``: Set this higher than the largest file in your Slack export.
  - ``ElasticsearchSettings. EnableIndexing``, ``ElasticsearchSettings > EnableSearching`` and ``ElasticsearchSettings.EnableAutocomplete``: All must be set to ``false`` during the import to prevent performance issues. After the import, you can purge and reindex before enabling Elasticsearch.

.. _export-slack-data:

2. Export Slack data
~~~~~~~~~~~~~~~~~~~~

Slack offers two ways to `export your data from their product <https://slack.com/help/articles/201658943-Export-your-workspace-data>`_.

1. Regular export - Contains only public channel posts. This does not include private channels, DMs, or group conversations. This can be generated from **Slack > Administration > Workspace settings > Import/Export Data > Export > Start Export**.
2. Corporate export - Contains all posts. This includes public channels, private channels, DMs and group messages. You must `request this export type from Slack directly <https://slack.com/help/articles/1500001548241-Request-to-export-additional-data-from-your-workspace-or-Enterprise-Grid-org>`_.

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
  - As a proprietary SaaS service, Slack is able to change its export format quickly and without notice.

Download file attachments and email addresses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

We'll now use **Bot User OAuth Token** with the ``slack-advanced-exporter`` tool to download emails and attachments. Download the latest release of ``slack-advanced-exporter`` `for your OS and architecture <https://github.com/grundleborg/slack-advanced-exporter/releases/>`_ and extract the executable from the download.

Once you have the program downloaded locally, run the commands below to fetch the emails, and then fetch file attachments. Replace ``<SLACK TOKEN>`` with the Slack token you generated earlier and ``<SLACK EXPORT FILE>`` with the `path to your export file <https://www.geeksforgeeks.org/absolute-relative-pathnames-unix/>`_.

.. code-block:: sh

  ./slack-advanced-exporter --input-archive <SLACK EXPORT FILE> --output-archive export-with-emails.zip fetch-emails --api-token <SLACK TOKEN>
  ./slack-advanced-exporter --input-archive export-with-emails.zip --output-archive export-with-emails-and-attachments.zip fetch-attachments --api-token <SLACK TOKEN>

.. note::

  - The first command collects all of the user emails and creates the file ``export-with-emails.zip``. The second command fetches attachments and creates the file ``export-with-emails-and-attachments.zip``, which we will use going forward.
  - The second command can take a long time if you have a large number of file uploads. If it's interrupted, delete the file generated (if any), and start again.

The file ``export-with-emails-and-attachments.zip`` now contains all the information necessary to be imported into Mattermost.

It's preferable to fetch e-mails first to avoid copying large attachments around. Make sure you choose different file names at each stage, as the tool does not support in-place modifications.

.. important::

  Avoid unzipping and rezipping the Slack export. Doing so can modify the directory structure of the archive which could cause issues with the import process.

.. _transform-the-export-for-mattermost:

3. Transform the export for Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that you have a Slack export file with emails and attachments, let's convert this information into Mattermost's bulk import format using the import preparation tool ``mmetl``.

`Download the latest release of mmetl <https://github.com/mattermost/mmetl/releases/>`__ for your OS and architecture. Run ``mmetl help`` to learn more about using the tool.

Next, run the command below to create a Mattermost bulk import file. Replace ``<TEAM-NAME>`` with the name of your team in Mattermost. Note that the name needs to be one word and lowercase (i.e. if you named your team ``My Team``, ``<TEAM-NAME>`` would be ``my-team``).

.. code-block:: sh

    ./mmetl transform slack --team <TEAM-NAME> --file export-with-emails-and-attachments.zip --output mattermost_import.jsonl

The tool outputs a `.jsonl <https://jsonlines.org/examples>`__ file containing all of your users, channels, and posts. It also creates a ``data`` folder that contains all of your attachments. It doesn't matter what you name the ``.jsonl`` file. You can name it what you want with the `--output` flag as shown above. It just needs to be a ``.jsonl`` file.

Debug transform
^^^^^^^^^^^^^^^

The ``mmetl transform`` process produces a ``transform-slack.log`` file that records INFO level output by default.

If you run the import commands with the ``--debug`` flag, the log will include additional ``DEBUG`` level entries. These entries provide more granular detail on each phase of the process, which can help identify where the transformation may be slowing down or failing.

MMETL parsing phases
^^^^^^^^^^^^^^^^^^^^

When parsing a Slack export file with the ``mmetl`` tool, the process runs through four phases. You can track progress by monitoring the log output during each phase. Understanding these phases helps set expectations for how long the parsing step may take.

**1. Reading the import file**

In this phase, ``mmetl`` reads through the Slack export file. Example log line:

``{"file":"parse.go:359","level":"info","msg":"Processing file 1 of 10335: aluminum-white-lightbulb/","time":"2024-03-11T20:41:09-04:00"}``

This step usually takes 5–10 minutes depending on the size of the export archive.

**2. Converting user mentions**

During this phase, ``mmetl`` converts Slack user mentions into Mattermost-compatible format. Example log line:

``{"file":"parse.go:224","level":"debug","msg":"Slack Import: converting user mentions for channel touchscreen-headphones-sleek. 1 of 400","time":"2024-03-11T20:41:10-04:00"}``

This step can be time-consuming on large imports and may take several hours.

**3. Converting channel mentions**

In this phase, channel references are updated. Example log line:

``{"file":"parse.go:259","level":"debug","msg":"Slack Import: converting channel mentions for channel robust-smart-home-device-matrix. 95 of 400","time":"2024-03-11T20:41:48-04:00"}``

This step typically completes in about half the time required for user mentions.

**4. Converting post markup**

Finally, Slack message formatting is converted into Mattermost-compatible Markdown. Example log line:

``{"file":"parse.go:330","level":"debug","msg":"Slack Import: converting markdown for channel vertex-robust-vacuum. 120 of 400","time":"2024-03-11T20:41:58-04:00"}``

This is the fastest step and usually completes quickly.

.. _import-data-into-mattermost:

4. Import data into Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can upload the export through Mattermost's API from the server or from another computer using mmctl commands. The server will save the import in its file store before running the import (e.g. AWS S3), so there will be time spent uploading/downloading the file in this case.

The migration is idempotent, meaning that you can run multiple imports that contain the same posts, and there won't be duplicated created posts in Mattermost. Each post is imported with the correct user/author and ``created_at`` value from your Slack instance.

Ensure you have the Mattermost command line tool ``mmctl`` installed. This allows you to perform different tasks that communicate to Mattermost's API. You'll also want to :ref:`configure authentication <administration-guide/manage/mmctl-command-line-tool:mmctl auth>` for the tool.

To prepare our files to be uploaded to the server, we need to put both the ``.jsonl`` file and ``data`` folder together into a zip file.

.. code-block:: sh

  zip -r mattermost-bulk-import.zip data mattermost_import.jsonl

Then we can upload the zip file to our Mattermost server. These files can be very large, so getting them onto the server can be challenging. You have two primary options for this step:

- You can use the ``mmctl`` tool:

  .. code-block:: sh

    mmctl import upload ./mattermost-bulk-import.zip

- Alternatively, you can move the file directly to the data directory under ``data/import`` and give it a unique name.

Run this command to list the available imports:

.. code-block:: sh

  mmctl import list available

Run this command to process the import. Replace ``<IMPORT FILE NAME>`` with the name you got from the ``mmctl import list available`` command:

.. code-block:: sh

  mmctl import process <IMPORT FILE NAME>

Finally, run this command to view the status of the import process job. If the job status shows as ``pending``, then wait before running the command again. The ``--json`` flag is required to view the possible error message. Replace ``<JOB ID>`` with the id you got from the ``mmctl import list process`` command:

.. code-block:: sh

  mmctl import job show <JOB ID> --json

Debug imports
^^^^^^^^^^^^^

You can use the ``mmctl import job show`` command to view any relevant errors that may have occurred.

Fixing unread channels and threads
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After importing, all messages may appear as unread for users. To resolve this issue, run the following SQL queries directly against the Mattermost database:

.. code-block:: sql

   begin;
   UPDATE channelmembers
   SET
       msgcount = channels.totalmsgcount,
       lastupdateat = channels.lastpostat,
       lastviewedat = channels.lastpostat,
       msgcountroot = channels.totalmsgcountroot
   FROM channels
   WHERE channelmembers.channelid = channels.id;

   INSERT INTO preferences (UserId, Category, Name, Value)
   SELECT
       cm.userid,
       'channel_approximate_view_time',
       cm.channelid,
       cm.lastupdateat
   FROM
       channelmembers cm
   ON CONFLICT (userid, category, name)
   DO UPDATE SET
       Value = EXCLUDED.Value;

   update preferences
     set value = false
     where category = 'direct_channel_show';

   update preferences
     set value = false
     where category = 'group_channel_show';

   commit;

Additional tools
^^^^^^^^^^^^^^^^

* `mm-emoji <https://github.com/users/maxwellpower/packages/container/package/mm-emoji>`__ - Designed to smoothly transition emojis from a Slack instance to Mattermost.
* `mm-importjs <https://github.com/mickmister/mmimportjs>`__ - Breaks up large import files into smaller ones, as well as automatically remove null characters in post content when importing data to Mattermost.
* `slack-migrate-pinned-posts <https://github.com/svelle/slack-migrate-pinned-posts>`__ - Migrates pinned posts from Slack to Mattermost.

Address placeholder emails
^^^^^^^^^^^^^^^^^^^^^^^^^^

During the import process, the emails and usernames from Slack are used to create new Mattermost accounts. If emails are not present in the Slack export archive, then placeholder values will be generated and the system admin will need to update these manually. We recommend administrators search the final import ``jsonl`` file for ``user`` lines with ``@example.com`` in the email property to address and resolve the missing information prior to import.

Email verification behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The email verification process during Slack import depends on who performs the import:

**System administrator imports:**

* Email addresses are automatically verified during the import process.
* Users can immediately use the **Password Reset** feature to set their password.
* No email verification steps are required before password reset.

**Non-administrator imports:**

* Email addresses remain unverified after import.
* Users must first verify their email addresses before they can reset their password.
* Additional email verification steps are required before account access.

Account activation
~~~~~~~~~~~~~~~~~~

* Slack users activate their new Mattermost accounts by using Mattermost's **Password Reset** screen with their email addresses from Slack to set new passwords for their Mattermost accounts. See the instructions on how to :ref:`migrate user authenticatation to LDAP or SAML <administration-guide/manage/mmctl-command-line-tool:mmctl user migrate-auth>`.

  * For imports performed by System Admins: Users can immediately use the **Password Reset** feature (no email verification is required).
  * For imports performed by non-administrators: Users must first verify their email addresses, then use the **Password Reset** feature.

* Once logged in, Mattermost users will have access to previous Slack messages in the public channels imported from Slack.

FAQ
---

What additional conderations are there for Slack Enterprise Grid?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Slack Enterprise Grid combines multiple workspaces under a single management plane and the associate export reflect that complexity. An Enterprise Grid export is a single archive containing all workspaces and shared channels.

Mattermost does not support shared channels between teams, so Slack Shared Channels must be mapped to a single team in Mattermost. We can create this mapping by determining the originating teams in Slack and creating a ``team.json`` mapping file for use with ``mmetl``. Because of the manual effort required to identify and map team IDs, Enterprise Grid migrations are typically more time-consuming than single-workspace migrations. Plan additional time and resources to complete this step successfully.

Export structure
^^^^^^^^^^^^^^^^

At the root level, you’ll see shared channels that span across Slack workspaces, and under ``/teams/`` you’ll find per-workspace data such as channels and users files. A typical structure looks like:

.. code-block:: text

   Enterprise Grid Export/
   ├── channel1/
   │   ├── 2023-01-01.json
   │   └── 2023-01-02.json
   ├── channel2/
   │   ├── 2023-05-01.json
   │   └── 2023-05-02.json
   ├── teams/
   │   ├── team1/
   │   │   ├── channel3/
   │   │   │   ├── 2023-05-01.json
   │   │   │   └── 2023-05-02.json
   │   │   ├── channels.json
   │   │   ├── mpims.json
   │   │   ├── dms.json
   │   │   ├── users.json
   │   │   └── groups.json
   │   └── team2/
   │       ├── channel4/
   │       │   ├── 2023-05-01.json
   │       │   └── 2023-05-02.json
   │       ├── channels.json
   │       ├── mpims.json
   │       ├── dms.json
   │       ├── users.json
   │       └── groups.json
   ├── channels.json
   ├── org_users.json
   ├── mpims.json
   ├── dms.json
   └── groups.json

Mapping shared channels to Mattermost teams
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Download the full Enterprise Grid export from Slack.

2. To determine where each shared channel belongs in Mattermost, looks for a ``team`` attribute on the first post in each shared channel. These ``team`` values map the channel back to its originating workspace in Slack. This is where each shared channel will live in Mattermost once imported.

  .. code-block:: json

    {
      "client_msg_id": "",
      "type": "",
      "text": "",
      "user": "U1",
      "ts": "1695219722.430309",
      "blocks": [  ],
      "team": "team1",
      "user_team": "team1",
      "source_team": "team1",
      "user_profile": { }
    },

3. Create a ``teams.json`` file that maps Slack team IDs to each ``team`` attribute you found above. For example:

  .. code-block:: json

    {
        "T0001" : "team1",
        "T0002" : "team2"
    }

4. Run the ``mmetl grid-transform`` command to split the Enterprise Grid export into per-team files:

  .. code-block:: bash

    ./mmetl grid-transform -f slackexport.zip -t teams.json

This process outputs a new archive for each team defined in ``teams.json``. Once split, you can continue the standard Mattermost import process on each file.

Are there features of Slack that are not supported for migration to Mattermost?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Slack import process focuses on preserving core collaboration data such as messages, files, channels, and users. However, certain Slack features are not supported by the Mattermost product and thus will not be migrated using the import tools in this document:

- **Slack apps and integrations**: Installed apps, bots, slash commands, webhooks, workflow builder and other integrations do not migrate. Most integrations supported by Slack can be recreated using the :doc:`integration and automation </integrations-guide/integrations-guide-index>` options in Mattermost.
- **Stared conversations**: Starred conversations are not preserved.
- **User groups**: User groups from Slack are not preserved, however they can be recreated in Mattermost using the :doc:`Custom Groups </end-user-guide/collaborate/organize-using-custom-user-groups>` feature.
- **Threaded Converations**: Slack threads are mostly supported, however some threading relationships may not always be preserved given the differences in how Mattermost and Slack threading works.
- **Canvases**: Canvases are not supported in Mattermost and will not be migrated.
- **User presence and profiles**: User status (online/away), profile pictures, and custom profile fields do not carry over. Users will need to update their profiles in Mattermost.
- **Channel memberships for deactivated users**: Deactivated or deleted Slack users are not migrated to Mattermost.

Because of these limitations, some manual reconfiguration is typically required after the import, especially for workflows and integrations. Support from a `Mattermost expert is available <https://mattermost.com/contact-sales/>`_ for your Slack migration.
