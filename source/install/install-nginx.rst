.. _install-nginx:

Installing NGINX Server
-----------------------

In a production setting, use a proxy server for greater security and performance of Mattermost.

The main benefits of using a proxy are as follows:

  -  SSL termination
  -  HTTP to HTTPS redirect
  -  Port mapping ``:80`` to ``:8065``
  -  Standard request logs

**Introduction**

Nginx is one of the most popular web servers in the world and is responsible for hosting some of the largest and highest-traffic sites on the internet. 
It is more resource-friendly than Apache in most cases and can be used as a web server or reverse proxy.

**To install NGINX on Ubuntu Server:**

1. Log in to the server that will host the proxy and open a terminal window.

2. Install NGINX.

Because Nginx is available in Ubuntu’s default repositories, it is possible to install it from these repositories using the ``apt`` packaging system.

Since this is our first interaction with the ``apt`` packaging system in this session, we will update our local package index so that we have access to the most recent package listings. Afterwards, we can install ``nginx``:

  ``sudo apt update``
  ``sudo apt install nginx``

After accepting the procedure, ``apt`` will install Nginx and any required dependencies to your server.

3. After installing it, you already have everything you need. You can point your browser to your server IP address. You should see the default Nginx landing page:

  ..figure:: ../images/install_nginx_welcome.png

  If you see this page, you have successfully installed Nginx on your web server. This page is included with Nginx to show you that the server is running correctly.

  Or you can also verify it by:

  ``curl http://localhost``

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

**Managing the Nginx Process**

Now that you have your web server up and running, let’s review some basic management commands.

To stop your web server, type:

``sudo systemctl stop nginx``

To start the web server when it is stopped, type:

``sudo systemctl start nginx``
 
To stop and then start the service again, type:

``sudo systemctl restart nginx``
 
If you are simply making configuration changes, Nginx can often reload without dropping connections. To do this, type:

``sudo systemctl reload nginx``
 
By default, Nginx is configured to start automatically when the server boots. If this is not what you want, you can disable this behavior by typing:

``sudo systemctl disable nginx``
 
To re-enable the service to start up at boot, you can type:

``sudo systemctl enable nginx``

**What to do next**

1. Map a fully qualified domain name (FQDN) such as ``mattermost.example.com`` to point to the NGINX server.
2. Configure NGINX to proxy connections from the internet to the Mattermost Server.
