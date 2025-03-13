Prepare your Mattermost database
================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:
  
You need a PostgreSQL database. See the :ref:`database software <install/software-hardware-requirements:database software>` documentation for details on database version support. Looking for information on migrating from MySQL to PostgreSQL? See the :doc:`Migrate from MySQL to PostgreSQL </deploy/postgres-migration>` documentation for details.

.. tip::

  We recommend using a managed PostgreSQL database service, such as Amazon RDS, Google Cloud SQL, or Azure Database for PostgreSQL.

Set up a PostgreSQL database
----------------------------

To set up a PostgreSQL database for use by the Mattermost server:

1. Log in to the server that will host the database, and install PostgreSQL. See the `PostgreSQL <https://www.postgresql.org/download/>`__ documentation for details. When the installation is complete, the PostgreSQL server is running, and a Linux user account called *postgres* has been created.

2. Access PostgreSQL by running:

  .. code-block:: sh

    sudo -u postgres psql

3. Create the Mattermost database by running:

  .. tab:: Ubuntu

    .. code-block:: SQL

      CREATE DATABASE mattermost;

  .. tab:: Red Hat

    .. code-block:: SQL

      CREATE DATABASE mattermost WITH ENCODING 'UTF8' LC_COLLATE='en_US.UTF-8' LC_CTYPE='en_US.UTF-8' TEMPLATE=template0;

4. Switch to the new database by running: 

  .. code-block:: sh

    \connect mattermost

5. Create the Mattermost user *mmuser* by running the following command. Ensure you use a password that's more secure than ``mmuser-password``.

  .. code-block:: SQL

    CREATE USER mmuser WITH PASSWORD 'mmuser-password';

6. If you're configuring PostgreSQL v15.x or later:
    
  a. Grant the user access to the Mattermost database by running:

    .. code-block:: SQL

      GRANT ALL PRIVILEGES ON DATABASE mattermost to mmuser;
                  

  b. Grant the user to change the owner of a database to a user ``mmuser`` by running:

     .. code-block:: SQL

       ALTER DATABASE mattermost OWNER TO mmuser;

  c. Grant access to objects contained in the specified schema by running: 

    .. code-block:: SQL

      GRANT USAGE, CREATE ON SCHEMA PUBLIC TO mmuser;

7. Exit the PostgreSQL interactive terminal by running:

  .. code-block:: text

    \q

8. (Optional) If you use separate servers for your database and the Mattermost server, you may allow PostgreSQL to listen on all assigned IP addresses. We recommend ensuring that only the Mattermost server is able to connect to the PostgreSQL port using a firewall.

  .. tab:: Ubuntu

    Open ``/etc/postgresql/{version}/main/postgresql.conf`` as *root* in a text editor.
    
    Replace ``{version}`` with the version of PostgreSQL that's currently running.

    a. Find the following line: ``#listen_addresses = 'localhost'``

    b. Uncomment the line and change ``localhost`` to ``*``: ``listen_addresses = '*'``

    c. Restart PostgreSQL for the change to take effect by running:

      .. code-block:: sh

          sudo systemctl restart postgresql-{version}

  .. tab:: Red Hat

    Open ``/var/lib/pgsql/{version}/data/postgresql.conf`` as *root* in a text editor.

    Replace ``{version}`` with the version of PostgreSQL that's currently running. 

    a. Find the following line: ``#listen_addresses = 'localhost'``

    b. Uncomment the line and change ``localhost`` to ``*``: ``listen_addresses = '*'``

    c. Restart PostgreSQL for the change to take effect by running:

      .. code-block:: sh

          sudo systemctl restart postgresql-{version}

