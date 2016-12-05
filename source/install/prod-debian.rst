..  _prod-debian:

Production Install on Debian Jessie
===================================

Install Mattermost in production mode on one, two or three machines, using the following steps:

.. attention:: This unofficial guide is maintained by the Mattermost community and this deployment configuration is not yet officially supported by Mattermost, Inc. `Community testing, feedback and improvements are welcome and greatly appreciated. <https://github.com/mattermost/platform/issues/1185>`_
 
.. contents::
    :backlinks: top

Install Debian Jessie (x64)
---------------------------

1. Set up 3 machines with Debian Jessie with 2GB of RAM or more. The
   servers will be used for the Load Balancer, Mattermost (this must be
   x64 to use pre-built binaries), and Database.
2. This can also be set up all on a single server for small teams:

   -  I have a Mattermost instance running on a single Debian Jessie
      server with 1GB of ram and 30 GB SSD
   -  This has been working in production for ~20 users without issue.
   -  The only difference in the below instructions for this method is
      to do everything on the same server

3. Make sure the system is up to date with the most recent security
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

    -  ``postgres=# \q``

9.  You can exit the postgres account by typing:

    -  ``exit``

10. Allow Postgres to listen on all assigned IP Addresses

    -  ``sudo vi /etc/postgresql/9.3/main/postgresql.conf``
    -  Uncomment 'listen\_addresses' and change 'localhost' to '\*'

11. Alter pg\_hba.conf to allow the mattermost server to talk to the
    postgres database

    -  ``sudo vi /etc/postgresql/9.3/main/pg_hba.conf``
    -  Add the following line to the 'IPv4 local connections'
    -  host all all 10.10.10.2/32 md5

12. Reload Postgres database

    -  ``sudo /etc/init.d/postgresql reload``

13. Attempt to connect with the new created user to verify everything
    looks good

    -  ``psql --host=10.10.10.1 --dbname=mattermost --username=mmuser --password``
    -  ``mattermost=> \q``

Set up Mattermost Server
------------------------

1. For the purposes of this guide we will assume this server has an IP
   address of 10.10.10.1
2. Download the latest Mattermost Server by typing:

   -  ``wget https://releases.mattermost.com/X.X.X/mattermost-team-X.X.X-linux-amd64.tar.gz``
   -  Where vX.X.X is the latest Mattermost release version. For
      example, v2.0.0

3. Install Mattermost under /opt

   -  Unzip the Mattermost Server by typing:
   -  ``tar -xvzf mattermost-team-X.X.X-linux-amd64.tar.gz``
   -  ``sudo mv mattermost /opt``

4. Create the storage directory for files. We assume you will have
   attached a large drive for storage of images and files. For this
   setup we will assume the directory is located at
   ``/opt/mattermost/data``.

   -  Create the directory by typing:
   -  ``sudo mkdir -p /opt/mattermost/data``

5. Create a system user and group called mattermost that will run this
   service

   -  ``sudo useradd -r mattermost -U``
   -  Set the mattermost account as the directory owner by typing:
   -  ``sudo chown -R mattermost:mattermost /opt/mattermost``
   -  ``sudo chmod -R g+w /opt/mattermost``
   -  Add yourself to the mattermost group to ensure you can edit these
      files:
   -  ``sudo usermod -aG mattermost USERNAME``

6. Configure Mattermost Server by editing the config.json file at
   /opt/mattermost/config

   -  ``cd /opt/mattermost/config``
   -  Edit the file by typing:
   -  ``vi config.json``
   -  replace ``DriverName": "mysql"`` with ``DriverName": "postgres"``
   -  replace
      ``"DataSource": "mmuser:mostest@tcp(dockerhost:3306)/mattermost_test?charset=utf8mb4,utf8"``
      with
      ``"DataSource": "postgres://mmuser:mmuser_password@10.10.10.1:5432/mattermost?sslmode=disable&connect_timeout=10"``

      -  Assuming a default IP address of 10.10.10.1
   
   -  ``config.json`` contains some configuration options that are relevant to the security of your mattermost instance.
      Therefore you should make sure you changed all those options from the default configuration to something different.
      This includes, but is not limited to, the following configuration options:
      * ``PublicLinkSalt``, ``InviteSalt``, ``PasswordResetSalt``, ``AtRestEncryptKey``

   -  Optionally you may continue to edit configuration settings in
      ``config.json`` or use the System Console described in a later
      section to finish the configuration.

