Deploy for Sovereign Collaboration in Microsoft Teams
=====================================================

Overview
--------

Agencies and critical infrastructure organizations often face strict data sovereignty requirements that restrict the use of public cloud services for sensitive collaboration. 

Deploying Mattermost for sovereign collaboration within Microsoft Teams and Outlook enables secure, compliant, and resilient communication while maintaining workflow continuity inside familiar Microsoft interfaces. Users access both Teams channels and Mattermost channels :doc:`from within the Microsoft ecosystem </integrations-guide/mattermost-mission-collaboration-for-m365>`, providing a single-pane-of-glass experience and eliminating application switching.

Mattermost can be hosted on-premises or in sovereign clouds, such as Azure GovCloud or Azure Local, ensuring that messages, files, recordings, and transcriptions remain in compliance-approved systems with encryption and strict policy enforcement. 

Unified authentication with Microsoft Entra-ID extends your Microsoft enterprise IT investments while delivering the compliance, control, and resilience required for mission-critical operations or out-of-band scenarios.

This document outlines architectural guidance for enabling sovereign collaboration within your Microsoft ecosystem.

.. image:: /images/architecture-ms-teams-collab.png
   :alt: Mattermost diagram displays the deployment components and relationships outlined in detail in this document.

.. note::
  Consider `talking to a Mattermost expert <https://mattermost.com/contact-sales/>`__ if your organization needs support deploying Mattermost and supporting services for soverign collaboration within your Microsoft ecosystem.

Architecture components
-----------------------

The deployment architecture includes the following components:

- **Users:** Enterprise users within the network boundary accessing client applications for M365 services and Mattermost.   

- **Microsoft Entra ID (Identity Provider):** Users authenticate to M365 applications and Mattermost using :doc:`single sign-on Entra ID </administration-guide/onboard/sso-entraid>` via OpenID Connect (OIDC) or SAML.

- **Client Applications:**

  - **Microsoft 365 Desktop Apps:** Teams and Outlook with :doc:`embedded Mattermost application </integrations-guide/mattermost-mission-collaboration-for-m365>` for seamless collaboration within a familiar interface while enforcing regulatory compliance.

  - **Mattermost Desktop Apps:** Access Mattermost via :doc:`desktop </deployment-guide/desktop/desktop-app-deployment>` or web apps in addition to the embedded views from Teams and Outlook. *(Optional - not shown)*

  - **Mattermost Mobile Apps:** Access Mattermost via :doc:`iPhone and Android apps </deployment-guide/mobile/mobile-app-deployment>`, with support for :doc:`ID-only push notifications </deployment-guide/mobile/host-your-own-push-proxy-service>` to ensure compliance with data sovereignty requirements. *(Optional - not shown)*

- **Mattermost Deployment:** Mattermost deployed for sovereign collaboration on enterprise-controlled infrastructure or private cloud, such as :doc:`Azure </deployment-guide/server/deploy-kubernetes>` or `Azure Local <https://learn.microsoft.com/en-us/azure/azure-local/manage/disconnected-operations-overview>`_, to maintain compliance with STIG, FedRAMP, and NIST 800-53 standards. See :doc:`reference architecture </deployment-guide/server/server-architecture>` documentation for Mattermost deployment configurations based on expected scale.

  - **Mattermost Server:** Core application server handling collaboration workloads, including:

    - :doc:`Messaging Collaboration </end-user-guide/messaging-collaboration>`: DDIL-ready 1:1, group messaging, and structured channel collaboration with :doc:`rich integration capabilities </integrations-guide/integrations-guide-index>` and :ref:`enterprise-grade search <administration-guide/scale/scaling-for-enterprise:enterprise search>`.

    - :doc:`Workflow Automation </end-user-guide/workflow-automation>`: Playbooks provide structure, monitoring and automation for repeatable processes built-in to your sovereign Mattermost deployment.

    - :doc:`Project Tracking </end-user-guide/project-task-management>`: Boards enables project management capabilities built-in to your sovereign Mattermost deployment.

    - :doc:`AI Agents </administration-guide/configure/agents-admin-guide>`: AI Agents run against Azure OpenAI endpoints or a self-hosted LLM that is OpenAI-compatible. 

    - :doc:`Audio & Screenshare </administration-guide/configure/calls-deployment>`: Calls offers native real-time self-hosted audio calls and screen sharing within your own network.

  - **Proxy Server:** The :doc:`proxy server </deployment-guide/server/setup-nginx-proxy>` handles HTTP(S) routing within the cluster, directing traffic between the server and clients accessing Mattermost services. NGINX is recommended for load balancing with support for WebSocket connections, health check endpoints, and sticky sessions. The proxy layer provides SSL termination and distributes client traffic across application servers.

  - **PostgreSQL Database:** Stores persistent application data on a :doc:`PostgreSQL v13+ database </deployment-guide/server/preparations>`, such as `Azure Database for PostgreSQL <https://azure.microsoft.com/en-us/products/postgresql>`_.

  - **Object Storage:** File uploads, images, and attachments are stored outside the application node on an :doc:`S3-compatible store </deployment-guide/server/preparations>`, such as MinIO. `Azure Blob Storage <https://azure.microsoft.com/en-us/products/storage/blobs>`_ can be used, but needs an S3-compatible proxy for Mattermost to interface with.

  - **Recording Instance:** ``calls-offloader`` :ref:`job service <administration-guide/configure/calls-deployment:configure recording, transcriptions, and live captions>` to offload heavy processing tasks from Mattermost Calls, such as recordings, transcriptions, and live captioning, to enterprise-controlled infrastructure or private cloud. *(Optional)*

