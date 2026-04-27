PostgreSQL high availability cluster
=====================================

:nosearch:

This guide describes how to deploy a high availability PostgreSQL cluster for
Mattermost using `repmgr <https://repmgr.org/>`__ for replication management
and automatic failover, `HAProxy <https://www.haproxy.org/>`__ for connection
routing, and `Keepalived <https://keepalived.org/>`__ for Virtual IP (VIP)
management.

This is infrastructure-level HA that operates independently of your Mattermost
edition. It is compatible with any self-hosted Mattermost deployment.

.. note::

   This guide has been validated on: **Ubuntu 24.04 LTS**, **PostgreSQL 17**,
   **repmgr 5.5**, **HAProxy 2.8**, **Keepalived**.

Architecture overview
---------------------

A PostgreSQL HA cluster for Mattermost consists of three nodes running in
parallel. Each node runs the full stack: PostgreSQL, repmgr daemon (repmgrd),
HAProxy, Keepalived, and a health-check service. A Virtual IP (VIP) floats
across nodes and always points to the current primary.

.. code-block:: text

                         VIP: <CLUSTER_VIP>
                                │
                ┌───────────────┼───────────────┐
                │               │               │
         ┌──────┴──────┐ ┌──────┴──────┐ ┌──────┴──────┐
         │     pg1     │ │     pg2     │ │     pg3     │
         │             │ │             │ │             │
         │  HAProxy    │ │  HAProxy    │ │  HAProxy    │
         │  Keepalived │ │  Keepalived │ │  Keepalived │
         │  pgchk.py   │ │  pgchk.py   │ │  pgchk.py   │
         │  repmgrd    │ │  repmgrd    │ │  repmgrd    │
         ├─────────────┤ ├─────────────┤ ├─────────────┤
         │ PostgreSQL  │ │ PostgreSQL  │ │ PostgreSQL  │
         │   PRIMARY   │ │   STANDBY   │ │   STANDBY   │
         └─────────────┘ └─────────────┘ └─────────────┘

**Components:**

.. list-table::
   :widths: 20 10 70
   :header-rows: 1

   * - Component
     - Version
     - Role
   * - PostgreSQL
     - 17
     - Primary database engine. Streaming replication with replication slots.
   * - repmgr / repmgrd
     - 5.5
     - Replication manager. Monitors cluster health and automatically promotes
       a standby when the primary fails.
   * - HAProxy
     - 2.8
     - TCP load balancer. Routes write traffic to the primary and read traffic
       to standbys via two ports.
   * - Keepalived
     - —
     - Manages the VIP using VRRP. Moves the VIP to the new primary after
       failover.
   * - pgchk.py
     - —
     - HTTP health-check endpoint (port 8008). HAProxy queries this to
       determine which node is the current primary.

**HAProxy ports:**

.. list-table::
   :widths: 15 85
   :header-rows: 1

   * - Port
     - Purpose
   * - 5000
     - Write traffic — routes to the current primary only
   * - 5001
     - Read traffic — load-balanced across all standbys

**Sizing:** This architecture is appropriate for Mattermost deployments up to
approximately 2,000 concurrent users. For larger deployments, see
:doc:`Scaling for Enterprise </administration-guide/scale/scaling-for-enterprise>`.

Before you begin
----------------

Is this the right architecture for you?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 30 35 35
   :header-rows: 1

   * - Scenario
     - Recommendation
     - Why
   * - Cloud-hosted on AWS/GCP/Azure
     - Use managed RDS/Cloud SQL with Multi-AZ
     - Managed failover, no infrastructure to operate
   * - On-premises or private cloud, single site
     - **This guide** — single-DC HA cluster
     - Automatic failover within the datacenter, no cloud dependency
   * - On-premises, two or more sites, DR required
     - Single-DC HA (this guide) + Multi-DC DR guide (coming soon)
     - Active/warm-standby across datacenters

Requirements
~~~~~~~~~~~~

**Hardware (per node — minimum):**

- Operating system: Ubuntu 24.04 LTS
- CPU: 2 cores
- RAM: 4 GB
- Disk: 50 GB

**You need 3 nodes** and one spare IP address on the same subnet for the VIP.

**Network — ports that must be open between all three nodes:**

