# Deployment Guide

The below diagram illustrates an on-premises deployment of Mattermost with optional configurations for scaling to performance from teams to large organizations. 

![image](https://cloud.githubusercontent.com/assets/177788/13022821/9336477a-d198-11e5-8b98-6d967d253cfe.png)

## Requirements and Installation Guides 

Mattermost supports workplace messaging for teams using one to three servers using instructions available on [docs.mattermost.com](http://docs.mattermost.com/install/requirements.html). See [Software and Hardware Requirements](http://docs.mattermost.com/install/requirements.html) documentation for server sizing estimates. 

## User Experience

### PC Web Browser

End users can securely share messages and files using a web-based Mattermost experience in IE, Chrome and Firefox. Please see [Software and Hard Requirements](http://docs.mattermost.com/install/requirements.html) documentation for full details. 

### Native Mobile Applications

Note: At the time of this writing Android application has yet to be released. It should be released within the next two weeks.

Native applications for iOS and Android are available for interacting with the Mattermost server and receiving encrypted push notifications. 

#### Mobile Applications for Mattermost Enterprise Edition 

Customers of Mattermost Enterprise Edition have a convenience feature for using hosted versions of the iOS and Android applications provided by Mattermost.com, which includes 256-bit AES SSL encryption from the customer's server to the hosted Mattermost service (https://push.mattermost.com) and then from the service to the native mobile application on iOS or Android. 

Mattermost Enterprise Edition customers may also choose to compile, deploy and extend their own version of the mobile applications for their internal Enterprise App Store using open source repositories for the native applications: 

- Open source Mattermost iOS application 
- Open source Mattermost Android application 

#### Mobile Applications for Mattermost Team Edition 

Users of Mattermost Team Edition can compile the open source repositories for the native mobile applications to enable the same functionality offered in Enterprise Edition. 

In addition, for organizations evaluating whether to compile their own mobile applications or upgrade to Enterprise Edition, a test service (http://push-test.mattermost.com) is available to connect to and use the same pre-compiled iOS and Android applications available in iTunes and on Google Play for Enterprise Edition customers. The test service does not offer encryption and may have occassional downtime and is therefore not recommended for production. 

### Mobile Web Browser

End users can securely share messages and files using a web-mobiled-based Mattermost experience on iOS and Android devices. Please see [Software and Hard Requirements](http://docs.mattermost.com/install/requirements.html) documentation for full details. 


## Communication Protocols

### HTTPS Connection 

The HTTPS connection to the Mattermost server renders pages and provides core functionality. It does not include real time interactivity, which is offered by the WSS connection. 

If the HTTPS connection is not available, the Mattermost service will not work. HTTPS is a secure, encrypted connection and is highly recommended. An unencrypted HTTP connection may be used in initial testing and configuration but it is not recommended for production. 

### WSS Connection 

The WSS connection to the Mattermost server enables real time updates and notifications. If the WSS connection is not available, but HTTPS is available, the system will appear to work, but real time updates and notifications will be unavailable. Typically an error message will be displayed warning users that the Mattermost server is either unreachable or the WebSocket connection is not properly configured. 

WSS is a secure, encrypted connection and is highly recommended. An unencrypted WS connection may be used in initial testing and configuration but it is not recommended for production. 

## Data Center Infrastructure 

### Push Notification Service 

The [Mattermost Push Notification Service](https://github.com/mattermost/push-proxy) proxies push notifications from the Mattermost server to iOS and Android devices. The service component is [available as open source software](https://github.com/mattermost/push-proxy). A hosted version is available to customers of Mattermost Enterprise Edition to connect with reference implementations of the Mattermost iOS application on iTunes and the Mattermost Android application in the Google Play Store (release pending). 

The push notification service can be installed on the same physical machine as the Mattermost server. 

### Load Balancer

The load balancer manages Secure Socket Layer encryption and decides how network traffic will be routed to the Mattermost server. 

### Mattermost Server in High Availability Configuration (pre-released Enterprise Edition only)

Large organizations needing high scale, high availability configurations can contact the Enterprise team for advisory on how to configure and size Mattermost Enterprise Edition to support their specific needs. 


Please contact the [Mattermost Enteprise team](https://about.mattermost.com/contact/) to discuss a high availability configuration and hardware sizing guidance tailored to the needs of your organization. 

Depending on customer needs, multiple Mattermost servers may be configured with cache and event synchronization to horizontally scale the Mattermost service. 

