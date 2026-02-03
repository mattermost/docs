Module 1.0: Deployment Preparations

Module Summary: This foundational module prepares learners to plan and architect Mattermost deployments in mission-critical environments by covering core architecture, deployment methods, database requirements, file storage options, and proxy configuration.

Table of Contents:

Section 1: Introduction
  Page 1: Module Overview

Section 2: Architecture and Deployment Methods
  Page 2: Mattermost Architecture Components
  Page 3: Deployment Methods Overview

Section 3: Database and Storage Preparation
  Page 4: Database Requirements
  Page 5: File Storage Options

Section 4: Proxy and Security
  Page 6: NGINX Proxy Preparation

Section 5: Module Summary
  Page 7: Module Complete

________________________________________

Page Title: Module Overview

Page 1 of 7

Estimated Time: 3 minutes

________________________________________


Deployment preparation is foundational to secure operations in the Intelligent Mission Environment. In Defense, Intelligence, Security, and Critical Infrastructure operations, proper deployment planning prevents security vulnerabilities and ensures mission continuity. A well-architected deployment supports real-time collaboration for mission operations, secure development workflows for DevSecOps teams, and cyber-resilient infrastructure for sovereign deployments.

This module equips you with the knowledge to assess customer requirements and plan Mattermost deployments that meet enterprise and government standards. You will learn to evaluate deployment architectures, select appropriate deployment methods, and prepare the infrastructure components required for production environments.

In this module, you will learn to prepare for successful Mattermost deployments in mission-critical environments.


In this module, you will learn:

You will begin by exploring how Mattermost architecture components work together to deliver secure real-time collaboration.

How to evaluate deployment methods and select the right approach for different operational requirements.

How to prepare database infrastructure with PostgreSQL version compatibility planning.

How to select and configure file storage solutions for different security and scale requirements.

You will finish by looking at NGINX reverse proxy configuration for secure TLS termination and traffic management.


Prerequisites

Before working with Mattermost deployment preparation, ensure you have the following:

Technical knowledge: You should understand basic Linux system administration including command-line operations, file permissions, and service management. You should be familiar with networking fundamentals including IP addressing, DNS, and firewall configuration. You should understand database concepts including relational databases and SQL basics.

Access requirements: You need access to planning documentation and architecture diagrams. For hands-on practice in later modules, you will need administrative access to Linux servers.

License requirements: This module covers concepts applicable to all Mattermost editions. Some features discussed may require Mattermost Enterprise license for production use.

Environment requirements: No specific environment is required for this preparation module. Later modules will require Linux servers for deployment practice.


Core Concepts

Mattermost is a secure collaboration platform designed for organizations that require control over their communications infrastructure. Unlike cloud-only solutions, Mattermost deploys in your own infrastructure, whether on-premises, in private cloud, or air-gapped environments.

The platform uses a three-layer architecture. The Access Layer provides user interfaces including web browsers, desktop applications, and mobile devices. The Application Layer runs the Mattermost Server which processes all requests and manages collaboration features. The Backend Infrastructure Layer includes the database, file storage, and optional services like search and caching.

Understanding this architecture helps you plan deployments that meet specific requirements. Defense contractors need air-gapped deployments with classification controls. Intelligence agencies require compartmented access and audit logging. Security operations centers need high availability for incident response. Critical infrastructure organizations require resilient deployments that support shift-based operations.

Deployment preparation involves five key areas. First, understand the architecture components and how they communicate. Second, evaluate deployment methods including Kubernetes, Linux servers, and containers. Third, prepare database infrastructure with appropriate PostgreSQL versions. Fourth, select file storage that matches security and scale requirements. Fifth, plan reverse proxy configuration for TLS termination and load balancing.

Each deployment method has specific use cases. Kubernetes provides auto-scaling and high availability for large production deployments. Linux server installation offers complete control for organizations with specific security requirements. Container-based deployment using Docker simplifies development and testing environments.

The database serves as the central data store for all Mattermost data including users, channels, messages, and configurations. PostgreSQL version 14 or higher is required. The database must be prepared before Mattermost installation.

File storage holds uploaded files, images, and attachments. Three options exist: S3-compatible object storage for production and high availability, Network File Storage using NFS for on-premises deployments, and local file storage for development environments only.

A reverse proxy like NGINX sits between users and the Mattermost Server. The proxy handles TLS encryption, provides a single entry point for security controls, and enables load balancing in clustered deployments. NGINX is the recommended reverse proxy for production environments.

This module establishes the foundation for deployment. Subsequent modules will guide you through hands-on installation and configuration. By the end of this module, you will be able to assess customer requirements and design appropriate Mattermost architectures.


Visual Asset Suggestion: Architecture overview diagram showing the three layers with icons for users, applications, servers, database, and storage. This helps visual learners understand the component relationships.


________________________________________

Page Title: Mattermost Architecture Components

Page 2 of 7

Estimated Time: 4 minutes

________________________________________


Mattermost uses a three-layer architecture that separates concerns and enables flexible deployment options. Understanding these layers helps you design deployments that meet security, scale, and operational requirements for defense and critical infrastructure environments.


Access Layer

The Access Layer provides user interfaces for interacting with Mattermost. Web browsers access Mattermost through HTTPS connections. Desktop applications for Windows, macOS, and Linux provide native experiences with offline support and notification management. Mobile applications for iOS and Android enable secure mobile access. Email clients receive notification emails when users are offline.

Each access method connects to the Mattermost Server using secure protocols. Web and desktop clients maintain persistent WebSocket connections for real-time updates. When a user sends a message, all other users in that channel receive it instantly through WebSocket push notifications.

For classified environments, mobile access may be restricted or require Mobile Device Management integration. Desktop applications can be customized and distributed through enterprise software deployment systems. Web access can be limited to specific networks or require VPN connectivity.


Application Layer

The Application Layer contains the Mattermost Server which processes all collaboration activities. The server is written in Go for performance and includes several key services.

The RESTful JSON Web Service provides the API for all client interactions. Clients send HTTP requests to create channels, post messages, upload files, and manage settings. The API follows REST principles with predictable endpoints and standard HTTP methods.

The Authentication Client handles user login and session management. It supports multiple authentication methods including username and password, LDAP synchronization, SAML single sign-on, OpenID Connect, and multi-factor authentication. For Defense and Intelligence environments, Common Access Card authentication integrates through SAML providers.

The Notification Service manages push notifications to mobile devices and email notifications. Mobile notifications route through the Mattermost Hosted Push Notification Service or your own Enterprise Push Notification Service for air-gapped deployments. Email notifications require SMTP server configuration.

The Data Management Service coordinates data storage across the database and file storage systems. It handles database transactions, manages file uploads, and maintains data consistency. All data operations go through this service to ensure security and compliance controls apply consistently.


