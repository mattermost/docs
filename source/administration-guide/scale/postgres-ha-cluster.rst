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

[stub]

Day-2 operations
----------------

[stub]

Troubleshooting
---------------

[stub]
