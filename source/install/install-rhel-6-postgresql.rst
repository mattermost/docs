:orphan:

..  _install-rhel-6-postgresql:

Installing PostgreSQL Database
==============================

1. Log in to the server that will host the database, and open a terminal window.

2. Download the PostgreSQL 9.4 Yum repository.

  ``wget https://download.postgresql.org/pub/repos/yum/9.4/redhat/rhel-6-x86_64/pgdg-redhat94-9.4-3.noarch.rpm``

3. Install the Yum repository from the file that you downloaded.

  ``sudo yum localinstall pgdg-redhat94-9.4-3.noarch.rpm``

4. Install PostgreSQL.

  ``sudo yum install postgresql94-server postgresql94-contrib``

5. Initialize the database.

  ``sudo service postgresql-9.4 initdb``

6. Set PostgreSQL to start on boot.

  ``sudo chkconfig postgresql-9.4 on``

7. Start the PostgreSQL server.

  ``sudo service postgresql-9.4 start``

8. Switch to the *postgres* Linux user account that was created during the installation.

  ``sudo --login --user postgres``

9. Start the PostgreSQL interactive terminal.

  ``psql``

10.  Create the Mattermost database.

  ``postgres=# CREATE DATABASE mattermost;``

11.  Create the Mattermost user 'mmuser'.

  ``postgres=# CREATE USER mmuser WITH PASSWORD 'mmuser-password';``

  .. note::
    Use a password that is more secure than 'mmuser-password'.

12.  Grant the user access to the Mattermost database.

  ``postgres=# GRANT ALL PRIVILEGES ON DATABASE mattermost to mmuser;``

13. Exit the PostgreSQL interactive terminal.

  ``postgres=# \q``

14. Log out of the *postgres* account.

  ``exit``

15. Allow Postgres to listen on all assigned IP Addresses.

  a. Open ``/etc/postgresql/9.4/main/postgresql.conf`` as root in a text editor.

  b. Find the following line:

    ``#listen_addresses = 'localhost'``

  c. Uncomment the line and change ``localhost`` to ``*``:

    ``listen_addresses = '*'``

  d. Restart PostgreSQL for the change to take effect:

    ``sudo service postgresql-9.4 restart``

16. Modify the file ``pg_hba.conf`` to allow the Mattermost server to communicate with the database.

  **If the Mattermost server and the database are on the same machine**:

    a. Open ``/var/lib/pgsql/9.4/data/pg_hba.conf`` as root in a text editor.

    b. Find the following line:

      ``local   all             all                        peer``

    c. Change ``peer`` to ``trust``:

      ``local   all             all                        trust``

  **If the Mattermost server and the database are on different machines**:

    a. Open ``/var/lib/pgsql/9.4/data/pg_hba.conf`` as root in a text editor.

    b. Add the following line to the end of the file, where *{mattermost-server-IP}* is the IP address of the machine that contains the Mattermost server.

      ``host all all {mattermost-server-IP}/32 md5``

17. Reload PostgreSQL:

  ``sudo service postgresql-9.4 reload``

18. Verify that you can connect with the user *mmuser*.

  a. If the Mattermost server and the database are on the same machine, use the following command:

    ``psql --dbname=mattermost --username=mmuser --password``

  b. If the Mattermost server is on a different machine, log into that machine and use the following command:

    ``psql --host={postgres-server-IP} --dbname=mattermost --username=mmuser --password``

    .. note::
      You might have to install the PostgreSQL client software to use the command.

  The PostgreSQL interactive terminal starts. To exit the PostgreSQL interactive terminal, type ``\q`` and press **Enter**.

With the database installed and the initial setup complete, you can now install the Mattermost server.
