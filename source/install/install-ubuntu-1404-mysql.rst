.. _install-ubuntu-1404-mysql:

Installing MySQL Database Server
================================

You can install either MySQL or PostgreSQL. The MySQL version must be 5.6 or greater.

To install PostgreSQL, see :ref:`install-ubuntu-1404-postgresql`

**To install MySQL 5.6 on Ubuntu Server:**

1. Log into the server that will host the database, and open a terminal window.

2. Install MySQL version 5.6.
  
  ``sudo apt-get install mysql-server-5.6``
  
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
