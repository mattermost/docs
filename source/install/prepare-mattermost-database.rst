Prepare your Mattermost database
================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:
  
You need a PostgreSQL database. See the :ref:`database software <install/software-hardware-requirements:database software>` documentation for details on database version support.

.. tip::

  Looking for information on working with a MySQL database? See the :doc:`prepare your Mattermost MySQL database </install/prepare-mattermost-mysql-database>` documentation for details.

To set up a PostgreSQL database for use by the Mattermost server:

1. Log in to the server that will host the database, and install PostgreSQL. See the `PostgreSQL <https://www.postgresql.org/download/>`__ documentation for details. When the installation is complete, the PostgreSQL server is running, and a Linux user account called *postgres* has been created.

2. Access PostgreSQL by running:

  .. code-block:: none
    :class: mm-code-block 

      sudo -u postgres psql

3. Create the Mattermost database by running:

  .. tab:: Ubuntu

    .. code-block:: none
      :class: mm-code-block 

      postgres=# CREATE DATABASE mattermost;

  .. tab:: Red Hat

    .. code-block:: none
      :class: mm-code-block 

      postgres=# CREATE DATABASE mattermost WITH ENCODING 'UTF8' LC_COLLATE='en_US.UTF-8' LC_CTYPE='en_US.UTF-8' TEMPLATE=template0;

4. Create the Mattermost user *mmuser* by running the following command. Ensure you use a password that's more secure than ``mmuser-password``.

  .. code-block:: none
    :class: mm-code-block 

      postgres=# CREATE USER mmuser WITH PASSWORD 'mmuser-password';

5. If you're configuring PostgreSQL v15.x or later:
    
  a. Grant the user access to the Mattermost database by running:

    .. code-block:: none
      :class: mm-code-block 

        postgres=# GRANT ALL PRIVILEGES ON DATABASE mattermost to mmuser;
                  

  b. Grant the user to change the owner of a database to a user ``mmuser`` by running:

     .. code-block:: none
      :class: mm-code-block 

        ALTER DATABASE mattermost OWNER TO mmuser;

  c. Grant access to objects contained in the specified schema by running: 

    .. code-block:: none
      :class: mm-code-block 

        GRANT USAGE, CREATE ON SCHEMA PUBLIC TO mmuser;

6. Exit the PostgreSQL interactive terminal by running:

  .. code-block:: none
    :class: mm-code-block 

      postgres=# \q

7. (Optional) If you use separate servers for your database and the Mattermost server, you may allow PostgreSQL to listen on all assigned IP addresses. We recommend ensuring that only the Mattermost server is able to connect to the PostgreSQL port using a firewall.

  .. tab:: Ubuntu

    Open ``/etc/postgresql/{version}/main/postgresql.conf`` as *root* in a text editor.
    
    Replace ``{version}`` with the version of PostgreSQL that's currently running.

    a. Find the following line: ``#listen_addresses = 'localhost'``

    b. Uncomment the line and change ``localhost`` to ``*``: ``listen_addresses = '*'``

    c. Restart PostgreSQL for the change to take effect by running:

      .. code-block:: none
        :class: mm-code-block 

          sudo systemctl restart postgresql-{version}

  .. tab:: Red Hat

    Open ``/var/lib/pgsql/{version}/data/postgresql.conf`` as *root* in a text editor.

    Replace ``{version}`` with the version of PostgreSQL that's currently running. 

    a. Find the following line: ``#listen_addresses = 'localhost'``

    b. Uncomment the line and change ``localhost`` to ``*``: ``listen_addresses = '*'``

    c. Restart PostgreSQL for the change to take effect by running:

      .. code-block:: none
        :class: mm-code-block 

          sudo systemctl restart postgresql-{version}

8. Modify the file ``pg_hba.conf`` to allow the Mattermost server to communicate with the database by ensuring host connection types are set to ``trust``.

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

9. Reload PostgreSQL by running:

  .. code-block:: none
    :class: mm-code-block 

      sudo systemctl reload postgresql-{version}

10. Verify that you can connect with the user *mmuser*.

.. tab:: Local Database (same server)

  If the Mattermost server and the database are on the same machine, use the following command: 

    .. code-block:: none
      :class: mm-code-block 

        psql --dbname=mattermost --username=mmuser --password

.. tab:: Remote Database (separate server)

  If the Mattermost server is on a different machine, log into that machine and use the following command: 

    .. code-block:: none
      :class: mm-code-block 

        psql --host={postgres-server-IP} --dbname=mattermost --username=mmuser --password

  .. note::

    You might have to install the PostgreSQL client software to use the command.

The PostgreSQL interactive terminal starts. To exit the PostgreSQL interactive terminal, type ``\q`` and press :kbd:`Enter` on Windows or Linux, or :kbd:`↵` on Mac.

When the PostgreSQL database is installed, and the initial setup is complete, you can install the Mattermost server.
