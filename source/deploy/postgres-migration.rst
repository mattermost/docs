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

FAQ
===

1. Can the migration-assist be run on the mattermost server?

  Technically, yes. The ``migration-assist`` tool can be run on the Mattermost server. However, it is recommended to run the tool on a separate server to avoid any performance issues. We advise running the migration against a copy of the MySQL database to ensure that the migration process does not impact the production environment.

2. How large should the PostgreSQL server be?

  The size of the PostgreSQL server should match that of the MySQL server initially. We recommend monitoring the performance of the PostgreSQL server and adjusting the resources as needed.

3. How large should the server running ``migration-assist`` server be?

  The tool itself is lightweight and does not require a large server. A server with 2 CPU cores and 16 GB of RAM should be sufficient for default configurations. However, you may need to adjust the resources based on the size of the MySQL database, your downtime limitations, and the configuration of ``pgloader``.

4. Do we/will we bundle pgloader or is that a separate install?

  We do not bundle pgloader with the Mattermost server. You will need to install pgloader separately. For more information, see the :doc:`install pgloader </deploy/manual-postgres-migration:install pgloader>` documentation.

5. Are there any other migrations available for plugins, or just Boards and Playbooks?
  
  We are working on providing migrations for other plugins as well such as Calls. Please stay tuned for updates.