Backend Infrastructure Layer

The Backend Infrastructure Layer provides data persistence and optional services.

Database Systems store all Mattermost data. PostgreSQL version 14 or higher is required. The database contains users, teams, channels, posts, file metadata, system configuration, and audit logs. Amazon RDS PostgreSQL is supported for cloud deployments. MySQL was deprecated starting with Mattermost version 11 and is no longer supported.

File Storage systems hold uploaded files, profile images, and attachments. S3-compatible object storage is recommended for production deployments and required for high availability. Network File Storage using NFS works for on-premises deployments with shared storage. Local file storage stores files directly on the server filesystem and works only for single-server deployments.

System Extensions enable integrations with other tools. Custom plugins extend Mattermost functionality. Webhooks connect external systems. OAuth applications integrate third-party authentication. For DevSecOps workflows, integrations with GitLab, Jenkins, and Jira enable automated notifications and workflow automation.


Communication Protocols

Mattermost uses two primary protocols. HTTPS handles standard web requests including page loads, API calls, and file uploads. The default port is 8065 for direct Mattermost access, but production deployments use port 443 through a reverse proxy.

WebSocket Secure protocol provides persistent connections for real-time updates. When a message is posted, the server immediately pushes it to all connected clients in that channel. WebSocket connections use the same port as HTTPS and upgrade from HTTP using standard WebSocket handshake procedures.

Additional ports support specific functions. Port 8074 enables cluster communication between Mattermost servers in high availability deployments using gossip protocol. Port 8067 provides performance metrics for Prometheus monitoring. Port 8065 also serves the metrics endpoint.

Database connections use standard PostgreSQL protocol on port 5432. LDAP authentication requires port 389 for standard LDAP or port 636 for LDAP over SSL. SMTP email notification typically uses port 25, 587, or 465 depending on the mail server configuration.


Security Considerations

Several security measures apply to the architecture. TLS encryption protects all data in transit between clients and servers. A reverse proxy handles TLS termination and forwards requests to Mattermost over the internal network. This separates security concerns and simplifies certificate management.

For internet-accessible deployments, additional security controls are recommended. Multi-factor authentication adds a second verification factor. SAML single sign-on integrates with enterprise identity providers. Rate limiting prevents brute force attacks. IP allowlists restrict access to authorized networks.

For classified deployments at Impact Level 5 or 6, additional controls apply. Air-gapped deployment eliminates internet connectivity. Classification banners display data sensitivity levels. Granular access controls restrict channel access based on clearance levels. Audit logging captures all system activities for compliance reviews.

Firewall configuration restricts port access. Only port 443 should be accessible from user networks. Port 8065 should only be accessible from the reverse proxy and administrative hosts. Database port 5432 should only allow connections from Mattermost servers. Cluster port 8074 should only allow connections between Mattermost servers in high availability deployments.


Visual Asset Suggestions: 
1. Three-layer architecture diagram with color-coded layers showing Access, Application, and Backend components
2. Network port diagram showing which ports are used for each type of communication
3. WebSocket vs HTTPS comparison showing persistent connections vs request-response pattern


Knowledge Check Questions

Use Workramp Multiple Choice question object.

Question: A defense contractor is planning a Mattermost deployment for 5,000 users across multiple security enclaves. The architecture requires real-time message delivery, audit logging, and the ability to scale horizontally. Which Mattermost architecture layer is responsible for coordinating data storage and enforcing security controls consistently across all operations?

A. Access Layer - handles user interfaces and client connections
B. Application Layer Data Management Service - coordinates all data operations
C. Backend Infrastructure Layer - provides data persistence
D. Authentication Client - manages security and access control

Correct Answer: B

Explanation: The Data Management Service within the Application Layer coordinates all data storage operations across database and file storage systems. It ensures security and compliance controls apply consistently to every operation. While the Backend Infrastructure provides storage, the Data Management Service orchestrates how data is stored and retrieved. The Authentication Client handles login, not ongoing data operations. The Access Layer only provides user interfaces.

Hint: The Data Management Service is the single point of coordination for all data operations in Mattermost. It sits in the Application Layer and works with both database and file storage. This centralized design ensures consistent security policy enforcement. Remember that coordination happens in the Application Layer, not the Backend Layer.

Key Takeaways: Understanding service responsibilities in the Application Layer is essential for troubleshooting data flow issues. The Data Management Service coordinates between multiple backend systems. Centralized data coordination enables consistent security control enforcement.


Use Workramp Multiple Choice question object.

Question: Your organization requires persistent real-time connections to deliver messages instantly to all channel members during active cyber defense operations. Which protocol and port combination does Mattermost use for these real-time updates in production deployments with NGINX reverse proxy?

A. HTTPS on port 8065 with polling every 5 seconds
B. WebSocket Secure on port 443 upgraded from HTTPS
C. Server-Sent Events on port 8067 for one-way streaming
D. Custom TCP protocol on port 8074 for gossip communication

Correct Answer: B

Explanation: Mattermost uses WebSocket Secure protocol for real-time bidirectional communication. In production deployments with a reverse proxy, WebSocket connections use port 443 and upgrade from HTTPS using standard WebSocket handshake. This provides instant message delivery without polling. Port 8065 is for direct Mattermost access without proxy. Port 8067 serves metrics. Port 8074 is for server-to-server cluster communication, not client connections.

Hint: WebSocket connections start as HTTPS requests and then upgrade to WebSocket protocol. In production, the reverse proxy handles this on port 443. The persistent connection enables instant message delivery without client polling. This is a common certification exam topic regarding real-time communication architecture.

Key Takeaways: WebSocket provides real-time bidirectional communication for instant message delivery. Production deployments use port 443 through reverse proxy for both HTTPS and WebSocket. Understanding protocol upgrades is essential for troubleshooting real-time connectivity issues.


Use Workramp Select All That Apply question object.

Question: An intelligence agency deployment requires Impact Level 6 compliance with air-gapped infrastructure. Which Backend Infrastructure components must be included in the deployment? Select all that apply.

A. PostgreSQL database for storing all Mattermost data
B. S3-compatible object storage or NFS for file attachments
C. Mattermost Hosted Push Notification Service for mobile devices
D. Enterprise Push Notification Service for air-gapped mobile support

Correct Answer: A, B, D

Explanation: PostgreSQL database is always required for all Mattermost deployments. File storage is required and must be S3-compatible or NFS for production. For air-gapped environments, the Mattermost Hosted Push Notification Service cannot be used because it requires internet connectivity. The Enterprise Push Notification Service must be deployed within the air-gapped environment to support mobile devices. This allows mobile notifications without external internet connections.

Hint: Air-gapped deployments cannot use any hosted external services. All infrastructure must run within the secure environment. The Hosted Push Notification Service is cloud-based and requires internet access. IL6 compliance requires complete network isolation. Remember that Enterprise Push Notification Service is specifically designed for air-gapped environments.

