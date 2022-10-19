.. _high-availability:
:orphan:
:nosearch:

You can configure Mattermost as a `high availability environment </scale/high-availability-cluster.html>`__ by going to **System Console > Environment > High Availability**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

In a Mattermost high availability cluster deployment, the System Console is set to read-only, and settings can only be changed by editing the ``config.json`` file directly. However, to test a high availability environment, you can disable ``ClusterSettings.ReadOnlyConfig`` in the ``config.json`` file by setting it to ``false``. This allows changes applied using the System Console to be saved back to the configuration file.

Enable high availability mode 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

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

Cluster name
~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------+-----------------------------------------------------------------+
| The cluster to join by name in a high availability environment. | - System Config path: **Environment > High Availability**       |
|                                                                 | - ``config.json`` setting: ``".ClusterSettings.ClusterName",``  |
| Only nodes with the same cluster name will join together.       | - Environment variable: ``MM_CLUSTERSETTINGS_CLUSTERNAME``      |
| This is to support blue-green deployments or staging pointing   |                                                                 |
| to the same database.                                           |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

Override hostname
~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------+----------------------------------------------------------------------+
| You can override the hostname of this server.                   | - System Config path: **Environment > High Availability**            |
|                                                                 | - ``config.json`` setting: ``".ClusterSettings.OverrideHostname",``  |
| - This property can be set to a specific IP address if needed;  | - Environment variable: ``MM_CLUSTERSETTINGS_OVERRIDEHOSTNAME``      |
|   however, we don’t recommend overriding the hostname unless    |                                                                      |
|   it's necessary.                                               |                                                                      |
| - If left blank, Mattermost attempts to get the hostname from   |                                                                      |
|   the operating system or uses the IP address.                  |                                                                      |
+-----------------------------------------------------------------+----------------------------------------------------------------------+
| See the `high availability cluster </scale/high-availability-cluster.html>`__ documentation for details.                               |
+-----------------------------------------------------------------+----------------------------------------------------------------------+

Use IP address
~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------+------------------------------------------------------------------------+
| You can configure your high availability environment to         | - System Config path: **Environment > High Availability**              |
| communicate using the hostname instead of the IP address.       | - ``config.json`` setting: ``".ClusterSettings.UseIPAddress: true",``  |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_USEIPADDRESS``            |
| - **true**: **(Default)** The cluster attempts to communicate   |                                                                        |
|   using the IP address specified.                               |                                                                        |
| - **false**: The cluster attempts to communicate using the      |                                                                        |
|   hostname.                                                     |                                                                        |
+-----------------------------------------------------------------+------------------------------------------------------------------------+

Use gossip
~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------+--------------------------------------------------------------------------------+
| All cluster traffic uses the gossip protocol.                   | - System Config path: **Environment > High Availability**                      |
|                                                                 | - ``config.json`` setting: ``".ClusterSettings.UseExperimentalGossip: true",`` |
| - **true**: **(Default)** The server attempts to communicate    | - Environment variable: ``MM_CLUSTERSETTINGS_USEEXPERIMENTALGOSSIP``           |
|   via the gossip protocol over the gossip port specified.       |                                                                                |
| - **false**: The server attempts to communicate over the        |                                                                                |
|   streaming port.                                               |                                                                                |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------+
| **Notes**:                                                                                                                                       |
|                                                                                                                                                  |
| - From Mattermost Server v5.36, gossip clustering can no longer be disabled.                                                                     |
| - The gossip port and gossip protocol are used to determine cluster health even when this setting is set to **false**.                           |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------+

Enable experimental gossip encryption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Gossip encryption uses AES-256 by default, and this value isn’t | - System Config path: **Environment > High Availability**                                    |
| configurable by design.                                         | - ``config.json`` setting: ``".ClusterSettings.EnableExperimentalGossipEncryption: false”,`` |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_ENABLEEXPERIMENTALGOSSIPENCRYPTION``            |
| - **true**: All communication through the cluster using the     |                                                                                              |
|   gossip protocol will be encrypted.                            |                                                                                              |
| - **false**: **(Default)** All communication using gossip       |                                                                                              |
|   protocol remains unencrypted.                                 |                                                                                              |
+-----------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| **Note**: Alternatively, you can manually set the ``ClusterEncryptionKey`` row value in the **Systems** table. A key is a byte array converted to base64.      |
| Set this value to either 16, 24, or 32 bytes to select AES-128, AES-192, or AES-256 respectively.                                                              |
+-----------------------------------------------------------------+----------------------------------------------------------------------------------------------+

