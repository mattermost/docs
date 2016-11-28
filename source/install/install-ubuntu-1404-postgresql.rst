Installing PostreSQL Database Server
====================================

Mattermost supports either PostgreSQL or MySQL.

Assume that the IP address of this server is 10.10.10.1

**To install PostgreSQL on Ubuntu Server:**

1.  Log into the server that will host the database and issue the following command:

    -  ``sudo apt-get install postgresql postgresql-contrib``

2.  PostgreSQL created a user account called ``postgres``. You will need
    to log into that account with:

    -  ``sudo -i -u postgres``

3.  You can get a PostgreSQL prompt by typing:

    -  ``psql``

4.  Create the Mattermost database by typing:

    -  ``postgres=# CREATE DATABASE mattermost;``

5.  Create the Mattermost user by typing:

    -  ``postgres=# CREATE USER mmuser WITH PASSWORD 'mmuser_password';``

6.  Grant the user access to the Mattermost database by typing:

    -  ``postgres=# GRANT ALL PRIVILEGES ON DATABASE mattermost to mmuser;``

7.  You can exit out of PostgreSQL by typing:

    -  ``postgre=# \q``

8.  You can exit the postgres account by typing:

    -  ``exit``

9. Allow Postgres to listen on all assigned IP Addresses

    -  ``sudo vi /etc/postgresql/9.3/main/postgresql.conf``
    -  Uncomment ``listen_addresses`` and change ``localhost`` to ``*``

10. Alter pg\_hba.conf to allow the mattermost server to talk to the
    postgres database

    -  ``sudo vi /etc/postgresql/9.3/main/pg_hba.conf``
    -  Add the following line to the ``IPv4 local connections``
    -  ``host all all 10.10.10.2/32 md5``

11. Reload Postgres database

    -  ``sudo /etc/init.d/postgresql reload``

    check with netstat command to see postgresql actually running on given ip and port

    - ``sudo netstat -anp | grep 5432``

    try restarting the postgresql service if reload won't work

    - ``sudo service postgresql restart``

12. Attempt to connect with the new created user to verify everything
    looks good

    -  ``psql --host=10.10.10.1 --dbname=mattermost --username=mmuser --password``
    -  ``mattermost=> \q``
