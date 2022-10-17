:nosearch:
.. This page is intentionally not accessible via the LHS navigation pane because it's common content included on other docs pages.

.. _install-nginx:

Install NGINX server
--------------------
NGINX is a popular web server and is responsible for hosting some of the largest and highest-traffic sites on the internet. It's more resource-friendly than Apache in most cases, and can be used as a web server or reverse proxy.

In a production setting, use a proxy server for greater security and performance of Mattermost.

-  SSL termination
-  HTTP to HTTPS redirect
-  Port mapping ``:80`` to ``:8065``
-  Standard request logs

Install NGINX on Ubuntu Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Log in to the server that will host the proxy and open a terminal window.

2. Install NGINX.

  Because NGINX is available in Ubuntu's default repositories, it's possible to install it from these repositories using the ``apt`` packaging system. First, update your local ``apt`` package index for access to the most recent package listings. Then, install ``nginx``:

  ``sudo apt update``
  
  ``sudo apt install nginx``

  After accepting the procedure, ``apt`` will install NGINX and any required dependencies to your server.

3. After installing it, you already have everything you need. You can point your browser to your server IP address. You should see the default NGINX landing page:

  .. image:: /images/install_nginx_welcome.png
    :alt: Example of the default NGINX landing page.

  If you see this page, you've successfully installed NGINX on your web server. This page is included with NGINX to show you that the server is running correctly.

  Or you can also verify it by running ``curl http://localhost``. 

  If NGINX is running, you see the following output:

  .. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
    <title>Welcome to nginx!</title>
    .
    .
    .
    <p><em>Thank you for using nginx.</em></p>
    </body>
    </html>

Manage the NGINX process
~~~~~~~~~~~~~~~~~~~~~~~~

Now that you have your web server up and running, let's review some basic management commands. These are all run in the command line interface.

To stop your web server, use: ``sudo systemctl stop nginx``

To start the web server when it's stopped, use: ``sudo systemctl start nginx``
 
To stop and then start the service again, use: ``sudo systemctl restart nginx``
 
If you're simply making configuration changes, NGINX can often reload without dropping connections. To do this, use: ``sudo systemctl reload nginx``
 
By default, NGINX is configured to start automatically when the server boots. If this isn't what you want, you can disable this behavior using: ``sudo systemctl disable nginx``
 
To re-enable the service to start up at boot, use: ``sudo systemctl enable nginx``

What to do next
~~~~~~~~~~~~~~~

1. Map a fully qualified domain name (FQDN) such as ``mattermost.example.com`` on your DNS server/service, to point to the NGINX server.
2. Configure NGINX to proxy connections from the internet to the Mattermost server.
