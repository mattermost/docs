Certificate-based authentication (Experimental)
===============================================

.. include:: ../../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

.. important::
   This feature has been removed in Mattermost server v11.0. If you're running Mattermost v11.0 or later, certificate-based authentication is no longer available. The configuration settings ``ClientSideCertEnable`` and ``ClientSideCertCheck`` have been removed, and attempting to enable them will prevent the server from starting.

   For users on Mattermost v10.12 and earlier, this documentation is maintained for reference purposes only.

Certificate-based authentication (CBA) was available as an experimental feature to identify a user or a device before granting access to Mattermost and provide an additional layer of security to access the system.

The following steps describe how to configure user CBA for your browser and Mattermost Desktop Apps on Mattermost v10.12 and earlier versions. Support for the Mattermost iOS and Android Apps was planned but never implemented before the feature's removal. It is expected that you can manage certificate distribution for each personal device (BYOD) and their life cycle management with a service like `OpenSSL <https://www.openssl.org/>`__.

Before you begin, follow the :doc:`official guides to install Mattermost </deployment-guide/deployment-guide-index>` on your system, including NGINX configuration as a proxy with SSL and HTTP/2, and a valid SSL certificate such as Let's Encrypt.

Set up mutual TLS authentication for the Web App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the first step for setting up certificate-based authentication. If you haven't set up mutual TLS authentication yet, :doc:`see our documentation to learn more </administration-guide/onboard/ssl-client-certificate>`.

Set up Mattermost server to log in with a client certificate (Mattermost v10.12 and earlier)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Make sure your Mattermost server is licensed with a valid Enterprise license.
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

.. code-block:: sh

  sudo restart mattermost

On Ubuntu 16.04, Debian Stretch, and RHEL 7:

.. code-block:: sh

  sudo systemctl restart mattermost

4. Go to ``https://example.mattermost.com`` and try to log in. The server should require the x.509 cert to have an ``emailAddress`` equal to the Mattermost user's email.
