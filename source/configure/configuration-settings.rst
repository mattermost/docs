Configuration Settings
======================

Mattermost configuration settings are maintained in the ``config.json`` configuration file, located in the ``mattermost/config`` directory. You can modify the configuration file using the System Console, or by using a text editor to modify it directly.

.. important::

   Mattermost must have write permissions to ``config.json``, otherwise changes made in the System Console will have no effect.

   On new installations from v5.14, the ``default.json`` file used to create the initial ``config.json`` has been removed from the binary and replaced with a build step that generates a fresh ``config.json``. This is to ensure the initial configuration file has all the correct defaults provided in the server code. Existing ``config.json`` files are not affected by this change.

   From Mattermost v5.38 (released August 16, 2021), the “config watcher” (the mechanism that automatically reloads the ``config.json`` file) has been deprecated in favor of the `mmctl config reload command <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-config-reload>`__ that must be run to apply configuration changes after they're made. This change will improve configuration performance and robustness.

   See the `Deprecated configuration settings documentation <https://docs.mattermost.com/configure/deprecated-configuration-settings.html>`__ for details on all deprecated Mattermost configuration settings.  

Configuration in Database
--------------------------

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Storing configuration in the database is supported from v5.10 and later. Please see more information on how to set this up `here <https://docs.mattermost.com/configure/configuation-in-mattermost-database.html>`_.

Environment Variables
---------------------

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Starting from Mattermost v3.8, you can use environment variables to manage the configuration. Environment variables override settings in ``config.json``. If a change to a setting in ``config.json`` requires a restart for it to take effect, then changes to the corresponding environment variable also require a server restart.

The name of the environment variable for any setting can be derived from the name of that setting in ``config.json``. For example, to derive the name of the Site URL setting:

1. Find the setting in ``config.json``. In this case, *ServiceSettings.SiteURL*.
2. Add ``MM_`` to the beginning and convert all characters to uppercase and replace the ``.`` with ``_``. For example, *MM_SERVICESETTINGS_SITEURL*.
3. The setting becomes ``export MM_SERVICESETTINGS_SITEURL="http://example.com"``.

Finally, if a setting is configured through an environment variable, modifying it in the System Console is disabled.

For any setting that is not set in ``config.json`` or in environment variables, the Mattermost server uses the default value as documented in the sections below.

.. note::
   If a setting is set through an environment variable and any other changes are made in the System Console, the value stored of the environment variable will be written back to the ``config.json`` as that setting's value.

.. warning::
   
   - Environment variables for Mattermost settings that are set within the active shell will take effect when migrating configuration. For more information, see `Configuration In Database <https://docs.mattermost.com/configure/configuation-in-mattermost-database.html>`_.
   - Database connection strings for the database read and search replicas need to be formatted using `URL encoding <https://www.w3schools.com/tags/ref_urlencode.asp>`__. Incorrectly formatted strings may cause some characters to terminate the string early, resulting in issues when the connection string is parsed.
   
Override Mattermost License File
--------------------------------

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Starting from Mattermost v5.26, you can use an environment variable to override any license in the database or file configuration without replacing those licenses.

When starting the server, specify the license key as ``MM_LICENSE`` with the contents of a license file.

.. note::
   If ``MM_LICENSE`` is set to a non-empty string, but the license specified is not valid, the Mattermost server will be started without a license.
   
   In a High Availability deployment, using an environment variable to override a server license only affects the individual app server and doesn't propagate to other servers in the cluster.

Load Custom Configuration Defaults
----------------------------------

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Starting from Mattermost v5.30, you can load a set of custom configuration defaults using an environment variable. This custom configuration applies only if the values are not already present in the current server configuration.

1. Create a JSON file that contains the custom configuration defaults. For example, ``custom.json``.
2. When starting the server, point the custom defaults environment variable to the defaults file: ``MM_CUSTOM_DEFAULTS_PATH=custom.json``.

.. contents::
  :depth: 2
  :local:
  :backlinks: entry

About
-----

Settings for managing the edition and license for Mattermost Enterprise Edition.

Edition and License
~~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **About > Edition and License**.

Edition
^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

View the edition of the Mattermost deployment.

License
^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

View subscription details including the number of users and expiry date of your Mattermost license.

License Key
^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Upload or remove license files. For more information on Mattermost Licensing, please see our `frequently asked questions about licensing <https://docs.mattermost.com/about/licensing-and-subscription.html>`_.

Reporting
---------

View statistics for your overall deployment and specific teams as well as access server logs. Access the following configuration settings in the System Console by going to **Reporting**.

Site Statistics
~~~~~~~~~~~~~~~

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

View statistics on active users, teams, channels, sessions, webhooks, and connections.

Team Statistics
~~~~~~~~~~~~~~~~

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

View statistics per team on the number of active users, as well as Public and Private channels.

Server Logs
~~~~~~~~~~~~

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

User Management
---------------

Settings for managing users, user access, groups, and permissions. 

Users
~~~~~~

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

View and manage active and inactive users, and revoke all user sessions. Access individual users to view their User ID, and view the teams they are on and what their role is on a team. Additionally, add the user to other teams without direct access to the team.

Groups
~~~~~~

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Groups offer System Admins a way to manage default teams and channels by linking AD/LDAP groups to Mattermost groups. See `Groups documentation <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`__ for more details.

Teams
~~~~~~

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Manage group synchronization on teams. See `Using AD/LDAP Synchronized Groups to Manage Team or Private Channel Membership <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html#using-ad-ldap-group-synchronization>`__ for more details.

Channels 
~~~~~~~~~

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Manage group synchronization on channels. See `Using AD/LDAP Synchronized Groups to Manage Team or Private Channel Membership <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html#using-ad-ldap-group-synchronization>`__ for more details.

Permissions
~~~~~~~~~~~

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20*

Advanced permissions offer System Admins a way to restrict actions in Mattermost to authorized users only. See `permissions documentation <https://docs.mattermost.com/onboard/advanced-permissions.html>`__ for more details.

Environment
-----------

Settings for configuring the network environment in which Mattermost is deployed.

Web Server
~~~~~~~~~~

Changes to properties in this section require a server restart before taking effect. Access the following configuration settings in the System Console by going to **Environment > Web Server**.


Site URL
^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The URL that users will use to access Mattermost. The port number is required if it's not a standard port such as 80 or 443.

**This field is required in Mattermost v3.8 and later.**

In Mattermost v5.1 and later, the URL may contain a subpath, such as ``"https://example.com/company/mattermost"``.

If Site URL is not set, the following features will not operate correctly:

- Email notifications will contain broken links, and email batching will not work.
- Authentication via OAuth 2.0, including GitLab, Google, and Office 365, will fail.
- Plugins may not work as expected.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SiteURL": ""`` with string input.                                    |
+-------------------------------------------------------------------------------------------------------------------+

Test Live URL
^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This button confirms that the value entered into the Site URL is valid and live.

Listen Address
^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The address and port to which to bind and listen. Specifying ":8065" will bind to all network interfaces. Specifying ``127.0.0.1:8065`` will only bind to the network interface having that IP address.

If you choose a port of a lower level (called "system ports" or "well-known ports", in the range of 0-1023), you must have permissions to bind to that port.

On Linux you can use: ``sudo setcap cap_net_bind_service=+ep /opt/mattermost/bin/mattermost`` to allow Mattermost to bind to well-known ports.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ListenAddress": ":8065"`` with string input. |
+-------------------------------------------------------------------------------------------+

Forward port 80 to 443
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Forwards all insecure traffic from port 80 to secure port 443.

**False**: When using a proxy such as NGINX in front of Mattermost this setting is unnecessary and should be set to ``false``.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Forward80To443": false`` with options ``true`` and ``false``.                 |
+----------------------------------------------------------------------------------------------------------------------------+

Connection Security
^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**None**: Mattermost will connect over an unsecured connection.

**TLS**: Encrypts the communication between Mattermost clients and your server. See `documentation <https://docs.mattermost.com/install/config-tls-mattermost.html>`__ for more details.

+---------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ConnectionSecurity": ""`` with options ``""`` and ``"TLS"``.                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------+

TLS Certificate File
^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The path to the certificate file to use for TLS connection security.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TLSCertFile": ""`` with string input. |
+------------------------------------------------------------------------------------+

TLS Key File
^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The path to the TLS key file to use for TLS connection security.

+-----------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TLSKeyFile": ""`` with string input. |
+-----------------------------------------------------------------------------------+

Use Let's Encrypt
^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enable the automatic retrieval of certificates from Let's Encrypt. The certificate will be retrieved when a client attempts to connect from a new domain. This will work with multiple domains. See :doc:`../install/config-tls-mattermost` for more details on setting up Let's Encrypt.

**False**: Manual certificate specification based on the **TLS Certificate File** and **TLS Key File** specified above.

+---------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UseLetsEncrypt": false`` with options ``true`` and ``false``.                      |
+---------------------------------------------------------------------------------------------------------------------------------+

.. note::
   If Let's Encrypt is enabled, forward port 80 through a firewall, with `Forward80To443 <https://docs.mattermost.com/configure/configuration-settings.html#forward-port-80-to-443>`__ ``config.json`` setting set to ``true`` to complete the Let's Encrypt certification.

Let's Encrypt Certificate Cache File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The path to the file where certificates and other data about the Let's Encrypt service will be stored.

+-----------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LetsEncryptCertificateCacheFile": "./config/letsencrypt.cache"`` with string input.  |
+-----------------------------------------------------------------------------------------------------------------------------------+

Read Timeout
^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Maximum time allowed from when the connection is accepted to when the request body is fully read.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ReadTimeout": 300`` with numerical input. |
+----------------------------------------------------------------------------------------+

Write Timeout
^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

If using HTTP (insecure), this is the maximum time allowed from the end of reading the request headers until the response is written. If using HTTPS, it is the total time from when the connection is accepted until the response is written.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"WriteTimeout": 300`` with numerical input. |
+-----------------------------------------------------------------------------------------+

Idle Timeout
^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Set an explicit idle timeout in the HTTP server. This is the maximum time allowed before an idle connection is disconnected.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdleTimeout": 60`` with numerical input.   |
+-----------------------------------------------------------------------------------------+

Webserver Mode
^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

gzip compression applies to the HTML, CSS, Javascript, and other static content files that make up the Mattermost web client. We recommend you enable gzip to improve performance unless your environment has specific restrictions, such as a web proxy that distributes gzip files poorly.

**gzip**: The Mattermost server will serve static files compressed with gzip to improve performance.

**Uncompressed**: The Mattermost server will serve static files uncompressed.

**Disabled**: The Mattermost server will not serve static files.

+----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"WebserverMode": "gzip"`` with options ``"gzip"``, ``"uncompressed"``, and ``"disabled"``. |
+----------------------------------------------------------------------------------------------------------------------------------------+

Enable Insecure Outgoing Connections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Outgoing HTTPS requests can accept unverified, self-signed certificates. For example, outgoing webhooks to a server with a self-signed TLS certificate, using any domain, will be allowed.

**False**: Only secure HTTPS requests are allowed.

.. important::
   Security note: Enabling this feature makes these connections susceptible to man-in-the-middle attacks.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableInsecureOutgoingConnections": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------+

Managed Resource Paths
^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

A comma-separated list of paths within the Mattermost domain that are managed by a third-party service instead of Mattermost itself. Links to these paths will be opened in a new tab/window by Mattermost apps. For example, if Mattermost is running on ``https://mymattermost.com``, setting this to ``conference`` will cause links such as ``https://mymattermost.com/conference`` to be opened in a new window.

When using the Mattermost Desktop App, additional configuration is required to open the link within the Desktop App instead of in a browser. See `here <https://docs.mattermost.com/install/desktop-managed-resources.html>`_ for more information.

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ManagedResourcePaths": ""`` with string input. |
+---------------------------------------------------------------------------------------------+

Reload Configuration from Disk
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

The workflow for failover without downing the server is to change the database line in the ``config.json`` file, select **Reload Configuration from Disk**, then select **Recycle Database Connections** in the **Database** section.

Purge All Caches
^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This button purges all the in-memory caches for sessions, accounts, and channels. Deployments using High Availability will attempt to purge all the servers in the cluster. Purging the caches may adversely impact performance.

Database
~~~~~~~~

Changes to properties in this section require a server restart before taking effect. Access the following configuration settings in the System Console by going to **Environment > Database**.

Driver Name
^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting can only be changed from ``config.json`` file, it cannot be changed from the System Console user interface.

**mysql**: Enables driver to MySQL database.

**postgres**: Enables driver to PostgreSQL database.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DriverName": "mysql"`` with string input. |
+----------------------------------------------------------------------------------------+

Data Source
^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This is the connection string to the master database. This setting can only be changed from the ``config.json`` file. 

.. note::
   
   To enable SSL, add ``&tls=true`` to your database connection string if your SQL driver supports it. Add ``&tls=skip-verify`` if you use self-signed certificates.

**MySQL Database**

When **DriverName** is set to ``mysql``, using ``collation`` is recommended over using ``charset``. 

To specify collation:

.. code-block:: none

  "SqlSettings": {
      "DataSource": "<user:pass>@<servername>/mattermost?charset=utf8mb4,utf8&collation=utf8mb4_general_ci",
      [...]
    }

If collation is omitted, the default collation, ``utf8mb4_general_ci`` is used:

.. code-block:: none

  "SqlSettings": {
      "DataSource": "<user:pass>@<servername>/mattermost?charset=utf8mb4,utf8",
      [...]
    }

.. note::
   
   If you're using MySQL 8.0 or later, the default collation has changed to ``utf8mb4_0900_ai_ci``. See our `Database Software Requirements <https://docs.mattermost.com/install/requirements.html#database-software>`__ documentation for details on MySQL 8.0 support.
   
**PostgreSQL Database**

When **DriverName** is set to ``postgres``, use a connection string in the form ``postgres://mmuser:password@localhost:5432/mattermost_test?sslmode=disable&connect_timeout=10``. 

+-----------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DataSource": ""`` with string input. |
+-----------------------------------------------------------------------------------+

Maximum Idle Connections
^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The maximum number of idle connections held open to the database.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxIdleConns": 10`` with numerical input. |
+----------------------------------------------------------------------------------------+

Maximum Connection Idle Timeout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The maximum time a database connection can remain idle.

+------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ConnMaxIdleTimeMilliseconds": 5`` with numerical input. |
+------------------------------------------------------------------------------------------------------+

Maximum Open Connections
^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The maximum number of open connections held open to the database.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxOpenConns": 300`` with numerical input. |
+-----------------------------------------------------------------------------------------+

Query Timeout
^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The number of seconds to wait for a response from the database after opening a connection and sending the query. Errors that you see in the UI or in the logs as a result of a query timeout can vary depending on the type of query.

+-------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"QueryTimeout": 30`` with numerical input.                                  |
+-------------------------------------------------------------------------------------------------------------------------+

Disable Database Search
^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Disables the use of the database to perform searches. Should only be used when other `search engines  <https://docs.mattermost.com/scale/elasticsearch.html>`_ are configured. If this setting is set to ``true`` and another search engine is not configured, it will result in empty search results.

**False**: Database search is not disabled.

+-------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DisableDatabaseSearch": false`` with options ``true`` and ``false``.       |
+-------------------------------------------------------------------------------------------------------------------------+

Maximum Connection Lifetime
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Maximum lifetime for a connection to the database, in milliseconds. Use this setting to configure the maximum amount of time a connection to the database may be reused. Defaults to an hour (3,600,000 milliseconds).

+-------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ConnMaxLifetimeMilliseconds": 3600000`` with numerical input.              |
+-------------------------------------------------------------------------------------------------------------------------+

Minimum Hashtag Length
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The minimum number of characters in a hashtag. This must be greater than or equal to 2. MySQL databases must be configured to support searching strings shorter than three characters, see `documentation <https://dev.mysql.com/doc/refman/8.0/en/fulltext-fine-tuning.html>`_.

+-------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MinimumHashtagLength": 3`` with numerical input.                           |
+-------------------------------------------------------------------------------------------------------------------------+

At Rest Encrypt Key
^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

A 32-character key for encrypting and decrypting sensitive fields in the database. You can generate your own cryptographically random alphanumeric string, or you can go to **System Console > Environment > Database** and select **Regenerate**, which displays the value until you select **Save**.

When using High Availability, the salt must be identical in each instance of Mattermost.

No fields are encrypted using ``AtRestEncryptKey``. It's a legacy setting used to encrypt data stored at rest in the database.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AtRestEncryptKey": ""`` with string input.  |
+------------------------------------------------------------------------------------------+

SQL Statement Logging (Trace)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Executing SQL statements are written to the log for development.

**False**: SQL statements are not written to the log.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Trace": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------+

Recycle Database Connections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This button reconnects to the database listed in the configuration settings. All old connections are closed after 20 seconds.

The workflow for failover without downing the server is to change the database line in the ``config.json`` file, select **Reload Configuration from Disk** in the **Environment > Database** section, then select **Recycle Database Connections**.

Elasticsearch
~~~~~~~~~~~~~~

Changes to properties in this section require a server restart before taking effect. Access the following configuration settings in the System Console by going to **Environment > Elasticsearch**.


Enable Elasticsearch Indexing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: Indexing of new posts occurs automatically. Search queries will use database search until **Enable Elasticsearch for search queries** is enabled. `Learn more about Elasticsearch in our documentation <https://docs.mattermost.com/scale/elasticsearch.html/>`__.

**False**: Elasticsearch indexing is disabled and new posts are not indexed. If indexing is disabled and re-enabled after an index is created, we recommend you purge and rebuild the index to ensure complete search results.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableIndexing": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

Server Connection Address
^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

The address of the Elasticsearch server. `Learn more about Elasticsearch in our documentation <https://docs.mattermost.com/scale/elasticsearch.html/>`__.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ConnectionUrl": ""`` with string input.                                   |
+------------------------------------------------------------------------------------------------------------------------+

Skip TLS Verification
^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: Skips the certificate verification step for TLS connections. Not recommended for production environments where TLS is required. For testing only.

**False**: Mattermost does not skip certificate verification.

+-------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SkipTLSVerification": false`` with boolean input.        |
+-------------------------------------------------------------------------------------------------------+

Server Username
^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

(Optional) The username to authenticate to the Elasticsearch server.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Username": ""`` with string input.                                   |
+-------------------------------------------------------------------------------------------------------------------+

Server Password
^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

(Optional) The password to authenticate to the Elasticsearch server.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Password": ""`` with string input.                                   |
+-------------------------------------------------------------------------------------------------------------------+

Enable Cluster Sniffing
^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: Sniffing finds and connects to all data nodes in your cluster automatically.

**False**: Sniffing is disabled.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Sniff": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------+

Bulk Indexing
^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This button starts a bulk index of all existing posts in the database. If the indexing process is cancelled the index and search results will be incomplete.

Purge Indexes
^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This button purges the entire Elasticsearch index. Typically only used if the index has corrupted and search is not behaving as expected. After purging the index a new index can be created with the **Bulk Index** button.

Enable Elasticsearch for Search Queries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: Elasticsearch will be used for all search queries using the latest index. Search results may be incomplete until a bulk index of the existing post database is finished.

**False**: Database search is used for search queries.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSearching": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

Enable Elasticsearch for Autocomplete Queries
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: Elasticsearch will be used for all autocompletion queries on users and channels using the latest index. Autocompletion results may be incomplete until a bulk index of the existing users and channels database is finished.

**False**: Database autocomplete is used.

+----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAutocomplete": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------+

File Storage
~~~~~~~~~~~~

Mattermost currently supports storing files on the local filesystem and Amazon S3 or S3 compatible containers. Access the following configuration settings in the System Console by going to **Environment > File Storage**.

.. note::
  We have tested Mattermost with `MinIO <https://www.minio.io/>`__ and `Digital Ocean Spaces <https://docs.digitalocean.com/products/spaces/>`_ products, but not all S3 compatible containers on the market. If you are looking to use other S3 compatible containers we advise completing your own testing.

File Storage System
^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

+-------------------------+-----------------------+
| ``config.json`` setting | ``DriverName``        |
+-------------------------+-----------------------+
| Allowed Values          | ``"local"`` (default) |
|                         | ``"amazons3"``        |
+-------------------------+-----------------------+

This selects which file storage system is used: Local File System or Amazon S3.

**Local File System**: Files and images are stored in the specified local file directory.

**Amazon S3**: Files and images are stored on Amazon S3 based on the provided access key, bucket, and region fields. The ``"amazons3"`` driver is compatible with MinIO (Beta) and Digital Ocean Spaces based on the provided access key, bucket, and region fields.

Local Storage Directory
^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The local directory to which files are written when the File Storage System is set to ``"local"``. This is relative to the directory Mattermost is installed to and defaults to ``"./data"`` When File Storage System is set to S3 this setting has no effect.

+-------------------------+------------------------------------------------------------------------------------------+
| ``config.json`` setting | ``Directory``                                                                            |
+-------------------------+------------------------------------------------------------------------------------------+
| Allowed Values          | Any directory writeable by the user Mattermost is running as. Defaults to ``"./data/"``. |
+-------------------------+------------------------------------------------------------------------------------------+

Maximum File Size
^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Maximum file size for message attachments and plugins entered in megabytes in the System Console. Converted to bytes in ``config.json`` at 1048576 bytes per megabyte.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxFileSize": 104857600`` with numerical input.                  |
+---------------------------------------------------------------------------------------------------------------+

.. warning:: Verify server memory can support your setting choice. Large file sizes increase the risk of server crashes and failed uploads due to network disruptions.

.. note::
  If you use a proxy or load balancer in front of Mattermost its settings need to be adjusted accordingly. For NGINX use ``client_max_body_size``. For Apache use ``LimitRequestBody``.
  
Enable Document Search by Content
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Enable users to search the contents of documents attached to messages. 

**True**: Documents are searchable by their content.  

.. note::
   Document content search results for files shared before upgrading to Mattermost Server 5.35 may be incomplete until an `mmctl content extraction job <https://docs.mattermost.com/manage/mmctl-command-line-tool.html#mmctl-extract>`__ is run, or an `extraction command is executed using the CLI <https://docs.mattermost.com/manage/command-line-tools.html>`__. If this command is not run, users can search older files based on file name only.

**False**: Documents aren't searchable by their content. When document content search is disabled, users can search for files by filename only.

+---------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileSettings.ExtractContent": true`` with options ``true`` and ``false``.          |
+---------------------------------------------------------------------------------------------------------------------------------+

In addition, you can optionally install `these dependencies <https://github.com/sajari/docconv#dependencies>`__ to extend content searching support to include file formats beyond PDF, DOCX, and ODT, such as DOC, RTF, XML, HTML, and PAGES. If you choose not to install the dependencies, you will see log entries for documents that couldn't be extracted. Any documents that can't be extracted are skipped and logged so that content extraction can proceed. The search support each dependency offers is described below: 

- ``tidy``: Used to search the contents of HTML and PAGES documents.
- ``wv``: Used to search the contents of DOC documents.
- ``popplerutils``: Used to significantly improve server performance when extracting the contents of PDF documents.
- ``unrtf``: Used to search the contents of RTF documents.
- ``Justtext``: Used to search HTML documents.

.. note::
  - Document content search is available in Mattermost Server from v5.35, with mobile support coming soon. 
  - Searching document contents adds load to your server. 
  - For large deployments, or teams that share many large, text-heavy documents, we recommended you review our `hardware requirements <https://docs.mattermost.com/install/software-hardware-requirements.html#hardware-requirements>`__, and test enabling this feature in a staging environment before enabling it in a production environment.
  
Enable Searching Content of Documents within ZIP Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This configuration setting enables users to search the contents of compressed ZIP files attached to messages.

**True**: Contents of documents within ZIP files are returned in search results. This may have an impact on server performance for large files.

**False**: The contents of documents within ZIP files aren't returned in search results.

+---------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileSettings.ArchiveRecursion": false`` with options ``true`` and ``false``.       |
+---------------------------------------------------------------------------------------------------------------------------------+

.. note::
  - Document content search within ZIP files is available in Mattermost Server from v5.35, with mobile support coming soon. 
  - Searching document contents adds load to your server. 
  - For large deployments, or teams that share many large, text-heavy documents, we recommended you review our `hardware requirements <https://docs.mattermost.com/install/software-hardware-requirements.html#hardware-requirements>`__, and test enabling this feature in a staging environment before enabling it in a production environment.

Amazon S3 Bucket
^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The name of the bucket for your S3-compatible object storage instance.

