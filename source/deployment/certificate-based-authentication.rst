Certificate-Based Authentication (E20)
=======================================

Certificate-based authentication (CBA) can be used identify a user or a device before granting access to Mattermost, providing an additional layer of security to access the system.

Enterprise Edition E20 supports device CBA with client side certificates through SAML 2.0 SSO and mutual TLS authentication at the NGINX proxy level. Additional configuration is required for user CBA.

Follow these steps to configure user CBA for your browser, Mattermost Desktop Apps, and the Mattermost iOS App. Before you begin, follow the `official guides to install Mattermost <https://docs.mattermost.com/guides/administrator.html#installing-mattermost>`_ on your system, including NGINX configuration as a proxy with SSL and HTTP/2, and a valid Let's Encrypt certificate.

.. contents::
  :backlinks: top
  :local:
  :depth: 2

Run a custom build of the Mattermost server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Fork the `mm-cba-proto <https://github.com/mattermost/mattermost-server/tree/mm-cba-proto>`_ branch from the mattermost-server repository.
2. `Use this guide <https://docs.mattermost.com/developer/dev-setup.html>`_ to create a custom build of the server based on the branch from step 1.

With this custom build, the Mattermost server can be used to log in with a client side certifiate supplied as part of mutual TLS authentication from above. This guide has made some simple assumptions about how the certificates map to Mattermost users.

Set up mutual TLS authentication for the Web App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enterprise Edition E20 supports device CBA with client side certificates through SAML 2.0 SSO and mutual TLS authentication at the NGINX proxy level. Many SAML service providers support certificate authentication, such as `ADFS and Azure AD <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-user-certificate-authentication>`_.

In addition to thes steps for the Mattermost Web App and the Desktop Apps, more information about setting up mutual TLS authentication `can be found here <https://blog.codeship.com/how-to-set-up-mutual-tls-authentication/>`_.

.. note::
  For the purposes of this guide, the Mattermost server domain name is example.mattermost.com, and the user account is ``mmuser`` with email ``mmuser@mattermost.com`` and password ``mmuser-password``.

1. Create a `certificate authority (CA) key <https://en.wikipedia.org/wiki/Certificate_authority>`_ and a certificate for signing the client certificate. When establishing a TLS connection, the NGINX proxy server requests and validates a client certificate provided by the web app.

.. code-block::

  openssl genrsa -des3 -out ca.mattermost.key 4096

  pass phrase: capassword

.. code-block::

  openssl req -new -x509 -days 365 -key ca.mattermost.key -out ca.mattermost.crt

  Country Name: US
  State: Maryland
  Locality Name: Meade
  Organization Name: Mattermost
  Organization Unit: Smarttotem
  Common Name: example.mattermost.com
  Email Address: admin@mattermost.com

2. Create the client side key for ``mmuser`` with a passphrase, and the certificate signing request:

.. code-block::

  openssl genrsa -des3 -out mmuser-mattermost.key 1024

  passphrase: mmuser-passphrase

.. code-block::

  openssl req -new -key mmuser-mattermost.key -out mmuser-mattermost.csr

  Country Name: US
  State: Maryland
  Locality Name: Meade
  Organization Name: Mattermost
  Organization Unit: Smarttotem
  Common Name: mmuser
  Email Address: mmuser@mattermost.com

  Challenge password: mmuser-passphrase

3. Sign the user's client certificate with the previously created CA certificate.

.. code-block::

  openssl x509 -req -days 365 -in mmuser-mattermost.csr -CA ca.mattermost.crt -CAkey ca.mattermost.key -set_serial 01 -out mmuser-mattermost.crt


4. Check the newly generated client certificate for ``mmuser``

.. code-block::

  openssl x509 -in mmuser-mattermost.crt -text -noout

5. Open the file ``/etc/nginx/sites-available/mattermost`` and modify the following lines, so that the NGINX proxy server requests and verifies the client certificate:

.. code-block::
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

6. Confirm the CA key for ``mmuser`` works by the following curl command to the proxy

.. code-block::

  curl -v -s -k --key mmuser-mattermost.key --cert mmuser-mattermost.crt:mmuser-passphrase https://example.mattermost.com

You should see the Mattermost login page. If you see:

 - ``No required SSL certificate was sent``, something went wrong. Review the above steps and try again.
 - ``* error reading X.509 key or certificate file: Decryption has failed.``, make sure the passphrase is included together with the certificate, because curl doesn't prompt for it separately. 

