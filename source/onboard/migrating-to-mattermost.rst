Migration guide
===============

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Thousands of organizations are moving to Mattermost for powerful, flexible, and easy-to-manage workplace collaboration. Mattermost deploys as a single Linux binary with PostgreSQL, and can scale from dozens to tens of thousands of users in a single channel.

This guide summarizes different approaches to migrating to Mattermost from other tools, including `Slack <#migrate-from-slack>`__, `HipChat <migrate-from-hipchat>`__, `Jabber <#migrate-from-jabber>`__, `Pidgin <#migrate-from-pidgin>`__, `Bitnami <#migrate-from-bitnami>`__, and other `bespoke messaging solutions <#migrate-from-bespoke-messaging-solutions>`__, as well as `migrating Mattermost server <#migrate-mattermost-server>`__ to another server instance.

.. contents:: On this page
  :backlinks: top
  :depth: 2

----

Migrate from Slack
------------------

To migrate from Slack to Mattermost involves the following steps:

- `Prepare your Mattermost server <#prepare-your-mattermost-server>`__
- `Generate a Slack import <#generate-a-slack-import>`__
- `Download file attachments and email addresses <#download-file-attachments-and-email-addresses>`__
- `Convert the Slack import to Mattermost's format <#convert-slack-import-to-mattermost-s-bulk-export-format>`__
- `Import data into Mattermost <#import-data-into-mattermost>`__

1. Prepare your Mattermost server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We recommend you create a separate team in Mattermost for each of your Slack workspaces.

You can import two workspaces into the same team, but you'll need to ensure there are no channel name collisions first. Make sure that all users in Mattermost have the same username as in Slack, otherwise the import will fail.

Also, system administrator roles will be overwritten if the usernames match and the user isn't an admin on the Slack workspace.

2. Generate a Slack import
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Slack offers two ways to `export your data from their product <https://get.slack.help/hc/en-us/articles/201658943-Export-your-workspace-data>`_.

1. Regular export - Contains only public channel posts. This does not include private channels, DMs, or group conversations. This can be generated from **Slack > Administration > Workspace settings > Import/Export Data > Export > Start Export**.
2. Corporate export - Contains all posts. This includes public channels, private channels, DMs and group messages. You must `request this export type from Slack directly <https://slack.com/help/articles/1500001548241-Request-to-export-all-conversations>`__.

You will receive a zip file containing the following contents. 

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you download your Slack export zip file, few pieces of data will be missing from the zip file:
- Emails of users
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

  slack-advanced-exporter --input-archive <SLACK EXPORT FILE> --output-archive export-with-emails.zip fetch-emails --api-token <SLACK TOKEN>
  slack-advanced-exporter --input-archive export-with-emails.zip --output-archive export-with-emails-and-attachments.zip fetch-attachments

.. note::

  - You'll end up with two files, ``export-with-emails.zip`` and ``export-with-emails-and-attachments.zip``. The file ``export-with-emails.zip`` won't include attachments.
  - The second command can take a long time if you have a large number of file uploads. If it's interrupted, delete the file generated (if any), and start again.

The file ``export-with-emails-and-attachments.zip`` now contains all the information necessary to be imported into Mattermost.

Michael K Note:
> This section caused the customer confusion because they always asked if they needed both emails and attachments.

From the slack advanced exporter repo:
Due to archive/zip limitations, these actions cannot modify archive in place. It's preferable to fetch e-mails first to avoid copying large attachments around.

.. important::

  Avoid unzipping and rezipping the Slack export. Doing so can modify the directory structure of the archive which could cause issues with the import process.

4. Convert Slack import to Mattermost's bulk export format
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that you have a Slack export file with emails and attachments, let's convert this information into Mattermost's bulk import format using the import preparation tool ``mmetl``. Download the latest release of ``mmetl`` for your OS and architecture `here <https://github.com/mattermost/mmetl/releases/>`__. Run ``mmetl help`` to learn more about using the tool.

Next, run the following command to create a Mattermost bulk import file. Replace ``<TEAM NAME>`` with the name of your team in Mattermost:

.. code:: bash

    ./mmetl transform slack --team <TEAM NAME> --file export-with-emails-and-attachments.zip --output mattermost_import.jsonl

