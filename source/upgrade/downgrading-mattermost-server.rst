Downgrade Mattermost Server
===========================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

In most cases you can downgrade Mattermost Server using the same steps as :doc:`upgrading-mattermost-server`. Server binaries can be found in the :doc:`Mattermost server version archive </about/version-archive>` documentation. 

.. important::

  - We don't recommend downgrading more than one major version back from your current installation.
  - We strongly recommend testing the downgrade in a staging environment first to identify any potential issues.
  - Ensure that your plugins and integrations are compatible with the downgraded version you're moving to.

Prepare for downgrade
---------------------

Before downgrading the Mattermost server, we strongly recommend the following preparation steps.

1. Back up your data: Ensure you have a full backup of your database and Mattermost application files. This is crucial in case you need to revert any changes.

  a. Back up your database using your organization’s standard procedures for backing up the database.

  b. Back up your application by copying into an archive folder (e.g. ``mattermost-back-YYYY-MM-DD-HH-mm``). Ensure to copy your Mattermost configuration files and any other necessary application files.

2. Carefully review the Mattermost changelog for the version you are downgrading to in order to understand any potential issues or incompatibilities.

3. Verify the current schema version of your database using the :ref:`mattermost db version <manage/command-line-tools:mattermost db version>` command.

Perform the downgrade
---------------------

1. Stop the Mattermost service to ensure that no data is being written to the database during the downgrade process.
2. Downgrade the application by replacing the current Mattermost application binary with the version you want to downgrade to. Make sure to use the binary of the target version.

3. If the database schema has changed between versions, you must to downgrade the schema. Use the :ref:`mattermost db downgrade <manage/command-line-tools:mattermost db downgrade>` command. For example: ``mattermost db downgrade --target <target-schema-version>``

.. tip::

  You can review downgrade changes before committing them by using the ``--save-plan`` option to generate the SQL downgrade script. This option allows you to save the SQL statements that would be executed during the downgrade process to a specified file, instead of applying them directly to the database. For example: ``mattermost db downgrade --save-plan downgrade_plan.sql``.

4. There may be changes in configuration settings between versions. Revert any necessary configuration changes in the ``config.json`` file to match the downgraded version's expectations and support.

After the downgrade
--------------------

1. Restart the Mattermost Server after completing the downgrade.
2. Check the logs and test the application to ensure that everything is functioning correctly.
3. Inform your users about the downgrade and any potential changes they might experience.