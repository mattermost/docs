Configuring proxy to Mattermost transport encryption
====================================================

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

Mattermost is able to encrypt the traffic between the proxy and the application server using TLS.

Prerequisites
-------------

- Operational Mattermost server or cluster.
- Authentication credentials for Mattermost user on application server.

Example environment
-------------------

In this scenario there is one Mattermost application server and one NGINX server, both running Ubuntu 20.04, with the following IPs:

- **transport-encryption-mattermost1:** 10.10.250.146
- **transport-encryption-nginx:** 10.10.250.107

Configuring NGINX
-----------------

On the NGINX server, connect to both servers with a sudo or root user. Open the Mattermost proxy configuration and search for the following line twice:

.. code-block:: text

  proxy_pass http://backend;

Change the protocol from ``http`` to ``https``:

.. code-block:: text

  proxy_pass https://backend;

Afterwards do not reload the NGINX server yet to minimize the downtime of the service.

Configuring Mattermost
----------------------

On the Mattermost server, change to the config directory of Mattermost and generate a self-signed certificate that will be used to encrypt the traffic between the proxy server and the application server.

**Note:** Alternatively you can sign a certificate from your company's CA.

.. code-block:: sh

  cd /opt/mattermost/config
  openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
  chown root:mattermost *.pem
  chmod 640 *.pem


Once complete, open the file ``config.json`` and modify the values ``ConnectionSecurity``, ``TLSCertFile`` and ``TLSKeyFile`` in the ``ServiceSettings`` section.

**Before**

.. code-block:: json

  {
      "ServiceSettings": {
          "SiteURL": "https://transport-encryption.dev.example.com",
          "WebsocketURL": "",
          "LicenseFileLocation": "",
          "ListenAddress": ":8065",
          "ConnectionSecurity": "",
          "TLSCertFile": "",
          "TLSKeyFile": "",
          "...":"..."
      },
      "...":"..."
  }


**After**

.. code-block:: json

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
      "...":"..."
  }


Restart the Mattermost server and ensure it's up and running:

.. code-block:: sh

  sudo systemctl restart mattermost
  systemctl status mattermost

.. code-block:: text

  ● mattermost.service - Mattermost
     Loaded: loaded (/lib/systemd/system/mattermost.service; static; vendor preset: enabled)
     Active: active (running) since Mon 2019-10-28 16:45:29 UTC; 1h 15min ago
     [...]

Finally, on the **NGINX server**, reload the configuration to ensure that requests are sent on HTTPS:

.. code-block:: sh

  sudo systemctl reload nginx
