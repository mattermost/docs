.. _config-ssl-http2-nginx:

Configuring NGINX with SSL and HTTP/2
=====================================

Using SSL gives greater security by ensuring that communications between Mattermost clients and the Mattermost server are encrypted. It also allows you to configure NGINX to use the HTTP/2 protocol.

Although you can configure HTTP/2 without SSL, both Firefox and Chrome browsers support HTTP/2 on secure connections only.

You can use any certificate that you want, but these instructions show you how to download and install certificates from *Let's Encrypt*.

1. Log into the server that hosts NGINX and open a terminal window.
2. Install git.

  - If you are using Ubuntu or Debian:  ``sudo apt-get install git``
  - If you are using RHEL: ``sudo yum install git``

3. Clone the Let's Encrypt repository on GitHub.

  ``git clone https://github.com/letsencrypt/letsencrypt``

4. Change to the ``letsencrypt`` directory.

  ``cd letsencrypt``

5. Stop NGINX.

  ``sudo service nginx stop``

6. Run ``netstat`` to make sure that nothing is listening on port 80.

  ``netstat -na | grep ':80.*LISTEN'``

7. Run the Let's Encrypt installer.

  ``./letsencrypt-auto certonly --standalone``

  When prompted, enter your domain name. The certificate is located in  ``/etc/letsencrypt/live``

8. Open the file ``/etc/nginx/sites-available/mattermost`` as root and update it to incorporate the following lines. Make sure that you use your own values for the Mattermost server IP address and FQDN for *server_name*.

  .. code-block:: none

    upstream backend {
        server 10.10.10.2:8065;
    }

    server {
       listen         80;
       server_name    mattermost.example.com;
       return         301 https://$server_name$request_uri;
    }

    proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=mattermost_cache:10m max_size=3g inactive=120m use_temp_path=off;

    server {
       listen 443 ssl http2;
       server_name mattermost.example.com;

       ssl on;
       ssl_certificate /etc/letsencrypt/live/yourdomainname/fullchain.pem;
       ssl_certificate_key /etc/letsencrypt/live/yourdomainname/privkey.pem;
       ssl_session_timeout 5m;
       ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
       ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';
       ssl_prefer_server_ciphers on;
       ssl_session_cache shared:SSL:10m;

       location /api/v3/users/websocket {
          proxy_set_header Upgrade $http_upgrade;
          proxy_set_header Connection "upgrade";
          proxy_set_header X-Forwarded-Ssl on;
          client_max_body_size 50M;
          proxy_set_header Host $http_host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header X-Forwarded-Proto $scheme;
          proxy_set_header X-Frame-Options SAMEORIGIN;
          proxy_buffers 256 16k;
          proxy_buffer_size 16k;
          proxy_read_timeout 600s;
          proxy_pass http://backend;
       }

       location / {
          proxy_set_header X-Forwarded-Ssl on;
          client_max_body_size 50M;
          proxy_set_header Connection "";
          proxy_set_header Host $http_host;
          proxy_set_header X-Real-IP $remote_addr;
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header X-Forwarded-Proto $scheme;
          proxy_set_header X-Frame-Options SAMEORIGIN;
          proxy_buffers 256 16k;
          proxy_buffer_size 16k;
          proxy_read_timeout 600s;
          proxy_cache mattermost_cache;
          proxy_cache_revalidate on;
          proxy_cache_min_uses 2;
          proxy_cache_use_stale timeout;
          proxy_cache_lock on;
          proxy_pass http://backend;
        }
    }


9. Restart NGINX

  ``sudo service nginx start``

10. Check that your SSL certificate is set up correctly.

  * Test the SSL certificate by visiting a site such as https://www.ssllabs.com/ssltest/index.html
  * If there’s an error about the missing chain or certificate path, there is likely an intermediate certificate missing that needs to be included.

11. Configure ``cron`` so that the certificate will automatically renew every month.

  ``crontab -e``
  
  In the following line, use your domain name in place of *<domain-name>*
  
  ``@monthly /home/ubuntu/letsencrypt/letsencrypt-auto certonly --reinstall --nginx -d <domain-name> && sudo service nginx reload``
