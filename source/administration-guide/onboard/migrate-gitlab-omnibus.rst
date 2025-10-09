Migrating from GitLab Omnibus to Mattermost Standalone
======================================================

Overview
--------

GitLab has announced the deprecation of Mattermost from the GitLab Omnibus package in a future release (date to be determined). As part of this transition, GitLab will continue to support Mattermost **up to version 10.11 ESR** within the Omnibus installation until a final removal date is determined.  

To ensure continuity and long-term support, organizations using Mattermost within GitLab Omnibus should plan to migrate to a **standalone Mattermost installation**. This approach provides ongoing access to the latest Mattermost releases, security updates, and enterprise capabilities independent of GitLab’s release cycle.

Migrating to a standalone deployment also enables greater flexibility in managing infrastructure, upgrading PostgreSQL, and scaling Mattermost independently to meet performance and compliance requirements.

Prerequisites
--------------

Before you begin:

- Administrative (root or sudo) access to the GitLab Omnibus server.
- A new standalone **PostgreSQL** server prepared and accessible.
- Sufficient disk space for the Mattermost database dump.
- A planned maintenance window, as Mattermost downtime is required.
- A current full backup of your Mattermost instance, including database and file storage.

Migration Steps
---------------

Follow the steps below to safely migrate from GitLab Omnibus to a standalone Mattermost installation.

.. note::
   The following procedure assumes your Mattermost database name is ``mattermost_production`` and your PostgreSQL user is ``mmuser``. Adjust as needed for your environment.

Step 1: Create a Database Dump from GitLab Omnibus
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use the GitLab Omnibus PostgreSQL tools to create a dump of the Mattermost database.  
Run this command on the GitLab server:

.. code-block:: bash

   sudo gitlab-psql -- /opt/gitlab/embedded/bin/pg_dump -h /var/opt/gitlab/postgresql --no-owner mattermost_production | gzip > mattermost_dbdump_$(date --rfc-3339=date).sql.gz

This will create a compressed SQL dump file of your Mattermost database.

Step 2: Prepare the New PostgreSQL Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set up your new PostgreSQL server following the official Mattermost database preparation guidelines. This includes:

- Installing the correct PostgreSQL version supported by your Mattermost server.
- Creating a new Mattermost database and user with appropriate permissions.

Refer to the official setup instructions in the :doc:`Mattermost Database Preparation Guide </install/install-database>`.

Step 3: Transfer and Restore the Database Dump
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Transfer the database dump file to your new PostgreSQL server, then restore it:

.. code-block:: bash

   zcat /tmp/mattermost_dbdump.sql.gz | psql -U mmuser -d mattermost

Verify that the database restoration completes successfully without errors.

Step 4: Update Mattermost Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On your standalone Mattermost server, update the ``config.json`` file to point to the new PostgreSQL server.  
Locate the ``SqlSettings.DataSource`` parameter and update it as follows:

.. code-block:: json

   "SqlSettings": {
       "DriverName": "postgres",
       "DataSource": "postgres://mmuser:password@new-postgres-server:5432/mattermost?sslmode=disable&connect_timeout=10"
   }

Ensure that credentials, hostnames, and connection settings match your new PostgreSQL configuration.

Step 5: Migrate the Mattermost Application and Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To move Mattermost application files from the GitLab server to a new standalone server:

1. **Install the same or newer version** of Mattermost on the new server. See the :doc:`Server Deployment Planning </server-deployment-planning.html#deployment-options>`.
2. **Copy your existing configuration and data** from the GitLab Omnibus instance:

   .. code-block:: bash

      # On the GitLab server
      sudo cp /var/opt/gitlab/mattermost/config/config.json /tmp/
      sudo cp -r /var/opt/gitlab/mattermost/data /tmp/mattermost_data

      # Transfer to new Mattermost server
      scp /tmp/config.json mattermost@new-server:/opt/mattermost/config/
      scp -r /tmp/mattermost_data mattermost@new-server:/opt/mattermost/data/

3. Ensure permissions are correctly set on the new server:

   .. code-block:: bash

      sudo chown -R mattermost:mattermost /opt/mattermost

Step 6: Start Mattermost
^^^^^^^^^^^^^^^^^^^^^^^^

Start the Mattermost service on your new standalone installation:

.. code-block:: bash

   sudo systemctl start mattermost

Mattermost will now connect to your standalone PostgreSQL database.

Step 7: Verify the Migration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After starting Mattermost, perform the following checks:

- Confirm that Mattermost starts successfully with no database connection errors.
- Review server logs for any startup or connection issues.
- Log into Mattermost and verify that all teams, channels, and users are present.
- Post test messages and upload files to confirm functionality.
- Validate user authentication and permissions.
- Confirm that database queries are directed to the new PostgreSQL server.

Important Considerations
------------------------

- Always maintain a **full backup** of your Mattermost database before migration.
- Schedule a **maintenance window** to minimize user disruption.
- Validate performance and monitoring configurations post-migration.
- Ensure that your new PostgreSQL server follows Mattermost’s security and tuning best practices.

Troubleshooting
---------------

If you encounter errors during the migration:

- Review PostgreSQL logs for permission or connection issues.
- Verify that the Mattermost PostgreSQL user has full access to the restored database.
- Ensure that the ``config.json`` file contains the correct database connection string.
- Restart the Mattermost service and check ``mattermost.log`` for detailed errors.
