.. _install-haproxy:

Installing HAProxy Server
=========================

In a production setting, use a proxy server for greater security and performance of Mattermost.

The main benefits of using a proxy are as follows:

  -  SSL Termination
  -  HTTP to HTTPS redirect
  -  Port mapping ``:80`` to ``:8065``
  -  Standard request logs
  
**To install HAProxy on RHEL 6.6 or 7.1:**

1. Log in to the server that will host the proxy and open a terminal window.

2. Install HAProxy.

  ``sudo yum install haproxy``
  
3. After the installation is complete, verify that HAProxy is running.

  ``sudo systemctl status haproxy``
  
5. After the installation is complete, start NGINX.
    On RHEL 6.6:
  
    ``sudo service nginx haproxy``
  
    On RHEL 7.1:
  
    ``sudo systemctl start haproxy``

4. **Optional** Set NGINX to start at system boot.
  
    On RHEL 6.6:
  
    ``sudo chkconfig haproxy on``
  
    On RHEL 7.1:
  
    ``sudo systemctl enable haproxy``

**What to do next**

1. Map a fully qualified domain name (FQDN) such as ``mattermost.example.com`` to point to the HAProxy server.
2. Configure HAProxy to proxy connections from the internet to the mattermost Server.
