..  _install-rhel-8-mysql:

Installing MySQL Database Server
================================

Install and set up the database for use by the Mattermost server. You can install either MySQL or PostgreSQL.

**To install MySQL on RHEL 8:**

1. Log in to the server that will host the database, and open a terminal window.

2. Install MySQL.

  .. note::
    If you have additional questions for the process reference the MySQL docs `here <https://dev.mysql.com/doc/mysql-repo-excerpt/5.6/en/linux-installation-yum-repo.html>`_ that matches your system.
  
    1. If your RHEL is a fresh install, you'll need to add the `MySQL Yum repository <https://dev.mysql.com/doc/mysql-repo-excerpt/5.6/en/linux-installation-yum-repo.html>`_. You can also use the MySQL repo - https://repo.mysql.com/.
    
    2. Download the latest release package using wget: 
    
    ``wget https://dev.mysql.com/get/mysql80-community-release-el8-1.noarch.rpm``
        
    3. Once downloaded, install it: `sudo yum localinstall platform-and-version-specific-package-name.rpm`. This will be the rpm package you installed in step 2. Now run a `sudo yum update`, this could take some time.
    4. Next disable the system mysql: `sudo yum module disable mysql` and then install mysql

  ``sudo yum install mysql-community-server``

3. Start the MySQL server.

  ``sudo systemctl start mysqld.service``
  
  .. note::
    1. The first time that you start MySQL, the superuser account ``'root'@'localhost'`` is created with a password. Run the command below to get this password.
    
    ``sudo grep 'temporary password' /var/log/mysqld.log``
    
    2. Also the first time that you start MySQL, the ``validate_password`` plugin is installed. The plugin forces passwords to contain at least one upper case letter, one lower case letter, one digit, and one special character, and that the total password length is at least 8 characters.

4. Change the root password. Login with the the command below. Use the password found in `sudo grep 'temporary password' /var/log/mysqld.log`.

  ``mysql -u root -p``

5. Change the password. At the prompt, type the following command. Be sure to replace ``Password42!`` with the password that you want to use:

  ``mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'Password42!';``

6. Set MySQL to start automatically when the machine starts.

  ``sudo systemctl enable mysqld``

7. Create the Mattermost user *mmuser*.

  ``mysql> create user 'mmuser'@'%' identified by 'mmuser-password';``

  .. note::
    1. Use a password that is more secure than 'mmuser-password'.
    2. The '%' means that mmuser can connect from any machine on the network. However, it's more secure to use the IP address of the machine that hosts Mattermost. For example, if you install Mattermost on the machine with IP address 10.10.10.2, then use the following command:

      ``mysql> create user 'mmuser'@'10.10.10.2' identified by 'mmuser-password';``

8. Create the Mattermost database.

  ``mysql> create database mattermost;``

9. Grant access privileges to the user *mmuser*.

  ``mysql> grant all privileges on mattermost.* to 'mmuser'@'%';``

With the database installed and the initial setup complete, you can now install the Mattermost server.