7. Generate a PKCS12 file from the CA key and certificate, to install the certificate into your client machine for your browser to use.

.. code-block::

  openssl pkcs12 -export -out mmuser-mattermost.p12 -inkey mmuser-mattermost.key -in mmuser-mattermost.crt -certfile ca.mattermost.crt

  Enter Export Password: mmuser-passphrase

8. Repeat steps 2-7 above for other users as needed.

9. Import the generated .p12 file in step 7 into your key chain. In the Chrome browser on macOS:

		1. Go to **Settings > Advanced > Privacy and security > Manage certificates**. This opens the Keychain Access app.
		2. Go to **File > Import Items** and select the ``mmuser-mattermost.p12`` file.

10. Go to https://example.mattermost.com. You should see a popup for the client certifcate request.

Set up Mattermost server to log in with a client certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. In ``ExperimentalSettings`` of the ``config.json`` file, set ``ClientSideCertEnable`` to ``true`` and ``ClientSideCertCheck`` to one of the following values:

- ``primary`` - After the client side certificate is verified, user's email is retrieved from the certificate and used to log in without a password.
- ``secondary`` - After the client side certificate is verified, user's email is retrieved from the certificate and matched against the one supplied by the user. If they match, the user logs in with regular email/password credentials.

2. Restart the Mattermost server.

On Ubuntu 14.04 and RHEL 6.6:

.. code-block::

  sudo restart mattermost

On Ubuntu 16.04, Debian Jessie, and RHEL 7.1:

.. code-block::

  sudo systemctl restart mattermost

3. Go to https://example.mattermost.com and try to log in. The server should require the x.509 cert to have an ``emailAddress`` equal to the Mattermost user's email.

Set up Purebred sample apps on iOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Clone the sample repos from `https://github.com/Purebred/KeyShareConsumer <https://github.com/Purebred/KeyShareConsumer>`_ and `https://github.com/Purebred/SampleKeyProvider <https://github.com/Purebred/SampleKeyProvider>`_.
2. Replace all ``red.hound`` strings with ``com.mattermost``.
3. Open the KeyShareConsumer and SampleKeyProvider apps. Go to **Project settings > Target > ...**

    - Verify all the bundle indentifiers are renamed to ``com.mattermost`.
    - Select **Mattermost Team** for the signing profile.

.. note::
  A real iOS device is required to run the sample apps, since some of the libraries do not target ``x86_amd64``.

4. Run both apps on the device and confirm they can interact with each other on the device.
5. Import one of the existing sample keys from the SampleKeyProvider app to KeyShareConsumer app.
6. If the import succeeds, then import the ``mmuser-mattermost.p12`` certificate into the SampleKeyProvider app.
7. Modify ``ViewController.m`` by adding the following:

.. code-block::

  NSURL* fifth = [NSURL URLWithString:[[NSBundle mainBundle] pathForResource:@"mmuser-mattermost" ofType:@"p12"]];
  OSStatus stat5 = [Pkcs12ViewController importP12:fifth password:@"mmuser-passphrase" deleteAfterImport:false];
    
  if(0 == stat1 && 0 == stat2 && 0 == stat3 && 0 == stat4 && 0 == stat5)
  {

9. Rerun the sample, and import the new key ``mmuser-mattermost.p12`` which appears as ``mmuser``. Confirm everything works with the sample apps.

Run the modified Mattermost React Native Mobile App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Fork the `cba <https://github.com/mattermost/mattermost-mobile/blob/cba>`_ branch from the mattermost-mobile repository.
2. Set **ExperimentalClientSideCertEnable** to ``true`` in the `mattermost-mobile/assets/base/config.json <https://github.com/mattermost/mattermost-mobile/blob/cba/assets/base/config.json#L15>`_ file.
3. `Use this guide <https://docs.mattermost.com/mobile/mobile-compile-yourself.html>`_ to build the apps based on the branch you created and modified in steps 1 and 2.
4. Import the certificate from the previous section above into the Mattermost iOS App and use it for mutual TLS authentication. You can `watch a demonstration video of this step here <https://drive.google.com/file/d/1zzk9XQ6RBvsWbCTrIfgE0484pD7w9Ux1/view>`_.
5. A user account is created automatically on first use, and the login credentials for email/password are bypassed with a button to sign in with the client-side certificate instead.
