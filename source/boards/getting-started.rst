Getting Started
===============

Mattermost Boards (formerly known as Focalboard) is included in the Mattermost Cloud workspace, enabled by default, and upgraded automatically.

For self-managed deployments, Focalboard is available in the Plugin Marketplace.

1. As a System Admin, go to **Main Menu > Plugin Marketplace**.
2. Search for **Focalboard**.
3. Select **Install** if not yet installed, then select **Configure** to enable.
4. From the plugin configuration page, set **Enable Plugin** to **true**.
5. Select **Save** to enable the plugin.

Once installed and configured, the Focalboard plugin requires websocket traffic to be passed by the proxy. Update your NGINX or Apache web proxy config following the steps below.

Updating the NGINX web proxy config
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After following the standard `Mattermost install steps <https://docs.mattermost.com/install/install-ubuntu-1804.html#configuring-nginx-as-a-proxy-for-mattermost-server>`_, edit ``/etc/nginx/sites-available/mattermost`` and add this section to it:

.. codeblock:: bash

   location ~ /plugins/focalboard/ws/* {
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

Restart NGINX with ``sudo systemctl restart nginx``.

Updating the Apache web proxy config (unofficial)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After following the `install guide for Apache and Mattermost <https://docs.mattermost.com/install/config-apache2.html#configuring-apache2-as-a-proxy-for-mattermost-server-unofficial>`_, modify the web sockets section in ``/etc/apache2/sites-available`` as follows:

.. codeblock:: bash

 # Set web sockets
  RewriteEngine On
  RewriteCond %{REQUEST_URI} /api/v[0-9]+/(users/)?websocket|/plugins/focalboard/ws/* [NC,OR]
  RewriteCond %{HTTP:UPGRADE} ^WebSocket$ [NC,OR]
  RewriteCond %{HTTP:CONNECTION} ^Upgrade$ [NC]
  RewriteRule .* ws://127.0.0.1:8065%{REQUEST_URI} [P,QSA,L]

Restart Apache with ``sudo systemctl restart apache2``
