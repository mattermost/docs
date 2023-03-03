:nosearch:

.. _config-proxy-apache2:

Configuring Apache2 as a reverse proxy for Mattermost Server (Unofficial)
-----------------------------------------------------------------

.. important:: This unofficial guide is maintained by the Mattermost community and this deployment configuration is not yet officially supported by Mattermost, Inc. `Community testing, feedback and improvements are welcome and greatly appreciated <https://github.com/mattermost/docs/issues/1295>`__. You can `edit this page on GitHub <https://github.com/mattermost/docs/blob/master/source/configure/config-proxy-apache2.rst>`__.

On a Debian-based operating system such as Ubuntu, Apache2 reverse proxy configuration is done in the ``/etc/apache2/sites-available`` directory. Red Hat-based systems organize Apache configuration files `differently <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/ch-web_servers>`__. If you're setting up Mattermost on a subdomain, you'll want to create a new configuration file along the lines of ``mysubdomain.mydomain.com.conf`` and enable it afterwards (usually with ``a2ensite mysubdomain.mydomain.com``).

**To configure Apache2 (>= 2.4.47) as a reverse proxy**

1. SSH into your server.
2. Make sure the Apache modules ``mod_rewrite``, ``mod_proxy`` and ``mod_proxy_http`` are installed and enabled. If not, follow the instructions from your Linux distribution to do so (usually this is being done with ``a2enmod rewrite``, ``a2enmod proxy`` and ``a2enmod proxy_http``).
3. Create the above mentioned configuration file. It is often helpful to start with a copy of ``000-default.conf`` or ``default-ssl.conf`` (on Ubuntu).
4. Edit your configuration using the guide below:

    1. If you're not setting up a subdomain, your ``ServerName`` will simply be set to ``mymattermost.tld``.
    2. ``ServerAlias`` can been added too if you want to capture any other (sub)domains.
    3. Remember to change the values to match your server's name, etc.
    4. If you have enabled TLS in the Mattermost settings, you must also enable the SSL module in Apache (usually with ``a2enmod ssl``) and change the ``http://`` part of the proxy destination to ``https://`` additionally to enabling the ``SSLProxyEngine``.
    5. To serve requests on a different port (such as 8443), in addition to setting the port in the VirtualHost element, add ``Listen 8443`` on a separate line before the VirtualHost line.

.. code-block:: apacheconf

        <VirtualHost *:80>
          ServerName mymattermost.tld
          # Uncomment the following line if this host also should be reachable on a different domain
          # ServerAlias sub.mymattermost.tld
          ServerAdmin hostmaster@mymattermost.tld
          
          RewriteEngine On
          RewriteRule "^/(.*)" "https://mymattermost.tld/$1" [R=301,L]
        </VirtualHost>
          
        <VirtualHost *:443>
          ServerName mymattermost.tld
          # Uncomment the following line if this host also should be reachable on a different domain
          # ServerAlias sub.mymattermost.tld
          ServerAdmin hostmaster@mymattermost.tld
          ProxyPreserveHost On

          ProxyPassMatch "^/(api/v[0-9]+/(users/)?websocket)$" "http://127.0.0.1:8065/$1" upgrade=websocket
          ProxyPassMatch "^/(plugins/focalboard/ws/.*$)" "http://127.0.0.1:8065/$1" upgrade=websocket
          ProxyPass / http://127.0.0.1:8065/
          ProxyPassReverse / http://127.0.0.1:8065/
          ProxyPassReverseCookieDomain 127.0.0.1 mymattermost.tld
          
          SSLEngine On
          SSLCertificateFile /path/to/your/certificate.pem
          SSLCertificateKeyFile /path/to/your/certificate.key
          
          # Uncomment the following line if your Mattermost server is requiring SSL/TLS connections
          # SSLProxyEngine On
        </VirtualHost>

6. Restart Apache2.

    - On Ubuntu 14.04 and RHEL 6: ``sudo service apache2 restart``
    - On Ubuntu 16.04+ and RHEL 7+: ``sudo systemctl restart apache2``

You should be all set! Ensure that your Mattermost config file is pointing to the correct URL (which may include a port), and then ensure that your socket connection is not dropping once deployed. To prevent external access to Mattermost on port 8065, in the config file, set ``ListenAddress`` to ``localhost:8065`` instead of ``:8065``.

**To configure Apache2 (< 2.4.47) as a reverse proxy**

1. Follow the instructions from above, but additionally also install and enable the ``mod_proxy_wstunnel`` module (usually with ``a2enmod proxy_wstunnel`` after it has been installed)

2. Use the following configuration

.. code-block:: apacheconf

        <VirtualHost *:80>
          ServerName mymattermost.tld
          # Uncomment the following line if this host also should be reachable on a different domain
          # ServerAlias sub.mymattermost.tld
          ServerAdmin hostmaster@mymattermost.tld
          
          RewriteEngine On
          RewriteRule "^/(.*)" "https://mymattermost.tld/$1" [R=301,L]
        </VirtualHost>

        <VirtualHost *:443>
          ServerName mymattermost.tld
          # Uncomment the following line if this host also should be reachable on a different domain
          # ServerAlias sub.mymattermost.tld
          ServerAdmin hostmaster@mymattermost.tld
          ProxyPreserveHost On

          # Set web sockets
          RewriteEngine On
          RewriteCond %{REQUEST_URI} /api/v[0-9]+/(users/)?websocket [NC,OR]
          RewriteCond %{REQUEST_URI} /plugins/focalboard/ws/ [NC]
          RewriteCond %{HTTP:UPGRADE} ^WebSocket$ [NC,OR]
          RewriteCond %{HTTP:CONNECTION} ^Upgrade$ [NC]
          RewriteRule .* ws://127.0.0.1:8065%{REQUEST_URI} [P,QSA,L]

          <Location />
            Require all granted
            ProxyPass http://127.0.0.1:8065/
            ProxyPassReverse http://127.0.0.1:8065/
            ProxyPassReverseCookieDomain 127.0.0.1 mymattermost.tld
          </Location>

          SSLEngine On
          SSLCertificateFile /path/to/your/certificate.pem
          SSLCertificateKeyFile /path/to/your/certificate.key
          
          # Uncomment the following line if your Mattermost server is requiring SSL/TLS connections
          # SSLProxyEngine On
        </VirtualHost>

 3. If you have enabled TLS in the Mattermost settings, you must also enable the SSL module in Apache (usually with ``a2enmod ssl``) and change the ``http://`` part of the proxy destination to ``https://`` and the websocket protocol from ``ws://`` to ``wss://`` additionally to enabling the ``SSLProxyEngine``.
