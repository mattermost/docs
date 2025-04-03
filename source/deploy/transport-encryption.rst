Configuring transport encryption
=================================

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

The components of the Mattermost setup are shown in the following diagram, including the transport encryption used. Aside from the encryption between the nodes of the Mattermost cluster, all transports rely on TLS encryption.

.. note::

  The transport between the Application servers is not used by default and requires additional setup steps. Enhancing the core product to include automatic encryption between cluster nodes is in progress and planned for a later release.

.. image:: ../images/transport-encryption.png
   :alt: Components of the Mattermost setup where all transports rely on TLS encryption.

Configuring proxy to Mattermost transport encryption
-----------------------------------------------------

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

Mattermost is able to encrypt the traffic between the proxy and the application server using TLS.

Prerequisites
~~~~~~~~~~~~~~

- Operational Mattermost server or cluster.
- Authentication credentials for Mattermost user on application server.

Example environment
~~~~~~~~~~~~~~~~~~~

In this scenario there is one Mattermost application server and one NGINX server, both running Ubuntu 20.04, with the following IPs:

- **transport-encryption-mattermost1:** 10.10.250.146
- **transport-encryption-nginx:** 10.10.250.107

Configuring NGINX
~~~~~~~~~~~~~~~~~~

On the NGINX server, connect to both servers with a sudo or root user. Open the Mattermost proxy configuration and search for the following line twice:

.. code-block:: text

  proxy_pass http://backend;

Change the protocol from ``http`` to ``https``:

.. code-block:: text

  proxy_pass https://backend;

Afterwards do not reload the NGINX server yet to minimize the downtime of the service.

Configuring Mattermost
~~~~~~~~~~~~~~~~~~~~~~~

On the Mattermost server, change to the config directory of Mattermost and generate a self-signed certificate that will be used to encrypt the traffic between the proxy server and the application server.

**Note:** Alternatively you can sign a certificate from your company's CA.

.. code-block:: sh

  cd /opt/mattermost/config
  openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
  chown root:mattermost *.pem
  chmod 640 *.pem


Once complete, open the file ``config.json`` and modify the values ``ConnectionSecurity``, ``TLSCertFile`` and ``TLSKeyFile`` in the ``ServiceSettings`` section.

**Before**

.. code-block:: json

  {
      "ServiceSettings": {
          "SiteURL": "https://transport-encryption.dev.example.com",
          "WebsocketURL": "",
          "LicenseFileLocation": "",
          "ListenAddress": ":8065",
          "ConnectionSecurity": "",
          "TLSCertFile": "",
          "TLSKeyFile": "",
          "...":"..."
      },
      "...":"..."
  }


**After**

.. code-block:: json

  {
      "ServiceSettings": {
          "SiteURL": "https://transport-encryption.dev.example.com",
          "WebsocketURL": "",
          "LicenseFileLocation": "",
          "ListenAddress": ":8065",
          "ConnectionSecurity": "TLS",
          "TLSCertFile": "/opt/mattermost/config/cert.pem",
          "TLSKeyFile": "/opt/mattermost/config/key.pem",
          "...":"..."
      },
      "...":"..."
  }


Restart the Mattermost server and ensure it's up and running:

.. code-block:: sh

  sudo systemctl restart mattermost
  systemctl status mattermost

.. code-block:: text

  ● mattermost.service - Mattermost
     Loaded: loaded (/lib/systemd/system/mattermost.service; static; vendor preset: enabled)
     Active: active (running) since Mon 2019-10-28 16:45:29 UTC; 1h 15min ago
     [...]

Finally, on the **NGINX server**, reload the configuration to ensure that requests are sent on HTTPS:

.. code-block:: sh

  sudo systemctl reload nginx

Configuring database transport encryption
------------------------------------------

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

Mattermost is able to encrypt the traffic between the database and the application using TLS. This guide describes the setup steps for a single, separate MySQL server.

Prerequisites
~~~~~~~~~~~~~~

