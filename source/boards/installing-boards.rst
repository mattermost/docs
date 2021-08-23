Installing the Focalboard App
-----------------------------

Focalboard is also available as a fully-contained, standalone personal desktop app for a single user that can be installed on Mac, Windows, or Linux or as a self-hosted server-based app.

Personal Desktop
~~~~~~~~~~~~~~~~

- macOS: Download Focalboard from the `App Store <https://apps.apple.com/app/apple-store/id1556908618?pt=2114704&ct=website&mt=8>`_.
- Windows: Download Focalboard from the `Microsoft App Store <https://www.microsoft.com/store/apps/9NLN2T0SX9VF?cid=website>`_.

To install Personal Desktop for Linux:

1. Download ``focalboard-linux.tar.gz`` from the latest `release on GitHub <https://github.com/mattermost/focalboard/releases>`_.
2. Unpack the ``.tar.gz`` archive.
3. Open ``focalboard-app`` from within the ``focalboard-app`` folder.

Personal Server
~~~~~~~~~~~~~~~

Focalboard Personal Server allows your team to work together on shared project boards.

Follow these steps to set it up on an Ubuntu server.

Set up Ubuntu Server 18.04
^^^^^^^^^^^^^^^^^^^^^^^^^^

Popular hosted options include:

* `Digital Ocean <https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04>`_
* `Amazon EC2 <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html>`_

Install Focalboard
^^^^^^^^^^^^^^^^^^

Download the Ubuntu archive package from the appropriate `release in GitHub <https://github.com/mattermost/focalboard/releases>`_. E.g. this is the link for v0.7.0 (which may no longer be the latest one):

.. code-block:: sh

   wget https://github.com/mattermost/focalboard/releases/download/v0.7.0/focalboard-server-linux-amd64.tar.gz
   tar -xvzf focalboard-server-linux-amd64.tar.gz
   sudo mv focalboard /opt

Install NGINX
^^^^^^^^^^^^^

By default, the Focalboard server runs on port 8000 (specified in ``config.json``). We recommend running NGINX as a web proxy to forward HTTP and websocket requests from port 80 to it. To install NGINX, run:

.. code-block:: sh

   sudo apt update
   sudo apt install nginx

You may need to adjust your firewall settings depending on the host, e.g.

* `Digital Ocean <https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-18-04>`_
* `EC2 <https://docs.nginx.com/nginx/deployment-guides/amazon-web-services/ec2-instances-for-nginx/>`_

