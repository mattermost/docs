Set up NGINX with SSL (Recommended)
===================================

1. You can use a free and an open certificate security like let's
   encrypt, this is how to proceed

-  ``sudo apt-get install git``
-  ``git clone https://github.com/letsencrypt/letsencrypt``
-  ``cd letsencrypt``

2. Be sure that the port 80 is not use by stopping NGINX

-  ``sudo service nginx stop``
-  ``netstat -na | grep ':80.*LISTEN'``
-  ``./letsencrypt-auto certonly --standalone``

3. This command will download packages and run the instance, after that
   you will have to give your domain name
4. You can find your certificate in ``/etc/letsencrypt/live``
5. Modify the file at ``/etc/nginx/sites-available/mattermost`` and add
   the following lines:

  ::

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
       listen 443 ssl;
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


6. Be sure to restart NGINX
  * ``\ sudo service nginx start``
7. Add the following line to cron so the cert will renew every month
  * ``crontab -e``
  * ``@monthly /home/ubuntu/letsencrypt/letsencrypt-auto certonly --reinstall --nginx -d yourdomainname && sudo service nginx reload``
8. Check that your SSL certificate is set up correctly
  * Test the SSL certificate by visiting a site such as `https://www.ssllabs.com/ssltest/index.html <https://www.ssllabs.com/ssltest/index.html>`_
  * If there’s an error about the missing chain or certificate path, there is likely an intermediate certificate missing that needs to be included

Setup HTTP2
------------

It is recommended to enable HTTP2 for enhanced performance. 

1. Modify your NGINX configuration as above. Then,

  - Change the line ``listen 443 ssl;`` to ``listen 443 ssl http2;``
  - Change the line ``proxy_pass http://10.10.10.2:8065;`` to ``proxy_pass https://10.10.10.2:8065;``
  
2. Restart NGINX