- Operational Mattermost server or cluster.
- Operational MySQL server.
- Confirmed connectivity between Mattermost and MySQL server.
- Authentication credentials for Mattermost user on MySQL server.

Example environment
~~~~~~~~~~~~~~~~~~~

In this scenario there is one Mattermost application server and one MySQL server, both running Ubuntu 20.04, with the following IPs:

- **transport-encryption-mattermost1:** 10.10.250.146
- **transport-encryption-mysql1:** 10.10.250.148

Configuring MySQL
~~~~~~~~~~~~~~~~~~

As a first step, connect to both servers with a sudo or root user.

Execute the following command to prepare the server for SSL connections:

.. code-block:: sh

  sudo mysql_ssl_rsa_setup --uid=mysql

This generates self-signed certificates in ``/var/lib/mysql/`` that the MySQL server uses to encrypt the connection. If you would like to use certificates from your company CA, please follow the MySQL documentation for configuration steps.

**Note:** Optionally, it can be enforced that all connections must be made via a local socket connection or TLS. To do this, open ``/etc/mysql/mysql.conf.d/mysqld.cnf`` and append the following line to the file:

.. code-block:: text

  require_secure_transport = ON

Any connection to the MySQL server must now be made with secure transport enabled.

Last but not least, restart the server and confirm it is up and running:

  .. code-block:: sh

  systemctl restart mysql
  systemctl status mysql

.. code-block:: text

  ● mysql.service - MySQL Community Server
     Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
     Active: active (running) since Fri 2019-10-18 16:41:25 UTC; 2s ago
    Process: 8380 ExecStart=/usr/sbin/mysqld --daemonize --pid-file=/run/mysqld/mysqld.pid (code=exited, status=0/SUCCESS)
    Process: 8360 ExecStartPre=/usr/share/mysql/mysql-systemd-start pre (code=exited, status=0/SUCCESS)
   Main PID: 8382 (mysqld)
      Tasks: 27 (limit: 2361)
     CGroup: /system.slice/mysql.service
             └─8382 /usr/sbin/mysqld --daemonize --pid-file=/run/mysqld/mysqld.pid

  Oct 18 16:41:25 transport-encryption-mysql1 systemd[1]: Stopped MySQL Community Server.
  Oct 18 16:41:25 transport-encryption-mysql1 systemd[1]: Starting MySQL Community Server...
  Oct 18 16:41:25 transport-encryption-mysql1 systemd[1]: Started MySQL Community Server.

Configuring Mattermost
~~~~~~~~~~~~~~~~~~~~~~~

On the Mattermost server, open the file ``config.json`` and look for the ``DataSource`` value in the ``SqlSettings`` section. It should look similar to this:

.. code-block:: text

  "DataSource": "mmuser:sad09zusaopdhsad123@tcp(10.10.250.148:3306)/mattermost?charset=utf8mb4,utf8\u0026writeTimeout=30s",

At the end of the line, we can configure that TLS must be turned on with the ``tls`` flag which supports the following values:

- true (Require TLS + a trusted certificate)
- false
- skip-verify (Require TLS + accept self-signed)
- preferred (Try TLS, fallback to unencrypted)

In our case we need to use ``skip-verify`` since we use a self-signed certificate. The configuration setting will now look like this:

.. code-block:: text

  "DataSource": "mmuser:sad09zusaopdhsad123@tcp(10.10.250.148:3306)/mattermost?charset=utf8mb4,utf8\u0026writeTimeout=30s&tls=skip-verify",

If you're running Mattermost in a cluster, be sure to update the value on each node of the cluster. If you are using configuration in the database, be sure to update the ``systemd`` unit file and enable TLS for the configuration store.

Once complete, restart the Mattermost server and ensure the system is operational:

.. code-block:: sh

  sudo systemctl restart mattermost
  systemctl status mattermost

