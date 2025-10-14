Certificate-based authentication (Experimental)
===============================================

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

.. important::
  **Experimental certificate-based authentication has been deprecated from Mattermost v11.0.** From Mattermost v11, you must :ref:`disable this feature <administration-guide/configure/experimental-configuration-settings:enable client-side certification>` to start the server. Enabling this setting will prevent the server from starting.

Prior to v11, certificate-based authentication (CBA) is available as an experimental feature to identify a user or a device before granting access to Mattermost and provide an additional layer of security to access the system.

Before you begin, follow the :doc:`official guides to install Mattermost </deployment-guide/deployment-guide-index>` on your system, including NGINX configuration as a proxy with SSL and HTTP/2, and a valid SSL certificate such as Let's Encrypt.

Then, follow the steps below to configure user CBA for your browser and Mattermost Desktop Apps. You can manage certificate distribution for each personal device (BYOD) and their life cycle management with a service like `OpenSSL <https://www.openssl.org/>`__.

Set up mutual TLS authentication for the Web App
-------------------------------------------------

:doc:`Setting up mutual TLS authentication </administration-guide/onboard/ssl-client-certificate>` is the first step to set up certificate-based authentication. 

Set up Mattermost server to log in with a client certificate
--------------------------------------------------------------

1. Make sure your Mattermost server is licensed with a valid Enterprise license.
2. In ``ExperimentalSettings`` of the ``config.json`` file, set ``ClientSideCertEnable`` to ``true`` and ``ClientSideCertCheck`` to one of the following values:

- ``primary`` - After the client side certificate is verified, user's email is retrieved from the certificate and is used to log in without a password.
- ``secondary`` - After the client side certificate is verified, user's email is retrieved from the certificate and matched against the one supplied by the user. 

If they match, the user logs in with regular email/password credentials.

The ``config.json`` file should then have the following lines

.. code-block:: text

  "ExperimentalSettings": {
      "ClientSideCertEnable": true,
      "ClientSideCertCheck": "secondary"
  },

3. Restart the Mattermost server.

4. Go to ``https://example.mattermost.com`` and try to log in. The server should require the x.509 cert to have an ``emailAddress`` equal to the Mattermost user's email.
