Migration Guide
===============

Thousands of organizations are moving to Mattermost for powerful, flexible, and easy-to-manage workplace collaboration. Mattermost deploys as a single Linux binary with MySQL or PostgreSQL, and can scale from dozens to tens of thousands of users in a single channel.

This guide summarizes different approaches to migrating from one Mattermost deployment to another, and migrating from other messenger tools (such as Slack, HipChat, Jabber, and bespoke solutions) to Mattermost.

.. contents::
  :backlinks: top
  :local:

Migrating the Mattermost Server
-------------------------------

The following instructions migrate Mattermost from one server to another by backing up and restoring the Mattermost database and ``config.json`` file. For these instructions **SOURCE** refers to the Mattermost server *from which* your system will be migrated and **DESTINATION** refers to the Mattermost server *to which* your system will be migrated.

1. Back up your SOURCE Mattermost server.
    1. See `Backup Guide <https://docs.mattermost.com/administration/backup.html>`__.
2. Upgrade your SOURCE Mattermost server to the latest major build version.
    1. See `Mattermost Upgrade Guide <https://docs.mattermost.com/guides/administrator.html#upgrade-mattermost>`__.
3. Install the latest major build of Mattermost server as your DESTINATION.
    1. See `Installing Mattermost <https://docs.mattermost.com/guides/administrator.html#installing-mattermost>`__ for install guides. Make sure your new instance is properly configured and tested. The database type (MySQL or PostgreSQL) and version of SOURCE and DESTINATION deployments need to match.
    2. Stop the DESTINATION server using ``sudo stop mattermost``, then back up the database and ``config.json`` file.
4. Migrate database from SOURCE to DESTINATION.
    1. Backup the database from the SOURCE Mattermost server and restore it in place of the database to which the DESTINATION server is connected.
5. Migrate ``config.json`` from SOURCE to DESTINATION.
    1. Copy of ``config.json`` file from SOURCE deployment to DESTINATION.
6. If you use local storage (``FileSettings.DriverName`` is set to ``local``), migrate ``./data`` from SOURCE to DESTINATION.
    1. Copy the ``./data`` directory from SOURCE deployment to DESTINATION.
    2. If you use a directory other than ``./data``, copy that directory instead.
7. Start the DESTINATION deployment.
    1. Run ``sudo start mattermost``.
    2. Go to the **System Console**, make a minor change, and save it to upgrade your ``config.json`` schema to the latest version using default values for any new settings added.
8. Test that the system is working by going to the URL of an existing team.
    1. You may need to refresh your Mattermost browser page in order to get the latest updates from the upgrade.

Once your migration is complete and verified, you can optionally `upgrade the Team Edition of Mattermost to Enterprise Edition using the upgrade guide <https://docs.mattermost.com/administration/upgrade.html#upgrade-team-edition-to-enterprise-edition>`__.

Migrating to Mattermost From Other Messaging Solutions
------------------------------------------------------

Migrating From Bespoke Messaging Solutions to Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many enterprises run bespoke, unsupported, lightly documented messaging systems driven by the initial excitement of the product's promise.

Often the solutions were championed by tech-savvy early adopters who loved a few features and pushed out the solution broadly.

Over time, management moves to an IT team, where an unsupported solution becomes problematic to maintain and secure. Mattermost is often selected to replace bespoke solutions by IT and DevOps teams as a stable, enterprise-grade, commercially-supported solution on an open source platform that meets and exceeds the flexibility and innovation of bespoke solutions.

Why IT Teams Choose to Leave Bespoke Solutions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Why IT Teams Choose Mattermost over Bespoke Solutions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost is designed to replace bespoke messaging solutions through a platform that is unmatched in flexibility. From the `hundreds of open source projects extending and customizing Mattermost through APIs and drivers <https://github.com/search?utf8=✓&q=mattermost&type=>`__, to an innovative client and server plugin framework for adapting the Mattermost user experience to the specific workflows and needs, thousands of high performance teams rely on Mattermost daily.

In addition, IT teams prefer Mattermost for its specific `security assurances <https://docs.mattermost.com/overview/security.html>`__:

