:orphan:
:nosearch:

.. This page is intentionally not accessible via the LHS navigation pane because it's common content included on other docs pages.

Configure NGINX as a proxy for Mattermost server
------------------------------------------------

NGINX is configured using a file in the ``/etc/nginx/sites-available`` directory. You need to create the file and then enable it. When creating the file, you need the IP address of your Mattermost server and the fully qualified domain name (FQDN) of your Mattermost website.

1. Log in to the server that hosts NGINX and open a terminal window.
2. Create a configuration file for Mattermost by running the following command:

  ``sudo touch /etc/nginx/sites-available/mattermost`` on Ubuntu
  ``sudo touch /etc/nginx/conf.d/mattermost`` on RHEL 8

3. Open the file ``/etc/nginx/sites-available/mattermost`` (Ubuntu) or  ``/etc/nginx/conf.d/mattermost`` (RHEL 8) as *root* user in a text editor and replace its contents, if any, with the following lines. Make sure that you use your own values for the Mattermost server IP address and FQDN for *server_name*.

SSL and HTTP/2 with server push are enabled in the provided configuration example.

  .. note::

    - If you're going to use Let's Encrypt to manage your SSL certificate, stop at step 3 and see the `NGINX HTTP/2 and SSL product documentation </install/config-ssl-http2-nginx.html>`__ for details.
    - You'll need valid SSL certificates in order for NGINX to pin the certificates properly. Additionally, your browser must have permissions to accept the certificate as a valid CA-signed certificate.
    - Note that the IP address included in the examples in this documentation may not match your network configuration.
    - If you're running NGINX on the same machine as Mattermost, and NGINX resolves ``localhost`` to more than one IP address (IPv4 or IPv6), we recommend using ``127.0.0.1`` instead of ``localhost``.

  .. code-block:: none

    upstream backend {
       server 10.10.10.2:8065;
       keepalive 32;
    }

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

       ssl_ciphers 'ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384';
       ssl_prefer_server_ciphers on;
       ssl_session_cache shared:SSL:50m;
       # HSTS (ngx_http_headers_module is required) (15768000 seconds = six months)
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

4. Remove the existing default sites-enabled file by running ``sudo rm /etc/nginx/sites-enabled/default`` (Ubuntu) or ``sudo rm /etc/nginx/conf.d/default`` (RHEL 8)

5. Enable the mattermost configuration by running ``sudo ln -s /etc/nginx/sites-available/mattermost /etc/nginx/sites-enabled/mattermost`` (Ubuntu) or ``sudo ln -s /etc/nginx/conf.d/mattermost /etc/nginx/conf.d/default.conf`` (RHEL 8)

6. Restart NGINX by running ``sudo systemctl restart nginx``.

7. Verify that you can see Mattermost through the proxy by running ``curl https://localhost``.

  If everything is working, you will see the HTML for the Mattermost signup page.

8. Restrict access to port 8065.

  By default, the Mattermost server accepts connections on port 8065 from every machine on the network. Use your firewall to deny connections on port 8065 to all machines except the machine that hosts NGINX and the machine that you use to administer the Mattermost server. If you're installing on Amazon Web Services, you can use Security Groups to restrict access.

Now that NGINX is installed and running, you can configure it to use SSL, which allows you to use HTTPS connections and the HTTP/2 protocol.
