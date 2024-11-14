Environment configuration settings
==================================

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. tip:: 

  Each configuration value below includes a JSON path to access the value programmatically in the ``config.json`` file using a JSON-aware tool. For example, the ``SiteURL`` value is under ``ServiceSettings``.

  - If using a tool such as `jq <https://stedolan.github.io/jq/>`__, you'd enter: ``cat config/config.json | jq '.ServiceSettings.SiteURL'``
  - When working with the ``config.json`` file manually, look for the key ``ServiceSettings``, then within that object, find the key ``SiteURL``.

Both self-hosted and Cloud admins can access the following configuration settings in **System Console > Environment**. Self-hosted admins can also edit the ``config.json`` file as described in the following tables. 

Web server
----------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Configure the network environment in which Mattermost is deployed by going to **System Console > Environment > Web Server**, or by updating the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: web-siteurl
  :displayname: Site URL (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.SiteURL
  :environment: MM_SERVICESETTINGS_SITEURL
  :description: The URL that users use to access Mattermost. The port number is required if it’s not a standard port, such as 80 or 443.

Site URL
~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+---------------------------------------------------------------+
| The URL that users use to access Mattermost.                  | - System Config path: **Environment > Web Server**            |
| The port number is required if it’s not a standard port,      | - ``config.json`` setting: ``.ServiceSettings.SiteURL",``     |
| such as 80 or 443. This field is required.                    | - Environment variable: ``MM_SERVICESETTINGS_SITEURL``        |
|                                                               |                                                               |
| Select the **Test Live URL** button in the System Console     |                                                               |
| to validate the Site URL.                                     |                                                               |
+---------------------------------------------------------------+---------------------------------------------------------------+
| **Notes**:                                                                                                                    |
|                                                                                                                               |
| - The URL may contain a subpath, such as ``https://example.com/company/mattermost``.                                          |
| - If you change the Site URL value, log out of the Desktop App, and sign back in using the new domain.                        |
| - If Site URL is not set:                                                                                                     |
|                                                                                                                               |
|   - Email notifications will contain broken links, and email batching will not work.                                          |
|   - Authentication via OAuth 2.0, including GitLab, Google, and Entra ID, will fail.                                          |
|   - Plugins may not work as expected.                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------+

.. config:setting:: max-url-length
  :displayname: Maximum URL length (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.MaximumURLLength
  :environment: MM_SERVICESETTINGS_MAXIMUMURLLENGTH
  :description: The longest URL, in characters, including query parameters, accepted by the Mattermost server. Default is 2048 characters.

Maximum URL length
~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The longest URL, in characters, including query parameters,   | - System Config path: N/A                                                |
| accepted by the Mattermost server. Longer URLs are rejected,  | - ``config.json`` setting: ``.ServiceSettings.MaximumURLLength: 2048",`` |
| and API calls fail with an error.                             | - Environment variable: ``MM_SERVICESETTINGS_MAXIMUMURLLENGTH``          |
|                                                               |                                                                          |
| Numeric value. Default is **2048** characters.                |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: web-listenaddress
  :displayname: Web server listen address (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.ListenAddress
  :environment: MM_SERVICESETTINGS_LISTENADDRESS

  The address and port to which to bind and listen. Specifying ``:8065`` will bind to all network interfaces.
  Specifying ``127.0.0.1:8065`` will only bind to the network interface having that IP address.

Web server listen address
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+------------------------------------------------------------------+
| The address and port to which to bind and listen.             | - System Config path: **Environment > Web Server**               |
| Specifying ``:8065`` will bind to all network interfaces.     | - ``config.json`` setting: ``".ServiceSettings.ListenAddress",`` |
| Specifying ``127.0.0.1:8065`` will only bind to the network   | - Environment variable: ``MM_SERVICESETTINGS_LISTENADDRESS``     |
| interface having that IP address.                             |                                                                  |
|                                                               |                                                                  |
| If you choose a port of a lower level (called “system ports”  |                                                                  |
| or “well-known ports”, in the range of 0-1023), you must have |                                                                  |
| permissions to bind to that port.                             |                                                                  |
+---------------------------------------------------------------+------------------------------------------------------------------+

.. config:setting:: web-forwardinsecure
  :displayname: Forward port 80 to 443 (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.Forward80To443
  :environment: MM_SERVICESETTINGS_FORWARD80TO443

  - **true**: Forwards all insecure traffic from port 80 to secure port 443.
  - **false**: **(Default)** When using a proxy such as NGINX in front of Mattermost this setting is unnecessary and should be set to false.

Forward port 80 to 443
~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Forward insecure traffic from port 80 to port 443.            | - System Config path: **Environment > Web Server**                       |
|                                                               | - ``config.json`` setting: ``".ServiceSettings.Forward80To443: false",`` |
| - **true**: Forwards all insecure traffic from port 80 to     | - Environment variable: ``MM_SERVICESETTINGS_FORWARD80TO443``            |
|   secure port 443.                                            |                                                                          |
| - **false**: **(Default)** When using a proxy such as NGINX   |                                                                          |
|   in front of Mattermost this setting is unnecessary          |                                                                          |
|   and should be set to false.                                 |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: web-connectionsecurity
  :displayname: Web server connection security (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.ConnectionSecurity
  :environment: MM_SERVICESETTINGS_CONNECTIONSECURITY
  :description: Connection security between Mattermost clients and the server.

  - **Not specified**: Mattermost will connect over an unsecure connection.
  - **TLS**: Encrypts the communication between Mattermost clients and your server.

Web server connection security
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| Connection security between Mattermost clients and the server.        | - System Config path: **Environment > Web Server**                    |
|                                                                       | - ``config.json`` setting: ``".ServiceSettings.ConnectionSecurity",`` |
| - **Not specified**: Mattermost will connect over an unsecure         | - Environment variable: ``MM_SERVICESETTINGS_CONNECTIONSECURITY``     |
|   connection.                                                         |                                                                       |
| - **TLS**: Encrypts the communication between Mattermost              |                                                                       |
|   clients and your server. See the :doc:`configuring TLS on           |                                                                       |
|   Mattermost </install/config-tls-mattermost>` for more details.      |                                                                       |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------+

.. config:setting:: web-tlscertificatefile
  :displayname: TLS certificate file (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.TLSCertFile
  :environment: MM_SERVICESETTINGS_TLSCERTFILE
  :description: The path to the certificate file to use for TLS connection security.

TLS certificate file
~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+------------------------------------------------------------------+
| The path to the certificate file to use for TLS        | - System Config path: **Environment > Web Server**               |
| connection security.                                   | - ``config.json`` setting: ``".ServiceSettings.TLSCertFile",``   |
|                                                        | - Environment variable: ``MM_SERVICESETTINGS_TLSCERTFILE``       |
| String input.                                          |                                                                  |
+--------------------------------------------------------+------------------------------------------------------------------+

.. config:setting:: web-tlskeyfile
  :displayname: TLS key file (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.TLSKeyFile
  :environment: MM_SERVICESETTINGS_TLSKEYFILE
  :description: The path to the TLS key file to use for TLS connection security.

TLS key file
~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+---------------------------------------------------------------+
| The path to the TLS key file to use for TLS            | - System Config path: **Environment > Web Server**            |
| connection security.                                   | - ``config.json`` setting: ``".ServiceSettings.TLSKeyFile",`` |
|                                                        | - Environment variable: ``MM_SERVICESETTINGS_TLSKEYFILE``     |
| String input.                                          |                                                               |
+--------------------------------------------------------+---------------------------------------------------------------+

.. config:setting:: web-useletsencrypt
  :displayname: Use Let's Encrypt (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.UseLetsEncrypt
  :environment: MM_SERVICESETTINGS_USELETSENCRYPT
  :description: Enable the automatic retrieval of certificates from Let’s Encrypt.

  - **true**: The certificate will be retrieved when a client attempts to connect from a new domain. This will work with multiple domains.
  - **false**: **(Default)** Manual certificate specification based on the TLS Certificate File and TLS Key File specified above.

Use Let's Encrypt
~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| Enable the automatic retrieval of certificates from Let’s Encrypt.                            | - System Config path: **Environment > Web Server**                       |
| See the :doc:`configuring TLS on Mattermost documentation </install/config-tls-mattermost>`   | - ``config.json`` setting: ``".ServiceSettings.UseLetsEncrypt: false",`` |
| for more details on setting up Let’s Encrypt.                                                 | - Environment variable: ``MM_SERVICESETTINGS_USELETSENCRYPT``            |
|                                                                                               |                                                                          |
| - **true**: The certificate will be retrieved when a client                                   |                                                                          |
|   attempts to connect from a new domain. This will work with                                  |                                                                          |
|   multiple domains.                                                                           |                                                                          |
| - **false**: **(Default)** Manual certificate specification                                   |                                                                          |
|   based on the TLS Certificate File and TLS Key File specified                                |                                                                          |
|   above.                                                                                      |                                                                          |
+-----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: web-letsencryptcache
  :displayname: Let's Encrypt certificate cache file (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.LetsEncryptCertificateCacheFile
  :environment: MM_SERVICESETTINGS_LETSENCRYPTCERTIFICATECACHEFILE
  :description: The path to the file where certificates and other data about the Let’s Encrypt service will be stored.

Let's Encrypt certificate cache file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+------------------------------------------------------------------------------------+
| The path to the file where certificates and other data | - System Config path: **Environment > Web Server**                                 |
| about the Let’s Encrypt service will be stored.        | - ``config.json`` setting: ``".ServiceSettings.LetsEncryptCertificateCacheFile",`` |
|                                                        | - Environment variable: ``MM_SERVICESETTINGS_LETSENCRYPTCERTIFICATECACHEFILE``     |
| File path input.                                       |                                                                                    |
+--------------------------------------------------------+------------------------------------------------------------------------------------+

.. config:setting:: web-readtimeout
  :displayname: Read timeout (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.ReadTimeout
  :environment: MM_SERVICESETTINGS_READTIMEOUT
  :description: Maximum time allowed from when the connection is accepted to when the request body is fully read. Default is **300** seconds.

Read timeout
~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------+---------------------------------------------------------------------+
| Maximum time allowed from when the connection is        | - System Config path: **Environment > Web Server**                  |
| accepted to when the request body is fully read.        | - ``config.json`` setting: ``".ServiceSettings.ReadTimeout: 300",`` |
|                                                         | - Environment variable: ``MM_SERVICESETTINGS_READTIMEOUT``          |
| Numerical input in seconds. Default is **300** seconds. |                                                                     |
+---------------------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: web-writetimeout
  :displayname: Write timeout (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.WriteTimeout
  :environment: MM_SERVICESETTINGS_WRITETIMEOUT

  If using HTTP (insecure), this is the maximum time, in seconds, allowed from the end of reading the request headers until the response is written.
  If using HTTPS, it's the total time, in seconds, from when the connection is accepted until the response is written.
  Default is 300 seconds.

Write timeout
~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------+-----------------------------------------------------------------------------+
| - If using HTTP (insecure), this is the maximum time     | - System Config path: **Environment > Web Server**                          |
|   allowed from the end of reading the request headers    | - ``config.json`` setting: ``".ServiceSettings.WriteTimeout: 300",``        |
|   until the response is written.                         | - Environment variable: ``MM_SERVICESETTINGS_WRITETIMEOUT``                 |
| - If using HTTPS, it's the total time from when the      |                                                                             |
|   connection is accepted until the response is written.  |                                                                             |
|                                                          |                                                                             |
| Numerical input in seconds. Default is **300** seconds.  |                                                                             |
+----------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: web-idletimeout
  :displayname: Idle timeout (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.IdleTimeout
  :environment: MM_SERVICESETTINGS_IDLETIMEOUT
  :description: This is the maximum time, in seconds, allowed before an idle connection is disconnected. Default is **300** seconds.

Idle timeout
~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------+---------------------------------------------------------------------+
| Set an explicit idle timeout in the HTTP server.        | - System Config path: **Environment > Web Server**                  |
| This is the maximum time allowed before an idle         | - ``config.json`` setting: ``".ServiceSettings.IdleTimeout: 300",`` |
| connection is disconnected.                             | - Environment variable: ``MM_SERVICESETTINGS_IDLETIMEOUT``          |
|                                                         |                                                                     |
| Numerical input in seconds. Default is **300** seconds. |                                                                     |
+---------------------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: web-webservermode
  :displayname: Webserver mode (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.WebserverMode
  :environment: MM_SERVICESETTINGS_WEBSERVERMODE

  - **gzip**: **(Default)** The Mattermost server will serve static files compressed with gzip to improve performance.
  - **Uncompressed**: The Mattermost server will serve static files uncompressed.
  - **Disabled**: The Mattermost server will not serve static files.

Webserver mode
~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------------+------------------------------------------------------------------------+
| We recommend gzip to improve performance unless your                | - System Config path: **Environment > Web Server**                     |
| environment has specific restrictions, such as a web proxy that     | - ``config.json`` setting: ``".ServiceSettings.WebserverMode: gzip",`` |
| distributes gzip files poorly.                                      | - Environment variable: ``MM_SERVICESETTINGS_WEBSERVERMODE``           |
|                                                                     |                                                                        |
| - **gzip**: **(Default)** The Mattermost server will serve static   |                                                                        |
|   files compressed with gzip to improve performance.                |                                                                        |
|   gzip compression applies to the HTML, CSS, Javascript, and other  |                                                                        |
|   static content files that make up the Mattermost web client.      |                                                                        |
| - **Uncompressed**: The Mattermost server will serve static         |                                                                        |
|   files uncompressed.                                               |                                                                        |
| - **Disabled**: The Mattermost server will not serve static files.  |                                                                        |
+---------------------------------------------------------------------+------------------------------------------------------------------------+

.. config:setting:: web-insecureoutgoingconnections
  :displayname: Enable insecure outgoing connections (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.EnableInsecureOutgoingConnections
  :environment: MM_SERVICESETTINGS_ENABLEINSECUREOUTGOINGCONNECTIONS

  - **true**: Outgoing HTTPS requests, including S3 clients, can accept unverified, self-signed certificates.
  - **false**: **(Default)** Only secure HTTPS requests are allowed.

Enable insecure outgoing connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| Configure Mattermost to allow insecure outgoing connections.  | - System Config path: **Environment > Web Server**                                          |
|                                                               | - ``config.json`` setting: ``".ServiceSettings.EnableInsecureOutgoingConnections: false",`` |
| - **true**: Outgoing HTTPS requests, including S3 clients,    | - Environment variable: ``MM_SERVICESETTINGS_ENABLEINSECUREOUTGOINGCONNECTIONS``            |
|   can accept unverified, self-signed certificates.            |                                                                                             |
|   For example, outgoing webhooks to a server with a           |                                                                                             |
|   self-signed TLS certificate, using any domain, will be      |                                                                                             |
|   allowed, and will skip TLS verification.                    |                                                                                             |
| - **false**: **(Default)** Only secure HTTPS requests are     |                                                                                             |
|   allowed.                                                    |                                                                                             |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| **Security note**: Enabling this feature makes these connections susceptible to man-in-the-middle attacks.                                                  |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+

.. config:setting:: web-managedresourcepaths
  :displayname: Managed resource paths (Web Server)
  :systemconsole: Environment > Web Server
  :configjson: .ServiceSettings.ManagedResourcePaths
  :environment: MM_SERVICESETTINGS_MANAGEDRESOURCEPATHS
  :description: A comma-separated list of paths within the Mattermost domain that are managed by a third party service instead of Mattermost itself.

Managed resource paths
~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+-------------------------------------------------------------------------+
| A comma-separated list of paths within the Mattermost  | - System Config path: **Environment > Web Server**                      |
| domain that are managed by a third party service       | - ``config.json`` setting: ``".ServiceSettings.ManagedResourcePaths",`` |
| instead of Mattermost itself.                          | - Environment variable: ``MM_SERVICESETTINGS_MANAGEDRESOURCEPATHS``     |
|                                                        |                                                                         |
| Links to these paths will be opened in a new           |                                                                         |
| tab/window by Mattermost apps.                         |                                                                         |
|                                                        |                                                                         |
| For example, if Mattermost is running on               |                                                                         |
| ``https://mymattermost.com``, setting this to          |                                                                         |
| conference will cause links such as                    |                                                                         |
| ``https://mymattermost.com/conference`` to open in a   |                                                                         |
| new window.                                            |                                                                         |
+--------------------------------------------------------+-------------------------------------------------------------------------+
| **Note:**                                                                                                                        |
| When using the Mattermost Desktop App, additional configuration is required to open the link within the Desktop App instead of   |
| in a browser. See the :doc:`desktop managed resources </install/desktop-app-managed-resources>`                                  |
| documentation for details.                                                                                                       |
+--------------------------------------------------------+-------------------------------------------------------------------------+

Reload configuration from disk
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

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

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------+---------------------------------------------------------------+
| Purge all in-memory caches for sessions, accounts,       | - System Config path: **Environment > Web Server**            |
| and channels.                                            | - ``config.json`` setting: N/A                                |
|                                                          | - Environment variable: N/A                                   |
| Select the **Purge All Caches** button in the System     |                                                               |
| Console to purge all caches.                             |                                                               |
+----------------------------------------------------------+---------------------------------------------------------------+
| **Note**: Purging the caches may adversely impact performance.                                                           |
| :doc:`high availability cluster-based deployments </scale/high-availability-cluster-based-deployment>` will attempt      |
| to purge all the servers in the cluster                                                                                  |
+----------------------------------------------------------+---------------------------------------------------------------+

.. config:setting:: web-websocketurl
  :displayname: Websocket URL (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.WebsocketURL
  :environment: MM_SERVICESETTINGS_WEBSOCKETURL
  :description: You can configure the server to instruct clients on where they should try to connect websockets to.

Websocket URL
~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+---------------------------------------------------------------------+
| You can configure the server to instruct clients       | - System Config path: N/A                                           |
| on where they should try to connect websockets to.     | - ``config.json`` setting: ``".ServiceSettings.WebsocketURL: "",``  |
|                                                        | - Environment variable: ``MM_SERVICESETTINGS_WEBSOCKETURL``         |
| String input.                                          |                                                                     |
+--------------------------------------------------------+---------------------------------------------------------------------+
| **Note**: We strongly recommend configuring a single websocket URL that matches the `Site URL <#site-url>`_ configuration    |
| setting.                                                                                                                     |
+--------------------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: web-licensefilelocation
  :displayname: License file location (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.LicenseFileLocation
  :environment: MM_SERVICESETTINGS_LICENSEFILELOCATION
  :description: The path and filename of the license file on disk.

License file location
~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+----------------------------------------------------------------------------+
| The path and filename of the license file on disk.     | - System Config path: N/A                                                  |
| On startup, if Mattermost can't find a valid license   | - ``config.json`` setting: ``".ServiceSettings.LicenseFileLocation: "",``  |
| in the database from a previous upload, it looks in    | - Environment variable: ``MM_SERVICESETTINGS_LICENSEFILELOCATION``         |
| this path for the license file.                        |                                                                            |
|                                                        |                                                                            |
| String input. Can be an absolute path or a path        |                                                                            |
| relative to the ``mattermost`` directory.              |                                                                            |
+--------------------------------------------------------+----------------------------------------------------------------------------+

.. config:setting:: web-tlsminimumversion
  :displayname: TLS minimum version (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.TLSMinVer
  :environment: MM_SERVICESETTINGS_TLSMINVER
  :description: The minimum TLS version used by the Mattermost server. Default value is **1.2**.

TLS minimum version
~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+---------------------------------------------------------------------+
| The minimum TLS version used by the Mattermost server. | - System Config path: N/A                                           |
|                                                        | - ``config.json`` setting: ``".ServiceSettings.TLSMinVer: 1.2",``   |
| String input. Default is **1.2**.                      | - Environment variable: ``MM_SERVICESETTINGS_TLSMINVER``            |
+--------------------------------------------------------+---------------------------------------------------------------------+
| **Note**: This setting only takes effect if you are using the built-in server binary directly, and not using a reverse proxy |
| layer, such as NGINX.                                                                                                        |
+--------------------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: web-trustedproxyipheader
  :displayname: Trusted proxy IP header (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.TrustedProxyIPHeader
  :environment: MM_SERVICESETTINGS_TRUSTEDPROXYIPHEADER
  :description: Specified headers that will be checked, one by one, for IP addresses (order is important). All other headers are ignored.

Trusted proxy IP header
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+------------------------------------------------------------------------------+
| Specified headers that will be checked, one by one,    | - System Config path: N/A                                                    |
| for IP addresses (order is important).                 | - ``config.json`` setting: ``".ServiceSettings.TrustedProxyIPHeader: []",``  |
| All other headers are ignored.                         | - Environment variable: ``MM_SERVICESETTINGS_TRUSTEDPROXYIPHEADER``          |
|                                                        |                                                                              |
| String array input consisting of header names,         |                                                                              |
| such as ``["X-Forwarded-For", "X-Real-Ip"]``.          |                                                                              |
+--------------------------------------------------------+------------------------------------------------------------------------------+
| **Notes**:                                                                                                                            |
|                                                                                                                                       |
| - The default value of ``[]`` means that no header will be trusted. Prior to v5.12, the absence of this configuration setting entry   |
|   will have it set to ``["X-Forwarded-For", "X-Real-Ip"]`` on upgrade to maintain backwards compatibility.                            |
| - We recommend keeping the default setting when Mattermost is running without a proxy to avoid the client sending the headers and     |
|   bypassing rate limiting and/or the audit log.                                                                                       |
| - For environments that use a reverse proxy, this issue does not exist, provided that the headers are set by the reverse proxy.       |
|   In those environments, only explicitly whitelist the header set by the reverse proxy and no additional values.                      |
|                                                                                                                                       |
|                                                                                                                                       |
+--------------------------------------------------------+------------------------------------------------------------------------------+

.. config:setting:: web-enablehsts
  :displayname: Enable Strict Transport Security (HSTS) (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.TLSStrictTransport
  :environment: MM_SERVICESETTINGS_TLSSTRICTTRANSPORT

  - **true**: Adds the Strict Transport Security (HSTS) header to all responses, forcing the browser to request all resources via HTTPS.
  - **false**: **(Default)** No restrictions on TLS transport. Strict Transport Security (HSTS) header isn't added to responses.

Enable Strict Transport Security (HSTS)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+-------------------------------------------------------------------------------+
| - **true**: Adds the Strict Transport Security (HSTS)  | - System Config path: N/A                                                     |
|   header to all responses, forcing the browser to      | - ``config.json`` setting: ``".ServiceSettings.TLSStrictTransport: false",``  |
|   request all resources via HTTPS.                     | - Environment variable: ``MM_SERVICESETTINGS_TLSSTRICTTRANSPORT``             |
| - **false**: **(Default)** No restrictions on TLS      |                                                                               |
|   transport. Strict Transport Security (HSTS) header   |                                                                               |
|   isn't added to responses.                            |                                                                               |
+--------------------------------------------------------+-------------------------------------------------------------------------------+
| See the `Strict-Transport-Security <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security>`__            |
| documentation for details.                                                                                                             |
+--------------------------------------------------------+-------------------------------------------------------------------------------+

.. config:setting:: web-securetlstransportexpiry
  :displayname: Secure TLS transport expiry (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.TLSStrictTransportMaxAge
  :environment: MM_SERVICESETTINGS_TLSSTRICTTRANSPORTMAXAGE
  :description: The time, in seconds, that the browser remembers a site is only to be accessed using HTTPS. Default is **63072000** seconds (2 years).

Secure TLS transport expiry
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+----------------------------------------------------------------------------------------+
| The time, in seconds, that the browser remembers a     | - System Config path: N/A                                                              |
| site is only to be accessed using HTTPS. After this    | - ``config.json`` setting: ``".ServiceSettings.TLSStrictTransportMaxAge: 63072000",``  |
| period, a site can't be accessed using HTTP unless     | - Environment variable: ``MM_SERVICESETTINGS_TLSSTRICTTRANSPORTMAXAGE``                |
| ``TLSStrictTransport`` is set to ``true``.             |                                                                                        |
|                                                        |                                                                                        |
| Numerical input. Default is **63072000** (2 years).    |                                                                                        |
+--------------------------------------------------------+----------------------------------------------------------------------------------------+
| See the `Strict-Transport-Security <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security>`__                     |
| documentation for details.                                                                                                                      |
+--------------------------------------------------------+----------------------------------------------------------------------------------------+

.. config:setting:: web-tlscipheroverwrites
  :displayname: TLS cipher overwrites (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.TLSOverwriteCiphers
  :environment: MM_SERVICESETTINGS_TLSOVERWRITECIPHERS
  :description: Set TLS ciphers overwrites to meet requirements from legacy clients which don't support modern ciphers, or to limit the types of accepted ciphers.

TLS cipher overwrites
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+-----------------------------------------------------------------------------+
| Set TLS ciphers overwrites to meet requirements from   | - System Config path: N/A                                                   |
| legacy clients which don't support modern ciphers,     | - ``config.json`` setting: ``".ServiceSettings.TLSOverwriteCiphers: []",``  |
| or to limit the types of accepted ciphers.             | - Environment variable: ``MM_SERVICESETTINGS_TLSOVERWRITECIPHERS``          |
|                                                        |                                                                             |
| If none specified, the Mattermost server assumes a     |                                                                             |
| set of currently considered secure ciphers, and allows |                                                                             |
| overwrites in the edge case.                           |                                                                             |
|                                                        |                                                                             |
| String array input.                                    |                                                                             |
+--------------------------------------------------------+-----------------------------------------------------------------------------+
| **Notes**:                                                                                                                           |
|                                                                                                                                      |
| - This setting only takes effect if you are using the built-in server binary directly, and not using a reverse proxy layer, such     |
|   as NGINX.                                                                                                                          |
| - See the ``ServerTLSSupportedCiphers`` variable in `/model/config.go                                                                |
|   <https://github.com/mattermost/mattermost/blob/master/server/public/model/config.go>`__ for a list of ciphers considered secure.   |
+--------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: web-goroutinehealththreshold
  :displayname: Goroutine health threshold (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.GoroutineHealthThreshold
  :environment: MM_SERVICESETTINGS_GOROUTINEHEALTHTHRESHOLD
  :description: Set a threshold on the number of goroutines when the Mattermost system is considered to be in a healthy state. Default is **-1** which turns off checking for the threshold.

Goroutine health threshold
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+----------------------------------------------------------------------------------+
| Set a threshold on the number of goroutines when the   | - System Config path: N/A                                                        |
| Mattermost system is considered to be in a healthy     | - ``config.json`` setting: ``".ServiceSettings.GoroutineHealthThreshold: -1",``  |
| state.                                                 | - Environment variable: ``MM_SERVICESETTINGS_GOROUTINEHEALTHTHRESHOLD``          |
|                                                        |                                                                                  |
| When goroutines exceed this limit, a warning is        |                                                                                  |
| returned in the server logs.                           |                                                                                  |
|                                                        |                                                                                  |
| Numeric input. Default is **-1** which turns off       |                                                                                  |
| checking for the threshold.                            |                                                                                  |
+--------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: web-allowcookiesforsubdomains
  :displayname: Allow cookies for subdomains (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.AllowCookiesForSubdomains
  :environment: MM_SERVICESETTINGS_ALLOWCOOKIESFORSUBDOMAINS

  - **true**: **(Default)** Allows cookies for subdomains by setting the domain parameter on Mattermost cookies.
  - **false**: Cookies not allowed for subdomains.

Allow cookies for subdomains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+-------------------------------------------------------------------------------------+
| - **true**: **(Default)** Allows cookies for           | - System Config path: N/A                                                           |
|   subdomains by setting the domain parameter on        | - ``config.json`` setting: ``".ServiceSettings.AllowCookiesForSubdomains: true",``  |
|   Mattermost cookies.                                  | - Environment variable: ``MM_SERVICESETTINGS_ALLOWCOOKIESFORSUBDOMAINS``            |
| - **false**: Cookies not allowed for subdomains.       |                                                                                     |
+--------------------------------------------------------+-------------------------------------------------------------------------------------+

.. config:setting:: web-clusterlogtimeout
  :displayname: Cluster log timeout (Web Server)
  :systemconsole: N/A
  :configjson: .ServiceSettings.ClusterLogTimeoutMilliseconds
  :environment: MM_SERVICESETTINGS_CLUSTERLOGTIMEOUTMILLISECONDS
  :description: Define the frequency, in milliseconds, of cluster request time logging for performance monitoring. Default is **2000** milliseconds (2 seconds).

Cluster log timeout
~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+--------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Define the frequency, in milliseconds, of cluster      | - System Config path: N/A                                                               |
| request time logging for performance monitoring.       | - ``config.json`` setting: ``".ServiceSettings.ClusterLogTimeoutMilliseconds: 2000",``  |
|                                                        | - Environment variable: ``MM_SERVICESETTINGS_CLUSTERLOGTIMEOUTMILLISECONDS``            |
|                                                        |                                                                                         |
| Numerical input. Default is **2000** milliseconds      |                                                                                         |
| (2 seconds).                                           |                                                                                         |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------+
| See the :doc:`performance monitoring </scale/deploy-prometheus-grafana-for-performance-monitoring>` documentation for details.                   |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. config:setting:: service-maxpayloadsize
  :displayname: Maximum payload size (File Storage)
  :systemconsole: N/A
  :configjson: .ServiceSettings.MaximumPayloadSizeBytes
  :environment: MM_SERVICESETTINGS_MAXIMUMPAYLOADSIZEBYTES
  :description: The maximum payload size in bytes for all APIs except APIs that receive a file as an input. For example, the upload attachment API or the API to upload a custom emoji. Default is 300000.

Maximum payload size
~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------+-------------------------------------------------------------------------------------+
| The maximum payload size in bytes for all APIs except     | - System Config path: N/A                                                           |
| APIs that receive a file as an input.                     | - ``config.json`` setting: ``".ServiceSettings.MaximumPayloadSizeBytes: 300000",``  |
|                                                           | - Environment variable: ``MM_SERVICESETTINGS_MAXIMUMPAYLOADSIZEBYTES``              |
| For example, the upload attachment API or the API to      |                                                                                     |
| upload a custom emoji.                                    |                                                                                     |
|                                                           |                                                                                     |
| Numerical value. Default is **300000** (300 kB).          |                                                                                     |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------+

----

Database
--------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Configure the database environment in which Mattermost is deployed by going to **System Console > Environment > Database**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. include:: ../_static/badges/academy-mattermost-database.rst
  :start-after: :nosearch:

.. config:setting:: database-drivername
  :displayname: Driver name (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.DriverName
  :environment: MM_SQLSETTINGS_DRIVERNAME
  :description: The type of database. Either **postgres** or **mysql**. The default value is **mysql**.

Driver name
~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The type of database. Can be either:                          | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``".SqlSettings.DriverName",``                |
| - **mysql**: **(Default)** Enables driver to MySQL database.  | - Environment variable: ``MM_SQLSETTINGS_DRIVERNAME``                    |
| - **postgres**: Enables driver to PostgreSQL database.        |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: database-datasource
  :displayname: Data source (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.DataSource
  :environment: MM_SQLSETTINGS_DATASOURCE
  :description: The connection string to the master database.

Data source
~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The connection string to the master database.                 | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``".SqlSettings.DataSource",``                |
| String input.                                                 | - Environment variable: ``MM_SQLSETTINGS_DATASOURCE``                    |
|                                                               |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **PostgreSQL databases**                                                                                                                 |
|                                                                                                                                          |
| When **Driver Name** is set to ``postgres``, use a connection string in the form of:                                                     |
| ``postgres://mmuser:password@hostname_or_IP:5432/mattermost_test?sslmode=disable&connect_timeout=10``                                    |
|                                                                                                                                          |
| **To use TLS with PostgreSQL databases**                                                                                                 |
|                                                                                                                                          |
| The parameter to encrypt connection against a PostgreSQL server is ``sslmode``. The library used to interact with PostgreSQL server is   |
| `pq <https://pkg.go.dev/github.com/lib/pq>`__. Currently, it's not possible to use all the values that you could pass to a standard      |
| PostgreSQL Client ``psql "sslmode=value"`` See the `SSL Mode Descriptions <https://www.postgresql.org/docs/current/libpq-ssl.html>`__    |
| documentation for details.                                                                                                               |
|                                                                                                                                          |
| Your database admin must configure the functionality according to the supported values described below:                                  |
|                                                                                                                                          |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
| | Short description of the ``sslmode``   | Value           | Example of a data source name                                             | |
| | parameter                              |                 |                                                                           | |
| +========================================+=================+===========================================================================+ |
| | Don't use TLS / SSL encryption against | ``disable``     | ``postgres://mmuser:password@hostname_or_IP:5432/mattermost_test          | |
| | the PostgreSQL server.                 |                 | ?sslmode=disable&connect_timeout=10``                                     | |
| |                                        |                 |                                                                           | |
| | Default value in file ``config.json``  |                 |                                                                           | |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
| | The data is encrypted and the network  | ``require``     | ``postgres://mmuser:password@hostname_or_IP:5432/mattermost_test          | |
| | is trusted.                            |                 | ?sslmode=require&connect_timeout=10``                                     | |
| |                                        |                 |                                                                           | |
| | Default value is ``sslmode`` when      |                 |                                                                           | |
| | omitted.                               |                 |                                                                           | |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
| | The data is encrypted when connecting  | ``verify-ca``   | ``postgres://mmuser:password@hostname_or_IP:5432/mattermost_test          | |
| | to a trusted server.                   |                 | ?sslmode=verify-ca&connect_timeout=10``                                   | |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
| | The data is encrypted when connecting  | ``verify-full`` | ``postgres://mmuser:password@hostname_or_IP:5432/mattermost_test          | |
| | to a trusted server.                   |                 | ?sslmode=verify-full&connect_timeout=10``                                 | |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
|                                                                                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **MySQL databases**                                                                                                                      |
|                                                                                                                                          |
| When **Driver Name** is set to ``mysql``, we recommend using ``collation`` over using ``charset``.                                       |
|                                                                                                                                          |
| To specify collation:                                                                                                                    |
|                                                                                                                                          |
| .. code-block:: text                                                                                                                     |
|                                                                                                                                          |
|   "SqlSettings": {                                                                                                                       |
|       "DataSource":                                                                                                                      |
|   "<mmuser:password>@tcp(hostname or IP:3306)/mattermost?charset=utf8mb4,utf8&collation=utf8mb4_general_ci",                             |
|       [...]                                                                                                                              |
|    }                                                                                                                                     |
|                                                                                                                                          |
| If collation is omitted, the default collation, ``utf8mb4_general_ci`` is used:                                                          |
|                                                                                                                                          |
| .. code-block:: text                                                                                                                     |
|                                                                                                                                          |
|   "SqlSettings": {                                                                                                                       |
|       "DataSource": "<mmuser:password>@tcp(hostname or IP:3306)/mattermost?charset=utf8mb4,utf8",                                        |
|       [...]                                                                                                                              |
|    }                                                                                                                                     |
|                                                                                                                                          |
| **Note**: If you’re using MySQL 8.0 or later, the default collation has changed to ``utf8mb4_0900_ai_ci``. See our                       |
| :doc:`Database Software Requirements </install/software-hardware-requirements>` documentation for details on MySQL 8.0 support.          |
|                                                                                                                                          |
| **To use TLS with MySQL databases**                                                                                                      |
|                                                                                                                                          |
| The parameter to encrypt connection against a MySQL server is ``tls``.                                                                   |
| The library used to interact with MySQL is `Go-MySQL-Driver <https://pkg.go.dev/github.com/go-sql-driver/mysql>`__.                      |
| For the moment, it's not possible to use all the values that you could pass to a standard MySQL Client ``mysql --ssl-mode=value``.       |
| See `Connection-Encryption Option Summary <https://dev.mysql.com/doc/refman/8.0/en/connection-options.html #option_general_ssl-mode>`__  |
| documentation for a version 8.0 example.                                                                                                 |
|                                                                                                                                          |
| Your database admin must configure the functionality according to supported values described below:                                      |
|                                                                                                                                          |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
| | Short description of the ``tls``       | Value           | Example of a data source name                                             | |
| | parameter                              |                 |                                                                           | |
| +========================================+=================+===========================================================================+ |
| | Don't use TLS / SSL encryption against | ``false``       | ``"<mmuser:password>@tcp(hostname or IP:3306)/mattermost_test             | |
| | MySQL server.                          |                 | ?charset=utf8mb4,utf8&writeTimeout=30s&tls=false"``                       | |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
| | Use TLS / SSL encryption against       | ``true``        | ``"<mmuser:password>@tcp(hostname or IP:3306)/mattermost_test             | |
| | MySQL server.                          |                 | ?charset=utf8mb4,utf8&writeTimeout=30s&tls=true"``                        | |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
| | Use TLS / SSL encryption with a self-  | ``skip-verify`` | ``"<mmuser:password>@tcp(hostname or IP:3306)/mattermost_test             | |
| | signed certificate against             |                 | ?charset=utf8mb4,utf8&writeTimeout=30s&tls=skip-verify"``                 | |
| | MySQL server.                          |                 |                                                                           | |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
| | Use TLS / SSL encryption if server     | ``preferred``   | ``"<mmuser:password>@tcp(hostname or IP:3306)/mattermost_test             | |
| | advertises a possible fallback;        |                 | ?charset=utf8mb4,utf8&writeTimeout=30s&tls=preferred"``                   | |
| | unencrypted if it's not advertised.    |                 |                                                                           | |
| +----------------------------------------+-----------------+---------------------------------------------------------------------------+ |
|                                                                                                                                          |
+------------------------------------------------------------+-----------------------------------------------------------------------------+
| **AWS High Availablity RDS cluster deployments**                                                                                         |
|                                                                                                                                          |
| For an AWS High Availability RDS cluster deployment, point this configuration setting to the write/read endpoint at the **cluster**      |
| level to benefit from the AWS failover handling. AWS takes care of promoting different database nodes to be the writer node.             |
| Mattermost doesn't need to manage this. See the                                                                                          |
| :ref:`high availablility database configuration <scale/high-availability-cluster-based-deployment:database configuration>` documentation |
| for details.                                                                                                                             |
+------------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: database-maxopenconnections
  :displayname: Maximum open connections (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.MaxOpenConns
  :environment: MM_SQLSETTINGS_MAXOPENCONNS
  :description: The maximum number of idle connections held open to the database. Default is **300**.

Maximum open connections
~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+------------------------------------------------------------------+
| The maximum number of open connections to the          | - System Config path: **Environment > Database**                 |
| database.                                              | - ``config.json`` setting: ``".SqlSettings.MaxOpenConns": 300,`` |
|                                                        | - Environment variable: ``MM_SQLSETTINGS_MAXOPENCONNS``          |
| Numerical input. Default is **300** for self-hosted    |                                                                  |
| deployments, and **100** for Cloud deployments.        |                                                                  |
+--------------------------------------------------------+------------------------------------------------------------------+

.. config:setting:: database-querytimeout
  :displayname: Query timeout (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.QueryTimeout
  :environment: MM_SQLSETTINGS_QUERYTIMEOUT
  :description: The amount of time to wait, in seconds, for a response from the database after opening a connection and sending the query. Default is **30** seconds.

Query timeout
~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+------------------------------------------------------------------+
| The amount of time to wait, in seconds, for a response | - System Config path: **Environment > Database**                 |
| from the database after opening a connection and       | - ``config.json`` setting: ``".SqlSettings.QueryTimeout: 30",``  |
| sending the query.                                     | - Environment variable: ``MM_SQLSETTINGS_QUERYTIMEOUT``          |
|                                                        |                                                                  |
| Numerical input in seconds. Default is **30** seconds. |                                                                  |
+--------------------------------------------------------+------------------------------------------------------------------+

.. config:setting:: database-maxconnectionlifetime
  :displayname: Maximum connection lifetime (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.ConnMaxLifetimeMilliseconds
  :environment: MM_SQLSETTINGS_CONNMAXLIFETIMEMILLISECONDS
  :description: Maximum lifetime for a connection to the database, in milliseconds. Default is **3600000** milliseconds (1 hour).

Maximum connection lifetime
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+-------------------------------------------------------------------------------------+
| Maximum lifetime for a connection to the database,     | - System Config path: **Environment > Database**                                    |
| in milliseconds. Use this setting to configure the     | - ``config.json`` setting: ``".SqlSettings.ConnMaxLifetimeMilliseconds: 3600000",`` |
| maximum amount of time a connection to the database    | - Environment variable: ``MM_SQLSETTINGS_CONNMAXLIFETIMEMILLISECONDS``              |
| may be reused                                          |                                                                                     |
|                                                        |                                                                                     |
| Numerical input in milliseconds. Default is            |                                                                                     |
| **3600000** milliseconds (1 hour).                     |                                                                                     |
+--------------------------------------------------------+-------------------------------------------------------------------------------------+

.. config:setting:: database-connmaxidletime
  :displayname: Maximum connection idle timeout (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.ConnMaxIdleTimeMilliseconds
  :environment: MM_SQLSETTINGS_CONNMAXIDLETIMEMILLISECONDS
  :description: Maximum time a database connection can remain idle, in milliseconds. Default is **300000** milliseconds (5 minutes).

Maximum connection idle timeout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+-------------------------------------------------------------------------------------+
| Maximum time a database connection can remain idle,    | - System Config path: **Environment > Database**                                    |
| in milliseconds.                                       | - ``config.json`` setting: ``".SqlSettings.ConnMaxIdleTimeMilliseconds: 300000",``  |
|                                                        | - Environment variable: ``MM_SQLSETTINGS_CONNMAXIDLETIMEMILLISECONDS``              |
| Numerical input in milliseconds. Default is **300000** |                                                                                     |
| (5 minutes).                                           |                                                                                     |
+--------------------------------------------------------+-------------------------------------------------------------------------------------+

.. config:setting:: database-minhashtaglength
  :displayname: Minimum hashtag length (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.MinimumHashtagLength
  :environment: MM_SQLSETTINGS_MINIMUMHASHTAGLENGTH
  :description: Minimum number of characters in a hashtag. This value must be greater than or equal to **2**. Default is **3**.

Minimum hashtag length
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------------+-------------------------------------------------------------------------+
| Minimum number of characters in a hashtag.                           | - System Config path: **Environment > Database**                        |
| This value must be greater than or equal to **2**.                   | - ``config.json`` setting: ``".SqlSettings.MinimumHashtagLength: 3",``  |
|                                                                      | - Environment variable: ``MM_SQLSETTINGS_MINIMUMHASHTAGLENGTH``         |
+----------------------------------------------------------------------+-------------------------------------------------------------------------+
| **Note**: MySQL databases must be configured to support searching strings shorter than three characters. See the                               |
| `MySQL documentation <https://dev.mysql.com/doc/refman/8.0/en/fulltext-fine-tuning.html>`__ for details.                                       |
+----------------------------------------------------------------------+-------------------------------------------------------------------------+

.. config:setting:: database-sqltrace
  :displayname: SQL statement logging (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.Trace
  :environment: MM_SQLSETTINGS_TRACE

  - **true**: Executing SQL statements are written to the log.
  - **false**: **(Default)** SQL statements aren't written to the log.

SQL statement logging
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Executed SQL statements can be written to the log for         | - System Config path: **Environment > Database**                         |
| development.                                                  | - ``config.json`` setting: ``".SqlSettings.Trace: false",``              |
|                                                               | - Environment variable: ``MM_SQLSETTINGS_TRACE``                         |
| - **true**: Executing SQL statements are written to the log.  |                                                                          |
| - **false**: **(Default)** SQL statements aren't written      |                                                                          |
|   to the log.                                                 |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Recycle database connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

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

.. config:setting:: database-disablesearch
  :displayname: Disable database search (Database)
  :systemconsole: Environment > Database
  :configjson: .SqlSettings.DisableDatabaseSearch
  :environment: MM_SQLSETTINGS_DISABLEDATABASESEARCH

  - **true**: Disables the use of the database to perform searches. If another search engine isn't configured, setting this value to ``true`` will result in empty search results.
  - **false**: **(Default)** Database search isn't disabled.

Disable database search
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+------------------------------------------------------------------------------+
| When other search engines are configured, such as             | - System Config path: **Environment > Database**                             |
| :doc:`Elasticsearch </scale/elasticsearch>`,                  | - ``config.json`` setting: ``".SqlSettings.DisableDatabaseSearch: false",``  |
| the database can be disabled to perform searches.             | - Environment variable: ``MM_SQLSETTINGS_DISABLEDATABASESEARCH``             |
|                                                               |                                                                              |
| - **true**: Disables the use of the database to perform       |                                                                              |
|   searches. If another search engine isn't configured,        |                                                                              |
|   setting this value to ``true`` will result in empty search  |                                                                              |
|   results.                                                    |                                                                              |
| - **false**: **(Default)** Database search isn't disabled.    |                                                                              |
+---------------------------------------------------------------+------------------------------------------------------------------------------+
| Search behavior in Mattermost depends on which search engines are enabled.                                                                   |
|                                                                                                                                              |
| - When :doc:`Elasticsearch </scale/elasticsearch>` is enabled, Mattermost will try to use it first.                                          |
| - If Elasticsearch fails or is disabled, Mattermost will attempt to use :doc:`Bleve </deploy/bleve-search>`, if enabled. If this occurs,     |
|   you will see the warning ``Encountered error on SearchPostsInTeamForUser.``                                                                |
| - If both Elasticsearch and Bleve fail or are disabled, Mattermost tries to search the database directly, if this is enabled.                |
| - If all of the above methods fail or are disabled, the search results will be empty.                                                        |
+---------------------------------------------------------------+------------------------------------------------------------------------------+

Applied schema migrations
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

A list of all migrations that have been applied to the data store based on the version information available in the ``db_migrations`` table. Select **About Mattermost** from the product menu to review the current database schema version applied to your deployment.


.. config:setting:: database-activesearchbackend
  :displayname: Active search backend (Database)
  :systemconsole: Environment > Database
  :configjson: N/A
  :environment: N/A
  :description: Read-only display of the currently active backend used for search.

Active Search Backend
~~~~~~~~~~~~~~~~~~~~~

Read-only display of the currently active backend used for search. Values can include ``none``, ``database``, ``elasticsearch``, or ``bleve``.

.. config:setting:: database-readreplicas
  :displayname: Read replicas (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.DataSourceReplicas
  :environment: MM_SQLSETTINGS_DATASOURCEREPLICAS
  :description: Specifies the connection strings for the read replica databases.

Read replicas
~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+-----------------------------------------------------------------------+
| Specifies the connection strings for the read replica  | - System Config path: N/A                                             |
| databases.                                             | - ``config.json`` setting: ``".SqlSettings.DataSourceReplicas": []``  |
|                                                        | - Environment variable: ``MM_SQLSETTINGS_DATASOURCEREPLICAS``         |
+--------------------------------------------------------+-----------------------------------------------------------------------+
| **Note**: Each database connection string in the array must be in the same form used for the                                   |
| `Data source <#data-source>`__ setting.                                                                                        |
+--------------------------------------------------------+-----------------------------------------------------------------------+
| **AWS High Availablity RDS cluster deployments**                                                                               |
|                                                                                                                                |
| For an AWS High Availability RDS cluster deployment, point this configuration setting directly to the underlying read-only     |
| node endpoint within the RDS cluster to circumvent the failover/load balancing that AWS/RDS takes care of (except for the      |
| write traffic). Mattermost has its own method of balancing the read-only connections, and can also balance those queries to    |
| the data source/write+read connection should those nodes fail. See the                                                         |
| :ref:`high availablility database configuration <scale/high-availability-cluster-based-deployment:database configuration>`     |
| documentation for details.                                                                                                     |
+--------------------------------------------------------+-----------------------------------------------------------------------+

.. config:setting:: database-searchreplicas
  :displayname: Search replicas (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.DataSourceSearchReplicas
  :environment: MM_SQLSETTINGS_DATASOURCESEARCHREPLICAS

  Specifies the connection strings for the search replica databases.
  A search replica is similar to a read replica, but is used only for handling search queries.

Search replicas
~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-pro-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+--------------------------------------------------------+-----------------------------------------------------------------------------+
| Specifies the connection strings for the search        | - System Config path: N/A                                                   |
| replica databases. A search replica is similar to a    | - ``config.json`` setting: ``".SqlSettings.DataSourceSearchReplicas": []``  |
| read replica, but is used only for handling search     | - Environment variable: ``MM_SQLSETTINGS_DATASOURCESEARCHREPLICAS``         |
| queries.                                               |                                                                             |
+--------------------------------------------------------+-----------------------------------------------------------------------------+
| **Note**: Each database connection string in the array must be in the same form used for the `Data source <#data-source>`__          |
| setting.                                                                                                                             |
+--------------------------------------------------------+-----------------------------------------------------------------------------+
| **AWS High Availablity RDS cluster deployments**                                                                                     |
|                                                                                                                                      |
| For an AWS High Availability RDS cluster deployment, point this configuration setting directly to the underlying read-only           |
| node endpoint within the RDS cluster to circumvent the failover/load balancing that AWS/RDS takes care of (except for the            |
| write traffic). Mattermost has its own method of balancing the read-only connections, and can also balance those queries to          |
| the data source/write+read connection should those nodes fail. See the                                                               |
| :ref:`high availablility database configuration <scale/high-availability-cluster-based-deployment:database configuration>`           |
| documentation for details.                                                                                                           |
+--------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: database-replicalagsettings
  :displayname: Replica lag settings (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.ReplicaLagSettings
  :environment: MM_SQLSETTINGS_REPLICALAGSETTINGS
  :description: Specifies a connection string and user-defined SQL queries on the database to measure replica lag for a single replica instance.

Replica lag settings
~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/ent-only.rst
  :start-after: :nosearch:

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+--------------------------------------------------------+----------------------------------------------------------------------------------+
| String array input specifies a connection string and   | - System Config path: N/A                                                        |
| user-defined SQL queries on the database to measure    | - ``config.json`` setting: ``".SqlSettings.ReplicaLagSettings": []``             |
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
| **Notes**:                                                                                                                                |
|                                                                                                                                           |
| - The ``QueryAbsoluteLag`` and ``QueryTimeLag`` queries must return a single row.                                                         |
| - To properly monitor this, you must setup :doc:`performance monitoring </scale/deploy-prometheus-grafana-for-performance-monitoring>`    |
|   for Mattermost.                                                                                                                         |
+--------------------------------------------------------+----------------------------------------------------------------------------------+

1. Configure the replica lag metric based on your database type. See the following tabs for details on configuring this for each database type.

  .. tab:: AWS Aurora

    Add the configuration highlighted below to your ``SqlSettings.ReplicaLagSettings`` array. You only need to add this once because replication statistics for AWS Aurora nodes are visible across all server instances that are members of the cluster. Be sure to change the ``DataSource`` to point to a single node in the group. 

    For more information on Aurora replication stats, see the `AWS Aurora documentaion <https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora_global_db_instance_status.html>`__.

    **Example:**

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

    **Example:**

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
3. Navigate to your Grafana instance monitoring Mattermost and open the `Mattermost Performance Monitoring v2 <https://grafana.com/grafana/dashboards/15582-mattermost-performance-monitoring-v2/>`__ dashboard.
4. The ``QueryTimeLag`` chart is already setup for you utilizing the existing ``Replica Lag`` chart. If using ``QueryAbsoluteLag`` metric clone the ``Replica Lag`` chart and edit the query to use the below absolute lag metrics and modify the title to be ``Replica Lag Absolute``.

  .. code-block:: text

    mattermost_db_replica_lag_abs{instance=~"$server"}

  .. image::  ../../source/images/database-configuration-settings-replica-lag-grafana-1.jpg
    :alt: A screenshot showing how to clone a chart within Grafana


  .. image:: ../../source/images/database-configuration-settings-replica-lag-grafana-2.jpg
    :alt: A screenshot showing the specific edits to make to the cloned grafana chart.


.. config:setting:: database-replicamonitorintervalseconds
  :displayname: Replica monitor interval (Database)
  :systemconsole: N/A
  :configjson: .SqlSettings.ReplicaMonitorIntervalSeconds
  :environment: MM_SQLSETTINGS_REPLICAMONITORINTERVALSECONDS

  Specifies how frequently unhealthy replicas will be monitored for liveness check. Mattermost will dynamically choose a replica if it's alive.

Replica monitor interval (seconds)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

+--------------------------------------------------------+---------------------------------------------------------------------------------+
| Specifies how frequently unhealthy replicas will be    | - System Config path: N/A                                                       |
| monitored for liveness check. Mattermost will          | - ``config.json`` setting: ``".SqlSettings.ReplicaMonitorIntervalSeconds": 5``  |
| dynamically choose a replica if it's alive.            | - Environment variable: ``MM_SQLSETTINGS_REPLICAMONITORINTERVALSECONDS``        |
|                                                        |                                                                                 |
| Numerical input. Default is 5 seconds.                 |                                                                                 |
+--------------------------------------------------------+---------------------------------------------------------------------------------+

----

Elasticsearch
-------------

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

Elasticsearch provides enterprise-scale deployments with optimized search performance and prevents performance degradation and timeouts. Learn more about :doc:`Elasticsearch </scale/elasticsearch>` in our product documentation.

You can configure the Elasticsearch environment in which Mattermost is deployed in **System Console > Environment > Elasticsearch**. You can also edit the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: elastic-enableindexing
  :displayname: Enable Elasticsearch indexing (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.EnableIndexing
  :environment: MM_ELASTICSEARCHSETTINGS_ENABLEINDEXING
  :description: Configure Mattermost to index new posts automatically.

  - **true**: Indexing of new posts occurs automatically.
  - **false**: **(Default)** Elasticsearch indexing is disabled and new messages aren't indexed.

Enable Elasticsearch indexing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------------+
| Configure Mattermost to index new posts automatically.        | - System Config path: **Environment > Elasticsearch**                          |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.EnableIndexing: false",`` |
| - **true**: Indexing of new messages occurs automatically.    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_ENABLEINDEXING``            |
| - **false**: **(Default)** Elasticsearch indexing is disabled |                                                                                |
|   and new messages aren't indexed.                            |                                                                                |
+---------------------------------------------------------------+--------------------------------------------------------------------------------+
| **Notes**:                                                                                                                                     |
|                                                                                                                                                |
| - Core search happens in a relational database and is intended for deployments under about 2-3 million posts and file entries. Beyond that     |
|   scale, `enabling Elasticsearch for search queries <#enable-elasticsearch-for-search-queries>`__ is highly recommended                        |
| - If you anticipate your Mattermost server reaching more than 2.5 million posts and file entries, we recommend enabling Elasticsearch for      |
|   optimum search performance **before** reaching 3 million posts.                                                                              |
| - For deployments with over 3 million posts, Elasticsearch is required to avoid significant performance issues, such as timeouts, with         |
|   :doc:`message searches </collaborate/search-for-messages>` and :doc:`@mentions </collaborate/mention-people>`.                               |
| - If indexing is disabled and then re-enabled after an index is created, purge and rebuild the index to ensure complete search results.        |
+---------------------------------------------------------------+--------------------------------------------------------------------------------+

.. config:setting:: elastic-backendtype
  :displayname: Elasticsearch backend type (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.Backend
  :environment: MM_ELASTICSEARCHSETTINGS_BACKEND
  :description: Set the type of search backend as either Elasticsearch or Opensearch.

Backend type
~~~~~~~~~~~~~

+----------------------------------------------------+-----------------------------------------------------------------------------------+
| The type of search backend.                        | - System Config path: **Environment > Elasticsearch**                             |
|                                                    | - ``config.json`` setting: ``".Elasticsearchsettings.Backend: elasticsearch",``   |
| - ``elasticsearch`` - (**Default**)                | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_BACKEND``                      |
| - ``opensearch`` - Required for AWS Opensearch     |                                                                                   |
|   customers.                                       |                                                                                   |
+----------------------------------------------------+-----------------------------------------------------------------------------------+

.. important::

  Mattermost v9.11 introduces support for `Elasticsearch v8 <https://www.elastic.co/guide/en/elasticsearch/reference/current/elasticsearch-intro.html>`__ and beta support for `Opensearch v1.x and v2.x <https://opensearch.org/>`_.

  - Mattermost supports Elasticsearch v7.17+. However, we recommend upgrading your Elasticsearch v7 instance to v8.x. See the `Elasticsearch upgrade <https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html>`_ documentation for details.
  - Customers using Elasticsearch v8 must set ``action.destructive_requires_name`` to ``false`` in ``elasticsearch.yml`` to enable wildcard operations.

  **AWS Elasticsearch Customers**

  The official AWS Elasticsearch v8 client only works from Elasticsearch v7.11 and later. This is a breaking change for customers using AWS Elasticsearch v7.10.x. If you're using AWS Elasticsearch, you must upgrade to `AWS Opensearch <https://aws.amazon.com/opensearch-service/>`_. See the `AWS Amazon Opensearch upgrade <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/version-migration.html>`_ documentation for details.

  If you're using AWS Elasticsearch, you must:

    1. Upgrade to AWS Opensearch for future compatibility. Refer to the `Opensearch upgrade <https://docs.aws.amazon.com/opensearch-service/latest/developerguide/version-migration.html>`_ documentation for details.
    2. Disable "compatibility mode" in Opensearch.
    3. Upgrade the Mattermost server.
    4. Change the default ``ElasticsearchSettings.Backend`` configuration value from ``elasticsearch`` to ``opensearch`` using :ref:`mmctl config set <manage/mmctl-command-line-tool:mmctl config set>`, or by editing the ``config.json`` file manually. This value cannot be changed using the System Console. See the Mattermost :ref:`Elasticsearch backend type <configure/environment-configuration-settings:backend type>` documentation for additional details.
    5. Restart the Mattermost server.

.. config:setting:: elastic-serverconnectionaddress
  :displayname: Server connection address (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.ConnectionUrl
  :environment: MM_ELASTICSEARCHSETTINGS_CONNECTIONURL
  :description: The address of the Elasticsearch server.

Server connection address
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------+--------------------------------------------------------------------------+
| The address of the Elasticsearch server.           | - System Config path: **Environment > Elasticsearch**                    |
|                                                    | - ``config.json`` setting: ``".Elasticsearchsettings.ConnectionUrl",``   |
|                                                    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CONNECTIONURL``       |
+----------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-CApath
  :displayname: CA path (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.CA
  :environment: MM_ELASTICSEARCHSETTINGS_CA
  :description: Optional path to the Custom Certificate Authority certificates for the Elasticsearch server.

CA path
~~~~~~~

+----------------------------------------------------+--------------------------------------------------------------------------+
| Optional path to the Custom Certificate Authority  | - System Config path: **Environment > Elasticsearch**                    |
| certificates for the Elasticsearch server.         | - ``config.json`` setting: ``".Elasticsearchsettings.CA",``              |
|                                                    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CA``                  |
+----------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: Available from Mattermost v7.8. Can be used in conjunction with basic auth credentials or to replace them.          |
| Leave this setting blank to use the default Certificate Authority certificates for the operating system.                      |
+----------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-clientcertificatepath
  :displayname: Client certificate path (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.ClientCert
  :environment: MM_ELASTICSEARCHSETTINGS_CLIENTCERT
  :description: Optional client certificate for the connection to the Elasticsearch server in PEM format.

Client certificate path
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+--------------------------------------------------------------------------+
| Optional client certificate for the connection to  | - System Config path: **Environment > Elasticsearch**                    |
| the Elasticsearch server in the PEM format.        | - ``config.json`` setting: ``".Elasticsearchsettings.ClientCert",``      |
|                                                    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CLIENTCERT``          |
+----------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: Available from Mattermost v7.8. Can be used in conjunction with basic auth credentials or to replace them.          |
+----------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-clientcertificatekeypath
  :displayname: Client certificate key path (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.ClientKey
  :environment: MM_ELASTICSEARCHSETTINGS_CLIENTKEY
  :description: Optional key for the client certificate in PEM format.

Client certificate key path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+--------------------------------------------------------------------------+
| Optional key for the client certificate in the PEM | - System Config path: **Environment > Elasticsearch**                    |
| format.                                            | - ``config.json`` setting: ``".Elasticsearchsettings.ClientKey",``       |
|                                                    | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CLIENTKEY``           |
+----------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: Available from Mattermost v7.8. Can be used in conjunction with basic auth credentials or to replace them.          |
+----------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-skiptlsverification
  :displayname: Skip TLS verification (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.SkipTLSVerification
  :environment: MM_ELASTICSEARCHSETTINGS_SKIPTLSVERIFICATION
  :description: The certificate step for TLS connections can be skipped.

  - **true**: Skips the certificate verification step for TLS connections.
  - **false**: **(Default)** Mattermost does not skip certificate verification.

Skip TLS verification
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------------------------------+
| The certificate step for TLS connections can be skipped.      | - System Config path: **Environment > Elasticsearch**                               |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.SkipTLSVerification: false",`` |
| - **true**: Skips the certificate verification step for       | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_SKIPTLSVERIFICATION``            |
|   TLS connections.                                            |                                                                                     |
| - **false**: **(Default)** Mattermost does not skip           |                                                                                     |
|   certificate verification.                                   |                                                                                     |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------+

.. config:setting:: elastic-serverusername
  :displayname: Server username (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.UserName
  :environment: MM_ELASTICSEARCHSETTINGS_USERNAME
  :description: (Optional) The username to authenticate to the Elasticsearch server.

Server username
~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| (Optional) The username to authenticate to the                | - System Config path: **Environment > Elasticsearch**                    |
| Elasticsearch server.                                         | - ``config.json`` setting: ``".Elasticsearchsettings.UserName",``        |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_USERNAME``            |
| String input.                                                 |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-serverpassword
  :displayname: Server password (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.Password
  :environment: MM_ELASTICSEARCHSETTINGS_PASSWORD
  :description: (Optional) The password to authenticate to the Elasticsearch server.

Server password
~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| (Optional) The password to authenticate to the                | - System Config path: **Environment > Elasticsearch**                    |
| Elasticsearch server.                                         | - ``config.json`` setting: ``".Elasticsearchsettings.Password",``        |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_PASSWORD``            |
| String input.                                                 |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-enablesniffing
  :displayname: Enable cluster sniffing (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.Sniff
  :environment: MM_ELASTICSEARCHSETTINGS_SNIFF
  :description: Configure Mattermost to automatically find and connect to all data nodes in a cluster.

  - **true**: Sniffing finds and connects to all data nodes in your cluster automatically.
  - **false**: **(Default)** Cluster sniffing is disabled.

Enable cluster sniffing
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------+--------------------------------------------------------------------------+
| Configure Mattermost to automatically find and connect to      | - System Config path: **Environment > Elasticsearch**                    |
| all data nodes in a cluster.                                   | - ``config.json`` setting: ``".Elasticsearchsettings.Sniff: false",``    |
|                                                                | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_SNIFF``               |
| - **true**: Sniffing finds and connects to all data nodes      |                                                                          |
|   in your cluster automatically.                               |                                                                          |
| - **false**: **(Default)** Cluster sniffing is disabled.       |                                                                          |
+----------------------------------------------------------------+--------------------------------------------------------------------------+
| Select the **Test Connection** button in the System Console to validate the connection between Mattermost and the Elasticsearch server.   |
+----------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-bulkindexing
  :displayname: Bulk indexing (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: N/A
  :environment: N/A
  :description: Configure Mattermost to start a bulk index of all existing posts in the database by selecting Index Now.

Bulk indexing
~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Configure Mattermost to start a bulk index of all existing    | - System Config path: **Environment > Elasticsearch**                    |
| posts in the database, from oldest to newest.                 | - ``config.json`` setting: N/A                                           |
|                                                               | - Environment variable: N/A                                              |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **Notes**:                                                                                                                               |
|                                                                                                                                          |
| - Always `purge indexes <#purge-indexes>`__ before bulk indexing.                                                                        |
| - Select the **Index Now** button in the System Console to start a bulk index of all posts, and review all index jobs in progress.       |
| - Elasticsearch is available during indexing, but search results may be incomplete until the indexing job is complete.                   |
| - If an in-progress indexing job is canceled, the index and search results will be incomplete.                                           |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-rebuildchannelsindex
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
| Select the **Rebuild Channels Index** button in the System Console to purge the channels index.                               |
| Ensure no other indexing jobs are in progress via the **Bulk Indexing** table before starting this process.                   |
| During indexing, channel auto-complete is available, but search results may be incomplete until the indexing job is complete. |
+---------------------------------------------------------------+---------------------------------------------------------------+

.. config:setting:: elastic-purgeindexes
  :displayname: Purge indexes (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: N/A
  :environment: N/A
  :description: Purge the entire Elasticsearch index by selecting Purge Indexes before creating a new index.

Purge indexes
~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-------------------------------------------+-------------------------------------------------------------+
| Purge the entire Elasticsearch index.     | - System Config path: **Environment > Elasticsearch**       |
|                                           | - ``config.json`` setting: N/A                              |
|                                           | - Environment variable: N/A                                 |
+-------------------------------------------+-------------------------------------------------------------+
| Select the **Purge Indexes** button in the System Console to purge the index.                           |
| After purging the index, create a new index by selecting the **Index Now** button.                      |
+-------------------------------------------+-------------------------------------------------------------+

.. config:setting:: elastic-indexestoskipwhilepurging
  :displayname: Indexes to skip while purging (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.IgnoredPurgeIndexes
  :environment: MM_ELASTICSEARCHSETTINGS_IGNOREDPURGEINDEXES
  :description: Specify index names to ignore while purging indexes, separated by commas.

Indexes to skip while purging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------------------+
| Specify index names to ignore while purging indexes.          | - System Config path: **Environment > Elasticsearch**                     |
| Separate multiple index names with commas.                    | - ``config.json`` setting: ``ElasticsearchSettings.IgnoredPurgeIndexes``  |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_IGNOREDPURGEINDEXES``  |
| Use an asterisk (*) to match a sequence of index name         |                                                                           |
| characters.                                                   |                                                                           |
+---------------------------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: elastic-enablesearch
  :displayname: Enable Elasticsearch for search queries (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.EnableSearching
  :environment: MM_ELASTICSEARCHSETTINGS_ENABLESEARCHING
  :description: Configure Mattermost to use Elasticsearch for all search queries using the latest index.

  - **true**: Elasticsearch is used for all search queries using the latest index. Search results may be incomplete until a bulk index of the existing message database is completed.
  - **false**: **(Default)** Relational database search is used for search queries.

Enable Elasticsearch for search queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

.. important::

  - Core search happens in a relational database and is intended for deployments under about 2-3 million posts and file entries. Beyond that scale, enabling Elasticsearch for search queries is highly recommended.
  - If you anticipate your Mattermost server reaching more than 2.5 million posts and file entries, we recommend enabling Elasticsearch for optimum search performance **before** reaching 3 million posts.
  - For deployments with over 3 million posts, Elasticsearch with :ref:`dedicated indexing <configure/environment-configuration-settings:enable elasticsearch indexing>` and scaled usage resourcing through :doc:`cluster support </scale/high-availability-cluster-based-deployment>` is required to avoid significant performance issues, such as timeouts, with :doc:`message searches </collaborate/search-for-messages>` and :doc:`@mentions </collaborate/mention-people>`.

+---------------------------------------------------------------+---------------------------------------------------------------------------------+
| Configure Mattermost to use Elasticsearch for all search      | - System Config path: **Environment > Elasticsearch**                           |
| queries using the latest index.                               | - ``config.json`` setting: ``".Elasticsearchsettings.EnableSearching: false",`` |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_ENABLESEARCHING``            |
| - **true**: Elasticsearch is used for all search queries      |                                                                                 |
|   using the latest index. Search results may be incomplete    |                                                                                 |
|   until a bulk index of the existing message database is      |                                                                                 |
|   completed.                                                  |                                                                                 |
| - **false**: **(Default)** Database search is used for        |                                                                                 |
|   search queries.                                             |                                                                                 |
+---------------------------------------------------------------+---------------------------------------------------------------------------------+
| **Note**: If indexing is disabled and then re-enabled after an index is created, purge and rebuild the index to ensure complete search results. |
+---------------------------------------------------------------+---------------------------------------------------------------------------------+

.. config:setting:: elastic-enableautocomplete
  :displayname: Enable Elasticsearch for autocomplete queries (Elasticsearch)
  :systemconsole: Environment > Elasticsearch
  :configjson: .Elasticsearchsettings.EnableAutocomplete
  :environment: MM_ELASTICSEARCHSETTINGS_ENABLEAUTOCOMPLETE
  :description: Configure Mattermost to use Elasticsearch for all autocompletion queries on users and channels using the latest index.

  - **true**: Elasticsearch will be used for all autocompletion queries on users and channels using the latest index.
  - **false**: **(Default)** Database autocomplete is used.

Enable Elasticsearch for autocomplete queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+------------------------------------------------------------------------------------+
| Configure Mattermost to use Elasticsearch for all             | - System Config path: **Environment > Elasticsearch**                              |
| autocompletion queries on users and channels using the        | - ``config.json`` setting: ``".Elasticsearchsettings.EnableAutocomplete: false",`` |
| latest index.                                                 | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_ENABLEAUTOCOMPLETE``            |
|                                                               |                                                                                    |
| - **true**: Elasticsearch will be used for all autocompletion |                                                                                    |
|   queries on users and channels using the latest index.       |                                                                                    |
| - **false**: **(Default)** Database autocomplete is used.     |                                                                                    |
+---------------------------------------------------------------+------------------------------------------------------------------------------------+
| **Note**: Autocompletion results may be incomplete until a bulk index of the existing users and channels database is finished.                     |
+---------------------------------------------------------------+------------------------------------------------------------------------------------+

.. config:setting:: elastic-postindexreplicas
  :displayname: Post index replicas (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.PostIndexReplicas
  :environment: MM_ELASTICSEARCHSETTINGS_POSTINDEXREPLICAS
  :description: The number of replicas to use for each post index. Default is **1**.

Post index replicas
~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The number of replicas to use for each post index.            | - System Config path: N/A                                                     |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.PostIndexReplicas: 1",`` |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_POSTINDEXREPLICAS``        |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Important notes**:                                                                                                                          |
|                                                                                                                                               |
| - If this setting is changed, the changed configuration only applies to newly-created indexes. To apply the change to existing indexes,       |
|   purge and rebuild the index after changing this setting.                                                                                    |
| - If there are ``n`` data nodes, the number of replicas per shard for each index should be ``n-1``.                                           |
| - If the number of nodes in an Elasticsearch cluster changes, this configuration setting, as well as                                          |
|   `Channel Index Replicas <#channel-index-replicas>`__ and `User Index Replicas <#user-index-replicas>`__ must also be updated accordingly.   |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

.. config:setting:: elastic-postindexshards
  :displayname: Post index shards (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.PostIndexShards
  :environment: MM_ELASTICSEARCHSETTINGS_POSTINDEXSHARDS
  :description: The number of shards to use for each post index. Default is **1**.

Post index shards
~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The number of shards to use for each post index.              | - System Config path: N/A                                                     |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.PostIndexShards: 1",``   |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_POSTINDEXSHARDS``          |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Important note**: If this configuration setting is changed, the changed configuration only applies to newly-created indexes.                |
| To apply the change to existing indexes, purge and rebuild the index after changing this setting.                                             |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+


.. config:setting:: elastic-channelindexreplicas
  :displayname: Channel index replicas (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.ChannelIndexReplicas
  :environment: MM_ELASTICSEARCHSETTINGS_CHANNELINDEXREPLICAS
  :description: The number of replicas to use for each channel index. Default is **1**.

Channel index replicas
~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+----------------------------------------------------------------------------------+
| The number of replicas to use for each channel index.         | - System Config path: N/A                                                        |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.ChannelIndexReplicas: 1",`` |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CHANNELINDEXREPLICAS``        |
+---------------------------------------------------------------+----------------------------------------------------------------------------------+
| **Note**: If there are ``n`` data nodes, the number of replicas per shard for each index should be ``n-1``. If the number of nodes in an         |
| Elasticsearch cluster changes, this configuration setting, as well as `Post Index Replicas <#post-index-shards>`__ and                           |
| `User Index Replicas <#user-index-replicas>`__ must also be updated accordingly.                                                                 |
+---------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: elastic-channelindexshards
  :displayname: Channel index shards (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.ChannelIndexShards
  :environment: MM_ELASTICSEARCHSETTINGS_CHANNELINDEXSHARDS
  :description: The number of shards to use for each channel index. Default is **1**.

Channel index shards
~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+----------------------------------------------------------------------------------+
| The number of shards to use for each channel index.           | - System Config path: N/A                                                        |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.ChannelIndexShards: 1",``   |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_CHANNELINDEXSHARDS``          |
+---------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: elastic-userindexreplicas
  :displayname: User index replicas (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.UserIndexReplicas
  :environment: MM_ELASTICSEARCHSETTINGS_USERINDEXREPLICAS
  :description: The number of replicas to use for each user index. Default is **1**.

User index replicas
~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The number of replicas to use for each user index.            | - System Config path: N/A                                                     |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.UserIndexReplicas: 1",`` |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_USERINDEXREPLICAS``        |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| **Note**: If there are ``n`` data nodes, the number of replicas per shard for each index should be ``n-1``. If the number of nodes in an      |
| Elasticsearch cluster changes, this configuration setting, as well as `Post Index Replicas <#post-index-replicas>`__ and                      |
| `Channel Index Replicas <#channel-index-replicas>`__ must also be updated accordingly.                                                        |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

.. config:setting:: elastic-userindexshards
  :displayname: User index shards (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.UserIndexShards
  :environment: MM_ELASTICSEARCHSETTINGS_USERINDEXSHARDS
  :description: The number of shards to use for each user index. Default is **1**.

User index shards
~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+----------------------------------------------------------------------------------+
| The number of shards to use for each user index.              | - System Config path: N/A                                                        |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.UserIndexShards: 1",``      |
| Numerical input. Default is **1**.                            | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_USERINDEXSHARDS``             |
+---------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: elastic-aggregatesearchindexes
  :displayname: Aggregate search indexes (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.AggregatePostsAfterDays
  :environment: MM_ELASTICSEARCHSETTINGS_AGGREGATEPOSTSAFTERDAYS
  :description: Elasticsearch indexes older than the age specified by this setting, in days, will be aggregated during the daily scheduled job. Default is **365** days.

Aggregate search indexes
~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Elasticsearch indexes older than the age specified by this    | - System Config path: N/A                                                              |
| setting, in days, will be aggregated during the daily         | - ``config.json`` setting: ``".Elasticsearchsettings.AggregatePostsAfterDays: 365",``  |
| scheduled job.                                                | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_AGGREGATEPOSTSAFTERDAYS``           |
|                                                               |                                                                                        |
| Numerical input. Default is **365** days.                     |                                                                                        |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
| **Note**: If you’re using :doc:`data retention </comply/data-retention-policy>` and                                                                    |
| :doc:`Elasticsearch </scale/elasticsearch>`, configure this with a value greater than your data retention policy.                                      |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------+

.. config:setting:: elastic-postaggregatorstarttime
  :displayname: Post aggregator start time (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.PostsAggregatorJobStartTime
  :environment: MM_ELASTICSEARCHSETTINGS_POSTSAGGREGATORJOBSTARTTIME
  :description: The start time of the daily scheduled aggregator job. Must be a 24-hour time stamp in the form ``HH:MM`` based on the local time of the server. Default is **03:00** (3 AM).

Post aggregator start time
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| The start time of the daily scheduled aggregator job.         | - System Config path: N/A                                                                   |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.PostsAggregatorJobStartTime: 03:00",`` |
| Must be a 24-hour time stamp in the form ``HH:MM`` based on   | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_POSTSAGGREGATORJOBSTARTTIME``            |
| the local time of the server.                                 |                                                                                             |
|                                                               |                                                                                             |
| Default is **03:00** (3 AM)                                   |                                                                                             |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+

.. config:setting:: elastic-indexprefix
  :displayname: Index prefix (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.IndexPrefix
  :environment: MM_ELASTICSEARCHSETTINGS_INDEXPREFIX
  :description: The prefix added to the Elasticsearch index name.

Index prefix
~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The prefix added to the Elasticsearch index name.             | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.IndexPrefix",``     |
|                                                               | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_INDEXPREFIX``         |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: When this setting is used, all Elasticsearch indexes created by Mattermost are given this prefix. You can set different        |
| prefixes so that multiple Mattermost deployments can share an Elasticsearch cluster without the index names colliding.                   |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: elastic-liveindexingbatchsize
  :displayname: Live indexing batch size (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.LiveIndexingBatchSize
  :environment: MM_ELASTICSEARCHSETTINGS_LIVEINDEXINGBATCHSIZE
  :description: The number of new posts batched together before they're added to the Elasticsearch index. Default is **1**.

Live indexing batch size
~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-----------------------------------------------------------------------------------+
| The number of new posts needed before those posts are added   | - System Config path: N/A                                                         |
| to the Elasticsearch index. Once added to the Index,          | - ``config.json`` setting: ``".Elasticsearchsettings.LiveIndexingBatchSize: 1",`` |
| the post becomes searchable.                                  | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_LIVEINDEXINGBATCHSIZE``        |
|                                                               |                                                                                   |
| On servers with more than 1 post per second, we suggest       |                                                                                   |
| setting this value to the average number of  posts over a     |                                                                                   |
| 20 second period of time.                                     |                                                                                   |
|                                                               |                                                                                   |
| Numerical input. Default is **1**. Every post is indexed      |                                                                                   |
| synchronously as they are created.                            |                                                                                   |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------+
| **Note**: It may be necessary to increase this value to avoid hitting the rate limit or resource limit of your Elasticsearch cluster              |
| on installs handling more than 1 post per second.                                                                                                 |
|                                                                                                                                                   |
| **What exactly happens when I increase this value?**                                                                                              |
| The primary impact is that a post will be indexed into Elasticsearch after the threshold of posts is met which then makes the posts searchable    |
| within Mattermost. So, if you set this based on our recommendations for larger servers, and you make a post, you cannot find it via search        | 
| for ~ 10-20 seconds, on average. Realistically, no users should see or feel this impact due to the limited amount of users who are actively       |
| **searching** for a post this quickly. You can set this value to a lower average or higher average as well, depending on your Elasticsearch       |
| server specifications.                                                                                                                            |
|                                                                                                                                                   |
| During busy periods, this delay will be faster as more traffic is happening, causing more posts and a quicker time to hit the index number.       |
| During slow times, expect the reverse.                                                                                                            |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------+

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

2. Decide the acceptable index window for your environment, and divide your average posts per minute by that. We suggest 10-20 seconds. Assuming you have ``600`` posts per minute on average, and you want to index every 20 seconds (``60 seconds / 20 seconds = 3```) you would calculate ``600 / 3`` to come to the number ``200``. After 200 posts, Mattermost will index the posts into Elasticsearch. So, on average, there would be a 20-second delay in searchability.

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

.. config:setting:: elastic-batchsize
  :displayname: Batch size (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.BatchSize
  :environment: MM_ELASTICSEARCHSETTINGS_BATCHSIZE
  :description: The number of posts for a single batch during a bulk indexing job. Default is **10000**.

Batch size
~~~~~~~~~~~

+-------------------------------------------+---------------------------------------------------------------------------+
| The number of posts for a single batch    | - System Config path: N/A                                                 |
| during a bulk indexing job.               | - ``config.json`` setting: ``".Elasticsearchsettings.BatchSize :10000",`` |
|                                           | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_BATCHSIZE``            |
| Numerical input. Default is **10000**.    |                                                                           |
+-------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: elastic-requesttimeout
  :displayname: Request timeout (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.RequestTimeoutSeconds
  :environment: MM_ELASTICSEARCHSETTINGS_REQUESTTIMEOUTSECONDS
  :description: The timeout, in seconds, for Elasticsearch calls. Default is **30** seconds.

Request timeout
~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+------------------------------------------------------------------------------------+
| The timeout, in seconds, for Elasticsearch calls.             | - System Config path: N/A                                                          |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.RequestTimeoutSeconds :30",`` |
| Numerical input in seconds. Default is **30** seconds.        | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_REQUESTTIMEOUTSECONDS``         |
+---------------------------------------------------------------+------------------------------------------------------------------------------------+

.. config:setting:: elastic-trace
  :displayname: Trace (Elasticsearch)
  :systemconsole: N/A
  :configjson: .Elasticsearchsettings.Trace
  :environment: MM_ELASTICSEARCHSETTINGS_TRACE
  :description: Options for printing Elasticsearch trace errors.

  - **error**: Creates the error trace when initializing the Elasticsearch client and prints any template creation or search query that returns an error as part of the error message.
  - **all**: Creates the three traces (error, trace and info) for the driver and doesn’t print the queries because they will be part of the trace log level of the driver.
  - **not specified**: **(Default)** No error trace is created.

Trace
~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Options for printing Elasticsearch trace errors.              | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``".Elasticsearchsettings.Trace",``           |
| - **error**: Creates the error trace when initializing        | - Environment variable: ``MM_ELASTICSEARCHSETTINGS_TRACE``               |
|   the Elasticsearch client and prints any template creation   |                                                                          |
|   or search query that returns an error as part of the        |                                                                          |
|   error message.                                              |                                                                          |
| - **all**: Creates the three traces (error, trace and info)   |                                                                          |
|   for the driver and doesn’t print the queries because they   |                                                                          |
|   will be part of the trace log level of the driver.          |                                                                          |
| - **not specified**: **(Default)** No error trace is created. |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

----

File storage
------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Configure file storage settings by going to **System Console > Environment > File Storage**, or by editing the ``config.json`` file as described in the following tables.

.. include:: ../_static/badges/academy-file-storage.rst
  :start-after: :nosearch:

.. note::

  Mattermost currently supports storing files on the local filesystem and Amazon S3 or S3-compatible containers. We have tested Mattermost with `MinIO <https://min.io/>`__ and `Digital Ocean Spaces <https://docs.digitalocean.com/products/spaces/>`__ products, but not all S3-compatible containers on the market. If you are looking to use other S3-compatible containers, we recommend completing your own testing.

.. config:setting:: file-storagesystem
  :displayname: File storage system (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.DriverName
  :environment: MM_FILESETTINGS_DRIVERNAME
  :description: The type of file storage system used.

  - **local**: **(Default)** Files and images are stored in the specified local file directory.
  - **amazons3**: Files and images are stored on Amazon S3 based on the access key, bucket, and region fields provided.

File storage system
~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The type of file storage system used.                         | - System Config path: **Environment > File Storage**                     |
| Can be either Local File System or Amazon S3.                 | - ``config.json`` setting: ``".FileSettings.DriverName:  local”,``       |
|                                                               | - Environment variable: ``MM_FILESETTINGS_DRIVERNAME``                   |
| - **local**: **(Default)** Files and images are stored in     |                                                                          |
|   the specified local file directory.                         |                                                                          |
| - **amazons3**: Files and images are stored on Amazon S3      |                                                                          |
|   based on the access key, bucket, and region fields          |                                                                          |
|   provided. The driver is compatible with MinIO (Beta)        |                                                                          |
|   and Digital Ocean Spaces.                                   |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-localstoragedirectory
  :displayname: Local storage directory (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.Directory
  :environment: MM_FILESETTINGS_DIRECTORY
  :description: The local directory to which files are written when the **File storage system** is set to **local**. Default value is **./data/**.

Local storage directory
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The local directory to which files are written when the       | - System Config path: **Environment > File Storage**                     |
| **File storage system** is set to **local**.                  | - ``config.json`` setting: ``".FileSettings.Directory”,``                |
| Can be any directory writable by the user Mattermost is       | - Environment variable: ``MM_FILESETTINGS_DIRECTORY``                    |
| running as, and is relative to the directory where            |                                                                          |
| Mattermost is installed.                                      |                                                                          |
|                                                               |                                                                          |
| Defaults to **./data/**.                                      |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: When **File storage system** is set to **amazons3**, this setting has no effect.                                               |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-maxfilesize
  :displayname: Maximum file size (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.MaxFileSize
  :environment: MM_FILESETTINGS_MAXFILESIZE
  :description: The maximum file size, in bytes, for message attachments and plugin uploads. Default value is **104857600** bytes (100 mebibytes).

Maximum file size
~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-------------------------------------------------------------------+--------------------------------------------------------------------------+
| The maximum file size for message attachments and plugin          | - System Config path: **Environment > File Storage**                     |
| uploads. This value must be specified in mebibytes in the         | - ``config.json`` setting: ``".FileSettings.MaxFileSize: 104857600",``   |
| System Console, and in bytes in the ``config.json`` file.         | - Environment variable: ``MM_FILESETTINGS_MAXFILESIZE``                  |
|                                                                   |                                                                          |
| The default is ``104857600`` bytes (**100** mebibytes).           |                                                                          |
+-------------------------------------------------------------------+--------------------------------------------------------------------------+
| **Warning**: Verify server memory can support your setting choice. Large file sizes increase the risk of server crashes and failed           |
| uploads due to network disruptions.                                                                                                          |
+-------------------------------------------------------------------+--------------------------------------------------------------------------+
| **Notes**:                                                                                                                                   |
|                                                                                                                                              |
| - When :ref:`uploading plugin files <configure/plugins-configuration-settings:upload plugin>`, a ``Received invlaid response from            |
|   the server`` error typically indicates that ``MaxFileSize`` isn't large enough to support the plugin file upload, and/or that proxy        |
|   settings may not be sufficient.                                                                                                            |
| - If you use a proxy or load balancer in front of Mattermost, the following proxy settings must be adjusted accordingly:                     |
|                                                                                                                                              |
|  - For NGINX, use ``client_max_body_size``.                                                                                                  |
|  - For Apache use ``LimitRequestBody``.                                                                                                      |
+-------------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-enabledocsearchbycontent
  :displayname: Enable document search by content (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.ExtractContent
  :environment: MM_FILESETTINGS_EXTRACTCONTENT
  :description: Enable users to search the contents of documents attached to messages.

  - **true**: **(Default)** Documents are searchable by their content.
  - **false**: Documents aren’t searchable by their content.

Enable document search by content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------------------------------+
| Enable users to search the contents of documents attached     | - System Config path: **Environment > File Storage**                                |
| to messages.                                                  | - ``config.json`` setting: ``".FileSettings.ExtractContent: true",``                |
|                                                               | - Environment variable: ``MM_FILESETTINGS_EXTRACTCONTENT``                          |
| - **true**: **(Default)** Documents are searchable by         |                                                                                     |
|   their content.                                              |                                                                                     |
| - **false**: Documents aren’t searchable by their content.    |                                                                                     |
|   When document content search is disabled, users can search  |                                                                                     |
|   for files by file name only.                                |                                                                                     |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------+
| **Note**: Document content search results for files shared before upgrading to Mattermost Server v5.35 may be incomplete until an                   |
| extraction command is executed using the :ref:`mmctl <manage/mmctl-command-line-tool:mmctl extract>`.                                               |
| If this command is not run, users can search older files based on file name only.                                                                   |
|                                                                                                                                                     |
| You can optionally install the following `dependencies <https://github.com/sajari/docconv#dependencies>`__ to extend content searching support in   |
| Mattermost to include file formats beyond PDF, DOCX, and ODT, such as DOC, RTF, XML, and HTML:                                                      |
|                                                                                                                                                     |
| - **tidy**: Used to search the contents of HTML documents.                                                                                          |
| - **wv**: Used to search the contents of DOC documents.                                                                                             |
| - **popplerutils**: Used to significantly improve server performance when extracting the contents of PDF documents.                                 |
| - **unrtf**: Used to search the contents of RTF documents.                                                                                          |
| - **JusText**: Used to search HTML documents.                                                                                                       |
|                                                                                                                                                     |
| If you choose not to install these dependencies, you’ll see log entries for documents that couldn’t be extracted.                                   |
| Any documents that can’t be extracted are skipped and logged so that content extraction can proceed.                                                |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------+

.. config:setting:: file-enabledocsearchwithinzipfile
  :displayname: Enable searching content of documents within ZIP files (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.ArchiveRecursion
  :environment: MM_FILESETTINGS_ARCHIVERECURSION
  :description: Enables users to search the contents of compressed ZIP files attached to messages.

  - **true**: Contents of documents within ZIP files are returned in search results.
  - **false**: **(Default)** The contents of documents within ZIP files aren’t returned in search results.

Enable searching content of documents within ZIP files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Enables users to search the contents of compressed ZIP files  | - System Config path: **Environment > File Storage**                                   |
| attached to messages.                                         | - ``config.json`` setting: ``".FileSettings.ArchiveRecursion: false",``                |
|                                                               | - Environment variable: ``MM_FILESETTINGS_ARCHIVERECURSION``                           |
| - **true**: Contents of documents within ZIP files are        |                                                                                        |
|   returned in search results. This may have an impact on      |                                                                                        |
|   server performance for large files.                         |                                                                                        |
|   the specified local file directory.                         |                                                                                        |
| - **false**: **(Default)** The contents of documents within   |                                                                                        |
|   ZIP files aren’t returned in search results.                |                                                                                        |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------+
| **Note**: Document content search within ZIP files is available, with mobile support coming soon.                                                      |
| Searching document contents adds load to your server. For large deployments, or teams that share many large, text-heavy documents,                     |
| we recommend you review our :ref:`hardware requirements <install/software-hardware-requirements:hardware requirements>`,                               |
| and test enabling this feature in a staging environment before enabling it in a production environment.                                                |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------+

.. config:setting:: file-s3bucket
  :displayname: Amazon S3 bucket (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3Bucket
  :environment: MM_FILESETTINGS_AMAZONS3BUCKET
  :description: The name of the bucket for your S3-compatible object storage instance.

Amazon S3 bucket
~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The name of the bucket for your S3-compatible object          | - System Config path: **Environment > File Storage**                     |
| storage instance.                                             | - ``config.json`` setting: ``".FileSettings.AmazonS3Bucket",``           |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3BUCKET``               |
| A string with the S3-compatible bucket name.                  |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-s3pathprefix
  :displayname: Amazon S3 path prefix (File Storage)
  :systemconsole: N/A
  :configjson: .FileSettings.AmazonS3PathPrefix
  :environment: MM_FILESETTINGS_AMAZONS3PATHPREFIX
  :description: The prefix you selected for your **Amazon S3 bucket** in AWS.

Amazon S3 path prefix
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The prefix you selected for your **Amazon S3 bucket** in AWS. | - System Config path: N/A                                                |
|                                                               | - ``config.json`` setting: ``".FileSettings.AmazonS3PathPrefix",``       |
| A string containing the path prefix.                          | - Environment variable: ``MM_FILESETTINGS_AMAZONS3PATHPREFIX``           |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-s3region
  :displayname: Amazon S3 region (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3Region
  :environment: MM_FILESETTINGS_AMAZONS3REGION
  :description: The AWS region you selected when creating your **Amazon S3 bucket** in AWS. For MinIO or Digital Ocean Spaces, leave this setting empty.

Amazon S3 region
~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The AWS region you selected when creating your                | - System Config path: **Environment > File Storage**                     |
| **Amazon S3 bucket** in AWS.                                  | - ``config.json`` setting: ```".FileSettings.AmazonS3Region",``          |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3REGION``               |
| A string with the AWS region containing the bucket.           |                                                                          |
| If no region is set, Mattermost attempts to get the           |                                                                          |
| appropriate region from AWS, and sets it to **us-east-1**     |                                                                          |
| if none found.                                                |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: For MinIO or Digital Ocean Spaces, leave this setting empty.                                                                   |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-s3accesskeyid
  :displayname: Amazon S3 access key ID (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3AccessKeyId
  :environment: MM_FILESETTINGS_AMAZONS3ACCESSKEYID
  :description: A string with the access key for the S3-compatible storage instance.

Amazon S3 access key ID
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| A string with the access key for the S3-compatible storage    | - System Config path: **Environment > File Storage**                     |
| instance. Your EC2 administrator can supply you with the      | - ``config.json`` setting: ``".FileSettings.AmazonS3AccessKeyId",``      |
| Access Key ID.                                                | - Environment variable: ``MM_FILESETTINGS_AMAZONS3ACCESSKEYID``          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| **Note**: This is required for access unless you are using an                                                                            |
| `Amazon S3 IAM Role <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html>`__ with       |
| Amazon S3.                                                                                                                               |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-s3endpoint
  :displayname: Amazon S3 endpoint (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3Endpoint
  :environment: MM_FILESETTINGS_AMAZONS3ENDPOINT
  :description: The hostname of your S3-compatible instance. Default value is **s3.amazonaws.com**.

Amazon S3 endpoint
~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+------------------------------------------------------------------------------------+
| The hostname of your S3-compatible instance.                  | - System Config path: **Environment > File Storage**                               |
|                                                               | - ``config.json`` setting: ``".FileSettings.AmazonS3Endpoint: s3.amazonaws.com",`` |
| A string with the hostname of the S3-compatible storage       | - Environment variable: ``MM_FILESETTINGS_AMAZONS3ENDPOINT``                       |
| instance. Defaults to **s3.amazonaws.com**.                   |                                                                                    |
+---------------------------------------------------------------+------------------------------------------------------------------------------------+
| **Note**: For Digital Ocean Spaces, the hostname should be set to **<region>.digitaloceanspaces.com**, where **<region>** is the abbreviation      |
| for the region you selected when setting up the Space. It can be **nyc3**, **ams3**, or **sgp1**.                                                  |
+---------------------------------------------------------------+------------------------------------------------------------------------------------+

.. config:setting:: file-s3secretaccesskey
  :displayname: Amazon S3 secret access key (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3SecretAccessKey
  :environment: MM_FILESETTINGS_AMAZONS3SECRETACCESSKEY
  :description: The secret access key associated with your Amazon S3 Access Key ID.

Amazon S3 secret access key
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| The secret access key associated with your Amazon S3          | - System Config path: **Environment > File Storage**                     |
| Access Key ID.                                                | - ``config.json`` setting: ``".FileSettings.AmazonS3SecretAccessKey",``  |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3SECRETACCESSKEY``      |
| A string with the secret access key for the S3-compatible     |                                                                          |
| storage instance.                                             |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-s3secureconnection
  :displayname: Enable secure Amazon S3 connections (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3SSL
  :environment: MM_FILESETTINGS_AMAZONS3SSL
  :description: Enable or disable secure Amazon S3 connections. Default value is **true**.

Enable secure Amazon S3 connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Enable or disable secure Amazon S3 connections.               | - System Config path: **Environment > File Storage**                     |
|                                                               | - ``config.json`` setting: ``".FileSettings.AmazonS3SSL: true",``        |
| - **true**: **(Default)** Enables only secure Amazon          | - Environment variable: ``MM_FILESETTINGS_AMAZONS3SSL``                  |
|   S3 connections.                                             |                                                                          |
| - **false**: Allows insecure connections to Amazon S3.        |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-s3signv2
  :displayname: Amazon S3 signature v2 (File Storage)
  :systemconsole: N/A
  :configjson: .FileSettings.AmazonS3SignV2
  :environment: MM_FILESETTINGS_AMAZONS3SIGNV2

  - **true**: Use Signature v2 signing process.
  - **false**: **(Default)** Use Signature v4 signing process.

Amazon S3 signature v2
~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Not available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| By default, Mattermost uses Signature v4 to sign API calls    | - System Config path: N/A                                                |
| to AWS, but under some circumstances, v2 is required.         | - ``config.json`` setting: ``".FileSettings.AmazonS3SignV2: false",``    |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3SIGNV2``               |
| - **true**: Use Signature v2 signing process.                 |                                                                          |
| - **false**: **(Default)** Use Signature v4 signing process.  |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| See the `AWS <https://docs.aws.amazon.com/general/latest/gr/signature-version-2.html>`__ documentation for information about when to     |
| use the Signature v2 signing process.                                                                                                    |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-s3sse
  :displayname: Enable server-side encryption for Amazon S3 (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3SSE
  :environment: MM_FILESETTINGS_AMAZONS3SSE

  - **true**: Encrypts files in Amazon S3 using server-side encryption with Amazon S3-managed keys.
  - **false**: **(Default)** Doesn’t encrypt files in Amazon S3.

Enable server-side encryption for Amazon S3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Enable server-side encryption for Amazon S3.                  | - System Config path: **Environment > File Storage**                     |
|                                                               | - ``config.json`` setting: ``".FileSettings.AmazonS3SSE: false",``       |
| - **true**: Encrypts files in Amazon S3 using server-side     | - Environment variable: ``MM_FILESETTINGS_AMAZONS3SSE``                  |
|   encryption with Amazon S3-managed keys.                     |                                                                          |
| - **false**: **(Default)** Doesn’t encrypt files in           |                                                                          |
|   Amazon S3.                                                  |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-s3trace
  :displayname: Enable Amazon S3 debugging (File Storage)
  :systemconsole: Environment > File Storage
  :configjson: .FileSettings.AmazonS3Trace
  :environment: MM_FILESETTINGS_AMAZONS3TRACE

  - **true**: Log additional debugging information is logged to the system logs.
  - **false**: **(Default)** No Amazon S3 debugging information is included in the system logs.

Enable Amazon S3 debugging
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Enable or disable Amazon S3 debugging to capture additional   | - System Config path: **Environment > File Storage**                     |
| debugging information in system logs                          | - ``config.json`` setting: ``".FileSettings.AmazonS3Trace: false",``     |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3TRACE``                |
| - **true**: Log additional debugging information is logged    |                                                                          |
|   to the system logs.                                         |                                                                          |
| - **false**: **(Default)** No Amazon S3 debugging information |                                                                          |
|   is included in the system logs. Typically set to **false**  |                                                                          |
|   in production.                                              |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Select the **Test Connection** button in the System Console to validate the settings and ensure the user can access the server.          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: file-amazons3requesttimeoutmilliseconds
  :displayname: Amazon S3 request timeout (File Storage)
  :systemconsole: N/A
  :configjson: .FileSettings.AmazonS3RequestTimeoutMilliseconds
  :environment: MM_FILESETTINGS_AMAZONS3REQUESTTIMEOUTMILLISECONDS
  :description: Amount of time, in milliseconds, before requests to Amazon S3 time out. Default value is 30000 (30 seconds).

Amazon S3 request timeout 
~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| The amount of time, in milliseconds, before requests to       | - System Config path: N/A                                                               |
| Amazon S3 storage time out.                                   | - ``config.json`` setting: ``".FileSettings.AmazonS3RequestTimeoutMilliseconds: 30000`` |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3REQUESTTIMEOUTMILLISECONDS``          |
| Default is 30000 (30 seconds).                                |                                                                                         |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. config:setting:: file-amazons3uploadpartsizebytes
  :displayname: Amazon S3 upload part size (File Storage)
  :systemconsole: N/A
  :configjson: .FileSettings.AmazonS3UploadPartSizeBytes
  :environment: MM_FILESETTINGS_AMAZONS3UPLOADPARTSIZEBYTES
  :description: The size, in bytes, of each part in a multi-part upload to Amazon S3. Default value is 5242880 (5MB).

Amazon S3 upload part size
~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------------------------------+
| The size, in bytes, of each part in a multi-part              | - System Config path: N/A                                                             |
| upload to Amazon S3.                                          | - ``config.json`` setting: ``".FileSettings.AmazonS3UploadPartSizeBytes: 5242880``    |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3UPLOADPARTSIZEBYTES``               |
| Numeric value. Default is 5242880 (5MB).                      |                                                                                       |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------+
| **Note**: A smaller part size can result in more requests and an increase in latency, while a larger part size can result in more memory              |
| being allocated.                                                                                                                                      |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------+

.. config:setting:: file-exportamazons3uploadpartsizebytes
  :displayname: Export Amazon S3 upload part size (File Storage)
  :systemconsole: N/A
  :configjson: .FileSettings.ExportAmazonS3UploadPartSizeBytes
  :environment: MM_FILESETTINGS_EXPORTAMAZONS3UPLOADPARTSIZEBYTES
  :description: The size, in bytes, of each part in a multi-part exported to Amazon S3. Default value is 104857600 (100MB).

Amazon S3 exported upload part size
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| The size, in bytes, of each part in a multi-part              | - System Config path: N/A                                                                  |
| exported to Amazon S3.                                        | - ``config.json`` setting: ``".FileSettings.ExportAmazonS3UploadPartSizeBytes: 104857600`` |
|                                                               | - Environment variable: ``MM_FILESETTINGS_EXPORTAMAZONS3UPLOADPARTSIZEBYTES``              |
| Numeric value. Default is 104857600 (100MB).                  |                                                                                            |
+---------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| **Note**: A smaller part size can result in more requests and an increase in latency, while a larger part size can result in more memory being allocated.  |
+---------------------------------------------------------------+--------------------------------------------------------------------------------------------+

.. config:setting:: file-initialfont
  :displayname: Initial font (File Storage)
  :systemconsole: N/A
  :configjson: .FileSettings.InitialFont
  :environment: MM_FILESETTINGS_INITIALFONT
  :description: The font used in auto-generated profile pictures with colored backgrounds and username initials. Default value is **nunito-bold.ttf**.

Initial font
~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+--------------------------------------------------------------------------------+
| The font used in auto-generated profile pictures with colored | - System Config path: N/A                                                      |
| backgrounds and username initials.                            | - ``config.json`` setting: ``".FileSettings.InitialFont: nunito-bold.ttf",``   |
|                                                               | - Environment variable: ``MM_FILESETTINGS_INITIALFONT``                        |
| A string with the font file name. Default is                  |                                                                                |
| **nunito-bold.ttf**.                                          |                                                                                |
+---------------------------------------------------------------+--------------------------------------------------------------------------------+

.. config:setting:: file-amazons3requesttimeoutmilliseconds
  :displayname: Amazon S3 request timeout (File Storage)
  :systemconsole: N/A
  :configjson: .FileSettings.AmazonS3RequestTimeoutMilliseconds
  :environment: MM_FILESETTINGS_AMAZONS3REQUESTTIMEOUTMILLISECONDS
  :description: Amount of time, in milliseconds, before requests to Amazon S3 time out. Default value is 30000 (30 seconds).

Amazon S3 request timeout 
~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| The amount of time, in milliseconds, before requests to       | - System Config path: N/A                                                               |
| Amazon S3 storage time out.                                   | - ``config.json`` setting: ``".FileSettings.AmazonS3RequestTimeoutMilliseconds: 30000`` |
|                                                               | - Environment variable: ``MM_FILESETTINGS_AMAZONS3REQUESTTIMEOUTMILLISECONDS``          |
| Default is 30000 (30 seconds).                                |                                                                                         |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------+

----

Image proxy
-----------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

An image proxy is used by Mattermost apps to prevent them from connecting directly to remote self-hosted servers. Configure an image proxy by going to **System Console > Environment > Image Proxy**, or by editing the ``config.json`` file as described in the following tables.

.. config:setting:: image-enableproxy
  :displayname: Enable image proxy (Image Proxy)
  :systemconsole: Environment > Image Proxy
  :configjson: .ImageProxySettings.Enable
  :environment: MM_IMAGEPROXYSETTINGS_ENABLE

  - **true**: **(Default)** Enables an image proxy for loading external images.
  - **false**: Disables the image proxy.

Enable image proxy
~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+---------------------------------------------------------------------+
| An image proxy anonymizes Mattermost app connections and      | - System Config path: **Environment > Image Proxy**                 |
| prevents them from accessing insecure content.                | - ``config.json setting``: ``".ImageProxySettings.Enable": true",`` |
|                                                               | - Environment variable: ``MM_IMAGEPROXYSETTINGS_ENABLE``            |
| - **true**: **(Default)** Enables an image proxy for loading  |                                                                     |
|   external images.                                            |                                                                     |
| - **false**: Disables the image proxy.                        |                                                                     |
+---------------------------------------------------------------+---------------------------------------------------------------------+
| See the :doc:`image proxy </deploy/image-proxy>` documentation to learn more.                                                       |
+---------------------------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: image-proxytype
  :displayname: Image proxy type (Image Proxy)
  :systemconsole: Environment > Image Proxy
  :configjson: .ImageProxySettings.ImageProxyType
  :environment: MM_IMAGEPROXYSETTINGS_IMAGEPROXYTYPE
  :description: The type of image proxy used by Mattermost.

  - **local**: **(Default)** The Mattermost server itself acts as the image proxy.
  - **atmos/camo**: An external atmos/camo image proxy is used.

Image proxy type
~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The type of image proxy used by Mattermost.                   | - System Config path: **Environment > Image Proxy**                           |
|                                                               | - ``config.json setting``: ``".ImageProxySettings.ImageProxyType": "local",`` |
| - **local**: **(Default)** The Mattermost server itself acts  | - Environment variable: ``MM_IMAGEPROXYSETTINGS_IMAGEPROXYTYPE``              |
|   as the image proxy.                                         |                                                                               |
| - **atmos/camo**: An external atmos/camo image proxy is used. |                                                                               |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| See the :doc:`image proxy </deploy/image-proxy>` documentation to learn more.                                                                 |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

.. config:setting:: image-remoteimageproxyurl
  :displayname: Remote image proxy URL (Image Proxy)
  :systemconsole: Environment > Image Proxy
  :configjson: .ImageProxySettings.RemoteImageProxyURL
  :environment: MM_IMAGEPROXYSETTINGS_REMOTEIMAGEPROXYURL
  :description: The URL of the atmos/camo proxy.

Remote image proxy URL
~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+---------------------------------------------------------------------------+
| The URL of the atmos/camo proxy. This setting isn't needed    | - System Config path: **Environment > Image Proxy**                       |
| when using the **local** image proxy.                         | - ``config.json setting``: ``".ImageProxySettings.RemoteImageProxyURL",`` |
|                                                               | - Environment variable: ``MM_IMAGEPROXYSETTINGS_REMOTEIMAGEPROXYURL``     |
+---------------------------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: image-remoteimageproxyoptions
  :displayname: Remote image proxy options (Image Proxy)
  :systemconsole: Environment > Image Proxy
  :configjson: .ImageProxySettings.RemoteImageProxyOptions
  :environment: MM_IMAGEPROXYSETTINGS_REMOTEIMAGEPROXYOPTIONS
  :description: The URL signing key passed to an atmos/camo image proxy.

Remote image proxy options
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| The URL signing key passed to an atmos/camo image proxy.      | - System Config path: **Environment > Image Proxy**                           |
| This setting isn't needed when using the **local** image      | - ``config.json setting``: ``".ImageProxySettings.RemoteImageProxyOptions",`` |
| proxy type.                                                   | - Environment variable: ``MM_IMAGEPROXYSETTINGS_REMOTEIMAGEPROXYOPTIONS``     |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| See the :doc:`image proxy </deploy/image-proxy>` documentation to learn more.                                                                 |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

----

SMTP
----

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Configure SMTP email server settings by going to **System Console > Environment > SMTP**, or by editing the ``config.json`` file as described in the following tables.

.. config:setting:: smtp-server
  :displayname: SMTP server (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SMTPServer
  :environment: MM_EMAILSETTINGS_SMTPSERVER
  :description: The location of the SMTP email server used for email notifications.

SMTP server
~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+---------------------------------------------------------------+
| The location of the SMTP email server used for email            | - System Config path: **Environment > SMTP**                  |
| notifications.                                                  | - ``config.json setting``: ``".EmailSettings.SMTPServer",``   |
|                                                                 | - Environment variable: ``MM_EMAILSETTINGS_SMTPSERVER``       |
+-----------------------------------------------------------------+---------------------------------------------------------------+

.. config:setting:: smtp-port
  :displayname: SMTP server port (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SMTPPort
  :environment: MM_EMAILSETTINGS_SMTPPORT
  :description: The port of SMTP email server.

SMTP server port
~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+---------------------------------------------------------------+
| The port of SMTP email server.                                  | - System Config path: **Environment > SMTP**                  |
|                                                                 | - ``config.json setting``: ``".EmailSettings.SMTPPort",``     |
| Numerical input.                                                | - Environment variable: ``MM_EMAILSETTINGS_SMTPPORT``         |
+-----------------------------------------------------------------+---------------------------------------------------------------+

.. config:setting:: smtp-enableauth
  :displayname: Enable SMTP authentication (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.EnableSMTPAuth
  :environment: MM_EMAILSETTINGS_ENABLESMTPAUTH

  - **true**: SMTP username and password are used for authenticating to the SMTP server.
  - **false**: **(Default)** Mattermost doesn’t attempt to authenticate to the SMTP server.

Enable SMTP authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+---------------------------------------------------------------------------+
| Enable or disable SMTP authentication.                          | - System Config path: **Environment > SMTP**                              |
|                                                                 | - ``config.json setting``: ``".EmailSettings.EnableSMTPAuth": false",``   |
| - **true**: SMTP username and password are used for             | - Environment variable: ``MM_EMAILSETTINGS_ENABLESMTPAUTH``               |
|   authenticating to the SMTP server.                            |                                                                           |
| - **false**: **(Default)** Mattermost doesn’t attempt to        |                                                                           |
|   authenticate to the SMTP server.                              |                                                                           |
+-----------------------------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: smtp-username
  :displayname: SMTP server username (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SMTPUsername
  :environment: MM_EMAILSETTINGS_SMTPUSERNAME
  :description: The username for authenticating to the SMTP server.

SMTP server username
~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+---------------------------------------------------------------+
| The username for authenticating to the SMTP server.             | - System Config path: **Environment > SMTP**                  |
|                                                                 | - ``config.json setting``: ``".EmailSettings.SMTPUsername",`` |
| String input.                                                   | - Environment variable: ``MM_EMAILSETTINGS_SMTPUSERNAME``     |
+-----------------------------------------------------------------+---------------------------------------------------------------+

.. config:setting:: smtp-password
  :displayname: SMTP server password (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SMTPPassword
  :environment: MM_EMAILSETTINGS_SMTPPASSWORD
  :description: The password associated with the SMTP username.

SMTP server password
~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+---------------------------------------------------------------+
| The password associated with the SMTP username.                 | - System Config path: **Environment > SMTP**                  |
|                                                                 | - ``config.json setting``: ``".EmailSettings.SMTPPassword",`` |
| String input.                                                   | - Environment variable: ``MM_EMAILSETTINGS_SMTPPASSWORD``     |
+-----------------------------------------------------------------+---------------------------------------------------------------+

.. config:setting:: smtp-connectionsecurity
  :displayname: SMTP connection security (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.ConnectionSecurity
  :environment: MM_EMAILSETTINGS_CONNECTIONSECURITY

  - **Not specified**: **(Default)** Send email over an unsecure connection.
  - **TLS**: Communication between Mattermost and your email server is encrypted.
  - **STARTTLS**: Attempts to upgrade an existing insecure connection to a secure connection using TLS.

SMTP connection security
~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+-----------------------------------------------------------------------+
| Specify connection security for emails sent using SMTP.         | - System Config path: **Environment > SMTP**                          |
|                                                                 | - ``config.json setting``: ``".EmailSettings.ConnectionSecurity",``   |
| - **Not specified**: **(Default)** Send email over an           | - Environment variable: ``MM_EMAILSETTINGS_CONNECTIONSECURITY``       |
|   unsecure connection.                                          |                                                                       |
| - **TLS**: Communication between Mattermost and your email      |                                                                       |
|   server is encrypted.                                          |                                                                       |
| - **STARTTLS**: Attempts to upgrade an existing insecure        |                                                                       |
|   connection to a secure connection using TLS.                  |                                                                       |
+-----------------------------------------------------------------+-----------------------------------------------------------------------+

.. config:setting:: smtp-skipservercertverification
  :displayname: Skip server certificate verification (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SkipServerCertificateVerification
  :environment: MM_EMAILSETTINGS_SKIPSERVERCERTIFICATEVERIFICATION

  - **true**: Mattermost won't verify the email server certificate.
  - **false**: **(Default)** Mattermost verifies the email server certificate.

Skip server certificate verification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Configure Mattermost to skip the verification of the email server     | - System Config path: **Environment > SMTP**                                                 |
| certificate.                                                          | - ``config.json setting``: ``".EmailSettings.SkipServerCertificateVerification": false",``   |
|                                                                       | - Environment variable: ``MM_EMAILSETTINGS_SKIPSERVERCERTIFICATEVERIFICATION``               |
| - **true**: Mattermost won't verify the email server certificate.     |                                                                                              |
| - **false**: **(Default)** Mattermost verifies the email              |                                                                                              |
|   server certificate.                                                 |                                                                                              |
+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------+

.. config:setting:: smtp-enablesecurityalerts
  :displayname: Enable security alerts (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .ServiceSettings.EnableSecurityFixAlert
  :environment: MM_SERVICESETTINGS_ENABLESECURITYFIXALERT

  - **true**: **(Default)** System admins are notified by email if a relevant security fix alert is announced. Requires email to be enabled.
  - **false**: Security alerts are disabled.

Enable security alerts
~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| Enable or disable security alerts.                              | - System Config path: **Environment > SMTP**                                       |
|                                                                 | - ``config.json setting``: ``".ServiceSettings.EnableSecurityFixAlert": true",``   |
| - **true**: **(Default)** System admins are notified by email   | - Environment variable: ``MM_SERVICESETTINGS_ENABLESECURITYFIXALERT``              |
|   if a relevant security fix alert is announced. Requires email |                                                                                    |
|   to be enabled.                                                |                                                                                    |
| - **false**: Security alerts are disabled.                      |                                                                                    |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+
| See the :ref:`Telemetry <manage/telemetry:security update check feature>` documentation to learn more.                                               |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+

.. config:setting:: smtp-servertimeout
  :displayname: SMTP server timeout (SMTP)
  :systemconsole: Environment > SMTP
  :configjson: .EmailSettings.SMTPServerTimeout
  :environment: MM_EMAILSETTINGS_SMTPSERVERTIMEOUT
  :description: The maximum amount of time, in seconds, allowed for establishing a TCP connection between Mattermost and the SMTP server.

SMTP server timeout
~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------------------------+----------------------------------------------------------------------+
| The maximum amount of time, in seconds, allowed for             | - System Config path: **Environment > SMTP**                         |
| establishing a TCP connection between Mattermost and the SMTP   | - ``config.json setting``: ``".EmailSettings.SMTPServerTimeout",``   |
| server.                                                         | - Environment variable: ``MM_EMAILSETTINGS_SMTPSERVERTIMEOUT``       |
|                                                                 |                                                                      |
| Numerical value in seconds.                                     |                                                                      |
+-----------------------------------------------------------------+----------------------------------------------------------------------+

----

Push notification server
------------------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: push-notification-server-configuration-settings.rst
    :start-after: :nosearch:

----

High availability
-----------------

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

You can configure Mattermost as a :doc:`high availability cluster-based deployment </scale/high-availability-cluster-based-deployment>` by going to **System Console > Environment > High Availability**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

In a Mattermost high availability cluster-based deployment, the System Console is set to read-only, and settings can only be changed by editing the ``config.json`` file directly. However, to test a high availability cluster-based environment, you can disable ``ClusterSettings.ReadOnlyConfig`` in the ``config.json`` file by setting it to ``false``. This allows changes applied using the System Console to be saved back to the configuration file.

.. config:setting:: ha-enable
  :displayname: Enable high availability mode (High Availability)
  :systemconsole: Environment > High Availability
  :configjson: .ClusterSettings.Enable
  :environment: MM_CLUSTERSETTINGS_ENABLE

  - **true**: The Mattermost server will attempt inter-node communication with the other servers in the cluster that have the same cluster name.
  - **false**: **(Default)** Mattermost high availability mode is disabled.

Enable high availability mode
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+-----------------------------------------------------------------+------------------------------------------------------------+
| You can enable high availability mode.                          | - System Config path: **Environment > High Availability**  |
|                                                                 | - ``config.json`` setting: ``".ClusterSettings.Enable",``  |
| - **true**: The Mattermost server will attempt inter-node       | - Environment variable: ``MM_CLUSTERSETTINGS_ENABLE``      |
|   communication with the other servers in the cluster that      |                                                            |
|   have the same cluster name. This sets the System Console to   |                                                            |
|   read-only mode to keep the servers' ``config.json`` files     |                                                            |
|   in sync.                                                      |                                                            |
| - **false**: **(Default)** Mattermost high availability mode    |                                                            |
|   is disabled.                                                  |                                                            |
+-----------------------------------------------------------------+------------------------------------------------------------+

.. config:setting:: ha-clustername
  :displayname: Cluster name (High Availability)
  :systemconsole: Environment > High Availability
  :configjson: .ClusterSettings.ClusterName
  :environment: MM_CLUSTERSETTINGS_CLUSTERNAME
  :description: The cluster to join by name in a high availability cluster-based deployment.

Cluster name
~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+------------------------------------------------------------------------------+-----------------------------------------------------------------+
| The cluster to join by name in a high availability cluster-based deployment. | - System Config path: **Environment > High Availability**       |
|                                                                              | - ``config.json`` setting: ``".ClusterSettings.ClusterName",``  |
| Only nodes with the same cluster name will join together.                    | - Environment variable: ``MM_CLUSTERSETTINGS_CLUSTERNAME``      |
| This is to support blue-green deployments or staging pointing                |                                                                 |
| to the same database.                                                        |                                                                 |
+------------------------------------------------------------------------------+-----------------------------------------------------------------+

.. config:setting:: ha-overridehostname
  :displayname: Override hostname (High Availability)
  :systemconsole: Environment > High Availability
  :configjson: .ClusterSettings.OverrideHostname
  :environment: MM_CLUSTERSETTINGS_OVERRIDEHOSTNAME
  :description: Override the hostname of this server.

Override hostname
~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+-----------------------------------------------------------------+------------------------------------------------------------------------+
| You can override the hostname of this server.                   | - System Config path: **Environment > High Availability**              |
|                                                                 | - ``config.json`` setting: ``".ClusterSettings.OverrideHostname",``    |
| - This property can be set to a specific IP address if needed;  | - Environment variable: ``MM_CLUSTERSETTINGS_OVERRIDEHOSTNAME``        |
|   however, we don’t recommend overriding the hostname unless    |                                                                        |
|   it's necessary.                                               |                                                                        |
| - If left blank, Mattermost attempts to get the hostname from   |                                                                        |
|   the operating system or uses the IP address.                  |                                                                        |
+-----------------------------------------------------------------+------------------------------------------------------------------------+
| See the :doc:`high availability cluster-based deployment </scale/high-availability-cluster-based-deployment>` documentation for details. |
+-----------------------------------------------------------------+------------------------------------------------------------------------+

.. config:setting:: ha-useipaddress
  :displayname: Use IP address (High Availability)
  :systemconsole: Environment > High Availability
  :configjson: .ClusterSettings.UseIPAddress
  :environment: MM_CLUSTERSETTINGS_USEIPADDRESS

  - **true**: **(Default)** The cluster attempts to communicate using the IP address specified.
  - **false**: The cluster attempts to communicate using the hostname.

Use IP address
~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+------------------------------------------------------------------------------+------------------------------------------------------------------------+
| You can configure your high availability cluster-based deployment to         | - System Config path: **Environment > High Availability**              |
| communicate using the hostname instead of the IP address.                    | - ``config.json`` setting: ``".ClusterSettings.UseIPAddress: true",``  |
|                                                                              | - Environment variable: ``MM_CLUSTERSETTINGS_USEIPADDRESS``            |
| - **true**: **(Default)** The cluster attempts to communicate                |                                                                        |
|   using the IP address specified.                                            |                                                                        |
| - **false**: The cluster attempts to communicate using the                   |                                                                        |
|   hostname.                                                                  |                                                                        |
+------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. config:setting:: ha-usegossip
  :displayname: Use gossip (High Availability)
  :systemconsole: Environment > High Availability
  :configjson: .ClusterSettings.UseExperimentalGossip
  :environment: MM_CLUSTERSETTINGS_USEEXPERIMENTALGOSSIP

  - **true**: **(Default)** The server attempts to communicate via the gossip protocol over the gossip port specified.
  - **false**: The server attempts to communicate over the streaming port.

Enable experimental gossip encryption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+-----------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Gossip encryption uses AES-256 by default, and this value isn’t | - System Config path: **Environment > High Availability**                                    |
| configurable by design.                                         | - ``config.json`` setting: ``".ClusterSettings.EnableExperimentalGossipEncryption: false”,`` |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_ENABLEEXPERIMENTALGOSSIPENCRYPTION``            |
| - **true**: **(Default for Cloud deployments)**                 |                                                                                              |
|   All communication through the cluster using the gossip        |                                                                                              |
|   protocol will be encrypted.                                   |                                                                                              |
| - **false**: **(Default for self-hosted deployments)**          |                                                                                              |
|   All communication using gossip protocol remains unchanged.    |                                                                                              |
|   protocol remains unencrypted.                                 |                                                                                              |
+-----------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| **Note**: Alternatively, you can manually set the ``ClusterEncryptionKey`` row value in the **Systems** table. A key is a byte array converted to base64.      |
| Set this value to either 16, 24, or 32 bytes to select AES-128, AES-192, or AES-256 respectively.                                                              |
+-----------------------------------------------------------------+----------------------------------------------------------------------------------------------+

.. config:setting:: ha-gossipcompression
  :displayname: Enable gossip compression (High Availability)
  :systemconsole: Environment > High Availability
  :configjson: .ClusterSettings.EnableGossipCompression
  :environment: MM_CLUSTERSETTINGS_ENABLEGOSSIPCOMPRESSION

  - **true**: **(Default)** All communication through the cluster uses gossip compression.
  - **false**: All communication using the gossip protocol remains uncompressed.

Enable gossip compression
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+-----------------------------------------------------------------+----------------------------------------------------------------------------------+
| We recommend that you disable this configuration                | - System Config path: **Environment > High Availability**                        |
| setting for better performance.                                 | - ``config.json`` setting: ``".ClusterSettings.EnableGossipCompression: true”,`` |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_ENABLEGOSSIPCOMPRESSION``           |
| - **true**: **(Default for self-hosted deployments)**           |                                                                                  |
|   All communication through the cluster uses gossip             |                                                                                  |
|   compression. This setting is enabled by default to maintain   |                                                                                  |
|   compatibility with older servers.                             |                                                                                  |
| - **false**: **(Default for Cloud deployments)**                |                                                                                  |
|   All communication using the gossip protocol remains           |                                                                                  |
|   uncompressed.                                                 |                                                                                  |
|                                                                 |                                                                                  |
+-----------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: ha-gossipport
  :displayname: Gossip port (High Availability)
  :systemconsole: Environment > High Availability
  :configjson: .ClusterSettings.GossipPort
  :environment: MM_CLUSTERSETTINGS_GOSSIPPORT
  :description: The port used for the gossip protocol. Both UDP and TCP should be allowed on this port. Default value is **8074**.

Gossip port
~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+-----------------------------------------------------------------+---------------------------------------------------------------------+
| The port used for the gossip protocol. Both UDP and TCP         | - System Config path: **Environment > High Availability**           |
| should be allowed on this port.                                 | - ``config.json`` setting: ``".ClusterSettings.GossipPort: 8074”,`` |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_GOSSIPPORT``           |
| Numerical input. Default is **8074**.                           |                                                                     |
+-----------------------------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: ha-readonlyconfig
  :displayname: Read only config (High Availability)
  :systemconsole: N/A
  :configjson: .ClusterSettings.ReadOnlyConfig
  :environment: MM_CLUSTERSETTINGS_READONLYCONFIG
  :description: Configure whether changes made in the System Console are written to config.json or ignored. Default is ignored.

Read only config
~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+-----------------------------------------------------------------+------------------------------------------------------------------------+
| - **true**: **(Default)** Changes made to settings in the       | - System Config path: N/A                                              |
|   System Console are ignored.                                   | - ``config.json`` setting: ``".ClusterSettings.ReadOnlyConfig: true,`` |
| - **false**: Changes made to settings in the System Console     | - Environment variable: ``MM_CLUSTERSETTINGS_READONLYCONFIG``          |
|   are written to ``config.json``.                               |                                                                        |
+-----------------------------------------------------------------+------------------------------------------------------------------------+

.. config:setting:: ha-networkinterface
  :displayname: Network interface (High Availability)
  :systemconsole: N/A
  :configjson: .ClusterSettings.NetworkInterface
  :environment: MM_CLUSTERSETTINGS_NETWORKINTERFACE
  :description: An IP address used to identify the device that does automatic IP detection in high availability cluster-based deployments.

Network interface
~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+-----------------------------------------------------------------+------------------------------------------------------------------------+
| An IP address used to identify the device that does automatic   | - System Config path: N/A                                              |
| IP detection in high availability cluster-based deployments.    | - ``config.json`` setting: ``".ClusterSettings.NetworkInterface: "",`` |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_NETWORKINTERFACE``        |
| String input.                                                   |                                                                        |
+-----------------------------------------------------------------+------------------------------------------------------------------------+

.. config:setting:: ha-bindaddress
  :displayname: Bind address (High Availability)
  :systemconsole: N/A
  :configjson: .ClusterSettings.BindAddress
  :environment: MM_CLUSTERSETTINGS_BINDADDRESS
  :description: An IP address used to bind cluster traffic to a specific network device.

Bind address
~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+-----------------------------------------------------------------+--------------------------------------------------------------------+
| An IP address used to bind cluster traffic to a specific        | - System Config path: N/A                                          |
| network device.                                                 | - ``config.json`` setting: ``".ClusterSettings.BindAddress: "",``  |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_BINDADDRESS``         |
| This setting is used primarily for servers with multiple        |                                                                    |
| network devices or different Bind Address and Advertise Address |                                                                    |
| like in deployments that involve NAT (Network Address           |                                                                    |
| Translation).                                                   |                                                                    |
|                                                                 |                                                                    |
| String input.                                                   |                                                                    |
+-----------------------------------------------------------------+--------------------------------------------------------------------+

.. config:setting:: ha-advertiseaddress
  :displayname: Advertise address (High Availability)
  :systemconsole: N/A
  :configjson: .ClusterSettings.AdvertiseAddress
  :environment: MM_CLUSTERSETTINGS_ADVERTISEADDRESS
  :description: The IP address used to access the server from other nodes.

Advertise address
~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+-----------------------------------------------------------------+------------------------------------------------------------------------+
| The IP address used to access the server from other nodes.      | - System Config path: N/A                                              |
| This settings is used primary when cluster nodes are not in     | - ``config.json`` setting: ``".ClusterSettings.AdvertiseAddress: "",`` |
| the same network and involve NAT (Network Address Translation). | - Environment variable: ``MM_CLUSTERSETTINGS_ADVERTISEADDRESS``        |
|                                                                 |                                                                        |
| String input.                                                   |                                                                        |
+-----------------------------------------------------------------+------------------------------------------------------------------------+

----

Rate limiting
-------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

.. include:: rate-limiting-configuration-settings.rst
    :start-after: :nosearch:

----

Logging
--------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Configure logging by going to **System Console > Environment > Logging**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. tip:: 
  
  You can manage additional logging configuration within the ``config.json`` file specifically for Mattermost notifications under ``NotificationLogSettings``. These settings are equivalent to the configuration settings available under ``LogSettings``.

.. config:setting:: log-enableconsole
  :displayname: Output logs to console (Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.EnableConsole
  :environment: MM_LOGSETTINGS_ENABLECONSOLE

  - **true**: **(Default)** Output log messages are written to the console based on the `console log level <#console-log-level>`__ configuration.
  - **false**: Output log messages aren’t written to the console.

Output logs to console
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------+---------------------------------------------------------------------+
| Configure Mattermost to output logs to the    | - System Config path: **Environment > Logging**                     |
| console.                                      | - ``config.json setting``: ``".LogSettings.EnableConsole": true",`` |
|                                               | - Environment variable: ``MM_LOGSETTINGS_ENABLECONSOLE``            |
| - **true**: **(Default)** Output log messages |                                                                     |
|   are written to the console based on the     |                                                                     |
|   `console log level <#console-log-level>`__  |                                                                     |
|   configuration. The server writes messages   |                                                                     |
|   to the standard output stream (stdout).     |                                                                     |
| - **false**: Output log messages aren’t       |                                                                     |
|   written to the console.                     |                                                                     |
+-----------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: log-consolelevel
  :displayname: Console log level (Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.ConsoleLevel
  :environment: MM_LOGSETTINGS_CONSOLELEVEL
  :description: The level of detail in log events written when Mattermost outputs log messages to the console.

  - **DEBUG**: **(Default)** Outputs verbose detail for developers debugging issues.
  - **ERROR**: Outputs only error messages.
  - **INFO**: Outputs error messages and information around startup and initialization.

Console log level
~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------+---------------------------------------------------------------------+
| The level of detail in log events written     | - System Config path: **Environment > Logging**                     |
| when Mattermost outputs log messages to the   | - ``config.json setting``: ``".LogSettings.ConsoleLevel": DEBUG",`` |
| console.                                      | - Environment variable: ``MM_LOGSETTINGS_CONSOLELEVEL``             |
|                                               |                                                                     |
| - **DEBUG**: **(Default)** Outputs verbose    |                                                                     |
|   detail for developers debugging issues.     |                                                                     |
| - **ERROR**: Outputs only error messages.     |                                                                     |
| - **INFO**: Outputs error messages and        |                                                                     |
|   information around startup and              |                                                                     |
|   initialization.                             |                                                                     |
+-----------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: log-consolejson
  :displayname: Output console logs as JSON (Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.ConsoleJson
  :environment: MM_LOGSETTINGS_CONSOLEJSON
  :description: Configure Mattermost to output console logs as JSON.

  - **true**: **(Default)** Logged events are written in a machine-readable JSON format.
  - **false**: Logged events are written in plain text.

Output console logs as JSON
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------+---------------------------------------------------------------------+
| Configure Mattermost to output console logs   | - System Config path: **Environment > Logging**                     |
| as JSON.                                      | - ``config.json setting``: ``".LogSettings.ConsoleJson": true",``   |
|                                               | - Environment variable: ``MM_LOGSETTINGS_CONSOLEJSON``              |
| - **true**: **(Default)** Logged events are   |                                                                     |
|   written in a machine-readable JSON format.  |                                                                     |
| - **false**: Logged events are written in     |                                                                     |
|   plain text.                                 |                                                                     |
+-----------------------------------------------+---------------------------------------------------------------------+
| **Note**: Typically set to **true** in a production environment.                                                    |
+-----------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: log-enableplaintextcolor
  :displayname: Colorize plain text console logs (Logging)
  :systemconsole: N/A
  :configjson: .LogSettings.EnableColor
  :environment: MM_LOGSETTINGS_ENABLECOLOR
  :description: Enables system admins to display plain text log level details in color.

  - **true**: When logged events are output to the console as plain text, colorize log levels details.
  - **false**: **(Default)** Plain text log details aren't colorized in the console.

Colorize plain text console logs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------+----------------------------------------------------------------------+
| Enables system admins to display plain text   | - System Config path: N/A                                            |
| log level details in color.                   | - ``config.json setting``: ``".LogSettings.EnableColor": false",``   |
|                                               | - Environment variable: ``MM_LOGSETTINGS_ENABLECOLOR``               |
| - **true**: When logged events are output to  |                                                                      |
|   the console as plain text, colorize log     |                                                                      |
|   levels details.                             |                                                                      |
| - **false**: **(Default)** Plain text log     |                                                                      |
|   details aren't colorized in the console.    |                                                                      |
+-----------------------------------------------+----------------------------------------------------------------------+

.. config:setting:: log-enablefile
  :displayname: Output logs to file (Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.EnableFile
  :environment: MM_LOGSETTINGS_ENABLEFILE
  :description: Configure Mattermost to output console logs to a file.

  - **true**: **(Default)** Logged events are written based on the `file log level <#file-log-level>`__ configuration to a ``mattermost.log`` file located in the directory configured via file location.
  - **false**: Logged events aren’t written to a file.

Output logs to file
~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------+---------------------------------------------------------------------+
| Configure Mattermost to output console logs   | - System Config path: **Environment > Logging**                     |
| to a file.                                    | - ``config.json setting``: ``".LogSettings.EnableFile": true",``    |
|                                               | - Environment variable: ``MM_LOGSETTINGS_ENABLEFILE``               |
| - **true**: **(Default)** Logged events are   |                                                                     |
|   written based on the                        |                                                                     |
|   `file log level <#file-log-level>`__        |                                                                     |
|   configuration to a ``mattermost.log`` file  |                                                                     |
|   located in the directory configured via     |                                                                     |
|   ``file location``.                          |                                                                     |
| - **false**: Logged events aren’t written to  |                                                                     |
|   a file.                                     |                                                                     |
+-----------------------------------------------+---------------------------------------------------------------------+
| **Note**: Typically set to **true** in a production environment. When enabled, you can download the                 |
| ``mattermost.log`` file locally by going to **System Console > Reporting > Server Logs**, and selecting **Download  |
| Logs**.                                                                                                             |
+-----------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: log-filelocation
  :displayname: File log directory (Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.FileLocation
  :environment: MM_LOGSETTINGS_FILELOCATION
  :description: The location of the log files. Default value is **./logs**.

File log directory
~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------+---------------------------------------------------------------------+
| The location of the log files.                | - System Config path: **Environment > Logging**                     |
|                                               | - ``config.json setting``: ``".LogSettings.FileLocation": "",``     |
| String input. If left blank, log files are    | - Environment variable: ``MM_LOGSETTINGS_FILELOCATION``             |
| stored in the ``./logs`` directory.           |                                                                     |
+-----------------------------------------------+---------------------------------------------------------------------+
| **Note**: The path you configure must exist, and Mattermost must have write permissions for this directory.         |
+-----------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: log-filelevel
  :displayname: File log level (Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.FileLevel
  :environment: MM_LOGSETTINGS_FILELEVEL
  :description: The level of detail in log events when Mattermost outputs log messages to a file.

  - **DEBUG**: Outputs verbose detail for developers debugging issues.
  - **ERROR**: Outputs only error messages.
  - **INFO**: **(Default)** Outputs error messages and information around startup and initialization.

File log level
~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------+---------------------------------------------------------------------+
| The level of detail in log events when        | - System Config path: **Environment > Logging**                     |
| Mattermost outputs log messages to a file.    | - ``config.json setting``: ``".LogSettings.FileLevel": INFO",``     |
|                                               | - Environment variable: ``MM_LOGSETTINGS_FILELEVEL``                |
| - **DEBUG**: Outputs verbose detail for       |                                                                     |
|   developers debugging issues.                |                                                                     |
| - **ERROR**: Outputs only error messages.     |                                                                     |
| - **INFO**: **(Default)** Outputs error       |                                                                     |
|   messages and information around startup     |                                                                     |
|   and initialization.                         |                                                                     |
+-----------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: log-filejson
  :displayname: Output file logs as JSON (Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.FileJson
  :environment: MM_LOGSETTINGS_FILEJSON
  :description: Configure Mattermost to output file logs as JSON.

  - **true**: **(Default)** Logged events are written in a machine-readable JSON format.
  - **false**: Logged events are written in plain text.

Output file logs as JSON
~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------+---------------------------------------------------------------------+
| Configure Mattermost to output file logs as   | - System Config path: **Environment > Logging**                     |
| JSON.                                         | - ``config.json setting``: ``".LogSettings.FileJson": true",``      |
|                                               | - Environment variable: ``MM_LOGSETTINGS_FILEJSON``                 |
| - **true**: **(Default)** Logged events are   |                                                                     |
|   written in a machine-readable JSON format.  |                                                                     |
| - **false**: Logged events are written in     |                                                                     |
|   plain text.                                 |                                                                     |
+-----------------------------------------------+---------------------------------------------------------------------+
| **Note**: Typically set to **true** in a production environment.                                                    |
+-----------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: log-enablewebhookdebug
  :displayname: Enable webhook debugging (Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.EnableWebhookDebugging
  :environment: MM_LOGSETTINGS_ENABLEWEBHOOKDEBUGGING
  :description: Configure Mattermost to capture the contents of incoming webhooks to log files for debugging.

  - **true**: **(Default)** The contents of incoming webhooks are printed to console and/or file logs for debugging.
  - **false**: The contents of incoming webhooks aren’t printed to log files.

Enable webhook debugging
~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------+------------------------------------------------------------------------------+
| Configure Mattermost to capture the contents  | - System Config path: **Environment > Logging**                              |
| of incoming webhooks to console and/or file   | - ``config.json setting``: ``".LogSettings.EnableWebhookDebugging": true",`` |
| logs for debugging.                           | - Environment variable: ``MM_LOGSETTINGS_ENABLEWEBHOOKDEBUGGING``            |
|                                               |                                                                              |
| - **true**: **(Default)** The contents of     |                                                                              |
|   incoming webhooks are printed to log files  |                                                                              |
|   for debugging.                              |                                                                              |
| - **false**: The contents of incoming         |                                                                              |
|   webhooks aren’t printed to log files.       |                                                                              |
+-----------------------------------------------+------------------------------------------------------------------------------+
| **Note**: Enable debug logs by changing the :ref:`file log level <manage/logging:file logs>` to ``DEBUG`` to include         |
| the request body of incoming webhooks in logs.                                                                               |
+-----------------------------------------------+------------------------------------------------------------------------------+

.. config:setting:: log-multipletargetoutput
  :displayname: Output logs to multiple targets (Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.AdvancedLoggingJSON
  :environment: MM_LOGSETTINGS_ADVANCEDLOGGINGJSON
  :description: Configure Mattermost to allow any combination of console, local file, syslog, and TCP socket targets, and send log records to multiple targets.

Output logs to multiple targets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------+---------------------------------------------------------------------------+
| Configure Mattermost to allow any combination | - System Config path: **Environment > Logging**                           |
| of console, local file, syslog, and TCP       | - ``config.json setting``: ``".LogSettings.AdvancedLoggingJSON":: "",``   |
| socket targets, and send log records to       | - Environment variable: ``MM_LOGSETTINGS_ADVANCEDLOGGINGJSON``            |
| multiple targets.                             |                                                                           |
|                                               |                                                                           |
| String input can contain a filespec to        |                                                                           |
| another configuration file, a database DSN,   |                                                                           |
| or JSON.                                      |                                                                           |
+-----------------------------------------------+---------------------------------------------------------------------------+
| **Notes**:                                                                                                                |
|                                                                                                                           |
| - These targets have been chosen as they support the vast majority of log aggregators, and other log analysis tools,      |
|   without needing additional software installed.                                                                          |
| - Logs are recorded asynchronously to reduce latency to the caller.                                                       |
| - Advanced logging supports hot-reloading of logger configuration.                                                        |
+-----------------------------------------------+---------------------------------------------------------------------------+
| **Note**: See the :doc:`Mattermost logging </manage/logging>` documentation for details.                                  |
+-----------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: log-maxfieldsize
  :displayname: Maximum field size (Logging)
  :systemconsole: N/A
  :configjson: .LogSettings.MaxFieldSize
  :environment: MM_LOGSETTINGS_MAXFIELDSIZE
  :description: Enables system admins to limit the size of log fields during logging. Default is **2048**.

Maximum field size
~~~~~~~~~~~~~~~~~~

+-----------------------------------------------+----------------------------------------------------------------------+
| Enables system admins to limit the size of    | - System Config path: N/A                                            |
| log fields during logging.                    | - ``config.json setting``: ``".LogSettings.MaxFieldSize": 2048",``   |
|                                               | - Environment variable: ``MM_LOGSETTINGS_MAXFIELDSIZE``              |
| Numerical value. Default is **2048**.         |                                                                      |
+-----------------------------------------------+----------------------------------------------------------------------+

.. config:setting:: log-enablediagnostics
  :displayname: Enable diagnostics and error reporting (Logging)
  :systemconsole: Environment > Logging
  :configjson: .LogSettings.EnableDiagnostics
  :environment: MM_LOGSETTINGS_ENABLEDIAGNOSTICS
  :description: Send diagnostics and error reports to Mattermost, Inc.

Enable diagnostics and error reporting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------+-------------------------------------------------------------------------+
| Whether or not diagnostics and error reports | - System Config path: **Environment > Logging**                         |
| are sent to Mattermost, Inc.                 | - ``config.json setting``: ``".LogSettings.EnableDiagnostics": "",``    |
|                                              | - Environment variable: ``MM_LOGSETTINGS_ENABLEDIAGNOSTICS``            |
| - **true**: **(Default)** Send diagnostics   |                                                                         |
|   and error reports.                         |                                                                         |
| - **false**: Diagnostics and error reports   |                                                                         |
|   aren't sent.                               |                                                                         |
+----------------------------------------------+-------------------------------------------------------------------------+
| **Note**: See the :ref:`telemetry <manage/telemetry:error and diagnostics reporting feature>` docummentation for       |
| details on the information Mattermost collects.                                                                        |
+----------------------------------------------+-------------------------------------------------------------------------+

----

Session lengths
---------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

User sessions are cleared when a user tries to log in, and sessions are cleared every 24 hours from the sessions database table. Configure session lengths by going to **System Console > Environment > Session Lengths**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: sessionlength-extendwithactivity
  :displayname: Extend session length with activity (Session Lengths)
  :systemconsole: Environment > Session Lengths
  :configjson: .ServiceSettings.ExtendSessionLengthWithActivity
  :environment: MM_SERVICESETTINGS_EXTENDSESSONLENGTHWITHACTIVITY

  - **true**: **(Default)** Sessions are automatically extended when users are active in their Mattermost client.
  - **false**: Sessions won't extend with activity in Mattermost.

Extend session length with activity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Improves the user experience by extending sessions and keeping | - System Config path: **Environment > Session Lengths**                                 |
| users logged in if they are active in their Mattermost apps.   | - ``config.json`` setting: ``".ServiceSettings.ExtendSessionLengthWithActivity: true,`` |
|                                                                | - Environment variable: ``MM_SERVICESETTINGS_EXTENDSESSONLENGTHWITHACTIVITY``           |
| - **true**: **(Default)** Sessions are automatically           |                                                                                         |
|   extended when users are active in their Mattermost           |                                                                                         |
|   client. User sessions only expire when users aren’t active   |                                                                                         |
|   in their Mattermost client for the entire duration of the    |                                                                                         |
|   session lengths defined.                                     |                                                                                         |
| - **false**: Sessions won't extend with activity in            |                                                                                         |
|   Mattermost. User sessions immediately expire at the          |                                                                                         |
|   end of the session length or based on the                    |                                                                                         |
|   `session idle timeout <#session-idle-timeout>`__ configured. |                                                                                         |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. config:setting:: sessionlength-TerminateSessionsOnPasswordChange
  :displayname: Terminate sessions on password change (Session Lengths)
  :systemconsole: Environment > Session Lengths
  :configjson: .ServiceSettings.TerminateSessionsOnPasswordChange
  :environment: MM_SERVICESETTINGS_TERMINATESESSIONSONPASSWORDCHANGE

  - **true**: **(Default for new deployments)** Session revocation is enabled. All sessions of a user expire if their password is changed (by themselves or a system admin). If the password change is initiated by the user, their current session isn't terminated.
  - **false**: **(Default for existing deployments)** Session revocation is disabled. When users change their password, only the user's current session is revoked. When a system admin changes the user's password, none of the user's sessions are revoked.

Terminate sessions on password change
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| Enable or disable session revocation when a user's             | - System Config path: **Environment > Session Lengths**                                   |
| password changes.                                              | - ``config.json`` setting: ``".ServiceSettings.TerminateSessionsOnPasswordChange: true,`` |
|                                                                | - Environment variable: ``MM_SERVICESETTINGS_TERMINATESESSIONSONPASSWORDCHANGE``          |
| - **true**: **(Default for new deployments)**                  |                                                                                           |
|   Session revocation is enabled.                               |                                                                                           |
|   All sessions of a user expire if their password is changed   |                                                                                           |
|   (by themselves or by a system admin). If the password change |                                                                                           |
|   is initiated by the user, their current session isn't        |                                                                                           |
|   terminated.                                                  |                                                                                           |
| - **false**: **(Default for existing deployments)**            |                                                                                           |
|   Session revocation is disabled.                              |                                                                                           |
|   When users change their password, only the user's current    |                                                                                           |
|   session is revoked. When a system admin changes the user's   |                                                                                           |
|   password, none of the user's sessions are revoked.           |                                                                                           |
+----------------------------------------------------------------+-------------------------------------------------------------------------------------------+

.. config:setting:: sessionlength-webinhours
  :displayname: Session length for AD/LDAP and email (Session Lengths)
  :systemconsole: Environment > Session Lengths
  :configjson: .ServiceSettings.SessionLengthWebInHours
  :environment: MM_SERVICESETTINGS_SESSONLENGTHWEBINHOURS

  Set the number of hours counted from the last time a user entered their credentials into the web app or the desktop app to the expiry of the user’s session on email and AD/LDAP authentication.
  Default is **720** hours.

Session length for AD/LDAP and email
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------+--------------------------------------------------------------------------------+
| Set the number of hours counted from the last time a user      | - System Config path: **Environment > Session Lengths**                        |
| entered their credentials into the web app or the desktop      | - ``config.json`` setting: ``".ServiceSettings.SessionLengthWebInHours: 720,`` |
| app to the expiry of the user’s session on email and AD/LDAP   | - Environment variable: ``MM_SERVICESETTINGS_SESSONLENGTHWEBINHOURS``          |
| authentication.                                                |                                                                                |
|                                                                |                                                                                |
| Numerical input in hours. Default is **720** hours.            |                                                                                |
+----------------------------------------------------------------+--------------------------------------------------------------------------------+
| **Note**: After changing this setting, the new session length takes effect after the next time the user enters their credentials.               |
+----------------------------------------------------------------+--------------------------------------------------------------------------------+

.. config:setting:: sessionlength-mobileinhours
  :displayname: Session length for mobile (Session Lengths)
  :systemconsole: Environment > Session Lengths
  :configjson: .ServiceSettings.SessionLengthMobileInHours
  :environment: MM_SERVICESETTINGS_SESSONLENGTHMOBILEINHOURS
  :description: Set the number of hours counted from the last time a user entered their credential into the mobile app to the expiry of the user’s session. Default is **720** hours.

Session length for mobile
~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------+-----------------------------------------------------------------------------------+
| Set the number of hours counted from the last time a user      | - System Config path: **Environment > Session Lengths**                           |
| entered their credential into the mobile app to the expiry     | - ``config.json`` setting: ``".ServiceSettings.SessionLengthMobileInHours: 720,`` |
| of the user’s session.                                         | - Environment variable: ``MM_SERVICESETTINGS_SESSONLENGTHMOBILEINHOURS``          |
|                                                                |                                                                                   |
| Numerical input in hours. Default is **720** hours.            |                                                                                   |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------+
| **Note**: After changing this setting, the new session length takes effect after the next time the user enters their credentials.                  |
+----------------------------------------------------------------+-----------------------------------------------------------------------------------+

.. config:setting:: sessionlength-ssoinhours
  :displayname: Session length for SSO (Session Lengths)
  :systemconsole: Environment > Session Lengths
  :configjson: .ServiceSettings.SessionLengthSSOInHours
  :environment: MM_SERVICESETTINGS_SESSONLENGTHSSOINHOURS
  :description: Set the number of hours from the last time a user entered their SSO credentials to the expiry of the user’s session. Default is **720** hours.

Session length for SSO
~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------+----------------------------------------------------------------------------------+
| Set the number of hours from the last time a user entered      | - System Config path: **Environment > Session Lengths**                          |
| their SSO credentials to the expiry of the user’s session.     | - ``config.json`` setting: ``".ServiceSettings.SessionLengthSSOInHours: 720,``   |
| This setting defines the session length for SSO                | - Environment variable: ``MM_SERVICESETTINGS_SESSONLENGTHSSOINHOURS``            |
| authentication, such as SAML, GitLab, and OAuth 2.0.           |                                                                                  |
|                                                                |                                                                                  |
| Numerical input in hours. Default is **720** hours.            |                                                                                  |
| Numbers as decimals are also valid values for this             |                                                                                  |
| configuration setting.                                         |                                                                                  |
+----------------------------------------------------------------+----------------------------------------------------------------------------------+
| **Notes**:                                                                                                                                        |
|                                                                                                                                                   |
| - After changing this setting, the new session length takes effect after the next time the user enters their credentials.                         |
| - If the authentication method is SAML, GitLab, or OAuth 2.0, users may automatically be logged back in to Mattermost if they are already logged  |
|   in to SAML, GitLab, or with OAuth 2.0.                                                                                                          |
+----------------------------------------------------------------+----------------------------------------------------------------------------------+

.. config:setting:: sessionlength-sessioncache
  :displayname: Session cache (Session Lengths)
  :systemconsole: Environment > Session Lengths
  :configjson: .ServiceSettings.SessionCacheInMinutes
  :environment: MM_SERVICESETTINGS_SESSONCACHEINMINUTES
  :description: Set the number of minutes to cache a session in memory. Default is **10** minutes.

Session cache
~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------+-----------------------------------------------------------------------------+
| Set the number of minutes to cache a session in memory.        | - System Config path: **Environment > Session Lengths**                     |
|                                                                | - ``config.json`` setting: ``".ServiceSettings.SessionCacheInMinutes: 10,`` |
| Numerical input in minutes. Default is **10** minutes.         | - Environment variable: ``MM_SERVICESETTINGS_SESSONCACHEINMINUTES``         |
+----------------------------------------------------------------+-----------------------------------------------------------------------------+

.. config:setting:: sessionlength-sessionidletimeout
  :displayname: Session idle timeout (Session Lengths)
  :systemconsole: N/A
  :configjson: .ServiceSettings.SessionIdleTimeoutInMinutes
  :environment: MM_SERVICESETTINGS_SESSONIDLETIMEOUTINMINUTES

  The number of minutes from the last time a user was active on the system to the expiry of the user’s session. Once expired, the user will need to log in to continue.
  Default is **43200** minutes (30 days). Minimum value is 5 minutes, and a value of 0 sets the time as unlimited.

Session idle timeout
~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+----------------------------------------------------------------+--------------------------------------------------------------------------------------+
| The number of minutes from the last time a user was active     | - System Config path: N/A                                                            |
| on the system to the expiry of the user’s session.             | - ``config.json`` setting: ``".ServiceSettings.SessionIdleTimeoutInMinutes: 43200,`` |
| Once expired, the user will need to log in to continue.        | - Environment variable: ``MM_SERVICESETTINGS_SESSONIDLETIMEOUTINMINUTES``            |
|                                                                |                                                                                      |
| Numerical input in minutes. Default is **43200** (30 days).    |                                                                                      |
| Minimum value is **5** minutes, and a value of **0** sets      |                                                                                      |
| the time as unlimited.                                         |                                                                                      |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------+
| **Notes**:                                                                                                                                            |
|                                                                                                                                                       |
| - This setting has no effect when `extend session length with activity <#extend-session-length-with-activity>`__ is set to **true**.                  |
| - This setting applies to the webapp and the desktop app. For mobile apps, use an                                                                     |
|   :doc:`EMM provider </deploy/deploy-mobile-apps-using-emm-provider>` to lock the app when not in use.                                                |
| - In :doc:`high availability mode </scale/high-availability-cluster-based-deployment>`, enable IP hash load balancing for reliable                    |
|   timeout measurement.                                                                                                                                |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------+

----

Performance monitoring
----------------------

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

Configure performance monitoring by going to **System Console > Environment > Performance Monitoring**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: perf-enablemonitoring
  :displayname: Enable performance monitoring (Performance Monitoring)
  :systemconsole: Environment > Performance Monitoring
  :configjson: .MetricsSettings.Enable
  :environment: MM_METRICSSETTINGS_ENABLE
  :description: Enable or disable performance monitoring.

  - **true**: Performance monitoring data collection and profiling is enabled.
  - **false**: **(Default)** Mattermost performance monitoring is disabled.

Enable performance monitoring
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+-----------------------------------------------+---------------------------------------------------------------------+
| Enable or disable performance monitoring.     | - System Config path: **Environment > Performance Monitoring**      |
|                                               | - ``config.json setting``: ``".MetricsSettings.Enable": false",``   |
| - **true**: Performance monitoring data       | - Environment variable: ``MM_METRICSSETTINGS_ENABLE``               |
|   collection and profiling is enabled.        |                                                                     |
| - **false**: **(Default)** Mattermost         |                                                                     |
|   performance monitoring is disabled.         |                                                                     |
+-----------------------------------------------+---------------------------------------------------------------------+
| See the :doc:`performance monitoring </scale/deploy-prometheus-grafana-for-performance-monitoring>` documentation   |
| to learn more.                                                                                                      |
+-----------------------------------------------+---------------------------------------------------------------------+

.. config:setting:: perf-listenaddress
  :displayname: Listen address for performance (Performance Monitoring)
  :systemconsole: Environment > Performance Monitoring
  :configjson: .MetricsSettings.ListenAddress
  :environment: MM_METRICSSETTINGS_LISTENADDRESS
  :description: The port the Mattermost server will listen on to expose performance metrics, when enabled. Default is port **8067**.

Listen address for performance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+---------------------------------------------------------------+-------------------------------------------------------------------------+
| The port the Mattermost server will listen on to expose       | - System Config path: **Environment > Performance Monitoring**          |
| performance metrics, when enabled.                            | - ``config.json setting``: ``".MetricsSettings.ListenAddress": 8067",`` |
|                                                               | - Environment variable: ``MM_METRICSSETTINGS_LISTENADDRESS``            |
| Numerical input. Default is **8067**.                         |                                                                         |
+---------------------------------------------------------------+-------------------------------------------------------------------------+

----

Developer
---------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

Configure developer mode by going to **System Console > Environment > Developer**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

.. config:setting:: dev-enabletesting
  :displayname: Enable testing commands (Developer)
  :systemconsole: Environment > Developer
  :configjson: .ServiceSettings.EnableTesting
  :environment: MM_SERVICESETTINGS_ENABLETESTING
  :description: Enable or disable the ``/test`` slash command.

  - **true**: **(Default)** The ``/test`` slash command is enabled to load test accounts and test data.
  - **false**:  The ``/test`` slash command is disabled.

Enable testing commands
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------+--------------------------------------------------------------------------+
| Enable or disable the ``/test`` slash command.    | - System Config path: **Environment > Developer**                        |
|                                                   | - ``config.json setting``: ``".ServiceSettings.EnableTesting": true",``  |
| - **true**: **(Default)** The ``/test`` slash     | - Environment variable: ``MM_SERVICESETTINGS_ENABLETESTING``             |
|   command is enabled to load test accounts        |                                                                          |
|   and test data.                                  |                                                                          |
| - **false**:  The ``/test`` slash command is      |                                                                          |
|   disabled.                                       |                                                                          |
+---------------------------------------------------+--------------------------------------------------------------------------+

.. config:setting:: dev-enabledeveloper
  :displayname: Enable developer mode (Developer)
  :systemconsole: Environment > Developer
  :configjson: .ServiceSettings.EnableDeveloper
  :environment: MM_SERVICESETTINGS_ENABLEDEVELOPER
  :description: Enable or disable developer mode.

  - **true**: **(Default)** Javascript errors are shown in a banner at the top of Mattermost the user interface. Not recommended for use in production.
  - **false**: Users are not alerted to Javascript errors.

Enable developer mode
~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------+---------------------------------------------------------------------------+
| Enable or disable developer mode.             | - System Config path: **Environment > Developer**                         |
|                                               | - ``config.json setting``: ``".ServiceSettings.EnableDeveloper": true",`` |
| - **true**: **(Default)** Javascript errors   | - Environment variable: ``MM_SERVICESETTINGS_ENABLEDEVELOPER``            |
|   are shown in a banner at the top of         |                                                                           |
|   Mattermost the user interface.              |                                                                           |
|   Not recommended for use in production.      |                                                                           |
| - **false**: Users are not alerted to         |                                                                           |
|   Javascript errors.                          |                                                                           |
+-----------------------------------------------+---------------------------------------------------------------------------+

.. config:setting:: dev-enableclientdebugging
  :displayname: Enable client debugging (Developer)
  :systemconsole: Environment > Developer
  :configjson: .ServiceSettings.EnableClientPerformanceDebugging
  :environment: MM_SERVICESETTINGS_ENABLECLIENTPERFORMANCEDEBUGGING
  :description: Enable or disable client-side debugging settings found in *Settings > Advanced > Debugging* for individual users.

  - **true**: Those settings are visible and can be enabled by users.
  - **false**: **(Default)** Those settings are hidden and disabled.

Enable client debugging
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+---------------------------------------------------+---------------------------------------------------------------------------------------------+
| Enable or disable client-side debugging settings  | - System Config path: **Environment > Developer**                                           |
| found in **Settings > Advanced > Debugging**      | - ``config.json setting``: ``".ServiceSettings.EnableClientPerformanceDebugging": false",`` |
| for individual users.                             | - Environment variable: ``MM_SERVICESETTINGS_ENABLECLIENTPERFORMANCEDEBUGGING``             |
|                                                   |                                                                                             |
| - **true**: Those settings are visible and can    |                                                                                             |
|   be enabled by users.                            |                                                                                             |
| - **false**: **(Default)** Those settings are     |                                                                                             |
|   hidden and disabled.                            |                                                                                             |
+---------------------------------------------------+---------------------------------------------------------------------------------------------+
| See the :ref:`client debugging <preferences/manage-advanced-options:performance debugging>` documentation to learn more.                        |
+---------------------------------------------------+---------------------------------------------------------------------------------------------+

.. config:setting:: dev-allowuntrustedinternalconnections
  :displayname: Allow untrusted internal connections (Developer)
  :systemconsole: Environment > Developer
  :configjson: .ServiceSettings.AllowedUntrustedInternalConnections
  :environment: MM_SERVICESETTINGS_ALLOWUNTRUSTEDINTERNALCONNECTIONS
  :description: This setting is a whitelist of local network addresses that can be requested by the Mattermost server.

Allow untrusted internal connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E10 or E20</p>

+-----------------------------------------------+-----------------------------------------------------------------------------------------------+
| Limit the ability for the Mattermost server   | - System Config path: **Environment > Developer**                                             |
| to make untrusted requests within its local   | - ``config.json setting``: ``".ServiceSettings.AllowedUntrustedInternalConnections": "",``    |
| network. A request is considered “untrusted”  | - Environment variable: ``MM_SERVICESETTINGS_ALLOWEDUNTRUSTEDINTERNALCONNECTIONS``            |
| when it’s made on behalf of a client.         |                                                                                               |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------+
| This setting is a whitelist of local network addresses that can be requested by the Mattermost server. It’s configured as a                   |
| whitespace-separated list of hostnames, IP addresses, and CIDR ranges that can be accessed.                                                   |
|                                                                                                                                               |
| Requests that can only be configured by system admins are considered trusted and won't be affected by this setting. Trusted URLs include      |
| ones used for OAuth login or for sending push notifications.                                                                                  |
|                                                                                                                                               |
| The following features make untrusted requests and are affected by this setting:                                                              |
|                                                                                                                                               |
| - Integrations using webhooks, slash commands, or message actions. This prevents them from requesting endpoints within the local network.     |
| - Link previews. When a link to a local network address is posted in a chat message, this prevents a link preview from being displayed.       |
| - The local :doc:`image proxy </deploy/image-proxy>`. If the local image proxy is enabled, images located on                                  |
|   the local network cannot be used by integrations or posted in chat messages.                                                                |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------+
|                                                                                                                                               |
| Some examples of when you may want to modify this setting include:                                                                            |
|                                                                                                                                               |
| - When installing a plugin that includes its own images, such as `Matterpoll <https://github.com/matterpoll/matterpoll>`__, you'll need to    |
|   add the Mattermost server’s domain name to                                                                                                  |
|   this list.                                                                                                                                  |
| - When running a bot or webhook-based integration on your local network, you’ll need to add the hostname of the bot/integration to this list. |
| - If your network is configured in such a way that publicly-accessible web pages or images are accessed by the Mattermost server using        |
|   their internal IP address, the hostnames for those servers must be added to this list.                                                      |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------+
| **Warning**: This setting is intended to prevent users located outside your local network from using the Mattermost server to request         |
| confidential data from inside your network. Care should be used when configuring this setting to prevent unintended access to your local      |
| network.                                                                                                                                      |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------+
| **Notes**:                                                                                                                                    |
|                                                                                                                                               |
| - The public IP of the Mattermost application server itself is also considered a reserved IP.                                                 |
| - Use whitespaces instead of commas to list the hostnames, IP addresses, or CIDR ranges.                                                      |
|   For example: ``webhooks.internal.example.com``, ``127.0.0.1``, or ``10.0.16.0/28``.                                                         |
| - IP address and domain name rules are applied before host resolution.                                                                        |
| - CIDR rules are applied after host resolution, and only CIDR rules require DNS resolution.                                                   |
| - Mattermost attempts to match IP addresses and hostnames without even resolving. If that fails, Mattermost resolve using the local resolver  |
|   (by reading the ``/etc/hosts`` file first), then checking for matching CIDR rules.                                                          |
|   For example, if the domain “webhooks.internal.example.com” resolves to the IP address ``10.0.16.20``, a webhook with the URL                |
|   ``https://webhooks.internal.example.com/webhook`` can be whitelisted using ``webhooks.internal.example.com``, or ``10.0.16.16/28``,         |
|   but not ``10.0.16.20``.                                                                                                                     |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------+

config.json-only settings
-------------------------

.. include:: ../_static/badges/allplans-selfhosted.rst
  :start-after: :nosearch:

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
|                                               | - ``config.json setting``: ``CloudSettings`` > ``Disable`` > ``false,``   |
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

.. config:setting:: exp-enableapiteamdeletion
  :displayname: Enable API team deletion (ServiceSettings)
  :systemconsole: N/A
  :configjson: EnableAPITeamDeletion
  :environment: N/A

  - **true**: The ``api/v4/teams/{teamid}?permanent=true`` API endpoint can be called by team admins and system admins (or users with appropriate permissions), or by running the mmctl team delete command, to permanently delete a team.
  - **false**: **(Default)** The API endpoint cannot be called, but ``api/v4/teams/{teamid}`` can still be used to soft delete a team.

Enable API team deletion
~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: The ``api/v4/teams/{teamid}?permanent=true`` API endpoint can be called by team admins and system admins (or users with appropriate permissions), or by running the :ref:`mmctl team delete <manage/mmctl-command-line-tool:mmctl team delete>` command to permanently delete a team.

**False**: The API endpoint cannot be called. Note that ``api/v4/teams/{teamid}`` can still be used to soft delete a team.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAPITeamDeletion": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enableapiuserdeletion
  :displayname: Enable API user deletion (ServiceSettings)
  :systemconsole: N/A
  :configjson: EnableAPIUserDeletion
  :environment: N/A

  - **true**: The ``api/v4/users/{userid}?permanent=true`` API endpoint can be called by system admins (or users with appropriate permissions), or by running the mmctl user delete command, to permanently delete a user.
  - **false**: **(Default)** The API endpoint cannot be called, but ``api/v4/users/{userid}`` can still be used to soft delete a user.

Enable API user deletion
~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: The ``api/v4/users/{userid}?permanent=true`` API endpoint can be called by system admins (or users with appropriate permissions), or by running the :ref:`mmctl user delete <manage/mmctl-command-line-tool:mmctl user delete>` command, to permanently delete a user.

**False**: The API endpoint cannot be called. Note that ``api/v4/users/{userid}`` can still be used to soft delete a user.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAPIUserDeletion": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

.. config:setting:: exp-enableapichanneldeletion
  :displayname: Enable API channel deletion (ServiceSettings)
  :systemconsole: N/A
  :configjson: EnableAPIChannelDeletion
  :environment: N/A

  - **true**: The ``api/v4/channels/{channelid}?permanent=true`` API endpoint can be called by system admins (or users with appropriate permissions), or by running the mmctl channel delete command, to permanently delete a channel.
  - **false**: **(Default)** The API endpoint cannot be called, but ``api/v4/channels/{channelid}`` can still be used to soft delete a channel.

Enable API channel deletion
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: The ``api/v4/channels/{channelid}?permanent=true`` API endpoint can be called by system admins (or users with appropriate permissions), or by running the :ref:`mmctl channel delete <manage/mmctl-command-line-tool:mmctl channel delete>` command, to permanently delete a channel.

**False**: The API endpoint cannot be called. Note that ``api/v4/channels/{channelid}`` can still be used to soft delete a channel.

+----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAPIChannelDeletion": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------+