Michael K Note:
I don't understand the below pre-existing paragraph. I'm not sure what the zip file structure is after slack advanced export
https://github.com/grundleborg/slack-advanced-exporter/blob/c0f7bf8230cd15d9b44af36d73ce8f0650538c67/cmd/fetch_attachments.go#L148
It looks like we place them in a folder called ``__uploads``
but it's my understanding that we should make a ``data`` folder. I'm not sure what ``bulk-export-attachments`` is representing below. I need to look into this more.
I need to go through this part of the process. I generated a slack export, but it doesn't contain posts for "today", so I don't have the available info

Next you have to create a zip file with the ``mattermost_import.jsonl`` file and the directory ``bulk-export-attachments`` (which needs to be moved to a subdirectory ``data`` first) that contains the attachments. On Linux and macOS you can use this command:

The tool outputs a `.jsonl` file https://jsonlines.org/examples. We now need to place this file and attachments into a new zip file. Place this output file in the root directory of the zip file.

Michael K note:
it doesn't matter what th `.jsonl` file is called
you can name it what you want with the `--output` flag as shown above
it just needs to be a `.jsonl` file and be in the root directory of the zip file
this is a point of confusion, since there is no clear understanding of what the name of the files needs to be

.. code:: bash

  zip -r mattermost-bulk-import.zip data mattermost_import.jsonl

The file ``mattermost-bulk-import.zip`` is now ready to import into Mattermost.

5. Import data into Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We have two options to run the import process:

1. SSH into the Mattermost server's host, upload the export file to this server's file system somehow, and use the ``mattermost`` command to process the export file.
2. Uploading the export through Mattermost's API, via command line ``mmctl`` from the server or from another computer.

Note that for the second option, the server will save the import in its file store before running the import (e.g. AWS S3 if you are using that are your file store), so there will be time spent uploading/downloading the file in this case. Since this is really just a one-time thing to import this file, we recommend the first option of running it on the server itself if you have a large export zip file.

Note that the migration is idempotent, meaning that you can run multiple imports that contain the same posts, and there will not be duplicated created posts in Mattermost. Each post is imported with the correct user/author and `created_at` value from your Slack instance. Threads are kept in tact with the import.

Option 1: Use the ``mattermost`` command to run the export
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First get the export file onto your server using something like ``scp``

Use the server executable named ``mattermost`` to run the export with the command:

.. code:: bash
    mattermost bulk import

Michael K Note:
need to fill in other details here for Option 1

Option 2: Upload export via ``mmctl``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ensure you have the Mattermost command line tool ``mmctl`` installed. This allows you to perform different tasks that communicate to Mattermost's API.

Once you have ``mmctl`` installed and authenticated, use this command to upload ``mattermost-bulk-import.zip``:

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

Debug imports
`````````````

The ``mmctl import job show`` shows a detailed error message. If you run into problems which the error message does not help to resolve, please try the first option of using the ``mattermost bulk import`` command. The ``mmctl`` import process does not give you any additional debugging information, even in the Mattermost server logs.

Additional tools
`````````````````

* `mm-emoji <https://github.com/maxwellpower/mm-emoji>`__ - Designed to smoothly transition emojis from a Slack instance to Mattermost.
* `mm-importjs <https://github.com/mickmister/mmimportjs>`__ - Breaks up large import files into smaller ones, as well as automatically remove null characters in post content when importing data to Mattermost.
* `slack-migrate-pinned-posts <https://github.com/svelle/slack-migrate-pinned-posts>`__ - Migrates pinned posts from Slack to Mattermost.

Use the imported team
`````````````````````

* During the import process, the emails and usernames from Slack are used to create new Mattermost accounts. If emails are not present in the Slack export archive, then placeholder values will be generated and the system admin will need to update these manually.
* Slack users can activate their new Mattermost accounts by using Mattermost's **Password Reset** screen with their email addresses from Slack to set new passwords for their Mattermost accounts.
* Once logged in, Mattermost users will have access to previous Slack messages in the public channels imported from Slack.

Migrate from HipChat 
--------------------

See `HipChat Migration Guide </onboard/migrating-from-hipchat-to-mattermost.html>`__ for details on migrating from HipChat Server and HipChat Data Center to Mattermost.

Migrate from Jabber
-------------------

BrightScout helped a major U.S. Federal Agency rapidly migrate from Jabber to Mattermost and open sourced their Extract, Transform and Load (ETL) tool at https://github.com/Brightscout/mattermost-etl. Read more about their `case study <https://mattermost.com/blog/u-s-federal-agency-migrates-from-jabber-to-mattermost-the-open-source-way/>`__ online.

----

Migrate from Pidgin
-------------------

