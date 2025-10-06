Deploy for Mission Partner Collaboration
==================================

Overview
--------

Mission partner collaboration extends sovereign and edge deployment models to enable joint and allied operations across organizations using Mattermost, Microsoft 365 and legacy platforms. This solution architecture outlined in this document delivers a secure, sovereign, and intelligent mission environment that is federated across enterprise and coalition partner networks, enabling interoperability while maintaining compliance and control.

Joint mission collaboration is achieved through federation using connected workspaces, Matrix connectors, guest accounts, and auto-translation for fast, accurate comprehension across globally distributed teams. Additionally, integrating external data feeds, workflow automation, and sovereign AI enables allied and partner users to collaborate at mission speed while enforcing zero-trust policies and maintaining data sovereignty.

Mattermost deployments may be hosted on-premises or in sovereign clouds, enabling allies and partners to retain control over sensitive data while extending interoperability to coalition partner enterprise networks.

Collaboration challenges
------------------------

Multi-agency collaborations face complex communication challenges:

- **Platform diversity:** Organizations often use different platforms, including Microsoft 365, Mattermost, and Matrix - with some using Teams for enterprise productivity supplemented with Mattermost for sovereign collaboration, data residency, and offline resilience. 
- **External access:** External partners need controlled access without full organizational membership.
- **Language barriers:** Organizations may speak different languages.
- **Compliance:** Data residency and compliance requirements vary across organizations.

Solution Architecture
---------------------

Traditional solutions require everyone to adopt the same platform or use insecure external tools. Mattermost powers a multi-layer approach addressing these collaboration challenges and diverse organizational needs, including: 

- **Mattermost ↔ Mattermost Collaboration:** Organizations with Mattermost deployments establish secure connections and share specific channels using Connected Workspaces over standard HTTPS/VPN.

- **External users ↔ Mattermost Collaboration:** Users from external organizations receive Mattermost guest accounts with least-privilege access. External users in Microsoft environments may access Mattermost using the embedded application in their Teams and Outlook clients.

- **Matrix / XMPP ↔ Mattermost Collaboration:** Organizations using legacy XMPP systems or Matrix servers connect to Mattermost via the Matrix bridge plugin for bidirectional communication.

- **Automatic Language Translation:** AI-powered automatic translation enables seamless communication across language barriers in channels with distributed teams.

Architecture components
-----------------------

The deployment architecture includes the following components:

- **Allied or Partner Networks:** Globally distributed and segregated networks for each allied or partner organization.

  - Networks may have a firewall or access gateway protecting egress and ingress, such as network policies, IP allowlists, or WAFs depending on networking configurations.
  - Networks may operate in contested environments where internet connectivity is intermittent.

- **Users:** Enterprise, allied, and coalition partner users accessing client applications for Mattermost and/or Microsoft 365.

- **Microsoft Entra ID (Identity Provider):** Partnered organizations using Microsoft 365 services may use Entra ID for unified authentication to M365 and Mattermost applications. *(Optional)*

- **Federation Services:**
  - **Connected workspaces:** Federated collaboration across partner networks, with seamless synchronization of messages, threads, and files.
  - **Guest Accounts:** Secure participation of external mission partners with least-privilege access. *(Optional)*
  - **Matrix & XMPP Interoperability:** Federation with legacy partner systems for cross-domain coalition collaboration. *(Optional)*

- **Client Applications:**
  - **Mattermost Desktop Apps:** Access Mattermost directly by deploying desktop or web apps in your organization.
  - **Mattermost Mobile Apps:** Access Mattermost via iPhone and Android apps, with support for ID-only push notifications to ensure compliance with data sovereignty requirements. *(Optional - not shown)*
  - **Microsoft 365 Desktop Apps:** For partnered organizations using Microsoft 365 services, Teams and Outlook can be deployed with the embedded Mattermost application for cross-domain partner collaboration within a familiar interface. *(Optional)* 

- **Mattermost Deployments:** Mattermost deployed for sovereign collaboration on private cloud or local infrastructure, such as Azure or Azure Local, to maintain compliance with STIG, FedRAMP, and NIST 800-53 standards. See reference architecture documentation for Mattermost deployment configurations based on expected scale.