+-------------------------+----------------------------------------------+
| ``config.json`` setting | ``AmazonS3Bucket``                           |
+-------------------------+----------------------------------------------+
| Allowed Values          | A string with the S3-compatible bucket name. |
+-------------------------+----------------------------------------------+

Amazon S3 Region
^^^^^^^^^^^^^^^^^

The AWS region you selected when creating your S3 bucket. If no region is set, Mattermost attempts to get the appropriate region from AWS and sets it to ``"us-east-1"`` if none is found. For MinIO or Digital Ocean Spaces, leave this setting empty.

+-------------------------+-----------------------------------------------------+
| ``config.json`` setting | ``AmazonS3Region``                                  |
+-------------------------+-----------------------------------------------------+
| Allowed Values          | A string with the AWS region containing the bucket. |
+-------------------------+-----------------------------------------------------+

Amazon S3 Access Key ID
^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This is required for access unless you are using an `Amazon S3 IAM Role <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html>`__ with Amazon S3. Your EC2 administrator can supply you with the Access Key ID.

+-------------------------+----------------------------------------------------------------------+
| ``config.json`` setting | ``AmazonS3AccessKeyId``                                              |
+-------------------------+----------------------------------------------------------------------+
| Allowed Values          | A string with the access key for the S3-compatible storage instance. |
+-------------------------+----------------------------------------------------------------------+

Amazon S3 Endpoint
^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The hostname of your S3-compatible instance. Defaults to ``"s3.amazonaws.com"``.

.. note::
  For Digital Ocean Spaces, the hostname should be set to ``"<region>.digitaloceanspaces.com"``, where ``<region>`` is the abbreviation for the region you chose when setting up the Space. It can be ``nyc3``, ``ams3``, or ``sgp1``.

+-------------------------+-------------------------------------------------------------------+
| ``config.json`` setting | ``AmazonS3Endpoint``                                              |
+-------------------------+-------------------------------------------------------------------+
| Allowed Values          | A string with the hostname of the S3-compatible storage instance. |
+-------------------------+-------------------------------------------------------------------+

Amazon S3 Secret Access Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The secret access key associated with your Amazon S3 Access Key ID.

+-------------------------+-----------------------------------------------------------------------------+
| ``config.json`` setting | ``AmazonS3SecretAccessKey``                                                 |
+-------------------------+-----------------------------------------------------------------------------+
| Allowed Values          | A string with the secret access key for the S3-compatible storage instance. |
+-------------------------+-----------------------------------------------------------------------------+

Enable Secure Amazon S3 Connections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables only secure Amazon S3 connections.

**False**: Allows insecure connections to Amazon S3.

+-------------------------+----------------------------------------------+
| ``config.json`` setting | ``AmazonS3SSL``                              |
+-------------------------+----------------------------------------------+
| Allowed Values          | ``true`` or ``false``. Defaults to ``true``. |
+-------------------------+----------------------------------------------+

Enable Server-Side Encryption for Amazon S3
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: Encrypts files in Amazon S3 using server-side encryption with `Amazon S3-managed keys <https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html>`__.

**False**: Doesn't encrypt files in Amazon S3.

.. note::
  Server-side encryption only works with Amazon S3.

+-------------------------+-----------------------------------------------+
| ``config.json`` setting | ``AmazonS3SSE``                               |
+-------------------------+-----------------------------------------------+
| Allowed Values          | ``true`` or ``false``. Defaults to ``false``. |
+-------------------------+-----------------------------------------------+

Enable Amazon S3 Debugging
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Log additional debugging information to the system logs. Typically set to ``false`` in production.

**False**: No Amazon S3 debugging information is included in the system logs.

+-------------------------+-----------------------------------------------+
| ``config.json`` setting | ``AmazonS3Trace``                             |
+-------------------------+-----------------------------------------------+
| Allowed Values          | ``true`` or ``false``. Defaults to ``false``. |
+-------------------------+-----------------------------------------------+

Test Connection
^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Ensures that the user can access the server and that the settings are valid.

Image Proxy
~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Environment > Image Proxy**.

Enable Image Proxy
^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

When ``true``, enables an image proxy for loading external images. The image proxy is used by the Mattermost apps to prevent them from connecting directly to remote servers. This anonymizes their connections and prevents them from accessing insecure content.

See the `image proxy <https://docs.mattermost.com/deploy/image-proxy.html#image-proxy>`__ documentation to learn more.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": true`` with options ``true`` and ``false``.                   |
+---------------------------------------------------------------------------------------------------------------------+

Image Proxy Type
^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The type of image proxy used by Mattermost. There are two options:

**local**: The Mattermost server itself acts as the image proxy. This is the default option.

**atmos/camo**: An external `atmos/camo <https://github.com/atmos/camo>`__ image proxy is used.

See the `documentation <https://docs.mattermost.com/deploy/image-proxy.html#atmos-camo-image-proxy>`__ to learn more.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ImageProxyType": "local"``, with options ``"local"`` and ``"atmos/camo"`` for the above settings, respectively. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

Remote Image Proxy URL
^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The URL of the ``atmos/camo`` proxy. This setting is not needed when using the local image proxy.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RemoteImageProxyURL": ""`` with string input.                          |
+---------------------------------------------------------------------------------------------------------------------+

Remote Image Proxy Options
^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The URL signing key passed to an ``atmos/camo`` image proxy. This setting is not needed when using the local image proxy.

See the `documentation <https://docs.mattermost.com/deploy/image-proxy.html#atmos-camo-image-proxy>`_ to learn more.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RemoteImageProxyOptions": ""`` with string input.                      |
+---------------------------------------------------------------------------------------------------------------------+

SMTP
~~~~

Access the following configuration settings in the System Console by going to **Environment > SMTP**.

SMTP Email Server
^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Location of SMTP email server used for email notifications.

+-----------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SMTPServer": ""`` with string input. |
+-----------------------------------------------------------------------------------+

SMTP Server Port
^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Port of SMTP email server.

+---------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SMTPPort": ""`` with string input. |
+---------------------------------------------------------------------------------+

SMTP Server Timeout
^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The maximum amount of time (in seconds) allowed for establishing a TCP connection between Mattermost and the SMTP server, to be idle before being terminated.

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SMTPServerTimeout": 10`` with numerical input. |
+---------------------------------------------------------------------------------------------+

Enable SMTP Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: SMTP username and password are used for authenticating to the SMTP server.

**False**: Mattermost doesn't attempt to authenticate to the SMTP server.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSMTPAuth": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

SMTP Server Username
^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The username for authenticating to the SMTP server.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SMTPUsername": ""`` with string input. |
+-------------------------------------------------------------------------------------+

SMTP Server Password
^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The password associated with the SMTP username.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SMTPPassword": ""`` with string input. |
+-------------------------------------------------------------------------------------+

.. _email-tls:

Connection Security
^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**None**: Send email over an unsecure connection.

**TLS**: Communication between Mattermost and your email server is encrypted.

**STARTTLS**: Attempts to upgrade an existing insecure connection to a secure connection using TLS.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ConnectionSecurity": ""`` with options ``""``, ``"TLS"``, and ``"STARTTLS"``. |
+----------------------------------------------------------------------------------------------------------------------------+

Skip Server Certificate Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Mattermost will not verify the email server certificate.

**False**: Mattermost will verify the email server certificate.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SkipServerCertificateVerification": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------+

Enable Security Alerts
^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enable System Admins to be notified by email if a relevant security fix alert is announced. Requires email to be enabled. To learn more about this feature, see :doc:`../manage/telemetry`.

**False**: Security alerts are disabled.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSecurityFixAlert": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

Push Notification Server
~~~~~~~~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Environment > Push Notification Server**.

Enable Push Notifications
^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Your Mattermost server sends mobile push notifications to the server specified in **PushNotificationServer**.

**False**: Mobile push notifications are disabled.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SendPushNotifications": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

Push Notification Server
^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Location of Mattermost Push Notification Service (MPNS), which re-sends push notifications from Mattermost to services like Apple Push Notification Service (APNS) and Google Cloud Messaging (GCM).

To confirm push notifications are working, connect to the `Mattermost iOS App on iTunes <https://apps.apple.com/us/app/mattermost/id1257222717>`__ or the `Mattermost Android App on Google Play <https://play.google.com/store/apps/details?id=com.mattermost.rn>`__:

- For Enterprise or Professional Edition, enter ``https://push.mattermost.com`` for the push notification server hosted in the United States. If you prefer to use a push notification server hosted in Germany, enter ``https://hpns-de.mattermost.com/``.
- For Team Edition, enter ``https://push-test.mattermost.com``.

Please review full documentation on `push notifications and mobile applications <https://docs.mattermost.com/deploy/mobile-hpns.html#mobile-push-notifications>`__ including guidance on compiling your own mobile apps and MPNS before deploying to production.

.. note::
  The ``https://push-test.mattermost.com`` server is provided for testing push notifications prior to compiling your own service. Please make sure `to read about its limitations <https://docs.mattermost.com/deploy/mobile-hpns.html#test-push-notifications-service-tpns>`_.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PushNotificationServer": "https://push-test.mattermost.com"`` with string input. |
+-------------------------------------------------------------------------------------------------------------------------------+

Max Notifications Per Channel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Maximum total number of users in a channel before @all, @here, and @channel no longer send notifications to maximize performance.

If you want to increase this value, we recommend increasing it a little at a time and monitor system health with `performance monitoring metrics <https://docs.mattermost.com/scale/performance-monitoring.html>`__. We also recommend only increasing this value if large channels have restricted permissions for who can post to the channel (for instance, a read-only Town Square channel).

+--------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxNotificationsPerChannel": 1000`` with numerical input. |
+--------------------------------------------------------------------------------------------------------+

**Troubleshooting Push Notifications**

To confirm push notifications are working:

1. Go to **System Console > Notifications > Environment > Push Notification Server > Enable Push Notifications** and select **Use TPNS connection to send notifications to iOS and Android apps**.
2. Set **Push Notification Server** to ``https://push.mattermost.com`` if using Enterprise Edition. If using Team Edition, set the value to ``https://push-test.mattermost.com``.
3. To confirm push notifications are working, connect to the `Mattermost iOS App on iTunes <https://about.mattermost.com/mattermost-ios-app>`__ or the `Mattermost Android App on Google Play <https://about.mattermost.com/mattermost-android-app>`__ and log in to your team site.
4. Close the app on your device, and close any other connections to your team site.
5. Wait 5 minutes and have another team member send you a direct message, which should trigger a push notification to the Mattermost app on your mobile device.
6. You should receive a push notification on your device alerting you of the direct message.

If you did not receive an alert:

1. Set **System Console > Environment > Logging > File Log Level** to *DEBUG* (make sure to set this back to *INFO* after troubleshooting to save disk space).
2. Repeat the above steps.
3. Go to **System Console > Reporting > Server Logs** and copy the log output into a file.
4. For Enterprise Edition customers, `submit a support request with the file attached <https://mattermost.zendesk.com/hc/en-us/requests/new>`__. For Team Edition users, please start a thread in the `troubleshooting forum <https://forum.mattermost.org/t/how-to-use-the-troubleshooting-forum/150>`__ for peer-to-peer support.

.. _high-availability:

High Availability
~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Environment > High Availability**.

Changes to properties in this section require a server restart before taking effect.

When High Availability mode is enabled, the System Console is set to read-only and settings can only be changed by editing the configuration file directly. However, for testing and validating a High Availability setup, you can set ``ReadOnlyConfig`` to ``false``, which allows changes made in the System Console to be saved back to the configuration file.

To learn more about configuring High Availability, see `High Availability Cluster <https://docs.mattermost.com/scale/high-availability-cluster.html>`_.

Enable High Availability Mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: The Mattermost server will attempt inter-node communication with the other servers in the cluster that have the same cluster name. This sets the System Console to read-only mode to keep the servers ``config.json`` files in sync.

**False**: Mattermost High Availability is disabled.

+-----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``.  |
+-----------------------------------------------------------------------------------------------------+

Cluster Name
^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

The cluster to join by name. Only nodes with the same cluster name will join together. This is to support Blue-Green deployments or staging pointing to the same database.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ClusterName": ""`` with string input. |
+------------------------------------------------------------------------------------+

Override Hostname
^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

If blank, Mattermost attempts to get the hostname from the OS or use the IP address. You can override the hostname of this server with this property. It is not recommended to override the hostname unless needed. This property can also be set to a specific IP address if needed. Also see `cluster discovery <https://docs.mattermost.com/scale/high-availability-cluster.html>`_ for more details.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"OverrideHostname": ""`` with string input. |
+-----------------------------------------------------------------------------------------+

Use IP Address
^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: The cluster attempts to communicate using the IP address.

**False**: The cluster attempts to communicate using the hostname.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UseIpAddress": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+

Use Gossip
^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

.. note::
   All cluster traffic uses the gossip protocol. From Mattermost Server v5.36 gossip clustering can no longer be disabled.

**True**: The server attempts to communicate via the gossip protocol over the gossip port.

**False**: The server attempts to communicate over the streaming port.

.. note::
   The gossip port and gossip protocol are used to determine cluster health even when this setting is ``false``.

+--------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UseExperimentalGossip": true`` with options ``true`` and ``false``.         |
+--------------------------------------------------------------------------------------------------------------------------+

Enable Experimental Gossip Encryption
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: All communication through the cluster using the gossip protocol will be encrypted.

**False**: All communication using gossip protocol remains unencrypted.

The encryption uses AES-256 by default, and it is not kept configurable by design. However, you can manually set the ``ClusterEncryptionKey`` row value in the Systems table. A key is a byte array converted to base64. It should be either 16, 24, or 32 bytes to select AES-128, AES-192, or AES-256.

+--------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableExperimentalGossipEncryption": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------------------+    
    
Enable Gossip Compression
^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: All communication through the cluster uses gossip compression. This is set to ``true`` by default to maintain compatibility with older servers.

**False**: All communication using the gossip protocol remains uncompressed. Once all servers in a cluster are upgraded to Mattermost v5.33 or later, we recommend that you disable this configuration setting for better performance.

+--------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableGossipCompression": true`` with options ``true`` and ``false``.             |
+--------------------------------------------------------------------------------------------------------------------------------+    

Gossip Port
^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

The port used for the gossip protocol. Both UDP and TCP should be allowed on this port.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GossipPort": 8074`` with numerical input.    |
+-------------------------------------------------------------------------------------------+

Streaming Port
^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

The port used for streaming data between servers.

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"StreamingPort": 8075`` with numerical input.    |
+----------------------------------------------------------------------------------------------+

Rate Limiting
~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Environment > Rate Limiting**.

Changes to properties in this section require a server restart before taking effect.

Enable Rate Limiting
^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Rate limiting prevents your server from being overloaded with too many requests. This decreases the risk and impact of third-party applications or malicious attacks on your server.

**True**: APIs are throttled at the rate specified by **PerSec**.

**False**: APIs are not throttled.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Maximum Queries per Second
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Throttle API at this number of requests per second if rate limiting is enabled.

The location of the log files. If blank, they are stored in the ``./logs`` directory. The path that you set must exist and Mattermost must have write permissions in it.

+----------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PerSec": 10`` with numerical input. |
+----------------------------------------------------------------------------------+

Maximum Burst Size
^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Typically set to ``true`` in production. When ``true``, logged events are written in a machine readable JSON format. Otherwise they are printed as plain text.

Maximum number of requests allowed beyond the per second query limit.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxBurst": 100`` with numerical input. |
+-------------------------------------------------------------------------------------+

Memory Store Size
^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Maximum number of user sessions connected to the system as determined by ``VaryByRemoteAddr`` and ``VaryByHeader`` variables.

Typically set to the number of users in the system.

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MemoryStoreSize": 10000`` with numerical input. |
+----------------------------------------------------------------------------------------------+

Vary rate limit by remote address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Rate limit API access by IP address. Recommended to set to ``true`` if you're using a proxy.

**False**: Rate limiting does not vary by IP address.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"VaryByRemoteAddr": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

Vary rate limit by user
^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Rate limit API access by user authentication token. Recommended to set to ``true`` if you're using a proxy.

**False**: Rate limiting does not vary by user authentication token.

+--------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"VaryByUser": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------+

Vary rate limit by HTTP header
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Vary rate limiting by HTTP header field specified (e.g. when configuring Ngnix set to ``X-Real-IP``, when configuring AmazonELB set to ``X-Forwarded-For``). Recommended to be set if you're using a proxy.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"VaryByHeader": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Advanced Logging 
~~~~~~~~~~~~~~~~

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Output logs to multiple targets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Allow any combination of console, local file, syslog, and TCP socket targets, and send log records to multiple targets. These targets have been chosen as they support the vast majority of log aggregators, and other log analysis tools, without needing additional software installed. Please see 'Audit Log v2 <https://docs.mattermost.com/comply/audit-log.html>`__ for more comprehensive documentation. 

System Admins can define multiple log targets to:

- Mirror log output to files and log aggregators for redundancy.
- Log certain entries to specific destinations. For example, all errors could be routed to a specific destination for review.

Additional configuration options include:

- Multiple local file targets: Supports rotation and compression triggered by size and/or duration.
- Multiple syslogs: Supports local and remote syslog servers, with or without TLS transport.
- Multiple TCP sockets: TCP socket target can be configured with an IP address or domain name, port, and optional TLS certificate.

All access to the REST API or CLI is audited. When using Advanced Logging for auditing, System Admins can capture the following auditing in the target configuration in addition to discrete log levels:

.. code-block:: none

   "Levels": [
      {"ID": 100, "Name": "audit-api"},
      {"ID": 101, "Name": "audit-content"},
      {"ID": 102, "Name": "audit-permissions"},
      {"ID": 103, "Name": "audit-cli"},
   ],

Where:

- ``audit-api``: Enables output of REST API calls.
- ``audit-content``: Enables output of API calls that generate content (e.g. ``create post``, ``create reaction``).
- ``audit-permissions``: Enables output of all permissions failures.
- ``audit-cli``: Enables output of legacy CLI calls.

.. note::

  - Logs are recorded asynchronously to reduce latency to the caller. 
  - Advanced logging supports hot-reloading of logger configuration.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature’s ``config.json`` setting is ``LogSettings.AdvancedLoggingConfig`` which can contain a filespec to another config file, a database DSN, or JSON.        |                                                        
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Options outlined in `this text file <https://github.com/mattermost/docs/files/5066579/Log.Settings.Options.txt>`__ are described in the following table.

+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| **Key**       | **Definition**                                                                                                                                         | **Type**    |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| **Levels**    |                                                                                                                                                        |             |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| ID            | Unique log level identifier. Must be registered in ``mattermost/mattermost-server/shared/mlog/levels.go``.                                             | int         |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Name          | Human-readable name for the log level identifier.                                                                                                      | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Stacktrace    | Set to ``true`` to generate a stacktrace. Set to ``false`` to prevent a stacktrace from being generated.                                               | bool        |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| **Targets**   |                                                                                                                                                        |             |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Type          | Can be one of: ``console``, ``file``, ``syslog``, or ``tcp``.                                                                                          | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Format        | Can be either ``json`` or ``plain``.                                                                                                                   | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Levels        | Array of log levels.                                                                                                                                   | []          |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Options       | Map of options specific to the target type.                                                                                                            | {}          |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| MaxQueueSize  | The number of audit records that can be queued/buffered at any point in time when writing to syslog. Default is 1000.                                  | int         |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| **Console**   |                                                                                                                                                        |             |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Out           | Can be either ``stdout`` or ``stderr``.                                                                                                                | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| **File**      |                                                                                                                                                        |             |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Filename      | Path and filename for logs.                                                                                                                            | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| MaxAgeDays    | Number of days until a rotation is triggered. Set to ``0`` to not rotate based on age.                                                                 | int         |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| MaxBackups    | Maximum number of rotated files to keep where the oldest are deleted. Set to ``0`` to discard rotated files.                                           | int         |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| MaxSizeMB     | Maximum file size before a rotation is triggered. Set to ``0`` to prevent rotation based on file size.                                                 | int         |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Compress      | Set to ``true`` to compress files after rotation. Set to ``false`` to not compress files after rotation.                                               | bool        |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| **SysLog**    |                                                                                                                                                        |             |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| IP            | IP address or domain of the syslog server.                                                                                                             | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Port          | Listening port of syslog server.                                                                                                                       | int         |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Tag           | Typically the program name, machine name, or node name.                                                                                                | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| TLS           | Set to ``true`` to connect via TLS. Set to ``false`` to prevent connecting via TLS.                                                                    | bool        |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Cert          | For TLS connections where TLS is set to ``true``, the filename of client certificate or base64-encoded certificate.                                    | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Insecure      | Used for testing purposes only. Set to ``true`` to prevent a certificate check from being performed. Set to ``false`` to perform a certificate check.  | bool        |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| **TCP**       |                                                                                                                                                        |             |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| IP            | IP address or domain of the socket server.                                                                                                             | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Port          | Listening port of the socket server.                                                                                                                   | int         |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| TLS           | Set to ``true`` to connect via TLS. Set to ``false`` to prevent connecting via TLS.                                                                    | bool        |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Cert          | For TLS connections where TLS is set to ``true``, the filename of client certificate or base64-encoded certificate.                                    | string      |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+
|               |                                                                                                                                                        |             |
| Insecure      | Used for testing purposes only. Set to ``true`` to prevent a certificate check from being performed. Set to ``false`` to perform a certificate check.  | bool        |
+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+-------------+

.. note::

    Filenames for ``AdvancedLoggingConfig`` can contain an absolute filename, a relative filename, or embedded JSON.

See the :download:`Advanced Logging Options Sample JSON ZIP file <../samples/advanced-logging-options-sample-json.zip>` for a sample configuration file. 

Standard Logging 
~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Environment > Logging**.

Output logs to console
^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

.. note::
   Logs are rotated once the log file reaches a size of 100 MB or more.

**True**: Output log messages to the console based on ``ConsoleLevel`` option. The server writes messages to the standard output stream (stdout).

**False**: Output log messages are not written to the console.

Changes to this setting require a server restart before taking effect.

+----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableConsole": true`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------+

Console Log Level
^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Level of detail at which log events are written to the console when ``EnableConsole`` = ``true``.

**DEBUG**: Prints high detail for developers debugging issues.

**ERROR**: Outputs only error messages.

**INFO**: Outputs error messages and information around startup and initialization.

+------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ConsoleLevel": "DEBUG"`` with options ``"DEBUG"``, ``"ERROR"``, and ``"INFO"``. |
+------------------------------------------------------------------------------------------------------------------------------+

Output console logs as JSON
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Typically set to ``true`` in production. When ``true``, logged events are written in a machine readable JSON format. Otherwise they are printed as plain text.

**True**: Logged events are written in a machine-readable JSON format.

**False**: Logged events are written in plain text.

Changes to this setting require a server restart before taking effect.

+----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ConsoleJson": true`` with options ``true`` and ``false``.                                 |
+----------------------------------------------------------------------------------------------------------------------------------------+

Output logs to file
^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Typically set to ``true`` in production. When ``true``, logged events are written to the ``mattermost.log`` file in the directory specified by the **FileLocation** setting. The logs are archived to a file in the same directory, and given a name with a datestamp and serial number. For example, ``mattermost.2017-03-31.001``.

**True**: Log files are written to files specified in ``FileLocation``.

**False**: Log files are not written.

Changes to this setting require a server restart before taking effect.

+----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableFile": true`` with options ``true`` and ``false``.                                  |
+----------------------------------------------------------------------------------------------------------------------------------------+

File Log Level
^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Level of detail at which log events are written to log files when ``EnableFile`` = ``true``.

**ERROR**: Outputs only error messages.

**INFO**: Outputs error messages and information around startup and initialization.

**DEBUG**: Prints high detail for developers debugging issues.

+--------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileLevel": "INFO"`` with options ``"DEBUG"``, ``"ERROR"``, and ``"INFO"``. |
+--------------------------------------------------------------------------------------------------------------------------+

Output file logs as JSON
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Typically set to ``true`` in production. When ``true``, logged events are written in a machine readable JSON format. Otherwise they are printed as plain text.

**True**: Logged events are written in a machine-readable JSON format.

**False**: Logged events are written in plain text.

Changes to this setting require a server restart before taking effect.

+----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileJson": true`` with options ``true`` and ``false``.                                    |
+----------------------------------------------------------------------------------------------------------------------------------------+

File Log Directory
^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The location of the log files. If blank, they are stored in the ``./logs`` directory. The path that you set must exist and Mattermost must have write permissions in it.

