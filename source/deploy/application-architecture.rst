Application architecture
=========================

Mattermost is an open-source collaboration platform that offers secure messaging, file sharing, and integrations for team communication. It's self-hosted, providing IT admins full control over data, security, integrations, and customization. The platform is built with modular components to ensure scalability, flexibility, and extensibility.

.. image:: ../images/network-diagram.svg
   :alt: Mattermost network diagram shows how the components can be deployed. Includes optional configurations for scaling for larger enterprise organizations.
   :class: bg-white

Workflow overview
-----------------

Users connect through various access points (web, mobile, desktop, email). Their requests are processed by the application layer (Mattermost Server), which manages API communications, authentication, notifications, and data workflows.

The backend infrastructure supports these operations by storing all data and files in well-architected storage systems.

Extendability and security layers ensure that the platform integrates seamlessly with enterprise systems while protecting sensitive data.

Core components
----------------

The technical architecture revolves around 3 main layers: `Access layer <#access-layer>`__, `Application layer <#application-layer>`__, and `Backend infrastructure <#backend-infrastructure>`__.

Access layer
~~~~~~~~~~~~

The Access Layer includes all the ways users interact with Mattermost, ensuring secure, scalable, and reliable communication across preferred platforms. High availability measures provide uninterrupted functionality for users, even in the face of server or network failures.

- **Web Interface**: Users can access Mattermost through a web browser (Chrome, Firefox, Safari, Edge). The web client communicates with the Mattermost server over HTTPS protocols. High availability for web interfaces can be achieved through load-balanced reverse proxies (e.g., NGINX or HAProxy) that distribute user traffic across multiple Mattermost server instances. Backup proxy servers can ensure failover scenarios to keep the web interface operational during outages.
- **Desktop and Mobile Apps**: Native apps for iOS, Android, macOS, Windows, and Linux provide seamless functionality across devices. These apps rely on secure APIs to interact with the server for real-time messaging and updates. High availability can be ensured by deploying redundant server clusters to handle API requests, along with failover mechanisms that automatically redirect traffic to healthy servers. Mobile apps also benefit from retry mechanisms and fallback services for push notifications to maintain real-time responsiveness.
- **Email Interaction**: Support for email clients like Outlook, Gmail, or Thunderbird enables integration of email notifications (e.g., new message alerts, invitations) into users' typical workflows. The Access Layer ensures that users are always connected via platforms of their choice while maintaining secure, synchronized communication paths. Email services can be configured with multiple SMTP servers for redundancy, ensuring that notifications are sent without delay even if a primary mail server becomes unavailable.

The Access Layer plays a critical role in ensuring that users are always connected via the platforms of their choice while maintaining secure, synchronized communication paths. With high availability measures in place, organizations can guarantee a seamless user experience, regardless of the scale or complexity of their deployment.

Application layer
~~~~~~~~~~~~~~~~~

The Mattermost Server is the heart of the platform and responsible for processing all user and system operations. It's composed of multiple modular elements as follows:

.. image:: ../images/architecture_basics.png
   :alt: Mattermost architecture basics
   :class: bg-white

**RESTful JSON Web Service**: Handles all incoming API requests (from web clients, apps, and integrations) and ensures that responses are formatted in JSON. Acts as the communication bridge between the clients (Access Layer) and backend systems. To ensure high availability, this layer can be distributed across multiple servers and load-balanced, preventing service disruptions due to high traffic or server failure.

**Authentication client**: Manages user authentication, ensuring secure login sessions. Integrates with traditional username/password-based authentication or enterprise-grade solutions like SSO (Single Sign-On) through Active Directory/LDAP. High availability is maintained through redundant authentication nodes and failover mechanisms, ensuring uninterrupted access even if a primary authentication service fails.

**Authentication Provider**: Provides pluggable authentication frameworks to support OAuth, SSO, and third-party identity services. Particularly important for enterprise environments with centralized identity management. Redundancy and failover strategies ensure reliability by distributing authentication frameworks across multiple servers and offering fallback options for seamless identity management.

**Notification Service**: Sends notifications through supported mediums:

- **Push Notifications**: Real-time notifications to iOS and Android devices (via a Push Notification Service). High availabilty is ensured through multiple notification servers and retry mechanisms, guaranteeing that notifications are delivered even in the event of service disruptions.
- **Email Notifications**: Delivered to users when they are offline or need event alerts. Load balancing and backup mail server configurations help ensure email delivery remains consistent and reliable.

**Data Management Service**: Responsible for managing message data, metadata, user profiles, and logs. Ensures the integrity of data passed between the database and the server. This layer serves as the operational core of the platform, orchestrating user activities with data handling and integration capabilities. 

