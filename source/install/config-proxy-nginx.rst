.. _config-proxy-nginx:

Configuring NGINX as a proxy for Mattermost Server
--------------------------------------------------

NGINX is configured using a file in the ``/etc/nginx/sites-available`` directory. You need to create the file and then enable it. When creating the file, you need the IP address of your Mattermost server and the fully qualified domain name (FQDN) of your Mattermost website.

**To configure NGINX as a proxy**

1. Log in to the server that hosts NGINX and open a terminal window.
2. Create a configuration file for Mattermost.

  ``sudo touch /etc/nginx/sites-available/mattermost``

On RHEL 7 and 8: ``sudo touch /etc/nginx/conf.d/mattermost``

3. Open the file ``/etc/nginx/sites-available/mattermost`` as *root* user in a text editor and replace its contents, if any, with the following lines. Make sure that you use your own values for the Mattermost server IP address and FQDN for *server_name*.

On RHEL 7 and 8, open the file ``/etc/nginx/conf.d/mattermost``.

SSL and HTTP/2 with server push are enabled in the provided configuration example.

.. note::
  
  - If you're going to use Let's Encrypt to manage your SSL certificate, stop here at step 3 here and see the `NGINX HTTP/2 & SSL product documentation <https://docs.mattermost.com/install/config-ssl-http2-nginx.html>`__ for details.
  - You'll need valid SSL certificates in order for NGINX to pin the certificates properly. Additionally, your browser must have permissions to accept the certificate as a valid CA-signed certificate.
  - Examples in this documentation are using a private IP address, which may not match your network configuration. 
  - In cases where the local machine resolves ``localhost`` to more than one IP address (IPv4 or IPv6), we recommend using ``127.0.0.1`` instead of ``localhost``. 

.. code-block:: none

    upstream backend {
       server 10.10.10.2:8065;
       keepalive 32;
    }

    proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=mattermost_cache:10m max_size=3g inactive=120m use_temp_path=off;

    server {
      listen 80 default_server;
      server_name   mattermost.example.com;
      return 301 https://$server_name$request_uri;
    }

    server {
       listen 443 ssl http2;
       server_name    mattermost.example.com;

       http2_push_preload on; # Enable HTTP/2 Server Push

       ssl on;
       ssl_certificate /etc/letsencrypt/live/{domain-name}/fullchain.pem;
       ssl_certificate_key /etc/letsencrypt/live/{domain-name}/privkey.pem;
       ssl_session_timeout 1d;

       # Enable TLS versions (TLSv1.3 is required upcoming HTTP/3 QUIC).
       ssl_protocols TLSv1.2 TLSv1.3;

       # Enable TLSv1.3's 0-RTT. Use $ssl_early_data when reverse proxying to
       # prevent replay attacks.
       #
       # @see: https://nginx.org/en/docs/http/ngx_http_ssl_module.html#ssl_early_data
       ssl_early_data on;

       ssl_ciphers 'ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256';
       ssl_prefer_server_ciphers on;
       ssl_session_cache shared:SSL:50m;
       # HSTS (ngx_http_headers_module is required) (15768000 seconds = 6 months)
       add_header Strict-Transport-Security max-age=15768000;
       # OCSP Stapling ---
       # fetch OCSP records from URL in ssl_certificate and cache them
       ssl_stapling on;
       ssl_stapling_verify on;

       add_header X-Early-Data $tls1_3_early_data;

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
    }

    # This block is useful for debugging TLS v1.3. Please feel free to remove this
    # and use the `$ssl_early_data` variable exposed by NGINX directly should you
    # wish to do so.
    map $ssl_early_data $tls1_3_early_data {
      "~." $ssl_early_data;
      default "";
    }

4. Remove the existing default sites-enabled file.

  ``sudo rm /etc/nginx/sites-enabled/default``

On RHEL 7 and 8: ``sudo rm /etc/nginx/conf.d/default``

5. Enable the mattermost configuration.

  ``sudo ln -s /etc/nginx/sites-available/mattermost /etc/nginx/sites-enabled/mattermost``

On RHEL 7 and 8: ``sudo ln -s /etc/nginx/conf.d/mattermost /etc/nginx/conf.d/default.conf``

6. Restart NGINX.

 ``sudo systemctl restart nginx``

7. Verify that you can see Mattermost through the proxy.

  ``curl https://localhost``

  If everything is working, you will see the HTML for the Mattermost signup page.

8. Restrict access to port 8065.

By default, the Mattermost server accepts connections on port 8065 from every machine on the network. Use your firewall to deny connections on port 8065 to all machines except the machine that hosts NGINX and the machine that you use to administer Mattermost server. If you're installing on Amazon Web Services, you can use Security Groups to restrict access.

Now that NGINX is installed and running, you can configure it to use SSL, which allows you to use HTTPS connections and the HTTP/2 protocol.

NGINX Configuration FAQ
~~~~~~~~~~~~~~~~~~~~~~~

Why are Websocket connections returning a 403 error?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is likely due to a failing cross-origin check. A check is applied for WebSocket code to see if the ``Origin`` header is the same as the host header. If it's not, a 403 error is returned. Open the file ``/etc/nginx/sites-available/mattermost`` as root in a text editor and make sure that the host header being set in the proxy is dynamic:

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

How do I setup an NGINX proxy with the Mattermost Docker installation?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

Why does NGINX fail when installing Gitlab CE with Mattermost on Azure?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You may need to update the callback URLs for the Application entry of Mattermost inside your GitLab instance.

1. Log in to your GitLab instance as the admin.
2. Go to **Admin > Applications**.
3. Select **Edit** on GitLab-Mattermost.
4. Update the Callback URLs to your new domain/URL.
5. Save the changes.
6. Update the external URL for GitLab and Mattermost in the ``/etc/gitlab/gitlab.rb`` configuration file.
