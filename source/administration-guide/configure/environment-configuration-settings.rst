Environment configuration settings
==================================

.. include:: ../../_static/badges/all-commercial.rst
  :start-after: :nosearch:

Review and manage the following environmental configuration options in the System Console by selecting the **Product** |product-list| menu, selecting **System Console**, and then selecting **Environment**:

- `Web server <#web-server>`__
- `Database <#database>`__
- `Enterprise search <#enterprise-search>`__
- `File storage <#file-storage>`__
- `Image proxy <#image-proxy>`__
- `SMTP <#smtp>`__
- `Push notification server <#push-notification-server>`__
- `High availability <#high-availability>`__
- `Rate limiting <#rate-limiting>`__
- `Logging <#logging>`__
- `Session lengths <#session-lengths>`__
- `Performance monitoring <#performance-monitoring>`__
- `Developer <#developer>`__
- `Mobile security <#mobile-security>`__
- `config.json-only settings <#config-json-only-settings>`__

.. tip::

  System admins managing a self-hosted Mattermost deployment can edit the ``config.json`` file as described in the following tables. Each configuration value below includes a JSON path to access the value programmatically in the ``config.json`` file using a JSON-aware tool. For example, the ``SiteURL`` value is under ``ServiceSettings``.

  - If using a tool such as `jq <https://stedolan.github.io/jq/>`__, you'd enter: ``cat config/config.json | jq '.ServiceSettings.SiteURL'``
  - When working with the ``config.json`` file manually, look for an object such as ``ServiceSettings``, then within that object, find the key ``SiteURL``.

Web server
----------

