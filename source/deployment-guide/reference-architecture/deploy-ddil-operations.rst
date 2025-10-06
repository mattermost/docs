Deploy for Enterprise to Edge DDIL Operations
=========================================

Overview
--------

Disconnected, Denied, Intermittent, and Limited (DDIL) network conditions present unique challenges for enterprise-to-edge operations. Field operations, remote deployments, and edge environments often become temporarily isolated from the internet, interrupting direct access to Microsoft 365 services such as Teams and Outlook.

Mattermost enables resilient collaboration by remaining fully operational in DDIL environments. Mission users continue to access self-hosted messaging collaboration, workflow automation, and mission planning within their mobile tactical network. No internet connectivity is required for enhanced collaboration functions, including mission tuned AI agents powered by self-hosted LLMs, and audio and screen sharing services.

When connectivity is restored, mission users regain access to M365 enterprise systems in addition to collaboration continuity with enterprise users through the :doc:`embedded Mattermost experience </integration-guide/mattermost-mission-collaboration-for-m365>` inside their Microsoft Teams and Outlook applications. All mission activity during the period of disconnection becomes available across enterprise and tactical environments when connectivity returns. 

Traditional cloud-only solutions fail in these scenarios, while fully disconnected systems don't integrate with enterprise tools during normal operations. This deployment architecture extends :doc:`sovereign collaboration with Microsoft Teams and Outlook </deployment-guide/reference-architecture/deploy-sovereign-collaboration>` to the tactical edge, providing a hybrid solution that enables enterprise integration and fully disconnected tactical collaboration.

.. image:: /images/architecture-ms-teams-ddil.png
   :alt: Mattermost diagram displays the deployment components and relationships outlined in detail in this document.

Architecture components
-----------------------

This hybrid deployment architecture provides optimal collaboration in both connected and disconnected states, including:

- **Enterprise Network:** Network containing enterprise services and continuous access to Microsoft 365. The network may have a firewall or access gateway protecting egress and ingress, such as network policies, IP allowlists, or WAFs depending on your networking configurations.

- **Enterprise Users:** Users within the enterprise network boundary accessing client applications for M365 services and Mattermost.

- **Tactical Network:** Operates independently during internet disconnections, hosting a self-contained Mattermost deployment to ensure mission users maintain collaboration capabilities.

- **Mission Users:** Tactical or edge users who may be intermittently disconnected from enterprise systems and Microsoft services.

- **Identity Providers:**

  - **Microsoft Entra ID:** Enterprise users authenticate to M365 applications and Mattermost using :doc:`single sign-on Entra ID </administration-guide/onboard/sso-entraid>` via OpenID Connect (OIDC) or SAML. This provider only works with functioning internet access.

  - **Alternative Local Identity Provider:** Deployed within the tactical network to provide authentication services for mission users during disconnected periods when M365 is unreachable. The local IdP serves as the primary authentication source for Mattermost and maintains an independent user directory that operates without internet connectivity. 

- **Client Applications:**

  - **Microsoft 365 Desktop Apps:** Teams and Outlook with :doc:`embedded Mattermost application </integration-guide/mattermost-mission-collaboration-for-m365>`.

    - When internet connected: Enables seamless enterprise-to-edge collaboration within a familiar interface.

    - When internet disconnected: Microsoft services are unreachable, but embedded Mattermost application remains fully operational for tactical teams.

  - **Mattermost Desktop Apps:** Access Mattermost via :doc:`desktop </deployment-guide/desktop/desktop-app-deployment>` or web apps in addition to the embedded views from Teams and Outlook. *(Optional - not shown)*

  - **Mattermost Mobile Apps:** Access Mattermost via :doc:`iPhone and Android apps </deployment-guide/mobile/mobile-app-deployment>`, with support for :doc:`ID-only push notifications </deployment-guide/mobile/host-your-own-push-proxy-service>` to ensure compliance with data sovereignty requirements. *(Optional when connectivity permits - not shown)*

- **Mattermost Deployment:** Mattermost deployed for sovereign tactical collaboration on local infrastructure, such as `Azure Local <https://learn.microsoft.com/en-us/azure/azure-local/manage/disconnected-operations-overview>`_, supporting data residency regulations and :doc:`disconnected operations </deployment-guide/server/air-gapped-deployment>`. See :doc:`reference architecture </deployment-guide/server/server-architecture>` documentation for Mattermost deployment configurations based on expected scale.

- **Mattermost Server:** Core application server handling tactical collaboration workloads, including:

  - :doc:`Messaging Collaboration </end-user-guide/messaging-collaboration>`: DDIL-ready 1:1, group messaging, and structured channel collaboration with rich integration capabilities and enterprise-grade search.

  - :doc:`Workflow Automation </end-user-guide/workflow-automation>`: Playbooks provide structure, monitoring and automation for repeatable processes built-in to your local Mattermost deployment.

  - :doc:`Project Tracking </end-user-guide/project-task-management>`:** Boards enables project management capabilities built-in to your local Mattermost deployment.

  - :doc:`AI Agents </administration-guide/configure/agents-admin-guide>`: AI Agents run against a local LLM hosted within your tactical network. 

  - :doc:`Audio & Screenshare </administration-guide/configure/calls-deployment>`: Calls offers native real-time self-hosted audio calls and screen sharing within your tactical network.

