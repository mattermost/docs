Using Sockets for Database
==========================

Mattermost requires a database back-end. If you plan to run it on the machine,
install MySQL or PostgreSQL as the database. In this document let's understand how
you can use sockets for setting up the database.

MySQL
-----

.. code-block:: bash

    $ mysql -u root -p
    CREATE DATABASE mattermostdb;
    CREATE USER mmuser IDENTIFIED BY 'mmuser_password';
    GRANT ALL ON mattermostdb.* TO mmuser;


PostgreSQL
----------

- Install and configure PostgreSQL.
- Choose between TCP or UNIX Socket, and jump to the corresponding section.

With TCP socket
---------------

- Create the new user while connecting to the server as ``postgres`` user
  (you will be prompted for a password for the new user):

  ``sudo -u postgres createuser -P mmuser``

- Create the Mattermost database, owned by ``mmuser`` user:

  ``sudo -u postgres createdb -O mmuser mattermostdb``

- In the connections and authentications section, set the ``listen_address`` list
  line per your needs:

   .. code-block:: bash

      /var/lib/postgres/data/postgresql.conf
      listen_address = 'localhost,my_local_ip_address'

  You can use '*' to listen on all available addresses.

- Then add a line like the following to the authentication config:

  .. code-block:: bash

     /var/lib/postgres/data/pg_hba.conf
     # TYPE  DATABASE        USER            ADDRESS                 METHOD
     # IPv4 local connections:
     host    all             all             ip_address/32   md5

- Run the setup using:

  .. code-block:: bash

     $ psql --host=ip_address --dbname=mattermostdb --username=mmuser --password

With Unix socket
----------------

- Create the new user while connecting to the server as ``postgres`` user:

  .. code-block:: bash

     sudo -u postgres createuser mattermost

- Create the Mattermost database, owned by ``mattermost`` user:

  .. code-block:: bash

     sudo -u postgres createuser mattermost

- Setup the Unix socket by adding the following line to ``/var/lib/postgres/data/pg_hba.conf``:

  .. code-block:: bash

     local    mattermostdb    mattermost    peer

- Restart postgresql.service.

- Run the setup using:

  .. code-block:: bash

     sudo -u mattermost psql --dbname=mattermostdb --username=mattermost


Configuring Mattermost
----------------------

- Mattermost is configured in ``/etc/webapps/mattermost/config.json``.
  Strings need to be quoted.

- The ``DriverName`` setting: ``mysql`` for MySQL and ``postgres`` for PostgreSQL.

  The ``DataSource``:

  - For MySQL, set it to ``mmuser:mmuser_password@unix(/run/mysqld/mysqld.sock)/mattermostdb?charset=utf8mb4,utf8``.
  - For PostgreSQL
    
    - TCP socket: ``postgres://mmuser:mmuser_password@127.0.0.1:5432/mattermostdb?sslmode=disable&connect_timeout=10``    
    
    - Unix socket: ``postgres:///mattermostdb?host=/run/postgresql``, where ``mattermostdb`` is the name of the database and ``/run/postgresql`` is the directory containing the Unix socket.

