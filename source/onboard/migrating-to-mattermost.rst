Migration guide
===============

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Thousands of organizations are moving to Mattermost for powerful, flexible, and easy-to-manage workplace collaboration. Mattermost deploys as a single Linux binary with PostgreSQL, and can scale from dozens to tens of thousands of users in a single channel.

This guide summarizes different approaches to migrating to Mattermost from other tools, including :doc:`Slack </onboard/migrate-from-slack>`, :doc:`HipChat </onboard/migrating-from-hipchat-to-mattermost>`, `Jabber <#migrate-from-jabber>`_, `Pidgin <#migrate-from-pidgin>`_, `Bitnami <#migrate-from-bitnami>`_, and other `bespoke messaging solutions <#migrate-from-bespoke-messaging-solutions>`_, as well as `migrating Mattermost server <#migrate-mattermost-server>`_ to another server instance.

Migrate from Slack
------------------

See the :doc:`Migrate from Slack </onboard/migrate-from-slack>` documentation for details on migrating from Slack to Mattermost.

Migrate from HipChat 
--------------------

See the :doc:`Migrate from HipChat </onboard/migrating-from-hipchat-to-mattermost>` documentation for details on migrating from HipChat Server and HipChat Data Center to Mattermost.

Migrate from Jabber
-------------------

BrightScout helped a major U.S. Federal Agency rapidly migrate from Jabber to Mattermost and open sourced their Extract, Transform and Load (ETL) tool at https://github.com/Brightscout/mattermost-etl. Read more about their `case study <https://mattermost.com/blog/u-s-federal-agency-migrates-from-jabber-to-mattermost-the-open-source-way/>`__ online.

Migrate from Pidgin
-------------------

In some cases, people are using Pidgin clients with different backends to communicate. To continue using Pidgin with a Mattermost backend, consider using `Mattermost ETL tool <https://github.com/Brightscout/mattermost-etl>`__, created by BrightScout, to migrate data from your existing backend into Mattermost. 

Then use the `Pidgin-Mattermost plugin <https://github.com/EionRobb/purple-mattermost>`__ (complete with an installer for end user machines) to continue to support legacy Pidgin users while offering a whole new Mattermost experience on web, mobile, and PC.

Migrate from Bitnami
--------------------

Bitnami uses MySQL, and renames the Mattermost database tables by converting the names to all lower case. For example, in non-Bitnami installations, the Users table is named ``Users``, but in Bitnami, the table is ``users`` (with a lowercase ``u``). As a result, when you migrate your data from Bitnami to a non-Bitnami installation, you must modify the MySQL startup script so that it starts MySQL in lowercase table mode.

You can modify the script by adding the ``--lower-case-table-names=1`` switch to the MySQL start command. The location of the start-up script generally depends on how you installed MySQL, whether by using the package manager for the operating system, or by manually installing MySQL. You must modify the start-up script before migrating the data.

For more information about letter case in MySQL table names and the ``--lower-case-table-names`` switch, see the `Identifier Case Sensitivity <https://dev.mysql.com/doc/refman/5.7/en/identifier-case-sensitivity.html>`__ topic in the MySQL documentation.

Migrate from bespoke messaging solutions
-----------------------------------------

Mattermost is often selected to replace bespoke solutions by IT and DevOps teams as a stable, enterprise-grade, commercially-supported solution on an open source platform that meets and exceeds the flexibility and innovation of bespoke solutions.

Migrating from bespoke messengers to Mattermost can be challenging. Because of the difficulty of upgrading and maintaining bespoke solutions, the format for storing data is unpredictable, and the community around any single legacy release is small.

If your data in the bespoke messenger is vital, consider:

1. :doc:`Mattermost bulk load tool </onboard/bulk-loading-data>`: Use the Mattermost bulk load tool to ETL from your bespoke system to Mattermost.
2. `Mattermost ETL framework from BrightScout <https://github.com/Brightscout/mattermost-etl>`__: Consider the Mattermost ETL framework from BrightScout to custom-configure an adapter to plug in to the Bulk Load tool mentioned above.
3. **Legacy Slack import:** If you only recently switched from Slack to a bespoke tool, consider going back to import the data and users from the old Slack instance directly into Mattermost, leveraging the extensive support for Slack-import provided.
4. **Export to Slack, then import to Mattermost:** `Export HipChat, Flowdock, Campfire, Chatwork, Hall, or CSV files to Slack <https://get.slack.help/hc/en-us/articles/201748703-Import-message-history>`__ and then export to a Slack export file and import the file into Mattermost.

If your data in the bespoke messenger is not vital, consider:

1. **Parallel systems:** Running Mattermost in parallel with your bespoke system until the majority of workflow and collaboration has moved to Mattermost
2. **Hard switch:** Announce a "hard switch" to Mattermost after a period of time of running both systems in parallel. Often this has been done due to security concerns in bespoke products or products nearing end-of-life.

Sometimes systems running in parallel turn into a hard switch migration when a bespoke or deprecated system experiences a major outage or a security exploit. In 2017, this was experienced by many companies using Mattermost and HipChat.com in parallel when `HipChat suffered a major security breach where customer data was stolen by an unknown attacker <https://thenextweb.com/insider/2017/04/24/hipchat-hacked-weekend-bad/#.tnw_lAotA9OV>`__.


----

Migrate Mattermost server
-------------------------

The following instructions migrate Mattermost from one server to another by backing up and restoring the Mattermost database and ``config.json`` file. For these instructions SOURCE refers to the Mattermost server *from which* your system will be migrated and DESTINATION refers to the Mattermost server *to which* your system will be migrated.

1. Back up your SOURCE Mattermost server. See :doc:`Backup and Disaster Recovery documentation </deploy/backup-disaster-recovery>`.
2. Upgrade your SOURCE Mattermost server to the latest major build version. See :doc:`Upgrading Mattermost Server documentation </upgrade/upgrading-mattermost-server>`.
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

Once your migration is complete and verified, you can optionally :ref:`upgrade the Team Edition of Mattermost to Enterprise Edition using the upgrade guide <upgrade/upgrading-mattermost-server:upgrade team edition to enterprise edition>`.
