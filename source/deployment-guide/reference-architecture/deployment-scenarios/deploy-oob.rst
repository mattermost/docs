Deploy for Out-of-Band (OOB) Communications
===========================================

When a critical incident disrupts an organization’s primary infrastructure—due to a cyberattack, cloud outage, or internal failure—a secure, independent communication channel becomes essential. Mattermost can serve as that channel by operating in an Out-of-Band (OOB) environment: isolated, pre-provisioned, and ready to support incident response and business continuity teams.

This document outlines architectural guidance for deploying Mattermost in an OOB scenario across `generic <#generic-oob-architecture>`__, `AWS <#aws-based-oob-deployment>`__, and `Azure <#azure-based-oob-deployment>`__ environments.

Generic OOB architecture
------------------------

This platform-agnostic design establishes a fallback communication system, decoupled from primary networks and identity providers.

.. image:: /images/oob-generic-architecture.png
   :alt: Generic OOB Architecture
   :align: center

Architecture components
~~~~~~~~~~~~~~~~~~~~~~~

- **Users (Cybersecurity, IR Teams)**: Pre-authorized personnel trained to access and use the OOB platform during emergencies. Credentials and access methods should be provisioned in advance.
- **Secure Access Layer**: A firewall or access gateway protecting entry into the OOB environment. May include network policies, IP allowlists, or WAFs.
- **Secondary IdP / Emergency Auth**: A dedicated identity provider not dependent on the organization’s primary SSO or IdP (e.g., a minimal Azure AD tenant, Okta org, or locally stored credentials with MFA).
- **VPN / Bastion Host**: A hardened jumpbox or independent VPN granting access to internal OOB components and Kubernetes control plane.
- **Failover DNS Manager**: Services like Cloudflare Load Balancer, Azure Traffic Manager, or Route 53 to monitor primary system health and reroute DNS to the OOB ingress.
- **Ingress Controller**: e.g., ingress-nginx to handle HTTP(S) routing within the cluster, directing traffic to Mattermost Web, API, and WebSocket endpoints.
- **Mattermost Operator & App**: Automates lifecycle of Mattermost instances in Kubernetes; ensures updates, scaling, and configuration consistency.
- **PostgreSQL Database**: Persistent storage for channels, messages, users, and configurations; can be self-hosted or managed externally with hardened access.
- **Backups**:

  - **Velero**: Backs up Kubernetes resources to external object store (S3, Blob).
  - **pg_dump / Cloud-native backup**: Regular logical exports or managed backups.
  - **Object Storage**: Durable, versioned storage (e.g., S3, Azure Blob) for snapshots and dumps.

AWS-based OOB deployment
------------------------

Deploying Mattermost in AWS leverages managed services and strong isolation capabilities.

.. image:: /images/oob-aws-architecture.png
   :alt: AWS OOB Deployment diagram
   :align: center

AWS components
~~~~~~~~~~~~~~~

- **Amazon EKS**: Managed Kubernetes for Mattermost Operator and application, with HA and auto-scaling.
- **Route 53**: DNS service for health-checked failover to the OOB environment.
- **Amazon Aurora PostgreSQL**: High-performance managed PostgreSQL with automated failovers.
- **Amazon S3**: Object storage for Velero snapshots, configurations, and database backups (with versioning and cross-region replication).
- **IAM Roles**: Scoped roles for EKS nodes and Velero using IRSA, enforcing least-privilege.

.. tip::

  - Use separate AWS accounts or VPCs for full isolation.
  - Configure Route 53 health checks against public or synthetic endpoints.
  - Encrypt secrets and enforce least-privilege IAM policies.

Azure-Based OOB deployment
--------------------------

For Azure customers, AKS and related services provide a robust OOB platform for Mattermost.

.. image:: /images/oob-azure-architecture.png
   :alt: Azure OOB Deployment diagram
   :align: center

Azure components
~~~~~~~~~~~~~~~~~

- **Azure Kubernetes Service (AKS)**: Runs Mattermost workloads with native autoscaling and Azure AD integration.
- **Azure DNS + Traffic Manager**: Global traffic routing and DNS failover based on endpoint health.
- **Azure Database for PostgreSQL**: Managed DB service with automated backups and patching.
- **Azure Blob Storage**: Destination for Velero snapshots and DB dumps; supports lifecycle policies and secure access.
- **Azure AD (Secondary Tenant)**: Acts as the IdP for OOB; deployed in a separate directory with scoped permissions and MFA.

.. tip::

  - Deploy in a dedicated subscription for security and billing separation.
  - Use Azure Monitor for health checks and Traffic Manager probes.
  - Harden AKS node pools and isolate workloads with namespaces and network policies.

Operational guidelines
----------------------

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - **Domain**
     - **Recommendation**
   * - Access Control
     - Isolate authentication from primary infrastructure. Use MFA, secure vaults, and emergency tokens. Preload user accounts in the secondary IdP.
   * - DNS Failover
     - Employ TTL-aware health checks via Route 53 or Traffic Manager. Monitor critical HTTP(S) or TCP endpoints.
   * - Backup Strategy
     - Schedule frequent Velero and database backups. Store in versioned, encrypted object storage.
   * - Disaster Recovery Drills
     - Conduct quarterly failover exercises: DNS switching, Mattermost access, and data restores.
   * - Security
     - Treat OOB as Tier 0. Use hardened OS images, audit logging, strict RBAC, and centralized monitoring. Rotate secrets regularly.

Mattermost can be an effective OOB communication platform when deployed with isolation, automation, and operational readiness. Whether on AWS, Azure, or a generic environment, prioritize independence, simplicity, and resilience. Pair these designs with standard IR playbooks and routine failover testing to build a confident, secure response capability.
