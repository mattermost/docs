Deploying Mobile Apps Using an EMM Provider
===========================================

`Enterprise Mobile Management software <https://en.wikipedia.org/wiki/Enterprise_mobility_management>`__ helps enterprise teams manage secure mobile endpoints with managed app configuration. 

You can use an EMM to: 

- Enforce users to download the Mattermost pre-built or custom apps managed by your organization.
- Set default server url address.
- Restrict users from changing servers.
- Enforce security policies.

An EMM provider pushes Mattermost Mobile apps to EMM-enrolled devices. This approach is recommended for organizations that typically use EMM solutions to deploy Mobile apps to meet security and compliance policies. 

Manage App Configuration Using AppConfig
----------------------------------------

AppConfig is our recommended approach for app configuration and management. It was introduced by the `AppConfig Community <https://www.appconfig.org/about/>`__, a group of leading EMM providers and app developers who have come together to make it easier for developers and customers to drive mobility in business. 

AppConfig provides an easy way to configure enterprise mobile apps with any of the EMM providers listed on the `AppConfig website <https://www.appconfig.org/members/>`__. Using AppConfig, you can manage default settings and security controls on both the public app stores, and custom-built mobile clients. For example, you can pre-configure your Mattermost server URL and username.

See our `Mattermost AppConfig Values <https://docs.mattermost.com/mobile/mobile-appconfig.html#mattermost-appconfig-values>`__ documentation for details on the configuration options that can be sent from the EMM provider to Mattermost Mobile apps. 

.. important::
    
    Mattermost only supports the AppConfig standard for securing Mattermost Mobile apps via an EMM provider due to incompatibilities with app wrapping and React Native applications. React Native is the technology used to develop the Mattermost Mobile apps. Different EMM vendors refer to “wrapping” in different ways, but it ultimately comes down to unpacking the mobile client bundle, injecting additional SDKs, and re-packaging/re-signing. 

    Mattermost doesn’t support app wrapping, and Mattermost Mobile apps won't function properly when using app wrapping (e.g., Websockets for real-time messaging will break). Use app wrapping/containerization technology at your own risk.

Connecting to your Private Network Mattermost Instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You need to set up a way to connect to your private network Mattermost instance, using an external proxy with encrypted transport through HTTPS and WSS network connections.

Depending on your security policies, we recommend deploying Mattermost behind a VPN and using a per-app VPN with your EMM provider, or a mobile VPN client.

Also consider deploying a mobile VPN client with multi-factor authentication (MFA) to your preferred login method, such as GitLab SSO with MFA, or run Mattermost Enterprise Edition with MFA.

Enroll Devices
--------------

When building your own custom versions or deploying the pre-built Mattermost Mobile apps, consider your organization’s mobile policy:

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

A Virtual Private Network (VPN) allows a device outside a firewall to access content inside the firewall as if it were on the same network.

.. note::

    Some mobile VPN options depend on the requirements of your organization and the demands and/or the needs of your users. 

We recommend one of two options: `per-app VPN <#per-app-vpn>`_ or a `device VPN <#device-vpn>`_ to secure your deployment. Both options are compatible with most EMM providers. 

We also recommend following our `recommended steps to secure your deployment <https://docs.mattermost.com/mobile/mobile-appstore-install.html>`__ and to review the following commonly-asked questions about data security on mobile devices:

- `How data is handled on a device after an account is deleted? <https://docs.mattermost.com/mobile/mobile-faq.html#how-is-data-handled-on-mobile-devices-after-a-user-account-is-deactivated>`__
- `What post metadata is sent in mobile push notifications? <https://docs.mattermost.com/mobile/mobile-faq.html#what-post-metadata-is-sent-in-mobile-push-notifications>`__
- `What are my options for securing the Mobile apps? <https://docs.mattermost.com/mobile/mobile-faq.html#what-are-my-options-for-securing-the-mobile-apps>`__
- `What are my options for securing push notifications? <https://docs.mattermost.com/mobile/mobile-faq.html#what-are-my-options-for-securing-push-notifications>`__

Per-app VPN
~~~~~~~~~~~

A common approach is to use a per-app VPN. This provides a connection to the VPN when needed (on-demand). If using a per-app VPN with Mattermost, you can configure the following options:

- **useVPN:** Mattermost waits until the connection to the VPN server is established before making any requests (otherwise they will fail). This is only supported on iOS as Android OS cannot support waiting. It still works but the first connection attempt may fail.
- **timeoutVPN (iOS only):** How long to wait for the connection to the VPN server before trying.

Device VPN
~~~~~~~~~~

With this option, all internet traffic routes through the VPN specified in the profile. This could cause issues for personal applications.

Connecting via Corporate Proxy Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Review the following commonly-asked questions about connecting through a corporate proxy server:

- `How do I receive mobile push notifications if my IT policy requires the use of a corporate proxy server? <https://docs.mattermost.com/mobile/mobile-faq.html#how-do-i-receive-mobile-push-notification-if-my-it-policy-requires-the-use-of-a-corporate-proxy-server>`__
- `Deploy Mattermost with connection restricted post-proxy relay in DMZ or a trusted cloud environment <https://docs.mattermost.com/mobile/mobile-faq.html#deploy-mattermost-with-connection-restricted-post-proxy-relay-in-dmz-or-a-trusted-cloud-environment>`__
- `Whitelist Mattermost push notification proxy to bypass your corporate proxy server <https://docs.mattermost.com/mobile/mobile-faq.html#whitelist-mattermost-push-notification-proxy-to-bypass-your-corporate-proxy-server>`__
- `Run App Store versions of the Mattermost Mobile apps <https://docs.mattermost.com/mobile/mobile-faq.html#run-app-store-versions-of-the-mattermost-mobile-apps>`__