Key Takeaways: Air-gapped deployments require all services to run internally without internet access. Database and file storage are always mandatory components. Enterprise Push Notification Service enables mobile support in classified environments.


________________________________________

Page Title: Deployment Methods Overview

Page 3 of 7

Estimated Time: 5 minutes

________________________________________


Mattermost supports three primary deployment methods. Each method has specific advantages and use cases. Selecting the right deployment method depends on operational requirements, team expertise, and infrastructure constraints.


Kubernetes Deployment

Kubernetes deployment is recommended for production environments. Kubernetes is a container orchestration platform that automates deployment, scaling, and management of containerized applications.

Kubernetes provides several advantages for mission-critical deployments. Auto-scaling automatically adjusts the number of Mattermost pods based on load. If CPU or memory usage increases during peak operations, Kubernetes launches additional pods. When load decreases, it reduces pods to optimize resource usage. This is critical for operations centers that experience variable usage patterns.

High availability comes built into Kubernetes. Multiple Mattermost pods run simultaneously behind a load balancer. If one pod fails, traffic automatically routes to healthy pods. Users experience no interruption. The Kubernetes control plane monitors pod health and restarts failed containers automatically.

Automated updates simplify maintenance. Kubernetes performs rolling updates by gradually replacing old pods with new versions. During updates, some pods run the old version while others run the new version. This ensures zero downtime during upgrades. If problems occur, rollback to the previous version happens quickly.

Infrastructure as code makes deployments repeatable and auditable. Kubernetes manifests describe the desired state in YAML files. Version control tracks all infrastructure changes. This meets compliance requirements for change management and provides audit trails for security reviews.

Kubernetes deployments work well for organizations with container expertise. DevSecOps teams familiar with Kubernetes can leverage existing skills and tools. Integration with existing Kubernetes infrastructure uses established monitoring, logging, and security controls.

The main requirement is Kubernetes cluster infrastructure. Most cloud providers offer managed Kubernetes services including AWS EKS, Azure AKS, and Google GKE. For on-premises or air-gapped deployments, self-managed Kubernetes requires significant expertise. Tools like Rancher or OpenShift simplify Kubernetes management for organizations building their own clusters.


Linux Server Deployment

Linux server deployment provides complete control over the installation. Mattermost runs directly on the Linux operating system without containerization. This method works well for organizations that prefer traditional server management or have specific security requirements.

Direct installation offers several benefits. You control every aspect of the system including kernel parameters, security modules, and package versions. For environments with specific security hardening requirements, direct installation enables precise configuration. Organizations using Security Technical Implementation Guides can apply all required settings.

Linux deployment supports multiple distributions. Ubuntu is commonly used and has extensive community support. Red Hat Enterprise Linux and CentOS provide commercial support options. Debian offers stability for long-term deployments. Oracle Linux is used in organizations with existing Oracle infrastructure.

This deployment method works for various scales. Small teams can run Mattermost on a single server. Growing organizations can deploy multiple servers with load balancing. High availability configurations use three or more Mattermost servers with shared database and file storage.

Organizations with strong Linux administration expertise prefer this method. System administrators can apply familiar tools and procedures. Integration with existing infrastructure management, monitoring, and backup systems uses standard Linux approaches.

Consider Linux deployment for environments that restrict container usage. Some security policies prohibit containers due to concerns about shared kernel security. Other organizations lack container expertise and prefer traditional approaches. Regulatory requirements may mandate specific operating system configurations that are easier to achieve with direct installation.


Docker Container Deployment

Docker container deployment packages Mattermost and its dependencies in containers. Docker Compose orchestrates multiple containers including Mattermost, NGINX reverse proxy, and PostgreSQL database.

Containers provide simplified installation. A single Docker Compose file describes the entire stack. Running docker-compose up starts all services. This reduces installation complexity compared to configuring each component separately.

Consistent environments across development, testing, and production prevent configuration drift. The same container images run everywhere. Developers can run the exact production environment on their laptops. This improves DevSecOps workflows by catching issues early.

Important limitations apply to Docker deployment. Docker Compose does not support high availability. You cannot run multiple Mattermost containers behind a load balancer using Docker Compose. For high availability, use Kubernetes instead. Docker Desktop on macOS and Windows is not supported for Mattermost deployments. Only Linux Docker Engine is supported.

Use Docker deployment for specific scenarios. Development environments benefit from quick setup and teardown. Testing environments can quickly spin up isolated instances. Proof of concept deployments demonstrate Mattermost functionality quickly. Small team deployments where high availability is not required can use Docker on Linux servers.

Do not use Docker Compose for production environments requiring high availability, large scale, or business continuity. Kubernetes provides production-grade orchestration. Linux server installation provides more control than Docker Compose.


Deployment Decision Factors

Several factors guide deployment method selection. Team expertise is critical. Teams with Kubernetes experience should use Kubernetes. Teams with traditional Linux administration expertise may prefer Linux server deployment. Teams wanting quick proof of concept should use Docker.

Operational requirements matter. High availability requires Kubernetes or multi-server Linux deployment. Single server deployments can use any method. Specific security requirements may mandate Linux deployment for precise control.

Infrastructure availability affects decisions. Organizations with existing Kubernetes clusters should use Kubernetes deployment. Organizations with server virtualization infrastructure can use Linux server deployment. Organizations with container platforms can evaluate Kubernetes or Docker based on scale requirements.

Consider future growth. Start with a deployment method that supports your growth path. If high availability will be needed eventually, starting with Kubernetes or planning multi-server Linux deployment prevents migration later. If scale is uncertain, Kubernetes provides the easiest path to scaling.

Regulatory and compliance requirements may limit options. Some frameworks require specific operating system hardening that is easier with Linux deployment. Other frameworks accept containerized deployments with appropriate security controls. Review compliance requirements before selecting deployment methods.


Visual Asset Suggestions:
1. Deployment method comparison table showing features, advantages, limitations, and use cases for each method
2. Decision flowchart helping readers select appropriate deployment method based on requirements
3. Scale comparison diagram showing Kubernetes with multiple pods, Linux with multiple servers, and Docker single server


Video Opportunity: A 3-5 minute overview video showing each deployment method in action. Show Kubernetes dashboard with auto-scaling pods. Show Linux server with systemctl managing Mattermost service. Show Docker Compose starting containers. Visual demonstration helps learners understand differences between methods.


Knowledge Check Questions

Use Workramp Multiple Choice question object.

Question: A defense agency plans to deploy Mattermost for 10,000 users across multiple classified networks. Requirements include zero-downtime upgrades, automatic failover, and the ability to scale capacity during large-scale exercises. The team has extensive Kubernetes experience from existing DevSecOps pipelines. Which deployment method best meets these requirements?

