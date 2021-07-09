Certificate-Based Authentication (Experimental)
================================================

*Available as an experimental feature in Enterprise Edition E20.*

Certificate-based authentication (CBA) can be used to identify a user or a device before granting access to Mattermost, providing an additional layer of security to access the system.

Follow these steps to configure user CBA for your browser and Mattermost Desktop Apps. Support for the Mattermost iOS and Android Apps is planned. It is expected that you can manage certificate distribution for each personal device (BYOD) and their lifecycle management with a service like `OpenSSL <https://www.openssl.org/>`__.

Before you begin, follow the `official guides to install Mattermost <https://docs.mattermost.com/guides/administrator.html#installing-mattermost>`__ on your system, including NGINX configuration as a proxy with SSL and HTTP/2, and a valid SSL certificate such as Let's Encrypt.

.. contents::
  :backlinks: top
  :local:
  :depth: 2

Set up mutual TLS authentication for the Web App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the first step for setting up certificate-based authentication. If you haven't set up mutual TLS authentication yet, `see our documentation to learn more <https://docs.mattermost.com/deployment/ssl-client-certificate.html>`__.

Set up Mattermost server to log in with a client certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Make sure your Mattermost server is licensed with a valid Enterprise Edition E20 license.
2. In ``ExperimentalSettings`` of the ``config.json`` file, set ``ClientSideCertEnable`` to ``true`` and ``ClientSideCertCheck`` to one of the following values:

- ``primary`` - After the client side certificate is verified, user's email is retrieved from the certificate and is used to log in without a password.
- ``secondary`` - After the client side certificate is verified, user's email is retrieved from the certificate and matched against the one supplied by the user. If they match, the user logs in with regular email/password credentials.

The ``config.json`` file should then have the following lines

.. code-block:: text

  "ExperimentalSettings": {
      "ClientSideCertEnable": true,
      "ClientSideCertCheck": "secondary"
  },

3. Restart the Mattermost server.

On Ubuntu 14.04 and RHEL 6:

.. code-block:: text

  sudo restart mattermost

On Ubuntu 16.04, Debian Stretch, and RHEL 7:

.. code-block:: text

  sudo systemctl restart mattermost

4. Go to ``https://example.mattermost.com`` and try to log in. The server should require the x.509 cert to have an ``emailAddress`` equal to the Mattermost user's email.