Changes to this setting require a server restart before taking effect.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileLocation": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Enable Webhook Debugging
^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Contents of incoming webhooks are printed to log files for debugging.

**False**: Contents of incoming webhooks are not printed to log files.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableWebhookDebugging": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

Enable Diagnostics and Error Reporting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: To improve the quality and performance of future Mattermost updates, this option sends error reporting and diagnostic information to Mattermost, Inc. All diagnostics and error reporting is encrypted in transit and does not include personally identifiable information or message contents. To learn more about this feature, see :doc:`../manage/telemetry`.

**False**: Diagnostics and error reporting are disabled.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableDiagnostics": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

Session Lengths
~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Environment > Session Lengths**.

User sessions are cleared when a user tries to log in. Additionally, a job runs every 24 hours to clear sessions from the sessions database table.

Extend session length with activity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Improves user experience by extending sessions and keeping users logged in if they are active in their Mattermost apps. 

**True**: Sessions will be automatically extended when the user is active in their Mattermost client. User sessions will only expire if they are not active in their Mattermost client for the entire duration of the session lengths defined in the fields below.

**False**: Sessions will not extend with activity in Mattermost. User sessions will immediately expire at the end of the session length or idle timeouts defined below.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExtendSessionLengthWithActivity": true`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------------+

Session length for email and AD/LDAP authentication (days)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Set the number of days from the last time a user entered their credentials to the expiry of the user's session on email and AD/LDAP authentication.

After changing this setting, the new session length will take effect after the next time the user enters their credentials.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SessionLengthWebInDays": 30`` with numerical input.             |
+--------------------------------------------------------------------------------------------------------------+

Session length for mobile apps (days)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Set the number of days from the last time a user entered their credentials to the expiry of the user's session on mobile apps.

After changing this setting, the new session length will take effect after the next time the user enters their credentials.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SessionLengthMobileInDays": 180`` with numerical input.        |
+-------------------------------------------------------------------------------------------------------------+

Session length for SSO authentication (days)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting defines the session length for SSO authentication, such as SAML, GitLab, and OAuth 2.0.

Set the number of days from the last time a user entered their credentials to the expiry of the user's session. If the authentication method is SAML, GitLab, or OAuth 2.0, the user may automatically be logged back in to Mattermost if they are already logged in to SAML, GitLab, or with OAuth 2.0.

After changing this setting, the setting will take effect after the next time the user enters their credentials.

+--------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SessionLengthSSOInDays": 30`` with numerical input. |
+--------------------------------------------------------------------------------------------------+

Session Cache (minutes)
^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Set the number of minutes to cache a session in memory.

+-------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SessionCacheInMinutes": 10`` with numerical input. |
+-------------------------------------------------------------------------------------------------+

