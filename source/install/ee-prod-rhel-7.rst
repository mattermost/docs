..  _prod-rhel-7:

Production Enterprise Install on RHEL 7.1+
==========================================

Install Mattermost Enterprise Edition in production mode on one, two or three machines.
 
.. contents::
  :backlinks: top

Install Red Hat Enterprise Linux (x64) 7.1+
-------------------------------------------

1. Set up 3 machines with RHEL with 2GB of RAM or more. The servers will
   be used for the Proxy, Mattermost (this must be x64 to use
   pre-built binaries), and Database.

   -  **Optional:** You can also use a **1 machine setup** (Proxy, Mattermost and Database on one machine) or a **2 machine setup** (Proxy and Mattermost on one machine, Database on another) depending on your data center standards.

2. Make sure the system is up to date with the most recent security
   patches.

   -  ``sudo dnf upgrade``

Set up Database Server
----------------------

**NOTE**: When Mattermost and postgresql are on the same machine,
it is recommended to use unix socket mechanism for the connection between Mattermost and Postgresql,
as it is more secure and faster.
Below instructions are for a connection via the TCP/IP socket.

Settings specific to the unix socket connection are detailed in the *Unix-domain socket connection*
section.

1.  For the purposes of this guide we will assume this server has an IP
    address of ``10.10.10.1``

    -  **Optional:** if installing on the same machine substitute ``10.10.10.1`` with ``127.0.0.1``

2.  Install PostgreSQL 9.4+ (or MySQL 5.6+)

    -  ``sudo dnf install http://yum.postgresql.org/9.4/redhat/rhel-6-x86_64/pgdg-redhat94-9.4-1.noarch.rpm``
    -  ``sudo dnf install postgresql94-server postgresql94-contrib``
    -  ``sudo /usr/pgsql-9.4/bin/postgresql94-setup initdb``
    -  ``sudo systemctl enable postgresql.service``
    -  ``sudo systemctl start postgresql.service``

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

    -  ``postgres=# \q``

9.  You can exit the Postgres account by typing:

    -  ``exit``

10. Alter ``/var/lib/pgsql/9.4/data/postgresql.conf`` to allow Postgres to listen
on all assigned IP Addresses:

    -  Uncomment ``listen_addresses`` and change ``localhost`` to ``\*``

11. Alter ``/var/lib/pgsql/9.4/data/pg_hba.conf`` to allow the Mattermost Server to talk to the
    Postgres database:

    -  Add the following line to the ``IPv4 local connections``:
    -  ``host all all 10.10.10.2/32 md5``

12. Reload Postgres database:

    -  ``sudo systemctl reload postgresql.service``

13. Attempt to connect with the new created user to verify everything
    looks good:

    -  ``psql --host=10.10.10.1 --dbname=mattermost --username=mmuser --password``
    -  ``mattermost=> \q``

Set up Mattermost Server
------------------------

1. For the purposes of this guide we will assume this server has an IP
   address of ``10.10.10.2``

   -  **Optional:** if installing on the same machine substitute ``10.10.10.2`` with ``127.0.0.1``

2. Download `any version of Mattermost Enterprise Edition <https://docs.mattermost.com/administration/upgrade.html#version-archive>`_ by typing:

   -  ``wget https://releases.mattermost.com/X.X.X/mattermost-X.X.X-linux-amd64.tar.gz``
   -  Where ``vX.X.X`` is typically the latest Mattermost release version, which is currently ``v3.3.0``.

3. Install Mattermost under ``/opt``

   -  Unzip the Mattermost Server by typing:
   -  ``tar -xvzf mattermost-X.X.X-linux-amd64.tar.gz``
   -  ``sudo mv mattermost /opt``

4. Create the storage directory for files. We assume you will have
   attached a large drive for storage of images and files. For this
   setup we will assume the directory is located at
   ``/opt/mattermost/data``.

   -  Create the directory by typing:
   -  ``sudo mkdir -p /opt/mattermost/data``

5. Create a system user and group called mattermost that will run this
   service:

   -  ``sudo useradd -r mattermost -U``
   -  Set the Mattermost account as the directory owner by typing:
   -  ``sudo chown -R mattermost:mattermost /opt/mattermost``
   -  ``sudo chmod -R g+w /opt/mattermost``
   -  Add yourself to the mattermost group to ensure you can edit these
      files:
   -  ``sudo usermod -aG mattermost USERNAME``

6. Configure Mattermost Server by editing the ``config.json`` file at
   ``/opt/mattermost/config``

   -  ``cd /opt/mattermost/config``
   -  Edit the file by typing:
   -  ``sudo vi config.json``
   -  replace ``DriverName": "mysql"`` with ``DriverName": "postgres"``
   -  replace
      ``"DataSource": "mmuser:mostest@tcp(dockerhost:3306)/mattermost_test?charset=utf8mb4,utf8"``
      with
      ``"DataSource": "postgres://mmuser:mmuser_password@10.10.10.1:5432/mattermost?sslmode=disable&connect_timeout=10"``
   -  Optionally you may continue to edit configuration settings in
      ``config.json`` or use the System Console described in a later
      section to finish the configuration.

7. Test the Mattermost Server

   -  ``cd /opt/mattermost/bin``
   -  Run the Mattermost Server by typing:
   -  ``./platform``
   -  You should see a console log like ``Server is listening on :8065``
      letting you know the service is running.
   -  Stop the server for now by pressing CTRL+C

