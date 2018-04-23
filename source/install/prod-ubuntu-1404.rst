..  _prod-ubuntu-1404:

Production Install on Ubuntu 14.04 LTS
======================================

Install Mattermost in production mode on one, two or three machines, using the following steps:

- `Install Ubuntu Server (x64) 14.04 LTS`_
- `Set up Database Server`_
- `Set up Mattermost Server`_
- `Set up NGINX Server`_


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

Install and set up either PostgreSQL 9.3 or MySQL 5.6.

Set up PostreSQL
~~~~~~~~~~~~~~~~

1.  For the purposes of this guide we will assume this server has an IP
    address of 10.10.10.1
2.  Install PostgreSQL 9.3+

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
    -  Uncomment ``listen_addresses`` and change ``localhost`` to ``*``

11. Alter pg\_hba.conf to allow the mattermost server to talk to the
    postgres database

    -  ``sudo vi /etc/postgresql/9.3/main/pg_hba.conf``
    -  Add the following line to the ``IPv4 local connections``
    -  ``host all all 10.10.10.2/32 md5``

12. Reload Postgres database

    -  ``sudo /etc/init.d/postgresql reload``

    check with netstat command to see postgresql actually running on given ip and port

    - ``sudo netstat -anp | grep 5432``

    try restarting the postgresql service if reload won't work

    - ``sudo service postgresql restart``

13. Attempt to connect with the new created user to verify everything
    looks good

    -  ``psql --host=10.10.10.1 --dbname=mattermost --username=mmuser --password``
    -  ``mattermost=> \q``

Set up MySQL Database Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Install MySQL 5.6.

    - ``sudo apt-get install mysql-server-5.6``

2. Log in to MySQL as root.

    - ``mysql -u root -p``

    When prompted, enter the root password that you created when installing MySQL.

3. Create the Mattermost user, 'mmuser'.

    - ``mysql> create user 'mmuser'@'%' identified by 'mmuser-password';``

    **Notes**:

    1. Use a password that is more secure than 'mmuser-password'
    2. The '%' means that mmuser can connect from any machine on the network.   However, it's more secure to use the IP address of the machine that hosts Mattermost. For example, if you install Mattermost on the machine with IP address 10.10.10.2, then use the following command:

    - ``mysql> create user 'mmuser'@'10.10.10.2' identified by 'mmuser-password';``

4. Create the Mattermost database.

    - ``mysql> create database mattermost;``

5. Grant access privileges to the user 'mmuser'

    - ``mysql> grant all privileges on mattermost.* to 'mmuser'@'%';``

Set up Mattermost Server
------------------------

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
   -  Below is a sample nginx configuration optimized for performance:

    ::
    
        upstream backend {
            server 10.10.10.2:8065;
        }

        proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=mattermost_cache:10m max_size=3g inactive=120m use_temp_path=off;

        server {
            listen 80;
            server_name    mattermost.example.com;

            location /api/v3/users/websocket {
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
                client_max_body_size 50M;
                proxy_set_header Host $http_host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
                proxy_set_header X-Frame-Options SAMEORIGIN;
                proxy_buffers 256 16k;
                proxy_buffer_size 16k;
                proxy_read_timeout 600s;
                proxy_pass http://backend;
            }

            location / {
                client_max_body_size 50M;
                proxy_set_header Connection "";
                proxy_set_header Host $http_host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
                proxy_set_header X-Frame-Options SAMEORIGIN;
                proxy_buffers 256 16k;
                proxy_buffer_size 16k;
                proxy_read_timeout 600s;
                proxy_cache mattermost_cache;
                proxy_cache_revalidate on;
                proxy_cache_min_uses 2;
                proxy_cache_use_stale timeout;
                proxy_cache_lock on;
                proxy_pass http://backend;
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

    upstream backend {
        server 10.10.10.2:8065;
    }

    server {
       listen         80;
       server_name    mattermost.example.com;
       return         301 https://$server_name$request_uri;
    }

    proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=mattermost_cache:10m max_size=3g inactive=120m use_temp_path=off;

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

       location /api/v3/users/websocket {
          proxy_set_header Upgrade $http_upgrade;
          proxy_set_header Connection "upgrade";
          proxy_set_header X-Forwarded-Ssl on;
          client_max_body_size 50M;
          proxy_set_header Host $http_host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header X-Forwarded-Proto $scheme;
          proxy_set_header X-Frame-Options SAMEORIGIN;
          proxy_buffers 256 16k;
          proxy_buffer_size 16k;
          proxy_read_timeout 600s;
          proxy_pass http://backend;
       }

       location / {
          proxy_set_header X-Forwarded-Ssl on;
          client_max_body_size 50M;
          proxy_set_header Connection "";
          proxy_set_header Host $http_host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header X-Forwarded-Proto $scheme;
          proxy_set_header X-Frame-Options SAMEORIGIN;
          proxy_buffers 256 16k;
          proxy_buffer_size 16k;
          proxy_read_timeout 600s;
          proxy_cache mattermost_cache;
          proxy_cache_revalidate on;
          proxy_cache_min_uses 2;
          proxy_cache_use_stale timeout;
          proxy_cache_lock on;
          proxy_pass http://backend;
        }
    }


6. Be sure to restart NGINX
  * ``\ sudo service nginx start``
7. Add the following line to cron so the cert will renew every month
  * ``crontab -e``
  * ``@monthly /home/ubuntu/letsencrypt/letsencrypt-auto certonly --reinstall --nginx -d yourdomainname && sudo service nginx reload``
8. Check that your SSL certificate is set up correctly
  * Test the SSL certificate by visiting a site such as `https://www.ssllabs.com/ssltest/index.html <https://www.ssllabs.com/ssltest/index.html>`_
  * If there’s an error about the missing chain or certificate path, there is likely an intermediate certificate missing that needs to be included

Setup HTTP2
------------

It is recommended to enable HTTP2 for enhanced performance. 

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

7. Feel free to modify other settings.
8. Restart the Mattermost Service by typing:

   -  ``sudo restart mattermost``
