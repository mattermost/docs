.. _install-rhel-66-nginx:

Installing NGINX Server
=======================

In a production setting, use a proxy server for greater security and performance of Mattermost.

The main benefits of using a proxy are as follows:

  -  SSL termination
  -  HTTP to HTTPS redirect
  -  Port mapping ``:80`` to ``:8065``
  -  Standard request logs

**To install NGINX on RHEL 6.6:**

1. Log into the server that will host the proxy, and open a terminal window.

3. Install NGINX on RHEL with

   -  ``sudo vi /etc/yum.repos.d/nginx.repo``
   -  Copy the below into the file

   ::

       [nginx]
       name=nginx repo
       baseurl=http://nginx.org/packages/rhel/6/$basearch/
       gpgcheck=0
       enabled=1

   -  ``sudo yum install nginx.x86_64``
   -  ``sudo service nginx start``
   -  ``sudo chkconfig nginx on``

4. Verify NGINX is running

   -  ``curl http://10.10.10.3``
   -  You should see a *Welcome to NGINX!* page

**What to do next**

1. Map a fully qualified domain name (FQDN) such as ``mattermost.example.com`` to point to the NGINX server.
2. Configure NGINX to proxy connections from the internet to the Mattermost Server.
