.. _config-ssl-http2-nginx:

Configuring NGINX with SSL and HTTP/2
-------------------------------------

NGINX is configured using a file in the ``/etc/nginx/sites-available`` directory. You need to create the file and then enable it. When creating the file, you need the IP address of your Mattermost server and the fully qualified domain name (FQDN) of your Mattermost website.

Using SSL gives greater security by ensuring that communications between Mattermost clients and the Mattermost server are encrypted. It also allows you to configure NGINX to use the HTTP/2 protocol.

Although you can configure HTTP/2 without SSL, both Firefox and Chrome browsers support HTTP/2 on secure connections only.

You can use any certificate that you want, but these instructions show you how to download and install certificates from `Let's Encrypt <https://letsencrypt.org/>`__, a free certificate authority.

.. note::
   If Let’s Encrypt is enabled, forward port 80 through a firewall, with `Forward80To443 <https://docs.mattermost.com/administration/config-settings.html#forward-port-80-to-443>`__ ``config.json`` setting set to ``true`` to complete the Let’s Encrypt certification.

**To configure NGINX as a proxy with SSL and HTTP/2**

If you're looking for additional Let's Encrypt/Certbot assistance you can access their documentation `here <https://certbot.eff.org>`_ .

1. Log in to the server that hosts NGINX and open a terminal window.

