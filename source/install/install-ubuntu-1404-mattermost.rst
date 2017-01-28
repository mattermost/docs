.. _install-ubuntu-1404-mattermost:

Installing Mattermost Server
============================

Install Mattermost Server on a 64-bit machine.

Assume that the IP address of this server is 10.10.10.2

**To install Mattermost Server on Ubuntu**

1. Log in to the server that will host Mattermost Server and open a terminal window.

2. Download `the latest version of the Mattermost Server <https://about.mattermost.com/download/>`_. In the following command, replace ``X.X.X`` with the version that you want to download:

  ``wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz``

5. Extract the Mattermost Server files.

  ``tar -xvzf mattermost*.gz``

3. Move the extracted file to the ``/opt`` directory.

  ``sudo mv mattermost /opt``

4. Create the storage directory for files.

  ``sudo mkdir /opt/mattermost/data``

  .. note::
    The storage directory will contain all the files and images that your users post to Mattermost, so you need to make sure that the drive is large enough to hold the anticipated number of uploaded files and images.

5. Set up a system user and group called ``mattermost`` that will run this service, and set the ownership and permissions.

  a. Create the Mattermost user and group:
    ``sudo useradd --system --user-group mattermost``
  b. Set the user and group *mattermost* as the owner of the Mattermost files:
    ``sudo chown -R mattermost:mattermost /opt/mattermost``
  c. Give write permissions to the *mattermost* group:
    ``sudo chmod -R g+w /opt/mattermost``

6. Set up the database driver in the file ``/opt/mattermost/config/config.json``. Open the file in a text editor and make the following changes:

  -  If you are using PostgreSQL:    
    1.  Set ``"DriverName"`` to ``"postgres"``
    2.  Set ``"DataSource"`` to the following value, replacing ``<mmuser-password>``  and ``<host-name-or-IP>`` with the appropriate values:
     ``"postgres://mmuser:<mmuser-password>@<host-name-or-IP>:5432/mattermost?sslmode=disable&connect_timeout=10"``.
  -  If you are using MySQL:    
    1.  Set ``"DriverName"`` to ``"mysql"``
    2.  Set ``"DataSource"`` to the following value, replacing ``<mmuser-password>``  and ``<host-name-or-IP>`` with the appropriate values:
      ``"mmuser:<mmuser-password>@tcp(<host-name-or-IP>:3306)/mattermost?charset=utf8"``

7. Test the Mattermost server to make sure everything works.

    a. Change to the ``bin`` directory:
      ``cd /opt/mattermost/bin``
    b. Start the Mattermost server as the user mattermost:
      ``sudo -u mattermost ./platform``
   
  When the server starts, it shows some log information and the text ``Server is listening on :8065``. You can stop the server by typing ``CTRL+C`` in the terminal window.
  
8. Setup Mattermost to use the Upstart daemon which handles supervision of the Mattermost process.

  a. Create the configuration file.
  
    ``sudo touch /etc/init/mattermost.conf``
  
  b. Open the config file as root in a text editor, and copy the following lines into the file:

    .. code-block:: none

      start on runlevel [2345]
      stop on runlevel [016]
      respawn
      limit nofile 50000 50000
      chdir /home/mattermost/mattermost
      setuid mattermost
      exec bin/platform

  c. Start the Mattermost server.
  
    ``sudo start mattermost``
  
  d. Verify that the service is running.
  
    ``curl http://localhost:8065``
  
    You should see the HTML that's returned by the Mattermost server.

Now that the Mattermost server is up and running, you can do some initial configuration and setup.