- **Self-hosted integrations:** :doc:`Custom apps, plugins, and webhooks </integrations-guide/integrations-guide-index>` can be deployed within the enterprise boundary. *(Optional - not shown)*

**Secure Access Layer:** A firewall or access gateway protecting entry into the enterprise network. This may include network policies, IP allowlists, or WAFs depending on your networking configurations. *(Optional)*

**Microsoft Global Network:** `World-wide network <https://learn.microsoft.com/en-us/azure/networking/microsoft-global-network>`_ of Microsoft data centers, delivering public cloud services including M365 and Azure OpenAI. 

**Azure OpenAI Service:** :doc:`LLM service </agents/docs/providers>` used for summarization, ai-enhanced search, and agent-assisted workflows, hosted within the Microsoft Global Network. *(Optional)*

Operational Best Practices
--------------------------

The following best practices and deployment configurations help ensure that Mattermost remains compliant, resilient, and fully sovereign when deployed alongside Microsoft 365.

High availability and fault tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deploy Mattermost in a :doc:`cluster-based architecture </administration-guide/scale/high-availability-cluster-based-deployment>` to ensure continued availability during outages or hardware failures. High availability requires redundant infrastructure across each critical component:

- Application servers: Scale horizontally across multiple nodes with a load balancer distributing client traffic.
- Database layer: Use PostgreSQL replication or managed HA services with automatic failover.
- Search service: :ref:`Elasticsearch or AWS OpenSearch Service <administration-guide/scale/scaling-for-enterprise:enterprise search>` provides optimized search performance with dedicated indexing for large-scale deployments.
- Object storage: Configure S3-compatible backends with erasure coding or replication for durability. All application servers must access shared file storage (NAS or S3) to ensure consistent data availability.
- Calls services: Run multiple ``rtcd`` and ``calls-offloader`` nodes for resilience.

Sovereign audio & screensharing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data sovereignty compliance may require that all voice and screen sharing traffic remain within enterprise-controlled infrastructure and does not traverse third-party services. Deploy :doc:`Mattermost Calls </administration-guide/configure/calls-deployment>` in a self-hosted configuration to ensure that Microsoft Teams users and Mattermost users collaborate without media ever leaving the sovereign network.

- The :ref:`rtcd service <administration-guide/configure/calls-deployment:the rtcd service>` for scalable, low-latency media routing hosted on-premises. Run multiple ``rtcd`` nodes for redundancy.
- The :ref:`calls offloader <administration-guide/configure/calls-deployment:configure recording, transcriptions, and live captions>` service offloads heavy processing tasks like recording, transcription and live captioning to a compliance-approved job server.

Compliance and retention
~~~~~~~~~~~~~~~~~~~~~~~~

Sovereign environments often require strict enforcement of retention policies, legal hold, and export controls. Configure Mattermost's built-in compliance features to meet agency or sectoral mandates.

- Enable :doc:`compliance export </administration-guide/comply/compliance-export>` and :doc:`monitoring </administration-guide/comply/compliance-monitoring>` to produce auditable exports of message data and user activity logs.
- Configure :doc:`message retention </administration-guide/comply/data-retention-policy>` and :doc:`legal hold </administration-guide/comply/legal-hold>` policies to align with applicable regulations.
- Integrate with your organization's :doc:`eDiscovery </administration-guide/comply/electronic-discovery>` and archiving systems as required.

Mobile notifications
~~~~~~~~~~~~~~~~~~~~

To prevent sensitive message content from being transmitted to external notification services such as Apple Push Notification Service (APNS) and Firebase Cloud Messaging (FCM), configure Mattermost to use :doc:`ID-only push notifications </deployment-guide/mobile/host-your-own-push-proxy-service>`. In this configuration, only a message identifier is sent to public push notification services and the client retrieves the content securely from the Mattermost server over an encrypted channel.
