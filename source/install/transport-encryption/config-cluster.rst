
Configuring Cluster Transport Encryption (E20)
==============================================

Mattermost is able to encrypt the messages sent within the cluster of a deployment using SSH tunneling. The guide walks through the deployment of this solution on Ubuntu 18.04, but it can be adapted for any Linux operating system.

While this document only describes the configuration of a three-node cluster, it is by no means limited to that number.

Prerequisites
-------------

- SSH port whitelisted between each node of the deployment.
- Active ufw/iptables on each node.
- Access to the root/sudo user of each node for configuration.
- A configured Mattermost cluster.
- Mattermost running with a dedicated service user.
- Mattermost service is stopped on each cluster node.

**Note:** Support on the application level is currently in development and will deprecate this document.

Example Environment
-------------------

In this scenario there are three application nodes in our environment with the following hostname/IP mapping:

- **transport-encryption-mattermost1:** 10.10.250.146
- **transport-encryption-mattermost2:** 10.10.250.231
- **transport-encryption-mattermost3:** 10.10.250.165

Preparations
------------

- Connect to each Mattermost server with a sudo or root user.
- Make a note of the IP from each cluster member used for the internal communication.
- Ensure ``AllowTcpForwarding`` is enabled in ``/etc/ssh/sshd_config`` of each cluster node.

SSH Authentication
------------------

On each node, generate a SSH key-pair for the service account. In our scenario this is called ``mattermost``:

.. code-block:: none

  $ sudo -u mattermost ssh-keygen -t rsa
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

**Note:** This service account can be separate from the service account already used for the Mattermost ``systemd`` service itself. It is important that it is allowed to create a SSH tunnel with port forwarding, but it does not require any additional
permissions.

ufw Configuration
-----------------

As a next step, allow SSH access from each of the other member nodes, e.g.:

- mattermost1 allows from mattermost2 and mattermost3
- mattermost2 allows from mattermost1 and mattermost3
- mattermost3 allows from mattermost1 and mattermost2

To do so, we add an exception in the firewall. The commands for ``mattermost1`` look as follows:

.. code-block:: none

  $ sudo ufw allow from 10.10.250.231/32 to any port ssh
  Rule added
  $ sudo ufw allow from 10.10.250.165/32 to any port ssh
  Rule added
  $ sudo ufw status
  Status: active

  To                         Action      From
  --                         ------      ----
  22/tcp                     ALLOW       10.10.250.10
  8065/tcp                   ALLOW       Anywhere
  22/tcp                     ALLOW       10.10.250.231
  22/tcp                     ALLOW       10.10.250.165


Repeat the same steps on the other nodes, replacing the IPs with the ones from the other member nodes. Do so for each member node, excluding the node itself.

Next, open ``/etc/ufw/after.rules`` and add the following block to the bottom of the file:

.. code-block:: none

  *nat
  :POSTROUTING ACCEPT [0:0]
  :PREROUTING ACCEPT [0:0]

  -A OUTPUT -p tcp -d 10.10.250.231 --dport 8075 -j DNAT --to-destination 127.0.0.1:18075
  -A OUTPUT -p tcp -d 10.10.250.231 --dport 8074 -j DNAT --to-destination 127.0.0.1:18074
  -A OUTPUT -p tcp -d 10.10.250.165 --dport 8075 -j DNAT --to-destination 127.0.0.1:28075
  -A OUTPUT -p tcp -d 10.10.250.165 --dport 8074 -j DNAT --to-destination 127.0.0.1:28074

  COMMIT


Two lines always belong to a single node, so in a deployment with four nodes:

.. code-block:: none

  -A OUTPUT -p tcp -d ip_node_2 --dport 8075 -j DNAT --to-destination 127.0.0.1:18075
  -A OUTPUT -p tcp -d ip_node_2 --dport 8074 -j DNAT --to-destination 127.0.0.1:18074
  -A OUTPUT -p tcp -d ip_node_3 --dport 8075 -j DNAT --to-destination 127.0.0.1:28075
  -A OUTPUT -p tcp -d ip_node_3 --dport 8074 -j DNAT --to-destination 127.0.0.1:28074
  -A OUTPUT -p tcp -d ip_node_4 --dport 8075 -j DNAT --to-destination 127.0.0.1:38075
  -A OUTPUT -p tcp -d ip_node_4 --dport 8074 -j DNAT --to-destination 127.0.0.1:38074

Please be aware that the ports on the right side must be unique, so if you have a cluster of six nodes, use 8075 and 8074 with 1 to 5 in front of it. If the cluster is of bigger size, additional ports must be used.

Ensure that your operating system has IP forwarding enabled using the following command:

.. code-block:: none

  $ sysctl -w net.ipv4.ip_forward=1

After that, reload the ufw rules and confirm that the iptable rules were successfully created:

.. code-block:: none

  $ iptables -t nat -L
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

SSH Configuration
-----------------

As a next step, we will ensure that the SSH tunnels are created as part of the Mattermost service start. To do so, create a file called ``pre_start.sh`` in ``/opt/mattermost/bin`` on ``mattermost1``:

.. code-block:: none

  #!/bin/bash
  ssh -N -f -o ServerAliveInterval=60 -o ExitOnForwardFailure=yes -L 18075:10.10.250.231:8075 10.10.250.231 || true
  ssh -N -f -o ServerAliveInterval=60 -o ExitOnForwardFailure=yes -L 18074:10.10.250.231:8074 10.10.250.231 || true
  ssh -N -f -o ServerAliveInterval=60 -o ExitOnForwardFailure=yes -L 28075:10.10.250.165:8075 10.10.250.165 || true
  ssh -N -f -o ServerAliveInterval=60 -o ExitOnForwardFailure=yes -L 28074:10.10.250.165:8074 10.10.250.165 || true

**Note:** We're ignoring the error from the SSH connection itself in case a tunnel is already active. Otherwise the Mattermost server would fail to start.

**Note:** Please make sure to back up this script in case of a version upgrade.

Afterwards, we set the executable bit on the shell script:

.. code-block:: none

  $ chmod +x /opt/mattermost/bin/pre_start.sh

Open the systemd unit file of Mattermost and search for ``Type=Notify``. After this, enter a ``ExecStartPre`` script that will be executed before Mattermost itself is started:

.. code-block:: none

  [Service]
  Type=notify
  ExecStartPre=/opt/mattermost/bin/pre_start.sh

Reload the systemd daemon afterwards:

.. code-block:: none

  $ systemctl daemon-reload

Repeat the same steps on each of the member nodes and adapt the node IPs and amount of entries for your environment.

Cluster Start
-------------

Once each node is configured, restart the service on each cluster and confirm that it's running using the command below:

.. code-block:: none

  root@transport-encryption-mattermost1:/opt/mattermost/bin# systemctl start mattermost
  root@transport-encryption-mattermost1:/opt/mattermost/bin# systemctl status mattermost.service
  ● mattermost.service - Mattermost
     Loaded: loaded (/lib/systemd/system/mattermost.service; static; vendor preset: enabled)
     Active: active (running) since Fri 2019-10-04 19:44:20 UTC; 5min ago
    Process: 16734 ExecStartPre=/opt/mattermost/bin/pre_start.sh (code=exited, status=0/SUCCESS)

Next, open the Mattermost System Console and confirm that each node is reporting successfully in the High Availability section.
