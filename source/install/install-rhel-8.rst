.. _install-rhel-8:

Install Mattermost on RHEL 8
=============================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

You can also use these instructions to install Mattermost on CentOS 8 or Oracle Linux 8. With the exception of the operating system that you install, the process is identical.

.. include:: install-common-intro.rst
    :start-after: :nosearch:

.. contents:: Install and configure the components in the following order.
  :depth: 2

.. include:: install-rhel-8-server.rst
    :start-after: :nosearch:

Install a database
------------------

.. note:: 
  
  You only need one database: either PostgreSQL or MySQL. See the `database software </install/software-hardware-requirements.html#database-software>`__ documentation for details on database version support.

.. tabs::

  .. tab:: Install PostgreSQL

    Install and set up a PostgreSQL database for use by the Mattermost server. 

    1. Log in to the server that will host the database, and open a terminal window.

    2. Install PostgreSQL. See the `PostgreSQL <https://www.postgresql.org/download/linux/redhat/>`__ documentation for details. 

    3. Initialize the database by running ``sudo postgresql-setup initdb``.

    4. Set PostgreSQL to start on boot by running ``sudo systemctl enable postgresql``.

    5. Start the PostgreSQL server by running ``sudo systemctl start postgresql``.

    6. Switch to the *postgres* Linux user account that was created during the installation by running ``sudo -iu postgres``.

    7. Start the PostgreSQL interactive terminal by running ``psql``.

    8.  Create the Mattermost database by running ``postgres=# CREATE DATABASE mattermost WITH ENCODING 'UTF8' LC_COLLATE='en_US.UTF-8' LC_CTYPE='en_US.UTF-8' TEMPLATE=template0;``.

    9.  Create the Mattermost user *mmuser* by running ``postgres=# CREATE USER mmuser WITH PASSWORD 'mmuser-password';``.

        .. note::
    
            Use a password that is more secure than ``mmuser-password``.

    10.  Grant the user access to the Mattermost database by running ``postgres=# GRANT ALL PRIVILEGES ON DATABASE mattermost to mmuser;``.

    11. Exit the PostgreSQL interactive terminal by running ``postgres=# \q``.

    12. Log out of the *postgres* account by running ``exit``.

    13. (Optional) If you use separate servers for your database and the Mattermost app server, you may allow PostgreSQL to listen on all assigned IP Addresses. To do so, open ``/etc/postgresql/{version}/main/postgresql.conf`` as *root* in a text editor, and replacing ``{version}`` with the version of PostgreSQL that's currently running. As a best practice, ensure that only the Mattermost server is able to connect to the PostgreSQL port using a firewall.

        a. Open ``/var/lib/pgsql/data/postgresql.conf`` as root in a text editor.

        b. Find the following line: ``#listen_addresses = 'localhost'``.

        c. Uncomment the line and change ``localhost`` to ``*``: ``listen_addresses = '*'``.

        d. Restart PostgreSQL for the change to take effect: ``sudo systemctl restart postgresql``.

    14. Modify the file ``pg_hba.conf`` to allow the Mattermost server to communicate with the database.

        **If the Mattermost server and the database are on the same machine:**

            a. Open ``/var/lib/pgsql/data/pg_hba.conf`` as root in a text editor.

            b. Find the following lines:

             ``local   all             all                        peer``
      
             ``host    all             all         ::1/128        ident``

            c. Change ``peer`` and ``ident`` to ``trust``:

             ``local   all             all                        trust``
      
             ``host    all             all         ::1/128        trust``

        **If the Mattermost server and the database are on different machines:**

            a. Open ``/var/lib/pgsql/data/pg_hba.conf`` as *root* in a text editor.

            b. Add the following line to the end of the file, where *{mattermost-server-IP}* is the IP address of the machine that contains the Mattermost server: ``host all all {mattermost-server-IP}/32 md5``.

    15. Reload PostgreSQL by running ``sudo systemctl reload postgresql``.

    16. Verify that you can connect with the user *mmuser*.

        a. If the Mattermost server and the database are on the same machine, use the following command: ``psql --dbname=mattermost --username=mmuser --password``.

        b. If the Mattermost server is on a different machine, log into that machine and use the following command: ``psql --host={postgres-server-IP} --dbname=mattermost --username=mmuser --password``.

        .. note::
      
            You might have to install the PostgreSQL client software to use the command.

    The PostgreSQL interactive terminal starts. To exit the PostgreSQL interactive terminal, type ``\q`` and press **Enter**.

    With the database installed and the initial setup complete, you can now install the Mattermost server.

      .. tab:: Install MySQL

    Install and set up a MySQL database for use by the Mattermost server.

    1. Log in to the server that will host the database, and open a terminal window.

    2. Install MySQL.

    3. Download and install the latest release package.

    4. Disable the system MySQL by running ``sudo yum module disable mysql``, and install MySQL by running ``sudo yum install mysql-community-server``.

    5. Start the MySQL server by running ``sudo systemctl start mysqld.service``.
  
        .. note::
   
            The first time that you start MySQL:
        
            - The superuser account ``'root'@'localhost'`` is created with a password. Get this password by running ``sudo grep 'temporary password' /var/log/mysqld.log``. 
            - The ``validate_password`` plugin is installed. The plugin forces passwords to contain at least one upper case letter, one lower case letter, one digit, and one special character, and that the total password length is at least eight characters.

    6. Change the root password. 

    7. Set MySQL to start automatically when the machine starts by running ``sudo systemctl enable mysqld``.

    8. Create the Mattermost user *mmuser* by running ``mysql> create user 'mmuser'@'%' identified by 'mmuser-password';``.

        .. note::
        
            - Use a password that's more secure than ``mmuser-password``.
            - The ``%`` means that mmuser can connect from any machine on the network. However, it's more secure to use the IP address of the machine that hosts Mattermost. For example, if you install Mattermost on the machine with IP address ``10.10.10.2``, then use the following command: ``mysql> create user 'mmuser'@'10.10.10.2' identified by 'mmuser-password';``.

    9. Create the Mattermost database by running ``mysql> create database mattermost;``.

    10. Grant access privileges to the user mmuser by running ``mysql> grant all privileges on mattermost.* to 'mmuser'@'%';``.
  
        .. note::
    
            This query grants the MySQL user all privileges on the database for convenience. If you need more security, you can use the following query to grant the user only the privileges necessary to run Mattermost: ``mysql> GRANT ALTER, CREATE, DELETE, DROP, INDEX, INSERT, SELECT, UPDATE, REFERENCES ON mattermost.* TO 'mmuser'@'%';``.
    
    11. Log out of MySQL by running ``mysql> exit``.

    With the database installed and the initial setup complete, you can now install the Mattermost server.

.. include:: install-rhel-8-mattermost.rst
    :start-after: :nosearch:

.. include:: config-mattermost-server.rst
    :start-after: :nosearch:

.. include:: config-tls-mattermost.rst
    :start-after: :nosearch:

.. include:: install-rhel-nginx.rst
    :start-after: :nosearch:

.. include:: config-proxy-nginx.rst
    :start-after: :nosearch:

.. include:: config-ssl-http2-nginx.rst
    :start-after: :nosearch: