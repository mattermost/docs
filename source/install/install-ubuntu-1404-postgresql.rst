.. _install-ubuntu-1404-postgresql:

Installing PostgreSQL Database Server
=====================================

Install and set up the database for use by the Mattermost server. You can install either PostgreSQL or MySQL. To install MySQL, see :ref:`install-ubuntu-1404-mysql`

Assume that the IP address of this server is 10.10.10.1

**To install PostgreSQL on Ubuntu Server 14.04:**

1. Log into the server that will host the database and issue the following command:

  ``sudo apt-get install postgresql postgresql-contrib``
  
  When the installation is complete, the PostgreSQL server is running, and a Linux user account called *postgres* has been created.

2. Log into the *postgres* account. 

  ``sudo --login --user postgres``

3. Start the PostgreSQL interactive terminal.

  ``psql``

4.  Create the Mattermost database.

  ``postgres=# CREATE DATABASE mattermost;``

5.  Create the Mattermost user *mmuser*.

  ``postgres=# CREATE USER mmuser WITH PASSWORD 'mmuser_password';``
  
  .. note::
    Use a password that is more secure than 'mmuser-password'.

6.  Grant the user access to the Mattermost database.

  ``postgres=# GRANT ALL PRIVILEGES ON DATABASE mattermost to mmuser;``

7. Exit the PostgreSQL interactive terminal.

  ``postgre=# \q``

8. Log out of the *postgres* account.

  ``exit``

9. Allow Postgres to listen on all assigned IP Addresses. Open ``/etc/postgresql/9.3/main/postgresql.conf`` as root in a text editor.

  a. Find the following line:
  
    ``#listen_addresses = 'localhost'``
    
  b. Uncomment the line and change ``localhost`` to ``*``.
  
    ``listen_addresses = '*'``

10. If the Mattermost server is on a separate machine, modify the file ``pg_hbe.conf`` to allow the Mattermost server to communicate with the database.

  If the Mattermost server and the database are on the same machine, then you can skip this step.

  a. Open ``/etc/postgresql/9.3/main/pg_hba.conf`` in a text editor.

  b. Add the following line to the end of the file, where *<mm-server-IP>* is the IP address of the machine that contains the Mattermost server.

    ``host all all <mm-server-IP>/32 md5``

11. Reload Postgres database.

  ``sudo /etc/init.d/postgresql reload``

12. Verify that you can connect with the user *mmuser*.
  
  ``psql --host=localhost --dbname=mattermost --username=mmuser --password``
  
  The PostgreSQL interactive terminal starts. To exit the PostgreSQL interactive terminal, type ``\q`` and press **Enter**.

With the database installed and the initial setup complete, you can now install the Mattermost server.
