Set up Mattermost Server
========================

For the purposes of this guide we will assume this server has an IP address of ``10.10.10.2``

1. Create a mattermost user and group

    - ``sudo adduser --system --group mattermost``

2. Change to the mattermost home directory.

    ``cd /home/mattermost``

3. Download `the latest version of the Mattermost Server <https://docs.mattermost.com/administration/upgrade.html#version-archive>`_ by typing:

   -  ``wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz``
   -  Where ``vX.X.X`` is the latest version.

4. Extract the Mattermost Server files by typing:

   -  ``sudo tar -xvzf *.gz``

5. Change the user and group of the extracted files to mattermost

   - ``sudo chown -R mattermost:mattermost mattermost/``

6. Create the storage directory for files. We assume you will have
   attached a large drive for storage of images and files. For this
   setup we will assume the directory is located at
   ``/mattermost/data``.

   -  Create the directory by typing:
   -  ``sudo mkdir -p /mattermost/data``
   -  Set the mattermost account as the directory owner by typing:
   -  ``sudo chown -R mattermost:mattermost /mattermost``

7. Configure Mattermost Server by editing the config.json file at
   ``/home/mattermost/config``

   -  ``cd /home/mattermost/mattermost/config``
   -  Edit the file by typing:
   -  ``vi config.json``
   -  If you are using PostgreSQL:    
     -  Set ``DriverName":`` to ``"postgres"``
     -  Set ``"DataSource:"`` to the following value: ``"postgres://mmuser:mmuser_password@10.10.10.1:5432/mattermost?sslmode=disable&connect_timeout=10"``
   -  If you are using MySQL:    
     -  Set ``DriverName":`` to ``"mysql"``
     -  Set ``"DataSource":`` to the following value: ``"mmuser:mmuser_password@tcp(10.10.10.1:3306)/mattermost?charset=utf8"``
   -  You can continue to edit configuration settings in
      ``config.json`` or use the System Console described in a later
      section to finish the configuration.

8. Test the Mattermost Server

   -  ``cd ~/mattermost/bin``
   -  Run the Mattermost Server by typing:
   -  ``./platform``
   -  You should see a console log like ``Server is listening on :8065``
      letting you know the service is running.
   -  Stop the server for now by typing ``ctrl-c``

9. Setup Mattermost to use the Upstart daemon which handles supervision
   of the Mattermost process.

   -  ``sudo touch /etc/init/mattermost.conf``
   -  ``sudo vi /etc/init/mattermost.conf``
   -  Copy the following lines into ``/etc/init/mattermost.conf``

      ::

          start on runlevel [2345]
          stop on runlevel [016]
          respawn
          limit nofile 50000 50000
          chdir /home/mattermost/mattermost
          setuid mattermost
          exec bin/platform

   -  You can manage the process by typing:
   -  ``sudo start mattermost``
   -  Verify the service is running by typing:
   -  ``curl http://10.10.10.2:8065``
   -  You should see a page titles *Mattermost - Signup*
   -  You can also stop the process by running the command
      ``sudo stop mattermost``, but we will skip this step for now.
