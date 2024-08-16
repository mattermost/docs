:orphan:
:nosearch:

.. This page is intentionally not accessible via the LHS navigation pane because it's common content included on other docs pages.

Configure NGINX with SSL and HTTP/2
-----------------------------------

NGINX is configured using a file in the ``/etc/nginx/sites-available`` directory. You need to create the file and then enable it. When creating the file, you need the IP address of your Mattermost server and the fully qualified domain name (FQDN) of your Mattermost website.

Using SSL gives greater security by ensuring that communications between Mattermost clients and the Mattermost server are encrypted. It also allows you to configure NGINX to use the HTTP/2 protocol.

Although you can configure HTTP/2 without SSL, both Firefox and Chrome browsers support HTTP/2 on secure connections only.

You can use any certificate that you want, but these instructions show you how to download and install certificates from `Let's Encrypt <https://letsencrypt.org/>`__, a free certificate authority.

.. note::

   If Let’s Encrypt is enabled, forward port 80 through a firewall, with :ref:`Forward80To443 <configure/environment-configuration-settings:forward port 80 to 443>` ``config.json`` setting set to ``true`` to complete the Let’s Encrypt certification. See the `Let's Encrypt/Certbot documentation <https://certbot.eff.org>`_ for additional assistance.

1. Log in to the server that hosts NGINX and open a terminal window.

2. Open the your Mattermost ``nginx.conf`` file as *root* in a text editor, then update the ``{ip}`` address in the ``upstream backend`` to point towards Mattermost (such as ``127.0.0.1:8065``), and update the ``server_name`` to be your domain for Mattermost.

  .. note::

   - On Ubuntu this file is located at ``/etc/nginx/sites-available/``. If you don't have this file, run ``sudo touch /etc/nginx/sites-available/mattermost``.
   - On CentOS/RHEL this file is located at ``/etc/nginx/conf.d/``. If you don't have this file, run ``sudo touch /etc/nginx/conf.d/mattermost``.
   - The IP address included in the examples in this documentation may not match your network configuration.
   - If you're running NGINX on the same machine as Mattermost, and NGINX resolves ``localhost`` to more than one IP address (IPv4 or IPv6), we recommend using ``127.0.0.1`` instead of ``localhost``.

  .. code-block:: text

   upstream backend {
       server {ip}:8065;
       keepalive 32;
       }

   server {
       listen 80 default_server;
       server_name mattermost.example.com;

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
           client_body_timeout 60s;
           send_timeout 300s;
           lingering_timeout 5s;
           proxy_connect_timeout 90s;
           proxy_send_timeout 300s;
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
           proxy_http_version 1.1;
           proxy_pass http://backend;
       }
   }


3. Remove the existing default sites-enabled file by running ``sudo rm /etc/nginx/sites-enabled/default`` (Ubuntu) or ``sudo rm /etc/nginx/conf.d/default`` (RHEL 8).

4. Enable the Mattermost configuration by running ``sudo ln -s /etc/nginx/sites-available/mattermost /etc/nginx/sites-enabled/mattermost`` (Ubuntu) or ``sudo ln -s /etc/nginx/conf.d/mattermost /etc/nginx/conf.d/default.conf`` (RHEL 8).

5. Run ``sudo nginx -t`` to ensure your configuration is done properly. If you get an error, look into the NGINX config and make the needed changes to the file under ``/etc/nginx/sites-available/mattermost``.

6. Restart NGINX by running ``sudo systemctl start nginx``.

7. Verify that you can see Mattermost through the proxy by running ``curl http://localhost``.

  If everything is working, you will see the HTML for the Mattermost signup page. You will see invalid certificate when accessing through the IP or localhost. Use the full FQDN domain to verify if the SSL certificate has pinned properly and is valid.

8. Install and update Snap by running ``sudo snap install core; sudo snap refresh core``.

9. Install the Certbot package by running ``sudo snap install --classic certbot``.

10. Add a symbolic link to ensure Certbot can run by running ``sudo ln -s /snap/bin/certbot /usr/bin/certbot``.

11. Run the Let's Encrypt installer dry-run to ensure your DNS is configured properly by running ``sudo certbot certonly --dry-run``.

  This will prompt you to enter your email, accept the TOS, share your email, and select the domain you're activating certbot for. This will validate that your DNS points to this server properly and you are able to successfully generate a certificate. If this finishes successfully, proceed to step 12.

12. Run the Let's Encrypt installer by running ``sudo certbot``. This will run certbot and will automatically edit your NGINX config file for the site(s) selected.

13. Ensure your SSL is configured properly by running ``curl https://{your domain here}``

14. Finally, we suggest editing your config file again to increase your SSL security settings above the default Let's Encrypt. This is the same file from Step 2 above. Edit it to look like the below:

  .. code-block:: text

   upstream backend {
       server {ip}:8065;
      keepalive 32;
       }

   proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=mattermost_cache:10m max_size=3g inactive=120m use_temp_path=off;

   server {
       server_name mattermost.example.com;

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
           client_body_timeout 60s;
           send_timeout 300s;
           lingering_timeout 5s;
           proxy_connect_timeout 90s;
           proxy_send_timeout 300s;
           proxy_read_timeout 90s;
           proxy_http_version 1.1;
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
           proxy_http_version 1.1;
           proxy_pass http://backend;
       }

       listen 443 ssl http2; # managed by Certbot
       ssl_certificate /etc/letsencrypt/live/mattermost.example.com/fullchain.pem; # managed by Certbot
       ssl_certificate_key /etc/letsencrypt/live/mattermost.example.com/privkey.pem; # managed by Certbot
       # include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
       ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

       ssl_session_timeout 1d;

       # Enable TLS versions (TLSv1.3 is required upcoming HTTP/3 QUIC).
       ssl_protocols TLSv1.2 TLSv1.3;

       # Enable TLSv1.3's 0-RTT. Use $ssl_early_data when reverse proxying to
       # prevent replay attacks.
       #
       # @see: https://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_early_data
       ssl_early_data on;

       ssl_ciphers ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES256-SHA;
       ssl_prefer_server_ciphers on;
       ssl_session_cache shared:SSL:50m;
       # HSTS (ngx_http_headers_module is required) (15768000 seconds = six months)
       add_header Strict-Transport-Security max-age=15768000;
       # OCSP Stapling ---
       # fetch OCSP records from URL in ssl_certificate and cache them
       ssl_stapling on;
       ssl_stapling_verify on;
   }


   server {
       if ($host = mattermost.example.com) {
           return 301 https://$host$request_uri;
       } # managed by Certbot


       listen 80 default_server;
       server_name mattermost.example.com;
       return 404; # managed by Certbot

   }

15.  Check that your SSL certificate is set up correctly.

  * Test the SSL certificate by visiting a site such as https://www.ssllabs.com/ssltest/index.html.
  * If there’s an error about the missing chain or certificate path, there is likely an intermediate certificate missing that needs to be included.

