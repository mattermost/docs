.. _config-proxy-apache2:

Configuring Apache2 as a proxy for Mattermost Server (Unofficial)
-----------------------------------------------------------------

.. important:: This unofficial guide is maintained by the Mattermost community and this deployment configuration is not yet officially supported by Mattermost, Inc. `Community testing, feedback and improvements are welcome and greatly appreciated <https://github.com/mattermost/docs/issues/1295>`__. You can `edit this page on GitHub <https://github.com/mattermost/docs/blob/master/source/install/config-proxy-apache2.rst>`__.

On a Debian-based operating system such as Ubuntu, Apache2 proxy configuration is done in the ``/etc/apache2/sites-available`` directory. Red Hat-based systems organize Apache configuration files `differently <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/ch-web_servers>`__. If you're setting up Mattermost on a subdomain, you'll want to create a new configuration file along the lines of ``mysubdomain.mydomain.com.conf``.

**To configure Apache2 as a proxy**

1. SSH into your server.
2. Make sure the Apache modules ``mod_rewrite`` , ``mod_proxy``, ``mod_proxy_http``, and ``mod_proxy_wstunnel`` are installed and enabled. If not, follow the instructions from your Linux distribution to do so.
3. Create the above mentioned configuration file. It is often helpful to start with a copy of ``000-default.conf`` or ``default-ssl.conf`` (on Ubuntu).
4. Edit your configuration using the guide below:

	1. If you're not setting up a subdomain, your ``ServerName`` will simply be set to ``mydomain.com``.
	2. ``ServerAlias`` can been added too if you want to capture ``www.mydomain.com``.
	3. Remember to change the values to match your server's name, etc.
	4. If you have enabled TLS in the Mattermost settings, you must use the protocol ``wss://`` instead of ``ws://`` in the ``RewriteRule``.
	5. To serve requests on a different port (such as 8443), in addition to setting the port in the VirtualHost element, add ``Listen 8443`` on a separate line before the VirtualHost line.

.. code-block:: apacheconf

		<VirtualHost *:80>
		  # If you're not using a subdomain you may need to set a ServerAlias to:
		  # ServerAlias www.mydomain.com
		  ServerName mysubdomain.mydomain.com
		  ServerAdmin hostmaster@mydomain.com
		  ProxyPreserveHost On

		  # Set web sockets
		  RewriteEngine On
		  RewriteCond %{REQUEST_URI} /api/v[0-9]+/(users/)?websocket [NC]
		  RewriteCond %{HTTP:UPGRADE} ^WebSocket$ [NC]
		  RewriteCond %{HTTP:CONNECTION} \bUpgrade\b [NC]
		  RewriteRule .* ws://127.0.0.1:8065%{REQUEST_URI} [P,QSA,L]

		  <Location />
			Require all granted
			ProxyPass http://127.0.0.1:8065/
			ProxyPassReverse http://127.0.0.1:8065/
			ProxyPassReverseCookieDomain 127.0.0.1 mysubdomain.mydomain.com
		  </Location>

		</VirtualHost>

5. (Debian/Ubuntu only) Because you'll likely have not set up the subdomain before now on Apache2, run ``a2ensite mysubdomain.mydomain.com`` to enable the site (do not run ``a2ensite mysubdomain.mydomain.com.conf``).

6. Restart Apache2.

	- On Ubuntu 14.04 and RHEL 6: ``sudo service apache2 restart``
	- On Ubuntu 16.04+ and RHEL 7+: ``sudo systemctl restart apache2``

You should be all set! Ensure that your Mattermost config file is pointing to the correct URL (which may include a port), and then ensure that your socket connection is not dropping once deployed. To prevent external access to Mattermost on port 8065, in the config file, set ``ListenAddress`` to ``localhost:8065`` instead of ``:8065``.