In some cases, people are using Pidgin clients with different backends to communicate. To continue using Pidgin with a Mattermost backend, consider using `Mattermost ETL tool <https://github.com/Brightscout/mattermost-etl>`__, created by BrightScout, to migrate data from your existing backend into Mattermost. 

Then use the `Pidgin-Mattermost plugin <https://github.com/EionRobb/purple-mattermost>`__ (complete with an installer for end user machines) to continue to support legacy Pidgin users while offering a whole new Mattermost experience on web, mobile, and PC.

----

Migrate from Bitnami
--------------------

Bitnami uses MySQL, and renames the Mattermost database tables by converting the names to all lower case. For example, in non-Bitnami installations, the Users table is named ``Users``, but in Bitnami, the table is ``users`` (with a lowercase ``u``). As a result, when you migrate your data from Bitnami to a non-Bitnami installation, you must modify the MySQL startup script so that it starts MySQL in lowercase table mode.

You can modify the script by adding the ``--lower-case-table-names=1`` switch to the MySQL start command. The location of the start-up script generally depends on how you installed MySQL, whether by using the package manager for the operating system, or by manually installing MySQL. You must modify the start-up script before migrating the data.

For more information about letter case in MySQL table names and the ``--lower-case-table-names`` switch, see the `Identifier Case Sensitivity <https://dev.mysql.com/doc/refman/5.7/en/identifier-case-sensitivity.html>`__ topic in the MySQL documentation.

----

Migrate from bespoke messaging solutions
-----------------------------------------

Mattermost is often selected to replace bespoke solutions by IT and DevOps teams as a stable, enterprise-grade, commercially-supported solution on an open source platform that meets and exceeds the flexibility and innovation of bespoke solutions.

Migrating from bespoke messengers to Mattermost can be challenging. Because of the difficulty of upgrading and maintaining bespoke solutions, the format for storing data is unpredictable, and the community around any single legacy release is small.

If your data in the bespoke messenger is vital, consider:

1. `Mattermost bulk load tool </onboard/bulk-loading-data.html>`__: Use the Mattermost bulk load tool to ETL from your bespoke system to Mattermost.
2. `Mattermost ETL framework from BrightScout <https://github.com/Brightscout/mattermost-etl>`__: Consider the Mattermost ETL framework from BrightScout to custom-configure an adapter to plug in to the Bulk Load tool mentioned above.
3. **Legacy Slack import:** If you only recently switched from Slack to a bespoke tool, consider going back to import the data and users from the old Slack instance directly into Mattermost, leveraging the extensive support for Slack-import provided.
4. **Export to Slack, then import to Mattermost:** `Export HipChat, Flowdock, Campfire, Chatwork, Hall, or CSV files to Slack <https://get.slack.help/hc/en-us/articles/201748703-Import-message-history>`__ and then export to a Slack export file and import the file into Mattermost.

If your data in the bespoke messenger is not vital, consider:

1. **Parallel systems:** Running Mattermost in parallel with your bespoke system until the majority of workflow and collaboration has moved to Mattermost
2. **Hard switch:** Announce a "hard switch" to Mattermost after a period of time of running both systems in parallel. Often this has been done due to security concerns in bespoke products or products nearing end-of-life.

Sometimes systems running in parallel turn into a hard switch migration when a bespoke or deprecated system experiences a major outage or a security exploit. In 2017, this was experienced by many companies using Mattermost and HipChat.com in parallel when `HipChat suffered a major security breach where customer data was stolen by an unknown attacker <https://thenextweb.com/insider/2017/04/24/hipchat-hacked-weekend-bad/#.tnw_lAotA9OV>`__.

When IT adopts management of Mattermost, often they will purchase the commercial version for additional compliance, access control, and scale features, in addition to high quality commercial support for upgrades and migrations. Teams can `purchase Mattermost Enterpise Edition with a credit card online <https://mattermost.com/pricing-self-managed/>`__ or `contact sales <https://mattermost.com/contact-us/>`__ to engage in an enterprise procurement process.

Why IT teams choose to leave bespoke solutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Because messaging solutions in technical teams often contain confidential and highly exploitable data, messaging solutions become a security concern that could impact all of an organization's technical infrastructure.

When IT teams are asked to maintain a bespoke messaging solution, they often need to consider security issues such as the following:

