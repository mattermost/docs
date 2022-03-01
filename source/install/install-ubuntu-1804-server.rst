.. _install-ubuntu-1804-server:

Installing Ubuntu Server 18.04 LTS
----------------------------------

Install the 64-bit version of Ubuntu Server on each machine that hosts one or more of the components.

**To install Ubuntu Server 18.04:**

1. To install Ubuntu Server 18.04, see the `Ubuntu Installation Guide. <https://help.ubuntu.com/18.04/installation-guide/amd64/index.html>`__

2. After the system is installed, make sure that it's up to date with the most recent security patches. Open a terminal window and issue the following commands:

  ``sudo apt update``

  ``sudo apt upgrade``

Now that the system is up to date, you can start installing the components that make up a Mattermost system.

**To uninstall For Ubuntu 18.04**

1. Stop the service: ``sudo service mattermost stop``
2. Disable the service: ``sudo systemctl disable mattermost``
3. Remove the service file: ``sudo rm /lib/systemd/system/mattermost.service``
4. Reload systemctl: ``systemctl daemon-reload``
  
**Warning: The following commands are permanent and irreversible:**
 
1. *Permanently* remove the Mattermost directory: ``sudo rm -rf /opt/mattermost``
2. *Permanently* delete the database: ``DROP DATABASE mattermost;``
