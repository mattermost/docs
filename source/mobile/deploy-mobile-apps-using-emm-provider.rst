Deploying Mobile Apps Using an EMM Provider
===========================================

An EMM Provider builds `Enterprise Mobile Management software <https://en.wikipedia.org/wiki/Enterprise_mobility_management>`__ that helps enterprise teams manage secure mobile endpoints with managed app configuration. 

You can use an EMM to: 

- Enforce users to download a mobile app.
- Set default server connections.
- Restrict users from changing servers.
- Enforce security policies.

An EMM provider pushes Mattermost Mobile apps to EMM-enrolled devices. This approach is recommended for organizations that typically use EMM solutions to deploy Mobile apps to meet security and compliance policies. 

Manage App Configuration Using AppConfig
----------------------------------------

AppConfig is our recommended approach for app configuration and management. It was introduced by the `AppConfig Community <https://www.appconfig.org/about/>`__, a group of leading EMM providers and app developers who have come together to make it easier for developers and customers to drive mobility in business. 

AppConfig provides an easy way to configure enterprise mobile apps with any of the EMM providers listed on the `AppConfig website <https://www.appconfig.org/members/>`__. Using AppConfig, you can manage default settings and security controls on both the public app stores, and custom-built mobile clients. For example, you can pre-configure your Mattermost Server URL and username.

See our `Mattermost AppConfig Values <https://docs.mattermost.com/mobile/mobile-appconfig.html#mattermost-appconfig-values>`__ documentation for details on the configuration options that can be sent from the EMM provider to Mattermost Mobile apps. 

.. important::
    Mattermost only supports the AppConfig standard for securing Mattermost Mobile apps via an EMM provider due to incompatibilities with app wrapping and React Native applications. React Native is the technology used to develop the Mattermost Mobile apps. Different EMM vendors refer to “wrapping” in different ways, but it ultimately comes down to unpacking the mobile client bundle, injecting additional SDKs, and re-packaging/re-signing. 

    Mattermost Mobile apps will not function properly when using app wrapping (e.g., Websockets for real-time messaging will break). Mattermost doesn’t support app wrapping, so use app wrapping/containerization technology at your own risk.

Connecting to your Private Network Mattermost Instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to set up a way to connect to your private network Mattermost instance, using an external proxy with encrypted transport through HTTPS and WSS network connections.

Depending on your security policies, we recommend deploying Mattermost behind a VPN and using a per-app VPN with your EMM provider, or a mobile VPN client.

Also consider deploying a mobile VPN client with multi-factor authentication (MFA) to your preferred login method, such as, GitLab SSO with MFA, or run Mattermost Enterprise Edition with MFA.

Host Your Own Push Proxy Service
--------------------------------

A push proxy is a key technology behind notification transmission. It enables notifications between the server and a Mobile app. Mattermost provides a self-hosted push proxy you can deploy called the `Mattermost Push Notification Service (MPNS) <https://docs.mattermost.com/deployment/deployment.html#push-notification-service>`__. However, if you choose to build custom versions of the Mattermost Mobile app, you must host your own instance of the MPNS by compiling your own MPNS from the `open source repository <https://github.com/mattermost/mattermost-push-proxy>`__, or by using the `pre-compiled version available on GitHub <https://github.com/mattermost/mattermost-push-proxy/releases>`__. 

See our `developer documentation <https://developers.mattermost.com/contribute/mobile/push-notifications/service/>`__ on installing the Mattermost Push Notification Service for details.

.. note::

- The MPNS should be behind your firewall inside your private network, or in your DMZ such that the Mattermost Server can access it. 
- The MPNS does not connect with Mobile apps directly; it parses and forwards push notifications from the Mattermost Server to the Apple Push Notification Service (APNS) or the Firebase Cloud Messaging (FCM). 
- The MPNS must be able to communicate with the Apple Push Notification Service over http2. If an outbound proxy appliance is deployed between the MPNS and APNS please ensure it supports http2.
  
Securing Push Notifications
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To secure your push notifications, make sure to use encrypted TLS connections between:

- MPNS and Apple Push Notification Service
- MPNS and Google’s Firebase Cloud Messaging
- MPNS and your Mattermost Server

