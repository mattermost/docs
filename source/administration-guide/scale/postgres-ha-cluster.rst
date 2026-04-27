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

[stub]

Setup guide
-----------

[stub]

Day-2 operations
----------------

[stub]

Troubleshooting
---------------

[stub]