1. Mattermost products are backed by Mattermost, Inc., which has commercial contracts with hundreds of enterprises around the world, many with Fortune 500 and Global 2000 organizations who require significant obligations and assurances from vendors of critical infrastructure.
2. Mattermost offers a `security bulletin <https://mattermost.com/security-updates/#sign-up>`__ to alert IT teams and customers of high priority security updates, with step-by-step instructions for upgrade and options for commercial support.
3. Mattermost maintains an `up-to-date list of security updates <https://mattermost.com/security-updates/>`__ for both its open source and commercial offerings.
4. To keep IT teams safe, Mattermost waits 14 days after releasing a security patch before disclosing the specific details of the vulnerability each addresses.
5. A `Responsible Disclosure Policy <https://mattermost.com/security-vulnerability-report/>`__ is available to supplement internal security reviews with confidential reports from external security researchers, with a recognition program for security research contributions after the security patch is properly released.

Bringing Data from Bespoke Solutions into Mattermost 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Migrating from bespoke messengers to Mattermost can be challenging. Because of the difficulty of upgrading and maintaining bespoke solutions, the format for storing data is unpredictable, and the community around any single legacy release is small.

If your data in the bespoke messenger is vital, consider:

1. `Mattermost Bulk Load tool <https://docs.mattermost.com/deployment/bulk-loading.html>`__: Use the Mattermost Bulk Load tool to ETL from your bespoke system to Mattermost.
2. `Mattermost ETL framework from BrightScout <https://github.com/Brightscout/mattermost-etl>`__: Consider the Mattermost ETL framework from BrightScout to custom-configure an adapter to plug in to the Bulk Load tool mentioned above.
3. **Legacy Slack import:** If you only recently switched from Slack to a bespoke tool, consider going back to import the data and users from the old Slack instance directly into Mattermost, leveraging the extensive support for Slack-import provided.
4. **Export to Slack, then import to Mattermost:** `Export HipChat, Flowdock, Campfire, Chatwork, Hall, or CSV files to Slack <https://get.slack.help/hc/en-us/articles/201748703-Import-message-history>`__ and then export to a Slack export file and import the file into Mattermost.

If your data in the bespoke messenger is not vital, consider:

1. **Parallel systems:** Running Mattermost in parallel with your bespoke system until the majority of workflow and collaboration has moved to Mattermost
2. **Hard switch:** Announce a "hard switch" to Mattermost after a period of time of running both systems in parallel. Often this has been done due to security concerns in bespoke products or products nearing end-of-life.

Sometimes systems running in parallel turn into a hard switch migration when a bespoke or deprecated system experiences a major outage or a security exploit. In 2017, this was experienced by many companies using Mattermost and HipChat.com in parallel when `HipChat suffered a major security breach where customer data was stolen by an unknown attacker <https://thenextweb.com/insider/2017/04/24/hipchat-hacked-weekend-bad/#.tnw_lAotA9OV>`__.

When IT adopts management of Mattermost, often they will purchase the commercial version for additional compliance, access control, and scale features, in addition to high quality commercial support for upgrades and migrations. Teams can `purchase Mattermost Enterpise Edition with a credit card online <https://mattermost.com/pricing-self-managed/>`__ or `contact sales <https://mattermost.com/contact-us/>`__ to engage in an enterprise procurement process.

Migrating from Slack
~~~~~~~~~~~~~~~~~~~~

Slack offers two ways to `export your data from their product <https://get.slack.help/hc/en-us/articles/201658943-Export-your-workspace-data>`_.

1. A Slack export file can be generated from **Slack > Administration > Workspace settings > Import/Export Data > Export > Start Export**. This export does not include private channels, direct, or group messages.
2. You can request a "Corporate Export" from Slack directly to get a larger export including private channels, direct, and group messages.

.. note::

  As a proprietary SaaS service, Slack is able to change its export format quickly and without notice. If you encounter issues not mentioned in the documentation below, please alert the product team by `filing an issue <https://mattermost.org/filing-issues/>`__.

Migrating from Slack Using the Mattermost mmetl Tool and Bulk Import
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
  
  This method is the recommended way to import Slack's corporate export file. It can be used with Mattermost v5.0 and onwards.