With self-hosted deployments, you can configure the network environment in which Mattermost is deployed by going to **System Console > Environment > Web Server**, or by updating the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: site-url
  :displayname: Site URL (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.SiteURL
  :environment: MM_SERVICESETTINGS_SITEURL
  :description: The URL that users use to access Mattermost. The port number is required if it’s not a standard port, such as 80 or 443.

Site URL
~~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------+
| The URL that users use to access Mattermost.                  | - System Config path: **Environment > Web Server**            |
| The port number is required if it’s not a standard port,      | - ``config.json`` setting: ``ServiceSettings`` > ``SiteURL``  |
| such as 80 or 443. This field is required.                    | - Environment variable: ``MM_SERVICESETTINGS_SITEURL``        |
|                                                               |                                                               |
| Select the **Test Live URL** button in the System Console     |                                                               |
| to validate the Site URL.                                     |                                                               |
+---------------------------------------------------------------+---------------------------------------------------------------+

.. note::

  - The URL may contain a subpath, such as ``https://example.com/company/mattermost``.
  - If you change the Site URL value, log out of the Desktop App, and sign back in using the new domain.
  - If Site URL is not set:

    - Email notifications will contain broken links, and email batching will not work.
    - Authentication via OAuth 2.0, including GitLab, Google, and Entra ID, will fail.
    - Plugins may not work as expected.

.. config:setting:: maximum-url-length
  :displayname: Maximum URL length (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.MaximumURLLength
  :environment: MM_SERVICESETTINGS_MAXIMUMURLLENGTH
  :description: The longest URL, in characters, including query parameters, accepted by the Mattermost server. Default is 2048 characters.

Maximum URL length
~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+----------------------------------------------------------------------------------+
| The longest URL, in characters, including query parameters,   | - System Config path: N/A                                                        |
| accepted by the Mattermost server. Longer URLs are rejected,  | - ``config.json`` setting: ``ServiceSettings`` > ``MaximumURLLength`` > ``2048`` |
| and API calls fail with an error.                             | - Environment variable: ``MM_SERVICESETTINGS_MAXIMUMURLLENGTH``                  |
|                                                               |                                                                                  |
| Numeric value. Default is **2048** characters.                |                                                                                  |
+---------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: web-server-listen-address
  :displayname: Web server listen address (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.ListenAddress
  :environment: MM_SERVICESETTINGS_LISTENADDRESS

  The address and port to which to bind and listen. Specifying ``:8065`` will bind to all network interfaces.
  Specifying ``127.0.0.1:8065`` will only bind to the network interface having that IP address.

Web server listen address
~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------+
| The address and port to which to bind and listen.             | - System Config path: **Environment > Web Server**                 |
| Specifying ``:8065`` will bind to all network interfaces.     | - ``config.json`` setting: ``ServiceSettings`` > ``ListenAddress`` |
| Specifying ``127.0.0.1:8065`` will only bind to the network   | - Environment variable: ``MM_SERVICESETTINGS_LISTENADDRESS``       |
| interface having that IP address.                             |                                                                    |
|                                                               |                                                                    |
| If you choose a port of a lower level (called “system ports”  |                                                                    |
| or “well-known ports”, in the range of 0-1023), you must have |                                                                    |
| permissions to bind to that port.                             |                                                                    |
+---------------------------------------------------------------+--------------------------------------------------------------------+

.. note::

  Web server uses ``address:port`` (e.g., ``":8065"``), while :ref:`Metrics <administration-guide/configure/environment-configuration-settings:listen address>` uses a port number only (e.g., ``8067``).

.. config:setting:: forward-port-80-to-443
  :displayname: Forward port 80 to 443 (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.Forward80To443
  :environment: MM_SERVICESETTINGS_FORWARD80TO443

  - **true**: Forwards all insecure traffic from port 80 to secure port 443.
  - **false**: **(Default)** When using a proxy such as NGINX in front of Mattermost this setting is unnecessary and should be set to false.

Forward port 80 to 443
~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------------------------+
| Forward insecure traffic from port 80 to port 443.            | - System Config path: **Environment > Web Server**                              |
|                                                               | - ``config.json`` setting: ``ServiceSettings`` > ``Forward80To443`` > ``false`` |
| - **true**: Forwards all insecure traffic from port 80 to     | - Environment variable: ``MM_SERVICESETTINGS_FORWARD80TO443``                   |
|   secure port 443.                                            |                                                                                 |
| - **false**: **(Default)** When using a proxy such as NGINX   |                                                                                 |
|   in front of Mattermost this setting is unnecessary          |                                                                                 |
|   and should be set to false.                                 |                                                                                 |
+---------------------------------------------------------------+---------------------------------------------------------------------------------+

.. config:setting:: web-server-connection-security
  :displayname: Web server connection security (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.ConnectionSecurity
  :environment: MM_SERVICESETTINGS_CONNECTIONSECURITY
  :description: Connection security between Mattermost clients and the server.

  - **Not specified**: Mattermost will connect over an unsecure connection.
  - **TLS**: Encrypts the communication between Mattermost clients and your server.

Web server connection security
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------+-------------------------------------------------------------------------+
| Connection security between Mattermost clients and the server.        | - System Config path: **Environment > Web Server**                      |
|                                                                       | - ``config.json`` setting: ``ServiceSettings`` > ``ConnectionSecurity`` |
| - **Not specified**: Mattermost will connect over an unsecure         | - Environment variable: ``MM_SERVICESETTINGS_CONNECTIONSECURITY``       |
|   connection.                                                         |                                                                         |
| - **TLS**: Encrypts the communication between Mattermost              |                                                                         |
|   clients and your server.                                            |                                                                         |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------+

See the :doc:`setting up TLS for Mattermost </deployment-guide/server/setup-tls>` for details.

.. config:setting:: tls-certificate-file
  :displayname: TLS certificate file (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.TLSCertFile
  :environment: MM_SERVICESETTINGS_TLSCERTFILE
  :description: The path to the certificate file to use for TLS connection security.

TLS certificate file
~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+--------------------------------------------------------------------+
| The path to the certificate file to use for TLS        | - System Config path: **Environment > Web Server**                 |
| connection security.                                   | - ``config.json`` setting: ``ServiceSettings`` > ``TLSCertFile``   |
|                                                        | - Environment variable: ``MM_SERVICESETTINGS_TLSCERTFILE``         |
| String input.                                          |                                                                    |
+--------------------------------------------------------+--------------------------------------------------------------------+

.. config:setting:: tls-key-file
  :displayname: TLS key file (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.TLSKeyFile
  :environment: MM_SERVICESETTINGS_TLSKEYFILE
  :description: The path to the TLS key file to use for TLS connection security.

TLS key file
~~~~~~~~~~~~

+--------------------------------------------------------+-----------------------------------------------------------------+
| The path to the TLS key file to use for TLS            | - System Config path: **Environment > Web Server**              |
| connection security.                                   | - ``config.json`` setting: ``ServiceSettings`` > ``TLSKeyFile`` |
|                                                        | - Environment variable: ``MM_SERVICESETTINGS_TLSKEYFILE``       |
| String input.                                          |                                                                 |
+--------------------------------------------------------+-----------------------------------------------------------------+

.. config:setting:: use-lets-encrypt
  :displayname: Use Let's Encrypt (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.UseLetsEncrypt
  :environment: MM_SERVICESETTINGS_USELETSENCRYPT
  :description: Enable the automatic retrieval of certificates from Let’s Encrypt.

  - **true**: The certificate will be retrieved when a client attempts to connect from a new domain. This will work with multiple domains.
  - **false**: **(Default)** Manual certificate specification based on the TLS Certificate File and TLS Key File specified above.

Use Let's Encrypt
~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------+
| Enable the automatic retrieval of certificates from Let’s Encrypt.          | - System Config path: **Environment > Web Server**                              |
|                                                                             | - ``config.json`` setting: ``ServiceSettings`` > ``UseLetsEncrypt`` > ``false`` |
|                                                                             | - Environment variable: ``MM_SERVICESETTINGS_USELETSENCRYPT``                   |
| - **true**: The certificate will be retrieved when a client                 |                                                                                 |
|   attempts to connect from a new domain. This will work with                |                                                                                 |
|   multiple domains.                                                         |                                                                                 |
| - **false**: **(Default)** Manual certificate specification                 |                                                                                 |
|   based on the TLS Certificate File and TLS Key File specified              |                                                                                 |
|   above.                                                                    |                                                                                 |
+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------+

See the :doc:`setting up TLS for Mattermost </deployment-guide/server/setup-tls>` for details on setting up Let's Encrypt.

.. config:setting:: lets-encrypt-certificate-cache-file
  :displayname: Let's Encrypt certificate cache file (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.LetsEncryptCertificateCacheFile
  :environment: MM_SERVICESETTINGS_LETSENCRYPTCERTIFICATECACHEFILE
  :description: The path to the file where certificates and other data about the Let’s Encrypt service will be stored.

Let's Encrypt certificate cache file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+--------------------------------------------------------------------------------------+
| The path to the file where certificates and other data | - System Config path: **Environment > Web Server**                                   |
| about the Let’s Encrypt service will be stored.        | - ``config.json`` setting: ``ServiceSettings`` > ``LetsEncryptCertificateCacheFile`` |
|                                                        | - Environment variable: ``MM_SERVICESETTINGS_LETSENCRYPTCERTIFICATECACHEFILE``       |
| File path input.                                       |                                                                                      |
+--------------------------------------------------------+--------------------------------------------------------------------------------------+

.. config:setting:: read-timeout
  :displayname: Read timeout (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.ReadTimeout
  :environment: MM_SERVICESETTINGS_READTIMEOUT
  :description: Maximum time allowed from when the connection is accepted to when the request body is fully read. Default is **300** seconds.

Read timeout
~~~~~~~~~~~~

+---------------------------------------------------------+----------------------------------------------------------------------------+
| Maximum time allowed from when the connection is        | - System Config path: **Environment > Web Server**                         |
| accepted to when the request body is fully read.        | - ``config.json`` setting: ``ServiceSettings`` > ``ReadTimeout`` > ``300`` |
|                                                         | - Environment variable: ``MM_SERVICESETTINGS_READTIMEOUT``                 |
| Numerical input in seconds. Default is **300** seconds. |                                                                            |
+---------------------------------------------------------+----------------------------------------------------------------------------+

.. config:setting:: write-timeout
  :displayname: Write timeout (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.WriteTimeout
  :environment: MM_SERVICESETTINGS_WRITETIMEOUT

  If using HTTP (insecure), this is the maximum time, in seconds, allowed from the end of reading the request headers until the response is written.
  If using HTTPS, it's the total time, in seconds, from when the connection is accepted until the response is written.
  Default is 300 seconds.

Write timeout
~~~~~~~~~~~~~

+----------------------------------------------------------+-----------------------------------------------------------------------------+
| - If using HTTP (insecure), this is the maximum time     | - System Config path: **Environment > Web Server**                          |
|   allowed from the end of reading the request headers    | - ``config.json`` setting: ``ServiceSettings`` > ``WriteTimeout`` > ``300`` |
|   until the response is written.                         | - Environment variable: ``MM_SERVICESETTINGS_WRITETIMEOUT``                 |
| - If using HTTPS, it's the total time from when the      |                                                                             |
|   connection is accepted until the response is written.  |                                                                             |
|                                                          |                                                                             |
| Numerical input in seconds. Default is **300** seconds.  |                                                                             |
+----------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: idle-timeout
  :displayname: Idle timeout (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.IdleTimeout
  :environment: MM_SERVICESETTINGS_IDLETIMEOUT
  :description: This is the maximum time, in seconds, allowed before an idle connection is disconnected. Default is **300** seconds.

Idle timeout
~~~~~~~~~~~~

+---------------------------------------------------------+----------------------------------------------------------------------------+
| Set an explicit idle timeout in the HTTP server.        | - System Config path: **Environment > Web Server**                         |
| This is the maximum time allowed before an idle         | - ``config.json`` setting: ``ServiceSettings`` > ``IdleTimeout`` > ``300`` |
| connection is disconnected.                             | - Environment variable: ``MM_SERVICESETTINGS_IDLETIMEOUT``                 |
|                                                         |                                                                            |
| Numerical input in seconds. Default is **300** seconds. |                                                                            |
+---------------------------------------------------------+----------------------------------------------------------------------------+

.. config:setting:: webserver-mode
  :displayname: Webserver mode (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.WebserverMode
  :environment: MM_SERVICESETTINGS_WEBSERVERMODE

  - **gzip**: **(Default)** The Mattermost server will serve static files compressed with gzip to improve performance.
  - **Uncompressed**: The Mattermost server will serve static files uncompressed.
  - **Disabled**: The Mattermost server will not serve static files.

Webserver mode
~~~~~~~~~~~~~~

+---------------------------------------------------------------------+---------------------------------------------------------------------------------+
| We recommend gzip to improve performance unless your                | - System Config path: **Environment > Web Server**                              |
| environment has specific restrictions, such as a web proxy that     | - ``config.json`` setting: ``ServiceSettings`` > ``WebserverMode`` > ``"gzip"`` |
| distributes gzip files poorly.                                      | - Environment variable: ``MM_SERVICESETTINGS_WEBSERVERMODE``                    |
|                                                                     |                                                                                 |
| - **gzip**: **(Default)** The Mattermost server will serve static   |                                                                                 |
|   files compressed with gzip to improve performance.                |                                                                                 |
|   gzip compression applies to the HTML, CSS, Javascript, and other  |                                                                                 |
|   static content files that make up the Mattermost web client.      |                                                                                 |
| - **Uncompressed**: The Mattermost server will serve static         |                                                                                 |
|   files uncompressed.                                               |                                                                                 |
| - **Disabled**: The Mattermost server will not serve static files.  |                                                                                 |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------+

.. config:setting:: enable-insecure-outgoing-connections
  :displayname: Enable insecure outgoing connections (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.EnableInsecureOutgoingConnections
  :environment: MM_SERVICESETTINGS_ENABLEINSECUREOUTGOINGCONNECTIONS

  - **true**: Outgoing HTTPS requests, including S3 clients, can accept unverified, self-signed certificates.
  - **false**: **(Default)** Only secure HTTPS requests are allowed.

Enable insecure outgoing connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Configure Mattermost to allow insecure outgoing connections.  | - System Config path: **Environment > Web Server**                                                 |
|                                                               | - ``config.json`` setting: ``ServiceSettings`` > ``EnableInsecureOutgoingConnections`` > ``false`` |
| - **true**: Outgoing HTTPS requests, including S3 clients,    | - Environment variable: ``MM_SERVICESETTINGS_ENABLEINSECUREOUTGOINGCONNECTIONS``                   |
|   can accept unverified, self-signed certificates.            |                                                                                                    |
|   For example, outgoing webhooks to a server with a           |                                                                                                    |
|   self-signed TLS certificate, using any domain, will be      |                                                                                                    |
|   allowed, and will skip TLS verification.                    |                                                                                                    |
| - **false**: **(Default)** Only secure HTTPS requests are     |                                                                                                    |
|   allowed.                                                    |                                                                                                    |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------------------+

.. warning::

  Enabling this feature makes these connections susceptible to man-in-the-middle attacks.

.. config:setting:: managed-resource-paths
  :displayname: Managed resource paths (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.ManagedResourcePaths
  :environment: MM_SERVICESETTINGS_MANAGEDRESOURCEPATHS
  :description: A comma-separated list of paths within the Mattermost domain that are managed by a third party service instead of Mattermost itself.

Managed resource paths
~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+---------------------------------------------------------------------------+
| A comma-separated list of paths within the Mattermost  | - System Config path: **Environment > Web Server**                        |
| domain that are managed by a third party service       | - ``config.json`` setting: ``ServiceSettings`` > ``ManagedResourcePaths`` |
| instead of Mattermost itself.                          | - Environment variable: ``MM_SERVICESETTINGS_MANAGEDRESOURCEPATHS``       |
|                                                        |                                                                           |
| Links to these paths will be opened in a new           |                                                                           |
| tab/window by Mattermost apps.                         |                                                                           |
|                                                        |                                                                           |
| For example, if Mattermost is running on               |                                                                           |
| ``https://mymattermost.com``, setting this to          |                                                                           |
| conference will cause links such as                    |                                                                           |
| ``https://mymattermost.com/conference`` to open in a   |                                                                           |
| new window.                                            |                                                                           |
+--------------------------------------------------------+---------------------------------------------------------------------------+

.. note::

  When using the Mattermost Desktop App, additional configuration is required to open the link within the Desktop App instead of in a browser. See the :doc:`desktop managed resources </deployment-guide/desktop/desktop-app-managed-resources>` documentation for details.

Reload configuration from disk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+----------------------------------------------------------+---------------------------------------------------------------+
| You must change the database line in the ``config.json`` | - System Config path: **Environment > Web Server**            |
| file, and then reload configuration to fail over         | - ``config.json`` setting: N/A                                |
| without taking the server down.                          | - Environment variable: N/A                                   |
|                                                          |                                                               |
| Select the **Reload configuration from disk** button     |                                                               |
| in the System Console after changing your database       |                                                               |
| configuration. Then, go to **Environment > Database**    |                                                               |
| and select **Recycle Database Connections** to           |                                                               |
| complete the reload.                                     |                                                               |
+----------------------------------------------------------+---------------------------------------------------------------+

Purge all caches
~~~~~~~~~~~~~~~~

+----------------------------------------------------------+---------------------------------------------------------------+
| Purge all in-memory caches for sessions, accounts,       | - System Config path: **Environment > Web Server**            |
| and channels.                                            | - ``config.json`` setting: N/A                                |
|                                                          | - Environment variable: N/A                                   |
| Select the **Purge All Caches** button in the System     |                                                               |
| Console to purge all caches.                             |                                                               |
+----------------------------------------------------------+---------------------------------------------------------------+

.. note::

  Purging the caches may adversely impact performance. :doc:`high availability cluster-based deployments </administration-guide/scale/high-availability-cluster-based-deployment>` will attempt to purge all the servers in the cluster.

.. config:setting:: websocket-url
  :displayname: Websocket URL (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.WebsocketURL
  :environment: MM_SERVICESETTINGS_WEBSOCKETURL
  :description: You can configure the server to instruct clients on where they should try to connect websockets to.

Websocket URL
~~~~~~~~~~~~~

+--------------------------------------------------------+-----------------------------------------------------------------------------+
| You can configure the server to instruct clients       | - System Config path: N/A                                                   |
| on where they should try to connect websockets to.     | - ``config.json`` setting: ``ServiceSettings`` > ``WebsocketURL`` > ``""``  |
|                                                        | - Environment variable: ``MM_SERVICESETTINGS_WEBSOCKETURL``                 |
| String input.                                          |                                                                             |
+--------------------------------------------------------+-----------------------------------------------------------------------------+

.. note::

  We strongly recommend configuring a single websocket URL that matches the `Site URL <#site-url>`_ configuration setting.

.. config:setting:: license-file-location
  :displayname: License file location (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.LicenseFileLocation
  :environment: MM_SERVICESETTINGS_LICENSEFILELOCATION
  :description: The path and filename of the license file on disk.

License file location
~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+------------------------------------------------------------------------------------+
| The path and filename of the license file on disk.     | - System Config path: N/A                                                          |
| On startup, if Mattermost can't find a valid license   | - ``config.json`` setting: ``ServiceSettings`` > ``LicenseFileLocation`` > ``""``  |
| in the database from a previous upload, it looks in    | - Environment variable: ``MM_SERVICESETTINGS_LICENSEFILELOCATION``                 |
| this path for the license file.                        |                                                                                    |
|                                                        |                                                                                    |
| String input. Can be an absolute path or a path        |                                                                                    |
| relative to the ``mattermost`` directory.              |                                                                                    |
+--------------------------------------------------------+------------------------------------------------------------------------------------+

.. config:setting:: tls-minimum-version
  :displayname: TLS minimum version (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.TLSMinVer
  :environment: MM_SERVICESETTINGS_TLSMINVER
  :description: The minimum TLS version used by the Mattermost server. Default value is **1.2**.

TLS minimum version
~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+----------------------------------------------------------------------------+
| The minimum TLS version used by the Mattermost server. | - System Config path: N/A                                                  |
|                                                        | - ``config.json`` setting: ``ServiceSettings`` > ``TLSMinVer`` > ``1.2``   |
| String input. Default is **1.2**.                      | - Environment variable: ``MM_SERVICESETTINGS_TLSMINVER``                   |
+--------------------------------------------------------+----------------------------------------------------------------------------+

.. note::

  This setting only takes effect if you are using the built-in server binary directly, and not using a reverse proxy layer, such as NGINX.

.. config:setting:: trusted-proxy-ip-header
  :displayname: Trusted proxy IP header (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.TrustedProxyIPHeader
  :environment: MM_SERVICESETTINGS_TRUSTEDPROXYIPHEADER
  :description: Specified headers that will be checked, one by one, for IP addresses (order is important). All other headers are ignored.

Trusted proxy IP header
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+-------------------------------------------------------------------------------------+
| Specified headers that will be checked, one by one,    | - System Config path: N/A                                                           |
| for IP addresses (order is important).                 | - ``config.json`` setting: ``ServiceSettings`` > ``TrustedProxyIPHeader`` > ``[]``  |
| All other headers are ignored.                         | - Environment variable: ``MM_SERVICESETTINGS_TRUSTEDPROXYIPHEADER``                 |
|                                                        |                                                                                     |
| String array input consisting of header names,         |                                                                                     |
| such as ``["X-Forwarded-For", "X-Real-Ip"]``.          |                                                                                     |
+--------------------------------------------------------+-------------------------------------------------------------------------------------+

.. note::

  - The default value of ``[]`` means that no header will be trusted.
  - We recommend keeping the default setting when Mattermost is running without a proxy to avoid the client sending the headers and bypassing rate limiting and/or the audit log.
  - For environments that use a reverse proxy, this issue does not exist, provided that the headers are set by the reverse proxy. In those environments, only explicitly whitelist the header set by the reverse proxy and no additional values.

.. config:setting:: enable-strict-transport-security-hsts
  :displayname: Enable Strict Transport Security (HSTS) (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.TLSStrictTransport
  :environment: MM_SERVICESETTINGS_TLSSTRICTTRANSPORT

  - **true**: Adds the Strict Transport Security (HSTS) header to all responses, forcing the browser to request all resources via HTTPS.
  - **false**: **(Default)** No restrictions on TLS transport. Strict Transport Security (HSTS) header isn't added to responses.

Enable Strict Transport Security (HSTS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+--------------------------------------------------------------------------------------+
| - **true**: Adds the Strict Transport Security (HSTS)  | - System Config path: N/A                                                            |
|   header to all responses, forcing the browser to      | - ``config.json`` setting: ``ServiceSettings`` > ``TLSStrictTransport`` > ``false``  |
|   request all resources via HTTPS.                     | - Environment variable: ``MM_SERVICESETTINGS_TLSSTRICTTRANSPORT``                    |
| - **false**: **(Default)** No restrictions on TLS      |                                                                                      |
|   transport. Strict Transport Security (HSTS) header   |                                                                                      |
|   isn't added to responses.                            |                                                                                      |
+--------------------------------------------------------+--------------------------------------------------------------------------------------+

See the `Strict-Transport-Security <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security>`__ documentation for details.

.. config:setting:: secure-tls-transport-expiry
  :displayname: Secure TLS transport expiry (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.TLSStrictTransportMaxAge
  :environment: MM_SERVICESETTINGS_TLSSTRICTTRANSPORTMAXAGE
  :description: The time, in seconds, that the browser remembers a site is only to be accessed using HTTPS. Default is **63072000** seconds (2 years).

Secure TLS transport expiry
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| The time, in seconds, that the browser remembers a     | - System Config path: N/A                                                                     |
| site is only to be accessed using HTTPS. After this    | - ``config.json`` setting: ``ServiceSettings`` > ``TLSStrictTransportMaxAge`` > ``63072000``  |
| period, a site can't be accessed using HTTP unless     | - Environment variable: ``MM_SERVICESETTINGS_TLSSTRICTTRANSPORTMAXAGE``                       |
| ``TLSStrictTransport`` is set to ``true``.             |                                                                                               |
|                                                        |                                                                                               |
| Numerical input. Default is **63072000** (2 years).    |                                                                                               |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------+

See the `Strict-Transport-Security <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security>`__ documentation for details.

.. config:setting:: tls-cipher-overwrites
  :displayname: TLS cipher overwrites (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.TLSOverwriteCiphers
  :environment: MM_SERVICESETTINGS_TLSOVERWRITECIPHERS
  :description: Set TLS ciphers overwrites to meet requirements from legacy clients which don't support modern ciphers, or to limit the types of accepted ciphers.

TLS cipher overwrites
~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+------------------------------------------------------------------------------------+
| Set TLS ciphers overwrites to meet requirements from   | - System Config path: N/A                                                          |
| legacy clients which don't support modern ciphers,     | - ``config.json`` setting: ``ServiceSettings`` > ``TLSOverwriteCiphers`` > ``[]``  |
| or to limit the types of accepted ciphers.             | - Environment variable: ``MM_SERVICESETTINGS_TLSOVERWRITECIPHERS``                 |
|                                                        |                                                                                    |
| If none specified, the Mattermost server assumes a     |                                                                                    |
| set of currently considered secure ciphers, and allows |                                                                                    |
| overwrites in the edge case.                           |                                                                                    |
|                                                        |                                                                                    |
| String array input.                                    |                                                                                    |
+--------------------------------------------------------+------------------------------------------------------------------------------------+

.. note::

  - This setting only takes effect if you are using the built-in server binary directly and not using a reverse proxy layer, such as NGINX.
  - See the ``ServerTLSSupportedCiphers`` variable in `/model/config.go <https://github.com/mattermost/mattermost/blob/master/server/public/model/config.go>`__ for a list of ciphers considered secure.

.. config:setting:: goroutine-health-threshold
  :displayname: Goroutine health threshold (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.GoroutineHealthThreshold
  :environment: MM_SERVICESETTINGS_GOROUTINEHEALTHTHRESHOLD
  :description: Set a threshold on the number of goroutines when the Mattermost system is considered to be in a healthy state. Default is **-1** which turns off checking for the threshold.

Goroutine health threshold
~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Set a threshold on the number of goroutines when the   | - System Config path: N/A                                                               |
| Mattermost system is considered to be in a healthy     | - ``config.json`` setting: ``ServiceSettings`` > ``GoroutineHealthThreshold`` > ``-1``  |
| state.                                                 | - Environment variable: ``MM_SERVICESETTINGS_GOROUTINEHEALTHTHRESHOLD``                 |
|                                                        |                                                                                         |
| When goroutines exceed this limit, a warning is        |                                                                                         |
| returned in the server logs.                           |                                                                                         |
|                                                        |                                                                                         |
| Numeric input. Default is **-1** which turns off       |                                                                                         |
| checking for the threshold.                            |                                                                                         |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. config:setting:: allow-cookies-for-subdomains
  :displayname: Allow cookies for subdomains (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.AllowCookiesForSubdomains
  :environment: MM_SERVICESETTINGS_ALLOWCOOKIESFORSUBDOMAINS

  - **true**: **(Default)** Allows cookies for subdomains by setting the domain parameter on Mattermost cookies.
  - **false**: Cookies not allowed for subdomains.

Allow cookies for subdomains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+--------------------------------------------------------------------------------------------+
| - **true**: **(Default)** Allows cookies for           | - System Config path: N/A                                                                  |
|   subdomains by setting the domain parameter on        | - ``config.json`` setting: ``ServiceSettings`` > ``AllowCookiesForSubdomains`` > ``true``  |
|   Mattermost cookies.                                  | - Environment variable: ``MM_SERVICESETTINGS_ALLOWCOOKIESFORSUBDOMAINS``                   |
| - **false**: Cookies aren't allowed for subdomains.    |                                                                                            |
+--------------------------------------------------------+--------------------------------------------------------------------------------------------+

.. config:setting:: cluster-log-timeout
  :displayname: Cluster log timeout (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.ClusterLogTimeoutMilliseconds
  :environment: MM_SERVICESETTINGS_CLUSTERLOGTIMEOUTMILLISECONDS
  :description: Define the frequency, in milliseconds, of cluster request time logging for performance monitoring. Default is **2000** milliseconds (2 seconds).

Cluster log timeout
~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+--------------------------------------------------------+------------------------------------------------------------------------------------------------+
| Define the frequency, in milliseconds, of cluster      | - System Config path: N/A                                                                      |
| request time logging for performance monitoring.       | - ``config.json`` setting: ``ServiceSettings`` > ``ClusterLogTimeoutMilliseconds`` > ``2000``  |
|                                                        | - Environment variable: ``MM_SERVICESETTINGS_CLUSTERLOGTIMEOUTMILLISECONDS``                   |
|                                                        |                                                                                                |
| Numerical input. Default is **2000** milliseconds      |                                                                                                |
| (2 seconds).                                           |                                                                                                |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------+

See the :doc:`performance monitoring </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>` documentation for details.

.. config:setting:: maximum-payload-size
  :displayname: Maximum payload size (File Storage)
  :systemconsole: N/A
  :configjson: .ServiceSettings.MaximumPayloadSizeBytes
  :environment: MM_SERVICESETTINGS_MAXIMUMPAYLOADSIZEBYTES
  :description: The maximum payload size in bytes for all APIs except APIs that receive a file as an input. For example, the upload attachment API or the API to upload a custom emoji. Default is 300000.

Maximum payload size
~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------+--------------------------------------------------------------------------------------------+
| The maximum payload size in bytes for all APIs except     | - System Config path: N/A                                                                  |
| APIs that receive a file as an input.                     | - ``config.json`` setting: ``ServiceSettings`` > ``MaximumPayloadSizeBytes`` > ``300000``  |
|                                                           | - Environment variable: ``MM_SERVICESETTINGS_MAXIMUMPAYLOADSIZEBYTES``                     |
| For example, the upload attachment API or the API to      |                                                                                            |
| upload a custom emoji.                                    |                                                                                            |
|                                                           |                                                                                            |
| Numerical value. Default is **300000** (300 kB).          |                                                                                            |
+-----------------------------------------------------------+--------------------------------------------------------------------------------------------+

----

Database
--------

With self-hosted deployments, you can configure the database environment in which Mattermost is deployed by going to **System Console > Environment > Database**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: driver-name
  :displayname: Driver name (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.DriverName
  :environment: MM_SQLSETTINGS_DRIVERNAME
  :description: The type of database. Either **postgres** or **mysql**. The default value is **mysql**.

Driver name
~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The type of database. Can be either:                          | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``SqlSettings`` > ``DriverName``              |
| - **mysql**: **(Default)** Enables driver to MySQL database.  | - Environment variable: ``MM_SQLSETTINGS_DRIVERNAME``                    |
| - **postgres**: Enables driver to PostgreSQL database.        |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: data-source
  :displayname: Data source (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.DataSource
  :environment: MM_SQLSETTINGS_DATASOURCE
  :description: The connection string to the master database.

Data source
~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The connection string to the master database.                 | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``SqlSettings`` > ``DataSource``              |
| String input.                                                 | - Environment variable: ``MM_SQLSETTINGS_DATASOURCE``                    |
|                                                               |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

PostgreSQL databases
^^^^^^^^^^^^^^^^^^^^

When **Driver Name** is set to postgres, use a connection string in the form of:
``postgres://mmuser:password@hostname_or_IP:5432/mattermost_test?sslmode=disable&connect_timeout=10``

**To use TLS with PostgreSQL databases**

The parameter to encrypt connection against a PostgreSQL server is sslmode. The library used to interact with PostgreSQL server is `pq <https://pkg.go.dev/github.com/lib/pq>`__. Currently, it's not possible to use all the values that you could pass to a standard PostgreSQL Client ``psql "sslmode=value"`` See the `SSL Mode Descriptions <https://www.postgresql.org/docs/current/libpq-ssl.html>`__ documentation for details.

Your database admin must configure the functionality according to the supported values described below.

+----------------------------------------+-----------------+---------------------------------------------------------------------------+
| Short description of the ``sslmode``   | Value           | Example of a data source name                                             |
| parameter                              |                 |                                                                           |
+========================================+=================+===========================================================================+
| Don't use TLS / SSL encryption against | ``disable``     | ``postgres://mmuser:password@hostname_or_IP:5432/mattermost_test          |
| the PostgreSQL server.                 |                 | ?sslmode=disable&connect_timeout=10``                                     |
|                                        |                 |                                                                           |
| Default value in file ``config.json``  |                 |                                                                           |
+----------------------------------------+-----------------+---------------------------------------------------------------------------+
| The data is encrypted and the network  | ``require``     | ``postgres://mmuser:password@hostname_or_IP:5432/mattermost_test          |
| is trusted.                            |                 | ?sslmode=require&connect_timeout=10``                                     |
|                                        |                 |                                                                           |
| Default value is ``sslmode`` when      |                 |                                                                           |
| omitted.                               |                 |                                                                           |
+----------------------------------------+-----------------+---------------------------------------------------------------------------+
| The data is encrypted when connecting  | ``verify-ca``   | ``postgres://mmuser:password@hostname_or_IP:5432/mattermost_test          |
| to a trusted server.                   |                 | ?sslmode=verify-ca&connect_timeout=10``                                   |
+----------------------------------------+-----------------+---------------------------------------------------------------------------+
| The data is encrypted when connecting  | ``verify-full`` | ``postgres://mmuser:password@hostname_or_IP:5432/mattermost_test          |
| to a trusted server.                   |                 | ?sslmode=verify-full&connect_timeout=10``                                 |
+----------------------------------------+-----------------+---------------------------------------------------------------------------+

MySQL Databases
^^^^^^^^^^^^^^^

When Driver Name is set to mysql, we recommend using collation over using charset.

To specify collation:

.. code-block:: text

  "SqlSettings": {
      "DataSource": "<mmuser:password>@tcp(hostname or IP:3306)/mattermost?charset=utf8mb4,utf8&collation=utf8mb4_general_ci",
      [...]
  }

If collation is omitted, the default collation, ``utf8mb4_general_ci`` is used:

.. code-block:: text

  "SqlSettings": {
    "DataSource": "<mmuser:password>@tcp(hostname or IP:3306)/mattermost?charset=utf8mb4,utf8",
    [...]
  }

.. note::

  If you’re using MySQL 8.0 or later, the default collation has changed to ``utf8mb4_0900_ai_ci``. See our :doc:`Database Software Requirements </deployment-guide/software-hardware-requirements>` documentation for details on MySQL 8.0 support.

**To use TLS with MySQL Databases**

The parameter to encrypt connection against a MySQL server is ``tls``.

The library used to interact with MySQL is `Go-MySQL-Driver <https://pkg.go.dev/github.com/go-sql-driver/mysql>`__.

For the moment, it's not possible to use all the values that you could pass to a standard MySQL Client ``mysql --ssl-mode=value``.
See `Connection-Encryption Option Summary <https://dev.mysql.com/doc/refman/8.0/en/connection-options.html#option_general_ssl-mode>`__ documentation for a version 8.0 example.

Your database admin must configure the functionality according to supported values described below.

+----------------------------------------+-----------------+-----------------------------------------------------------------+
| Short description of the ``tls``       | Value           | Example of a data source name                                   |
| parameter                              |                 |                                                                 |
+========================================+=================+=================================================================+
| Don't use TLS / SSL encryption against | ``false``       | ``"<mmuser:password>@tcp(hostname or IP:3306)/mattermost_test   |
| MySQL server.                          |                 | ?charset=utf8mb4,utf8&writeTimeout=30s&tls=false"``             |
+----------------------------------------+-----------------+-----------------------------------------------------------------+
| Use TLS / SSL encryption against       | ``true``        | ``"<mmuser:password>@tcp(hostname or IP:3306)/mattermost_test   |
| MySQL server.                          |                 | ?charset=utf8mb4,utf8&writeTimeout=30s&tls=true"``              |
+----------------------------------------+-----------------+-----------------------------------------------------------------+
| Use TLS / SSL encryption with a self-  | ``skip-verify`` | ``"<mmuser:password>@tcp(hostname or IP:3306)/mattermost_test   |
| signed certificate against             |                 | ?charset=utf8mb4,utf8&writeTimeout=30s&tls=skip-verify"``       |
| MySQL server.                          |                 |                                                                 |
+----------------------------------------+-----------------+-----------------------------------------------------------------+
| Use TLS / SSL encryption if server     | ``preferred``   | ``"<mmuser:password>@tcp(hostname or IP:3306)/mattermost_test   |
| advertises a possible fallback;        |                 | ?charset=utf8mb4,utf8&writeTimeout=30s&tls=preferred"``         |
| unencrypted if it's not advertised.    |                 |                                                                 |
+----------------------------------------+-----------------+-----------------------------------------------------------------+

AWS High Availablity RDS cluster deployments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For an AWS High Availability RDS cluster deployment, point this configuration setting to the write/read endpoint at the **cluster**
level to benefit from the AWS failover handling. AWS takes care of promoting different database nodes to be the writer node.
Mattermost doesn't need to manage this. See the :ref:`high availablility database configuration <administration-guide/scale/high-availability-cluster-based-deployment:database configuration>` documentation for details.

.. config:setting:: maximum-open-connections
  :displayname: Maximum open connections (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.MaxOpenConns
  :environment: MM_SQLSETTINGS_MAXOPENCONNS
  :description: The maximum number of open connections to the database. Default is **100**.

Maximum open connections
~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+-------------------------------------------------------------------------+
| The maximum number of open connections to the          | - System Config path: **Environment > Database**                        |
| database.                                              | - ``config.json`` setting: ``SqlSettings`` > ``MaxOpenConns`` > ``100`` |
|                                                        | - Environment variable: ``MM_SQLSETTINGS_MAXOPENCONNS``                 |
| Numerical input. Default is **100**.                   |                                                                         |
+--------------------------------------------------------+-------------------------------------------------------------------------+

.. config:setting:: maximum-idle-connections
  :displayname: Maximum idle connections (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.MaxIdleConns
  :environment: MM_SQLSETTINGS_MAXIDLECONNS
  :description: The maximum number of idle connections held open to the database. Default is **50**.

Maximum idle connections
~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+-------------------------------------------------------------------------+
| The maximum number of idle connections held open to    | - System Config path: **Environment > Database**                        |
| the database.                                          | - ``config.json`` setting: ``SqlSettings`` > ``MaxIdleConns`` > ``50``  |
|                                                        | - Environment variable: ``MM_SQLSETTINGS_MAXIDLECONNS``                 |
| Numerical input. Default is **50**.                    |                                                                         |
| A 2:1 ratio with MaxOpenConns is recommended.          |                                                                         |
+--------------------------------------------------------+-------------------------------------------------------------------------+

.. config:setting:: query-timeout
  :displayname: Query timeout (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.QueryTimeout
  :environment: MM_SQLSETTINGS_QUERYTIMEOUT
  :description: The amount of time to wait, in seconds, for a response from the database after opening a connection and sending the query. Default is **30** seconds.

Query timeout
~~~~~~~~~~~~~

+--------------------------------------------------------+-------------------------------------------------------------------------+
| The amount of time to wait, in seconds, for a response | - System Config path: **Environment > Database**                        |
| from the database after opening a connection and       | - ``config.json`` setting: ``SqlSettings`` > ``QueryTimeout`` > ``30``  |
| sending the query.                                     | - Environment variable: ``MM_SQLSETTINGS_QUERYTIMEOUT``                 |
|                                                        |                                                                         |
| Numerical input in seconds. Default is **30** seconds. |                                                                         |
+--------------------------------------------------------+-------------------------------------------------------------------------+

.. config:setting:: maximum-connection-lifetime
  :displayname: Maximum connection lifetime (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.ConnMaxLifetimeMilliseconds
  :environment: MM_SQLSETTINGS_CONNMAXLIFETIMEMILLISECONDS
  :description: Maximum lifetime for a connection to the database, in milliseconds. Default is **3600000** milliseconds (1 hour).

Maximum connection lifetime
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+--------------------------------------------------------------------------------------------+
| Maximum lifetime for a connection to the database,     | - System Config path: **Environment > Database**                                           |
| in milliseconds. Use this setting to configure the     | - ``config.json`` setting: ``SqlSettings`` > ``ConnMaxLifetimeMilliseconds`` > ``3600000`` |
| maximum amount of time a connection to the database    | - Environment variable: ``MM_SQLSETTINGS_CONNMAXLIFETIMEMILLISECONDS``                     |
| may be reused                                          |                                                                                            |
|                                                        |                                                                                            |
| Numerical input in milliseconds. Default is            |                                                                                            |
| **3600000** milliseconds (1 hour).                     |                                                                                            |
+--------------------------------------------------------+--------------------------------------------------------------------------------------------+

.. config:setting:: maximum-connection-idle-timeout
  :displayname: Maximum connection idle timeout (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.ConnMaxIdleTimeMilliseconds
  :environment: MM_SQLSETTINGS_CONNMAXIDLETIMEMILLISECONDS
  :description: Maximum time a database connection can remain idle, in milliseconds. Default is **300000** milliseconds (5 minutes).

Maximum connection idle timeout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+--------------------------------------------------------------------------------------------+
| Maximum time a database connection can remain idle,    | - System Config path: **Environment > Database**                                           |
| in milliseconds.                                       | - ``config.json`` setting: ``SqlSettings`` > ``ConnMaxIdleTimeMilliseconds`` > ``300000``  |
|                                                        | - Environment variable: ``MM_SQLSETTINGS_CONNMAXIDLETIMEMILLISECONDS``                     |
| Numerical input in milliseconds. Default is **300000** |                                                                                            |
| (5 minutes).                                           |                                                                                            |
+--------------------------------------------------------+--------------------------------------------------------------------------------------------+

.. config:setting:: minimum-hashtag-length
  :displayname: Minimum hashtag length (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.MinimumHashtagLength
  :environment: MM_SQLSETTINGS_MINIMUMHASHTAGLENGTH
  :description: Minimum number of characters in a hashtag. This value must be greater than or equal to **2**. Default is **3**.

Minimum hashtag length
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------+--------------------------------------------------------------------------------+
| Minimum number of characters in a hashtag.                           | - System Config path: **Environment > Database**                               |
| This value must be greater than or equal to **2**.                   | - ``config.json`` setting: ``SqlSettings`` > ``MinimumHashtagLength`` > ``3``  |
|                                                                      | - Environment variable: ``MM_SQLSETTINGS_MINIMUMHASHTAGLENGTH``                |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------+

.. note::

  MySQL databases must be configured to support searching strings shorter than three characters. See the `MySQL documentation <https://dev.mysql.com/doc/refman/8.0/en/fulltext-fine-tuning.html>`__ for details.

.. config:setting:: sql-statement-logging
  :displayname: SQL statement logging (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.Trace
  :environment: MM_SQLSETTINGS_TRACE
  :description: Log executed SQL statements for development purposes. Default is **false**.

  - **true**: Executing SQL statements are written to the log.
  - **false**: **(Default)** SQL statements aren't written to the log.

SQL statement logging
~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Executed SQL statements can be written to the log for         | - System Config path: **Environment > Database**                         |
| development.                                                  | - ``config.json`` setting: ``SqlSettings`` > ``Trace`` > ``false``       |
|                                                               | - Environment variable: ``MM_SQLSETTINGS_TRACE``                         |
| - **true**: Executing SQL statements are written to the log.  |                                                                          |
| - **false**: **(Default)** SQL statements aren't written      |                                                                          |
|   to the log.                                                 |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Recycle database connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+--------------------------------------------------------+------------------------------------------------------------------+
| Select the **Recycle Database Connections** button to  | - System Config path: **Environment > Database**                 |
| manually recycle the connection pool by closing the    | - ``config.json`` setting: N/A                                   |
| current set of open connections to the database        | - Environment variable: N/A                                      |
| within 20 seconds, and then creating a new set of      |                                                                  |
| connections.                                           |                                                                  |
|                                                        |                                                                  |
| To fail over without stopping the server, change the   |                                                                  |
| database line in the ``config.json`` file, select      |                                                                  |
| **Reload Configuration from Disk** via **Environment   |                                                                  |
| > Web Server**, then select **Recycle Database         |                                                                  |
| Connections**.                                         |                                                                  |
+--------------------------------------------------------+------------------------------------------------------------------+

.. config:setting:: disable-database-search
  :displayname: Disable database search (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.DisableDatabaseSearch
  :environment: MM_SQLSETTINGS_DISABLEDATABASESEARCH

  - **true**: Disables the use of the database to perform searches. If another search engine isn't configured, setting this value to ``true`` will result in empty search results.
  - **false**: **(Default)** Database search isn't disabled.

Disable database search
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
| When :doc:`enterprise-scale search </administration-guide/scale/enterprise-search>`,    | - System Config path: **Environment > Database**                                    |
| database search can be disabled from performing searches.                               | - ``config.json`` setting: ``SqlSettings`` > ``DisableDatabaseSearch`` > ``false``  |
|                                                                                         | - Environment variable: ``MM_SQLSETTINGS_DISABLEDATABASESEARCH``                    |
| - **true**: Disables the use of the database to perform                                 |                                                                                     |
|   searches. If another search engine isn't configured,                                  |                                                                                     |
|   setting this value to ``true`` will result in empty search                            |                                                                                     |
|   results.                                                                              |                                                                                     |
| - **false**: **(Default)** Database search isn't disabled.                              |                                                                                     |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

Search behavior in Mattermost depends on which search engines are enabled:

- When :doc:`Elasticsearch </administration-guide/scale/elasticsearch-setup>` or :doc:`AWS OpenSearch </administration-guide/scale/opensearch-setup>` is enabled, Mattermost will try to use it first.
- If Elasticsearch fails or is disabled, Mattermost will attempt to use Bleve search, if enabled. Bleve search has been deprecated in Mattermost v11.0. We recommend using Elasticsearch or OpenSearch for enterprise search capabilities.
- If these fail or are disabled, Mattermost tries to search the database directly, if this is enabled.
- If all of the above methods fail or are disabled, the search results will be empty.

.. note::

  Disabling this configuration setting in larger deployments may improve server performance in the following areas:

  - **Reduced Database Load**: When database search is enabled, every search query executed by users needs to interact with the database, leading to additional load on the database server. By disabling database search, you can avoid these queries, thereby reducing the database load.
  - **Improved Response Time**: Database searches can be time-consuming, especially with large datasets. Disabling database search can result in faster response times because the system no longer spends time fetching and processing search results from the database.
  - **Offloading Search to Indexing Services**: Disabling database search often means that searches are offloaded to specialized indexing services like Elasticsearch, which are optimized for search operations. These services can provide faster and more efficient search capabilities compared to traditional database searches.
  - **Lower Resource Consumption**: Running search queries directly against the database can be resource-intensive (using CPU and memory). With database search disabled, these resources can be allocated to other critical functions, improving overall system performance.
  - **Enhanced Scalability**: As the number of users and data volume grow, database search can become less efficient. Specialized search services are designed to scale more effectively, enhancing overall system scalability and performance.

  However, the ability to perform database searches in Mattermost is a critical feature for many users, particularly when other search engines aren't enabled. Disabling this feature will result in users seeing an error if they attempt to use the Mattermost Search box. It’s important to balance performance improvements with the needs of your organization and users.

Applied schema migrations
~~~~~~~~~~~~~~~~~~~~~~~~~

A list of all migrations that have been applied to the data store based on the version information available in the ``db_migrations`` table. Select **About Mattermost** from the Product |product-list| menu to review the current database schema version applied to your deployment.

.. config:setting:: active-search-backend
  :displayname: Active search backend (Database)
  :systemconsole: Environment > Database
  :configjson: N/A
  :environment: N/A
  :description: Read-only display of the currently active backend used for search.

Active search backend
~~~~~~~~~~~~~~~~~~~~~

Read-only display of the currently active backend used for search. Values can include ``none``, ``database``, ``elasticsearch``, or ``bleve``.

.. config:setting:: read-replicas
  :displayname: Read replicas (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.DataSourceReplicas
  :environment: MM_SQLSETTINGS_DATASOURCEREPLICAS
  :description: Specifies the connection strings for the read replica databases.

Read replicas
~~~~~~~~~~~~~

+--------------------------------------------------------+-------------------------------------------------------------------------------+
| Specifies the connection strings for the read replica  | - System Config path: N/A                                                     |
| databases.                                             | - ``config.json`` setting: ``SqlSettings`` > ``DataSourceReplicas`` > ``[]``  |
|                                                        | - Environment variable: ``MM_SQLSETTINGS_DATASOURCEREPLICAS``                 |
+--------------------------------------------------------+-------------------------------------------------------------------------------+

.. note::

  - Each database connection string in the array must be in the same form used for the `Data source <#data-source>`__ setting.
  - Space separate multiple read replicas in the array to allow Mattermost to load balance read queries across multiple database instances. For example, ``MM_SQLSETTINGS_DATASOURCEREPLICAS=dc-1 dc-2``

AWS High Availability RDS cluster deployments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For an AWS High Availability RDS cluster deployment, point this configuration setting directly to the underlying read-only node endpoint within the RDS cluster to circumvent the failover/load balancing that AWS/RDS takes care of (except for the write traffic). Mattermost has its own method of balancing the read-only connections and can also balance those queries to the data source/write+read connection should those nodes fail. See the :ref:`high availablility database configuration <administration-guide/scale/high-availability-cluster-based-deployment:database configuration>` documentation for details.

.. config:setting:: search-replicas
  :displayname: Search replicas (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.DataSourceSearchReplicas
  :environment: MM_SQLSETTINGS_DATASOURCESEARCHREPLICAS

  Specifies the connection strings for the search replica databases.
  A search replica is similar to a read replica, but is used only for handling search queries.

Search replicas
~~~~~~~~~~~~~~~

+--------------------------------------------------------+-------------------------------------------------------------------------------------+
| Specifies the connection strings for the search        | - System Config path: N/A                                                           |
| replica databases. A search replica is similar to a    | - ``config.json`` setting: ``SqlSettings`` > ``DataSourceSearchReplicas`` > ``[]``  |
| read replica, but is used only for handling search     | - Environment variable: ``MM_SQLSETTINGS_DATASOURCESEARCHREPLICAS``                 |
| queries.                                               |                                                                                     |
+--------------------------------------------------------+-------------------------------------------------------------------------------------+

.. note::

  Each database connection string in the array must be in the same form used for the `Data source <#data-source>`__ setting.

AWS High Availability RDS cluster deployments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For an AWS High Availability RDS cluster deployment, point this configuration setting directly to the underlying read-only node endpoint within the RDS cluster to circumvent the failover/load balancing that AWS/RDS takes care of (except for the write traffic). Mattermost has its own method of balancing the read-only connections and can also balance those queries to the data source/write+read connection should those nodes fail. See the :ref:`high availablility database configuration <administration-guide/scale/high-availability-cluster-based-deployment:database configuration>` documentation for details.

.. config:setting:: replica-lag-settings
  :displayname: Replica lag settings (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.ReplicaLagSettings
  :environment: MM_SQLSETTINGS_REPLICALAGSETTINGS
  :description: Specifies a connection string and user-defined SQL queries on the database to measure replica lag for a single replica instance.

Replica lag settings
~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+--------------------------------------------------------+----------------------------------------------------------------------------------+
| String array input specifies a connection string and   | - System Config path: N/A                                                        |
| user-defined SQL queries on the database to measure    | - ``config.json`` setting: ``SqlSettings`` > ``ReplicaLagSettings`` > ``[]``     |
| replica lag for a single replica instance.             | - Environment variable: ``MM_SQLSETTINGS_REPLICALAGSETTINGS``                    |
|                                                        |                                                                                  |
| These settings monitor absolute lag based on binlog    |                                                                                  |
| distance/transaction queue length, and the time taken  |                                                                                  |
| for the replica to catch up.                           |                                                                                  |
|                                                        |                                                                                  |
| String array input consists of:                        |                                                                                  |
|                                                        |                                                                                  |
| - ``DataSource``: The database credentials to connect  |                                                                                  |
|   to the database instance.                            |                                                                                  |
| - ``QueryAbsoluteLag``: A plain SQL query that must    |                                                                                  |
|   return a single row. The first column must be the    |                                                                                  |
|   node value of the Prometheus metric, and the second  |                                                                                  |
|   column must be the value of the lag used to          |                                                                                  |
|   measure absolute lag.                                |                                                                                  |
| - ``QueryTimeLag``: A plain SQL query that must        |                                                                                  |
|   return a single row. The first column must be the    |                                                                                  |
|   node value of the Prometheus metric, and the second  |                                                                                  |
|   column must be the value of the lag used to measure  |                                                                                  |
|   the time lag.                                        |                                                                                  |
+--------------------------------------------------------+----------------------------------------------------------------------------------+

.. note::

  - The ``QueryAbsoluteLag`` and ``QueryTimeLag`` queries must return a single row.
  - To properly monitor this, you must set up :doc:`performance monitoring </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>` for Mattermost.

1. Configure the replica lag metric based on your database type. See the following tabs for details on configuring this for each database type.

  .. tab:: AWS Aurora

    Add the configuration highlighted below to your ``SqlSettings.ReplicaLagSettings`` array. You only need to add this once because replication statistics for AWS Aurora nodes are visible across all server instances that are members of the cluster. Be sure to change the ``DataSource`` to point to a single node in the group.

    For more information on Aurora replication stats, see the `AWS Aurora documentaion <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_global_db_instance_status.html>`__.

    Example

    .. code-block:: json
      :emphasize-lines: 4,5,6,7,8

      {
        "SqlSettings": {
            "ReplicaLagSettings": [
              {
                  "DataSource": "replica-1",
                  "QueryAbsoluteLag": "select server_id, highest_lsn_rcvd-durable_lsn as bindiff from aurora_global_db_instance_status() where server_id=<>",
                  "QueryTimeLag": "select server_id, visibility_lag_in_msec from aurora_global_db_instance_status() where server_id=<>"
              }
            ]
        }
      }

  .. tab:: MySQL Group Replication

    Add the configuration highlighted below to your ``SqlSettings.ReplicaLagSettings`` array. You only need to add this once because replication statistics for all nodes are shared across all server instances that are members of the MySQL replication group. Be sure to change the ``DataSource`` to point to a single node in the group.

    For more information on group replication stats, see the `MySQL documentation <https://dev.mysql.com/doc/refman/8.0/en/group-replication-replication-group-member-stats.html>`__.

    Example

    .. code-block:: json
      :emphasize-lines: 4,5,6,7,8

      {
        "SqlSettings": {
            "ReplicaLagSettings": [
              {
                  "DataSource": "replica-1",
                  "QueryAbsoluteLag": "select member_id, count_transactions_remote_in_applier_queue FROM performance_schema.replication_group_member_stats where member_id=<>",
                  "QueryTimeLag": ""
              }
            ]
        }
      }

  .. tab:: PostgreSQL replication slots

    1. Add the configuration highlighted below to your ``SqlSettings.ReplicaLagSettings`` array. This query should run against the **primary** node in your cluster, to do this change the ``DataSource`` to match the `SqlSettings.DataSource <#data-source>`__ setting you have configured.

    For more information on pg_stat_replication, see the `PostgreSQL documentation <https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STAT-REPLICATION-VIEW>`__.

        **Example:**

        .. code-block:: json
          :emphasize-lines: 4,5,6,7,8

          {
            "SqlSettings": {
                "ReplicaLagSettings": [
                  {
                      "DataSource": "postgres://mmuser:password@localhost:5432/mattermost_test?sslmode=disable&connect_timeout=10.",
                      "QueryAbsoluteLag": "select usename, pg_wal_lsn_diff(pg_current_wal_lsn(),replay_lsn) as metric from pg_stat_replication;",
                      "QueryTimeLag": ""
                  }
                ]
            }
          }

    2. Grant permissions to the database user for ``pg_monitor``. This user should be the same user configured above in the ``DataSource`` string.

      For more information on roles, see the `PostgreSQL documentation <https://www.postgresql.org/docs/10/default-roles.html>`__.

      .. code-block:: sh

        sudo -u postgres psql
        postgres=# GRANT pg_monitor TO mmuser;

2. Save the config and restart all Mattermost nodes.
3. Navigate to your Grafana instance monitoring Mattermost and open the `Mattermost Performance Monitoring v2 <https://grafana.com/grafana/dashboards/15582-mattermost-performance-monitoring-v2/>`_ dashboard.
4. The ``QueryTimeLag`` chart is already setup for you utilizing the existing ``Replica Lag`` chart. If using ``QueryAbsoluteLag`` metric clone the ``Replica Lag`` chart and edit the query to use the below absolute lag metrics and modify the title to be ``Replica Lag Absolute``.

  .. code-block:: text

    mattermost_db_replica_lag_abs{instance=~"$server"}

  .. image::  ../../images/database-configuration-settings-replica-lag-grafana-1.jpg
    :alt: A screenshot showing how to clone a chart within Grafana


  .. image:: ../../images/database-configuration-settings-replica-lag-grafana-2.jpg
    :alt: A screenshot showing the specific edits to make to the cloned grafana chart.


.. config:setting:: replica-monitor-interval-seconds
  :displayname: Replica monitor interval (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.ReplicaMonitorIntervalSeconds
  :environment: MM_SQLSETTINGS_REPLICAMONITORINTERVALSECONDS

  Specifies how frequently unhealthy replicas will be monitored for liveness check. Mattermost will dynamically choose a replica if it's alive.

Replica monitor interval (seconds)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Specifies how frequently unhealthy replicas will be    | - System Config path: N/A                                                               |
| monitored for liveness check. Mattermost will          | - ``config.json`` setting: ``SqlSettings`` > ``ReplicaMonitorIntervalSeconds`` > ``5``  |
| dynamically choose a replica if it's alive.            | - Environment variable: ``MM_SQLSETTINGS_REPLICAMONITORINTERVALSECONDS``                |
|                                                        |                                                                                         |
| Numerical input. Default is 5 seconds.                 |                                                                                         |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. note::

  This configuration setting is applicable to self-hosted deployments only.

----

Enterprise search
-----------------

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

Core database search happens in a relational database and is intended for deployments under about 2–3 million posts and file entries. Beyond that scale, enabling enterprise search with Elasticsearch or AWS OpenSearch is highly recommended for optimum search performance before reaching 3 million posts.

For self-hosted deployments with over 3 million posts, Elasticsearch or AWS OpenSearch is required to avoid significant performance issues, such as timeouts, with :doc:`message searches </end-user-guide/collaborate/search-for-messages>` and :doc:`@mentions </end-user-guide/collaborate/mention-people>`.

You can configure Mattermost enterprise search by going to **System Console > Environment > Elasticsearch**. The following configuration settings apply to both Elasticsearch and AWS OpenSearch. You can also edit the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: enable-elasticsearch-indexing
  :displayname: Enable Elasticsearch indexing (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.EnableIndexing
  :environment: MM_ELASTICSEARCHSETTINGS_ENABLEINDEXING
  :description: Configure Mattermost to index new posts automatically.

  - **true**: Indexing of new posts occurs automatically.
  - **false**: **(Default)** Elasticsearch indexing is disabled and new messages aren't indexed.

Enable Elasticsearch indexing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Configure Mattermost to index new posts automatically.        | - System Config path: **Environment > Elasticsearch**                                 |
|                                                               | - ``config.json`` setting: ``ElasticsearchSettings`` > ``EnableIndexing`` > ``false`` |
| - **true**: Indexing of new messages occurs automatically.    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_ENABLEINDEXING``                   |
| - **false**: **(Default)** Indexing of new messages is        |                                                                                       |
|   disabled, and new messages aren't indexed.                  |                                                                                       |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------+

.. note::

  If indexing is disabled and then re-enabled after an index is created, purge and rebuild the index to ensure complete search results.

.. config:setting:: backend-type
  :displayname: Elasticsearch backend type (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.Backend
  :environment: MM_ELASTICSEARCHSETTINGS_BACKEND
  :description: Set the type of search backend as either Elasticsearch or AWS OpenSearch.

Backend type
~~~~~~~~~~~~~

Both :doc:`Elasticsearch </administration-guide/scale/elasticsearch-setup>` and :doc:`AWS OpenSearch </administration-guide/scale/opensearch-setup>` provide enterprise-scale deployments with optimized search performance and prevents performance degradation and timeouts. Learn more about :doc:`enterprise search </administration-guide/scale/enterprise-search>` in our product documentation.

+----------------------------------------------------+--------------------------------------------------------------------------------------------+
| The type of search backend.                        | - System Config path: **Environment > Elasticsearch**                                      |
|                                                    | - ``config.json`` setting: ``ElasticsearchSettings`` > ``Backend`` > ``"elasticsearch"``   |
| - ``elasticsearch`` - (**Default**)                | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_BACKEND``                               |
| - ``opensearch`` - Required for AWS OpenSearch.    |                                                                                            |
+----------------------------------------------------+--------------------------------------------------------------------------------------------+

Learn more about :ref:`enterprise search version support <administration-guide/scale/enterprise-search:supported paths>`.

.. config:setting:: server-connection-address
  :displayname: Server connection address (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.ConnectionUrl
  :environment: MM_ELASTICSEARCHSETTINGS_CONNECTIONURL
  :description: The address of the Elasticsearch or AWS OpenSearch server.

Server connection address
~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+--------------------------------------------------------------------------+
| The address of the Elasticsearch or AWS            | - System Config path: **Environment > Elasticsearch**                    |
| OpenSearch server.                                 | - ``config.json`` setting: ``ElasticsearchSettings`` > ``ConnectionUrl`` |
|                                                    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CONNECTIONURL``       |
+----------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: ca-path
  :displayname: CA path (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.CA
  :environment: MM_ELASTICSEARCHSETTINGS_CA
  :description: Optional path to the Custom Certificate Authority certificates for the Elasticsearch or AWS OpenSearch server.

CA path
~~~~~~~

+----------------------------------------------------+--------------------------------------------------------------------------+
| Optional path to the Custom Certificate Authority  | - System Config path: **Environment > Elasticsearch**                    |
| certificates for the Elasticsearch or AWS          | - ``config.json`` setting: ``ElasticsearchSettings`` > ``CA``            |
| OpenSearch server.                                 | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CA``                  |
+----------------------------------------------------+--------------------------------------------------------------------------+

.. note::

  - Available from Mattermost v7.8. The certificate path should be ``/opt/mattermost/data/elasticsearch/`` or ``/opt/mattermost/data/opensearch`` and configured in the System Console as ``./elasticsearch/cert.pem`` or ``./opensearch/cert.pem``.
  - Can be used in conjunction with basic authentication credentials or can replace them. Leave this setting blank to use the default Certificate Authority certificates for the operating system.

.. config:setting:: client-certificate-path
  :displayname: Client certificate path (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.ClientCert
  :environment: MM_ELASTICSEARCHSETTINGS_CLIENTCERT
  :description: Optional client certificate for the connection to the Elasticsearch or AWS OpenSearch server in PEM format.

Client certificate path
~~~~~~~~~~~~~~~~~~~~~~~

Available from Mattermost v7.8. Can be used in conjunction with basic auth credentials or to replace them.

+----------------------------------------------------+--------------------------------------------------------------------------+
| Optional client certificate for the connection to  | - System Config path: **Environment > Elasticsearch**                    |
| the Elasticsearch or AWS OpenSearch server in      | - ``config.json`` setting: ``ElasticsearchSettings`` > ``ClientCert``    |
| the PEM format.                                    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CLIENTCERT``          |
+----------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: client-certificate-key-path
  :displayname: Client certificate key path (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.ClientKey
  :environment: MM_ELASTICSEARCHSETTINGS_CLIENTKEY
  :description: Optional key for the client certificate in PEM format.

Client certificate key path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Available from Mattermost v7.8. Can be used in conjunction with basic auth credentials or to replace them.

+----------------------------------------------------+--------------------------------------------------------------------------+
| Optional key for the client certificate in the PEM | - System Config path: **Environment > Elasticsearch**                    |
| format.                                            | - ``config.json`` setting: ``ElasticsearchSettings`` > ``ClientKey``     |
|                                                    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CLIENTKEY``           |
+----------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: skip-tls-verification
  :displayname: Skip TLS verification (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.SkipTLSVerification
  :environment: MM_ELASTICSEARCHSETTINGS_SKIPTLSVERIFICATION
  :description: The certificate step for TLS connections can be skipped.

  - **true**: Skips the certificate verification step for TLS connections.
  - **false**: **(Default)** Mattermost does not skip certificate verification.

Skip TLS verification
~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| The certificate step for TLS connections can be skipped.      | - System Config path: **Environment > Elasticsearch**                                      |
|                                                               | - ``config.json`` setting: ``ElasticsearchSettings`` > ``SkipTLSVerification`` > ``false`` |
| - **true**: Skips the certificate verification step for       | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_SKIPTLSVERIFICATION``                   |
|   TLS connections.                                            |                                                                                            |
| - **false**: **(Default)** Mattermost requires                |                                                                                            |
|   certificate verification.                                   |                                                                                            |
+---------------------------------------------------------------+--------------------------------------------------------------------------------------------+

.. config:setting:: server-username
  :displayname: Server username (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.UserName
  :environment: MM_ELASTICSEARCHSETTINGS_USERNAME
  :description: (Optional) The username to authenticate to the Elasticsearch or AWS OpenSearch server.

Server username
~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| (Optional) The username to authenticate to the                | - System Config path: **Environment > Elasticsearch**                    |
| Elasticsearch or AWS OpenSearch server.                       | - ``config.json`` setting: ``ElasticsearchSettings`` > ``UserName``      |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_USERNAME``            |
| String input.                                                 |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: server-password
  :displayname: Server password (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.Password
  :environment: MM_ELASTICSEARCHSETTINGS_PASSWORD
  :description: (Optional) The password to authenticate to the Elasticsearch or AWS OpenSearch server.

Server password
~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| (Optional) The password to authenticate to the                | - System Config path: **Environment > Elasticsearch**                    |
| Elasticsearch or AWS OpenSearch server.                       | - ``config.json`` setting: ``ElasticsearchSettings`` > ``Password``      |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_PASSWORD``            |
| String input.                                                 |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: enable-cluster-sniffing
  :displayname: Enable cluster sniffing (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.Sniff
  :environment: MM_ELASTICSEARCHSETTINGS_SNIFF
  :description: Configure Mattermost to automatically find and connect to all data nodes in a cluster.

  - **true**: Sniffing finds and connects to all data nodes in your cluster automatically.
  - **false**: **(Default)** Cluster sniffing is disabled.

Enable cluster sniffing
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+---------------------------------------------------------------------------------+
| Configure Mattermost to automatically find and connect to      | - System Config path: **Environment > Elasticsearch**                           |
| all data nodes in a cluster.                                   | - ``config.json`` setting: ``ElasticsearchSettings`` > ``Sniff`` > ``false``    |
|                                                                | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_SNIFF``                      |
| - **true**: Sniffing finds and connects to all data nodes      |                                                                                 |
|   in your cluster automatically.                               |                                                                                 |
| - **false**: **(Default)** Cluster sniffing is disabled.       |                                                                                 |
+----------------------------------------------------------------+---------------------------------------------------------------------------------+

Select the **Test Connection** button in the System Console to validate the connection between Mattermost and the Elasticsearch or AWS OpenSearch server.

.. config:setting:: bulk-indexing
  :displayname: Bulk indexing (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: N/A
  :environment: N/A
  :description: Configure Mattermost to start a bulk index of all existing posts in the database by selecting Index Now.

Bulk indexing
~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Configure Mattermost to start a bulk index of all existing    | - System Config path: **Environment > Elasticsearch**                    |
| posts in the database, from oldest to newest.                 | - ``config.json`` setting: N/A                                           |
|                                                               | - Environment variable: N/A                                              |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. note::

  - Always `purge indexes <#purge-indexes>`__ before bulk indexing.
  - Select the **Index Now** button in the System Console to start a bulk index of all posts, and review all index jobs in progress.
  - Elasticsearch or AWS OpenSearch is available during indexing, but search results may be incomplete until the indexing job is complete.
  - If an in-progress indexing job is canceled, the index and search results will be incomplete.

.. config:setting:: rebuild-channels-index
  :displayname: Rebuild channels index (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: N/A
  :environment: N/A
  :description: Purge the channels index adn re-index all channels in the database, from oldest to newest.

Rebuild channels index
~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------+
| Purge the channels index adn re-index all channels in the     | - System Config path: **Environment > Elasticsearch**         |
| database, from oldest to newest.                              | - ``config.json`` setting: N/A                                |
|                                                               | - Environment variable: N/A                                   |
+---------------------------------------------------------------+---------------------------------------------------------------+

Select the **Rebuild Channels Index** button in the System Console to purge the channels index. Ensure no other indexing jobs are in progress via the **Bulk Indexing** table before starting this process. During indexing, channel auto-complete is available, but search results may be incomplete until the indexing job is complete.

.. config:setting:: purge-indexes
  :displayname: Purge indexes (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: N/A
  :environment: N/A
  :description: Purge the entire Elasticsearch or AWS OpenSearch index by selecting Purge Indexes before creating a new index.

Purge indexes
~~~~~~~~~~~~~

+-------------------------------------------+-------------------------------------------------------------+
| Purge the entire Elasticsearch index.     | - System Config path: **Environment > Elasticsearch**       |
|                                           | - ``config.json`` setting: N/A                              |
|                                           | - Environment variable: N/A                                 |
+-------------------------------------------+-------------------------------------------------------------+

Select the **Purge Indexes** button in the System Console to purge the index. After purging the index, create a new index by selecting the **Index Now** button.

.. config:setting:: indexes-to-skip-while-purging
  :displayname: Indexes to skip while purging (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.IgnoredPurgeIndexes
  :environment: MM_ELASTICSEARCHSETTINGS_IGNOREDPURGEINDEXES
  :description: Specify index names to ignore while purging indexes, separated by commas.

Indexes to skip while purging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------------------------+
| Specify index names to ignore while purging indexes.          | - System Config path: **Environment > Elasticsearch**                           |
| Separate multiple index names with commas.                    | - ``config.json`` setting: ``ElasticsearchSettings`` > ``IgnoredPurgeIndexes``  |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_IGNOREDPURGEINDEXES``        |
| Use an asterisk (*) to match a sequence of index name         |                                                                                 |
| characters.                                                   |                                                                                 |
+---------------------------------------------------------------+---------------------------------------------------------------------------------+

.. config:setting:: enable-elasticsearch-for-search-queries
  :displayname: Enable Elasticsearch for search queries (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.EnableSearching
  :environment: MM_ELASTICSEARCHSETTINGS_ENABLESEARCHING
  :description: Configure Mattermost to use Elasticsearch or AWS OpenSearch for all search queries using the latest index.

  - **true**: Elasticsearch or AWS OpenSearch is used for all search queries using the latest index. Search results may be incomplete until a bulk index of the existing message database is completed.
  - **false**: **(Default)** Relational database search is used for search queries.

Enable Elasticsearch for search queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Configure Mattermost to use Elasticsearch or AWS OpenSearch   | - System Config path: **Environment > Elasticsearch**                                  |
| for all search queries using the latest index.                | - ``config.json`` setting: ``ElasticsearchSettings`` > ``EnableSearching`` > ``false`` |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_ENABLESEARCHING``                   |
| - **true**: Elasticsearch or AWS OpenSearch is used for all   |                                                                                        |
|   search queries using the latest index. Search results may   |                                                                                        |
|   be incomplete until a bulk index of the existing message    |                                                                                        |
|   database is completed.                                      |                                                                                        |
| - **false**: **(Default)** Database search is used for        |                                                                                        |
|   search queries.                                             |                                                                                        |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------+

If indexing is disabled and then re-enabled after an index is created, purge and rebuild the index to ensure complete search results.

.. config:setting:: enable-elasticsearch-for-autocomplete-queries
  :displayname: Enable Elasticsearch for autocomplete queries (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.EnableAutocomplete
  :environment: MM_ELASTICSEARCHSETTINGS_ENABLEAUTOCOMPLETE
  :description: Configure Mattermost to use Elasticsearch for all autocompletion queries on users and channels using the latest index.

  - **true**: Elasticsearch will be used for all autocompletion queries on users and channels using the latest index.
  - **false**: **(Default)** Database autocomplete is used.

Enable Elasticsearch for autocomplete queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| Configure Mattermost to use Elasticsearch or AWS OpenSearch   | - System Config path: **Environment > Elasticsearch**                                     |
| for all autocompletion queries on users and channels using    | - ``config.json`` setting: ``ElasticsearchSettings`` > ``EnableAutocomplete`` > ``false`` |
| the latest index.                                             | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_ENABLEAUTOCOMPLETE``                   |
|                                                               |                                                                                           |
| - **true**: Elasticsearch or AWS OpenSearch will be used for  |                                                                                           |
|   all autocompletion queries on users and channels using the  |                                                                                           |
|   latest index.                                               |                                                                                           |
| - **false**: **(Default)** Database autocomplete is used.     |                                                                                           |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------+

Autocompletion results may be incomplete until a bulk index of the existing users and channels database is finished.

.. config:setting:: post-index-replicas
  :displayname: Post index replicas (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.PostIndexReplicas
  :environment: MM_ELASTICSEARCHSETTINGS_POSTINDEXREPLICAS
  :description: The number of replicas to use for each post index. Default is **1**.

Post index replicas
~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------------------+
| The number of replicas to use for each post index.            | - System Config path: N/A                                                            |
|                                                               | - ``config.json`` setting: ``ElasticsearchSettings`` > ``PostIndexReplicas`` > ``1`` |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_POSTINDEXREPLICAS``               |
+---------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. note::

  - If this setting is changed, the changed configuration only applies to newly-created indexes. To apply the change to existing indexes, purge and rebuild the index after changing this setting.
  - If there are ``n`` data nodes, the number of replicas per shard for each index should be ``n-1``.
  - If the number of nodes in an Elasticsearch or AWS OpenSearch cluster changes, this configuration setting, as well as `Channel Index Replicas <#channel-index-replicas>`__ and `User Index Replicas <#user-index-replicas>`__ must also be updated accordingly.

.. config:setting:: post-index-shards
  :displayname: Post index shards (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.PostIndexShards
  :environment: MM_ELASTICSEARCHSETTINGS_POSTINDEXSHARDS
  :description: The number of shards to use for each post index. Default is **1**.

Post index shards
~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------------------+
| The number of shards to use for each post index.              | - System Config path: N/A                                                            |
|                                                               | - ``config.json`` setting: ``ElasticsearchSettings`` > ``PostIndexShards`` > ``1``   |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_POSTINDEXSHARDS``                 |
+---------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. note::

  If this configuration setting is changed, the changed configuration only applies to newly-created indexes. To apply the change to existing indexes, purge and rebuild the index after changing this setting.

.. config:setting:: channel-index-replicas
  :displayname: Channel index replicas (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.ChannelIndexReplicas
  :environment: MM_ELASTICSEARCHSETTINGS_CHANNELINDEXREPLICAS
  :description: The number of replicas to use for each channel index. Default is **1**.

Channel index replicas
~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| The number of replicas to use for each channel index.         | - System Config path: N/A                                                               |
|                                                               | - ``config.json`` setting: ``ElasticsearchSettings`` > ``ChannelIndexReplicas`` > ``1`` |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CHANNELINDEXREPLICAS``               |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. note::

  If there are ``n`` data nodes, the number of replicas per shard for each index should be ``n-1``. If the number of nodes in an Elasticsearch or AWS OpenSearch cluster changes, this configuration setting, as well as `Post Index Replicas <#post-index-shards>`__ and `User Index Replicas <#user-index-replicas>`__ must also be updated accordingly.

.. config:setting:: channel-index-shards
  :displayname: Channel index shards (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.ChannelIndexShards
  :environment: MM_ELASTICSEARCHSETTINGS_CHANNELINDEXSHARDS
  :description: The number of shards to use for each channel index. Default is **1**.

Channel index shards
~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| The number of shards to use for each channel index.           | - System Config path: N/A                                                               |
|                                                               | - ``config.json`` setting: ``ElasticsearchSettings`` > ``ChannelIndexShards`` > ``1``   |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CHANNELINDEXSHARDS``                 |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. config:setting:: user-index-replicas
  :displayname: User index replicas (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.UserIndexReplicas
  :environment: MM_ELASTICSEARCHSETTINGS_USERINDEXREPLICAS
  :description: The number of replicas to use for each user index. Default is **1**.

User index replicas
~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------------------+
| The number of replicas to use for each user index.            | - System Config path: N/A                                                            |
|                                                               | - ``config.json`` setting: ``ElasticsearchSettings`` > ``UserIndexReplicas`` > ``1`` |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_USERINDEXREPLICAS``               |
+---------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. note::

  If there are ``n`` data nodes, the number of replicas per shard for each index should be ``n-1``. If the number of nodes in an Elasticsearch or AWS OpenSearch cluster changes, this configuration setting, as well as `Post Index Replicas <#post-index-shards>`__ and `User Index Replicas <#user-index-replicas>`__ must also be updated accordingly.

.. config:setting:: user-index-shards
  :displayname: User index shards (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.UserIndexShards
  :environment: MM_ELASTICSEARCHSETTINGS_USERINDEXSHARDS
  :description: The number of shards to use for each user index. Default is **1**.

User index shards
~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-------------------------------------------------------------------------------------+
| The number of shards to use for each user index.              | - System Config path: N/A                                                           |
|                                                               | - ``config.json`` setting: ``ElasticsearchSettings`` > ``UserIndexShards`` > ``1``  |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_USERINDEXSHARDS``                |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------+

.. config:setting:: aggregate-search-indexes
  :displayname: Aggregate search indexes (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.AggregatePostsAfterDays
  :environment: MM_ELASTICSEARCHSETTINGS_AGGREGATEPOSTSAFTERDAYS
  :description: Elasticsearch or AWS OpenSearch indexes older than the age specified by this setting, in days, will be aggregated during the daily scheduled job. Default is **365** days.

Aggregate search indexes
~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Elasticsearch or AWS OpenSearch indexes older than the age    | - System Config path: N/A                                                                     |
| specified by this setting, in days, will be aggregated during | - ``config.json`` setting: ``ElasticsearchSettings`` > ``AggregatePostsAfterDays`` > ``365``  |
| the daily scheduled job.                                      | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_AGGREGATEPOSTSAFTERDAYS``                  |
|                                                               |                                                                                               |
| Numerical input. Default is **365** days.                     |                                                                                               |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------+

.. note::

  If you’re using :doc:`data retention </administration-guide/comply/data-retention-policy>` and :doc:`enterprise search </administration-guide/scale/enterprise-search>`, configure this with a value greater than your data retention policy.

.. config:setting:: post-aggregator-start-time
  :displayname: Post aggregator start time (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.PostsAggregatorJobStartTime
  :environment: MM_ELASTICSEARCHSETTINGS_POSTSAGGREGATORJOBSTARTTIME
  :description: The start time of the daily scheduled aggregator job. Must be a 24-hour time stamp in the form ``HH:MM`` based on the local time of the server. Default is **03:00** (3 AM).

Post aggregator start time
~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| The start time of the daily scheduled aggregator job.         | - System Config path: N/A                                                                            |
|                                                               | - ``config.json`` setting: ``ElasticsearchSettings`` > ``PostsAggregatorJobStartTime`` > ``"03:00"`` |
| Must be a 24-hour time stamp in the form ``HH:MM`` based on   | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_POSTSAGGREGATORJOBSTARTTIME``                     |
| the local time of the server.                                 |                                                                                                      |
|                                                               |                                                                                                      |
| Default is **03:00** (3 AM)                                   |                                                                                                      |
+---------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

.. config:setting:: index-prefix
  :displayname: Index prefix (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.IndexPrefix
  :environment: MM_ELASTICSEARCHSETTINGS_INDEXPREFIX
  :description: The prefix added to the Elasticsearch or AWS OpenSearch index name.

Index prefix
~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The prefix added to the Elasticsearch or AWS OpenSearch       | - System Config path: N/A                                                |
| index name.                                                   | - ``config.json`` setting: ``ElasticsearchSettings`` > ``IndexPrefix``   |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_INDEXPREFIX``         |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. note::

  When this setting is used, all Elasticsearch or AWS OpenSearch indexes created by Mattermost are given this prefix. You can set different prefixes so that multiple Mattermost deployments can share an Elasticsearch or AWS OpenSearch cluster without the index names colliding.

.. config:setting:: global-search-prefix
  :displayname: Global search prefix (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.GlobalSearchPrefix
  :environment: MM_ELASTICSEARCHSETTINGS_GLOBALSEARCHPREFIX
  :description: Enable global search across multiple Elasticsearch indices with the same index prefix.

Global search prefix
~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| Enable global search across multiple Elasticsearch indices    | - System Config path: N/A                                                     |
| with the same `index prefix <#index-prefix>`__.               | - ``config.json`` setting: ``ElasticsearchSettings`` > ``GlobalSearchPrefix`` |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_GLOBALSEARCHPREFIX``       |
| This is helpful for setups with multiple data centers where   |                                                                               |
| Elasticsearch instances share data using cross-cluster        |                                                                               |
| replication. It allows for easier and unified searching       |                                                                               |
| across distributed indices.                                   |                                                                               |
|                                                               |                                                                               |
| Value must be a prefix of ``IndexPrefix``.                    |                                                                               |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

.. config:setting:: live-indexing-batch-size
  :displayname: Live indexing batch size (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.LiveIndexingBatchSize
  :environment: MM_ELASTICSEARCHSETTINGS_LIVEINDEXINGBATCHSIZE
  :description: The number of new posts batched together before they're added to the Elasticsearch or AWS OpenSearch index. Default is **1**.

Live indexing batch size
~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+------------------------------------------------------------------------------------------+
| The number of new posts needed before those posts are added   | - System Config path: N/A                                                                |
| to the Elasticsearch or AWS OpenSearch index. Once added to   | - ``config.json`` setting: ``ElasticsearchSettings`` > ``LiveIndexingBatchSize`` > ``1`` |
| the index, the post becomes searchable.                       | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_LIVEINDEXINGBATCHSIZE``               |
|                                                               |                                                                                          |
| On servers with more than 1 post per second, we suggest       |                                                                                          |
| setting this value to the average number of  posts over a     |                                                                                          |
| 20 second period of time.                                     |                                                                                          |
|                                                               |                                                                                          |
| Numerical input. Default is **1**. Every post is indexed      |                                                                                          |
| synchronously as they are created.                            |                                                                                          |
+---------------------------------------------------------------+------------------------------------------------------------------------------------------+

.. note::

  It may be necessary to increase this value to avoid hitting the rate limit or resource limit of your Elasticsearch or AWS OpenSearch cluster on installs handling more than 1 post per second.

**What exactly happens when I increase this value?**

The primary impact is that a post will be indexed into Elasticsearch or AWS OpenSearch after the threshold of posts is met, which then makes the posts searchable within Mattermost. So, if you set this based on recommendations for larger servers, and you make a post, you cannot find it via search for ~10–20 seconds, on average. Realistically, no users should see or feel this impact due to the limited number of users who are actively **searching** for a post this quickly. You can set this value to a lower or higher average depending on your Elasticsearch or AWS OpenSearch server specifications.

During busy periods, this delay will be faster as more traffic is occurring, causing more posts and a quicker time to hit the index number. During slower periods, expect the reverse.

**How to find the right number for your server**

1. You must understand how many posts your server makes every minute. Run the query below to calculate your server's average posts per minute.

    Note that this query can be heavy, so we recommend that you run it during non-peak hours.
    Additionally, you can adjust the ``WHERE`` clause to see the posts per minute over a different time period. Right now ``31536000000`` represents the number of milliseconds in a year.

    .. code-block:: SQL

      SELECT
        AVG(postsPerMinute) as averagePostsPerMinute
      FROM (
        SELECT
          count(*) as postsPerMinute,
          date_trunc('minute', to_timestamp(createat/1000))
        FROM posts
        WHERE createAt > ( (extract(epoch from now()) * 1000 )  - 31536000000)
        GROUP BY date_trunc('minute', to_timestamp(createat/1000))
      ) as ppm;

2. Decide the acceptable index window for your environment, and divide your average posts per minute by that. We suggest 10-20 seconds. Assuming you have ``600`` posts per minute on average, and you want to index every 20 seconds (``60 seconds / 20 seconds = 3```) you would calculate ``600 / 3`` to come to the number ``200``. After 200 posts, Mattermost will index the posts into Elasticsearch or AWS OpenSearch. So, on average, there would be a 20-second delay in searchability.

3. Edit the ``config.json`` or run mmctl to modify the ``LiveIndexingBatchSize`` setting

    **In the ``config.json``**

    .. code-block:: JSON

      {
        "ElasticsearchSettings": {
          "LiveIndexingBatchSize": 200
        }
      }

    **Via mmctl**

    .. code-block:: sh

      mmctl config set ElasticsearchSettings.LiveIndexingBatchSize 200

    **Via an environment variable**

    .. code-block:: sh

      MM_ELASTICSEARCHSETTINGS_LIVEINDEXINGBATCHSIZE = 200

4. Restart the Mattermost server.

.. config:setting:: batch-size
  :displayname: Batch size (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.BatchSize
  :environment: MM_ELASTICSEARCHSETTINGS_BATCHSIZE
  :description: The number of posts for a single batch during a bulk indexing job. Default is **10000**.

Batch size
~~~~~~~~~~~

+-------------------------------------------+----------------------------------------------------------------------------------+
| The number of posts for a single batch    | - System Config path: N/A                                                        |
| during a bulk indexing job.               | - ``config.json`` setting: ``ElasticsearchSettings`` > ``BatchSize`` > ``10000`` |
|                                           | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_BATCHSIZE``                   |
| Numerical input. Default is **10000**.    |                                                                                  |
+-------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: request-timeout
  :displayname: Request timeout (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.RequestTimeoutSeconds
  :environment: MM_ELASTICSEARCHSETTINGS_REQUESTTIMEOUTSECONDS
  :description: The timeout, in seconds, for Elasticsearch or AWS OpenSearch calls. Default is **30** seconds.

Request timeout
~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| The timeout, in seconds, for Elasticsearch or AWS OpenSearch  | - System Config path: N/A                                                                 |
| calls.                                                        | - ``config.json`` setting: ``ElasticsearchSettings`` > ``RequestTimeoutSeconds`` > ``30`` |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_REQUESTTIMEOUTSECONDS``                |
| Numerical input in seconds. Default is **30** seconds.        |                                                                                           |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------+

.. config:setting:: trace
  :displayname: Trace (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.Trace
  :environment: MM_ELASTICSEARCHSETTINGS_TRACE
  :description: Options for printing Elasticsearch or AWS OpenSearch trace errors.

  - **error**: Creates the error trace when initializing the Elasticsearch or AWS OpenSearch client and prints any template creation or search query that returns an error as part of the error message.
  - **all**: Creates the three traces (error, trace and info) for the driver and doesn’t print the queries because they will be part of the trace log level of the driver.
  - **not specified**: **(Default)** No error trace is created.

Trace
~~~~~

+---------------------------------------------------------------------+--------------------------------------------------------------------------+
| Options for printing Elasticsearch or AWS OpenSearch trace errors.  | - System Config path: N/A                                                |
|                                                                     | - ``config.json`` setting: ``ElasticsearchSettings`` > ``Trace``         |
| - **error**: Creates the error trace when initializing              | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_TRACE``               |
|   the Elasticsearch or AWS OpenSearch client and prints any         |                                                                          |
|   template creation or search query that returns an error as part   |                                                                          |
|   of the error message.                                             |                                                                          |
| - **all**: Creates the three traces (error, trace and info)         |                                                                          |
|   for the driver and doesn’t print the queries because they         |                                                                          |
|   will be part of the trace log level of the driver.                |                                                                          |
| - **not specified**: **(Default)** No error trace is created.       |                                                                          |
+---------------------------------------------------------------------+--------------------------------------------------------------------------+

----

File storage
------------

With self-hosted deployments, you can configure file storage settings by going to **System Console > Environment > File Storage**, or by editing the ``config.json`` file as described in the following tables.

.. note::

  Mattermost currently supports storing files on the local filesystem and Amazon S3 or S3-compatible containers. We have tested Mattermost with `Digital Ocean Spaces <https://docs.digitalocean.com/products/spaces/>`__, but not all S3-compatible containers on the market. If you are looking to use other S3-compatible containers, we recommend completing your own testing. You can also use local storage or a network drive using NFS.

.. config:setting:: file-storage-system
  :displayname: File storage system (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.DriverName
  :environment: MM_FILESETTINGS_DRIVERNAME
  :description: The type of file storage system used.

  - **local**: **(Default)** Files and images are stored in the specified local file directory.
  - **amazons3**: Files and images are stored on Amazon S3 based on the access key, bucket, and region fields provided.

File storage system
~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------+
| The type of file storage system used.                         | - System Config path: **Environment > File Storage**                        |
| Can be either Local File System or Amazon S3.                 | - ``config.json`` setting: ``FileSettings`` > ``DriverName`` > ``"local"``  |
|                                                               | - Environment variable: ``MM_FILESETTINGS_DRIVERNAME``                      |
| - **local**: **(Default)** Files and images are stored in     |                                                                             |
|   the specified local file directory.                         |                                                                             |
| - **amazons3**: Files and images are stored on Amazon S3      |                                                                             |
|   based on the access key, bucket, and region fields          |                                                                             |
|   provided. The driver is compatible with other S3-compatible |                                                                             |
|   services, such as Digital Ocean Spaces.                     |                                                                             |
+---------------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: local-storage-directory
  :displayname: Local storage directory (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.Directory
  :environment: MM_FILESETTINGS_DIRECTORY
  :description: The local directory to which files are written when the **File storage system** is set to **local**. Default value is **./data/**.

Local storage directory
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The local directory to which files are written when the       | - System Config path: **Environment > File Storage**                     |
| **File storage system** is set to **local**.                  | - ``config.json`` setting: ``FileSettings`` > ``Directory``              |
| Can be any directory writable by the user Mattermost is       | - Environment variable: ``MM_FILESETTINGS_DIRECTORY``                    |
| running as, and is relative to the directory where            |                                                                          |
| Mattermost is installed.                                      |                                                                          |
|                                                               |                                                                          |
| Defaults to **./data/**.                                      |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

When **File storage system** is set to **amazons3**, this setting has no effect.

.. config:setting:: maximum-file-size
  :displayname: Maximum file size (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.MaxFileSize
  :environment: MM_FILESETTINGS_MAXFILESIZE
  :description: The maximum file size, in bytes, for message attachments and plugin uploads. Default value is **104857600** bytes (100 mebibytes).

Maximum file size
~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------+---------------------------------------------------------------------------------+
| The maximum file size for message attachments and plugin          | - System Config path: **Environment > File Storage**                            |
| uploads. This value must be specified in mebibytes in the         | - ``config.json`` setting: ``FileSettings`` > ``MaxFileSize`` > ``104857600``   |
| System Console, and in bytes in the ``config.json`` file.         | - Environment variable: ``MM_FILESETTINGS_MAXFILESIZE``                         |
|                                                                   |                                                                                 |
| The default is ``104857600`` bytes (**100** mebibytes).           |                                                                                 |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------+

.. note::

  - Verify server memory can support your setting choice. Large file sizes increase the risk of server crashes and failed uploads due to network disruptions.
  - When :ref:`uploading plugin files <administration-guide/configure/plugins-configuration-settings:upload plugin>`, a ``Received invalid response from the server`` error typically indicates that ``MaxFileSize`` isn't large enough to support the plugin file upload, and/or that proxy settings may not be sufficient.
  - If you use a proxy or load balancer in front of Mattermost, the following proxy settings must be adjusted accordingly:

    - For NGINX, use ``client_max_body_size``.
    - For Apache, use ``LimitRequestBody``.

.. config:setting:: enable-document-search-by-content
  :displayname: Enable document search by content (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.ExtractContent
  :environment: MM_FILESETTINGS_EXTRACTCONTENT
  :description: Enable users to search the contents of documents attached to messages.

  - **true**: **(Default)** Documents are searchable by their content.
  - **false**: Documents aren’t searchable by their content.

Enable document search by content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Enable users to search the contents of documents attached     | - System Config path: **Environment > File Storage**                                |
| to messages.                                                  | - ``config.json`` setting: ``FileSettings`` > ``ExtractContent`` > ``true``         |
|                                                               | - Environment variable: ``MM_FILESETTINGS_EXTRACTCONTENT``                          |
| - **true**: **(Default)** Documents are searchable by         |                                                                                     |
|   their content.                                              |                                                                                     |
| - **false**: Documents aren’t searchable by their content.    |                                                                                     |
|   When document content search is disabled, users can search  |                                                                                     |
|   for files by file name only.                                |                                                                                     |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------+

.. note::

  Enabling document search by content is required when extracting content from files. Both Mattermost :doc:`file search </end-user-guide/collaborate/search-for-messages>` and :doc:`Mattermost Agents </end-user-guide/agents>` can access files and their content, when enabled with the necessary dependencies. Document content search results for files shared before upgrading to Mattermost Server v5.35 may be incomplete until an extraction command is executed using the :ref:`mmctl <administration-guide/manage/mmctl-command-line-tool:mmctl extract>`. If this command is not run, users can search older files based on file name only.

  You can optionally install the following `dependencies <https://github.com/sajari/docconv#dependencies>`__ to extend content searching support in Mattermost to include file formats beyond PDF, DOCX, and ODT, such as DOC, RTF, XML, and HTML:

  - **tidy**: Used to search the contents of HTML documents.
  - **wv**: Used to search the contents of DOC documents.
  - **poppler-utils**: Used to significantly improve server performance when extracting the contents of PDF documents.
  - **unrtf**: Used to search the contents of RTF documents.
  - **JusText**: Used to search HTML documents. See the `JusText Python package <https://pypi.org/project/jusText/>`__ for deployment information.

  If you choose not to install these dependencies, you’ll see log entries for documents that couldn’t be extracted. Any documents that can’t be extracted are skipped and logged so that content extraction can proceed.

.. config:setting:: enable-searching-content-of-documents-within-zip-files
  :displayname: Enable searching content of documents within ZIP files (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.ArchiveRecursion
  :environment: MM_FILESETTINGS_ARCHIVERECURSION
  :description: Enables users to search the contents of compressed ZIP files attached to messages.

  - **true**: Contents of documents within ZIP files are returned in search results.
  - **false**: **(Default)** The contents of documents within ZIP files aren’t returned in search results.

Enable searching content of documents within ZIP files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Enables users to search the contents of compressed ZIP files  | - System Config path: **Environment > File Storage**                                   |
| attached to messages.                                         | - ``config.json`` setting: ``FileSettings`` > ``ArchiveRecursion`` > ``false``         |
|                                                               | - Environment variable: ``MM_FILESETTINGS_ARCHIVERECURSION``                           |
| - **true**: Contents of documents within ZIP files are        |                                                                                        |
|   returned in search results. This may have an impact on      |                                                                                        |
|   server performance for large files.                         |                                                                                        |
|   the specified local file directory.                         |                                                                                        |
| - **false**: **(Default)** The contents of documents within   |                                                                                        |
|   ZIP files aren’t returned in search results.                |                                                                                        |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------+

.. note::

  - You can search for document content within ZIP files when using Mattermost in a web browser or the desktop app.
  - Searching document contents adds load to your server.
  - For large deployments, or teams that share many large, text-heavy documents, we recommend you review our :ref:`hardware requirements <deployment-guide/software-hardware-requirements:hardware requirements>`, and test enabling this feature in a staging environment before enabling it in a production environment.

.. config:setting:: amazon-s3-bucket
  :displayname: Amazon S3 bucket (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3Bucket
  :environment: MM_FILESETTINGS_AMAZONS3BUCKET
  :description: The name of the bucket for your S3-compatible object storage instance.

Amazon S3 bucket
~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The name of the bucket for your S3-compatible object          | - System Config path: **Environment > File Storage**                     |
| storage instance.                                             | - ``config.json`` setting: ``FileSettings`` > ``AmazonS3Bucket``         |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3BUCKET``               |
| A string with the S3-compatible bucket name.                  |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: amazon-s3-path-prefix
  :displayname: Amazon S3 path prefix (File Storage)
  :systemconsole: N/A
  :configjson: .FileSettings.AmazonS3PathPrefix
  :environment: MM_FILESETTINGS_AMAZONS3PATHPREFIX
  :description: The prefix you selected for your **Amazon S3 bucket** in AWS.

Amazon S3 path prefix
~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The prefix you selected for your **Amazon S3 bucket** in AWS. | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``FileSettings`` > ``AmazonS3PathPrefix``     |
| A string containing the path prefix.                          | - Environment variable: ``MM_FILESETTINGS_AMAZONS3PATHPREFIX``           |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: amazon-s3-region
  :displayname: Amazon S3 region (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3Region
  :environment: MM_FILESETTINGS_AMAZONS3REGION
  :description: The AWS region you selected when creating your **Amazon S3 bucket** in AWS. For Digital Ocean Spaces or other S3-compatible services, leave this setting empty.

Amazon S3 region
~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The AWS region you selected when creating your                | - System Config path: **Environment > File Storage**                     |
| **Amazon S3 bucket** in AWS.                                  | - ``config.json`` setting: ```".FileSettings.AmazonS3Region",``          |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3REGION``               |
| A string with the AWS region containing the bucket.           |                                                                          |
| If no region is set, Mattermost attempts to get the           |                                                                          |
| appropriate region from AWS, and sets it to **us-east-1**     |                                                                          |
| if none found.                                                |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

For Digital Ocean Spaces or other S3-compatible services, leave this setting empty.

.. config:setting:: amazon-s3-access-key-id
  :displayname: Amazon S3 access key ID (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3AccessKeyId
  :environment: MM_FILESETTINGS_AMAZONS3ACCESSKEYID
  :description: A string with the access key for the S3-compatible storage instance.

Amazon S3 access key ID
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| A string with the access key for the S3-compatible storage    | - System Config path: **Environment > File Storage**                     |
| instance. Your EC2 administrator can supply you with the      | - ``config.json`` setting: ``FileSettings`` > ``AmazonS3AccessKeyId``    |
| Access Key ID.                                                | - Environment variable: ``MM_FILESETTINGS_AMAZONS3ACCESSKEYID``          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. note::

  This is required for access unless you are using an `Amazon S3 IAM Role <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html>`__ with Amazon S3.

.. config:setting:: amazon-s3-endpoint
  :displayname: Amazon S3 endpoint (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3Endpoint
  :environment: MM_FILESETTINGS_AMAZONS3ENDPOINT
  :description: The hostname of your S3-compatible instance. Default value is **s3.amazonaws.com**.

Amazon S3 endpoint
~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| The hostname of your S3-compatible instance.                  | - System Config path: **Environment > File Storage**                                        |
|                                                               | - ``config.json`` setting: ``FileSettings`` > ``AmazonS3Endpoint`` > ``"s3.amazonaws.com"`` |
| A string with the hostname of the S3-compatible storage       | - Environment variable: ``MM_FILESETTINGS_AMAZONS3ENDPOINT``                                |
| instance. Defaults to **s3.amazonaws.com**.                   |                                                                                             |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+

.. note::

  For Digital Ocean Spaces, the hostname should be set to **<region>.digitaloceanspaces.com**, where **<region>** is the abbreviation for the region you selected when setting up the Space. It can be **nyc3**, **ams3**, or **sgp1**.

.. config:setting:: amazon-s3-secret-access-key
  :displayname: Amazon S3 secret access key (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3SecretAccessKey
  :environment: MM_FILESETTINGS_AMAZONS3SECRETACCESSKEY
  :description: The secret access key associated with your Amazon S3 Access Key ID.

Amazon S3 secret access key
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+----------------------------------------------------------------------------+
| The secret access key associated with your Amazon S3          | - System Config path: **Environment > File Storage**                       |
| Access Key ID.                                                | - ``config.json`` setting: ``FileSettings`` > ``AmazonS3SecretAccessKey``  |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3SECRETACCESSKEY``        |
| A string with the secret access key for the S3-compatible     |                                                                            |
| storage instance.                                             |                                                                            |
+---------------------------------------------------------------+----------------------------------------------------------------------------+

.. config:setting:: enable-secure-amazon-s3-connections
  :displayname: Enable secure Amazon S3 connections (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3SSL
  :environment: MM_FILESETTINGS_AMAZONS3SSL
  :description: Enable or disable secure Amazon S3 connections. Default value is **true**.

Enable secure Amazon S3 connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Enable or disable secure Amazon S3 connections.               | - System Config path: **Environment > File Storage**                     |
|                                                               | - ``config.json`` setting: ``FileSettings`` > ``AmazonS3SSL`` > ``true`` |
| - **true**: **(Default)** Enables only secure Amazon          | - Environment variable: ``MM_FILESETTINGS_AMAZONS3SSL``                  |
|   S3 connections.                                             |                                                                          |
| - **false**: Allows insecure connections to Amazon S3.        |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: amazon-s3-signature-v2
  :displayname: Amazon S3 signature v2 (File Storage)
  :systemconsole: N/A
  :configjson: .FileSettings.AmazonS3SignV2
  :environment: MM_FILESETTINGS_AMAZONS3SIGNV2

  - **true**: Use Signature v2 signing process.
  - **false**: **(Default)** Use Signature v4 signing process.

Amazon S3 signature v2
~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+------------------------------------------------------------------------------+
| By default, Mattermost uses Signature v4 to sign API calls    | - System Config path: N/A                                                    |
| to AWS, but under some circumstances, v2 is required.         | - ``config.json`` setting: ``FileSettings`` > ``AmazonS3SignV2`` > ``false`` |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3SIGNV2``                   |
| - **true**: Use Signature v2 signing process.                 |                                                                              |
| - **false**: **(Default)** Use Signature v4 signing process.  |                                                                              |
+---------------------------------------------------------------+------------------------------------------------------------------------------+

See the `AWS <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html>`_ documentation for information about when to use the Signature v2 signing process.

.. config:setting:: enable-server-side-encryption-for-amazon-s3
  :displayname: Enable server-side encryption for Amazon S3 (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3SSE
  :environment: MM_FILESETTINGS_AMAZONS3SSE

  - **true**: Encrypts files in Amazon S3 using server-side encryption with Amazon S3-managed keys.
  - **false**: **(Default)** Doesn’t encrypt files in Amazon S3.

Enable server-side encryption for Amazon S3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

+---------------------------------------------------------------+-----------------------------------------------------------------------------+
| Enable server-side encryption for Amazon S3.                  | - System Config path: **Environment > File Storage**                        |
|                                                               | - ``config.json`` setting: ``FileSettings`` > ``AmazonS3SSE`` > ``false``   |
| - **true**: Encrypts files in Amazon S3 using server-side     | - Environment variable: ``MM_FILESETTINGS_AMAZONS3SSE``                     |
|   encryption with Amazon S3-managed keys.                     |                                                                             |
| - **false**: **(Default)** Doesn’t encrypt files in           |                                                                             |
|   Amazon S3.                                                  |                                                                             |
+---------------------------------------------------------------+-----------------------------------------------------------------------------+

.. note::

  This configuration setting is available for self-hosted deployments only.

.. config:setting:: enable-amazon-s3-debugging
  :displayname: Enable Amazon S3 debugging (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3Trace
  :environment: MM_FILESETTINGS_AMAZONS3TRACE

  - **true**: Log additional debugging information is logged to the system logs.
  - **false**: **(Default)** No Amazon S3 debugging information is included in the system logs.

Enable Amazon S3 debugging
~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------+
| Enable or disable Amazon S3 debugging to capture additional   | - System Config path: **Environment > File Storage**                        |
| debugging information in system logs.                         | - ``config.json`` setting: ``FileSettings`` > ``AmazonS3Trace`` > ``false`` |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3TRACE``                   |
| - **true**: Log additional debugging information is logged    |                                                                             |
|   to the system logs.                                         |                                                                             |
| - **false**: **(Default)** No Amazon S3 debugging information |                                                                             |
|   is included in the system logs. Typically set to **false**  |                                                                             |
|   in production.                                              |                                                                             |
+---------------------------------------------------------------+-----------------------------------------------------------------------------+

Select the **Test Connection** button in the System Console to validate the settings and ensure the user can access the server.

.. config:setting:: amazon-s3-storage-class
  :displayname: Amazon S3 storage class (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3StorageClass
  :environment: MM_FILESETTINGS_AMAZONS3STORAGECLASS
  :description: The storage class to use for uploads to S3-compatible storage solutions. Default is an empty string ``""``.

Amazon S3 storage class
~~~~~~~~~~~~~~~~~~~~~~~

Some Amazon S3-compatible storage solutions require the storage class parameter to be present in upload requests, otherwise they will be rejected. Configure this storage class as the storage class required by your S3-compatible solution.

+---------------------------------------------------------------+------------------------------------------------------------------------------------+
| The storage class to use for uploads to S3-compatible         | - System Config path: **Environment > File Storage**                               |
| storage solutions.                                            | - ``config.json`` setting: ``FileSettings`` > ``AmazonS3StorageClass`` > ``""``,   |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3STORAGECLASS``                   |
| String input. Default is an empty string ``""``.              |                                                                                    |
| Select **Test Connection** to test the configured connection. |                                                                                    |
+---------------------------------------------------------------+------------------------------------------------------------------------------------+

.. note::

  Most Amazon S3-compatible storage solutions assign a default storage class of ``STANDARD`` when no storage class is provided. See the `Amazon S3 storage class <https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html#AmazonS3-PutObject-request-header-StorageClass>`_ documentation for details about supported storage classes.

.. config:setting:: export-amazon-s3-storage-class
  :displayname: Export Amazon S3 storage class (File Storage)
  :systemconsole: N/a
  :configjson: .FileSettings.ExportAmazonS3StorageClass
  :environment: MM_FILESETTINGS_EXPORTAMAZONS3STORAGECLASS
  :description: The storage class to use for exports to S3-compatible storage solutions. Default value is an empty string ``""``.

Export Amazon S3 storage class
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
| The storage class to use for exports to S3-compatible         | - System Config path: N/A                                                              |
| storage solutions.                                            | - ``config.json`` setting: ``FileSettings`` > ``ExportAmazonS3StorageClass`` > ``""``  |
|                                                               | - Environment variable: ``MM_FILESETTINGS_EXPORTAMAZONS3STORAGECLASS``                 |
| String input. Default is an empty string ``""``.              |                                                                                        |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------+

.. note::

  Most Amazon S3-compatible storage solutions assign a default storage class of ``STANDARD`` when no storage class is provided. See the `Amazon S3 storage class <https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html#AmazonS3-PutObject-request-header-StorageClass>`_ documentation for details about supported storage classes.

.. config:setting:: amazon-s3-request-timeout
  :displayname: Amazon S3 request timeout (File Storage)
  :systemconsole: N/A
  :configjson: .FileSettings.AmazonS3RequestTimeoutMilliseconds
  :environment: MM_FILESETTINGS_AMAZONS3REQUESTTIMEOUTMILLISECONDS
  :description: Amount of time, in milliseconds, before requests to Amazon S3 time out. Default value is 30000 (30 seconds).

Amazon S3 request timeout
~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| The amount of time, in milliseconds, before requests to       | - System Config path: N/A                                                                        |
| Amazon S3 storage time out.                                   | - ``config.json`` setting: ``FileSettings`` > ``AmazonS3RequestTimeoutMilliseconds`` > ``30000`` |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3REQUESTTIMEOUTMILLISECONDS``                   |
| Default is 30000 (30 seconds).                                |                                                                                                  |
+---------------------------------------------------------------+--------------------------------------------------------------------------------------------------+

.. config:setting:: amazon-s3-upload-part-size
  :displayname: Amazon S3 upload part size (File Storage)
  :systemconsole: N/A
  :configjson: .FileSettings.AmazonS3UploadPartSizeBytes
  :environment: MM_FILESETTINGS_AMAZONS3UPLOADPARTSIZEBYTES
  :description: The size, in bytes, of each part in a multi-part upload to Amazon S3. Default value is 5242880 (5MB).

Amazon S3 upload part size
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| The size, in bytes, of each part in a multi-part              | - System Config path: N/A                                                                      |
| upload to Amazon S3.                                          | - ``config.json`` setting: ``FileSettings`` > ``AmazonS3UploadPartSizeBytes`` > ``5242880``    |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3UPLOADPARTSIZEBYTES``                        |
| Numeric value. Default is 5242880 (5MB).                      |                                                                                                |
+---------------------------------------------------------------+------------------------------------------------------------------------------------------------+

.. note::

  A smaller part size can result in more requests and an increase in latency, while a larger part size can result in more memory being allocated.

.. config:setting:: amazon-s3-exported-upload-part-size
  :displayname: Export Amazon S3 upload part size (File Storage)
  :systemconsole: N/A
  :configjson: .FileSettings.ExportAmazonS3UploadPartSizeBytes
  :environment: MM_FILESETTINGS_EXPORTAMAZONS3UPLOADPARTSIZEBYTES
  :description: The size, in bytes, of each part in a multi-part exported to Amazon S3. Default value is 104857600 (100MB).

Amazon S3 exported upload part size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| The size, in bytes, of each part in a multi-part              | - System Config path: N/A                                                                           |
| exported to Amazon S3.                                        | - ``config.json`` setting: ``FileSettings`` > ``ExportAmazonS3UploadPartSizeBytes`` > ``104857600`` |
|                                                               | - Environment variable: ``MM_FILESETTINGS_EXPORTAMAZONS3UPLOADPARTSIZEBYTES``                       |
| Numeric value. Default is 104857600 (100MB).                  |                                                                                                     |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+

.. note::

  A smaller part size can result in more requests and an increase in latency, while a larger part size can result in more memory being allocated.

.. config:setting:: amazon-s3-request-timeout
  :displayname: Amazon S3 request timeout (File Storage)
  :systemconsole: N/A
  :configjson: .FileSettings.AmazonS3RequestTimeoutMilliseconds
  :environment: MM_FILESETTINGS_AMAZONS3REQUESTTIMEOUTMILLISECONDS
  :description: Amount of time, in milliseconds, before requests to Amazon S3 time out. Default value is 30000 (30 seconds).

Amazon S3 request timeout
~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| The amount of time, in milliseconds, before requests to       | - System Config path: N/A                                                                        |
| Amazon S3 storage time out.                                   | - ``config.json`` setting: ``FileSettings`` > ``AmazonS3RequestTimeoutMilliseconds`` > ``30000`` |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3REQUESTTIMEOUTMILLISECONDS``                   |
| Default is 30000 (30 seconds).                                |                                                                                                  |
+---------------------------------------------------------------+--------------------------------------------------------------------------------------------------+

.. config:setting:: initial-font
  :displayname: Initial font (File Storage)
  :systemconsole: N/A
  :configjson: .FileSettings.InitialFont
  :environment: MM_FILESETTINGS_INITIALFONT
  :description: The font used in auto-generated profile pictures with colored backgrounds and username initials. Default value is **nunito-bold.ttf**.

Initial font
~~~~~~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| The font used in auto-generated profile pictures with colored | - System Config path: N/A                                                               |
| backgrounds and username initials.                            | - ``config.json`` setting: ``FileSettings`` > ``InitialFont`` > ``"nunito-bold.ttf"``   |
|                                                               | - Environment variable: ``MM_FILESETTINGS_INITIALFONT``                                 |
| A string with the font file name. Default is                  |                                                                                         |
| **nunito-bold.ttf**.                                          |                                                                                         |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+

----

Image proxy
-----------

With self-hosted deployments, an image proxy can be used by Mattermost apps to prevent them from connecting directly to remote self-hosted servers. Configure an image proxy by going to **System Console > Environment > Image Proxy**, or by editing the ``config.json`` file as described in the following tables.

.. config:setting:: enable-image-proxy
  :displayname: Enable image proxy (Image Proxy)
  :systemconsole: Environment > Image Proxy
  :configjson: .ImageProxySettings.Enable
  :environment: MM_IMAGEPROXYSETTINGS_ENABLE

  - **true**: Enables an image proxy for loading external images.
  - **false**: **(Default)** Disables the image proxy.

Enable image proxy
~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------------------+
| An image proxy anonymizes Mattermost app connections and      | - System Config path: **Environment > Image Proxy**                       |
| prevents them from accessing insecure content.                | - ``config.json`` setting: ``ImageProxySettings`` > ``Enable`` > ``true`` |
|                                                               | - Environment variable: ``MM_IMAGEPROXYSETTINGS_ENABLE``                  |
| - **true**: Enables an image proxy for loading                |                                                                           |
|   external images.                                            |                                                                           |
| - **false**: **(Default)** Disables the image proxy.          |                                                                           |
+---------------------------------------------------------------+---------------------------------------------------------------------------+

See the :doc:`image proxy </deployment-guide/server/image-proxy>` documentation to learn more.

.. config:setting:: image-proxy-type
  :displayname: Image proxy type (Image Proxy)
  :systemconsole: Environment > Image Proxy
  :configjson: .ImageProxySettings.ImageProxyType
  :environment: MM_IMAGEPROXYSETTINGS_IMAGEPROXYTYPE
  :description: The type of image proxy used by Mattermost.

  - **local**: **(Default)** The Mattermost server itself acts as the image proxy.
  - **atmos/camo**: An external atmos/camo image proxy is used.

Image proxy type
~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------------------+
| The type of image proxy used by Mattermost.                   | - System Config path: **Environment > Image Proxy**                                  |
|                                                               | - ``config.json`` setting: ``ImageProxySettings`` > ``ImageProxyType`` > ``"local"`` |
| - **local**: **(Default)** The Mattermost server itself acts  | - Environment variable: ``MM_IMAGEPROXYSETTINGS_IMAGEPROXYTYPE``                     |
|   as the image proxy.                                         |                                                                                      |
| - **atmos/camo**: An external atmos/camo image proxy is used. |                                                                                      |
+---------------------------------------------------------------+--------------------------------------------------------------------------------------+

See the :doc:`image proxy </deployment-guide/server/image-proxy>` documentation to learn more.

.. config:setting:: remote-image-proxy-url
  :displayname: Remote image proxy URL (Image Proxy)
  :systemconsole: Environment > Image Proxy
  :configjson: .ImageProxySettings.RemoteImageProxyURL
  :environment: MM_IMAGEPROXYSETTINGS_REMOTEIMAGEPROXYURL
  :description: The URL of the atmos/camo proxy.

Remote image proxy URL
~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------+
| The URL of the atmos/camo proxy. This setting isn't needed    | - System Config path: **Environment > Image Proxy**                         |
| when using the **local** image proxy.                         | - ``config.json`` setting: ``ImageProxySettings`` > ``RemoteImageProxyURL`` |
|                                                               | - Environment variable: ``MM_IMAGEPROXYSETTINGS_REMOTEIMAGEPROXYURL``       |
+---------------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: remote-image-proxy-options
  :displayname: Remote image proxy options (Image Proxy)
  :systemconsole: Environment > Image Proxy
  :configjson: .ImageProxySettings.RemoteImageProxyOptions
  :environment: MM_IMAGEPROXYSETTINGS_REMOTEIMAGEPROXYOPTIONS
  :description: The URL signing key passed to an atmos/camo image proxy.

Remote image proxy options
~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------------------------+
| The URL signing key passed to an atmos/camo image proxy.      | - System Config path: **Environment > Image Proxy**                             |
| This setting isn't needed when using the **local** image      | - ``config.json`` setting: ``ImageProxySettings`` > ``RemoteImageProxyOptions`` |
| proxy type.                                                   | - Environment variable: ``MM_IMAGEPROXYSETTINGS_REMOTEIMAGEPROXYOPTIONS``       |
+---------------------------------------------------------------+---------------------------------------------------------------------------------+

See the :doc:`image proxy </deployment-guide/server/image-proxy>` documentation to learn more.

----

SMTP
----

With self-hosted deployments, you can configure SMTP email server settings by going to **System Console > Environment > SMTP**, or by editing the ``config.json`` file as described in the following tables.

.. config:setting:: smtp-server
  :displayname: SMTP server (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SMTPServer
  :environment: MM_EMAILSETTINGS_SMTPSERVER
  :description: The location of the SMTP email server used for email notifications.

SMTP server
~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
| The location of the SMTP email server used for email            | - System Config path: **Environment > SMTP**                    |
| notifications.                                                  | - ``config.json`` setting: ``EmailSettings`` > ``SMTPServer``   |
|                                                                 | - Environment variable: ``MM_EMAILSETTINGS_SMTPSERVER``         |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

.. config:setting:: smtp-server-port
  :displayname: SMTP server port (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SMTPPort
  :environment: MM_EMAILSETTINGS_SMTPPORT
  :description: The port of SMTP email server. String input.

SMTP server port
~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
| The port of SMTP email server.                                  | - System Config path: **Environment > SMTP**                    |
|                                                                 | - ``config.json`` setting: ``EmailSettings`` > ``"SMTPPort"``   |
| String input.                                                   | - Environment variable: ``MM_EMAILSETTINGS_SMTPPORT``           |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

.. config:setting:: enable-smtp-authentication
  :displayname: Enable SMTP authentication (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.EnableSMTPAuth
  :environment: MM_EMAILSETTINGS_ENABLESMTPAUTH

  - **true**: SMTP username and password are used for authenticating to the SMTP server.
  - **false**: **(Default)** Mattermost doesn’t attempt to authenticate to the SMTP server.

Enable SMTP authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+---------------------------------------------------------------------------------+
| Enable or disable SMTP authentication.                          | - System Config path: **Environment > SMTP**                                    |
|                                                                 | - ``config.json`` setting: ``EmailSettings`` > ``EnableSMTPAuth`` > ``false``   |
| - **true**: SMTP username and password are used for             | - Environment variable: ``MM_EMAILSETTINGS_ENABLESMTPAUTH``                     |
|   authenticating to the SMTP server.                            |                                                                                 |
| - **false**: **(Default)** Mattermost doesn’t attempt to        |                                                                                 |
|   authenticate to the SMTP server.                              |                                                                                 |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------+

.. config:setting:: smtp-server-username
  :displayname: SMTP server username (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SMTPUsername
  :environment: MM_EMAILSETTINGS_SMTPUSERNAME
  :description: The username for authenticating to the SMTP server.

SMTP server username
~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
| The username for authenticating to the SMTP server.             | - System Config path: **Environment > SMTP**                    |
|                                                                 | - ``config.json`` setting: ``EmailSettings`` > ``SMTPUsername`` |
| String input.                                                   | - Environment variable: ``MM_EMAILSETTINGS_SMTPUSERNAME``       |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

.. config:setting:: smtp-server-password
  :displayname: SMTP server password (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SMTPPassword
  :environment: MM_EMAILSETTINGS_SMTPPASSWORD
  :description: The password associated with the SMTP username.

SMTP server password
~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------+
| The password associated with the SMTP username.                 | - System Config path: **Environment > SMTP**                    |
|                                                                 | - ``config.json`` setting: ``EmailSettings`` > ``SMTPPassword`` |
| String input.                                                   | - Environment variable: ``MM_EMAILSETTINGS_SMTPPASSWORD``       |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

.. config:setting:: smtp-connection-security
  :displayname: SMTP connection security (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.ConnectionSecurity
  :environment: MM_EMAILSETTINGS_CONNECTIONSECURITY

  - **Not specified**: **(Default)** Send email over an unsecure connection.
  - **TLS**: Communication between Mattermost and your email server is encrypted.
  - **STARTTLS**: Attempts to upgrade an existing insecure connection to a secure connection using TLS.

SMTP connection security
~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------------+
| Specify connection security for emails sent using SMTP.         | - System Config path: **Environment > SMTP**                          |
|                                                                 | - ``config.json`` setting: ``EmailSettings`` > ``ConnectionSecurity`` |
| - **Not specified**: **(Default)** Send email over an           | - Environment variable: ``MM_EMAILSETTINGS_CONNECTIONSECURITY``       |
|   unsecure connection.                                          |                                                                       |
| - **TLS**: Communication between Mattermost and your email      |                                                                       |
|   server is encrypted.                                          |                                                                       |
| - **STARTTLS**: Attempts to upgrade an existing insecure        |                                                                       |
|   connection to a secure connection using TLS.                  |                                                                       |
+-----------------------------------------------------------------+-----------------------------------------------------------------------+

.. config:setting:: skip-server-certificate-verification
  :displayname: Skip server certificate verification (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SkipServerCertificateVerification
  :environment: MM_EMAILSETTINGS_SKIPSERVERCERTIFICATEVERIFICATION

  - **true**: Mattermost won't verify the email server certificate.
  - **false**: **(Default)** Mattermost verifies the email server certificate.

Skip server certificate verification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Configure Mattermost to skip the verification of the email server     | - System Config path: **Environment > SMTP**                                                       |
| certificate.                                                          | - ``config.json`` setting: ``EmailSettings`` > ``SkipServerCertificateVerification`` > ``false``   |
|                                                                       | - Environment variable: ``MM_EMAILSETTINGS_SKIPSERVERCERTIFICATEVERIFICATION``                     |
| - **true**: Mattermost won't verify the email server certificate.     |                                                                                                    |
| - **false**: **(Default)** Mattermost verifies the email              |                                                                                                    |
|   server certificate.                                                 |                                                                                                    |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+

.. config:setting:: enable-security-alerts
  :displayname: Enable security alerts (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .ServiceSettings.EnableSecurityFixAlert
  :environment: MM_SERVICESETTINGS_ENABLESECURITYFIXALERT

  - **true**: **(Default)** System admins are notified by email if a relevant security fix alert is announced. Requires email to be enabled.
  - **false**: Security alerts are disabled.

Enable security alerts
~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Enable or disable security alerts.                              | - System Config path: **Environment > SMTP**                                             |
|                                                                 | - ``config.json`` setting: ``ServiceSettings`` > ``EnableSecurityFixAlert`` > ``true``   |
| - **true**: **(Default)** System admins are notified by email   | - Environment variable: ``MM_SERVICESETTINGS_ENABLESECURITYFIXALERT``                    |
|   if a relevant security fix alert is announced. Requires email |                                                                                          |
|   to be enabled.                                                |                                                                                          |
| - **false**: Security alerts are disabled.                      |                                                                                          |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------------+

See the :ref:`Telemetry <administration-guide/manage/telemetry:security update check feature>` documentation to learn more.

.. config:setting:: smtp-server-timeout
  :displayname: SMTP server timeout (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SMTPServerTimeout
  :environment: MM_EMAILSETTINGS_SMTPSERVERTIMEOUT
  :description: The maximum amount of time, in seconds, allowed for establishing a TCP connection between Mattermost and the SMTP server.

SMTP server timeout
~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+----------------------------------------------------------------------+
| The maximum amount of time, in seconds, allowed for             | - System Config path: **Environment > SMTP**                         |
| establishing a TCP connection between Mattermost and the SMTP   | - ``config.json`` setting: ``EmailSettings`` > ``SMTPServerTimeout`` |
| server.                                                         | - Environment variable: ``MM_EMAILSETTINGS_SMTPSERVERTIMEOUT``       |
|                                                                 |                                                                      |
| Numerical value in seconds.                                     |                                                                      |
+-----------------------------------------------------------------+----------------------------------------------------------------------+

----

Push notification server
------------------------

.. include:: push-notification-server-configuration-settings.rst
    :start-after: :nosearch:

----

High availability
-----------------

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

With self-hosted deployments, you can configure Mattermost as a :doc:`high availability cluster-based deployment </administration-guide/scale/high-availability-cluster-based-deployment>` by going to **System Console > Environment > High Availability**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

In a Mattermost high availability cluster-based deployment, the System Console is set to read-only, and settings can only be changed by editing the ``config.json`` file directly. However, to test a high availability cluster-based environment, you can disable ``ClusterSettings.ReadOnlyConfig`` in the ``config.json`` file by setting it to ``false``. This allows changes applied using the System Console to be saved back to the configuration file.

.. config:setting:: enable-high-availability-mode
  :displayname: Enable high availability mode (High Availability)
  :systemconsole: Environment > High Availability
  :configjson: .ClusterSettings.Enable
  :environment: MM_CLUSTERSETTINGS_ENABLE

  - **true**: The Mattermost server will attempt inter-node communication with the other servers in the cluster that have the same cluster name.
  - **false**: **(Default)** Mattermost high availability mode is disabled.

Enable high availability mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+---------------------------------------------------------------------------+
| You can enable high availability mode.                          | - System Config path: **Environment > High Availability**                 |
|                                                                 | - ``config.json`` setting: ``ClusterSettings`` > ``Enable`` > ``false``   |
| - **true**: The Mattermost server will attempt inter-node       | - Environment variable: ``MM_CLUSTERSETTINGS_ENABLE``                     |
|   communication with the other servers in the cluster that      |                                                                           |
|   have the same cluster name. This sets the System Console to   |                                                                           |
|   read-only mode to keep the servers' ``config.json`` files     |                                                                           |
|   in sync.                                                      |                                                                           |
| - **false**: **(Default)** Mattermost high availability mode    |                                                                           |
|   is disabled.                                                  |                                                                           |
+-----------------------------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: cluster-name
  :displayname: Cluster name (High Availability)
  :systemconsole: Environment > High Availability
  :configjson: .ClusterSettings.ClusterName
  :environment: MM_CLUSTERSETTINGS_CLUSTERNAME
  :description: The cluster to join by name in a high availability cluster-based deployment.

Cluster name
~~~~~~~~~~~~

+------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| The cluster to join by name in a high availability cluster-based deployment. | - System Config path: **Environment > High Availability**                |
|                                                                              | - ``config.json`` setting: ``ClusterSettings`` > ``ClusterName``         |
| Only nodes with the same cluster name will join together.                    | - Environment variable: ``MM_CLUSTERSETTINGS_CLUSTERNAME``               |
| This is to support blue-green deployments or staging pointing                |                                                                          |
| to the same database.                                                        |                                                                          |
+------------------------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: override-hostname
  :displayname: Override hostname (High Availability)
  :systemconsole: Environment > High Availability
  :configjson: .ClusterSettings.OverrideHostname
  :environment: MM_CLUSTERSETTINGS_OVERRIDEHOSTNAME
  :description: Override the hostname of this server.

Override hostname
~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+---------------------------------------------------------------------------------+
| You can override the hostname of this server.                   | - System Config path: **Environment > High Availability**                       |
|                                                                 | - ``config.json`` setting: ``ClusterSettings`` > ``OverrideHostname``           |
| - This property can be set to a specific IP address if needed;  | - Environment variable: ``MM_CLUSTERSETTINGS_OVERRIDEHOSTNAME``                 |
|   however, we don’t recommend overriding the hostname unless    |                                                                                 |
|   it's necessary.                                               |                                                                                 |
| - If left blank, Mattermost attempts to get the hostname from   |                                                                                 |
|   the operating system or uses the IP address.                  |                                                                                 |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------+

See the :doc:`high availability cluster-based deployment </administration-guide/scale/high-availability-cluster-based-deployment>` documentation for details.

.. config:setting:: use-ip-address
  :displayname: Use IP address (High Availability)
  :systemconsole: Environment > High Availability
  :configjson: .ClusterSettings.UseIPAddress
  :environment: MM_CLUSTERSETTINGS_USEIPADDRESS

  - **true**: **(Default)** The cluster attempts to communicate using the IP address specified.
  - **false**: The cluster attempts to communicate using the hostname.

Use IP address
~~~~~~~~~~~~~~

+------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| You can configure your high availability cluster-based deployment to         | - System Config path: **Environment > High Availability**                     |
| communicate using the hostname instead of the IP address.                    | - ``config.json`` setting: ``ClusterSettings`` > ``UseIPAddress`` > ``true``  |
|                                                                              | - Environment variable: ``MM_CLUSTERSETTINGS_USEIPADDRESS``                   |
| - **true**: **(Default)** The cluster attempts to communicate                |                                                                               |
|   using the IP address specified.                                            |                                                                               |
| - **false**: The cluster attempts to communicate using the                   |                                                                               |
|   hostname.                                                                  |                                                                               |
+------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

.. config:setting:: enable-gossip-encryption
  :displayname: Enable gossip encryption (High Availability)
  :systemconsole: Environment > High Availability
  :configjson: .ClusterSettings.EnableGossipEncryption
  :environment: MM_CLUSTERSETTINGS_ENABLEGOSSIPENCRYPTION

  - **true**: **(Default)** The server attempts to communicate via the gossip protocol over the gossip port specified.
  - **false**: The server attempts to communicate over the streaming port.

Enable gossip encryption
~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Gossip encryption uses AES-256 by default, and this value isn't | - System Config path: **Environment > High Availability**                               |
| configurable by design.                                         | - ``config.json`` setting: ``ClusterSettings`` > ``EnableGossipEncryption`` > ``true``  |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_ENABLEGOSSIPENCRYPTION``                   |
| - **true**: **(Default)** The server attempts to communicate    |                                                                                         |
|   via the gossip protocol over the gossip port specified.       |                                                                                         |
| - **false**: The server attempts to communicate over the        |                                                                                         |
|   streaming port.                                               |                                                                                         |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. note::

  - The Gossip protocol is based on principles outlined in the `SWIM protocol developed by researchers at Cornell University <https://www.cs.cornell.edu/projects/Quicksilver/public_pdfs/SWIM.pdf>`_. The gossip protocol is a communication mechanism in distributed systems where nodes randomly exchange information to ensure data consistency across the network. It is decentralized, scalable, and fault-tolerant, making it ideal for systems with numerous nodes. Information is spread in a manner similar to social gossip, with nodes periodically "gossiping" updates to random peers until the network converges to a consistent state. Widely used in distributed databases, blockchain networks, and peer-to-peer systems, the protocol is simple to implement and resilient to node failures. However, it can suffer from redundancy and propagation delays in large networks.
  - Alternatively, you can manually set the ``ClusterEncryptionKey`` row value in the **Systems** table. A key is a byte array converted to base64. Set this value to either 16, 24, or 32 bytes to select AES-128, AES-192, or AES-256 respectively.
  - From Mattermost v10.11, gossip encryption is enabled by default for all new deployments. For existing deployments, all communication using the gossip protocol remains unencrypted unless you manually enable encryption. Prior to v10.11, gossip encryption is enabled by default for Cloud deployments and disabled by default for self-hosted deployments.

.. config:setting:: enable-gossip-compression
  :displayname: Enable gossip compression (High Availability)
  :systemconsole: Environment > High Availability
  :configjson: .ClusterSettings.EnableGossipCompression
  :environment: MM_CLUSTERSETTINGS_ENABLEGOSSIPCOMPRESSION

  - **true**: **(Default)** All communication through the cluster uses gossip compression.
  - **false**: All communication using the gossip protocol remains uncompressed.

Enable gossip compression
~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| We recommend that you disable this configuration                | - System Config path: **Environment > High Availability**                               |
| setting for better performance.                                 | - ``config.json`` setting: ``ClusterSettings`` > ``EnableGossipCompression`` > ``true`` |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_ENABLEGOSSIPCOMPRESSION``                  |
| - **true**: **(Default for self-hosted deployments)**           |                                                                                         |
|   All communication through the cluster uses gossip             |                                                                                         |
|   compression. This setting is enabled by default to maintain   |                                                                                         |
|   compatibility with older servers.                             |                                                                                         |
| - **false**: **(Default for Cloud deployments)**                |                                                                                         |
|   All communication using the gossip protocol remains           |                                                                                         |
|   uncompressed.                                                 |                                                                                         |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. config:setting:: gossip-port
  :displayname: Gossip port (High Availability)
  :systemconsole: Environment > High Availability
  :configjson: .ClusterSettings.GossipPort
  :environment: MM_CLUSTERSETTINGS_GOSSIPPORT
  :description: The port used for the gossip protocol. Both UDP and TCP should be allowed on this port. Default value is **8074**.

Gossip port
~~~~~~~~~~~

+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| The port used for the gossip protocol. Both UDP and TCP         | - System Config path: **Environment > High Availability**                  |
| should be allowed on this port.                                 | - ``config.json`` setting: ``ClusterSettings`` > ``GossipPort`` > ``8074`` |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_GOSSIPPORT``                  |
| Numerical input. Default is **8074**.                           |                                                                            |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+

.. config:setting:: read-only-config
  :displayname: Read only config (High Availability)
  :systemconsole: N/A
  :configjson: .ClusterSettings.ReadOnlyConfig
  :environment: MM_CLUSTERSETTINGS_READONLYCONFIG
  :description: Configure whether changes made in the System Console are written to config.json or ignored. Default is ignored.

Read only config
~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+--------------------------------------------------------------------------------+
| - **true**: **(Default)** Changes made to settings in the       | - System Config path: N/A                                                      |
|   System Console are ignored.                                   | - ``config.json`` setting: ``ClusterSettings`` > ``ReadOnlyConfig`` > ``true`` |
| - **false**: Changes made to settings in the System Console     | - Environment variable: ``MM_CLUSTERSETTINGS_READONLYCONFIG``                  |
|   are written to ``config.json``.                               |                                                                                |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------+

.. config:setting:: network-interface
  :displayname: Network interface (High Availability)
  :systemconsole: N/A
  :configjson: .ClusterSettings.NetworkInterface
  :environment: MM_CLUSTERSETTINGS_NETWORKINTERFACE
  :description: An IP address used to identify the device that does automatic IP detection in high availability cluster-based deployments.

Network interface
~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+--------------------------------------------------------------------------------+
| An IP address used to identify the device that does automatic   | - System Config path: N/A                                                      |
| IP detection in high availability cluster-based deployments.    | - ``config.json`` setting: ``ClusterSettings`` > ``NetworkInterface`` > ``""`` |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_NETWORKINTERFACE``                |
| String input.                                                   |                                                                                |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------+

.. config:setting:: bind-address
  :displayname: Bind address (High Availability)
  :systemconsole: N/A
  :configjson: .ClusterSettings.BindAddress
  :environment: MM_CLUSTERSETTINGS_BINDADDRESS
  :description: An IP address used to bind cluster traffic to a specific network device.

Bind address
~~~~~~~~~~~~

+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| An IP address used to bind cluster traffic to a specific        | - System Config path: N/A                                                  |
| network device.                                                 | - ``config.json`` setting: ``ClusterSettings`` > ``BindAddress`` > ``""``  |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_BINDADDRESS``                 |
| This setting is used primarily for servers with multiple        |                                                                            |
| network devices or different Bind Address and Advertise Address |                                                                            |
| like in deployments that involve NAT (Network Address           |                                                                            |
| Translation).                                                   |                                                                            |
|                                                                 |                                                                            |
| String input.                                                   |                                                                            |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+

.. config:setting:: advertise-address
  :displayname: Advertise address (High Availability)
  :systemconsole: N/A
  :configjson: .ClusterSettings.AdvertiseAddress
  :environment: MM_CLUSTERSETTINGS_ADVERTISEADDRESS
  :description: The IP address used to access the server from other nodes.

Advertise address
~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+--------------------------------------------------------------------------------+
| The IP address used to access the server from other nodes.      | - System Config path: N/A                                                      |
| This settings is used primary when cluster nodes are not in     | - ``config.json`` setting: ``ClusterSettings`` > ``AdvertiseAddress`` > ``""`` |
| the same network and involve NAT (Network Address Translation). | - Environment variable: ``MM_CLUSTERSETTINGS_ADVERTISEADDRESS``                |
|                                                                 |                                                                                |
| String input.                                                   |                                                                                |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------+

----

Rate limiting
-------------

.. include:: rate-limiting-configuration-settings.rst
    :start-after: :nosearch:

----

Logging
--------

Mattermost provides 3 independent logging systems for self-hosted deployments that can be configured separately with separate log files and rotation policies to meet different operational and compliance needs:

- `Log Settings <#log-settings>`__
- `Notification Log Settings <#notification-logging>`__
- `Audit Log Settings <#audit-logging>`__

By default, all Mattermost editions write logs to both the console and to the ``mattermost.log`` file in a machine-readable JSON format. Mattermost Enterprise and Professional customers can additionally log directly to syslog and TCP socket destination targets.

Log settings
~~~~~~~~~~~~

Configure general logging by going to **System Console > Environment > Logging**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: output-logs-to-console
  :displayname: Output general logs to console (General Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.EnableConsole
  :environment: MM_LOGSETTINGS_ENABLECONSOLE

  - **true**: **(Default)** General logs are written to the console based on the `console log level <#console-log-level>`__ configuration.
  - **false**: Output log messages aren’t written to the console.

Output logs to console
^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+---------------------------------------------------------------------------+
| Configure Mattermost to output general logs   | - System Config path: **Environment > Logging**                           |
| to the console.                               | - ``config.json`` setting: ``LogSettings`` > ``EnableConsole`` > ``true`` |
|                                               | - Environment variable: ``MM_LOGSETTINGS_ENABLECONSOLE``                  |
| - **true**: **(Default)** Output log messages |                                                                           |
|   are written to the console based on the     |                                                                           |
|   `console log level <#console-log-level>`__  |                                                                           |
|   configuration. The server writes messages   |                                                                           |
|   to the standard output stream (stdout).     |                                                                           |
| - **false**: Output log messages aren’t       |                                                                           |
|   written to the console.                     |                                                                           |
+-----------------------------------------------+---------------------------------------------------------------------------+

.. note::

  From Mattermost v11.0, notification logs are automatically included in the main console logs.

.. config:setting:: console-log-level
  :displayname: Console general log level (General Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.ConsoleLevel
  :environment: MM_LOGSETTINGS_CONSOLELEVEL
  :description: The level of detail in log events written when Mattermost outputs log messages to the console.

  - **DEBUG**: **(Default)** Outputs verbose detail for developers debugging issues.
  - **ERROR**: Outputs only error messages.
  - **INFO**: Outputs general error messages and information around startup and initialization.

Console log level
^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+-----------------------------------------------------------------------------+
| The level of detail in general log events     | - System Config path: **Environment > Logging**                             |
| written when Mattermost outputs log messages  | - ``config.json`` setting: ``LogSettings`` > ``ConsoleLevel`` > ``"DEBUG"`` |
| to the console.                               | - Environment variable: ``MM_LOGSETTINGS_CONSOLELEVEL``                     |
|                                               |                                                                             |
| - **DEBUG**: **(Default)** Outputs verbose    |                                                                             |
|   detail for developers debugging issues.     |                                                                             |
| - **ERROR**: Outputs only error messages.     |                                                                             |
| - **INFO**: Outputs error messages and        |                                                                             |
|   information around startup and              |                                                                             |
|   initialization.                             |                                                                             |
+-----------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: output-console-logs-as-json
  :displayname: Output general console logs as JSON (General Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.ConsoleJson
  :environment: MM_LOGSETTINGS_CONSOLEJSON
  :description: Configure Mattermost to output general console logs as JSON.

  - **true**: **(Default)** General events are written in a machine-readable JSON format.
  - **false**: Logged events are written in plain text.

Output console logs as JSON
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+---------------------------------------------------------------------------+
| Configure Mattermost to output general        | - System Config path: **Environment > Logging**                           |
| console logs as JSON.                         | - ``config.json`` setting: ``LogSettings`` > ``ConsoleJson`` > ``true``   |
|                                               | - Environment variable: ``MM_LOGSETTINGS_CONSOLEJSON``                    |
| - **true**: **(Default)** Logged events are   |                                                                           |
|   written in a machine-readable JSON format.  |                                                                           |
| - **false**: Logged events are written in     |                                                                           |
|   plain text.                                 |                                                                           |
+-----------------------------------------------+---------------------------------------------------------------------------+

Typically set to **true** in a production environment.

.. config:setting:: colorize-plain-text-console-logs
  :displayname: Colorize plain text general console logs (General Logging)
  :systemconsole: N/A
  :configjson: .LogSettings.EnableColor
  :environment: MM_LOGSETTINGS_ENABLECOLOR
  :description: Enables system admins to display plain text general log level details in color.

  - **true**: When logged general events are output to the console as plain text, colorize log levels details.
  - **false**: **(Default)** Plain text log details aren't colorized in the console.

Colorize plain text console logs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+----------------------------------------------------------------------------+
| Enables system admins to display plain text   | - System Config path: N/A                                                  |
| general log level details in color.           | - ``config.json`` setting: ``LogSettings`` > ``EnableColor`` > ``false``   |
|                                               | - Environment variable: ``MM_LOGSETTINGS_ENABLECOLOR``                     |
| - **true**: When logged events are output to  |                                                                            |
|   the console as plain text, colorize log     |                                                                            |
|   levels details.                             |                                                                            |
| - **false**: **(Default)** Plain text log     |                                                                            |
|   details aren't colorized in the console.    |                                                                            |
+-----------------------------------------------+----------------------------------------------------------------------------+

.. config:setting:: output-logs-to-file
  :displayname: Output general logs to file (General Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.EnableFile
  :environment: MM_LOGSETTINGS_ENABLEFILE
  :description: Configure Mattermost to output console logs to a file.

  - **true**: **(Default)** General events are written based on the `file log level <#file-log-level>`__ configuration to a ``mattermost.log`` file located in the directory configured via file location.
  - **false**: Logged events aren’t written to a file.

Output logs to file
^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+---------------------------------------------------------------------------+
| Configure Mattermost to output general        | - System Config path: **Environment > Logging**                           |
| console logs to a file.                       | - ``config.json`` setting: ``LogSettings`` > ``EnableFile`` > ``true``    |
|                                               | - Environment variable: ``MM_LOGSETTINGS_ENABLEFILE``                     |
| - **true**: **(Default)** Logged events are   |                                                                           |
|   written based on the                        |                                                                           |
|   `file log level <#file-log-level>`__        |                                                                           |
|   configuration to a ``mattermost.log`` file  |                                                                           |
|   located in the directory configured via     |                                                                           |
|   ``file location``.                          |                                                                           |
| - **false**: Logged events aren’t written to  |                                                                           |
|   a file.                                     |                                                                           |
+-----------------------------------------------+---------------------------------------------------------------------------+

.. note::

  - From Mattermost v11.0, notification logs are automatically included in the main file logs.
  - This setting is typically set to **true** in a production environment. When enabled, you can download the ``mattermost.log`` file locally by going to **System Console > Reporting > Server Logs**, and selecting **Download Logs**.

.. config:setting:: file-log-directory
  :displayname: General file log directory (General Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.FileLocation
  :environment: MM_LOGSETTINGS_FILELOCATION
  :description: The location of the general log files. Default value is **./logs**.

File log directory
^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+----------------------------------------------------------------------------+
| The location of the general log files.        | - System Config path: **Environment > Logging**                            |
|                                               | - ``config.json`` setting: ``LogSettings`` > ``FileLocation`` > ``""``     |
| String input. If left blank, log files are    | - Environment variable: ``MM_LOGSETTINGS_FILELOCATION``                    |
| stored in the ``./logs`` directory.           |                                                                            |
+-----------------------------------------------+----------------------------------------------------------------------------+

.. note::

  - The path you configure must exist, and Mattermost must have write permissions for this directory.
  - From Mattermost v11.4, you can use the ``MM_LOG_PATH`` environment variable to restrict log file locations to a designated root directory. This security enhancement ensures that all log files configured via ``LogSettings.FileLocation`` or ``LogSettings.AdvancedLoggingJSON`` remain within an authorized logging directory. 

    - If ``MM_LOG_PATH`` isn't set, the default ``logs`` directory is used. Paths outside the root directory generate error logs and are excluded from :doc:`support packet </administration-guide/manage/admin/generating-support-packet>` downloads. See the :ref:`log path restrictions <administration-guide/manage/logging:log path restrictions>` documentation for details.

.. config:setting:: file-log-level
  :displayname: General file log level (General Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.FileLevel
  :environment: MM_LOGSETTINGS_FILELEVEL
  :description: The level of detail in general log events when Mattermost outputs log messages to a file.

  - **DEBUG**: Outputs verbose detail for developers debugging issues.
  - **ERROR**: Outputs only error messages.
  - **INFO**: **(Default)** Outputs error messages and information around startup and initialization.

File log level
^^^^^^^^^^^^^^

+-------------------------------------------------+-------------------------------------------------------------------------+
| The level of detail in general log events when  | - System Config path: **Environment > Logging**                         |
| when Mattermost outputs log messages to a file. | - ``config.json`` setting: ``LogSettings`` > ``FileLevel`` > ``"INFO"`` |
|                                                 | - Environment variable: ``MM_LOGSETTINGS_FILELEVEL``                    |
| - **DEBUG**: Outputs verbose detail for         |                                                                         |
|   developers debugging issues.                  |                                                                         |
| - **ERROR**: Outputs only error messages.       |                                                                         |
| - **INFO**: **(Default)** Outputs error         |                                                                         |
|   messages and information around startup       |                                                                         |
|   and initialization.                           |                                                                         |
+-------------------------------------------------+-------------------------------------------------------------------------+

.. config:setting:: output-file-logs-as-json
  :displayname: Output general file logs as JSON (General Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.FileJson
  :environment: MM_LOGSETTINGS_FILEJSON
  :description: Configure Mattermost to output general file logs as JSON.

  - **true**: **(Default)** General events are written in a machine-readable JSON format.
  - **false**: Logged events are written in plain text.

Output file logs as JSON
^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+------------------------------------------------------------------------+
| Configure Mattermost to output general file   | - System Config path: **Environment > Logging**                        |
| logs as JSON.                                 | - ``config.json`` setting: ``LogSettings`` > ``FileJson`` > ``true``   |
|                                               | - Environment variable: ``MM_LOGSETTINGS_FILEJSON``                    |
| - **true**: **(Default)** Logged events are   |                                                                        |
|   written in a machine-readable JSON format.  |                                                                        |
| - **false**: Logged events are written in     |                                                                        |
|   plain text.                                 |                                                                        |
+-----------------------------------------------+------------------------------------------------------------------------+

Typically set to **true** in a production environment.

.. config:setting:: enable-webhook-debugging
  :displayname: Enable general webhook debugging (General Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.EnableWebhookDebugging
  :environment: MM_LOGSETTINGS_ENABLEWEBHOOKDEBUGGING
  :description: Configure Mattermost to capture the contents of general incoming webhooks to log files for debugging.

  - **true**: **(Default)** The contents of general incoming webhooks are printed to console and/or file logs for debugging.
  - **false**: The contents of incoming webhooks aren’t printed to log files.

Enable webhook debugging
^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+------------------------------------------------------------------------------------+
| Configure Mattermost to capture the contents  | - System Config path: **Environment > Logging**                                    |
| of general incoming webhooks to console       | - ``config.json`` setting: ``LogSettings`` > ``EnableWebhookDebugging`` > ``true`` |
| and/or file logs for debugging.               | - Environment variable: ``MM_LOGSETTINGS_ENABLEWEBHOOKDEBUGGING``                  |
|                                               |                                                                                    |
| - **true**: **(Default)** The contents of     |                                                                                    |
|   incoming webhooks are printed to log files  |                                                                                    |
|   for debugging.                              |                                                                                    |
| - **false**: The contents of incoming         |                                                                                    |
|   webhooks aren’t printed to log files.       |                                                                                    |
+-----------------------------------------------+------------------------------------------------------------------------------------+

.. note::

  Enable debug logs by changing the `file log level <#file-log-level>`__ to ``DEBUG`` to include the request body of incoming webhooks in logs.

.. config:setting:: output-logs-to-multiple-targets
  :displayname: Output general logs to multiple targets (General Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.AdvancedLoggingJSON
  :environment: MM_LOGSETTINGS_ADVANCEDLOGGINGJSON
  :description: Configure Mattermost to allow any combination of console, local file, syslog, and TCP socket targets, and send general log records to multiple targets.

Output logs to multiple targets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+------------------------------------------------------------------------------------+
| Configure Mattermost to allow any combination | - System Config path: **Environment > Logging**                                    |
| of console, local file, syslog, and TCP       | - ``config.json`` setting: ``LogSettings`` > ``AdvancedLoggingJSON`` > ``": ""``   |
| socket targets, and send general log records  | - Environment variable: ``MM_LOGSETTINGS_ADVANCEDLOGGINGJSON``                     |
| to multiple targets.                          |                                                                                    |
|                                               |                                                                                    |
| String input can contain a filespec to        |                                                                                    |
| another configuration file, a database DSN,   |                                                                                    |
| or JSON.                                      |                                                                                    |
+-----------------------------------------------+------------------------------------------------------------------------------------+

.. note::

  - See the :doc:`Mattermost logging </administration-guide/manage/logging>` documentation for details. These targets have been chosen as they support the vast majority of log aggregators, and other log analysis tools, without needing additional software installed.
  - Logs are recorded asynchronously to reduce latency to the caller.
  - Advanced logging supports hot-reloading of logger configuration.
  - From Mattermost v11.4, file paths specified in ``AdvancedLoggingJSON`` configurations should be within the directory specified by the ``MM_LOG_PATH`` environment variable. See :ref:`log path restrictions <administration-guide/manage/logging:log path restrictions>` for details.

.. config:setting:: maximum-field-size
  :displayname: Maximum general log field size (General Logging)
  :systemconsole: N/A
  :configjson: .LogSettings.MaxFieldSize
  :environment: MM_LOGSETTINGS_MAXFIELDSIZE
  :description: Enables system admins to limit the size of general log fields during logging. Default is **2048**.

Maximum field size
^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+----------------------------------------------------------------------------+
| Enables system admins to limit the size of    | - System Config path: N/A                                                  |
| general log fields during logging.            | - ``config.json`` setting: ``LogSettings`` > ``MaxFieldSize`` > ``2048``   |
|                                               | - Environment variable: ``MM_LOGSETTINGS_MAXFIELDSIZE``                    |
| Numerical value. Default is **2048**.         |                                                                            |
+-----------------------------------------------+----------------------------------------------------------------------------+

.. config:setting:: enable-diagnostics-and-error-reporting
  :displayname: Enable general diagnostics and error reporting (General Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.EnableDiagnostics
  :environment: MM_LOGSETTINGS_ENABLEDIAGNOSTICS
  :description: Send general diagnostics and error reports to Mattermost, Inc.

Enable diagnostics and error reporting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------------------------------+--------------------------------------------------------------------------------+
| Whether or not general diagnostics and error | - System Config path: **Environment > Logging**                                |
| reports are sent to Mattermost, Inc.         | - ``config.json`` setting: ``LogSettings`` > ``EnableDiagnostics`` > ``""``    |
|                                              | - Environment variable: ``MM_LOGSETTINGS_ENABLEDIAGNOSTICS``                   |
| - **true**: **(Default)** Send diagnostics   |                                                                                |
|   and error reports.                         |                                                                                |
| - **false**: Diagnostics and error reports   |                                                                                |
|   aren't sent.                               |                                                                                |
+----------------------------------------------+--------------------------------------------------------------------------------+

.. note::

  See the :ref:`telemetry <administration-guide/manage/telemetry:error and diagnostics reporting feature>` docummentation for details on the information Mattermost collects.

.. config:setting:: enable-verbose-diagnostics
  :displayname: Enable general verbose diagnostics (General Logging)
  :systemconsole: N/A
  :configjson: .LogSettings.VerboseDiagnostics
  :environment: MM_LOGSETTINGS_VERBOSEDIAGNOSTICS
  :description: Configure whether to send verbose general diagnostics information.

  - **true**: Send verbose diagnostics information.
  - **false**: **(Default)** Verbose diagnostics information isn't sent.

Enable verbose diagnostics
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------------------------------+---------------------------------------------------------------------------------+
| Whether or not verbose general diagnostics   | - System Config path: N/A                                                       |
| information is sent.                         | - ``config.json`` setting: ``LogSettings`` > ``VerboseDiagnostics`` > ``false`` |
|                                              | - Environment variable: ``MM_LOGSETTINGS_VERBOSEDIAGNOSTICS``                   |
| - **true**: Send verbose diagnostics         |                                                                                 |
|   information.                               |                                                                                 |
| - **false**: **(Default)** Verbose           |                                                                                 |
|   diagnostics information isn't sent.        |                                                                                 |
+----------------------------------------------+---------------------------------------------------------------------------------+

.. config:setting:: enable-sentry
  :displayname: Enable general Sentry reporting (General Logging)
  :systemconsole: N/A
  :configjson: .LogSettings.EnableSentry
  :environment: MM_LOGSETTINGS_ENABLESENTRY
  :description: Configure whether to send general error reports to Sentry.

  - **true**: **(Default)** Send error reports to Sentry. Default matches the EnableDiagnostics setting.
  - **false**: Error reports are not sent to Sentry.

Enable Sentry reporting
^^^^^^^^^^^^^^^^^^^^^^^^

+----------------------------------------------+--------------------------------------------------------------------------------+
| Whether or not general error reports are     | - System Config path: N/A                                                      |
| sent to Sentry.                              | - ``config.json`` setting: ``LogSettings`` > ``EnableSentry`` > ``true``       |
|                                              | - Environment variable: ``MM_LOGSETTINGS_ENABLESENTRY``                        |
| - **true**: **(Default)** Send error reports |                                                                                |
|   to Sentry. Default matches the             |                                                                                |
|   EnableDiagnostics setting.                 |                                                                                |
| - **false**: Error reports are not sent      |                                                                                |
|   to Sentry.                                 |                                                                                |
+----------------------------------------------+--------------------------------------------------------------------------------+

----

Notification logging
~~~~~~~~~~~~~~~~~~~~~

.. important::

  **From Mattermost v11, notification log settings have been consolidated into the standard console logs and mattermost.log file**. You can no longer disable notification logging without using advanced logging settings, as the main log level setting now controls both server and notification logs.

  You can use the ``AdvancedLoggingJSON`` configuration with discrete notification log levels: ``NotificationError``, ``NotificationWarn``, ``NotificationInfo``, ``NotificationDebug``, and ``NotificationTrace`` to split notification logs into separate files and reduce troubleshooting noise. See :ref:`Advanced Logging <administration-guide/manage/logging:advanced logging>` for details.

The following configuration settings apply only to Mattermost server versions prior to v11.0.

You can configure logging specifically for Mattermost notifications by editing the ``config.json`` file as described in the following tables. These settings operate independently from the main ``LogSettings`` and allow you to customize logging behavior specifically for the notification subsystem. Changes to these configuration settings require a server restart before taking effect.

.. config:setting:: output-logs-to-console
  :displayname: Output notification logs to console (Notification Logging)
  :systemconsole: N/A
  :configjson: .NotificationLogSettings.EnableConsole
  :environment: MM_NOTIFICATIONLOGSETTINGS_ENABLECONSOLE

  - **true**: **(Default)** Notification logs are written to the console based on the `console log level <#console-log-level>`__ configuration.
  - **false**: Output log messages aren’t written to the console.

Output logs to console
^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+---------------------------------------------------------------------------------------+
| Configure Mattermost to output notification   | - System Config path: N/A                                                             |
| logs to the console.                          | - ``config.json`` setting: ``NotificationLogSettings`` > ``EnableConsole`` > ``true`` |
|                                               | - Environment variable: ``MM_NOTIFICATIONLOGSETTINGS_ENABLECONSOLE``                  |
| - **true**: **(Default)** Output log messages |                                                                                       |
|   are written to the console based on the     |                                                                                       |
|   `console log level <#console-log-level>`__  |                                                                                       |
|   configuration. The server writes messages   |                                                                                       |
|   to the standard output stream (stdout).     |                                                                                       |
| - **false**: Output log messages aren't       |                                                                                       |
|   written to the console.                     |                                                                                       |
+-----------------------------------------------+---------------------------------------------------------------------------------------+

.. config:setting:: console-log-level
  :displayname: Console notification log level (Notification Logging)
  :systemconsole: N/A
  :configjson: .NotificationLogSettings.ConsoleLevel
  :environment: MM_NOTIFICATIONLOGSETTINGS_CONSOLELEVEL
  :description: The level of detail in notification log events written when Mattermost outputs log messages to the console.

  - **DEBUG**: **(Default)** Outputs verbose detail for developers debugging issues.
  - **ERROR**: Outputs only error messages.
  - **INFO**: Outputs general error messages and information around startup and initialization.

Console log level
^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+-----------------------------------------------------------------------------------------+
| The level of detail in notification log       | - System Config path: N/A                                                               |
| events written when Mattermost outputs log    | - ``config.json`` setting: ``NotificationLogSettings`` > ``ConsoleLevel`` > ``"DEBUG"`` |
| messages to the console.                      | - Environment variable: ``MM_NOTIFICATIONLOGSETTINGS_CONSOLELEVEL``                     |
|                                               |                                                                                         |
| - **DEBUG**: **(Default)** Outputs verbose    |                                                                                         |
|   detail for developers debugging issues.     |                                                                                         |
| - **ERROR**: Outputs only error messages.     |                                                                                         |
| - **INFO**: Outputs error messages and        |                                                                                         |
|   information around startup and              |                                                                                         |
|   initialization.                             |                                                                                         |
+-----------------------------------------------+-----------------------------------------------------------------------------------------+

.. config:setting:: output-console-logs-as-json
  :displayname: Output notification console logs as JSON (Notification Logging)
  :systemconsole: N/A
  :configjson: .NotificationLogSettings.ConsoleJson
  :environment: MM_NOTIFICATIONLOGSETTINGS_CONSOLEJSON
  :description: Configure Mattermost to output notification console logs as JSON.

  - **true**: **(Default)** Notification events are written in a machine-readable JSON format.
  - **false**: Logged events are written in plain text.

Output console logs as JSON
^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+---------------------------------------------------------------------------------------+
| Configure Mattermost to output notification   | - System Config path: N/A                                                             |
| console logs as JSON.                         | - ``config.json`` setting: ``NotificationLogSettings`` > ``ConsoleJson`` > ``true``   |
|                                               | - Environment variable: ``MM_NOTIFICATIONLOGSETTINGS_CONSOLEJSON``                    |
| - **true**: **(Default)** Logged events are   |                                                                                       |
|   written in a machine-readable JSON format.  |                                                                                       |
| - **false**: Logged events are written in     |                                                                                       |
|   plain text.                                 |                                                                                       |
+-----------------------------------------------+---------------------------------------------------------------------------------------+

Typically set to **true** in a production environment.

.. config:setting:: colorize-plain-text-console-logs
  :displayname: Colorize plain text notification console logs (Notification Logging)
  :systemconsole: N/A
  :configjson: .NotificationLogSettings.EnableColor
  :environment: MM_NOTIFICATIONLOGSETTINGS_ENABLECOLOR
  :description: Enables system admins to display plain text general log level details in color.

  - **true**: When logged notification events are output to the console as plain text, colorize log levels details.
  - **false**: **(Default)** Plain text log details aren't colorized in the console.

Colorize plain text console logs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+----------------------------------------------------------------------------------------+
| Enables system admins to display plain text   | - System Config path: N/A                                                              |
| notification log level details in color.      | - ``config.json`` setting: ``NotificationLogSettings`` > ``EnableColor`` > ``false``   |
|                                               | - Environment variable: ``MM_NOTIFICATIONLOGSETTINGS_ENABLECOLOR``                     |
| - **true**: When logged events are output to  |                                                                                        |
|   the console as plain text, colorize log     |                                                                                        |
|   levels details.                             |                                                                                        |
| - **false**: **(Default)** Plain text log     |                                                                                        |
|   details aren't colorized in the console.    |                                                                                        |
+-----------------------------------------------+----------------------------------------------------------------------------------------+

.. config:setting:: output-logs-to-file
  :displayname: Output notification logs to file (Notification Logging)
  :systemconsole: N/A
  :configjson: .NotificationLogSettings.EnableFile
  :environment: MM_NOTIFICATIONLOGSETTINGS_ENABLEFILE
  :description: Configure Mattermost to output notification console logs to a file.

  - **true**: **(Default)** Notification events are written based on the `file log level <#file-log-level>`__ configuration to a ``notifications.log`` file located in the directory configured via file location.
  - **false**: Logged events aren’t written to a file.

Output logs to file
^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+---------------------------------------------------------------------------------------+
| Configure Mattermost to output notification   | - System Config path: N/A                                                             |
| console logs to a file.                       | - ``config.json`` setting: ``NotificationLogSettings`` > ``EnableFile`` > ``true``    |
|                                               | - Environment variable: ``MM_NOTIFICATIONLOGSETTINGS_ENABLEFILE``                     |
| - **true**: **(Default)** Logged events are   |                                                                                       |
|   written based on the                        |                                                                                       |
|   `file log level <#file-log-level>`__        |                                                                                       |
|   configuration to a ``notifications.log``    |                                                                                       |
|   file located in the directory configured    |                                                                                       |
|   via ``file location``.                      |                                                                                       |
| - **false**: Logged events aren't written to  |                                                                                       |
|   a file.                                     |                                                                                       |
+-----------------------------------------------+---------------------------------------------------------------------------------------+

.. config:setting:: file-log-directory
  :displayname: Notification file log directory (Notification Logging)
  :systemconsole: N/A
  :configjson: .NotificationLogSettings.FileLocation
  :environment: MM_NOTIFICATIONLOGSETTINGS_FILELOCATION
  :description: The location of the notification log files. Default value is **./logs**.

File log directory
^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+-------------------------------------------------------------------------------------+
| The location of the notification log files.   | - System Config path: N/A                                                           |
|                                               | - ``config.json`` setting: ``NotificationLogSettings`` > ``FileLocation`` > ``""``  |
| String input. If left blank, log files are    | - Environment variable: ``MM_NOTIFICATIONLOGSETTINGS_FILELOCATION``                 |
| stored in the ``./logs`` directory.           |                                                                                     |
+-----------------------------------------------+-------------------------------------------------------------------------------------+

.. note::

  The path you configure must exist, and Mattermost must have write permissions for this directory.

.. config:setting:: file-log-level
  :displayname: Notification file log level (Notification Logging)
  :systemconsole: N/A
  :configjson: .NotificationLogSettings.FileLevel
  :environment: MM_NOTIFICATIONLOGSETTINGS_FILELEVEL
  :description: The level of detail in notification log events when Mattermost outputs log messages to a file.

  - **DEBUG**: Outputs verbose detail for developers debugging issues.
  - **ERROR**: Outputs only error messages.
  - **INFO**: **(Default)** Outputs error messages and information around startup and initialization.

File log level
^^^^^^^^^^^^^^

+-------------------------------------------------+--------------------------------------------------------------------------------------+
| The level of detail in notification log events  | - System Config path: N/A                                                            |
| when Mattermost outputs log messages to a file. | - ``config.json`` setting: ``NotificationLogSettings`` > ``FileLevel`` > ``"INFO"``  |
|                                                 | - Environment variable: ``MM_NOTIFICATIONLOGSETTINGS_FILELEVEL``                     |
| - **DEBUG**: Outputs verbose detail for         |                                                                                      |
|   developers debugging issues.                  |                                                                                      |
| - **ERROR**: Outputs only error messages.       |                                                                                      |
| - **INFO**: **(Default)** Outputs error         |                                                                                      |
|   messages and information around startup       |                                                                                      |
|   and initialization.                           |                                                                                      |
+-------------------------------------------------+--------------------------------------------------------------------------------------+

.. config:setting:: output-file-logs-as-json
  :displayname: Output notification file logs as JSON (Notification Logging)
  :systemconsole: N/A
  :configjson: .NotificationLogSettings.FileJson
  :environment: MM_NOTIFICATIONLOGSETTINGS_FILEJSON
  :description: Configure Mattermost to output notification file logs as JSON.

  - **true**: **(Default)** Notification events are written in a machine-readable JSON format.
  - **false**: Logged events are written in plain text.

Output file logs as JSON
^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+------------------------------------------------------------------------------------+
| Configure Mattermost to output notification   | - System Config path: N/A                                                          |
| file logs as JSON.                            | - ``config.json`` setting: ``NotificationLogSettings`` > ``FileJson`` > ``true``   |
|                                               | - Environment variable: ``MM_NOTIFICATIONLOGSETTINGS_FILEJSON``                    |
| - **true**: **(Default)** Logged events are   |                                                                                    |
|   written in a machine-readable JSON format.  |                                                                                    |
| - **false**: Logged events are written in     |                                                                                    |
|   plain text.                                 |                                                                                    |
+-----------------------------------------------+------------------------------------------------------------------------------------+

.. config:setting:: output-logs-to-multiple-targets
  :displayname: Output notification logs to multiple targets (Notification Logging)
  :systemconsole: N/A
  :configjson: .NotificationLogSettings.AdvancedLoggingJSON
  :environment: MM_NOTIFICATIONLOGSETTINGS_ADVANCEDLOGGINGJSON
  :description: Configure Mattermost to allow any combination of console, local file, syslog, and TCP socket targets, and send notification log records to multiple targets.

Output logs to multiple targets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+-----------------------------------------------------------------------------------------------+
| Configure Mattermost to allow any combination | - System Config path: N/A                                                                     |
| of console, local file, syslog, and TCP       | - ``config.json`` setting: ``NotificationLogSettings`` > ``AdvancedLoggingJSON`` > ``": ""``  |
| socket targets, and send notification log     | - Environment variable: ``MM_NOTIFICATIONLOGSETTINGS_ADVANCEDLOGGINGJSON``                    |
| records to multiple targets.                  |                                                                                               |
|                                               |                                                                                               |
| String input can contain a filespec to        |                                                                                               |
| another configuration file, a database DSN,   |                                                                                               |
| or JSON.                                      |                                                                                               |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------+

----

Audit logging
~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-plus.rst
  :start-after: :nosearch:

Configure audit logging by going to **System Console > Compliance > Audit Logging**, or by editing the ``config.json`` file as described in the following tables. These settings operate independently from the main ``LogSettings`` and allow you to customize logging behavior specifically for the audit subsystem. Changes to these configuration settings require a server restart before taking effect.

.. config:setting:: auditlog-fileenabled
  :displayname: Output audit logs to file (Audit Logging)
  :systemconsole: Compliance > Audit Logging
  :configjson: .ExperimentalAuditSettings.FileEnabled
  :environment: MM_EXPERIMENTALAUDITSETTINGS_FILEENABLED
  :description: Whether to write audit log files to disk.

  - **true**: Logged events are written to the file specified by the audit file name configuration setting.
  - **false**: **(Default)** Audit log files aren't written.

Output audit logs to file
^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------------------------------------------+----------------------------------------------------------------------------------------+
| Whether to write audit log files to disk.        | - System Config path: **Compliance > Audit Logging**                                   |
|                                                  | - ``config.json`` setting: ``ExperimentalAuditSettings`` > ``FileEnabled`` > ``false`` |
| - **true**: Logged events are written to the     | - Environment variable: ``MM_EXPERIMENTALAUDITSETTINGS_FILEENABLED``                   |
|   file specified by the audit file name          |                                                                                        |
|   configuration setting.                         |                                                                                        |
| - **false**: **(Default)** Audit log files       |                                                                                        |
|   aren't written.                                |                                                                                        |
+--------------------------------------------------+----------------------------------------------------------------------------------------+

.. note::

  When ``FileEnabled`` is set to **true**, then the `audit file name <#auditlog-filename>`__ must be set.

.. config:setting:: auditlog-filename
  :displayname: Audit file name (Audit Logging)
  :systemconsole: Compliance > Audit Logging
  :configjson: .ExperimentalAuditSettings.FileName
  :environment: MM_EXPERIMENTALAUDITSETTINGS_FILENAME
  :description: The name of the audit log file.

Audit file name
^^^^^^^^^^^^^^^

+--------------------------------------------------+-----------------------------------------------------------------------------------+
| The name of the audit log files.                 | - System Config path: **Compliance > Audit Logging**                              |
|                                                  | - ``config.json`` setting: ``ExperimentalAuditSettings`` > ``FileName`` > ``""``  |
| The path that you set to the audit file must     | - Environment variable: ``MM_EXPERIMENTALAUDITSETTINGS_FILENAME``                 |
| exist and Mattermost must have write             |                                                                                   |
| permissions in it.                               |                                                                                   |
|                                                  |                                                                                   |
| **Example:** ``/var/log/mattermost_audit.log``   |                                                                                   |
+--------------------------------------------------+-----------------------------------------------------------------------------------+

.. note::

  The file name must be set to `enable <#auditlog-fileenabled>`__ audit logging.

.. config:setting:: auditlog-filemaxsizemb
  :displayname: Maximum audit file size (Audit Logging)
  :systemconsole: Compliance > Audit Logging
  :configjson: .ExperimentalAuditSettings.FileMaxSizeMB
  :environment: MM_EXPERIMENTALAUDITSETTINGS_FILEMAXSIZEMB
  :description: The maximum size in megabytes for audit log files before they are rotated. Default is 100 MB.

Maximum file size
^^^^^^^^^^^^^^^^^

+--------------------------------------------------+----------------------------------------------------------------------------------------+
| The maximum size in megabytes for audit log      | - System Config path: **Compliance > Audit Logging**                                   |
| files before they are rotated.                   | - ``config.json`` setting: ``ExperimentalAuditSettings`` > ``FileMaxSizeMB`` > ``100`` |
|                                                  | - Environment variable: ``MM_EXPERIMENTALAUDITSETTINGS_FILEMAXSIZEMB``                 |
| Numerical input. Default is **100** MB.          |                                                                                        |
+--------------------------------------------------+----------------------------------------------------------------------------------------+

.. config:setting:: auditlog-filemaxagedays
  :displayname: Maximum audit file age (Audit Logging)
  :systemconsole: Compliance > Audit Logging
  :configjson: .ExperimentalAuditSettings.FileMaxAgeDays
  :environment: MM_EXPERIMENTALAUDITSETTINGS_FILEMAXAGEDAYS
  :description: The maximum age in days for audit log files before they are deleted. Default is 0 (no limit).

Maximum file age
^^^^^^^^^^^^^^^^

+--------------------------------------------------+----------------------------------------------------------------------------------------+
| The maximum age in days for audit log files      | - System Config path: **Compliance > Audit Logging**                                   |
| before they are deleted.                         | - ``config.json`` setting: ``ExperimentalAuditSettings`` > ``FileMaxAgeDays`` > ``0``  |
|                                                  | - Environment variable: ``MM_EXPERIMENTALAUDITSETTINGS_FILEMAXAGEDAYS``                |
| Numerical input. Default is **0** (no limit).    |                                                                                        |
+--------------------------------------------------+----------------------------------------------------------------------------------------+

.. config:setting:: auditlog-filemaxbackups
  :displayname: Maximum audit file backups (Audit Logging)
  :systemconsole: Compliance > Audit Logging
  :configjson: .ExperimentalAuditSettings.FileMaxBackups
  :environment: MM_EXPERIMENTALAUDITSETTINGS_FILEMAXBACKUPS
  :description: The maximum number of audit log file backups to retain. Default is 0 (no limit).

Maximum file backups
^^^^^^^^^^^^^^^^^^^^

+--------------------------------------------------+----------------------------------------------------------------------------------------+
| The maximum number of audit log file backups     | - System Config path: **Compliance > Audit Logging**                                   |
| to retain.                                       | - ``config.json`` setting: ``ExperimentalAuditSettings`` > ``FileMaxBackups`` > ``0``  |
|                                                  | - Environment variable: ``MM_EXPERIMENTALAUDITSETTINGS_FILEMAXBACKUPS``                |
| Numerical input. Default is **0** (no limit).    |                                                                                        |
+--------------------------------------------------+----------------------------------------------------------------------------------------+

.. config:setting:: auditlog-filecompress
  :displayname: Compress audit log files (Audit Logging)
  :systemconsole: Compliance > Audit Logging
  :configjson: .ExperimentalAuditSettings.FileCompress
  :environment: MM_EXPERIMENTALAUDITSETTINGS_FILECOMPRESS
  :description: Whether to compress rotated audit log files.

  - **true**: Rotated audit log files are compressed.
  - **false**: **(Default)** Rotated audit log files aren't compressed.

Compress audit log files
^^^^^^^^^^^^^^^^^^^^^^^^

+--------------------------------------------------+-------------------------------------------------------------------------------------------+
| Whether to compress rotated audit log files.     | - System Config path: **Compliance > Audit Logging**                                      |
|                                                  | - ``config.json`` setting: ``ExperimentalAuditSettings`` > ``FileCompress`` > ``false``   |
| - **true**: Rotated audit log files are          | - Environment variable: ``MM_EXPERIMENTALAUDITSETTINGS_FILECOMPRESS``                     |
|   compressed.                                    |                                                                                           |
| - **false**: **(Default)** Rotated audit log     |                                                                                           |
|   files aren't compressed.                       |                                                                                           |
+--------------------------------------------------+-------------------------------------------------------------------------------------------+

.. config:setting:: auditlog-filemaxqueuesize
  :displayname: Audit log queue size (Audit Logging)
  :systemconsole: Compliance > Audit Logging
  :configjson: .ExperimentalAuditSettings.FileMaxQueueSize
  :environment: MM_EXPERIMENTALAUDITSETTINGS_FILEMAXQUEUESIZE
  :description: The maximum number of audit log entries that can be queued. Default is 1000.

Audit log queue size
^^^^^^^^^^^^^^^^^^^^

+--------------------------------------------------+--------------------------------------------------------------------------------------------+
| The maximum number of audit log entries that     | - System Config path: **Compliance > Audit Logging**                                       |
| can be queued.                                   | - ``config.json`` setting: ``ExperimentalAuditSettings`` > ``FileMaxQueueSize`` > ``1000`` |
|                                                  | - Environment variable: ``MM_EXPERIMENTALAUDITSETTINGS_FILEMAXQUEUESIZE``                  |
| Numerical input. Default is **1000**.            |                                                                                            |
+--------------------------------------------------+--------------------------------------------------------------------------------------------+

.. config:setting:: auditlog-certificate
  :displayname: Audit log certificate (Audit Logging)
  :systemconsole: N/A
  :configjson: .ExperimentalAuditSettings.Certificate
  :environment: MM_EXPERIMENTALAUDITSETTINGS_CERTIFICATE
  :description: Certificate configuration for audit logging. Default is blank.

Audit log certificate
^^^^^^^^^^^^^^^^^^^^^

+--------------------------------------------------+-------------------------------------------------------------------------------------------+
| Certificate configuration for audit logging.     | - System Config path: N/A                                                                 |
|                                                  | - ``config.json`` setting: ``ExperimentalAuditSettings`` > ``Certificate`` > ``""``       |
| String input. Default is blank.                  | - Environment variable: ``MM_EXPERIMENTALAUDITSETTINGS_CERTIFICATE``                      |
+--------------------------------------------------+-------------------------------------------------------------------------------------------+

.. config:setting:: auditlog-advancedloggingjson
  :displayname: Output audit logs to multiple targets (Audit Logging)
  :systemconsole: Compliance > Audit Logging
  :configjson: .ExperimentalAuditSettings.AdvancedLoggingJSON
  :environment: MM_EXPERIMENTALAUDITSETTINGS_ADVANCEDLOGGINGJSON
  :description: Configures Mattermost to output audit log records to multiple targets.

Output audit logs to multiple targets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+--------------------------------------------------+---------------------------------------------------------------------------------------------+
| Configures Mattermost to output audit log        | - System Config path: **Compliance > Audit Logging**                                        |
| records to multiple targets.                     | - ``config.json`` setting: ``ExperimentalAuditSettings`` > ``AdvancedLoggingJSON`` > ``{}`` |
|                                                  | - Environment variable: ``MM_EXPERIMENTALAUDITSETTINGS_ADVANCEDLOGGINGJSON``                |
+--------------------------------------------------+---------------------------------------------------------------------------------------------+

.. note::

  - See the :doc:`Mattermost logging </administration-guide/manage/logging>` documentation for details on advanced logging configuration. These targets have been chosen as they support the vast majority of log aggregators, and other log analysis tools, without needing additional software installed.
  - Audit logs are recorded asynchronously to reduce latency to the caller.
  - Advanced audit logging supports hot-reloading of logger configuration.

----

Session lengths
---------------

With self-hosted deployments, user sessions are cleared when a user tries to log in, and sessions are cleared every 24 hours from the sessions database table. Configure session lengths by going to **System Console > Environment > Session Lengths**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: extend-session-length-with-activity
  :displayname: Extend session length with activity (Session Lengths)
  :systemconsole: Environment > Session Lengths
  :configjson: .ServiceSettings.ExtendSessionLengthWithActivity
  :environment: MM_SERVICESETTINGS_EXTENDSESSIONLENGTHWITHACTIVITY

  - **true**: **(Default)** Sessions are automatically extended when users are active in their Mattermost client.
  - **false**: Sessions won't extend with activity in Mattermost.

Extend session length with activity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| Improves the user experience by extending sessions and keeping | - System Config path: **Environment > Session Lengths**                                         |
| users logged in if they are active in their Mattermost apps.   | - ``config.json`` setting: ``ServiceSettings`` > ``ExtendSessionLengthWithActivity`` > ``true`` |
|                                                                | - Environment variable: ``MM_SERVICESETTINGS_EXTENDSESSIONLENGTHWITHACTIVITY``                  |
| - **true**: **(Default)** Sessions are automatically           |                                                                                                 |
|   extended when users are active in their Mattermost           |                                                                                                 |
|   client. User sessions only expire when users aren’t active   |                                                                                                 |
|   in their Mattermost client for the entire duration of the    |                                                                                                 |
|   session lengths defined.                                     |                                                                                                 |
| - **false**: Sessions won't extend with activity in            |                                                                                                 |
|   Mattermost. User sessions immediately expire at the          |                                                                                                 |
|   end of the session length or based on the                    |                                                                                                 |
|   `session idle timeout <#session-idle-timeout>`__ configured. |                                                                                                 |
+----------------------------------------------------------------+-------------------------------------------------------------------------------------------------+

.. config:setting:: terminate-sessions-on-password-change
  :displayname: Terminate sessions on password change (Session Lengths)
  :systemconsole: Environment > Session Lengths
  :configjson: .ServiceSettings.TerminateSessionsOnPasswordChange
  :environment: MM_SERVICESETTINGS_TERMINATESESSIONSONPASSWORDCHANGE

  - **true**: **(Default for new deployments)** Session revocation is enabled. All sessions of a user expire if their password is changed (by themselves or a system admin). If the password change is initiated by the user, their current session isn't terminated.
  - **false**: **(Default for existing deployments)** Session revocation is disabled. When users change their password, only the user's current session is revoked. When a system admin changes the user's password, none of the user's sessions are revoked.

Terminate sessions on password change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Enable or disable session revocation when a user's             | - System Config path: **Environment > Session Lengths**                                           |
| password changes.                                              | - ``config.json`` setting: ``ServiceSettings`` > ``TerminateSessionsOnPasswordChange`` > ``true`` |
|                                                                | - Environment variable: ``MM_SERVICESETTINGS_TERMINATESESSIONSONPASSWORDCHANGE``                  |
| - **true**: **(Default for new deployments)**                  |                                                                                                   |
|   Session revocation is enabled.                               |                                                                                                   |
|   All sessions of a user expire if their password is changed   |                                                                                                   |
|   (by themselves or by a system admin). If the password change |                                                                                                   |
|   is initiated by the user, their current session isn't        |                                                                                                   |
|   terminated.                                                  |                                                                                                   |
| - **false**: **(Default for existing deployments)**            |                                                                                                   |
|   Session revocation is disabled.                              |                                                                                                   |
|   When users change their password, only the user's current    |                                                                                                   |
|   session is revoked. When a system admin changes the user's   |                                                                                                   |
|   password, none of the user's sessions are revoked.           |                                                                                                   |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

.. config:setting:: session-length-for-adldap-and-email
  :displayname: Session length for AD/LDAP and email (Session Lengths)
  :systemconsole: Environment > Session Lengths
  :configjson: .ServiceSettings.SessionLengthWebInHours
  :environment: MM_SERVICESETTINGS_SESSIONLENGTHWEBINHOURS

  Set the number of hours counted from the last time a user entered their credentials into the web app or the desktop app to the expiry of the user’s session on email and AD/LDAP authentication.
  Default is **720** hours.

Session length for AD/LDAP and email
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Set the number of hours counted from the last time a user      | - System Config path: **Environment > Session Lengths**                                |
| entered their credentials into the web app or the desktop      | - ``config.json`` setting: ``ServiceSettings`` > ``SessionLengthWebInHours`` > ``720`` |
| app to the expiry of the user’s session on email and AD/LDAP   | - Environment variable: ``MM_SERVICESETTINGS_SESSIONLENGTHWEBINHOURS``                 |
| authentication.                                                |                                                                                        |
|                                                                |                                                                                        |
| Numerical input in hours. Default is **720** hours.            |                                                                                        |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------+

.. note::

  After changing this setting, the new session length takes effect after the next time the user enters their credentials.

.. config:setting:: session-length-for-mobile
  :displayname: Session length for mobile (Session Lengths)
  :systemconsole: Environment > Session Lengths
  :configjson: .ServiceSettings.SessionLengthMobileInHours
  :environment: MM_SERVICESETTINGS_SESSIONLENGTHMOBILEINHOURS
  :description: Set the number of hours counted from the last time a user entered their credential into the mobile app to the expiry of the user’s session. Default is **720** hours.

Session length for mobile
~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| Set the number of hours counted from the last time a user      | - System Config path: **Environment > Session Lengths**                                   |
| entered their credential into the mobile app to the expiry     | - ``config.json`` setting: ``ServiceSettings`` > ``SessionLengthMobileInHours`` > ``720`` |
| of the user’s session.                                         | - Environment variable: ``MM_SERVICESETTINGS_SESSIONLENGTHMOBILEINHOURS``                 |
|                                                                |                                                                                           |
| Numerical input in hours. Default is **720** hours.            |                                                                                           |
+----------------------------------------------------------------+-------------------------------------------------------------------------------------------+

.. note::

  After changing this setting, the new session length takes effect after the next time the user enters their credentials.

.. config:setting:: session-length-for-sso
  :displayname: Session length for SSO (Session Lengths)
  :systemconsole: Environment > Session Lengths
  :configjson: .ServiceSettings.SessionLengthSSOInHours
  :environment: MM_SERVICESETTINGS_SESSIONLENGTHSSOINHOURS
  :description: Set the number of hours from the last time a user entered their SSO credentials to the expiry of the user’s session. Default is **720** hours.

Session length for SSO
~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Set the number of hours from the last time a user entered      | - System Config path: **Environment > Session Lengths**                                  |
| their SSO credentials to the expiry of the user’s session.     | - ``config.json`` setting: ``ServiceSettings`` > ``SessionLengthSSOInHours`` > ``720``   |
| This setting defines the session length for SSO                | - Environment variable: ``MM_SERVICESETTINGS_SESSIONLENGTHSSOINHOURS``                   |
| authentication, such as SAML, GitLab, and OAuth 2.0.           |                                                                                          |
|                                                                |                                                                                          |
| Numerical input in hours. Default is **720** hours.            |                                                                                          |
| Numbers as decimals are also valid values for this             |                                                                                          |
| configuration setting.                                         |                                                                                          |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------+

.. note::

  - After changing this setting, the new session length takes effect after the next time the user enters their credentials.
  - If the authentication method is SAML, GitLab, or OAuth 2.0, users may automatically be logged back in to Mattermost if they are already logged in to SAML, GitLab, or with OAuth 2.0.

.. config:setting:: session-cache
  :displayname: Session cache (Session Lengths)
  :systemconsole: Environment > Session Lengths
  :configjson: .ServiceSettings.SessionCacheInMinutes
  :environment: MM_SERVICESETTINGS_SESSIONCACHEINMINUTES
  :description: Set the number of minutes to cache a session in memory. Default is **10** minutes.

Session cache
~~~~~~~~~~~~~

+----------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Set the number of minutes to cache a session in memory.        | - System Config path: **Environment > Session Lengths**                             |
|                                                                | - ``config.json`` setting: ``ServiceSettings`` > ``SessionCacheInMinutes`` > ``10`` |
| Numerical input in minutes. Default is **10** minutes.         | - Environment variable: ``MM_SERVICESETTINGS_SESSIONCACHEINMINUTES``                |
+----------------------------------------------------------------+-------------------------------------------------------------------------------------+

.. config:setting:: session-idle-timeout
  :displayname: Session idle timeout (Session Lengths)
  :systemconsole: N/A
  :configjson: .ServiceSettings.SessionIdleTimeoutInMinutes
  :environment: MM_SERVICESETTINGS_SESSIONIDLETIMEOUTINMINUTES

  The number of minutes from the last time a user was active on the system to the expiry of the user’s session. Once expired, the user will need to log in to continue.
  Default is **43200** minutes (30 days). Minimum value is 5 minutes, and a value of 0 sets the time as unlimited.

Session idle timeout
~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| The number of minutes from the last time a user was active     | - System Config path: N/A                                                                    |
| on the system to the expiry of the user’s session.             | - ``config.json`` setting: ``ServiceSettings`` > ``SessionIdleTimeoutInMinutes`` > ``43200`` |
| Once expired, the user will need to log in to continue.        | - Environment variable: ``MM_SERVICESETTINGS_SESSIONIDLETIMEOUTINMINUTES``                   |
|                                                                |                                                                                              |
| Numerical input in minutes. Default is **43200** (30 days).    |                                                                                              |
| Minimum value is **5** minutes, and a value of **0** sets      |                                                                                              |
| the time as unlimited.                                         |                                                                                              |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------+

.. note::

  - This setting has no effect when `extend session length with activity <#extend-session-length-with-activity>`__ is set to **true**.
  - This setting applies to the webapp and the desktop app. For mobile apps, use an :doc:`EMM provider </deployment-guide/mobile/deploy-mobile-apps-using-emm-provider>` to lock the app when not in use.                                                |
  - In :doc:`high availability mode </administration-guide/scale/high-availability-cluster-based-deployment>`, enable IP hash load balancing for reliable timeout measurement.

----

Performance monitoring
----------------------

.. include:: ../../_static/badges/entry-ent.rst
  :start-after: :nosearch:

With self-hosted deployments, you can configure performance monitoring by going to **System Console > Environment > Performance Monitoring**, or by editing the ``config.json`` file as described in the following tables.

.. code-block:: json

   {
     "MetricsSettings": {
       "Enable": false,
       "BlockProfileRate": 0,
       "ListenAddress": :8067,
       "EnableClientMetrics": false,
       "EnableNotificationMetrics": true,
       "ClientSideUserIds": ""
     }
   }

Changes to configuration settings in this section require a server restart before taking effect.

See the :doc:`performance monitoring </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>` documentation to learn more about setting up performance monitoring with Prometheus and Grafana. See the :doc:`collect performance metrics </administration-guide/scale/collect-performance-metrics>` documentation to learn more about using the Mattermost Metrics plugin.

.. config:setting:: enable-performance-monitoring
  :displayname: Enable performance monitoring (Performance Monitoring)
  :systemconsole: Environment > Performance Monitoring
  :configjson: .MetricsSettings.Enable
  :environment: MM_METRICSSETTINGS_ENABLE
  :description: Enable or disable performance monitoring.

  - **true**: Performance monitoring data collection and profiling is enabled.
  - **false**: **(Default)** Mattermost performance monitoring is disabled.

Enable performance monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------+---------------------------------------------------------------------------+
| Enable or disable performance monitoring.     | - System Config path: **Environment > Performance Monitoring**            |
|                                               | - ``config.json`` setting: ``MetricsSettings`` > ``Enable`` > ``false``   |
| - **true**: Performance monitoring data       | - Environment variable: ``MM_METRICSSETTINGS_ENABLE``                     |
|   collection and profiling is enabled.        |                                                                           |
| - **false**: **(Default)** Mattermost         |                                                                           |
|   performance monitoring is disabled.         |                                                                           |
+-----------------------------------------------+---------------------------------------------------------------------------+

See the :doc:`performance monitoring </administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring>` documentation to learn more.

.. config:setting:: enable-client-performance-monitoring
  :displayname: Enable client performance monitoring (Performance Monitoring)
  :systemconsole: Environment > Performance Monitoring
  :configjson: .MetricsSettings.EnableClientMetrics
  :environment: MM_METRICSSETTINGS_ENABLECLIENTMETRICS
  :description: Enable or disable client performance monitoring.

  - **true**: Client performance monitoring data collection and profiling is enabled.
  - **false**: **(Default)** Mattermost client performance monitoring is disabled.

Enable client performance monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+----------------------------------------------------------------------------------------+
| Enable or disable client performance monitoring.     | - System Config path: **Environment > Performance Monitoring**                         |
|                                                      | - ``config.json`` setting: ``MetricsSettings`` > ``EnableClientMetrics`` > ``false``   |
| - **true**: Client performance monitoring data       | - Environment variable: ``MM_METRICSSETTINGS_ENABLECLIENTMETRICS``                     |
|   collection and profiling is enabled.               |                                                                                        |
| - **false**: **(Default)** Mattermost                |                                                                                        |
|   client performance monitoring is disabled.         |                                                                                        |
+------------------------------------------------------+----------------------------------------------------------------------------------------+

.. config:setting:: client-side-user-ids
  :displayname: Client side user ids (Performance Monitoring)
  :systemconsole: Environment > Performance Monitoring
  :configjson: .MetricsSettings.ClientSideUserIds
  :environment: MM_METRICSSETTINGS_CLIENTSIDEUSERIDS
  :description: A list of comma-separated user ids you want to track for client side webapp metrics. Limited to 5. Blank by default.

Client side user ids
~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-------------------------------------------------------------------------+
| A list of comma-separated user IDs you want to track for      | - System Config path: **Environment > Performance Monitoring**          |
| client-side webapp metrics.                                   | - ``config.json`` setting: ``MetricsSettings`` > ``ClientSideUserIds``  |
|                                                               | - Environment variable: ``MM_METRICSSETTINGS_CLIENTSIDEUSERIDS``        |
| Limited to 5 user IDs. Blank by default.                      |                                                                         |
+---------------------------------------------------------------+-------------------------------------------------------------------------+

.. note::

  - This setting only applies when ``EnableClientMetrics`` is set to ``true``.
  - Each user ID should correspond to a valid user in the Mattermost system. For example, ``MM_METRICSSETTINGS_CLIENTSIDEUSERIDS="user1,user2,user3"``.
  - The total number of user IDs is limited to 5 to ensure performance. Adding more IDs can overwhelm Prometheus due to high label cardinality. To avoid performance issues, we recommend minimizing changes to this list.

.. config:setting:: listen-address-for-performance
  :displayname: Listen address for performance (Performance Monitoring)
  :systemconsole: Environment > Performance Monitoring
  :configjson: .MetricsSettings.ListenAddress
  :environment: MM_METRICSSETTINGS_LISTENADDRESS
  :description: The port the Mattermost server will listen on to expose performance metrics, when enabled. Default is port **8067**.

Listen address
~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The port the Mattermost server will listen on to expose       | - System Config path: **Environment > Performance Monitoring**                |
| performance metrics, when enabled.                            | - ``config.json`` setting: ``MetricsSettings`` > ``ListenAddress`` > ``8067`` |
|                                                               | - Environment variable: ``MM_METRICSSETTINGS_LISTENADDRESS``                  |
| Numerical input. Default is **8067**.                         |                                                                               |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

.. note::

  - ``ListenAddress`` accepts a port only. It doesn’t take an IP/host. If you need to restrict interfaces, do so via your OS firewall or reverse proxy.
  - The address uses a ``host:port`` format. Use ``:8067`` to listen on all interfaces on port **8067**, or use ``localhost:8067`` to restrict to **localhost** only.

.. config:setting:: block-profile-rate
  :displayname: Block profile rate (Performance Monitoring)
  :systemconsole: N/A
  :configjson: .MetricsSettings.BlockProfileRate
  :environment: MM_METRICSSETTINGS_BLOCKPROFILERATE
  :description: Control how often Mattermost collects data about delays caused by blocking operations within Mattermost (such as when one part of the program has to wait for another). Default is **0** (profiling is disabled).

Block profile rate
~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| Control how often Mattermost collects data about delays       | - System Config path: **N/A**                                                 |
| caused by blocking operations within Mattermost (such as      | - ``config.json`` setting: ``MetricsSettings`` > ``BlockProfileRate`` > ``0`` |
| when one part of the program has to wait for another).        | - Environment variable: ``MM_METRICSSETTINGS_BLOCKPROFILERATE``               |
| Default is **0** (profiling is disabled).                     |                                                                               |
|                                                               |                                                                               |
| The profiler aims to sample an average of one blocking        |                                                                               |
| event per rate nanoseconds spent blocked.                     |                                                                               |
|                                                               |                                                                               |
| Default is **0**.                                             |                                                                               |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

.. note::

  - This setting isn't available in the System Console and can only be set in ``config.json``.
  - Only adjust this if you’re diagnosing performance issues and know how to analyze profiling data. The value represents how frequently Mattermost records blocking events in its performance profile:

    - Set to 0 to record no blocking events (profiling is disabled).
    - Set to 1 to record every blocking event (profiling is fully enabled).
    - Set to a higher number to record only a fraction of events (useful for sampling instead of full profiling).

.. config:setting:: enable-notification-monitoring
  :displayname: Enable notification monitoring (Performance Monitoring)
  :systemconsole: Site Configuration > Notifications
  :configjson: .MetricsSettings.EnableNotificationMetrics
  :environment: MM_METRICSSETTINGS_ENABLENOTIFICATIONMETRICS
  :description: Control whether Mattermost collects notification metrics data for client-side web and desktop app users. Default is **true**.

Enable notification monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------+----------------------------------------------------------------------------------------------------+
| Enable or disable notification metrics data   | - System Config path: **Site Configuration > Notifications**                                       |
| collection.                                   | - ``config.json`` setting: ``MetricsSettings`` > ``EnableNotificationMetrics`` > ``true``          |
|                                               | - Environment variable: ``MM_METRICSSETTINGS_ENABLENOTIFICATIONMETRICS``                           |
| - **true**: **(Default)** Mattermost          |                                                                                                    |
|   notification data collection is enabled for |                                                                                                    |
|   client-side web and desktop app users.      |                                                                                                    |
| - **false**: Mattermost notification          |                                                                                                    |
|   data collection is disabled.                |                                                                                                    |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------+

.. note::

  - ``MetricsSettings.Enable`` must be set to ``true``
  - The ``NotificationMonitoring`` feature flag must be set to ``true``

See the :ref:`performance monitoring <administration-guide/scale/deploy-prometheus-grafana-for-performance-monitoring:getting started>` documentation
to learn more about Mattermost Notification Health metrics.

----

Developer
---------

With self-hosted deployments, you can configure developer mode by going to **System Console > Environment > Developer**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: enable-testing-commands
  :displayname: Enable testing commands (Developer)
  :systemconsole: Environment > Developer
  :configjson: .ServiceSettings.EnableTesting
  :environment: MM_SERVICESETTINGS_ENABLETESTING
  :description: Enable or disable the ``/test`` slash command.

  - **true**: **(Default)** The ``/test`` slash command is enabled to load test accounts and test data.
  - **false**:  The ``/test`` slash command is disabled.

Enable testing commands
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+--------------------------------------------------------------------------------+
| Enable or disable the ``/test`` slash command.    | - System Config path: **Environment > Developer**                              |
|                                                   | - ``config.json`` setting: ``ServiceSettings`` > ``EnableTesting`` > ``true``  |
| - **true**: **(Default)** The ``/test`` slash     | - Environment variable: ``MM_SERVICESETTINGS_ENABLETESTING``                   |
|   command is enabled to load test accounts        |                                                                                |
|   and test data.                                  |                                                                                |
| - **false**:  The ``/test`` slash command is      |                                                                                |
|   disabled.                                       |                                                                                |
+---------------------------------------------------+--------------------------------------------------------------------------------+

.. config:setting:: enable-developer-mode
  :displayname: Enable developer mode (Developer)
  :systemconsole: Environment > Developer
  :configjson: .ServiceSettings.EnableDeveloper
  :environment: MM_SERVICESETTINGS_ENABLEDEVELOPER
  :description: Enable or disable developer mode.

  - **true**: **(Default)** Javascript errors are shown in a banner at the top of Mattermost the user interface. Not recommended for use in production.
  - **false**: Users are not alerted to Javascript errors.

Enable developer mode
~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------+---------------------------------------------------------------------------------+
| Enable or disable developer mode.             | - System Config path: **Environment > Developer**                               |
|                                               | - ``config.json`` setting: ``ServiceSettings`` > ``EnableDeveloper`` > ``true`` |
| - **true**: **(Default)** Javascript errors   | - Environment variable: ``MM_SERVICESETTINGS_ENABLEDEVELOPER``                  |
|   are shown in a banner at the top of         |                                                                                 |
|   Mattermost the user interface.              |                                                                                 |
|   Not recommended for use in production.      |                                                                                 |
| - **false**: Users are not alerted to         |                                                                                 |
|   Javascript errors.                          |                                                                                 |
+-----------------------------------------------+---------------------------------------------------------------------------------+

.. config:setting:: enable-client-debugging
  :displayname: Enable client debugging (Developer)
  :systemconsole: Environment > Developer
  :configjson: .ServiceSettings.EnableClientPerformanceDebugging
  :environment: MM_SERVICESETTINGS_ENABLECLIENTPERFORMANCEDEBUGGING
  :description: Enable or disable client-side debugging settings found in *Settings > Advanced > Debugging* for individual users.

  - **true**: Those settings are visible and can be enabled by users.
  - **false**: **(Default)** Those settings are hidden and disabled.

Enable client debugging
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Enable or disable client-side debugging settings  | - System Config path: **Environment > Developer**                                                 |
| found in **Settings > Advanced > Debugging**      | - ``config.json`` setting: ``ServiceSettings`` > ``EnableClientPerformanceDebugging`` > ``false`` |
| for individual users.                             | - Environment variable: ``MM_SERVICESETTINGS_ENABLECLIENTPERFORMANCEDEBUGGING``                   |
|                                                   |                                                                                                   |
| - **true**: Those settings are visible and can    |                                                                                                   |
|   be enabled by users.                            |                                                                                                   |
| - **false**: **(Default)** Those settings are     |                                                                                                   |
|   hidden and disabled.                            |                                                                                                   |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------+

See the :ref:`client debugging <end-user-guide/preferences/manage-advanced-options:performance debugging>` documentation to learn more.

.. config:setting:: allow-untrusted-internal-connections
  :displayname: Allow untrusted internal connections (Developer)
  :systemconsole: Environment > Developer
  :configjson: .ServiceSettings.AllowedUntrustedInternalConnections
  :environment: MM_SERVICESETTINGS_ALLOWUNTRUSTEDINTERNALCONNECTIONS
  :description: This setting is a whitelist of local network addresses that can be requested by the Mattermost server.

Allow untrusted internal connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

  This setting is intended to prevent users located outside your local network from using the Mattermost server to request confidential data from inside your network. Care should be used when configuring this setting to prevent unintended access to your local network.

+-----------------------------------------------+----------------------------------------------------------------------------------------------------+
| Limit the ability for the Mattermost server   | - System Config path: **Environment > Developer**                                                  |
| to make untrusted requests within its local   | - ``config.json`` setting: ``ServiceSettings`` > ``AllowedUntrustedInternalConnections`` > ``""``  |
| network. A request is considered “untrusted”  | - Environment variable: ``MM_SERVICESETTINGS_ALLOWEDUNTRUSTEDINTERNALCONNECTIONS``                 |
| when it’s made on behalf of a client.         |                                                                                                    |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------+

This setting is a whitelist of local network addresses that can be requested by the Mattermost server. It’s configured as a whitespace-separated list of hostnames, IP addresses, and CIDR ranges that can be accessed.

Requests that can only be configured by system admins are considered trusted and won't be affected by this setting. Trusted URLs include ones used for OAuth login or for sending push notifications.

The following features make untrusted requests and are affected by this setting:

- Integrations using webhooks, slash commands, or message actions. This prevents them from requesting endpoints within the local network.
- Link previews. When a link to a local network address is posted in a chat message, this prevents a link preview from being displayed.
- The local :doc:`image proxy </deployment-guide/server/image-proxy>`. If the local image proxy is enabled, images located on the local network cannot be used by integrations or posted in chat messages.

Some examples of when you may want to modify this setting include:

- When installing a plugin that includes its own images, such as `Matterpoll <https://github.com/matterpoll/matterpoll>`__, you'll need to add the Mattermost server’s domain name to this list.
- When running a bot or webhook-based integration on your local network, you’ll need to add the hostname of the bot/integration to this list.
- If your network is configured in such a way that publicly-accessible web pages or images are accessed by the Mattermost server using their internal IP address, the hostnames for those servers must be added to this list.

.. note::

  - The public IP of the Mattermost application server itself is also considered a reserved IP.
  - Use whitespaces instead of commas to list the hostnames, IP addresses, or CIDR ranges. For example: ``webhooks.internal.example.com``, ``127.0.0.1``, or ``10.0.16.0/28``.
  - IP address and domain name rules are applied before host resolution.
  - CIDR rules are applied after host resolution, and only CIDR rules require DNS resolution.
  - Mattermost attempts to match IP addresses and hostnames without even resolving. If that fails, Mattermost resolve using the local resolver (by reading the ``/etc/hosts`` file first), then checking for matching CIDR rules. For example, if the domain “webhooks.internal.example.com” resolves to the IP address ``10.0.16.20``, a webhook with the URL ``https://webhooks.internal.example.com/webhook`` can be whitelisted using ``webhooks.internal.example.com``, or ``10.0.16.16/28``, but not ``10.0.16.20``.

Mobile security
---------------

.. include:: ../../_static/badges/ent-adv.rst
  :start-after: :nosearch:

From Mattermost v10.7 and mobile app v2.27, you can configure biometric authentication, prevent Mattermost use on jailbroken or rooted devices, and can block screen captures without relying on an EMM Provider. Configure these options by going to **System Console > Environment > Mobile Security**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart and require users to restart their mobile app or log out and back in before taking effect.

.. config:setting:: enable-biometric-authentication
  :displayname: Enable Biometric Authentication
  :systemconsole: Environment > Mobile Security
  :configjson: .NativeAppSettings.MobileEnableBiometrics
  :environment: MM_NATIVEAPPSETTINGS_MOBILEENABLEBIOMETRICS
  :description: Enforces biometric authentication (with PIN/passcode fallback) before accessing the app. Users will be prompted based on session activity and server switching rules.

    - **true**: Biometric authentication is enabled.
    - **false**: **(Default)** Biometric authentication is disabled.

Enable biometric authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------+-------------------------------------------------------------------------------------------+
| Enforce biometric authentication, with        | - System Config path: **Environment > Mobile Security**                                   |
| PIN/passcode fallback, before accessing       | - ``config.json`` setting: ``NativeAppSettings`` > ``MobileEnableBiometrics`` > ``false`` |
| the app. Users will be prompted based on      | - Environment variable: ``MM_NATIVEAPPSETTINGS_MOBILEENABLEBIOMETRICS``                   |
| session activity and server switching rules.  |                                                                                           |
|                                               |                                                                                           |
| - **true**: Biometric authentication is       |                                                                                           |
|   enabled.                                    |                                                                                           |
| - **false**: **(Default)** Biometric          |                                                                                           |
|   authentication is disabled.                 |                                                                                           |
+-----------------------------------------------+-------------------------------------------------------------------------------------------+

.. note::

  - Changing this configuration setting takes effect when mobile users restart their Mattermost mobile app or log out and log back in.
  - Users must authenticate in the following situations:

    - Adding a new server: When a new server is added to the mobile app and biometric authentication is enabled.
    - Opening the mobile app: At app launch when the active server requires authentication.
    - Returning after background use: After the app has been in the background for 5 minutes or more and the active server requires authentication.
    - Using multiple servers: When accessing a server for the first time, after 5 minutes of inactivity on a server, and when the last authentication attempt fails.

.. config:setting:: mobile-security-enabled
  :displayname: Enable Jailbreak/Root Protection
  :systemconsole: Environment > Mobile Security
  :configjson: .NativeAppSettings.MobileJailbreakProtection
  :environment: MM_NATIVEAPPSETTINGS_MOBILEJAILBREAKPROTECTION
  :description: Prevent access to the app on devices detected as jailbroken or rooted. If a device fails the security check, users will be denied access or prompted to switch to a compliant server.

    - **true**: Jailbreak/Root protection is enabled.
    - **false**: **(Default)** Jailbreak/Root protection is disabled.

Enable jailbreak/root protection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------+----------------------------------------------------------------------------------------------+
| Prevent access to the app on devices          | - System Config path: **Environment > Mobile Security**                                      |
| detected as jailbroken or rooted. If a        | - ``config.json`` setting: ``NativeAppSettings`` > ``MobileJailbreakProtection`` > ``false`` |
| device fails the security check, users will   | - Environment variable: ``MM_NATIVEAPPSETTINGS_MOBILEJAILBREAKPROTECTION``                   |
| be denied access or prompted to switch to a   |                                                                                              |
| compliant server.                             |                                                                                              |
|                                               |                                                                                              |
| - **true**: Jailbreak/Root protection is      |                                                                                              |
|   enabled.                                    |                                                                                              |
| - **false**: **(Default)** Jailbreak/Root     |                                                                                              |
|   protection is disabled.                     |                                                                                              |
+-----------------------------------------------+----------------------------------------------------------------------------------------------+

.. note::

  - Changing this configuration setting takes effect when mobile users restart their Mattermost mobile app or log out and log back in.
  - See the `Expo SDK documentation <https://docs.expo.dev/versions/latest/sdk/device/#deviceisrootedexperimentalasync>`_ to learn more about how checks are performed for this functionality.

.. config:setting:: mobile-security-enabled
  :displayname: Prevent Screen Capture
  :systemconsole: Environment > Mobile Security
  :configjson: .NativeAppSettings.MobilePreventScreenCapture
  :environment: MM_NATIVEAPPSETTINGS_MOBILEPREVENTSCREENCAPTURE
  :description: Block screenshots and screen recordings when using the mobile app. Screenshots will appear blank, and screen recordings will blur (iOS) or show a black screen (Android). Also applies when switching apps.

    - **true**: Screen capture blocking is enabled.
    - **false**: **(Default)** Screen capture blocking is disabled.

Prevent screen capture
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------+-----------------------------------------------------------------------------------------------+
| Block screenshots and screen recordings when  | - System Config path: **Environment > Mobile Security**                                       |
| using the mobile app. Screenshots will        | - ``config.json`` setting: ``NativeAppSettings`` > ``MobilePreventScreenCapture`` > ``false`` |
| appear blank, and screen recordings will      | - Environment variable: ``MM_NATIVEAPPSETTINGS_MOBILEPREVENTSCREENCAPTURE``                   |
| blur (iOS) or show a black screen (Android).  |                                                                                               |
| Also applies when switching apps.             |                                                                                               |
|                                               |                                                                                               |
| - **true**: Screen capture blocking is        |                                                                                               |
|   enabled.                                    |                                                                                               |
| - **false**: **(Default)** Screen capture     |                                                                                               |
|   blocking is disabled.                       |                                                                                               |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------+

.. note::

  Changing this configuration setting takes effect when mobile users restart their Mattermost mobile app or log out and log back in.

.. config:setting:: mobile-enable-secure-file-preview
  :displayname: Enable secure file preview on mobile (File sharing)
  :systemconsole: Site Configuration > File sharing and downloads
  :configjson: .FileSettings.MobileEnableSecureFilePreview
  :environment: MM_FILESETTINGS_MOBILEENABLESECUREFILEPREVIEW

  - **true**: Prevents file downloads, previews, and sharing for most file types. Allows in-app previews for PDFs, videos, and images only. Files are stored temporarily in the app's cache and cannot be exported or shared.
  - **false**: **(Default)** Secure file preview mode is disabled.

Enable secure file preview on mobile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting improves an organization's mobile security posture by restricting file access while still allowing essential file viewing capabilities.

+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| - **true**: Prevents file downloads, previews, and sharing for most file types,                                                       | - System Config path: **Site Configuration > File sharing and downloads**                         |
|   even when the                                                                                                                       | - ``config.json`` setting: ``FileSettings`` > ``MobileEnableSecureFilePreview`` > ``false``       |
|   :ref:`Allow file downloads on mobile <administration-guide/configure/site-configuration-settings:allow file downloads on mobile>`   | - Environment variable: ``MM_FILESETTINGS_MOBILEENABLESECUREFILEPREVIEW``                         |
|   configuration setting is enabled. Allows in-app previews for PDFs,                                                                  |                                                                                                   |
|   videos, and images only. Files are stored temporarily in the app's cache and cannot be exported or shared.                          |                                                                                                   |
| - **false**: **(Default)** Secure file preview mode is disabled.                                                                      |                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

.. note::
  Changing this configuration setting takes effect when mobile users restart their Mattermost mobile app or log out and log back in.

.. config:setting:: mobile-allow-pdf-link-navigation
  :displayname: Allow PDF link navigation on mobile (File sharing)
  :systemconsole: Site Configuration > File sharing and downloads
  :configjson: .FileSettings.MobileAllowPdfLinkNavigation
  :environment: MM_FILESETTINGS_MOBILEALLOWPDFLINKNAVIGATION

  - **true**: **(Default)** Enables tapping links inside PDFs on mobile when Secure File Preview Mode is active. Links will open in the device browser or supported app.
  - **false**: Disables link navigation in PDFs when Secure File Preview Mode is active.

Allow PDF link navigation on mobile
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| - **true**: **(Default)** Enables tapping links inside PDFs               | - System Config path: **Site Configuration > File sharing and downloads**                     |
|   on mobile when Secure File Preview Mode is active. Links will open      | - ``config.json`` setting: ``FileSettings`` > ``MobileAllowPdfLinkNavigation`` > ``true``     |
|   in the device browser or supported app.                                 | - Environment variable: ``MM_FILESETTINGS_MOBILEALLOWPDFLINKNAVIGATION``                      |
| - **false**: Disables link navigation in PDFs                             |                                                                                               |
|   when Secure File Preview Mode is active.                                |                                                                                               |
+---------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+

.. note::

  - Changing this configuration setting takes effect when mobile users restart their Mattermost mobile app or log out and log back in.
  - This setting has no effect when the `Secure file preview on mobile <#enable-secure-file-preview-on-mobile>`__ configuration setting is disabled.

----

config.json-only settings
-------------------------

The following self-hosted deployment settings are only configurable in the ``config.json`` file and are not available in the System Console.

.. config:setting:: disable-customer-portal-requests
  :displayname: Disable customer portal requests
  :systemconsole: N/A
  :configjson: .CloudSettings.Disable
  :environment: MM_CLOUDSETTINGS_DISABLE
  :description: Enable or disable server requests to the Mattermost Customer Portal.

    - **true**: **(Default)** Server-side requests made to the customer portal are disabled.
    - **false**: Server-side requests made to the customer portal are enabled, but will always fail in air-gapped and restricted environments.

Disable Customer Portal requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------+---------------------------------------------------------------------------+
| Enable or disable customer portal requests.   | - System Config path: **N/A**                                             |
|                                               | - ``config.json`` setting: ``CloudSettings`` > ``Disable`` > ``true,``    |
|                                               | - Environment variable: ``MM_CLOUDSETTINGS_DISABLE``                      |
| - **true**: **(Default)** Server-side         |                                                                           |
|   requests made to the customer portal are    |                                                                           |
|   disabled.                                   |                                                                           |
| - **false**: Server-side requests made to the |                                                                           |
|   Mattermost Customer Portal are enabled,     |                                                                           |
|   but will always fail in air-gapped and      |                                                                           |
|   restricted deployment environments.         |                                                                           |
+-----------------------------------------------+---------------------------------------------------------------------------+

.. note::

  Cloud admins can’t modify this configuration setting.

.. config:setting:: enable-api-team-deletion
  :displayname: Enable API team deletion (ServiceSettings)
  :systemconsole: N/A
  :configjson: .ServiceSettings.EnableAPITeamDeletion
  :environment: N/A
  :description: Allow permanent team deletion via API.

  - **true**: The ``api/v4/teams/{teamid}?permanent=true`` API endpoint can be called by team admins and system admins (or users with appropriate permissions), or by running the mmctl team delete command, to permanently delete a team.
  - **false**: **(Default)** The API endpoint cannot be called, but ``api/v4/teams/{teamid}`` can still be used to soft delete a team.

Enable API team deletion
~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Allow permanent team deletion via API.                          | - System Config path: N/A                                                              |
|                                                                 | - ``config.json`` setting: ``ServiceSettings`` > ``EnableAPITeamDeletion`` > ``false`` |
| - **true**: Team and system admins (or users with appropriate   | - Environment variable: N/A                                                            |
|   permissions) can call ``api/v4/teams/{teamid}?permanent=true``|                                                                                        |
|   or use ``mmctl team delete`` to permanently delete a team.    |                                                                                        |
| - **false**: **(Default)** Endpoint not available;              |                                                                                        |
|   ``api/v4/teams/{teamid}`` still soft deletes a team.          |                                                                                        |
+-----------------------------------------------------------------+----------------------------------------------------------------------------------------+

.. note::

  This setting isn’t available in the System Console and can only be set in ``config.json``.

.. config:setting:: enable-api-user-deletion
  :displayname: Enable API user deletion (ServiceSettings)
  :systemconsole: N/A
  :configjson: .ServiceSettings.EnableAPIUserDeletion
  :environment: N/A
  :description: Allow permanent user deletion via API.

  - **true**: The ``api/v4/users/{userid}?permanent=true`` API endpoint can be called by system admins (or users with appropriate permissions), or by running the mmctl user delete command, to permanently delete a user.
  - **false**: **(Default)** The API endpoint cannot be called, but ``api/v4/users/{userid}`` can still be used to soft delete a user.

Enable API user deletion
~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Allow permanent user deletion via API.                          | - System Config path: N/A                                                              |
|                                                                 | - ``config.json`` setting: ``ServiceSettings`` > ``EnableAPIUserDeletion`` > ``false`` |
| - **true**: System admins (or users with appropriate            | - Environment variable: N/A                                                            |
|   permissions) can call ``api/v4/users/{userid}?permanent=true``|                                                                                        |
|   or use ``mmctl user delete`` to permanently delete a user.    |                                                                                        |
| - **false**: **(Default)** Endpoint not available;              |                                                                                        |
|   ``api/v4/users/{userid}`` still soft deletes a user.          |                                                                                        |
+-----------------------------------------------------------------+----------------------------------------------------------------------------------------+

.. note::

  This setting isn’t available in the System Console and can only be set in ``config.json``.

.. config:setting:: enable-api-channel-deletion
  :displayname: Enable API channel deletion (ServiceSettings)
  :systemconsole: N/A
  :configjson: .ServiceSettings.EnableAPIChannelDeletion
  :environment: N/A
  :description: Allow permanent channel deletion via API.

  - **true**: The ``api/v4/channels/{channelid}?permanent=true`` API endpoint can be called by system admins (or users with appropriate permissions), or by running the mmctl channel delete command, to permanently delete a channel.
  - **false**: **(Default)** The API endpoint cannot be called, but ``api/v4/channels/{channelid}`` can still be used to soft delete a channel.

Enable API channel deletion
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| Allow permanent channel deletion via API.                       | - System Config path: N/A                                                                 |
|                                                                 | - ``config.json`` setting: ``ServiceSettings`` > ``EnableAPIChannelDeletion`` > ``false`` |
| - **true**: System admins (or users with appropriate            | - Environment variable: N/A                                                               |
|   permissions) can call                                         |                                                                                           |
|   ``api/v4/channels/{channelid}?permanent=true`` or use         |                                                                                           |
|   ``mmctl channel delete`` to permanently delete a channel.     |                                                                                           |
| - **false**: **(Default)** Endpoint not available;              |                                                                                           |
|   ``api/v4/channels/{channelid}`` still soft deletes a channel. |                                                                                           |
+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------+

.. note::

  This setting isn’t available in the System Console and can only be set in ``config.json``.

.. config:setting:: enable-desktop-app-developer-mode
  :displayname: Enable desktop app developer mode (ServiceSettings)
  :systemconsole: N/A
  :configjson: N/A
  :environment: N/A
  :description: Enable developer debugging options in the Mattermost desktop app. Disabled by default.

  - **true**: Developer debugging options are available in the Mattermost desktop app by going to the **View > Developer Tools** menu
  - **false**: **(Default)** Developer debugging options are unavailable in the Mattermost desktop app.

Enable desktop app developer mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From Desktop App v5.10, this setting enables developer debugging options available by going to the **View > Developer Tools** menu in the Mattermost desktop app.

This setting isn't available in the System Console and can only be enabled in ``config.json`` by setting the environment variable ``MM_DESKTOP_DEVELOPER_MODE`` to ``true``. This setting is disabled by default.

- **True**: Unlocks the following options in the Desktop App for the purposes of troubleshooting and debugging. You should only enable this setting if instructed to by a Mattermost developer:

  - **Browser Mode Only**: Completely disables the preload script and stops web app components from knowing they're in the desktop app. This option should be the best indicator of whether a web app component is causing performance and/or memory retention issues. This option disables notifications, cross-tab navigation, unread/mentions badges, the calls widget, and breaks resizing on macOS.
  - **Disable Notification Storage**: Turns off maps that hold references to unread notifications until they've been selected & read. This option is good for debugging in cases where Mattermost is holding onto too many references to unused notifications.
  - **Disable User Activity Monitor**: Turns off the interval that checks whether the user is away or not. This option is good for debugging whether a user's availability status is causing unexpected desktop app behavior.
  - **Disable Context Menu**: Turns off the context menu attached to the BrowserViews. This option is good as a library santity check.
  - **Force Legacy Messaging API**: Forces the app to revert back to the old messaging API instead of the newer contextBridge API. This option is a good santity check to confirm whether the new API is responsible for holding onto memory.
  - **Force New Messaging API**: Forces the app to use the contextBridge API and completely disables the legacy one. This option forces off listeners for the legacy API.

- **False**: **(Default)** Developer debugging options are locked and unavailable in the Desktop App.

Redis cache backend
~~~~~~~~~~~~~~~~~~~

.. include:: ../../_static/badges/ent-adv.rst
  :start-after: :nosearch:

From Mattermost v10.4, Mattermost Enterprise customers with self-hosted deployments can configure `Redis <https://redis.io/>`_ (Remote Dictionary Server) as an alternative cache backend. Redis is an open-source, in-memory data structure store that can be used as a database, cache, and message broker. It supports various data structures and is a top choice for its performance because its able to store data in memory and provide very quick data access.

Using Redis as a caching solution can help ensure that Mattermost for enterprise-level deployments with high concurrency and large user bases remains performant and efficient, even under heavy usage.

Configure a Redis cache by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: redis-cache-type
  :displayname: Define cache type (CacheSettings)
  :systemconsole: N/A
  :configjson: CacheType
  :environment: MM_CACHESETTINGS_CACHETYPE

  - **lru**: **(Default)** Mattermost uses the in-memory cache store.
  - **redis**: Mattermost uses the configured Redis cache store.

Cache type
^^^^^^^^^^

+-----------------------------------------------+---------------------------------------------------------------------------+
| Define the cache type.                        | - System Config path: **N/A**                                             |
|                                               | - ``config.json`` setting: ``CacheSettings`` > ``CacheType,`` > ``lru``   |
| - **lru**: **(Default)** Mattermost uses the  | - Environment variable: ``MM_CACHESETTINGS_CACHETYPE``                    |
|   in-memory cache store.                      |                                                                           |
| - **redis**: Mattermost uses the configured   |                                                                           |
|   Redis cache store.                          |                                                                           |
+-----------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: redis-cache-address
  :displayname: Hostname of the Redis host (CacheSettings)
  :systemconsole: N/A
  :configjson: RedisAddress
  :environment: MM_CACHESETTINGS_REDISADDRESS
  :description: Specify the hostname of the Redis host.

Redis address
^^^^^^^^^^^^^^

+-----------------------------------------------+---------------------------------------------------------------------------+
| The hostname of the Redis host.               | - System Config path: **N/A**                                             |
|                                               | - ``config.json`` setting: ``CacheSettings`` > ``RedisAddress,``          |
| String input.                                 | - Environment variable: ``MM_CACHESETTINGS_REDISADDRESS``                 |
+-----------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: redis-cache-password
  :displayname: Password of the Redis host (CacheSettings)
  :systemconsole: N/A
  :configjson: RedisPassword
  :environment: MM_CACHESETTINGS_REDISPASSWORD
  :description: Specify the password of the Redis host.

Redis password
^^^^^^^^^^^^^^

+-----------------------------------------------+---------------------------------------------------------------------------+
| The password of the Redis host.               | - System Config path: **N/A**                                             |
|                                               | - ``config.json`` setting: ``CacheSettings`` > ``RedisPassword,``         |
| String input. Leave blank if there is no      | - Environment variable: ``MM_CACHESETTINGS_REDISPASSWORD``                |
| password.                                     |                                                                           |
+-----------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: redis-cache-database
  :displayname: Database of the Redis host (CacheSettings)
  :systemconsole: N/A
  :configjson: RedisDB
  :environment: MM_CACHESETTINGS_REDISDB
  :description: Specify the databse of the Redis host. Zero-indexed number up to 15. Typically set to 0. Redis allows a maximum of 16 databases.

Redis database
^^^^^^^^^^^^^^

+-----------------------------------------------+---------------------------------------------------------------------------+
| The database of the Redis host.               | - System Config path: **N/A**                                             |
|                                               | - ``config.json`` setting: ``CacheSettings`` > ``RedisDB,``               |
| Zero-indexed number up to 15. Typically set   | - Environment variable: ``MM_CACHESETTINGS_REDISDB``                      |
| to ``0``. Redis allows a maximum of 16        |                                                                           |
| databases.                                    |                                                                           |
+-----------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: redis-cache-type
  :displayname: Define the cache type (CacheSettings)
  :systemconsole: N/A
  :configjson: CacheType
  :environment: MM_CACHESETTINGS_CACHETYPE

  - **true**: Client-side cache of Redis is disabled. Typically used as a test option, and not in production environments.
  - **false**: **(Default)** Client-side cache of Redis is enabled.

Disable client cache
^^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+--------------------------------------------------------------------------------------+
| Disables the client-side cache of Redis.      | - System Config path: **N/A**                                                        |
|                                               | - ``config.json`` setting: ``CacheSettings`` > ``DisableClientCache,`` > ``false``   |
| - **true**: Client-side cache of Redis is     | - Environment variable: ``MM_CACHESETTINGS_REDISDB``                                 |
|   disabled. Typically used as a test option,  |                                                                                      |
|   and not in production environments.         |                                                                                      |
| - **false**: **(Default)** Client-side cache  |                                                                                      |
|   of Redis is enabled.                        |                                                                                      |
+-----------------------------------------------+--------------------------------------------------------------------------------------+

.. config:setting:: redis-cache-prefix
  :displayname: Redis cache prefix (CacheSettings)
  :systemconsole: N/A
  :configjson: CacheSettings.RedisCachePrefix
  :environment: MM_CACHESETTINGS_REDISCACHEPREFIX
  :description: Adds a prefix to all Redis cache keys. Blank by default.

Redis cache prefix
^^^^^^^^^^^^^^^^^^

+-----------------------------------------------+--------------------------------------------------------------------------------------+
| Adds a prefix to all Redis cache keys.        | - System Config path: **N/A**                                                        |
|                                               | - ``config.json`` setting: ``CacheSettings`` > ``RedisCachePrefix``                  |
|                                               | - Environment variable: ``MM_CACHESETTINGS_REDISCACHEPREFIX``                        |
+-----------------------------------------------+--------------------------------------------------------------------------------------+

.. tip::

  Adding a prefix to all Redis cache keys reduces key collisions, simplifies debugging, isolates data, and provides a clear structure for managing and scaling Redis-based systems. In environments where multiple systems or tenants use the same Redis instance, prefixes become critical for maintaining data integrity and operational efficiency.

.. config:setting:: enable-webhub-channel-iteration
  :displayname: Enable webhub channel iteration
  :systemconsole: N/A
  :configjson: ServiceSettings.EnableWebHubChannelIteration
  :environment: MM_SERVICESETTINGS_ENABLEWEBHUBCHANNELITERATION

    - **true**: Improves websocket broadcasting performance; however, performance may decrease when users join or leave a channel. Not recommended unless you have at least 200,000 concurrent users actively using Mattermost.
    - **false**: **(Default)** Websocket broadcasting performance in channels is disabled.

Enable webhub channel iteration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| Control the performance of websocket broadcasting in | - System Config path: **N/A**                                                                    |
| channels.                                            | - ``config.json`` setting: ``ServiceSettings`` > ``EnableWebHubChannelIteration,`` > ``false``   |
|                                                      | - Environment variable: ``MM_SERVICESETTINGS_ENABLEWEBHUBCHANNELITERATION``                      |
| When enabled, improves websocket broadcasting        |                                                                                                  |
| performance; however, performance may decrease       |                                                                                                  |
| when users join or leave a channel.                  |                                                                                                  |
|                                                      |                                                                                                  |
| Not recommended unless you have at least 200,000     |                                                                                                  |
| concurrent users actively using Mattermost.          |                                                                                                  |
|                                                      |                                                                                                  |
| Disabled by default.                                 |                                                                                                  |
+------------------------------------------------------+--------------------------------------------------------------------------------------------------+

.. config:setting:: enable-dedicated-export-filestore-target
  :displayname: Enable dedicated export filestore target
  :systemconsole: N/A
  :configjson: EnableWebHubChannelIteration
  :environment: MM_FILESETTINGS_DEDICATEDEXPORTSTORE

    - **true**: A new ``ExportFileBackend()`` is generated under ``FileSettings`` using new configuration values for select configuration settings.
    - **false**: **(Default)** Standard file storage is used. Standard file storage will also be used when the configuration setting or value is omitted.

Enable dedicated export filestore target
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------------------------+-------------------------------------------------------------------------+
| Enables the ability to specify an alternate filestore                                | - System Config path: **N/A**                                           |
| target for Mattermost                                                                | - ``config.json`` setting: ``FileSettings`` > ``DedicatedExportStore``  |
| :doc:`bulk exports </administration-guide/manage/bulk-export-tool>` and              | - Environment variable: ``MM_FILESETTINGS_DEDICATEDEXPORTSTORE``        |
| :doc:`compliance exports </administration-guide/comply/compliance-export>`.          |                                                                         |
|                                                                                      |                                                                         |
| - **True**: A new ``ExportFileBackend()`` is generated                               |                                                                         |
|   under ``FileSettings`` using new configuration values                              |                                                                         |
|   for the following configuration settings:                                          |                                                                         |
|                                                                                      |                                                                         |
|  - ``ExportDriverName``                                                              |                                                                         |
|  - ``ExportDirectory``                                                               |                                                                         |
|  - ``ExportAmazonS3AccessKeyId``                                                     |                                                                         |
|  - ``ExportAmazonS3SecretAccessKey``                                                 |                                                                         |
|  - ``ExportAmazonS3Bucket``                                                          |                                                                         |
|  - ``ExportAmazonS3PathPrefix``                                                      |                                                                         |
|  - ``ExportAmazonS3Region``                                                          |                                                                         |
|  - ``ExportAmazonS3Endpoint``                                                        |                                                                         |
|  - ``ExportAmazonS3SSL``                                                             |                                                                         |
|  - ``ExportAmazonS3SignV2``                                                          |                                                                         |
|  - ``ExportAmazonS3SSE``                                                             |                                                                         |
|  - ``ExportAmazonS3Trace``                                                           |                                                                         |
|  - ``ExportAmazonS3RequestTimeoutMilliseconds``                                      |                                                                         |
|  - ``ExportAmazonS3PresignExpiresSeconds``                                           |                                                                         |
|                                                                                      |                                                                         |
| - **False**: (**Default**) Standard                                                  |                                                                         |
|   :ref:`file storage                                                                 |                                                                         |
|   <administration-guide/configure/environment-configuration-settings:file storage>`  |                                                                         |
|   is used. Standard file storage will also be used when the configuration setting    |                                                                         |
|   or value is omitted.                                                               |                                                                         |
+--------------------------------------------------------------------------------------+-------------------------------------------------------------------------+

.. note::

  - When an alternate filestore target is configured, Mattermost Cloud admins can generate an S3 presigned URL for exports using the ``/exportlink [job-id|zip file|latest]`` slash command. See the :ref:`Mattermost data migration <administration-guide/manage/cloud-data-export:create the export>` documentation for details. Alternatively, Cloud and self-hosted admins can use the :ref:`mmctl export generate-presigned-url <administration-guide/manage/mmctl-command-line-tool:mmctl export generate-presigned-url>` command to generate a presigned URL directly from mmctl.
  - Generating an S3 presigned URL requires the feature flag ``EnableExportDirectDownload`` to be set to ``true``,  the storage must be compatible with generating an S3 link, and this experimental configuration setting must be set to ``true``. Presigned URLs for exports aren't supported for systems with shared storage.