Configure NGINX
'''''''''''''''

Create a new site config:

.. code-block:: sh

   sudo nano /etc/nginx/sites-available/focalboard

Copy and paste this configuration:

.. code-block:: sh

   upstream focalboard {
      server localhost:8000;
      keepalive 32;
   }

   server {
     listen 80 default_server;

    server_name focalboard.example.com;

     location ~ /ws/* {
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
        client_body_timeout 60;
        send_timeout 300;
        lingering_timeout 5;
        proxy_connect_timeout 1d;
        proxy_send_timeout 1d;
        proxy_read_timeout 1d;
        proxy_pass http://focalboard;
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
        proxy_cache_revalidate on;
        proxy_cache_min_uses 2;
        proxy_cache_use_stale timeout;
        proxy_cache_lock on;
        proxy_http_version 1.1;
        proxy_pass http://focalboard;
    }
 }

If there is a default site, you may need to delete it

.. code-block:: sh

   sudo rm /etc/nginx/sites-enabled/default

Enable the Focalboard site, test the config, and reload NGINX:

.. code-block:: sh

   sudo ln -s /etc/nginx/sites-available/focalboard /etc/nginx/sites-enabled/focalboard
   sudo nginx -t
   sudo /etc/init.d/nginx reload

Set up TLS on NGINX
~~~~~~~~~~~~~~~~~~~~

For a production server, it's important to set up TLS to encrypt web traffic. Without this, your login passwords and data are unprotected. Refer to the `NGINX TLS guide <https://docs.nginx.com/nginx/admin-guide/security-controls/terminating-ssl-http/>`_ and `Let's Encrypt Certbot guide <https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx>`_ on setting this up.

Install PostgreSQL (Recommended)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Focalboard stores data in a SQLite database by default, but we recommend running against PostgreSQL in production (we've tested against PostgreSQL 10.15). To install, run:

.. code-block:: sh

   sudo apt install postgresql postgresql-contrib

Then run as the *postgres* user to create a new database:

.. code-block:: sh

   sudo --login --user postgres
   psql

On the ``psql`` prompt, run the following commands (**change the user/password** to your own values):

.. code-block:: sh

   CREATE DATABASE boards;
   CREATE USER <b>boardsuser</b> WITH PASSWORD '<b>boardsuser-password</b>';
   \q

Exit the *postgres* user session:

.. code-block:: sh

   exit

Edit the Focalboard ``config.json``:

.. code-block:: sh

   nano /opt/focalboard/config.json

Change the dbconfig setting to use the postgres database you created:

.. code-block:: sh

   "dbtype": "postgres",
   "dbconfig": "postgres://boardsuser:boardsuser-password@localhost/boards?sslmode=disable&connect_timeout=10",

Install MySQL
~~~~~~~~~~~~~

As an alternative to PostgreSQL, you also can store your data in a MySQL database. To install, run:

.. code-block:: sh

   sudo apt-get install mysql-server

Log in as *root* in your database:

.. code-block:: sh

   sudo mysql

At the MySQL prompt, run the following commands (change `user/password`` to your own values):

.. code-block:: sh

   CREATE DATABASE boards;
   GRANT ALL on boards.* to 'boardsuser'@'localhost' identified by 'boardsuser-password';

Exit the mysql-prompt:

.. code-block:: sh

   exit

Edit the Focalboard ``config.json``:

.. code-block:: sh

   nano /opt/focalboard/config.json

Change the dbconfig setting to use the MySQL database you created:

.. code-block:: sh

   "dbtype": "mysql",
   "dbconfig": "boardsuser:boardsuser-password@tcp(127.0.0.1:3306)/boards",

Configure Focalboard to run as a service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This will keep the server running across reboots. First, create a new service config file:

.. code-block:: sh

   sudo nano /lib/systemd/system/focalboard.service

Paste in the following:

.. code-block:: sh

   [Unit]
   Description=Focalboard server

   [Service]
   Type=simple
   Restart=always
   RestartSec=5s
   ExecStart=/opt/focalboard/bin/focalboard-server
   WorkingDirectory=/opt/focalboard

   [Install]
   WantedBy=multi-user.target

Make systemd reload the new unit, and start it on machine reboot:

.. code-block:: sh

   sudo systemctl daemon-reload
   sudo systemctl start focalboard.service
   sudo systemctl enable focalboard.service

Test the server
~~~~~~~~~~~~~~~~

At this point, the Focalboard server should be running.

Test that it's running locally with:

.. code-block:: sh

   curl localhost:8000
   curl localhost

The first command checks that the server is running on port 8000 (default), and the second checks that NGINX is proxying requests successfully. Both commands should return the same snippet of HTML.

To access the server remotely, open a browser to its IP address or domain.

Set up the server
~~~~~~~~~~~~~~~~~~

After installing the server, open a browser to the domain you used (or ``http://localhost:8000`` for local installs). You should be redirected to the login screen. Click the link to register a new user instead, and complete the registration.

The first user registration will always be permitted, but **subsequent registrations will require an invite link which includes a code**. You can invite additional users by clicking on your username in the top left, then selecting "Invite users".

Personal Server configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Personal Server settings are stored in ``config.json`` and are read when the server is launched. The contents are:

.. csv-table::
    :header: "Key", "Description", "Example"

    "serverRoot", "Root URL of the serverRoot URL of the server", "http://localhost:8000"
    "port", "Server port", "8000"
    "dbtype", "Type of database. ``sqlite3``, ``postgres``, or ``mysql``", "sqlite3"
    "dbconfig", "Database connection string", "``postgres://user:pass@localhost/boards?sslmode=disable&connect_timeout=10``"
    "webpath", "Path to web files", "``./webapp/pack``"
    "filespath", "Path to uploaded files folder", "``./files``"
    "telemetry", "Enable health diagnostics telemetry", "``true``"
    "prometheus_address", "Enables Prometheus metrics, if it's empty is disabled", "``:9092``"
    "session_expire_time", "Session expiration time in seconds", "2592000"
    "session_refresh_time", "Session refresh time in seconds", "18000"
    "localOnly", "Only allow connections from localhost", "``false``"
    "enableLocalMode", "Enable admin APIs on local Unix port", "``true``"
    "localModeSocketLocation", "Location of local Unix port", "``/var/tmp/focalboard_local.socket``"

Resetting passwords
~~~~~~~~~~~~~~~~~~~

By default, Personal Server exposes admin APIs on a local Unix socket at ``/var/tmp/focalboard_local.socket``. This is configurable using the ``enableLocalMode`` and ``localModeSocketLocation`` settings in ``config.json``.

To reset a user's password, you can use the following ``reset-password.sh`` script:

.. code-block:: sh

   #!/bin/bash

   if [[ $# < 2 ]] ; then
      echo 'reset-password.sh <username> <new password>'
      exit 1
   fi

   curl --unix-socket /var/tmp/focalboard_local.socket http://localhost/api/v1/admin/users/$1/password -X POST -H 'Content-Type: application/json' -d '{ "password": "'$2'" }'

After resetting a user's password (e.g. if they forgot it), direct them to change it from the user menu, by clicking on their username at the top of the sidebar.

Upgrading Personal Server
------------------------

Follow these steps to upgrade an existing Personal Server installation that was previously set up.

Use the URL of the Ubuntu archive package, ``focalboard-server-linux-amd64.tar.gz``, from the appropriate `release in GitHub <https://github.com/mattermost/focalboard/releases>`_.

Create and use a clean directory, or delete any existing packages first, then run:

.. code-block:: sh

# Download the new version (e.g. 0.7.0 here, check the release for the latest one)
   wget https://github.com/mattermost/focalboard/releases/download/v0.7.0/focalboard-server-linux-amd64.tar.gz
   tar -xvzf focalboard-server-linux-amd64.tar.gz

# Stop the server
   sudo systemctl stop focalboard.service

# Back up the old version
   sudo mv /opt/focalboard /opt/focalboard-old
   sudo mv focalboard /opt

# Copy config and move uploaded files over
   sudo mv /opt/focalboard-old/files /opt/focalboard
   sudo cp /opt/focalboard-old/config.json /opt/focalboard

# Start the server
   sudo systemctl start focalboard.service

# (Optional) delete the backup after verifying
   sudo rm -rf /opt/focalboard-old
