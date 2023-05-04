.. _install-debian:

Installing Mattermost on Debian Buster
=======================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Install a production-ready Mattermost system on up to three machines.

.. include:: install-common-intro.rst
  :start-after: :nosearch:

.. contents:: Install and configure the components in the following order.
  :depth: 2

.. include:: install-tar.rst
  :start-after: :nosearch:

Install a database
------------------

.. note:: 
  
  You only need one database: either PostgreSQL or MySQL. See the `database software </install/software-hardware-requirements.html#database-software>`__ documentation for details on database version support.

.. tabs::

    .. tab:: Install PostgreSQL

    Install and set up a PostgreSQL database for use by the Mattermost server. These instructions assume that the IP address of this server is ``10.10.10.1``.

    1. Log in to the server that will host the database, and install PostgreSQL. See the `PostgreSQL <https://www.postgresql.org/download/linux/debian/>`__ documentation for details. When the installation is complete, the PostgreSQL server is running, and a Linux user account called *postgres* has been created.

    2. Log in to the *postgres* account by running ``sudo --login --user postgres``.

    3. Start the PostgreSQL interactive terminal by running ``psql``.

    4. Create the Mattermost database by running ``postgres=# CREATE DATABASE mattermost;``.

    5. Create the Mattermost user 'mmuser' by running ``postgres=# CREATE USER mmuser WITH PASSWORD 'mmuser-password';``.

      .. note::
      
        Use a password that is more secure than ``mmuser-password``.

    6. Grant the user access to the Mattermost database by running ``postgres=# GRANT ALL PRIVILEGES ON DATABASE mattermost to mmuser;``.

    7. Exit the PostgreSQL interactive terminal by running ``postgres=# \q``.

    8. Log out of the *postgres* account by running ``exit``.

    9. (Optional) If you use separate servers for your database and the Mattermost app server, you may allow PostgreSQL to listen on all assigned IP Addresses. To do so, open ``/etc/postgresql/{version}/main/postgresql.conf`` as *root* in a text editor, and replacing ``{version}`` with the version of PostgreSQL that's currently running. As a best practice, ensure that only the Mattermost server is able to connect to the PostgreSQL port using a firewall.

      a. Find the following line: ``#listen_addresses = 'localhost'``.

      b. Uncomment the line and change ``localhost`` to ``*``: ``listen_addresses = '*'``.

      c. Restart PostgreSQL for the change to take effect: ``sudo systemctl restart postgresql``.

    10. Modify the file ``pg_hba.conf`` to allow the Mattermost server to communicate with the database.

      **If the Mattermost server and the database are on the same machine**:

        a. Open ``/etc/postgresql/9.4/main/pg_hba.conf`` in a text editor as *root* user.

        b. Find the following lines:

          ``local   all             all                        peer``
      
          ``host    all             all         ::1/128        ident``

        c. Change ``peer`` and ``ident`` to ``trust``:

          ``local   all             all                        trust``
      
          ``host    all             all         ::1/128        trust``

      **If the Mattermost server and the database are on different machines**:

        a. Open ``/etc/postgresql/9.4/main/pg_hba.conf`` in a text editor as *root* user.

        b. Add the following line to the end of the file, where ``{mattermost-server-IP}`` is the IP address of the machine that contains the Mattermost server: ``host all all {mattermost-server-IP}/32 md5``.

    11. Reload PostgreSQL by running ``sudo systemctl reload postgresql``.

    12. Verify that you can connect with the user *mmuser*.

      a. If the Mattermost server and the database are on the same machine, use the following command: ``psql --dbname=mattermost --username=mmuser --password``

      b. If the Mattermost server is on a different machine, log into that machine and use the following command: ``psql --host={postgres-server-IP} --dbname=mattermost --username=mmuser --password``

    .. note::
      
      You might have to install the PostgreSQL client software to use the command.

    The PostgreSQL interactive terminal starts. To exit the PostgreSQL interactive terminal, type ``\q`` and press :kbd:`Enter` on Windows or Linux, or :kbd:`↵` on Mac. 
    
    With the database installed and the initial setup complete, you can now install the Mattermost server.

  .. tab:: Install MySQL

    Install and set up a MySQL database for use by the Mattermost server.

    1. Log into the server that will host the database, and open a terminal window.

    2. Download the MySQL repository package by running ``wget https://dev.mysql.com/get/mysql-apt-config_0.8.13-1_all.deb``.

    3. Install the repository by running ``sudo dpkg -i mysql-apt-config*``.

    4. Update your local package list by running ``sudo apt-get update``.

    5. Add the MySQL repo MySQL by running ``sudo apt-get install mysql-server``.

      .. note::
    
        During the install, you'll be prompted to create a password for the MySQL root user. Make a note of the password because you'll need it in the next step.

    6. Log in to MySQL as *root* by running ``mysql -u root -p``. When prompted, enter the root password that you created when installing MySQL.

    7. Create the Mattermost user ``mmuser`` by running ``mysql> create user 'mmuser'@'%' identified by 'mmuser-password';``.

      .. note::
    
        - Use a password that is more secure than ``mmuser-password``.
        - The ``%`` means that mmuser can connect from any machine on the network. However, it's more secure to use the IP address of the machine that hosts Mattermost. For example, if you install Mattermost on the machine with IP address 10.10.10.2, then use the following command: ``mysql> create user 'mmuser'@'10.10.10.2' identified by 'mmuser-password';``.

    8. Create the Mattermost database by running ``mysql> create database mattermost;``.

    9. Grant access privileges to the user ``mmuser`` by running ``mysql> grant all privileges on mattermost.* to 'mmuser'@'%';``.
  
      .. note::
    
        This query grants the MySQL user we just created all privileges on the database for convenience. If you need more security, you can use the following query to grant the user only the privileges necessary to run Mattermost: ``mysql> GRANT ALTER, CREATE, DELETE, DROP, INDEX, INSERT, SELECT, UPDATE, REFERENCES ON mattermost.* TO 'mmuser'@'%';``.

    10. Log out of MySQL by running ``mysql> exit``. Once the database is installed, and the initial setup is complete, you can install the Mattermost server.

.. include:: config-mattermost-server.rst
  :start-after: :nosearch:

.. include:: config-tls-mattermost.rst
  :start-after: :nosearch:

.. include:: install-nginx.rst
  :start-after: :nosearch:

.. include:: config-proxy-nginx.rst
  :start-after: :nosearch:

.. include:: config-ssl-http2-nginx.rst
  :start-after: :nosearch: