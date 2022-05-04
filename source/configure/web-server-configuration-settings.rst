Web server configuration settings
=================================

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/download
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Configure the network environment in which Mattermost is deployed by going to **System Console > Environment > Web Server**, or by updating the ``config.json`` file as described in the following table. Changes to configuration settings in this section require a server restart before taking effect.

.. include:: common-config-settings-notation.rst
    :start-after: :nosearch:

Site URL
--------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

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
| - From Mattermost v5.1, the URL may contain a subpath, such as "https://example.com/company/mattermost".                      |
| - If Site URL is not set, the following features will not operate correctly:                                                  |
|                                                                                                                               |
|   - Email notifications will contain broken links, and email batching will not work.                                          |
|   - Authentication via OAuth 2.0, including GitLab, Google, and Office 365, will fail.                                        |
|   - Plugins may not work as expected.                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------+

Listen address
--------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+------------------------------------------------------------------+
| The address and port to which to bind and listen.             | - System Config path: **Environment > Web Server**               |
| Specifying ``:8065`` will bind to all network interfaces.     | - ``config.json`` setting: ``".ServiceSettings.ListenAddress",`` |
| Specifying ``127.0.0.1:8065`` will only bind to the network   | - Environment variable: ``MM_SERVICESETTINGS.LISTENADDRESS``     |
| interface having that IP address.                             |                                                                  |
|                                                               |                                                                  |
| If you choose a port of a lower level (called “system ports”  |                                                                  |
| or “well-known ports”, in the range of 0-1023), you must have |                                                                  |
| permissions to bind to that port.                             |                                                                  |
+---------------------------------------------------------------+------------------------------------------------------------------+

Forward port 80 to 443
----------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+--------------------------------------------------------------------------+
| Forward insecure traffic from port 80 to port 442.            | - System Config path: **Environment > Web Server**                       |
|                                                               | - ``config.json`` setting: ``".ServiceSettings.Forward80To443: false",`` |
| - **true**: Forwards all insecure traffic from port 80 to     | - Environment variable: ``MM_SERVICESETTINGS_FORWARD80TO443``            |
|   secure port 443.                                            |                                                                          |
| - **false**: **(Default)** When using a proxy such as NGINX   |                                                                          |
|   in front of Mattermost this setting is unnecessary          |                                                                          |
|   and should be set to false.                                 |                                                                          |
+---------------------------------------------------------------+--------------------------------------------------------------------------+

Connection security
-------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------------------------------+-----------------------------------------------------------------------+
| Connection security between Mattermost clients and the server.        | - System Config path: **Environment > Web Server**                    |
|                                                                       | - ``config.json`` setting: ``".ServiceSettings.ConnectionSecurity",`` |
| - **Not specified**: Mattermost will connect over an unsecure         | - Environment variable: ``MM_SERVICESETTINGS_CONNECTIONSECURITY``     |
|   connection.                                                         |                                                                       |
| - **TLS**: Encrypts the communication between Mattermost              |                                                                       |
|   clients and your server. See the `configuring TLS on Mattermost     |                                                                       |
|   <https://docs.mattermost.com/install/config-tls-mattermost.html>`__ |                                                                       |
|   for more details                                                    |                                                                       |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------+

TLS certificate file
--------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+--------------------------------------------------------+------------------------------------------------------------------+
| The path to the certificate file to use for TLS        | - System Config path: **Environment > Web Server**               |
| connection security.                                   | - ``config.json`` setting: ``".ServiceSettings.TLSCertFile",``   |
|                                                        | - Environment variable: ``MM_SERVICESETTINGS_TLSCERTFILE``       |
| String input                                           |                                                                  |
+--------------------------------------------------------+------------------------------------------------------------------+

TSL key file
------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+--------------------------------------------------------+---------------------------------------------------------------+
| The path to the TLS key file to use for TLS            | - System Config path: **REnvironment > Web Server**           |
| connection security.                                   | - ``config.json`` setting: ``".ServiceSettings.TLSKeyFile",`` |
|                                                        | - Environment variable: ``MM_SERVICESETTINGS_TLSKEYFILE``     |
| String input                                           |                                                               |
+--------------------------------------------------------+---------------------------------------------------------------+

