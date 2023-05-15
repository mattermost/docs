:orphan:
:nosearch:

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

*Available in legacy Enterprise Edition E10/E20*

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

*Available in legacy Enterprise Edition E10/E20*

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

*Available in legacy Enterprise Edition E10/E20*

+---------------------------------------------------+---------------------------------------------------------------------------------------------+
| Enable or disable client-side debugging settings  | - System Config path: **Environment > Developer**                                           |
| found in *Settings > Advanced > Debugging* for    | - ``config.json setting``: ``".ServiceSettings.EnableClientPerformanceDebugging": false",`` |
| individual users.                                 | - Environment variable: ``MM_SERVICESETTINGS_ENABLECLIENTPERFORMANCEDEBUGGING``             |
|                                                   |                                                                                             |
| - **true**: Those settings are visible and can    |                                                                                             |
|   be enabled by users.                            |                                                                                             |
| - **false**: **(Default)** Those settings are     |                                                                                             |
|   hidden and disabled.                            |                                                                                             |
+---------------------------------------------------+---------------------------------------------------------------------------------------------+
| See the `client debugging <https://docs.mattermost.com/channels/channels-settings.html#client-debugging>`__ documentation to learn more.        |
+---------------------------------------------------+---------------------------------------------------------------------------------------------+

.. config:setting:: dev-allowuntrustedinternalconnections
  :displayname: Allow untrusted internal connections (Developer)
  :systemconsole: Environment > Developer
  :configjson: .ServiceSettings.AllowedUntrustedInternalConnections
  :environment: MM_SERVICESETTINGS_ALLOWUNTRUSTEDINTERNALCONNECTIONS
  :description: This setting is a whitelist of local network addresses that can be requested by the Mattermost server.

Allow untrusted internal connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E10/E20*

+-----------------------------------------------+-----------------------------------------------------------------------------------------------+
| Limit the ability for the Mattermost server   | - System Config path: **Environment > Developer**                                             |
| to make untrusted requests within its local   | - ``config.json setting``: ``".ServiceSettings.AllowedUntrustedInternalConnections": "",``    |
| network. A request is considered “untrusted”  | - Environment variable: ``MM_SERVICESETTINGS_ALLOWEDUNTRUSTEDINTERNALCONNECTIONS``            |
| when it’s made on behalf of a client.         |                                                                                               |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------+
| This setting is a whitelist of local network addresses that can be requested by the Mattermost server. It’s configured as a                   |
| whitespace-separated list of hostnames, IP addresses, and CIDR ranges that can be accessed.                                                   |
|                                                                                                                                               |
| Requests that can only be configured by System Admins are considered trusted and won't be affected by this setting. Trusted URLs include      |
| ones used for OAuth login or for sending push notifications.                                                                                  |
|                                                                                                                                               |
| The following features make untrusted requests and are affected by this setting:                                                              |
|                                                                                                                                               |
| - Integrations using webhooks, slash commands, or message actions. This prevents them from requesting endpoints within the local network.     |
| - Link previews. When a link to a local network address is posted in a chat message, this prevents a link preview from being displayed.       |
| - The local `image proxy </deploy/image-proxy.html>`__. If the local image proxy is enabled, images located on                                |
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
