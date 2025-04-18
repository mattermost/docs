(Optional) Using sockets for database
======================================

.. include:: ../../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

You can use sockets for setting up the database. Choose between TCP or UNIX Socket.

With TCP socket
---------------

1. Create the new user while connecting to the server as ``postgres`` user (you will be prompted for a password for the new user):

  ``sudo -u postgres createuser -P mmuser``

2. Create the Mattermost database, owned by ``mmuser`` user:

  ``sudo -u postgres createdb -O mmuser mattermostdb``

3. In the connections and authentications section, set the ``listen_address`` list line per your needs:

   .. code-block:: sh

      /var/lib/postgres/data/postgresql.conf
      listen_address = 'localhost,my_local_ip_address'

  You can use '*' to listen on all available addresses.

4. Then add a line like the following to the authentication config:

  .. code-block:: sh

     /var/lib/postgres/data/pg_hba.conf
     # TYPE  DATABASE        USER            ADDRESS                 METHOD
     # IPv4 local connections:
     host    all             all             ip_address/32   md5

5. Run the setup using:

  .. code-block:: sh

    psql --host=ip_address --dbname=mattermostdb --username=mmuser --password

With Unix socket
----------------

1. Create the new user while connecting to the server as ``postgres`` user:

  .. code-block:: sh

     sudo -u postgres createuser mattermost

2. Create the Mattermost database, owned by ``mattermost`` user:

  .. code-block:: sh

     sudo -u postgres createdb -O mattermost mattermostdb

3. Set up the Unix socket by adding the following line to ``/var/lib/postgres/data/pg_hba.conf``:

  .. code-block:: sh

     local    mattermostdb    mattermost    peer

4. Restart postgresql.service.

5. Run the setup using:

  .. code-block:: sh

     sudo -u mattermost psql --dbname=mattermostdb

Configuring Mattermost
----------------------

Mattermost is configured in ``/etc/webapps/mattermost/config.json``. Strings need to be quoted.

- Set ``DriverName`` to ``postgres``.

- Set ``DataSource``:

  - TCP socket: ``postgres://mmuser:mmuser_password@127.0.0.1:5432/mattermostdb?sslmode=disable&connect_timeout=10``    
  - Unix socket: ``postgres:///mattermostdb?host=/run/postgresql``, where ``mattermostdb`` is the name of the database and ``/run/postgresql`` is the directory containing the Unix socket.