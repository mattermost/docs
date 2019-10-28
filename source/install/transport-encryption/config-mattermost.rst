=============================================
Configuring Proxy to Mattermost Transport Encryption
=============================================

Mattermost is able to encrypt the traffic between the proxy and the application
server using TLS.

**Prerequisites:**

- Mattermost server or cluster operational
- Authentication credentials for Mattermost user on application server

Example Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In this scenario there is 1 Mattermost application server and one NGINX server,
both running Ubuntu 18.04, with the following IPs:

- **transport-encryption-mattermost1:** 10.10.250.146
- **transport-encryption-nginx:** 10.10.250.107

Preparations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Connect to both servers with a sudo or root user

NGINX Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
On the NGINX server, open the Mattermost proxy configuration (Refer to - `Configuring NGINX with SSL and HTTP/2 (End-User - Proxy) </install/install-rhel-6.html#configuring-nginx-with-ssl-and-http-2>`__ for additional information)
and search for the following line twice:

.. code-block:: none

  proxy_pass http://backend;

And change the protocol from ``http`` to ``https``:

.. code-block:: none

  proxy_pass https://backend;

Afterwards do not reload the NGINX server yet to minimize the downtime of the service.

Mattermost Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
On the Mattermost server, change to the config directory of Mattermost and generate a self-signed certificate
that will be used to encrypt the traffic between the proxy server and the application server.

**Note:** As an alternative, sign a certificate from your companies CA.

.. code-block:: none

  $ cd /opt/mattermost/config
  $ openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
  $ chown root:mattermost *.pem
  $ chmod 640 *.pem


Afterwards open the file ``config.json`` and modify the values ``ConnectionSecurity``,
``TLSCertFile`` and ``TLSKeyFile`` in the ``ServiceSettings`` section.

**Before:**

.. codeblock:: json

{
    "ServiceSettings": {
        "SiteURL": "https://transport-encryption.dev.example.com",
        "WebsocketURL": "",
        "LicenseFileLocation": "",
        "ListenAddress": ":8065",
        "ConnectionSecurity": "",
        "TLSCertFile": "",
        "TLSKeyFile": "",

**After:**

.. codeblock:: json

{
    "ServiceSettings": {
        "SiteURL": "https://transport-encryption.dev.example.com",
        "WebsocketURL": "",
        "LicenseFileLocation": "",
        "ListenAddress": ":8065",
        "ConnectionSecurity": "TLS",
        "TLSCertFile": "/opt/mattermost/config/cert.pem",
        "TLSKeyFile": "/opt/mattermost/config/key.pem",
        "...":"..."
    },


Afterwards, restart the Mattermost server and ensure it's up and running:

.. code-block:: none

  $ sudo systemctl restart mattermost
  $ systemctl status mattermost
  ● mattermost.service - Mattermost
     Loaded: loaded (/lib/systemd/system/mattermost.service; static; vendor preset: enabled)
     Active: active (running) since Mon 2019-10-28 16:45:29 UTC; 1h 15min ago
     [...]

Finally, on the **NGINX server**, reload the configuration that requests are being
made on HTTPS:

.. code-block:: none

  $ sudo systemctl reload nginx
