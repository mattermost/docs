..  _prod-ubuntu:

Production Enterprise Install on Ubuntu 14.04 LTS
=================================================

Install Mattermost Enterprise Edition in production mode on one, two or three machines.
 
.. contents::
  :backlinks: top

Install Ubuntu Server (x64) 14.04 LTS
-------------------------------------

1. Set up 3 machines with Ubuntu 14.04 with 2GB of RAM or more. The
   servers will be used for the Proxy, Mattermost (must be
   x64), and Database.

   -  **Optional:** You can also use a **1 machine setup** (Proxy, Mattermost and Database on one machine) or a **2 machine setup** (Proxy and Mattermost on one machine, Database on another) depending on your data center standards. 

2. Make sure the system is up to date with the most recent security
   patches.

   -  ``sudo apt-get update``
   -  ``sudo apt-get upgrade``

Set up Database Server
----------------------

1.  For the purposes of this guide we will assume this server has an IP
    address of 10.10.10.1
2.  Install PostgreSQL 9.3+ (or MySQL 5.6+)

    -  ``sudo apt-get install postgresql postgresql-contrib``

3.  PostgreSQL created a user account called ``postgres``. You will need
    to log into that account with:

    -  ``sudo -i -u postgres``

4.  You can get a PostgreSQL prompt by typing:

    -  ``psql``

5.  Create the Mattermost database by typing:

    -  ``postgres=# CREATE DATABASE mattermost;``

6.  Create the Mattermost user by typing:

    -  ``postgres=# CREATE USER mmuser WITH PASSWORD 'mmuser_password';``

7.  Grant the user access to the Mattermost database by typing:

    -  ``postgres=# GRANT ALL PRIVILEGES ON DATABASE mattermost to mmuser;``

8.  You can exit out of PostgreSQL by typing:

    -  ``postgre=# \q``

9.  You can exit the postgres account by typing:

    -  ``exit``

10. Allow Postgres to listen on all assigned IP Addresses

    -  ``sudo vi /etc/postgresql/9.3/main/postgresql.conf``
    -  Uncomment ``listen_addresses`` and change ``localhost`` to ``\*``

11. Alter pg\_hba.conf to allow the mattermost server to talk to the
    postgres database

    -  ``sudo vi /etc/postgresql/9.3/main/pg_hba.conf``
    -  Add the following line to the ``IPv4 local connections``
    -  ``host all all 10.10.10.2/32 md5``

12. Reload Postgres database

    -  ``sudo /etc/init.d/postgresql reload``

13. Attempt to connect with the new created user to verify everything
    looks good

    -  ``psql --host=10.10.10.1 --dbname=mattermost --username=mmuser --password``
    -  ``mattermost=> \q``

Set up Mattermost Server
------------------------

1. For the purposes of this guide we will assume this server has an IP
   address of ``10.10.10.2``
2. For the sake of making this guide simple we located the files at
   ``/home/ubuntu/mattermost``. In the future we will give guidance for
   storing under ``/opt``.
3. We have also elected to run the Mattermost Server as the ``ubuntu``
   account for simplicity. We recommend setting up and running the
   service under a ``mattermost`` user account with limited permissions.
4. Download `any version of Mattermost Enterprise Edition <https://docs.mattermost.com/administration/upgrade.html#version-archive>`_ by typing:

   -  ``wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz``
   -  Where ``vX.X.X`` is typically the latest Mattermost release version, which is currently ``v3.3.0``. 
   
5. Unzip the Mattermost Server by typing:

   -  ``tar -xvzf mattermost-X.X.X-linux-amd64.tar.gz``

6. Create the storage directory for files. We assume you will have
   attached a large drive for storage of images and files. For this
   setup we will assume the directory is located at
   ``/mattermost/data``.

   -  Create the directory by typing:
   -  ``sudo mkdir -p /mattermost/data``
   -  Set the ubuntu account as the directory owner by typing:
   -  ``sudo chown -R ubuntu /mattermost``

