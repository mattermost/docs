.. _config-proxy-nginx:

Configuring NGINX as a proxy for Mattermost Server
==================================================

NGINX is configured using a file in the ``/etc/nginx/sites-available`` directory. You need to create the file and then enable it. When creating the file, you need the IP address of your Mattermost server and the fully qualified domain name (FQDN) of your Mattermost website.

**To configure NGINX as a proxy**

1. Log in to the server that hosts NGINX and open a terminal window.
2. Create a configuration file for Mattermost.

  ``sudo touch /etc/nginx/sites-available/mattermost``

3. Open the file ``/etc/nginx/sites-available/mattermost`` as root in a text editor and replace its contents, if any, with the following lines. Make sure that you use your own values for the Mattermost server IP address and FQDN for *server_name*.

  .. code-block:: none

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

4. Remove the existing default sites-enabled file.

  ``sudo rm /etc/nginx/sites-enabled/default``

5. Enable the mattermost configuration.

  ``sudo ln -s /etc/nginx/sites-available/mattermost /etc/nginx/sites-enabled/mattermost``

6. Restart NGINX.

  On Ubuntu 14.04 and RHEL 6.6: ``sudo service nginx restart``

  On Ubuntu 16.04 and RHEL 7.1: ``sudo systemctl restart nginx``

7. Verify that you can see Mattermost through the proxy.

  ``curl http://localhost``

  If everything is working, you will see the HTML for the Mattermost signup page.

8. Make sure that Mattermost accepts connections only from the proxy.

  By default, the Mattermost server accepts connections on port 8065 from every machine on the network. You should make sure that Mattermost accepts connections on port 8065 only from the machine that hosts NGINX.

  a. On the Mattermost server, open ``config.json`` as root in a text editor. The default location of ``config.json`` is ``/opt/mattermost/config/config.json``.

  b. Locate the line ``"ListenAddress": ":8065",`` and change it to ``"ListenAddress": "{IP-address}:8065",`` where *{IP-address}* is the address or domain name of the machine that hosts NGINX. For example, if NGINX and Mattermost are on the same machine, change the line to ``"ListenAddress": "localhost:8065",``

  c. Restart the Mattermost server for the changes to take effect.

    On Ubuntu 14.04 and RHEL 6.6: ``sudo service mattermost restart``

    On Ubuntu 16.04 and RHEL 7.1: ``sudo systemctl restart mattermost``

Now that NGINX is installed and running, you can configure it to use SSL, which allows you to use HTTPS connections and the HTTP/2 protocol.
