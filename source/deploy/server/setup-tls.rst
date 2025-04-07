(Optional) Set up TLS
======================

You have two options if you want users to connect with HTTPS:

:doc:`Install a proxy such as NGINX </deploy/server/setup-nginx-proxy>` and then `set up TLS on the proxy <#Use-TLS-on-NGINX-as-a-proxy>`__. This is our recommended option if you have a large number of users (more than 200), or if you want to use a reverse proxy for other reasons, such as load balancing or caching. A proxy server delivers better performance and provides standard HTTP request logs.

Alternatively, if you have fewer than 200 users, you can set up TLS on Mattermost server. This is the easiest option when you don't need to use a reverse proxy.

  - You can use `Let's Encrypt <https://letsencrypt.org/>`__ to automatically install and set up the certificate.
  - You can also specify your own certificate.
  - You can use a self-signed certificate, but this is not recommended for production environments.

Configure TLS on the Mattermost server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. In **System Console > Environment > Web Server**:

  a. Change the **Listen Address** setting to ``:443``.
  b. Change the **Connection Security** setting to ``TLS``.
  c. Change the **Forward port 80 to 443** setting to ``true``.

2. Activate the ``CAP_NET_BIND_SERVICE`` capability to allow Mattermost to bind to low ports:

    .. code-block:: sh

       sudo setcap cap_net_bind_service=+ep /opt/mattermost/bin/mattermost

3. Install the security certificate. Use Let's Encrypt to automatically install and setup the certificate, or specify your own certificate.

Use a Let's Encrypt certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The certificate is retrieved the first time that a client tries to connect to the Mattermost server. Certificates are retrieved for any hostname a client tries to reach the server at.

1. Change the **Use Let's Encrypt** setting to ``true``.
2. Restart the Mattermost server for these changes to take effect.

.. note::

  - If Let's Encrypt is enabled, forward port 80 through a firewall, with :ref:`Forward80To443 <configure/environment-configuration-settings:forward port 80 to 443>` ``config.json`` setting set to ``true`` to complete the Let's Encrypt certification.
  - Your Mattermost server must be accessible from the Let's Encrypt CA in order to verify your domain name and issue the certificate. Be sure to open your firewall and configure any reverse proxies to forward traffic to ports 80 and 443. More information can be found `at Let's Encrypt <https://letsencrypt.org/how-it-works/>`_.

Use your own certificate
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Change the **Use Let's Encrypt** setting to ``false``.
2. Change the **TLS Certificate File** setting to the location of the certificate file.
3. Change the **TLS Key File** setting to the location of the private key file.
4. Restart the Mattermost server for these changes to take effect.

.. note::

  Password-protected certificates aren't supported.

Use TLS on NGINX (as a proxy)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

  Do not set up TLS on Mattermost before doing so for NGINX. It breaks the connection as the TLS prevents it from successfully communicating with the Mattermost server.

- NGINX will act as a forward proxy to encrypt the traffic between the client and Mattermost server. After installing the SSL certificate, the incoming traffic will be handled via NGINX on port 443 exposed to the internet, proxy to the Mattermost server running on port 80.
- (Optional) Upstream encryption between NGINX to Mattermost server is allowed.
- Follow `NGINX's guide on setting up SSL Termination for TCP Upstream Servers <https://docs.nginx.com/nginx/admin-guide/security-controls/terminating-ssl-tcp/>`__.

More helpful resources:

- `NGINX's SSL blog <https://www.f5.com/company/blog/nginx/nginx-ssl/>`_
- `NGINX's SSL guide <https://docs.nginx.com/nginx/admin-guide/security-controls/terminating-ssl-http/>`_