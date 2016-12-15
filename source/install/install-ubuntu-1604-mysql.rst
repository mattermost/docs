.. _install-ubuntu-1604-mysql:

Installing MySQL Database Server
================================

You can install either MySQL or PostgreSQL. To install PostgreSQL, see :ref:`install-ubuntu-1604-postgresql`

**To install MySQL on Ubuntu Server 16.04:**

1. Log into the server that will host the database, and open a terminal window.

2. Install MySQL.
  
  ``sudo apt-get install mysql-server``
  
  .. note::
    During the install, you'll be prompted to create a password for the MySQL root user. Make a note of the password because you'll need it in the next step.
  
3. Log in to MySQL as root.
  
  ``mysql -u root -p``
  
  When prompted, enter the root password that you created when installing MySQL.

4. Create the Mattermost user 'mmuser'.

  ``mysql> create user 'mmuser'@'%' identified by 'mmuser-password';``

  .. note::
    1. Use a password that is more secure than 'mmuser-password'
    2. The '%' means that mmuser can connect from any machine on the network. However, it's more secure to use the IP address of the machine that hosts Mattermost. For example, if you install Mattermost on the machine with IP address 10.10.10.2, then use the following command:

  ``mysql> create user 'mmuser'@'10.10.10.2' identified by 'mmuser-password';``

5. Create the Mattermost database.

  ``mysql> create database mattermost;``

6. Grant access privileges to the user 'mmuser'

  ``mysql> grant all privileges on mattermost.* to 'mmuser'@'%';``

7. Log out of MySQL.
 
   ``mysql> exit``

With the database installed and the initial setup complete, you can now install the Mattermost server.
