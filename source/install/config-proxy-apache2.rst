.. _config-proxy-apache2:

Configuring Apache2 as a proxy for Mattermost Server (Unofficial)
=================================================================

.. important::

    This unofficial guide is maintained by the Mattermost community and this
    deployment configuration is not yet officially supported by Mattermost, Inc.
    Community testing, feedback and improvements are welcome and greatly
    appreciated. You can `edit this page on GitHub <https://github.com/mattermost/docs/blob/master/source/install/config-proxy-apache2.rst>`_.

The following is an exemplary description how to setup Apache ``httpd`` 2 as
proxy serving requests to the domain ``mattermost.mydomain.net`` from a
Mattermost instance that runs on the same host, listening on port ``8065``.
The Apache2 proxy configuration in this guide is done through a configuration
file for a *virtual host* ``/etc/apache2/sites-available`` directory. If you're
setting up Mattermost on a subdomain you'll want to create a new configuration,
e.g. ``mattermost.mydomain.net.conf``.

1. Login to your server.
2. If necessary, create a new configuration file.
3. Edit your configuration using the example below, replacing values to match
   your environment.

   .. code-block:: apacheconf

        <VirtualHost *:80>
          ServerName mattermost.mydomain.net
          ServerAdmin hostmaster@mydomain.net
          ProxyPreserveHost On

          # setup the proxy
          <Proxy "mattermost.mydomain.net">
            Order allow,deny
            Allow from all
          </Proxy>

          # Set web sockets
          RewriteEngine On
          RewriteCond %{REQUEST_URI} ^/api/v3/users/websocket [NC,OR]
          RewriteCond %{HTTP:UPGRADE} ^WebSocket$ [NC,OR]
          RewriteCond %{HTTP:CONNECTION} ^Upgrade$ [NC]
          RewriteRule .* wss://127.0.0.1:8065%{REQUEST_URI} [P,QSA,L]
          RewriteCond %{DOCUMENT_ROOT}/%{REQUEST_FILENAME} !-f

          <Location /api/v3/users/websocket>
            Require all granted
            ProxyPass ws://127.0.0.1:8065/api/v3/users/websocket
            ProxyPassReverse ws://127.0.0.1:8065/api/v3/users/websocket
            ProxyPassReverseCookieDomain 127.0.0.1 mattermost.mydomain.net
          </Location>

          <Location />
            Require all granted
            ProxyPass http://127.0.0.1:8065/
            ProxyPassReverse http://127.0.0.1:8065/
            ProxyPassReverseCookieDomain 127.0.0.1 mattermost.mydomain.net
          </Location>
        </VirtualHost>

4. If you created a new configuration file, enable its configuration, ensure
   necessary Apache modules are enabled, test the overall configuration and
   restart Apache::

       a2ensite mattermost.mydomain.net.conf
      a2enmod proxy_http proxy_wstunnel rewrite
      apachectl configtest
      apachectl restart

You should be all set! Ensure that your Mattermost configuration has the
``ServiceSettings.SiteURL`` set according to the configured ``ServerName``.