Enable gossip compression
~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------+----------------------------------------------------------------------------------+
| Once all servers in a cluster are upgraded to Mattermost v5.33  | - System Config path: **Environment > High Availability**                        |
| or later, we recommend that you disable this configuration      | - ``config.json`` setting: ``".ClusterSettings.EnableGossipCompression: true”,`` |
| setting for better performance.                                 | - Environment variable: ``MM_CLUSTERSETTINGS_ENABLE GOSSIPCOMPRESSION``          |
|                                                                 |                                                                                  |
| - **true**: **(Default)** All communication through the         |                                                                                  |
|   cluster uses gossip compression. This setting is enabled by   |                                                                                  |
|   default to maintain compatibility with older servers.         |                                                                                  |
| - **false**: All communication using the gossip protocol        |                                                                                  |
|   remains uncompressed.                                         |                                                                                  |
+-----------------------------------------------------------------+----------------------------------------------------------------------------------+

Gossip port
~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------+---------------------------------------------------------------------+
| The port used for the gossip protocol. Both UDP and TCP         | - System Config path: **Environment > High Availability**           |
| should be allowed on this port.                                 | - ``config.json`` setting: ``".ClusterSettings.GossipPort: 8074”,`` |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_GOSSIPPORT``           |
| Numerical input. Default is **8074**.                           |                                                                     |
+-----------------------------------------------------------------+---------------------------------------------------------------------+

Streaming port
~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------+------------------------------------------------------------------------+
| The port used for streaming data between servers.               | - System Config path: **Environment > High Availability**              |
|                                                                 | - ``config.json`` setting: ``".ClusterSettings.StreamingPort: 8075",`` |
| Numerical input. Default is **8075**.                           | - Environment variable: ``MM_CLUSTERSETTINGS_STREAMINGPORT``           |
+-----------------------------------------------------------------+------------------------------------------------------------------------+

Read only config
~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------+------------------------------------------------------------------------+
| - **true**: **(Default)** Changes made to settings in the       | - System Config path: N/A                                              |
|   System Console are ignored.                                   | - ``config.json`` setting: ``".ClusterSettings.ReadOnlyConfig: true,`` |
| - **false**: Changes made to settings in the System Console     | - Environment variable: ``MM_CLUSTERSETTINGS_READONLYCONFIG``          |
|   are written to ``config.json``.                               |                                                                        | 
+-----------------------------------------------------------------+------------------------------------------------------------------------+

Network interface
~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------+------------------------------------------------------------------------+
| An IP address used to identify the device that does automatic   | - System Config path: N/A                                              |
| IP detection in high availability clusters.                     | - ``config.json`` setting: ``".ClusterSettings.NetworkInterface: "",`` |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_NETWORKINTERFACE``        |
| String input.                                                   |                                                                        |
+-----------------------------------------------------------------+------------------------------------------------------------------------+

Bind address
~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

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

Advertise address
~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------+------------------------------------------------------------------------+
| The IP address used to access the server from other nodes.      | - System Config path: N/A                                              |
| This settings is used primary when cluster nodes are not in     | - ``config.json`` setting: ``".ClusterSettings.AdvertiseAddress: "",`` |
| the same network and involve NAT (Network Address Translation). | - Environment variable: ``MM_CLUSTERSETTINGS_ADVERTISEADDRESS``        |
|                                                                 |                                                                        |
| String input.                                                   |                                                                        |
+-----------------------------------------------------------------+------------------------------------------------------------------------+

Maximum idle connections for high availability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------+------------------------------------------------------------------------+
| The maximum number of idle connections held open from one       | - System Config path: N/A                                              |
| server to all others in the cluster.                            | - ``config.json`` setting: ``".ClusterSettings.MaxIdleConns: 100,``    |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_MAXIDLECONNS``            |
| Numerical input. Default is **100**.                            |                                                                        |
+-----------------------------------------------------------------+------------------------------------------------------------------------+

Maximum idle connections per host
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------+------------------------------------------------------------------------------+
| The maximum number of idle connections held open from one       | - System Config path: N/A                                                    |
| server to another server in the cluster.                        | - ``config.json`` setting: ``".ClusterSettings.MaxIdleConnsPerHost: 128",``  |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_MAXIDLECONNSPERHOST``           |
| Numerical input. Default is **128**.                            |                                                                              |
+-----------------------------------------------------------------+------------------------------------------------------------------------------+

Idle connection timeout
~~~~~~~~~~~~~~~~~~~~~~~

*Available in legacy Enterprise Edition E20*

+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| The amount of time, in milliseconds, to leave an idle           | - System Config path: N/A                                                             |
| connection open between servers in the cluster.                 | - ``config.json`` setting: ``".ClusterSettings.IdleConnTimeoutMilliseconds: 90000",`` |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_IDLECONNTIMEOUTMILLISECONDS``            |
| Numerical input. Default is **90000**.                          |                                                                                       | 
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+