High availability is achieved through database replication, failover strategies, and distributed data handling mechanisms. These measures ensure uninterrupted access to data and protect against component failures or downtime. The Data Management Service serves as the operational core of the platform, orchestrating user activities with scalable and fault-tolerant data handling capabilities.

Backend infrastructure
~~~~~~~~~~~~~~~~~~~~~~

The backend infrastructure provides the storage and data handling capabilities required for Mattermost operations. It consists of the following components:

**Database Systems**: Mattermost uses PostgreSQL as its primary database (supports Amazon RDS for cloud-hosted PostgreSQL) to store all persistent data, such as:

- Messages
- User accounts and credentials
- Configuration settings
- Team/channel metadata

To ensure high availability, database systems can leverage clustering, replication, and failover mechanisms. PostgreSQL supports features like synchronous and asynchronous replication to create replicas for redundancy. Cloud-hosted solutions like Amazon RDS provide automatic failover and backup capabilities, ensuring continuous operation during system failures.

**File Storage**: Manages all multimedia assets (e.g., file uploads, images, videos) shared across channels. Storage solutions include the following options:

- **Local Storage**: Files stored directly on the server’s filesystem. For high availability, redundancy can be achieved using RAID configurations or backups to recover from disk failures.
- **Network Attached Storage (NAS)**: Common for enterprises centralizing file storage within their network. NAS setups can include fault-tolerant configurations like distributed systems or replication for uninterrupted access.
- **S3**: Offers cloud-based scalable storage for larger environments or organizations with distributed deployments. The database and file storage handle scalability, ensuring efficient support for millions of messages and files while guaranteeing data consistency. S3 inherently supports high availability by distributing data across multiple availability zones, ensuring no single point of failure.

High availability measures ensure scalable and fail-safe support for millions of messages and files while guaranteeing data consistency.

**System Extensions**: Mattermost is not only a collaboration tool but also a platform designed for extensibility. Key extensibility features include:

**Self-Hosted Integrations**: Connect Mattermost to other local or cloud-based systems like Jira, GitLab, or any custom integrations your team needs. Leverage built-in APIs and webhooks to automate workflows and trigger system-to-system communications. For high availaiblity, integrations can employ redundant communication channels and retry mechanisms to handle transient failures gracefully.  

**Third-Party Authentication**: Bind integrations to third-party platforms (e.g., Slack-importing APIs, OAuth services). Third-party identity services ensure consistent and secure user access flows. Third-party identity services can leverage load-balancing and failover strategies to ensure consistent and secure user access flows, even under high traffic or outages.

**Security and Scalability Features**: Security and scalability are baked into the architecture, making Mattermost ideal for enterprise use cases:

**Security**

- A reverse proxy like NGINX or a hardware proxy is deployed to manage external traffic. It protects servers, enforces HTTPS, and handles load balancing.
- Configurable SSL/TLS encryption ensures data security during transmission.
- Granular user permissions and roles secure sensitive information within teams.

**Scalability and High Availability**: The Enterprise Edition supports deploying multiple Mattermost servers in a clustered environment to balance user requests across multiple servers for reliability and performance in large organizations. Clustering ensures automatic failover so that user traffic is shifted to functioning servers in case of outages.

**Notifications and communication services**: Mattermost supports asynchronous and real-time communication, enhanced by notification systems tailored for different workflows:

- **Push Notifications**: Delivered to mobile devices for message alerts or mentions. High availability is achieved with backup notification services and retry mechanisms for reliable delivery.
- **Email Integration**: Provides regular notifications when users are offline or inactive. Failover mail servers and distributed configurations ensure email notifications are sent without interruption.

These services ensure continuous engagement and communication.

Communication protocols
~~~~~~~~~~~~~~~~~~~~~~~

There are also communication protocols (HTTPS and WS) that define the type of connection the user makes with the Mattermost server. High availability measures ensure reliable and resilient connections between clients and the Mattermost server, especially in production environments.

**HTTPS Connection** (Secure Hypertext Transfer Protocol)

- HTTPS connections to the Mattermost server render pages and provide access to core platform functionality, but do not include real-time interactivity (which is enabled by WSS connections).
- HTTPS is a secure, encrypted protocol and is highly recommended for production. Unencrypted HTTP connections may be used in initial testing and configuration, but should never be used in a production environment. For high availability, HTTPS traffic should be handled by a reverse proxy (e.g., NGINX or HAProxy) with load balancer configurations to distribute connections across multiple Mattermost server instances. Redundant proxy servers ensure failover capabilities, providing uninterrupted service.

**WSS Connection** (Secure WebSocket Protocol)

Secure WebSocket (WSS) connections to the Mattermost Server enable real-time updates and notifications between clients and the server.