A. Linux server deployment with manual load balancer configuration
B. Kubernetes deployment with auto-scaling and rolling updates
C. Docker Compose deployment with health checks and restarts
D. Multiple Linux servers with custom shell scripts for failover

Correct Answer: B

Explanation: Kubernetes deployment provides all required capabilities. Auto-scaling adjusts capacity during high-load exercises. Rolling updates enable zero-downtime upgrades by gradually replacing pods. Built-in failover automatically routes traffic away from failed pods. The team's Kubernetes expertise means they can implement and maintain the deployment effectively. Docker Compose does not support high availability or load balancing. Linux deployments can achieve high availability but require more manual configuration than Kubernetes provides automatically.

Hint: Kubernetes is recommended for production environments specifically because it provides auto-scaling, high availability, and automated updates. The team's existing Kubernetes expertise is important. Using familiar technology reduces risk and implementation time. This scenario tests your ability to match requirements with appropriate deployment methods.

Key Takeaways: Kubernetes is the recommended deployment method for production environments requiring high availability. Auto-scaling and rolling updates are built-in Kubernetes features. Team expertise should influence deployment method selection.


Use Workramp True/False question object.

Question: Docker Compose deployment is appropriate for production environments serving 5,000 users with business continuity requirements and high availability needs.

A. True
B. False

Correct Answer: B (False)

Explanation: Docker Compose does not support high availability configurations. It cannot run multiple Mattermost containers behind a load balancer. For production environments with business continuity requirements, use Kubernetes deployment or multi-server Linux deployment instead. Docker Compose is suitable only for development, testing, proof of concept, or small single-server deployments where high availability is not required. The 5,000 user count and business continuity requirements make Docker Compose inappropriate.

Hint: Docker Compose limitations are a critical exam topic. Remember that Docker Compose does not support high availability or clustering. For any production environment with scale or availability requirements, use Kubernetes or Linux multi-server deployment. Docker Compose is for development and small deployments only.

Key Takeaways: Docker Compose has specific limitations that exclude it from production use cases. High availability requires Kubernetes or clustered Linux servers. Deployment method selection must align with operational requirements.


Use Workramp Multiple Choice question object.

Question: An organization has strict security requirements that mandate specific kernel hardening, custom SELinux policies, and direct control over all system packages. The security team must apply DISA Security Technical Implementation Guides to the operating system. Container usage is prohibited by security policy. Which deployment method meets these requirements?

A. Kubernetes deployment with container security controls
B. Linux server deployment with direct installation
C. Docker deployment with custom base images
D. Kubernetes with virtual machines instead of containers

Correct Answer: B

Explanation: Linux server deployment provides complete control over operating system configuration. Direct installation allows applying kernel hardening, custom SELinux policies, and STIG configurations precisely. Since security policy prohibits containers, Kubernetes and Docker options are not viable regardless of security controls. Linux deployment is the only method that meets both the technical requirements for OS-level control and the policy requirement to avoid containers.

Hint: Some environments prohibit containers for security or policy reasons. In these cases, Linux server deployment is the only option. Direct installation provides maximum control over OS configuration. This is common in highly secure environments with specific compliance requirements. DISA STIGs are military/government security guides that require precise OS configuration.

Key Takeaways: Linux server deployment provides maximum control for security hardening. Some organizations prohibit containers based on security policies. Compliance requirements may mandate specific deployment methods.


________________________________________

Page Title: Database Requirements

Page 4 of 7

Estimated Time: 4 minutes

________________________________________


The database serves as the central data store for all Mattermost information. Proper database selection and preparation is critical for reliable operations. PostgreSQL is the required database for Mattermost.


PostgreSQL Version Requirements

Mattermost requires PostgreSQL version 14.0 or higher. This requirement ensures compatibility with database features that Mattermost uses for performance and reliability. Amazon RDS PostgreSQL and Amazon Aurora PostgreSQL are supported for cloud deployments.

PostgreSQL version requirements follow a predictable policy. Mattermost aligns with PostgreSQL community support timelines. The PostgreSQL community supports each major version for five years. When a PostgreSQL version approaches end of life, Mattermost updates its minimum version requirement.

Mattermost provides nine months notice before requiring a new PostgreSQL version. This gives administrators time to plan and execute database upgrades. The notice appears in release notes, documentation, and deprecation announcements. For Extended Support Release versions, the notice period aligns with ESR schedules to minimize disruption.

Understanding the version timeline helps with long-term planning. As of Mattermost v10.6, PostgreSQL 13 or higher is required. Future releases will require PostgreSQL 14 or higher, with specific timelines announced in advance. Always check current documentation for the most recent version requirements.

For new deployments, use PostgreSQL 14 or the latest stable version. This provides the longest support window before upgrades are required. Avoid using minimum supported versions for new installations unless specific compatibility requirements exist.


MySQL Deprecation

MySQL support was deprecated starting with Mattermost v11. MySQL is no longer supported for new or existing installations. Organizations using MySQL must migrate to PostgreSQL before upgrading to Mattermost v11 or later.

The decision to deprecate MySQL was based on technical considerations. PostgreSQL provides advanced features that improve Mattermost performance and reliability. PostgreSQL full-text search offers better internationalization support. JSON data type support enables more efficient configuration storage. PostgreSQL community support and ecosystem align better with Mattermost technical direction.

If you currently use MySQL, migration to PostgreSQL is required. Mattermost provides a migration tool that automates most of the process. The tool exports data from MySQL, converts schema and data, and imports into PostgreSQL. Plan migration during maintenance windows and test thoroughly in non-production environments before migrating production systems.

For planning purposes, do not propose MySQL for any new Mattermost deployments. All architecture planning must include PostgreSQL. If customers mention MySQL, inform them about deprecation and plan PostgreSQL from the beginning.


Database Preparation Steps

Before installing Mattermost, prepare the database following these steps.

First, create a PostgreSQL server instance. This can be a dedicated server, virtual machine, cloud database instance, or containerized PostgreSQL. For production environments, deploy PostgreSQL on separate infrastructure from the Mattermost application server. This separation improves security and performance.

Second, create the Mattermost database. Connect to PostgreSQL as a superuser and execute database creation commands. The database must use UTF8 encoding to support internationalization. Character set and collation must be set correctly for proper text handling.

In PostgreSQL command line, run:

CREATE DATABASE mattermost WITH ENCODING UTF8 LC_COLLATE equals en_US.UTF-8 LC_CTYPE equals en_US.UTF-8 TEMPLATE equals template0;

This creates a database named mattermost with proper encoding settings. The template0 template ensures clean creation without inherited objects.

Third, create a database user for Mattermost. Do not use the PostgreSQL superuser for Mattermost connections. Create a dedicated user with limited privileges following the principle of least privilege.