1. Use the `slack-advanced-exporter <https://github.com/grundleborg/slack-advanced-exporter>`_ to download attachments and add users' email addresses to your Slack corporate export file.
2. Use the `mmetl tool <https://github.com/mattermost/mmetl>`_ to transform Slack's corporate export file into the ``jsonl`` format required by the bulk import tool.
3. Bulk load the files using the steps provided in the `bulk loading documentation <https://docs.mattermost.com/deployment/bulk-loading.html#bulk-loading-data>`_.

Migrating from Slack using the Mattermost Web App
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
  
  For larger imports, particularly those where you have used the `slack-advanced-exporter tool` to add Slack post attachments to the archive or the Corporate Export file, it is recommended to import the Slack data using the `mmetl tool and bulk loading tool <https://docs.mattermost.com/administration/migrating.html#migrating-from-slack-using-the-mattermost-mmetl-tool-and-bulk-import>`__.

1. Generate a Slack export file from **Slack > Administration > Workspace Settings > Import/Export Data > Export > Start Export**. Alternatively, use the Slack Corporate Export file after receiving it from Slack.
2. In Mattermost go to **Main Menu > Team Settings > Import > Import from Slack**. Team Admin or System Admin permission is required to access this menu option.
3. Choose **Select file** to upload the Slack export file and select **Import**.

Migrating from Slack Using the Mattermost CLI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Generate a Slack export file from **Slack > Administration > Workspace Settings > Import/Export Data > Export > Start Export**.
2. Run the following Mattermost CLI command, with the name of a team you've already created:

   ``$ mattermost import slack team_name /path/to/your-slack-export.zip``
   
.. note::

  To run the CLI command, you must be in the directory that contains the Mattermost installation. On a default installation of Mattermost, the directory is ``/opt/mattermost/``. Also, if you followed our `installation process <../guides/administrator.html#installing-mattermost>`__, you must run the command as the user *mattermost*. The executable is in the ``bin`` subdirectory and is called ``mattermost``.

Using the Imported Team
^^^^^^^^^^^^^^^^^^^^^^^

* During the import process, the emails and usernames from Slack are used to create new Mattermost accounts. If emails are not present in the Slack export archive, then placeholder values will be generated and the System Admin will need to update these manually.
* Slack users can activate their new Mattermost accounts by using Mattermost's **Password Reset** screen with their email addresses from Slack to set new passwords for their Mattermost accounts.
* Once logged in, Mattermost users will have access to previous Slack messages in the public channels imported from Slack.

Migrating from Bitnami
~~~~~~~~~~~~~~~~~~~~~~

Bitnami uses MySQL, and renames the Mattermost database tables by converting the names to all lower case. For example, in non-Bitnami installations, the Users table is named "Users", but in Bitnami, the table is "users". As a result, when you migrate your data from Bitnami to a non-Bitnami installation, you must modify the MySQL startup script so that it starts MySQL in lowercase table mode.

You can modify the script by adding the ``--lower-case-table-names=1`` switch to the MySQL start command. The location of the start-up script generally depends on how you installed MySQL, whether by using the package manager for the operating system, or by manually installing MySQL. You must modify the start-up script before migrating the data.

For more information about letter case in MySQL table names and the ``--lower-case-table-names`` switch, see the `Identifier Case Sensitivity <https://dev.mysql.com/doc/refman/5.7/en/identifier-case-sensitivity.html>`__ topic in the MySQL documentation.

Migrating from HipChat Server and HipChat Data Center to Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please see `HipChat Migration Guide <https://docs.mattermost.com/administration/hipchat-migration-guidelines.html>`__.

Migrating from Jabber to Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BrightScout helped a major U.S. Federal Agency rapidly migrate from Jabber to Mattermost and open sourced their Extract, Transform and Load (ETL) tool at https://github.com/Brightscout/mattermost-etl.

Read more about their `case study <https://mattermost.com/blog/u-s-federal-agency-migrates-from-jabber-to-mattermost-the-open-source-way/>`__ online.

Migrating from Pidgin to Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In some cases people are using Pidgin clients with different backends to communicate. To continue using Pidgin with a Mattermost backend consider using `Mattermost ETL tool <https://github.com/Brightscout/mattermost-etl>`__ created by BrightScout to migrate data from your existing backend into Mattermost, then use the `Pidgin-Mattermost plugin <https://github.com/EionRobb/purple-mattermost>`__ (complete with an installer for end user machines) to continue to support legacy Pidgin users while offering a whole new Mattermost experience on web, mobile, and PC.