7. Configure Mattermost Server by editing the config.json file at
   ``/home/ubuntu/mattermost/config``

   -  ``cd ~/mattermost/config``
   -  Edit the file by typing:
   -  ``vi config.json``
   -  replace ``DriverName": "mysql"`` with ``DriverName": "postgres"``
   -  replace
      ``"DataSource": "mmuser:mostest@tcp(dockerhost:3306)/mattermost_test?charset=utf8mb4,utf8"``
      with
      ``"DataSource": "postgres://mmuser:mmuser_password@10.10.10.1:5432/mattermost?sslmode=disable&connect_timeout=10"``
   -  Optionally you may continue to edit configuration settings in
      ``config.json`` or use the System Console described in a later
      section to finish the configuration.

8. Test the Mattermost Server

   -  ``cd ~/mattermost/bin``
   -  Run the Mattermost Server by typing:
   -  ``./platform``
   -  You should see a console log like ``Server is listening on :8065``
      letting you know the service is running.
   -  Stop the server for now by pressing CTRL+C

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
          chdir /home/ubuntu/mattermost
          setuid ubuntu
          exec bin/platform

   -  You can manage the process by typing:
   -  ``sudo start mattermost``
   -  Verify the service is running by typing:
   -  ``curl http://10.10.10.2:8065``
   -  You should see a page titles *Mattermost - Signup*
   -  You can also stop the process by running the command
      ``sudo stop mattermost``, but we will skip this step for now.

Set up NGINX Server
-------------------

1. For the purposes of this guide we will assume this server has an IP
   address of ``10.10.10.3``
2. We use NGINX for proxying request to the Mattermost Server. The main
   benefits are:

   -  SSL termination
   -  http to https redirect
   -  Port mapping ``:80`` to ``:8065``
   -  Standard request logs


3. Install NGINX on Ubuntu with

   -  ``sudo apt-get install nginx``

4. Verify NGINX is running

   -  ``curl http://10.10.10.3``
   -  You should see a *Welcome to NGINX!* page

5. You can manage NGINX with the following commands

   -  ``sudo service nginx stop``
   -  ``sudo service nginx start``
   -  ``sudo service nginx restart``

6. Map a FQDN (fully qualified domain name) like
   ``mattermost.example.com`` to point to the NGINX server.
7. Configure NGINX to proxy connections from the internet to the
   Mattermost Server

   -  Create a configuration for Mattermost
   -  ``sudo touch /etc/nginx/sites-available/mattermost``
   -  Below is a sample configuration with the minimum settings required
      to configure Mattermost

    ::

        server {
          server_name mattermost.example.com;

          location / {
             client_max_body_size 50M;
             proxy_set_header Upgrade $http_upgrade;
             proxy_set_header Connection "upgrade";
             proxy_set_header Host $http_host;
             proxy_set_header X-Real-IP $remote_addr;
             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
             proxy_set_header X-Forwarded-Proto $scheme;
             proxy_set_header X-Frame-Options SAMEORIGIN;
             proxy_pass http://10.10.10.2:8065;
          }
       }


   * Remove the existing file with
   * ``` sudo rm /etc/nginx/sites-enabled/default```
   * Link the mattermost config by typing:
   * ```sudo ln -s /etc/nginx/sites-available/mattermost /etc/nginx/sites-enabled/mattermost```
   * Restart NGINX by typing:
   * ``` sudo service nginx restart```
   * Verify you can see Mattermost thru the proxy by typing:
   * ``` curl http://localhost```
   * You should see a page titles *Mattermost - Signup*

Set up NGINX with SSL (Recommended)
-----------------------------------

1. You can use a free and an open certificate security like let's
   encrypt, this is how to proceed

-  ``sudo apt-get install git``
-  ``git clone https://github.com/letsencrypt/letsencrypt``
-  ``cd letsencrypt``

2. Be sure that the port 80 is not use by stopping NGINX