If a WSS connection is not available and HTTPS is substituted, the system will appear to work but real-time updates and notifications will not. In this mode of operation, updates will only appear on a page refresh. WSS has a persistent connection to the Mattermost server when a client is connected, while HTTPS has an intermittent connection and only connects to the server when a page or file is requested.

High availability for WSS connections can be achieved through clustering Mattermost servers and load balancing WebSocket connections across those cluster nodes. Proxy servers and WebSocket-specific configurations (such as sticky sessions or connection persistence) are essential to maintain real-time interactivity during server or network failures.

.. image:: ../images/architecture_with_protocol.png
   :alt: Mattermost architecture with protocol connections
   :class: bg-white

By incorporating high availability strategies into communication protocols, the platform ensures secure, scalable, and reliable connections for both regular user interactions (via HTTPS) and real-time updates (via WSS). These measures are critical for mission-critical environments and distributed deployments where continuous communication is necessary.

**Behind a VPN**

Mattermost is intended to be installed within a private network which can offer multiple factors of authentication, including secure access to computing devices and physical locations. If outside access is required, a virtual private network client (VPN), such as `OpenVPN <https://openvpn.net/>`__, with additional authentication used to connect to Mattermost for web, desktop, and mobile experiences, is recommended.

**Non-VPN setup**

If Mattermost is accessible from the open internet, the following is recommended:

1. An IT admin should be assigned to set up appropriate network security, subscribe to `the Mattermost security bulletin <https://mattermost.com/security-updates/#sign-up>`__, and :doc:`apply new security updates </upgrade/upgrading-mattermost-server>`.
2. The organization enables :doc:`SAML Single Sign-on </onboard/sso-saml>` or enable :doc:`MFA </onboard/multi-factor-authentication>`.

If Mattermost is accessible from the open internet with no VPN or MFA set up, we recommended using it only for non-confidential, unimportant conversations where impact of a compromised system is not essential.

Mattermost services ports
^^^^^^^^^^^^^^^^^^^^^^^^^

The following table lists the Mattermost services ports for Mattermost Server, push proxy, and mobile app clients. System admins with clients that need to speak to the Mattermost server without a proxy can open specific firewall ports as needed.

**Mattermost Server**

+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+
| Service Name                                                | Config Setting                        | Port (default)                    | Protocol  | Direction  | Info                                                          |
+=============================================================+=======================================+===================================+===========+============+===============================================================+
| HTTP/Websocket                                              | ServiceSettings.ListenAddress         | 8065/80/443 (TLS)                 | TCP       | Inbound    | External (no proxy) / Internal (with proxy)                   |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+ Usually this requires port 80 and 443 when running HTTPS.     |
|                                                             |                                       |                                   |           |            |                                                               |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+
| Cluster                                                     | ClusterSettings.GossipPort            | 8074                              | TCP/UDP   | Inbound    | Internal                                                      |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+
| Metrics                                                     | MetricsSettings.ListenAddress         | 8067                              | TCP       | Inbound    | External (no proxy) / Internal (with proxy)                   |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+
| Database                                                    | SqlSettings.DataSource                | 5432 (PostgreSQL) / 3306 (MySQL)  | TCP       | Outbound   | Usually internal (recommended)                                |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+
| LDAP                                                        | LdapSettings.LdapPort                 | 389                               | TCP/UDP   | Outbound   |                                                               |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+
| S3 Storage                                                  | FileSettings.AmazonS3Endpoint         | 443 (TLS)                         | TCP       | Outbound   |                                                               |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+
| SMTP                                                        | EmailSettings.SMTPPort                | 10025                             | TCP/UDP   | Outbound   |                                                               |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+
| Push Notifications                                          | EmailSettings.PushNotificationServer  | 443 (TLS)                         | TCP       | Outbound   |                                                               |
+-------------------------------------------------------------+---------------------------------------+-----------------------------------+-----------+------------+---------------------------------------------------------------+

**Push Proxy**

+---------------+-----------------+-----------------+-----------+------------+----------------------------------------------+
| Service Name  | Config Setting  | Port (default)  | Protocol  | Direction  | Info                                         |
+===============+=================+=================+===========+============+==============================================+
| Push Proxy    | ListenAddress   | 8066            | TCP       | Inbound    | External (no proxy) / Internal (with proxy)  |
+---------------+-----------------+-----------------+-----------+------------+----------------------------------------------+

**Mobile Clients**

To receive push notifications, your network must allow traffic on `port 5223 for iOS devices <https://support.apple.com/en-us/102266>`_ and `ports 5228-5230 for Android <https://firebase.google.com/docs/cloud-messaging/concept-options#messaging-ports-and-your-firewall>`_.