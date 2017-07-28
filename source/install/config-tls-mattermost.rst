Configuring TLS on Mattermost Server
====================================

You have two options if you want users to connect with HTTPS: 

  1. Set up TLS on Mattermost Server. 
  2. Install a proxy such as NGINX and set up TLS on the proxy. 

The easiest option is to set up TLS on the Mattermost Server, but if you expect to have more than 200 users, use a proxy for better performance. A proxy server also provides standard HTTP request logs.

**Configure TLS on the Mattermost Server**:

1. In the **System Console** > **General** > **Configuration**.
  a. Change the **Listen Address** setting to ``:443``.
  b. Change the **Connection Security** setting to ``TLS``.
  c. Change the **Forward port 80 to 443** setting to ``true``.
2. Activate the ``CAP_NET_BIND_SERVICE`` capability to allow Mattermost to bind to low ports.

  a. Open a terminal window and change to the Mattermost ``bin`` directory.
    ``cd /opt/mattermost/bin``
  b. Run the following command:
    ``sudo setcap cap_net_bind_service=+ep ./platform``

3. Install the security certificate. You can use `Let's Encrypt <https://letsencrypt.org/>`_ to automatically install and setup the certificate, or you can specify your own certificate.

  **To use a Let's Encrypt certificate**:

    The certificate is retrieved the first time that a client tries to connect to the Mattermost server. Certificates are retrieved for any hostname a client tries to reach the server at.

    a. Change the **Use Let's Encrypt** setting to ``true``.
    b. Restart the Mattermost server for these changes to take effect.

  **To use your own certificate**:

    a. Change the **Use Let's Encrypt** setting to ``false``.
    b. Change the **TLS Certificate File** setting to the location of the certificate file.
    c. Change the **TLS Key File** setting to the location of the private key file.
    d. Restart the Mattermost server for these changes to take effect.