.. code-block:: text

  ● mattermost.service - Mattermost
     Loaded: loaded (/lib/systemd/system/mattermost.service; static; vendor preset: enabled)
     Active: active (running) since Fri 2019-10-18 16:47:08 UTC; 3s ago
    Process: 3424 ExecStartPre=/opt/mattermost/bin/pre_start.sh (code=exited, status=0/SUCCESS)
   Main PID: 3443 (mattermost)
      Tasks: 20 (limit: 2361)
     CGroup: /system.slice/mattermost.service
             ├─3443 /opt/mattermost/bin/mattermost --config=mysql://mmuser:sad09zusaopdhsad123@tcp(10.10.250.148:3306)/mattermost?charset=utf8mb4,utf8&writeTimeout=30s&tls=skip-verify
             └─3459 plugins/com.mattermost.nps/server/dist/plugin-linux-amd64

  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"debug","ts":1571417228.8637397,"caller":"scheduler/worker.go:36","msg":"Worker started","worker":"Plugins"}
  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"debug","ts":1571417228.8639545,"caller":"jobs/jobs_watcher.go:38","msg":"Watcher Started"}
  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"info","ts":1571417228.8641603,"caller":"jobs/schedulers.go:72","msg":"Starting schedulers."}
  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"debug","ts":1571417228.8645394,"caller":"app/web_hub.go:436","msg":"Hub for index 0 is starting with goroutine 3923"}
  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"debug","ts":1571417228.8648505,"caller":"app/web_hub.go:436","msg":"Hub for index 1 is starting with goroutine 3924"}
  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"debug","ts":1571417228.8656101,"caller":"web/static.go:31","msg":"Using client directory at /opt/mattermost/client"}
  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"info","ts":1571417228.8681324,"caller":"commands/server.go:105","msg":"Sending systemd READY notification."}
  Oct 18 16:47:08 transport-encryption-mattermost1 systemd[1]: Started Mattermost.
  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"debug","ts":1571417228.9003174,"caller":"jobs/schedulers.go:166","msg":"Next run time for scheduler","scheduler_name":"MigrationsSched
  Oct 18 16:47:08 transport-encryption-mattermost1 mattermost[3443]: {"level":"debug","ts":1571417228.9025588,"caller":"jobs/schedulers.go:166","msg":"Next run time for scheduler","scheduler_name":"PluginsSchedule

Configuring cluster transport encryption
-----------------------------------------

.. include:: ../_static/badges/ent-selfhosted.rst
  :start-after: :nosearch:

Mattermost is able to encrypt the messages sent within the cluster of a deployment using SSH tunneling. The guide walks through the deployment of this solution on Ubuntu 20.04, but it can be adapted for any Linux operating system.

While this document only describes the configuration of a three-node cluster, it is by no means limited to that number.

Prerequisites
~~~~~~~~~~~~~

- SSH port whitelisted between each node of the deployment.
- Active ufw/iptables on each node.
- Access to the root/sudo user of each node for configuration.
- A configured Mattermost cluster.
- Mattermost running with a dedicated service user.
- Mattermost service is stopped on each cluster node.

.. note:: 
  Support on the application level is currently in development and, when available, will deprecate this document.

Example environment
~~~~~~~~~~~~~~~~~~~

In this scenario there are three application nodes in our environment with the following hostname/IP mapping:

- **transport-encryption-mattermost1:** 10.10.250.146
- **transport-encryption-mattermost2:** 10.10.250.231
- **transport-encryption-mattermost3:** 10.10.250.165

Preparations
~~~~~~~~~~~~~

- Connect to each Mattermost server with a sudo or root user.
- Make a note of the IP from each cluster member used for the internal communication.
- Ensure ``AllowTcpForwarding`` is enabled in ``/etc/ssh/sshd_config`` of each cluster node.

SSH authentication
~~~~~~~~~~~~~~~~~~~

On each node, generate a SSH key-pair for the service account. In our scenario this is called ``mattermost``:

.. code-block:: sh

  sudo -u mattermost ssh-keygen -t rsa

.. code-block:: text

  Generating public/private rsa key pair.
  Enter file in which to save the key (/home/mattermost/.ssh/id_rsa):
  Enter passphrase (empty for no passphrase):
  Enter same passphrase again:
  Your identification has been saved in /home/mattermost/.ssh/id_rsa.
  Your public key has been saved in /home/mattermost/.ssh/id_rsa.pub.
  The key fingerprint is:
  SHA256:redacted mattermost@transport-encryption-mattermost1


The location of the SSH key itself is irrelevant if company policies require the usage of another storage location.

Next, ensure that the SSH public key of each node is added to the ``authorized_keys`` file of the other nodes of the cluster. To do so, copy the contents of ``/home/mattermost/.ssh/id_rsa.pub`` of nodes 2 and 3, and add it to ``/home/mattermost/.ssh/authorized_keys`` of node 1.

Repeat this step for each node of the cluster. As a result, each node should be able to establish an SSH connection to the other nodes of the cluster.

.. note:: 

  This service account can be separate from the service account already used for the Mattermost ``systemd`` service itself. It's important that this service account is allowed to create a SSH tunnel with port forwarding, but it doesn't require any additional permissions.

ufw configuration
~~~~~~~~~~~~~~~~~

As a next step, allow SSH access from each of the other member nodes, e.g.:

- mattermost1 allows from mattermost2 and mattermost3
- mattermost2 allows from mattermost1 and mattermost3
- mattermost3 allows from mattermost1 and mattermost2

To do so, we add an exception in the firewall. The commands for ``mattermost1`` look as follows:

.. code-block:: sh

  sudo ufw allow from 10.10.250.231/32 to any port ssh
  sudo ufw allow from 10.10.250.165/32 to any port ssh
  sudo ufw status

.. code-block:: text

  Rule added
  Rule added
  Status: active

  To                         Action      From
  --                         ------      ----
  22/tcp                     ALLOW       10.10.250.10
  8065/tcp                   ALLOW       Anywhere
  22/tcp                     ALLOW       10.10.250.231
  22/tcp                     ALLOW       10.10.250.165


Repeat the same steps on the other nodes, replacing the IPs with the ones from the other member nodes. Do so for each member node, excluding the node itself.

Next, open ``/etc/ufw/after.rules`` and add the following block to the bottom of the file:

.. code-block:: text

  *nat
  :POSTROUTING ACCEPT [0:0]
  :PREROUTING ACCEPT [0:0]

  -A OUTPUT -p tcp -d 10.10.250.231 --dport 8075 -j DNAT --to-destination 127.0.0.1:18075
  -A OUTPUT -p tcp -d 10.10.250.231 --dport 8074 -j DNAT --to-destination 127.0.0.1:18074
  -A OUTPUT -p tcp -d 10.10.250.165 --dport 8075 -j DNAT --to-destination 127.0.0.1:28075
  -A OUTPUT -p tcp -d 10.10.250.165 --dport 8074 -j DNAT --to-destination 127.0.0.1:28074

  COMMIT


Two lines always belong to a single node, so in a deployment with four nodes:

.. code-block:: text

  -A OUTPUT -p tcp -d ip_node_2 --dport 8075 -j DNAT --to-destination 127.0.0.1:18075
  -A OUTPUT -p tcp -d ip_node_2 --dport 8074 -j DNAT --to-destination 127.0.0.1:18074
  -A OUTPUT -p tcp -d ip_node_3 --dport 8075 -j DNAT --to-destination 127.0.0.1:28075
  -A OUTPUT -p tcp -d ip_node_3 --dport 8074 -j DNAT --to-destination 127.0.0.1:28074
  -A OUTPUT -p tcp -d ip_node_4 --dport 8075 -j DNAT --to-destination 127.0.0.1:38075
  -A OUTPUT -p tcp -d ip_node_4 --dport 8074 -j DNAT --to-destination 127.0.0.1:38074

Please be aware that the ports on the right side must be unique, so if you have a cluster of six nodes, use 8075 and 8074 with 1 to 5 in front of it. If the cluster is of bigger size, additional ports must be used.

Ensure that your operating system has IP forwarding enabled using the following command:

.. code-block:: sh

  sysctl -w net.ipv4.ip_forward=1

After that, reload the ufw rules and confirm that the iptable rules were successfully created:

.. code-block:: sh

  iptables -t nat -L

.. code-block:: text

  Chain PREROUTING (policy ACCEPT)
  target     prot opt source               destination

  Chain INPUT (policy ACCEPT)
  target     prot opt source               destination

  Chain OUTPUT (policy ACCEPT)
  target     prot opt source               destination
  DNAT       tcp  --  anywhere             10.10.250.231        tcp dpt:8075 to:127.0.0.1:18075
  DNAT       tcp  --  anywhere             10.10.250.231        tcp dpt:8074 to:127.0.0.1:18074
  DNAT       tcp  --  anywhere             10.10.250.165        tcp dpt:8075 to:127.0.0.1:28075
  DNAT       tcp  --  anywhere             10.10.250.165        tcp dpt:8074 to:127.0.0.1:28074

Repeat those steps for every node on the cluster. At the end of this section the following should be configured:

- SSH access enabled in firewall from each cluster node to another.
- Per node 2 iptables rules for port 8074 and 8075.
- IP forwarding enabled.

SSH configuration
~~~~~~~~~~~~~~~~~

As a next step, ensure that the SSH tunnels are created as part of the Mattermost service start. To do so, create a file called ``pre_start.sh`` in ``/opt/mattermost/bin`` on ``mattermost1``:

.. code-block:: sh

  #!/bin/bash
  ssh -N -f -o ServerAliveInterval=60 -o ExitOnForwardFailure=yes -L 18075:10.10.250.231:8075 10.10.250.231 || true
  ssh -N -f -o ServerAliveInterval=60 -o ExitOnForwardFailure=yes -L 18074:10.10.250.231:8074 10.10.250.231 || true
  ssh -N -f -o ServerAliveInterval=60 -o ExitOnForwardFailure=yes -L 28075:10.10.250.165:8075 10.10.250.165 || true
  ssh -N -f -o ServerAliveInterval=60 -o ExitOnForwardFailure=yes -L 28074:10.10.250.165:8074 10.10.250.165 || true

.. note:: 
  
  - We're ignoring the error from the SSH connection itself in case a tunnel is already active. Otherwise the Mattermost server would fail to start.
  - Please make sure to back up this script in case of a version upgrade.

Afterwards, set the executable bit on the shell script:

.. code-block:: sh

  chmod +x /opt/mattermost/bin/pre_start.sh

Open the systemd unit file of Mattermost and search for ``Type=Notify``. After this, enter a ``ExecStartPre`` script that will be executed before Mattermost itself is started:

.. code-block:: text

  [Service]
  Type=notify
  ExecStartPre=/opt/mattermost/bin/pre_start.sh

Reload the systemd daemon afterwards:

.. code-block:: sh

  systemctl daemon-reload

Repeat the same steps on each of the member nodes and adapt the node IPs and amount of entries for your environment.

Cluster start
~~~~~~~~~~~~~~

Once each node is configured, restart the service on each cluster and confirm that it's running using the command below:

.. code-block:: sh

  systemctl start mattermost
  systemctl status mattermost.service

.. code-block:: text

  ● mattermost.service - Mattermost
     Loaded: loaded (/lib/systemd/system/mattermost.service; static; vendor preset: enabled)
     Active: active (running) since Fri 2019-10-04 19:44:20 UTC; 5min ago
    Process: 16734 ExecStartPre=/opt/mattermost/bin/pre_start.sh (code=exited, status=0/SUCCESS)

Next, open the Mattermost System Console and confirm that each node is reporting successfully in the High Availability section.