.. list-table::
   :widths: 15 85
   :header-rows: 1

   * - Port
     - Purpose
   * - 22
     - SSH (administration)
   * - 5432
     - PostgreSQL (replication, repmgr)
   * - 8008
     - pgchk.py health check (HAProxy → database nodes)
   * - VRRP (112)
     - Keepalived VIP election between nodes

**Ports that Mattermost application servers must reach:**

.. list-table::
   :widths: 15 85
   :header-rows: 1

   * - Port
     - Purpose
   * - 5000
     - Write connections (primary)
   * - 5001
     - Read connections (standbys)

**Software:** The following packages will be installed during setup. No
pre-installation is required.

- ``postgresql-17``
- ``postgresql-17-repmgr``
- ``haproxy``
- ``keepalived``
- ``python3`` (for pgchk.py)

Node planning worksheet
~~~~~~~~~~~~~~~~~~~~~~~

Complete this before starting. You will substitute these values throughout
the guide.

.. list-table::
   :widths: 15 25 25 35
   :header-rows: 1

   * - Node
     - Hostname
     - IP address
     - Initial role
   * - 1
     - pg1
     - _______________
     - Primary
   * - 2
     - pg2
     - _______________
     - Standby
   * - 3
     - pg3
     - _______________
     - Standby
   * - VIP
     - —
     - _______________
     - Floating (always points to primary)

**Subnet:** ``_______________`` (e.g. ``10.0.1.0``)

Time estimate
~~~~~~~~~~~~~

Allow **2–3 hours** for a first-time setup on pre-provisioned servers.

Setup guide
-----------

.. note::

   Throughout this guide, substitute the IP addresses and subnet you recorded
   in the node planning worksheet above.

.. warning::

   Complete each phase in order. The checkpoint at the end of each phase must
   pass before you proceed.