Use Let's Encrypt
-----------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------------+--------------------------------------------------------------------------+
| Enable the automatic retrieval of certificates from Let’s Encrypt.  | - System Config path: **Environment > Web Server**                       |
| See the `configuring TLS on Mattermost documentation                | - ``config.json`` setting: ``".ServiceSettings.UseLetsEncrypt: false",`` |
| <https://docs.mattermost.com/install/config-tls-mattermost.html>`__ | - Environment variable: ``MM_SERVICESETTINGS_USELETSENCRYPT``            |
| for more details on setting up Let’s Encrypt.                       |                                                                          |
|                                                                     |                                                                          |
| - **true**: The certificate will be retrieved when a client         |                                                                          |
|   attempts to connect from a new domain. This will work with        |                                                                          |
|   multiple domains.                                                 |                                                                          |
| - **false**: **(Default)** Manual certificate specification         |                                                                          |
|   based on the TLS Certificate File and TLS Key File specified      |                                                                          |
|   above.                                                            |                                                                          |
+---------------------------------------------------------------------+--------------------------------------------------------------------------+

Let's Encrypt certificate cache file
-------------------------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+--------------------------------------------------------+------------------------------------------------------------------------------------+
| The path to the file where certificates and other data | - System Config path: **Reporting > Team Statistics**                              |
| about the Let’s Encrypt service will be stored.        | - ``config.json`` setting: ``".ServiceSettings.LetsEncryptCertificateCacheFile",`` |
|                                                        | - Environment variable: ``MM_SERVICESETTINGS_LETSENCRYPTCERTIFICATECACHEFILE``     |
| File path                                              |                                                                                    |
+--------------------------------------------------------+------------------------------------------------------------------------------------+

Read timeout
------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+--------------------------------------------------------+---------------------------------------------------------------------+
| Maximum time allowed from when the connection is       | - System Config path: **Environment > Web Server**                  |
| accepted to when the request body is fully read.       | - ``config.json`` setting: ``".ServiceSettings.ReadTimeout: 300",`` |
|                                                        | - Environment variable: ``MM_SERVICESETTINGS_READTIMEOUT``          |
| Numerical input in seconds. Default is 300 seconds.    |                                                                     |
+--------------------------------------------------------+---------------------------------------------------------------------+

Write timeout
-------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+--------------------------------------------------------+-----------------------------------------------------------------------------+
| If using HTTP (insecure), this is the maximum time     | - System Config path: **Environment > Web Server**                          |
| allowed from the end of reading the request headers    | - ``config.json`` setting: ``".ServiceSettings.WriteTimeoutTimeout: 300",`` |
| until the response is written.                         | - Environment variable: ``MM_SERVICESETTINGS_WRITETIMEOUTTIMEOUT``          |
|                                                        |                                                                             |
| If using HTTPS, it's the total time from when the      |                                                                             |
| connection is accepted until the response is written.  |                                                                             |
| accepted to when the request body is fully read.       |                                                                             |
|                                                        |                                                                             |
| Numerical input in seconds. Default is 300 seconds.    |                                                                             |
+--------------------------------------------------------+-----------------------------------------------------------------------------+

Idle timeout
------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+--------------------------------------------------------+---------------------------------------------------------------------+
| Set an explicit idle timeout in the HTTP server.       | - System Config path: **Environment > Web Server**                  |
| This is the maximum time allowed before an idle        | - ``config.json`` setting: ``".ServiceSettings.IdleTimeout: 300",`` |
| connection is disconnected.                            | - Environment variable: ``MM_SERVICESETTINGS_IDLETIMEOUT``          | 
|                                                        |                                                                     |
| Numerical input in seconds. Default is 300 seconds.    |                                                                     |
+--------------------------------------------------------+---------------------------------------------------------------------+

