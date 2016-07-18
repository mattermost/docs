# Deployment Overview

The below diagram illustrates an on-premises deployment of Mattermost with optional configurations for scaling to performance from teams to large organizations.

![image](../images/network.PNG)

[View Mattermost Network Diagram](http://docs.mattermost.com/_images/network.PNG)

Notes: 
- Mattermost Enterprise Edition server in High Availability configuration available Q3, 2016.
- GitLab Mattermost deployment is [documented separately](http://doc.gitlab.com/omnibus/gitlab-mattermost/) and not included below.

## Requirements and Installation Guides

Mattermost supports workplace messaging for teams using one to three servers using instructions available on [docs.mattermost.com](http://docs.mattermost.com/install/requirements.html). See [Software and Hardware Requirements](http://docs.mattermost.com/install/requirements.html) documentation for server sizing estimates.

## User Experience

### PC Web Experience 

End users can securely share messages and files using a web-based Mattermost experience in IE, Chrome and Firefox. Please see [Software and Hardware Requirements](http://docs.mattermost.com/install/requirements.html) documentation for full details.

### Mobile App Experience

Native applications for iOS and Android are available for interacting with the Mattermost server and receiving encrypted push notifications from your private cloud. Organizations can use [a Hosted Push Notification Service](http://docs.mattermost.com/deployment/push.html#hosted-push-notifications-service-hpns) with encrypted communications to mobile apps on iTunes and Google Play, or deploy to an [Enterprise App Store](http://docs.mattermost.com/deployment/push.html#enterprise-app-store-eas) on your organization's private network. A [Test Push Notification Service](http://docs.mattermost.com/deployment/push.html#test-push-notifications-service-tpns) is available for use while evaluating options. 

### Mobile Web Experience 

End users can securely share messages and files using a web-mobiled-based Mattermost experience on iOS and Android devices. Please see [Software and Hardware Requirements](http://docs.mattermost.com/install/requirements.html) documentation for full details.

### Email Client 

Receive emails on desktop and mobile from the Mattermost server.

## Communication Protocols

### HTTPS Connection (Secure Hypertext Transfer Protocol)

The HTTPS connection to the Mattermost server renders pages and provides core functionality. It does not include real-time interactivity, which is enabled by the WSS connection.

If the HTTPS connection is not available, the Mattermost service will not work. HTTPS is a secure, encrypted protocol and is highly recommended for production. An unencrypted HTTP connection may be used in initial testing and configuration but it is not recommended for production.

### WSS Connection (Secure WebSocket Protocol)

The WSS connection to the Mattermost server enables real-time updates and notifications. If the WSS connection is not available, but HTTPS is available, the system will appear to work, but real time updates and notifications will not work. Updates will only appear on a page refresh. WSS will be a persistent connection to the Mattermost server while you are connected, while HTTPS will be intermittent depending on when you load a page or a file.

Typically a "Mattermost unreachable" error message will be displayed warning users that the Mattermost server is either unreachable or the WebSocket connection is not properly configured.

WSS is a secure, encrypted connection and is highly recommended. An unencrypted WS connection may be used in initial testing and configuration but it is not recommended for production.

## VPN Setup

Mattermost is designed to be deployed behind a firewall on your private network, with optional access from the outside over a Virtual Private Network (VPN). This means running a VPN client on PC and mobile devices accessing Mattermost.

An alternative option is to run Mattermost from outside your private network by opening standard ports, such as 80 or 443. If this option is taken it is recommended that desktop and mobile clients accessing Mattermost without a VPN use at least the multi-factor authentication feature included in Mattermost Enterprise Edition. 

## Data Center Infrastructure

### Push Notification Service

The [Mattermost Push Notification Service (MPNS)](http://docs.mattermost.com/deployment/push.html) routes push notifications to: 

1. Apple Push Notification Service to send notifications to the Mattermost iOS app. 
2. Google Push Notification Service to send notifications to the Mattermost Android app.

If you're deploying mobile applications to an Enterprise App Store, your MPNS should be behind your firewall on your private network. If you're using mobile apps in iTunes and Google Play, you can relay notifications to mobile apps using the [Hosted Push Notification Service (HPNS)](http://docs.mattermost.com/deployment/push.html#hosted-push-notifications-service-hpns) included with Mattermost Enterprise Edition. 

HPNS does not connect to your mobile apps directly, it sends messages over an encrypted channel to Apple or Google which are relayed to the app users download from iTunes or Google Play. 

### Proxy

The proxy manages Secure Socket Layer encryption and sets the policy on how network traffic will be routed to the Mattermost server.

Mattermost install guides include setup instructions for the NGNIX software proxy by default. For large scale deployments, a hardware proxy with dedicated devices for processing SSL encryption and decryption could potentially increase efficiencies.

In a high availability configuration (Enteprise Edition only) the proxy would also balance network load across multiple Mattermost servers.

### Microsoft Active Directory Single-Sign-On (Enterprise Edition) 

Mattermost Enterprise Edition supports Microsoft Active Directory and LDAP single-sign-on with secure transport over TLS or stunnel. 

### On-Premises Integrations

Mattermost offers complete access to its Web Service APIs, along with incoming and outgoing webhooks, and Slash command options for integrating with your on-premises systems.

Dozens of open source integrations to common tools like Jira, Jenkins, GitLab, Trac, Redmine, and SVN, along with interactive bot applications (Hubot, mattermost-bot), and other communication tools (Email, IRC, XMPP, Threema) are freely available for use and customization.

### Email Service

For notifications and account verification, Mattermost connects to your existing email service over SMTP, including Microsoft Exchange, Amazon SES, SendGrid and self-hosted email solutions.

## Mattermost Server

The Mattermost server installs as a single compiled binary file. All server settings are stored in a configuration file, `config/config.json`, which can be updated directly or via a web-based System Console user interface.

#### RESTful JSON Web Service

The entirety of the Mattermost server is accessible through a RESTful Web Service API. The API can be completely accessed by developers creating custom applications for Mattermost either directly or via Javascript and Golang drivers.

#### Authentication Client

Authenticates users by email or username plus password.

For customers of Enterprise Edition, single-sign-on via Microsoft Active Directory and LDAP is also available.

#### Authentication Provider

Enables authentication of Mattermost server to other services with Authentication Client interface using OAuth2.

#### Notification Service

Sends notifications via SMTP email and mobile push notifications via Mattermost Push Notificiation Service.

#### Data Management Service

Connects to and manages supported databases.

### High Availability (Enterprise Edition, available 2016)

Large organizations needing sophisticated, high scale, high availability configurations can contact the [Enterprise team](https://about.mattermost.com/contact/) for guidance on configuring and sizing Mattermost Enterprise Edition to support their specific needs. Multiple Mattermost servers may be configured with cache and event synchronization to horizontally scale the Mattermost service.

## Data Stores

### Databases

Mattermost uses a MySQL or Postgres database to store and retrieve system data and to execute full text search. Solid State Drives can be used for faster read times to increase performance. 

See [Database requirements](http://docs.mattermost.com/install/requirements.html#database-software) for full details. 

#### Multiple Read Replicas (Enterprise Edition) 

For enterprise deployments the Mattermost database can be configured with a master and multiple read replicas. The read replicas can be configured as a redundant backup to the active server, so that during hardware failures operation can be diverted to the read replica server without interrupting service. The safest configuration is to size the disk space on the read replica used for failover two to three times larger than storage available on master, so that if the master fails because it runs out of disk space it will fail over to a read replica with enough extra space to run smoothly until the master is corrected.

#### Global Deployments (Enterprise Edition, available 2016)

Enterprise customers with deployments spanning many time zones can contact the [Enterprise Team](https://about.mattermost.com/contact/) for advanced configurations to minimize latency by:    

1. Storing static assets over a global CDN.   
2. Deploying multiple Mattermost servers to host API communication closer to the location of end users.   
3. Deploying multiple database read replicas closer to the location of end users.   

### File Store

Images and files shared by users are stored and retrieved in one of three options.
    
1. For teams sharing only modest amounts of file data, local storage on the same physical machine as the Mattermost server may be sufficient.    
2. For enterprises sharing very large amounts of data, a Network-Attached Storage server may be used, which can scale to peta-bytes if necessary.    
3. Alternatively, for both ease-of-use and scale, Amazon's S3 file storage service is another option as well.

## Deployment Options 

Mattermost Enterprise Edition customers can contact Mattermost, Inc. for advisory on deployment options for their specific environments. The following section describes common deployment configurations. 

### Mobile devices with VPN clients (recommended) 

Mattermost can be deployed behind your company firewall on a private network with access from the outside via a Virtual Private Network (VPN). This means running a VPN client on the mobile devices and desktop computers that need to access Mattermost. 

The [Mattermost Push Notification Service](http://docs.mattermost.com/deployment/deployment.html#push-notification-service) (MPNS) should be behind your firewall on your private network. MPNS does not connect with mobile apps directly, it forwards push notifications from the Mattermost server to a relay service for iTunes or Google Play, or to mobile apps within an Enterprise App Store. 

### Mobile devices without VPN clients 

Mattermost can be deployed outside your private network by opening standard ports like 80 or 443. With this option, mobile clients and desktop computers access the Mattermost server without a VPN client, and it is recommended that users sign in with multi-factor authentication, available in Mattermost E10 and higher. 

The [Mattermost Push Notification Service](http://docs.mattermost.com/deployment/deployment.html#push-notification-service) (MPNS) should be behind your firewall inside your private network. MPNS does not connect with mobile apps directly, it forwards push notifications from the Mattermost server to a relay service for iTunes or Google Play, or directly to mobile apps within an Enterprise App Store behind your firewall. 

Certificate-based authentication for mobile devices is planned for Mattermost E20, [contact the Enterprise Sales Team for more information](https://about.mattermost.com/pricing/).