Run:

CREATE USER mmuser WITH PASSWORD your_secure_password;

Replace your_secure_password with a strong randomly generated password. Store the password securely in a password manager or secrets management system.

Fourth, grant necessary privileges to the Mattermost user. The user needs permission to connect to the database and perform all operations within that database.

Run:

GRANT ALL PRIVILEGES ON DATABASE mattermost TO mmuser;

For PostgreSQL 15 and higher, additional privileges are required. Connect to the mattermost database and grant schema privileges:

GRANT ALL PRIVILEGES ON SCHEMA public TO mmuser;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO mmuser;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO mmuser;

These grants ensure the Mattermost user can create tables, sequences, and other objects needed during installation and operation.

Fifth, configure remote database access if the database runs on a separate server. Edit the PostgreSQL configuration file postgresql.conf to allow network connections. Set:

listen_addresses equals asterisk

This allows PostgreSQL to accept connections on all network interfaces. For better security, specify the specific IP address of the Mattermost server instead of asterisk.

Edit the client authentication file pg_hba.conf to allow connections from the Mattermost server. Add a line like:

host mattermost mmuser mattermost_server_ip/32 scram-sha-256

Replace mattermost_server_ip with the actual IP address of your Mattermost server. The /32 subnet mask means only that specific IP address can connect. The scram-sha-256 authentication method provides secure password authentication.

After configuration changes, restart the PostgreSQL service to apply changes.

Sixth, test database connectivity from the Mattermost server before installing Mattermost. Use the psql command line tool to verify connection:

psql --host equals database_server --port equals 5432 --username equals mmuser --dbname equals mattermost

If connection succeeds, database preparation is complete. If connection fails, troubleshoot network connectivity, firewall rules, and authentication configuration.


Database Configuration Best Practices

Several best practices improve database reliability and performance. Use strong passwords for database users. Generate random passwords at least 16 characters long with mixed case, numbers, and special characters. Do not use default or common passwords.

Enable TLS encryption for database connections in production environments. This protects credentials and data during transmission. Configure PostgreSQL to require SSL connections and configure Mattermost to use SSL connection strings.

Implement regular database backups. Use PostgreSQL pg_dump for logical backups or filesystem-level snapshots for physical backups. Test backup restoration procedures regularly. For compliance purposes, retain backups according to data retention policies.

Monitor database performance and capacity. Track connection counts, query execution times, disk space usage, and replication lag if using read replicas. Set up alerts for abnormal conditions.

For high availability deployments, configure PostgreSQL replication. Streaming replication provides a standby database that can take over if the primary fails. Logical replication enables more complex scenarios like selective replication or multi-master configurations.

Tune PostgreSQL configuration for Mattermost workloads. Important parameters include shared_buffers for memory allocation, max_connections for concurrent connections, and work_mem for query operations. Consult PostgreSQL documentation and Mattermost performance tuning guides for specific recommendations.


Visual Asset Suggestions:
1. PostgreSQL version timeline diagram showing support windows and Mattermost version requirements
2. Database preparation checklist as an infographic
3. Network diagram showing Mattermost server connecting to PostgreSQL database with ports and protocols labeled


Knowledge Check Questions

Use Workramp Multiple Choice question object.

Question: An intelligence agency is upgrading their Mattermost deployment to v11.0 Extended Support Release. The current deployment uses MySQL 8.0 as the database. What action must be taken before upgrading Mattermost?

A. Upgrade MySQL to version 8.2 which is compatible with Mattermost v11
B. Migrate from MySQL to PostgreSQL 14 or higher using the migration tool
C. Configure Mattermost to use both MySQL and PostgreSQL during transition
D. MySQL continues to work with deprecation warnings until Mattermost v12

Correct Answer: B

Explanation: MySQL support was deprecated starting with Mattermost v11 and is no longer supported. Migration to PostgreSQL 14 or higher is required before upgrading to v11. Mattermost provides a migration tool to automate the process. No MySQL version is compatible with v11 or later. Mattermost does not support running both databases simultaneously. The deprecation is immediate in v11, not gradual with warnings.

Hint: MySQL deprecation in Mattermost v11 is a critical exam topic. Remember that MySQL is completely unsupported starting with v11. Migration to PostgreSQL is mandatory. The migration tool automates most of the process but requires planning and testing. Any customer running MySQL must migrate before upgrading to v11 or later.

Key Takeaways: MySQL is not supported in Mattermost v11 and later versions. Migration to PostgreSQL is required before upgrading. The migration tool automates the process but requires testing.


Use Workramp Multiple Choice question object.

Question: You are preparing PostgreSQL 15 for a new Mattermost deployment. After creating the database and user, you grant ALL PRIVILEGES ON DATABASE mattermost TO mmuser. During Mattermost installation, you receive errors about insufficient permissions to create tables. What is the most likely cause?

A. The database user password contains special characters that need escaping
B. PostgreSQL 15 requires additional schema-level privileges not needed in earlier versions
C. The mattermost database was not created with UTF8 encoding
D. The mmuser account needs SUPERUSER privilege to create tables

Correct Answer: B

Explanation: PostgreSQL 15 changed permission handling and requires additional schema-level grants. After granting database privileges, you must also grant privileges on the public schema, tables, and sequences. This is a PostgreSQL 15-specific requirement. Password special characters would cause authentication errors, not permission errors. UTF8 encoding affects character handling, not table creation permissions. SUPERUSER privilege is not required and violates least privilege principles.

Hint: PostgreSQL 15 introduced permission changes that affect Mattermost installations. Remember to grant schema privileges in addition to database privileges for PostgreSQL 15 and higher. The specific commands are: GRANT ALL PRIVILEGES ON SCHEMA public TO mmuser, plus grants for tables and sequences. This is a common troubleshooting scenario in certification exams.

Key Takeaways: PostgreSQL 15 and higher require additional schema-level privilege grants. Database-level grants alone are insufficient. Always consult current documentation for version-specific requirements.


________________________________________

Page Title: File Storage Options

Page 3 of 7

Estimated Time: 3 minutes

________________________________________


Mattermost stores uploaded files, profile images, and message attachments in file storage. Selecting appropriate file storage is critical for security, reliability, and scale. Three file storage options are available.


S3-Compatible Object Storage

S3-compatible object storage is the recommended option for production deployments. Amazon S3 originated this storage model and many providers now offer S3-compatible services. Options include Amazon S3, MinIO for on-premises deployments, Digital Ocean Spaces, Wasabi, and Backblaze B2.

Object storage provides several advantages. High durability protects files with redundant storage across multiple systems. Amazon S3 offers 99.999999999 percent durability. Files are protected against hardware failures. Geographic replication can store copies in multiple regions for disaster recovery.

