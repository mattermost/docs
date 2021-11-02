.. _install-debian-mysql:

Installing MySQL Database Server
--------------------------------

Install and set up the database for use by the Mattermost server. You can install either MySQL or PostgreSQL.

**To install MySQL on Debian Buster:**

1. Log into the server that will host the database, and open a terminal window.

2. Download the MySQL repository package.

  ``wget https://dev.mysql.com/get/mysql-apt-config_0.8.13-1_all.deb``

3. Install the repository

  ``sudo dpkg -i mysql-apt-config*``

4. Update your local package list.

  ``sudo apt-get update``

5. Add the MySQL repo MySQL.

  ``sudo apt-get install mysql-server``

  .. note::
    During the install, you'll be prompted to create a password for the MySQL root user. Make a note of the password because you'll need it in the next step.

6. Log in to MySQL as root.

  ``mysql -u root -p``

  When prompted, enter the root password that you created when installing MySQL.

7. Create the Mattermost user 'mmuser'.

  ``mysql> create user 'mmuser'@'%' identified by 'mmuser-password';``

  .. note::
    1. Use a password that is more secure than 'mmuser-password'.
    2. The '%' means that mmuser can connect from any machine on the network. However, it's more secure to use the IP address of the machine that hosts Mattermost. For example, if you install Mattermost on the machine with IP address 10.10.10.2, then use the following command:

  ``mysql> create user 'mmuser'@'10.10.10.2' identified by 'mmuser-password';``

8. Create the Mattermost database.

  ``mysql> create database mattermost;``

9. Grant access privileges to the user 'mmuser'.

  ``mysql> grant all privileges on mattermost.* to 'mmuser'@'%';``
  
  .. note::
    This query grants the MySQL user we just created all privileges on the database for convenience. If you need more security you can use this query to grant the user only the privileges necessary to run Mattermost.
    
    ``mysql> GRANT ALTER, CREATE, DELETE, DROP, INDEX, INSERT, SELECT, UPDATE, REFERENCES ON mattermost.* TO 'mmuser'@'%';``

10. Log out of MySQL.

  ``mysql> exit``

With the database installed and the initial setup complete, you can now install the Mattermost server.
