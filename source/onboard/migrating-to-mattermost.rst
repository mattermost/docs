Migration guide
===============

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Thousands of organizations are moving to Mattermost for powerful, flexible, and easy-to-manage workplace collaboration. Mattermost deploys as a single Linux binary with PostgreSQL, and can scale from dozens to tens of thousands of users in a single channel.

This guide summarizes different approaches to migrating from one Mattermost deployment to another, and migrating from other tools (such as Slack, HipChat, Jabber, and bespoke solutions) to Mattermost.

.. contents:: On this page
  :backlinks: top
  :depth: 1
  :local:

Migrate Mattermost server
-------------------------

The following instructions migrate Mattermost from one server to another by backing up and restoring the Mattermost database and ``config.json`` file. For these instructions **SOURCE** refers to the Mattermost server *from which* your system will be migrated and **DESTINATION** refers to the Mattermost server *to which* your system will be migrated.

1. Back up your SOURCE Mattermost server. See `Backup and Disaster Recovery documentation </deploy/backup-disaster-recovery.html>`__.
2. Upgrade your SOURCE Mattermost server to the latest major build version. See `Upgrading Mattermost Server documentation </upgrade/upgrading-mattermost-server.html>`__.
3. Install the latest major build of Mattermost server as your DESTINATION. See `Install Mattermost documentation </guides/install-deploy-upgrade-scale.html#install-mattermost>`__ for details. 

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

Migrate to Mattermost from bespoke messaging solutions
-------------------------------------------------------

Many enterprises run bespoke, unsupported, lightly documented messaging systems driven by the initial excitement of the product's promise.

Often the solutions were championed by tech-savvy early adopters who loved a few features and pushed out the solution broadly.

Over time, management moves to an IT team, where an unsupported solution becomes problematic to maintain and secure. Mattermost is often selected to replace bespoke solutions by IT and DevOps teams as a stable, enterprise-grade, commercially-supported solution on an open source platform that meets and exceeds the flexibility and innovation of bespoke solutions.

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

Bring data from bespoke solutions into Mattermost 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Migrate from Slack
------------------

Slack offers two ways to `export your data from their product <https://get.slack.help/hc/en-us/articles/201658943-Export-your-workspace-data>`_.

1. A Slack export file can be generated from **Slack > Administration > Workspace settings > Import/Export Data > Export > Start Export**. This export does not include private channels, direct, or group messages.
2. You can request a "Corporate Export" from Slack directly to get a larger export including private channels, direct, and group messages.

.. note::

  As a proprietary SaaS service, Slack is able to change its export format quickly and without notice. If you encounter issues not mentioned in the following documentation, please let the Mattermost Product Team know by `filing an issue <https://handbook.mattermost.com/contributors/contributors/ways-to-contribute>`__.

Use the Mattermost mmetl tool and bulk import
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This method is the recommended way to import Slack's corporate export file, but will work with any Slack export file.

1. Prepare your Mattermost server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We recommend you create a new team in Mattermost to hold the imported Slack data. You can import this into an existing team, but ensure there are no channel name collisions. Also, make sure that all users in Mattermost have the same username as in Slack, otherwise the import will fail. Also, system administrator roles will be overwritten if the usernames match and the user isn't an admin on the Slack workspace.

2. Generate a Slack import
^^^^^^^^^^^^^^^^^^^^^^^^^^

The first step is to generate a `Slack export <https://slack.com/help/articles/201658943-Export-your-workspace-data>`_.

.. note::

  Make sure not to unzip and rezip the Slack export. Doing that can modify the directory structure of the archive which could cause issues with the import process.

Next, follow these steps to create a bot token:

1. Go to https://api.slack.com/apps.
2. Select **Create New App**.
3. Select **From scratch**.
4. Name the app something like "Slack Advanced Exporter" and select the workspace. You'll have to do this for every workspace. Then create the app.
5. Select **OAuth & Permissions** and scroll down to **Scopes**.
6. Under **Bot Token Scopes** select ``users:read`` and ``users:read.email``.
7. Scroll up and select **Install to Workspace**.
8. Grant the app permissions.
9. Copy the Bot User OAuth Token and save it somewhere convenient.

3. Download file attachments and email addresses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Slack export does not include file attachments and email addresses, so you must use ``slack-advanced-exporter`` to download them. Download the latest release of ``slack-advanced-exporter`` for your OS and architecture `here <https://github.com/grundleborg/slack-advanced-exporter/releases/>`__ and extract it.

Once it's installed, run these commands. Replace ``<SLACK TOKEN>`` with the Slack token you generated earlier and ``<SLACK EXPORT FILE>`` with the `path <https://www.geeksforgeeks.org/absolute-relative-pathnames-unix/>`__ to your file.

.. note::

    - You'll end up with two files (``export-with-emails.zip`` and ``export-with-emails-and-attachments.zip``). The file ``export-with-emails.zip`` will not have attachments.
    - The second command can take a long time if you have a large number of file uploads. If it's interrupted, delete the file generated (if any), and start again.

.. code:: bash

    slack-advanced-exporter --input-archive <SLACK EXPORT FILE> --output-archive export-with-emails.zip fetch-emails --api-token <SLACK TOKEN>
    slack-advanced-exporter --input-archive export-with-emails.zip --output-archive export-with-emails-and-attachments.zip fetch-attachments

