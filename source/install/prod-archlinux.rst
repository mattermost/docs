..  _prod-archlinux:

Production Install on Archlinux
======================================

Install Mattermost in production mode on one, two or three machines.

.. contents::
    :backlinks: top


Set up Database Server
----------------------

**NOTE**: When Mattermost and postgresql are on the same machine,
it is recommended to use unix socket mechanism for the connection between Mattermost and Postgresql,
as it is more secure and faster.
Below instructions are for a connection via the TCP/IP socket.

Settings specific to the unix socket connection are detailed in the *Unix-domain socket connection*
section.


For the purposes of this guide we will assume this server has an IP address of ``10.10.10.1``.

*Optional*: if installing on the same machine substitute ``10.10.10.1`` with ``127.0.0.1``

1.  Install PostgreSQL 9.5+::

        # pacman -Syu postgresql postgresql-libs

    **NOTE**: main configuration files are ``postgresql.conf, ph_hba.conf,
    pg_ident.conf``. After installation, you will find a sample of these files
    in the ``/usr/share/postgresql`` directory. Please copy these files in the
    ``var/lib/postgres/data`` default directory, remove the ``.sample`` at the
    end of the file name and edit them according to your needs.

    For more details, please refer to the `PostgreSQL Arch wiki <https://wiki.archlinux.org/index.php/PostgreSQL>`_.


2.  Start and enable the systemd service::

        # systemctl start postgresql.service
        # systemctl enable postgresql.service

3.  During instalation, PostgreSQL created a user account called ``postgres``.
    Log into that account::

        $ sudo -i -u postgres

4.  Initialize the database cluster. This has to be done once::

        [postgres]$ initdb --locale $LANG -E UTF8 -D '/var/lib/postgres/data'

5.  Connect to the postgreSQL server as user postgres::

        [postgres]$ psql

6.  Create the Mattermost database::

        postgres=# CREATE DATABASE mattermost;

7.  Create the Mattermost user::

        postgres=# CREATE USER mmuser WITH PASSWORD 'mmuser_password';


8.  Grant the user access to the Mattermost database::

        postgres=# GRANT ALL PRIVILEGES ON DATABASE mattermost to mmuser;

9.  Exit out of PostgreSQL::

        postgres=# \q

10.  Exit the postgres user::

        [postgres]$ exit

11. Allow Postgres to listen on all assigned IP Addresses

    Edit the config file ``/var/lib/postgres/data/postgresql.conf``.
    In the connections and authentications section, uncomment the ``listen_addresses``
    line and edit to your needs::

        listen_addresses = 'localhost,my_local_ip_address'
        #You can use '*' to listen on all local addresses

12. Allow the mattermost server to talk to the postgres database

    Edit the config file ``/var/lib/postgres/data/pg_hba.conf``.
    Add the following line to the ``IPv4 local connections``::

        host all all 10.10.10.2/32 md5

13. Reload Postgres database::

        # systemctl restart postgresql.service

    Check with ``netstat`` command to see postgresql actually running on given ip and port::

        # netstat -anp | grep 5432

14. Attempt to connect with the new created user to verify everything
    looks good::

        $ psql --host=10.10.10.1 --dbname=mattermost --username=mmuser --password
        mattermost=> \q


Set up Mattermost Server with Arch User Repository (unofficial)
---------------------------------------------------------------

Archlinux uses a specific feature called `Arch User Repository <https://wiki.archlinux.org/index.php/Arch_User_Repository>`_.
to manage extra packages which do not belong to the official repository. It allows
you to compile a package from source and then install it via the Arch package manager
`pacman <https://wiki.archlinux.org/index.php/Pacman#Additional_commands>`_. This way
you will be able to easily track upgrades or dependency issues. This is the recommended
way to install extra packages.

There is an AUR unofficial package called `mattermost <https://aur.archlinux.org/packages/mattermost>`_ .
Follow the `AUR instructions <https://wiki.archlinux.org/index.php/Arch_User_Repository>`_
to build and install. Please go to the `AUR package page <https://aur.archlinux.org/packages/mattermost/>`_
to leave a comment for sharing feedback or troubleshooting.

Once the package has been built and install, follow this procedure.

For the purposes of this guide we will assume this server has an IP address of ``10.10.10.2``

1. Configure Mattermost Server by editing the config.json file at
   ``/etc/webapps/mattermost/config.json``:

-  replace ``DriverName": "mysql"`` with ``DriverName": "postgres"``

