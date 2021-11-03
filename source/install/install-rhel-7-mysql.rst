..  _install-rhel-7-mysql:

Installing MySQL Database Server
--------------------------------

Install and set up the database for use by the Mattermost server. You can install either MySQL or PostgreSQL.

**To install MySQL 5.7 on RHEL 7:**

1. Log in to the server that will host the database, and open a terminal window.

2. Download the MySQL Yum repository from dev.mysql.com.

  ``wget http://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm``

3. Install the Yum repository from the file that you downloaded.

  ``sudo yum localinstall mysql57-community-release-el7-9.noarch.rpm``

4. Install MySQL.

  ``sudo yum install mysql-community-server``

5. Start the MySQL server.

  ``sudo systemctl start mysqld.service``
  
  .. note::
    1. The first time that you start MySQL, the superuser account ``'root'@'localhost'`` is created and a temporary password is generated for it.
    2. Also the first time that you start MySQL, the ``validate_password`` plugin is installed. The plugin forces passwords to contain at least one upper case letter, one lower case letter, one digit, and one special character, and that the total password length is at least 8 characters.

6. Obtain the root password that was generated when you started MySQL for the first time.

  ``sudo grep 'temporary password' /var/log/mysqld.log``

7. Change the root password. Login with the password that you obtained from the previous step.

  ``mysql -u root -p``

8. Change the password. At the mysql prompt, type the following command. Be sure to replace ``Password42!`` with the password that you want to use.

  ``mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'Password42!';``

9. Set MySQL to start automatically when the machine starts.

  ``sudo systemctl enable mysqld``

10. Create the Mattermost user 'mmuser'.

  ``mysql> create user 'mmuser'@'%' identified by 'mmuser-password';``

  .. note::
    1. Use a password that is more secure than 'mmuser-password'.
    2. The '%' means that mmuser can connect from any machine on the network. However, it's more secure to use the IP address of the machine that hosts Mattermost. For example, if you install Mattermost on the machine with IP address 10.10.10.2, then use the following command:

      ``mysql> create user 'mmuser'@'10.10.10.2' identified by 'mmuser-password';``

11. Create the Mattermost database.

  ``mysql> create database mattermost;``

12. Grant access privileges to the user 'mmuser'.

  ``mysql> grant all privileges on mattermost.* to 'mmuser'@'%';``
  
  .. note::
    This query grants the MySQL user we just created all privileges on the database for convenience. If you need more security you can use this query to grant the user only the privileges necessary to run Mattermost.
    
    ``mysql> GRANT ALTER, CREATE, DELETE, DROP, INDEX, INSERT, SELECT, UPDATE, REFERENCES ON mattermost.* TO 'mmuser'@'%';``
    
13. Log out of MySQL.

    ``mysql> exit``

With the database installed and the initial setup complete, you can now install the Mattermost server.
