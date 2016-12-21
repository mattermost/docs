.. _config-ssl-http2-nginx:

Configuring NGINX with SSL and HTTP/2
=====================================

Using SSL gives greater security by ensuring that communications between Mattermost clients and the Mattermost server are encrypted. It also allows you to configure NGINX to use the HTTP/2 protocol.

Although you can configure HTTP/2 without SSL, both Firefox and Chrome browsers support HTTP/2 on secure connections only.

You can use any certificate that you want, but these instructions show you how to download and install certificates from *Let's Encrypt*.

**To configure SSL and HTTP/2:**

1. Log into the server that hosts NGINX and open a terminal window.
2. Install git.

  - If you are using Ubuntu or Debian:  ``sudo apt-get install git``
  - If you are using RHEL: ``sudo yum install git``

3. Clone the Let's Encrypt repository on GitHub.

  ``git clone https://github.com/letsencrypt/letsencrypt``

4. Change to the ``letsencrypt`` directory.

  ``cd letsencrypt``

5. Stop NGINX.

  On Ubuntu 14.04 and RHEL 6.6:
  
  ``sudo service nginx stop``
  
  On Ubuntu 16.04 and RHEL 7.1:
  
  ``sudo systemctl stop nginx``

6. Run ``netstat`` to make sure that nothing is listening on port 80.

  ``netstat -na | grep ':80.*LISTEN'``

7. Run the Let's Encrypt installer.

  ``./letsencrypt-auto certonly --standalone``

  When prompted, enter your domain name. The certificate is located in  ``/etc/letsencrypt/live``

8. Open the file ``/etc/nginx/sites-available/mattermost`` as root in a text editor and update the *server* section to incorporate the highlighted lines in the following sample. Make sure to replace {domain-name} with your own domain name, in 2 places.

  .. code-block:: none
    :emphasize-lines: 5,9-16

    . 
    .
    .
    server {
      listen 443 ssl http2;
    .
    .
    .
      ssl on;
      ssl_certificate /etc/letsencrypt/live/{domain-name}/fullchain.pem;
      ssl_certificate_key /etc/letsencrypt/live/{domain-name}/privkey.pem;
      ssl_session_timeout 5m;
      ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
      ssl_ciphers 'EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH';
      ssl_prefer_server_ciphers on;
      ssl_session_cache shared:SSL:10m;
    .
    .
    .
    }

9. Restart NGINX

  On Ubuntu 14.04 and RHEL 6.6:
  
  ``sudo service nginx start``
  
  On Ubuntu 16.04 and RHEL 7.1:
  
  ``sudo systemctl start nginx``

10. Check that your SSL certificate is set up correctly.

  * Test the SSL certificate by visiting a site such as https://www.ssllabs.com/ssltest/index.html
  * If there’s an error about the missing chain or certificate path, there is likely an intermediate certificate missing that needs to be included.

11. Configure ``cron`` so that the certificate will automatically renew every month.

  ``crontab -e``
  
  In the following line, use your domain name in place of *{domain-name}*
  
  ``@monthly /home/ubuntu/letsencrypt/letsencrypt-auto certonly --reinstall --nginx -d {domain-name} && sudo service nginx reload``