2. Open the your Mattermost ``nginx.conf`` file as *root* in a text editor and update the ``{ip}`` address in the ``upstream backend`` to point towards Mattermost (ex: ``127.0.0.1:8065``, and the ``server_name`` to be your domain for Mattermost.

.. note::
   On Ubuntu this file is located at ``/etc/nginx/sites-available/``. If you don't have this file run ``sudo touch /etc/nginx/sites-available/mattermost``.
   On CentOS/RHEL this file is located at ``/etc/nginx/conf.d/``. If you don't have this file run ``sudo touch /etc/nginx/conf.d/mattermost``.
   
.. code-block:: none

   upstream backend {
       server {ip}:8065;
       keepalive 32;
       }

   proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=mattermost_cache:10m max_size=3g inactive=120m use_temp_path=off;

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


3. Remove the existing default sites-enabled file.

  ``sudo rm /etc/nginx/sites-enabled/default``

   On RHEL 7+: ``sudo rm /etc/nginx/conf.d/default``

4. Enable the Mattermost configuration.

  ``sudo ln -s /etc/nginx/sites-available/mattermost /etc/nginx/sites-enabled/mattermost``

   On RHEL 7+: ``sudo ln -s /etc/nginx/conf.d/mattermost /etc/nginx/conf.d/default.conf``
   
5. Run ``sudo nginx -t`` to ensure your configuration is done properly. If you get an error, look into the NGINX config and make the needed changes to the file under ``/etc/nginx/sites-available/mattermost``.

6. Restart NGINX.

  On Ubuntu 18.04+, RHEL 7+:

  ``sudo systemctl start nginx``

7. Verify that you can see Mattermost through the proxy.

  ``curl http://localhost``

  If everything is working, you will see the HTML for the Mattermost signup page. You will see invalid certificate when accessing through the IP or localhost. Use the full FQDN domain to verify if the SSL certificate has pinned properly and is valid.

8. Install and update Snap.

  ``sudo snap install core; sudo snap refresh core``

9. Install the Certbot package.

  ``sudo snap install --classic certbot``

10. Add a symbolic link to ensure Certbot can run.

  ``sudo ln -s /snap/bin/certbot /usr/bin/certbot``

11. Run the Let's Encrypt installer dry-run to ensure your DNS is configured properly.

  ``sudo certbot certonly --dry-run``

  This will prompt you to enter your email, accept the TOS, share your email, and select the domain you're activating certbot for. This will validate that your DNS points to this server properly and you are able to successfully generate a certificate. If this finishes successfully, proceed to step 12.
  
12. Run the Let's Encrypt installer.

  ``sudo certbot``

  This will run certbot and will automatically edit your NGINX config file for the site(s) selected.
  
13. Ensure your SSL is configured properly by running:

   ``curl https://{your domain here}``

14. Finally, we suggest editing your config file again to increase your SSL security settings above the default Let's Encrypt. This is the same file from Step 2 above. Edit it to look like the below:

.. code-block:: none

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
           client_body_timeout 60;
           send_timeout 300;
           lingering_timeout 5;
           proxy_connect_timeout 90;
           proxy_send_timeout 300;
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
           proxy_cache mattermost_cache;
           proxy_cache_revalidate on;
           proxy_cache_min_uses 2;
           proxy_cache_use_stale timeout;
           proxy_cache_lock on;
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

       ssl_ciphers ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA;
       ssl_prefer_server_ciphers on;
       ssl_session_cache shared:SSL:50m;
       # HSTS (ngx_http_headers_module is required) (15768000 seconds = 6 months)
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

15. Check that your SSL certificate is set up correctly.

  * Test the SSL certificate by visiting a site such as https://www.ssllabs.com/ssltest/index.html.
  * If there’s an error about the missing chain or certificate path, there is likely an intermediate certificate missing that needs to be included.

NGINX Configuration FAQ
~~~~~~~~~~~~~~~~~~~~~~~

**Why are Websocket connections returning a 403 error?**

This is likely due to a failing cross-origin check. A check is applied for WebSocket code to see if the ``Origin`` header is the same as the host header. If it's not, a 403 error is returned. Open the file ``/etc/nginx/sites-available/mattermost`` as *root* in a text editor and make sure that the host header being set in the proxy is dynamic:

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

1. Find the name of the Mattermost network and connect it to the NGINX proxy.

.. code-block:: none

    docker network ls
    # Grep the name of your Mattermost network like "mymattermost_default".
    docker network connect mymattermost_default nginx-proxy

2. Restart the Mattermost Docker containers.

.. code-block:: none

    docker-compose stop app
    docker-compose start app

.. tip::

  You don't need to run the 'web' container, since NGINX proxy accepts incoming requests.

3. Update your ``docker-compose.yml`` file to include a new environment variable ``VIRTUAL_HOST`` and an ``expose`` directive.

.. code-block:: none

    environment:
      # set same as db credentials and dbname
      - MM_USERNAME=mmuser
      - MM_PASSWORD=mmuser-password
      - MM_DBNAME=mattermost
      - VIRTUAL_HOST=mymattermost.tld
    expose:
      - "80"
      - "443"

**Why does NGINX fail when installing Gitlab CE with Mattermost on Azure?**

You may need to update the Callback URLs for the Application entry of Mattermost inside your GitLab instance.

1. Log in to your GitLab instance as the admin.
2. Go to **Admin > Applications**.
3. Select **Edit** on GitLab-Mattermost.
4. Update the callback URLs to your new domain/URL.
5. Save the changes.
6. Update the external URL for GitLab and Mattermost in the ``/etc/gitlab/gitlab.rb`` configuration file.

**Why does Certbot fail the http-01 challenge?**

.. code-block:: none

      Requesting a certificate for yourdomain.com
      Performing the following challenges:
      http-01 challenge for yourdomain.com
      Waiting for verification...
      Challenge failed for domain yourdomain.com
      http-01 challenge for yourdomain.com
      Cleaning up challenges
      Some challenges have failed.
   
If you see the above errors this is typically because certbot was not able to access port 80. This can be due to a firewall or other DNS configuration. Ensure that your A/AAAA records are pointing to this server and your ``server_name`` within the NGINX config does not have a redirect.

.. note::
   If you're using Cloudflare you'll need to disable ``force traffic to https``.

**Certbot rate limiting**

If you're running certbot as stand-alone you'll see this error:

.. code-block:: none

      Error: Could not issue a Let's Encrypt SSL/TLS certificate for example.com.
      One of the Let's Encrypt rate limits has been exceeded for example.com.
      See the related Knowledge Base article for details.
      Details
      Invalid response from https://acme-v02.api.letsencrypt.org/acme/new-order.
      Details:
      Type: urn:ietf:params:acme:error:rateLimited
      Status: 429
      Detail: Error creating new order :: too many failed authorizations recently: see https://letsencrypt.org/docs/rate-limits/

If you're running Let's Encrypt within Mattermost you'll see this error:

.. code-block:: none

      {"level":"error","ts":1609092001.752515,"caller":"http/server.go:3088","msg":"http: TLS handshake error from ip:port: 429 urn:ietf:params:acme:error:rateLimited: Error creating new order :: too many failed authorizations recently: see https://letsencrypt.org/docs/rate-limits/","source":"httpserver"}

This means that you've attempted to generate a cert too many times. You can find more information `here <https://letsencrypt.org/docs/rate-limits>`_.
