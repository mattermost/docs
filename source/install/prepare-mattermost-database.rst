Prepare your Mattermost database
================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. note:: 
  
  You need one database: either PostgreSQL or MySQL, and PostgreSQL is our preferred database of choice. See the `database software </install/software-hardware-requirements.html#database-software>`__ documentation for details on database version support.

.. tabs::

  .. tab:: Install PostgreSQL

    Install and set up a PostgreSQL database for use by the Mattermost server. These instructions assume that the IP address of this server is ``10.10.10.1``.

    1. Log in to the server that will host the database, and install PostgreSQL. See the `PostgreSQL <https://www.postgresql.org/download/>`__ documentation for details. When the installation is complete, the PostgreSQL server is running, and a Linux user account called *postgres* has been created.

    2. Access PostgreSQL by running:
    
        .. code-block:: none
          :class: mm-code-block 
    
            sudo -u postgres psql
  
    3. Create the Mattermost database by running:

        .. code-block:: none
          :class: mm-code-block 
    
            postgres=# CREATE DATABASE mattermost;

    4. Create the Mattermost user *mmuser* by running the following command. Ensure you use a password that's more secure than ``mmuser-password``.

        .. code-block:: none
          :class: mm-code-block 
    
            postgres=# CREATE USER mmuser WITH PASSWORD 'mmuser-password';
  
    5. If you're configuring PostgreSQL v15.x or later:
    
      a. Grant the user access to the Mattermost database by running:

          .. code-block:: none
            :class: mm-code-block 
    
              postgres=# GRANT ALL PRIVILEGES ON DATABASE mattermost to mmuser;
     
      b. Grant access to objects contained in the specified schema by running: 

          .. code-block:: none
            :class: mm-code-block 
    
              GRANT USAGE, CREATE ON SCHEMA PUBLIC TO mmuser;

    6. Exit the PostgreSQL interactive terminal by running:

        .. code-block:: none
          :class: mm-code-block 
    
            postgres=# \q

    7. (Optional) If you use separate servers for your database and the Mattermost server, you may allow PostgreSQL to listen on all assigned IP addresses by opening ``/etc/postgresql/{version}/main/postgresql.conf`` as *root* in a text editor, and replacing ``{version}`` with the version of PostgreSQL that's currently running. 
    
      As a best practice, ensure that only the Mattermost server is able to connect to the PostgreSQL port using a firewall.

        a. Find the following line: ``#listen_addresses = 'localhost'``

        b. Uncomment the line and change ``localhost`` to ``*``: ``listen_addresses = '*'``

        c. Restart PostgreSQL for the change to take effect by running:

          .. code-block:: none
            :class: mm-code-block 
    
              sudo systemctl restart postgresql

    8. Modify the file ``pg_hba.conf`` to allow the Mattermost server to communicate with the database by ensuring host connection types are set to ``trust``.

      **Note**: These host connections are specific to Ubuntu 20.04, and will differ depending on the operating system you're running. For example, in Ubuntu 22.04, the ``peer`` connection types are listed as ``sha-256`` instead.

        **If the Mattermost server and the database are on the same machine:**

        a. Open ``/etc/postgresql/{version}/main/pg_hba.conf`` as *root* in a text editor.

        b.  Find the following lines:

          ``local   all             all                        peer``
      
          ``host    all             all         ::1/128        ident``

        c. Change ``peer`` and ``ident`` to ``trust``:

          ``local   all             all                        trust``
      
          ``host    all             all         ::1/128        trust``

        **If the Mattermost server and the database are on different machines:**

        a. Open ``/etc/postgresql/{version}/main/pg_hba.conf`` in a text editor as *root* user.

        b. Add the following line to the end of the file, where ``{mattermost-server-IP}`` is the IP address of the Mattermost server: ``host all all {mattermost-server-IP}/32 md5``.

    9. Reload PostgreSQL by running .

        .. code-block:: none
          :class: mm-code-block 
    
            sudo systemctl reload postgresql

    10. Verify that you can connect with the user *mmuser*.

      If the Mattermost server and the database are on the same machine, use the following command: 

        .. code-block:: none
          :class: mm-code-block 
    
            psql --dbname=mattermost --username=mmuser --password

      If the Mattermost server is on a different machine, log into that machine and use the following command: 

        .. code-block:: none
          :class: mm-code-block 
    
            psql --host={postgres-server-IP} --dbname=mattermost --username=mmuser --password

    .. note::

      You might have to install the PostgreSQL client software to use the command.

    The PostgreSQL interactive terminal starts. To exit the PostgreSQL interactive terminal, type ``\q`` and press :kbd:`Enter` on Windows or Linux, or :kbd:`↵` on Mac.

    When the PostgreSQL database is installed, and the initial setup complete, you can install the Mattermost server.

  .. tab:: Install MySQL
    
    Install and set up a MySQL database for use by the Mattermost server.

    1. Log into the server that will host the database, and open a terminal window.

    2. Install MySQL.

    3. Run ``sudo mysql_secure_installation`` and follow the instructions.

    4. Log in to MySQL as *root* by running ``sudo mysql``.

    5. Create the Mattermost user *mmuser* by running ``mysql> create user 'mmuser'@'%' identified by 'mmuser-password';``. 
    
      - Use a password that is more secure than ``mmuser-password``.
      - The ``%`` means that mmuser can connect from any machine on the network. However, it's more secure to use the IP address of the machine that hosts Mattermost. For example, if you install Mattermost on the machine with IP address 10.10.10.2, then use the following command: ``mysql> create user 'mmuser'@'10.10.10.2' identified by 'mmuser-password';``

    6. Create the Mattermost database by running ``mysql> create database mattermost;``.

    7. Grant access privileges to the user *mmuser* by running ``mysql> grant all privileges on mattermost.* to 'mmuser'@'%';``.

      .. note::
      
        This query grants the MySQL user we just created all privileges on the database for convenience. If you need more security, use the following query to grant the user only the privileges necessary to run Mattermost: ``mysql> GRANT ALTER, CREATE, DELETE, DROP, INDEX, INSERT, SELECT, UPDATE, REFERENCES ON mattermost.* TO 'mmuser'@'%';``

    8. Log out of MySQL by running ``mysql> exit``. Once the database is installed and the initial setup is complete, you can install the Mattermost server.