.. _install-nginx:

Installing NGINX Server
-----------------------

In a production setting, use a proxy server for greater security and performance of Mattermost.

The main benefits of using a proxy are as follows:

  -  SSL termination
  -  HTTP to HTTPS redirect
  -  Port mapping ``:80`` to ``:8065``
  -  Standard request logs

**To install NGINX on Ubuntu Server:**

1. Log in to the server that will host the proxy and open a terminal window.

2. Install NGINX.

  ``sudo apt-get install nginx``

3. After the installation is complete, verify that NGINX is running.

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

.. Note::

  You can stop, start, and restart NGINX with the following commands:

  .. code-block:: none

    sudo service nginx stop
    sudo service nginx start
    sudo service nginx restart

**What to do next**

1. Map a fully qualified domain name (FQDN) such as ``mattermost.example.com`` to point to the NGINX server.
2. Configure NGINX to proxy connections from the internet to the Mattermost Server.