Enabling MPNS in Mattermost
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to **System Console > Environment > Push Notification Server**.
2. Under **Enable Push Notifications**, select **Manually enter Push Notification Service location**.
3. Enter the location of your MPNS in the **Push Notification Server**  field, then select **Save**.
4. (Optional) Customize mobile push notification contents. Most deployments choose to include the full message content sent in the notification payload.
    a. Go to **System Console > Site Configuration > Notifications**.
    b. Under **Push Notification Contents**, select the type of information to include in push notifications, then select **Save**.
5. Subscribe to `Mattermost Security Bulletins <https://mattermost.com/security-updates/#sign-up>`__. When notified of security updates, apply them promptly.

.. note:: 

    As part of the process of building the applications you will need to sign the applications. You must also obtain the appropriate certificate for both Android and iOS. If this is not done, the applications will not be able to interact with your instance of the MPNS. Once this is complete, you can proceed with the deployment of your MPNS instance.

Enroll Devices
--------------

When building your own custom versions of Mattermost Mobile apps, consider your organization’s mobile policy:

- Can users bring their own device (BYOD) If so, what devices will be used?
- Are devices company-owned and company-issued?
- Are both options supported?
- What operating systems do you want to start testing?

Once you know what possible device configurations you’ll be supporting, consider creating a sample configuration, then running validation tests against each configuration item.

Generate and Assign Device Profiles
-----------------------------------

Generate and assign a device profile for device-wide configurations through the EMM provider.

Consider Mobile VPN Options
---------------------------

A Virtual Private Network (VPN) allows a device outside a firewall to access content inside the firewall as if it were on the same network. Most enterprise teams are familiar with VPNs, so we won’t go into many VPN details here. 

.. note::

    Some mobile VPN options depend on the requirements of your organization and the demands and/or the needs of your users. 

We recommend one of two options: `per-app VPN <#per-app-vpn>`_ or a `device VPN <#device-vpn>`_ to secure your deployment. Both options are compatible with most EMM providers. 

We also recommend following our `recommended steps to secure your deployment <https://docs.mattermost.com/mobile/mobile-appstore-install.html>`__ and to review the following Frequently Asked Questions about data security on mobile devices:

- `How data is handled on a device after an account is deleted? <https://docs.mattermost.com/mobile/mobile-faq.html#how-is-data-handled-on-mobile-devices-after-a-user-account-is-deactivated>`__
- `What post metadata is sent in mobile push notifications? <https://docs.mattermost.com/mobile/mobile-faq.html#what-post-metadata-is-sent-in-mobile-push-notifications>`__
- `What are my options for securing the Mobile apps? <https://docs.mattermost.com/mobile/mobile-faq.html#what-are-my-options-for-securing-the-mobile-apps>`__
- `What are my options for securing push notifications? <https://docs.mattermost.com/mobile/mobile-faq.html#what-are-my-options-for-securing-push-notifications>`__

Per-app VPN
~~~~~~~~~~~

A common approach is to use a per-app VPN. This provides a connection to the VPN when needed (on-demand). If using a per-app VPN with Mattermost, you can configure the following options:

- **useVPN**: Mattermost waits until the connection to the VPN server is established before making any requests (otherwise they will fail). Only supported on iOS given Android OS cannot support waiting - still works but the first connection attempt may fail. 
- **timeoutVPN** (iOS only): How long to wait for the connection to the VPN server before trying.

Device VPN
~~~~~~~~~~

With this option, all internet traffic routes through the VPN specified in the profile. This could cause issues for personal applications.

Connecting via Corporate Proxy Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Review the following Frequently Asked Questions about connecting through a corporate proxy server:

- `How do I receive mobile push notifications if my IT policy requires the use of a corporate proxy server? <https://docs.mattermost.com/mobile/mobile-faq.html#how-do-i-receive-mobile-push-notification-if-my-it-policy-requires-the-use-of-a-corporate-proxy-server>`__
- `Deploy Mattermost with connection restricted post-proxy relay in DMZ or a trusted cloud environment <https://docs.mattermost.com/mobile/mobile-faq.html#deploy-mattermost-with-connection-restricted-post-proxy-relay-in-dmz-or-a-trusted-cloud-environment>`__
- `Whitelist Mattermost push notification proxy to bypass your corporate proxy server <https://docs.mattermost.com/mobile/mobile-faq.html#whitelist-mattermost-push-notification-proxy-to-bypass-your-corporate-proxy-server>`__
- `Run App Store versions of the Mattermost Mobile apps <https://docs.mattermost.com/mobile/mobile-faq.html#run-app-store-versions-of-the-mattermost-mobile-apps>`__
