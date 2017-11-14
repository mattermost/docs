.. _install-haproxy:

Installing HAProxy Server
=========================

In a production setting, use a proxy server for greater security and performance of Mattermost.

The main benefits of using a proxy are as follows:

  -  SSL Termination
  -  HTTP to HTTPS redirect
  -  Port mapping ``:80`` to ``:8065``
  -  Standard request logs
  
**To install HAProxy on Ubuntu Server:**

1. Log in to the server that will host the proxy and open a terminal window.

2. Install HAProxy.

  ``sudo apt-get install haproxy``
  
3. After the installation is complete, verify that HAProxy is running.

  ``sudo systemctl status haproxy``
  
.. Note::

  You can stop, start and restart HAProxy with the following commands:

  .. code-block:: none
  
    sudo service systemctl stop haproxy
    sudo service systemctl start haproxy
    sudo service systemctl restart haproxy

**What to do next**

1. Map a fully qualified domain name (FQDN) such as ``mattermost.example.com`` to point to the HAProxy server.
2. Configure HAProxy to proxy connections from the internet to the mattermost Server.