7. Test the Mattermost Server

   -  ``cd /opt/mattermost/bin``
   -  Run the Mattermost Server by typing:
   -  ``./platform``
   -  You should see a console log like ``Server is listening on :8065``
      letting you know the service is running.
   -  Stop the server for now by typing ``ctrl-c``

8. Setup Mattermost to use the systemd init daemon which handles
   supervision of the Mattermost process
   
   **Set up systemd with a unit file**
   
   -  ``sudo touch /etc/systemd/system/mattermost.service``
   -  ``sudo vi /etc/systemd/system/mattermost.service``
   -  Copy the following lines into ``/etc/systemd/system/mattermost.service``

      ::

         [Unit]
         Description=Mattermost is an open source, self-hosted Slack-alternative
         After=syslog.target network.target
         
         [Service]
         Type=simple
         User=mattermost
         Group=mattermost
         ExecStart=/opt/mattermost/bin/platform
         PrivateTmp=yes
         WorkingDirectory=/opt/mattermost
         Restart=always
         RestartSec=30
         LimitNOFILE=49152
         
         [Install]
         WantedBy=multi-user.target
   
   - ``systemctl daemon-reload``
   - ``systemctl enable mattermost``
   - ``systemctl start mattermost``
   
   **Set up systemd with a legacy init script** (applies to Debian installations that are not using systemd)

   -  ``sudo touch /etc/init.d/mattermost``
   -  ``sudo vi /etc/init.d/mattermost``
   -  Copy the following lines into ``/etc/init.d/mattermost``

      ::

          #! /bin/sh
         ### BEGIN INIT INFO
         # Provides:          mattermost
         # Required-Start:    $network $syslog
         # Required-Stop:     $network $syslog
         # Default-Start:     2 3 4 5
         # Default-Stop:      0 1 6
         # Short-Description: Mattermost Group Chat
         # Description:       Mattermost: An open-source Slack
         ### END INIT INFO
         
         PATH=/sbin:/usr/sbin:/bin:/usr/bin
         DESC="Mattermost"
         NAME=mattermost
         MATTERMOST_ROOT=/opt/mattermost
         MATTERMOST_GROUP=mattermost
         MATTERMOST_USER=mattermost
         DAEMON="$MATTERMOST_ROOT/bin/platform"
         PIDFILE=/var/run/$NAME.pid
         SCRIPTNAME=/etc/init.d/$NAME
         
         . /lib/lsb/init-functions
         
         do_start() {
             # Return
             #   0 if daemon has been started
             #   1 if daemon was already running
             #   2 if daemon could not be started
             start-stop-daemon --start --quiet \
                 --chuid $MATTERMOST_USER:$MATTERMOST_GROUP --chdir $MATTERMOST_ROOT --background \
                 --pidfile $PIDFILE --exec $DAEMON --test > /dev/null \
                 || return 1
             start-stop-daemon --start --quiet \
                 --chuid $MATTERMOST_USER:$MATTERMOST_GROUP --chdir $MATTERMOST_ROOT --background \
                 --make-pidfile --pidfile $PIDFILE --exec $DAEMON \
                 || return 2
         }
         
         #
         # Function that stops the daemon/service
         #
         do_stop() {
             # Return
             #   0 if daemon has been stopped
             #   1 if daemon was already stopped
             #   2 if daemon could not be stopped
             #   other if a failure occurred
             start-stop-daemon --stop --quiet --retry=TERM/30/KILL/5 \
                 --pidfile $PIDFILE --exec $DAEMON
             RETVAL="$?"
             [ "$RETVAL" = 2 ] && return 2
             # Wait for children to finish too if this is a daemon that forks
             # and if the daemon is only ever run from this initscript.
             # If the above conditions are not satisfied then add some other code
             # that waits for the process to drop all resources that could be
             # needed by services started subsequently.  A last resort is to
             # sleep for some time.
             start-stop-daemon --stop --quiet --oknodo --retry=0/30/KILL/5 \
                 --exec $DAEMON
             [ "$?" = 2 ] && return 2
             # Many daemons don't delete their pidfiles when they exit.
             rm -f $PIDFILE
             return "$RETVAL"
         }
         
         case "$1" in
         start)
             [ "$VERBOSE" != no ] && log_daemon_msg "Starting $DESC" "$NAME"
             do_start
             case "$?" in
                     0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
                     2) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
             esac
             ;;
         stop)
             [ "$VERBOSE" != no ] && log_daemon_msg "Stopping $DESC" "$NAME"
             do_stop
             case "$?" in
                     0|1) [ "$VERBOSE" != no ] && log_end_msg 0 ;;
                     2) [ "$VERBOSE" != no ] && log_end_msg 1 ;;
             esac
             ;;
         status)
             status_of_proc "$DAEMON" "$NAME" && exit 0 || exit $?
             ;;
         restart|force-reload)
             #
             # If the "reload" option is implemented then remove the
             # 'force-reload' alias
             #
             log_daemon_msg "Restarting $DESC" "$NAME"
             do_stop
             case "$?" in
             0|1)
                     do_start
                     case "$?" in
                             0) log_end_msg 0 ;;
                             1) log_end_msg 1 ;; # Old process is still running
                             *) log_end_msg 1 ;; # Failed to start
                     esac
                     ;;
             *)
                     # Failed to stop
                     log_end_msg 1
                     ;;
             esac
             ;;
         *)
             echo "Usage: $SCRIPTNAME {start|stop|status|restart|force-reload}" >&2
             exit 3
             ;;
         esac
         
         exit 0

   -  Make sure that /etc/init.d/mattermost is executable

      -  ``sudo chmod +x /etc/init.d/mattermost``
   
   - ``systemctl daemon-reload``
   - ``systemctl enable mattermost``
   - ``systemctl start mattermost``


