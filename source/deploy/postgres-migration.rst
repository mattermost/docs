Migration guidelines from MySQL to PostgreSQL
=============================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

From Mattermost v8.0, PostgreSQL is our database of choice for Mattermost to enhance the platform’s performance and capabilities. Recognizing the importance of supporting the community members who are interested in migrating from a MySQL database, we have taken proactive measures to provide guidance and best practices.

.. toctree::
   :maxdepth: 1
   :hidden:
   :titlesonly:

   Automate PostgreSQL migration </deploy/postgres-migration-assist-tool>
   Manually migrate to PostgreSQL </deploy/manual-postgres-migration>

* :doc:`Automated migration from MySQL to PostgreSQL </deploy/postgres-migration-assist-tool>` - A comprehensive set of guidelines and a ``migration-assist`` tool to streamline the migration process, alleviate potential challenges, and faciliate a smooth transition.
* :doc:`Manually migrate from MySQL to PostgreSQL </deploy/manual-postgres-migration>` - A good option if your organization has database administrators to own the migration process, or if you want to learn what the ``migration-assist`` tool automates for you.

Frequently asked questions
------------------------------

1. Can the migration-assist be run on the mattermost server?

  Technically, yes. The ``migration-assist`` tool can be run on the Mattermost server. However, it is recommended to run the tool on a separate server to avoid any performance issues. We advise running the migration against a copy of the MySQL database to ensure that the migration process does not impact the production environment.

2. How large should the PostgreSQL server be?

  The size of the PostgreSQL server should match that of the MySQL server initially. We recommend monitoring the performance of the PostgreSQL server and adjusting the resources as needed.

3. How large should the server running ``migration-assist`` server be?

  The tool itself is lightweight and does not require a large server. A server with 2 CPU cores and 16 GB of RAM should be sufficient for default configurations. However, you may need to adjust the resources based on the size of the MySQL database, your downtime limitations, and the configuration of ``pgloader``.

4. Do we/will we bundle pgloader or is that a separate install?

  We do not bundle pgloader with the Mattermost server. You will need to install pgloader separately. For more information, see the :doc:`install pgloader </deploy/manual-postgres-migration:install pgloader>` documentation.

5. Are there any other migrations available for plugins, or just Boards, Playbooks and Calls?
  
  We are working on providing migrations for other plugins as well such as NPS-plugin. Please stay tuned for updates.

6. Does these processes support AWS RDS databases?

  Yes, the processes support AWS RDS databases. However, you may need to adjust the security group settings to allow the migration process to access the databases.

Troubleshooting
---------------

Unsupported authentication for MySQL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are facing an error due to authentication with MySQL v8, it may be related to a `known issue <https://github.com/dimitri/pgloader/issues/782>`_ with pgloader. The fix is to set the default authentication method to ``mysql_native_password`` in your MySQL configuration. To do so, add the ``default-authentication-plugin=mysql_native_password`` value to your ``mysql.cnf`` file. Also, do not forget to update your user to use this authentication method.

.. code-block:: sql

  ALTER USER '<mysql_user>'@'%' IDENTIFIED WITH mysql_native_password BY '<mysql_password>';

Errors during the pgloader command execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you encounter errors during the execution of the ``pgloader`` command, ensure that both of the databases are accessible and that the users have the necessary permissions to access the database. Do not continue with the migration if there are errors during the execution of the ``pgloader`` command.

Also, there may be cases where ``pgloader`` continue to migration remaining tables and skip one or more tables. In such cases, it is recommended to identify issues with the table and fix them before running the ``pgloader`` command again with a clean database. It is possible to run the ``pgloader`` command with the ``--debug`` flag to get more information about the errors.

For experienced users, it is recoverable to run the ``pgloader`` without requiring to restart the migration from scratch. In this case, you will need to manually fix the issues with the table and run the ``pgloader`` command with a tailored configuration just for those tables. Also ensure that the schema name is reverted back to ``public`` and the ``search_path`` is restored or remove necessary clauses form the configuration.

Mattermost can't connect to the PostgreSQL database
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are facing an issue where Mattermost can't connect to the PostgreSQL database, ensure that the PostgreSQL server is running and that the database is accessible. If there were errors during the execution of the ``pgloader`` command, it can fail to revert shcema name back to ``public`` or potentially restoring the ``search_path``. You can manually revert the schema name back to ``public`` and restore the ``search_path`` by running the following commands:

.. code-block:: sql

  ALTER SCHEMA <schema_name> RENAME TO public;

Also ensure that the database user has the necessary settings to have default access to the ``public`` schema. You can do this by running the following commands:

.. code-block:: sql

  ALTER USER <user> SET SEARCH_PATH TO 'public';
  SELECT pg_catalog.set_config('search_path', '"$user", public', false); -- should give access for the session

You can check for the default ``search_path`` by running the following command:

.. code-block:: sql

  SELECT boot_val FROM pg_settings WHERE name='search_path';

Contact Support
---------------

Mattermost customers looking for guidance tailored to their Mattermost deployment can contact a `Mattermost Expert <https://mattermost.com/contact-sales/>`_ for guidance.