1. Is the solution backed by a commercial entity with significant legal obligations to ensure the safety and security of the product?
2. Is there a security bulletin available to alert our organization of high-priority security updates, with clear instructions to apply the updates?
3. Does the solution have a clear and up-to-date list of security updates?
4. Are security updates released prior to detailed disclosure of vulnerability details, so as to provide our organization with time to apply security updates before vulnerabilities are widely known?
5. In addition to internal testing, is there a Responsible Disclosure Policy for external security researchers to confidentially report security issues, and a recognition program for their contributions?

Bespoke communication products that provide weak security assurance can dramatically increase the risk to IT teams and their organizations.

When early adopters of a bespoke solutions ask IT to "take over" and assume the risk of managing a rapidly installed, difficult-to-maintain system with limited or no assurance of security, the IT team is under a great deal of pressure.

Often at this point, IT teams accelerate their exploration of Mattermost as a long-term solution, given the `thousands of organizations (many in mission critical, high security industries) that have switched <https://mattermost.com/customers/>`__.

Why IT teams choose Mattermost over bespoke solutions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mattermost is designed to replace bespoke messaging solutions through a platform that is unmatched in flexibility. From the `hundreds of open source projects extending and customizing Mattermost through APIs and drivers <https://github.com/search?utf8=✓&q=mattermost&type=>`__, to an innovative client and server plugin framework for adapting the Mattermost user experience to the specific workflows and needs, thousands of high performance teams rely on Mattermost daily.

In addition, IT teams prefer Mattermost for its specific `security assurances </about/security.html>`__:

1. Mattermost products are backed by Mattermost, Inc., which has commercial contracts with hundreds of enterprises around the world, many with Fortune 500 and Global 2000 organizations who require significant obligations and assurances from vendors of critical infrastructure.
2. Mattermost offers a `security bulletin <https://mattermost.com/security-updates/#sign-up>`__ to alert IT teams and customers of high priority security updates, with step-by-step instructions for upgrade and options for commercial support.
3. Mattermost maintains an `up-to-date list of security updates <https://mattermost.com/security-updates/>`__ for both its open source and commercial offerings.
4. To keep IT teams safe, Mattermost waits 14 days after releasing a security patch before disclosing the specific details of the vulnerability each addresses.
5. A `Responsible Disclosure Policy <https://mattermost.com/security-vulnerability-report/>`__ is available to supplement internal security reviews with confidential reports from external security researchers, with a recognition program for security research contributions after the security patch is properly released.

----

Migrate Mattermost server
-------------------------

The following instructions migrate Mattermost from one server to another by backing up and restoring the Mattermost database and ``config.json`` file. For these instructions SOURCE refers to the Mattermost server *from which* your system will be migrated and DESTINATION refers to the Mattermost server *to which* your system will be migrated.

1. Back up your SOURCE Mattermost server. See `Backup and Disaster Recovery documentation </deploy/backup-disaster-recovery.html>`__.
2. Upgrade your SOURCE Mattermost server to the latest major build version. See `Upgrading Mattermost Server documentation </upgrade/upgrading-mattermost-server.html>`__.
3. Install the latest major build of Mattermost server as your DESTINATION. 

  - Make sure your new instance is properly configured and tested. The database type (MySQL or PostgreSQL) and version of SOURCE and DESTINATION deployments need to match.
  - Stop the DESTINATION server using ``sudo stop mattermost``, then back up the database and ``config.json`` file.

4. Migrate database from SOURCE to DESTINATION. Backup the database from the SOURCE Mattermost server and restore it in place of the database to which the DESTINATION server is connected.
5. Migrate ``config.json`` from SOURCE to DESTINATION. Copy ``config.json`` file from SOURCE deployment to DESTINATION.
6. If you use local storage (``FileSettings.DriverName`` is set to ``local``), migrate ``./data`` from SOURCE to DESTINATION.

  - Copy the ``./data`` directory from SOURCE deployment to DESTINATION.
  - If you use a directory other than ``./data``, copy that directory instead.
7. Start the DESTINATION deployment by running ``sudo start mattermost``. Then go to the **System Console**, make a minor change, and save it to upgrade your ``config.json`` schema to the latest version using default values for any new settings added.
8. Test that the system is working by going to the URL of an existing team. You may need to refresh your Mattermost browser page in order to get the latest updates from the upgrade.

Once your migration is complete and verified, you can optionally `upgrade the Team Edition of Mattermost to Enterprise Edition using the upgrade guide </upgrade/upgrading-mattermost-server.html#upgrading-team-edition-to-enterprise-edition>`__.