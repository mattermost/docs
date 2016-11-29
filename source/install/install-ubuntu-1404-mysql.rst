.. _install-ubuntu-1404-mysql:

Installing MySQL Database Server
================================

Mattermost supports either MySQL or PostgreSQL.

**To install MySQL 5.6 on Ubuntu Server:**

1. Log into the server that will host the database and open a terminal window.
2. Make sure that your package index is up to date. 

  ``sudo apt-get update``

3. Install MySQL version 5.6.
  
  ``sudo apt-get install mysql-server-5.6``
  
4. Log in to MySQL as root.
  
  ``mysql -u root -p``
  
  When prompted, enter the root password that you created when installing MySQL.

5. Create the Mattermost user 'mmuser'.

  ``mysql> create user 'mmuser'@'%' identified by 'mmuser-password';``

  **Notes**:

  1. Use a password that is more secure than 'mmuser-password'
  2. The '%' means that mmuser can connect from any machine on the network. However, it's more secure to use the IP address of the machine that hosts Mattermost. For example, if you install Mattermost on the machine with IP address 10.10.10.2, then use the following command:

  ``mysql> create user 'mmuser'@'10.10.10.2' identified by 'mmuser-password';``

6. Create the Mattermost database.

  ``mysql> create database mattermost;``

7. Grant access privileges to the user 'mmuser'

  ``mysql> grant all privileges on mattermost.* to 'mmuser'@'%';``

**What to do next**

In a production environment, you should install NGINX. Using NGINX as a proxy server increases the security and performance of your Mattermost installation.

**Related links**
  - :ref:`install-nginx`
