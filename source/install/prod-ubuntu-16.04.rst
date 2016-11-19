..  _prod-ubuntu-1604:

Production Install on Ubuntu 16.04 LTS
======================================

Install Mattermost in production mode on one, two or three machines, using the following steps:

- `Install Ubuntu Server (x64) 16.04 LTS`_
- `Set up Database Server`_
- `Set up Mattermost Server`_
- `Set up NGINX Server`_
- `Post-Installation Mattermost Configuration`_


Install Ubuntu Server (x64) 16.04 LTS
-------------------------------------

1. Set up 3 machines with Ubuntu 16.04 with 2GB of RAM or more. The
   servers will be used for the Proxy, Mattermost (must be
   x64), and Database.

   -  **Optional:** You can also use a **1 machine setup** (Proxy, Mattermost and Database on one machine) or a **2 machine setup** (Proxy and Mattermost on one machine, Database on another) depending on your data center standards.

2. Make sure the system is up to date with the most recent security
   patches.

   ::

       sudo apt update
       sudo apt upgrade


Set up Database Server
----------------------

1.  For the purposes of this guide we will assume this server has an IP
    address of ``10.10.10.1``.
2.  Install PostgreSQL 9.5+::

        sudo apt-get install postgresql postgresql-contrib

3.  PostgreSQL created a user account called ``postgres``. You will need
    to log into that account with::

        sudo -i -u postgres

4.  You can get a PostgreSQL prompt by typing::

        psql

5.  Create the Mattermost database by typing::

        postgres=# CREATE DATABASE mattermost;

6.  Create the Mattermost user by typing::

        postgres=# CREATE USER mmuser WITH PASSWORD 'mmuser_password';

7.  Grant the user access to the Mattermost database by typing::

        postgres=# GRANT ALL PRIVILEGES ON DATABASE mattermost to mmuser;

8.  You can exit out of PostgreSQL by typing::

        postgres=# \q

9.  You can exit the postgres account by typing::

        exit

10. Allow Postgres to listen on all assigned IP Addresses

    -  Edit the config file::

           sudo vi /etc/postgresql/9.5/main/postgresql.conf

    -  Uncomment ``listen_addresses`` and change ``localhost`` to ``*``

11. Alter ``pg_hba.conf`` to allow the mattermost server to talk to the
    postgres database

    -  Edit the config file::

        sudo vi /etc/postgresql/9.5/main/pg_hba.conf

    -  Add the following line to the ``IPv4 local connections``::

        host all all 10.10.10.2/32 md5

12. Reload Postgres database::

        sudo systemctl reload postgresql.service

    Check with ``netstat`` command to see postgresql actually running on given ip and port::

        sudo netstat -anp | grep 5432

    Try restarting the postgresql service if reload won't work::

        sudo systemctl restart postgresql.service

13. Attempt to connect with the new created user to verify everything
    looks good::

        psql --host=10.10.10.1 --dbname=mattermost --username=mmuser --password
        mattermost=> \q


Set up Mattermost Server
------------------------

For the purposes of this guide we will assume this server has an IP address of ``10.10.10.2``

1. Create a user and group for running mattermost::

       sudo useradd --create-home --user-group --system mattermost

2. Change to the account of the new user::

       sudo --user=mattermost --shell

3. Change into the home of the new user::

       cd

4. Download `any version of the Mattermost Server <https://docs.mattermost.com/administration/upgrade.html#version-archive>`_ by typing::

       wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz

   Where ``X.X.X`` is typically the latest Mattermost release version.

5. Unzip the Mattermost Server by typing::

       tar -xvzf mattermost-X.X.X-linux-amd64.tar.gz

6. Configure Mattermost Server by editing the config.json file at
   ``/home/mattermost/mattermost/config``:

   -  Change to the directory::

       cd ~/mattermost/config

   -  Edit the file by typing::

       vi config.json

   -  replace ``DriverName": "mysql"`` with ``DriverName": "postgres"``
   -  replace
      ``"DataSource": "mmuser:mostest@tcp(dockerhost:3306)/mattermost_test?charset=utf8mb4,utf8"``
      with
      ``"DataSource": "postgres://mmuser:mmuser_password@10.10.10.1:5432/mattermost?sslmode=disable&connect_timeout=10"``
   -  Optionally you may continue to edit configuration settings in
      ``config.json`` or use the System Console described in a later
      section to finish the configuration.