8. Set up Mattermost to use the systemd init daemon which handles
   supervision of the Mattermost process. 

   * Create and edit ``/etc/systemd/system/mattermost.service``

      ::

          [Unit]
          Description=Mattermost server
          After=network.target postgresql.service

          [Service]
          User=mattermost
          Group=mattermost
          WorkingDirectory=/opt/mattermost
          ExecStart=/opt/mattermost/bin/platform
          Restart=on-failures
          PIDFile=/var/spool/mattermost/pid/master.pid
          LimitNOFILE=49152

          [Install]
          WantedBy=multi-user.target

   - Make sure the service is executable with ``sudo chmod 664 /etc/systemd/system/mattermost.service``
   * Reload the services with ``sudo systemctl daemon-reload``
   * Start Mattermost service with``\ sudo systemctl start mattermost.service``
   * ``sudo chkconfig mattermost on``
   * Start server on reboot ``sudo systemctl enable mattermost.service``

Unix-domain socket connection
-----------------------------

Below are the instructions specific to a connection between Postgresql and Mattermost via an Unix-domain socket.
Only changes from the original setup described above will be mentioned.

**Set up database server**

- Step 5: Name the database ``mattermost_db``

- Step 6: Name the user ``mattermost``

- Step 11: Add the following line instead:
  ``local   mattermost_db       mattermost          peer       map=mattermap``

- Append the following line to ``/var/lib/pgsql/9.4/data/pg_ident.conf``:

  ``mattermap      mattermost              mattermost``

  It maps unix user *mattermost* to psql user *mattermost*.

- Step 13: Verify everything looks good::

    $ su mattermost
    $ psql --dbname=mattermost_db --username=mattermost
    mattermost_db=> \q

**Set up Mattermost server**

- Step 6: Edit ``/opt/mattermost/config/config.json``

   * Replace ``DriverName": "mysql"`` with ``DriverName": "postgres"``
   * Replace  ``"DataSource": "mmuser:mostest@tcp(dockerhost:3306)/mattermost_test?charset=utf8mb4,utf8"`` with ``"DataSource": "postgres:///mattermost_db?host=/var/run/postgresql"``

Set up NGINX Server
-------------------

1. For the purposes of this guide we will assume this server has an IP
   address of ``10.10.10.3``

   -  **Optional:** if installing on the same machine substitute ``10.10.10.3`` with ``127.0.0.1``

2. We use NGINX for proxying request to the Mattermost Server. The main
   benefits are:

   -  SSL termination
   -  HTTP to HTTPS redirect
   -  Port mapping ``:80`` to ``:8065``
   -  Standard request logs

3. Install NGINX on RHEL with

   -  ``sudo vi /etc/yum.repos.d/nginx.repo``
   -  Copy the below into the file

      ::

          [nginx]
          name=nginx repo
          baseurl=http://nginx.org/packages/rhel/7/$basearch/
          gpgcheck=0
          enabled=1

   -  ``sudo dnf install nginx.x86_64``
   -  ``sudo service nginx start``
   -  ``sudo chkconfig nginx on``

4. Verify NGINX is running

   -  ``curl http://10.10.10.3``
   -  You should see a *Welcome to NGINX!* page

5. Map a FQDN (fully qualified domain name) like
   **mattermost.example.com** to point to the NGINX server.
6. Configure NGINX to proxy connections from the internet to the
   Mattermost Server

   -  Create a configuration for Mattermost
   -  ``sudo touch /etc/nginx/conf.d/mattermost.conf``
   -  Below is a sample configuration with the minimum settings required
      to configure Mattermost:

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


   - Remove the existing file with:
   - ``sudo mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.bak``
   - Restart NGINX by typing:
   - ``sudo service nginx restart``
   - Verify you can see Mattermost thru the proxy by typing:
   - ``curl http://localhost``
   - You should see a page titles *Mattermost - Signup*
   - Not seeing the page?  Look for errors with ``sudo cat /var/log/audit/audit.log | grep nginx | grep denied``
   - **Optional** if you're running on the same server as the Mattermost server and see 502 errors you may need to run ``sudo setsebool -P httpd_can_network_connect true`` because SELinux is
     preventing the connection

Set up NGINX with SSL (Recommended)
-----------------------------------

1. You can use a free and an open certificate security like `Let's
   Encrypt <https://letsencrypt.org/>`_, this is how to proceed

-  ``sudo dnf install git``
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


6. Be sure to restart nginx

   ``sudo systemctl restart nginx``

7. Check that your SSL certificate is set up correctly

Test the SSL certificate by visiting a site such as `https://www.ssllabs.com/ssltest/index.html`.

If there’s an error about the missing chain or certificate path, there is likely
an intermediate certificate missing that needs to be included.

8. Set up Letsencrypt cert automatic renewal

- Check your Letsencrypt setup is correct by running the below command. It renew
the certificate in a fake manner:

``sudo certbot renew --dry-run``

You should see a congratulation message if successful.

Then, add a cron job or use systemd timer capability to run twice a day the renewal
process.

- write the ``/etc/systemd/system/letsencrypt.renewal.service`` file

::

     [Unit]
     Description=Renew let's encrypt certificates

     [Service]
     ExecStart=/usr/bin/certbot renew --quiet

- write the ``/etc/systemd/system/letsencrypt.timer`` file

::

     [Unit]
     Description=start letsencrypt.renewal.service every 12 hours

     [Timer]
     OnUnitActiveSec=12hours

     [Install]
     WantedBy=timers.target

- Start and enable these two systemd files.

Test setup and configure Mattermost Server
-------------------------------------------

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
      ``/opt/mattermost/data``

6. Update **General** > **Logging** settings:

   -  Set *Log to The Console* to ``false``

7. Update **Advanced** > **Rate Limiting** settings:

   -  Set *Vary By Remote Address* to ``false``
   -  Set *Vary By HTTP Header* to ``X-Real-IP``

8. Feel free to modify other settings
9. Restart the Mattermost Service by typing:

   -  ``sudo restart mattermost``