The file ``export-with-emails-and-attachments.zip`` now contains all the information necessary to be imported into Mattermost.

4. Convert Slack import to Mattermost bulk export format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that you have a Slack export file with emails and attachments you have to convert it to the Mattermost format using ``mmetl``. Download the latest release of ``mmetl`` for your OS and architecture `here <https://github.com/mattermost/mmetl/releases/>`__ and extract it to your $PATH like with ``slack-advanced-exporter``. The same caveat applies.

Next, run this command to do the conversion. Replace ``<TEAM NAME>`` with the name of your team:

.. code:: bash

    ./mmetl transform slack --team <TEAM NAME> --file export-with-emails-and-attachments.zip --output mattermost_import.jsonl

Next you have to create a zip file with the ``mattermost_import.jsonl`` file and the directory ``bulk-export-attachments`` (which needs to be moved to a subdirectory ``data`` first) that contains the attachments. On Linux and macOS you can use this command:

.. code:: bash

    zip -r mattermost-bulk-import.zip data mattermost_import.jsonl

The file ``mattermost-bulk-import.zip`` is now ready to import into Mattermost.

5. Import into Mattermost
^^^^^^^^^^^^^^^^^^^^^^^^^

Now you can start the import process. Once you have ``mmctl`` installed and authenticated use this command to upload ``mattermost-bulk-import.zip``:

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

Debugging imports
^^^^^^^^^^^^^^^^^

The ``mmctl import job show`` shows a detailed error message. If you run into problems which the error message does not help to resolve, your best bet is to use the ``mattermost bulk import`` command. The ``mmctl`` import process does not give you any additional debugging information, even in the Mattermost server logs.

Additional tools
^^^^^^^^^^^^^^^^

* `mm-emoji <https://github.com/maxwellpower/mm-emoji>`__ - Designed to smoothly transition emojis from a Slack instance to Mattermost.
* `mm-importjs <https://github.com/mickmister/mmimportjs>`__ - Breaks up large import files into smaller ones, as well as automatically remove null characters in post content when importing data to Mattermost.
* `slack-migrate-pinned-posts <https://github.com/svelle/slack-migrate-pinned-posts>`__ - Migrates pinned posts from Slack to Mattermost.

Use the Mattermost web app (deprecated)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important::
  The ability to migrate from Slack using the Mattermost web app has been deprecated and removed in favor of using the `Mattermost mmetl tool with bulk import <#use-the-mattermost-mmetl-tool-and-bulk-import>`_.

1. Generate a Slack export file from **Slack > Administration > Workspace Settings > Import/Export Data > Export > Start Export**. Alternatively, use the Slack Corporate Export file after receiving it from Slack.
2. In Mattermost go to **Main Menu > Team Settings > Import > Import from Slack**. Team admin or system admin permission is required to access this menu option.
3. Choose **Select file** to upload the Slack export file and select **Import**.

Use the imported team
^^^^^^^^^^^^^^^^^^^^^^

* During the import process, the emails and usernames from Slack are used to create new Mattermost accounts. If emails are not present in the Slack export archive, then placeholder values will be generated and the system admin will need to update these manually.
* Slack users can activate their new Mattermost accounts by using Mattermost's **Password Reset** screen with their email addresses from Slack to set new passwords for their Mattermost accounts.
* Once logged in, Mattermost users will have access to previous Slack messages in the public channels imported from Slack.

Migrate from Bitnami
--------------------

Bitnami uses MySQL, and renames the Mattermost database tables by converting the names to all lower case. For example, in non-Bitnami installations, the Users table is named "Users", but in Bitnami, the table is "users". As a result, when you migrate your data from Bitnami to a non-Bitnami installation, you must modify the MySQL startup script so that it starts MySQL in lowercase table mode.

You can modify the script by adding the ``--lower-case-table-names=1`` switch to the MySQL start command. The location of the start-up script generally depends on how you installed MySQL, whether by using the package manager for the operating system, or by manually installing MySQL. You must modify the start-up script before migrating the data.

For more information about letter case in MySQL table names and the ``--lower-case-table-names`` switch, see the `Identifier Case Sensitivity <https://dev.mysql.com/doc/refman/5.7/en/identifier-case-sensitivity.html>`__ topic in the MySQL documentation.

Migrate from HipChat Server and HipChat Data Center to Mattermost
------------------------------------------------------------------

Please see `HipChat Migration Guide </onboard/migrating-from-hipchat-to-mattermost.html>`__.

Migrate from Jabber to Mattermost
---------------------------------

BrightScout helped a major U.S. Federal Agency rapidly migrate from Jabber to Mattermost and open sourced their Extract, Transform and Load (ETL) tool at https://github.com/Brightscout/mattermost-etl.

Read more about their `case study <https://mattermost.com/blog/u-s-federal-agency-migrates-from-jabber-to-mattermost-the-open-source-way/>`__ online.

Migrate from Pidgin to Mattermost
---------------------------------

In some cases people are using Pidgin clients with different backends to communicate. To continue using Pidgin with a Mattermost backend consider using `Mattermost ETL tool <https://github.com/Brightscout/mattermost-etl>`__ created by BrightScout to migrate data from your existing backend into Mattermost, then use the `Pidgin-Mattermost plugin <https://github.com/EionRobb/purple-mattermost>`__ (complete with an installer for end user machines) to continue to support legacy Pidgin users while offering a whole new Mattermost experience on web, mobile, and PC.