7. Test the Mattermost Server

   -  Change to the folder with the executable::

       cd ~/mattermost/bin

   -  Run the Mattermost Server by typing::

       ./platform

   -  You should see a console log like ``Server is listening on :8065``
      letting you know the service is running.
   -  Stop the server for now by typing ``ctrl-c``

8. Exit the *mattermost* account::

       exit

9. Create a systemd unit-file for service management.

   - Create the unit-file::

       sudo vi /lib/systemd/system/mattermost.service

   - Fill it with the following content::

         [Unit]
         Description=Mattermost
         After=network.target
         After=postgresql.service
         Requires=postgresql.service

         [Service]
         Type=simple
         ExecStart=/home/mattermost/mattermost/bin/platform
         Restart=always
         RestartSec=10
         WorkingDirectory=/home/mattermost/mattermost
         User=mattermost
         Group=mattermost

         [Install]
         WantedBy=multi-user.target

   - Make systemd load the new unit::

       sudo systemctl daemon-reload

   - Check if the unit was loaded::

       sudo systemctl status mattermost.service

     It should give you an output similar to the following::

       ● mattermost.service - Mattermost
         Loaded: loaded (/lib/systemd/system/mattermost.service; disabled; vendor pres
         Active: inactive (dead)

   - Start the service to check if it works::

       sudo systemctl start mattermost.service

   -  Verify the service is running by typing::

          curl http://10.10.10.2:8065

      You should see a page titled ``Mattermost``.

   - Enable the unit to be started during server boot::

       sudo systemctl enable mattermost.service

   - Stopping the service if possible but we skip this now.
     If for some reason you want to stop mattermost the following command will do it::

        sudo systemctl stop mattermost.service

10. Create the storage directory for files. We assume you will have
   attached a large drive for storage of images and files. For this
   setup we will assume the directory is located at
   ``/mattermost/data``.

   -  Create the directory by typing::

       sudo mkdir -p /mattermost/data

   -  Set the *mattermost* account as the directory owner by typing::

       sudo chown -R mattermost /mattermost


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


3. Install NGINX on Ubuntu with::

       sudo apt install nginx

4. Verify NGINX is running::

       curl http://10.10.10.3

   You should see a *Welcome to NGINX!* page

5. You can manage NGINX with the following commands

   - Stop::

       sudo systemctl stop nginx.service

   - Start::

       sudo systemctl start nginx.service

   - Restart::

       sudo systemctl restart nginx.service

6. Map a FQDN (fully qualified domain name) like
   ``mattermost.example.com`` to point to the NGINX server.
7. Configure NGINX to proxy connections from the internet to the
   Mattermost Server

   -  Create a configuration for Mattermost::

        sudo touch /etc/nginx/sites-available/mattermost

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


   * Remove the existing file with::

        sudo rm /etc/nginx/sites-enabled/default

   * Link the mattermost config by typing::

        sudo ln -s /etc/nginx/sites-available/mattermost /etc/nginx/sites-enabled/mattermost

   * Restart NGINX by typing::

        sudo service nginx restart

   * Verify you can see Mattermost thru the proxy by typing::

        curl http://localhost

   * You should see a page titled *Mattermost*


Set up NGINX with SSL (Recommended)
-----------------------------------

You can use a free and an open certificate security like let's encrypt.

1. Install git::

       sudo apt install git

2. Be sure that the port 80 is not use by stopping NGINX::

       sudo systemctl stop nginx.service
       netstat -na | grep ':80.*LISTEN'

3. Clone the letsencrypt repository, download packages and run the instance. After that you will have to give your domain name::

       sudo --user=mattermost --shell
       git clone https://github.com/letsencrypt/letsencrypt
       cd letsencrypt
       ./letsencrypt-auto certonly --standalone
       exit

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


6. Be sure to restart NGINX::

      sudo service nginx start

7. Edit the cron configuration so the cert will renew every month::

       crontab -e

  Insert this line::

      @monthly /home/mattermost/letsencrypt/letsencrypt-auto certonly --reinstall -d yourdomainname && sudo service nginx reload

8. Check that your SSL certificate is set up correctly
  * Test the SSL certificate by visiting a site such as `https://www.ssllabs.com/ssltest/index.html <https://www.ssllabs.com/ssltest/index.html>`_.
  * If there’s an error about the missing chain or certificate path, there is likely an intermediate certificate missing that needs to be included.

Post-Installation Mattermost Configuration
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
8. Restart the Mattermost Service by typing::

       sudo systemctl restart mattermost.service
