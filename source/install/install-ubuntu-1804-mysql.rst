.. _install-ubuntu-1804-mysql:

Installing MySQL Database Server
--------------------------------

Install and set up the database for use by the Mattermost server. You can install either MySQL or PostgreSQL.

**To install MySQL on Ubuntu Server 18.04:**

1. Log into the server that will host the database, and open a terminal window.

2. Install MySQL.

  ``sudo apt install mysql-server``

3. Run ``mysql_secure_installation`` and follow the instructions.

  ``sudo mysql_secure_installation``

4. Log in to MySQL as root.

  ``sudo mysql``

5. Create the Mattermost user 'mmuser'.

  ``mysql> create user 'mmuser'@'%' identified by 'mmuser-password';``

  .. note::
    1. Use a password that is more secure than 'mmuser-password'.
    2. The '%' means that mmuser can connect from any machine on the network. However, it's more secure to use the IP address of the machine that hosts Mattermost. For example, if you install Mattermost on the machine with IP address 10.10.10.2, then use the following command: ``mysql> create user 'mmuser'@'10.10.10.2' identified by 'mmuser-password';``

6. Create the Mattermost database.

  ``mysql> create database mattermost;``

7. Grant access privileges to the user 'mmuser'.

  ``mysql> grant all privileges on mattermost.* to 'mmuser'@'%';``

  .. note::
    This query grants the MySQL user we just created all privileges on the database for convenience. If you need more security you can use this query to grant the user only the privileges necessary to run Mattermost.

    ``mysql> GRANT ALTER, CREATE, DELETE, DROP, INDEX, INSERT, SELECT, UPDATE, REFERENCES ON mattermost.* TO 'mmuser'@'%';``

8. Log out of MySQL.

   ``mysql> exit``

   .. note::
    If you have installed MySQL on its own server, you need to edit the ``/etc/mysql/mysql.conf.d/mysqld.cnf`` file and comment out the ``bind-address = 127.0.0.1`` using the ``#`` symbol, then restart your sql server.




With the database installed and the initial setup complete, you can now install the Mattermost server.