Set up NGINX Server
-------------------

1. For the purposes of this guide we will assume this server has an IP
   address of 10.10.10.3
2. We use NGINX for proxying request to the Mattermost Server. The main
   benefits are:

   -  SSL termination
   -  http to https redirect
   -  Port mapping :80 to :8065
   -  Standard request logs

3. Install NGINX on Debian with

   -  ``sudo apt-get install nginx``

4. Verify NGINX is running

   -  ``curl http://10.10.10.3``
   -  You should see a *Welcome to nginx!* page

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

   -  Remove the existing file with

      -  ``sudo rm /etc/nginx/sites-enabled/default``

   -  Link the mattermost config by typing:

      -  ``sudo ln -s /etc/nginx/sites-available/mattermost /etc/nginx/sites-enabled/mattermost``

   -  Restart NGINX by typing:

      -  ``sudo service nginx restart``

   -  Verify you can see Mattermost thru the proxy by typing:

      -  ``curl http://localhost``

   -  You should see a page titles *Mattermost - Signup*

Set up NGINX with SSL (Recommended)
-----------------------------------

1. You can use a free and an open certificate security like let's
   encrypt, this is how to proceed

   -  ``sudo apt-get install git``
   -  ``git clone https://github.com/letsencrypt/letsencrypt``
   -  ``cd letsencrypt``
   -  Be sure that the port 80 is not use by stopping nginx
   -  ``sudo service nginx stop``
   -  ``netstat -na | grep ':80.*LISTEN'``
   -  ``./letsencrypt-auto certonly --standalone``
   -  This command will download packages and run the instance, after
      that you will have to give your domain name
   -  You can find your certificate in /etc/letsencrypt/live

2. Modify the file at ``/etc/nginx/sites-available/mattermost`` and add
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

3. Be sure to restart nginx

   -  ``sudo service nginx start``

4. Add the following line to cron so the cert will renew every month

   -  ``crontab -e``
   -  ``@monthly /home/YOURUSERNAME/letsencrypt/letsencrypt-auto certonly --reinstall -d yourdomainname && sudo service nginx reload``

5. Check that your SSL certificate is set up correctly

   - Test the SSL certificate by visiting a site such as `https://www.ssllabs.com/ssltest/index.html <https://www.ssllabs.com/ssltest/index.html>`_
   - If there’s an error about the missing chain or certificate path, there is likely an intermediate certificate missing that needs to be included

Finish Mattermost Server setup
------------------------------

1. Navigate to ``https://mattermost.example.com`` and create a team and
   user.
2. The first user in the system is automatically granted the
   ``system_admin`` role, which gives you access to the System Console.
3. From the ``town-square`` channel click the dropdown and choose the
   ``System Console`` option
4.  Update **Notification** > **Email** settings to setup an SMTP email service. The example below assumes AmazonSES.

   -  Set *Send Email Notifications* to true
   -  Set *Require Email Verification* to true
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

   -  Set *Vary By Remote Address* to false
   -  Set *Vary By HTTP Header* to X-Real-IP

8. Feel free to modify other settings.
9. Restart the Mattermost Service by typing:

   -  ``sudo restart mattermost``
