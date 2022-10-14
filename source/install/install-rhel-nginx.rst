:nosearch:

.. This page is intentionally not accessible via the LHS navigation pane because it's common content included on other docs pages.

.. _install-rhel-nginx:

Install NGINX server
---------------------

In a production setting, use a proxy server for greater security and performance of Mattermost:

  -  SSL termination
  -  HTTP to HTTPS redirect
  -  Port mapping ``:80`` to ``:8065``
  -  Standard request logs

1. Log in to the server that will host the proxy, and open a terminal window.

2. Create the file ``/etc/yum.repos.d/nginx.repo`` by running ``sudo touch /etc/yum.repos.d/nginx.repo``.

  If you are on RHEL 8 you can skip to **Step 4. Install NGINX**.

3. Open the file as *root* in a text editor and add the following contents, where *{version}* is **7** for RHEL 7:

  .. code-block:: none
  
    [nginx]
    name=nginx repo
    baseurl=https://nginx.org/packages/rhel/{version}/$basearch/
    gpgcheck=0
    enabled=1

4. Install NGINX by running ``sudo yum install nginx.x86_64``.

5. After the installation is complete, start NGINX by running ``sudo systemctl start nginx``.
    On RHEL 6:
  
6. **Optional** Set NGINX to start at system boot by running ``sudo systemctl enable nginx``.

7. Verify that NGINX is running by running ``curl http://localhost``.
  
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

1. Map a fully qualified domain name (FQDN) such as ``mattermost.example.com`` on your DNS server/service, to point to the NGINX server.
2. Configure NGINX to proxy connections from the Internet to the Mattermost Server.
