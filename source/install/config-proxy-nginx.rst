.. _config-proxy-nginx:

Configuring NGINX as a proxy for Mattermost Server
==================================================

NGINX is configured using a file in the ``/etc/nginx/sites-available`` directory. You need to create the file and then enable it. When creating the file, you need the IP address of your Mattermost server and the fully qualified domain name (FQDN) of your Mattermost website.

**To configure NGINX as a proxy**

1. Log in to the server that hosts NGINX and open a terminal window.
2. Create a configuration file for Mattermost.

  ``sudo touch /etc/nginx/sites-available/mattermost``
  
On RHEL 7: ``sudo touch /etc/nginx/conf.d/mattermost``

3. Open the file ``/etc/nginx/sites-available/mattermost`` as root in a text editor and replace its contents, if any, with the following lines. Make sure that you use your own values for the Mattermost server IP address and FQDN for *server_name*.
On RHEL 7, open the file ``/etc/nginx/conf.d/mattermost``.

  .. code-block:: none

    upstream backend {
       server 10.10.10.2:8065;
       keepalive 32;
    }

    proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=mattermost_cache:10m max_size=3g inactive=120m use_temp_path=off;

    server {
       listen 80;
       server_name    mattermost.example.com;

       location ~ /api/v[0-9]+/(users/)?websocket$ {
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
           proxy_connect_timeout 90;
           proxy_send_timeout 300;
           proxy_read_timeout 90s;
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
           proxy_http_version 1.1;
           proxy_pass http://backend;
       }
    }

4. Remove the existing default sites-enabled file.

  ``sudo rm /etc/nginx/sites-enabled/default``

On RHEL 7: ``sudo rm /etc/nginx/conf.d/default``

5. Enable the mattermost configuration.

  ``sudo ln -s /etc/nginx/sites-available/mattermost /etc/nginx/sites-enabled/mattermost``

On RHEL 7: ``sudo ln -s /etc/nginx/conf.d/mattermost /etc/nginx/conf.d/default.conf``

6. Restart NGINX.

  On Ubuntu 14.04 and RHEL 6: ``sudo service nginx restart``

  On Ubuntu 16.04, Ubuntu 18.04, Debian Stretch, and RHEL 7: ``sudo systemctl restart nginx``

7. Verify that you can see Mattermost through the proxy.

  ``curl http://localhost``

  If everything is working, you will see the HTML for the Mattermost signup page.

8. Restrict access to port 8065.
  By default, the Mattermost server accepts connections on port 8065 from every machine on the network. Use your firewall to deny connections on port 8065 to all machines except the machine that hosts NGINX and the machine that you use to administer Mattermost server. If you're installing on Amazon Web Services, you can use security groups to restrict access.

Now that NGINX is installed and running, you can configure it to use SSL, which allows you to use HTTPS connections and the HTTP/2 protocol.

**NGINX Configuration FAQ**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Why are Websocket connections returning a 403 error?**

This is likely due to a failing cross-origin check. A check is applied for WebSocket code to see if the ``Origin`` header is the same as the host header. If it's not, a 403 error is returned.  Open the file ``/etc/nginx/sites-available/mattermost`` 
as root in a text editor and make sure that the host header being set in the proxy is dynamic:

.. code-block:: none
  :emphasize-lines: 4

  location ~ /api/v[0-9]+/(users/)?websocket$ {
    proxy_pass            http://backend;
    (...)
    proxy_set_header      Host $host;
    proxy_set_header      X-Forwarded-For $remote_addr;
  }

Then in ``config.json`` set the ``AllowCorsFrom`` setting to match the domain being used by clients. You may need to add variations of the host name that clients may send. Your NGINX log will be helpful in diagnosing the problem.

.. code-block:: none
  :emphasize-lines: 2

  "EnableUserAccessTokens": false,
  "AllowCorsFrom": "domain.com domain.com:443 im.domain.com",
  "SessionLengthWebInDays": 30,

For other troubleshooting tips for WebSocket errors, see `potential solutions here <https://docs.mattermost.com/install/troubleshooting.html#please-check-connection-mattermost-unreachable-if-issue-persists-ask-administrator-to-check-websocket-port>`__.

**How do I setup an NGINX proxy with the Mattermost Docker installation?**

1. Find the name of the Mattermost network and connect it to the NGINX proxy:

  .. code-block:: none

    docker network ls
    # Grep the name of your Mattermost network like "mymattermost_default".
    docker network connect mymattermost_default nginx-proxy

2. Restart the Mattermost Docker containers

  .. code-block:: none

    docker-compose stop app
    docker-compose start app

.. tip :: There is no need to run the 'web' container, since NGINX proxy accepts incoming requests.

3. Update your docker-compose.yml file to include a new environment variable ``VIRTUAL_HOST`` and an ``expose`` directive.

  .. code-block:: none

    environment:
      # set same as db credentials and dbname
      - MM_USERNAME=mmuser
      - MM_PASSWORD=mmuser-password
      - MM_DBNAME=mattermost
      - VIRTUAL_HOST=mymattermost.tld
    expose:
      - "80"

If you are using SSL, you may also need to expose port 443. 

**Why does NGINX fail when installing Gitlab CE with Mattermost on Azure?**

You may need to update the Callback URLs for the Application entry of Mattermost inside your Gitlab instance.

1. Log into your GitLab instance as the admin
2. Go to **Admin > Applications**
3. Click **Edit** on GitLab-Mattermost
4. Update the Callback URLs to your new domain/URL
5. Save the changes
6. Update the external URL for Gitlab and Mattermost in the ``/etc/gitlab/gitlab.rb`` configuration file.