- **Mattermost Server:** Core application server handling collaboration workloads, including:
  - **Messaging Collaboration:** Sovereign 1:1, group messaging, and structured channel collaboration.
  - **Workflow Automation (Optional):** Playbooks provide structure, monitoring and automation for repeatable processes built-in to your sovereign Mattermost deployment.
  - **Project Tracking (Optional):** Boards enables project management capabilities built-in to your sovereign Mattermost deployment.
  - **AI Agents (Optional):** AI Agents run against Azure OpenAI endpoints or a self-hosted LLM that is OpenAI-compatible.
  - **Audio & Screenshare (Optional):** Calls offers native real-time self-hosted audio calls and screen sharing within your own network.

- **Proxy Server:** The proxy server handles HTTP(S) routing within the cluster, directing traffic between the server and clients accessing Mattermost services, including requests from users in connected organizations. NGINX is recommended for load balancing with support for WebSocket connections, health check endpoints, and sticky sessions. The proxy layer provides SSL termination and distributes client traffic across application servers.

- **PostgreSQL Database:** Stores persistent application data on a PostgreSQL v13+ database, such as Azure Database for PostgreSQL.

- **Object Storage:** File uploads, images, and attachments are stored outside the application node on an S3-compatible store, such as MinIO. Azure Blob Storage can be used, but needs an S3-compatible proxy for Mattermost to interface with.

- **Recording Instance:** ``calls-offloader`` job service to offload heavy processing tasks from Mattermost Calls, such as recordings, transcriptions, and live captioning, to local infrastructure or private cloud. *(Optional)*

- **Integration framework:** Custom apps, plugins, and webhooks can be deployed for real-time data integrations and alerting. *(Optional - not shown)*

- **Self-hosted LLM:** Locally hosted OpenAI compatible LLM for agentic powered collaboration. *(Optional)*

- **Microsoft Global Network:** World-wide network of Microsoft data centers, delivering public cloud services including M365 and Azure OpenAI. *(Optional)* 

Operational Best Practices
--------------------------

The following best practices and deployment configurations help ensure that Mattermost remains secure, resilient, and interoperable across federated mission partner environments.

Network Configuration
~~~~~~~~~~~~~~~~~~~~~

When external access is enabled through various federation capabilities, it is recommended to deploy Mattermost in a DMZ rather than on the internal network. This approach provides defense-in-depth and preserves security boundaries by isolating each connected server deployment from the enterprise network.

- **DMZ Deployment:** Position Mattermost application servers in the DMZ network segment, allowing both internal users and external partner federation traffic to access the collaboration platform through controlled network boundaries.
- **VPN Termination:** Terminate site-to-site VPN connections at the network perimeter or DMZ layer, enabling encrypted partner connectivity without exposing internal network infrastructure. VPN tunnels establish secure communication channels between partner organizations over the internet.
- **Firewall Segmentation:** Deploy ingress and egress firewall rules to control traffic flow between the DMZ, internal network, and external partner networks. Restrict database and object storage access to only originate from the DMZ segment where Mattermost servers reside.
- **Federation Traffic Isolation:** Partner federation traffic (Connected workspaces synchronize over HTTPS port 443/TCP) remains isolated within the DMZ, protecting internal systems while enabling partner collaboration and enforcing zero-trust principles across organizational boundaries.

Resilient federation for joint operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connected workspaces allow federated collaboration across multiple organizations and networks while maintaining local data control of each Mattermost deployment. Messages, threads, and files are securely synchronized between environments, ensuring mission continuity for multinational operations without requiring partners to join a single centralized deployment.

- Enforce zero-trust access and ensure that only authorized mission partners can view or contribute to shared collaboration channels.
- Configure auto-translation in shared channels for seamless multilingual cross-domain collaboration.
- Mattermost instances can operate independently during outages or intermittent connectivity and sync conversations once connectivity returns.

Many mission partners continue to operate on legacy systems such as Matrix and XMPP. To enable joint operations without forcing migration, Mattermost supports secure interoperability with these environments for continuity of coalition communications while allowing modernized workflows to extend across federated networks.