9. Modify the file ``pg_hba.conf`` to allow the Mattermost server to communicate with the database by ensuring host connection types are set to ``trust``.

  .. tab:: Ubuntu

    These host connections are specific to Ubuntu 20.04, and will differ depending on the operating system version you're running. For example, in Ubuntu 22.04, the ``peer`` connection types are listed as ``sha-256`` instead.

    **Local Database (same server)**

    If the Mattermost server and the database are on the same machine:

    a. Open ``/etc/postgresql/{version}/main/pg_hba.conf`` as *root* in a text editor. 

    b.  Find the following lines:

      ``local   all             all                        peer``

      ``host    all             all         ::1/128        ident``

    c. Change ``peer`` and ``ident`` to ``trust``:

      ``local   all             all                        trust``

      ``host    all             all         ::1/128        trust``

    **Remote Database (separate server)**

    If the Mattermost server and the database are on different machines:

    a. Open ``/etc/postgresql/{version}/main/pg_hba.conf`` in a text editor as *root* user.

    b. Add the following line to the end of the file, where ``{mattermost-server-IP}`` is the IP address of the Mattermost server: ``host all all {mattermost-server-IP}/32 md5``.

  .. tab:: Red Hat

    These host connections are specific to Red Hat 8, and will differ depending on the operating system version you're running.

    **Local Database (same server)**

    If the Mattermost server and the database are on the same machine:

    a. Open ``/var/lib/pgsql/{version}/data/pg_hba.conf`` as *root* in a text editor. 

    b.  Find the following lines:

      ``local   all             all                        peer``

      ``host    all             all         ::1/128        scram-sha-256``

    c. Change ``peer`` and ``ident`` to ``trust``:

      ``local   all             all                        trust``

      ``host    all             all         ::1/128        trust``

    **Remote Database (separate server)**

    If the Mattermost server and the database are on different machines:

    a. Open ```/var/lib/pgsql/{version}/data/pg_hba.conf`` in a text editor as *root* user.

    b. Add the following line to the end of the file, where ``{mattermost-server-IP}`` is the IP address of the Mattermost server: ``host all all {mattermost-server-IP}/32 md5``.

10. Reload PostgreSQL by running:

  .. code-block:: sh

      sudo systemctl reload postgresql-{version}

11. Verify that you can connect with the user *mmuser*.

.. tab:: Local Database (same server)

  If the Mattermost server and the database are on the same machine, use the following command: 

    .. code-block:: sh

        psql --dbname=mattermost --username=mmuser --password

.. tab:: Remote Database (separate server)

  If the Mattermost server is on a different machine, log into that machine and use the following command: 

    .. code-block:: sh

        psql --host={postgres-server-IP} --dbname=mattermost --username=mmuser --password

  .. note::

    You might have to install the PostgreSQL client software to use the command.

The PostgreSQL interactive terminal starts. To exit the PostgreSQL interactive terminal, type ``\q`` and press :kbd:`Enter` on Windows or Linux, or :kbd:`↵` on Mac.

When the PostgreSQL database is installed, and the initial setup is complete, you can install the Mattermost server.

.. important::

  If you are upgrading a major version of Postgres, it is essential that ``ANALYZE VERBOSE`` is run on the database post upgrade. This is necessary to re-populate the ``pg_statistics`` table used to generate optimal query plans. The database performance might suffer if this step is not done.


Minimum supported version policy
---------------------------------

To make planning easier and ensure your Mattermost deployment remains fast and secure, we are introducing a policy for updating the minimum supported version of PostgreSQL. The oldest supported PostgreSQL version Mattermost supports will match the oldest version supported by the PostgreSQL community. This ensures you benefit from the latest features and security updates.

This policy change takes effect from Mattermost v10.6, where the minimum PostgreSQL version required will be PostgreSQL 13. This aligns with the PostgreSQL community's support policy, which provides 5 years of support for each major version.

.. note::

  Mattermost v10.6 is not an :ref:`Extended Support Release (ESR) <about/release-policy:extended support releases>`. Going forward, this database version support policy will only apply to ESR releases.

When a PostgreSQL version reaches its end of life (EOL), Mattermost will require a newer version starting with the next scheduled ESR release. This means the following future PostgreSQL minimum version increases as follows:

+-----------------------------------------------------------+------------------+--------------------------------+
| **Mattermost Version**                                    | **Release Date** | **Minimum PostgreSQL Version** |
+===========================================================+==================+================================+
| :ref:`v9.11 ESR <release-v9-11-extended-support-release>` | 2024-8-15        | 11.x                           |
+-----------------------------------------------------------+------------------+--------------------------------+
| :ref:`v10.5 ESR <release-v10.5-extended-support-release>` | 2025-2-15        | 11.x                           |
+-----------------------------------------------------------+------------------+--------------------------------+
| v10.6                                                     | 2025-3-15        | 13.x                           |
+-----------------------------------------------------------+------------------+--------------------------------+
| v10.11 ESR                                                | 2025-8-15        | 13.x                           |
+-----------------------------------------------------------+------------------+--------------------------------+
| v11.5 ESR ``*``                                           | 2026-2-15        | 14.x (EOL 2026-11-12)          |
+-----------------------------------------------------------+------------------+--------------------------------+

``*`` Forcasted release version and date.

Customers will have 9 months to plan, test, and upgrade their PostgreSQL version before the new requirement takes effect. This policy aims to provide clarity and transparency so you can align database upgrades with the Mattermost release schedule. Contact a `Mattermost Expert <https://mattermost.com/contact-sales/>`_. to discuss your options.

Frequently asked questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

What about MySQL databases?
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Mattermost is :ref:`deprecating support for MySQL <deploy/postgres-migration:why is mattermost dropping support for mysql?>` starting with v11. We aren't actively maintaining or working on MySQL support.
