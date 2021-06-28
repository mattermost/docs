.. _install-ubuntu-1804-postgresql:

Installing PostgreSQL Database Server
=====================================

Install and set up the database for use by the Mattermost server. You can install either PostgreSQL or MySQL.

Assume that the IP address of this server is 10.10.10.1.

**To install PostgreSQL on Ubuntu Server 20.04:**

1. Log in to the server that will host the database and issue the following command:

  ``sudo apt install postgresql postgresql-contrib``

  When the installation is complete, the PostgreSQL server is running, and a Linux user account called *postgres* has been created.
  
Confirm this version is PostgreSQL version 10 or higher. You can do this by running ``psql -V``. If this is not version 10 or higher you can reference the PostgreSQL documentation [here](https://www.postgresql.org/download/linux/ubuntu/) to install an updated version of PostgreSQL.

2. Access PostgreSQL with one of the following options:

  - ``sudo --login --user postgres`` then ``psql``
  - ``sudo -u postgres psql``
  
3.  Create the Mattermost database.

  ``postgres=# CREATE DATABASE mattermost;``

4.  Create the Mattermost user *mmuser*.

  ``postgres=# CREATE USER mmuser WITH PASSWORD 'mmuser-password';``

.. note::
  
    Use a password that's more secure than *mmuser-password*.

5.  Grant the user access to the Mattermost database.

  ``postgres=# GRANT ALL PRIVILEGES ON DATABASE mattermost to mmuser;``

6. Exit the PostgreSQL interactive terminal.

  ``postgres=# \q``

7. Log out of the *postgres* account.

  ``exit``

8. (Optional) If you use a different server for your database and the Mattermost server, you may allow PostgreSQL to listen on all assigned IP addresses. To do so, open ``/etc/postgresql/{version}/main/postgresql.conf`` in a text editor as *root* user. Replace ``{version}`` with the version of PostgreSQL that's currently running. As a best practice, ensure that only the Mattermost server is able to connect to the PostgreSQL port using a firewall.

  a. Find the following line:

    ``#listen_addresses = 'localhost'``

  b. Uncomment the line and change ``localhost`` to ``*``:

    ``listen_addresses = '*'``

  c. Restart PostgreSQL for the change to take effect:

    ``sudo systemctl restart postgresql``

9. Modify the file ``pg_hba.conf`` to allow the Mattermost server to communicate with the database.

  **If the Mattermost server and the database are on the same machine:**

    a. Open ``/etc/postgresql/{version}/main/pg_hba.conf`` as *root* in a text editor.

    b. Find the following lines:

      ``local   all             all                        peer``
      
      ``host    all             all         ::1/128        ident``

    c. Change ``peer`` and ``ident`` to ``trust``:

      ``local   all             all                        trust``
      
      ``host    all             all         ::1/128        trust``

  **If the Mattermost server and the database are on different machines:**

    a. Open ``/etc/postgresql/{version}/main/pg_hba.conf`` in a text editor as *root* user.

    b. Add the following line to the end of the file, where ``{mattermost-server-IP}`` is the IP address of the Mattermost server.

      ``host all all {mattermost-server-IP}/32 md5``

10. Reload PostgreSQL:

  ``sudo systemctl reload postgresql``

11. Verify that you can connect with the user *mmuser*.

  - If the Mattermost server and the database are on the same machine, use the following command:

    ``psql --dbname=mattermost --username=mmuser --password``

  - If the Mattermost server is on a different machine, log into that machine and use the following command:

    ``psql --host={postgres-server-IP} --dbname=mattermost --username=mmuser --password``

.. note::

  You might have to install the PostgreSQL client software to use the command.

The PostgreSQL interactive terminal starts. To exit the PostgreSQL interactive terminal, type ``\q`` and press ENTER.

With the database installed and the initial setup complete, you can now install the Mattermost server.