Scalability is built into object storage. Storage capacity scales automatically as your usage grows. You never run out of space or need to provision additional storage. Pricing is consumption-based with no upfront capacity planning required.

Object storage is required for high availability Mattermost deployments. Multiple Mattermost servers must access the same files simultaneously. Object storage provides shared access from all servers. When a user uploads a file through one server, any server can retrieve it.

Security features in object storage include encryption at rest, access policies, and audit logging. Files are encrypted when stored. Access control policies restrict which systems can access buckets. Audit logs track all access for compliance reviews.

To use S3-compatible storage, you need specific information. Bucket name is the storage container for your files. Region specifies the geographic location of the bucket. Access key ID and secret access key provide authentication credentials. Endpoint URL specifies the S3 service location.

Configure Mattermost file storage by navigating to System Console then Environment then File Storage. Set File Storage System to Amazon S3. Enter the bucket name, region, access key ID, secret access key, and endpoint URL if using S3-compatible services other than Amazon S3.

In config.json, this appears under FileSettings section:

FileSettings:
  DriverName: amazons3
  AmazonS3AccessKeyId: your_access_key
  AmazonS3SecretAccessKey: your_secret_key
  AmazonS3Bucket: your_bucket_name
  AmazonS3Region: your_region
  AmazonS3Endpoint: your_endpoint_url

For Amazon S3, leave AmazonS3Endpoint empty. For other S3-compatible services like MinIO, specify the endpoint URL.


Network File Storage

Network File Storage using Network File System provides shared file access across multiple servers. A dedicated NAS appliance or file server exports an NFS share. All Mattermost servers mount this share to the same local path.

NFS works well for on-premises deployments that need high availability but prefer traditional file storage over object storage. Organizations with existing NFS infrastructure can leverage it for Mattermost file storage.

To use NFS, create a dedicated export on your NAS system. For example, create /export/mattermost_data on the NAS server. Configure NFS export to allow read and write access from Mattermost servers.

On each Mattermost server, create a local mount point:

mkdir /mnt/mattermost_data

Mount the NFS share:

mount -t nfs nas_server:/export/mattermost_data /mnt/mattermost_data

Add the mount to /etc/fstab to automatically mount on boot:

nas_server:/export/mattermost_data /mnt/mattermost_data nfs defaults 0 0

Configure Mattermost to use this directory. Navigate to System Console then Environment then File Storage. Set File Storage System to Local File System. Set Local Storage Directory to /mnt/mattermost_data.

In config.json:

FileSettings:
  DriverName: local
  Directory: /mnt/mattermost_data

Important considerations for NFS include network reliability and performance. NFS traffic should use dedicated storage networks to avoid interference with user traffic. If the NFS server becomes unavailable, file uploads and downloads fail until connectivity is restored. High availability NFS configurations can mitigate this risk.


Local File Storage

Local file storage stores files directly on the Mattermost server filesystem. Files are written to a directory on the local disk. This is the simplest option but has significant limitations.

Local storage works only for single-server deployments. Multiple Mattermost servers cannot share local file storage. Each server would have its own files. Users connecting to different servers would see different files. This makes local storage incompatible with high availability and load balancing.

Use local storage only for development environments, testing, proof of concept deployments, or very small single-server production deployments where high availability is not required.

To configure local storage, create the data directory:

mkdir /opt/mattermost/data
chown -R mattermost:mattermost /opt/mattermost/data

Navigate to System Console then Environment then File Storage. Set File Storage System to Local File System. Set Local Storage Directory to /opt/mattermost/data.

In config.json:

FileSettings:
  DriverName: local
  Directory: /opt/mattermost/data

For production deployments, plan to migrate to S3 or NFS before adding more servers. Migration tools can copy files from local storage to object storage.


Storage Selection Decision Matrix

Choose storage based on deployment requirements. For high availability deployments with multiple servers, use S3-compatible object storage or NFS. S3 is recommended for its scalability and durability.

For single-server deployments, all three options work. S3 provides the easiest growth path. If you later add servers for high availability, no migration is needed. NFS requires NFS infrastructure. Local storage is simplest for proof of concept but requires migration for growth.

For air-gapped environments, use MinIO for S3-compatible storage or NFS. MinIO deploys entirely within your environment without internet connectivity. NFS is a traditional technology that works in any environment.

For cloud deployments, use Amazon S3 or cloud provider object storage. Cloud object storage integrates well with cloud infrastructure and provides excellent durability and performance.

Consider compliance requirements. Some frameworks require encryption at rest for file storage. S3 and NFS support encryption. Some frameworks require geographic restrictions on data storage. Use region settings to control data location.


Visual Asset Suggestions:
1. Storage option comparison table showing features, requirements, and use cases
2. High availability diagram showing multiple Mattermost servers accessing shared S3 storage
3. Migration path diagram showing progression from local to NFS to S3 as deployments grow


Knowledge Check Questions

Use Workramp Multiple Choice question object.

Question: A critical infrastructure organization plans to deploy Mattermost for 8,000 users across three data centers for high availability. The architecture includes three Mattermost servers behind a load balancer. Users may connect to any server based on load balancing decisions. File attachments must be accessible regardless of which server handles the request. Which file storage option meets these requirements?

A. Local file storage on each Mattermost server
B. S3-compatible object storage shared by all servers
C. Local file storage with file replication scripts
D. Separate S3 buckets for each Mattermost server

Correct Answer: B

Explanation: S3-compatible object storage provides shared access from all Mattermost servers. All servers connect to the same bucket and access the same files. When a user uploads a file through any server, it is immediately available to all servers. Local file storage does not work for multi-server deployments because files are not shared. File replication scripts would create synchronization issues and race conditions. Separate buckets would prevent file sharing. S3 is specifically designed for this use case and is required for high availability.

Hint: File storage for high availability is a critical exam topic. Remember that S3-compatible object storage or NFS are the only options for multi-server deployments. Local storage never works with multiple servers. All servers must access the same storage. This requirement is absolute and non-negotiable for load-balanced deployments.

Key Takeaways: High availability requires shared file storage accessible from all servers. S3-compatible object storage is the recommended solution. Local file storage only works for single-server deployments.


Use Workramp True/False question object.

Question: Local file storage provides adequate performance and reliability for production deployments serving 5,000 users with a three-server high availability configuration.

A. True
B. False

Correct Answer: B (False)

Explanation: Local file storage cannot be used in multi-server high availability configurations. Each server would have separate local storage with no file sharing. Files uploaded through one server would not be accessible from other servers. For high availability deployments, S3-compatible object storage or NFS is required. Local file storage is only appropriate for single-server deployments, typically development, testing, or small production deployments without high availability requirements.

Hint: This is a common misconception that appears on certification exams. Local storage fundamentally cannot work with multiple servers. The number of users is irrelevant. The multi-server requirement absolutely requires shared storage. Always choose S3 or NFS for high availability scenarios.

