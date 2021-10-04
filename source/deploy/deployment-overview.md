# Deployment Overview

The Mattermost network diagram below illustrates a private cloud deployment of Mattermost with optional configurations for scaling to performance from teams to large organizations.

![image](../images/network_diagram.png)

**Note**

  - GitLab Mattermost deployment is [documented separately](https://docs.gitlab.com/omnibus/gitlab-mattermost/) and not included below.

## Requirements and Installation Guides

Mattermost supports workplace messaging for teams using one to three servers with instructions available in the Install Guides section of this documentation. See [Software and Hardware Requirements](https://docs.mattermost.com/install/software-hardware-requirements.html) documentation for server sizing estimates.

## User Experience

### PC Web Experience

End users can securely share messages and files using a web-based Mattermost experience in Chrome, Firefox, Safari, and Edge. Please see [Software and Hardware Requirements](https://docs.mattermost.com/install/software-hardware-requirements.html) documentation for full details.

### Mobile App Experience

Native applications for iOS and Android are available for interacting with the Mattermost server and receiving encrypted push notifications from your private cloud. Organizations can use [a Hosted Push Notification Service](https://docs.mattermost.com/deploy/mobile-hpns.html#hosted-push-notifications-service-hpns) with encrypted communications to mobile apps on the App Store and Google Play, or deploy to an [Enterprise App Store](https://docs.mattermost.com/deployment/push.html#enterprise-app-store-eas) on your organization's private network. A [Test Push Notification Service](https://docs.mattermost.com/deploy/mobile-hpns.html#test-push-notifications-service-tpns) is available for use while evaluating options.

### Mobile Web Experience

End users can securely share messages and files using a mobile web-based Mattermost experience on iOS and Android devices. Please see [Software and Hardware Requirements](https://docs.mattermost.com/install/software-hardware-requirements.html) documentation for full details.

### Email Client

Receive emails on desktop and mobile from the Mattermost server.

## Communication Protocols

### HTTPS Connection (Secure Hypertext Transfer Protocol)

The HTTPS connection to the Mattermost server renders pages and provides core functionality. It does not include real-time interactivity, which is enabled by the WSS connection.

If the HTTPS connection is not available, the Mattermost service will not work. HTTPS is a secure, encrypted protocol and is highly recommended for production. An unencrypted HTTP connection may be used in initial testing and configuration but it is not recommended for production.

### WSS Connection (Secure WebSocket Protocol)

WSS is a secure, encrypted connection and is highly recommended. An unencrypted WSS connection may be used in initial testing and configuration but it is not recommended for production.

The WSS connection to the Mattermost server enables real-time updates and notifications. If the WSS connection is not available, but HTTPS is available, the system will appear to work, but real-time updates and notifications will not work. Updates will only appear on a page refresh. WSS will be a persistent connection to the Mattermost server while you are connected, while HTTPS will be intermittent depending on when you load a page or a file.

Typically a "Mattermost unreachable" error message will be displayed warning users that the Mattermost server is either unreachable or the WebSocket connection is not properly configured.

## Network Access and Multi-Factor Authentication

### Behind a VPN

Mattermost is intended to be installed within a private network which can offer multiple factors of authentication, including secure access to computing devices and physical locations.

If outside access is required, a virtual private network client (VPN), such as [OpenVPN](https://openvpn.net/), with additional authentication used to connect to Mattermost for web, desktop, and mobile experiences, is recommended.

### Non-VPN Setup

If Mattermost is accessible from the open internet, the following is recommended:

1. An IT admin should be assigned to set up appropriate network security, subscribe to [the Mattermost security bulletin](https://mattermost.com/security-updates/#sign-up), and [apply new security updates](https://docs.mattermost.com/upgrade/upgrading-mattermost-server.html).
2. The organization upgrades to [Mattermost Enterprise Edition](https://mattermost.com/pricing-self-managed/) to enable SAML Single Sign-on or enable MFA using Google Authenticator. For non-enterprise deployments, VPN is recommended.

If Mattermost is accessible from the open internet with no VPN or MFA set up, we recommended using it only for non-confidential, unimportant conversations where impact of a compromised system is not essential.

**Note** 

  Not-for-profit and academic institutions are eligible for special [not-for-profit](https://mattermost.com/nonprofit/) and [academic pricing](https://mattermost.com/education/) for Mattermost Enterprise Edition.

## Data Center Infrastructure

### Push Notification Service

The [Mattermost Push Notification Service (MPNS)](https://docs.mattermost.com/deploy/mobile-hpns.html#enable-mpns) routes push notifications to:

1. Apple Push Notification Service to send notifications to the Mattermost iOS app.
2. Google Push Notification Service to send notifications to the Mattermost Android app.

If you're deploying mobile applications to an Enterprise App Store, your MPNS should be behind your firewall on your private network. If you're using mobile apps in the App Store and Google Play, you can relay notifications to mobile apps using the [Hosted Push Notification Service (HPNS)](https://docs.mattermost.com/deploy/mobile-hpns.html#hosted-push-notifications-service-hpns) included with Mattermost Enterprise Edition.

HPNS does not connect to your mobile apps directly. It sends messages over an encrypted channel to Apple or Google which are relayed to the app users downloaded from the App Store or Google Play.

### Proxy

The proxy manages Secure Socket Layer (SSL) encryption and sets the policy on how network traffic will be routed to the Mattermost server.

Mattermost install guides include setup instructions for the NGNIX software proxy by default. For large scale deployments, a hardware proxy with dedicated devices for processing SSL encryption and decryption could potentially increase efficiencies.

In a High Availability configuration (Enterprise Edition only) the proxy would also balance network load across multiple Mattermost servers.

### Microsoft Active Directory Single Sign-On (Enterprise Edition)

Mattermost Enterprise Edition supports Microsoft Active Directory and LDAP Single Sign-on with secure transport over TLS or stunnel.

### Private Cloud Integrations

Mattermost offers complete access to its Web Service APIs, along with incoming and outgoing webhooks, and slash command options for integrating with your self-managed systems.

[Visit our app directory](https://mattermost.com/marketplace/#privateApps) for dozens of open source integrations to common tools like Jira, Jenkins, GitLab, Trac, Redmine, and SVN, along with interactive bot applications (Hubot, mattermost-bot), and other communication tools (Email, IRC, XMPP, Threema) that are freely available for use and customization.

### Email Service

For notifications and account verification, Mattermost connects to your existing email service over SMTP, including Microsoft Exchange, Amazon SES, SendGrid, and self-hosted email solutions.

## Mattermost Server

The Mattermost server installs as a single compiled binary file. All server settings are stored in a configuration file, ``config/config.json``, which can be updated directly or via the web-based System Console user interface.

#### RESTful JSON Web Service

The entirety of the Mattermost server is accessible through a RESTful Web Service API. The API can be completely accessed by developers creating custom applications for Mattermost either directly or via Javascript and Golang drivers.

#### Authentication Client

Authenticates users by email or username plus password.

For customers of Enterprise Edition, Single Sign-on via Microsoft Active Directory and LDAP is also available.

#### Authentication Provider

Enables authentication of Mattermost server to other services with Authentication Client interface using OAuth2.

#### Notification Service

Sends notifications via SMTP email and mobile push notifications via Mattermost Push Notificiation Service.

#### Data Management Service

Connects to and manages supported databases.

### High Availability (Enterprise Edition)

Large organizations needing sophisticated, large scale, High Availability configurations can set up a [highly available, horizontally scalable](https://docs.mattermost.com/scale/high-availability-cluster.html) deployment. Contact the [Enterprise team](https://mattermost.com/contact-us/) for guidance on configuring and sizing Mattermost Enterprise Edition to support your specific needs.

## Data Stores

### Databases

Mattermost uses a MySQL or Postgres database to store and retrieve system data and to execute full text search. Solid State Drives (SSDs) can be used for faster read times to increase performance.

See [Database requirements](https://docs.mattermost.com/install/software-hardware-requirements.html#database-software) for full details.

#### Multiple Read Replicas (Enterprise Edition)

For enterprise deployments, the Mattermost database can be configured with a master and multiple read replicas. The read replicas can be configured as a redundant backup to the active server, so that during hardware failures operation can be diverted to the read replica server without interrupting service. 

The safest configuration is to size the disk space on the read replica used for failover two to three times larger than storage available on master, so that if the master fails because it runs out of disk space it will fail over to a read replica with enough extra space to run smoothly until the master is corrected.

#### Search Replicas (Enterprise Edition)

You can configure one or more search replicas to isolate search queries. A search replica is similar to a read replica, but is used only for handling search queries.

#### Global Deployments (Enterprise Edition)

Enterprise customers with deployments spanning many time zones can contact the [Enterprise team](https://mattermost.com/contact-us/) for advanced configurations to minimize latency by:

1. Storing static assets over a global CDN.
2. Deploying multiple Mattermost servers to host API communication closer to the location of end users.
3. Deploying multiple database read replicas closer to the location of end users.

### File Store

Images and files shared by users are stored and retrieved in one of three options.

1. For teams sharing only modest amounts of file data, local storage on the same physical machine as the Mattermost server may be sufficient.
2. For enterprises sharing very large amounts of data, a Network Attached Storage (NAS) server may be used, which can scale to petabytes if necessary.
3. Alternatively, for both ease-of-use and scale, a third option is to use Amazon's S3 file storage service.

## Deployment Options

Mattermost Enterprise Edition customers can contact Mattermost, Inc. for advice on deployment options for their specific environments. The following section describes common deployment configurations.

### Mobile Devices with VPN Clients (recommended)

Mattermost can be deployed behind your company firewall on a private network with access from the outside via a Virtual Private Network (VPN). This means running a VPN client on the mobile devices and desktop computers that need to access Mattermost.

The [Mattermost Push Notification Service](https://docs.mattermost.com/deploy/deployment-overview.html#push-notification-service) (MPNS) should be behind your firewall on your private network. MPNS does not connect with mobile apps directly, it forwards push notifications from the Mattermost server to a relay service for the App Store or Google Play, or to mobile apps within an Enterprise App Store.

### Mobile Devices without VPN Clients

If Mattermost is available on the internet, we recommend Mattermost Enterprise Edition featuring SAML-based Single Sign-on and multi-factor authentication (MFA) using Google Authenticator.

The [Mattermost Push Notification Service](https://docs.mattermost.com/deploy/deployment-overview.html#push-notification-service) (MPNS) should be behind your firewall inside your private network. MPNS does not connect with mobile apps directly, it forwards push notifications from the Mattermost server to a relay service for App Store or Google Play, or directly to mobile apps within an Enterprise App Store behind your firewall.

For support for certificate-based authentication for mobile devices, [contact the Enterprise Sales team for more information](https://mattermost.com/contact-us/).

### Mobile Devices with an EMM Provider

Mattermost mobile applications can also be deployed via [EMM providers who support AppConfig](https://docs.mattermost.com/deploy/mobile-appconfig.html) such as Blackberry UEM, Mobileiron, and Airwatch. EMM solutions typically offer "App Tunnel" or per-app VPN capabilities that can be used to connect to mobile apps behind a VPN.