Synchronize Mattermost channels with Matrix or XMPP rooms, allowing messages, threads, and attachments to flow across systems in real-time. Each organization maintains control of its data and infrastructure, while interoperability is enabled through federation bridges rather than centralized services.

Controlled external access
~~~~~~~~~~~~~~~~~~~~~~~~~~

Mission partner collaboration may require involving external users such as allied forces, contractors, or coalition partners that do not have Mattermost deployments themselves. Guest accounts provide a controlled mechanism to enable these users to participate in joint mission operations while maintaining strict compliance and security boundaries.

- Guest accounts are restricted to specific teams and channels. This ensures external users only have access to mission-critical resources necessary for their role.
- Guests can be granted access to shared channels, enabling collaboration with additional trusted organizations through connected workspaces.
- Guest users can be provided VPN credentials that allow them to connect specifically to the DMZ network segment where Mattermost resides. This architecture ensures external guests can access the collaboration platform without gaining access to internal corporate resources, files, or systems.

Zero-trust access controls
~~~~~~~~~~~~~~~~~~~~~~~~~~

Mission partner collaboration environments should adopt zero-trust principles by implementing attribute-based access control (ABAC) to ensure access to mission channels is governed by dynamic attributes such as role, clearance, location, and mission context.

- Restrict channel access based on user attributes rather than static groups.
- Continuously audit ABAC policies to ensure compliance with multinational operational and legal requirements.

Sovereign AI
~~~~~~~~~~~~

AI capabilities enhance mission collaboration with summarization, translation, semantic search, and decision support. Sovereign AI ensures these capabilities remain fully under organizational control, without reliance on public cloud services or external data processing. Deploying AI in a self-hosted or compliance-approved environment enables secure, mission-ready augmentation.

- Deploy OpenAI-compatible language models on local or private cloud infrastructure to maintain data sovereignty and ensure offline availability.
- Configure custom agents for summarization, workflow automation, and decision support while enforcing organizational compliance policies.
- Enable multilingual collaboration in shared channels using sovereign AI services to provide real-time translations across partner organizations.
- Embed AI into operational playbooks for automated task execution, situational summaries, and proactive recommendations.
- Allow authorized users from partner organizations to securely access locally hosted LLMs through shared channels in connected workspaces.

High availability and fault tolerance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deploy Mattermost in a cluster-based architecture to ensure continued availability during outages or hardware failures. High availability requires redundant infrastructure across each critical component:

- Application servers: Scale horizontally across multiple nodes with a load balancer distributing client traffic.
- Search service: Elasticsearch or AWS OpenSearch Service provides optimized search performance with dedicated indexing for large-scale deployments.
- Object storage: Configure S3-compatible backends with erasure coding or replication for durability. All application servers must access shared file storage (NAS or S3) to ensure consistent data availability.
- Calls services: Run multiple ``rtcd`` and offloader nodes for resilience.

Sovereign audio & screensharing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deploy Mattermost Calls in a self-hosted configuration to ensure voice and screen sharing capabilities remain operational without reliance on the internet, and that media traffic does not traverse non-compliant third-party services.

- The rtcd service for scalable, low-latency media routing hosted on-premises. Run multiple ``rtcd`` nodes for redundancy.
- The calls offloader service offloads heavy processing tasks like recording, transcription and live captioning to a locally hosted compliance-approved job server.

Compliance and retention
~~~~~~~~~~~~~~~~~~~~~~~~

Sovereign environments often require strict enforcement of retention policies, legal hold, and export controls. Configure Mattermost's built-in compliance features to meet agency or sectoral mandates.

- Enable compliance export and monitoring to produce auditable exports of message data and user activity logs.
- Configure message retention and legal hold policies to align with applicable regulations.
- Integrate with your organization's eDiscovery and archiving systems as required.

Mobile notifications
~~~~~~~~~~~~~~~~~~~~

To prevent sensitive message content from being transmitted to external notification services such as Apple Push Notification Service (APNS) and Firebase Cloud Messaging (FCM), configure Mattermost to use ID-only push notifications. In this mode, only a message identifier is sent to public push notification services, and the client retrieves the content securely from the Mattermost server over an encrypted channel.

Talk to an Expert
-----------------