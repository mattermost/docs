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

* :doc:`Automate migration from MySQL to PostgreSQL </deploy/postgres-migration-assist-tool>` - A comprehensive set of guidelines and a ``migration-assist`` tool to streamline the migration process, alleviate potential challenges, and faciliate a smooth transition.
* :doc:`Manually migrate from MySQL to PostgreSQL </deploy/manual-postgres-migration>` - A good option if your organization has database administrators to own the migration process, or if you want to learn what the ``migration-assist`` tool automates for you.