Key Takeaways: Local file storage is incompatible with high availability architectures. Multi-server deployments require S3-compatible object storage or NFS. Storage selection is determined by architecture requirements, not user count.


________________________________________

Page Title: NGINX Proxy Preparation

Page 6 of 7

Estimated Time: 4 minutes

________________________________________


A reverse proxy sits between users and the Mattermost Server. NGINX is the recommended reverse proxy for production Mattermost deployments. Understanding why reverse proxies matter and how to prepare for NGINX configuration is essential for secure deployments.


Why Use a Reverse Proxy

Reverse proxies provide three critical functions: security, performance, and monitoring.

Security benefits include TLS termination. NGINX handles SSL/TLS encryption and decryption. User connections use HTTPS to the proxy. The proxy forwards requests to Mattermost over the internal network using HTTP. This separates security responsibilities. NGINX specialists can manage certificates and TLS configuration. Mattermost administrators focus on collaboration features.

TLS termination at the proxy simplifies certificate management. One certificate protects the entire deployment. In high availability configurations with multiple Mattermost servers, the certificate is installed only on the proxy servers. You do not need certificates on every Mattermost server.

Traffic routing policies enhance security. The proxy can implement IP allowlists, geographic restrictions, and rate limiting. These controls prevent attacks before they reach Mattermost. Rate limiting stops brute force password attacks by limiting login attempts per IP address.

The proxy provides a single entry point for security controls. All traffic flows through the proxy where inspection, logging, and filtering apply. This simplifies security architecture and reduces attack surface. Only proxy ports need to be open to user networks. Mattermost ports are restricted to the internal network.

Performance benefits include load balancing. In high availability deployments, the proxy distributes requests across multiple Mattermost servers. If one server becomes overloaded, the proxy redirects traffic to other servers. This optimizes resource usage and improves response times.

SSL offloading improves performance. TLS encryption and decryption is computationally expensive. Dedicated proxy servers handle this work. Mattermost servers focus on application processing. This division of labor improves overall system capacity.

Connection pooling reduces overhead. The proxy maintains persistent connections to backend Mattermost servers. Multiple user requests can reuse these connections. This reduces connection establishment overhead and improves efficiency.

Monitoring and troubleshooting benefit from centralized logging. The proxy logs all connection attempts, requests, and errors. These logs provide visibility into traffic patterns, failed authentication attempts, and system issues. For compliance, proxy logs capture access attempts for audit purposes.


NGINX Installation and Configuration Overview

NGINX installation is straightforward on major Linux distributions. On Ubuntu or Debian, run:

apt update
apt install nginx

On RHEL or CentOS, run:

yum install nginx

After installation, NGINX runs as a system service. Start and enable it:

systemctl start nginx
systemctl enable nginx

The enable command ensures NGINX starts automatically after system reboot.

NGINX configuration uses text files in specific directories. On Ubuntu, site configurations go in /etc/nginx/sites-available/. On RHEL, configurations go in /etc/nginx/conf.d/. Create a dedicated configuration file for Mattermost.

A typical Mattermost NGINX configuration includes several sections. The upstream block defines backend Mattermost servers. For single-server deployments, list one server. For high availability, list multiple servers with load balancing options.

Example upstream configuration:

upstream backend {
  server 10.0.0.10:8065;
  keepalive 32;
}

For multiple servers:

upstream backend {
  server 10.0.0.10:8065;
  server 10.0.0.11:8065;
  server 10.0.0.12:8065;
  keepalive 32;
}

The server block handles HTTP requests on port 80 and redirects to HTTPS. This ensures all connections use encryption.

Another server block handles HTTPS on port 443. This block specifies TLS certificates, proxies requests to Mattermost, and handles WebSocket upgrades for real-time connections.

WebSocket support is critical. Mattermost uses WebSocket for real-time message delivery. NGINX must be configured to proxy WebSocket connections correctly. This requires specific headers:

proxy_set_header Upgrade $http_upgrade;
proxy_set_header Connection "upgrade";

Without these headers, real-time messaging fails and users must refresh their browsers to see new messages.


TLS Certificate Options

Production deployments require TLS certificates. Three main options exist: Let's Encrypt, commercial certificates, and self-signed certificates.

Let's Encrypt provides free automated certificates. Certbot is the client tool that requests and installs Let's Encrypt certificates. Certbot can automatically configure NGINX with correct certificate paths. Certificates renew automatically every 90 days.

Let's Encrypt works for internet-accessible deployments. The Let's Encrypt service must validate domain ownership by connecting to your server. For internal deployments or air-gapped environments, Let's Encrypt is not suitable.

To use Let's Encrypt with Certbot:

Install Certbot:

apt install certbot python3-certbot-nginx

Request certificate:

certbot --nginx -d your_domain.com

Certbot configures NGINX automatically and sets up automatic renewal.

Commercial certificates from certificate authorities provide longer validity periods and may be required by organizational policies. Purchase certificates from providers like DigiCert, Sectigo, or GlobalSign. Install certificates manually in NGINX configuration.

Self-signed certificates work for testing and development. They provide encryption but browsers display security warnings because the certificate is not signed by a trusted authority. Generate self-signed certificates with OpenSSL:

openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes

Do not use self-signed certificates for production unless organizational policy requires private certificate authorities.

For classified environments, use certificates issued by organizational certificate authorities. Many defense and intelligence organizations operate internal certificate authorities. Request certificates through normal organizational processes. Install certificates in NGINX like commercial certificates.


NGINX Configuration Best Practices

Several best practices improve security and performance. Use TLS 1.2 and TLS 1.3 only. Disable older protocols like TLS 1.0 and TLS 1.1 which have known vulnerabilities.

In NGINX configuration:

ssl_protocols TLSv1.2 TLSv1.3;

Configure strong cipher suites. Use modern ciphers that provide forward secrecy. Disable weak ciphers like RC4 or DES.

Enable HTTP Strict Transport Security. HSTS tells browsers to always use HTTPS for your domain. This prevents downgrade attacks.

add_header Strict-Transport-Security "max-age=15768000" always;

The max-age value is in seconds. This example sets 6 months.

Set appropriate proxy timeouts. Mattermost operations can take time, especially file uploads. Configure timeouts to prevent premature connection closure:

proxy_read_timeout 90;
proxy_connect_timeout 90;
proxy_send_timeout 90;

For large file uploads, increase client_max_body_size. The default is often too small for practical use:

client_max_body_size 50M;

This allows file uploads up to 50 megabytes. Adjust based on organizational requirements.

Test NGINX configuration before reloading. NGINX provides a test command:

nginx -t

This checks configuration syntax without affecting the running service. If the test succeeds, reload NGINX to apply changes:

systemctl reload nginx

