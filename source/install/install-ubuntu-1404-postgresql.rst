Set up PostreSQL
================

1.  For the purposes of this guide we will assume this server has an IP
    address of 10.10.10.1
2.  Install PostgreSQL 9.3+

    -  ``sudo apt-get install postgresql postgresql-contrib``

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

    -  ``postgre=# \q``

9.  You can exit the postgres account by typing:

    -  ``exit``

10. Allow Postgres to listen on all assigned IP Addresses

    -  ``sudo vi /etc/postgresql/9.3/main/postgresql.conf``
    -  Uncomment ``listen_addresses`` and change ``localhost`` to ``*``

11. Alter pg\_hba.conf to allow the mattermost server to talk to the
    postgres database

    -  ``sudo vi /etc/postgresql/9.3/main/pg_hba.conf``
    -  Add the following line to the ``IPv4 local connections``
    -  ``host all all 10.10.10.2/32 md5``

12. Reload Postgres database

    -  ``sudo /etc/init.d/postgresql reload``

    check with netstat command to see postgresql actually running on given ip and port

    - ``sudo netstat -anp | grep 5432``

    try restarting the postgresql service if reload won't work

    - ``sudo service postgresql restart``

13. Attempt to connect with the new created user to verify everything
    looks good

    -  ``psql --host=10.10.10.1 --dbname=mattermost --username=mmuser --password``
    -  ``mattermost=> \q``
