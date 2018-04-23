.. _config-proxy-apache2:

Configuring Apache2 as a proxy for Mattermost Server (Unofficial)
==================================================================

.. important:: This unofficial guide is maintained by the Mattermost community and this deployment configuration is not yet officially supported by Mattermost, Inc. `Community testing, feedback and improvements are welcome and greatly appreciated <https://github.com/mattermost/docs/issues/1295>`_. You can `edit this page on GitHub <https://github.com/mattermost/docs/blob/master/source/install/config-proxy-apache2.rst>`_.

The Apache2 proxy configuration is done through the ``/etc/apache2/sites-available`` directory. If you're setting up Mattermost on a subdomain you'll want to create a new configuration along the lines of ``mysubdomain.mydomain.com.conf``.

Copy the `default` configuration file found in the same directory.

**To configure Apache2 as a proxy**

1. SSH into your server
2. Create/open the above mentioned, correct file (000-default or a new subdomain configuration).
3. Edit your configuration using the guide below.

	1. If you're not setting up a subdomain your ``ServerName`` will simply be set to ``mydomain.com``.
	2. ``ServerAlias`` can been added too if you want to capture ``www.mydomain.com``.
	3. Remember to change the values to match your server's name etc.
	4. Save once finished

.. code-block:: apacheconf

		<VirtualHost *:80>
		  # If you're not using a subdomain you may need to set a ServerAlias to:
		  # ServerAlias www.mydomain.com
		  ServerName mysubdomain.mydomain.com
		  ServerAdmin hostmaster@mydomain.com
		  ProxyPreserveHost On

		  # setup the proxy
		  <Proxy *>
			 Order allow,deny
			 Allow from all
		  </Proxy>

		  # Set web sockets
		  RewriteEngine On
		  RewriteCond %{REQUEST_URI} /api/v[0-9]+/(users/)?websocket [NC,OR]
		  RewriteCond %{HTTP:UPGRADE} ^WebSocket$ [NC,OR]
		  RewriteCond %{HTTP:CONNECTION} ^Upgrade$ [NC]
		  RewriteRule .* wss://127.0.0.1:8065%{REQUEST_URI} [P,QSA,L]
		  RewriteCond %{DOCUMENT_ROOT}/%{REQUEST_FILENAME} !-f
			# This line simply forces HTTPS
		  RewriteRule (.*) https://%{SERVER_NAME}%{REQUEST_URI} [END,QSA,R=permanent]

		  <LocationMatch "^/api/v(?<apiversion>[0-9]+)/(?<apiusers>users/)?websocket">
			Require all granted
			ProxyPass ws://127.0.0.1:8065/api/v%{env:MATCH_APIVERSION}/%{env:MATCH_APIUSERS}websocket
			ProxyPassReverse ws://127.0.0.1:8065/api/v%{env:MATCH_APIVERSION}/%{env:MATCH_APIUSERS}websocket
			ProxyPassReverseCookieDomain 127.0.0.1 mysubdomain.mydomain.com
		  </LocationMatch>

		  <Location />
			Require all granted
			ProxyPass http://127.0.0.1:8065/
			ProxyPassReverse http://127.0.0.1:8065/
			ProxyPassReverseCookieDomain 127.0.0.1 mysubdomain.mydomain.com
		  </Location>

		</VirtualHost>

4. Because you'll likely have not set up the subdomain before now on Apache2, run ``a2ensite mysubdomain.mydomain.com`` to enable the site (do not run ``a2ensite mysubdomain.mydomain.com.conf``)

5. Restart Apache2

	- On Ubuntu 14.04 and RHEL 6: ``sudo service apache2 restart``
	- On Ubuntu 16.04 and RHEL 7: ``sudo systemctl restart apache2``

You should be all set! Ensure that your Mattermost config file is pointing to the correct URL and then ensure that once deployed your socket connection is not dropping.
