### Apache as reverse proxy
Most of the guides describe on how to use NGINX as a reverse proxy server to
provide an (encrypted) endpoint for Mattermost.

This description is based on a RHEL-7.1 installation, but should be applicable
for other distributions using altered paths for the configuration files. The
steps below can be used a substitute of the nginx setup in the section
[Set up Nginx Server](prod-rhel-7.html#set-up-nginx-server).

## Set Up Apache server
1. For the purposes of this guide we will assume this server has an IP address of `10.10.10.3`
1. We use Apache for proxying request to the Mattermost Server.  The main benefits are:
    * SSL termination
    * HTTP to HTTPS redirect
    * Port mapping :80 to :8065
    * Standard request logs
1. Install Apache on RHEL with
    * ``` sudo yum install httpd```
    * ``` sudo systemctl start httpd```
    * ``` sudo systemctl enable httpd```
1. Verify Apache is running
    * ``` curl http://10.10.10.3```
    * You should see a *Welkom* page
1. Map a FQDN (fully qualified domain name) like **mattermost.example.com** to point to the apache server.
1. Configure apache to proxy connections from the internet to the Mattermost Server
    * Create a configuration file for Mattermost
    * ``` sudo touch /etc/httpd/conf/mattermost.conf```
    * Below is a sample configuration with the minimum settings required to configure Mattermost
    ```
   <VirtualHost _default_:80>
      ServerName mattermost.example.com

      ProxyPreserveHost On
      RewriteEngine     On

      RewriteCond %{REQUEST_URI}  ^/api/v1/websocket      [NC,OR]
      RewriteCond %{HTTP:UPGRADE} ^WebSocket$             [NC,OR]
      RewriteCond %{HTTP:CONNECTION} ^Upgrade$            [NC]
      RewriteRule .* ws://10.10.10.2:8065%{REQUEST_URI}   [P,QSA,L]

      RewriteCond %{DOCUMENT_ROOT}/%{REQUEST_FILENAME}    !-f
      RewriteRule .* http://10.10.10.2:8065%{REQUEST_URI} [P,QSA,L]

      # Be sure to uncomment the next 2 lines if https is used
      # RequestHeader set X-Forwarded-Proto "https"
      # Header set Strict-Transport-Security "max-age=31536000; includeSubDomains"


      # Prevent apache from sending incorrect 304 status updates
      RequestHeader unset If-Modified-Since
      RequestHeader unset If-None-Match

      <Location /api/v1/websocket>
         Require all granted
         ProxyPassReverse ws://10.10.10.2:8065/api/v1/websocket
         ProxyPassReverseCookieDomain 10.10.10.2 mattermost.example.com
      </Location>

      <Location />
         Require all granted
         ProxyPassReverse http://10.10.10.2:8065/
         ProxyPassReverseCookieDomain 10.10.10.2 mattermost.example.com
      </Location>
   </VirtualHost>
    ```
    * Restart apache by typing:
    * ``` sudo systemctl restart httpd```
    * Verify you can see Mattermost thru the proxy by typing:
    * ``` curl http://localhost```
    * You should see a page titles *Mattermost - Signup*
    * **Optional** if you are running selinux on the server, you may need to run ``` sudo setsebool -P httpd_can_network_connect true``` to allow netwerk connections


## Finish Mattermost Server setup
Follow the guide as described in [Production Install on RHEL 7.1+](prod-rhel-7.html).