Session Idle Timeout (minutes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The number of minutes from the last time a user was active on the system to the expiry of the user's session. Once expired, the user will need to log in to continue. Minimum is 5 minutes, and 0 is unlimited.

Applies to the desktop app and browsers. For mobile apps, use an EMM provider to lock the app when not in use. In High Availability mode, enable IP hash load balancing for reliable timeout measurement.

This setting does not take effect if ``ExtendSessionLengthWithActivity`` is set to ``true``.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SessionIdleTimeoutInMinutes": 43200`` with numerical input.        |
+-----------------------------------------------------------------------------------------------------------------+

Performance Monitoring
~~~~~~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Environment > Performance Monitoring**.

Changes to properties in this section require a server restart before taking effect.

Enable Performance Monitoring
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: Mattermost enables performance monitoring collection and profiling. Please see `documentation <https://docs.mattermost.com/scale/performance-monitoring.html>`__ to learn more about configuring performance monitoring for Mattermost.

**False**: Mattermost performance monitoring is disabled.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Listen Address
^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

The address the Mattermost server will listen on to expose performance metrics.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"InterNodeListenAddress": ":8067"`` with string input. |
+----------------------------------------------------------------------------------------------------+

Developer
~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Environment > Developer**.

Enable Testing Commands
^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: ``/test`` slash command is enabled to load test accounts and test data.

**False**: ``/test`` slash command is disabled.

Changes to this setting require a server restart before taking effect.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableTesting": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------+

Enable Developer Mode
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Javascript errors are shown in a purple bar at the top of the user interface. Not recommended for use in production.

**False**: Users are not alerted to Javascript errors.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableDeveloper": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

Allow Untrusted Internal Connections To
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting limits the ability for the Mattermost server to make untrusted requests within its local network. A request is considered "untrusted" when it's made on behalf of a client. The following features make untrusted requests and are affected by this setting:

- Integrations using webhooks, slash commands, or message actions. This prevents them from requesting endpoints within the local network.
- Link previews. When a link to a local network address is posted in a chat message, this prevents a link preview from being displayed.
- The `local image proxy <https://docs.mattermost.com/deploy/image-proxy.html>`_. If the local image proxy is enabled, images located on the local network cannot be used by integrations or posted in chat messages.

Requests that can only be configured by admins are considered trusted and will not be affected by this setting. Trusted URLs include ones used for OAuth login or for sending push notifications.

.. warning::
   This setting is intended to prevent users located outside your local network from using the Mattermost server to request confidential data from inside your network. Care should be used when configuring this setting to prevent unintended access to your local network.

Some examples of when you may want to modify this setting include:

- When installing a plugin that includes its own images, such as `Matterpoll <https://github.com/matterpoll/matterpoll>`__, you will need to add the Mattermost server's domain name to this list.
- When running a bot or webhook-based integration on your local network, you'll need to add the hostname of the bot/integration to this list.
- If your network is configured in such a way that publicly-accessible web pages or images are accessed by the Mattermost server using their internal IP address, the hostnames for those servers must be added to this list.

This setting is a whitelist of local network addresses that can be requested by the Mattermost server. It's configured as a whitespace-separated list of hostnames, IP addresses, and CIDR ranges that can be accessed (such as ``webhooks.internal.example.com 127.0.0.1 10.0.16.0/28``). Since v5.9, the public IP of the Mattermost application server itself is also considered a reserved IP.

.. note::
   Use whitespaces instead of commas to list the hostnames, IP addresses, or CIDR ranges. For example: ``webhooks.internal.example.com 127.0.0.1 10.0.16.0/28``.

IP address and domain name rules are applied before host resolution. CIDR rules are applied after host resolution, and only CIDR rules require DNS resolution. We try to match IP addresses and hostnames without even resolving. If that fails, we resolve using the local resolver (by reading the ``/etc/hosts`` file first), then check for matching CIDR rules. For example, if the domain "webhooks.internal.example.com" resolves to the IP address ``10.0.16.20``, a webhook with the URL "https://webhooks.internal.example.com/webhook" can be whitelisted using ``webhooks.internal.example.com`` or ``10.0.16.16/28``, but not ``10.0.16.20``.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowedUntrustedInternalConnections": ""`` with string input. |
+------------------------------------------------------------------------------------------------------------+

Site Configuration
-------------------

Settings for customizing your Mattermost deployment.

Customization
~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Customization**.

Site Name
^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Name of service shown in login screens and UI. Maximum 30 characters.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SiteName": "Mattermost"`` with string input. |
+-------------------------------------------------------------------------------------------+

Site Description
^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Description of service shown in login screens and UI. When not specified, "All team communication in one place, searchable and accessible anywhere" is displayed.

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CustomDescriptionText": ""`` with string input. |
+----------------------------------------------------------------------------------------------+

Enable Custom Branding
^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*This feature was moved to Team Edition in Mattermost v5.0, released June 16th, 2018. Prior to v5.0, this feature is available in legacy Enterprise Edition E10 and E20.*

**True**: Enables custom branding to show a JPG image some custom text on the server login page.

**False**: Custom branding is disabled.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCustomBrand": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Custom Brand Image
^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Custom JPG image is displayed on left side of server login page. Recommended maximum image size is less than 2 MB because image will be loaded for every user who logs in.

+----------------------------------------------------------------------------------------------------+
| This features has no ``config.json`` setting and must be set in the System Console user interface. |
+----------------------------------------------------------------------------------------------------+

Custom Brand Text
^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Custom text will be shown below custom brand image on left side of server login page. Maximum 500 characters allowed. You can format this text using the same `Markdown formatting codes <https://docs.mattermost.com/help/messaging/formatting-text.html>`__ as using in Mattermost messages.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CustomBrandText": ""`` with string input. |
+----------------------------------------------------------------------------------------+

Enable Ask Community Link
^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: **Ask the community** link is visible in the Mattermost channel header, under the **Help** menu. When selected, users are redirected to https://mattermost.com/pl/default-ask-mattermost-community/, where they can join the Mattermost Community to ask questions and help others troubleshoot issues. This option is not available on the mobile apps.

**False**: The link is not visible to users.

+--------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"enable_ask_community_link": ""`` with options ``true`` and ``false``. Defaults to true. |
+--------------------------------------------------------------------------------------------------------------------------------------+

Help link
^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Configurable link to a Help page your organization may provide to end users. By default, links to Mattermost help documentation are hosted on `docs.mattermost.com <https://docs.mattermost.com/>`__.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"HelpLink": "https://about.mattermost.com/default-help/"`` with string input. |
+---------------------------------------------------------------------------------------------------------------------------+

Support Email
^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Set an email address for feedback or support requests.

To ensure that users can contact you for assistance, set this value to an email address your System Admin receives, such as ``"support@yourcompany.com"``. This address is displayed on email notifications and during the Getting Started tutorial.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SupportEmail": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Terms of Service link
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Configurable link to Terms of Service your organization may provide to end users on the footer of the sign-up and login pages. By default, links to a Terms of Service page hosted on about.mattermost.com. If changing the link to a different Terms of Service, make sure to include the "Mattermost Conditions of Use" notice to end users that must also be shown to users from the "Terms of Service" link.

In version 5.17 and later, this setting does not change the terms of service link in **Main Menu > About Mattermost**, which refers to the Mattermost Terms of Service.

+--------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TermsOfServiceLink": "https://about.mattermost.com/default-terms/"`` with string input. |
+--------------------------------------------------------------------------------------------------------------------------------------+

Privacy Policy link
^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Configurable link to Privacy Policy your organization may provide to end users on the footer of the sign-up and login pages. By default, links to a Privacy Policy page hosted on about.mattermost.com.

In version 5.17 and later, this setting does not change the privacy policy link in **Main Menu > About Mattermost**, which refers to the Mattermost Privacy Policy.

+----------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PrivacyPolicyLink": "https://about.mattermost.com/default-privacy-policy/"`` with string input. |
+----------------------------------------------------------------------------------------------------------------------------------------------+

About Link
^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Configurable link to an About page describing your organization may provide to end users. By default, links to an About page hosted on about.mattermost.com.

+-----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AboutLink": "https://about.mattermost.com/default-about/"`` with string input. |
+-----------------------------------------------------------------------------------------------------------------------------+

Report a Problem link
^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Set the link for the support website.

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ReportAProblemLink": "https://about.mattermost.com/default-report-a-problem/"`` with string input. |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

Mattermost Apps Download Page Link
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Configurable link to a download page for Mattermost Apps. When a link is present, an option to **Download Apps** will be added in the Main Menu so users can find the download page. Leave this field blank to hide the option from the Main Menu. Defaults to a page on about.mattermost.com where users can download the iOS, Android, and Desktop clients. If you're using an Enterprise App Store for your mobile apps, change this link to point to a customized download page where users can find the correct apps.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AppDownloadLink": "https://mattermost.com/download/"`` with string input. |
+------------------------------------------------------------------------------------------------------------------------+

Android App Download Link
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Configurable link to download the Android app. When a link is present, users who access the site on a mobile web browser will be prompted with a page giving them the option to download the app. Leave this field blank to prevent the page from appearing. If you are using an Enterprise App Store for your mobile apps, change this link to point to the correct app.

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AndroidAppDownloadLink": "https://about.mattermost.com/mattermost-android-app/"`` with string input. |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

iOS App Download Link
^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Configurable link to download the iOS app. When a link is present, users who access the site on a mobile web browser will be prompted with a page giving them the option to download the app. Leave this field blank to prevent the page from appearing. If you are using an Enterprise App Store for your mobile apps, change this link to point to the correct app.

+-------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IosAppDownloadLink": "https://about.mattermost.com/mattermost-ios-app/"`` with string input. |
+-------------------------------------------------------------------------------------------------------------------------------------------+

Localization
~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Localization**.

Default Server Language
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Default language for system messages and logs.

Changes to this setting require a server restart before taking effect.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DefaultServerLocale": "en"`` with options ``"bg"``, ``"de"``, ``"en"``, ``"es"``, ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``, ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``"zh_CN"``, and ``"zh_TW"``. |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Default Client Language
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Default language for newly-created users and pages where the user hasn't logged in.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DefaultClientLocale": "en"`` with options ``"bg"``, ``"de"``, ``"en"``, ``"es"``, ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``, ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``"zh_CN"``, and ``"zh_TW"``. |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Available Languages
^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Sets which languages are available for users in **Account Settings > Display > Languages**. Leave the field blank to add new languages automatically by default, or add new languages using the dropdown menu manually as they become available. If you're manually adding new languages, the **Default Client Language** must be added before saving the setting.

.. note::
  Servers which upgraded to v3.1 need to manually set this field blank to have new languages added by default.

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AvailableLocales": ""`` with options ``""``, ``"bg"``, ``"de"``, ``"en"``, ``"es"``, ``"fr"``, ``"hu"``, ``"it"``, ``"ja"``, ``"ko"``, ``"nl"``, ``"pl"``, ``"pt-br"``, ``"ro"``, ``"ru"``, ``"sv"``, ``"tr"``, ``"zh_CN"``, and ``"zh_TW"``.  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Users and Teams
~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Users and Teams**.

Max Users Per Team
^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Maximum number of users per team, excluding inactive users.

The **Max Users Per Team** refers to the size of the "team site" which is workspace a "team of people" inhabits. A team of people is considered a small organization where people work closely together towards a specific shared goal and share the same etiquette. In the physical world, a team of people could typically be seated around a single table to have a meal and discuss their project.

The default maximum of 50 people, is at the extreme high end of a single team of people. At this point organizations are more often "multiple teams of people" and investments in explicitly defining etiquette, such as `channel organization <https://docs.mattermost.com/messaging/organizing-mattermost.html>`__ in Enterprise Edition, are often used to scale the high levels of productivity found in a team of people using Mattermost to multiple teams of people.

In terms of technical performance, `with appropriate hardware, Mattermost can easily scale to hundreds and even thousands of users <https://docs.mattermost.com/install/software-hardware-requirements.html>`__, and provided the administrator believes the appropriate etiquette is in place, they should feel free to increase the default value.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxUsersPerTeam": 50`` with numerical input. |
+-------------------------------------------------------------------------------------------+

Max Channels Per Team
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Maximum number of channels per team, including both active and deleted channels.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxChannelsPerTeam": 2000`` with numerical input.    |
+---------------------------------------------------------------------------------------------------+

Enable users to open Direct Message channels with
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**Any user on the Mattermost server**: The Direct Messages **More** menu has the option to open a Direct Message channel with any user on the server.

**Any member of the team**: The Direct Messages **More** menu only has the option to open a Direct Message channel with users on the current team, and CTRL/CMD+K channel switcher only lists users on the current team. If a user belongs to multiple teams, Direct Messages will still be received regardless of what team they are currently on.

This setting only affects the UI, not permissions on the server. For instance, a Direct Message channel can be created with anyone on the server regardless of this setting.

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictDirectMessage": "any"`` with options ``"any"`` and ``"team"`` for the above settings, respectively. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+



Teammate Name Display
^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specifies how names are displayed in the user interface by default. Please note that users can override this setting in **Account Settings > Display > Teammate Name Display**.

**Show username**: Displays the user's username.

**Show nickname if one exists**: Displays the user's nickname. If the user does not have a nickname, their full name is displayed. If the user does not have a full name, their username is displayed.

**Show first and last name**: Displays the user's full name. If the user does not have a full name, their username is displayed. Recommended when using SAML or LDAP if first name and last name attributes are configured.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TeammateNameDisplay": "username"`` with options ``"username"``, ``"nickname_full_name"``, and ``"full_name"`` for the above settings, respectively. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Lock Teammate Name Display for all users
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Disables users' ability to change settings under **Account Settings > Display > Teammate Name Display**.

**False**: Users can change how their teammate name displays.

Allow Users to View Archived Channels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Allows users to view, share, and search for content of channels that have been archived. Users can only view the content in channels of which they were a member before the channel was archived.

**False**: Users are unable to view, share, or search for content of channels that have been archived.

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalViewArchivedChannels": true`` with options ``true`` and ``false``.         |
+-------------------------------------------------------------------------------------------------------------------------------------+

Show Email Address
^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Show email address of all users.

**False**: Hide email address of users from other users in the user interface, including Team Admins. This is designed for managing teams where users choose to keep their contact information private. System Admins will still be able to see email addresses in the UI.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ShowEmailAddress": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

Show Full Name
^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Show full name of all users.

**False**: Hide full name of users from other users including Team Admins. This is designed for managing teams where users choose to keep their contact information private. System Admins will still be able to see full names in the UI.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ShowFullName": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+

Enable Custom User Statuses
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Users can set descriptive status messages and optional status emojis that are visible to all users.

**False**: Users are unable to set custom user statuses.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCustomUserStatuses": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------------+

Notifications
~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Notifications**.

Show @channel and @all confirmation dialog
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Users will be prompted to confirm when posting @channel and @all in channels with over five members.

**False**: No confirmation is required.

+--------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableConfirmNotificationsToChannel": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------------------+

Enable Email Notifications
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables sending of email notifications.

**False**: Disables email notifications for posts. This is useful for developers who may want to skip email setup for faster development. In order to remove the **Preview Mode: Email notifications have not been configured** banner, you should also set **Enable Preview Mode Banner** to ``false``.

If this setting is set to ``false`` and the SMTP server is set up, account related emails (such as password, email, username, user token, MFA, and other authentication related changes) will be sent regardless of this setting. 

Email invitations and account deactivation emails are not affected by this setting.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SendEmailNotifications": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

.. _email-preview-mode-banner-config:

Enable Preview Mode Banner
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Preview Mode banner is displayed to all users when ``"SendEmailNotifications": false`` so users are aware that email notifications are disabled.

**False**: Preview Mode banner is not displayed to users.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePreviewModeBanner": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Enable Email Batching
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Users can select how often to receive email notifications, and multiple notifications within that timeframe will be combined into a single email. Batching will occur at a default interval of 15 minutes, configurable in **Account Settings > Notifications**.

.. note::
  - Email batching cannot be enabled unless the `SiteURL <https://docs.mattermost.com/configure/configuration-settings.html#site-url>`__ is configured and the `SMTP Email Server <https://docs.mattermost.com/configure/configuration-settings.html#smtp-email-server>`__ is configured. 
  - Email batching in `High Availability mode <https://docs.mattermost.com/configure/configuration-settings.html#enable-high-availability-mode>`__ is planned but not yet supported.

**False**: If email notifications are enabled in Account Settings, emails will be sent individually for every mention or direct message received.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableEmailBatching": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------+

Email Notification Contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**Send full message contents**: Sender name and channel are included in email notifications.

**Send generic description with only sender name**: The team name and name of the person who sent the message, with no information about channel name or message contents, is included in email notifications. Typically used for compliance reasons if Mattermost contains confidential information and policy dictates it cannot be stored in email.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EmailNotificationContentsType": "full"`` with options ``"full"`` and ``"generic"`` for the above settings, respectively.             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Notification Display Name
^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Name displayed on email account used when sending notification emails from Mattermost system.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FeedbackName": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Notification From Address
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Address displayed on email account used when sending notification emails from within Mattermost.

So you don't miss messages, please make sure to change this value to an email your system administrator receives, such as ``"admin@yourcompany.com"``.

+--------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FeedbackEmail": ""`` with string input. |
+--------------------------------------------------------------------------------------+

Notification Reply-To Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Email address used in the Reply-To header when sending notification emails from Mattermost.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ReplyToAddress": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Notification Footer Mailing Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Organization name and mailing address displayed in the footer of email notifications from Mattermost, such as "© ABC Corporation, 565 Knight Way, Palo Alto, California, 94305, USA". If the field is left empty, the organization name and mailing address will not be displayed.

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FeedbackOrganization": ""`` with string input. |
+---------------------------------------------------------------------------------------------+

Push Notification Contents
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**Generic description with only sender name**: Push notifications include only the name of the person who sent the message but no information about channel name or message text.

**Generic description with sender and channel names**: Push notifications include names of users and channels but no specific details from the message text.

**Full message content sent in the notification payload**: Selecting **Send full message snippet** sends excerpts from messages triggering notifications with specifics and may include confidential information sent in messages. If your Push Notification Service is outside your firewall, it is HIGHLY RECOMMENDED this option only be used with an "https" protocol to encrypt the connection.

**Full message content fetched from the server on receipt** (*Available in Mattermost Enterprise*): The notification payload relayed through the `Apple Push Notification service <https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1>`_ or `Firebase Cloud Messaging <https://firebase.google.com/docs/cloud-messaging>`_ service contains no message content. Instead it contains a unique message ID used to fetch message content from the server when a push notification is received by a device via a `notification service app extention <https://developer.apple.com/documentation/usernotifications/modifying_content_in_newly_delivered_notifications>`_ on iOS or `an expandable notification pattern <https://developer.android.com/training/notify-user/expanded>`_ on Android. If the server cannot be reached, a generic push notification message is displayed without message content or sender name. 

For customers who choose to wrap the Mattermost mobile application in a secure container, such as BlackBerry Dynamics, MobileIron, AirWatch or other solutions, the container needs to execute the fetching of message contents from the unique message ID when push notification are received. If the container is unable to execute the fetch, the push notification contents cannot be received by the customer's mobile application without passing the message contents through either the `Apple Push Notification service <https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1>`_ or `Firebase Cloud Messaging <https://firebase.google.com/docs/cloud-messaging>`_ service. 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PushNotificationContents": "full"`` with options ``"generic_no_channel"``, ``"generic"``, ``"full"``, and ``"id_loaded"`` for the above settings, respectively.    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Announcement Banner
~~~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Announcement Banner**.

Enable Announcement Banner
^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Enable an announcement banner across all teams. The banner is displayed at the top of the screen and is the entire width of the screen. By default, users can dismiss the banner until you either change the text of the banner or until you re-enable the banner after it has been disabled. You can prevent users from dismissing the banner, and you can control the text color and the background color.

**True**: Enable the announcement banner. The banner is displayed only if ``BannerText`` has a value.

**False**: Disable the announcement banner.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableBanner": false`` with options ``true`` and ``false``.  |
+-----------------------------------------------------------------------------------------------------------+

Banner Text
^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The text of the announcement banner.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BannerText": ""`` with string input.  |
+------------------------------------------------------------------------------------+

Banner Color
^^^^^^^^^^^^

The background color of the announcement banner.

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BannerColor": "#f2a93b"`` with string input.   |
+---------------------------------------------------------------------------------------------+

Banner Text Color
^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The color of the text in the announcement banner.

+-------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BannerTextColor": "#333333"`` with string input.   |
+-------------------------------------------------------------------------------------------------+

Allow Banner Dismissal
^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Users can dismiss the banner until the next time they log in or the banner is updated.

**False**: The banner is permanently visible until it is turned off by the System Admin.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowBannerDismissal": true`` with options ``true`` and ``false``.   |
+-------------------------------------------------------------------------------------------------------------------+

Emoji
~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Emoji**.

Enable Emoji Picker
^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables an emoji picker that allows users to select emojis to add as reactions or use in messages. Enabling the emoji picker with a large number of custom emojis may slow down performance.

**False**: The emoji picker is disabled.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableEmojiPicker": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

Enable Custom Emoji
^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables a **Custom Emoji** option in the emoji picker, where users can go to add customiz emojis.

**False**: Custom emojis are disabled.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCustomEmoji": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

Posts
~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Posts**.

Enable Link Previews
^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Link previews are previews of linked website content, image links, and YouTube videos that are displayed below posts when available.

Link previews are requested by the server, meaning the Mattermost server must be connected to the internet for previews to be displayed. This connection can be established through a `firewall or outbound proxy <https://docs.mattermost.com/install/outbound-proxy.html>`__ in environments where direct internet connectivity is not given or security policies make this necessary.

**True**: Website link previews, image link previews, and YouTube previews are enabled on the server. Users can enable or disable website previews for themselves from **Account Settings > Display > Website Link Previews**.

**False**: Website link previews, image link previews, and YouTube previews are disabled. The server does not request metadata for any links sent in messages.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableLinkPreviews": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Disable Link Previews for Specific Domains
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Link previews are disabled for this list of comma-separated domains (e.g. “github.com, mattermost.com”). 

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictLinkPreviews": ""`` with string input. |
+---------------------------------------------------------------------------------------------+

Enable message link previews
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**True**: Links to messages generate a preview for any users with access to the original message. 

**False**: Links to messages don't include a preview.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePermalinkPreviews": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Enable SVGs
^^^^^^^^^^^

**True**: Enables users to see previews of SVG file attachments and SVG image links.

**False**: Previews of SVG file attachments and SVG image links are not displayed.

+--------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSVGs": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------+

Enable LaTeX Rendering
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables rendering of LaTeX code.

**False**: Disables rendering of LaTeX code to prevent the app from crashing when sharing code that might outgrow assigned memory. When disabled, LaTeX code will be highlighted.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableLatex": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+

Custom URL Schemes
^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

A list of URL schemes that are used for autolinking in message text. ``http``, ``https``, ``ftp``, ``tel`` and ``mailto`` always create links.

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CustomUrlSchemes": []`` with string array input consisting of URL schemes, such as ``["git", "smtp"]``. |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

Google API Key
^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Mattermost offers the ability to embed YouTube videos from URLs shared by end users. 

Set this key and add YouTube Data API v3 as a service to your key to enable the display of titles for embedded YouTube video previews. Without the key, YouTube previews will still be created based on hyperlinks appearing in messages or comments but they will not show the video title. If Google detects the number of views is exceedingly high, they may throttle embed access. 

Should this occur, you can remove the throttle by registering for a Google Developer Key and entering it in this field following these instructions: https://www.youtube.com/watch?v=Im69kzhpR3I. Your Google Developer Key is used in client-side Javascript.

Using a Google API Key allows Mattermost to detect when a video is no longer available and display the post with a *Video not found* label.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GoogleDeveloperKey": ""`` with string input. |
+-------------------------------------------------------------------------------------------+

File Sharing and Downloads
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > File Sharing and Downloads**.

Allow File Sharing
^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

When ``false``, disables file sharing on the server. All file and image uploads on messages are forbidden across clients and devices, including mobile.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableFileAttachments": true`` with options ``true`` and ``false``.    |
+---------------------------------------------------------------------------------------------------------------------+

Allow File Uploads on Mobile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: Enables file uploads on messages using Mattermost clients.

**False**: Disables file uploads on mobile apps. All file and image uploads on messages are forbidden across clients and devices, including mobile.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableMobileUpload": true`` with options ``true`` and ``false``.       |
+---------------------------------------------------------------------------------------------------------------------+

Allow File Downloads on Mobile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: Enables file downloads on Mattermost mobile apps.

**False**: Disables file downloads on mobile apps. Users can still download files from a mobile web browser.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableMobileDownload": true`` with options ``true`` and ``false``.     |
+---------------------------------------------------------------------------------------------------------------------+

Public Links
~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Public Links**.

Enable Public File Links
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Allow users to generate public links to files and images for sharing outside the Mattermost system with a public URL.

**False**: The **Get Public Link** option is hidden from the image preview user interface.

.. note:: 

   When switched to ``False``, anyone who tries to visit a previously generated public link will receive an error message saying public links have been disabled. When switched back to ``True``, old public links will work again unless the **Public Link Salt** has been regenerated.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePublicLink": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

Public Link Salt
^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

32-character salt added to the URL of public links when public links are enabled. Select **Regenerate** in the System Console to create a new salt, which will invalidate all existing public links.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PublicLinkSalt": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Notices
~~~~~~~~

Access the following configuration settings in the System Console by going to **Site Configuration > Notices**.

Enable Admin Notices
^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: System Admins will receive notices about available server upgrades and relevant system administration features. `Learn more <https://docs.mattermost.com/manage/in-product-notices.html>`_

**False**: System Admins will not receive notices except those that apply to all end users (See ``UserNoticesEnabled``). 

+----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AdminNoticesEnabled": true`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------+

Enable End User Notices
^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: All users will receive notices about available client upgrades and relevant end user features to improve user experience. `Learn more <https://docs.mattermost.com/manage/in-product-notices.html>`_

**False**: Users will not receive notices about available client upgrades and relevant end user features. 

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserNoticesEnabled": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Authentication
---------------

Authentication settings to enable account creation and sign in with email, GitLab, Google or Office 365 OAuth, AD/LDAP, or SAML.

Signup
~~~~~~~

Enable Account Creation
^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Ability to create new accounts is enabled via inviting new members or sharing the team invite link.

**False**: Ability to create accounts is disabled. The **Create Account** button displays an error when trying to signup via an email invite or team invite link.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserCreation": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Restrict account creation to specified email domains
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Teams and user accounts can only be created by a verified email from this list of comma-separated domains (e.g. "corp.mattermost.com, mattermost.org").

This setting only affects email login.

+--------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictCreationToDomains": ""`` with string input. |
+--------------------------------------------------------------------------------------------------+

Enable Open Server
^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Users can sign up to the server from the root page without an invite.

**False**: Users can only sign up to the server if they receive an invite.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOpenServer": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

Enable Email Invitations
^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Users can invite others to the Mattermost system by email.

**False**: Email invitations are disabled.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableEmailInvitations": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Invalidate pending email invites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This button invalidates active email invitations that have not been accepted by the user. By default email invitations expire after 48 hours.

Email
~~~~~

Enable account creation with email
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Allow team creation and account signup using email and password.

**False**: Email signup is disabled. This limits signup to single sign-on services like OAuth or AD/LDAP.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSignUpWithEmail": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

Require Email Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Require email verification after account creation prior to allowing login.

**False**: Users do not need to verify their email address prior to login. Developers may set this field to ``false`` to skip sending verification emails for faster development.

+----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RequireEmailVerification": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------+

Enable sign-in with email
^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Mattermost allows account creation using email and password.

**False**: Sign in with email is disabled and does not appear on the login screen. Use this value when you want to limit sign up to a Single Sign-on service like AD/LDAP, SAML, or GitLab.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSignInWithEmail": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

Enable sign-in with username
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Mattermost allows users with email login to sign in using their username and password. This setting does not affect AD/LDAP login.

**False**: Sign in with username is disabled and does not appear on the login screen.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``EnableSignInWithUsername": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Password
~~~~~~~~~

Minimum Password Length
^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*This feature was moved to Team Edition in Mattermost v5.0, released June 16th, 2018. Prior to v5.0, this feature is available in legacy Enterprise Edition E10 and E20.*

Minimum number of characters required for a valid password. Must be a whole number greater than or equal to 5 and less than or equal to 64.

+----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MinimumLength": 10`` with numerical input.                  |
+----------------------------------------------------------------------------------------------------------+

Password Requirements
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*This feature was moved to Team Edition in Mattermost v5.0, released June 16th, 2018. Prior to v5.0, this feature is available in legacy Enterprise Edition E10 and E20.*

Set the required character types to be included in a valid password. Defaults to allow any characters unless otherwise specified by the checkboxes. The error messasage previewed in the System Console will appear on the account creation page if a user enters an invalid password.

- **At least one lowercase letter**: Select this checkbox if a valid password must contain at least one lowercase letter.
- **At least one uppercase letter**: Select this checkbox if a valid password must contain at least one uppercase letter.
- **At least one number**: Select this checkbox if a valid password must contain at least one number.
- **At least one symbol**: Select this checkbox if a valid password must contain at least one symbol. Valid symbols include: ``!"#$%&'()*+,-./:;<=>?@[]^_`|~``.

This feature's ``config.json`` settings are, respectively:

.. list-table::
    :widths: 80

    * - ``"Lowercase": true`` with options ``true`` and ``false``.
    * - ``"Number": true`` with options ``true`` and ``false``.
    * - ``"Uppercase": true`` with options ``true`` and ``false``.
    * - ``"Symbol": true`` with options ``true`` and ``false``.

Maximum Login Attempts
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Failed login attempts allowed before a user is locked out and required to reset their password via email.

+------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaximumLoginAttempts": 10`` with numerical input. |
+------------------------------------------------------------------------------------------------+

MFA
~~~~

Configure security settings for multi-factor authentication.

The default recommendation for secure deployment is to host Mattermost within your own private network, with VPN clients on mobile, so everything works under your existing security policies and authentication protocols, which may already include multi-factor authentication.

If you choose to run Mattermost outside your private network, bypassing your existing security protocols, we recommend you set up a multi-factor authentication service specifically for accessing Mattermost.


Enable Multi-factor Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Users with LDAP and email authentication will be given the option to require a phone-based passcode, in addition to their password-based authentication, to sign-in to the Mattermost server. Specifically, they will be asked to download the `Google Authenticator <https://en.wikipedia.org/wiki/Google_Authenticator>`__ app to their iOS or Android mobile device, connect the app with their account, and then enter a passcode generated by the app on their phone whenever they log in to the Mattermost server.

**False**: Multi-factor authentication is disabled.

+-----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableMultifactorAuthentication": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------------------+

Enforce Multi-factor Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20*

**True**: `Multi-factor authentication (MFA) <https://docs.mattermost.com/onboard/multi-factor-authentication.html>`__ is required for login. New users will be required to configure MFA on signup. Logged in users without MFA configured are redirected to the MFA setup page until configuration is complete. If your system has users with login options other than AD/LDAP and email, MFA must be enforced with the authentication provider outside of Mattermost.

**False**: Multi-factor authentication is optional.

+------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnforceMultifactorAuthentication": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------------+

AD/LDAP
~~~~~~~~

Enable sign-in with AD/LDAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20*

**True**: Mattermost allows login using AD/LDAP or Active Directory.

**False**: Login with AD/LDAP is disabled.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Enable Synchronization with AD/LDAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Mattermost periodically synchronizes users from AD/LDAP.

**False**: AD/LDAP synchronization is disabled.

+--------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSync": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------+

Login Field Name
^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The placeholder text that appears in the login field on the login page. Typically this would be whatever name is used to refer to AD/LDAP credentials in your company, so it is recognizable to your users. Defaults to **AD/LDAP Username**.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginFieldName": ""`` with string input. |
+---------------------------------------------------------------------------------------+

AD/LDAP Server
^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The domain or IP address of the AD/LDAP server.

+-----------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LdapServer": ""`` with string input. |
+-----------------------------------------------------------------------------------+

AD/LDAP Port
^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The port Mattermost will use to connect to the AD/LDAP server. Defaults to ``389``.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LdapPort": 389`` with numerical input. |
+-------------------------------------------------------------------------------------+

Connection Security
^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The type of connection security Mattermost uses to connect to AD/LDAP.

**None**: No encryption, Mattermost will not attempt to establish an encrypted connection to the AD/LDAP server.

**TLS**: Encrypts the communication between Mattermost and your server using TLS.

**STARTTLS**: Takes an existing insecure connection and attempts to upgrade it to a secure connection using TLS.

If the "No encryption" option is selected it is highly recommended that the AD/LDAP connection is secured outside of Mattermost, for example, by adding a stunnel proxy.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ConnectionSecurity": ""`` with options ``""``, ``"TLS"``, and ``"STARTTLS"``. |
+----------------------------------------------------------------------------------------------------------------------------+

Skip Certificate Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Skips the certificate verification step for TLS or STARTTLS connections. Not recommended for production environments where TLS is required. For testing only.

**False**: Mattermost does not skip certificate verification.

+-------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SkipCertificateVerification": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------+

Private Key
^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

(Optional) The private key file provided by your LDAP Authentication Provider and uploaded if TLS client certificates are being used as the primary authentication mechanism.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PrivateKeyFile": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Public Certificate
^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

(Optional) The public TLS certificate file provided by your LDAP Authentication Provider and uploaded if TLS client certificates are being used as the primary authentication mechanism.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PublicCertificateFile": ""`` with with string input. |
+---------------------------------------------------------------------------------------------------+

Bind Username
^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The username used to perform the AD/LDAP search. This should be an account created specifically for use with Mattermost. Its permissions should be limited to read-only access to the portion of the AD/LDAP tree specified in the **Base DN** field. When using Active Directory, **Bind Username** should specify domain in ``"DOMAIN/username"`` format. This field is required, and anonymous bind is not currently supported.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BindUsername": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Bind Password
^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Password of the user given in **Bind Username**. Anonymous bind is not currently supported.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BindPassword": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Base DN
^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The **Base Distinguished Name** of the location where Mattermost should start its search for users in the AD/LDAP tree.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BaseDN": ""`` with string input. |
+-------------------------------------------------------------------------------+

User Filter
^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

(Optional) Enter an AD/LDAP Filter to use when searching for user objects (accepts `general syntax <https://www.ldapexplorer.com/en/manual/109010000-ldap-filter-syntax.htm>`__). Only the users selected by the query will be able to access Mattermost.

Sample filters for Active Directory:

- To filter out disabled users: ``(&(objectCategory=Person)(!(UserAccountControl:1.2.840.113556.1.4.803:=2)))``.
- To filter out by group membership, determine the distinguishedName of your group, then use the group membership general syntax format as your filter.

  * For example, if the security group distinguishedName is ``CN=group1,OU=groups,DC=example,DC=com``, then the user filter to use is: ``(memberOf=CN=group1,OU=groups,DC=example,DC=com)``. Note that the user must explicitly belong to this group for the filter to apply.

This filter uses the permissions of the **Bind Username** account to execute the search. Administrators should make sure to use a specially created account for Bind Username with read-only access to the portion of the AD/LDAP tree specified in the **Base DN** field.

+-----------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserFilter": ""`` with string input. |
+-----------------------------------------------------------------------------------+

Group Filter
^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

(Optional) Enter an AD/LDAP Filter to use when searching for group objects (accepts `general syntax <https://www.ldapexplorer.com/en/manual/109010000-ldap-filter-syntax.htm>`__). Only the groups selected by the query will be able to access Mattermost.

This filter is defaulted to ``(|(objectClass=group)(objectClass=groupOfNames)(objectClass=groupOfUniqueNames))`` when blank.

.. note::
  This filter is used only when AD/LDAP Group Sync is enabled. See `AD/LDAP Group Sync documentation <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`_ for more information on enabling and configuring AD/LDAP Group Sync.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GroupFilter": ""`` with string input. |
+------------------------------------------------------------------------------------+

Enable Admin Filter
^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables System Admins to configure an AD/LDAP filter.

**False**: Disables the ability for System Admins to configure an AD/LDAP filter.

Admin Filter
^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

(Optional) Enter a filter to use for designating the System Admin role to users. When enabled the user is promoted to this role on their next login or at the next scheduled AD/LDAP sync. If the Admin Filter is removed, users who are currently logged in retain their Admin role. When they log out this is revoked and on their next login they will no longer have Admin privileges.

This filter default is ``false`` and must be set to ``true`` in order for the Admin Filter to be used.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAdminFilter": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Guest Filter
^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

(Optional) Enter an AD/LDAP Filter to use when searching for external users who have Guest Access to Mattermost. Only the users selected by the query will be able to log in to and use Mattermost as Guests. This filter default is blank.

See the `Guest Accounts documentation <https://docs.mattermost.com/onboard/guest-accounts.html>`__ for more information.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GuestFilter": ""`` with string input. |
+------------------------------------------------------------------------------------+

ID Attribute
^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The attribute in the AD/LDAP server used as a unique identifier in Mattermost. It should be an AD/LDAP attribute with a value that does not change.

If a user's ID Attribute changes, a new Mattermost account (unassociated with the previous one) is created. To prevent this, it's recommended that a unique attribute such as ``objectGUID`` in Active Directory and ``entryUUID`` in LDAP be used instead.

Before making any changes confirm with your LDAP provider whether these attributes are available in your environment.

If you need to change this field after users have already logged in, use the `mattermost ldap idmigrate <https://docs.mattermost.com/manage/command-line-tools.html#mattermost-ldap-idmigrate>`__ CLI tool.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------+

Login ID Attribute
^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The attribute in the AD/LDAP server used to log in to Mattermost. Normally this attribute is the same as the **Username Attribute** field above.

If your team typically uses domain\username to log in to other services with AD/LDAP, you may enter domain\username in this field to maintain consistency between sites.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginIdAttribute": ""`` with string input. |
+-----------------------------------------------------------------------------------------+

Username Attribute
^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The attribute in the AD/LDAP server used to populate the username field in Mattermost. This may be the same as the Login ID Attribute.

This attribute will be used within the Mattermost user interface to identify and mention users. For example, if a Username Attribute is set to **john.smith** a user typing ``@john`` will see ``@john.smith`` in their auto-complete options and posting a message with ``@john.smith`` will send a notification to that user that they've been mentioned.

The **Username Attribute** may be set to the same value used to sign-in to the system, called a **Login ID Attribute**, or it can be mapped to a different value.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UsernameAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Email Attribute
^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The attribute in the AD/LDAP server used to populate the email address field in Mattermost.

Email notifications will be sent to this email address, and this email address may be viewable by other Mattermost users depending on privacy settings chosen by the System Admin.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EmailAttribute": ""`` with string input.    |
+------------------------------------------------------------------------------------------+

First Name Attribute
^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

(Optional) The attribute in the AD/LDAP server used to populate the first name of users in Mattermost. When set, users cannot edit their first name, since it is synchronized with the LDAP server. When left blank, users can set their first name in Account Settings.

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FirstNameAttribute": ""`` with string input.    |
+----------------------------------------------------------------------------------------------+

Last Name Attribute
^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

(Optional) The attribute in the AD/LDAP server used to populate the last name of users in Mattermost. When set, users cannot edit their last name, since it is synchronized with the LDAP server. When left blank, users can set their last name in Account Settings.

+-----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LastNameAttribute": ""`` with string input.      |
+-----------------------------------------------------------------------------------------------+

Nickname Attribute
^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

(Optional) The attribute in the AD/LDAP server used to populate the nickname of users in Mattermost. When set, users cannot edit their nickname, since it is synchronized with the LDAP server. When left blank, users can set their nickname in Account Settings.

+--------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"NicknameAttribute": ""`` with string input.   |
+--------------------------------------------------------------------------------------------+

Position Attribute
^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

(Optional) The attribute in the AD/LDAP server used to populate the position field in Mattermost. When set, users cannot edit their position, since it is synchronized with the LDAP server. When left blank, users can set their position in Account Settings.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PositionAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Profile Picture Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The attribute in the AD/LDAP server used to synchronize (and lock) the profile picture used in Mattermost.

The Mattermost server will replace the user’s profile image upon login (not at the sync interval as with other attributes). The sync will not occur if the current Mattermost profile image matches the image associated with that user in AD/LDAP.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PictureAttribute": ""`` with string input. |
+-----------------------------------------------------------------------------------------+

Group Display Name Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

(Required) Enter an AD/LDAP Group Display name attribute used to populate Mattermost Group names.

.. note::
  This attribute is used only when AD/LDAP Group Sync is enabled. See `AD/LDAP Group Sync documentation <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`_ for more information on enabling and configuring AD/LDAP Group Sync.

+--------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GroupDisplayNameAttribute": ""`` with string input. |
+--------------------------------------------------------------------------------------------------+

Group Id Attribute
^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

(Required) Enter an AD/LDAP Group ID attribute to use as a unique identifier for Groups. This should be an AD/LDAP value that does not change. This is usually ``entryUUID`` for LDAP and ``objectGUID`` for AD.

.. note::
  This attribute is used only when AD/LDAP Group Sync is enabled. See `AD/LDAP Group Sync documentation <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`_ for more information on enabling and configuring AD/LDAP Group Sync.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GroupIdAttribute": ""`` with string input. |
+-----------------------------------------------------------------------------------------+

Synchronization Interval (minutes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Set how often Mattermost accounts synchronize attributes with AD/LDAP, in minutes. 

When synchronizing, Mattermost queries AD/LDAP for relevant account information and updates Mattermost accounts based on changes to attributes (first name, last name, and nickname). 

When accounts are disabled in AD/LDAP users are made inactive in Mattermost, and their active sessions are revoked once Mattermost synchronizes attributes. To synchronize immediately after disabling an account, use the **AD/LDAP Synchronize Now** button.

+-----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SyncIntervalMinutes": 60`` with numerical input. |
+-----------------------------------------------------------------------------------------------+

.. note::
  LDAP syncs cause a large number of database read queries. Ensure that you monitor database load during a sync to determine how often these syncs should happen in your environment in order to minimize performance degradation.

Maximum Page Size
^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The maximum number of users the Mattermost server will request from the AD/LDAP server at one time. Use this setting if your AD/LDAP server limits the number of users that can be requested at once.

- A value of 0 is unlimited and does not paginate the results.
- A value of 1500 is recommended to align with the default AD/LDAP ``MaxPageSize`` setting.

+--------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxPageSize": 0`` with numerical input. |
+--------------------------------------------------------------------------------------+

Query Timeout (seconds)
^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The timeout value for queries to the AD/LDAP server. Increase this value if you are getting timeout errors caused by a slow AD/LDAP server.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"QueryTimeout": 60`` with numerical input. |
+----------------------------------------------------------------------------------------+

AD/LDAP Test
^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This button can be used to test the connection to the AD/LDAP server. If the test is successful, it shows a confirmation message and if there is a problem with the configuration settings it will show an error message.

AD/LDAP Synchronize Now
^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This button causes AD/LDAP synchronization to occur as soon as it is pressed. Use it whenever you have made a change in the AD/LDAP server you want to take effect immediately. After using the button, the next AD/LDAP synchronization will occur after the time specified by the Synchronization Interval.

You can monitor the status of the synchronization job in the table below this button.

.. note::
  If synchronization **Status** displays as ``Pending`` and does not complete, make sure that the **Enable Synchronization with AD/LDAP** setting is set to ``true``.

.. figure:: ../images/ldap-sync-table.png

.. _saml-enterprise:

SAML
~~~~~

.. note::
   In line with Microsoft ADFS guidance we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_.

Enable Login With SAML
^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: Mattermost allows login using SAML. Please see `documentation <https://docs.mattermost.com/onboard/sso-saml.html>`__ to learn more about configuring SAML for Mattermost.

**False**: Login with SAML is disabled.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Enable Synchronizing SAML Accounts With AD/LDAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: Mattermost periodically synchronizes SAML user attributes, including user deactivation and removal, with AD/LDAP. Enable and configure synchronization settings at **Authentication > AD/LDAP**. See `documentation <https://about.mattermost.com/default-saml-ldap-sync>`__ to learn more.

**False**: Synchronization of SAML accounts with AD/LDAP is disabled.

+----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSyncWithLdap": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------+

Ignore Guest Users When Synchronizing with AD/LDAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Available when ``Enable Synchronizing SAML Accounts With AD/LDAP`` is set to ``true``. 

**True**: Mattermost ignores Guest Users identified by the Guest Attribute when synchronizing with AD/LDAP on user deactivation and removal. Manage guest deactivation manually via **System Console > Users**. See `documentation <https://docs.mattermost.com/onboard/ad-ldap.html>`__ to learn more.

**False**: Synchronization of SAML deactivates and removes Guest Users when synchronizing with AD/LDAP.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IgnoreGuestsLdapSync": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

Override SAML Bind Data with AD/LDAP Information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: Mattermost overrides the SAML ID attribute with the AD/LDAP ID attribute if configured or overrides the SAML Email attribute with the AD/LDAP Email attribute if SAML ID attribute is not present. See `documentation <https://docs.mattermost.com/onboard/ad-ldap.html>`__ to learn more.

**False**: Mattermost uses the email attribute to bind users to SAML.

.. note::
  Moving from ``true`` to ``false`` will prevent the override from happening. To prevent the disabling of user accounts, SAML IDs must match the LDAP IDs when this feature is enabled. This setting should be set to ``false`` unless LDAP sync is enabled.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSyncWithLdapIncludeAuth": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------------------+

Identity Provider Metadata URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

The URL where Mattermost sends a request to obtain setup metadata from the provider.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdpMetadataUrl": ""`` with string input. |
+---------------------------------------------------------------------------------------+

SAML SSO URL
^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

The URL where Mattermost sends a SAML request to start login sequence.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdpURL": ""`` with string input. |
+-------------------------------------------------------------------------------+

Identity Provider Issuer URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

The issuer URL for the Identity Provider you use for SAML requests.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdpDescriptorUrl": ""`` with string input. |
+-----------------------------------------------------------------------------------------+

Identity Provider Public Certificate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

The public authentication certificate issued by your Identity Provider.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdpCertificateFile": ""`` with string input. |
+-------------------------------------------------------------------------------------------+

Verify Signature
^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: Mattermost verifies that the signature sent from the SAML Response matches the Service Provider Login URL.

**False**: Not recommended for production environments. For testing only.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Verify": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------+

Service Provider Login URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Enter ``https://<your-mattermost-url>/login/sso/saml`` (example: ``https://example.com/login/sso/saml``). Make sure you use HTTP or HTTPS in your URL depending on your server configuration. This field is also known as the Assertion Consumer Service URL.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AssertionConsumerServiceURL": ""`` with string input. |
+----------------------------------------------------------------------------------------------------+

Service Provider Identifier
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

The unique identifier for the Service Provider, usually the same as Service Provider Login URL. In ADFS, this must match the Relying Party Identifier.

+--------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ServiceProviderIdentifier": ""`` with string input. |
+--------------------------------------------------------------------------------------------------+

Enable Encryption
^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: Mattermost will decrypt SAML Assertions encrypted with your Service Provider Public Certificate.

**False**: Not recommended for production environments. For testing only.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Encrypt": true`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Service Provider Private Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

The private key used to decrypt SAML Assertions from the Identity Provider.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PrivateKeyFile": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Service Provider Public Certificate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

The certificate file used to generate the signature on a SAML request to the Identity Provider for a service provider initiated SAML login, when Mattermost is the Service Provider.

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PublicCertificateFile": ""`` with string input. |
+----------------------------------------------------------------------------------------------+

Sign Request
^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

When ``true``, Mattermost signs the SAML request using your Service Provider Private Key. When ``false``, Mattermost does not sign the SAML request.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SignRequest": ""`` with string input. |
+------------------------------------------------------------------------------------+

Signature Algorithm
^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

The signature algorithm used to sign the request. Supported options are `RSAwithSHA1 <https://www.w3.org/2000/09/xmldsig#rsa-sha1>`_, `RSAwithSHA256 <https://www.w3.org/2000/09/xmldsig#rsa-sha1>`_, and `RSAwithSHA512 <https://www.w3.org/2001/04/xmldsig-more#rsa-sha512>`_.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SignatureAlgorithm": ""`` with string input. |
+-------------------------------------------------------------------------------------------+

Canonical Algorithm
^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

The canonicalization algorithm. Supported options are ``Canonical1.0`` for `Exclusive XML Canonicalization 1.0 (omit comments) <https://www.w3.org/TR/2002/REC-xml-exc-c14n-20020718/>`_ (``http://www.w3.org/2001/10/xml-exc-c14n#``) and ``Canonical1.1`` for `Canonical XML 1.1 (omit comments) <https://www.w3.org/TR/2008/REC-xml-c14n11-20080502/>`_ (``http://www.w3.org/2006/12/xml-c14n11``).

+-------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CanonicalAlgorithm": "Canonical1.0"`` with string input. |
+-------------------------------------------------------------------------------------------------------+

Email Attribute
^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

The attribute in the SAML Assertion that will be used to populate the email addresses of users in Mattermost.

Email notifications will be sent to this email address, and this email address may be viewable by other Mattermost users depending on privacy settings choosen by the System Admin.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EmailAttribute": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Username Attribute
^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

The attribute in the SAML Assertion that will be used to populate the username field in Mattermost user interface. This attribute will be used within the Mattermost user interface to identify and mention users. For example, if a Username Attribute is set to **john.smith** a user typing ``@john`` will see ``@john.smith`` in their auto-complete options and posting a message with ``@john.smith`` will send a notification to that user that they've been mentioned.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UsernameAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Id Attribute
^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion used to bind users from SAML to users in Mattermost.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------+

Guest Attribute
^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion used to apply a Guest role to users in Mattermost.

See the `Guest Accounts documentation <https://docs.mattermost.com/onboard/guest-accounts.html>`__ for more information.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GuestAttribute": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Enable Admin Attribute
^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: Enables System Admins to configure the SAML Assertion.

**False**: Disables the ability for System Admins to configure the SAML Assertion.

Admin Attribute
^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion for designating System Admins. The user is automatically promoted to this role on their next login. If the Admin Attribute is removed, users who are currently logged in retain their Admin role. When they log out this is revoked and on their next login they will no longer have Admin privileges.

This attribute's default is ``false`` and must be set to ``true`` in order for the Admin Attribute to be used.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAdminAttribute": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

First Name Attribute
^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion that will be used to populate the first name of users in Mattermost.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FirstNameAttribute": ""`` with string input. |
+-------------------------------------------------------------------------------------------+

Last Name Attribute
^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion that will be used to populate the last name of users in Mattermost.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LastNameAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Nickname Attribute
^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion that will be used to populate the nickname of users in Mattermost.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"NicknameAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Position Attribute
^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion that will be used to populate the position field for users in Mattermost (typically used to describe a person's job title or role at the company).

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PositionAttribute": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Preferred Language Attribute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

(Optional) The attribute in the SAML Assertion that will be used to populate the language of users in Mattermost.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LocaleAttribute": ""`` with string input. |
+----------------------------------------------------------------------------------------+

Login Button Text
^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

(Optional) The text that appears in the login button on the login page. Defaults to **SAML**.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonText": ""`` with string input. |
+----------------------------------------------------------------------------------------+

OAuth 2.0
~~~~~~~~~

.. note::
  
  OAuth 2.0 is being deprecated and will be replaced by `OpenID Connect <https://docs.mattermost.com/configure/configuration-settings.html#openid-connect>`__ in a future release.

Settings to configure OAuth login for account creation and login.

Select OAuth 2.0 service provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Choose whether OAuth can be used for account creation and login. Options include:

- **Do not allow sign-in via an OAuth 2.0 provider**
- **GitLab** (available in all plans; see `GitLab Settings <https://docs.mattermost.com/configure/configuration-settings.html#gitlab-settings>`__ for details)
- **Google Apps** (Available in Mattermost Enterprise and Professional; see `Google Settings <https://docs.mattermost.com/configure/configuration-settings.html#google-settings>`__ for details)
- **Office 365** (Available in Mattermost Enterprise and Professional; see `Office 365 Settings <https://docs.mattermost.com/configure/configuration-settings.html#office-365-settings>`__ for details)

This feature's setting does not appear in ``config.json``.

GitLab
''''''

Enable authentication with GitLab
.................................

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Allow team creation and account signup using GitLab OAuth. To configure, input the **Secret** and **Id** credentials.

**False**: GitLab OAuth cannot be used for team creation or account signup.

.. note:: 
   For Enterprise subscriptions, GitLab settings can be found under **OAuth 2.0**

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Application ID
..............

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Obtain this value by logging into your GitLab account. Go to **Profile Settings > Applications > New Application**, enter a Name, then enter Redirect URLs ``https://<your-mattermost-url>/login/gitlab/complete`` (example: ``https://example.com:8065/login/gitlab/complete`` and ``https://<your-mattermost-url>/signup/gitlab/complete``.

+---------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input. |
+---------------------------------------------------------------------------+

Application Secret Key
......................

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Obtain this value by logging into your GitLab account. Go to **Profile Settings > Applications > New Application**, enter a Name, then enter Redirect URLs ``https://<your-mattermost-url>/login/gitlab/complete`` (example: ``https://example.com:8065/login/gitlab/complete`` and ``https://<your-mattermost-url>/signup/gitlab/complete``.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input. |
+-------------------------------------------------------------------------------+

GitLab Site URL
................

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the URL of your GitLab instance (example ``https://example.com:3000``). If your GitLab instance is not set up with SSL, start the URL with ``http://`` instead of ``https://``.

User API Endpoint
.................

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Enter ``https://<your-gitlab-url>/api/v3/user`` (example: ``https://example.com:3000/api/v3/user``). Use HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserApiEndpoint": ""`` with string input. |
+----------------------------------------------------------------------------------------+

Auth Endpoint
..............

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Enter ``https://<your-gitlab-url>/oauth/authorize`` (example: ``https://example.com:3000/oauth/authorize``). Use HTTP or HTTPS depending on how your server is configured.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AuthEndpoint": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Token Endpoint
..............

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Enter ``https://<your-gitlab-url>/oauth/token`` (example: ``https://example.com:3000/oauth/token``). Use HTTP or HTTPS depending on how your server is configured.

+--------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TokenEndpoint": ""`` with string input. |
+--------------------------------------------------------------------------------------+

Google
''''''

Enable authentication with Google by selecting ``Google Apps`` from **OAuth 2.0 > Select OAuth 2.0 service provider**.

**True**: Allow team creation and account signup using Google OAuth. To configure, input the **Client ID** and **Client Secret** credentials. See `the documentation <https://docs.mattermost.com/onboard/sso-google.html>`__ for more detail.

**False**: Google OAuth cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Client ID
.........

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

+---------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input. |
+---------------------------------------------------------------------------+

Client Secret
.............

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input. |
+-------------------------------------------------------------------------------+

User API Endpoint
..................

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

We recommend you use ``https://people.googleapis.com/v1/people/me?personFields=names,emailAddresses,nicknames,metadata`` as the User API Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserApiEndpoint": "https://people.googleapis.com/v1/people/me?personFields=names,emailAddresses,nicknames,metadata"``   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Auth Endpoint
..............

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

We recommend you use ``https://accounts.google.com/o/oauth2/v2/auth`` as the Auth Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+---------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AuthEndpoint": "https://accounts.google.com/o/oauth2/v2/auth"`` with string input. |
+---------------------------------------------------------------------------------------------------------------------------------+

Token Endpoint
..............

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

We recommend that you use ``https://www.googleapis.com/oauth2/v4/token`` as the Token Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+--------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TokenEndpoint": "https://www.googleapis.com/oauth2/v4/token"`` with string input. |
+--------------------------------------------------------------------------------------------------------------------------------+

Office 365
'''''''''''

.. note::
   In line with Microsoft ADFS guidance we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`__.

Enable authentication with Office 365 by selecting **Office 365** from **System Console > Authentication > OAuth 2.0 > Select OAuth 2.0 service provider**.

**True**: Allow team creation and account signup using Office 365 OAuth. To configure, input the **Application ID** and **Application Secret Password** credentials. See `the documentation <https://docs.mattermost.com/onboard/sso-office.html>`__ for more detail.

**False**: Office 365 OAuth cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Application ID
..............

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Microsoft or Office account.

+---------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input. |
+---------------------------------------------------------------------------+

Application Secret Password
...........................

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Microsoft or Office account.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input. |
+-------------------------------------------------------------------------------+

Directory (tenant) ID
.....................

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This value is the ID of the application's AAD directory.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DirectoryId": ""`` with string input. |
+------------------------------------------------------------------------------------+

User API Endpoint
.................

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

We recommend using ``https://graph.microsoft.com/v1.0/me`` as the User API Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserApiEndpoint": "https://graph.microsoft.com/v1.0/me"`` with string input. |
+---------------------------------------------------------------------------------------------------------------------------+

Auth Endpoint
.............

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

We recommend using ``https://accounts.google.com/o/oauth2/v2/auth`` as the Auth Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AuthEndpoint": "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"`` with string input.                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Token Endpoint
..............

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

We recommend that you use ``https://login.microsoftonline.com/common/oauth2/v2.0/token`` as the Token Endpoint. Otherwise, enter a custom endpoint in ``config.json`` with HTTP or HTTPS depending on how your server is configured.

+------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TokenEndpoint": "https://login.microsoftonline.com/common/oauth2/v2.0/token"`` with string input. |
+------------------------------------------------------------------------------------------------------------------------------------------------+

OpenID Connect
~~~~~~~~~~~~~~

Select OpenID Connect service provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Choose whether OpenID Connect can be used for account creation and login. Options include:

- **Do not allow sign-in via an OpenID provider**
- **GitLab** (available in all plans; see `GitLab Settings <https://docs.mattermost.com/configure/configuration-settings.html#gitlab-settings>`__ for details)
- **Google Apps** (Available in Mattermost Enterprise and Professional; see `Google Settings <https://docs.mattermost.com/configure/configuration-settings.html#google-settings>`__ for details)
- **Office 365** (Available in Mattermost Enterprise and Professional; see `Office 365 Settings <https://docs.mattermost.com/configure/configuration-settings.html#office-365-settings>`__ for details)
- **OpenID Connect (Other)** (Available in Mattermost Enterprise and Professional; see `OpenID Connect Settings <https://docs.mattermost.com/configure/configuration-settings.html#openid-connect-other-settings>`__ for more detail)

This feature's setting does not appear in ``config.json``.

GitLab Settings
'''''''''''''''

GitLab Site URL
................

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20. Not available in Cloud Starter.*

Specify the URL of your GitLab instance (example ``https://example.com:3000``). If your GitLab instance is not set up with SSL, start the URL with ``http://`` instead of ``https://``.

Discovery Endpoint
..................

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20*
*Not available in Cloud Starter*

Obtain this value by registering Mattermost as an application in your service provider account. Should be in the format ``https://myopenid.provider.com/{my_company}/.well-known/openid-configuration`` where the value of *{my_company}* is replaced with your organization.

Client ID
.........

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20*
*Not available in Cloud Starter*

Obtain this value by registering Mattermost as an application in your service provider account.

Client Secret
..............

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20*
*Not available in Cloud Starter*

Obtain this value by registering Mattermost as an application in your Google account.

Google Settings
'''''''''''''''

Enable authentication with Google by selecting ``Google Apps`` from **System Console > Authentication > OpenID Connect > Select service provider**.

**True**: Allow team creation and account signup using Google OpenID Connect. To configure, input the **Client ID**, **Client Secret**, and **DiscoveryEndpoint** credentials. See `the documentation <https://docs.mattermost.com/onboard/sso-google.html>`__ for more detail.

**False**: Google OpenID Connect cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Discovery Endpoint
...................

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This value is prepopulated with ``https://accounts.google.com/.well-known/openid-configuration``.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DiscoveryEndpoint": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Client ID
..........

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

+---------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input. |
+---------------------------------------------------------------------------+

Client Secret
.............

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input. |
+-------------------------------------------------------------------------------+

Office 365 Settings
'''''''''''''''''''

.. note::
   In line with Microsoft ADFS guidance, we recommend `configuring intranet forms-based authentication for devices that do not support WIA <https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-intranet-forms-based-authentication-for-devices-that-do-not-support-wia>`_.

Enable authentication with Office 365 by selecting **Office 365** from **System Console > Authentication > OpenID Connect > Select service provider**.

**True**: Allow team creation and account signup using Office 365 OpenID Connect. To configure, input the **Application ID** and **Application Secret Password** credentials. See `the documentation <https://docs.mattermost.com/onboard/sso-office.html>`__ for more detail.

**False**: Office 365 OpenID Connect cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Directory (tenant) ID
.....................

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This value is the ID of the application's AAD directory.

Discovery Endpoint
..................

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This value is prepopulated with https://login.microsoftonline.com/common/v2.0/.well-known/openid-configuration.

Client ID
..........

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

Client Secret
..............

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your Google account.

OpenID Connect (Other) 
'''''''''''''''''''''''

Enable authentication with a service provider by selecting ``OpenID Connect (Other)`` from **System Console > Authentication > OpenID Connect > Select service provider**.

**True**: Allow team creation and account signup using OpenID Connect. To configure, input the **Client ID**, **Client Secret**, and **DiscoveryEndpoint** credentials. See `the documentation <https://docs.mattermost.com/onboard/sso-openidconnect.html>`__ for more detail.

**False**: OpenID Connect cannot be used for team creation or account signup.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Button Name
............

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Specify the text that displays on the OpenID login button.

+-----------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ButtonText": ""`` with string input. |
+-----------------------------------------------------------------------------------+

Button Color
.............

Specify the color of the OpenID login button for white labeling purposes. Use a hex code with a #-sign before the code, for example ``#145DBF``.

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ButtonColor": ""`` with string input. |
+------------------------------------------------------------------------------------+

Discovery Endpoint
..................

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your service provider account. Should be in the format ``https://myopenid.provider.com/{my_company}/.well-known/openid-configuration`` where the value of *{my_company}* is replaced with your organization.

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DiscoveryEndpoint": ""`` with string input. |
+------------------------------------------------------------------------------------------+

Client ID
..........

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your service provider account.

+---------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Id": ""`` with string input. |
+---------------------------------------------------------------------------+

Client Secret
..............

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Obtain this value by registering Mattermost as an application in your service provider account.

+-------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Secret": ""`` with string input. |
+-------------------------------------------------------------------------------+

Guest Access
~~~~~~~~~~~~

Enable Guest Access
^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20*

**True**: Allow guest invitations to channels within teams. Please see `Guest Accounts documentation <https://docs.mattermost.com/onboard/guest-accounts.html>`_ for more information.

**False**: Email signup is disabled. This limits signup to Single sign-on services like OAuth or AD/LDAP.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Whitelisted Guest Domains
^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20*

When populated, guest accounts can only be created by a verified email from this list of comma-separated domains.

+--------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictCreationToDomains": ""`` with string input. |
+--------------------------------------------------------------------------------------------------+

Enforce Multi-factor Authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20*

This setting defaults to false and is read-only if multi-factor authentication is not enforced for regular users.

**True**: Multi-factor authentication (MFA) is required for login. New guest users will be required to configure MFA on sign-up. Logged in guest users without MFA configured are redirected to the MFA setup page until configuration is complete.

**False**: Multi-factor authentication for guests is optional.

+------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnforceMultifactorAuthentication": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------------+

Plugins
--------

Settings to configure Mattermost plugins.

Plugin Management
~~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Plugins > Plugin Management**.

Enable Plugins
^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.
  
.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables plugins on your Mattermost server. Use plugins to integrate with third-party systems, extend functionality, or customize the user interface of your Mattermost server. See `documentation <https://developers.mattermost.com/integrate/admin-guide/admin-plugins-beta/>`__ to learn more.

**False**: Disables plugins on your Mattermost server.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------+

Require Plugin Signature
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.
  
.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Require valid plugin signatures before starting managed or unmanaged plugins. Pre-packaged plugins are not subject to plugin signature verification. Plugins installed through the Plugin Marketplace are always subject to plugin signature verification at the time of download.

**False**: Don't require valid plugin signatures before starting managed or unmanaged plugins. Pre-packaged plugins are not subject to plugin signature verification. Plugins installed through the Plugin Marketplace are always subject to plugin signature verification at the time of download.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RequirePluginSignature": true`` with options ``true`` and ``false``.   |
+---------------------------------------------------------------------------------------------------------------------+

Automatic Prepackaged Plugins
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.
  
.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Any pre-packaged plugins enabled in the configuration will be installed or upgraded automatically. If a newer version is already installed, no changes are made.

**False**: Pre-packaged plugins aren't installed or upgraded automatically but may be installed manually from the Plugin Marketplace, even when offline.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AutomaticPrepackagedPlugins": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

Enable Marketplace
^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.
  
.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables Plugin Marketplace on your Mattermost server for all System Admins.

**False**: Disables Plugin Marketplace on your Mattermost server for all System Admins.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableMarketplace": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

Enable Remote Marketplace
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.
  
.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: The server will attempt to connect to the configured Plugin Marketplace to show the latest plugins. If the connection fails, the Plugin Marketplace shows only pre-packaged and already installed plugins alongside a connection error.

**False**: The server won't attempt to connect to a remote marketplace, and will show only pre-packaged and already installed plugins. Use this setting if your server can't connect to the internet.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableRemoteMarketplace": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Marketplace URL
^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.
  
.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

If the Marketplace is enabled, this setting specifies which URL should be used to query for new Marketplace plugins.

+------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MarketplaceUrl": "https://api.integrations.mattermost.com"`` with string input. |
+------------------------------------------------------------------------------------------------------------------------------+

Installed Plugin State
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.
  
.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Lists installed plugins on your Mattermost server and whether they are enabled. Pre-packaged plugins are installed by default and can be deactivated, but not removed.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PluginStates": {}`` with object input mapping plugin IDs as keys to objects, each of which contains a key ``"Enable": false`` with options ``true`` or ``false``. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Plugin Settings
^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.
  
.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Settings specific to each Mattermost plugin.

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Plugins": {}`` with object input mapping plugin IDs as keys to objects containing plugin-specific data. |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

Agenda
~~~~~~~

Access the following configuration settings in the System Console by going to **Plugins > Agenda**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables the Agenda plugin on your Mattermost server.

**False**: Disables the Agenda plugin on your Mattermost server.

Antivirus
~~~~~~~~~~

This plugin allows the forwarding of uploaded files to an antivirus scanning application, `ClamAV anti-virus software <https://www.clamav.net/>`__, and prevents the upload from completing if there is a virus detected in the file. 

Use this plugin to prevent users from inadvertently spreading malware or viruses via your Mattermost server. See the `Mattermost Antivirus Plugin <https://github.com/mattermost/mattermost-plugin-antivirus>`__ documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Antivirus**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables the Antivirus plugin on your Mattermost server.

**False**: Disables the Antivirus plugin on your Mattermost server.

ClamAV - Host and Port
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the hostname and port to connect to the ClamAV server.

Scan Timeout (seconds)
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify how long the virus scan can take before timing out.

Apps
~~~~

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |cloud|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

**True**: Enables the Apps plugin on your Mattermost server.

**False**: Disables the Apps plugin on your Mattermost server.

To create your own Mattermost App, see the `Mattermost Apps <https://developers.mattermost.com/integrate/apps/>`__ developer documentation.

Autolink
~~~~~~~~~

This plugin creates regular expression (regexp) patterns that are reformatted into a Markdown link before the message is saved into the database. System Admins can configure this plugin in the ``config.json`` file, using the ``/autolink`` slash command (when enabled), or through using the System Console. See the `Autolink Plugin <https://github.com/mattermost/mattermost-plugin-autolink/blob/master/README.md>`__ documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Autolink**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables the Autolink plugin on your Mattermost server.

**False**: Disables the Autolink plugin on your Mattermost server.

Enable administration with /autolink command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables the ability to configure the Apps plugin using the ``/autolink`` slash command.

**False**: Disables the ability to use the slash command to configure the plugin.

Apply plugin to updated posts as well as new posts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Applies the plugin to updated posts as well as new posts. 

**False**: Applies the plugin to new posts only.

Admin User IDs
^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify users authorized to administer the plugin in addition to System Admins. Separate multiple user IDs with commas.

.. tip::
  Find user IDs by going to **System Console > User Management > Users**.

AWS SNS
~~~~~~~~

This plugin is used to receive alert notifications from `Amazon AWS CloudWatch <https://aws.amazon.com/cloudwatch/>`__ to Mattermost channels via `AWS Simple Notification Server (SNS) <https://docs.aws.amazon.com/sns/latest/dg/welcome.html>`__. 

Access the following configuration settings in the System Console by going to **Plugins > AWS SNS**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables the AWS SNS plugin on your Mattermost server.

**False**: Disables the AWS SNS plugin on your Mattermost server.

Channel to send notifications to
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the channel to send notifications to in the format ``teamname,channelname``. For example, for a channel with a URL of ``https://example.com/myteam/channels/mychannel``, set the value to ``myteam,mychannel``. If the specified channel does not exist, the plugin creates the channel for you.

Authorized User IDs
^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify users authorized to accept AWS SNS subscriptions to a Mattermost channel. Separate multiple user IDs with commas.

.. tip::
  Find user IDs by going to **System Console > User Management > Users**.

Token
^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Generate a token to validate incoming requests from AWS SNS by selecting ``Regenerate``.

Channel Export
~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Plugins > Channel Export**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.
  
.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables the Channel Export plugin on your Mattermost workspace.

**False**: Disables the Channel Export plugin on your Mattermost workspace.

Demo Plugin
~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Plugins > Demo Plugin**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables the Demo plugin on your Mattermost workspace.

**False**: Disables the Demo plugin on your Mattermost workspace.

Channel Name
^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the channel to use as part of the demo plugin. If the specified channel does not exist, the plugin creates the channel for you.


Username
^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the user to use as part of the demo plugin. If the specified user does not exist, the plugin creates the user for you.

GIF commands
~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Plugins > GIF commands**.

This plugin is used to post GIFs from Gfycat, Giphy, or Tenor using slash commands.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables the GIF commands plugin on your Mattermost server.

**False**: Disables the GIF commands plugin on your Mattermost server.

Display the GIF as
^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Display the GIF as an embedded image where the GIF can't be collapsed, or as a collapsible image preview where the full URL displays. 

.. note::
   `Link previews <https://docs.mattermost.com/configure/configuration-settings.html#enable-link-previews>`__ must be enabled in order to display GIF link previews. Mattermost deployments restricted to access behind a firewall must open port 443 to both ``https://api.gfycat.com/v1`` and ``https://gfycat.com/<id>`` (for all request types) for this feature to work.

GIF Provider
^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the GIF provider as GIPHY, Tenor, or Gfycat.

.. note::
  Selecting GIPHY or Tenor requires an API Key for this feature to work. An API key is not required for Gfycat.

Giphy/Tenor API Key
^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Configure your own API Key when specifying the GIF Provider as GIPHY or Tenor. An API key is not required for Gfycat. 

To get your own API key, see the `GIPHY Developers Quick Start <https://developers.giphy.com/docs/api/#quick-start-guide>`__ documentation, or the `Tenor Developer <https://tenor.com/developer/keyregistration>`__ documentation for details.

Content Rating (GIPHY & Tenor only)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Select an `MPAA-style content rating <https://en.wikipedia.org/wiki/Motion_Picture_Association_film_rating_system>`__ for GIFs from GIPHY or Tenor. Leave this field empty to disable content filtering.

Gfycat display style
^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the display style for GIFs from Gfycat. See the `Gfycat Developer API <Gfycat display style>`__ documentation for details.


GIPHY display style
^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the display style for GIFs from GIPHY. See the `GIPHY Developers Rendition Guide <https://developers.giphy.com/docs/optional-settings/>`__ for details.

Tenor display style
^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the display style for GIFs from Tenor. See the `Tenor API <https://tenor.com/gifapi/documentation#responseobjects-gifformat>`__ documentation for details.

Language
^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the language used to search GIFs from GIPHY. See the `GIPHY Developers Language Support <https://developers.giphy.com/docs/optional-settings/#language-support>`__ documentation for details.

Force GIF preview before posting (force /gifs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enabled by default to prevent accidental posting of inappropriate GIFs from a provider that does not support content rating filtering.

**False**: Both ``/gif`` and ``/gifs`` slash commands are available for the GIF commands plugin on your Mattermost server.

Mattermost Boards
~~~~~~~~~~~~~~~~~

Mattermost Boards is an open source alternative to Trello, Notion, and Asana that's integrated from Mattermost v5.36. Boards is a project management tool that helps define, organize, track and manage work across teams, using a familiar kanban board view. See the `Mattermost Boards <https://docs.mattermost.com/guides/boards.html>`__ product documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Mattermost Boards**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables the Mattermost Boards plugin on your Mattermost workspace.

**False**: Disables the Mattermost Boards plugin on your Mattermost workspace.

Mattermost Playbooks
~~~~~~~~~~~~~~~~~~~~

Mattermost Playbooks is an open source, self-hosted collaboration tool for teams. Each playbook represents a recurring outcome or specific goal that your teams collaborate on to achieve, such as service outage recovery or customer onboarding. Teams run a playbook every time they want to orchestrate people, tools, and data to achieve that outcome as quickly as possible while providing visibility to stakeholders. Playbooks also allow teams to incorporate learnings from the retrospective to tweak and improve the playbook with every iteration. See the `Mattermost Playbooks <https://docs.mattermost.com/guides/playbooks.html>`__ documentation for details.

Access the following configuration settings in the System Console by going to **Plugins > Playbooks**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables the Mattermost Playbooks plugin on your Mattermost workspace.

**False**: Disables the Mattermost Playbooks plugin on your Mattermost workspace.

Enabled Teams
^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Enable Playbooks for all Mattermost teams, or for only selected teams.

Enable Experimental Features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables exeprimental Playbooks features on your Mattermost workspace.

**False**: Disables experimental Playbooks features on your Mattermost workspace.

User Satisfaction Surveys
~~~~~~~~~~~~~~~~~~~~~~~~~

This plugin enables Mattermost to send user satisfaction surveys to gather feedback and improve product quality directly from your Mattermost users. Please refer to the 'Mattermost Privacy Policy <https://mattermost.com/privacy-policy/>`__ for more information on the collection and use of information received through Mattermost services.

Access the following configuration settings in the System Console by going to **Plugins > User Satisfaction Surveys**.

Enable Plugin
^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables the Mattermost Playbooks plugin on your Mattermost workspace.

**False**: Disables the Mattermost Playbooks plugin on your Mattermost workspace.

Enable User Satisfaction Survey
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: A user satisfaction survey will be sent out to all users on a quarterly basis. The survey results will be used by Mattermost, Inc. to improve the quality and user experience of the product. Please refer to the 'Mattermost Privacy Policy <https://mattermost.com/privacy-policy/>`__ for more information on the collection and use of information received through Mattermost services.

**False**: User satisfaction surveys are disabled. 

Zoom
~~~~

This plugin allows team members to initiate a Zoom meeting with a single click. All participants in a channel can easily join the Zoom meeting and the shared link is updated when the meeting is over. See the `Zoom Conferencing Plugin <https://mattermost.gitbook.io/plugin-zoom/>`__ product documentation for details.

.. note::
  To set up this plugin, you need to create a Zoom App using a Zoom Administrator account. See the `Zoom Configuration <https://mattermost.gitbook.io/plugin-zoom/installation/zoom-configuration>`__ documentation for details. 

Access the following configuration settings in the System Console by going to **Plugins > Zoom**.

Enable Plugin
^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables the Zoom plugin on your Mattermost server.

**False**: Disables the Zoom plugin on your Mattermost server.

Zoom URL
^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the URL for a self-hosted private cloud or on-premise Zoom server. For example, ``https://yourzoom.com``. Leave blank if you're using Zoom's vendor-hosted SaaS service.

Zoom API URL
^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the API URL for a self-hosted private cloud or on-premise Zoom server. For example, ``https://api.yourzoom.com/v2``. Leave blank if you're using Zoom's vendor-hosted SaaS service.

Enable OAuth
^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: OAuth will be used as the authentication means with Zoom.

**False**: JWT will be used as the authentication means with Zoom.

.. note::

  If you are currently using a JWT Zoom application and switch to OAuth, all users will need to connect their Zoom account using OAuth the next time they try to start a meeting. See the `Zoom Configuration <https://mattermost.gitbook.io/plugin-zoom/installation/zoom-configuration>`__ documentation for details.

OAuth by Account Level App (Beta)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Only an account administrator has to log in. The rest of the users will use their e-mail to log in.

**False**: All users must use their e-mail to log in.

Zoom OAuth Client ID
^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the Client ID for the OAuth app registered with Zoom. Leave blank if not using OAuth.

Zoom OAuth Client Secret
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the Client Secret for the OAuth app registered with Zoom. Leave blank if not using OAuth.

At Rest Token Encryption Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Generate an AES encryption key for Zoom OAuth Token used to encrypt stored access tokens by selecting ``Regenerate``. Regenerating the key invalidates your existing Zoom OAuth.

API Key
^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the API Key generated by Zoom used to create meetings and pull user data.

API Secret
^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the API Secret generated by Zoom for your API key.

Webhook Secret
^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Generate a secret for the webhook URL endpoint used to authenticate the webhook to Mattermost. Regenerating the secret invalidates your existing Zoom plugin.

Integrations
-------------

Settings to configure webhooks, slash commands, and external integration services.

Integration Management
~~~~~~~~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Integrations > Integration Management**.

Enable Incoming Webhooks
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Developers building integrations can create webhook URLs for Public channels and Private channels. Please see our `documentation page <https://docs.mattermost.com/developer/webhooks-incoming.html>`__ to learn about creating webhooks, view samples, and to let the community know about integrations you have built.

**True**: Incoming webhooks will be allowed. To manage incoming webhooks, go to **Account Settings > Integrations**. The webhook URLs created in Account Settings can be used by external applications to create posts in any Public or Private channels that you have access to.

**False**: The **Integrations > Incoming Webhooks** section of Account Settings is hidden and all incoming webhooks are disabled.

.. important::
   Security note: By enabling this feature, users may be able to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`__ by attempting to impersonate other users. To combat these attacks, a BOT tag appears next to all posts from a webhook. Enable at your own risk.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableIncomingWebhooks": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

Enable Outgoing Webhooks
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Developers building integrations can create webhook tokens for Public channels. Trigger words are used to fire new message events to external integrations. For security reasons, outgoing webhooks are only available in Public channels. Please see our `documentation page <https://docs.mattermost.com/developer/webhooks-outgoing.html>`__ to learn about creating webhooks and view samples.

**True**: Outgoing webhooks will be allowed. To manage outgoing webhooks, go to **Account Settings > Integrations**.

**False**: The **Integrations > Outgoing Webhooks** section of Account Settings is hidden and all outgoing webhooks are disabled.

.. important:: 
   Security note: By enabling this feature, users may be able to perform `phishing attacks <https://en.wikipedia.org/wiki/Phishing>`__ by attempting to impersonate other users. To combat these attacks, a BOT tag appears next to all posts from a webhook. Enable at your own risk.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOutgoingWebhooks": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

Enable Custom Slash Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Slash commands send events to external integrations that send a response back to Mattermost.

**True**: Allow users to create custom slash commands from **Main Menu > Integrations > Commands**.

**False**: Slash commands are hidden in the **Integrations** user interface.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableCommands": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

Enable OAuth 2.0 Service Provider
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Mattermost acts as an OAuth 2.0 service provider allowing Mattermost to authorize API requests from external applications.

**False**: Mattermost does not function as an OAuth 2.0 service provider.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOAuthServiceProvider": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

Enable integrations to override usernames
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Webhooks, slash commands, OAuth 2.0 apps, and other integrations such as `Zapier <https://docs.mattermost.com/integrations/zapier.html>`__, will be allowed to change the username they are posting as. If no username is present, the username for the post is the same as it would be for a setting of ``False``.

**False**: Custom slash commands can only post as the username of the user who used the slash command. OAuth 2.0 apps can only post as the username of the user who set up the integration. For incoming webhooks and outgoing webhooks, the username is "webhook". See https://developers.mattermost.com/integrate/other-integrations/ for more details.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostUsernameOverride": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

Enable integrations to override profile picture icons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Webhooks, slash commands, and other integrations, such as `Zapier <https://docs.mattermost.com/integrations/zapier.html>`__, will be allowed to change the profile picture they post with.

**False**: Webhooks, slash commands, and OAuth 2.0 apps can only post with the profile picture of the account they were set up with. See https://developers.mattermost.com/integrate/other-integrations/ for more details.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostIconOverride": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Enable Personal Access Tokens
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Users can create `personal access tokens <https://docs.mattermost.com/developer/personal-access-tokens.html>`__ for integrations in **Account Settings > Security**. They can be used to authenticate against the API and give full access to the account.

To manage who can create personal access tokens or to search users by token ID, go to the **System Console > Users** page.

**False**: Personal access tokens are disabled on the server.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserAccessTokens": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Bot Accounts
~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Integrations > Bot Accounts**.

Enable Bot Account Creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Users can create bot accounts for integrations in **Integrations > Bot Accounts**. Bot accounts are similar to user accounts except they cannot be used to log in. See `documentation <https://developers.mattermost.com/integrate/admin-guide/admin-bot-accounts/>`__ to learn more.

**False**: Bot accounts cannot be created through the user interface or the RESTful API. Plugins can still create and manage bot accounts.

+----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableBotAccountCreation": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------+

Disable bot accounts when owner is deactivated
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: When a user is deactivated, disables all bot accounts managed by the user. To re-enable bot accounts, go to **Integrations > Bot Accounts**.

**False**: When a user is deactivated, all bot accounts managed by the user remain active.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DisableBotsWhenOwnerIsDeactivated": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------+

GIF (Beta)
~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Integrations > GIF (Beta)**.

Enable GIF Picker
^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Allow users to select GIFs from the emoji picker via a Gfycat integration.

**False**: GIFs cannot be selected in the emoji picker.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableGifPicker": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

.. note::
   `Link previews <https://docs.mattermost.com/configure/configuration-settings.html#enable-link-previews>`__ must be enabled in order to display GIF link previews. Mattermost deployments restricted to access behind a firewall must open port 443 to both https://api.gfycat.com/v1 and https://gfycat.com/<id> (for all request types) for this feature to work.

Gfycat API Key
^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

When blank, uses the default API key provided by Gfycat. Alternatively, a unique API key can be requested at https://developers.gfycat.com/signup/#/. Enter the client ID you receive via email to this field.

+-----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GfycatApiKey": "2_KtH_W5"`` with string input.   |
+-----------------------------------------------------------------------------------------------+

Gfycat API Secret
^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The API secret generated by Gfycat for your API key. When blank, uses the default API secret provided by Gfycat.

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GfycatApiSecret": "3wLVZPiswc3DnaiaFoLkDvB4X0IV6CpMkj4tf2inJRsBY6-FnkT08zGmppWFgeof"`` with string input.  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

CORS
~~~~~

Access the following configuration settings in the System Console by going to **Integrations > CORS**.

Enable cross-origin requests from
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Enable HTTP cross-origin requests from specific domains separated by spaces. Type ``*`` to allow CORS from any domain or leave it blank to disable it.

.. note::
 Please make sure you have entered your Site URL before enabling this setting to prevent losing access to the System Console after saving. If you experience lost access to the System Console after changing this setting, you can set your `Site URL <https://docs.mattermost.com/configure/configuration-settings.html#site-url>`__ through the ``config.json`` file.

+--------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowCorsFrom": ""`` with string input. |
+--------------------------------------------------------------------------------------+

CORS Exposed Headers
^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Whitelist of headers that will be accessible to the requester.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CorsExposedHeaders": ""`` with string input. |
+-------------------------------------------------------------------------------------------+

CORS Allow Credentials
^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Requests that pass validation will include the ``Access-Control-Allow-Credentials`` header.

**False**: Requests won't include the ``Access-Control-Allow-Credentials`` header.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CorsAllowCredentials": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

CORS Debug
^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Prints messages to the logs to help when developing an integration that uses CORS. These messages will include the structured key value pair ``"source": "cors"``.

**False**: Debug messages not printed to the logs.

+-------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CorsDebug": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------+

Compliance
------------

Data Retention Policies
~~~~~~~~~~~~~~~~~~~~~~~

Changes to properties in this section require a server restart before taking effect.

.. warning:: 
   Once a message or a file is deleted, the action is irreversible. Please be careful when setting up a custom data retention policy.

Access the following configuration settings in the System Console by going to **Compliance > Data Retention Policies**.


Global retention policy for messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Set how long Mattermost keeps messages and files across all teams and channels. Doesn't apply to custom retention policies.

If **Days** or **Years** is chosen, set how many days or years messages are kept in Mattermost. Messages older than the duration you set will be deleted nightly. The minimum time is one day.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableMessageDeletion": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

and

+-------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MessageRetentionDays": 365`` with numerical input. |
+-------------------------------------------------------------------------------------------------+

Global retention policy for files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Set how long Mattermost keeps files across all teams and channels. Doesn't apply to custom retention policies.

If **Days** or **Years** is chosen, set how many days or years files are kept in Mattermost. Files older than the duration you set will be deleted nightly. The minimum time is one day.

+----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableFileDeletion": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------+

and

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileRetentionDays": 365`` with numerical input. |
+----------------------------------------------------------------------------------------------+

Custom retention policy
^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Set how long Mattermost keeps messages and files across specific teams and channels by specifing a name for the custom retention policy, setting a duration value, specifying the teams and channels that will follow this policy.

Data Deletion Time
^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Set the start time of the daily scheduled data retention job. Choose a time when fewer people are using your system. Must be a 24-hour time stamp in the form ``HH:MM``.

This setting is based on the local time of the server.

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DeletionJobStartTime": "02:00"`` with 24-hour timestamp input in the form ``"HH:MM"``. |
+-------------------------------------------------------------------------------------------------------------------------------------+

Run Deletion Job Now
^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Start a Data Retention deletion job immediately. You can monitor the status of the job in the data deletion job table within the Policy Log section.

Compliance Export
~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Compliance > Compliance Export**.

Enable Compliance Export
^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available as an add-on to legacy Enterprise Edition E20*

**True**: Mattermost will generate a compliance export file that contains all messages that were posted in the last 24 hours. The export task is scheduled to run once per day. See the `documentation to learn more <https://docs.mattermost.com/comply/compliance-export.html>`__.

**False**: Mattermost doesn't generate a compliance export file.

+----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableExport": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------+

Compliance Export Time
^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available as an add-on to legacy Enterprise Edition E20*

Set the start time of the daily scheduled compliance export job. Choose a time when fewer people are using your system. Must be a 24-hour time stamp in the form ``HH:MM``.

This setting is based on the local time of the server.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DailyRunTime": 01:00`` with 24-hour timestamp input in the form ``"HH:MM"``. |
+---------------------------------------------------------------------------------------------------------------------------+

Export File Format
^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available as an add-on to legacy Enterprise Edition E20*

File format of the compliance export. Corresponds to the system that you want to import the data into.

Currently supported formats are CSV, Actiance XML, and Global Relay EML.

If Global Relay is chosen, the following options will be presented:

Global Relay Customer Account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available as an add-on to legacy Enterprise Edition E20*

Type of Global Relay customer account your organization has, either ``A9/Type 9`` or ``A10/Type 10``.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"CustomerType": "A9/Type 9"`` with options ``"A9/Type 9"`` and ``"A10/Type 10"``. |
+-------------------------------------------------------------------------------------------------------------------------------+

Global Relay SMTP Username
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available as an add-on to legacy Enterprise Edition E20*

The username for authenticating to the Global Relay SMTP server.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SmtpUsername": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Global Relay SMTP Password
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available as an add-on to legacy Enterprise Edition E20*

The password associated with the Global Relay SMTP username.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SmtpPassword": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Global Relay Email Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available as an add-on to legacy Enterprise Edition E20*

The email address your Global Relay server monitors for incoming compliance exports.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EmailAddress": ""`` with string input. |
+-------------------------------------------------------------------------------------+

Run Compliance Export Job Now
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available as an add-on to legacy Enterprise Edition E20*

This button initiates a compliance export job immediately. You can monitor the status of the job in the compliance export job table.

Compliance Monitoring
~~~~~~~~~~~~~~~~~~~~~~

Settings used to enable and configure Mattermost compliance reports. This feature is replaced by the `Compliance Export <configure/configuration-settings.html#compliance-export>`__ feature, and will be removed in a future release. We recommend migrating to the new system.

Access the following configuration settings in the System Console by going to **Compliance > Compliance Export**.

Enable Compliance Reporting
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available as an add-on to legacy Enterprise Edition E20*

**True**: Compliance reporting is enabled in Mattermost.

**False**: Compliance reporting is disabled.

+----------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Enable": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------+

Compliance Report Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available as an add-on to legacy Enterprise Edition E20*

Sets the directory where compliance reports are written.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Directory": "./data/"`` with string input. |
+-----------------------------------------------------------------------------------------+

Enable Daily Report
^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available as an add-on to legacy Enterprise Edition E20*

**True**: Mattermost generates a daily compliance report.

**False**: Daily reports are not generated.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableDaily": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+

Batch Size
^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available as an add-on to legacy Enterprise Edition E20*

Set the size of the batches in which posts will be read from the database to generate the compliance report. This setting is currently not available in the System Console and can only be set in ``config.json``.

+------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BatchSize": 30000`` with default value ``30000``. |
+------------------------------------------------------------------------------------------------+

Custom Terms of Service
~~~~~~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Compliance > Custom Terms of Service**.

Enable Custom Terms of Service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available as an add-on to legacy Enterprise Edition E20*

.. note::
  This configuration setting can only be modified using the System Console user interface.

**True**: New users must accept the Terms of Service before accessing any Mattermost teams on desktop, web, or mobile. Existing users must accept them after login or a page refresh. To update the Terms of Service link displayed in account creation and login pages, go to **System Console > Legal and Support > Terms of Service Link**.

**False**: During account creation or login, users can review Terms of Service by accessing the link configured via **System Console > Legal and Support > Terms of Service link**.

Custom Terms of Service Text
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available as an add-on to legacy Enterprise Edition E20*

Text that will appear in your custom Terms of Service. Supports Markdown-formatted text.

Re-Acceptance Period
^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available as an add-on to legacy Enterprise Edition E20*

The number of days before Terms of Service acceptance expires, and the terms must be re-accepted.

Defaults to 365 days. 0 indicates the terms do not expire.

Experimental
-------------

There are a number of settings considered "experimental" that are configurable from the System Console. These may be replaced or removed in a future release.

AD/LDAP Settings
~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Experimental > Features**.

AD/LDAP Login Button Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the color of the AD/LDAP login button for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonColor": ""`` with string input.                                       |
+-------------------------------------------------------------------------------------------------------------------------------+

AD/LDAP Login Button Border Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the color of the AD/LDAP login button border for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonBorderColor": ""`` with string input.                                 |
+-------------------------------------------------------------------------------------------------------------------------------+

AD/LDAP Login Button Text Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the color of the AD/LDAP login button text for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonTextColor": ""`` with string input.                                   |
+-------------------------------------------------------------------------------------------------------------------------------+

Allow Authentication Transfer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20*

**True**: Users can change their sign-in method to any that is enabled on the server, either via Account Settings or the APIs.

**False**: Users cannot change their sign-in method, regardless of which authentication options are enabled.

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalEnableAuthenticationTransfer": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------------+

Link Metadata Timeout
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Adds a configurable timeout for requests made to return link metadata. If the metadata is not returned before this timeout expires, the message will post without requiring metadata. This timeout covers the failure cases of broken URLs and bad content types on slow network connections.

+---------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LinkMetadataTimeoutMilliseconds": 5000`` with numerical input.                     |
+---------------------------------------------------------------------------------------------------------------------------------+

Email Settings
~~~~~~~~~~~~~~

Email Batching Buffer Size
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the maximum number of notifications batched into a single email.

+--------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``EmailBatchingBufferSize": 256`` with numerical input.                        |
+--------------------------------------------------------------------------------------------------------------------------+

Email Batching Interval
^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the maximum frequency, in seconds, which the batching job checks for new notifications. Longer batching intervals will increase performance.

+-----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``EmailBatchingInterval": 30`` with numerical input.                        |
+-----------------------------------------------------------------------------------------------------------------------+

Email Login Button Color
^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the color of the email login button for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonColor": ""`` with string input.                                       |
+-------------------------------------------------------------------------------------------------------------------------------+

Email Login Button Border Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the color of the email login button border for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonBorderColor": ""`` with string input.                                 |
+-------------------------------------------------------------------------------------------------------------------------------+

Email Login Button Text Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Specify the color of the email login button text for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonTextColor": ""`` with string input.                                   |
+-------------------------------------------------------------------------------------------------------------------------------+

Enable Account Deactivation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Ability for users to deactivate their own account from **Account Settings > Advanced**. If a user deactivates their own account, they will get an email notification confirming they were deactivated.

**False**: Ability for users to deactivate their own account is disabled.

+--------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserDeactivation": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------+

Enable Automatic Replies
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Users can enable Automatic Replies in **Account Settings > Notifications**. Users set a custom message that will be automatically sent in response to Direct Messages.

**False**: Disables the Automatic Direct Message Replies feature and hides it from Account Settings.

+--------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalEnableAutomaticReplies": false`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------------------------+

Enable Channel Viewed WebSocket Messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting determines whether ``channel_viewed WebSocket`` events are sent, which synchronize unread notifications across clients and devices. Disabling the setting in larger deployments may improve server performance.

+------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableChannelViewedMessages": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------------+

Enable Client-Side Certification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: Enables client-side certification for your Mattermost server. See `the documentation <https://docs.mattermost.com/onboard/certificate-based-authentication.html>`__ to learn more.

**False**: Client-side certification is disabled.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ClientSideCertEnable": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

Client-Side Certification Login Method
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Used in combination with the ``ClientSideCertEnable`` configuration setting.

**Primary**: After the client side certificate is verified, user's email is retrieved from the certificate and is used to log in without a password.

**Secondary**: After the client side certificate is verified, user's email is retrieved from the certificate and matched against the one supplied by the user. If they match, the user logs in with regular email/password credentials.

+----------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ClientSideCertCheck": "secondary"`` with options ``"primary"`` and ``"secondary"``. |
+----------------------------------------------------------------------------------------------------------------------------------+

Enable Default Channel Leave/Join System Messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting determines whether team leave/join system messages are posted in the default ``town-square`` channel.

**True**: Enables leave/join system messages in the default ``town-square`` channel.

**False**: Disables leave/join messages from the default ``town-square`` channel. These system messages won't be added to the database either.

+----------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalEnableDefaultChannelLeaveJoinMessages": true`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------------------------------+

Enable Hardened Mode (Experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Enables a hardened mode for Mattermost that makes user experience trade-offs in the interest of security.

**False**: Disables hardened mode.

Changes made when hardened mode is enabled:

- Failed login returns a generic error message instead of a specific message for username and password.
- If `multi-factor authentication (MFA) <https://docs.mattermost.com/onboard/multi-factor-authentication.html>`__ is enabled, the route to check if a user has MFA enabled always returns true. This causes the MFA input screen to appear even if the user does not have MFA enabled. The user may enter any value to pass the screen. Note that hardened mode does not affect user experience when MFA is enforced.
- Password reset does not inform the user that they can not reset their SSO account through Mattermost and instead claims to have sent the password reset email.
- Mattermost sanitizes all 500 errors before returned to the client. Use the supplied ``request_id`` to match user facing errors with the server logs.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalEnableHardenedMode": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------------+

Enable AD/LDAP Group Sync
^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |cloud| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

**True**: Enables AD/LDAP Group Sync configurable under **User Management > Groups**.

**False**: Disables AD/LDAP Group Sync and removes **User Management > Groups** from the System Console.

For more information on AD/LDAP Group Sync, please see the `AD/LDAP Group Sync documentation <https://docs.mattermost.com/onboard/ad-ldap-groups-synchronization.html>`_.

+-----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalLdapGroupSync": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------------+

Enable Preview Features
^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Preview features can be enabled from **Account Settings > Advanced > Preview pre-release features**.

**False**: Disables and hides preview features from **Account Settings > Advanced > Preview pre-release features**.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePreviewFeatures": true`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

Enable Theme Selection
^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20*

**True**: Enables the **Display > Theme** tab in Account Settings so users can select their theme.

**False**: Users cannot select a different theme. The **Display > Theme** tab is hidden in Account Settings.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableThemeSelection": true`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------+

Allow Custom Themes
^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20*

**True**: Enables the **Display > Theme > Custom Theme** section in Account Settings.

**False**: Users cannot use a custom theme. The **Display > Theme > Custom Theme** section is hidden in Account Settings.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowCustomThemes": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

Default Theme
^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20*

Set a default theme that applies to all new users on the system.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DefaultTheme": "default"`` with options ``"default"``, ``"organization"``, ``"mattermostDark"``, and ``"windows10"``. |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Tutorial (Experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Users are prompted with a tutorial when they open Mattermost for the first time after account creation.

**False**: The tutorial is disabled. Users are placed in Town Square when they open Mattermost for the first time after account creation.

+--------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableTutorial": true`` with options ``true`` and ``false``.                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------+

Enable Onboarding 
^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: New Mattermost users are shown key tasks to complete as part of initial onboarding.

**False**: User onboarding tasks are disabled. Users are placed in Town Square when they open Mattermost for the first time after account creation.

+--------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOnboarding": true`` with options ``true`` and ``false``.                                |
+--------------------------------------------------------------------------------------------------------------------------------------------+

Enable User Typing Messages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting determines whether "user is typing..." messages are displayed below the message box. Disabling the setting in larger deployments may improve server performance.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserTypingMessages": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------------+

Time Between User Typing Updates (User Typing Timeout)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting defines how frequently "user is typing..." messages are updated, measured in milliseconds.

+----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TimeBetweenUserTypingUpdatesMilliseconds": 5000`` with numerical input. |
+----------------------------------------------------------------------------------------------------------------------+

Primary Team (Experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

The primary team of which users on the server are members. When a primary team is set, the options to join other teams or leave the primary team are disabled.

If the team URL of the primary team is https://example.mattermost.com/myteam/, then set the value to ``myteam`` in ``config.json``.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalPrimaryTeam": ""`` with string input.                  |
+-----------------------------------------------------------------------------------------------------------------+

SAML Settings
~~~~~~~~~~~~~

SAML Login Button Color
^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Specify the color of the SAML login button for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonColor": ""`` with string input.                                       |
+-------------------------------------------------------------------------------------------------------------------------------+

SAML Login Button Border Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Specify the color of the SAML login button border for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonBorderColor": ""`` with string input.                                 |
+-------------------------------------------------------------------------------------------------------------------------------+

SAML Login Button Text Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |cloud| |self-hosted|

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
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

Specify the color of the SAML login button text for white labeling purposes. Use a hex code with a #-sign before the code. This setting only applies to the mobile apps.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LoginButtonTextColor": ""`` with string input.                                   |
+-------------------------------------------------------------------------------------------------------------------------------+

Collapsed Reply Threads (Beta)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

Collapsed Reply Threads offers an enhanced experience for users communicating in threads and replying to messages. Collapsed Reply Threads are available in Mattermost Cloud and from self-hosted Mattermost v5.37 as an early access beta, and are disabled by default. See our `Organizing Conversations using Collapsed Reply Threads (Beta) <https://docs.mattermost.com/messaging/organizing-conversations.html>`__ documentation to learn more about this feature.

System Admins can set the default appearance of Collapsed Reply Threads for their end users by going to **System Console > Experimental > Features**, then setting **Collapsed Reply Threads** to one of the following options:

**Enabled (Default Off)**: Enable Collapsed Reply Threads functionality on the server. Users can choose to `enable Collapsed Reply Threads <https://docs.mattermost.com/messaging/managing-account-settings.html#collapsed-reply-threads-beta>`__ for their Mattermost account in **Account Settings**.

**Disabled**: Disable Collapsed Reply Threads functionality.

+-------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ServiceSettings.CollapsedThreads": disabled`` with options ``disabled`` and ``default_off``. |
+-------------------------------------------------------------------------------------------------------------------------------------------+

Use Channel Name in Email Notifications (Experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

**True**: Channel and team name appears in email notification subject lines. Useful for servers using only one team.

**False**: Only team name appears in email notification subject line.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UseChannelInEmailNotifications": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------------+

User Status Away Timeout
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |cloud| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |cloud| image:: ../images/cloud-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Cloud deployments.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting defines the number of seconds after which the user's status indicator changes to "Away", when they are away from Mattermost.

+--------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"UserStatusAwayTimeout": 300`` with numerical input. |
+--------------------------------------------------------------------------------------------------+

Settings configurable only in ``config.json``
----------------------------------------------

There are a number of settings customizable in ``config.json`` which are unavailable in the System Console and require updating from the file itself.

Service Settings
~~~~~~~~~~~~~~~~

Automatically Follow Threads
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

This setting has been added as a requirement to support `Collapsed Reply Threads <https://docs.mattermost.com/messaging/organizing-conversations.html>`_, and may affect server performance. We recommend that you review our `documentation on hardware requirements <https://docs.mattermost.com/install/requirements.html#hardware-requirements>`_ to ensure your servers are appropriately scaled for the size of your user base.

**True**: Threads a user starts, participates in, or is mentioned in are automatically followed. A new ``Threads`` table is added in the database that tracks threads and thread participants, and a ``ThreadMembership`` table tracks followed threads for each user and the read or unread state of each followed thread.   

**False**: Threads are not automatically followed and Collapsed Reply Threads cannot be enabled.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ThreadAutoFollow": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

.. note::

   Enabling this configuration setting doesn’t retroactively follow threads for older actions taken prior to the setting being enabled. For example, if a user comments on an old thread, they automatically follow the thread if this setting is enabled regardless of whether the thread existed when this setting was disabled.

WebSocket URL
^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

This setting allows the server to instruct clients where they should try to connect WebSockets to.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"WebsocketURL": ""`` with string input. |
+-------------------------------------------------------------------------------------+

License File Location
^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Path and filename of the license file on disk. On startup, if Mattermost cannot find a valid license in the database from a previous upload, it looks here. It can be an absolute path or a path relative to the ``mattermost`` directory.

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LicenseFileLocation": ""`` with string input.  |
+---------------------------------------------------------------------------------------------+

TLS Minimum Version
^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The minimum TLS version used by the Mattermost server. TLS v1.2 is default given insecurities for TLS 1.0 and 1.1.

.. note::
  This setting only takes effect if you are using the built-in server binary directly, and not using a reverse proxy layer such as NGINX.

+-------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TLSMinVer": "1.2"`` with string input. |
+-------------------------------------------------------------------------------------+

Trusted Proxy IP Header
^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Specified headers that will be checked one by one for IP addresses (order is important). All other headers are ignored.

Starting with v5.12, new configs will have this set by default to ``[]``, meaning that no header will be trusted. Configs created prior to v5.12 without this config entry will have it set to ``["X-Forwarded-For", "X-Real-Ip"]`` on upgrade in order to maintain backwards compatibility.

We recommend keeping the default setting when Mattermost is running without a proxy, to avoid the client sending the headers and bypassing rate limiting and/or the audit log. For environments that use a reverse proxy this problem does not exist, provided that the headers are set by the reverse proxy. In those environments, only explicitly whitelist the header that is set by the reverse proxy and no additional values.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TrustedProxyIPHeader": []`` with string array input consisting of header names, such as ``["X-Forwarded-For", "X-Real-Ip"]``. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enable Strict Transport Security (HSTS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Adds the Strict Transport Security (HSTS) header to all responses, forcing the browser to request all resources via HTTPS. Learn more `here <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security>`__.

**False**: No restrictions on TLS transport. Strict Transport Security (HSTS) header is not added to responses.

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TLSStrictTransport": false`` with options ``true`` and ``false``.                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

Secure TLS Transport Expiry
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The time in seconds that the browser remembers a site is only to be accessed using HTTPS. After this period, a site can be accessed using HTTP unless ``TLSStrictTransport`` is set to ``true``. Defaults to two years. Learn more `here <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security>`__.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TLSStrictTransportMaxAge": 63072000`` with numerical input.    |
+-------------------------------------------------------------------------------------------------------------+

TLS Cipher Overwrites
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Set TLS ciphers overwrites to meet requirements from legacy clients which don't support modern ciphers, or to limit the types of accepted ciphers.

If none specified, the Mattermost server assumes a set of currently considered secure ciphers, and allows overwrites in the edge case. See the ``ServerTLSSupportedCiphers`` variable in `/model/config.go <https://github.com/mattermost/mattermost-server/blob/master/model/config.go>`__ for the list of ciphers considered secure.

.. note::
  This setting only takes effect if you are using the built-in server binary directly, and not using a reverse proxy layer such as NGINX.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"TLSStrictTransportMaxAge": 63072000`` with numerical input.    |
+-------------------------------------------------------------------------------------------------------------+

Go Routine Health Threshold
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Set a threshold on the number of goroutines when the Mattermost system is considered to be in a healthy state. When goroutines exceed this limit, a warning is returned in the server logs.

To turn off checking for the threshold, set this value to ``-1``.

+----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GoroutineHealthThreshold": -1`` with numerical input.       |
+----------------------------------------------------------------------------------------------------------+

Allow Cookies for Subdomains
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Allows cookies for subdomains by setting the domain parameter on Mattermost cookies.

**False**: Cookies not allowed for subdomains.

+----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowCookiesForSubdomains": true`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------+

Cluster Log Timeout
^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

This setting defines the frequency of cluster request time logging for :doc:`../scale/performance-monitoring`, measured in milliseconds.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ClusterLogTimeoutMilliseconds": 2000`` with numerical input. |
+-----------------------------------------------------------------------------------------------------------+

Read Only Config
^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Changes made to settings in the System Console are ignored.

**False**: Changes made to settings in the System Console are written to ``config.json``.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ReadOnlyConfig": true`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------+

Enable Post Search
^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

If this setting is enabled, users can search messages. Disabling search can result in a performance increase, but users get an error message when they attempt to use the search box.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnablePostSearch": true`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

Enable File Search
^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

This configuration setting enables users to search documents attached to messages by filename. To enable users to search documents by their content, you must also enable the ``ExtractContent`` configuration setting. See our `Enable Document Search by Content <https://docs.mattermost.com/configure/configuration-settings.html#enable-document-search-by-content>`__ documentation for details. Document content search is available in Mattermost Server from v5.35, with mobile support coming soon. 

**True**: Supported document types are searchable by their filename. 

**False**: File-based searches are disabled.

+-----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ServiceSettings.EnableFileSearch": true`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------------------+

Enable User Status Updates
^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Turn status updates off to improve performance. When status updates are off, users appear online only for brief periods when posting a message, and only to members of the channel in which the message is posted.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUserStatuses": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

WebSocket Secure Port
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``. Changes to this setting require a server restart before taking effect.

(Optional) This setting defines the port on which the secured WebSocket will listen using the ``wss`` protocol. Defaults to ``443``. When the client attempts to make a WebSocket connection it first checks to see if the page is loaded with HTTPS. If so, it will use the secure WebSocket connection. If not, it will use the unsecure WebSocket connection. IT IS HIGHLY RECOMMENDED PRODUCTION DEPLOYMENTS ONLY OPERATE UNDER HTTPS AND WSS.


+------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"WebsocketSecurePort": 443`` with numerical input. |
+------------------------------------------------------------------------------------------------+

WebSocket Port
^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``. Changes to this setting require a server restart before taking effect.

(Optional) This setting defines the port on which the unsecured WebSocket will listen using the ``ws`` protocol. Defaults to ``80``. When the client attempts to make a WebSocket connection it first checks to see if the page is loaded with HTTPS. If so, it will use the secure WebSocket connection. If not, it will use the unsecure WebSocket connection. IT IS HIGHLY RECOMMENDED PRODUCTION DEPLOYMENTS ONLY OPERATE UNDER HTTPS AND WSS.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``WebsocketPort": 80`` with numerical input. |
+----------------------------------------------------------------------------------------+

Enable API Team Deletion
^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: The ``api/v4/teams/{teamid}?permanent=true`` API endpoint can be called by Team and System Admins to permanently delete a team.

**False**: The API endpoint cannot be called. Note that ``api/v4/teams/{teamid}`` can still be used to soft delete a team.

.. note::
  mmctl local mode ignores this setting and behaves as though ``EnableAPITeamDeletion`` is set to ``true``.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAPITeamDeletion": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

Enable API User Deletion
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: The ``api/v4/users/{userid}?permanent=true`` API endpoint can be called by System Admins, or users with appropriate permissions, to permanently delete a user.

**False**: The API endpoint cannot be called. Note that ``api/v4/users/{userid}`` can still be used to soft delete a user.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAPIUserDeletion": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

.. note::
  mmctl local mode ignores this setting and behaves as though ``EnableAPIUserDeletion`` is set to ``true``.

Enable API Channel Deletion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: The ``api/v4/channels/{channelid}?permanent=true`` API endpoint can be called by System Admins, or users with appropriate permissions, to permanently delete a channel.

**False**: The API endpoint cannot be called. Note that ``api/v4/channels/{channelid}`` can still be used to soft delete a channel.

+----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAPIChannelDeletion": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------------------+

.. note::
  mmctl local mode ignores this setting and behaves as though ``EnableAPIChannelDeletion`` is set to ``true``.

Enable OpenTracing
^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: A Jaeger client is instantiated and is used to trace each HTTP request as it goes through App and Store layers. Context is added to App and Store and is passed down the layer chain to create OpenTracing 'spans'.

By default, in order to avoid leaking sensitive information, no method parameters are reported to OpenTracing. Only the name of the method is reported.

**False**: OpenTracing is not enabled.

+---------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableOpenTracing": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------+

Import Settings Default Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The directory where the imported files are stored. The path is relative to the ``FileSettings`` directory. By default, imports are stored under ``./data/import``.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting under the ``ImportSettings`` section is ``Directory: ./import`` with string input. |
+---------------------------------------------------------------------------------------------------------------------------+

Import Settings Default Retention Days
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The number of days to retain the imported files before deleting them.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting under the ``ImportSettings`` section is ``RetentionDays: 30`` with numerical input. |
+----------------------------------------------------------------------------------------------------------------------------+

Export Settings Default Directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The directory where the exported files are stored. The path is relative to the ``FileSettings`` directory. By default, exports are stored under ``./data/export``.

+---------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting under the ``ExportSettings`` section is ``Directory: ./export`` with string input. |
+---------------------------------------------------------------------------------------------------------------------------+

Export Settings Default Retention Days
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The number of days to retain the exported files before deleting them.

+----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting under the ``ExportSettings`` section is ``RetentionDays: 30`` with numerical input. |
+----------------------------------------------------------------------------------------------------------------------------+

Enable Local Mode
^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables local mode for mmctl.

**False**: Prevents local mode for mmctl.

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableLocalMode": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------+

Enable Local Mode Socket Location
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The path for the socket that the server will create for mmctl to connect and communicate through local mode. If the default value for this key is changed, you will need to point mmctl to the new socket path when in local mode, using the ``--local-socket-path /new/path/to/socket`` flag in addition to the ``--local`` flag.

If nothing is specified, the default path that both the server and mmctl assumes is ``/var/tmp/mattermost_local.socket``.

+--------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LocalModeSocketLocation": "/var/tmp/mattermost_local.socket"`` with string input. |
+--------------------------------------------------------------------------------------------------------------------------------+

Scoping IDP Provider Id
^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Allows an authenticated user to skip the initial login page of their federated Azure AD server, and only require a password to log in.

+---------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ScopingIDPProviderId": ""`` with string input. |
+---------------------------------------------------------------------------------------------+

Scoping IDP Name
^^^^^^^^^^^^^^^^

|enterprise| |professional| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Adds the name associated with a user's Scoping Identity Provider ID.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ScopingIDPName": ""`` with string input. |
+---------------------------------------------------------------------------------------+

Global Relay SMTP Server Timeout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available as an add-on to legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

The number of seconds that can elapse before the connection attempt to the SMTP server is abandoned. The default value is 1800 seconds. This setting is currently not available in the System Console and can only be set in ``config.json``.

+-----------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"GlobalRelaySettings.SMTPServerTimeout": "1800"`` with numerical input.   |
+-----------------------------------------------------------------------------------------------------------------------+

Batch Size
^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Determines how many new posts are batched together to a compliance export file.

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BatchSize": 10000`` with numerical input. |
+----------------------------------------------------------------------------------------+

App Custom URL Schemes
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Define valid custom URL schemes for redirect links provided by custom-built mobile Mattermost apps. This ensures users are redirected to the custom-built mobile app and not Mattermost's mobile client. 

When configured, after OAuth or SAML user authentication is complete, custom URL schemes sent by mobile clients are validated to ensure they don't include default schemes such as ``http`` or ``https``. Mobile users are then redirected back to the mobile app using the custom scheme URL provided by the mobile client. We recommend that you update your mobile client values as well with valid custom URL schemes.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"NativeAppSettings.AppCustomURLSchemes"`` with an array of strings as input. For example: ``[custom-app://, some-app://]``.                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


Colorize plain text console logs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: When logged events are output to the console as plain text, colorize log levels details.

**False**: Plain text log details aren't colorized in the console.

+----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableColor": false`` with options ``true`` and ``false``.                                |
+----------------------------------------------------------------------------------------------------------------------------------------+

SQL Settings
~~~~~~~~~~~~

Read Replicas
^^^^^^^^^^^^^^

|enterprise| |professional| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20*

This setting isn't available in the System Console and can only be set in ``config.json``. Changes to this setting require a server restart before taking effect.

Specifies the connection strings for the read replica databases. Each string must be in the same form as used for the `Data Source`_ setting.

+---------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DataSourceReplicas": []`` with string array input consisting of database connection strings.   |
+---------------------------------------------------------------------------------------------------------------------------------------------+

Search Replicas
^^^^^^^^^^^^^^^^

|enterprise| |professional| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20*

This setting isn't available in the System Console and can only be set in ``config.json``. Changes to this setting require a server restart before taking effect.

Specifies the connection strings for the search replica databases. A search replica is similar to a read replica, but is used only for handling search queries. Each string must be in the same form as used for the `Data Source`_ setting.

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DataSourceSearchReplicas": []`` with string array input consisting of database connection strings.   |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

Replica Lag Settings
^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Specifies a connection string and user-defined SQL queries on the database to measure replica lag for a single replica instance. These settings monitor absolute lag based on binlog distance/transaction queue length, and the time taken for the replica to catch up.

+-------------------------------------------------------------------------------------------------------+
| This feature’s ``config.json`` setting is ``"ReplicaLagSettings": []`` with string array input.       |
+-------------------------------------------------------------------------------------------------------+

String array input consists of:

- ``DataSource``: The DB credentials to connect to the replica instance.
- ``QueryAbsoluteLag``: A plain SQL query that must return a single row. The first column must be the node value of the Prometheus metric, and the second column must be the value of the lag used to measure absolute lag.
- ``QueryTimeLag``: A plain SQL query that must return a single row. The first column must be the node value of the Prometheus metric, and the second column must be the value of the lag used to measure the time lag.

Examples:

For AWS Aurora instances, ``QueryAbsoluteLag`` can be:

.. code-block:: sh

   select server_id, highest_lsn_rcvd-durable_lsn as bindiff from aurora_global_db_instance_status() where server_id=<>

And for AWS Aurora instances, ``QueryTimeLag`` can be:

.. code-block:: sh

   select server_id, visibility_lag_in_msec from aurora_global_db_instance_status() where server_id=<>

For MySQL Group Replication, the absolute lag can be measured from the number of pending transactions in the applier queue:

.. code-block:: sh

   select member_id, count_transactions_remote_in_applier_queue FROM performance_schema.replication_group_member_stats where member_id=<>

Image Settings
~~~~~~~~~~~~~~

Maximum Image Resolution
^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Maxiumum image resolution size for message attachments in megapixels. 

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileSettings.MaxImageResolution": 33177600`` with numerical input.     |
+---------------------------------------------------------------------------------------------------------------------+

File Settings
~~~~~~~~~~~~~~

Initial Font
^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Font used in auto-generated profile pics with colored backgrounds.

+-----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"InitialFont": "luximbi.ttf"`` with string input. |
+-----------------------------------------------------------------------------------------------+

Amazon S3 Signature V2
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

By default, Mattermost uses Signature V4 to sign API calls to AWS, but under some circumstances, V2 is required. For more information about when to use V2, see https://docs.aws.amazon.com/general/latest/gr/signature-version-2.html.

**True**: Use Signature Version 2 Signing Process.

**False**: Use Signature Version 4 Signing Process.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AmazonS3SignV2": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

Amazon S3 Path
^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Allows using the same S3 bucket for multiple deployments.

+------------------------------------------------------------------------------------------------------------+
| This feature’s ``config.json`` setting is ``"AmazonS3PathPrefix: ""`` with string input.                   |
+------------------------------------------------------------------------------------------------------------+

GitLab Settings
~~~~~~~~~~~~~~~

Scope
^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Not available in Cloud Starter*

This setting isn't available in the System Console and can only be set in ``config.json``.

Standard setting for OAuth to determine the scope of information shared with OAuth client. Not currently supported by GitLab OAuth.

+------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Scope": ""`` with string input. |
+------------------------------------------------------------------------------+

Google Settings
~~~~~~~~~~~~~~~

Scope
^^^^^^

|enterprise| |professional| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Standard setting for OAuth to determine the scope of information shared with OAuth client. Recommended setting is ``profile email``.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Scope": "profile email"`` with string input. |
+-------------------------------------------------------------------------------------------+

Office 365 Settings
~~~~~~~~~~~~~~~~~~~~

Scope
^^^^^^

|enterprise| |professional| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Standard setting for OAuth to determine the scope of information shared with OAuth client. Recommended setting is ``User.Read``.

+---------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Scope": "User.Read"`` with string input. |
+---------------------------------------------------------------------------------------+

Cluster Settings
~~~~~~~~~~~~~~~~

Maximum Idle Connections
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The maximum number of idle connections held open from one server to all others in the cluster.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxIdleConns": 100`` with numerical input. |
+-----------------------------------------------------------------------------------------+

Maximum Idle Connections per Host
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The maximum number of idle connections held open from one server to another server in the cluster.

+------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxIdleConnsPerHost": 128`` with numerical input. |
+------------------------------------------------------------------------------------------------+

Idle Connection Timeout (in Milliseconds)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The number of milliseconds to leave an idle connection open between servers in the cluster.

+----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IdleConnTimeoutMilliseconds": 90000`` with numerical input. |
+----------------------------------------------------------------------------------------------------------+

Network Interface
^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

An IP address used to identify the device that does automatic IP detection in High Availability clusters.

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"NetworkInterface": ""`` with string input. |
+-----------------------------------------------------------------------------------------+

Bind Address
^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

An IP address used to bind cluster traffic to a specific network device. This setting is used primarily for servers with multiple network devices or different Bind Address and Advertise Address like in deployments that involve NAT (Network Address Translation).

+------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BindAddress": ""`` with string input. |
+------------------------------------------------------------------------------------+

Advertise Address
^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The IP address used to access the server from other nodes. This settings is used primary when cluster nodes are not in the same network and involve NAT (Network Address Translation).

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AdvertiseAddress": ""`` with string input. |
+-----------------------------------------------------------------------------------------+

Metrics Settings
~~~~~~~~~~~~~~~~~

Block Profile Rate
^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``. Changes to this setting require a server restart before taking effect.

Value that controls the `fraction of goroutine blocking events reported in the blocking profile <https://golang.org/pkg/runtime/#SetBlockProfileRate>`__.

The profiler aims to sample an average of one blocking event per rate nanoseconds spent blocked.

To include every blocking event in the profile, set the rate to ``1``. To turn off profiling entirely, set the rate to ``0``.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BlockProfileRate": 0`` with options ``0`` and ``1``. |
+---------------------------------------------------------------------------------------------------+

Plugin Settings
~~~~~~~~~~~~~~~

Signature Public Key Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

In addition to the Mattermost plugin signing key built into the server, each public key specified here is trusted to validate plugin signatures.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SignaturePublicKeyFiles": {}`` with string array input consisting of contents that are relative or absolute paths to signature files.              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Chimera OAuth Proxy URL
^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Specify the `Chimera <https://github.com/mattermost/chimera>`__ URL used by Mattermost plugins to connect with pre-created OAuth applications.

+-------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ChimeraOAuthProxyUrl": {}`` with string input.                             |
+-------------------------------------------------------------------------------------------------------------------------+

Custom User Attributes
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Learn more `in our documentation <https://github.com/mattermost/mattermost-plugin-custom-attributes/blob/master/README.md>`_.

GitHub
^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Learn more `in our documentation <https://github.com/mattermost/mattermost-plugin-github/blob/master/README.md>`_.

Jira
^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Learn more `in our documentation <https://github.com/mattermost/mattermost-plugin-jira/blob/master/README.md>`_.

Net Promoter Score
^^^^^^^^^^^^^^^^^^

This setting isn't available in the System Console and can only be set in ``config.json``.

Learn more `in our documentation <https://docs.mattermost.com/manage/user-satisfaction-surveys.html>`_.

Welcome Bot
^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Learn more `in our documentation <https://github.com/mattermost/mattermost-plugin-welcomebot/blob/master/README.md>`_.

Experimental Settings only in ``config.json``
---------------------------------------------

Audit settings
~~~~~~~~~~~~~~

The audit settings output audit records to syslog (local or remote server via TLS) and/or to a local file. Both are disabled by default. They can be enabled simultaneously.

Enable Reliable Websockets
^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Enable this setting to make websocket messages more reliable by buffering messages during a connection loss and then re-transmitting all unsent messages when the connection is revived. This setting can only be changed from ``config.json`` file, it cannot be changed from the System Console user interface.

+---------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableReliableWebsockets": true`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------------------+

Remote Clusters
^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Enable this setting to add, remove, and view remote clusters for shared channels. 

**True**: System Admins can manage remote clusters using the System Console.

**False**: Remote cluster management is disabled.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RemoteClusters": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

Syslog configuration options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Enable this setting to write audit records to a local or remote syslog, specifying the IP, port, user-generated fields, and certificate settings. 

**True**: Syslog output is enabled.

**False**: Syslog output is disabled.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SysLogEnabled": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------+

Syslog IP
^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The IP address or domain of the syslog server. Use ``localhost`` for local syslog. 

+-------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SysLogIP": "localhost"`` with string input consisting of an IP address or domain name. |
+-------------------------------------------------------------------------------------------------------------------------------------+

Syslog port
^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The port that the syslog server is listening on. The default port is 6514. 

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SysLogPort": 6514`` with numeric input consisting of a port number. |
+------------------------------------------------------------------------------------------------------------------+

Syslog tag
^^^^^^^^^^

all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.


This setting isn't available in the System Console and can only be set in ``config.json``.

The syslog metadata tag field.

+-------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SysLogTag": ""`` with string input consisting of a user-defined tag field. |
+-------------------------------------------------------------------------------------------------------------------------+

Syslog cert
^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

This is the path to the syslog server certificate for TLS connections (``.crt`` or ``.pem``). 

+-----------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SysLogCert": ""`` with string input consisting of the path to the certificate. |
+-----------------------------------------------------------------------------------------------------------------------------+

Syslog insecure
^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

This setting controls whether a client verifies the server's certificate chain and host name. If ``true``, TLS accepts any certificate presented by the server and any host name in that certificate. In this mode, TLS is susceptible to man-in-the-middle attacks. 

.. note:: 
   This should be used only for testing and not in a production environment.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SysLogInsecure": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

Syslog max queue size
^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

This setting determines how many audit records can be queued/buffered at any point in time when writing to syslog. The default is 1000 records. 
This setting can be left as default unless you are seeing audit write failures in the server log and need to adjust the number accordingly.

+------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"SysLogMaxQueueSize": 1000`` with numerical input. |
+------------------------------------------------------------------------------------------------+

File configuration options
^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Enable this setting to write audit files locally, specifying size, backup interval, compression, and maximum age to manage file rotation. 

**True**: File output is enabled.

**False**: File output is disabled.

+---------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileEnabled": false`` with options ``true`` and ``false``. |
+---------------------------------------------------------------------------------------------------------+

File name
^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

This is the path to the output file location. 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileName": ""`` with string input consisting of a user-defined path (e.g. ``/var/log/mattermost_audit.log``).                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

File max size MB
^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

This is the maximum size (measured in megabytes) that the file can grow before triggering rotation. The default setting is 100. 

+------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileMaxSizeMB": 100`` with numerical input. |
+------------------------------------------------------------------------------------------+

File max age days
^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

This is the maximum age in days a file can reach before triggering rotation. The default value is 0, indicating no limit on the age. 

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileMaxAgeDays": 0`` with numerical input. |
+-----------------------------------------------------------------------------------------+

File max backups
^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

This is the maximum number of rotated files kept; the oldest is deleted first. The default value is 0, indicating no limit on the number of backups. 

+-----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileMaxBackups": 0`` with numerical input. |
+-----------------------------------------------------------------------------------------+

File compress
^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

When ``true``, rotated files are compressed using ``gzip``. 

+----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileCompress": false`` with options ``true`` and ``false``. |
+----------------------------------------------------------------------------------------------------------+

File max queue size
^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

This setting determines how many audit records can be queued/buffered at any point in time when writing to a file. The default is 1000 records. 
This setting can be left as default unless you are seeing audit write failures in the server log and need to adjust the number accordingly.

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileMaxQueueSize": 1000`` with numerical input. |
+----------------------------------------------------------------------------------------------+

Advanced Audit Logging Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Output logs to multiple targets
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Send log records to multiple targets:

- Multiple local file targets
- Multiple syslogs
- Multiple TCP sockets

Allow any combination of local file, syslog, and TCP socket targets. 

File target supports rotation and compression triggered by size and/or duration. Syslog target supports local and remote syslog servers, with or without TLS transport. TCP socket target can be configured with an IP address or domain name, port, and optional TLS certificate.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``ExperimentalAuditSettings.AdvancedLoggingConfig`` which can contain a filespec to another config file, a database DSN, or JSON.   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Options are outlined in this text file: `Log Settings Options <https://github.com/mattermost/docs/files/5066579/Log.Settings.Options.txt>`_. Sample config: `Advanced Logging Options Sample.json.zip <https://github.com/mattermost/docs/files/5066597/Advanced.Logging.Options.Sample.json.zip>`_.

Service Settings
~~~~~~~~~~~~~~~~

Group Unread Channels (Experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

This setting applies to the new sidebar only. You must disable the `Enable Legacy Sidebar <https://docs.mattermost.com/configure/configuration-settings.html#enable-legacy-sidebar>`__ configuration setting to see and enable this functionality in the System Console. 

**Default Off**: Disables the unread channels sidebar section for all users by default. Users can enable it in **Account Settings > Sidebar > Group unread channels separately**.

**Default On**: Enables the unread channels sidebar section for all users by default. Users can disable it in **Account Settings > Sidebar > Group unread channels separately**. 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalGroupUnreadChannels": "default_off"`` with options ``"default_off"`` and ``"default_on"``. |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

Strict CSRF Token Enforcement (Experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables CSRF protection tokens for additional hardening compared to the currently used custom header. When the user logs in, an additional cookie is created with the CSRF token contained.

**False**: Disables CSRF protection tokens.

+-------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalStrictCSRFEnforcement": false`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------------------+

Restrict System Admin
^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Restricts the System Admin from viewing and modifying a subset of server configuration settings from the System Console. Not recommended for use in on-prem installations. This is intended to support Mattermost Private Cloud in giving the System Admin role to users but restricting certain actions only for Cloud Admins.

**False**: No restrictions are applied to the System Admin role.

+-------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RestrictSystemAdmin": "false"`` with options ``true`` and ``false``. |
+-------------------------------------------------------------------------------------------------------------------+

Team Settings
~~~~~~~~~~~~~~

Teammate Name Display
^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Control Teammate Name Display at the system level. 

**True**: Allows System Admins to control Teammate Name Display at the system level.

**False**: System Admins cannot control Teammate Name Display at the system level.

+------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LockTeammateNameDisplay": []`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------------+

Default Channels (Experimental)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Default channels every user is added to automatically after joining a new team. Only applies to Public channels, but affects all teams on the server. 

When not set, every user is added to the ``off-topic`` and ``town-square`` channels by default.

.. note::

   Even if ``town-square`` is not listed, every user is added to that channel after joining a new team.

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExperimentalDefaultChannels": []`` with string array input consisting of channel names, such as ``["announcement", "developers"]``. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Email Settings
~~~~~~~~~~~~~~

Client Requirement Settings (Experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Latest Android Version
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The latest version of the Android React Native app that is recommended for use. 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AndroidLatestVersion": ""`` with string input corresponding to a version string, such as ``"1.2.0"``. |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

Minimum Android Version
^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The minimum version of the Android React Native app that is required to be used. 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AndroidMinVersion": ""`` with string input corresponding to a version string, such as ``"1.2.0"``. |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

Latest Desktop Version
^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The latest version of the desktop app that is recommended for use. 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DesktopLatestVersion": ""`` with string input corresponding to a version string, such as ``"1.2.0"``. |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

Minimum Destop Version
^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The minimum version of the desktop app that is required to be used. 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DesktopMinVersion": ""`` with string input corresponding to a version string, such as ``"1.2.0"``. |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

Latest iOS Version
^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The latest version of the iOS app that is recommended for use. 

+------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IosLatestVersion": ""`` with string input corresponding to a version string, such as ``"1.2.0"``. |
+------------------------------------------------------------------------------------------------------------------------------------------------+

Minimum iOS Version
^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The minimum version of the iOS React Native app that is required to be used. 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IosMinVersion": ""`` with string input corresponding to a version string, such as ``"1.2.0"``. |
+---------------------------------------------------------------------------------------------------------------------------------------------+

Push Notification Buffer
^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Used to control the buffer of outstanding Push Notification messages to be sent. If the number of messages exceeds that number, then the request making the Push Notification will be blocked until there's room. 

+---------------------------------------------------------------------------------------------------------------------------------------------+
| This feature’s ``config.json`` setting is ``"PushNotificationBuffer": 1000"`` with numerical input.                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------+

Theme Settings (Experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Allowed Themes
^^^^^^^^^^^^^^^

|enterprise| |professional| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Select the themes that can be chosen by users when ``EnableThemeSelection`` is set to ``true``. 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowedThemes": []`` with string array input consisting of the options ``"default"``, ``"organization"``, ``"mattermostDark"``, and ``"windows10"``, such as ``["mattermostDark", "windows10"]``. |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Experimental Settings
~~~~~~~~~~~~~~~~~~~~~

Disable Post Metadata
^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Disabling post metadata is only recommended if you are experiencing a significant decrease in performance around channel and post load times.

**False**: Load channels with more accurate scroll positioning by loading post metadata.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"DisablePostMetadata": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------------+

Analytics Settings
~~~~~~~~~~~~~~~~~~~

Maximum Users for Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |professional| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |professional| image:: ../images/professional-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Professional subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E10 and E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Sets the maximum number of users on the server before statistics for total posts, total hashtag posts, total file posts, posts per day, and active users with posts per day are disabled. 

This setting is used to maximize performance for large Enterprise deployments.

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"MaxUsersForStatistics": 2500`` with numerical input. |
+---------------------------------------------------------------------------------------------------+

Elasticsearch Settings
~~~~~~~~~~~~~~~~~~~~~~~~

Post Index Replicas
^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

The number of replicas to use for each post index. If this setting is changed, it only applies to newly-created indexes. To apply the change to existing indexes, purge and rebuild the index after changing this setting. 

+---------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PostIndexReplicas": 2`` with numerical input.        |
+---------------------------------------------------------------------------------------------------+

Post Index Shards
^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

The number of shards to use for each post index. If this setting is changed, it only applies to newly-created indexes. To apply the change to existing indexes, purge and rebuild the index after changing this setting. 

+-------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PostIndexShards": 1`` with numerical input.        |
+-------------------------------------------------------------------------------------------------+

Aggregate Search Indexes
^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Elasticsearch indexes over the age specified by this setting will be aggregated during the daily scheduled job. 

.. note::
  If you're using `data retention <https://docs.mattermost.com/comply/data-retention-policy.html>`_ and `ElasticSearch <https://docs.mattermost.com/scale/elasticsearch.html>`_, ensure the `ElasticSearch aggregate search indexes <https://docs.mattermost.com/configure/configuration-settings.html#aggregate-search-indexes>`_ setting is set to a value that is greater than your data retention policy in days.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AggregatePostsAfterDays": 365`` with numerical input.        |
+-----------------------------------------------------------------------------------------------------------+

Post Aggregator Start Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

The start time of the daily scheduled aggregator job. Must be a 24-hour time stamp in the form ``HH:MM``. This setting is based on the local time of the server.

+--------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"PostsAggregatorJobStartTime": "03:00"`` with 24-hour timestamp input in the form ``"HH:MM"``. |
+--------------------------------------------------------------------------------------------------------------------------------------------+

Index Prefix
^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Prefix on the Elasticsearch index name. Enables the use of Mattermost Elasticsearch on a shared Elasticsearch cluster. 

+----------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IndexPrefix": ""`` with string input.     |
+----------------------------------------------------------------------------------------+

.. note::
  When this setting is used, all Elasticsearch indexes created by Mattermost are given this prefix. You can set different prefixes so that multiple Mattermost deployments can share an Elasticsearch cluster without the index names colliding.
  
Live Indexing Batch Size
^^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Determines how many new posts are batched together before they are added to the Elasticsearch index. It may be necessary to increase this value to avoid hitting the rate limit of your Elasticsearch cluster on installs handling multiple messages per second. 

+--------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"LiveIndexingBatchSize": 1`` with numerical input.         |
+--------------------------------------------------------------------------------------------------------+

Request Timeout
^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Timeout in seconds for Elasticsearch calls.

+-------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RequestTimeoutSeconds": 30`` with numerical input.       |
+-------------------------------------------------------------------------------------------------------+

Bulk Indexing Time Window
^^^^^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Determines the maximum time window for a batch of posts being indexed by the Bulk Indexer. This setting servers as a performance optimisation for installs with over ~10 million posts in the database. Approximate this value based on the average number of seconds for 2,000 posts to be added to the database on a typical day in production. Setting this value too low will cause Bulk Indexing jobs to run slowly. 

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BulkIndexingTimeWindowSeconds": 3600`` with numerical input.       |
+-----------------------------------------------------------------------------------------------------------------+

Trace
^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Options for printing Elasticsearch trace errors.  Accepts ``error``, ``all``, or empty.  ``error`` will create the error trace when initialising the Elasticsearch client and will print any template creation or search query that returns an error as part of the error message. ``all`` will create the three traces (error, trace and info) for the driver and will not print the queries because they will be part of the trace log level of the driver. 

+-------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Trace": ""`` with string input.                          |
+-------------------------------------------------------------------------------------------------------+

Bleve Settings (Experimental)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Access the following configuration settings in the System Console by going to **Experimental > Bleve**.

Index Dir
^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Directory path to use for storing bleve indexes. 

.. tip::
   
   The bleve index directory path isn't required to exist within the ``mattermost`` directory. When it exists outside of the ``mattermost`` directory, no  additional steps are needed to preserve or reindex these files as part of a Mattermost upgrade. See our `Upgrading Mattermost Server <https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html>`__ documentation for details. 

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"IndexDir": ""`` with string input.                           |
+-----------------------------------------------------------------------------------------------------------+

Enable Indexing
^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: The indexing of new posts occurs automatically. Search queries will not use bleve search until **Enable Bleve for search queries** is enabled.

**False**: The indexing of new posts does not occur automatically.

+------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableIndexing": false`` with options ``true`` and ``false``. |
+------------------------------------------------------------------------------------------------------------+

Enable Searching
^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Search queries will use bleve search.

**False**: Search queries will not use bleve search.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableSearching": false`` with options ``true`` and ``false``.  |
+--------------------------------------------------------------------------------------------------------------+

Enable Autocomplete
^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Autocomplete queries will use bleve search.

**False**: Autocomplete queries will not use bleve search.

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableAutocomplete": false`` with options ``true`` and ``false``.  |
+-----------------------------------------------------------------------------------------------------------------+

Bulk Indexing Time Window Seconds
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Determines the maximum time window for a batch of posts being indexed by the Bulk Indexer. This setting serves as a performance optimization for installs with over ~10 million posts in the database. Approximate this value based on the average number of seconds for 2,000 posts to be added to the database on a typical day in production. Setting this value too low will cause Bulk Indexing jobs to run slowly. 

+-------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"BulkIndexingTimeWindowSeconds": 3600`` with numerical input.   |
+-------------------------------------------------------------------------------------------------------------+

Message Export Settings
~~~~~~~~~~~~~~~~~~~~~~~

Export From Timestamp
^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Set the Unix timestamp (seconds since epoch, UTC) to export data from. 

+----------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"ExportFromTimestamp": 0`` with numerical input. |
+----------------------------------------------------------------------------------------------+

File Location
^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.

Set the file location of the compliance exports. By default, they are written to the ``exports`` subdirectory of the configured `Local Storage directory <https://docs.mattermost.com/configure/configuration-settings.html#local-storage-directory>`_.

+-------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"FileLocation": "export"`` with string input. |
+-------------------------------------------------------------------------------------------+

Plugin Settings (Beta)
~~~~~~~~~~~~~~~~~~~~~~

Enable Plugin Uploads
^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables plugin uploads by System Admins at **Plugins > Management**. If you do not plan to upload a plugin, set to ``false`` to control which plugins are installed on your server. See `documentation <https://developers.mattermost.com/integrate/admin-guide/admin-plugins-beta/>`__ to learn more.

**False**: Disables plugin uploads on your Mattermost server.

+-----------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableUploads": false`` with options ``true`` and ``false``. |
+-----------------------------------------------------------------------------------------------------------+

Allow Insecure Download URL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables downloading and installing a plugin from a remote URL.

**False**: Disables downloading and installing a plugin from a remote URL.

+-----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"AllowInsecureDownloadUrl": false`` with options ``true`` and ``false``.                    |
+-----------------------------------------------------------------------------------------------------------------------------------------+

Enable Plugin Health Check
^^^^^^^^^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

**True**: Enables plugin health check to ensure all plugins are periodically monitored, and restarted or deactivated based on their health status. The health check runs every 30 seconds. If the plugin is detected to fail 3 times within an hour, the Mattermost server attempts to restart it. If the restart fails 3 successive times, it's automatically disabled.

**False**: Disables plugin health check on your Mattermost server.

+--------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"EnableHealthCheck": true`` with options ``true`` and ``false``. |
+--------------------------------------------------------------------------------------------------------------+

Directory
^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The location of the plugin files. If blank, they are stored in the ``./plugins`` directory. The path that you set must exist and Mattermost must have write permissions in it. 

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Directory": "./plugins"`` with string input.                       |
+-----------------------------------------------------------------------------------------------------------------+

Client Directory
^^^^^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

The location of client plugin files. If blank, they are stored in the ``./client/plugins`` directory. The path that you set must exist and Mattermost must have write permissions in it. 

+-----------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"Directory": "./client/plugins"`` with string input.                |
+-----------------------------------------------------------------------------------------------------------------+

Jobs
~~~~~

Settings to configure how Mattermost schedules and completes periodic tasks such as the deletion of old posts with Data Retention enabled or indexing posts with Elasticsearch. These settings control which Mattermost servers are designated as a Scheduler, a server that queues the tasks at the correct times, and as a Worker, a server that completes the given tasks.

When running Mattermost on a single machine, both ``RunJobs`` and ``RunScheduler`` should be enabled. Without both of these enabled, Mattermost will not function properly.

When running Mattermost in High Availability mode, ``RunJobs`` should be enabled on one or more servers while ``RunScheduler`` should be enabled on all servers under normal circumstances. A High Availability cluster will have one Scheduler and one or more Workers. See the below sections for more information.

Run Jobs
^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Set whether or not this Mattermost server will handle tasks created by the Scheduler. When running Mattermost on a single machine, this setting should always be enabled.

When running Mattermost in `High Availablity mode <https://docs.mattermost.com/scale/high-availability-cluster.html>`__, one or more servers should have this setting enabled. We recommend that your High Availability cluster has one or more dedicated Workers with this setting enabled while the remaining Mattermost app servers have it disabled.

+------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RunJobs": true`` with options ``true`` and ``false``.                                 |
+------------------------------------------------------------------------------------------------------------------------------------+

Run Scheduler
^^^^^^^^^^^^^^

|all-plans| |self-hosted|

.. |all-plans| image:: ../images/all-plans-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in Mattermost Free and Starter subscription plans.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

This setting isn't available in the System Console and can only be set in ``config.json``.

Set whether or not this Mattermost server will schedule tasks that will be completed by a Worker. When running Mattermost on a single machine, this setting should always be enabled.

When running Mattermost in `High Availablity mode <https://docs.mattermost.com/scale/high-availability-cluster.html>`__, this setting should always be enabled. In a High Availability cluster, exactly one of the servers will be designated as the Scheduler at a time to ensure that duplicate tasks aren't created. See `High Availability documentation <https://docs.mattermost.com/scale/high-availability-cluster.html>`__ for more details.

.. warning::

   We strongly recommend that you not change this setting from the default setting of ``true`` as this prevents the ``ClusterLeader`` from being able to run the scheduler. As a result, recurring jobs such as LDAP sync, Compliance Export, and data retention will no longer be scheduled. In previous Mattermost Server versions, and this documentation, the instructions stated to run the Job Server with ``RunScheduler: false``. The cluster design has evolved and this is no longer the case.

+-----------------------------------------------------------------------------------------------------------------------------------------+
| This feature's ``config.json`` setting is ``"RunScheduler": true`` with options ``true`` and ``false``.                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------+

Enable Shared Channels
^^^^^^^^^^^^^^^^^^^^^^

|enterprise| |self-hosted|

.. |enterprise| image:: ../images/enterprise-badge.png
  :scale: 30
  :target: https://mattermost.com/pricing
  :alt: Available in the Mattermost Enterprise subscription plan.

.. |self-hosted| image:: ../images/self-hosted-badge.png
  :scale: 30
  :target: https://mattermost.com/deploy
  :alt: Available for Mattermost Self-Hosted deployments.

*Available in legacy Enterprise Edition E20*

This setting isn't available in the System Console and can only be set in ``config.json``.


Shared Channels enables the ability to establish secure connections between Mattermost instances, and invite secured connections to shared channels where secure connections can participate as they would in any Public and Private channel. 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| This feature's two ``config.json`` settings include ``"ExperimentalSettings:EnableSharedChannels": false`` with options ``true`` or ``false``, and ``"ExperimentalSettings:EnableRemoteClusterService": false`` with options ``true`` or ``false``. |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   - Both configuration settings must be enabled in order to share channels with secure connections.
   - Enabling Shared Channels functionality requires a server restart.
   - System Admins for Cloud deployments can submit a request to have this configuration setting enabled in their Cloud instance.