- **Proxy Server:** The :doc:`proxy server </deployment-guide/server/setup-nginx-proxy>` handles HTTP(S) routing within the cluster, directing traffic between the server and clients accessing Mattermost services. NGINX is recommended for load balancing with support for WebSocket connections, health check endpoints, and sticky sessions. The proxy layer provides SSL termination and distributes client traffic across application servers.

- **PostgreSQL Database:** Stores persistent application data on a :doc:`PostgreSQL v13+ database </deployment-guide/server/preparations>` hosted locally within your tactical network.

- **Object Storage:** File uploads, images, and attachments are stored outside the application node on an :doc:`S3-compatible store </deployment-guide/server/preparations>`, such as MinIO, hosted locally within your tactical network.

- **Recording Instance:** ``calls-offloader`` :ref:`job service </administration-guide/configure/calls-deployment:configure recording, transcriptions, and live captions>` to offload heavy processing tasks from Mattermost Calls to self-hosted infrastructure within your tactical network, such as recordings, transcriptions, and live captioning. *(Optional)*

- **Self-hosted integrations:** Custom apps, plugins, and webhooks can be deployed within your tactical network. *(Optional - not shown)*

- **Self-hosted LLM:** Locally hosted OpenAI compatible LLM for agentic powered collaboration within your tactical network. *(Optional)*

- **Microsoft Global Network:** World-wide network of Microsoft data centers, delivering public cloud services when internet connectivity permits. 

Operational Best Practices
--------------------------

The following best practices and deployment configurations help ensure that Mattermost remains compliant and operationally resilient in contested environments.

User Authentication
~~~~~~~~~~~~~~~~~~~

DDIL environments require authentication infrastructure that remains fully operational without internet connectivity. Relying solely on cloud-based identity providers like Microsoft Entra ID creates a critical single point of failure when tactical networks become disconnected. To ensure mission users maintain authentication capabilities, deploy a locally hosted identity provider within the tactical network.

**Enterprise Users:** Access Teams and Outlook by authenticating to Microsoft 365 via Entra ID, and their M365 session also provides access to the embedded Mattermost experience when the tactical network is internet connected.

**Mission users:** Authenticate to Mattermost using a local IdP, such as Keycloak (open-source IdP with OIDC/SAML support), Active Directory with ADFS, or OpenLDAP with an OIDC bridge. When internet connected, the local IdP can optionally federate with Microsoft Entra ID to synchronize user accounts, credentials, and group memberships to enable access to Microsoft applications.

User accounts must be provisioned in the local IdP before disconnection occurs to ensure authentication services remain available throughout DDIL conditions. 

Sovereign AI
~~~~~~~~~~~~

Deploy an OpenAI compatible LLM on tactical infrastructure to ensure AI capabilities remain fully sovereign and operational in disconnected scenarios. A self-hosted LLM can power message and call summarization, semantic search, and mission-tuned AI agents without relying on public cloud AI services. This guarantees compliance with strict data handling mandates and enables AI-enhanced workflows to function locally, even during extended disconnections.

Self-hosted audio & screensharing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Effective collaboration at the tactical edge requires all voice and screen sharing capabilities remain operational without reliance on the internet or third-party services. Deploy Mattermost Calls in a self-hosted configuration, including:

- The rtcd service for scalable, low-latency media routing hosted on-premises. Run multiple ``rtcd`` nodes for redundancy.
- The calls offloader service offloads heavy processing tasks like recording, transcription and live captioning to a locally hosted compliance-approved job server.

High availability and fault tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deploy Mattermost in a cluster-based architecture to ensure continued availability during outages or hardware failures. High availability requires redundant infrastructure across each critical component:

- Application servers: Scale horizontally across multiple nodes with a load balancer distributing client traffic.
- Search service: Elasticsearch or AWS OpenSearch Service provides optimized search performance with dedicated indexing for large-scale deployments.
- Object storage: Configure S3-compatible backends with erasure coding or replication for durability. All application servers must access shared file storage (NAS or S3) to ensure consistent data availability.
- Calls services: Run multiple ``rtcd`` and offloader nodes for resilience.

Compliance and retention
~~~~~~~~~~~~~~~~~~~~~~~~

Sovereign environments often require strict enforcement of retention policies, legal hold, and export controls. Configure Mattermost's built-in compliance features to meet organizational mandates.

- Enable compliance export and monitoring to produce auditable exports of message data and user activity logs.
- Configure message retention and legal hold policies to align with applicable regulations.
- Integrate with your organization's eDiscovery and archiving systems as required.

Talk to an Expert
-----------------
