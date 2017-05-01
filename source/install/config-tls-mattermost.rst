Configuring TLS on the Mattermost Server
========================================

. Note::
  You can skip this section if you will be using NGINX to specify the certificates in use and configure the TLS/SSL settings.

1. Go to the **General** > **Configuration** section of the System Console.
2. Change the **Listen Address** setting to ``:443``
3. Change the **Connection Security** setting to ``TLS``
4. Change the **Forward port 80 to 443** setting to ``true`` if you wish to redirect users that try to connect insecurely to a secure connection. If you're using a proxy such as NGINX in front of Mattermost this setting is unnecessary and should be set to ``false``
5. Run ``sudo setcap cap_net_bind_service=+ep ./bin/platform`` in your Mattermost directory to allow Mattermost to bind to low ports. You will need to re-run this command every time you upgrade Mattermost or it will fail to bind to the port.

At this point you have two options: automatic certificate retrieval though Let's Encrypt or manually specifying a certificate.

Automatic Certificate Retrieval
-------------------------------

In this mode a certificate will be automatically retrieved the first time a client tries to connect to the Mattermost server. Certificates will be retrieved for any hostname a client tries to reach the server at. Setting this up is only one step:

1. Change the **Use Let's Encrypt** setting to ``true``.
2. Restart the Mattermost server for these changes to take effect.


Manual Certificate Specification
--------------------------------

1. Change the **Use Let's Encrypt** setting to ``false``.
2. Change the **TLS Certificate File** setting to the location of the certificate file.
3. Change the **TLS Key File** setting to the location of the private key file.
4. Restart the Mattermost server for these changes to take effect. 