Phase 1: Base installation (all nodes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run all steps in Phase 1 on **pg1, pg2, and pg3**.

**Step 1.1 — Configure /etc/hosts**

On each node, append to ``/etc/hosts``:

.. code-block:: text

   <PG1_IP>  pg1
   <PG2_IP>  pg2
   <PG3_IP>  pg3

Verify hostname resolution on each node:

.. code-block:: bash

   ping -c 1 pg1 && ping -c 1 pg2 && ping -c 1 pg3

Expected: 3 successful pings.

**Step 1.2 — Install PostgreSQL 17 and repmgr 5.5**

.. code-block:: bash

   sudo apt update
   sudo apt install -y curl ca-certificates
   sudo install -d /usr/share/postgresql-common/pgdg
   sudo curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc \
       --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc
   sudo sh -c 'echo "deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] \
       https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" \
       > /etc/apt/sources.list.d/pgdg.list'
   sudo apt update
   sudo apt install -y postgresql-17 postgresql-17-repmgr

✅ **Phase 1 checkpoint** — run on every node:

.. code-block:: bash

   sudo systemctl status postgresql | grep "active (running)"
   /usr/lib/postgresql/17/bin/repmgr --version

**Pass:** PostgreSQL shows ``active (running)``; repmgr prints ``repmgr 5.5.x``.

**Fail:** If PostgreSQL did not start, check ``journalctl -u postgresql`` for errors.

Phase 2: PostgreSQL configuration (all nodes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run all steps in Phase 2 on **pg1, pg2, and pg3**.

**Step 2.1 — Configure postgresql.conf**

Append to ``/etc/postgresql/17/main/postgresql.conf``:

.. code-block:: ini

   # Replication settings
   listen_addresses = '*'
   max_wal_senders = 10
   max_replication_slots = 10
   wal_level = replica
   hot_standby = on
   archive_mode = on
   archive_command = '/bin/true'
   shared_preload_libraries = 'repmgr'
   wal_log_hints = on
   wal_keep_size = 1024

**Step 2.2 — Configure pg_hba.conf**

Append to ``/etc/postgresql/17/main/pg_hba.conf``:

.. code-block:: text

   # repmgr access
   host    repmgr      repmgr      <SUBNET>/24     trust
   host    repmgr      repmgr      127.0.0.1/32    trust
   # Replication connections
   host    replication repmgr      <SUBNET>/24     trust
   host    replication repmgr      127.0.0.1/32    trust

.. note::

   For production, replace ``trust`` with ``scram-sha-256`` and configure
   ``.pgpass`` files on each node.

**Step 2.3 — Restart PostgreSQL**

.. code-block:: bash

   sudo systemctl restart postgresql

✅ **Phase 2 checkpoint** — run on every node:

.. code-block:: bash

   sudo -u postgres psql -c "SHOW wal_level;"
   sudo -u postgres psql -c "SHOW shared_preload_libraries;"

**Pass:** ``wal_level`` is ``replica``; ``shared_preload_libraries`` contains ``repmgr``.

**Fail:** If PostgreSQL did not restart, check ``journalctl -u postgresql``.

Phase 3: repmgr configuration and cluster initialisation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Step 3.1 — Create repmgr user and database (pg1 only)**

.. code-block:: bash

   sudo -u postgres createuser --superuser repmgr
   sudo -u postgres createdb --owner=repmgr repmgr
   sudo -u postgres psql -c "ALTER USER repmgr SET search_path TO repmgr, public;"

**Step 3.2 — Create /etc/repmgr.conf (all nodes)**

Create ``/etc/repmgr.conf`` on each node. Adjust ``node_id``, ``node_name``,
and ``host`` for each node:

**pg1:**

.. code-block:: ini

   node_id=1
   node_name='pg1'
   conninfo='host=<PG1_IP> user=repmgr dbname=repmgr connect_timeout=2'
   data_directory='/var/lib/postgresql/17/main'
   use_replication_slots=yes
   monitoring_history=yes
   log_level=INFO
   pg_bindir='/usr/lib/postgresql/17/bin'
   service_start_command='sudo /usr/bin/pg_ctlcluster 17 main start'
   service_stop_command='sudo /usr/bin/pg_ctlcluster 17 main stop'
   service_restart_command='sudo /usr/bin/pg_ctlcluster 17 main restart'
   service_reload_command='sudo /usr/bin/pg_ctlcluster 17 main reload'
   service_promote_command='sudo /usr/bin/pg_ctlcluster 17 main promote'
   failover=automatic
   promote_command='repmgr standby promote -f /etc/repmgr.conf --log-to-file'
   follow_command='repmgr standby follow -f /etc/repmgr.conf --log-to-file --upstream-node-id=%n'
   reconnect_attempts=3
   reconnect_interval=5
   monitor_interval_secs=2

**pg2:** Same as above with ``node_id=2``, ``node_name='pg2'``, ``host=<PG2_IP>``.

**pg3:** Same as above with ``node_id=3``, ``node_name='pg3'``, ``host=<PG3_IP>``.

**Step 3.3 — Register primary (pg1 only)**

.. code-block:: bash

   sudo -u postgres repmgr -f /etc/repmgr.conf primary register

**Step 3.4 — Clone standbys (pg2 and pg3)**

Run on **pg2**, then **pg3**:

.. code-block:: bash

   sudo systemctl stop postgresql
   sudo -u postgres repmgr -h <PG1_IP> -U repmgr -d repmgr \
       -f /etc/repmgr.conf standby clone --delete-existing-pgdata
   sudo systemctl start postgresql
   sudo -u postgres repmgr -f /etc/repmgr.conf standby register

**Step 3.5 — Start repmgrd (all nodes)**

Create ``/etc/systemd/system/repmgrd.service``:

.. code-block:: ini

   [Unit]
   Description=repmgr daemon
   After=postgresql.service
   Requires=postgresql.service

   [Service]
   User=postgres
   ExecStart=/usr/lib/postgresql/17/bin/repmgrd -f /etc/repmgr.conf --no-daemonize
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target

.. code-block:: bash

   sudo systemctl daemon-reload
   sudo systemctl enable repmgrd
   sudo systemctl start repmgrd

✅ **Phase 3 checkpoint** — run on any node:

.. code-block:: bash

   sudo -u postgres repmgr -f /etc/repmgr.conf cluster show

**Pass:** Output shows all three nodes — pg1 as ``* running`` (primary), pg2 and
pg3 as ``running`` (standby). On pg1, the following query returns 2 rows:

.. code-block:: bash

   sudo -u postgres psql -c "SELECT client_addr, state FROM pg_stat_replication;"

**Fail:** A standby showing ``! running`` means replication did not establish.
Check ``journalctl -u postgresql`` on the failed standby. Common cause: firewall
blocking port 5432 between nodes.

Phase 4: HAProxy, health check, and VIP (all nodes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run all steps in Phase 4 on **pg1, pg2, and pg3**.

**Step 4.1 — Install HAProxy**

.. code-block:: bash

   sudo apt install -y haproxy

**Step 4.2 — Configure HAProxy**

Replace ``/etc/haproxy/haproxy.cfg``:

.. code-block:: text

   global
       log /dev/log local0
       maxconn 4000

   defaults
       log global
       mode tcp
       timeout connect 5s
       timeout client 30s
       timeout server 30s

   frontend pg_write
       bind *:5000
       default_backend pg_primary

   frontend pg_read
       bind *:5001
       default_backend pg_replicas

   backend pg_primary
       option tcp-check
       server pg1 <PG1_IP>:5432 check port 8008
       server pg2 <PG2_IP>:5432 check port 8008 backup
       server pg3 <PG3_IP>:5432 check port 8008 backup

   backend pg_replicas
       balance roundrobin
       option tcp-check
       server pg2 <PG2_IP>:5432 check port 8008
       server pg3 <PG3_IP>:5432 check port 8008
       server pg1 <PG1_IP>:5432 check port 8008 backup

**Step 4.3 — Deploy pgchk.py**

``pgchk.py`` is a lightweight HTTP server that returns ``200 OK`` when the local
node is the primary and ``503`` otherwise. HAProxy queries port 8008 on each
node to determine where to route connections.

Copy ``pgchk.py`` from the
`ha-postgres-reprmgr-haproxy repository <https://github.com/sadohert/ha-postgres-reprmgr-haproxy>`__
to ``/usr/local/bin/pgchk.py`` on each node and make it executable:

.. code-block:: bash

   sudo chmod +x /usr/local/bin/pgchk.py

Create ``/etc/systemd/system/pgchk.service``:

.. code-block:: ini

   [Unit]
   Description=PostgreSQL Health Check for HAProxy
   After=postgresql.service

   [Service]
   ExecStart=/usr/bin/python3 /usr/local/bin/pgchk.py --port 8008
   Restart=always

   [Install]
   WantedBy=multi-user.target

.. code-block:: bash

   sudo systemctl daemon-reload
   sudo systemctl enable pgchk
   sudo systemctl start pgchk
   sudo systemctl enable haproxy
   sudo systemctl start haproxy

**Step 4.4 — Install and configure Keepalived**

.. code-block:: bash

   sudo apt install -y keepalived

Create ``/etc/keepalived/keepalived.conf``. Set the ``priority`` field: pg1 gets
``101``, pg2 gets ``100``, pg3 gets ``99``. Set ``virtual_ipaddress`` to your VIP:

.. code-block:: text

   vrrp_instance VI_1 {
       state BACKUP
       interface eth0
       virtual_router_id 51
       priority 101
       advert_int 1
       nopreempt
       virtual_ipaddress {
           <CLUSTER_VIP>/24
       }
   }

.. code-block:: bash

   sudo systemctl enable keepalived
   sudo systemctl start keepalived

✅ **Phase 4 checkpoint** — run on any node:

.. code-block:: bash

   # VIP should be active on the primary node (pg1)
   ip addr show | grep <CLUSTER_VIP>

   # Port 5000 should connect to primary
   psql -h <CLUSTER_VIP> -p 5000 -U repmgr -d repmgr \
       -c "SELECT inet_server_addr(), pg_is_in_recovery();"

   # Port 5001 should connect to a standby
   psql -h <CLUSTER_VIP> -p 5001 -U repmgr -d repmgr \
       -c "SELECT inet_server_addr(), pg_is_in_recovery();"

**Pass:** VIP visible on pg1. Port 5000 returns ``pg_is_in_recovery = f`` (primary).
Port 5001 returns ``pg_is_in_recovery = t`` (standby).

**Fail:** If the VIP is not on pg1, check ``journalctl -u keepalived``. If HAProxy
is not routing correctly, check ``journalctl -u haproxy`` and verify pgchk.py
is responding: ``curl http://<PG1_IP>:8008`` should return HTTP 200.

Day-2 operations
----------------

[stub]

Troubleshooting
---------------

[stub]
