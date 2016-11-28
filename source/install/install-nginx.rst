Set up NGINX Server
===================

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
