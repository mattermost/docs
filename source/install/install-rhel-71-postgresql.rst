..  _install-rhel-71-postgresql:

Installing PostgreSQL Database
==============================

1.  For the purposes of this guide we will assume this server has an IP
    address of ``10.10.10.1``

    -  **Optional:** if installing on the same machine substitute
       ``10.10.10.1`` with ``127.0.0.1``

2.  Install PostgreSQL 9.4+ (or MySQL 5.6+)

    -  ``sudo yum install     yum install http://yum.postgresql.org/9.4/redhat/rhel-7-x86_64/pgdg-redhat94-9.4-1.noarch.rpm``
    -  ``sudo yum install postgresql94-server postgresql94-contrib``
    -  ``sudo /usr/pgsql-9.4/bin/postgresql94-setup initdb``
    -  ``sudo systemctl enable postgresql-9.4.service``
    -  ``sudo systemctl start postgresql-9.4.service``

3.  PostgreSQL created a user account called ``postgres``. You will need
    to log into that account with:

    -  ``sudo -i -u postgres``

4.  You can get a PostgreSQL prompt by typing:

    -  ``psql``

5.  Create the Mattermost database by typing:

    -  ``postgres=# CREATE DATABASE mattermost;``

6.  Create the Mattermost user by typing:

    -  ``postgres=# CREATE USER mmuser WITH PASSWORD 'mmuser_password';``

7.  Grant the user access to the Mattermost database by typing:

    -  ``postgres=# GRANT ALL PRIVILEGES ON DATABASE mattermost to mmuser;``

8.  You can exit out of PostgreSQL by typing:

    -  ``postgres=# \q``

9.  You can exit the Postgres account by typing:

    -  ``exit``

10. Allow Postgres to listen on all assigned IP Addresses:

    -  ``sudo vi /var/lib/pgsql/9.4/data/postgresql.conf``
    -  Uncomment ``listen_addresses`` and change ``localhost`` to ``\*``

11. Alter ``pg_hba.conf`` to allow the Mattermost Server to talk to the
    Postgres database:

    -  ``sudo vi /var/lib/pgsql/9.4/data/pg_hba.conf``
    -  Add the following line to the ``IPv4 local connections``:
    -  ``host all all 10.10.10.2/32 md5``

12. Reload Postgres database:

    -  ``sudo systemctl reload postgresql-9.4.service``

13. Attempt to connect with the new created user to verify everything
    looks good:

    -  ``psql --host=10.10.10.1 --dbname=mattermost --username=mmuser --password``
    -  ``mattermost=> \q``
