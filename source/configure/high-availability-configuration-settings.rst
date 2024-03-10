:orphan:
:nosearch:

You can configure Mattermost as a :doc:`high availability environment </scale/high-availability-cluster>` by going to **System Console > Environment > High Availability**, or by editing the ``config.json`` file as described in the following tables. Changes to configuration settings in this section require a server restart before taking effect.

In a Mattermost high availability cluster deployment, the System Console is set to read-only, and settings can only be changed by editing the ``config.json`` file directly. However, to test a high availability environment, you can disable ``ClusterSettings.ReadOnlyConfig`` in the ``config.json`` file by setting it to ``false``. This allows changes applied using the System Console to be saved back to the configuration file.

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
  :description: The cluster to join by name in a high availability environment.

Cluster name
~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+-----------------------------------------------------------------+-----------------------------------------------------------------+
| The cluster to join by name in a high availability environment. | - System Config path: **Environment > High Availability**       |
|                                                                 | - ``config.json`` setting: ``".ClusterSettings.ClusterName",``  |
| Only nodes with the same cluster name will join together.       | - Environment variable: ``MM_CLUSTERSETTINGS_CLUSTERNAME``      |
| This is to support blue-green deployments or staging pointing   |                                                                 |
| to the same database.                                           |                                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------+

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

+-----------------------------------------------------------------+----------------------------------------------------------------------+
| You can override the hostname of this server.                   | - System Config path: **Environment > High Availability**            |
|                                                                 | - ``config.json`` setting: ``".ClusterSettings.OverrideHostname",``  |
| - This property can be set to a specific IP address if needed;  | - Environment variable: ``MM_CLUSTERSETTINGS_OVERRIDEHOSTNAME``      |
|   however, we don’t recommend overriding the hostname unless    |                                                                      |
|   it's necessary.                                               |                                                                      |
| - If left blank, Mattermost attempts to get the hostname from   |                                                                      |
|   the operating system or uses the IP address.                  |                                                                      |
+-----------------------------------------------------------------+----------------------------------------------------------------------+
| See the :doc:`high availability cluster </scale/high-availability-cluster>` documentation for details.                               |
+-----------------------------------------------------------------+----------------------------------------------------------------------+

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

+-----------------------------------------------------------------+------------------------------------------------------------------------+
| You can configure your high availability environment to         | - System Config path: **Environment > High Availability**              |
| communicate using the hostname instead of the IP address.       | - ``config.json`` setting: ``".ClusterSettings.UseIPAddress: true",``  |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_USEIPADDRESS``            |
| - **true**: **(Default)** The cluster attempts to communicate   |                                                                        |
|   using the IP address specified.                               |                                                                        |
| - **false**: The cluster attempts to communicate using the      |                                                                        |
|   hostname.                                                     |                                                                        |
+-----------------------------------------------------------------+------------------------------------------------------------------------+

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

.. config:setting:: ha-streamingport
  :displayname: Streaming port (High Availability)
  :systemconsole: Environment > High Availability
  :configjson: .ClusterSettings.StreamingPort
  :environment: MM_CLUSTERSETTINGS_STREAMINGPORT
  :description: The port used for streaming data between servers. Default value is **8075**.

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
  :description: An IP address used to identify the device that does automatic IP detection in high availability clusters.

Network interface
~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+-----------------------------------------------------------------+------------------------------------------------------------------------+
| An IP address used to identify the device that does automatic   | - System Config path: N/A                                              |
| IP detection in high availability clusters.                     | - ``config.json`` setting: ``".ClusterSettings.NetworkInterface: "",`` |
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

.. config:setting:: ha-maxidleconnections
  :displayname: Maximum idle connections for high availability (High Availability)
  :systemconsole: N/A
  :configjson: .ClusterSettings.MaxIdleConns
  :environment: MM_CLUSTERSETTINGS_MAXIDLECONNS
  :description: The maximum number of idle connections held open from one server to all others in the cluster. Default is **100** idle connections.

Maximum idle connections for high availability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+-----------------------------------------------------------------+------------------------------------------------------------------------+
| The maximum number of idle connections held open from one       | - System Config path: N/A                                              |
| server to all others in the cluster.                            | - ``config.json`` setting: ``".ClusterSettings.MaxIdleConns: 100,``    |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_MAXIDLECONNS``            |
| Numerical input. Default is **100**.                            |                                                                        |
+-----------------------------------------------------------------+------------------------------------------------------------------------+

.. config:setting:: ha-maxidleconnectionsperhost
  :displayname: Maximum idle connections per host (High Availability)
  :systemconsole: N/A
  :configjson: .ClusterSettings.MaxIdleConnsPerHost
  :environment: MM_CLUSTERSETTINGS_MAXIDLECONNSPERHOST
  :description: The maximum number of idle connections held open from one server to another server in the cluster. Default is **128** idle connections.

Maximum idle connections per host
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+-----------------------------------------------------------------+------------------------------------------------------------------------------+
| The maximum number of idle connections held open from one       | - System Config path: N/A                                                    |
| server to another server in the cluster.                        | - ``config.json`` setting: ``".ClusterSettings.MaxIdleConnsPerHost: 128",``  |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_MAXIDLECONNSPERHOST``           |
| Numerical input. Default is **128**.                            |                                                                              |
+-----------------------------------------------------------------+------------------------------------------------------------------------------+

.. config:setting:: ha-idleconnectiontimeout
  :displayname: Idle connection timeout (High Availability)
  :systemconsole: N/A
  :configjson: .ClusterSettings.IdleConnTimeoutMilliseconds
  :environment: MM_CLUSTERSETTINGS_IDLECONNTIMEOUTMILLISECONDS
  :description: The amount of time, in milliseconds, to leave an idle connection open between servers in the cluster. Default is **90000** milliseconds.

Idle connection timeout
~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

 <p class="mm-label-note">Also available in legacy Mattermost Enterprise Edition E20</p>

+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+
| The amount of time, in milliseconds, to leave an idle           | - System Config path: N/A                                                             |
| connection open between servers in the cluster.                 | - ``config.json`` setting: ``".ClusterSettings.IdleConnTimeoutMilliseconds: 90000",`` |
|                                                                 | - Environment variable: ``MM_CLUSTERSETTINGS_IDLECONNTIMEOUTMILLISECONDS``            |
| Numerical input. Default is **90000**.                          |                                                                                       |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------+