-  replace ``"DataSource": "mmuser:mostest@tcp(dockerhost:3306)/mattermost_test?charset=utf8mb4,utf8"`` with
   ``"DataSource": "postgres://mmuser:mmuser_password@10.10.10.1:5432/mattermost?sslmode=disable&connect_timeout=10"``


2. Start and enable mattermost service::

        # systemctl start mattermost.service
        # systemctl enable mattermost.service


3. Verify the service is running by typing::

          curl http://10.10.10.2:8065

You should see a page titled ``Mattermost``.

**NOTE**:

- user and group mattermost have been created during installation
- the mattermost directory is located at ``/var/lib/mattermost`` and is owned by
``mattermost:root``


Unix-domain socket connection
-----------------------------

Below are the instructions specific to a connection between Postgresql and Mattermost via an Unix-domain socket.
**Only changes from the original setup described above will be mentioned**.

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
    mattermost_db=>

**Set up Mattermost server**

- Step 6: Edit ``/opt/mattermost/config/config.json``

  * Replace ``DriverName": "mysql"`` with ``DriverName": "postgres"``
  * Replace  ``"DataSource": "mmuser:mostest@tcp(dockerhost:3306)/mattermost_test?charset=utf8mb4,utf8"`` with ``"DataSource": "postgres:///mattermost_db?host=/var/run/postgresql"``


Set up NGINX Server
-------------------

We use NGINX for proxying request to the Mattermost Server. The main
benefits are:

-  SSL termination
-  http to https redirect
-  Port mapping 80 to 8065
-  Standard request logs

1- Install the `nginx package <https://www.archlinux.org/packages/?name=nginx-mainline>`_
from the extra repository. Please visit `Nginx Arch wiki <https://wiki.archlinux.org/index.php/Nginx>`_
for more explanations about settings.

2- Enable and start the server::

    # systemctl enable nginx
    # systemctl start nginx

The default served page at ``http://127.0.0.1`` is located at ``/usr/share/nginx/html/index.html``.
The command ::

    $ curl http://127.0.0.1

should return a *Welcome to NGINX!* page

3- Map a FQDN (fully qualified domain name) like ``mattermost.example.com``

to point to the NGINX server.

4- Configure NGINX to proxy connections from the internet to the Mattermost Server.

-  Create and edit a configuration file ``/etc/nginx/servers-available/mattermost`` for Mattermost.

Below is a sample nginx configuration optimized for performance::

        upstream backend {
            server 127.0.0.1:8065;
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


- Enable the mattermost server::

        # mkdir /etc/nginx/servers-enabled
        # ln -s /etc/nginx/servers-available/mattermost /etc/nginx/server-enabled/mattermost

- Restart NGINX::

        # systemctl restart ngnix.service

- Verify you can see Mattermost thru the proxy by typing::

        curl http://localhost

You should see a page titled *Mattermost*


Set up NGINX with SSL (Recommended)
-----------------------------------

There is now a free and an open certificate security called `let's encrypt <https://letsencrypt.org/>`_.
As stated on the Let's Encrypt website, it is largely recommended to use the `Certbot <https://certbot.eff.org/>`_
ACME client. Follow instructions for `Nginx on Arch Linux client <https://certbot.eff.org/#arch-nginx>`_.


1.  Install the Certbot client::

      # pacman -Syu certbot

2.  Obtain a cert using the `webroot plugin <https://certbot.eff.org/docs/using.html#webroot>`_::

      # certbot certonly --webroot -w /var/www/example -d example.com -d www.example.com

The above command will obtain a single cert for **example.com** and **www.example.com**, assuming
the root of these servers is located at ``/var/www/example``. Certbot will try to place a file in
directory ``/var/www/example/.well-known/acme-challenge`` and then read it.

3.  Modify the file at ``/etc/nginx/sites-available/mattermost`` this way::


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


4.  Restart Nginx::

      # systemctl restart nginx.service


5.  Set up Letsencrypt cert automatic renewal with systemd timer

- Run the following command to check your setup is correct::

      # certbot renew --dry-run

- write the ``/etc/systemd/system/letsencrypt.renewal.service`` file::

     [Unit]
     Description=Renew let's encrypt certificates

     [Service]
     ExecStart=/usr/bin/certbot renew --quiet

- write the ``/etc/systemd/system/letsencrypt.renewal.timer`` file::

     [Unit]
     Description=start letsencrypt.renewal.service every 12 hours

     [Timer]
     OnUnitActiveSec=12hours

     [Install]
     WantedBy=timers.target

- Start and enable these two systemd files.


8. Check that your SSL certificate is set up correctly

* Test the SSL certificate by visiting a site such as `ssllabs <https://www.ssllabs.com/ssltest/index.html>`_.

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