Webserver mode
--------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------------+------------------------------------------------------------------------+
| We recommend gzip to improve performance unless your                | - System Config path: **Environment > Web Server**                     |
| environment has specific restrictions, such as a web proxy that     | - ``config.json`` setting: ``".ServiceSettings.WebserverMode: gzip",`` |
| distributes gzip files poorly.                                      | - Environment variable: ``MM_SERVICESETTINGS_WEBSERVERMODE``           |
|                                                                     |                                                                        |
| - **gzip**: **(Default)** The Mattermost server will serve stati    |                                                                        |
|   files compressed with gzip to improve performance.                |                                                                        |
|   gzip compression applies to the HTML, CSS, Javascript, and other  |                                                                        |
|   static content files that make up the Mattermost web client.      |                                                                        |
| - **Uncompressed**: The Mattermost server will serve static         |                                                                        |
|   files uncompressed.                                               |                                                                        |
| - **Disabled**: The Mattermost server will not serve static files.  |                                                                        |
|   based on the TLS Certificate File and TLS Key File specified      |                                                                        |
|   above.                                                            |                                                                        |
+---------------------------------------------------------------------+------------------------------------------------------------------------+

Enable insecure outgoing connections
------------------------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| **Security note**: Enabling this feature makes these          | - System Config path: **Environment > Web Server**                                          |
| connections susceptible to man-in-the-middle attacks.         | - ``config.json`` setting: ``".ServiceSettings.EnableInsecureOutgoingConnections: false",`` |
|                                                               | - Environment variable: ``MM_SERVICESETTINGS_ENABLEINSECUREOUTGOINGCONNECTIONS``            |
| - **true**: Outgoing HTTPS requests can accept unverified,    |                                                                                             |
|   self-signed certificates. For example, outgoing webhooks    |                                                                                             |
|   to a server with a self-signed TLS certificate, using any   |                                                                                             |
|   domain, will be allowed.                                    |                                                                                             |
| - **false**: **(Default)** Only secure HTTPS requests are     |                                                                                             |
|   allowed.                                                    |                                                                                             |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------+

Managed resource paths
----------------------

|all-plans| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

+--------------------------------------------------------+-------------------------------------------------------------------------+
| A comma-separated list of paths within the Mattermost  | - System Config path: **Environment > Web Server**                      |
| domain that are managed by a third party service       | - ``config.json`` setting: ``".ServiceSettings.ManagedResourcePaths",`` |
| instead of Mattermost itself.                          | - Environment variable: ``MM_SERVICESETTINGS_ManagedResourcePaths``     |
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
| in a browser. See the `desktop managed resources <https://docs.mattermost.com/install/desktop-app-managed-resources.html>`__     |
| documentation for details.                                                                                                       |
+--------------------------------------------------------+-------------------------------------------------------------------------+

Reload configuration from disk
------------------------------

|enterprise| |self-hosted|

*Available in legacy Enterprise Edition E10/E20*

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
----------------

|all-plans| |self-hosted|

+----------------------------------------------------------+---------------------------------------------------------------+
| Purge all in-memory caches for sessions, accounts,       | - System Config path: **Environment > Web Server**            |
| and channels by pressing **Purge All Caches** in the     | - ``config.json`` setting: N/A                                |
| System Console.                                          | - Environment variable: N/A                                   |
| file, and then reload configuration to fail over         |                                                               |
| without taking the server down.                          |                                                               |
|                                                          |                                                               |
| Select the **Reload configuration from disk** button     |                                                               |
| in the System Console after changing your database       |                                                               | 
| configuration. Then, go to **Environment > Database**    |                                                               |
| and select **Recycle Database Connections** to           |                                                               |
| complete the reload.                                     |                                                               |
+----------------------------------------------------------+---------------------------------------------------------------+
| **Note**:                                                                                                                |
| Purging the caches may adversely impact performance. Deployments using `High Availability                                |
| <https://docs.mattermost.com/scale/high-availability-cluster.html>`__ will attempt to purge all the servers in the       |
| cluster.                                                                                                                 |
+----------------------------------------------------------+---------------------------------------------------------------+
