.. _config-ssl-http2-nginx:

Configuring HAProxy with SSL and HTTP/2
=====================================

Using SSL gives greater security by ensuring that communications between Mattermost clients and the Mattermost server are encrypted. It also allows you to configure HAProxy to use the HTTP/2 protocol.

Although you can configure HTTP/2 without SSL, both Firefox and Chrome browsers support HTTP/2 on secure connections only.

You can use any certificate that you want, but these instructions show you how to download and install certificates from `Let's Encrypt <https://letsencrypt.org/>`_, a free certificate authority.

**To configure SSL and HTTP/2:**

1. Log in to the server that hosts HAProxy and open a terminal window.
2. Install git.

  If you are using Ubuntu or Debian:

  ``sudo apt-get install git``

  If you are using RHEL:

  ``sudo yum install git``

3. Clone the Let's Encrypt repository on GitHub.

  ``git clone https://github.com/letsencrypt/letsencrypt``

4. Change to the ``letsencrypt`` directory.

  ``cd letsencrypt``

5. Stop HAProxy.

  On Ubuntu 14.04 and RHEL 6.6:

  ``sudo service haproxy stop``

  On Ubuntu 16.04 and RHEL 7.1:

  ``sudo systemctl stop haproxy``

6. Run ``netstat`` to make sure that nothing is listening on port 80.

  ``netstat -na | grep ':80.*LISTEN'``

7. Run the Let's Encrypt installer.

  ``./letsencrypt-auto certonly --standalone``

  When prompted, enter your domain name. After the installation is complete, you can find the certificate in the   ``/etc/letsencrypt/live`` directory.

8. Open the file ``/etc/haproxy/haproxy.cfg`` as root in a text editor and update the *server* section to incorporate the highlighted lines in the following sample. Make sure to replace *{domain-name}* with your own domain name, in 2 places.

  .. code-block:: none
    :emphasize-lines: 6-10, 13, 15-23, 33

    .
    .
    .
    frontend www-http
    redirect scheme https code 301 if !{ ssl_fc }
    
    frontend www-https
    bind *:443 ssl crt /etc/haproxy/certs/{domain-name}/{domain-name}.pem
    default_backend mattermost

9. Restart HAProxy.

  On Ubuntu 14.04 and RHEL 6.6:

  ``sudo service haproxy start``

  On Ubuntu 16.04 and RHEL 7.1:

  ``sudo systemctl start haproxy``

10. Check that your SSL certificate is set up correctly.

  * Test the SSL certificate by visiting a site such as https://www.ssllabs.com/ssltest/index.html
  * If there’s an error about the missing chain or certificate path, there is likely an intermediate certificate missing that needs to be included.

11. Configure a Let's Encrypt backend

  .. code-block:: none
  
    backend letsencrypt
    server 127.0.0.1:54321
    
12. Restart HAProxy.

  On Ubuntu 14.04 and RHEL 6.6:

  ``sudo service haproxy start``

  On Ubuntu 16.04 and RHEL 7.1:

  ``sudo systemctl start haproxy``
  
13. Open the file ``/etc/letsencrypt/renewal/{domain-name}.conf`` as root in a text editor and update the ``http01_port`` section to incorporate the highlighted lines in the following sample.

  .. code-block:: none
  
    http01_port = 54321
    
    Run a ``--dry-run`` so we don't actually renew anything
    
    ``sudo certbot renew --dry-run``

14. Create a script called ``renew.sh`` to renew and generate a ``.pem`` for HAProxy.

  In the following script, use your own domain name in place of *{domain-name}*
  
  .. code-block:: none
  
    SITE={domain-name}
    
    # move to the correct let's encrypt directory
    cd /etc/letsencrypt/live/$SITE
    
    # cat files to make combined .pem for haproxy
    cat fullchain.pem privkey.pem > /etc/haproxy/certs/$SITE.pem
    
    #reload haproxy
    service haproxy reload
    
  Make the script executable
  
    ``sudo chmod u+x /usr/local/bin/renew.sh``
    
15. Configure ``cron`` so that the certificate will automatically renew every month.
  
  ``crontab -e``

  In the following line, use your own domain name in place of *{domain-name}*

  ``@monthly /usr/bin/certbot renew --renew-hook "/usr/local/bin/renew.sh" >> /var/log/haproxy/cert-renewal.log``
