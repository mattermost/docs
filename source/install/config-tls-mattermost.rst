Configuring TLS on Mattermost Server
====================================

You have two options if you want users to connect with HTTPS:

  1. Set up TLS on Mattermost Server.
  2. Install a proxy such as NGINX and set up TLS on the proxy.

The easiest option is to set up TLS on the Mattermost Server, but if you expect to have more than 200 users, use a proxy for better performance. A proxy server also provides standard HTTP request logs.

.. note::
   Your Mattermost server must be accessible from the Let's Encrypt CA in order to verify your domain name and issue the certificate. Be sure to open your firewall and configure any reverse proxies to forward traffic to ports 80 and 443. More information can be found `at Let's Encrypt <https://letsencrypt.org/how-it-works/>`_.

**Configure TLS on the Mattermost Server**:

1. In **System Console > Environment > Web Server** (or **System Console > General > Configuration** in versions prior to 5.12).
  a. Change the **Listen Address** setting to ``:443``.
  b. Change the **Connection Security** setting to ``TLS``.
  c. Change the **Forward port 80 to 443** setting to ``true``.
2. Activate the ``CAP_NET_BIND_SERVICE`` capability to allow Mattermost to bind to low ports.

  ``sudo setcap cap_net_bind_service=+ep /opt/mattermost/bin/mattermost``

3. Install the security certificate. You can use `Let's Encrypt <https://letsencrypt.org/>`__ to automatically install and setup the certificate, or you can specify your own certificate.

  **To use a Let's Encrypt certificate**:

    The certificate is retrieved the first time that a client tries to connect to the Mattermost server. Certificates are retrieved for any hostname a client tries to reach the server at.

    a. Change the **Use Let's Encrypt** setting to ``true``.
    b. Restart the Mattermost server for these changes to take effect.

.. note::
   If Let's Encrypt is enabled, forward port 80 through a firewall, with `Forward80To443 <https://docs.mattermost.com/administration/config-settings.html#forward-port-80-to-443>`__ ``config.json`` setting set to ``true`` to complete the Let's Encrypt certification.

**To use your own certificate**:

    a. Change the **Use Let's Encrypt** setting to ``false``.
    b. Change the **TLS Certificate File** setting to the location of the certificate file.
    c. Change the **TLS Key File** setting to the location of the private key file.
    d. Restart the Mattermost server for these changes to take effect.

.. note::
   Password-protected certificates are not supported.
