.. _install-rhel-nginx:

Installing NGINX Server
=======================

In a production setting, use a proxy server for greater security and performance of Mattermost.

The main benefits of using a proxy are as follows:

  -  SSL termination
  -  HTTP to HTTPS redirect
  -  Port mapping ``:80`` to ``:8065``
  -  Standard request logs

**To install NGINX on RHEL 6.6 or 7.1:**

1. Log into the server that will host the proxy, and open a terminal window.

2. Create the file /etc/yum.repos.d/nginx.repo.
  ``sudo touch /etc/yum.repos.d/nginx.repo``

3. Open the file as root in a text editor and add the following contents, where *{version}* is **6** for RHEL 6.6, and **7** for RHEL 7.1:

  .. code-block:: none
  
    [nginx]
    name=nginx repo
    baseurl=http://nginx.org/packages/rhel/{version}/$basearch/
    gpgcheck=0
    enabled=1

4. Install NGINX.

  ``sudo yum install nginx.x86_64``

5. After the installation is complete, start NGINX.
    On RHEL 6.6:
  
    ``sudo service nginx start``
  
    On RHEL 7.1:
  
    ``sudo systemctl start nginx``
  
6. **Optional** Set NGINX to start at system boot.
  
    On RHEL 6.6:
  
    ``sudo chkconfig nginx on``
  
    On RHEL 7.1:
  
    ``sudo systemctl enable nginx``

4. Verify that NGINX is running.

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


**What to do next**

1. Map a fully qualified domain name (FQDN) such as ``mattermost.example.com`` to point to the NGINX server.
2. Configure NGINX to proxy connections from the Internet to the Mattermost Server.