-  ``sudo service nginx stop``
-  ``netstat -na | grep ':80.*LISTEN'``
-  ``./letsencrypt-auto certonly --standalone``

3. This command will download packages and run the instance, after that
   you will have to give your domain name
4. You can find your certificate in ``/etc/letsencrypt/live``
5. Modify the file at ``/etc/nginx/sites-available/mattermost`` and add
   the following lines:

  ::

      server {
         listen         80;
         server_name    mattermost.example.com;
         return         301 https://$server_name$request_uri;
      }

      server {
         listen 443 ssl;
         server_name mattermost.example.com;

         ssl on;
         ssl_certificate /etc/letsencrypt/live/yourdomainname/fullchain.pem;
         ssl_certificate_key /etc/letsencrypt/live/yourdomainname/privkey.pem;
         ssl_session_timeout 5m;
         ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
         ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';
         ssl_prefer_server_ciphers on;
         ssl_session_cache shared:SSL:10m;

         location / {
            gzip off;
            proxy_set_header X-Forwarded-Ssl on;
            client_max_body_size 50M;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header X-Frame-Options SAMEORIGIN;
            proxy_pass http://10.10.10.2:8065;
         }
      }



6. Be sure to restart NGINX
  * ``\ sudo service nginx start``
7. Add the following line to cron so the cert will renew every month
  * ``crontab -e``
  * ``@monthly /home/ubuntu/letsencrypt/letsencrypt-auto certonly --reinstall -d yourdomainname && sudo service nginx reload``
8. Check that your SSL certificate is set up correctly
  * Test the SSL certificate by visiting a site such as `https://www.ssllabs.com/ssltest/index.html <https://www.ssllabs.com/ssltest/index.html>`_
  * If there’s an error about the missing chain or certificate path, there is likely an intermediate certificate missing that needs to be included

Setup HTTP2
------------

It is recomented to enable HTTP2 for enhanced performance. 

1. Modify your NGINX configuration as above. Then,

  - Change the line ``listen 443 ssl;`` to ``listen 443 ssl http2;``
  - Change the line ``proxy_pass http://10.10.10.2:8065;`` to ``proxy_pass https://10.10.10.2:8065;``
  
2. Restart NGINX

3. Setup TLS on the Mattermost server by following `these instrucions. <https://docs.mattermost.com/install/setup-tls.html>`_

Test setup and configure Mattermost Server
------------------------------------------

1. Navigate to ``https://mattermost.example.com`` and create a team and
   user.
2. The first user in the system is automatically granted the
   ``system_admin`` role, which gives you access to the System Console.
3. From the ``town-square`` channel click the dropdown and choose the
   ``System Console`` option
4.  Update **Notification** > **Email** settings to setup an SMTP email service. The example below assumes AmazonSES.

   -  Set *Send Email Notifications* to ``true``
   -  Set *Require Email Verification* to ``true``
   -  Set *Feedback Name* to ``No-Reply``
   -  Set *Feedback Email* to ``mattermost@example.com``
   -  Set *SMTP Username* to ``[YOUR_SMTP_USERNAME]``
   -  Set *SMTP Password* to ``[YOUR_SMTP_PASSWORD]``
   -  Set *SMTP Server* to ``email-smtp.us-east-1.amazonaws.com``
   -  Set *SMTP Port* to ``465``
   -  Set *Connection Security* to ``TLS``
   -  Save the Settings

5. Update **File** > **Storage** settings:

   -  Change *Local Directory Location* from ``./data/`` to
      ``/mattermost/data``

6. Update **General** > **Logging** settings:

   -  Set *Log to The Console* to ``false``

7. Update **Advanced** > **Rate Limiting** settings:

   -  Set *Vary By Remote Address* to ``false``
   -  Set *Vary By HTTP Header* to ``X-Real-IP``

8. Feel free to modify other settings.
9. Restart the Mattermost Service by typing:

   -  ``sudo restart mattermost``