Regular reloads apply configuration changes without dropping existing connections.


Visual Asset Suggestions:
1. Reverse proxy architecture diagram showing users connecting to NGINX which forwards to Mattermost servers
2. TLS termination diagram showing encrypted connection to proxy and internal HTTP to Mattermost
3. Certificate options comparison table showing Let's Encrypt, commercial, and self-signed certificates with use cases


Video Opportunity: A 10-minute video walking through NGINX installation and configuration for Mattermost. Show installing NGINX, creating configuration file, obtaining Let's Encrypt certificate with Certbot, and testing the configuration. Demonstrate accessing Mattermost through NGINX with browser developer tools showing HTTPS connection. Show WebSocket connections in the network tab. Visual demonstration helps learners understand the complete process.


Knowledge Check Questions

Use Workramp Multiple Choice question object.

Question: A security operations center deploys Mattermost for incident response coordination. During peak incidents, users report that new messages do not appear automatically. They must refresh their browsers to see updates. Investigation shows HTTPS connections work correctly and message posting succeeds. What is the most likely NGINX configuration issue?

A. TLS certificates are self-signed instead of from certificate authority
B. NGINX worker_connections setting is too low for concurrent users
C. WebSocket proxy headers for Connection upgrade are missing
D. The upstream keepalive connection count is insufficient

Correct Answer: C

Explanation: Missing WebSocket proxy headers prevent real-time message delivery. Mattermost uses WebSocket for pushing new messages to clients. Without proper WebSocket configuration in NGINX, connections fall back to HTTP polling or fail entirely. Users see new messages only when refreshing. The required headers are Upgrade and Connection set to upgrade. Self-signed certificates cause browser warnings but do not affect WebSocket functionality. Low worker connections cause connection refusals. Insufficient keepalive affects performance but not WebSocket upgrades.

Hint: WebSocket configuration in NGINX is a critical exam topic. Remember that WebSocket connections start as HTTP and upgrade using specific headers. The proxy must forward these headers correctly. Without Upgrade and Connection headers, real-time messaging fails. This is one of the most common NGINX configuration mistakes. Symptoms are messages not appearing in real-time but appearing after browser refresh.

Key Takeaways: WebSocket support requires specific NGINX proxy headers for connection upgrades. Missing headers prevent real-time messaging while allowing standard HTTP requests. This is a common troubleshooting scenario in production deployments.


Use Workramp Multiple Choice question object.

Question: An intelligence agency is deploying Mattermost in an air-gapped environment at Impact Level 5. The deployment requires TLS encryption for all connections. Which certificate option is most appropriate?

A. Let's Encrypt with automated renewal via Certbot
B. Certificates issued by the agency's internal certificate authority
C. Self-signed certificates generated with OpenSSL
D. Commercial certificates from DigiCert requiring annual renewal

Correct Answer: B

Explanation: Air-gapped environments cannot access external certificate authorities like Let's Encrypt or DigiCert. Organizations operating classified systems typically run internal certificate authorities. Request certificates through organizational processes and install them in NGINX. Self-signed certificates work technically but cause browser warnings and do not integrate with organizational trust chains. Internal CA certificates are trusted by organizational systems through group policy or MDM configuration.

Hint: Air-gapped and classified environments cannot use external services. Let's Encrypt requires internet access for domain validation. Commercial CAs also require external connectivity for validation and revocation checking. Internal certificate authorities are standard in defense and intelligence environments. Remember that certificate trust must work within the isolated environment. OCSP and CRL checking must also work without internet access.

Key Takeaways: Air-gapped environments require internal certificate authorities. External certificate authorities require internet connectivity for validation. Organizations with classified systems typically operate internal CAs.


Use Workramp Select All That Apply question object.

Question: You are configuring NGINX as a reverse proxy for a production Mattermost deployment serving 3,000 users with high availability requirements. Which NGINX configuration elements are required for proper operation? Select all that apply.

A. Upstream backend servers configuration listing Mattermost servers and ports
B. WebSocket proxy headers for Upgrade and Connection to enable real-time messaging
C. TLS certificate paths and SSL protocols for encrypted connections
D. Rate limiting rules to prevent distributed denial of service attacks

Correct Answer: A, B, C

Explanation: Upstream backend configuration is required to tell NGINX where to send requests. WebSocket proxy headers are required for real-time messaging functionality. TLS certificate configuration is required for production security. Rate limiting is a best practice for security but not strictly required for operation. The proxy will function without rate limiting though it is recommended. The question asks for required elements, not recommended elements.

Hint: Distinguish between required configuration and recommended best practices. Required means the system will not function correctly without it. Recommended means the system functions but security or performance improves with it. Upstream, WebSocket headers, and TLS are required. Rate limiting, HSTS, and performance tuning are recommended. Certification exams often test your ability to distinguish required from optional configurations.

Key Takeaways: NGINX configuration requires upstream servers, WebSocket headers, and TLS certificates for production Mattermost deployments. Additional security controls are recommended but not required for basic operation. Understanding the difference between required and optional configuration is important.


________________________________________

Page Title: Module Complete

Page 7 of 7

Estimated Time: 1 minute

________________________________________


Module 1.0 Complete

You have completed Module 1.0: Deployment Preparations and can now:

Explain Mattermost three-layer architecture including Access Layer, Application Layer, and Backend Infrastructure components with understanding of how components communicate through HTTPS and WebSocket protocols.

Evaluate deployment methods including Kubernetes for production auto-scaling and high availability, Linux server installation for complete control and security hardening, and Docker containers for development and testing environments.

Plan database infrastructure using PostgreSQL version 14 or higher with knowledge of version compatibility timeline and nine-month notice policy for version requirements changes.

Select appropriate file storage solutions including S3-compatible object storage for production and high availability, Network File Storage using NFS for on-premises deployments, and local file storage for single-server development environments.

Prepare NGINX reverse proxy configuration for TLS termination, load balancing, and WebSocket support with understanding of certificate options including Let's Encrypt, commercial certificates, and organizational certificate authorities for classified environments.

Assess customer requirements and recommend appropriate architecture decisions for Mattermost deployments in Defense, Intelligence, Security, and Critical Infrastructure environments with consideration for security requirements, scale needs, and operational constraints.


Next Steps

Module 2.0: Linux Deployment Overview introduces hands-on deployment procedures. You will learn specific installation methods for generic Linux, Ubuntu package installation, and RHEL/CentOS installation. Each method includes step-by-step procedures, configuration guidance, and maintenance best practices.

The knowledge you gained in this module provides the foundation for understanding deployment decisions covered in subsequent modules. As you progress through hands-on installation modules, you will apply these preparation concepts to real deployment scenarios.


Visual Asset Suggestion: Module completion badge or certificate graphic showing Module 1.0 complete with checkmarks for each key competency area.
