SSL Client Certificate Setup (Beta)
===================================

Follow these steps to configure SSL client certificates for your browser and the Mattermost Desktop Apps on Windows, Mac and Linux. SSL client certificates are not yet supported on the Mattermost mobile apps.

Before you begin, follow the `official guides to install Mattermost <https://docs.mattermost.com/guides/administrator.html#installing-mattermost>`__ on your system, including NGINX configuration as a proxy with SSL and HTTP/2, and a valid SSL certificate such as Let's Encrypt.

For the purposes of this guide, the Mattermost server domain name is ``example.mattermost.com``, and the user account is ``mmuser`` with email ``mmuser@mattermost.com`` and password ``mmuser-password``.

.. note::
  Generating the client certificates in this section is optional if you have already generated them before.

Set up mutual TLS authentication for the Web App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create a `certificate authority (CA) key <https://en.wikipedia.org/wiki/Certificate_authority>`__ and a certificate for signing the client certificate. When establishing a TLS connection, the NGINX proxy server requests and validates a client certificate provided by the web app.

.. code-block:: none

  openssl genrsa -des3 -out ca.mattermost.key 4096
  
  pass phrase: capassword

    
.. code-block:: none

  openssl req -new -x509 -days 365 -key ca.mattermost.key -out ca.mattermost.crt

  Country Name: US
  State: Maryland
  Locality Name: Meade
  Organization Name: Mattermost
  Organization Unit: Smarttotem
  Common Name: example.mattermost.com
  Email Address: admin@mattermost.com

2. Create the client side key for ``mmuser`` with a passphrase, and the certificate signing request:

.. code-block:: none

  openssl genrsa -des3 -out mmuser-mattermost.key 1024

  passphrase: mmuser-passphrase

.. code-block:: none

  openssl req -new -key mmuser-mattermost.key -out mmuser-mattermost.csr

  Country Name: US
  State: Maryland
  Locality Name: Meade
  Organization Name: Mattermost
  Organization Unit: Smarttotem
  Common Name: mmuser
  Email Address: mmuser@mattermost.com
  
  Challenge password: mmuser-passphrase

3. Sign the user's client certificate with the previously created CA certificate:

.. code-block:: none

  openssl x509 -req -days 365 -in mmuser-mattermost.csr -CA ca.mattermost.crt -CAkey ca.mattermost.key -set_serial 01 -out mmuser-mattermost.crt

4. Check the newly generated client certificate for ``mmuser``:

.. code-block:: none

  openssl x509 -in mmuser-mattermost.crt -text -noout

5. Open the file ``/etc/nginx/sites-available/mattermost`` and modify the following lines, so that the NGINX proxy server requests and verifies the client certificate:

.. code-block:: none
  :emphasize-lines: 4-5, 10-11, 16-17

  ssl on;
  ssl_certificate /etc/letsencrypt/live/example.mattermost.com/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/example.mattermost.com/privkey.pem;
  ssl_client_certificate /opt/mattermost/config/ca.mattermost.crt;
  ssl_verify_client on;

  ...

  location ~ /api/v[0-9]+/(users/)?websocket$ {
   proxy_set_header X-SSL-Client-Cert $ssl_client_cert;
   proxy_set_header X-SSL-Client-Cert-Subject-DN $ssl_client_s_dn;
     
  ...

  location / {
   proxy_set_header X-SSL-Client-Cert $ssl_client_cert;
   proxy_set_header X-SSL-Client-Cert-Subject-DN $ssl_client_s_dn;
 
  ...

6. Confirm the CA key for ``mmuser`` works by the following curl command to the proxy:

.. code-block:: none

  curl -v -s -k --key mmuser-mattermost.key --cert mmuser-mattermost.crt:mmuser-passphrase https://example.mattermost.com

You should see the Mattermost login page. If you see:

 - ``No required SSL certificate was sent``, something went wrong. Review the above steps and try again.
 - ``Error reading X.509 key or certificate file: Decryption has failed.``, make sure the passphrase is included together with the certificate, because curl doesn't prompt for it separately. 

7. Generate a PKCS12 file from the CA key and certificate, to install the certificate into your client machine for your browser to use:

.. code-block:: none

  openssl pkcs12 -export -out mmuser-mattermost.p12 -inkey mmuser-mattermost.key -in mmuser-mattermost.crt -certfile ca.mattermost.crt

  Enter Export Password: mmuser-passphrase

8. Repeat steps 2-7 above for other users as needed.

9. Import the generated .p12 file in step 7 into your key chain. In the Chrome browser on macOS:

  1. Go to **Settings > Advanced > Privacy and security > Manage certificates**. This opens the Keychain Access app.
  2. Go to **File > Import Items** and select the ``mmuser-mattermost.p12`` file.

10. Go to https://example.mattermost.com. You should see a popup for the client certificate request.

Troubleshooting
~~~~~~~~~~~~~~~~

`Follow this process <https://mattermost.org/troubleshoot/>`__ to resolve configuration issues and to ask for help.
